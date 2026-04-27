# Track A 문제 분석 — train[540]~train[549]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[540] ~ train[549] (10개)

## 목차

1. [문제 540: `4166ff67-829...`](#540) — single-answer, 정답: C4
2. [문제 541: `a340366d-ba6...`](#541) — single-answer, 정답: C11
3. [문제 542: `59993d5c-5fc...`](#542) — single-answer, 정답: C20
4. [문제 543: `55c920f9-05d...`](#543) — single-answer, 정답: C15
5. [문제 544: `6f0f12fd-06c...`](#544) — single-answer, 정답: C15
6. [문제 545: `3b31d709-cfa...`](#545) — single-answer, 정답: C4
7. [문제 546: `905b5148-d76...`](#546) — single-answer, 정답: C6
8. [문제 547: `11859700-814...`](#547) — single-answer, 정답: C13
9. [문제 548: `418c3a81-d4d...`](#548) — single-answer, 정답: C3
10. [문제 549: `99b976b3-6c6...`](#549) — single-answer, 정답: C2

---

### 문제 540: `4166ff67-829...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `4166ff67-829b-4ba2-8870-287f4a659dc7` |
| Tag | **single-answer** |
| 정답 | **C4** |
| C4 의미 | Lift the tilt angle  of 3269027_2 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[540] topology](images/train_0540.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3269027_2 by 50 degrees
- `C2`: Lift the tilt angle of 3276252_1 by 1 degrees
- `C3`: Press down the tilt angle of 3276252_1 by 1 degrees
- `C4`: Lift the tilt angle  of 3269027_2 by 10 degrees **← 정답**
- `C5`: Add neighbor relationship between 3276252_1 and 3272510_3
- `C6`: Decrease transmission power for 3276252_1
- `C7`: Decrease transmission power for 3272510_3
- `C8`: Increase transmission power for 3276252_1
- `C9`: Decrease A3 Offset threshold for 3272510_3
- `C10`: Insufficient data; more data is needed for judgment.
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3276252_1
- `C12`: Check test server and transmission issues
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3272510_3
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3272510_3
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3276252_1
- `C16`: Press down the tilt angle  of 3269027_2 by 10 degrees
- `C17`: Add neighbor relationship between 3269027_2 and 3272510_3
- `C18`: Increase A3 Offset threshold for 3272510_3
- `C19`: Increase A3 Offset threshold for 3276252_1
- `C20`: Increase transmission power for 3272510_3
- `C21`: Adjust the azimuth of 3276252_1 by 6 degrees
- `C22`: Decrease A3 Offset threshold for 3276252_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.373 | MS1 | 121.4656693678 | 31.1446226273 | 422 | 504990 | -91.51 | 17.99 | 557.58 | 0.12 | 2.87 | 1569 |
| 2024-09-20 22:21:32.808 | MS1 | 121.4656726303 | 31.1446263849 | 422 | 504990 | -91.59 | 14.96 | 360.42 | 0.14 | 2.15 | 1574 |
| 2024-09-20 22:21:33.777 | MS1 | 121.4656653629 | 31.1446360827 | 422 | 504990 | -87.60 | 17.03 | 483.50 | 0.14 | 2.84 | 1588 |
| 2024-09-20 22:21:34.238 | MS1 | 121.4656709656 | 31.1446215701 | 422 | 504990 | -89.38 | 15.72 | 64.05 | 0.09 | 2.65 | 1581 |
| 2024-09-20 22:21:35.684 | MS1 | 121.4656608455 | 31.1446187705 | 422 | 504990 | -90.76 | 13.86 | 73.53 | 0.06 | 2.72 | 1592 |
| 2024-09-20 22:21:36.350 | MS1 | 121.4656622745 | 31.1446189492 | 422 | 504990 | -86.89 | 12.75 | 55.31 | 0.15 | 2.20 | 1569 |
| 2024-09-20 22:21:37.177 | MS1 | 121.4656736159 | 31.1446325921 | 422 | 504990 | -92.68 | 12.25 | 80.98 | 0.02 | 2.83 | 1577 |
| 2024-09-20 22:21:38.746 | MS1 | 121.4656657035 | 31.1446325581 | 422 | 504990 | -93.01 | 7.57 | 91.28 | 0.16 | 2.07 | 1597 |
| 2024-09-20 22:21:39.671 | MS1 | 121.4656605711 | 31.1446334859 | 422 | 504990 | -92.54 | 11.92 | 72.36 | 0.17 | 2.51 | 1560 |
| 2024-09-20 22:21:40.889 | MS1 | 121.4656702696 | 31.1446300562 | 422 | 504990 | -92.13 | 9.89 | 466.03 | 0.11 | 2.30 | 1599 |
| 2024-09-20 22:21:41.443 | MS1 | 121.4656694527 | 31.1446251960 | 422 | 504990 | -93.65 | 10.31 | 462.01 | 0.05 | 2.68 | 1587 |
| 2024-09-20 22:21:42.450 | MS1 | 121.4656622351 | 31.1446289576 | 422 | 504990 | -89.55 | 10.28 | 394.37 | 0.19 | 2.43 | 1579 |

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
| 3216649 | 4 | 121.4758664652 | 31.1450251829 | 1 | 15 | 11 | 28.5 | TDD | 382 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3269027 | 2 | 121.4660933494 | 31.1444344395 | 165 | 4 | 9 | 23.7 | TDD | 276 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3272510 | 3 | 121.4687589666 | 31.1447694572 | 151 | 5 | 6 | 39.9 | TDD | 837 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3276252 | 1 | 121.4722924912 | 31.1533623746 | 207 | 0 | 0 | 17.1 | TDD | 422 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |

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
| 2024-09-20 22:21:31.574 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.596 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.732 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.732 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.409 | NREventA3 | measId:2;ServCellPCI:716;Se... |
| 2024-09-20 22:21:38.649 | NRHandoverAttempt | SourcePCI:716;SourceNR-ARFC... |
| 2024-09-20 22:21:38.684 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.697 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.824 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.824 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3276252 | 1 | 80.2393 | 91.5211 | -117.0639 | 10.7379 | 91.6616 | 0.0039 | 0.0094 |
| 2024_09_20 22:00 | 3269027 | 2 | 18.8424 | 17.0535 | -117.8347 | 7.0042 | 193.1818 | 0.0021 | 0.0133 |
| 2024_09_20 22:00 | 3272510 | 3 | 13.3853 | 15.4690 | -114.4695 | 10.6551 | 110.3933 | 0.0122 | 0.0129 |
| 2024_09_20 22:00 | 3216649 | 4 | 7.4044 | 16.9101 | -115.4534 | 12.5936 | 150.0486 | 0.0143 | 0.0147 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416972_D38E9E57 | 504990 | 422 | -90.0 | 504990 | 837 | -91.3 | 504990 | 276 | -99.8 | 504990 | 382 |
| MR_1774416972_F8A57B57 | 504990 | 422 | -90.0 | 504990 | 837 | -91.2 | 504990 | 276 | -99.0 | 504990 | 382 |
| MR_1774416972_606AAB86 | 504990 | 422 | -90.3 | 504990 | 837 | -93.3 | 504990 | 276 | -102.2 | 504990 | 382 |
| MR_1774416972_EE95F808 | 504990 | 422 | -89.1 | 504990 | 837 | -90.2 | 504990 | 276 | -100.5 | 504990 | 382 |
| MR_1774416972_F6BF2ADB | 504990 | 422 | -89.7 | 504990 | 837 | -90.7 | 504990 | 276 | -98.5 | 504990 | 382 |
| MR_1774416972_AFD64E1A | 504990 | 422 | -88.2 | 504990 | 837 | -93.8 | 504990 | 276 | -99.0 | 504990 | 382 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 541: `a340366d-ba6...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `a340366d-ba65-4624-9645-f11b4deb8ead` |
| Tag | **single-answer** |
| 정답 | **C11** |
| C11 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[541] topology](images/train_0541.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3211878_1
- `C2`: Lift the tilt angle of 3269822_3 by 10 degrees
- `C3`: Increase A3 Offset threshold for 3269822_3
- `C4`: Check test server and transmission issues
- `C5`: Increase transmission power for 3269822_3
- `C6`: Decrease transmission power for 3269822_3
- `C7`: Increase A3 Offset threshold for 3211878_1
- `C8`: Adjust the azimuth of 3211878_1 by 50 degrees
- `C9`: Decrease A3 Offset threshold for 3211878_1
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3269822_3
- `C11`: Insufficient data; more data is needed for judgment. **← 정답**
- `C12`: Add neighbor relationship between 3252373_2 and 3211878_1
- `C13`: Increase transmission power for 3211878_1
- `C14`: Decrease A3 Offset threshold for 3269822_3
- `C15`: Lift the tilt angle  of 3211878_1 by 6 degrees
- `C16`: Decrease transmission power for 3211878_1
- `C17`: Adjust the azimuth of 3269822_3 by 50 degrees
- `C18`: Press down the tilt angle  of 3211878_1 by 6 degrees
- `C19`: Add neighbor relationship between 3269822_3 and 3211878_1
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3269822_3
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3211878_1
- `C22`: Press down the tilt angle of 3269822_3 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.344 | MS1 | 121.4656712995 | 31.1446181329 | 6 | 504990 | -90.63 | 15.05 | 502.04 | 0.11 | 2.41 | 1573 |
| 2024-09-20 22:21:32.536 | MS1 | 121.4656694117 | 31.1446308346 | 6 | 504990 | -88.90 | 12.48 | 436.35 | 0.11 | 2.13 | 1588 |
| 2024-09-20 22:21:33.394 | MS1 | 121.4656702387 | 31.1446287920 | 6 | 504990 | -85.63 | 17.95 | 554.54 | 0.17 | 2.19 | 1591 |
| 2024-09-20 22:21:34.871 | MS1 | 121.4656666016 | 31.1446208799 | 6 | 504990 | -87.47 | 15.59 | 53.61 | 0.09 | 2.26 | 1591 |
| 2024-09-20 22:21:35.470 | MS1 | 121.4656683675 | 31.1446268991 | 6 | 504990 | -85.14 | 17.17 | 69.66 | 0.11 | 2.10 | 1562 |
| 2024-09-20 22:21:36.227 | MS1 | 121.4656690895 | 31.1446230345 | 6 | 504990 | -91.35 | 16.22 | 65.63 | 0.15 | 2.90 | 1596 |
| 2024-09-20 22:21:37.249 | MS1 | 121.4656748830 | 31.1446243034 | 6 | 504990 | -91.45 | 12.39 | 79.15 | 0.09 | 2.83 | 1566 |
| 2024-09-20 22:21:38.862 | MS1 | 121.4656632999 | 31.1446358555 | 6 | 504990 | -90.77 | 12.80 | 65.72 | 0.11 | 2.15 | 1586 |
| 2024-09-20 22:21:39.919 | MS1 | 121.4656647288 | 31.1446230229 | 6 | 504990 | -90.97 | 9.90 | 97.99 | 0.09 | 2.55 | 1563 |
| 2024-09-20 22:21:40.459 | MS1 | 121.4656593786 | 31.1446376548 | 6 | 504990 | -92.20 | 12.32 | 497.52 | 0.01 | 2.04 | 1598 |
| 2024-09-20 22:21:41.596 | MS1 | 121.4656733131 | 31.1446372300 | 6 | 504990 | -92.29 | 7.18 | 321.52 | 0.10 | 2.43 | 1575 |
| 2024-09-20 22:21:42.175 | MS1 | 121.4656749088 | 31.1446207803 | 6 | 504990 | -90.50 | 7.38 | 579.59 | 0.03 | 2.00 | 1595 |

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
| 3211878 | 1 | 121.4640701109 | 31.1536135627 | 80 | 4 | 1 | 43.1 | TDD | 60 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3252373 | 2 | 121.4658095895 | 31.1526121253 | 21 | 2 | 5 | 29.3 | TDD | 31 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3269822 | 3 | 121.4702380968 | 31.1475964884 | 344 | 8 | 6 | 36.5 | TDD | 6 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3279543 | 4 | 121.4737535373 | 31.1515706327 | 53 | 8 | 4 | 32.6 | TDD | 471 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |

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
| 2024-09-20 22:21:31.131 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.150 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.271 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.271 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.959 | NREventA3 | measId:2;ServCellPCI:125;Se... |
| 2024-09-20 22:21:38.199 | NRHandoverAttempt | SourcePCI:125;SourceNR-ARFC... |
| 2024-09-20 22:21:38.233 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.244 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.356 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.356 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3211878 | 1 | 79.9277 | 87.2849 | -115.2782 | 7.3871 | 119.2673 | 0.0002 | 0.0129 |
| 2024_09_19 22:00 | 3252373 | 2 | 92.2770 | 89.8193 | -115.4509 | 16.0166 | 108.6955 | 0.0045 | 0.0199 |
| 2024_09_19 22:00 | 3269822 | 3 | 90.4981 | 83.9618 | -115.5734 | 14.4870 | 94.0078 | 0.0146 | 0.0023 |
| 2024_09_19 22:00 | 3279543 | 4 | 81.1378 | 92.5125 | -114.9683 | 8.1809 | 159.3967 | 0.0048 | 0.0072 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412924_74CABACF | 504990 | 6 | -85.7 | 504990 | 60 | -89.0 | 504990 | 31 | -100.9 | 504990 | 471 |
| MR_1774412924_50B63E0B | 504990 | 6 | -86.8 | 504990 | 60 | -85.8 | 504990 | 31 | -101.5 | 504990 | 471 |
| MR_1774412924_95709FE8 | 504990 | 6 | -87.9 | 504990 | 60 | -87.5 | 504990 | 31 | -100.2 | 504990 | 471 |
| MR_1774412924_9EF72B0C | 504990 | 6 | -85.8 | 504990 | 60 | -85.1 | 504990 | 31 | -99.2 | 504990 | 471 |
| MR_1774412924_88350958 | 504990 | 6 | -87.9 | 504990 | 60 | -86.0 | 504990 | 31 | -99.4 | 504990 | 471 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 542: `59993d5c-5fc...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `59993d5c-5fcc-4b7f-b1a9-5874906992ec` |
| Tag | **single-answer** |
| 정답 | **C20** |
| C20 의미 | Decrease A3 Offset threshold for 3274954_1 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[542] topology](images/train_0542.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3274954_1
- `C2`: Lift the tilt angle  of 3210349_3 by 10 degrees
- `C3`: Insufficient data; more data is needed for judgment.
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3210349_3
- `C5`: Decrease transmission power for 3274954_1
- `C6`: Increase transmission power for 3274954_1
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3274954_1
- `C8`: Increase A3 Offset threshold for 3210349_3
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3210349_3
- `C10`: Add neighbor relationship between 3268716_4 and 3210349_3
- `C11`: Adjust the azimuth of 3210349_3 by 41 degrees
- `C12`: Increase transmission power for 3210349_3
- `C13`: Press down the tilt angle  of 3210349_3 by 10 degrees
- `C14`: Lift the tilt angle of 3274954_1 by 4 degrees
- `C15`: Press down the tilt angle of 3274954_1 by 4 degrees
- `C16`: Add neighbor relationship between 3274954_1 and 3210349_3
- `C17`: Adjust the azimuth of 3274954_1 by 50 degrees
- `C18`: Check test server and transmission issues
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3274954_1
- `C20`: Decrease A3 Offset threshold for 3274954_1 **← 정답**
- `C21`: Decrease A3 Offset threshold for 3210349_3
- `C22`: Decrease transmission power for 3210349_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.234 | MS1 | 121.4656610034 | 31.1446313199 | 210 | 504990 | -79.29 | 16.82 | 340.19 | 0.04 | 2.26 | 1582 |
| 2024-09-20 22:21:32.782 | MS1 | 121.4656633915 | 31.1446302096 | 210 | 504990 | -79.98 | 16.18 | 342.45 | 0.09 | 2.91 | 1600 |
| 2024-09-20 22:21:33.681 | MS1 | 121.4656640742 | 31.1446282595 | 210 | 504990 | -81.77 | 15.05 | 495.25 | 0.15 | 2.58 | 1593 |
| 2024-09-20 22:21:34.245 | MS1 | 121.4656656868 | 31.1446348659 | 210 | 504990 | -85.17 | -3.14 | 64.43 | 0.06 | 1.11 | 1570 |
| 2024-09-20 22:21:35.770 | MS1 | 121.4656646076 | 31.1446180042 | 210 | 504990 | -84.48 | -2.10 | 41.84 | 0.19 | 1.33 | 1599 |
| 2024-09-20 22:21:36.134 | MS1 | 121.4656594827 | 31.1446266546 | 210 | 504990 | -88.01 | -3.72 | 40.80 | 0.18 | 1.50 | 1570 |
| 2024-09-20 22:21:37.632 | MS1 | 121.4656625925 | 31.1446278919 | 210 | 504990 | -91.79 | -1.29 | 35.20 | 0.02 | 1.04 | 1582 |
| 2024-09-20 22:21:38.437 | MS1 | 121.4656649879 | 31.1446340737 | 210 | 504990 | -91.75 | -3.14 | 46.88 | 0.02 | 1.30 | 1562 |
| 2024-09-20 22:21:39.128 | MS1 | 121.4656649288 | 31.1446252606 | 277 | 504990 | -83.98 | 14.93 | 216.46 | 0.15 | 1.08 | 1579 |
| 2024-09-20 22:21:40.179 | MS1 | 121.4656650034 | 31.1446251063 | 277 | 504990 | -77.73 | 17.21 | 355.17 | 0.08 | 2.87 | 1588 |
| 2024-09-20 22:21:41.885 | MS1 | 121.4656663726 | 31.1446303575 | 277 | 504990 | -84.09 | 16.10 | 496.20 | 0.05 | 2.05 | 1587 |
| 2024-09-20 22:21:42.616 | MS1 | 121.4656654123 | 31.1446371918 | 277 | 504990 | -76.75 | 17.87 | 379.96 | 0.18 | 2.00 | 1561 |

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
| 3210349 | 3 | 121.4677926948 | 31.1443663902 | 237 | 8 | 12 | 45.6 | TDD | 277 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3268716 | 4 | 121.4726939424 | 31.1441097750 | 124 | 9 | 12 | 48.0 | TDD | 941 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3273610 | 2 | 121.4644490432 | 31.1442712333 | 230 | 5 | 12 | 28.3 | TDD | 812 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3274954 | 1 | 121.4752144869 | 31.1440648079 | 30 | 3 | 0 | 21.2 | TDD | 210 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:30.998 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.018 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.153 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.153 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.817 | NREventA3 | measId:2;ServCellPCI:341;Se... |
| 2024-09-20 22:21:38.057 | NRHandoverAttempt | SourcePCI:341;SourceNR-ARFC... |
| 2024-09-20 22:21:38.094 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.105 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.205 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.205 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3274954 | 1 | 18.0910 | 16.3935 | -115.4748 | 8.5882 | 160.9528 | 0.0049 | 0.1396 |
| 2024_09_20 22:00 | 3273610 | 2 | 9.7324 | 5.4955 | -115.5109 | 16.5371 | 96.4857 | 0.0175 | 0.0181 |
| 2024_09_20 22:00 | 3210349 | 3 | 13.5267 | 14.2695 | -116.6215 | 18.6420 | 153.5520 | 0.0006 | 0.0155 |
| 2024_09_20 22:00 | 3268716 | 4 | 10.9666 | 18.6549 | -116.7878 | 7.4822 | 123.6227 | 0.0053 | 0.0025 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413585_44244D43 | 504990 | 277 | -79.1 | 504990 | 210 | -83.5 | 504990 | 941 | -78.2 | 504990 | 812 |
| MR_1774413585_54A00A9B | 504990 | 210 | -85.7 | 504990 | 277 | -78.6 | 504990 | 941 | -81.2 | 504990 | 812 |
| MR_1774413585_42F17B60 | 504990 | 277 | -81.2 | 504990 | 210 | -86.6 | 504990 | 941 | -79.7 | 504990 | 812 |
| MR_1774413585_DC5AAD50 | 504990 | 277 | -81.1 | 504990 | 210 | -86.6 | 504990 | 941 | -81.4 | 504990 | 812 |
| MR_1774413585_19146AAD | 504990 | 210 | -85.7 | 504990 | 277 | -78.7 | 504990 | 941 | -79.5 | 504990 | 812 |
| MR_1774413585_B89C3538 | 504990 | 277 | -80.7 | 504990 | 210 | -84.3 | 504990 | 941 | -80.9 | 504990 | 812 |
| MR_1774413585_EFD353FB | 504990 | 210 | -84.4 | 504990 | 277 | -78.9 | 504990 | 941 | -79.7 | 504990 | 812 |
| MR_1774413585_A857FDCA | 504990 | 210 | -84.4 | 504990 | 277 | -78.8 | 504990 | 941 | -80.6 | 504990 | 812 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 543: `55c920f9-05d...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `55c920f9-05da-45ee-b3fb-b1c99e8f0eef` |
| Tag | **single-answer** |
| 정답 | **C15** |
| C15 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3278170_2 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[543] topology](images/train_0543.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle  of 3230901_1 by 5 degrees
- `C2`: Add neighbor relationship between 3278170_2 and 3230901_1
- `C3`: Increase A3 Offset threshold for 3230901_1
- `C4`: Press down the tilt angle of 3278170_2 by 1 degrees
- `C5`: Increase A3 Offset threshold for 3278170_2
- `C6`: Decrease A3 Offset threshold for 3278170_2
- `C7`: Add neighbor relationship between 3224759_12 and 3230901_1
- `C8`: Check test server and transmission issues
- `C9`: Decrease A3 Offset threshold for 3230901_1
- `C10`: Decrease transmission power for 3230901_1
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3230901_1
- `C12`: Adjust the azimuth of 3278170_2 by 25 degrees
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3278170_2
- `C14`: Lift the tilt angle of 3278170_2 by 1 degrees
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3278170_2 **← 정답**
- `C16`: Insufficient data; more data is needed for judgment.
- `C17`: Adjust the azimuth of 3230901_1 by 43 degrees
- `C18`: Increase transmission power for 3230901_1
- `C19`: Decrease transmission power for 3278170_2
- `C20`: Increase transmission power for 3278170_2
- `C21`: Press down the tilt angle  of 3230901_1 by 5 degrees
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3230901_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.249 | MS1 | 121.4656682915 | 31.1446291805 | 962 | 504990 | -94.77 | 13.34 | 552.51 | 0.05 | 2.30 | 1589 |
| 2024-09-20 22:21:32.285 | MS1 | 121.4656734789 | 31.1446327019 | 252 | 504990 | -93.49 | 12.25 | 457.66 | 0.02 | 2.23 | 1561 |
| 2024-09-20 22:21:33.867 | MS1 | 121.4656729905 | 31.1446326845 | 278 | 504990 | -94.37 | 13.23 | 571.40 | 0.15 | 2.23 | 1586 |
| 2024-09-20 22:21:34.896 | MS1 | 121.4656646396 | 31.1446378944 | 865 | 152650 | -94.91 | 6.56 | 51.21 | 0.19 | 1.61 | 952 |
| 2024-09-20 22:21:35.646 | MS1 | 121.4656602686 | 31.1446309616 | 145 | 152650 | -96.68 | 5.13 | 75.56 | 0.02 | 1.58 | 918 |
| 2024-09-20 22:21:36.765 | MS1 | 121.4656777531 | 31.1446365986 | 951 | 152650 | -94.53 | 5.96 | 52.12 | 0.15 | 1.84 | 955 |
| 2024-09-20 22:21:37.224 | MS1 | 121.4656652018 | 31.1446217288 | 588 | 152650 | -87.01 | 2.28 | 72.47 | 0.17 | 1.88 | 903 |
| 2024-09-20 22:21:38.164 | MS1 | 121.4656610865 | 31.1446312497 | 865 | 152650 | -94.54 | 5.36 | 61.81 | 0.15 | 1.77 | 943 |
| 2024-09-20 22:21:39.768 | MS1 | 121.4656664624 | 31.1446332199 | 145 | 152650 | -90.16 | 2.84 | 82.37 | 0.07 | 1.65 | 934 |
| 2024-09-20 22:21:40.156 | MS1 | 121.4656599648 | 31.1446265032 | 951 | 152650 | -89.39 | 3.25 | 63.42 | 0.17 | 2.42 | 1569 |
| 2024-09-20 22:21:41.760 | MS1 | 121.4656645984 | 31.1446356666 | 588 | 152650 | -88.20 | 2.94 | 52.85 | 0.05 | 2.43 | 1576 |
| 2024-09-20 22:21:42.500 | MS1 | 121.4656656276 | 31.1446190043 | 865 | 152650 | -95.88 | 7.02 | 64.49 | 0.12 | 2.43 | 1599 |

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
| 3223006 | 10 | 121.4736006298 | 31.1542403798 | 92 | 14 | 11 | 27.8 | FDD | 588 | n1 | 152650 | 30M | 4T4R | 12 | 152650 |
| 3223014 | 7 | 121.4755270987 | 31.1443635487 | 164 | 0 | 2 | 26.1 | FDD | 865 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |
| 3224759 | 12 | 121.4718800921 | 31.1467862494 | 127 | 13 | 4 | 6.5 | FDD | 951 | n1 | 152650 | 30M | 4T4R | 28 | 152650 |
| 3226349 | 8 | 121.4693342448 | 31.1469399301 | 143 | 6 | 10 | 15.3 | FDD | 872 | n1 | 152650 | 30M | 4T4R | 17 | 152650 |
| 3227089 | 4 | 121.4668552055 | 31.1450677667 | 235 | 5 | 6 | 25.0 | TDD | 278 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3228067 | 9 | 121.4692213400 | 31.1538115798 | 98 | 12 | 8 | 14.1 | FDD | 460 | n1 | 152650 | 30M | 4T4R | 23 | 152650 |
| 3230901 | 1 | 121.4757225493 | 31.1555590441 | 175 | 4 | 10 | 24.3 | TDD | 736 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3247937 | 5 | 121.4713002961 | 31.1446333148 | 221 | 5 | 2 | 24.4 | TDD | 571 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3251609 | 6 | 121.4650589493 | 31.1492633189 | 325 | 1 | 6 | 27.4 | TDD | 252 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3258997 | 11 | 121.4717706472 | 31.1459436434 | 350 | 12 | 1 | 22.0 | FDD | 145 | n1 | 152650 | 30M | 4T4R | 20 | 152650 |
| 3271282 | 13 | 121.4737403911 | 31.1441998320 | 239 | 13 | 4 | 15.3 | FDD | 479 | n1 | 152650 | 30M | 4T4R | 20 | 152650 |
| 3278037 | 3 | 121.4654622197 | 31.1489511278 | 118 | 13 | 9 | 24.9 | TDD | 429 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3278170 | 2 | 121.4729596590 | 31.1509031435 | 250 | 0 | 12 | 22.9 | TDD | 962 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |

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
| 2024-09-20 22:21:30.967 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.102 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.102 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.810 | NREventA2 | measId:1;ServCellPCI:867;Se... |
| 2024-09-20 22:21:34.929 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.150 | NREventA5 | measId:3;ServCellPCI:867;Se... |
| 2024-09-20 22:21:35.192 | NRHandoverAttempt | SourcePCI:867;SourceNR-ARFC... |
| 2024-09-20 22:21:35.236 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.247 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:35.382 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.382 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3230901 | 1 | 17.9978 | 11.1216 | -114.4607 | 9.9662 | 168.7505 | 0.0083 | 0.0078 |
| 2024_09_20 22:00 | 3278170 | 2 | 17.8698 | 12.9203 | -115.4141 | 6.8255 | 185.6464 | 0.0192 | 0.0014 |
| 2024_09_20 22:00 | 3278037 | 3 | 8.6113 | 15.5325 | -115.9343 | 14.2982 | 94.1950 | 0.0054 | 0.0062 |
| 2024_09_20 22:00 | 3227089 | 4 | 12.6817 | 13.1135 | -117.7733 | 13.2105 | 129.7622 | 0.0159 | 0.0184 |
| 2024_09_20 22:00 | 3247937 | 5 | 15.2826 | 16.5156 | -114.0348 | 19.8938 | 149.2476 | 0.0184 | 0.0024 |
| 2024_09_20 22:00 | 3251609 | 6 | 16.4390 | 7.9309 | -115.2489 | 7.4863 | 163.1118 | 0.0186 | 0.0122 |
| 2024_09_20 22:00 | 3223014 | 7 | 12.4056 | 5.2554 | -116.5842 | 3.6360 | 42.8540 | 0.0040 | 0.0149 |
| 2024_09_20 22:00 | 3226349 | 8 | 16.1322 | 16.5000 | -116.4475 | 4.9105 | 25.1032 | 0.0080 | 0.0114 |
| 2024_09_20 22:00 | 3228067 | 9 | 17.1367 | 6.6915 | -116.2311 | 3.6727 | 22.5436 | 0.0047 | 0.0164 |
| 2024_09_20 22:00 | 3223006 | 10 | 10.9753 | 8.9056 | -114.6532 | 4.3643 | 57.3239 | 0.0057 | 0.0102 |
| 2024_09_20 22:00 | 3258997 | 11 | 15.9622 | 15.9538 | -115.1747 | 4.7055 | 37.6594 | 0.0042 | 0.0054 |
| 2024_09_20 22:00 | 3224759 | 12 | 6.5210 | 10.9061 | -116.5423 | 3.1841 | 36.6842 | 0.0095 | 0.0089 |
| 2024_09_20 22:00 | 3271282 | 13 | 9.7356 | 9.3403 | -114.9838 | 4.7951 | 27.9769 | 0.0059 | 0.0090 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415009_34D86625 | 152650 | 865 | -96.6 | 152650 | 460 | -99.3 | 152650 | 872 | -107.2 | 152650 | 479 |
| MR_1774415009_6A526666 | 152650 | 865 | -95.4 | 152650 | 460 | -96.6 | 152650 | 872 | -106.7 | 152650 | 479 |
| MR_1774415009_9D730FAA | 152650 | 865 | -95.0 | 152650 | 460 | -96.8 | 152650 | 872 | -108.2 | 152650 | 479 |
| MR_1774415009_280AC440 | 504990 | 278 | -94.5 | 504990 | 736 | -96.7 | 504990 | 429 | -96.7 | 504990 | 571 |
| MR_1774415009_3CD41CF0 | 504990 | 278 | -93.9 | 504990 | 736 | -96.8 | 504990 | 429 | -96.2 | 504990 | 571 |
| MR_1774415009_B1C8717F | 152650 | 865 | -94.6 | 152650 | 460 | -96.9 | 152650 | 872 | -105.8 | 152650 | 479 |
| MR_1774415009_DD9FE85C | 152650 | 865 | -96.9 | 152650 | 460 | -99.7 | 152650 | 872 | -104.6 | 152650 | 479 |
| MR_1774415009_1BE82A34 | 504990 | 278 | -92.6 | 504990 | 736 | -96.6 | 504990 | 429 | -97.9 | 504990 | 571 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 544: `6f0f12fd-06c...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `6f0f12fd-06c6-40f4-98b8-90bfef957265` |
| Tag | **single-answer** |
| 정답 | **C15** |
| C15 의미 | Lift the tilt angle  of 3243441_3 by 5 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[544] topology](images/train_0544.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3243908_1
- `C2`: Adjust the azimuth of 3243441_3 by 50 degrees
- `C3`: Decrease A3 Offset threshold for 3258547_4
- `C4`: Increase A3 Offset threshold for 3243908_1
- `C5`: Check test server and transmission issues
- `C6`: Add neighbor relationship between 3243441_3 and 3258547_4
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3258547_4
- `C8`: Decrease transmission power for 3243908_1
- `C9`: Add neighbor relationship between 3243908_1 and 3258547_4
- `C10`: Press down the tilt angle  of 3243441_3 by 5 degrees
- `C11`: Decrease A3 Offset threshold for 3243908_1
- `C12`: Insufficient data; more data is needed for judgment.
- `C13`: Lift the tilt angle of 3243908_1 by 4 degrees
- `C14`: Increase transmission power for 3258547_4
- `C15`: Lift the tilt angle  of 3243441_3 by 5 degrees **← 정답**
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3258547_4
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3243908_1
- `C18`: Increase transmission power for 3243908_1
- `C19`: Adjust the azimuth of 3243908_1 by 3 degrees
- `C20`: Increase A3 Offset threshold for 3258547_4
- `C21`: Decrease transmission power for 3258547_4
- `C22`: Press down the tilt angle of 3243908_1 by 4 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.280 | MS1 | 121.4656634422 | 31.1446281693 | 32 | 504990 | -88.25 | 15.39 | 495.12 | 0.03 | 2.95 | 1561 |
| 2024-09-20 22:21:32.545 | MS1 | 121.4656601781 | 31.1446227179 | 32 | 504990 | -90.67 | 16.98 | 498.50 | 0.05 | 2.18 | 1563 |
| 2024-09-20 22:21:33.586 | MS1 | 121.4656599649 | 31.1446374693 | 32 | 504990 | -86.56 | 15.35 | 607.99 | 0.17 | 2.96 | 1578 |
| 2024-09-20 22:21:34.984 | MS1 | 121.4656672272 | 31.1446293199 | 32 | 504990 | -87.49 | 13.04 | 54.73 | 0.10 | 2.14 | 1565 |
| 2024-09-20 22:21:35.901 | MS1 | 121.4656607493 | 31.1446324823 | 32 | 504990 | -85.41 | 12.70 | 48.79 | 0.18 | 2.30 | 1568 |
| 2024-09-20 22:21:36.291 | MS1 | 121.4656730148 | 31.1446376649 | 32 | 504990 | -86.99 | 14.19 | 72.16 | 0.04 | 2.79 | 1562 |
| 2024-09-20 22:21:37.652 | MS1 | 121.4656647271 | 31.1446263694 | 32 | 504990 | -91.54 | 11.20 | 55.47 | 0.03 | 2.67 | 1584 |
| 2024-09-20 22:21:38.138 | MS1 | 121.4656637000 | 31.1446321784 | 32 | 504990 | -93.40 | 12.48 | 81.89 | 0.16 | 2.07 | 1578 |
| 2024-09-20 22:21:39.912 | MS1 | 121.4656717148 | 31.1446186238 | 32 | 504990 | -92.55 | 12.47 | 59.51 | 0.15 | 2.70 | 1589 |
| 2024-09-20 22:21:40.421 | MS1 | 121.4656617427 | 31.1446332556 | 32 | 504990 | -89.65 | 8.86 | 427.41 | 0.02 | 2.03 | 1599 |
| 2024-09-20 22:21:41.587 | MS1 | 121.4656736729 | 31.1446215954 | 32 | 504990 | -89.90 | 8.13 | 491.30 | 0.13 | 2.41 | 1567 |
| 2024-09-20 22:21:42.483 | MS1 | 121.4656594318 | 31.1446294148 | 32 | 504990 | -89.94 | 7.83 | 502.00 | 0.11 | 2.39 | 1596 |

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
| 3243441 | 3 | 121.4673721916 | 31.1470753750 | 76 | 8 | 4 | 44.8 | TDD | 500 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3243908 | 1 | 121.4686944768 | 31.1452679609 | 253 | 0 | 0 | 22.7 | TDD | 32 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3258547 | 4 | 121.4663724538 | 31.1539137426 | 290 | 3 | 5 | 33.1 | TDD | 990 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3263037 | 2 | 121.4656203947 | 31.1524881135 | 48 | 3 | 10 | 16.1 | TDD | 257 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:31.628 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.644 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.789 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.789 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.483 | NREventA3 | measId:2;ServCellPCI:818;Se... |
| 2024-09-20 22:21:38.723 | NRHandoverAttempt | SourcePCI:818;SourceNR-ARFC... |
| 2024-09-20 22:21:38.762 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.774 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.920 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.920 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3243908 | 1 | 77.2452 | 89.2845 | -115.2222 | 11.8050 | 199.1271 | 0.0076 | 0.0068 |
| 2024_09_20 22:00 | 3263037 | 2 | 5.0053 | 9.8168 | -116.3358 | 9.7058 | 87.0868 | 0.0007 | 0.0078 |
| 2024_09_20 22:00 | 3243441 | 3 | 7.6474 | 19.1728 | -114.6719 | 15.3209 | 163.1695 | 0.0112 | 0.0189 |
| 2024_09_20 22:00 | 3258547 | 4 | 15.2684 | 9.0826 | -116.1972 | 12.2001 | 155.5766 | 0.0059 | 0.0189 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415883_E78A885A | 504990 | 32 | -86.0 | 504990 | 990 | -94.4 | 504990 | 500 | -98.6 | 504990 | 257 |
| MR_1774415883_580955A4 | 504990 | 32 | -86.0 | 504990 | 990 | -91.0 | 504990 | 500 | -100.2 | 504990 | 257 |
| MR_1774415883_7621800B | 504990 | 32 | -89.3 | 504990 | 990 | -94.4 | 504990 | 500 | -97.2 | 504990 | 257 |
| MR_1774415883_664FB381 | 504990 | 32 | -85.8 | 504990 | 990 | -92.4 | 504990 | 500 | -97.4 | 504990 | 257 |
| MR_1774415883_67CDF0A0 | 504990 | 32 | -86.6 | 504990 | 990 | -92.2 | 504990 | 500 | -98.8 | 504990 | 257 |
| MR_1774415883_9101C38B | 504990 | 32 | -86.8 | 504990 | 990 | -91.2 | 504990 | 500 | -99.8 | 504990 | 257 |
| MR_1774415883_AC0EE68E | 504990 | 32 | -87.2 | 504990 | 990 | -93.4 | 504990 | 500 | -97.5 | 504990 | 257 |
| MR_1774415883_9001950F | 504990 | 32 | -89.0 | 504990 | 990 | -91.1 | 504990 | 500 | -100.0 | 504990 | 257 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 545: `3b31d709-cfa...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `3b31d709-cfa8-4884-8b1f-c670e92bfe95` |
| Tag | **single-answer** |
| 정답 | **C4** |
| C4 의미 | Decrease A3 Offset threshold for 3248869_4 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[545] topology](images/train_0545.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3248869_4
- `C2`: Press down the tilt angle  of 3210909_3 by 6 degrees
- `C3`: Press down the tilt angle of 3248869_4 by 10 degrees
- `C4`: Decrease A3 Offset threshold for 3248869_4 **← 정답**
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3248869_4
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3210909_3
- `C7`: Insufficient data; more data is needed for judgment.
- `C8`: Lift the tilt angle  of 3210909_3 by 6 degrees
- `C9`: Increase transmission power for 3210909_3
- `C10`: Decrease transmission power for 3210909_3
- `C11`: Increase transmission power for 3248869_4
- `C12`: Decrease transmission power for 3248869_4
- `C13`: Adjust the azimuth of 3248869_4 by 50 degrees
- `C14`: Add neighbor relationship between 3252492_2 and 3210909_3
- `C15`: Increase A3 Offset threshold for 3210909_3
- `C16`: Check test server and transmission issues
- `C17`: Increase A3 Offset threshold for 3248869_4
- `C18`: Decrease A3 Offset threshold for 3210909_3
- `C19`: Add neighbor relationship between 3248869_4 and 3210909_3
- `C20`: Lift the tilt angle of 3248869_4 by 10 degrees
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3210909_3
- `C22`: Adjust the azimuth of 3210909_3 by 50 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.119 | MS1 | 121.4656679225 | 31.1446242554 | 147 | 504990 | -79.50 | 13.66 | 321.64 | 0.09 | 2.23 | 1561 |
| 2024-09-20 22:21:32.171 | MS1 | 121.4656692863 | 31.1446247368 | 147 | 504990 | -82.95 | 12.38 | 347.16 | 0.11 | 2.66 | 1568 |
| 2024-09-20 22:21:33.415 | MS1 | 121.4656744019 | 31.1446373997 | 147 | 504990 | -76.70 | 16.87 | 527.43 | 0.03 | 2.89 | 1576 |
| 2024-09-20 22:21:34.875 | MS1 | 121.4656762112 | 31.1446219052 | 147 | 504990 | -84.04 | -1.76 | 62.43 | 0.01 | 1.47 | 1578 |
| 2024-09-20 22:21:35.172 | MS1 | 121.4656598348 | 31.1446347630 | 147 | 504990 | -87.52 | -1.13 | 42.07 | 0.09 | 1.04 | 1596 |
| 2024-09-20 22:21:36.140 | MS1 | 121.4656725694 | 31.1446279615 | 147 | 504990 | -92.50 | -0.35 | 28.26 | 0.20 | 1.30 | 1565 |
| 2024-09-20 22:21:37.226 | MS1 | 121.4656736482 | 31.1446298612 | 147 | 504990 | -86.65 | -1.81 | 47.17 | 0.09 | 1.20 | 1584 |
| 2024-09-20 22:21:38.981 | MS1 | 121.4656748963 | 31.1446376208 | 147 | 504990 | -87.99 | -2.61 | 42.17 | 0.03 | 1.44 | 1572 |
| 2024-09-20 22:21:39.756 | MS1 | 121.4656730986 | 31.1446285395 | 811 | 504990 | -77.15 | 16.36 | 254.00 | 0.15 | 1.32 | 1598 |
| 2024-09-20 22:21:40.503 | MS1 | 121.4656738960 | 31.1446254036 | 811 | 504990 | -76.37 | 14.77 | 477.48 | 0.01 | 2.43 | 1561 |
| 2024-09-20 22:21:41.445 | MS1 | 121.4656696118 | 31.1446262760 | 811 | 504990 | -81.50 | 15.42 | 556.61 | 0.18 | 2.53 | 1578 |
| 2024-09-20 22:21:42.219 | MS1 | 121.4656668308 | 31.1446371610 | 811 | 504990 | -80.75 | 17.27 | 444.65 | 0.04 | 2.61 | 1564 |

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
| 3210909 | 3 | 121.4732964990 | 31.1469683307 | 61 | 2 | 3 | 48.1 | TDD | 811 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3246539 | 1 | 121.4698515930 | 31.1519553410 | 156 | 5 | 8 | 34.8 | TDD | 458 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3248869 | 4 | 121.4745240367 | 31.1520166615 | 95 | 15 | 6 | 48.9 | TDD | 147 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3252492 | 2 | 121.4756641766 | 31.1527510875 | 97 | 12 | 12 | 23.1 | TDD | 666 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:31.308 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.425 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.425 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.128 | NREventA3 | measId:2;ServCellPCI:970;Se... |
| 2024-09-20 22:21:38.368 | NRHandoverAttempt | SourcePCI:970;SourceNR-ARFC... |
| 2024-09-20 22:21:38.409 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.422 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.541 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.541 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3246539 | 1 | 14.5247 | 6.1542 | -115.5045 | 9.5621 | 117.7477 | 0.0181 | 0.0021 |
| 2024_09_20 22:00 | 3252492 | 2 | 7.9755 | 12.6145 | -115.7740 | 6.2253 | 131.0846 | 0.0171 | 0.0154 |
| 2024_09_20 22:00 | 3210909 | 3 | 19.5166 | 10.1509 | -116.8900 | 15.1760 | 93.6825 | 0.0026 | 0.0075 |
| 2024_09_20 22:00 | 3248869 | 4 | 6.9338 | 13.1777 | -117.5195 | 9.8527 | 129.2140 | 0.0132 | 0.1124 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414018_3344EA13 | 504990 | 147 | -85.6 | 504990 | 811 | -78.1 | 504990 | 666 | -79.4 | 504990 | 458 |
| MR_1774414018_AA83E479 | 504990 | 811 | -77.5 | 504990 | 147 | -82.4 | 504990 | 666 | -80.6 | 504990 | 458 |
| MR_1774414018_1CAF5830 | 504990 | 811 | -79.4 | 504990 | 147 | -85.3 | 504990 | 666 | -77.7 | 504990 | 458 |
| MR_1774414018_F6AF0ED5 | 504990 | 811 | -79.2 | 504990 | 147 | -85.7 | 504990 | 666 | -80.5 | 504990 | 458 |
| MR_1774414018_31C24B6E | 504990 | 147 | -85.9 | 504990 | 811 | -77.7 | 504990 | 666 | -80.4 | 504990 | 458 |
| MR_1774414018_113C3148 | 504990 | 811 | -79.7 | 504990 | 147 | -84.7 | 504990 | 666 | -77.8 | 504990 | 458 |
| MR_1774414018_197918B2 | 504990 | 811 | -77.9 | 504990 | 147 | -82.4 | 504990 | 666 | -80.7 | 504990 | 458 |
| MR_1774414018_049800E7 | 504990 | 147 | -83.0 | 504990 | 811 | -78.3 | 504990 | 666 | -79.7 | 504990 | 458 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 546: `905b5148-d76...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `905b5148-d76c-4d4d-aac2-3296567297b2` |
| Tag | **single-answer** |
| 정답 | **C6** |
| C6 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3249534_4 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[546] topology](images/train_0546.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3259094_2 by 10 degrees
- `C2`: Press down the tilt angle of 3249534_4 by 4 degrees
- `C3`: Decrease A3 Offset threshold for 3259094_2
- `C4`: Decrease transmission power for 3259094_2
- `C5`: Insufficient data; more data is needed for judgment.
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3249534_4 **← 정답**
- `C7`: Add neighbor relationship between 3249534_4 and 3259094_2
- `C8`: Increase A3 Offset threshold for 3249534_4
- `C9`: Decrease A3 Offset threshold for 3249534_4
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3259094_2
- `C11`: Decrease transmission power for 3249534_4
- `C12`: Check test server and transmission issues
- `C13`: Increase transmission power for 3259094_2
- `C14`: Lift the tilt angle of 3249534_4 by 4 degrees
- `C15`: Increase A3 Offset threshold for 3259094_2
- `C16`: Adjust the azimuth of 3249534_4 by 24 degrees
- `C17`: Increase transmission power for 3249534_4
- `C18`: Adjust the azimuth of 3259094_2 by 50 degrees
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3249534_4
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3259094_2
- `C21`: Lift the tilt angle  of 3259094_2 by 10 degrees
- `C22`: Add neighbor relationship between 3255006_1 and 3259094_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.898 | MS1 | 121.4656735034 | 31.1446187896 | 551 | 504990 | -86.99 | 16.67 | 377.84 | 0.09 | 2.08 | 1565 |
| 2024-09-20 22:21:32.953 | MS1 | 121.4656766108 | 31.1446227188 | 551 | 504990 | -89.02 | 12.34 | 441.45 | 0.08 | 2.53 | 1564 |
| 2024-09-20 22:21:33.933 | MS1 | 121.4656617536 | 31.1446374454 | 551 | 504990 | -87.92 | 12.56 | 608.47 | 0.19 | 2.54 | 1572 |
| 2024-09-20 22:21:34.140 | MS1 | 121.4656656376 | 31.1446346411 | 551 | 504990 | -90.31 | 13.28 | 92.49 | 0.67 | 2.61 | 523 |
| 2024-09-20 22:21:35.411 | MS1 | 121.4656683982 | 31.1446330758 | 551 | 504990 | -86.45 | 12.12 | 59.58 | 0.64 | 2.10 | 691 |
| 2024-09-20 22:21:36.758 | MS1 | 121.4656693854 | 31.1446371364 | 551 | 504990 | -90.58 | 16.26 | 62.54 | 0.57 | 2.47 | 634 |
| 2024-09-20 22:21:37.133 | MS1 | 121.4656606891 | 31.1446330718 | 551 | 504990 | -91.77 | 9.64 | 86.70 | 0.61 | 2.13 | 587 |
| 2024-09-20 22:21:38.330 | MS1 | 121.4656607129 | 31.1446352959 | 551 | 504990 | -91.62 | 7.89 | 54.17 | 0.63 | 2.71 | 518 |
| 2024-09-20 22:21:39.224 | MS1 | 121.4656608705 | 31.1446357227 | 551 | 504990 | -91.71 | 8.27 | 76.97 | 0.51 | 2.80 | 548 |
| 2024-09-20 22:21:40.541 | MS1 | 121.4656757945 | 31.1446295823 | 551 | 504990 | -90.68 | 12.27 | 381.75 | 0.06 | 2.91 | 1573 |
| 2024-09-20 22:21:41.760 | MS1 | 121.4656694044 | 31.1446279137 | 551 | 504990 | -89.83 | 10.26 | 316.23 | 0.07 | 2.36 | 1575 |
| 2024-09-20 22:21:42.650 | MS1 | 121.4656778364 | 31.1446217091 | 551 | 504990 | -93.95 | 10.88 | 381.33 | 0.15 | 2.10 | 1572 |

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
| 3249534 | 4 | 121.4705007140 | 31.1446623122 | 294 | 1 | 11 | 23.9 | TDD | 551 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3255006 | 1 | 121.4719074011 | 31.1533562445 | 357 | 0 | 9 | 33.9 | TDD | 1 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3256974 | 3 | 121.4752004768 | 31.1530476974 | 244 | 2 | 8 | 46.4 | TDD | 476 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3259094 | 2 | 121.4741812522 | 31.1480704466 | 74 | 13 | 9 | 19.1 | TDD | 75 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |

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
| 2024-09-20 22:21:31.384 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.404 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.530 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.530 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.206 | NREventA3 | measId:2;ServCellPCI:478;Se... |
| 2024-09-20 22:21:38.446 | NRHandoverAttempt | SourcePCI:478;SourceNR-ARFC... |
| 2024-09-20 22:21:38.492 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.502 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.638 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.638 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3255006 | 1 | 12.5746 | 6.1498 | -114.3683 | 8.6329 | 164.1971 | 0.0128 | 0.0140 |
| 2024_09_20 22:00 | 3259094 | 2 | 10.6538 | 19.5191 | -117.5794 | 12.0262 | 121.1251 | 0.0126 | 0.0073 |
| 2024_09_20 22:00 | 3256974 | 3 | 15.6049 | 7.5708 | -117.1445 | 14.9491 | 80.4378 | 0.0100 | 0.0005 |
| 2024_09_20 22:00 | 3249534 | 4 | 6.2307 | 8.3803 | -117.7453 | 17.1420 | 149.4806 | 0.0132 | 0.0086 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413136_102F1537 | 504990 | 551 | -89.7 | 504990 | 75 | -90.5 | 504990 | 1 | -103.4 | 504990 | 476 |
| MR_1774413136_8D8D5D2D | 504990 | 551 | -89.1 | 504990 | 75 | -92.7 | 504990 | 1 | -104.1 | 504990 | 476 |
| MR_1774413136_59D9100B | 504990 | 551 | -89.4 | 504990 | 75 | -92.1 | 504990 | 1 | -104.0 | 504990 | 476 |
| MR_1774413136_B1D29EA2 | 504990 | 551 | -90.4 | 504990 | 75 | -91.2 | 504990 | 1 | -102.4 | 504990 | 476 |
| MR_1774413136_0D3C08B9 | 504990 | 551 | -91.6 | 504990 | 75 | -91.9 | 504990 | 1 | -103.4 | 504990 | 476 |
| MR_1774413136_2C1C5CDA | 504990 | 551 | -89.7 | 504990 | 75 | -92.8 | 504990 | 1 | -105.4 | 504990 | 476 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 547: `11859700-814...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `11859700-814b-4594-9d87-70714cf9531c` |
| Tag | **single-answer** |
| 정답 | **C13** |
| C13 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[547] topology](images/train_0547.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3213240_3
- `C2`: Insufficient data; more data is needed for judgment.
- `C3`: Add neighbor relationship between 3213240_3 and 3242409_2
- `C4`: Increase A3 Offset threshold for 3242409_2
- `C5`: Add neighbor relationship between 3276103_1 and 3242409_2
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3213240_3
- `C7`: Decrease transmission power for 3242409_2
- `C8`: Press down the tilt angle of 3213240_3 by 6 degrees
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3242409_2
- `C10`: Decrease A3 Offset threshold for 3242409_2
- `C11`: Lift the tilt angle of 3213240_3 by 6 degrees
- `C12`: Lift the tilt angle  of 3242409_2 by 10 degrees
- `C13`: Check test server and transmission issues **← 정답**
- `C14`: Increase A3 Offset threshold for 3213240_3
- `C15`: Decrease transmission power for 3213240_3
- `C16`: Press down the tilt angle  of 3242409_2 by 10 degrees
- `C17`: Increase transmission power for 3242409_2
- `C18`: Increase transmission power for 3213240_3
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3242409_2
- `C20`: Adjust the azimuth of 3213240_3 by 50 degrees
- `C21`: Adjust the azimuth of 3242409_2 by 16 degrees
- `C22`: Decrease A3 Offset threshold for 3213240_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.930 | MS1 | 121.4656729259 | 31.1446358972 | 830 | 504990 | -85.83 | 15.96 | 489.61 | 0.19 | 2.55 | 1598 |
| 2024-09-20 22:21:32.566 | MS1 | 121.4656767827 | 31.1446329573 | 830 | 504990 | -86.22 | 13.64 | 430.74 | 0.04 | 2.40 | 1590 |
| 2024-09-20 22:21:33.570 | MS1 | 121.4656777817 | 31.1446225083 | 830 | 504990 | -90.83 | 12.14 | 495.43 | 0.19 | 2.54 | 1599 |
| 2024-09-20 22:21:34.152 | MS1 | 121.4656771707 | 31.1446188232 | 830 | 504990 | -87.31 | 12.50 | 91.19 | 0.03 | 2.01 | 400 |
| 2024-09-20 22:21:35.195 | MS1 | 121.4656743959 | 31.1446293474 | 830 | 504990 | -86.77 | 17.27 | 53.90 | 0.15 | 2.66 | 428 |
| 2024-09-20 22:21:36.948 | MS1 | 121.4656757027 | 31.1446289929 | 830 | 504990 | -87.27 | 13.11 | 62.90 | 0.03 | 2.05 | 382 |
| 2024-09-20 22:21:37.735 | MS1 | 121.4656740514 | 31.1446180615 | 830 | 504990 | -89.33 | 11.28 | 76.34 | 0.16 | 2.67 | 415 |
| 2024-09-20 22:21:38.178 | MS1 | 121.4656632979 | 31.1446373109 | 830 | 504990 | -89.59 | 9.42 | 67.37 | 0.20 | 2.54 | 462 |
| 2024-09-20 22:21:39.282 | MS1 | 121.4656630344 | 31.1446339482 | 830 | 504990 | -90.07 | 12.60 | 82.69 | 0.10 | 2.63 | 327 |
| 2024-09-20 22:21:40.990 | MS1 | 121.4656687338 | 31.1446314320 | 830 | 504990 | -92.65 | 7.09 | 592.27 | 0.14 | 2.23 | 1574 |
| 2024-09-20 22:21:41.766 | MS1 | 121.4656622130 | 31.1446190599 | 830 | 504990 | -91.94 | 10.21 | 383.21 | 0.06 | 2.44 | 1597 |
| 2024-09-20 22:21:42.842 | MS1 | 121.4656618986 | 31.1446224508 | 830 | 504990 | -91.53 | 12.58 | 540.16 | 0.14 | 2.87 | 1561 |

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
| 3213240 | 3 | 121.4721073088 | 31.1454216275 | 48 | 2 | 0 | 44.0 | TDD | 830 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3242409 | 2 | 121.4692861544 | 31.1484796048 | 235 | 8 | 3 | 40.3 | TDD | 835 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3247870 | 4 | 121.4650359550 | 31.1519907854 | 229 | 4 | 7 | 26.9 | TDD | 719 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3276103 | 1 | 121.4669369887 | 31.1498476555 | 61 | 5 | 5 | 28.0 | TDD | 1002 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:31.158 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.173 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.313 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.313 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.992 | NREventA3 | measId:2;ServCellPCI:109;Se... |
| 2024-09-20 22:21:38.232 | NRHandoverAttempt | SourcePCI:109;SourceNR-ARFC... |
| 2024-09-20 22:21:38.269 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.283 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.407 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.407 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3276103 | 1 | 18.8225 | 15.2178 | -115.0321 | 15.9279 | 150.6689 | 0.0136 | 0.0006 |
| 2024_09_20 22:00 | 3242409 | 2 | 6.0094 | 9.1823 | -116.6667 | 16.5135 | 122.8805 | 0.0139 | 0.0092 |
| 2024_09_20 22:00 | 3213240 | 3 | 12.6890 | 5.7768 | -114.8771 | 15.8437 | 115.8561 | 0.0077 | 0.0190 |
| 2024_09_20 22:00 | 3247870 | 4 | 14.6711 | 7.5074 | -116.7637 | 14.5162 | 157.2067 | 0.0172 | 0.0097 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414581_DEDA2607 | 504990 | 830 | -86.9 | 504990 | 835 | -88.4 | 504990 | 1002 | -96.1 | 504990 | 719 |
| MR_1774414581_70F0A9D7 | 504990 | 830 | -85.4 | 504990 | 835 | -90.5 | 504990 | 1002 | -94.5 | 504990 | 719 |
| MR_1774414581_C6592FBC | 504990 | 830 | -86.8 | 504990 | 835 | -89.7 | 504990 | 1002 | -94.4 | 504990 | 719 |
| MR_1774414581_BB7A5BC3 | 504990 | 830 | -87.7 | 504990 | 835 | -88.4 | 504990 | 1002 | -95.5 | 504990 | 719 |
| MR_1774414581_EDB6B52F | 504990 | 830 | -89.1 | 504990 | 835 | -88.2 | 504990 | 1002 | -95.3 | 504990 | 719 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 548: `418c3a81-d4d...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `418c3a81-d4d7-440c-a509-9a5e0317087f` |
| Tag | **single-answer** |
| 정답 | **C3** |
| C3 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3235061_2 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[548] topology](images/train_0548.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3235061_2
- `C2`: Lift the tilt angle of 3235061_2 by 4 degrees
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3235061_2 **← 정답**
- `C4`: Decrease transmission power for 3235061_2
- `C5`: Increase A3 Offset threshold for 3235061_2
- `C6`: Adjust the azimuth of 3235061_2 by 5 degrees
- `C7`: Check test server and transmission issues
- `C8`: Add neighbor relationship between 3235061_2 and 3271023_1
- `C9`: Decrease A3 Offset threshold for 3271023_1
- `C10`: Adjust the azimuth of 3271023_1 by 50 degrees
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3235061_2
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3271023_1
- `C13`: Press down the tilt angle of 3235061_2 by 4 degrees
- `C14`: Decrease transmission power for 3271023_1
- `C15`: Insufficient data; more data is needed for judgment.
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3271023_1
- `C17`: Increase A3 Offset threshold for 3271023_1
- `C18`: Increase transmission power for 3271023_1
- `C19`: Press down the tilt angle  of 3271023_1 by 10 degrees
- `C20`: Lift the tilt angle  of 3271023_1 by 10 degrees
- `C21`: Add neighbor relationship between 3248370_3 and 3271023_1
- `C22`: Decrease A3 Offset threshold for 3235061_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.541 | MS1 | 121.4656619600 | 31.1446311428 | 545 | 504990 | -87.94 | 14.06 | 342.97 | 0.01 | 2.54 | 1570 |
| 2024-09-20 22:21:32.950 | MS1 | 121.4656614036 | 31.1446329426 | 545 | 504990 | -88.38 | 15.67 | 423.53 | 0.04 | 2.06 | 1560 |
| 2024-09-20 22:21:33.819 | MS1 | 121.4656757147 | 31.1446227058 | 545 | 504990 | -89.55 | 14.27 | 312.65 | 0.00 | 2.67 | 1567 |
| 2024-09-20 22:21:34.726 | MS1 | 121.4656775857 | 31.1446294627 | 545 | 504990 | -89.06 | 17.08 | 72.21 | 0.64 | 2.67 | 619 |
| 2024-09-20 22:21:35.143 | MS1 | 121.4656679562 | 31.1446240429 | 545 | 504990 | -88.95 | 13.59 | 87.70 | 0.63 | 2.91 | 626 |
| 2024-09-20 22:21:36.894 | MS1 | 121.4656642359 | 31.1446266189 | 545 | 504990 | -86.98 | 16.81 | 66.56 | 0.60 | 2.78 | 501 |
| 2024-09-20 22:21:37.469 | MS1 | 121.4656651597 | 31.1446323497 | 545 | 504990 | -89.33 | 9.33 | 71.31 | 0.55 | 2.91 | 568 |
| 2024-09-20 22:21:38.101 | MS1 | 121.4656734728 | 31.1446330898 | 545 | 504990 | -90.07 | 11.29 | 75.42 | 0.61 | 2.86 | 628 |
| 2024-09-20 22:21:39.422 | MS1 | 121.4656616661 | 31.1446225732 | 545 | 504990 | -89.62 | 7.59 | 88.07 | 0.55 | 2.26 | 607 |
| 2024-09-20 22:21:40.580 | MS1 | 121.4656722022 | 31.1446378797 | 545 | 504990 | -93.13 | 7.05 | 477.07 | 0.12 | 2.14 | 1567 |
| 2024-09-20 22:21:41.100 | MS1 | 121.4656743468 | 31.1446294152 | 545 | 504990 | -91.73 | 10.86 | 585.10 | 0.17 | 2.95 | 1592 |
| 2024-09-20 22:21:42.340 | MS1 | 121.4656688953 | 31.1446232419 | 545 | 504990 | -92.52 | 12.46 | 310.47 | 0.01 | 2.85 | 1572 |

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
| 3235061 | 2 | 121.4640895369 | 31.1555186220 | 178 | 2 | 8 | 47.9 | TDD | 545 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3248370 | 3 | 121.4656311028 | 31.1493929889 | 137 | 0 | 12 | 34.1 | TDD | 841 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3248833 | 4 | 121.4756995884 | 31.1512183837 | 237 | 3 | 4 | 49.9 | TDD | 89 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3271023 | 1 | 121.4723677833 | 31.1554988415 | 35 | 9 | 0 | 19.9 | TDD | 592 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |

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
| 2024-09-20 22:21:31.319 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.338 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.464 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.464 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.202 | NREventA3 | measId:2;ServCellPCI:603;Se... |
| 2024-09-20 22:21:38.442 | NRHandoverAttempt | SourcePCI:603;SourceNR-ARFC... |
| 2024-09-20 22:21:38.477 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.492 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.606 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.606 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3271023 | 1 | 7.1099 | 17.9729 | -116.8501 | 16.4171 | 82.5867 | 0.0088 | 0.0044 |
| 2024_09_20 22:00 | 3235061 | 2 | 19.0970 | 16.9359 | -114.3029 | 14.9018 | 85.3664 | 0.0195 | 0.0109 |
| 2024_09_20 22:00 | 3248370 | 3 | 17.2772 | 15.6433 | -116.0104 | 6.6415 | 116.7704 | 0.0152 | 0.0197 |
| 2024_09_20 22:00 | 3248833 | 4 | 5.4049 | 9.7098 | -115.0344 | 6.8171 | 186.2777 | 0.0035 | 0.0106 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417133_E482DD38 | 504990 | 545 | -87.9 | 504990 | 592 | -96.9 | 504990 | 841 | -100.3 | 504990 | 89 |
| MR_1774417133_5DA17329 | 504990 | 545 | -91.0 | 504990 | 592 | -95.7 | 504990 | 841 | -100.5 | 504990 | 89 |
| MR_1774417133_7FE782F3 | 504990 | 545 | -89.1 | 504990 | 592 | -95.3 | 504990 | 841 | -103.8 | 504990 | 89 |
| MR_1774417133_4C290456 | 504990 | 545 | -88.3 | 504990 | 592 | -94.9 | 504990 | 841 | -101.5 | 504990 | 89 |
| MR_1774417133_0CA994BF | 504990 | 545 | -90.0 | 504990 | 592 | -96.3 | 504990 | 841 | -104.1 | 504990 | 89 |
| MR_1774417133_5874DF7A | 504990 | 545 | -89.8 | 504990 | 592 | -93.4 | 504990 | 841 | -103.7 | 504990 | 89 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 549: `99b976b3-6c6...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `99b976b3-6c64-41cb-81e3-228b544fa4f9` |
| Tag | **single-answer** |
| 정답 | **C2** |
| C2 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3234779_6 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[549] topology](images/train_0549.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3263525_3 by 15 degrees
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3234779_6 **← 정답**
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3234779_6
- `C4`: Press down the tilt angle of 3234779_6 by 2 degrees
- `C5`: Adjust the azimuth of 3234779_6 by 33 degrees
- `C6`: Increase A3 Offset threshold for 3234779_6
- `C7`: Lift the tilt angle  of 3263525_3 by 6 degrees
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3263525_3
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3263525_3
- `C10`: Insufficient data; more data is needed for judgment.
- `C11`: Add neighbor relationship between 3236716_9 and 3263525_3
- `C12`: Lift the tilt angle of 3234779_6 by 2 degrees
- `C13`: Increase A3 Offset threshold for 3263525_3
- `C14`: Add neighbor relationship between 3234779_6 and 3263525_3
- `C15`: Increase transmission power for 3263525_3
- `C16`: Press down the tilt angle  of 3263525_3 by 6 degrees
- `C17`: Decrease transmission power for 3263525_3
- `C18`: Check test server and transmission issues
- `C19`: Decrease A3 Offset threshold for 3263525_3
- `C20`: Decrease transmission power for 3234779_6
- `C21`: Increase transmission power for 3234779_6
- `C22`: Decrease A3 Offset threshold for 3234779_6

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.693 | MS1 | 121.4656601631 | 31.1446200654 | 382 | 504990 | -94.80 | 13.85 | 372.46 | 0.17 | 2.02 | 1590 |
| 2024-09-20 22:21:32.561 | MS1 | 121.4656616198 | 31.1446202445 | 393 | 504990 | -93.47 | 11.01 | 422.12 | 0.03 | 2.19 | 1593 |
| 2024-09-20 22:21:33.794 | MS1 | 121.4656598627 | 31.1446196848 | 379 | 504990 | -94.43 | 13.46 | 333.68 | 0.16 | 2.97 | 1566 |
| 2024-09-20 22:21:34.466 | MS1 | 121.4656752853 | 31.1446377441 | 148 | 152650 | -87.82 | 2.48 | 74.27 | 0.17 | 1.97 | 965 |
| 2024-09-20 22:21:35.537 | MS1 | 121.4656628923 | 31.1446301600 | 112 | 152650 | -92.39 | 5.60 | 93.33 | 0.02 | 1.54 | 903 |
| 2024-09-20 22:21:36.420 | MS1 | 121.4656727340 | 31.1446231495 | 1004 | 152650 | -87.53 | 7.55 | 48.89 | 0.06 | 1.92 | 923 |
| 2024-09-20 22:21:37.585 | MS1 | 121.4656598046 | 31.1446221686 | 798 | 152650 | -92.03 | 6.65 | 71.35 | 0.12 | 1.58 | 900 |
| 2024-09-20 22:21:38.847 | MS1 | 121.4656584542 | 31.1446269938 | 148 | 152650 | -94.84 | 7.19 | 59.62 | 0.06 | 1.88 | 986 |
| 2024-09-20 22:21:39.136 | MS1 | 121.4656706061 | 31.1446309707 | 112 | 152650 | -87.53 | 2.14 | 84.23 | 0.11 | 1.98 | 990 |
| 2024-09-20 22:21:40.999 | MS1 | 121.4656674125 | 31.1446309492 | 1004 | 152650 | -90.22 | 3.16 | 64.37 | 0.15 | 2.66 | 1573 |
| 2024-09-20 22:21:41.529 | MS1 | 121.4656592310 | 31.1446279270 | 798 | 152650 | -95.45 | 7.26 | 63.88 | 0.02 | 2.27 | 1565 |
| 2024-09-20 22:21:42.129 | MS1 | 121.4656724590 | 31.1446193261 | 148 | 152650 | -87.51 | 2.50 | 94.20 | 0.15 | 2.64 | 1591 |

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
| 3223890 | 10 | 121.4671830792 | 31.1479708632 | 99 | 15 | 4 | 29.4 | FDD | 112 | n1 | 152650 | 30M | 4T4R | 25 | 152650 |
| 3226393 | 11 | 121.4700719791 | 31.1455772529 | 99 | 5 | 10 | 25.8 | FDD | 148 | n1 | 152650 | 30M | 4T4R | 23 | 152650 |
| 3226401 | 2 | 121.4668530412 | 31.1524775064 | 318 | 4 | 1 | 4.0 | TDD | 1003 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3227362 | 5 | 121.4709777528 | 31.1490410471 | 70 | 13 | 6 | 6.1 | TDD | 379 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3229488 | 7 | 121.4756197536 | 31.1545377949 | 68 | 0 | 7 | 10.6 | FDD | 418 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |
| 3234779 | 6 | 121.4650102047 | 31.1554262810 | 144 | 1 | 7 | 17.6 | TDD | 382 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3236716 | 9 | 121.4707404662 | 31.1534966019 | 93 | 13 | 0 | 14.6 | FDD | 1004 | n1 | 152650 | 30M | 4T4R | 28 | 152650 |
| 3260071 | 4 | 121.4673631985 | 31.1544615631 | 265 | 9 | 11 | 12.9 | TDD | 723 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3262572 | 8 | 121.4690389304 | 31.1504327531 | 65 | 10 | 2 | 2.8 | FDD | 38 | n1 | 152650 | 30M | 4T4R | 27 | 152650 |
| 3263525 | 3 | 121.4685656502 | 31.1527344262 | 212 | 4 | 1 | 24.9 | TDD | 947 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3264490 | 12 | 121.4659869665 | 31.1504168782 | 132 | 12 | 7 | 9.1 | FDD | 213 | n1 | 152650 | 30M | 4T4R | 28 | 152650 |
| 3273092 | 13 | 121.4755903954 | 31.1453058577 | 222 | 5 | 2 | 2.8 | FDD | 798 | n1 | 152650 | 30M | 4T4R | 29 | 152650 |
| 3278942 | 1 | 121.4740428330 | 31.1448727096 | 149 | 4 | 0 | 12.5 | TDD | 393 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |

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
| 2024-09-20 22:21:31.314 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.332 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.447 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.447 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.115 | NREventA2 | measId:1;ServCellPCI:885;Se... |
| 2024-09-20 22:21:35.254 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.550 | NREventA5 | measId:3;ServCellPCI:885;Se... |
| 2024-09-20 22:21:35.626 | NRHandoverAttempt | SourcePCI:885;SourceNR-ARFC... |
| 2024-09-20 22:21:35.663 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.673 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:35.784 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.784 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3278942 | 1 | 14.5012 | 14.5938 | -115.5420 | 15.6153 | 176.3394 | 0.0017 | 0.0194 |
| 2024_09_20 22:00 | 3226401 | 2 | 17.2689 | 9.3965 | -116.9428 | 8.6340 | 129.1323 | 0.0141 | 0.0199 |
| 2024_09_20 22:00 | 3263525 | 3 | 6.4650 | 12.9458 | -117.8198 | 7.3855 | 105.4146 | 0.0176 | 0.0118 |
| 2024_09_20 22:00 | 3260071 | 4 | 6.1927 | 17.6167 | -117.8271 | 19.7166 | 194.7325 | 0.0098 | 0.0197 |
| 2024_09_20 22:00 | 3227362 | 5 | 5.3088 | 15.8894 | -117.5098 | 9.0895 | 160.3363 | 0.0128 | 0.0149 |
| 2024_09_20 22:00 | 3234779 | 6 | 15.0951 | 7.5042 | -115.6320 | 14.3719 | 86.3823 | 0.0111 | 0.0072 |
| 2024_09_20 22:00 | 3229488 | 7 | 10.9977 | 17.5979 | -116.1043 | 3.3071 | 29.4900 | 0.0009 | 0.0190 |
| 2024_09_20 22:00 | 3262572 | 8 | 5.9646 | 17.1229 | -115.2376 | 3.1316 | 42.6879 | 0.0060 | 0.0191 |
| 2024_09_20 22:00 | 3236716 | 9 | 12.3221 | 13.1464 | -117.1758 | 3.0777 | 46.8527 | 0.0172 | 0.0066 |
| 2024_09_20 22:00 | 3223890 | 10 | 6.0755 | 6.2767 | -114.8369 | 4.2016 | 58.1071 | 0.0059 | 0.0154 |
| 2024_09_20 22:00 | 3226393 | 11 | 6.5757 | 19.9695 | -117.0520 | 3.8303 | 32.2744 | 0.0067 | 0.0006 |
| 2024_09_20 22:00 | 3264490 | 12 | 12.8550 | 14.8773 | -117.5385 | 3.0702 | 21.0990 | 0.0086 | 0.0170 |
| 2024_09_20 22:00 | 3273092 | 13 | 16.6398 | 11.0108 | -115.8977 | 3.2971 | 47.9471 | 0.0172 | 0.0102 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412919_D337EA14 | 504990 | 379 | -96.2 | 504990 | 947 | -91.3 | 504990 | 723 | -95.6 | 504990 | 1003 |
| MR_1774412919_D4EA4B23 | 504990 | 379 | -95.6 | 504990 | 947 | -92.7 | 504990 | 723 | -97.7 | 504990 | 1003 |
| MR_1774412919_BF79412C | 152650 | 148 | -89.6 | 152650 | 418 | -96.9 | 152650 | 38 | -99.5 | 152650 | 213 |
| MR_1774412919_34EBC984 | 152650 | 148 | -86.4 | 152650 | 418 | -97.2 | 152650 | 38 | -96.7 | 152650 | 213 |
| MR_1774412919_55F03A32 | 504990 | 379 | -95.4 | 504990 | 947 | -93.5 | 504990 | 723 | -96.2 | 504990 | 1003 |

> *... 2개 열 생략 (전체 14열)*

---
