# Track A 문제 분석 — train[840]~train[849]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[840] ~ train[849] (10개)

## 목차

1. [문제 840: `90c41604-f76...`](#840) — single-answer, 정답: C20
2. [문제 841: `615371c5-fc8...`](#841) — multiple-answer, 정답: C20|C22
3. [문제 842: `9d975683-012...`](#842) — single-answer, 정답: C13
4. [문제 843: `17b8f94b-d3c...`](#843) — single-answer, 정답: C13
5. [문제 844: `8aa9465a-7f8...`](#844) — multiple-answer, 정답: C15|C19
6. [문제 845: `924b3337-c4d...`](#845) — multiple-answer, 정답: C2|C21
7. [문제 846: `a5b569d2-076...`](#846) — single-answer, 정답: C12
8. [문제 847: `a9e3881a-759...`](#847) — single-answer, 정답: C21
9. [문제 848: `311aca6b-105...`](#848) — single-answer, 정답: C3
10. [문제 849: `8ba5c377-666...`](#849) — single-answer, 정답: C11

---

### 문제 840: `90c41604-f76...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `90c41604-f76f-49c1-a19e-5d1bea912f94` |
| Tag | **single-answer** |
| 정답 | **C20** |
| C20 의미 | Lift the tilt angle  of 3270068_2 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[840] topology](images/train_0840.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3271706_3
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3253422_4
- `C3`: Increase A3 Offset threshold for 3271706_3
- `C4`: Adjust the azimuth of 3270068_2 by 39 degrees
- `C5`: Insufficient data; more data is needed for judgment.
- `C6`: Adjust the azimuth of 3271706_3 by 43 degrees
- `C7`: Lift the tilt angle of 3271706_3 by 6 degrees
- `C8`: Decrease transmission power for 3253422_4
- `C9`: Press down the tilt angle  of 3270068_2 by 10 degrees
- `C10`: Decrease A3 Offset threshold for 3271706_3
- `C11`: Decrease transmission power for 3271706_3
- `C12`: Add neighbor relationship between 3270068_2 and 3253422_4
- `C13`: Increase transmission power for 3271706_3
- `C14`: Increase transmission power for 3253422_4
- `C15`: Press down the tilt angle of 3271706_3 by 6 degrees
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3253422_4
- `C17`: Increase A3 Offset threshold for 3253422_4
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3271706_3
- `C19`: Decrease A3 Offset threshold for 3253422_4
- `C20`: Lift the tilt angle  of 3270068_2 by 10 degrees **← 정답**
- `C21`: Check test server and transmission issues
- `C22`: Add neighbor relationship between 3271706_3 and 3253422_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.723 | MS1 | 121.4656733321 | 31.1446186705 | 861 | 504990 | -90.39 | 13.28 | 410.46 | 0.05 | 2.67 | 1565 |
| 2024-09-20 22:21:32.919 | MS1 | 121.4656737900 | 31.1446355485 | 861 | 504990 | -85.65 | 15.19 | 455.00 | 0.18 | 2.99 | 1563 |
| 2024-09-20 22:21:33.155 | MS1 | 121.4656730967 | 31.1446277355 | 861 | 504990 | -90.11 | 15.20 | 343.87 | 0.18 | 2.18 | 1570 |
| 2024-09-20 22:21:34.137 | MS1 | 121.4656701017 | 31.1446346555 | 861 | 504990 | -91.58 | 13.39 | 90.92 | 0.14 | 2.86 | 1584 |
| 2024-09-20 22:21:35.336 | MS1 | 121.4656596486 | 31.1446308961 | 861 | 504990 | -85.50 | 13.89 | 60.75 | 0.05 | 2.12 | 1580 |
| 2024-09-20 22:21:36.871 | MS1 | 121.4656642486 | 31.1446301782 | 861 | 504990 | -90.22 | 14.08 | 72.16 | 0.17 | 2.19 | 1585 |
| 2024-09-20 22:21:37.801 | MS1 | 121.4656711625 | 31.1446333118 | 861 | 504990 | -92.74 | 9.05 | 93.43 | 0.14 | 2.61 | 1599 |
| 2024-09-20 22:21:38.234 | MS1 | 121.4656709335 | 31.1446294092 | 861 | 504990 | -92.27 | 11.28 | 87.51 | 0.10 | 2.50 | 1564 |
| 2024-09-20 22:21:39.854 | MS1 | 121.4656636694 | 31.1446321356 | 861 | 504990 | -89.95 | 10.91 | 87.88 | 0.14 | 2.87 | 1590 |
| 2024-09-20 22:21:40.535 | MS1 | 121.4656611988 | 31.1446308058 | 861 | 504990 | -90.48 | 9.11 | 530.53 | 0.15 | 2.29 | 1595 |
| 2024-09-20 22:21:41.904 | MS1 | 121.4656640671 | 31.1446349965 | 861 | 504990 | -90.33 | 8.41 | 495.09 | 0.03 | 2.27 | 1581 |
| 2024-09-20 22:21:42.848 | MS1 | 121.4656608965 | 31.1446233602 | 861 | 504990 | -92.55 | 10.23 | 305.31 | 0.09 | 2.49 | 1579 |

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
| 3253422 | 4 | 121.4640281679 | 31.1456433772 | 87 | 11 | 11 | 18.0 | TDD | 109 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3263706 | 1 | 121.4748122094 | 31.1445254735 | 209 | 1 | 1 | 29.7 | TDD | 376 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3270068 | 2 | 121.4734134268 | 31.1549382512 | 73 | 6 | 5 | 41.3 | TDD | 562 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3271706 | 3 | 121.4741800886 | 31.1540753363 | 261 | 5 | 3 | 20.4 | TDD | 861 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:30.939 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.960 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.075 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.075 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.778 | NREventA3 | measId:2;ServCellPCI:236;Se... |
| 2024-09-20 22:21:38.018 | NRHandoverAttempt | SourcePCI:236;SourceNR-ARFC... |
| 2024-09-20 22:21:38.055 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.066 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.186 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.186 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3263706 | 1 | 12.6231 | 6.8496 | -115.8734 | 12.7139 | 194.3406 | 0.0086 | 0.0034 |
| 2024_09_20 22:00 | 3270068 | 2 | 5.9519 | 8.6841 | -116.6741 | 9.2009 | 131.7561 | 0.0160 | 0.0018 |
| 2024_09_20 22:00 | 3271706 | 3 | 75.7231 | 91.7234 | -117.0979 | 11.5657 | 145.4103 | 0.0022 | 0.0174 |
| 2024_09_20 22:00 | 3253422 | 4 | 10.5736 | 5.9588 | -117.7495 | 12.6428 | 114.3201 | 0.0049 | 0.0062 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416462_D2557EEB | 504990 | 861 | -90.8 | 504990 | 109 | -98.1 | 504990 | 562 | -105.4 | 504990 | 376 |
| MR_1774416462_65FDFD9A | 504990 | 861 | -89.7 | 504990 | 109 | -100.2 | 504990 | 562 | -105.7 | 504990 | 376 |
| MR_1774416462_ADBB7F58 | 504990 | 861 | -90.4 | 504990 | 109 | -98.0 | 504990 | 562 | -105.8 | 504990 | 376 |
| MR_1774416462_2AB76B46 | 504990 | 861 | -90.9 | 504990 | 109 | -98.1 | 504990 | 562 | -105.4 | 504990 | 376 |
| MR_1774416462_CBEE8F85 | 504990 | 861 | -93.1 | 504990 | 109 | -97.5 | 504990 | 562 | -104.7 | 504990 | 376 |
| MR_1774416462_9C295D28 | 504990 | 861 | -91.4 | 504990 | 109 | -99.4 | 504990 | 562 | -104.1 | 504990 | 376 |
| MR_1774416462_71DF5725 | 504990 | 861 | -89.7 | 504990 | 109 | -97.9 | 504990 | 562 | -104.7 | 504990 | 376 |
| MR_1774416462_61D3BBE0 | 504990 | 861 | -93.4 | 504990 | 109 | -99.4 | 504990 | 562 | -104.4 | 504990 | 376 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 841: `615371c5-fc8...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `615371c5-fc81-4ebc-9c5c-dab1505e4534` |
| Tag | **multiple-answer** |
| 정답 | **C20|C22** |
| C20 의미 | Adjust the azimuth of 3270676_1 by 44 degrees |
| C22 의미 | Increase transmission power for 3270676_1 |
| 패턴 분류 | **P4 Coverage (azimuth)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[841] topology](images/train_0841.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3246525_2
- `C2`: Decrease transmission power for 3246525_2
- `C3`: Lift the tilt angle  of 3246525_2 by 4 degrees
- `C4`: Increase A3 Offset threshold for 3270676_1
- `C5`: Increase A3 Offset threshold for 3246525_2
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3270676_1
- `C7`: Add neighbor relationship between 3270676_1 and 3246525_2
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3270676_1
- `C9`: Press down the tilt angle of 3270676_1 by 10 degrees
- `C10`: Adjust the azimuth of 3246525_2 by 31 degrees
- `C11`: Increase transmission power for 3246525_2
- `C12`: Decrease A3 Offset threshold for 3270676_1
- `C13`: Press down the tilt angle  of 3246525_2 by 4 degrees
- `C14`: Decrease A3 Offset threshold for 3246525_2
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3246525_2
- `C16`: Add neighbor relationship between 3271103_4 and 3246525_2
- `C17`: Insufficient data; more data is needed for judgment.
- `C18`: Decrease transmission power for 3270676_1
- `C19`: Lift the tilt angle of 3270676_1 by 10 degrees
- `C20`: Adjust the azimuth of 3270676_1 by 44 degrees **← 정답**
- `C21`: Check test server and transmission issues
- `C22`: Increase transmission power for 3270676_1 **← 정답**

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.504 | MS1 | 121.4656590318 | 31.1446194029 | 900 | 504990 | -94.09 | 13.11 | 563.07 | 0.19 | 2.94 | 1569 |
| 2024-09-20 22:21:32.721 | MS1 | 121.4656729587 | 31.1446219883 | 900 | 504990 | -89.06 | 15.04 | 353.86 | 0.07 | 2.33 | 1588 |
| 2024-09-20 22:21:33.785 | MS1 | 121.4656770263 | 31.1446210719 | 900 | 504990 | -93.46 | 14.04 | 449.24 | 0.08 | 2.73 | 1583 |
| 2024-09-20 22:21:34.555 | MS1 | 121.4656613315 | 31.1446328678 | 900 | 504990 | -105.40 | 0.70 | 14.29 | 0.18 | 1.40 | 1565 |
| 2024-09-20 22:21:35.332 | MS1 | 121.4656753970 | 31.1446374023 | 900 | 504990 | -100.85 | 0.50 | 71.41 | 0.04 | 1.37 | 1583 |
| 2024-09-20 22:21:36.477 | MS1 | 121.4656592263 | 31.1446190809 | 900 | 504990 | -100.59 | 0.18 | 42.67 | 0.08 | 1.45 | 1574 |
| 2024-09-20 22:21:37.770 | MS1 | 121.4656751385 | 31.1446330774 | 900 | 504990 | -104.72 | -0.79 | 32.72 | 0.17 | 1.05 | 1578 |
| 2024-09-20 22:21:38.821 | MS1 | 121.4656778690 | 31.1446212906 | 900 | 504990 | -105.97 | 1.04 | 52.26 | 0.16 | 1.02 | 1562 |
| 2024-09-20 22:21:39.415 | MS1 | 121.4656645113 | 31.1446328747 | 900 | 504990 | -103.29 | 1.95 | 34.84 | 0.01 | 1.08 | 1581 |
| 2024-09-20 22:21:40.804 | MS1 | 121.4656614163 | 31.1446361416 | 900 | 504990 | -89.20 | 12.39 | 523.95 | 0.02 | 2.28 | 1575 |
| 2024-09-20 22:21:41.221 | MS1 | 121.4656759066 | 31.1446190414 | 900 | 504990 | -92.73 | 17.54 | 398.05 | 0.03 | 2.64 | 1588 |
| 2024-09-20 22:21:42.518 | MS1 | 121.4656701232 | 31.1446378320 | 900 | 504990 | -89.36 | 14.39 | 507.18 | 0.16 | 2.00 | 1569 |

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
| 3246525 | 2 | 121.4652837183 | 31.1467325672 | 140 | 0 | 2 | 15.4 | TDD | 775 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3251433 | 3 | 121.4753711008 | 31.1473002208 | 354 | 1 | 7 | 35.4 | TDD | 742 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3270676 | 1 | 121.4676245361 | 31.1451790965 | 296 | 11 | 12 | 40.5 | TDD | 900 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3271103 | 4 | 121.4721660469 | 31.1558148916 | 16 | 10 | 8 | 36.6 | TDD | 935 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:31.123 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.140 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.265 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.265 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.436 | NREventA2 | measId:1;ServCellPCI:938;Se... |
| 2024-09-20 22:21:34.563 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3270676 | 1 | 14.1008 | 14.0159 | -116.0465 | 16.1065 | 191.0686 | 0.1646 | 0.0002 |
| 2024_09_20 22:00 | 3246525 | 2 | 7.5375 | 13.2342 | -116.3577 | 18.0285 | 82.0464 | 0.0074 | 0.0091 |
| 2024_09_20 22:00 | 3251433 | 3 | 16.2239 | 10.4573 | -115.7477 | 15.0900 | 172.2084 | 0.0105 | 0.0130 |
| 2024_09_20 22:00 | 3271103 | 4 | 5.1599 | 15.3144 | -114.2190 | 8.6497 | 190.4196 | 0.0160 | 0.0138 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414610_B4D7AC02 | 504990 | 900 | -104.6 | 504990 | 775 | -110.3 | 504990 | 935 | -114.2 | 504990 | 742 |
| MR_1774414610_43E6CB59 | 504990 | 900 | -105.8 | 504990 | 775 | -110.5 | 504990 | 935 | -117.8 | 504990 | 742 |
| MR_1774414610_AE1657F9 | 504990 | 900 | -107.2 | 504990 | 775 | -110.4 | 504990 | 935 | -114.8 | 504990 | 742 |
| MR_1774414610_8129E4E8 | 504990 | 900 | -105.0 | 504990 | 775 | -107.0 | 504990 | 935 | -114.2 | 504990 | 742 |
| MR_1774414610_0C2452A6 | 504990 | 900 | -106.3 | 504990 | 775 | -107.8 | 504990 | 935 | -116.9 | 504990 | 742 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 842: `9d975683-012...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `9d975683-012e-4424-a3cb-d72d28df1a12` |
| Tag | **single-answer** |
| 정답 | **C13** |
| C13 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3217655_2 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[842] topology](images/train_0842.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3229998_3
- `C2`: Check test server and transmission issues
- `C3`: Increase transmission power for 3229998_3
- `C4`: Press down the tilt angle  of 3229998_3 by 10 degrees
- `C5`: Press down the tilt angle of 3217655_2 by 3 degrees
- `C6`: Adjust the azimuth of 3229998_3 by 50 degrees
- `C7`: Decrease transmission power for 3229998_3
- `C8`: Decrease A3 Offset threshold for 3217655_2
- `C9`: Increase A3 Offset threshold for 3217655_2
- `C10`: Lift the tilt angle of 3217655_2 by 3 degrees
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3229998_3
- `C12`: Increase transmission power for 3217655_2
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3217655_2 **← 정답**
- `C14`: Lift the tilt angle  of 3229998_3 by 10 degrees
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3229998_3
- `C16`: Add neighbor relationship between 3217655_2 and 3229998_3
- `C17`: Add neighbor relationship between 3215899_1 and 3229998_3
- `C18`: Decrease transmission power for 3217655_2
- `C19`: Insufficient data; more data is needed for judgment.
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3217655_2
- `C21`: Decrease A3 Offset threshold for 3229998_3
- `C22`: Adjust the azimuth of 3217655_2 by 36 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.636 | MS1 | 121.4656715829 | 31.1446210802 | 20 | 504990 | -85.14 | 15.56 | 357.38 | 0.01 | 2.58 | 1573 |
| 2024-09-20 22:21:32.761 | MS1 | 121.4656621517 | 31.1446353239 | 20 | 504990 | -90.82 | 13.96 | 496.29 | 0.15 | 2.03 | 1571 |
| 2024-09-20 22:21:33.426 | MS1 | 121.4656613927 | 31.1446284139 | 20 | 504990 | -87.62 | 13.97 | 335.61 | 0.09 | 2.54 | 1569 |
| 2024-09-20 22:21:34.238 | MS1 | 121.4656750120 | 31.1446332909 | 20 | 504990 | -91.22 | 16.05 | 77.46 | 0.62 | 2.45 | 672 |
| 2024-09-20 22:21:35.939 | MS1 | 121.4656689045 | 31.1446344315 | 20 | 504990 | -88.66 | 12.18 | 52.74 | 0.69 | 2.05 | 662 |
| 2024-09-20 22:21:36.332 | MS1 | 121.4656679537 | 31.1446356321 | 20 | 504990 | -88.70 | 15.37 | 60.53 | 0.57 | 2.75 | 527 |
| 2024-09-20 22:21:37.695 | MS1 | 121.4656699914 | 31.1446196633 | 20 | 504990 | -93.54 | 9.88 | 73.37 | 0.55 | 2.76 | 598 |
| 2024-09-20 22:21:38.660 | MS1 | 121.4656589689 | 31.1446234457 | 20 | 504990 | -91.15 | 12.68 | 104.42 | 0.61 | 2.20 | 503 |
| 2024-09-20 22:21:39.480 | MS1 | 121.4656634047 | 31.1446191149 | 20 | 504990 | -90.37 | 7.64 | 84.26 | 0.61 | 2.90 | 570 |
| 2024-09-20 22:21:40.592 | MS1 | 121.4656728902 | 31.1446331314 | 20 | 504990 | -91.89 | 12.48 | 527.98 | 0.14 | 2.32 | 1573 |
| 2024-09-20 22:21:41.747 | MS1 | 121.4656666724 | 31.1446275476 | 20 | 504990 | -91.89 | 9.73 | 379.69 | 0.04 | 2.22 | 1591 |
| 2024-09-20 22:21:42.575 | MS1 | 121.4656645481 | 31.1446287510 | 20 | 504990 | -92.18 | 12.67 | 450.61 | 0.07 | 2.87 | 1590 |

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
| 3215899 | 1 | 121.4672273050 | 31.1508852031 | 131 | 11 | 0 | 41.2 | TDD | 384 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3217655 | 2 | 121.4713343721 | 31.1469911085 | 208 | 0 | 0 | 29.1 | TDD | 20 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3229998 | 3 | 121.4718040174 | 31.1533109066 | 64 | 14 | 3 | 16.0 | TDD | 157 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3233254 | 4 | 121.4724858423 | 31.1552741223 | 139 | 12 | 7 | 31.0 | TDD | 774 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:31.469 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.488 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.615 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.615 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.310 | NREventA3 | measId:2;ServCellPCI:790;Se... |
| 2024-09-20 22:21:38.550 | NRHandoverAttempt | SourcePCI:790;SourceNR-ARFC... |
| 2024-09-20 22:21:38.589 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.603 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.738 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.738 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3215899 | 1 | 9.8871 | 14.3534 | -117.1217 | 8.7730 | 108.5485 | 0.0030 | 0.0153 |
| 2024_09_20 22:00 | 3217655 | 2 | 6.5836 | 13.7442 | -115.8345 | 10.5395 | 163.0505 | 0.0163 | 0.0113 |
| 2024_09_20 22:00 | 3229998 | 3 | 18.7835 | 10.9164 | -114.8849 | 11.3253 | 188.8059 | 0.0143 | 0.0058 |
| 2024_09_20 22:00 | 3233254 | 4 | 7.4610 | 10.7960 | -117.1732 | 16.5357 | 163.4491 | 0.0162 | 0.0051 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414829_BEB98FB8 | 504990 | 20 | -91.6 | 504990 | 157 | -93.1 | 504990 | 384 | -106.0 | 504990 | 774 |
| MR_1774414829_010D1DEE | 504990 | 20 | -91.8 | 504990 | 157 | -91.9 | 504990 | 384 | -102.8 | 504990 | 774 |
| MR_1774414829_0188A2E9 | 504990 | 20 | -90.0 | 504990 | 157 | -91.1 | 504990 | 384 | -105.7 | 504990 | 774 |
| MR_1774414829_A169C906 | 504990 | 20 | -93.0 | 504990 | 157 | -93.3 | 504990 | 384 | -103.8 | 504990 | 774 |
| MR_1774414829_751C7BE7 | 504990 | 20 | -93.2 | 504990 | 157 | -90.7 | 504990 | 384 | -106.4 | 504990 | 774 |
| MR_1774414829_1A2D06D3 | 504990 | 20 | -90.5 | 504990 | 157 | -94.2 | 504990 | 384 | -106.5 | 504990 | 774 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 843: `17b8f94b-d3c...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `17b8f94b-d3c1-4f5a-9a57-73a418d9f1b9` |
| Tag | **single-answer** |
| 정답 | **C13** |
| C13 의미 | Decrease A3 Offset threshold for 3247026_4 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[843] topology](images/train_0843.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3247026_4 and 3220020_3
- `C2`: Increase A3 Offset threshold for 3220020_3
- `C3`: Decrease transmission power for 3220020_3
- `C4`: Decrease transmission power for 3247026_4
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3247026_4
- `C6`: Decrease A3 Offset threshold for 3220020_3
- `C7`: Press down the tilt angle  of 3220020_3 by 10 degrees
- `C8`: Increase transmission power for 3220020_3
- `C9`: Press down the tilt angle of 3247026_4 by 8 degrees
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3220020_3
- `C11`: Add neighbor relationship between 3233552_2 and 3220020_3
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3220020_3
- `C13`: Decrease A3 Offset threshold for 3247026_4 **← 정답**
- `C14`: Increase A3 Offset threshold for 3247026_4
- `C15`: Lift the tilt angle of 3247026_4 by 8 degrees
- `C16`: Insufficient data; more data is needed for judgment.
- `C17`: Lift the tilt angle  of 3220020_3 by 10 degrees
- `C18`: Increase transmission power for 3247026_4
- `C19`: Check test server and transmission issues
- `C20`: Adjust the azimuth of 3220020_3 by 50 degrees
- `C21`: Adjust the azimuth of 3247026_4 by 50 degrees
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3247026_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.698 | MS1 | 121.4656722922 | 31.1446323396 | 69 | 504990 | -82.73 | 15.27 | 453.15 | 0.09 | 2.76 | 1581 |
| 2024-09-20 22:21:32.785 | MS1 | 121.4656740329 | 31.1446187470 | 69 | 504990 | -79.24 | 15.90 | 397.86 | 0.12 | 2.83 | 1563 |
| 2024-09-20 22:21:33.344 | MS1 | 121.4656627685 | 31.1446257724 | 69 | 504990 | -81.43 | 14.46 | 351.05 | 0.06 | 2.44 | 1584 |
| 2024-09-20 22:21:34.149 | MS1 | 121.4656657027 | 31.1446198690 | 69 | 504990 | -86.62 | -2.34 | 54.16 | 0.10 | 1.26 | 1593 |
| 2024-09-20 22:21:35.734 | MS1 | 121.4656608104 | 31.1446308330 | 69 | 504990 | -88.80 | -1.49 | 28.67 | 0.15 | 1.04 | 1567 |
| 2024-09-20 22:21:36.374 | MS1 | 121.4656708671 | 31.1446311865 | 69 | 504990 | -87.61 | -2.79 | 44.47 | 0.01 | 1.47 | 1564 |
| 2024-09-20 22:21:37.321 | MS1 | 121.4656721695 | 31.1446199361 | 69 | 504990 | -83.84 | -1.69 | 56.25 | 0.12 | 1.15 | 1584 |
| 2024-09-20 22:21:38.608 | MS1 | 121.4656709895 | 31.1446320773 | 69 | 504990 | -86.74 | -1.27 | 21.40 | 0.10 | 1.27 | 1581 |
| 2024-09-20 22:21:39.259 | MS1 | 121.4656719766 | 31.1446281158 | 332 | 504990 | -84.12 | 15.19 | 225.61 | 0.01 | 1.49 | 1572 |
| 2024-09-20 22:21:40.779 | MS1 | 121.4656672267 | 31.1446374603 | 332 | 504990 | -78.00 | 15.32 | 380.91 | 0.11 | 2.14 | 1593 |
| 2024-09-20 22:21:41.347 | MS1 | 121.4656695527 | 31.1446265490 | 332 | 504990 | -83.01 | 14.96 | 470.27 | 0.09 | 2.78 | 1562 |
| 2024-09-20 22:21:42.483 | MS1 | 121.4656593375 | 31.1446309676 | 332 | 504990 | -82.88 | 12.54 | 392.05 | 0.18 | 2.01 | 1582 |

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
| 3220020 | 3 | 121.4702126006 | 31.1530199106 | 28 | 15 | 7 | 19.9 | TDD | 332 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3231234 | 1 | 121.4647464779 | 31.1508265923 | 201 | 11 | 3 | 34.3 | TDD | 560 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3233552 | 2 | 121.4754860885 | 31.1549530096 | 60 | 5 | 0 | 35.8 | TDD | 251 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3247026 | 4 | 121.4732724839 | 31.1450817489 | 87 | 5 | 4 | 33.9 | TDD | 69 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

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
| 2024-09-20 22:21:31.658 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.675 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.817 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.817 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.491 | NREventA3 | measId:2;ServCellPCI:478;Se... |
| 2024-09-20 22:21:38.731 | NRHandoverAttempt | SourcePCI:478;SourceNR-ARFC... |
| 2024-09-20 22:21:38.779 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.794 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.940 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.940 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3231234 | 1 | 13.7492 | 11.9282 | -115.8758 | 18.8650 | 81.7983 | 0.0195 | 0.0143 |
| 2024_09_20 22:00 | 3233552 | 2 | 13.5279 | 11.2264 | -116.0552 | 16.9432 | 139.8311 | 0.0077 | 0.0045 |
| 2024_09_20 22:00 | 3220020 | 3 | 5.5485 | 18.7175 | -114.4239 | 12.9024 | 84.1912 | 0.0138 | 0.0068 |
| 2024_09_20 22:00 | 3247026 | 4 | 7.3200 | 11.2755 | -114.5115 | 13.8241 | 182.1902 | 0.0066 | 0.1455 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416094_BAD5230F | 504990 | 69 | -88.6 | 504990 | 332 | -83.2 | 504990 | 251 | -81.6 | 504990 | 560 |
| MR_1774416094_D0A10914 | 504990 | 69 | -88.3 | 504990 | 332 | -81.9 | 504990 | 251 | -81.7 | 504990 | 560 |
| MR_1774416094_6AD16ADE | 504990 | 332 | -83.4 | 504990 | 69 | -85.3 | 504990 | 251 | -81.0 | 504990 | 560 |
| MR_1774416094_CCC5DFEC | 504990 | 332 | -80.5 | 504990 | 69 | -87.5 | 504990 | 251 | -83.3 | 504990 | 560 |
| MR_1774416094_F816970A | 504990 | 332 | -80.6 | 504990 | 69 | -85.5 | 504990 | 251 | -83.1 | 504990 | 560 |
| MR_1774416094_0BF7FF6C | 504990 | 332 | -83.4 | 504990 | 69 | -87.2 | 504990 | 251 | -80.8 | 504990 | 560 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 844: `8aa9465a-7f8...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `8aa9465a-7f8b-4070-b8aa-7f8a496f8c22` |
| Tag | **multiple-answer** |
| 정답 | **C15|C19** |
| C15 의미 | Press down the tilt angle  of 3261753_1 by 4 degrees |
| C19 의미 | Decrease transmission power for 3261753_1 |
| 패턴 분류 | **P3 Overshoot (tilt)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[844] topology](images/train_0844.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3275437_4
- `C2`: Insufficient data; more data is needed for judgment.
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3275437_4
- `C4`: Decrease A3 Offset threshold for 3261753_1
- `C5`: Decrease A3 Offset threshold for 3275437_4
- `C6`: Press down the tilt angle of 3275437_4 by 2 degrees
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3261753_1
- `C8`: Increase A3 Offset threshold for 3261753_1
- `C9`: Add neighbor relationship between 3253058_2 and 3261753_1
- `C10`: Increase transmission power for 3261753_1
- `C11`: Decrease transmission power for 3275437_4
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3261753_1
- `C13`: Lift the tilt angle of 3275437_4 by 2 degrees
- `C14`: Check test server and transmission issues
- `C15`: Press down the tilt angle  of 3261753_1 by 4 degrees **← 정답**
- `C16`: Lift the tilt angle  of 3261753_1 by 4 degrees
- `C17`: Increase A3 Offset threshold for 3275437_4
- `C18`: Adjust the azimuth of 3275437_4 by 5 degrees
- `C19`: Decrease transmission power for 3261753_1 **← 정답**
- `C20`: Add neighbor relationship between 3275437_4 and 3261753_1
- `C21`: Adjust the azimuth of 3261753_1 by 18 degrees
- `C22`: Increase transmission power for 3275437_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.698 | MS1 | 121.4656699611 | 31.1446356920 | 325 | 504990 | -80.44 | 15.40 | 389.91 | 0.01 | 2.16 | 1567 |
| 2024-09-20 22:21:32.822 | MS1 | 121.4656685226 | 31.1446370090 | 325 | 504990 | -76.64 | 13.07 | 300.77 | 0.08 | 2.83 | 1565 |
| 2024-09-20 22:21:33.533 | MS1 | 121.4656710888 | 31.1446270413 | 325 | 504990 | -75.19 | 16.86 | 503.25 | 0.16 | 2.32 | 1561 |
| 2024-09-20 22:21:34.570 | MS1 | 121.4656708883 | 31.1446280009 | 325 | 504990 | -91.33 | 2.45 | 79.75 | 0.11 | 1.23 | 1598 |
| 2024-09-20 22:21:35.177 | MS1 | 121.4656736631 | 31.1446229026 | 325 | 504990 | -85.81 | 1.44 | 47.73 | 0.08 | 1.02 | 1563 |
| 2024-09-20 22:21:36.507 | MS1 | 121.4656734524 | 31.1446362218 | 325 | 504990 | -92.81 | 1.06 | 82.54 | 0.01 | 1.30 | 1570 |
| 2024-09-20 22:21:37.614 | MS1 | 121.4656625034 | 31.1446335003 | 325 | 504990 | -88.39 | 1.64 | 60.92 | 0.19 | 1.26 | 1598 |
| 2024-09-20 22:21:38.213 | MS1 | 121.4656719233 | 31.1446263109 | 325 | 504990 | -86.69 | 1.16 | 63.60 | 0.00 | 1.47 | 1596 |
| 2024-09-20 22:21:39.257 | MS1 | 121.4656721750 | 31.1446289581 | 325 | 504990 | -88.41 | 2.35 | 44.57 | 0.01 | 1.03 | 1560 |
| 2024-09-20 22:21:40.315 | MS1 | 121.4656590998 | 31.1446332585 | 325 | 504990 | -77.50 | 15.74 | 300.60 | 0.19 | 2.92 | 1577 |
| 2024-09-20 22:21:41.823 | MS1 | 121.4656605318 | 31.1446207041 | 325 | 504990 | -75.67 | 14.58 | 372.29 | 0.18 | 2.66 | 1577 |
| 2024-09-20 22:21:42.765 | MS1 | 121.4656655253 | 31.1446285216 | 325 | 504990 | -82.94 | 17.93 | 307.60 | 0.13 | 2.97 | 1560 |

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
| 3253058 | 2 | 121.4730584904 | 31.1540367458 | 136 | 6 | 9 | 21.0 | TDD | 258 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3256824 | 3 | 121.4747570233 | 31.1495159766 | 31 | 4 | 7 | 24.5 | TDD | 347 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3261753 | 1 | 121.4727761137 | 31.1454332340 | 280 | 1 | 4 | 36.7 | TDD | 17 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3275437 | 4 | 121.4675373938 | 31.1541281807 | 185 | 0 | 8 | 32.4 | TDD | 325 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |

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
| 2024-09-20 22:21:31.531 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.548 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.687 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.687 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3261753 | 1 | 17.8689 | 16.8436 | -115.7409 | 11.9696 | 118.1325 | 0.0159 | 0.0144 |
| 2024_09_20 22:00 | 3253058 | 2 | 9.5227 | 14.3333 | -117.9058 | 5.7837 | 134.0369 | 0.0092 | 0.0154 |
| 2024_09_20 22:00 | 3256824 | 3 | 19.1655 | 9.0422 | -114.7096 | 11.4348 | 190.7342 | 0.0114 | 0.0192 |
| 2024_09_20 22:00 | 3275437 | 4 | 10.0881 | 18.2726 | -109.1428 | 15.3845 | 196.1849 | 0.0135 | 0.0165 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413720_BE115A82 | 504990 | 325 | -92.0 | 504990 | 17 | -87.6 | 504990 | 258 | -87.5 | 504990 | 347 |
| MR_1774413720_D7321FCD | 504990 | 17 | -92.0 | 504990 | 325 | -86.0 | 504990 | 258 | -89.5 | 504990 | 347 |
| MR_1774413720_4BF0E21A | 504990 | 325 | -91.1 | 504990 | 17 | -86.3 | 504990 | 258 | -89.0 | 504990 | 347 |
| MR_1774413720_4D347A50 | 504990 | 325 | -89.7 | 504990 | 17 | -86.6 | 504990 | 258 | -87.1 | 504990 | 347 |
| MR_1774413720_BC4C76C9 | 504990 | 325 | -90.0 | 504990 | 17 | -87.1 | 504990 | 258 | -87.7 | 504990 | 347 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 845: `924b3337-c4d...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `924b3337-c4d2-473f-a350-e42f4c8bc028` |
| Tag | **multiple-answer** |
| 정답 | **C2|C21** |
| C2 의미 | Press down the tilt angle  of 3252116_4 by 4 degrees |
| C21 의미 | Decrease transmission power for 3252116_4 |
| 패턴 분류 | **P3 Overshoot (tilt)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[845] topology](images/train_0845.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3224438_1 by 6 degrees
- `C2`: Press down the tilt angle  of 3252116_4 by 4 degrees **← 정답**
- `C3`: Increase A3 Offset threshold for 3252116_4
- `C4`: Increase transmission power for 3252116_4
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3252116_4
- `C6`: Add neighbor relationship between 3224438_1 and 3252116_4
- `C7`: Insufficient data; more data is needed for judgment.
- `C8`: Increase A3 Offset threshold for 3224438_1
- `C9`: Check test server and transmission issues
- `C10`: Adjust the azimuth of 3224438_1 by 6 degrees
- `C11`: Press down the tilt angle of 3224438_1 by 6 degrees
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3252116_4
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3224438_1
- `C14`: Add neighbor relationship between 3277897_3 and 3252116_4
- `C15`: Decrease A3 Offset threshold for 3252116_4
- `C16`: Adjust the azimuth of 3252116_4 by 1 degrees
- `C17`: Decrease transmission power for 3224438_1
- `C18`: Lift the tilt angle  of 3252116_4 by 4 degrees
- `C19`: Decrease A3 Offset threshold for 3224438_1
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3224438_1
- `C21`: Decrease transmission power for 3252116_4 **← 정답**
- `C22`: Increase transmission power for 3224438_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.213 | MS1 | 121.4656688556 | 31.1446320701 | 568 | 504990 | -80.21 | 14.53 | 460.41 | 0.14 | 2.19 | 1566 |
| 2024-09-20 22:21:32.710 | MS1 | 121.4656715201 | 31.1446319556 | 568 | 504990 | -82.56 | 14.08 | 400.02 | 0.06 | 2.57 | 1592 |
| 2024-09-20 22:21:33.834 | MS1 | 121.4656733716 | 31.1446350400 | 568 | 504990 | -80.03 | 14.35 | 434.13 | 0.08 | 2.78 | 1585 |
| 2024-09-20 22:21:34.178 | MS1 | 121.4656661246 | 31.1446372925 | 568 | 504990 | -94.00 | 3.19 | 82.30 | 0.14 | 1.12 | 1580 |
| 2024-09-20 22:21:35.985 | MS1 | 121.4656583801 | 31.1446327924 | 568 | 504990 | -88.42 | 0.35 | 72.07 | 0.14 | 1.14 | 1573 |
| 2024-09-20 22:21:36.940 | MS1 | 121.4656757102 | 31.1446227890 | 568 | 504990 | -88.91 | 3.12 | 72.74 | 0.02 | 1.43 | 1570 |
| 2024-09-20 22:21:37.582 | MS1 | 121.4656631019 | 31.1446310406 | 568 | 504990 | -87.05 | 2.00 | 74.27 | 0.01 | 1.39 | 1583 |
| 2024-09-20 22:21:38.541 | MS1 | 121.4656661659 | 31.1446182758 | 568 | 504990 | -88.63 | 0.97 | 60.75 | 0.10 | 1.01 | 1573 |
| 2024-09-20 22:21:39.656 | MS1 | 121.4656656606 | 31.1446294788 | 568 | 504990 | -94.76 | 2.49 | 59.80 | 0.02 | 1.17 | 1597 |
| 2024-09-20 22:21:40.117 | MS1 | 121.4656751598 | 31.1446273587 | 568 | 504990 | -82.78 | 13.37 | 351.26 | 0.04 | 2.89 | 1598 |
| 2024-09-20 22:21:41.836 | MS1 | 121.4656700555 | 31.1446318834 | 568 | 504990 | -80.53 | 17.31 | 428.45 | 0.14 | 2.88 | 1596 |
| 2024-09-20 22:21:42.276 | MS1 | 121.4656605445 | 31.1446219036 | 568 | 504990 | -79.63 | 16.86 | 586.69 | 0.00 | 2.78 | 1581 |

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
| 3224438 | 1 | 121.4748878573 | 31.1491384104 | 246 | 4 | 0 | 30.9 | TDD | 568 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3235962 | 2 | 121.4651243687 | 31.1537741525 | 92 | 15 | 11 | 26.4 | TDD | 730 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3252116 | 4 | 121.4669557542 | 31.1510578729 | 189 | 2 | 10 | 22.8 | TDD | 1007 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3277897 | 3 | 121.4654905996 | 31.1556069754 | 48 | 10 | 12 | 33.8 | TDD | 802 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |

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
| 2024-09-20 22:21:31.189 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.207 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.312 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.312 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3224438 | 1 | 12.9298 | 10.2184 | -109.8027 | 11.0251 | 99.0625 | 0.0055 | 0.0096 |
| 2024_09_20 22:00 | 3235962 | 2 | 11.1921 | 13.6132 | -115.9514 | 16.3062 | 91.3922 | 0.0167 | 0.0017 |
| 2024_09_20 22:00 | 3277897 | 3 | 10.1845 | 16.6367 | -114.7775 | 5.9491 | 181.6527 | 0.0021 | 0.0194 |
| 2024_09_20 22:00 | 3252116 | 4 | 5.2939 | 9.6260 | -115.4145 | 19.8761 | 166.3570 | 0.0046 | 0.0096 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416518_587D99EC | 504990 | 568 | -94.3 | 504990 | 1007 | -92.6 | 504990 | 802 | -95.5 | 504990 | 730 |
| MR_1774416518_E18F287D | 504990 | 568 | -93.2 | 504990 | 1007 | -93.1 | 504990 | 802 | -95.6 | 504990 | 730 |
| MR_1774416518_490597B7 | 504990 | 568 | -92.5 | 504990 | 1007 | -93.0 | 504990 | 802 | -96.5 | 504990 | 730 |
| MR_1774416518_FD070251 | 504990 | 1007 | -92.1 | 504990 | 568 | -94.6 | 504990 | 802 | -94.4 | 504990 | 730 |
| MR_1774416518_94F8FB1B | 504990 | 568 | -95.4 | 504990 | 1007 | -94.4 | 504990 | 802 | -98.1 | 504990 | 730 |
| MR_1774416518_2CFA9298 | 504990 | 568 | -92.3 | 504990 | 1007 | -93.1 | 504990 | 802 | -95.8 | 504990 | 730 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 846: `a5b569d2-076...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `a5b569d2-0764-4610-a5c8-93d6e5fb10f9` |
| Tag | **single-answer** |
| 정답 | **C12** |
| C12 의미 | Lift the tilt angle  of 3259629_4 by 4 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[846] topology](images/train_0846.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Check test server and transmission issues
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3212020_2
- `C3`: Press down the tilt angle  of 3259629_4 by 4 degrees
- `C4`: Decrease transmission power for 3212020_2
- `C5`: Decrease transmission power for 3248872_1
- `C6`: Decrease A3 Offset threshold for 3212020_2
- `C7`: Increase A3 Offset threshold for 3212020_2
- `C8`: Adjust the azimuth of 3259629_4 by 50 degrees
- `C9`: Increase transmission power for 3212020_2
- `C10`: Add neighbor relationship between 3212020_2 and 3248872_1
- `C11`: Decrease A3 Offset threshold for 3248872_1
- `C12`: Lift the tilt angle  of 3259629_4 by 4 degrees **← 정답**
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3248872_1
- `C14`: Increase A3 Offset threshold for 3248872_1
- `C15`: Insufficient data; more data is needed for judgment.
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3212020_2
- `C17`: Increase transmission power for 3248872_1
- `C18`: Lift the tilt angle of 3212020_2 by 4 degrees
- `C19`: Adjust the azimuth of 3212020_2 by 43 degrees
- `C20`: Add neighbor relationship between 3259629_4 and 3248872_1
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3248872_1
- `C22`: Press down the tilt angle of 3212020_2 by 4 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.442 | MS1 | 121.4656581909 | 31.1446326149 | 442 | 504990 | -89.67 | 17.51 | 334.45 | 0.17 | 2.43 | 1589 |
| 2024-09-20 22:21:32.975 | MS1 | 121.4656698231 | 31.1446279714 | 442 | 504990 | -87.12 | 15.80 | 554.32 | 0.09 | 2.35 | 1561 |
| 2024-09-20 22:21:33.209 | MS1 | 121.4656618893 | 31.1446241253 | 442 | 504990 | -90.09 | 17.84 | 446.99 | 0.19 | 2.35 | 1578 |
| 2024-09-20 22:21:34.363 | MS1 | 121.4656690153 | 31.1446197726 | 442 | 504990 | -88.97 | 17.28 | 84.75 | 0.14 | 2.01 | 1571 |
| 2024-09-20 22:21:35.148 | MS1 | 121.4656662991 | 31.1446338150 | 442 | 504990 | -85.51 | 13.57 | 66.72 | 0.08 | 2.30 | 1593 |
| 2024-09-20 22:21:36.451 | MS1 | 121.4656725127 | 31.1446368071 | 442 | 504990 | -90.84 | 16.45 | 61.16 | 0.07 | 2.50 | 1560 |
| 2024-09-20 22:21:37.732 | MS1 | 121.4656596019 | 31.1446324314 | 442 | 504990 | -93.18 | 11.55 | 68.89 | 0.17 | 2.79 | 1586 |
| 2024-09-20 22:21:38.181 | MS1 | 121.4656734788 | 31.1446246040 | 442 | 504990 | -92.99 | 12.10 | 103.77 | 0.04 | 2.46 | 1582 |
| 2024-09-20 22:21:39.374 | MS1 | 121.4656694063 | 31.1446373017 | 442 | 504990 | -89.62 | 9.94 | 97.43 | 0.11 | 2.16 | 1573 |
| 2024-09-20 22:21:40.316 | MS1 | 121.4656765565 | 31.1446228874 | 442 | 504990 | -90.06 | 9.56 | 393.23 | 0.04 | 2.50 | 1565 |
| 2024-09-20 22:21:41.930 | MS1 | 121.4656743750 | 31.1446300719 | 442 | 504990 | -89.72 | 12.44 | 478.65 | 0.03 | 2.91 | 1589 |
| 2024-09-20 22:21:42.172 | MS1 | 121.4656633266 | 31.1446359932 | 442 | 504990 | -91.67 | 11.18 | 310.43 | 0.12 | 2.02 | 1580 |

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
| 3212020 | 2 | 121.4673781792 | 31.1497006346 | 239 | 1 | 8 | 33.5 | TDD | 442 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3248872 | 1 | 121.4732899051 | 31.1520175633 | 108 | 3 | 9 | 20.3 | TDD | 272 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3249687 | 3 | 121.4714416439 | 31.1497134284 | 352 | 13 | 0 | 17.5 | TDD | 10 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3259629 | 4 | 121.4721297982 | 31.1559748788 | 17 | 1 | 1 | 23.3 | TDD | 818 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |

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
| 2024-09-20 22:21:31.344 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.365 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.510 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.510 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.178 | NREventA3 | measId:2;ServCellPCI:750;Se... |
| 2024-09-20 22:21:38.418 | NRHandoverAttempt | SourcePCI:750;SourceNR-ARFC... |
| 2024-09-20 22:21:38.461 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.474 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.589 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.589 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3248872 | 1 | 17.4057 | 16.9859 | -116.8601 | 11.4472 | 189.4274 | 0.0072 | 0.0132 |
| 2024_09_20 22:00 | 3212020 | 2 | 75.5610 | 93.5996 | -115.7927 | 14.4354 | 137.3792 | 0.0011 | 0.0195 |
| 2024_09_20 22:00 | 3249687 | 3 | 5.4251 | 19.6927 | -116.3446 | 19.1534 | 156.8513 | 0.0073 | 0.0016 |
| 2024_09_20 22:00 | 3259629 | 4 | 16.1069 | 12.1431 | -115.6698 | 13.5853 | 147.0699 | 0.0017 | 0.0084 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414923_EB8EAE27 | 504990 | 442 | -88.3 | 504990 | 272 | -96.2 | 504990 | 818 | -101.4 | 504990 | 10 |
| MR_1774414923_F23CBF30 | 504990 | 442 | -89.0 | 504990 | 272 | -98.8 | 504990 | 818 | -102.9 | 504990 | 10 |
| MR_1774414923_B1D4640D | 504990 | 442 | -88.2 | 504990 | 272 | -97.9 | 504990 | 818 | -101.0 | 504990 | 10 |
| MR_1774414923_F43158BB | 504990 | 442 | -90.2 | 504990 | 272 | -96.8 | 504990 | 818 | -101.8 | 504990 | 10 |
| MR_1774414923_8D357A93 | 504990 | 442 | -87.8 | 504990 | 272 | -97.4 | 504990 | 818 | -101.5 | 504990 | 10 |
| MR_1774414923_129F86D7 | 504990 | 442 | -89.5 | 504990 | 272 | -98.7 | 504990 | 818 | -101.8 | 504990 | 10 |
| MR_1774414923_37BE85A3 | 504990 | 442 | -90.4 | 504990 | 272 | -96.5 | 504990 | 818 | -103.0 | 504990 | 10 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 847: `a9e3881a-759...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `a9e3881a-759c-4c68-b33a-2586326744fd` |
| Tag | **single-answer** |
| 정답 | **C21** |
| C21 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[847] topology](images/train_0847.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3264422_4
- `C2`: Adjust the azimuth of 3250026_2 by 50 degrees
- `C3`: Decrease transmission power for 3250026_2
- `C4`: Adjust the azimuth of 3264422_4 by 50 degrees
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3250026_2
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3250026_2
- `C7`: Press down the tilt angle of 3264422_4 by 10 degrees
- `C8`: Increase A3 Offset threshold for 3250026_2
- `C9`: Increase A3 Offset threshold for 3264422_4
- `C10`: Lift the tilt angle of 3264422_4 by 10 degrees
- `C11`: Increase transmission power for 3250026_2
- `C12`: Insufficient data; more data is needed for judgment.
- `C13`: Decrease A3 Offset threshold for 3264422_4
- `C14`: Lift the tilt angle  of 3250026_2 by 6 degrees
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3264422_4
- `C16`: Press down the tilt angle  of 3250026_2 by 6 degrees
- `C17`: Add neighbor relationship between 3264422_4 and 3250026_2
- `C18`: Increase transmission power for 3264422_4
- `C19`: Add neighbor relationship between 3259303_1 and 3250026_2
- `C20`: Decrease transmission power for 3264422_4
- `C21`: Check test server and transmission issues **← 정답**
- `C22`: Decrease A3 Offset threshold for 3250026_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.475 | MS1 | 121.4656743361 | 31.1446297989 | 847 | 504990 | -91.69 | 12.43 | 547.38 | 0.16 | 2.72 | 1587 |
| 2024-09-20 22:21:32.980 | MS1 | 121.4656714107 | 31.1446230644 | 847 | 504990 | -91.43 | 14.10 | 387.83 | 0.01 | 2.55 | 1576 |
| 2024-09-20 22:21:33.680 | MS1 | 121.4656670412 | 31.1446281574 | 847 | 504990 | -88.19 | 16.67 | 321.98 | 0.18 | 2.33 | 1580 |
| 2024-09-20 22:21:34.678 | MS1 | 121.4656644176 | 31.1446238134 | 847 | 504990 | -90.15 | 16.78 | 89.52 | 0.18 | 2.64 | 334 |
| 2024-09-20 22:21:35.163 | MS1 | 121.4656774011 | 31.1446371638 | 847 | 504990 | -89.70 | 15.90 | 69.84 | 0.16 | 2.46 | 412 |
| 2024-09-20 22:21:36.288 | MS1 | 121.4656649440 | 31.1446203185 | 847 | 504990 | -86.49 | 16.84 | 91.06 | 0.10 | 2.33 | 411 |
| 2024-09-20 22:21:37.990 | MS1 | 121.4656686042 | 31.1446298065 | 847 | 504990 | -89.88 | 10.48 | 97.67 | 0.03 | 2.97 | 346 |
| 2024-09-20 22:21:38.371 | MS1 | 121.4656761939 | 31.1446350888 | 847 | 504990 | -93.53 | 10.85 | 59.96 | 0.07 | 2.01 | 349 |
| 2024-09-20 22:21:39.333 | MS1 | 121.4656728890 | 31.1446373604 | 847 | 504990 | -92.85 | 10.30 | 87.98 | 0.02 | 2.87 | 407 |
| 2024-09-20 22:21:40.702 | MS1 | 121.4656721097 | 31.1446340234 | 847 | 504990 | -93.41 | 7.59 | 410.22 | 0.00 | 2.69 | 1575 |
| 2024-09-20 22:21:41.230 | MS1 | 121.4656626118 | 31.1446356389 | 847 | 504990 | -92.56 | 10.72 | 479.03 | 0.02 | 2.09 | 1563 |
| 2024-09-20 22:21:42.443 | MS1 | 121.4656655203 | 31.1446272001 | 847 | 504990 | -93.15 | 11.45 | 484.91 | 0.06 | 2.10 | 1565 |

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
| 3215862 | 3 | 121.4750096152 | 31.1527938996 | 127 | 1 | 11 | 32.1 | TDD | 620 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3250026 | 2 | 121.4643073310 | 31.1497638430 | 352 | 4 | 8 | 23.9 | TDD | 827 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3259303 | 1 | 121.4662118713 | 31.1479002271 | 185 | 5 | 11 | 43.2 | TDD | 385 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3264422 | 4 | 121.4690814314 | 31.1447057462 | 72 | 11 | 8 | 46.3 | TDD | 847 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |

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
| 2024-09-20 22:21:30.818 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.841 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:30.952 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.952 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.659 | NREventA3 | measId:2;ServCellPCI:861;Se... |
| 2024-09-20 22:21:37.899 | NRHandoverAttempt | SourcePCI:861;SourceNR-ARFC... |
| 2024-09-20 22:21:37.945 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.959 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.103 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.103 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3259303 | 1 | 17.1806 | 19.6197 | -114.2978 | 5.0449 | 188.9227 | 0.0172 | 0.0035 |
| 2024_09_20 22:00 | 3250026 | 2 | 19.0531 | 16.1601 | -116.3805 | 7.3057 | 169.7783 | 0.0051 | 0.0071 |
| 2024_09_20 22:00 | 3215862 | 3 | 5.4531 | 15.7439 | -114.9357 | 10.4926 | 191.4209 | 0.0150 | 0.0129 |
| 2024_09_20 22:00 | 3264422 | 4 | 14.0828 | 13.3173 | -115.3835 | 11.7698 | 101.9271 | 0.0015 | 0.0176 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413781_79B4B542 | 504990 | 847 | -89.0 | 504990 | 827 | -95.2 | 504990 | 385 | -104.9 | 504990 | 620 |
| MR_1774413781_35C89D30 | 504990 | 847 | -90.9 | 504990 | 827 | -95.6 | 504990 | 385 | -102.6 | 504990 | 620 |
| MR_1774413781_25431F16 | 504990 | 847 | -88.6 | 504990 | 827 | -94.2 | 504990 | 385 | -103.9 | 504990 | 620 |
| MR_1774413781_C0231E1E | 504990 | 847 | -90.4 | 504990 | 827 | -93.0 | 504990 | 385 | -102.5 | 504990 | 620 |
| MR_1774413781_B59FAC42 | 504990 | 847 | -91.8 | 504990 | 827 | -94.2 | 504990 | 385 | -101.4 | 504990 | 620 |
| MR_1774413781_4BC48EEF | 504990 | 847 | -89.3 | 504990 | 827 | -92.9 | 504990 | 385 | -104.6 | 504990 | 620 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 848: `311aca6b-105...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `311aca6b-1058-41c0-97bf-2827ce3ab832` |
| Tag | **single-answer** |
| 정답 | **C3** |
| C3 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3223768_3 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[848] topology](images/train_0848.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3223768_3
- `C2`: Check test server and transmission issues
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3223768_3 **← 정답**
- `C4`: Press down the tilt angle  of 3251602_2 by 10 degrees
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3251602_2
- `C6`: Decrease A3 Offset threshold for 3223768_3
- `C7`: Lift the tilt angle of 3223768_3 by 3 degrees
- `C8`: Adjust the azimuth of 3251602_2 by 50 degrees
- `C9`: Increase A3 Offset threshold for 3251602_2
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3223768_3
- `C11`: Decrease transmission power for 3223768_3
- `C12`: Add neighbor relationship between 3223768_3 and 3251602_2
- `C13`: Increase transmission power for 3223768_3
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Increase transmission power for 3251602_2
- `C16`: Add neighbor relationship between 3211289_4 and 3251602_2
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3251602_2
- `C18`: Adjust the azimuth of 3223768_3 by 20 degrees
- `C19`: Lift the tilt angle  of 3251602_2 by 10 degrees
- `C20`: Decrease transmission power for 3251602_2
- `C21`: Decrease A3 Offset threshold for 3251602_2
- `C22`: Press down the tilt angle of 3223768_3 by 3 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.461 | MS1 | 121.4656629261 | 31.1446347555 | 483 | 504990 | -85.22 | 13.36 | 364.98 | 0.18 | 2.17 | 1571 |
| 2024-09-20 22:21:32.256 | MS1 | 121.4656589014 | 31.1446217456 | 483 | 504990 | -86.39 | 15.65 | 552.99 | 0.05 | 2.65 | 1562 |
| 2024-09-20 22:21:33.182 | MS1 | 121.4656750173 | 31.1446368829 | 483 | 504990 | -88.84 | 17.62 | 422.03 | 0.04 | 2.33 | 1591 |
| 2024-09-20 22:21:34.199 | MS1 | 121.4656665761 | 31.1446192138 | 483 | 504990 | -87.23 | 13.89 | 73.67 | 0.52 | 2.89 | 668 |
| 2024-09-20 22:21:35.688 | MS1 | 121.4656759251 | 31.1446227504 | 483 | 504990 | -88.36 | 16.29 | 65.60 | 0.56 | 2.68 | 697 |
| 2024-09-20 22:21:36.616 | MS1 | 121.4656770849 | 31.1446265992 | 483 | 504990 | -85.33 | 14.32 | 95.25 | 0.50 | 2.78 | 514 |
| 2024-09-20 22:21:37.541 | MS1 | 121.4656766066 | 31.1446379753 | 483 | 504990 | -89.07 | 7.93 | 91.78 | 0.68 | 2.63 | 681 |
| 2024-09-20 22:21:38.730 | MS1 | 121.4656624727 | 31.1446218939 | 483 | 504990 | -89.06 | 11.59 | 100.89 | 0.59 | 2.74 | 697 |
| 2024-09-20 22:21:39.962 | MS1 | 121.4656738312 | 31.1446262468 | 483 | 504990 | -89.03 | 10.47 | 75.15 | 0.59 | 2.49 | 692 |
| 2024-09-20 22:21:40.435 | MS1 | 121.4656641892 | 31.1446280827 | 483 | 504990 | -90.28 | 12.87 | 594.03 | 0.18 | 2.07 | 1563 |
| 2024-09-20 22:21:41.162 | MS1 | 121.4656615446 | 31.1446221184 | 483 | 504990 | -91.33 | 8.74 | 456.84 | 0.08 | 2.01 | 1585 |
| 2024-09-20 22:21:42.212 | MS1 | 121.4656669327 | 31.1446371843 | 483 | 504990 | -90.06 | 9.51 | 311.25 | 0.01 | 2.96 | 1561 |

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
| 3211289 | 4 | 121.4657127013 | 31.1465632127 | 40 | 4 | 8 | 41.0 | TDD | 518 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3223768 | 3 | 121.4706481025 | 31.1484332658 | 248 | 1 | 9 | 24.4 | TDD | 483 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3248090 | 1 | 121.4649480184 | 31.1506271697 | 310 | 5 | 10 | 43.6 | TDD | 153 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3251602 | 2 | 121.4723382947 | 31.1474225707 | 99 | 9 | 4 | 28.7 | TDD | 890 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |

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
| 2024-09-20 22:21:30.818 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:30.942 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.942 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.688 | NREventA3 | measId:2;ServCellPCI:555;Se... |
| 2024-09-20 22:21:37.928 | NRHandoverAttempt | SourcePCI:555;SourceNR-ARFC... |
| 2024-09-20 22:21:37.959 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.973 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.075 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.075 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3248090 | 1 | 9.5975 | 10.6682 | -114.2545 | 9.0522 | 109.0569 | 0.0057 | 0.0060 |
| 2024_09_20 22:00 | 3251602 | 2 | 8.5547 | 10.3980 | -114.8470 | 13.1639 | 83.0291 | 0.0033 | 0.0169 |
| 2024_09_20 22:00 | 3223768 | 3 | 15.9727 | 10.6168 | -115.6821 | 11.1373 | 175.0110 | 0.0193 | 0.0082 |
| 2024_09_20 22:00 | 3211289 | 4 | 6.0984 | 10.7985 | -116.1924 | 10.4735 | 169.4097 | 0.0008 | 0.0198 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412250_DBCCA9EA | 504990 | 483 | -85.4 | 504990 | 890 | -90.3 | 504990 | 518 | -99.3 | 504990 | 153 |
| MR_1774412250_D2E2E9F5 | 504990 | 483 | -85.7 | 504990 | 890 | -92.2 | 504990 | 518 | -101.7 | 504990 | 153 |
| MR_1774412250_3F6DB229 | 504990 | 483 | -85.5 | 504990 | 890 | -92.9 | 504990 | 518 | -100.3 | 504990 | 153 |
| MR_1774412250_926FE1AD | 504990 | 483 | -87.7 | 504990 | 890 | -92.6 | 504990 | 518 | -99.7 | 504990 | 153 |
| MR_1774412250_3A763323 | 504990 | 483 | -86.5 | 504990 | 890 | -93.3 | 504990 | 518 | -98.9 | 504990 | 153 |
| MR_1774412250_6973ED3D | 504990 | 483 | -86.5 | 504990 | 890 | -89.8 | 504990 | 518 | -100.9 | 504990 | 153 |
| MR_1774412250_F70BE2BE | 504990 | 483 | -85.2 | 504990 | 890 | -91.8 | 504990 | 518 | -99.7 | 504990 | 153 |
| MR_1774412250_EBEE8E16 | 504990 | 483 | -88.8 | 504990 | 890 | -90.3 | 504990 | 518 | -101.8 | 504990 | 153 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 849: `8ba5c377-666...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `8ba5c377-6665-4ac3-83bc-5073f90baa88` |
| Tag | **single-answer** |
| 정답 | **C11** |
| C11 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3232788_1 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[849] topology](images/train_0849.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3232788_1 and 3238869_2
- `C2`: Increase transmission power for 3238869_2
- `C3`: Lift the tilt angle  of 3238869_2 by 5 degrees
- `C4`: Decrease A3 Offset threshold for 3232788_1
- `C5`: Adjust the azimuth of 3238869_2 by 50 degrees
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3232788_1
- `C7`: Decrease A3 Offset threshold for 3238869_2
- `C8`: Add neighbor relationship between 3270402_4 and 3238869_2
- `C9`: Increase A3 Offset threshold for 3232788_1
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3238869_2
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3232788_1 **← 정답**
- `C12`: Increase A3 Offset threshold for 3238869_2
- `C13`: Increase transmission power for 3232788_1
- `C14`: Press down the tilt angle of 3232788_1 by 1 degrees
- `C15`: Lift the tilt angle of 3232788_1 by 1 degrees
- `C16`: Decrease transmission power for 3238869_2
- `C17`: Press down the tilt angle  of 3238869_2 by 5 degrees
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3238869_2
- `C19`: Adjust the azimuth of 3232788_1 by 37 degrees
- `C20`: Insufficient data; more data is needed for judgment.
- `C21`: Decrease transmission power for 3232788_1
- `C22`: Check test server and transmission issues

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.749 | MS1 | 121.4656650265 | 31.1446232820 | 379 | 504990 | -87.41 | 14.24 | 502.20 | 0.15 | 2.75 | 1600 |
| 2024-09-20 22:21:32.513 | MS1 | 121.4656729972 | 31.1446216893 | 379 | 504990 | -89.01 | 12.13 | 404.79 | 0.14 | 2.10 | 1585 |
| 2024-09-20 22:21:33.506 | MS1 | 121.4656580017 | 31.1446199253 | 379 | 504990 | -90.23 | 16.62 | 547.47 | 0.15 | 2.91 | 1562 |
| 2024-09-20 22:21:34.313 | MS1 | 121.4656691110 | 31.1446246127 | 379 | 504990 | -89.72 | 12.22 | 86.76 | 0.62 | 2.51 | 630 |
| 2024-09-20 22:21:35.777 | MS1 | 121.4656768069 | 31.1446180875 | 379 | 504990 | -89.71 | 14.01 | 93.82 | 0.56 | 2.43 | 502 |
| 2024-09-20 22:21:36.640 | MS1 | 121.4656688505 | 31.1446186715 | 379 | 504990 | -86.70 | 15.22 | 97.06 | 0.55 | 2.90 | 611 |
| 2024-09-20 22:21:37.123 | MS1 | 121.4656683528 | 31.1446301156 | 379 | 504990 | -93.50 | 8.85 | 81.34 | 0.56 | 2.32 | 665 |
| 2024-09-20 22:21:38.174 | MS1 | 121.4656688084 | 31.1446249657 | 379 | 504990 | -92.65 | 10.22 | 69.79 | 0.51 | 2.64 | 583 |
| 2024-09-20 22:21:39.183 | MS1 | 121.4656593645 | 31.1446331310 | 379 | 504990 | -92.59 | 12.03 | 78.87 | 0.52 | 2.54 | 521 |
| 2024-09-20 22:21:40.550 | MS1 | 121.4656629891 | 31.1446374664 | 379 | 504990 | -93.22 | 11.83 | 377.32 | 0.01 | 2.22 | 1589 |
| 2024-09-20 22:21:41.629 | MS1 | 121.4656601785 | 31.1446340186 | 379 | 504990 | -90.29 | 12.80 | 420.54 | 0.15 | 2.42 | 1561 |
| 2024-09-20 22:21:42.596 | MS1 | 121.4656644198 | 31.1446261967 | 379 | 504990 | -93.50 | 7.29 | 576.53 | 0.12 | 2.96 | 1600 |

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
| 3211414 | 3 | 121.4707204437 | 31.1458246806 | 285 | 5 | 2 | 15.3 | TDD | 550 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3232788 | 1 | 121.4748306620 | 31.1534854889 | 259 | 0 | 6 | 33.6 | TDD | 379 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3238869 | 2 | 121.4691113265 | 31.1494298915 | 48 | 2 | 10 | 27.9 | TDD | 771 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3270402 | 4 | 121.4758664522 | 31.1507356255 | 20 | 8 | 4 | 26.5 | TDD | 863 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |

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
| 2024-09-20 22:21:31.045 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.154 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.154 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.930 | NREventA3 | measId:2;ServCellPCI:861;Se... |
| 2024-09-20 22:21:38.170 | NRHandoverAttempt | SourcePCI:861;SourceNR-ARFC... |
| 2024-09-20 22:21:38.205 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.218 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.322 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.322 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3232788 | 1 | 11.6180 | 10.5009 | -116.4947 | 15.0698 | 126.7065 | 0.0031 | 0.0043 |
| 2024_09_20 22:00 | 3238869 | 2 | 15.9578 | 9.1512 | -116.3533 | 11.8584 | 196.8436 | 0.0049 | 0.0045 |
| 2024_09_20 22:00 | 3211414 | 3 | 10.2220 | 7.4324 | -116.3799 | 14.0432 | 80.2558 | 0.0078 | 0.0086 |
| 2024_09_20 22:00 | 3270402 | 4 | 16.3857 | 14.1623 | -117.0881 | 17.4860 | 163.8856 | 0.0123 | 0.0060 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412745_1AE5448A | 504990 | 379 | -90.4 | 504990 | 771 | -98.2 | 504990 | 863 | -97.0 | 504990 | 550 |
| MR_1774412745_72DC4D11 | 504990 | 379 | -90.5 | 504990 | 771 | -95.6 | 504990 | 863 | -97.9 | 504990 | 550 |
| MR_1774412745_466AF8C4 | 504990 | 379 | -87.8 | 504990 | 771 | -98.7 | 504990 | 863 | -97.3 | 504990 | 550 |
| MR_1774412745_AAA29585 | 504990 | 379 | -91.7 | 504990 | 771 | -96.4 | 504990 | 863 | -98.4 | 504990 | 550 |
| MR_1774412745_558B127E | 504990 | 379 | -89.2 | 504990 | 771 | -96.4 | 504990 | 863 | -97.9 | 504990 | 550 |

> *... 2개 열 생략 (전체 14열)*

---
