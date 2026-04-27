# Track A 문제 분석 — train[1440]~train[1449]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[1440] ~ train[1449] (10개)

## 목차

1. [문제 1440: `fda970d9-1c8...`](#1440) — single-answer, 정답: C6
2. [문제 1441: `3251dabb-905...`](#1441) — single-answer, 정답: C12
3. [문제 1442: `2aa4d028-394...`](#1442) — single-answer, 정답: C18
4. [문제 1443: `51f6dba2-28b...`](#1443) — single-answer, 정답: C19
5. [문제 1444: `761d01b0-84c...`](#1444) — single-answer, 정답: C5
6. [문제 1445: `849df86a-125...`](#1445) — single-answer, 정답: C21
7. [문제 1446: `199ff4ff-b68...`](#1446) — multiple-answer, 정답: C17|C20
8. [문제 1447: `7e1f304e-bfc...`](#1447) — single-answer, 정답: C5
9. [문제 1448: `d2a0100a-aa8...`](#1448) — single-answer, 정답: C21
10. [문제 1449: `23355532-893...`](#1449) — single-answer, 정답: C15

---

### 문제 1440: `fda970d9-1c8...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `fda970d9-1c86-4ab8-8aa4-a6b038ac42e3` |
| Tag | **single-answer** |
| 정답 | **C6** |
| C6 의미 | Decrease A3 Offset threshold for 3241243_3 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1440] topology](images/train_1440.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3220760_4 and 3213928_1
- `C2`: Decrease transmission power for 3213928_1
- `C3`: Adjust the azimuth of 3241243_3 by 30 degrees
- `C4`: Insufficient data; more data is needed for judgment.
- `C5`: Decrease transmission power for 3241243_3
- `C6`: Decrease A3 Offset threshold for 3241243_3 **← 정답**
- `C7`: Increase A3 Offset threshold for 3213928_1
- `C8`: Increase transmission power for 3241243_3
- `C9`: Press down the tilt angle of 3241243_3 by 10 degrees
- `C10`: Lift the tilt angle of 3241243_3 by 10 degrees
- `C11`: Press down the tilt angle  of 3213928_1 by 4 degrees
- `C12`: Check test server and transmission issues
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3213928_1
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3241243_3
- `C15`: Increase transmission power for 3213928_1
- `C16`: Lift the tilt angle  of 3213928_1 by 4 degrees
- `C17`: Decrease A3 Offset threshold for 3213928_1
- `C18`: Increase A3 Offset threshold for 3241243_3
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3241243_3
- `C20`: Adjust the azimuth of 3213928_1 by 50 degrees
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3213928_1
- `C22`: Add neighbor relationship between 3241243_3 and 3213928_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.144 | MS1 | 121.4656671887 | 31.1446300783 | 843 | 504990 | -77.75 | 17.76 | 388.34 | 0.08 | 2.72 | 1586 |
| 2024-09-20 22:21:32.158 | MS1 | 121.4656603009 | 31.1446230644 | 843 | 504990 | -76.17 | 16.83 | 392.46 | 0.02 | 2.40 | 1573 |
| 2024-09-20 22:21:33.566 | MS1 | 121.4656623075 | 31.1446201739 | 843 | 504990 | -82.77 | 14.91 | 391.60 | 0.16 | 2.43 | 1579 |
| 2024-09-20 22:21:34.958 | MS1 | 121.4656705442 | 31.1446182874 | 843 | 504990 | -83.08 | -1.45 | 64.91 | 0.06 | 1.28 | 1580 |
| 2024-09-20 22:21:35.211 | MS1 | 121.4656608457 | 31.1446349497 | 843 | 504990 | -92.27 | -3.30 | 41.85 | 0.18 | 1.40 | 1564 |
| 2024-09-20 22:21:36.299 | MS1 | 121.4656672457 | 31.1446330255 | 843 | 504990 | -86.75 | -3.03 | 37.92 | 0.14 | 1.45 | 1572 |
| 2024-09-20 22:21:37.763 | MS1 | 121.4656658345 | 31.1446325431 | 843 | 504990 | -84.83 | -1.78 | 48.39 | 0.02 | 1.30 | 1598 |
| 2024-09-20 22:21:38.530 | MS1 | 121.4656772438 | 31.1446289729 | 843 | 504990 | -90.40 | -3.79 | 34.46 | 0.14 | 1.39 | 1599 |
| 2024-09-20 22:21:39.581 | MS1 | 121.4656769182 | 31.1446289007 | 313 | 504990 | -76.74 | 16.25 | 221.45 | 0.18 | 1.30 | 1595 |
| 2024-09-20 22:21:40.555 | MS1 | 121.4656590526 | 31.1446316197 | 313 | 504990 | -78.37 | 16.20 | 561.99 | 0.09 | 2.69 | 1568 |
| 2024-09-20 22:21:41.190 | MS1 | 121.4656588301 | 31.1446251668 | 313 | 504990 | -79.61 | 17.70 | 461.69 | 0.17 | 2.95 | 1599 |
| 2024-09-20 22:21:42.159 | MS1 | 121.4656636881 | 31.1446303307 | 313 | 504990 | -84.81 | 16.45 | 548.16 | 0.07 | 2.76 | 1597 |

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
| 3213928 | 1 | 121.4656039228 | 31.1536427071 | 121 | 1 | 2 | 45.0 | TDD | 313 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3220760 | 4 | 121.4644521277 | 31.1503487536 | 344 | 8 | 4 | 31.8 | TDD | 420 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3241243 | 3 | 121.4667280472 | 31.1442054046 | 325 | 11 | 11 | 23.1 | TDD | 843 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3241544 | 2 | 121.4664665032 | 31.1555165670 | 43 | 15 | 6 | 35.9 | TDD | 906 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |

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
| 2024-09-20 22:21:31.002 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.027 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.173 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.173 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.816 | NREventA3 | measId:2;ServCellPCI:272;Se... |
| 2024-09-20 22:21:38.056 | NRHandoverAttempt | SourcePCI:272;SourceNR-ARFC... |
| 2024-09-20 22:21:38.098 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.112 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.233 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.233 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3213928 | 1 | 17.7076 | 11.4082 | -115.7020 | 10.8258 | 187.5236 | 0.0111 | 0.0188 |
| 2024_09_20 22:00 | 3241544 | 2 | 8.0476 | 13.4595 | -117.4141 | 17.3645 | 135.3814 | 0.0173 | 0.0074 |
| 2024_09_20 22:00 | 3241243 | 3 | 16.7384 | 6.1703 | -116.3914 | 15.4569 | 175.3757 | 0.0005 | 0.1575 |
| 2024_09_20 22:00 | 3220760 | 4 | 8.7359 | 17.1990 | -116.6626 | 5.2759 | 179.1890 | 0.0105 | 0.0158 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415356_7A450550 | 504990 | 313 | -75.4 | 504990 | 843 | -84.0 | 504990 | 420 | -77.7 | 504990 | 906 |
| MR_1774415356_DB98ACB3 | 504990 | 843 | -83.1 | 504990 | 313 | -75.1 | 504990 | 420 | -77.8 | 504990 | 906 |
| MR_1774415356_8A9BAB65 | 504990 | 313 | -75.2 | 504990 | 843 | -83.6 | 504990 | 420 | -80.9 | 504990 | 906 |
| MR_1774415356_61256DDA | 504990 | 843 | -81.1 | 504990 | 313 | -77.7 | 504990 | 420 | -78.0 | 504990 | 906 |
| MR_1774415356_33E90F78 | 504990 | 843 | -83.0 | 504990 | 313 | -76.6 | 504990 | 420 | -77.2 | 504990 | 906 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1441: `3251dabb-905...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `3251dabb-905f-4b93-8728-0fb962b7043c` |
| Tag | **single-answer** |
| 정답 | **C12** |
| C12 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3264707_6 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1441] topology](images/train_1441.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3237717_3 by 4 degrees
- `C2`: Increase transmission power for 3237717_3
- `C3`: Lift the tilt angle of 3264707_6 by 1 degrees
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3237717_3
- `C5`: Decrease A3 Offset threshold for 3264707_6
- `C6`: Insufficient data; more data is needed for judgment.
- `C7`: Adjust the azimuth of 3264707_6 by 28 degrees
- `C8`: Adjust the azimuth of 3237717_3 by 9 degrees
- `C9`: Add neighbor relationship between 3213557_11 and 3237717_3
- `C10`: Decrease transmission power for 3264707_6
- `C11`: Decrease A3 Offset threshold for 3237717_3
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3264707_6 **← 정답**
- `C13`: Lift the tilt angle  of 3237717_3 by 4 degrees
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3237717_3
- `C15`: Check test server and transmission issues
- `C16`: Increase A3 Offset threshold for 3264707_6
- `C17`: Increase transmission power for 3264707_6
- `C18`: Decrease transmission power for 3237717_3
- `C19`: Increase A3 Offset threshold for 3237717_3
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3264707_6
- `C21`: Press down the tilt angle of 3264707_6 by 1 degrees
- `C22`: Add neighbor relationship between 3264707_6 and 3237717_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.601 | MS1 | 121.4656648671 | 31.1446352933 | 699 | 504990 | -94.52 | 14.64 | 432.49 | 0.12 | 2.83 | 1597 |
| 2024-09-20 22:21:32.968 | MS1 | 121.4656582183 | 31.1446373144 | 259 | 504990 | -94.34 | 13.77 | 404.18 | 0.05 | 2.84 | 1594 |
| 2024-09-20 22:21:33.345 | MS1 | 121.4656652089 | 31.1446229536 | 427 | 504990 | -94.95 | 14.75 | 430.28 | 0.20 | 2.41 | 1570 |
| 2024-09-20 22:21:34.432 | MS1 | 121.4656666972 | 31.1446319823 | 191 | 152650 | -89.54 | 3.85 | 53.69 | 0.16 | 1.90 | 970 |
| 2024-09-20 22:21:35.308 | MS1 | 121.4656700290 | 31.1446297210 | 383 | 152650 | -89.68 | 4.74 | 45.69 | 0.20 | 1.88 | 901 |
| 2024-09-20 22:21:36.383 | MS1 | 121.4656688264 | 31.1446200377 | 439 | 152650 | -87.98 | 2.56 | 60.33 | 0.05 | 1.75 | 933 |
| 2024-09-20 22:21:37.629 | MS1 | 121.4656732931 | 31.1446234241 | 657 | 152650 | -88.25 | 7.67 | 51.17 | 0.18 | 1.90 | 917 |
| 2024-09-20 22:21:38.385 | MS1 | 121.4656758149 | 31.1446265707 | 191 | 152650 | -88.57 | 6.58 | 80.63 | 0.03 | 1.97 | 996 |
| 2024-09-20 22:21:39.787 | MS1 | 121.4656758627 | 31.1446244452 | 383 | 152650 | -88.19 | 6.04 | 59.39 | 0.18 | 1.94 | 901 |
| 2024-09-20 22:21:40.936 | MS1 | 121.4656637273 | 31.1446213133 | 439 | 152650 | -89.83 | 4.02 | 79.19 | 0.07 | 2.12 | 1600 |
| 2024-09-20 22:21:41.325 | MS1 | 121.4656692294 | 31.1446195929 | 657 | 152650 | -94.10 | 5.12 | 74.25 | 0.16 | 2.03 | 1595 |
| 2024-09-20 22:21:42.838 | MS1 | 121.4656724342 | 31.1446357756 | 191 | 152650 | -87.43 | 4.21 | 81.36 | 0.17 | 2.36 | 1571 |

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
| 3213001 | 5 | 121.4640094834 | 31.1541774646 | 183 | 7 | 6 | 20.3 | TDD | 237 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3213557 | 11 | 121.4659825834 | 31.1464076552 | 104 | 13 | 10 | 11.6 | FDD | 439 | n1 | 152650 | 30M | 4T4R | 24 | 152650 |
| 3225246 | 12 | 121.4673921860 | 31.1507544894 | 274 | 7 | 0 | 15.4 | FDD | 379 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |
| 3226255 | 1 | 121.4703814128 | 31.1455139884 | 104 | 14 | 7 | 28.8 | TDD | 259 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3227477 | 8 | 121.4759638768 | 31.1441188756 | 92 | 9 | 8 | 10.8 | FDD | 223 | n1 | 152650 | 30M | 4T4R | 13 | 152650 |
| 3237717 | 3 | 121.4673421414 | 31.1498432011 | 186 | 2 | 2 | 18.5 | TDD | 395 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3240819 | 4 | 121.4682539954 | 31.1442878759 | 270 | 11 | 12 | 12.0 | TDD | 427 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3249602 | 9 | 121.4744220604 | 31.1541705968 | 341 | 0 | 3 | 20.8 | FDD | 551 | n1 | 152650 | 30M | 4T4R | 11 | 152650 |
| 3252001 | 2 | 121.4757986265 | 31.1453551706 | 330 | 9 | 6 | 8.2 | TDD | 614 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3252741 | 10 | 121.4653979787 | 31.1493412693 | 87 | 15 | 7 | 26.8 | FDD | 657 | n1 | 152650 | 30M | 4T4R | 26 | 152650 |
| 3254323 | 13 | 121.4654707086 | 31.1492019162 | 33 | 11 | 1 | 18.3 | FDD | 383 | n1 | 152650 | 30M | 4T4R | 10 | 152650 |
| 3264707 | 6 | 121.4658542061 | 31.1467241039 | 156 | 0 | 4 | 4.9 | TDD | 699 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3270169 | 7 | 121.4661072224 | 31.1448557616 | 255 | 6 | 12 | 5.7 | FDD | 191 | n1 | 152650 | 30M | 4T4R | 18 | 152650 |

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
| 2024-09-20 22:21:30.969 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.992 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.113 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.113 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.770 | NREventA2 | measId:1;ServCellPCI:344;Se... |
| 2024-09-20 22:21:34.904 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.202 | NREventA5 | measId:3;ServCellPCI:344;Se... |
| 2024-09-20 22:21:35.268 | NRHandoverAttempt | SourcePCI:344;SourceNR-ARFC... |
| 2024-09-20 22:21:35.318 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.330 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:35.475 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.475 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3226255 | 1 | 19.1217 | 6.3621 | -115.1723 | 12.8489 | 85.7898 | 0.0053 | 0.0167 |
| 2024_09_20 22:00 | 3252001 | 2 | 16.3110 | 18.4622 | -115.4252 | 16.6867 | 103.0267 | 0.0042 | 0.0076 |
| 2024_09_20 22:00 | 3237717 | 3 | 9.7714 | 7.9012 | -116.9190 | 11.9748 | 151.7377 | 0.0174 | 0.0042 |
| 2024_09_20 22:00 | 3240819 | 4 | 7.7838 | 11.0710 | -114.4054 | 11.5828 | 154.0236 | 0.0039 | 0.0130 |
| 2024_09_20 22:00 | 3213001 | 5 | 15.9321 | 13.0945 | -115.4731 | 12.1270 | 123.8138 | 0.0102 | 0.0064 |
| 2024_09_20 22:00 | 3264707 | 6 | 8.8976 | 9.5725 | -117.2839 | 9.4660 | 136.4638 | 0.0085 | 0.0044 |
| 2024_09_20 22:00 | 3270169 | 7 | 11.5568 | 16.8270 | -114.3266 | 3.5647 | 25.1257 | 0.0192 | 0.0183 |
| 2024_09_20 22:00 | 3227477 | 8 | 8.9049 | 5.1739 | -116.9882 | 4.7524 | 45.4733 | 0.0200 | 0.0131 |
| 2024_09_20 22:00 | 3249602 | 9 | 15.8624 | 19.2990 | -117.2435 | 4.1280 | 45.7158 | 0.0047 | 0.0109 |
| 2024_09_20 22:00 | 3252741 | 10 | 17.2828 | 18.5126 | -117.0053 | 4.4577 | 59.6034 | 0.0175 | 0.0137 |
| 2024_09_20 22:00 | 3213557 | 11 | 12.8143 | 7.5189 | -115.0387 | 3.1670 | 25.1298 | 0.0136 | 0.0110 |
| 2024_09_20 22:00 | 3225246 | 12 | 18.7604 | 14.9432 | -116.2900 | 3.5015 | 45.1190 | 0.0017 | 0.0072 |
| 2024_09_20 22:00 | 3254323 | 13 | 14.1663 | 16.0486 | -115.2580 | 3.8682 | 31.9438 | 0.0137 | 0.0047 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414744_9BCFB3B6 | 152650 | 191 | -88.3 | 152650 | 379 | -92.3 | 152650 | 223 | -97.4 | 152650 | 551 |
| MR_1774414744_0CB56ED0 | 504990 | 427 | -94.4 | 504990 | 395 | -98.5 | 504990 | 237 | -97.7 | 504990 | 614 |
| MR_1774414744_5B87B3AB | 504990 | 427 | -95.2 | 504990 | 395 | -97.7 | 504990 | 237 | -98.1 | 504990 | 614 |
| MR_1774414744_C44187A5 | 152650 | 191 | -90.3 | 152650 | 379 | -93.4 | 152650 | 223 | -97.7 | 152650 | 551 |
| MR_1774414744_07D23D29 | 152650 | 191 | -91.3 | 152650 | 379 | -92.7 | 152650 | 223 | -98.1 | 152650 | 551 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1442: `2aa4d028-394...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `2aa4d028-394f-4184-a7f3-732adb000e18` |
| Tag | **single-answer** |
| 정답 | **C18** |
| C18 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1442] topology](images/train_1442.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3246770_2 and 3227492_4
- `C2`: Decrease transmission power for 3227492_4
- `C3`: Press down the tilt angle  of 3227492_4 by 9 degrees
- `C4`: Increase A3 Offset threshold for 3224812_1
- `C5`: Lift the tilt angle  of 3227492_4 by 9 degrees
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3227492_4
- `C7`: Decrease A3 Offset threshold for 3224812_1
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3227492_4
- `C9`: Increase A3 Offset threshold for 3227492_4
- `C10`: Press down the tilt angle of 3224812_1 by 10 degrees
- `C11`: Decrease A3 Offset threshold for 3227492_4
- `C12`: Increase transmission power for 3224812_1
- `C13`: Adjust the azimuth of 3224812_1 by 50 degrees
- `C14`: Lift the tilt angle of 3224812_1 by 10 degrees
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3224812_1
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3224812_1
- `C17`: Add neighbor relationship between 3224812_1 and 3227492_4
- `C18`: Insufficient data; more data is needed for judgment. **← 정답**
- `C19`: Increase transmission power for 3227492_4
- `C20`: Check test server and transmission issues
- `C21`: Decrease transmission power for 3224812_1
- `C22`: Adjust the azimuth of 3227492_4 by 50 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.755 | MS1 | 121.4656686860 | 31.1446181460 | 186 | 504990 | -86.26 | 15.65 | 301.20 | 0.17 | 2.90 | 1561 |
| 2024-09-20 22:21:32.806 | MS1 | 121.4656637559 | 31.1446280577 | 186 | 504990 | -87.71 | 16.54 | 466.60 | 0.02 | 2.28 | 1576 |
| 2024-09-20 22:21:33.331 | MS1 | 121.4656760351 | 31.1446322598 | 186 | 504990 | -86.04 | 13.19 | 552.71 | 0.08 | 2.44 | 1589 |
| 2024-09-20 22:21:34.734 | MS1 | 121.4656712185 | 31.1446367215 | 186 | 504990 | -91.99 | 14.98 | 64.63 | 0.12 | 2.72 | 1580 |
| 2024-09-20 22:21:35.675 | MS1 | 121.4656647658 | 31.1446257447 | 186 | 504990 | -86.77 | 13.97 | 91.50 | 0.15 | 2.30 | 1584 |
| 2024-09-20 22:21:36.707 | MS1 | 121.4656750649 | 31.1446322312 | 186 | 504990 | -86.76 | 14.00 | 50.97 | 0.10 | 2.51 | 1585 |
| 2024-09-20 22:21:37.197 | MS1 | 121.4656694370 | 31.1446217967 | 186 | 504990 | -93.07 | 8.88 | 74.94 | 0.02 | 2.33 | 1561 |
| 2024-09-20 22:21:38.851 | MS1 | 121.4656704062 | 31.1446323045 | 186 | 504990 | -91.58 | 9.93 | 78.91 | 0.05 | 2.41 | 1582 |
| 2024-09-20 22:21:39.785 | MS1 | 121.4656726194 | 31.1446317638 | 186 | 504990 | -89.71 | 8.94 | 72.16 | 0.05 | 2.33 | 1578 |
| 2024-09-20 22:21:40.155 | MS1 | 121.4656678302 | 31.1446238871 | 186 | 504990 | -93.18 | 12.59 | 394.31 | 0.20 | 2.59 | 1589 |
| 2024-09-20 22:21:41.712 | MS1 | 121.4656645503 | 31.1446313180 | 186 | 504990 | -92.67 | 8.79 | 438.03 | 0.12 | 2.59 | 1592 |
| 2024-09-20 22:21:42.343 | MS1 | 121.4656596426 | 31.1446229843 | 186 | 504990 | -90.49 | 12.59 | 303.75 | 0.14 | 2.59 | 1577 |

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
| 3224812 | 1 | 121.4721737899 | 31.1495997537 | 343 | 9 | 7 | 39.5 | TDD | 186 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3226490 | 3 | 121.4707075098 | 31.1529366789 | 49 | 2 | 7 | 19.7 | TDD | 276 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3227492 | 4 | 121.4726069526 | 31.1530390289 | 285 | 8 | 0 | 27.3 | TDD | 127 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3246770 | 2 | 121.4656113973 | 31.1487534506 | 271 | 0 | 0 | 28.2 | TDD | 244 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:31.592 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.607 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.745 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.745 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.471 | NREventA3 | measId:2;ServCellPCI:776;Se... |
| 2024-09-20 22:21:38.711 | NRHandoverAttempt | SourcePCI:776;SourceNR-ARFC... |
| 2024-09-20 22:21:38.752 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.766 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.897 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.897 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3224812 | 1 | 91.3148 | 89.3122 | -116.0936 | 13.9725 | 142.8776 | 0.0037 | 0.0117 |
| 2024_09_19 22:00 | 3246770 | 2 | 94.8027 | 75.5167 | -116.6264 | 9.2357 | 107.2411 | 0.0137 | 0.0101 |
| 2024_09_19 22:00 | 3226490 | 3 | 90.9401 | 82.5955 | -116.9970 | 6.9464 | 197.8914 | 0.0075 | 0.0125 |
| 2024_09_19 22:00 | 3227492 | 4 | 92.8856 | 93.9778 | -116.1248 | 6.6811 | 116.9141 | 0.0172 | 0.0062 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413506_6BB5B2C6 | 504990 | 186 | -93.5 | 504990 | 127 | -93.0 | 504990 | 244 | -105.8 | 504990 | 276 |
| MR_1774413506_54FED56A | 504990 | 186 | -92.9 | 504990 | 127 | -90.9 | 504990 | 244 | -102.7 | 504990 | 276 |
| MR_1774413506_C37404B2 | 504990 | 186 | -91.0 | 504990 | 127 | -91.9 | 504990 | 244 | -103.3 | 504990 | 276 |
| MR_1774413506_F986D8E2 | 504990 | 186 | -90.5 | 504990 | 127 | -92.9 | 504990 | 244 | -105.9 | 504990 | 276 |
| MR_1774413506_29BE1B93 | 504990 | 186 | -90.1 | 504990 | 127 | -93.5 | 504990 | 244 | -105.5 | 504990 | 276 |
| MR_1774413506_7B353874 | 504990 | 186 | -90.7 | 504990 | 127 | -90.3 | 504990 | 244 | -105.1 | 504990 | 276 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1443: `51f6dba2-28b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `51f6dba2-28b9-47be-80c6-7b1c81df8892` |
| Tag | **single-answer** |
| 정답 | **C19** |
| C19 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3264540_1 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1443] topology](images/train_1443.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3264540_1 and 3255449_4
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3264540_1
- `C3`: Adjust the azimuth of 3255449_4 by 29 degrees
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3255449_4
- `C5`: Adjust the azimuth of 3264540_1 by 27 degrees
- `C6`: Increase transmission power for 3264540_1
- `C7`: Check test server and transmission issues
- `C8`: Increase A3 Offset threshold for 3255449_4
- `C9`: Decrease A3 Offset threshold for 3255449_4
- `C10`: Increase A3 Offset threshold for 3264540_1
- `C11`: Lift the tilt angle  of 3255449_4 by 3 degrees
- `C12`: Press down the tilt angle of 3264540_1 by 3 degrees
- `C13`: Insufficient data; more data is needed for judgment.
- `C14`: Decrease transmission power for 3264540_1
- `C15`: Decrease A3 Offset threshold for 3264540_1
- `C16`: Lift the tilt angle of 3264540_1 by 3 degrees
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3255449_4
- `C18`: Press down the tilt angle  of 3255449_4 by 3 degrees
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3264540_1 **← 정답**
- `C20`: Add neighbor relationship between 3248696_9 and 3255449_4
- `C21`: Increase transmission power for 3255449_4
- `C22`: Decrease transmission power for 3255449_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.908 | MS1 | 121.4656750432 | 31.1446269459 | 547 | 504990 | -94.54 | 12.65 | 529.71 | 0.12 | 2.69 | 1591 |
| 2024-09-20 22:21:32.591 | MS1 | 121.4656753623 | 31.1446339365 | 995 | 504990 | -93.97 | 14.82 | 380.31 | 0.05 | 2.18 | 1572 |
| 2024-09-20 22:21:33.345 | MS1 | 121.4656669857 | 31.1446344702 | 500 | 504990 | -94.53 | 9.31 | 369.49 | 0.03 | 2.20 | 1579 |
| 2024-09-20 22:21:34.259 | MS1 | 121.4656688123 | 31.1446217762 | 128 | 152650 | -91.99 | 5.69 | 51.94 | 0.07 | 1.99 | 934 |
| 2024-09-20 22:21:35.429 | MS1 | 121.4656702102 | 31.1446241787 | 575 | 152650 | -93.91 | 5.10 | 94.31 | 0.10 | 1.92 | 981 |
| 2024-09-20 22:21:36.309 | MS1 | 121.4656736228 | 31.1446194008 | 389 | 152650 | -96.88 | 2.32 | 82.94 | 0.06 | 1.86 | 932 |
| 2024-09-20 22:21:37.634 | MS1 | 121.4656711383 | 31.1446200633 | 866 | 152650 | -91.22 | 3.14 | 60.81 | 0.08 | 1.69 | 976 |
| 2024-09-20 22:21:38.400 | MS1 | 121.4656621526 | 31.1446182523 | 128 | 152650 | -92.19 | 7.99 | 62.94 | 0.04 | 1.93 | 962 |
| 2024-09-20 22:21:39.940 | MS1 | 121.4656593511 | 31.1446266920 | 575 | 152650 | -96.57 | 3.96 | 55.86 | 0.07 | 1.60 | 910 |
| 2024-09-20 22:21:40.658 | MS1 | 121.4656697190 | 31.1446250094 | 389 | 152650 | -94.23 | 3.97 | 85.27 | 0.18 | 2.57 | 1587 |
| 2024-09-20 22:21:41.453 | MS1 | 121.4656662709 | 31.1446246978 | 866 | 152650 | -94.74 | 2.33 | 49.93 | 0.09 | 2.54 | 1567 |
| 2024-09-20 22:21:42.826 | MS1 | 121.4656673855 | 31.1446299457 | 128 | 152650 | -96.50 | 5.79 | 61.08 | 0.14 | 2.11 | 1583 |

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
| 3218188 | 11 | 121.4715997993 | 31.1533473284 | 20 | 10 | 8 | 19.9 | FDD | 218 | n1 | 152650 | 30M | 4T4R | 23 | 152650 |
| 3224124 | 7 | 121.4643857890 | 31.1487967827 | 328 | 7 | 2 | 18.1 | FDD | 128 | n1 | 152650 | 30M | 4T4R | 24 | 152650 |
| 3235482 | 13 | 121.4657676816 | 31.1530887453 | 108 | 12 | 9 | 23.8 | FDD | 575 | n1 | 152650 | 30M | 4T4R | 26 | 152650 |
| 3243527 | 10 | 121.4703426102 | 31.1534012582 | 319 | 13 | 4 | 5.2 | FDD | 526 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |
| 3248696 | 9 | 121.4644951806 | 31.1446869237 | 312 | 2 | 8 | 24.2 | FDD | 389 | n1 | 152650 | 30M | 4T4R | 22 | 152650 |
| 3252460 | 5 | 121.4733998952 | 31.1498187647 | 141 | 11 | 12 | 3.3 | TDD | 877 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3255449 | 4 | 121.4646498663 | 31.1544690548 | 146 | 2 | 2 | 20.2 | TDD | 902 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3256472 | 12 | 121.4745786819 | 31.1472521885 | 99 | 5 | 7 | 9.9 | FDD | 221 | n1 | 152650 | 30M | 4T4R | 15 | 152650 |
| 3264540 | 1 | 121.4720513439 | 31.1460656371 | 282 | 2 | 9 | 15.3 | TDD | 547 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3267492 | 2 | 121.4649444276 | 31.1530038165 | 264 | 11 | 7 | 25.0 | TDD | 995 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3274604 | 6 | 121.4643311384 | 31.1499400636 | 344 | 1 | 1 | 7.5 | TDD | 500 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3276176 | 3 | 121.4656389116 | 31.1460404303 | 316 | 6 | 0 | 22.8 | TDD | 453 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3279479 | 8 | 121.4686889768 | 31.1533771714 | 212 | 8 | 12 | 0.5 | FDD | 866 | n1 | 152650 | 30M | 4T4R | 12 | 152650 |

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
| 2024-09-20 22:21:30.910 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.930 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.034 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.034 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.741 | NREventA2 | measId:1;ServCellPCI:569;Se... |
| 2024-09-20 22:21:34.845 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.145 | NREventA5 | measId:3;ServCellPCI:569;Se... |
| 2024-09-20 22:21:35.178 | NRHandoverAttempt | SourcePCI:569;SourceNR-ARFC... |
| 2024-09-20 22:21:35.216 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.231 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:35.373 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.373 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3264540 | 1 | 13.6556 | 19.9661 | -114.4056 | 19.4297 | 155.4530 | 0.0107 | 0.0035 |
| 2024_09_20 22:00 | 3267492 | 2 | 7.1553 | 7.2208 | -117.7397 | 15.4720 | 154.0775 | 0.0161 | 0.0143 |
| 2024_09_20 22:00 | 3276176 | 3 | 15.2268 | 11.9329 | -115.1543 | 18.1345 | 163.4698 | 0.0155 | 0.0172 |
| 2024_09_20 22:00 | 3255449 | 4 | 11.2973 | 6.1239 | -114.8639 | 17.2423 | 118.5635 | 0.0032 | 0.0037 |
| 2024_09_20 22:00 | 3252460 | 5 | 16.9077 | 19.7028 | -114.7604 | 7.3712 | 140.6550 | 0.0072 | 0.0155 |
| 2024_09_20 22:00 | 3274604 | 6 | 11.8260 | 10.0204 | -114.7435 | 9.7313 | 119.2584 | 0.0067 | 0.0116 |
| 2024_09_20 22:00 | 3224124 | 7 | 19.7143 | 13.9454 | -114.4185 | 3.9994 | 49.3742 | 0.0126 | 0.0110 |
| 2024_09_20 22:00 | 3279479 | 8 | 17.2956 | 9.0160 | -116.1304 | 3.6640 | 23.9232 | 0.0125 | 0.0161 |
| 2024_09_20 22:00 | 3248696 | 9 | 16.0847 | 12.7817 | -115.7054 | 3.1243 | 27.6954 | 0.0154 | 0.0053 |
| 2024_09_20 22:00 | 3243527 | 10 | 6.1752 | 7.4599 | -115.9485 | 3.3410 | 22.6303 | 0.0138 | 0.0076 |
| 2024_09_20 22:00 | 3218188 | 11 | 9.9466 | 12.6684 | -117.7112 | 3.3871 | 40.8439 | 0.0021 | 0.0078 |
| 2024_09_20 22:00 | 3256472 | 12 | 6.9314 | 17.2376 | -115.6044 | 3.1787 | 27.3635 | 0.0001 | 0.0141 |
| 2024_09_20 22:00 | 3235482 | 13 | 7.4046 | 18.1694 | -115.5100 | 4.7147 | 44.6391 | 0.0193 | 0.0195 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413880_F81C7F2E | 504990 | 500 | -96.5 | 504990 | 902 | -96.4 | 504990 | 453 | -99.9 | 504990 | 877 |
| MR_1774413880_9F68EE63 | 152650 | 128 | -90.6 | 152650 | 526 | -98.9 | 152650 | 221 | -102.3 | 152650 | 218 |
| MR_1774413880_7527458D | 504990 | 500 | -95.1 | 504990 | 902 | -95.9 | 504990 | 453 | -98.9 | 504990 | 877 |
| MR_1774413880_02EA8B42 | 152650 | 128 | -92.3 | 152650 | 526 | -99.5 | 152650 | 221 | -103.2 | 152650 | 218 |
| MR_1774413880_784C5FE4 | 504990 | 500 | -93.7 | 504990 | 902 | -96.0 | 504990 | 453 | -99.9 | 504990 | 877 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1444: `761d01b0-84c...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `761d01b0-84cd-455f-842d-af1731964d26` |
| Tag | **single-answer** |
| 정답 | **C5** |
| C5 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1444] topology](images/train_1444.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3261432_1
- `C2`: Add neighbor relationship between 3214834_2 and 3261432_1
- `C3`: Lift the tilt angle of 3237084_4 by 6 degrees
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3261432_1
- `C5`: Check test server and transmission issues **← 정답**
- `C6`: Adjust the azimuth of 3237084_4 by 50 degrees
- `C7`: Press down the tilt angle  of 3261432_1 by 10 degrees
- `C8`: Adjust the azimuth of 3261432_1 by 50 degrees
- `C9`: Add neighbor relationship between 3237084_4 and 3261432_1
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3237084_4
- `C11`: Decrease transmission power for 3261432_1
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3261432_1
- `C13`: Decrease transmission power for 3237084_4
- `C14`: Increase transmission power for 3261432_1
- `C15`: Decrease A3 Offset threshold for 3237084_4
- `C16`: Increase A3 Offset threshold for 3237084_4
- `C17`: Decrease A3 Offset threshold for 3261432_1
- `C18`: Insufficient data; more data is needed for judgment.
- `C19`: Press down the tilt angle of 3237084_4 by 6 degrees
- `C20`: Increase transmission power for 3237084_4
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3237084_4
- `C22`: Lift the tilt angle  of 3261432_1 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.886 | MS1 | 121.4656677215 | 31.1446290094 | 236 | 504990 | -86.36 | 14.93 | 314.18 | 0.14 | 2.11 | 1564 |
| 2024-09-20 22:21:32.331 | MS1 | 121.4656761160 | 31.1446343104 | 236 | 504990 | -89.04 | 15.91 | 552.22 | 0.13 | 2.31 | 1588 |
| 2024-09-20 22:21:33.429 | MS1 | 121.4656721885 | 31.1446275985 | 236 | 504990 | -88.87 | 14.02 | 400.08 | 0.16 | 2.20 | 1579 |
| 2024-09-20 22:21:34.482 | MS1 | 121.4656763814 | 31.1446225580 | 236 | 504990 | -91.68 | 12.70 | 81.99 | 0.06 | 2.66 | 395 |
| 2024-09-20 22:21:35.966 | MS1 | 121.4656779999 | 31.1446320056 | 236 | 504990 | -87.73 | 16.67 | 100.97 | 0.04 | 2.57 | 465 |
| 2024-09-20 22:21:36.795 | MS1 | 121.4656665543 | 31.1446350590 | 236 | 504990 | -87.96 | 15.57 | 90.47 | 0.12 | 2.35 | 370 |
| 2024-09-20 22:21:37.505 | MS1 | 121.4656688868 | 31.1446342394 | 236 | 504990 | -92.79 | 10.63 | 68.30 | 0.13 | 2.05 | 491 |
| 2024-09-20 22:21:38.763 | MS1 | 121.4656684689 | 31.1446379068 | 236 | 504990 | -89.97 | 7.38 | 60.13 | 0.19 | 2.40 | 318 |
| 2024-09-20 22:21:39.432 | MS1 | 121.4656614963 | 31.1446194298 | 236 | 504990 | -90.40 | 8.59 | 80.32 | 0.16 | 2.61 | 306 |
| 2024-09-20 22:21:40.829 | MS1 | 121.4656625455 | 31.1446333991 | 236 | 504990 | -89.72 | 12.64 | 343.86 | 0.04 | 2.26 | 1577 |
| 2024-09-20 22:21:41.555 | MS1 | 121.4656722558 | 31.1446345987 | 236 | 504990 | -91.47 | 7.25 | 503.72 | 0.15 | 2.98 | 1560 |
| 2024-09-20 22:21:42.282 | MS1 | 121.4656686439 | 31.1446327653 | 236 | 504990 | -90.61 | 7.47 | 419.76 | 0.07 | 2.94 | 1600 |

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
| 3214834 | 2 | 121.4714678838 | 31.1461507749 | 1 | 1 | 1 | 32.0 | TDD | 309 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3237084 | 4 | 121.4724326988 | 31.1523215913 | 346 | 4 | 7 | 35.5 | TDD | 236 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3248469 | 3 | 121.4692865409 | 31.1556441190 | 188 | 2 | 7 | 38.8 | TDD | 632 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3261432 | 1 | 121.4691016936 | 31.1530818814 | 13 | 9 | 2 | 44.8 | TDD | 232 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:31.122 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.144 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.250 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.250 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.022 | NREventA3 | measId:2;ServCellPCI:291;Se... |
| 2024-09-20 22:21:38.262 | NRHandoverAttempt | SourcePCI:291;SourceNR-ARFC... |
| 2024-09-20 22:21:38.309 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.323 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.440 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.440 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3261432 | 1 | 16.2464 | 9.6905 | -116.7176 | 6.7579 | 139.5569 | 0.0133 | 0.0115 |
| 2024_09_20 22:00 | 3214834 | 2 | 16.8617 | 18.4675 | -115.4783 | 17.4341 | 196.7970 | 0.0170 | 0.0152 |
| 2024_09_20 22:00 | 3248469 | 3 | 10.6491 | 16.1332 | -116.0979 | 12.4187 | 102.1400 | 0.0012 | 0.0167 |
| 2024_09_20 22:00 | 3237084 | 4 | 12.6917 | 10.9659 | -117.0769 | 15.3914 | 167.2242 | 0.0090 | 0.0112 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415504_50100D1C | 504990 | 236 | -91.3 | 504990 | 232 | -98.3 | 504990 | 309 | -100.9 | 504990 | 632 |
| MR_1774415504_A7BD9E6E | 504990 | 236 | -90.3 | 504990 | 232 | -97.3 | 504990 | 309 | -99.7 | 504990 | 632 |
| MR_1774415504_FDB0543F | 504990 | 236 | -91.5 | 504990 | 232 | -100.7 | 504990 | 309 | -100.5 | 504990 | 632 |
| MR_1774415504_43764115 | 504990 | 236 | -93.2 | 504990 | 232 | -100.3 | 504990 | 309 | -100.6 | 504990 | 632 |
| MR_1774415504_63B2D58E | 504990 | 236 | -92.0 | 504990 | 232 | -98.8 | 504990 | 309 | -98.9 | 504990 | 632 |
| MR_1774415504_AC1BD4B2 | 504990 | 236 | -90.9 | 504990 | 232 | -97.6 | 504990 | 309 | -100.5 | 504990 | 632 |
| MR_1774415504_0F8153A3 | 504990 | 236 | -92.2 | 504990 | 232 | -99.6 | 504990 | 309 | -99.0 | 504990 | 632 |
| MR_1774415504_ED965C58 | 504990 | 236 | -92.3 | 504990 | 232 | -98.2 | 504990 | 309 | -98.7 | 504990 | 632 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1445: `849df86a-125...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `849df86a-125b-451c-b095-6b48bc8ad3d1` |
| Tag | **single-answer** |
| 정답 | **C21** |
| C21 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1445] topology](images/train_1445.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3272002_2
- `C2`: Adjust the azimuth of 3272002_2 by 50 degrees
- `C3`: Decrease A3 Offset threshold for 3272002_2
- `C4`: Increase transmission power for 3272002_2
- `C5`: Lift the tilt angle  of 3248672_1 by 10 degrees
- `C6`: Increase transmission power for 3248672_1
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3248672_1
- `C8`: Add neighbor relationship between 3272002_2 and 3248672_1
- `C9`: Add neighbor relationship between 3263628_4 and 3248672_1
- `C10`: Decrease transmission power for 3248672_1
- `C11`: Increase A3 Offset threshold for 3248672_1
- `C12`: Press down the tilt angle of 3272002_2 by 10 degrees
- `C13`: Lift the tilt angle of 3272002_2 by 10 degrees
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3248672_1
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3272002_2
- `C17`: Adjust the azimuth of 3248672_1 by 50 degrees
- `C18`: Decrease transmission power for 3272002_2
- `C19`: Press down the tilt angle  of 3248672_1 by 10 degrees
- `C20`: Increase A3 Offset threshold for 3272002_2
- `C21`: Check test server and transmission issues **← 정답**
- `C22`: Decrease A3 Offset threshold for 3248672_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.199 | MS1 | 121.4656750569 | 31.1446268327 | 103 | 504990 | -88.93 | 15.28 | 385.98 | 0.10 | 2.40 | 1572 |
| 2024-09-20 22:21:32.382 | MS1 | 121.4656662265 | 31.1446255471 | 103 | 504990 | -85.77 | 13.09 | 313.94 | 0.19 | 2.67 | 1597 |
| 2024-09-20 22:21:33.443 | MS1 | 121.4656618990 | 31.1446318674 | 103 | 504990 | -91.72 | 15.02 | 443.77 | 0.20 | 2.89 | 1588 |
| 2024-09-20 22:21:34.749 | MS1 | 121.4656691777 | 31.1446278649 | 103 | 504990 | -91.76 | 12.69 | 87.42 | 0.09 | 2.90 | 421 |
| 2024-09-20 22:21:35.403 | MS1 | 121.4656770695 | 31.1446354411 | 103 | 504990 | -90.67 | 14.67 | 90.88 | 0.01 | 2.33 | 369 |
| 2024-09-20 22:21:36.712 | MS1 | 121.4656590942 | 31.1446184131 | 103 | 504990 | -89.81 | 12.62 | 54.27 | 0.12 | 2.98 | 413 |
| 2024-09-20 22:21:37.222 | MS1 | 121.4656582328 | 31.1446334705 | 103 | 504990 | -90.76 | 8.77 | 80.66 | 0.05 | 2.31 | 300 |
| 2024-09-20 22:21:38.364 | MS1 | 121.4656682146 | 31.1446347403 | 103 | 504990 | -89.76 | 7.71 | 92.61 | 0.04 | 2.11 | 436 |
| 2024-09-20 22:21:39.672 | MS1 | 121.4656751247 | 31.1446364385 | 103 | 504990 | -93.71 | 11.18 | 59.10 | 0.07 | 2.63 | 437 |
| 2024-09-20 22:21:40.310 | MS1 | 121.4656652540 | 31.1446300177 | 103 | 504990 | -93.57 | 12.48 | 291.00 | 0.07 | 2.90 | 1560 |
| 2024-09-20 22:21:41.957 | MS1 | 121.4656742838 | 31.1446303933 | 103 | 504990 | -89.44 | 7.72 | 417.00 | 0.11 | 2.38 | 1560 |
| 2024-09-20 22:21:42.666 | MS1 | 121.4656590532 | 31.1446192537 | 103 | 504990 | -93.92 | 8.02 | 415.93 | 0.06 | 2.04 | 1580 |

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
| 3224693 | 3 | 121.4704765000 | 31.1503155809 | 43 | 5 | 12 | 41.9 | TDD | 626 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3248672 | 1 | 121.4701472634 | 31.1508591679 | 318 | 13 | 7 | 31.3 | TDD | 162 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3263628 | 4 | 121.4696648208 | 31.1448399226 | 112 | 1 | 12 | 38.7 | TDD | 367 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3272002 | 2 | 121.4758744494 | 31.1445696630 | 147 | 15 | 11 | 37.5 | TDD | 103 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |

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
| 2024-09-20 22:21:31.066 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.085 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.204 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.204 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.882 | NREventA3 | measId:2;ServCellPCI:998;Se... |
| 2024-09-20 22:21:38.122 | NRHandoverAttempt | SourcePCI:998;SourceNR-ARFC... |
| 2024-09-20 22:21:38.167 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.180 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.286 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.286 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3248672 | 1 | 5.4320 | 18.9371 | -116.1445 | 6.0920 | 176.8629 | 0.0129 | 0.0119 |
| 2024_09_20 22:00 | 3272002 | 2 | 6.9125 | 6.2390 | -115.5617 | 10.3530 | 164.5749 | 0.0070 | 0.0102 |
| 2024_09_20 22:00 | 3224693 | 3 | 10.8197 | 18.6579 | -115.0178 | 14.0799 | 140.3776 | 0.0197 | 0.0033 |
| 2024_09_20 22:00 | 3263628 | 4 | 18.7526 | 16.4961 | -116.0061 | 6.6820 | 89.1210 | 0.0031 | 0.0095 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416765_7A8A7DBF | 504990 | 103 | -91.2 | 504990 | 162 | -95.2 | 504990 | 367 | -100.8 | 504990 | 626 |
| MR_1774416765_023BA21D | 504990 | 103 | -92.0 | 504990 | 162 | -97.6 | 504990 | 367 | -99.5 | 504990 | 626 |
| MR_1774416765_D12F792A | 504990 | 103 | -90.6 | 504990 | 162 | -95.0 | 504990 | 367 | -99.7 | 504990 | 626 |
| MR_1774416765_A4FE867B | 504990 | 103 | -92.6 | 504990 | 162 | -98.9 | 504990 | 367 | -100.4 | 504990 | 626 |
| MR_1774416765_AFABF962 | 504990 | 103 | -91.5 | 504990 | 162 | -96.9 | 504990 | 367 | -99.9 | 504990 | 626 |
| MR_1774416765_AF2AFAF5 | 504990 | 103 | -91.8 | 504990 | 162 | -96.0 | 504990 | 367 | -98.9 | 504990 | 626 |
| MR_1774416765_C0FE2645 | 504990 | 103 | -91.4 | 504990 | 162 | -96.7 | 504990 | 367 | -101.5 | 504990 | 626 |
| MR_1774416765_F3296692 | 504990 | 103 | -89.8 | 504990 | 162 | -98.8 | 504990 | 367 | -102.0 | 504990 | 626 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1446: `199ff4ff-b68...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `199ff4ff-b689-4f28-9bb8-1633cff6b54e` |
| Tag | **multiple-answer** |
| 정답 | **C17|C20** |
| C17 의미 | Adjust the azimuth of 3263850_4 by 49 degrees |
| C20 의미 | Increase transmission power for 3263850_4 |
| 패턴 분류 | **P4 Coverage (azimuth)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1446] topology](images/train_1446.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3263850_4
- `C2`: Decrease A3 Offset threshold for 3263850_4
- `C3`: Adjust the azimuth of 3278287_1 by 7 degrees
- `C4`: Add neighbor relationship between 3263850_4 and 3278287_1
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3278287_1
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3278287_1
- `C7`: Increase A3 Offset threshold for 3278287_1
- `C8`: Increase A3 Offset threshold for 3263850_4
- `C9`: Lift the tilt angle  of 3278287_1 by 5 degrees
- `C10`: Decrease transmission power for 3263850_4
- `C11`: Press down the tilt angle of 3263850_4 by 10 degrees
- `C12`: Check test server and transmission issues
- `C13`: Press down the tilt angle  of 3278287_1 by 5 degrees
- `C14`: Add neighbor relationship between 3233296_2 and 3278287_1
- `C15`: Insufficient data; more data is needed for judgment.
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3263850_4
- `C17`: Adjust the azimuth of 3263850_4 by 49 degrees **← 정답**
- `C18`: Lift the tilt angle of 3263850_4 by 10 degrees
- `C19`: Increase transmission power for 3278287_1
- `C20`: Increase transmission power for 3263850_4 **← 정답**
- `C21`: Decrease transmission power for 3278287_1
- `C22`: Decrease A3 Offset threshold for 3278287_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.992 | MS1 | 121.4656767922 | 31.1446275904 | 301 | 504990 | -91.75 | 14.64 | 376.52 | 0.17 | 2.96 | 1566 |
| 2024-09-20 22:21:32.119 | MS1 | 121.4656661784 | 31.1446282690 | 301 | 504990 | -89.38 | 15.45 | 538.93 | 0.10 | 2.65 | 1574 |
| 2024-09-20 22:21:33.368 | MS1 | 121.4656733535 | 31.1446330297 | 301 | 504990 | -93.43 | 12.20 | 481.63 | 0.16 | 2.69 | 1564 |
| 2024-09-20 22:21:34.448 | MS1 | 121.4656749528 | 31.1446289826 | 301 | 504990 | -105.05 | -1.11 | 46.99 | 0.16 | 1.02 | 1561 |
| 2024-09-20 22:21:35.918 | MS1 | 121.4656752741 | 31.1446244671 | 301 | 504990 | -109.88 | -1.36 | 80.46 | 0.04 | 1.17 | 1591 |
| 2024-09-20 22:21:36.974 | MS1 | 121.4656589260 | 31.1446277115 | 301 | 504990 | -107.93 | 1.30 | 51.95 | 0.04 | 1.41 | 1597 |
| 2024-09-20 22:21:37.628 | MS1 | 121.4656625616 | 31.1446341311 | 301 | 504990 | -100.92 | -0.78 | 45.16 | 0.01 | 1.04 | 1565 |
| 2024-09-20 22:21:38.933 | MS1 | 121.4656584974 | 31.1446329846 | 301 | 504990 | -109.78 | 0.80 | 72.33 | 0.01 | 1.46 | 1599 |
| 2024-09-20 22:21:39.617 | MS1 | 121.4656647824 | 31.1446257182 | 301 | 504990 | -108.96 | -0.69 | 69.51 | 0.01 | 1.45 | 1579 |
| 2024-09-20 22:21:40.341 | MS1 | 121.4656739592 | 31.1446191707 | 301 | 504990 | -90.73 | 17.93 | 387.85 | 0.19 | 2.07 | 1599 |
| 2024-09-20 22:21:41.737 | MS1 | 121.4656629201 | 31.1446346230 | 301 | 504990 | -90.22 | 13.31 | 444.90 | 0.00 | 2.69 | 1575 |
| 2024-09-20 22:21:42.145 | MS1 | 121.4656736369 | 31.1446371190 | 301 | 504990 | -87.79 | 16.89 | 301.86 | 0.13 | 2.99 | 1581 |

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
| 3233296 | 2 | 121.4690361649 | 31.1559807304 | 43 | 2 | 10 | 30.7 | TDD | 11 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3263850 | 4 | 121.4643455798 | 31.1443388296 | 26 | 5 | 5 | 43.1 | TDD | 301 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3266981 | 3 | 121.4754068287 | 31.1509274811 | 325 | 8 | 1 | 16.1 | TDD | 300 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3278287 | 1 | 121.4656800964 | 31.1486112212 | 173 | 1 | 6 | 29.7 | TDD | 82 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |

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
| 2024-09-20 22:21:31.151 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.166 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.299 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.299 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.487 | NREventA2 | measId:1;ServCellPCI:253;Se... |
| 2024-09-20 22:21:34.635 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3278287 | 1 | 10.9872 | 15.4552 | -117.2980 | 6.0017 | 189.5024 | 0.0086 | 0.0188 |
| 2024_09_20 22:00 | 3233296 | 2 | 10.0245 | 10.8045 | -115.4448 | 7.1659 | 139.1045 | 0.0185 | 0.0016 |
| 2024_09_20 22:00 | 3266981 | 3 | 12.2650 | 16.6684 | -115.6759 | 11.3105 | 140.0769 | 0.0033 | 0.0048 |
| 2024_09_20 22:00 | 3263850 | 4 | 12.5925 | 16.6868 | -114.0143 | 13.5951 | 128.9428 | 0.1816 | 0.0045 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415795_470B8959 | 504990 | 301 | -103.8 | 504990 | 82 | -108.0 | 504990 | 11 | -116.2 | 504990 | 300 |
| MR_1774415795_ACD43D7D | 504990 | 301 | -104.2 | 504990 | 82 | -107.8 | 504990 | 11 | -114.5 | 504990 | 300 |
| MR_1774415795_DB961200 | 504990 | 301 | -104.2 | 504990 | 82 | -107.5 | 504990 | 11 | -117.1 | 504990 | 300 |
| MR_1774415795_3A72722B | 504990 | 301 | -106.2 | 504990 | 82 | -106.7 | 504990 | 11 | -117.4 | 504990 | 300 |
| MR_1774415795_4F259EF4 | 504990 | 301 | -103.7 | 504990 | 82 | -107.2 | 504990 | 11 | -116.5 | 504990 | 300 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1447: `7e1f304e-bfc...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `7e1f304e-bfc3-4481-a9b9-b0fbd90d5238` |
| Tag | **single-answer** |
| 정답 | **C5** |
| C5 의미 | Lift the tilt angle  of 3278300_2 by 8 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1447] topology](images/train_1447.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3261407_4
- `C2`: Increase A3 Offset threshold for 3226844_1
- `C3`: Adjust the azimuth of 3261407_4 by 34 degrees
- `C4`: Add neighbor relationship between 3261407_4 and 3226844_1
- `C5`: Lift the tilt angle  of 3278300_2 by 8 degrees **← 정답**
- `C6`: Add neighbor relationship between 3278300_2 and 3226844_1
- `C7`: Adjust the azimuth of 3278300_2 by 50 degrees
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3261407_4
- `C9`: Decrease transmission power for 3226844_1
- `C10`: Decrease A3 Offset threshold for 3261407_4
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3261407_4
- `C12`: Check test server and transmission issues
- `C13`: Increase A3 Offset threshold for 3261407_4
- `C14`: Increase transmission power for 3226844_1
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3226844_1
- `C16`: Press down the tilt angle of 3261407_4 by 2 degrees
- `C17`: Decrease transmission power for 3261407_4
- `C18`: Decrease A3 Offset threshold for 3226844_1
- `C19`: Press down the tilt angle  of 3278300_2 by 8 degrees
- `C20`: Insufficient data; more data is needed for judgment.
- `C21`: Lift the tilt angle of 3261407_4 by 2 degrees
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3226844_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.607 | MS1 | 121.4656691197 | 31.1446230365 | 750 | 504990 | -90.16 | 16.41 | 448.36 | 0.08 | 2.26 | 1594 |
| 2024-09-20 22:21:32.722 | MS1 | 121.4656701768 | 31.1446375671 | 750 | 504990 | -91.03 | 16.10 | 369.37 | 0.16 | 2.15 | 1582 |
| 2024-09-20 22:21:33.367 | MS1 | 121.4656583276 | 31.1446365647 | 750 | 504990 | -86.99 | 17.97 | 334.18 | 0.10 | 2.15 | 1593 |
| 2024-09-20 22:21:34.432 | MS1 | 121.4656673914 | 31.1446187813 | 750 | 504990 | -85.85 | 14.26 | 46.12 | 0.18 | 2.58 | 1599 |
| 2024-09-20 22:21:35.452 | MS1 | 121.4656651970 | 31.1446343217 | 750 | 504990 | -88.91 | 17.56 | 69.23 | 0.01 | 2.43 | 1566 |
| 2024-09-20 22:21:36.411 | MS1 | 121.4656761949 | 31.1446232979 | 750 | 504990 | -87.75 | 14.78 | 65.17 | 0.11 | 2.08 | 1585 |
| 2024-09-20 22:21:37.853 | MS1 | 121.4656629520 | 31.1446331183 | 750 | 504990 | -93.46 | 11.52 | 96.26 | 0.12 | 2.74 | 1569 |
| 2024-09-20 22:21:38.936 | MS1 | 121.4656671964 | 31.1446315459 | 750 | 504990 | -90.34 | 12.65 | 66.20 | 0.14 | 2.92 | 1596 |
| 2024-09-20 22:21:39.217 | MS1 | 121.4656588654 | 31.1446262973 | 750 | 504990 | -89.25 | 8.76 | 106.34 | 0.09 | 2.47 | 1597 |
| 2024-09-20 22:21:40.627 | MS1 | 121.4656684325 | 31.1446267013 | 750 | 504990 | -92.57 | 9.53 | 488.32 | 0.15 | 2.61 | 1578 |
| 2024-09-20 22:21:41.557 | MS1 | 121.4656677190 | 31.1446291971 | 750 | 504990 | -92.89 | 7.29 | 486.18 | 0.03 | 2.25 | 1586 |
| 2024-09-20 22:21:42.359 | MS1 | 121.4656612248 | 31.1446280541 | 750 | 504990 | -91.57 | 11.53 | 349.49 | 0.01 | 2.24 | 1565 |

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
| 3226844 | 1 | 121.4706592914 | 31.1548377137 | 39 | 7 | 2 | 21.7 | TDD | 40 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3261407 | 4 | 121.4729875970 | 31.1496537136 | 265 | 1 | 4 | 16.3 | TDD | 750 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3276112 | 3 | 121.4745742647 | 31.1524309923 | 94 | 5 | 8 | 15.5 | TDD | 565 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3278300 | 2 | 121.4680721437 | 31.1446772908 | 61 | 2 | 1 | 25.4 | TDD | 810 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:31.157 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.181 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.309 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.309 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.057 | NREventA3 | measId:2;ServCellPCI:915;Se... |
| 2024-09-20 22:21:38.297 | NRHandoverAttempt | SourcePCI:915;SourceNR-ARFC... |
| 2024-09-20 22:21:38.328 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.342 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.442 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.442 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3226844 | 1 | 14.4682 | 12.8900 | -116.5284 | 5.4809 | 156.0805 | 0.0011 | 0.0063 |
| 2024_09_20 22:00 | 3278300 | 2 | 14.2229 | 7.9539 | -116.4844 | 14.1754 | 134.0902 | 0.0150 | 0.0186 |
| 2024_09_20 22:00 | 3276112 | 3 | 13.5064 | 16.8290 | -116.7353 | 6.8981 | 108.8071 | 0.0021 | 0.0099 |
| 2024_09_20 22:00 | 3261407 | 4 | 77.3030 | 92.1594 | -115.6213 | 19.8291 | 133.2446 | 0.0180 | 0.0058 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413028_EEF7C02B | 504990 | 750 | -85.9 | 504990 | 40 | -93.7 | 504990 | 810 | -94.5 | 504990 | 565 |
| MR_1774413028_F28E74FD | 504990 | 750 | -85.2 | 504990 | 40 | -96.3 | 504990 | 810 | -97.1 | 504990 | 565 |
| MR_1774413028_4C9AC059 | 504990 | 750 | -84.4 | 504990 | 40 | -93.1 | 504990 | 810 | -95.3 | 504990 | 565 |
| MR_1774413028_BDF5F07B | 504990 | 750 | -84.9 | 504990 | 40 | -96.5 | 504990 | 810 | -94.3 | 504990 | 565 |
| MR_1774413028_798171A2 | 504990 | 750 | -86.7 | 504990 | 40 | -93.1 | 504990 | 810 | -94.5 | 504990 | 565 |
| MR_1774413028_65D449B2 | 504990 | 750 | -85.4 | 504990 | 40 | -94.6 | 504990 | 810 | -95.0 | 504990 | 565 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1448: `d2a0100a-aa8...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `d2a0100a-aa8c-4463-9883-a70e9f1ea611` |
| Tag | **single-answer** |
| 정답 | **C21** |
| C21 의미 | Add neighbor relationship between 3243682_4 and 3223609_2 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1448] topology](images/train_1448.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle  of 3223609_2 by 3 degrees
- `C2`: Press down the tilt angle of 3243682_4 by 10 degrees
- `C3`: Lift the tilt angle of 3243682_4 by 10 degrees
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3223609_2
- `C5`: Decrease transmission power for 3243682_4
- `C6`: Press down the tilt angle  of 3223609_2 by 3 degrees
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3223609_2
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3243682_4
- `C9`: Add neighbor relationship between 3245674_1 and 3223609_2
- `C10`: Adjust the azimuth of 3243682_4 by 7 degrees
- `C11`: Increase transmission power for 3223609_2
- `C12`: Insufficient data; more data is needed for judgment.
- `C13`: Decrease A3 Offset threshold for 3223609_2
- `C14`: Check test server and transmission issues
- `C15`: Decrease A3 Offset threshold for 3243682_4
- `C16`: Decrease transmission power for 3223609_2
- `C17`: Increase A3 Offset threshold for 3223609_2
- `C18`: Increase transmission power for 3243682_4
- `C19`: Increase A3 Offset threshold for 3243682_4
- `C20`: Adjust the azimuth of 3223609_2 by 0 degrees
- `C21`: Add neighbor relationship between 3243682_4 and 3223609_2 **← 정답**
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3243682_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.912 | MS1 | 121.4656741090 | 31.1446354282 | 342 | 504990 | -78.07 | 13.65 | 461.79 | 0.14 | 2.54 | 1560 |
| 2024-09-20 22:21:32.768 | MS1 | 121.4656668661 | 31.1446259212 | 342 | 504990 | -82.90 | 13.08 | 426.16 | 0.06 | 2.03 | 1590 |
| 2024-09-20 22:21:33.604 | MS1 | 121.4656695567 | 31.1446188382 | 342 | 504990 | -79.17 | 12.81 | 539.66 | 0.05 | 2.03 | 1585 |
| 2024-09-20 22:21:34.139 | MS1 | 121.4656724811 | 31.1446354838 | 342 | 504990 | -88.49 | -1.22 | 56.43 | 0.18 | 1.45 | 1593 |
| 2024-09-20 22:21:35.202 | MS1 | 121.4656707328 | 31.1446237915 | 342 | 504990 | -90.15 | -2.39 | 34.07 | 0.10 | 1.33 | 1586 |
| 2024-09-20 22:21:36.302 | MS1 | 121.4656585381 | 31.1446256165 | 342 | 504990 | -88.79 | -2.43 | 48.06 | 0.09 | 1.47 | 1569 |
| 2024-09-20 22:21:37.766 | MS1 | 121.4656586561 | 31.1446203985 | 342 | 504990 | -92.17 | -1.33 | 46.97 | 0.08 | 1.40 | 1589 |
| 2024-09-20 22:21:38.372 | MS1 | 121.4656680575 | 31.1446309762 | 342 | 504990 | -75.04 | 13.67 | 345.96 | 0.13 | 1.45 | 1599 |
| 2024-09-20 22:21:39.960 | MS1 | 121.4656770551 | 31.1446292244 | 342 | 504990 | -84.52 | 13.47 | 568.85 | 0.01 | 1.36 | 1563 |
| 2024-09-20 22:21:40.577 | MS1 | 121.4656635068 | 31.1446350617 | 342 | 504990 | -80.62 | 16.91 | 358.89 | 0.16 | 2.29 | 1576 |
| 2024-09-20 22:21:41.293 | MS1 | 121.4656658646 | 31.1446196688 | 342 | 504990 | -79.45 | 16.70 | 476.94 | 0.02 | 2.54 | 1580 |
| 2024-09-20 22:21:42.354 | MS1 | 121.4656735978 | 31.1446342300 | 342 | 504990 | -78.38 | 15.74 | 334.76 | 0.00 | 2.87 | 1560 |

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
| 3223609 | 2 | 121.4685576921 | 31.1532338501 | 196 | 1 | 9 | 34.3 | TDD | 194 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3243682 | 4 | 121.4747708106 | 31.1550029964 | 210 | 15 | 3 | 47.8 | TDD | 342 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3245674 | 1 | 121.4742559945 | 31.1535650432 | 317 | 1 | 10 | 23.3 | TDD | 281 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3250803 | 3 | 121.4719475449 | 31.1503670626 | 238 | 3 | 4 | 20.9 | TDD | 514 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:31.063 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.087 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.199 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.199 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.937 | NREventA3 | measId:2;ServCellPCI:295;Se... |
| 2024-09-20 22:21:35.937 | NREventA3 | measId:2;ServCellPCI:295;Se... |
| 2024-09-20 22:21:36.937 | NREventA3 | measId:2;ServCellPCI:295;Se... |
| 2024-09-20 22:21:39.437 | NRRRCReestablishAttempt | PCI:295 |
| 2024-09-20 22:21:39.451 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.463 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:39.591 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.591 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3245674 | 1 | 10.3483 | 12.1395 | -116.7950 | 11.0973 | 145.5174 | 0.0193 | 0.0162 |
| 2024_09_20 22:00 | 3223609 | 2 | 6.7672 | 11.1836 | -117.5979 | 14.9352 | 154.1612 | 0.0109 | 0.0129 |
| 2024_09_20 22:00 | 3250803 | 3 | 16.1211 | 7.1276 | -115.8632 | 14.1076 | 159.4378 | 0.0138 | 0.0117 |
| 2024_09_20 22:00 | 3243682 | 4 | 9.0707 | 5.8958 | -116.0891 | 11.7387 | 157.2164 | 0.0140 | 0.1814 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417037_E17A2D0A | 504990 | 194 | -84.8 | 504990 | 342 | -87.4 | 504990 | 281 | -83.1 | 504990 | 514 |
| MR_1774417037_87B1FB33 | 504990 | 342 | -86.7 | 504990 | 194 | -81.2 | 504990 | 281 | -85.5 | 504990 | 514 |
| MR_1774417037_084692D0 | 504990 | 342 | -89.8 | 504990 | 194 | -82.8 | 504990 | 281 | -85.5 | 504990 | 514 |
| MR_1774417037_DF3EBB73 | 504990 | 194 | -83.2 | 504990 | 342 | -88.6 | 504990 | 281 | -84.8 | 504990 | 514 |
| MR_1774417037_77799DFE | 504990 | 342 | -90.4 | 504990 | 194 | -83.7 | 504990 | 281 | -86.2 | 504990 | 514 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1449: `23355532-893...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `23355532-893c-4ca7-9666-d75e5d7900b9` |
| Tag | **single-answer** |
| 정답 | **C15** |
| C15 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3269066_3 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1449] topology](images/train_1449.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3273425_1
- `C2`: Increase A3 Offset threshold for 3269066_3
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3273425_1
- `C4`: Decrease A3 Offset threshold for 3273425_1
- `C5`: Lift the tilt angle of 3269066_3 by 4 degrees
- `C6`: Add neighbor relationship between 3234242_4 and 3273425_1
- `C7`: Decrease transmission power for 3269066_3
- `C8`: Press down the tilt angle  of 3273425_1 by 7 degrees
- `C9`: Decrease A3 Offset threshold for 3269066_3
- `C10`: Adjust the azimuth of 3269066_3 by 46 degrees
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3273425_1
- `C12`: Decrease transmission power for 3273425_1
- `C13`: Adjust the azimuth of 3273425_1 by 50 degrees
- `C14`: Increase transmission power for 3269066_3
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3269066_3 **← 정답**
- `C16`: Lift the tilt angle  of 3273425_1 by 7 degrees
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3269066_3
- `C18`: Check test server and transmission issues
- `C19`: Insufficient data; more data is needed for judgment.
- `C20`: Increase A3 Offset threshold for 3273425_1
- `C21`: Add neighbor relationship between 3269066_3 and 3273425_1
- `C22`: Press down the tilt angle of 3269066_3 by 4 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.205 | MS1 | 121.4656670981 | 31.1446359923 | 925 | 504990 | -90.01 | 16.36 | 562.82 | 0.16 | 2.51 | 1565 |
| 2024-09-20 22:21:32.143 | MS1 | 121.4656652413 | 31.1446183424 | 925 | 504990 | -87.61 | 12.75 | 479.33 | 0.18 | 2.97 | 1591 |
| 2024-09-20 22:21:33.609 | MS1 | 121.4656718775 | 31.1446247354 | 925 | 504990 | -87.66 | 16.44 | 568.91 | 0.04 | 2.24 | 1575 |
| 2024-09-20 22:21:34.634 | MS1 | 121.4656693043 | 31.1446350700 | 925 | 504990 | -89.92 | 12.58 | 51.29 | 0.67 | 2.95 | 583 |
| 2024-09-20 22:21:35.475 | MS1 | 121.4656626048 | 31.1446257081 | 925 | 504990 | -90.29 | 12.24 | 81.53 | 0.53 | 2.12 | 535 |
| 2024-09-20 22:21:36.508 | MS1 | 121.4656646507 | 31.1446243650 | 925 | 504990 | -91.78 | 17.89 | 60.09 | 0.65 | 2.18 | 645 |
| 2024-09-20 22:21:37.787 | MS1 | 121.4656645111 | 31.1446185413 | 925 | 504990 | -91.18 | 8.00 | 93.62 | 0.54 | 2.73 | 534 |
| 2024-09-20 22:21:38.183 | MS1 | 121.4656715770 | 31.1446300169 | 925 | 504990 | -92.17 | 9.47 | 91.02 | 0.57 | 2.30 | 632 |
| 2024-09-20 22:21:39.746 | MS1 | 121.4656713482 | 31.1446180194 | 925 | 504990 | -93.37 | 11.76 | 49.84 | 0.63 | 2.87 | 642 |
| 2024-09-20 22:21:40.381 | MS1 | 121.4656677729 | 31.1446220658 | 925 | 504990 | -90.29 | 11.25 | 512.36 | 0.03 | 2.63 | 1586 |
| 2024-09-20 22:21:41.610 | MS1 | 121.4656761939 | 31.1446323358 | 925 | 504990 | -93.20 | 7.16 | 357.19 | 0.04 | 2.75 | 1566 |
| 2024-09-20 22:21:42.762 | MS1 | 121.4656619095 | 31.1446357047 | 925 | 504990 | -91.20 | 9.58 | 338.52 | 0.19 | 2.85 | 1573 |

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
| 3234242 | 4 | 121.4666708922 | 31.1541498775 | 192 | 6 | 8 | 16.8 | TDD | 263 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3268710 | 2 | 121.4689723889 | 31.1456001791 | 18 | 9 | 11 | 32.3 | TDD | 189 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3269066 | 3 | 121.4658791765 | 31.1527567409 | 135 | 1 | 6 | 47.3 | TDD | 925 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3273425 | 1 | 121.4721214957 | 31.1456780042 | 354 | 4 | 1 | 31.1 | TDD | 299 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |

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
| 2024-09-20 22:21:31.481 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.499 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.605 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.605 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.323 | NREventA3 | measId:2;ServCellPCI:913;Se... |
| 2024-09-20 22:21:38.563 | NRHandoverAttempt | SourcePCI:913;SourceNR-ARFC... |
| 2024-09-20 22:21:38.596 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.610 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.710 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.710 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3273425 | 1 | 9.1668 | 18.0622 | -117.9631 | 6.1883 | 195.7797 | 0.0016 | 0.0149 |
| 2024_09_20 22:00 | 3268710 | 2 | 13.0482 | 16.8149 | -116.8979 | 16.8185 | 145.6874 | 0.0160 | 0.0022 |
| 2024_09_20 22:00 | 3269066 | 3 | 8.4669 | 12.7265 | -117.5659 | 19.1249 | 86.7706 | 0.0134 | 0.0095 |
| 2024_09_20 22:00 | 3234242 | 4 | 13.7695 | 11.2100 | -116.2059 | 17.4334 | 171.2186 | 0.0039 | 0.0118 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413845_4657A65A | 504990 | 925 | -88.5 | 504990 | 299 | -92.8 | 504990 | 263 | -101.3 | 504990 | 189 |
| MR_1774413845_BEDA4F0F | 504990 | 925 | -91.7 | 504990 | 299 | -94.0 | 504990 | 263 | -101.6 | 504990 | 189 |
| MR_1774413845_0FDBCFC0 | 504990 | 925 | -90.2 | 504990 | 299 | -91.8 | 504990 | 263 | -102.5 | 504990 | 189 |
| MR_1774413845_2E0ADA86 | 504990 | 925 | -91.5 | 504990 | 299 | -91.5 | 504990 | 263 | -103.5 | 504990 | 189 |
| MR_1774413845_617DFD83 | 504990 | 925 | -88.3 | 504990 | 299 | -92.4 | 504990 | 263 | -103.8 | 504990 | 189 |

> *... 2개 열 생략 (전체 14열)*

---
