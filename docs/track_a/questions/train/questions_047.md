# Track A 문제 분석 — train[460]~train[469]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[460] ~ train[469] (10개)

## 목차

1. [문제 460: `796c4aaa-36c...`](#460) — single-answer, 정답: C4
2. [문제 461: `a4542e36-8b9...`](#461) — multiple-answer, 정답: C12|C18
3. [문제 462: `5d5709af-30d...`](#462) — single-answer, 정답: C3
4. [문제 463: `51ea67b3-340...`](#463) — single-answer, 정답: C12
5. [문제 464: `7af468cf-f4d...`](#464) — single-answer, 정답: C1
6. [문제 465: `b65c583e-631...`](#465) — single-answer, 정답: C9
7. [문제 466: `1525d575-765...`](#466) — single-answer, 정답: C7
8. [문제 467: `82fd5d5b-00f...`](#467) — single-answer, 정답: C13
9. [문제 468: `22ea59ad-f36...`](#468) — single-answer, 정답: C1
10. [문제 469: `c6766881-ee0...`](#469) — single-answer, 정답: C3

---

### 문제 460: `796c4aaa-36c...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `796c4aaa-36c8-4bf4-8c4a-53fc46cd3e6c` |
| Tag | **single-answer** |
| 정답 | **C4** |
| C4 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[460] topology](images/train_0460.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3268376_2
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3268376_2
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3211090_3
- `C4`: Check test server and transmission issues **← 정답**
- `C5`: Increase transmission power for 3268376_2
- `C6`: Lift the tilt angle of 3211090_3 by 5 degrees
- `C7`: Decrease transmission power for 3268376_2
- `C8`: Increase transmission power for 3211090_3
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3211090_3
- `C10`: Insufficient data; more data is needed for judgment.
- `C11`: Decrease A3 Offset threshold for 3268376_2
- `C12`: Press down the tilt angle  of 3268376_2 by 10 degrees
- `C13`: Adjust the azimuth of 3211090_3 by 31 degrees
- `C14`: Decrease A3 Offset threshold for 3211090_3
- `C15`: Decrease transmission power for 3211090_3
- `C16`: Add neighbor relationship between 3211090_3 and 3268376_2
- `C17`: Add neighbor relationship between 3255073_1 and 3268376_2
- `C18`: Lift the tilt angle  of 3268376_2 by 10 degrees
- `C19`: Adjust the azimuth of 3268376_2 by 50 degrees
- `C20`: Press down the tilt angle of 3211090_3 by 5 degrees
- `C21`: Increase A3 Offset threshold for 3211090_3
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3268376_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.224 | MS1 | 121.4656643385 | 31.1446220891 | 532 | 504990 | -89.89 | 16.84 | 485.72 | 0.09 | 2.26 | 1564 |
| 2024-09-20 22:21:32.968 | MS1 | 121.4656605445 | 31.1446341048 | 532 | 504990 | -90.78 | 16.07 | 458.26 | 0.07 | 2.45 | 1578 |
| 2024-09-20 22:21:33.382 | MS1 | 121.4656678527 | 31.1446194898 | 532 | 504990 | -90.73 | 14.24 | 339.54 | 0.19 | 2.17 | 1599 |
| 2024-09-20 22:21:34.610 | MS1 | 121.4656648221 | 31.1446305134 | 532 | 504990 | -90.57 | 16.95 | 64.26 | 0.07 | 2.64 | 488 |
| 2024-09-20 22:21:35.756 | MS1 | 121.4656683707 | 31.1446211135 | 532 | 504990 | -90.42 | 15.93 | 88.24 | 0.17 | 2.16 | 402 |
| 2024-09-20 22:21:36.204 | MS1 | 121.4656774366 | 31.1446277128 | 532 | 504990 | -91.85 | 14.85 | 47.39 | 0.14 | 2.65 | 415 |
| 2024-09-20 22:21:37.216 | MS1 | 121.4656586910 | 31.1446197238 | 532 | 504990 | -90.19 | 7.34 | 92.42 | 0.20 | 2.12 | 384 |
| 2024-09-20 22:21:38.695 | MS1 | 121.4656722030 | 31.1446206823 | 532 | 504990 | -91.78 | 12.13 | 70.07 | 0.00 | 2.30 | 423 |
| 2024-09-20 22:21:39.458 | MS1 | 121.4656730442 | 31.1446376731 | 532 | 504990 | -93.52 | 7.88 | 98.05 | 0.15 | 2.77 | 300 |
| 2024-09-20 22:21:40.945 | MS1 | 121.4656597052 | 31.1446305203 | 532 | 504990 | -90.46 | 10.85 | 488.66 | 0.07 | 2.83 | 1574 |
| 2024-09-20 22:21:41.807 | MS1 | 121.4656661174 | 31.1446365781 | 532 | 504990 | -89.53 | 10.49 | 499.06 | 0.03 | 2.94 | 1594 |
| 2024-09-20 22:21:42.161 | MS1 | 121.4656735582 | 31.1446284379 | 532 | 504990 | -90.90 | 8.30 | 374.22 | 0.12 | 2.47 | 1600 |

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
| 3211090 | 3 | 121.4705147840 | 31.1514561902 | 180 | 4 | 0 | 20.1 | TDD | 532 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3238483 | 4 | 121.4759800149 | 31.1443518954 | 130 | 9 | 11 | 18.8 | TDD | 751 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3255073 | 1 | 121.4749096661 | 31.1505465978 | 102 | 3 | 9 | 26.2 | TDD | 849 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3268376 | 2 | 121.4752876272 | 31.1474113727 | 162 | 14 | 10 | 43.0 | TDD | 227 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:31.518 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.541 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.661 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.661 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.366 | NREventA3 | measId:2;ServCellPCI:262;Se... |
| 2024-09-20 22:21:38.606 | NRHandoverAttempt | SourcePCI:262;SourceNR-ARFC... |
| 2024-09-20 22:21:38.646 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.658 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.798 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.798 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3255073 | 1 | 17.2649 | 13.0694 | -114.6848 | 7.8804 | 126.6749 | 0.0002 | 0.0120 |
| 2024_09_20 22:00 | 3268376 | 2 | 15.8704 | 7.0127 | -116.8852 | 15.4662 | 111.1195 | 0.0111 | 0.0066 |
| 2024_09_20 22:00 | 3211090 | 3 | 9.4402 | 14.7830 | -115.3540 | 5.3166 | 98.1145 | 0.0059 | 0.0196 |
| 2024_09_20 22:00 | 3238483 | 4 | 9.7610 | 12.9910 | -116.5533 | 18.4222 | 150.8113 | 0.0179 | 0.0104 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412567_39D32FA7 | 504990 | 532 | -89.1 | 504990 | 227 | -94.9 | 504990 | 849 | -103.1 | 504990 | 751 |
| MR_1774412567_0488FFA7 | 504990 | 532 | -91.2 | 504990 | 227 | -94.0 | 504990 | 849 | -103.8 | 504990 | 751 |
| MR_1774412567_75854718 | 504990 | 532 | -92.4 | 504990 | 227 | -93.2 | 504990 | 849 | -103.0 | 504990 | 751 |
| MR_1774412567_657DFF8A | 504990 | 532 | -89.9 | 504990 | 227 | -92.9 | 504990 | 849 | -101.0 | 504990 | 751 |
| MR_1774412567_F9801486 | 504990 | 532 | -92.0 | 504990 | 227 | -94.2 | 504990 | 849 | -103.0 | 504990 | 751 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 461: `a4542e36-8b9...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `a4542e36-8b93-4896-bd93-d664c6ba4ac0` |
| Tag | **multiple-answer** |
| 정답 | **C12|C18** |
| C12 의미 | Increase transmission power for 3217311_3 |
| C18 의미 | Adjust the azimuth of 3217311_3 by 31 degrees |
| 패턴 분류 | **P4 Coverage (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[461] topology](images/train_0461.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3217311_3
- `C2`: Check test server and transmission issues
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3217311_3
- `C4`: Add neighbor relationship between 3222474_4 and 3270618_1
- `C5`: Decrease A3 Offset threshold for 3270618_1
- `C6`: Insufficient data; more data is needed for judgment.
- `C7`: Adjust the azimuth of 3270618_1 by 21 degrees
- `C8`: Increase transmission power for 3270618_1
- `C9`: Increase A3 Offset threshold for 3270618_1
- `C10`: Decrease transmission power for 3270618_1
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3217311_3
- `C12`: Increase transmission power for 3217311_3 **← 정답**
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3270618_1
- `C14`: Press down the tilt angle of 3217311_3 by 9 degrees
- `C15`: Decrease transmission power for 3217311_3
- `C16`: Lift the tilt angle of 3217311_3 by 9 degrees
- `C17`: Add neighbor relationship between 3217311_3 and 3270618_1
- `C18`: Adjust the azimuth of 3217311_3 by 31 degrees **← 정답**
- `C19`: Press down the tilt angle  of 3270618_1 by 4 degrees
- `C20`: Decrease A3 Offset threshold for 3217311_3
- `C21`: Lift the tilt angle  of 3270618_1 by 4 degrees
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3270618_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.170 | MS1 | 121.4656752861 | 31.1446270993 | 36 | 504990 | -92.92 | 15.91 | 497.32 | 0.08 | 2.36 | 1583 |
| 2024-09-20 22:21:32.631 | MS1 | 121.4656719949 | 31.1446316407 | 36 | 504990 | -86.11 | 14.79 | 317.38 | 0.00 | 2.30 | 1580 |
| 2024-09-20 22:21:33.574 | MS1 | 121.4656703351 | 31.1446202749 | 36 | 504990 | -87.48 | 17.51 | 397.27 | 0.20 | 2.70 | 1580 |
| 2024-09-20 22:21:34.259 | MS1 | 121.4656585245 | 31.1446369707 | 36 | 504990 | -108.53 | 0.42 | 43.82 | 0.14 | 1.15 | 1564 |
| 2024-09-20 22:21:35.706 | MS1 | 121.4656652460 | 31.1446319257 | 36 | 504990 | -102.61 | -1.03 | 36.96 | 0.12 | 1.45 | 1589 |
| 2024-09-20 22:21:36.880 | MS1 | 121.4656594877 | 31.1446271771 | 36 | 504990 | -108.78 | 1.14 | 34.27 | 0.13 | 1.31 | 1570 |
| 2024-09-20 22:21:37.134 | MS1 | 121.4656620884 | 31.1446358084 | 36 | 504990 | -109.48 | -1.93 | 76.88 | 0.01 | 1.23 | 1599 |
| 2024-09-20 22:21:38.235 | MS1 | 121.4656726215 | 31.1446272487 | 36 | 504990 | -106.49 | 1.39 | 70.66 | 0.01 | 1.28 | 1581 |
| 2024-09-20 22:21:39.535 | MS1 | 121.4656622791 | 31.1446253147 | 36 | 504990 | -104.63 | -0.45 | 20.12 | 0.16 | 1.27 | 1561 |
| 2024-09-20 22:21:40.771 | MS1 | 121.4656634457 | 31.1446230998 | 36 | 504990 | -92.06 | 15.49 | 370.10 | 0.05 | 2.18 | 1600 |
| 2024-09-20 22:21:41.988 | MS1 | 121.4656695532 | 31.1446366843 | 36 | 504990 | -93.18 | 17.74 | 589.54 | 0.09 | 2.03 | 1588 |
| 2024-09-20 22:21:42.322 | MS1 | 121.4656767142 | 31.1446249557 | 36 | 504990 | -93.20 | 14.38 | 349.92 | 0.09 | 2.50 | 1582 |

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
| 3217311 | 3 | 121.4654551376 | 31.1496908869 | 209 | 4 | 2 | 47.1 | TDD | 36 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3222474 | 4 | 121.4736423753 | 31.1498543436 | 210 | 2 | 1 | 24.7 | TDD | 492 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3239918 | 2 | 121.4743010253 | 31.1523696513 | 1 | 5 | 9 | 38.0 | TDD | 866 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3270618 | 1 | 121.4737108590 | 31.1442308460 | 294 | 3 | 12 | 16.8 | TDD | 992 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:31.577 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.596 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.697 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.697 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.967 | NREventA2 | measId:1;ServCellPCI:656;Se... |
| 2024-09-20 22:21:35.078 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3270618 | 1 | 16.7693 | 18.5128 | -115.3570 | 16.7295 | 184.2173 | 0.0047 | 0.0192 |
| 2024_09_20 22:00 | 3239918 | 2 | 12.7033 | 13.1266 | -117.4185 | 11.0096 | 92.2876 | 0.0043 | 0.0135 |
| 2024_09_20 22:00 | 3217311 | 3 | 6.0126 | 15.0455 | -116.6095 | 6.3298 | 181.4463 | 0.1553 | 0.0124 |
| 2024_09_20 22:00 | 3222474 | 4 | 5.4905 | 10.0280 | -117.7550 | 5.2693 | 127.2110 | 0.0022 | 0.0132 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414470_D2B8E2A4 | 504990 | 36 | -109.8 | 504990 | 992 | -111.1 | 504990 | 492 | -116.2 | 504990 | 866 |
| MR_1774414470_E360A978 | 504990 | 36 | -106.8 | 504990 | 992 | -112.7 | 504990 | 492 | -116.9 | 504990 | 866 |
| MR_1774414470_D49733E1 | 504990 | 36 | -109.1 | 504990 | 992 | -109.9 | 504990 | 492 | -115.3 | 504990 | 866 |
| MR_1774414470_79C1EF01 | 504990 | 36 | -107.1 | 504990 | 992 | -113.6 | 504990 | 492 | -118.1 | 504990 | 866 |
| MR_1774414470_448A74D8 | 504990 | 36 | -109.8 | 504990 | 992 | -113.3 | 504990 | 492 | -117.8 | 504990 | 866 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 462: `5d5709af-30d...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `5d5709af-30d1-4195-99e4-016a7bc45983` |
| Tag | **single-answer** |
| 정답 | **C3** |
| C3 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[462] topology](images/train_0462.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3218280_4
- `C2`: Decrease A3 Offset threshold for 3218280_4
- `C3`: Insufficient data; more data is needed for judgment. **← 정답**
- `C4`: Decrease transmission power for 3218280_4
- `C5`: Press down the tilt angle of 3218280_4 by 10 degrees
- `C6`: Adjust the azimuth of 3218280_4 by 26 degrees
- `C7`: Lift the tilt angle  of 3248004_3 by 10 degrees
- `C8`: Add neighbor relationship between 3251885_2 and 3248004_3
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3218280_4
- `C10`: Check test server and transmission issues
- `C11`: Decrease transmission power for 3248004_3
- `C12`: Increase A3 Offset threshold for 3218280_4
- `C13`: Adjust the azimuth of 3248004_3 by 50 degrees
- `C14`: Lift the tilt angle of 3218280_4 by 10 degrees
- `C15`: Increase A3 Offset threshold for 3248004_3
- `C16`: Decrease A3 Offset threshold for 3248004_3
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3248004_3
- `C18`: Press down the tilt angle  of 3248004_3 by 10 degrees
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3248004_3
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3218280_4
- `C21`: Increase transmission power for 3248004_3
- `C22`: Add neighbor relationship between 3218280_4 and 3248004_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.104 | MS1 | 121.4656664826 | 31.1446189808 | 559 | 504990 | -91.14 | 13.96 | 539.41 | 0.19 | 2.40 | 1561 |
| 2024-09-20 22:21:32.781 | MS1 | 121.4656695909 | 31.1446202486 | 559 | 504990 | -89.81 | 16.17 | 501.14 | 0.16 | 2.18 | 1591 |
| 2024-09-20 22:21:33.107 | MS1 | 121.4656652618 | 31.1446340196 | 559 | 504990 | -85.87 | 12.64 | 387.61 | 0.07 | 2.30 | 1597 |
| 2024-09-20 22:21:34.144 | MS1 | 121.4656645698 | 31.1446237512 | 559 | 504990 | -89.87 | 14.70 | 51.16 | 0.07 | 2.25 | 1597 |
| 2024-09-20 22:21:35.870 | MS1 | 121.4656613466 | 31.1446289082 | 559 | 504990 | -87.23 | 15.45 | 59.93 | 0.02 | 2.04 | 1579 |
| 2024-09-20 22:21:36.441 | MS1 | 121.4656743531 | 31.1446210232 | 559 | 504990 | -91.74 | 13.73 | 62.41 | 0.07 | 2.21 | 1593 |
| 2024-09-20 22:21:37.284 | MS1 | 121.4656676026 | 31.1446282038 | 559 | 504990 | -90.84 | 9.71 | 89.33 | 0.12 | 2.25 | 1563 |
| 2024-09-20 22:21:38.337 | MS1 | 121.4656595165 | 31.1446282499 | 559 | 504990 | -93.03 | 9.83 | 78.40 | 0.17 | 2.37 | 1570 |
| 2024-09-20 22:21:39.108 | MS1 | 121.4656717053 | 31.1446331096 | 559 | 504990 | -90.17 | 8.16 | 82.21 | 0.04 | 2.45 | 1583 |
| 2024-09-20 22:21:40.739 | MS1 | 121.4656683627 | 31.1446326824 | 559 | 504990 | -92.46 | 7.43 | 582.90 | 0.11 | 2.09 | 1564 |
| 2024-09-20 22:21:41.556 | MS1 | 121.4656627617 | 31.1446271909 | 559 | 504990 | -89.63 | 10.95 | 567.24 | 0.15 | 2.39 | 1565 |
| 2024-09-20 22:21:42.416 | MS1 | 121.4656738571 | 31.1446286386 | 559 | 504990 | -92.46 | 9.14 | 446.82 | 0.18 | 2.37 | 1576 |

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
| 3218280 | 4 | 121.4740821128 | 31.1457822751 | 287 | 9 | 1 | 24.3 | TDD | 559 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3248004 | 3 | 121.4647010647 | 31.1468558687 | 267 | 12 | 6 | 37.3 | TDD | 22 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3251885 | 2 | 121.4688685477 | 31.1504499301 | 58 | 1 | 0 | 38.7 | TDD | 476 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3277846 | 1 | 121.4646918115 | 31.1552487678 | 353 | 11 | 0 | 38.9 | TDD | 986 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:31.540 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.559 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.705 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.705 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.430 | NREventA3 | measId:2;ServCellPCI:333;Se... |
| 2024-09-20 22:21:38.670 | NRHandoverAttempt | SourcePCI:333;SourceNR-ARFC... |
| 2024-09-20 22:21:38.713 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.728 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.842 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.842 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3277846 | 1 | 89.7766 | 91.0050 | -115.0835 | 11.1589 | 83.8505 | 0.0169 | 0.0087 |
| 2024_09_19 22:00 | 3251885 | 2 | 79.6784 | 78.5685 | -114.5636 | 18.1128 | 89.6567 | 0.0004 | 0.0050 |
| 2024_09_19 22:00 | 3248004 | 3 | 86.2918 | 80.2106 | -117.6986 | 16.6627 | 139.5239 | 0.0083 | 0.0022 |
| 2024_09_19 22:00 | 3218280 | 4 | 94.8922 | 87.8235 | -115.9722 | 9.2642 | 118.4155 | 0.0066 | 0.0059 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416136_10351085 | 504990 | 559 | -90.8 | 504990 | 22 | -90.1 | 504990 | 476 | -104.5 | 504990 | 986 |
| MR_1774416136_244AC0C0 | 504990 | 559 | -87.9 | 504990 | 22 | -89.0 | 504990 | 476 | -105.2 | 504990 | 986 |
| MR_1774416136_81EBF528 | 504990 | 559 | -88.3 | 504990 | 22 | -91.6 | 504990 | 476 | -103.7 | 504990 | 986 |
| MR_1774416136_1A89BFD8 | 504990 | 559 | -89.5 | 504990 | 22 | -90.7 | 504990 | 476 | -104.8 | 504990 | 986 |
| MR_1774416136_C1F08F22 | 504990 | 559 | -87.9 | 504990 | 22 | -91.6 | 504990 | 476 | -102.9 | 504990 | 986 |
| MR_1774416136_E923C1C5 | 504990 | 559 | -90.6 | 504990 | 22 | -91.8 | 504990 | 476 | -103.5 | 504990 | 986 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 463: `51ea67b3-340...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `51ea67b3-3406-40e2-b44f-12464cd5fe64` |
| Tag | **single-answer** |
| 정답 | **C12** |
| C12 의미 | Lift the tilt angle  of 3240561_3 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[463] topology](images/train_0463.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3238098_1
- `C2`: Lift the tilt angle of 3239459_4 by 4 degrees
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3238098_1
- `C4`: Increase transmission power for 3239459_4
- `C5`: Increase A3 Offset threshold for 3239459_4
- `C6`: Increase A3 Offset threshold for 3238098_1
- `C7`: Decrease A3 Offset threshold for 3238098_1
- `C8`: Add neighbor relationship between 3239459_4 and 3238098_1
- `C9`: Decrease transmission power for 3239459_4
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3239459_4
- `C11`: Press down the tilt angle of 3239459_4 by 4 degrees
- `C12`: Lift the tilt angle  of 3240561_3 by 10 degrees **← 정답**
- `C13`: Check test server and transmission issues
- `C14`: Decrease transmission power for 3238098_1
- `C15`: Increase transmission power for 3238098_1
- `C16`: Insufficient data; more data is needed for judgment.
- `C17`: Decrease A3 Offset threshold for 3239459_4
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3239459_4
- `C19`: Adjust the azimuth of 3239459_4 by 42 degrees
- `C20`: Adjust the azimuth of 3240561_3 by 50 degrees
- `C21`: Press down the tilt angle  of 3240561_3 by 10 degrees
- `C22`: Add neighbor relationship between 3240561_3 and 3238098_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.737 | MS1 | 121.4656620819 | 31.1446289331 | 420 | 504990 | -88.95 | 16.44 | 562.02 | 0.11 | 2.50 | 1583 |
| 2024-09-20 22:21:32.804 | MS1 | 121.4656584123 | 31.1446268121 | 420 | 504990 | -88.39 | 12.43 | 307.69 | 0.02 | 2.42 | 1571 |
| 2024-09-20 22:21:33.270 | MS1 | 121.4656583071 | 31.1446355864 | 420 | 504990 | -91.35 | 17.06 | 309.89 | 0.19 | 2.48 | 1582 |
| 2024-09-20 22:21:34.727 | MS1 | 121.4656725163 | 31.1446292509 | 420 | 504990 | -91.48 | 16.48 | 71.32 | 0.19 | 2.46 | 1585 |
| 2024-09-20 22:21:35.818 | MS1 | 121.4656621689 | 31.1446298158 | 420 | 504990 | -86.66 | 12.59 | 84.25 | 0.12 | 2.20 | 1586 |
| 2024-09-20 22:21:36.819 | MS1 | 121.4656734877 | 31.1446354343 | 420 | 504990 | -85.58 | 12.00 | 65.64 | 0.02 | 2.66 | 1582 |
| 2024-09-20 22:21:37.846 | MS1 | 121.4656610744 | 31.1446262295 | 420 | 504990 | -89.26 | 7.69 | 91.27 | 0.18 | 2.65 | 1566 |
| 2024-09-20 22:21:38.649 | MS1 | 121.4656596089 | 31.1446302526 | 420 | 504990 | -90.33 | 8.10 | 47.33 | 0.18 | 2.81 | 1569 |
| 2024-09-20 22:21:39.657 | MS1 | 121.4656664274 | 31.1446290036 | 420 | 504990 | -93.95 | 12.62 | 74.92 | 0.03 | 2.85 | 1570 |
| 2024-09-20 22:21:40.710 | MS1 | 121.4656630508 | 31.1446184814 | 420 | 504990 | -92.48 | 9.55 | 391.46 | 0.14 | 2.94 | 1578 |
| 2024-09-20 22:21:41.843 | MS1 | 121.4656676589 | 31.1446180011 | 420 | 504990 | -89.84 | 11.08 | 591.10 | 0.14 | 2.78 | 1598 |
| 2024-09-20 22:21:42.330 | MS1 | 121.4656668758 | 31.1446251924 | 420 | 504990 | -90.07 | 9.63 | 540.50 | 0.10 | 2.30 | 1570 |

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
| 3238098 | 1 | 121.4728877434 | 31.1491177917 | 343 | 9 | 7 | 46.7 | TDD | 696 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3239459 | 4 | 121.4688311652 | 31.1497147543 | 250 | 1 | 12 | 35.9 | TDD | 420 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3240561 | 3 | 121.4679215958 | 31.1453017953 | 71 | 14 | 0 | 49.7 | TDD | 810 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3270021 | 2 | 121.4754591176 | 31.1494978787 | 202 | 3 | 10 | 17.1 | TDD | 97 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |

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
| 2024-09-20 22:21:31.372 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.389 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.510 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.510 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.206 | NREventA3 | measId:2;ServCellPCI:94;Ser... |
| 2024-09-20 22:21:38.446 | NRHandoverAttempt | SourcePCI:94;SourceNR-ARFCN... |
| 2024-09-20 22:21:38.481 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.492 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.599 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.599 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3238098 | 1 | 7.0440 | 18.6698 | -116.3367 | 12.2615 | 147.5447 | 0.0014 | 0.0065 |
| 2024_09_20 22:00 | 3270021 | 2 | 9.3022 | 11.6700 | -116.4740 | 5.2595 | 95.9952 | 0.0026 | 0.0001 |
| 2024_09_20 22:00 | 3240561 | 3 | 13.1239 | 11.5276 | -115.2934 | 13.6375 | 173.2426 | 0.0062 | 0.0118 |
| 2024_09_20 22:00 | 3239459 | 4 | 81.1341 | 92.0802 | -115.1196 | 19.4281 | 144.9675 | 0.0011 | 0.0043 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415400_1E469F47 | 504990 | 420 | -91.1 | 504990 | 696 | -92.1 | 504990 | 810 | -100.4 | 504990 | 97 |
| MR_1774415400_6863496F | 504990 | 420 | -92.2 | 504990 | 696 | -91.4 | 504990 | 810 | -101.2 | 504990 | 97 |
| MR_1774415400_B80EE093 | 504990 | 420 | -92.6 | 504990 | 696 | -91.0 | 504990 | 810 | -102.8 | 504990 | 97 |
| MR_1774415400_282B5A30 | 504990 | 420 | -90.4 | 504990 | 696 | -93.8 | 504990 | 810 | -101.2 | 504990 | 97 |
| MR_1774415400_0F0A4666 | 504990 | 420 | -91.4 | 504990 | 696 | -90.2 | 504990 | 810 | -102.8 | 504990 | 97 |
| MR_1774415400_0366E73C | 504990 | 420 | -92.3 | 504990 | 696 | -90.0 | 504990 | 810 | -102.6 | 504990 | 97 |
| MR_1774415400_CE59D631 | 504990 | 420 | -90.3 | 504990 | 696 | -92.4 | 504990 | 810 | -99.4 | 504990 | 97 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 464: `7af468cf-f4d...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `7af468cf-f4d2-4963-a556-efbc1ffe3b3e` |
| Tag | **single-answer** |
| 정답 | **C1** |
| C1 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[464] topology](images/train_0464.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment. **← 정답**
- `C2`: Increase A3 Offset threshold for 3273694_2
- `C3`: Press down the tilt angle of 3268754_1 by 10 degrees
- `C4`: Adjust the azimuth of 3268754_1 by 50 degrees
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3273694_2
- `C6`: Increase A3 Offset threshold for 3268754_1
- `C7`: Add neighbor relationship between 3268754_1 and 3273694_2
- `C8`: Increase transmission power for 3268754_1
- `C9`: Decrease transmission power for 3268754_1
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3273694_2
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3268754_1
- `C12`: Decrease A3 Offset threshold for 3268754_1
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3268754_1
- `C14`: Lift the tilt angle  of 3273694_2 by 6 degrees
- `C15`: Add neighbor relationship between 3251156_4 and 3273694_2
- `C16`: Adjust the azimuth of 3273694_2 by 50 degrees
- `C17`: Increase transmission power for 3273694_2
- `C18`: Decrease transmission power for 3273694_2
- `C19`: Decrease A3 Offset threshold for 3273694_2
- `C20`: Lift the tilt angle of 3268754_1 by 10 degrees
- `C21`: Press down the tilt angle  of 3273694_2 by 6 degrees
- `C22`: Check test server and transmission issues

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.481 | MS1 | 121.4656624891 | 31.1446337617 | 803 | 504990 | -88.09 | 12.10 | 386.38 | 0.03 | 2.49 | 1588 |
| 2024-09-20 22:21:32.160 | MS1 | 121.4656726508 | 31.1446272213 | 803 | 504990 | -87.19 | 12.62 | 443.92 | 0.17 | 2.43 | 1579 |
| 2024-09-20 22:21:33.360 | MS1 | 121.4656647438 | 31.1446282659 | 803 | 504990 | -85.97 | 13.77 | 472.40 | 0.18 | 2.19 | 1579 |
| 2024-09-20 22:21:34.822 | MS1 | 121.4656767037 | 31.1446365610 | 803 | 504990 | -85.57 | 15.07 | 74.64 | 0.02 | 2.31 | 1583 |
| 2024-09-20 22:21:35.954 | MS1 | 121.4656733980 | 31.1446216006 | 803 | 504990 | -89.43 | 12.87 | 84.11 | 0.13 | 2.87 | 1597 |
| 2024-09-20 22:21:36.512 | MS1 | 121.4656736858 | 31.1446343904 | 803 | 504990 | -86.03 | 16.75 | 71.03 | 0.06 | 2.25 | 1586 |
| 2024-09-20 22:21:37.991 | MS1 | 121.4656650935 | 31.1446331533 | 803 | 504990 | -89.05 | 8.94 | 88.27 | 0.04 | 2.44 | 1600 |
| 2024-09-20 22:21:38.444 | MS1 | 121.4656689059 | 31.1446281703 | 803 | 504990 | -93.56 | 12.40 | 91.19 | 0.02 | 2.40 | 1587 |
| 2024-09-20 22:21:39.403 | MS1 | 121.4656735446 | 31.1446271865 | 803 | 504990 | -93.00 | 9.41 | 90.03 | 0.06 | 2.21 | 1593 |
| 2024-09-20 22:21:40.295 | MS1 | 121.4656765860 | 31.1446302169 | 803 | 504990 | -89.47 | 12.06 | 523.08 | 0.08 | 2.31 | 1585 |
| 2024-09-20 22:21:41.519 | MS1 | 121.4656673122 | 31.1446180175 | 803 | 504990 | -93.62 | 10.86 | 435.33 | 0.08 | 2.86 | 1570 |
| 2024-09-20 22:21:42.378 | MS1 | 121.4656779968 | 31.1446362247 | 803 | 504990 | -93.25 | 12.48 | 388.72 | 0.07 | 2.36 | 1593 |

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
| 3238964 | 3 | 121.4644666027 | 31.1458218677 | 253 | 8 | 9 | 40.2 | TDD | 461 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3251156 | 4 | 121.4707596782 | 31.1455677857 | 267 | 13 | 8 | 39.9 | TDD | 375 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3268754 | 1 | 121.4648634065 | 31.1442006450 | 152 | 0 | 1 | 26.4 | TDD | 803 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3273694 | 2 | 121.4646959979 | 31.1532236293 | 76 | 4 | 1 | 31.5 | TDD | 868 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |

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
| 2024-09-20 22:21:31.368 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.497 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.497 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.159 | NREventA3 | measId:2;ServCellPCI:268;Se... |
| 2024-09-20 22:21:38.399 | NRHandoverAttempt | SourcePCI:268;SourceNR-ARFC... |
| 2024-09-20 22:21:38.431 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.442 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.544 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.544 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3268754 | 1 | 88.9251 | 93.0394 | -115.6227 | 10.9718 | 140.3168 | 0.0005 | 0.0032 |
| 2024_09_19 22:00 | 3273694 | 2 | 92.5739 | 76.7884 | -115.4111 | 13.1891 | 190.2477 | 0.0190 | 0.0064 |
| 2024_09_19 22:00 | 3238964 | 3 | 92.8213 | 84.3050 | -115.2115 | 13.0825 | 122.1095 | 0.0116 | 0.0199 |
| 2024_09_19 22:00 | 3251156 | 4 | 86.1261 | 87.8488 | -114.5279 | 11.6178 | 99.1634 | 0.0087 | 0.0174 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416454_8F73E548 | 504990 | 803 | -87.1 | 504990 | 868 | -92.3 | 504990 | 375 | -93.9 | 504990 | 461 |
| MR_1774416454_BF67C7DC | 504990 | 803 | -86.8 | 504990 | 868 | -90.8 | 504990 | 375 | -91.1 | 504990 | 461 |
| MR_1774416454_5F580AB9 | 504990 | 803 | -84.5 | 504990 | 868 | -91.1 | 504990 | 375 | -90.9 | 504990 | 461 |
| MR_1774416454_16218B4F | 504990 | 803 | -86.2 | 504990 | 868 | -89.2 | 504990 | 375 | -93.7 | 504990 | 461 |
| MR_1774416454_7C01E97A | 504990 | 803 | -86.1 | 504990 | 868 | -92.2 | 504990 | 375 | -93.5 | 504990 | 461 |
| MR_1774416454_192F38B2 | 504990 | 803 | -84.6 | 504990 | 868 | -89.8 | 504990 | 375 | -91.4 | 504990 | 461 |
| MR_1774416454_736BF457 | 504990 | 803 | -84.3 | 504990 | 868 | -91.1 | 504990 | 375 | -92.3 | 504990 | 461 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 465: `b65c583e-631...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `b65c583e-631d-4b32-a344-38ae7ec7f8d4` |
| Tag | **single-answer** |
| 정답 | **C9** |
| C9 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3239178_4 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[465] topology](images/train_0465.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3239178_4 by 3 degrees
- `C2`: Increase transmission power for 3239178_4
- `C3`: Decrease A3 Offset threshold for 3267166_2
- `C4`: Increase A3 Offset threshold for 3267166_2
- `C5`: Check test server and transmission issues
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3267166_2
- `C7`: Increase transmission power for 3267166_2
- `C8`: Add neighbor relationship between 3274971_1 and 3267166_2
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3239178_4 **← 정답**
- `C10`: Lift the tilt angle  of 3267166_2 by 9 degrees
- `C11`: Decrease transmission power for 3267166_2
- `C12`: Press down the tilt angle of 3239178_4 by 3 degrees
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3267166_2
- `C14`: Decrease transmission power for 3239178_4
- `C15`: Add neighbor relationship between 3239178_4 and 3267166_2
- `C16`: Insufficient data; more data is needed for judgment.
- `C17`: Adjust the azimuth of 3239178_4 by 30 degrees
- `C18`: Adjust the azimuth of 3267166_2 by 50 degrees
- `C19`: Increase A3 Offset threshold for 3239178_4
- `C20`: Press down the tilt angle  of 3267166_2 by 9 degrees
- `C21`: Decrease A3 Offset threshold for 3239178_4
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3239178_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.686 | MS1 | 121.4656618390 | 31.1446211146 | 647 | 504990 | -91.30 | 15.75 | 532.50 | 0.03 | 2.28 | 1588 |
| 2024-09-20 22:21:32.564 | MS1 | 121.4656670282 | 31.1446309115 | 647 | 504990 | -88.63 | 17.78 | 541.02 | 0.04 | 2.27 | 1597 |
| 2024-09-20 22:21:33.827 | MS1 | 121.4656658974 | 31.1446200093 | 647 | 504990 | -91.79 | 13.83 | 498.30 | 0.06 | 2.07 | 1589 |
| 2024-09-20 22:21:34.175 | MS1 | 121.4656711586 | 31.1446276560 | 647 | 504990 | -91.05 | 17.40 | 90.89 | 0.63 | 2.98 | 605 |
| 2024-09-20 22:21:35.188 | MS1 | 121.4656594387 | 31.1446357162 | 647 | 504990 | -88.54 | 12.69 | 75.76 | 0.68 | 2.83 | 583 |
| 2024-09-20 22:21:36.398 | MS1 | 121.4656774359 | 31.1446337185 | 647 | 504990 | -89.69 | 15.61 | 70.59 | 0.50 | 2.33 | 527 |
| 2024-09-20 22:21:37.386 | MS1 | 121.4656658462 | 31.1446354300 | 647 | 504990 | -89.24 | 10.33 | 60.01 | 0.69 | 2.92 | 580 |
| 2024-09-20 22:21:38.838 | MS1 | 121.4656630576 | 31.1446330204 | 647 | 504990 | -91.88 | 7.19 | 102.59 | 0.51 | 2.45 | 680 |
| 2024-09-20 22:21:39.424 | MS1 | 121.4656677237 | 31.1446264980 | 647 | 504990 | -90.39 | 8.44 | 105.01 | 0.64 | 2.95 | 693 |
| 2024-09-20 22:21:40.582 | MS1 | 121.4656664871 | 31.1446232764 | 647 | 504990 | -93.59 | 12.22 | 348.46 | 0.02 | 2.87 | 1578 |
| 2024-09-20 22:21:41.253 | MS1 | 121.4656712742 | 31.1446271288 | 647 | 504990 | -92.08 | 7.70 | 456.80 | 0.17 | 2.73 | 1594 |
| 2024-09-20 22:21:42.314 | MS1 | 121.4656669378 | 31.1446370131 | 647 | 504990 | -90.13 | 12.24 | 428.10 | 0.05 | 2.16 | 1573 |

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
| 3239178 | 4 | 121.4735965321 | 31.1554252832 | 242 | 2 | 10 | 34.3 | TDD | 647 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3258448 | 3 | 121.4704093277 | 31.1553201301 | 247 | 13 | 3 | 48.3 | TDD | 726 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3267166 | 2 | 121.4647456868 | 31.1552662904 | 118 | 7 | 11 | 44.8 | TDD | 212 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3274971 | 1 | 121.4721265871 | 31.1536641588 | 259 | 10 | 3 | 21.6 | TDD | 618 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |

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
| 2024-09-20 22:21:31.458 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.478 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.627 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.627 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.315 | NREventA3 | measId:2;ServCellPCI:82;Ser... |
| 2024-09-20 22:21:38.555 | NRHandoverAttempt | SourcePCI:82;SourceNR-ARFCN... |
| 2024-09-20 22:21:38.586 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.601 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.737 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.737 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3274971 | 1 | 18.3681 | 7.2313 | -117.3566 | 15.6015 | 197.1682 | 0.0057 | 0.0101 |
| 2024_09_20 22:00 | 3267166 | 2 | 16.0503 | 17.5451 | -114.6731 | 7.9979 | 119.9508 | 0.0147 | 0.0101 |
| 2024_09_20 22:00 | 3258448 | 3 | 11.7251 | 17.1639 | -115.0788 | 8.5079 | 156.7745 | 0.0109 | 0.0028 |
| 2024_09_20 22:00 | 3239178 | 4 | 19.1178 | 8.1360 | -115.3812 | 6.4083 | 167.6096 | 0.0033 | 0.0096 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412168_42D817A0 | 504990 | 647 | -92.2 | 504990 | 212 | -90.6 | 504990 | 618 | -98.7 | 504990 | 726 |
| MR_1774412168_E52D9AB7 | 504990 | 647 | -91.5 | 504990 | 212 | -93.1 | 504990 | 618 | -98.1 | 504990 | 726 |
| MR_1774412168_098987A2 | 504990 | 647 | -89.2 | 504990 | 212 | -93.5 | 504990 | 618 | -99.9 | 504990 | 726 |
| MR_1774412168_2356442E | 504990 | 647 | -90.5 | 504990 | 212 | -90.5 | 504990 | 618 | -98.2 | 504990 | 726 |
| MR_1774412168_AAC5707D | 504990 | 647 | -93.0 | 504990 | 212 | -93.2 | 504990 | 618 | -100.8 | 504990 | 726 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 466: `1525d575-765...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `1525d575-765d-4b74-ba89-778b7835f80f` |
| Tag | **single-answer** |
| 정답 | **C7** |
| C7 의미 | Lift the tilt angle  of 3240140_2 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[466] topology](images/train_0466.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3226427_4
- `C2`: Adjust the azimuth of 3256111_1 by 27 degrees
- `C3`: Add neighbor relationship between 3240140_2 and 3226427_4
- `C4`: Press down the tilt angle of 3256111_1 by 4 degrees
- `C5`: Increase transmission power for 3226427_4
- `C6`: Decrease A3 Offset threshold for 3226427_4
- `C7`: Lift the tilt angle  of 3240140_2 by 10 degrees **← 정답**
- `C8`: Decrease transmission power for 3256111_1
- `C9`: Adjust the azimuth of 3240140_2 by 4 degrees
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3256111_1
- `C11`: Press down the tilt angle  of 3240140_2 by 10 degrees
- `C12`: Insufficient data; more data is needed for judgment.
- `C13`: Decrease A3 Offset threshold for 3256111_1
- `C14`: Check test server and transmission issues
- `C15`: Decrease transmission power for 3226427_4
- `C16`: Increase transmission power for 3256111_1
- `C17`: Lift the tilt angle of 3256111_1 by 4 degrees
- `C18`: Increase A3 Offset threshold for 3226427_4
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3226427_4
- `C20`: Increase A3 Offset threshold for 3256111_1
- `C21`: Add neighbor relationship between 3256111_1 and 3226427_4
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3256111_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.559 | MS1 | 121.4656629364 | 31.1446295296 | 952 | 504990 | -88.96 | 15.30 | 499.85 | 0.06 | 2.13 | 1580 |
| 2024-09-20 22:21:32.115 | MS1 | 121.4656680691 | 31.1446263243 | 952 | 504990 | -85.38 | 12.35 | 597.26 | 0.12 | 2.01 | 1564 |
| 2024-09-20 22:21:33.208 | MS1 | 121.4656592935 | 31.1446245433 | 952 | 504990 | -89.45 | 16.27 | 572.21 | 0.02 | 2.04 | 1576 |
| 2024-09-20 22:21:34.335 | MS1 | 121.4656618245 | 31.1446187510 | 952 | 504990 | -88.40 | 14.37 | 77.99 | 0.02 | 2.22 | 1578 |
| 2024-09-20 22:21:35.316 | MS1 | 121.4656733847 | 31.1446257310 | 952 | 504990 | -91.18 | 14.41 | 88.55 | 0.16 | 2.79 | 1589 |
| 2024-09-20 22:21:36.776 | MS1 | 121.4656606241 | 31.1446297864 | 952 | 504990 | -86.53 | 12.47 | 83.76 | 0.10 | 2.87 | 1589 |
| 2024-09-20 22:21:37.638 | MS1 | 121.4656605581 | 31.1446373932 | 952 | 504990 | -90.40 | 9.12 | 75.49 | 0.01 | 2.24 | 1594 |
| 2024-09-20 22:21:38.841 | MS1 | 121.4656655477 | 31.1446186011 | 952 | 504990 | -89.95 | 7.79 | 49.70 | 0.10 | 2.59 | 1573 |
| 2024-09-20 22:21:39.913 | MS1 | 121.4656633258 | 31.1446321506 | 952 | 504990 | -91.63 | 8.67 | 100.18 | 0.09 | 2.73 | 1595 |
| 2024-09-20 22:21:40.107 | MS1 | 121.4656715436 | 31.1446299709 | 952 | 504990 | -89.76 | 11.81 | 327.98 | 0.11 | 2.34 | 1597 |
| 2024-09-20 22:21:41.790 | MS1 | 121.4656617415 | 31.1446305832 | 952 | 504990 | -91.70 | 9.11 | 536.39 | 0.06 | 2.82 | 1565 |
| 2024-09-20 22:21:42.376 | MS1 | 121.4656712852 | 31.1446257324 | 952 | 504990 | -89.99 | 8.68 | 434.51 | 0.07 | 2.96 | 1564 |

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
| 3216083 | 3 | 121.4665228382 | 31.1450402344 | 216 | 0 | 5 | 30.7 | TDD | 592 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3226427 | 4 | 121.4648541243 | 31.1542436275 | 172 | 15 | 3 | 43.2 | TDD | 30 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3240140 | 2 | 121.4718977595 | 31.1543840847 | 47 | 0 | 9 | 24.7 | TDD | 256 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3256111 | 1 | 121.4727109751 | 31.1529448532 | 189 | 2 | 8 | 46.9 | TDD | 952 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |

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
| 2024-09-20 22:21:30.922 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.025 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.025 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.719 | NREventA3 | measId:2;ServCellPCI:846;Se... |
| 2024-09-20 22:21:37.959 | NRHandoverAttempt | SourcePCI:846;SourceNR-ARFC... |
| 2024-09-20 22:21:37.999 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.013 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.147 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.147 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3256111 | 1 | 88.3453 | 93.4687 | -115.0871 | 9.5217 | 187.0367 | 0.0107 | 0.0196 |
| 2024_09_20 22:00 | 3240140 | 2 | 13.8737 | 12.3383 | -115.5517 | 15.9886 | 126.5224 | 0.0034 | 0.0103 |
| 2024_09_20 22:00 | 3216083 | 3 | 12.3879 | 15.7524 | -115.0786 | 16.8937 | 140.3855 | 0.0085 | 0.0182 |
| 2024_09_20 22:00 | 3226427 | 4 | 8.2336 | 5.0738 | -116.3087 | 5.6387 | 177.8984 | 0.0091 | 0.0155 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415775_528EEDA6 | 504990 | 952 | -89.3 | 504990 | 30 | -98.8 | 504990 | 256 | -98.6 | 504990 | 592 |
| MR_1774415775_777E637E | 504990 | 952 | -89.4 | 504990 | 30 | -98.2 | 504990 | 256 | -99.2 | 504990 | 592 |
| MR_1774415775_174C7BC4 | 504990 | 952 | -88.0 | 504990 | 30 | -98.3 | 504990 | 256 | -102.2 | 504990 | 592 |
| MR_1774415775_C442DB96 | 504990 | 952 | -88.1 | 504990 | 30 | -96.7 | 504990 | 256 | -98.8 | 504990 | 592 |
| MR_1774415775_C15B3555 | 504990 | 952 | -88.6 | 504990 | 30 | -98.7 | 504990 | 256 | -100.9 | 504990 | 592 |
| MR_1774415775_8244E958 | 504990 | 952 | -89.7 | 504990 | 30 | -98.7 | 504990 | 256 | -100.0 | 504990 | 592 |
| MR_1774415775_59A2A91C | 504990 | 952 | -87.2 | 504990 | 30 | -96.4 | 504990 | 256 | -100.9 | 504990 | 592 |
| MR_1774415775_63DC8AEE | 504990 | 952 | -88.7 | 504990 | 30 | -97.0 | 504990 | 256 | -100.1 | 504990 | 592 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 467: `82fd5d5b-00f...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `82fd5d5b-00fc-4d50-b513-5716f982860c` |
| Tag | **single-answer** |
| 정답 | **C13** |
| C13 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3225536_1 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[467] topology](images/train_0467.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3246569_5 by 4 degrees
- `C2`: Decrease A3 Offset threshold for 3246569_5
- `C3`: Increase transmission power for 3225536_1
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3225536_1
- `C5`: Increase transmission power for 3246569_5
- `C6`: Lift the tilt angle of 3225536_1 by 3 degrees
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3246569_5
- `C8`: Insufficient data; more data is needed for judgment.
- `C9`: Increase A3 Offset threshold for 3246569_5
- `C10`: Press down the tilt angle of 3225536_1 by 3 degrees
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3246569_5
- `C12`: Add neighbor relationship between 3228983_9 and 3246569_5
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3225536_1 **← 정답**
- `C14`: Adjust the azimuth of 3225536_1 by 4 degrees
- `C15`: Decrease transmission power for 3246569_5
- `C16`: Check test server and transmission issues
- `C17`: Adjust the azimuth of 3246569_5 by 24 degrees
- `C18`: Add neighbor relationship between 3225536_1 and 3246569_5
- `C19`: Increase A3 Offset threshold for 3225536_1
- `C20`: Decrease A3 Offset threshold for 3225536_1
- `C21`: Decrease transmission power for 3225536_1
- `C22`: Lift the tilt angle  of 3246569_5 by 4 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.686 | MS1 | 121.4656724530 | 31.1446324043 | 264 | 504990 | -93.76 | 11.96 | 359.16 | 0.14 | 2.10 | 1566 |
| 2024-09-20 22:21:32.454 | MS1 | 121.4656718369 | 31.1446221722 | 655 | 504990 | -94.15 | 10.88 | 533.44 | 0.12 | 2.72 | 1599 |
| 2024-09-20 22:21:33.251 | MS1 | 121.4656739526 | 31.1446199061 | 145 | 504990 | -93.04 | 13.25 | 411.88 | 0.06 | 2.86 | 1593 |
| 2024-09-20 22:21:34.785 | MS1 | 121.4656607006 | 31.1446238588 | 213 | 152650 | -91.74 | 2.46 | 77.81 | 0.14 | 1.56 | 910 |
| 2024-09-20 22:21:35.811 | MS1 | 121.4656627136 | 31.1446248016 | 727 | 152650 | -94.85 | 6.89 | 65.85 | 0.14 | 1.83 | 993 |
| 2024-09-20 22:21:36.318 | MS1 | 121.4656630674 | 31.1446325710 | 436 | 152650 | -93.08 | 4.06 | 58.06 | 0.01 | 1.95 | 975 |
| 2024-09-20 22:21:37.361 | MS1 | 121.4656679310 | 31.1446209886 | 188 | 152650 | -87.25 | 2.35 | 92.75 | 0.08 | 1.74 | 930 |
| 2024-09-20 22:21:38.893 | MS1 | 121.4656634135 | 31.1446208502 | 213 | 152650 | -89.36 | 5.54 | 76.19 | 0.05 | 1.84 | 926 |
| 2024-09-20 22:21:39.759 | MS1 | 121.4656602455 | 31.1446365718 | 727 | 152650 | -96.80 | 4.79 | 88.94 | 0.09 | 1.73 | 986 |
| 2024-09-20 22:21:40.166 | MS1 | 121.4656691945 | 31.1446305779 | 436 | 152650 | -91.16 | 2.09 | 49.95 | 0.05 | 2.31 | 1576 |
| 2024-09-20 22:21:41.676 | MS1 | 121.4656723795 | 31.1446250108 | 188 | 152650 | -91.69 | 4.41 | 78.78 | 0.03 | 2.55 | 1597 |
| 2024-09-20 22:21:42.126 | MS1 | 121.4656662488 | 31.1446196837 | 213 | 152650 | -88.92 | 3.62 | 74.99 | 0.20 | 2.51 | 1595 |

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
| 3225536 | 1 | 121.4727650978 | 31.1485130887 | 241 | 2 | 4 | 19.3 | TDD | 264 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3227121 | 11 | 121.4696523863 | 31.1535037727 | 277 | 4 | 9 | 2.4 | FDD | 727 | n1 | 152650 | 30M | 4T4R | 26 | 152650 |
| 3228257 | 6 | 121.4706453724 | 31.1446502440 | 69 | 1 | 3 | 14.2 | TDD | 415 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3228983 | 9 | 121.4671384378 | 31.1520668477 | 207 | 3 | 1 | 4.4 | FDD | 436 | n1 | 152650 | 30M | 4T4R | 29 | 152650 |
| 3232872 | 3 | 121.4733731577 | 31.1461302370 | 353 | 15 | 12 | 29.4 | TDD | 655 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3240914 | 4 | 121.4661470623 | 31.1536220433 | 301 | 4 | 4 | 14.7 | TDD | 145 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3246569 | 5 | 121.4697457387 | 31.1467040647 | 215 | 1 | 0 | 26.8 | TDD | 633 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3251590 | 12 | 121.4741858471 | 31.1473174657 | 278 | 12 | 12 | 10.8 | FDD | 731 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |
| 3255480 | 7 | 121.4675457497 | 31.1487781174 | 130 | 4 | 4 | 3.7 | FDD | 544 | n1 | 152650 | 30M | 4T4R | 27 | 152650 |
| 3260492 | 13 | 121.4730708490 | 31.1500011446 | 8 | 4 | 2 | 3.1 | FDD | 188 | n1 | 152650 | 30M | 4T4R | 21 | 152650 |
| 3262190 | 8 | 121.4718566449 | 31.1492362402 | 8 | 1 | 12 | 12.4 | FDD | 764 | n1 | 152650 | 30M | 4T4R | 18 | 152650 |
| 3270330 | 2 | 121.4683554263 | 31.1539186644 | 41 | 10 | 3 | 9.1 | TDD | 15 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3278202 | 10 | 121.4641404910 | 31.1529796249 | 9 | 5 | 9 | 23.0 | FDD | 213 | n1 | 152650 | 30M | 4T4R | 25 | 152650 |

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
| 2024-09-20 22:21:31.142 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.273 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.273 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.010 | NREventA2 | measId:1;ServCellPCI:331;Se... |
| 2024-09-20 22:21:35.136 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.372 | NREventA5 | measId:3;ServCellPCI:331;Se... |
| 2024-09-20 22:21:35.419 | NRHandoverAttempt | SourcePCI:331;SourceNR-ARFC... |
| 2024-09-20 22:21:35.462 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.477 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:35.582 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.582 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3225536 | 1 | 15.7762 | 13.2474 | -117.0507 | 11.2776 | 125.4324 | 0.0091 | 0.0119 |
| 2024_09_20 22:00 | 3270330 | 2 | 17.7286 | 11.9040 | -117.6925 | 19.1545 | 118.2103 | 0.0001 | 0.0117 |
| 2024_09_20 22:00 | 3232872 | 3 | 16.9419 | 7.9250 | -116.9596 | 13.6750 | 169.0791 | 0.0160 | 0.0177 |
| 2024_09_20 22:00 | 3240914 | 4 | 14.9309 | 13.3394 | -114.4952 | 8.4309 | 187.2912 | 0.0109 | 0.0105 |
| 2024_09_20 22:00 | 3246569 | 5 | 9.7279 | 6.5720 | -116.6848 | 16.9032 | 85.6957 | 0.0133 | 0.0075 |
| 2024_09_20 22:00 | 3228257 | 6 | 12.7294 | 19.3283 | -115.9630 | 8.1707 | 178.4607 | 0.0066 | 0.0197 |
| 2024_09_20 22:00 | 3255480 | 7 | 8.7946 | 9.6984 | -117.1404 | 4.9814 | 21.8543 | 0.0052 | 0.0048 |
| 2024_09_20 22:00 | 3262190 | 8 | 9.5343 | 8.6384 | -117.1599 | 4.3593 | 52.2068 | 0.0021 | 0.0163 |
| 2024_09_20 22:00 | 3228983 | 9 | 13.9117 | 19.5566 | -114.6783 | 3.5913 | 27.2232 | 0.0017 | 0.0032 |
| 2024_09_20 22:00 | 3278202 | 10 | 10.3313 | 13.9564 | -116.1041 | 4.8532 | 43.8031 | 0.0122 | 0.0063 |
| 2024_09_20 22:00 | 3227121 | 11 | 15.2105 | 8.4954 | -114.1207 | 4.6296 | 57.4150 | 0.0008 | 0.0094 |
| 2024_09_20 22:00 | 3251590 | 12 | 15.2841 | 13.9799 | -114.1347 | 3.6842 | 43.2439 | 0.0161 | 0.0186 |
| 2024_09_20 22:00 | 3260492 | 13 | 11.1040 | 16.1413 | -114.9707 | 3.0920 | 23.3028 | 0.0183 | 0.0130 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414827_48EECADF | 504990 | 145 | -94.9 | 504990 | 633 | -89.9 | 504990 | 15 | -97.3 | 504990 | 415 |
| MR_1774414827_9B50E482 | 152650 | 213 | -92.1 | 152650 | 731 | -99.5 | 152650 | 544 | -100.7 | 152650 | 764 |
| MR_1774414827_DA37E625 | 504990 | 145 | -93.9 | 504990 | 633 | -90.8 | 504990 | 15 | -98.0 | 504990 | 415 |
| MR_1774414827_E76DDFFE | 504990 | 145 | -94.5 | 504990 | 633 | -89.7 | 504990 | 15 | -97.0 | 504990 | 415 |
| MR_1774414827_19F7C767 | 152650 | 213 | -93.2 | 152650 | 731 | -100.5 | 152650 | 544 | -102.6 | 152650 | 764 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 468: `22ea59ad-f36...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `22ea59ad-f361-45c3-8f43-2605b6664b6d` |
| Tag | **single-answer** |
| 정답 | **C1** |
| C1 의미 | Add neighbor relationship between 3231459_4 and 3228654_2 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[468] topology](images/train_0468.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3231459_4 and 3228654_2 **← 정답**
- `C2`: Press down the tilt angle  of 3228654_2 by 5 degrees
- `C3`: Increase transmission power for 3228654_2
- `C4`: Increase A3 Offset threshold for 3231459_4
- `C5`: Lift the tilt angle  of 3228654_2 by 5 degrees
- `C6`: Press down the tilt angle of 3231459_4 by 10 degrees
- `C7`: Adjust the azimuth of 3228654_2 by 18 degrees
- `C8`: Check test server and transmission issues
- `C9`: Insufficient data; more data is needed for judgment.
- `C10`: Add neighbor relationship between 3223734_1 and 3228654_2
- `C11`: Decrease transmission power for 3231459_4
- `C12`: Decrease A3 Offset threshold for 3228654_2
- `C13`: Increase transmission power for 3231459_4
- `C14`: Increase A3 Offset threshold for 3228654_2
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3228654_2
- `C16`: Adjust the azimuth of 3231459_4 by 16 degrees
- `C17`: Decrease transmission power for 3228654_2
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3228654_2
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3231459_4
- `C20`: Decrease A3 Offset threshold for 3231459_4
- `C21`: Lift the tilt angle of 3231459_4 by 10 degrees
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3231459_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.446 | MS1 | 121.4656639917 | 31.1446241439 | 22 | 504990 | -83.92 | 12.90 | 520.01 | 0.19 | 2.43 | 1598 |
| 2024-09-20 22:21:32.262 | MS1 | 121.4656613921 | 31.1446305713 | 22 | 504990 | -78.22 | 13.67 | 564.97 | 0.14 | 2.71 | 1567 |
| 2024-09-20 22:21:33.922 | MS1 | 121.4656596826 | 31.1446377331 | 22 | 504990 | -75.50 | 12.56 | 349.92 | 0.16 | 2.28 | 1597 |
| 2024-09-20 22:21:34.638 | MS1 | 121.4656769121 | 31.1446334611 | 22 | 504990 | -91.98 | -2.07 | 27.24 | 0.18 | 1.13 | 1578 |
| 2024-09-20 22:21:35.982 | MS1 | 121.4656652083 | 31.1446235993 | 22 | 504990 | -88.71 | -1.15 | 39.14 | 0.12 | 1.02 | 1580 |
| 2024-09-20 22:21:36.955 | MS1 | 121.4656646514 | 31.1446345477 | 22 | 504990 | -86.34 | -1.45 | 49.59 | 0.20 | 1.38 | 1575 |
| 2024-09-20 22:21:37.803 | MS1 | 121.4656706694 | 31.1446271303 | 22 | 504990 | -94.75 | -1.50 | 40.34 | 0.03 | 1.45 | 1568 |
| 2024-09-20 22:21:38.727 | MS1 | 121.4656642910 | 31.1446273306 | 22 | 504990 | -81.02 | 16.81 | 387.19 | 0.17 | 1.07 | 1572 |
| 2024-09-20 22:21:39.513 | MS1 | 121.4656598476 | 31.1446308832 | 22 | 504990 | -78.43 | 17.77 | 554.29 | 0.12 | 1.49 | 1593 |
| 2024-09-20 22:21:40.348 | MS1 | 121.4656746659 | 31.1446375197 | 22 | 504990 | -78.39 | 13.93 | 474.51 | 0.13 | 2.62 | 1597 |
| 2024-09-20 22:21:41.589 | MS1 | 121.4656766605 | 31.1446377933 | 22 | 504990 | -82.52 | 14.89 | 562.55 | 0.01 | 2.40 | 1596 |
| 2024-09-20 22:21:42.938 | MS1 | 121.4656642765 | 31.1446334196 | 22 | 504990 | -84.77 | 14.64 | 338.80 | 0.04 | 2.27 | 1594 |

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
| 3223734 | 1 | 121.4643499442 | 31.1540546053 | 99 | 0 | 11 | 33.8 | TDD | 2 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3228654 | 2 | 121.4685805555 | 31.1467580791 | 211 | 0 | 1 | 29.3 | TDD | 459 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3231459 | 4 | 121.4751179262 | 31.1469600669 | 238 | 11 | 7 | 27.8 | TDD | 22 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3259683 | 3 | 121.4732294608 | 31.1522477296 | 357 | 7 | 10 | 45.8 | TDD | 443 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |

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
| 2024-09-20 22:21:31.484 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.504 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.652 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.652 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.370 | NREventA3 | measId:2;ServCellPCI:504;Se... |
| 2024-09-20 22:21:36.370 | NREventA3 | measId:2;ServCellPCI:504;Se... |
| 2024-09-20 22:21:37.370 | NREventA3 | measId:2;ServCellPCI:504;Se... |
| 2024-09-20 22:21:39.870 | NRRRCReestablishAttempt | PCI:504 |
| 2024-09-20 22:21:39.888 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.899 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:40.034 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:40.034 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3223734 | 1 | 6.9169 | 7.6233 | -116.0219 | 9.3757 | 124.8652 | 0.0021 | 0.0137 |
| 2024_09_20 22:00 | 3228654 | 2 | 9.8166 | 18.5053 | -116.1358 | 19.6066 | 115.3046 | 0.0146 | 0.0007 |
| 2024_09_20 22:00 | 3259683 | 3 | 17.7217 | 7.0437 | -116.7452 | 12.7564 | 170.9751 | 0.0191 | 0.0177 |
| 2024_09_20 22:00 | 3231459 | 4 | 7.8142 | 16.3119 | -114.8489 | 16.3327 | 156.5590 | 0.0158 | 0.1983 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412481_702FDFE0 | 504990 | 22 | -92.0 | 504990 | 459 | -85.6 | 504990 | 2 | -87.6 | 504990 | 443 |
| MR_1774412481_8ED0F97D | 504990 | 459 | -89.2 | 504990 | 22 | -93.4 | 504990 | 2 | -87.4 | 504990 | 443 |
| MR_1774412481_312AF349 | 504990 | 22 | -91.4 | 504990 | 459 | -89.2 | 504990 | 2 | -86.4 | 504990 | 443 |
| MR_1774412481_F5B38FCC | 504990 | 459 | -88.1 | 504990 | 22 | -91.7 | 504990 | 2 | -87.7 | 504990 | 443 |
| MR_1774412481_2F1D393C | 504990 | 459 | -89.2 | 504990 | 22 | -92.8 | 504990 | 2 | -86.5 | 504990 | 443 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 469: `c6766881-ee0...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `c6766881-ee0d-4142-b7fe-d4f4b9966b6d` |
| Tag | **single-answer** |
| 정답 | **C3** |
| C3 의미 | Lift the tilt angle  of 3277232_4 by 7 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[469] topology](images/train_0469.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3221641_2
- `C2`: Press down the tilt angle of 3221641_2 by 5 degrees
- `C3`: Lift the tilt angle  of 3277232_4 by 7 degrees **← 정답**
- `C4`: Decrease A3 Offset threshold for 3221641_2
- `C5`: Adjust the azimuth of 3221641_2 by 39 degrees
- `C6`: Increase A3 Offset threshold for 3279534_1
- `C7`: Add neighbor relationship between 3221641_2 and 3279534_1
- `C8`: Decrease transmission power for 3279534_1
- `C9`: Decrease transmission power for 3221641_2
- `C10`: Adjust the azimuth of 3277232_4 by 38 degrees
- `C11`: Decrease A3 Offset threshold for 3279534_1
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3279534_1
- `C13`: Check test server and transmission issues
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3279534_1
- `C15`: Increase A3 Offset threshold for 3221641_2
- `C16`: Press down the tilt angle  of 3277232_4 by 7 degrees
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3221641_2
- `C18`: Lift the tilt angle of 3221641_2 by 5 degrees
- `C19`: Add neighbor relationship between 3277232_4 and 3279534_1
- `C20`: Increase transmission power for 3221641_2
- `C21`: Increase transmission power for 3279534_1
- `C22`: Insufficient data; more data is needed for judgment.

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.455 | MS1 | 121.4656655363 | 31.1446293573 | 453 | 504990 | -89.76 | 13.25 | 456.57 | 0.07 | 2.98 | 1593 |
| 2024-09-20 22:21:32.757 | MS1 | 121.4656705895 | 31.1446248794 | 453 | 504990 | -85.73 | 16.74 | 355.94 | 0.06 | 2.66 | 1574 |
| 2024-09-20 22:21:33.470 | MS1 | 121.4656753812 | 31.1446251443 | 453 | 504990 | -90.77 | 13.32 | 387.99 | 0.18 | 2.32 | 1577 |
| 2024-09-20 22:21:34.225 | MS1 | 121.4656706069 | 31.1446312911 | 453 | 504990 | -90.59 | 15.92 | 82.99 | 0.06 | 2.28 | 1583 |
| 2024-09-20 22:21:35.495 | MS1 | 121.4656749631 | 31.1446220961 | 453 | 504990 | -87.76 | 12.59 | 78.67 | 0.05 | 2.49 | 1563 |
| 2024-09-20 22:21:36.318 | MS1 | 121.4656719407 | 31.1446187948 | 453 | 504990 | -90.66 | 14.67 | 84.95 | 0.06 | 2.28 | 1585 |
| 2024-09-20 22:21:37.374 | MS1 | 121.4656744149 | 31.1446223745 | 453 | 504990 | -93.39 | 12.70 | 78.33 | 0.07 | 2.39 | 1593 |
| 2024-09-20 22:21:38.831 | MS1 | 121.4656719315 | 31.1446320402 | 453 | 504990 | -90.64 | 8.92 | 87.47 | 0.11 | 2.05 | 1572 |
| 2024-09-20 22:21:39.958 | MS1 | 121.4656663194 | 31.1446181525 | 453 | 504990 | -90.19 | 8.09 | 65.36 | 0.05 | 2.40 | 1568 |
| 2024-09-20 22:21:40.247 | MS1 | 121.4656615774 | 31.1446298472 | 453 | 504990 | -92.76 | 9.08 | 527.70 | 0.13 | 2.71 | 1581 |
| 2024-09-20 22:21:41.595 | MS1 | 121.4656633129 | 31.1446221416 | 453 | 504990 | -89.06 | 11.96 | 361.22 | 0.15 | 2.90 | 1596 |
| 2024-09-20 22:21:42.924 | MS1 | 121.4656713481 | 31.1446253935 | 453 | 504990 | -90.98 | 11.70 | 575.25 | 0.02 | 2.56 | 1564 |

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
| 3214361 | 3 | 121.4700149159 | 31.1513909655 | 343 | 4 | 3 | 32.6 | TDD | 366 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3221641 | 2 | 121.4712306884 | 31.1552722298 | 243 | 4 | 1 | 28.1 | TDD | 453 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3277232 | 4 | 121.4708738397 | 31.1515641016 | 62 | 9 | 8 | 34.2 | TDD | 151 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3279534 | 1 | 121.4745175998 | 31.1441567171 | 235 | 5 | 10 | 34.5 | TDD | 458 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |

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
| 2024-09-20 22:21:30.845 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.864 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:30.995 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.995 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.720 | NREventA3 | measId:2;ServCellPCI:147;Se... |
| 2024-09-20 22:21:37.960 | NRHandoverAttempt | SourcePCI:147;SourceNR-ARFC... |
| 2024-09-20 22:21:37.998 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.008 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.136 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.136 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3279534 | 1 | 17.3361 | 12.7427 | -115.8762 | 18.5164 | 111.6544 | 0.0109 | 0.0120 |
| 2024_09_20 22:00 | 3221641 | 2 | 87.2991 | 82.5249 | -116.6396 | 13.3932 | 114.5096 | 0.0139 | 0.0178 |
| 2024_09_20 22:00 | 3214361 | 3 | 16.7449 | 8.3361 | -117.2424 | 5.4634 | 171.3005 | 0.0130 | 0.0062 |
| 2024_09_20 22:00 | 3277232 | 4 | 8.1005 | 7.8398 | -117.9520 | 11.4752 | 117.0216 | 0.0130 | 0.0006 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412496_4D4326A7 | 504990 | 453 | -89.0 | 504990 | 458 | -91.9 | 504990 | 151 | -101.4 | 504990 | 366 |
| MR_1774412496_3116A009 | 504990 | 453 | -89.1 | 504990 | 458 | -95.3 | 504990 | 151 | -99.7 | 504990 | 366 |
| MR_1774412496_DB82FBCA | 504990 | 453 | -89.5 | 504990 | 458 | -92.5 | 504990 | 151 | -103.0 | 504990 | 366 |
| MR_1774412496_ECE93B96 | 504990 | 453 | -92.1 | 504990 | 458 | -93.6 | 504990 | 151 | -100.5 | 504990 | 366 |
| MR_1774412496_8C4D9B7D | 504990 | 453 | -92.3 | 504990 | 458 | -94.2 | 504990 | 151 | -101.4 | 504990 | 366 |

> *... 2개 열 생략 (전체 14열)*

---
