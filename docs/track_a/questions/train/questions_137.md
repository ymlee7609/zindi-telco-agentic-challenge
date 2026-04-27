# Track A 문제 분석 — train[1360]~train[1369]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[1360] ~ train[1369] (10개)

## 목차

1. [문제 1360: `ef56aaad-7b6...`](#1360) — single-answer, 정답: C17
2. [문제 1361: `df8d3f01-fd4...`](#1361) — single-answer, 정답: C13
3. [문제 1362: `4cd0d56f-d1f...`](#1362) — single-answer, 정답: C1
4. [문제 1363: `63b2c7a8-b46...`](#1363) — multiple-answer, 정답: C8|C17
5. [문제 1364: `c8f15ca6-994...`](#1364) — single-answer, 정답: C3
6. [문제 1365: `811e2a5f-737...`](#1365) — single-answer, 정답: C16
7. [문제 1366: `a59fe79b-678...`](#1366) — single-answer, 정답: C7
8. [문제 1367: `b45b36e7-862...`](#1367) — single-answer, 정답: C22
9. [문제 1368: `b4ad2782-7b8...`](#1368) — single-answer, 정답: C2
10. [문제 1369: `859f89ba-ca4...`](#1369) — single-answer, 정답: C11

---

### 문제 1360: `ef56aaad-7b6...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `ef56aaad-7b65-496a-ad04-fb1af650fc04` |
| Tag | **single-answer** |
| 정답 | **C17** |
| C17 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1360] topology](images/train_1360.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3267503_3 and 3252118_2
- `C2`: Decrease A3 Offset threshold for 3252118_2
- `C3`: Increase A3 Offset threshold for 3252118_2
- `C4`: Decrease A3 Offset threshold for 3267503_3
- `C5`: Increase transmission power for 3267503_3
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3267503_3
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3267503_3
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3252118_2
- `C9`: Increase transmission power for 3252118_2
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3252118_2
- `C11`: Adjust the azimuth of 3252118_2 by 50 degrees
- `C12`: Increase A3 Offset threshold for 3267503_3
- `C13`: Press down the tilt angle  of 3252118_2 by 3 degrees
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Lift the tilt angle of 3267503_3 by 5 degrees
- `C16`: Lift the tilt angle  of 3252118_2 by 3 degrees
- `C17`: Check test server and transmission issues **← 정답**
- `C18`: Adjust the azimuth of 3267503_3 by 50 degrees
- `C19`: Decrease transmission power for 3252118_2
- `C20`: Decrease transmission power for 3267503_3
- `C21`: Press down the tilt angle of 3267503_3 by 5 degrees
- `C22`: Add neighbor relationship between 3267333_1 and 3252118_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.675 | MS1 | 121.4656773425 | 31.1446202472 | 546 | 504990 | -88.93 | 14.48 | 419.40 | 0.16 | 2.15 | 1592 |
| 2024-09-20 22:21:32.465 | MS1 | 121.4656659248 | 31.1446249170 | 546 | 504990 | -89.37 | 14.16 | 319.01 | 0.19 | 2.96 | 1575 |
| 2024-09-20 22:21:33.948 | MS1 | 121.4656676608 | 31.1446245174 | 546 | 504990 | -86.08 | 15.79 | 415.44 | 0.15 | 2.82 | 1584 |
| 2024-09-20 22:21:34.106 | MS1 | 121.4656636211 | 31.1446297856 | 546 | 504990 | -86.04 | 17.79 | 49.51 | 0.02 | 2.58 | 470 |
| 2024-09-20 22:21:35.649 | MS1 | 121.4656620086 | 31.1446190131 | 546 | 504990 | -89.72 | 12.10 | 84.96 | 0.17 | 2.71 | 458 |
| 2024-09-20 22:21:36.834 | MS1 | 121.4656639455 | 31.1446368099 | 546 | 504990 | -87.90 | 16.57 | 50.81 | 0.07 | 2.01 | 461 |
| 2024-09-20 22:21:37.946 | MS1 | 121.4656753083 | 31.1446364402 | 546 | 504990 | -90.88 | 9.94 | 78.21 | 0.03 | 2.69 | 377 |
| 2024-09-20 22:21:38.961 | MS1 | 121.4656728893 | 31.1446249178 | 546 | 504990 | -92.57 | 11.08 | 83.41 | 0.15 | 2.10 | 324 |
| 2024-09-20 22:21:39.623 | MS1 | 121.4656692044 | 31.1446273864 | 546 | 504990 | -92.43 | 9.59 | 75.71 | 0.07 | 2.89 | 346 |
| 2024-09-20 22:21:40.255 | MS1 | 121.4656688821 | 31.1446272847 | 546 | 504990 | -89.50 | 9.37 | 396.14 | 0.09 | 2.10 | 1591 |
| 2024-09-20 22:21:41.984 | MS1 | 121.4656586281 | 31.1446237254 | 546 | 504990 | -92.94 | 11.74 | 507.15 | 0.15 | 2.86 | 1567 |
| 2024-09-20 22:21:42.583 | MS1 | 121.4656631607 | 31.1446291412 | 546 | 504990 | -91.50 | 10.47 | 365.66 | 0.17 | 2.68 | 1582 |

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
| 3250008 | 4 | 121.4756867799 | 31.1533919413 | 138 | 2 | 4 | 42.9 | TDD | 854 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3252118 | 2 | 121.4750219877 | 31.1538756288 | 111 | 1 | 6 | 48.0 | TDD | 930 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3267333 | 1 | 121.4682932440 | 31.1525720464 | 65 | 15 | 5 | 39.7 | TDD | 608 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3267503 | 3 | 121.4728952585 | 31.1447284193 | 216 | 3 | 7 | 21.4 | TDD | 546 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:31.099 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.123 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.229 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.229 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.926 | NREventA3 | measId:2;ServCellPCI:384;Se... |
| 2024-09-20 22:21:38.166 | NRHandoverAttempt | SourcePCI:384;SourceNR-ARFC... |
| 2024-09-20 22:21:38.211 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.221 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.332 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.332 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3267333 | 1 | 16.7923 | 16.1104 | -117.1004 | 8.2012 | 166.6491 | 0.0017 | 0.0174 |
| 2024_09_20 22:00 | 3252118 | 2 | 12.2488 | 10.9040 | -114.7124 | 7.9165 | 150.9875 | 0.0193 | 0.0036 |
| 2024_09_20 22:00 | 3267503 | 3 | 5.2275 | 13.8221 | -115.1072 | 17.6941 | 94.0752 | 0.0145 | 0.0094 |
| 2024_09_20 22:00 | 3250008 | 4 | 11.3979 | 11.7625 | -114.2298 | 19.2998 | 173.0282 | 0.0191 | 0.0175 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415779_B08C162E | 504990 | 546 | -84.1 | 504990 | 930 | -92.0 | 504990 | 608 | -96.3 | 504990 | 854 |
| MR_1774415779_9730C8C8 | 504990 | 546 | -84.8 | 504990 | 930 | -93.3 | 504990 | 608 | -94.2 | 504990 | 854 |
| MR_1774415779_1CF077C9 | 504990 | 546 | -86.5 | 504990 | 930 | -95.2 | 504990 | 608 | -93.1 | 504990 | 854 |
| MR_1774415779_9357752A | 504990 | 546 | -85.9 | 504990 | 930 | -93.2 | 504990 | 608 | -94.6 | 504990 | 854 |
| MR_1774415779_92A60491 | 504990 | 546 | -85.7 | 504990 | 930 | -93.9 | 504990 | 608 | -94.4 | 504990 | 854 |
| MR_1774415779_3C0AF882 | 504990 | 546 | -84.1 | 504990 | 930 | -92.5 | 504990 | 608 | -93.9 | 504990 | 854 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1361: `df8d3f01-fd4...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `df8d3f01-fd45-4d8b-b5fa-fdebddbbc9f7` |
| Tag | **single-answer** |
| 정답 | **C13** |
| C13 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1361] topology](images/train_1361.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3230029_2
- `C2`: Increase A3 Offset threshold for 3230029_2
- `C3`: Press down the tilt angle of 3245151_1 by 10 degrees
- `C4`: Lift the tilt angle of 3245151_1 by 10 degrees
- `C5`: Increase transmission power for 3230029_2
- `C6`: Check test server and transmission issues
- `C7`: Add neighbor relationship between 3227153_3 and 3230029_2
- `C8`: Increase transmission power for 3245151_1
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3230029_2
- `C10`: Decrease transmission power for 3230029_2
- `C11`: Adjust the azimuth of 3230029_2 by 50 degrees
- `C12`: Press down the tilt angle  of 3230029_2 by 8 degrees
- `C13`: Insufficient data; more data is needed for judgment. **← 정답**
- `C14`: Adjust the azimuth of 3245151_1 by 50 degrees
- `C15`: Lift the tilt angle  of 3230029_2 by 8 degrees
- `C16`: Add neighbor relationship between 3245151_1 and 3230029_2
- `C17`: Decrease A3 Offset threshold for 3245151_1
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3245151_1
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3230029_2
- `C20`: Decrease transmission power for 3245151_1
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3245151_1
- `C22`: Increase A3 Offset threshold for 3245151_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.275 | MS1 | 121.4656580941 | 31.1446304704 | 20 | 504990 | -87.00 | 12.72 | 448.95 | 0.17 | 2.53 | 1581 |
| 2024-09-20 22:21:32.189 | MS1 | 121.4656694763 | 31.1446180272 | 20 | 504990 | -86.18 | 16.92 | 594.76 | 0.17 | 2.71 | 1578 |
| 2024-09-20 22:21:33.421 | MS1 | 121.4656682462 | 31.1446187552 | 20 | 504990 | -91.43 | 15.30 | 342.70 | 0.17 | 2.99 | 1581 |
| 2024-09-20 22:21:34.860 | MS1 | 121.4656651393 | 31.1446320969 | 20 | 504990 | -88.04 | 12.26 | 62.30 | 0.08 | 2.69 | 1576 |
| 2024-09-20 22:21:35.734 | MS1 | 121.4656586616 | 31.1446181634 | 20 | 504990 | -87.35 | 12.24 | 74.05 | 0.13 | 2.21 | 1576 |
| 2024-09-20 22:21:36.213 | MS1 | 121.4656663359 | 31.1446350305 | 20 | 504990 | -90.47 | 13.37 | 60.12 | 0.11 | 2.18 | 1585 |
| 2024-09-20 22:21:37.862 | MS1 | 121.4656660722 | 31.1446301934 | 20 | 504990 | -89.27 | 8.19 | 73.08 | 0.17 | 2.67 | 1565 |
| 2024-09-20 22:21:38.659 | MS1 | 121.4656656247 | 31.1446266439 | 20 | 504990 | -91.37 | 12.59 | 84.59 | 0.06 | 2.88 | 1560 |
| 2024-09-20 22:21:39.643 | MS1 | 121.4656687324 | 31.1446372256 | 20 | 504990 | -92.25 | 8.77 | 83.55 | 0.06 | 2.87 | 1560 |
| 2024-09-20 22:21:40.638 | MS1 | 121.4656645221 | 31.1446274097 | 20 | 504990 | -89.60 | 10.65 | 461.32 | 0.03 | 2.36 | 1560 |
| 2024-09-20 22:21:41.408 | MS1 | 121.4656701086 | 31.1446377754 | 20 | 504990 | -89.50 | 8.16 | 291.28 | 0.03 | 2.18 | 1564 |
| 2024-09-20 22:21:42.663 | MS1 | 121.4656740177 | 31.1446366261 | 20 | 504990 | -89.50 | 8.22 | 534.87 | 0.10 | 2.93 | 1589 |

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
| 3227153 | 3 | 121.4690166762 | 31.1557674446 | 86 | 0 | 0 | 29.2 | TDD | 550 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3230029 | 2 | 121.4718295230 | 31.1498606452 | 345 | 5 | 2 | 43.6 | TDD | 237 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3245151 | 1 | 121.4679164134 | 31.1482338037 | 148 | 12 | 11 | 46.5 | TDD | 20 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3259559 | 4 | 121.4670016080 | 31.1479658899 | 322 | 1 | 6 | 47.2 | TDD | 941 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |

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
| 2024-09-20 22:21:31.570 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.585 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.710 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.710 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.406 | NREventA3 | measId:2;ServCellPCI:633;Se... |
| 2024-09-20 22:21:38.646 | NRHandoverAttempt | SourcePCI:633;SourceNR-ARFC... |
| 2024-09-20 22:21:38.680 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.691 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.811 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.811 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3245151 | 1 | 82.3910 | 82.7954 | -116.9699 | 10.0508 | 177.3719 | 0.0046 | 0.0082 |
| 2024_09_19 22:00 | 3230029 | 2 | 80.8474 | 87.7781 | -114.5604 | 16.2867 | 142.9388 | 0.0189 | 0.0084 |
| 2024_09_19 22:00 | 3227153 | 3 | 87.0226 | 75.4126 | -116.6158 | 17.0932 | 180.7606 | 0.0135 | 0.0189 |
| 2024_09_19 22:00 | 3259559 | 4 | 78.8659 | 85.0771 | -117.0228 | 19.7980 | 133.5354 | 0.0149 | 0.0116 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415131_33D921C8 | 504990 | 20 | -86.4 | 504990 | 237 | -87.6 | 504990 | 550 | -99.2 | 504990 | 941 |
| MR_1774415131_918B5FCD | 504990 | 20 | -90.0 | 504990 | 237 | -87.2 | 504990 | 550 | -98.7 | 504990 | 941 |
| MR_1774415131_49E57E5A | 504990 | 20 | -88.7 | 504990 | 237 | -89.6 | 504990 | 550 | -99.5 | 504990 | 941 |
| MR_1774415131_58036BB8 | 504990 | 20 | -88.0 | 504990 | 237 | -88.5 | 504990 | 550 | -96.6 | 504990 | 941 |
| MR_1774415131_AA56F5F0 | 504990 | 20 | -87.9 | 504990 | 237 | -86.9 | 504990 | 550 | -97.7 | 504990 | 941 |
| MR_1774415131_D8AA507D | 504990 | 20 | -86.4 | 504990 | 237 | -87.2 | 504990 | 550 | -98.8 | 504990 | 941 |
| MR_1774415131_8C327D48 | 504990 | 20 | -86.1 | 504990 | 237 | -87.1 | 504990 | 550 | -99.6 | 504990 | 941 |
| MR_1774415131_F09DB777 | 504990 | 20 | -89.2 | 504990 | 237 | -90.1 | 504990 | 550 | -96.4 | 504990 | 941 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1362: `4cd0d56f-d1f...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `4cd0d56f-d1f0-4f43-96ec-32f699b5a958` |
| Tag | **single-answer** |
| 정답 | **C1** |
| C1 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3261045_4 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1362] topology](images/train_1362.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3261045_4 **← 정답**
- `C2`: Add neighbor relationship between 3261045_4 and 3238934_2
- `C3`: Adjust the azimuth of 3238934_2 by 50 degrees
- `C4`: Decrease A3 Offset threshold for 3238934_2
- `C5`: Increase A3 Offset threshold for 3238934_2
- `C6`: Insufficient data; more data is needed for judgment.
- `C7`: Decrease transmission power for 3238934_2
- `C8`: Decrease A3 Offset threshold for 3261045_4
- `C9`: Lift the tilt angle  of 3238934_2 by 10 degrees
- `C10`: Increase A3 Offset threshold for 3261045_4
- `C11`: Check test server and transmission issues
- `C12`: Increase transmission power for 3261045_4
- `C13`: Decrease transmission power for 3261045_4
- `C14`: Increase transmission power for 3238934_2
- `C15`: Press down the tilt angle  of 3238934_2 by 10 degrees
- `C16`: Lift the tilt angle of 3261045_4 by 4 degrees
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3261045_4
- `C18`: Adjust the azimuth of 3261045_4 by 21 degrees
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3238934_2
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3238934_2
- `C21`: Press down the tilt angle of 3261045_4 by 4 degrees
- `C22`: Add neighbor relationship between 3240762_1 and 3238934_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.579 | MS1 | 121.4656705225 | 31.1446372093 | 990 | 504990 | -85.51 | 15.27 | 556.45 | 0.10 | 2.03 | 1590 |
| 2024-09-20 22:21:32.338 | MS1 | 121.4656711445 | 31.1446204271 | 990 | 504990 | -86.89 | 13.23 | 441.72 | 0.11 | 2.64 | 1572 |
| 2024-09-20 22:21:33.941 | MS1 | 121.4656741133 | 31.1446191291 | 990 | 504990 | -87.30 | 14.79 | 379.26 | 0.19 | 2.51 | 1582 |
| 2024-09-20 22:21:34.553 | MS1 | 121.4656668536 | 31.1446356711 | 990 | 504990 | -87.94 | 16.07 | 78.14 | 0.58 | 2.31 | 608 |
| 2024-09-20 22:21:35.779 | MS1 | 121.4656725492 | 31.1446231225 | 990 | 504990 | -90.89 | 14.56 | 100.53 | 0.60 | 2.43 | 555 |
| 2024-09-20 22:21:36.687 | MS1 | 121.4656633311 | 31.1446225065 | 990 | 504990 | -87.47 | 12.18 | 54.71 | 0.64 | 2.61 | 674 |
| 2024-09-20 22:21:37.904 | MS1 | 121.4656596614 | 31.1446279539 | 990 | 504990 | -93.96 | 10.56 | 54.62 | 0.65 | 2.39 | 669 |
| 2024-09-20 22:21:38.598 | MS1 | 121.4656592650 | 31.1446323448 | 990 | 504990 | -90.21 | 11.38 | 94.40 | 0.59 | 2.95 | 699 |
| 2024-09-20 22:21:39.136 | MS1 | 121.4656661606 | 31.1446342160 | 990 | 504990 | -90.86 | 7.30 | 74.29 | 0.54 | 2.47 | 504 |
| 2024-09-20 22:21:40.667 | MS1 | 121.4656707811 | 31.1446344468 | 990 | 504990 | -92.66 | 8.94 | 325.14 | 0.09 | 2.51 | 1570 |
| 2024-09-20 22:21:41.289 | MS1 | 121.4656665611 | 31.1446355992 | 990 | 504990 | -90.60 | 7.35 | 399.42 | 0.00 | 2.31 | 1563 |
| 2024-09-20 22:21:42.306 | MS1 | 121.4656699026 | 31.1446348315 | 990 | 504990 | -92.01 | 11.78 | 478.17 | 0.19 | 2.90 | 1594 |

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
| 3233685 | 3 | 121.4666910854 | 31.1440027321 | 195 | 3 | 4 | 45.5 | TDD | 515 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3238934 | 2 | 121.4656245932 | 31.1486021047 | 37 | 13 | 1 | 40.7 | TDD | 921 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3240762 | 1 | 121.4644992248 | 31.1535750225 | 197 | 6 | 10 | 33.4 | TDD | 512 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3261045 | 4 | 121.4725832142 | 31.1526877541 | 237 | 3 | 9 | 20.1 | TDD | 990 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:31.200 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.218 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.324 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.324 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.021 | NREventA3 | measId:2;ServCellPCI:356;Se... |
| 2024-09-20 22:21:38.261 | NRHandoverAttempt | SourcePCI:356;SourceNR-ARFC... |
| 2024-09-20 22:21:38.293 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.305 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.412 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.412 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3240762 | 1 | 5.0493 | 17.1104 | -116.5429 | 13.5134 | 169.6127 | 0.0005 | 0.0160 |
| 2024_09_20 22:00 | 3238934 | 2 | 19.0170 | 17.0142 | -115.6684 | 6.2786 | 92.1068 | 0.0159 | 0.0171 |
| 2024_09_20 22:00 | 3233685 | 3 | 17.5126 | 17.9271 | -115.4717 | 15.5549 | 163.8668 | 0.0077 | 0.0066 |
| 2024_09_20 22:00 | 3261045 | 4 | 14.4785 | 17.3220 | -114.7576 | 15.8140 | 102.6561 | 0.0188 | 0.0083 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416232_44793752 | 504990 | 990 | -88.3 | 504990 | 921 | -94.9 | 504990 | 512 | -96.1 | 504990 | 515 |
| MR_1774416232_8C9EF467 | 504990 | 990 | -88.4 | 504990 | 921 | -97.5 | 504990 | 512 | -99.1 | 504990 | 515 |
| MR_1774416232_33BB91E3 | 504990 | 990 | -88.2 | 504990 | 921 | -97.3 | 504990 | 512 | -98.0 | 504990 | 515 |
| MR_1774416232_8639B67D | 504990 | 990 | -87.0 | 504990 | 921 | -96.2 | 504990 | 512 | -96.2 | 504990 | 515 |
| MR_1774416232_EA82D54F | 504990 | 990 | -87.2 | 504990 | 921 | -96.1 | 504990 | 512 | -98.9 | 504990 | 515 |
| MR_1774416232_7C7E660B | 504990 | 990 | -88.1 | 504990 | 921 | -96.4 | 504990 | 512 | -97.7 | 504990 | 515 |
| MR_1774416232_DC69F813 | 504990 | 990 | -86.1 | 504990 | 921 | -95.3 | 504990 | 512 | -96.9 | 504990 | 515 |
| MR_1774416232_8F6A5A43 | 504990 | 990 | -89.5 | 504990 | 921 | -96.6 | 504990 | 512 | -98.8 | 504990 | 515 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1363: `63b2c7a8-b46...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `63b2c7a8-b469-4f75-80a8-305c660b4e2d` |
| Tag | **multiple-answer** |
| 정답 | **C8|C17** |
| C8 의미 | Decrease transmission power for 3222169_4 |
| C17 의미 | Press down the tilt angle  of 3222169_4 by 5 degrees |
| 패턴 분류 | **P3 Overshoot (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1363] topology](images/train_1363.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3222169_4
- `C2`: Decrease A3 Offset threshold for 3267407_1
- `C3`: Add neighbor relationship between 3265183_3 and 3222169_4
- `C4`: Lift the tilt angle of 3267407_1 by 5 degrees
- `C5`: Insufficient data; more data is needed for judgment.
- `C6`: Increase transmission power for 3222169_4
- `C7`: Press down the tilt angle of 3267407_1 by 5 degrees
- `C8`: Decrease transmission power for 3222169_4 **← 정답**
- `C9`: Add neighbor relationship between 3267407_1 and 3222169_4
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3222169_4
- `C11`: Adjust the azimuth of 3222169_4 by 4 degrees
- `C12`: Increase A3 Offset threshold for 3267407_1
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3222169_4
- `C14`: Increase transmission power for 3267407_1
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3267407_1
- `C16`: Increase A3 Offset threshold for 3222169_4
- `C17`: Press down the tilt angle  of 3222169_4 by 5 degrees **← 정답**
- `C18`: Adjust the azimuth of 3267407_1 by 6 degrees
- `C19`: Check test server and transmission issues
- `C20`: Decrease transmission power for 3267407_1
- `C21`: Lift the tilt angle  of 3222169_4 by 5 degrees
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3267407_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.431 | MS1 | 121.4656628476 | 31.1446304216 | 48 | 504990 | -81.79 | 15.69 | 568.01 | 0.01 | 2.56 | 1593 |
| 2024-09-20 22:21:32.927 | MS1 | 121.4656611676 | 31.1446245646 | 48 | 504990 | -76.90 | 16.97 | 423.75 | 0.00 | 2.49 | 1568 |
| 2024-09-20 22:21:33.447 | MS1 | 121.4656661695 | 31.1446255535 | 48 | 504990 | -77.71 | 13.57 | 549.54 | 0.06 | 2.84 | 1573 |
| 2024-09-20 22:21:34.853 | MS1 | 121.4656758450 | 31.1446312481 | 48 | 504990 | -90.07 | 1.78 | 78.99 | 0.17 | 1.02 | 1563 |
| 2024-09-20 22:21:35.177 | MS1 | 121.4656648382 | 31.1446204575 | 48 | 504990 | -86.80 | 0.55 | 63.02 | 0.15 | 1.22 | 1589 |
| 2024-09-20 22:21:36.107 | MS1 | 121.4656591056 | 31.1446235002 | 48 | 504990 | -90.42 | 1.72 | 46.00 | 0.02 | 1.31 | 1597 |
| 2024-09-20 22:21:37.444 | MS1 | 121.4656767733 | 31.1446327112 | 48 | 504990 | -94.65 | 2.70 | 36.00 | 0.11 | 1.19 | 1595 |
| 2024-09-20 22:21:38.858 | MS1 | 121.4656681210 | 31.1446274807 | 48 | 504990 | -86.43 | 3.74 | 83.00 | 0.12 | 1.24 | 1593 |
| 2024-09-20 22:21:39.793 | MS1 | 121.4656751618 | 31.1446291201 | 48 | 504990 | -92.73 | 1.52 | 37.79 | 0.03 | 1.48 | 1591 |
| 2024-09-20 22:21:40.549 | MS1 | 121.4656666619 | 31.1446347958 | 48 | 504990 | -77.75 | 17.15 | 524.95 | 0.02 | 2.43 | 1563 |
| 2024-09-20 22:21:41.579 | MS1 | 121.4656607624 | 31.1446327982 | 48 | 504990 | -83.07 | 17.80 | 545.40 | 0.15 | 2.07 | 1598 |
| 2024-09-20 22:21:42.270 | MS1 | 121.4656642635 | 31.1446310111 | 48 | 504990 | -77.83 | 16.26 | 600.69 | 0.11 | 2.31 | 1580 |

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
| 3222169 | 4 | 121.4709172464 | 31.1440897168 | 273 | 1 | 10 | 37.2 | TDD | 206 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3251956 | 2 | 121.4640555618 | 31.1451868315 | 268 | 0 | 4 | 32.8 | TDD | 226 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3265183 | 3 | 121.4694366566 | 31.1541476986 | 127 | 3 | 8 | 22.7 | TDD | 371 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3267407 | 1 | 121.4736786935 | 31.1519307014 | 229 | 2 | 0 | 49.6 | TDD | 48 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |

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
| 2024-09-20 22:21:31.352 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.373 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.496 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.496 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3267407 | 1 | 5.7024 | 14.9921 | -108.8824 | 15.4189 | 85.2934 | 0.0092 | 0.0023 |
| 2024_09_20 22:00 | 3251956 | 2 | 19.8178 | 5.5383 | -116.9618 | 12.9056 | 180.5234 | 0.0012 | 0.0087 |
| 2024_09_20 22:00 | 3265183 | 3 | 13.5918 | 13.5380 | -116.7222 | 15.7304 | 111.5133 | 0.0042 | 0.0025 |
| 2024_09_20 22:00 | 3222169 | 4 | 18.9708 | 19.9317 | -114.8301 | 6.3494 | 154.3015 | 0.0172 | 0.0034 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412211_71563FFF | 504990 | 48 | -89.2 | 504990 | 206 | -91.3 | 504990 | 371 | -93.4 | 504990 | 226 |
| MR_1774412211_6075B0E0 | 504990 | 206 | -88.2 | 504990 | 48 | -90.8 | 504990 | 371 | -92.9 | 504990 | 226 |
| MR_1774412211_0EEA8EBA | 504990 | 48 | -91.3 | 504990 | 206 | -89.7 | 504990 | 371 | -91.3 | 504990 | 226 |
| MR_1774412211_E91EEA6F | 504990 | 48 | -89.8 | 504990 | 206 | -88.4 | 504990 | 371 | -90.7 | 504990 | 226 |
| MR_1774412211_A696BF80 | 504990 | 206 | -91.4 | 504990 | 48 | -90.0 | 504990 | 371 | -92.1 | 504990 | 226 |
| MR_1774412211_88765BB8 | 504990 | 48 | -91.5 | 504990 | 206 | -89.9 | 504990 | 371 | -93.0 | 504990 | 226 |
| MR_1774412211_058B4366 | 504990 | 48 | -90.4 | 504990 | 206 | -91.6 | 504990 | 371 | -91.1 | 504990 | 226 |
| MR_1774412211_4226A4A8 | 504990 | 48 | -89.8 | 504990 | 206 | -88.7 | 504990 | 371 | -93.5 | 504990 | 226 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1364: `c8f15ca6-994...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `c8f15ca6-9943-49c9-be17-ecf25f6539fe` |
| Tag | **single-answer** |
| 정답 | **C3** |
| C3 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3238800_2 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1364] topology](images/train_1364.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle  of 3228083_1 by 2 degrees
- `C2`: Increase transmission power for 3238800_2
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3238800_2 **← 정답**
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3228083_1
- `C5`: Increase A3 Offset threshold for 3238800_2
- `C6`: Adjust the azimuth of 3238800_2 by 22 degrees
- `C7`: Lift the tilt angle of 3238800_2 by 3 degrees
- `C8`: Adjust the azimuth of 3228083_1 by 3 degrees
- `C9`: Decrease A3 Offset threshold for 3228083_1
- `C10`: Add neighbor relationship between 3238800_2 and 3228083_1
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3228083_1
- `C12`: Check test server and transmission issues
- `C13`: Decrease A3 Offset threshold for 3238800_2
- `C14`: Increase A3 Offset threshold for 3228083_1
- `C15`: Decrease transmission power for 3238800_2
- `C16`: Insufficient data; more data is needed for judgment.
- `C17`: Increase transmission power for 3228083_1
- `C18`: Press down the tilt angle  of 3228083_1 by 2 degrees
- `C19`: Add neighbor relationship between 3229182_11 and 3228083_1
- `C20`: Press down the tilt angle of 3238800_2 by 3 degrees
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3238800_2
- `C22`: Decrease transmission power for 3228083_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.661 | MS1 | 121.4656733103 | 31.1446308367 | 451 | 504990 | -95.07 | 11.64 | 476.04 | 0.08 | 2.38 | 1590 |
| 2024-09-20 22:21:32.710 | MS1 | 121.4656587480 | 31.1446180948 | 220 | 504990 | -93.99 | 13.22 | 344.16 | 0.03 | 2.11 | 1578 |
| 2024-09-20 22:21:33.850 | MS1 | 121.4656729932 | 31.1446233155 | 309 | 504990 | -95.68 | 14.95 | 486.08 | 0.10 | 2.83 | 1589 |
| 2024-09-20 22:21:34.337 | MS1 | 121.4656671971 | 31.1446319366 | 96 | 152650 | -95.07 | 6.14 | 71.47 | 0.10 | 1.60 | 922 |
| 2024-09-20 22:21:35.848 | MS1 | 121.4656662839 | 31.1446363407 | 214 | 152650 | -87.18 | 7.45 | 95.53 | 0.06 | 1.55 | 925 |
| 2024-09-20 22:21:36.967 | MS1 | 121.4656592646 | 31.1446269880 | 213 | 152650 | -89.62 | 6.86 | 56.54 | 0.16 | 1.54 | 913 |
| 2024-09-20 22:21:37.974 | MS1 | 121.4656778025 | 31.1446251167 | 32 | 152650 | -88.02 | 6.21 | 91.61 | 0.04 | 1.86 | 971 |
| 2024-09-20 22:21:38.625 | MS1 | 121.4656717751 | 31.1446348542 | 96 | 152650 | -96.06 | 2.25 | 52.57 | 0.12 | 1.87 | 905 |
| 2024-09-20 22:21:39.423 | MS1 | 121.4656636678 | 31.1446356793 | 214 | 152650 | -88.01 | 3.55 | 55.35 | 0.09 | 1.63 | 939 |
| 2024-09-20 22:21:40.900 | MS1 | 121.4656663985 | 31.1446195218 | 213 | 152650 | -92.60 | 6.21 | 84.63 | 0.03 | 2.50 | 1574 |
| 2024-09-20 22:21:41.655 | MS1 | 121.4656731343 | 31.1446245033 | 32 | 152650 | -90.91 | 7.10 | 79.66 | 0.13 | 2.52 | 1585 |
| 2024-09-20 22:21:42.913 | MS1 | 121.4656668869 | 31.1446267762 | 96 | 152650 | -96.03 | 3.11 | 51.89 | 0.17 | 2.88 | 1561 |

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
| 3226813 | 12 | 121.4708505666 | 31.1475821046 | 106 | 13 | 1 | 25.6 | FDD | 214 | n1 | 152650 | 30M | 4T4R | 20 | 152650 |
| 3227641 | 9 | 121.4659439899 | 31.1530877120 | 195 | 7 | 1 | 24.8 | FDD | 866 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |
| 3228083 | 1 | 121.4734116478 | 31.1548454542 | 216 | 2 | 8 | 10.6 | TDD | 770 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3229182 | 11 | 121.4714153118 | 31.1552938110 | 11 | 0 | 9 | 9.8 | FDD | 213 | n1 | 152650 | 30M | 4T4R | 22 | 152650 |
| 3234340 | 4 | 121.4714188649 | 31.1458378184 | 87 | 0 | 3 | 11.9 | TDD | 309 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3238800 | 2 | 121.4743947291 | 31.1507777733 | 253 | 2 | 7 | 13.7 | TDD | 451 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3239122 | 10 | 121.4677980510 | 31.1548605475 | 165 | 15 | 10 | 8.7 | FDD | 387 | n1 | 152650 | 30M | 4T4R | 25 | 152650 |
| 3248135 | 7 | 121.4683765365 | 31.1529399269 | 236 | 15 | 0 | 5.6 | FDD | 96 | n1 | 152650 | 30M | 4T4R | 29 | 152650 |
| 3250798 | 5 | 121.4667651656 | 31.1471392988 | 253 | 5 | 10 | 16.5 | TDD | 536 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3259735 | 3 | 121.4675534228 | 31.1552610849 | 220 | 13 | 8 | 4.5 | TDD | 620 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3266630 | 8 | 121.4644677658 | 31.1551193170 | 111 | 12 | 5 | 4.3 | FDD | 32 | n1 | 152650 | 30M | 4T4R | 30 | 152650 |
| 3268033 | 6 | 121.4723946503 | 31.1528200283 | 187 | 13 | 3 | 24.8 | TDD | 220 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3275314 | 13 | 121.4737796015 | 31.1473946590 | 343 | 6 | 12 | 25.9 | FDD | 345 | n1 | 152650 | 30M | 4T4R | 13 | 152650 |

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
| 2024-09-20 22:21:31.036 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.059 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.166 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.166 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.891 | NREventA2 | measId:1;ServCellPCI:455;Se... |
| 2024-09-20 22:21:34.992 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.278 | NREventA5 | measId:3;ServCellPCI:455;Se... |
| 2024-09-20 22:21:35.341 | NRHandoverAttempt | SourcePCI:455;SourceNR-ARFC... |
| 2024-09-20 22:21:35.389 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.402 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:35.527 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.527 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3228083 | 1 | 15.6108 | 7.7465 | -114.9314 | 8.6636 | 98.1630 | 0.0097 | 0.0080 |
| 2024_09_20 22:00 | 3238800 | 2 | 17.3198 | 10.6054 | -115.6811 | 9.0186 | 162.0372 | 0.0156 | 0.0035 |
| 2024_09_20 22:00 | 3259735 | 3 | 9.6673 | 12.0197 | -117.0028 | 14.5775 | 173.3971 | 0.0032 | 0.0040 |
| 2024_09_20 22:00 | 3234340 | 4 | 17.6098 | 16.5342 | -115.8761 | 11.0466 | 104.5609 | 0.0146 | 0.0162 |
| 2024_09_20 22:00 | 3250798 | 5 | 7.5208 | 16.7503 | -116.9059 | 9.8917 | 167.8007 | 0.0100 | 0.0192 |
| 2024_09_20 22:00 | 3268033 | 6 | 6.0033 | 17.5039 | -114.8311 | 18.1146 | 110.2882 | 0.0112 | 0.0170 |
| 2024_09_20 22:00 | 3248135 | 7 | 19.2743 | 13.0948 | -114.4787 | 3.1636 | 45.3560 | 0.0097 | 0.0014 |
| 2024_09_20 22:00 | 3266630 | 8 | 14.8439 | 6.0536 | -116.6723 | 4.7744 | 49.2653 | 0.0170 | 0.0054 |
| 2024_09_20 22:00 | 3227641 | 9 | 17.4177 | 12.3666 | -115.0416 | 4.3217 | 59.3826 | 0.0108 | 0.0091 |
| 2024_09_20 22:00 | 3239122 | 10 | 17.1829 | 14.3041 | -116.6798 | 3.2771 | 22.6744 | 0.0012 | 0.0085 |
| 2024_09_20 22:00 | 3229182 | 11 | 15.1201 | 16.4044 | -115.3573 | 4.3979 | 34.3062 | 0.0036 | 0.0044 |
| 2024_09_20 22:00 | 3226813 | 12 | 11.8030 | 13.6695 | -114.4363 | 3.4795 | 29.7549 | 0.0048 | 0.0065 |
| 2024_09_20 22:00 | 3275314 | 13 | 13.3643 | 6.3568 | -116.2173 | 3.1722 | 41.6571 | 0.0114 | 0.0091 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414652_5BD0740A | 504990 | 309 | -94.8 | 504990 | 770 | -95.8 | 504990 | 536 | -104.7 | 504990 | 620 |
| MR_1774414652_F72025BA | 504990 | 309 | -97.1 | 504990 | 770 | -93.2 | 504990 | 536 | -101.5 | 504990 | 620 |
| MR_1774414652_5A767A3F | 504990 | 309 | -96.9 | 504990 | 770 | -94.2 | 504990 | 536 | -100.9 | 504990 | 620 |
| MR_1774414652_A5EB3374 | 504990 | 309 | -96.6 | 504990 | 770 | -93.0 | 504990 | 536 | -101.5 | 504990 | 620 |
| MR_1774414652_582DC075 | 504990 | 309 | -93.9 | 504990 | 770 | -93.2 | 504990 | 536 | -101.3 | 504990 | 620 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1365: `811e2a5f-737...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `811e2a5f-7377-4003-a2c5-d018933b2975` |
| Tag | **single-answer** |
| 정답 | **C16** |
| C16 의미 | Decrease A3 Offset threshold for 3234931_4 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1365] topology](images/train_1365.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle  of 3263355_2 by 10 degrees
- `C2`: Press down the tilt angle  of 3263355_2 by 10 degrees
- `C3`: Lift the tilt angle of 3234931_4 by 9 degrees
- `C4`: Adjust the azimuth of 3263355_2 by 50 degrees
- `C5`: Increase A3 Offset threshold for 3263355_2
- `C6`: Adjust the azimuth of 3234931_4 by 50 degrees
- `C7`: Press down the tilt angle of 3234931_4 by 9 degrees
- `C8`: Add neighbor relationship between 3234931_4 and 3263355_2
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3234931_4
- `C10`: Increase transmission power for 3263355_2
- `C11`: Insufficient data; more data is needed for judgment.
- `C12`: Add neighbor relationship between 3221820_1 and 3263355_2
- `C13`: Check test server and transmission issues
- `C14`: Decrease A3 Offset threshold for 3263355_2
- `C15`: Increase transmission power for 3234931_4
- `C16`: Decrease A3 Offset threshold for 3234931_4 **← 정답**
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3263355_2
- `C18`: Decrease transmission power for 3234931_4
- `C19`: Increase A3 Offset threshold for 3234931_4
- `C20`: Decrease transmission power for 3263355_2
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3234931_4
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3263355_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.202 | MS1 | 121.4656687750 | 31.1446357489 | 279 | 504990 | -82.12 | 17.83 | 403.82 | 0.00 | 2.13 | 1570 |
| 2024-09-20 22:21:32.806 | MS1 | 121.4656769778 | 31.1446274434 | 279 | 504990 | -77.15 | 16.36 | 518.55 | 0.17 | 2.88 | 1567 |
| 2024-09-20 22:21:33.707 | MS1 | 121.4656729075 | 31.1446298648 | 279 | 504990 | -78.03 | 16.81 | 388.65 | 0.09 | 2.24 | 1597 |
| 2024-09-20 22:21:34.819 | MS1 | 121.4656608067 | 31.1446346065 | 279 | 504990 | -84.26 | -2.50 | 40.74 | 0.04 | 1.39 | 1562 |
| 2024-09-20 22:21:35.620 | MS1 | 121.4656681217 | 31.1446233719 | 279 | 504990 | -86.98 | -1.84 | 58.98 | 0.09 | 1.06 | 1591 |
| 2024-09-20 22:21:36.237 | MS1 | 121.4656740035 | 31.1446294678 | 279 | 504990 | -85.95 | -3.74 | 66.47 | 0.03 | 1.25 | 1594 |
| 2024-09-20 22:21:37.746 | MS1 | 121.4656686699 | 31.1446187531 | 279 | 504990 | -86.44 | -3.26 | 38.52 | 0.18 | 1.00 | 1599 |
| 2024-09-20 22:21:38.857 | MS1 | 121.4656680085 | 31.1446216149 | 279 | 504990 | -89.48 | -3.34 | 36.76 | 0.12 | 1.39 | 1599 |
| 2024-09-20 22:21:39.665 | MS1 | 121.4656698904 | 31.1446271151 | 788 | 504990 | -77.59 | 17.25 | 222.19 | 0.01 | 1.34 | 1599 |
| 2024-09-20 22:21:40.515 | MS1 | 121.4656724619 | 31.1446371758 | 788 | 504990 | -76.06 | 17.46 | 563.79 | 0.08 | 2.06 | 1582 |
| 2024-09-20 22:21:41.606 | MS1 | 121.4656589372 | 31.1446191530 | 788 | 504990 | -76.77 | 15.68 | 500.95 | 0.00 | 2.54 | 1585 |
| 2024-09-20 22:21:42.947 | MS1 | 121.4656697261 | 31.1446218768 | 788 | 504990 | -82.64 | 16.57 | 415.88 | 0.08 | 2.25 | 1571 |

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
| 3220800 | 3 | 121.4735187527 | 31.1497480097 | 305 | 9 | 3 | 25.0 | TDD | 677 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3221820 | 1 | 121.4759894014 | 31.1559534527 | 59 | 15 | 9 | 28.7 | TDD | 233 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3234931 | 4 | 121.4692930427 | 31.1538618619 | 356 | 8 | 4 | 20.6 | TDD | 279 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3263355 | 2 | 121.4756223271 | 31.1476194770 | 69 | 8 | 3 | 45.6 | TDD | 788 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |

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
| 2024-09-20 22:21:31.151 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.293 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.293 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.971 | NREventA3 | measId:2;ServCellPCI:207;Se... |
| 2024-09-20 22:21:38.211 | NRHandoverAttempt | SourcePCI:207;SourceNR-ARFC... |
| 2024-09-20 22:21:38.258 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.270 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.377 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.377 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3221820 | 1 | 16.8691 | 14.5815 | -114.0594 | 15.6421 | 113.8922 | 0.0059 | 0.0109 |
| 2024_09_20 22:00 | 3263355 | 2 | 17.0554 | 11.6086 | -116.0088 | 12.9705 | 160.9141 | 0.0060 | 0.0090 |
| 2024_09_20 22:00 | 3220800 | 3 | 11.4208 | 11.3733 | -117.8207 | 10.8998 | 131.8700 | 0.0164 | 0.0184 |
| 2024_09_20 22:00 | 3234931 | 4 | 14.7388 | 12.8419 | -115.9265 | 17.4520 | 179.4015 | 0.0134 | 0.1588 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414222_05401846 | 504990 | 279 | -83.6 | 504990 | 788 | -77.3 | 504990 | 233 | -80.6 | 504990 | 677 |
| MR_1774414222_DC83A902 | 504990 | 279 | -83.9 | 504990 | 788 | -80.0 | 504990 | 233 | -79.3 | 504990 | 677 |
| MR_1774414222_32E481A2 | 504990 | 279 | -82.9 | 504990 | 788 | -77.7 | 504990 | 233 | -78.4 | 504990 | 677 |
| MR_1774414222_75387468 | 504990 | 279 | -84.3 | 504990 | 788 | -79.3 | 504990 | 233 | -80.4 | 504990 | 677 |
| MR_1774414222_C51ED505 | 504990 | 279 | -85.1 | 504990 | 788 | -79.7 | 504990 | 233 | -78.3 | 504990 | 677 |
| MR_1774414222_C3DE60A8 | 504990 | 279 | -84.7 | 504990 | 788 | -77.4 | 504990 | 233 | -78.9 | 504990 | 677 |
| MR_1774414222_8A591C8B | 504990 | 788 | -79.8 | 504990 | 279 | -85.5 | 504990 | 233 | -80.4 | 504990 | 677 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1366: `a59fe79b-678...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `a59fe79b-6789-4327-877b-bb5baf59dff4` |
| Tag | **single-answer** |
| 정답 | **C7** |
| C7 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3246700_4 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1366] topology](images/train_1366.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3217336_3 and 3228997_1
- `C2`: Increase transmission power for 3228997_1
- `C3`: Adjust the azimuth of 3228997_1 by 50 degrees
- `C4`: Lift the tilt angle of 3246700_4 by 3 degrees
- `C5`: Increase transmission power for 3246700_4
- `C6`: Press down the tilt angle of 3246700_4 by 3 degrees
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3246700_4 **← 정답**
- `C8`: Increase A3 Offset threshold for 3228997_1
- `C9`: Press down the tilt angle  of 3228997_1 by 10 degrees
- `C10`: Decrease A3 Offset threshold for 3228997_1
- `C11`: Decrease transmission power for 3228997_1
- `C12`: Decrease transmission power for 3246700_4
- `C13`: Decrease A3 Offset threshold for 3246700_4
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3228997_1
- `C15`: Check test server and transmission issues
- `C16`: Increase A3 Offset threshold for 3246700_4
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3246700_4
- `C18`: Adjust the azimuth of 3246700_4 by 44 degrees
- `C19`: Add neighbor relationship between 3246700_4 and 3228997_1
- `C20`: Insufficient data; more data is needed for judgment.
- `C21`: Lift the tilt angle  of 3228997_1 by 10 degrees
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3228997_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.627 | MS1 | 121.4656646610 | 31.1446373459 | 356 | 504990 | -88.21 | 14.28 | 450.37 | 0.17 | 2.01 | 1583 |
| 2024-09-20 22:21:32.391 | MS1 | 121.4656682273 | 31.1446230710 | 356 | 504990 | -86.75 | 13.12 | 527.50 | 0.07 | 2.82 | 1577 |
| 2024-09-20 22:21:33.502 | MS1 | 121.4656583701 | 31.1446371761 | 356 | 504990 | -86.61 | 14.97 | 468.57 | 0.09 | 2.66 | 1563 |
| 2024-09-20 22:21:34.575 | MS1 | 121.4656659417 | 31.1446186136 | 356 | 504990 | -87.82 | 15.68 | 81.03 | 0.69 | 2.97 | 656 |
| 2024-09-20 22:21:35.734 | MS1 | 121.4656681363 | 31.1446197172 | 356 | 504990 | -85.12 | 13.45 | 92.23 | 0.58 | 2.08 | 553 |
| 2024-09-20 22:21:36.625 | MS1 | 121.4656700112 | 31.1446283240 | 356 | 504990 | -91.64 | 16.98 | 74.71 | 0.57 | 2.67 | 578 |
| 2024-09-20 22:21:37.732 | MS1 | 121.4656724659 | 31.1446333410 | 356 | 504990 | -89.41 | 8.33 | 81.14 | 0.55 | 2.89 | 566 |
| 2024-09-20 22:21:38.265 | MS1 | 121.4656661901 | 31.1446223628 | 356 | 504990 | -89.76 | 9.28 | 71.35 | 0.68 | 2.25 | 653 |
| 2024-09-20 22:21:39.486 | MS1 | 121.4656739953 | 31.1446265157 | 356 | 504990 | -90.53 | 9.84 | 55.25 | 0.69 | 2.89 | 535 |
| 2024-09-20 22:21:40.318 | MS1 | 121.4656664942 | 31.1446352875 | 356 | 504990 | -92.87 | 9.31 | 397.39 | 0.02 | 2.71 | 1595 |
| 2024-09-20 22:21:41.786 | MS1 | 121.4656657963 | 31.1446200346 | 356 | 504990 | -93.25 | 11.32 | 340.60 | 0.18 | 2.67 | 1577 |
| 2024-09-20 22:21:42.793 | MS1 | 121.4656644357 | 31.1446197687 | 356 | 504990 | -93.55 | 10.62 | 341.54 | 0.01 | 2.93 | 1582 |

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
| 3217336 | 3 | 121.4715329494 | 31.1484679687 | 280 | 3 | 10 | 28.4 | TDD | 226 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3228997 | 1 | 121.4659794322 | 31.1498534702 | 354 | 10 | 5 | 30.0 | TDD | 72 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3246700 | 4 | 121.4719115718 | 31.1551531333 | 251 | 2 | 12 | 15.6 | TDD | 356 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3273674 | 2 | 121.4687531227 | 31.1492232531 | 124 | 11 | 10 | 25.3 | TDD | 497 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:31.581 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.709 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.709 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.396 | NREventA3 | measId:2;ServCellPCI:292;Se... |
| 2024-09-20 22:21:38.636 | NRHandoverAttempt | SourcePCI:292;SourceNR-ARFC... |
| 2024-09-20 22:21:38.670 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.683 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.791 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.791 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3228997 | 1 | 14.1937 | 14.3549 | -116.3441 | 8.3315 | 181.1588 | 0.0168 | 0.0027 |
| 2024_09_20 22:00 | 3273674 | 2 | 7.9342 | 19.6365 | -117.7780 | 12.2660 | 131.1150 | 0.0013 | 0.0177 |
| 2024_09_20 22:00 | 3217336 | 3 | 5.1522 | 16.3900 | -116.6851 | 12.1831 | 90.0769 | 0.0038 | 0.0022 |
| 2024_09_20 22:00 | 3246700 | 4 | 6.8650 | 19.2364 | -117.6002 | 6.5706 | 187.0500 | 0.0197 | 0.0060 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414526_D95C3DF5 | 504990 | 356 | -86.2 | 504990 | 72 | -94.4 | 504990 | 226 | -103.0 | 504990 | 497 |
| MR_1774414526_044B15BB | 504990 | 356 | -85.9 | 504990 | 72 | -96.7 | 504990 | 226 | -100.8 | 504990 | 497 |
| MR_1774414526_846D3DE2 | 504990 | 356 | -85.9 | 504990 | 72 | -94.8 | 504990 | 226 | -102.2 | 504990 | 497 |
| MR_1774414526_97FFE9B2 | 504990 | 356 | -86.9 | 504990 | 72 | -93.1 | 504990 | 226 | -101.9 | 504990 | 497 |
| MR_1774414526_4EF54365 | 504990 | 356 | -86.4 | 504990 | 72 | -95.0 | 504990 | 226 | -101.7 | 504990 | 497 |
| MR_1774414526_76F8D7A8 | 504990 | 356 | -87.8 | 504990 | 72 | -96.1 | 504990 | 226 | -100.5 | 504990 | 497 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1367: `b45b36e7-862...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `b45b36e7-862d-4a9e-87c4-82a076bc9276` |
| Tag | **single-answer** |
| 정답 | **C22** |
| C22 의미 | Add neighbor relationship between 3253882_3 and 3275617_4 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1367] topology](images/train_1367.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment.
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3253882_3
- `C3`: Decrease A3 Offset threshold for 3253882_3
- `C4`: Press down the tilt angle of 3253882_3 by 6 degrees
- `C5`: Increase A3 Offset threshold for 3275617_4
- `C6`: Increase A3 Offset threshold for 3253882_3
- `C7`: Decrease A3 Offset threshold for 3275617_4
- `C8`: Decrease transmission power for 3253882_3
- `C9`: Decrease transmission power for 3275617_4
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3275617_4
- `C11`: Check test server and transmission issues
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3275617_4
- `C13`: Lift the tilt angle of 3253882_3 by 6 degrees
- `C14`: Adjust the azimuth of 3253882_3 by 50 degrees
- `C15`: Add neighbor relationship between 3226424_2 and 3275617_4
- `C16`: Increase transmission power for 3253882_3
- `C17`: Adjust the azimuth of 3275617_4 by 12 degrees
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3253882_3
- `C19`: Increase transmission power for 3275617_4
- `C20`: Lift the tilt angle  of 3275617_4 by 4 degrees
- `C21`: Press down the tilt angle  of 3275617_4 by 4 degrees
- `C22`: Add neighbor relationship between 3253882_3 and 3275617_4 **← 정답**

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.979 | MS1 | 121.4656759482 | 31.1446320578 | 549 | 504990 | -76.22 | 13.11 | 582.78 | 0.06 | 2.18 | 1597 |
| 2024-09-20 22:21:32.850 | MS1 | 121.4656613174 | 31.1446247694 | 549 | 504990 | -77.25 | 13.99 | 493.06 | 0.08 | 2.06 | 1580 |
| 2024-09-20 22:21:33.869 | MS1 | 121.4656729730 | 31.1446291424 | 549 | 504990 | -84.18 | 15.36 | 511.06 | 0.17 | 2.98 | 1568 |
| 2024-09-20 22:21:34.353 | MS1 | 121.4656631167 | 31.1446294039 | 549 | 504990 | -93.92 | -1.21 | 63.03 | 0.19 | 1.36 | 1586 |
| 2024-09-20 22:21:35.143 | MS1 | 121.4656591232 | 31.1446339861 | 549 | 504990 | -93.06 | -3.27 | 69.15 | 0.07 | 1.41 | 1574 |
| 2024-09-20 22:21:36.806 | MS1 | 121.4656770074 | 31.1446368430 | 549 | 504990 | -89.72 | -2.36 | 44.05 | 0.10 | 1.24 | 1590 |
| 2024-09-20 22:21:37.497 | MS1 | 121.4656739562 | 31.1446261297 | 549 | 504990 | -92.05 | -3.21 | 27.38 | 0.00 | 1.25 | 1598 |
| 2024-09-20 22:21:38.866 | MS1 | 121.4656628196 | 31.1446225387 | 549 | 504990 | -82.01 | 17.71 | 571.19 | 0.16 | 1.35 | 1584 |
| 2024-09-20 22:21:39.339 | MS1 | 121.4656615636 | 31.1446355525 | 549 | 504990 | -83.19 | 17.38 | 445.55 | 0.07 | 1.04 | 1594 |
| 2024-09-20 22:21:40.986 | MS1 | 121.4656777084 | 31.1446236280 | 549 | 504990 | -83.78 | 17.02 | 554.21 | 0.09 | 2.88 | 1579 |
| 2024-09-20 22:21:41.743 | MS1 | 121.4656671832 | 31.1446266788 | 549 | 504990 | -77.25 | 15.85 | 297.65 | 0.14 | 2.38 | 1566 |
| 2024-09-20 22:21:42.624 | MS1 | 121.4656719070 | 31.1446194808 | 549 | 504990 | -75.22 | 12.35 | 556.59 | 0.10 | 2.50 | 1584 |

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
| 3226424 | 2 | 121.4745958919 | 31.1517158222 | 141 | 7 | 5 | 32.0 | TDD | 68 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3253882 | 3 | 121.4666059324 | 31.1541407639 | 266 | 4 | 4 | 44.5 | TDD | 549 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3264086 | 1 | 121.4670093653 | 31.1532150396 | 203 | 5 | 12 | 44.3 | TDD | 939 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3275617 | 4 | 121.4749164122 | 31.1527636786 | 212 | 3 | 2 | 17.4 | TDD | 478 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |

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
| 2024-09-20 22:21:31.020 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.037 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.170 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.170 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.881 | NREventA3 | measId:2;ServCellPCI:607;Se... |
| 2024-09-20 22:21:35.881 | NREventA3 | measId:2;ServCellPCI:607;Se... |
| 2024-09-20 22:21:36.881 | NREventA3 | measId:2;ServCellPCI:607;Se... |
| 2024-09-20 22:21:39.381 | NRRRCReestablishAttempt | PCI:607 |
| 2024-09-20 22:21:39.393 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.403 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:39.549 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.549 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3264086 | 1 | 6.3984 | 13.9461 | -116.3565 | 10.3817 | 148.4169 | 0.0015 | 0.0075 |
| 2024_09_20 22:00 | 3226424 | 2 | 7.7124 | 15.8441 | -116.4456 | 10.4560 | 156.3459 | 0.0186 | 0.0074 |
| 2024_09_20 22:00 | 3253882 | 3 | 12.9610 | 17.3844 | -114.0728 | 11.1412 | 157.9672 | 0.0118 | 0.1770 |
| 2024_09_20 22:00 | 3275617 | 4 | 13.1007 | 7.8816 | -114.0420 | 8.7973 | 180.3378 | 0.0105 | 0.0046 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413409_4B818AE4 | 504990 | 478 | -88.5 | 504990 | 549 | -94.6 | 504990 | 68 | -96.2 | 504990 | 939 |
| MR_1774413409_9FDB5A7F | 504990 | 549 | -93.6 | 504990 | 478 | -88.4 | 504990 | 68 | -96.5 | 504990 | 939 |
| MR_1774413409_3014D47D | 504990 | 478 | -88.0 | 504990 | 549 | -95.7 | 504990 | 68 | -97.0 | 504990 | 939 |
| MR_1774413409_B0D60371 | 504990 | 549 | -94.9 | 504990 | 478 | -90.0 | 504990 | 68 | -95.9 | 504990 | 939 |
| MR_1774413409_853AD4B2 | 504990 | 549 | -93.3 | 504990 | 478 | -89.8 | 504990 | 68 | -97.5 | 504990 | 939 |
| MR_1774413409_A8F0C148 | 504990 | 549 | -94.3 | 504990 | 478 | -90.4 | 504990 | 68 | -95.4 | 504990 | 939 |
| MR_1774413409_1FB337F4 | 504990 | 478 | -86.7 | 504990 | 549 | -95.9 | 504990 | 68 | -96.3 | 504990 | 939 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1368: `b4ad2782-7b8...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `b4ad2782-7b88-44a8-86bc-dc307d1dc195` |
| Tag | **single-answer** |
| 정답 | **C2** |
| C2 의미 | Decrease A3 Offset threshold for 3211427_1 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1368] topology](images/train_1368.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3211427_1 by 24 degrees
- `C2`: Decrease A3 Offset threshold for 3211427_1 **← 정답**
- `C3`: Adjust the azimuth of 3226887_2 by 9 degrees
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3226887_2
- `C5`: Press down the tilt angle  of 3226887_2 by 10 degrees
- `C6`: Decrease transmission power for 3211427_1
- `C7`: Increase A3 Offset threshold for 3211427_1
- `C8`: Increase A3 Offset threshold for 3226887_2
- `C9`: Add neighbor relationship between 3260959_3 and 3226887_2
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3211427_1
- `C11`: Lift the tilt angle of 3211427_1 by 10 degrees
- `C12`: Add neighbor relationship between 3211427_1 and 3226887_2
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3226887_2
- `C14`: Lift the tilt angle  of 3226887_2 by 10 degrees
- `C15`: Increase transmission power for 3226887_2
- `C16`: Decrease transmission power for 3226887_2
- `C17`: Press down the tilt angle of 3211427_1 by 10 degrees
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3211427_1
- `C19`: Check test server and transmission issues
- `C20`: Increase transmission power for 3211427_1
- `C21`: Insufficient data; more data is needed for judgment.
- `C22`: Decrease A3 Offset threshold for 3226887_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.581 | MS1 | 121.4656714789 | 31.1446338870 | 50 | 504990 | -81.98 | 16.93 | 477.90 | 0.00 | 2.23 | 1594 |
| 2024-09-20 22:21:32.877 | MS1 | 121.4656599910 | 31.1446297718 | 50 | 504990 | -84.86 | 12.71 | 473.19 | 0.20 | 2.21 | 1584 |
| 2024-09-20 22:21:33.378 | MS1 | 121.4656657144 | 31.1446281385 | 50 | 504990 | -76.01 | 13.64 | 531.11 | 0.17 | 2.73 | 1568 |
| 2024-09-20 22:21:34.736 | MS1 | 121.4656623909 | 31.1446330873 | 50 | 504990 | -85.17 | -2.58 | 58.25 | 0.03 | 1.00 | 1562 |
| 2024-09-20 22:21:35.644 | MS1 | 121.4656738038 | 31.1446254470 | 50 | 504990 | -86.02 | -3.51 | 62.83 | 0.12 | 1.46 | 1599 |
| 2024-09-20 22:21:36.509 | MS1 | 121.4656629026 | 31.1446277853 | 50 | 504990 | -92.02 | -3.68 | 52.19 | 0.18 | 1.00 | 1570 |
| 2024-09-20 22:21:37.405 | MS1 | 121.4656713374 | 31.1446208974 | 50 | 504990 | -90.86 | -1.72 | 73.55 | 0.14 | 1.36 | 1566 |
| 2024-09-20 22:21:38.720 | MS1 | 121.4656601281 | 31.1446365013 | 50 | 504990 | -83.52 | -3.04 | 44.78 | 0.18 | 1.06 | 1587 |
| 2024-09-20 22:21:39.408 | MS1 | 121.4656752369 | 31.1446247478 | 923 | 504990 | -75.35 | 17.51 | 231.03 | 0.18 | 1.44 | 1573 |
| 2024-09-20 22:21:40.404 | MS1 | 121.4656721051 | 31.1446346359 | 923 | 504990 | -79.20 | 13.62 | 516.28 | 0.11 | 2.13 | 1576 |
| 2024-09-20 22:21:41.529 | MS1 | 121.4656743116 | 31.1446268811 | 923 | 504990 | -82.95 | 15.29 | 334.56 | 0.17 | 2.01 | 1563 |
| 2024-09-20 22:21:42.990 | MS1 | 121.4656649679 | 31.1446344931 | 923 | 504990 | -78.17 | 15.01 | 433.81 | 0.10 | 2.03 | 1568 |

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
| 3211427 | 1 | 121.4649586208 | 31.1482220176 | 146 | 14 | 8 | 43.8 | TDD | 50 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3226887 | 2 | 121.4719855653 | 31.1452049642 | 273 | 14 | 11 | 24.3 | TDD | 923 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3260959 | 3 | 121.4746713504 | 31.1447635238 | 186 | 11 | 8 | 24.3 | TDD | 899 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3277228 | 4 | 121.4748563432 | 31.1474625257 | 176 | 14 | 0 | 34.5 | TDD | 54 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |

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
| 2024-09-20 22:21:30.829 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.854 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:30.978 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.978 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.684 | NREventA3 | measId:2;ServCellPCI:246;Se... |
| 2024-09-20 22:21:37.924 | NRHandoverAttempt | SourcePCI:246;SourceNR-ARFC... |
| 2024-09-20 22:21:37.971 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.986 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.114 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.114 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3211427 | 1 | 10.8103 | 12.5119 | -114.7294 | 12.3629 | 120.1250 | 0.0123 | 0.1075 |
| 2024_09_20 22:00 | 3226887 | 2 | 5.6450 | 11.8760 | -115.4693 | 18.2467 | 101.5652 | 0.0043 | 0.0174 |
| 2024_09_20 22:00 | 3260959 | 3 | 6.2240 | 18.7991 | -114.8650 | 9.1181 | 145.0563 | 0.0108 | 0.0028 |
| 2024_09_20 22:00 | 3277228 | 4 | 12.1214 | 9.0762 | -116.7125 | 18.6046 | 109.1705 | 0.0010 | 0.0143 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412978_309E68C7 | 504990 | 50 | -86.4 | 504990 | 923 | -80.1 | 504990 | 899 | -83.0 | 504990 | 54 |
| MR_1774412978_C34397EB | 504990 | 923 | -81.2 | 504990 | 50 | -86.9 | 504990 | 899 | -84.9 | 504990 | 54 |
| MR_1774412978_4D85DE85 | 504990 | 923 | -80.9 | 504990 | 50 | -84.4 | 504990 | 899 | -86.1 | 504990 | 54 |
| MR_1774412978_78BC20AD | 504990 | 50 | -86.7 | 504990 | 923 | -82.3 | 504990 | 899 | -84.7 | 504990 | 54 |
| MR_1774412978_1F2B78BF | 504990 | 923 | -82.4 | 504990 | 50 | -86.5 | 504990 | 899 | -85.5 | 504990 | 54 |
| MR_1774412978_2750D7CE | 504990 | 923 | -81.2 | 504990 | 50 | -85.1 | 504990 | 899 | -84.4 | 504990 | 54 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1369: `859f89ba-ca4...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `859f89ba-ca4d-40d9-9cf4-2da577e57580` |
| Tag | **single-answer** |
| 정답 | **C11** |
| C11 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3269578_3 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1369] topology](images/train_1369.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3210571_4
- `C2`: Decrease A3 Offset threshold for 3269578_3
- `C3`: Adjust the azimuth of 3269578_3 by 19 degrees
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3269578_3
- `C5`: Decrease A3 Offset threshold for 3210571_4
- `C6`: Increase A3 Offset threshold for 3210571_4
- `C7`: Lift the tilt angle  of 3210571_4 by 7 degrees
- `C8`: Decrease transmission power for 3269578_3
- `C9`: Decrease transmission power for 3210571_4
- `C10`: Press down the tilt angle of 3269578_3 by 2 degrees
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3269578_3 **← 정답**
- `C12`: Insufficient data; more data is needed for judgment.
- `C13`: Add neighbor relationship between 3269578_3 and 3210571_4
- `C14`: Increase A3 Offset threshold for 3269578_3
- `C15`: Add neighbor relationship between 3247066_1 and 3210571_4
- `C16`: Adjust the azimuth of 3210571_4 by 50 degrees
- `C17`: Press down the tilt angle  of 3210571_4 by 7 degrees
- `C18`: Lift the tilt angle of 3269578_3 by 2 degrees
- `C19`: Check test server and transmission issues
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3210571_4
- `C21`: Increase transmission power for 3269578_3
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3210571_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.727 | MS1 | 121.4656657623 | 31.1446237264 | 91 | 504990 | -86.46 | 16.91 | 373.69 | 0.10 | 2.97 | 1574 |
| 2024-09-20 22:21:32.984 | MS1 | 121.4656641807 | 31.1446267758 | 91 | 504990 | -85.42 | 14.53 | 523.31 | 0.15 | 2.41 | 1560 |
| 2024-09-20 22:21:33.325 | MS1 | 121.4656698770 | 31.1446257437 | 91 | 504990 | -91.81 | 12.52 | 332.97 | 0.10 | 2.87 | 1569 |
| 2024-09-20 22:21:34.685 | MS1 | 121.4656633724 | 31.1446247335 | 91 | 504990 | -90.60 | 17.70 | 49.68 | 0.53 | 2.13 | 512 |
| 2024-09-20 22:21:35.969 | MS1 | 121.4656706987 | 31.1446198402 | 91 | 504990 | -87.37 | 17.22 | 91.73 | 0.61 | 2.05 | 575 |
| 2024-09-20 22:21:36.527 | MS1 | 121.4656759192 | 31.1446302304 | 91 | 504990 | -91.54 | 12.68 | 62.15 | 0.54 | 2.54 | 618 |
| 2024-09-20 22:21:37.946 | MS1 | 121.4656609803 | 31.1446264969 | 91 | 504990 | -92.41 | 7.73 | 96.47 | 0.56 | 2.00 | 554 |
| 2024-09-20 22:21:38.982 | MS1 | 121.4656591024 | 31.1446273953 | 91 | 504990 | -92.88 | 8.46 | 69.03 | 0.64 | 2.61 | 660 |
| 2024-09-20 22:21:39.407 | MS1 | 121.4656621691 | 31.1446308014 | 91 | 504990 | -92.46 | 8.20 | 79.92 | 0.54 | 2.04 | 609 |
| 2024-09-20 22:21:40.407 | MS1 | 121.4656731008 | 31.1446332236 | 91 | 504990 | -92.01 | 9.62 | 600.89 | 0.13 | 2.89 | 1586 |
| 2024-09-20 22:21:41.140 | MS1 | 121.4656692755 | 31.1446264455 | 91 | 504990 | -92.98 | 10.05 | 506.55 | 0.10 | 2.54 | 1580 |
| 2024-09-20 22:21:42.349 | MS1 | 121.4656718713 | 31.1446237066 | 91 | 504990 | -89.53 | 11.39 | 350.10 | 0.08 | 2.19 | 1585 |

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
| 3210571 | 4 | 121.4679737032 | 31.1547018069 | 37 | 6 | 2 | 26.3 | TDD | 636 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3247066 | 1 | 121.4642032147 | 31.1533109983 | 261 | 7 | 7 | 21.6 | TDD | 976 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3269578 | 3 | 121.4737020132 | 31.1523103495 | 203 | 0 | 10 | 32.2 | TDD | 91 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3279902 | 2 | 121.4730589123 | 31.1447275690 | 28 | 5 | 2 | 37.1 | TDD | 594 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

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
| 2024-09-20 22:21:31.188 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.210 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.343 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.343 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.042 | NREventA3 | measId:2;ServCellPCI:959;Se... |
| 2024-09-20 22:21:38.282 | NRHandoverAttempt | SourcePCI:959;SourceNR-ARFC... |
| 2024-09-20 22:21:38.319 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.331 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.434 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.434 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3247066 | 1 | 7.9970 | 13.8370 | -114.8277 | 10.3101 | 91.7821 | 0.0133 | 0.0067 |
| 2024_09_20 22:00 | 3279902 | 2 | 6.3343 | 7.3251 | -116.0856 | 9.5383 | 159.9929 | 0.0024 | 0.0095 |
| 2024_09_20 22:00 | 3269578 | 3 | 11.4668 | 8.2748 | -116.5411 | 17.6459 | 135.5072 | 0.0179 | 0.0127 |
| 2024_09_20 22:00 | 3210571 | 4 | 10.1958 | 6.6498 | -117.7680 | 8.7800 | 150.0757 | 0.0090 | 0.0172 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416742_EE54DF1A | 504990 | 91 | -88.8 | 504990 | 636 | -91.9 | 504990 | 976 | -95.8 | 504990 | 594 |
| MR_1774416742_E2E62CC2 | 504990 | 91 | -89.3 | 504990 | 636 | -91.4 | 504990 | 976 | -99.3 | 504990 | 594 |
| MR_1774416742_63A90CDB | 504990 | 91 | -92.5 | 504990 | 636 | -88.5 | 504990 | 976 | -98.2 | 504990 | 594 |
| MR_1774416742_A3050933 | 504990 | 91 | -91.4 | 504990 | 636 | -89.3 | 504990 | 976 | -96.3 | 504990 | 594 |
| MR_1774416742_C1B9A5E0 | 504990 | 91 | -90.6 | 504990 | 636 | -92.2 | 504990 | 976 | -98.9 | 504990 | 594 |

> *... 2개 열 생략 (전체 14열)*

---
