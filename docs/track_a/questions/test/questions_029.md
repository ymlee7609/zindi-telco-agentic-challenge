# Track A 문제 분석 — test[280]~test[289]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/test.json`
> 범위: test[280] ~ test[289] (10개)

## 목차

1. [문제 280: `420fd6bb-9a8...`](#280) — single-answer
2. [문제 281: `7a329918-6f1...`](#281) — single-answer
3. [문제 282: `bd599082-1cc...`](#282) — single-answer
4. [문제 283: `4a04fb6d-c7a...`](#283) — single-answer
5. [문제 284: `43439b12-da9...`](#284) — single-answer
6. [문제 285: `c15fa4f0-2ee...`](#285) — single-answer
7. [문제 286: `ec36924c-70b...`](#286) — single-answer
8. [문제 287: `a25b3802-e90...`](#287) — single-answer
9. [문제 288: `1df0054b-c89...`](#288) — single-answer
10. [문제 289: `47e8b48f-0b3...`](#289) — single-answer

---

### 문제 280: `420fd6bb-9a8...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `420fd6bb-9a8c-451f-9b1a-99971a9aca3b` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[280] topology](images/test_0280.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3237458_3
- `C2`: Increase transmission power for 3237458_3
- `C3`: Decrease A3 Offset threshold for 3237458_3
- `C4`: Add neighbor relationship between 3243848_1 and 3234684_2
- `C5`: Decrease A3 Offset threshold for 3234684_2
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3234684_2
- `C7`: Insufficient data; more data is needed for judgment.
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3237458_3
- `C9`: Press down the tilt angle of 3237458_3 by 10 degrees
- `C10`: Increase A3 Offset threshold for 3234684_2
- `C11`: Adjust the azimuth of 3237458_3 by 50 degrees
- `C12`: Lift the tilt angle  of 3234684_2 by 3 degrees
- `C13`: Lift the tilt angle of 3237458_3 by 10 degrees
- `C14`: Increase A3 Offset threshold for 3237458_3
- `C15`: Add neighbor relationship between 3237458_3 and 3234684_2
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3234684_2
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3237458_3
- `C18`: Decrease transmission power for 3234684_2
- `C19`: Increase transmission power for 3234684_2
- `C20`: Adjust the azimuth of 3234684_2 by 50 degrees
- `C21`: Check test server and transmission issues
- `C22`: Press down the tilt angle  of 3234684_2 by 3 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.698 | MS1 | 121.4656599077 | 31.1446351874 | 243 | 504990 | -79.50 | 16.92 | 417.51 | 0.03 | 2.84 | 1562 |
| 2024-09-20 22:21:32.376 | MS1 | 121.4656719662 | 31.1446351898 | 243 | 504990 | -75.76 | 13.31 | 487.49 | 0.01 | 2.58 | 1571 |
| 2024-09-20 22:21:33.786 | MS1 | 121.4656718936 | 31.1446296143 | 243 | 504990 | -81.54 | 17.56 | 552.64 | 0.17 | 2.96 | 1572 |
| 2024-09-20 22:21:34.345 | MS1 | 121.4656693623 | 31.1446185470 | 243 | 504990 | -92.30 | -3.87 | 53.94 | 0.18 | 1.47 | 1569 |
| 2024-09-20 22:21:35.250 | MS1 | 121.4656752212 | 31.1446309352 | 243 | 504990 | -85.93 | -0.65 | 68.92 | 0.16 | 1.40 | 1589 |
| 2024-09-20 22:21:36.803 | MS1 | 121.4656752044 | 31.1446332824 | 243 | 504990 | -90.67 | -2.57 | 53.61 | 0.17 | 1.37 | 1590 |
| 2024-09-20 22:21:37.966 | MS1 | 121.4656764277 | 31.1446219098 | 243 | 504990 | -87.05 | -3.06 | 64.65 | 0.17 | 1.21 | 1571 |
| 2024-09-20 22:21:38.107 | MS1 | 121.4656675477 | 31.1446184702 | 243 | 504990 | -88.46 | -2.95 | 31.44 | 0.08 | 1.33 | 1572 |
| 2024-09-20 22:21:39.616 | MS1 | 121.4656672949 | 31.1446270987 | 1001 | 504990 | -78.48 | 15.40 | 211.18 | 0.08 | 1.47 | 1568 |
| 2024-09-20 22:21:40.489 | MS1 | 121.4656725161 | 31.1446297715 | 1001 | 504990 | -84.30 | 17.92 | 331.97 | 0.16 | 2.87 | 1579 |
| 2024-09-20 22:21:41.500 | MS1 | 121.4656746216 | 31.1446218991 | 1001 | 504990 | -81.20 | 14.05 | 314.35 | 0.04 | 2.07 | 1567 |
| 2024-09-20 22:21:42.927 | MS1 | 121.4656638330 | 31.1446275532 | 1001 | 504990 | -79.45 | 16.57 | 457.60 | 0.05 | 2.34 | 1595 |

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
| 3216027 | 4 | 121.4695500173 | 31.1531788511 | 356 | 3 | 3 | 42.6 | TDD | 647 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3234684 | 2 | 121.4649571245 | 31.1549691075 | 112 | 2 | 1 | 25.8 | TDD | 1001 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3237458 | 3 | 121.4673013673 | 31.1465435592 | 69 | 11 | 9 | 16.3 | TDD | 243 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3243848 | 1 | 121.4660969835 | 31.1540795723 | 299 | 15 | 7 | 40.9 | TDD | 472 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |

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
| 2024-09-20 22:21:31.449 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.565 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.565 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.235 | NREventA3 | measId:2;ServCellPCI:165;Se... |
| 2024-09-20 22:21:38.475 | NRHandoverAttempt | SourcePCI:165;SourceNR-ARFC... |
| 2024-09-20 22:21:38.512 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.526 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.644 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.644 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3243848 | 1 | 10.5159 | 10.3986 | -117.7143 | 19.8788 | 90.1015 | 0.0093 | 0.0128 |
| 2024_09_20 22:00 | 3234684 | 2 | 14.4700 | 19.3544 | -117.0972 | 10.4885 | 90.5412 | 0.0138 | 0.0075 |
| 2024_09_20 22:00 | 3237458 | 3 | 7.6732 | 5.7221 | -116.5278 | 9.5874 | 184.6005 | 0.0188 | 0.1158 |
| 2024_09_20 22:00 | 3216027 | 4 | 13.6570 | 10.6015 | -115.8418 | 9.7672 | 187.7234 | 0.0148 | 0.0193 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416524_D64C89C5 | 504990 | 243 | -94.2 | 504990 | 1001 | -86.0 | 504990 | 472 | -96.9 | 504990 | 647 |
| MR_1774416524_0F8E3CC1 | 504990 | 243 | -91.5 | 504990 | 1001 | -88.1 | 504990 | 472 | -94.3 | 504990 | 647 |
| MR_1774416524_FEF5AAAD | 504990 | 1001 | -86.8 | 504990 | 243 | -94.2 | 504990 | 472 | -95.7 | 504990 | 647 |
| MR_1774416524_E3C874FF | 504990 | 1001 | -89.1 | 504990 | 243 | -92.6 | 504990 | 472 | -94.2 | 504990 | 647 |
| MR_1774416524_39F9623A | 504990 | 1001 | -87.7 | 504990 | 243 | -92.0 | 504990 | 472 | -97.3 | 504990 | 647 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 281: `7a329918-6f1...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `7a329918-6f13-4794-86f4-12fae9974c61` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[281] topology](images/test_0281.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3225486_2
- `C2`: Adjust the azimuth of 3220403_1 by 7 degrees
- `C3`: Insufficient data; more data is needed for judgment.
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3220403_1
- `C5`: Adjust the azimuth of 3225486_2 by 50 degrees
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3225486_2
- `C7`: Add neighbor relationship between 3220403_1 and 3225486_2
- `C8`: Check test server and transmission issues
- `C9`: Lift the tilt angle of 3220403_1 by 4 degrees
- `C10`: Decrease A3 Offset threshold for 3225486_2
- `C11`: Increase transmission power for 3225486_2
- `C12`: Decrease transmission power for 3225486_2
- `C13`: Increase A3 Offset threshold for 3220403_1
- `C14`: Increase transmission power for 3220403_1
- `C15`: Decrease A3 Offset threshold for 3220403_1
- `C16`: Lift the tilt angle  of 3225486_2 by 10 degrees
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3220403_1
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3225486_2
- `C19`: Press down the tilt angle of 3220403_1 by 4 degrees
- `C20`: Add neighbor relationship between 3239124_4 and 3225486_2
- `C21`: Press down the tilt angle  of 3225486_2 by 10 degrees
- `C22`: Decrease transmission power for 3220403_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.922 | MS1 | 121.4656777981 | 31.1446216908 | 472 | 504990 | -85.03 | 17.32 | 588.51 | 0.18 | 2.76 | 1589 |
| 2024-09-20 22:21:32.684 | MS1 | 121.4656627600 | 31.1446187300 | 472 | 504990 | -85.10 | 12.27 | 388.42 | 0.02 | 2.43 | 1575 |
| 2024-09-20 22:21:33.560 | MS1 | 121.4656766561 | 31.1446292577 | 472 | 504990 | -87.83 | 12.66 | 552.58 | 0.06 | 2.28 | 1570 |
| 2024-09-20 22:21:34.223 | MS1 | 121.4656608653 | 31.1446313854 | 472 | 504990 | -88.17 | 14.73 | 75.71 | 0.51 | 2.28 | 670 |
| 2024-09-20 22:21:35.461 | MS1 | 121.4656698022 | 31.1446221180 | 472 | 504990 | -86.85 | 12.45 | 80.40 | 0.56 | 2.68 | 584 |
| 2024-09-20 22:21:36.944 | MS1 | 121.4656591719 | 31.1446376814 | 472 | 504990 | -88.20 | 16.89 | 101.47 | 0.54 | 2.42 | 617 |
| 2024-09-20 22:21:37.547 | MS1 | 121.4656681210 | 31.1446183609 | 472 | 504990 | -93.56 | 8.23 | 95.48 | 0.58 | 2.78 | 563 |
| 2024-09-20 22:21:38.549 | MS1 | 121.4656644775 | 31.1446220742 | 472 | 504990 | -92.37 | 12.84 | 66.35 | 0.55 | 2.21 | 681 |
| 2024-09-20 22:21:39.437 | MS1 | 121.4656652856 | 31.1446208105 | 472 | 504990 | -93.96 | 10.14 | 56.69 | 0.56 | 2.97 | 656 |
| 2024-09-20 22:21:40.661 | MS1 | 121.4656627351 | 31.1446319971 | 472 | 504990 | -92.47 | 7.74 | 405.68 | 0.06 | 2.76 | 1591 |
| 2024-09-20 22:21:41.361 | MS1 | 121.4656616461 | 31.1446235457 | 472 | 504990 | -91.56 | 9.80 | 462.64 | 0.16 | 2.57 | 1567 |
| 2024-09-20 22:21:42.963 | MS1 | 121.4656599742 | 31.1446274726 | 472 | 504990 | -91.38 | 12.98 | 338.93 | 0.17 | 2.02 | 1577 |

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
| 3213491 | 3 | 121.4724581334 | 31.1483108032 | 112 | 15 | 10 | 45.3 | TDD | 957 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3220403 | 1 | 121.4655926882 | 31.1503455864 | 172 | 0 | 11 | 43.6 | TDD | 472 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3225486 | 2 | 121.4712657289 | 31.1468677373 | 47 | 15 | 8 | 31.6 | TDD | 129 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3239124 | 4 | 121.4660754933 | 31.1474370547 | 23 | 7 | 5 | 40.5 | TDD | 663 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:31.017 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.017 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.688 | NREventA3 | measId:2;ServCellPCI:266;Se... |
| 2024-09-20 22:21:37.928 | NRHandoverAttempt | SourcePCI:266;SourceNR-ARFC... |
| 2024-09-20 22:21:37.976 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.990 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.096 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.096 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3220403 | 1 | 18.7768 | 6.7042 | -114.8205 | 13.1142 | 160.5425 | 0.0167 | 0.0076 |
| 2024_09_20 22:00 | 3225486 | 2 | 16.5517 | 16.1655 | -115.7827 | 18.5516 | 183.3812 | 0.0153 | 0.0125 |
| 2024_09_20 22:00 | 3213491 | 3 | 7.9856 | 9.2155 | -115.3197 | 5.3795 | 140.6261 | 0.0186 | 0.0095 |
| 2024_09_20 22:00 | 3239124 | 4 | 10.5327 | 6.5561 | -115.9987 | 15.5693 | 155.2462 | 0.0076 | 0.0078 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412084_D4DFD00B | 504990 | 472 | -89.3 | 504990 | 129 | -95.7 | 504990 | 663 | -103.0 | 504990 | 957 |
| MR_1774412084_59F7D247 | 504990 | 472 | -87.4 | 504990 | 129 | -95.7 | 504990 | 663 | -102.1 | 504990 | 957 |
| MR_1774412084_885BDED8 | 504990 | 472 | -87.8 | 504990 | 129 | -96.6 | 504990 | 663 | -102.1 | 504990 | 957 |
| MR_1774412084_B71AA187 | 504990 | 472 | -86.8 | 504990 | 129 | -95.0 | 504990 | 663 | -102.4 | 504990 | 957 |
| MR_1774412084_66E4CDFD | 504990 | 472 | -88.6 | 504990 | 129 | -97.7 | 504990 | 663 | -101.8 | 504990 | 957 |
| MR_1774412084_D137BE1B | 504990 | 472 | -89.9 | 504990 | 129 | -96.0 | 504990 | 663 | -104.7 | 504990 | 957 |
| MR_1774412084_024FA1EA | 504990 | 472 | -86.9 | 504990 | 129 | -95.6 | 504990 | 663 | -102.5 | 504990 | 957 |
| MR_1774412084_AC25F8CE | 504990 | 472 | -88.7 | 504990 | 129 | -95.9 | 504990 | 663 | -103.4 | 504990 | 957 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 282: `bd599082-1cc...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `bd599082-1cc1-446e-8f75-5de537220a2e` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[282] topology](images/test_0282.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3260586_1
- `C2`: Add neighbor relationship between 3262471_4 and 3260586_1
- `C3`: Decrease transmission power for 3211041_2
- `C4`: Decrease transmission power for 3260586_1
- `C5`: Increase transmission power for 3260586_1
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3211041_2
- `C7`: Insufficient data; more data is needed for judgment.
- `C8`: Lift the tilt angle of 3211041_2 by 4 degrees
- `C9`: Adjust the azimuth of 3211041_2 by 5 degrees
- `C10`: Press down the tilt angle of 3211041_2 by 4 degrees
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3260586_1
- `C12`: Lift the tilt angle  of 3260586_1 by 10 degrees
- `C13`: Increase transmission power for 3211041_2
- `C14`: Decrease A3 Offset threshold for 3211041_2
- `C15`: Adjust the azimuth of 3260586_1 by 50 degrees
- `C16`: Add neighbor relationship between 3211041_2 and 3260586_1
- `C17`: Increase A3 Offset threshold for 3211041_2
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3260586_1
- `C19`: Decrease A3 Offset threshold for 3260586_1
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3211041_2
- `C21`: Press down the tilt angle  of 3260586_1 by 10 degrees
- `C22`: Check test server and transmission issues

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.798 | MS1 | 121.4656639201 | 31.1446206553 | 615 | 504990 | -86.37 | 14.93 | 348.24 | 0.02 | 2.24 | 1591 |
| 2024-09-20 22:21:32.322 | MS1 | 121.4656592692 | 31.1446362653 | 615 | 504990 | -87.95 | 12.25 | 519.95 | 0.03 | 2.99 | 1579 |
| 2024-09-20 22:21:33.515 | MS1 | 121.4656627148 | 31.1446242107 | 615 | 504990 | -85.20 | 15.93 | 372.99 | 0.16 | 2.37 | 1580 |
| 2024-09-20 22:21:34.130 | MS1 | 121.4656723935 | 31.1446250337 | 615 | 504990 | -87.91 | 17.14 | 56.62 | 0.68 | 2.71 | 621 |
| 2024-09-20 22:21:35.503 | MS1 | 121.4656666234 | 31.1446259579 | 615 | 504990 | -85.82 | 16.94 | 83.72 | 0.64 | 2.49 | 664 |
| 2024-09-20 22:21:36.404 | MS1 | 121.4656760791 | 31.1446295812 | 615 | 504990 | -88.85 | 15.29 | 66.98 | 0.51 | 2.09 | 506 |
| 2024-09-20 22:21:37.404 | MS1 | 121.4656712689 | 31.1446219669 | 615 | 504990 | -89.87 | 8.87 | 93.42 | 0.66 | 2.96 | 622 |
| 2024-09-20 22:21:38.380 | MS1 | 121.4656596012 | 31.1446225825 | 615 | 504990 | -90.74 | 10.60 | 54.89 | 0.65 | 2.50 | 568 |
| 2024-09-20 22:21:39.253 | MS1 | 121.4656604214 | 31.1446351363 | 615 | 504990 | -92.28 | 10.89 | 94.12 | 0.66 | 2.53 | 525 |
| 2024-09-20 22:21:40.444 | MS1 | 121.4656717379 | 31.1446244237 | 615 | 504990 | -89.17 | 8.02 | 384.18 | 0.11 | 2.97 | 1576 |
| 2024-09-20 22:21:41.202 | MS1 | 121.4656722812 | 31.1446344917 | 615 | 504990 | -92.75 | 11.64 | 510.31 | 0.12 | 2.95 | 1588 |
| 2024-09-20 22:21:42.921 | MS1 | 121.4656715724 | 31.1446186771 | 615 | 504990 | -90.14 | 11.27 | 564.65 | 0.18 | 2.23 | 1590 |

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
| 3211041 | 2 | 121.4655993756 | 31.1500192210 | 174 | 2 | 1 | 20.2 | TDD | 615 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3221917 | 3 | 121.4747528707 | 31.1537077357 | 144 | 4 | 7 | 18.5 | TDD | 573 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3260586 | 1 | 121.4655506378 | 31.1458047740 | 347 | 3 | 12 | 35.9 | TDD | 792 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3262471 | 4 | 121.4716235492 | 31.1513927131 | 114 | 3 | 7 | 32.9 | TDD | 456 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:31.339 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.364 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.490 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.490 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.168 | NREventA3 | measId:2;ServCellPCI:100;Se... |
| 2024-09-20 22:21:38.408 | NRHandoverAttempt | SourcePCI:100;SourceNR-ARFC... |
| 2024-09-20 22:21:38.455 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.466 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.611 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.611 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3260586 | 1 | 15.1291 | 18.2943 | -117.0039 | 16.6140 | 139.3994 | 0.0196 | 0.0162 |
| 2024_09_20 22:00 | 3211041 | 2 | 16.6490 | 14.0907 | -116.9264 | 8.2644 | 178.7325 | 0.0039 | 0.0040 |
| 2024_09_20 22:00 | 3221917 | 3 | 16.9281 | 15.8516 | -114.6402 | 10.4626 | 85.8330 | 0.0039 | 0.0109 |
| 2024_09_20 22:00 | 3262471 | 4 | 17.1951 | 8.3563 | -116.8553 | 9.8240 | 155.3697 | 0.0077 | 0.0041 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412935_C968BBD4 | 504990 | 615 | -88.3 | 504990 | 792 | -92.4 | 504990 | 456 | -97.3 | 504990 | 573 |
| MR_1774412935_0C4A3C38 | 504990 | 615 | -89.0 | 504990 | 792 | -91.0 | 504990 | 456 | -97.6 | 504990 | 573 |
| MR_1774412935_BC115669 | 504990 | 615 | -88.7 | 504990 | 792 | -89.7 | 504990 | 456 | -96.4 | 504990 | 573 |
| MR_1774412935_FE76343E | 504990 | 615 | -85.9 | 504990 | 792 | -90.3 | 504990 | 456 | -95.6 | 504990 | 573 |
| MR_1774412935_13E037B7 | 504990 | 615 | -87.9 | 504990 | 792 | -90.7 | 504990 | 456 | -93.7 | 504990 | 573 |
| MR_1774412935_5FCF7911 | 504990 | 615 | -87.1 | 504990 | 792 | -91.8 | 504990 | 456 | -95.1 | 504990 | 573 |
| MR_1774412935_54284784 | 504990 | 615 | -89.5 | 504990 | 792 | -92.2 | 504990 | 456 | -94.1 | 504990 | 573 |
| MR_1774412935_D12A0F68 | 504990 | 615 | -88.1 | 504990 | 792 | -91.7 | 504990 | 456 | -97.2 | 504990 | 573 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 283: `4a04fb6d-c7a...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `4a04fb6d-c7a9-4b67-b69c-8fd4b319e37a` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[283] topology](images/test_0283.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3253302_4
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3277064_1
- `C3`: Increase transmission power for 3277064_1
- `C4`: Increase transmission power for 3253302_4
- `C5`: Add neighbor relationship between 3247933_3 and 3253302_4
- `C6`: Decrease A3 Offset threshold for 3253302_4
- `C7`: Adjust the azimuth of 3277064_1 by 50 degrees
- `C8`: Increase A3 Offset threshold for 3253302_4
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3253302_4
- `C10`: Decrease A3 Offset threshold for 3277064_1
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3253302_4
- `C12`: Add neighbor relationship between 3277064_1 and 3253302_4
- `C13`: Press down the tilt angle  of 3253302_4 by 8 degrees
- `C14`: Press down the tilt angle of 3277064_1 by 5 degrees
- `C15`: Lift the tilt angle  of 3253302_4 by 8 degrees
- `C16`: Check test server and transmission issues
- `C17`: Lift the tilt angle of 3277064_1 by 5 degrees
- `C18`: Insufficient data; more data is needed for judgment.
- `C19`: Increase A3 Offset threshold for 3277064_1
- `C20`: Adjust the azimuth of 3253302_4 by 50 degrees
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3277064_1
- `C22`: Decrease transmission power for 3277064_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.715 | MS1 | 121.4656701090 | 31.1446268355 | 176 | 504990 | -77.62 | 13.72 | 545.90 | 0.16 | 2.21 | 1586 |
| 2024-09-20 22:21:32.581 | MS1 | 121.4656680827 | 31.1446215310 | 176 | 504990 | -81.22 | 12.32 | 600.37 | 0.10 | 2.95 | 1569 |
| 2024-09-20 22:21:33.253 | MS1 | 121.4656769771 | 31.1446206682 | 176 | 504990 | -80.52 | 15.73 | 556.48 | 0.17 | 2.85 | 1592 |
| 2024-09-20 22:21:34.100 | MS1 | 121.4656748046 | 31.1446350014 | 176 | 504990 | -85.28 | -0.47 | 47.76 | 0.18 | 1.37 | 1571 |
| 2024-09-20 22:21:35.486 | MS1 | 121.4656726143 | 31.1446195804 | 176 | 504990 | -92.48 | -2.84 | 50.23 | 0.03 | 1.23 | 1569 |
| 2024-09-20 22:21:36.241 | MS1 | 121.4656654055 | 31.1446322702 | 176 | 504990 | -86.84 | -2.98 | 64.93 | 0.17 | 1.30 | 1565 |
| 2024-09-20 22:21:37.506 | MS1 | 121.4656638837 | 31.1446355152 | 176 | 504990 | -84.88 | -3.92 | 75.83 | 0.11 | 1.49 | 1591 |
| 2024-09-20 22:21:38.308 | MS1 | 121.4656703971 | 31.1446268276 | 176 | 504990 | -88.80 | -2.05 | 78.55 | 0.09 | 1.00 | 1574 |
| 2024-09-20 22:21:39.676 | MS1 | 121.4656727574 | 31.1446275911 | 342 | 504990 | -79.64 | 15.17 | 284.97 | 0.05 | 1.44 | 1592 |
| 2024-09-20 22:21:40.130 | MS1 | 121.4656604482 | 31.1446344740 | 342 | 504990 | -79.85 | 12.39 | 316.72 | 0.02 | 2.55 | 1591 |
| 2024-09-20 22:21:41.530 | MS1 | 121.4656720817 | 31.1446209530 | 342 | 504990 | -78.48 | 16.65 | 595.29 | 0.11 | 2.10 | 1592 |
| 2024-09-20 22:21:42.419 | MS1 | 121.4656741753 | 31.1446236610 | 342 | 504990 | -79.03 | 12.49 | 383.40 | 0.05 | 2.86 | 1600 |

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
| 3247933 | 3 | 121.4677859794 | 31.1461059827 | 157 | 2 | 12 | 26.6 | TDD | 421 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3253302 | 4 | 121.4724706574 | 31.1558281033 | 8 | 7 | 5 | 22.5 | TDD | 342 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3265963 | 2 | 121.4707506351 | 31.1517929716 | 285 | 15 | 9 | 37.7 | TDD | 475 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3277064 | 1 | 121.4641194607 | 31.1524286857 | 222 | 2 | 1 | 46.3 | TDD | 176 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:31.297 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.322 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.447 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.447 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.158 | NREventA3 | measId:2;ServCellPCI:742;Se... |
| 2024-09-20 22:21:38.398 | NRHandoverAttempt | SourcePCI:742;SourceNR-ARFC... |
| 2024-09-20 22:21:38.439 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.451 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.551 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.551 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3277064 | 1 | 15.7208 | 18.1009 | -115.8677 | 17.7488 | 110.7232 | 0.0036 | 0.1175 |
| 2024_09_20 22:00 | 3265963 | 2 | 9.8443 | 15.0778 | -114.4884 | 5.3932 | 179.4172 | 0.0137 | 0.0015 |
| 2024_09_20 22:00 | 3247933 | 3 | 10.1469 | 13.2571 | -115.7158 | 7.5737 | 158.6822 | 0.0079 | 0.0126 |
| 2024_09_20 22:00 | 3253302 | 4 | 5.2919 | 16.6171 | -117.3272 | 9.0656 | 172.7635 | 0.0190 | 0.0061 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415977_7AA73A20 | 504990 | 342 | -80.5 | 504990 | 176 | -83.4 | 504990 | 421 | -83.3 | 504990 | 475 |
| MR_1774415977_D9D639A9 | 504990 | 176 | -85.8 | 504990 | 342 | -80.4 | 504990 | 421 | -85.4 | 504990 | 475 |
| MR_1774415977_0F037A2B | 504990 | 342 | -81.1 | 504990 | 176 | -86.6 | 504990 | 421 | -82.9 | 504990 | 475 |
| MR_1774415977_0B1D57FA | 504990 | 176 | -85.7 | 504990 | 342 | -82.7 | 504990 | 421 | -83.9 | 504990 | 475 |
| MR_1774415977_7EF52F59 | 504990 | 342 | -82.1 | 504990 | 176 | -86.7 | 504990 | 421 | -83.2 | 504990 | 475 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 284: `43439b12-da9...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `43439b12-da9b-4290-ac75-f2ba3cd618ed` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[284] topology](images/test_0284.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3261018_2 by 10 degrees
- `C2`: Decrease A3 Offset threshold for 3273750_1
- `C3`: Lift the tilt angle of 3273750_1 by 5 degrees
- `C4`: Increase transmission power for 3261018_2
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3261018_2
- `C6`: Check test server and transmission issues
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3273750_1
- `C8`: Increase A3 Offset threshold for 3273750_1
- `C9`: Lift the tilt angle  of 3261018_2 by 10 degrees
- `C10`: Decrease transmission power for 3273750_1
- `C11`: Increase A3 Offset threshold for 3261018_2
- `C12`: Add neighbor relationship between 3238057_3 and 3261018_2
- `C13`: Adjust the azimuth of 3261018_2 by 50 degrees
- `C14`: Increase transmission power for 3273750_1
- `C15`: Adjust the azimuth of 3273750_1 by 30 degrees
- `C16`: Press down the tilt angle of 3273750_1 by 5 degrees
- `C17`: Add neighbor relationship between 3273750_1 and 3261018_2
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3273750_1
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3261018_2
- `C20`: Decrease transmission power for 3261018_2
- `C21`: Decrease A3 Offset threshold for 3261018_2
- `C22`: Insufficient data; more data is needed for judgment.

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.728 | MS1 | 121.4656621638 | 31.1446270605 | 746 | 504990 | -87.13 | 15.99 | 346.35 | 0.12 | 2.70 | 1596 |
| 2024-09-20 22:21:32.882 | MS1 | 121.4656692631 | 31.1446271432 | 746 | 504990 | -87.88 | 14.55 | 316.65 | 0.13 | 2.95 | 1565 |
| 2024-09-20 22:21:33.289 | MS1 | 121.4656670624 | 31.1446311445 | 746 | 504990 | -91.53 | 15.21 | 519.14 | 0.08 | 2.92 | 1591 |
| 2024-09-20 22:21:34.778 | MS1 | 121.4656650687 | 31.1446221391 | 746 | 504990 | -86.16 | 15.41 | 69.40 | 0.70 | 2.81 | 586 |
| 2024-09-20 22:21:35.368 | MS1 | 121.4656633307 | 31.1446243225 | 746 | 504990 | -85.89 | 15.18 | 67.36 | 0.67 | 2.37 | 519 |
| 2024-09-20 22:21:36.920 | MS1 | 121.4656651499 | 31.1446237748 | 746 | 504990 | -86.21 | 17.99 | 74.37 | 0.59 | 2.83 | 563 |
| 2024-09-20 22:21:37.935 | MS1 | 121.4656658279 | 31.1446244520 | 746 | 504990 | -93.29 | 8.90 | 87.90 | 0.59 | 2.79 | 574 |
| 2024-09-20 22:21:38.362 | MS1 | 121.4656733402 | 31.1446265539 | 746 | 504990 | -89.87 | 12.94 | 72.46 | 0.55 | 2.80 | 580 |
| 2024-09-20 22:21:39.665 | MS1 | 121.4656686431 | 31.1446269919 | 746 | 504990 | -90.35 | 8.81 | 82.88 | 0.63 | 2.53 | 502 |
| 2024-09-20 22:21:40.480 | MS1 | 121.4656738773 | 31.1446339681 | 746 | 504990 | -89.44 | 12.93 | 356.88 | 0.13 | 2.03 | 1582 |
| 2024-09-20 22:21:41.859 | MS1 | 121.4656631070 | 31.1446326236 | 746 | 504990 | -89.79 | 10.11 | 348.39 | 0.13 | 2.01 | 1573 |
| 2024-09-20 22:21:42.619 | MS1 | 121.4656602869 | 31.1446287961 | 746 | 504990 | -93.93 | 7.19 | 539.47 | 0.02 | 2.37 | 1571 |

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
| 3238057 | 3 | 121.4759884367 | 31.1519699248 | 244 | 12 | 5 | 43.4 | TDD | 76 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3261018 | 2 | 121.4694144762 | 31.1459296654 | 308 | 8 | 10 | 30.6 | TDD | 739 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3267423 | 4 | 121.4648742375 | 31.1504724612 | 98 | 2 | 9 | 37.9 | TDD | 526 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3273750 | 1 | 121.4756388829 | 31.1515660862 | 201 | 3 | 11 | 42.9 | TDD | 746 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |

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
| 2024-09-20 22:21:31.488 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.591 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.591 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.365 | NREventA3 | measId:2;ServCellPCI:648;Se... |
| 2024-09-20 22:21:38.605 | NRHandoverAttempt | SourcePCI:648;SourceNR-ARFC... |
| 2024-09-20 22:21:38.651 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.661 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.795 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.795 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3273750 | 1 | 7.4754 | 11.5859 | -115.8069 | 17.7687 | 192.2466 | 0.0153 | 0.0171 |
| 2024_09_20 22:00 | 3261018 | 2 | 5.3792 | 9.1472 | -117.7828 | 5.4000 | 198.3239 | 0.0147 | 0.0070 |
| 2024_09_20 22:00 | 3238057 | 3 | 6.1038 | 8.2393 | -114.6077 | 12.6300 | 191.6024 | 0.0112 | 0.0163 |
| 2024_09_20 22:00 | 3267423 | 4 | 18.7469 | 13.9311 | -114.0830 | 6.2637 | 82.8992 | 0.0115 | 0.0085 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414952_B3A57A1E | 504990 | 746 | -85.3 | 504990 | 739 | -88.6 | 504990 | 76 | -95.6 | 504990 | 526 |
| MR_1774414952_911EABBE | 504990 | 746 | -87.8 | 504990 | 739 | -88.3 | 504990 | 76 | -95.2 | 504990 | 526 |
| MR_1774414952_02FC272E | 504990 | 746 | -87.0 | 504990 | 739 | -88.2 | 504990 | 76 | -95.4 | 504990 | 526 |
| MR_1774414952_B3B27A83 | 504990 | 746 | -84.6 | 504990 | 739 | -88.0 | 504990 | 76 | -98.3 | 504990 | 526 |
| MR_1774414952_15B02424 | 504990 | 746 | -87.6 | 504990 | 739 | -89.9 | 504990 | 76 | -98.0 | 504990 | 526 |
| MR_1774414952_7397F952 | 504990 | 746 | -87.4 | 504990 | 739 | -88.3 | 504990 | 76 | -95.5 | 504990 | 526 |
| MR_1774414952_7F282B12 | 504990 | 746 | -85.8 | 504990 | 739 | -89.1 | 504990 | 76 | -97.7 | 504990 | 526 |
| MR_1774414952_39B51270 | 504990 | 746 | -88.1 | 504990 | 739 | -88.2 | 504990 | 76 | -96.6 | 504990 | 526 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 285: `c15fa4f0-2ee...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `c15fa4f0-2eef-4195-943c-2f87871a5fca` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[285] topology](images/test_0285.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3220630_1 by 6 degrees
- `C2`: Lift the tilt angle  of 3220109_2 by 6 degrees
- `C3`: Adjust the azimuth of 3220630_1 by 50 degrees
- `C4`: Add neighbor relationship between 3246076_3 and 3220109_2
- `C5`: Decrease transmission power for 3220630_1
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3220630_1
- `C7`: Increase transmission power for 3220109_2
- `C8`: Check test server and transmission issues
- `C9`: Decrease A3 Offset threshold for 3220109_2
- `C10`: Increase A3 Offset threshold for 3220630_1
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3220109_2
- `C12`: Decrease A3 Offset threshold for 3220630_1
- `C13`: Decrease transmission power for 3220109_2
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3220630_1
- `C15`: Add neighbor relationship between 3220630_1 and 3220109_2
- `C16`: Increase transmission power for 3220630_1
- `C17`: Increase A3 Offset threshold for 3220109_2
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3220109_2
- `C19`: Insufficient data; more data is needed for judgment.
- `C20`: Adjust the azimuth of 3220109_2 by 50 degrees
- `C21`: Press down the tilt angle of 3220630_1 by 6 degrees
- `C22`: Press down the tilt angle  of 3220109_2 by 6 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.559 | MS1 | 121.4656774599 | 31.1446346037 | 969 | 504990 | -86.53 | 13.19 | 361.90 | 0.11 | 2.45 | 1571 |
| 2024-09-20 22:21:32.181 | MS1 | 121.4656756321 | 31.1446372930 | 969 | 504990 | -90.33 | 16.36 | 412.90 | 0.13 | 2.60 | 1572 |
| 2024-09-20 22:21:33.683 | MS1 | 121.4656636391 | 31.1446292327 | 969 | 504990 | -86.35 | 15.44 | 588.17 | 0.12 | 2.22 | 1562 |
| 2024-09-20 22:21:34.471 | MS1 | 121.4656613526 | 31.1446353959 | 969 | 504990 | -90.34 | 16.65 | 99.74 | 0.09 | 2.58 | 434 |
| 2024-09-20 22:21:35.801 | MS1 | 121.4656773260 | 31.1446186766 | 969 | 504990 | -89.72 | 16.68 | 55.65 | 0.11 | 2.89 | 463 |
| 2024-09-20 22:21:36.758 | MS1 | 121.4656622236 | 31.1446344862 | 969 | 504990 | -91.06 | 14.07 | 68.67 | 0.17 | 2.09 | 314 |
| 2024-09-20 22:21:37.101 | MS1 | 121.4656689880 | 31.1446231413 | 969 | 504990 | -92.96 | 12.37 | 98.08 | 0.17 | 2.25 | 342 |
| 2024-09-20 22:21:38.466 | MS1 | 121.4656730240 | 31.1446340515 | 969 | 504990 | -90.23 | 12.00 | 87.81 | 0.16 | 2.31 | 356 |
| 2024-09-20 22:21:39.286 | MS1 | 121.4656648473 | 31.1446224061 | 969 | 504990 | -92.44 | 9.90 | 91.15 | 0.13 | 2.77 | 382 |
| 2024-09-20 22:21:40.671 | MS1 | 121.4656612362 | 31.1446283057 | 969 | 504990 | -92.44 | 7.71 | 506.05 | 0.03 | 2.74 | 1581 |
| 2024-09-20 22:21:41.871 | MS1 | 121.4656746789 | 31.1446327053 | 969 | 504990 | -90.69 | 7.25 | 329.49 | 0.18 | 2.03 | 1588 |
| 2024-09-20 22:21:42.863 | MS1 | 121.4656723483 | 31.1446221385 | 969 | 504990 | -91.56 | 7.38 | 556.53 | 0.16 | 2.89 | 1600 |

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
| 3220109 | 2 | 121.4668473924 | 31.1533353350 | 96 | 4 | 7 | 34.0 | TDD | 883 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3220630 | 1 | 121.4675062028 | 31.1548122648 | 297 | 5 | 12 | 24.0 | TDD | 969 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3227210 | 4 | 121.4640263647 | 31.1465412502 | 70 | 6 | 4 | 27.1 | TDD | 591 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3246076 | 3 | 121.4643181308 | 31.1556985778 | 270 | 0 | 3 | 32.8 | TDD | 233 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:31.588 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.604 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.749 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.749 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.437 | NREventA3 | measId:2;ServCellPCI:508;Se... |
| 2024-09-20 22:21:38.677 | NRHandoverAttempt | SourcePCI:508;SourceNR-ARFC... |
| 2024-09-20 22:21:38.721 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.732 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.834 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.834 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3220630 | 1 | 8.6552 | 17.0921 | -115.9372 | 5.3077 | 155.6863 | 0.0150 | 0.0126 |
| 2024_09_20 22:00 | 3220109 | 2 | 6.8064 | 12.9549 | -116.4796 | 11.2282 | 197.4144 | 0.0018 | 0.0124 |
| 2024_09_20 22:00 | 3246076 | 3 | 18.9942 | 13.3535 | -115.1971 | 6.6179 | 89.2592 | 0.0073 | 0.0078 |
| 2024_09_20 22:00 | 3227210 | 4 | 19.1623 | 8.2372 | -115.4003 | 19.3889 | 193.8957 | 0.0135 | 0.0038 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415848_8185C3C4 | 504990 | 969 | -91.9 | 504990 | 883 | -100.3 | 504990 | 233 | -101.7 | 504990 | 591 |
| MR_1774415848_75EA6F68 | 504990 | 969 | -90.8 | 504990 | 883 | -100.0 | 504990 | 233 | -101.2 | 504990 | 591 |
| MR_1774415848_7837AC0A | 504990 | 969 | -89.0 | 504990 | 883 | -99.6 | 504990 | 233 | -100.6 | 504990 | 591 |
| MR_1774415848_3040A9C6 | 504990 | 969 | -91.1 | 504990 | 883 | -99.3 | 504990 | 233 | -100.7 | 504990 | 591 |
| MR_1774415848_5911B919 | 504990 | 969 | -88.8 | 504990 | 883 | -100.0 | 504990 | 233 | -100.8 | 504990 | 591 |
| MR_1774415848_C00FB0D0 | 504990 | 969 | -88.8 | 504990 | 883 | -98.8 | 504990 | 233 | -103.5 | 504990 | 591 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 286: `ec36924c-70b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `ec36924c-70b8-4e2f-8a7c-2db429e886bc` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[286] topology](images/test_0286.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3237181_4
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3237181_4
- `C3`: Adjust the azimuth of 3268594_3 by 27 degrees
- `C4`: Increase A3 Offset threshold for 3237181_4
- `C5`: Decrease A3 Offset threshold for 3268594_3
- `C6`: Lift the tilt angle  of 3237181_4 by 6 degrees
- `C7`: Increase transmission power for 3237181_4
- `C8`: Insufficient data; more data is needed for judgment.
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3237181_4
- `C10`: Decrease transmission power for 3268594_3
- `C11`: Increase A3 Offset threshold for 3268594_3
- `C12`: Adjust the azimuth of 3237181_4 by 50 degrees
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3268594_3
- `C14`: Press down the tilt angle of 3268594_3 by 7 degrees
- `C15`: Decrease A3 Offset threshold for 3237181_4
- `C16`: Press down the tilt angle  of 3237181_4 by 6 degrees
- `C17`: Add neighbor relationship between 3243723_2 and 3237181_4
- `C18`: Check test server and transmission issues
- `C19`: Lift the tilt angle of 3268594_3 by 7 degrees
- `C20`: Add neighbor relationship between 3268594_3 and 3237181_4
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3268594_3
- `C22`: Increase transmission power for 3268594_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.984 | MS1 | 121.4656748584 | 31.1446220656 | 470 | 504990 | -86.03 | 16.24 | 420.11 | 0.01 | 2.16 | 1592 |
| 2024-09-20 22:21:32.579 | MS1 | 121.4656778138 | 31.1446293985 | 470 | 504990 | -90.71 | 17.78 | 602.67 | 0.20 | 2.92 | 1571 |
| 2024-09-20 22:21:33.361 | MS1 | 121.4656680929 | 31.1446317049 | 470 | 504990 | -90.11 | 12.17 | 568.17 | 0.05 | 2.22 | 1598 |
| 2024-09-20 22:21:34.253 | MS1 | 121.4656610388 | 31.1446186076 | 470 | 504990 | -89.42 | 15.76 | 89.09 | 0.04 | 2.43 | 1588 |
| 2024-09-20 22:21:35.854 | MS1 | 121.4656586938 | 31.1446287300 | 470 | 504990 | -86.84 | 13.88 | 83.69 | 0.00 | 2.62 | 1575 |
| 2024-09-20 22:21:36.284 | MS1 | 121.4656762609 | 31.1446326666 | 470 | 504990 | -90.39 | 17.13 | 89.74 | 0.06 | 2.56 | 1572 |
| 2024-09-20 22:21:37.270 | MS1 | 121.4656707989 | 31.1446313792 | 470 | 504990 | -93.64 | 10.69 | 58.53 | 0.13 | 2.81 | 1597 |
| 2024-09-20 22:21:38.116 | MS1 | 121.4656661266 | 31.1446370850 | 470 | 504990 | -92.29 | 11.04 | 82.62 | 0.02 | 2.11 | 1567 |
| 2024-09-20 22:21:39.882 | MS1 | 121.4656647175 | 31.1446366259 | 470 | 504990 | -93.24 | 11.18 | 95.26 | 0.02 | 2.10 | 1584 |
| 2024-09-20 22:21:40.357 | MS1 | 121.4656652967 | 31.1446320437 | 470 | 504990 | -92.40 | 12.65 | 469.93 | 0.20 | 2.47 | 1595 |
| 2024-09-20 22:21:41.900 | MS1 | 121.4656635317 | 31.1446312955 | 470 | 504990 | -90.62 | 8.38 | 368.08 | 0.13 | 2.90 | 1576 |
| 2024-09-20 22:21:42.650 | MS1 | 121.4656745180 | 31.1446262921 | 470 | 504990 | -93.41 | 8.42 | 403.80 | 0.03 | 2.11 | 1582 |

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
| 3237181 | 4 | 121.4746377455 | 31.1445374134 | 346 | 4 | 4 | 34.3 | TDD | 300 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3243723 | 2 | 121.4671749721 | 31.1467178075 | 78 | 3 | 10 | 31.2 | TDD | 412 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3264692 | 1 | 121.4756034560 | 31.1511861203 | 64 | 3 | 12 | 26.1 | TDD | 72 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3268594 | 3 | 121.4720230576 | 31.1555427310 | 179 | 6 | 7 | 17.0 | TDD | 470 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:31.358 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.376 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.477 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.477 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.217 | NREventA3 | measId:2;ServCellPCI:887;Se... |
| 2024-09-20 22:21:38.457 | NRHandoverAttempt | SourcePCI:887;SourceNR-ARFC... |
| 2024-09-20 22:21:38.499 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.511 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.638 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.638 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3264692 | 1 | 76.4895 | 80.0538 | -117.2479 | 9.5861 | 152.1057 | 0.0069 | 0.0064 |
| 2024_09_19 22:00 | 3243723 | 2 | 90.4875 | 80.1815 | -117.8366 | 10.7527 | 174.3901 | 0.0161 | 0.0160 |
| 2024_09_19 22:00 | 3268594 | 3 | 77.0530 | 91.3685 | -114.3606 | 9.7354 | 127.7380 | 0.0197 | 0.0139 |
| 2024_09_19 22:00 | 3237181 | 4 | 87.1091 | 89.6769 | -115.2437 | 9.8687 | 198.4213 | 0.0075 | 0.0099 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412185_B396DAFC | 504990 | 470 | -91.0 | 504990 | 300 | -93.5 | 504990 | 412 | -102.2 | 504990 | 72 |
| MR_1774412185_B74B9E18 | 504990 | 470 | -88.0 | 504990 | 300 | -90.9 | 504990 | 412 | -98.9 | 504990 | 72 |
| MR_1774412185_47E912D7 | 504990 | 470 | -88.2 | 504990 | 300 | -91.0 | 504990 | 412 | -102.3 | 504990 | 72 |
| MR_1774412185_9D4E0292 | 504990 | 470 | -88.2 | 504990 | 300 | -92.0 | 504990 | 412 | -98.5 | 504990 | 72 |
| MR_1774412185_F162C99F | 504990 | 470 | -89.3 | 504990 | 300 | -90.7 | 504990 | 412 | -101.3 | 504990 | 72 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 287: `a25b3802-e90...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `a25b3802-e908-43bb-9c91-43dcf8c24bf2` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[287] topology](images/test_0287.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3259454_1
- `C2`: Increase A3 Offset threshold for 3259454_1
- `C3`: Decrease transmission power for 3259454_1
- `C4`: Lift the tilt angle  of 3216118_2 by 10 degrees
- `C5`: Increase A3 Offset threshold for 3225203_4
- `C6`: Adjust the azimuth of 3216118_2 by 50 degrees
- `C7`: Decrease A3 Offset threshold for 3225203_4
- `C8`: Add neighbor relationship between 3259454_1 and 3225203_4
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3259454_1
- `C10`: Lift the tilt angle of 3259454_1 by 6 degrees
- `C11`: Check test server and transmission issues
- `C12`: Increase transmission power for 3259454_1
- `C13`: Press down the tilt angle  of 3216118_2 by 10 degrees
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3225203_4
- `C15`: Adjust the azimuth of 3259454_1 by 2 degrees
- `C16`: Insufficient data; more data is needed for judgment.
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3225203_4
- `C18`: Press down the tilt angle of 3259454_1 by 6 degrees
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3259454_1
- `C20`: Decrease transmission power for 3225203_4
- `C21`: Add neighbor relationship between 3216118_2 and 3225203_4
- `C22`: Increase transmission power for 3225203_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.983 | MS1 | 121.4656713824 | 31.1446334997 | 176 | 504990 | -89.57 | 13.52 | 521.13 | 0.02 | 2.50 | 1598 |
| 2024-09-20 22:21:32.660 | MS1 | 121.4656778693 | 31.1446294740 | 176 | 504990 | -90.85 | 12.23 | 492.24 | 0.08 | 2.92 | 1597 |
| 2024-09-20 22:21:33.882 | MS1 | 121.4656582606 | 31.1446378499 | 176 | 504990 | -85.51 | 13.06 | 480.90 | 0.12 | 2.92 | 1584 |
| 2024-09-20 22:21:34.626 | MS1 | 121.4656682569 | 31.1446284991 | 176 | 504990 | -87.62 | 17.92 | 100.18 | 0.06 | 2.92 | 1587 |
| 2024-09-20 22:21:35.553 | MS1 | 121.4656637180 | 31.1446295598 | 176 | 504990 | -85.99 | 12.54 | 69.39 | 0.08 | 2.23 | 1579 |
| 2024-09-20 22:21:36.547 | MS1 | 121.4656722077 | 31.1446304162 | 176 | 504990 | -86.21 | 16.28 | 65.73 | 0.15 | 2.49 | 1563 |
| 2024-09-20 22:21:37.643 | MS1 | 121.4656742551 | 31.1446263076 | 176 | 504990 | -92.84 | 7.84 | 93.35 | 0.18 | 2.90 | 1577 |
| 2024-09-20 22:21:38.396 | MS1 | 121.4656673885 | 31.1446316147 | 176 | 504990 | -89.38 | 11.53 | 68.02 | 0.06 | 2.37 | 1591 |
| 2024-09-20 22:21:39.877 | MS1 | 121.4656688156 | 31.1446314219 | 176 | 504990 | -89.80 | 12.83 | 48.34 | 0.09 | 2.40 | 1578 |
| 2024-09-20 22:21:40.254 | MS1 | 121.4656739078 | 31.1446372829 | 176 | 504990 | -92.47 | 7.40 | 347.40 | 0.06 | 2.64 | 1576 |
| 2024-09-20 22:21:41.490 | MS1 | 121.4656699514 | 31.1446194855 | 176 | 504990 | -90.22 | 8.05 | 442.45 | 0.18 | 2.58 | 1569 |
| 2024-09-20 22:21:42.481 | MS1 | 121.4656732620 | 31.1446197928 | 176 | 504990 | -91.40 | 7.74 | 463.44 | 0.14 | 2.57 | 1562 |

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
| 3216118 | 2 | 121.4693054676 | 31.1503414391 | 30 | 11 | 3 | 29.9 | TDD | 554 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3225203 | 4 | 121.4717636932 | 31.1506739846 | 110 | 13 | 4 | 47.7 | TDD | 196 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3259454 | 1 | 121.4699964257 | 31.1494504289 | 216 | 2 | 6 | 45.8 | TDD | 176 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3269980 | 3 | 121.4711175617 | 31.1464980665 | 212 | 12 | 2 | 42.5 | TDD | 560 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |

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
| 2024-09-20 22:21:31.253 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.268 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.375 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.375 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.053 | NREventA3 | measId:2;ServCellPCI:581;Se... |
| 2024-09-20 22:21:38.293 | NRHandoverAttempt | SourcePCI:581;SourceNR-ARFC... |
| 2024-09-20 22:21:38.339 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.350 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.483 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.483 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3259454 | 1 | 79.7781 | 77.3435 | -115.0655 | 6.3882 | 136.5967 | 0.0199 | 0.0117 |
| 2024_09_20 22:00 | 3216118 | 2 | 6.8341 | 15.0054 | -114.7415 | 14.9833 | 125.6064 | 0.0138 | 0.0087 |
| 2024_09_20 22:00 | 3269980 | 3 | 11.3675 | 10.4944 | -115.7789 | 5.3300 | 155.4469 | 0.0075 | 0.0096 |
| 2024_09_20 22:00 | 3225203 | 4 | 14.1639 | 8.2254 | -116.1110 | 6.2543 | 175.8227 | 0.0064 | 0.0037 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413480_0689FBEC | 504990 | 176 | -87.4 | 504990 | 196 | -86.6 | 504990 | 554 | -96.0 | 504990 | 560 |
| MR_1774413480_2A29CFAB | 504990 | 176 | -86.9 | 504990 | 196 | -85.2 | 504990 | 554 | -96.4 | 504990 | 560 |
| MR_1774413480_C4F79AF5 | 504990 | 176 | -87.8 | 504990 | 196 | -85.6 | 504990 | 554 | -95.9 | 504990 | 560 |
| MR_1774413480_D56602FD | 504990 | 176 | -84.8 | 504990 | 196 | -86.9 | 504990 | 554 | -93.3 | 504990 | 560 |
| MR_1774413480_E1F86EDB | 504990 | 176 | -86.0 | 504990 | 196 | -87.0 | 504990 | 554 | -93.6 | 504990 | 560 |
| MR_1774413480_D42698FA | 504990 | 176 | -86.0 | 504990 | 196 | -87.1 | 504990 | 554 | -93.3 | 504990 | 560 |
| MR_1774413480_13766F06 | 504990 | 176 | -87.6 | 504990 | 196 | -85.9 | 504990 | 554 | -94.9 | 504990 | 560 |
| MR_1774413480_6CF010CF | 504990 | 176 | -87.1 | 504990 | 196 | -86.2 | 504990 | 554 | -94.8 | 504990 | 560 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 288: `1df0054b-c89...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `1df0054b-c893-4564-b957-0a359771fa00` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[288] topology](images/test_0288.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3258106_3 by 50 degrees
- `C2`: Increase transmission power for 3258106_3
- `C3`: Decrease A3 Offset threshold for 3253855_4
- `C4`: Decrease transmission power for 3253855_4
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3253855_4
- `C6`: Increase A3 Offset threshold for 3253855_4
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3258106_3
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3258106_3
- `C9`: Increase A3 Offset threshold for 3258106_3
- `C10`: Adjust the azimuth of 3253855_4 by 42 degrees
- `C11`: Decrease transmission power for 3258106_3
- `C12`: Increase transmission power for 3253855_4
- `C13`: Add neighbor relationship between 3266311_1 and 3253855_4
- `C14`: Check test server and transmission issues
- `C15`: Decrease A3 Offset threshold for 3258106_3
- `C16`: Add neighbor relationship between 3258106_3 and 3253855_4
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3253855_4
- `C18`: Press down the tilt angle  of 3253855_4 by 5 degrees
- `C19`: Insufficient data; more data is needed for judgment.
- `C20`: Lift the tilt angle  of 3253855_4 by 5 degrees
- `C21`: Press down the tilt angle of 3258106_3 by 10 degrees
- `C22`: Lift the tilt angle of 3258106_3 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.940 | MS1 | 121.4656768850 | 31.1446225985 | 909 | 504990 | -81.17 | 12.59 | 380.37 | 0.10 | 2.77 | 1568 |
| 2024-09-20 22:21:32.258 | MS1 | 121.4656597489 | 31.1446271510 | 909 | 504990 | -84.90 | 15.35 | 592.36 | 0.13 | 2.22 | 1580 |
| 2024-09-20 22:21:33.293 | MS1 | 121.4656691802 | 31.1446190704 | 909 | 504990 | -78.13 | 12.54 | 314.31 | 0.16 | 2.21 | 1584 |
| 2024-09-20 22:21:34.256 | MS1 | 121.4656752561 | 31.1446338840 | 909 | 504990 | -93.53 | -3.17 | 29.41 | 0.15 | 1.25 | 1572 |
| 2024-09-20 22:21:35.396 | MS1 | 121.4656655172 | 31.1446375481 | 909 | 504990 | -91.70 | -3.72 | 45.81 | 0.12 | 1.17 | 1580 |
| 2024-09-20 22:21:36.901 | MS1 | 121.4656772381 | 31.1446283483 | 909 | 504990 | -88.63 | -1.99 | 60.22 | 0.11 | 1.07 | 1571 |
| 2024-09-20 22:21:37.826 | MS1 | 121.4656678819 | 31.1446335336 | 909 | 504990 | -90.46 | -2.71 | 59.74 | 0.03 | 1.26 | 1575 |
| 2024-09-20 22:21:38.627 | MS1 | 121.4656702193 | 31.1446200987 | 909 | 504990 | -78.91 | 14.97 | 452.49 | 0.14 | 1.39 | 1575 |
| 2024-09-20 22:21:39.731 | MS1 | 121.4656682616 | 31.1446322846 | 909 | 504990 | -75.09 | 14.65 | 561.42 | 0.08 | 1.42 | 1570 |
| 2024-09-20 22:21:40.705 | MS1 | 121.4656689182 | 31.1446309306 | 909 | 504990 | -84.34 | 13.91 | 331.98 | 0.16 | 2.89 | 1596 |
| 2024-09-20 22:21:41.393 | MS1 | 121.4656672308 | 31.1446301451 | 909 | 504990 | -81.62 | 17.48 | 450.37 | 0.09 | 2.73 | 1576 |
| 2024-09-20 22:21:42.943 | MS1 | 121.4656679514 | 31.1446303423 | 909 | 504990 | -80.11 | 17.05 | 339.94 | 0.16 | 2.79 | 1584 |

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
| 3230785 | 2 | 121.4675710613 | 31.1556348135 | 144 | 2 | 8 | 41.4 | TDD | 236 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3253855 | 4 | 121.4694163060 | 31.1521124401 | 245 | 3 | 3 | 37.6 | TDD | 310 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3258106 | 3 | 121.4677080227 | 31.1559536034 | 26 | 13 | 2 | 17.0 | TDD | 909 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3266311 | 1 | 121.4685046386 | 31.1524441152 | 72 | 2 | 8 | 25.1 | TDD | 800 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:31.267 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.282 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.411 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.411 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.106 | NREventA3 | measId:2;ServCellPCI:144;Se... |
| 2024-09-20 22:21:36.106 | NREventA3 | measId:2;ServCellPCI:144;Se... |
| 2024-09-20 22:21:37.106 | NREventA3 | measId:2;ServCellPCI:144;Se... |
| 2024-09-20 22:21:39.606 | NRRRCReestablishAttempt | PCI:144 |
| 2024-09-20 22:21:39.617 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.632 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:39.769 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.769 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3266311 | 1 | 13.4676 | 13.5586 | -114.9772 | 7.3133 | 137.6835 | 0.0086 | 0.0177 |
| 2024_09_20 22:00 | 3230785 | 2 | 17.7204 | 8.2753 | -114.9926 | 16.5815 | 162.1196 | 0.0058 | 0.0099 |
| 2024_09_20 22:00 | 3258106 | 3 | 15.8528 | 5.1366 | -114.6980 | 7.6888 | 129.6170 | 0.0148 | 0.1929 |
| 2024_09_20 22:00 | 3253855 | 4 | 13.7711 | 6.8786 | -114.0721 | 14.0146 | 115.4728 | 0.0058 | 0.0099 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415321_419C3BC7 | 504990 | 909 | -93.3 | 504990 | 310 | -88.4 | 504990 | 800 | -94.5 | 504990 | 236 |
| MR_1774415321_5AF51DAD | 504990 | 909 | -93.3 | 504990 | 310 | -90.4 | 504990 | 800 | -95.3 | 504990 | 236 |
| MR_1774415321_F17F0409 | 504990 | 909 | -93.9 | 504990 | 310 | -91.1 | 504990 | 800 | -95.6 | 504990 | 236 |
| MR_1774415321_07CEB3CA | 504990 | 909 | -95.4 | 504990 | 310 | -89.5 | 504990 | 800 | -94.4 | 504990 | 236 |
| MR_1774415321_7643E713 | 504990 | 909 | -94.7 | 504990 | 310 | -89.6 | 504990 | 800 | -93.8 | 504990 | 236 |
| MR_1774415321_B135DF1F | 504990 | 909 | -93.5 | 504990 | 310 | -90.1 | 504990 | 800 | -93.7 | 504990 | 236 |
| MR_1774415321_EC7CB024 | 504990 | 909 | -93.1 | 504990 | 310 | -88.4 | 504990 | 800 | -92.8 | 504990 | 236 |
| MR_1774415321_EAB36025 | 504990 | 310 | -90.7 | 504990 | 909 | -92.7 | 504990 | 800 | -94.4 | 504990 | 236 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 289: `47e8b48f-0b3...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `47e8b48f-0b30-438c-9333-3796829aae7e` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[289] topology](images/test_0289.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3244466_2
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3257287_1
- `C3`: Adjust the azimuth of 3244466_2 by 5 degrees
- `C4`: Increase transmission power for 3244466_2
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3257287_1
- `C6`: Adjust the azimuth of 3257287_1 by 43 degrees
- `C7`: Lift the tilt angle  of 3244466_2 by 10 degrees
- `C8`: Add neighbor relationship between 3257287_1 and 3244466_2
- `C9`: Decrease transmission power for 3257287_1
- `C10`: Press down the tilt angle of 3257287_1 by 6 degrees
- `C11`: Decrease A3 Offset threshold for 3257287_1
- `C12`: Increase A3 Offset threshold for 3257287_1
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3244466_2
- `C14`: Decrease A3 Offset threshold for 3244466_2
- `C15`: Insufficient data; more data is needed for judgment.
- `C16`: Add neighbor relationship between 3226944_4 and 3244466_2
- `C17`: Check test server and transmission issues
- `C18`: Lift the tilt angle of 3257287_1 by 6 degrees
- `C19`: Decrease transmission power for 3244466_2
- `C20`: Increase transmission power for 3257287_1
- `C21`: Increase A3 Offset threshold for 3244466_2
- `C22`: Press down the tilt angle  of 3244466_2 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.170 | MS1 | 121.4656672376 | 31.1446325232 | 362 | 504990 | -88.43 | 16.28 | 473.77 | 0.09 | 2.27 | 1587 |
| 2024-09-20 22:21:32.541 | MS1 | 121.4656711756 | 31.1446371561 | 362 | 504990 | -90.83 | 14.82 | 451.86 | 0.18 | 2.82 | 1593 |
| 2024-09-20 22:21:33.925 | MS1 | 121.4656757751 | 31.1446227848 | 362 | 504990 | -85.98 | 17.93 | 322.19 | 0.15 | 2.49 | 1584 |
| 2024-09-20 22:21:34.613 | MS1 | 121.4656684529 | 31.1446294292 | 362 | 504990 | -90.67 | 13.90 | 98.68 | 0.19 | 2.43 | 479 |
| 2024-09-20 22:21:35.191 | MS1 | 121.4656713631 | 31.1446246913 | 362 | 504990 | -86.15 | 14.70 | 57.40 | 0.13 | 2.57 | 435 |
| 2024-09-20 22:21:36.624 | MS1 | 121.4656663328 | 31.1446265956 | 362 | 504990 | -85.54 | 13.64 | 102.98 | 0.04 | 2.87 | 422 |
| 2024-09-20 22:21:37.380 | MS1 | 121.4656686379 | 31.1446230568 | 362 | 504990 | -93.02 | 7.60 | 67.00 | 0.10 | 2.38 | 446 |
| 2024-09-20 22:21:38.972 | MS1 | 121.4656741757 | 31.1446244522 | 362 | 504990 | -92.43 | 12.65 | 92.24 | 0.03 | 2.76 | 427 |
| 2024-09-20 22:21:39.358 | MS1 | 121.4656646894 | 31.1446290252 | 362 | 504990 | -91.49 | 10.15 | 70.72 | 0.08 | 2.11 | 433 |
| 2024-09-20 22:21:40.704 | MS1 | 121.4656705447 | 31.1446221625 | 362 | 504990 | -89.11 | 9.82 | 334.48 | 0.19 | 2.54 | 1562 |
| 2024-09-20 22:21:41.151 | MS1 | 121.4656773407 | 31.1446188753 | 362 | 504990 | -93.63 | 10.27 | 416.68 | 0.03 | 2.35 | 1588 |
| 2024-09-20 22:21:42.210 | MS1 | 121.4656700662 | 31.1446351647 | 362 | 504990 | -90.24 | 11.61 | 336.93 | 0.15 | 2.80 | 1581 |

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
| 3226944 | 4 | 121.4713834994 | 31.1526174485 | 325 | 7 | 2 | 18.7 | TDD | 494 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3244466 | 2 | 121.4666437443 | 31.1475053305 | 191 | 5 | 0 | 47.8 | TDD | 306 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3257287 | 1 | 121.4656711565 | 31.1492331380 | 223 | 4 | 8 | 21.2 | TDD | 362 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3275001 | 3 | 121.4759295943 | 31.1511481356 | 3 | 3 | 5 | 31.3 | TDD | 461 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:30.960 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.983 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.119 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.119 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.815 | NREventA3 | measId:2;ServCellPCI:720;Se... |
| 2024-09-20 22:21:38.055 | NRHandoverAttempt | SourcePCI:720;SourceNR-ARFC... |
| 2024-09-20 22:21:38.087 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.099 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.213 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.213 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3257287 | 1 | 9.6447 | 6.7142 | -117.7984 | 16.3989 | 176.7531 | 0.0071 | 0.0069 |
| 2024_09_20 22:00 | 3244466 | 2 | 13.2432 | 9.9335 | -117.5891 | 8.7739 | 138.5576 | 0.0036 | 0.0156 |
| 2024_09_20 22:00 | 3275001 | 3 | 5.9019 | 9.4985 | -115.5115 | 6.5432 | 171.4509 | 0.0200 | 0.0155 |
| 2024_09_20 22:00 | 3226944 | 4 | 19.2565 | 17.8440 | -115.6289 | 5.5525 | 96.6863 | 0.0099 | 0.0022 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414679_33D9B7E7 | 504990 | 362 | -89.8 | 504990 | 306 | -99.5 | 504990 | 494 | -103.3 | 504990 | 461 |
| MR_1774414679_251959EE | 504990 | 362 | -89.4 | 504990 | 306 | -99.4 | 504990 | 494 | -103.8 | 504990 | 461 |
| MR_1774414679_5DCCC384 | 504990 | 362 | -92.5 | 504990 | 306 | -97.4 | 504990 | 494 | -105.6 | 504990 | 461 |
| MR_1774414679_9AC4110F | 504990 | 362 | -88.9 | 504990 | 306 | -98.1 | 504990 | 494 | -102.7 | 504990 | 461 |
| MR_1774414679_C97DAAD6 | 504990 | 362 | -92.6 | 504990 | 306 | -98.4 | 504990 | 494 | -105.2 | 504990 | 461 |
| MR_1774414679_5F482875 | 504990 | 362 | -89.4 | 504990 | 306 | -97.3 | 504990 | 494 | -105.4 | 504990 | 461 |
| MR_1774414679_BC86A5F2 | 504990 | 362 | -90.0 | 504990 | 306 | -97.2 | 504990 | 494 | -105.0 | 504990 | 461 |
| MR_1774414679_937628FE | 504990 | 362 | -89.1 | 504990 | 306 | -97.6 | 504990 | 494 | -105.7 | 504990 | 461 |

> *... 2개 열 생략 (전체 14열)*

---
