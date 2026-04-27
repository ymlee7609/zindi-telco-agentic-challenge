# Track A 문제 분석 — train[1830]~train[1839]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[1830] ~ train[1839] (10개)

## 목차

1. [문제 1830: `a863e3fe-07e...`](#1830) — single-answer, 정답: C2
2. [문제 1831: `4d1a9221-7d8...`](#1831) — single-answer, 정답: C17
3. [문제 1832: `cdf076f6-09a...`](#1832) — single-answer, 정답: C5
4. [문제 1833: `b61a1dc5-2ce...`](#1833) — single-answer, 정답: C2
5. [문제 1834: `021d97eb-f01...`](#1834) — single-answer, 정답: C6
6. [문제 1835: `9ce9a526-0ab...`](#1835) — single-answer, 정답: C21
7. [문제 1836: `fb36c798-e72...`](#1836) — single-answer, 정답: C15
8. [문제 1837: `84ace18d-f07...`](#1837) — single-answer, 정답: C3
9. [문제 1838: `c0114e44-c0b...`](#1838) — multiple-answer, 정답: C2|C6|C8|C14
10. [문제 1839: `6433ee79-efe...`](#1839) — single-answer, 정답: C14

---

### 문제 1830: `a863e3fe-07e...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `a863e3fe-07e0-4245-a54f-305a29d1b4f4` |
| Tag | **single-answer** |
| 정답 | **C2** |
| C2 의미 | Lift the tilt angle  of 3263229_1 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1830] topology](images/train_1830.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3267684_4
- `C2`: Lift the tilt angle  of 3263229_1 by 10 degrees **← 정답**
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3226025_2
- `C4`: Adjust the azimuth of 3226025_2 by 7 degrees
- `C5`: Decrease A3 Offset threshold for 3226025_2
- `C6`: Check test server and transmission issues
- `C7`: Press down the tilt angle of 3226025_2 by 2 degrees
- `C8`: Decrease transmission power for 3267684_4
- `C9`: Add neighbor relationship between 3226025_2 and 3267684_4
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3267684_4
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3226025_2
- `C12`: Add neighbor relationship between 3263229_1 and 3267684_4
- `C13`: Increase transmission power for 3267684_4
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3267684_4
- `C15`: Increase transmission power for 3226025_2
- `C16`: Decrease transmission power for 3226025_2
- `C17`: Press down the tilt angle  of 3263229_1 by 10 degrees
- `C18`: Increase A3 Offset threshold for 3226025_2
- `C19`: Lift the tilt angle of 3226025_2 by 2 degrees
- `C20`: Insufficient data; more data is needed for judgment.
- `C21`: Increase A3 Offset threshold for 3267684_4
- `C22`: Adjust the azimuth of 3263229_1 by 50 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.423 | MS1 | 121.4656613384 | 31.1446332283 | 882 | 504990 | -88.48 | 12.73 | 483.65 | 0.11 | 2.76 | 1594 |
| 2024-09-20 22:21:32.551 | MS1 | 121.4656657885 | 31.1446298172 | 882 | 504990 | -90.08 | 16.17 | 501.79 | 0.03 | 2.62 | 1581 |
| 2024-09-20 22:21:33.824 | MS1 | 121.4656695413 | 31.1446335243 | 882 | 504990 | -86.46 | 14.80 | 321.12 | 0.01 | 2.16 | 1569 |
| 2024-09-20 22:21:34.305 | MS1 | 121.4656610671 | 31.1446215072 | 882 | 504990 | -89.31 | 14.00 | 100.82 | 0.05 | 2.35 | 1580 |
| 2024-09-20 22:21:35.459 | MS1 | 121.4656774566 | 31.1446254191 | 882 | 504990 | -85.77 | 17.65 | 62.92 | 0.12 | 2.73 | 1564 |
| 2024-09-20 22:21:36.264 | MS1 | 121.4656651070 | 31.1446342604 | 882 | 504990 | -88.54 | 13.71 | 55.13 | 0.06 | 2.23 | 1595 |
| 2024-09-20 22:21:37.758 | MS1 | 121.4656722162 | 31.1446260118 | 882 | 504990 | -89.39 | 9.65 | 80.23 | 0.13 | 2.11 | 1564 |
| 2024-09-20 22:21:38.263 | MS1 | 121.4656624154 | 31.1446247585 | 882 | 504990 | -89.90 | 8.03 | 72.67 | 0.08 | 2.09 | 1589 |
| 2024-09-20 22:21:39.909 | MS1 | 121.4656763423 | 31.1446304636 | 882 | 504990 | -90.34 | 10.14 | 77.05 | 0.17 | 2.39 | 1560 |
| 2024-09-20 22:21:40.135 | MS1 | 121.4656660799 | 31.1446271532 | 882 | 504990 | -93.98 | 10.75 | 395.35 | 0.06 | 2.09 | 1596 |
| 2024-09-20 22:21:41.197 | MS1 | 121.4656610179 | 31.1446196106 | 882 | 504990 | -91.63 | 7.03 | 331.75 | 0.16 | 2.45 | 1564 |
| 2024-09-20 22:21:42.168 | MS1 | 121.4656597058 | 31.1446189793 | 882 | 504990 | -89.07 | 12.80 | 563.85 | 0.14 | 2.52 | 1592 |

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
| 3222752 | 3 | 121.4739145302 | 31.1502039788 | 103 | 11 | 11 | 40.2 | TDD | 42 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3226025 | 2 | 121.4743098529 | 31.1523614542 | 231 | 1 | 5 | 16.8 | TDD | 882 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3263229 | 1 | 121.4643071898 | 31.1557133319 | 50 | 3 | 1 | 20.7 | TDD | 833 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3267684 | 4 | 121.4648232805 | 31.1466262871 | 15 | 5 | 5 | 21.4 | TDD | 761 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:31.496 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.626 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.626 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.341 | NREventA3 | measId:2;ServCellPCI:709;Se... |
| 2024-09-20 22:21:38.581 | NRHandoverAttempt | SourcePCI:709;SourceNR-ARFC... |
| 2024-09-20 22:21:38.626 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.640 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.767 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.767 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3263229 | 1 | 14.6291 | 19.1834 | -115.7980 | 7.4881 | 96.5873 | 0.0127 | 0.0104 |
| 2024_09_20 22:00 | 3226025 | 2 | 90.7203 | 85.4798 | -117.6820 | 16.7909 | 155.7773 | 0.0080 | 0.0124 |
| 2024_09_20 22:00 | 3222752 | 3 | 9.5198 | 12.2085 | -115.2041 | 18.2523 | 166.4800 | 0.0150 | 0.0164 |
| 2024_09_20 22:00 | 3267684 | 4 | 16.8867 | 17.1834 | -117.1074 | 16.5210 | 108.9852 | 0.0003 | 0.0137 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413392_71FE17BA | 504990 | 882 | -83.9 | 504990 | 761 | -85.5 | 504990 | 833 | -94.7 | 504990 | 42 |
| MR_1774413392_6EDF8D83 | 504990 | 882 | -84.6 | 504990 | 761 | -86.6 | 504990 | 833 | -96.8 | 504990 | 42 |
| MR_1774413392_84B7C2AA | 504990 | 882 | -86.4 | 504990 | 761 | -85.8 | 504990 | 833 | -96.9 | 504990 | 42 |
| MR_1774413392_CBD103FA | 504990 | 882 | -86.0 | 504990 | 761 | -86.0 | 504990 | 833 | -96.4 | 504990 | 42 |
| MR_1774413392_414F3E1A | 504990 | 882 | -85.0 | 504990 | 761 | -86.5 | 504990 | 833 | -95.6 | 504990 | 42 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1831: `4d1a9221-7d8...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `4d1a9221-7d84-44c5-b916-58ef77b251d3` |
| Tag | **single-answer** |
| 정답 | **C17** |
| C17 의미 | Add neighbor relationship between 3260785_3 and 3276357_1 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1831] topology](images/train_1831.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3260785_3 by 10 degrees
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3276357_1
- `C3`: Adjust the azimuth of 3276357_1 by 17 degrees
- `C4`: Decrease A3 Offset threshold for 3260785_3
- `C5`: Adjust the azimuth of 3260785_3 by 50 degrees
- `C6`: Lift the tilt angle of 3260785_3 by 10 degrees
- `C7`: Increase A3 Offset threshold for 3276357_1
- `C8`: Increase transmission power for 3276357_1
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3260785_3
- `C10`: Decrease A3 Offset threshold for 3276357_1
- `C11`: Insufficient data; more data is needed for judgment.
- `C12`: Increase A3 Offset threshold for 3260785_3
- `C13`: Increase transmission power for 3260785_3
- `C14`: Decrease transmission power for 3276357_1
- `C15`: Check test server and transmission issues
- `C16`: Lift the tilt angle  of 3276357_1 by 2 degrees
- `C17`: Add neighbor relationship between 3260785_3 and 3276357_1 **← 정답**
- `C18`: Press down the tilt angle  of 3276357_1 by 2 degrees
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3260785_3
- `C20`: Decrease transmission power for 3260785_3
- `C21`: Add neighbor relationship between 3235736_2 and 3276357_1
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3276357_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.104 | MS1 | 121.4656650062 | 31.1446332900 | 445 | 504990 | -79.05 | 12.95 | 312.67 | 0.09 | 2.23 | 1590 |
| 2024-09-20 22:21:32.662 | MS1 | 121.4656715600 | 31.1446348927 | 445 | 504990 | -80.98 | 16.22 | 590.19 | 0.09 | 2.90 | 1596 |
| 2024-09-20 22:21:33.469 | MS1 | 121.4656610202 | 31.1446298259 | 445 | 504990 | -80.53 | 12.61 | 549.71 | 0.03 | 2.34 | 1581 |
| 2024-09-20 22:21:34.481 | MS1 | 121.4656612586 | 31.1446347346 | 445 | 504990 | -90.53 | -2.88 | 50.87 | 0.08 | 1.46 | 1578 |
| 2024-09-20 22:21:35.513 | MS1 | 121.4656708483 | 31.1446201989 | 445 | 504990 | -91.91 | -3.44 | 47.62 | 0.01 | 1.46 | 1600 |
| 2024-09-20 22:21:36.915 | MS1 | 121.4656594796 | 31.1446238625 | 445 | 504990 | -89.39 | -2.01 | 64.39 | 0.09 | 1.10 | 1567 |
| 2024-09-20 22:21:37.731 | MS1 | 121.4656658705 | 31.1446379272 | 445 | 504990 | -85.13 | -0.13 | 64.81 | 0.16 | 1.38 | 1576 |
| 2024-09-20 22:21:38.179 | MS1 | 121.4656676128 | 31.1446324835 | 445 | 504990 | -79.52 | 15.02 | 572.94 | 0.05 | 1.22 | 1572 |
| 2024-09-20 22:21:39.260 | MS1 | 121.4656777829 | 31.1446233191 | 445 | 504990 | -77.04 | 14.26 | 529.81 | 0.03 | 1.21 | 1598 |
| 2024-09-20 22:21:40.661 | MS1 | 121.4656700366 | 31.1446354604 | 445 | 504990 | -84.12 | 16.56 | 440.83 | 0.01 | 2.27 | 1572 |
| 2024-09-20 22:21:41.354 | MS1 | 121.4656613444 | 31.1446277145 | 445 | 504990 | -82.63 | 14.98 | 401.00 | 0.20 | 2.96 | 1571 |
| 2024-09-20 22:21:42.552 | MS1 | 121.4656736183 | 31.1446199850 | 445 | 504990 | -78.75 | 13.79 | 450.45 | 0.07 | 2.95 | 1560 |

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
| 3235736 | 2 | 121.4720754817 | 31.1515738280 | 258 | 7 | 0 | 39.8 | TDD | 876 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3260785 | 3 | 121.4676481490 | 31.1491746526 | 135 | 9 | 7 | 34.2 | TDD | 445 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3276357 | 1 | 121.4741549535 | 31.1534664218 | 236 | 0 | 2 | 40.0 | TDD | 552 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3277625 | 4 | 121.4743370622 | 31.1522332175 | 307 | 10 | 9 | 25.8 | TDD | 479 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |

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
| 2024-09-20 22:21:31.055 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.191 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.191 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.875 | NREventA3 | measId:2;ServCellPCI:231;Se... |
| 2024-09-20 22:21:35.875 | NREventA3 | measId:2;ServCellPCI:231;Se... |
| 2024-09-20 22:21:36.875 | NREventA3 | measId:2;ServCellPCI:231;Se... |
| 2024-09-20 22:21:39.375 | NRRRCReestablishAttempt | PCI:231 |
| 2024-09-20 22:21:39.395 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.405 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:39.539 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.539 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3276357 | 1 | 8.2864 | 12.4392 | -114.4252 | 13.4058 | 149.9570 | 0.0102 | 0.0127 |
| 2024_09_20 22:00 | 3235736 | 2 | 9.4602 | 16.2756 | -117.9548 | 15.1270 | 145.7048 | 0.0098 | 0.0100 |
| 2024_09_20 22:00 | 3260785 | 3 | 16.0504 | 16.8577 | -116.8473 | 5.6068 | 147.6010 | 0.0037 | 0.1161 |
| 2024_09_20 22:00 | 3277625 | 4 | 8.3837 | 5.2924 | -114.7449 | 15.9474 | 104.5309 | 0.0105 | 0.0066 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417155_FDD55C06 | 504990 | 445 | -89.2 | 504990 | 552 | -83.6 | 504990 | 876 | -90.2 | 504990 | 479 |
| MR_1774417155_11D16CC5 | 504990 | 552 | -85.2 | 504990 | 445 | -91.9 | 504990 | 876 | -89.9 | 504990 | 479 |
| MR_1774417155_50D6075D | 504990 | 445 | -88.6 | 504990 | 552 | -84.4 | 504990 | 876 | -90.2 | 504990 | 479 |
| MR_1774417155_D13DC9DC | 504990 | 445 | -90.8 | 504990 | 552 | -85.6 | 504990 | 876 | -87.8 | 504990 | 479 |
| MR_1774417155_E4783926 | 504990 | 552 | -85.4 | 504990 | 445 | -89.8 | 504990 | 876 | -88.1 | 504990 | 479 |
| MR_1774417155_7BD05D0A | 504990 | 552 | -85.1 | 504990 | 445 | -90.8 | 504990 | 876 | -89.7 | 504990 | 479 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1832: `cdf076f6-09a...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `cdf076f6-09a6-4eeb-ae94-7983ccb1f598` |
| Tag | **single-answer** |
| 정답 | **C5** |
| C5 의미 | Add neighbor relationship between 3230661_4 and 3213118_1 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1832] topology](images/train_1832.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3213118_1
- `C2`: Increase A3 Offset threshold for 3213118_1
- `C3`: Adjust the azimuth of 3230661_4 by 50 degrees
- `C4`: Decrease A3 Offset threshold for 3230661_4
- `C5`: Add neighbor relationship between 3230661_4 and 3213118_1 **← 정답**
- `C6`: Decrease transmission power for 3213118_1
- `C7`: Increase transmission power for 3213118_1
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3230661_4
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3213118_1
- `C10`: Decrease A3 Offset threshold for 3213118_1
- `C11`: Add neighbor relationship between 3268497_2 and 3213118_1
- `C12`: Increase A3 Offset threshold for 3230661_4
- `C13`: Press down the tilt angle of 3230661_4 by 10 degrees
- `C14`: Lift the tilt angle of 3230661_4 by 10 degrees
- `C15`: Increase transmission power for 3230661_4
- `C16`: Lift the tilt angle  of 3213118_1 by 3 degrees
- `C17`: Insufficient data; more data is needed for judgment.
- `C18`: Press down the tilt angle  of 3213118_1 by 3 degrees
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3230661_4
- `C20`: Decrease transmission power for 3230661_4
- `C21`: Check test server and transmission issues
- `C22`: Adjust the azimuth of 3213118_1 by 26 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.812 | MS1 | 121.4656713485 | 31.1446344509 | 463 | 504990 | -77.54 | 16.04 | 487.89 | 0.18 | 2.02 | 1560 |
| 2024-09-20 22:21:32.586 | MS1 | 121.4656603812 | 31.1446224264 | 463 | 504990 | -75.29 | 15.74 | 376.39 | 0.03 | 2.40 | 1560 |
| 2024-09-20 22:21:33.621 | MS1 | 121.4656623525 | 31.1446246080 | 463 | 504990 | -78.08 | 15.90 | 375.57 | 0.02 | 2.06 | 1576 |
| 2024-09-20 22:21:34.795 | MS1 | 121.4656624469 | 31.1446319471 | 463 | 504990 | -87.23 | -0.97 | 55.96 | 0.00 | 1.15 | 1595 |
| 2024-09-20 22:21:35.478 | MS1 | 121.4656726422 | 31.1446242685 | 463 | 504990 | -92.86 | -2.16 | 75.14 | 0.01 | 1.18 | 1565 |
| 2024-09-20 22:21:36.645 | MS1 | 121.4656591350 | 31.1446379955 | 463 | 504990 | -92.19 | -2.25 | 42.88 | 0.16 | 1.50 | 1567 |
| 2024-09-20 22:21:37.132 | MS1 | 121.4656630973 | 31.1446251163 | 463 | 504990 | -91.81 | -0.02 | 39.26 | 0.06 | 1.17 | 1563 |
| 2024-09-20 22:21:38.473 | MS1 | 121.4656642583 | 31.1446371348 | 463 | 504990 | -83.00 | 17.12 | 585.71 | 0.05 | 1.17 | 1593 |
| 2024-09-20 22:21:39.939 | MS1 | 121.4656661292 | 31.1446317844 | 463 | 504990 | -76.79 | 13.78 | 551.65 | 0.13 | 1.17 | 1568 |
| 2024-09-20 22:21:40.339 | MS1 | 121.4656626343 | 31.1446223900 | 463 | 504990 | -75.01 | 17.66 | 384.34 | 0.15 | 2.94 | 1568 |
| 2024-09-20 22:21:41.646 | MS1 | 121.4656596239 | 31.1446357050 | 463 | 504990 | -81.81 | 13.74 | 477.60 | 0.09 | 2.44 | 1587 |
| 2024-09-20 22:21:42.336 | MS1 | 121.4656645170 | 31.1446263830 | 463 | 504990 | -77.57 | 17.14 | 414.32 | 0.16 | 2.23 | 1577 |

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
| 3213118 | 1 | 121.4700588456 | 31.1539744065 | 228 | 2 | 7 | 23.2 | TDD | 464 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3230661 | 4 | 121.4683666246 | 31.1491587138 | 286 | 7 | 10 | 34.0 | TDD | 463 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3257921 | 3 | 121.4756812038 | 31.1451435767 | 212 | 2 | 5 | 15.3 | TDD | 452 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3268497 | 2 | 121.4688800258 | 31.1508413014 | 299 | 1 | 7 | 39.7 | TDD | 330 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

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
| 2024-09-20 22:21:31.349 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.365 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.499 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.499 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.152 | NREventA3 | measId:2;ServCellPCI:405;Se... |
| 2024-09-20 22:21:36.152 | NREventA3 | measId:2;ServCellPCI:405;Se... |
| 2024-09-20 22:21:37.152 | NREventA3 | measId:2;ServCellPCI:405;Se... |
| 2024-09-20 22:21:39.652 | NRRRCReestablishAttempt | PCI:405 |
| 2024-09-20 22:21:39.664 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.677 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:39.811 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.811 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3213118 | 1 | 15.9500 | 10.0139 | -117.1760 | 7.3024 | 97.2154 | 0.0044 | 0.0010 |
| 2024_09_20 22:00 | 3268497 | 2 | 11.1094 | 17.9209 | -114.6230 | 13.3765 | 198.5585 | 0.0122 | 0.0020 |
| 2024_09_20 22:00 | 3257921 | 3 | 14.7063 | 14.8876 | -114.1888 | 11.8094 | 138.6920 | 0.0040 | 0.0071 |
| 2024_09_20 22:00 | 3230661 | 4 | 10.8809 | 10.7985 | -116.4493 | 19.2296 | 90.9325 | 0.0096 | 0.1000 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414289_F20AAA92 | 504990 | 464 | -82.2 | 504990 | 463 | -88.0 | 504990 | 330 | -92.0 | 504990 | 452 |
| MR_1774414289_A272C1CE | 504990 | 463 | -88.4 | 504990 | 464 | -80.6 | 504990 | 330 | -91.4 | 504990 | 452 |
| MR_1774414289_CBD6C2E4 | 504990 | 464 | -84.0 | 504990 | 463 | -85.3 | 504990 | 330 | -94.0 | 504990 | 452 |
| MR_1774414289_A0581E4A | 504990 | 464 | -84.1 | 504990 | 463 | -88.0 | 504990 | 330 | -92.2 | 504990 | 452 |
| MR_1774414289_DC85DD39 | 504990 | 464 | -81.3 | 504990 | 463 | -87.0 | 504990 | 330 | -91.0 | 504990 | 452 |
| MR_1774414289_F46EEE80 | 504990 | 464 | -81.9 | 504990 | 463 | -88.0 | 504990 | 330 | -92.4 | 504990 | 452 |
| MR_1774414289_4E5287E4 | 504990 | 463 | -85.3 | 504990 | 464 | -81.1 | 504990 | 330 | -92.5 | 504990 | 452 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1833: `b61a1dc5-2ce...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `b61a1dc5-2cec-4fb4-ada6-0b90507ac126` |
| Tag | **single-answer** |
| 정답 | **C2** |
| C2 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3219707_4 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1833] topology](images/train_1833.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3220112_2
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3219707_4 **← 정답**
- `C3`: Add neighbor relationship between 3275801_7 and 3220112_2
- `C4`: Adjust the azimuth of 3219707_4 by 49 degrees
- `C5`: Increase transmission power for 3219707_4
- `C6`: Insufficient data; more data is needed for judgment.
- `C7`: Increase transmission power for 3220112_2
- `C8`: Lift the tilt angle of 3219707_4 by 4 degrees
- `C9`: Press down the tilt angle  of 3220112_2 by 2 degrees
- `C10`: Adjust the azimuth of 3220112_2 by 11 degrees
- `C11`: Add neighbor relationship between 3219707_4 and 3220112_2
- `C12`: Increase A3 Offset threshold for 3220112_2
- `C13`: Increase A3 Offset threshold for 3219707_4
- `C14`: Lift the tilt angle  of 3220112_2 by 2 degrees
- `C15`: Decrease transmission power for 3220112_2
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3220112_2
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3219707_4
- `C18`: Press down the tilt angle of 3219707_4 by 4 degrees
- `C19`: Check test server and transmission issues
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3220112_2
- `C21`: Decrease transmission power for 3219707_4
- `C22`: Decrease A3 Offset threshold for 3219707_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.486 | MS1 | 121.4656665368 | 31.1446228852 | 501 | 504990 | -93.51 | 10.42 | 352.11 | 0.10 | 2.80 | 1598 |
| 2024-09-20 22:21:32.625 | MS1 | 121.4656640126 | 31.1446257758 | 1007 | 504990 | -95.84 | 14.62 | 474.95 | 0.14 | 2.81 | 1570 |
| 2024-09-20 22:21:33.720 | MS1 | 121.4656651255 | 31.1446214084 | 640 | 504990 | -93.84 | 11.81 | 451.50 | 0.01 | 2.36 | 1563 |
| 2024-09-20 22:21:34.625 | MS1 | 121.4656650694 | 31.1446192128 | 376 | 152650 | -89.35 | 4.89 | 69.62 | 0.05 | 1.63 | 947 |
| 2024-09-20 22:21:35.604 | MS1 | 121.4656624126 | 31.1446284377 | 877 | 152650 | -91.93 | 3.63 | 102.00 | 0.15 | 1.50 | 993 |
| 2024-09-20 22:21:36.667 | MS1 | 121.4656592047 | 31.1446224078 | 416 | 152650 | -91.78 | 3.94 | 99.19 | 0.04 | 1.72 | 939 |
| 2024-09-20 22:21:37.232 | MS1 | 121.4656641751 | 31.1446249103 | 890 | 152650 | -93.15 | 2.51 | 73.73 | 0.00 | 1.71 | 917 |
| 2024-09-20 22:21:38.280 | MS1 | 121.4656686159 | 31.1446184722 | 376 | 152650 | -93.70 | 6.56 | 59.04 | 0.19 | 1.63 | 924 |
| 2024-09-20 22:21:39.329 | MS1 | 121.4656590441 | 31.1446356432 | 877 | 152650 | -88.48 | 6.21 | 54.04 | 0.01 | 1.70 | 950 |
| 2024-09-20 22:21:40.139 | MS1 | 121.4656730127 | 31.1446339831 | 416 | 152650 | -95.26 | 5.88 | 86.66 | 0.14 | 2.13 | 1566 |
| 2024-09-20 22:21:41.941 | MS1 | 121.4656714985 | 31.1446312846 | 890 | 152650 | -88.05 | 7.83 | 58.21 | 0.05 | 2.39 | 1563 |
| 2024-09-20 22:21:42.887 | MS1 | 121.4656685449 | 31.1446362901 | 376 | 152650 | -92.05 | 6.63 | 81.41 | 0.02 | 2.63 | 1577 |

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
| 3216641 | 12 | 121.4711084255 | 31.1450343034 | 108 | 0 | 4 | 8.3 | FDD | 890 | n1 | 152650 | 30M | 4T4R | 30 | 152650 |
| 3217762 | 3 | 121.4681844985 | 31.1548515654 | 177 | 11 | 2 | 7.9 | TDD | 1007 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3219707 | 4 | 121.4693614058 | 31.1494483541 | 164 | 2 | 4 | 21.3 | TDD | 501 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3220112 | 2 | 121.4681120639 | 31.1492232183 | 194 | 1 | 7 | 5.1 | TDD | 195 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3220534 | 8 | 121.4657285459 | 31.1466057510 | 148 | 4 | 4 | 28.3 | FDD | 877 | n1 | 152650 | 30M | 4T4R | 12 | 152650 |
| 3222811 | 1 | 121.4754908634 | 31.1519289036 | 142 | 14 | 4 | 6.9 | TDD | 640 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3226976 | 6 | 121.4670560586 | 31.1477493097 | 109 | 14 | 12 | 17.9 | TDD | 279 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3228410 | 10 | 121.4722698481 | 31.1501019697 | 218 | 3 | 7 | 4.3 | FDD | 376 | n1 | 152650 | 30M | 4T4R | 29 | 152650 |
| 3233427 | 13 | 121.4713398001 | 31.1444478015 | 280 | 3 | 11 | 9.5 | FDD | 351 | n1 | 152650 | 30M | 4T4R | 25 | 152650 |
| 3251098 | 5 | 121.4759340870 | 31.1542902444 | 207 | 11 | 3 | 7.1 | TDD | 245 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3256703 | 9 | 121.4654280117 | 31.1460763983 | 214 | 4 | 2 | 29.2 | FDD | 19 | n1 | 152650 | 30M | 4T4R | 14 | 152650 |
| 3275801 | 7 | 121.4702956658 | 31.1493921031 | 210 | 9 | 6 | 5.2 | FDD | 416 | n1 | 152650 | 30M | 4T4R | 20 | 152650 |
| 3279709 | 11 | 121.4741696010 | 31.1443082946 | 255 | 5 | 11 | 11.4 | FDD | 505 | n1 | 152650 | 30M | 4T4R | 23 | 152650 |

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
| 2024-09-20 22:21:31.224 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.245 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.347 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.347 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.058 | NREventA2 | measId:1;ServCellPCI:933;Se... |
| 2024-09-20 22:21:35.207 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.428 | NREventA5 | measId:3;ServCellPCI:933;Se... |
| 2024-09-20 22:21:35.462 | NRHandoverAttempt | SourcePCI:933;SourceNR-ARFC... |
| 2024-09-20 22:21:35.507 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.519 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:35.665 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.665 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3222811 | 1 | 17.0714 | 13.1203 | -114.8980 | 9.9678 | 125.1823 | 0.0031 | 0.0122 |
| 2024_09_20 22:00 | 3220112 | 2 | 12.2081 | 5.8411 | -114.9553 | 19.3061 | 190.9780 | 0.0141 | 0.0146 |
| 2024_09_20 22:00 | 3217762 | 3 | 6.3862 | 13.2471 | -115.0058 | 18.0490 | 96.7822 | 0.0002 | 0.0189 |
| 2024_09_20 22:00 | 3219707 | 4 | 13.4783 | 12.7357 | -114.8270 | 15.2892 | 88.8159 | 0.0072 | 0.0038 |
| 2024_09_20 22:00 | 3251098 | 5 | 6.0269 | 10.3593 | -115.3910 | 11.8728 | 163.4095 | 0.0051 | 0.0126 |
| 2024_09_20 22:00 | 3226976 | 6 | 6.5466 | 13.2672 | -115.0435 | 8.2880 | 91.2134 | 0.0191 | 0.0031 |
| 2024_09_20 22:00 | 3275801 | 7 | 14.1857 | 6.7813 | -116.2067 | 3.7869 | 55.0438 | 0.0095 | 0.0113 |
| 2024_09_20 22:00 | 3220534 | 8 | 11.7769 | 18.7759 | -115.9659 | 3.5988 | 49.2015 | 0.0120 | 0.0087 |
| 2024_09_20 22:00 | 3256703 | 9 | 8.5701 | 16.0278 | -114.9203 | 4.7279 | 51.3604 | 0.0085 | 0.0051 |
| 2024_09_20 22:00 | 3228410 | 10 | 16.8634 | 8.1347 | -117.7659 | 4.3615 | 32.6540 | 0.0164 | 0.0079 |
| 2024_09_20 22:00 | 3279709 | 11 | 7.1117 | 15.8500 | -116.0490 | 4.1087 | 33.6197 | 0.0005 | 0.0008 |
| 2024_09_20 22:00 | 3216641 | 12 | 5.8260 | 17.2369 | -114.1351 | 4.0953 | 23.8974 | 0.0187 | 0.0004 |
| 2024_09_20 22:00 | 3233427 | 13 | 9.5467 | 19.5928 | -114.2557 | 4.4738 | 36.8974 | 0.0033 | 0.0115 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416502_AD8A4C94 | 504990 | 640 | -92.0 | 504990 | 195 | -92.1 | 504990 | 279 | -97.5 | 504990 | 245 |
| MR_1774416502_EBA7859E | 152650 | 376 | -88.2 | 152650 | 19 | -96.5 | 152650 | 351 | -95.9 | 152650 | 505 |
| MR_1774416502_0EC55148 | 152650 | 376 | -88.1 | 152650 | 19 | -98.7 | 152650 | 351 | -97.3 | 152650 | 505 |
| MR_1774416502_3AF6C394 | 504990 | 640 | -93.7 | 504990 | 195 | -92.7 | 504990 | 279 | -97.3 | 504990 | 245 |
| MR_1774416502_53B21DEC | 152650 | 376 | -89.8 | 152650 | 19 | -96.3 | 152650 | 351 | -95.9 | 152650 | 505 |
| MR_1774416502_D8E8002B | 152650 | 376 | -90.1 | 152650 | 19 | -96.9 | 152650 | 351 | -98.6 | 152650 | 505 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1834: `021d97eb-f01...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `021d97eb-f01d-4c37-b46a-944e80bbbbb4` |
| Tag | **single-answer** |
| 정답 | **C6** |
| C6 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1834] topology](images/train_1834.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3278022_4
- `C2`: Press down the tilt angle  of 3265904_3 by 10 degrees
- `C3`: Press down the tilt angle of 3278022_4 by 2 degrees
- `C4`: Decrease transmission power for 3278022_4
- `C5`: Add neighbor relationship between 3279296_1 and 3265904_3
- `C6`: Insufficient data; more data is needed for judgment. **← 정답**
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3278022_4
- `C8`: Lift the tilt angle of 3278022_4 by 2 degrees
- `C9`: Increase A3 Offset threshold for 3278022_4
- `C10`: Increase transmission power for 3265904_3
- `C11`: Decrease transmission power for 3265904_3
- `C12`: Decrease A3 Offset threshold for 3278022_4
- `C13`: Decrease A3 Offset threshold for 3265904_3
- `C14`: Adjust the azimuth of 3278022_4 by 37 degrees
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3278022_4
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3265904_3
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3265904_3
- `C18`: Check test server and transmission issues
- `C19`: Increase A3 Offset threshold for 3265904_3
- `C20`: Add neighbor relationship between 3278022_4 and 3265904_3
- `C21`: Adjust the azimuth of 3265904_3 by 36 degrees
- `C22`: Lift the tilt angle  of 3265904_3 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.454 | MS1 | 121.4656777582 | 31.1446371260 | 199 | 504990 | -90.46 | 14.90 | 345.95 | 0.16 | 2.32 | 1562 |
| 2024-09-20 22:21:32.539 | MS1 | 121.4656612830 | 31.1446322194 | 199 | 504990 | -87.16 | 16.71 | 412.21 | 0.18 | 2.74 | 1560 |
| 2024-09-20 22:21:33.251 | MS1 | 121.4656683364 | 31.1446297635 | 199 | 504990 | -91.97 | 14.66 | 592.97 | 0.03 | 2.23 | 1560 |
| 2024-09-20 22:21:34.718 | MS1 | 121.4656615210 | 31.1446211076 | 199 | 504990 | -86.59 | 14.56 | 82.95 | 0.05 | 2.93 | 1598 |
| 2024-09-20 22:21:35.157 | MS1 | 121.4656725236 | 31.1446312588 | 199 | 504990 | -88.20 | 16.02 | 105.12 | 0.06 | 2.03 | 1568 |
| 2024-09-20 22:21:36.337 | MS1 | 121.4656684715 | 31.1446359372 | 199 | 504990 | -89.54 | 14.63 | 75.54 | 0.18 | 2.48 | 1589 |
| 2024-09-20 22:21:37.225 | MS1 | 121.4656584097 | 31.1446340274 | 199 | 504990 | -91.72 | 11.26 | 49.43 | 0.16 | 2.68 | 1600 |
| 2024-09-20 22:21:38.629 | MS1 | 121.4656633016 | 31.1446233007 | 199 | 504990 | -92.41 | 11.18 | 71.98 | 0.07 | 2.26 | 1582 |
| 2024-09-20 22:21:39.766 | MS1 | 121.4656723548 | 31.1446287419 | 199 | 504990 | -93.98 | 10.72 | 66.87 | 0.08 | 2.66 | 1574 |
| 2024-09-20 22:21:40.737 | MS1 | 121.4656777770 | 31.1446313367 | 199 | 504990 | -92.46 | 7.15 | 488.08 | 0.05 | 2.98 | 1585 |
| 2024-09-20 22:21:41.991 | MS1 | 121.4656624547 | 31.1446253969 | 199 | 504990 | -92.78 | 8.87 | 486.96 | 0.18 | 2.07 | 1561 |
| 2024-09-20 22:21:42.691 | MS1 | 121.4656676837 | 31.1446351002 | 199 | 504990 | -93.65 | 10.67 | 497.66 | 0.10 | 2.42 | 1570 |

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
| 3251142 | 2 | 121.4706892628 | 31.1441373509 | 190 | 7 | 6 | 25.6 | TDD | 108 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3265904 | 3 | 121.4714602150 | 31.1517725441 | 179 | 8 | 1 | 43.5 | TDD | 302 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3278022 | 4 | 121.4751080235 | 31.1544245295 | 183 | 1 | 2 | 19.5 | TDD | 199 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3279296 | 1 | 121.4709978391 | 31.1477261763 | 265 | 2 | 3 | 17.0 | TDD | 819 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |

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
| 2024-09-20 22:21:31.106 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.229 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.229 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.903 | NREventA3 | measId:2;ServCellPCI:68;Ser... |
| 2024-09-20 22:21:38.143 | NRHandoverAttempt | SourcePCI:68;SourceNR-ARFCN... |
| 2024-09-20 22:21:38.183 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.198 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.312 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.312 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3279296 | 1 | 84.7346 | 83.4644 | -114.6832 | 6.5921 | 194.1563 | 0.0092 | 0.0149 |
| 2024_09_19 22:00 | 3251142 | 2 | 79.8561 | 89.0711 | -114.3110 | 19.1443 | 155.5091 | 0.0136 | 0.0075 |
| 2024_09_19 22:00 | 3265904 | 3 | 85.9952 | 89.3276 | -114.6763 | 14.5506 | 176.1472 | 0.0083 | 0.0125 |
| 2024_09_19 22:00 | 3278022 | 4 | 80.8945 | 75.7668 | -114.6657 | 12.3771 | 156.6721 | 0.0011 | 0.0150 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417136_097E403D | 504990 | 199 | -87.7 | 504990 | 302 | -91.3 | 504990 | 819 | -98.1 | 504990 | 108 |
| MR_1774417136_0359C14F | 504990 | 199 | -87.7 | 504990 | 302 | -92.2 | 504990 | 819 | -99.8 | 504990 | 108 |
| MR_1774417136_6E267EB5 | 504990 | 199 | -85.0 | 504990 | 302 | -93.6 | 504990 | 819 | -101.0 | 504990 | 108 |
| MR_1774417136_6512E587 | 504990 | 199 | -87.0 | 504990 | 302 | -94.2 | 504990 | 819 | -97.9 | 504990 | 108 |
| MR_1774417136_175DAB9C | 504990 | 199 | -86.5 | 504990 | 302 | -92.2 | 504990 | 819 | -99.5 | 504990 | 108 |
| MR_1774417136_93E580BB | 504990 | 199 | -86.9 | 504990 | 302 | -92.0 | 504990 | 819 | -99.6 | 504990 | 108 |
| MR_1774417136_065F3B0C | 504990 | 199 | -86.7 | 504990 | 302 | -92.1 | 504990 | 819 | -100.5 | 504990 | 108 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1835: `9ce9a526-0ab...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `9ce9a526-0ab8-49cd-92f8-9891aa77fd68` |
| Tag | **single-answer** |
| 정답 | **C21** |
| C21 의미 | Lift the tilt angle  of 3252300_4 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1835] topology](images/train_1835.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Check test server and transmission issues
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3215536_3
- `C3`: Insufficient data; more data is needed for judgment.
- `C4`: Adjust the azimuth of 3252300_4 by 50 degrees
- `C5`: Decrease A3 Offset threshold for 3215536_3
- `C6`: Add neighbor relationship between 3215536_3 and 3215644_2
- `C7`: Increase transmission power for 3215536_3
- `C8`: Add neighbor relationship between 3252300_4 and 3215644_2
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3215644_2
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3215536_3
- `C11`: Adjust the azimuth of 3215536_3 by 43 degrees
- `C12`: Increase A3 Offset threshold for 3215536_3
- `C13`: Increase A3 Offset threshold for 3215644_2
- `C14`: Press down the tilt angle  of 3252300_4 by 10 degrees
- `C15`: Decrease A3 Offset threshold for 3215644_2
- `C16`: Press down the tilt angle of 3215536_3 by 4 degrees
- `C17`: Decrease transmission power for 3215644_2
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3215644_2
- `C19`: Decrease transmission power for 3215536_3
- `C20`: Increase transmission power for 3215644_2
- `C21`: Lift the tilt angle  of 3252300_4 by 10 degrees **← 정답**
- `C22`: Lift the tilt angle of 3215536_3 by 4 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.494 | MS1 | 121.4656746011 | 31.1446265842 | 179 | 504990 | -86.60 | 12.08 | 478.89 | 0.16 | 2.11 | 1600 |
| 2024-09-20 22:21:32.920 | MS1 | 121.4656600242 | 31.1446236353 | 179 | 504990 | -87.12 | 13.54 | 343.01 | 0.11 | 2.21 | 1587 |
| 2024-09-20 22:21:33.503 | MS1 | 121.4656752246 | 31.1446351349 | 179 | 504990 | -87.08 | 14.74 | 575.95 | 0.15 | 2.21 | 1576 |
| 2024-09-20 22:21:34.148 | MS1 | 121.4656679178 | 31.1446366740 | 179 | 504990 | -89.13 | 13.92 | 40.51 | 0.11 | 2.14 | 1575 |
| 2024-09-20 22:21:35.575 | MS1 | 121.4656769017 | 31.1446277999 | 179 | 504990 | -91.34 | 16.51 | 53.34 | 0.02 | 2.72 | 1562 |
| 2024-09-20 22:21:36.738 | MS1 | 121.4656730959 | 31.1446181592 | 179 | 504990 | -91.56 | 12.89 | 80.12 | 0.11 | 2.26 | 1596 |
| 2024-09-20 22:21:37.217 | MS1 | 121.4656598994 | 31.1446211595 | 179 | 504990 | -92.20 | 7.56 | 47.97 | 0.06 | 2.30 | 1565 |
| 2024-09-20 22:21:38.314 | MS1 | 121.4656649800 | 31.1446213116 | 179 | 504990 | -91.62 | 10.47 | 73.14 | 0.13 | 2.63 | 1589 |
| 2024-09-20 22:21:39.191 | MS1 | 121.4656735805 | 31.1446313172 | 179 | 504990 | -92.10 | 9.53 | 72.04 | 0.01 | 2.66 | 1594 |
| 2024-09-20 22:21:40.802 | MS1 | 121.4656773588 | 31.1446298151 | 179 | 504990 | -90.83 | 7.21 | 420.77 | 0.11 | 2.11 | 1586 |
| 2024-09-20 22:21:41.404 | MS1 | 121.4656776839 | 31.1446213789 | 179 | 504990 | -93.10 | 9.68 | 573.06 | 0.01 | 2.82 | 1583 |
| 2024-09-20 22:21:42.200 | MS1 | 121.4656736445 | 31.1446218506 | 179 | 504990 | -90.99 | 11.92 | 308.34 | 0.16 | 2.23 | 1592 |

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
| 3215536 | 3 | 121.4738848408 | 31.1515749284 | 182 | 2 | 12 | 32.8 | TDD | 179 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3215644 | 2 | 121.4693778884 | 31.1549744153 | 9 | 9 | 12 | 20.1 | TDD | 868 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3218754 | 1 | 121.4723504626 | 31.1555866679 | 68 | 0 | 9 | 21.2 | TDD | 795 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3252300 | 4 | 121.4672323537 | 31.1479359776 | 49 | 8 | 11 | 36.7 | TDD | 36 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |

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
| 2024-09-20 22:21:31.015 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.035 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.178 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.178 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.875 | NREventA3 | measId:2;ServCellPCI:758;Se... |
| 2024-09-20 22:21:38.115 | NRHandoverAttempt | SourcePCI:758;SourceNR-ARFC... |
| 2024-09-20 22:21:38.159 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.169 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.286 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.286 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3218754 | 1 | 16.7090 | 13.1688 | -114.2580 | 10.6558 | 101.6384 | 0.0022 | 0.0003 |
| 2024_09_20 22:00 | 3215644 | 2 | 18.1721 | 11.8186 | -114.9788 | 18.5042 | 130.0209 | 0.0003 | 0.0007 |
| 2024_09_20 22:00 | 3215536 | 3 | 80.5239 | 82.8103 | -115.2068 | 11.3903 | 193.0026 | 0.0118 | 0.0101 |
| 2024_09_20 22:00 | 3252300 | 4 | 12.1175 | 10.4663 | -114.5565 | 12.0085 | 88.4652 | 0.0162 | 0.0159 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413189_1A80160C | 504990 | 179 | -90.5 | 504990 | 868 | -94.8 | 504990 | 36 | -96.8 | 504990 | 795 |
| MR_1774413189_358BB426 | 504990 | 179 | -88.3 | 504990 | 868 | -94.4 | 504990 | 36 | -95.9 | 504990 | 795 |
| MR_1774413189_22DCDFE2 | 504990 | 179 | -88.1 | 504990 | 868 | -96.9 | 504990 | 36 | -97.5 | 504990 | 795 |
| MR_1774413189_F6CB0413 | 504990 | 179 | -90.5 | 504990 | 868 | -93.6 | 504990 | 36 | -99.0 | 504990 | 795 |
| MR_1774413189_F4E13D4F | 504990 | 179 | -88.5 | 504990 | 868 | -96.9 | 504990 | 36 | -99.0 | 504990 | 795 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1836: `fb36c798-e72...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `fb36c798-e72d-4b94-be23-f9175e2b6cb7` |
| Tag | **single-answer** |
| 정답 | **C15** |
| C15 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1836] topology](images/train_1836.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3222374_2 by 31 degrees
- `C2`: Increase A3 Offset threshold for 3257600_3
- `C3`: Press down the tilt angle of 3222374_2 by 8 degrees
- `C4`: Decrease A3 Offset threshold for 3257600_3
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3222374_2
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3257600_3
- `C7`: Insufficient data; more data is needed for judgment.
- `C8`: Press down the tilt angle  of 3257600_3 by 10 degrees
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3222374_2
- `C10`: Add neighbor relationship between 3222374_2 and 3257600_3
- `C11`: Decrease A3 Offset threshold for 3222374_2
- `C12`: Adjust the azimuth of 3257600_3 by 3 degrees
- `C13`: Increase A3 Offset threshold for 3222374_2
- `C14`: Lift the tilt angle  of 3257600_3 by 10 degrees
- `C15`: Check test server and transmission issues **← 정답**
- `C16`: Increase transmission power for 3222374_2
- `C17`: Lift the tilt angle of 3222374_2 by 8 degrees
- `C18`: Add neighbor relationship between 3231533_1 and 3257600_3
- `C19`: Decrease transmission power for 3222374_2
- `C20`: Increase transmission power for 3257600_3
- `C21`: Decrease transmission power for 3257600_3
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3257600_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.683 | MS1 | 121.4656621888 | 31.1446347232 | 260 | 504990 | -85.33 | 17.59 | 446.67 | 0.09 | 2.65 | 1577 |
| 2024-09-20 22:21:32.403 | MS1 | 121.4656661440 | 31.1446261728 | 260 | 504990 | -86.92 | 14.75 | 530.05 | 0.20 | 2.18 | 1573 |
| 2024-09-20 22:21:33.131 | MS1 | 121.4656582357 | 31.1446301441 | 260 | 504990 | -89.12 | 17.42 | 431.89 | 0.15 | 2.57 | 1585 |
| 2024-09-20 22:21:34.398 | MS1 | 121.4656671245 | 31.1446250742 | 260 | 504990 | -86.61 | 13.07 | 57.20 | 0.13 | 2.26 | 414 |
| 2024-09-20 22:21:35.945 | MS1 | 121.4656699803 | 31.1446221282 | 260 | 504990 | -89.12 | 16.57 | 57.13 | 0.10 | 2.90 | 471 |
| 2024-09-20 22:21:36.348 | MS1 | 121.4656775273 | 31.1446292100 | 260 | 504990 | -86.80 | 12.60 | 92.27 | 0.04 | 2.46 | 376 |
| 2024-09-20 22:21:37.556 | MS1 | 121.4656699552 | 31.1446193738 | 260 | 504990 | -91.41 | 8.21 | 90.28 | 0.06 | 2.98 | 496 |
| 2024-09-20 22:21:38.941 | MS1 | 121.4656624988 | 31.1446238244 | 260 | 504990 | -93.11 | 10.64 | 84.05 | 0.03 | 2.95 | 384 |
| 2024-09-20 22:21:39.570 | MS1 | 121.4656641108 | 31.1446332057 | 260 | 504990 | -92.81 | 9.45 | 102.97 | 0.07 | 2.86 | 320 |
| 2024-09-20 22:21:40.597 | MS1 | 121.4656728329 | 31.1446257754 | 260 | 504990 | -93.43 | 9.37 | 449.89 | 0.14 | 2.18 | 1595 |
| 2024-09-20 22:21:41.157 | MS1 | 121.4656739082 | 31.1446213992 | 260 | 504990 | -90.29 | 10.96 | 592.11 | 0.17 | 2.38 | 1587 |
| 2024-09-20 22:21:42.389 | MS1 | 121.4656766162 | 31.1446277194 | 260 | 504990 | -91.82 | 12.73 | 469.49 | 0.01 | 2.39 | 1570 |

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
| 3220903 | 4 | 121.4668883716 | 31.1518007604 | 22 | 6 | 11 | 44.1 | TDD | 999 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3222374 | 2 | 121.4718661161 | 31.1508496969 | 251 | 5 | 8 | 46.2 | TDD | 260 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3231533 | 1 | 121.4661358590 | 31.1440944107 | 233 | 9 | 5 | 43.7 | TDD | 868 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3257600 | 3 | 121.4732645829 | 31.1474712164 | 243 | 10 | 3 | 17.9 | TDD | 166 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |

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
| 2024-09-20 22:21:31.029 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.050 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.165 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.165 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.843 | NREventA3 | measId:2;ServCellPCI:719;Se... |
| 2024-09-20 22:21:38.083 | NRHandoverAttempt | SourcePCI:719;SourceNR-ARFC... |
| 2024-09-20 22:21:38.131 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.141 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.257 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.257 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3231533 | 1 | 7.6389 | 13.3487 | -114.6010 | 11.6155 | 140.5185 | 0.0196 | 0.0139 |
| 2024_09_20 22:00 | 3222374 | 2 | 8.3845 | 13.8099 | -114.5938 | 15.5466 | 121.4278 | 0.0005 | 0.0012 |
| 2024_09_20 22:00 | 3257600 | 3 | 19.2431 | 7.7056 | -114.4542 | 6.8983 | 143.7534 | 0.0113 | 0.0117 |
| 2024_09_20 22:00 | 3220903 | 4 | 7.7173 | 12.6722 | -115.8984 | 15.5117 | 86.5247 | 0.0037 | 0.0015 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414322_890214DB | 504990 | 260 | -88.0 | 504990 | 166 | -93.1 | 504990 | 868 | -101.0 | 504990 | 999 |
| MR_1774414322_49ED8362 | 504990 | 260 | -86.9 | 504990 | 166 | -90.9 | 504990 | 868 | -99.8 | 504990 | 999 |
| MR_1774414322_2C77CBA3 | 504990 | 260 | -88.1 | 504990 | 166 | -92.4 | 504990 | 868 | -98.4 | 504990 | 999 |
| MR_1774414322_3F5309A3 | 504990 | 260 | -86.1 | 504990 | 166 | -92.6 | 504990 | 868 | -100.3 | 504990 | 999 |
| MR_1774414322_63A6F60C | 504990 | 260 | -88.2 | 504990 | 166 | -90.1 | 504990 | 868 | -100.6 | 504990 | 999 |
| MR_1774414322_BECE7EC3 | 504990 | 260 | -85.3 | 504990 | 166 | -93.9 | 504990 | 868 | -101.3 | 504990 | 999 |
| MR_1774414322_E9A3931F | 504990 | 260 | -86.4 | 504990 | 166 | -93.7 | 504990 | 868 | -99.7 | 504990 | 999 |
| MR_1774414322_80B54DBE | 504990 | 260 | -88.2 | 504990 | 166 | -92.9 | 504990 | 868 | -97.9 | 504990 | 999 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1837: `84ace18d-f07...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `84ace18d-f074-4830-a7a5-31ca19d803cd` |
| Tag | **single-answer** |
| 정답 | **C3** |
| C3 의미 | Lift the tilt angle  of 3226861_1 by 8 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1837] topology](images/train_1837.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3220111_3
- `C2`: Check test server and transmission issues
- `C3`: Lift the tilt angle  of 3226861_1 by 8 degrees **← 정답**
- `C4`: Decrease transmission power for 3243682_4
- `C5`: Insufficient data; more data is needed for judgment.
- `C6`: Adjust the azimuth of 3226861_1 by 50 degrees
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3243682_4
- `C8`: Increase A3 Offset threshold for 3243682_4
- `C9`: Decrease A3 Offset threshold for 3243682_4
- `C10`: Lift the tilt angle of 3220111_3 by 6 degrees
- `C11`: Press down the tilt angle of 3220111_3 by 6 degrees
- `C12`: Decrease A3 Offset threshold for 3220111_3
- `C13`: Increase transmission power for 3220111_3
- `C14`: Adjust the azimuth of 3220111_3 by 33 degrees
- `C15`: Increase A3 Offset threshold for 3220111_3
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3243682_4
- `C17`: Add neighbor relationship between 3220111_3 and 3243682_4
- `C18`: Add neighbor relationship between 3226861_1 and 3243682_4
- `C19`: Press down the tilt angle  of 3226861_1 by 8 degrees
- `C20`: Increase transmission power for 3243682_4
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3220111_3
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3220111_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.338 | MS1 | 121.4656651008 | 31.1446224963 | 868 | 504990 | -87.85 | 12.76 | 583.24 | 0.02 | 2.50 | 1580 |
| 2024-09-20 22:21:32.346 | MS1 | 121.4656668158 | 31.1446346312 | 868 | 504990 | -90.24 | 15.21 | 453.92 | 0.11 | 2.57 | 1564 |
| 2024-09-20 22:21:33.564 | MS1 | 121.4656655504 | 31.1446254168 | 868 | 504990 | -87.62 | 16.11 | 583.47 | 0.10 | 2.18 | 1587 |
| 2024-09-20 22:21:34.609 | MS1 | 121.4656632381 | 31.1446183411 | 868 | 504990 | -88.43 | 17.61 | 58.02 | 0.01 | 2.76 | 1567 |
| 2024-09-20 22:21:35.811 | MS1 | 121.4656717767 | 31.1446223252 | 868 | 504990 | -91.17 | 15.98 | 67.22 | 0.05 | 2.82 | 1578 |
| 2024-09-20 22:21:36.340 | MS1 | 121.4656639272 | 31.1446256799 | 868 | 504990 | -88.42 | 15.22 | 99.25 | 0.18 | 2.45 | 1563 |
| 2024-09-20 22:21:37.946 | MS1 | 121.4656605519 | 31.1446241872 | 868 | 504990 | -90.55 | 10.59 | 90.04 | 0.19 | 2.76 | 1595 |
| 2024-09-20 22:21:38.594 | MS1 | 121.4656699057 | 31.1446310639 | 868 | 504990 | -89.26 | 12.55 | 77.06 | 0.11 | 2.51 | 1594 |
| 2024-09-20 22:21:39.314 | MS1 | 121.4656766827 | 31.1446257006 | 868 | 504990 | -90.39 | 12.77 | 94.63 | 0.01 | 2.00 | 1591 |
| 2024-09-20 22:21:40.265 | MS1 | 121.4656758850 | 31.1446314881 | 868 | 504990 | -90.10 | 7.77 | 546.68 | 0.09 | 2.06 | 1587 |
| 2024-09-20 22:21:41.269 | MS1 | 121.4656732370 | 31.1446329863 | 868 | 504990 | -90.10 | 9.54 | 452.55 | 0.10 | 2.24 | 1578 |
| 2024-09-20 22:21:42.331 | MS1 | 121.4656641066 | 31.1446281431 | 868 | 504990 | -89.66 | 12.59 | 328.37 | 0.02 | 2.66 | 1591 |

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
| 3220111 | 3 | 121.4759081284 | 31.1523177787 | 196 | 4 | 3 | 43.1 | TDD | 868 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3226861 | 1 | 121.4659626077 | 31.1520080747 | 341 | 12 | 0 | 22.1 | TDD | 793 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3243682 | 4 | 121.4707465092 | 31.1486604029 | 316 | 7 | 3 | 16.1 | TDD | 699 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3255387 | 2 | 121.4641853125 | 31.1486988143 | 134 | 6 | 9 | 18.7 | TDD | 83 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:30.924 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.071 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.071 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.757 | NREventA3 | measId:2;ServCellPCI:311;Se... |
| 2024-09-20 22:21:37.997 | NRHandoverAttempt | SourcePCI:311;SourceNR-ARFC... |
| 2024-09-20 22:21:38.031 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.046 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.196 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.196 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3226861 | 1 | 8.4825 | 9.7151 | -114.4154 | 5.8198 | 179.7478 | 0.0132 | 0.0127 |
| 2024_09_20 22:00 | 3255387 | 2 | 8.5329 | 15.6431 | -117.4310 | 17.3441 | 92.3858 | 0.0173 | 0.0136 |
| 2024_09_20 22:00 | 3220111 | 3 | 93.3210 | 88.3538 | -117.3520 | 7.1932 | 119.8823 | 0.0167 | 0.0093 |
| 2024_09_20 22:00 | 3243682 | 4 | 11.3651 | 7.2744 | -116.4811 | 11.5489 | 174.4744 | 0.0188 | 0.0094 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416690_58657B74 | 504990 | 868 | -87.5 | 504990 | 699 | -90.9 | 504990 | 793 | -99.0 | 504990 | 83 |
| MR_1774416690_1C9DCE3A | 504990 | 868 | -89.9 | 504990 | 699 | -91.1 | 504990 | 793 | -97.9 | 504990 | 83 |
| MR_1774416690_BAB17BD2 | 504990 | 868 | -87.3 | 504990 | 699 | -89.2 | 504990 | 793 | -98.8 | 504990 | 83 |
| MR_1774416690_D949590B | 504990 | 868 | -89.7 | 504990 | 699 | -88.4 | 504990 | 793 | -100.9 | 504990 | 83 |
| MR_1774416690_ECBDD5C2 | 504990 | 868 | -87.9 | 504990 | 699 | -88.6 | 504990 | 793 | -99.9 | 504990 | 83 |
| MR_1774416690_31274297 | 504990 | 868 | -87.0 | 504990 | 699 | -89.0 | 504990 | 793 | -100.6 | 504990 | 83 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1838: `c0114e44-c0b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `c0114e44-c0b3-4459-8658-9e187a9d6a2a` |
| Tag | **multiple-answer** |
| 정답 | **C2|C6|C8|C14** |
| C2 의미 | Decrease transmission power for 3254478_3 |
| C6 의미 | Increase A3 Offset threshold for 3253592_2 |
| C8 의미 | Press down the tilt angle  of 3254478_3 by 5 degrees |
| C14 의미 | Increase A3 Offset threshold for 3254478_3 |
| 패턴 분류 | **P3 Overshoot (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1838] topology](images/train_1838.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 5 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 5개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3254478_3
- `C2`: Decrease transmission power for 3254478_3 **← 정답**
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3253592_2
- `C4`: Decrease transmission power for 3253592_2
- `C5`: Increase transmission power for 3253592_2
- `C6`: Increase A3 Offset threshold for 3253592_2 **← 정답**
- `C7`: Add neighbor relationship between 3253592_2 and 3254478_3
- `C8`: Press down the tilt angle  of 3254478_3 by 5 degrees **← 정답**
- `C9`: Decrease A3 Offset threshold for 3254478_3
- `C10`: Press down the tilt angle of 3253592_2 by 5 degrees
- `C11`: Adjust the azimuth of 3254478_3 by 43 degrees
- `C12`: Check test server and transmission issues
- `C13`: Lift the tilt angle  of 3254478_3 by 5 degrees
- `C14`: Increase A3 Offset threshold for 3254478_3 **← 정답**
- `C15`: Insufficient data; more data is needed for judgment.
- `C16`: Increase transmission power for 3254478_3
- `C17`: Adjust the azimuth of 3253592_2 by 6 degrees
- `C18`: Lift the tilt angle of 3253592_2 by 5 degrees
- `C19`: Decrease A3 Offset threshold for 3253592_2
- `C20`: Add neighbor relationship between 3259706_5 and 3254478_3
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3254478_3
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3253592_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.785 | MS1 | 121.4656634569 | 31.1446344895 | 133 | 504990 | -80.01 | 14.91 | 505.66 | 0.14 | 2.66 | 1586 |
| 2024-09-20 22:21:32.314 | MS1 | 121.4656701846 | 31.1446296278 | 133 | 504990 | -76.43 | 13.46 | 309.53 | 0.14 | 2.33 | 1584 |
| 2024-09-20 22:21:33.493 | MS1 | 121.4656751557 | 31.1446286816 | 133 | 504990 | -82.67 | 13.69 | 557.14 | 0.08 | 2.83 | 1598 |
| 2024-09-20 22:21:34.875 | MS1 | 121.4656716950 | 31.1446246220 | 260 | 504990 | -87.42 | 2.96 | 79.11 | 0.06 | 1.07 | 1580 |
| 2024-09-20 22:21:35.102 | MS1 | 121.4656724141 | 31.1446215900 | 260 | 504990 | -85.19 | 2.69 | 61.56 | 0.06 | 1.50 | 1573 |
| 2024-09-20 22:21:36.634 | MS1 | 121.4656632173 | 31.1446345988 | 133 | 504990 | -80.26 | 1.39 | 57.91 | 0.13 | 1.02 | 1586 |
| 2024-09-20 22:21:37.251 | MS1 | 121.4656773870 | 31.1446374079 | 133 | 504990 | -87.45 | 3.20 | 55.33 | 0.01 | 1.13 | 1586 |
| 2024-09-20 22:21:38.534 | MS1 | 121.4656612787 | 31.1446206378 | 260 | 504990 | -87.73 | 2.43 | 59.78 | 0.08 | 1.45 | 1596 |
| 2024-09-20 22:21:39.410 | MS1 | 121.4656635139 | 31.1446351195 | 260 | 504990 | -83.86 | 4.97 | 79.80 | 0.14 | 1.06 | 1593 |
| 2024-09-20 22:21:40.260 | MS1 | 121.4656739743 | 31.1446261076 | 260 | 504990 | -80.62 | 12.49 | 383.88 | 0.17 | 2.84 | 1571 |
| 2024-09-20 22:21:41.965 | MS1 | 121.4656695012 | 31.1446258861 | 260 | 504990 | -75.85 | 12.11 | 324.18 | 0.01 | 2.50 | 1560 |
| 2024-09-20 22:21:42.331 | MS1 | 121.4656732056 | 31.1446231250 | 260 | 504990 | -80.16 | 15.16 | 572.72 | 0.01 | 2.88 | 1588 |

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
| 3231790 | 1 | 121.4699872617 | 31.1526104649 | 265 | 7 | 0 | 29.9 | TDD | 260 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3253592 | 2 | 121.4669762422 | 31.1502421025 | 197 | 3 | 2 | 24.5 | TDD | 133 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3254478 | 3 | 121.4733349120 | 31.1531014204 | 175 | 3 | 11 | 43.8 | TDD | 717 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3259706 | 5 | 121.4640295331 | 31.1558890132 | 289 | 0 | 12 | 20.6 | TDD | 954 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3262187 | 4 | 121.4722066571 | 31.1489303485 | 221 | 10 | 11 | 37.4 | TDD | 819 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |

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
| 2024-09-20 22:21:31.560 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.577 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.690 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.690 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.381 | NREventA3 | measId:2;ServCellPCI:102;Se... |
| 2024-09-20 22:21:34.621 | NRHandoverAttempt | SourcePCI:102;SourceNR-ARFC... |
| 2024-09-20 22:21:34.666 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:34.679 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:34.820 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:34.820 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:36.381 | NREventA3 | measId:2;ServCellPCI:517;Se... |
| 2024-09-20 22:21:36.621 | NRHandoverAttempt | SourcePCI:517;SourceNR-ARFC... |
| 2024-09-20 22:21:36.658 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:36.668 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:36.781 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.781 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.381 | NREventA3 | measId:2;ServCellPCI:102;Se... |
| 2024-09-20 22:21:38.621 | NRHandoverAttempt | SourcePCI:102;SourceNR-ARFC... |
| 2024-09-20 22:21:38.657 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.669 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.795 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.795 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3231790 | 1 | 17.4374 | 16.3178 | -114.4185 | 18.9263 | 164.1736 | 0.0104 | 0.0001 |
| 2024_09_20 22:00 | 3253592 | 2 | 14.7756 | 8.1570 | -116.0851 | 5.2250 | 117.4855 | 0.0129 | 0.0063 |
| 2024_09_20 22:00 | 3254478 | 3 | 14.4312 | 15.0558 | -114.1652 | 12.5285 | 171.2312 | 0.0148 | 0.0188 |
| 2024_09_20 22:00 | 3262187 | 4 | 19.9213 | 16.2259 | -116.6137 | 10.9448 | 154.2501 | 0.0045 | 0.0055 |
| 2024_09_20 22:00 | 3259706 | 5 | 9.5682 | 11.0472 | -116.1873 | 16.2752 | 82.0650 | 0.0088 | 0.0068 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414626_F7AD8C2E | 504990 | 260 | -88.9 | 504990 | 133 | -85.0 | 504990 | 717 | -88.8 | 504990 | 954 |
| MR_1774414626_C31D319F | 504990 | 260 | -87.7 | 504990 | 133 | -85.5 | 504990 | 717 | -86.1 | 504990 | 954 |
| MR_1774414626_7AA3700B | 504990 | 260 | -89.0 | 504990 | 133 | -83.8 | 504990 | 717 | -88.2 | 504990 | 954 |
| MR_1774414626_F40B9A93 | 504990 | 260 | -86.8 | 504990 | 133 | -83.1 | 504990 | 717 | -87.0 | 504990 | 954 |
| MR_1774414626_D2B11F1B | 504990 | 133 | -86.4 | 504990 | 260 | -85.0 | 504990 | 717 | -86.1 | 504990 | 954 |
| MR_1774414626_252F02CF | 504990 | 260 | -89.4 | 504990 | 133 | -84.8 | 504990 | 717 | -88.7 | 504990 | 954 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1839: `6433ee79-efe...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `6433ee79-efe6-4259-a0ae-b495c2201db1` |
| Tag | **single-answer** |
| 정답 | **C14** |
| C14 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3230513_2 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1839] topology](images/train_1839.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3230513_2
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3214309_4
- `C3`: Lift the tilt angle of 3230513_2 by 4 degrees
- `C4`: Decrease transmission power for 3230513_2
- `C5`: Press down the tilt angle of 3230513_2 by 4 degrees
- `C6`: Increase A3 Offset threshold for 3230513_2
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3214309_4
- `C8`: Add neighbor relationship between 3259589_10 and 3214309_4
- `C9`: Increase transmission power for 3230513_2
- `C10`: Adjust the azimuth of 3230513_2 by 28 degrees
- `C11`: Decrease A3 Offset threshold for 3230513_2
- `C12`: Increase transmission power for 3214309_4
- `C13`: Lift the tilt angle  of 3214309_4 by 6 degrees
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3230513_2 **← 정답**
- `C15`: Increase A3 Offset threshold for 3214309_4
- `C16`: Add neighbor relationship between 3230513_2 and 3214309_4
- `C17`: Press down the tilt angle  of 3214309_4 by 6 degrees
- `C18`: Check test server and transmission issues
- `C19`: Insufficient data; more data is needed for judgment.
- `C20`: Adjust the azimuth of 3214309_4 by 48 degrees
- `C21`: Decrease A3 Offset threshold for 3214309_4
- `C22`: Decrease transmission power for 3214309_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.312 | MS1 | 121.4656599012 | 31.1446245328 | 70 | 504990 | -94.13 | 12.32 | 353.07 | 0.00 | 2.60 | 1582 |
| 2024-09-20 22:21:32.877 | MS1 | 121.4656769030 | 31.1446321624 | 800 | 504990 | -93.54 | 9.39 | 436.47 | 0.08 | 2.98 | 1591 |
| 2024-09-20 22:21:33.358 | MS1 | 121.4656731887 | 31.1446363569 | 306 | 504990 | -94.72 | 12.87 | 313.69 | 0.11 | 2.05 | 1597 |
| 2024-09-20 22:21:34.360 | MS1 | 121.4656608900 | 31.1446232278 | 646 | 152650 | -96.74 | 3.52 | 90.99 | 0.07 | 1.65 | 996 |
| 2024-09-20 22:21:35.376 | MS1 | 121.4656647665 | 31.1446223784 | 164 | 152650 | -89.76 | 5.24 | 81.06 | 0.04 | 1.53 | 944 |
| 2024-09-20 22:21:36.639 | MS1 | 121.4656771756 | 31.1446245593 | 520 | 152650 | -89.32 | 4.30 | 69.19 | 0.01 | 1.72 | 974 |
| 2024-09-20 22:21:37.705 | MS1 | 121.4656670521 | 31.1446190143 | 392 | 152650 | -90.95 | 4.82 | 102.90 | 0.14 | 2.00 | 985 |
| 2024-09-20 22:21:38.338 | MS1 | 121.4656625736 | 31.1446240120 | 646 | 152650 | -92.90 | 4.11 | 62.90 | 0.11 | 1.77 | 950 |
| 2024-09-20 22:21:39.145 | MS1 | 121.4656722123 | 31.1446195949 | 164 | 152650 | -90.16 | 5.55 | 70.12 | 0.15 | 1.87 | 975 |
| 2024-09-20 22:21:40.827 | MS1 | 121.4656629484 | 31.1446269254 | 520 | 152650 | -89.29 | 5.77 | 83.85 | 0.11 | 2.97 | 1562 |
| 2024-09-20 22:21:41.965 | MS1 | 121.4656593020 | 31.1446361883 | 392 | 152650 | -94.28 | 7.50 | 46.16 | 0.03 | 2.89 | 1562 |
| 2024-09-20 22:21:42.450 | MS1 | 121.4656702878 | 31.1446203589 | 646 | 152650 | -93.15 | 5.13 | 67.39 | 0.00 | 2.83 | 1561 |

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
| 3214309 | 4 | 121.4728060594 | 31.1543537894 | 164 | 5 | 4 | 16.8 | TDD | 402 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3217569 | 12 | 121.4750160584 | 31.1450527993 | 28 | 12 | 5 | 28.4 | FDD | 392 | n1 | 152650 | 30M | 4T4R | 21 | 152650 |
| 3225037 | 1 | 121.4659838466 | 31.1453671674 | 89 | 7 | 1 | 9.0 | TDD | 800 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3230513 | 2 | 121.4675877128 | 31.1521905481 | 164 | 3 | 7 | 16.4 | TDD | 70 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3238319 | 11 | 121.4714822019 | 31.1457669468 | 355 | 8 | 6 | 26.6 | FDD | 776 | n1 | 152650 | 30M | 4T4R | 12 | 152650 |
| 3245821 | 9 | 121.4753831390 | 31.1537877204 | 36 | 7 | 0 | 0.3 | FDD | 646 | n1 | 152650 | 30M | 4T4R | 17 | 152650 |
| 3248587 | 3 | 121.4728200130 | 31.1473217268 | 322 | 11 | 0 | 27.0 | TDD | 306 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3249950 | 5 | 121.4668608834 | 31.1513466441 | 307 | 2 | 3 | 27.7 | TDD | 27 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3253014 | 13 | 121.4660623382 | 31.1490747027 | 67 | 2 | 4 | 16.7 | FDD | 763 | n1 | 152650 | 30M | 4T4R | 27 | 152650 |
| 3255939 | 7 | 121.4641258884 | 31.1476377957 | 307 | 5 | 8 | 1.9 | FDD | 164 | n1 | 152650 | 30M | 4T4R | 27 | 152650 |
| 3259589 | 10 | 121.4748714632 | 31.1494010861 | 291 | 12 | 0 | 6.7 | FDD | 520 | n1 | 152650 | 30M | 4T4R | 25 | 152650 |
| 3271812 | 6 | 121.4663243213 | 31.1445502781 | 278 | 5 | 11 | 10.6 | TDD | 733 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3277753 | 8 | 121.4757600186 | 31.1537390733 | 344 | 2 | 6 | 1.8 | FDD | 581 | n1 | 152650 | 30M | 4T4R | 26 | 152650 |

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
| 2024-09-20 22:21:31.212 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.230 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.336 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.336 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.040 | NREventA2 | measId:1;ServCellPCI:343;Se... |
| 2024-09-20 22:21:35.145 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.379 | NREventA5 | measId:3;ServCellPCI:343;Se... |
| 2024-09-20 22:21:35.410 | NRHandoverAttempt | SourcePCI:343;SourceNR-ARFC... |
| 2024-09-20 22:21:35.432 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.442 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:35.561 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.561 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3225037 | 1 | 10.8221 | 19.9100 | -116.2816 | 14.4487 | 127.6855 | 0.0029 | 0.0002 |
| 2024_09_20 22:00 | 3230513 | 2 | 12.1760 | 7.4970 | -116.8861 | 15.4744 | 94.6770 | 0.0129 | 0.0101 |
| 2024_09_20 22:00 | 3248587 | 3 | 7.7829 | 11.0367 | -117.2427 | 17.4614 | 139.4686 | 0.0026 | 0.0164 |
| 2024_09_20 22:00 | 3214309 | 4 | 14.1496 | 7.5322 | -116.9907 | 13.7596 | 90.4930 | 0.0198 | 0.0021 |
| 2024_09_20 22:00 | 3249950 | 5 | 9.8130 | 10.1280 | -117.8574 | 10.4768 | 138.8322 | 0.0080 | 0.0104 |
| 2024_09_20 22:00 | 3271812 | 6 | 15.5541 | 7.0160 | -115.5343 | 10.3742 | 96.8961 | 0.0072 | 0.0093 |
| 2024_09_20 22:00 | 3255939 | 7 | 14.0874 | 14.0254 | -115.6023 | 4.9629 | 36.1234 | 0.0084 | 0.0090 |
| 2024_09_20 22:00 | 3277753 | 8 | 16.1634 | 15.3775 | -115.0471 | 3.5741 | 23.2839 | 0.0159 | 0.0129 |
| 2024_09_20 22:00 | 3245821 | 9 | 13.1111 | 18.2233 | -116.2565 | 4.2934 | 22.5040 | 0.0015 | 0.0198 |
| 2024_09_20 22:00 | 3259589 | 10 | 14.0861 | 8.7012 | -114.9192 | 4.8691 | 44.1285 | 0.0054 | 0.0127 |
| 2024_09_20 22:00 | 3238319 | 11 | 19.0173 | 17.5745 | -115.0672 | 3.1992 | 56.6759 | 0.0101 | 0.0089 |
| 2024_09_20 22:00 | 3217569 | 12 | 17.3311 | 14.7092 | -115.3462 | 3.1108 | 27.9687 | 0.0137 | 0.0114 |
| 2024_09_20 22:00 | 3253014 | 13 | 16.4359 | 13.2121 | -117.4859 | 4.7715 | 59.9279 | 0.0066 | 0.0078 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414630_6D9A3A6F | 504990 | 306 | -95.6 | 504990 | 402 | -97.9 | 504990 | 733 | -102.4 | 504990 | 27 |
| MR_1774414630_D8F97D64 | 504990 | 306 | -94.7 | 504990 | 402 | -99.6 | 504990 | 733 | -102.4 | 504990 | 27 |
| MR_1774414630_02DD187D | 152650 | 646 | -96.5 | 152650 | 776 | -97.5 | 152650 | 581 | -108.9 | 152650 | 763 |
| MR_1774414630_E04EDB3F | 504990 | 306 | -95.8 | 504990 | 402 | -96.3 | 504990 | 733 | -100.3 | 504990 | 27 |
| MR_1774414630_126A217E | 504990 | 306 | -96.5 | 504990 | 402 | -99.9 | 504990 | 733 | -100.1 | 504990 | 27 |
| MR_1774414630_643233A7 | 152650 | 646 | -95.4 | 152650 | 776 | -98.4 | 152650 | 581 | -105.7 | 152650 | 763 |
| MR_1774414630_9BA649B4 | 504990 | 306 | -93.4 | 504990 | 402 | -98.2 | 504990 | 733 | -100.1 | 504990 | 27 |

> *... 2개 열 생략 (전체 14열)*

---
