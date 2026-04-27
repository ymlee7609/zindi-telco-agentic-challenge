# Track A 문제 분석 — train[1320]~train[1329]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[1320] ~ train[1329] (10개)

## 목차

1. [문제 1320: `398fec09-bba...`](#1320) — single-answer, 정답: C3
2. [문제 1321: `6cecbd9d-6d5...`](#1321) — multiple-answer, 정답: C4|C13
3. [문제 1322: `8645470e-c55...`](#1322) — single-answer, 정답: C5
4. [문제 1323: `2b39630c-9ca...`](#1323) — single-answer, 정답: C14
5. [문제 1324: `f700f740-815...`](#1324) — single-answer, 정답: C6
6. [문제 1325: `94cbd7c0-c41...`](#1325) — single-answer, 정답: C6
7. [문제 1326: `43b27ef1-26f...`](#1326) — single-answer, 정답: C5
8. [문제 1327: `de4e627d-c0b...`](#1327) — single-answer, 정답: C15
9. [문제 1328: `4c344670-53a...`](#1328) — single-answer, 정답: C18
10. [문제 1329: `603ea76f-9a9...`](#1329) — single-answer, 정답: C13

---

### 문제 1320: `398fec09-bba...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `398fec09-bbab-46de-882b-d979640a5834` |
| Tag | **single-answer** |
| 정답 | **C3** |
| C3 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3253787_4 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1320] topology](images/train_1320.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3253787_4 by 45 degrees
- `C2`: Add neighbor relationship between 3277587_13 and 3216289_1
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3253787_4 **← 정답**
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3216289_1
- `C5`: Increase A3 Offset threshold for 3253787_4
- `C6`: Check test server and transmission issues
- `C7`: Add neighbor relationship between 3253787_4 and 3216289_1
- `C8`: Increase A3 Offset threshold for 3216289_1
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3253787_4
- `C10`: Increase transmission power for 3253787_4
- `C11`: Decrease transmission power for 3253787_4
- `C12`: Decrease A3 Offset threshold for 3253787_4
- `C13`: Lift the tilt angle  of 3216289_1 by 4 degrees
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3216289_1
- `C15`: Lift the tilt angle of 3253787_4 by 6 degrees
- `C16`: Adjust the azimuth of 3216289_1 by 22 degrees
- `C17`: Insufficient data; more data is needed for judgment.
- `C18`: Decrease transmission power for 3216289_1
- `C19`: Increase transmission power for 3216289_1
- `C20`: Press down the tilt angle  of 3216289_1 by 4 degrees
- `C21`: Decrease A3 Offset threshold for 3216289_1
- `C22`: Press down the tilt angle of 3253787_4 by 6 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.657 | MS1 | 121.4656719980 | 31.1446271027 | 662 | 504990 | -94.42 | 12.28 | 335.68 | 0.07 | 2.63 | 1575 |
| 2024-09-20 22:21:32.896 | MS1 | 121.4656770515 | 31.1446360142 | 359 | 504990 | -93.53 | 10.81 | 384.92 | 0.05 | 2.01 | 1588 |
| 2024-09-20 22:21:33.222 | MS1 | 121.4656726083 | 31.1446226502 | 665 | 504990 | -94.83 | 13.26 | 400.67 | 0.19 | 2.52 | 1561 |
| 2024-09-20 22:21:34.727 | MS1 | 121.4656719865 | 31.1446311443 | 105 | 152650 | -90.26 | 7.04 | 84.87 | 0.00 | 1.80 | 965 |
| 2024-09-20 22:21:35.219 | MS1 | 121.4656655390 | 31.1446293035 | 345 | 152650 | -95.98 | 4.46 | 60.30 | 0.03 | 1.73 | 909 |
| 2024-09-20 22:21:36.667 | MS1 | 121.4656711359 | 31.1446345564 | 476 | 152650 | -95.39 | 4.80 | 87.67 | 0.01 | 1.61 | 931 |
| 2024-09-20 22:21:37.245 | MS1 | 121.4656727100 | 31.1446305428 | 943 | 152650 | -92.19 | 4.60 | 56.07 | 0.01 | 1.66 | 975 |
| 2024-09-20 22:21:38.809 | MS1 | 121.4656752424 | 31.1446226799 | 105 | 152650 | -90.61 | 5.49 | 92.42 | 0.06 | 1.98 | 987 |
| 2024-09-20 22:21:39.217 | MS1 | 121.4656679444 | 31.1446350942 | 345 | 152650 | -93.35 | 2.22 | 69.74 | 0.03 | 1.63 | 939 |
| 2024-09-20 22:21:40.360 | MS1 | 121.4656649465 | 31.1446258908 | 476 | 152650 | -96.50 | 3.03 | 48.32 | 0.18 | 2.46 | 1589 |
| 2024-09-20 22:21:41.867 | MS1 | 121.4656590546 | 31.1446249807 | 943 | 152650 | -92.52 | 2.74 | 60.86 | 0.01 | 2.53 | 1598 |
| 2024-09-20 22:21:42.241 | MS1 | 121.4656594118 | 31.1446323221 | 105 | 152650 | -87.70 | 7.52 | 67.02 | 0.17 | 2.26 | 1562 |

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
| 3211024 | 7 | 121.4729544082 | 31.1446168514 | 340 | 6 | 8 | 24.5 | FDD | 451 | n1 | 152650 | 30M | 4T4R | 15 | 152650 |
| 3213637 | 10 | 121.4650393161 | 31.1540092825 | 253 | 7 | 12 | 25.6 | FDD | 13 | n1 | 152650 | 30M | 4T4R | 23 | 152650 |
| 3216289 | 1 | 121.4678350333 | 31.1551194185 | 168 | 3 | 7 | 15.3 | TDD | 899 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3220044 | 3 | 121.4721112729 | 31.1532623770 | 74 | 4 | 1 | 10.2 | TDD | 298 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3235900 | 12 | 121.4685562188 | 31.1505266256 | 219 | 11 | 3 | 22.4 | FDD | 345 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |
| 3253787 | 4 | 121.4668873547 | 31.1489749838 | 239 | 5 | 2 | 6.6 | TDD | 662 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3261096 | 2 | 121.4708196871 | 31.1449269598 | 63 | 3 | 6 | 19.8 | TDD | 359 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3267101 | 11 | 121.4691321415 | 31.1524871848 | 88 | 8 | 2 | 6.3 | FDD | 943 | n1 | 152650 | 30M | 4T4R | 24 | 152650 |
| 3270194 | 9 | 121.4744754992 | 31.1478448352 | 322 | 1 | 6 | 16.9 | FDD | 105 | n1 | 152650 | 30M | 4T4R | 27 | 152650 |
| 3273473 | 5 | 121.4683661592 | 31.1447811182 | 63 | 0 | 6 | 4.6 | TDD | 376 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3275900 | 8 | 121.4650944756 | 31.1551780556 | 260 | 13 | 9 | 2.2 | FDD | 40 | n1 | 152650 | 30M | 4T4R | 23 | 152650 |
| 3277587 | 13 | 121.4747884888 | 31.1486708303 | 60 | 3 | 6 | 20.6 | FDD | 476 | n1 | 152650 | 30M | 4T4R | 27 | 152650 |
| 3279722 | 6 | 121.4730535166 | 31.1482010930 | 95 | 0 | 10 | 17.7 | TDD | 665 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |

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
| 2024-09-20 22:21:31.156 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.178 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.321 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.321 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.055 | NREventA2 | measId:1;ServCellPCI:572;Se... |
| 2024-09-20 22:21:35.190 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.422 | NREventA5 | measId:3;ServCellPCI:572;Se... |
| 2024-09-20 22:21:35.464 | NRHandoverAttempt | SourcePCI:572;SourceNR-ARFC... |
| 2024-09-20 22:21:35.488 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.503 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:35.612 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.612 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3216289 | 1 | 11.2742 | 15.4033 | -116.8232 | 15.1812 | 119.7301 | 0.0060 | 0.0178 |
| 2024_09_20 22:00 | 3261096 | 2 | 17.0155 | 5.5135 | -115.3440 | 12.0190 | 177.1456 | 0.0061 | 0.0165 |
| 2024_09_20 22:00 | 3220044 | 3 | 12.7085 | 14.7602 | -117.6386 | 13.3065 | 132.9878 | 0.0068 | 0.0020 |
| 2024_09_20 22:00 | 3253787 | 4 | 5.4565 | 12.4662 | -114.8958 | 9.8341 | 114.6305 | 0.0078 | 0.0020 |
| 2024_09_20 22:00 | 3273473 | 5 | 17.0652 | 10.1077 | -114.4179 | 14.1148 | 82.2787 | 0.0168 | 0.0034 |
| 2024_09_20 22:00 | 3279722 | 6 | 17.3328 | 6.7054 | -117.2456 | 11.4480 | 115.0364 | 0.0028 | 0.0042 |
| 2024_09_20 22:00 | 3211024 | 7 | 17.7308 | 15.2848 | -117.8654 | 3.7096 | 59.0714 | 0.0005 | 0.0036 |
| 2024_09_20 22:00 | 3275900 | 8 | 15.9496 | 15.3428 | -115.4837 | 3.4785 | 28.7959 | 0.0136 | 0.0165 |
| 2024_09_20 22:00 | 3270194 | 9 | 17.8816 | 15.9552 | -117.3464 | 4.0336 | 22.1856 | 0.0087 | 0.0044 |
| 2024_09_20 22:00 | 3213637 | 10 | 16.8018 | 6.1894 | -116.5688 | 4.7124 | 23.4510 | 0.0161 | 0.0017 |
| 2024_09_20 22:00 | 3267101 | 11 | 16.7313 | 7.7831 | -117.4649 | 4.9987 | 52.1352 | 0.0181 | 0.0002 |
| 2024_09_20 22:00 | 3235900 | 12 | 9.0149 | 8.1348 | -115.2784 | 3.0761 | 47.8140 | 0.0132 | 0.0087 |
| 2024_09_20 22:00 | 3277587 | 13 | 12.5071 | 12.0099 | -115.2480 | 3.1518 | 45.7434 | 0.0000 | 0.0092 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412265_03717013 | 152650 | 105 | -91.6 | 152650 | 40 | -94.3 | 152650 | 451 | -96.9 | 152650 | 13 |
| MR_1774412265_26DAC07B | 152650 | 105 | -90.0 | 152650 | 40 | -92.1 | 152650 | 451 | -95.8 | 152650 | 13 |
| MR_1774412265_03BCDD81 | 152650 | 105 | -90.9 | 152650 | 40 | -91.4 | 152650 | 451 | -98.6 | 152650 | 13 |
| MR_1774412265_D4ADE5FC | 152650 | 105 | -88.3 | 152650 | 40 | -91.9 | 152650 | 451 | -98.7 | 152650 | 13 |
| MR_1774412265_9789D915 | 152650 | 105 | -90.1 | 152650 | 40 | -92.6 | 152650 | 451 | -97.4 | 152650 | 13 |
| MR_1774412265_DDE7D3DB | 152650 | 105 | -92.0 | 152650 | 40 | -93.8 | 152650 | 451 | -98.5 | 152650 | 13 |
| MR_1774412265_D806D855 | 152650 | 105 | -90.2 | 152650 | 40 | -93.9 | 152650 | 451 | -96.8 | 152650 | 13 |
| MR_1774412265_70E9CA7F | 504990 | 665 | -96.7 | 504990 | 899 | -92.0 | 504990 | 376 | -100.2 | 504990 | 298 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1321: `6cecbd9d-6d5...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `6cecbd9d-6d50-4a26-86e0-fe2c83d64f73` |
| Tag | **multiple-answer** |
| 정답 | **C4|C13** |
| C4 의미 | Increase transmission power for 3228913_4 |
| C13 의미 | Adjust the azimuth of 3228913_4 by 30 degrees |
| 패턴 분류 | **P4 Coverage (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1321] topology](images/train_1321.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment.
- `C2`: Increase A3 Offset threshold for 3228913_4
- `C3`: Decrease A3 Offset threshold for 3228913_4
- `C4`: Increase transmission power for 3228913_4 **← 정답**
- `C5`: Lift the tilt angle of 3228913_4 by 9 degrees
- `C6`: Press down the tilt angle of 3228913_4 by 9 degrees
- `C7`: Add neighbor relationship between 3278962_3 and 3220721_2
- `C8`: Press down the tilt angle  of 3220721_2 by 5 degrees
- `C9`: Decrease A3 Offset threshold for 3220721_2
- `C10`: Lift the tilt angle  of 3220721_2 by 5 degrees
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3220721_2
- `C12`: Check test server and transmission issues
- `C13`: Adjust the azimuth of 3228913_4 by 30 degrees **← 정답**
- `C14`: Increase A3 Offset threshold for 3220721_2
- `C15`: Adjust the azimuth of 3220721_2 by 28 degrees
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3228913_4
- `C17`: Decrease transmission power for 3228913_4
- `C18`: Decrease transmission power for 3220721_2
- `C19`: Add neighbor relationship between 3228913_4 and 3220721_2
- `C20`: Increase transmission power for 3220721_2
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3220721_2
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3228913_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.701 | MS1 | 121.4656757024 | 31.1446205590 | 731 | 504990 | -86.14 | 16.70 | 562.32 | 0.16 | 2.42 | 1592 |
| 2024-09-20 22:21:32.619 | MS1 | 121.4656651222 | 31.1446187578 | 731 | 504990 | -87.49 | 15.21 | 500.81 | 0.13 | 2.23 | 1572 |
| 2024-09-20 22:21:33.819 | MS1 | 121.4656766417 | 31.1446375927 | 731 | 504990 | -93.87 | 17.53 | 577.60 | 0.02 | 2.43 | 1584 |
| 2024-09-20 22:21:34.124 | MS1 | 121.4656679256 | 31.1446278097 | 731 | 504990 | -101.59 | -0.50 | 57.37 | 0.14 | 1.14 | 1581 |
| 2024-09-20 22:21:35.115 | MS1 | 121.4656672684 | 31.1446275163 | 731 | 504990 | -106.83 | 1.02 | 34.81 | 0.08 | 1.21 | 1593 |
| 2024-09-20 22:21:36.751 | MS1 | 121.4656636303 | 31.1446338353 | 731 | 504990 | -109.74 | 0.37 | 32.52 | 0.12 | 1.06 | 1565 |
| 2024-09-20 22:21:37.200 | MS1 | 121.4656646546 | 31.1446221422 | 731 | 504990 | -108.46 | -1.68 | 23.39 | 0.14 | 1.08 | 1583 |
| 2024-09-20 22:21:38.645 | MS1 | 121.4656759286 | 31.1446245365 | 731 | 504990 | -102.17 | -1.76 | 27.10 | 0.02 | 1.17 | 1580 |
| 2024-09-20 22:21:39.288 | MS1 | 121.4656666248 | 31.1446348195 | 731 | 504990 | -102.81 | -0.53 | 36.74 | 0.01 | 1.50 | 1579 |
| 2024-09-20 22:21:40.415 | MS1 | 121.4656619047 | 31.1446318548 | 731 | 504990 | -89.15 | 13.40 | 391.20 | 0.06 | 2.62 | 1599 |
| 2024-09-20 22:21:41.521 | MS1 | 121.4656752387 | 31.1446297393 | 731 | 504990 | -90.41 | 15.74 | 378.72 | 0.05 | 2.73 | 1561 |
| 2024-09-20 22:21:42.731 | MS1 | 121.4656772742 | 31.1446239815 | 731 | 504990 | -87.19 | 13.40 | 440.60 | 0.11 | 2.83 | 1596 |

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
| 3220721 | 2 | 121.4751636253 | 31.1478242300 | 221 | 4 | 3 | 22.6 | TDD | 878 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3228913 | 4 | 121.4640781704 | 31.1483026512 | 130 | 3 | 11 | 44.9 | TDD | 731 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3238603 | 1 | 121.4667450024 | 31.1548669894 | 180 | 4 | 6 | 32.6 | TDD | 627 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3278962 | 3 | 121.4644576742 | 31.1516083122 | 194 | 15 | 6 | 28.6 | TDD | 123 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |

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
| 2024-09-20 22:21:31.600 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.624 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.727 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.727 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.925 | NREventA2 | measId:1;ServCellPCI:472;Se... |
| 2024-09-20 22:21:35.071 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3238603 | 1 | 16.0015 | 16.8521 | -116.0339 | 16.9602 | 123.3978 | 0.0112 | 0.0188 |
| 2024_09_20 22:00 | 3220721 | 2 | 11.2540 | 19.6195 | -114.8887 | 18.5257 | 186.4714 | 0.0130 | 0.0139 |
| 2024_09_20 22:00 | 3278962 | 3 | 13.2739 | 10.7785 | -116.5090 | 10.0732 | 99.7798 | 0.0041 | 0.0173 |
| 2024_09_20 22:00 | 3228913 | 4 | 7.0197 | 14.4969 | -114.2994 | 15.0839 | 147.5441 | 0.1524 | 0.0162 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412850_609C839E | 504990 | 731 | -103.0 | 504990 | 878 | -109.6 | 504990 | 123 | -110.0 | 504990 | 627 |
| MR_1774412850_ECCEF0AB | 504990 | 731 | -101.3 | 504990 | 878 | -110.1 | 504990 | 123 | -112.3 | 504990 | 627 |
| MR_1774412850_0BFF3E35 | 504990 | 731 | -100.6 | 504990 | 878 | -109.2 | 504990 | 123 | -113.7 | 504990 | 627 |
| MR_1774412850_83B8F74C | 504990 | 731 | -100.0 | 504990 | 878 | -108.0 | 504990 | 123 | -112.9 | 504990 | 627 |
| MR_1774412850_B3BBCC31 | 504990 | 731 | -100.5 | 504990 | 878 | -108.5 | 504990 | 123 | -111.2 | 504990 | 627 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1322: `8645470e-c55...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `8645470e-c553-445c-962d-2680ffc706ab` |
| Tag | **single-answer** |
| 정답 | **C5** |
| C5 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3242121_1 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1322] topology](images/train_1322.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3241651_4
- `C2`: Add neighbor relationship between 3242121_1 and 3241651_4
- `C3`: Press down the tilt angle of 3242121_1 by 5 degrees
- `C4`: Decrease transmission power for 3242121_1
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3242121_1 **← 정답**
- `C6`: Insufficient data; more data is needed for judgment.
- `C7`: Decrease A3 Offset threshold for 3242121_1
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3241651_4
- `C9`: Press down the tilt angle  of 3241651_4 by 10 degrees
- `C10`: Lift the tilt angle  of 3241651_4 by 10 degrees
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3241651_4
- `C12`: Adjust the azimuth of 3242121_1 by 6 degrees
- `C13`: Decrease transmission power for 3241651_4
- `C14`: Adjust the azimuth of 3241651_4 by 50 degrees
- `C15`: Increase A3 Offset threshold for 3241651_4
- `C16`: Increase transmission power for 3242121_1
- `C17`: Increase A3 Offset threshold for 3242121_1
- `C18`: Lift the tilt angle of 3242121_1 by 5 degrees
- `C19`: Decrease A3 Offset threshold for 3241651_4
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3242121_1
- `C21`: Add neighbor relationship between 3220253_3 and 3241651_4
- `C22`: Check test server and transmission issues

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.699 | MS1 | 121.4656684669 | 31.1446367836 | 408 | 504990 | -88.31 | 15.62 | 491.26 | 0.14 | 2.39 | 1599 |
| 2024-09-20 22:21:32.534 | MS1 | 121.4656769023 | 31.1446363514 | 408 | 504990 | -91.22 | 12.36 | 568.30 | 0.12 | 2.53 | 1573 |
| 2024-09-20 22:21:33.981 | MS1 | 121.4656756371 | 31.1446274140 | 408 | 504990 | -87.15 | 13.17 | 350.10 | 0.15 | 2.73 | 1598 |
| 2024-09-20 22:21:34.342 | MS1 | 121.4656767319 | 31.1446355910 | 408 | 504990 | -87.56 | 12.13 | 45.60 | 0.57 | 2.89 | 694 |
| 2024-09-20 22:21:35.743 | MS1 | 121.4656741683 | 31.1446206707 | 408 | 504990 | -85.37 | 13.02 | 81.94 | 0.50 | 2.64 | 699 |
| 2024-09-20 22:21:36.752 | MS1 | 121.4656774264 | 31.1446257078 | 408 | 504990 | -87.74 | 15.60 | 92.18 | 0.70 | 2.60 | 647 |
| 2024-09-20 22:21:37.133 | MS1 | 121.4656660534 | 31.1446365269 | 408 | 504990 | -90.35 | 7.26 | 56.84 | 0.59 | 2.68 | 547 |
| 2024-09-20 22:21:38.848 | MS1 | 121.4656671320 | 31.1446192402 | 408 | 504990 | -91.41 | 11.17 | 96.33 | 0.51 | 2.82 | 575 |
| 2024-09-20 22:21:39.646 | MS1 | 121.4656727991 | 31.1446281795 | 408 | 504990 | -90.77 | 8.57 | 67.30 | 0.51 | 2.14 | 527 |
| 2024-09-20 22:21:40.705 | MS1 | 121.4656697234 | 31.1446203289 | 408 | 504990 | -93.87 | 8.26 | 336.11 | 0.11 | 2.24 | 1582 |
| 2024-09-20 22:21:41.897 | MS1 | 121.4656721153 | 31.1446216982 | 408 | 504990 | -93.11 | 9.32 | 576.26 | 0.01 | 2.64 | 1585 |
| 2024-09-20 22:21:42.233 | MS1 | 121.4656722985 | 31.1446252525 | 408 | 504990 | -90.12 | 11.04 | 539.10 | 0.15 | 2.93 | 1577 |

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
| 3220253 | 3 | 121.4743449352 | 31.1498122575 | 303 | 12 | 2 | 35.8 | TDD | 829 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3241651 | 4 | 121.4667335118 | 31.1536074194 | 130 | 12 | 8 | 45.5 | TDD | 807 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3242121 | 1 | 121.4710152274 | 31.1441742688 | 282 | 1 | 6 | 35.4 | TDD | 408 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3266948 | 2 | 121.4698825779 | 31.1462923918 | 104 | 8 | 4 | 33.8 | TDD | 689 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |

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
| 2024-09-20 22:21:30.863 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.887 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:30.997 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.997 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.681 | NREventA3 | measId:2;ServCellPCI:1006;S... |
| 2024-09-20 22:21:37.921 | NRHandoverAttempt | SourcePCI:1006;SourceNR-ARF... |
| 2024-09-20 22:21:37.956 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.966 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.101 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.101 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3242121 | 1 | 8.3567 | 11.1971 | -116.0064 | 7.8648 | 123.1994 | 0.0019 | 0.0097 |
| 2024_09_20 22:00 | 3266948 | 2 | 19.7163 | 9.7544 | -117.4155 | 11.0073 | 112.0996 | 0.0176 | 0.0128 |
| 2024_09_20 22:00 | 3220253 | 3 | 6.0886 | 13.2194 | -114.2673 | 18.6287 | 85.3085 | 0.0126 | 0.0117 |
| 2024_09_20 22:00 | 3241651 | 4 | 14.2802 | 13.9191 | -117.5189 | 17.9442 | 99.5319 | 0.0199 | 0.0053 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413985_A083014B | 504990 | 408 | -86.3 | 504990 | 807 | -91.4 | 504990 | 829 | -97.4 | 504990 | 689 |
| MR_1774413985_AD8753CC | 504990 | 408 | -89.2 | 504990 | 807 | -91.4 | 504990 | 829 | -96.4 | 504990 | 689 |
| MR_1774413985_D08D0135 | 504990 | 408 | -88.7 | 504990 | 807 | -92.2 | 504990 | 829 | -95.1 | 504990 | 689 |
| MR_1774413985_B41EA034 | 504990 | 408 | -87.5 | 504990 | 807 | -91.6 | 504990 | 829 | -95.8 | 504990 | 689 |
| MR_1774413985_22872235 | 504990 | 408 | -87.8 | 504990 | 807 | -89.2 | 504990 | 829 | -94.5 | 504990 | 689 |
| MR_1774413985_E6D82DE0 | 504990 | 408 | -89.3 | 504990 | 807 | -90.4 | 504990 | 829 | -98.0 | 504990 | 689 |
| MR_1774413985_525FCC57 | 504990 | 408 | -88.9 | 504990 | 807 | -89.4 | 504990 | 829 | -95.3 | 504990 | 689 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1323: `2b39630c-9ca...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `2b39630c-9ca5-4a37-973b-c49367d359eb` |
| Tag | **single-answer** |
| 정답 | **C14** |
| C14 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1323] topology](images/train_1323.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3243865_4
- `C2`: Increase transmission power for 3271714_2
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3243865_4
- `C4`: Increase transmission power for 3243865_4
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3271714_2
- `C6`: Lift the tilt angle  of 3243865_4 by 10 degrees
- `C7`: Decrease A3 Offset threshold for 3271714_2
- `C8`: Press down the tilt angle of 3271714_2 by 5 degrees
- `C9`: Insufficient data; more data is needed for judgment.
- `C10`: Decrease A3 Offset threshold for 3243865_4
- `C11`: Press down the tilt angle  of 3243865_4 by 10 degrees
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3271714_2
- `C13`: Add neighbor relationship between 3271714_2 and 3243865_4
- `C14`: Check test server and transmission issues **← 정답**
- `C15`: Decrease transmission power for 3271714_2
- `C16`: Increase A3 Offset threshold for 3271714_2
- `C17`: Decrease transmission power for 3243865_4
- `C18`: Add neighbor relationship between 3228699_3 and 3243865_4
- `C19`: Adjust the azimuth of 3271714_2 by 49 degrees
- `C20`: Increase A3 Offset threshold for 3243865_4
- `C21`: Lift the tilt angle of 3271714_2 by 5 degrees
- `C22`: Adjust the azimuth of 3243865_4 by 50 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.695 | MS1 | 121.4656766707 | 31.1446289653 | 565 | 504990 | -88.27 | 17.18 | 494.13 | 0.17 | 2.25 | 1566 |
| 2024-09-20 22:21:32.925 | MS1 | 121.4656640183 | 31.1446272894 | 565 | 504990 | -91.85 | 15.55 | 511.88 | 0.04 | 2.72 | 1572 |
| 2024-09-20 22:21:33.441 | MS1 | 121.4656618361 | 31.1446301936 | 565 | 504990 | -90.80 | 15.56 | 422.91 | 0.02 | 2.36 | 1598 |
| 2024-09-20 22:21:34.952 | MS1 | 121.4656767029 | 31.1446217953 | 565 | 504990 | -85.20 | 13.49 | 53.00 | 0.14 | 2.26 | 360 |
| 2024-09-20 22:21:35.493 | MS1 | 121.4656735972 | 31.1446280732 | 565 | 504990 | -90.56 | 16.63 | 93.25 | 0.10 | 2.66 | 497 |
| 2024-09-20 22:21:36.309 | MS1 | 121.4656598774 | 31.1446185146 | 565 | 504990 | -91.91 | 12.31 | 85.04 | 0.12 | 2.03 | 323 |
| 2024-09-20 22:21:37.209 | MS1 | 121.4656669736 | 31.1446253648 | 565 | 504990 | -92.61 | 10.56 | 61.42 | 0.05 | 2.20 | 478 |
| 2024-09-20 22:21:38.892 | MS1 | 121.4656625702 | 31.1446249270 | 565 | 504990 | -89.37 | 12.15 | 83.10 | 0.02 | 2.25 | 395 |
| 2024-09-20 22:21:39.174 | MS1 | 121.4656606270 | 31.1446225351 | 565 | 504990 | -91.80 | 10.52 | 62.62 | 0.03 | 2.42 | 402 |
| 2024-09-20 22:21:40.548 | MS1 | 121.4656641350 | 31.1446372759 | 565 | 504990 | -93.54 | 8.93 | 377.53 | 0.12 | 2.62 | 1571 |
| 2024-09-20 22:21:41.675 | MS1 | 121.4656581404 | 31.1446349909 | 565 | 504990 | -90.30 | 10.25 | 459.84 | 0.16 | 2.56 | 1595 |
| 2024-09-20 22:21:42.883 | MS1 | 121.4656754044 | 31.1446248166 | 565 | 504990 | -91.24 | 7.27 | 454.78 | 0.19 | 2.73 | 1571 |

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
| 3228699 | 3 | 121.4725037586 | 31.1503366298 | 199 | 0 | 0 | 49.9 | TDD | 533 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3243865 | 4 | 121.4651730198 | 31.1491498866 | 103 | 8 | 2 | 20.7 | TDD | 791 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3265626 | 1 | 121.4703611460 | 31.1470977453 | 126 | 3 | 8 | 17.9 | TDD | 793 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3271714 | 2 | 121.4640576257 | 31.1479895708 | 207 | 0 | 5 | 37.8 | TDD | 565 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |

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
| 2024-09-20 22:21:31.558 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.577 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.710 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.710 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.381 | NREventA3 | measId:2;ServCellPCI:603;Se... |
| 2024-09-20 22:21:38.621 | NRHandoverAttempt | SourcePCI:603;SourceNR-ARFC... |
| 2024-09-20 22:21:38.662 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.675 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.791 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.791 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3265626 | 1 | 14.3545 | 16.8817 | -115.6681 | 11.9637 | 112.5436 | 0.0045 | 0.0175 |
| 2024_09_20 22:00 | 3271714 | 2 | 11.1214 | 19.5754 | -114.9530 | 6.2409 | 105.3186 | 0.0077 | 0.0140 |
| 2024_09_20 22:00 | 3228699 | 3 | 9.2967 | 19.5331 | -117.3699 | 7.8282 | 134.4773 | 0.0144 | 0.0125 |
| 2024_09_20 22:00 | 3243865 | 4 | 9.8653 | 12.6691 | -115.7006 | 17.1951 | 194.0587 | 0.0181 | 0.0133 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413220_A887C545 | 504990 | 565 | -84.1 | 504990 | 791 | -89.5 | 504990 | 533 | -96.2 | 504990 | 793 |
| MR_1774413220_4E2A41A7 | 504990 | 565 | -85.6 | 504990 | 791 | -88.0 | 504990 | 533 | -97.3 | 504990 | 793 |
| MR_1774413220_3B2539F3 | 504990 | 565 | -84.9 | 504990 | 791 | -90.0 | 504990 | 533 | -96.6 | 504990 | 793 |
| MR_1774413220_68850A88 | 504990 | 565 | -85.8 | 504990 | 791 | -87.6 | 504990 | 533 | -96.6 | 504990 | 793 |
| MR_1774413220_85F97B68 | 504990 | 565 | -86.4 | 504990 | 791 | -87.8 | 504990 | 533 | -96.9 | 504990 | 793 |
| MR_1774413220_F5DA78BA | 504990 | 565 | -84.8 | 504990 | 791 | -89.1 | 504990 | 533 | -98.3 | 504990 | 793 |
| MR_1774413220_68D77C96 | 504990 | 565 | -83.7 | 504990 | 791 | -88.2 | 504990 | 533 | -99.3 | 504990 | 793 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1324: `f700f740-815...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `f700f740-8158-4522-a385-64e8a8f19b91` |
| Tag | **single-answer** |
| 정답 | **C6** |
| C6 의미 | Lift the tilt angle  of 3212637_4 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1324] topology](images/train_1324.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment.
- `C2`: Adjust the azimuth of 3214119_1 by 18 degrees
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3225374_2
- `C4`: Decrease A3 Offset threshold for 3225374_2
- `C5`: Increase A3 Offset threshold for 3214119_1
- `C6`: Lift the tilt angle  of 3212637_4 by 10 degrees **← 정답**
- `C7`: Add neighbor relationship between 3212637_4 and 3225374_2
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3225374_2
- `C9`: Decrease transmission power for 3214119_1
- `C10`: Press down the tilt angle  of 3212637_4 by 10 degrees
- `C11`: Lift the tilt angle of 3214119_1 by 4 degrees
- `C12`: Decrease transmission power for 3225374_2
- `C13`: Decrease A3 Offset threshold for 3214119_1
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3214119_1
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3214119_1
- `C16`: Check test server and transmission issues
- `C17`: Increase A3 Offset threshold for 3225374_2
- `C18`: Increase transmission power for 3214119_1
- `C19`: Adjust the azimuth of 3212637_4 by 50 degrees
- `C20`: Increase transmission power for 3225374_2
- `C21`: Press down the tilt angle of 3214119_1 by 4 degrees
- `C22`: Add neighbor relationship between 3214119_1 and 3225374_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.613 | MS1 | 121.4656589171 | 31.1446335590 | 294 | 504990 | -90.04 | 16.95 | 462.03 | 0.15 | 2.13 | 1590 |
| 2024-09-20 22:21:32.361 | MS1 | 121.4656711608 | 31.1446199331 | 294 | 504990 | -85.34 | 14.16 | 450.29 | 0.08 | 2.75 | 1575 |
| 2024-09-20 22:21:33.783 | MS1 | 121.4656728860 | 31.1446193278 | 294 | 504990 | -91.95 | 13.09 | 360.82 | 0.04 | 2.28 | 1579 |
| 2024-09-20 22:21:34.396 | MS1 | 121.4656735530 | 31.1446206954 | 294 | 504990 | -90.12 | 12.39 | 83.59 | 0.05 | 2.18 | 1600 |
| 2024-09-20 22:21:35.708 | MS1 | 121.4656612310 | 31.1446320792 | 294 | 504990 | -86.63 | 16.65 | 64.10 | 0.04 | 2.24 | 1597 |
| 2024-09-20 22:21:36.788 | MS1 | 121.4656770326 | 31.1446342269 | 294 | 504990 | -88.74 | 15.75 | 80.17 | 0.09 | 2.37 | 1597 |
| 2024-09-20 22:21:37.811 | MS1 | 121.4656654326 | 31.1446345745 | 294 | 504990 | -91.79 | 12.07 | 95.87 | 0.18 | 2.21 | 1590 |
| 2024-09-20 22:21:38.174 | MS1 | 121.4656715624 | 31.1446292426 | 294 | 504990 | -93.67 | 9.42 | 61.43 | 0.15 | 2.39 | 1596 |
| 2024-09-20 22:21:39.728 | MS1 | 121.4656692076 | 31.1446245516 | 294 | 504990 | -91.27 | 8.57 | 71.69 | 0.02 | 2.39 | 1590 |
| 2024-09-20 22:21:40.771 | MS1 | 121.4656605266 | 31.1446339180 | 294 | 504990 | -93.40 | 8.21 | 459.21 | 0.15 | 2.86 | 1588 |
| 2024-09-20 22:21:41.510 | MS1 | 121.4656712025 | 31.1446366257 | 294 | 504990 | -89.14 | 11.62 | 499.99 | 0.09 | 2.94 | 1584 |
| 2024-09-20 22:21:42.893 | MS1 | 121.4656611278 | 31.1446193153 | 294 | 504990 | -92.59 | 10.13 | 528.99 | 0.08 | 2.24 | 1577 |

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
| 3212637 | 4 | 121.4670882288 | 31.1498185084 | 47 | 4 | 10 | 26.1 | TDD | 157 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3214119 | 1 | 121.4710826623 | 31.1531783561 | 226 | 2 | 7 | 41.4 | TDD | 294 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3217795 | 3 | 121.4724439282 | 31.1454085692 | 192 | 4 | 12 | 20.1 | TDD | 54 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3225374 | 2 | 121.4751880350 | 31.1473009425 | 51 | 10 | 9 | 34.6 | TDD | 365 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

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
| 2024-09-20 22:21:31.556 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.571 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.709 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.709 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.390 | NREventA3 | measId:2;ServCellPCI:878;Se... |
| 2024-09-20 22:21:38.630 | NRHandoverAttempt | SourcePCI:878;SourceNR-ARFC... |
| 2024-09-20 22:21:38.662 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.673 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.822 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.822 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3214119 | 1 | 88.7445 | 94.6344 | -117.6597 | 17.3904 | 123.8279 | 0.0179 | 0.0139 |
| 2024_09_20 22:00 | 3225374 | 2 | 9.8116 | 8.6113 | -117.4253 | 7.7841 | 104.8609 | 0.0174 | 0.0140 |
| 2024_09_20 22:00 | 3217795 | 3 | 19.5585 | 10.0684 | -115.7673 | 18.0854 | 80.0584 | 0.0084 | 0.0088 |
| 2024_09_20 22:00 | 3212637 | 4 | 6.0053 | 8.8790 | -115.7451 | 18.1179 | 164.2115 | 0.0037 | 0.0139 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415246_5DD1FDE9 | 504990 | 294 | -91.7 | 504990 | 365 | -98.0 | 504990 | 157 | -101.9 | 504990 | 54 |
| MR_1774415246_2A6C798D | 504990 | 294 | -90.2 | 504990 | 365 | -97.3 | 504990 | 157 | -99.6 | 504990 | 54 |
| MR_1774415246_5137AA60 | 504990 | 294 | -90.7 | 504990 | 365 | -96.3 | 504990 | 157 | -98.5 | 504990 | 54 |
| MR_1774415246_1EE89831 | 504990 | 294 | -89.0 | 504990 | 365 | -96.7 | 504990 | 157 | -98.9 | 504990 | 54 |
| MR_1774415246_81123F4C | 504990 | 294 | -89.9 | 504990 | 365 | -96.9 | 504990 | 157 | -102.3 | 504990 | 54 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1325: `94cbd7c0-c41...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `94cbd7c0-c419-4439-9760-72e4cb53993b` |
| Tag | **single-answer** |
| 정답 | **C6** |
| C6 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3213875_2 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1325] topology](images/train_1325.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3225440_1 by 32 degrees
- `C2`: Decrease A3 Offset threshold for 3225440_1
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3225440_1
- `C4`: Lift the tilt angle of 3213875_2 by 3 degrees
- `C5`: Press down the tilt angle of 3213875_2 by 3 degrees
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3213875_2 **← 정답**
- `C7`: Decrease A3 Offset threshold for 3213875_2
- `C8`: Increase A3 Offset threshold for 3225440_1
- `C9`: Lift the tilt angle  of 3225440_1 by 5 degrees
- `C10`: Decrease transmission power for 3213875_2
- `C11`: Add neighbor relationship between 3247309_9 and 3225440_1
- `C12`: Check test server and transmission issues
- `C13`: Adjust the azimuth of 3213875_2 by 43 degrees
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3225440_1
- `C15`: Press down the tilt angle  of 3225440_1 by 5 degrees
- `C16`: Increase transmission power for 3213875_2
- `C17`: Add neighbor relationship between 3213875_2 and 3225440_1
- `C18`: Increase transmission power for 3225440_1
- `C19`: Insufficient data; more data is needed for judgment.
- `C20`: Increase A3 Offset threshold for 3213875_2
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3213875_2
- `C22`: Decrease transmission power for 3225440_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.192 | MS1 | 121.4656749232 | 31.1446367485 | 458 | 504990 | -93.24 | 10.99 | 539.03 | 0.03 | 2.01 | 1595 |
| 2024-09-20 22:21:32.174 | MS1 | 121.4656616665 | 31.1446224039 | 912 | 504990 | -95.46 | 12.12 | 548.80 | 0.07 | 2.19 | 1597 |
| 2024-09-20 22:21:33.855 | MS1 | 121.4656725375 | 31.1446333064 | 336 | 504990 | -93.85 | 10.52 | 515.72 | 0.18 | 2.41 | 1591 |
| 2024-09-20 22:21:34.566 | MS1 | 121.4656728329 | 31.1446366735 | 844 | 152650 | -89.78 | 5.12 | 92.56 | 0.12 | 1.67 | 950 |
| 2024-09-20 22:21:35.325 | MS1 | 121.4656643294 | 31.1446301628 | 547 | 152650 | -91.26 | 3.92 | 49.39 | 0.05 | 1.83 | 993 |
| 2024-09-20 22:21:36.479 | MS1 | 121.4656770383 | 31.1446339387 | 170 | 152650 | -90.42 | 2.31 | 80.61 | 0.09 | 1.63 | 947 |
| 2024-09-20 22:21:37.917 | MS1 | 121.4656643847 | 31.1446247888 | 222 | 152650 | -94.38 | 3.97 | 86.94 | 0.08 | 1.69 | 997 |
| 2024-09-20 22:21:38.616 | MS1 | 121.4656612889 | 31.1446183553 | 844 | 152650 | -94.45 | 5.83 | 86.56 | 0.16 | 1.91 | 944 |
| 2024-09-20 22:21:39.551 | MS1 | 121.4656752124 | 31.1446347967 | 547 | 152650 | -90.41 | 7.59 | 66.70 | 0.01 | 1.75 | 966 |
| 2024-09-20 22:21:40.787 | MS1 | 121.4656715878 | 31.1446358054 | 170 | 152650 | -95.31 | 7.87 | 58.32 | 0.07 | 2.10 | 1583 |
| 2024-09-20 22:21:41.974 | MS1 | 121.4656766401 | 31.1446195913 | 222 | 152650 | -87.48 | 7.29 | 60.17 | 0.13 | 2.98 | 1577 |
| 2024-09-20 22:21:42.872 | MS1 | 121.4656717779 | 31.1446184101 | 844 | 152650 | -90.89 | 7.48 | 72.33 | 0.11 | 2.33 | 1581 |

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
| 3213875 | 2 | 121.4696206283 | 31.1541187846 | 243 | 2 | 5 | 25.6 | TDD | 458 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3217186 | 5 | 121.4747415293 | 31.1492398186 | 135 | 4 | 3 | 20.7 | TDD | 757 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3220976 | 3 | 121.4691298579 | 31.1512584308 | 18 | 6 | 6 | 16.7 | TDD | 912 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3221953 | 4 | 121.4751288304 | 31.1475185453 | 122 | 5 | 4 | 29.9 | TDD | 336 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3225440 | 1 | 121.4724326767 | 31.1450026545 | 234 | 2 | 10 | 29.7 | TDD | 708 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3236359 | 7 | 121.4758511761 | 31.1486285526 | 265 | 11 | 9 | 3.8 | FDD | 547 | n1 | 152650 | 30M | 4T4R | 15 | 152650 |
| 3247309 | 9 | 121.4725688243 | 31.1481712541 | 241 | 13 | 2 | 19.2 | FDD | 170 | n1 | 152650 | 30M | 4T4R | 21 | 152650 |
| 3248796 | 6 | 121.4650030790 | 31.1544108936 | 285 | 15 | 12 | 8.3 | TDD | 665 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3250322 | 8 | 121.4737163230 | 31.1502607275 | 95 | 14 | 5 | 2.3 | FDD | 229 | n1 | 152650 | 30M | 4T4R | 24 | 152650 |
| 3251041 | 11 | 121.4669470066 | 31.1541308523 | 304 | 12 | 12 | 26.0 | FDD | 881 | n1 | 152650 | 30M | 4T4R | 11 | 152650 |
| 3260008 | 13 | 121.4660242136 | 31.1482183782 | 148 | 9 | 7 | 4.7 | FDD | 222 | n1 | 152650 | 30M | 4T4R | 29 | 152650 |
| 3260038 | 12 | 121.4705179636 | 31.1463331552 | 341 | 2 | 5 | 0.5 | FDD | 504 | n1 | 152650 | 30M | 4T4R | 21 | 152650 |
| 3272195 | 10 | 121.4668282128 | 31.1450165394 | 330 | 2 | 4 | 29.7 | FDD | 844 | n1 | 152650 | 30M | 4T4R | 12 | 152650 |

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
| 2024-09-20 22:21:30.948 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.970 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.103 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.103 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.814 | NREventA2 | measId:1;ServCellPCI:638;Se... |
| 2024-09-20 22:21:34.964 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.184 | NREventA5 | measId:3;ServCellPCI:638;Se... |
| 2024-09-20 22:21:35.254 | NRHandoverAttempt | SourcePCI:638;SourceNR-ARFC... |
| 2024-09-20 22:21:35.290 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.303 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:35.453 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.453 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3225440 | 1 | 7.2513 | 17.3189 | -117.0043 | 8.2126 | 179.0021 | 0.0133 | 0.0061 |
| 2024_09_20 22:00 | 3213875 | 2 | 16.1459 | 9.4799 | -115.3691 | 14.4434 | 123.5357 | 0.0144 | 0.0141 |
| 2024_09_20 22:00 | 3220976 | 3 | 13.5367 | 15.3123 | -114.5277 | 5.7387 | 139.1537 | 0.0073 | 0.0094 |
| 2024_09_20 22:00 | 3221953 | 4 | 13.1678 | 6.6073 | -114.7404 | 10.3293 | 159.2574 | 0.0026 | 0.0114 |
| 2024_09_20 22:00 | 3217186 | 5 | 8.9721 | 14.1016 | -117.7434 | 9.6581 | 106.9329 | 0.0101 | 0.0138 |
| 2024_09_20 22:00 | 3248796 | 6 | 16.1532 | 8.7185 | -116.6526 | 11.9348 | 101.7314 | 0.0183 | 0.0081 |
| 2024_09_20 22:00 | 3236359 | 7 | 13.3111 | 5.8507 | -115.9938 | 3.5157 | 58.2763 | 0.0125 | 0.0002 |
| 2024_09_20 22:00 | 3250322 | 8 | 15.3236 | 9.0262 | -115.4193 | 3.9482 | 54.3723 | 0.0132 | 0.0051 |
| 2024_09_20 22:00 | 3247309 | 9 | 18.5028 | 5.9592 | -115.5094 | 4.1995 | 40.6153 | 0.0062 | 0.0066 |
| 2024_09_20 22:00 | 3272195 | 10 | 19.0529 | 6.0062 | -116.0943 | 4.0592 | 47.7250 | 0.0154 | 0.0185 |
| 2024_09_20 22:00 | 3251041 | 11 | 15.8536 | 14.1803 | -114.3542 | 4.7681 | 35.0049 | 0.0149 | 0.0012 |
| 2024_09_20 22:00 | 3260038 | 12 | 14.5232 | 11.7086 | -116.1099 | 3.8892 | 30.5012 | 0.0010 | 0.0086 |
| 2024_09_20 22:00 | 3260008 | 13 | 16.3359 | 13.9652 | -117.7426 | 3.1628 | 37.9589 | 0.0152 | 0.0047 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412488_E7492DE6 | 152650 | 844 | -90.8 | 152650 | 229 | -99.1 | 152650 | 504 | -97.7 | 152650 | 881 |
| MR_1774412488_79E48308 | 504990 | 336 | -94.0 | 504990 | 708 | -90.3 | 504990 | 757 | -99.8 | 504990 | 665 |
| MR_1774412488_F83BBC66 | 504990 | 336 | -95.4 | 504990 | 708 | -91.8 | 504990 | 757 | -102.0 | 504990 | 665 |
| MR_1774412488_2954E2CF | 504990 | 336 | -92.6 | 504990 | 708 | -91.9 | 504990 | 757 | -102.3 | 504990 | 665 |
| MR_1774412488_97879F6E | 152650 | 844 | -91.0 | 152650 | 229 | -96.1 | 152650 | 504 | -97.8 | 152650 | 881 |
| MR_1774412488_97819476 | 152650 | 844 | -91.7 | 152650 | 229 | -96.2 | 152650 | 504 | -97.5 | 152650 | 881 |
| MR_1774412488_7EBD6E72 | 152650 | 844 | -88.6 | 152650 | 229 | -97.8 | 152650 | 504 | -99.1 | 152650 | 881 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1326: `43b27ef1-26f...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `43b27ef1-26fa-4a9d-bb73-ae53082d0866` |
| Tag | **single-answer** |
| 정답 | **C5** |
| C5 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3225831_1 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1326] topology](images/train_1326.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3242891_3
- `C2`: Decrease transmission power for 3242891_3
- `C3`: Add neighbor relationship between 3239392_4 and 3242891_3
- `C4`: Increase A3 Offset threshold for 3242891_3
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3225831_1 **← 정답**
- `C6`: Increase transmission power for 3242891_3
- `C7`: Lift the tilt angle  of 3242891_3 by 10 degrees
- `C8`: Decrease transmission power for 3225831_1
- `C9`: Decrease A3 Offset threshold for 3225831_1
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3242891_3
- `C11`: Lift the tilt angle of 3225831_1 by 3 degrees
- `C12`: Increase transmission power for 3225831_1
- `C13`: Adjust the azimuth of 3225831_1 by 45 degrees
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Adjust the azimuth of 3242891_3 by 32 degrees
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3225831_1
- `C17`: Press down the tilt angle of 3225831_1 by 3 degrees
- `C18`: Press down the tilt angle  of 3242891_3 by 10 degrees
- `C19`: Check test server and transmission issues
- `C20`: Increase A3 Offset threshold for 3225831_1
- `C21`: Add neighbor relationship between 3225831_1 and 3242891_3
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3242891_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.505 | MS1 | 121.4656700709 | 31.1446268322 | 355 | 504990 | -88.81 | 13.43 | 315.97 | 0.05 | 2.53 | 1582 |
| 2024-09-20 22:21:32.408 | MS1 | 121.4656604188 | 31.1446232117 | 355 | 504990 | -90.86 | 12.89 | 324.77 | 0.15 | 2.08 | 1567 |
| 2024-09-20 22:21:33.943 | MS1 | 121.4656779901 | 31.1446342915 | 355 | 504990 | -91.30 | 13.63 | 584.99 | 0.13 | 2.22 | 1593 |
| 2024-09-20 22:21:34.720 | MS1 | 121.4656748177 | 31.1446310976 | 355 | 504990 | -91.96 | 13.42 | 104.04 | 0.70 | 2.78 | 619 |
| 2024-09-20 22:21:35.688 | MS1 | 121.4656595501 | 31.1446281168 | 355 | 504990 | -90.25 | 14.69 | 84.39 | 0.52 | 2.61 | 524 |
| 2024-09-20 22:21:36.332 | MS1 | 121.4656714784 | 31.1446199445 | 355 | 504990 | -85.11 | 16.75 | 89.35 | 0.65 | 2.27 | 641 |
| 2024-09-20 22:21:37.627 | MS1 | 121.4656716182 | 31.1446310432 | 355 | 504990 | -93.51 | 8.35 | 84.30 | 0.61 | 2.63 | 663 |
| 2024-09-20 22:21:38.288 | MS1 | 121.4656759906 | 31.1446193441 | 355 | 504990 | -92.38 | 8.14 | 63.87 | 0.50 | 2.13 | 539 |
| 2024-09-20 22:21:39.359 | MS1 | 121.4656634087 | 31.1446361470 | 355 | 504990 | -89.08 | 12.14 | 79.03 | 0.66 | 2.79 | 614 |
| 2024-09-20 22:21:40.539 | MS1 | 121.4656747167 | 31.1446257257 | 355 | 504990 | -91.27 | 9.59 | 382.35 | 0.11 | 2.56 | 1586 |
| 2024-09-20 22:21:41.992 | MS1 | 121.4656697759 | 31.1446299595 | 355 | 504990 | -89.58 | 12.90 | 548.55 | 0.19 | 2.15 | 1565 |
| 2024-09-20 22:21:42.723 | MS1 | 121.4656762621 | 31.1446184712 | 355 | 504990 | -90.33 | 7.46 | 358.72 | 0.12 | 2.70 | 1600 |

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
| 3223262 | 2 | 121.4710416651 | 31.1554459945 | 121 | 8 | 8 | 18.7 | TDD | 116 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3225831 | 1 | 121.4742430786 | 31.1531770341 | 266 | 2 | 6 | 15.5 | TDD | 355 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3239392 | 4 | 121.4646673126 | 31.1504657282 | 229 | 1 | 10 | 35.6 | TDD | 535 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3242891 | 3 | 121.4651235355 | 31.1527290467 | 145 | 15 | 6 | 21.8 | TDD | 807 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |

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
| 2024-09-20 22:21:31.098 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.121 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.250 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.250 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.956 | NREventA3 | measId:2;ServCellPCI:935;Se... |
| 2024-09-20 22:21:38.196 | NRHandoverAttempt | SourcePCI:935;SourceNR-ARFC... |
| 2024-09-20 22:21:38.231 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.242 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.361 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.361 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3225831 | 1 | 9.7088 | 16.5361 | -115.6063 | 11.2459 | 125.2609 | 0.0023 | 0.0028 |
| 2024_09_20 22:00 | 3223262 | 2 | 14.4908 | 6.7062 | -114.7920 | 13.4815 | 171.4926 | 0.0094 | 0.0056 |
| 2024_09_20 22:00 | 3242891 | 3 | 16.6213 | 9.8838 | -117.4535 | 7.3937 | 90.5580 | 0.0171 | 0.0193 |
| 2024_09_20 22:00 | 3239392 | 4 | 12.2500 | 11.2831 | -115.2315 | 5.7232 | 142.7651 | 0.0143 | 0.0185 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412410_C3DEA945 | 504990 | 355 | -88.8 | 504990 | 807 | -95.0 | 504990 | 535 | -98.3 | 504990 | 116 |
| MR_1774412410_8010DC7F | 504990 | 355 | -88.7 | 504990 | 807 | -95.2 | 504990 | 535 | -97.9 | 504990 | 116 |
| MR_1774412410_62E97B7F | 504990 | 355 | -90.9 | 504990 | 807 | -95.5 | 504990 | 535 | -95.6 | 504990 | 116 |
| MR_1774412410_D749E04A | 504990 | 355 | -91.1 | 504990 | 807 | -96.3 | 504990 | 535 | -97.3 | 504990 | 116 |
| MR_1774412410_205BA81B | 504990 | 355 | -91.5 | 504990 | 807 | -96.1 | 504990 | 535 | -96.4 | 504990 | 116 |
| MR_1774412410_6E23E0DB | 504990 | 355 | -89.1 | 504990 | 807 | -95.8 | 504990 | 535 | -97.3 | 504990 | 116 |
| MR_1774412410_485D965F | 504990 | 355 | -91.7 | 504990 | 807 | -97.3 | 504990 | 535 | -99.1 | 504990 | 116 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1327: `de4e627d-c0b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `de4e627d-c0bf-4dfb-a942-779b20542da0` |
| Tag | **single-answer** |
| 정답 | **C15** |
| C15 의미 | Add neighbor relationship between 3258049_2 and 3221484_1 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1327] topology](images/train_1327.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3221484_1
- `C2`: Decrease A3 Offset threshold for 3258049_2
- `C3`: Adjust the azimuth of 3258049_2 by 50 degrees
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3258049_2
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3221484_1
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3221484_1
- `C7`: Increase transmission power for 3258049_2
- `C8`: Press down the tilt angle of 3258049_2 by 4 degrees
- `C9`: Lift the tilt angle of 3258049_2 by 4 degrees
- `C10`: Insufficient data; more data is needed for judgment.
- `C11`: Press down the tilt angle  of 3221484_1 by 6 degrees
- `C12`: Decrease transmission power for 3221484_1
- `C13`: Check test server and transmission issues
- `C14`: Lift the tilt angle  of 3221484_1 by 6 degrees
- `C15`: Add neighbor relationship between 3258049_2 and 3221484_1 **← 정답**
- `C16`: Add neighbor relationship between 3256636_4 and 3221484_1
- `C17`: Decrease A3 Offset threshold for 3221484_1
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3258049_2
- `C19`: Decrease transmission power for 3258049_2
- `C20`: Increase A3 Offset threshold for 3258049_2
- `C21`: Increase transmission power for 3221484_1
- `C22`: Adjust the azimuth of 3221484_1 by 18 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.265 | MS1 | 121.4656711849 | 31.1446246948 | 196 | 504990 | -82.96 | 16.96 | 454.30 | 0.04 | 2.34 | 1578 |
| 2024-09-20 22:21:32.164 | MS1 | 121.4656770814 | 31.1446189433 | 196 | 504990 | -77.19 | 14.52 | 567.22 | 0.12 | 2.90 | 1590 |
| 2024-09-20 22:21:33.382 | MS1 | 121.4656720686 | 31.1446227042 | 196 | 504990 | -84.86 | 17.72 | 363.21 | 0.15 | 2.56 | 1594 |
| 2024-09-20 22:21:34.686 | MS1 | 121.4656697336 | 31.1446246374 | 196 | 504990 | -86.74 | -3.81 | 30.55 | 0.07 | 1.45 | 1594 |
| 2024-09-20 22:21:35.629 | MS1 | 121.4656593013 | 31.1446283970 | 196 | 504990 | -86.26 | -2.01 | 33.42 | 0.14 | 1.17 | 1579 |
| 2024-09-20 22:21:36.728 | MS1 | 121.4656651837 | 31.1446204603 | 196 | 504990 | -94.04 | -1.30 | 59.55 | 0.20 | 1.33 | 1576 |
| 2024-09-20 22:21:37.115 | MS1 | 121.4656769797 | 31.1446363679 | 196 | 504990 | -93.91 | -3.83 | 48.92 | 0.15 | 1.17 | 1579 |
| 2024-09-20 22:21:38.774 | MS1 | 121.4656770774 | 31.1446181968 | 196 | 504990 | -75.03 | 17.87 | 351.95 | 0.10 | 1.42 | 1568 |
| 2024-09-20 22:21:39.853 | MS1 | 121.4656688480 | 31.1446208643 | 196 | 504990 | -75.44 | 13.21 | 349.42 | 0.18 | 1.02 | 1571 |
| 2024-09-20 22:21:40.866 | MS1 | 121.4656629634 | 31.1446258007 | 196 | 504990 | -84.27 | 15.83 | 589.04 | 0.19 | 2.75 | 1576 |
| 2024-09-20 22:21:41.667 | MS1 | 121.4656673689 | 31.1446261520 | 196 | 504990 | -77.13 | 14.61 | 579.42 | 0.07 | 2.76 | 1595 |
| 2024-09-20 22:21:42.723 | MS1 | 121.4656652310 | 31.1446297824 | 196 | 504990 | -81.96 | 17.33 | 460.80 | 0.07 | 2.13 | 1570 |

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
| 3221484 | 1 | 121.4736851827 | 31.1507057967 | 246 | 4 | 5 | 33.6 | TDD | 647 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3240531 | 3 | 121.4727807416 | 31.1447627291 | 61 | 4 | 2 | 47.3 | TDD | 509 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3256636 | 4 | 121.4734905528 | 31.1525558535 | 303 | 13 | 12 | 40.3 | TDD | 429 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3258049 | 2 | 121.4730832076 | 31.1553966981 | 94 | 3 | 1 | 21.0 | TDD | 196 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |

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
| 2024-09-20 22:21:31.515 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.539 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.646 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.646 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.380 | NREventA3 | measId:2;ServCellPCI:507;Se... |
| 2024-09-20 22:21:36.380 | NREventA3 | measId:2;ServCellPCI:507;Se... |
| 2024-09-20 22:21:37.380 | NREventA3 | measId:2;ServCellPCI:507;Se... |
| 2024-09-20 22:21:39.880 | NRRRCReestablishAttempt | PCI:507 |
| 2024-09-20 22:21:39.891 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.903 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:40.024 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:40.024 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3221484 | 1 | 17.2959 | 9.7142 | -114.2394 | 14.6333 | 145.7818 | 0.0077 | 0.0113 |
| 2024_09_20 22:00 | 3258049 | 2 | 19.9820 | 13.5630 | -115.0178 | 14.8797 | 173.1860 | 0.0005 | 0.1334 |
| 2024_09_20 22:00 | 3240531 | 3 | 18.1320 | 11.5791 | -116.5870 | 10.6804 | 192.4706 | 0.0167 | 0.0078 |
| 2024_09_20 22:00 | 3256636 | 4 | 7.5301 | 16.9784 | -116.1588 | 15.9708 | 155.7059 | 0.0145 | 0.0086 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412311_C59300AE | 504990 | 647 | -82.4 | 504990 | 196 | -87.5 | 504990 | 429 | -84.9 | 504990 | 509 |
| MR_1774412311_D092E893 | 504990 | 196 | -85.3 | 504990 | 647 | -80.0 | 504990 | 429 | -87.5 | 504990 | 509 |
| MR_1774412311_DBAE5C64 | 504990 | 647 | -80.0 | 504990 | 196 | -87.8 | 504990 | 429 | -87.8 | 504990 | 509 |
| MR_1774412311_93A50CD3 | 504990 | 647 | -79.5 | 504990 | 196 | -86.4 | 504990 | 429 | -88.0 | 504990 | 509 |
| MR_1774412311_D8BF893D | 504990 | 647 | -80.8 | 504990 | 196 | -88.5 | 504990 | 429 | -87.2 | 504990 | 509 |
| MR_1774412311_6081B377 | 504990 | 196 | -86.1 | 504990 | 647 | -82.7 | 504990 | 429 | -84.5 | 504990 | 509 |
| MR_1774412311_ECDB12F5 | 504990 | 647 | -82.8 | 504990 | 196 | -86.3 | 504990 | 429 | -87.8 | 504990 | 509 |
| MR_1774412311_38865AE7 | 504990 | 647 | -80.5 | 504990 | 196 | -87.6 | 504990 | 429 | -87.1 | 504990 | 509 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1328: `4c344670-53a...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `4c344670-53a8-4eef-a402-130f54b59b01` |
| Tag | **single-answer** |
| 정답 | **C18** |
| C18 의미 | Decrease A3 Offset threshold for 3262489_3 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1328] topology](images/train_1328.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3262489_3
- `C2`: Lift the tilt angle  of 3279324_2 by 7 degrees
- `C3`: Press down the tilt angle of 3262489_3 by 10 degrees
- `C4`: Add neighbor relationship between 3262489_3 and 3279324_2
- `C5`: Insufficient data; more data is needed for judgment.
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3279324_2
- `C7`: Decrease A3 Offset threshold for 3279324_2
- `C8`: Increase transmission power for 3262489_3
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3279324_2
- `C10`: Press down the tilt angle  of 3279324_2 by 7 degrees
- `C11`: Check test server and transmission issues
- `C12`: Increase transmission power for 3279324_2
- `C13`: Decrease transmission power for 3262489_3
- `C14`: Adjust the azimuth of 3262489_3 by 47 degrees
- `C15`: Lift the tilt angle of 3262489_3 by 10 degrees
- `C16`: Increase A3 Offset threshold for 3279324_2
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3262489_3
- `C18`: Decrease A3 Offset threshold for 3262489_3 **← 정답**
- `C19`: Decrease transmission power for 3279324_2
- `C20`: Add neighbor relationship between 3272399_1 and 3279324_2
- `C21`: Adjust the azimuth of 3279324_2 by 50 degrees
- `C22`: Increase A3 Offset threshold for 3262489_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.981 | MS1 | 121.4656699601 | 31.1446334808 | 541 | 504990 | -75.13 | 16.16 | 449.96 | 0.14 | 2.71 | 1563 |
| 2024-09-20 22:21:32.299 | MS1 | 121.4656628545 | 31.1446295607 | 541 | 504990 | -79.54 | 13.58 | 526.70 | 0.11 | 2.39 | 1568 |
| 2024-09-20 22:21:33.704 | MS1 | 121.4656697241 | 31.1446196104 | 541 | 504990 | -77.05 | 16.35 | 397.10 | 0.16 | 2.20 | 1571 |
| 2024-09-20 22:21:34.648 | MS1 | 121.4656701860 | 31.1446222877 | 541 | 504990 | -84.56 | -0.70 | 52.36 | 0.09 | 1.30 | 1568 |
| 2024-09-20 22:21:35.854 | MS1 | 121.4656733469 | 31.1446247702 | 541 | 504990 | -88.11 | -3.14 | 51.61 | 0.15 | 1.15 | 1573 |
| 2024-09-20 22:21:36.360 | MS1 | 121.4656649484 | 31.1446362232 | 541 | 504990 | -92.59 | -3.71 | 52.28 | 0.17 | 1.11 | 1584 |
| 2024-09-20 22:21:37.486 | MS1 | 121.4656656808 | 31.1446350775 | 541 | 504990 | -92.81 | -3.89 | 47.55 | 0.08 | 1.46 | 1584 |
| 2024-09-20 22:21:38.492 | MS1 | 121.4656646378 | 31.1446359981 | 541 | 504990 | -85.75 | -3.33 | 26.56 | 0.15 | 1.27 | 1595 |
| 2024-09-20 22:21:39.936 | MS1 | 121.4656645319 | 31.1446233809 | 817 | 504990 | -76.85 | 17.75 | 255.69 | 0.17 | 1.32 | 1594 |
| 2024-09-20 22:21:40.371 | MS1 | 121.4656725186 | 31.1446369315 | 817 | 504990 | -80.99 | 14.65 | 396.92 | 0.09 | 2.23 | 1580 |
| 2024-09-20 22:21:41.969 | MS1 | 121.4656738074 | 31.1446183021 | 817 | 504990 | -82.91 | 14.53 | 479.35 | 0.09 | 2.71 | 1576 |
| 2024-09-20 22:21:42.210 | MS1 | 121.4656623092 | 31.1446254037 | 817 | 504990 | -83.75 | 13.15 | 472.89 | 0.13 | 2.35 | 1583 |

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
| 3258331 | 4 | 121.4751623605 | 31.1498123841 | 211 | 6 | 6 | 29.0 | TDD | 278 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3262489 | 3 | 121.4681354392 | 31.1447659972 | 219 | 8 | 11 | 43.9 | TDD | 541 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3272399 | 1 | 121.4728928049 | 31.1553697165 | 43 | 10 | 1 | 46.0 | TDD | 696 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3279324 | 2 | 121.4683306822 | 31.1472487109 | 304 | 1 | 11 | 42.8 | TDD | 817 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |

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
| 2024-09-20 22:21:31.175 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.199 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.341 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.341 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.026 | NREventA3 | measId:2;ServCellPCI:825;Se... |
| 2024-09-20 22:21:38.266 | NRHandoverAttempt | SourcePCI:825;SourceNR-ARFC... |
| 2024-09-20 22:21:38.307 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.321 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.431 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.431 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3272399 | 1 | 16.1400 | 5.4592 | -116.2352 | 5.6764 | 108.6684 | 0.0076 | 0.0048 |
| 2024_09_20 22:00 | 3279324 | 2 | 10.0444 | 16.0972 | -117.0759 | 19.6795 | 82.1724 | 0.0090 | 0.0061 |
| 2024_09_20 22:00 | 3262489 | 3 | 18.6577 | 7.4984 | -115.3943 | 14.6081 | 102.6257 | 0.0144 | 0.1322 |
| 2024_09_20 22:00 | 3258331 | 4 | 19.2346 | 13.7712 | -117.1511 | 17.5910 | 169.4902 | 0.0143 | 0.0139 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414175_243B53D3 | 504990 | 817 | -79.9 | 504990 | 541 | -83.3 | 504990 | 696 | -81.6 | 504990 | 278 |
| MR_1774414175_8CABE12B | 504990 | 541 | -85.1 | 504990 | 817 | -79.8 | 504990 | 696 | -78.1 | 504990 | 278 |
| MR_1774414175_4D8FDED9 | 504990 | 541 | -84.7 | 504990 | 817 | -80.3 | 504990 | 696 | -78.4 | 504990 | 278 |
| MR_1774414175_3AC4E8E4 | 504990 | 817 | -79.0 | 504990 | 541 | -83.4 | 504990 | 696 | -78.8 | 504990 | 278 |
| MR_1774414175_23B444C9 | 504990 | 817 | -77.2 | 504990 | 541 | -82.7 | 504990 | 696 | -79.7 | 504990 | 278 |
| MR_1774414175_660E4EFC | 504990 | 541 | -86.1 | 504990 | 817 | -78.5 | 504990 | 696 | -79.4 | 504990 | 278 |
| MR_1774414175_3C5A976B | 504990 | 541 | -83.4 | 504990 | 817 | -77.6 | 504990 | 696 | -78.2 | 504990 | 278 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1329: `603ea76f-9a9...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `603ea76f-9a9f-403d-94f2-41f3ed43581f` |
| Tag | **single-answer** |
| 정답 | **C13** |
| C13 의미 | Add neighbor relationship between 3268421_4 and 3235195_2 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1329] topology](images/train_1329.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3235195_2
- `C2`: Increase A3 Offset threshold for 3235195_2
- `C3`: Decrease A3 Offset threshold for 3235195_2
- `C4`: Adjust the azimuth of 3268421_4 by 50 degrees
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3235195_2
- `C6`: Lift the tilt angle of 3268421_4 by 3 degrees
- `C7`: Increase transmission power for 3268421_4
- `C8`: Lift the tilt angle  of 3235195_2 by 6 degrees
- `C9`: Decrease A3 Offset threshold for 3268421_4
- `C10`: Decrease transmission power for 3268421_4
- `C11`: Press down the tilt angle of 3268421_4 by 3 degrees
- `C12`: Press down the tilt angle  of 3235195_2 by 6 degrees
- `C13`: Add neighbor relationship between 3268421_4 and 3235195_2 **← 정답**
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3268421_4
- `C15`: Check test server and transmission issues
- `C16`: Add neighbor relationship between 3262627_1 and 3235195_2
- `C17`: Adjust the azimuth of 3235195_2 by 41 degrees
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3268421_4
- `C19`: Increase A3 Offset threshold for 3268421_4
- `C20`: Increase transmission power for 3235195_2
- `C21`: Decrease transmission power for 3235195_2
- `C22`: Insufficient data; more data is needed for judgment.

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.513 | MS1 | 121.4656595689 | 31.1446203805 | 55 | 504990 | -76.80 | 15.90 | 303.41 | 0.18 | 2.32 | 1595 |
| 2024-09-20 22:21:32.387 | MS1 | 121.4656739667 | 31.1446310924 | 55 | 504990 | -75.80 | 16.70 | 448.60 | 0.17 | 2.39 | 1576 |
| 2024-09-20 22:21:33.851 | MS1 | 121.4656632970 | 31.1446242135 | 55 | 504990 | -79.42 | 13.20 | 444.99 | 0.16 | 2.04 | 1597 |
| 2024-09-20 22:21:34.218 | MS1 | 121.4656754405 | 31.1446318814 | 55 | 504990 | -92.58 | -2.21 | 42.81 | 0.19 | 1.41 | 1587 |
| 2024-09-20 22:21:35.635 | MS1 | 121.4656630918 | 31.1446377796 | 55 | 504990 | -93.54 | -1.97 | 64.58 | 0.04 | 1.27 | 1577 |
| 2024-09-20 22:21:36.421 | MS1 | 121.4656772483 | 31.1446185103 | 55 | 504990 | -87.67 | -2.55 | 56.44 | 0.18 | 1.21 | 1583 |
| 2024-09-20 22:21:37.510 | MS1 | 121.4656716298 | 31.1446255768 | 55 | 504990 | -91.83 | -1.23 | 37.15 | 0.10 | 1.19 | 1599 |
| 2024-09-20 22:21:38.878 | MS1 | 121.4656733052 | 31.1446216213 | 55 | 504990 | -80.57 | 15.64 | 308.27 | 0.08 | 1.48 | 1572 |
| 2024-09-20 22:21:39.213 | MS1 | 121.4656763386 | 31.1446181042 | 55 | 504990 | -75.95 | 12.09 | 583.65 | 0.05 | 1.39 | 1562 |
| 2024-09-20 22:21:40.336 | MS1 | 121.4656751378 | 31.1446287685 | 55 | 504990 | -81.90 | 16.20 | 414.32 | 0.02 | 2.44 | 1590 |
| 2024-09-20 22:21:41.754 | MS1 | 121.4656748630 | 31.1446285889 | 55 | 504990 | -84.81 | 13.15 | 413.18 | 0.12 | 2.57 | 1560 |
| 2024-09-20 22:21:42.184 | MS1 | 121.4656650289 | 31.1446307627 | 55 | 504990 | -77.79 | 15.72 | 334.52 | 0.19 | 2.63 | 1586 |

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
| 3235195 | 2 | 121.4713136171 | 31.1548023105 | 246 | 5 | 4 | 15.8 | TDD | 460 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3262627 | 1 | 121.4725464871 | 31.1556829939 | 325 | 4 | 8 | 43.3 | TDD | 585 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3268421 | 4 | 121.4721109942 | 31.1541951662 | 260 | 2 | 12 | 19.8 | TDD | 55 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3269211 | 3 | 121.4681199902 | 31.1445192913 | 355 | 7 | 9 | 31.7 | TDD | 982 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |

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
| 2024-09-20 22:21:31.119 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.137 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.267 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.267 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.934 | NREventA3 | measId:2;ServCellPCI:86;Ser... |
| 2024-09-20 22:21:35.934 | NREventA3 | measId:2;ServCellPCI:86;Ser... |
| 2024-09-20 22:21:36.934 | NREventA3 | measId:2;ServCellPCI:86;Ser... |
| 2024-09-20 22:21:39.434 | NRRRCReestablishAttempt | PCI:86 |
| 2024-09-20 22:21:39.452 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.466 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:39.594 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.594 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3262627 | 1 | 9.5088 | 16.7655 | -116.8855 | 19.5684 | 111.3358 | 0.0047 | 0.0159 |
| 2024_09_20 22:00 | 3235195 | 2 | 6.5940 | 6.0985 | -114.4952 | 17.1613 | 125.0339 | 0.0131 | 0.0195 |
| 2024_09_20 22:00 | 3269211 | 3 | 10.1981 | 10.3638 | -116.7838 | 19.6787 | 89.2220 | 0.0105 | 0.0156 |
| 2024_09_20 22:00 | 3268421 | 4 | 12.4305 | 16.9486 | -116.7683 | 11.1739 | 194.1009 | 0.0136 | 0.1598 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414875_E0EF7EFD | 504990 | 460 | -85.5 | 504990 | 55 | -92.1 | 504990 | 585 | -90.2 | 504990 | 982 |
| MR_1774414875_A16A8C3D | 504990 | 55 | -92.4 | 504990 | 460 | -85.1 | 504990 | 585 | -90.0 | 504990 | 982 |
| MR_1774414875_3E906661 | 504990 | 55 | -93.9 | 504990 | 460 | -85.8 | 504990 | 585 | -90.7 | 504990 | 982 |
| MR_1774414875_5B875125 | 504990 | 460 | -86.1 | 504990 | 55 | -91.6 | 504990 | 585 | -88.2 | 504990 | 982 |
| MR_1774414875_52EF8E50 | 504990 | 460 | -87.6 | 504990 | 55 | -94.0 | 504990 | 585 | -87.9 | 504990 | 982 |
| MR_1774414875_50494182 | 504990 | 55 | -90.7 | 504990 | 460 | -88.4 | 504990 | 585 | -90.4 | 504990 | 982 |
| MR_1774414875_858B2BC7 | 504990 | 55 | -90.9 | 504990 | 460 | -88.2 | 504990 | 585 | -88.8 | 504990 | 982 |

> *... 2개 열 생략 (전체 14열)*

---
