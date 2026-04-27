# Track A 문제 분석 — train[420]~train[429]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[420] ~ train[429] (10개)

## 목차

1. [문제 420: `66ae3088-dc3...`](#420) — single-answer, 정답: C2
2. [문제 421: `3c0cba35-417...`](#421) — single-answer, 정답: C1
3. [문제 422: `c2a160ad-f3b...`](#422) — single-answer, 정답: C13
4. [문제 423: `7b706559-4aa...`](#423) — single-answer, 정답: C5
5. [문제 424: `2d330330-3b1...`](#424) — single-answer, 정답: C1
6. [문제 425: `84534c1a-c14...`](#425) — single-answer, 정답: C16
7. [문제 426: `4ebebe73-154...`](#426) — single-answer, 정답: C6
8. [문제 427: `f1a0d49b-d47...`](#427) — single-answer, 정답: C1
9. [문제 428: `e548909f-fd9...`](#428) — single-answer, 정답: C7
10. [문제 429: `df83aee4-52c...`](#429) — single-answer, 정답: C7

---

### 문제 420: `66ae3088-dc3...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `66ae3088-dc38-428c-80a2-7cb2a61140d9` |
| Tag | **single-answer** |
| 정답 | **C2** |
| C2 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[420] topology](images/train_0420.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3217087_2 by 10 degrees
- `C2`: Insufficient data; more data is needed for judgment. **← 정답**
- `C3`: Increase A3 Offset threshold for 3250397_3
- `C4`: Adjust the azimuth of 3217087_2 by 7 degrees
- `C5`: Add neighbor relationship between 3242658_1 and 3250397_3
- `C6`: Decrease A3 Offset threshold for 3250397_3
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3217087_2
- `C8`: Increase A3 Offset threshold for 3217087_2
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3217087_2
- `C10`: Press down the tilt angle  of 3250397_3 by 10 degrees
- `C11`: Decrease A3 Offset threshold for 3217087_2
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3250397_3
- `C13`: Add neighbor relationship between 3217087_2 and 3250397_3
- `C14`: Adjust the azimuth of 3250397_3 by 50 degrees
- `C15`: Check test server and transmission issues
- `C16`: Decrease transmission power for 3250397_3
- `C17`: Decrease transmission power for 3217087_2
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3250397_3
- `C19`: Lift the tilt angle of 3217087_2 by 10 degrees
- `C20`: Lift the tilt angle  of 3250397_3 by 10 degrees
- `C21`: Increase transmission power for 3217087_2
- `C22`: Increase transmission power for 3250397_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.551 | MS1 | 121.4656643007 | 31.1446335339 | 702 | 504990 | -90.80 | 15.48 | 312.80 | 0.01 | 2.61 | 1566 |
| 2024-09-20 22:21:32.643 | MS1 | 121.4656665893 | 31.1446203255 | 702 | 504990 | -90.07 | 14.29 | 467.73 | 0.14 | 2.18 | 1580 |
| 2024-09-20 22:21:33.701 | MS1 | 121.4656654754 | 31.1446316328 | 702 | 504990 | -87.34 | 16.44 | 306.08 | 0.01 | 2.43 | 1579 |
| 2024-09-20 22:21:34.955 | MS1 | 121.4656605012 | 31.1446379236 | 702 | 504990 | -87.75 | 16.20 | 59.48 | 0.16 | 2.14 | 1583 |
| 2024-09-20 22:21:35.585 | MS1 | 121.4656723982 | 31.1446187790 | 702 | 504990 | -89.13 | 16.16 | 58.93 | 0.13 | 2.01 | 1581 |
| 2024-09-20 22:21:36.968 | MS1 | 121.4656648011 | 31.1446317113 | 702 | 504990 | -88.88 | 15.02 | 91.18 | 0.11 | 2.95 | 1600 |
| 2024-09-20 22:21:37.896 | MS1 | 121.4656776664 | 31.1446361681 | 702 | 504990 | -90.47 | 11.90 | 75.35 | 0.10 | 2.27 | 1593 |
| 2024-09-20 22:21:38.256 | MS1 | 121.4656612927 | 31.1446222049 | 702 | 504990 | -89.15 | 8.43 | 95.08 | 0.12 | 2.18 | 1562 |
| 2024-09-20 22:21:39.473 | MS1 | 121.4656723488 | 31.1446278665 | 702 | 504990 | -89.56 | 11.47 | 87.39 | 0.04 | 2.88 | 1572 |
| 2024-09-20 22:21:40.786 | MS1 | 121.4656769307 | 31.1446327222 | 702 | 504990 | -93.29 | 9.45 | 598.99 | 0.06 | 2.74 | 1573 |
| 2024-09-20 22:21:41.770 | MS1 | 121.4656776160 | 31.1446314639 | 702 | 504990 | -91.75 | 8.14 | 413.99 | 0.14 | 2.44 | 1579 |
| 2024-09-20 22:21:42.243 | MS1 | 121.4656640446 | 31.1446368134 | 702 | 504990 | -93.81 | 9.72 | 522.97 | 0.17 | 2.77 | 1571 |

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
| 3217087 | 2 | 121.4746431856 | 31.1519920960 | 219 | 12 | 11 | 46.9 | TDD | 702 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3240092 | 4 | 121.4753951511 | 31.1522063896 | 272 | 14 | 0 | 30.1 | TDD | 332 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3242658 | 1 | 121.4684902113 | 31.1482236247 | 163 | 7 | 0 | 45.4 | TDD | 934 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3250397 | 3 | 121.4738636910 | 31.1460343586 | 119 | 13 | 3 | 30.8 | TDD | 342 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:31.104 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.126 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.251 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.251 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.930 | NREventA3 | measId:2;ServCellPCI:716;Se... |
| 2024-09-20 22:21:38.170 | NRHandoverAttempt | SourcePCI:716;SourceNR-ARFC... |
| 2024-09-20 22:21:38.201 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.212 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.345 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.345 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3242658 | 1 | 94.2543 | 76.3130 | -115.4603 | 7.1778 | 169.6600 | 0.0036 | 0.0017 |
| 2024_09_19 22:00 | 3217087 | 2 | 78.3034 | 89.3942 | -114.8260 | 6.0909 | 175.1926 | 0.0177 | 0.0045 |
| 2024_09_19 22:00 | 3250397 | 3 | 90.7183 | 92.9739 | -117.0208 | 18.6124 | 85.4561 | 0.0016 | 0.0067 |
| 2024_09_19 22:00 | 3240092 | 4 | 83.8410 | 75.7407 | -115.7744 | 14.3959 | 192.1669 | 0.0059 | 0.0096 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413522_59D23171 | 504990 | 702 | -89.7 | 504990 | 342 | -98.2 | 504990 | 934 | -100.3 | 504990 | 332 |
| MR_1774413522_0B784C34 | 504990 | 702 | -86.0 | 504990 | 342 | -97.2 | 504990 | 934 | -97.7 | 504990 | 332 |
| MR_1774413522_BC884A7A | 504990 | 702 | -85.8 | 504990 | 342 | -97.5 | 504990 | 934 | -101.3 | 504990 | 332 |
| MR_1774413522_85BC8FA5 | 504990 | 702 | -89.3 | 504990 | 342 | -96.8 | 504990 | 934 | -98.0 | 504990 | 332 |
| MR_1774413522_5515C046 | 504990 | 702 | -88.0 | 504990 | 342 | -95.5 | 504990 | 934 | -98.0 | 504990 | 332 |
| MR_1774413522_323DFD9C | 504990 | 702 | -87.1 | 504990 | 342 | -97.3 | 504990 | 934 | -98.3 | 504990 | 332 |
| MR_1774413522_A26434E5 | 504990 | 702 | -88.5 | 504990 | 342 | -94.9 | 504990 | 934 | -100.9 | 504990 | 332 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 421: `3c0cba35-417...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `3c0cba35-417d-4777-ac5b-da52938a456c` |
| Tag | **single-answer** |
| 정답 | **C1** |
| C1 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3235401_2 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[421] topology](images/train_0421.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3235401_2 **← 정답**
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3216101_1
- `C3`: Insufficient data; more data is needed for judgment.
- `C4`: Lift the tilt angle  of 3216101_1 by 10 degrees
- `C5`: Press down the tilt angle  of 3216101_1 by 10 degrees
- `C6`: Decrease A3 Offset threshold for 3216101_1
- `C7`: Add neighbor relationship between 3235401_2 and 3216101_1
- `C8`: Increase A3 Offset threshold for 3216101_1
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3235401_2
- `C10`: Increase transmission power for 3216101_1
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3216101_1
- `C12`: Check test server and transmission issues
- `C13`: Lift the tilt angle of 3235401_2 by 4 degrees
- `C14`: Decrease transmission power for 3216101_1
- `C15`: Increase transmission power for 3235401_2
- `C16`: Increase A3 Offset threshold for 3235401_2
- `C17`: Add neighbor relationship between 3238412_4 and 3216101_1
- `C18`: Adjust the azimuth of 3235401_2 by 8 degrees
- `C19`: Press down the tilt angle of 3235401_2 by 4 degrees
- `C20`: Adjust the azimuth of 3216101_1 by 50 degrees
- `C21`: Decrease A3 Offset threshold for 3235401_2
- `C22`: Decrease transmission power for 3235401_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.279 | MS1 | 121.4656640909 | 31.1446239097 | 985 | 504990 | -86.21 | 12.47 | 586.67 | 0.15 | 2.55 | 1600 |
| 2024-09-20 22:21:32.957 | MS1 | 121.4656729317 | 31.1446290626 | 985 | 504990 | -87.68 | 16.58 | 407.68 | 0.19 | 2.53 | 1578 |
| 2024-09-20 22:21:33.179 | MS1 | 121.4656775568 | 31.1446349631 | 985 | 504990 | -86.19 | 15.57 | 376.19 | 0.15 | 2.29 | 1597 |
| 2024-09-20 22:21:34.196 | MS1 | 121.4656639627 | 31.1446261908 | 985 | 504990 | -91.56 | 14.99 | 61.27 | 0.69 | 2.78 | 516 |
| 2024-09-20 22:21:35.257 | MS1 | 121.4656586958 | 31.1446306817 | 985 | 504990 | -89.23 | 13.41 | 88.63 | 0.63 | 2.73 | 536 |
| 2024-09-20 22:21:36.959 | MS1 | 121.4656683659 | 31.1446250776 | 985 | 504990 | -87.15 | 13.45 | 88.71 | 0.69 | 2.26 | 596 |
| 2024-09-20 22:21:37.142 | MS1 | 121.4656647727 | 31.1446214945 | 985 | 504990 | -91.81 | 7.55 | 58.88 | 0.57 | 2.62 | 595 |
| 2024-09-20 22:21:38.758 | MS1 | 121.4656640081 | 31.1446351609 | 985 | 504990 | -90.04 | 12.57 | 81.37 | 0.57 | 2.15 | 501 |
| 2024-09-20 22:21:39.558 | MS1 | 121.4656597358 | 31.1446196573 | 985 | 504990 | -90.56 | 12.13 | 75.16 | 0.58 | 2.61 | 535 |
| 2024-09-20 22:21:40.498 | MS1 | 121.4656629222 | 31.1446350791 | 985 | 504990 | -91.78 | 10.56 | 473.88 | 0.05 | 2.25 | 1570 |
| 2024-09-20 22:21:41.938 | MS1 | 121.4656622807 | 31.1446231150 | 985 | 504990 | -92.13 | 8.20 | 525.72 | 0.07 | 2.09 | 1560 |
| 2024-09-20 22:21:42.151 | MS1 | 121.4656596397 | 31.1446376270 | 985 | 504990 | -92.74 | 7.11 | 547.53 | 0.03 | 2.41 | 1575 |

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
| 3216101 | 1 | 121.4655440558 | 31.1455471191 | 31 | 10 | 6 | 37.8 | TDD | 1000 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3235401 | 2 | 121.4651601869 | 31.1519044519 | 169 | 2 | 9 | 23.6 | TDD | 985 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3238412 | 4 | 121.4679718955 | 31.1532581821 | 297 | 8 | 7 | 33.4 | TDD | 159 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3278693 | 3 | 121.4708656591 | 31.1532529182 | 332 | 3 | 4 | 28.1 | TDD | 605 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |

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
| 2024-09-20 22:21:31.377 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.394 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.542 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.542 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.250 | NREventA3 | measId:2;ServCellPCI:57;Ser... |
| 2024-09-20 22:21:38.490 | NRHandoverAttempt | SourcePCI:57;SourceNR-ARFCN... |
| 2024-09-20 22:21:38.538 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.551 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.669 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.669 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3216101 | 1 | 10.0249 | 5.1058 | -117.4049 | 11.5894 | 155.6900 | 0.0104 | 0.0105 |
| 2024_09_20 22:00 | 3235401 | 2 | 16.3899 | 12.4384 | -117.8813 | 18.7413 | 110.9088 | 0.0170 | 0.0060 |
| 2024_09_20 22:00 | 3278693 | 3 | 19.2762 | 19.7087 | -114.2253 | 13.4156 | 166.9866 | 0.0178 | 0.0025 |
| 2024_09_20 22:00 | 3238412 | 4 | 14.1234 | 5.7326 | -116.4184 | 18.9913 | 134.5007 | 0.0069 | 0.0122 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415381_AF3D7049 | 504990 | 985 | -92.7 | 504990 | 1000 | -94.8 | 504990 | 159 | -96.2 | 504990 | 605 |
| MR_1774415381_327A3CFE | 504990 | 985 | -93.0 | 504990 | 1000 | -96.0 | 504990 | 159 | -97.5 | 504990 | 605 |
| MR_1774415381_46385536 | 504990 | 985 | -92.1 | 504990 | 1000 | -95.0 | 504990 | 159 | -96.1 | 504990 | 605 |
| MR_1774415381_56382636 | 504990 | 985 | -93.2 | 504990 | 1000 | -92.7 | 504990 | 159 | -97.9 | 504990 | 605 |
| MR_1774415381_D25ADA4A | 504990 | 985 | -90.6 | 504990 | 1000 | -93.0 | 504990 | 159 | -96.9 | 504990 | 605 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 422: `c2a160ad-f3b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `c2a160ad-f3b1-4421-a40f-99776ea833b2` |
| Tag | **single-answer** |
| 정답 | **C13** |
| C13 의미 | Lift the tilt angle  of 3237608_3 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[422] topology](images/train_0422.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Check test server and transmission issues
- `C2`: Adjust the azimuth of 3259128_2 by 22 degrees
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3260644_1
- `C4`: Insufficient data; more data is needed for judgment.
- `C5`: Lift the tilt angle of 3259128_2 by 6 degrees
- `C6`: Increase transmission power for 3260644_1
- `C7`: Decrease transmission power for 3259128_2
- `C8`: Decrease A3 Offset threshold for 3260644_1
- `C9`: Adjust the azimuth of 3237608_3 by 50 degrees
- `C10`: Add neighbor relationship between 3259128_2 and 3260644_1
- `C11`: Decrease A3 Offset threshold for 3259128_2
- `C12`: Add neighbor relationship between 3237608_3 and 3260644_1
- `C13`: Lift the tilt angle  of 3237608_3 by 10 degrees **← 정답**
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3260644_1
- `C15`: Increase A3 Offset threshold for 3259128_2
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3259128_2
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3259128_2
- `C18`: Increase transmission power for 3259128_2
- `C19`: Increase A3 Offset threshold for 3260644_1
- `C20`: Decrease transmission power for 3260644_1
- `C21`: Press down the tilt angle of 3259128_2 by 6 degrees
- `C22`: Press down the tilt angle  of 3237608_3 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.105 | MS1 | 121.4656689498 | 31.1446353541 | 239 | 504990 | -85.43 | 13.18 | 379.50 | 0.03 | 2.34 | 1569 |
| 2024-09-20 22:21:32.634 | MS1 | 121.4656732479 | 31.1446356789 | 239 | 504990 | -86.12 | 13.50 | 384.44 | 0.14 | 2.68 | 1574 |
| 2024-09-20 22:21:33.206 | MS1 | 121.4656728890 | 31.1446320031 | 239 | 504990 | -88.19 | 15.79 | 566.46 | 0.18 | 2.16 | 1588 |
| 2024-09-20 22:21:34.608 | MS1 | 121.4656649585 | 31.1446365469 | 239 | 504990 | -87.23 | 16.78 | 100.86 | 0.12 | 2.95 | 1579 |
| 2024-09-20 22:21:35.677 | MS1 | 121.4656706202 | 31.1446237423 | 239 | 504990 | -85.58 | 15.53 | 63.56 | 0.12 | 2.96 | 1582 |
| 2024-09-20 22:21:36.397 | MS1 | 121.4656693836 | 31.1446275296 | 239 | 504990 | -88.79 | 14.35 | 72.40 | 0.05 | 2.58 | 1561 |
| 2024-09-20 22:21:37.508 | MS1 | 121.4656672069 | 31.1446188807 | 239 | 504990 | -93.34 | 12.29 | 97.51 | 0.05 | 2.59 | 1594 |
| 2024-09-20 22:21:38.770 | MS1 | 121.4656756424 | 31.1446247885 | 239 | 504990 | -93.59 | 7.13 | 57.17 | 0.01 | 2.04 | 1591 |
| 2024-09-20 22:21:39.361 | MS1 | 121.4656714232 | 31.1446319629 | 239 | 504990 | -93.34 | 10.03 | 93.53 | 0.17 | 2.50 | 1591 |
| 2024-09-20 22:21:40.256 | MS1 | 121.4656728799 | 31.1446290710 | 239 | 504990 | -89.20 | 12.95 | 538.59 | 0.10 | 2.32 | 1593 |
| 2024-09-20 22:21:41.319 | MS1 | 121.4656762462 | 31.1446259937 | 239 | 504990 | -93.45 | 7.33 | 320.23 | 0.05 | 2.91 | 1567 |
| 2024-09-20 22:21:42.565 | MS1 | 121.4656684491 | 31.1446355602 | 239 | 504990 | -93.62 | 12.72 | 402.16 | 0.09 | 2.04 | 1565 |

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
| 3237608 | 3 | 121.4649208347 | 31.1547684452 | 296 | 2 | 8 | 47.3 | TDD | 989 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3251360 | 4 | 121.4714702390 | 31.1544887078 | 211 | 7 | 11 | 17.3 | TDD | 138 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3259128 | 2 | 121.4718267670 | 31.1484760607 | 212 | 2 | 12 | 44.6 | TDD | 239 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3260644 | 1 | 121.4715003488 | 31.1442549744 | 100 | 12 | 5 | 42.5 | TDD | 970 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |

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
| 2024-09-20 22:21:31.161 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.176 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.311 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.311 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.047 | NREventA3 | measId:2;ServCellPCI:508;Se... |
| 2024-09-20 22:21:38.287 | NRHandoverAttempt | SourcePCI:508;SourceNR-ARFC... |
| 2024-09-20 22:21:38.336 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.351 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.468 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.468 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3260644 | 1 | 9.8003 | 13.6428 | -116.6170 | 19.7360 | 111.2176 | 0.0081 | 0.0082 |
| 2024_09_20 22:00 | 3259128 | 2 | 85.7492 | 83.3444 | -117.0865 | 10.5390 | 146.2302 | 0.0189 | 0.0072 |
| 2024_09_20 22:00 | 3237608 | 3 | 7.6799 | 19.3151 | -114.4872 | 12.7938 | 81.4709 | 0.0135 | 0.0109 |
| 2024_09_20 22:00 | 3251360 | 4 | 17.4418 | 7.0372 | -114.1767 | 16.2289 | 98.6046 | 0.0058 | 0.0051 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415800_2F82FDF6 | 504990 | 239 | -87.3 | 504990 | 970 | -95.4 | 504990 | 989 | -95.3 | 504990 | 138 |
| MR_1774415800_5DC10C43 | 504990 | 239 | -85.7 | 504990 | 970 | -94.7 | 504990 | 989 | -97.6 | 504990 | 138 |
| MR_1774415800_79058DC5 | 504990 | 239 | -85.8 | 504990 | 970 | -92.9 | 504990 | 989 | -97.0 | 504990 | 138 |
| MR_1774415800_7E2AA828 | 504990 | 239 | -83.9 | 504990 | 970 | -93.8 | 504990 | 989 | -96.7 | 504990 | 138 |
| MR_1774415800_FCB5C56E | 504990 | 239 | -86.8 | 504990 | 970 | -93.1 | 504990 | 989 | -98.4 | 504990 | 138 |
| MR_1774415800_75BE1D20 | 504990 | 239 | -84.9 | 504990 | 970 | -96.3 | 504990 | 989 | -97.0 | 504990 | 138 |
| MR_1774415800_964FE5FB | 504990 | 239 | -86.1 | 504990 | 970 | -94.7 | 504990 | 989 | -96.8 | 504990 | 138 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 423: `7b706559-4aa...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `7b706559-4aa8-4443-9af2-510e4ed5da00` |
| Tag | **single-answer** |
| 정답 | **C5** |
| C5 의미 | Lift the tilt angle  of 3262267_3 by 4 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[423] topology](images/train_0423.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3221415_1
- `C2`: Increase transmission power for 3255824_4
- `C3`: Decrease A3 Offset threshold for 3221415_1
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3255824_4
- `C5`: Lift the tilt angle  of 3262267_3 by 4 degrees **← 정답**
- `C6`: Add neighbor relationship between 3262267_3 and 3221415_1
- `C7`: Increase A3 Offset threshold for 3255824_4
- `C8`: Press down the tilt angle of 3255824_4 by 5 degrees
- `C9`: Adjust the azimuth of 3262267_3 by 49 degrees
- `C10`: Decrease transmission power for 3255824_4
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3221415_1
- `C12`: Adjust the azimuth of 3255824_4 by 8 degrees
- `C13`: Add neighbor relationship between 3255824_4 and 3221415_1
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Decrease transmission power for 3221415_1
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3221415_1
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3255824_4
- `C18`: Check test server and transmission issues
- `C19`: Press down the tilt angle  of 3262267_3 by 4 degrees
- `C20`: Decrease A3 Offset threshold for 3255824_4
- `C21`: Increase transmission power for 3221415_1
- `C22`: Lift the tilt angle of 3255824_4 by 5 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.767 | MS1 | 121.4656685978 | 31.1446244194 | 542 | 504990 | -87.15 | 15.16 | 432.76 | 0.09 | 2.93 | 1577 |
| 2024-09-20 22:21:32.275 | MS1 | 121.4656719595 | 31.1446265248 | 542 | 504990 | -86.03 | 17.43 | 529.40 | 0.13 | 2.91 | 1596 |
| 2024-09-20 22:21:33.543 | MS1 | 121.4656688418 | 31.1446366835 | 542 | 504990 | -87.91 | 13.48 | 320.86 | 0.08 | 2.24 | 1579 |
| 2024-09-20 22:21:34.463 | MS1 | 121.4656709794 | 31.1446341336 | 542 | 504990 | -92.00 | 15.68 | 51.43 | 0.07 | 2.88 | 1576 |
| 2024-09-20 22:21:35.617 | MS1 | 121.4656733728 | 31.1446221650 | 542 | 504990 | -90.83 | 12.92 | 76.98 | 0.13 | 2.33 | 1568 |
| 2024-09-20 22:21:36.941 | MS1 | 121.4656629583 | 31.1446191901 | 542 | 504990 | -91.05 | 13.59 | 66.08 | 0.15 | 2.55 | 1588 |
| 2024-09-20 22:21:37.498 | MS1 | 121.4656715003 | 31.1446274766 | 542 | 504990 | -91.11 | 9.16 | 76.86 | 0.14 | 2.16 | 1570 |
| 2024-09-20 22:21:38.332 | MS1 | 121.4656768186 | 31.1446374993 | 542 | 504990 | -91.58 | 9.30 | 59.70 | 0.07 | 2.35 | 1592 |
| 2024-09-20 22:21:39.354 | MS1 | 121.4656688475 | 31.1446196310 | 542 | 504990 | -92.02 | 11.05 | 90.69 | 0.06 | 2.16 | 1587 |
| 2024-09-20 22:21:40.279 | MS1 | 121.4656609308 | 31.1446306552 | 542 | 504990 | -91.29 | 7.12 | 341.18 | 0.10 | 2.78 | 1596 |
| 2024-09-20 22:21:41.434 | MS1 | 121.4656715232 | 31.1446270182 | 542 | 504990 | -93.82 | 12.35 | 464.30 | 0.12 | 2.70 | 1594 |
| 2024-09-20 22:21:42.162 | MS1 | 121.4656608248 | 31.1446324284 | 542 | 504990 | -90.84 | 10.87 | 471.43 | 0.08 | 2.11 | 1597 |

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
| 3221415 | 1 | 121.4681880318 | 31.1536080534 | 144 | 1 | 12 | 48.4 | TDD | 16 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3230263 | 2 | 121.4708840925 | 31.1457406083 | 347 | 5 | 10 | 34.9 | TDD | 508 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3255824 | 4 | 121.4735174642 | 31.1505202474 | 237 | 3 | 7 | 36.0 | TDD | 542 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3262267 | 3 | 121.4690054012 | 31.1440448995 | 73 | 3 | 12 | 31.0 | TDD | 885 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |

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
| 2024-09-20 22:21:31.176 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.198 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.319 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.319 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.039 | NREventA3 | measId:2;ServCellPCI:88;Ser... |
| 2024-09-20 22:21:38.279 | NRHandoverAttempt | SourcePCI:88;SourceNR-ARFCN... |
| 2024-09-20 22:21:38.320 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.331 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.459 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.459 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3221415 | 1 | 7.7959 | 18.9674 | -116.8673 | 12.3373 | 167.4020 | 0.0080 | 0.0053 |
| 2024_09_20 22:00 | 3230263 | 2 | 19.0568 | 12.6059 | -115.3652 | 15.1998 | 148.0675 | 0.0119 | 0.0073 |
| 2024_09_20 22:00 | 3262267 | 3 | 8.0758 | 11.2593 | -115.5128 | 17.8872 | 150.6918 | 0.0085 | 0.0020 |
| 2024_09_20 22:00 | 3255824 | 4 | 89.4101 | 82.1055 | -114.2919 | 8.2649 | 179.2229 | 0.0085 | 0.0088 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414181_5DFEA253 | 504990 | 542 | -92.2 | 504990 | 16 | -99.5 | 504990 | 885 | -100.6 | 504990 | 508 |
| MR_1774414181_486829D0 | 504990 | 542 | -90.1 | 504990 | 16 | -97.7 | 504990 | 885 | -101.3 | 504990 | 508 |
| MR_1774414181_02DA7C99 | 504990 | 542 | -91.0 | 504990 | 16 | -99.3 | 504990 | 885 | -100.3 | 504990 | 508 |
| MR_1774414181_04D93D8D | 504990 | 542 | -92.7 | 504990 | 16 | -101.5 | 504990 | 885 | -101.2 | 504990 | 508 |
| MR_1774414181_FCF0911F | 504990 | 542 | -91.6 | 504990 | 16 | -97.7 | 504990 | 885 | -101.3 | 504990 | 508 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 424: `2d330330-3b1...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `2d330330-3b17-403a-ac3e-e08eb74de0e2` |
| Tag | **single-answer** |
| 정답 | **C1** |
| C1 의미 | Add neighbor relationship between 3250893_1 and 3211058_3 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[424] topology](images/train_0424.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3250893_1 and 3211058_3 **← 정답**
- `C2`: Insufficient data; more data is needed for judgment.
- `C3`: Decrease A3 Offset threshold for 3250893_1
- `C4`: Decrease A3 Offset threshold for 3211058_3
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3250893_1
- `C6`: Decrease transmission power for 3250893_1
- `C7`: Press down the tilt angle of 3250893_1 by 10 degrees
- `C8`: Add neighbor relationship between 3235835_2 and 3211058_3
- `C9`: Press down the tilt angle  of 3211058_3 by 6 degrees
- `C10`: Adjust the azimuth of 3211058_3 by 31 degrees
- `C11`: Check test server and transmission issues
- `C12`: Increase A3 Offset threshold for 3250893_1
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3250893_1
- `C14`: Lift the tilt angle of 3250893_1 by 10 degrees
- `C15`: Increase transmission power for 3250893_1
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3211058_3
- `C17`: Adjust the azimuth of 3250893_1 by 5 degrees
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3211058_3
- `C19`: Increase transmission power for 3211058_3
- `C20`: Lift the tilt angle  of 3211058_3 by 6 degrees
- `C21`: Decrease transmission power for 3211058_3
- `C22`: Increase A3 Offset threshold for 3211058_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.659 | MS1 | 121.4656680544 | 31.1446268790 | 505 | 504990 | -82.43 | 15.79 | 424.17 | 0.16 | 2.62 | 1565 |
| 2024-09-20 22:21:32.889 | MS1 | 121.4656639208 | 31.1446360844 | 505 | 504990 | -83.41 | 17.14 | 571.68 | 0.20 | 2.42 | 1592 |
| 2024-09-20 22:21:33.960 | MS1 | 121.4656706908 | 31.1446214064 | 505 | 504990 | -82.98 | 13.43 | 573.35 | 0.07 | 2.94 | 1595 |
| 2024-09-20 22:21:34.141 | MS1 | 121.4656627436 | 31.1446325478 | 505 | 504990 | -89.78 | -0.56 | 63.48 | 0.01 | 1.04 | 1582 |
| 2024-09-20 22:21:35.581 | MS1 | 121.4656601554 | 31.1446201418 | 505 | 504990 | -89.35 | -2.08 | 50.17 | 0.18 | 1.02 | 1577 |
| 2024-09-20 22:21:36.577 | MS1 | 121.4656760941 | 31.1446373977 | 505 | 504990 | -88.97 | -3.85 | 64.00 | 0.00 | 1.40 | 1599 |
| 2024-09-20 22:21:37.136 | MS1 | 121.4656759736 | 31.1446351847 | 505 | 504990 | -91.63 | -0.13 | 39.13 | 0.10 | 1.34 | 1568 |
| 2024-09-20 22:21:38.233 | MS1 | 121.4656716025 | 31.1446361992 | 505 | 504990 | -78.76 | 16.70 | 408.05 | 0.14 | 1.31 | 1577 |
| 2024-09-20 22:21:39.515 | MS1 | 121.4656586389 | 31.1446281979 | 505 | 504990 | -77.16 | 17.85 | 476.52 | 0.06 | 1.41 | 1570 |
| 2024-09-20 22:21:40.939 | MS1 | 121.4656688381 | 31.1446219051 | 505 | 504990 | -83.64 | 12.53 | 405.55 | 0.04 | 2.88 | 1572 |
| 2024-09-20 22:21:41.151 | MS1 | 121.4656753194 | 31.1446199106 | 505 | 504990 | -80.26 | 16.72 | 582.37 | 0.06 | 2.72 | 1598 |
| 2024-09-20 22:21:42.782 | MS1 | 121.4656602840 | 31.1446253383 | 505 | 504990 | -76.49 | 14.98 | 582.73 | 0.06 | 2.21 | 1576 |

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
| 3211058 | 3 | 121.4742929676 | 31.1510208226 | 260 | 4 | 9 | 28.9 | TDD | 44 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3235835 | 2 | 121.4712928697 | 31.1460146102 | 250 | 0 | 9 | 42.6 | TDD | 969 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3245459 | 4 | 121.4740768215 | 31.1471855585 | 112 | 8 | 6 | 20.5 | TDD | 745 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3250893 | 1 | 121.4713934513 | 31.1457819443 | 252 | 8 | 7 | 23.7 | TDD | 505 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |

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
| 2024-09-20 22:21:30.839 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.858 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:30.961 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.961 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.738 | NREventA3 | measId:2;ServCellPCI:124;Se... |
| 2024-09-20 22:21:35.738 | NREventA3 | measId:2;ServCellPCI:124;Se... |
| 2024-09-20 22:21:36.738 | NREventA3 | measId:2;ServCellPCI:124;Se... |
| 2024-09-20 22:21:39.238 | NRRRCReestablishAttempt | PCI:124 |
| 2024-09-20 22:21:39.251 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.261 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:39.408 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.408 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3250893 | 1 | 12.8473 | 13.4169 | -115.2669 | 6.2592 | 133.3992 | 0.0017 | 0.1825 |
| 2024_09_20 22:00 | 3235835 | 2 | 12.3411 | 12.4896 | -115.7573 | 18.3780 | 190.8056 | 0.0167 | 0.0013 |
| 2024_09_20 22:00 | 3211058 | 3 | 8.6999 | 14.0629 | -114.4478 | 16.7355 | 160.6828 | 0.0022 | 0.0095 |
| 2024_09_20 22:00 | 3245459 | 4 | 11.1644 | 11.2754 | -117.4399 | 15.3259 | 111.9046 | 0.0128 | 0.0017 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412306_BBCBAC9E | 504990 | 44 | -84.0 | 504990 | 505 | -90.5 | 504990 | 969 | -90.2 | 504990 | 745 |
| MR_1774412306_F67F1C6E | 504990 | 44 | -83.6 | 504990 | 505 | -87.8 | 504990 | 969 | -89.3 | 504990 | 745 |
| MR_1774412306_89DBDA30 | 504990 | 505 | -90.8 | 504990 | 44 | -83.4 | 504990 | 969 | -86.6 | 504990 | 745 |
| MR_1774412306_007BE15B | 504990 | 44 | -85.0 | 504990 | 505 | -88.9 | 504990 | 969 | -87.8 | 504990 | 745 |
| MR_1774412306_2950DAC8 | 504990 | 44 | -84.0 | 504990 | 505 | -91.2 | 504990 | 969 | -88.8 | 504990 | 745 |
| MR_1774412306_4B78CE78 | 504990 | 505 | -91.1 | 504990 | 44 | -82.5 | 504990 | 969 | -86.8 | 504990 | 745 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 425: `84534c1a-c14...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `84534c1a-c14b-4fad-951e-6e2e91ace32d` |
| Tag | **single-answer** |
| 정답 | **C16** |
| C16 의미 | Decrease A3 Offset threshold for 3235950_3 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[425] topology](images/train_0425.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle  of 3220669_1 by 10 degrees
- `C2`: Decrease transmission power for 3220669_1
- `C3`: Add neighbor relationship between 3215447_2 and 3220669_1
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3235950_3
- `C5`: Adjust the azimuth of 3220669_1 by 24 degrees
- `C6`: Press down the tilt angle  of 3220669_1 by 10 degrees
- `C7`: Add neighbor relationship between 3235950_3 and 3220669_1
- `C8`: Adjust the azimuth of 3235950_3 by 50 degrees
- `C9`: Decrease transmission power for 3235950_3
- `C10`: Insufficient data; more data is needed for judgment.
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3220669_1
- `C12`: Increase transmission power for 3235950_3
- `C13`: Increase A3 Offset threshold for 3220669_1
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3220669_1
- `C15`: Decrease A3 Offset threshold for 3220669_1
- `C16`: Decrease A3 Offset threshold for 3235950_3 **← 정답**
- `C17`: Increase A3 Offset threshold for 3235950_3
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3235950_3
- `C19`: Press down the tilt angle of 3235950_3 by 10 degrees
- `C20`: Lift the tilt angle of 3235950_3 by 10 degrees
- `C21`: Increase transmission power for 3220669_1
- `C22`: Check test server and transmission issues

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.896 | MS1 | 121.4656636267 | 31.1446309276 | 962 | 504990 | -78.96 | 16.79 | 345.91 | 0.20 | 2.17 | 1593 |
| 2024-09-20 22:21:32.960 | MS1 | 121.4656628028 | 31.1446303170 | 962 | 504990 | -84.50 | 17.07 | 504.13 | 0.05 | 2.53 | 1596 |
| 2024-09-20 22:21:33.898 | MS1 | 121.4656602221 | 31.1446292044 | 962 | 504990 | -82.79 | 15.48 | 300.72 | 0.08 | 2.44 | 1560 |
| 2024-09-20 22:21:34.744 | MS1 | 121.4656605517 | 31.1446357857 | 962 | 504990 | -89.88 | -3.67 | 37.71 | 0.04 | 1.08 | 1578 |
| 2024-09-20 22:21:35.702 | MS1 | 121.4656725155 | 31.1446342387 | 962 | 504990 | -90.31 | -2.55 | 72.96 | 0.18 | 1.48 | 1583 |
| 2024-09-20 22:21:36.312 | MS1 | 121.4656582203 | 31.1446308086 | 962 | 504990 | -84.35 | -1.23 | 62.99 | 0.02 | 1.21 | 1577 |
| 2024-09-20 22:21:37.777 | MS1 | 121.4656754253 | 31.1446350708 | 962 | 504990 | -88.21 | -1.39 | 46.12 | 0.11 | 1.47 | 1579 |
| 2024-09-20 22:21:38.986 | MS1 | 121.4656747209 | 31.1446235180 | 962 | 504990 | -92.48 | -3.21 | 27.47 | 0.01 | 1.25 | 1582 |
| 2024-09-20 22:21:39.252 | MS1 | 121.4656738020 | 31.1446353973 | 528 | 504990 | -79.49 | 17.73 | 207.14 | 0.18 | 1.27 | 1579 |
| 2024-09-20 22:21:40.860 | MS1 | 121.4656746419 | 31.1446256114 | 528 | 504990 | -76.60 | 16.91 | 465.38 | 0.06 | 2.21 | 1600 |
| 2024-09-20 22:21:41.865 | MS1 | 121.4656623176 | 31.1446290042 | 528 | 504990 | -80.31 | 14.01 | 507.36 | 0.02 | 2.06 | 1582 |
| 2024-09-20 22:21:42.638 | MS1 | 121.4656684813 | 31.1446249944 | 528 | 504990 | -79.23 | 14.89 | 531.50 | 0.13 | 2.20 | 1568 |

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
| 3215447 | 2 | 121.4708152445 | 31.1539755179 | 153 | 8 | 12 | 18.9 | TDD | 9 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3220669 | 1 | 121.4704211456 | 31.1557372029 | 176 | 13 | 12 | 30.2 | TDD | 528 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3225785 | 4 | 121.4698271062 | 31.1557754139 | 237 | 3 | 4 | 16.9 | TDD | 186 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3235950 | 3 | 121.4713162572 | 31.1557252207 | 85 | 8 | 10 | 45.1 | TDD | 962 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |

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
| 2024-09-20 22:21:31.540 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.565 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.697 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.697 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.350 | NREventA3 | measId:2;ServCellPCI:696;Se... |
| 2024-09-20 22:21:38.590 | NRHandoverAttempt | SourcePCI:696;SourceNR-ARFC... |
| 2024-09-20 22:21:38.626 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.641 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.785 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.785 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3220669 | 1 | 12.7351 | 15.4670 | -115.1053 | 6.9362 | 194.5550 | 0.0041 | 0.0060 |
| 2024_09_20 22:00 | 3215447 | 2 | 12.6073 | 15.9172 | -116.9318 | 8.3599 | 177.3484 | 0.0052 | 0.0109 |
| 2024_09_20 22:00 | 3235950 | 3 | 15.0354 | 10.2393 | -116.5413 | 11.3744 | 175.5235 | 0.0046 | 0.1881 |
| 2024_09_20 22:00 | 3225785 | 4 | 10.5705 | 19.6599 | -117.5749 | 8.7686 | 150.9156 | 0.0156 | 0.0083 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414180_25A0E8D6 | 504990 | 962 | -88.5 | 504990 | 528 | -83.9 | 504990 | 9 | -86.8 | 504990 | 186 |
| MR_1774414180_0FF4F93F | 504990 | 962 | -90.3 | 504990 | 528 | -85.7 | 504990 | 9 | -88.2 | 504990 | 186 |
| MR_1774414180_3381C352 | 504990 | 962 | -89.7 | 504990 | 528 | -83.7 | 504990 | 9 | -86.8 | 504990 | 186 |
| MR_1774414180_378613DD | 504990 | 962 | -89.4 | 504990 | 528 | -84.2 | 504990 | 9 | -88.1 | 504990 | 186 |
| MR_1774414180_9157835E | 504990 | 528 | -85.5 | 504990 | 962 | -90.8 | 504990 | 9 | -90.3 | 504990 | 186 |
| MR_1774414180_7B48B577 | 504990 | 962 | -91.5 | 504990 | 528 | -86.8 | 504990 | 9 | -89.2 | 504990 | 186 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 426: `4ebebe73-154...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `4ebebe73-1546-4252-afec-521e143234dd` |
| Tag | **single-answer** |
| 정답 | **C6** |
| C6 의미 | Add neighbor relationship between 3248698_1 and 3264017_3 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[426] topology](images/train_0426.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3248698_1
- `C2`: Press down the tilt angle  of 3264017_3 by 4 degrees
- `C3`: Check test server and transmission issues
- `C4`: Insufficient data; more data is needed for judgment.
- `C5`: Adjust the azimuth of 3248698_1 by 50 degrees
- `C6`: Add neighbor relationship between 3248698_1 and 3264017_3 **← 정답**
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3264017_3
- `C8`: Increase A3 Offset threshold for 3264017_3
- `C9`: Adjust the azimuth of 3264017_3 by 19 degrees
- `C10`: Increase transmission power for 3264017_3
- `C11`: Lift the tilt angle  of 3264017_3 by 4 degrees
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3264017_3
- `C13`: Decrease A3 Offset threshold for 3264017_3
- `C14`: Lift the tilt angle of 3248698_1 by 3 degrees
- `C15`: Decrease A3 Offset threshold for 3248698_1
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3248698_1
- `C17`: Decrease transmission power for 3264017_3
- `C18`: Add neighbor relationship between 3279725_4 and 3264017_3
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3248698_1
- `C20`: Press down the tilt angle of 3248698_1 by 3 degrees
- `C21`: Increase transmission power for 3248698_1
- `C22`: Increase A3 Offset threshold for 3248698_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.687 | MS1 | 121.4656625026 | 31.1446334371 | 980 | 504990 | -80.61 | 14.27 | 367.27 | 0.01 | 2.20 | 1581 |
| 2024-09-20 22:21:32.502 | MS1 | 121.4656732237 | 31.1446278087 | 980 | 504990 | -78.95 | 17.38 | 510.98 | 0.01 | 2.08 | 1590 |
| 2024-09-20 22:21:33.685 | MS1 | 121.4656737626 | 31.1446228669 | 980 | 504990 | -82.59 | 13.53 | 466.41 | 0.12 | 2.48 | 1597 |
| 2024-09-20 22:21:34.404 | MS1 | 121.4656675327 | 31.1446327577 | 980 | 504990 | -91.47 | -2.91 | 61.22 | 0.01 | 1.25 | 1600 |
| 2024-09-20 22:21:35.214 | MS1 | 121.4656608413 | 31.1446328084 | 980 | 504990 | -93.08 | -2.61 | 33.93 | 0.18 | 1.06 | 1588 |
| 2024-09-20 22:21:36.638 | MS1 | 121.4656604120 | 31.1446271087 | 980 | 504990 | -88.71 | -2.86 | 46.14 | 0.05 | 1.21 | 1599 |
| 2024-09-20 22:21:37.594 | MS1 | 121.4656660035 | 31.1446305775 | 980 | 504990 | -92.71 | -3.09 | 36.85 | 0.01 | 1.04 | 1590 |
| 2024-09-20 22:21:38.209 | MS1 | 121.4656756482 | 31.1446371938 | 980 | 504990 | -79.75 | 15.56 | 378.50 | 0.14 | 1.23 | 1573 |
| 2024-09-20 22:21:39.282 | MS1 | 121.4656748437 | 31.1446287752 | 980 | 504990 | -83.00 | 15.34 | 550.81 | 0.12 | 1.41 | 1581 |
| 2024-09-20 22:21:40.712 | MS1 | 121.4656719866 | 31.1446191719 | 980 | 504990 | -78.01 | 17.31 | 576.93 | 0.09 | 2.79 | 1587 |
| 2024-09-20 22:21:41.959 | MS1 | 121.4656709234 | 31.1446208931 | 980 | 504990 | -76.09 | 16.73 | 425.11 | 0.13 | 2.62 | 1579 |
| 2024-09-20 22:21:42.698 | MS1 | 121.4656678326 | 31.1446379090 | 980 | 504990 | -80.51 | 15.23 | 465.84 | 0.11 | 2.73 | 1589 |

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
| 3248698 | 1 | 121.4757934905 | 31.1545917137 | 36 | 2 | 12 | 17.9 | TDD | 980 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3249522 | 2 | 121.4737777308 | 31.1550174619 | 113 | 7 | 6 | 42.9 | TDD | 817 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3264017 | 3 | 121.4700120781 | 31.1526816242 | 186 | 2 | 6 | 31.0 | TDD | 459 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3279725 | 4 | 121.4681421790 | 31.1505386289 | 80 | 3 | 5 | 37.8 | TDD | 220 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:31.120 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.145 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.283 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.283 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.971 | NREventA3 | measId:2;ServCellPCI:848;Se... |
| 2024-09-20 22:21:35.971 | NREventA3 | measId:2;ServCellPCI:848;Se... |
| 2024-09-20 22:21:36.971 | NREventA3 | measId:2;ServCellPCI:848;Se... |
| 2024-09-20 22:21:39.471 | NRRRCReestablishAttempt | PCI:848 |
| 2024-09-20 22:21:39.485 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.497 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:39.639 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.639 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3248698 | 1 | 16.1547 | 18.1282 | -116.2929 | 12.8225 | 154.2808 | 0.0072 | 0.1334 |
| 2024_09_20 22:00 | 3249522 | 2 | 15.3803 | 5.8743 | -117.0666 | 16.3347 | 156.6416 | 0.0074 | 0.0025 |
| 2024_09_20 22:00 | 3264017 | 3 | 13.0170 | 14.6141 | -114.5129 | 14.3035 | 171.7012 | 0.0141 | 0.0166 |
| 2024_09_20 22:00 | 3279725 | 4 | 17.8875 | 19.6092 | -115.1705 | 17.0261 | 131.6546 | 0.0088 | 0.0121 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416097_B9525F2E | 504990 | 459 | -84.5 | 504990 | 980 | -92.4 | 504990 | 220 | -95.7 | 504990 | 817 |
| MR_1774416097_4A0CF6B1 | 504990 | 459 | -84.9 | 504990 | 980 | -92.0 | 504990 | 220 | -92.8 | 504990 | 817 |
| MR_1774416097_8008AEBA | 504990 | 459 | -86.6 | 504990 | 980 | -92.1 | 504990 | 220 | -93.7 | 504990 | 817 |
| MR_1774416097_B1655F1E | 504990 | 980 | -90.4 | 504990 | 459 | -86.8 | 504990 | 220 | -95.0 | 504990 | 817 |
| MR_1774416097_ECAEC4B3 | 504990 | 459 | -85.9 | 504990 | 980 | -91.9 | 504990 | 220 | -94.8 | 504990 | 817 |
| MR_1774416097_BBC6563B | 504990 | 459 | -86.7 | 504990 | 980 | -89.8 | 504990 | 220 | -95.7 | 504990 | 817 |
| MR_1774416097_6C006B30 | 504990 | 980 | -90.5 | 504990 | 459 | -87.6 | 504990 | 220 | -93.5 | 504990 | 817 |
| MR_1774416097_00FB5D52 | 504990 | 459 | -85.0 | 504990 | 980 | -91.2 | 504990 | 220 | -92.4 | 504990 | 817 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 427: `f1a0d49b-d47...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `f1a0d49b-d471-4db8-baaf-ec0c33fb6baf` |
| Tag | **single-answer** |
| 정답 | **C1** |
| C1 의미 | Add neighbor relationship between 3243493_2 and 3270477_1 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[427] topology](images/train_0427.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3243493_2 and 3270477_1 **← 정답**
- `C2`: Increase transmission power for 3270477_1
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3270477_1
- `C4`: Decrease A3 Offset threshold for 3243493_2
- `C5`: Increase transmission power for 3243493_2
- `C6`: Check test server and transmission issues
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3270477_1
- `C8`: Press down the tilt angle  of 3270477_1 by 3 degrees
- `C9`: Add neighbor relationship between 3251268_3 and 3270477_1
- `C10`: Press down the tilt angle of 3243493_2 by 9 degrees
- `C11`: Decrease transmission power for 3243493_2
- `C12`: Lift the tilt angle of 3243493_2 by 9 degrees
- `C13`: Increase A3 Offset threshold for 3270477_1
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Adjust the azimuth of 3243493_2 by 47 degrees
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3243493_2
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3243493_2
- `C18`: Increase A3 Offset threshold for 3243493_2
- `C19`: Lift the tilt angle  of 3270477_1 by 3 degrees
- `C20`: Decrease A3 Offset threshold for 3270477_1
- `C21`: Decrease transmission power for 3270477_1
- `C22`: Adjust the azimuth of 3270477_1 by 19 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.272 | MS1 | 121.4656694551 | 31.1446379924 | 42 | 504990 | -75.21 | 14.68 | 588.92 | 0.01 | 2.29 | 1594 |
| 2024-09-20 22:21:32.472 | MS1 | 121.4656671711 | 31.1446326158 | 42 | 504990 | -75.70 | 15.30 | 556.11 | 0.11 | 2.56 | 1579 |
| 2024-09-20 22:21:33.654 | MS1 | 121.4656741402 | 31.1446243544 | 42 | 504990 | -75.46 | 14.54 | 567.36 | 0.02 | 2.95 | 1590 |
| 2024-09-20 22:21:34.869 | MS1 | 121.4656684056 | 31.1446231537 | 42 | 504990 | -93.36 | -3.12 | 45.58 | 0.11 | 1.19 | 1589 |
| 2024-09-20 22:21:35.756 | MS1 | 121.4656759734 | 31.1446296697 | 42 | 504990 | -93.31 | -0.44 | 46.07 | 0.01 | 1.35 | 1599 |
| 2024-09-20 22:21:36.569 | MS1 | 121.4656653266 | 31.1446185332 | 42 | 504990 | -93.03 | -3.60 | 50.62 | 0.08 | 1.30 | 1595 |
| 2024-09-20 22:21:37.211 | MS1 | 121.4656730462 | 31.1446254910 | 42 | 504990 | -91.97 | -2.23 | 35.50 | 0.11 | 1.10 | 1581 |
| 2024-09-20 22:21:38.494 | MS1 | 121.4656709996 | 31.1446315573 | 42 | 504990 | -84.63 | 12.07 | 483.47 | 0.13 | 1.36 | 1600 |
| 2024-09-20 22:21:39.558 | MS1 | 121.4656740597 | 31.1446331604 | 42 | 504990 | -78.72 | 12.36 | 585.69 | 0.18 | 1.28 | 1573 |
| 2024-09-20 22:21:40.989 | MS1 | 121.4656623532 | 31.1446365668 | 42 | 504990 | -84.48 | 14.01 | 368.65 | 0.11 | 2.44 | 1581 |
| 2024-09-20 22:21:41.805 | MS1 | 121.4656638660 | 31.1446232740 | 42 | 504990 | -75.70 | 16.25 | 359.97 | 0.18 | 2.93 | 1573 |
| 2024-09-20 22:21:42.882 | MS1 | 121.4656592235 | 31.1446335481 | 42 | 504990 | -83.98 | 16.41 | 501.87 | 0.10 | 2.39 | 1579 |

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
| 3243493 | 2 | 121.4702326222 | 31.1456565816 | 208 | 6 | 4 | 26.3 | TDD | 42 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3251268 | 3 | 121.4648100895 | 31.1474149808 | 18 | 11 | 4 | 35.0 | TDD | 235 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3262485 | 4 | 121.4650455824 | 31.1504911241 | 144 | 3 | 2 | 27.3 | TDD | 581 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3270477 | 1 | 121.4749017877 | 31.1543674590 | 200 | 2 | 5 | 30.1 | TDD | 317 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |

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
| 2024-09-20 22:21:31.556 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.579 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.710 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.710 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.425 | NREventA3 | measId:2;ServCellPCI:270;Se... |
| 2024-09-20 22:21:36.425 | NREventA3 | measId:2;ServCellPCI:270;Se... |
| 2024-09-20 22:21:37.425 | NREventA3 | measId:2;ServCellPCI:270;Se... |
| 2024-09-20 22:21:39.925 | NRRRCReestablishAttempt | PCI:270 |
| 2024-09-20 22:21:39.943 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.958 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:40.099 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:40.099 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3270477 | 1 | 7.8981 | 17.9808 | -117.4646 | 11.4903 | 117.9548 | 0.0147 | 0.0085 |
| 2024_09_20 22:00 | 3243493 | 2 | 19.9427 | 8.3387 | -117.6713 | 14.9216 | 82.6285 | 0.0195 | 0.1215 |
| 2024_09_20 22:00 | 3251268 | 3 | 16.6872 | 8.8952 | -115.6717 | 13.8090 | 94.3726 | 0.0058 | 0.0052 |
| 2024_09_20 22:00 | 3262485 | 4 | 9.5069 | 6.8004 | -114.0646 | 17.9551 | 186.8317 | 0.0095 | 0.0156 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414759_38FB8F6A | 504990 | 42 | -93.6 | 504990 | 317 | -90.5 | 504990 | 235 | -98.6 | 504990 | 581 |
| MR_1774414759_E754E17E | 504990 | 42 | -92.4 | 504990 | 317 | -87.0 | 504990 | 235 | -96.2 | 504990 | 581 |
| MR_1774414759_C670AEC8 | 504990 | 42 | -91.5 | 504990 | 317 | -89.8 | 504990 | 235 | -95.4 | 504990 | 581 |
| MR_1774414759_1542CF0B | 504990 | 42 | -92.8 | 504990 | 317 | -89.3 | 504990 | 235 | -97.6 | 504990 | 581 |
| MR_1774414759_907C3035 | 504990 | 317 | -87.6 | 504990 | 42 | -92.1 | 504990 | 235 | -97.4 | 504990 | 581 |
| MR_1774414759_40C59B9D | 504990 | 317 | -90.6 | 504990 | 42 | -94.4 | 504990 | 235 | -96.2 | 504990 | 581 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 428: `e548909f-fd9...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `e548909f-fd94-45aa-908f-72a2d0b4d941` |
| Tag | **single-answer** |
| 정답 | **C7** |
| C7 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[428] topology](images/train_0428.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3276087_4
- `C2`: Adjust the azimuth of 3278792_1 by 50 degrees
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3278792_1
- `C4`: Decrease transmission power for 3278792_1
- `C5`: Increase transmission power for 3276087_4
- `C6`: Adjust the azimuth of 3276087_4 by 50 degrees
- `C7`: Insufficient data; more data is needed for judgment. **← 정답**
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3278792_1
- `C9`: Lift the tilt angle  of 3276087_4 by 7 degrees
- `C10`: Decrease A3 Offset threshold for 3278792_1
- `C11`: Decrease transmission power for 3276087_4
- `C12`: Increase transmission power for 3278792_1
- `C13`: Add neighbor relationship between 3279371_2 and 3276087_4
- `C14`: Check test server and transmission issues
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3276087_4
- `C16`: Press down the tilt angle of 3278792_1 by 10 degrees
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3276087_4
- `C18`: Lift the tilt angle of 3278792_1 by 10 degrees
- `C19`: Add neighbor relationship between 3278792_1 and 3276087_4
- `C20`: Increase A3 Offset threshold for 3278792_1
- `C21`: Press down the tilt angle  of 3276087_4 by 7 degrees
- `C22`: Decrease A3 Offset threshold for 3276087_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.353 | MS1 | 121.4656696489 | 31.1446311625 | 311 | 504990 | -86.30 | 14.22 | 431.98 | 0.19 | 2.97 | 1598 |
| 2024-09-20 22:21:32.919 | MS1 | 121.4656679595 | 31.1446204099 | 311 | 504990 | -85.90 | 13.05 | 429.53 | 0.09 | 2.05 | 1592 |
| 2024-09-20 22:21:33.975 | MS1 | 121.4656602036 | 31.1446234565 | 311 | 504990 | -91.36 | 15.91 | 498.52 | 0.02 | 2.76 | 1593 |
| 2024-09-20 22:21:34.829 | MS1 | 121.4656755973 | 31.1446345267 | 311 | 504990 | -91.41 | 15.70 | 86.70 | 0.19 | 2.77 | 1577 |
| 2024-09-20 22:21:35.837 | MS1 | 121.4656654123 | 31.1446307263 | 311 | 504990 | -89.94 | 16.93 | 65.24 | 0.03 | 2.63 | 1575 |
| 2024-09-20 22:21:36.270 | MS1 | 121.4656679371 | 31.1446317888 | 311 | 504990 | -86.90 | 13.47 | 73.23 | 0.17 | 2.85 | 1569 |
| 2024-09-20 22:21:37.889 | MS1 | 121.4656714564 | 31.1446324160 | 311 | 504990 | -90.32 | 12.43 | 50.74 | 0.08 | 2.62 | 1586 |
| 2024-09-20 22:21:38.718 | MS1 | 121.4656635484 | 31.1446378692 | 311 | 504990 | -92.54 | 9.75 | 79.35 | 0.11 | 2.82 | 1574 |
| 2024-09-20 22:21:39.825 | MS1 | 121.4656691693 | 31.1446322318 | 311 | 504990 | -92.46 | 12.51 | 84.36 | 0.03 | 2.86 | 1566 |
| 2024-09-20 22:21:40.936 | MS1 | 121.4656685269 | 31.1446296842 | 311 | 504990 | -90.32 | 7.31 | 477.20 | 0.19 | 2.55 | 1587 |
| 2024-09-20 22:21:41.465 | MS1 | 121.4656712916 | 31.1446226194 | 311 | 504990 | -89.63 | 11.57 | 341.82 | 0.09 | 2.54 | 1560 |
| 2024-09-20 22:21:42.864 | MS1 | 121.4656775192 | 31.1446227869 | 311 | 504990 | -90.10 | 10.48 | 593.40 | 0.16 | 2.47 | 1562 |

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
| 3250592 | 3 | 121.4655786734 | 31.1473761706 | 152 | 14 | 0 | 34.7 | TDD | 870 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3276087 | 4 | 121.4663952058 | 31.1557969772 | 341 | 5 | 10 | 34.4 | TDD | 639 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3278792 | 1 | 121.4695018332 | 31.1472230581 | 311 | 12 | 9 | 38.3 | TDD | 311 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3279371 | 2 | 121.4694050022 | 31.1488556481 | 46 | 11 | 0 | 16.9 | TDD | 966 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:30.996 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.017 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.128 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.128 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.812 | NREventA3 | measId:2;ServCellPCI:620;Se... |
| 2024-09-20 22:21:38.052 | NRHandoverAttempt | SourcePCI:620;SourceNR-ARFC... |
| 2024-09-20 22:21:38.083 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.098 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.231 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.231 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3278792 | 1 | 75.4339 | 81.9789 | -114.9103 | 7.3186 | 125.0374 | 0.0026 | 0.0068 |
| 2024_09_19 22:00 | 3279371 | 2 | 87.6099 | 87.8468 | -115.7020 | 8.3517 | 92.4831 | 0.0083 | 0.0051 |
| 2024_09_19 22:00 | 3250592 | 3 | 93.2885 | 86.9018 | -114.4899 | 19.9279 | 91.1384 | 0.0160 | 0.0061 |
| 2024_09_19 22:00 | 3276087 | 4 | 79.7759 | 83.0127 | -116.3159 | 6.1731 | 89.4829 | 0.0166 | 0.0088 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414467_1776EA26 | 504990 | 311 | -91.1 | 504990 | 639 | -97.7 | 504990 | 966 | -106.4 | 504990 | 870 |
| MR_1774414467_49F09FD0 | 504990 | 311 | -91.3 | 504990 | 639 | -97.8 | 504990 | 966 | -104.0 | 504990 | 870 |
| MR_1774414467_518ECA55 | 504990 | 311 | -90.5 | 504990 | 639 | -99.6 | 504990 | 966 | -105.1 | 504990 | 870 |
| MR_1774414467_3C24F3E0 | 504990 | 311 | -91.0 | 504990 | 639 | -97.3 | 504990 | 966 | -103.8 | 504990 | 870 |
| MR_1774414467_671A786B | 504990 | 311 | -93.2 | 504990 | 639 | -99.4 | 504990 | 966 | -106.5 | 504990 | 870 |
| MR_1774414467_6E3AB34E | 504990 | 311 | -92.7 | 504990 | 639 | -99.2 | 504990 | 966 | -105.4 | 504990 | 870 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 429: `df83aee4-52c...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `df83aee4-52cb-482c-bd3d-ea06ab3b5648` |
| Tag | **single-answer** |
| 정답 | **C7** |
| C7 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[429] topology](images/train_0429.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3222912_1 by 5 degrees
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3263734_3
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3222912_1
- `C4`: Add neighbor relationship between 3222912_1 and 3263734_3
- `C5`: Adjust the azimuth of 3263734_3 by 50 degrees
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3222912_1
- `C7`: Check test server and transmission issues **← 정답**
- `C8`: Adjust the azimuth of 3222912_1 by 7 degrees
- `C9`: Insufficient data; more data is needed for judgment.
- `C10`: Decrease A3 Offset threshold for 3222912_1
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3263734_3
- `C12`: Increase A3 Offset threshold for 3222912_1
- `C13`: Lift the tilt angle of 3222912_1 by 5 degrees
- `C14`: Decrease transmission power for 3222912_1
- `C15`: Increase transmission power for 3263734_3
- `C16`: Lift the tilt angle  of 3263734_3 by 2 degrees
- `C17`: Add neighbor relationship between 3232171_4 and 3263734_3
- `C18`: Increase A3 Offset threshold for 3263734_3
- `C19`: Decrease transmission power for 3263734_3
- `C20`: Press down the tilt angle  of 3263734_3 by 2 degrees
- `C21`: Increase transmission power for 3222912_1
- `C22`: Decrease A3 Offset threshold for 3263734_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.509 | MS1 | 121.4656673580 | 31.1446355947 | 224 | 504990 | -87.10 | 17.45 | 332.03 | 0.07 | 2.52 | 1595 |
| 2024-09-20 22:21:32.947 | MS1 | 121.4656641123 | 31.1446228102 | 224 | 504990 | -88.80 | 15.98 | 473.80 | 0.14 | 2.24 | 1595 |
| 2024-09-20 22:21:33.322 | MS1 | 121.4656593041 | 31.1446193211 | 224 | 504990 | -88.81 | 14.93 | 425.08 | 0.07 | 2.27 | 1596 |
| 2024-09-20 22:21:34.901 | MS1 | 121.4656758558 | 31.1446191749 | 224 | 504990 | -86.10 | 15.76 | 86.53 | 0.15 | 2.48 | 444 |
| 2024-09-20 22:21:35.585 | MS1 | 121.4656603507 | 31.1446373204 | 224 | 504990 | -91.56 | 14.27 | 86.02 | 0.15 | 2.67 | 365 |
| 2024-09-20 22:21:36.515 | MS1 | 121.4656640951 | 31.1446357790 | 224 | 504990 | -87.44 | 17.39 | 70.17 | 0.19 | 2.52 | 413 |
| 2024-09-20 22:21:37.552 | MS1 | 121.4656739444 | 31.1446225538 | 224 | 504990 | -89.29 | 7.76 | 55.74 | 0.09 | 2.87 | 387 |
| 2024-09-20 22:21:38.892 | MS1 | 121.4656595637 | 31.1446345573 | 224 | 504990 | -92.38 | 8.77 | 85.61 | 0.16 | 2.10 | 439 |
| 2024-09-20 22:21:39.176 | MS1 | 121.4656700697 | 31.1446200796 | 224 | 504990 | -90.85 | 7.25 | 74.05 | 0.01 | 2.15 | 481 |
| 2024-09-20 22:21:40.673 | MS1 | 121.4656639445 | 31.1446264471 | 224 | 504990 | -93.26 | 9.07 | 431.80 | 0.00 | 2.61 | 1572 |
| 2024-09-20 22:21:41.632 | MS1 | 121.4656586427 | 31.1446280016 | 224 | 504990 | -89.50 | 7.53 | 316.94 | 0.14 | 2.74 | 1567 |
| 2024-09-20 22:21:42.716 | MS1 | 121.4656774889 | 31.1446372588 | 224 | 504990 | -93.89 | 7.50 | 388.60 | 0.12 | 2.39 | 1598 |

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
| 3210512 | 2 | 121.4736458949 | 31.1511754713 | 27 | 4 | 12 | 16.2 | TDD | 409 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3222912 | 1 | 121.4713655767 | 31.1492711092 | 219 | 2 | 1 | 35.2 | TDD | 224 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3232171 | 4 | 121.4683565454 | 31.1487441486 | 31 | 7 | 12 | 21.1 | TDD | 712 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3263734 | 3 | 121.4670462526 | 31.1546599679 | 83 | 1 | 11 | 28.8 | TDD | 27 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:30.864 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.879 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.001 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.001 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.669 | NREventA3 | measId:2;ServCellPCI:998;Se... |
| 2024-09-20 22:21:37.909 | NRHandoverAttempt | SourcePCI:998;SourceNR-ARFC... |
| 2024-09-20 22:21:37.946 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.956 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.101 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.101 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3222912 | 1 | 13.9915 | 9.6576 | -116.3194 | 16.2887 | 169.5696 | 0.0070 | 0.0119 |
| 2024_09_20 22:00 | 3210512 | 2 | 8.9172 | 13.7715 | -114.7550 | 9.2750 | 155.1585 | 0.0042 | 0.0137 |
| 2024_09_20 22:00 | 3263734 | 3 | 18.0645 | 12.4453 | -114.2529 | 9.4020 | 192.1648 | 0.0187 | 0.0034 |
| 2024_09_20 22:00 | 3232171 | 4 | 11.3356 | 14.0808 | -117.6306 | 18.6308 | 98.5648 | 0.0026 | 0.0092 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414315_A273726B | 504990 | 224 | -85.1 | 504990 | 27 | -86.4 | 504990 | 712 | -98.8 | 504990 | 409 |
| MR_1774414315_A27947AF | 504990 | 224 | -84.2 | 504990 | 27 | -89.1 | 504990 | 712 | -100.9 | 504990 | 409 |
| MR_1774414315_15D00FDD | 504990 | 224 | -85.9 | 504990 | 27 | -87.5 | 504990 | 712 | -98.2 | 504990 | 409 |
| MR_1774414315_8F4B0183 | 504990 | 224 | -84.6 | 504990 | 27 | -88.1 | 504990 | 712 | -98.3 | 504990 | 409 |
| MR_1774414315_4241CB9B | 504990 | 224 | -85.6 | 504990 | 27 | -86.6 | 504990 | 712 | -100.3 | 504990 | 409 |
| MR_1774414315_0A23D786 | 504990 | 224 | -87.2 | 504990 | 27 | -89.0 | 504990 | 712 | -98.4 | 504990 | 409 |
| MR_1774414315_913072E0 | 504990 | 224 | -86.9 | 504990 | 27 | -88.7 | 504990 | 712 | -99.3 | 504990 | 409 |

> *... 2개 열 생략 (전체 14열)*

---
