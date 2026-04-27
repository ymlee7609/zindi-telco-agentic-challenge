# Track A 문제 분석 — train[790]~train[799]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[790] ~ train[799] (10개)

## 목차

1. [문제 790: `134167e4-acb...`](#790) — single-answer, 정답: C8
2. [문제 791: `0ac0c1be-87c...`](#791) — single-answer, 정답: C8
3. [문제 792: `72333785-4f4...`](#792) — multiple-answer, 정답: C7|C13
4. [문제 793: `0716500d-ba8...`](#793) — single-answer, 정답: C16
5. [문제 794: `4ca7eb58-f07...`](#794) — single-answer, 정답: C2
6. [문제 795: `bf138cbf-70a...`](#795) — single-answer, 정답: C16
7. [문제 796: `473a49ab-e35...`](#796) — single-answer, 정답: C18
8. [문제 797: `e7234bdb-303...`](#797) — single-answer, 정답: C7
9. [문제 798: `2aa0f8fc-9db...`](#798) — single-answer, 정답: C7
10. [문제 799: `8a9604f8-d40...`](#799) — single-answer, 정답: C14

---

### 문제 790: `134167e4-acb...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `134167e4-acbc-4169-8dc0-28bffe92eb99` |
| Tag | **single-answer** |
| 정답 | **C8** |
| C8 의미 | Add neighbor relationship between 3259370_3 and 3226769_1 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[790] topology](images/train_0790.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3226769_1
- `C2`: Press down the tilt angle of 3259370_3 by 6 degrees
- `C3`: Decrease A3 Offset threshold for 3259370_3
- `C4`: Lift the tilt angle  of 3226769_1 by 5 degrees
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3226769_1
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3259370_3
- `C7`: Increase A3 Offset threshold for 3259370_3
- `C8`: Add neighbor relationship between 3259370_3 and 3226769_1 **← 정답**
- `C9`: Lift the tilt angle of 3259370_3 by 6 degrees
- `C10`: Adjust the azimuth of 3226769_1 by 12 degrees
- `C11`: Increase transmission power for 3259370_3
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3259370_3
- `C13`: Decrease A3 Offset threshold for 3226769_1
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3226769_1
- `C15`: Check test server and transmission issues
- `C16`: Increase A3 Offset threshold for 3226769_1
- `C17`: Adjust the azimuth of 3259370_3 by 3 degrees
- `C18`: Decrease transmission power for 3259370_3
- `C19`: Insufficient data; more data is needed for judgment.
- `C20`: Add neighbor relationship between 3230200_4 and 3226769_1
- `C21`: Press down the tilt angle  of 3226769_1 by 5 degrees
- `C22`: Decrease transmission power for 3226769_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.610 | MS1 | 121.4656762623 | 31.1446368027 | 725 | 504990 | -76.94 | 14.07 | 345.65 | 0.04 | 2.13 | 1592 |
| 2024-09-20 22:21:32.751 | MS1 | 121.4656584655 | 31.1446362026 | 725 | 504990 | -81.33 | 17.79 | 478.44 | 0.13 | 2.19 | 1577 |
| 2024-09-20 22:21:33.380 | MS1 | 121.4656601202 | 31.1446238994 | 725 | 504990 | -81.13 | 13.19 | 325.08 | 0.10 | 2.22 | 1579 |
| 2024-09-20 22:21:34.622 | MS1 | 121.4656587815 | 31.1446367445 | 725 | 504990 | -91.66 | -3.23 | 49.48 | 0.05 | 1.03 | 1583 |
| 2024-09-20 22:21:35.567 | MS1 | 121.4656660223 | 31.1446226132 | 725 | 504990 | -91.99 | -0.87 | 67.41 | 0.19 | 1.25 | 1593 |
| 2024-09-20 22:21:36.328 | MS1 | 121.4656582639 | 31.1446363370 | 725 | 504990 | -85.53 | -3.59 | 49.54 | 0.14 | 1.39 | 1586 |
| 2024-09-20 22:21:37.100 | MS1 | 121.4656761577 | 31.1446207488 | 725 | 504990 | -87.86 | -0.25 | 27.49 | 0.20 | 1.17 | 1592 |
| 2024-09-20 22:21:38.704 | MS1 | 121.4656583758 | 31.1446189651 | 725 | 504990 | -81.07 | 16.16 | 588.24 | 0.15 | 1.07 | 1567 |
| 2024-09-20 22:21:39.408 | MS1 | 121.4656674511 | 31.1446240885 | 725 | 504990 | -83.98 | 13.67 | 541.47 | 0.11 | 1.22 | 1591 |
| 2024-09-20 22:21:40.886 | MS1 | 121.4656774275 | 31.1446191181 | 725 | 504990 | -84.18 | 13.76 | 558.14 | 0.08 | 2.24 | 1578 |
| 2024-09-20 22:21:41.900 | MS1 | 121.4656643273 | 31.1446377379 | 725 | 504990 | -77.17 | 15.96 | 345.25 | 0.17 | 2.68 | 1583 |
| 2024-09-20 22:21:42.983 | MS1 | 121.4656717481 | 31.1446347888 | 725 | 504990 | -75.95 | 12.92 | 325.43 | 0.01 | 2.86 | 1598 |

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
| 3226769 | 1 | 121.4741636597 | 31.1474399964 | 237 | 4 | 1 | 18.3 | TDD | 10 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3230200 | 4 | 121.4735132563 | 31.1557981952 | 145 | 6 | 10 | 37.8 | TDD | 230 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3259370 | 3 | 121.4752133647 | 31.1545241336 | 216 | 5 | 11 | 26.3 | TDD | 725 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3273369 | 2 | 121.4711727153 | 31.1457156602 | 117 | 3 | 5 | 25.0 | TDD | 195 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:31.030 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.052 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.173 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.173 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.873 | NREventA3 | measId:2;ServCellPCI:51;Ser... |
| 2024-09-20 22:21:35.873 | NREventA3 | measId:2;ServCellPCI:51;Ser... |
| 2024-09-20 22:21:36.873 | NREventA3 | measId:2;ServCellPCI:51;Ser... |
| 2024-09-20 22:21:39.373 | NRRRCReestablishAttempt | PCI:51 |
| 2024-09-20 22:21:39.386 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.401 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:39.545 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.545 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3226769 | 1 | 5.4607 | 10.6248 | -116.8047 | 5.4058 | 188.5367 | 0.0036 | 0.0135 |
| 2024_09_20 22:00 | 3273369 | 2 | 16.3274 | 18.4028 | -117.5248 | 18.4578 | 182.4175 | 0.0127 | 0.0186 |
| 2024_09_20 22:00 | 3259370 | 3 | 16.5081 | 13.2967 | -114.5027 | 18.5099 | 198.6699 | 0.0007 | 0.1992 |
| 2024_09_20 22:00 | 3230200 | 4 | 13.6875 | 10.9471 | -116.3960 | 8.4058 | 147.6042 | 0.0186 | 0.0101 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414599_628FB41D | 504990 | 10 | -87.8 | 504990 | 725 | -91.8 | 504990 | 230 | -85.9 | 504990 | 195 |
| MR_1774414599_5D71A949 | 504990 | 725 | -93.6 | 504990 | 10 | -86.3 | 504990 | 230 | -88.4 | 504990 | 195 |
| MR_1774414599_CECCAAEA | 504990 | 725 | -92.9 | 504990 | 10 | -89.1 | 504990 | 230 | -88.0 | 504990 | 195 |
| MR_1774414599_0446D7FB | 504990 | 10 | -87.5 | 504990 | 725 | -91.6 | 504990 | 230 | -88.4 | 504990 | 195 |
| MR_1774414599_4F486F99 | 504990 | 10 | -87.4 | 504990 | 725 | -91.0 | 504990 | 230 | -88.3 | 504990 | 195 |
| MR_1774414599_DD36B0FD | 504990 | 10 | -86.3 | 504990 | 725 | -93.5 | 504990 | 230 | -89.5 | 504990 | 195 |
| MR_1774414599_F5118977 | 504990 | 10 | -88.0 | 504990 | 725 | -90.1 | 504990 | 230 | -85.7 | 504990 | 195 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 791: `0ac0c1be-87c...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `0ac0c1be-87c1-4e1a-8084-d450b74f0ead` |
| Tag | **single-answer** |
| 정답 | **C8** |
| C8 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[791] topology](images/train_0791.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3265310_4
- `C2`: Increase transmission power for 3214573_1
- `C3`: Decrease transmission power for 3214573_1
- `C4`: Decrease A3 Offset threshold for 3214573_1
- `C5`: Press down the tilt angle  of 3214573_1 by 10 degrees
- `C6`: Decrease transmission power for 3265310_4
- `C7`: Lift the tilt angle  of 3214573_1 by 10 degrees
- `C8`: Check test server and transmission issues **← 정답**
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3214573_1
- `C10`: Increase A3 Offset threshold for 3265310_4
- `C11`: Adjust the azimuth of 3265310_4 by 50 degrees
- `C12`: Lift the tilt angle of 3265310_4 by 10 degrees
- `C13`: Insufficient data; more data is needed for judgment.
- `C14`: Increase A3 Offset threshold for 3214573_1
- `C15`: Increase transmission power for 3265310_4
- `C16`: Add neighbor relationship between 3216855_3 and 3214573_1
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3265310_4
- `C18`: Add neighbor relationship between 3265310_4 and 3214573_1
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3265310_4
- `C20`: Adjust the azimuth of 3214573_1 by 25 degrees
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3214573_1
- `C22`: Press down the tilt angle of 3265310_4 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.960 | MS1 | 121.4656693622 | 31.1446289410 | 950 | 504990 | -87.59 | 13.98 | 453.69 | 0.18 | 2.55 | 1569 |
| 2024-09-20 22:21:32.931 | MS1 | 121.4656771451 | 31.1446241528 | 950 | 504990 | -85.34 | 17.17 | 333.45 | 0.12 | 2.48 | 1562 |
| 2024-09-20 22:21:33.926 | MS1 | 121.4656651461 | 31.1446375545 | 950 | 504990 | -86.45 | 15.08 | 493.00 | 0.12 | 2.89 | 1569 |
| 2024-09-20 22:21:34.377 | MS1 | 121.4656743633 | 31.1446214781 | 950 | 504990 | -86.92 | 12.67 | 60.26 | 0.11 | 2.48 | 411 |
| 2024-09-20 22:21:35.693 | MS1 | 121.4656775953 | 31.1446303738 | 950 | 504990 | -89.00 | 12.20 | 68.19 | 0.14 | 2.34 | 481 |
| 2024-09-20 22:21:36.221 | MS1 | 121.4656668805 | 31.1446352257 | 950 | 504990 | -88.32 | 17.19 | 64.28 | 0.02 | 2.31 | 396 |
| 2024-09-20 22:21:37.961 | MS1 | 121.4656584048 | 31.1446368354 | 950 | 504990 | -93.59 | 11.38 | 69.04 | 0.20 | 2.20 | 370 |
| 2024-09-20 22:21:38.635 | MS1 | 121.4656774558 | 31.1446180909 | 950 | 504990 | -93.14 | 12.67 | 60.02 | 0.10 | 2.33 | 390 |
| 2024-09-20 22:21:39.767 | MS1 | 121.4656692612 | 31.1446201614 | 950 | 504990 | -89.07 | 12.96 | 52.81 | 0.11 | 2.55 | 444 |
| 2024-09-20 22:21:40.941 | MS1 | 121.4656585640 | 31.1446225192 | 950 | 504990 | -92.83 | 10.09 | 577.62 | 0.17 | 2.61 | 1575 |
| 2024-09-20 22:21:41.114 | MS1 | 121.4656635794 | 31.1446327120 | 950 | 504990 | -93.64 | 7.96 | 505.62 | 0.02 | 2.02 | 1587 |
| 2024-09-20 22:21:42.456 | MS1 | 121.4656614054 | 31.1446312137 | 950 | 504990 | -90.66 | 7.68 | 317.96 | 0.17 | 2.28 | 1564 |

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
| 3214573 | 1 | 121.4681673745 | 31.1505018570 | 225 | 12 | 11 | 21.5 | TDD | 24 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3216855 | 3 | 121.4708611724 | 31.1496131541 | 254 | 3 | 8 | 22.8 | TDD | 453 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3222705 | 2 | 121.4648295618 | 31.1526548348 | 158 | 8 | 6 | 25.4 | TDD | 145 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3265310 | 4 | 121.4685673648 | 31.1493248322 | 58 | 9 | 3 | 37.5 | TDD | 950 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:31.363 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.513 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.513 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.176 | NREventA3 | measId:2;ServCellPCI:637;Se... |
| 2024-09-20 22:21:38.416 | NRHandoverAttempt | SourcePCI:637;SourceNR-ARFC... |
| 2024-09-20 22:21:38.460 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.475 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.594 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.594 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3214573 | 1 | 13.4387 | 14.8528 | -114.4537 | 9.0596 | 197.0595 | 0.0134 | 0.0104 |
| 2024_09_20 22:00 | 3222705 | 2 | 11.4295 | 12.6298 | -114.0294 | 14.3392 | 141.6747 | 0.0099 | 0.0058 |
| 2024_09_20 22:00 | 3216855 | 3 | 13.9380 | 19.0719 | -114.2799 | 17.8024 | 128.0397 | 0.0199 | 0.0031 |
| 2024_09_20 22:00 | 3265310 | 4 | 11.0311 | 15.6804 | -114.5747 | 12.9222 | 122.8504 | 0.0165 | 0.0145 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415804_BFABD759 | 504990 | 950 | -85.9 | 504990 | 24 | -93.5 | 504990 | 453 | -97.6 | 504990 | 145 |
| MR_1774415804_F76CAC44 | 504990 | 950 | -86.5 | 504990 | 24 | -95.6 | 504990 | 453 | -97.7 | 504990 | 145 |
| MR_1774415804_E5A05074 | 504990 | 950 | -85.8 | 504990 | 24 | -92.5 | 504990 | 453 | -97.5 | 504990 | 145 |
| MR_1774415804_892B3BEE | 504990 | 950 | -87.2 | 504990 | 24 | -94.4 | 504990 | 453 | -95.9 | 504990 | 145 |
| MR_1774415804_CF44931A | 504990 | 950 | -87.7 | 504990 | 24 | -91.9 | 504990 | 453 | -96.1 | 504990 | 145 |
| MR_1774415804_C73A5EBD | 504990 | 950 | -85.5 | 504990 | 24 | -91.7 | 504990 | 453 | -94.5 | 504990 | 145 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 792: `72333785-4f4...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `72333785-4f43-4f23-8b38-b5ec50d4da83` |
| Tag | **multiple-answer** |
| 정답 | **C7|C13** |
| C7 의미 | Increase transmission power for 3240301_2 |
| C13 의미 | Adjust the azimuth of 3240301_2 by 50 degrees |
| 패턴 분류 | **P4 Coverage (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[792] topology](images/train_0792.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3221826_3
- `C2`: Decrease A3 Offset threshold for 3221826_3
- `C3`: Increase transmission power for 3221826_3
- `C4`: Press down the tilt angle  of 3221826_3 by 5 degrees
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3240301_2
- `C6`: Lift the tilt angle of 3240301_2 by 10 degrees
- `C7`: Increase transmission power for 3240301_2 **← 정답**
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3221826_3
- `C9`: Add neighbor relationship between 3240301_2 and 3221826_3
- `C10`: Check test server and transmission issues
- `C11`: Increase A3 Offset threshold for 3221826_3
- `C12`: Decrease A3 Offset threshold for 3240301_2
- `C13`: Adjust the azimuth of 3240301_2 by 50 degrees **← 정답**
- `C14`: Decrease transmission power for 3221826_3
- `C15`: Press down the tilt angle of 3240301_2 by 10 degrees
- `C16`: Increase A3 Offset threshold for 3240301_2
- `C17`: Insufficient data; more data is needed for judgment.
- `C18`: Lift the tilt angle  of 3221826_3 by 5 degrees
- `C19`: Add neighbor relationship between 3212480_4 and 3221826_3
- `C20`: Decrease transmission power for 3240301_2
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3240301_2
- `C22`: Adjust the azimuth of 3221826_3 by 20 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.269 | MS1 | 121.4656740017 | 31.1446345911 | 843 | 504990 | -85.48 | 17.11 | 476.89 | 0.11 | 2.52 | 1560 |
| 2024-09-20 22:21:32.119 | MS1 | 121.4656738534 | 31.1446313344 | 843 | 504990 | -87.37 | 16.63 | 452.67 | 0.06 | 2.83 | 1571 |
| 2024-09-20 22:21:33.497 | MS1 | 121.4656762801 | 31.1446338601 | 843 | 504990 | -88.79 | 15.70 | 514.73 | 0.06 | 2.65 | 1575 |
| 2024-09-20 22:21:34.152 | MS1 | 121.4656726896 | 31.1446271902 | 843 | 504990 | -107.54 | -0.45 | 47.31 | 0.18 | 1.14 | 1593 |
| 2024-09-20 22:21:35.249 | MS1 | 121.4656755024 | 31.1446209446 | 843 | 504990 | -109.60 | 0.80 | 43.08 | 0.18 | 1.26 | 1580 |
| 2024-09-20 22:21:36.439 | MS1 | 121.4656711494 | 31.1446249832 | 843 | 504990 | -104.88 | 0.56 | 68.86 | 0.13 | 1.20 | 1580 |
| 2024-09-20 22:21:37.122 | MS1 | 121.4656715529 | 31.1446364446 | 843 | 504990 | -107.30 | -1.73 | 62.36 | 0.08 | 1.41 | 1596 |
| 2024-09-20 22:21:38.949 | MS1 | 121.4656777749 | 31.1446342272 | 843 | 504990 | -107.14 | 0.45 | 20.69 | 0.08 | 1.37 | 1597 |
| 2024-09-20 22:21:39.284 | MS1 | 121.4656736976 | 31.1446257921 | 843 | 504990 | -107.58 | 1.30 | 54.02 | 0.19 | 1.28 | 1599 |
| 2024-09-20 22:21:40.487 | MS1 | 121.4656696076 | 31.1446323059 | 843 | 504990 | -88.64 | 16.49 | 339.39 | 0.02 | 2.64 | 1568 |
| 2024-09-20 22:21:41.191 | MS1 | 121.4656593839 | 31.1446373419 | 843 | 504990 | -92.84 | 12.07 | 370.65 | 0.11 | 2.34 | 1573 |
| 2024-09-20 22:21:42.987 | MS1 | 121.4656711922 | 31.1446252531 | 843 | 504990 | -92.40 | 16.54 | 409.41 | 0.08 | 2.94 | 1592 |

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
| 3212480 | 4 | 121.4703126189 | 31.1553405787 | 197 | 8 | 1 | 42.6 | TDD | 317 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3221826 | 3 | 121.4759801233 | 31.1527933285 | 247 | 3 | 6 | 43.0 | TDD | 852 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3240301 | 2 | 121.4657018185 | 31.1452587379 | 117 | 2 | 6 | 15.4 | TDD | 843 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3256472 | 1 | 121.4642712602 | 31.1475465737 | 338 | 9 | 2 | 22.6 | TDD | 209 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |

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
| 2024-09-20 22:21:31.262 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.281 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.400 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.400 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.563 | NREventA2 | measId:1;ServCellPCI:809;Se... |
| 2024-09-20 22:21:34.694 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3256472 | 1 | 18.0896 | 12.6566 | -116.4738 | 14.5239 | 129.8294 | 0.0169 | 0.0150 |
| 2024_09_20 22:00 | 3240301 | 2 | 19.5412 | 13.4495 | -115.0265 | 8.1246 | 179.0531 | 0.1121 | 0.0060 |
| 2024_09_20 22:00 | 3221826 | 3 | 13.8847 | 16.3051 | -115.7387 | 14.2945 | 162.5978 | 0.0122 | 0.0196 |
| 2024_09_20 22:00 | 3212480 | 4 | 13.3461 | 10.9078 | -116.5131 | 12.0699 | 160.8206 | 0.0062 | 0.0006 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414321_F89D3A11 | 504990 | 843 | -106.9 | 504990 | 852 | -112.5 | 504990 | 317 | -120.2 | 504990 | 209 |
| MR_1774414321_734ABB34 | 504990 | 843 | -109.2 | 504990 | 852 | -115.7 | 504990 | 317 | -120.2 | 504990 | 209 |
| MR_1774414321_0186FEA4 | 504990 | 843 | -108.6 | 504990 | 852 | -114.2 | 504990 | 317 | -120.9 | 504990 | 209 |
| MR_1774414321_1CC1E2B4 | 504990 | 843 | -105.9 | 504990 | 852 | -112.2 | 504990 | 317 | -119.9 | 504990 | 209 |
| MR_1774414321_D3B1A597 | 504990 | 843 | -109.2 | 504990 | 852 | -112.0 | 504990 | 317 | -119.0 | 504990 | 209 |
| MR_1774414321_F0740F8F | 504990 | 843 | -106.4 | 504990 | 852 | -115.1 | 504990 | 317 | -117.5 | 504990 | 209 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 793: `0716500d-ba8...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `0716500d-ba85-41ce-b059-38f74108c7f2` |
| Tag | **single-answer** |
| 정답 | **C16** |
| C16 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3227059_3 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[793] topology](images/train_0793.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3227059_3
- `C2`: Adjust the azimuth of 3227059_3 by 39 degrees
- `C3`: Increase A3 Offset threshold for 3269243_1
- `C4`: Press down the tilt angle  of 3269243_1 by 10 degrees
- `C5`: Check test server and transmission issues
- `C6`: Press down the tilt angle of 3227059_3 by 2 degrees
- `C7`: Decrease transmission power for 3227059_3
- `C8`: Increase A3 Offset threshold for 3227059_3
- `C9`: Decrease transmission power for 3269243_1
- `C10`: Lift the tilt angle  of 3269243_1 by 10 degrees
- `C11`: Insufficient data; more data is needed for judgment.
- `C12`: Decrease A3 Offset threshold for 3269243_1
- `C13`: Add neighbor relationship between 3227059_3 and 3269243_1
- `C14`: Lift the tilt angle of 3227059_3 by 2 degrees
- `C15`: Adjust the azimuth of 3269243_1 by 50 degrees
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3227059_3 **← 정답**
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3269243_1
- `C18`: Increase transmission power for 3269243_1
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3269243_1
- `C20`: Decrease A3 Offset threshold for 3227059_3
- `C21`: Increase transmission power for 3227059_3
- `C22`: Add neighbor relationship between 3231092_2 and 3269243_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.913 | MS1 | 121.4656627598 | 31.1446206376 | 430 | 504990 | -85.75 | 13.90 | 465.55 | 0.04 | 2.45 | 1570 |
| 2024-09-20 22:21:32.105 | MS1 | 121.4656744326 | 31.1446226815 | 430 | 504990 | -87.27 | 13.76 | 335.23 | 0.13 | 2.10 | 1597 |
| 2024-09-20 22:21:33.131 | MS1 | 121.4656754570 | 31.1446310019 | 430 | 504990 | -87.70 | 14.03 | 499.93 | 0.11 | 2.72 | 1586 |
| 2024-09-20 22:21:34.642 | MS1 | 121.4656688425 | 31.1446239541 | 430 | 504990 | -90.64 | 13.76 | 68.83 | 0.56 | 2.86 | 542 |
| 2024-09-20 22:21:35.128 | MS1 | 121.4656739479 | 31.1446296713 | 430 | 504990 | -86.69 | 17.94 | 48.20 | 0.59 | 2.00 | 640 |
| 2024-09-20 22:21:36.930 | MS1 | 121.4656642635 | 31.1446259673 | 430 | 504990 | -91.58 | 13.92 | 94.93 | 0.54 | 2.47 | 577 |
| 2024-09-20 22:21:37.477 | MS1 | 121.4656731762 | 31.1446331045 | 430 | 504990 | -91.18 | 9.58 | 56.93 | 0.53 | 2.22 | 622 |
| 2024-09-20 22:21:38.685 | MS1 | 121.4656668430 | 31.1446211723 | 430 | 504990 | -92.97 | 11.51 | 64.52 | 0.57 | 2.09 | 610 |
| 2024-09-20 22:21:39.951 | MS1 | 121.4656657120 | 31.1446294595 | 430 | 504990 | -93.39 | 10.79 | 72.65 | 0.60 | 2.69 | 682 |
| 2024-09-20 22:21:40.778 | MS1 | 121.4656590726 | 31.1446280981 | 430 | 504990 | -91.74 | 12.57 | 456.71 | 0.05 | 2.79 | 1563 |
| 2024-09-20 22:21:41.121 | MS1 | 121.4656774395 | 31.1446312859 | 430 | 504990 | -93.43 | 9.93 | 537.18 | 0.19 | 2.29 | 1597 |
| 2024-09-20 22:21:42.490 | MS1 | 121.4656613550 | 31.1446225844 | 430 | 504990 | -92.58 | 9.82 | 482.88 | 0.04 | 2.73 | 1595 |

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
| 3227059 | 3 | 121.4654866268 | 31.1551059067 | 218 | 0 | 7 | 31.5 | TDD | 430 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3231092 | 2 | 121.4645708933 | 31.1534151397 | 325 | 15 | 6 | 42.6 | TDD | 692 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3269243 | 1 | 121.4688519156 | 31.1475934946 | 91 | 6 | 4 | 31.2 | TDD | 408 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3271362 | 4 | 121.4651078415 | 31.1531060246 | 124 | 5 | 8 | 41.3 | TDD | 558 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |

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
| 2024-09-20 22:21:31.010 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.029 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.174 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.174 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.874 | NREventA3 | measId:2;ServCellPCI:35;Ser... |
| 2024-09-20 22:21:38.114 | NRHandoverAttempt | SourcePCI:35;SourceNR-ARFCN... |
| 2024-09-20 22:21:38.157 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.167 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.295 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.295 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3269243 | 1 | 16.1144 | 9.9241 | -116.8823 | 9.3766 | 192.1316 | 0.0035 | 0.0041 |
| 2024_09_20 22:00 | 3231092 | 2 | 7.1401 | 11.2976 | -114.4649 | 13.4591 | 175.0008 | 0.0065 | 0.0086 |
| 2024_09_20 22:00 | 3227059 | 3 | 14.3605 | 9.5932 | -116.7739 | 7.9369 | 137.1917 | 0.0110 | 0.0079 |
| 2024_09_20 22:00 | 3271362 | 4 | 7.5410 | 19.3023 | -117.0883 | 16.4260 | 144.2079 | 0.0121 | 0.0024 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413254_0E215C10 | 504990 | 430 | -90.4 | 504990 | 408 | -90.8 | 504990 | 692 | -98.4 | 504990 | 558 |
| MR_1774413254_7F2EF6F1 | 504990 | 430 | -90.3 | 504990 | 408 | -90.5 | 504990 | 692 | -99.0 | 504990 | 558 |
| MR_1774413254_5D89FF74 | 504990 | 430 | -92.2 | 504990 | 408 | -92.8 | 504990 | 692 | -95.2 | 504990 | 558 |
| MR_1774413254_F7393D5E | 504990 | 430 | -91.0 | 504990 | 408 | -90.6 | 504990 | 692 | -96.1 | 504990 | 558 |
| MR_1774413254_D4B03190 | 504990 | 430 | -89.1 | 504990 | 408 | -93.6 | 504990 | 692 | -95.4 | 504990 | 558 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 794: `4ca7eb58-f07...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `4ca7eb58-f07e-4ffa-8db2-da10a6636431` |
| Tag | **single-answer** |
| 정답 | **C2** |
| C2 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3237066_3 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[794] topology](images/train_0794.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3237066_3
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3237066_3 **← 정답**
- `C3`: Add neighbor relationship between 3237066_3 and 3221428_1
- `C4`: Decrease transmission power for 3237066_3
- `C5`: Increase transmission power for 3237066_3
- `C6`: Press down the tilt angle of 3237066_3 by 3 degrees
- `C7`: Adjust the azimuth of 3237066_3 by 23 degrees
- `C8`: Decrease transmission power for 3221428_1
- `C9`: Increase A3 Offset threshold for 3221428_1
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3237066_3
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3221428_1
- `C12`: Lift the tilt angle of 3237066_3 by 3 degrees
- `C13`: Add neighbor relationship between 3261295_4 and 3221428_1
- `C14`: Increase A3 Offset threshold for 3237066_3
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3221428_1
- `C16`: Lift the tilt angle  of 3221428_1 by 10 degrees
- `C17`: Check test server and transmission issues
- `C18`: Press down the tilt angle  of 3221428_1 by 10 degrees
- `C19`: Increase transmission power for 3221428_1
- `C20`: Adjust the azimuth of 3221428_1 by 50 degrees
- `C21`: Decrease A3 Offset threshold for 3221428_1
- `C22`: Insufficient data; more data is needed for judgment.

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.281 | MS1 | 121.4656739677 | 31.1446324071 | 925 | 504990 | -90.89 | 13.14 | 383.14 | 0.16 | 2.73 | 1581 |
| 2024-09-20 22:21:32.535 | MS1 | 121.4656699306 | 31.1446314819 | 925 | 504990 | -86.73 | 14.73 | 601.09 | 0.02 | 2.49 | 1598 |
| 2024-09-20 22:21:33.689 | MS1 | 121.4656661398 | 31.1446280530 | 925 | 504990 | -90.01 | 15.96 | 570.59 | 0.05 | 2.19 | 1578 |
| 2024-09-20 22:21:34.690 | MS1 | 121.4656756336 | 31.1446222696 | 925 | 504990 | -87.39 | 12.08 | 71.81 | 0.60 | 2.13 | 530 |
| 2024-09-20 22:21:35.649 | MS1 | 121.4656693304 | 31.1446315193 | 925 | 504990 | -89.03 | 16.64 | 93.19 | 0.55 | 2.40 | 682 |
| 2024-09-20 22:21:36.394 | MS1 | 121.4656741502 | 31.1446225254 | 925 | 504990 | -85.66 | 13.88 | 55.49 | 0.67 | 2.77 | 665 |
| 2024-09-20 22:21:37.650 | MS1 | 121.4656650934 | 31.1446221587 | 925 | 504990 | -93.27 | 7.63 | 82.84 | 0.58 | 2.43 | 546 |
| 2024-09-20 22:21:38.915 | MS1 | 121.4656585656 | 31.1446375518 | 925 | 504990 | -89.56 | 8.48 | 94.37 | 0.61 | 2.83 | 556 |
| 2024-09-20 22:21:39.122 | MS1 | 121.4656712095 | 31.1446267399 | 925 | 504990 | -92.89 | 8.73 | 96.93 | 0.51 | 2.83 | 616 |
| 2024-09-20 22:21:40.560 | MS1 | 121.4656631281 | 31.1446372034 | 925 | 504990 | -93.44 | 9.69 | 383.11 | 0.17 | 2.55 | 1596 |
| 2024-09-20 22:21:41.284 | MS1 | 121.4656596578 | 31.1446312151 | 925 | 504990 | -90.24 | 8.95 | 469.91 | 0.11 | 2.53 | 1568 |
| 2024-09-20 22:21:42.597 | MS1 | 121.4656732015 | 31.1446272917 | 925 | 504990 | -89.62 | 9.64 | 467.14 | 0.08 | 2.63 | 1564 |

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
| 3221428 | 1 | 121.4658946094 | 31.1549664644 | 131 | 9 | 10 | 46.4 | TDD | 209 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3237066 | 3 | 121.4696968532 | 31.1450219360 | 286 | 1 | 2 | 16.4 | TDD | 925 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3261295 | 4 | 121.4675288980 | 31.1546992261 | 184 | 5 | 12 | 41.6 | TDD | 445 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3278765 | 2 | 121.4654610229 | 31.1521232579 | 101 | 8 | 1 | 19.5 | TDD | 796 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |

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
| 2024-09-20 22:21:30.978 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.000 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.123 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.123 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.851 | NREventA3 | measId:2;ServCellPCI:755;Se... |
| 2024-09-20 22:21:38.091 | NRHandoverAttempt | SourcePCI:755;SourceNR-ARFC... |
| 2024-09-20 22:21:38.131 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.141 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.289 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.289 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3221428 | 1 | 5.8483 | 13.7036 | -114.1295 | 16.4763 | 119.5732 | 0.0185 | 0.0137 |
| 2024_09_20 22:00 | 3278765 | 2 | 10.3567 | 10.2165 | -115.7269 | 7.8089 | 165.7854 | 0.0005 | 0.0143 |
| 2024_09_20 22:00 | 3237066 | 3 | 6.0906 | 14.0684 | -115.6878 | 5.0594 | 187.7741 | 0.0086 | 0.0078 |
| 2024_09_20 22:00 | 3261295 | 4 | 14.7032 | 8.0632 | -117.8888 | 6.8550 | 100.4742 | 0.0139 | 0.0161 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416738_A31D7B0A | 504990 | 925 | -86.1 | 504990 | 209 | -95.3 | 504990 | 445 | -96.4 | 504990 | 796 |
| MR_1774416738_90F57220 | 504990 | 925 | -86.6 | 504990 | 209 | -94.0 | 504990 | 445 | -95.4 | 504990 | 796 |
| MR_1774416738_213E6179 | 504990 | 925 | -87.0 | 504990 | 209 | -94.9 | 504990 | 445 | -98.3 | 504990 | 796 |
| MR_1774416738_6F5049C3 | 504990 | 925 | -88.7 | 504990 | 209 | -96.5 | 504990 | 445 | -97.8 | 504990 | 796 |
| MR_1774416738_81366BF6 | 504990 | 925 | -86.2 | 504990 | 209 | -96.7 | 504990 | 445 | -97.6 | 504990 | 796 |
| MR_1774416738_8047496B | 504990 | 925 | -88.5 | 504990 | 209 | -95.6 | 504990 | 445 | -98.2 | 504990 | 796 |
| MR_1774416738_88F2A272 | 504990 | 925 | -86.9 | 504990 | 209 | -95.3 | 504990 | 445 | -94.5 | 504990 | 796 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 795: `bf138cbf-70a...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `bf138cbf-70a0-4177-8a34-31e57267d4a3` |
| Tag | **single-answer** |
| 정답 | **C16** |
| C16 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[795] topology](images/train_0795.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle  of 3217432_3 by 10 degrees
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3217432_3
- `C3`: Decrease transmission power for 3218727_2
- `C4`: Increase transmission power for 3218727_2
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3218727_2
- `C6`: Adjust the azimuth of 3218727_2 by 24 degrees
- `C7`: Increase A3 Offset threshold for 3217432_3
- `C8`: Decrease transmission power for 3217432_3
- `C9`: Press down the tilt angle  of 3217432_3 by 10 degrees
- `C10`: Add neighbor relationship between 3218727_2 and 3217432_3
- `C11`: Lift the tilt angle of 3218727_2 by 10 degrees
- `C12`: Press down the tilt angle of 3218727_2 by 10 degrees
- `C13`: Add neighbor relationship between 3232178_4 and 3217432_3
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3218727_2
- `C15`: Increase A3 Offset threshold for 3218727_2
- `C16`: Check test server and transmission issues **← 정답**
- `C17`: Increase transmission power for 3217432_3
- `C18`: Insufficient data; more data is needed for judgment.
- `C19`: Decrease A3 Offset threshold for 3217432_3
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3217432_3
- `C21`: Decrease A3 Offset threshold for 3218727_2
- `C22`: Adjust the azimuth of 3217432_3 by 50 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.972 | MS1 | 121.4656642319 | 31.1446326490 | 570 | 504990 | -89.64 | 17.91 | 303.29 | 0.08 | 2.03 | 1562 |
| 2024-09-20 22:21:32.681 | MS1 | 121.4656758072 | 31.1446231648 | 570 | 504990 | -87.11 | 15.72 | 557.14 | 0.11 | 2.93 | 1597 |
| 2024-09-20 22:21:33.959 | MS1 | 121.4656707965 | 31.1446247698 | 570 | 504990 | -85.67 | 14.13 | 586.59 | 0.13 | 2.05 | 1576 |
| 2024-09-20 22:21:34.666 | MS1 | 121.4656757149 | 31.1446276723 | 570 | 504990 | -86.67 | 16.43 | 68.00 | 0.11 | 2.88 | 310 |
| 2024-09-20 22:21:35.812 | MS1 | 121.4656674046 | 31.1446196372 | 570 | 504990 | -89.25 | 17.30 | 55.08 | 0.02 | 2.07 | 379 |
| 2024-09-20 22:21:36.698 | MS1 | 121.4656753075 | 31.1446228169 | 570 | 504990 | -90.09 | 17.75 | 85.76 | 0.10 | 2.49 | 379 |
| 2024-09-20 22:21:37.366 | MS1 | 121.4656683745 | 31.1446368910 | 570 | 504990 | -93.94 | 9.04 | 59.27 | 0.01 | 2.32 | 358 |
| 2024-09-20 22:21:38.419 | MS1 | 121.4656613211 | 31.1446308271 | 570 | 504990 | -89.28 | 10.98 | 57.40 | 0.19 | 2.58 | 440 |
| 2024-09-20 22:21:39.714 | MS1 | 121.4656658028 | 31.1446369546 | 570 | 504990 | -90.25 | 11.21 | 83.84 | 0.09 | 2.22 | 308 |
| 2024-09-20 22:21:40.853 | MS1 | 121.4656718177 | 31.1446182095 | 570 | 504990 | -93.96 | 12.25 | 439.81 | 0.08 | 2.04 | 1569 |
| 2024-09-20 22:21:41.835 | MS1 | 121.4656596048 | 31.1446198808 | 570 | 504990 | -92.91 | 10.57 | 530.96 | 0.06 | 2.28 | 1588 |
| 2024-09-20 22:21:42.827 | MS1 | 121.4656632244 | 31.1446350621 | 570 | 504990 | -92.37 | 9.66 | 553.18 | 0.12 | 2.47 | 1600 |

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
| 3217432 | 3 | 121.4755377552 | 31.1505094645 | 326 | 12 | 8 | 30.2 | TDD | 973 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3218727 | 2 | 121.4675182412 | 31.1536664680 | 166 | 14 | 4 | 22.8 | TDD | 570 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3232178 | 4 | 121.4727751505 | 31.1452442758 | 244 | 1 | 12 | 17.8 | TDD | 271 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3257278 | 1 | 121.4753977757 | 31.1533447656 | 49 | 15 | 11 | 41.0 | TDD | 777 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |

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
| 2024-09-20 22:21:31.139 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.162 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.293 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.293 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.940 | NREventA3 | measId:2;ServCellPCI:574;Se... |
| 2024-09-20 22:21:38.180 | NRHandoverAttempt | SourcePCI:574;SourceNR-ARFC... |
| 2024-09-20 22:21:38.213 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.226 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.332 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.332 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3257278 | 1 | 12.5441 | 5.9538 | -116.4684 | 12.7436 | 87.5993 | 0.0142 | 0.0081 |
| 2024_09_20 22:00 | 3218727 | 2 | 6.0731 | 8.0260 | -117.4668 | 12.3995 | 171.2515 | 0.0183 | 0.0010 |
| 2024_09_20 22:00 | 3217432 | 3 | 16.5634 | 11.4035 | -114.8113 | 6.6822 | 172.5265 | 0.0035 | 0.0006 |
| 2024_09_20 22:00 | 3232178 | 4 | 14.4513 | 19.2142 | -115.1639 | 16.7385 | 132.5787 | 0.0082 | 0.0036 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417167_AE1C7D48 | 504990 | 570 | -88.1 | 504990 | 973 | -90.1 | 504990 | 271 | -93.6 | 504990 | 777 |
| MR_1774417167_6F4D9944 | 504990 | 570 | -85.4 | 504990 | 973 | -89.6 | 504990 | 271 | -95.0 | 504990 | 777 |
| MR_1774417167_38FB13E8 | 504990 | 570 | -85.3 | 504990 | 973 | -90.0 | 504990 | 271 | -92.8 | 504990 | 777 |
| MR_1774417167_49DB50C6 | 504990 | 570 | -88.2 | 504990 | 973 | -90.9 | 504990 | 271 | -95.6 | 504990 | 777 |
| MR_1774417167_DE3984E2 | 504990 | 570 | -87.9 | 504990 | 973 | -90.4 | 504990 | 271 | -95.0 | 504990 | 777 |
| MR_1774417167_8BE8ED68 | 504990 | 570 | -87.9 | 504990 | 973 | -88.9 | 504990 | 271 | -95.7 | 504990 | 777 |
| MR_1774417167_1DD04CD6 | 504990 | 570 | -85.9 | 504990 | 973 | -89.5 | 504990 | 271 | -95.7 | 504990 | 777 |
| MR_1774417167_2B8AACAD | 504990 | 570 | -87.5 | 504990 | 973 | -90.4 | 504990 | 271 | -92.5 | 504990 | 777 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 796: `473a49ab-e35...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `473a49ab-e35e-41db-951c-bd21f3bae539` |
| Tag | **single-answer** |
| 정답 | **C18** |
| C18 의미 | Lift the tilt angle  of 3215649_2 by 5 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[796] topology](images/train_0796.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3219952_4
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3219952_4
- `C3`: Increase A3 Offset threshold for 3219952_4
- `C4`: Press down the tilt angle of 3219952_4 by 5 degrees
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3236322_1
- `C6`: Insufficient data; more data is needed for judgment.
- `C7`: Adjust the azimuth of 3219952_4 by 26 degrees
- `C8`: Decrease transmission power for 3236322_1
- `C9`: Add neighbor relationship between 3215649_2 and 3236322_1
- `C10`: Press down the tilt angle  of 3215649_2 by 5 degrees
- `C11`: Increase transmission power for 3236322_1
- `C12`: Add neighbor relationship between 3219952_4 and 3236322_1
- `C13`: Decrease A3 Offset threshold for 3219952_4
- `C14`: Check test server and transmission issues
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3236322_1
- `C16`: Decrease A3 Offset threshold for 3236322_1
- `C17`: Adjust the azimuth of 3215649_2 by 50 degrees
- `C18`: Lift the tilt angle  of 3215649_2 by 5 degrees **← 정답**
- `C19`: Decrease transmission power for 3219952_4
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3219952_4
- `C21`: Lift the tilt angle of 3219952_4 by 5 degrees
- `C22`: Increase A3 Offset threshold for 3236322_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.266 | MS1 | 121.4656617458 | 31.1446337798 | 94 | 504990 | -90.65 | 14.46 | 491.66 | 0.14 | 2.01 | 1584 |
| 2024-09-20 22:21:32.364 | MS1 | 121.4656595776 | 31.1446277814 | 94 | 504990 | -85.81 | 12.56 | 550.77 | 0.04 | 2.50 | 1576 |
| 2024-09-20 22:21:33.806 | MS1 | 121.4656632874 | 31.1446318032 | 94 | 504990 | -86.21 | 15.43 | 593.34 | 0.15 | 2.04 | 1567 |
| 2024-09-20 22:21:34.139 | MS1 | 121.4656629136 | 31.1446292807 | 94 | 504990 | -91.21 | 17.53 | 78.48 | 0.01 | 2.14 | 1580 |
| 2024-09-20 22:21:35.202 | MS1 | 121.4656645549 | 31.1446218152 | 94 | 504990 | -89.04 | 16.66 | 80.36 | 0.19 | 2.50 | 1567 |
| 2024-09-20 22:21:36.921 | MS1 | 121.4656657795 | 31.1446317799 | 94 | 504990 | -87.17 | 17.24 | 77.56 | 0.09 | 2.19 | 1585 |
| 2024-09-20 22:21:37.778 | MS1 | 121.4656732948 | 31.1446273234 | 94 | 504990 | -89.06 | 8.87 | 79.51 | 0.06 | 2.58 | 1594 |
| 2024-09-20 22:21:38.589 | MS1 | 121.4656614273 | 31.1446194246 | 94 | 504990 | -93.65 | 9.80 | 98.33 | 0.03 | 2.07 | 1586 |
| 2024-09-20 22:21:39.944 | MS1 | 121.4656701269 | 31.1446363881 | 94 | 504990 | -89.91 | 11.64 | 96.24 | 0.19 | 2.17 | 1576 |
| 2024-09-20 22:21:40.232 | MS1 | 121.4656593736 | 31.1446222349 | 94 | 504990 | -89.43 | 10.33 | 320.72 | 0.01 | 2.65 | 1600 |
| 2024-09-20 22:21:41.765 | MS1 | 121.4656664312 | 31.1446237436 | 94 | 504990 | -89.39 | 9.23 | 549.53 | 0.02 | 2.79 | 1587 |
| 2024-09-20 22:21:42.977 | MS1 | 121.4656653147 | 31.1446194610 | 94 | 504990 | -93.03 | 7.19 | 482.74 | 0.04 | 2.15 | 1585 |

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
| 3215649 | 2 | 121.4650621495 | 31.1483541930 | 37 | 15 | 10 | 23.2 | TDD | 594 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3219952 | 4 | 121.4702869219 | 31.1449364974 | 240 | 2 | 6 | 25.4 | TDD | 94 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3234822 | 3 | 121.4731435608 | 31.1475620606 | 9 | 0 | 3 | 43.7 | TDD | 812 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3236322 | 1 | 121.4739315763 | 31.1555688193 | 121 | 4 | 7 | 29.9 | TDD | 25 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |

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
| 2024-09-20 22:21:31.316 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.431 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.431 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.142 | NREventA3 | measId:2;ServCellPCI:720;Se... |
| 2024-09-20 22:21:38.382 | NRHandoverAttempt | SourcePCI:720;SourceNR-ARFC... |
| 2024-09-20 22:21:38.424 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.438 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.584 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.584 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3236322 | 1 | 6.0080 | 7.4564 | -114.1376 | 14.7408 | 166.6799 | 0.0154 | 0.0079 |
| 2024_09_20 22:00 | 3215649 | 2 | 19.7976 | 19.7376 | -117.0861 | 16.3259 | 117.5620 | 0.0086 | 0.0073 |
| 2024_09_20 22:00 | 3234822 | 3 | 6.6227 | 9.5888 | -116.6790 | 11.5579 | 192.9882 | 0.0112 | 0.0184 |
| 2024_09_20 22:00 | 3219952 | 4 | 83.1220 | 82.0342 | -115.8950 | 10.0420 | 191.4432 | 0.0148 | 0.0195 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413707_44677EEF | 504990 | 94 | -92.1 | 504990 | 25 | -93.6 | 504990 | 594 | -102.7 | 504990 | 812 |
| MR_1774413707_6B37246A | 504990 | 94 | -92.1 | 504990 | 25 | -96.1 | 504990 | 594 | -104.1 | 504990 | 812 |
| MR_1774413707_FA0DD39D | 504990 | 94 | -89.6 | 504990 | 25 | -96.7 | 504990 | 594 | -101.7 | 504990 | 812 |
| MR_1774413707_FC3805AB | 504990 | 94 | -92.8 | 504990 | 25 | -95.0 | 504990 | 594 | -102.8 | 504990 | 812 |
| MR_1774413707_7D038B15 | 504990 | 94 | -91.1 | 504990 | 25 | -95.8 | 504990 | 594 | -105.0 | 504990 | 812 |
| MR_1774413707_7C078FB7 | 504990 | 94 | -90.7 | 504990 | 25 | -96.0 | 504990 | 594 | -104.9 | 504990 | 812 |
| MR_1774413707_87443F66 | 504990 | 94 | -89.2 | 504990 | 25 | -96.5 | 504990 | 594 | -104.6 | 504990 | 812 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 797: `e7234bdb-303...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `e7234bdb-3039-4723-84b0-ab9e7d83403d` |
| Tag | **single-answer** |
| 정답 | **C7** |
| C7 의미 | Add neighbor relationship between 3230637_2 and 3264872_1 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[797] topology](images/train_0797.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3264872_1
- `C2`: Press down the tilt angle  of 3264872_1 by 4 degrees
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3230637_2
- `C4`: Insufficient data; more data is needed for judgment.
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3264872_1
- `C6`: Decrease transmission power for 3264872_1
- `C7`: Add neighbor relationship between 3230637_2 and 3264872_1 **← 정답**
- `C8`: Decrease transmission power for 3230637_2
- `C9`: Increase A3 Offset threshold for 3230637_2
- `C10`: Adjust the azimuth of 3230637_2 by 50 degrees
- `C11`: Decrease A3 Offset threshold for 3264872_1
- `C12`: Decrease A3 Offset threshold for 3230637_2
- `C13`: Lift the tilt angle of 3230637_2 by 10 degrees
- `C14`: Increase A3 Offset threshold for 3264872_1
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3264872_1
- `C16`: Adjust the azimuth of 3264872_1 by 6 degrees
- `C17`: Check test server and transmission issues
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3230637_2
- `C19`: Lift the tilt angle  of 3264872_1 by 4 degrees
- `C20`: Increase transmission power for 3230637_2
- `C21`: Add neighbor relationship between 3246622_4 and 3264872_1
- `C22`: Press down the tilt angle of 3230637_2 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.231 | MS1 | 121.4656710136 | 31.1446294806 | 467 | 504990 | -83.20 | 13.54 | 303.08 | 0.16 | 2.95 | 1562 |
| 2024-09-20 22:21:32.100 | MS1 | 121.4656659370 | 31.1446186251 | 467 | 504990 | -84.83 | 13.81 | 559.42 | 0.09 | 2.21 | 1600 |
| 2024-09-20 22:21:33.734 | MS1 | 121.4656731401 | 31.1446337176 | 467 | 504990 | -81.87 | 14.56 | 303.37 | 0.15 | 2.18 | 1599 |
| 2024-09-20 22:21:34.451 | MS1 | 121.4656724708 | 31.1446254056 | 467 | 504990 | -85.82 | -3.41 | 48.15 | 0.04 | 1.06 | 1571 |
| 2024-09-20 22:21:35.742 | MS1 | 121.4656653263 | 31.1446329893 | 467 | 504990 | -85.40 | -1.67 | 63.69 | 0.05 | 1.24 | 1596 |
| 2024-09-20 22:21:36.489 | MS1 | 121.4656607787 | 31.1446260246 | 467 | 504990 | -93.42 | -1.93 | 49.35 | 0.17 | 1.14 | 1574 |
| 2024-09-20 22:21:37.252 | MS1 | 121.4656776139 | 31.1446191971 | 467 | 504990 | -86.71 | -3.35 | 74.03 | 0.18 | 1.35 | 1581 |
| 2024-09-20 22:21:38.980 | MS1 | 121.4656583705 | 31.1446256628 | 467 | 504990 | -75.98 | 15.46 | 522.51 | 0.20 | 1.01 | 1584 |
| 2024-09-20 22:21:39.267 | MS1 | 121.4656659415 | 31.1446302150 | 467 | 504990 | -76.78 | 15.48 | 361.40 | 0.17 | 1.40 | 1567 |
| 2024-09-20 22:21:40.681 | MS1 | 121.4656672569 | 31.1446237442 | 467 | 504990 | -84.09 | 16.63 | 432.74 | 0.02 | 2.23 | 1582 |
| 2024-09-20 22:21:41.896 | MS1 | 121.4656586143 | 31.1446209159 | 467 | 504990 | -83.23 | 13.53 | 589.79 | 0.08 | 2.94 | 1585 |
| 2024-09-20 22:21:42.367 | MS1 | 121.4656758578 | 31.1446183967 | 467 | 504990 | -79.28 | 14.32 | 556.84 | 0.01 | 2.62 | 1570 |

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
| 3230637 | 2 | 121.4698555348 | 31.1450454351 | 83 | 11 | 7 | 41.7 | TDD | 467 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3246622 | 4 | 121.4697604233 | 31.1553217495 | 178 | 7 | 8 | 28.6 | TDD | 663 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3255778 | 3 | 121.4759753025 | 31.1531738137 | 206 | 4 | 3 | 48.8 | TDD | 118 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3264872 | 1 | 121.4716790668 | 31.1470513679 | 239 | 0 | 9 | 47.5 | TDD | 832 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |

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
| 2024-09-20 22:21:30.990 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.117 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.117 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.789 | NREventA3 | measId:2;ServCellPCI:986;Se... |
| 2024-09-20 22:21:35.789 | NREventA3 | measId:2;ServCellPCI:986;Se... |
| 2024-09-20 22:21:36.789 | NREventA3 | measId:2;ServCellPCI:986;Se... |
| 2024-09-20 22:21:39.289 | NRRRCReestablishAttempt | PCI:986 |
| 2024-09-20 22:21:39.302 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.317 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:39.445 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.445 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3264872 | 1 | 11.7565 | 11.1992 | -116.9238 | 17.0824 | 99.9655 | 0.0141 | 0.0182 |
| 2024_09_20 22:00 | 3230637 | 2 | 5.4207 | 19.6346 | -115.7987 | 15.7622 | 122.1506 | 0.0025 | 0.1319 |
| 2024_09_20 22:00 | 3255778 | 3 | 17.3239 | 6.0936 | -117.0416 | 5.4824 | 133.0466 | 0.0168 | 0.0163 |
| 2024_09_20 22:00 | 3246622 | 4 | 6.5144 | 7.9614 | -116.0873 | 16.4720 | 112.1800 | 0.0106 | 0.0123 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412741_508390D2 | 504990 | 832 | -81.7 | 504990 | 467 | -85.0 | 504990 | 663 | -88.5 | 504990 | 118 |
| MR_1774412741_F5171527 | 504990 | 467 | -85.3 | 504990 | 832 | -80.4 | 504990 | 663 | -91.1 | 504990 | 118 |
| MR_1774412741_2F5B2F0C | 504990 | 467 | -86.3 | 504990 | 832 | -80.0 | 504990 | 663 | -88.3 | 504990 | 118 |
| MR_1774412741_CBB3BDF3 | 504990 | 832 | -82.3 | 504990 | 467 | -85.4 | 504990 | 663 | -90.6 | 504990 | 118 |
| MR_1774412741_52593112 | 504990 | 832 | -81.2 | 504990 | 467 | -84.1 | 504990 | 663 | -89.8 | 504990 | 118 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 798: `2aa0f8fc-9db...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `2aa0f8fc-9db4-48a4-a951-3b905c390b61` |
| Tag | **single-answer** |
| 정답 | **C7** |
| C7 의미 | Add neighbor relationship between 3248410_3 and 3244277_4 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[798] topology](images/train_0798.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3248410_3 by 50 degrees
- `C2`: Decrease transmission power for 3244277_4
- `C3`: Press down the tilt angle of 3248410_3 by 10 degrees
- `C4`: Increase transmission power for 3248410_3
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3248410_3
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3248410_3
- `C7`: Add neighbor relationship between 3248410_3 and 3244277_4 **← 정답**
- `C8`: Press down the tilt angle  of 3244277_4 by 6 degrees
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3244277_4
- `C10`: Increase A3 Offset threshold for 3248410_3
- `C11`: Add neighbor relationship between 3234134_1 and 3244277_4
- `C12`: Increase transmission power for 3244277_4
- `C13`: Check test server and transmission issues
- `C14`: Decrease transmission power for 3248410_3
- `C15`: Decrease A3 Offset threshold for 3248410_3
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3244277_4
- `C17`: Insufficient data; more data is needed for judgment.
- `C18`: Increase A3 Offset threshold for 3244277_4
- `C19`: Lift the tilt angle  of 3244277_4 by 6 degrees
- `C20`: Decrease A3 Offset threshold for 3244277_4
- `C21`: Lift the tilt angle of 3248410_3 by 10 degrees
- `C22`: Adjust the azimuth of 3244277_4 by 3 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.667 | MS1 | 121.4656779447 | 31.1446271612 | 875 | 504990 | -84.22 | 16.02 | 408.22 | 0.16 | 2.92 | 1572 |
| 2024-09-20 22:21:32.149 | MS1 | 121.4656644163 | 31.1446296353 | 875 | 504990 | -76.29 | 12.12 | 348.17 | 0.12 | 2.43 | 1564 |
| 2024-09-20 22:21:33.180 | MS1 | 121.4656635726 | 31.1446205968 | 875 | 504990 | -77.53 | 13.28 | 486.17 | 0.13 | 2.45 | 1568 |
| 2024-09-20 22:21:34.512 | MS1 | 121.4656703113 | 31.1446350166 | 875 | 504990 | -87.91 | -2.40 | 61.01 | 0.11 | 1.30 | 1589 |
| 2024-09-20 22:21:35.712 | MS1 | 121.4656666434 | 31.1446375271 | 875 | 504990 | -91.54 | -3.48 | 73.68 | 0.17 | 1.21 | 1577 |
| 2024-09-20 22:21:36.459 | MS1 | 121.4656753094 | 31.1446223794 | 875 | 504990 | -94.52 | -1.70 | 64.03 | 0.02 | 1.10 | 1585 |
| 2024-09-20 22:21:37.103 | MS1 | 121.4656776478 | 31.1446208672 | 875 | 504990 | -87.61 | -3.96 | 65.66 | 0.13 | 1.19 | 1598 |
| 2024-09-20 22:21:38.421 | MS1 | 121.4656636281 | 31.1446212650 | 875 | 504990 | -77.41 | 17.41 | 546.44 | 0.06 | 1.20 | 1590 |
| 2024-09-20 22:21:39.352 | MS1 | 121.4656607403 | 31.1446278286 | 875 | 504990 | -79.77 | 15.74 | 554.86 | 0.15 | 1.47 | 1590 |
| 2024-09-20 22:21:40.789 | MS1 | 121.4656589079 | 31.1446192223 | 875 | 504990 | -75.79 | 14.09 | 460.80 | 0.15 | 2.67 | 1575 |
| 2024-09-20 22:21:41.347 | MS1 | 121.4656582395 | 31.1446318144 | 875 | 504990 | -82.21 | 14.65 | 455.04 | 0.10 | 2.79 | 1578 |
| 2024-09-20 22:21:42.578 | MS1 | 121.4656751492 | 31.1446198251 | 875 | 504990 | -81.35 | 14.23 | 576.07 | 0.08 | 2.80 | 1570 |

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
| 3224491 | 2 | 121.4721777831 | 31.1441598434 | 58 | 7 | 7 | 45.3 | TDD | 418 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3234134 | 1 | 121.4707480381 | 31.1481964547 | 48 | 11 | 7 | 25.0 | TDD | 289 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3244277 | 4 | 121.4730236009 | 31.1492918000 | 237 | 4 | 0 | 28.4 | TDD | 630 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3248410 | 3 | 121.4688182749 | 31.1551051010 | 334 | 12 | 12 | 19.2 | TDD | 875 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |

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
| 2024-09-20 22:21:31.058 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.074 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.214 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.214 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.941 | NREventA3 | measId:2;ServCellPCI:935;Se... |
| 2024-09-20 22:21:35.941 | NREventA3 | measId:2;ServCellPCI:935;Se... |
| 2024-09-20 22:21:36.941 | NREventA3 | measId:2;ServCellPCI:935;Se... |
| 2024-09-20 22:21:39.441 | NRRRCReestablishAttempt | PCI:935 |
| 2024-09-20 22:21:39.452 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.464 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:39.596 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.596 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3234134 | 1 | 8.0274 | 12.9390 | -117.7176 | 7.7187 | 101.5201 | 0.0096 | 0.0028 |
| 2024_09_20 22:00 | 3224491 | 2 | 17.7218 | 13.4630 | -114.1758 | 7.3067 | 160.9930 | 0.0038 | 0.0156 |
| 2024_09_20 22:00 | 3248410 | 3 | 13.3010 | 17.2109 | -114.6744 | 10.5297 | 157.5284 | 0.0081 | 0.1925 |
| 2024_09_20 22:00 | 3244277 | 4 | 16.1121 | 7.7205 | -116.6310 | 14.6961 | 172.5382 | 0.0166 | 0.0168 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416549_483E09F2 | 504990 | 630 | -81.7 | 504990 | 875 | -89.1 | 504990 | 289 | -87.1 | 504990 | 418 |
| MR_1774416549_331230FA | 504990 | 875 | -89.1 | 504990 | 630 | -82.4 | 504990 | 289 | -86.7 | 504990 | 418 |
| MR_1774416549_1741B798 | 504990 | 875 | -88.0 | 504990 | 630 | -81.4 | 504990 | 289 | -87.4 | 504990 | 418 |
| MR_1774416549_AC81CD34 | 504990 | 875 | -86.1 | 504990 | 630 | -84.3 | 504990 | 289 | -85.1 | 504990 | 418 |
| MR_1774416549_1446A1AF | 504990 | 875 | -87.8 | 504990 | 630 | -84.4 | 504990 | 289 | -84.3 | 504990 | 418 |
| MR_1774416549_B2F67411 | 504990 | 875 | -86.9 | 504990 | 630 | -81.8 | 504990 | 289 | -84.4 | 504990 | 418 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 799: `8a9604f8-d40...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `8a9604f8-d40d-4950-b703-9f531d6b3b5f` |
| Tag | **single-answer** |
| 정답 | **C14** |
| C14 의미 | Lift the tilt angle  of 3274153_1 by 7 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[799] topology](images/train_0799.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3274095_2 by 1 degrees
- `C2`: Decrease transmission power for 3274095_2
- `C3`: Press down the tilt angle of 3274095_2 by 1 degrees
- `C4`: Increase transmission power for 3266585_3
- `C5`: Increase A3 Offset threshold for 3274095_2
- `C6`: Decrease A3 Offset threshold for 3266585_3
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3274095_2
- `C8`: Adjust the azimuth of 3274095_2 by 16 degrees
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3274095_2
- `C10`: Decrease A3 Offset threshold for 3274095_2
- `C11`: Add neighbor relationship between 3274095_2 and 3266585_3
- `C12`: Decrease transmission power for 3266585_3
- `C13`: Increase A3 Offset threshold for 3266585_3
- `C14`: Lift the tilt angle  of 3274153_1 by 7 degrees **← 정답**
- `C15`: Add neighbor relationship between 3274153_1 and 3266585_3
- `C16`: Insufficient data; more data is needed for judgment.
- `C17`: Check test server and transmission issues
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3266585_3
- `C19`: Adjust the azimuth of 3274153_1 by 50 degrees
- `C20`: Increase transmission power for 3274095_2
- `C21`: Press down the tilt angle  of 3274153_1 by 7 degrees
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3266585_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.180 | MS1 | 121.4656659654 | 31.1446371882 | 940 | 504990 | -86.07 | 15.13 | 314.85 | 0.17 | 2.11 | 1583 |
| 2024-09-20 22:21:32.148 | MS1 | 121.4656748616 | 31.1446221263 | 940 | 504990 | -89.92 | 15.87 | 415.33 | 0.04 | 2.38 | 1569 |
| 2024-09-20 22:21:33.349 | MS1 | 121.4656767225 | 31.1446210536 | 940 | 504990 | -87.26 | 16.08 | 536.18 | 0.18 | 2.51 | 1562 |
| 2024-09-20 22:21:34.671 | MS1 | 121.4656607384 | 31.1446291891 | 940 | 504990 | -87.72 | 17.20 | 92.94 | 0.07 | 2.50 | 1590 |
| 2024-09-20 22:21:35.144 | MS1 | 121.4656602777 | 31.1446184207 | 940 | 504990 | -91.73 | 17.84 | 87.24 | 0.17 | 2.38 | 1575 |
| 2024-09-20 22:21:36.217 | MS1 | 121.4656623973 | 31.1446303810 | 940 | 504990 | -86.45 | 16.15 | 68.06 | 0.12 | 2.71 | 1592 |
| 2024-09-20 22:21:37.427 | MS1 | 121.4656601907 | 31.1446294423 | 940 | 504990 | -91.91 | 11.89 | 65.14 | 0.08 | 2.51 | 1594 |
| 2024-09-20 22:21:38.431 | MS1 | 121.4656634615 | 31.1446305018 | 940 | 504990 | -91.53 | 11.93 | 56.63 | 0.01 | 2.56 | 1562 |
| 2024-09-20 22:21:39.983 | MS1 | 121.4656681607 | 31.1446222991 | 940 | 504990 | -92.45 | 12.45 | 69.34 | 0.14 | 2.64 | 1580 |
| 2024-09-20 22:21:40.301 | MS1 | 121.4656772762 | 31.1446190301 | 940 | 504990 | -89.13 | 12.24 | 577.83 | 0.20 | 2.96 | 1579 |
| 2024-09-20 22:21:41.758 | MS1 | 121.4656697044 | 31.1446298480 | 940 | 504990 | -89.26 | 7.84 | 386.95 | 0.19 | 2.14 | 1566 |
| 2024-09-20 22:21:42.388 | MS1 | 121.4656640896 | 31.1446275651 | 940 | 504990 | -93.64 | 8.97 | 599.53 | 0.07 | 2.53 | 1588 |

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
| 3234673 | 4 | 121.4708631863 | 31.1506636081 | 172 | 3 | 7 | 47.2 | TDD | 341 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3266585 | 3 | 121.4678990328 | 31.1553344745 | 54 | 6 | 3 | 21.5 | TDD | 444 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3274095 | 2 | 121.4757211724 | 31.1520379371 | 213 | 0 | 2 | 21.6 | TDD | 940 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3274153 | 1 | 121.4692478064 | 31.1456225391 | 45 | 13 | 8 | 46.5 | TDD | 265 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |

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
| 2024-09-20 22:21:31.644 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.792 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.792 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.467 | NREventA3 | measId:2;ServCellPCI:156;Se... |
| 2024-09-20 22:21:38.707 | NRHandoverAttempt | SourcePCI:156;SourceNR-ARFC... |
| 2024-09-20 22:21:38.750 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.765 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.910 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.910 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3274153 | 1 | 6.8943 | 17.2273 | -114.6352 | 11.1963 | 150.8810 | 0.0093 | 0.0073 |
| 2024_09_20 22:00 | 3274095 | 2 | 76.5222 | 89.6556 | -115.9973 | 16.8407 | 147.9887 | 0.0033 | 0.0154 |
| 2024_09_20 22:00 | 3266585 | 3 | 7.2441 | 8.5658 | -116.9742 | 18.3391 | 198.9674 | 0.0068 | 0.0129 |
| 2024_09_20 22:00 | 3234673 | 4 | 14.5024 | 6.4070 | -115.2342 | 16.5926 | 139.1616 | 0.0101 | 0.0116 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416675_387C331B | 504990 | 940 | -87.6 | 504990 | 444 | -86.8 | 504990 | 265 | -93.8 | 504990 | 341 |
| MR_1774416675_594F1839 | 504990 | 940 | -89.2 | 504990 | 444 | -89.4 | 504990 | 265 | -94.7 | 504990 | 341 |
| MR_1774416675_CAB6988E | 504990 | 940 | -89.2 | 504990 | 444 | -85.9 | 504990 | 265 | -94.4 | 504990 | 341 |
| MR_1774416675_97B99A41 | 504990 | 940 | -89.6 | 504990 | 444 | -86.8 | 504990 | 265 | -96.8 | 504990 | 341 |
| MR_1774416675_CB884B78 | 504990 | 940 | -85.8 | 504990 | 444 | -86.2 | 504990 | 265 | -93.8 | 504990 | 341 |

> *... 2개 열 생략 (전체 14열)*

---
