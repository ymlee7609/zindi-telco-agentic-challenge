# Track A 문제 분석 — train[1050]~train[1059]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[1050] ~ train[1059] (10개)

## 목차

1. [문제 1050: `9a8ba85d-ee9...`](#1050) — single-answer, 정답: C7
2. [문제 1051: `c921cc86-93a...`](#1051) — single-answer, 정답: C15
3. [문제 1052: `553bbd7f-9af...`](#1052) — single-answer, 정답: C9
4. [문제 1053: `586b0b83-b62...`](#1053) — single-answer, 정답: C22
5. [문제 1054: `5d480ab4-d3a...`](#1054) — single-answer, 정답: C13
6. [문제 1055: `3e75b0c8-162...`](#1055) — single-answer, 정답: C5
7. [문제 1056: `04cfe46f-c2f...`](#1056) — single-answer, 정답: C18
8. [문제 1057: `c9112de4-2be...`](#1057) — single-answer, 정답: C10
9. [문제 1058: `ae5f74e0-216...`](#1058) — multiple-answer, 정답: C6|C21
10. [문제 1059: `f0dd52b1-eb8...`](#1059) — single-answer, 정답: C8

---

### 문제 1050: `9a8ba85d-ee9...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `9a8ba85d-ee93-4c94-bad8-3581b136f0b7` |
| Tag | **single-answer** |
| 정답 | **C7** |
| C7 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1050] topology](images/train_1050.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3212479_2
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3212479_2
- `C3`: Add neighbor relationship between 3227609_3 and 3212479_2
- `C4`: Press down the tilt angle  of 3212479_2 by 10 degrees
- `C5`: Add neighbor relationship between 3214442_4 and 3212479_2
- `C6`: Decrease transmission power for 3227609_3
- `C7`: Insufficient data; more data is needed for judgment. **← 정답**
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3227609_3
- `C9`: Increase A3 Offset threshold for 3212479_2
- `C10`: Increase transmission power for 3227609_3
- `C11`: Check test server and transmission issues
- `C12`: Lift the tilt angle  of 3212479_2 by 10 degrees
- `C13`: Lift the tilt angle of 3227609_3 by 10 degrees
- `C14`: Press down the tilt angle of 3227609_3 by 10 degrees
- `C15`: Adjust the azimuth of 3212479_2 by 13 degrees
- `C16`: Adjust the azimuth of 3227609_3 by 50 degrees
- `C17`: Increase transmission power for 3212479_2
- `C18`: Decrease A3 Offset threshold for 3212479_2
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3227609_3
- `C20`: Increase A3 Offset threshold for 3227609_3
- `C21`: Decrease A3 Offset threshold for 3227609_3
- `C22`: Decrease transmission power for 3212479_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.513 | MS1 | 121.4656761822 | 31.1446215806 | 324 | 504990 | -91.82 | 13.13 | 318.53 | 0.15 | 2.31 | 1580 |
| 2024-09-20 22:21:32.790 | MS1 | 121.4656608998 | 31.1446190689 | 324 | 504990 | -88.23 | 13.14 | 541.40 | 0.08 | 2.11 | 1564 |
| 2024-09-20 22:21:33.928 | MS1 | 121.4656679074 | 31.1446352118 | 324 | 504990 | -91.37 | 15.98 | 313.06 | 0.08 | 2.68 | 1564 |
| 2024-09-20 22:21:34.371 | MS1 | 121.4656749709 | 31.1446261052 | 324 | 504990 | -90.60 | 12.96 | 74.66 | 0.16 | 2.11 | 1571 |
| 2024-09-20 22:21:35.382 | MS1 | 121.4656645493 | 31.1446193214 | 324 | 504990 | -87.65 | 15.26 | 46.05 | 0.19 | 2.88 | 1590 |
| 2024-09-20 22:21:36.358 | MS1 | 121.4656658428 | 31.1446280169 | 324 | 504990 | -88.41 | 16.37 | 68.75 | 0.17 | 2.25 | 1578 |
| 2024-09-20 22:21:37.462 | MS1 | 121.4656620366 | 31.1446302931 | 324 | 504990 | -89.19 | 12.74 | 64.74 | 0.08 | 2.55 | 1590 |
| 2024-09-20 22:21:38.819 | MS1 | 121.4656627436 | 31.1446250163 | 324 | 504990 | -90.40 | 12.95 | 76.58 | 0.01 | 2.58 | 1577 |
| 2024-09-20 22:21:39.502 | MS1 | 121.4656727601 | 31.1446299202 | 324 | 504990 | -92.63 | 10.42 | 85.75 | 0.15 | 2.57 | 1560 |
| 2024-09-20 22:21:40.671 | MS1 | 121.4656755170 | 31.1446258312 | 324 | 504990 | -90.70 | 7.09 | 443.99 | 0.16 | 2.47 | 1591 |
| 2024-09-20 22:21:41.419 | MS1 | 121.4656737915 | 31.1446295401 | 324 | 504990 | -90.68 | 12.02 | 480.44 | 0.03 | 2.16 | 1565 |
| 2024-09-20 22:21:42.556 | MS1 | 121.4656634990 | 31.1446333008 | 324 | 504990 | -90.76 | 10.35 | 402.90 | 0.10 | 2.45 | 1595 |

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
| 3212479 | 2 | 121.4672190210 | 31.1446718140 | 281 | 10 | 8 | 26.0 | TDD | 666 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3214442 | 4 | 121.4747633847 | 31.1547810052 | 62 | 8 | 4 | 24.8 | TDD | 46 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3227609 | 3 | 121.4648617258 | 31.1503954951 | 98 | 11 | 2 | 15.3 | TDD | 324 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3243085 | 1 | 121.4696284945 | 31.1459223498 | 251 | 8 | 11 | 15.4 | TDD | 648 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:30.869 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.890 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.015 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.015 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.730 | NREventA3 | measId:2;ServCellPCI:951;Se... |
| 2024-09-20 22:21:37.970 | NRHandoverAttempt | SourcePCI:951;SourceNR-ARFC... |
| 2024-09-20 22:21:38.008 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.019 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.121 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.121 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3243085 | 1 | 90.6480 | 78.2575 | -114.8703 | 13.0692 | 180.6763 | 0.0162 | 0.0184 |
| 2024_09_19 22:00 | 3212479 | 2 | 81.2297 | 86.3424 | -115.7322 | 7.4385 | 175.4927 | 0.0191 | 0.0087 |
| 2024_09_19 22:00 | 3227609 | 3 | 84.3489 | 90.9497 | -115.1001 | 10.8887 | 113.2233 | 0.0132 | 0.0020 |
| 2024_09_19 22:00 | 3214442 | 4 | 88.6273 | 78.7243 | -117.3542 | 9.9468 | 91.4938 | 0.0068 | 0.0193 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415556_56991C87 | 504990 | 324 | -89.5 | 504990 | 666 | -98.5 | 504990 | 46 | -103.9 | 504990 | 648 |
| MR_1774415556_849356D2 | 504990 | 324 | -91.9 | 504990 | 666 | -98.6 | 504990 | 46 | -105.1 | 504990 | 648 |
| MR_1774415556_F0DFA486 | 504990 | 324 | -89.4 | 504990 | 666 | -100.2 | 504990 | 46 | -102.3 | 504990 | 648 |
| MR_1774415556_19AC8F34 | 504990 | 324 | -89.3 | 504990 | 666 | -99.6 | 504990 | 46 | -102.0 | 504990 | 648 |
| MR_1774415556_E0BFE6D2 | 504990 | 324 | -89.4 | 504990 | 666 | -100.2 | 504990 | 46 | -105.7 | 504990 | 648 |
| MR_1774415556_5E95C442 | 504990 | 324 | -90.7 | 504990 | 666 | -97.9 | 504990 | 46 | -105.4 | 504990 | 648 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1051: `c921cc86-93a...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `c921cc86-93a0-4bd1-b99c-71be7047de28` |
| Tag | **single-answer** |
| 정답 | **C15** |
| C15 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3265550_6 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1051] topology](images/train_1051.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3243370_11 and 3215933_4
- `C2`: Insufficient data; more data is needed for judgment.
- `C3`: Decrease transmission power for 3215933_4
- `C4`: Press down the tilt angle of 3265550_6 by 6 degrees
- `C5`: Decrease A3 Offset threshold for 3215933_4
- `C6`: Increase transmission power for 3215933_4
- `C7`: Adjust the azimuth of 3215933_4 by 5 degrees
- `C8`: Decrease transmission power for 3265550_6
- `C9`: Increase transmission power for 3265550_6
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3215933_4
- `C11`: Lift the tilt angle  of 3215933_4 by 6 degrees
- `C12`: Adjust the azimuth of 3265550_6 by 37 degrees
- `C13`: Increase A3 Offset threshold for 3265550_6
- `C14`: Increase A3 Offset threshold for 3215933_4
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3265550_6 **← 정답**
- `C16`: Lift the tilt angle of 3265550_6 by 6 degrees
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3265550_6
- `C18`: Check test server and transmission issues
- `C19`: Press down the tilt angle  of 3215933_4 by 6 degrees
- `C20`: Decrease A3 Offset threshold for 3265550_6
- `C21`: Add neighbor relationship between 3265550_6 and 3215933_4
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3215933_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.480 | MS1 | 121.4656589438 | 31.1446257040 | 479 | 504990 | -95.80 | 11.58 | 504.62 | 0.13 | 2.83 | 1576 |
| 2024-09-20 22:21:32.833 | MS1 | 121.4656662689 | 31.1446353522 | 705 | 504990 | -93.66 | 9.39 | 557.08 | 0.02 | 2.52 | 1564 |
| 2024-09-20 22:21:33.211 | MS1 | 121.4656712540 | 31.1446353667 | 971 | 504990 | -94.63 | 9.11 | 473.37 | 0.07 | 2.76 | 1572 |
| 2024-09-20 22:21:34.842 | MS1 | 121.4656758792 | 31.1446331256 | 868 | 152650 | -95.37 | 5.75 | 98.27 | 0.05 | 1.62 | 949 |
| 2024-09-20 22:21:35.470 | MS1 | 121.4656586051 | 31.1446338516 | 686 | 152650 | -88.26 | 7.66 | 58.96 | 0.08 | 1.75 | 912 |
| 2024-09-20 22:21:36.129 | MS1 | 121.4656742317 | 31.1446310064 | 213 | 152650 | -90.67 | 6.97 | 47.56 | 0.04 | 1.67 | 925 |
| 2024-09-20 22:21:37.526 | MS1 | 121.4656695750 | 31.1446269943 | 306 | 152650 | -90.85 | 2.45 | 56.42 | 0.06 | 1.59 | 930 |
| 2024-09-20 22:21:38.993 | MS1 | 121.4656656421 | 31.1446187651 | 868 | 152650 | -92.63 | 3.35 | 92.69 | 0.08 | 1.73 | 924 |
| 2024-09-20 22:21:39.960 | MS1 | 121.4656769059 | 31.1446216113 | 686 | 152650 | -95.84 | 3.41 | 69.78 | 0.16 | 1.92 | 923 |
| 2024-09-20 22:21:40.238 | MS1 | 121.4656738939 | 31.1446344728 | 213 | 152650 | -87.49 | 2.18 | 66.04 | 0.15 | 2.17 | 1589 |
| 2024-09-20 22:21:41.970 | MS1 | 121.4656688741 | 31.1446378322 | 306 | 152650 | -87.63 | 6.18 | 70.02 | 0.09 | 2.84 | 1578 |
| 2024-09-20 22:21:42.476 | MS1 | 121.4656703303 | 31.1446197112 | 868 | 152650 | -87.14 | 7.48 | 73.14 | 0.04 | 2.17 | 1567 |

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
| 3214003 | 2 | 121.4662461882 | 31.1546144269 | 312 | 1 | 6 | 20.1 | TDD | 971 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3215933 | 4 | 121.4721878795 | 31.1485834124 | 230 | 4 | 6 | 25.4 | TDD | 501 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3243370 | 11 | 121.4716744250 | 31.1483677423 | 315 | 2 | 7 | 27.9 | FDD | 213 | n1 | 152650 | 30M | 4T4R | 15 | 152650 |
| 3243391 | 7 | 121.4743424028 | 31.1550938658 | 343 | 7 | 2 | 12.1 | FDD | 868 | n1 | 152650 | 30M | 4T4R | 23 | 152650 |
| 3246779 | 3 | 121.4643803384 | 31.1513094911 | 15 | 11 | 8 | 12.2 | TDD | 173 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3247338 | 9 | 121.4670735922 | 31.1487884874 | 229 | 6 | 1 | 2.5 | FDD | 175 | n1 | 152650 | 30M | 4T4R | 17 | 152650 |
| 3250105 | 5 | 121.4643454855 | 31.1448565887 | 142 | 10 | 8 | 15.1 | TDD | 311 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3256060 | 12 | 121.4655975498 | 31.1452949172 | 37 | 3 | 7 | 19.6 | FDD | 22 | n1 | 152650 | 30M | 4T4R | 12 | 152650 |
| 3258267 | 1 | 121.4654403516 | 31.1493056689 | 137 | 3 | 8 | 27.7 | TDD | 705 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3263801 | 10 | 121.4653904729 | 31.1522638161 | 221 | 9 | 9 | 20.7 | FDD | 306 | n1 | 152650 | 30M | 4T4R | 23 | 152650 |
| 3265550 | 6 | 121.4702531842 | 31.1505144950 | 177 | 4 | 5 | 25.7 | TDD | 479 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3268191 | 13 | 121.4649525693 | 31.1489216091 | 264 | 0 | 8 | 13.6 | FDD | 989 | n1 | 152650 | 30M | 4T4R | 28 | 152650 |
| 3273409 | 8 | 121.4711011604 | 31.1484257369 | 175 | 8 | 0 | 0.6 | FDD | 686 | n1 | 152650 | 30M | 4T4R | 15 | 152650 |

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
| 2024-09-20 22:21:30.805 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.820 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:30.962 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.962 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.619 | NREventA2 | measId:1;ServCellPCI:254;Se... |
| 2024-09-20 22:21:34.759 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.031 | NREventA5 | measId:3;ServCellPCI:254;Se... |
| 2024-09-20 22:21:35.104 | NRHandoverAttempt | SourcePCI:254;SourceNR-ARFC... |
| 2024-09-20 22:21:35.143 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.153 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:35.301 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.301 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3258267 | 1 | 19.9485 | 18.4487 | -114.8184 | 7.8280 | 124.3771 | 0.0197 | 0.0058 |
| 2024_09_20 22:00 | 3214003 | 2 | 8.5239 | 17.9698 | -117.1280 | 16.5948 | 155.9065 | 0.0190 | 0.0132 |
| 2024_09_20 22:00 | 3246779 | 3 | 12.2887 | 6.6565 | -114.6333 | 5.9373 | 194.0862 | 0.0144 | 0.0156 |
| 2024_09_20 22:00 | 3215933 | 4 | 13.8575 | 15.1137 | -117.1946 | 11.3478 | 87.1135 | 0.0050 | 0.0136 |
| 2024_09_20 22:00 | 3250105 | 5 | 12.9596 | 8.7122 | -116.4377 | 11.4276 | 108.2001 | 0.0087 | 0.0185 |
| 2024_09_20 22:00 | 3265550 | 6 | 7.1430 | 12.3168 | -115.7700 | 15.6898 | 184.4227 | 0.0005 | 0.0173 |
| 2024_09_20 22:00 | 3243391 | 7 | 11.3806 | 11.0609 | -114.8584 | 4.0932 | 42.5803 | 0.0074 | 0.0144 |
| 2024_09_20 22:00 | 3273409 | 8 | 8.6494 | 13.2960 | -117.2739 | 3.1484 | 52.4673 | 0.0194 | 0.0108 |
| 2024_09_20 22:00 | 3247338 | 9 | 12.4112 | 7.4892 | -117.1933 | 4.0260 | 32.3120 | 0.0079 | 0.0029 |
| 2024_09_20 22:00 | 3263801 | 10 | 6.1836 | 17.0381 | -114.0797 | 3.7323 | 23.5783 | 0.0044 | 0.0057 |
| 2024_09_20 22:00 | 3243370 | 11 | 17.3525 | 10.0034 | -117.6780 | 3.5543 | 57.4039 | 0.0033 | 0.0170 |
| 2024_09_20 22:00 | 3256060 | 12 | 10.1168 | 13.9010 | -114.9915 | 3.5366 | 55.4091 | 0.0075 | 0.0075 |
| 2024_09_20 22:00 | 3268191 | 13 | 12.6527 | 11.9353 | -115.3099 | 3.0740 | 21.2807 | 0.0192 | 0.0186 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412495_6B151105 | 152650 | 868 | -96.1 | 152650 | 22 | -99.7 | 152650 | 175 | -105.8 | 152650 | 989 |
| MR_1774412495_5CC5B293 | 504990 | 971 | -96.6 | 504990 | 501 | -96.1 | 504990 | 173 | -100.3 | 504990 | 311 |
| MR_1774412495_8E65FA1F | 152650 | 868 | -97.0 | 152650 | 22 | -97.1 | 152650 | 175 | -102.9 | 152650 | 989 |
| MR_1774412495_EE072BB1 | 504990 | 971 | -92.7 | 504990 | 501 | -96.2 | 504990 | 173 | -100.3 | 504990 | 311 |
| MR_1774412495_EACD93A1 | 152650 | 868 | -94.3 | 152650 | 22 | -99.4 | 152650 | 175 | -102.5 | 152650 | 989 |
| MR_1774412495_29F0606C | 152650 | 868 | -93.6 | 152650 | 22 | -96.7 | 152650 | 175 | -103.3 | 152650 | 989 |
| MR_1774412495_8538ACAD | 504990 | 971 | -94.5 | 504990 | 501 | -95.7 | 504990 | 173 | -100.5 | 504990 | 311 |
| MR_1774412495_00DDC677 | 504990 | 971 | -95.5 | 504990 | 501 | -93.5 | 504990 | 173 | -101.4 | 504990 | 311 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1052: `553bbd7f-9af...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `553bbd7f-9afb-4b16-81a8-f07024ec9783` |
| Tag | **single-answer** |
| 정답 | **C9** |
| C9 의미 | Add neighbor relationship between 3258695_4 and 3229644_1 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1052] topology](images/train_1052.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3229644_1 by 4 degrees
- `C2`: Decrease A3 Offset threshold for 3258695_4
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3258695_4
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3229644_1
- `C5`: Insufficient data; more data is needed for judgment.
- `C6`: Decrease transmission power for 3258695_4
- `C7`: Adjust the azimuth of 3229644_1 by 19 degrees
- `C8`: Increase transmission power for 3229644_1
- `C9`: Add neighbor relationship between 3258695_4 and 3229644_1 **← 정답**
- `C10`: Increase transmission power for 3258695_4
- `C11`: Decrease A3 Offset threshold for 3229644_1
- `C12`: Check test server and transmission issues
- `C13`: Increase A3 Offset threshold for 3258695_4
- `C14`: Add neighbor relationship between 3230403_3 and 3229644_1
- `C15`: Increase A3 Offset threshold for 3229644_1
- `C16`: Decrease transmission power for 3229644_1
- `C17`: Adjust the azimuth of 3258695_4 by 50 degrees
- `C18`: Press down the tilt angle of 3258695_4 by 7 degrees
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3258695_4
- `C20`: Lift the tilt angle  of 3229644_1 by 4 degrees
- `C21`: Lift the tilt angle of 3258695_4 by 7 degrees
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3229644_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.701 | MS1 | 121.4656759665 | 31.1446316286 | 925 | 504990 | -81.63 | 16.59 | 491.42 | 0.08 | 2.98 | 1568 |
| 2024-09-20 22:21:32.148 | MS1 | 121.4656661209 | 31.1446371621 | 925 | 504990 | -83.67 | 17.75 | 607.16 | 0.01 | 2.48 | 1597 |
| 2024-09-20 22:21:33.937 | MS1 | 121.4656737330 | 31.1446298327 | 925 | 504990 | -77.84 | 14.45 | 421.72 | 0.12 | 2.08 | 1568 |
| 2024-09-20 22:21:34.559 | MS1 | 121.4656672251 | 31.1446320495 | 925 | 504990 | -93.79 | -3.87 | 57.24 | 0.17 | 1.04 | 1563 |
| 2024-09-20 22:21:35.646 | MS1 | 121.4656664658 | 31.1446196425 | 925 | 504990 | -86.36 | -1.84 | 68.21 | 0.13 | 1.31 | 1599 |
| 2024-09-20 22:21:36.344 | MS1 | 121.4656681746 | 31.1446206134 | 925 | 504990 | -88.28 | -2.22 | 48.24 | 0.16 | 1.47 | 1574 |
| 2024-09-20 22:21:37.451 | MS1 | 121.4656698353 | 31.1446324448 | 925 | 504990 | -86.85 | -0.76 | 67.58 | 0.19 | 1.39 | 1565 |
| 2024-09-20 22:21:38.123 | MS1 | 121.4656605722 | 31.1446267871 | 925 | 504990 | -83.78 | 16.75 | 321.16 | 0.17 | 1.36 | 1580 |
| 2024-09-20 22:21:39.494 | MS1 | 121.4656737649 | 31.1446352673 | 925 | 504990 | -75.78 | 17.95 | 507.62 | 0.19 | 1.34 | 1595 |
| 2024-09-20 22:21:40.397 | MS1 | 121.4656603499 | 31.1446234751 | 925 | 504990 | -79.33 | 12.87 | 472.92 | 0.09 | 2.02 | 1576 |
| 2024-09-20 22:21:41.839 | MS1 | 121.4656741563 | 31.1446292443 | 925 | 504990 | -78.10 | 13.35 | 355.93 | 0.07 | 2.43 | 1598 |
| 2024-09-20 22:21:42.369 | MS1 | 121.4656642240 | 31.1446185940 | 925 | 504990 | -77.17 | 15.10 | 491.97 | 0.09 | 2.11 | 1566 |

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
| 3212224 | 2 | 121.4706423117 | 31.1557758255 | 107 | 7 | 0 | 33.3 | TDD | 980 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3229644 | 1 | 121.4686778030 | 31.1471873666 | 244 | 1 | 9 | 21.3 | TDD | 234 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3230403 | 3 | 121.4679991836 | 31.1532537332 | 135 | 0 | 0 | 21.9 | TDD | 973 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3258695 | 4 | 121.4753110425 | 31.1551747016 | 134 | 5 | 4 | 41.4 | TDD | 925 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |

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
| 2024-09-20 22:21:30.801 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.818 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:30.921 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.921 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.633 | NREventA3 | measId:2;ServCellPCI:585;Se... |
| 2024-09-20 22:21:35.633 | NREventA3 | measId:2;ServCellPCI:585;Se... |
| 2024-09-20 22:21:36.633 | NREventA3 | measId:2;ServCellPCI:585;Se... |
| 2024-09-20 22:21:39.133 | NRRRCReestablishAttempt | PCI:585 |
| 2024-09-20 22:21:39.143 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.156 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:39.280 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.280 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3229644 | 1 | 13.6216 | 15.3540 | -116.1620 | 5.3920 | 86.4241 | 0.0150 | 0.0017 |
| 2024_09_20 22:00 | 3212224 | 2 | 13.2307 | 12.2500 | -116.5186 | 6.4874 | 133.7731 | 0.0039 | 0.0063 |
| 2024_09_20 22:00 | 3230403 | 3 | 6.6881 | 10.8824 | -115.4538 | 16.8985 | 106.2289 | 0.0026 | 0.0077 |
| 2024_09_20 22:00 | 3258695 | 4 | 13.2107 | 16.0569 | -116.2073 | 11.5370 | 145.9369 | 0.0199 | 0.1265 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413826_C244C61F | 504990 | 925 | -95.2 | 504990 | 234 | -86.7 | 504990 | 973 | -87.9 | 504990 | 980 |
| MR_1774413826_5896273F | 504990 | 925 | -92.8 | 504990 | 234 | -88.2 | 504990 | 973 | -89.1 | 504990 | 980 |
| MR_1774413826_1D83A571 | 504990 | 925 | -92.8 | 504990 | 234 | -88.2 | 504990 | 973 | -89.9 | 504990 | 980 |
| MR_1774413826_355A4135 | 504990 | 925 | -92.0 | 504990 | 234 | -89.2 | 504990 | 973 | -88.6 | 504990 | 980 |
| MR_1774413826_8B7F8583 | 504990 | 925 | -95.6 | 504990 | 234 | -86.7 | 504990 | 973 | -90.4 | 504990 | 980 |
| MR_1774413826_AC7B2007 | 504990 | 234 | -86.0 | 504990 | 925 | -95.2 | 504990 | 973 | -87.6 | 504990 | 980 |
| MR_1774413826_84A94D61 | 504990 | 234 | -87.6 | 504990 | 925 | -93.6 | 504990 | 973 | -90.4 | 504990 | 980 |
| MR_1774413826_9820F690 | 504990 | 925 | -93.8 | 504990 | 234 | -87.2 | 504990 | 973 | -88.7 | 504990 | 980 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1053: `586b0b83-b62...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `586b0b83-b620-4c2c-9ff8-aa9213bcbdc7` |
| Tag | **single-answer** |
| 정답 | **C22** |
| C22 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1053] topology](images/train_1053.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3226079_3 by 50 degrees
- `C2`: Press down the tilt angle  of 3261341_2 by 4 degrees
- `C3`: Decrease A3 Offset threshold for 3226079_3
- `C4`: Press down the tilt angle of 3226079_3 by 10 degrees
- `C5`: Increase A3 Offset threshold for 3226079_3
- `C6`: Decrease transmission power for 3261341_2
- `C7`: Lift the tilt angle  of 3261341_2 by 4 degrees
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3261341_2
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3226079_3
- `C10`: Add neighbor relationship between 3278633_1 and 3261341_2
- `C11`: Decrease transmission power for 3226079_3
- `C12`: Increase transmission power for 3226079_3
- `C13`: Lift the tilt angle of 3226079_3 by 10 degrees
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3226079_3
- `C15`: Increase transmission power for 3261341_2
- `C16`: Increase A3 Offset threshold for 3261341_2
- `C17`: Adjust the azimuth of 3261341_2 by 12 degrees
- `C18`: Add neighbor relationship between 3226079_3 and 3261341_2
- `C19`: Decrease A3 Offset threshold for 3261341_2
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3261341_2
- `C21`: Check test server and transmission issues
- `C22`: Insufficient data; more data is needed for judgment. **← 정답**

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.994 | MS1 | 121.4656608296 | 31.1446198432 | 284 | 504990 | -91.85 | 17.53 | 452.51 | 0.16 | 2.69 | 1592 |
| 2024-09-20 22:21:32.517 | MS1 | 121.4656651055 | 31.1446182006 | 284 | 504990 | -87.62 | 16.07 | 593.02 | 0.17 | 2.22 | 1598 |
| 2024-09-20 22:21:33.284 | MS1 | 121.4656722578 | 31.1446213171 | 284 | 504990 | -85.17 | 16.22 | 359.48 | 0.17 | 2.68 | 1581 |
| 2024-09-20 22:21:34.690 | MS1 | 121.4656687221 | 31.1446310825 | 284 | 504990 | -85.12 | 16.21 | 60.71 | 0.19 | 2.55 | 1575 |
| 2024-09-20 22:21:35.444 | MS1 | 121.4656735483 | 31.1446255748 | 284 | 504990 | -86.15 | 17.59 | 82.94 | 0.19 | 2.50 | 1593 |
| 2024-09-20 22:21:36.768 | MS1 | 121.4656626351 | 31.1446235662 | 284 | 504990 | -86.95 | 15.45 | 56.63 | 0.19 | 2.59 | 1587 |
| 2024-09-20 22:21:37.476 | MS1 | 121.4656740902 | 31.1446202871 | 284 | 504990 | -89.32 | 12.09 | 54.61 | 0.01 | 2.89 | 1582 |
| 2024-09-20 22:21:38.899 | MS1 | 121.4656613258 | 31.1446320798 | 284 | 504990 | -93.13 | 11.96 | 65.91 | 0.18 | 2.38 | 1588 |
| 2024-09-20 22:21:39.108 | MS1 | 121.4656676639 | 31.1446318785 | 284 | 504990 | -90.57 | 9.70 | 49.23 | 0.12 | 2.65 | 1584 |
| 2024-09-20 22:21:40.163 | MS1 | 121.4656652973 | 31.1446203954 | 284 | 504990 | -93.36 | 12.17 | 377.45 | 0.15 | 2.25 | 1566 |
| 2024-09-20 22:21:41.821 | MS1 | 121.4656692964 | 31.1446332688 | 284 | 504990 | -93.54 | 12.63 | 516.98 | 0.01 | 2.93 | 1560 |
| 2024-09-20 22:21:42.534 | MS1 | 121.4656723474 | 31.1446316600 | 284 | 504990 | -92.87 | 9.44 | 416.28 | 0.02 | 2.23 | 1563 |

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
| 3226079 | 3 | 121.4661588613 | 31.1451330582 | 353 | 7 | 9 | 41.3 | TDD | 284 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3242256 | 4 | 121.4659084551 | 31.1559876472 | 322 | 9 | 11 | 18.1 | TDD | 979 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3261341 | 2 | 121.4758898326 | 31.1550922428 | 232 | 3 | 8 | 18.9 | TDD | 923 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3278633 | 1 | 121.4689835121 | 31.1455846194 | 143 | 4 | 7 | 42.1 | TDD | 138 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |

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
| 2024-09-20 22:21:31.434 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.453 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.559 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.559 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.308 | NREventA3 | measId:2;ServCellPCI:159;Se... |
| 2024-09-20 22:21:38.548 | NRHandoverAttempt | SourcePCI:159;SourceNR-ARFC... |
| 2024-09-20 22:21:38.579 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.594 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.706 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.706 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3278633 | 1 | 83.6034 | 87.5679 | -114.0608 | 16.9317 | 96.5712 | 0.0094 | 0.0139 |
| 2024_09_19 22:00 | 3261341 | 2 | 75.6288 | 81.0034 | -114.6770 | 15.0389 | 173.7993 | 0.0077 | 0.0017 |
| 2024_09_19 22:00 | 3226079 | 3 | 86.5666 | 92.5073 | -114.3523 | 14.7700 | 128.2402 | 0.0012 | 0.0127 |
| 2024_09_19 22:00 | 3242256 | 4 | 80.6926 | 92.1036 | -117.8697 | 10.1924 | 139.9587 | 0.0107 | 0.0130 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412026_07A05F3A | 504990 | 284 | -85.3 | 504990 | 923 | -87.3 | 504990 | 138 | -96.2 | 504990 | 979 |
| MR_1774412026_A07C6D17 | 504990 | 284 | -83.9 | 504990 | 923 | -87.3 | 504990 | 138 | -94.0 | 504990 | 979 |
| MR_1774412026_B28F5D7D | 504990 | 284 | -87.0 | 504990 | 923 | -87.6 | 504990 | 138 | -95.2 | 504990 | 979 |
| MR_1774412026_061A326A | 504990 | 284 | -86.3 | 504990 | 923 | -88.6 | 504990 | 138 | -94.3 | 504990 | 979 |
| MR_1774412026_1554F457 | 504990 | 284 | -85.1 | 504990 | 923 | -88.0 | 504990 | 138 | -94.3 | 504990 | 979 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1054: `5d480ab4-d3a...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `5d480ab4-d3a1-457a-8ef0-cc98751111ad` |
| Tag | **single-answer** |
| 정답 | **C13** |
| C13 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3272492_1 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1054] topology](images/train_1054.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3241910_4
- `C2`: Add neighbor relationship between 3273611_3 and 3241910_4
- `C3`: Increase transmission power for 3272492_1
- `C4`: Adjust the azimuth of 3241910_4 by 50 degrees
- `C5`: Insufficient data; more data is needed for judgment.
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3272492_1
- `C7`: Decrease transmission power for 3241910_4
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3241910_4
- `C9`: Decrease A3 Offset threshold for 3272492_1
- `C10`: Increase A3 Offset threshold for 3241910_4
- `C11`: Decrease transmission power for 3272492_1
- `C12`: Press down the tilt angle of 3272492_1 by 3 degrees
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3272492_1 **← 정답**
- `C14`: Adjust the azimuth of 3272492_1 by 17 degrees
- `C15`: Add neighbor relationship between 3272492_1 and 3241910_4
- `C16`: Lift the tilt angle  of 3241910_4 by 7 degrees
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3241910_4
- `C18`: Decrease A3 Offset threshold for 3241910_4
- `C19`: Check test server and transmission issues
- `C20`: Press down the tilt angle  of 3241910_4 by 7 degrees
- `C21`: Lift the tilt angle of 3272492_1 by 3 degrees
- `C22`: Increase A3 Offset threshold for 3272492_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.339 | MS1 | 121.4656657360 | 31.1446354069 | 8 | 504990 | -90.36 | 15.16 | 339.61 | 0.01 | 2.52 | 1573 |
| 2024-09-20 22:21:32.337 | MS1 | 121.4656661737 | 31.1446195062 | 8 | 504990 | -85.56 | 13.73 | 403.09 | 0.07 | 2.76 | 1599 |
| 2024-09-20 22:21:33.393 | MS1 | 121.4656720127 | 31.1446209033 | 8 | 504990 | -89.98 | 13.36 | 409.79 | 0.08 | 2.41 | 1582 |
| 2024-09-20 22:21:34.353 | MS1 | 121.4656738502 | 31.1446290441 | 8 | 504990 | -91.58 | 13.65 | 54.74 | 0.63 | 2.12 | 663 |
| 2024-09-20 22:21:35.104 | MS1 | 121.4656615793 | 31.1446256595 | 8 | 504990 | -85.44 | 13.55 | 100.29 | 0.62 | 2.32 | 547 |
| 2024-09-20 22:21:36.769 | MS1 | 121.4656739838 | 31.1446276148 | 8 | 504990 | -86.75 | 17.42 | 100.75 | 0.55 | 2.32 | 512 |
| 2024-09-20 22:21:37.818 | MS1 | 121.4656593600 | 31.1446212512 | 8 | 504990 | -93.35 | 8.64 | 60.86 | 0.68 | 2.55 | 512 |
| 2024-09-20 22:21:38.479 | MS1 | 121.4656708945 | 31.1446221280 | 8 | 504990 | -92.85 | 7.03 | 62.33 | 0.52 | 2.60 | 573 |
| 2024-09-20 22:21:39.648 | MS1 | 121.4656625939 | 31.1446209136 | 8 | 504990 | -93.71 | 10.40 | 63.92 | 0.52 | 2.44 | 573 |
| 2024-09-20 22:21:40.928 | MS1 | 121.4656593182 | 31.1446320967 | 8 | 504990 | -92.23 | 9.82 | 462.39 | 0.05 | 2.06 | 1588 |
| 2024-09-20 22:21:41.250 | MS1 | 121.4656583850 | 31.1446330207 | 8 | 504990 | -92.87 | 7.50 | 356.86 | 0.15 | 2.54 | 1590 |
| 2024-09-20 22:21:42.794 | MS1 | 121.4656633544 | 31.1446198712 | 8 | 504990 | -93.77 | 10.03 | 575.52 | 0.14 | 2.27 | 1590 |

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
| 3241910 | 4 | 121.4663740365 | 31.1542582994 | 334 | 5 | 3 | 46.5 | TDD | 163 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3243665 | 2 | 121.4702934172 | 31.1509758188 | 206 | 13 | 1 | 29.1 | TDD | 365 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3272492 | 1 | 121.4724163047 | 31.1492796429 | 214 | 1 | 9 | 35.6 | TDD | 8 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3273611 | 3 | 121.4746198422 | 31.1504823784 | 120 | 2 | 9 | 45.9 | TDD | 371 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |

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
| 2024-09-20 22:21:30.813 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.834 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:30.941 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.941 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.633 | NREventA3 | measId:2;ServCellPCI:474;Se... |
| 2024-09-20 22:21:37.873 | NRHandoverAttempt | SourcePCI:474;SourceNR-ARFC... |
| 2024-09-20 22:21:37.911 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.921 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.066 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.066 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3272492 | 1 | 5.3069 | 7.0018 | -115.2477 | 10.1238 | 109.5284 | 0.0198 | 0.0188 |
| 2024_09_20 22:00 | 3243665 | 2 | 9.4418 | 7.3104 | -116.4438 | 16.5489 | 172.1676 | 0.0014 | 0.0196 |
| 2024_09_20 22:00 | 3273611 | 3 | 16.3039 | 15.7331 | -115.9259 | 15.6948 | 125.0274 | 0.0011 | 0.0137 |
| 2024_09_20 22:00 | 3241910 | 4 | 6.0800 | 9.5470 | -117.8334 | 15.3007 | 84.3878 | 0.0186 | 0.0090 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416794_DDB46312 | 504990 | 8 | -90.8 | 504990 | 163 | -94.8 | 504990 | 371 | -104.5 | 504990 | 365 |
| MR_1774416794_7D703D1C | 504990 | 8 | -90.7 | 504990 | 163 | -94.4 | 504990 | 371 | -105.6 | 504990 | 365 |
| MR_1774416794_56E216E8 | 504990 | 8 | -91.7 | 504990 | 163 | -91.5 | 504990 | 371 | -104.3 | 504990 | 365 |
| MR_1774416794_74185C16 | 504990 | 8 | -89.7 | 504990 | 163 | -94.9 | 504990 | 371 | -105.0 | 504990 | 365 |
| MR_1774416794_7F14D1E5 | 504990 | 8 | -91.4 | 504990 | 163 | -93.7 | 504990 | 371 | -106.3 | 504990 | 365 |
| MR_1774416794_66D974FC | 504990 | 8 | -92.4 | 504990 | 163 | -92.8 | 504990 | 371 | -103.9 | 504990 | 365 |
| MR_1774416794_C5149034 | 504990 | 8 | -90.9 | 504990 | 163 | -92.3 | 504990 | 371 | -102.5 | 504990 | 365 |
| MR_1774416794_F8707349 | 504990 | 8 | -92.0 | 504990 | 163 | -93.6 | 504990 | 371 | -106.3 | 504990 | 365 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1055: `3e75b0c8-162...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `3e75b0c8-1623-453f-b231-0a356cd61c36` |
| Tag | **single-answer** |
| 정답 | **C5** |
| C5 의미 | Add neighbor relationship between 3253896_1 and 3231542_2 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1055] topology](images/train_1055.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3231542_2 by 2 degrees
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3253896_1
- `C3`: Lift the tilt angle  of 3231542_2 by 2 degrees
- `C4`: Adjust the azimuth of 3253896_1 by 50 degrees
- `C5`: Add neighbor relationship between 3253896_1 and 3231542_2 **← 정답**
- `C6`: Increase transmission power for 3253896_1
- `C7`: Add neighbor relationship between 3229495_3 and 3231542_2
- `C8`: Adjust the azimuth of 3231542_2 by 5 degrees
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3253896_1
- `C10`: Increase transmission power for 3231542_2
- `C11`: Check test server and transmission issues
- `C12`: Lift the tilt angle of 3253896_1 by 9 degrees
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3231542_2
- `C14`: Decrease A3 Offset threshold for 3231542_2
- `C15`: Decrease transmission power for 3231542_2
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3231542_2
- `C17`: Decrease transmission power for 3253896_1
- `C18`: Decrease A3 Offset threshold for 3253896_1
- `C19`: Press down the tilt angle of 3253896_1 by 9 degrees
- `C20`: Increase A3 Offset threshold for 3231542_2
- `C21`: Insufficient data; more data is needed for judgment.
- `C22`: Increase A3 Offset threshold for 3253896_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.178 | MS1 | 121.4656709248 | 31.1446332400 | 352 | 504990 | -77.30 | 12.14 | 375.93 | 0.06 | 2.92 | 1579 |
| 2024-09-20 22:21:32.728 | MS1 | 121.4656588599 | 31.1446243432 | 352 | 504990 | -76.06 | 16.71 | 445.84 | 0.05 | 2.53 | 1577 |
| 2024-09-20 22:21:33.122 | MS1 | 121.4656737519 | 31.1446180930 | 352 | 504990 | -83.94 | 14.07 | 325.51 | 0.13 | 2.62 | 1572 |
| 2024-09-20 22:21:34.619 | MS1 | 121.4656707058 | 31.1446223321 | 352 | 504990 | -93.43 | -0.74 | 59.59 | 0.12 | 1.29 | 1563 |
| 2024-09-20 22:21:35.431 | MS1 | 121.4656592649 | 31.1446200119 | 352 | 504990 | -89.21 | -2.67 | 65.03 | 0.17 | 1.49 | 1577 |
| 2024-09-20 22:21:36.202 | MS1 | 121.4656644052 | 31.1446323919 | 352 | 504990 | -86.59 | -2.61 | 57.42 | 0.17 | 1.09 | 1589 |
| 2024-09-20 22:21:37.826 | MS1 | 121.4656698680 | 31.1446202432 | 352 | 504990 | -94.70 | -0.39 | 33.40 | 0.08 | 1.26 | 1580 |
| 2024-09-20 22:21:38.578 | MS1 | 121.4656618071 | 31.1446309041 | 352 | 504990 | -82.37 | 12.71 | 439.55 | 0.16 | 1.12 | 1568 |
| 2024-09-20 22:21:39.378 | MS1 | 121.4656757029 | 31.1446273433 | 352 | 504990 | -80.06 | 15.09 | 540.74 | 0.01 | 1.45 | 1599 |
| 2024-09-20 22:21:40.279 | MS1 | 121.4656718755 | 31.1446182928 | 352 | 504990 | -77.12 | 17.13 | 413.49 | 0.15 | 2.04 | 1585 |
| 2024-09-20 22:21:41.982 | MS1 | 121.4656647656 | 31.1446226216 | 352 | 504990 | -77.19 | 17.08 | 332.73 | 0.13 | 2.44 | 1586 |
| 2024-09-20 22:21:42.431 | MS1 | 121.4656696114 | 31.1446263388 | 352 | 504990 | -81.02 | 13.11 | 310.10 | 0.07 | 2.13 | 1563 |

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
| 3229495 | 3 | 121.4663175699 | 31.1530328645 | 12 | 1 | 7 | 20.4 | TDD | 86 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3231542 | 2 | 121.4741699994 | 31.1450904265 | 261 | 1 | 1 | 21.1 | TDD | 681 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3253896 | 1 | 121.4759712818 | 31.1512347529 | 302 | 7 | 0 | 49.2 | TDD | 352 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3270475 | 4 | 121.4705289514 | 31.1531717842 | 188 | 3 | 12 | 29.7 | TDD | 680 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |

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
| 2024-09-20 22:21:31.259 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.281 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.429 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.429 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.149 | NREventA3 | measId:2;ServCellPCI:142;Se... |
| 2024-09-20 22:21:36.149 | NREventA3 | measId:2;ServCellPCI:142;Se... |
| 2024-09-20 22:21:37.149 | NREventA3 | measId:2;ServCellPCI:142;Se... |
| 2024-09-20 22:21:39.649 | NRRRCReestablishAttempt | PCI:142 |
| 2024-09-20 22:21:39.662 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.673 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:39.793 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.793 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3253896 | 1 | 16.3883 | 8.8408 | -114.3971 | 5.7940 | 168.2291 | 0.0177 | 0.1660 |
| 2024_09_20 22:00 | 3231542 | 2 | 13.1497 | 11.4884 | -117.4249 | 6.9541 | 141.4215 | 0.0114 | 0.0091 |
| 2024_09_20 22:00 | 3229495 | 3 | 19.3636 | 10.8664 | -115.6147 | 9.7795 | 90.1262 | 0.0144 | 0.0131 |
| 2024_09_20 22:00 | 3270475 | 4 | 11.2821 | 6.4134 | -115.3485 | 9.9715 | 158.6108 | 0.0097 | 0.0133 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413993_C8C33AD9 | 504990 | 681 | -87.1 | 504990 | 352 | -95.2 | 504990 | 86 | -94.2 | 504990 | 680 |
| MR_1774413993_ABA4203D | 504990 | 352 | -94.2 | 504990 | 681 | -87.1 | 504990 | 86 | -93.5 | 504990 | 680 |
| MR_1774413993_4F4F8E90 | 504990 | 352 | -91.5 | 504990 | 681 | -89.8 | 504990 | 86 | -93.8 | 504990 | 680 |
| MR_1774413993_19A0D8A6 | 504990 | 352 | -94.7 | 504990 | 681 | -88.4 | 504990 | 86 | -95.7 | 504990 | 680 |
| MR_1774413993_F4378A45 | 504990 | 681 | -86.2 | 504990 | 352 | -94.1 | 504990 | 86 | -96.2 | 504990 | 680 |
| MR_1774413993_824C1C2A | 504990 | 681 | -86.2 | 504990 | 352 | -92.4 | 504990 | 86 | -96.2 | 504990 | 680 |
| MR_1774413993_2C2161DC | 504990 | 681 | -86.0 | 504990 | 352 | -91.5 | 504990 | 86 | -94.4 | 504990 | 680 |
| MR_1774413993_B0760E8F | 504990 | 352 | -91.9 | 504990 | 681 | -88.6 | 504990 | 86 | -93.5 | 504990 | 680 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1056: `04cfe46f-c2f...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `04cfe46f-c2fb-4559-ad0a-c6e10057c633` |
| Tag | **single-answer** |
| 정답 | **C18** |
| C18 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1056] topology](images/train_1056.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3227032_1
- `C2`: Adjust the azimuth of 3274733_4 by 50 degrees
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3274733_4
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3227032_1
- `C5`: Decrease A3 Offset threshold for 3227032_1
- `C6`: Adjust the azimuth of 3227032_1 by 6 degrees
- `C7`: Increase transmission power for 3274733_4
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3227032_1
- `C9`: Press down the tilt angle of 3227032_1 by 2 degrees
- `C10`: Insufficient data; more data is needed for judgment.
- `C11`: Decrease transmission power for 3274733_4
- `C12`: Increase A3 Offset threshold for 3227032_1
- `C13`: Press down the tilt angle  of 3274733_4 by 10 degrees
- `C14`: Increase A3 Offset threshold for 3274733_4
- `C15`: Add neighbor relationship between 3229938_3 and 3274733_4
- `C16`: Decrease transmission power for 3227032_1
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3274733_4
- `C18`: Check test server and transmission issues **← 정답**
- `C19`: Decrease A3 Offset threshold for 3274733_4
- `C20`: Lift the tilt angle  of 3274733_4 by 10 degrees
- `C21`: Lift the tilt angle of 3227032_1 by 2 degrees
- `C22`: Add neighbor relationship between 3227032_1 and 3274733_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.941 | MS1 | 121.4656722384 | 31.1446282259 | 616 | 504990 | -86.45 | 17.87 | 333.19 | 0.19 | 2.03 | 1566 |
| 2024-09-20 22:21:32.434 | MS1 | 121.4656590678 | 31.1446187504 | 616 | 504990 | -91.24 | 14.50 | 532.30 | 0.03 | 3.00 | 1594 |
| 2024-09-20 22:21:33.703 | MS1 | 121.4656747684 | 31.1446343575 | 616 | 504990 | -86.21 | 15.57 | 385.29 | 0.13 | 2.32 | 1590 |
| 2024-09-20 22:21:34.234 | MS1 | 121.4656771160 | 31.1446323232 | 616 | 504990 | -86.02 | 16.94 | 54.92 | 0.03 | 2.20 | 392 |
| 2024-09-20 22:21:35.281 | MS1 | 121.4656586883 | 31.1446303108 | 616 | 504990 | -91.63 | 17.76 | 52.75 | 0.09 | 2.49 | 480 |
| 2024-09-20 22:21:36.977 | MS1 | 121.4656600495 | 31.1446195099 | 616 | 504990 | -88.65 | 12.00 | 98.14 | 0.08 | 2.19 | 413 |
| 2024-09-20 22:21:37.219 | MS1 | 121.4656652645 | 31.1446370567 | 616 | 504990 | -89.16 | 8.19 | 63.26 | 0.10 | 2.98 | 469 |
| 2024-09-20 22:21:38.418 | MS1 | 121.4656763561 | 31.1446230639 | 616 | 504990 | -91.62 | 10.24 | 101.82 | 0.05 | 2.36 | 426 |
| 2024-09-20 22:21:39.633 | MS1 | 121.4656673452 | 31.1446290144 | 616 | 504990 | -91.52 | 8.96 | 59.17 | 0.03 | 2.55 | 323 |
| 2024-09-20 22:21:40.595 | MS1 | 121.4656707942 | 31.1446272333 | 616 | 504990 | -93.26 | 9.13 | 390.05 | 0.03 | 2.65 | 1568 |
| 2024-09-20 22:21:41.803 | MS1 | 121.4656703451 | 31.1446338398 | 616 | 504990 | -89.76 | 10.44 | 571.40 | 0.04 | 2.38 | 1593 |
| 2024-09-20 22:21:42.803 | MS1 | 121.4656648832 | 31.1446245360 | 616 | 504990 | -91.76 | 12.92 | 505.79 | 0.02 | 2.62 | 1563 |

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
| 3227032 | 1 | 121.4734277122 | 31.1498688541 | 238 | 0 | 7 | 35.3 | TDD | 616 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3229938 | 3 | 121.4738067826 | 31.1553883356 | 268 | 5 | 8 | 29.1 | TDD | 357 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3264533 | 2 | 121.4731370403 | 31.1497099464 | 274 | 7 | 11 | 49.5 | TDD | 482 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3274733 | 4 | 121.4758875325 | 31.1467096401 | 320 | 9 | 3 | 45.0 | TDD | 959 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:31.525 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.547 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.657 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.657 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.391 | NREventA3 | measId:2;ServCellPCI:991;Se... |
| 2024-09-20 22:21:38.631 | NRHandoverAttempt | SourcePCI:991;SourceNR-ARFC... |
| 2024-09-20 22:21:38.679 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.691 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.838 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.838 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3227032 | 1 | 11.7467 | 14.8054 | -114.6961 | 5.5884 | 161.2991 | 0.0000 | 0.0172 |
| 2024_09_20 22:00 | 3264533 | 2 | 13.2018 | 18.3554 | -115.1549 | 17.4475 | 90.6711 | 0.0007 | 0.0086 |
| 2024_09_20 22:00 | 3229938 | 3 | 6.7563 | 12.1481 | -115.4558 | 17.9990 | 83.5133 | 0.0195 | 0.0195 |
| 2024_09_20 22:00 | 3274733 | 4 | 18.3228 | 10.4131 | -115.9440 | 16.8741 | 173.4140 | 0.0008 | 0.0120 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416677_1FC93964 | 504990 | 616 | -85.7 | 504990 | 959 | -86.9 | 504990 | 357 | -97.9 | 504990 | 482 |
| MR_1774416677_C511EB3C | 504990 | 616 | -87.8 | 504990 | 959 | -85.2 | 504990 | 357 | -100.2 | 504990 | 482 |
| MR_1774416677_5E6AA12F | 504990 | 616 | -86.3 | 504990 | 959 | -86.2 | 504990 | 357 | -99.4 | 504990 | 482 |
| MR_1774416677_100FEAE2 | 504990 | 616 | -84.2 | 504990 | 959 | -84.6 | 504990 | 357 | -101.1 | 504990 | 482 |
| MR_1774416677_26DF148E | 504990 | 616 | -85.2 | 504990 | 959 | -87.3 | 504990 | 357 | -99.0 | 504990 | 482 |
| MR_1774416677_1219FFD7 | 504990 | 616 | -87.6 | 504990 | 959 | -87.0 | 504990 | 357 | -97.6 | 504990 | 482 |
| MR_1774416677_312AB910 | 504990 | 616 | -84.4 | 504990 | 959 | -85.4 | 504990 | 357 | -99.8 | 504990 | 482 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1057: `c9112de4-2be...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `c9112de4-2be7-4662-acc4-cd81783d3407` |
| Tag | **single-answer** |
| 정답 | **C10** |
| C10 의미 | Decrease A3 Offset threshold for 3242315_4 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1057] topology](images/train_1057.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3273773_3
- `C2`: Adjust the azimuth of 3273773_3 by 50 degrees
- `C3`: Check test server and transmission issues
- `C4`: Lift the tilt angle of 3242315_4 by 10 degrees
- `C5`: Decrease A3 Offset threshold for 3273773_3
- `C6`: Add neighbor relationship between 3253786_2 and 3273773_3
- `C7`: Lift the tilt angle  of 3273773_3 by 10 degrees
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3242315_4
- `C9`: Decrease transmission power for 3273773_3
- `C10`: Decrease A3 Offset threshold for 3242315_4 **← 정답**
- `C11`: Increase transmission power for 3273773_3
- `C12`: Increase transmission power for 3242315_4
- `C13`: Decrease transmission power for 3242315_4
- `C14`: Press down the tilt angle  of 3273773_3 by 10 degrees
- `C15`: Increase A3 Offset threshold for 3242315_4
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3242315_4
- `C17`: Increase A3 Offset threshold for 3273773_3
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3273773_3
- `C19`: Insufficient data; more data is needed for judgment.
- `C20`: Adjust the azimuth of 3242315_4 by 50 degrees
- `C21`: Add neighbor relationship between 3242315_4 and 3273773_3
- `C22`: Press down the tilt angle of 3242315_4 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.247 | MS1 | 121.4656742679 | 31.1446214396 | 70 | 504990 | -76.29 | 12.28 | 580.20 | 0.18 | 2.04 | 1583 |
| 2024-09-20 22:21:32.671 | MS1 | 121.4656670403 | 31.1446182208 | 70 | 504990 | -75.65 | 17.21 | 526.32 | 0.08 | 2.43 | 1599 |
| 2024-09-20 22:21:33.549 | MS1 | 121.4656696701 | 31.1446356971 | 70 | 504990 | -81.55 | 16.76 | 440.00 | 0.11 | 2.47 | 1592 |
| 2024-09-20 22:21:34.807 | MS1 | 121.4656714124 | 31.1446268371 | 70 | 504990 | -90.15 | -1.41 | 42.01 | 0.04 | 1.09 | 1584 |
| 2024-09-20 22:21:35.704 | MS1 | 121.4656686439 | 31.1446339715 | 70 | 504990 | -86.33 | -1.44 | 72.12 | 0.07 | 1.37 | 1593 |
| 2024-09-20 22:21:36.207 | MS1 | 121.4656730201 | 31.1446315207 | 70 | 504990 | -92.12 | -2.70 | 58.41 | 0.14 | 1.33 | 1567 |
| 2024-09-20 22:21:37.564 | MS1 | 121.4656677851 | 31.1446321786 | 70 | 504990 | -87.66 | -3.91 | 63.62 | 0.10 | 1.17 | 1592 |
| 2024-09-20 22:21:38.299 | MS1 | 121.4656725695 | 31.1446323480 | 70 | 504990 | -85.48 | -3.08 | 65.10 | 0.01 | 1.09 | 1592 |
| 2024-09-20 22:21:39.187 | MS1 | 121.4656635404 | 31.1446247351 | 733 | 504990 | -78.22 | 13.80 | 193.00 | 0.03 | 1.25 | 1571 |
| 2024-09-20 22:21:40.650 | MS1 | 121.4656631265 | 31.1446322950 | 733 | 504990 | -83.16 | 16.71 | 418.45 | 0.03 | 2.07 | 1590 |
| 2024-09-20 22:21:41.137 | MS1 | 121.4656761162 | 31.1446330056 | 733 | 504990 | -84.08 | 12.33 | 583.14 | 0.16 | 2.46 | 1572 |
| 2024-09-20 22:21:42.687 | MS1 | 121.4656655062 | 31.1446210833 | 733 | 504990 | -80.25 | 15.26 | 380.82 | 0.18 | 2.45 | 1567 |

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
| 3242315 | 4 | 121.4686444080 | 31.1518188800 | 43 | 9 | 4 | 32.7 | TDD | 70 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3253786 | 2 | 121.4646953852 | 31.1499454761 | 354 | 15 | 10 | 40.3 | TDD | 714 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3273773 | 3 | 121.4679418797 | 31.1453963414 | 323 | 4 | 2 | 41.0 | TDD | 733 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3273936 | 1 | 121.4648256532 | 31.1499439110 | 91 | 12 | 3 | 16.6 | TDD | 688 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |

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
| 2024-09-20 22:21:31.287 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.302 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.438 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.438 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.098 | NREventA3 | measId:2;ServCellPCI:895;Se... |
| 2024-09-20 22:21:38.338 | NRHandoverAttempt | SourcePCI:895;SourceNR-ARFC... |
| 2024-09-20 22:21:38.383 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.395 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.507 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.507 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3273936 | 1 | 12.2761 | 7.7782 | -114.0602 | 17.3879 | 139.8824 | 0.0011 | 0.0014 |
| 2024_09_20 22:00 | 3253786 | 2 | 5.1948 | 19.0538 | -117.6588 | 16.6310 | 184.3864 | 0.0024 | 0.0031 |
| 2024_09_20 22:00 | 3273773 | 3 | 19.6745 | 6.1132 | -115.2975 | 19.6436 | 142.0296 | 0.0122 | 0.0007 |
| 2024_09_20 22:00 | 3242315 | 4 | 15.5793 | 16.7584 | -117.6794 | 19.6016 | 93.8616 | 0.0182 | 0.1860 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417184_45B625A6 | 504990 | 733 | -84.8 | 504990 | 70 | -89.5 | 504990 | 714 | -92.9 | 504990 | 688 |
| MR_1774417184_06F8D371 | 504990 | 70 | -90.3 | 504990 | 733 | -83.6 | 504990 | 714 | -93.2 | 504990 | 688 |
| MR_1774417184_39324850 | 504990 | 70 | -91.9 | 504990 | 733 | -84.7 | 504990 | 714 | -94.1 | 504990 | 688 |
| MR_1774417184_63F867C1 | 504990 | 733 | -83.4 | 504990 | 70 | -90.9 | 504990 | 714 | -94.6 | 504990 | 688 |
| MR_1774417184_CD4C7B27 | 504990 | 70 | -89.6 | 504990 | 733 | -85.5 | 504990 | 714 | -96.1 | 504990 | 688 |
| MR_1774417184_B5CC7DB5 | 504990 | 70 | -89.8 | 504990 | 733 | -85.3 | 504990 | 714 | -94.3 | 504990 | 688 |
| MR_1774417184_8B381579 | 504990 | 70 | -91.6 | 504990 | 733 | -83.6 | 504990 | 714 | -93.1 | 504990 | 688 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1058: `ae5f74e0-216...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `ae5f74e0-2168-432c-879d-9e2860e6465e` |
| Tag | **multiple-answer** |
| 정답 | **C6|C21** |
| C6 의미 | Increase transmission power for 3240191_3 |
| C21 의미 | Adjust the azimuth of 3240191_3 by 48 degrees |
| 패턴 분류 | **P4 Coverage (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1058] topology](images/train_1058.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment.
- `C2`: Lift the tilt angle  of 3245667_2 by 4 degrees
- `C3`: Press down the tilt angle  of 3245667_2 by 4 degrees
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3245667_2
- `C5`: Decrease A3 Offset threshold for 3245667_2
- `C6`: Increase transmission power for 3240191_3 **← 정답**
- `C7`: Check test server and transmission issues
- `C8`: Increase A3 Offset threshold for 3245667_2
- `C9`: Press down the tilt angle of 3240191_3 by 8 degrees
- `C10`: Increase transmission power for 3245667_2
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3240191_3
- `C12`: Add neighbor relationship between 3240191_3 and 3245667_2
- `C13`: Increase A3 Offset threshold for 3240191_3
- `C14`: Decrease A3 Offset threshold for 3240191_3
- `C15`: Lift the tilt angle of 3240191_3 by 8 degrees
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3240191_3
- `C17`: Adjust the azimuth of 3245667_2 by 45 degrees
- `C18`: Decrease transmission power for 3245667_2
- `C19`: Decrease transmission power for 3240191_3
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3245667_2
- `C21`: Adjust the azimuth of 3240191_3 by 48 degrees **← 정답**
- `C22`: Add neighbor relationship between 3232618_1 and 3245667_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.974 | MS1 | 121.4656726399 | 31.1446236959 | 764 | 504990 | -88.96 | 12.25 | 518.73 | 0.08 | 2.91 | 1590 |
| 2024-09-20 22:21:32.949 | MS1 | 121.4656585602 | 31.1446183246 | 764 | 504990 | -87.82 | 16.33 | 545.18 | 0.13 | 2.96 | 1576 |
| 2024-09-20 22:21:33.874 | MS1 | 121.4656608465 | 31.1446227168 | 764 | 504990 | -88.27 | 12.58 | 491.57 | 0.16 | 2.14 | 1568 |
| 2024-09-20 22:21:34.440 | MS1 | 121.4656616950 | 31.1446240364 | 764 | 504990 | -105.44 | -0.27 | 76.10 | 0.04 | 1.45 | 1580 |
| 2024-09-20 22:21:35.928 | MS1 | 121.4656700956 | 31.1446323420 | 764 | 504990 | -100.13 | -0.49 | 87.57 | 0.01 | 1.40 | 1589 |
| 2024-09-20 22:21:36.589 | MS1 | 121.4656601703 | 31.1446359833 | 764 | 504990 | -109.32 | -0.81 | 80.98 | 0.11 | 1.14 | 1562 |
| 2024-09-20 22:21:37.398 | MS1 | 121.4656614060 | 31.1446236817 | 764 | 504990 | -106.94 | -0.70 | 67.89 | 0.11 | 1.16 | 1599 |
| 2024-09-20 22:21:38.611 | MS1 | 121.4656680363 | 31.1446193235 | 764 | 504990 | -103.05 | 1.47 | 33.75 | 0.08 | 1.24 | 1577 |
| 2024-09-20 22:21:39.246 | MS1 | 121.4656593679 | 31.1446193819 | 764 | 504990 | -107.46 | 1.36 | 71.84 | 0.14 | 1.07 | 1573 |
| 2024-09-20 22:21:40.656 | MS1 | 121.4656642431 | 31.1446332959 | 764 | 504990 | -90.22 | 15.24 | 338.64 | 0.15 | 2.53 | 1579 |
| 2024-09-20 22:21:41.802 | MS1 | 121.4656731380 | 31.1446365566 | 764 | 504990 | -90.90 | 12.39 | 444.40 | 0.00 | 2.41 | 1583 |
| 2024-09-20 22:21:42.586 | MS1 | 121.4656659188 | 31.1446186094 | 764 | 504990 | -88.68 | 17.39 | 349.94 | 0.17 | 2.29 | 1590 |

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
| 3232618 | 1 | 121.4666312083 | 31.1495712622 | 142 | 9 | 12 | 34.3 | TDD | 752 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3240191 | 3 | 121.4734221763 | 31.1451041000 | 314 | 6 | 11 | 30.9 | TDD | 764 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3240980 | 4 | 121.4733882041 | 31.1446579380 | 212 | 8 | 7 | 17.2 | TDD | 349 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3245667 | 2 | 121.4686598613 | 31.1512838345 | 156 | 2 | 7 | 33.3 | TDD | 25 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |

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
| 2024-09-20 22:21:31.407 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.425 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.558 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.558 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.741 | NREventA2 | measId:1;ServCellPCI:17;Ser... |
| 2024-09-20 22:21:34.891 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3232618 | 1 | 9.1291 | 5.0214 | -115.7842 | 19.1475 | 124.9621 | 0.0114 | 0.0164 |
| 2024_09_20 22:00 | 3245667 | 2 | 11.3440 | 5.3277 | -116.1772 | 5.1403 | 163.5174 | 0.0134 | 0.0099 |
| 2024_09_20 22:00 | 3240191 | 3 | 18.5276 | 5.6044 | -115.3040 | 12.9586 | 171.5393 | 0.1205 | 0.0144 |
| 2024_09_20 22:00 | 3240980 | 4 | 7.7464 | 8.9674 | -116.4886 | 6.2227 | 136.1829 | 0.0184 | 0.0135 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415766_CE181E5F | 504990 | 764 | -104.8 | 504990 | 25 | -110.8 | 504990 | 752 | -114.8 | 504990 | 349 |
| MR_1774415766_1EF21B87 | 504990 | 764 | -107.3 | 504990 | 25 | -108.4 | 504990 | 752 | -113.0 | 504990 | 349 |
| MR_1774415766_D588893D | 504990 | 764 | -104.9 | 504990 | 25 | -109.4 | 504990 | 752 | -113.6 | 504990 | 349 |
| MR_1774415766_4E07E0D7 | 504990 | 764 | -106.9 | 504990 | 25 | -109.1 | 504990 | 752 | -115.5 | 504990 | 349 |
| MR_1774415766_1850DD02 | 504990 | 764 | -104.2 | 504990 | 25 | -108.9 | 504990 | 752 | -116.1 | 504990 | 349 |
| MR_1774415766_41C19443 | 504990 | 764 | -105.2 | 504990 | 25 | -110.6 | 504990 | 752 | -113.9 | 504990 | 349 |
| MR_1774415766_DBDB8DB9 | 504990 | 764 | -104.1 | 504990 | 25 | -107.9 | 504990 | 752 | -114.7 | 504990 | 349 |
| MR_1774415766_C759CC97 | 504990 | 764 | -104.8 | 504990 | 25 | -109.1 | 504990 | 752 | -115.2 | 504990 | 349 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1059: `f0dd52b1-eb8...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `f0dd52b1-eb8e-4197-ba39-fa4ca1725414` |
| Tag | **single-answer** |
| 정답 | **C8** |
| C8 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1059] topology](images/train_1059.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3222805_2 and 3270620_4
- `C2`: Add neighbor relationship between 3253185_1 and 3270620_4
- `C3`: Increase transmission power for 3253185_1
- `C4`: Lift the tilt angle of 3253185_1 by 10 degrees
- `C5`: Decrease transmission power for 3270620_4
- `C6`: Check test server and transmission issues
- `C7`: Lift the tilt angle  of 3270620_4 by 8 degrees
- `C8`: Insufficient data; more data is needed for judgment. **← 정답**
- `C9`: Adjust the azimuth of 3270620_4 by 50 degrees
- `C10`: Adjust the azimuth of 3253185_1 by 50 degrees
- `C11`: Press down the tilt angle of 3253185_1 by 10 degrees
- `C12`: Increase A3 Offset threshold for 3270620_4
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3253185_1
- `C14`: Decrease transmission power for 3253185_1
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3270620_4
- `C16`: Increase A3 Offset threshold for 3253185_1
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3270620_4
- `C18`: Decrease A3 Offset threshold for 3270620_4
- `C19`: Increase transmission power for 3270620_4
- `C20`: Press down the tilt angle  of 3270620_4 by 8 degrees
- `C21`: Decrease A3 Offset threshold for 3253185_1
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3253185_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.307 | MS1 | 121.4656603616 | 31.1446240580 | 205 | 504990 | -85.08 | 15.98 | 580.07 | 0.05 | 2.06 | 1587 |
| 2024-09-20 22:21:32.516 | MS1 | 121.4656622888 | 31.1446248554 | 205 | 504990 | -87.78 | 13.02 | 346.48 | 0.10 | 2.69 | 1580 |
| 2024-09-20 22:21:33.177 | MS1 | 121.4656649115 | 31.1446326510 | 205 | 504990 | -91.32 | 16.51 | 528.32 | 0.09 | 2.47 | 1583 |
| 2024-09-20 22:21:34.933 | MS1 | 121.4656617583 | 31.1446311796 | 205 | 504990 | -89.02 | 15.18 | 54.73 | 0.15 | 2.26 | 1577 |
| 2024-09-20 22:21:35.352 | MS1 | 121.4656633456 | 31.1446259483 | 205 | 504990 | -91.15 | 16.28 | 98.07 | 0.03 | 2.23 | 1571 |
| 2024-09-20 22:21:36.174 | MS1 | 121.4656763887 | 31.1446317943 | 205 | 504990 | -85.07 | 17.64 | 75.73 | 0.16 | 2.65 | 1592 |
| 2024-09-20 22:21:37.716 | MS1 | 121.4656678175 | 31.1446281705 | 205 | 504990 | -91.61 | 12.27 | 96.84 | 0.00 | 2.30 | 1597 |
| 2024-09-20 22:21:38.610 | MS1 | 121.4656608077 | 31.1446215743 | 205 | 504990 | -92.50 | 10.21 | 96.94 | 0.03 | 2.24 | 1593 |
| 2024-09-20 22:21:39.889 | MS1 | 121.4656724981 | 31.1446364568 | 205 | 504990 | -91.46 | 8.07 | 73.13 | 0.01 | 2.03 | 1561 |
| 2024-09-20 22:21:40.264 | MS1 | 121.4656658345 | 31.1446379241 | 205 | 504990 | -92.20 | 8.37 | 328.01 | 0.06 | 2.70 | 1597 |
| 2024-09-20 22:21:41.149 | MS1 | 121.4656714935 | 31.1446270007 | 205 | 504990 | -90.07 | 10.59 | 518.86 | 0.20 | 2.04 | 1561 |
| 2024-09-20 22:21:42.737 | MS1 | 121.4656697046 | 31.1446202609 | 205 | 504990 | -90.89 | 12.70 | 545.43 | 0.10 | 2.93 | 1580 |

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
| 3222805 | 2 | 121.4656079903 | 31.1486739742 | 13 | 13 | 2 | 33.9 | TDD | 835 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3253185 | 1 | 121.4755967201 | 31.1553482055 | 31 | 11 | 10 | 16.4 | TDD | 205 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3265264 | 3 | 121.4672519772 | 31.1518689745 | 231 | 11 | 10 | 28.5 | TDD | 733 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3270620 | 4 | 121.4668787724 | 31.1552956459 | 82 | 6 | 7 | 46.0 | TDD | 207 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:31.295 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.316 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.441 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.441 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.139 | NREventA3 | measId:2;ServCellPCI:153;Se... |
| 2024-09-20 22:21:38.379 | NRHandoverAttempt | SourcePCI:153;SourceNR-ARFC... |
| 2024-09-20 22:21:38.425 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.439 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.543 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.543 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3253185 | 1 | 77.3377 | 77.2754 | -114.6474 | 13.7693 | 87.2513 | 0.0200 | 0.0143 |
| 2024_09_19 22:00 | 3222805 | 2 | 78.3604 | 82.3215 | -116.2954 | 11.3416 | 145.0842 | 0.0175 | 0.0039 |
| 2024_09_19 22:00 | 3265264 | 3 | 90.2840 | 84.2828 | -115.4787 | 12.9868 | 125.2434 | 0.0010 | 0.0016 |
| 2024_09_19 22:00 | 3270620 | 4 | 90.6670 | 82.6478 | -115.1423 | 6.6351 | 142.8372 | 0.0095 | 0.0050 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415829_24EF3034 | 504990 | 205 | -89.1 | 504990 | 207 | -94.5 | 504990 | 835 | -101.7 | 504990 | 733 |
| MR_1774415829_6D11B90D | 504990 | 205 | -88.7 | 504990 | 207 | -93.3 | 504990 | 835 | -105.3 | 504990 | 733 |
| MR_1774415829_211A17D8 | 504990 | 205 | -88.8 | 504990 | 207 | -96.1 | 504990 | 835 | -104.2 | 504990 | 733 |
| MR_1774415829_BE431A5F | 504990 | 205 | -89.2 | 504990 | 207 | -95.1 | 504990 | 835 | -104.4 | 504990 | 733 |
| MR_1774415829_21B01F04 | 504990 | 205 | -91.0 | 504990 | 207 | -95.9 | 504990 | 835 | -105.3 | 504990 | 733 |
| MR_1774415829_68F165DE | 504990 | 205 | -90.0 | 504990 | 207 | -96.4 | 504990 | 835 | -105.4 | 504990 | 733 |
| MR_1774415829_C429AD2C | 504990 | 205 | -87.9 | 504990 | 207 | -94.5 | 504990 | 835 | -104.3 | 504990 | 733 |
| MR_1774415829_E12FB3A4 | 504990 | 205 | -87.6 | 504990 | 207 | -93.3 | 504990 | 835 | -102.7 | 504990 | 733 |

> *... 2개 열 생략 (전체 14열)*

---
