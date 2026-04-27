# Track A 문제 분석 — train[530]~train[539]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[530] ~ train[539] (10개)

## 목차

1. [문제 530: `fd0e1902-5d5...`](#530) — single-answer, 정답: C8
2. [문제 531: `91d1abcb-260...`](#531) — single-answer, 정답: C21
3. [문제 532: `986fc26a-e0c...`](#532) — single-answer, 정답: C5
4. [문제 533: `f432ef91-04a...`](#533) — single-answer, 정답: C15
5. [문제 534: `7f8ca1f1-d9e...`](#534) — single-answer, 정답: C1
6. [문제 535: `913385d6-133...`](#535) — single-answer, 정답: C11
7. [문제 536: `fdacc653-e2b...`](#536) — single-answer, 정답: C6
8. [문제 537: `e4ab116d-ce4...`](#537) — single-answer, 정답: C5
9. [문제 538: `7a0d8a4f-cca...`](#538) — single-answer, 정답: C1
10. [문제 539: `9bf26c13-e95...`](#539) — single-answer, 정답: C4

---

### 문제 530: `fd0e1902-5d5...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `fd0e1902-5d5c-457b-82f3-968b1acf4178` |
| Tag | **single-answer** |
| 정답 | **C8** |
| C8 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3214645_2 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[530] topology](images/train_0530.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3245439_3
- `C2`: Add neighbor relationship between 3214645_2 and 3245439_3
- `C3`: Decrease transmission power for 3214645_2
- `C4`: Insufficient data; more data is needed for judgment.
- `C5`: Lift the tilt angle of 3214645_2 by 5 degrees
- `C6`: Increase A3 Offset threshold for 3245439_3
- `C7`: Press down the tilt angle  of 3245439_3 by 10 degrees
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3214645_2 **← 정답**
- `C9`: Increase transmission power for 3245439_3
- `C10`: Add neighbor relationship between 3223413_1 and 3245439_3
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3245439_3
- `C12`: Increase A3 Offset threshold for 3214645_2
- `C13`: Decrease A3 Offset threshold for 3214645_2
- `C14`: Increase transmission power for 3214645_2
- `C15`: Adjust the azimuth of 3245439_3 by 50 degrees
- `C16`: Lift the tilt angle  of 3245439_3 by 10 degrees
- `C17`: Check test server and transmission issues
- `C18`: Decrease A3 Offset threshold for 3245439_3
- `C19`: Adjust the azimuth of 3214645_2 by 3 degrees
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3214645_2
- `C21`: Decrease transmission power for 3245439_3
- `C22`: Press down the tilt angle of 3214645_2 by 5 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.153 | MS1 | 121.4656767647 | 31.1446333275 | 211 | 504990 | -89.45 | 13.78 | 500.00 | 0.17 | 2.86 | 1592 |
| 2024-09-20 22:21:32.578 | MS1 | 121.4656703332 | 31.1446366082 | 211 | 504990 | -91.97 | 12.77 | 334.76 | 0.05 | 2.40 | 1586 |
| 2024-09-20 22:21:33.276 | MS1 | 121.4656593232 | 31.1446315955 | 211 | 504990 | -90.76 | 16.30 | 401.17 | 0.02 | 2.77 | 1573 |
| 2024-09-20 22:21:34.508 | MS1 | 121.4656616747 | 31.1446196084 | 211 | 504990 | -85.83 | 14.40 | 74.35 | 0.69 | 2.98 | 572 |
| 2024-09-20 22:21:35.356 | MS1 | 121.4656657414 | 31.1446365922 | 211 | 504990 | -90.87 | 15.65 | 69.65 | 0.51 | 2.78 | 576 |
| 2024-09-20 22:21:36.501 | MS1 | 121.4656763477 | 31.1446358426 | 211 | 504990 | -87.03 | 15.15 | 70.58 | 0.55 | 2.69 | 669 |
| 2024-09-20 22:21:37.555 | MS1 | 121.4656752163 | 31.1446378843 | 211 | 504990 | -89.63 | 8.76 | 103.74 | 0.56 | 2.64 | 523 |
| 2024-09-20 22:21:38.959 | MS1 | 121.4656685260 | 31.1446249478 | 211 | 504990 | -93.81 | 12.98 | 91.99 | 0.53 | 2.58 | 651 |
| 2024-09-20 22:21:39.487 | MS1 | 121.4656750312 | 31.1446369106 | 211 | 504990 | -92.46 | 7.43 | 67.21 | 0.64 | 2.43 | 560 |
| 2024-09-20 22:21:40.263 | MS1 | 121.4656589656 | 31.1446183330 | 211 | 504990 | -89.46 | 10.08 | 417.80 | 0.08 | 2.48 | 1579 |
| 2024-09-20 22:21:41.603 | MS1 | 121.4656607511 | 31.1446355434 | 211 | 504990 | -90.33 | 11.00 | 332.50 | 0.08 | 2.10 | 1570 |
| 2024-09-20 22:21:42.436 | MS1 | 121.4656774690 | 31.1446346971 | 211 | 504990 | -90.46 | 8.99 | 458.47 | 0.13 | 2.05 | 1570 |

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
| 3214645 | 2 | 121.4731288182 | 31.1486152691 | 241 | 4 | 0 | 15.3 | TDD | 211 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3223413 | 1 | 121.4708494046 | 31.1452113522 | 40 | 5 | 6 | 31.4 | TDD | 434 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3245439 | 3 | 121.4648311434 | 31.1528730455 | 10 | 12 | 9 | 15.6 | TDD | 783 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3253447 | 4 | 121.4703987474 | 31.1446343164 | 87 | 4 | 0 | 42.3 | TDD | 759 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:30.918 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.933 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.045 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.045 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.724 | NREventA3 | measId:2;ServCellPCI:316;Se... |
| 2024-09-20 22:21:37.964 | NRHandoverAttempt | SourcePCI:316;SourceNR-ARFC... |
| 2024-09-20 22:21:37.998 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.008 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.110 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.110 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3223413 | 1 | 15.7887 | 10.5956 | -116.7352 | 14.8631 | 84.7378 | 0.0014 | 0.0191 |
| 2024_09_20 22:00 | 3214645 | 2 | 13.6239 | 7.4430 | -114.3681 | 13.0084 | 120.4756 | 0.0107 | 0.0010 |
| 2024_09_20 22:00 | 3245439 | 3 | 12.4850 | 9.4894 | -117.3011 | 10.5612 | 154.8908 | 0.0193 | 0.0127 |
| 2024_09_20 22:00 | 3253447 | 4 | 7.5133 | 17.4866 | -116.4850 | 13.8938 | 87.9769 | 0.0077 | 0.0062 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413272_688CA828 | 504990 | 211 | -87.4 | 504990 | 783 | -90.1 | 504990 | 434 | -100.3 | 504990 | 759 |
| MR_1774413272_C432B783 | 504990 | 211 | -84.9 | 504990 | 783 | -93.9 | 504990 | 434 | -102.1 | 504990 | 759 |
| MR_1774413272_BCCA5650 | 504990 | 211 | -86.8 | 504990 | 783 | -92.9 | 504990 | 434 | -101.2 | 504990 | 759 |
| MR_1774413272_AC9D6235 | 504990 | 211 | -85.7 | 504990 | 783 | -91.4 | 504990 | 434 | -101.9 | 504990 | 759 |
| MR_1774413272_2F868702 | 504990 | 211 | -84.1 | 504990 | 783 | -94.0 | 504990 | 434 | -99.4 | 504990 | 759 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 531: `91d1abcb-260...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `91d1abcb-2609-4b8d-8b55-56d98f50494e` |
| Tag | **single-answer** |
| 정답 | **C21** |
| C21 의미 | Add neighbor relationship between 3249547_2 and 3243557_3 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[531] topology](images/train_0531.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3249547_2 by 34 degrees
- `C2`: Press down the tilt angle  of 3243557_3 by 4 degrees
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3243557_3
- `C4`: Check test server and transmission issues
- `C5`: Lift the tilt angle  of 3243557_3 by 4 degrees
- `C6`: Increase A3 Offset threshold for 3249547_2
- `C7`: Decrease A3 Offset threshold for 3249547_2
- `C8`: Adjust the azimuth of 3243557_3 by 45 degrees
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3249547_2
- `C10`: Add neighbor relationship between 3214416_4 and 3243557_3
- `C11`: Lift the tilt angle of 3249547_2 by 10 degrees
- `C12`: Insufficient data; more data is needed for judgment.
- `C13`: Press down the tilt angle of 3249547_2 by 10 degrees
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3243557_3
- `C15`: Decrease transmission power for 3249547_2
- `C16`: Decrease transmission power for 3243557_3
- `C17`: Increase A3 Offset threshold for 3243557_3
- `C18`: Increase transmission power for 3243557_3
- `C19`: Increase transmission power for 3249547_2
- `C20`: Decrease A3 Offset threshold for 3243557_3
- `C21`: Add neighbor relationship between 3249547_2 and 3243557_3 **← 정답**
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3249547_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.411 | MS1 | 121.4656582453 | 31.1446226234 | 586 | 504990 | -79.90 | 14.72 | 383.18 | 0.17 | 2.15 | 1582 |
| 2024-09-20 22:21:32.592 | MS1 | 121.4656721097 | 31.1446274378 | 586 | 504990 | -78.96 | 12.55 | 307.38 | 0.10 | 2.30 | 1587 |
| 2024-09-20 22:21:33.419 | MS1 | 121.4656650336 | 31.1446351159 | 586 | 504990 | -79.58 | 17.23 | 378.05 | 0.05 | 2.55 | 1586 |
| 2024-09-20 22:21:34.287 | MS1 | 121.4656590233 | 31.1446305101 | 586 | 504990 | -92.51 | -1.48 | 60.96 | 0.05 | 1.44 | 1592 |
| 2024-09-20 22:21:35.240 | MS1 | 121.4656675675 | 31.1446257625 | 586 | 504990 | -93.57 | -0.71 | 41.72 | 0.19 | 1.06 | 1586 |
| 2024-09-20 22:21:36.214 | MS1 | 121.4656717404 | 31.1446312974 | 586 | 504990 | -92.79 | -1.43 | 66.07 | 0.05 | 1.15 | 1585 |
| 2024-09-20 22:21:37.198 | MS1 | 121.4656727115 | 31.1446375030 | 586 | 504990 | -85.27 | -1.95 | 25.05 | 0.08 | 1.48 | 1582 |
| 2024-09-20 22:21:38.662 | MS1 | 121.4656740699 | 31.1446271444 | 586 | 504990 | -78.26 | 16.77 | 315.21 | 0.14 | 1.29 | 1589 |
| 2024-09-20 22:21:39.366 | MS1 | 121.4656747764 | 31.1446226522 | 586 | 504990 | -80.15 | 12.89 | 564.68 | 0.20 | 1.39 | 1582 |
| 2024-09-20 22:21:40.869 | MS1 | 121.4656587912 | 31.1446281022 | 586 | 504990 | -78.91 | 13.85 | 519.33 | 0.07 | 2.97 | 1580 |
| 2024-09-20 22:21:41.597 | MS1 | 121.4656605815 | 31.1446327133 | 586 | 504990 | -79.13 | 12.59 | 478.94 | 0.17 | 2.04 | 1586 |
| 2024-09-20 22:21:42.698 | MS1 | 121.4656714786 | 31.1446255121 | 586 | 504990 | -82.80 | 13.27 | 416.72 | 0.02 | 2.57 | 1571 |

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
| 3214416 | 4 | 121.4730749204 | 31.1502752772 | 273 | 13 | 8 | 39.7 | TDD | 133 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3243557 | 3 | 121.4742721419 | 31.1483138970 | 198 | 2 | 5 | 25.0 | TDD | 858 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3245582 | 1 | 121.4752720041 | 31.1476032769 | 177 | 7 | 0 | 24.5 | TDD | 480 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3249547 | 2 | 121.4679884012 | 31.1472255804 | 183 | 9 | 3 | 39.0 | TDD | 586 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |

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
| 2024-09-20 22:21:31.538 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.538 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.211 | NREventA3 | measId:2;ServCellPCI:553;Se... |
| 2024-09-20 22:21:36.211 | NREventA3 | measId:2;ServCellPCI:553;Se... |
| 2024-09-20 22:21:37.211 | NREventA3 | measId:2;ServCellPCI:553;Se... |
| 2024-09-20 22:21:39.711 | NRRRCReestablishAttempt | PCI:553 |
| 2024-09-20 22:21:39.730 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.743 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:39.877 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.877 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3245582 | 1 | 14.7429 | 7.0805 | -117.3300 | 13.0787 | 165.5420 | 0.0012 | 0.0165 |
| 2024_09_20 22:00 | 3249547 | 2 | 13.4930 | 13.0208 | -115.2693 | 5.8683 | 139.2369 | 0.0121 | 0.1166 |
| 2024_09_20 22:00 | 3243557 | 3 | 15.7558 | 17.2033 | -117.2205 | 8.4380 | 175.4172 | 0.0013 | 0.0038 |
| 2024_09_20 22:00 | 3214416 | 4 | 13.3540 | 9.8474 | -115.8855 | 16.6972 | 110.0772 | 0.0166 | 0.0094 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415998_BB87F066 | 504990 | 586 | -92.8 | 504990 | 858 | -89.4 | 504990 | 133 | -89.0 | 504990 | 480 |
| MR_1774415998_F548AE76 | 504990 | 586 | -93.7 | 504990 | 858 | -87.5 | 504990 | 133 | -89.8 | 504990 | 480 |
| MR_1774415998_F9E6A82D | 504990 | 858 | -88.9 | 504990 | 586 | -94.4 | 504990 | 133 | -87.7 | 504990 | 480 |
| MR_1774415998_96261095 | 504990 | 586 | -93.8 | 504990 | 858 | -87.0 | 504990 | 133 | -87.0 | 504990 | 480 |
| MR_1774415998_46B6336D | 504990 | 586 | -93.4 | 504990 | 858 | -89.7 | 504990 | 133 | -87.2 | 504990 | 480 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 532: `986fc26a-e0c...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `986fc26a-e0cd-4bfd-8216-a2ac19ed6dfb` |
| Tag | **single-answer** |
| 정답 | **C5** |
| C5 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3221508_3 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[532] topology](images/train_0532.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3212694_1 by 10 degrees
- `C2`: Add neighbor relationship between 3221508_3 and 3212694_1
- `C3`: Decrease transmission power for 3221508_3
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3221508_3
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3221508_3 **← 정답**
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3212694_1
- `C7`: Insufficient data; more data is needed for judgment.
- `C8`: Increase transmission power for 3221508_3
- `C9`: Decrease A3 Offset threshold for 3212694_1
- `C10`: Lift the tilt angle of 3221508_3 by 4 degrees
- `C11`: Decrease A3 Offset threshold for 3221508_3
- `C12`: Add neighbor relationship between 3236518_4 and 3212694_1
- `C13`: Increase A3 Offset threshold for 3221508_3
- `C14`: Adjust the azimuth of 3212694_1 by 50 degrees
- `C15`: Lift the tilt angle  of 3212694_1 by 10 degrees
- `C16`: Decrease transmission power for 3212694_1
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3212694_1
- `C18`: Increase A3 Offset threshold for 3212694_1
- `C19`: Increase transmission power for 3212694_1
- `C20`: Press down the tilt angle of 3221508_3 by 4 degrees
- `C21`: Adjust the azimuth of 3221508_3 by 46 degrees
- `C22`: Check test server and transmission issues

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.206 | MS1 | 121.4656655203 | 31.1446212765 | 171 | 504990 | -87.61 | 12.01 | 334.52 | 0.13 | 2.91 | 1588 |
| 2024-09-20 22:21:32.465 | MS1 | 121.4656612192 | 31.1446273336 | 171 | 504990 | -90.84 | 17.23 | 451.29 | 0.15 | 2.80 | 1586 |
| 2024-09-20 22:21:33.718 | MS1 | 121.4656606241 | 31.1446285998 | 171 | 504990 | -87.86 | 14.12 | 407.35 | 0.16 | 2.41 | 1591 |
| 2024-09-20 22:21:34.403 | MS1 | 121.4656594342 | 31.1446331254 | 171 | 504990 | -87.25 | 12.32 | 87.13 | 0.69 | 2.13 | 552 |
| 2024-09-20 22:21:35.926 | MS1 | 121.4656757823 | 31.1446271885 | 171 | 504990 | -91.09 | 15.75 | 86.30 | 0.59 | 2.21 | 668 |
| 2024-09-20 22:21:36.707 | MS1 | 121.4656610351 | 31.1446341256 | 171 | 504990 | -88.90 | 14.91 | 60.49 | 0.54 | 2.86 | 570 |
| 2024-09-20 22:21:37.600 | MS1 | 121.4656735017 | 31.1446271882 | 171 | 504990 | -90.77 | 7.18 | 74.59 | 0.64 | 2.84 | 612 |
| 2024-09-20 22:21:38.497 | MS1 | 121.4656662297 | 31.1446234797 | 171 | 504990 | -91.63 | 9.04 | 56.46 | 0.64 | 2.07 | 500 |
| 2024-09-20 22:21:39.575 | MS1 | 121.4656756310 | 31.1446214321 | 171 | 504990 | -89.94 | 11.48 | 55.42 | 0.59 | 2.29 | 626 |
| 2024-09-20 22:21:40.328 | MS1 | 121.4656614154 | 31.1446252634 | 171 | 504990 | -89.97 | 10.82 | 342.44 | 0.19 | 2.38 | 1564 |
| 2024-09-20 22:21:41.449 | MS1 | 121.4656745298 | 31.1446358506 | 171 | 504990 | -89.99 | 9.21 | 558.03 | 0.19 | 2.45 | 1575 |
| 2024-09-20 22:21:42.199 | MS1 | 121.4656748503 | 31.1446209100 | 171 | 504990 | -93.37 | 10.27 | 444.67 | 0.01 | 2.97 | 1581 |

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
| 3212694 | 1 | 121.4659278415 | 31.1493011350 | 358 | 12 | 9 | 45.8 | TDD | 178 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3221508 | 3 | 121.4656751649 | 31.1543144958 | 134 | 2 | 0 | 42.2 | TDD | 171 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3226243 | 2 | 121.4683373199 | 31.1464319464 | 3 | 3 | 11 | 15.9 | TDD | 466 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3236518 | 4 | 121.4715703594 | 31.1453496654 | 175 | 6 | 5 | 44.2 | TDD | 901 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |

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
| 2024-09-20 22:21:31.049 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.070 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.199 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.199 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.851 | NREventA3 | measId:2;ServCellPCI:647;Se... |
| 2024-09-20 22:21:38.091 | NRHandoverAttempt | SourcePCI:647;SourceNR-ARFC... |
| 2024-09-20 22:21:38.127 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.137 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.242 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.242 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3212694 | 1 | 18.7041 | 12.7076 | -116.7823 | 5.5184 | 172.0292 | 0.0120 | 0.0133 |
| 2024_09_20 22:00 | 3226243 | 2 | 16.7188 | 10.4052 | -116.1885 | 13.9128 | 147.9249 | 0.0131 | 0.0171 |
| 2024_09_20 22:00 | 3221508 | 3 | 16.8465 | 6.7083 | -117.2496 | 16.3987 | 103.5197 | 0.0006 | 0.0181 |
| 2024_09_20 22:00 | 3236518 | 4 | 12.9031 | 18.0230 | -115.8938 | 18.4554 | 103.8114 | 0.0120 | 0.0055 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417022_5EE19F10 | 504990 | 171 | -87.0 | 504990 | 178 | -93.5 | 504990 | 901 | -93.4 | 504990 | 466 |
| MR_1774417022_AA411D2C | 504990 | 171 | -88.5 | 504990 | 178 | -91.4 | 504990 | 901 | -95.4 | 504990 | 466 |
| MR_1774417022_8FC057B9 | 504990 | 171 | -87.5 | 504990 | 178 | -93.0 | 504990 | 901 | -95.3 | 504990 | 466 |
| MR_1774417022_56832751 | 504990 | 171 | -88.0 | 504990 | 178 | -91.2 | 504990 | 901 | -95.1 | 504990 | 466 |
| MR_1774417022_18695322 | 504990 | 171 | -88.8 | 504990 | 178 | -92.6 | 504990 | 901 | -94.8 | 504990 | 466 |
| MR_1774417022_576ADF68 | 504990 | 171 | -88.6 | 504990 | 178 | -94.2 | 504990 | 901 | -96.0 | 504990 | 466 |
| MR_1774417022_CD8A3E1B | 504990 | 171 | -86.9 | 504990 | 178 | -90.9 | 504990 | 901 | -95.2 | 504990 | 466 |
| MR_1774417022_7F0207C8 | 504990 | 171 | -88.1 | 504990 | 178 | -90.8 | 504990 | 901 | -96.3 | 504990 | 466 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 533: `f432ef91-04a...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `f432ef91-04a2-4165-af4a-8ab71958138f` |
| Tag | **single-answer** |
| 정답 | **C15** |
| C15 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3256338_6 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[533] topology](images/train_0533.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3256864_5
- `C2`: Adjust the azimuth of 3256864_5 by 15 degrees
- `C3`: Lift the tilt angle of 3256338_6 by 1 degrees
- `C4`: Increase transmission power for 3256338_6
- `C5`: Add neighbor relationship between 3256338_6 and 3256864_5
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3256864_5
- `C7`: Decrease transmission power for 3256338_6
- `C8`: Insufficient data; more data is needed for judgment.
- `C9`: Adjust the azimuth of 3256338_6 by 29 degrees
- `C10`: Decrease transmission power for 3256864_5
- `C11`: Increase A3 Offset threshold for 3256338_6
- `C12`: Press down the tilt angle  of 3256864_5 by 3 degrees
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3256338_6
- `C14`: Add neighbor relationship between 3242004_11 and 3256864_5
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3256338_6 **← 정답**
- `C16`: Check test server and transmission issues
- `C17`: Press down the tilt angle of 3256338_6 by 1 degrees
- `C18`: Decrease A3 Offset threshold for 3256338_6
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3256864_5
- `C20`: Increase A3 Offset threshold for 3256864_5
- `C21`: Lift the tilt angle  of 3256864_5 by 3 degrees
- `C22`: Decrease A3 Offset threshold for 3256864_5

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.847 | MS1 | 121.4656769900 | 31.1446355170 | 696 | 504990 | -93.28 | 11.31 | 452.99 | 0.06 | 2.26 | 1560 |
| 2024-09-20 22:21:32.114 | MS1 | 121.4656778150 | 31.1446290323 | 289 | 504990 | -93.23 | 11.18 | 569.62 | 0.11 | 2.39 | 1593 |
| 2024-09-20 22:21:33.915 | MS1 | 121.4656720900 | 31.1446198421 | 64 | 504990 | -94.78 | 12.85 | 402.34 | 0.12 | 2.49 | 1598 |
| 2024-09-20 22:21:34.774 | MS1 | 121.4656604256 | 31.1446321487 | 649 | 152650 | -89.70 | 5.91 | 93.21 | 0.15 | 1.91 | 955 |
| 2024-09-20 22:21:35.671 | MS1 | 121.4656718213 | 31.1446297008 | 961 | 152650 | -92.48 | 3.93 | 88.03 | 0.10 | 1.56 | 964 |
| 2024-09-20 22:21:36.175 | MS1 | 121.4656585629 | 31.1446268035 | 309 | 152650 | -93.92 | 5.09 | 88.26 | 0.13 | 1.77 | 978 |
| 2024-09-20 22:21:37.450 | MS1 | 121.4656687162 | 31.1446323261 | 881 | 152650 | -87.86 | 7.51 | 83.39 | 0.10 | 1.80 | 972 |
| 2024-09-20 22:21:38.470 | MS1 | 121.4656598437 | 31.1446218943 | 649 | 152650 | -87.84 | 5.55 | 104.44 | 0.20 | 1.87 | 965 |
| 2024-09-20 22:21:39.611 | MS1 | 121.4656624844 | 31.1446193628 | 961 | 152650 | -88.49 | 6.44 | 66.33 | 0.06 | 1.70 | 963 |
| 2024-09-20 22:21:40.372 | MS1 | 121.4656626441 | 31.1446340521 | 309 | 152650 | -96.82 | 6.03 | 67.76 | 0.07 | 2.11 | 1563 |
| 2024-09-20 22:21:41.781 | MS1 | 121.4656731141 | 31.1446211491 | 881 | 152650 | -94.19 | 6.53 | 51.48 | 0.20 | 2.67 | 1581 |
| 2024-09-20 22:21:42.861 | MS1 | 121.4656742628 | 31.1446227894 | 649 | 152650 | -90.41 | 7.86 | 98.50 | 0.18 | 2.36 | 1560 |

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
| 3217066 | 7 | 121.4663978315 | 31.1536134717 | 147 | 0 | 12 | 28.3 | FDD | 961 | n1 | 152650 | 30M | 4T4R | 23 | 152650 |
| 3220446 | 4 | 121.4687773887 | 31.1514037450 | 229 | 12 | 0 | 16.1 | TDD | 822 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3228441 | 13 | 121.4720591938 | 31.1539347947 | 187 | 10 | 9 | 0.8 | FDD | 668 | n1 | 152650 | 30M | 4T4R | 17 | 152650 |
| 3230000 | 2 | 121.4715400001 | 31.1485783681 | 55 | 9 | 12 | 13.4 | TDD | 289 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3242004 | 11 | 121.4726306606 | 31.1483876945 | 125 | 15 | 4 | 10.6 | FDD | 309 | n1 | 152650 | 30M | 4T4R | 28 | 152650 |
| 3253379 | 12 | 121.4657307191 | 31.1545334926 | 3 | 11 | 12 | 27.0 | FDD | 184 | n1 | 152650 | 30M | 4T4R | 13 | 152650 |
| 3256338 | 6 | 121.4654584166 | 31.1553038936 | 150 | 0 | 0 | 26.1 | TDD | 696 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3256864 | 5 | 121.4723982195 | 31.1542547104 | 226 | 2 | 6 | 19.8 | TDD | 247 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3256913 | 1 | 121.4650692660 | 31.1444032137 | 259 | 3 | 9 | 16.6 | TDD | 64 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3258627 | 10 | 121.4661780173 | 31.1533784729 | 291 | 13 | 11 | 22.2 | FDD | 881 | n1 | 152650 | 30M | 4T4R | 20 | 152650 |
| 3265954 | 3 | 121.4652438715 | 31.1552864081 | 11 | 11 | 5 | 6.1 | TDD | 226 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3278265 | 9 | 121.4748950283 | 31.1556823906 | 204 | 12 | 11 | 0.0 | FDD | 649 | n1 | 152650 | 30M | 4T4R | 19 | 152650 |
| 3279400 | 8 | 121.4725613046 | 31.1537578859 | 328 | 10 | 3 | 5.3 | FDD | 354 | n1 | 152650 | 30M | 4T4R | 10 | 152650 |

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
| 2024-09-20 22:21:31.581 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.598 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.717 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.717 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.447 | NREventA2 | measId:1;ServCellPCI:494;Se... |
| 2024-09-20 22:21:35.555 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.848 | NREventA5 | measId:3;ServCellPCI:494;Se... |
| 2024-09-20 22:21:35.904 | NRHandoverAttempt | SourcePCI:494;SourceNR-ARFC... |
| 2024-09-20 22:21:35.946 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.960 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:36.077 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.077 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3256913 | 1 | 11.6209 | 12.1882 | -116.0261 | 19.6880 | 150.6475 | 0.0017 | 0.0199 |
| 2024_09_20 22:00 | 3230000 | 2 | 6.6849 | 16.8057 | -116.3159 | 5.6159 | 109.9242 | 0.0077 | 0.0057 |
| 2024_09_20 22:00 | 3265954 | 3 | 13.1245 | 10.2743 | -115.5573 | 6.6644 | 153.2930 | 0.0067 | 0.0187 |
| 2024_09_20 22:00 | 3220446 | 4 | 9.2921 | 10.1618 | -116.0359 | 11.6752 | 88.5586 | 0.0183 | 0.0104 |
| 2024_09_20 22:00 | 3256864 | 5 | 15.1366 | 11.7903 | -116.7999 | 7.6241 | 151.5458 | 0.0166 | 0.0089 |
| 2024_09_20 22:00 | 3256338 | 6 | 16.6512 | 19.8284 | -116.4145 | 7.7978 | 193.9057 | 0.0125 | 0.0095 |
| 2024_09_20 22:00 | 3217066 | 7 | 18.3879 | 13.6559 | -116.2239 | 4.4602 | 43.4837 | 0.0024 | 0.0110 |
| 2024_09_20 22:00 | 3279400 | 8 | 6.6368 | 10.4441 | -116.1209 | 4.8155 | 27.7006 | 0.0078 | 0.0071 |
| 2024_09_20 22:00 | 3278265 | 9 | 13.0011 | 7.8730 | -114.9827 | 3.8720 | 20.7279 | 0.0133 | 0.0053 |
| 2024_09_20 22:00 | 3258627 | 10 | 10.6050 | 13.1816 | -117.2950 | 3.9332 | 36.7059 | 0.0085 | 0.0121 |
| 2024_09_20 22:00 | 3242004 | 11 | 10.3263 | 7.3202 | -114.8567 | 3.0737 | 46.4371 | 0.0118 | 0.0195 |
| 2024_09_20 22:00 | 3253379 | 12 | 19.4196 | 17.7027 | -114.3789 | 3.5435 | 30.2656 | 0.0089 | 0.0174 |
| 2024_09_20 22:00 | 3228441 | 13 | 13.2201 | 12.4042 | -115.3152 | 3.6022 | 48.0803 | 0.0079 | 0.0169 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416376_5BEDD9FA | 504990 | 64 | -93.5 | 504990 | 247 | -89.3 | 504990 | 226 | -101.9 | 504990 | 822 |
| MR_1774416376_CB872B89 | 152650 | 649 | -87.9 | 152650 | 354 | -95.1 | 152650 | 668 | -95.4 | 152650 | 184 |
| MR_1774416376_9C61BBA8 | 152650 | 649 | -89.9 | 152650 | 354 | -95.2 | 152650 | 668 | -96.1 | 152650 | 184 |
| MR_1774416376_BF990415 | 152650 | 649 | -89.7 | 152650 | 354 | -94.4 | 152650 | 668 | -95.4 | 152650 | 184 |
| MR_1774416376_0D23BA5C | 152650 | 649 | -89.3 | 152650 | 354 | -97.2 | 152650 | 668 | -97.6 | 152650 | 184 |
| MR_1774416376_E756A957 | 152650 | 649 | -90.7 | 152650 | 354 | -96.6 | 152650 | 668 | -96.3 | 152650 | 184 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 534: `7f8ca1f1-d9e...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `7f8ca1f1-d9ea-4f65-959c-5a4822228377` |
| Tag | **single-answer** |
| 정답 | **C1** |
| C1 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3263493_1 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[534] topology](images/train_0534.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3263493_1 **← 정답**
- `C2`: Check test server and transmission issues
- `C3`: Decrease transmission power for 3263493_1
- `C4`: Increase A3 Offset threshold for 3263493_1
- `C5`: Lift the tilt angle  of 3245302_2 by 10 degrees
- `C6`: Press down the tilt angle  of 3245302_2 by 10 degrees
- `C7`: Add neighbor relationship between 3263493_1 and 3245302_2
- `C8`: Increase A3 Offset threshold for 3245302_2
- `C9`: Insufficient data; more data is needed for judgment.
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3263493_1
- `C11`: Increase transmission power for 3245302_2
- `C12`: Decrease transmission power for 3245302_2
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3245302_2
- `C14`: Adjust the azimuth of 3245302_2 by 42 degrees
- `C15`: Add neighbor relationship between 3243724_3 and 3245302_2
- `C16`: Increase transmission power for 3263493_1
- `C17`: Decrease A3 Offset threshold for 3263493_1
- `C18`: Adjust the azimuth of 3263493_1 by 16 degrees
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3245302_2
- `C20`: Decrease A3 Offset threshold for 3245302_2
- `C21`: Lift the tilt angle of 3263493_1 by 5 degrees
- `C22`: Press down the tilt angle of 3263493_1 by 5 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.123 | MS1 | 121.4656710300 | 31.1446276646 | 17 | 504990 | -87.42 | 12.66 | 365.15 | 0.08 | 2.62 | 1570 |
| 2024-09-20 22:21:32.549 | MS1 | 121.4656625006 | 31.1446201899 | 17 | 504990 | -89.35 | 14.78 | 345.89 | 0.20 | 2.64 | 1594 |
| 2024-09-20 22:21:33.367 | MS1 | 121.4656749675 | 31.1446342303 | 17 | 504990 | -91.83 | 13.30 | 370.02 | 0.07 | 2.96 | 1579 |
| 2024-09-20 22:21:34.149 | MS1 | 121.4656614740 | 31.1446187152 | 17 | 504990 | -90.24 | 16.59 | 65.98 | 0.69 | 2.30 | 527 |
| 2024-09-20 22:21:35.565 | MS1 | 121.4656746007 | 31.1446371170 | 17 | 504990 | -85.69 | 15.23 | 53.31 | 0.68 | 2.03 | 688 |
| 2024-09-20 22:21:36.988 | MS1 | 121.4656708713 | 31.1446323206 | 17 | 504990 | -87.42 | 14.70 | 53.24 | 0.60 | 2.22 | 626 |
| 2024-09-20 22:21:37.951 | MS1 | 121.4656761546 | 31.1446232093 | 17 | 504990 | -92.76 | 10.46 | 86.82 | 0.59 | 2.05 | 549 |
| 2024-09-20 22:21:38.893 | MS1 | 121.4656674467 | 31.1446184871 | 17 | 504990 | -93.77 | 12.11 | 82.61 | 0.53 | 2.07 | 597 |
| 2024-09-20 22:21:39.948 | MS1 | 121.4656641834 | 31.1446276692 | 17 | 504990 | -93.25 | 7.95 | 57.94 | 0.61 | 2.51 | 554 |
| 2024-09-20 22:21:40.314 | MS1 | 121.4656619956 | 31.1446276480 | 17 | 504990 | -91.29 | 10.29 | 501.16 | 0.17 | 2.63 | 1580 |
| 2024-09-20 22:21:41.829 | MS1 | 121.4656715236 | 31.1446336718 | 17 | 504990 | -91.49 | 8.24 | 316.62 | 0.16 | 2.36 | 1588 |
| 2024-09-20 22:21:42.734 | MS1 | 121.4656745121 | 31.1446268178 | 17 | 504990 | -92.36 | 7.76 | 347.15 | 0.14 | 2.07 | 1584 |

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
| 3243724 | 3 | 121.4722005038 | 31.1540892388 | 242 | 13 | 8 | 22.5 | TDD | 382 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3245302 | 2 | 121.4709484057 | 31.1535428325 | 165 | 14 | 3 | 37.9 | TDD | 284 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3251015 | 4 | 121.4757796822 | 31.1459407893 | 255 | 13 | 1 | 15.1 | TDD | 903 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3263493 | 1 | 121.4730040638 | 31.1449497060 | 283 | 1 | 8 | 43.1 | TDD | 17 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:31.527 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.547 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.678 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.678 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.359 | NREventA3 | measId:2;ServCellPCI:463;Se... |
| 2024-09-20 22:21:38.599 | NRHandoverAttempt | SourcePCI:463;SourceNR-ARFC... |
| 2024-09-20 22:21:38.646 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.661 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.767 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.767 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3263493 | 1 | 8.6749 | 10.0992 | -117.9851 | 9.9305 | 199.7891 | 0.0109 | 0.0178 |
| 2024_09_20 22:00 | 3245302 | 2 | 8.8046 | 5.3114 | -114.1273 | 5.9592 | 185.2559 | 0.0189 | 0.0093 |
| 2024_09_20 22:00 | 3243724 | 3 | 19.4603 | 11.2316 | -117.1684 | 15.8977 | 165.9768 | 0.0063 | 0.0022 |
| 2024_09_20 22:00 | 3251015 | 4 | 19.5947 | 16.7172 | -115.9247 | 12.0778 | 149.5163 | 0.0083 | 0.0086 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416177_038FDAF1 | 504990 | 17 | -92.0 | 504990 | 284 | -95.2 | 504990 | 382 | -105.0 | 504990 | 903 |
| MR_1774416177_39F9C542 | 504990 | 17 | -90.8 | 504990 | 284 | -96.4 | 504990 | 382 | -103.7 | 504990 | 903 |
| MR_1774416177_92B9E491 | 504990 | 17 | -89.7 | 504990 | 284 | -94.6 | 504990 | 382 | -105.3 | 504990 | 903 |
| MR_1774416177_0723C487 | 504990 | 17 | -90.8 | 504990 | 284 | -96.3 | 504990 | 382 | -106.3 | 504990 | 903 |
| MR_1774416177_37F24EE4 | 504990 | 17 | -90.7 | 504990 | 284 | -96.0 | 504990 | 382 | -106.3 | 504990 | 903 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 535: `913385d6-133...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `913385d6-1339-46aa-9a59-834dde3664f5` |
| Tag | **single-answer** |
| 정답 | **C11** |
| C11 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[535] topology](images/train_0535.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3217235_2
- `C2`: Adjust the azimuth of 3262695_1 by 50 degrees
- `C3`: Decrease transmission power for 3217235_2
- `C4`: Press down the tilt angle  of 3217235_2 by 9 degrees
- `C5`: Increase transmission power for 3262695_1
- `C6`: Lift the tilt angle  of 3217235_2 by 9 degrees
- `C7`: Decrease A3 Offset threshold for 3262695_1
- `C8`: Check test server and transmission issues
- `C9`: Adjust the azimuth of 3217235_2 by 50 degrees
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3262695_1
- `C11`: Insufficient data; more data is needed for judgment. **← 정답**
- `C12`: Add neighbor relationship between 3221997_3 and 3217235_2
- `C13`: Press down the tilt angle of 3262695_1 by 10 degrees
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3262695_1
- `C15`: Decrease A3 Offset threshold for 3217235_2
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3217235_2
- `C17`: Increase transmission power for 3217235_2
- `C18`: Increase A3 Offset threshold for 3217235_2
- `C19`: Decrease transmission power for 3262695_1
- `C20`: Add neighbor relationship between 3262695_1 and 3217235_2
- `C21`: Lift the tilt angle of 3262695_1 by 10 degrees
- `C22`: Increase A3 Offset threshold for 3262695_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.242 | MS1 | 121.4656583205 | 31.1446227411 | 360 | 504990 | -86.19 | 16.34 | 322.01 | 0.20 | 2.27 | 1571 |
| 2024-09-20 22:21:32.516 | MS1 | 121.4656703485 | 31.1446235258 | 360 | 504990 | -89.92 | 14.53 | 572.71 | 0.13 | 2.53 | 1578 |
| 2024-09-20 22:21:33.547 | MS1 | 121.4656671017 | 31.1446340296 | 360 | 504990 | -85.69 | 12.43 | 554.31 | 0.10 | 2.44 | 1568 |
| 2024-09-20 22:21:34.993 | MS1 | 121.4656621571 | 31.1446273482 | 360 | 504990 | -87.14 | 15.23 | 81.34 | 0.12 | 2.10 | 1571 |
| 2024-09-20 22:21:35.412 | MS1 | 121.4656620951 | 31.1446347686 | 360 | 504990 | -90.57 | 12.60 | 65.97 | 0.15 | 2.46 | 1589 |
| 2024-09-20 22:21:36.216 | MS1 | 121.4656710252 | 31.1446192835 | 360 | 504990 | -85.49 | 16.26 | 67.58 | 0.16 | 2.68 | 1561 |
| 2024-09-20 22:21:37.531 | MS1 | 121.4656710831 | 31.1446211104 | 360 | 504990 | -93.61 | 7.89 | 106.23 | 0.04 | 2.74 | 1563 |
| 2024-09-20 22:21:38.640 | MS1 | 121.4656778514 | 31.1446229221 | 360 | 504990 | -90.63 | 12.71 | 60.64 | 0.15 | 2.98 | 1590 |
| 2024-09-20 22:21:39.628 | MS1 | 121.4656735132 | 31.1446363444 | 360 | 504990 | -90.59 | 10.19 | 67.17 | 0.18 | 2.85 | 1594 |
| 2024-09-20 22:21:40.999 | MS1 | 121.4656771233 | 31.1446224772 | 360 | 504990 | -91.08 | 10.47 | 394.53 | 0.00 | 2.99 | 1573 |
| 2024-09-20 22:21:41.410 | MS1 | 121.4656711807 | 31.1446295967 | 360 | 504990 | -89.89 | 7.91 | 487.60 | 0.19 | 2.37 | 1570 |
| 2024-09-20 22:21:42.102 | MS1 | 121.4656746270 | 31.1446372739 | 360 | 504990 | -89.74 | 12.20 | 380.81 | 0.10 | 2.61 | 1578 |

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
| 3217235 | 2 | 121.4709386225 | 31.1485660743 | 44 | 7 | 9 | 27.6 | TDD | 328 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3221997 | 3 | 121.4711285531 | 31.1473259348 | 311 | 9 | 11 | 49.4 | TDD | 758 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3223869 | 4 | 121.4756468242 | 31.1544328137 | 29 | 1 | 12 | 44.4 | TDD | 503 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3262695 | 1 | 121.4661773575 | 31.1499235249 | 301 | 8 | 4 | 35.2 | TDD | 360 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:31.083 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.102 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.245 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.245 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.891 | NREventA3 | measId:2;ServCellPCI:232;Se... |
| 2024-09-20 22:21:38.131 | NRHandoverAttempt | SourcePCI:232;SourceNR-ARFC... |
| 2024-09-20 22:21:38.179 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.190 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.293 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.293 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3262695 | 1 | 76.1254 | 88.6063 | -116.5936 | 10.3505 | 98.5574 | 0.0002 | 0.0143 |
| 2024_09_19 22:00 | 3217235 | 2 | 89.1228 | 80.1042 | -115.5729 | 19.2114 | 166.9793 | 0.0150 | 0.0158 |
| 2024_09_19 22:00 | 3221997 | 3 | 88.5771 | 86.3692 | -114.9592 | 12.0095 | 174.6617 | 0.0001 | 0.0195 |
| 2024_09_19 22:00 | 3223869 | 4 | 75.7553 | 76.7657 | -114.3085 | 6.7783 | 183.3599 | 0.0087 | 0.0186 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415176_57A5AC8E | 504990 | 360 | -86.2 | 504990 | 328 | -95.1 | 504990 | 758 | -97.6 | 504990 | 503 |
| MR_1774415176_40FE597D | 504990 | 360 | -85.9 | 504990 | 328 | -96.9 | 504990 | 758 | -99.1 | 504990 | 503 |
| MR_1774415176_9C37E0DE | 504990 | 360 | -88.8 | 504990 | 328 | -93.4 | 504990 | 758 | -100.5 | 504990 | 503 |
| MR_1774415176_84928DD7 | 504990 | 360 | -88.7 | 504990 | 328 | -93.5 | 504990 | 758 | -101.2 | 504990 | 503 |
| MR_1774415176_BE4716B3 | 504990 | 360 | -87.9 | 504990 | 328 | -95.4 | 504990 | 758 | -100.2 | 504990 | 503 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 536: `fdacc653-e2b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `fdacc653-e2b4-435b-a2d0-65e83c13d3f5` |
| Tag | **single-answer** |
| 정답 | **C6** |
| C6 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3278404_6 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[536] topology](images/train_0536.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3229118_8 and 3216154_3
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3278404_6
- `C3`: Increase transmission power for 3278404_6
- `C4`: Lift the tilt angle of 3278404_6 by 3 degrees
- `C5`: Increase A3 Offset threshold for 3278404_6
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3278404_6 **← 정답**
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3216154_3
- `C8`: Increase transmission power for 3216154_3
- `C9`: Decrease transmission power for 3216154_3
- `C10`: Press down the tilt angle of 3278404_6 by 3 degrees
- `C11`: Press down the tilt angle  of 3216154_3 by 3 degrees
- `C12`: Adjust the azimuth of 3216154_3 by 23 degrees
- `C13`: Lift the tilt angle  of 3216154_3 by 3 degrees
- `C14`: Adjust the azimuth of 3278404_6 by 1 degrees
- `C15`: Insufficient data; more data is needed for judgment.
- `C16`: Increase A3 Offset threshold for 3216154_3
- `C17`: Check test server and transmission issues
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3216154_3
- `C19`: Decrease A3 Offset threshold for 3216154_3
- `C20`: Decrease transmission power for 3278404_6
- `C21`: Add neighbor relationship between 3278404_6 and 3216154_3
- `C22`: Decrease A3 Offset threshold for 3278404_6

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.231 | MS1 | 121.4656738906 | 31.1446297988 | 155 | 504990 | -93.84 | 11.70 | 349.70 | 0.12 | 2.70 | 1584 |
| 2024-09-20 22:21:32.684 | MS1 | 121.4656687068 | 31.1446264806 | 676 | 504990 | -95.85 | 14.20 | 423.33 | 0.02 | 2.74 | 1583 |
| 2024-09-20 22:21:33.214 | MS1 | 121.4656630691 | 31.1446254837 | 267 | 504990 | -94.75 | 9.45 | 390.17 | 0.17 | 2.45 | 1564 |
| 2024-09-20 22:21:34.251 | MS1 | 121.4656763050 | 31.1446366571 | 744 | 152650 | -93.33 | 7.08 | 69.47 | 0.16 | 1.76 | 995 |
| 2024-09-20 22:21:35.143 | MS1 | 121.4656742047 | 31.1446210705 | 282 | 152650 | -90.98 | 6.86 | 62.72 | 0.02 | 1.55 | 998 |
| 2024-09-20 22:21:36.450 | MS1 | 121.4656687715 | 31.1446216111 | 293 | 152650 | -95.20 | 4.90 | 63.75 | 0.16 | 1.89 | 905 |
| 2024-09-20 22:21:37.843 | MS1 | 121.4656639991 | 31.1446241381 | 785 | 152650 | -89.61 | 5.88 | 62.66 | 0.15 | 1.83 | 998 |
| 2024-09-20 22:21:38.440 | MS1 | 121.4656648861 | 31.1446342653 | 744 | 152650 | -91.96 | 5.78 | 90.28 | 0.19 | 1.98 | 985 |
| 2024-09-20 22:21:39.498 | MS1 | 121.4656744031 | 31.1446199313 | 282 | 152650 | -90.72 | 4.55 | 97.93 | 0.18 | 1.62 | 952 |
| 2024-09-20 22:21:40.303 | MS1 | 121.4656709702 | 31.1446200680 | 293 | 152650 | -95.79 | 3.91 | 78.10 | 0.17 | 2.83 | 1578 |
| 2024-09-20 22:21:41.501 | MS1 | 121.4656689136 | 31.1446323662 | 785 | 152650 | -92.83 | 2.89 | 93.15 | 0.15 | 2.92 | 1582 |
| 2024-09-20 22:21:42.427 | MS1 | 121.4656663331 | 31.1446233565 | 744 | 152650 | -88.23 | 6.36 | 51.72 | 0.08 | 2.05 | 1560 |

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
| 3211826 | 11 | 121.4732839363 | 31.1540734109 | 162 | 3 | 6 | 7.8 | FDD | 785 | n1 | 152650 | 30M | 4T4R | 27 | 152650 |
| 3215876 | 7 | 121.4676399110 | 31.1534050277 | 146 | 4 | 5 | 12.9 | FDD | 98 | n1 | 152650 | 30M | 4T4R | 14 | 152650 |
| 3216154 | 3 | 121.4739146881 | 31.1442272686 | 250 | 2 | 5 | 7.9 | TDD | 490 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3216482 | 5 | 121.4686178886 | 31.1536287217 | 346 | 7 | 10 | 12.2 | TDD | 440 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3229118 | 8 | 121.4664354479 | 31.1506492765 | 99 | 4 | 5 | 20.0 | FDD | 293 | n1 | 152650 | 30M | 4T4R | 25 | 152650 |
| 3230480 | 4 | 121.4751449405 | 31.1459409548 | 40 | 8 | 11 | 15.5 | TDD | 267 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3233451 | 10 | 121.4737084168 | 31.1516077703 | 212 | 12 | 1 | 29.9 | FDD | 111 | n1 | 152650 | 30M | 4T4R | 21 | 152650 |
| 3243169 | 1 | 121.4663018169 | 31.1473745628 | 14 | 15 | 2 | 20.8 | TDD | 416 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3253948 | 12 | 121.4759706222 | 31.1513330559 | 233 | 11 | 11 | 1.3 | FDD | 119 | n1 | 152650 | 30M | 4T4R | 14 | 152650 |
| 3261718 | 9 | 121.4690767141 | 31.1444189172 | 282 | 9 | 8 | 3.2 | FDD | 744 | n1 | 152650 | 30M | 4T4R | 24 | 152650 |
| 3278100 | 13 | 121.4713393200 | 31.1541679394 | 323 | 5 | 8 | 2.1 | FDD | 282 | n1 | 152650 | 30M | 4T4R | 12 | 152650 |
| 3278404 | 6 | 121.4754896523 | 31.1508691256 | 234 | 2 | 12 | 15.5 | TDD | 155 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3279267 | 2 | 121.4709458403 | 31.1458295538 | 72 | 7 | 0 | 11.7 | TDD | 676 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |

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
| 2024-09-20 22:21:31.395 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.411 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.515 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.515 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.220 | NREventA2 | measId:1;ServCellPCI:97;Ser... |
| 2024-09-20 22:21:35.365 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.649 | NREventA5 | measId:3;ServCellPCI:97;Ser... |
| 2024-09-20 22:21:35.688 | NRHandoverAttempt | SourcePCI:97;SourceNR-ARFCN... |
| 2024-09-20 22:21:35.727 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.737 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:35.866 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.866 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3243169 | 1 | 12.9173 | 18.9885 | -116.4902 | 11.2889 | 84.1262 | 0.0070 | 0.0056 |
| 2024_09_20 22:00 | 3279267 | 2 | 19.9774 | 11.1088 | -114.8125 | 11.6909 | 102.0062 | 0.0059 | 0.0082 |
| 2024_09_20 22:00 | 3216154 | 3 | 9.8764 | 7.1667 | -116.8615 | 19.2247 | 147.5571 | 0.0064 | 0.0112 |
| 2024_09_20 22:00 | 3230480 | 4 | 9.7405 | 12.6301 | -114.3995 | 13.6435 | 131.7706 | 0.0175 | 0.0164 |
| 2024_09_20 22:00 | 3216482 | 5 | 17.6289 | 10.7790 | -116.2171 | 19.0949 | 184.9565 | 0.0182 | 0.0128 |
| 2024_09_20 22:00 | 3278404 | 6 | 7.0989 | 9.7935 | -115.7617 | 19.6115 | 105.4707 | 0.0195 | 0.0136 |
| 2024_09_20 22:00 | 3215876 | 7 | 16.8335 | 19.0462 | -116.2202 | 4.2223 | 48.6766 | 0.0022 | 0.0192 |
| 2024_09_20 22:00 | 3229118 | 8 | 9.4346 | 12.4221 | -114.5839 | 4.0172 | 31.2000 | 0.0112 | 0.0030 |
| 2024_09_20 22:00 | 3261718 | 9 | 14.4630 | 19.0703 | -116.8725 | 3.6345 | 24.2170 | 0.0079 | 0.0008 |
| 2024_09_20 22:00 | 3233451 | 10 | 8.8379 | 6.7299 | -116.1966 | 4.7836 | 40.7366 | 0.0085 | 0.0065 |
| 2024_09_20 22:00 | 3211826 | 11 | 12.8144 | 19.1637 | -117.7092 | 3.8670 | 24.4524 | 0.0163 | 0.0191 |
| 2024_09_20 22:00 | 3253948 | 12 | 9.0490 | 17.6667 | -116.9298 | 3.7724 | 20.3219 | 0.0195 | 0.0116 |
| 2024_09_20 22:00 | 3278100 | 13 | 6.2268 | 7.9408 | -115.2297 | 3.2367 | 51.1797 | 0.0007 | 0.0114 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412705_EEEEC083 | 504990 | 267 | -96.7 | 504990 | 490 | -94.4 | 504990 | 416 | -94.8 | 504990 | 440 |
| MR_1774412705_0C5FFD31 | 152650 | 744 | -94.8 | 152650 | 98 | -98.8 | 152650 | 119 | -100.1 | 152650 | 111 |
| MR_1774412705_CDE669B1 | 152650 | 744 | -93.7 | 152650 | 98 | -99.6 | 152650 | 119 | -98.8 | 152650 | 111 |
| MR_1774412705_D46D94A4 | 504990 | 267 | -96.2 | 504990 | 490 | -93.2 | 504990 | 416 | -96.2 | 504990 | 440 |
| MR_1774412705_0E5D919B | 504990 | 267 | -96.6 | 504990 | 490 | -95.0 | 504990 | 416 | -94.1 | 504990 | 440 |
| MR_1774412705_B3D1A92A | 152650 | 744 | -94.1 | 152650 | 98 | -97.2 | 152650 | 119 | -99.6 | 152650 | 111 |
| MR_1774412705_70273943 | 152650 | 744 | -94.2 | 152650 | 98 | -97.8 | 152650 | 119 | -99.1 | 152650 | 111 |
| MR_1774412705_EFB347F4 | 152650 | 744 | -94.3 | 152650 | 98 | -99.4 | 152650 | 119 | -101.5 | 152650 | 111 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 537: `e4ab116d-ce4...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `e4ab116d-ce47-42e2-8acb-7fd1f6351c49` |
| Tag | **single-answer** |
| 정답 | **C5** |
| C5 의미 | Lift the tilt angle  of 3244314_2 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[537] topology](images/train_0537.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3213447_4
- `C2`: Add neighbor relationship between 3213447_4 and 3237431_3
- `C3`: Increase transmission power for 3213447_4
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3237431_3
- `C5`: Lift the tilt angle  of 3244314_2 by 10 degrees **← 정답**
- `C6`: Decrease A3 Offset threshold for 3213447_4
- `C7`: Insufficient data; more data is needed for judgment.
- `C8`: Decrease transmission power for 3213447_4
- `C9`: Increase transmission power for 3237431_3
- `C10`: Increase A3 Offset threshold for 3237431_3
- `C11`: Press down the tilt angle of 3213447_4 by 4 degrees
- `C12`: Decrease transmission power for 3237431_3
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3213447_4
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3237431_3
- `C15`: Adjust the azimuth of 3213447_4 by 26 degrees
- `C16`: Decrease A3 Offset threshold for 3237431_3
- `C17`: Check test server and transmission issues
- `C18`: Adjust the azimuth of 3244314_2 by 50 degrees
- `C19`: Press down the tilt angle  of 3244314_2 by 10 degrees
- `C20`: Lift the tilt angle of 3213447_4 by 4 degrees
- `C21`: Increase A3 Offset threshold for 3213447_4
- `C22`: Add neighbor relationship between 3244314_2 and 3237431_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.818 | MS1 | 121.4656693597 | 31.1446271355 | 575 | 504990 | -87.64 | 13.53 | 312.05 | 0.16 | 2.44 | 1567 |
| 2024-09-20 22:21:32.134 | MS1 | 121.4656667985 | 31.1446367937 | 575 | 504990 | -86.95 | 12.65 | 492.77 | 0.13 | 2.42 | 1577 |
| 2024-09-20 22:21:33.413 | MS1 | 121.4656627413 | 31.1446353951 | 575 | 504990 | -88.57 | 14.80 | 401.33 | 0.17 | 2.75 | 1571 |
| 2024-09-20 22:21:34.576 | MS1 | 121.4656677392 | 31.1446367742 | 575 | 504990 | -85.30 | 13.25 | 80.31 | 0.12 | 2.70 | 1577 |
| 2024-09-20 22:21:35.755 | MS1 | 121.4656664301 | 31.1446343056 | 575 | 504990 | -86.56 | 17.32 | 57.16 | 0.14 | 2.30 | 1592 |
| 2024-09-20 22:21:36.904 | MS1 | 121.4656774158 | 31.1446189235 | 575 | 504990 | -85.46 | 17.44 | 94.47 | 0.02 | 2.88 | 1595 |
| 2024-09-20 22:21:37.433 | MS1 | 121.4656659916 | 31.1446322297 | 575 | 504990 | -89.21 | 8.91 | 86.07 | 0.11 | 2.47 | 1588 |
| 2024-09-20 22:21:38.594 | MS1 | 121.4656743415 | 31.1446236019 | 575 | 504990 | -89.46 | 10.99 | 59.94 | 0.17 | 2.67 | 1564 |
| 2024-09-20 22:21:39.324 | MS1 | 121.4656747637 | 31.1446219176 | 575 | 504990 | -89.16 | 12.97 | 64.24 | 0.03 | 2.88 | 1594 |
| 2024-09-20 22:21:40.404 | MS1 | 121.4656589243 | 31.1446346170 | 575 | 504990 | -92.68 | 9.06 | 415.71 | 0.14 | 2.82 | 1587 |
| 2024-09-20 22:21:41.487 | MS1 | 121.4656609211 | 31.1446339000 | 575 | 504990 | -89.88 | 8.42 | 523.93 | 0.06 | 2.89 | 1590 |
| 2024-09-20 22:21:42.482 | MS1 | 121.4656687553 | 31.1446295726 | 575 | 504990 | -89.55 | 7.95 | 545.35 | 0.13 | 2.77 | 1594 |

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
| 3213447 | 4 | 121.4724695838 | 31.1450343750 | 240 | 1 | 0 | 37.9 | TDD | 575 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3237431 | 3 | 121.4697954696 | 31.1445458575 | 196 | 11 | 11 | 42.9 | TDD | 596 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3244314 | 2 | 121.4716359033 | 31.1549549568 | 38 | 6 | 5 | 23.4 | TDD | 947 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3244893 | 1 | 121.4727955464 | 31.1461700857 | 41 | 1 | 7 | 44.1 | TDD | 162 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |

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
| 2024-09-20 22:21:30.973 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.991 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.092 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.092 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.804 | NREventA3 | measId:2;ServCellPCI:855;Se... |
| 2024-09-20 22:21:38.044 | NRHandoverAttempt | SourcePCI:855;SourceNR-ARFC... |
| 2024-09-20 22:21:38.074 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.086 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.189 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.189 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3244893 | 1 | 12.5771 | 13.6812 | -114.4617 | 5.7953 | 128.9601 | 0.0179 | 0.0158 |
| 2024_09_20 22:00 | 3244314 | 2 | 11.0197 | 15.2439 | -115.7496 | 16.5382 | 121.9255 | 0.0029 | 0.0171 |
| 2024_09_20 22:00 | 3237431 | 3 | 17.3740 | 19.2893 | -115.4251 | 6.0374 | 126.6000 | 0.0088 | 0.0118 |
| 2024_09_20 22:00 | 3213447 | 4 | 77.8932 | 92.0470 | -114.2092 | 16.6210 | 154.5774 | 0.0098 | 0.0152 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416794_ACA9F20F | 504990 | 575 | -86.9 | 504990 | 596 | -90.7 | 504990 | 947 | -96.1 | 504990 | 162 |
| MR_1774416794_D58EF187 | 504990 | 575 | -84.3 | 504990 | 596 | -90.2 | 504990 | 947 | -96.9 | 504990 | 162 |
| MR_1774416794_5BDA823B | 504990 | 575 | -85.6 | 504990 | 596 | -88.4 | 504990 | 947 | -99.3 | 504990 | 162 |
| MR_1774416794_1F7E28BA | 504990 | 575 | -84.8 | 504990 | 596 | -89.6 | 504990 | 947 | -99.0 | 504990 | 162 |
| MR_1774416794_DE3FB35F | 504990 | 575 | -86.8 | 504990 | 596 | -87.7 | 504990 | 947 | -98.9 | 504990 | 162 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 538: `7a0d8a4f-cca...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `7a0d8a4f-ccaa-457b-b514-352bd2076b15` |
| Tag | **single-answer** |
| 정답 | **C1** |
| C1 의미 | Lift the tilt angle  of 3276035_1 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[538] topology](images/train_0538.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle  of 3276035_1 by 10 degrees **← 정답**
- `C2`: Increase transmission power for 3259706_4
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3259706_4
- `C4`: Decrease A3 Offset threshold for 3259706_4
- `C5`: Insufficient data; more data is needed for judgment.
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3259706_4
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3239606_3
- `C8`: Press down the tilt angle  of 3276035_1 by 10 degrees
- `C9`: Decrease transmission power for 3239606_3
- `C10`: Check test server and transmission issues
- `C11`: Press down the tilt angle of 3259706_4 by 6 degrees
- `C12`: Decrease A3 Offset threshold for 3239606_3
- `C13`: Adjust the azimuth of 3276035_1 by 50 degrees
- `C14`: Increase transmission power for 3239606_3
- `C15`: Adjust the azimuth of 3259706_4 by 10 degrees
- `C16`: Increase A3 Offset threshold for 3239606_3
- `C17`: Add neighbor relationship between 3259706_4 and 3239606_3
- `C18`: Add neighbor relationship between 3276035_1 and 3239606_3
- `C19`: Decrease transmission power for 3259706_4
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3239606_3
- `C21`: Increase A3 Offset threshold for 3259706_4
- `C22`: Lift the tilt angle of 3259706_4 by 6 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.954 | MS1 | 121.4656675525 | 31.1446205039 | 687 | 504990 | -86.99 | 13.65 | 383.40 | 0.09 | 2.49 | 1561 |
| 2024-09-20 22:21:32.291 | MS1 | 121.4656654773 | 31.1446238183 | 687 | 504990 | -88.51 | 14.00 | 344.37 | 0.06 | 2.16 | 1563 |
| 2024-09-20 22:21:33.241 | MS1 | 121.4656671280 | 31.1446315109 | 687 | 504990 | -85.82 | 14.44 | 444.76 | 0.10 | 2.67 | 1591 |
| 2024-09-20 22:21:34.337 | MS1 | 121.4656662367 | 31.1446180854 | 687 | 504990 | -90.67 | 17.88 | 85.31 | 0.04 | 2.55 | 1589 |
| 2024-09-20 22:21:35.787 | MS1 | 121.4656681033 | 31.1446193890 | 687 | 504990 | -86.96 | 12.85 | 67.50 | 0.05 | 2.97 | 1561 |
| 2024-09-20 22:21:36.639 | MS1 | 121.4656728664 | 31.1446257917 | 687 | 504990 | -89.49 | 15.87 | 85.58 | 0.12 | 2.17 | 1585 |
| 2024-09-20 22:21:37.484 | MS1 | 121.4656769917 | 31.1446249800 | 687 | 504990 | -92.24 | 11.06 | 47.67 | 0.03 | 2.28 | 1564 |
| 2024-09-20 22:21:38.782 | MS1 | 121.4656700282 | 31.1446240707 | 687 | 504990 | -89.31 | 10.78 | 54.60 | 0.05 | 2.55 | 1561 |
| 2024-09-20 22:21:39.986 | MS1 | 121.4656733492 | 31.1446246050 | 687 | 504990 | -90.68 | 9.81 | 80.41 | 0.11 | 2.47 | 1567 |
| 2024-09-20 22:21:40.332 | MS1 | 121.4656777185 | 31.1446284080 | 687 | 504990 | -90.50 | 10.40 | 309.99 | 0.14 | 2.83 | 1563 |
| 2024-09-20 22:21:41.357 | MS1 | 121.4656660958 | 31.1446247095 | 687 | 504990 | -92.87 | 8.28 | 347.47 | 0.06 | 2.91 | 1570 |
| 2024-09-20 22:21:42.293 | MS1 | 121.4656635788 | 31.1446326498 | 687 | 504990 | -91.51 | 9.33 | 543.73 | 0.17 | 2.94 | 1567 |

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
| 3212941 | 2 | 121.4733777252 | 31.1515934947 | 116 | 12 | 12 | 39.6 | TDD | 835 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3239606 | 3 | 121.4682078312 | 31.1479160843 | 283 | 12 | 2 | 21.1 | TDD | 139 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3259706 | 4 | 121.4714838082 | 31.1498974025 | 233 | 3 | 6 | 40.5 | TDD | 687 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3276035 | 1 | 121.4674696133 | 31.1515526483 | 79 | 8 | 3 | 19.4 | TDD | 464 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |

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
| 2024-09-20 22:21:31.309 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.334 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.462 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.462 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.185 | NREventA3 | measId:2;ServCellPCI:308;Se... |
| 2024-09-20 22:21:38.425 | NRHandoverAttempt | SourcePCI:308;SourceNR-ARFC... |
| 2024-09-20 22:21:38.458 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.469 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.576 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.576 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3276035 | 1 | 17.2956 | 8.4662 | -115.8788 | 12.0200 | 96.6421 | 0.0002 | 0.0072 |
| 2024_09_20 22:00 | 3212941 | 2 | 19.4029 | 7.4410 | -117.3091 | 10.4566 | 102.9214 | 0.0116 | 0.0058 |
| 2024_09_20 22:00 | 3239606 | 3 | 5.3643 | 9.9915 | -115.4864 | 11.7100 | 172.1930 | 0.0192 | 0.0041 |
| 2024_09_20 22:00 | 3259706 | 4 | 90.6722 | 93.9238 | -114.8868 | 10.8953 | 194.3444 | 0.0153 | 0.0045 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414140_7B8783ED | 504990 | 687 | -92.4 | 504990 | 139 | -96.7 | 504990 | 464 | -97.8 | 504990 | 835 |
| MR_1774414140_D68BE446 | 504990 | 687 | -92.6 | 504990 | 139 | -96.1 | 504990 | 464 | -97.5 | 504990 | 835 |
| MR_1774414140_B63D7AF8 | 504990 | 687 | -90.3 | 504990 | 139 | -99.0 | 504990 | 464 | -96.4 | 504990 | 835 |
| MR_1774414140_F97858A6 | 504990 | 687 | -92.2 | 504990 | 139 | -96.5 | 504990 | 464 | -96.2 | 504990 | 835 |
| MR_1774414140_90EA7EED | 504990 | 687 | -89.3 | 504990 | 139 | -98.4 | 504990 | 464 | -96.8 | 504990 | 835 |
| MR_1774414140_3012661D | 504990 | 687 | -89.2 | 504990 | 139 | -97.7 | 504990 | 464 | -98.5 | 504990 | 835 |
| MR_1774414140_193308C6 | 504990 | 687 | -89.6 | 504990 | 139 | -98.8 | 504990 | 464 | -98.5 | 504990 | 835 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 539: `9bf26c13-e95...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `9bf26c13-e95b-49d4-a6cd-99a94c2f7974` |
| Tag | **single-answer** |
| 정답 | **C4** |
| C4 의미 | Add neighbor relationship between 3219785_1 and 3230430_4 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[539] topology](images/train_0539.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3230430_4
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3219785_1
- `C3`: Add neighbor relationship between 3240069_2 and 3230430_4
- `C4`: Add neighbor relationship between 3219785_1 and 3230430_4 **← 정답**
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3230430_4
- `C6`: Decrease A3 Offset threshold for 3230430_4
- `C7`: Press down the tilt angle of 3219785_1 by 10 degrees
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3219785_1
- `C9`: Increase A3 Offset threshold for 3219785_1
- `C10`: Decrease transmission power for 3219785_1
- `C11`: Lift the tilt angle of 3219785_1 by 10 degrees
- `C12`: Check test server and transmission issues
- `C13`: Press down the tilt angle  of 3230430_4 by 3 degrees
- `C14`: Adjust the azimuth of 3230430_4 by 47 degrees
- `C15`: Decrease transmission power for 3230430_4
- `C16`: Insufficient data; more data is needed for judgment.
- `C17`: Lift the tilt angle  of 3230430_4 by 3 degrees
- `C18`: Increase transmission power for 3219785_1
- `C19`: Decrease A3 Offset threshold for 3219785_1
- `C20`: Increase transmission power for 3230430_4
- `C21`: Adjust the azimuth of 3219785_1 by 50 degrees
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3230430_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.918 | MS1 | 121.4656588352 | 31.1446191693 | 472 | 504990 | -81.47 | 16.44 | 599.03 | 0.19 | 2.09 | 1583 |
| 2024-09-20 22:21:32.788 | MS1 | 121.4656697799 | 31.1446244001 | 472 | 504990 | -81.68 | 16.15 | 319.67 | 0.17 | 2.31 | 1589 |
| 2024-09-20 22:21:33.583 | MS1 | 121.4656676713 | 31.1446297337 | 472 | 504990 | -79.11 | 12.94 | 448.71 | 0.07 | 2.95 | 1593 |
| 2024-09-20 22:21:34.569 | MS1 | 121.4656637655 | 31.1446375553 | 472 | 504990 | -88.56 | -0.36 | 53.76 | 0.14 | 1.09 | 1560 |
| 2024-09-20 22:21:35.753 | MS1 | 121.4656669812 | 31.1446197235 | 472 | 504990 | -90.95 | -0.77 | 29.99 | 0.12 | 1.46 | 1586 |
| 2024-09-20 22:21:36.246 | MS1 | 121.4656769720 | 31.1446299288 | 472 | 504990 | -89.86 | -1.03 | 39.24 | 0.03 | 1.14 | 1587 |
| 2024-09-20 22:21:37.677 | MS1 | 121.4656605884 | 31.1446320943 | 472 | 504990 | -85.19 | -3.62 | 50.86 | 0.20 | 1.24 | 1576 |
| 2024-09-20 22:21:38.515 | MS1 | 121.4656635926 | 31.1446236610 | 472 | 504990 | -82.99 | 16.84 | 332.11 | 0.15 | 1.10 | 1568 |
| 2024-09-20 22:21:39.962 | MS1 | 121.4656653931 | 31.1446345422 | 472 | 504990 | -77.83 | 16.31 | 306.48 | 0.19 | 1.34 | 1560 |
| 2024-09-20 22:21:40.463 | MS1 | 121.4656652450 | 31.1446337536 | 472 | 504990 | -79.42 | 14.88 | 484.22 | 0.15 | 2.99 | 1566 |
| 2024-09-20 22:21:41.290 | MS1 | 121.4656749237 | 31.1446240096 | 472 | 504990 | -79.59 | 13.72 | 485.40 | 0.01 | 2.75 | 1597 |
| 2024-09-20 22:21:42.208 | MS1 | 121.4656723316 | 31.1446371203 | 472 | 504990 | -75.21 | 12.14 | 325.89 | 0.13 | 2.19 | 1591 |

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
| 3219785 | 1 | 121.4723441952 | 31.1455821961 | 111 | 14 | 9 | 35.1 | TDD | 472 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3230430 | 4 | 121.4759307531 | 31.1497026489 | 193 | 2 | 2 | 28.0 | TDD | 471 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3240069 | 2 | 121.4657832781 | 31.1451960806 | 28 | 15 | 0 | 26.1 | TDD | 665 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3251489 | 3 | 121.4661769905 | 31.1549267908 | 254 | 3 | 1 | 45.0 | TDD | 449 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:31.082 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.103 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.247 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.247 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.973 | NREventA3 | measId:2;ServCellPCI:267;Se... |
| 2024-09-20 22:21:35.973 | NREventA3 | measId:2;ServCellPCI:267;Se... |
| 2024-09-20 22:21:36.973 | NREventA3 | measId:2;ServCellPCI:267;Se... |
| 2024-09-20 22:21:39.473 | NRRRCReestablishAttempt | PCI:267 |
| 2024-09-20 22:21:39.484 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.496 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:39.622 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.622 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3219785 | 1 | 19.8258 | 19.7074 | -117.1077 | 6.1927 | 122.1231 | 0.0144 | 0.1040 |
| 2024_09_20 22:00 | 3240069 | 2 | 14.1086 | 11.1807 | -115.3075 | 5.4977 | 165.6542 | 0.0107 | 0.0086 |
| 2024_09_20 22:00 | 3251489 | 3 | 7.1277 | 10.9079 | -115.0590 | 15.1121 | 105.7267 | 0.0135 | 0.0084 |
| 2024_09_20 22:00 | 3230430 | 4 | 14.2257 | 5.5456 | -117.0393 | 10.9971 | 112.6552 | 0.0110 | 0.0157 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413843_141281EF | 504990 | 471 | -80.8 | 504990 | 472 | -88.5 | 504990 | 665 | -92.0 | 504990 | 449 |
| MR_1774413843_747FDA33 | 504990 | 472 | -89.2 | 504990 | 471 | -81.3 | 504990 | 665 | -92.1 | 504990 | 449 |
| MR_1774413843_236C8317 | 504990 | 472 | -89.3 | 504990 | 471 | -80.8 | 504990 | 665 | -93.9 | 504990 | 449 |
| MR_1774413843_0ED7103C | 504990 | 472 | -88.7 | 504990 | 471 | -83.4 | 504990 | 665 | -91.2 | 504990 | 449 |
| MR_1774413843_CC94B1EE | 504990 | 472 | -87.7 | 504990 | 471 | -81.9 | 504990 | 665 | -94.0 | 504990 | 449 |

> *... 2개 열 생략 (전체 14열)*

---
