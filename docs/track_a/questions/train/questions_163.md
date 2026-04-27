# Track A 문제 분석 — train[1620]~train[1629]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[1620] ~ train[1629] (10개)

## 목차

1. [문제 1620: `e52b9561-bef...`](#1620) — single-answer, 정답: C19
2. [문제 1621: `3d9afb82-8a4...`](#1621) — single-answer, 정답: C10
3. [문제 1622: `8dab3863-ec3...`](#1622) — single-answer, 정답: C15
4. [문제 1623: `66d76d64-468...`](#1623) — single-answer, 정답: C3
5. [문제 1624: `fe5f598a-be8...`](#1624) — single-answer, 정답: C14
6. [문제 1625: `b8b06690-1b6...`](#1625) — single-answer, 정답: C22
7. [문제 1626: `ebee55da-b6c...`](#1626) — single-answer, 정답: C13
8. [문제 1627: `50a17321-e15...`](#1627) — single-answer, 정답: C3
9. [문제 1628: `254d3aca-b4c...`](#1628) — single-answer, 정답: C13
10. [문제 1629: `e866100e-9be...`](#1629) — single-answer, 정답: C11

---

### 문제 1620: `e52b9561-bef...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `e52b9561-bef0-4108-a324-e897ca128683` |
| Tag | **single-answer** |
| 정답 | **C19** |
| C19 의미 | Decrease A3 Offset threshold for 3237380_4 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1620] topology](images/train_1620.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3225673_3 by 28 degrees
- `C2`: Increase A3 Offset threshold for 3237380_4
- `C3`: Press down the tilt angle  of 3225673_3 by 4 degrees
- `C4`: Increase transmission power for 3237380_4
- `C5`: Increase A3 Offset threshold for 3225673_3
- `C6`: Decrease A3 Offset threshold for 3225673_3
- `C7`: Adjust the azimuth of 3237380_4 by 2 degrees
- `C8`: Add neighbor relationship between 3237380_4 and 3225673_3
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3237380_4
- `C10`: Increase transmission power for 3225673_3
- `C11`: Insufficient data; more data is needed for judgment.
- `C12`: Lift the tilt angle  of 3225673_3 by 4 degrees
- `C13`: Lift the tilt angle of 3237380_4 by 10 degrees
- `C14`: Decrease transmission power for 3237380_4
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3237380_4
- `C16`: Decrease transmission power for 3225673_3
- `C17`: Add neighbor relationship between 3213968_2 and 3225673_3
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3225673_3
- `C19`: Decrease A3 Offset threshold for 3237380_4 **← 정답**
- `C20`: Check test server and transmission issues
- `C21`: Press down the tilt angle of 3237380_4 by 10 degrees
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3225673_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.776 | MS1 | 121.4656712381 | 31.1446205307 | 735 | 504990 | -77.78 | 15.48 | 541.37 | 0.13 | 2.02 | 1561 |
| 2024-09-20 22:21:32.150 | MS1 | 121.4656644923 | 31.1446197660 | 735 | 504990 | -78.72 | 14.04 | 344.94 | 0.12 | 2.70 | 1566 |
| 2024-09-20 22:21:33.189 | MS1 | 121.4656650724 | 31.1446225215 | 735 | 504990 | -79.42 | 15.27 | 568.25 | 0.08 | 2.54 | 1576 |
| 2024-09-20 22:21:34.937 | MS1 | 121.4656755641 | 31.1446320135 | 735 | 504990 | -92.27 | -3.40 | 72.83 | 0.08 | 1.21 | 1597 |
| 2024-09-20 22:21:35.786 | MS1 | 121.4656610600 | 31.1446293088 | 735 | 504990 | -83.58 | -2.01 | 52.59 | 0.16 | 1.30 | 1573 |
| 2024-09-20 22:21:36.458 | MS1 | 121.4656723599 | 31.1446219666 | 735 | 504990 | -90.68 | -3.70 | 49.96 | 0.11 | 1.32 | 1564 |
| 2024-09-20 22:21:37.220 | MS1 | 121.4656618372 | 31.1446242368 | 735 | 504990 | -88.99 | -1.70 | 60.75 | 0.16 | 1.14 | 1571 |
| 2024-09-20 22:21:38.152 | MS1 | 121.4656671392 | 31.1446192929 | 735 | 504990 | -89.49 | -0.52 | 78.15 | 0.08 | 1.06 | 1586 |
| 2024-09-20 22:21:39.926 | MS1 | 121.4656747655 | 31.1446356459 | 107 | 504990 | -83.37 | 14.90 | 208.62 | 0.16 | 1.34 | 1599 |
| 2024-09-20 22:21:40.124 | MS1 | 121.4656766977 | 31.1446361437 | 107 | 504990 | -79.58 | 15.07 | 527.37 | 0.03 | 2.72 | 1585 |
| 2024-09-20 22:21:41.154 | MS1 | 121.4656764364 | 31.1446204345 | 107 | 504990 | -78.07 | 15.23 | 304.56 | 0.10 | 2.25 | 1577 |
| 2024-09-20 22:21:42.416 | MS1 | 121.4656635082 | 31.1446293609 | 107 | 504990 | -80.74 | 15.44 | 407.98 | 0.03 | 2.42 | 1560 |

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
| 3213968 | 2 | 121.4757977339 | 31.1454966739 | 84 | 6 | 12 | 45.2 | TDD | 146 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3225673 | 3 | 121.4703169436 | 31.1553265602 | 228 | 2 | 3 | 49.9 | TDD | 107 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3237380 | 4 | 121.4736302608 | 31.1479914624 | 246 | 9 | 5 | 15.4 | TDD | 735 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3277107 | 1 | 121.4673956475 | 31.1502453987 | 128 | 14 | 11 | 35.6 | TDD | 25 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:30.858 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.876 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:30.984 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.984 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.732 | NREventA3 | measId:2;ServCellPCI:873;Se... |
| 2024-09-20 22:21:37.972 | NRHandoverAttempt | SourcePCI:873;SourceNR-ARFC... |
| 2024-09-20 22:21:38.017 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.032 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.159 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.159 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3277107 | 1 | 14.4186 | 16.0559 | -117.9937 | 12.2500 | 133.4589 | 0.0115 | 0.0147 |
| 2024_09_20 22:00 | 3213968 | 2 | 16.5638 | 16.2631 | -114.4303 | 8.7108 | 85.8948 | 0.0126 | 0.0048 |
| 2024_09_20 22:00 | 3225673 | 3 | 18.0489 | 17.2521 | -117.1362 | 6.8861 | 177.5729 | 0.0008 | 0.0013 |
| 2024_09_20 22:00 | 3237380 | 4 | 6.6392 | 17.4277 | -114.3620 | 5.5390 | 173.4278 | 0.0160 | 0.1067 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415589_C54E66BE | 504990 | 107 | -86.1 | 504990 | 735 | -93.8 | 504990 | 146 | -89.4 | 504990 | 25 |
| MR_1774415589_A24735AE | 504990 | 107 | -88.7 | 504990 | 735 | -91.6 | 504990 | 146 | -89.8 | 504990 | 25 |
| MR_1774415589_623200D5 | 504990 | 735 | -91.3 | 504990 | 107 | -88.8 | 504990 | 146 | -89.9 | 504990 | 25 |
| MR_1774415589_9290DA42 | 504990 | 107 | -89.1 | 504990 | 735 | -93.6 | 504990 | 146 | -91.9 | 504990 | 25 |
| MR_1774415589_81759167 | 504990 | 107 | -87.7 | 504990 | 735 | -91.4 | 504990 | 146 | -91.9 | 504990 | 25 |
| MR_1774415589_7337FD99 | 504990 | 107 | -89.0 | 504990 | 735 | -92.9 | 504990 | 146 | -90.7 | 504990 | 25 |
| MR_1774415589_AF92BF7B | 504990 | 735 | -90.3 | 504990 | 107 | -89.0 | 504990 | 146 | -89.3 | 504990 | 25 |
| MR_1774415589_731D77A7 | 504990 | 107 | -86.7 | 504990 | 735 | -93.5 | 504990 | 146 | -89.8 | 504990 | 25 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1621: `3d9afb82-8a4...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `3d9afb82-8a46-4660-bccd-dcc8eac4cb10` |
| Tag | **single-answer** |
| 정답 | **C10** |
| C10 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1621] topology](images/train_1621.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3269001_3
- `C2`: Increase A3 Offset threshold for 3269001_3
- `C3`: Increase transmission power for 3251502_2
- `C4`: Decrease transmission power for 3269001_3
- `C5`: Increase A3 Offset threshold for 3251502_2
- `C6`: Decrease transmission power for 3251502_2
- `C7`: Adjust the azimuth of 3269001_3 by 50 degrees
- `C8`: Adjust the azimuth of 3251502_2 by 50 degrees
- `C9`: Add neighbor relationship between 3261778_1 and 3269001_3
- `C10`: Insufficient data; more data is needed for judgment. **← 정답**
- `C11`: Check test server and transmission issues
- `C12`: Press down the tilt angle of 3251502_2 by 10 degrees
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3269001_3
- `C14`: Lift the tilt angle  of 3269001_3 by 10 degrees
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3269001_3
- `C16`: Add neighbor relationship between 3251502_2 and 3269001_3
- `C17`: Lift the tilt angle of 3251502_2 by 10 degrees
- `C18`: Decrease A3 Offset threshold for 3269001_3
- `C19`: Decrease A3 Offset threshold for 3251502_2
- `C20`: Press down the tilt angle  of 3269001_3 by 10 degrees
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3251502_2
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3251502_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.997 | MS1 | 121.4656659798 | 31.1446367593 | 314 | 504990 | -89.40 | 16.07 | 546.68 | 0.17 | 2.83 | 1567 |
| 2024-09-20 22:21:32.784 | MS1 | 121.4656636520 | 31.1446187596 | 314 | 504990 | -90.29 | 14.42 | 449.66 | 0.18 | 2.96 | 1590 |
| 2024-09-20 22:21:33.173 | MS1 | 121.4656629934 | 31.1446196950 | 314 | 504990 | -87.00 | 17.88 | 495.00 | 0.08 | 2.54 | 1569 |
| 2024-09-20 22:21:34.501 | MS1 | 121.4656639674 | 31.1446285836 | 314 | 504990 | -89.85 | 12.72 | 85.57 | 0.17 | 2.42 | 1577 |
| 2024-09-20 22:21:35.197 | MS1 | 121.4656676871 | 31.1446313418 | 314 | 504990 | -90.03 | 14.99 | 103.73 | 0.00 | 2.54 | 1570 |
| 2024-09-20 22:21:36.683 | MS1 | 121.4656707287 | 31.1446304477 | 314 | 504990 | -85.86 | 16.64 | 67.62 | 0.02 | 2.68 | 1578 |
| 2024-09-20 22:21:37.467 | MS1 | 121.4656624895 | 31.1446361368 | 314 | 504990 | -91.81 | 9.48 | 80.05 | 0.17 | 2.08 | 1567 |
| 2024-09-20 22:21:38.315 | MS1 | 121.4656596166 | 31.1446340764 | 314 | 504990 | -93.87 | 10.27 | 62.65 | 0.16 | 2.03 | 1581 |
| 2024-09-20 22:21:39.499 | MS1 | 121.4656610954 | 31.1446255591 | 314 | 504990 | -90.43 | 10.70 | 54.25 | 0.19 | 2.34 | 1569 |
| 2024-09-20 22:21:40.926 | MS1 | 121.4656620078 | 31.1446287563 | 314 | 504990 | -91.24 | 8.00 | 499.72 | 0.04 | 2.20 | 1591 |
| 2024-09-20 22:21:41.260 | MS1 | 121.4656680333 | 31.1446188427 | 314 | 504990 | -92.29 | 7.13 | 541.85 | 0.10 | 2.86 | 1562 |
| 2024-09-20 22:21:42.375 | MS1 | 121.4656608037 | 31.1446316560 | 314 | 504990 | -93.63 | 10.33 | 446.29 | 0.09 | 2.98 | 1572 |

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
| 3219429 | 4 | 121.4682596093 | 31.1533139659 | 324 | 2 | 1 | 45.1 | TDD | 571 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3251502 | 2 | 121.4692383744 | 31.1516448968 | 113 | 11 | 2 | 21.3 | TDD | 314 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3261778 | 1 | 121.4641807103 | 31.1555032090 | 60 | 13 | 7 | 45.8 | TDD | 337 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3269001 | 3 | 121.4640516654 | 31.1449167650 | 286 | 13 | 9 | 48.6 | TDD | 691 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |

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
| 2024-09-20 22:21:31.538 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.561 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.694 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.694 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.352 | NREventA3 | measId:2;ServCellPCI:472;Se... |
| 2024-09-20 22:21:38.592 | NRHandoverAttempt | SourcePCI:472;SourceNR-ARFC... |
| 2024-09-20 22:21:38.637 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.648 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.760 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.760 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3261778 | 1 | 92.9672 | 87.8759 | -115.8609 | 15.8761 | 159.4639 | 0.0189 | 0.0000 |
| 2024_09_19 22:00 | 3251502 | 2 | 89.7799 | 89.6928 | -117.4054 | 7.6650 | 181.7145 | 0.0143 | 0.0090 |
| 2024_09_19 22:00 | 3269001 | 3 | 82.3198 | 89.4395 | -115.5746 | 5.8560 | 86.5665 | 0.0177 | 0.0089 |
| 2024_09_19 22:00 | 3219429 | 4 | 82.2741 | 94.1867 | -117.2328 | 13.4280 | 128.6521 | 0.0178 | 0.0032 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414303_EA30C883 | 504990 | 314 | -89.5 | 504990 | 691 | -89.6 | 504990 | 337 | -98.9 | 504990 | 571 |
| MR_1774414303_338BC057 | 504990 | 314 | -91.6 | 504990 | 691 | -88.3 | 504990 | 337 | -101.9 | 504990 | 571 |
| MR_1774414303_27182E48 | 504990 | 314 | -90.4 | 504990 | 691 | -91.6 | 504990 | 337 | -101.6 | 504990 | 571 |
| MR_1774414303_4335503C | 504990 | 314 | -89.1 | 504990 | 691 | -88.4 | 504990 | 337 | -101.7 | 504990 | 571 |
| MR_1774414303_83030585 | 504990 | 314 | -89.6 | 504990 | 691 | -88.9 | 504990 | 337 | -102.3 | 504990 | 571 |
| MR_1774414303_F7C0B05B | 504990 | 314 | -91.3 | 504990 | 691 | -90.9 | 504990 | 337 | -99.4 | 504990 | 571 |
| MR_1774414303_80C43C85 | 504990 | 314 | -88.1 | 504990 | 691 | -90.6 | 504990 | 337 | -101.8 | 504990 | 571 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1622: `8dab3863-ec3...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `8dab3863-ec3b-4102-8e5e-cd8d0520fb71` |
| Tag | **single-answer** |
| 정답 | **C15** |
| C15 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1622] topology](images/train_1622.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3257818_2
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3257818_2
- `C3`: Lift the tilt angle of 3232513_1 by 4 degrees
- `C4`: Increase transmission power for 3232513_1
- `C5`: Press down the tilt angle of 3232513_1 by 4 degrees
- `C6`: Decrease A3 Offset threshold for 3232513_1
- `C7`: Press down the tilt angle  of 3257818_2 by 10 degrees
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3257818_2
- `C9`: Decrease A3 Offset threshold for 3257818_2
- `C10`: Add neighbor relationship between 3233892_3 and 3257818_2
- `C11`: Increase transmission power for 3257818_2
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3232513_1
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3232513_1
- `C14`: Decrease transmission power for 3232513_1
- `C15`: Check test server and transmission issues **← 정답**
- `C16`: Increase A3 Offset threshold for 3232513_1
- `C17`: Increase A3 Offset threshold for 3257818_2
- `C18`: Add neighbor relationship between 3232513_1 and 3257818_2
- `C19`: Adjust the azimuth of 3232513_1 by 50 degrees
- `C20`: Adjust the azimuth of 3257818_2 by 50 degrees
- `C21`: Insufficient data; more data is needed for judgment.
- `C22`: Lift the tilt angle  of 3257818_2 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.488 | MS1 | 121.4656740437 | 31.1446223726 | 130 | 504990 | -87.30 | 17.94 | 429.75 | 0.11 | 2.81 | 1583 |
| 2024-09-20 22:21:32.742 | MS1 | 121.4656759696 | 31.1446361306 | 130 | 504990 | -88.51 | 16.63 | 310.01 | 0.03 | 2.77 | 1578 |
| 2024-09-20 22:21:33.702 | MS1 | 121.4656713020 | 31.1446328441 | 130 | 504990 | -89.75 | 16.18 | 542.85 | 0.18 | 2.16 | 1569 |
| 2024-09-20 22:21:34.447 | MS1 | 121.4656633877 | 31.1446282967 | 130 | 504990 | -89.45 | 14.94 | 102.03 | 0.02 | 2.55 | 436 |
| 2024-09-20 22:21:35.751 | MS1 | 121.4656614544 | 31.1446253158 | 130 | 504990 | -91.93 | 15.87 | 90.66 | 0.07 | 2.68 | 418 |
| 2024-09-20 22:21:36.297 | MS1 | 121.4656769244 | 31.1446185168 | 130 | 504990 | -85.44 | 16.23 | 79.84 | 0.15 | 2.32 | 432 |
| 2024-09-20 22:21:37.215 | MS1 | 121.4656720079 | 31.1446183888 | 130 | 504990 | -92.76 | 12.49 | 53.46 | 0.09 | 2.41 | 387 |
| 2024-09-20 22:21:38.304 | MS1 | 121.4656696215 | 31.1446249167 | 130 | 504990 | -93.08 | 10.32 | 53.08 | 0.19 | 2.20 | 424 |
| 2024-09-20 22:21:39.910 | MS1 | 121.4656595844 | 31.1446360790 | 130 | 504990 | -90.34 | 12.50 | 61.01 | 0.20 | 2.71 | 433 |
| 2024-09-20 22:21:40.638 | MS1 | 121.4656739602 | 31.1446363392 | 130 | 504990 | -92.40 | 12.02 | 340.41 | 0.17 | 2.90 | 1591 |
| 2024-09-20 22:21:41.524 | MS1 | 121.4656637238 | 31.1446348010 | 130 | 504990 | -93.54 | 9.08 | 427.82 | 0.20 | 2.90 | 1565 |
| 2024-09-20 22:21:42.394 | MS1 | 121.4656669815 | 31.1446287309 | 130 | 504990 | -91.38 | 11.34 | 420.47 | 0.05 | 2.57 | 1569 |

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
| 3232513 | 1 | 121.4756129027 | 31.1489133036 | 98 | 2 | 0 | 40.4 | TDD | 130 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3233892 | 3 | 121.4689622070 | 31.1547549077 | 101 | 1 | 4 | 18.3 | TDD | 213 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3252781 | 4 | 121.4748891968 | 31.1559790170 | 278 | 13 | 5 | 47.5 | TDD | 92 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3257818 | 2 | 121.4719331674 | 31.1445121123 | 8 | 11 | 4 | 19.6 | TDD | 996 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:30.884 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.024 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.024 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.738 | NREventA3 | measId:2;ServCellPCI:731;Se... |
| 2024-09-20 22:21:37.978 | NRHandoverAttempt | SourcePCI:731;SourceNR-ARFC... |
| 2024-09-20 22:21:38.025 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.037 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.166 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.166 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3232513 | 1 | 13.9985 | 14.8673 | -114.4303 | 16.6288 | 166.1384 | 0.0184 | 0.0089 |
| 2024_09_20 22:00 | 3257818 | 2 | 14.2846 | 6.6125 | -117.2283 | 13.5716 | 163.5449 | 0.0134 | 0.0081 |
| 2024_09_20 22:00 | 3233892 | 3 | 7.6241 | 13.6203 | -114.2401 | 13.3883 | 136.9674 | 0.0053 | 0.0095 |
| 2024_09_20 22:00 | 3252781 | 4 | 14.0542 | 18.2775 | -115.6866 | 18.0720 | 182.0133 | 0.0025 | 0.0028 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415551_FE18C231 | 504990 | 130 | -93.5 | 504990 | 996 | -91.1 | 504990 | 213 | -101.2 | 504990 | 92 |
| MR_1774415551_9A10EC70 | 504990 | 130 | -93.6 | 504990 | 996 | -93.8 | 504990 | 213 | -102.4 | 504990 | 92 |
| MR_1774415551_DFE57E3A | 504990 | 130 | -93.3 | 504990 | 996 | -91.4 | 504990 | 213 | -100.7 | 504990 | 92 |
| MR_1774415551_D0E6D289 | 504990 | 130 | -91.3 | 504990 | 996 | -92.6 | 504990 | 213 | -100.4 | 504990 | 92 |
| MR_1774415551_8205D97A | 504990 | 130 | -93.9 | 504990 | 996 | -94.2 | 504990 | 213 | -101.4 | 504990 | 92 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1623: `66d76d64-468...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `66d76d64-4681-4a9f-a11f-1b26d5be5add` |
| Tag | **single-answer** |
| 정답 | **C3** |
| C3 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1623] topology](images/train_1623.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3265408_2 by 50 degrees
- `C2`: Adjust the azimuth of 3257290_4 by 50 degrees
- `C3`: Check test server and transmission issues **← 정답**
- `C4`: Decrease transmission power for 3265408_2
- `C5`: Decrease A3 Offset threshold for 3257290_4
- `C6`: Insufficient data; more data is needed for judgment.
- `C7`: Decrease transmission power for 3257290_4
- `C8`: Lift the tilt angle  of 3257290_4 by 10 degrees
- `C9`: Increase transmission power for 3265408_2
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3257290_4
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3257290_4
- `C12`: Add neighbor relationship between 3244052_1 and 3257290_4
- `C13`: Press down the tilt angle of 3265408_2 by 7 degrees
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3265408_2
- `C15`: Decrease A3 Offset threshold for 3265408_2
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3265408_2
- `C17`: Increase A3 Offset threshold for 3257290_4
- `C18`: Lift the tilt angle of 3265408_2 by 7 degrees
- `C19`: Increase A3 Offset threshold for 3265408_2
- `C20`: Add neighbor relationship between 3265408_2 and 3257290_4
- `C21`: Increase transmission power for 3257290_4
- `C22`: Press down the tilt angle  of 3257290_4 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.542 | MS1 | 121.4656614335 | 31.1446371468 | 625 | 504990 | -85.56 | 13.22 | 566.56 | 0.04 | 2.95 | 1598 |
| 2024-09-20 22:21:32.133 | MS1 | 121.4656688092 | 31.1446340201 | 625 | 504990 | -85.87 | 12.84 | 496.56 | 0.08 | 2.42 | 1564 |
| 2024-09-20 22:21:33.247 | MS1 | 121.4656718047 | 31.1446313549 | 625 | 504990 | -85.08 | 12.64 | 589.52 | 0.05 | 2.13 | 1585 |
| 2024-09-20 22:21:34.884 | MS1 | 121.4656677258 | 31.1446264309 | 625 | 504990 | -85.90 | 14.87 | 58.72 | 0.03 | 2.64 | 458 |
| 2024-09-20 22:21:35.441 | MS1 | 121.4656639772 | 31.1446180820 | 625 | 504990 | -89.08 | 12.04 | 62.79 | 0.15 | 2.76 | 473 |
| 2024-09-20 22:21:36.315 | MS1 | 121.4656624552 | 31.1446368248 | 625 | 504990 | -88.64 | 16.94 | 54.34 | 0.10 | 2.99 | 417 |
| 2024-09-20 22:21:37.116 | MS1 | 121.4656688227 | 31.1446379929 | 625 | 504990 | -91.38 | 7.39 | 76.15 | 0.05 | 2.77 | 455 |
| 2024-09-20 22:21:38.974 | MS1 | 121.4656627254 | 31.1446302032 | 625 | 504990 | -92.93 | 9.49 | 77.21 | 0.04 | 2.73 | 450 |
| 2024-09-20 22:21:39.818 | MS1 | 121.4656652976 | 31.1446298488 | 625 | 504990 | -91.02 | 9.39 | 63.92 | 0.05 | 2.04 | 328 |
| 2024-09-20 22:21:40.143 | MS1 | 121.4656658344 | 31.1446303781 | 625 | 504990 | -91.91 | 8.91 | 394.54 | 0.02 | 2.31 | 1580 |
| 2024-09-20 22:21:41.745 | MS1 | 121.4656620863 | 31.1446310676 | 625 | 504990 | -93.04 | 9.81 | 343.80 | 0.16 | 2.05 | 1561 |
| 2024-09-20 22:21:42.397 | MS1 | 121.4656742898 | 31.1446290122 | 625 | 504990 | -91.69 | 10.39 | 528.62 | 0.14 | 2.22 | 1586 |

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
| 3244052 | 1 | 121.4753202842 | 31.1477224606 | 13 | 7 | 7 | 41.6 | TDD | 520 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3257290 | 4 | 121.4691306629 | 31.1461277288 | 115 | 14 | 4 | 48.0 | TDD | 766 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3259113 | 3 | 121.4752933991 | 31.1441092874 | 215 | 5 | 0 | 19.3 | TDD | 868 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3265408 | 2 | 121.4722384290 | 31.1446047129 | 72 | 3 | 7 | 44.1 | TDD | 625 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |

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
| 2024-09-20 22:21:30.999 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.020 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.133 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.133 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.801 | NREventA3 | measId:2;ServCellPCI:308;Se... |
| 2024-09-20 22:21:38.041 | NRHandoverAttempt | SourcePCI:308;SourceNR-ARFC... |
| 2024-09-20 22:21:38.076 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.090 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.224 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.224 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3244052 | 1 | 7.0213 | 8.3228 | -115.5312 | 15.5594 | 156.2875 | 0.0131 | 0.0024 |
| 2024_09_20 22:00 | 3265408 | 2 | 9.4432 | 5.3418 | -117.9027 | 5.9016 | 173.6772 | 0.0047 | 0.0136 |
| 2024_09_20 22:00 | 3259113 | 3 | 12.4396 | 16.5475 | -116.7679 | 10.4594 | 106.5990 | 0.0100 | 0.0169 |
| 2024_09_20 22:00 | 3257290 | 4 | 13.1210 | 10.3875 | -115.0642 | 5.7724 | 141.9225 | 0.0186 | 0.0163 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413406_41CA721D | 504990 | 625 | -86.6 | 504990 | 766 | -93.3 | 504990 | 520 | -93.4 | 504990 | 868 |
| MR_1774413406_A02787C3 | 504990 | 625 | -87.3 | 504990 | 766 | -91.0 | 504990 | 520 | -95.2 | 504990 | 868 |
| MR_1774413406_9A5F3DA7 | 504990 | 625 | -86.5 | 504990 | 766 | -93.3 | 504990 | 520 | -94.1 | 504990 | 868 |
| MR_1774413406_25E0A224 | 504990 | 625 | -85.2 | 504990 | 766 | -91.4 | 504990 | 520 | -95.0 | 504990 | 868 |
| MR_1774413406_F891445A | 504990 | 625 | -86.7 | 504990 | 766 | -90.8 | 504990 | 520 | -92.4 | 504990 | 868 |
| MR_1774413406_58A24BA1 | 504990 | 625 | -84.8 | 504990 | 766 | -93.1 | 504990 | 520 | -93.4 | 504990 | 868 |
| MR_1774413406_6A54BDF1 | 504990 | 625 | -84.9 | 504990 | 766 | -92.3 | 504990 | 520 | -93.3 | 504990 | 868 |
| MR_1774413406_593153A6 | 504990 | 625 | -87.0 | 504990 | 766 | -91.3 | 504990 | 520 | -92.0 | 504990 | 868 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1624: `fe5f598a-be8...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `fe5f598a-be8d-48fb-ac7c-4936fb8724c0` |
| Tag | **single-answer** |
| 정답 | **C14** |
| C14 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3238799_3 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1624] topology](images/train_1624.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3238799_3
- `C2`: Press down the tilt angle  of 3239927_6 by 0 degrees
- `C3`: Check test server and transmission issues
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3239927_6
- `C5`: Add neighbor relationship between 3238799_3 and 3239927_6
- `C6`: Add neighbor relationship between 3251376_10 and 3239927_6
- `C7`: Decrease A3 Offset threshold for 3239927_6
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3239927_6
- `C9`: Lift the tilt angle of 3238799_3 by 2 degrees
- `C10`: Lift the tilt angle  of 3239927_6 by 0 degrees
- `C11`: Press down the tilt angle of 3238799_3 by 2 degrees
- `C12`: Increase A3 Offset threshold for 3238799_3
- `C13`: Adjust the azimuth of 3239927_6 by 12 degrees
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3238799_3 **← 정답**
- `C15`: Decrease A3 Offset threshold for 3238799_3
- `C16`: Decrease transmission power for 3238799_3
- `C17`: Insufficient data; more data is needed for judgment.
- `C18`: Adjust the azimuth of 3238799_3 by 30 degrees
- `C19`: Increase transmission power for 3239927_6
- `C20`: Decrease transmission power for 3239927_6
- `C21`: Increase A3 Offset threshold for 3239927_6
- `C22`: Increase transmission power for 3238799_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.121 | MS1 | 121.4656712996 | 31.1446247909 | 559 | 504990 | -93.03 | 14.80 | 369.59 | 0.01 | 2.78 | 1572 |
| 2024-09-20 22:21:32.722 | MS1 | 121.4656704153 | 31.1446194767 | 7 | 504990 | -93.36 | 10.66 | 471.28 | 0.02 | 2.96 | 1561 |
| 2024-09-20 22:21:33.582 | MS1 | 121.4656592220 | 31.1446339489 | 730 | 504990 | -94.45 | 11.52 | 424.03 | 0.13 | 2.55 | 1569 |
| 2024-09-20 22:21:34.113 | MS1 | 121.4656636252 | 31.1446296300 | 902 | 152650 | -89.33 | 7.98 | 74.36 | 0.04 | 1.90 | 912 |
| 2024-09-20 22:21:35.611 | MS1 | 121.4656636539 | 31.1446274335 | 774 | 152650 | -87.60 | 6.15 | 60.03 | 0.19 | 1.70 | 996 |
| 2024-09-20 22:21:36.960 | MS1 | 121.4656743244 | 31.1446358570 | 16 | 152650 | -88.39 | 6.40 | 94.28 | 0.13 | 1.70 | 928 |
| 2024-09-20 22:21:37.575 | MS1 | 121.4656622397 | 31.1446268928 | 433 | 152650 | -93.18 | 7.13 | 86.06 | 0.04 | 1.77 | 943 |
| 2024-09-20 22:21:38.257 | MS1 | 121.4656722655 | 31.1446371190 | 902 | 152650 | -89.62 | 4.30 | 105.17 | 0.02 | 1.86 | 977 |
| 2024-09-20 22:21:39.244 | MS1 | 121.4656703318 | 31.1446354680 | 774 | 152650 | -89.94 | 2.60 | 59.53 | 0.02 | 1.72 | 932 |
| 2024-09-20 22:21:40.605 | MS1 | 121.4656711365 | 31.1446362364 | 16 | 152650 | -89.93 | 3.01 | 74.41 | 0.14 | 2.89 | 1588 |
| 2024-09-20 22:21:41.186 | MS1 | 121.4656721706 | 31.1446207458 | 433 | 152650 | -90.26 | 3.03 | 74.78 | 0.05 | 2.02 | 1592 |
| 2024-09-20 22:21:42.783 | MS1 | 121.4656777795 | 31.1446246616 | 902 | 152650 | -95.76 | 3.11 | 89.58 | 0.15 | 2.76 | 1563 |

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
| 3212774 | 13 | 121.4702710390 | 31.1516102740 | 36 | 10 | 10 | 11.1 | FDD | 820 | n1 | 152650 | 30M | 4T4R | 24 | 152650 |
| 3217143 | 2 | 121.4707461786 | 31.1444246579 | 63 | 5 | 7 | 21.1 | TDD | 7 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3224176 | 4 | 121.4697927211 | 31.1442245466 | 290 | 13 | 6 | 23.3 | TDD | 851 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3228853 | 7 | 121.4729150133 | 31.1527391660 | 252 | 0 | 3 | 6.2 | FDD | 193 | n1 | 152650 | 30M | 4T4R | 13 | 152650 |
| 3238283 | 5 | 121.4750265553 | 31.1543924384 | 252 | 14 | 9 | 21.3 | TDD | 730 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3238799 | 3 | 121.4742765263 | 31.1549730555 | 185 | 1 | 10 | 26.1 | TDD | 559 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3239927 | 6 | 121.4652651543 | 31.1535293638 | 166 | 0 | 3 | 5.1 | TDD | 380 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3241504 | 12 | 121.4675328602 | 31.1517975556 | 186 | 2 | 1 | 10.4 | FDD | 977 | n1 | 152650 | 30M | 4T4R | 13 | 152650 |
| 3247099 | 9 | 121.4743677876 | 31.1455530407 | 226 | 2 | 1 | 9.0 | FDD | 774 | n1 | 152650 | 30M | 4T4R | 10 | 152650 |
| 3251376 | 10 | 121.4720639993 | 31.1447649572 | 346 | 2 | 10 | 0.4 | FDD | 16 | n1 | 152650 | 30M | 4T4R | 12 | 152650 |
| 3258666 | 8 | 121.4696416106 | 31.1557735741 | 214 | 9 | 10 | 4.3 | FDD | 902 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |
| 3276818 | 1 | 121.4692137979 | 31.1443373649 | 17 | 7 | 1 | 16.6 | TDD | 768 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3277343 | 11 | 121.4753600375 | 31.1515110671 | 164 | 0 | 1 | 2.3 | FDD | 433 | n1 | 152650 | 30M | 4T4R | 23 | 152650 |

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
| 2024-09-20 22:21:31.293 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.314 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.436 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.436 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.099 | NREventA2 | measId:1;ServCellPCI:670;Se... |
| 2024-09-20 22:21:35.210 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.446 | NREventA5 | measId:3;ServCellPCI:670;Se... |
| 2024-09-20 22:21:35.523 | NRHandoverAttempt | SourcePCI:670;SourceNR-ARFC... |
| 2024-09-20 22:21:35.565 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.579 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:35.682 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.682 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3276818 | 1 | 8.7406 | 12.9933 | -116.8058 | 11.8017 | 196.8477 | 0.0148 | 0.0158 |
| 2024_09_20 22:00 | 3217143 | 2 | 16.6041 | 18.6211 | -117.9024 | 9.8853 | 98.2136 | 0.0172 | 0.0154 |
| 2024_09_20 22:00 | 3238799 | 3 | 7.3236 | 8.3905 | -116.0757 | 18.2398 | 184.3673 | 0.0003 | 0.0197 |
| 2024_09_20 22:00 | 3224176 | 4 | 14.3235 | 11.1410 | -114.3326 | 9.8328 | 104.7642 | 0.0062 | 0.0144 |
| 2024_09_20 22:00 | 3238283 | 5 | 19.8886 | 17.7191 | -117.7832 | 16.1636 | 83.2519 | 0.0006 | 0.0145 |
| 2024_09_20 22:00 | 3239927 | 6 | 7.2107 | 9.9479 | -114.8063 | 15.6602 | 121.7259 | 0.0005 | 0.0194 |
| 2024_09_20 22:00 | 3228853 | 7 | 17.4138 | 13.0421 | -117.4771 | 3.6431 | 32.5851 | 0.0114 | 0.0005 |
| 2024_09_20 22:00 | 3258666 | 8 | 18.9000 | 12.6880 | -117.8558 | 3.0052 | 53.1651 | 0.0156 | 0.0175 |
| 2024_09_20 22:00 | 3247099 | 9 | 14.9090 | 11.0508 | -116.6412 | 4.2720 | 35.7319 | 0.0132 | 0.0066 |
| 2024_09_20 22:00 | 3251376 | 10 | 12.8803 | 18.9117 | -116.7147 | 3.3131 | 48.5099 | 0.0018 | 0.0169 |
| 2024_09_20 22:00 | 3277343 | 11 | 15.1765 | 16.1478 | -116.1339 | 4.5963 | 40.2485 | 0.0033 | 0.0013 |
| 2024_09_20 22:00 | 3241504 | 12 | 11.5798 | 11.3058 | -114.1953 | 3.6823 | 39.5171 | 0.0183 | 0.0116 |
| 2024_09_20 22:00 | 3212774 | 13 | 19.3957 | 19.0096 | -116.2216 | 4.2179 | 42.6683 | 0.0033 | 0.0032 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415414_27303152 | 152650 | 902 | -89.8 | 152650 | 977 | -91.2 | 152650 | 193 | -96.4 | 152650 | 820 |
| MR_1774415414_E85352AF | 504990 | 730 | -95.7 | 504990 | 380 | -90.9 | 504990 | 768 | -99.2 | 504990 | 851 |
| MR_1774415414_27EE61C4 | 504990 | 730 | -92.5 | 504990 | 380 | -93.2 | 504990 | 768 | -99.1 | 504990 | 851 |
| MR_1774415414_4BF10DD4 | 504990 | 730 | -95.8 | 504990 | 380 | -89.4 | 504990 | 768 | -97.8 | 504990 | 851 |
| MR_1774415414_DE61C472 | 152650 | 902 | -91.2 | 152650 | 977 | -93.0 | 152650 | 193 | -94.4 | 152650 | 820 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1625: `b8b06690-1b6...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `b8b06690-1b6c-410f-983c-45097193e586` |
| Tag | **single-answer** |
| 정답 | **C22** |
| C22 의미 | Decrease A3 Offset threshold for 3213293_1 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1625] topology](images/train_1625.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3213293_1
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3257147_4
- `C3`: Insufficient data; more data is needed for judgment.
- `C4`: Lift the tilt angle  of 3257147_4 by 10 degrees
- `C5`: Adjust the azimuth of 3213293_1 by 50 degrees
- `C6`: Decrease transmission power for 3257147_4
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3257147_4
- `C8`: Decrease A3 Offset threshold for 3257147_4
- `C9`: Check test server and transmission issues
- `C10`: Increase A3 Offset threshold for 3257147_4
- `C11`: Lift the tilt angle of 3213293_1 by 10 degrees
- `C12`: Increase transmission power for 3257147_4
- `C13`: Add neighbor relationship between 3238011_3 and 3257147_4
- `C14`: Add neighbor relationship between 3213293_1 and 3257147_4
- `C15`: Adjust the azimuth of 3257147_4 by 42 degrees
- `C16`: Increase A3 Offset threshold for 3213293_1
- `C17`: Press down the tilt angle of 3213293_1 by 10 degrees
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3213293_1
- `C19`: Decrease transmission power for 3213293_1
- `C20`: Press down the tilt angle  of 3257147_4 by 10 degrees
- `C21`: Increase transmission power for 3213293_1
- `C22`: Decrease A3 Offset threshold for 3213293_1 **← 정답**

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.935 | MS1 | 121.4656773801 | 31.1446371362 | 458 | 504990 | -80.55 | 15.71 | 317.67 | 0.00 | 2.95 | 1583 |
| 2024-09-20 22:21:32.772 | MS1 | 121.4656595838 | 31.1446253459 | 458 | 504990 | -81.70 | 13.20 | 559.70 | 0.03 | 2.29 | 1570 |
| 2024-09-20 22:21:33.955 | MS1 | 121.4656704219 | 31.1446204150 | 458 | 504990 | -80.61 | 12.53 | 386.57 | 0.09 | 2.06 | 1593 |
| 2024-09-20 22:21:34.682 | MS1 | 121.4656742229 | 31.1446323669 | 458 | 504990 | -85.69 | -0.75 | 62.79 | 0.01 | 1.46 | 1583 |
| 2024-09-20 22:21:35.624 | MS1 | 121.4656705786 | 31.1446219134 | 458 | 504990 | -87.68 | -0.47 | 45.00 | 0.16 | 1.02 | 1593 |
| 2024-09-20 22:21:36.451 | MS1 | 121.4656726275 | 31.1446197300 | 458 | 504990 | -90.67 | -0.65 | 58.14 | 0.08 | 1.46 | 1584 |
| 2024-09-20 22:21:37.889 | MS1 | 121.4656614882 | 31.1446365873 | 458 | 504990 | -83.11 | -3.83 | 69.08 | 0.17 | 1.36 | 1577 |
| 2024-09-20 22:21:38.525 | MS1 | 121.4656762575 | 31.1446206595 | 458 | 504990 | -90.57 | -2.69 | 49.14 | 0.06 | 1.07 | 1593 |
| 2024-09-20 22:21:39.320 | MS1 | 121.4656700175 | 31.1446374034 | 189 | 504990 | -75.94 | 15.60 | 233.28 | 0.01 | 1.27 | 1576 |
| 2024-09-20 22:21:40.470 | MS1 | 121.4656613197 | 31.1446365801 | 189 | 504990 | -78.09 | 15.07 | 378.09 | 0.03 | 2.56 | 1577 |
| 2024-09-20 22:21:41.487 | MS1 | 121.4656661734 | 31.1446367946 | 189 | 504990 | -82.55 | 13.86 | 482.37 | 0.19 | 2.56 | 1587 |
| 2024-09-20 22:21:42.477 | MS1 | 121.4656741865 | 31.1446330759 | 189 | 504990 | -81.52 | 17.13 | 594.15 | 0.06 | 2.18 | 1562 |

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
| 3213293 | 1 | 121.4667237732 | 31.1453618783 | 311 | 5 | 7 | 30.3 | TDD | 458 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3238011 | 3 | 121.4706446693 | 31.1542975335 | 28 | 0 | 7 | 16.6 | TDD | 197 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3249394 | 2 | 121.4717343941 | 31.1492425321 | 35 | 5 | 5 | 44.5 | TDD | 595 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3257147 | 4 | 121.4730183882 | 31.1533047093 | 174 | 9 | 4 | 34.2 | TDD | 189 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

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
| 2024-09-20 22:21:30.987 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.006 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.147 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.147 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.843 | NREventA3 | measId:2;ServCellPCI:640;Se... |
| 2024-09-20 22:21:38.083 | NRHandoverAttempt | SourcePCI:640;SourceNR-ARFC... |
| 2024-09-20 22:21:38.128 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.138 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.242 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.242 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3213293 | 1 | 12.0157 | 7.5158 | -117.8414 | 17.5292 | 123.7170 | 0.0129 | 0.1987 |
| 2024_09_20 22:00 | 3249394 | 2 | 19.6693 | 18.5844 | -117.1679 | 10.3429 | 182.7641 | 0.0167 | 0.0198 |
| 2024_09_20 22:00 | 3238011 | 3 | 5.9003 | 8.7120 | -114.3898 | 11.2288 | 165.3114 | 0.0101 | 0.0159 |
| 2024_09_20 22:00 | 3257147 | 4 | 15.6431 | 18.5295 | -116.6937 | 12.8246 | 95.9787 | 0.0022 | 0.0151 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414938_ED3C7C0E | 504990 | 458 | -84.4 | 504990 | 189 | -80.7 | 504990 | 197 | -84.8 | 504990 | 595 |
| MR_1774414938_D797FDAF | 504990 | 458 | -86.0 | 504990 | 189 | -79.1 | 504990 | 197 | -83.5 | 504990 | 595 |
| MR_1774414938_14F274CF | 504990 | 189 | -79.4 | 504990 | 458 | -83.9 | 504990 | 197 | -84.6 | 504990 | 595 |
| MR_1774414938_3040F528 | 504990 | 458 | -84.8 | 504990 | 189 | -80.9 | 504990 | 197 | -87.0 | 504990 | 595 |
| MR_1774414938_2E744F23 | 504990 | 458 | -86.5 | 504990 | 189 | -78.6 | 504990 | 197 | -83.6 | 504990 | 595 |
| MR_1774414938_1BBE2F8A | 504990 | 458 | -83.8 | 504990 | 189 | -79.2 | 504990 | 197 | -86.0 | 504990 | 595 |
| MR_1774414938_D68AAE7A | 504990 | 458 | -87.1 | 504990 | 189 | -82.5 | 504990 | 197 | -83.6 | 504990 | 595 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1626: `ebee55da-b6c...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `ebee55da-b6cd-44be-b852-a350be51f3c6` |
| Tag | **single-answer** |
| 정답 | **C13** |
| C13 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1626] topology](images/train_1626.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3271608_3
- `C2`: Decrease transmission power for 3224099_2
- `C3`: Add neighbor relationship between 3224099_2 and 3271608_3
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3271608_3
- `C5`: Lift the tilt angle of 3224099_2 by 10 degrees
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3224099_2
- `C7`: Insufficient data; more data is needed for judgment.
- `C8`: Increase transmission power for 3224099_2
- `C9`: Press down the tilt angle  of 3271608_3 by 2 degrees
- `C10`: Increase transmission power for 3271608_3
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3271608_3
- `C12`: Adjust the azimuth of 3271608_3 by 50 degrees
- `C13`: Check test server and transmission issues **← 정답**
- `C14`: Decrease A3 Offset threshold for 3271608_3
- `C15`: Increase A3 Offset threshold for 3224099_2
- `C16`: Decrease transmission power for 3271608_3
- `C17`: Press down the tilt angle of 3224099_2 by 10 degrees
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3224099_2
- `C19`: Lift the tilt angle  of 3271608_3 by 2 degrees
- `C20`: Decrease A3 Offset threshold for 3224099_2
- `C21`: Adjust the azimuth of 3224099_2 by 50 degrees
- `C22`: Add neighbor relationship between 3236134_4 and 3271608_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.674 | MS1 | 121.4656608035 | 31.1446197068 | 586 | 504990 | -91.52 | 17.17 | 600.85 | 0.13 | 2.14 | 1582 |
| 2024-09-20 22:21:32.274 | MS1 | 121.4656679904 | 31.1446259213 | 586 | 504990 | -90.14 | 14.75 | 312.58 | 0.02 | 2.31 | 1560 |
| 2024-09-20 22:21:33.833 | MS1 | 121.4656737938 | 31.1446295515 | 586 | 504990 | -90.42 | 13.95 | 440.60 | 0.20 | 2.91 | 1562 |
| 2024-09-20 22:21:34.857 | MS1 | 121.4656650670 | 31.1446263731 | 586 | 504990 | -87.65 | 16.36 | 60.83 | 0.18 | 2.11 | 415 |
| 2024-09-20 22:21:35.810 | MS1 | 121.4656655895 | 31.1446213933 | 586 | 504990 | -90.97 | 15.55 | 51.45 | 0.14 | 2.02 | 454 |
| 2024-09-20 22:21:36.498 | MS1 | 121.4656749927 | 31.1446283825 | 586 | 504990 | -89.60 | 12.04 | 96.58 | 0.12 | 2.87 | 378 |
| 2024-09-20 22:21:37.797 | MS1 | 121.4656630306 | 31.1446367830 | 586 | 504990 | -93.64 | 9.69 | 83.30 | 0.13 | 2.63 | 405 |
| 2024-09-20 22:21:38.154 | MS1 | 121.4656610171 | 31.1446235879 | 586 | 504990 | -92.57 | 9.74 | 89.45 | 0.04 | 2.30 | 348 |
| 2024-09-20 22:21:39.496 | MS1 | 121.4656734673 | 31.1446201315 | 586 | 504990 | -92.29 | 8.27 | 69.20 | 0.09 | 2.45 | 357 |
| 2024-09-20 22:21:40.435 | MS1 | 121.4656634429 | 31.1446195497 | 586 | 504990 | -91.28 | 9.19 | 447.11 | 0.09 | 2.70 | 1598 |
| 2024-09-20 22:21:41.234 | MS1 | 121.4656596010 | 31.1446202491 | 586 | 504990 | -92.95 | 9.97 | 397.09 | 0.02 | 2.09 | 1581 |
| 2024-09-20 22:21:42.942 | MS1 | 121.4656617092 | 31.1446343881 | 586 | 504990 | -92.04 | 8.43 | 446.81 | 0.01 | 2.20 | 1591 |

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
| 3220063 | 1 | 121.4718001379 | 31.1536213246 | 28 | 5 | 11 | 43.1 | TDD | 704 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3224099 | 2 | 121.4697916636 | 31.1449680396 | 22 | 9 | 0 | 41.8 | TDD | 586 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3236134 | 4 | 121.4691899367 | 31.1554192013 | 96 | 0 | 8 | 27.4 | TDD | 906 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3271608 | 3 | 121.4699592388 | 31.1528910151 | 5 | 0 | 7 | 32.8 | TDD | 130 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

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
| 2024-09-20 22:21:30.986 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.009 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.151 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.151 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.833 | NREventA3 | measId:2;ServCellPCI:135;Se... |
| 2024-09-20 22:21:38.073 | NRHandoverAttempt | SourcePCI:135;SourceNR-ARFC... |
| 2024-09-20 22:21:38.112 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.125 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.242 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.242 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3220063 | 1 | 18.5284 | 8.7682 | -114.6401 | 6.3340 | 176.4850 | 0.0151 | 0.0057 |
| 2024_09_20 22:00 | 3224099 | 2 | 11.2139 | 12.2092 | -114.3601 | 11.5476 | 123.4950 | 0.0198 | 0.0150 |
| 2024_09_20 22:00 | 3271608 | 3 | 14.4693 | 9.8506 | -116.6716 | 6.1064 | 131.9700 | 0.0169 | 0.0083 |
| 2024_09_20 22:00 | 3236134 | 4 | 18.4829 | 10.3787 | -115.7713 | 18.8157 | 187.9010 | 0.0096 | 0.0156 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413256_E663981B | 504990 | 586 | -88.5 | 504990 | 130 | -87.1 | 504990 | 906 | -97.4 | 504990 | 704 |
| MR_1774413256_8A569194 | 504990 | 586 | -86.4 | 504990 | 130 | -87.3 | 504990 | 906 | -96.4 | 504990 | 704 |
| MR_1774413256_B3F169B9 | 504990 | 586 | -87.9 | 504990 | 130 | -86.6 | 504990 | 906 | -95.9 | 504990 | 704 |
| MR_1774413256_34A0F242 | 504990 | 586 | -88.3 | 504990 | 130 | -88.5 | 504990 | 906 | -97.1 | 504990 | 704 |
| MR_1774413256_DE6A61CF | 504990 | 586 | -89.4 | 504990 | 130 | -88.9 | 504990 | 906 | -94.0 | 504990 | 704 |
| MR_1774413256_BFDD327B | 504990 | 586 | -85.9 | 504990 | 130 | -88.5 | 504990 | 906 | -97.1 | 504990 | 704 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1627: `50a17321-e15...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `50a17321-e15a-4b58-b541-5e48dc349c6a` |
| Tag | **single-answer** |
| 정답 | **C3** |
| C3 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1627] topology](images/train_1627.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Check test server and transmission issues
- `C2`: Increase A3 Offset threshold for 3275218_3
- `C3`: Insufficient data; more data is needed for judgment. **← 정답**
- `C4`: Lift the tilt angle  of 3275218_3 by 10 degrees
- `C5`: Add neighbor relationship between 3272914_4 and 3275218_3
- `C6`: Adjust the azimuth of 3272914_4 by 14 degrees
- `C7`: Increase transmission power for 3272914_4
- `C8`: Decrease A3 Offset threshold for 3275218_3
- `C9`: Decrease A3 Offset threshold for 3272914_4
- `C10`: Increase A3 Offset threshold for 3272914_4
- `C11`: Lift the tilt angle of 3272914_4 by 10 degrees
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3272914_4
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3272914_4
- `C14`: Press down the tilt angle of 3272914_4 by 10 degrees
- `C15`: Adjust the azimuth of 3275218_3 by 50 degrees
- `C16`: Decrease transmission power for 3275218_3
- `C17`: Add neighbor relationship between 3212470_2 and 3275218_3
- `C18`: Decrease transmission power for 3272914_4
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3275218_3
- `C20`: Increase transmission power for 3275218_3
- `C21`: Press down the tilt angle  of 3275218_3 by 10 degrees
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3275218_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.202 | MS1 | 121.4656592680 | 31.1446263690 | 725 | 504990 | -85.84 | 13.50 | 407.27 | 0.10 | 2.44 | 1588 |
| 2024-09-20 22:21:32.445 | MS1 | 121.4656707330 | 31.1446376852 | 725 | 504990 | -86.90 | 15.90 | 308.63 | 0.08 | 2.29 | 1574 |
| 2024-09-20 22:21:33.463 | MS1 | 121.4656677701 | 31.1446373825 | 725 | 504990 | -89.30 | 16.85 | 488.86 | 0.01 | 2.91 | 1568 |
| 2024-09-20 22:21:34.282 | MS1 | 121.4656591192 | 31.1446226565 | 725 | 504990 | -85.45 | 15.32 | 79.39 | 0.01 | 2.41 | 1571 |
| 2024-09-20 22:21:35.503 | MS1 | 121.4656653654 | 31.1446245647 | 725 | 504990 | -90.85 | 15.77 | 68.43 | 0.06 | 2.53 | 1568 |
| 2024-09-20 22:21:36.245 | MS1 | 121.4656644852 | 31.1446200918 | 725 | 504990 | -91.22 | 14.98 | 82.72 | 0.10 | 2.91 | 1578 |
| 2024-09-20 22:21:37.705 | MS1 | 121.4656775750 | 31.1446311139 | 725 | 504990 | -91.19 | 12.63 | 82.50 | 0.00 | 2.84 | 1592 |
| 2024-09-20 22:21:38.644 | MS1 | 121.4656740191 | 31.1446248367 | 725 | 504990 | -92.27 | 12.11 | 67.84 | 0.14 | 2.23 | 1564 |
| 2024-09-20 22:21:39.301 | MS1 | 121.4656762689 | 31.1446265530 | 725 | 504990 | -89.01 | 11.37 | 62.47 | 0.20 | 2.46 | 1566 |
| 2024-09-20 22:21:40.699 | MS1 | 121.4656754142 | 31.1446181403 | 725 | 504990 | -93.96 | 12.26 | 484.05 | 0.14 | 2.91 | 1582 |
| 2024-09-20 22:21:41.849 | MS1 | 121.4656586698 | 31.1446185305 | 725 | 504990 | -89.67 | 8.31 | 390.53 | 0.16 | 2.56 | 1574 |
| 2024-09-20 22:21:42.391 | MS1 | 121.4656678186 | 31.1446229595 | 725 | 504990 | -89.11 | 9.39 | 525.36 | 0.03 | 2.03 | 1566 |

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
| 3210191 | 1 | 121.4759808561 | 31.1483053918 | 335 | 4 | 8 | 43.2 | TDD | 280 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3212470 | 2 | 121.4654173456 | 31.1487959992 | 314 | 4 | 4 | 31.0 | TDD | 849 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3272914 | 4 | 121.4742929371 | 31.1441012417 | 288 | 10 | 11 | 27.0 | TDD | 725 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3275218 | 3 | 121.4681420155 | 31.1531458329 | 72 | 13 | 6 | 34.2 | TDD | 99 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |

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
| 2024-09-20 22:21:30.936 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.951 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.101 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.101 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.798 | NREventA3 | measId:2;ServCellPCI:471;Se... |
| 2024-09-20 22:21:38.038 | NRHandoverAttempt | SourcePCI:471;SourceNR-ARFC... |
| 2024-09-20 22:21:38.078 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.092 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.208 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.208 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3210191 | 1 | 94.1361 | 87.2989 | -117.8560 | 19.1621 | 198.5852 | 0.0045 | 0.0125 |
| 2024_09_19 22:00 | 3212470 | 2 | 79.0598 | 90.6077 | -116.1868 | 17.0370 | 192.9980 | 0.0172 | 0.0034 |
| 2024_09_19 22:00 | 3275218 | 3 | 93.9124 | 79.1501 | -114.8642 | 14.7143 | 152.0398 | 0.0114 | 0.0122 |
| 2024_09_19 22:00 | 3272914 | 4 | 83.8501 | 87.4050 | -117.0867 | 17.8463 | 86.0315 | 0.0157 | 0.0084 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414368_14B0CFB8 | 504990 | 725 | -87.3 | 504990 | 99 | -95.5 | 504990 | 849 | -96.0 | 504990 | 280 |
| MR_1774414368_256E9029 | 504990 | 725 | -86.7 | 504990 | 99 | -92.6 | 504990 | 849 | -95.2 | 504990 | 280 |
| MR_1774414368_8772A070 | 504990 | 725 | -86.2 | 504990 | 99 | -94.9 | 504990 | 849 | -94.8 | 504990 | 280 |
| MR_1774414368_7AE346AF | 504990 | 725 | -83.5 | 504990 | 99 | -92.7 | 504990 | 849 | -94.7 | 504990 | 280 |
| MR_1774414368_9433D6BC | 504990 | 725 | -85.1 | 504990 | 99 | -95.0 | 504990 | 849 | -96.9 | 504990 | 280 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1628: `254d3aca-b4c...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `254d3aca-b4c1-43cd-9fd7-6c0e692ad4de` |
| Tag | **single-answer** |
| 정답 | **C13** |
| C13 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1628] topology](images/train_1628.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3263316_3
- `C2`: Add neighbor relationship between 3263316_3 and 3276448_2
- `C3`: Add neighbor relationship between 3211306_1 and 3276448_2
- `C4`: Check test server and transmission issues
- `C5`: Decrease A3 Offset threshold for 3276448_2
- `C6`: Decrease transmission power for 3263316_3
- `C7`: Adjust the azimuth of 3276448_2 by 50 degrees
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3276448_2
- `C9`: Increase transmission power for 3263316_3
- `C10`: Lift the tilt angle of 3263316_3 by 10 degrees
- `C11`: Press down the tilt angle of 3263316_3 by 10 degrees
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3276448_2
- `C13`: Insufficient data; more data is needed for judgment. **← 정답**
- `C14`: Increase A3 Offset threshold for 3276448_2
- `C15`: Adjust the azimuth of 3263316_3 by 50 degrees
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3263316_3
- `C17`: Decrease A3 Offset threshold for 3263316_3
- `C18`: Lift the tilt angle  of 3276448_2 by 7 degrees
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3263316_3
- `C20`: Decrease transmission power for 3276448_2
- `C21`: Press down the tilt angle  of 3276448_2 by 7 degrees
- `C22`: Increase transmission power for 3276448_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.389 | MS1 | 121.4656696919 | 31.1446241420 | 725 | 504990 | -85.59 | 13.11 | 344.84 | 0.13 | 2.46 | 1585 |
| 2024-09-20 22:21:32.236 | MS1 | 121.4656759901 | 31.1446249612 | 725 | 504990 | -86.92 | 15.83 | 586.73 | 0.08 | 2.98 | 1578 |
| 2024-09-20 22:21:33.739 | MS1 | 121.4656596484 | 31.1446207572 | 725 | 504990 | -89.39 | 12.84 | 398.05 | 0.09 | 2.38 | 1583 |
| 2024-09-20 22:21:34.398 | MS1 | 121.4656612827 | 31.1446373373 | 725 | 504990 | -91.25 | 17.20 | 82.51 | 0.13 | 2.63 | 1583 |
| 2024-09-20 22:21:35.403 | MS1 | 121.4656711995 | 31.1446188728 | 725 | 504990 | -88.72 | 12.62 | 105.98 | 0.06 | 2.85 | 1573 |
| 2024-09-20 22:21:36.924 | MS1 | 121.4656701123 | 31.1446273301 | 725 | 504990 | -91.85 | 14.16 | 106.19 | 0.12 | 2.21 | 1565 |
| 2024-09-20 22:21:37.391 | MS1 | 121.4656653815 | 31.1446316440 | 725 | 504990 | -91.55 | 9.58 | 66.65 | 0.11 | 2.91 | 1569 |
| 2024-09-20 22:21:38.521 | MS1 | 121.4656776026 | 31.1446294870 | 725 | 504990 | -89.65 | 7.89 | 70.66 | 0.01 | 2.26 | 1565 |
| 2024-09-20 22:21:39.637 | MS1 | 121.4656648403 | 31.1446267913 | 725 | 504990 | -90.16 | 12.75 | 81.83 | 0.19 | 2.68 | 1571 |
| 2024-09-20 22:21:40.160 | MS1 | 121.4656637221 | 31.1446185227 | 725 | 504990 | -91.23 | 9.94 | 539.14 | 0.15 | 2.23 | 1592 |
| 2024-09-20 22:21:41.468 | MS1 | 121.4656770690 | 31.1446214631 | 725 | 504990 | -91.34 | 7.22 | 564.57 | 0.02 | 2.11 | 1595 |
| 2024-09-20 22:21:42.806 | MS1 | 121.4656684805 | 31.1446376350 | 725 | 504990 | -93.07 | 12.01 | 327.50 | 0.14 | 2.46 | 1569 |

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
| 3211306 | 1 | 121.4686264568 | 31.1521682501 | 245 | 14 | 10 | 23.4 | TDD | 568 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3263316 | 3 | 121.4750206759 | 31.1555069894 | 132 | 12 | 10 | 22.1 | TDD | 725 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3265583 | 4 | 121.4651997899 | 31.1478397675 | 11 | 9 | 8 | 40.2 | TDD | 655 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3276448 | 2 | 121.4643491246 | 31.1551586430 | 260 | 5 | 4 | 32.1 | TDD | 131 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |

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
| 2024-09-20 22:21:31.035 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.051 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.168 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.168 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.928 | NREventA3 | measId:2;ServCellPCI:663;Se... |
| 2024-09-20 22:21:38.168 | NRHandoverAttempt | SourcePCI:663;SourceNR-ARFC... |
| 2024-09-20 22:21:38.209 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.224 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.363 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.363 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3211306 | 1 | 89.9313 | 89.7681 | -115.5852 | 18.9848 | 162.9820 | 0.0018 | 0.0169 |
| 2024_09_19 22:00 | 3276448 | 2 | 78.9055 | 82.7571 | -115.7788 | 17.3058 | 88.7870 | 0.0053 | 0.0045 |
| 2024_09_19 22:00 | 3263316 | 3 | 90.2974 | 92.6499 | -114.5275 | 11.2338 | 119.8819 | 0.0095 | 0.0016 |
| 2024_09_19 22:00 | 3265583 | 4 | 80.6800 | 91.8652 | -114.1753 | 17.5635 | 119.2146 | 0.0053 | 0.0131 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413901_1B3C75B8 | 504990 | 725 | -91.2 | 504990 | 131 | -100.4 | 504990 | 568 | -99.9 | 504990 | 655 |
| MR_1774413901_55FBA076 | 504990 | 725 | -90.2 | 504990 | 131 | -98.4 | 504990 | 568 | -101.2 | 504990 | 655 |
| MR_1774413901_9505DE24 | 504990 | 725 | -92.7 | 504990 | 131 | -99.5 | 504990 | 568 | -100.3 | 504990 | 655 |
| MR_1774413901_15D25FFA | 504990 | 725 | -90.0 | 504990 | 131 | -97.2 | 504990 | 568 | -100.8 | 504990 | 655 |
| MR_1774413901_CABE9D50 | 504990 | 725 | -89.7 | 504990 | 131 | -99.5 | 504990 | 568 | -98.2 | 504990 | 655 |
| MR_1774413901_A7BF90AB | 504990 | 725 | -92.7 | 504990 | 131 | -97.5 | 504990 | 568 | -101.0 | 504990 | 655 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1629: `e866100e-9be...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `e866100e-9be7-4d04-984b-9819acaaed51` |
| Tag | **single-answer** |
| 정답 | **C11** |
| C11 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3272762_5 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1629] topology](images/train_1629.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3244067_6
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3244067_6
- `C3`: Decrease transmission power for 3272762_5
- `C4`: Decrease A3 Offset threshold for 3272762_5
- `C5`: Add neighbor relationship between 3261918_12 and 3244067_6
- `C6`: Press down the tilt angle of 3272762_5 by 6 degrees
- `C7`: Add neighbor relationship between 3272762_5 and 3244067_6
- `C8`: Adjust the azimuth of 3244067_6 by 35 degrees
- `C9`: Increase transmission power for 3272762_5
- `C10`: Increase transmission power for 3244067_6
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3272762_5 **← 정답**
- `C12`: Insufficient data; more data is needed for judgment.
- `C13`: Adjust the azimuth of 3272762_5 by 15 degrees
- `C14`: Lift the tilt angle  of 3244067_6 by 4 degrees
- `C15`: Press down the tilt angle  of 3244067_6 by 4 degrees
- `C16`: Increase A3 Offset threshold for 3272762_5
- `C17`: Decrease transmission power for 3244067_6
- `C18`: Decrease A3 Offset threshold for 3244067_6
- `C19`: Increase A3 Offset threshold for 3244067_6
- `C20`: Lift the tilt angle of 3272762_5 by 6 degrees
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3272762_5
- `C22`: Check test server and transmission issues

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.403 | MS1 | 121.4656672344 | 31.1446254769 | 350 | 504990 | -95.09 | 9.89 | 412.42 | 0.10 | 2.81 | 1580 |
| 2024-09-20 22:21:32.852 | MS1 | 121.4656660327 | 31.1446351823 | 826 | 504990 | -95.88 | 10.42 | 563.69 | 0.13 | 2.10 | 1560 |
| 2024-09-20 22:21:33.971 | MS1 | 121.4656675950 | 31.1446335298 | 355 | 504990 | -93.71 | 12.29 | 347.60 | 0.01 | 2.11 | 1595 |
| 2024-09-20 22:21:34.632 | MS1 | 121.4656621542 | 31.1446317008 | 3 | 152650 | -90.58 | 5.52 | 93.83 | 0.06 | 1.78 | 986 |
| 2024-09-20 22:21:35.724 | MS1 | 121.4656711935 | 31.1446343684 | 579 | 152650 | -95.60 | 4.32 | 88.40 | 0.09 | 1.54 | 922 |
| 2024-09-20 22:21:36.720 | MS1 | 121.4656629726 | 31.1446239476 | 793 | 152650 | -95.39 | 5.28 | 66.07 | 0.13 | 1.70 | 988 |
| 2024-09-20 22:21:37.939 | MS1 | 121.4656582540 | 31.1446234045 | 108 | 152650 | -88.66 | 6.30 | 61.12 | 0.07 | 1.70 | 949 |
| 2024-09-20 22:21:38.339 | MS1 | 121.4656638341 | 31.1446209744 | 3 | 152650 | -95.26 | 4.81 | 78.88 | 0.10 | 1.53 | 991 |
| 2024-09-20 22:21:39.517 | MS1 | 121.4656648238 | 31.1446253658 | 579 | 152650 | -95.34 | 5.12 | 60.23 | 0.05 | 1.59 | 906 |
| 2024-09-20 22:21:40.488 | MS1 | 121.4656765272 | 31.1446240212 | 793 | 152650 | -88.59 | 2.27 | 67.97 | 0.14 | 2.24 | 1594 |
| 2024-09-20 22:21:41.938 | MS1 | 121.4656587246 | 31.1446355603 | 108 | 152650 | -94.37 | 2.48 | 53.51 | 0.17 | 2.36 | 1563 |
| 2024-09-20 22:21:42.586 | MS1 | 121.4656634231 | 31.1446189882 | 3 | 152650 | -93.57 | 4.94 | 88.23 | 0.01 | 2.25 | 1592 |

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
| 3210450 | 11 | 121.4686345758 | 31.1530550972 | 91 | 8 | 2 | 3.9 | FDD | 149 | n1 | 152650 | 30M | 4T4R | 15 | 152650 |
| 3223021 | 8 | 121.4742349380 | 31.1507087206 | 8 | 5 | 0 | 3.7 | FDD | 3 | n1 | 152650 | 30M | 4T4R | 30 | 152650 |
| 3231404 | 7 | 121.4729741211 | 31.1498414930 | 280 | 5 | 4 | 21.9 | FDD | 579 | n1 | 152650 | 30M | 4T4R | 10 | 152650 |
| 3241823 | 13 | 121.4699861071 | 31.1553133358 | 17 | 7 | 6 | 4.8 | FDD | 252 | n1 | 152650 | 30M | 4T4R | 23 | 152650 |
| 3244067 | 6 | 121.4658545812 | 31.1489627292 | 147 | 1 | 9 | 26.0 | TDD | 383 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3246610 | 9 | 121.4754738101 | 31.1545293503 | 284 | 14 | 9 | 27.0 | FDD | 108 | n1 | 152650 | 30M | 4T4R | 28 | 152650 |
| 3250420 | 2 | 121.4663650969 | 31.1449416219 | 204 | 8 | 4 | 5.7 | TDD | 517 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3258784 | 10 | 121.4665174779 | 31.1460866303 | 110 | 11 | 11 | 15.6 | FDD | 723 | n1 | 152650 | 30M | 4T4R | 26 | 152650 |
| 3261918 | 12 | 121.4748886387 | 31.1556432954 | 108 | 15 | 7 | 8.6 | FDD | 793 | n1 | 152650 | 30M | 4T4R | 28 | 152650 |
| 3265946 | 1 | 121.4719435734 | 31.1509804827 | 231 | 4 | 1 | 19.8 | TDD | 355 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3272762 | 5 | 121.4691928941 | 31.1517284573 | 188 | 4 | 3 | 27.1 | TDD | 350 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3275588 | 4 | 121.4655829834 | 31.1502916833 | 170 | 4 | 5 | 7.2 | TDD | 669 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3277322 | 3 | 121.4690025522 | 31.1557697580 | 187 | 4 | 3 | 28.2 | TDD | 826 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:31.281 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.281 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.028 | NREventA2 | measId:1;ServCellPCI:648;Se... |
| 2024-09-20 22:21:35.143 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.344 | NREventA5 | measId:3;ServCellPCI:648;Se... |
| 2024-09-20 22:21:35.424 | NRHandoverAttempt | SourcePCI:648;SourceNR-ARFC... |
| 2024-09-20 22:21:35.468 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.479 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:35.618 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.618 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3265946 | 1 | 14.9461 | 7.4005 | -115.4368 | 17.1365 | 112.4030 | 0.0041 | 0.0120 |
| 2024_09_20 22:00 | 3250420 | 2 | 13.1144 | 14.7723 | -114.7527 | 12.8926 | 105.2923 | 0.0016 | 0.0149 |
| 2024_09_20 22:00 | 3277322 | 3 | 16.3674 | 8.2141 | -117.0572 | 14.8599 | 193.0990 | 0.0119 | 0.0194 |
| 2024_09_20 22:00 | 3275588 | 4 | 18.9865 | 10.6497 | -115.1895 | 17.0898 | 84.7850 | 0.0006 | 0.0156 |
| 2024_09_20 22:00 | 3272762 | 5 | 13.5175 | 14.8078 | -116.4800 | 13.9011 | 151.5344 | 0.0140 | 0.0078 |
| 2024_09_20 22:00 | 3244067 | 6 | 19.3629 | 14.7697 | -116.6632 | 19.7421 | 155.5754 | 0.0177 | 0.0166 |
| 2024_09_20 22:00 | 3231404 | 7 | 6.1711 | 6.5353 | -116.8336 | 4.6983 | 30.5061 | 0.0152 | 0.0156 |
| 2024_09_20 22:00 | 3223021 | 8 | 13.9019 | 5.4422 | -117.2035 | 4.0011 | 48.7129 | 0.0132 | 0.0191 |
| 2024_09_20 22:00 | 3246610 | 9 | 9.5382 | 9.2893 | -115.1235 | 3.9167 | 54.9550 | 0.0045 | 0.0193 |
| 2024_09_20 22:00 | 3258784 | 10 | 10.9794 | 13.8341 | -116.9033 | 4.1822 | 55.0754 | 0.0012 | 0.0062 |
| 2024_09_20 22:00 | 3210450 | 11 | 14.6431 | 19.0479 | -115.0087 | 4.5835 | 28.6418 | 0.0148 | 0.0173 |
| 2024_09_20 22:00 | 3261918 | 12 | 7.8336 | 9.0878 | -117.5411 | 3.4515 | 57.6494 | 0.0069 | 0.0030 |
| 2024_09_20 22:00 | 3241823 | 13 | 11.0410 | 5.7821 | -115.3574 | 4.3263 | 43.2647 | 0.0016 | 0.0048 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413084_5159B975 | 152650 | 3 | -90.2 | 152650 | 723 | -95.3 | 152650 | 149 | -100.6 | 152650 | 252 |
| MR_1774413084_FEAF63D2 | 504990 | 355 | -94.4 | 504990 | 383 | -87.6 | 504990 | 517 | -95.7 | 504990 | 669 |
| MR_1774413084_28C7B868 | 504990 | 355 | -94.7 | 504990 | 383 | -90.6 | 504990 | 517 | -95.8 | 504990 | 669 |
| MR_1774413084_9DC2C267 | 152650 | 3 | -90.6 | 152650 | 723 | -98.4 | 152650 | 149 | -99.4 | 152650 | 252 |
| MR_1774413084_40340C47 | 152650 | 3 | -90.7 | 152650 | 723 | -98.0 | 152650 | 149 | -100.5 | 152650 | 252 |
| MR_1774413084_EDDBC139 | 152650 | 3 | -89.7 | 152650 | 723 | -98.4 | 152650 | 149 | -100.3 | 152650 | 252 |
| MR_1774413084_57AABCAC | 152650 | 3 | -90.3 | 152650 | 723 | -95.5 | 152650 | 149 | -100.5 | 152650 | 252 |

> *... 2개 열 생략 (전체 14열)*

---
