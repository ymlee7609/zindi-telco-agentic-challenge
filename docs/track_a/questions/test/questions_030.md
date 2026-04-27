# Track A 문제 분석 — test[290]~test[299]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/test.json`
> 범위: test[290] ~ test[299] (10개)

## 목차

1. [문제 290: `46069693-61c...`](#290) — single-answer
2. [문제 291: `524ea0a2-1d5...`](#291) — single-answer
3. [문제 292: `0009e432-664...`](#292) — single-answer
4. [문제 293: `a97d8660-c41...`](#293) — single-answer
5. [문제 294: `72ac892b-e74...`](#294) — single-answer
6. [문제 295: `4a0d2f3d-98c...`](#295) — single-answer
7. [문제 296: `4fb1d9a6-c5d...`](#296) — single-answer
8. [문제 297: `c68566f1-996...`](#297) — single-answer
9. [문제 298: `f2e9383a-947...`](#298) — single-answer
10. [문제 299: `65a90582-b07...`](#299) — single-answer

---

### 문제 290: `46069693-61c...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `46069693-61c3-431e-84a2-c438e6be8d81` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[290] topology](images/test_0290.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3255379_4
- `C2`: Increase A3 Offset threshold for 3255379_4
- `C3`: Lift the tilt angle of 3255379_4 by 10 degrees
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3228562_1
- `C5`: Press down the tilt angle  of 3228562_1 by 10 degrees
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3255379_4
- `C7`: Decrease A3 Offset threshold for 3228562_1
- `C8`: Increase A3 Offset threshold for 3228562_1
- `C9`: Increase transmission power for 3228562_1
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3228562_1
- `C11`: Add neighbor relationship between 3255379_4 and 3228562_1
- `C12`: Adjust the azimuth of 3255379_4 by 13 degrees
- `C13`: Decrease transmission power for 3255379_4
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3255379_4
- `C15`: Check test server and transmission issues
- `C16`: Press down the tilt angle of 3255379_4 by 10 degrees
- `C17`: Adjust the azimuth of 3228562_1 by 46 degrees
- `C18`: Insufficient data; more data is needed for judgment.
- `C19`: Add neighbor relationship between 3246869_3 and 3228562_1
- `C20`: Decrease A3 Offset threshold for 3255379_4
- `C21`: Lift the tilt angle  of 3228562_1 by 10 degrees
- `C22`: Decrease transmission power for 3228562_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.312 | MS1 | 121.4656596428 | 31.1446313083 | 572 | 504990 | -91.29 | 15.16 | 350.82 | 0.09 | 2.49 | 1595 |
| 2024-09-20 22:21:32.928 | MS1 | 121.4656605265 | 31.1446212141 | 572 | 504990 | -86.38 | 14.78 | 433.09 | 0.09 | 2.68 | 1561 |
| 2024-09-20 22:21:33.967 | MS1 | 121.4656706958 | 31.1446295298 | 572 | 504990 | -87.31 | 15.22 | 440.59 | 0.01 | 2.01 | 1576 |
| 2024-09-20 22:21:34.272 | MS1 | 121.4656729939 | 31.1446258725 | 572 | 504990 | -91.88 | 15.89 | 83.23 | 0.15 | 2.57 | 494 |
| 2024-09-20 22:21:35.619 | MS1 | 121.4656749986 | 31.1446190468 | 572 | 504990 | -85.49 | 16.98 | 78.43 | 0.10 | 2.49 | 428 |
| 2024-09-20 22:21:36.181 | MS1 | 121.4656693633 | 31.1446379624 | 572 | 504990 | -89.32 | 16.87 | 50.90 | 0.01 | 2.16 | 412 |
| 2024-09-20 22:21:37.953 | MS1 | 121.4656631395 | 31.1446186476 | 572 | 504990 | -92.59 | 11.72 | 108.18 | 0.03 | 2.50 | 396 |
| 2024-09-20 22:21:38.375 | MS1 | 121.4656703227 | 31.1446224444 | 572 | 504990 | -92.47 | 7.34 | 75.08 | 0.06 | 2.08 | 394 |
| 2024-09-20 22:21:39.934 | MS1 | 121.4656606647 | 31.1446315444 | 572 | 504990 | -92.46 | 8.80 | 93.44 | 0.19 | 2.79 | 481 |
| 2024-09-20 22:21:40.327 | MS1 | 121.4656664599 | 31.1446267746 | 572 | 504990 | -90.32 | 11.49 | 478.61 | 0.09 | 2.44 | 1578 |
| 2024-09-20 22:21:41.820 | MS1 | 121.4656671882 | 31.1446347630 | 572 | 504990 | -89.28 | 9.85 | 466.90 | 0.15 | 2.13 | 1592 |
| 2024-09-20 22:21:42.401 | MS1 | 121.4656743438 | 31.1446358017 | 572 | 504990 | -93.16 | 8.76 | 466.87 | 0.02 | 2.93 | 1586 |

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
| 3228562 | 1 | 121.4697704429 | 31.1544188996 | 154 | 13 | 12 | 27.1 | TDD | 480 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3246869 | 3 | 121.4747658331 | 31.1470312199 | 79 | 6 | 9 | 48.2 | TDD | 394 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3255379 | 4 | 121.4708939586 | 31.1472057182 | 227 | 11 | 7 | 23.1 | TDD | 572 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3277673 | 2 | 121.4697624967 | 31.1548515894 | 43 | 10 | 0 | 25.0 | TDD | 793 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:31.452 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.473 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.602 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.602 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.279 | NREventA3 | measId:2;ServCellPCI:383;Se... |
| 2024-09-20 22:21:38.519 | NRHandoverAttempt | SourcePCI:383;SourceNR-ARFC... |
| 2024-09-20 22:21:38.550 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.561 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.667 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.667 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3228562 | 1 | 10.2656 | 19.8208 | -114.6310 | 18.2994 | 86.5081 | 0.0020 | 0.0178 |
| 2024_09_20 22:00 | 3277673 | 2 | 19.6410 | 17.5081 | -114.9093 | 15.8230 | 122.6443 | 0.0150 | 0.0153 |
| 2024_09_20 22:00 | 3246869 | 3 | 17.9630 | 13.3739 | -115.4413 | 9.6521 | 127.1328 | 0.0020 | 0.0137 |
| 2024_09_20 22:00 | 3255379 | 4 | 17.0926 | 11.6034 | -117.4064 | 6.5233 | 147.3994 | 0.0048 | 0.0150 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414498_84FDB98B | 504990 | 572 | -91.9 | 504990 | 480 | -98.4 | 504990 | 394 | -102.3 | 504990 | 793 |
| MR_1774414498_771E7ABA | 504990 | 572 | -93.0 | 504990 | 480 | -96.2 | 504990 | 394 | -101.5 | 504990 | 793 |
| MR_1774414498_13E3256F | 504990 | 572 | -93.7 | 504990 | 480 | -97.1 | 504990 | 394 | -102.9 | 504990 | 793 |
| MR_1774414498_49BC025D | 504990 | 572 | -93.1 | 504990 | 480 | -99.0 | 504990 | 394 | -102.2 | 504990 | 793 |
| MR_1774414498_AE8F4E45 | 504990 | 572 | -91.9 | 504990 | 480 | -97.2 | 504990 | 394 | -99.7 | 504990 | 793 |
| MR_1774414498_B2452E43 | 504990 | 572 | -92.7 | 504990 | 480 | -96.2 | 504990 | 394 | -103.0 | 504990 | 793 |
| MR_1774414498_CEB687CD | 504990 | 572 | -91.6 | 504990 | 480 | -98.1 | 504990 | 394 | -100.9 | 504990 | 793 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 291: `524ea0a2-1d5...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `524ea0a2-1d54-4e35-99f6-de96c121fcbf` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[291] topology](images/test_0291.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3277267_1 and 3235201_4
- `C2`: Press down the tilt angle  of 3235201_4 by 10 degrees
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3277267_1
- `C4`: Lift the tilt angle of 3277267_1 by 4 degrees
- `C5`: Insufficient data; more data is needed for judgment.
- `C6`: Adjust the azimuth of 3235201_4 by 50 degrees
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3235201_4
- `C8`: Add neighbor relationship between 3267448_3 and 3235201_4
- `C9`: Press down the tilt angle of 3277267_1 by 4 degrees
- `C10`: Lift the tilt angle  of 3235201_4 by 10 degrees
- `C11`: Decrease transmission power for 3277267_1
- `C12`: Decrease A3 Offset threshold for 3277267_1
- `C13`: Increase transmission power for 3235201_4
- `C14`: Decrease transmission power for 3235201_4
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3235201_4
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3277267_1
- `C17`: Increase A3 Offset threshold for 3235201_4
- `C18`: Decrease A3 Offset threshold for 3235201_4
- `C19`: Increase transmission power for 3277267_1
- `C20`: Increase A3 Offset threshold for 3277267_1
- `C21`: Check test server and transmission issues
- `C22`: Adjust the azimuth of 3277267_1 by 42 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.510 | MS1 | 121.4656634965 | 31.1446326802 | 594 | 504990 | -85.84 | 13.38 | 450.61 | 0.20 | 2.28 | 1586 |
| 2024-09-20 22:21:32.585 | MS1 | 121.4656604964 | 31.1446376289 | 594 | 504990 | -88.24 | 16.75 | 435.12 | 0.15 | 2.68 | 1588 |
| 2024-09-20 22:21:33.711 | MS1 | 121.4656707324 | 31.1446200656 | 594 | 504990 | -88.24 | 12.39 | 556.04 | 0.12 | 2.42 | 1592 |
| 2024-09-20 22:21:34.469 | MS1 | 121.4656627817 | 31.1446208634 | 594 | 504990 | -90.35 | 17.42 | 86.19 | 0.63 | 2.96 | 542 |
| 2024-09-20 22:21:35.612 | MS1 | 121.4656603926 | 31.1446232366 | 594 | 504990 | -90.93 | 12.61 | 88.80 | 0.51 | 2.86 | 583 |
| 2024-09-20 22:21:36.610 | MS1 | 121.4656680792 | 31.1446249980 | 594 | 504990 | -87.55 | 12.50 | 102.02 | 0.62 | 2.54 | 600 |
| 2024-09-20 22:21:37.485 | MS1 | 121.4656612244 | 31.1446312308 | 594 | 504990 | -92.98 | 8.74 | 100.13 | 0.59 | 2.66 | 603 |
| 2024-09-20 22:21:38.935 | MS1 | 121.4656645727 | 31.1446344576 | 594 | 504990 | -89.84 | 8.09 | 67.29 | 0.55 | 2.21 | 617 |
| 2024-09-20 22:21:39.546 | MS1 | 121.4656683050 | 31.1446294977 | 594 | 504990 | -89.37 | 8.50 | 92.48 | 0.63 | 2.62 | 528 |
| 2024-09-20 22:21:40.127 | MS1 | 121.4656679333 | 31.1446304712 | 594 | 504990 | -93.74 | 8.85 | 585.66 | 0.16 | 2.85 | 1599 |
| 2024-09-20 22:21:41.546 | MS1 | 121.4656690523 | 31.1446358075 | 594 | 504990 | -92.61 | 8.93 | 582.15 | 0.18 | 2.62 | 1585 |
| 2024-09-20 22:21:42.132 | MS1 | 121.4656597548 | 31.1446337154 | 594 | 504990 | -89.78 | 7.73 | 364.56 | 0.03 | 2.56 | 1592 |

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
| 3235201 | 4 | 121.4714014456 | 31.1453522478 | 142 | 9 | 1 | 45.5 | TDD | 613 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3267448 | 3 | 121.4689719324 | 31.1482823039 | 138 | 5 | 2 | 36.0 | TDD | 356 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3270251 | 2 | 121.4742772210 | 31.1533698626 | 339 | 14 | 12 | 39.0 | TDD | 187 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3277267 | 1 | 121.4682856346 | 31.1539237848 | 236 | 3 | 7 | 20.8 | TDD | 594 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

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
| 2024-09-20 22:21:31.610 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.634 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.749 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.749 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.487 | NREventA3 | measId:2;ServCellPCI:41;Ser... |
| 2024-09-20 22:21:38.727 | NRHandoverAttempt | SourcePCI:41;SourceNR-ARFCN... |
| 2024-09-20 22:21:38.772 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.786 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.927 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.927 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3277267 | 1 | 14.8024 | 16.1292 | -115.4208 | 5.9819 | 91.7619 | 0.0140 | 0.0060 |
| 2024_09_20 22:00 | 3270251 | 2 | 15.7960 | 6.5844 | -116.7003 | 14.5604 | 169.8676 | 0.0095 | 0.0057 |
| 2024_09_20 22:00 | 3267448 | 3 | 15.2503 | 5.4926 | -117.3360 | 10.3337 | 83.6182 | 0.0049 | 0.0007 |
| 2024_09_20 22:00 | 3235201 | 4 | 7.4091 | 7.6227 | -117.1725 | 14.5428 | 143.5242 | 0.0131 | 0.0061 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414144_25D66516 | 504990 | 594 | -89.6 | 504990 | 613 | -100.1 | 504990 | 356 | -105.3 | 504990 | 187 |
| MR_1774414144_A431B2B3 | 504990 | 594 | -88.8 | 504990 | 613 | -101.1 | 504990 | 356 | -104.9 | 504990 | 187 |
| MR_1774414144_83BE0F58 | 504990 | 594 | -91.6 | 504990 | 613 | -99.1 | 504990 | 356 | -105.8 | 504990 | 187 |
| MR_1774414144_F1A622CD | 504990 | 594 | -92.3 | 504990 | 613 | -99.3 | 504990 | 356 | -104.3 | 504990 | 187 |
| MR_1774414144_6386C696 | 504990 | 594 | -89.0 | 504990 | 613 | -99.3 | 504990 | 356 | -105.6 | 504990 | 187 |
| MR_1774414144_9623B1D8 | 504990 | 594 | -91.0 | 504990 | 613 | -98.5 | 504990 | 356 | -104.5 | 504990 | 187 |
| MR_1774414144_78448814 | 504990 | 594 | -92.3 | 504990 | 613 | -97.2 | 504990 | 356 | -104.8 | 504990 | 187 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 292: `0009e432-664...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `0009e432-6645-4f51-9de5-62c908f429e0` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[292] topology](images/test_0292.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3252048_4 by 10 degrees
- `C2`: Decrease transmission power for 3217373_1
- `C3`: Adjust the azimuth of 3252048_4 by 46 degrees
- `C4`: Increase transmission power for 3217373_1
- `C5`: Lift the tilt angle  of 3252048_4 by 10 degrees
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3252048_4
- `C7`: Decrease A3 Offset threshold for 3217373_1
- `C8`: Increase A3 Offset threshold for 3217373_1
- `C9`: Add neighbor relationship between 3217373_1 and 3252048_4
- `C10`: Increase transmission power for 3252048_4
- `C11`: Add neighbor relationship between 3249107_3 and 3252048_4
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3217373_1
- `C13`: Press down the tilt angle of 3217373_1 by 10 degrees
- `C14`: Increase A3 Offset threshold for 3252048_4
- `C15`: Insufficient data; more data is needed for judgment.
- `C16`: Decrease transmission power for 3252048_4
- `C17`: Adjust the azimuth of 3217373_1 by 50 degrees
- `C18`: Lift the tilt angle of 3217373_1 by 10 degrees
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3252048_4
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3217373_1
- `C21`: Decrease A3 Offset threshold for 3252048_4
- `C22`: Check test server and transmission issues

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.824 | MS1 | 121.4656659942 | 31.1446183629 | 968 | 504990 | -90.04 | 12.68 | 352.34 | 0.13 | 2.20 | 1567 |
| 2024-09-20 22:21:32.805 | MS1 | 121.4656763852 | 31.1446267593 | 968 | 504990 | -87.43 | 12.84 | 550.96 | 0.01 | 2.83 | 1583 |
| 2024-09-20 22:21:33.228 | MS1 | 121.4656612851 | 31.1446305102 | 968 | 504990 | -89.48 | 15.07 | 403.05 | 0.18 | 2.68 | 1585 |
| 2024-09-20 22:21:34.147 | MS1 | 121.4656770475 | 31.1446334953 | 968 | 504990 | -85.71 | 12.15 | 105.49 | 0.06 | 2.82 | 1599 |
| 2024-09-20 22:21:35.483 | MS1 | 121.4656595699 | 31.1446243647 | 968 | 504990 | -89.62 | 15.97 | 87.02 | 0.09 | 2.75 | 1581 |
| 2024-09-20 22:21:36.357 | MS1 | 121.4656692661 | 31.1446347637 | 968 | 504990 | -86.74 | 16.39 | 77.49 | 0.10 | 2.32 | 1588 |
| 2024-09-20 22:21:37.535 | MS1 | 121.4656760357 | 31.1446291620 | 968 | 504990 | -91.38 | 12.36 | 53.48 | 0.02 | 2.23 | 1572 |
| 2024-09-20 22:21:38.239 | MS1 | 121.4656736152 | 31.1446268524 | 968 | 504990 | -89.62 | 7.93 | 63.63 | 0.18 | 2.12 | 1570 |
| 2024-09-20 22:21:39.103 | MS1 | 121.4656772218 | 31.1446361427 | 968 | 504990 | -92.65 | 9.18 | 80.05 | 0.15 | 2.39 | 1596 |
| 2024-09-20 22:21:40.209 | MS1 | 121.4656776260 | 31.1446329529 | 968 | 504990 | -89.31 | 11.30 | 559.31 | 0.10 | 2.57 | 1570 |
| 2024-09-20 22:21:41.519 | MS1 | 121.4656751065 | 31.1446378094 | 968 | 504990 | -89.81 | 8.19 | 536.10 | 0.04 | 2.40 | 1571 |
| 2024-09-20 22:21:42.237 | MS1 | 121.4656637331 | 31.1446204834 | 968 | 504990 | -92.01 | 10.34 | 418.12 | 0.09 | 2.25 | 1599 |

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
| 3217373 | 1 | 121.4718490199 | 31.1507407730 | 75 | 11 | 7 | 20.5 | TDD | 968 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3249107 | 3 | 121.4729429337 | 31.1510835296 | 166 | 15 | 11 | 31.0 | TDD | 869 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3252048 | 4 | 121.4751666304 | 31.1536230705 | 176 | 11 | 1 | 29.2 | TDD | 991 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3277545 | 2 | 121.4732521866 | 31.1482114654 | 313 | 13 | 9 | 29.5 | TDD | 547 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |

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
| 2024-09-20 22:21:31.141 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.159 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.306 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.306 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.988 | NREventA3 | measId:2;ServCellPCI:467;Se... |
| 2024-09-20 22:21:38.228 | NRHandoverAttempt | SourcePCI:467;SourceNR-ARFC... |
| 2024-09-20 22:21:38.266 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.280 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.386 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.386 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3217373 | 1 | 93.3500 | 83.1760 | -117.6166 | 17.1186 | 173.1336 | 0.0019 | 0.0085 |
| 2024_09_19 22:00 | 3277545 | 2 | 75.4692 | 89.7120 | -114.5387 | 19.1816 | 148.2369 | 0.0099 | 0.0188 |
| 2024_09_19 22:00 | 3249107 | 3 | 79.5496 | 80.2112 | -117.5513 | 11.1497 | 126.2403 | 0.0190 | 0.0135 |
| 2024_09_19 22:00 | 3252048 | 4 | 77.0667 | 81.2421 | -115.8138 | 8.7709 | 174.6567 | 0.0046 | 0.0175 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413408_48592091 | 504990 | 968 | -90.6 | 504990 | 991 | -91.6 | 504990 | 869 | -95.2 | 504990 | 547 |
| MR_1774413408_61676AD1 | 504990 | 968 | -89.1 | 504990 | 991 | -91.7 | 504990 | 869 | -94.6 | 504990 | 547 |
| MR_1774413408_1D185AAA | 504990 | 968 | -88.9 | 504990 | 991 | -94.3 | 504990 | 869 | -95.3 | 504990 | 547 |
| MR_1774413408_29C551E5 | 504990 | 968 | -87.9 | 504990 | 991 | -92.3 | 504990 | 869 | -95.8 | 504990 | 547 |
| MR_1774413408_6495A9F5 | 504990 | 968 | -89.0 | 504990 | 991 | -94.5 | 504990 | 869 | -96.9 | 504990 | 547 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 293: `a97d8660-c41...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `a97d8660-c413-4e92-a159-458954fa2046` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[293] topology](images/test_0293.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3254852_2 and 3233794_3
- `C2`: Decrease A3 Offset threshold for 3254852_2
- `C3`: Add neighbor relationship between 3236402_1 and 3233794_3
- `C4`: Insufficient data; more data is needed for judgment.
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3233794_3
- `C6`: Increase A3 Offset threshold for 3254852_2
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3233794_3
- `C8`: Decrease transmission power for 3233794_3
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3254852_2
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3254852_2
- `C11`: Press down the tilt angle  of 3236402_1 by 10 degrees
- `C12`: Adjust the azimuth of 3236402_1 by 50 degrees
- `C13`: Lift the tilt angle of 3254852_2 by 4 degrees
- `C14`: Increase transmission power for 3254852_2
- `C15`: Increase A3 Offset threshold for 3233794_3
- `C16`: Press down the tilt angle of 3254852_2 by 4 degrees
- `C17`: Decrease A3 Offset threshold for 3233794_3
- `C18`: Decrease transmission power for 3254852_2
- `C19`: Adjust the azimuth of 3254852_2 by 26 degrees
- `C20`: Lift the tilt angle  of 3236402_1 by 10 degrees
- `C21`: Check test server and transmission issues
- `C22`: Increase transmission power for 3233794_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.175 | MS1 | 121.4656742471 | 31.1446249277 | 753 | 504990 | -90.96 | 17.66 | 465.99 | 0.12 | 2.74 | 1598 |
| 2024-09-20 22:21:32.412 | MS1 | 121.4656606744 | 31.1446369912 | 753 | 504990 | -89.39 | 15.81 | 531.22 | 0.07 | 2.69 | 1578 |
| 2024-09-20 22:21:33.495 | MS1 | 121.4656702785 | 31.1446273613 | 753 | 504990 | -86.96 | 17.82 | 493.36 | 0.15 | 2.27 | 1591 |
| 2024-09-20 22:21:34.496 | MS1 | 121.4656688516 | 31.1446375728 | 753 | 504990 | -89.84 | 12.55 | 83.82 | 0.16 | 2.43 | 1599 |
| 2024-09-20 22:21:35.770 | MS1 | 121.4656612471 | 31.1446274993 | 753 | 504990 | -87.83 | 16.33 | 65.15 | 0.01 | 2.80 | 1571 |
| 2024-09-20 22:21:36.756 | MS1 | 121.4656665771 | 31.1446363804 | 753 | 504990 | -89.62 | 13.29 | 89.18 | 0.02 | 2.54 | 1572 |
| 2024-09-20 22:21:37.125 | MS1 | 121.4656702501 | 31.1446318091 | 753 | 504990 | -92.01 | 8.97 | 71.89 | 0.09 | 2.18 | 1574 |
| 2024-09-20 22:21:38.455 | MS1 | 121.4656699444 | 31.1446205438 | 753 | 504990 | -91.91 | 12.88 | 70.63 | 0.10 | 2.69 | 1584 |
| 2024-09-20 22:21:39.897 | MS1 | 121.4656610358 | 31.1446226610 | 753 | 504990 | -89.84 | 10.06 | 50.76 | 0.00 | 2.58 | 1598 |
| 2024-09-20 22:21:40.669 | MS1 | 121.4656599687 | 31.1446207035 | 753 | 504990 | -90.70 | 10.92 | 450.33 | 0.15 | 2.31 | 1568 |
| 2024-09-20 22:21:41.431 | MS1 | 121.4656610941 | 31.1446353482 | 753 | 504990 | -90.79 | 9.64 | 576.17 | 0.19 | 2.19 | 1566 |
| 2024-09-20 22:21:42.809 | MS1 | 121.4656716707 | 31.1446256436 | 753 | 504990 | -92.94 | 10.50 | 426.51 | 0.08 | 2.49 | 1581 |

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
| 3224195 | 4 | 121.4641066023 | 31.1507074716 | 7 | 14 | 4 | 46.5 | TDD | 301 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3233794 | 3 | 121.4675030063 | 31.1457915989 | 118 | 6 | 12 | 34.2 | TDD | 683 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3236402 | 1 | 121.4755945947 | 31.1492281230 | 63 | 2 | 1 | 18.1 | TDD | 952 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3254852 | 2 | 121.4734383601 | 31.1481927360 | 216 | 3 | 7 | 15.4 | TDD | 753 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:31.244 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.263 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.390 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.390 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.134 | NREventA3 | measId:2;ServCellPCI:596;Se... |
| 2024-09-20 22:21:38.374 | NRHandoverAttempt | SourcePCI:596;SourceNR-ARFC... |
| 2024-09-20 22:21:38.417 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.429 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.578 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.578 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3236402 | 1 | 14.1921 | 15.5225 | -115.2045 | 5.8431 | 171.6505 | 0.0111 | 0.0078 |
| 2024_09_20 22:00 | 3254852 | 2 | 84.1069 | 92.0866 | -116.4357 | 16.9043 | 99.0621 | 0.0056 | 0.0155 |
| 2024_09_20 22:00 | 3233794 | 3 | 19.1927 | 10.8248 | -116.3782 | 14.4516 | 83.9515 | 0.0008 | 0.0043 |
| 2024_09_20 22:00 | 3224195 | 4 | 8.9257 | 17.5988 | -115.5572 | 16.7724 | 89.1519 | 0.0123 | 0.0098 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416145_0C4B0557 | 504990 | 753 | -89.2 | 504990 | 683 | -90.0 | 504990 | 952 | -99.8 | 504990 | 301 |
| MR_1774416145_52884665 | 504990 | 753 | -90.7 | 504990 | 683 | -87.4 | 504990 | 952 | -100.5 | 504990 | 301 |
| MR_1774416145_1E17DEFA | 504990 | 753 | -91.0 | 504990 | 683 | -89.0 | 504990 | 952 | -100.5 | 504990 | 301 |
| MR_1774416145_0BD73F61 | 504990 | 753 | -89.7 | 504990 | 683 | -88.5 | 504990 | 952 | -99.4 | 504990 | 301 |
| MR_1774416145_1202B28C | 504990 | 753 | -90.3 | 504990 | 683 | -89.5 | 504990 | 952 | -98.7 | 504990 | 301 |
| MR_1774416145_A04ACB90 | 504990 | 753 | -89.6 | 504990 | 683 | -90.5 | 504990 | 952 | -99.0 | 504990 | 301 |
| MR_1774416145_1884B565 | 504990 | 753 | -88.1 | 504990 | 683 | -88.2 | 504990 | 952 | -97.8 | 504990 | 301 |
| MR_1774416145_5E0CD44E | 504990 | 753 | -88.0 | 504990 | 683 | -91.2 | 504990 | 952 | -100.5 | 504990 | 301 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 294: `72ac892b-e74...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `72ac892b-e74c-4c1a-a84c-a1305865a853` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[294] topology](images/test_0294.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3238730_2 by 4 degrees
- `C2`: Increase A3 Offset threshold for 3259645_1
- `C3`: Decrease transmission power for 3259645_1
- `C4`: Increase transmission power for 3259645_1
- `C5`: Lift the tilt angle  of 3259645_1 by 2 degrees
- `C6`: Add neighbor relationship between 3238730_2 and 3259645_1
- `C7`: Insufficient data; more data is needed for judgment.
- `C8`: Add neighbor relationship between 3237566_4 and 3259645_1
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3259645_1
- `C10`: Increase transmission power for 3238730_2
- `C11`: Press down the tilt angle of 3238730_2 by 4 degrees
- `C12`: Decrease A3 Offset threshold for 3259645_1
- `C13`: Check test server and transmission issues
- `C14`: Increase A3 Offset threshold for 3238730_2
- `C15`: Press down the tilt angle  of 3259645_1 by 2 degrees
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3238730_2
- `C17`: Adjust the azimuth of 3259645_1 by 50 degrees
- `C18`: Decrease transmission power for 3238730_2
- `C19`: Adjust the azimuth of 3238730_2 by 9 degrees
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3238730_2
- `C21`: Decrease A3 Offset threshold for 3238730_2
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3259645_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.764 | MS1 | 121.4656674699 | 31.1446341270 | 390 | 504990 | -90.69 | 13.50 | 311.61 | 0.14 | 2.78 | 1579 |
| 2024-09-20 22:21:32.218 | MS1 | 121.4656636671 | 31.1446356194 | 390 | 504990 | -91.35 | 15.26 | 587.63 | 0.06 | 2.79 | 1567 |
| 2024-09-20 22:21:33.563 | MS1 | 121.4656658418 | 31.1446289405 | 390 | 504990 | -86.24 | 17.53 | 554.02 | 0.07 | 2.51 | 1587 |
| 2024-09-20 22:21:34.599 | MS1 | 121.4656701994 | 31.1446355177 | 390 | 504990 | -88.58 | 16.79 | 72.93 | 0.57 | 2.33 | 610 |
| 2024-09-20 22:21:35.965 | MS1 | 121.4656708995 | 31.1446345677 | 390 | 504990 | -88.35 | 14.82 | 92.87 | 0.64 | 2.23 | 644 |
| 2024-09-20 22:21:36.939 | MS1 | 121.4656659309 | 31.1446235797 | 390 | 504990 | -89.82 | 14.37 | 86.15 | 0.69 | 2.23 | 578 |
| 2024-09-20 22:21:37.728 | MS1 | 121.4656683295 | 31.1446235800 | 390 | 504990 | -89.55 | 8.47 | 49.28 | 0.50 | 2.49 | 632 |
| 2024-09-20 22:21:38.269 | MS1 | 121.4656622112 | 31.1446318310 | 390 | 504990 | -89.99 | 9.71 | 97.49 | 0.68 | 2.18 | 635 |
| 2024-09-20 22:21:39.756 | MS1 | 121.4656717115 | 31.1446239591 | 390 | 504990 | -92.92 | 9.34 | 63.15 | 0.68 | 2.82 | 547 |
| 2024-09-20 22:21:40.946 | MS1 | 121.4656760847 | 31.1446253684 | 390 | 504990 | -90.12 | 8.91 | 498.11 | 0.02 | 2.73 | 1563 |
| 2024-09-20 22:21:41.562 | MS1 | 121.4656769135 | 31.1446232986 | 390 | 504990 | -89.46 | 9.03 | 598.20 | 0.14 | 2.42 | 1572 |
| 2024-09-20 22:21:42.937 | MS1 | 121.4656629655 | 31.1446219889 | 390 | 504990 | -91.61 | 11.55 | 402.13 | 0.13 | 2.54 | 1585 |

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
| 3237566 | 4 | 121.4675329101 | 31.1478770644 | 133 | 8 | 8 | 15.6 | TDD | 726 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3238730 | 2 | 121.4644212213 | 31.1522942706 | 163 | 2 | 11 | 29.0 | TDD | 390 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3259645 | 1 | 121.4750119624 | 31.1505571443 | 3 | 0 | 10 | 42.9 | TDD | 361 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3259702 | 3 | 121.4746453641 | 31.1490025488 | 225 | 8 | 11 | 44.3 | TDD | 261 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |

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
| 2024-09-20 22:21:31.450 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.470 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.593 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.593 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.258 | NREventA3 | measId:2;ServCellPCI:347;Se... |
| 2024-09-20 22:21:38.498 | NRHandoverAttempt | SourcePCI:347;SourceNR-ARFC... |
| 2024-09-20 22:21:38.546 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.560 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.702 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.702 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3259645 | 1 | 16.0204 | 13.1411 | -117.1161 | 18.7287 | 181.0518 | 0.0120 | 0.0159 |
| 2024_09_20 22:00 | 3238730 | 2 | 10.7415 | 11.6967 | -115.3127 | 11.7275 | 192.7025 | 0.0088 | 0.0184 |
| 2024_09_20 22:00 | 3259702 | 3 | 17.8973 | 5.7000 | -114.0249 | 12.5323 | 129.4610 | 0.0050 | 0.0151 |
| 2024_09_20 22:00 | 3237566 | 4 | 8.7433 | 6.9562 | -114.7553 | 8.2490 | 107.8593 | 0.0130 | 0.0200 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415316_82AC82F4 | 504990 | 390 | -86.7 | 504990 | 361 | -95.3 | 504990 | 726 | -98.8 | 504990 | 261 |
| MR_1774415316_23AF96B7 | 504990 | 390 | -89.6 | 504990 | 361 | -98.1 | 504990 | 726 | -96.1 | 504990 | 261 |
| MR_1774415316_DDCF096E | 504990 | 390 | -87.7 | 504990 | 361 | -97.9 | 504990 | 726 | -99.4 | 504990 | 261 |
| MR_1774415316_BFA22C4D | 504990 | 390 | -87.8 | 504990 | 361 | -95.3 | 504990 | 726 | -96.8 | 504990 | 261 |
| MR_1774415316_78A8A4D9 | 504990 | 390 | -90.4 | 504990 | 361 | -97.8 | 504990 | 726 | -98.8 | 504990 | 261 |
| MR_1774415316_94377F60 | 504990 | 390 | -87.2 | 504990 | 361 | -98.7 | 504990 | 726 | -96.3 | 504990 | 261 |
| MR_1774415316_228CA6B9 | 504990 | 390 | -90.2 | 504990 | 361 | -96.0 | 504990 | 726 | -96.1 | 504990 | 261 |
| MR_1774415316_58A314AC | 504990 | 390 | -88.8 | 504990 | 361 | -98.9 | 504990 | 726 | -99.1 | 504990 | 261 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 295: `4a0d2f3d-98c...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `4a0d2f3d-98c4-4fa0-a5c9-124086e01435` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[295] topology](images/test_0295.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle  of 3225432_2 by 8 degrees
- `C2`: Decrease transmission power for 3278999_4
- `C3`: Decrease A3 Offset threshold for 3278999_4
- `C4`: Check test server and transmission issues
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3278999_4
- `C6`: Press down the tilt angle of 3224937_1 by 3 degrees
- `C7`: Decrease transmission power for 3224937_1
- `C8`: Press down the tilt angle  of 3225432_2 by 8 degrees
- `C9`: Increase transmission power for 3278999_4
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3224937_1
- `C11`: Increase A3 Offset threshold for 3224937_1
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3278999_4
- `C13`: Lift the tilt angle of 3224937_1 by 3 degrees
- `C14`: Decrease A3 Offset threshold for 3224937_1
- `C15`: Insufficient data; more data is needed for judgment.
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3224937_1
- `C17`: Adjust the azimuth of 3224937_1 by 7 degrees
- `C18`: Increase transmission power for 3224937_1
- `C19`: Add neighbor relationship between 3224937_1 and 3278999_4
- `C20`: Adjust the azimuth of 3225432_2 by 50 degrees
- `C21`: Increase A3 Offset threshold for 3278999_4
- `C22`: Add neighbor relationship between 3225432_2 and 3278999_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.478 | MS1 | 121.4656678746 | 31.1446235608 | 761 | 504990 | -86.48 | 12.16 | 366.55 | 0.20 | 2.30 | 1561 |
| 2024-09-20 22:21:32.148 | MS1 | 121.4656619513 | 31.1446209283 | 761 | 504990 | -85.98 | 12.69 | 453.58 | 0.05 | 2.62 | 1585 |
| 2024-09-20 22:21:33.968 | MS1 | 121.4656763380 | 31.1446356544 | 761 | 504990 | -86.63 | 16.78 | 305.59 | 0.02 | 2.18 | 1570 |
| 2024-09-20 22:21:34.752 | MS1 | 121.4656669365 | 31.1446211849 | 761 | 504990 | -91.59 | 16.82 | 72.63 | 0.15 | 2.61 | 1567 |
| 2024-09-20 22:21:35.997 | MS1 | 121.4656764153 | 31.1446271011 | 761 | 504990 | -87.20 | 15.91 | 64.78 | 0.13 | 2.24 | 1571 |
| 2024-09-20 22:21:36.709 | MS1 | 121.4656759697 | 31.1446267845 | 761 | 504990 | -90.36 | 16.25 | 78.47 | 0.05 | 2.12 | 1564 |
| 2024-09-20 22:21:37.194 | MS1 | 121.4656707172 | 31.1446271106 | 761 | 504990 | -92.55 | 12.82 | 62.27 | 0.06 | 2.65 | 1570 |
| 2024-09-20 22:21:38.113 | MS1 | 121.4656674104 | 31.1446338177 | 761 | 504990 | -93.70 | 11.83 | 102.29 | 0.17 | 2.95 | 1563 |
| 2024-09-20 22:21:39.593 | MS1 | 121.4656696043 | 31.1446229620 | 761 | 504990 | -92.95 | 9.11 | 53.62 | 0.01 | 2.36 | 1562 |
| 2024-09-20 22:21:40.608 | MS1 | 121.4656603966 | 31.1446347633 | 761 | 504990 | -91.34 | 8.40 | 431.21 | 0.08 | 2.67 | 1572 |
| 2024-09-20 22:21:41.782 | MS1 | 121.4656741868 | 31.1446357543 | 761 | 504990 | -93.35 | 12.30 | 351.94 | 0.10 | 2.73 | 1561 |
| 2024-09-20 22:21:42.598 | MS1 | 121.4656647075 | 31.1446332064 | 761 | 504990 | -93.95 | 9.35 | 590.54 | 0.10 | 2.65 | 1569 |

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
| 3224937 | 1 | 121.4733133233 | 31.1448532935 | 261 | 0 | 8 | 40.2 | TDD | 761 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3225432 | 2 | 121.4671035020 | 31.1555566857 | 358 | 4 | 6 | 48.4 | TDD | 755 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3266507 | 3 | 121.4682669904 | 31.1483791823 | 87 | 6 | 10 | 40.6 | TDD | 221 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3278999 | 4 | 121.4746921706 | 31.1509745063 | 50 | 6 | 10 | 40.7 | TDD | 366 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

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
| 2024-09-20 22:21:31.385 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.402 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.503 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.503 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.276 | NREventA3 | measId:2;ServCellPCI:577;Se... |
| 2024-09-20 22:21:38.516 | NRHandoverAttempt | SourcePCI:577;SourceNR-ARFC... |
| 2024-09-20 22:21:38.548 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.563 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.695 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.695 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3224937 | 1 | 76.7200 | 92.4040 | -114.1095 | 19.8561 | 174.8105 | 0.0081 | 0.0157 |
| 2024_09_20 22:00 | 3225432 | 2 | 17.3993 | 10.4090 | -114.9123 | 17.2375 | 98.1280 | 0.0161 | 0.0060 |
| 2024_09_20 22:00 | 3266507 | 3 | 5.0990 | 12.6713 | -114.5995 | 11.5384 | 106.4442 | 0.0092 | 0.0007 |
| 2024_09_20 22:00 | 3278999 | 4 | 18.3748 | 10.8718 | -115.3929 | 18.3398 | 128.5359 | 0.0135 | 0.0182 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416757_0B772DE6 | 504990 | 761 | -93.5 | 504990 | 366 | -91.7 | 504990 | 755 | -99.4 | 504990 | 221 |
| MR_1774416757_24BD59C9 | 504990 | 761 | -91.1 | 504990 | 366 | -93.0 | 504990 | 755 | -101.2 | 504990 | 221 |
| MR_1774416757_19E2A061 | 504990 | 761 | -92.0 | 504990 | 366 | -94.0 | 504990 | 755 | -98.7 | 504990 | 221 |
| MR_1774416757_9E1D741E | 504990 | 761 | -93.2 | 504990 | 366 | -92.4 | 504990 | 755 | -98.0 | 504990 | 221 |
| MR_1774416757_A96D90FE | 504990 | 761 | -90.4 | 504990 | 366 | -92.9 | 504990 | 755 | -100.8 | 504990 | 221 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 296: `4fb1d9a6-c5d...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `4fb1d9a6-c5db-428b-a734-ed143d63cacc` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[296] topology](images/test_0296.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3226062_3
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3252094_2
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3226062_3
- `C4`: Add neighbor relationship between 3271186_1 and 3226062_3
- `C5`: Increase A3 Offset threshold for 3226062_3
- `C6`: Decrease A3 Offset threshold for 3226062_3
- `C7`: Decrease transmission power for 3252094_2
- `C8`: Decrease A3 Offset threshold for 3252094_2
- `C9`: Adjust the azimuth of 3226062_3 by 50 degrees
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3252094_2
- `C11`: Insufficient data; more data is needed for judgment.
- `C12`: Increase transmission power for 3252094_2
- `C13`: Add neighbor relationship between 3252094_2 and 3226062_3
- `C14`: Check test server and transmission issues
- `C15`: Press down the tilt angle of 3252094_2 by 10 degrees
- `C16`: Increase transmission power for 3226062_3
- `C17`: Lift the tilt angle of 3252094_2 by 10 degrees
- `C18`: Press down the tilt angle  of 3226062_3 by 10 degrees
- `C19`: Increase A3 Offset threshold for 3252094_2
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3226062_3
- `C21`: Adjust the azimuth of 3252094_2 by 50 degrees
- `C22`: Lift the tilt angle  of 3226062_3 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.992 | MS1 | 121.4656706307 | 31.1446244444 | 365 | 504990 | -91.48 | 17.73 | 516.81 | 0.00 | 2.03 | 1593 |
| 2024-09-20 22:21:32.929 | MS1 | 121.4656702317 | 31.1446186176 | 365 | 504990 | -89.45 | 16.20 | 587.42 | 0.06 | 2.64 | 1564 |
| 2024-09-20 22:21:33.675 | MS1 | 121.4656751626 | 31.1446271657 | 365 | 504990 | -85.17 | 16.08 | 487.64 | 0.18 | 2.17 | 1585 |
| 2024-09-20 22:21:34.838 | MS1 | 121.4656756188 | 31.1446366140 | 365 | 504990 | -88.14 | 15.04 | 70.24 | 0.04 | 2.88 | 1590 |
| 2024-09-20 22:21:35.147 | MS1 | 121.4656752591 | 31.1446362129 | 365 | 504990 | -87.82 | 17.75 | 73.97 | 0.18 | 2.34 | 1568 |
| 2024-09-20 22:21:36.587 | MS1 | 121.4656589145 | 31.1446286498 | 365 | 504990 | -88.51 | 16.17 | 67.82 | 0.19 | 2.99 | 1597 |
| 2024-09-20 22:21:37.134 | MS1 | 121.4656707574 | 31.1446338746 | 365 | 504990 | -91.58 | 9.69 | 67.63 | 0.12 | 2.22 | 1573 |
| 2024-09-20 22:21:38.977 | MS1 | 121.4656763512 | 31.1446257949 | 365 | 504990 | -90.07 | 12.48 | 46.49 | 0.02 | 2.21 | 1561 |
| 2024-09-20 22:21:39.933 | MS1 | 121.4656685373 | 31.1446225613 | 365 | 504990 | -91.57 | 8.57 | 90.31 | 0.01 | 2.18 | 1561 |
| 2024-09-20 22:21:40.673 | MS1 | 121.4656765701 | 31.1446362645 | 365 | 504990 | -90.13 | 10.06 | 320.00 | 0.13 | 2.56 | 1587 |
| 2024-09-20 22:21:41.827 | MS1 | 121.4656626752 | 31.1446355886 | 365 | 504990 | -91.41 | 10.12 | 430.93 | 0.18 | 2.72 | 1589 |
| 2024-09-20 22:21:42.752 | MS1 | 121.4656743733 | 31.1446218260 | 365 | 504990 | -93.90 | 12.99 | 603.20 | 0.13 | 2.61 | 1570 |

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
| 3225533 | 4 | 121.4732054908 | 31.1525584851 | 300 | 8 | 11 | 45.1 | TDD | 327 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3226062 | 3 | 121.4661566044 | 31.1444169443 | 42 | 0 | 5 | 33.7 | TDD | 238 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3252094 | 2 | 121.4658831715 | 31.1496442165 | 313 | 12 | 9 | 19.3 | TDD | 365 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3271186 | 1 | 121.4708230392 | 31.1487377365 | 341 | 11 | 1 | 45.3 | TDD | 24 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

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
| 2024-09-20 22:21:31.020 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.163 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.163 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.875 | NREventA3 | measId:2;ServCellPCI:960;Se... |
| 2024-09-20 22:21:38.115 | NRHandoverAttempt | SourcePCI:960;SourceNR-ARFC... |
| 2024-09-20 22:21:38.158 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.170 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.282 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.282 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3271186 | 1 | 77.5257 | 92.6913 | -115.1898 | 7.7130 | 184.8088 | 0.0103 | 0.0184 |
| 2024_09_19 22:00 | 3252094 | 2 | 81.9634 | 78.9968 | -114.2806 | 19.6433 | 152.1733 | 0.0042 | 0.0048 |
| 2024_09_19 22:00 | 3226062 | 3 | 80.5906 | 90.2114 | -116.0718 | 7.1940 | 196.5391 | 0.0121 | 0.0164 |
| 2024_09_19 22:00 | 3225533 | 4 | 83.6329 | 91.9347 | -114.5705 | 9.7246 | 92.4801 | 0.0116 | 0.0159 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417153_E2B068E8 | 504990 | 365 | -88.3 | 504990 | 238 | -91.7 | 504990 | 24 | -101.5 | 504990 | 327 |
| MR_1774417153_881427F7 | 504990 | 365 | -89.9 | 504990 | 238 | -92.2 | 504990 | 24 | -99.2 | 504990 | 327 |
| MR_1774417153_89AAD717 | 504990 | 365 | -88.7 | 504990 | 238 | -92.0 | 504990 | 24 | -101.2 | 504990 | 327 |
| MR_1774417153_9103B668 | 504990 | 365 | -88.0 | 504990 | 238 | -91.8 | 504990 | 24 | -99.4 | 504990 | 327 |
| MR_1774417153_E69A3E29 | 504990 | 365 | -89.3 | 504990 | 238 | -90.0 | 504990 | 24 | -101.1 | 504990 | 327 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 297: `c68566f1-996...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `c68566f1-996a-41fb-9e35-5c6d4b753ab1` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[297] topology](images/test_0297.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3269677_2
- `C2`: Increase A3 Offset threshold for 3269677_2
- `C3`: Lift the tilt angle of 3271497_3 by 10 degrees
- `C4`: Decrease A3 Offset threshold for 3269677_2
- `C5`: Lift the tilt angle  of 3269677_2 by 10 degrees
- `C6`: Add neighbor relationship between 3228849_4 and 3269677_2
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3271497_3
- `C8`: Increase transmission power for 3269677_2
- `C9`: Add neighbor relationship between 3271497_3 and 3269677_2
- `C10`: Insufficient data; more data is needed for judgment.
- `C11`: Adjust the azimuth of 3269677_2 by 50 degrees
- `C12`: Press down the tilt angle  of 3269677_2 by 10 degrees
- `C13`: Press down the tilt angle of 3271497_3 by 10 degrees
- `C14`: Increase A3 Offset threshold for 3271497_3
- `C15`: Adjust the azimuth of 3271497_3 by 50 degrees
- `C16`: Decrease transmission power for 3269677_2
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3271497_3
- `C18`: Decrease transmission power for 3271497_3
- `C19`: Decrease A3 Offset threshold for 3271497_3
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3269677_2
- `C21`: Increase transmission power for 3271497_3
- `C22`: Check test server and transmission issues

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.208 | MS1 | 121.4656651521 | 31.1446321756 | 301 | 504990 | -82.78 | 15.27 | 347.52 | 0.11 | 2.66 | 1588 |
| 2024-09-20 22:21:32.725 | MS1 | 121.4656650309 | 31.1446183931 | 301 | 504990 | -84.58 | 14.25 | 513.14 | 0.01 | 2.01 | 1595 |
| 2024-09-20 22:21:33.787 | MS1 | 121.4656687448 | 31.1446232295 | 301 | 504990 | -76.61 | 14.17 | 401.39 | 0.03 | 2.67 | 1574 |
| 2024-09-20 22:21:34.998 | MS1 | 121.4656706303 | 31.1446342531 | 301 | 504990 | -83.03 | -2.78 | 48.59 | 0.14 | 1.35 | 1583 |
| 2024-09-20 22:21:35.544 | MS1 | 121.4656716494 | 31.1446287344 | 301 | 504990 | -83.90 | -3.26 | 49.50 | 0.13 | 1.32 | 1595 |
| 2024-09-20 22:21:36.662 | MS1 | 121.4656690383 | 31.1446376858 | 301 | 504990 | -87.71 | -0.27 | 80.30 | 0.19 | 1.19 | 1586 |
| 2024-09-20 22:21:37.140 | MS1 | 121.4656632983 | 31.1446213981 | 301 | 504990 | -83.68 | -0.52 | 56.97 | 0.16 | 1.45 | 1568 |
| 2024-09-20 22:21:38.144 | MS1 | 121.4656775805 | 31.1446247600 | 301 | 504990 | -83.75 | -0.28 | 51.29 | 0.16 | 1.43 | 1582 |
| 2024-09-20 22:21:39.351 | MS1 | 121.4656727943 | 31.1446351449 | 243 | 504990 | -79.67 | 14.94 | 269.00 | 0.15 | 1.30 | 1585 |
| 2024-09-20 22:21:40.896 | MS1 | 121.4656624415 | 31.1446191879 | 243 | 504990 | -75.25 | 17.24 | 390.87 | 0.09 | 2.08 | 1574 |
| 2024-09-20 22:21:41.178 | MS1 | 121.4656658690 | 31.1446318013 | 243 | 504990 | -81.05 | 14.18 | 542.35 | 0.01 | 2.87 | 1589 |
| 2024-09-20 22:21:42.961 | MS1 | 121.4656594494 | 31.1446335977 | 243 | 504990 | -77.95 | 13.08 | 495.84 | 0.06 | 2.28 | 1571 |

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
| 3224196 | 1 | 121.4746317816 | 31.1536017140 | 184 | 8 | 8 | 19.2 | TDD | 937 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3228849 | 4 | 121.4725984125 | 31.1543325137 | 280 | 8 | 0 | 22.2 | TDD | 731 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3269677 | 2 | 121.4758537694 | 31.1498172150 | 145 | 12 | 3 | 35.6 | TDD | 243 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3271497 | 3 | 121.4673455809 | 31.1503696343 | 312 | 10 | 5 | 41.5 | TDD | 301 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:31.286 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.301 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.414 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.414 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.162 | NREventA3 | measId:2;ServCellPCI:472;Se... |
| 2024-09-20 22:21:38.402 | NRHandoverAttempt | SourcePCI:472;SourceNR-ARFC... |
| 2024-09-20 22:21:38.449 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.460 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.600 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.600 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3224196 | 1 | 10.8983 | 6.5340 | -117.7196 | 12.0286 | 105.3330 | 0.0145 | 0.0028 |
| 2024_09_20 22:00 | 3269677 | 2 | 6.1647 | 19.0017 | -117.5798 | 15.3771 | 151.6699 | 0.0006 | 0.0133 |
| 2024_09_20 22:00 | 3271497 | 3 | 6.0753 | 14.3247 | -114.4689 | 16.2562 | 196.7377 | 0.0073 | 0.1183 |
| 2024_09_20 22:00 | 3228849 | 4 | 15.4242 | 12.2961 | -116.6080 | 14.4359 | 112.3719 | 0.0003 | 0.0024 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416783_7A0BDC35 | 504990 | 243 | -80.6 | 504990 | 301 | -82.6 | 504990 | 731 | -81.2 | 504990 | 937 |
| MR_1774416783_23D9B574 | 504990 | 301 | -84.1 | 504990 | 243 | -78.8 | 504990 | 731 | -82.3 | 504990 | 937 |
| MR_1774416783_0C959C35 | 504990 | 301 | -82.7 | 504990 | 243 | -76.8 | 504990 | 731 | -81.9 | 504990 | 937 |
| MR_1774416783_04F134EA | 504990 | 301 | -81.6 | 504990 | 243 | -78.3 | 504990 | 731 | -83.9 | 504990 | 937 |
| MR_1774416783_0D1E58A8 | 504990 | 301 | -84.7 | 504990 | 243 | -80.5 | 504990 | 731 | -81.4 | 504990 | 937 |
| MR_1774416783_21830ABC | 504990 | 301 | -82.9 | 504990 | 243 | -78.9 | 504990 | 731 | -82.8 | 504990 | 937 |
| MR_1774416783_84592B95 | 504990 | 301 | -82.1 | 504990 | 243 | -77.7 | 504990 | 731 | -84.2 | 504990 | 937 |
| MR_1774416783_37F9AA62 | 504990 | 243 | -79.0 | 504990 | 301 | -81.4 | 504990 | 731 | -81.1 | 504990 | 937 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 298: `f2e9383a-947...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `f2e9383a-9471-4f7a-8d9c-355e68193cf7` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[298] topology](images/test_0298.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3232449_2 by 50 degrees
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3238543_4
- `C3`: Press down the tilt angle of 3238543_4 by 10 degrees
- `C4`: Adjust the azimuth of 3238543_4 by 50 degrees
- `C5`: Check test server and transmission issues
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3238543_4
- `C7`: Decrease transmission power for 3238543_4
- `C8`: Decrease transmission power for 3232449_2
- `C9`: Decrease A3 Offset threshold for 3238543_4
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3232449_2
- `C11`: Decrease A3 Offset threshold for 3232449_2
- `C12`: Lift the tilt angle  of 3232449_2 by 4 degrees
- `C13`: Insufficient data; more data is needed for judgment.
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3232449_2
- `C15`: Increase A3 Offset threshold for 3238543_4
- `C16`: Increase A3 Offset threshold for 3232449_2
- `C17`: Add neighbor relationship between 3238543_4 and 3232449_2
- `C18`: Increase transmission power for 3232449_2
- `C19`: Increase transmission power for 3238543_4
- `C20`: Add neighbor relationship between 3247743_3 and 3232449_2
- `C21`: Lift the tilt angle of 3238543_4 by 10 degrees
- `C22`: Press down the tilt angle  of 3232449_2 by 4 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.137 | MS1 | 121.4656641884 | 31.1446344715 | 23 | 504990 | -88.47 | 17.86 | 399.61 | 0.09 | 2.25 | 1567 |
| 2024-09-20 22:21:32.400 | MS1 | 121.4656684816 | 31.1446290349 | 23 | 504990 | -88.94 | 15.90 | 491.82 | 0.08 | 2.15 | 1581 |
| 2024-09-20 22:21:33.914 | MS1 | 121.4656767807 | 31.1446364603 | 23 | 504990 | -86.90 | 16.93 | 401.72 | 0.04 | 2.86 | 1582 |
| 2024-09-20 22:21:34.248 | MS1 | 121.4656745314 | 31.1446307020 | 23 | 504990 | -88.08 | 13.31 | 99.10 | 0.01 | 2.16 | 1563 |
| 2024-09-20 22:21:35.263 | MS1 | 121.4656752290 | 31.1446311648 | 23 | 504990 | -90.54 | 16.46 | 98.24 | 0.17 | 2.06 | 1590 |
| 2024-09-20 22:21:36.377 | MS1 | 121.4656640285 | 31.1446185157 | 23 | 504990 | -86.59 | 14.41 | 88.52 | 0.09 | 2.51 | 1577 |
| 2024-09-20 22:21:37.815 | MS1 | 121.4656669972 | 31.1446374788 | 23 | 504990 | -92.68 | 9.32 | 81.43 | 0.04 | 2.84 | 1599 |
| 2024-09-20 22:21:38.954 | MS1 | 121.4656612774 | 31.1446374307 | 23 | 504990 | -90.07 | 12.65 | 81.32 | 0.10 | 2.14 | 1587 |
| 2024-09-20 22:21:39.930 | MS1 | 121.4656746105 | 31.1446376451 | 23 | 504990 | -92.93 | 11.52 | 106.78 | 0.20 | 2.03 | 1568 |
| 2024-09-20 22:21:40.592 | MS1 | 121.4656737959 | 31.1446237143 | 23 | 504990 | -93.14 | 9.08 | 569.71 | 0.16 | 2.28 | 1564 |
| 2024-09-20 22:21:41.768 | MS1 | 121.4656638204 | 31.1446216770 | 23 | 504990 | -92.71 | 10.09 | 538.08 | 0.02 | 2.96 | 1599 |
| 2024-09-20 22:21:42.849 | MS1 | 121.4656632167 | 31.1446250445 | 23 | 504990 | -92.54 | 12.55 | 522.97 | 0.11 | 2.31 | 1567 |

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
| 3232449 | 2 | 121.4728017128 | 31.1505349757 | 342 | 2 | 9 | 26.4 | TDD | 772 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3238543 | 4 | 121.4656536885 | 31.1528373024 | 295 | 10 | 5 | 26.6 | TDD | 23 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3247743 | 3 | 121.4673440038 | 31.1539059381 | 2 | 10 | 9 | 48.5 | TDD | 798 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3276642 | 1 | 121.4642709949 | 31.1454556675 | 72 | 6 | 11 | 30.4 | TDD | 867 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |

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
| 2024-09-20 22:21:31.398 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.418 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.532 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.532 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.233 | NREventA3 | measId:2;ServCellPCI:104;Se... |
| 2024-09-20 22:21:38.473 | NRHandoverAttempt | SourcePCI:104;SourceNR-ARFC... |
| 2024-09-20 22:21:38.504 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.518 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.633 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.633 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3276642 | 1 | 77.4710 | 75.8516 | -117.2040 | 15.8935 | 119.9679 | 0.0052 | 0.0120 |
| 2024_09_19 22:00 | 3232449 | 2 | 91.4456 | 80.9645 | -117.0651 | 18.3564 | 111.6075 | 0.0014 | 0.0162 |
| 2024_09_19 22:00 | 3247743 | 3 | 82.0355 | 79.3442 | -116.7526 | 16.7346 | 122.7184 | 0.0029 | 0.0008 |
| 2024_09_19 22:00 | 3238543 | 4 | 89.1316 | 93.0383 | -116.4909 | 7.1723 | 120.6545 | 0.0047 | 0.0161 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414799_94FDD500 | 504990 | 23 | -87.1 | 504990 | 772 | -98.0 | 504990 | 798 | -99.2 | 504990 | 867 |
| MR_1774414799_FB35935C | 504990 | 23 | -87.0 | 504990 | 772 | -99.3 | 504990 | 798 | -97.2 | 504990 | 867 |
| MR_1774414799_E6C896A9 | 504990 | 23 | -86.3 | 504990 | 772 | -97.8 | 504990 | 798 | -98.5 | 504990 | 867 |
| MR_1774414799_F7B9FAA9 | 504990 | 23 | -88.2 | 504990 | 772 | -98.1 | 504990 | 798 | -99.3 | 504990 | 867 |
| MR_1774414799_26001E94 | 504990 | 23 | -88.9 | 504990 | 772 | -97.4 | 504990 | 798 | -98.6 | 504990 | 867 |
| MR_1774414799_530F297C | 504990 | 23 | -87.9 | 504990 | 772 | -98.3 | 504990 | 798 | -98.6 | 504990 | 867 |
| MR_1774414799_66D36DC9 | 504990 | 23 | -87.3 | 504990 | 772 | -98.8 | 504990 | 798 | -98.9 | 504990 | 867 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 299: `65a90582-b07...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `65a90582-b070-4bf1-b22e-53b40cc6d7fb` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[299] topology](images/test_0299.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3215904_2
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3215904_2
- `C3`: Lift the tilt angle of 3266486_1 by 5 degrees
- `C4`: Press down the tilt angle  of 3215904_2 by 10 degrees
- `C5`: Lift the tilt angle  of 3215904_2 by 10 degrees
- `C6`: Press down the tilt angle of 3266486_1 by 5 degrees
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3215904_2
- `C8`: Increase transmission power for 3215904_2
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3266486_1
- `C10`: Decrease transmission power for 3266486_1
- `C11`: Check test server and transmission issues
- `C12`: Add neighbor relationship between 3264573_3 and 3215904_2
- `C13`: Adjust the azimuth of 3266486_1 by 13 degrees
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Adjust the azimuth of 3215904_2 by 47 degrees
- `C16`: Increase A3 Offset threshold for 3266486_1
- `C17`: Decrease A3 Offset threshold for 3266486_1
- `C18`: Add neighbor relationship between 3266486_1 and 3215904_2
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3266486_1
- `C20`: Increase A3 Offset threshold for 3215904_2
- `C21`: Increase transmission power for 3266486_1
- `C22`: Decrease transmission power for 3215904_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.231 | MS1 | 121.4656721705 | 31.1446354275 | 441 | 504990 | -81.97 | 15.05 | 404.42 | 0.15 | 2.03 | 1593 |
| 2024-09-20 22:21:32.678 | MS1 | 121.4656600683 | 31.1446238621 | 441 | 504990 | -75.65 | 13.17 | 391.07 | 0.04 | 2.02 | 1575 |
| 2024-09-20 22:21:33.903 | MS1 | 121.4656764260 | 31.1446321467 | 441 | 504990 | -83.30 | 13.01 | 408.28 | 0.09 | 2.98 | 1591 |
| 2024-09-20 22:21:34.390 | MS1 | 121.4656757523 | 31.1446325183 | 441 | 504990 | -89.11 | -3.86 | 51.51 | 0.08 | 1.28 | 1573 |
| 2024-09-20 22:21:35.232 | MS1 | 121.4656754229 | 31.1446230121 | 441 | 504990 | -85.97 | -1.01 | 46.35 | 0.01 | 1.46 | 1587 |
| 2024-09-20 22:21:36.701 | MS1 | 121.4656752263 | 31.1446231201 | 441 | 504990 | -91.89 | -2.35 | 54.60 | 0.01 | 1.48 | 1569 |
| 2024-09-20 22:21:37.460 | MS1 | 121.4656728511 | 31.1446283175 | 441 | 504990 | -86.45 | -2.03 | 40.50 | 0.01 | 1.44 | 1594 |
| 2024-09-20 22:21:38.648 | MS1 | 121.4656769942 | 31.1446335137 | 441 | 504990 | -84.20 | -2.10 | 62.60 | 0.18 | 1.40 | 1595 |
| 2024-09-20 22:21:39.597 | MS1 | 121.4656667071 | 31.1446212843 | 770 | 504990 | -76.02 | 16.86 | 212.20 | 0.08 | 1.47 | 1564 |
| 2024-09-20 22:21:40.399 | MS1 | 121.4656611061 | 31.1446307680 | 770 | 504990 | -78.57 | 16.59 | 427.49 | 0.02 | 2.05 | 1585 |
| 2024-09-20 22:21:41.157 | MS1 | 121.4656640938 | 31.1446343745 | 770 | 504990 | -80.42 | 15.17 | 347.02 | 0.14 | 2.41 | 1573 |
| 2024-09-20 22:21:42.234 | MS1 | 121.4656646112 | 31.1446222275 | 770 | 504990 | -83.54 | 12.34 | 332.73 | 0.16 | 2.87 | 1582 |

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
| 3215904 | 2 | 121.4648894571 | 31.1495502263 | 125 | 9 | 11 | 17.9 | TDD | 770 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3264573 | 3 | 121.4708838334 | 31.1509570659 | 329 | 1 | 8 | 26.2 | TDD | 477 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3266486 | 1 | 121.4691754681 | 31.1496277460 | 224 | 2 | 6 | 31.6 | TDD | 441 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3275425 | 4 | 121.4677772997 | 31.1505153941 | 248 | 4 | 11 | 41.0 | TDD | 534 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |

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
| 2024-09-20 22:21:30.750 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.775 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:30.884 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.884 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.611 | NREventA3 | measId:2;ServCellPCI:224;Se... |
| 2024-09-20 22:21:37.851 | NRHandoverAttempt | SourcePCI:224;SourceNR-ARFC... |
| 2024-09-20 22:21:37.895 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.907 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.019 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.019 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3266486 | 1 | 12.2841 | 10.8057 | -115.6788 | 6.2718 | 111.8794 | 0.0164 | 0.1876 |
| 2024_09_20 22:00 | 3215904 | 2 | 12.9755 | 19.8218 | -114.5221 | 17.7361 | 82.8665 | 0.0024 | 0.0089 |
| 2024_09_20 22:00 | 3264573 | 3 | 10.6793 | 19.8766 | -115.8738 | 5.3783 | 82.7699 | 0.0001 | 0.0048 |
| 2024_09_20 22:00 | 3275425 | 4 | 8.3100 | 19.1291 | -114.0765 | 8.7958 | 146.3584 | 0.0000 | 0.0112 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415554_8BAA8B71 | 504990 | 441 | -90.0 | 504990 | 770 | -83.9 | 504990 | 477 | -85.7 | 504990 | 534 |
| MR_1774415554_11853657 | 504990 | 770 | -82.9 | 504990 | 441 | -89.7 | 504990 | 477 | -87.8 | 504990 | 534 |
| MR_1774415554_8DF2C1F3 | 504990 | 441 | -89.4 | 504990 | 770 | -84.6 | 504990 | 477 | -86.2 | 504990 | 534 |
| MR_1774415554_CC9E8EF7 | 504990 | 441 | -87.2 | 504990 | 770 | -83.0 | 504990 | 477 | -86.6 | 504990 | 534 |
| MR_1774415554_E56D2750 | 504990 | 770 | -85.5 | 504990 | 441 | -90.1 | 504990 | 477 | -88.0 | 504990 | 534 |

> *... 2개 열 생략 (전체 14열)*

---
