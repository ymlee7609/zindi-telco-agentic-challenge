# Track A 문제 분석 — train[1190]~train[1199]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[1190] ~ train[1199] (10개)

## 목차

1. [문제 1190: `87b7fda2-400...`](#1190) — single-answer, 정답: C21
2. [문제 1191: `698ea370-c31...`](#1191) — multiple-answer, 정답: C1|C13
3. [문제 1192: `ac6b5f2c-264...`](#1192) — single-answer, 정답: C13
4. [문제 1193: `d0577b88-a7c...`](#1193) — single-answer, 정답: C2
5. [문제 1194: `3d8c80cc-7e6...`](#1194) — single-answer, 정답: C14
6. [문제 1195: `e919cd95-d25...`](#1195) — single-answer, 정답: C8
7. [문제 1196: `51d60cb4-669...`](#1196) — single-answer, 정답: C17
8. [문제 1197: `dc29a039-d5a...`](#1197) — single-answer, 정답: C18
9. [문제 1198: `7fda8777-c3c...`](#1198) — single-answer, 정답: C20
10. [문제 1199: `e18f5c91-f97...`](#1199) — single-answer, 정답: C1

---

### 문제 1190: `87b7fda2-400...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `87b7fda2-400e-4d7e-8fcc-444eb60a927f` |
| Tag | **single-answer** |
| 정답 | **C21** |
| C21 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1190] topology](images/train_1190.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3216146_1
- `C2`: Add neighbor relationship between 3216146_1 and 3261293_3
- `C3`: Adjust the azimuth of 3216146_1 by 27 degrees
- `C4`: Decrease transmission power for 3261293_3
- `C5`: Adjust the azimuth of 3261293_3 by 50 degrees
- `C6`: Increase transmission power for 3216146_1
- `C7`: Decrease A3 Offset threshold for 3261293_3
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3261293_3
- `C9`: Increase A3 Offset threshold for 3261293_3
- `C10`: Press down the tilt angle of 3216146_1 by 6 degrees
- `C11`: Increase A3 Offset threshold for 3216146_1
- `C12`: Increase transmission power for 3261293_3
- `C13`: Check test server and transmission issues
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3261293_3
- `C15`: Lift the tilt angle  of 3261293_3 by 10 degrees
- `C16`: Decrease A3 Offset threshold for 3216146_1
- `C17`: Press down the tilt angle  of 3261293_3 by 10 degrees
- `C18`: Decrease transmission power for 3216146_1
- `C19`: Lift the tilt angle of 3216146_1 by 6 degrees
- `C20`: Add neighbor relationship between 3273872_2 and 3261293_3
- `C21`: Insufficient data; more data is needed for judgment. **← 정답**
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3216146_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.329 | MS1 | 121.4656776866 | 31.1446333427 | 410 | 504990 | -88.41 | 12.23 | 531.09 | 0.08 | 2.27 | 1565 |
| 2024-09-20 22:21:32.773 | MS1 | 121.4656730509 | 31.1446188447 | 410 | 504990 | -87.91 | 16.48 | 348.97 | 0.05 | 2.40 | 1586 |
| 2024-09-20 22:21:33.596 | MS1 | 121.4656676479 | 31.1446192230 | 410 | 504990 | -88.23 | 15.42 | 427.58 | 0.11 | 2.47 | 1588 |
| 2024-09-20 22:21:34.735 | MS1 | 121.4656604607 | 31.1446212671 | 410 | 504990 | -91.59 | 15.64 | 60.45 | 0.07 | 2.24 | 1561 |
| 2024-09-20 22:21:35.606 | MS1 | 121.4656636763 | 31.1446206087 | 410 | 504990 | -88.79 | 13.96 | 58.64 | 0.12 | 2.73 | 1590 |
| 2024-09-20 22:21:36.431 | MS1 | 121.4656723217 | 31.1446222555 | 410 | 504990 | -88.97 | 16.49 | 74.59 | 0.12 | 2.97 | 1586 |
| 2024-09-20 22:21:37.531 | MS1 | 121.4656684731 | 31.1446317320 | 410 | 504990 | -89.05 | 10.48 | 81.67 | 0.18 | 2.44 | 1591 |
| 2024-09-20 22:21:38.923 | MS1 | 121.4656710653 | 31.1446322284 | 410 | 504990 | -91.45 | 10.69 | 95.36 | 0.20 | 2.51 | 1589 |
| 2024-09-20 22:21:39.531 | MS1 | 121.4656725652 | 31.1446376553 | 410 | 504990 | -92.78 | 10.17 | 87.46 | 0.17 | 2.56 | 1591 |
| 2024-09-20 22:21:40.847 | MS1 | 121.4656703226 | 31.1446281104 | 410 | 504990 | -91.76 | 12.99 | 487.05 | 0.06 | 2.06 | 1587 |
| 2024-09-20 22:21:41.729 | MS1 | 121.4656753633 | 31.1446235813 | 410 | 504990 | -90.34 | 10.18 | 520.56 | 0.01 | 2.23 | 1586 |
| 2024-09-20 22:21:42.418 | MS1 | 121.4656625044 | 31.1446233049 | 410 | 504990 | -90.32 | 7.55 | 347.91 | 0.15 | 2.41 | 1585 |

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
| 3214014 | 4 | 121.4664903345 | 31.1473677024 | 355 | 0 | 1 | 23.1 | TDD | 606 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3216146 | 1 | 121.4665030538 | 31.1549601960 | 157 | 5 | 2 | 23.2 | TDD | 410 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3261293 | 3 | 121.4662627871 | 31.1442537945 | 241 | 13 | 0 | 28.4 | TDD | 949 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3273872 | 2 | 121.4696312791 | 31.1532778619 | 167 | 9 | 5 | 16.1 | TDD | 298 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

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
| 2024-09-20 22:21:31.064 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.086 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.223 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.223 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.949 | NREventA3 | measId:2;ServCellPCI:931;Se... |
| 2024-09-20 22:21:38.189 | NRHandoverAttempt | SourcePCI:931;SourceNR-ARFC... |
| 2024-09-20 22:21:38.232 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.244 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.368 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.368 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3216146 | 1 | 83.8714 | 94.3068 | -117.1639 | 11.8668 | 80.0445 | 0.0106 | 0.0031 |
| 2024_09_19 22:00 | 3273872 | 2 | 77.8353 | 90.0243 | -116.4378 | 5.1537 | 137.2487 | 0.0122 | 0.0134 |
| 2024_09_19 22:00 | 3261293 | 3 | 79.7803 | 83.5930 | -117.6479 | 17.0749 | 186.0416 | 0.0099 | 0.0014 |
| 2024_09_19 22:00 | 3214014 | 4 | 87.2843 | 92.3917 | -115.7921 | 6.5096 | 103.6958 | 0.0197 | 0.0083 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415263_7BD051DD | 504990 | 410 | -92.0 | 504990 | 949 | -95.2 | 504990 | 298 | -102.7 | 504990 | 606 |
| MR_1774415263_9F496259 | 504990 | 410 | -91.3 | 504990 | 949 | -96.4 | 504990 | 298 | -106.1 | 504990 | 606 |
| MR_1774415263_3BD83BAC | 504990 | 410 | -90.2 | 504990 | 949 | -97.8 | 504990 | 298 | -103.1 | 504990 | 606 |
| MR_1774415263_B3E06BAF | 504990 | 410 | -91.2 | 504990 | 949 | -94.4 | 504990 | 298 | -105.8 | 504990 | 606 |
| MR_1774415263_75037C94 | 504990 | 410 | -91.9 | 504990 | 949 | -96.2 | 504990 | 298 | -104.7 | 504990 | 606 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1191: `698ea370-c31...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `698ea370-c312-491b-b213-aa1453698259` |
| Tag | **multiple-answer** |
| 정답 | **C1|C13** |
| C1 의미 | Increase transmission power for 3264188_1 |
| C13 의미 | Adjust the azimuth of 3264188_1 by 23 degrees |
| 패턴 분류 | **P4 Coverage (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1191] topology](images/train_1191.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3264188_1 **← 정답**
- `C2`: Decrease transmission power for 3254057_3
- `C3`: Add neighbor relationship between 3262541_4 and 3254057_3
- `C4`: Decrease A3 Offset threshold for 3254057_3
- `C5`: Adjust the azimuth of 3254057_3 by 23 degrees
- `C6`: Increase transmission power for 3254057_3
- `C7`: Press down the tilt angle  of 3254057_3 by 5 degrees
- `C8`: Decrease transmission power for 3264188_1
- `C9`: Press down the tilt angle of 3264188_1 by 10 degrees
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3254057_3
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3264188_1
- `C12`: Increase A3 Offset threshold for 3264188_1
- `C13`: Adjust the azimuth of 3264188_1 by 23 degrees **← 정답**
- `C14`: Add neighbor relationship between 3264188_1 and 3254057_3
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3254057_3
- `C16`: Lift the tilt angle of 3264188_1 by 10 degrees
- `C17`: Check test server and transmission issues
- `C18`: Decrease A3 Offset threshold for 3264188_1
- `C19`: Insufficient data; more data is needed for judgment.
- `C20`: Lift the tilt angle  of 3254057_3 by 5 degrees
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3264188_1
- `C22`: Increase A3 Offset threshold for 3254057_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.856 | MS1 | 121.4656654117 | 31.1446186197 | 874 | 504990 | -87.17 | 17.15 | 458.32 | 0.10 | 2.07 | 1589 |
| 2024-09-20 22:21:32.183 | MS1 | 121.4656682973 | 31.1446375386 | 874 | 504990 | -92.81 | 14.34 | 509.54 | 0.02 | 2.82 | 1561 |
| 2024-09-20 22:21:33.553 | MS1 | 121.4656683188 | 31.1446222485 | 874 | 504990 | -91.20 | 17.63 | 441.36 | 0.09 | 2.34 | 1578 |
| 2024-09-20 22:21:34.469 | MS1 | 121.4656645810 | 31.1446224177 | 874 | 504990 | -101.80 | -0.66 | 38.94 | 0.06 | 1.19 | 1565 |
| 2024-09-20 22:21:35.593 | MS1 | 121.4656634664 | 31.1446284533 | 874 | 504990 | -105.42 | 1.96 | 15.75 | 0.13 | 1.16 | 1599 |
| 2024-09-20 22:21:36.835 | MS1 | 121.4656614812 | 31.1446247528 | 874 | 504990 | -103.12 | -0.58 | 51.04 | 0.13 | 1.19 | 1572 |
| 2024-09-20 22:21:37.229 | MS1 | 121.4656640283 | 31.1446228608 | 874 | 504990 | -106.29 | 1.70 | 20.89 | 0.09 | 1.12 | 1585 |
| 2024-09-20 22:21:38.974 | MS1 | 121.4656659504 | 31.1446306276 | 874 | 504990 | -107.01 | -0.96 | 46.33 | 0.16 | 1.29 | 1563 |
| 2024-09-20 22:21:39.901 | MS1 | 121.4656637378 | 31.1446336958 | 874 | 504990 | -100.56 | -1.92 | 42.78 | 0.09 | 1.28 | 1583 |
| 2024-09-20 22:21:40.409 | MS1 | 121.4656583408 | 31.1446210203 | 874 | 504990 | -87.84 | 15.59 | 337.86 | 0.19 | 2.50 | 1572 |
| 2024-09-20 22:21:41.657 | MS1 | 121.4656689023 | 31.1446296712 | 874 | 504990 | -92.04 | 13.96 | 585.95 | 0.05 | 2.08 | 1589 |
| 2024-09-20 22:21:42.545 | MS1 | 121.4656646058 | 31.1446344432 | 874 | 504990 | -85.57 | 16.12 | 392.21 | 0.18 | 2.19 | 1564 |

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
| 3254057 | 3 | 121.4723282776 | 31.1451637787 | 288 | 3 | 9 | 22.0 | TDD | 211 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3262541 | 4 | 121.4756227584 | 31.1487191663 | 126 | 8 | 6 | 47.6 | TDD | 483 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3264188 | 1 | 121.4642916189 | 31.1455830152 | 152 | 8 | 4 | 19.0 | TDD | 874 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3275386 | 2 | 121.4714431741 | 31.1450567599 | 121 | 12 | 3 | 24.1 | TDD | 627 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:31.226 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.226 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.430 | NREventA2 | measId:1;ServCellPCI:906;Se... |
| 2024-09-20 22:21:34.560 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3264188 | 1 | 9.0118 | 16.1183 | -117.6085 | 12.6547 | 86.1811 | 0.1284 | 0.0145 |
| 2024_09_20 22:00 | 3275386 | 2 | 8.4091 | 18.8263 | -115.3143 | 9.9602 | 81.4022 | 0.0037 | 0.0190 |
| 2024_09_20 22:00 | 3254057 | 3 | 14.9652 | 16.1104 | -117.4827 | 5.6050 | 111.9469 | 0.0014 | 0.0104 |
| 2024_09_20 22:00 | 3262541 | 4 | 9.8728 | 13.3569 | -114.1833 | 5.7149 | 189.7694 | 0.0129 | 0.0146 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413479_DCC25043 | 504990 | 874 | -102.9 | 504990 | 211 | -107.0 | 504990 | 483 | -112.8 | 504990 | 627 |
| MR_1774413479_7ED24350 | 504990 | 874 | -103.3 | 504990 | 211 | -105.1 | 504990 | 483 | -110.2 | 504990 | 627 |
| MR_1774413479_42959804 | 504990 | 874 | -100.0 | 504990 | 211 | -107.5 | 504990 | 483 | -109.4 | 504990 | 627 |
| MR_1774413479_7D708FA4 | 504990 | 874 | -100.8 | 504990 | 211 | -107.8 | 504990 | 483 | -109.5 | 504990 | 627 |
| MR_1774413479_EC6B912D | 504990 | 874 | -100.2 | 504990 | 211 | -106.9 | 504990 | 483 | -111.2 | 504990 | 627 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1192: `ac6b5f2c-264...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `ac6b5f2c-264f-4c8d-9c6c-682ad0b74d87` |
| Tag | **single-answer** |
| 정답 | **C13** |
| C13 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1192] topology](images/train_1192.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3222758_1
- `C2`: Press down the tilt angle of 3222758_1 by 10 degrees
- `C3`: Insufficient data; more data is needed for judgment.
- `C4`: Decrease A3 Offset threshold for 3231804_3
- `C5`: Press down the tilt angle  of 3231804_3 by 10 degrees
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3231804_3
- `C7`: Lift the tilt angle  of 3231804_3 by 10 degrees
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3231804_3
- `C9`: Increase transmission power for 3222758_1
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3222758_1
- `C11`: Decrease A3 Offset threshold for 3222758_1
- `C12`: Increase A3 Offset threshold for 3222758_1
- `C13`: Check test server and transmission issues **← 정답**
- `C14`: Increase A3 Offset threshold for 3231804_3
- `C15`: Decrease transmission power for 3231804_3
- `C16`: Lift the tilt angle of 3222758_1 by 10 degrees
- `C17`: Adjust the azimuth of 3231804_3 by 50 degrees
- `C18`: Adjust the azimuth of 3222758_1 by 50 degrees
- `C19`: Add neighbor relationship between 3222758_1 and 3231804_3
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3222758_1
- `C21`: Increase transmission power for 3231804_3
- `C22`: Add neighbor relationship between 3263414_4 and 3231804_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.287 | MS1 | 121.4656770628 | 31.1446246394 | 418 | 504990 | -85.51 | 13.47 | 526.35 | 0.08 | 2.18 | 1600 |
| 2024-09-20 22:21:32.156 | MS1 | 121.4656750022 | 31.1446193164 | 418 | 504990 | -90.85 | 17.13 | 376.62 | 0.10 | 2.21 | 1573 |
| 2024-09-20 22:21:33.636 | MS1 | 121.4656628957 | 31.1446357981 | 418 | 504990 | -90.31 | 15.98 | 383.50 | 0.10 | 2.16 | 1575 |
| 2024-09-20 22:21:34.915 | MS1 | 121.4656734532 | 31.1446337523 | 418 | 504990 | -87.79 | 14.26 | 74.87 | 0.09 | 2.81 | 353 |
| 2024-09-20 22:21:35.225 | MS1 | 121.4656687177 | 31.1446236734 | 418 | 504990 | -90.81 | 17.18 | 92.67 | 0.04 | 2.00 | 452 |
| 2024-09-20 22:21:36.625 | MS1 | 121.4656692157 | 31.1446379006 | 418 | 504990 | -91.85 | 17.45 | 62.42 | 0.01 | 2.36 | 345 |
| 2024-09-20 22:21:37.770 | MS1 | 121.4656661480 | 31.1446258013 | 418 | 504990 | -90.46 | 8.92 | 60.54 | 0.15 | 2.73 | 393 |
| 2024-09-20 22:21:38.976 | MS1 | 121.4656606639 | 31.1446207957 | 418 | 504990 | -91.71 | 9.48 | 61.30 | 0.04 | 2.15 | 386 |
| 2024-09-20 22:21:39.428 | MS1 | 121.4656778504 | 31.1446324227 | 418 | 504990 | -93.24 | 10.77 | 100.02 | 0.13 | 2.85 | 383 |
| 2024-09-20 22:21:40.297 | MS1 | 121.4656633400 | 31.1446366828 | 418 | 504990 | -89.13 | 7.41 | 357.57 | 0.19 | 2.08 | 1599 |
| 2024-09-20 22:21:41.369 | MS1 | 121.4656756962 | 31.1446207595 | 418 | 504990 | -89.13 | 10.75 | 437.45 | 0.14 | 2.13 | 1561 |
| 2024-09-20 22:21:42.684 | MS1 | 121.4656678850 | 31.1446284644 | 418 | 504990 | -91.61 | 11.11 | 523.86 | 0.11 | 2.60 | 1570 |

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
| 3215302 | 2 | 121.4675275745 | 31.1530724624 | 61 | 11 | 9 | 45.3 | TDD | 10 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3222758 | 1 | 121.4679167625 | 31.1443756619 | 333 | 15 | 0 | 21.2 | TDD | 418 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3231804 | 3 | 121.4664014671 | 31.1536843424 | 254 | 9 | 4 | 49.8 | TDD | 573 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3263414 | 4 | 121.4653696546 | 31.1525850588 | 144 | 11 | 1 | 25.6 | TDD | 898 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |

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
| 2024-09-20 22:21:30.860 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.881 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:30.997 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.997 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.704 | NREventA3 | measId:2;ServCellPCI:504;Se... |
| 2024-09-20 22:21:37.944 | NRHandoverAttempt | SourcePCI:504;SourceNR-ARFC... |
| 2024-09-20 22:21:37.984 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.998 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.103 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.103 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3222758 | 1 | 17.3557 | 13.0867 | -115.1552 | 19.5716 | 104.1566 | 0.0161 | 0.0128 |
| 2024_09_20 22:00 | 3215302 | 2 | 12.5999 | 16.9406 | -117.7413 | 19.9537 | 116.7487 | 0.0033 | 0.0037 |
| 2024_09_20 22:00 | 3231804 | 3 | 18.0061 | 12.6409 | -115.1549 | 9.0635 | 150.3854 | 0.0074 | 0.0021 |
| 2024_09_20 22:00 | 3263414 | 4 | 19.7612 | 17.0437 | -116.2754 | 19.2247 | 182.8326 | 0.0004 | 0.0124 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416225_4A1792EA | 504990 | 418 | -86.5 | 504990 | 573 | -88.3 | 504990 | 898 | -99.5 | 504990 | 10 |
| MR_1774416225_F82D6F47 | 504990 | 418 | -88.3 | 504990 | 573 | -87.4 | 504990 | 898 | -99.7 | 504990 | 10 |
| MR_1774416225_BE39E5B8 | 504990 | 418 | -86.3 | 504990 | 573 | -88.5 | 504990 | 898 | -99.6 | 504990 | 10 |
| MR_1774416225_53BBA451 | 504990 | 418 | -88.8 | 504990 | 573 | -88.9 | 504990 | 898 | -98.1 | 504990 | 10 |
| MR_1774416225_7579881D | 504990 | 418 | -88.5 | 504990 | 573 | -88.9 | 504990 | 898 | -96.8 | 504990 | 10 |
| MR_1774416225_D0123648 | 504990 | 418 | -89.1 | 504990 | 573 | -89.0 | 504990 | 898 | -97.6 | 504990 | 10 |
| MR_1774416225_696E3FF0 | 504990 | 418 | -88.8 | 504990 | 573 | -87.6 | 504990 | 898 | -97.5 | 504990 | 10 |
| MR_1774416225_19926681 | 504990 | 418 | -85.8 | 504990 | 573 | -85.8 | 504990 | 898 | -98.3 | 504990 | 10 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1193: `d0577b88-a7c...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `d0577b88-a7cf-4b27-b588-3ddce513058b` |
| Tag | **single-answer** |
| 정답 | **C2** |
| C2 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3266772_1 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1193] topology](images/train_1193.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle  of 3227833_2 by 1 degrees
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3266772_1 **← 정답**
- `C3`: Decrease transmission power for 3266772_1
- `C4`: Increase transmission power for 3266772_1
- `C5`: Adjust the azimuth of 3266772_1 by 25 degrees
- `C6`: Increase A3 Offset threshold for 3266772_1
- `C7`: Add neighbor relationship between 3266772_1 and 3227833_2
- `C8`: Decrease transmission power for 3227833_2
- `C9`: Adjust the azimuth of 3227833_2 by 23 degrees
- `C10`: Decrease A3 Offset threshold for 3266772_1
- `C11`: Check test server and transmission issues
- `C12`: Increase transmission power for 3227833_2
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3227833_2
- `C14`: Press down the tilt angle of 3266772_1 by 3 degrees
- `C15`: Insufficient data; more data is needed for judgment.
- `C16`: Add neighbor relationship between 3259601_7 and 3227833_2
- `C17`: Decrease A3 Offset threshold for 3227833_2
- `C18`: Lift the tilt angle of 3266772_1 by 3 degrees
- `C19`: Increase A3 Offset threshold for 3227833_2
- `C20`: Press down the tilt angle  of 3227833_2 by 1 degrees
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3227833_2
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3266772_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.554 | MS1 | 121.4656641216 | 31.1446319722 | 550 | 504990 | -94.85 | 10.54 | 414.30 | 0.06 | 2.15 | 1594 |
| 2024-09-20 22:21:32.187 | MS1 | 121.4656596024 | 31.1446250572 | 55 | 504990 | -93.21 | 10.61 | 534.36 | 0.05 | 2.24 | 1583 |
| 2024-09-20 22:21:33.265 | MS1 | 121.4656767870 | 31.1446319065 | 18 | 504990 | -93.67 | 12.80 | 437.13 | 0.20 | 2.18 | 1576 |
| 2024-09-20 22:21:34.877 | MS1 | 121.4656657230 | 31.1446196156 | 756 | 152650 | -88.72 | 3.92 | 74.87 | 0.14 | 1.75 | 957 |
| 2024-09-20 22:21:35.751 | MS1 | 121.4656581131 | 31.1446358352 | 958 | 152650 | -89.55 | 4.71 | 80.17 | 0.16 | 1.86 | 973 |
| 2024-09-20 22:21:36.920 | MS1 | 121.4656613590 | 31.1446304943 | 259 | 152650 | -89.94 | 4.29 | 70.90 | 0.00 | 1.99 | 975 |
| 2024-09-20 22:21:37.548 | MS1 | 121.4656619529 | 31.1446349612 | 986 | 152650 | -94.33 | 4.54 | 101.57 | 0.20 | 1.51 | 949 |
| 2024-09-20 22:21:38.854 | MS1 | 121.4656689396 | 31.1446333383 | 756 | 152650 | -95.26 | 3.05 | 85.33 | 0.02 | 1.65 | 954 |
| 2024-09-20 22:21:39.973 | MS1 | 121.4656652059 | 31.1446375748 | 958 | 152650 | -89.31 | 5.08 | 92.22 | 0.18 | 1.56 | 919 |
| 2024-09-20 22:21:40.767 | MS1 | 121.4656705124 | 31.1446256559 | 259 | 152650 | -94.06 | 6.31 | 92.76 | 0.17 | 2.13 | 1567 |
| 2024-09-20 22:21:41.948 | MS1 | 121.4656694814 | 31.1446183508 | 986 | 152650 | -90.36 | 4.37 | 51.45 | 0.07 | 2.93 | 1591 |
| 2024-09-20 22:21:42.412 | MS1 | 121.4656627136 | 31.1446360227 | 756 | 152650 | -94.50 | 7.25 | 70.40 | 0.08 | 2.57 | 1586 |

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
| 3215285 | 3 | 121.4689044567 | 31.1447038226 | 3 | 11 | 2 | 29.6 | TDD | 18 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3219875 | 8 | 121.4672488305 | 31.1526477077 | 54 | 4 | 3 | 27.0 | FDD | 569 | n1 | 152650 | 30M | 4T4R | 13 | 152650 |
| 3227833 | 2 | 121.4672900770 | 31.1479790619 | 179 | 0 | 7 | 10.5 | TDD | 426 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3234781 | 11 | 121.4717421598 | 31.1482323896 | 106 | 1 | 7 | 8.4 | FDD | 729 | n1 | 152650 | 30M | 4T4R | 15 | 152650 |
| 3236038 | 13 | 121.4750191774 | 31.1451499870 | 239 | 8 | 6 | 10.2 | FDD | 958 | n1 | 152650 | 30M | 4T4R | 19 | 152650 |
| 3246280 | 5 | 121.4703471523 | 31.1481643144 | 303 | 1 | 11 | 10.4 | TDD | 154 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3254357 | 12 | 121.4684211048 | 31.1485386441 | 359 | 1 | 9 | 8.4 | FDD | 986 | n1 | 152650 | 30M | 4T4R | 13 | 152650 |
| 3258459 | 6 | 121.4693102733 | 31.1548840794 | 270 | 13 | 0 | 21.2 | TDD | 286 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3259601 | 7 | 121.4704308383 | 31.1466255590 | 262 | 14 | 0 | 3.3 | FDD | 259 | n1 | 152650 | 30M | 4T4R | 11 | 152650 |
| 3263861 | 10 | 121.4644585097 | 31.1469237659 | 325 | 14 | 10 | 21.8 | FDD | 758 | n1 | 152650 | 30M | 4T4R | 28 | 152650 |
| 3266772 | 1 | 121.4679807383 | 31.1490692142 | 179 | 0 | 1 | 26.7 | TDD | 550 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3275308 | 4 | 121.4699112284 | 31.1459712078 | 12 | 15 | 2 | 0.5 | TDD | 55 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3279882 | 9 | 121.4685444526 | 31.1519103707 | 357 | 14 | 9 | 14.4 | FDD | 756 | n1 | 152650 | 30M | 4T4R | 28 | 152650 |

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
| 2024-09-20 22:21:30.993 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.010 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.127 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.127 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.878 | NREventA2 | measId:1;ServCellPCI:163;Se... |
| 2024-09-20 22:21:35.028 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.228 | NREventA5 | measId:3;ServCellPCI:163;Se... |
| 2024-09-20 22:21:35.301 | NRHandoverAttempt | SourcePCI:163;SourceNR-ARFC... |
| 2024-09-20 22:21:35.338 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.351 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:35.488 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.488 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3266772 | 1 | 13.4504 | 16.7662 | -114.7465 | 16.4410 | 114.7653 | 0.0171 | 0.0171 |
| 2024_09_20 22:00 | 3227833 | 2 | 18.0529 | 18.9838 | -117.8339 | 15.4245 | 127.8046 | 0.0173 | 0.0107 |
| 2024_09_20 22:00 | 3215285 | 3 | 8.5245 | 7.3729 | -114.2202 | 6.8320 | 196.6711 | 0.0025 | 0.0180 |
| 2024_09_20 22:00 | 3275308 | 4 | 6.5498 | 15.9798 | -117.1794 | 12.9235 | 113.6086 | 0.0003 | 0.0047 |
| 2024_09_20 22:00 | 3246280 | 5 | 5.2818 | 19.0032 | -115.1433 | 9.5806 | 131.1204 | 0.0093 | 0.0148 |
| 2024_09_20 22:00 | 3258459 | 6 | 13.4275 | 16.3747 | -116.9622 | 15.9661 | 97.4889 | 0.0103 | 0.0111 |
| 2024_09_20 22:00 | 3259601 | 7 | 18.4067 | 9.2412 | -114.5083 | 4.1701 | 38.6497 | 0.0192 | 0.0012 |
| 2024_09_20 22:00 | 3219875 | 8 | 13.5567 | 18.3364 | -115.6021 | 3.6450 | 45.1134 | 0.0134 | 0.0144 |
| 2024_09_20 22:00 | 3279882 | 9 | 15.6162 | 14.2824 | -116.8215 | 4.1443 | 59.8100 | 0.0050 | 0.0020 |
| 2024_09_20 22:00 | 3263861 | 10 | 19.8710 | 17.3661 | -117.4319 | 3.6236 | 58.9657 | 0.0060 | 0.0045 |
| 2024_09_20 22:00 | 3234781 | 11 | 7.3718 | 10.7829 | -114.7459 | 3.2576 | 46.5142 | 0.0002 | 0.0006 |
| 2024_09_20 22:00 | 3254357 | 12 | 17.0440 | 5.6566 | -115.1328 | 3.6033 | 48.1137 | 0.0157 | 0.0009 |
| 2024_09_20 22:00 | 3236038 | 13 | 15.6593 | 16.4284 | -116.8966 | 3.3083 | 29.7026 | 0.0184 | 0.0114 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412354_2DB0FD76 | 152650 | 756 | -90.7 | 152650 | 729 | -94.0 | 152650 | 758 | -97.0 | 152650 | 569 |
| MR_1774412354_F43B2850 | 152650 | 756 | -90.2 | 152650 | 729 | -96.0 | 152650 | 758 | -99.1 | 152650 | 569 |
| MR_1774412354_A2968851 | 152650 | 756 | -87.8 | 152650 | 729 | -93.9 | 152650 | 758 | -96.1 | 152650 | 569 |
| MR_1774412354_65B593A7 | 504990 | 18 | -93.4 | 504990 | 426 | -94.6 | 504990 | 286 | -92.2 | 504990 | 154 |
| MR_1774412354_CA564605 | 152650 | 756 | -87.9 | 152650 | 729 | -96.6 | 152650 | 758 | -96.6 | 152650 | 569 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1194: `3d8c80cc-7e6...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `3d8c80cc-7e68-4efb-ba34-648a84360165` |
| Tag | **single-answer** |
| 정답 | **C14** |
| C14 의미 | Lift the tilt angle  of 3277065_3 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1194] topology](images/train_1194.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Check test server and transmission issues
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3236051_2
- `C3`: Decrease A3 Offset threshold for 3236051_2
- `C4`: Lift the tilt angle of 3236051_2 by 1 degrees
- `C5`: Decrease transmission power for 3253011_1
- `C6`: Increase transmission power for 3236051_2
- `C7`: Decrease A3 Offset threshold for 3253011_1
- `C8`: Increase A3 Offset threshold for 3236051_2
- `C9`: Decrease transmission power for 3236051_2
- `C10`: Increase A3 Offset threshold for 3253011_1
- `C11`: Add neighbor relationship between 3236051_2 and 3253011_1
- `C12`: Adjust the azimuth of 3236051_2 by 41 degrees
- `C13`: Insufficient data; more data is needed for judgment.
- `C14`: Lift the tilt angle  of 3277065_3 by 10 degrees **← 정답**
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3253011_1
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3253011_1
- `C17`: Adjust the azimuth of 3277065_3 by 50 degrees
- `C18`: Press down the tilt angle of 3236051_2 by 1 degrees
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3236051_2
- `C20`: Add neighbor relationship between 3277065_3 and 3253011_1
- `C21`: Press down the tilt angle  of 3277065_3 by 10 degrees
- `C22`: Increase transmission power for 3253011_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.229 | MS1 | 121.4656706584 | 31.1446183738 | 515 | 504990 | -87.04 | 13.74 | 526.35 | 0.11 | 2.60 | 1575 |
| 2024-09-20 22:21:32.959 | MS1 | 121.4656669193 | 31.1446197645 | 515 | 504990 | -86.65 | 14.94 | 586.83 | 0.07 | 2.99 | 1589 |
| 2024-09-20 22:21:33.178 | MS1 | 121.4656707082 | 31.1446365072 | 515 | 504990 | -89.85 | 17.97 | 313.70 | 0.10 | 2.86 | 1591 |
| 2024-09-20 22:21:34.300 | MS1 | 121.4656760439 | 31.1446356033 | 515 | 504990 | -85.08 | 14.15 | 63.46 | 0.11 | 2.13 | 1563 |
| 2024-09-20 22:21:35.202 | MS1 | 121.4656690086 | 31.1446205755 | 515 | 504990 | -87.36 | 12.55 | 55.19 | 0.09 | 2.94 | 1588 |
| 2024-09-20 22:21:36.569 | MS1 | 121.4656729406 | 31.1446204132 | 515 | 504990 | -87.52 | 14.58 | 78.07 | 0.00 | 2.74 | 1582 |
| 2024-09-20 22:21:37.136 | MS1 | 121.4656725243 | 31.1446180660 | 515 | 504990 | -90.55 | 8.26 | 51.85 | 0.02 | 2.24 | 1580 |
| 2024-09-20 22:21:38.925 | MS1 | 121.4656622957 | 31.1446244449 | 515 | 504990 | -91.43 | 8.61 | 49.72 | 0.02 | 2.37 | 1597 |
| 2024-09-20 22:21:39.133 | MS1 | 121.4656615649 | 31.1446324357 | 515 | 504990 | -91.72 | 7.03 | 56.04 | 0.01 | 2.26 | 1581 |
| 2024-09-20 22:21:40.155 | MS1 | 121.4656607534 | 31.1446245649 | 515 | 504990 | -93.67 | 10.53 | 470.54 | 0.03 | 2.20 | 1585 |
| 2024-09-20 22:21:41.446 | MS1 | 121.4656744367 | 31.1446379365 | 515 | 504990 | -92.61 | 7.78 | 576.48 | 0.03 | 2.56 | 1596 |
| 2024-09-20 22:21:42.963 | MS1 | 121.4656584252 | 31.1446270759 | 515 | 504990 | -92.85 | 11.58 | 526.18 | 0.09 | 2.48 | 1599 |

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
| 3236051 | 2 | 121.4683620805 | 31.1549617214 | 234 | 0 | 12 | 27.9 | TDD | 515 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3253011 | 1 | 121.4741310379 | 31.1443412391 | 336 | 14 | 1 | 21.9 | TDD | 880 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3277065 | 3 | 121.4644397379 | 31.1455921375 | 336 | 10 | 1 | 19.9 | TDD | 188 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3278574 | 4 | 121.4669343764 | 31.1440845243 | 317 | 11 | 4 | 31.4 | TDD | 839 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |

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
| 2024-09-20 22:21:31.188 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.207 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.311 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.311 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.088 | NREventA3 | measId:2;ServCellPCI:231;Se... |
| 2024-09-20 22:21:38.328 | NRHandoverAttempt | SourcePCI:231;SourceNR-ARFC... |
| 2024-09-20 22:21:38.375 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.385 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.508 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.508 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3253011 | 1 | 14.6359 | 8.5342 | -115.1566 | 8.7772 | 183.4858 | 0.0196 | 0.0172 |
| 2024_09_20 22:00 | 3236051 | 2 | 85.8094 | 78.4646 | -114.9358 | 6.7086 | 148.8032 | 0.0173 | 0.0092 |
| 2024_09_20 22:00 | 3277065 | 3 | 10.7565 | 17.0611 | -114.6670 | 19.3185 | 104.9189 | 0.0171 | 0.0140 |
| 2024_09_20 22:00 | 3278574 | 4 | 15.0580 | 15.8760 | -117.9220 | 11.7528 | 193.8778 | 0.0169 | 0.0102 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416491_A1B9F417 | 504990 | 515 | -84.5 | 504990 | 880 | -90.6 | 504990 | 188 | -97.3 | 504990 | 839 |
| MR_1774416491_5A165E69 | 504990 | 515 | -83.6 | 504990 | 880 | -89.4 | 504990 | 188 | -96.4 | 504990 | 839 |
| MR_1774416491_FD80202B | 504990 | 515 | -86.6 | 504990 | 880 | -90.2 | 504990 | 188 | -98.5 | 504990 | 839 |
| MR_1774416491_9439EBDD | 504990 | 515 | -84.4 | 504990 | 880 | -87.2 | 504990 | 188 | -99.4 | 504990 | 839 |
| MR_1774416491_2DE93528 | 504990 | 515 | -85.3 | 504990 | 880 | -88.6 | 504990 | 188 | -96.2 | 504990 | 839 |
| MR_1774416491_2C7488EA | 504990 | 515 | -84.5 | 504990 | 880 | -88.1 | 504990 | 188 | -97.8 | 504990 | 839 |
| MR_1774416491_D3345090 | 504990 | 515 | -83.1 | 504990 | 880 | -87.5 | 504990 | 188 | -98.0 | 504990 | 839 |
| MR_1774416491_93A627A8 | 504990 | 515 | -83.4 | 504990 | 880 | -87.8 | 504990 | 188 | -98.1 | 504990 | 839 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1195: `e919cd95-d25...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `e919cd95-d25d-437b-b226-192590c87a33` |
| Tag | **single-answer** |
| 정답 | **C8** |
| C8 의미 | Decrease A3 Offset threshold for 3229028_3 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1195] topology](images/train_1195.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle  of 3275813_2 by 10 degrees
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3275813_2
- `C3`: Increase A3 Offset threshold for 3275813_2
- `C4`: Decrease A3 Offset threshold for 3275813_2
- `C5`: Press down the tilt angle of 3229028_3 by 10 degrees
- `C6`: Lift the tilt angle of 3229028_3 by 10 degrees
- `C7`: Increase transmission power for 3275813_2
- `C8`: Decrease A3 Offset threshold for 3229028_3 **← 정답**
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3275813_2
- `C10`: Add neighbor relationship between 3255535_1 and 3275813_2
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3229028_3
- `C12`: Increase transmission power for 3229028_3
- `C13`: Insufficient data; more data is needed for judgment.
- `C14`: Decrease transmission power for 3275813_2
- `C15`: Press down the tilt angle  of 3275813_2 by 10 degrees
- `C16`: Add neighbor relationship between 3229028_3 and 3275813_2
- `C17`: Check test server and transmission issues
- `C18`: Adjust the azimuth of 3229028_3 by 47 degrees
- `C19`: Adjust the azimuth of 3275813_2 by 50 degrees
- `C20`: Decrease transmission power for 3229028_3
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3229028_3
- `C22`: Increase A3 Offset threshold for 3229028_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.197 | MS1 | 121.4656713841 | 31.1446350396 | 828 | 504990 | -78.22 | 17.43 | 384.55 | 0.04 | 2.33 | 1577 |
| 2024-09-20 22:21:32.101 | MS1 | 121.4656721363 | 31.1446350305 | 828 | 504990 | -84.29 | 16.30 | 328.15 | 0.13 | 2.86 | 1578 |
| 2024-09-20 22:21:33.943 | MS1 | 121.4656654877 | 31.1446363345 | 828 | 504990 | -82.93 | 17.90 | 443.98 | 0.16 | 2.08 | 1585 |
| 2024-09-20 22:21:34.761 | MS1 | 121.4656585668 | 31.1446273896 | 828 | 504990 | -85.89 | -2.57 | 51.47 | 0.14 | 1.03 | 1583 |
| 2024-09-20 22:21:35.317 | MS1 | 121.4656758624 | 31.1446214312 | 828 | 504990 | -85.80 | -0.33 | 57.67 | 0.01 | 1.24 | 1599 |
| 2024-09-20 22:21:36.249 | MS1 | 121.4656650532 | 31.1446308451 | 828 | 504990 | -91.42 | -3.12 | 60.91 | 0.14 | 1.32 | 1582 |
| 2024-09-20 22:21:37.667 | MS1 | 121.4656660949 | 31.1446227496 | 828 | 504990 | -90.99 | -2.58 | 33.06 | 0.02 | 1.40 | 1589 |
| 2024-09-20 22:21:38.850 | MS1 | 121.4656623172 | 31.1446200789 | 828 | 504990 | -92.06 | -0.19 | 49.61 | 0.14 | 1.32 | 1583 |
| 2024-09-20 22:21:39.318 | MS1 | 121.4656766958 | 31.1446259728 | 162 | 504990 | -75.37 | 14.41 | 275.88 | 0.06 | 1.31 | 1563 |
| 2024-09-20 22:21:40.821 | MS1 | 121.4656745084 | 31.1446197367 | 162 | 504990 | -75.37 | 14.88 | 472.76 | 0.06 | 2.08 | 1587 |
| 2024-09-20 22:21:41.816 | MS1 | 121.4656640570 | 31.1446348834 | 162 | 504990 | -76.19 | 13.07 | 464.07 | 0.08 | 2.92 | 1571 |
| 2024-09-20 22:21:42.508 | MS1 | 121.4656620055 | 31.1446325254 | 162 | 504990 | -79.79 | 12.50 | 359.18 | 0.00 | 2.16 | 1564 |

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
| 3229028 | 3 | 121.4685858235 | 31.1530555916 | 150 | 12 | 2 | 19.7 | TDD | 828 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3233223 | 4 | 121.4696090241 | 31.1449100447 | 130 | 0 | 6 | 29.4 | TDD | 446 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3255535 | 1 | 121.4693775202 | 31.1450695631 | 5 | 3 | 11 | 38.7 | TDD | 281 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3275813 | 2 | 121.4646563543 | 31.1447398086 | 44 | 2 | 5 | 32.9 | TDD | 162 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

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
| 2024-09-20 22:21:30.975 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.993 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.097 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.097 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.802 | NREventA3 | measId:2;ServCellPCI:481;Se... |
| 2024-09-20 22:21:38.042 | NRHandoverAttempt | SourcePCI:481;SourceNR-ARFC... |
| 2024-09-20 22:21:38.087 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.097 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.215 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.215 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3255535 | 1 | 5.8179 | 15.7434 | -116.1634 | 9.5044 | 146.6162 | 0.0090 | 0.0017 |
| 2024_09_20 22:00 | 3275813 | 2 | 13.4262 | 19.8519 | -117.7786 | 6.5356 | 191.2595 | 0.0141 | 0.0049 |
| 2024_09_20 22:00 | 3229028 | 3 | 12.4969 | 8.1449 | -114.2868 | 10.0269 | 81.0709 | 0.0111 | 0.1879 |
| 2024_09_20 22:00 | 3233223 | 4 | 17.9817 | 10.5842 | -116.7082 | 16.9470 | 163.0013 | 0.0004 | 0.0163 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414829_3F65F7AB | 504990 | 162 | -80.2 | 504990 | 828 | -85.5 | 504990 | 281 | -82.2 | 504990 | 446 |
| MR_1774414829_5F044674 | 504990 | 828 | -84.3 | 504990 | 162 | -80.7 | 504990 | 281 | -83.8 | 504990 | 446 |
| MR_1774414829_D6489E33 | 504990 | 828 | -86.5 | 504990 | 162 | -81.5 | 504990 | 281 | -81.0 | 504990 | 446 |
| MR_1774414829_3C61258D | 504990 | 162 | -79.2 | 504990 | 828 | -86.0 | 504990 | 281 | -82.8 | 504990 | 446 |
| MR_1774414829_D858BC0B | 504990 | 828 | -86.8 | 504990 | 162 | -79.4 | 504990 | 281 | -84.4 | 504990 | 446 |
| MR_1774414829_3F64D8D1 | 504990 | 828 | -86.1 | 504990 | 162 | -78.9 | 504990 | 281 | -82.2 | 504990 | 446 |
| MR_1774414829_6DB54C83 | 504990 | 828 | -85.9 | 504990 | 162 | -78.9 | 504990 | 281 | -81.5 | 504990 | 446 |
| MR_1774414829_791EE514 | 504990 | 162 | -80.0 | 504990 | 828 | -86.0 | 504990 | 281 | -81.0 | 504990 | 446 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1196: `51d60cb4-669...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `51d60cb4-669d-47ec-9fcc-88eac1253b88` |
| Tag | **single-answer** |
| 정답 | **C17** |
| C17 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1196] topology](images/train_1196.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3237309_1 by 6 degrees
- `C2`: Decrease A3 Offset threshold for 3253269_2
- `C3`: Decrease transmission power for 3253269_2
- `C4`: Decrease transmission power for 3237309_1
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3253269_2
- `C6`: Adjust the azimuth of 3237309_1 by 50 degrees
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3237309_1
- `C8`: Insufficient data; more data is needed for judgment.
- `C9`: Add neighbor relationship between 3275085_4 and 3253269_2
- `C10`: Decrease A3 Offset threshold for 3237309_1
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3253269_2
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3237309_1
- `C13`: Lift the tilt angle  of 3253269_2 by 5 degrees
- `C14`: Press down the tilt angle  of 3253269_2 by 5 degrees
- `C15`: Add neighbor relationship between 3237309_1 and 3253269_2
- `C16`: Press down the tilt angle of 3237309_1 by 6 degrees
- `C17`: Check test server and transmission issues **← 정답**
- `C18`: Increase A3 Offset threshold for 3253269_2
- `C19`: Adjust the azimuth of 3253269_2 by 50 degrees
- `C20`: Increase transmission power for 3253269_2
- `C21`: Increase transmission power for 3237309_1
- `C22`: Increase A3 Offset threshold for 3237309_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.169 | MS1 | 121.4656643768 | 31.1446265561 | 619 | 504990 | -89.09 | 15.73 | 341.48 | 0.07 | 2.80 | 1574 |
| 2024-09-20 22:21:32.306 | MS1 | 121.4656608054 | 31.1446303099 | 619 | 504990 | -91.50 | 16.65 | 325.10 | 0.09 | 2.27 | 1596 |
| 2024-09-20 22:21:33.442 | MS1 | 121.4656586818 | 31.1446220017 | 619 | 504990 | -87.23 | 15.25 | 520.71 | 0.02 | 2.05 | 1567 |
| 2024-09-20 22:21:34.301 | MS1 | 121.4656663251 | 31.1446347786 | 619 | 504990 | -85.15 | 12.81 | 69.83 | 0.05 | 2.77 | 352 |
| 2024-09-20 22:21:35.904 | MS1 | 121.4656727091 | 31.1446324488 | 619 | 504990 | -89.71 | 15.46 | 77.91 | 0.07 | 2.77 | 354 |
| 2024-09-20 22:21:36.480 | MS1 | 121.4656751124 | 31.1446258123 | 619 | 504990 | -89.31 | 16.79 | 75.92 | 0.19 | 2.41 | 499 |
| 2024-09-20 22:21:37.911 | MS1 | 121.4656632979 | 31.1446198246 | 619 | 504990 | -89.76 | 8.52 | 60.04 | 0.09 | 2.63 | 300 |
| 2024-09-20 22:21:38.489 | MS1 | 121.4656607289 | 31.1446198401 | 619 | 504990 | -90.65 | 8.98 | 87.80 | 0.11 | 2.36 | 324 |
| 2024-09-20 22:21:39.170 | MS1 | 121.4656637442 | 31.1446377445 | 619 | 504990 | -89.75 | 12.02 | 78.07 | 0.16 | 2.03 | 449 |
| 2024-09-20 22:21:40.147 | MS1 | 121.4656617824 | 31.1446218375 | 619 | 504990 | -92.98 | 10.27 | 319.50 | 0.11 | 2.13 | 1580 |
| 2024-09-20 22:21:41.447 | MS1 | 121.4656741956 | 31.1446243304 | 619 | 504990 | -90.68 | 12.57 | 596.47 | 0.05 | 2.26 | 1567 |
| 2024-09-20 22:21:42.295 | MS1 | 121.4656712609 | 31.1446367530 | 619 | 504990 | -89.87 | 9.61 | 313.46 | 0.02 | 2.59 | 1595 |

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
| 3228069 | 3 | 121.4668451228 | 31.1461814496 | 271 | 14 | 10 | 46.5 | TDD | 67 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3237309 | 1 | 121.4666879154 | 31.1558785323 | 13 | 4 | 0 | 40.7 | TDD | 619 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3253269 | 2 | 121.4660052303 | 31.1533233206 | 53 | 3 | 1 | 34.3 | TDD | 927 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3275085 | 4 | 121.4706724429 | 31.1473373439 | 316 | 4 | 3 | 34.4 | TDD | 255 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:31.630 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.646 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.753 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.753 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.495 | NREventA3 | measId:2;ServCellPCI:829;Se... |
| 2024-09-20 22:21:38.735 | NRHandoverAttempt | SourcePCI:829;SourceNR-ARFC... |
| 2024-09-20 22:21:38.766 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.776 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.898 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.898 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3237309 | 1 | 5.0565 | 19.8498 | -115.5524 | 9.4150 | 147.4473 | 0.0039 | 0.0078 |
| 2024_09_20 22:00 | 3253269 | 2 | 6.8770 | 18.2332 | -115.7096 | 11.9438 | 175.7211 | 0.0176 | 0.0128 |
| 2024_09_20 22:00 | 3228069 | 3 | 9.1936 | 7.3313 | -116.2697 | 16.2146 | 121.0796 | 0.0162 | 0.0141 |
| 2024_09_20 22:00 | 3275085 | 4 | 18.0168 | 19.7580 | -114.0646 | 9.7836 | 101.8553 | 0.0155 | 0.0039 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417008_8458C840 | 504990 | 619 | -85.0 | 504990 | 927 | -88.3 | 504990 | 255 | -92.9 | 504990 | 67 |
| MR_1774417008_2D47D00B | 504990 | 619 | -86.2 | 504990 | 927 | -86.6 | 504990 | 255 | -91.3 | 504990 | 67 |
| MR_1774417008_10BD4F21 | 504990 | 619 | -85.1 | 504990 | 927 | -86.6 | 504990 | 255 | -90.0 | 504990 | 67 |
| MR_1774417008_70178A86 | 504990 | 619 | -83.6 | 504990 | 927 | -88.0 | 504990 | 255 | -93.6 | 504990 | 67 |
| MR_1774417008_206889A5 | 504990 | 619 | -87.1 | 504990 | 927 | -87.4 | 504990 | 255 | -93.5 | 504990 | 67 |
| MR_1774417008_1EF09419 | 504990 | 619 | -87.0 | 504990 | 927 | -87.8 | 504990 | 255 | -90.0 | 504990 | 67 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1197: `dc29a039-d5a...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `dc29a039-d5a1-422a-a6ca-5c573badb1ba` |
| Tag | **single-answer** |
| 정답 | **C18** |
| C18 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3278248_1 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1197] topology](images/train_1197.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3278248_1 by 49 degrees
- `C2`: Lift the tilt angle  of 3245588_3 by 5 degrees
- `C3`: Adjust the azimuth of 3245588_3 by 16 degrees
- `C4`: Increase A3 Offset threshold for 3245588_3
- `C5`: Add neighbor relationship between 3256213_12 and 3245588_3
- `C6`: Increase transmission power for 3278248_1
- `C7`: Decrease A3 Offset threshold for 3245588_3
- `C8`: Lift the tilt angle of 3278248_1 by 6 degrees
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3278248_1
- `C10`: Decrease A3 Offset threshold for 3278248_1
- `C11`: Insufficient data; more data is needed for judgment.
- `C12`: Check test server and transmission issues
- `C13`: Decrease transmission power for 3245588_3
- `C14`: Add neighbor relationship between 3278248_1 and 3245588_3
- `C15`: Decrease transmission power for 3278248_1
- `C16`: Press down the tilt angle  of 3245588_3 by 5 degrees
- `C17`: Increase A3 Offset threshold for 3278248_1
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3278248_1 **← 정답**
- `C19`: Press down the tilt angle of 3278248_1 by 6 degrees
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3245588_3
- `C21`: Increase transmission power for 3245588_3
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3245588_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.938 | MS1 | 121.4656736425 | 31.1446361699 | 577 | 504990 | -94.01 | 14.06 | 388.46 | 0.04 | 2.29 | 1593 |
| 2024-09-20 22:21:32.562 | MS1 | 121.4656702423 | 31.1446193218 | 857 | 504990 | -94.13 | 12.48 | 546.26 | 0.14 | 2.25 | 1573 |
| 2024-09-20 22:21:33.221 | MS1 | 121.4656759024 | 31.1446339934 | 732 | 504990 | -94.72 | 14.51 | 343.92 | 0.03 | 2.44 | 1570 |
| 2024-09-20 22:21:34.724 | MS1 | 121.4656689816 | 31.1446260792 | 28 | 152650 | -92.68 | 2.71 | 66.40 | 0.08 | 1.63 | 946 |
| 2024-09-20 22:21:35.554 | MS1 | 121.4656625266 | 31.1446201762 | 674 | 152650 | -93.06 | 5.22 | 77.09 | 0.12 | 1.81 | 966 |
| 2024-09-20 22:21:36.671 | MS1 | 121.4656732710 | 31.1446378874 | 658 | 152650 | -92.26 | 2.47 | 57.96 | 0.14 | 1.99 | 957 |
| 2024-09-20 22:21:37.648 | MS1 | 121.4656629562 | 31.1446344467 | 719 | 152650 | -93.25 | 3.49 | 66.32 | 0.16 | 1.53 | 993 |
| 2024-09-20 22:21:38.712 | MS1 | 121.4656779132 | 31.1446199215 | 28 | 152650 | -94.74 | 3.12 | 104.96 | 0.04 | 1.56 | 924 |
| 2024-09-20 22:21:39.960 | MS1 | 121.4656632011 | 31.1446239788 | 674 | 152650 | -87.77 | 3.73 | 58.46 | 0.03 | 1.80 | 924 |
| 2024-09-20 22:21:40.144 | MS1 | 121.4656751903 | 31.1446342995 | 658 | 152650 | -87.82 | 5.12 | 90.81 | 0.07 | 2.19 | 1579 |
| 2024-09-20 22:21:41.979 | MS1 | 121.4656695625 | 31.1446320724 | 719 | 152650 | -87.92 | 3.95 | 93.13 | 0.09 | 2.70 | 1563 |
| 2024-09-20 22:21:42.574 | MS1 | 121.4656774018 | 31.1446263794 | 28 | 152650 | -87.99 | 3.68 | 52.70 | 0.10 | 2.38 | 1560 |

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
| 3213648 | 6 | 121.4683106386 | 31.1497015612 | 120 | 11 | 3 | 7.4 | TDD | 732 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3214345 | 11 | 121.4747972125 | 31.1543284127 | 185 | 4 | 3 | 29.6 | FDD | 719 | n1 | 152650 | 30M | 4T4R | 18 | 152650 |
| 3215570 | 7 | 121.4739139916 | 31.1509000136 | 19 | 13 | 11 | 26.7 | FDD | 674 | n1 | 152650 | 30M | 4T4R | 14 | 152650 |
| 3215835 | 8 | 121.4658535063 | 31.1535588334 | 111 | 15 | 6 | 17.5 | FDD | 2 | n1 | 152650 | 30M | 4T4R | 12 | 152650 |
| 3219341 | 9 | 121.4679009733 | 31.1448675928 | 62 | 0 | 1 | 2.4 | FDD | 648 | n1 | 152650 | 30M | 4T4R | 26 | 152650 |
| 3226113 | 10 | 121.4730544253 | 31.1510381428 | 336 | 14 | 5 | 25.1 | FDD | 266 | n1 | 152650 | 30M | 4T4R | 25 | 152650 |
| 3237724 | 5 | 121.4714644308 | 31.1463797140 | 215 | 15 | 3 | 3.1 | TDD | 857 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3243592 | 4 | 121.4644916220 | 31.1519114018 | 97 | 10 | 4 | 0.8 | TDD | 629 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3245588 | 3 | 121.4724403987 | 31.1516333487 | 204 | 4 | 8 | 10.6 | TDD | 710 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3256213 | 12 | 121.4702098285 | 31.1524666917 | 84 | 10 | 9 | 5.3 | FDD | 658 | n1 | 152650 | 30M | 4T4R | 11 | 152650 |
| 3272444 | 2 | 121.4701680991 | 31.1542879351 | 52 | 5 | 9 | 20.5 | TDD | 642 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3274191 | 13 | 121.4640502170 | 31.1468030968 | 281 | 12 | 6 | 25.7 | FDD | 28 | n1 | 152650 | 30M | 4T4R | 24 | 152650 |
| 3278248 | 1 | 121.4752963001 | 31.1443168627 | 223 | 5 | 8 | 11.8 | TDD | 577 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:30.949 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.968 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.113 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.113 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.839 | NREventA2 | measId:1;ServCellPCI:985;Se... |
| 2024-09-20 22:21:34.962 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.252 | NREventA5 | measId:3;ServCellPCI:985;Se... |
| 2024-09-20 22:21:35.314 | NRHandoverAttempt | SourcePCI:985;SourceNR-ARFC... |
| 2024-09-20 22:21:35.358 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.370 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:35.470 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.470 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3278248 | 1 | 5.3371 | 18.3526 | -115.4170 | 17.6704 | 118.1800 | 0.0125 | 0.0113 |
| 2024_09_20 22:00 | 3272444 | 2 | 9.4274 | 10.3551 | -115.3997 | 16.5361 | 199.4891 | 0.0079 | 0.0034 |
| 2024_09_20 22:00 | 3245588 | 3 | 17.4866 | 15.5080 | -117.2332 | 14.2897 | 120.9072 | 0.0132 | 0.0167 |
| 2024_09_20 22:00 | 3243592 | 4 | 14.1088 | 5.3058 | -116.2260 | 12.2967 | 175.8192 | 0.0018 | 0.0079 |
| 2024_09_20 22:00 | 3237724 | 5 | 8.7632 | 9.4561 | -115.2874 | 19.4180 | 198.6669 | 0.0175 | 0.0028 |
| 2024_09_20 22:00 | 3213648 | 6 | 9.1326 | 10.9382 | -115.5415 | 17.3148 | 83.0417 | 0.0084 | 0.0165 |
| 2024_09_20 22:00 | 3215570 | 7 | 12.4560 | 14.8689 | -114.8438 | 4.5932 | 44.7237 | 0.0181 | 0.0155 |
| 2024_09_20 22:00 | 3215835 | 8 | 6.8497 | 17.1293 | -114.7210 | 3.2448 | 44.1363 | 0.0007 | 0.0114 |
| 2024_09_20 22:00 | 3219341 | 9 | 5.1535 | 14.9513 | -114.4008 | 3.7884 | 41.2365 | 0.0083 | 0.0131 |
| 2024_09_20 22:00 | 3226113 | 10 | 8.8923 | 17.8254 | -116.1483 | 4.5886 | 54.0156 | 0.0195 | 0.0194 |
| 2024_09_20 22:00 | 3214345 | 11 | 16.6196 | 9.4289 | -116.0713 | 3.9980 | 39.2298 | 0.0175 | 0.0075 |
| 2024_09_20 22:00 | 3256213 | 12 | 5.1941 | 5.5741 | -114.1824 | 3.0575 | 33.9809 | 0.0119 | 0.0032 |
| 2024_09_20 22:00 | 3274191 | 13 | 7.9329 | 5.6354 | -114.8192 | 3.9372 | 56.0431 | 0.0017 | 0.0037 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413863_88CC713C | 152650 | 28 | -92.4 | 152650 | 648 | -97.0 | 152650 | 2 | -100.2 | 152650 | 266 |
| MR_1774413863_5B941E12 | 152650 | 28 | -93.4 | 152650 | 648 | -96.9 | 152650 | 2 | -102.5 | 152650 | 266 |
| MR_1774413863_28D2FC9C | 152650 | 28 | -93.5 | 152650 | 648 | -94.7 | 152650 | 2 | -102.6 | 152650 | 266 |
| MR_1774413863_EED8D943 | 152650 | 28 | -94.1 | 152650 | 648 | -95.3 | 152650 | 2 | -100.3 | 152650 | 266 |
| MR_1774413863_5AE2EAF0 | 152650 | 28 | -90.9 | 152650 | 648 | -94.3 | 152650 | 2 | -100.5 | 152650 | 266 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1198: `7fda8777-c3c...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `7fda8777-c3c7-439a-8348-a9390aba9310` |
| Tag | **single-answer** |
| 정답 | **C20** |
| C20 의미 | Decrease A3 Offset threshold for 3264310_2 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1198] topology](images/train_1198.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3264310_2
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3272921_1
- `C3`: Decrease A3 Offset threshold for 3272921_1
- `C4`: Decrease transmission power for 3272921_1
- `C5`: Check test server and transmission issues
- `C6`: Increase transmission power for 3264310_2
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3264310_2
- `C8`: Adjust the azimuth of 3264310_2 by 50 degrees
- `C9`: Lift the tilt angle of 3264310_2 by 10 degrees
- `C10`: Press down the tilt angle of 3264310_2 by 10 degrees
- `C11`: Add neighbor relationship between 3260573_4 and 3272921_1
- `C12`: Add neighbor relationship between 3264310_2 and 3272921_1
- `C13`: Decrease transmission power for 3264310_2
- `C14`: Adjust the azimuth of 3272921_1 by 50 degrees
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3272921_1
- `C16`: Insufficient data; more data is needed for judgment.
- `C17`: Press down the tilt angle  of 3272921_1 by 10 degrees
- `C18`: Lift the tilt angle  of 3272921_1 by 10 degrees
- `C19`: Increase transmission power for 3272921_1
- `C20`: Decrease A3 Offset threshold for 3264310_2 **← 정답**
- `C21`: Increase A3 Offset threshold for 3272921_1
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3264310_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.582 | MS1 | 121.4656734950 | 31.1446229313 | 131 | 504990 | -78.41 | 15.04 | 541.04 | 0.11 | 2.56 | 1594 |
| 2024-09-20 22:21:32.546 | MS1 | 121.4656757315 | 31.1446287377 | 131 | 504990 | -82.16 | 16.06 | 584.48 | 0.13 | 2.07 | 1587 |
| 2024-09-20 22:21:33.434 | MS1 | 121.4656742221 | 31.1446269508 | 131 | 504990 | -80.76 | 15.97 | 588.73 | 0.06 | 2.57 | 1589 |
| 2024-09-20 22:21:34.757 | MS1 | 121.4656580339 | 31.1446333367 | 131 | 504990 | -87.77 | -0.06 | 67.07 | 0.20 | 1.15 | 1583 |
| 2024-09-20 22:21:35.300 | MS1 | 121.4656680531 | 31.1446307896 | 131 | 504990 | -92.53 | -0.94 | 74.68 | 0.03 | 1.08 | 1560 |
| 2024-09-20 22:21:36.207 | MS1 | 121.4656637481 | 31.1446272818 | 131 | 504990 | -88.62 | -2.60 | 58.31 | 0.13 | 1.17 | 1578 |
| 2024-09-20 22:21:37.174 | MS1 | 121.4656640413 | 31.1446377158 | 131 | 504990 | -84.26 | -0.42 | 39.54 | 0.18 | 1.42 | 1561 |
| 2024-09-20 22:21:38.664 | MS1 | 121.4656669650 | 31.1446291352 | 131 | 504990 | -83.48 | -0.91 | 66.64 | 0.13 | 1.35 | 1579 |
| 2024-09-20 22:21:39.540 | MS1 | 121.4656682349 | 31.1446235415 | 266 | 504990 | -75.01 | 16.89 | 164.05 | 0.13 | 1.36 | 1585 |
| 2024-09-20 22:21:40.348 | MS1 | 121.4656731881 | 31.1446270304 | 266 | 504990 | -75.44 | 17.26 | 552.51 | 0.08 | 2.23 | 1565 |
| 2024-09-20 22:21:41.324 | MS1 | 121.4656596935 | 31.1446374183 | 266 | 504990 | -80.56 | 17.48 | 381.65 | 0.19 | 2.02 | 1582 |
| 2024-09-20 22:21:42.582 | MS1 | 121.4656600786 | 31.1446368506 | 266 | 504990 | -83.32 | 17.80 | 415.81 | 0.09 | 2.15 | 1584 |

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
| 3249641 | 3 | 121.4715674010 | 31.1539571505 | 232 | 3 | 12 | 49.4 | TDD | 156 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3260573 | 4 | 121.4748536006 | 31.1558267366 | 81 | 11 | 9 | 37.5 | TDD | 130 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3264310 | 2 | 121.4677867077 | 31.1481235278 | 263 | 13 | 1 | 38.4 | TDD | 131 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3272921 | 1 | 121.4661542534 | 31.1534711827 | 116 | 9 | 3 | 35.4 | TDD | 266 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |

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
| 2024-09-20 22:21:31.242 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.263 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.397 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.397 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.094 | NREventA3 | measId:2;ServCellPCI:78;Ser... |
| 2024-09-20 22:21:38.334 | NRHandoverAttempt | SourcePCI:78;SourceNR-ARFCN... |
| 2024-09-20 22:21:38.371 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.385 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.500 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.500 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3272921 | 1 | 16.2398 | 16.8418 | -116.7156 | 10.3346 | 134.9502 | 0.0068 | 0.0013 |
| 2024_09_20 22:00 | 3264310 | 2 | 10.5047 | 6.9442 | -117.9305 | 5.0727 | 155.6462 | 0.0133 | 0.1568 |
| 2024_09_20 22:00 | 3249641 | 3 | 12.2428 | 13.1126 | -117.1535 | 16.0752 | 157.6854 | 0.0005 | 0.0005 |
| 2024_09_20 22:00 | 3260573 | 4 | 8.5836 | 8.9851 | -116.1758 | 18.5457 | 157.6847 | 0.0017 | 0.0116 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412511_829781CD | 504990 | 131 | -89.2 | 504990 | 266 | -84.1 | 504990 | 130 | -83.8 | 504990 | 156 |
| MR_1774412511_CDE38004 | 504990 | 131 | -86.0 | 504990 | 266 | -82.1 | 504990 | 130 | -86.0 | 504990 | 156 |
| MR_1774412511_2656C6D8 | 504990 | 266 | -85.0 | 504990 | 131 | -88.8 | 504990 | 130 | -84.3 | 504990 | 156 |
| MR_1774412511_1717EE2C | 504990 | 131 | -89.2 | 504990 | 266 | -81.7 | 504990 | 130 | -86.5 | 504990 | 156 |
| MR_1774412511_1F32CB59 | 504990 | 131 | -88.6 | 504990 | 266 | -82.9 | 504990 | 130 | -84.8 | 504990 | 156 |
| MR_1774412511_0181A7FF | 504990 | 131 | -86.2 | 504990 | 266 | -85.0 | 504990 | 130 | -83.9 | 504990 | 156 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1199: `e18f5c91-f97...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `e18f5c91-f971-480f-b0ee-234d62d1946b` |
| Tag | **single-answer** |
| 정답 | **C1** |
| C1 의미 | Add neighbor relationship between 3250937_1 and 3259075_2 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1199] topology](images/train_1199.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3250937_1 and 3259075_2 **← 정답**
- `C2`: Check test server and transmission issues
- `C3`: Increase A3 Offset threshold for 3259075_2
- `C4`: Lift the tilt angle of 3250937_1 by 10 degrees
- `C5`: Decrease A3 Offset threshold for 3250937_1
- `C6`: Adjust the azimuth of 3259075_2 by 47 degrees
- `C7`: Decrease A3 Offset threshold for 3259075_2
- `C8`: Press down the tilt angle  of 3259075_2 by 1 degrees
- `C9`: Adjust the azimuth of 3250937_1 by 50 degrees
- `C10`: Increase transmission power for 3259075_2
- `C11`: Increase A3 Offset threshold for 3250937_1
- `C12`: Add neighbor relationship between 3249149_4 and 3259075_2
- `C13`: Decrease transmission power for 3250937_1
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3250937_1
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3250937_1
- `C16`: Increase transmission power for 3250937_1
- `C17`: Insufficient data; more data is needed for judgment.
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3259075_2
- `C19`: Decrease transmission power for 3259075_2
- `C20`: Press down the tilt angle of 3250937_1 by 10 degrees
- `C21`: Lift the tilt angle  of 3259075_2 by 1 degrees
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3259075_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.195 | MS1 | 121.4656730225 | 31.1446283569 | 162 | 504990 | -77.86 | 17.87 | 529.30 | 0.14 | 2.84 | 1587 |
| 2024-09-20 22:21:32.146 | MS1 | 121.4656772976 | 31.1446202111 | 162 | 504990 | -79.16 | 16.38 | 335.09 | 0.15 | 2.18 | 1592 |
| 2024-09-20 22:21:33.500 | MS1 | 121.4656587578 | 31.1446279537 | 162 | 504990 | -75.29 | 13.80 | 548.48 | 0.16 | 2.34 | 1588 |
| 2024-09-20 22:21:34.685 | MS1 | 121.4656685536 | 31.1446351384 | 162 | 504990 | -92.21 | -1.17 | 35.66 | 0.12 | 1.16 | 1594 |
| 2024-09-20 22:21:35.262 | MS1 | 121.4656609519 | 31.1446230874 | 162 | 504990 | -92.34 | -3.58 | 50.80 | 0.10 | 1.06 | 1571 |
| 2024-09-20 22:21:36.672 | MS1 | 121.4656773602 | 31.1446307740 | 162 | 504990 | -88.21 | -2.18 | 34.74 | 0.04 | 1.01 | 1572 |
| 2024-09-20 22:21:37.229 | MS1 | 121.4656756563 | 31.1446240303 | 162 | 504990 | -85.34 | -2.20 | 44.01 | 0.09 | 1.25 | 1570 |
| 2024-09-20 22:21:38.954 | MS1 | 121.4656731160 | 31.1446203770 | 162 | 504990 | -83.83 | 12.76 | 583.54 | 0.06 | 1.11 | 1578 |
| 2024-09-20 22:21:39.297 | MS1 | 121.4656693667 | 31.1446242790 | 162 | 504990 | -81.88 | 16.34 | 407.56 | 0.19 | 1.37 | 1571 |
| 2024-09-20 22:21:40.779 | MS1 | 121.4656666681 | 31.1446205016 | 162 | 504990 | -76.41 | 12.51 | 447.22 | 0.12 | 2.52 | 1575 |
| 2024-09-20 22:21:41.254 | MS1 | 121.4656666730 | 31.1446367042 | 162 | 504990 | -76.78 | 14.06 | 477.11 | 0.16 | 2.73 | 1584 |
| 2024-09-20 22:21:42.111 | MS1 | 121.4656656285 | 31.1446186337 | 162 | 504990 | -83.56 | 16.30 | 507.38 | 0.18 | 2.79 | 1585 |

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
| 3249149 | 4 | 121.4755831077 | 31.1541410422 | 201 | 6 | 4 | 50.0 | TDD | 830 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3250937 | 1 | 121.4756500421 | 31.1448970301 | 209 | 8 | 11 | 47.9 | TDD | 162 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3259075 | 2 | 121.4698694714 | 31.1511628873 | 162 | 0 | 8 | 20.6 | TDD | 602 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3266236 | 3 | 121.4666276107 | 31.1464481722 | 177 | 13 | 12 | 16.5 | TDD | 101 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |

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
| 2024-09-20 22:21:31.039 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.055 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.161 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.161 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.893 | NREventA3 | measId:2;ServCellPCI:949;Se... |
| 2024-09-20 22:21:35.893 | NREventA3 | measId:2;ServCellPCI:949;Se... |
| 2024-09-20 22:21:36.893 | NREventA3 | measId:2;ServCellPCI:949;Se... |
| 2024-09-20 22:21:39.393 | NRRRCReestablishAttempt | PCI:949 |
| 2024-09-20 22:21:39.413 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.424 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:39.547 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.547 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3250937 | 1 | 16.2914 | 13.8225 | -115.0869 | 8.5012 | 135.3858 | 0.0076 | 0.1301 |
| 2024_09_20 22:00 | 3259075 | 2 | 17.0318 | 19.1293 | -114.1209 | 9.2009 | 166.7173 | 0.0105 | 0.0158 |
| 2024_09_20 22:00 | 3266236 | 3 | 9.7433 | 13.9753 | -115.3375 | 13.4510 | 194.5954 | 0.0038 | 0.0038 |
| 2024_09_20 22:00 | 3249149 | 4 | 13.3852 | 16.0185 | -114.9601 | 8.0030 | 112.9962 | 0.0063 | 0.0021 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414008_B6E52234 | 504990 | 602 | -85.3 | 504990 | 162 | -91.2 | 504990 | 830 | -90.1 | 504990 | 101 |
| MR_1774414008_B9E3B486 | 504990 | 602 | -85.6 | 504990 | 162 | -91.4 | 504990 | 830 | -87.3 | 504990 | 101 |
| MR_1774414008_DE816881 | 504990 | 162 | -91.7 | 504990 | 602 | -86.4 | 504990 | 830 | -89.1 | 504990 | 101 |
| MR_1774414008_AE5AB3A1 | 504990 | 602 | -86.3 | 504990 | 162 | -92.8 | 504990 | 830 | -90.1 | 504990 | 101 |
| MR_1774414008_76254AC2 | 504990 | 162 | -92.8 | 504990 | 602 | -86.3 | 504990 | 830 | -89.4 | 504990 | 101 |
| MR_1774414008_AE8BF335 | 504990 | 602 | -87.0 | 504990 | 162 | -91.9 | 504990 | 830 | -87.3 | 504990 | 101 |
| MR_1774414008_5C1C09F5 | 504990 | 602 | -86.2 | 504990 | 162 | -91.4 | 504990 | 830 | -90.7 | 504990 | 101 |
| MR_1774414008_7DB0F066 | 504990 | 602 | -86.2 | 504990 | 162 | -93.2 | 504990 | 830 | -90.4 | 504990 | 101 |

> *... 2개 열 생략 (전체 14열)*

---
