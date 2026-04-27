# Track A 문제 분석 — train[1020]~train[1029]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[1020] ~ train[1029] (10개)

## 목차

1. [문제 1020: `692d8e85-9a0...`](#1020) — single-answer, 정답: C1
2. [문제 1021: `6f49e863-87b...`](#1021) — single-answer, 정답: C22
3. [문제 1022: `e9bc0950-eb6...`](#1022) — single-answer, 정답: C13
4. [문제 1023: `f9b63445-b76...`](#1023) — single-answer, 정답: C14
5. [문제 1024: `c8d019d7-bf4...`](#1024) — single-answer, 정답: C6
6. [문제 1025: `63af2b29-bf7...`](#1025) — single-answer, 정답: C2
7. [문제 1026: `f0325075-a12...`](#1026) — multiple-answer, 정답: C2|C6|C11|C14
8. [문제 1027: `a3aab5e6-5b8...`](#1027) — single-answer, 정답: C16
9. [문제 1028: `6bfe2a67-57f...`](#1028) — single-answer, 정답: C6
10. [문제 1029: `5ac230d6-1eb...`](#1029) — single-answer, 정답: C16

---

### 문제 1020: `692d8e85-9a0...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `692d8e85-9a0c-4d49-a207-3ab3b63b5279` |
| Tag | **single-answer** |
| 정답 | **C1** |
| C1 의미 | Lift the tilt angle  of 3219398_4 by 7 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1020] topology](images/train_1020.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle  of 3219398_4 by 7 degrees **← 정답**
- `C2`: Decrease A3 Offset threshold for 3236103_3
- `C3`: Check test server and transmission issues
- `C4`: Increase A3 Offset threshold for 3236103_3
- `C5`: Adjust the azimuth of 3274540_2 by 16 degrees
- `C6`: Increase transmission power for 3274540_2
- `C7`: Add neighbor relationship between 3274540_2 and 3236103_3
- `C8`: Increase A3 Offset threshold for 3274540_2
- `C9`: Decrease A3 Offset threshold for 3274540_2
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3236103_3
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3274540_2
- `C12`: Adjust the azimuth of 3219398_4 by 29 degrees
- `C13`: Increase transmission power for 3236103_3
- `C14`: Add neighbor relationship between 3219398_4 and 3236103_3
- `C15`: Press down the tilt angle of 3274540_2 by 6 degrees
- `C16`: Insufficient data; more data is needed for judgment.
- `C17`: Decrease transmission power for 3274540_2
- `C18`: Decrease transmission power for 3236103_3
- `C19`: Press down the tilt angle  of 3219398_4 by 7 degrees
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3236103_3
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3274540_2
- `C22`: Lift the tilt angle of 3274540_2 by 6 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.164 | MS1 | 121.4656621417 | 31.1446291745 | 92 | 504990 | -90.59 | 17.39 | 555.03 | 0.12 | 2.87 | 1584 |
| 2024-09-20 22:21:32.512 | MS1 | 121.4656675491 | 31.1446307917 | 92 | 504990 | -90.10 | 12.59 | 490.22 | 0.04 | 2.74 | 1585 |
| 2024-09-20 22:21:33.293 | MS1 | 121.4656662635 | 31.1446259460 | 92 | 504990 | -90.82 | 14.98 | 446.98 | 0.06 | 2.14 | 1563 |
| 2024-09-20 22:21:34.289 | MS1 | 121.4656703784 | 31.1446279472 | 92 | 504990 | -85.94 | 13.47 | 103.35 | 0.14 | 2.07 | 1573 |
| 2024-09-20 22:21:35.612 | MS1 | 121.4656720319 | 31.1446239806 | 92 | 504990 | -87.61 | 16.93 | 95.09 | 0.04 | 2.14 | 1575 |
| 2024-09-20 22:21:36.520 | MS1 | 121.4656761565 | 31.1446266173 | 92 | 504990 | -85.75 | 17.77 | 82.82 | 0.19 | 2.59 | 1579 |
| 2024-09-20 22:21:37.806 | MS1 | 121.4656633399 | 31.1446207036 | 92 | 504990 | -91.58 | 7.86 | 100.37 | 0.17 | 2.66 | 1561 |
| 2024-09-20 22:21:38.442 | MS1 | 121.4656661488 | 31.1446335390 | 92 | 504990 | -89.95 | 10.46 | 69.85 | 0.18 | 2.91 | 1584 |
| 2024-09-20 22:21:39.223 | MS1 | 121.4656592104 | 31.1446350646 | 92 | 504990 | -91.44 | 10.42 | 103.38 | 0.05 | 2.75 | 1575 |
| 2024-09-20 22:21:40.378 | MS1 | 121.4656742768 | 31.1446220269 | 92 | 504990 | -89.97 | 9.29 | 472.36 | 0.19 | 2.31 | 1561 |
| 2024-09-20 22:21:41.494 | MS1 | 121.4656761600 | 31.1446367326 | 92 | 504990 | -91.03 | 12.25 | 558.33 | 0.13 | 2.12 | 1581 |
| 2024-09-20 22:21:42.408 | MS1 | 121.4656713280 | 31.1446314680 | 92 | 504990 | -90.74 | 9.12 | 349.91 | 0.06 | 2.27 | 1589 |

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
| 3219398 | 4 | 121.4647601234 | 31.1487047720 | 53 | 1 | 9 | 49.4 | TDD | 599 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3236103 | 3 | 121.4649594154 | 31.1508056761 | 203 | 3 | 0 | 42.4 | TDD | 582 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3248269 | 1 | 121.4723339166 | 31.1484525916 | 113 | 14 | 5 | 17.3 | TDD | 560 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3274540 | 2 | 121.4747857520 | 31.1552542997 | 200 | 5 | 8 | 15.5 | TDD | 92 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:30.902 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.041 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.041 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.695 | NREventA3 | measId:2;ServCellPCI:118;Se... |
| 2024-09-20 22:21:37.935 | NRHandoverAttempt | SourcePCI:118;SourceNR-ARFC... |
| 2024-09-20 22:21:37.985 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.998 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.105 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.105 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3248269 | 1 | 11.0661 | 12.3675 | -115.7616 | 13.6857 | 184.0800 | 0.0171 | 0.0026 |
| 2024_09_20 22:00 | 3274540 | 2 | 90.4051 | 76.1188 | -114.5954 | 7.9920 | 113.3868 | 0.0137 | 0.0122 |
| 2024_09_20 22:00 | 3236103 | 3 | 16.3885 | 12.4352 | -117.0366 | 18.7137 | 104.2118 | 0.0121 | 0.0036 |
| 2024_09_20 22:00 | 3219398 | 4 | 5.6478 | 16.7983 | -115.7500 | 10.1918 | 84.2053 | 0.0165 | 0.0007 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413870_A2F644D5 | 504990 | 92 | -88.4 | 504990 | 582 | -93.7 | 504990 | 599 | -94.7 | 504990 | 560 |
| MR_1774413870_D99FFC2A | 504990 | 92 | -88.1 | 504990 | 582 | -94.8 | 504990 | 599 | -96.4 | 504990 | 560 |
| MR_1774413870_41D6EAF7 | 504990 | 92 | -89.3 | 504990 | 582 | -92.5 | 504990 | 599 | -94.5 | 504990 | 560 |
| MR_1774413870_A8A126A1 | 504990 | 92 | -86.0 | 504990 | 582 | -94.0 | 504990 | 599 | -97.3 | 504990 | 560 |
| MR_1774413870_8A6FAFA3 | 504990 | 92 | -88.9 | 504990 | 582 | -93.8 | 504990 | 599 | -96.9 | 504990 | 560 |
| MR_1774413870_6F76B328 | 504990 | 92 | -89.0 | 504990 | 582 | -95.4 | 504990 | 599 | -95.4 | 504990 | 560 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1021: `6f49e863-87b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `6f49e863-87bf-4b1c-8ef1-2c0ea55c3b6c` |
| Tag | **single-answer** |
| 정답 | **C22** |
| C22 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3269122_2 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1021] topology](images/train_1021.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3269122_2 and 3237856_1
- `C2`: Increase A3 Offset threshold for 3269122_2
- `C3`: Decrease A3 Offset threshold for 3269122_2
- `C4`: Press down the tilt angle of 3269122_2 by 2 degrees
- `C5`: Check test server and transmission issues
- `C6`: Lift the tilt angle of 3269122_2 by 2 degrees
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3237856_1
- `C8`: Adjust the azimuth of 3269122_2 by 30 degrees
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3237856_1
- `C10`: Increase transmission power for 3237856_1
- `C11`: Decrease A3 Offset threshold for 3237856_1
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3269122_2
- `C13`: Insufficient data; more data is needed for judgment.
- `C14`: Increase A3 Offset threshold for 3237856_1
- `C15`: Increase transmission power for 3269122_2
- `C16`: Adjust the azimuth of 3237856_1 by 30 degrees
- `C17`: Add neighbor relationship between 3250436_9 and 3237856_1
- `C18`: Press down the tilt angle  of 3237856_1 by 2 degrees
- `C19`: Decrease transmission power for 3269122_2
- `C20`: Lift the tilt angle  of 3237856_1 by 2 degrees
- `C21`: Decrease transmission power for 3237856_1
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3269122_2 **← 정답**

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.340 | MS1 | 121.4656734373 | 31.1446341629 | 936 | 504990 | -95.31 | 10.28 | 322.80 | 0.01 | 2.60 | 1565 |
| 2024-09-20 22:21:32.286 | MS1 | 121.4656739223 | 31.1446302560 | 72 | 504990 | -94.76 | 14.45 | 530.12 | 0.01 | 2.61 | 1585 |
| 2024-09-20 22:21:33.897 | MS1 | 121.4656773158 | 31.1446217517 | 564 | 504990 | -94.06 | 9.55 | 516.79 | 0.09 | 2.04 | 1580 |
| 2024-09-20 22:21:34.820 | MS1 | 121.4656638246 | 31.1446237516 | 752 | 152650 | -92.88 | 2.12 | 90.38 | 0.06 | 1.97 | 955 |
| 2024-09-20 22:21:35.910 | MS1 | 121.4656738124 | 31.1446288905 | 724 | 152650 | -89.71 | 2.97 | 84.05 | 0.20 | 1.50 | 923 |
| 2024-09-20 22:21:36.835 | MS1 | 121.4656637799 | 31.1446329635 | 584 | 152650 | -93.63 | 2.06 | 64.25 | 0.18 | 1.83 | 901 |
| 2024-09-20 22:21:37.297 | MS1 | 121.4656593266 | 31.1446235795 | 155 | 152650 | -95.11 | 6.30 | 67.06 | 0.13 | 1.63 | 909 |
| 2024-09-20 22:21:38.649 | MS1 | 121.4656658755 | 31.1446316321 | 752 | 152650 | -88.76 | 5.31 | 83.80 | 0.08 | 1.91 | 940 |
| 2024-09-20 22:21:39.937 | MS1 | 121.4656649762 | 31.1446210534 | 724 | 152650 | -92.95 | 6.37 | 77.28 | 0.18 | 1.73 | 967 |
| 2024-09-20 22:21:40.996 | MS1 | 121.4656771525 | 31.1446249843 | 584 | 152650 | -87.51 | 6.82 | 88.49 | 0.08 | 2.84 | 1577 |
| 2024-09-20 22:21:41.807 | MS1 | 121.4656636257 | 31.1446328821 | 155 | 152650 | -96.00 | 3.75 | 52.41 | 0.16 | 2.54 | 1590 |
| 2024-09-20 22:21:42.530 | MS1 | 121.4656625730 | 31.1446229297 | 752 | 152650 | -88.44 | 7.88 | 64.19 | 0.11 | 2.66 | 1575 |

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
| 3210652 | 5 | 121.4756644464 | 31.1483909975 | 300 | 3 | 1 | 13.5 | TDD | 564 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3212794 | 12 | 121.4666739894 | 31.1547740698 | 57 | 5 | 1 | 9.1 | FDD | 533 | n1 | 152650 | 30M | 4T4R | 14 | 152650 |
| 3215753 | 3 | 121.4749504854 | 31.1440100101 | 131 | 8 | 3 | 12.2 | TDD | 72 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3225261 | 6 | 121.4661536029 | 31.1537885731 | 273 | 14 | 9 | 29.9 | TDD | 411 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3228943 | 8 | 121.4683984690 | 31.1495964479 | 27 | 14 | 8 | 4.5 | FDD | 390 | n1 | 152650 | 30M | 4T4R | 13 | 152650 |
| 3231335 | 13 | 121.4642824433 | 31.1466176112 | 235 | 5 | 10 | 17.9 | FDD | 155 | n1 | 152650 | 30M | 4T4R | 28 | 152650 |
| 3237856 | 1 | 121.4731726144 | 31.1454071077 | 293 | 1 | 0 | 10.8 | TDD | 997 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3238501 | 11 | 121.4719073609 | 31.1547599771 | 283 | 12 | 10 | 20.5 | FDD | 724 | n1 | 152650 | 30M | 4T4R | 10 | 152650 |
| 3247443 | 10 | 121.4729888710 | 31.1524929027 | 130 | 2 | 3 | 11.8 | FDD | 752 | n1 | 152650 | 30M | 4T4R | 21 | 152650 |
| 3250436 | 9 | 121.4684530232 | 31.1528744087 | 90 | 4 | 9 | 11.7 | FDD | 584 | n1 | 152650 | 30M | 4T4R | 15 | 152650 |
| 3253955 | 7 | 121.4675208169 | 31.1462873030 | 31 | 10 | 2 | 25.3 | FDD | 646 | n1 | 152650 | 30M | 4T4R | 27 | 152650 |
| 3255758 | 4 | 121.4648167968 | 31.1446312661 | 39 | 4 | 7 | 17.3 | TDD | 624 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3269122 | 2 | 121.4748167786 | 31.1529589880 | 193 | 1 | 3 | 25.8 | TDD | 936 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |

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
| 2024-09-20 22:21:31.504 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.528 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.675 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.675 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.357 | NREventA2 | measId:1;ServCellPCI:289;Se... |
| 2024-09-20 22:21:35.500 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.704 | NREventA5 | measId:3;ServCellPCI:289;Se... |
| 2024-09-20 22:21:35.757 | NRHandoverAttempt | SourcePCI:289;SourceNR-ARFC... |
| 2024-09-20 22:21:35.799 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.812 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:35.928 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.928 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3237856 | 1 | 10.1424 | 8.1443 | -117.4620 | 6.2522 | 91.1897 | 0.0188 | 0.0095 |
| 2024_09_20 22:00 | 3269122 | 2 | 17.6253 | 19.3270 | -115.6496 | 9.6102 | 177.3165 | 0.0003 | 0.0200 |
| 2024_09_20 22:00 | 3215753 | 3 | 8.9690 | 18.0631 | -117.3715 | 9.9366 | 141.7514 | 0.0111 | 0.0061 |
| 2024_09_20 22:00 | 3255758 | 4 | 16.7403 | 10.3743 | -117.4533 | 16.2528 | 101.7955 | 0.0032 | 0.0078 |
| 2024_09_20 22:00 | 3210652 | 5 | 19.2500 | 12.7014 | -117.7330 | 8.4696 | 91.0698 | 0.0082 | 0.0073 |
| 2024_09_20 22:00 | 3225261 | 6 | 19.5041 | 7.3321 | -117.5954 | 13.6505 | 183.4159 | 0.0131 | 0.0178 |
| 2024_09_20 22:00 | 3253955 | 7 | 6.8844 | 12.1352 | -115.7064 | 4.8767 | 30.6626 | 0.0093 | 0.0114 |
| 2024_09_20 22:00 | 3228943 | 8 | 16.7175 | 10.6175 | -116.1778 | 4.4488 | 59.8788 | 0.0179 | 0.0159 |
| 2024_09_20 22:00 | 3250436 | 9 | 9.2675 | 5.7634 | -114.7699 | 3.1802 | 37.6048 | 0.0002 | 0.0112 |
| 2024_09_20 22:00 | 3247443 | 10 | 5.8425 | 8.1009 | -115.3821 | 4.4727 | 41.1397 | 0.0171 | 0.0161 |
| 2024_09_20 22:00 | 3238501 | 11 | 18.8631 | 6.3672 | -117.2761 | 4.3289 | 24.4762 | 0.0085 | 0.0085 |
| 2024_09_20 22:00 | 3212794 | 12 | 16.7436 | 10.0210 | -114.8072 | 4.3189 | 36.4959 | 0.0125 | 0.0169 |
| 2024_09_20 22:00 | 3231335 | 13 | 6.8122 | 5.1067 | -114.2392 | 3.7923 | 25.9768 | 0.0039 | 0.0037 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416850_453CDA21 | 504990 | 564 | -92.1 | 504990 | 997 | -88.3 | 504990 | 624 | -98.7 | 504990 | 411 |
| MR_1774416850_035B3876 | 152650 | 752 | -94.3 | 152650 | 646 | -98.4 | 152650 | 390 | -101.9 | 152650 | 533 |
| MR_1774416850_B6B637D0 | 152650 | 752 | -91.0 | 152650 | 646 | -98.2 | 152650 | 390 | -103.0 | 152650 | 533 |
| MR_1774416850_A0A1C5C5 | 504990 | 564 | -93.2 | 504990 | 997 | -87.9 | 504990 | 624 | -100.7 | 504990 | 411 |
| MR_1774416850_7C37FC1D | 504990 | 564 | -94.4 | 504990 | 997 | -89.9 | 504990 | 624 | -99.0 | 504990 | 411 |
| MR_1774416850_AF5D9084 | 152650 | 752 | -91.6 | 152650 | 646 | -97.9 | 152650 | 390 | -104.9 | 152650 | 533 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1022: `e9bc0950-eb6...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `e9bc0950-eb6a-4812-9fdb-297cc80abd50` |
| Tag | **single-answer** |
| 정답 | **C13** |
| C13 의미 | Lift the tilt angle  of 3263037_4 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1022] topology](images/train_1022.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3246008_1 by 6 degrees
- `C2`: Decrease A3 Offset threshold for 3210847_3
- `C3`: Decrease A3 Offset threshold for 3246008_1
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3246008_1
- `C5`: Increase transmission power for 3210847_3
- `C6`: Add neighbor relationship between 3246008_1 and 3210847_3
- `C7`: Adjust the azimuth of 3246008_1 by 32 degrees
- `C8`: Check test server and transmission issues
- `C9`: Add neighbor relationship between 3263037_4 and 3210847_3
- `C10`: Decrease transmission power for 3210847_3
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3246008_1
- `C12`: Lift the tilt angle of 3246008_1 by 6 degrees
- `C13`: Lift the tilt angle  of 3263037_4 by 10 degrees **← 정답**
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Decrease transmission power for 3246008_1
- `C16`: Increase transmission power for 3246008_1
- `C17`: Increase A3 Offset threshold for 3246008_1
- `C18`: Adjust the azimuth of 3263037_4 by 50 degrees
- `C19`: Increase A3 Offset threshold for 3210847_3
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3210847_3
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3210847_3
- `C22`: Press down the tilt angle  of 3263037_4 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.430 | MS1 | 121.4656662724 | 31.1446374604 | 704 | 504990 | -87.41 | 17.13 | 428.68 | 0.19 | 2.32 | 1568 |
| 2024-09-20 22:21:32.740 | MS1 | 121.4656713892 | 31.1446205317 | 704 | 504990 | -87.54 | 13.38 | 354.75 | 0.19 | 2.32 | 1599 |
| 2024-09-20 22:21:33.172 | MS1 | 121.4656715420 | 31.1446260725 | 704 | 504990 | -91.59 | 13.58 | 480.31 | 0.02 | 2.43 | 1565 |
| 2024-09-20 22:21:34.771 | MS1 | 121.4656659810 | 31.1446249283 | 704 | 504990 | -87.45 | 12.24 | 52.00 | 0.11 | 2.77 | 1592 |
| 2024-09-20 22:21:35.730 | MS1 | 121.4656665833 | 31.1446311464 | 704 | 504990 | -88.16 | 12.57 | 75.47 | 0.15 | 2.96 | 1571 |
| 2024-09-20 22:21:36.682 | MS1 | 121.4656754352 | 31.1446273871 | 704 | 504990 | -89.59 | 17.35 | 61.86 | 0.01 | 2.74 | 1574 |
| 2024-09-20 22:21:37.402 | MS1 | 121.4656680372 | 31.1446304271 | 704 | 504990 | -89.46 | 9.24 | 92.92 | 0.08 | 2.14 | 1580 |
| 2024-09-20 22:21:38.426 | MS1 | 121.4656749850 | 31.1446271451 | 704 | 504990 | -90.14 | 8.96 | 87.35 | 0.15 | 2.73 | 1579 |
| 2024-09-20 22:21:39.428 | MS1 | 121.4656629456 | 31.1446235368 | 704 | 504990 | -93.65 | 10.21 | 65.51 | 0.08 | 2.31 | 1594 |
| 2024-09-20 22:21:40.332 | MS1 | 121.4656712467 | 31.1446351151 | 704 | 504990 | -89.59 | 9.14 | 590.48 | 0.18 | 2.42 | 1600 |
| 2024-09-20 22:21:41.444 | MS1 | 121.4656638694 | 31.1446247834 | 704 | 504990 | -90.02 | 12.98 | 373.38 | 0.06 | 2.22 | 1582 |
| 2024-09-20 22:21:42.959 | MS1 | 121.4656708298 | 31.1446285745 | 704 | 504990 | -92.12 | 12.20 | 433.24 | 0.01 | 2.57 | 1568 |

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
| 3210847 | 3 | 121.4664956226 | 31.1487007061 | 137 | 14 | 9 | 17.4 | TDD | 916 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3246008 | 1 | 121.4755716453 | 31.1457205058 | 231 | 4 | 8 | 30.6 | TDD | 704 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3263037 | 4 | 121.4657949944 | 31.1508890197 | 352 | 7 | 11 | 44.0 | TDD | 719 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3269473 | 2 | 121.4753946907 | 31.1478356830 | 161 | 3 | 2 | 28.8 | TDD | 322 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |

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
| 2024-09-20 22:21:30.963 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.983 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.095 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.095 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.804 | NREventA3 | measId:2;ServCellPCI:482;Se... |
| 2024-09-20 22:21:38.044 | NRHandoverAttempt | SourcePCI:482;SourceNR-ARFC... |
| 2024-09-20 22:21:38.082 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.095 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.229 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.229 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3246008 | 1 | 85.6122 | 88.2040 | -117.2606 | 9.1471 | 138.7788 | 0.0168 | 0.0170 |
| 2024_09_20 22:00 | 3269473 | 2 | 18.9903 | 19.5405 | -116.2363 | 15.5090 | 136.7149 | 0.0088 | 0.0057 |
| 2024_09_20 22:00 | 3210847 | 3 | 13.4306 | 16.2625 | -115.9834 | 14.6515 | 142.4115 | 0.0126 | 0.0031 |
| 2024_09_20 22:00 | 3263037 | 4 | 10.8465 | 13.6009 | -117.4656 | 7.8119 | 158.8093 | 0.0137 | 0.0148 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413700_642CAED9 | 504990 | 704 | -89.1 | 504990 | 916 | -96.7 | 504990 | 719 | -101.8 | 504990 | 322 |
| MR_1774413700_111FF493 | 504990 | 704 | -88.9 | 504990 | 916 | -96.3 | 504990 | 719 | -98.9 | 504990 | 322 |
| MR_1774413700_5592A692 | 504990 | 704 | -85.5 | 504990 | 916 | -93.8 | 504990 | 719 | -99.2 | 504990 | 322 |
| MR_1774413700_359E3624 | 504990 | 704 | -87.4 | 504990 | 916 | -94.1 | 504990 | 719 | -98.2 | 504990 | 322 |
| MR_1774413700_FD6391EF | 504990 | 704 | -86.1 | 504990 | 916 | -97.3 | 504990 | 719 | -101.4 | 504990 | 322 |
| MR_1774413700_60DC57D5 | 504990 | 704 | -86.1 | 504990 | 916 | -95.1 | 504990 | 719 | -98.0 | 504990 | 322 |
| MR_1774413700_9C7410E9 | 504990 | 704 | -87.1 | 504990 | 916 | -94.4 | 504990 | 719 | -99.1 | 504990 | 322 |
| MR_1774413700_65C4BB61 | 504990 | 704 | -87.8 | 504990 | 916 | -93.8 | 504990 | 719 | -98.1 | 504990 | 322 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1023: `f9b63445-b76...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `f9b63445-b762-4ebf-ad29-024a7c1f0d51` |
| Tag | **single-answer** |
| 정답 | **C14** |
| C14 의미 | Decrease A3 Offset threshold for 3239579_4 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1023] topology](images/train_1023.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3256255_1
- `C2`: Increase transmission power for 3239579_4
- `C3`: Decrease A3 Offset threshold for 3256255_1
- `C4`: Lift the tilt angle  of 3256255_1 by 10 degrees
- `C5`: Check test server and transmission issues
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3256255_1
- `C7`: Add neighbor relationship between 3240219_3 and 3256255_1
- `C8`: Increase transmission power for 3256255_1
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3256255_1
- `C10`: Lift the tilt angle of 3239579_4 by 10 degrees
- `C11`: Add neighbor relationship between 3239579_4 and 3256255_1
- `C12`: Increase A3 Offset threshold for 3239579_4
- `C13`: Adjust the azimuth of 3239579_4 by 50 degrees
- `C14`: Decrease A3 Offset threshold for 3239579_4 **← 정답**
- `C15`: Decrease transmission power for 3239579_4
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3239579_4
- `C17`: Adjust the azimuth of 3256255_1 by 50 degrees
- `C18`: Press down the tilt angle of 3239579_4 by 10 degrees
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3239579_4
- `C20`: Insufficient data; more data is needed for judgment.
- `C21`: Decrease transmission power for 3256255_1
- `C22`: Press down the tilt angle  of 3256255_1 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.222 | MS1 | 121.4656750145 | 31.1446185833 | 244 | 504990 | -77.77 | 15.54 | 538.66 | 0.11 | 2.27 | 1600 |
| 2024-09-20 22:21:32.239 | MS1 | 121.4656732645 | 31.1446300738 | 244 | 504990 | -77.11 | 16.05 | 444.95 | 0.15 | 2.05 | 1600 |
| 2024-09-20 22:21:33.763 | MS1 | 121.4656706156 | 31.1446340523 | 244 | 504990 | -80.73 | 12.90 | 585.38 | 0.19 | 2.54 | 1575 |
| 2024-09-20 22:21:34.652 | MS1 | 121.4656650255 | 31.1446271198 | 244 | 504990 | -83.87 | -3.33 | 42.41 | 0.15 | 1.04 | 1588 |
| 2024-09-20 22:21:35.695 | MS1 | 121.4656694143 | 31.1446350087 | 244 | 504990 | -84.46 | -2.48 | 51.71 | 0.08 | 1.19 | 1565 |
| 2024-09-20 22:21:36.346 | MS1 | 121.4656745193 | 31.1446215602 | 244 | 504990 | -90.34 | -2.95 | 43.67 | 0.12 | 1.47 | 1589 |
| 2024-09-20 22:21:37.357 | MS1 | 121.4656761277 | 31.1446298712 | 244 | 504990 | -83.21 | -1.59 | 38.22 | 0.03 | 1.19 | 1595 |
| 2024-09-20 22:21:38.755 | MS1 | 121.4656710720 | 31.1446309937 | 244 | 504990 | -89.76 | -3.33 | 25.91 | 0.03 | 1.10 | 1600 |
| 2024-09-20 22:21:39.531 | MS1 | 121.4656635810 | 31.1446379544 | 616 | 504990 | -80.46 | 13.25 | 272.17 | 0.09 | 1.06 | 1572 |
| 2024-09-20 22:21:40.567 | MS1 | 121.4656729481 | 31.1446364361 | 616 | 504990 | -77.08 | 16.28 | 453.36 | 0.01 | 2.17 | 1587 |
| 2024-09-20 22:21:41.688 | MS1 | 121.4656735669 | 31.1446320763 | 616 | 504990 | -75.50 | 12.67 | 319.82 | 0.16 | 2.88 | 1562 |
| 2024-09-20 22:21:42.268 | MS1 | 121.4656606728 | 31.1446353049 | 616 | 504990 | -82.41 | 17.77 | 553.00 | 0.11 | 2.82 | 1562 |

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
| 3239579 | 4 | 121.4680112003 | 31.1444929034 | 122 | 2 | 0 | 40.9 | TDD | 244 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3240219 | 3 | 121.4666860159 | 31.1555663981 | 170 | 1 | 10 | 24.5 | TDD | 643 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3252811 | 2 | 121.4688162319 | 31.1468898867 | 149 | 1 | 7 | 16.9 | TDD | 410 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3256255 | 1 | 121.4641831358 | 31.1502552832 | 309 | 10 | 0 | 29.5 | TDD | 616 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |

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
| 2024-09-20 22:21:30.830 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.845 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:30.976 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.976 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.730 | NREventA3 | measId:2;ServCellPCI:101;Se... |
| 2024-09-20 22:21:37.970 | NRHandoverAttempt | SourcePCI:101;SourceNR-ARFC... |
| 2024-09-20 22:21:38.006 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.020 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.124 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.124 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3256255 | 1 | 18.7734 | 5.1363 | -115.6384 | 19.5323 | 188.3896 | 0.0066 | 0.0151 |
| 2024_09_20 22:00 | 3252811 | 2 | 14.0625 | 12.9292 | -117.8669 | 17.7307 | 119.4617 | 0.0051 | 0.0160 |
| 2024_09_20 22:00 | 3240219 | 3 | 5.1461 | 6.8263 | -116.2608 | 10.1411 | 161.5820 | 0.0128 | 0.0038 |
| 2024_09_20 22:00 | 3239579 | 4 | 13.2912 | 9.7668 | -115.1903 | 13.9410 | 104.8354 | 0.0197 | 0.1131 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416425_BB6A3C7C | 504990 | 244 | -82.6 | 504990 | 616 | -77.5 | 504990 | 643 | -83.6 | 504990 | 410 |
| MR_1774416425_FD51E107 | 504990 | 244 | -83.2 | 504990 | 616 | -79.8 | 504990 | 643 | -86.3 | 504990 | 410 |
| MR_1774416425_D7E02EB3 | 504990 | 244 | -83.8 | 504990 | 616 | -77.1 | 504990 | 643 | -84.3 | 504990 | 410 |
| MR_1774416425_B6ACA94F | 504990 | 616 | -80.6 | 504990 | 244 | -84.8 | 504990 | 643 | -82.8 | 504990 | 410 |
| MR_1774416425_9AA0C993 | 504990 | 244 | -85.1 | 504990 | 616 | -77.3 | 504990 | 643 | -82.7 | 504990 | 410 |
| MR_1774416425_90101F54 | 504990 | 244 | -84.1 | 504990 | 616 | -80.6 | 504990 | 643 | -83.6 | 504990 | 410 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1024: `c8d019d7-bf4...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `c8d019d7-bf40-4309-af54-7bf0c3d216b1` |
| Tag | **single-answer** |
| 정답 | **C6** |
| C6 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1024] topology](images/train_1024.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3226460_1 by 50 degrees
- `C2`: Decrease A3 Offset threshold for 3243027_2
- `C3`: Lift the tilt angle  of 3226460_1 by 10 degrees
- `C4`: Lift the tilt angle of 3243027_2 by 10 degrees
- `C5`: Decrease transmission power for 3243027_2
- `C6`: Check test server and transmission issues **← 정답**
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3226460_1
- `C8`: Decrease transmission power for 3226460_1
- `C9`: Adjust the azimuth of 3243027_2 by 50 degrees
- `C10`: Decrease A3 Offset threshold for 3226460_1
- `C11`: Press down the tilt angle  of 3226460_1 by 10 degrees
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3243027_2
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3226460_1
- `C14`: Increase A3 Offset threshold for 3243027_2
- `C15`: Increase transmission power for 3226460_1
- `C16`: Add neighbor relationship between 3258030_4 and 3226460_1
- `C17`: Insufficient data; more data is needed for judgment.
- `C18`: Increase transmission power for 3243027_2
- `C19`: Increase A3 Offset threshold for 3226460_1
- `C20`: Press down the tilt angle of 3243027_2 by 10 degrees
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3243027_2
- `C22`: Add neighbor relationship between 3243027_2 and 3226460_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.826 | MS1 | 121.4656733533 | 31.1446267692 | 971 | 504990 | -87.37 | 13.53 | 584.89 | 0.09 | 2.60 | 1591 |
| 2024-09-20 22:21:32.497 | MS1 | 121.4656613698 | 31.1446334474 | 971 | 504990 | -85.14 | 13.82 | 564.93 | 0.04 | 2.84 | 1591 |
| 2024-09-20 22:21:33.148 | MS1 | 121.4656711563 | 31.1446346989 | 971 | 504990 | -91.71 | 15.60 | 462.48 | 0.18 | 2.51 | 1569 |
| 2024-09-20 22:21:34.586 | MS1 | 121.4656715220 | 31.1446257256 | 971 | 504990 | -88.75 | 13.60 | 62.22 | 0.01 | 2.86 | 410 |
| 2024-09-20 22:21:35.436 | MS1 | 121.4656721695 | 31.1446231115 | 971 | 504990 | -87.33 | 16.98 | 58.49 | 0.08 | 2.69 | 363 |
| 2024-09-20 22:21:36.615 | MS1 | 121.4656585316 | 31.1446255614 | 971 | 504990 | -88.20 | 13.87 | 67.54 | 0.06 | 2.53 | 470 |
| 2024-09-20 22:21:37.918 | MS1 | 121.4656622857 | 31.1446318979 | 971 | 504990 | -89.64 | 12.55 | 80.28 | 0.14 | 2.56 | 336 |
| 2024-09-20 22:21:38.823 | MS1 | 121.4656694430 | 31.1446284516 | 971 | 504990 | -90.37 | 8.45 | 82.68 | 0.02 | 2.97 | 459 |
| 2024-09-20 22:21:39.949 | MS1 | 121.4656619166 | 31.1446340447 | 971 | 504990 | -93.95 | 8.58 | 66.23 | 0.09 | 2.40 | 396 |
| 2024-09-20 22:21:40.429 | MS1 | 121.4656733537 | 31.1446373662 | 971 | 504990 | -93.35 | 7.21 | 372.70 | 0.13 | 2.59 | 1585 |
| 2024-09-20 22:21:41.376 | MS1 | 121.4656662698 | 31.1446298662 | 971 | 504990 | -89.22 | 11.85 | 467.14 | 0.18 | 2.53 | 1578 |
| 2024-09-20 22:21:42.257 | MS1 | 121.4656704567 | 31.1446342833 | 971 | 504990 | -92.97 | 7.05 | 493.66 | 0.01 | 2.48 | 1571 |

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
| 3226460 | 1 | 121.4694236235 | 31.1445619105 | 22 | 7 | 9 | 48.8 | TDD | 760 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3243027 | 2 | 121.4691198414 | 31.1498569914 | 82 | 14 | 12 | 23.6 | TDD | 971 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3258030 | 4 | 121.4678410363 | 31.1471694878 | 358 | 2 | 9 | 46.7 | TDD | 839 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3269551 | 3 | 121.4732941501 | 31.1503237493 | 359 | 0 | 12 | 42.6 | TDD | 436 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |

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
| 2024-09-20 22:21:31.422 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.437 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.542 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.542 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.280 | NREventA3 | measId:2;ServCellPCI:336;Se... |
| 2024-09-20 22:21:38.520 | NRHandoverAttempt | SourcePCI:336;SourceNR-ARFC... |
| 2024-09-20 22:21:38.550 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.563 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.666 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.666 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3226460 | 1 | 8.8873 | 10.6013 | -116.3836 | 17.9384 | 158.8959 | 0.0116 | 0.0094 |
| 2024_09_20 22:00 | 3243027 | 2 | 12.5576 | 8.2946 | -115.7518 | 7.4653 | 102.1246 | 0.0192 | 0.0110 |
| 2024_09_20 22:00 | 3269551 | 3 | 10.5436 | 12.1645 | -117.8199 | 12.0351 | 163.4413 | 0.0074 | 0.0150 |
| 2024_09_20 22:00 | 3258030 | 4 | 14.5654 | 11.0346 | -114.8070 | 13.9596 | 161.8768 | 0.0186 | 0.0022 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416069_A5D989FE | 504990 | 971 | -89.9 | 504990 | 760 | -95.6 | 504990 | 839 | -98.0 | 504990 | 436 |
| MR_1774416069_26223FEE | 504990 | 971 | -89.2 | 504990 | 760 | -98.4 | 504990 | 839 | -101.5 | 504990 | 436 |
| MR_1774416069_4F706F98 | 504990 | 971 | -87.4 | 504990 | 760 | -98.0 | 504990 | 839 | -101.5 | 504990 | 436 |
| MR_1774416069_703DEA83 | 504990 | 971 | -87.0 | 504990 | 760 | -96.4 | 504990 | 839 | -99.7 | 504990 | 436 |
| MR_1774416069_7F11E35F | 504990 | 971 | -90.0 | 504990 | 760 | -95.4 | 504990 | 839 | -98.1 | 504990 | 436 |
| MR_1774416069_A3017FD5 | 504990 | 971 | -90.0 | 504990 | 760 | -96.2 | 504990 | 839 | -100.9 | 504990 | 436 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1025: `63af2b29-bf7...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `63af2b29-bf72-4a70-bf8b-9a939aefc295` |
| Tag | **single-answer** |
| 정답 | **C2** |
| C2 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3279986_2 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1025] topology](images/train_1025.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3279986_2 by 5 degrees
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3279986_2 **← 정답**
- `C3`: Lift the tilt angle  of 3253982_5 by 1 degrees
- `C4`: Increase A3 Offset threshold for 3279986_2
- `C5`: Decrease A3 Offset threshold for 3253982_5
- `C6`: Adjust the azimuth of 3279986_2 by 35 degrees
- `C7`: Press down the tilt angle  of 3253982_5 by 1 degrees
- `C8`: Lift the tilt angle of 3279986_2 by 5 degrees
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3253982_5
- `C10`: Increase A3 Offset threshold for 3253982_5
- `C11`: Increase transmission power for 3279986_2
- `C12`: Adjust the azimuth of 3253982_5 by 43 degrees
- `C13`: Decrease transmission power for 3253982_5
- `C14`: Decrease transmission power for 3279986_2
- `C15`: Add neighbor relationship between 3266740_13 and 3253982_5
- `C16`: Increase transmission power for 3253982_5
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3279986_2
- `C18`: Add neighbor relationship between 3279986_2 and 3253982_5
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3253982_5
- `C20`: Check test server and transmission issues
- `C21`: Decrease A3 Offset threshold for 3279986_2
- `C22`: Insufficient data; more data is needed for judgment.

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.923 | MS1 | 121.4656676381 | 31.1446287030 | 579 | 504990 | -94.92 | 12.19 | 364.78 | 0.15 | 2.27 | 1579 |
| 2024-09-20 22:21:32.880 | MS1 | 121.4656750861 | 31.1446295133 | 138 | 504990 | -93.77 | 14.17 | 557.95 | 0.12 | 2.24 | 1578 |
| 2024-09-20 22:21:33.201 | MS1 | 121.4656655750 | 31.1446335261 | 452 | 504990 | -93.44 | 12.68 | 561.26 | 0.08 | 2.67 | 1560 |
| 2024-09-20 22:21:34.547 | MS1 | 121.4656659689 | 31.1446298332 | 738 | 152650 | -87.83 | 5.26 | 53.45 | 0.11 | 1.97 | 930 |
| 2024-09-20 22:21:35.637 | MS1 | 121.4656637579 | 31.1446268166 | 181 | 152650 | -88.84 | 3.78 | 96.34 | 0.08 | 1.81 | 995 |
| 2024-09-20 22:21:36.121 | MS1 | 121.4656709213 | 31.1446341333 | 63 | 152650 | -94.98 | 6.19 | 81.76 | 0.03 | 1.83 | 943 |
| 2024-09-20 22:21:37.725 | MS1 | 121.4656659380 | 31.1446344200 | 367 | 152650 | -89.14 | 2.34 | 99.96 | 0.06 | 1.65 | 928 |
| 2024-09-20 22:21:38.649 | MS1 | 121.4656679523 | 31.1446282988 | 738 | 152650 | -93.33 | 4.82 | 92.16 | 0.07 | 1.65 | 972 |
| 2024-09-20 22:21:39.950 | MS1 | 121.4656681743 | 31.1446231097 | 181 | 152650 | -92.59 | 6.57 | 69.73 | 0.01 | 1.76 | 983 |
| 2024-09-20 22:21:40.748 | MS1 | 121.4656760465 | 31.1446315775 | 63 | 152650 | -95.06 | 5.13 | 66.97 | 0.14 | 2.14 | 1563 |
| 2024-09-20 22:21:41.404 | MS1 | 121.4656748849 | 31.1446196934 | 367 | 152650 | -90.56 | 6.81 | 88.63 | 0.12 | 2.06 | 1579 |
| 2024-09-20 22:21:42.874 | MS1 | 121.4656728830 | 31.1446199674 | 738 | 152650 | -88.15 | 6.49 | 88.25 | 0.03 | 2.60 | 1575 |

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
| 3215813 | 8 | 121.4663898795 | 31.1473116181 | 317 | 5 | 7 | 19.9 | FDD | 611 | n1 | 152650 | 30M | 4T4R | 21 | 152650 |
| 3221485 | 6 | 121.4757844509 | 31.1492246732 | 316 | 3 | 5 | 4.0 | TDD | 757 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3225596 | 12 | 121.4741585913 | 31.1520393841 | 154 | 0 | 6 | 29.7 | FDD | 885 | n1 | 152650 | 30M | 4T4R | 22 | 152650 |
| 3225869 | 11 | 121.4750071337 | 31.1533908353 | 297 | 1 | 11 | 15.3 | FDD | 181 | n1 | 152650 | 30M | 4T4R | 27 | 152650 |
| 3238352 | 3 | 121.4697578550 | 31.1497882936 | 6 | 13 | 10 | 20.0 | TDD | 452 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3249428 | 9 | 121.4659311812 | 31.1444332366 | 192 | 13 | 12 | 27.8 | FDD | 367 | n1 | 152650 | 30M | 4T4R | 24 | 152650 |
| 3249562 | 1 | 121.4735854831 | 31.1499782622 | 293 | 15 | 3 | 8.9 | TDD | 321 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3253006 | 10 | 121.4689184319 | 31.1534902740 | 70 | 3 | 9 | 13.9 | FDD | 338 | n1 | 152650 | 30M | 4T4R | 10 | 152650 |
| 3253982 | 5 | 121.4650752521 | 31.1542269481 | 220 | 1 | 8 | 0.6 | TDD | 724 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3260459 | 7 | 121.4661562298 | 31.1508492698 | 160 | 6 | 2 | 26.7 | FDD | 738 | n1 | 152650 | 30M | 4T4R | 20 | 152650 |
| 3266740 | 13 | 121.4706671213 | 31.1509461988 | 29 | 13 | 12 | 10.9 | FDD | 63 | n1 | 152650 | 30M | 4T4R | 27 | 152650 |
| 3267430 | 4 | 121.4713449810 | 31.1535665691 | 330 | 10 | 11 | 10.2 | TDD | 138 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3279986 | 2 | 121.4644281063 | 31.1455896158 | 167 | 1 | 4 | 11.0 | TDD | 579 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |

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
| 2024-09-20 22:21:31.501 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.633 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.633 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.337 | NREventA2 | measId:1;ServCellPCI:820;Se... |
| 2024-09-20 22:21:35.484 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.784 | NREventA5 | measId:3;ServCellPCI:820;Se... |
| 2024-09-20 22:21:35.849 | NRHandoverAttempt | SourcePCI:820;SourceNR-ARFC... |
| 2024-09-20 22:21:35.872 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.882 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:35.995 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.995 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3249562 | 1 | 6.6248 | 12.5430 | -114.8009 | 8.8398 | 119.2816 | 0.0196 | 0.0120 |
| 2024_09_20 22:00 | 3279986 | 2 | 16.5807 | 7.0516 | -114.7370 | 17.1871 | 156.0799 | 0.0058 | 0.0144 |
| 2024_09_20 22:00 | 3238352 | 3 | 17.9821 | 9.2077 | -114.0627 | 11.9043 | 103.0331 | 0.0042 | 0.0164 |
| 2024_09_20 22:00 | 3267430 | 4 | 9.7399 | 5.8020 | -114.7281 | 17.5543 | 92.2876 | 0.0028 | 0.0117 |
| 2024_09_20 22:00 | 3253982 | 5 | 7.0730 | 16.5711 | -114.9577 | 5.5418 | 148.3466 | 0.0022 | 0.0138 |
| 2024_09_20 22:00 | 3221485 | 6 | 19.2888 | 19.5052 | -116.2591 | 17.3548 | 175.9449 | 0.0063 | 0.0047 |
| 2024_09_20 22:00 | 3260459 | 7 | 18.8419 | 8.4833 | -115.9583 | 3.6603 | 21.6551 | 0.0127 | 0.0012 |
| 2024_09_20 22:00 | 3215813 | 8 | 17.1118 | 11.5848 | -116.2906 | 4.6667 | 21.9988 | 0.0124 | 0.0170 |
| 2024_09_20 22:00 | 3249428 | 9 | 13.2616 | 8.1209 | -115.0677 | 4.4997 | 49.9121 | 0.0141 | 0.0103 |
| 2024_09_20 22:00 | 3253006 | 10 | 15.7861 | 11.0344 | -116.2338 | 3.9170 | 30.6356 | 0.0074 | 0.0196 |
| 2024_09_20 22:00 | 3225869 | 11 | 15.9471 | 5.4618 | -114.2447 | 3.7426 | 31.3839 | 0.0078 | 0.0150 |
| 2024_09_20 22:00 | 3225596 | 12 | 15.9249 | 5.7897 | -115.9524 | 3.6133 | 50.2317 | 0.0161 | 0.0001 |
| 2024_09_20 22:00 | 3266740 | 13 | 18.2068 | 13.3006 | -115.2204 | 4.7970 | 38.8280 | 0.0127 | 0.0128 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417118_153F56A1 | 504990 | 452 | -93.6 | 504990 | 724 | -89.7 | 504990 | 321 | -92.8 | 504990 | 757 |
| MR_1774417118_2A45256D | 504990 | 452 | -94.7 | 504990 | 724 | -90.5 | 504990 | 321 | -92.1 | 504990 | 757 |
| MR_1774417118_487A731D | 152650 | 738 | -86.2 | 152650 | 611 | -93.8 | 152650 | 885 | -94.9 | 152650 | 338 |
| MR_1774417118_B5EF737A | 152650 | 738 | -88.4 | 152650 | 611 | -94.7 | 152650 | 885 | -94.2 | 152650 | 338 |
| MR_1774417118_6F0FE02D | 152650 | 738 | -86.2 | 152650 | 611 | -94.7 | 152650 | 885 | -93.7 | 152650 | 338 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1026: `f0325075-a12...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `f0325075-a124-4d71-840c-6424b5feb653` |
| Tag | **multiple-answer** |
| 정답 | **C2|C6|C11|C14** |
| C2 의미 | Press down the tilt angle  of 3222591_5 by 1 degrees |
| C6 의미 | Increase A3 Offset threshold for 3222591_5 |
| C11 의미 | Decrease transmission power for 3222591_5 |
| C14 의미 | Increase A3 Offset threshold for 3241049_4 |
| 패턴 분류 | **P3 Overshoot (tilt)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1026] topology](images/train_1026.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 5 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 5개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3241049_4
- `C2`: Press down the tilt angle  of 3222591_5 by 1 degrees **← 정답**
- `C3`: Increase transmission power for 3222591_5
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3241049_4
- `C5`: Insufficient data; more data is needed for judgment.
- `C6`: Increase A3 Offset threshold for 3222591_5 **← 정답**
- `C7`: Adjust the azimuth of 3222591_5 by 39 degrees
- `C8`: Decrease A3 Offset threshold for 3241049_4
- `C9`: Adjust the azimuth of 3241049_4 by 19 degrees
- `C10`: Decrease A3 Offset threshold for 3222591_5
- `C11`: Decrease transmission power for 3222591_5 **← 정답**
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3241049_4
- `C13`: Press down the tilt angle of 3241049_4 by 2 degrees
- `C14`: Increase A3 Offset threshold for 3241049_4 **← 정답**
- `C15`: Lift the tilt angle  of 3222591_5 by 1 degrees
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3222591_5
- `C17`: Check test server and transmission issues
- `C18`: Increase transmission power for 3241049_4
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3222591_5
- `C20`: Lift the tilt angle of 3241049_4 by 2 degrees
- `C21`: Add neighbor relationship between 3278081_2 and 3222591_5
- `C22`: Add neighbor relationship between 3241049_4 and 3222591_5

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.971 | MS1 | 121.4656710860 | 31.1446240375 | 465 | 504990 | -81.17 | 14.66 | 420.22 | 0.06 | 2.38 | 1575 |
| 2024-09-20 22:21:32.691 | MS1 | 121.4656738364 | 31.1446342709 | 465 | 504990 | -77.15 | 12.18 | 575.21 | 0.18 | 2.02 | 1582 |
| 2024-09-20 22:21:33.660 | MS1 | 121.4656731170 | 31.1446315257 | 465 | 504990 | -82.70 | 13.80 | 595.06 | 0.11 | 2.05 | 1567 |
| 2024-09-20 22:21:34.636 | MS1 | 121.4656755773 | 31.1446312237 | 424 | 504990 | -80.45 | 2.36 | 40.63 | 0.18 | 1.49 | 1567 |
| 2024-09-20 22:21:35.611 | MS1 | 121.4656613234 | 31.1446249149 | 424 | 504990 | -84.44 | 3.81 | 40.72 | 0.18 | 1.21 | 1584 |
| 2024-09-20 22:21:36.185 | MS1 | 121.4656632171 | 31.1446330322 | 465 | 504990 | -84.62 | 3.14 | 43.85 | 0.11 | 1.36 | 1571 |
| 2024-09-20 22:21:37.955 | MS1 | 121.4656688085 | 31.1446334138 | 465 | 504990 | -88.85 | 1.80 | 21.95 | 0.08 | 1.37 | 1576 |
| 2024-09-20 22:21:38.938 | MS1 | 121.4656615363 | 31.1446295128 | 424 | 504990 | -85.26 | 2.58 | 29.26 | 0.01 | 1.31 | 1560 |
| 2024-09-20 22:21:39.605 | MS1 | 121.4656630420 | 31.1446246049 | 424 | 504990 | -84.22 | 4.30 | 62.13 | 0.12 | 1.07 | 1560 |
| 2024-09-20 22:21:40.803 | MS1 | 121.4656642969 | 31.1446335725 | 424 | 504990 | -76.98 | 17.47 | 554.43 | 0.20 | 2.33 | 1595 |
| 2024-09-20 22:21:41.940 | MS1 | 121.4656653359 | 31.1446366596 | 424 | 504990 | -84.20 | 13.30 | 441.08 | 0.12 | 2.96 | 1596 |
| 2024-09-20 22:21:42.725 | MS1 | 121.4656688976 | 31.1446285626 | 424 | 504990 | -83.04 | 14.60 | 433.90 | 0.06 | 2.52 | 1586 |

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
| 3221255 | 1 | 121.4726674439 | 31.1517319571 | 164 | 14 | 2 | 43.9 | TDD | 834 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3222591 | 5 | 121.4722525967 | 31.1559098113 | 246 | 0 | 2 | 17.4 | TDD | 126 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3241049 | 4 | 121.4677675177 | 31.1559995294 | 170 | 1 | 6 | 21.5 | TDD | 465 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3263368 | 3 | 121.4752716505 | 31.1508482005 | 300 | 9 | 11 | 29.8 | TDD | 424 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3278081 | 2 | 121.4708044577 | 31.1539493810 | 228 | 9 | 1 | 32.9 | TDD | 38 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |

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
| 2024-09-20 22:21:30.916 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.932 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.038 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.038 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:33.784 | NREventA3 | measId:2;ServCellPCI:534;Se... |
| 2024-09-20 22:21:34.024 | NRHandoverAttempt | SourcePCI:534;SourceNR-ARFC... |
| 2024-09-20 22:21:34.059 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:34.074 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:34.210 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:34.210 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.784 | NREventA3 | measId:2;ServCellPCI:632;Se... |
| 2024-09-20 22:21:36.024 | NRHandoverAttempt | SourcePCI:632;SourceNR-ARFC... |
| 2024-09-20 22:21:36.074 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:36.085 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:36.200 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.200 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.784 | NREventA3 | measId:2;ServCellPCI:534;Se... |
| 2024-09-20 22:21:38.024 | NRHandoverAttempt | SourcePCI:534;SourceNR-ARFC... |
| 2024-09-20 22:21:38.067 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.082 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.217 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.217 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3221255 | 1 | 10.2665 | 13.0253 | -114.9762 | 10.4177 | 140.0711 | 0.0166 | 0.0103 |
| 2024_09_20 22:00 | 3278081 | 2 | 17.4076 | 14.3732 | -117.5111 | 15.3630 | 107.2737 | 0.0060 | 0.0132 |
| 2024_09_20 22:00 | 3263368 | 3 | 9.3578 | 6.0484 | -117.3865 | 5.4212 | 151.7640 | 0.0096 | 0.0091 |
| 2024_09_20 22:00 | 3241049 | 4 | 11.4997 | 5.1197 | -117.2864 | 19.8970 | 190.6824 | 0.0099 | 0.0009 |
| 2024_09_20 22:00 | 3222591 | 5 | 8.1254 | 19.0226 | -117.7341 | 18.9514 | 192.6772 | 0.0174 | 0.0179 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416696_BE24358C | 504990 | 424 | -80.8 | 504990 | 465 | -82.7 | 504990 | 126 | -85.5 | 504990 | 38 |
| MR_1774416696_90E1E65A | 504990 | 465 | -79.6 | 504990 | 424 | -82.0 | 504990 | 126 | -86.7 | 504990 | 38 |
| MR_1774416696_913B4E70 | 504990 | 465 | -80.8 | 504990 | 424 | -80.1 | 504990 | 126 | -88.3 | 504990 | 38 |
| MR_1774416696_14C8ED69 | 504990 | 465 | -79.3 | 504990 | 424 | -82.4 | 504990 | 126 | -85.7 | 504990 | 38 |
| MR_1774416696_6314D0B1 | 504990 | 465 | -81.4 | 504990 | 424 | -79.5 | 504990 | 126 | -85.9 | 504990 | 38 |
| MR_1774416696_40A4F4CF | 504990 | 465 | -80.7 | 504990 | 424 | -79.1 | 504990 | 126 | -87.1 | 504990 | 38 |
| MR_1774416696_A3D9361E | 504990 | 424 | -82.1 | 504990 | 465 | -80.8 | 504990 | 126 | -85.2 | 504990 | 38 |
| MR_1774416696_3F3DF03F | 504990 | 424 | -82.1 | 504990 | 465 | -79.8 | 504990 | 126 | -88.7 | 504990 | 38 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1027: `a3aab5e6-5b8...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `a3aab5e6-5b88-480a-abc3-b48c5e800bdc` |
| Tag | **single-answer** |
| 정답 | **C16** |
| C16 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1027] topology](images/train_1027.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle  of 3269753_2 by 3 degrees
- `C2`: Increase A3 Offset threshold for 3269753_2
- `C3`: Decrease transmission power for 3266297_4
- `C4`: Decrease A3 Offset threshold for 3269753_2
- `C5`: Add neighbor relationship between 3215279_1 and 3269753_2
- `C6`: Increase transmission power for 3269753_2
- `C7`: Decrease A3 Offset threshold for 3266297_4
- `C8`: Adjust the azimuth of 3266297_4 by 48 degrees
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3269753_2
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3266297_4
- `C11`: Press down the tilt angle of 3266297_4 by 10 degrees
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3266297_4
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3269753_2
- `C14`: Decrease transmission power for 3269753_2
- `C15`: Lift the tilt angle of 3266297_4 by 10 degrees
- `C16`: Check test server and transmission issues **← 정답**
- `C17`: Add neighbor relationship between 3266297_4 and 3269753_2
- `C18`: Increase transmission power for 3266297_4
- `C19`: Adjust the azimuth of 3269753_2 by 50 degrees
- `C20`: Insufficient data; more data is needed for judgment.
- `C21`: Increase A3 Offset threshold for 3266297_4
- `C22`: Press down the tilt angle  of 3269753_2 by 3 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.303 | MS1 | 121.4656760857 | 31.1446378665 | 604 | 504990 | -90.77 | 13.03 | 561.22 | 0.10 | 2.85 | 1566 |
| 2024-09-20 22:21:32.492 | MS1 | 121.4656646806 | 31.1446300351 | 604 | 504990 | -89.73 | 14.21 | 476.98 | 0.13 | 2.15 | 1584 |
| 2024-09-20 22:21:33.245 | MS1 | 121.4656758059 | 31.1446338059 | 604 | 504990 | -87.98 | 13.61 | 526.92 | 0.16 | 2.91 | 1571 |
| 2024-09-20 22:21:34.121 | MS1 | 121.4656603243 | 31.1446278758 | 604 | 504990 | -90.48 | 15.46 | 95.95 | 0.15 | 2.40 | 491 |
| 2024-09-20 22:21:35.500 | MS1 | 121.4656695170 | 31.1446192659 | 604 | 504990 | -91.04 | 15.78 | 93.19 | 0.08 | 2.09 | 308 |
| 2024-09-20 22:21:36.418 | MS1 | 121.4656719770 | 31.1446239160 | 604 | 504990 | -86.25 | 13.84 | 62.20 | 0.13 | 2.48 | 431 |
| 2024-09-20 22:21:37.375 | MS1 | 121.4656724111 | 31.1446193117 | 604 | 504990 | -90.03 | 9.25 | 59.65 | 0.19 | 2.57 | 496 |
| 2024-09-20 22:21:38.444 | MS1 | 121.4656645619 | 31.1446352410 | 604 | 504990 | -89.41 | 8.13 | 63.91 | 0.01 | 2.50 | 497 |
| 2024-09-20 22:21:39.719 | MS1 | 121.4656693875 | 31.1446355817 | 604 | 504990 | -93.13 | 12.30 | 84.11 | 0.15 | 2.63 | 309 |
| 2024-09-20 22:21:40.545 | MS1 | 121.4656766876 | 31.1446321655 | 604 | 504990 | -89.02 | 12.59 | 451.21 | 0.16 | 2.86 | 1578 |
| 2024-09-20 22:21:41.651 | MS1 | 121.4656637602 | 31.1446291030 | 604 | 504990 | -91.03 | 7.22 | 318.03 | 0.16 | 2.74 | 1599 |
| 2024-09-20 22:21:42.594 | MS1 | 121.4656735770 | 31.1446364725 | 604 | 504990 | -89.67 | 12.08 | 326.95 | 0.03 | 2.94 | 1570 |

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
| 3215279 | 1 | 121.4711870243 | 31.1559842171 | 180 | 6 | 7 | 40.9 | TDD | 281 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3225738 | 3 | 121.4696175944 | 31.1454524300 | 236 | 10 | 4 | 32.0 | TDD | 164 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3266297 | 4 | 121.4696323958 | 31.1501201826 | 164 | 14 | 11 | 40.0 | TDD | 604 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3269753 | 2 | 121.4663831957 | 31.1510883024 | 301 | 0 | 8 | 32.7 | TDD | 988 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |

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
| 2024-09-20 22:21:30.888 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.907 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.051 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.051 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.782 | NREventA3 | measId:2;ServCellPCI:346;Se... |
| 2024-09-20 22:21:38.022 | NRHandoverAttempt | SourcePCI:346;SourceNR-ARFC... |
| 2024-09-20 22:21:38.066 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.079 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.195 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.195 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3215279 | 1 | 5.0481 | 15.1724 | -116.2312 | 7.2880 | 141.7825 | 0.0005 | 0.0034 |
| 2024_09_20 22:00 | 3269753 | 2 | 14.9129 | 8.6576 | -117.3464 | 14.7913 | 101.6730 | 0.0023 | 0.0051 |
| 2024_09_20 22:00 | 3225738 | 3 | 19.4099 | 14.9559 | -117.4407 | 11.3732 | 81.9789 | 0.0107 | 0.0178 |
| 2024_09_20 22:00 | 3266297 | 4 | 9.1426 | 9.1673 | -115.0559 | 5.6113 | 89.0938 | 0.0176 | 0.0121 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413190_94245EDC | 504990 | 604 | -89.7 | 504990 | 988 | -97.4 | 504990 | 281 | -103.4 | 504990 | 164 |
| MR_1774413190_D030BA4B | 504990 | 604 | -92.1 | 504990 | 988 | -97.5 | 504990 | 281 | -104.6 | 504990 | 164 |
| MR_1774413190_6B95BBBD | 504990 | 604 | -90.1 | 504990 | 988 | -96.8 | 504990 | 281 | -105.6 | 504990 | 164 |
| MR_1774413190_A3D2D536 | 504990 | 604 | -89.0 | 504990 | 988 | -95.5 | 504990 | 281 | -103.7 | 504990 | 164 |
| MR_1774413190_197D1240 | 504990 | 604 | -91.2 | 504990 | 988 | -97.0 | 504990 | 281 | -105.6 | 504990 | 164 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1028: `6bfe2a67-57f...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `6bfe2a67-57f2-4711-8343-9179f3cd6be9` |
| Tag | **single-answer** |
| 정답 | **C6** |
| C6 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1028] topology](images/train_1028.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3268073_3
- `C2`: Increase transmission power for 3268073_3
- `C3`: Increase A3 Offset threshold for 3268073_3
- `C4`: Press down the tilt angle of 3268073_3 by 6 degrees
- `C5`: Lift the tilt angle of 3268073_3 by 6 degrees
- `C6`: Insufficient data; more data is needed for judgment. **← 정답**
- `C7`: Increase A3 Offset threshold for 3253770_1
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3268073_3
- `C9`: Decrease A3 Offset threshold for 3253770_1
- `C10`: Add neighbor relationship between 3277219_4 and 3253770_1
- `C11`: Adjust the azimuth of 3253770_1 by 50 degrees
- `C12`: Decrease transmission power for 3268073_3
- `C13`: Add neighbor relationship between 3268073_3 and 3253770_1
- `C14`: Decrease transmission power for 3253770_1
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3253770_1
- `C16`: Increase transmission power for 3253770_1
- `C17`: Lift the tilt angle  of 3253770_1 by 10 degrees
- `C18`: Press down the tilt angle  of 3253770_1 by 10 degrees
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3253770_1
- `C20`: Adjust the azimuth of 3268073_3 by 50 degrees
- `C21`: Check test server and transmission issues
- `C22`: Decrease A3 Offset threshold for 3268073_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.738 | MS1 | 121.4656766935 | 31.1446290719 | 13 | 504990 | -88.71 | 16.89 | 450.21 | 0.10 | 2.02 | 1593 |
| 2024-09-20 22:21:32.976 | MS1 | 121.4656630293 | 31.1446363410 | 13 | 504990 | -89.77 | 16.30 | 494.07 | 0.03 | 2.89 | 1564 |
| 2024-09-20 22:21:33.601 | MS1 | 121.4656590002 | 31.1446181384 | 13 | 504990 | -85.44 | 15.18 | 489.66 | 0.11 | 2.51 | 1572 |
| 2024-09-20 22:21:34.727 | MS1 | 121.4656764992 | 31.1446223027 | 13 | 504990 | -88.86 | 14.77 | 84.09 | 0.16 | 3.00 | 1588 |
| 2024-09-20 22:21:35.669 | MS1 | 121.4656645970 | 31.1446264054 | 13 | 504990 | -85.45 | 17.41 | 48.68 | 0.12 | 2.54 | 1574 |
| 2024-09-20 22:21:36.880 | MS1 | 121.4656626011 | 31.1446346743 | 13 | 504990 | -87.88 | 17.22 | 73.88 | 0.16 | 2.16 | 1593 |
| 2024-09-20 22:21:37.277 | MS1 | 121.4656722027 | 31.1446188252 | 13 | 504990 | -90.41 | 8.08 | 60.59 | 0.17 | 2.29 | 1579 |
| 2024-09-20 22:21:38.457 | MS1 | 121.4656586740 | 31.1446275740 | 13 | 504990 | -89.01 | 11.25 | 65.31 | 0.07 | 2.97 | 1598 |
| 2024-09-20 22:21:39.219 | MS1 | 121.4656656334 | 31.1446251647 | 13 | 504990 | -91.40 | 7.64 | 64.37 | 0.09 | 2.49 | 1565 |
| 2024-09-20 22:21:40.932 | MS1 | 121.4656747155 | 31.1446286230 | 13 | 504990 | -92.86 | 12.89 | 498.27 | 0.14 | 2.44 | 1590 |
| 2024-09-20 22:21:41.949 | MS1 | 121.4656752123 | 31.1446333506 | 13 | 504990 | -89.40 | 9.97 | 549.62 | 0.13 | 2.99 | 1594 |
| 2024-09-20 22:21:42.741 | MS1 | 121.4656589086 | 31.1446290561 | 13 | 504990 | -93.43 | 8.12 | 346.94 | 0.12 | 2.64 | 1586 |

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
| 3211372 | 2 | 121.4712663146 | 31.1449259550 | 181 | 15 | 12 | 40.9 | TDD | 100 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3253770 | 1 | 121.4727451241 | 31.1484904615 | 62 | 12 | 8 | 37.3 | TDD | 456 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3268073 | 3 | 121.4713748510 | 31.1535803035 | 281 | 5 | 9 | 25.9 | TDD | 13 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3277219 | 4 | 121.4694120499 | 31.1448416208 | 93 | 10 | 8 | 16.4 | TDD | 239 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |

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
| 2024-09-20 22:21:31.000 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.024 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.165 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.165 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.832 | NREventA3 | measId:2;ServCellPCI:123;Se... |
| 2024-09-20 22:21:38.072 | NRHandoverAttempt | SourcePCI:123;SourceNR-ARFC... |
| 2024-09-20 22:21:38.108 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.121 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.253 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.253 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3253770 | 1 | 83.9005 | 85.5636 | -116.6392 | 13.6416 | 172.8969 | 0.0023 | 0.0160 |
| 2024_09_19 22:00 | 3211372 | 2 | 84.4341 | 80.9047 | -114.1397 | 10.0923 | 106.3636 | 0.0137 | 0.0042 |
| 2024_09_19 22:00 | 3268073 | 3 | 88.1158 | 77.5551 | -117.0670 | 19.2855 | 151.0844 | 0.0123 | 0.0148 |
| 2024_09_19 22:00 | 3277219 | 4 | 90.2802 | 80.7765 | -115.0686 | 19.8946 | 125.1003 | 0.0073 | 0.0023 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415066_7C7F76D3 | 504990 | 13 | -86.9 | 504990 | 456 | -93.5 | 504990 | 239 | -95.6 | 504990 | 100 |
| MR_1774415066_FEA7088D | 504990 | 13 | -87.6 | 504990 | 456 | -92.6 | 504990 | 239 | -97.3 | 504990 | 100 |
| MR_1774415066_CE84E82B | 504990 | 13 | -87.3 | 504990 | 456 | -92.9 | 504990 | 239 | -95.9 | 504990 | 100 |
| MR_1774415066_CAA9BA22 | 504990 | 13 | -86.9 | 504990 | 456 | -92.7 | 504990 | 239 | -96.2 | 504990 | 100 |
| MR_1774415066_6EAE241A | 504990 | 13 | -89.9 | 504990 | 456 | -93.2 | 504990 | 239 | -97.5 | 504990 | 100 |
| MR_1774415066_FC33E89A | 504990 | 13 | -87.8 | 504990 | 456 | -93.6 | 504990 | 239 | -94.5 | 504990 | 100 |
| MR_1774415066_D71FD9A4 | 504990 | 13 | -89.9 | 504990 | 456 | -92.6 | 504990 | 239 | -94.6 | 504990 | 100 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1029: `5ac230d6-1eb...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `5ac230d6-1eb5-42e9-a741-48aa584926b8` |
| Tag | **single-answer** |
| 정답 | **C16** |
| C16 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3217895_1 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1029] topology](images/train_1029.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle  of 3260434_2 by 10 degrees
- `C2`: Adjust the azimuth of 3260434_2 by 50 degrees
- `C3`: Press down the tilt angle of 3217895_1 by 3 degrees
- `C4`: Check test server and transmission issues
- `C5`: Add neighbor relationship between 3270053_3 and 3260434_2
- `C6`: Decrease A3 Offset threshold for 3217895_1
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3260434_2
- `C8`: Decrease transmission power for 3260434_2
- `C9`: Increase transmission power for 3217895_1
- `C10`: Add neighbor relationship between 3217895_1 and 3260434_2
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3260434_2
- `C12`: Insufficient data; more data is needed for judgment.
- `C13`: Decrease A3 Offset threshold for 3260434_2
- `C14`: Increase A3 Offset threshold for 3217895_1
- `C15`: Increase transmission power for 3260434_2
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3217895_1 **← 정답**
- `C17`: Press down the tilt angle  of 3260434_2 by 10 degrees
- `C18`: Adjust the azimuth of 3217895_1 by 25 degrees
- `C19`: Lift the tilt angle of 3217895_1 by 3 degrees
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3217895_1
- `C21`: Decrease transmission power for 3217895_1
- `C22`: Increase A3 Offset threshold for 3260434_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.172 | MS1 | 121.4656772811 | 31.1446298560 | 873 | 504990 | -89.59 | 17.84 | 405.08 | 0.07 | 2.61 | 1565 |
| 2024-09-20 22:21:32.666 | MS1 | 121.4656635453 | 31.1446254899 | 873 | 504990 | -88.15 | 15.53 | 540.74 | 0.16 | 2.10 | 1573 |
| 2024-09-20 22:21:33.157 | MS1 | 121.4656641373 | 31.1446347458 | 873 | 504990 | -89.51 | 17.12 | 297.74 | 0.01 | 2.90 | 1599 |
| 2024-09-20 22:21:34.946 | MS1 | 121.4656673779 | 31.1446265512 | 873 | 504990 | -85.87 | 15.83 | 58.58 | 0.68 | 2.01 | 671 |
| 2024-09-20 22:21:35.752 | MS1 | 121.4656632045 | 31.1446252497 | 873 | 504990 | -85.44 | 16.05 | 64.32 | 0.66 | 2.38 | 528 |
| 2024-09-20 22:21:36.334 | MS1 | 121.4656630998 | 31.1446367580 | 873 | 504990 | -88.99 | 12.73 | 53.37 | 0.59 | 2.07 | 611 |
| 2024-09-20 22:21:37.868 | MS1 | 121.4656760664 | 31.1446362659 | 873 | 504990 | -92.27 | 8.88 | 58.23 | 0.58 | 2.49 | 564 |
| 2024-09-20 22:21:38.942 | MS1 | 121.4656582231 | 31.1446201324 | 873 | 504990 | -91.59 | 12.51 | 91.49 | 0.58 | 2.93 | 696 |
| 2024-09-20 22:21:39.244 | MS1 | 121.4656611265 | 31.1446294721 | 873 | 504990 | -92.51 | 12.78 | 58.39 | 0.52 | 2.11 | 614 |
| 2024-09-20 22:21:40.158 | MS1 | 121.4656745232 | 31.1446365861 | 873 | 504990 | -91.46 | 7.71 | 425.56 | 0.10 | 2.23 | 1577 |
| 2024-09-20 22:21:41.151 | MS1 | 121.4656628606 | 31.1446227659 | 873 | 504990 | -92.31 | 7.75 | 318.38 | 0.19 | 2.04 | 1578 |
| 2024-09-20 22:21:42.354 | MS1 | 121.4656735262 | 31.1446360779 | 873 | 504990 | -90.91 | 7.79 | 460.48 | 0.08 | 2.80 | 1563 |

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
| 3217895 | 1 | 121.4658236857 | 31.1552319938 | 206 | 2 | 2 | 30.5 | TDD | 873 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3241054 | 4 | 121.4750076468 | 31.1490522340 | 2 | 8 | 9 | 22.6 | TDD | 906 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3260434 | 2 | 121.4738658765 | 31.1451304070 | 354 | 12 | 3 | 42.1 | TDD | 114 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3270053 | 3 | 121.4645558089 | 31.1497150467 | 245 | 4 | 3 | 26.3 | TDD | 765 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:31.306 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.327 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.432 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.432 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.115 | NREventA3 | measId:2;ServCellPCI:292;Se... |
| 2024-09-20 22:21:38.355 | NRHandoverAttempt | SourcePCI:292;SourceNR-ARFC... |
| 2024-09-20 22:21:38.400 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.412 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.516 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.516 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3217895 | 1 | 6.3134 | 10.3030 | -116.6372 | 7.8707 | 118.4206 | 0.0085 | 0.0080 |
| 2024_09_20 22:00 | 3260434 | 2 | 10.2304 | 12.4037 | -117.9944 | 8.3342 | 109.9276 | 0.0009 | 0.0074 |
| 2024_09_20 22:00 | 3270053 | 3 | 8.9063 | 18.0604 | -115.1175 | 18.9322 | 115.5016 | 0.0149 | 0.0059 |
| 2024_09_20 22:00 | 3241054 | 4 | 13.7016 | 12.0050 | -114.8111 | 11.0027 | 116.2486 | 0.0088 | 0.0164 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416569_C76E322E | 504990 | 873 | -86.4 | 504990 | 114 | -91.8 | 504990 | 765 | -95.5 | 504990 | 906 |
| MR_1774416569_498A25F7 | 504990 | 873 | -84.0 | 504990 | 114 | -91.7 | 504990 | 765 | -95.8 | 504990 | 906 |
| MR_1774416569_6EE10C26 | 504990 | 873 | -86.7 | 504990 | 114 | -94.9 | 504990 | 765 | -96.3 | 504990 | 906 |
| MR_1774416569_48512E57 | 504990 | 873 | -84.1 | 504990 | 114 | -94.3 | 504990 | 765 | -96.7 | 504990 | 906 |
| MR_1774416569_035FE2A6 | 504990 | 873 | -87.7 | 504990 | 114 | -95.3 | 504990 | 765 | -96.4 | 504990 | 906 |
| MR_1774416569_A8648607 | 504990 | 873 | -87.3 | 504990 | 114 | -91.9 | 504990 | 765 | -94.9 | 504990 | 906 |

> *... 2개 열 생략 (전체 14열)*

---
