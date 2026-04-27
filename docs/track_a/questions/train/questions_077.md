# Track A 문제 분석 — train[760]~train[769]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[760] ~ train[769] (10개)

## 목차

1. [문제 760: `92d9ac2e-d7e...`](#760) — multiple-answer, 정답: C12|C16
2. [문제 761: `844a4562-9bd...`](#761) — multiple-answer, 정답: C1|C4|C12|C13
3. [문제 762: `abb80e66-827...`](#762) — single-answer, 정답: C11
4. [문제 763: `308d192c-7de...`](#763) — single-answer, 정답: C6
5. [문제 764: `d6c4aa62-ef0...`](#764) — multiple-answer, 정답: C10|C19
6. [문제 765: `9c022d66-ca4...`](#765) — single-answer, 정답: C12
7. [문제 766: `91959b19-78b...`](#766) — single-answer, 정답: C14
8. [문제 767: `8a6b55b7-fc6...`](#767) — single-answer, 정답: C12
9. [문제 768: `857c87e0-e50...`](#768) — single-answer, 정답: C19
10. [문제 769: `f698b104-1a9...`](#769) — single-answer, 정답: C20

---

### 문제 760: `92d9ac2e-d7e...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `92d9ac2e-d7e0-4788-939f-a66af7c81eae` |
| Tag | **multiple-answer** |
| 정답 | **C12|C16** |
| C12 의미 | Increase transmission power for 3241055_2 |
| C16 의미 | Adjust the azimuth of 3241055_2 by 50 degrees |
| 패턴 분류 | **P4 Coverage (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[760] topology](images/train_0760.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3256916_4
- `C2`: Press down the tilt angle of 3241055_2 by 10 degrees
- `C3`: Press down the tilt angle  of 3256916_4 by 4 degrees
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3256916_4
- `C5`: Decrease A3 Offset threshold for 3241055_2
- `C6`: Increase transmission power for 3256916_4
- `C7`: Decrease transmission power for 3256916_4
- `C8`: Add neighbor relationship between 3241055_2 and 3256916_4
- `C9`: Insufficient data; more data is needed for judgment.
- `C10`: Decrease transmission power for 3241055_2
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3241055_2
- `C12`: Increase transmission power for 3241055_2 **← 정답**
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3241055_2
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3256916_4
- `C15`: Lift the tilt angle of 3241055_2 by 10 degrees
- `C16`: Adjust the azimuth of 3241055_2 by 50 degrees **← 정답**
- `C17`: Lift the tilt angle  of 3256916_4 by 4 degrees
- `C18`: Increase A3 Offset threshold for 3241055_2
- `C19`: Add neighbor relationship between 3271954_3 and 3256916_4
- `C20`: Increase A3 Offset threshold for 3256916_4
- `C21`: Check test server and transmission issues
- `C22`: Adjust the azimuth of 3256916_4 by 25 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.483 | MS1 | 121.4656669262 | 31.1446180697 | 117 | 504990 | -94.50 | 17.72 | 413.39 | 0.07 | 2.83 | 1583 |
| 2024-09-20 22:21:32.451 | MS1 | 121.4656768825 | 31.1446236035 | 117 | 504990 | -88.33 | 17.56 | 348.27 | 0.18 | 2.05 | 1598 |
| 2024-09-20 22:21:33.819 | MS1 | 121.4656778755 | 31.1446231491 | 117 | 504990 | -90.36 | 17.74 | 551.74 | 0.20 | 2.84 | 1585 |
| 2024-09-20 22:21:34.946 | MS1 | 121.4656766973 | 31.1446280886 | 117 | 504990 | -102.38 | 0.94 | 53.45 | 0.10 | 1.40 | 1578 |
| 2024-09-20 22:21:35.956 | MS1 | 121.4656613379 | 31.1446202175 | 117 | 504990 | -100.66 | -0.46 | 68.92 | 0.05 | 1.31 | 1587 |
| 2024-09-20 22:21:36.497 | MS1 | 121.4656746038 | 31.1446288244 | 117 | 504990 | -105.18 | -1.04 | 70.26 | 0.08 | 1.27 | 1575 |
| 2024-09-20 22:21:37.687 | MS1 | 121.4656684344 | 31.1446359416 | 117 | 504990 | -107.41 | -0.57 | 12.49 | 0.16 | 1.17 | 1596 |
| 2024-09-20 22:21:38.855 | MS1 | 121.4656678444 | 31.1446358970 | 117 | 504990 | -105.97 | 1.95 | 32.39 | 0.12 | 1.40 | 1565 |
| 2024-09-20 22:21:39.279 | MS1 | 121.4656610562 | 31.1446244334 | 117 | 504990 | -108.98 | 0.81 | 69.58 | 0.15 | 1.37 | 1596 |
| 2024-09-20 22:21:40.914 | MS1 | 121.4656632887 | 31.1446200984 | 117 | 504990 | -93.04 | 17.79 | 530.43 | 0.08 | 2.93 | 1562 |
| 2024-09-20 22:21:41.528 | MS1 | 121.4656724816 | 31.1446363936 | 117 | 504990 | -88.40 | 13.50 | 564.15 | 0.10 | 2.75 | 1596 |
| 2024-09-20 22:21:42.828 | MS1 | 121.4656649638 | 31.1446276574 | 117 | 504990 | -89.88 | 13.97 | 329.09 | 0.16 | 2.75 | 1577 |

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
| 3241055 | 2 | 121.4688936666 | 31.1520022735 | 148 | 13 | 5 | 29.6 | TDD | 117 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3250893 | 1 | 121.4677342734 | 31.1475644809 | 178 | 3 | 9 | 27.2 | TDD | 564 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3256916 | 4 | 121.4725349423 | 31.1460442411 | 282 | 1 | 10 | 35.8 | TDD | 735 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3271954 | 3 | 121.4750396808 | 31.1516618725 | 195 | 14 | 12 | 34.2 | TDD | 70 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:30.935 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.957 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.067 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.067 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.288 | NREventA2 | measId:1;ServCellPCI:910;Se... |
| 2024-09-20 22:21:34.399 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3250893 | 1 | 8.5535 | 18.3138 | -117.8986 | 16.1482 | 135.2241 | 0.0151 | 0.0101 |
| 2024_09_20 22:00 | 3241055 | 2 | 15.4315 | 19.6917 | -115.5026 | 8.1178 | 131.5499 | 0.1659 | 0.0107 |
| 2024_09_20 22:00 | 3271954 | 3 | 7.3487 | 12.6594 | -117.8057 | 15.4942 | 156.3512 | 0.0105 | 0.0084 |
| 2024_09_20 22:00 | 3256916 | 4 | 11.8987 | 11.9497 | -116.5810 | 18.1947 | 102.6883 | 0.0035 | 0.0155 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414851_41B8879C | 504990 | 117 | -101.6 | 504990 | 735 | -105.3 | 504990 | 70 | -112.4 | 504990 | 564 |
| MR_1774414851_125B2D73 | 504990 | 117 | -102.7 | 504990 | 735 | -107.1 | 504990 | 70 | -113.3 | 504990 | 564 |
| MR_1774414851_C9D1F19B | 504990 | 117 | -103.7 | 504990 | 735 | -106.9 | 504990 | 70 | -111.9 | 504990 | 564 |
| MR_1774414851_513B891D | 504990 | 117 | -102.1 | 504990 | 735 | -105.1 | 504990 | 70 | -113.5 | 504990 | 564 |
| MR_1774414851_DD45AD0C | 504990 | 117 | -102.9 | 504990 | 735 | -106.6 | 504990 | 70 | -111.4 | 504990 | 564 |
| MR_1774414851_09264C23 | 504990 | 117 | -103.7 | 504990 | 735 | -108.8 | 504990 | 70 | -112.9 | 504990 | 564 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 761: `844a4562-9bd...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `844a4562-9bd2-4b3a-837e-4a4e09f0ecf9` |
| Tag | **multiple-answer** |
| 정답 | **C1|C4|C12|C13** |
| C1 의미 | Press down the tilt angle  of 3225307_2 by 6 degrees |
| C4 의미 | Increase A3 Offset threshold for 3225307_2 |
| C12 의미 | Decrease transmission power for 3225307_2 |
| C13 의미 | Increase A3 Offset threshold for 3216577_3 |
| 패턴 분류 | **P3 Overshoot (tilt)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[761] topology](images/train_0761.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 5 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 5개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3225307_2 by 6 degrees **← 정답**
- `C2`: Press down the tilt angle of 3216577_3 by 4 degrees
- `C3`: Decrease A3 Offset threshold for 3225307_2
- `C4`: Increase A3 Offset threshold for 3225307_2 **← 정답**
- `C5`: Add neighbor relationship between 3278943_4 and 3225307_2
- `C6`: Increase transmission power for 3216577_3
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3225307_2
- `C8`: Adjust the azimuth of 3216577_3 by 28 degrees
- `C9`: Insufficient data; more data is needed for judgment.
- `C10`: Increase transmission power for 3225307_2
- `C11`: Lift the tilt angle  of 3225307_2 by 6 degrees
- `C12`: Decrease transmission power for 3225307_2 **← 정답**
- `C13`: Increase A3 Offset threshold for 3216577_3 **← 정답**
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3216577_3
- `C15`: Check test server and transmission issues
- `C16`: Lift the tilt angle of 3216577_3 by 4 degrees
- `C17`: Adjust the azimuth of 3225307_2 by 6 degrees
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3225307_2
- `C19`: Decrease transmission power for 3216577_3
- `C20`: Add neighbor relationship between 3216577_3 and 3225307_2
- `C21`: Decrease A3 Offset threshold for 3216577_3
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3216577_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.899 | MS1 | 121.4656632734 | 31.1446367481 | 728 | 504990 | -78.54 | 15.28 | 443.27 | 0.15 | 2.51 | 1595 |
| 2024-09-20 22:21:32.290 | MS1 | 121.4656641118 | 31.1446267474 | 728 | 504990 | -83.60 | 13.70 | 527.57 | 0.01 | 2.70 | 1596 |
| 2024-09-20 22:21:33.498 | MS1 | 121.4656675136 | 31.1446370987 | 728 | 504990 | -77.98 | 14.94 | 395.00 | 0.02 | 2.79 | 1599 |
| 2024-09-20 22:21:34.132 | MS1 | 121.4656659360 | 31.1446349177 | 318 | 504990 | -86.15 | 3.23 | 76.00 | 0.03 | 1.38 | 1583 |
| 2024-09-20 22:21:35.213 | MS1 | 121.4656716671 | 31.1446343887 | 318 | 504990 | -82.24 | 2.74 | 87.68 | 0.14 | 1.02 | 1561 |
| 2024-09-20 22:21:36.807 | MS1 | 121.4656701951 | 31.1446294473 | 728 | 504990 | -89.76 | 2.81 | 68.68 | 0.00 | 1.49 | 1587 |
| 2024-09-20 22:21:37.419 | MS1 | 121.4656583671 | 31.1446338598 | 728 | 504990 | -88.01 | 1.91 | 74.81 | 0.06 | 1.03 | 1589 |
| 2024-09-20 22:21:38.665 | MS1 | 121.4656624988 | 31.1446191549 | 318 | 504990 | -86.99 | 2.80 | 47.27 | 0.01 | 1.45 | 1570 |
| 2024-09-20 22:21:39.339 | MS1 | 121.4656705537 | 31.1446301907 | 318 | 504990 | -80.17 | 1.69 | 37.12 | 0.08 | 1.11 | 1564 |
| 2024-09-20 22:21:40.499 | MS1 | 121.4656694332 | 31.1446203305 | 318 | 504990 | -77.03 | 16.60 | 444.34 | 0.10 | 2.78 | 1589 |
| 2024-09-20 22:21:41.999 | MS1 | 121.4656627057 | 31.1446370388 | 318 | 504990 | -79.68 | 12.03 | 482.11 | 0.06 | 2.14 | 1569 |
| 2024-09-20 22:21:42.229 | MS1 | 121.4656727181 | 31.1446191565 | 318 | 504990 | -81.30 | 15.61 | 341.00 | 0.06 | 2.15 | 1591 |

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
| 3212379 | 5 | 121.4721430964 | 31.1496331618 | 91 | 8 | 0 | 42.5 | TDD | 318 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3213581 | 1 | 121.4711795694 | 31.1558157725 | 27 | 14 | 6 | 39.2 | TDD | 741 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3216577 | 3 | 121.4747003190 | 31.1551965258 | 188 | 3 | 2 | 15.7 | TDD | 728 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3225307 | 2 | 121.4724032424 | 31.1492548323 | 237 | 4 | 6 | 27.9 | TDD | 907 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3278943 | 4 | 121.4744865840 | 31.1553674850 | 287 | 3 | 10 | 37.6 | TDD | 472 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |

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
| 2024-09-20 22:21:31.517 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.542 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.657 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.657 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.410 | NREventA3 | measId:2;ServCellPCI:833;Se... |
| 2024-09-20 22:21:34.650 | NRHandoverAttempt | SourcePCI:833;SourceNR-ARFC... |
| 2024-09-20 22:21:34.699 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:34.711 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:34.829 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:34.829 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:36.410 | NREventA3 | measId:2;ServCellPCI:889;Se... |
| 2024-09-20 22:21:36.650 | NRHandoverAttempt | SourcePCI:889;SourceNR-ARFC... |
| 2024-09-20 22:21:36.688 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:36.698 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:36.803 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.803 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.410 | NREventA3 | measId:2;ServCellPCI:833;Se... |
| 2024-09-20 22:21:38.650 | NRHandoverAttempt | SourcePCI:833;SourceNR-ARFC... |
| 2024-09-20 22:21:38.685 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.695 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.812 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.812 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3213581 | 1 | 13.6794 | 10.3024 | -114.0040 | 15.5973 | 108.6194 | 0.0161 | 0.0189 |
| 2024_09_20 22:00 | 3225307 | 2 | 8.4637 | 19.4705 | -116.7142 | 19.1585 | 124.0861 | 0.0055 | 0.0105 |
| 2024_09_20 22:00 | 3216577 | 3 | 18.6608 | 15.7485 | -115.4122 | 8.7009 | 153.8596 | 0.0151 | 0.0184 |
| 2024_09_20 22:00 | 3278943 | 4 | 18.9344 | 9.1446 | -117.8765 | 16.6332 | 138.6088 | 0.0063 | 0.0191 |
| 2024_09_20 22:00 | 3212379 | 5 | 15.7256 | 7.4897 | -114.9286 | 13.3557 | 140.4232 | 0.0074 | 0.0121 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416007_40E12202 | 504990 | 318 | -86.1 | 504990 | 728 | -83.7 | 504990 | 907 | -87.6 | 504990 | 472 |
| MR_1774416007_A29C1AFA | 504990 | 728 | -88.1 | 504990 | 318 | -86.4 | 504990 | 907 | -88.8 | 504990 | 472 |
| MR_1774416007_C85A2852 | 504990 | 318 | -85.7 | 504990 | 728 | -85.2 | 504990 | 907 | -86.0 | 504990 | 472 |
| MR_1774416007_346C8162 | 504990 | 318 | -87.9 | 504990 | 728 | -83.1 | 504990 | 907 | -87.0 | 504990 | 472 |
| MR_1774416007_F7342703 | 504990 | 318 | -86.5 | 504990 | 728 | -86.5 | 504990 | 907 | -89.1 | 504990 | 472 |
| MR_1774416007_1A8C5DC9 | 504990 | 318 | -84.2 | 504990 | 728 | -85.0 | 504990 | 907 | -86.5 | 504990 | 472 |
| MR_1774416007_46A20DED | 504990 | 318 | -87.1 | 504990 | 728 | -85.5 | 504990 | 907 | -87.8 | 504990 | 472 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 762: `abb80e66-827...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `abb80e66-827d-49db-9927-22359f22ede8` |
| Tag | **single-answer** |
| 정답 | **C11** |
| C11 의미 | Add neighbor relationship between 3210171_1 and 3263467_2 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[762] topology](images/train_0762.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3263467_2
- `C2`: Press down the tilt angle  of 3263467_2 by 2 degrees
- `C3`: Adjust the azimuth of 3210171_1 by 11 degrees
- `C4`: Add neighbor relationship between 3269651_4 and 3263467_2
- `C5`: Decrease transmission power for 3263467_2
- `C6`: Increase transmission power for 3263467_2
- `C7`: Insufficient data; more data is needed for judgment.
- `C8`: Lift the tilt angle of 3210171_1 by 10 degrees
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3210171_1
- `C10`: Increase A3 Offset threshold for 3263467_2
- `C11`: Add neighbor relationship between 3210171_1 and 3263467_2 **← 정답**
- `C12`: Decrease A3 Offset threshold for 3263467_2
- `C13`: Increase transmission power for 3210171_1
- `C14`: Lift the tilt angle  of 3263467_2 by 2 degrees
- `C15`: Increase A3 Offset threshold for 3210171_1
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3263467_2
- `C17`: Check test server and transmission issues
- `C18`: Decrease transmission power for 3210171_1
- `C19`: Press down the tilt angle of 3210171_1 by 10 degrees
- `C20`: Decrease A3 Offset threshold for 3210171_1
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3210171_1
- `C22`: Adjust the azimuth of 3263467_2 by 23 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.309 | MS1 | 121.4656586347 | 31.1446356249 | 432 | 504990 | -83.60 | 14.91 | 531.81 | 0.13 | 2.27 | 1585 |
| 2024-09-20 22:21:32.497 | MS1 | 121.4656619002 | 31.1446264910 | 432 | 504990 | -82.85 | 14.72 | 398.39 | 0.01 | 2.29 | 1580 |
| 2024-09-20 22:21:33.179 | MS1 | 121.4656599661 | 31.1446273958 | 432 | 504990 | -80.29 | 13.21 | 465.38 | 0.18 | 2.01 | 1560 |
| 2024-09-20 22:21:34.238 | MS1 | 121.4656626782 | 31.1446269499 | 432 | 504990 | -92.77 | -3.93 | 49.37 | 0.19 | 1.40 | 1591 |
| 2024-09-20 22:21:35.521 | MS1 | 121.4656650710 | 31.1446263882 | 432 | 504990 | -85.81 | -2.02 | 32.58 | 0.06 | 1.41 | 1589 |
| 2024-09-20 22:21:36.117 | MS1 | 121.4656731495 | 31.1446305841 | 432 | 504990 | -92.29 | -0.28 | 34.30 | 0.15 | 1.43 | 1594 |
| 2024-09-20 22:21:37.429 | MS1 | 121.4656685706 | 31.1446187677 | 432 | 504990 | -94.54 | -0.99 | 38.72 | 0.15 | 1.10 | 1560 |
| 2024-09-20 22:21:38.137 | MS1 | 121.4656620969 | 31.1446307146 | 432 | 504990 | -79.69 | 13.78 | 452.68 | 0.10 | 1.22 | 1586 |
| 2024-09-20 22:21:39.491 | MS1 | 121.4656648141 | 31.1446290453 | 432 | 504990 | -80.02 | 15.86 | 463.78 | 0.05 | 1.04 | 1590 |
| 2024-09-20 22:21:40.317 | MS1 | 121.4656773552 | 31.1446345115 | 432 | 504990 | -80.51 | 15.87 | 474.34 | 0.14 | 2.17 | 1572 |
| 2024-09-20 22:21:41.811 | MS1 | 121.4656742372 | 31.1446208168 | 432 | 504990 | -79.37 | 17.60 | 470.36 | 0.06 | 2.84 | 1567 |
| 2024-09-20 22:21:42.903 | MS1 | 121.4656674468 | 31.1446255087 | 432 | 504990 | -79.63 | 17.25 | 376.94 | 0.13 | 2.27 | 1565 |

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
| 3210171 | 1 | 121.4677748688 | 31.1523553247 | 182 | 11 | 3 | 32.4 | TDD | 432 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3239216 | 3 | 121.4729971124 | 31.1447168957 | 70 | 11 | 3 | 40.0 | TDD | 306 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3263467 | 2 | 121.4750489146 | 31.1557228128 | 239 | 1 | 6 | 19.6 | TDD | 506 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3269651 | 4 | 121.4701054760 | 31.1474661171 | 48 | 2 | 3 | 25.9 | TDD | 990 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |

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
| 2024-09-20 22:21:31.495 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.512 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.616 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.616 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.368 | NREventA3 | measId:2;ServCellPCI:121;Se... |
| 2024-09-20 22:21:36.368 | NREventA3 | measId:2;ServCellPCI:121;Se... |
| 2024-09-20 22:21:37.368 | NREventA3 | measId:2;ServCellPCI:121;Se... |
| 2024-09-20 22:21:39.868 | NRRRCReestablishAttempt | PCI:121 |
| 2024-09-20 22:21:39.885 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.896 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:40.036 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:40.036 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3210171 | 1 | 8.4406 | 7.4553 | -115.4086 | 14.1137 | 157.7864 | 0.0193 | 0.1324 |
| 2024_09_20 22:00 | 3263467 | 2 | 7.2575 | 13.1540 | -117.7238 | 6.0890 | 167.8365 | 0.0056 | 0.0100 |
| 2024_09_20 22:00 | 3239216 | 3 | 19.7498 | 13.0519 | -117.7330 | 9.8709 | 163.8926 | 0.0105 | 0.0195 |
| 2024_09_20 22:00 | 3269651 | 4 | 9.5059 | 10.4111 | -116.7034 | 18.7934 | 89.0080 | 0.0182 | 0.0058 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415080_C220C62C | 504990 | 432 | -90.9 | 504990 | 506 | -87.4 | 504990 | 990 | -91.1 | 504990 | 306 |
| MR_1774415080_EE88A5DA | 504990 | 506 | -87.6 | 504990 | 432 | -93.0 | 504990 | 990 | -90.5 | 504990 | 306 |
| MR_1774415080_681D33EC | 504990 | 506 | -86.7 | 504990 | 432 | -93.7 | 504990 | 990 | -89.0 | 504990 | 306 |
| MR_1774415080_4A3BAE68 | 504990 | 506 | -87.7 | 504990 | 432 | -93.9 | 504990 | 990 | -91.1 | 504990 | 306 |
| MR_1774415080_DFBE3293 | 504990 | 432 | -94.0 | 504990 | 506 | -85.1 | 504990 | 990 | -89.5 | 504990 | 306 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 763: `308d192c-7de...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `308d192c-7de9-4f20-94bc-dd25a7ad5a6f` |
| Tag | **single-answer** |
| 정답 | **C6** |
| C6 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3279872_2 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[763] topology](images/train_0763.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3257339_1
- `C2`: Increase A3 Offset threshold for 3257339_1
- `C3`: Adjust the azimuth of 3279872_2 by 1 degrees
- `C4`: Press down the tilt angle of 3279872_2 by 3 degrees
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3279872_2
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3279872_2 **← 정답**
- `C7`: Insufficient data; more data is needed for judgment.
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3257339_1
- `C9`: Decrease transmission power for 3279872_2
- `C10`: Decrease A3 Offset threshold for 3279872_2
- `C11`: Increase transmission power for 3279872_2
- `C12`: Add neighbor relationship between 3279872_2 and 3257339_1
- `C13`: Increase A3 Offset threshold for 3279872_2
- `C14`: Add neighbor relationship between 3255276_3 and 3257339_1
- `C15`: Decrease transmission power for 3257339_1
- `C16`: Press down the tilt angle  of 3257339_1 by 3 degrees
- `C17`: Decrease A3 Offset threshold for 3257339_1
- `C18`: Lift the tilt angle of 3279872_2 by 3 degrees
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3257339_1
- `C20`: Lift the tilt angle  of 3257339_1 by 3 degrees
- `C21`: Check test server and transmission issues
- `C22`: Adjust the azimuth of 3257339_1 by 50 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.519 | MS1 | 121.4656611114 | 31.1446181921 | 260 | 504990 | -89.09 | 15.93 | 589.41 | 0.13 | 2.10 | 1592 |
| 2024-09-20 22:21:32.448 | MS1 | 121.4656605035 | 31.1446202338 | 260 | 504990 | -87.83 | 13.10 | 465.16 | 0.00 | 2.63 | 1591 |
| 2024-09-20 22:21:33.313 | MS1 | 121.4656653246 | 31.1446288370 | 260 | 504990 | -87.49 | 16.13 | 538.34 | 0.04 | 2.22 | 1566 |
| 2024-09-20 22:21:34.937 | MS1 | 121.4656670220 | 31.1446274815 | 260 | 504990 | -88.75 | 12.41 | 55.63 | 0.58 | 2.30 | 666 |
| 2024-09-20 22:21:35.847 | MS1 | 121.4656703910 | 31.1446308585 | 260 | 504990 | -86.19 | 14.47 | 64.85 | 0.64 | 2.12 | 529 |
| 2024-09-20 22:21:36.842 | MS1 | 121.4656656564 | 31.1446199750 | 260 | 504990 | -86.14 | 12.18 | 81.49 | 0.61 | 2.17 | 585 |
| 2024-09-20 22:21:37.683 | MS1 | 121.4656748275 | 31.1446333686 | 260 | 504990 | -89.92 | 12.28 | 81.52 | 0.69 | 2.03 | 684 |
| 2024-09-20 22:21:38.198 | MS1 | 121.4656604472 | 31.1446366726 | 260 | 504990 | -93.59 | 9.05 | 65.59 | 0.60 | 2.60 | 664 |
| 2024-09-20 22:21:39.616 | MS1 | 121.4656771544 | 31.1446298523 | 260 | 504990 | -92.71 | 10.15 | 94.98 | 0.61 | 2.06 | 614 |
| 2024-09-20 22:21:40.890 | MS1 | 121.4656617338 | 31.1446243219 | 260 | 504990 | -92.71 | 12.30 | 323.17 | 0.06 | 2.45 | 1571 |
| 2024-09-20 22:21:41.774 | MS1 | 121.4656606814 | 31.1446252955 | 260 | 504990 | -92.66 | 7.75 | 517.32 | 0.20 | 2.07 | 1565 |
| 2024-09-20 22:21:42.907 | MS1 | 121.4656778044 | 31.1446295046 | 260 | 504990 | -92.64 | 7.32 | 447.44 | 0.16 | 2.05 | 1575 |

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
| 3253801 | 4 | 121.4697973933 | 31.1555427825 | 217 | 15 | 1 | 36.5 | TDD | 758 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3255276 | 3 | 121.4671852560 | 31.1500828853 | 77 | 7 | 6 | 35.1 | TDD | 117 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3257339 | 1 | 121.4652229123 | 31.1530000076 | 2 | 2 | 1 | 24.2 | TDD | 193 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3279872 | 2 | 121.4709016839 | 31.1482005508 | 230 | 1 | 9 | 25.4 | TDD | 260 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

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
| 2024-09-20 22:21:31.517 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.539 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.658 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.658 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.344 | NREventA3 | measId:2;ServCellPCI:169;Se... |
| 2024-09-20 22:21:38.584 | NRHandoverAttempt | SourcePCI:169;SourceNR-ARFC... |
| 2024-09-20 22:21:38.618 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.630 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.742 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.742 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3257339 | 1 | 11.2846 | 14.1567 | -116.1779 | 14.0065 | 89.5404 | 0.0032 | 0.0045 |
| 2024_09_20 22:00 | 3279872 | 2 | 16.5283 | 14.7536 | -117.3020 | 12.5243 | 82.8238 | 0.0077 | 0.0196 |
| 2024_09_20 22:00 | 3255276 | 3 | 17.2860 | 16.7946 | -114.9950 | 16.4470 | 131.8942 | 0.0017 | 0.0092 |
| 2024_09_20 22:00 | 3253801 | 4 | 13.0832 | 10.1787 | -114.1784 | 19.1239 | 120.2024 | 0.0037 | 0.0056 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413589_81E43E54 | 504990 | 260 | -87.0 | 504990 | 193 | -90.0 | 504990 | 117 | -100.2 | 504990 | 758 |
| MR_1774413589_3769935E | 504990 | 260 | -87.4 | 504990 | 193 | -90.5 | 504990 | 117 | -102.4 | 504990 | 758 |
| MR_1774413589_F7F346C0 | 504990 | 260 | -88.7 | 504990 | 193 | -91.9 | 504990 | 117 | -103.5 | 504990 | 758 |
| MR_1774413589_ECEAC0D7 | 504990 | 260 | -89.5 | 504990 | 193 | -90.7 | 504990 | 117 | -101.1 | 504990 | 758 |
| MR_1774413589_684D3AF4 | 504990 | 260 | -86.9 | 504990 | 193 | -88.3 | 504990 | 117 | -102.7 | 504990 | 758 |
| MR_1774413589_91477B09 | 504990 | 260 | -89.6 | 504990 | 193 | -91.9 | 504990 | 117 | -102.4 | 504990 | 758 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 764: `d6c4aa62-ef0...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `d6c4aa62-ef07-4794-af1b-980f0f5c585b` |
| Tag | **multiple-answer** |
| 정답 | **C10|C19** |
| C10 의미 | Adjust the azimuth of 3217264_1 by 50 degrees |
| C19 의미 | Increase transmission power for 3217264_1 |
| 패턴 분류 | **P4 Coverage (azimuth)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[764] topology](images/train_0764.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3217264_1
- `C2`: Check test server and transmission issues
- `C3`: Decrease A3 Offset threshold for 3237565_3
- `C4`: Press down the tilt angle of 3217264_1 by 9 degrees
- `C5`: Decrease transmission power for 3217264_1
- `C6`: Insufficient data; more data is needed for judgment.
- `C7`: Increase transmission power for 3237565_3
- `C8`: Press down the tilt angle  of 3237565_3 by 4 degrees
- `C9`: Lift the tilt angle  of 3237565_3 by 4 degrees
- `C10`: Adjust the azimuth of 3217264_1 by 50 degrees **← 정답**
- `C11`: Add neighbor relationship between 3217264_1 and 3237565_3
- `C12`: Lift the tilt angle of 3217264_1 by 9 degrees
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3237565_3
- `C14`: Add neighbor relationship between 3241841_4 and 3237565_3
- `C15`: Decrease A3 Offset threshold for 3217264_1
- `C16`: Increase A3 Offset threshold for 3217264_1
- `C17`: Decrease transmission power for 3237565_3
- `C18`: Adjust the azimuth of 3237565_3 by 8 degrees
- `C19`: Increase transmission power for 3217264_1 **← 정답**
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3237565_3
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3217264_1
- `C22`: Increase A3 Offset threshold for 3237565_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.236 | MS1 | 121.4656625964 | 31.1446224162 | 961 | 504990 | -86.45 | 15.55 | 489.16 | 0.16 | 2.86 | 1589 |
| 2024-09-20 22:21:32.440 | MS1 | 121.4656589122 | 31.1446225027 | 961 | 504990 | -92.56 | 13.66 | 378.12 | 0.18 | 2.88 | 1562 |
| 2024-09-20 22:21:33.394 | MS1 | 121.4656731031 | 31.1446320305 | 961 | 504990 | -94.27 | 16.48 | 344.01 | 0.08 | 2.60 | 1580 |
| 2024-09-20 22:21:34.254 | MS1 | 121.4656682964 | 31.1446333957 | 961 | 504990 | -101.59 | -0.74 | 52.83 | 0.06 | 1.24 | 1568 |
| 2024-09-20 22:21:35.123 | MS1 | 121.4656582301 | 31.1446321411 | 961 | 504990 | -100.00 | -0.57 | 53.38 | 0.06 | 1.13 | 1584 |
| 2024-09-20 22:21:36.177 | MS1 | 121.4656728176 | 31.1446345896 | 961 | 504990 | -108.36 | 0.13 | 21.76 | 0.19 | 1.25 | 1598 |
| 2024-09-20 22:21:37.240 | MS1 | 121.4656769302 | 31.1446208445 | 961 | 504990 | -103.88 | -0.69 | 53.63 | 0.03 | 1.42 | 1574 |
| 2024-09-20 22:21:38.162 | MS1 | 121.4656720224 | 31.1446313695 | 961 | 504990 | -100.79 | -0.65 | 83.46 | 0.05 | 1.40 | 1593 |
| 2024-09-20 22:21:39.433 | MS1 | 121.4656590933 | 31.1446293043 | 961 | 504990 | -104.39 | -1.57 | 52.03 | 0.06 | 1.11 | 1593 |
| 2024-09-20 22:21:40.343 | MS1 | 121.4656748572 | 31.1446269251 | 961 | 504990 | -93.64 | 15.97 | 365.79 | 0.17 | 2.27 | 1589 |
| 2024-09-20 22:21:41.357 | MS1 | 121.4656649257 | 31.1446298201 | 961 | 504990 | -94.52 | 17.27 | 400.05 | 0.06 | 2.82 | 1572 |
| 2024-09-20 22:21:42.973 | MS1 | 121.4656631408 | 31.1446280521 | 961 | 504990 | -94.75 | 16.44 | 500.73 | 0.02 | 2.14 | 1563 |

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
| 3217264 | 1 | 121.4660006063 | 31.1552753167 | 117 | 8 | 7 | 26.0 | TDD | 961 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3237565 | 3 | 121.4756850767 | 31.1496224913 | 248 | 2 | 4 | 30.9 | TDD | 430 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3241841 | 4 | 121.4703710981 | 31.1519719345 | 289 | 4 | 10 | 30.4 | TDD | 606 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3271603 | 2 | 121.4750592194 | 31.1502399707 | 284 | 10 | 10 | 24.4 | TDD | 915 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:31.191 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.208 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.337 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.337 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.585 | NREventA2 | measId:1;ServCellPCI:788;Se... |
| 2024-09-20 22:21:34.717 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3217264 | 1 | 18.9411 | 11.3819 | -115.0069 | 14.1762 | 131.0286 | 0.1738 | 0.0029 |
| 2024_09_20 22:00 | 3271603 | 2 | 11.6306 | 15.1981 | -117.9937 | 12.6631 | 137.0589 | 0.0137 | 0.0183 |
| 2024_09_20 22:00 | 3237565 | 3 | 17.8109 | 14.1033 | -115.3894 | 12.4927 | 95.9692 | 0.0195 | 0.0015 |
| 2024_09_20 22:00 | 3241841 | 4 | 19.9881 | 18.9850 | -114.9303 | 17.3971 | 149.6339 | 0.0113 | 0.0085 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415193_6EDEBBE1 | 504990 | 961 | -100.3 | 504990 | 430 | -108.2 | 504990 | 606 | -116.4 | 504990 | 915 |
| MR_1774415193_B39D0DF5 | 504990 | 961 | -99.9 | 504990 | 430 | -106.1 | 504990 | 606 | -114.2 | 504990 | 915 |
| MR_1774415193_1205F30D | 504990 | 961 | -100.3 | 504990 | 430 | -107.2 | 504990 | 606 | -116.4 | 504990 | 915 |
| MR_1774415193_17C3B09F | 504990 | 961 | -101.5 | 504990 | 430 | -108.5 | 504990 | 606 | -116.1 | 504990 | 915 |
| MR_1774415193_0C3E919F | 504990 | 961 | -100.0 | 504990 | 430 | -107.5 | 504990 | 606 | -113.9 | 504990 | 915 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 765: `9c022d66-ca4...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `9c022d66-ca43-438d-8b89-a432cfe0d058` |
| Tag | **single-answer** |
| 정답 | **C12** |
| C12 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[765] topology](images/train_0765.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3265935_1 and 3251556_3
- `C2`: Adjust the azimuth of 3275411_2 by 42 degrees
- `C3`: Increase A3 Offset threshold for 3251556_3
- `C4`: Decrease A3 Offset threshold for 3275411_2
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3251556_3
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3275411_2
- `C7`: Increase transmission power for 3275411_2
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3275411_2
- `C9`: Press down the tilt angle  of 3251556_3 by 10 degrees
- `C10`: Adjust the azimuth of 3251556_3 by 50 degrees
- `C11`: Decrease A3 Offset threshold for 3251556_3
- `C12`: Insufficient data; more data is needed for judgment. **← 정답**
- `C13`: Lift the tilt angle  of 3251556_3 by 10 degrees
- `C14`: Add neighbor relationship between 3275411_2 and 3251556_3
- `C15`: Decrease transmission power for 3275411_2
- `C16`: Increase transmission power for 3251556_3
- `C17`: Check test server and transmission issues
- `C18`: Lift the tilt angle of 3275411_2 by 10 degrees
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3251556_3
- `C20`: Increase A3 Offset threshold for 3275411_2
- `C21`: Press down the tilt angle of 3275411_2 by 10 degrees
- `C22`: Decrease transmission power for 3251556_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.870 | MS1 | 121.4656759589 | 31.1446354621 | 794 | 504990 | -90.60 | 14.40 | 381.68 | 0.07 | 2.35 | 1584 |
| 2024-09-20 22:21:32.456 | MS1 | 121.4656607552 | 31.1446372701 | 794 | 504990 | -87.86 | 16.07 | 431.73 | 0.13 | 2.61 | 1586 |
| 2024-09-20 22:21:33.229 | MS1 | 121.4656773246 | 31.1446358657 | 794 | 504990 | -89.91 | 15.87 | 547.85 | 0.07 | 2.03 | 1569 |
| 2024-09-20 22:21:34.208 | MS1 | 121.4656669529 | 31.1446371375 | 794 | 504990 | -86.20 | 12.11 | 64.83 | 0.03 | 2.17 | 1588 |
| 2024-09-20 22:21:35.208 | MS1 | 121.4656752107 | 31.1446218427 | 794 | 504990 | -89.22 | 16.85 | 58.65 | 0.17 | 2.68 | 1577 |
| 2024-09-20 22:21:36.649 | MS1 | 121.4656589968 | 31.1446378949 | 794 | 504990 | -88.75 | 13.95 | 87.78 | 0.11 | 2.30 | 1593 |
| 2024-09-20 22:21:37.277 | MS1 | 121.4656757291 | 31.1446379105 | 794 | 504990 | -92.49 | 9.50 | 88.56 | 0.05 | 2.65 | 1571 |
| 2024-09-20 22:21:38.676 | MS1 | 121.4656750218 | 31.1446371350 | 794 | 504990 | -92.36 | 9.61 | 77.91 | 0.12 | 2.74 | 1575 |
| 2024-09-20 22:21:39.523 | MS1 | 121.4656658100 | 31.1446352604 | 794 | 504990 | -93.20 | 7.90 | 50.40 | 0.10 | 2.26 | 1572 |
| 2024-09-20 22:21:40.219 | MS1 | 121.4656739738 | 31.1446336228 | 794 | 504990 | -93.50 | 8.39 | 456.61 | 0.14 | 2.27 | 1561 |
| 2024-09-20 22:21:41.129 | MS1 | 121.4656632025 | 31.1446197419 | 794 | 504990 | -90.70 | 7.73 | 588.23 | 0.00 | 2.79 | 1584 |
| 2024-09-20 22:21:42.238 | MS1 | 121.4656611794 | 31.1446207050 | 794 | 504990 | -93.88 | 7.94 | 551.50 | 0.17 | 2.16 | 1594 |

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
| 3251556 | 3 | 121.4677894032 | 31.1530744858 | 359 | 13 | 8 | 15.2 | TDD | 107 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3254277 | 4 | 121.4703595935 | 31.1449881713 | 21 | 7 | 0 | 35.9 | TDD | 780 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3265935 | 1 | 121.4675520317 | 31.1541276653 | 274 | 9 | 2 | 44.7 | TDD | 456 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3275411 | 2 | 121.4690877070 | 31.1514177914 | 161 | 10 | 2 | 33.4 | TDD | 794 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |

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
| 2024-09-20 22:21:31.298 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.313 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.452 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.452 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.131 | NREventA3 | measId:2;ServCellPCI:928;Se... |
| 2024-09-20 22:21:38.371 | NRHandoverAttempt | SourcePCI:928;SourceNR-ARFC... |
| 2024-09-20 22:21:38.409 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.421 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.547 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.547 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3265935 | 1 | 79.3922 | 84.8225 | -116.6555 | 14.5910 | 83.9694 | 0.0032 | 0.0011 |
| 2024_09_19 22:00 | 3275411 | 2 | 90.9529 | 86.1600 | -117.5633 | 18.0691 | 162.0121 | 0.0120 | 0.0002 |
| 2024_09_19 22:00 | 3251556 | 3 | 75.6238 | 93.5449 | -115.5304 | 11.8504 | 108.2779 | 0.0149 | 0.0126 |
| 2024_09_19 22:00 | 3254277 | 4 | 81.5794 | 90.4811 | -115.3598 | 15.4953 | 153.9959 | 0.0034 | 0.0036 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412310_44ABB0E0 | 504990 | 794 | -87.5 | 504990 | 107 | -92.7 | 504990 | 456 | -93.5 | 504990 | 780 |
| MR_1774412310_3E5C9C9D | 504990 | 794 | -84.8 | 504990 | 107 | -95.1 | 504990 | 456 | -93.0 | 504990 | 780 |
| MR_1774412310_B0407254 | 504990 | 794 | -87.1 | 504990 | 107 | -92.4 | 504990 | 456 | -95.0 | 504990 | 780 |
| MR_1774412310_28857594 | 504990 | 794 | -85.0 | 504990 | 107 | -94.1 | 504990 | 456 | -94.9 | 504990 | 780 |
| MR_1774412310_32814213 | 504990 | 794 | -87.9 | 504990 | 107 | -92.3 | 504990 | 456 | -93.4 | 504990 | 780 |
| MR_1774412310_C294A013 | 504990 | 794 | -87.4 | 504990 | 107 | -94.5 | 504990 | 456 | -95.7 | 504990 | 780 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 766: `91959b19-78b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `91959b19-78b5-41f2-b17c-4446082773c3` |
| Tag | **single-answer** |
| 정답 | **C14** |
| C14 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3260590_2 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[766] topology](images/train_0766.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3276940_6
- `C2`: Add neighbor relationship between 3260590_2 and 3276940_6
- `C3`: Decrease A3 Offset threshold for 3260590_2
- `C4`: Increase A3 Offset threshold for 3260590_2
- `C5`: Press down the tilt angle  of 3276940_6 by 6 degrees
- `C6`: Decrease transmission power for 3260590_2
- `C7`: Increase transmission power for 3276940_6
- `C8`: Increase A3 Offset threshold for 3276940_6
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3276940_6
- `C10`: Decrease transmission power for 3276940_6
- `C11`: Increase transmission power for 3260590_2
- `C12`: Insufficient data; more data is needed for judgment.
- `C13`: Adjust the azimuth of 3260590_2 by 29 degrees
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3260590_2 **← 정답**
- `C15`: Add neighbor relationship between 3276316_8 and 3276940_6
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3260590_2
- `C17`: Decrease A3 Offset threshold for 3276940_6
- `C18`: Adjust the azimuth of 3276940_6 by 2 degrees
- `C19`: Press down the tilt angle of 3260590_2 by 2 degrees
- `C20`: Lift the tilt angle of 3260590_2 by 2 degrees
- `C21`: Check test server and transmission issues
- `C22`: Lift the tilt angle  of 3276940_6 by 6 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.433 | MS1 | 121.4656638590 | 31.1446224976 | 39 | 504990 | -93.65 | 9.18 | 519.88 | 0.12 | 2.02 | 1600 |
| 2024-09-20 22:21:32.284 | MS1 | 121.4656602391 | 31.1446207289 | 715 | 504990 | -95.89 | 12.35 | 367.33 | 0.14 | 2.76 | 1584 |
| 2024-09-20 22:21:33.607 | MS1 | 121.4656724190 | 31.1446345370 | 413 | 504990 | -94.68 | 12.94 | 356.59 | 0.13 | 2.27 | 1560 |
| 2024-09-20 22:21:34.300 | MS1 | 121.4656723434 | 31.1446187753 | 188 | 152650 | -87.49 | 5.62 | 71.00 | 0.01 | 1.88 | 911 |
| 2024-09-20 22:21:35.699 | MS1 | 121.4656642229 | 31.1446289119 | 383 | 152650 | -95.42 | 3.97 | 95.55 | 0.02 | 1.75 | 948 |
| 2024-09-20 22:21:36.486 | MS1 | 121.4656746222 | 31.1446195771 | 468 | 152650 | -89.74 | 6.18 | 47.72 | 0.16 | 1.86 | 958 |
| 2024-09-20 22:21:37.932 | MS1 | 121.4656700360 | 31.1446302087 | 284 | 152650 | -96.24 | 6.99 | 57.57 | 0.01 | 1.69 | 987 |
| 2024-09-20 22:21:38.671 | MS1 | 121.4656720903 | 31.1446223394 | 188 | 152650 | -91.65 | 3.21 | 69.89 | 0.13 | 1.79 | 904 |
| 2024-09-20 22:21:39.712 | MS1 | 121.4656636755 | 31.1446264152 | 383 | 152650 | -88.89 | 2.13 | 93.87 | 0.13 | 1.87 | 911 |
| 2024-09-20 22:21:40.842 | MS1 | 121.4656581809 | 31.1446185410 | 468 | 152650 | -94.03 | 7.93 | 93.97 | 0.06 | 2.77 | 1570 |
| 2024-09-20 22:21:41.929 | MS1 | 121.4656588219 | 31.1446240581 | 284 | 152650 | -91.94 | 5.75 | 79.11 | 0.17 | 2.01 | 1569 |
| 2024-09-20 22:21:42.584 | MS1 | 121.4656632033 | 31.1446292337 | 188 | 152650 | -96.46 | 6.83 | 84.97 | 0.19 | 2.27 | 1594 |

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
| 3215711 | 12 | 121.4747201652 | 31.1441533854 | 78 | 15 | 4 | 18.3 | FDD | 830 | n1 | 152650 | 30M | 4T4R | 23 | 152650 |
| 3220259 | 5 | 121.4754568764 | 31.1527063657 | 321 | 13 | 9 | 21.4 | TDD | 413 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3223012 | 13 | 121.4680922017 | 31.1551996424 | 107 | 6 | 12 | 29.3 | FDD | 383 | n1 | 152650 | 30M | 4T4R | 21 | 152650 |
| 3232507 | 3 | 121.4720240839 | 31.1446234140 | 260 | 7 | 6 | 12.8 | TDD | 715 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3235538 | 7 | 121.4724623092 | 31.1477526225 | 47 | 5 | 0 | 16.9 | FDD | 659 | n1 | 152650 | 30M | 4T4R | 20 | 152650 |
| 3239513 | 1 | 121.4681851282 | 31.1499417624 | 161 | 9 | 10 | 19.1 | TDD | 451 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3250781 | 10 | 121.4707826097 | 31.1467192245 | 329 | 13 | 4 | 3.8 | FDD | 379 | n1 | 152650 | 30M | 4T4R | 22 | 152650 |
| 3257168 | 4 | 121.4759313525 | 31.1555369053 | 76 | 4 | 4 | 5.3 | TDD | 911 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3260590 | 2 | 121.4708722494 | 31.1535018466 | 178 | 1 | 3 | 20.5 | TDD | 39 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3266553 | 9 | 121.4677746455 | 31.1464394037 | 106 | 12 | 0 | 14.0 | FDD | 284 | n1 | 152650 | 30M | 4T4R | 28 | 152650 |
| 3272868 | 11 | 121.4753973014 | 31.1447674088 | 155 | 14 | 8 | 22.5 | FDD | 188 | n1 | 152650 | 30M | 4T4R | 18 | 152650 |
| 3276316 | 8 | 121.4743604508 | 31.1449815543 | 262 | 11 | 11 | 2.0 | FDD | 468 | n1 | 152650 | 30M | 4T4R | 19 | 152650 |
| 3276940 | 6 | 121.4673324150 | 31.1519740401 | 189 | 5 | 0 | 14.0 | TDD | 894 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |

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
| 2024-09-20 22:21:31.614 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.637 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.779 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.779 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.499 | NREventA2 | measId:1;ServCellPCI:480;Se... |
| 2024-09-20 22:21:35.615 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.845 | NREventA5 | measId:3;ServCellPCI:480;Se... |
| 2024-09-20 22:21:35.915 | NRHandoverAttempt | SourcePCI:480;SourceNR-ARFC... |
| 2024-09-20 22:21:35.943 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.954 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:36.074 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.074 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3239513 | 1 | 11.0714 | 18.4542 | -116.8321 | 18.2470 | 135.3252 | 0.0141 | 0.0166 |
| 2024_09_20 22:00 | 3260590 | 2 | 8.3113 | 12.1518 | -116.7799 | 13.1009 | 109.7983 | 0.0017 | 0.0080 |
| 2024_09_20 22:00 | 3232507 | 3 | 16.2446 | 14.6709 | -117.8092 | 10.2182 | 128.1737 | 0.0004 | 0.0104 |
| 2024_09_20 22:00 | 3257168 | 4 | 17.9147 | 12.9724 | -116.1962 | 16.6265 | 136.2044 | 0.0145 | 0.0009 |
| 2024_09_20 22:00 | 3220259 | 5 | 13.1579 | 9.1934 | -117.4052 | 15.9821 | 84.1803 | 0.0092 | 0.0018 |
| 2024_09_20 22:00 | 3276940 | 6 | 18.6904 | 9.6303 | -116.2692 | 15.4489 | 119.4094 | 0.0105 | 0.0168 |
| 2024_09_20 22:00 | 3235538 | 7 | 14.1501 | 13.1293 | -114.6463 | 4.4128 | 29.5685 | 0.0130 | 0.0056 |
| 2024_09_20 22:00 | 3276316 | 8 | 12.8882 | 11.5929 | -117.3497 | 4.1364 | 57.2772 | 0.0167 | 0.0171 |
| 2024_09_20 22:00 | 3266553 | 9 | 14.8832 | 14.7523 | -117.8529 | 3.2429 | 52.3529 | 0.0127 | 0.0022 |
| 2024_09_20 22:00 | 3250781 | 10 | 6.9053 | 14.4651 | -116.5402 | 3.5062 | 47.3391 | 0.0005 | 0.0117 |
| 2024_09_20 22:00 | 3272868 | 11 | 9.3447 | 15.8531 | -117.0538 | 3.6110 | 33.7448 | 0.0120 | 0.0051 |
| 2024_09_20 22:00 | 3215711 | 12 | 10.6874 | 8.1930 | -115.6333 | 3.7501 | 41.9014 | 0.0178 | 0.0076 |
| 2024_09_20 22:00 | 3223012 | 13 | 5.2274 | 17.0543 | -117.0527 | 3.9703 | 47.6514 | 0.0133 | 0.0052 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415648_F939EA33 | 504990 | 413 | -96.0 | 504990 | 894 | -88.9 | 504990 | 451 | -99.6 | 504990 | 911 |
| MR_1774415648_73476B57 | 504990 | 413 | -93.2 | 504990 | 894 | -89.5 | 504990 | 451 | -98.5 | 504990 | 911 |
| MR_1774415648_4C230BE8 | 504990 | 413 | -93.5 | 504990 | 894 | -89.7 | 504990 | 451 | -98.0 | 504990 | 911 |
| MR_1774415648_678C79F3 | 152650 | 188 | -88.1 | 152650 | 659 | -91.5 | 152650 | 830 | -93.3 | 152650 | 379 |
| MR_1774415648_88090C27 | 504990 | 413 | -96.6 | 504990 | 894 | -91.1 | 504990 | 451 | -99.2 | 504990 | 911 |
| MR_1774415648_2BC707DE | 504990 | 413 | -96.3 | 504990 | 894 | -91.5 | 504990 | 451 | -99.6 | 504990 | 911 |
| MR_1774415648_2E5EB2A1 | 504990 | 413 | -96.4 | 504990 | 894 | -92.0 | 504990 | 451 | -98.8 | 504990 | 911 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 767: `8a6b55b7-fc6...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `8a6b55b7-fc6e-486e-9313-5b4f16179f36` |
| Tag | **single-answer** |
| 정답 | **C12** |
| C12 의미 | Decrease A3 Offset threshold for 3247737_1 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[767] topology](images/train_0767.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3247104_3
- `C2`: Adjust the azimuth of 3247104_3 by 12 degrees
- `C3`: Decrease A3 Offset threshold for 3247104_3
- `C4`: Adjust the azimuth of 3247737_1 by 10 degrees
- `C5`: Increase transmission power for 3247737_1
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3247104_3
- `C7`: Lift the tilt angle of 3247737_1 by 4 degrees
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3247737_1
- `C9`: Lift the tilt angle  of 3247104_3 by 9 degrees
- `C10`: Increase transmission power for 3247104_3
- `C11`: Add neighbor relationship between 3213472_2 and 3247104_3
- `C12`: Decrease A3 Offset threshold for 3247737_1 **← 정답**
- `C13`: Press down the tilt angle  of 3247104_3 by 9 degrees
- `C14`: Decrease transmission power for 3247104_3
- `C15`: Decrease transmission power for 3247737_1
- `C16`: Check test server and transmission issues
- `C17`: Increase A3 Offset threshold for 3247737_1
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3247737_1
- `C19`: Increase A3 Offset threshold for 3247104_3
- `C20`: Insufficient data; more data is needed for judgment.
- `C21`: Press down the tilt angle of 3247737_1 by 4 degrees
- `C22`: Add neighbor relationship between 3247737_1 and 3247104_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.169 | MS1 | 121.4656660105 | 31.1446225670 | 344 | 504990 | -78.41 | 15.06 | 513.62 | 0.19 | 2.56 | 1597 |
| 2024-09-20 22:21:32.454 | MS1 | 121.4656698705 | 31.1446302061 | 344 | 504990 | -83.66 | 13.83 | 487.90 | 0.01 | 2.06 | 1600 |
| 2024-09-20 22:21:33.562 | MS1 | 121.4656648280 | 31.1446341384 | 344 | 504990 | -80.43 | 16.99 | 518.54 | 0.09 | 2.94 | 1575 |
| 2024-09-20 22:21:34.605 | MS1 | 121.4656698583 | 31.1446268698 | 344 | 504990 | -92.29 | -0.65 | 64.21 | 0.14 | 1.27 | 1563 |
| 2024-09-20 22:21:35.526 | MS1 | 121.4656654134 | 31.1446273885 | 344 | 504990 | -92.56 | -2.56 | 48.81 | 0.12 | 1.30 | 1592 |
| 2024-09-20 22:21:36.829 | MS1 | 121.4656624803 | 31.1446186195 | 344 | 504990 | -89.11 | -3.00 | 45.70 | 0.20 | 1.05 | 1593 |
| 2024-09-20 22:21:37.267 | MS1 | 121.4656619565 | 31.1446271827 | 344 | 504990 | -91.02 | -1.77 | 63.45 | 0.01 | 1.23 | 1570 |
| 2024-09-20 22:21:38.200 | MS1 | 121.4656739560 | 31.1446345900 | 344 | 504990 | -84.02 | -2.48 | 49.40 | 0.12 | 1.24 | 1584 |
| 2024-09-20 22:21:39.360 | MS1 | 121.4656747241 | 31.1446222791 | 866 | 504990 | -77.45 | 17.12 | 289.43 | 0.19 | 1.06 | 1582 |
| 2024-09-20 22:21:40.915 | MS1 | 121.4656696306 | 31.1446340957 | 866 | 504990 | -82.33 | 12.51 | 353.12 | 0.17 | 2.17 | 1597 |
| 2024-09-20 22:21:41.608 | MS1 | 121.4656665814 | 31.1446316395 | 866 | 504990 | -83.00 | 14.75 | 545.66 | 0.15 | 2.04 | 1600 |
| 2024-09-20 22:21:42.844 | MS1 | 121.4656745860 | 31.1446298772 | 866 | 504990 | -82.10 | 17.87 | 388.84 | 0.13 | 2.01 | 1588 |

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
| 3213472 | 2 | 121.4666922139 | 31.1484417927 | 46 | 6 | 11 | 34.7 | TDD | 889 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3247104 | 3 | 121.4753343695 | 31.1446339355 | 282 | 6 | 7 | 47.5 | TDD | 866 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3247737 | 1 | 121.4654055520 | 31.1533704508 | 189 | 2 | 2 | 38.6 | TDD | 344 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3253228 | 4 | 121.4713462217 | 31.1447318317 | 180 | 4 | 0 | 46.0 | TDD | 264 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |

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
| 2024-09-20 22:21:31.097 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.112 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.254 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.254 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.925 | NREventA3 | measId:2;ServCellPCI:705;Se... |
| 2024-09-20 22:21:38.165 | NRHandoverAttempt | SourcePCI:705;SourceNR-ARFC... |
| 2024-09-20 22:21:38.210 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.225 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.373 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.373 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3247737 | 1 | 6.2637 | 14.1331 | -117.7398 | 15.0559 | 129.0451 | 0.0182 | 0.1948 |
| 2024_09_20 22:00 | 3213472 | 2 | 14.3072 | 13.8147 | -115.4613 | 8.4382 | 83.1942 | 0.0011 | 0.0097 |
| 2024_09_20 22:00 | 3247104 | 3 | 10.5057 | 6.2589 | -116.5502 | 9.3905 | 157.8029 | 0.0187 | 0.0125 |
| 2024_09_20 22:00 | 3253228 | 4 | 8.1353 | 7.2202 | -116.5322 | 14.6075 | 140.0501 | 0.0098 | 0.0187 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415190_D226EBB7 | 504990 | 344 | -91.4 | 504990 | 866 | -86.0 | 504990 | 889 | -88.6 | 504990 | 264 |
| MR_1774415190_E36F985D | 504990 | 344 | -90.7 | 504990 | 866 | -86.8 | 504990 | 889 | -88.6 | 504990 | 264 |
| MR_1774415190_476EA62F | 504990 | 866 | -86.6 | 504990 | 344 | -90.7 | 504990 | 889 | -89.7 | 504990 | 264 |
| MR_1774415190_64A2A91B | 504990 | 344 | -90.5 | 504990 | 866 | -85.8 | 504990 | 889 | -89.5 | 504990 | 264 |
| MR_1774415190_46179084 | 504990 | 866 | -86.8 | 504990 | 344 | -92.9 | 504990 | 889 | -87.7 | 504990 | 264 |
| MR_1774415190_D8D4B14F | 504990 | 866 | -83.7 | 504990 | 344 | -91.2 | 504990 | 889 | -86.1 | 504990 | 264 |
| MR_1774415190_9D549DF4 | 504990 | 344 | -93.4 | 504990 | 866 | -86.9 | 504990 | 889 | -86.3 | 504990 | 264 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 768: `857c87e0-e50...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `857c87e0-e500-4f4d-8ccf-be60ef10e297` |
| Tag | **single-answer** |
| 정답 | **C19** |
| C19 의미 | Decrease A3 Offset threshold for 3250201_1 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[768] topology](images/train_0768.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3263993_4
- `C2`: Decrease A3 Offset threshold for 3263993_4
- `C3`: Press down the tilt angle of 3250201_1 by 8 degrees
- `C4`: Add neighbor relationship between 3250201_1 and 3263993_4
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3263993_4
- `C6`: Check test server and transmission issues
- `C7`: Adjust the azimuth of 3250201_1 by 50 degrees
- `C8`: Lift the tilt angle of 3250201_1 by 8 degrees
- `C9`: Decrease transmission power for 3263993_4
- `C10`: Adjust the azimuth of 3263993_4 by 50 degrees
- `C11`: Insufficient data; more data is needed for judgment.
- `C12`: Lift the tilt angle  of 3263993_4 by 10 degrees
- `C13`: Add neighbor relationship between 3270589_2 and 3263993_4
- `C14`: Increase transmission power for 3250201_1
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3250201_1
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3263993_4
- `C17`: Press down the tilt angle  of 3263993_4 by 10 degrees
- `C18`: Increase A3 Offset threshold for 3263993_4
- `C19`: Decrease A3 Offset threshold for 3250201_1 **← 정답**
- `C20`: Decrease transmission power for 3250201_1
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3250201_1
- `C22`: Increase A3 Offset threshold for 3250201_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.896 | MS1 | 121.4656721273 | 31.1446313072 | 418 | 504990 | -84.81 | 17.50 | 595.40 | 0.10 | 2.11 | 1572 |
| 2024-09-20 22:21:32.648 | MS1 | 121.4656623197 | 31.1446346771 | 418 | 504990 | -79.63 | 14.76 | 550.50 | 0.02 | 2.29 | 1597 |
| 2024-09-20 22:21:33.618 | MS1 | 121.4656599526 | 31.1446191418 | 418 | 504990 | -78.91 | 14.66 | 504.70 | 0.09 | 2.80 | 1568 |
| 2024-09-20 22:21:34.294 | MS1 | 121.4656597426 | 31.1446208533 | 418 | 504990 | -90.09 | -1.60 | 32.59 | 0.11 | 1.47 | 1594 |
| 2024-09-20 22:21:35.758 | MS1 | 121.4656686616 | 31.1446329883 | 418 | 504990 | -92.58 | -1.83 | 80.60 | 0.09 | 1.39 | 1593 |
| 2024-09-20 22:21:36.608 | MS1 | 121.4656623672 | 31.1446372341 | 418 | 504990 | -91.66 | -0.93 | 43.25 | 0.18 | 1.37 | 1600 |
| 2024-09-20 22:21:37.711 | MS1 | 121.4656753607 | 31.1446301565 | 418 | 504990 | -92.00 | -2.78 | 43.37 | 0.14 | 1.34 | 1562 |
| 2024-09-20 22:21:38.493 | MS1 | 121.4656586010 | 31.1446300912 | 418 | 504990 | -86.50 | -2.85 | 49.38 | 0.14 | 1.08 | 1600 |
| 2024-09-20 22:21:39.403 | MS1 | 121.4656647687 | 31.1446241040 | 191 | 504990 | -78.35 | 17.91 | 233.10 | 0.12 | 1.43 | 1588 |
| 2024-09-20 22:21:40.617 | MS1 | 121.4656713563 | 31.1446230854 | 191 | 504990 | -84.04 | 16.69 | 318.16 | 0.10 | 2.43 | 1574 |
| 2024-09-20 22:21:41.889 | MS1 | 121.4656633425 | 31.1446377313 | 191 | 504990 | -82.15 | 15.12 | 514.59 | 0.19 | 2.47 | 1583 |
| 2024-09-20 22:21:42.226 | MS1 | 121.4656700495 | 31.1446213246 | 191 | 504990 | -79.15 | 13.51 | 581.19 | 0.00 | 2.28 | 1568 |

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
| 3250201 | 1 | 121.4678042478 | 31.1540793463 | 22 | 7 | 6 | 21.7 | TDD | 418 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3263104 | 3 | 121.4686165772 | 31.1442645639 | 256 | 4 | 12 | 23.2 | TDD | 357 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3263993 | 4 | 121.4717248167 | 31.1529435729 | 297 | 15 | 5 | 18.8 | TDD | 191 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3270589 | 2 | 121.4662523969 | 31.1538460445 | 261 | 5 | 0 | 16.1 | TDD | 787 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |

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
| 2024-09-20 22:21:31.466 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.490 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.615 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.615 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.317 | NREventA3 | measId:2;ServCellPCI:786;Se... |
| 2024-09-20 22:21:38.557 | NRHandoverAttempt | SourcePCI:786;SourceNR-ARFC... |
| 2024-09-20 22:21:38.592 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.605 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.743 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.743 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3250201 | 1 | 13.4419 | 19.5091 | -115.4641 | 16.1443 | 178.4269 | 0.0146 | 0.1618 |
| 2024_09_20 22:00 | 3270589 | 2 | 15.1191 | 6.0636 | -117.9024 | 15.3491 | 185.5695 | 0.0144 | 0.0150 |
| 2024_09_20 22:00 | 3263104 | 3 | 15.5600 | 8.8092 | -114.9376 | 19.5277 | 183.1336 | 0.0070 | 0.0036 |
| 2024_09_20 22:00 | 3263993 | 4 | 19.8179 | 18.0740 | -116.0428 | 17.2349 | 124.3123 | 0.0056 | 0.0070 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412719_F3F4B9A2 | 504990 | 191 | -85.1 | 504990 | 418 | -91.2 | 504990 | 787 | -89.9 | 504990 | 357 |
| MR_1774412719_6888893D | 504990 | 418 | -89.1 | 504990 | 191 | -82.8 | 504990 | 787 | -88.1 | 504990 | 357 |
| MR_1774412719_BBC7C424 | 504990 | 191 | -83.1 | 504990 | 418 | -88.7 | 504990 | 787 | -88.5 | 504990 | 357 |
| MR_1774412719_ACB94D39 | 504990 | 191 | -85.2 | 504990 | 418 | -90.4 | 504990 | 787 | -89.8 | 504990 | 357 |
| MR_1774412719_9D8EA282 | 504990 | 418 | -89.2 | 504990 | 191 | -86.4 | 504990 | 787 | -86.7 | 504990 | 357 |
| MR_1774412719_7B15D8A7 | 504990 | 191 | -84.0 | 504990 | 418 | -88.7 | 504990 | 787 | -86.9 | 504990 | 357 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 769: `f698b104-1a9...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `f698b104-1a9a-4609-9c19-ebbaf01da9ff` |
| Tag | **single-answer** |
| 정답 | **C20** |
| C20 의미 | Add neighbor relationship between 3249777_4 and 3247522_3 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[769] topology](images/train_0769.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3247522_3
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3247522_3
- `C3`: Insufficient data; more data is needed for judgment.
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3249777_4
- `C5`: Decrease A3 Offset threshold for 3249777_4
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3249777_4
- `C7`: Increase transmission power for 3247522_3
- `C8`: Adjust the azimuth of 3247522_3 by 0 degrees
- `C9`: Decrease transmission power for 3247522_3
- `C10`: Increase A3 Offset threshold for 3249777_4
- `C11`: Adjust the azimuth of 3249777_4 by 50 degrees
- `C12`: Decrease A3 Offset threshold for 3247522_3
- `C13`: Press down the tilt angle of 3249777_4 by 10 degrees
- `C14`: Press down the tilt angle  of 3247522_3 by 5 degrees
- `C15`: Decrease transmission power for 3249777_4
- `C16`: Check test server and transmission issues
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3247522_3
- `C18`: Add neighbor relationship between 3261216_1 and 3247522_3
- `C19`: Lift the tilt angle  of 3247522_3 by 5 degrees
- `C20`: Add neighbor relationship between 3249777_4 and 3247522_3 **← 정답**
- `C21`: Increase transmission power for 3249777_4
- `C22`: Lift the tilt angle of 3249777_4 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.729 | MS1 | 121.4656669726 | 31.1446270703 | 246 | 504990 | -79.36 | 16.00 | 363.19 | 0.14 | 2.85 | 1582 |
| 2024-09-20 22:21:32.672 | MS1 | 121.4656705588 | 31.1446194270 | 246 | 504990 | -81.21 | 12.47 | 439.54 | 0.16 | 2.65 | 1560 |
| 2024-09-20 22:21:33.365 | MS1 | 121.4656693716 | 31.1446272441 | 246 | 504990 | -77.53 | 15.77 | 544.05 | 0.02 | 2.18 | 1572 |
| 2024-09-20 22:21:34.383 | MS1 | 121.4656602247 | 31.1446273789 | 246 | 504990 | -94.04 | -2.46 | 34.43 | 0.04 | 1.14 | 1584 |
| 2024-09-20 22:21:35.920 | MS1 | 121.4656586167 | 31.1446307857 | 246 | 504990 | -90.39 | -0.39 | 65.69 | 0.06 | 1.23 | 1579 |
| 2024-09-20 22:21:36.915 | MS1 | 121.4656658675 | 31.1446334697 | 246 | 504990 | -93.80 | -1.72 | 43.58 | 0.14 | 1.08 | 1593 |
| 2024-09-20 22:21:37.706 | MS1 | 121.4656638414 | 31.1446284747 | 246 | 504990 | -94.46 | -2.85 | 29.57 | 0.00 | 1.19 | 1575 |
| 2024-09-20 22:21:38.446 | MS1 | 121.4656722754 | 31.1446258815 | 246 | 504990 | -81.22 | 13.01 | 471.51 | 0.10 | 1.47 | 1579 |
| 2024-09-20 22:21:39.157 | MS1 | 121.4656754233 | 31.1446299777 | 246 | 504990 | -77.89 | 13.42 | 351.55 | 0.11 | 1.22 | 1593 |
| 2024-09-20 22:21:40.410 | MS1 | 121.4656606954 | 31.1446213275 | 246 | 504990 | -79.68 | 16.20 | 390.76 | 0.07 | 2.86 | 1581 |
| 2024-09-20 22:21:41.719 | MS1 | 121.4656623878 | 31.1446187222 | 246 | 504990 | -76.38 | 13.98 | 519.91 | 0.04 | 2.95 | 1598 |
| 2024-09-20 22:21:42.344 | MS1 | 121.4656606681 | 31.1446229596 | 246 | 504990 | -83.70 | 12.48 | 333.94 | 0.20 | 2.62 | 1576 |

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
| 3210571 | 2 | 121.4724850909 | 31.1536833620 | 114 | 1 | 3 | 32.7 | TDD | 256 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3247522 | 3 | 121.4690964882 | 31.1555517693 | 195 | 3 | 5 | 39.2 | TDD | 381 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3249777 | 4 | 121.4651858697 | 31.1520826307 | 327 | 11 | 1 | 37.1 | TDD | 246 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3261216 | 1 | 121.4710933823 | 31.1442887684 | 195 | 13 | 10 | 43.7 | TDD | 88 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |

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
| 2024-09-20 22:21:31.045 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.192 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.192 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.867 | NREventA3 | measId:2;ServCellPCI:47;Ser... |
| 2024-09-20 22:21:35.867 | NREventA3 | measId:2;ServCellPCI:47;Ser... |
| 2024-09-20 22:21:36.867 | NREventA3 | measId:2;ServCellPCI:47;Ser... |
| 2024-09-20 22:21:39.367 | NRRRCReestablishAttempt | PCI:47 |
| 2024-09-20 22:21:39.378 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.392 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:39.537 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.537 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3261216 | 1 | 15.4375 | 16.8447 | -114.8641 | 15.6113 | 82.3371 | 0.0064 | 0.0199 |
| 2024_09_20 22:00 | 3210571 | 2 | 13.4153 | 19.0940 | -117.1299 | 9.2141 | 174.4845 | 0.0114 | 0.0039 |
| 2024_09_20 22:00 | 3247522 | 3 | 13.7744 | 10.1643 | -114.3781 | 17.3662 | 82.0354 | 0.0007 | 0.0036 |
| 2024_09_20 22:00 | 3249777 | 4 | 19.0515 | 19.5931 | -116.1074 | 19.1714 | 184.5499 | 0.0005 | 0.1522 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414507_9D87DF97 | 504990 | 381 | -89.1 | 504990 | 246 | -95.0 | 504990 | 88 | -89.2 | 504990 | 256 |
| MR_1774414507_1EE0DFC3 | 504990 | 246 | -94.1 | 504990 | 381 | -90.5 | 504990 | 88 | -90.5 | 504990 | 256 |
| MR_1774414507_94CE62B3 | 504990 | 246 | -95.3 | 504990 | 381 | -87.8 | 504990 | 88 | -89.1 | 504990 | 256 |
| MR_1774414507_28EDB4D0 | 504990 | 246 | -95.6 | 504990 | 381 | -88.0 | 504990 | 88 | -89.5 | 504990 | 256 |
| MR_1774414507_1D876C1A | 504990 | 246 | -95.7 | 504990 | 381 | -87.6 | 504990 | 88 | -89.0 | 504990 | 256 |
| MR_1774414507_282D3465 | 504990 | 246 | -95.5 | 504990 | 381 | -88.8 | 504990 | 88 | -88.2 | 504990 | 256 |
| MR_1774414507_BFB9ABE0 | 504990 | 246 | -93.4 | 504990 | 381 | -89.9 | 504990 | 88 | -90.6 | 504990 | 256 |
| MR_1774414507_2CD655FD | 504990 | 246 | -92.2 | 504990 | 381 | -87.6 | 504990 | 88 | -89.7 | 504990 | 256 |

> *... 2개 열 생략 (전체 14열)*

---
