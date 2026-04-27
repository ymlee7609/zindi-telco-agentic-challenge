# Track A 문제 분석 — train[1030]~train[1039]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[1030] ~ train[1039] (10개)

## 목차

1. [문제 1030: `0bed6f58-24b...`](#1030) — single-answer, 정답: C22
2. [문제 1031: `2617f17a-5cb...`](#1031) — single-answer, 정답: C21
3. [문제 1032: `79a3d36d-179...`](#1032) — single-answer, 정답: C18
4. [문제 1033: `40d745a9-559...`](#1033) — single-answer, 정답: C14
5. [문제 1034: `f100e18d-0c5...`](#1034) — single-answer, 정답: C20
6. [문제 1035: `3933d568-f6e...`](#1035) — single-answer, 정답: C12
7. [문제 1036: `a865e402-5e4...`](#1036) — single-answer, 정답: C17
8. [문제 1037: `da9973d7-c2f...`](#1037) — multiple-answer, 정답: C12|C18
9. [문제 1038: `eba4e047-db9...`](#1038) — multiple-answer, 정답: C4|C12
10. [문제 1039: `3ad16005-df4...`](#1039) — multiple-answer, 정답: C18|C22

---

### 문제 1030: `0bed6f58-24b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `0bed6f58-24b0-45cd-8d7c-d4065017bfff` |
| Tag | **single-answer** |
| 정답 | **C22** |
| C22 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1030] topology](images/train_1030.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3278106_2
- `C2`: Insufficient data; more data is needed for judgment.
- `C3`: Increase transmission power for 3278106_2
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3215797_4
- `C5`: Press down the tilt angle  of 3278106_2 by 4 degrees
- `C6`: Lift the tilt angle of 3215797_4 by 10 degrees
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3278106_2
- `C8`: Add neighbor relationship between 3242296_3 and 3278106_2
- `C9`: Decrease A3 Offset threshold for 3278106_2
- `C10`: Increase A3 Offset threshold for 3215797_4
- `C11`: Decrease transmission power for 3215797_4
- `C12`: Adjust the azimuth of 3278106_2 by 50 degrees
- `C13`: Add neighbor relationship between 3215797_4 and 3278106_2
- `C14`: Decrease A3 Offset threshold for 3215797_4
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3278106_2
- `C16`: Increase A3 Offset threshold for 3278106_2
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3215797_4
- `C18`: Increase transmission power for 3215797_4
- `C19`: Press down the tilt angle of 3215797_4 by 10 degrees
- `C20`: Lift the tilt angle  of 3278106_2 by 4 degrees
- `C21`: Adjust the azimuth of 3215797_4 by 50 degrees
- `C22`: Check test server and transmission issues **← 정답**

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.479 | MS1 | 121.4656601029 | 31.1446347226 | 607 | 504990 | -89.89 | 17.44 | 434.08 | 0.05 | 2.09 | 1577 |
| 2024-09-20 22:21:32.885 | MS1 | 121.4656706050 | 31.1446186042 | 607 | 504990 | -89.90 | 17.26 | 591.84 | 0.01 | 2.55 | 1572 |
| 2024-09-20 22:21:33.546 | MS1 | 121.4656632063 | 31.1446198731 | 607 | 504990 | -88.92 | 17.91 | 422.52 | 0.06 | 2.70 | 1562 |
| 2024-09-20 22:21:34.670 | MS1 | 121.4656626689 | 31.1446272662 | 607 | 504990 | -89.42 | 12.74 | 66.85 | 0.05 | 2.27 | 351 |
| 2024-09-20 22:21:35.209 | MS1 | 121.4656662813 | 31.1446314053 | 607 | 504990 | -86.37 | 12.89 | 68.39 | 0.08 | 2.46 | 443 |
| 2024-09-20 22:21:36.553 | MS1 | 121.4656683876 | 31.1446254405 | 607 | 504990 | -91.68 | 12.45 | 58.57 | 0.19 | 2.22 | 347 |
| 2024-09-20 22:21:37.984 | MS1 | 121.4656613320 | 31.1446358196 | 607 | 504990 | -89.76 | 7.22 | 85.49 | 0.05 | 2.64 | 416 |
| 2024-09-20 22:21:38.152 | MS1 | 121.4656650272 | 31.1446373041 | 607 | 504990 | -92.41 | 7.92 | 77.92 | 0.03 | 2.08 | 356 |
| 2024-09-20 22:21:39.332 | MS1 | 121.4656750090 | 31.1446316468 | 607 | 504990 | -91.76 | 11.32 | 89.17 | 0.13 | 2.61 | 314 |
| 2024-09-20 22:21:40.593 | MS1 | 121.4656745043 | 31.1446339736 | 607 | 504990 | -89.98 | 9.19 | 556.95 | 0.09 | 2.91 | 1565 |
| 2024-09-20 22:21:41.503 | MS1 | 121.4656708586 | 31.1446216187 | 607 | 504990 | -92.96 | 7.79 | 413.53 | 0.04 | 2.63 | 1577 |
| 2024-09-20 22:21:42.182 | MS1 | 121.4656744723 | 31.1446201276 | 607 | 504990 | -90.25 | 7.92 | 584.28 | 0.10 | 2.89 | 1583 |

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
| 3215797 | 4 | 121.4665905056 | 31.1447172396 | 353 | 12 | 10 | 21.9 | TDD | 607 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3223629 | 1 | 121.4679545811 | 31.1503312494 | 133 | 14 | 4 | 22.2 | TDD | 440 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3242296 | 3 | 121.4697233119 | 31.1524785703 | 100 | 4 | 2 | 30.6 | TDD | 964 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3278106 | 2 | 121.4745206121 | 31.1465188569 | 74 | 3 | 3 | 17.4 | TDD | 972 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |

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
| 2024-09-20 22:21:31.342 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.367 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.516 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.516 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.233 | NREventA3 | measId:2;ServCellPCI:775;Se... |
| 2024-09-20 22:21:38.473 | NRHandoverAttempt | SourcePCI:775;SourceNR-ARFC... |
| 2024-09-20 22:21:38.518 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.533 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.660 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.660 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3223629 | 1 | 8.2678 | 14.3667 | -116.9097 | 15.2332 | 184.6801 | 0.0096 | 0.0073 |
| 2024_09_20 22:00 | 3278106 | 2 | 11.7374 | 15.7814 | -116.6833 | 15.1995 | 142.0988 | 0.0006 | 0.0049 |
| 2024_09_20 22:00 | 3242296 | 3 | 6.6786 | 14.0157 | -115.9241 | 5.9102 | 145.5120 | 0.0020 | 0.0173 |
| 2024_09_20 22:00 | 3215797 | 4 | 10.3803 | 15.4902 | -114.3718 | 18.2377 | 88.9426 | 0.0017 | 0.0108 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417109_F712667D | 504990 | 607 | -90.7 | 504990 | 972 | -99.2 | 504990 | 964 | -101.1 | 504990 | 440 |
| MR_1774417109_A94958B8 | 504990 | 607 | -88.8 | 504990 | 972 | -98.6 | 504990 | 964 | -100.2 | 504990 | 440 |
| MR_1774417109_E40D6767 | 504990 | 607 | -90.0 | 504990 | 972 | -98.9 | 504990 | 964 | -100.5 | 504990 | 440 |
| MR_1774417109_A01E9705 | 504990 | 607 | -91.3 | 504990 | 972 | -101.0 | 504990 | 964 | -100.7 | 504990 | 440 |
| MR_1774417109_0CFA9EF4 | 504990 | 607 | -88.5 | 504990 | 972 | -99.9 | 504990 | 964 | -98.6 | 504990 | 440 |
| MR_1774417109_762432AB | 504990 | 607 | -88.1 | 504990 | 972 | -100.1 | 504990 | 964 | -98.4 | 504990 | 440 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1031: `2617f17a-5cb...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `2617f17a-5cbd-4022-bd3c-98496693d2aa` |
| Tag | **single-answer** |
| 정답 | **C21** |
| C21 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3246961_5 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1031] topology](images/train_1031.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3223818_12 and 3274746_4
- `C2`: Add neighbor relationship between 3246961_5 and 3274746_4
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3246961_5
- `C4`: Decrease A3 Offset threshold for 3246961_5
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3274746_4
- `C6`: Adjust the azimuth of 3246961_5 by 43 degrees
- `C7`: Increase A3 Offset threshold for 3246961_5
- `C8`: Decrease transmission power for 3246961_5
- `C9`: Insufficient data; more data is needed for judgment.
- `C10`: Press down the tilt angle  of 3274746_4 by 4 degrees
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3274746_4
- `C12`: Decrease transmission power for 3274746_4
- `C13`: Increase transmission power for 3246961_5
- `C14`: Adjust the azimuth of 3274746_4 by 5 degrees
- `C15`: Decrease A3 Offset threshold for 3274746_4
- `C16`: Increase A3 Offset threshold for 3274746_4
- `C17`: Lift the tilt angle of 3246961_5 by 6 degrees
- `C18`: Check test server and transmission issues
- `C19`: Lift the tilt angle  of 3274746_4 by 4 degrees
- `C20`: Press down the tilt angle of 3246961_5 by 6 degrees
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3246961_5 **← 정답**
- `C22`: Increase transmission power for 3274746_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.318 | MS1 | 121.4656765036 | 31.1446233091 | 851 | 504990 | -94.06 | 10.71 | 309.72 | 0.05 | 2.30 | 1565 |
| 2024-09-20 22:21:32.312 | MS1 | 121.4656699707 | 31.1446231542 | 717 | 504990 | -95.47 | 11.24 | 350.28 | 0.08 | 2.00 | 1572 |
| 2024-09-20 22:21:33.366 | MS1 | 121.4656685385 | 31.1446281326 | 587 | 504990 | -94.16 | 12.14 | 327.15 | 0.16 | 2.94 | 1560 |
| 2024-09-20 22:21:34.925 | MS1 | 121.4656631237 | 31.1446313739 | 681 | 152650 | -95.02 | 3.08 | 53.47 | 0.03 | 1.87 | 912 |
| 2024-09-20 22:21:35.609 | MS1 | 121.4656701456 | 31.1446345088 | 833 | 152650 | -92.74 | 2.53 | 93.92 | 0.13 | 1.84 | 943 |
| 2024-09-20 22:21:36.698 | MS1 | 121.4656753612 | 31.1446235099 | 946 | 152650 | -87.26 | 3.71 | 86.69 | 0.01 | 1.72 | 921 |
| 2024-09-20 22:21:37.927 | MS1 | 121.4656724844 | 31.1446308678 | 547 | 152650 | -92.63 | 5.24 | 88.05 | 0.04 | 1.50 | 910 |
| 2024-09-20 22:21:38.996 | MS1 | 121.4656647782 | 31.1446345341 | 681 | 152650 | -90.62 | 7.58 | 67.11 | 0.08 | 1.54 | 958 |
| 2024-09-20 22:21:39.709 | MS1 | 121.4656605456 | 31.1446308781 | 833 | 152650 | -93.70 | 4.51 | 54.62 | 0.17 | 1.57 | 988 |
| 2024-09-20 22:21:40.689 | MS1 | 121.4656640848 | 31.1446331829 | 946 | 152650 | -93.87 | 4.71 | 77.69 | 0.13 | 2.98 | 1575 |
| 2024-09-20 22:21:41.496 | MS1 | 121.4656618370 | 31.1446344245 | 547 | 152650 | -89.16 | 5.29 | 80.81 | 0.00 | 2.59 | 1564 |
| 2024-09-20 22:21:42.858 | MS1 | 121.4656684859 | 31.1446244947 | 681 | 152650 | -90.41 | 3.17 | 80.71 | 0.04 | 2.17 | 1593 |

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
| 3213419 | 6 | 121.4663611023 | 31.1476196568 | 278 | 4 | 0 | 13.8 | TDD | 663 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3219120 | 13 | 121.4737377161 | 31.1450207718 | 291 | 7 | 7 | 26.8 | FDD | 338 | n1 | 152650 | 30M | 4T4R | 17 | 152650 |
| 3222375 | 2 | 121.4645723233 | 31.1540332109 | 159 | 2 | 12 | 4.5 | TDD | 493 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3223818 | 12 | 121.4686129397 | 31.1445249569 | 143 | 5 | 9 | 27.9 | FDD | 946 | n1 | 152650 | 30M | 4T4R | 10 | 152650 |
| 3225842 | 10 | 121.4686870608 | 31.1530181126 | 264 | 15 | 8 | 15.1 | FDD | 424 | n1 | 152650 | 30M | 4T4R | 23 | 152650 |
| 3246447 | 8 | 121.4693933463 | 31.1440458714 | 6 | 2 | 8 | 6.8 | FDD | 866 | n1 | 152650 | 30M | 4T4R | 27 | 152650 |
| 3246961 | 5 | 121.4645144667 | 31.1552648189 | 218 | 5 | 4 | 11.6 | TDD | 851 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3254978 | 7 | 121.4654304611 | 31.1529420460 | 198 | 9 | 5 | 17.2 | FDD | 833 | n1 | 152650 | 30M | 4T4R | 18 | 152650 |
| 3255976 | 1 | 121.4682385181 | 31.1466079794 | 145 | 9 | 5 | 5.0 | TDD | 587 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3258178 | 9 | 121.4672598156 | 31.1510785647 | 69 | 4 | 9 | 10.2 | FDD | 547 | n1 | 152650 | 30M | 4T4R | 24 | 152650 |
| 3272068 | 11 | 121.4658533162 | 31.1540283450 | 348 | 4 | 3 | 26.9 | FDD | 681 | n1 | 152650 | 30M | 4T4R | 13 | 152650 |
| 3274746 | 4 | 121.4717481266 | 31.1525163886 | 218 | 4 | 3 | 2.8 | TDD | 560 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3277841 | 3 | 121.4654191499 | 31.1537704716 | 18 | 12 | 11 | 3.9 | TDD | 717 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:31.006 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.024 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.141 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.141 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.807 | NREventA2 | measId:1;ServCellPCI:378;Se... |
| 2024-09-20 22:21:34.936 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.188 | NREventA5 | measId:3;ServCellPCI:378;Se... |
| 2024-09-20 22:21:35.252 | NRHandoverAttempt | SourcePCI:378;SourceNR-ARFC... |
| 2024-09-20 22:21:35.276 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.287 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:35.416 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.416 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3255976 | 1 | 19.4215 | 19.3366 | -115.8617 | 19.0395 | 156.6873 | 0.0001 | 0.0162 |
| 2024_09_20 22:00 | 3222375 | 2 | 14.6304 | 12.1506 | -116.5949 | 6.8802 | 93.5661 | 0.0138 | 0.0153 |
| 2024_09_20 22:00 | 3277841 | 3 | 17.4017 | 8.1163 | -115.9108 | 8.9902 | 103.3983 | 0.0094 | 0.0127 |
| 2024_09_20 22:00 | 3274746 | 4 | 5.9387 | 13.1882 | -114.7123 | 7.8373 | 199.7182 | 0.0164 | 0.0096 |
| 2024_09_20 22:00 | 3246961 | 5 | 16.2268 | 18.6376 | -117.7028 | 15.4975 | 191.3278 | 0.0002 | 0.0174 |
| 2024_09_20 22:00 | 3213419 | 6 | 16.6377 | 12.7913 | -117.0118 | 12.9087 | 185.3893 | 0.0130 | 0.0091 |
| 2024_09_20 22:00 | 3254978 | 7 | 7.9507 | 15.8358 | -114.0319 | 3.4580 | 40.6715 | 0.0143 | 0.0021 |
| 2024_09_20 22:00 | 3246447 | 8 | 10.4868 | 8.5165 | -117.5710 | 4.0074 | 31.0975 | 0.0085 | 0.0161 |
| 2024_09_20 22:00 | 3258178 | 9 | 7.5034 | 9.7847 | -114.0129 | 4.8588 | 49.7144 | 0.0084 | 0.0143 |
| 2024_09_20 22:00 | 3225842 | 10 | 11.1088 | 8.2281 | -117.9218 | 3.9835 | 57.1551 | 0.0020 | 0.0116 |
| 2024_09_20 22:00 | 3272068 | 11 | 17.7614 | 8.3039 | -114.4674 | 3.6090 | 21.5644 | 0.0134 | 0.0050 |
| 2024_09_20 22:00 | 3223818 | 12 | 17.6454 | 15.5906 | -117.0869 | 4.7314 | 31.9357 | 0.0064 | 0.0057 |
| 2024_09_20 22:00 | 3219120 | 13 | 12.2543 | 17.6879 | -117.5441 | 4.3335 | 23.0295 | 0.0009 | 0.0155 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414619_D0FFBEC6 | 504990 | 587 | -95.0 | 504990 | 560 | -92.0 | 504990 | 493 | -100.7 | 504990 | 663 |
| MR_1774414619_F26ADAC9 | 504990 | 587 | -94.7 | 504990 | 560 | -91.6 | 504990 | 493 | -103.1 | 504990 | 663 |
| MR_1774414619_5B59DD72 | 152650 | 681 | -95.2 | 152650 | 866 | -100.6 | 152650 | 424 | -106.1 | 152650 | 338 |
| MR_1774414619_D71AA110 | 152650 | 681 | -94.4 | 152650 | 866 | -101.6 | 152650 | 424 | -103.3 | 152650 | 338 |
| MR_1774414619_1F98C1EC | 152650 | 681 | -93.2 | 152650 | 866 | -99.3 | 152650 | 424 | -104.5 | 152650 | 338 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1032: `79a3d36d-179...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `79a3d36d-179e-4d02-8969-21042956c5f7` |
| Tag | **single-answer** |
| 정답 | **C18** |
| C18 의미 | Decrease A3 Offset threshold for 3256250_3 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1032] topology](images/train_1032.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3251047_1
- `C2`: Press down the tilt angle of 3256250_3 by 5 degrees
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3256250_3
- `C4`: Decrease transmission power for 3251047_1
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3256250_3
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3251047_1
- `C7`: Press down the tilt angle  of 3251047_1 by 6 degrees
- `C8`: Increase A3 Offset threshold for 3256250_3
- `C9`: Increase transmission power for 3251047_1
- `C10`: Add neighbor relationship between 3233911_4 and 3251047_1
- `C11`: Lift the tilt angle of 3256250_3 by 5 degrees
- `C12`: Add neighbor relationship between 3256250_3 and 3251047_1
- `C13`: Insufficient data; more data is needed for judgment.
- `C14`: Check test server and transmission issues
- `C15`: Lift the tilt angle  of 3251047_1 by 6 degrees
- `C16`: Decrease transmission power for 3256250_3
- `C17`: Increase transmission power for 3256250_3
- `C18`: Decrease A3 Offset threshold for 3256250_3 **← 정답**
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3251047_1
- `C20`: Adjust the azimuth of 3256250_3 by 50 degrees
- `C21`: Adjust the azimuth of 3251047_1 by 50 degrees
- `C22`: Decrease A3 Offset threshold for 3251047_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.602 | MS1 | 121.4656593787 | 31.1446244391 | 549 | 504990 | -79.40 | 17.81 | 517.90 | 0.02 | 2.18 | 1568 |
| 2024-09-20 22:21:32.619 | MS1 | 121.4656632422 | 31.1446210880 | 549 | 504990 | -84.39 | 13.53 | 321.58 | 0.07 | 2.60 | 1570 |
| 2024-09-20 22:21:33.778 | MS1 | 121.4656699660 | 31.1446240106 | 549 | 504990 | -82.45 | 14.37 | 538.06 | 0.10 | 2.67 | 1579 |
| 2024-09-20 22:21:34.441 | MS1 | 121.4656610547 | 31.1446342936 | 549 | 504990 | -91.09 | -0.22 | 35.92 | 0.10 | 1.06 | 1570 |
| 2024-09-20 22:21:35.318 | MS1 | 121.4656590706 | 31.1446228125 | 549 | 504990 | -83.77 | -2.51 | 40.66 | 0.12 | 1.50 | 1569 |
| 2024-09-20 22:21:36.681 | MS1 | 121.4656642806 | 31.1446284385 | 549 | 504990 | -84.00 | -3.99 | 53.34 | 0.07 | 1.29 | 1594 |
| 2024-09-20 22:21:37.432 | MS1 | 121.4656761613 | 31.1446268387 | 549 | 504990 | -84.17 | -1.63 | 60.97 | 0.05 | 1.49 | 1566 |
| 2024-09-20 22:21:38.967 | MS1 | 121.4656585088 | 31.1446212815 | 549 | 504990 | -92.05 | -3.71 | 64.96 | 0.07 | 1.33 | 1575 |
| 2024-09-20 22:21:39.842 | MS1 | 121.4656608937 | 31.1446310112 | 726 | 504990 | -77.77 | 16.87 | 282.00 | 0.01 | 1.02 | 1587 |
| 2024-09-20 22:21:40.345 | MS1 | 121.4656725145 | 31.1446309082 | 726 | 504990 | -76.60 | 15.25 | 309.50 | 0.18 | 2.74 | 1581 |
| 2024-09-20 22:21:41.104 | MS1 | 121.4656672814 | 31.1446292156 | 726 | 504990 | -76.26 | 16.32 | 322.11 | 0.02 | 2.63 | 1564 |
| 2024-09-20 22:21:42.894 | MS1 | 121.4656660272 | 31.1446298012 | 726 | 504990 | -75.95 | 16.16 | 531.77 | 0.09 | 2.34 | 1563 |

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
| 3233911 | 4 | 121.4656743232 | 31.1548769577 | 25 | 11 | 9 | 25.2 | TDD | 558 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3251047 | 1 | 121.4663913300 | 31.1528134269 | 114 | 5 | 11 | 18.1 | TDD | 726 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3256250 | 3 | 121.4691843130 | 31.1520498613 | 134 | 3 | 7 | 35.7 | TDD | 549 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3265570 | 2 | 121.4752018797 | 31.1549896229 | 242 | 9 | 0 | 19.0 | TDD | 803 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |

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
| 2024-09-20 22:21:31.591 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.614 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.724 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.724 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.400 | NREventA3 | measId:2;ServCellPCI:359;Se... |
| 2024-09-20 22:21:38.640 | NRHandoverAttempt | SourcePCI:359;SourceNR-ARFC... |
| 2024-09-20 22:21:38.689 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.699 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.843 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.843 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3251047 | 1 | 12.4252 | 14.7890 | -115.5428 | 8.8324 | 153.9807 | 0.0142 | 0.0005 |
| 2024_09_20 22:00 | 3265570 | 2 | 18.2930 | 15.9482 | -117.2220 | 16.9147 | 83.2347 | 0.0117 | 0.0044 |
| 2024_09_20 22:00 | 3256250 | 3 | 18.8253 | 10.4603 | -115.9350 | 10.5619 | 188.3498 | 0.0106 | 0.1413 |
| 2024_09_20 22:00 | 3233911 | 4 | 19.6913 | 10.7879 | -116.9325 | 9.9300 | 137.6812 | 0.0038 | 0.0185 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416801_4A938622 | 504990 | 549 | -92.4 | 504990 | 726 | -86.8 | 504990 | 558 | -85.3 | 504990 | 803 |
| MR_1774416801_F4FFB26C | 504990 | 726 | -85.2 | 504990 | 549 | -89.1 | 504990 | 558 | -87.2 | 504990 | 803 |
| MR_1774416801_5C8409A2 | 504990 | 549 | -90.7 | 504990 | 726 | -86.6 | 504990 | 558 | -87.4 | 504990 | 803 |
| MR_1774416801_8CAB0508 | 504990 | 549 | -90.0 | 504990 | 726 | -86.2 | 504990 | 558 | -86.5 | 504990 | 803 |
| MR_1774416801_3FEF6E10 | 504990 | 549 | -91.9 | 504990 | 726 | -84.5 | 504990 | 558 | -84.9 | 504990 | 803 |
| MR_1774416801_6FFE89E3 | 504990 | 549 | -92.4 | 504990 | 726 | -87.7 | 504990 | 558 | -87.9 | 504990 | 803 |
| MR_1774416801_634754B5 | 504990 | 726 | -84.4 | 504990 | 549 | -90.2 | 504990 | 558 | -86.7 | 504990 | 803 |
| MR_1774416801_D2B24C95 | 504990 | 549 | -89.1 | 504990 | 726 | -84.4 | 504990 | 558 | -87.6 | 504990 | 803 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1033: `40d745a9-559...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `40d745a9-5592-4972-9cce-b1985dff81b0` |
| Tag | **single-answer** |
| 정답 | **C14** |
| C14 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1033] topology](images/train_1033.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3265356_1
- `C2`: Adjust the azimuth of 3265356_1 by 50 degrees
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3234165_4
- `C4`: Add neighbor relationship between 3278913_3 and 3234165_4
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3234165_4
- `C6`: Insufficient data; more data is needed for judgment.
- `C7`: Add neighbor relationship between 3265356_1 and 3234165_4
- `C8`: Increase transmission power for 3234165_4
- `C9`: Increase A3 Offset threshold for 3234165_4
- `C10`: Press down the tilt angle of 3265356_1 by 10 degrees
- `C11`: Increase A3 Offset threshold for 3265356_1
- `C12`: Increase transmission power for 3265356_1
- `C13`: Decrease A3 Offset threshold for 3234165_4
- `C14`: Check test server and transmission issues **← 정답**
- `C15`: Adjust the azimuth of 3234165_4 by 2 degrees
- `C16`: Decrease transmission power for 3234165_4
- `C17`: Decrease A3 Offset threshold for 3265356_1
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3265356_1
- `C19`: Decrease transmission power for 3265356_1
- `C20`: Press down the tilt angle  of 3234165_4 by 10 degrees
- `C21`: Lift the tilt angle  of 3234165_4 by 10 degrees
- `C22`: Lift the tilt angle of 3265356_1 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.655 | MS1 | 121.4656654047 | 31.1446297200 | 846 | 504990 | -91.01 | 12.12 | 400.40 | 0.04 | 2.92 | 1598 |
| 2024-09-20 22:21:32.609 | MS1 | 121.4656679001 | 31.1446342191 | 846 | 504990 | -85.40 | 13.94 | 580.62 | 0.04 | 2.48 | 1596 |
| 2024-09-20 22:21:33.371 | MS1 | 121.4656693862 | 31.1446248917 | 846 | 504990 | -86.11 | 17.76 | 466.86 | 0.04 | 2.51 | 1579 |
| 2024-09-20 22:21:34.927 | MS1 | 121.4656747174 | 31.1446357527 | 846 | 504990 | -86.45 | 15.64 | 91.54 | 0.12 | 2.55 | 442 |
| 2024-09-20 22:21:35.434 | MS1 | 121.4656752669 | 31.1446251161 | 846 | 504990 | -88.40 | 15.99 | 80.14 | 0.02 | 2.88 | 428 |
| 2024-09-20 22:21:36.784 | MS1 | 121.4656712459 | 31.1446259510 | 846 | 504990 | -87.67 | 12.30 | 105.66 | 0.14 | 2.25 | 314 |
| 2024-09-20 22:21:37.347 | MS1 | 121.4656599467 | 31.1446231745 | 846 | 504990 | -92.01 | 12.56 | 50.73 | 0.03 | 2.03 | 388 |
| 2024-09-20 22:21:38.268 | MS1 | 121.4656595085 | 31.1446256609 | 846 | 504990 | -93.81 | 7.78 | 93.16 | 0.20 | 2.95 | 426 |
| 2024-09-20 22:21:39.741 | MS1 | 121.4656720327 | 31.1446319818 | 846 | 504990 | -89.96 | 12.55 | 75.52 | 0.20 | 2.97 | 462 |
| 2024-09-20 22:21:40.946 | MS1 | 121.4656766147 | 31.1446209356 | 846 | 504990 | -92.47 | 12.40 | 579.87 | 0.04 | 2.32 | 1579 |
| 2024-09-20 22:21:41.548 | MS1 | 121.4656630885 | 31.1446247509 | 846 | 504990 | -92.93 | 8.11 | 547.78 | 0.09 | 2.78 | 1589 |
| 2024-09-20 22:21:42.268 | MS1 | 121.4656724679 | 31.1446272778 | 846 | 504990 | -89.50 | 7.87 | 324.49 | 0.14 | 2.19 | 1580 |

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
| 3234165 | 4 | 121.4724411031 | 31.1481314208 | 241 | 10 | 12 | 21.8 | TDD | 510 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3260956 | 2 | 121.4731595021 | 31.1508492089 | 338 | 15 | 9 | 16.2 | TDD | 452 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3265356 | 1 | 121.4667153870 | 31.1466292689 | 41 | 6 | 1 | 22.3 | TDD | 846 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3278913 | 3 | 121.4663132911 | 31.1543519048 | 238 | 1 | 3 | 24.5 | TDD | 654 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:31.160 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.175 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.289 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.289 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.026 | NREventA3 | measId:2;ServCellPCI:81;Ser... |
| 2024-09-20 22:21:38.266 | NRHandoverAttempt | SourcePCI:81;SourceNR-ARFCN... |
| 2024-09-20 22:21:38.296 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.309 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.409 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.409 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3265356 | 1 | 5.5139 | 17.9174 | -116.9002 | 10.1889 | 197.1362 | 0.0144 | 0.0199 |
| 2024_09_20 22:00 | 3260956 | 2 | 5.8469 | 17.7514 | -115.0593 | 18.3445 | 120.5285 | 0.0013 | 0.0167 |
| 2024_09_20 22:00 | 3278913 | 3 | 6.7298 | 18.4682 | -117.0301 | 6.3112 | 165.0423 | 0.0030 | 0.0087 |
| 2024_09_20 22:00 | 3234165 | 4 | 19.8391 | 13.4092 | -117.7542 | 9.4845 | 196.7172 | 0.0061 | 0.0159 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413869_2B3AD7C5 | 504990 | 846 | -86.6 | 504990 | 510 | -95.3 | 504990 | 654 | -97.5 | 504990 | 452 |
| MR_1774413869_106C7624 | 504990 | 846 | -87.4 | 504990 | 510 | -94.5 | 504990 | 654 | -96.6 | 504990 | 452 |
| MR_1774413869_497F8E0C | 504990 | 846 | -84.9 | 504990 | 510 | -93.6 | 504990 | 654 | -94.4 | 504990 | 452 |
| MR_1774413869_6B180198 | 504990 | 846 | -88.1 | 504990 | 510 | -94.4 | 504990 | 654 | -96.1 | 504990 | 452 |
| MR_1774413869_11F2A100 | 504990 | 846 | -85.0 | 504990 | 510 | -96.9 | 504990 | 654 | -95.4 | 504990 | 452 |
| MR_1774413869_1481F2CB | 504990 | 846 | -85.0 | 504990 | 510 | -94.7 | 504990 | 654 | -93.7 | 504990 | 452 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1034: `f100e18d-0c5...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `f100e18d-0c5b-4f05-acfb-3c182dc89952` |
| Tag | **single-answer** |
| 정답 | **C20** |
| C20 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3256096_4 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1034] topology](images/train_1034.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3256096_4 by 2 degrees
- `C2`: Decrease A3 Offset threshold for 3256096_4
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3256096_4
- `C4`: Decrease transmission power for 3272473_2
- `C5`: Lift the tilt angle  of 3272473_2 by 6 degrees
- `C6`: Check test server and transmission issues
- `C7`: Increase A3 Offset threshold for 3256096_4
- `C8`: Increase A3 Offset threshold for 3272473_2
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3272473_2
- `C10`: Add neighbor relationship between 3256096_4 and 3272473_2
- `C11`: Adjust the azimuth of 3256096_4 by 27 degrees
- `C12`: Decrease transmission power for 3256096_4
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3272473_2
- `C14`: Increase transmission power for 3256096_4
- `C15`: Add neighbor relationship between 3232822_13 and 3272473_2
- `C16`: Decrease A3 Offset threshold for 3272473_2
- `C17`: Increase transmission power for 3272473_2
- `C18`: Insufficient data; more data is needed for judgment.
- `C19`: Press down the tilt angle  of 3272473_2 by 6 degrees
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3256096_4 **← 정답**
- `C21`: Adjust the azimuth of 3272473_2 by 17 degrees
- `C22`: Lift the tilt angle of 3256096_4 by 2 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.713 | MS1 | 121.4656702080 | 31.1446323122 | 270 | 504990 | -93.54 | 13.00 | 448.00 | 0.04 | 2.48 | 1595 |
| 2024-09-20 22:21:32.776 | MS1 | 121.4656657416 | 31.1446315969 | 615 | 504990 | -93.26 | 9.25 | 389.77 | 0.11 | 2.43 | 1590 |
| 2024-09-20 22:21:33.991 | MS1 | 121.4656705354 | 31.1446252470 | 34 | 504990 | -94.25 | 9.90 | 308.65 | 0.16 | 2.39 | 1588 |
| 2024-09-20 22:21:34.337 | MS1 | 121.4656656423 | 31.1446286556 | 689 | 152650 | -91.24 | 4.69 | 63.67 | 0.02 | 1.75 | 934 |
| 2024-09-20 22:21:35.277 | MS1 | 121.4656646352 | 31.1446225194 | 238 | 152650 | -93.08 | 4.53 | 82.11 | 0.06 | 1.90 | 966 |
| 2024-09-20 22:21:36.578 | MS1 | 121.4656629609 | 31.1446311961 | 853 | 152650 | -90.45 | 2.25 | 77.22 | 0.09 | 1.74 | 911 |
| 2024-09-20 22:21:37.487 | MS1 | 121.4656613439 | 31.1446276517 | 468 | 152650 | -95.59 | 5.99 | 61.18 | 0.15 | 1.54 | 910 |
| 2024-09-20 22:21:38.836 | MS1 | 121.4656640885 | 31.1446306160 | 689 | 152650 | -93.81 | 4.81 | 66.65 | 0.03 | 1.64 | 999 |
| 2024-09-20 22:21:39.975 | MS1 | 121.4656667822 | 31.1446230362 | 238 | 152650 | -92.49 | 5.15 | 99.12 | 0.06 | 1.75 | 981 |
| 2024-09-20 22:21:40.538 | MS1 | 121.4656727534 | 31.1446275010 | 853 | 152650 | -91.65 | 5.01 | 74.44 | 0.02 | 2.77 | 1572 |
| 2024-09-20 22:21:41.269 | MS1 | 121.4656753807 | 31.1446349123 | 468 | 152650 | -93.92 | 5.67 | 65.15 | 0.07 | 2.32 | 1581 |
| 2024-09-20 22:21:42.759 | MS1 | 121.4656770117 | 31.1446275713 | 689 | 152650 | -89.56 | 2.66 | 79.74 | 0.10 | 2.70 | 1582 |

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
| 3213284 | 10 | 121.4700970722 | 31.1542496769 | 253 | 4 | 2 | 28.6 | FDD | 689 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |
| 3225028 | 1 | 121.4701899681 | 31.1529105337 | 119 | 2 | 2 | 25.3 | TDD | 34 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3232822 | 13 | 121.4645873418 | 31.1507518781 | 304 | 6 | 8 | 29.4 | FDD | 853 | n1 | 152650 | 30M | 4T4R | 10 | 152650 |
| 3238821 | 11 | 121.4686338012 | 31.1493735457 | 113 | 13 | 12 | 0.7 | FDD | 851 | n1 | 152650 | 30M | 4T4R | 13 | 152650 |
| 3238960 | 3 | 121.4689812246 | 31.1537234931 | 307 | 2 | 3 | 13.9 | TDD | 615 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3239885 | 5 | 121.4652610091 | 31.1462303269 | 47 | 0 | 5 | 11.5 | TDD | 278 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3241840 | 9 | 121.4662673081 | 31.1452833497 | 226 | 15 | 2 | 3.3 | FDD | 238 | n1 | 152650 | 30M | 4T4R | 29 | 152650 |
| 3243553 | 6 | 121.4700192404 | 31.1450135266 | 235 | 7 | 6 | 14.1 | TDD | 607 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3256096 | 4 | 121.4755702917 | 31.1530584433 | 252 | 2 | 7 | 3.1 | TDD | 270 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3262486 | 7 | 121.4753616128 | 31.1444050547 | 339 | 1 | 5 | 12.1 | FDD | 801 | n1 | 152650 | 30M | 4T4R | 17 | 152650 |
| 3270052 | 12 | 121.4657650976 | 31.1470881860 | 7 | 10 | 12 | 5.5 | FDD | 468 | n1 | 152650 | 30M | 4T4R | 18 | 152650 |
| 3272473 | 2 | 121.4694677873 | 31.1483797405 | 204 | 5 | 12 | 5.7 | TDD | 102 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3273640 | 8 | 121.4678347792 | 31.1496350574 | 221 | 15 | 2 | 13.2 | FDD | 936 | n1 | 152650 | 30M | 4T4R | 30 | 152650 |

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
| 2024-09-20 22:21:30.789 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.804 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:30.914 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.914 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.652 | NREventA2 | measId:1;ServCellPCI:41;Ser... |
| 2024-09-20 22:21:34.788 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.055 | NREventA5 | measId:3;ServCellPCI:41;Ser... |
| 2024-09-20 22:21:35.126 | NRHandoverAttempt | SourcePCI:41;SourceNR-ARFCN... |
| 2024-09-20 22:21:35.160 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.175 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:35.304 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.304 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3225028 | 1 | 5.1198 | 16.6611 | -114.8111 | 8.4743 | 189.6474 | 0.0196 | 0.0034 |
| 2024_09_20 22:00 | 3272473 | 2 | 7.6383 | 12.9252 | -117.5161 | 17.4945 | 194.0575 | 0.0170 | 0.0105 |
| 2024_09_20 22:00 | 3238960 | 3 | 9.4618 | 6.1612 | -114.0824 | 9.0071 | 134.1397 | 0.0162 | 0.0042 |
| 2024_09_20 22:00 | 3256096 | 4 | 6.3807 | 10.3433 | -114.1949 | 6.3313 | 192.8925 | 0.0138 | 0.0080 |
| 2024_09_20 22:00 | 3239885 | 5 | 14.7720 | 16.5570 | -117.2232 | 12.3576 | 111.5943 | 0.0118 | 0.0058 |
| 2024_09_20 22:00 | 3243553 | 6 | 19.7341 | 8.3026 | -114.6167 | 12.8074 | 145.5329 | 0.0057 | 0.0073 |
| 2024_09_20 22:00 | 3262486 | 7 | 10.9908 | 8.0855 | -116.7014 | 3.8926 | 28.1985 | 0.0105 | 0.0080 |
| 2024_09_20 22:00 | 3273640 | 8 | 16.0715 | 16.3597 | -116.2180 | 3.9026 | 44.6964 | 0.0160 | 0.0033 |
| 2024_09_20 22:00 | 3241840 | 9 | 9.3264 | 17.9874 | -116.3571 | 4.1496 | 49.2083 | 0.0073 | 0.0198 |
| 2024_09_20 22:00 | 3213284 | 10 | 15.9908 | 19.9250 | -115.4842 | 3.2175 | 49.9864 | 0.0158 | 0.0017 |
| 2024_09_20 22:00 | 3238821 | 11 | 15.2757 | 17.6855 | -115.0200 | 3.1507 | 43.0151 | 0.0077 | 0.0101 |
| 2024_09_20 22:00 | 3270052 | 12 | 11.5114 | 13.3001 | -117.2270 | 4.6757 | 47.6312 | 0.0137 | 0.0149 |
| 2024_09_20 22:00 | 3232822 | 13 | 11.7149 | 12.1408 | -117.0197 | 3.8294 | 45.8197 | 0.0175 | 0.0155 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412648_FEC49EA8 | 152650 | 689 | -91.9 | 152650 | 936 | -96.0 | 152650 | 851 | -96.0 | 152650 | 801 |
| MR_1774412648_5302EBC5 | 504990 | 34 | -96.1 | 504990 | 102 | -94.1 | 504990 | 607 | -97.5 | 504990 | 278 |
| MR_1774412648_E8C9B0A7 | 504990 | 34 | -95.0 | 504990 | 102 | -93.2 | 504990 | 607 | -97.9 | 504990 | 278 |
| MR_1774412648_1769995D | 152650 | 689 | -92.8 | 152650 | 936 | -92.4 | 152650 | 851 | -98.8 | 152650 | 801 |
| MR_1774412648_FC71E25A | 152650 | 689 | -91.4 | 152650 | 936 | -95.7 | 152650 | 851 | -96.0 | 152650 | 801 |
| MR_1774412648_BB40D861 | 152650 | 689 | -89.4 | 152650 | 936 | -93.2 | 152650 | 851 | -97.3 | 152650 | 801 |
| MR_1774412648_C0AFCC4B | 152650 | 689 | -90.7 | 152650 | 936 | -95.8 | 152650 | 851 | -97.8 | 152650 | 801 |
| MR_1774412648_8DCC1A74 | 504990 | 34 | -95.8 | 504990 | 102 | -94.0 | 504990 | 607 | -98.4 | 504990 | 278 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1035: `3933d568-f6e...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `3933d568-f6eb-4f00-bc0e-bbfd5d0c198d` |
| Tag | **single-answer** |
| 정답 | **C12** |
| C12 의미 | Lift the tilt angle  of 3229979_3 by 5 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1035] topology](images/train_1035.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3278473_2
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3252020_1
- `C3`: Decrease transmission power for 3278473_2
- `C4`: Adjust the azimuth of 3278473_2 by 39 degrees
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3278473_2
- `C6`: Lift the tilt angle of 3278473_2 by 4 degrees
- `C7`: Adjust the azimuth of 3229979_3 by 50 degrees
- `C8`: Increase transmission power for 3278473_2
- `C9`: Insufficient data; more data is needed for judgment.
- `C10`: Decrease A3 Offset threshold for 3252020_1
- `C11`: Increase A3 Offset threshold for 3278473_2
- `C12`: Lift the tilt angle  of 3229979_3 by 5 degrees **← 정답**
- `C13`: Increase transmission power for 3252020_1
- `C14`: Check test server and transmission issues
- `C15`: Increase A3 Offset threshold for 3252020_1
- `C16`: Press down the tilt angle of 3278473_2 by 4 degrees
- `C17`: Decrease A3 Offset threshold for 3278473_2
- `C18`: Press down the tilt angle  of 3229979_3 by 5 degrees
- `C19`: Decrease transmission power for 3252020_1
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3252020_1
- `C21`: Add neighbor relationship between 3229979_3 and 3252020_1
- `C22`: Add neighbor relationship between 3278473_2 and 3252020_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.943 | MS1 | 121.4656775861 | 31.1446242570 | 787 | 504990 | -85.56 | 13.70 | 310.43 | 0.06 | 2.39 | 1585 |
| 2024-09-20 22:21:32.405 | MS1 | 121.4656586362 | 31.1446190150 | 787 | 504990 | -90.23 | 17.58 | 537.74 | 0.10 | 2.21 | 1599 |
| 2024-09-20 22:21:33.967 | MS1 | 121.4656720179 | 31.1446352370 | 787 | 504990 | -87.98 | 17.91 | 394.00 | 0.04 | 2.62 | 1582 |
| 2024-09-20 22:21:34.980 | MS1 | 121.4656759028 | 31.1446185563 | 787 | 504990 | -91.16 | 12.59 | 61.00 | 0.06 | 2.15 | 1589 |
| 2024-09-20 22:21:35.117 | MS1 | 121.4656751120 | 31.1446272427 | 787 | 504990 | -91.02 | 16.72 | 53.50 | 0.15 | 2.86 | 1568 |
| 2024-09-20 22:21:36.770 | MS1 | 121.4656743393 | 31.1446203391 | 787 | 504990 | -86.84 | 17.48 | 64.64 | 0.04 | 2.96 | 1597 |
| 2024-09-20 22:21:37.290 | MS1 | 121.4656642135 | 31.1446366287 | 787 | 504990 | -90.24 | 11.68 | 46.25 | 0.12 | 2.37 | 1589 |
| 2024-09-20 22:21:38.895 | MS1 | 121.4656609814 | 31.1446313351 | 787 | 504990 | -92.03 | 9.93 | 92.46 | 0.18 | 2.09 | 1583 |
| 2024-09-20 22:21:39.240 | MS1 | 121.4656638544 | 31.1446199117 | 787 | 504990 | -93.81 | 11.72 | 96.61 | 0.10 | 2.86 | 1563 |
| 2024-09-20 22:21:40.665 | MS1 | 121.4656592180 | 31.1446278041 | 787 | 504990 | -93.88 | 11.04 | 304.99 | 0.09 | 2.71 | 1574 |
| 2024-09-20 22:21:41.781 | MS1 | 121.4656744867 | 31.1446304302 | 787 | 504990 | -90.19 | 10.78 | 400.97 | 0.19 | 2.61 | 1600 |
| 2024-09-20 22:21:42.250 | MS1 | 121.4656736307 | 31.1446338931 | 787 | 504990 | -90.00 | 10.37 | 517.61 | 0.09 | 2.94 | 1568 |

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
| 3229979 | 3 | 121.4674420548 | 31.1458335191 | 147 | 3 | 12 | 40.4 | TDD | 126 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3252020 | 1 | 121.4717538106 | 31.1440421045 | 328 | 1 | 4 | 37.3 | TDD | 33 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3258158 | 4 | 121.4758950930 | 31.1531502314 | 78 | 7 | 4 | 19.1 | TDD | 631 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3278473 | 2 | 121.4730500800 | 31.1481168075 | 280 | 1 | 5 | 43.3 | TDD | 787 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |

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
| 2024-09-20 22:21:31.461 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.482 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.591 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.591 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.294 | NREventA3 | measId:2;ServCellPCI:985;Se... |
| 2024-09-20 22:21:38.534 | NRHandoverAttempt | SourcePCI:985;SourceNR-ARFC... |
| 2024-09-20 22:21:38.578 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.593 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.715 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.715 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3252020 | 1 | 13.5517 | 19.7795 | -114.0518 | 15.0552 | 145.3366 | 0.0032 | 0.0015 |
| 2024_09_20 22:00 | 3278473 | 2 | 84.3524 | 75.1920 | -116.1744 | 12.7296 | 130.2131 | 0.0023 | 0.0124 |
| 2024_09_20 22:00 | 3229979 | 3 | 6.0401 | 5.3569 | -115.9070 | 13.3194 | 95.2116 | 0.0187 | 0.0192 |
| 2024_09_20 22:00 | 3258158 | 4 | 6.3036 | 15.4829 | -116.3095 | 12.8001 | 93.7521 | 0.0101 | 0.0112 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413667_D1A566D5 | 504990 | 787 | -89.2 | 504990 | 33 | -93.9 | 504990 | 126 | -100.2 | 504990 | 631 |
| MR_1774413667_F265957B | 504990 | 787 | -89.5 | 504990 | 33 | -92.3 | 504990 | 126 | -100.6 | 504990 | 631 |
| MR_1774413667_1E11A56C | 504990 | 787 | -91.3 | 504990 | 33 | -95.0 | 504990 | 126 | -100.3 | 504990 | 631 |
| MR_1774413667_D804A0CB | 504990 | 787 | -89.7 | 504990 | 33 | -93.6 | 504990 | 126 | -99.1 | 504990 | 631 |
| MR_1774413667_A3B65156 | 504990 | 787 | -91.0 | 504990 | 33 | -92.1 | 504990 | 126 | -101.7 | 504990 | 631 |
| MR_1774413667_03EFC157 | 504990 | 787 | -91.6 | 504990 | 33 | -92.6 | 504990 | 126 | -101.6 | 504990 | 631 |
| MR_1774413667_446D6D92 | 504990 | 787 | -90.0 | 504990 | 33 | -92.8 | 504990 | 126 | -101.9 | 504990 | 631 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1036: `a865e402-5e4...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `a865e402-5e4b-49e8-85d6-4ce5cf16c22b` |
| Tag | **single-answer** |
| 정답 | **C17** |
| C17 의미 | Add neighbor relationship between 3225225_1 and 3277305_2 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1036] topology](images/train_1036.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3225225_1
- `C2`: Decrease transmission power for 3277305_2
- `C3`: Adjust the azimuth of 3277305_2 by 42 degrees
- `C4`: Lift the tilt angle of 3225225_1 by 10 degrees
- `C5`: Decrease transmission power for 3225225_1
- `C6`: Press down the tilt angle  of 3277305_2 by 5 degrees
- `C7`: Lift the tilt angle  of 3277305_2 by 5 degrees
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3277305_2
- `C9`: Decrease A3 Offset threshold for 3277305_2
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3277305_2
- `C11`: Increase A3 Offset threshold for 3277305_2
- `C12`: Increase transmission power for 3277305_2
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3225225_1
- `C14`: Press down the tilt angle of 3225225_1 by 10 degrees
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3225225_1
- `C16`: Adjust the azimuth of 3225225_1 by 50 degrees
- `C17`: Add neighbor relationship between 3225225_1 and 3277305_2 **← 정답**
- `C18`: Insufficient data; more data is needed for judgment.
- `C19`: Check test server and transmission issues
- `C20`: Increase transmission power for 3225225_1
- `C21`: Add neighbor relationship between 3216720_4 and 3277305_2
- `C22`: Decrease A3 Offset threshold for 3225225_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.680 | MS1 | 121.4656763221 | 31.1446185012 | 179 | 504990 | -76.97 | 12.69 | 356.21 | 0.12 | 2.17 | 1576 |
| 2024-09-20 22:21:32.590 | MS1 | 121.4656672628 | 31.1446184778 | 179 | 504990 | -76.91 | 16.54 | 566.16 | 0.00 | 2.43 | 1580 |
| 2024-09-20 22:21:33.997 | MS1 | 121.4656627460 | 31.1446279247 | 179 | 504990 | -79.44 | 17.70 | 451.53 | 0.20 | 2.40 | 1568 |
| 2024-09-20 22:21:34.779 | MS1 | 121.4656755346 | 31.1446342584 | 179 | 504990 | -92.15 | -1.77 | 51.29 | 0.19 | 1.12 | 1573 |
| 2024-09-20 22:21:35.825 | MS1 | 121.4656651539 | 31.1446373017 | 179 | 504990 | -90.05 | -2.26 | 52.97 | 0.14 | 1.26 | 1587 |
| 2024-09-20 22:21:36.742 | MS1 | 121.4656776916 | 31.1446379504 | 179 | 504990 | -89.86 | -2.97 | 33.38 | 0.01 | 1.14 | 1583 |
| 2024-09-20 22:21:37.963 | MS1 | 121.4656709565 | 31.1446209965 | 179 | 504990 | -86.31 | -0.54 | 42.54 | 0.01 | 1.05 | 1588 |
| 2024-09-20 22:21:38.427 | MS1 | 121.4656755418 | 31.1446370539 | 179 | 504990 | -76.21 | 13.78 | 378.28 | 0.14 | 1.27 | 1569 |
| 2024-09-20 22:21:39.564 | MS1 | 121.4656729981 | 31.1446336902 | 179 | 504990 | -76.07 | 14.78 | 454.22 | 0.16 | 1.33 | 1593 |
| 2024-09-20 22:21:40.283 | MS1 | 121.4656689237 | 31.1446201588 | 179 | 504990 | -75.33 | 13.43 | 550.22 | 0.05 | 2.51 | 1568 |
| 2024-09-20 22:21:41.323 | MS1 | 121.4656611240 | 31.1446293225 | 179 | 504990 | -78.22 | 17.53 | 453.95 | 0.12 | 2.01 | 1572 |
| 2024-09-20 22:21:42.740 | MS1 | 121.4656730337 | 31.1446379305 | 179 | 504990 | -78.07 | 13.54 | 536.26 | 0.13 | 2.68 | 1598 |

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
| 3216720 | 4 | 121.4738801137 | 31.1488095511 | 150 | 6 | 9 | 39.0 | TDD | 71 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3225225 | 1 | 121.4733075902 | 31.1484333555 | 93 | 13 | 6 | 36.9 | TDD | 179 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3249927 | 3 | 121.4723634997 | 31.1487095820 | 332 | 13 | 2 | 45.0 | TDD | 723 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3277305 | 2 | 121.4709855660 | 31.1535373858 | 249 | 3 | 11 | 32.0 | TDD | 734 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |

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
| 2024-09-20 22:21:31.140 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.158 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.261 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.261 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.948 | NREventA3 | measId:2;ServCellPCI:113;Se... |
| 2024-09-20 22:21:35.948 | NREventA3 | measId:2;ServCellPCI:113;Se... |
| 2024-09-20 22:21:36.948 | NREventA3 | measId:2;ServCellPCI:113;Se... |
| 2024-09-20 22:21:39.448 | NRRRCReestablishAttempt | PCI:113 |
| 2024-09-20 22:21:39.460 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.472 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:39.613 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.613 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3225225 | 1 | 18.0610 | 10.7838 | -114.1342 | 6.1924 | 94.3485 | 0.0125 | 0.1389 |
| 2024_09_20 22:00 | 3277305 | 2 | 16.5898 | 6.9384 | -114.6332 | 19.2960 | 141.9950 | 0.0154 | 0.0040 |
| 2024_09_20 22:00 | 3249927 | 3 | 14.7509 | 6.1198 | -117.6264 | 6.9976 | 129.6122 | 0.0028 | 0.0057 |
| 2024_09_20 22:00 | 3216720 | 4 | 13.2376 | 7.4367 | -114.3953 | 16.0076 | 161.5986 | 0.0027 | 0.0177 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415610_A0C9667D | 504990 | 179 | -93.9 | 504990 | 734 | -85.9 | 504990 | 71 | -98.2 | 504990 | 723 |
| MR_1774415610_FCB1102E | 504990 | 734 | -85.8 | 504990 | 179 | -93.1 | 504990 | 71 | -97.1 | 504990 | 723 |
| MR_1774415610_9FD3A982 | 504990 | 179 | -92.7 | 504990 | 734 | -87.8 | 504990 | 71 | -95.5 | 504990 | 723 |
| MR_1774415610_13C69E01 | 504990 | 179 | -92.8 | 504990 | 734 | -88.5 | 504990 | 71 | -97.8 | 504990 | 723 |
| MR_1774415610_2C46DEC9 | 504990 | 179 | -91.3 | 504990 | 734 | -87.4 | 504990 | 71 | -95.1 | 504990 | 723 |
| MR_1774415610_3425990D | 504990 | 179 | -93.8 | 504990 | 734 | -87.1 | 504990 | 71 | -95.0 | 504990 | 723 |
| MR_1774415610_B126C60F | 504990 | 734 | -85.1 | 504990 | 179 | -92.0 | 504990 | 71 | -95.2 | 504990 | 723 |
| MR_1774415610_0BA8CDB2 | 504990 | 179 | -90.6 | 504990 | 734 | -85.3 | 504990 | 71 | -98.5 | 504990 | 723 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1037: `da9973d7-c2f...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `da9973d7-c2f1-4adb-a938-40502785a7f3` |
| Tag | **multiple-answer** |
| 정답 | **C12|C18** |
| C12 의미 | Adjust the azimuth of 3220094_3 by 50 degrees |
| C18 의미 | Increase transmission power for 3220094_3 |
| 패턴 분류 | **P4 Coverage (azimuth)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1037] topology](images/train_1037.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3273258_2 by 3 degrees
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3273258_2
- `C3`: Increase A3 Offset threshold for 3273258_2
- `C4`: Lift the tilt angle of 3220094_3 by 5 degrees
- `C5`: Decrease transmission power for 3220094_3
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3220094_3
- `C7`: Decrease A3 Offset threshold for 3273258_2
- `C8`: Insufficient data; more data is needed for judgment.
- `C9`: Add neighbor relationship between 3220094_3 and 3273258_2
- `C10`: Check test server and transmission issues
- `C11`: Add neighbor relationship between 3266123_1 and 3273258_2
- `C12`: Adjust the azimuth of 3220094_3 by 50 degrees **← 정답**
- `C13`: Decrease A3 Offset threshold for 3220094_3
- `C14`: Increase transmission power for 3273258_2
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3220094_3
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3273258_2
- `C17`: Decrease transmission power for 3273258_2
- `C18`: Increase transmission power for 3220094_3 **← 정답**
- `C19`: Increase A3 Offset threshold for 3220094_3
- `C20`: Press down the tilt angle of 3220094_3 by 5 degrees
- `C21`: Lift the tilt angle  of 3273258_2 by 3 degrees
- `C22`: Press down the tilt angle  of 3273258_2 by 3 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.639 | MS1 | 121.4656623381 | 31.1446185692 | 926 | 504990 | -94.02 | 17.33 | 572.87 | 0.18 | 2.15 | 1562 |
| 2024-09-20 22:21:32.740 | MS1 | 121.4656710881 | 31.1446217277 | 926 | 504990 | -91.36 | 14.54 | 429.93 | 0.19 | 2.56 | 1598 |
| 2024-09-20 22:21:33.292 | MS1 | 121.4656755592 | 31.1446344659 | 926 | 504990 | -90.87 | 14.14 | 400.84 | 0.12 | 2.98 | 1581 |
| 2024-09-20 22:21:34.437 | MS1 | 121.4656719388 | 31.1446324408 | 926 | 504990 | -104.77 | -1.40 | 19.77 | 0.17 | 1.35 | 1565 |
| 2024-09-20 22:21:35.482 | MS1 | 121.4656741472 | 31.1446312219 | 926 | 504990 | -103.17 | -1.43 | 58.44 | 0.07 | 1.04 | 1591 |
| 2024-09-20 22:21:36.513 | MS1 | 121.4656746313 | 31.1446372985 | 926 | 504990 | -100.36 | 1.11 | 68.21 | 0.02 | 1.27 | 1574 |
| 2024-09-20 22:21:37.786 | MS1 | 121.4656679477 | 31.1446197476 | 926 | 504990 | -107.63 | -1.80 | 85.39 | 0.13 | 1.33 | 1581 |
| 2024-09-20 22:21:38.313 | MS1 | 121.4656633596 | 31.1446299147 | 926 | 504990 | -105.50 | -0.82 | 24.87 | 0.10 | 1.25 | 1584 |
| 2024-09-20 22:21:39.412 | MS1 | 121.4656632242 | 31.1446312078 | 926 | 504990 | -100.10 | 0.27 | 53.87 | 0.17 | 1.09 | 1566 |
| 2024-09-20 22:21:40.949 | MS1 | 121.4656638588 | 31.1446350598 | 926 | 504990 | -88.42 | 15.24 | 563.17 | 0.06 | 2.78 | 1573 |
| 2024-09-20 22:21:41.238 | MS1 | 121.4656615522 | 31.1446271996 | 926 | 504990 | -91.05 | 13.71 | 457.47 | 0.03 | 2.50 | 1589 |
| 2024-09-20 22:21:42.276 | MS1 | 121.4656728997 | 31.1446324055 | 926 | 504990 | -87.16 | 16.91 | 447.57 | 0.09 | 2.81 | 1566 |

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
| 3220094 | 3 | 121.4641398346 | 31.1544798411 | 96 | 3 | 0 | 37.5 | TDD | 926 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3245560 | 4 | 121.4729964542 | 31.1511034337 | 336 | 11 | 7 | 38.5 | TDD | 847 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3266123 | 1 | 121.4674104092 | 31.1485866189 | 339 | 1 | 4 | 29.0 | TDD | 345 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3273258 | 2 | 121.4748787057 | 31.1474830254 | 247 | 1 | 6 | 34.4 | TDD | 874 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |

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
| 2024-09-20 22:21:30.883 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.908 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.014 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.014 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.218 | NREventA2 | measId:1;ServCellPCI:240;Se... |
| 2024-09-20 22:21:34.322 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3266123 | 1 | 11.1657 | 16.0349 | -116.5100 | 12.8855 | 104.9131 | 0.0073 | 0.0011 |
| 2024_09_20 22:00 | 3273258 | 2 | 6.3473 | 9.6581 | -117.0500 | 8.0290 | 93.6327 | 0.0022 | 0.0086 |
| 2024_09_20 22:00 | 3220094 | 3 | 11.9432 | 15.1110 | -116.8474 | 18.9003 | 175.8219 | 0.1748 | 0.0099 |
| 2024_09_20 22:00 | 3245560 | 4 | 9.2335 | 14.6650 | -116.6055 | 18.5000 | 100.6731 | 0.0155 | 0.0119 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416619_EF06CAE6 | 504990 | 926 | -104.5 | 504990 | 874 | -107.1 | 504990 | 345 | -114.4 | 504990 | 847 |
| MR_1774416619_982D9F57 | 504990 | 926 | -103.0 | 504990 | 874 | -105.9 | 504990 | 345 | -111.3 | 504990 | 847 |
| MR_1774416619_0D96B9F2 | 504990 | 926 | -105.3 | 504990 | 874 | -107.9 | 504990 | 345 | -114.3 | 504990 | 847 |
| MR_1774416619_919E1298 | 504990 | 926 | -105.3 | 504990 | 874 | -109.1 | 504990 | 345 | -114.7 | 504990 | 847 |
| MR_1774416619_987923B3 | 504990 | 926 | -105.4 | 504990 | 874 | -107.5 | 504990 | 345 | -111.9 | 504990 | 847 |
| MR_1774416619_CDE46B63 | 504990 | 926 | -106.1 | 504990 | 874 | -108.9 | 504990 | 345 | -113.3 | 504990 | 847 |
| MR_1774416619_123D7EF1 | 504990 | 926 | -104.9 | 504990 | 874 | -107.0 | 504990 | 345 | -113.5 | 504990 | 847 |
| MR_1774416619_B20C0C58 | 504990 | 926 | -106.7 | 504990 | 874 | -108.8 | 504990 | 345 | -114.6 | 504990 | 847 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1038: `eba4e047-db9...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `eba4e047-db96-49d6-b11b-80dae03bce19` |
| Tag | **multiple-answer** |
| 정답 | **C4|C12** |
| C4 의미 | Press down the tilt angle  of 3257657_2 by 4 degrees |
| C12 의미 | Decrease transmission power for 3257657_2 |
| 패턴 분류 | **P3 Overshoot (tilt)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1038] topology](images/train_1038.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3229992_4 by 3 degrees
- `C2`: Decrease A3 Offset threshold for 3257657_2
- `C3`: Lift the tilt angle  of 3257657_2 by 4 degrees
- `C4`: Press down the tilt angle  of 3257657_2 by 4 degrees **← 정답**
- `C5`: Check test server and transmission issues
- `C6`: Insufficient data; more data is needed for judgment.
- `C7`: Add neighbor relationship between 3268274_1 and 3257657_2
- `C8`: Increase transmission power for 3229992_4
- `C9`: Decrease transmission power for 3229992_4
- `C10`: Adjust the azimuth of 3229992_4 by 6 degrees
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3229992_4
- `C12`: Decrease transmission power for 3257657_2 **← 정답**
- `C13`: Decrease A3 Offset threshold for 3229992_4
- `C14`: Press down the tilt angle of 3229992_4 by 3 degrees
- `C15`: Add neighbor relationship between 3229992_4 and 3257657_2
- `C16`: Increase A3 Offset threshold for 3257657_2
- `C17`: Increase transmission power for 3257657_2
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3229992_4
- `C19`: Increase A3 Offset threshold for 3229992_4
- `C20`: Adjust the azimuth of 3257657_2 by 16 degrees
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3257657_2
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3257657_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.860 | MS1 | 121.4656709588 | 31.1446300777 | 558 | 504990 | -78.75 | 12.98 | 407.61 | 0.00 | 2.63 | 1585 |
| 2024-09-20 22:21:32.556 | MS1 | 121.4656755335 | 31.1446273081 | 558 | 504990 | -84.48 | 13.64 | 418.45 | 0.04 | 2.09 | 1577 |
| 2024-09-20 22:21:33.766 | MS1 | 121.4656759496 | 31.1446370805 | 558 | 504990 | -78.96 | 14.82 | 448.95 | 0.11 | 2.16 | 1582 |
| 2024-09-20 22:21:34.943 | MS1 | 121.4656641174 | 31.1446308826 | 558 | 504990 | -88.20 | 0.59 | 91.04 | 0.18 | 1.10 | 1568 |
| 2024-09-20 22:21:35.248 | MS1 | 121.4656706102 | 31.1446279137 | 558 | 504990 | -92.02 | 3.58 | 60.29 | 0.12 | 1.41 | 1600 |
| 2024-09-20 22:21:36.176 | MS1 | 121.4656587000 | 31.1446328455 | 558 | 504990 | -88.09 | 2.96 | 62.39 | 0.06 | 1.03 | 1582 |
| 2024-09-20 22:21:37.816 | MS1 | 121.4656685670 | 31.1446344140 | 558 | 504990 | -91.79 | 2.76 | 84.31 | 0.19 | 1.19 | 1564 |
| 2024-09-20 22:21:38.636 | MS1 | 121.4656634050 | 31.1446243064 | 558 | 504990 | -89.97 | 3.09 | 53.23 | 0.16 | 1.38 | 1572 |
| 2024-09-20 22:21:39.970 | MS1 | 121.4656673421 | 31.1446301277 | 558 | 504990 | -85.48 | 1.27 | 61.52 | 0.07 | 1.08 | 1580 |
| 2024-09-20 22:21:40.616 | MS1 | 121.4656769649 | 31.1446348313 | 558 | 504990 | -79.44 | 15.50 | 567.85 | 0.17 | 2.90 | 1580 |
| 2024-09-20 22:21:41.952 | MS1 | 121.4656588190 | 31.1446210654 | 558 | 504990 | -79.41 | 16.85 | 311.99 | 0.18 | 2.11 | 1563 |
| 2024-09-20 22:21:42.819 | MS1 | 121.4656605810 | 31.1446242216 | 558 | 504990 | -77.75 | 15.02 | 433.30 | 0.12 | 2.60 | 1564 |

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
| 3229992 | 4 | 121.4661813652 | 31.1530208961 | 189 | 2 | 9 | 15.0 | TDD | 558 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3235980 | 3 | 121.4656586025 | 31.1518356176 | 313 | 10 | 6 | 16.0 | TDD | 44 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3257657 | 2 | 121.4732267018 | 31.1546093860 | 197 | 3 | 0 | 27.9 | TDD | 835 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3268274 | 1 | 121.4665662071 | 31.1480683397 | 287 | 12 | 1 | 19.7 | TDD | 258 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |

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
| 2024-09-20 22:21:31.472 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.497 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.609 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.609 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3268274 | 1 | 9.3547 | 11.0547 | -115.9521 | 7.3144 | 186.4213 | 0.0099 | 0.0107 |
| 2024_09_20 22:00 | 3257657 | 2 | 19.4796 | 7.4376 | -115.2743 | 19.8260 | 102.3068 | 0.0150 | 0.0102 |
| 2024_09_20 22:00 | 3235980 | 3 | 9.2201 | 14.6548 | -116.7551 | 17.4927 | 137.1807 | 0.0099 | 0.0087 |
| 2024_09_20 22:00 | 3229992 | 4 | 6.0185 | 16.2215 | -108.4378 | 14.2231 | 189.6002 | 0.0058 | 0.0190 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417117_E3A87131 | 504990 | 558 | -87.3 | 504990 | 835 | -85.3 | 504990 | 258 | -87.9 | 504990 | 44 |
| MR_1774417117_E056C8DA | 504990 | 558 | -86.4 | 504990 | 835 | -82.5 | 504990 | 258 | -91.2 | 504990 | 44 |
| MR_1774417117_9588CEAA | 504990 | 558 | -87.1 | 504990 | 835 | -84.2 | 504990 | 258 | -90.1 | 504990 | 44 |
| MR_1774417117_04EAABE7 | 504990 | 558 | -87.0 | 504990 | 835 | -82.8 | 504990 | 258 | -87.8 | 504990 | 44 |
| MR_1774417117_6DAE013E | 504990 | 558 | -87.1 | 504990 | 835 | -84.9 | 504990 | 258 | -88.4 | 504990 | 44 |
| MR_1774417117_F4C16AFC | 504990 | 835 | -87.3 | 504990 | 558 | -82.4 | 504990 | 258 | -89.9 | 504990 | 44 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1039: `3ad16005-df4...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `3ad16005-df41-49cd-8822-282ec2fa2759` |
| Tag | **multiple-answer** |
| 정답 | **C18|C22** |
| C18 의미 | Increase transmission power for 3210191_1 |
| C22 의미 | Adjust the azimuth of 3210191_1 by 50 degrees |
| 패턴 분류 | **P4 Coverage (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1039] topology](images/train_1039.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3210191_1 by 9 degrees
- `C2`: Add neighbor relationship between 3262926_4 and 3210841_2
- `C3`: Add neighbor relationship between 3210191_1 and 3210841_2
- `C4`: Adjust the azimuth of 3210841_2 by 3 degrees
- `C5`: Lift the tilt angle  of 3210841_2 by 3 degrees
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3210191_1
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3210191_1
- `C8`: Increase transmission power for 3210841_2
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3210841_2
- `C10`: Decrease A3 Offset threshold for 3210841_2
- `C11`: Decrease A3 Offset threshold for 3210191_1
- `C12`: Increase A3 Offset threshold for 3210841_2
- `C13`: Increase A3 Offset threshold for 3210191_1
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3210841_2
- `C15`: Decrease transmission power for 3210191_1
- `C16`: Check test server and transmission issues
- `C17`: Press down the tilt angle of 3210191_1 by 9 degrees
- `C18`: Increase transmission power for 3210191_1 **← 정답**
- `C19`: Insufficient data; more data is needed for judgment.
- `C20`: Decrease transmission power for 3210841_2
- `C21`: Press down the tilt angle  of 3210841_2 by 3 degrees
- `C22`: Adjust the azimuth of 3210191_1 by 50 degrees **← 정답**

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.945 | MS1 | 121.4656587803 | 31.1446288128 | 472 | 504990 | -87.56 | 14.50 | 519.71 | 0.16 | 2.61 | 1560 |
| 2024-09-20 22:21:32.356 | MS1 | 121.4656599785 | 31.1446333696 | 472 | 504990 | -91.79 | 12.18 | 332.43 | 0.12 | 2.44 | 1596 |
| 2024-09-20 22:21:33.648 | MS1 | 121.4656625213 | 31.1446373504 | 472 | 504990 | -93.97 | 16.46 | 402.85 | 0.11 | 2.24 | 1592 |
| 2024-09-20 22:21:34.241 | MS1 | 121.4656683919 | 31.1446355094 | 472 | 504990 | -101.45 | 1.69 | 18.65 | 0.01 | 1.38 | 1572 |
| 2024-09-20 22:21:35.475 | MS1 | 121.4656757285 | 31.1446290881 | 472 | 504990 | -101.33 | 0.49 | 76.33 | 0.07 | 1.19 | 1597 |
| 2024-09-20 22:21:36.351 | MS1 | 121.4656716933 | 31.1446257573 | 472 | 504990 | -108.47 | 0.13 | 65.02 | 0.17 | 1.36 | 1588 |
| 2024-09-20 22:21:37.585 | MS1 | 121.4656673199 | 31.1446301227 | 472 | 504990 | -105.73 | 1.48 | 72.60 | 0.13 | 1.03 | 1576 |
| 2024-09-20 22:21:38.293 | MS1 | 121.4656582908 | 31.1446274005 | 472 | 504990 | -103.53 | 1.02 | 26.92 | 0.12 | 1.49 | 1582 |
| 2024-09-20 22:21:39.495 | MS1 | 121.4656757318 | 31.1446357257 | 472 | 504990 | -109.44 | 1.53 | 23.04 | 0.14 | 1.42 | 1579 |
| 2024-09-20 22:21:40.495 | MS1 | 121.4656732250 | 31.1446300519 | 472 | 504990 | -89.94 | 12.26 | 582.59 | 0.15 | 2.21 | 1565 |
| 2024-09-20 22:21:41.704 | MS1 | 121.4656741930 | 31.1446190888 | 472 | 504990 | -85.25 | 12.16 | 440.57 | 0.13 | 2.13 | 1572 |
| 2024-09-20 22:21:42.594 | MS1 | 121.4656689175 | 31.1446254003 | 472 | 504990 | -90.36 | 15.56 | 541.47 | 0.05 | 2.01 | 1576 |

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
| 3210191 | 1 | 121.4755513656 | 31.1477371913 | 199 | 6 | 5 | 46.3 | TDD | 472 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3210841 | 2 | 121.4663406330 | 31.1554844656 | 186 | 1 | 5 | 44.0 | TDD | 8 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3214593 | 3 | 121.4736843794 | 31.1459748864 | 208 | 2 | 12 | 44.3 | TDD | 837 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3262926 | 4 | 121.4658539211 | 31.1447563944 | 155 | 4 | 4 | 23.4 | TDD | 553 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:31.564 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.580 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.688 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.688 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.884 | NREventA2 | measId:1;ServCellPCI:578;Se... |
| 2024-09-20 22:21:34.994 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3210191 | 1 | 11.2825 | 17.9009 | -115.6325 | 17.5207 | 92.4296 | 0.1595 | 0.0167 |
| 2024_09_20 22:00 | 3210841 | 2 | 8.2207 | 18.5518 | -114.3238 | 17.6550 | 86.5055 | 0.0018 | 0.0012 |
| 2024_09_20 22:00 | 3214593 | 3 | 15.2335 | 11.3007 | -117.7345 | 13.6944 | 81.8943 | 0.0070 | 0.0169 |
| 2024_09_20 22:00 | 3262926 | 4 | 17.6022 | 19.4331 | -117.9441 | 9.8782 | 118.8002 | 0.0088 | 0.0052 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413727_53F2F204 | 504990 | 472 | -100.0 | 504990 | 8 | -108.4 | 504990 | 553 | -112.2 | 504990 | 837 |
| MR_1774413727_74EC7ACB | 504990 | 472 | -102.8 | 504990 | 8 | -107.2 | 504990 | 553 | -112.7 | 504990 | 837 |
| MR_1774413727_534F05A4 | 504990 | 472 | -102.6 | 504990 | 8 | -105.8 | 504990 | 553 | -113.2 | 504990 | 837 |
| MR_1774413727_1E1E8A65 | 504990 | 472 | -102.7 | 504990 | 8 | -109.4 | 504990 | 553 | -113.6 | 504990 | 837 |
| MR_1774413727_D7DD81B2 | 504990 | 472 | -101.0 | 504990 | 8 | -106.6 | 504990 | 553 | -113.3 | 504990 | 837 |
| MR_1774413727_F0B5BFF7 | 504990 | 472 | -101.6 | 504990 | 8 | -108.9 | 504990 | 553 | -113.9 | 504990 | 837 |
| MR_1774413727_66F671DD | 504990 | 472 | -100.1 | 504990 | 8 | -108.5 | 504990 | 553 | -111.1 | 504990 | 837 |
| MR_1774413727_53A9D53B | 504990 | 472 | -103.0 | 504990 | 8 | -106.8 | 504990 | 553 | -111.6 | 504990 | 837 |

> *... 2개 열 생략 (전체 14열)*

---
