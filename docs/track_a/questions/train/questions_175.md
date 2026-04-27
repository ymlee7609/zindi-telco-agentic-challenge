# Track A 문제 분석 — train[1740]~train[1749]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[1740] ~ train[1749] (10개)

## 목차

1. [문제 1740: `2d1274bb-af7...`](#1740) — single-answer, 정답: C7
2. [문제 1741: `a7530b93-bc2...`](#1741) — single-answer, 정답: C22
3. [문제 1742: `fe9a1dab-14e...`](#1742) — single-answer, 정답: C19
4. [문제 1743: `1ff70170-32e...`](#1743) — single-answer, 정답: C19
5. [문제 1744: `ea6b60eb-274...`](#1744) — single-answer, 정답: C12
6. [문제 1745: `e61558a0-8a9...`](#1745) — single-answer, 정답: C8
7. [문제 1746: `a05ed6ad-25d...`](#1746) — single-answer, 정답: C20
8. [문제 1747: `eb8d2d92-1c5...`](#1747) — single-answer, 정답: C16
9. [문제 1748: `55742713-88b...`](#1748) — single-answer, 정답: C16
10. [문제 1749: `be087267-690...`](#1749) — single-answer, 정답: C21

---

### 문제 1740: `2d1274bb-af7...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `2d1274bb-af7a-4afa-9570-ccf3c5e57462` |
| Tag | **single-answer** |
| 정답 | **C7** |
| C7 의미 | Lift the tilt angle  of 3227244_1 by 4 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1740] topology](images/train_1740.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3237197_2
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3237197_2
- `C3`: Add neighbor relationship between 3227244_1 and 3237668_3
- `C4`: Press down the tilt angle of 3237197_2 by 5 degrees
- `C5`: Check test server and transmission issues
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3237668_3
- `C7`: Lift the tilt angle  of 3227244_1 by 4 degrees **← 정답**
- `C8`: Add neighbor relationship between 3237197_2 and 3237668_3
- `C9`: Press down the tilt angle  of 3227244_1 by 4 degrees
- `C10`: Decrease transmission power for 3237668_3
- `C11`: Decrease transmission power for 3237197_2
- `C12`: Decrease A3 Offset threshold for 3237668_3
- `C13`: Adjust the azimuth of 3237197_2 by 50 degrees
- `C14`: Decrease A3 Offset threshold for 3237197_2
- `C15`: Lift the tilt angle of 3237197_2 by 5 degrees
- `C16`: Insufficient data; more data is needed for judgment.
- `C17`: Increase transmission power for 3237668_3
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3237668_3
- `C19`: Increase A3 Offset threshold for 3237197_2
- `C20`: Increase A3 Offset threshold for 3237668_3
- `C21`: Adjust the azimuth of 3227244_1 by 50 degrees
- `C22`: Increase transmission power for 3237197_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.911 | MS1 | 121.4656690299 | 31.1446275364 | 775 | 504990 | -85.48 | 15.50 | 438.17 | 0.12 | 2.03 | 1563 |
| 2024-09-20 22:21:32.370 | MS1 | 121.4656758223 | 31.1446278614 | 775 | 504990 | -87.84 | 14.13 | 331.35 | 0.04 | 2.09 | 1585 |
| 2024-09-20 22:21:33.642 | MS1 | 121.4656704741 | 31.1446339753 | 775 | 504990 | -90.44 | 15.60 | 467.40 | 0.17 | 2.35 | 1592 |
| 2024-09-20 22:21:34.562 | MS1 | 121.4656594322 | 31.1446273374 | 775 | 504990 | -91.46 | 15.62 | 81.04 | 0.03 | 2.48 | 1560 |
| 2024-09-20 22:21:35.202 | MS1 | 121.4656596455 | 31.1446271559 | 775 | 504990 | -85.29 | 13.55 | 56.22 | 0.04 | 2.06 | 1585 |
| 2024-09-20 22:21:36.618 | MS1 | 121.4656667546 | 31.1446343531 | 775 | 504990 | -87.85 | 14.04 | 99.71 | 0.04 | 2.57 | 1586 |
| 2024-09-20 22:21:37.917 | MS1 | 121.4656635942 | 31.1446348617 | 775 | 504990 | -93.85 | 9.14 | 87.26 | 0.18 | 2.36 | 1592 |
| 2024-09-20 22:21:38.861 | MS1 | 121.4656682687 | 31.1446287841 | 775 | 504990 | -92.58 | 7.39 | 78.77 | 0.11 | 2.75 | 1561 |
| 2024-09-20 22:21:39.198 | MS1 | 121.4656715845 | 31.1446310671 | 775 | 504990 | -90.11 | 8.46 | 76.36 | 0.12 | 2.46 | 1598 |
| 2024-09-20 22:21:40.139 | MS1 | 121.4656666864 | 31.1446304488 | 775 | 504990 | -93.58 | 10.77 | 493.78 | 0.17 | 2.10 | 1591 |
| 2024-09-20 22:21:41.827 | MS1 | 121.4656769097 | 31.1446285759 | 775 | 504990 | -89.87 | 10.56 | 535.83 | 0.11 | 2.20 | 1589 |
| 2024-09-20 22:21:42.639 | MS1 | 121.4656697159 | 31.1446375474 | 775 | 504990 | -93.68 | 11.41 | 355.93 | 0.06 | 2.44 | 1564 |

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
| 3218460 | 4 | 121.4695155651 | 31.1530404609 | 356 | 6 | 4 | 27.1 | TDD | 922 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3227244 | 1 | 121.4662451354 | 31.1490595090 | 289 | 11 | 6 | 27.5 | TDD | 402 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3237197 | 2 | 121.4681547956 | 31.1541375000 | 143 | 4 | 10 | 18.4 | TDD | 775 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3237668 | 3 | 121.4743674467 | 31.1451298138 | 147 | 2 | 2 | 23.2 | TDD | 253 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:31.345 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.363 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.506 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.506 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.147 | NREventA3 | measId:2;ServCellPCI:395;Se... |
| 2024-09-20 22:21:38.387 | NRHandoverAttempt | SourcePCI:395;SourceNR-ARFC... |
| 2024-09-20 22:21:38.424 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.439 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.584 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.584 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3227244 | 1 | 15.2580 | 6.5690 | -114.1861 | 17.2474 | 100.1836 | 0.0164 | 0.0063 |
| 2024_09_20 22:00 | 3237197 | 2 | 75.2334 | 92.2507 | -114.4840 | 7.5920 | 120.5024 | 0.0040 | 0.0002 |
| 2024_09_20 22:00 | 3237668 | 3 | 16.3538 | 14.5768 | -116.6334 | 13.7376 | 196.1969 | 0.0080 | 0.0010 |
| 2024_09_20 22:00 | 3218460 | 4 | 19.1352 | 8.2989 | -115.6105 | 17.0048 | 107.5789 | 0.0188 | 0.0089 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416977_969C3A16 | 504990 | 775 | -90.8 | 504990 | 253 | -96.1 | 504990 | 402 | -98.8 | 504990 | 922 |
| MR_1774416977_67C989C3 | 504990 | 775 | -90.7 | 504990 | 253 | -93.1 | 504990 | 402 | -99.6 | 504990 | 922 |
| MR_1774416977_7A8D7317 | 504990 | 775 | -90.5 | 504990 | 253 | -94.9 | 504990 | 402 | -98.1 | 504990 | 922 |
| MR_1774416977_A746663D | 504990 | 775 | -90.4 | 504990 | 253 | -95.8 | 504990 | 402 | -98.1 | 504990 | 922 |
| MR_1774416977_127EB402 | 504990 | 775 | -89.7 | 504990 | 253 | -93.3 | 504990 | 402 | -100.4 | 504990 | 922 |
| MR_1774416977_AC459F30 | 504990 | 775 | -91.9 | 504990 | 253 | -93.2 | 504990 | 402 | -101.3 | 504990 | 922 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1741: `a7530b93-bc2...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `a7530b93-bc24-4790-9160-8430cd66f6e1` |
| Tag | **single-answer** |
| 정답 | **C22** |
| C22 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1741] topology](images/train_1741.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3219169_4
- `C2`: Add neighbor relationship between 3234877_1 and 3219169_4
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3234877_1
- `C4`: Decrease transmission power for 3234877_1
- `C5`: Insufficient data; more data is needed for judgment.
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3219169_4
- `C7`: Increase transmission power for 3234877_1
- `C8`: Adjust the azimuth of 3219169_4 by 50 degrees
- `C9`: Increase A3 Offset threshold for 3234877_1
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3219169_4
- `C11`: Adjust the azimuth of 3234877_1 by 50 degrees
- `C12`: Press down the tilt angle of 3234877_1 by 8 degrees
- `C13`: Lift the tilt angle  of 3219169_4 by 6 degrees
- `C14`: Decrease A3 Offset threshold for 3234877_1
- `C15`: Increase transmission power for 3219169_4
- `C16`: Decrease transmission power for 3219169_4
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3234877_1
- `C18`: Press down the tilt angle  of 3219169_4 by 6 degrees
- `C19`: Lift the tilt angle of 3234877_1 by 8 degrees
- `C20`: Decrease A3 Offset threshold for 3219169_4
- `C21`: Add neighbor relationship between 3253495_3 and 3219169_4
- `C22`: Check test server and transmission issues **← 정답**

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.337 | MS1 | 121.4656747811 | 31.1446183242 | 370 | 504990 | -88.26 | 14.04 | 446.92 | 0.02 | 2.96 | 1568 |
| 2024-09-20 22:21:32.461 | MS1 | 121.4656622968 | 31.1446183783 | 370 | 504990 | -85.92 | 12.57 | 552.15 | 0.00 | 2.82 | 1568 |
| 2024-09-20 22:21:33.101 | MS1 | 121.4656646581 | 31.1446295408 | 370 | 504990 | -88.84 | 14.09 | 362.94 | 0.16 | 2.44 | 1582 |
| 2024-09-20 22:21:34.909 | MS1 | 121.4656581956 | 31.1446342591 | 370 | 504990 | -91.23 | 16.19 | 59.69 | 0.04 | 2.99 | 338 |
| 2024-09-20 22:21:35.669 | MS1 | 121.4656598094 | 31.1446326036 | 370 | 504990 | -90.34 | 17.62 | 73.13 | 0.05 | 2.66 | 482 |
| 2024-09-20 22:21:36.670 | MS1 | 121.4656655908 | 31.1446349329 | 370 | 504990 | -86.54 | 14.69 | 87.41 | 0.07 | 2.57 | 455 |
| 2024-09-20 22:21:37.385 | MS1 | 121.4656756729 | 31.1446239236 | 370 | 504990 | -93.61 | 9.52 | 74.80 | 0.02 | 2.30 | 421 |
| 2024-09-20 22:21:38.418 | MS1 | 121.4656743388 | 31.1446261484 | 370 | 504990 | -90.93 | 7.84 | 89.69 | 0.18 | 2.82 | 402 |
| 2024-09-20 22:21:39.998 | MS1 | 121.4656750382 | 31.1446320185 | 370 | 504990 | -91.90 | 7.69 | 60.79 | 0.08 | 2.24 | 375 |
| 2024-09-20 22:21:40.586 | MS1 | 121.4656662951 | 31.1446215946 | 370 | 504990 | -90.75 | 11.61 | 402.60 | 0.09 | 2.99 | 1572 |
| 2024-09-20 22:21:41.814 | MS1 | 121.4656679669 | 31.1446313265 | 370 | 504990 | -89.46 | 10.57 | 396.05 | 0.19 | 2.69 | 1586 |
| 2024-09-20 22:21:42.881 | MS1 | 121.4656612783 | 31.1446345512 | 370 | 504990 | -89.35 | 10.42 | 382.48 | 0.09 | 2.22 | 1587 |

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
| 3219169 | 4 | 121.4719213733 | 31.1471856182 | 141 | 3 | 3 | 40.3 | TDD | 106 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3227968 | 2 | 121.4741547009 | 31.1534452804 | 108 | 5 | 10 | 22.9 | TDD | 635 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3234877 | 1 | 121.4700949076 | 31.1483888685 | 329 | 6 | 6 | 19.9 | TDD | 370 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3253495 | 3 | 121.4743107676 | 31.1542948076 | 11 | 7 | 2 | 30.6 | TDD | 100 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |

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
| 2024-09-20 22:21:31.357 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.493 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.493 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.234 | NREventA3 | measId:2;ServCellPCI:747;Se... |
| 2024-09-20 22:21:38.474 | NRHandoverAttempt | SourcePCI:747;SourceNR-ARFC... |
| 2024-09-20 22:21:38.509 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.521 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.664 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.664 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3234877 | 1 | 17.4293 | 6.5557 | -117.3969 | 8.8080 | 145.0137 | 0.0128 | 0.0030 |
| 2024_09_20 22:00 | 3227968 | 2 | 19.2103 | 14.4783 | -117.0081 | 13.0367 | 144.1160 | 0.0130 | 0.0159 |
| 2024_09_20 22:00 | 3253495 | 3 | 9.6361 | 14.9844 | -114.2279 | 15.4244 | 91.4135 | 0.0012 | 0.0157 |
| 2024_09_20 22:00 | 3219169 | 4 | 12.1231 | 8.4589 | -114.9020 | 16.6097 | 123.7064 | 0.0170 | 0.0023 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412964_63D4E35D | 504990 | 370 | -90.2 | 504990 | 106 | -89.8 | 504990 | 100 | -102.8 | 504990 | 635 |
| MR_1774412964_4D4335A5 | 504990 | 370 | -92.4 | 504990 | 106 | -91.8 | 504990 | 100 | -102.7 | 504990 | 635 |
| MR_1774412964_15F9AE38 | 504990 | 370 | -92.8 | 504990 | 106 | -91.1 | 504990 | 100 | -101.7 | 504990 | 635 |
| MR_1774412964_390CA9E3 | 504990 | 370 | -90.6 | 504990 | 106 | -92.9 | 504990 | 100 | -103.2 | 504990 | 635 |
| MR_1774412964_D9FE3BEB | 504990 | 370 | -92.6 | 504990 | 106 | -92.3 | 504990 | 100 | -100.5 | 504990 | 635 |
| MR_1774412964_750AA23B | 504990 | 370 | -93.1 | 504990 | 106 | -93.5 | 504990 | 100 | -100.4 | 504990 | 635 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1742: `fe9a1dab-14e...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `fe9a1dab-14e6-472c-ba90-5fee09d74dd0` |
| Tag | **single-answer** |
| 정답 | **C19** |
| C19 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3277209_5 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1742] topology](images/train_1742.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3236840_6 by 43 degrees
- `C2`: Lift the tilt angle  of 3236840_6 by 6 degrees
- `C3`: Check test server and transmission issues
- `C4`: Increase transmission power for 3277209_5
- `C5`: Increase A3 Offset threshold for 3277209_5
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3236840_6
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3277209_5
- `C8`: Add neighbor relationship between 3277209_5 and 3236840_6
- `C9`: Decrease A3 Offset threshold for 3277209_5
- `C10`: Press down the tilt angle of 3277209_5 by 5 degrees
- `C11`: Add neighbor relationship between 3250189_7 and 3236840_6
- `C12`: Press down the tilt angle  of 3236840_6 by 6 degrees
- `C13`: Decrease A3 Offset threshold for 3236840_6
- `C14`: Adjust the azimuth of 3277209_5 by 3 degrees
- `C15`: Lift the tilt angle of 3277209_5 by 5 degrees
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3236840_6
- `C17`: Increase A3 Offset threshold for 3236840_6
- `C18`: Decrease transmission power for 3277209_5
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3277209_5 **← 정답**
- `C20`: Decrease transmission power for 3236840_6
- `C21`: Insufficient data; more data is needed for judgment.
- `C22`: Increase transmission power for 3236840_6

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.903 | MS1 | 121.4656598897 | 31.1446350170 | 780 | 504990 | -94.76 | 10.93 | 546.57 | 0.04 | 2.93 | 1579 |
| 2024-09-20 22:21:32.127 | MS1 | 121.4656588140 | 31.1446372687 | 833 | 504990 | -95.12 | 11.20 | 371.59 | 0.20 | 2.50 | 1569 |
| 2024-09-20 22:21:33.265 | MS1 | 121.4656597789 | 31.1446233028 | 681 | 504990 | -93.80 | 11.21 | 350.03 | 0.12 | 2.11 | 1592 |
| 2024-09-20 22:21:34.361 | MS1 | 121.4656640890 | 31.1446303795 | 533 | 152650 | -95.64 | 3.22 | 69.39 | 0.12 | 1.87 | 932 |
| 2024-09-20 22:21:35.578 | MS1 | 121.4656754480 | 31.1446244212 | 203 | 152650 | -92.09 | 5.54 | 73.39 | 0.18 | 1.80 | 914 |
| 2024-09-20 22:21:36.154 | MS1 | 121.4656687094 | 31.1446208119 | 964 | 152650 | -89.67 | 5.00 | 90.45 | 0.05 | 1.62 | 956 |
| 2024-09-20 22:21:37.103 | MS1 | 121.4656651155 | 31.1446214029 | 585 | 152650 | -94.53 | 5.62 | 71.70 | 0.15 | 1.59 | 905 |
| 2024-09-20 22:21:38.190 | MS1 | 121.4656776326 | 31.1446219679 | 533 | 152650 | -92.05 | 5.80 | 94.45 | 0.12 | 1.88 | 933 |
| 2024-09-20 22:21:39.793 | MS1 | 121.4656764241 | 31.1446186378 | 203 | 152650 | -92.25 | 3.64 | 84.82 | 0.10 | 1.69 | 963 |
| 2024-09-20 22:21:40.964 | MS1 | 121.4656658977 | 31.1446278180 | 964 | 152650 | -92.18 | 5.05 | 66.13 | 0.13 | 2.77 | 1591 |
| 2024-09-20 22:21:41.605 | MS1 | 121.4656630386 | 31.1446193471 | 585 | 152650 | -87.26 | 3.42 | 91.89 | 0.11 | 2.21 | 1574 |
| 2024-09-20 22:21:42.657 | MS1 | 121.4656656518 | 31.1446336025 | 533 | 152650 | -91.75 | 2.65 | 55.49 | 0.16 | 2.53 | 1597 |

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
| 3219491 | 1 | 121.4748991140 | 31.1526965133 | 6 | 12 | 3 | 7.5 | TDD | 833 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3220838 | 11 | 121.4642804610 | 31.1491374431 | 331 | 15 | 1 | 26.9 | FDD | 203 | n1 | 152650 | 30M | 4T4R | 13 | 152650 |
| 3221118 | 9 | 121.4701618769 | 31.1499890481 | 18 | 6 | 4 | 19.9 | FDD | 580 | n1 | 152650 | 30M | 4T4R | 23 | 152650 |
| 3221807 | 12 | 121.4719336338 | 31.1534266873 | 3 | 6 | 11 | 11.0 | FDD | 533 | n1 | 152650 | 30M | 4T4R | 24 | 152650 |
| 3236840 | 6 | 121.4743326087 | 31.1460472844 | 216 | 5 | 3 | 11.8 | TDD | 621 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3243450 | 13 | 121.4688916345 | 31.1473219804 | 165 | 12 | 2 | 15.6 | FDD | 892 | n1 | 152650 | 30M | 4T4R | 11 | 152650 |
| 3244782 | 3 | 121.4710086609 | 31.1529827337 | 94 | 13 | 11 | 5.4 | TDD | 681 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3244821 | 10 | 121.4699830645 | 31.1518144608 | 316 | 8 | 2 | 19.0 | FDD | 585 | n1 | 152650 | 30M | 4T4R | 28 | 152650 |
| 3250189 | 7 | 121.4695075478 | 31.1476117514 | 170 | 11 | 3 | 27.9 | FDD | 964 | n1 | 152650 | 30M | 4T4R | 14 | 152650 |
| 3255772 | 8 | 121.4674687989 | 31.1527901793 | 223 | 11 | 0 | 20.2 | FDD | 548 | n1 | 152650 | 30M | 4T4R | 14 | 152650 |
| 3258629 | 2 | 121.4670765015 | 31.1475770218 | 121 | 2 | 7 | 1.3 | TDD | 965 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3276075 | 4 | 121.4643905722 | 31.1466491783 | 321 | 14 | 8 | 29.1 | TDD | 523 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3277209 | 5 | 121.4688412399 | 31.1458542388 | 243 | 4 | 5 | 5.8 | TDD | 780 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |

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
| 2024-09-20 22:21:30.915 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.938 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.062 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.062 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.778 | NREventA2 | measId:1;ServCellPCI:441;Se... |
| 2024-09-20 22:21:34.921 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.138 | NREventA5 | measId:3;ServCellPCI:441;Se... |
| 2024-09-20 22:21:35.173 | NRHandoverAttempt | SourcePCI:441;SourceNR-ARFC... |
| 2024-09-20 22:21:35.221 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.235 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:35.354 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.354 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3219491 | 1 | 11.1684 | 6.1474 | -115.4196 | 9.2880 | 126.1380 | 0.0180 | 0.0104 |
| 2024_09_20 22:00 | 3258629 | 2 | 19.9447 | 9.9044 | -115.1260 | 19.5143 | 93.2517 | 0.0018 | 0.0135 |
| 2024_09_20 22:00 | 3244782 | 3 | 16.5878 | 13.6115 | -116.0346 | 13.3564 | 130.6669 | 0.0061 | 0.0059 |
| 2024_09_20 22:00 | 3276075 | 4 | 7.1201 | 5.7737 | -115.1611 | 6.4143 | 80.9510 | 0.0128 | 0.0010 |
| 2024_09_20 22:00 | 3277209 | 5 | 13.2971 | 12.4171 | -114.1360 | 12.2589 | 163.0256 | 0.0032 | 0.0160 |
| 2024_09_20 22:00 | 3236840 | 6 | 8.7100 | 13.7460 | -116.9455 | 15.5245 | 131.3743 | 0.0142 | 0.0089 |
| 2024_09_20 22:00 | 3250189 | 7 | 19.9601 | 13.4122 | -117.8246 | 4.2362 | 53.7257 | 0.0083 | 0.0132 |
| 2024_09_20 22:00 | 3255772 | 8 | 11.4035 | 11.3227 | -114.1347 | 3.2353 | 37.1255 | 0.0110 | 0.0100 |
| 2024_09_20 22:00 | 3221118 | 9 | 12.5089 | 15.1867 | -116.7855 | 4.2599 | 30.1322 | 0.0134 | 0.0012 |
| 2024_09_20 22:00 | 3244821 | 10 | 15.5676 | 12.2249 | -115.7155 | 4.5483 | 30.8935 | 0.0009 | 0.0021 |
| 2024_09_20 22:00 | 3220838 | 11 | 10.7373 | 15.8168 | -114.4244 | 3.2837 | 31.6118 | 0.0068 | 0.0015 |
| 2024_09_20 22:00 | 3221807 | 12 | 14.3867 | 9.9013 | -115.6708 | 4.3345 | 52.0607 | 0.0054 | 0.0152 |
| 2024_09_20 22:00 | 3243450 | 13 | 14.5025 | 6.2243 | -115.1439 | 4.0665 | 30.6252 | 0.0120 | 0.0199 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416572_DCCAE041 | 152650 | 533 | -94.4 | 152650 | 548 | -98.5 | 152650 | 580 | -104.5 | 152650 | 892 |
| MR_1774416572_4CB7F34D | 504990 | 681 | -94.2 | 504990 | 621 | -96.0 | 504990 | 523 | -100.2 | 504990 | 965 |
| MR_1774416572_C9E08ADA | 152650 | 533 | -94.1 | 152650 | 548 | -97.6 | 152650 | 580 | -107.9 | 152650 | 892 |
| MR_1774416572_269EF43D | 152650 | 533 | -97.6 | 152650 | 548 | -99.6 | 152650 | 580 | -108.2 | 152650 | 892 |
| MR_1774416572_00B7B796 | 504990 | 681 | -95.1 | 504990 | 621 | -98.9 | 504990 | 523 | -101.9 | 504990 | 965 |
| MR_1774416572_F6E9017B | 152650 | 533 | -96.6 | 152650 | 548 | -99.6 | 152650 | 580 | -106.2 | 152650 | 892 |
| MR_1774416572_D3D57368 | 504990 | 681 | -92.0 | 504990 | 621 | -99.5 | 504990 | 523 | -100.9 | 504990 | 965 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1743: `1ff70170-32e...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `1ff70170-32e9-47f7-b484-7f36bc81eec1` |
| Tag | **single-answer** |
| 정답 | **C19** |
| C19 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3233936_2 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1743] topology](images/train_1743.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3233936_2 by 2 degrees
- `C2`: Decrease A3 Offset threshold for 3278044_3
- `C3`: Add neighbor relationship between 3233936_2 and 3278044_3
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3278044_3
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3278044_3
- `C6`: Add neighbor relationship between 3258419_1 and 3278044_3
- `C7`: Insufficient data; more data is needed for judgment.
- `C8`: Lift the tilt angle  of 3278044_3 by 4 degrees
- `C9`: Check test server and transmission issues
- `C10`: Decrease transmission power for 3233936_2
- `C11`: Adjust the azimuth of 3278044_3 by 50 degrees
- `C12`: Adjust the azimuth of 3233936_2 by 24 degrees
- `C13`: Decrease A3 Offset threshold for 3233936_2
- `C14`: Lift the tilt angle of 3233936_2 by 2 degrees
- `C15`: Decrease transmission power for 3278044_3
- `C16`: Increase transmission power for 3233936_2
- `C17`: Increase transmission power for 3278044_3
- `C18`: Increase A3 Offset threshold for 3278044_3
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3233936_2 **← 정답**
- `C20`: Increase A3 Offset threshold for 3233936_2
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3233936_2
- `C22`: Press down the tilt angle  of 3278044_3 by 4 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.347 | MS1 | 121.4656719735 | 31.1446273083 | 540 | 504990 | -90.62 | 13.72 | 561.17 | 0.18 | 2.49 | 1575 |
| 2024-09-20 22:21:32.494 | MS1 | 121.4656768414 | 31.1446262106 | 540 | 504990 | -88.08 | 13.47 | 430.20 | 0.11 | 2.54 | 1575 |
| 2024-09-20 22:21:33.752 | MS1 | 121.4656665729 | 31.1446292760 | 540 | 504990 | -86.28 | 16.22 | 357.69 | 0.06 | 2.79 | 1590 |
| 2024-09-20 22:21:34.939 | MS1 | 121.4656717040 | 31.1446322243 | 540 | 504990 | -91.21 | 14.62 | 87.11 | 0.55 | 2.48 | 602 |
| 2024-09-20 22:21:35.430 | MS1 | 121.4656749764 | 31.1446218973 | 540 | 504990 | -85.39 | 15.65 | 102.41 | 0.60 | 2.59 | 698 |
| 2024-09-20 22:21:36.260 | MS1 | 121.4656664361 | 31.1446208355 | 540 | 504990 | -88.05 | 15.44 | 75.27 | 0.62 | 2.17 | 664 |
| 2024-09-20 22:21:37.867 | MS1 | 121.4656614528 | 31.1446229948 | 540 | 504990 | -92.54 | 9.03 | 60.52 | 0.61 | 2.10 | 558 |
| 2024-09-20 22:21:38.587 | MS1 | 121.4656693512 | 31.1446318158 | 540 | 504990 | -89.28 | 9.60 | 88.99 | 0.53 | 2.80 | 555 |
| 2024-09-20 22:21:39.728 | MS1 | 121.4656643975 | 31.1446367381 | 540 | 504990 | -92.75 | 12.54 | 72.81 | 0.57 | 2.74 | 684 |
| 2024-09-20 22:21:40.192 | MS1 | 121.4656740971 | 31.1446191664 | 540 | 504990 | -90.07 | 8.17 | 553.55 | 0.06 | 2.65 | 1568 |
| 2024-09-20 22:21:41.595 | MS1 | 121.4656668406 | 31.1446235040 | 540 | 504990 | -91.66 | 12.72 | 425.33 | 0.06 | 2.88 | 1583 |
| 2024-09-20 22:21:42.743 | MS1 | 121.4656625667 | 31.1446304213 | 540 | 504990 | -89.88 | 7.06 | 422.66 | 0.00 | 2.44 | 1586 |

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
| 3233936 | 2 | 121.4728030141 | 31.1459530904 | 282 | 0 | 2 | 19.6 | TDD | 540 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3258419 | 1 | 121.4704555361 | 31.1513552408 | 99 | 3 | 5 | 24.5 | TDD | 914 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3268671 | 4 | 121.4685157344 | 31.1478834569 | 214 | 5 | 12 | 22.4 | TDD | 7 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3278044 | 3 | 121.4719811694 | 31.1527613540 | 55 | 2 | 7 | 38.4 | TDD | 1004 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |

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
| 2024-09-20 22:21:31.629 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.651 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.757 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.757 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.451 | NREventA3 | measId:2;ServCellPCI:539;Se... |
| 2024-09-20 22:21:38.691 | NRHandoverAttempt | SourcePCI:539;SourceNR-ARFC... |
| 2024-09-20 22:21:38.733 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.743 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.885 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.885 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3258419 | 1 | 7.7027 | 6.9529 | -115.2782 | 18.2542 | 140.3253 | 0.0023 | 0.0080 |
| 2024_09_20 22:00 | 3233936 | 2 | 8.2065 | 7.3671 | -114.7837 | 14.0089 | 139.4314 | 0.0018 | 0.0113 |
| 2024_09_20 22:00 | 3278044 | 3 | 9.4014 | 10.0928 | -115.5270 | 11.8033 | 106.7814 | 0.0145 | 0.0129 |
| 2024_09_20 22:00 | 3268671 | 4 | 13.1990 | 10.4860 | -115.2506 | 13.6107 | 161.4260 | 0.0117 | 0.0090 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414166_05DFFF5B | 504990 | 540 | -90.1 | 504990 | 1004 | -98.8 | 504990 | 914 | -101.2 | 504990 | 7 |
| MR_1774414166_25F265DD | 504990 | 540 | -92.3 | 504990 | 1004 | -96.7 | 504990 | 914 | -101.1 | 504990 | 7 |
| MR_1774414166_EDD6D949 | 504990 | 540 | -90.1 | 504990 | 1004 | -99.7 | 504990 | 914 | -101.8 | 504990 | 7 |
| MR_1774414166_D96D8CC1 | 504990 | 540 | -91.4 | 504990 | 1004 | -96.5 | 504990 | 914 | -100.6 | 504990 | 7 |
| MR_1774414166_41930C86 | 504990 | 540 | -92.0 | 504990 | 1004 | -97.7 | 504990 | 914 | -99.5 | 504990 | 7 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1744: `ea6b60eb-274...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `ea6b60eb-2749-4f1f-a94c-49c8ea4dea18` |
| Tag | **single-answer** |
| 정답 | **C12** |
| C12 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3243425_2 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1744] topology](images/train_1744.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3268365_5 by 6 degrees
- `C2`: Increase A3 Offset threshold for 3268365_5
- `C3`: Check test server and transmission issues
- `C4`: Add neighbor relationship between 3243425_2 and 3268365_5
- `C5`: Decrease A3 Offset threshold for 3243425_2
- `C6`: Increase transmission power for 3268365_5
- `C7`: Decrease A3 Offset threshold for 3268365_5
- `C8`: Press down the tilt angle of 3243425_2 by 6 degrees
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3268365_5
- `C10`: Decrease transmission power for 3268365_5
- `C11`: Increase transmission power for 3243425_2
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3243425_2 **← 정답**
- `C13`: Lift the tilt angle  of 3268365_5 by 6 degrees
- `C14`: Adjust the azimuth of 3243425_2 by 3 degrees
- `C15`: Adjust the azimuth of 3268365_5 by 42 degrees
- `C16`: Add neighbor relationship between 3248728_13 and 3268365_5
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3243425_2
- `C18`: Decrease transmission power for 3243425_2
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3268365_5
- `C20`: Insufficient data; more data is needed for judgment.
- `C21`: Increase A3 Offset threshold for 3243425_2
- `C22`: Lift the tilt angle of 3243425_2 by 6 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.126 | MS1 | 121.4656668172 | 31.1446187640 | 998 | 504990 | -94.42 | 15.00 | 569.37 | 0.14 | 2.05 | 1579 |
| 2024-09-20 22:21:32.873 | MS1 | 121.4656721585 | 31.1446229527 | 545 | 504990 | -94.44 | 12.44 | 305.06 | 0.15 | 2.21 | 1584 |
| 2024-09-20 22:21:33.445 | MS1 | 121.4656626473 | 31.1446219269 | 732 | 504990 | -95.15 | 10.99 | 493.58 | 0.12 | 2.63 | 1571 |
| 2024-09-20 22:21:34.418 | MS1 | 121.4656710861 | 31.1446191679 | 956 | 152650 | -88.16 | 4.70 | 53.03 | 0.13 | 1.62 | 1000 |
| 2024-09-20 22:21:35.491 | MS1 | 121.4656720833 | 31.1446334190 | 304 | 152650 | -92.05 | 3.55 | 61.85 | 0.11 | 1.86 | 953 |
| 2024-09-20 22:21:36.988 | MS1 | 121.4656604145 | 31.1446252690 | 349 | 152650 | -91.00 | 7.08 | 44.18 | 0.20 | 1.51 | 911 |
| 2024-09-20 22:21:37.724 | MS1 | 121.4656607461 | 31.1446336373 | 625 | 152650 | -93.77 | 3.83 | 64.21 | 0.16 | 1.80 | 938 |
| 2024-09-20 22:21:38.267 | MS1 | 121.4656778521 | 31.1446183920 | 956 | 152650 | -90.16 | 6.23 | 84.08 | 0.12 | 1.95 | 996 |
| 2024-09-20 22:21:39.510 | MS1 | 121.4656706688 | 31.1446341109 | 304 | 152650 | -96.40 | 5.33 | 87.29 | 0.15 | 1.81 | 953 |
| 2024-09-20 22:21:40.423 | MS1 | 121.4656655731 | 31.1446222715 | 349 | 152650 | -96.97 | 3.79 | 59.51 | 0.14 | 2.29 | 1590 |
| 2024-09-20 22:21:41.937 | MS1 | 121.4656616477 | 31.1446256206 | 625 | 152650 | -96.27 | 3.09 | 66.10 | 0.09 | 2.91 | 1588 |
| 2024-09-20 22:21:42.805 | MS1 | 121.4656609483 | 31.1446194081 | 956 | 152650 | -89.63 | 4.83 | 57.44 | 0.01 | 2.44 | 1568 |

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
| 3212646 | 10 | 121.4717599365 | 31.1469515171 | 336 | 10 | 0 | 22.5 | FDD | 625 | n1 | 152650 | 30M | 4T4R | 29 | 152650 |
| 3213480 | 6 | 121.4748542022 | 31.1467191711 | 237 | 11 | 10 | 20.7 | TDD | 732 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3216723 | 3 | 121.4696050208 | 31.1451468581 | 199 | 15 | 8 | 8.7 | TDD | 589 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3218670 | 9 | 121.4674809228 | 31.1542994135 | 66 | 0 | 6 | 26.0 | FDD | 304 | n1 | 152650 | 30M | 4T4R | 12 | 152650 |
| 3234603 | 11 | 121.4671341093 | 31.1505268082 | 69 | 3 | 12 | 26.0 | FDD | 984 | n1 | 152650 | 30M | 4T4R | 15 | 152650 |
| 3238377 | 7 | 121.4715025198 | 31.1531850884 | 278 | 10 | 11 | 5.5 | FDD | 931 | n1 | 152650 | 30M | 4T4R | 20 | 152650 |
| 3243425 | 2 | 121.4650322807 | 31.1536692713 | 180 | 5 | 12 | 9.6 | TDD | 998 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3248728 | 13 | 121.4716044025 | 31.1479007956 | 54 | 5 | 9 | 5.9 | FDD | 349 | n1 | 152650 | 30M | 4T4R | 24 | 152650 |
| 3261785 | 8 | 121.4648774619 | 31.1455579149 | 170 | 7 | 2 | 8.1 | FDD | 892 | n1 | 152650 | 30M | 4T4R | 14 | 152650 |
| 3267980 | 1 | 121.4740668511 | 31.1555103952 | 310 | 10 | 11 | 3.9 | TDD | 545 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3268177 | 4 | 121.4704344110 | 31.1462766619 | 293 | 15 | 8 | 23.2 | TDD | 783 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3268365 | 5 | 121.4725865965 | 31.1470184152 | 290 | 5 | 8 | 6.9 | TDD | 885 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3269888 | 12 | 121.4682328235 | 31.1487260163 | 166 | 12 | 6 | 17.1 | FDD | 956 | n1 | 152650 | 30M | 4T4R | 14 | 152650 |

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
| 2024-09-20 22:21:31.080 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.211 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.211 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.952 | NREventA2 | measId:1;ServCellPCI:593;Se... |
| 2024-09-20 22:21:35.073 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.329 | NREventA5 | measId:3;ServCellPCI:593;Se... |
| 2024-09-20 22:21:35.359 | NRHandoverAttempt | SourcePCI:593;SourceNR-ARFC... |
| 2024-09-20 22:21:35.401 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.416 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:35.558 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.558 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3267980 | 1 | 9.5479 | 11.9873 | -117.0301 | 18.6288 | 139.2376 | 0.0067 | 0.0183 |
| 2024_09_20 22:00 | 3243425 | 2 | 5.9532 | 18.7170 | -114.1649 | 18.5976 | 86.1899 | 0.0071 | 0.0026 |
| 2024_09_20 22:00 | 3216723 | 3 | 7.6200 | 7.2974 | -114.8847 | 8.6356 | 178.4183 | 0.0174 | 0.0167 |
| 2024_09_20 22:00 | 3268177 | 4 | 10.2810 | 17.2053 | -115.6273 | 18.2313 | 126.6763 | 0.0005 | 0.0026 |
| 2024_09_20 22:00 | 3268365 | 5 | 8.4224 | 9.4642 | -116.4522 | 16.8340 | 81.8623 | 0.0062 | 0.0104 |
| 2024_09_20 22:00 | 3213480 | 6 | 10.5074 | 14.4642 | -115.2366 | 15.3094 | 182.9480 | 0.0098 | 0.0156 |
| 2024_09_20 22:00 | 3238377 | 7 | 12.1995 | 7.3027 | -115.7338 | 4.2490 | 31.4138 | 0.0017 | 0.0077 |
| 2024_09_20 22:00 | 3261785 | 8 | 10.5704 | 6.0199 | -114.2122 | 4.6614 | 53.2362 | 0.0107 | 0.0015 |
| 2024_09_20 22:00 | 3218670 | 9 | 17.9274 | 14.9307 | -117.3598 | 3.6637 | 49.3646 | 0.0191 | 0.0175 |
| 2024_09_20 22:00 | 3212646 | 10 | 16.1455 | 13.9140 | -116.0367 | 3.3340 | 42.2066 | 0.0081 | 0.0200 |
| 2024_09_20 22:00 | 3234603 | 11 | 12.2298 | 7.7366 | -114.4776 | 4.1524 | 30.5291 | 0.0188 | 0.0186 |
| 2024_09_20 22:00 | 3269888 | 12 | 6.7752 | 13.3494 | -114.0407 | 3.9352 | 30.0856 | 0.0044 | 0.0161 |
| 2024_09_20 22:00 | 3248728 | 13 | 17.3322 | 19.6220 | -117.7976 | 4.2887 | 52.0949 | 0.0103 | 0.0180 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415213_735EE554 | 504990 | 732 | -93.5 | 504990 | 885 | -97.0 | 504990 | 589 | -97.2 | 504990 | 783 |
| MR_1774415213_57BD278B | 152650 | 956 | -87.0 | 152650 | 984 | -93.6 | 152650 | 892 | -96.6 | 152650 | 931 |
| MR_1774415213_28C33C44 | 504990 | 732 | -95.8 | 504990 | 885 | -96.5 | 504990 | 589 | -99.2 | 504990 | 783 |
| MR_1774415213_AD0A41CB | 504990 | 732 | -95.4 | 504990 | 885 | -94.5 | 504990 | 589 | -99.9 | 504990 | 783 |
| MR_1774415213_284B1F4B | 504990 | 732 | -97.1 | 504990 | 885 | -95.0 | 504990 | 589 | -99.1 | 504990 | 783 |
| MR_1774415213_4C0818AC | 504990 | 732 | -95.4 | 504990 | 885 | -96.2 | 504990 | 589 | -97.3 | 504990 | 783 |
| MR_1774415213_967F5B03 | 152650 | 956 | -89.2 | 152650 | 984 | -94.6 | 152650 | 892 | -97.7 | 152650 | 931 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1745: `e61558a0-8a9...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `e61558a0-8a98-444d-bc82-6afed2cdefe2` |
| Tag | **single-answer** |
| 정답 | **C8** |
| C8 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1745] topology](images/train_1745.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3222920_2
- `C2`: Increase transmission power for 3256780_3
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3222920_2
- `C4`: Decrease transmission power for 3222920_2
- `C5`: Press down the tilt angle of 3222920_2 by 3 degrees
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3256780_3
- `C7`: Press down the tilt angle  of 3256780_3 by 10 degrees
- `C8`: Check test server and transmission issues **← 정답**
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3256780_3
- `C10`: Lift the tilt angle of 3222920_2 by 3 degrees
- `C11`: Adjust the azimuth of 3222920_2 by 50 degrees
- `C12`: Add neighbor relationship between 3222920_2 and 3256780_3
- `C13`: Increase A3 Offset threshold for 3222920_2
- `C14`: Increase A3 Offset threshold for 3256780_3
- `C15`: Decrease A3 Offset threshold for 3256780_3
- `C16`: Add neighbor relationship between 3225812_1 and 3256780_3
- `C17`: Lift the tilt angle  of 3256780_3 by 10 degrees
- `C18`: Decrease A3 Offset threshold for 3222920_2
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3222920_2
- `C20`: Adjust the azimuth of 3256780_3 by 50 degrees
- `C21`: Insufficient data; more data is needed for judgment.
- `C22`: Decrease transmission power for 3256780_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.190 | MS1 | 121.4656616428 | 31.1446246677 | 277 | 504990 | -86.02 | 13.04 | 586.39 | 0.04 | 2.47 | 1574 |
| 2024-09-20 22:21:32.593 | MS1 | 121.4656677379 | 31.1446349910 | 277 | 504990 | -90.17 | 13.26 | 466.88 | 0.14 | 2.12 | 1570 |
| 2024-09-20 22:21:33.951 | MS1 | 121.4656643164 | 31.1446188106 | 277 | 504990 | -86.49 | 15.84 | 359.80 | 0.00 | 2.73 | 1568 |
| 2024-09-20 22:21:34.969 | MS1 | 121.4656706223 | 31.1446265858 | 277 | 504990 | -88.97 | 13.82 | 72.00 | 0.16 | 2.55 | 374 |
| 2024-09-20 22:21:35.471 | MS1 | 121.4656655671 | 31.1446307208 | 277 | 504990 | -88.14 | 16.09 | 72.50 | 0.12 | 2.37 | 409 |
| 2024-09-20 22:21:36.345 | MS1 | 121.4656598105 | 31.1446252427 | 277 | 504990 | -85.41 | 17.58 | 76.26 | 0.14 | 2.04 | 303 |
| 2024-09-20 22:21:37.838 | MS1 | 121.4656769909 | 31.1446320475 | 277 | 504990 | -93.73 | 12.63 | 75.99 | 0.09 | 2.33 | 453 |
| 2024-09-20 22:21:38.374 | MS1 | 121.4656601366 | 31.1446329610 | 277 | 504990 | -89.20 | 12.77 | 69.73 | 0.01 | 2.85 | 384 |
| 2024-09-20 22:21:39.416 | MS1 | 121.4656730767 | 31.1446257406 | 277 | 504990 | -90.11 | 10.82 | 84.65 | 0.12 | 2.12 | 365 |
| 2024-09-20 22:21:40.640 | MS1 | 121.4656671487 | 31.1446220541 | 277 | 504990 | -90.63 | 11.00 | 458.35 | 0.10 | 2.03 | 1588 |
| 2024-09-20 22:21:41.879 | MS1 | 121.4656610690 | 31.1446302913 | 277 | 504990 | -91.11 | 9.89 | 594.61 | 0.06 | 2.83 | 1581 |
| 2024-09-20 22:21:42.392 | MS1 | 121.4656586193 | 31.1446188715 | 277 | 504990 | -90.96 | 11.89 | 364.96 | 0.12 | 2.10 | 1565 |

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
| 3222920 | 2 | 121.4755421893 | 31.1504942406 | 148 | 1 | 4 | 48.1 | TDD | 277 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3225812 | 1 | 121.4724520162 | 31.1502989923 | 236 | 12 | 7 | 35.1 | TDD | 666 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3256780 | 3 | 121.4745008054 | 31.1557466641 | 27 | 15 | 6 | 36.7 | TDD | 557 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3268105 | 4 | 121.4731477359 | 31.1521823920 | 8 | 12 | 3 | 37.1 | TDD | 31 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:31.095 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.112 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.252 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.252 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.926 | NREventA3 | measId:2;ServCellPCI:934;Se... |
| 2024-09-20 22:21:38.166 | NRHandoverAttempt | SourcePCI:934;SourceNR-ARFC... |
| 2024-09-20 22:21:38.197 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.209 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.344 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.344 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3225812 | 1 | 5.9516 | 8.1834 | -117.8976 | 5.8023 | 146.0153 | 0.0124 | 0.0006 |
| 2024_09_20 22:00 | 3222920 | 2 | 15.2028 | 12.2463 | -114.0250 | 9.2981 | 156.3235 | 0.0104 | 0.0077 |
| 2024_09_20 22:00 | 3256780 | 3 | 12.8446 | 17.7036 | -114.0798 | 16.7515 | 107.2141 | 0.0102 | 0.0179 |
| 2024_09_20 22:00 | 3268105 | 4 | 18.0951 | 11.2393 | -114.9382 | 14.4872 | 116.3108 | 0.0051 | 0.0150 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416547_607096BE | 504990 | 277 | -87.3 | 504990 | 557 | -96.2 | 504990 | 666 | -96.9 | 504990 | 31 |
| MR_1774416547_F6F2AD0C | 504990 | 277 | -90.4 | 504990 | 557 | -95.0 | 504990 | 666 | -95.5 | 504990 | 31 |
| MR_1774416547_BEC35723 | 504990 | 277 | -87.4 | 504990 | 557 | -93.6 | 504990 | 666 | -95.7 | 504990 | 31 |
| MR_1774416547_24707078 | 504990 | 277 | -88.7 | 504990 | 557 | -94.0 | 504990 | 666 | -95.6 | 504990 | 31 |
| MR_1774416547_EBE50E5A | 504990 | 277 | -87.9 | 504990 | 557 | -94.2 | 504990 | 666 | -96.9 | 504990 | 31 |
| MR_1774416547_88F00054 | 504990 | 277 | -90.5 | 504990 | 557 | -96.6 | 504990 | 666 | -97.9 | 504990 | 31 |
| MR_1774416547_F45B3B29 | 504990 | 277 | -89.9 | 504990 | 557 | -96.3 | 504990 | 666 | -96.9 | 504990 | 31 |
| MR_1774416547_C0E20CCE | 504990 | 277 | -90.2 | 504990 | 557 | -94.4 | 504990 | 666 | -94.5 | 504990 | 31 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1746: `a05ed6ad-25d...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `a05ed6ad-25d7-414f-9af8-e2c48c80c4e5` |
| Tag | **single-answer** |
| 정답 | **C20** |
| C20 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3245935_1 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1746] topology](images/train_1746.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3245935_1 by 47 degrees
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3245935_1
- `C3`: Increase A3 Offset threshold for 3230735_4
- `C4`: Decrease transmission power for 3230735_4
- `C5`: Add neighbor relationship between 3245935_1 and 3230735_4
- `C6`: Insufficient data; more data is needed for judgment.
- `C7`: Decrease A3 Offset threshold for 3245935_1
- `C8`: Increase transmission power for 3245935_1
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3230735_4
- `C10`: Increase transmission power for 3230735_4
- `C11`: Press down the tilt angle of 3245935_1 by 1 degrees
- `C12`: Decrease transmission power for 3245935_1
- `C13`: Check test server and transmission issues
- `C14`: Lift the tilt angle  of 3230735_4 by 5 degrees
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3230735_4
- `C16`: Increase A3 Offset threshold for 3245935_1
- `C17`: Press down the tilt angle  of 3230735_4 by 5 degrees
- `C18`: Adjust the azimuth of 3230735_4 by 39 degrees
- `C19`: Decrease A3 Offset threshold for 3230735_4
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3245935_1 **← 정답**
- `C21`: Lift the tilt angle of 3245935_1 by 1 degrees
- `C22`: Add neighbor relationship between 3235756_7 and 3230735_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.268 | MS1 | 121.4656600741 | 31.1446340157 | 678 | 504990 | -95.80 | 10.60 | 474.60 | 0.06 | 2.70 | 1585 |
| 2024-09-20 22:21:32.842 | MS1 | 121.4656737688 | 31.1446324699 | 13 | 504990 | -95.97 | 10.76 | 552.22 | 0.16 | 2.43 | 1564 |
| 2024-09-20 22:21:33.485 | MS1 | 121.4656699294 | 31.1446216531 | 761 | 504990 | -95.72 | 13.27 | 443.23 | 0.04 | 2.88 | 1580 |
| 2024-09-20 22:21:34.724 | MS1 | 121.4656615011 | 31.1446371386 | 719 | 152650 | -95.76 | 3.13 | 75.63 | 0.17 | 1.82 | 956 |
| 2024-09-20 22:21:35.184 | MS1 | 121.4656721524 | 31.1446308633 | 317 | 152650 | -92.43 | 4.60 | 92.29 | 0.15 | 1.50 | 928 |
| 2024-09-20 22:21:36.805 | MS1 | 121.4656711533 | 31.1446222547 | 328 | 152650 | -94.22 | 4.00 | 59.03 | 0.01 | 1.97 | 906 |
| 2024-09-20 22:21:37.210 | MS1 | 121.4656720807 | 31.1446343072 | 605 | 152650 | -93.88 | 5.85 | 66.98 | 0.17 | 1.91 | 943 |
| 2024-09-20 22:21:38.129 | MS1 | 121.4656669042 | 31.1446195728 | 719 | 152650 | -92.97 | 3.75 | 88.74 | 0.10 | 1.93 | 1000 |
| 2024-09-20 22:21:39.235 | MS1 | 121.4656732715 | 31.1446352111 | 317 | 152650 | -90.77 | 6.41 | 54.85 | 0.12 | 1.62 | 936 |
| 2024-09-20 22:21:40.700 | MS1 | 121.4656653432 | 31.1446219665 | 328 | 152650 | -88.90 | 7.15 | 89.82 | 0.07 | 2.14 | 1578 |
| 2024-09-20 22:21:41.502 | MS1 | 121.4656652792 | 31.1446273062 | 605 | 152650 | -93.92 | 6.63 | 60.81 | 0.17 | 2.34 | 1563 |
| 2024-09-20 22:21:42.853 | MS1 | 121.4656759992 | 31.1446325636 | 719 | 152650 | -87.39 | 3.38 | 77.81 | 0.14 | 2.87 | 1599 |

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
| 3211102 | 10 | 121.4737856484 | 31.1555274315 | 270 | 5 | 11 | 6.3 | FDD | 317 | n1 | 152650 | 30M | 4T4R | 19 | 152650 |
| 3216290 | 13 | 121.4713551651 | 31.1507413815 | 257 | 14 | 10 | 3.4 | FDD | 255 | n1 | 152650 | 30M | 4T4R | 15 | 152650 |
| 3221088 | 2 | 121.4756780730 | 31.1469034524 | 27 | 15 | 3 | 28.6 | TDD | 13 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3227766 | 12 | 121.4732237990 | 31.1462187732 | 105 | 2 | 0 | 24.1 | FDD | 318 | n1 | 152650 | 30M | 4T4R | 14 | 152650 |
| 3230461 | 9 | 121.4682373331 | 31.1544510481 | 281 | 10 | 4 | 21.1 | FDD | 719 | n1 | 152650 | 30M | 4T4R | 23 | 152650 |
| 3230735 | 4 | 121.4684155866 | 31.1497323179 | 244 | 4 | 5 | 6.0 | TDD | 278 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3235756 | 7 | 121.4691469250 | 31.1453494668 | 234 | 14 | 10 | 20.7 | FDD | 328 | n1 | 152650 | 30M | 4T4R | 17 | 152650 |
| 3235859 | 5 | 121.4683153469 | 31.1493497226 | 359 | 11 | 2 | 1.0 | TDD | 761 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3236330 | 6 | 121.4722577188 | 31.1464675293 | 26 | 2 | 3 | 0.9 | TDD | 28 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3245935 | 1 | 121.4676898221 | 31.1546098281 | 237 | 0 | 10 | 29.3 | TDD | 678 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3246867 | 8 | 121.4681898690 | 31.1508534269 | 96 | 12 | 7 | 18.2 | FDD | 141 | n1 | 152650 | 30M | 4T4R | 22 | 152650 |
| 3249728 | 11 | 121.4720302740 | 31.1497119519 | 16 | 0 | 11 | 28.6 | FDD | 605 | n1 | 152650 | 30M | 4T4R | 20 | 152650 |
| 3275635 | 3 | 121.4702980185 | 31.1538311751 | 127 | 6 | 1 | 22.7 | TDD | 245 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |

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
| 2024-09-20 22:21:31.644 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.663 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.811 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.811 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.474 | NREventA2 | measId:1;ServCellPCI:684;Se... |
| 2024-09-20 22:21:35.587 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.873 | NREventA5 | measId:3;ServCellPCI:684;Se... |
| 2024-09-20 22:21:35.923 | NRHandoverAttempt | SourcePCI:684;SourceNR-ARFC... |
| 2024-09-20 22:21:35.950 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.965 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:36.089 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.089 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3245935 | 1 | 16.8438 | 19.5693 | -115.8735 | 8.8500 | 104.4690 | 0.0200 | 0.0091 |
| 2024_09_20 22:00 | 3221088 | 2 | 9.1992 | 9.5273 | -116.4311 | 16.8488 | 190.2196 | 0.0112 | 0.0035 |
| 2024_09_20 22:00 | 3275635 | 3 | 17.5963 | 15.8207 | -114.3746 | 9.4359 | 83.4866 | 0.0055 | 0.0080 |
| 2024_09_20 22:00 | 3230735 | 4 | 13.5205 | 18.4078 | -115.8134 | 17.2195 | 94.2028 | 0.0187 | 0.0027 |
| 2024_09_20 22:00 | 3235859 | 5 | 9.7530 | 18.9821 | -115.0624 | 9.9205 | 150.0624 | 0.0162 | 0.0181 |
| 2024_09_20 22:00 | 3236330 | 6 | 13.0537 | 6.0193 | -115.4710 | 9.7239 | 166.7747 | 0.0077 | 0.0126 |
| 2024_09_20 22:00 | 3235756 | 7 | 15.6061 | 16.6496 | -116.4231 | 4.5196 | 54.2635 | 0.0009 | 0.0187 |
| 2024_09_20 22:00 | 3246867 | 8 | 8.5422 | 16.2225 | -117.6622 | 4.4533 | 26.4276 | 0.0160 | 0.0092 |
| 2024_09_20 22:00 | 3230461 | 9 | 10.3071 | 11.5873 | -114.9152 | 4.7434 | 39.4997 | 0.0173 | 0.0173 |
| 2024_09_20 22:00 | 3211102 | 10 | 10.1922 | 12.0657 | -114.0822 | 4.5260 | 27.6681 | 0.0141 | 0.0174 |
| 2024_09_20 22:00 | 3249728 | 11 | 7.1342 | 6.5879 | -117.9861 | 3.1454 | 47.2111 | 0.0133 | 0.0176 |
| 2024_09_20 22:00 | 3227766 | 12 | 16.4227 | 19.8336 | -115.8150 | 3.6010 | 50.0422 | 0.0198 | 0.0151 |
| 2024_09_20 22:00 | 3216290 | 13 | 18.1327 | 9.1936 | -116.6762 | 3.2745 | 32.2519 | 0.0059 | 0.0002 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414532_8B8BA278 | 152650 | 719 | -94.4 | 152650 | 141 | -101.0 | 152650 | 318 | -106.8 | 152650 | 255 |
| MR_1774414532_43161090 | 152650 | 719 | -94.9 | 152650 | 141 | -98.5 | 152650 | 318 | -105.1 | 152650 | 255 |
| MR_1774414532_672920FB | 152650 | 719 | -93.9 | 152650 | 141 | -98.7 | 152650 | 318 | -105.1 | 152650 | 255 |
| MR_1774414532_BE90E246 | 152650 | 719 | -94.6 | 152650 | 141 | -100.9 | 152650 | 318 | -106.3 | 152650 | 255 |
| MR_1774414532_04C556D2 | 152650 | 719 | -94.9 | 152650 | 141 | -99.8 | 152650 | 318 | -103.6 | 152650 | 255 |
| MR_1774414532_78E05007 | 504990 | 761 | -97.0 | 504990 | 278 | -98.6 | 504990 | 245 | -97.2 | 504990 | 28 |
| MR_1774414532_A581349C | 152650 | 719 | -95.3 | 152650 | 141 | -98.6 | 152650 | 318 | -105.8 | 152650 | 255 |
| MR_1774414532_D24354A5 | 504990 | 761 | -95.1 | 504990 | 278 | -97.4 | 504990 | 245 | -100.0 | 504990 | 28 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1747: `eb8d2d92-1c5...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `eb8d2d92-1c52-4c53-820c-75dba2777d5f` |
| Tag | **single-answer** |
| 정답 | **C16** |
| C16 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3211591_2 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1747] topology](images/train_1747.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3248847_4 by 10 degrees
- `C2`: Add neighbor relationship between 3268271_3 and 3248847_4
- `C3`: Adjust the azimuth of 3248847_4 by 50 degrees
- `C4`: Increase transmission power for 3248847_4
- `C5`: Lift the tilt angle  of 3248847_4 by 10 degrees
- `C6`: Add neighbor relationship between 3211591_2 and 3248847_4
- `C7`: Press down the tilt angle of 3211591_2 by 5 degrees
- `C8`: Decrease transmission power for 3248847_4
- `C9`: Adjust the azimuth of 3211591_2 by 26 degrees
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3248847_4
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3211591_2
- `C12`: Decrease A3 Offset threshold for 3248847_4
- `C13`: Increase transmission power for 3211591_2
- `C14`: Increase A3 Offset threshold for 3248847_4
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3248847_4
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3211591_2 **← 정답**
- `C17`: Increase A3 Offset threshold for 3211591_2
- `C18`: Decrease A3 Offset threshold for 3211591_2
- `C19`: Decrease transmission power for 3211591_2
- `C20`: Check test server and transmission issues
- `C21`: Insufficient data; more data is needed for judgment.
- `C22`: Lift the tilt angle of 3211591_2 by 5 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.967 | MS1 | 121.4656691832 | 31.1446370074 | 467 | 504990 | -91.27 | 15.95 | 441.45 | 0.12 | 2.55 | 1599 |
| 2024-09-20 22:21:32.316 | MS1 | 121.4656757720 | 31.1446315817 | 467 | 504990 | -88.99 | 15.66 | 517.52 | 0.06 | 2.51 | 1582 |
| 2024-09-20 22:21:33.677 | MS1 | 121.4656611436 | 31.1446225072 | 467 | 504990 | -86.12 | 17.95 | 588.81 | 0.17 | 2.67 | 1582 |
| 2024-09-20 22:21:34.164 | MS1 | 121.4656761684 | 31.1446339847 | 467 | 504990 | -88.55 | 16.68 | 63.36 | 0.54 | 2.76 | 689 |
| 2024-09-20 22:21:35.394 | MS1 | 121.4656744915 | 31.1446280635 | 467 | 504990 | -88.22 | 12.17 | 72.00 | 0.50 | 2.80 | 512 |
| 2024-09-20 22:21:36.416 | MS1 | 121.4656722359 | 31.1446294238 | 467 | 504990 | -91.20 | 12.78 | 47.09 | 0.57 | 2.28 | 653 |
| 2024-09-20 22:21:37.518 | MS1 | 121.4656733531 | 31.1446186755 | 467 | 504990 | -89.88 | 7.07 | 87.05 | 0.56 | 2.30 | 685 |
| 2024-09-20 22:21:38.957 | MS1 | 121.4656633617 | 31.1446243962 | 467 | 504990 | -90.05 | 12.67 | 70.38 | 0.53 | 2.31 | 677 |
| 2024-09-20 22:21:39.591 | MS1 | 121.4656720095 | 31.1446208587 | 467 | 504990 | -90.61 | 9.93 | 54.06 | 0.64 | 2.46 | 612 |
| 2024-09-20 22:21:40.548 | MS1 | 121.4656762066 | 31.1446336715 | 467 | 504990 | -91.32 | 12.38 | 428.74 | 0.07 | 2.55 | 1572 |
| 2024-09-20 22:21:41.151 | MS1 | 121.4656739342 | 31.1446205570 | 467 | 504990 | -92.28 | 7.77 | 517.09 | 0.09 | 2.43 | 1600 |
| 2024-09-20 22:21:42.394 | MS1 | 121.4656765714 | 31.1446187520 | 467 | 504990 | -89.10 | 7.62 | 330.52 | 0.00 | 2.39 | 1563 |

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
| 3211591 | 2 | 121.4738748338 | 31.1473943869 | 275 | 2 | 3 | 47.5 | TDD | 467 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3230702 | 1 | 121.4645206672 | 31.1440395418 | 102 | 13 | 5 | 35.5 | TDD | 880 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3248847 | 4 | 121.4675022793 | 31.1453587895 | 130 | 10 | 4 | 17.5 | TDD | 751 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3268271 | 3 | 121.4694491288 | 31.1523913496 | 251 | 4 | 1 | 36.8 | TDD | 436 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:30.877 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:30.997 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.997 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.709 | NREventA3 | measId:2;ServCellPCI:893;Se... |
| 2024-09-20 22:21:37.949 | NRHandoverAttempt | SourcePCI:893;SourceNR-ARFC... |
| 2024-09-20 22:21:37.985 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.000 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.145 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.145 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3230702 | 1 | 9.5445 | 7.8043 | -116.5516 | 10.3938 | 197.3705 | 0.0090 | 0.0077 |
| 2024_09_20 22:00 | 3211591 | 2 | 16.7553 | 11.0980 | -115.6834 | 14.4426 | 140.4470 | 0.0022 | 0.0006 |
| 2024_09_20 22:00 | 3268271 | 3 | 5.3391 | 19.6209 | -117.0764 | 18.8321 | 158.3590 | 0.0010 | 0.0194 |
| 2024_09_20 22:00 | 3248847 | 4 | 19.5902 | 15.2059 | -114.1265 | 13.3971 | 148.3418 | 0.0169 | 0.0144 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412062_E827F048 | 504990 | 467 | -90.3 | 504990 | 751 | -91.6 | 504990 | 436 | -103.6 | 504990 | 880 |
| MR_1774412062_54565AB4 | 504990 | 467 | -87.6 | 504990 | 751 | -91.8 | 504990 | 436 | -104.5 | 504990 | 880 |
| MR_1774412062_13AA52F8 | 504990 | 467 | -89.8 | 504990 | 751 | -92.6 | 504990 | 436 | -101.6 | 504990 | 880 |
| MR_1774412062_1759556F | 504990 | 467 | -88.6 | 504990 | 751 | -92.0 | 504990 | 436 | -101.7 | 504990 | 880 |
| MR_1774412062_F92BDDF5 | 504990 | 467 | -88.5 | 504990 | 751 | -92.7 | 504990 | 436 | -102.3 | 504990 | 880 |
| MR_1774412062_288F829D | 504990 | 467 | -88.1 | 504990 | 751 | -93.4 | 504990 | 436 | -104.6 | 504990 | 880 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1748: `55742713-88b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `55742713-88b0-4c38-b3ea-94972652fcd8` |
| Tag | **single-answer** |
| 정답 | **C16** |
| C16 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1748] topology](images/train_1748.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3231245_1
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3252392_2
- `C3`: Lift the tilt angle  of 3252392_2 by 4 degrees
- `C4`: Decrease A3 Offset threshold for 3231245_1
- `C5`: Adjust the azimuth of 3252392_2 by 9 degrees
- `C6`: Adjust the azimuth of 3231245_1 by 50 degrees
- `C7`: Lift the tilt angle of 3231245_1 by 4 degrees
- `C8`: Decrease A3 Offset threshold for 3252392_2
- `C9`: Add neighbor relationship between 3231245_1 and 3252392_2
- `C10`: Increase transmission power for 3231245_1
- `C11`: Increase transmission power for 3252392_2
- `C12`: Check test server and transmission issues
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3231245_1
- `C14`: Add neighbor relationship between 3273556_4 and 3252392_2
- `C15`: Decrease transmission power for 3231245_1
- `C16`: Insufficient data; more data is needed for judgment. **← 정답**
- `C17`: Press down the tilt angle of 3231245_1 by 4 degrees
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3252392_2
- `C19`: Increase A3 Offset threshold for 3252392_2
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3231245_1
- `C21`: Press down the tilt angle  of 3252392_2 by 4 degrees
- `C22`: Decrease transmission power for 3252392_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.776 | MS1 | 121.4656694001 | 31.1446269054 | 360 | 504990 | -89.30 | 17.86 | 544.55 | 0.07 | 2.30 | 1576 |
| 2024-09-20 22:21:32.479 | MS1 | 121.4656662937 | 31.1446292007 | 360 | 504990 | -89.45 | 14.82 | 495.28 | 0.19 | 2.58 | 1571 |
| 2024-09-20 22:21:33.265 | MS1 | 121.4656716428 | 31.1446271894 | 360 | 504990 | -85.00 | 15.60 | 388.96 | 0.06 | 2.59 | 1579 |
| 2024-09-20 22:21:34.672 | MS1 | 121.4656631914 | 31.1446328564 | 360 | 504990 | -90.30 | 15.96 | 81.72 | 0.06 | 2.48 | 1567 |
| 2024-09-20 22:21:35.726 | MS1 | 121.4656671400 | 31.1446373745 | 360 | 504990 | -88.15 | 14.11 | 55.13 | 0.02 | 2.20 | 1569 |
| 2024-09-20 22:21:36.573 | MS1 | 121.4656600180 | 31.1446214234 | 360 | 504990 | -88.13 | 15.26 | 55.83 | 0.17 | 2.57 | 1590 |
| 2024-09-20 22:21:37.413 | MS1 | 121.4656676677 | 31.1446311257 | 360 | 504990 | -90.89 | 9.50 | 87.34 | 0.08 | 2.55 | 1599 |
| 2024-09-20 22:21:38.513 | MS1 | 121.4656646788 | 31.1446181312 | 360 | 504990 | -90.89 | 12.18 | 87.89 | 0.19 | 2.56 | 1596 |
| 2024-09-20 22:21:39.724 | MS1 | 121.4656654725 | 31.1446373001 | 360 | 504990 | -91.52 | 10.30 | 49.92 | 0.16 | 2.10 | 1589 |
| 2024-09-20 22:21:40.484 | MS1 | 121.4656695177 | 31.1446348042 | 360 | 504990 | -92.49 | 12.14 | 485.71 | 0.19 | 2.54 | 1578 |
| 2024-09-20 22:21:41.643 | MS1 | 121.4656699751 | 31.1446377549 | 360 | 504990 | -89.20 | 11.59 | 530.82 | 0.13 | 2.52 | 1585 |
| 2024-09-20 22:21:42.637 | MS1 | 121.4656728835 | 31.1446310901 | 360 | 504990 | -93.32 | 11.78 | 501.09 | 0.11 | 2.05 | 1596 |

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
| 3231245 | 1 | 121.4735337497 | 31.1526105206 | 64 | 2 | 6 | 44.5 | TDD | 360 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3252392 | 2 | 121.4705645419 | 31.1532185778 | 215 | 1 | 11 | 46.5 | TDD | 915 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3266795 | 3 | 121.4739130511 | 31.1556862540 | 217 | 2 | 9 | 36.4 | TDD | 516 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3273556 | 4 | 121.4749953521 | 31.1540324394 | 225 | 11 | 11 | 47.3 | TDD | 743 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:31.011 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.032 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.147 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.147 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.826 | NREventA3 | measId:2;ServCellPCI:489;Se... |
| 2024-09-20 22:21:38.066 | NRHandoverAttempt | SourcePCI:489;SourceNR-ARFC... |
| 2024-09-20 22:21:38.110 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.120 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.222 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.222 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3231245 | 1 | 80.4398 | 81.9797 | -116.9781 | 19.1147 | 88.2395 | 0.0098 | 0.0115 |
| 2024_09_19 22:00 | 3252392 | 2 | 77.4967 | 92.6252 | -115.3708 | 11.0573 | 111.4239 | 0.0131 | 0.0036 |
| 2024_09_19 22:00 | 3266795 | 3 | 87.3930 | 79.4427 | -115.0960 | 9.2367 | 88.5932 | 0.0151 | 0.0067 |
| 2024_09_19 22:00 | 3273556 | 4 | 94.5152 | 85.7116 | -114.8012 | 12.0799 | 194.5498 | 0.0146 | 0.0142 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415806_B5FC6A72 | 504990 | 360 | -88.8 | 504990 | 915 | -94.2 | 504990 | 743 | -103.0 | 504990 | 516 |
| MR_1774415806_92550D8B | 504990 | 360 | -89.0 | 504990 | 915 | -92.7 | 504990 | 743 | -103.1 | 504990 | 516 |
| MR_1774415806_3B974FDE | 504990 | 360 | -89.6 | 504990 | 915 | -94.2 | 504990 | 743 | -100.7 | 504990 | 516 |
| MR_1774415806_2269D594 | 504990 | 360 | -91.6 | 504990 | 915 | -95.3 | 504990 | 743 | -102.1 | 504990 | 516 |
| MR_1774415806_DDF666B4 | 504990 | 360 | -92.3 | 504990 | 915 | -93.1 | 504990 | 743 | -101.9 | 504990 | 516 |
| MR_1774415806_C75C4A7A | 504990 | 360 | -91.7 | 504990 | 915 | -94.7 | 504990 | 743 | -102.2 | 504990 | 516 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1749: `be087267-690...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `be087267-6905-4176-a794-91c801578d28` |
| Tag | **single-answer** |
| 정답 | **C21** |
| C21 의미 | Lift the tilt angle  of 3258725_2 by 6 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1749] topology](images/train_1749.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3240413_3
- `C2`: Decrease transmission power for 3240413_3
- `C3`: Press down the tilt angle  of 3258725_2 by 6 degrees
- `C4`: Increase transmission power for 3240413_3
- `C5`: Insufficient data; more data is needed for judgment.
- `C6`: Increase A3 Offset threshold for 3237635_1
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3240413_3
- `C8`: Increase transmission power for 3237635_1
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3240413_3
- `C10`: Decrease transmission power for 3237635_1
- `C11`: Add neighbor relationship between 3258725_2 and 3240413_3
- `C12`: Press down the tilt angle of 3237635_1 by 4 degrees
- `C13`: Add neighbor relationship between 3237635_1 and 3240413_3
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3237635_1
- `C15`: Check test server and transmission issues
- `C16`: Decrease A3 Offset threshold for 3237635_1
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3237635_1
- `C18`: Adjust the azimuth of 3237635_1 by 14 degrees
- `C19`: Increase A3 Offset threshold for 3240413_3
- `C20`: Adjust the azimuth of 3258725_2 by 50 degrees
- `C21`: Lift the tilt angle  of 3258725_2 by 6 degrees **← 정답**
- `C22`: Lift the tilt angle of 3237635_1 by 4 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.872 | MS1 | 121.4656711153 | 31.1446262367 | 610 | 504990 | -88.13 | 12.12 | 411.63 | 0.04 | 2.24 | 1592 |
| 2024-09-20 22:21:32.665 | MS1 | 121.4656729308 | 31.1446274807 | 610 | 504990 | -90.35 | 16.77 | 372.29 | 0.19 | 2.01 | 1592 |
| 2024-09-20 22:21:33.253 | MS1 | 121.4656594500 | 31.1446238646 | 610 | 504990 | -89.23 | 15.77 | 539.56 | 0.00 | 2.53 | 1594 |
| 2024-09-20 22:21:34.802 | MS1 | 121.4656591340 | 31.1446267548 | 610 | 504990 | -89.89 | 15.36 | 69.96 | 0.10 | 2.54 | 1572 |
| 2024-09-20 22:21:35.634 | MS1 | 121.4656678812 | 31.1446203185 | 610 | 504990 | -88.02 | 17.41 | 68.17 | 0.08 | 2.37 | 1568 |
| 2024-09-20 22:21:36.514 | MS1 | 121.4656777129 | 31.1446228585 | 610 | 504990 | -85.90 | 14.73 | 73.69 | 0.03 | 2.78 | 1593 |
| 2024-09-20 22:21:37.916 | MS1 | 121.4656773445 | 31.1446187087 | 610 | 504990 | -89.06 | 10.97 | 77.17 | 0.14 | 2.28 | 1562 |
| 2024-09-20 22:21:38.569 | MS1 | 121.4656717921 | 31.1446309561 | 610 | 504990 | -93.39 | 12.77 | 49.76 | 0.13 | 2.44 | 1586 |
| 2024-09-20 22:21:39.218 | MS1 | 121.4656732234 | 31.1446379761 | 610 | 504990 | -90.97 | 8.02 | 67.48 | 0.10 | 2.20 | 1580 |
| 2024-09-20 22:21:40.758 | MS1 | 121.4656591871 | 31.1446239072 | 610 | 504990 | -92.87 | 8.92 | 401.83 | 0.08 | 2.90 | 1568 |
| 2024-09-20 22:21:41.783 | MS1 | 121.4656719889 | 31.1446299318 | 610 | 504990 | -93.62 | 11.92 | 528.95 | 0.10 | 2.77 | 1565 |
| 2024-09-20 22:21:42.860 | MS1 | 121.4656718405 | 31.1446279542 | 610 | 504990 | -91.06 | 8.71 | 590.15 | 0.06 | 2.30 | 1572 |

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
| 3229813 | 4 | 121.4675584739 | 31.1522789703 | 35 | 9 | 8 | 46.1 | TDD | 359 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3237635 | 1 | 121.4676485376 | 31.1543455573 | 204 | 2 | 10 | 40.7 | TDD | 610 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3240413 | 3 | 121.4709191900 | 31.1558128767 | 16 | 5 | 0 | 23.9 | TDD | 106 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3258725 | 2 | 121.4731435042 | 31.1527344781 | 81 | 13 | 3 | 41.4 | TDD | 103 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |

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
| 2024-09-20 22:21:31.073 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.093 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.206 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.206 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.895 | NREventA3 | measId:2;ServCellPCI:251;Se... |
| 2024-09-20 22:21:38.135 | NRHandoverAttempt | SourcePCI:251;SourceNR-ARFC... |
| 2024-09-20 22:21:38.179 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.191 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.304 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.304 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3237635 | 1 | 86.4365 | 92.9901 | -116.1775 | 9.6352 | 98.0859 | 0.0119 | 0.0100 |
| 2024_09_20 22:00 | 3258725 | 2 | 11.0861 | 5.8822 | -117.4275 | 9.5692 | 199.5170 | 0.0165 | 0.0169 |
| 2024_09_20 22:00 | 3240413 | 3 | 16.7122 | 18.5247 | -114.2173 | 11.1827 | 120.6758 | 0.0002 | 0.0136 |
| 2024_09_20 22:00 | 3229813 | 4 | 12.1478 | 8.1068 | -116.6767 | 19.7614 | 122.1316 | 0.0077 | 0.0129 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412650_285B1163 | 504990 | 610 | -90.4 | 504990 | 106 | -93.5 | 504990 | 103 | -102.4 | 504990 | 359 |
| MR_1774412650_25FE7EBD | 504990 | 610 | -90.6 | 504990 | 106 | -94.5 | 504990 | 103 | -100.0 | 504990 | 359 |
| MR_1774412650_5D48DF64 | 504990 | 610 | -90.6 | 504990 | 106 | -94.7 | 504990 | 103 | -99.4 | 504990 | 359 |
| MR_1774412650_FA20B147 | 504990 | 610 | -88.9 | 504990 | 106 | -92.6 | 504990 | 103 | -99.3 | 504990 | 359 |
| MR_1774412650_DCAF6BD4 | 504990 | 610 | -91.6 | 504990 | 106 | -92.2 | 504990 | 103 | -100.1 | 504990 | 359 |
| MR_1774412650_D776C677 | 504990 | 610 | -90.8 | 504990 | 106 | -91.1 | 504990 | 103 | -102.5 | 504990 | 359 |
| MR_1774412650_579E9A57 | 504990 | 610 | -90.1 | 504990 | 106 | -95.1 | 504990 | 103 | -103.1 | 504990 | 359 |
| MR_1774412650_91DB0523 | 504990 | 610 | -91.8 | 504990 | 106 | -91.4 | 504990 | 103 | -100.4 | 504990 | 359 |

> *... 2개 열 생략 (전체 14열)*

---
