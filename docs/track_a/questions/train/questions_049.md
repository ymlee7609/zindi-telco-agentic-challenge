# Track A 문제 분석 — train[480]~train[489]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[480] ~ train[489] (10개)

## 목차

1. [문제 480: `90298dfe-7a7...`](#480) — single-answer, 정답: C21
2. [문제 481: `c91defb8-e3b...`](#481) — single-answer, 정답: C18
3. [문제 482: `e0fb399e-ef2...`](#482) — single-answer, 정답: C13
4. [문제 483: `b7ded16d-e81...`](#483) — multiple-answer, 정답: C16|C20
5. [문제 484: `1fac1919-14c...`](#484) — multiple-answer, 정답: C1|C20
6. [문제 485: `c6a3f5da-d1e...`](#485) — multiple-answer, 정답: C7|C13
7. [문제 486: `519321fa-ee6...`](#486) — single-answer, 정답: C3
8. [문제 487: `9887eb61-f04...`](#487) — single-answer, 정답: C7
9. [문제 488: `4cef1e1a-6c1...`](#488) — single-answer, 정답: C8
10. [문제 489: `12f2cce3-616...`](#489) — single-answer, 정답: C18

---

### 문제 480: `90298dfe-7a7...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `90298dfe-7a71-456b-bfbd-a8fb60745e65` |
| Tag | **single-answer** |
| 정답 | **C21** |
| C21 의미 | Decrease A3 Offset threshold for 3217637_4 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[480] topology](images/train_0480.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3268431_2 by 50 degrees
- `C2`: Increase A3 Offset threshold for 3268431_2
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3268431_2
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3217637_4
- `C5`: Lift the tilt angle of 3217637_4 by 10 degrees
- `C6`: Increase transmission power for 3268431_2
- `C7`: Press down the tilt angle  of 3268431_2 by 6 degrees
- `C8`: Decrease transmission power for 3217637_4
- `C9`: Lift the tilt angle  of 3268431_2 by 6 degrees
- `C10`: Increase transmission power for 3217637_4
- `C11`: Check test server and transmission issues
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3217637_4
- `C13`: Increase A3 Offset threshold for 3217637_4
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Decrease A3 Offset threshold for 3268431_2
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3268431_2
- `C17`: Press down the tilt angle of 3217637_4 by 10 degrees
- `C18`: Add neighbor relationship between 3217637_4 and 3268431_2
- `C19`: Adjust the azimuth of 3217637_4 by 50 degrees
- `C20`: Decrease transmission power for 3268431_2
- `C21`: Decrease A3 Offset threshold for 3217637_4 **← 정답**
- `C22`: Add neighbor relationship between 3242299_1 and 3268431_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.578 | MS1 | 121.4656653633 | 31.1446331348 | 446 | 504990 | -81.00 | 16.08 | 482.26 | 0.07 | 2.62 | 1576 |
| 2024-09-20 22:21:32.144 | MS1 | 121.4656588723 | 31.1446327621 | 446 | 504990 | -81.78 | 14.38 | 475.68 | 0.02 | 2.28 | 1562 |
| 2024-09-20 22:21:33.398 | MS1 | 121.4656634365 | 31.1446198535 | 446 | 504990 | -75.93 | 13.13 | 405.77 | 0.03 | 2.68 | 1577 |
| 2024-09-20 22:21:34.518 | MS1 | 121.4656669144 | 31.1446360323 | 446 | 504990 | -86.56 | -2.85 | 26.40 | 0.05 | 1.06 | 1590 |
| 2024-09-20 22:21:35.449 | MS1 | 121.4656704778 | 31.1446370492 | 446 | 504990 | -85.90 | -1.68 | 34.24 | 0.03 | 1.25 | 1565 |
| 2024-09-20 22:21:36.918 | MS1 | 121.4656760132 | 31.1446314737 | 446 | 504990 | -90.07 | -1.07 | 77.71 | 0.18 | 1.26 | 1573 |
| 2024-09-20 22:21:37.316 | MS1 | 121.4656745093 | 31.1446360700 | 446 | 504990 | -83.32 | -0.07 | 40.14 | 0.16 | 1.33 | 1580 |
| 2024-09-20 22:21:38.808 | MS1 | 121.4656740919 | 31.1446298637 | 446 | 504990 | -84.72 | -2.64 | 35.22 | 0.19 | 1.00 | 1590 |
| 2024-09-20 22:21:39.347 | MS1 | 121.4656745399 | 31.1446194477 | 931 | 504990 | -80.68 | 16.26 | 285.41 | 0.14 | 1.04 | 1572 |
| 2024-09-20 22:21:40.534 | MS1 | 121.4656616418 | 31.1446223405 | 931 | 504990 | -81.54 | 13.47 | 340.37 | 0.05 | 2.22 | 1567 |
| 2024-09-20 22:21:41.590 | MS1 | 121.4656685826 | 31.1446308176 | 931 | 504990 | -78.51 | 13.07 | 562.53 | 0.11 | 2.44 | 1568 |
| 2024-09-20 22:21:42.253 | MS1 | 121.4656601147 | 31.1446214194 | 931 | 504990 | -83.88 | 17.42 | 495.32 | 0.09 | 2.68 | 1589 |

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
| 3217637 | 4 | 121.4685182948 | 31.1459496529 | 162 | 14 | 12 | 15.7 | TDD | 446 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3242299 | 1 | 121.4678063426 | 31.1551498072 | 344 | 1 | 4 | 17.4 | TDD | 73 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3252523 | 3 | 121.4691714886 | 31.1497060254 | 121 | 12 | 12 | 39.0 | TDD | 285 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3268431 | 2 | 121.4650514642 | 31.1494534088 | 275 | 3 | 7 | 30.3 | TDD | 931 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |

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
| 2024-09-20 22:21:30.753 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.771 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:30.896 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.896 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.634 | NREventA3 | measId:2;ServCellPCI:197;Se... |
| 2024-09-20 22:21:37.874 | NRHandoverAttempt | SourcePCI:197;SourceNR-ARFC... |
| 2024-09-20 22:21:37.918 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.930 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.062 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.062 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3242299 | 1 | 6.9145 | 10.2601 | -115.9549 | 10.0158 | 98.3669 | 0.0113 | 0.0023 |
| 2024_09_20 22:00 | 3268431 | 2 | 11.7506 | 10.7021 | -116.9406 | 16.3523 | 131.7569 | 0.0097 | 0.0193 |
| 2024_09_20 22:00 | 3252523 | 3 | 19.1162 | 16.7197 | -116.9731 | 19.3509 | 167.4210 | 0.0095 | 0.0124 |
| 2024_09_20 22:00 | 3217637 | 4 | 13.0815 | 10.2992 | -117.1809 | 15.2597 | 143.4288 | 0.0105 | 0.1252 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416011_C007CE1A | 504990 | 446 | -86.2 | 504990 | 931 | -83.1 | 504990 | 73 | -89.0 | 504990 | 285 |
| MR_1774416011_9475915E | 504990 | 446 | -86.9 | 504990 | 931 | -82.2 | 504990 | 73 | -87.4 | 504990 | 285 |
| MR_1774416011_6B31F35B | 504990 | 446 | -86.1 | 504990 | 931 | -82.7 | 504990 | 73 | -86.7 | 504990 | 285 |
| MR_1774416011_0E6DE0CC | 504990 | 931 | -82.9 | 504990 | 446 | -88.0 | 504990 | 73 | -87.1 | 504990 | 285 |
| MR_1774416011_8405C3AF | 504990 | 931 | -80.6 | 504990 | 446 | -85.3 | 504990 | 73 | -89.7 | 504990 | 285 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 481: `c91defb8-e3b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `c91defb8-e3bf-447d-885a-3467c92c89a7` |
| Tag | **single-answer** |
| 정답 | **C18** |
| C18 의미 | Decrease A3 Offset threshold for 3213025_1 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[481] topology](images/train_0481.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3232768_2 by 10 degrees
- `C2`: Add neighbor relationship between 3258123_4 and 3232768_2
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3213025_1
- `C4`: Increase transmission power for 3232768_2
- `C5`: Lift the tilt angle of 3213025_1 by 10 degrees
- `C6`: Insufficient data; more data is needed for judgment.
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3213025_1
- `C8`: Adjust the azimuth of 3232768_2 by 50 degrees
- `C9`: Adjust the azimuth of 3213025_1 by 50 degrees
- `C10`: Increase A3 Offset threshold for 3213025_1
- `C11`: Decrease A3 Offset threshold for 3232768_2
- `C12`: Press down the tilt angle of 3213025_1 by 10 degrees
- `C13`: Lift the tilt angle  of 3232768_2 by 10 degrees
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3232768_2
- `C15`: Increase A3 Offset threshold for 3232768_2
- `C16`: Add neighbor relationship between 3213025_1 and 3232768_2
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3232768_2
- `C18`: Decrease A3 Offset threshold for 3213025_1 **← 정답**
- `C19`: Increase transmission power for 3213025_1
- `C20`: Check test server and transmission issues
- `C21`: Decrease transmission power for 3232768_2
- `C22`: Decrease transmission power for 3213025_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.926 | MS1 | 121.4656673680 | 31.1446185763 | 65 | 504990 | -80.14 | 17.32 | 396.80 | 0.07 | 2.63 | 1577 |
| 2024-09-20 22:21:32.420 | MS1 | 121.4656744048 | 31.1446182548 | 65 | 504990 | -75.08 | 16.38 | 343.95 | 0.04 | 2.57 | 1600 |
| 2024-09-20 22:21:33.831 | MS1 | 121.4656704415 | 31.1446345531 | 65 | 504990 | -75.31 | 15.92 | 389.98 | 0.03 | 2.23 | 1577 |
| 2024-09-20 22:21:34.400 | MS1 | 121.4656672600 | 31.1446257929 | 65 | 504990 | -84.30 | -1.46 | 58.13 | 0.05 | 1.11 | 1567 |
| 2024-09-20 22:21:35.505 | MS1 | 121.4656690990 | 31.1446227988 | 65 | 504990 | -90.35 | -1.85 | 30.56 | 0.17 | 1.30 | 1561 |
| 2024-09-20 22:21:36.663 | MS1 | 121.4656649084 | 31.1446299029 | 65 | 504990 | -89.74 | -2.26 | 62.21 | 0.18 | 1.24 | 1564 |
| 2024-09-20 22:21:37.475 | MS1 | 121.4656612990 | 31.1446204437 | 65 | 504990 | -89.59 | -2.94 | 76.18 | 0.10 | 1.22 | 1589 |
| 2024-09-20 22:21:38.201 | MS1 | 121.4656735527 | 31.1446227384 | 65 | 504990 | -85.10 | -3.09 | 50.26 | 0.12 | 1.34 | 1598 |
| 2024-09-20 22:21:39.912 | MS1 | 121.4656736049 | 31.1446301266 | 489 | 504990 | -82.35 | 12.54 | 174.12 | 0.14 | 1.48 | 1595 |
| 2024-09-20 22:21:40.151 | MS1 | 121.4656713412 | 31.1446334554 | 489 | 504990 | -79.34 | 14.50 | 526.42 | 0.05 | 2.41 | 1570 |
| 2024-09-20 22:21:41.169 | MS1 | 121.4656605561 | 31.1446345381 | 489 | 504990 | -75.75 | 16.72 | 309.80 | 0.17 | 2.91 | 1589 |
| 2024-09-20 22:21:42.876 | MS1 | 121.4656761570 | 31.1446187905 | 489 | 504990 | -79.47 | 17.77 | 335.33 | 0.07 | 2.07 | 1580 |

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
| 3213025 | 1 | 121.4725010831 | 31.1458526099 | 85 | 7 | 0 | 31.0 | TDD | 65 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3232768 | 2 | 121.4693836466 | 31.1545839414 | 296 | 9 | 2 | 21.9 | TDD | 489 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3258123 | 4 | 121.4725152607 | 31.1443278718 | 165 | 4 | 9 | 20.6 | TDD | 510 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3265047 | 3 | 121.4732823102 | 31.1515523177 | 195 | 2 | 8 | 34.0 | TDD | 734 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |

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
| 2024-09-20 22:21:31.164 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.179 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.318 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.318 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.999 | NREventA3 | measId:2;ServCellPCI:413;Se... |
| 2024-09-20 22:21:38.239 | NRHandoverAttempt | SourcePCI:413;SourceNR-ARFC... |
| 2024-09-20 22:21:38.269 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.283 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.426 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.426 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3213025 | 1 | 11.9399 | 15.9344 | -115.6922 | 15.7296 | 183.9111 | 0.0019 | 0.1445 |
| 2024_09_20 22:00 | 3232768 | 2 | 5.8210 | 7.3514 | -115.9166 | 12.7936 | 180.3268 | 0.0175 | 0.0090 |
| 2024_09_20 22:00 | 3265047 | 3 | 15.5743 | 14.9871 | -114.5429 | 11.3786 | 137.8629 | 0.0159 | 0.0151 |
| 2024_09_20 22:00 | 3258123 | 4 | 9.4551 | 17.2289 | -117.2094 | 13.7936 | 125.1841 | 0.0037 | 0.0133 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413890_6F771FB7 | 504990 | 65 | -84.2 | 504990 | 489 | -78.8 | 504990 | 510 | -86.9 | 504990 | 734 |
| MR_1774413890_C68E8E4D | 504990 | 489 | -79.3 | 504990 | 65 | -85.9 | 504990 | 510 | -86.6 | 504990 | 734 |
| MR_1774413890_41E1850E | 504990 | 489 | -79.1 | 504990 | 65 | -84.3 | 504990 | 510 | -85.9 | 504990 | 734 |
| MR_1774413890_65A62FDE | 504990 | 489 | -81.2 | 504990 | 65 | -84.5 | 504990 | 510 | -87.4 | 504990 | 734 |
| MR_1774413890_7B4D4A35 | 504990 | 65 | -84.0 | 504990 | 489 | -79.1 | 504990 | 510 | -85.3 | 504990 | 734 |
| MR_1774413890_599F3FF3 | 504990 | 65 | -82.4 | 504990 | 489 | -79.3 | 504990 | 510 | -87.5 | 504990 | 734 |
| MR_1774413890_3B960116 | 504990 | 65 | -83.5 | 504990 | 489 | -81.1 | 504990 | 510 | -85.6 | 504990 | 734 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 482: `e0fb399e-ef2...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `e0fb399e-ef2b-46e0-bd3a-b21c6fe11d93` |
| Tag | **single-answer** |
| 정답 | **C13** |
| C13 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3271479_1 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[482] topology](images/train_0482.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3271479_1
- `C2`: Adjust the azimuth of 3271479_1 by 12 degrees
- `C3`: Lift the tilt angle of 3271479_1 by 2 degrees
- `C4`: Check test server and transmission issues
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3277495_4
- `C6`: Increase A3 Offset threshold for 3271479_1
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3271479_1
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3277495_4
- `C9`: Insufficient data; more data is needed for judgment.
- `C10`: Decrease A3 Offset threshold for 3271479_1
- `C11`: Decrease transmission power for 3277495_4
- `C12`: Add neighbor relationship between 3225390_10 and 3277495_4
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3271479_1 **← 정답**
- `C14`: Add neighbor relationship between 3271479_1 and 3277495_4
- `C15`: Decrease A3 Offset threshold for 3277495_4
- `C16`: Increase transmission power for 3277495_4
- `C17`: Increase A3 Offset threshold for 3277495_4
- `C18`: Press down the tilt angle of 3271479_1 by 2 degrees
- `C19`: Press down the tilt angle  of 3277495_4 by 2 degrees
- `C20`: Adjust the azimuth of 3277495_4 by 38 degrees
- `C21`: Lift the tilt angle  of 3277495_4 by 2 degrees
- `C22`: Increase transmission power for 3271479_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.747 | MS1 | 121.4656606549 | 31.1446296068 | 416 | 504990 | -94.07 | 9.09 | 393.20 | 0.13 | 2.82 | 1563 |
| 2024-09-20 22:21:32.369 | MS1 | 121.4656739411 | 31.1446245178 | 733 | 504990 | -95.06 | 12.97 | 503.57 | 0.07 | 2.84 | 1577 |
| 2024-09-20 22:21:33.920 | MS1 | 121.4656626362 | 31.1446366391 | 320 | 504990 | -94.46 | 12.58 | 373.86 | 0.04 | 2.96 | 1594 |
| 2024-09-20 22:21:34.442 | MS1 | 121.4656591651 | 31.1446198893 | 838 | 152650 | -89.42 | 3.30 | 76.57 | 0.11 | 1.94 | 957 |
| 2024-09-20 22:21:35.415 | MS1 | 121.4656634870 | 31.1446292974 | 450 | 152650 | -90.46 | 2.42 | 103.83 | 0.14 | 1.80 | 924 |
| 2024-09-20 22:21:36.786 | MS1 | 121.4656732046 | 31.1446263728 | 846 | 152650 | -93.64 | 2.45 | 98.05 | 0.12 | 1.79 | 960 |
| 2024-09-20 22:21:37.389 | MS1 | 121.4656667227 | 31.1446284559 | 277 | 152650 | -95.74 | 5.88 | 65.45 | 0.19 | 1.82 | 985 |
| 2024-09-20 22:21:38.275 | MS1 | 121.4656596535 | 31.1446235311 | 838 | 152650 | -87.31 | 2.62 | 43.91 | 0.14 | 1.89 | 992 |
| 2024-09-20 22:21:39.801 | MS1 | 121.4656685453 | 31.1446253870 | 450 | 152650 | -90.74 | 6.91 | 72.89 | 0.10 | 1.66 | 985 |
| 2024-09-20 22:21:40.765 | MS1 | 121.4656671280 | 31.1446317809 | 846 | 152650 | -88.10 | 5.62 | 99.17 | 0.04 | 2.66 | 1576 |
| 2024-09-20 22:21:41.181 | MS1 | 121.4656749117 | 31.1446200163 | 277 | 152650 | -95.85 | 5.56 | 56.01 | 0.08 | 2.44 | 1581 |
| 2024-09-20 22:21:42.658 | MS1 | 121.4656589300 | 31.1446339088 | 838 | 152650 | -87.60 | 2.27 | 89.33 | 0.18 | 2.35 | 1590 |

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
| 3215156 | 12 | 121.4730177506 | 31.1448019953 | 65 | 8 | 2 | 1.9 | FDD | 277 | n1 | 152650 | 30M | 4T4R | 23 | 152650 |
| 3215435 | 6 | 121.4692890761 | 31.1507126541 | 238 | 5 | 3 | 26.9 | TDD | 733 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3218004 | 8 | 121.4734405194 | 31.1518586298 | 83 | 5 | 0 | 27.8 | FDD | 838 | n1 | 152650 | 30M | 4T4R | 26 | 152650 |
| 3222707 | 7 | 121.4684502456 | 31.1534985088 | 66 | 13 | 5 | 27.7 | FDD | 450 | n1 | 152650 | 30M | 4T4R | 11 | 152650 |
| 3225390 | 10 | 121.4727781639 | 31.1503590087 | 99 | 11 | 12 | 10.7 | FDD | 846 | n1 | 152650 | 30M | 4T4R | 17 | 152650 |
| 3228683 | 11 | 121.4644402505 | 31.1486195607 | 261 | 15 | 4 | 26.1 | FDD | 532 | n1 | 152650 | 30M | 4T4R | 22 | 152650 |
| 3233650 | 5 | 121.4675423326 | 31.1532470942 | 341 | 4 | 0 | 7.2 | TDD | 989 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3239591 | 2 | 121.4691680112 | 31.1529890919 | 115 | 1 | 5 | 28.3 | TDD | 320 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3239743 | 13 | 121.4671076163 | 31.1551877330 | 232 | 1 | 6 | 9.6 | FDD | 219 | n1 | 152650 | 30M | 4T4R | 18 | 152650 |
| 3240118 | 9 | 121.4645024129 | 31.1516714013 | 220 | 15 | 8 | 25.5 | FDD | 297 | n1 | 152650 | 30M | 4T4R | 10 | 152650 |
| 3262376 | 3 | 121.4715314504 | 31.1483922608 | 255 | 6 | 8 | 8.1 | TDD | 836 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3271479 | 1 | 121.4731102411 | 31.1544185579 | 225 | 1 | 5 | 11.8 | TDD | 416 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3277495 | 4 | 121.4741716133 | 31.1488341375 | 202 | 2 | 7 | 5.2 | TDD | 777 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |

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
| 2024-09-20 22:21:30.956 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.976 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.102 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.102 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.838 | NREventA2 | measId:1;ServCellPCI:212;Se... |
| 2024-09-20 22:21:34.972 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.190 | NREventA5 | measId:3;ServCellPCI:212;Se... |
| 2024-09-20 22:21:35.236 | NRHandoverAttempt | SourcePCI:212;SourceNR-ARFC... |
| 2024-09-20 22:21:35.282 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.295 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:35.431 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.431 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3271479 | 1 | 7.3879 | 8.8396 | -117.0820 | 8.9412 | 95.7717 | 0.0052 | 0.0131 |
| 2024_09_20 22:00 | 3239591 | 2 | 5.1987 | 12.8948 | -115.8603 | 11.8541 | 169.0069 | 0.0179 | 0.0069 |
| 2024_09_20 22:00 | 3262376 | 3 | 6.2249 | 16.6991 | -115.0759 | 8.7505 | 186.8509 | 0.0034 | 0.0039 |
| 2024_09_20 22:00 | 3277495 | 4 | 7.7957 | 11.9641 | -117.3158 | 8.8112 | 91.4427 | 0.0163 | 0.0189 |
| 2024_09_20 22:00 | 3233650 | 5 | 17.2334 | 8.4932 | -115.0250 | 15.4692 | 144.5581 | 0.0044 | 0.0159 |
| 2024_09_20 22:00 | 3215435 | 6 | 19.2962 | 18.1964 | -115.8188 | 6.8582 | 153.4704 | 0.0105 | 0.0023 |
| 2024_09_20 22:00 | 3222707 | 7 | 15.5840 | 18.8988 | -114.0385 | 3.9664 | 32.5962 | 0.0049 | 0.0095 |
| 2024_09_20 22:00 | 3218004 | 8 | 11.0158 | 18.4519 | -116.9853 | 4.3740 | 35.2718 | 0.0015 | 0.0062 |
| 2024_09_20 22:00 | 3240118 | 9 | 7.1867 | 7.9577 | -116.6542 | 4.4294 | 24.4075 | 0.0044 | 0.0071 |
| 2024_09_20 22:00 | 3225390 | 10 | 10.4862 | 12.5094 | -116.4265 | 3.4577 | 27.9803 | 0.0187 | 0.0107 |
| 2024_09_20 22:00 | 3228683 | 11 | 5.1447 | 8.8156 | -116.3495 | 3.1531 | 55.3021 | 0.0182 | 0.0151 |
| 2024_09_20 22:00 | 3215156 | 12 | 6.1389 | 8.3904 | -114.6872 | 3.7062 | 21.0711 | 0.0042 | 0.0104 |
| 2024_09_20 22:00 | 3239743 | 13 | 5.4324 | 5.9774 | -116.7651 | 3.8805 | 34.6241 | 0.0029 | 0.0129 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413319_F3DAA1EF | 504990 | 320 | -94.5 | 504990 | 777 | -92.7 | 504990 | 836 | -97.1 | 504990 | 989 |
| MR_1774413319_DD45290F | 152650 | 838 | -90.2 | 152650 | 532 | -92.4 | 152650 | 219 | -95.5 | 152650 | 297 |
| MR_1774413319_F6AC35C5 | 504990 | 320 | -92.9 | 504990 | 777 | -90.9 | 504990 | 836 | -96.6 | 504990 | 989 |
| MR_1774413319_99E9FD41 | 152650 | 838 | -88.3 | 152650 | 532 | -92.9 | 152650 | 219 | -95.3 | 152650 | 297 |
| MR_1774413319_A859DF00 | 152650 | 838 | -89.5 | 152650 | 532 | -93.7 | 152650 | 219 | -97.1 | 152650 | 297 |
| MR_1774413319_3F701BC7 | 152650 | 838 | -88.9 | 152650 | 532 | -91.2 | 152650 | 219 | -95.5 | 152650 | 297 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 483: `b7ded16d-e81...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `b7ded16d-e81f-47e7-aa51-ce7890db640b` |
| Tag | **multiple-answer** |
| 정답 | **C16|C20** |
| C16 의미 | Decrease transmission power for 3256898_2 |
| C20 의미 | Press down the tilt angle  of 3256898_2 by 6 degrees |
| 패턴 분류 | **P3 Overshoot (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[483] topology](images/train_0483.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3256898_2
- `C2`: Increase A3 Offset threshold for 3250057_1
- `C3`: Decrease A3 Offset threshold for 3256898_2
- `C4`: Increase A3 Offset threshold for 3256898_2
- `C5`: Increase transmission power for 3256898_2
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3250057_1
- `C7`: Add neighbor relationship between 3279228_4 and 3256898_2
- `C8`: Lift the tilt angle  of 3256898_2 by 6 degrees
- `C9`: Add neighbor relationship between 3250057_1 and 3256898_2
- `C10`: Insufficient data; more data is needed for judgment.
- `C11`: Adjust the azimuth of 3256898_2 by 16 degrees
- `C12`: Adjust the azimuth of 3250057_1 by 50 degrees
- `C13`: Check test server and transmission issues
- `C14`: Lift the tilt angle of 3250057_1 by 3 degrees
- `C15`: Decrease A3 Offset threshold for 3250057_1
- `C16`: Decrease transmission power for 3256898_2 **← 정답**
- `C17`: Increase transmission power for 3250057_1
- `C18`: Press down the tilt angle of 3250057_1 by 3 degrees
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3250057_1
- `C20`: Press down the tilt angle  of 3256898_2 by 6 degrees **← 정답**
- `C21`: Decrease transmission power for 3250057_1
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3256898_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.249 | MS1 | 121.4656727817 | 31.1446223221 | 352 | 504990 | -77.81 | 12.90 | 378.89 | 0.18 | 2.03 | 1569 |
| 2024-09-20 22:21:32.400 | MS1 | 121.4656741692 | 31.1446371266 | 352 | 504990 | -81.40 | 12.01 | 493.86 | 0.15 | 2.18 | 1573 |
| 2024-09-20 22:21:33.548 | MS1 | 121.4656594917 | 31.1446273158 | 352 | 504990 | -76.10 | 17.20 | 414.97 | 0.11 | 2.13 | 1581 |
| 2024-09-20 22:21:34.704 | MS1 | 121.4656751874 | 31.1446311699 | 352 | 504990 | -94.85 | 3.42 | 62.77 | 0.17 | 1.04 | 1594 |
| 2024-09-20 22:21:35.441 | MS1 | 121.4656768729 | 31.1446275250 | 352 | 504990 | -94.73 | 2.42 | 56.97 | 0.16 | 1.45 | 1587 |
| 2024-09-20 22:21:36.688 | MS1 | 121.4656618271 | 31.1446258095 | 352 | 504990 | -91.56 | 0.88 | 73.08 | 0.01 | 1.48 | 1591 |
| 2024-09-20 22:21:37.429 | MS1 | 121.4656768569 | 31.1446237329 | 352 | 504990 | -87.18 | 2.06 | 54.86 | 0.16 | 1.48 | 1563 |
| 2024-09-20 22:21:38.595 | MS1 | 121.4656617666 | 31.1446251228 | 352 | 504990 | -90.09 | 3.98 | 58.18 | 0.09 | 1.43 | 1593 |
| 2024-09-20 22:21:39.242 | MS1 | 121.4656650836 | 31.1446349829 | 352 | 504990 | -92.82 | 3.42 | 75.56 | 0.14 | 1.20 | 1584 |
| 2024-09-20 22:21:40.368 | MS1 | 121.4656582565 | 31.1446308468 | 352 | 504990 | -77.07 | 12.90 | 464.63 | 0.08 | 2.84 | 1592 |
| 2024-09-20 22:21:41.540 | MS1 | 121.4656626062 | 31.1446337217 | 352 | 504990 | -83.62 | 15.09 | 510.65 | 0.01 | 2.50 | 1580 |
| 2024-09-20 22:21:42.156 | MS1 | 121.4656748545 | 31.1446211596 | 352 | 504990 | -78.18 | 12.22 | 313.36 | 0.04 | 2.49 | 1588 |

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
| 3250057 | 1 | 121.4746057427 | 31.1443529805 | 322 | 1 | 9 | 24.8 | TDD | 352 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3256898 | 2 | 121.4734134825 | 31.1490735161 | 252 | 3 | 3 | 42.6 | TDD | 921 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3278712 | 3 | 121.4722486992 | 31.1512580387 | 105 | 1 | 6 | 45.8 | TDD | 145 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3279228 | 4 | 121.4698375289 | 31.1532614274 | 214 | 7 | 11 | 24.3 | TDD | 251 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |

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
| 2024-09-20 22:21:30.761 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:30.874 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.874 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3250057 | 1 | 16.0116 | 5.1354 | -109.2386 | 13.0555 | 176.8323 | 0.0038 | 0.0144 |
| 2024_09_20 22:00 | 3256898 | 2 | 12.5810 | 19.1136 | -117.8869 | 9.4592 | 192.7538 | 0.0137 | 0.0143 |
| 2024_09_20 22:00 | 3278712 | 3 | 12.3241 | 18.7285 | -114.6017 | 11.2947 | 126.8566 | 0.0097 | 0.0077 |
| 2024_09_20 22:00 | 3279228 | 4 | 17.2044 | 7.2263 | -117.3521 | 9.0494 | 102.8623 | 0.0172 | 0.0029 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413243_806E0F8E | 504990 | 921 | -96.1 | 504990 | 352 | -93.6 | 504990 | 251 | -95.2 | 504990 | 145 |
| MR_1774413243_535D2ADB | 504990 | 352 | -96.2 | 504990 | 921 | -92.0 | 504990 | 251 | -92.3 | 504990 | 145 |
| MR_1774413243_D22C12DE | 504990 | 352 | -94.0 | 504990 | 921 | -92.6 | 504990 | 251 | -93.6 | 504990 | 145 |
| MR_1774413243_9D1B72E9 | 504990 | 921 | -93.4 | 504990 | 352 | -90.4 | 504990 | 251 | -93.5 | 504990 | 145 |
| MR_1774413243_05D92BFF | 504990 | 921 | -94.2 | 504990 | 352 | -91.7 | 504990 | 251 | -94.5 | 504990 | 145 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 484: `1fac1919-14c...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `1fac1919-14ca-4659-8247-908eae3c984c` |
| Tag | **multiple-answer** |
| 정답 | **C1|C20** |
| C1 의미 | Increase transmission power for 3220102_2 |
| C20 의미 | Adjust the azimuth of 3220102_2 by 22 degrees |
| 패턴 분류 | **P4 Coverage (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[484] topology](images/train_0484.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3220102_2 **← 정답**
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3220102_2
- `C3`: Increase A3 Offset threshold for 3220102_2
- `C4`: Lift the tilt angle  of 3217773_1 by 4 degrees
- `C5`: Add neighbor relationship between 3220102_2 and 3217773_1
- `C6`: Press down the tilt angle of 3220102_2 by 10 degrees
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3217773_1
- `C8`: Check test server and transmission issues
- `C9`: Decrease A3 Offset threshold for 3220102_2
- `C10`: Insufficient data; more data is needed for judgment.
- `C11`: Decrease transmission power for 3217773_1
- `C12`: Lift the tilt angle of 3220102_2 by 10 degrees
- `C13`: Press down the tilt angle  of 3217773_1 by 4 degrees
- `C14`: Increase A3 Offset threshold for 3217773_1
- `C15`: Increase transmission power for 3217773_1
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3217773_1
- `C17`: Decrease transmission power for 3220102_2
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3220102_2
- `C19`: Decrease A3 Offset threshold for 3217773_1
- `C20`: Adjust the azimuth of 3220102_2 by 22 degrees **← 정답**
- `C21`: Add neighbor relationship between 3252021_3 and 3217773_1
- `C22`: Adjust the azimuth of 3217773_1 by 47 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.204 | MS1 | 121.4656645124 | 31.1446342573 | 380 | 504990 | -90.12 | 13.81 | 417.33 | 0.10 | 2.11 | 1577 |
| 2024-09-20 22:21:32.618 | MS1 | 121.4656628450 | 31.1446365090 | 380 | 504990 | -92.63 | 16.80 | 582.15 | 0.12 | 2.46 | 1574 |
| 2024-09-20 22:21:33.137 | MS1 | 121.4656650763 | 31.1446238089 | 380 | 504990 | -94.58 | 14.12 | 310.64 | 0.20 | 2.60 | 1571 |
| 2024-09-20 22:21:34.473 | MS1 | 121.4656661735 | 31.1446239536 | 380 | 504990 | -101.54 | 0.04 | 33.87 | 0.00 | 1.29 | 1587 |
| 2024-09-20 22:21:35.599 | MS1 | 121.4656622044 | 31.1446295263 | 380 | 504990 | -106.39 | 1.20 | 48.93 | 0.19 | 1.18 | 1578 |
| 2024-09-20 22:21:36.308 | MS1 | 121.4656706227 | 31.1446368902 | 380 | 504990 | -100.52 | 1.63 | 88.65 | 0.10 | 1.01 | 1585 |
| 2024-09-20 22:21:37.398 | MS1 | 121.4656720677 | 31.1446350733 | 380 | 504990 | -105.52 | 1.90 | 56.51 | 0.07 | 1.24 | 1567 |
| 2024-09-20 22:21:38.643 | MS1 | 121.4656694142 | 31.1446252090 | 380 | 504990 | -106.41 | 1.08 | 46.41 | 0.03 | 1.37 | 1569 |
| 2024-09-20 22:21:39.754 | MS1 | 121.4656606463 | 31.1446201852 | 380 | 504990 | -101.13 | 1.47 | 37.64 | 0.11 | 1.32 | 1597 |
| 2024-09-20 22:21:40.381 | MS1 | 121.4656732805 | 31.1446184016 | 380 | 504990 | -85.22 | 16.87 | 378.12 | 0.04 | 2.54 | 1599 |
| 2024-09-20 22:21:41.845 | MS1 | 121.4656661742 | 31.1446249608 | 380 | 504990 | -90.60 | 13.16 | 316.34 | 0.13 | 2.05 | 1579 |
| 2024-09-20 22:21:42.320 | MS1 | 121.4656647200 | 31.1446360748 | 380 | 504990 | -93.33 | 14.25 | 582.68 | 0.14 | 2.19 | 1589 |

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
| 3217773 | 1 | 121.4759935431 | 31.1445016764 | 318 | 1 | 11 | 43.6 | TDD | 754 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3220102 | 2 | 121.4687215186 | 31.1512712413 | 223 | 10 | 10 | 22.4 | TDD | 380 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3252021 | 3 | 121.4693028017 | 31.1531857350 | 246 | 14 | 4 | 48.7 | TDD | 348 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3253693 | 4 | 121.4739279937 | 31.1492734499 | 179 | 6 | 9 | 30.5 | TDD | 79 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |

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
| 2024-09-20 22:21:31.210 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.228 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.366 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.366 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.589 | NREventA2 | measId:1;ServCellPCI:410;Se... |
| 2024-09-20 22:21:34.725 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3217773 | 1 | 12.2686 | 13.3752 | -115.4875 | 6.2863 | 151.5423 | 0.0117 | 0.0131 |
| 2024_09_20 22:00 | 3220102 | 2 | 10.5483 | 18.2147 | -117.1649 | 14.9060 | 192.0097 | 0.1349 | 0.0021 |
| 2024_09_20 22:00 | 3252021 | 3 | 11.9490 | 14.3938 | -115.5360 | 7.3272 | 108.4565 | 0.0098 | 0.0093 |
| 2024_09_20 22:00 | 3253693 | 4 | 18.3975 | 5.3877 | -117.3543 | 5.8643 | 155.9527 | 0.0152 | 0.0187 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414046_24DD41C2 | 504990 | 380 | -102.9 | 504990 | 754 | -107.2 | 504990 | 348 | -112.9 | 504990 | 79 |
| MR_1774414046_90CD2BC5 | 504990 | 380 | -102.6 | 504990 | 754 | -110.2 | 504990 | 348 | -111.9 | 504990 | 79 |
| MR_1774414046_9125CD05 | 504990 | 380 | -101.5 | 504990 | 754 | -107.1 | 504990 | 348 | -113.7 | 504990 | 79 |
| MR_1774414046_89907D87 | 504990 | 380 | -103.0 | 504990 | 754 | -107.3 | 504990 | 348 | -112.4 | 504990 | 79 |
| MR_1774414046_8A855E10 | 504990 | 380 | -100.7 | 504990 | 754 | -106.7 | 504990 | 348 | -114.5 | 504990 | 79 |
| MR_1774414046_D87D65A8 | 504990 | 380 | -101.1 | 504990 | 754 | -109.7 | 504990 | 348 | -114.4 | 504990 | 79 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 485: `c6a3f5da-d1e...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `c6a3f5da-d1e6-4667-be28-6ae4cfdecfbf` |
| Tag | **multiple-answer** |
| 정답 | **C7|C13** |
| C7 의미 | Adjust the azimuth of 3231270_2 by 47 degrees |
| C13 의미 | Increase transmission power for 3231270_2 |
| 패턴 분류 | **P4 Coverage (azimuth)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[485] topology](images/train_0485.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3231270_2 and 3241110_4
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3241110_4
- `C3`: Lift the tilt angle  of 3241110_4 by 5 degrees
- `C4`: Insufficient data; more data is needed for judgment.
- `C5`: Increase A3 Offset threshold for 3231270_2
- `C6`: Decrease A3 Offset threshold for 3231270_2
- `C7`: Adjust the azimuth of 3231270_2 by 47 degrees **← 정답**
- `C8`: Decrease transmission power for 3241110_4
- `C9`: Check test server and transmission issues
- `C10`: Decrease transmission power for 3231270_2
- `C11`: Press down the tilt angle  of 3241110_4 by 5 degrees
- `C12`: Lift the tilt angle of 3231270_2 by 10 degrees
- `C13`: Increase transmission power for 3231270_2 **← 정답**
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3231270_2
- `C15`: Decrease A3 Offset threshold for 3241110_4
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3231270_2
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3241110_4
- `C18`: Press down the tilt angle of 3231270_2 by 10 degrees
- `C19`: Adjust the azimuth of 3241110_4 by 24 degrees
- `C20`: Increase transmission power for 3241110_4
- `C21`: Increase A3 Offset threshold for 3241110_4
- `C22`: Add neighbor relationship between 3264425_3 and 3241110_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.538 | MS1 | 121.4656740591 | 31.1446269364 | 45 | 504990 | -89.34 | 12.29 | 458.33 | 0.13 | 2.37 | 1575 |
| 2024-09-20 22:21:32.487 | MS1 | 121.4656705249 | 31.1446307403 | 45 | 504990 | -94.36 | 15.67 | 560.86 | 0.01 | 2.73 | 1575 |
| 2024-09-20 22:21:33.448 | MS1 | 121.4656755999 | 31.1446342701 | 45 | 504990 | -91.03 | 12.68 | 398.71 | 0.15 | 2.16 | 1582 |
| 2024-09-20 22:21:34.401 | MS1 | 121.4656664624 | 31.1446337867 | 45 | 504990 | -103.79 | -0.54 | 49.56 | 0.01 | 1.31 | 1570 |
| 2024-09-20 22:21:35.350 | MS1 | 121.4656626844 | 31.1446199372 | 45 | 504990 | -108.30 | -1.39 | 79.10 | 0.15 | 1.48 | 1586 |
| 2024-09-20 22:21:36.972 | MS1 | 121.4656624403 | 31.1446253008 | 45 | 504990 | -104.28 | -0.93 | 29.60 | 0.06 | 1.21 | 1584 |
| 2024-09-20 22:21:37.523 | MS1 | 121.4656581546 | 31.1446188920 | 45 | 504990 | -102.33 | 1.20 | 17.06 | 0.05 | 1.47 | 1593 |
| 2024-09-20 22:21:38.907 | MS1 | 121.4656708166 | 31.1446277345 | 45 | 504990 | -108.97 | -0.91 | 36.98 | 0.16 | 1.49 | 1572 |
| 2024-09-20 22:21:39.437 | MS1 | 121.4656713528 | 31.1446360962 | 45 | 504990 | -108.85 | -0.00 | 36.98 | 0.09 | 1.13 | 1583 |
| 2024-09-20 22:21:40.235 | MS1 | 121.4656646835 | 31.1446214015 | 45 | 504990 | -89.55 | 14.41 | 562.55 | 0.13 | 2.34 | 1587 |
| 2024-09-20 22:21:41.361 | MS1 | 121.4656629638 | 31.1446262127 | 45 | 504990 | -94.76 | 12.15 | 427.07 | 0.08 | 2.40 | 1598 |
| 2024-09-20 22:21:42.133 | MS1 | 121.4656657476 | 31.1446253639 | 45 | 504990 | -94.25 | 13.83 | 357.82 | 0.19 | 2.65 | 1598 |

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
| 3231270 | 2 | 121.4662452598 | 31.1470835089 | 145 | 13 | 6 | 35.6 | TDD | 45 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3241110 | 4 | 121.4740421315 | 31.1460985751 | 282 | 2 | 1 | 45.8 | TDD | 871 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3255359 | 1 | 121.4724934464 | 31.1476747647 | 293 | 4 | 0 | 37.5 | TDD | 291 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3264425 | 3 | 121.4707400063 | 31.1489183041 | 324 | 10 | 12 | 34.6 | TDD | 806 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |

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
| 2024-09-20 22:21:31.542 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.565 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.672 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.672 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.914 | NREventA2 | measId:1;ServCellPCI:600;Se... |
| 2024-09-20 22:21:35.050 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3255359 | 1 | 18.0435 | 10.9062 | -116.8599 | 19.2375 | 95.3111 | 0.0176 | 0.0177 |
| 2024_09_20 22:00 | 3231270 | 2 | 17.5206 | 7.8879 | -115.0962 | 10.9691 | 80.1093 | 0.1969 | 0.0003 |
| 2024_09_20 22:00 | 3264425 | 3 | 11.5351 | 14.8880 | -116.5075 | 18.8805 | 150.0510 | 0.0144 | 0.0078 |
| 2024_09_20 22:00 | 3241110 | 4 | 9.0320 | 8.0169 | -116.6152 | 12.7151 | 124.0675 | 0.0097 | 0.0094 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414101_54BBC4B1 | 504990 | 45 | -101.9 | 504990 | 871 | -111.4 | 504990 | 806 | -115.5 | 504990 | 291 |
| MR_1774414101_1925496E | 504990 | 45 | -105.0 | 504990 | 871 | -111.7 | 504990 | 806 | -115.8 | 504990 | 291 |
| MR_1774414101_C63D3959 | 504990 | 45 | -105.5 | 504990 | 871 | -111.3 | 504990 | 806 | -116.9 | 504990 | 291 |
| MR_1774414101_25B81710 | 504990 | 45 | -104.1 | 504990 | 871 | -109.6 | 504990 | 806 | -113.7 | 504990 | 291 |
| MR_1774414101_3411A5BC | 504990 | 45 | -103.7 | 504990 | 871 | -110.0 | 504990 | 806 | -113.8 | 504990 | 291 |
| MR_1774414101_21A7A257 | 504990 | 45 | -103.6 | 504990 | 871 | -109.3 | 504990 | 806 | -116.3 | 504990 | 291 |
| MR_1774414101_26B52BDF | 504990 | 45 | -103.9 | 504990 | 871 | -111.3 | 504990 | 806 | -117.0 | 504990 | 291 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 486: `519321fa-ee6...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `519321fa-ee67-48b6-95a7-d2749239096e` |
| Tag | **single-answer** |
| 정답 | **C3** |
| C3 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3234648_2 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[486] topology](images/train_0486.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3234648_2 and 3278226_1
- `C2`: Press down the tilt angle  of 3278226_1 by 10 degrees
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3234648_2 **← 정답**
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3278226_1
- `C5`: Insufficient data; more data is needed for judgment.
- `C6`: Increase A3 Offset threshold for 3234648_2
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3278226_1
- `C8`: Adjust the azimuth of 3234648_2 by 10 degrees
- `C9`: Decrease A3 Offset threshold for 3278226_1
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3234648_2
- `C11`: Increase A3 Offset threshold for 3278226_1
- `C12`: Decrease transmission power for 3278226_1
- `C13`: Lift the tilt angle  of 3278226_1 by 10 degrees
- `C14`: Add neighbor relationship between 3226757_4 and 3278226_1
- `C15`: Increase transmission power for 3234648_2
- `C16`: Lift the tilt angle of 3234648_2 by 1 degrees
- `C17`: Increase transmission power for 3278226_1
- `C18`: Check test server and transmission issues
- `C19`: Decrease transmission power for 3234648_2
- `C20`: Adjust the azimuth of 3278226_1 by 50 degrees
- `C21`: Decrease A3 Offset threshold for 3234648_2
- `C22`: Press down the tilt angle of 3234648_2 by 1 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.147 | MS1 | 121.4656771679 | 31.1446245742 | 698 | 504990 | -88.28 | 12.69 | 445.72 | 0.11 | 2.85 | 1597 |
| 2024-09-20 22:21:32.627 | MS1 | 121.4656748695 | 31.1446300511 | 698 | 504990 | -86.80 | 14.41 | 552.71 | 0.15 | 2.06 | 1564 |
| 2024-09-20 22:21:33.417 | MS1 | 121.4656683362 | 31.1446245478 | 698 | 504990 | -91.90 | 15.29 | 344.66 | 0.04 | 2.99 | 1591 |
| 2024-09-20 22:21:34.459 | MS1 | 121.4656754135 | 31.1446316757 | 698 | 504990 | -91.44 | 15.36 | 63.90 | 0.55 | 2.77 | 648 |
| 2024-09-20 22:21:35.428 | MS1 | 121.4656683830 | 31.1446302675 | 698 | 504990 | -86.50 | 15.78 | 88.86 | 0.68 | 2.43 | 549 |
| 2024-09-20 22:21:36.754 | MS1 | 121.4656724984 | 31.1446302522 | 698 | 504990 | -91.49 | 16.44 | 77.32 | 0.54 | 2.86 | 533 |
| 2024-09-20 22:21:37.730 | MS1 | 121.4656713367 | 31.1446244231 | 698 | 504990 | -92.93 | 8.27 | 86.77 | 0.52 | 2.38 | 571 |
| 2024-09-20 22:21:38.336 | MS1 | 121.4656652465 | 31.1446243322 | 698 | 504990 | -93.04 | 7.77 | 83.32 | 0.51 | 2.91 | 569 |
| 2024-09-20 22:21:39.840 | MS1 | 121.4656590615 | 31.1446180009 | 698 | 504990 | -89.39 | 8.64 | 52.22 | 0.55 | 2.47 | 601 |
| 2024-09-20 22:21:40.974 | MS1 | 121.4656751124 | 31.1446236923 | 698 | 504990 | -93.29 | 12.05 | 324.13 | 0.08 | 2.91 | 1592 |
| 2024-09-20 22:21:41.886 | MS1 | 121.4656662333 | 31.1446285143 | 698 | 504990 | -91.53 | 12.13 | 432.48 | 0.15 | 2.95 | 1600 |
| 2024-09-20 22:21:42.831 | MS1 | 121.4656590257 | 31.1446206644 | 698 | 504990 | -91.76 | 10.60 | 563.06 | 0.18 | 2.07 | 1596 |

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
| 3226757 | 4 | 121.4753693556 | 31.1451870310 | 212 | 15 | 4 | 16.5 | TDD | 415 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3234648 | 2 | 121.4663310297 | 31.1554816944 | 193 | 0 | 2 | 27.8 | TDD | 698 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3244044 | 3 | 121.4668632658 | 31.1519710318 | 82 | 0 | 3 | 21.3 | TDD | 203 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3278226 | 1 | 121.4728557034 | 31.1455669828 | 203 | 14 | 9 | 45.1 | TDD | 232 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |

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
| 2024-09-20 22:21:31.298 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.318 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.426 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.426 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.119 | NREventA3 | measId:2;ServCellPCI:364;Se... |
| 2024-09-20 22:21:38.359 | NRHandoverAttempt | SourcePCI:364;SourceNR-ARFC... |
| 2024-09-20 22:21:38.403 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.417 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.524 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.524 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3278226 | 1 | 6.5141 | 13.6376 | -116.7433 | 7.3796 | 103.4060 | 0.0019 | 0.0128 |
| 2024_09_20 22:00 | 3234648 | 2 | 18.4734 | 9.2306 | -116.9364 | 15.5049 | 138.3750 | 0.0195 | 0.0111 |
| 2024_09_20 22:00 | 3244044 | 3 | 10.1794 | 16.5750 | -114.7912 | 6.7959 | 171.9163 | 0.0085 | 0.0040 |
| 2024_09_20 22:00 | 3226757 | 4 | 19.0927 | 7.0385 | -116.7932 | 15.2488 | 161.9432 | 0.0013 | 0.0174 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412656_FFFA3CA1 | 504990 | 698 | -92.9 | 504990 | 232 | -98.8 | 504990 | 415 | -99.2 | 504990 | 203 |
| MR_1774412656_F69F9449 | 504990 | 698 | -92.8 | 504990 | 232 | -97.9 | 504990 | 415 | -100.6 | 504990 | 203 |
| MR_1774412656_B2F7B870 | 504990 | 698 | -89.9 | 504990 | 232 | -98.0 | 504990 | 415 | -99.2 | 504990 | 203 |
| MR_1774412656_D89487E1 | 504990 | 698 | -92.7 | 504990 | 232 | -97.1 | 504990 | 415 | -98.0 | 504990 | 203 |
| MR_1774412656_7B222901 | 504990 | 698 | -92.5 | 504990 | 232 | -98.2 | 504990 | 415 | -101.5 | 504990 | 203 |
| MR_1774412656_FABDF87C | 504990 | 698 | -92.7 | 504990 | 232 | -99.6 | 504990 | 415 | -100.1 | 504990 | 203 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 487: `9887eb61-f04...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `9887eb61-f04d-49a0-bd86-00fd66a303d5` |
| Tag | **single-answer** |
| 정답 | **C7** |
| C7 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3267744_4 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[487] topology](images/train_0487.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3233224_3 and 3231033_2
- `C2`: Adjust the azimuth of 3231033_2 by 50 degrees
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3231033_2
- `C4`: Decrease A3 Offset threshold for 3231033_2
- `C5`: Decrease A3 Offset threshold for 3267744_4
- `C6`: Check test server and transmission issues
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3267744_4 **← 정답**
- `C8`: Increase transmission power for 3231033_2
- `C9`: Insufficient data; more data is needed for judgment.
- `C10`: Adjust the azimuth of 3267744_4 by 14 degrees
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3231033_2
- `C12`: Press down the tilt angle of 3267744_4 by 4 degrees
- `C13`: Increase A3 Offset threshold for 3267744_4
- `C14`: Increase transmission power for 3267744_4
- `C15`: Lift the tilt angle of 3267744_4 by 4 degrees
- `C16`: Decrease transmission power for 3231033_2
- `C17`: Add neighbor relationship between 3267744_4 and 3231033_2
- `C18`: Decrease transmission power for 3267744_4
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3267744_4
- `C20`: Increase A3 Offset threshold for 3231033_2
- `C21`: Lift the tilt angle  of 3231033_2 by 10 degrees
- `C22`: Press down the tilt angle  of 3231033_2 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.348 | MS1 | 121.4656603797 | 31.1446204274 | 167 | 504990 | -85.90 | 15.27 | 312.81 | 0.14 | 2.86 | 1598 |
| 2024-09-20 22:21:32.744 | MS1 | 121.4656681435 | 31.1446204256 | 167 | 504990 | -87.90 | 17.18 | 505.81 | 0.11 | 2.61 | 1567 |
| 2024-09-20 22:21:33.130 | MS1 | 121.4656614615 | 31.1446295915 | 167 | 504990 | -87.64 | 13.21 | 434.92 | 0.15 | 2.05 | 1592 |
| 2024-09-20 22:21:34.118 | MS1 | 121.4656747418 | 31.1446316466 | 167 | 504990 | -87.90 | 16.08 | 76.92 | 0.65 | 2.98 | 681 |
| 2024-09-20 22:21:35.872 | MS1 | 121.4656765226 | 31.1446367052 | 167 | 504990 | -89.86 | 15.66 | 81.82 | 0.64 | 3.00 | 683 |
| 2024-09-20 22:21:36.778 | MS1 | 121.4656670241 | 31.1446224803 | 167 | 504990 | -88.09 | 17.33 | 81.87 | 0.66 | 2.01 | 683 |
| 2024-09-20 22:21:37.536 | MS1 | 121.4656677631 | 31.1446351170 | 167 | 504990 | -93.51 | 10.78 | 55.91 | 0.65 | 2.85 | 577 |
| 2024-09-20 22:21:38.826 | MS1 | 121.4656734740 | 31.1446182043 | 167 | 504990 | -93.99 | 9.50 | 72.36 | 0.57 | 2.26 | 513 |
| 2024-09-20 22:21:39.371 | MS1 | 121.4656654490 | 31.1446191434 | 167 | 504990 | -93.24 | 11.44 | 47.57 | 0.60 | 2.70 | 670 |
| 2024-09-20 22:21:40.405 | MS1 | 121.4656663307 | 31.1446322440 | 167 | 504990 | -93.70 | 7.33 | 601.62 | 0.20 | 2.06 | 1564 |
| 2024-09-20 22:21:41.526 | MS1 | 121.4656640755 | 31.1446347080 | 167 | 504990 | -90.84 | 11.24 | 468.99 | 0.10 | 2.79 | 1600 |
| 2024-09-20 22:21:42.550 | MS1 | 121.4656747088 | 31.1446273153 | 167 | 504990 | -92.98 | 9.13 | 484.93 | 0.06 | 2.36 | 1578 |

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
| 3231033 | 2 | 121.4662692168 | 31.1543908931 | 23 | 12 | 10 | 28.3 | TDD | 652 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3233224 | 3 | 121.4688762764 | 31.1449707956 | 50 | 1 | 0 | 37.5 | TDD | 419 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3267744 | 4 | 121.4684293522 | 31.1491230491 | 222 | 0 | 3 | 37.2 | TDD | 167 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3276994 | 1 | 121.4692514866 | 31.1490698144 | 289 | 1 | 3 | 42.9 | TDD | 291 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |

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
| 2024-09-20 22:21:31.402 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.423 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.546 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.546 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.251 | NREventA3 | measId:2;ServCellPCI:415;Se... |
| 2024-09-20 22:21:38.491 | NRHandoverAttempt | SourcePCI:415;SourceNR-ARFC... |
| 2024-09-20 22:21:38.524 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.538 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.649 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.649 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3276994 | 1 | 10.4375 | 17.1920 | -116.2106 | 11.7732 | 186.9104 | 0.0174 | 0.0007 |
| 2024_09_20 22:00 | 3231033 | 2 | 5.7431 | 17.4061 | -116.4769 | 10.6448 | 184.8285 | 0.0032 | 0.0047 |
| 2024_09_20 22:00 | 3233224 | 3 | 8.2733 | 13.0022 | -116.4408 | 7.7760 | 103.5126 | 0.0191 | 0.0064 |
| 2024_09_20 22:00 | 3267744 | 4 | 7.1810 | 16.7885 | -117.4307 | 8.0081 | 177.6953 | 0.0145 | 0.0142 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415811_755F1EF0 | 504990 | 167 | -85.9 | 504990 | 652 | -91.5 | 504990 | 419 | -97.8 | 504990 | 291 |
| MR_1774415811_53C569B2 | 504990 | 167 | -86.1 | 504990 | 652 | -91.8 | 504990 | 419 | -95.3 | 504990 | 291 |
| MR_1774415811_863E67EF | 504990 | 167 | -89.6 | 504990 | 652 | -91.6 | 504990 | 419 | -96.8 | 504990 | 291 |
| MR_1774415811_DC4ADA26 | 504990 | 167 | -87.5 | 504990 | 652 | -91.0 | 504990 | 419 | -96.2 | 504990 | 291 |
| MR_1774415811_C3868052 | 504990 | 167 | -89.7 | 504990 | 652 | -89.2 | 504990 | 419 | -98.1 | 504990 | 291 |
| MR_1774415811_4BAB92F2 | 504990 | 167 | -87.2 | 504990 | 652 | -89.1 | 504990 | 419 | -95.4 | 504990 | 291 |
| MR_1774415811_A2DEB963 | 504990 | 167 | -87.7 | 504990 | 652 | -89.6 | 504990 | 419 | -94.8 | 504990 | 291 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 488: `4cef1e1a-6c1...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `4cef1e1a-6c19-4dd5-a454-1be0d1faaa53` |
| Tag | **single-answer** |
| 정답 | **C8** |
| C8 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3230743_2 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[488] topology](images/train_0488.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3230743_2
- `C2`: Insufficient data; more data is needed for judgment.
- `C3`: Adjust the azimuth of 3230743_2 by 10 degrees
- `C4`: Lift the tilt angle  of 3234480_3 by 3 degrees
- `C5`: Lift the tilt angle of 3230743_2 by 5 degrees
- `C6`: Increase transmission power for 3230743_2
- `C7`: Check test server and transmission issues
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3230743_2 **← 정답**
- `C9`: Press down the tilt angle  of 3234480_3 by 3 degrees
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3230743_2
- `C11`: Decrease A3 Offset threshold for 3234480_3
- `C12`: Add neighbor relationship between 3230743_2 and 3234480_3
- `C13`: Increase A3 Offset threshold for 3230743_2
- `C14`: Decrease A3 Offset threshold for 3230743_2
- `C15`: Decrease transmission power for 3234480_3
- `C16`: Add neighbor relationship between 3260451_4 and 3234480_3
- `C17`: Increase transmission power for 3234480_3
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3234480_3
- `C19`: Press down the tilt angle of 3230743_2 by 5 degrees
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3234480_3
- `C21`: Adjust the azimuth of 3234480_3 by 50 degrees
- `C22`: Increase A3 Offset threshold for 3234480_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.782 | MS1 | 121.4656658792 | 31.1446301789 | 569 | 504990 | -85.04 | 15.30 | 577.65 | 0.17 | 2.36 | 1589 |
| 2024-09-20 22:21:32.940 | MS1 | 121.4656598335 | 31.1446256199 | 569 | 504990 | -90.56 | 15.19 | 383.82 | 0.04 | 3.00 | 1567 |
| 2024-09-20 22:21:33.976 | MS1 | 121.4656727714 | 31.1446337908 | 569 | 504990 | -88.75 | 16.96 | 461.80 | 0.20 | 2.87 | 1583 |
| 2024-09-20 22:21:34.986 | MS1 | 121.4656601041 | 31.1446224884 | 569 | 504990 | -87.00 | 12.08 | 73.34 | 0.60 | 2.62 | 638 |
| 2024-09-20 22:21:35.150 | MS1 | 121.4656779240 | 31.1446274129 | 569 | 504990 | -90.88 | 12.14 | 43.20 | 0.56 | 2.14 | 514 |
| 2024-09-20 22:21:36.297 | MS1 | 121.4656668458 | 31.1446229999 | 569 | 504990 | -88.30 | 15.67 | 70.50 | 0.64 | 2.06 | 570 |
| 2024-09-20 22:21:37.586 | MS1 | 121.4656721505 | 31.1446320038 | 569 | 504990 | -91.12 | 7.82 | 74.01 | 0.61 | 2.78 | 673 |
| 2024-09-20 22:21:38.498 | MS1 | 121.4656772302 | 31.1446278412 | 569 | 504990 | -90.20 | 8.41 | 90.88 | 0.64 | 2.78 | 597 |
| 2024-09-20 22:21:39.932 | MS1 | 121.4656708671 | 31.1446224097 | 569 | 504990 | -92.76 | 8.88 | 77.68 | 0.68 | 2.56 | 612 |
| 2024-09-20 22:21:40.250 | MS1 | 121.4656593806 | 31.1446196506 | 569 | 504990 | -90.45 | 7.41 | 587.16 | 0.12 | 2.37 | 1568 |
| 2024-09-20 22:21:41.564 | MS1 | 121.4656670610 | 31.1446295750 | 569 | 504990 | -90.70 | 11.59 | 354.70 | 0.17 | 2.74 | 1569 |
| 2024-09-20 22:21:42.450 | MS1 | 121.4656701325 | 31.1446335048 | 569 | 504990 | -89.55 | 7.49 | 406.96 | 0.08 | 2.33 | 1568 |

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
| 3212960 | 1 | 121.4743556432 | 31.1483405993 | 296 | 0 | 4 | 22.8 | TDD | 984 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3230743 | 2 | 121.4728823189 | 31.1490226129 | 225 | 3 | 10 | 27.8 | TDD | 569 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3234480 | 3 | 121.4727240407 | 31.1457989165 | 5 | 1 | 0 | 18.0 | TDD | 842 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3260451 | 4 | 121.4729538249 | 31.1484780969 | 332 | 15 | 4 | 26.8 | TDD | 871 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |

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
| 2024-09-20 22:21:30.966 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.981 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.112 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.112 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.850 | NREventA3 | measId:2;ServCellPCI:830;Se... |
| 2024-09-20 22:21:38.090 | NRHandoverAttempt | SourcePCI:830;SourceNR-ARFC... |
| 2024-09-20 22:21:38.132 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.146 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.254 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.254 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3212960 | 1 | 16.6599 | 9.1134 | -117.1706 | 12.2387 | 163.6417 | 0.0077 | 0.0170 |
| 2024_09_20 22:00 | 3230743 | 2 | 10.8295 | 19.0504 | -114.8378 | 11.5729 | 136.1006 | 0.0097 | 0.0192 |
| 2024_09_20 22:00 | 3234480 | 3 | 6.1841 | 17.5516 | -114.1532 | 9.2812 | 154.2340 | 0.0027 | 0.0060 |
| 2024_09_20 22:00 | 3260451 | 4 | 12.1060 | 6.7251 | -114.9434 | 18.8756 | 166.6001 | 0.0104 | 0.0003 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415014_C884011F | 504990 | 569 | -86.0 | 504990 | 842 | -94.5 | 504990 | 871 | -97.0 | 504990 | 984 |
| MR_1774415014_54F00102 | 504990 | 569 | -85.2 | 504990 | 842 | -93.5 | 504990 | 871 | -95.9 | 504990 | 984 |
| MR_1774415014_7DEDEC6F | 504990 | 569 | -85.2 | 504990 | 842 | -94.6 | 504990 | 871 | -95.7 | 504990 | 984 |
| MR_1774415014_1B8CBBD5 | 504990 | 569 | -86.6 | 504990 | 842 | -95.9 | 504990 | 871 | -97.5 | 504990 | 984 |
| MR_1774415014_1826DBE8 | 504990 | 569 | -86.9 | 504990 | 842 | -95.1 | 504990 | 871 | -97.1 | 504990 | 984 |
| MR_1774415014_58BCC756 | 504990 | 569 | -86.7 | 504990 | 842 | -96.7 | 504990 | 871 | -96.1 | 504990 | 984 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 489: `12f2cce3-616...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `12f2cce3-6160-4c07-83a7-5838527db3bd` |
| Tag | **single-answer** |
| 정답 | **C18** |
| C18 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[489] topology](images/train_0489.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3276376_3 by 3 degrees
- `C2`: Increase A3 Offset threshold for 3276376_3
- `C3`: Add neighbor relationship between 3234727_1 and 3276376_3
- `C4`: Lift the tilt angle  of 3276376_3 by 3 degrees
- `C5`: Decrease A3 Offset threshold for 3228998_2
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3228998_2
- `C7`: Adjust the azimuth of 3276376_3 by 50 degrees
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3228998_2
- `C9`: Increase transmission power for 3228998_2
- `C10`: Decrease transmission power for 3276376_3
- `C11`: Decrease transmission power for 3228998_2
- `C12`: Add neighbor relationship between 3228998_2 and 3276376_3
- `C13`: Increase A3 Offset threshold for 3228998_2
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3276376_3
- `C15`: Adjust the azimuth of 3228998_2 by 50 degrees
- `C16`: Press down the tilt angle of 3228998_2 by 8 degrees
- `C17`: Decrease A3 Offset threshold for 3276376_3
- `C18`: Check test server and transmission issues **← 정답**
- `C19`: Increase transmission power for 3276376_3
- `C20`: Lift the tilt angle of 3228998_2 by 8 degrees
- `C21`: Insufficient data; more data is needed for judgment.
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3276376_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.210 | MS1 | 121.4656630683 | 31.1446180807 | 337 | 504990 | -90.12 | 14.89 | 330.48 | 0.12 | 2.26 | 1575 |
| 2024-09-20 22:21:32.313 | MS1 | 121.4656664169 | 31.1446215612 | 337 | 504990 | -86.64 | 13.97 | 527.39 | 0.11 | 2.48 | 1577 |
| 2024-09-20 22:21:33.886 | MS1 | 121.4656583120 | 31.1446254892 | 337 | 504990 | -91.03 | 17.20 | 330.60 | 0.11 | 2.73 | 1591 |
| 2024-09-20 22:21:34.957 | MS1 | 121.4656727986 | 31.1446214447 | 337 | 504990 | -86.72 | 14.63 | 92.29 | 0.07 | 2.64 | 460 |
| 2024-09-20 22:21:35.495 | MS1 | 121.4656731006 | 31.1446311839 | 337 | 504990 | -87.31 | 14.23 | 63.25 | 0.08 | 2.01 | 484 |
| 2024-09-20 22:21:36.872 | MS1 | 121.4656709779 | 31.1446306154 | 337 | 504990 | -87.87 | 16.28 | 96.45 | 0.16 | 2.31 | 314 |
| 2024-09-20 22:21:37.437 | MS1 | 121.4656613872 | 31.1446339981 | 337 | 504990 | -90.96 | 12.77 | 76.46 | 0.16 | 2.50 | 348 |
| 2024-09-20 22:21:38.575 | MS1 | 121.4656671139 | 31.1446191669 | 337 | 504990 | -93.49 | 7.47 | 59.84 | 0.06 | 2.36 | 398 |
| 2024-09-20 22:21:39.275 | MS1 | 121.4656586562 | 31.1446244813 | 337 | 504990 | -92.62 | 7.46 | 93.34 | 0.15 | 2.51 | 412 |
| 2024-09-20 22:21:40.364 | MS1 | 121.4656747354 | 31.1446206750 | 337 | 504990 | -93.10 | 12.99 | 358.56 | 0.12 | 2.08 | 1591 |
| 2024-09-20 22:21:41.870 | MS1 | 121.4656735679 | 31.1446283695 | 337 | 504990 | -92.89 | 12.26 | 430.85 | 0.00 | 2.82 | 1585 |
| 2024-09-20 22:21:42.748 | MS1 | 121.4656776494 | 31.1446224660 | 337 | 504990 | -93.85 | 8.31 | 337.36 | 0.13 | 2.96 | 1564 |

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
| 3216147 | 4 | 121.4645958351 | 31.1445562297 | 228 | 3 | 12 | 39.1 | TDD | 901 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3228998 | 2 | 121.4666173585 | 31.1459449550 | 330 | 0 | 3 | 24.2 | TDD | 337 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3234727 | 1 | 121.4678776294 | 31.1507140050 | 14 | 4 | 3 | 40.0 | TDD | 688 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3276376 | 3 | 121.4723190924 | 31.1453899880 | 126 | 1 | 9 | 25.6 | TDD | 781 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |

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
| 2024-09-20 22:21:30.785 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.809 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:30.957 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.957 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.684 | NREventA3 | measId:2;ServCellPCI:320;Se... |
| 2024-09-20 22:21:37.924 | NRHandoverAttempt | SourcePCI:320;SourceNR-ARFC... |
| 2024-09-20 22:21:37.959 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.970 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.075 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.075 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3234727 | 1 | 14.9718 | 16.9360 | -117.0426 | 5.5835 | 88.6970 | 0.0006 | 0.0013 |
| 2024_09_20 22:00 | 3228998 | 2 | 9.4913 | 5.2791 | -116.5701 | 11.2395 | 184.9406 | 0.0158 | 0.0007 |
| 2024_09_20 22:00 | 3276376 | 3 | 7.4939 | 13.1822 | -114.1668 | 15.1801 | 156.5555 | 0.0009 | 0.0112 |
| 2024_09_20 22:00 | 3216147 | 4 | 14.8298 | 15.2959 | -117.0324 | 11.2397 | 105.6528 | 0.0141 | 0.0112 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415248_FBDD3436 | 504990 | 337 | -86.0 | 504990 | 781 | -94.0 | 504990 | 688 | -96.3 | 504990 | 901 |
| MR_1774415248_1972B5DB | 504990 | 337 | -88.5 | 504990 | 781 | -94.8 | 504990 | 688 | -97.7 | 504990 | 901 |
| MR_1774415248_626B03C9 | 504990 | 337 | -85.5 | 504990 | 781 | -94.8 | 504990 | 688 | -94.9 | 504990 | 901 |
| MR_1774415248_B863FE21 | 504990 | 337 | -88.0 | 504990 | 781 | -94.8 | 504990 | 688 | -95.2 | 504990 | 901 |
| MR_1774415248_70FA15AD | 504990 | 337 | -87.6 | 504990 | 781 | -93.4 | 504990 | 688 | -97.0 | 504990 | 901 |
| MR_1774415248_656165E1 | 504990 | 337 | -85.3 | 504990 | 781 | -92.7 | 504990 | 688 | -95.7 | 504990 | 901 |
| MR_1774415248_452750AF | 504990 | 337 | -88.7 | 504990 | 781 | -93.5 | 504990 | 688 | -95.9 | 504990 | 901 |

> *... 2개 열 생략 (전체 14열)*

---
