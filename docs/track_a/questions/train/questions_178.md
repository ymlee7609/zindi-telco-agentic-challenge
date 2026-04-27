# Track A 문제 분석 — train[1770]~train[1779]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[1770] ~ train[1779] (10개)

## 목차

1. [문제 1770: `01b04a86-b80...`](#1770) — single-answer, 정답: C11
2. [문제 1771: `d083a7b1-34b...`](#1771) — single-answer, 정답: C22
3. [문제 1772: `5437f3ee-280...`](#1772) — single-answer, 정답: C11
4. [문제 1773: `07eb3f8b-16c...`](#1773) — single-answer, 정답: C16
5. [문제 1774: `5ef8ce32-a57...`](#1774) — multiple-answer, 정답: C3|C11
6. [문제 1775: `880cb68e-a6a...`](#1775) — single-answer, 정답: C11
7. [문제 1776: `e724a5a3-61d...`](#1776) — single-answer, 정답: C13
8. [문제 1777: `f9279b59-684...`](#1777) — multiple-answer, 정답: C1|C5|C15|C16
9. [문제 1778: `0efa986e-a35...`](#1778) — multiple-answer, 정답: C3|C12
10. [문제 1779: `4f2fe21f-52f...`](#1779) — single-answer, 정답: C14

---

### 문제 1770: `01b04a86-b80...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `01b04a86-b806-42b6-ac0a-d0266bb49974` |
| Tag | **single-answer** |
| 정답 | **C11** |
| C11 의미 | Decrease A3 Offset threshold for 3219277_1 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1770] topology](images/train_1770.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3214026_4 by 10 degrees
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3214026_4
- `C3`: Check test server and transmission issues
- `C4`: Add neighbor relationship between 3219277_1 and 3214026_4
- `C5`: Add neighbor relationship between 3228488_2 and 3214026_4
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3219277_1
- `C7`: Decrease transmission power for 3214026_4
- `C8`: Lift the tilt angle  of 3214026_4 by 10 degrees
- `C9`: Increase A3 Offset threshold for 3214026_4
- `C10`: Increase transmission power for 3214026_4
- `C11`: Decrease A3 Offset threshold for 3219277_1 **← 정답**
- `C12`: Increase transmission power for 3219277_1
- `C13`: Insufficient data; more data is needed for judgment.
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3219277_1
- `C15`: Adjust the azimuth of 3214026_4 by 50 degrees
- `C16`: Increase A3 Offset threshold for 3219277_1
- `C17`: Adjust the azimuth of 3219277_1 by 20 degrees
- `C18`: Decrease A3 Offset threshold for 3214026_4
- `C19`: Lift the tilt angle of 3219277_1 by 10 degrees
- `C20`: Decrease transmission power for 3219277_1
- `C21`: Press down the tilt angle of 3219277_1 by 10 degrees
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3214026_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.883 | MS1 | 121.4656701126 | 31.1446349903 | 394 | 504990 | -78.15 | 17.00 | 575.19 | 0.08 | 2.54 | 1571 |
| 2024-09-20 22:21:32.521 | MS1 | 121.4656643252 | 31.1446263739 | 394 | 504990 | -80.09 | 14.38 | 507.54 | 0.17 | 2.00 | 1588 |
| 2024-09-20 22:21:33.792 | MS1 | 121.4656736349 | 31.1446227600 | 394 | 504990 | -76.61 | 14.07 | 330.81 | 0.04 | 2.31 | 1582 |
| 2024-09-20 22:21:34.453 | MS1 | 121.4656771955 | 31.1446276634 | 394 | 504990 | -86.99 | -1.98 | 57.97 | 0.19 | 1.48 | 1569 |
| 2024-09-20 22:21:35.467 | MS1 | 121.4656669102 | 31.1446207287 | 394 | 504990 | -92.60 | -2.75 | 65.69 | 0.11 | 1.47 | 1560 |
| 2024-09-20 22:21:36.718 | MS1 | 121.4656682273 | 31.1446244113 | 394 | 504990 | -86.85 | -2.15 | 35.02 | 0.17 | 1.08 | 1575 |
| 2024-09-20 22:21:37.469 | MS1 | 121.4656751356 | 31.1446327670 | 394 | 504990 | -84.01 | -2.41 | 34.10 | 0.09 | 1.07 | 1566 |
| 2024-09-20 22:21:38.489 | MS1 | 121.4656759938 | 31.1446287163 | 394 | 504990 | -88.81 | -3.55 | 38.88 | 0.16 | 1.03 | 1577 |
| 2024-09-20 22:21:39.776 | MS1 | 121.4656704995 | 31.1446250627 | 335 | 504990 | -76.65 | 14.90 | 294.73 | 0.12 | 1.32 | 1588 |
| 2024-09-20 22:21:40.676 | MS1 | 121.4656584715 | 31.1446375298 | 335 | 504990 | -79.50 | 14.04 | 422.24 | 0.16 | 2.71 | 1589 |
| 2024-09-20 22:21:41.385 | MS1 | 121.4656683054 | 31.1446217172 | 335 | 504990 | -76.49 | 16.88 | 592.02 | 0.16 | 2.90 | 1568 |
| 2024-09-20 22:21:42.287 | MS1 | 121.4656774120 | 31.1446221994 | 335 | 504990 | -75.16 | 14.89 | 452.40 | 0.14 | 2.63 | 1577 |

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
| 3214026 | 4 | 121.4697094786 | 31.1514354086 | 301 | 15 | 8 | 38.3 | TDD | 335 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3219277 | 1 | 121.4756704535 | 31.1464045956 | 278 | 14 | 8 | 37.7 | TDD | 394 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3228488 | 2 | 121.4689221424 | 31.1535519759 | 330 | 9 | 6 | 42.9 | TDD | 411 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3261743 | 3 | 121.4711632625 | 31.1528834464 | 24 | 13 | 12 | 42.8 | TDD | 668 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:30.808 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.825 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:30.932 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.932 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.621 | NREventA3 | measId:2;ServCellPCI:983;Se... |
| 2024-09-20 22:21:37.861 | NRHandoverAttempt | SourcePCI:983;SourceNR-ARFC... |
| 2024-09-20 22:21:37.898 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.909 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.026 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.026 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3219277 | 1 | 17.8194 | 7.0121 | -114.9475 | 12.9132 | 107.3632 | 0.0119 | 0.1165 |
| 2024_09_20 22:00 | 3228488 | 2 | 11.7772 | 6.5324 | -116.0577 | 5.9015 | 166.0804 | 0.0077 | 0.0054 |
| 2024_09_20 22:00 | 3261743 | 3 | 9.7957 | 8.1334 | -115.4769 | 13.9331 | 149.9989 | 0.0036 | 0.0166 |
| 2024_09_20 22:00 | 3214026 | 4 | 7.2577 | 10.5571 | -115.1754 | 7.3278 | 173.4527 | 0.0019 | 0.0042 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414879_67876A2D | 504990 | 335 | -81.9 | 504990 | 394 | -85.2 | 504990 | 411 | -83.6 | 504990 | 668 |
| MR_1774414879_82DC6FD8 | 504990 | 335 | -83.8 | 504990 | 394 | -86.7 | 504990 | 411 | -82.7 | 504990 | 668 |
| MR_1774414879_FDFB6194 | 504990 | 394 | -85.8 | 504990 | 335 | -83.6 | 504990 | 411 | -83.5 | 504990 | 668 |
| MR_1774414879_E7A6034C | 504990 | 335 | -80.9 | 504990 | 394 | -86.7 | 504990 | 411 | -81.6 | 504990 | 668 |
| MR_1774414879_3704C13E | 504990 | 394 | -87.6 | 504990 | 335 | -82.0 | 504990 | 411 | -83.3 | 504990 | 668 |
| MR_1774414879_9A5AA88D | 504990 | 335 | -80.1 | 504990 | 394 | -85.3 | 504990 | 411 | -82.3 | 504990 | 668 |
| MR_1774414879_D4636D6F | 504990 | 335 | -83.9 | 504990 | 394 | -86.8 | 504990 | 411 | -81.6 | 504990 | 668 |
| MR_1774414879_D5D1B724 | 504990 | 394 | -88.3 | 504990 | 335 | -81.4 | 504990 | 411 | -85.2 | 504990 | 668 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1771: `d083a7b1-34b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `d083a7b1-34b2-4ea3-a904-8d3006944fb7` |
| Tag | **single-answer** |
| 정답 | **C22** |
| C22 의미 | Lift the tilt angle  of 3249551_3 by 7 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1771] topology](images/train_1771.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3241648_1 by 46 degrees
- `C2`: Decrease transmission power for 3262270_2
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3262270_2
- `C4`: Increase A3 Offset threshold for 3262270_2
- `C5`: Increase A3 Offset threshold for 3241648_1
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3241648_1
- `C7`: Add neighbor relationship between 3249551_3 and 3262270_2
- `C8`: Check test server and transmission issues
- `C9`: Decrease A3 Offset threshold for 3262270_2
- `C10`: Increase transmission power for 3262270_2
- `C11`: Adjust the azimuth of 3249551_3 by 50 degrees
- `C12`: Add neighbor relationship between 3241648_1 and 3262270_2
- `C13`: Press down the tilt angle of 3241648_1 by 4 degrees
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3262270_2
- `C15`: Lift the tilt angle of 3241648_1 by 4 degrees
- `C16`: Increase transmission power for 3241648_1
- `C17`: Press down the tilt angle  of 3249551_3 by 7 degrees
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3241648_1
- `C19`: Decrease transmission power for 3241648_1
- `C20`: Insufficient data; more data is needed for judgment.
- `C21`: Decrease A3 Offset threshold for 3241648_1
- `C22`: Lift the tilt angle  of 3249551_3 by 7 degrees **← 정답**

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.952 | MS1 | 121.4656683188 | 31.1446211956 | 312 | 504990 | -90.75 | 14.44 | 412.30 | 0.10 | 2.63 | 1585 |
| 2024-09-20 22:21:32.223 | MS1 | 121.4656674319 | 31.1446285380 | 312 | 504990 | -85.15 | 17.11 | 551.45 | 0.01 | 2.87 | 1579 |
| 2024-09-20 22:21:33.625 | MS1 | 121.4656683043 | 31.1446239056 | 312 | 504990 | -86.04 | 17.86 | 404.08 | 0.15 | 2.79 | 1588 |
| 2024-09-20 22:21:34.499 | MS1 | 121.4656663335 | 31.1446366761 | 312 | 504990 | -90.67 | 14.80 | 80.60 | 0.06 | 2.89 | 1568 |
| 2024-09-20 22:21:35.586 | MS1 | 121.4656705329 | 31.1446263090 | 312 | 504990 | -90.09 | 14.98 | 71.18 | 0.16 | 2.02 | 1564 |
| 2024-09-20 22:21:36.157 | MS1 | 121.4656588854 | 31.1446296845 | 312 | 504990 | -87.57 | 13.63 | 44.22 | 0.06 | 2.72 | 1562 |
| 2024-09-20 22:21:37.196 | MS1 | 121.4656653198 | 31.1446278475 | 312 | 504990 | -91.22 | 7.79 | 52.19 | 0.02 | 2.25 | 1593 |
| 2024-09-20 22:21:38.155 | MS1 | 121.4656715899 | 31.1446234373 | 312 | 504990 | -91.39 | 7.59 | 83.63 | 0.16 | 2.12 | 1575 |
| 2024-09-20 22:21:39.636 | MS1 | 121.4656623963 | 31.1446377182 | 312 | 504990 | -90.12 | 10.50 | 61.22 | 0.13 | 2.36 | 1584 |
| 2024-09-20 22:21:40.545 | MS1 | 121.4656774838 | 31.1446265375 | 312 | 504990 | -89.18 | 10.32 | 306.72 | 0.08 | 2.74 | 1593 |
| 2024-09-20 22:21:41.816 | MS1 | 121.4656728246 | 31.1446323053 | 312 | 504990 | -90.16 | 11.39 | 529.02 | 0.18 | 2.94 | 1591 |
| 2024-09-20 22:21:42.869 | MS1 | 121.4656637593 | 31.1446220498 | 312 | 504990 | -92.79 | 11.09 | 369.27 | 0.05 | 2.65 | 1588 |

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
| 3241648 | 1 | 121.4723083029 | 31.1485478223 | 281 | 1 | 2 | 33.8 | TDD | 312 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3249551 | 3 | 121.4732627264 | 31.1470815594 | 112 | 4 | 1 | 45.3 | TDD | 636 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3253612 | 4 | 121.4652458611 | 31.1516659806 | 241 | 8 | 3 | 38.6 | TDD | 37 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3262270 | 2 | 121.4723220878 | 31.1468310773 | 334 | 3 | 8 | 42.4 | TDD | 241 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:31.431 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.446 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.567 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.567 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.240 | NREventA3 | measId:2;ServCellPCI:950;Se... |
| 2024-09-20 22:21:38.480 | NRHandoverAttempt | SourcePCI:950;SourceNR-ARFC... |
| 2024-09-20 22:21:38.511 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.522 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.649 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.649 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3241648 | 1 | 76.7838 | 88.6504 | -116.2842 | 18.4929 | 143.0659 | 0.0017 | 0.0073 |
| 2024_09_20 22:00 | 3262270 | 2 | 17.5128 | 11.8792 | -117.4182 | 13.2457 | 117.0958 | 0.0182 | 0.0168 |
| 2024_09_20 22:00 | 3249551 | 3 | 10.0512 | 12.7952 | -117.9191 | 10.3058 | 167.4706 | 0.0040 | 0.0131 |
| 2024_09_20 22:00 | 3253612 | 4 | 19.5831 | 12.1825 | -115.2609 | 19.6538 | 100.2655 | 0.0081 | 0.0081 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415889_D75475B6 | 504990 | 312 | -90.5 | 504990 | 241 | -99.2 | 504990 | 636 | -104.0 | 504990 | 37 |
| MR_1774415889_FE946174 | 504990 | 312 | -90.9 | 504990 | 241 | -99.3 | 504990 | 636 | -105.0 | 504990 | 37 |
| MR_1774415889_A87198A1 | 504990 | 312 | -92.5 | 504990 | 241 | -98.9 | 504990 | 636 | -106.5 | 504990 | 37 |
| MR_1774415889_702F39C2 | 504990 | 312 | -92.2 | 504990 | 241 | -98.4 | 504990 | 636 | -103.8 | 504990 | 37 |
| MR_1774415889_C1C79BF4 | 504990 | 312 | -90.6 | 504990 | 241 | -98.8 | 504990 | 636 | -105.0 | 504990 | 37 |
| MR_1774415889_FF08747F | 504990 | 312 | -91.5 | 504990 | 241 | -98.4 | 504990 | 636 | -104.9 | 504990 | 37 |
| MR_1774415889_E734FFB6 | 504990 | 312 | -90.5 | 504990 | 241 | -100.0 | 504990 | 636 | -104.3 | 504990 | 37 |
| MR_1774415889_AADA6BFD | 504990 | 312 | -91.7 | 504990 | 241 | -96.5 | 504990 | 636 | -103.5 | 504990 | 37 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1772: `5437f3ee-280...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `5437f3ee-280f-4052-ada7-3868db563d50` |
| Tag | **single-answer** |
| 정답 | **C11** |
| C11 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1772] topology](images/train_1772.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3244081_4
- `C2`: Press down the tilt angle of 3244081_4 by 3 degrees
- `C3`: Press down the tilt angle  of 3263762_3 by 5 degrees
- `C4`: Lift the tilt angle of 3244081_4 by 3 degrees
- `C5`: Insufficient data; more data is needed for judgment.
- `C6`: Add neighbor relationship between 3214997_1 and 3263762_3
- `C7`: Increase transmission power for 3244081_4
- `C8`: Adjust the azimuth of 3263762_3 by 50 degrees
- `C9`: Lift the tilt angle  of 3263762_3 by 5 degrees
- `C10`: Increase A3 Offset threshold for 3244081_4
- `C11`: Check test server and transmission issues **← 정답**
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3263762_3
- `C13`: Increase transmission power for 3263762_3
- `C14`: Decrease transmission power for 3244081_4
- `C15`: Decrease transmission power for 3263762_3
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3244081_4
- `C17`: Adjust the azimuth of 3244081_4 by 50 degrees
- `C18`: Decrease A3 Offset threshold for 3244081_4
- `C19`: Add neighbor relationship between 3244081_4 and 3263762_3
- `C20`: Increase A3 Offset threshold for 3263762_3
- `C21`: Decrease A3 Offset threshold for 3263762_3
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3263762_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.489 | MS1 | 121.4656638191 | 31.1446276032 | 623 | 504990 | -89.62 | 13.54 | 418.87 | 0.02 | 2.24 | 1600 |
| 2024-09-20 22:21:32.842 | MS1 | 121.4656774914 | 31.1446257081 | 623 | 504990 | -90.18 | 15.94 | 316.04 | 0.15 | 2.39 | 1599 |
| 2024-09-20 22:21:33.844 | MS1 | 121.4656655778 | 31.1446265790 | 623 | 504990 | -86.76 | 17.80 | 375.81 | 0.03 | 2.07 | 1594 |
| 2024-09-20 22:21:34.442 | MS1 | 121.4656637357 | 31.1446243434 | 623 | 504990 | -86.36 | 16.11 | 78.99 | 0.01 | 2.18 | 427 |
| 2024-09-20 22:21:35.588 | MS1 | 121.4656604740 | 31.1446325686 | 623 | 504990 | -88.41 | 13.26 | 103.26 | 0.10 | 2.42 | 337 |
| 2024-09-20 22:21:36.155 | MS1 | 121.4656640171 | 31.1446237864 | 623 | 504990 | -86.30 | 15.08 | 65.82 | 0.07 | 2.47 | 414 |
| 2024-09-20 22:21:37.717 | MS1 | 121.4656703745 | 31.1446260433 | 623 | 504990 | -90.44 | 9.13 | 77.32 | 0.11 | 2.68 | 438 |
| 2024-09-20 22:21:38.867 | MS1 | 121.4656725448 | 31.1446190252 | 623 | 504990 | -90.01 | 11.19 | 81.71 | 0.19 | 2.32 | 413 |
| 2024-09-20 22:21:39.718 | MS1 | 121.4656691870 | 31.1446271104 | 623 | 504990 | -90.36 | 9.15 | 49.33 | 0.00 | 2.20 | 346 |
| 2024-09-20 22:21:40.216 | MS1 | 121.4656735170 | 31.1446188993 | 623 | 504990 | -89.16 | 11.27 | 465.67 | 0.19 | 2.06 | 1598 |
| 2024-09-20 22:21:41.344 | MS1 | 121.4656766577 | 31.1446239436 | 623 | 504990 | -90.04 | 9.64 | 560.66 | 0.00 | 2.92 | 1569 |
| 2024-09-20 22:21:42.412 | MS1 | 121.4656749965 | 31.1446358474 | 623 | 504990 | -89.49 | 9.55 | 362.83 | 0.20 | 2.63 | 1593 |

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
| 3214997 | 1 | 121.4700965498 | 31.1490801099 | 121 | 0 | 1 | 33.5 | TDD | 665 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3232093 | 2 | 121.4698817633 | 31.1476090430 | 96 | 11 | 5 | 18.6 | TDD | 443 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3244081 | 4 | 121.4675913200 | 31.1517260314 | 86 | 1 | 1 | 23.2 | TDD | 623 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3263762 | 3 | 121.4686950788 | 31.1484013061 | 30 | 2 | 3 | 27.2 | TDD | 397 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |

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
| 2024-09-20 22:21:30.997 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.129 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.129 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.786 | NREventA3 | measId:2;ServCellPCI:841;Se... |
| 2024-09-20 22:21:38.026 | NRHandoverAttempt | SourcePCI:841;SourceNR-ARFC... |
| 2024-09-20 22:21:38.075 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.085 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.215 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.215 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3214997 | 1 | 18.2217 | 9.4016 | -116.7416 | 11.5519 | 103.9902 | 0.0088 | 0.0187 |
| 2024_09_20 22:00 | 3232093 | 2 | 8.7316 | 10.1131 | -114.4940 | 18.0051 | 162.1204 | 0.0069 | 0.0070 |
| 2024_09_20 22:00 | 3263762 | 3 | 16.9098 | 16.5885 | -117.7035 | 9.0096 | 147.4873 | 0.0055 | 0.0094 |
| 2024_09_20 22:00 | 3244081 | 4 | 10.2785 | 6.4932 | -115.4840 | 19.1961 | 161.8936 | 0.0044 | 0.0152 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414990_5DBA2BE4 | 504990 | 623 | -84.8 | 504990 | 397 | -88.0 | 504990 | 665 | -93.5 | 504990 | 443 |
| MR_1774414990_0886BA8B | 504990 | 623 | -87.8 | 504990 | 397 | -88.1 | 504990 | 665 | -93.0 | 504990 | 443 |
| MR_1774414990_A07EEE04 | 504990 | 623 | -88.0 | 504990 | 397 | -87.9 | 504990 | 665 | -95.4 | 504990 | 443 |
| MR_1774414990_4F3817F2 | 504990 | 623 | -84.7 | 504990 | 397 | -86.7 | 504990 | 665 | -96.0 | 504990 | 443 |
| MR_1774414990_C0298EF3 | 504990 | 623 | -86.4 | 504990 | 397 | -88.2 | 504990 | 665 | -94.6 | 504990 | 443 |
| MR_1774414990_A0F8CAF7 | 504990 | 623 | -87.7 | 504990 | 397 | -87.6 | 504990 | 665 | -95.3 | 504990 | 443 |
| MR_1774414990_9328CBFA | 504990 | 623 | -84.8 | 504990 | 397 | -88.2 | 504990 | 665 | -95.0 | 504990 | 443 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1773: `07eb3f8b-16c...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `07eb3f8b-16cb-44dd-9e95-f00f6b5ce8cc` |
| Tag | **single-answer** |
| 정답 | **C16** |
| C16 의미 | Decrease A3 Offset threshold for 3212764_2 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1773] topology](images/train_1773.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3225231_3
- `C2`: Increase A3 Offset threshold for 3212764_2
- `C3`: Adjust the azimuth of 3212764_2 by 17 degrees
- `C4`: Adjust the azimuth of 3225231_3 by 50 degrees
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3212764_2
- `C6`: Press down the tilt angle  of 3225231_3 by 10 degrees
- `C7`: Add neighbor relationship between 3240312_4 and 3225231_3
- `C8`: Lift the tilt angle of 3212764_2 by 10 degrees
- `C9`: Increase A3 Offset threshold for 3225231_3
- `C10`: Decrease transmission power for 3212764_2
- `C11`: Lift the tilt angle  of 3225231_3 by 10 degrees
- `C12`: Press down the tilt angle of 3212764_2 by 10 degrees
- `C13`: Insufficient data; more data is needed for judgment.
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3225231_3
- `C15`: Check test server and transmission issues
- `C16`: Decrease A3 Offset threshold for 3212764_2 **← 정답**
- `C17`: Add neighbor relationship between 3212764_2 and 3225231_3
- `C18`: Increase transmission power for 3212764_2
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3212764_2
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3225231_3
- `C21`: Increase transmission power for 3225231_3
- `C22`: Decrease transmission power for 3225231_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.847 | MS1 | 121.4656661329 | 31.1446217622 | 498 | 504990 | -80.91 | 13.27 | 334.05 | 0.00 | 2.48 | 1581 |
| 2024-09-20 22:21:32.769 | MS1 | 121.4656606212 | 31.1446301989 | 498 | 504990 | -81.21 | 17.25 | 312.97 | 0.17 | 2.09 | 1566 |
| 2024-09-20 22:21:33.515 | MS1 | 121.4656648915 | 31.1446303701 | 498 | 504990 | -75.32 | 13.01 | 492.09 | 0.08 | 2.32 | 1570 |
| 2024-09-20 22:21:34.121 | MS1 | 121.4656761100 | 31.1446200913 | 498 | 504990 | -84.79 | -2.26 | 50.90 | 0.05 | 1.03 | 1565 |
| 2024-09-20 22:21:35.449 | MS1 | 121.4656634567 | 31.1446216062 | 498 | 504990 | -90.73 | -2.21 | 44.87 | 0.00 | 1.05 | 1579 |
| 2024-09-20 22:21:36.545 | MS1 | 121.4656707156 | 31.1446192236 | 498 | 504990 | -88.83 | -1.33 | 56.20 | 0.01 | 1.02 | 1572 |
| 2024-09-20 22:21:37.499 | MS1 | 121.4656723291 | 31.1446326859 | 498 | 504990 | -92.50 | -0.99 | 64.04 | 0.09 | 1.41 | 1562 |
| 2024-09-20 22:21:38.985 | MS1 | 121.4656585949 | 31.1446336110 | 498 | 504990 | -86.10 | -2.42 | 69.51 | 0.01 | 1.12 | 1563 |
| 2024-09-20 22:21:39.455 | MS1 | 121.4656731493 | 31.1446267233 | 620 | 504990 | -80.43 | 13.03 | 249.09 | 0.10 | 1.24 | 1590 |
| 2024-09-20 22:21:40.711 | MS1 | 121.4656685769 | 31.1446332256 | 620 | 504990 | -81.99 | 13.04 | 475.88 | 0.19 | 2.63 | 1562 |
| 2024-09-20 22:21:41.859 | MS1 | 121.4656695831 | 31.1446311213 | 620 | 504990 | -79.21 | 17.49 | 412.98 | 0.09 | 2.74 | 1570 |
| 2024-09-20 22:21:42.991 | MS1 | 121.4656717564 | 31.1446281647 | 620 | 504990 | -78.96 | 15.13 | 579.13 | 0.06 | 2.04 | 1582 |

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
| 3212764 | 2 | 121.4664421757 | 31.1451689049 | 248 | 15 | 6 | 26.8 | TDD | 498 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3225231 | 3 | 121.4648219361 | 31.1493863272 | 56 | 14 | 3 | 19.9 | TDD | 620 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3240312 | 4 | 121.4665866572 | 31.1512920764 | 308 | 14 | 4 | 15.6 | TDD | 647 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3252687 | 1 | 121.4740730890 | 31.1547974650 | 151 | 12 | 1 | 19.6 | TDD | 856 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:30.965 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.983 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.110 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.110 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.826 | NREventA3 | measId:2;ServCellPCI:238;Se... |
| 2024-09-20 22:21:38.066 | NRHandoverAttempt | SourcePCI:238;SourceNR-ARFC... |
| 2024-09-20 22:21:38.112 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.122 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.263 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.263 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3252687 | 1 | 15.4037 | 14.6543 | -114.7275 | 14.7476 | 159.9641 | 0.0191 | 0.0098 |
| 2024_09_20 22:00 | 3212764 | 2 | 15.8134 | 14.8936 | -115.7147 | 8.6321 | 195.8297 | 0.0075 | 0.1865 |
| 2024_09_20 22:00 | 3225231 | 3 | 11.8805 | 16.7137 | -116.7528 | 7.2025 | 191.5306 | 0.0080 | 0.0126 |
| 2024_09_20 22:00 | 3240312 | 4 | 11.1589 | 11.2048 | -117.8639 | 19.8925 | 84.4253 | 0.0056 | 0.0074 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413770_FF6EF691 | 504990 | 620 | -78.2 | 504990 | 498 | -86.6 | 504990 | 647 | -81.4 | 504990 | 856 |
| MR_1774413770_23AE57E0 | 504990 | 620 | -76.9 | 504990 | 498 | -84.6 | 504990 | 647 | -79.6 | 504990 | 856 |
| MR_1774413770_DCE3A136 | 504990 | 498 | -85.9 | 504990 | 620 | -78.6 | 504990 | 647 | -81.1 | 504990 | 856 |
| MR_1774413770_67955C13 | 504990 | 620 | -78.9 | 504990 | 498 | -83.1 | 504990 | 647 | -80.5 | 504990 | 856 |
| MR_1774413770_57E2C121 | 504990 | 498 | -83.9 | 504990 | 620 | -79.4 | 504990 | 647 | -80.2 | 504990 | 856 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1774: `5ef8ce32-a57...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `5ef8ce32-a574-474a-b0cb-f83d8ed2bf19` |
| Tag | **multiple-answer** |
| 정답 | **C3|C11** |
| C3 의미 | Increase transmission power for 3249188_1 |
| C11 의미 | Adjust the azimuth of 3249188_1 by 43 degrees |
| 패턴 분류 | **P4 Coverage (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1774] topology](images/train_1774.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3249188_1
- `C2`: Insufficient data; more data is needed for judgment.
- `C3`: Increase transmission power for 3249188_1 **← 정답**
- `C4`: Decrease A3 Offset threshold for 3257623_2
- `C5`: Add neighbor relationship between 3249188_1 and 3257623_2
- `C6`: Press down the tilt angle of 3249188_1 by 10 degrees
- `C7`: Add neighbor relationship between 3275620_3 and 3257623_2
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3249188_1
- `C9`: Increase transmission power for 3257623_2
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3249188_1
- `C11`: Adjust the azimuth of 3249188_1 by 43 degrees **← 정답**
- `C12`: Lift the tilt angle of 3249188_1 by 10 degrees
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3257623_2
- `C14`: Increase A3 Offset threshold for 3257623_2
- `C15`: Increase A3 Offset threshold for 3249188_1
- `C16`: Lift the tilt angle  of 3257623_2 by 3 degrees
- `C17`: Adjust the azimuth of 3257623_2 by 49 degrees
- `C18`: Decrease A3 Offset threshold for 3249188_1
- `C19`: Press down the tilt angle  of 3257623_2 by 3 degrees
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3257623_2
- `C21`: Check test server and transmission issues
- `C22`: Decrease transmission power for 3257623_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.968 | MS1 | 121.4656592654 | 31.1446195516 | 106 | 504990 | -92.10 | 13.16 | 440.91 | 0.05 | 2.18 | 1597 |
| 2024-09-20 22:21:32.448 | MS1 | 121.4656615046 | 31.1446235323 | 106 | 504990 | -86.00 | 13.43 | 590.16 | 0.16 | 2.03 | 1600 |
| 2024-09-20 22:21:33.404 | MS1 | 121.4656639859 | 31.1446184518 | 106 | 504990 | -90.12 | 14.11 | 338.91 | 0.16 | 2.36 | 1570 |
| 2024-09-20 22:21:34.394 | MS1 | 121.4656634565 | 31.1446207040 | 106 | 504990 | -105.28 | -0.25 | 29.36 | 0.00 | 1.35 | 1597 |
| 2024-09-20 22:21:35.656 | MS1 | 121.4656610793 | 31.1446259130 | 106 | 504990 | -105.98 | -0.85 | 54.96 | 0.08 | 1.37 | 1584 |
| 2024-09-20 22:21:36.350 | MS1 | 121.4656704344 | 31.1446279185 | 106 | 504990 | -109.91 | -1.62 | 69.60 | 0.01 | 1.20 | 1571 |
| 2024-09-20 22:21:37.635 | MS1 | 121.4656682602 | 31.1446318410 | 106 | 504990 | -102.77 | -0.24 | 68.64 | 0.01 | 1.11 | 1560 |
| 2024-09-20 22:21:38.238 | MS1 | 121.4656753402 | 31.1446363904 | 106 | 504990 | -101.33 | 1.92 | 56.11 | 0.14 | 1.30 | 1588 |
| 2024-09-20 22:21:39.409 | MS1 | 121.4656722224 | 31.1446219068 | 106 | 504990 | -100.66 | 1.33 | 19.41 | 0.10 | 1.11 | 1585 |
| 2024-09-20 22:21:40.178 | MS1 | 121.4656753888 | 31.1446288510 | 106 | 504990 | -90.54 | 12.89 | 400.25 | 0.18 | 2.01 | 1584 |
| 2024-09-20 22:21:41.282 | MS1 | 121.4656690909 | 31.1446326965 | 106 | 504990 | -88.21 | 13.38 | 348.72 | 0.10 | 2.96 | 1581 |
| 2024-09-20 22:21:42.660 | MS1 | 121.4656768677 | 31.1446348488 | 106 | 504990 | -91.80 | 16.73 | 391.70 | 0.03 | 2.69 | 1566 |

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
| 3249188 | 1 | 121.4703209484 | 31.1511774987 | 168 | 8 | 2 | 40.4 | TDD | 106 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3257623 | 2 | 121.4714419481 | 31.1465196667 | 298 | 0 | 5 | 27.7 | TDD | 759 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3275620 | 3 | 121.4758532646 | 31.1484408872 | 94 | 13 | 12 | 26.7 | TDD | 44 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3279447 | 4 | 121.4738100993 | 31.1440958214 | 278 | 14 | 12 | 29.5 | TDD | 844 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:31.272 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.292 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.422 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.422 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.671 | NREventA2 | measId:1;ServCellPCI:499;Se... |
| 2024-09-20 22:21:34.811 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3249188 | 1 | 9.6522 | 19.8175 | -117.2723 | 9.1272 | 179.1310 | 0.1718 | 0.0141 |
| 2024_09_20 22:00 | 3257623 | 2 | 6.1162 | 10.3393 | -115.3811 | 13.9103 | 197.9160 | 0.0063 | 0.0041 |
| 2024_09_20 22:00 | 3275620 | 3 | 5.0021 | 19.9856 | -116.5229 | 8.6924 | 149.9206 | 0.0151 | 0.0165 |
| 2024_09_20 22:00 | 3279447 | 4 | 7.0967 | 16.8314 | -116.7149 | 7.0193 | 177.4977 | 0.0082 | 0.0114 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412588_2763E685 | 504990 | 106 | -105.6 | 504990 | 759 | -112.4 | 504990 | 44 | -117.2 | 504990 | 844 |
| MR_1774412588_34B0C8F4 | 504990 | 106 | -106.2 | 504990 | 759 | -109.2 | 504990 | 44 | -116.6 | 504990 | 844 |
| MR_1774412588_B3F5B3D5 | 504990 | 106 | -105.4 | 504990 | 759 | -112.3 | 504990 | 44 | -116.9 | 504990 | 844 |
| MR_1774412588_AC760929 | 504990 | 106 | -104.5 | 504990 | 759 | -110.2 | 504990 | 44 | -119.6 | 504990 | 844 |
| MR_1774412588_ADF84929 | 504990 | 106 | -104.8 | 504990 | 759 | -111.2 | 504990 | 44 | -119.0 | 504990 | 844 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1775: `880cb68e-a6a...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `880cb68e-a6a0-4d9f-945b-9f4e441a8221` |
| Tag | **single-answer** |
| 정답 | **C11** |
| C11 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1775] topology](images/train_1775.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3216740_3
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3216740_3
- `C3`: Insufficient data; more data is needed for judgment.
- `C4`: Press down the tilt angle of 3216740_3 by 10 degrees
- `C5`: Adjust the azimuth of 3271402_2 by 50 degrees
- `C6`: Increase transmission power for 3216740_3
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3271402_2
- `C8`: Decrease A3 Offset threshold for 3216740_3
- `C9`: Decrease A3 Offset threshold for 3271402_2
- `C10`: Adjust the azimuth of 3216740_3 by 50 degrees
- `C11`: Check test server and transmission issues **← 정답**
- `C12`: Decrease transmission power for 3271402_2
- `C13`: Decrease transmission power for 3216740_3
- `C14`: Increase A3 Offset threshold for 3271402_2
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3271402_2
- `C16`: Increase transmission power for 3271402_2
- `C17`: Press down the tilt angle  of 3271402_2 by 10 degrees
- `C18`: Lift the tilt angle of 3216740_3 by 10 degrees
- `C19`: Add neighbor relationship between 3216740_3 and 3271402_2
- `C20`: Increase A3 Offset threshold for 3216740_3
- `C21`: Add neighbor relationship between 3279237_4 and 3271402_2
- `C22`: Lift the tilt angle  of 3271402_2 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.996 | MS1 | 121.4656700256 | 31.1446222000 | 556 | 504990 | -87.85 | 15.87 | 363.95 | 0.03 | 2.41 | 1583 |
| 2024-09-20 22:21:32.796 | MS1 | 121.4656636864 | 31.1446232851 | 556 | 504990 | -85.70 | 16.18 | 386.67 | 0.07 | 2.96 | 1596 |
| 2024-09-20 22:21:33.388 | MS1 | 121.4656611113 | 31.1446208737 | 556 | 504990 | -87.86 | 17.05 | 473.32 | 0.01 | 2.82 | 1560 |
| 2024-09-20 22:21:34.550 | MS1 | 121.4656659113 | 31.1446233447 | 556 | 504990 | -87.47 | 16.14 | 93.74 | 0.07 | 2.01 | 323 |
| 2024-09-20 22:21:35.986 | MS1 | 121.4656588904 | 31.1446345873 | 556 | 504990 | -88.20 | 16.57 | 59.78 | 0.09 | 2.65 | 456 |
| 2024-09-20 22:21:36.883 | MS1 | 121.4656589594 | 31.1446243376 | 556 | 504990 | -85.63 | 16.85 | 101.22 | 0.04 | 2.24 | 413 |
| 2024-09-20 22:21:37.734 | MS1 | 121.4656755405 | 31.1446357726 | 556 | 504990 | -93.35 | 7.56 | 77.81 | 0.16 | 2.59 | 499 |
| 2024-09-20 22:21:38.531 | MS1 | 121.4656595760 | 31.1446306175 | 556 | 504990 | -89.32 | 9.28 | 70.67 | 0.17 | 2.05 | 336 |
| 2024-09-20 22:21:39.712 | MS1 | 121.4656733019 | 31.1446322960 | 556 | 504990 | -92.48 | 12.22 | 58.63 | 0.13 | 2.49 | 486 |
| 2024-09-20 22:21:40.684 | MS1 | 121.4656710972 | 31.1446329648 | 556 | 504990 | -91.68 | 10.86 | 332.05 | 0.13 | 2.46 | 1596 |
| 2024-09-20 22:21:41.123 | MS1 | 121.4656690674 | 31.1446256368 | 556 | 504990 | -89.45 | 9.85 | 488.61 | 0.20 | 2.09 | 1590 |
| 2024-09-20 22:21:42.892 | MS1 | 121.4656733794 | 31.1446205722 | 556 | 504990 | -89.48 | 12.12 | 571.54 | 0.08 | 2.01 | 1570 |

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
| 3216740 | 3 | 121.4692959119 | 31.1493897658 | 69 | 15 | 0 | 20.4 | TDD | 556 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3236467 | 1 | 121.4754652378 | 31.1440975347 | 48 | 1 | 7 | 19.0 | TDD | 264 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3271402 | 2 | 121.4695151584 | 31.1542531225 | 351 | 9 | 12 | 40.2 | TDD | 75 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3279237 | 4 | 121.4718974120 | 31.1484223077 | 318 | 3 | 6 | 33.3 | TDD | 155 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |

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
| 2024-09-20 22:21:31.326 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.469 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.469 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.130 | NREventA3 | measId:2;ServCellPCI:574;Se... |
| 2024-09-20 22:21:38.370 | NRHandoverAttempt | SourcePCI:574;SourceNR-ARFC... |
| 2024-09-20 22:21:38.407 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.417 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.557 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.557 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3236467 | 1 | 11.8073 | 15.6090 | -114.5704 | 8.0265 | 146.5767 | 0.0093 | 0.0193 |
| 2024_09_20 22:00 | 3271402 | 2 | 17.5880 | 11.6202 | -115.6009 | 7.2795 | 147.5788 | 0.0170 | 0.0123 |
| 2024_09_20 22:00 | 3216740 | 3 | 13.7882 | 19.3989 | -114.7447 | 12.2899 | 171.3665 | 0.0195 | 0.0052 |
| 2024_09_20 22:00 | 3279237 | 4 | 14.8386 | 13.5918 | -114.4990 | 15.4713 | 82.7773 | 0.0184 | 0.0073 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416138_7C2E9378 | 504990 | 556 | -88.0 | 504990 | 75 | -98.0 | 504990 | 155 | -101.5 | 504990 | 264 |
| MR_1774416138_991513DB | 504990 | 556 | -86.8 | 504990 | 75 | -95.0 | 504990 | 155 | -99.8 | 504990 | 264 |
| MR_1774416138_71AB80E0 | 504990 | 556 | -87.8 | 504990 | 75 | -95.2 | 504990 | 155 | -100.2 | 504990 | 264 |
| MR_1774416138_E728A35B | 504990 | 556 | -87.3 | 504990 | 75 | -97.9 | 504990 | 155 | -102.2 | 504990 | 264 |
| MR_1774416138_1DA0D79A | 504990 | 556 | -89.2 | 504990 | 75 | -96.4 | 504990 | 155 | -99.4 | 504990 | 264 |
| MR_1774416138_B4120D79 | 504990 | 556 | -86.7 | 504990 | 75 | -97.2 | 504990 | 155 | -101.4 | 504990 | 264 |
| MR_1774416138_CC238298 | 504990 | 556 | -85.9 | 504990 | 75 | -96.6 | 504990 | 155 | -101.3 | 504990 | 264 |
| MR_1774416138_A7064CB6 | 504990 | 556 | -87.0 | 504990 | 75 | -98.3 | 504990 | 155 | -102.0 | 504990 | 264 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1776: `e724a5a3-61d...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `e724a5a3-61da-4269-b4ea-f75ac458a8eb` |
| Tag | **single-answer** |
| 정답 | **C13** |
| C13 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1776] topology](images/train_1776.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3274931_3
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3228995_4
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3228995_4
- `C4`: Insufficient data; more data is needed for judgment.
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3274931_3
- `C6`: Press down the tilt angle  of 3274931_3 by 10 degrees
- `C7`: Press down the tilt angle of 3228995_4 by 10 degrees
- `C8`: Increase transmission power for 3228995_4
- `C9`: Decrease A3 Offset threshold for 3274931_3
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3274931_3
- `C11`: Lift the tilt angle  of 3274931_3 by 10 degrees
- `C12`: Lift the tilt angle of 3228995_4 by 10 degrees
- `C13`: Check test server and transmission issues **← 정답**
- `C14`: Adjust the azimuth of 3274931_3 by 50 degrees
- `C15`: Decrease transmission power for 3228995_4
- `C16`: Add neighbor relationship between 3228995_4 and 3274931_3
- `C17`: Increase transmission power for 3274931_3
- `C18`: Add neighbor relationship between 3237589_1 and 3274931_3
- `C19`: Decrease A3 Offset threshold for 3228995_4
- `C20`: Adjust the azimuth of 3228995_4 by 50 degrees
- `C21`: Increase A3 Offset threshold for 3228995_4
- `C22`: Decrease transmission power for 3274931_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.557 | MS1 | 121.4656633950 | 31.1446237789 | 535 | 504990 | -85.29 | 15.43 | 468.46 | 0.18 | 2.26 | 1584 |
| 2024-09-20 22:21:32.727 | MS1 | 121.4656647330 | 31.1446189762 | 535 | 504990 | -91.01 | 16.55 | 347.07 | 0.19 | 2.63 | 1581 |
| 2024-09-20 22:21:33.991 | MS1 | 121.4656645300 | 31.1446347867 | 535 | 504990 | -86.83 | 14.15 | 406.98 | 0.04 | 2.46 | 1584 |
| 2024-09-20 22:21:34.608 | MS1 | 121.4656737960 | 31.1446195065 | 535 | 504990 | -85.35 | 12.38 | 75.31 | 0.11 | 2.40 | 499 |
| 2024-09-20 22:21:35.702 | MS1 | 121.4656603868 | 31.1446257648 | 535 | 504990 | -85.97 | 13.90 | 47.39 | 0.18 | 2.40 | 300 |
| 2024-09-20 22:21:36.192 | MS1 | 121.4656657068 | 31.1446255861 | 535 | 504990 | -86.24 | 13.87 | 63.65 | 0.15 | 2.31 | 375 |
| 2024-09-20 22:21:37.444 | MS1 | 121.4656702781 | 31.1446377901 | 535 | 504990 | -89.06 | 12.90 | 83.58 | 0.11 | 2.51 | 434 |
| 2024-09-20 22:21:38.802 | MS1 | 121.4656662152 | 31.1446310708 | 535 | 504990 | -92.15 | 10.29 | 94.81 | 0.04 | 2.50 | 336 |
| 2024-09-20 22:21:39.888 | MS1 | 121.4656686922 | 31.1446254917 | 535 | 504990 | -93.75 | 10.90 | 78.47 | 0.11 | 2.20 | 409 |
| 2024-09-20 22:21:40.183 | MS1 | 121.4656657692 | 31.1446314815 | 535 | 504990 | -93.30 | 8.06 | 531.10 | 0.16 | 2.22 | 1589 |
| 2024-09-20 22:21:41.921 | MS1 | 121.4656649675 | 31.1446203205 | 535 | 504990 | -93.59 | 8.29 | 550.19 | 0.04 | 2.16 | 1579 |
| 2024-09-20 22:21:42.559 | MS1 | 121.4656732601 | 31.1446294335 | 535 | 504990 | -93.58 | 9.26 | 559.60 | 0.00 | 2.44 | 1593 |

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
| 3228995 | 4 | 121.4752970370 | 31.1532727326 | 325 | 11 | 2 | 23.6 | TDD | 535 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3233376 | 2 | 121.4757435534 | 31.1486459795 | 246 | 5 | 9 | 33.8 | TDD | 722 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3237589 | 1 | 121.4678940800 | 31.1488149155 | 229 | 1 | 4 | 27.0 | TDD | 201 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3274931 | 3 | 121.4693288120 | 31.1533284561 | 264 | 8 | 9 | 49.0 | TDD | 435 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |

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
| 2024-09-20 22:21:30.919 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.936 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.086 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.086 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.734 | NREventA3 | measId:2;ServCellPCI:117;Se... |
| 2024-09-20 22:21:37.974 | NRHandoverAttempt | SourcePCI:117;SourceNR-ARFC... |
| 2024-09-20 22:21:38.015 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.026 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.158 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.158 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3237589 | 1 | 18.0181 | 12.0429 | -115.7917 | 12.7615 | 167.2957 | 0.0032 | 0.0117 |
| 2024_09_20 22:00 | 3233376 | 2 | 6.2793 | 6.6718 | -116.1517 | 6.4824 | 158.1125 | 0.0095 | 0.0016 |
| 2024_09_20 22:00 | 3274931 | 3 | 8.5502 | 19.9101 | -114.4040 | 14.7035 | 97.4013 | 0.0006 | 0.0124 |
| 2024_09_20 22:00 | 3228995 | 4 | 14.3370 | 5.6865 | -114.8200 | 19.5309 | 179.9246 | 0.0049 | 0.0084 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416387_01A96C74 | 504990 | 535 | -83.7 | 504990 | 435 | -93.3 | 504990 | 201 | -96.2 | 504990 | 722 |
| MR_1774416387_B069D871 | 504990 | 535 | -86.6 | 504990 | 435 | -94.0 | 504990 | 201 | -93.5 | 504990 | 722 |
| MR_1774416387_415F05FF | 504990 | 535 | -84.0 | 504990 | 435 | -93.6 | 504990 | 201 | -95.0 | 504990 | 722 |
| MR_1774416387_9688CAFB | 504990 | 535 | -85.3 | 504990 | 435 | -92.7 | 504990 | 201 | -96.2 | 504990 | 722 |
| MR_1774416387_78305385 | 504990 | 535 | -86.7 | 504990 | 435 | -93.6 | 504990 | 201 | -97.0 | 504990 | 722 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1777: `f9279b59-684...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `f9279b59-6841-4602-82ed-6ed0460835c0` |
| Tag | **multiple-answer** |
| 정답 | **C1|C5|C15|C16** |
| C1 의미 | Increase A3 Offset threshold for 3236651_5 |
| C5 의미 | Increase A3 Offset threshold for 3279526_1 |
| C15 의미 | Press down the tilt angle  of 3236651_5 by 3 degrees |
| C16 의미 | Decrease transmission power for 3236651_5 |
| 패턴 분류 | **P2 Ping-pong** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1777] topology](images/train_1777.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 5 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 5개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3236651_5 **← 정답**
- `C2`: Decrease A3 Offset threshold for 3279526_1
- `C3`: Adjust the azimuth of 3236651_5 by 44 degrees
- `C4`: Increase transmission power for 3236651_5
- `C5`: Increase A3 Offset threshold for 3279526_1 **← 정답**
- `C6`: Increase transmission power for 3279526_1
- `C7`: Lift the tilt angle of 3279526_1 by 4 degrees
- `C8`: Add neighbor relationship between 3279526_1 and 3236651_5
- `C9`: Check test server and transmission issues
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3236651_5
- `C11`: Adjust the azimuth of 3279526_1 by 21 degrees
- `C12`: Add neighbor relationship between 3258264_4 and 3236651_5
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3279526_1
- `C14`: Lift the tilt angle  of 3236651_5 by 3 degrees
- `C15`: Press down the tilt angle  of 3236651_5 by 3 degrees **← 정답**
- `C16`: Decrease transmission power for 3236651_5 **← 정답**
- `C17`: Decrease transmission power for 3279526_1
- `C18`: Insufficient data; more data is needed for judgment.
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3279526_1
- `C20`: Press down the tilt angle of 3279526_1 by 4 degrees
- `C21`: Decrease A3 Offset threshold for 3236651_5
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3236651_5

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.524 | MS1 | 121.4656696596 | 31.1446308157 | 762 | 504990 | -80.42 | 13.65 | 504.09 | 0.12 | 2.53 | 1593 |
| 2024-09-20 22:21:32.582 | MS1 | 121.4656764178 | 31.1446306944 | 762 | 504990 | -80.29 | 13.74 | 453.51 | 0.08 | 2.98 | 1595 |
| 2024-09-20 22:21:33.471 | MS1 | 121.4656728917 | 31.1446219102 | 762 | 504990 | -78.65 | 16.98 | 350.19 | 0.03 | 2.17 | 1560 |
| 2024-09-20 22:21:34.544 | MS1 | 121.4656613365 | 31.1446372948 | 630 | 504990 | -88.89 | 1.55 | 68.34 | 0.15 | 1.28 | 1560 |
| 2024-09-20 22:21:35.589 | MS1 | 121.4656638499 | 31.1446256155 | 630 | 504990 | -85.05 | 3.58 | 38.59 | 0.19 | 1.20 | 1570 |
| 2024-09-20 22:21:36.627 | MS1 | 121.4656659500 | 31.1446275419 | 762 | 504990 | -87.72 | 2.52 | 73.39 | 0.10 | 1.39 | 1595 |
| 2024-09-20 22:21:37.224 | MS1 | 121.4656645238 | 31.1446224449 | 762 | 504990 | -82.93 | 4.98 | 68.20 | 0.13 | 1.42 | 1571 |
| 2024-09-20 22:21:38.895 | MS1 | 121.4656677604 | 31.1446311310 | 630 | 504990 | -80.68 | 4.90 | 78.31 | 0.20 | 1.17 | 1562 |
| 2024-09-20 22:21:39.375 | MS1 | 121.4656651618 | 31.1446286507 | 630 | 504990 | -83.52 | 3.45 | 55.30 | 0.07 | 1.41 | 1591 |
| 2024-09-20 22:21:40.360 | MS1 | 121.4656776564 | 31.1446191432 | 630 | 504990 | -77.27 | 17.34 | 479.19 | 0.18 | 2.81 | 1576 |
| 2024-09-20 22:21:41.649 | MS1 | 121.4656615713 | 31.1446289645 | 630 | 504990 | -75.17 | 16.22 | 404.12 | 0.03 | 2.11 | 1560 |
| 2024-09-20 22:21:42.353 | MS1 | 121.4656744366 | 31.1446226944 | 630 | 504990 | -77.13 | 17.35 | 545.47 | 0.17 | 2.19 | 1562 |

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
| 3236651 | 5 | 121.4738142201 | 31.1559039441 | 168 | 2 | 2 | 32.5 | TDD | 351 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3258264 | 4 | 121.4723631023 | 31.1482467060 | 290 | 7 | 3 | 44.0 | TDD | 698 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3274379 | 3 | 121.4689884670 | 31.1492844607 | 182 | 12 | 10 | 28.7 | TDD | 630 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3279067 | 2 | 121.4662140349 | 31.1476434712 | 33 | 5 | 7 | 48.8 | TDD | 655 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3279526 | 1 | 121.4749627117 | 31.1544585820 | 198 | 3 | 2 | 20.1 | TDD | 762 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:31.587 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.612 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.736 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.736 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.466 | NREventA3 | measId:2;ServCellPCI:523;Se... |
| 2024-09-20 22:21:34.706 | NRHandoverAttempt | SourcePCI:523;SourceNR-ARFC... |
| 2024-09-20 22:21:34.746 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:34.758 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:34.860 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:34.860 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:36.466 | NREventA3 | measId:2;ServCellPCI:211;Se... |
| 2024-09-20 22:21:36.706 | NRHandoverAttempt | SourcePCI:211;SourceNR-ARFC... |
| 2024-09-20 22:21:36.754 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:36.765 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:36.871 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.871 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.466 | NREventA3 | measId:2;ServCellPCI:523;Se... |
| 2024-09-20 22:21:38.706 | NRHandoverAttempt | SourcePCI:523;SourceNR-ARFC... |
| 2024-09-20 22:21:38.747 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.760 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.864 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.864 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3279526 | 1 | 10.1572 | 12.9837 | -116.0177 | 14.1109 | 190.3990 | 0.0064 | 0.0155 |
| 2024_09_20 22:00 | 3279067 | 2 | 5.9847 | 7.1288 | -117.3573 | 13.7280 | 154.6109 | 0.0033 | 0.0068 |
| 2024_09_20 22:00 | 3274379 | 3 | 16.2445 | 8.2450 | -115.8700 | 13.2135 | 124.5184 | 0.0126 | 0.0052 |
| 2024_09_20 22:00 | 3258264 | 4 | 9.8154 | 17.8360 | -115.9702 | 17.5919 | 139.7733 | 0.0198 | 0.0031 |
| 2024_09_20 22:00 | 3236651 | 5 | 8.2820 | 5.8870 | -115.6775 | 17.7684 | 82.5425 | 0.0095 | 0.0063 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416497_23F23746 | 504990 | 630 | -87.1 | 504990 | 762 | -86.7 | 504990 | 351 | -87.3 | 504990 | 698 |
| MR_1774416497_3FAB118F | 504990 | 630 | -88.0 | 504990 | 762 | -88.4 | 504990 | 351 | -89.3 | 504990 | 698 |
| MR_1774416497_3D19C2E8 | 504990 | 630 | -90.2 | 504990 | 762 | -85.7 | 504990 | 351 | -89.5 | 504990 | 698 |
| MR_1774416497_B1C8A490 | 504990 | 762 | -90.5 | 504990 | 630 | -86.1 | 504990 | 351 | -90.6 | 504990 | 698 |
| MR_1774416497_4D200571 | 504990 | 762 | -87.4 | 504990 | 630 | -87.5 | 504990 | 351 | -88.1 | 504990 | 698 |
| MR_1774416497_51983C5F | 504990 | 762 | -87.2 | 504990 | 630 | -86.5 | 504990 | 351 | -90.5 | 504990 | 698 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1778: `0efa986e-a35...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `0efa986e-a356-4d92-ba3b-09de2b8df399` |
| Tag | **multiple-answer** |
| 정답 | **C3|C12** |
| C3 의미 | Increase transmission power for 3230966_1 |
| C12 의미 | Adjust the azimuth of 3230966_1 by 34 degrees |
| 패턴 분류 | **P4 Coverage (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1778] topology](images/train_1778.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3230966_1
- `C2`: Decrease A3 Offset threshold for 3254142_3
- `C3`: Increase transmission power for 3230966_1 **← 정답**
- `C4`: Add neighbor relationship between 3265737_2 and 3254142_3
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3254142_3
- `C6`: Increase A3 Offset threshold for 3254142_3
- `C7`: Press down the tilt angle  of 3254142_3 by 5 degrees
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3230966_1
- `C9`: Press down the tilt angle of 3230966_1 by 7 degrees
- `C10`: Insufficient data; more data is needed for judgment.
- `C11`: Decrease A3 Offset threshold for 3230966_1
- `C12`: Adjust the azimuth of 3230966_1 by 34 degrees **← 정답**
- `C13`: Increase transmission power for 3254142_3
- `C14`: Lift the tilt angle  of 3254142_3 by 5 degrees
- `C15`: Decrease transmission power for 3254142_3
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3254142_3
- `C17`: Adjust the azimuth of 3254142_3 by 1 degrees
- `C18`: Add neighbor relationship between 3230966_1 and 3254142_3
- `C19`: Decrease transmission power for 3230966_1
- `C20`: Increase A3 Offset threshold for 3230966_1
- `C21`: Lift the tilt angle of 3230966_1 by 7 degrees
- `C22`: Check test server and transmission issues

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.800 | MS1 | 121.4656737405 | 31.1446186728 | 210 | 504990 | -89.48 | 16.26 | 312.20 | 0.07 | 2.89 | 1577 |
| 2024-09-20 22:21:32.480 | MS1 | 121.4656703130 | 31.1446196002 | 210 | 504990 | -86.62 | 16.59 | 445.39 | 0.18 | 2.68 | 1590 |
| 2024-09-20 22:21:33.358 | MS1 | 121.4656729288 | 31.1446366695 | 210 | 504990 | -94.24 | 15.17 | 346.96 | 0.07 | 2.85 | 1592 |
| 2024-09-20 22:21:34.753 | MS1 | 121.4656624493 | 31.1446311359 | 210 | 504990 | -102.67 | -1.11 | 45.62 | 0.00 | 1.22 | 1565 |
| 2024-09-20 22:21:35.466 | MS1 | 121.4656744724 | 31.1446186097 | 210 | 504990 | -106.25 | 1.23 | 35.66 | 0.02 | 1.39 | 1566 |
| 2024-09-20 22:21:36.117 | MS1 | 121.4656627156 | 31.1446260021 | 210 | 504990 | -101.79 | -0.18 | 86.53 | 0.17 | 1.38 | 1572 |
| 2024-09-20 22:21:37.749 | MS1 | 121.4656704464 | 31.1446278103 | 210 | 504990 | -108.44 | -0.33 | 54.89 | 0.07 | 1.10 | 1584 |
| 2024-09-20 22:21:38.946 | MS1 | 121.4656640621 | 31.1446194202 | 210 | 504990 | -103.98 | -1.91 | 77.49 | 0.00 | 1.00 | 1567 |
| 2024-09-20 22:21:39.990 | MS1 | 121.4656734764 | 31.1446232965 | 210 | 504990 | -103.31 | 0.99 | 79.19 | 0.15 | 1.27 | 1577 |
| 2024-09-20 22:21:40.614 | MS1 | 121.4656615282 | 31.1446343770 | 210 | 504990 | -88.94 | 12.48 | 377.56 | 0.05 | 2.65 | 1586 |
| 2024-09-20 22:21:41.477 | MS1 | 121.4656724262 | 31.1446300640 | 210 | 504990 | -93.25 | 12.66 | 363.21 | 0.10 | 2.87 | 1594 |
| 2024-09-20 22:21:42.204 | MS1 | 121.4656694201 | 31.1446240366 | 210 | 504990 | -92.71 | 17.23 | 576.46 | 0.16 | 2.02 | 1600 |

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
| 3217072 | 4 | 121.4735382547 | 31.1503192113 | 25 | 10 | 10 | 34.5 | TDD | 332 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3230966 | 1 | 121.4641659326 | 31.1482216833 | 126 | 2 | 6 | 40.4 | TDD | 210 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3254142 | 3 | 121.4738925503 | 31.1546238671 | 216 | 4 | 5 | 19.1 | TDD | 667 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3265737 | 2 | 121.4660650973 | 31.1458507880 | 243 | 6 | 4 | 48.3 | TDD | 498 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:31.299 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.321 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.469 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.469 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.648 | NREventA2 | measId:1;ServCellPCI:251;Se... |
| 2024-09-20 22:21:34.765 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3230966 | 1 | 13.0843 | 15.5979 | -115.8072 | 18.5616 | 125.2809 | 0.1490 | 0.0195 |
| 2024_09_20 22:00 | 3265737 | 2 | 18.0009 | 12.6499 | -115.1586 | 8.0704 | 182.6196 | 0.0157 | 0.0056 |
| 2024_09_20 22:00 | 3254142 | 3 | 10.5580 | 19.9145 | -115.6087 | 11.2209 | 118.3089 | 0.0163 | 0.0119 |
| 2024_09_20 22:00 | 3217072 | 4 | 5.0470 | 11.7520 | -115.0379 | 16.5478 | 186.1565 | 0.0017 | 0.0063 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414584_0B99B82F | 504990 | 210 | -102.9 | 504990 | 667 | -104.5 | 504990 | 498 | -113.5 | 504990 | 332 |
| MR_1774414584_10D2872B | 504990 | 210 | -104.4 | 504990 | 667 | -105.3 | 504990 | 498 | -113.6 | 504990 | 332 |
| MR_1774414584_3E0B08CA | 504990 | 210 | -101.0 | 504990 | 667 | -104.3 | 504990 | 498 | -112.6 | 504990 | 332 |
| MR_1774414584_11CD3CD1 | 504990 | 210 | -104.1 | 504990 | 667 | -106.7 | 504990 | 498 | -111.8 | 504990 | 332 |
| MR_1774414584_B672DEC3 | 504990 | 210 | -101.4 | 504990 | 667 | -104.8 | 504990 | 498 | -113.3 | 504990 | 332 |
| MR_1774414584_01179EA0 | 504990 | 210 | -103.4 | 504990 | 667 | -107.0 | 504990 | 498 | -113.9 | 504990 | 332 |
| MR_1774414584_52760FC8 | 504990 | 210 | -104.0 | 504990 | 667 | -104.1 | 504990 | 498 | -113.3 | 504990 | 332 |
| MR_1774414584_54AA4694 | 504990 | 210 | -102.1 | 504990 | 667 | -106.1 | 504990 | 498 | -114.5 | 504990 | 332 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1779: `4f2fe21f-52f...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `4f2fe21f-52f8-49e5-9231-fb50c2ba8e9e` |
| Tag | **single-answer** |
| 정답 | **C14** |
| C14 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3222206_3 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1779] topology](images/train_1779.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3229865_1
- `C2`: Add neighbor relationship between 3245327_4 and 3229865_1
- `C3`: Decrease A3 Offset threshold for 3222206_3
- `C4`: Adjust the azimuth of 3222206_3 by 37 degrees
- `C5`: Increase transmission power for 3222206_3
- `C6`: Lift the tilt angle of 3222206_3 by 1 degrees
- `C7`: Add neighbor relationship between 3222206_3 and 3229865_1
- `C8`: Decrease A3 Offset threshold for 3229865_1
- `C9`: Insufficient data; more data is needed for judgment.
- `C10`: Decrease transmission power for 3229865_1
- `C11`: Press down the tilt angle  of 3229865_1 by 10 degrees
- `C12`: Press down the tilt angle of 3222206_3 by 1 degrees
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3229865_1
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3222206_3 **← 정답**
- `C15`: Increase transmission power for 3229865_1
- `C16`: Lift the tilt angle  of 3229865_1 by 10 degrees
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3229865_1
- `C18`: Decrease transmission power for 3222206_3
- `C19`: Adjust the azimuth of 3229865_1 by 50 degrees
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3222206_3
- `C21`: Increase A3 Offset threshold for 3222206_3
- `C22`: Check test server and transmission issues

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.576 | MS1 | 121.4656615181 | 31.1446295549 | 806 | 504990 | -87.95 | 15.62 | 344.43 | 0.14 | 2.62 | 1597 |
| 2024-09-20 22:21:32.561 | MS1 | 121.4656675349 | 31.1446355781 | 806 | 504990 | -91.21 | 12.41 | 498.78 | 0.06 | 2.56 | 1577 |
| 2024-09-20 22:21:33.115 | MS1 | 121.4656740244 | 31.1446217150 | 806 | 504990 | -90.17 | 12.53 | 381.70 | 0.13 | 2.70 | 1579 |
| 2024-09-20 22:21:34.306 | MS1 | 121.4656636261 | 31.1446344742 | 806 | 504990 | -86.99 | 14.60 | 93.32 | 0.59 | 2.12 | 640 |
| 2024-09-20 22:21:35.172 | MS1 | 121.4656669228 | 31.1446369676 | 806 | 504990 | -90.23 | 15.84 | 86.94 | 0.53 | 2.10 | 627 |
| 2024-09-20 22:21:36.296 | MS1 | 121.4656632401 | 31.1446299841 | 806 | 504990 | -91.75 | 17.08 | 84.13 | 0.58 | 2.47 | 516 |
| 2024-09-20 22:21:37.119 | MS1 | 121.4656608752 | 31.1446346917 | 806 | 504990 | -90.40 | 11.85 | 91.98 | 0.61 | 2.74 | 624 |
| 2024-09-20 22:21:38.901 | MS1 | 121.4656647370 | 31.1446283586 | 806 | 504990 | -93.50 | 7.79 | 85.77 | 0.55 | 2.94 | 568 |
| 2024-09-20 22:21:39.163 | MS1 | 121.4656674677 | 31.1446301801 | 806 | 504990 | -89.98 | 8.78 | 87.19 | 0.60 | 2.08 | 594 |
| 2024-09-20 22:21:40.337 | MS1 | 121.4656710646 | 31.1446271031 | 806 | 504990 | -93.47 | 12.93 | 415.44 | 0.06 | 2.09 | 1578 |
| 2024-09-20 22:21:41.920 | MS1 | 121.4656725605 | 31.1446367209 | 806 | 504990 | -92.38 | 12.04 | 559.77 | 0.03 | 2.25 | 1560 |
| 2024-09-20 22:21:42.836 | MS1 | 121.4656673765 | 31.1446351733 | 806 | 504990 | -92.45 | 7.03 | 552.69 | 0.01 | 2.82 | 1574 |

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
| 3222206 | 3 | 121.4699421100 | 31.1535042441 | 239 | 0 | 12 | 21.4 | TDD | 806 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3229865 | 1 | 121.4694806472 | 31.1494550381 | 55 | 10 | 5 | 43.2 | TDD | 408 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3245327 | 4 | 121.4688367699 | 31.1464913047 | 283 | 9 | 9 | 29.2 | TDD | 711 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3258681 | 2 | 121.4732155928 | 31.1483332857 | 171 | 9 | 3 | 40.9 | TDD | 544 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |

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
| 2024-09-20 22:21:31.064 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.179 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.179 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.891 | NREventA3 | measId:2;ServCellPCI:248;Se... |
| 2024-09-20 22:21:38.131 | NRHandoverAttempt | SourcePCI:248;SourceNR-ARFC... |
| 2024-09-20 22:21:38.162 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.174 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.285 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.285 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3229865 | 1 | 16.1629 | 6.7261 | -115.6008 | 10.8972 | 159.9361 | 0.0077 | 0.0100 |
| 2024_09_20 22:00 | 3258681 | 2 | 18.3682 | 7.0810 | -117.6441 | 16.5870 | 158.7031 | 0.0189 | 0.0200 |
| 2024_09_20 22:00 | 3222206 | 3 | 13.1490 | 19.2814 | -117.7304 | 11.9828 | 95.0115 | 0.0120 | 0.0031 |
| 2024_09_20 22:00 | 3245327 | 4 | 11.9555 | 10.1906 | -117.5433 | 11.4963 | 140.4730 | 0.0069 | 0.0071 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415511_AFB13D06 | 504990 | 806 | -88.9 | 504990 | 408 | -91.7 | 504990 | 711 | -98.3 | 504990 | 544 |
| MR_1774415511_E9D53951 | 504990 | 806 | -86.7 | 504990 | 408 | -91.2 | 504990 | 711 | -98.4 | 504990 | 544 |
| MR_1774415511_D014160F | 504990 | 806 | -87.7 | 504990 | 408 | -91.9 | 504990 | 711 | -99.4 | 504990 | 544 |
| MR_1774415511_14F60804 | 504990 | 806 | -86.4 | 504990 | 408 | -89.8 | 504990 | 711 | -98.6 | 504990 | 544 |
| MR_1774415511_6FED087D | 504990 | 806 | -86.2 | 504990 | 408 | -90.8 | 504990 | 711 | -97.7 | 504990 | 544 |

> *... 2개 열 생략 (전체 14열)*

---
