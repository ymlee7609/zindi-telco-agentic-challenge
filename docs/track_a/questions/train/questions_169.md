# Track A 문제 분석 — train[1680]~train[1689]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[1680] ~ train[1689] (10개)

## 목차

1. [문제 1680: `0eec2b9f-fc9...`](#1680) — single-answer, 정답: C19
2. [문제 1681: `7db124a5-8a4...`](#1681) — single-answer, 정답: C19
3. [문제 1682: `06ae6154-d18...`](#1682) — single-answer, 정답: C8
4. [문제 1683: `8385a992-e6b...`](#1683) — multiple-answer, 정답: C3|C9|C15|C17
5. [문제 1684: `16a32820-b94...`](#1684) — single-answer, 정답: C9
6. [문제 1685: `3f7907d7-e47...`](#1685) — single-answer, 정답: C3
7. [문제 1686: `7ca7486d-b27...`](#1686) — single-answer, 정답: C2
8. [문제 1687: `556e6c0a-dc1...`](#1687) — single-answer, 정답: C22
9. [문제 1688: `2b63d321-d87...`](#1688) — single-answer, 정답: C10
10. [문제 1689: `1f3033a4-b36...`](#1689) — single-answer, 정답: C10

---

### 문제 1680: `0eec2b9f-fc9...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `0eec2b9f-fc94-4fc1-aa27-fad9a42c29a9` |
| Tag | **single-answer** |
| 정답 | **C19** |
| C19 의미 | Lift the tilt angle  of 3240381_3 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1680] topology](images/train_1680.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3278168_2 by 24 degrees
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3278168_2
- `C3`: Check test server and transmission issues
- `C4`: Press down the tilt angle  of 3240381_3 by 10 degrees
- `C5`: Decrease transmission power for 3261219_1
- `C6`: Add neighbor relationship between 3240381_3 and 3261219_1
- `C7`: Increase A3 Offset threshold for 3261219_1
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3278168_2
- `C9`: Adjust the azimuth of 3240381_3 by 50 degrees
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3261219_1
- `C11`: Lift the tilt angle of 3278168_2 by 4 degrees
- `C12`: Increase transmission power for 3261219_1
- `C13`: Decrease transmission power for 3278168_2
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Decrease A3 Offset threshold for 3261219_1
- `C16`: Increase A3 Offset threshold for 3278168_2
- `C17`: Decrease A3 Offset threshold for 3278168_2
- `C18`: Press down the tilt angle of 3278168_2 by 4 degrees
- `C19`: Lift the tilt angle  of 3240381_3 by 10 degrees **← 정답**
- `C20`: Increase transmission power for 3278168_2
- `C21`: Add neighbor relationship between 3278168_2 and 3261219_1
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3261219_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.595 | MS1 | 121.4656746031 | 31.1446292972 | 706 | 504990 | -91.58 | 17.99 | 576.68 | 0.07 | 2.26 | 1583 |
| 2024-09-20 22:21:32.510 | MS1 | 121.4656740578 | 31.1446346106 | 706 | 504990 | -85.56 | 16.31 | 584.36 | 0.15 | 2.58 | 1578 |
| 2024-09-20 22:21:33.864 | MS1 | 121.4656755587 | 31.1446292494 | 706 | 504990 | -85.46 | 16.97 | 541.05 | 0.19 | 2.28 | 1588 |
| 2024-09-20 22:21:34.541 | MS1 | 121.4656631248 | 31.1446261114 | 706 | 504990 | -88.99 | 15.24 | 75.24 | 0.19 | 2.84 | 1586 |
| 2024-09-20 22:21:35.219 | MS1 | 121.4656779902 | 31.1446220489 | 706 | 504990 | -89.42 | 15.55 | 58.41 | 0.12 | 2.35 | 1597 |
| 2024-09-20 22:21:36.284 | MS1 | 121.4656620533 | 31.1446365138 | 706 | 504990 | -89.62 | 17.85 | 53.26 | 0.19 | 2.91 | 1576 |
| 2024-09-20 22:21:37.144 | MS1 | 121.4656639310 | 31.1446210879 | 706 | 504990 | -91.56 | 12.17 | 84.25 | 0.06 | 2.96 | 1587 |
| 2024-09-20 22:21:38.306 | MS1 | 121.4656732577 | 31.1446180670 | 706 | 504990 | -89.81 | 11.55 | 67.95 | 0.05 | 2.57 | 1592 |
| 2024-09-20 22:21:39.816 | MS1 | 121.4656611108 | 31.1446222135 | 706 | 504990 | -91.43 | 10.71 | 75.58 | 0.17 | 2.03 | 1597 |
| 2024-09-20 22:21:40.815 | MS1 | 121.4656670231 | 31.1446311936 | 706 | 504990 | -91.65 | 11.93 | 531.89 | 0.16 | 2.55 | 1578 |
| 2024-09-20 22:21:41.849 | MS1 | 121.4656662822 | 31.1446244998 | 706 | 504990 | -90.66 | 8.52 | 364.09 | 0.06 | 2.88 | 1566 |
| 2024-09-20 22:21:42.896 | MS1 | 121.4656722665 | 31.1446358421 | 706 | 504990 | -93.50 | 9.71 | 539.35 | 0.15 | 2.88 | 1577 |

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
| 3240381 | 3 | 121.4733105701 | 31.1465558342 | 139 | 14 | 3 | 48.7 | TDD | 187 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3251041 | 4 | 121.4641294566 | 31.1454867783 | 278 | 4 | 6 | 33.5 | TDD | 951 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3261219 | 1 | 121.4716027253 | 31.1502070168 | 5 | 11 | 8 | 45.7 | TDD | 145 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3278168 | 2 | 121.4755904097 | 31.1556211729 | 242 | 3 | 7 | 21.9 | TDD | 706 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:30.840 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.860 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:30.974 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.974 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.655 | NREventA3 | measId:2;ServCellPCI:240;Se... |
| 2024-09-20 22:21:37.895 | NRHandoverAttempt | SourcePCI:240;SourceNR-ARFC... |
| 2024-09-20 22:21:37.934 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.944 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.092 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.092 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3261219 | 1 | 19.3262 | 15.1449 | -117.1683 | 17.6904 | 189.1712 | 0.0056 | 0.0181 |
| 2024_09_20 22:00 | 3278168 | 2 | 92.8137 | 81.8543 | -114.4115 | 17.4283 | 173.7306 | 0.0090 | 0.0009 |
| 2024_09_20 22:00 | 3240381 | 3 | 12.5588 | 10.8099 | -117.1676 | 10.1953 | 180.8708 | 0.0070 | 0.0065 |
| 2024_09_20 22:00 | 3251041 | 4 | 16.1862 | 19.9360 | -114.9496 | 14.7042 | 171.9471 | 0.0173 | 0.0013 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413161_01733894 | 504990 | 706 | -87.2 | 504990 | 145 | -96.2 | 504990 | 187 | -102.5 | 504990 | 951 |
| MR_1774413161_E1074827 | 504990 | 706 | -90.4 | 504990 | 145 | -95.3 | 504990 | 187 | -100.7 | 504990 | 951 |
| MR_1774413161_EFFD7C85 | 504990 | 706 | -90.7 | 504990 | 145 | -94.7 | 504990 | 187 | -99.7 | 504990 | 951 |
| MR_1774413161_9AADA2C4 | 504990 | 706 | -88.9 | 504990 | 145 | -97.7 | 504990 | 187 | -101.5 | 504990 | 951 |
| MR_1774413161_BD971627 | 504990 | 706 | -88.1 | 504990 | 145 | -97.2 | 504990 | 187 | -101.3 | 504990 | 951 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1681: `7db124a5-8a4...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `7db124a5-8a41-4b21-9a8d-f46897520f8f` |
| Tag | **single-answer** |
| 정답 | **C19** |
| C19 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3279256_3 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1681] topology](images/train_1681.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3214690_4
- `C2`: Add neighbor relationship between 3279256_3 and 3214690_4
- `C3`: Decrease A3 Offset threshold for 3279256_3
- `C4`: Add neighbor relationship between 3271323_2 and 3214690_4
- `C5`: Increase A3 Offset threshold for 3214690_4
- `C6`: Decrease transmission power for 3279256_3
- `C7`: Decrease A3 Offset threshold for 3214690_4
- `C8`: Adjust the azimuth of 3279256_3 by 20 degrees
- `C9`: Press down the tilt angle of 3279256_3 by 3 degrees
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3214690_4
- `C11`: Press down the tilt angle  of 3214690_4 by 2 degrees
- `C12`: Lift the tilt angle of 3279256_3 by 3 degrees
- `C13`: Lift the tilt angle  of 3214690_4 by 2 degrees
- `C14`: Decrease transmission power for 3214690_4
- `C15`: Insufficient data; more data is needed for judgment.
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3279256_3
- `C17`: Check test server and transmission issues
- `C18`: Adjust the azimuth of 3214690_4 by 50 degrees
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3279256_3 **← 정답**
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3214690_4
- `C21`: Increase A3 Offset threshold for 3279256_3
- `C22`: Increase transmission power for 3279256_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.696 | MS1 | 121.4656717600 | 31.1446240117 | 669 | 504990 | -86.17 | 14.48 | 367.32 | 0.06 | 2.23 | 1575 |
| 2024-09-20 22:21:32.158 | MS1 | 121.4656669021 | 31.1446210129 | 669 | 504990 | -89.05 | 12.59 | 458.05 | 0.14 | 2.23 | 1582 |
| 2024-09-20 22:21:33.596 | MS1 | 121.4656622088 | 31.1446337041 | 669 | 504990 | -87.83 | 13.38 | 325.95 | 0.15 | 2.01 | 1587 |
| 2024-09-20 22:21:34.655 | MS1 | 121.4656756165 | 31.1446363554 | 669 | 504990 | -86.45 | 15.45 | 44.13 | 0.69 | 2.93 | 565 |
| 2024-09-20 22:21:35.490 | MS1 | 121.4656650151 | 31.1446306206 | 669 | 504990 | -86.65 | 16.09 | 93.08 | 0.65 | 2.71 | 535 |
| 2024-09-20 22:21:36.106 | MS1 | 121.4656589468 | 31.1446299682 | 669 | 504990 | -88.97 | 14.99 | 65.69 | 0.60 | 2.34 | 660 |
| 2024-09-20 22:21:37.805 | MS1 | 121.4656617263 | 31.1446193927 | 669 | 504990 | -91.52 | 8.45 | 76.63 | 0.60 | 2.14 | 688 |
| 2024-09-20 22:21:38.418 | MS1 | 121.4656631926 | 31.1446362311 | 669 | 504990 | -93.38 | 10.18 | 84.52 | 0.54 | 2.21 | 687 |
| 2024-09-20 22:21:39.717 | MS1 | 121.4656757068 | 31.1446309916 | 669 | 504990 | -93.53 | 10.97 | 61.77 | 0.54 | 2.94 | 544 |
| 2024-09-20 22:21:40.653 | MS1 | 121.4656674441 | 31.1446280546 | 669 | 504990 | -91.99 | 11.28 | 537.37 | 0.04 | 2.57 | 1575 |
| 2024-09-20 22:21:41.628 | MS1 | 121.4656718886 | 31.1446258797 | 669 | 504990 | -90.20 | 7.88 | 318.16 | 0.11 | 2.44 | 1595 |
| 2024-09-20 22:21:42.982 | MS1 | 121.4656762882 | 31.1446302280 | 669 | 504990 | -90.53 | 8.27 | 351.64 | 0.09 | 2.07 | 1572 |

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
| 3214690 | 4 | 121.4711412472 | 31.1512414650 | 47 | 0 | 11 | 30.8 | TDD | 558 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3215677 | 1 | 121.4642179935 | 31.1444114327 | 65 | 13 | 1 | 47.7 | TDD | 856 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3271323 | 2 | 121.4752784263 | 31.1480855326 | 336 | 2 | 6 | 44.4 | TDD | 819 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3279256 | 3 | 121.4728560779 | 31.1443939662 | 292 | 1 | 4 | 19.0 | TDD | 669 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |

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
| 2024-09-20 22:21:30.804 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.823 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:30.929 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.929 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.702 | NREventA3 | measId:2;ServCellPCI:391;Se... |
| 2024-09-20 22:21:37.942 | NRHandoverAttempt | SourcePCI:391;SourceNR-ARFC... |
| 2024-09-20 22:21:37.976 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.986 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.122 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.122 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3215677 | 1 | 8.3690 | 15.4346 | -115.6343 | 14.7773 | 83.3781 | 0.0186 | 0.0096 |
| 2024_09_20 22:00 | 3271323 | 2 | 16.1539 | 5.1796 | -115.8592 | 18.6523 | 163.4162 | 0.0153 | 0.0003 |
| 2024_09_20 22:00 | 3279256 | 3 | 13.7183 | 8.8806 | -116.6636 | 17.9264 | 196.9057 | 0.0113 | 0.0182 |
| 2024_09_20 22:00 | 3214690 | 4 | 18.8238 | 7.1240 | -116.0378 | 12.8549 | 87.1651 | 0.0086 | 0.0170 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416690_48AFEFD2 | 504990 | 669 | -88.3 | 504990 | 558 | -87.5 | 504990 | 819 | -92.4 | 504990 | 856 |
| MR_1774416690_1B3B143B | 504990 | 669 | -85.2 | 504990 | 558 | -88.1 | 504990 | 819 | -94.9 | 504990 | 856 |
| MR_1774416690_A374CBA9 | 504990 | 669 | -86.3 | 504990 | 558 | -87.9 | 504990 | 819 | -92.1 | 504990 | 856 |
| MR_1774416690_E5F49707 | 504990 | 669 | -85.2 | 504990 | 558 | -88.0 | 504990 | 819 | -94.5 | 504990 | 856 |
| MR_1774416690_EE056160 | 504990 | 669 | -85.3 | 504990 | 558 | -85.6 | 504990 | 819 | -94.1 | 504990 | 856 |
| MR_1774416690_6A1BAA1D | 504990 | 669 | -87.8 | 504990 | 558 | -85.0 | 504990 | 819 | -92.4 | 504990 | 856 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1682: `06ae6154-d18...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `06ae6154-d188-4810-86a9-dd8edbef7e9e` |
| Tag | **single-answer** |
| 정답 | **C8** |
| C8 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3225389_1 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1682] topology](images/train_1682.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3254864_6 by 32 degrees
- `C2`: Lift the tilt angle  of 3254864_6 by 2 degrees
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3225389_1
- `C4`: Add neighbor relationship between 3277350_13 and 3254864_6
- `C5`: Check test server and transmission issues
- `C6`: Add neighbor relationship between 3225389_1 and 3254864_6
- `C7`: Increase transmission power for 3254864_6
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3225389_1 **← 정답**
- `C9`: Decrease transmission power for 3254864_6
- `C10`: Press down the tilt angle of 3225389_1 by 3 degrees
- `C11`: Decrease transmission power for 3225389_1
- `C12`: Increase transmission power for 3225389_1
- `C13`: Insufficient data; more data is needed for judgment.
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3254864_6
- `C15`: Adjust the azimuth of 3225389_1 by 42 degrees
- `C16`: Increase A3 Offset threshold for 3254864_6
- `C17`: Decrease A3 Offset threshold for 3254864_6
- `C18`: Lift the tilt angle of 3225389_1 by 3 degrees
- `C19`: Increase A3 Offset threshold for 3225389_1
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3254864_6
- `C21`: Press down the tilt angle  of 3254864_6 by 2 degrees
- `C22`: Decrease A3 Offset threshold for 3225389_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.708 | MS1 | 121.4656591429 | 31.1446256688 | 104 | 504990 | -94.18 | 13.92 | 444.76 | 0.05 | 2.84 | 1589 |
| 2024-09-20 22:21:32.897 | MS1 | 121.4656703021 | 31.1446310105 | 307 | 504990 | -95.31 | 12.77 | 577.37 | 0.12 | 2.73 | 1564 |
| 2024-09-20 22:21:33.233 | MS1 | 121.4656701544 | 31.1446331828 | 442 | 504990 | -95.34 | 11.64 | 420.50 | 0.09 | 2.50 | 1561 |
| 2024-09-20 22:21:34.682 | MS1 | 121.4656663440 | 31.1446331354 | 919 | 152650 | -91.99 | 7.10 | 86.48 | 0.12 | 1.74 | 950 |
| 2024-09-20 22:21:35.902 | MS1 | 121.4656597545 | 31.1446216994 | 555 | 152650 | -92.84 | 2.73 | 90.77 | 0.13 | 1.64 | 979 |
| 2024-09-20 22:21:36.879 | MS1 | 121.4656710624 | 31.1446276159 | 250 | 152650 | -94.04 | 2.96 | 86.79 | 0.11 | 1.78 | 901 |
| 2024-09-20 22:21:37.410 | MS1 | 121.4656633717 | 31.1446360616 | 611 | 152650 | -92.41 | 7.33 | 64.89 | 0.17 | 1.76 | 929 |
| 2024-09-20 22:21:38.944 | MS1 | 121.4656707667 | 31.1446293360 | 919 | 152650 | -96.19 | 7.23 | 88.72 | 0.02 | 1.53 | 919 |
| 2024-09-20 22:21:39.648 | MS1 | 121.4656727110 | 31.1446333746 | 555 | 152650 | -92.89 | 3.12 | 69.80 | 0.20 | 1.87 | 952 |
| 2024-09-20 22:21:40.758 | MS1 | 121.4656707970 | 31.1446240339 | 250 | 152650 | -90.94 | 2.48 | 77.31 | 0.12 | 2.00 | 1598 |
| 2024-09-20 22:21:41.949 | MS1 | 121.4656605135 | 31.1446328724 | 611 | 152650 | -88.44 | 5.26 | 92.25 | 0.14 | 2.43 | 1566 |
| 2024-09-20 22:21:42.793 | MS1 | 121.4656671567 | 31.1446370319 | 919 | 152650 | -94.86 | 7.75 | 73.96 | 0.12 | 2.47 | 1573 |

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
| 3222052 | 9 | 121.4729572649 | 31.1482460217 | 266 | 13 | 7 | 28.8 | FDD | 433 | n1 | 152650 | 30M | 4T4R | 27 | 152650 |
| 3224028 | 8 | 121.4709956050 | 31.1521521730 | 288 | 10 | 8 | 29.9 | FDD | 555 | n1 | 152650 | 30M | 4T4R | 25 | 152650 |
| 3224485 | 3 | 121.4716150837 | 31.1467509628 | 354 | 0 | 5 | 10.0 | TDD | 307 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3224646 | 2 | 121.4706128147 | 31.1548728043 | 244 | 2 | 11 | 5.3 | TDD | 492 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3225389 | 1 | 121.4665956591 | 31.1543111408 | 143 | 3 | 0 | 7.5 | TDD | 104 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3233252 | 10 | 121.4739698911 | 31.1556805638 | 76 | 2 | 6 | 27.7 | FDD | 885 | n1 | 152650 | 30M | 4T4R | 23 | 152650 |
| 3254864 | 6 | 121.4708600361 | 31.1551254010 | 171 | 1 | 5 | 22.7 | TDD | 671 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3262385 | 11 | 121.4732602219 | 31.1508502323 | 148 | 13 | 6 | 20.7 | FDD | 919 | n1 | 152650 | 30M | 4T4R | 12 | 152650 |
| 3266428 | 12 | 121.4748157484 | 31.1473850136 | 164 | 7 | 0 | 10.7 | FDD | 248 | n1 | 152650 | 30M | 4T4R | 28 | 152650 |
| 3272682 | 7 | 121.4720819097 | 31.1533302570 | 199 | 10 | 9 | 0.4 | FDD | 611 | n1 | 152650 | 30M | 4T4R | 20 | 152650 |
| 3273163 | 5 | 121.4664888405 | 31.1473984984 | 262 | 8 | 0 | 3.1 | TDD | 442 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3273182 | 4 | 121.4698590319 | 31.1464814394 | 261 | 9 | 11 | 18.6 | TDD | 631 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3277350 | 13 | 121.4738922604 | 31.1547724204 | 164 | 3 | 1 | 18.6 | FDD | 250 | n1 | 152650 | 30M | 4T4R | 26 | 152650 |

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
| 2024-09-20 22:21:31.159 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.175 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.312 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.312 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.005 | NREventA2 | measId:1;ServCellPCI:612;Se... |
| 2024-09-20 22:21:35.148 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.427 | NREventA5 | measId:3;ServCellPCI:612;Se... |
| 2024-09-20 22:21:35.488 | NRHandoverAttempt | SourcePCI:612;SourceNR-ARFC... |
| 2024-09-20 22:21:35.529 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.540 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:35.685 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.685 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3225389 | 1 | 17.1449 | 14.0194 | -117.5366 | 12.1816 | 143.0069 | 0.0048 | 0.0145 |
| 2024_09_20 22:00 | 3224646 | 2 | 12.0874 | 16.2430 | -116.6608 | 8.5249 | 145.5950 | 0.0163 | 0.0098 |
| 2024_09_20 22:00 | 3224485 | 3 | 8.4556 | 9.2166 | -117.9527 | 17.4886 | 184.9876 | 0.0170 | 0.0155 |
| 2024_09_20 22:00 | 3273182 | 4 | 10.2755 | 11.7329 | -117.8174 | 19.2829 | 94.3618 | 0.0078 | 0.0168 |
| 2024_09_20 22:00 | 3273163 | 5 | 16.9892 | 6.2254 | -114.7071 | 13.2453 | 115.8770 | 0.0136 | 0.0113 |
| 2024_09_20 22:00 | 3254864 | 6 | 10.1974 | 8.4733 | -114.1660 | 16.8630 | 114.2837 | 0.0172 | 0.0018 |
| 2024_09_20 22:00 | 3272682 | 7 | 8.6974 | 12.7012 | -115.8588 | 3.7133 | 57.5200 | 0.0118 | 0.0058 |
| 2024_09_20 22:00 | 3224028 | 8 | 17.8018 | 7.5064 | -117.1388 | 4.9490 | 50.6570 | 0.0067 | 0.0089 |
| 2024_09_20 22:00 | 3222052 | 9 | 17.0595 | 15.1224 | -114.9205 | 4.4778 | 43.8190 | 0.0130 | 0.0018 |
| 2024_09_20 22:00 | 3233252 | 10 | 17.2705 | 19.0987 | -115.0139 | 4.9080 | 41.7284 | 0.0174 | 0.0148 |
| 2024_09_20 22:00 | 3262385 | 11 | 12.5419 | 10.0295 | -116.7758 | 4.5254 | 34.9782 | 0.0189 | 0.0115 |
| 2024_09_20 22:00 | 3266428 | 12 | 5.3133 | 9.2617 | -117.8638 | 3.0276 | 21.6119 | 0.0195 | 0.0171 |
| 2024_09_20 22:00 | 3277350 | 13 | 5.0505 | 15.4256 | -117.0983 | 4.8001 | 45.0779 | 0.0175 | 0.0174 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416290_8EA847E9 | 504990 | 442 | -94.1 | 504990 | 671 | -94.2 | 504990 | 492 | -99.3 | 504990 | 631 |
| MR_1774416290_E1E3CD7D | 504990 | 442 | -95.6 | 504990 | 671 | -95.3 | 504990 | 492 | -98.5 | 504990 | 631 |
| MR_1774416290_DDE7C9BF | 152650 | 919 | -91.0 | 152650 | 248 | -99.2 | 152650 | 433 | -100.3 | 152650 | 885 |
| MR_1774416290_8115AC6B | 152650 | 919 | -93.3 | 152650 | 248 | -100.0 | 152650 | 433 | -98.1 | 152650 | 885 |
| MR_1774416290_9A757CF5 | 504990 | 442 | -95.2 | 504990 | 671 | -92.6 | 504990 | 492 | -98.4 | 504990 | 631 |
| MR_1774416290_401E61A2 | 152650 | 919 | -90.5 | 152650 | 248 | -97.9 | 152650 | 433 | -99.2 | 152650 | 885 |
| MR_1774416290_E6B9A321 | 152650 | 919 | -93.9 | 152650 | 248 | -99.5 | 152650 | 433 | -97.6 | 152650 | 885 |
| MR_1774416290_EF513F85 | 152650 | 919 | -93.2 | 152650 | 248 | -100.7 | 152650 | 433 | -99.5 | 152650 | 885 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1683: `8385a992-e6b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `8385a992-e6b7-4bf9-a33f-7695bcc3d7b9` |
| Tag | **multiple-answer** |
| 정답 | **C3|C9|C15|C17** |
| C3 의미 | Increase A3 Offset threshold for 3261231_3 |
| C9 의미 | Press down the tilt angle  of 3261231_3 by 4 degrees |
| C15 의미 | Increase A3 Offset threshold for 3216610_1 |
| C17 의미 | Decrease transmission power for 3261231_3 |
| 패턴 분류 | **P2 Ping-pong** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1683] topology](images/train_1683.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 5 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 5개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3261231_3
- `C2`: Lift the tilt angle  of 3261231_3 by 4 degrees
- `C3`: Increase A3 Offset threshold for 3261231_3 **← 정답**
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3261231_3
- `C5`: Insufficient data; more data is needed for judgment.
- `C6`: Check test server and transmission issues
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3216610_1
- `C8`: Decrease A3 Offset threshold for 3216610_1
- `C9`: Press down the tilt angle  of 3261231_3 by 4 degrees **← 정답**
- `C10`: Add neighbor relationship between 3216610_1 and 3261231_3
- `C11`: Increase transmission power for 3216610_1
- `C12`: Adjust the azimuth of 3216610_1 by 13 degrees
- `C13`: Decrease transmission power for 3216610_1
- `C14`: Decrease A3 Offset threshold for 3261231_3
- `C15`: Increase A3 Offset threshold for 3216610_1 **← 정답**
- `C16`: Press down the tilt angle of 3216610_1 by 5 degrees
- `C17`: Decrease transmission power for 3261231_3 **← 정답**
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3261231_3
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3216610_1
- `C20`: Adjust the azimuth of 3261231_3 by 11 degrees
- `C21`: Lift the tilt angle of 3216610_1 by 5 degrees
- `C22`: Add neighbor relationship between 3274768_4 and 3261231_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.516 | MS1 | 121.4656777945 | 31.1446369338 | 968 | 504990 | -76.56 | 12.02 | 587.13 | 0.04 | 2.27 | 1575 |
| 2024-09-20 22:21:32.733 | MS1 | 121.4656652071 | 31.1446343589 | 968 | 504990 | -75.00 | 16.32 | 454.77 | 0.06 | 2.99 | 1594 |
| 2024-09-20 22:21:33.527 | MS1 | 121.4656706965 | 31.1446252491 | 968 | 504990 | -84.90 | 15.92 | 491.35 | 0.19 | 2.61 | 1569 |
| 2024-09-20 22:21:34.363 | MS1 | 121.4656755394 | 31.1446197295 | 217 | 504990 | -88.46 | 4.69 | 56.08 | 0.13 | 1.48 | 1576 |
| 2024-09-20 22:21:35.957 | MS1 | 121.4656597038 | 31.1446209142 | 217 | 504990 | -83.04 | 3.61 | 43.21 | 0.16 | 1.49 | 1592 |
| 2024-09-20 22:21:36.387 | MS1 | 121.4656744378 | 31.1446220450 | 968 | 504990 | -89.47 | 1.26 | 30.51 | 0.11 | 1.47 | 1561 |
| 2024-09-20 22:21:37.653 | MS1 | 121.4656679484 | 31.1446212789 | 968 | 504990 | -81.15 | 4.85 | 20.30 | 0.05 | 1.47 | 1565 |
| 2024-09-20 22:21:38.849 | MS1 | 121.4656613054 | 31.1446242187 | 217 | 504990 | -83.51 | 1.87 | 53.59 | 0.18 | 1.40 | 1565 |
| 2024-09-20 22:21:39.693 | MS1 | 121.4656660042 | 31.1446197111 | 217 | 504990 | -85.72 | 3.64 | 43.10 | 0.10 | 1.42 | 1590 |
| 2024-09-20 22:21:40.909 | MS1 | 121.4656602346 | 31.1446343341 | 217 | 504990 | -84.65 | 15.24 | 559.67 | 0.16 | 2.16 | 1561 |
| 2024-09-20 22:21:41.121 | MS1 | 121.4656749530 | 31.1446335295 | 217 | 504990 | -77.24 | 14.44 | 427.03 | 0.19 | 2.94 | 1564 |
| 2024-09-20 22:21:42.823 | MS1 | 121.4656688732 | 31.1446210636 | 217 | 504990 | -77.00 | 15.02 | 495.49 | 0.05 | 2.56 | 1591 |

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
| 3216610 | 1 | 121.4693196412 | 31.1519776176 | 216 | 4 | 11 | 20.0 | TDD | 968 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3233436 | 5 | 121.4688529603 | 31.1556656890 | 308 | 15 | 12 | 40.9 | TDD | 217 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3237367 | 2 | 121.4666174427 | 31.1500623180 | 318 | 11 | 7 | 21.3 | TDD | 520 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3261231 | 3 | 121.4738263982 | 31.1448848901 | 257 | 2 | 7 | 30.5 | TDD | 398 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3274768 | 4 | 121.4749395514 | 31.1497908091 | 138 | 4 | 12 | 38.9 | TDD | 631 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |

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
| 2024-09-20 22:21:31.356 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.381 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.507 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.507 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.245 | NREventA3 | measId:2;ServCellPCI:902;Se... |
| 2024-09-20 22:21:34.485 | NRHandoverAttempt | SourcePCI:902;SourceNR-ARFC... |
| 2024-09-20 22:21:34.520 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:34.535 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:34.656 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:34.656 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:36.245 | NREventA3 | measId:2;ServCellPCI:5;Serv... |
| 2024-09-20 22:21:36.485 | NRHandoverAttempt | SourcePCI:5;SourceNR-ARFCN:... |
| 2024-09-20 22:21:36.519 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:36.531 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:36.667 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.667 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.245 | NREventA3 | measId:2;ServCellPCI:902;Se... |
| 2024-09-20 22:21:38.485 | NRHandoverAttempt | SourcePCI:902;SourceNR-ARFC... |
| 2024-09-20 22:21:38.527 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.538 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.670 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.670 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3216610 | 1 | 15.1729 | 5.7857 | -116.4081 | 19.7254 | 191.2830 | 0.0039 | 0.0144 |
| 2024_09_20 22:00 | 3237367 | 2 | 19.4701 | 7.1670 | -117.5916 | 13.6614 | 112.0056 | 0.0009 | 0.0188 |
| 2024_09_20 22:00 | 3261231 | 3 | 12.5478 | 11.3444 | -117.9519 | 6.6816 | 141.9174 | 0.0196 | 0.0104 |
| 2024_09_20 22:00 | 3274768 | 4 | 11.8440 | 9.4774 | -114.1365 | 19.3142 | 125.3817 | 0.0033 | 0.0175 |
| 2024_09_20 22:00 | 3233436 | 5 | 7.6620 | 17.8647 | -114.1549 | 8.3557 | 167.0500 | 0.0079 | 0.0144 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413194_B3365781 | 504990 | 217 | -89.1 | 504990 | 968 | -86.3 | 504990 | 398 | -86.7 | 504990 | 631 |
| MR_1774413194_7D6AC31B | 504990 | 217 | -88.2 | 504990 | 968 | -89.2 | 504990 | 398 | -89.4 | 504990 | 631 |
| MR_1774413194_AAA3B85F | 504990 | 968 | -86.5 | 504990 | 217 | -87.8 | 504990 | 398 | -87.8 | 504990 | 631 |
| MR_1774413194_7E44DC56 | 504990 | 217 | -89.4 | 504990 | 968 | -88.2 | 504990 | 398 | -87.5 | 504990 | 631 |
| MR_1774413194_F5B10BB5 | 504990 | 968 | -87.1 | 504990 | 217 | -86.5 | 504990 | 398 | -89.3 | 504990 | 631 |
| MR_1774413194_AB3A0DA3 | 504990 | 217 | -89.8 | 504990 | 968 | -86.8 | 504990 | 398 | -89.1 | 504990 | 631 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1684: `16a32820-b94...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `16a32820-b94c-488e-8d06-368791fd055a` |
| Tag | **single-answer** |
| 정답 | **C9** |
| C9 의미 | Decrease A3 Offset threshold for 3268313_1 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1684] topology](images/train_1684.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Check test server and transmission issues
- `C2`: Increase A3 Offset threshold for 3268313_1
- `C3`: Lift the tilt angle of 3268313_1 by 7 degrees
- `C4`: Adjust the azimuth of 3268313_1 by 50 degrees
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3250809_3
- `C6`: Add neighbor relationship between 3232724_4 and 3250809_3
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3250809_3
- `C8`: Decrease A3 Offset threshold for 3250809_3
- `C9`: Decrease A3 Offset threshold for 3268313_1 **← 정답**
- `C10`: Press down the tilt angle of 3268313_1 by 7 degrees
- `C11`: Lift the tilt angle  of 3250809_3 by 9 degrees
- `C12`: Insufficient data; more data is needed for judgment.
- `C13`: Press down the tilt angle  of 3250809_3 by 9 degrees
- `C14`: Decrease transmission power for 3268313_1
- `C15`: Increase A3 Offset threshold for 3250809_3
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3268313_1
- `C17`: Decrease transmission power for 3250809_3
- `C18`: Adjust the azimuth of 3250809_3 by 46 degrees
- `C19`: Increase transmission power for 3250809_3
- `C20`: Increase transmission power for 3268313_1
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3268313_1
- `C22`: Add neighbor relationship between 3268313_1 and 3250809_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.481 | MS1 | 121.4656627197 | 31.1446207396 | 232 | 504990 | -76.17 | 17.62 | 361.23 | 0.01 | 2.18 | 1564 |
| 2024-09-20 22:21:32.340 | MS1 | 121.4656773685 | 31.1446307050 | 232 | 504990 | -83.67 | 14.88 | 447.25 | 0.05 | 2.12 | 1571 |
| 2024-09-20 22:21:33.861 | MS1 | 121.4656648961 | 31.1446322288 | 232 | 504990 | -83.08 | 15.70 | 523.18 | 0.15 | 2.12 | 1600 |
| 2024-09-20 22:21:34.457 | MS1 | 121.4656777628 | 31.1446196418 | 232 | 504990 | -88.90 | -3.29 | 62.14 | 0.08 | 1.28 | 1600 |
| 2024-09-20 22:21:35.466 | MS1 | 121.4656774596 | 31.1446259209 | 232 | 504990 | -87.09 | -0.72 | 40.55 | 0.01 | 1.36 | 1577 |
| 2024-09-20 22:21:36.465 | MS1 | 121.4656621585 | 31.1446340903 | 232 | 504990 | -86.30 | -3.91 | 74.58 | 0.02 | 1.11 | 1561 |
| 2024-09-20 22:21:37.869 | MS1 | 121.4656597993 | 31.1446228012 | 232 | 504990 | -88.79 | -1.11 | 41.26 | 0.05 | 1.04 | 1593 |
| 2024-09-20 22:21:38.239 | MS1 | 121.4656599781 | 31.1446312194 | 232 | 504990 | -91.14 | -1.08 | 29.04 | 0.03 | 1.35 | 1590 |
| 2024-09-20 22:21:39.787 | MS1 | 121.4656685474 | 31.1446187782 | 474 | 504990 | -77.26 | 17.60 | 251.75 | 0.12 | 1.28 | 1564 |
| 2024-09-20 22:21:40.767 | MS1 | 121.4656759393 | 31.1446317588 | 474 | 504990 | -76.23 | 16.87 | 588.90 | 0.06 | 2.04 | 1571 |
| 2024-09-20 22:21:41.378 | MS1 | 121.4656608225 | 31.1446208708 | 474 | 504990 | -82.58 | 14.84 | 549.89 | 0.10 | 2.24 | 1580 |
| 2024-09-20 22:21:42.352 | MS1 | 121.4656590470 | 31.1446237202 | 474 | 504990 | -78.10 | 14.81 | 364.41 | 0.11 | 2.76 | 1583 |

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
| 3232724 | 4 | 121.4739277918 | 31.1456595391 | 25 | 2 | 10 | 17.0 | TDD | 874 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3250809 | 3 | 121.4707923807 | 31.1476161956 | 282 | 6 | 11 | 29.5 | TDD | 474 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3267524 | 2 | 121.4693093751 | 31.1487502068 | 48 | 3 | 2 | 18.3 | TDD | 81 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3268313 | 1 | 121.4710009095 | 31.1485929175 | 38 | 6 | 10 | 16.4 | TDD | 232 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |

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
| 2024-09-20 22:21:31.281 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.304 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.444 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.444 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.162 | NREventA3 | measId:2;ServCellPCI:38;Ser... |
| 2024-09-20 22:21:38.402 | NRHandoverAttempt | SourcePCI:38;SourceNR-ARFCN... |
| 2024-09-20 22:21:38.451 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.464 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.584 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.584 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3268313 | 1 | 17.7873 | 5.0065 | -117.4958 | 12.8033 | 86.8079 | 0.0191 | 0.1443 |
| 2024_09_20 22:00 | 3267524 | 2 | 16.2147 | 18.6851 | -114.1433 | 11.5737 | 160.6231 | 0.0096 | 0.0062 |
| 2024_09_20 22:00 | 3250809 | 3 | 8.2831 | 17.8954 | -115.0141 | 9.0805 | 113.3115 | 0.0092 | 0.0010 |
| 2024_09_20 22:00 | 3232724 | 4 | 13.9665 | 5.0155 | -115.6636 | 6.6111 | 142.6602 | 0.0143 | 0.0092 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412670_057BC6F7 | 504990 | 232 | -87.5 | 504990 | 474 | -82.9 | 504990 | 874 | -85.0 | 504990 | 81 |
| MR_1774412670_92EE0D07 | 504990 | 232 | -90.1 | 504990 | 474 | -82.7 | 504990 | 874 | -84.6 | 504990 | 81 |
| MR_1774412670_19031AB3 | 504990 | 232 | -90.1 | 504990 | 474 | -82.2 | 504990 | 874 | -85.9 | 504990 | 81 |
| MR_1774412670_16FB0E3E | 504990 | 474 | -84.0 | 504990 | 232 | -88.1 | 504990 | 874 | -85.2 | 504990 | 81 |
| MR_1774412670_61C4E9CE | 504990 | 232 | -87.9 | 504990 | 474 | -81.7 | 504990 | 874 | -85.7 | 504990 | 81 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1685: `3f7907d7-e47...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `3f7907d7-e472-4ce2-8a3b-73102d277b05` |
| Tag | **single-answer** |
| 정답 | **C3** |
| C3 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1685] topology](images/train_1685.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3210524_2 by 3 degrees
- `C2`: Decrease transmission power for 3210524_2
- `C3`: Insufficient data; more data is needed for judgment. **← 정답**
- `C4`: Decrease transmission power for 3266639_3
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3266639_3
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3210524_2
- `C7`: Add neighbor relationship between 3248467_1 and 3266639_3
- `C8`: Add neighbor relationship between 3210524_2 and 3266639_3
- `C9`: Adjust the azimuth of 3266639_3 by 21 degrees
- `C10`: Increase A3 Offset threshold for 3210524_2
- `C11`: Lift the tilt angle  of 3266639_3 by 10 degrees
- `C12`: Decrease A3 Offset threshold for 3210524_2
- `C13`: Increase A3 Offset threshold for 3266639_3
- `C14`: Check test server and transmission issues
- `C15`: Lift the tilt angle of 3210524_2 by 3 degrees
- `C16`: Increase transmission power for 3210524_2
- `C17`: Adjust the azimuth of 3210524_2 by 50 degrees
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3266639_3
- `C19`: Increase transmission power for 3266639_3
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3210524_2
- `C21`: Press down the tilt angle  of 3266639_3 by 10 degrees
- `C22`: Decrease A3 Offset threshold for 3266639_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.812 | MS1 | 121.4656677592 | 31.1446250417 | 828 | 504990 | -90.79 | 15.37 | 367.12 | 0.18 | 2.97 | 1599 |
| 2024-09-20 22:21:32.249 | MS1 | 121.4656601696 | 31.1446305333 | 828 | 504990 | -90.43 | 16.66 | 601.30 | 0.08 | 2.75 | 1584 |
| 2024-09-20 22:21:33.100 | MS1 | 121.4656670941 | 31.1446286585 | 828 | 504990 | -85.81 | 17.45 | 481.43 | 0.05 | 2.07 | 1566 |
| 2024-09-20 22:21:34.579 | MS1 | 121.4656654629 | 31.1446310934 | 828 | 504990 | -90.22 | 13.21 | 41.63 | 0.15 | 2.09 | 1561 |
| 2024-09-20 22:21:35.731 | MS1 | 121.4656692668 | 31.1446313576 | 828 | 504990 | -85.37 | 17.55 | 81.31 | 0.15 | 2.61 | 1569 |
| 2024-09-20 22:21:36.961 | MS1 | 121.4656747937 | 31.1446190771 | 828 | 504990 | -87.26 | 13.71 | 93.56 | 0.01 | 2.99 | 1596 |
| 2024-09-20 22:21:37.134 | MS1 | 121.4656721616 | 31.1446286701 | 828 | 504990 | -90.48 | 8.22 | 62.49 | 0.11 | 2.42 | 1592 |
| 2024-09-20 22:21:38.539 | MS1 | 121.4656609659 | 31.1446349611 | 828 | 504990 | -90.84 | 11.25 | 101.67 | 0.05 | 2.94 | 1580 |
| 2024-09-20 22:21:39.161 | MS1 | 121.4656756468 | 31.1446217312 | 828 | 504990 | -93.19 | 12.34 | 60.13 | 0.14 | 2.43 | 1583 |
| 2024-09-20 22:21:40.601 | MS1 | 121.4656607451 | 31.1446248910 | 828 | 504990 | -92.04 | 8.00 | 460.25 | 0.04 | 2.65 | 1594 |
| 2024-09-20 22:21:41.180 | MS1 | 121.4656682933 | 31.1446353499 | 828 | 504990 | -89.79 | 11.36 | 507.18 | 0.19 | 2.80 | 1600 |
| 2024-09-20 22:21:42.166 | MS1 | 121.4656628354 | 31.1446255989 | 828 | 504990 | -91.11 | 10.39 | 358.98 | 0.12 | 2.62 | 1581 |

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
| 3210524 | 2 | 121.4740256150 | 31.1524292862 | 308 | 1 | 5 | 46.9 | TDD | 828 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3220845 | 4 | 121.4691926745 | 31.1532036715 | 153 | 9 | 7 | 16.0 | TDD | 898 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3248467 | 1 | 121.4739001649 | 31.1488898410 | 339 | 14 | 11 | 17.4 | TDD | 258 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3266639 | 3 | 121.4718370812 | 31.1480941705 | 258 | 11 | 2 | 48.1 | TDD | 772 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:31.061 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.077 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.197 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.197 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.869 | NREventA3 | measId:2;ServCellPCI:673;Se... |
| 2024-09-20 22:21:38.109 | NRHandoverAttempt | SourcePCI:673;SourceNR-ARFC... |
| 2024-09-20 22:21:38.159 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.170 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.279 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.279 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3248467 | 1 | 86.0727 | 76.0073 | -117.5540 | 13.4298 | 162.8807 | 0.0171 | 0.0087 |
| 2024_09_19 22:00 | 3210524 | 2 | 94.7507 | 85.4938 | -115.7032 | 16.3916 | 175.3167 | 0.0122 | 0.0039 |
| 2024_09_19 22:00 | 3266639 | 3 | 94.6022 | 82.2735 | -116.6502 | 5.7558 | 192.3945 | 0.0048 | 0.0115 |
| 2024_09_19 22:00 | 3220845 | 4 | 79.2352 | 88.4711 | -116.8527 | 8.3858 | 116.0094 | 0.0125 | 0.0122 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415840_F1D8877D | 504990 | 828 | -91.4 | 504990 | 772 | -95.7 | 504990 | 258 | -98.4 | 504990 | 898 |
| MR_1774415840_EEDB875B | 504990 | 828 | -91.0 | 504990 | 772 | -94.5 | 504990 | 258 | -98.3 | 504990 | 898 |
| MR_1774415840_9688F686 | 504990 | 828 | -90.2 | 504990 | 772 | -97.9 | 504990 | 258 | -98.6 | 504990 | 898 |
| MR_1774415840_3FB592E2 | 504990 | 828 | -92.2 | 504990 | 772 | -95.2 | 504990 | 258 | -98.3 | 504990 | 898 |
| MR_1774415840_15BD72D7 | 504990 | 828 | -89.8 | 504990 | 772 | -96.8 | 504990 | 258 | -97.6 | 504990 | 898 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1686: `7ca7486d-b27...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `7ca7486d-b27a-403c-be7a-fedb8b21d690` |
| Tag | **single-answer** |
| 정답 | **C2** |
| C2 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3212372_1 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1686] topology](images/train_1686.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment.
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3212372_1 **← 정답**
- `C3`: Decrease transmission power for 3212372_1
- `C4`: Add neighbor relationship between 3212372_1 and 3272726_4
- `C5`: Add neighbor relationship between 3269252_2 and 3272726_4
- `C6`: Adjust the azimuth of 3272726_4 by 50 degrees
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3212372_1
- `C8`: Check test server and transmission issues
- `C9`: Lift the tilt angle  of 3272726_4 by 8 degrees
- `C10`: Decrease A3 Offset threshold for 3272726_4
- `C11`: Increase A3 Offset threshold for 3272726_4
- `C12`: Increase transmission power for 3272726_4
- `C13`: Increase transmission power for 3212372_1
- `C14`: Increase A3 Offset threshold for 3212372_1
- `C15`: Lift the tilt angle of 3212372_1 by 1 degrees
- `C16`: Press down the tilt angle  of 3272726_4 by 8 degrees
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3272726_4
- `C18`: Decrease transmission power for 3272726_4
- `C19`: Decrease A3 Offset threshold for 3212372_1
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3272726_4
- `C21`: Press down the tilt angle of 3212372_1 by 1 degrees
- `C22`: Adjust the azimuth of 3212372_1 by 23 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.436 | MS1 | 121.4656750602 | 31.1446295133 | 302 | 504990 | -90.26 | 14.05 | 437.68 | 0.16 | 2.27 | 1561 |
| 2024-09-20 22:21:32.404 | MS1 | 121.4656621558 | 31.1446268638 | 302 | 504990 | -88.89 | 13.39 | 400.68 | 0.16 | 2.82 | 1582 |
| 2024-09-20 22:21:33.700 | MS1 | 121.4656682250 | 31.1446227985 | 302 | 504990 | -86.52 | 12.74 | 460.61 | 0.09 | 2.46 | 1562 |
| 2024-09-20 22:21:34.536 | MS1 | 121.4656592631 | 31.1446281079 | 302 | 504990 | -90.95 | 15.66 | 86.11 | 0.64 | 2.22 | 671 |
| 2024-09-20 22:21:35.217 | MS1 | 121.4656686559 | 31.1446345410 | 302 | 504990 | -91.47 | 12.21 | 58.40 | 0.52 | 2.89 | 588 |
| 2024-09-20 22:21:36.674 | MS1 | 121.4656694832 | 31.1446336640 | 302 | 504990 | -91.07 | 13.67 | 63.68 | 0.69 | 2.59 | 632 |
| 2024-09-20 22:21:37.720 | MS1 | 121.4656647524 | 31.1446271185 | 302 | 504990 | -89.07 | 8.57 | 93.07 | 0.65 | 2.96 | 694 |
| 2024-09-20 22:21:38.837 | MS1 | 121.4656596727 | 31.1446281266 | 302 | 504990 | -91.76 | 9.04 | 105.44 | 0.56 | 2.28 | 699 |
| 2024-09-20 22:21:39.839 | MS1 | 121.4656596733 | 31.1446241976 | 302 | 504990 | -91.64 | 11.55 | 63.46 | 0.51 | 2.27 | 568 |
| 2024-09-20 22:21:40.159 | MS1 | 121.4656610080 | 31.1446229857 | 302 | 504990 | -90.81 | 7.82 | 394.94 | 0.03 | 2.81 | 1563 |
| 2024-09-20 22:21:41.637 | MS1 | 121.4656766641 | 31.1446290695 | 302 | 504990 | -90.23 | 11.23 | 345.81 | 0.01 | 2.17 | 1583 |
| 2024-09-20 22:21:42.794 | MS1 | 121.4656630093 | 31.1446365153 | 302 | 504990 | -93.09 | 9.80 | 496.83 | 0.14 | 2.96 | 1580 |

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
| 3212372 | 1 | 121.4737271570 | 31.1553042051 | 236 | 0 | 11 | 32.3 | TDD | 302 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3219827 | 3 | 121.4746740945 | 31.1535393775 | 129 | 8 | 11 | 29.9 | TDD | 126 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3269252 | 2 | 121.4726528795 | 31.1461453228 | 299 | 1 | 10 | 26.1 | TDD | 132 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3272726 | 4 | 121.4669279608 | 31.1465907259 | 90 | 1 | 6 | 31.6 | TDD | 887 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |

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
| 2024-09-20 22:21:31.119 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.242 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.242 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.929 | NREventA3 | measId:2;ServCellPCI:728;Se... |
| 2024-09-20 22:21:38.169 | NRHandoverAttempt | SourcePCI:728;SourceNR-ARFC... |
| 2024-09-20 22:21:38.214 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.225 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.328 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.328 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3212372 | 1 | 15.2938 | 18.8023 | -114.4813 | 5.5722 | 162.4053 | 0.0132 | 0.0029 |
| 2024_09_20 22:00 | 3269252 | 2 | 6.2900 | 15.8794 | -115.0434 | 7.9322 | 148.4935 | 0.0072 | 0.0073 |
| 2024_09_20 22:00 | 3219827 | 3 | 11.9383 | 15.4710 | -117.7048 | 14.2404 | 136.3236 | 0.0013 | 0.0059 |
| 2024_09_20 22:00 | 3272726 | 4 | 9.9622 | 17.8058 | -116.4438 | 16.2846 | 163.6346 | 0.0098 | 0.0056 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414907_3A99492D | 504990 | 302 | -92.9 | 504990 | 887 | -91.0 | 504990 | 132 | -100.0 | 504990 | 126 |
| MR_1774414907_8811B11C | 504990 | 302 | -91.6 | 504990 | 887 | -92.8 | 504990 | 132 | -101.3 | 504990 | 126 |
| MR_1774414907_F73A254F | 504990 | 302 | -92.7 | 504990 | 887 | -92.2 | 504990 | 132 | -100.8 | 504990 | 126 |
| MR_1774414907_05BEC986 | 504990 | 302 | -92.2 | 504990 | 887 | -93.7 | 504990 | 132 | -102.4 | 504990 | 126 |
| MR_1774414907_58E1E006 | 504990 | 302 | -90.5 | 504990 | 887 | -92.8 | 504990 | 132 | -103.0 | 504990 | 126 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1687: `556e6c0a-dc1...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `556e6c0a-dc10-44ea-8571-85c2cd39953c` |
| Tag | **single-answer** |
| 정답 | **C22** |
| C22 의미 | Lift the tilt angle  of 3257076_2 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1687] topology](images/train_1687.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3212756_4
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3249226_1
- `C3`: Decrease A3 Offset threshold for 3249226_1
- `C4`: Add neighbor relationship between 3212756_4 and 3249226_1
- `C5`: Check test server and transmission issues
- `C6`: Lift the tilt angle of 3212756_4 by 6 degrees
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3212756_4
- `C8`: Increase A3 Offset threshold for 3249226_1
- `C9`: Insufficient data; more data is needed for judgment.
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3212756_4
- `C11`: Add neighbor relationship between 3257076_2 and 3249226_1
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3249226_1
- `C13`: Press down the tilt angle of 3212756_4 by 6 degrees
- `C14`: Decrease transmission power for 3212756_4
- `C15`: Increase A3 Offset threshold for 3212756_4
- `C16`: Adjust the azimuth of 3212756_4 by 48 degrees
- `C17`: Press down the tilt angle  of 3257076_2 by 10 degrees
- `C18`: Adjust the azimuth of 3257076_2 by 50 degrees
- `C19`: Increase transmission power for 3249226_1
- `C20`: Decrease transmission power for 3249226_1
- `C21`: Decrease A3 Offset threshold for 3212756_4
- `C22`: Lift the tilt angle  of 3257076_2 by 10 degrees **← 정답**

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.721 | MS1 | 121.4656644651 | 31.1446227209 | 165 | 504990 | -85.37 | 14.78 | 301.30 | 0.18 | 2.67 | 1584 |
| 2024-09-20 22:21:32.984 | MS1 | 121.4656626040 | 31.1446260838 | 165 | 504990 | -90.13 | 12.62 | 381.80 | 0.17 | 2.70 | 1581 |
| 2024-09-20 22:21:33.193 | MS1 | 121.4656627376 | 31.1446361442 | 165 | 504990 | -88.80 | 12.18 | 373.98 | 0.04 | 2.65 | 1566 |
| 2024-09-20 22:21:34.204 | MS1 | 121.4656628359 | 31.1446313536 | 165 | 504990 | -89.94 | 13.97 | 57.98 | 0.19 | 2.66 | 1574 |
| 2024-09-20 22:21:35.852 | MS1 | 121.4656696012 | 31.1446224929 | 165 | 504990 | -91.19 | 17.57 | 94.16 | 0.02 | 2.96 | 1582 |
| 2024-09-20 22:21:36.682 | MS1 | 121.4656739205 | 31.1446256461 | 165 | 504990 | -89.07 | 16.35 | 91.37 | 0.06 | 2.76 | 1577 |
| 2024-09-20 22:21:37.644 | MS1 | 121.4656762947 | 31.1446248929 | 165 | 504990 | -89.64 | 8.02 | 85.93 | 0.09 | 2.70 | 1592 |
| 2024-09-20 22:21:38.117 | MS1 | 121.4656645316 | 31.1446378819 | 165 | 504990 | -90.89 | 7.95 | 67.54 | 0.11 | 2.59 | 1596 |
| 2024-09-20 22:21:39.694 | MS1 | 121.4656750832 | 31.1446202186 | 165 | 504990 | -93.56 | 12.63 | 65.88 | 0.18 | 2.52 | 1589 |
| 2024-09-20 22:21:40.605 | MS1 | 121.4656698941 | 31.1446269523 | 165 | 504990 | -89.68 | 12.98 | 392.11 | 0.04 | 2.28 | 1562 |
| 2024-09-20 22:21:41.260 | MS1 | 121.4656600149 | 31.1446210539 | 165 | 504990 | -90.99 | 7.22 | 525.11 | 0.19 | 2.63 | 1587 |
| 2024-09-20 22:21:42.193 | MS1 | 121.4656774690 | 31.1446298300 | 165 | 504990 | -93.85 | 9.73 | 370.36 | 0.18 | 2.49 | 1560 |

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
| 3212756 | 4 | 121.4756346389 | 31.1514386628 | 279 | 4 | 12 | 40.2 | TDD | 165 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3217523 | 3 | 121.4643298677 | 31.1485893137 | 127 | 4 | 1 | 18.4 | TDD | 829 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3249226 | 1 | 121.4640398661 | 31.1520476181 | 282 | 9 | 7 | 48.8 | TDD | 105 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3257076 | 2 | 121.4739664041 | 31.1445269184 | 171 | 1 | 1 | 38.4 | TDD | 251 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |

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
| 2024-09-20 22:21:30.905 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.920 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.064 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.064 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.748 | NREventA3 | measId:2;ServCellPCI:989;Se... |
| 2024-09-20 22:21:37.988 | NRHandoverAttempt | SourcePCI:989;SourceNR-ARFC... |
| 2024-09-20 22:21:38.026 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.038 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.175 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.175 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3249226 | 1 | 19.3986 | 16.4423 | -114.7343 | 18.1535 | 85.6607 | 0.0037 | 0.0051 |
| 2024_09_20 22:00 | 3257076 | 2 | 7.8132 | 5.1245 | -115.2926 | 11.3788 | 147.1082 | 0.0081 | 0.0084 |
| 2024_09_20 22:00 | 3217523 | 3 | 7.8852 | 15.0644 | -117.1405 | 13.1741 | 88.3255 | 0.0015 | 0.0146 |
| 2024_09_20 22:00 | 3212756 | 4 | 75.4244 | 75.2341 | -115.3689 | 8.2192 | 171.3740 | 0.0197 | 0.0138 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415101_A0136068 | 504990 | 165 | -88.2 | 504990 | 105 | -92.5 | 504990 | 251 | -102.1 | 504990 | 829 |
| MR_1774415101_CCAC21A4 | 504990 | 165 | -90.8 | 504990 | 105 | -89.4 | 504990 | 251 | -104.1 | 504990 | 829 |
| MR_1774415101_06DACD24 | 504990 | 165 | -89.0 | 504990 | 105 | -89.0 | 504990 | 251 | -100.9 | 504990 | 829 |
| MR_1774415101_C539FEF2 | 504990 | 165 | -89.5 | 504990 | 105 | -91.9 | 504990 | 251 | -101.0 | 504990 | 829 |
| MR_1774415101_A9D1C6E2 | 504990 | 165 | -91.1 | 504990 | 105 | -92.5 | 504990 | 251 | -100.9 | 504990 | 829 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1688: `2b63d321-d87...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `2b63d321-d87b-403b-abaa-1f6038730778` |
| Tag | **single-answer** |
| 정답 | **C10** |
| C10 의미 | Add neighbor relationship between 3277563_2 and 3255154_4 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1688] topology](images/train_1688.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3255154_4
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3255154_4
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3255154_4
- `C4`: Decrease A3 Offset threshold for 3255154_4
- `C5`: Increase transmission power for 3255154_4
- `C6`: Add neighbor relationship between 3210841_3 and 3255154_4
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3277563_2
- `C8`: Decrease transmission power for 3255154_4
- `C9`: Insufficient data; more data is needed for judgment.
- `C10`: Add neighbor relationship between 3277563_2 and 3255154_4 **← 정답**
- `C11`: Press down the tilt angle of 3277563_2 by 10 degrees
- `C12`: Lift the tilt angle of 3277563_2 by 10 degrees
- `C13`: Decrease transmission power for 3277563_2
- `C14`: Adjust the azimuth of 3255154_4 by 9 degrees
- `C15`: Check test server and transmission issues
- `C16`: Decrease A3 Offset threshold for 3277563_2
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3277563_2
- `C18`: Increase A3 Offset threshold for 3277563_2
- `C19`: Increase transmission power for 3277563_2
- `C20`: Adjust the azimuth of 3277563_2 by 41 degrees
- `C21`: Press down the tilt angle  of 3255154_4 by 3 degrees
- `C22`: Lift the tilt angle  of 3255154_4 by 3 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.311 | MS1 | 121.4656765132 | 31.1446363312 | 444 | 504990 | -81.14 | 13.59 | 519.94 | 0.19 | 2.84 | 1593 |
| 2024-09-20 22:21:32.722 | MS1 | 121.4656702507 | 31.1446346542 | 444 | 504990 | -83.74 | 15.15 | 549.23 | 0.01 | 2.60 | 1594 |
| 2024-09-20 22:21:33.711 | MS1 | 121.4656593335 | 31.1446256015 | 444 | 504990 | -77.61 | 16.10 | 355.05 | 0.09 | 2.73 | 1561 |
| 2024-09-20 22:21:34.636 | MS1 | 121.4656734069 | 31.1446350297 | 444 | 504990 | -93.85 | -1.93 | 64.85 | 0.17 | 1.18 | 1561 |
| 2024-09-20 22:21:35.412 | MS1 | 121.4656704905 | 31.1446210582 | 444 | 504990 | -93.24 | -3.96 | 62.09 | 0.10 | 1.21 | 1572 |
| 2024-09-20 22:21:36.552 | MS1 | 121.4656669659 | 31.1446352280 | 444 | 504990 | -89.52 | -1.57 | 61.14 | 0.17 | 1.35 | 1599 |
| 2024-09-20 22:21:37.785 | MS1 | 121.4656628335 | 31.1446220612 | 444 | 504990 | -91.23 | -1.04 | 39.52 | 0.18 | 1.09 | 1593 |
| 2024-09-20 22:21:38.204 | MS1 | 121.4656714657 | 31.1446250870 | 444 | 504990 | -82.61 | 15.46 | 554.81 | 0.04 | 1.07 | 1581 |
| 2024-09-20 22:21:39.143 | MS1 | 121.4656632121 | 31.1446183405 | 444 | 504990 | -77.13 | 14.10 | 463.40 | 0.18 | 1.43 | 1573 |
| 2024-09-20 22:21:40.540 | MS1 | 121.4656595313 | 31.1446194656 | 444 | 504990 | -79.95 | 16.73 | 514.66 | 0.15 | 2.64 | 1577 |
| 2024-09-20 22:21:41.513 | MS1 | 121.4656721467 | 31.1446357216 | 444 | 504990 | -82.69 | 13.34 | 460.99 | 0.17 | 2.40 | 1585 |
| 2024-09-20 22:21:42.804 | MS1 | 121.4656619352 | 31.1446308455 | 444 | 504990 | -79.32 | 13.22 | 589.62 | 0.01 | 2.38 | 1575 |

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
| 3210841 | 3 | 121.4662378995 | 31.1513822273 | 194 | 6 | 5 | 25.8 | TDD | 132 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3222548 | 1 | 121.4718604792 | 31.1506253421 | 223 | 0 | 2 | 44.3 | TDD | 428 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3255154 | 4 | 121.4725704878 | 31.1493182063 | 241 | 0 | 9 | 49.0 | TDD | 727 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3277563 | 2 | 121.4711014844 | 31.1484185605 | 272 | 12 | 10 | 16.8 | TDD | 444 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:31.227 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.248 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.387 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.387 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.073 | NREventA3 | measId:2;ServCellPCI:855;Se... |
| 2024-09-20 22:21:36.073 | NREventA3 | measId:2;ServCellPCI:855;Se... |
| 2024-09-20 22:21:37.073 | NREventA3 | measId:2;ServCellPCI:855;Se... |
| 2024-09-20 22:21:39.573 | NRRRCReestablishAttempt | PCI:855 |
| 2024-09-20 22:21:39.588 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.600 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:39.723 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.723 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3222548 | 1 | 16.1841 | 8.3193 | -116.4223 | 10.6114 | 104.7872 | 0.0116 | 0.0160 |
| 2024_09_20 22:00 | 3277563 | 2 | 12.4914 | 14.9998 | -114.5889 | 15.6068 | 143.8857 | 0.0118 | 0.1247 |
| 2024_09_20 22:00 | 3210841 | 3 | 18.5715 | 13.9821 | -114.6515 | 10.8389 | 161.8145 | 0.0085 | 0.0013 |
| 2024_09_20 22:00 | 3255154 | 4 | 18.4787 | 5.3620 | -117.4245 | 8.3378 | 165.7702 | 0.0158 | 0.0127 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416562_BAD3DF6D | 504990 | 444 | -93.3 | 504990 | 727 | -87.0 | 504990 | 132 | -95.3 | 504990 | 428 |
| MR_1774416562_B68F35CE | 504990 | 727 | -89.8 | 504990 | 444 | -93.3 | 504990 | 132 | -97.8 | 504990 | 428 |
| MR_1774416562_F13BC9FB | 504990 | 444 | -94.9 | 504990 | 727 | -90.4 | 504990 | 132 | -95.2 | 504990 | 428 |
| MR_1774416562_1AB2D898 | 504990 | 444 | -94.4 | 504990 | 727 | -90.0 | 504990 | 132 | -95.2 | 504990 | 428 |
| MR_1774416562_16D9BEF9 | 504990 | 727 | -89.0 | 504990 | 444 | -93.5 | 504990 | 132 | -95.9 | 504990 | 428 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1689: `1f3033a4-b36...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `1f3033a4-b363-4d9a-8ec5-762de8c3abd2` |
| Tag | **single-answer** |
| 정답 | **C10** |
| C10 의미 | Decrease A3 Offset threshold for 3211635_3 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1689] topology](images/train_1689.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3211635_3 by 10 degrees
- `C2`: Lift the tilt angle  of 3249548_4 by 6 degrees
- `C3`: Lift the tilt angle of 3211635_3 by 10 degrees
- `C4`: Insufficient data; more data is needed for judgment.
- `C5`: Adjust the azimuth of 3211635_3 by 50 degrees
- `C6`: Adjust the azimuth of 3249548_4 by 50 degrees
- `C7`: Decrease transmission power for 3249548_4
- `C8`: Increase A3 Offset threshold for 3249548_4
- `C9`: Add neighbor relationship between 3211635_3 and 3249548_4
- `C10`: Decrease A3 Offset threshold for 3211635_3 **← 정답**
- `C11`: Increase A3 Offset threshold for 3211635_3
- `C12`: Check test server and transmission issues
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3249548_4
- `C14`: Increase transmission power for 3249548_4
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3211635_3
- `C16`: Decrease A3 Offset threshold for 3249548_4
- `C17`: Press down the tilt angle  of 3249548_4 by 6 degrees
- `C18`: Add neighbor relationship between 3260631_1 and 3249548_4
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3249548_4
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3211635_3
- `C21`: Increase transmission power for 3211635_3
- `C22`: Decrease transmission power for 3211635_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.478 | MS1 | 121.4656708698 | 31.1446198107 | 380 | 504990 | -83.22 | 12.55 | 511.71 | 0.16 | 2.48 | 1571 |
| 2024-09-20 22:21:32.331 | MS1 | 121.4656658814 | 31.1446307360 | 380 | 504990 | -77.38 | 13.62 | 389.10 | 0.14 | 2.29 | 1572 |
| 2024-09-20 22:21:33.561 | MS1 | 121.4656720262 | 31.1446353844 | 380 | 504990 | -82.21 | 12.67 | 460.26 | 0.06 | 2.61 | 1590 |
| 2024-09-20 22:21:34.486 | MS1 | 121.4656661426 | 31.1446213763 | 380 | 504990 | -85.83 | -0.51 | 65.68 | 0.13 | 1.22 | 1583 |
| 2024-09-20 22:21:35.593 | MS1 | 121.4656601640 | 31.1446332180 | 380 | 504990 | -85.87 | -2.58 | 33.45 | 0.10 | 1.46 | 1599 |
| 2024-09-20 22:21:36.659 | MS1 | 121.4656678412 | 31.1446285558 | 380 | 504990 | -83.05 | -3.30 | 44.63 | 0.19 | 1.26 | 1588 |
| 2024-09-20 22:21:37.611 | MS1 | 121.4656755986 | 31.1446318531 | 380 | 504990 | -90.43 | -0.98 | 46.75 | 0.05 | 1.30 | 1577 |
| 2024-09-20 22:21:38.717 | MS1 | 121.4656657476 | 31.1446379336 | 380 | 504990 | -84.17 | -1.37 | 70.38 | 0.17 | 1.28 | 1593 |
| 2024-09-20 22:21:39.889 | MS1 | 121.4656636133 | 31.1446236384 | 317 | 504990 | -77.04 | 16.86 | 194.11 | 0.07 | 1.48 | 1583 |
| 2024-09-20 22:21:40.243 | MS1 | 121.4656656320 | 31.1446184266 | 317 | 504990 | -80.55 | 17.45 | 494.08 | 0.05 | 2.86 | 1568 |
| 2024-09-20 22:21:41.672 | MS1 | 121.4656600885 | 31.1446260687 | 317 | 504990 | -79.06 | 12.40 | 323.65 | 0.19 | 2.83 | 1580 |
| 2024-09-20 22:21:42.590 | MS1 | 121.4656603499 | 31.1446218923 | 317 | 504990 | -79.57 | 15.50 | 424.62 | 0.17 | 2.68 | 1589 |

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
| 3211635 | 3 | 121.4700017319 | 31.1446869284 | 88 | 14 | 8 | 29.7 | TDD | 380 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3249548 | 4 | 121.4679590962 | 31.1483702499 | 294 | 4 | 9 | 15.8 | TDD | 317 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3260631 | 1 | 121.4727043207 | 31.1466170168 | 236 | 6 | 3 | 17.0 | TDD | 297 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3262981 | 2 | 121.4720184106 | 31.1497695230 | 291 | 2 | 4 | 45.1 | TDD | 450 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |

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
| 2024-09-20 22:21:30.957 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.979 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.090 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.090 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.772 | NREventA3 | measId:2;ServCellPCI:857;Se... |
| 2024-09-20 22:21:38.012 | NRHandoverAttempt | SourcePCI:857;SourceNR-ARFC... |
| 2024-09-20 22:21:38.051 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.065 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.194 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.194 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3260631 | 1 | 6.2145 | 5.2667 | -117.6082 | 15.7253 | 83.9452 | 0.0151 | 0.0078 |
| 2024_09_20 22:00 | 3262981 | 2 | 8.5905 | 7.8067 | -114.9316 | 18.5558 | 82.5389 | 0.0066 | 0.0147 |
| 2024_09_20 22:00 | 3211635 | 3 | 10.7090 | 18.7130 | -114.5044 | 11.1983 | 141.3914 | 0.0186 | 0.1420 |
| 2024_09_20 22:00 | 3249548 | 4 | 14.7831 | 7.3177 | -117.9398 | 13.7005 | 100.7352 | 0.0052 | 0.0103 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415525_21E0FECE | 504990 | 380 | -85.2 | 504990 | 317 | -80.9 | 504990 | 297 | -79.5 | 504990 | 450 |
| MR_1774415525_F8F90FCC | 504990 | 380 | -87.5 | 504990 | 317 | -81.3 | 504990 | 297 | -82.0 | 504990 | 450 |
| MR_1774415525_7314B61B | 504990 | 380 | -86.9 | 504990 | 317 | -81.8 | 504990 | 297 | -81.8 | 504990 | 450 |
| MR_1774415525_832FE8E3 | 504990 | 317 | -80.8 | 504990 | 380 | -87.5 | 504990 | 297 | -81.9 | 504990 | 450 |
| MR_1774415525_2C437A50 | 504990 | 380 | -85.3 | 504990 | 317 | -79.2 | 504990 | 297 | -78.4 | 504990 | 450 |
| MR_1774415525_80CBA7DA | 504990 | 380 | -84.8 | 504990 | 317 | -81.5 | 504990 | 297 | -80.8 | 504990 | 450 |
| MR_1774415525_1667D695 | 504990 | 380 | -86.4 | 504990 | 317 | -78.2 | 504990 | 297 | -80.9 | 504990 | 450 |
| MR_1774415525_ECB17076 | 504990 | 380 | -86.3 | 504990 | 317 | -82.0 | 504990 | 297 | -79.1 | 504990 | 450 |

> *... 2개 열 생략 (전체 14열)*

---
