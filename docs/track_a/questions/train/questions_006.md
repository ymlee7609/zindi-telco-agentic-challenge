# Track A 문제 분석 — train[50]~train[59]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[50] ~ train[59] (10개)

## 목차

1. [문제 50: `1d92f2d3-75b...`](#50) — single-answer, 정답: C22
2. [문제 51: `5ba4b75f-be5...`](#51) — single-answer, 정답: C11
3. [문제 52: `a7003713-305...`](#52) — single-answer, 정답: C8
4. [문제 53: `165a6ae4-40b...`](#53) — single-answer, 정답: C11
5. [문제 54: `68d174ff-984...`](#54) — single-answer, 정답: C19
6. [문제 55: `65fa7046-5a8...`](#55) — single-answer, 정답: C6
7. [문제 56: `c708f6a4-cc4...`](#56) — single-answer, 정답: C6
8. [문제 57: `0e65f7cf-ebd...`](#57) — single-answer, 정답: C10
9. [문제 58: `116a8416-594...`](#58) — single-answer, 정답: C3
10. [문제 59: `a44aaa5b-c78...`](#59) — single-answer, 정답: C7

---

### 문제 50: `1d92f2d3-75b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `1d92f2d3-75ba-4186-8077-d75c78423be0` |
| Tag | **single-answer** |
| 정답 | **C22** |
| C22 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3232028_4 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[50] topology](images/train_0050.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3233731_1
- `C2`: Adjust the azimuth of 3233731_1 by 50 degrees
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3232028_4
- `C4`: Check test server and transmission issues
- `C5`: Increase A3 Offset threshold for 3232028_4
- `C6`: Adjust the azimuth of 3232028_4 by 40 degrees
- `C7`: Lift the tilt angle of 3232028_4 by 5 degrees
- `C8`: Decrease A3 Offset threshold for 3232028_4
- `C9`: Insufficient data; more data is needed for judgment.
- `C10`: Lift the tilt angle  of 3233731_1 by 10 degrees
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3233731_1
- `C12`: Increase transmission power for 3233731_1
- `C13`: Add neighbor relationship between 3210001_3 and 3233731_1
- `C14`: Press down the tilt angle of 3232028_4 by 5 degrees
- `C15`: Add neighbor relationship between 3232028_4 and 3233731_1
- `C16`: Decrease transmission power for 3233731_1
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3233731_1
- `C18`: Press down the tilt angle  of 3233731_1 by 10 degrees
- `C19`: Decrease transmission power for 3232028_4
- `C20`: Increase transmission power for 3232028_4
- `C21`: Decrease A3 Offset threshold for 3233731_1
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3232028_4 **← 정답**

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.466 | MS1 | 121.4656608662 | 31.1446195844 | 191 | 504990 | -89.78 | 15.72 | 423.08 | 0.06 | 2.62 | 1598 |
| 2024-09-20 22:21:32.355 | MS1 | 121.4656760101 | 31.1446214811 | 191 | 504990 | -91.01 | 13.63 | 544.40 | 0.00 | 2.99 | 1591 |
| 2024-09-20 22:21:33.378 | MS1 | 121.4656661615 | 31.1446220281 | 191 | 504990 | -85.86 | 16.94 | 325.31 | 0.16 | 2.84 | 1590 |
| 2024-09-20 22:21:34.620 | MS1 | 121.4656651942 | 31.1446195588 | 191 | 504990 | -91.09 | 14.74 | 70.72 | 0.60 | 2.51 | 625 |
| 2024-09-20 22:21:35.124 | MS1 | 121.4656630558 | 31.1446341335 | 191 | 504990 | -91.52 | 14.02 | 70.25 | 0.52 | 2.96 | 548 |
| 2024-09-20 22:21:36.826 | MS1 | 121.4656778965 | 31.1446346358 | 191 | 504990 | -89.79 | 16.16 | 61.75 | 0.70 | 2.23 | 592 |
| 2024-09-20 22:21:37.607 | MS1 | 121.4656598076 | 31.1446231972 | 191 | 504990 | -90.85 | 9.86 | 93.88 | 0.66 | 2.94 | 530 |
| 2024-09-20 22:21:38.558 | MS1 | 121.4656623341 | 31.1446210580 | 191 | 504990 | -89.88 | 8.84 | 89.83 | 0.59 | 2.16 | 528 |
| 2024-09-20 22:21:39.419 | MS1 | 121.4656762716 | 31.1446335940 | 191 | 504990 | -92.98 | 9.43 | 81.32 | 0.50 | 2.07 | 573 |
| 2024-09-20 22:21:40.336 | MS1 | 121.4656667859 | 31.1446355901 | 191 | 504990 | -89.18 | 7.14 | 562.72 | 0.19 | 2.82 | 1593 |
| 2024-09-20 22:21:41.908 | MS1 | 121.4656669966 | 31.1446368987 | 191 | 504990 | -90.17 | 7.09 | 493.60 | 0.07 | 2.14 | 1562 |
| 2024-09-20 22:21:42.152 | MS1 | 121.4656609674 | 31.1446294777 | 191 | 504990 | -89.75 | 11.61 | 527.56 | 0.15 | 2.37 | 1577 |

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
| 3210001 | 3 | 121.4749226227 | 31.1462272957 | 14 | 0 | 6 | 32.8 | TDD | 958 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3232028 | 4 | 121.4656552855 | 31.1524243296 | 220 | 4 | 5 | 22.0 | TDD | 191 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3233731 | 1 | 121.4662702391 | 31.1501821818 | 30 | 7 | 10 | 44.9 | TDD | 10 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3250616 | 2 | 121.4679486907 | 31.1472640257 | 323 | 12 | 8 | 45.6 | TDD | 308 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:31.429 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.445 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.556 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.556 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.255 | NREventA3 | measId:2;ServCellPCI:106;Se... |
| 2024-09-20 22:21:38.495 | NRHandoverAttempt | SourcePCI:106;SourceNR-ARFC... |
| 2024-09-20 22:21:38.543 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.557 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.695 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.695 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3233731 | 1 | 14.4106 | 12.6023 | -114.6697 | 15.3225 | 154.0775 | 0.0182 | 0.0068 |
| 2024_09_20 22:00 | 3250616 | 2 | 11.0200 | 5.5024 | -115.6287 | 8.9545 | 108.7701 | 0.0154 | 0.0124 |
| 2024_09_20 22:00 | 3210001 | 3 | 10.7217 | 12.4178 | -114.6892 | 12.9226 | 92.6167 | 0.0016 | 0.0016 |
| 2024_09_20 22:00 | 3232028 | 4 | 6.6371 | 19.3167 | -114.1650 | 18.1898 | 156.9991 | 0.0119 | 0.0017 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416434_EE8A140B | 504990 | 191 | -92.6 | 504990 | 10 | -94.9 | 504990 | 958 | -98.9 | 504990 | 308 |
| MR_1774416434_D3D0B8C3 | 504990 | 191 | -92.8 | 504990 | 10 | -93.5 | 504990 | 958 | -101.6 | 504990 | 308 |
| MR_1774416434_253E4DB2 | 504990 | 191 | -92.1 | 504990 | 10 | -94.5 | 504990 | 958 | -98.9 | 504990 | 308 |
| MR_1774416434_B24CA7FE | 504990 | 191 | -92.5 | 504990 | 10 | -96.9 | 504990 | 958 | -99.5 | 504990 | 308 |
| MR_1774416434_E67F7723 | 504990 | 191 | -90.2 | 504990 | 10 | -93.7 | 504990 | 958 | -100.4 | 504990 | 308 |
| MR_1774416434_CC59FBC8 | 504990 | 191 | -90.9 | 504990 | 10 | -95.9 | 504990 | 958 | -99.7 | 504990 | 308 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 51: `5ba4b75f-be5...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `5ba4b75f-be5f-414a-8bfe-6014fdc5de6f` |
| Tag | **single-answer** |
| 정답 | **C11** |
| C11 의미 | Lift the tilt angle  of 3256064_3 by 6 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[51] topology](images/train_0051.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3275227_4
- `C2`: Increase transmission power for 3237135_2
- `C3`: Press down the tilt angle of 3275227_4 by 5 degrees
- `C4`: Check test server and transmission issues
- `C5`: Decrease transmission power for 3237135_2
- `C6`: Insufficient data; more data is needed for judgment.
- `C7`: Increase transmission power for 3275227_4
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3237135_2
- `C9`: Decrease A3 Offset threshold for 3275227_4
- `C10`: Press down the tilt angle  of 3256064_3 by 6 degrees
- `C11`: Lift the tilt angle  of 3256064_3 by 6 degrees **← 정답**
- `C12`: Adjust the azimuth of 3256064_3 by 50 degrees
- `C13`: Add neighbor relationship between 3256064_3 and 3237135_2
- `C14`: Increase A3 Offset threshold for 3237135_2
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3237135_2
- `C16`: Lift the tilt angle of 3275227_4 by 5 degrees
- `C17`: Adjust the azimuth of 3275227_4 by 29 degrees
- `C18`: Decrease A3 Offset threshold for 3237135_2
- `C19`: Decrease transmission power for 3275227_4
- `C20`: Add neighbor relationship between 3275227_4 and 3237135_2
- `C21`: Increase A3 Offset threshold for 3275227_4
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3275227_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.395 | MS1 | 121.4656588370 | 31.1446203017 | 463 | 504990 | -86.95 | 12.79 | 448.76 | 0.13 | 2.84 | 1597 |
| 2024-09-20 22:21:32.534 | MS1 | 121.4656726519 | 31.1446275432 | 463 | 504990 | -89.46 | 15.81 | 587.48 | 0.04 | 2.11 | 1560 |
| 2024-09-20 22:21:33.483 | MS1 | 121.4656737659 | 31.1446264733 | 463 | 504990 | -85.33 | 17.70 | 449.50 | 0.15 | 2.91 | 1597 |
| 2024-09-20 22:21:34.922 | MS1 | 121.4656743860 | 31.1446354917 | 463 | 504990 | -90.11 | 15.62 | 63.78 | 0.12 | 2.74 | 1594 |
| 2024-09-20 22:21:35.962 | MS1 | 121.4656615331 | 31.1446346431 | 463 | 504990 | -85.18 | 15.72 | 68.15 | 0.17 | 2.66 | 1585 |
| 2024-09-20 22:21:36.346 | MS1 | 121.4656607248 | 31.1446313348 | 463 | 504990 | -88.65 | 16.70 | 50.11 | 0.03 | 2.24 | 1594 |
| 2024-09-20 22:21:37.618 | MS1 | 121.4656622116 | 31.1446283166 | 463 | 504990 | -89.27 | 10.11 | 68.76 | 0.08 | 2.44 | 1577 |
| 2024-09-20 22:21:38.264 | MS1 | 121.4656700016 | 31.1446362040 | 463 | 504990 | -91.22 | 12.43 | 86.64 | 0.18 | 2.01 | 1574 |
| 2024-09-20 22:21:39.206 | MS1 | 121.4656736621 | 31.1446342071 | 463 | 504990 | -89.80 | 8.74 | 99.01 | 0.14 | 2.62 | 1564 |
| 2024-09-20 22:21:40.170 | MS1 | 121.4656746840 | 31.1446314850 | 463 | 504990 | -89.45 | 8.23 | 327.83 | 0.11 | 2.77 | 1597 |
| 2024-09-20 22:21:41.750 | MS1 | 121.4656668502 | 31.1446369233 | 463 | 504990 | -93.26 | 11.24 | 494.35 | 0.19 | 2.72 | 1592 |
| 2024-09-20 22:21:42.551 | MS1 | 121.4656664327 | 31.1446259870 | 463 | 504990 | -89.44 | 7.70 | 324.27 | 0.20 | 2.62 | 1577 |

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
| 3220398 | 1 | 121.4753541484 | 31.1491140439 | 309 | 4 | 12 | 35.8 | TDD | 64 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3237135 | 2 | 121.4747501018 | 31.1445002153 | 199 | 4 | 6 | 27.1 | TDD | 934 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3256064 | 3 | 121.4736732481 | 31.1541200093 | 113 | 2 | 12 | 43.0 | TDD | 438 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3275227 | 4 | 121.4713123672 | 31.1467829037 | 275 | 0 | 9 | 48.1 | TDD | 463 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

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
| 2024-09-20 22:21:30.895 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.917 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.062 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.062 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.732 | NREventA3 | measId:2;ServCellPCI:361;Se... |
| 2024-09-20 22:21:37.972 | NRHandoverAttempt | SourcePCI:361;SourceNR-ARFC... |
| 2024-09-20 22:21:38.002 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.014 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.142 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.142 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3220398 | 1 | 15.6559 | 14.5466 | -117.6164 | 9.9380 | 148.3090 | 0.0155 | 0.0185 |
| 2024_09_20 22:00 | 3237135 | 2 | 18.8922 | 15.9419 | -114.9834 | 17.2578 | 136.0161 | 0.0033 | 0.0020 |
| 2024_09_20 22:00 | 3256064 | 3 | 11.0415 | 17.7508 | -115.2726 | 11.2655 | 142.1503 | 0.0180 | 0.0145 |
| 2024_09_20 22:00 | 3275227 | 4 | 76.5866 | 87.8617 | -117.9054 | 11.3479 | 116.9277 | 0.0036 | 0.0120 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415943_0FAB6217 | 504990 | 463 | -89.8 | 504990 | 934 | -96.4 | 504990 | 438 | -105.7 | 504990 | 64 |
| MR_1774415943_40498EC4 | 504990 | 463 | -91.4 | 504990 | 934 | -97.3 | 504990 | 438 | -103.9 | 504990 | 64 |
| MR_1774415943_A934FA02 | 504990 | 463 | -89.5 | 504990 | 934 | -95.4 | 504990 | 438 | -105.6 | 504990 | 64 |
| MR_1774415943_ECD65720 | 504990 | 463 | -91.8 | 504990 | 934 | -97.3 | 504990 | 438 | -105.4 | 504990 | 64 |
| MR_1774415943_D6E9C938 | 504990 | 463 | -88.5 | 504990 | 934 | -95.6 | 504990 | 438 | -102.7 | 504990 | 64 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 52: `a7003713-305...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `a7003713-305c-4d54-a53b-fa4673f85096` |
| Tag | **single-answer** |
| 정답 | **C8** |
| C8 의미 | Add neighbor relationship between 3223709_1 and 3215535_3 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[52] topology](images/train_0052.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3223709_1
- `C2`: Press down the tilt angle of 3223709_1 by 10 degrees
- `C3`: Increase transmission power for 3223709_1
- `C4`: Decrease transmission power for 3223709_1
- `C5`: Decrease A3 Offset threshold for 3215535_3
- `C6`: Decrease transmission power for 3215535_3
- `C7`: Check test server and transmission issues
- `C8`: Add neighbor relationship between 3223709_1 and 3215535_3 **← 정답**
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3215535_3
- `C10`: Increase transmission power for 3215535_3
- `C11`: Lift the tilt angle of 3223709_1 by 10 degrees
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3215535_3
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3223709_1
- `C14`: Increase A3 Offset threshold for 3215535_3
- `C15`: Lift the tilt angle  of 3215535_3 by 3 degrees
- `C16`: Add neighbor relationship between 3210633_4 and 3215535_3
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3223709_1
- `C18`: Adjust the azimuth of 3223709_1 by 50 degrees
- `C19`: Adjust the azimuth of 3215535_3 by 1 degrees
- `C20`: Insufficient data; more data is needed for judgment.
- `C21`: Press down the tilt angle  of 3215535_3 by 3 degrees
- `C22`: Decrease A3 Offset threshold for 3223709_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.937 | MS1 | 121.4656644764 | 31.1446342669 | 514 | 504990 | -78.56 | 17.64 | 591.22 | 0.18 | 2.93 | 1596 |
| 2024-09-20 22:21:32.944 | MS1 | 121.4656774966 | 31.1446327563 | 514 | 504990 | -75.36 | 13.80 | 485.69 | 0.03 | 2.47 | 1587 |
| 2024-09-20 22:21:33.323 | MS1 | 121.4656628495 | 31.1446284146 | 514 | 504990 | -84.57 | 16.56 | 388.34 | 0.07 | 2.55 | 1562 |
| 2024-09-20 22:21:34.930 | MS1 | 121.4656681189 | 31.1446202354 | 514 | 504990 | -88.31 | -0.69 | 55.12 | 0.18 | 1.46 | 1574 |
| 2024-09-20 22:21:35.623 | MS1 | 121.4656644070 | 31.1446329645 | 514 | 504990 | -90.52 | -3.89 | 57.89 | 0.13 | 1.11 | 1582 |
| 2024-09-20 22:21:36.647 | MS1 | 121.4656655070 | 31.1446189638 | 514 | 504990 | -89.60 | -2.57 | 25.01 | 0.10 | 1.39 | 1569 |
| 2024-09-20 22:21:37.997 | MS1 | 121.4656603049 | 31.1446249205 | 514 | 504990 | -93.34 | -0.61 | 55.28 | 0.03 | 1.23 | 1595 |
| 2024-09-20 22:21:38.773 | MS1 | 121.4656593604 | 31.1446189679 | 514 | 504990 | -79.40 | 13.25 | 409.06 | 0.12 | 1.43 | 1597 |
| 2024-09-20 22:21:39.446 | MS1 | 121.4656661005 | 31.1446305066 | 514 | 504990 | -84.43 | 14.49 | 456.27 | 0.16 | 1.22 | 1564 |
| 2024-09-20 22:21:40.479 | MS1 | 121.4656642355 | 31.1446297908 | 514 | 504990 | -78.14 | 13.31 | 454.74 | 0.18 | 2.07 | 1598 |
| 2024-09-20 22:21:41.647 | MS1 | 121.4656664492 | 31.1446361516 | 514 | 504990 | -77.02 | 13.43 | 502.00 | 0.07 | 2.65 | 1597 |
| 2024-09-20 22:21:42.535 | MS1 | 121.4656764464 | 31.1446330132 | 514 | 504990 | -81.76 | 12.80 | 295.28 | 0.07 | 2.30 | 1563 |

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
| 3210633 | 4 | 121.4705658211 | 31.1503412578 | 18 | 8 | 12 | 18.1 | TDD | 831 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3215535 | 3 | 121.4681830468 | 31.1488717404 | 208 | 1 | 9 | 15.1 | TDD | 550 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3223709 | 1 | 121.4661409126 | 31.1441810781 | 89 | 11 | 6 | 41.3 | TDD | 514 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3275467 | 2 | 121.4640212286 | 31.1520235655 | 311 | 2 | 8 | 28.4 | TDD | 165 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |

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
| 2024-09-20 22:21:31.473 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.492 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.593 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.593 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.363 | NREventA3 | measId:2;ServCellPCI:956;Se... |
| 2024-09-20 22:21:36.363 | NREventA3 | measId:2;ServCellPCI:956;Se... |
| 2024-09-20 22:21:37.363 | NREventA3 | measId:2;ServCellPCI:956;Se... |
| 2024-09-20 22:21:39.863 | NRRRCReestablishAttempt | PCI:956 |
| 2024-09-20 22:21:39.881 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.893 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:40.038 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:40.038 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3223709 | 1 | 18.0588 | 6.6159 | -117.7719 | 5.3845 | 150.7751 | 0.0064 | 0.1052 |
| 2024_09_20 22:00 | 3275467 | 2 | 7.3705 | 16.7287 | -116.0031 | 8.7020 | 124.0231 | 0.0051 | 0.0093 |
| 2024_09_20 22:00 | 3215535 | 3 | 11.8773 | 5.4055 | -114.4429 | 13.1298 | 156.7266 | 0.0184 | 0.0136 |
| 2024_09_20 22:00 | 3210633 | 4 | 18.9089 | 12.9029 | -116.8457 | 15.0025 | 152.4586 | 0.0153 | 0.0156 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415820_D361BD1B | 504990 | 550 | -80.8 | 504990 | 514 | -90.0 | 504990 | 831 | -91.8 | 504990 | 165 |
| MR_1774415820_EBC4294D | 504990 | 550 | -82.9 | 504990 | 514 | -90.3 | 504990 | 831 | -95.0 | 504990 | 165 |
| MR_1774415820_7512A6AB | 504990 | 514 | -89.9 | 504990 | 550 | -82.5 | 504990 | 831 | -93.0 | 504990 | 165 |
| MR_1774415820_E8175A5B | 504990 | 514 | -86.8 | 504990 | 550 | -82.8 | 504990 | 831 | -93.6 | 504990 | 165 |
| MR_1774415820_6AABFD27 | 504990 | 550 | -83.7 | 504990 | 514 | -89.8 | 504990 | 831 | -92.9 | 504990 | 165 |
| MR_1774415820_E22C01A5 | 504990 | 514 | -88.6 | 504990 | 550 | -83.4 | 504990 | 831 | -93.9 | 504990 | 165 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 53: `165a6ae4-40b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `165a6ae4-40b1-4675-becf-ddc2125a51c2` |
| Tag | **single-answer** |
| 정답 | **C11** |
| C11 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3246914_1 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[53] topology](images/train_0053.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3246914_1 by 5 degrees
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3249712_4
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3249712_4
- `C4`: Add neighbor relationship between 3246914_1 and 3249712_4
- `C5`: Increase transmission power for 3246914_1
- `C6`: Decrease transmission power for 3249712_4
- `C7`: Increase A3 Offset threshold for 3249712_4
- `C8`: Decrease A3 Offset threshold for 3246914_1
- `C9`: Lift the tilt angle  of 3249712_4 by 6 degrees
- `C10`: Adjust the azimuth of 3249712_4 by 50 degrees
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3246914_1 **← 정답**
- `C12`: Adjust the azimuth of 3246914_1 by 47 degrees
- `C13`: Increase A3 Offset threshold for 3246914_1
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Check test server and transmission issues
- `C16`: Decrease transmission power for 3246914_1
- `C17`: Decrease A3 Offset threshold for 3249712_4
- `C18`: Press down the tilt angle of 3246914_1 by 5 degrees
- `C19`: Press down the tilt angle  of 3249712_4 by 6 degrees
- `C20`: Add neighbor relationship between 3277055_3 and 3249712_4
- `C21`: Increase transmission power for 3249712_4
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3246914_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.963 | MS1 | 121.4656628861 | 31.1446358166 | 553 | 504990 | -89.88 | 15.19 | 589.59 | 0.20 | 2.29 | 1583 |
| 2024-09-20 22:21:32.374 | MS1 | 121.4656682040 | 31.1446281358 | 553 | 504990 | -90.39 | 14.77 | 343.76 | 0.12 | 2.88 | 1582 |
| 2024-09-20 22:21:33.437 | MS1 | 121.4656617170 | 31.1446188814 | 553 | 504990 | -90.91 | 12.17 | 559.24 | 0.12 | 2.79 | 1564 |
| 2024-09-20 22:21:34.223 | MS1 | 121.4656585182 | 31.1446192381 | 553 | 504990 | -88.83 | 15.14 | 78.61 | 0.52 | 2.98 | 603 |
| 2024-09-20 22:21:35.139 | MS1 | 121.4656738317 | 31.1446192032 | 553 | 504990 | -85.45 | 13.83 | 73.88 | 0.57 | 2.72 | 636 |
| 2024-09-20 22:21:36.659 | MS1 | 121.4656617273 | 31.1446347630 | 553 | 504990 | -85.17 | 17.19 | 100.85 | 0.55 | 2.57 | 536 |
| 2024-09-20 22:21:37.912 | MS1 | 121.4656696877 | 31.1446205389 | 553 | 504990 | -90.80 | 7.14 | 56.60 | 0.56 | 2.44 | 618 |
| 2024-09-20 22:21:38.404 | MS1 | 121.4656736305 | 31.1446376667 | 553 | 504990 | -93.46 | 8.36 | 67.75 | 0.55 | 2.71 | 503 |
| 2024-09-20 22:21:39.561 | MS1 | 121.4656586475 | 31.1446226185 | 553 | 504990 | -91.99 | 9.64 | 61.68 | 0.51 | 2.57 | 518 |
| 2024-09-20 22:21:40.643 | MS1 | 121.4656769737 | 31.1446281458 | 553 | 504990 | -90.37 | 8.73 | 351.78 | 0.09 | 2.10 | 1585 |
| 2024-09-20 22:21:41.727 | MS1 | 121.4656774728 | 31.1446305631 | 553 | 504990 | -91.81 | 8.11 | 330.48 | 0.13 | 2.14 | 1560 |
| 2024-09-20 22:21:42.780 | MS1 | 121.4656650638 | 31.1446286167 | 553 | 504990 | -91.06 | 7.10 | 403.31 | 0.05 | 2.96 | 1572 |

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
| 3246914 | 1 | 121.4733980366 | 31.1517180816 | 176 | 3 | 12 | 28.6 | TDD | 553 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3249712 | 4 | 121.4663084794 | 31.1485410353 | 315 | 2 | 5 | 34.3 | TDD | 238 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3265342 | 2 | 121.4688346403 | 31.1480739575 | 347 | 14 | 5 | 43.7 | TDD | 306 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3277055 | 3 | 121.4674407227 | 31.1558863716 | 9 | 11 | 2 | 36.1 | TDD | 619 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |

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
| 2024-09-20 22:21:31.032 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.051 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.180 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.180 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.913 | NREventA3 | measId:2;ServCellPCI:16;Ser... |
| 2024-09-20 22:21:38.153 | NRHandoverAttempt | SourcePCI:16;SourceNR-ARFCN... |
| 2024-09-20 22:21:38.203 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.217 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.318 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.318 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3246914 | 1 | 5.2605 | 9.6087 | -117.3461 | 9.6958 | 111.2386 | 0.0047 | 0.0019 |
| 2024_09_20 22:00 | 3265342 | 2 | 6.2609 | 12.0509 | -117.5714 | 9.6370 | 86.1778 | 0.0182 | 0.0149 |
| 2024_09_20 22:00 | 3277055 | 3 | 7.3870 | 9.2773 | -117.4369 | 12.9969 | 175.8685 | 0.0108 | 0.0173 |
| 2024_09_20 22:00 | 3249712 | 4 | 13.3953 | 5.7063 | -114.0520 | 6.7313 | 123.7720 | 0.0147 | 0.0093 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413502_75B2D38F | 504990 | 553 | -87.2 | 504990 | 238 | -97.1 | 504990 | 619 | -97.9 | 504990 | 306 |
| MR_1774413502_39E1A0D2 | 504990 | 553 | -89.3 | 504990 | 238 | -94.9 | 504990 | 619 | -97.1 | 504990 | 306 |
| MR_1774413502_DA0C2F48 | 504990 | 553 | -87.5 | 504990 | 238 | -93.5 | 504990 | 619 | -97.1 | 504990 | 306 |
| MR_1774413502_C6609734 | 504990 | 553 | -89.1 | 504990 | 238 | -93.5 | 504990 | 619 | -98.8 | 504990 | 306 |
| MR_1774413502_D084F57A | 504990 | 553 | -88.5 | 504990 | 238 | -93.4 | 504990 | 619 | -97.7 | 504990 | 306 |
| MR_1774413502_28106C34 | 504990 | 553 | -90.0 | 504990 | 238 | -96.2 | 504990 | 619 | -98.4 | 504990 | 306 |
| MR_1774413502_D71E2F14 | 504990 | 553 | -88.5 | 504990 | 238 | -95.9 | 504990 | 619 | -99.8 | 504990 | 306 |
| MR_1774413502_91DA73E9 | 504990 | 553 | -87.0 | 504990 | 238 | -93.4 | 504990 | 619 | -99.4 | 504990 | 306 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 54: `68d174ff-984...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `68d174ff-984b-45f9-8d6d-455c875a31d9` |
| Tag | **single-answer** |
| 정답 | **C19** |
| C19 의미 | Add neighbor relationship between 3245522_3 and 3262887_1 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[54] topology](images/train_0054.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3262887_1
- `C2`: Add neighbor relationship between 3214749_4 and 3262887_1
- `C3`: Decrease A3 Offset threshold for 3245522_3
- `C4`: Insufficient data; more data is needed for judgment.
- `C5`: Increase A3 Offset threshold for 3245522_3
- `C6`: Adjust the azimuth of 3245522_3 by 50 degrees
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3245522_3
- `C8`: Increase transmission power for 3245522_3
- `C9`: Decrease transmission power for 3245522_3
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3262887_1
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3245522_3
- `C12`: Increase transmission power for 3262887_1
- `C13`: Check test server and transmission issues
- `C14`: Lift the tilt angle of 3245522_3 by 7 degrees
- `C15`: Lift the tilt angle  of 3262887_1 by 1 degrees
- `C16`: Decrease transmission power for 3262887_1
- `C17`: Press down the tilt angle of 3245522_3 by 7 degrees
- `C18`: Decrease A3 Offset threshold for 3262887_1
- `C19`: Add neighbor relationship between 3245522_3 and 3262887_1 **← 정답**
- `C20`: Adjust the azimuth of 3262887_1 by 17 degrees
- `C21`: Press down the tilt angle  of 3262887_1 by 1 degrees
- `C22`: Increase A3 Offset threshold for 3262887_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.983 | MS1 | 121.4656587764 | 31.1446361394 | 723 | 504990 | -80.21 | 16.84 | 444.64 | 0.16 | 2.74 | 1563 |
| 2024-09-20 22:21:32.937 | MS1 | 121.4656776477 | 31.1446311046 | 723 | 504990 | -80.01 | 14.49 | 322.04 | 0.17 | 2.23 | 1581 |
| 2024-09-20 22:21:33.917 | MS1 | 121.4656676772 | 31.1446299996 | 723 | 504990 | -75.62 | 16.76 | 430.71 | 0.12 | 2.25 | 1593 |
| 2024-09-20 22:21:34.110 | MS1 | 121.4656673106 | 31.1446298450 | 723 | 504990 | -87.26 | -3.55 | 43.27 | 0.02 | 1.14 | 1589 |
| 2024-09-20 22:21:35.750 | MS1 | 121.4656748424 | 31.1446379280 | 723 | 504990 | -87.32 | -1.27 | 52.81 | 0.07 | 1.45 | 1587 |
| 2024-09-20 22:21:36.389 | MS1 | 121.4656724313 | 31.1446189247 | 723 | 504990 | -93.71 | -2.65 | 42.17 | 0.04 | 1.22 | 1568 |
| 2024-09-20 22:21:37.380 | MS1 | 121.4656608248 | 31.1446299249 | 723 | 504990 | -88.37 | -3.06 | 62.67 | 0.05 | 1.34 | 1568 |
| 2024-09-20 22:21:38.168 | MS1 | 121.4656734397 | 31.1446199032 | 723 | 504990 | -80.86 | 15.98 | 515.79 | 0.14 | 1.03 | 1569 |
| 2024-09-20 22:21:39.230 | MS1 | 121.4656715372 | 31.1446318950 | 723 | 504990 | -78.13 | 17.88 | 490.70 | 0.19 | 1.38 | 1560 |
| 2024-09-20 22:21:40.491 | MS1 | 121.4656768880 | 31.1446263563 | 723 | 504990 | -78.60 | 17.85 | 498.43 | 0.11 | 2.93 | 1596 |
| 2024-09-20 22:21:41.894 | MS1 | 121.4656650185 | 31.1446288300 | 723 | 504990 | -78.14 | 15.14 | 507.83 | 0.14 | 2.49 | 1578 |
| 2024-09-20 22:21:42.122 | MS1 | 121.4656699748 | 31.1446233247 | 723 | 504990 | -79.16 | 15.29 | 463.78 | 0.00 | 2.61 | 1563 |

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
| 3214749 | 4 | 121.4663345250 | 31.1441761389 | 134 | 6 | 7 | 39.8 | TDD | 229 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3245522 | 3 | 121.4757366858 | 31.1490797078 | 141 | 5 | 4 | 34.7 | TDD | 723 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3262887 | 1 | 121.4713582740 | 31.1548576970 | 188 | 0 | 11 | 28.9 | TDD | 761 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3271118 | 2 | 121.4688825670 | 31.1516540723 | 334 | 1 | 4 | 15.5 | TDD | 626 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |

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
| 2024-09-20 22:21:30.837 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.856 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:30.984 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.984 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.680 | NREventA3 | measId:2;ServCellPCI:315;Se... |
| 2024-09-20 22:21:35.680 | NREventA3 | measId:2;ServCellPCI:315;Se... |
| 2024-09-20 22:21:36.680 | NREventA3 | measId:2;ServCellPCI:315;Se... |
| 2024-09-20 22:21:39.180 | NRRRCReestablishAttempt | PCI:315 |
| 2024-09-20 22:21:39.197 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.212 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:39.339 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.339 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3262887 | 1 | 5.3501 | 18.2764 | -114.3205 | 16.1226 | 118.6936 | 0.0164 | 0.0036 |
| 2024_09_20 22:00 | 3271118 | 2 | 18.1239 | 14.0453 | -115.0353 | 8.6427 | 125.2870 | 0.0018 | 0.0141 |
| 2024_09_20 22:00 | 3245522 | 3 | 19.9545 | 19.5619 | -114.8555 | 7.9728 | 185.0438 | 0.0111 | 0.1216 |
| 2024_09_20 22:00 | 3214749 | 4 | 7.2590 | 19.0840 | -115.5179 | 13.0365 | 112.0188 | 0.0085 | 0.0127 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416443_8C27063D | 504990 | 723 | -86.5 | 504990 | 761 | -82.4 | 504990 | 229 | -92.8 | 504990 | 626 |
| MR_1774416443_1CA1E557 | 504990 | 723 | -87.6 | 504990 | 761 | -81.5 | 504990 | 229 | -90.9 | 504990 | 626 |
| MR_1774416443_EF71624B | 504990 | 723 | -86.9 | 504990 | 761 | -83.8 | 504990 | 229 | -91.9 | 504990 | 626 |
| MR_1774416443_534B3E9C | 504990 | 723 | -88.7 | 504990 | 761 | -84.8 | 504990 | 229 | -93.3 | 504990 | 626 |
| MR_1774416443_D6D89C8E | 504990 | 723 | -87.3 | 504990 | 761 | -84.2 | 504990 | 229 | -91.0 | 504990 | 626 |
| MR_1774416443_76E7CA77 | 504990 | 723 | -86.6 | 504990 | 761 | -81.9 | 504990 | 229 | -89.8 | 504990 | 626 |
| MR_1774416443_A363B9C0 | 504990 | 761 | -82.1 | 504990 | 723 | -86.8 | 504990 | 229 | -92.8 | 504990 | 626 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 55: `65fa7046-5a8...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `65fa7046-5a83-40c0-9f14-c8c0bb7c0854` |
| Tag | **single-answer** |
| 정답 | **C6** |
| C6 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[55] topology](images/train_0055.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3254778_1
- `C2`: Lift the tilt angle of 3254778_1 by 10 degrees
- `C3`: Increase transmission power for 3254778_1
- `C4`: Add neighbor relationship between 3254778_1 and 3269757_3
- `C5`: Decrease A3 Offset threshold for 3254778_1
- `C6`: Check test server and transmission issues **← 정답**
- `C7`: Add neighbor relationship between 3233201_4 and 3269757_3
- `C8`: Insufficient data; more data is needed for judgment.
- `C9`: Lift the tilt angle  of 3269757_3 by 4 degrees
- `C10`: Decrease A3 Offset threshold for 3269757_3
- `C11`: Press down the tilt angle  of 3269757_3 by 4 degrees
- `C12`: Increase transmission power for 3269757_3
- `C13`: Decrease transmission power for 3269757_3
- `C14`: Increase A3 Offset threshold for 3254778_1
- `C15`: Adjust the azimuth of 3269757_3 by 50 degrees
- `C16`: Decrease transmission power for 3254778_1
- `C17`: Increase A3 Offset threshold for 3269757_3
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3269757_3
- `C19`: Press down the tilt angle of 3254778_1 by 10 degrees
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3269757_3
- `C21`: Adjust the azimuth of 3254778_1 by 50 degrees
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3254778_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.530 | MS1 | 121.4656771885 | 31.1446231656 | 24 | 504990 | -89.89 | 14.40 | 546.31 | 0.16 | 2.88 | 1572 |
| 2024-09-20 22:21:32.217 | MS1 | 121.4656775233 | 31.1446228858 | 24 | 504990 | -88.42 | 17.27 | 439.90 | 0.09 | 2.97 | 1578 |
| 2024-09-20 22:21:33.130 | MS1 | 121.4656590271 | 31.1446279152 | 24 | 504990 | -89.90 | 13.39 | 387.46 | 0.16 | 2.81 | 1589 |
| 2024-09-20 22:21:34.725 | MS1 | 121.4656614785 | 31.1446339415 | 24 | 504990 | -90.68 | 12.26 | 82.95 | 0.11 | 2.32 | 396 |
| 2024-09-20 22:21:35.456 | MS1 | 121.4656640956 | 31.1446298453 | 24 | 504990 | -88.63 | 13.59 | 56.82 | 0.15 | 2.98 | 318 |
| 2024-09-20 22:21:36.852 | MS1 | 121.4656755075 | 31.1446332076 | 24 | 504990 | -87.25 | 16.14 | 55.83 | 0.10 | 2.28 | 379 |
| 2024-09-20 22:21:37.955 | MS1 | 121.4656602148 | 31.1446314226 | 24 | 504990 | -90.78 | 12.56 | 71.83 | 0.16 | 2.17 | 342 |
| 2024-09-20 22:21:38.139 | MS1 | 121.4656686446 | 31.1446190557 | 24 | 504990 | -90.35 | 12.06 | 94.26 | 0.18 | 2.08 | 328 |
| 2024-09-20 22:21:39.747 | MS1 | 121.4656636015 | 31.1446189068 | 24 | 504990 | -89.71 | 7.02 | 62.79 | 0.10 | 2.37 | 315 |
| 2024-09-20 22:21:40.557 | MS1 | 121.4656588389 | 31.1446261739 | 24 | 504990 | -90.60 | 12.12 | 542.33 | 0.11 | 2.48 | 1562 |
| 2024-09-20 22:21:41.428 | MS1 | 121.4656772525 | 31.1446290301 | 24 | 504990 | -92.98 | 7.10 | 308.52 | 0.14 | 2.14 | 1591 |
| 2024-09-20 22:21:42.242 | MS1 | 121.4656618013 | 31.1446198974 | 24 | 504990 | -92.91 | 8.07 | 515.60 | 0.13 | 2.93 | 1570 |

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
| 3213347 | 2 | 121.4730628918 | 31.1450668902 | 235 | 13 | 5 | 40.8 | TDD | 32 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3233201 | 4 | 121.4720084070 | 31.1525676576 | 72 | 10 | 7 | 15.8 | TDD | 907 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3254778 | 1 | 121.4680140387 | 31.1509107473 | 266 | 6 | 8 | 45.4 | TDD | 24 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3269757 | 3 | 121.4648784963 | 31.1551252417 | 64 | 3 | 11 | 25.9 | TDD | 691 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |

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
| 2024-09-20 22:21:30.829 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.850 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:30.993 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.993 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.714 | NREventA3 | measId:2;ServCellPCI:558;Se... |
| 2024-09-20 22:21:37.954 | NRHandoverAttempt | SourcePCI:558;SourceNR-ARFC... |
| 2024-09-20 22:21:37.991 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.005 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.106 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.106 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3254778 | 1 | 10.1339 | 7.5990 | -115.6671 | 16.3170 | 161.2896 | 0.0169 | 0.0039 |
| 2024_09_20 22:00 | 3213347 | 2 | 13.9710 | 19.2592 | -117.4884 | 7.9297 | 134.9673 | 0.0041 | 0.0110 |
| 2024_09_20 22:00 | 3269757 | 3 | 13.6363 | 7.1322 | -116.8369 | 6.2325 | 199.5212 | 0.0008 | 0.0119 |
| 2024_09_20 22:00 | 3233201 | 4 | 15.3980 | 9.7663 | -116.5709 | 11.7735 | 166.6013 | 0.0038 | 0.0025 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412867_7FDA46A8 | 504990 | 24 | -92.3 | 504990 | 691 | -93.8 | 504990 | 907 | -105.0 | 504990 | 32 |
| MR_1774412867_ADC5749E | 504990 | 24 | -91.3 | 504990 | 691 | -94.5 | 504990 | 907 | -102.8 | 504990 | 32 |
| MR_1774412867_636C3F3C | 504990 | 24 | -91.9 | 504990 | 691 | -97.2 | 504990 | 907 | -104.2 | 504990 | 32 |
| MR_1774412867_34102B66 | 504990 | 24 | -89.3 | 504990 | 691 | -93.6 | 504990 | 907 | -105.6 | 504990 | 32 |
| MR_1774412867_3C29E2F1 | 504990 | 24 | -89.8 | 504990 | 691 | -95.2 | 504990 | 907 | -104.5 | 504990 | 32 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 56: `c708f6a4-cc4...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `c708f6a4-cc4a-49e8-b507-7c8ef377c901` |
| Tag | **single-answer** |
| 정답 | **C6** |
| C6 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3263951_3 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[56] topology](images/train_0056.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3241181_2
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3241181_2
- `C3`: Lift the tilt angle  of 3241181_2 by 8 degrees
- `C4`: Decrease transmission power for 3263951_3
- `C5`: Press down the tilt angle of 3263951_3 by 1 degrees
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3263951_3 **← 정답**
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3241181_2
- `C8`: Increase transmission power for 3241181_2
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3263951_3
- `C10`: Adjust the azimuth of 3241181_2 by 50 degrees
- `C11`: Insufficient data; more data is needed for judgment.
- `C12`: Adjust the azimuth of 3263951_3 by 27 degrees
- `C13`: Add neighbor relationship between 3240200_1 and 3241181_2
- `C14`: Check test server and transmission issues
- `C15`: Increase A3 Offset threshold for 3263951_3
- `C16`: Increase A3 Offset threshold for 3241181_2
- `C17`: Add neighbor relationship between 3263951_3 and 3241181_2
- `C18`: Decrease A3 Offset threshold for 3263951_3
- `C19`: Press down the tilt angle  of 3241181_2 by 8 degrees
- `C20`: Lift the tilt angle of 3263951_3 by 1 degrees
- `C21`: Increase transmission power for 3263951_3
- `C22`: Decrease A3 Offset threshold for 3241181_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.446 | MS1 | 121.4656661149 | 31.1446334447 | 364 | 504990 | -87.84 | 13.43 | 296.76 | 0.01 | 2.88 | 1561 |
| 2024-09-20 22:21:32.773 | MS1 | 121.4656739992 | 31.1446378512 | 364 | 504990 | -90.94 | 15.31 | 524.13 | 0.10 | 2.23 | 1566 |
| 2024-09-20 22:21:33.663 | MS1 | 121.4656622065 | 31.1446229287 | 364 | 504990 | -90.85 | 12.01 | 591.89 | 0.18 | 2.76 | 1600 |
| 2024-09-20 22:21:34.461 | MS1 | 121.4656678197 | 31.1446349968 | 364 | 504990 | -88.70 | 13.11 | 57.10 | 0.62 | 2.14 | 696 |
| 2024-09-20 22:21:35.608 | MS1 | 121.4656617981 | 31.1446276221 | 364 | 504990 | -91.94 | 15.29 | 61.59 | 0.58 | 2.38 | 519 |
| 2024-09-20 22:21:36.975 | MS1 | 121.4656727494 | 31.1446272407 | 364 | 504990 | -88.33 | 12.75 | 66.66 | 0.54 | 2.80 | 556 |
| 2024-09-20 22:21:37.220 | MS1 | 121.4656707644 | 31.1446286617 | 364 | 504990 | -92.89 | 12.15 | 64.85 | 0.66 | 2.71 | 561 |
| 2024-09-20 22:21:38.681 | MS1 | 121.4656765892 | 31.1446348624 | 364 | 504990 | -90.58 | 8.93 | 65.89 | 0.69 | 2.08 | 555 |
| 2024-09-20 22:21:39.365 | MS1 | 121.4656622131 | 31.1446202190 | 364 | 504990 | -90.24 | 11.62 | 78.96 | 0.69 | 2.37 | 577 |
| 2024-09-20 22:21:40.916 | MS1 | 121.4656736115 | 31.1446335768 | 364 | 504990 | -92.76 | 12.55 | 537.42 | 0.11 | 2.56 | 1591 |
| 2024-09-20 22:21:41.135 | MS1 | 121.4656712748 | 31.1446360153 | 364 | 504990 | -91.74 | 11.21 | 393.07 | 0.06 | 2.69 | 1561 |
| 2024-09-20 22:21:42.816 | MS1 | 121.4656754304 | 31.1446181127 | 364 | 504990 | -91.83 | 9.96 | 423.01 | 0.15 | 2.49 | 1595 |

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
| 3240200 | 1 | 121.4699978340 | 31.1496477387 | 206 | 9 | 1 | 39.8 | TDD | 376 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3241181 | 2 | 121.4726855199 | 31.1459461080 | 335 | 6 | 0 | 28.7 | TDD | 947 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3263951 | 3 | 121.4702111050 | 31.1557797384 | 172 | 0 | 9 | 16.4 | TDD | 364 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3279363 | 4 | 121.4697666212 | 31.1472924986 | 136 | 0 | 7 | 26.5 | TDD | 375 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |

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
| 2024-09-20 22:21:30.957 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.982 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.083 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.083 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.821 | NREventA3 | measId:2;ServCellPCI:522;Se... |
| 2024-09-20 22:21:38.061 | NRHandoverAttempt | SourcePCI:522;SourceNR-ARFC... |
| 2024-09-20 22:21:38.097 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.112 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.214 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.214 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3240200 | 1 | 6.9198 | 9.2018 | -117.4339 | 18.9586 | 92.6740 | 0.0114 | 0.0021 |
| 2024_09_20 22:00 | 3241181 | 2 | 15.7840 | 12.9911 | -114.1189 | 11.8467 | 86.0506 | 0.0184 | 0.0049 |
| 2024_09_20 22:00 | 3263951 | 3 | 7.9145 | 18.5714 | -117.0720 | 15.5307 | 114.9964 | 0.0039 | 0.0067 |
| 2024_09_20 22:00 | 3279363 | 4 | 9.9484 | 5.7059 | -114.6540 | 16.6431 | 194.8446 | 0.0199 | 0.0075 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412453_76F7A2DB | 504990 | 364 | -89.7 | 504990 | 947 | -93.5 | 504990 | 376 | -97.1 | 504990 | 375 |
| MR_1774412453_ECAAAACB | 504990 | 364 | -88.8 | 504990 | 947 | -92.3 | 504990 | 376 | -96.5 | 504990 | 375 |
| MR_1774412453_1AD0FEF0 | 504990 | 364 | -89.3 | 504990 | 947 | -94.5 | 504990 | 376 | -96.2 | 504990 | 375 |
| MR_1774412453_10188610 | 504990 | 364 | -89.5 | 504990 | 947 | -95.1 | 504990 | 376 | -98.3 | 504990 | 375 |
| MR_1774412453_175EF467 | 504990 | 364 | -89.3 | 504990 | 947 | -94.8 | 504990 | 376 | -96.8 | 504990 | 375 |
| MR_1774412453_D70DD1D1 | 504990 | 364 | -88.6 | 504990 | 947 | -92.8 | 504990 | 376 | -97.3 | 504990 | 375 |
| MR_1774412453_F33D5D2D | 504990 | 364 | -89.2 | 504990 | 947 | -93.5 | 504990 | 376 | -96.2 | 504990 | 375 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 57: `0e65f7cf-ebd...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `0e65f7cf-ebd4-40c4-a236-b85e265c7485` |
| Tag | **single-answer** |
| 정답 | **C10** |
| C10 의미 | Decrease A3 Offset threshold for 3274460_4 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[57] topology](images/train_0057.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3274460_4 by 10 degrees
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3274460_4
- `C3`: Adjust the azimuth of 3274460_4 by 50 degrees
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3218946_3
- `C5`: Decrease transmission power for 3274460_4
- `C6`: Lift the tilt angle  of 3218946_3 by 3 degrees
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3274460_4
- `C8`: Decrease A3 Offset threshold for 3218946_3
- `C9`: Check test server and transmission issues
- `C10`: Decrease A3 Offset threshold for 3274460_4 **← 정답**
- `C11`: Increase A3 Offset threshold for 3218946_3
- `C12`: Insufficient data; more data is needed for judgment.
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3218946_3
- `C14`: Increase transmission power for 3218946_3
- `C15`: Add neighbor relationship between 3255010_2 and 3218946_3
- `C16`: Press down the tilt angle  of 3218946_3 by 3 degrees
- `C17`: Add neighbor relationship between 3274460_4 and 3218946_3
- `C18`: Increase transmission power for 3274460_4
- `C19`: Lift the tilt angle of 3274460_4 by 10 degrees
- `C20`: Increase A3 Offset threshold for 3274460_4
- `C21`: Adjust the azimuth of 3218946_3 by 50 degrees
- `C22`: Decrease transmission power for 3218946_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.992 | MS1 | 121.4656768707 | 31.1446183319 | 262 | 504990 | -80.10 | 16.70 | 429.35 | 0.17 | 2.50 | 1598 |
| 2024-09-20 22:21:32.751 | MS1 | 121.4656700401 | 31.1446218636 | 262 | 504990 | -80.75 | 14.49 | 567.65 | 0.02 | 2.40 | 1579 |
| 2024-09-20 22:21:33.345 | MS1 | 121.4656739172 | 31.1446200926 | 262 | 504990 | -77.55 | 16.69 | 468.84 | 0.07 | 2.01 | 1577 |
| 2024-09-20 22:21:34.279 | MS1 | 121.4656615080 | 31.1446181272 | 262 | 504990 | -91.56 | -2.52 | 64.62 | 0.07 | 1.21 | 1590 |
| 2024-09-20 22:21:35.407 | MS1 | 121.4656777278 | 31.1446221039 | 262 | 504990 | -85.40 | -0.32 | 49.01 | 0.04 | 1.00 | 1587 |
| 2024-09-20 22:21:36.614 | MS1 | 121.4656701025 | 31.1446282207 | 262 | 504990 | -89.50 | -1.42 | 41.69 | 0.14 | 1.35 | 1587 |
| 2024-09-20 22:21:37.438 | MS1 | 121.4656621548 | 31.1446251569 | 262 | 504990 | -92.49 | -0.04 | 45.20 | 0.06 | 1.39 | 1582 |
| 2024-09-20 22:21:38.687 | MS1 | 121.4656737554 | 31.1446366570 | 262 | 504990 | -83.56 | -1.49 | 36.21 | 0.04 | 1.49 | 1598 |
| 2024-09-20 22:21:39.865 | MS1 | 121.4656688564 | 31.1446347461 | 717 | 504990 | -78.03 | 15.23 | 182.98 | 0.17 | 1.22 | 1593 |
| 2024-09-20 22:21:40.103 | MS1 | 121.4656600541 | 31.1446375339 | 717 | 504990 | -82.07 | 16.88 | 462.57 | 0.08 | 2.51 | 1596 |
| 2024-09-20 22:21:41.102 | MS1 | 121.4656708198 | 31.1446313325 | 717 | 504990 | -81.85 | 12.84 | 428.82 | 0.09 | 2.13 | 1569 |
| 2024-09-20 22:21:42.143 | MS1 | 121.4656651505 | 31.1446286202 | 717 | 504990 | -82.49 | 17.66 | 581.57 | 0.12 | 2.29 | 1575 |

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
| 3218946 | 3 | 121.4670155352 | 31.1543992243 | 92 | 1 | 7 | 38.7 | TDD | 717 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3227312 | 1 | 121.4690891095 | 31.1516707920 | 10 | 2 | 5 | 24.9 | TDD | 472 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3255010 | 2 | 121.4724208534 | 31.1512840490 | 65 | 10 | 4 | 48.8 | TDD | 930 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3274460 | 4 | 121.4716622021 | 31.1465748717 | 2 | 14 | 2 | 16.9 | TDD | 262 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |

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
| 2024-09-20 22:21:31.480 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.503 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.607 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.607 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.298 | NREventA3 | measId:2;ServCellPCI:82;Ser... |
| 2024-09-20 22:21:38.538 | NRHandoverAttempt | SourcePCI:82;SourceNR-ARFCN... |
| 2024-09-20 22:21:38.569 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.580 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.706 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.706 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3227312 | 1 | 19.5828 | 16.0909 | -117.8599 | 6.1646 | 141.7591 | 0.0117 | 0.0059 |
| 2024_09_20 22:00 | 3255010 | 2 | 14.4000 | 5.4949 | -116.3892 | 14.2275 | 142.7322 | 0.0195 | 0.0126 |
| 2024_09_20 22:00 | 3218946 | 3 | 19.8107 | 8.4497 | -117.3987 | 13.0220 | 189.8010 | 0.0082 | 0.0035 |
| 2024_09_20 22:00 | 3274460 | 4 | 13.7679 | 9.1259 | -117.0101 | 12.3859 | 179.1865 | 0.0066 | 0.1788 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413650_396C1222 | 504990 | 717 | -85.0 | 504990 | 262 | -92.1 | 504990 | 930 | -94.4 | 504990 | 472 |
| MR_1774413650_46D5E190 | 504990 | 717 | -84.8 | 504990 | 262 | -90.3 | 504990 | 930 | -90.9 | 504990 | 472 |
| MR_1774413650_CDA60C9B | 504990 | 717 | -85.3 | 504990 | 262 | -90.2 | 504990 | 930 | -94.3 | 504990 | 472 |
| MR_1774413650_F8C1473A | 504990 | 262 | -89.7 | 504990 | 717 | -86.5 | 504990 | 930 | -90.8 | 504990 | 472 |
| MR_1774413650_6D8FD169 | 504990 | 262 | -90.0 | 504990 | 717 | -85.6 | 504990 | 930 | -93.8 | 504990 | 472 |
| MR_1774413650_5E69FC81 | 504990 | 262 | -91.9 | 504990 | 717 | -87.7 | 504990 | 930 | -93.8 | 504990 | 472 |
| MR_1774413650_973DE026 | 504990 | 717 | -86.9 | 504990 | 262 | -92.8 | 504990 | 930 | -91.6 | 504990 | 472 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 58: `116a8416-594...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `116a8416-5940-43ec-9619-8c033a13a68b` |
| Tag | **single-answer** |
| 정답 | **C3** |
| C3 의미 | Add neighbor relationship between 3231162_1 and 3235153_3 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[58] topology](images/train_0058.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3235153_3 by 16 degrees
- `C2`: Insufficient data; more data is needed for judgment.
- `C3`: Add neighbor relationship between 3231162_1 and 3235153_3 **← 정답**
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3235153_3
- `C5`: Lift the tilt angle of 3231162_1 by 10 degrees
- `C6`: Check test server and transmission issues
- `C7`: Lift the tilt angle  of 3235153_3 by 5 degrees
- `C8`: Decrease A3 Offset threshold for 3235153_3
- `C9`: Increase A3 Offset threshold for 3235153_3
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3235153_3
- `C11`: Increase transmission power for 3235153_3
- `C12`: Add neighbor relationship between 3273143_2 and 3235153_3
- `C13`: Decrease transmission power for 3235153_3
- `C14`: Press down the tilt angle  of 3235153_3 by 5 degrees
- `C15`: Decrease A3 Offset threshold for 3231162_1
- `C16`: Increase transmission power for 3231162_1
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3231162_1
- `C18`: Increase A3 Offset threshold for 3231162_1
- `C19`: Adjust the azimuth of 3231162_1 by 50 degrees
- `C20`: Press down the tilt angle of 3231162_1 by 10 degrees
- `C21`: Decrease transmission power for 3231162_1
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3231162_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.260 | MS1 | 121.4656609002 | 31.1446365103 | 896 | 504990 | -81.32 | 14.36 | 567.72 | 0.05 | 2.20 | 1574 |
| 2024-09-20 22:21:32.809 | MS1 | 121.4656593801 | 31.1446341666 | 896 | 504990 | -75.74 | 12.36 | 358.24 | 0.08 | 2.40 | 1600 |
| 2024-09-20 22:21:33.113 | MS1 | 121.4656656103 | 31.1446211279 | 896 | 504990 | -82.73 | 15.02 | 475.22 | 0.06 | 2.20 | 1571 |
| 2024-09-20 22:21:34.879 | MS1 | 121.4656630493 | 31.1446211157 | 896 | 504990 | -89.68 | -1.92 | 26.66 | 0.13 | 1.42 | 1584 |
| 2024-09-20 22:21:35.505 | MS1 | 121.4656702311 | 31.1446296278 | 896 | 504990 | -92.01 | -0.27 | 68.19 | 0.03 | 1.29 | 1585 |
| 2024-09-20 22:21:36.613 | MS1 | 121.4656692518 | 31.1446238195 | 896 | 504990 | -85.02 | -1.63 | 59.85 | 0.04 | 1.18 | 1571 |
| 2024-09-20 22:21:37.246 | MS1 | 121.4656621384 | 31.1446323483 | 896 | 504990 | -87.90 | -3.06 | 38.01 | 0.10 | 1.02 | 1588 |
| 2024-09-20 22:21:38.477 | MS1 | 121.4656766909 | 31.1446218670 | 896 | 504990 | -77.81 | 15.95 | 446.34 | 0.06 | 1.50 | 1567 |
| 2024-09-20 22:21:39.762 | MS1 | 121.4656614388 | 31.1446312862 | 896 | 504990 | -80.45 | 12.29 | 433.32 | 0.01 | 1.20 | 1578 |
| 2024-09-20 22:21:40.266 | MS1 | 121.4656708714 | 31.1446322471 | 896 | 504990 | -83.23 | 13.01 | 406.13 | 0.14 | 2.45 | 1599 |
| 2024-09-20 22:21:41.193 | MS1 | 121.4656666089 | 31.1446256058 | 896 | 504990 | -84.66 | 16.88 | 366.90 | 0.11 | 2.34 | 1569 |
| 2024-09-20 22:21:42.392 | MS1 | 121.4656685868 | 31.1446199412 | 896 | 504990 | -82.19 | 15.20 | 475.50 | 0.08 | 2.19 | 1561 |

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
| 3231162 | 1 | 121.4667855556 | 31.1440205101 | 166 | 4 | 7 | 45.2 | TDD | 896 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3233067 | 4 | 121.4682165178 | 31.1535225600 | 180 | 12 | 6 | 45.7 | TDD | 646 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3235153 | 3 | 121.4753758691 | 31.1502311197 | 220 | 4 | 4 | 22.6 | TDD | 491 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3273143 | 2 | 121.4708393132 | 31.1462607085 | 250 | 2 | 8 | 36.8 | TDD | 598 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |

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
| 2024-09-20 22:21:30.929 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.952 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.063 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.063 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.817 | NREventA3 | measId:2;ServCellPCI:656;Se... |
| 2024-09-20 22:21:35.817 | NREventA3 | measId:2;ServCellPCI:656;Se... |
| 2024-09-20 22:21:36.817 | NREventA3 | measId:2;ServCellPCI:656;Se... |
| 2024-09-20 22:21:39.317 | NRRRCReestablishAttempt | PCI:656 |
| 2024-09-20 22:21:39.332 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.342 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:39.485 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.485 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3231162 | 1 | 10.6885 | 6.6700 | -115.5183 | 14.8976 | 129.2348 | 0.0073 | 0.1061 |
| 2024_09_20 22:00 | 3273143 | 2 | 14.8462 | 12.9798 | -116.6926 | 5.2683 | 88.2623 | 0.0184 | 0.0039 |
| 2024_09_20 22:00 | 3235153 | 3 | 9.9100 | 10.7103 | -114.4967 | 8.3877 | 102.9303 | 0.0060 | 0.0034 |
| 2024_09_20 22:00 | 3233067 | 4 | 12.5637 | 13.2330 | -117.1556 | 15.0157 | 126.1622 | 0.0069 | 0.0112 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417042_6FD81A36 | 504990 | 896 | -90.3 | 504990 | 491 | -83.5 | 504990 | 598 | -89.7 | 504990 | 646 |
| MR_1774417042_A8DF9903 | 504990 | 896 | -89.2 | 504990 | 491 | -85.4 | 504990 | 598 | -89.2 | 504990 | 646 |
| MR_1774417042_58B1E4C5 | 504990 | 896 | -87.9 | 504990 | 491 | -85.4 | 504990 | 598 | -89.5 | 504990 | 646 |
| MR_1774417042_2B940173 | 504990 | 896 | -90.8 | 504990 | 491 | -83.8 | 504990 | 598 | -91.4 | 504990 | 646 |
| MR_1774417042_48241DE2 | 504990 | 896 | -90.2 | 504990 | 491 | -85.8 | 504990 | 598 | -89.7 | 504990 | 646 |
| MR_1774417042_F627371A | 504990 | 491 | -83.0 | 504990 | 896 | -88.5 | 504990 | 598 | -92.4 | 504990 | 646 |
| MR_1774417042_9042399B | 504990 | 896 | -89.5 | 504990 | 491 | -85.3 | 504990 | 598 | -91.9 | 504990 | 646 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 59: `a44aaa5b-c78...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `a44aaa5b-c781-4f32-a7cf-ca8ace1d9710` |
| Tag | **single-answer** |
| 정답 | **C7** |
| C7 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[59] topology](images/train_0059.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3262480_2 by 7 degrees
- `C2`: Lift the tilt angle of 3236468_3 by 10 degrees
- `C3`: Decrease transmission power for 3236468_3
- `C4`: Decrease A3 Offset threshold for 3236468_3
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3262480_2
- `C6`: Add neighbor relationship between 3236468_3 and 3262480_2
- `C7`: Insufficient data; more data is needed for judgment. **← 정답**
- `C8`: Increase A3 Offset threshold for 3236468_3
- `C9`: Decrease transmission power for 3262480_2
- `C10`: Increase transmission power for 3236468_3
- `C11`: Increase A3 Offset threshold for 3262480_2
- `C12`: Increase transmission power for 3262480_2
- `C13`: Decrease A3 Offset threshold for 3262480_2
- `C14`: Check test server and transmission issues
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3236468_3
- `C16`: Adjust the azimuth of 3262480_2 by 50 degrees
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3236468_3
- `C18`: Press down the tilt angle of 3236468_3 by 10 degrees
- `C19`: Lift the tilt angle  of 3262480_2 by 7 degrees
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3262480_2
- `C21`: Add neighbor relationship between 3247269_1 and 3262480_2
- `C22`: Adjust the azimuth of 3236468_3 by 48 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.538 | MS1 | 121.4656684852 | 31.1446344838 | 244 | 504990 | -86.55 | 15.67 | 546.06 | 0.10 | 2.97 | 1589 |
| 2024-09-20 22:21:32.550 | MS1 | 121.4656594417 | 31.1446308349 | 244 | 504990 | -89.31 | 17.19 | 455.50 | 0.14 | 2.84 | 1587 |
| 2024-09-20 22:21:33.466 | MS1 | 121.4656696488 | 31.1446314555 | 244 | 504990 | -89.61 | 15.35 | 507.96 | 0.04 | 2.51 | 1576 |
| 2024-09-20 22:21:34.514 | MS1 | 121.4656630540 | 31.1446192737 | 244 | 504990 | -85.97 | 17.50 | 68.56 | 0.03 | 2.67 | 1574 |
| 2024-09-20 22:21:35.176 | MS1 | 121.4656628592 | 31.1446215809 | 244 | 504990 | -90.78 | 13.18 | 72.41 | 0.14 | 2.52 | 1575 |
| 2024-09-20 22:21:36.164 | MS1 | 121.4656703299 | 31.1446282568 | 244 | 504990 | -86.03 | 12.49 | 105.66 | 0.12 | 2.00 | 1574 |
| 2024-09-20 22:21:37.868 | MS1 | 121.4656594493 | 31.1446357418 | 244 | 504990 | -89.52 | 7.00 | 67.32 | 0.06 | 2.88 | 1577 |
| 2024-09-20 22:21:38.632 | MS1 | 121.4656607821 | 31.1446276770 | 244 | 504990 | -89.70 | 12.00 | 97.94 | 0.02 | 2.27 | 1573 |
| 2024-09-20 22:21:39.752 | MS1 | 121.4656656138 | 31.1446197331 | 244 | 504990 | -93.96 | 8.35 | 64.24 | 0.04 | 2.41 | 1578 |
| 2024-09-20 22:21:40.734 | MS1 | 121.4656615514 | 31.1446232345 | 244 | 504990 | -93.72 | 11.61 | 303.55 | 0.05 | 2.00 | 1576 |
| 2024-09-20 22:21:41.693 | MS1 | 121.4656629262 | 31.1446337569 | 244 | 504990 | -92.31 | 8.36 | 485.67 | 0.14 | 2.75 | 1585 |
| 2024-09-20 22:21:42.298 | MS1 | 121.4656778967 | 31.1446234183 | 244 | 504990 | -90.33 | 7.47 | 366.17 | 0.01 | 2.51 | 1565 |

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
| 3214083 | 4 | 121.4643299075 | 31.1547308107 | 297 | 11 | 12 | 45.7 | TDD | 556 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3236468 | 3 | 121.4694103516 | 31.1492121597 | 263 | 12 | 3 | 44.4 | TDD | 244 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3247269 | 1 | 121.4675439859 | 31.1452171345 | 220 | 7 | 2 | 24.5 | TDD | 609 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3262480 | 2 | 121.4743473196 | 31.1536019118 | 6 | 6 | 9 | 18.2 | TDD | 491 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |

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
| 2024-09-20 22:21:30.934 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.955 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.092 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.092 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.793 | NREventA3 | measId:2;ServCellPCI:953;Se... |
| 2024-09-20 22:21:38.033 | NRHandoverAttempt | SourcePCI:953;SourceNR-ARFC... |
| 2024-09-20 22:21:38.076 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.089 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.227 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.227 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3247269 | 1 | 85.3368 | 89.7614 | -116.5710 | 14.7100 | 154.1650 | 0.0111 | 0.0151 |
| 2024_09_19 22:00 | 3262480 | 2 | 93.4855 | 78.9339 | -114.2965 | 9.2225 | 133.4220 | 0.0057 | 0.0198 |
| 2024_09_19 22:00 | 3236468 | 3 | 88.8406 | 89.6023 | -114.8186 | 10.8110 | 126.1761 | 0.0144 | 0.0023 |
| 2024_09_19 22:00 | 3214083 | 4 | 90.3169 | 85.2306 | -116.2278 | 19.1800 | 144.6096 | 0.0036 | 0.0141 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415145_9C86A2A3 | 504990 | 244 | -85.3 | 504990 | 491 | -86.6 | 504990 | 609 | -94.6 | 504990 | 556 |
| MR_1774415145_9AEF7FF2 | 504990 | 244 | -87.3 | 504990 | 491 | -85.8 | 504990 | 609 | -97.2 | 504990 | 556 |
| MR_1774415145_726717EA | 504990 | 244 | -86.6 | 504990 | 491 | -87.1 | 504990 | 609 | -96.9 | 504990 | 556 |
| MR_1774415145_66A17EF4 | 504990 | 244 | -87.9 | 504990 | 491 | -85.6 | 504990 | 609 | -96.5 | 504990 | 556 |
| MR_1774415145_EDFA2EE3 | 504990 | 244 | -86.5 | 504990 | 491 | -84.7 | 504990 | 609 | -95.3 | 504990 | 556 |

> *... 2개 열 생략 (전체 14열)*

---
