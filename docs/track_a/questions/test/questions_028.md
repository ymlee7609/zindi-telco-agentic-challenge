# Track A 문제 분석 — test[270]~test[279]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/test.json`
> 범위: test[270] ~ test[279] (10개)

## 목차

1. [문제 270: `c6fd35ca-fd7...`](#270) — single-answer
2. [문제 271: `27ec44ed-284...`](#271) — single-answer
3. [문제 272: `c48c772c-6ca...`](#272) — single-answer
4. [문제 273: `3f1e8a1c-33c...`](#273) — single-answer
5. [문제 274: `7ebb3374-b85...`](#274) — multiple-answer
6. [문제 275: `419dfe03-35a...`](#275) — single-answer
7. [문제 276: `bce6d685-3e1...`](#276) — single-answer
8. [문제 277: `e233b67c-f5f...`](#277) — single-answer
9. [문제 278: `6d6dca89-d76...`](#278) — single-answer
10. [문제 279: `2cad12ac-b4a...`](#279) — single-answer

---

### 문제 270: `c6fd35ca-fd7...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `c6fd35ca-fd7c-4470-825b-8f814d44a2c2` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[270] topology](images/test_0270.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3222323_5 by 38 degrees
- `C2`: Press down the tilt angle  of 3254336_3 by 4 degrees
- `C3`: Add neighbor relationship between 3216650_9 and 3254336_3
- `C4`: Increase A3 Offset threshold for 3254336_3
- `C5`: Lift the tilt angle of 3222323_5 by 5 degrees
- `C6`: Check test server and transmission issues
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3254336_3
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3254336_3
- `C9`: Decrease A3 Offset threshold for 3222323_5
- `C10`: Decrease transmission power for 3254336_3
- `C11`: Add neighbor relationship between 3222323_5 and 3254336_3
- `C12`: Increase transmission power for 3254336_3
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3222323_5
- `C14`: Adjust the azimuth of 3254336_3 by 30 degrees
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3222323_5
- `C16`: Insufficient data; more data is needed for judgment.
- `C17`: Decrease transmission power for 3222323_5
- `C18`: Increase A3 Offset threshold for 3222323_5
- `C19`: Press down the tilt angle of 3222323_5 by 5 degrees
- `C20`: Decrease A3 Offset threshold for 3254336_3
- `C21`: Increase transmission power for 3222323_5
- `C22`: Lift the tilt angle  of 3254336_3 by 4 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.359 | MS1 | 121.4656658029 | 31.1446183012 | 220 | 504990 | -93.38 | 10.37 | 542.16 | 0.07 | 2.05 | 1591 |
| 2024-09-20 22:21:32.323 | MS1 | 121.4656702342 | 31.1446366267 | 126 | 504990 | -93.88 | 10.55 | 442.79 | 0.10 | 2.85 | 1579 |
| 2024-09-20 22:21:33.383 | MS1 | 121.4656589368 | 31.1446235310 | 65 | 504990 | -94.19 | 9.46 | 413.66 | 0.07 | 2.87 | 1596 |
| 2024-09-20 22:21:34.664 | MS1 | 121.4656709200 | 31.1446314876 | 932 | 152650 | -95.24 | 4.01 | 79.81 | 0.05 | 1.81 | 993 |
| 2024-09-20 22:21:35.968 | MS1 | 121.4656766457 | 31.1446255181 | 883 | 152650 | -89.09 | 7.06 | 79.30 | 0.10 | 1.50 | 941 |
| 2024-09-20 22:21:36.172 | MS1 | 121.4656686887 | 31.1446252342 | 488 | 152650 | -89.99 | 2.43 | 73.82 | 0.07 | 1.85 | 955 |
| 2024-09-20 22:21:37.762 | MS1 | 121.4656625188 | 31.1446353124 | 155 | 152650 | -91.09 | 5.86 | 91.95 | 0.11 | 1.97 | 960 |
| 2024-09-20 22:21:38.116 | MS1 | 121.4656611457 | 31.1446367839 | 932 | 152650 | -88.72 | 6.02 | 91.98 | 0.13 | 1.56 | 946 |
| 2024-09-20 22:21:39.819 | MS1 | 121.4656687622 | 31.1446278586 | 883 | 152650 | -89.36 | 3.21 | 63.64 | 0.10 | 1.98 | 912 |
| 2024-09-20 22:21:40.955 | MS1 | 121.4656622827 | 31.1446324611 | 488 | 152650 | -93.85 | 3.46 | 43.76 | 0.08 | 2.44 | 1598 |
| 2024-09-20 22:21:41.722 | MS1 | 121.4656607022 | 31.1446373533 | 155 | 152650 | -90.67 | 6.17 | 58.02 | 0.18 | 2.22 | 1574 |
| 2024-09-20 22:21:42.868 | MS1 | 121.4656759544 | 31.1446199882 | 932 | 152650 | -89.13 | 6.03 | 87.13 | 0.18 | 2.10 | 1560 |

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
| 3212545 | 7 | 121.4736497521 | 31.1490834235 | 2 | 6 | 11 | 6.3 | FDD | 932 | n1 | 152650 | 30M | 4T4R | 26 | 152650 |
| 3216650 | 9 | 121.4668739826 | 31.1480489866 | 109 | 4 | 8 | 21.7 | FDD | 488 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |
| 3221298 | 13 | 121.4718640950 | 31.1505002178 | 198 | 15 | 6 | 20.6 | FDD | 155 | n1 | 152650 | 30M | 4T4R | 20 | 152650 |
| 3222323 | 5 | 121.4722508096 | 31.1543858895 | 248 | 5 | 4 | 0.0 | TDD | 220 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3222634 | 1 | 121.4665213337 | 31.1546435022 | 167 | 13 | 12 | 11.8 | TDD | 65 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3232644 | 12 | 121.4748894087 | 31.1477446185 | 292 | 11 | 11 | 28.2 | FDD | 883 | n1 | 152650 | 30M | 4T4R | 13 | 152650 |
| 3235884 | 11 | 121.4662583561 | 31.1474042117 | 60 | 6 | 5 | 0.1 | FDD | 402 | n1 | 152650 | 30M | 4T4R | 19 | 152650 |
| 3254336 | 3 | 121.4714806172 | 31.1534198883 | 240 | 4 | 11 | 4.0 | TDD | 429 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3255051 | 10 | 121.4684237248 | 31.1472422751 | 19 | 9 | 7 | 12.9 | FDD | 778 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |
| 3256718 | 8 | 121.4711745146 | 31.1515752946 | 76 | 12 | 5 | 10.9 | FDD | 133 | n1 | 152650 | 30M | 4T4R | 18 | 152650 |
| 3272631 | 4 | 121.4675263347 | 31.1485720422 | 192 | 15 | 5 | 13.0 | TDD | 152 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3275922 | 2 | 121.4676971478 | 31.1508522325 | 304 | 4 | 10 | 25.2 | TDD | 228 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3278316 | 6 | 121.4681519177 | 31.1504934863 | 211 | 11 | 7 | 27.6 | TDD | 126 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |

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
| 2024-09-20 22:21:31.185 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.298 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.298 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.055 | NREventA2 | measId:1;ServCellPCI:836;Se... |
| 2024-09-20 22:21:35.174 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.461 | NREventA5 | measId:3;ServCellPCI:836;Se... |
| 2024-09-20 22:21:35.533 | NRHandoverAttempt | SourcePCI:836;SourceNR-ARFC... |
| 2024-09-20 22:21:35.582 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.592 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:35.723 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.723 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3222634 | 1 | 13.5632 | 14.5918 | -115.3075 | 10.4790 | 120.5740 | 0.0087 | 0.0142 |
| 2024_09_20 22:00 | 3275922 | 2 | 18.8387 | 9.1990 | -114.1146 | 7.3951 | 187.7698 | 0.0115 | 0.0077 |
| 2024_09_20 22:00 | 3254336 | 3 | 13.9440 | 6.0877 | -117.7993 | 14.1292 | 138.5505 | 0.0129 | 0.0109 |
| 2024_09_20 22:00 | 3272631 | 4 | 16.9878 | 19.9423 | -117.9868 | 14.2349 | 116.1892 | 0.0067 | 0.0070 |
| 2024_09_20 22:00 | 3222323 | 5 | 18.2430 | 12.5130 | -115.8548 | 10.2857 | 98.7820 | 0.0138 | 0.0061 |
| 2024_09_20 22:00 | 3278316 | 6 | 7.5967 | 11.9171 | -117.4332 | 18.7487 | 162.5679 | 0.0071 | 0.0068 |
| 2024_09_20 22:00 | 3212545 | 7 | 16.7777 | 16.9732 | -115.0319 | 3.0146 | 26.2540 | 0.0096 | 0.0163 |
| 2024_09_20 22:00 | 3256718 | 8 | 9.2113 | 18.5151 | -115.0639 | 4.0156 | 27.0299 | 0.0186 | 0.0101 |
| 2024_09_20 22:00 | 3216650 | 9 | 19.2261 | 13.0984 | -114.0477 | 3.9385 | 30.8461 | 0.0004 | 0.0106 |
| 2024_09_20 22:00 | 3255051 | 10 | 13.2897 | 13.1515 | -116.7989 | 3.3462 | 54.0305 | 0.0052 | 0.0100 |
| 2024_09_20 22:00 | 3235884 | 11 | 6.4638 | 9.7242 | -114.8845 | 3.9527 | 52.2842 | 0.0001 | 0.0063 |
| 2024_09_20 22:00 | 3232644 | 12 | 14.9354 | 11.1216 | -115.0570 | 4.6365 | 20.5985 | 0.0184 | 0.0135 |
| 2024_09_20 22:00 | 3221298 | 13 | 9.8302 | 17.7927 | -115.1933 | 3.1183 | 23.2394 | 0.0020 | 0.0191 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414623_7FF34716 | 152650 | 932 | -96.9 | 152650 | 778 | -97.7 | 152650 | 133 | -102.5 | 152650 | 402 |
| MR_1774414623_54A5CC49 | 152650 | 932 | -96.9 | 152650 | 778 | -98.0 | 152650 | 133 | -102.3 | 152650 | 402 |
| MR_1774414623_53F86D9A | 152650 | 932 | -95.9 | 152650 | 778 | -99.9 | 152650 | 133 | -103.8 | 152650 | 402 |
| MR_1774414623_7CA234E0 | 152650 | 932 | -95.4 | 152650 | 778 | -100.3 | 152650 | 133 | -104.5 | 152650 | 402 |
| MR_1774414623_6CC95564 | 504990 | 65 | -96.0 | 504990 | 429 | -93.5 | 504990 | 152 | -97.2 | 504990 | 228 |
| MR_1774414623_8A9644B0 | 152650 | 932 | -95.0 | 152650 | 778 | -97.4 | 152650 | 133 | -103.6 | 152650 | 402 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 271: `27ec44ed-284...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `27ec44ed-2846-4331-a650-b82688e0bc93` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[271] topology](images/test_0271.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3217951_3 by 6 degrees
- `C2`: Insufficient data; more data is needed for judgment.
- `C3`: Adjust the azimuth of 3261303_2 by 50 degrees
- `C4`: Decrease transmission power for 3217951_3
- `C5`: Press down the tilt angle  of 3261303_2 by 10 degrees
- `C6`: Increase A3 Offset threshold for 3261303_2
- `C7`: Increase transmission power for 3261303_2
- `C8`: Adjust the azimuth of 3217951_3 by 50 degrees
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3217951_3
- `C10`: Decrease A3 Offset threshold for 3217951_3
- `C11`: Increase A3 Offset threshold for 3217951_3
- `C12`: Lift the tilt angle  of 3261303_2 by 10 degrees
- `C13`: Increase transmission power for 3217951_3
- `C14`: Check test server and transmission issues
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3217951_3
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3261303_2
- `C17`: Decrease transmission power for 3261303_2
- `C18`: Lift the tilt angle of 3217951_3 by 6 degrees
- `C19`: Add neighbor relationship between 3217951_3 and 3261303_2
- `C20`: Add neighbor relationship between 3279473_4 and 3261303_2
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3261303_2
- `C22`: Decrease A3 Offset threshold for 3261303_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.325 | MS1 | 121.4656640631 | 31.1446221422 | 237 | 504990 | -89.21 | 15.61 | 300.29 | 0.12 | 2.36 | 1584 |
| 2024-09-20 22:21:32.163 | MS1 | 121.4656686330 | 31.1446307477 | 237 | 504990 | -90.89 | 12.59 | 340.60 | 0.18 | 2.08 | 1595 |
| 2024-09-20 22:21:33.437 | MS1 | 121.4656766238 | 31.1446265818 | 237 | 504990 | -90.88 | 12.74 | 492.85 | 0.06 | 2.62 | 1582 |
| 2024-09-20 22:21:34.396 | MS1 | 121.4656695775 | 31.1446243064 | 237 | 504990 | -90.56 | 13.18 | 71.13 | 0.16 | 2.45 | 359 |
| 2024-09-20 22:21:35.599 | MS1 | 121.4656619535 | 31.1446329640 | 237 | 504990 | -90.48 | 13.26 | 43.00 | 0.16 | 2.59 | 371 |
| 2024-09-20 22:21:36.413 | MS1 | 121.4656692746 | 31.1446330578 | 237 | 504990 | -91.10 | 13.91 | 52.35 | 0.13 | 2.44 | 490 |
| 2024-09-20 22:21:37.816 | MS1 | 121.4656687330 | 31.1446264564 | 237 | 504990 | -92.53 | 10.72 | 62.36 | 0.07 | 2.62 | 472 |
| 2024-09-20 22:21:38.931 | MS1 | 121.4656595515 | 31.1446253860 | 237 | 504990 | -93.05 | 9.95 | 72.08 | 0.06 | 2.80 | 491 |
| 2024-09-20 22:21:39.283 | MS1 | 121.4656695115 | 31.1446286230 | 237 | 504990 | -92.74 | 10.92 | 63.71 | 0.19 | 2.92 | 385 |
| 2024-09-20 22:21:40.523 | MS1 | 121.4656709692 | 31.1446356337 | 237 | 504990 | -90.11 | 9.06 | 416.69 | 0.10 | 2.08 | 1591 |
| 2024-09-20 22:21:41.689 | MS1 | 121.4656769485 | 31.1446337066 | 237 | 504990 | -90.57 | 10.85 | 386.10 | 0.05 | 2.95 | 1586 |
| 2024-09-20 22:21:42.573 | MS1 | 121.4656595556 | 31.1446190776 | 237 | 504990 | -91.97 | 9.11 | 310.36 | 0.17 | 2.82 | 1572 |

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
| 3217951 | 3 | 121.4743079718 | 31.1527470587 | 306 | 4 | 1 | 33.3 | TDD | 237 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3261303 | 2 | 121.4692561573 | 31.1463640842 | 332 | 15 | 0 | 47.2 | TDD | 932 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3262906 | 1 | 121.4705300284 | 31.1531253312 | 346 | 3 | 2 | 49.9 | TDD | 873 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3279473 | 4 | 121.4703578864 | 31.1554378698 | 220 | 8 | 7 | 39.1 | TDD | 870 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |

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
| 2024-09-20 22:21:31.448 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.473 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.583 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.583 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.275 | NREventA3 | measId:2;ServCellPCI:974;Se... |
| 2024-09-20 22:21:38.515 | NRHandoverAttempt | SourcePCI:974;SourceNR-ARFC... |
| 2024-09-20 22:21:38.552 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.565 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.687 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.687 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3262906 | 1 | 10.1664 | 14.2243 | -117.6744 | 13.8932 | 161.2792 | 0.0068 | 0.0069 |
| 2024_09_20 22:00 | 3261303 | 2 | 10.4322 | 5.7529 | -114.9383 | 12.2425 | 97.3672 | 0.0119 | 0.0180 |
| 2024_09_20 22:00 | 3217951 | 3 | 16.4677 | 10.0863 | -114.6099 | 12.1204 | 119.1006 | 0.0046 | 0.0184 |
| 2024_09_20 22:00 | 3279473 | 4 | 8.2904 | 11.2523 | -115.0179 | 9.5029 | 146.9215 | 0.0045 | 0.0182 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414693_E4D1EBC4 | 504990 | 237 | -89.0 | 504990 | 932 | -97.3 | 504990 | 870 | -101.4 | 504990 | 873 |
| MR_1774414693_4F3F0BA0 | 504990 | 237 | -91.2 | 504990 | 932 | -100.8 | 504990 | 870 | -101.3 | 504990 | 873 |
| MR_1774414693_624538CC | 504990 | 237 | -91.9 | 504990 | 932 | -98.6 | 504990 | 870 | -99.3 | 504990 | 873 |
| MR_1774414693_F231AAA8 | 504990 | 237 | -90.7 | 504990 | 932 | -97.7 | 504990 | 870 | -100.9 | 504990 | 873 |
| MR_1774414693_0B9D236E | 504990 | 237 | -91.0 | 504990 | 932 | -100.9 | 504990 | 870 | -101.5 | 504990 | 873 |
| MR_1774414693_FFFF09CD | 504990 | 237 | -92.0 | 504990 | 932 | -100.1 | 504990 | 870 | -101.6 | 504990 | 873 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 272: `c48c772c-6ca...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `c48c772c-6cac-46c5-bdbd-e3d695ac6178` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[272] topology](images/test_0272.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3212857_2
- `C2`: Decrease A3 Offset threshold for 3212857_2
- `C3`: Lift the tilt angle  of 3212857_2 by 10 degrees
- `C4`: Check test server and transmission issues
- `C5`: Decrease transmission power for 3212857_2
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3279869_3
- `C7`: Increase transmission power for 3279869_3
- `C8`: Press down the tilt angle  of 3212857_2 by 10 degrees
- `C9`: Adjust the azimuth of 3212857_2 by 50 degrees
- `C10`: Decrease transmission power for 3279869_3
- `C11`: Press down the tilt angle of 3279869_3 by 4 degrees
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3212857_2
- `C13`: Add neighbor relationship between 3258425_1 and 3212857_2
- `C14`: Adjust the azimuth of 3279869_3 by 2 degrees
- `C15`: Add neighbor relationship between 3279869_3 and 3212857_2
- `C16`: Increase A3 Offset threshold for 3279869_3
- `C17`: Decrease A3 Offset threshold for 3279869_3
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3279869_3
- `C19`: Increase transmission power for 3212857_2
- `C20`: Insufficient data; more data is needed for judgment.
- `C21`: Increase A3 Offset threshold for 3212857_2
- `C22`: Lift the tilt angle of 3279869_3 by 4 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.765 | MS1 | 121.4656630556 | 31.1446341602 | 781 | 504990 | -87.19 | 17.71 | 331.76 | 0.13 | 2.49 | 1567 |
| 2024-09-20 22:21:32.875 | MS1 | 121.4656687402 | 31.1446330611 | 781 | 504990 | -88.38 | 13.89 | 601.88 | 0.16 | 2.98 | 1595 |
| 2024-09-20 22:21:33.207 | MS1 | 121.4656636561 | 31.1446330990 | 781 | 504990 | -85.92 | 15.37 | 343.83 | 0.13 | 2.51 | 1584 |
| 2024-09-20 22:21:34.575 | MS1 | 121.4656765757 | 31.1446211804 | 781 | 504990 | -85.47 | 13.12 | 82.89 | 0.18 | 2.94 | 332 |
| 2024-09-20 22:21:35.779 | MS1 | 121.4656761003 | 31.1446363819 | 781 | 504990 | -87.68 | 14.55 | 59.89 | 0.04 | 2.04 | 500 |
| 2024-09-20 22:21:36.587 | MS1 | 121.4656772477 | 31.1446269529 | 781 | 504990 | -85.73 | 17.02 | 93.37 | 0.14 | 2.43 | 497 |
| 2024-09-20 22:21:37.162 | MS1 | 121.4656660377 | 31.1446197687 | 781 | 504990 | -89.27 | 8.55 | 71.39 | 0.01 | 2.77 | 458 |
| 2024-09-20 22:21:38.392 | MS1 | 121.4656636355 | 31.1446193319 | 781 | 504990 | -89.31 | 7.03 | 92.10 | 0.20 | 2.24 | 453 |
| 2024-09-20 22:21:39.285 | MS1 | 121.4656765279 | 31.1446199747 | 781 | 504990 | -90.87 | 10.87 | 78.66 | 0.18 | 2.71 | 429 |
| 2024-09-20 22:21:40.373 | MS1 | 121.4656658841 | 31.1446291256 | 781 | 504990 | -93.43 | 8.81 | 522.33 | 0.00 | 2.13 | 1577 |
| 2024-09-20 22:21:41.437 | MS1 | 121.4656705730 | 31.1446327374 | 781 | 504990 | -93.26 | 9.72 | 485.63 | 0.04 | 2.42 | 1596 |
| 2024-09-20 22:21:42.129 | MS1 | 121.4656689748 | 31.1446236137 | 781 | 504990 | -90.29 | 8.13 | 529.94 | 0.16 | 2.32 | 1570 |

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
| 3212857 | 2 | 121.4701167144 | 31.1463911617 | 322 | 15 | 2 | 46.3 | TDD | 683 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3231299 | 4 | 121.4657215819 | 31.1538360453 | 164 | 11 | 2 | 43.2 | TDD | 766 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3258425 | 1 | 121.4681819142 | 31.1506812234 | 80 | 15 | 4 | 22.7 | TDD | 752 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3279869 | 3 | 121.4655449811 | 31.1541432029 | 181 | 1 | 1 | 49.1 | TDD | 781 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |

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
| 2024-09-20 22:21:31.044 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.068 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.184 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.184 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.870 | NREventA3 | measId:2;ServCellPCI:572;Se... |
| 2024-09-20 22:21:38.110 | NRHandoverAttempt | SourcePCI:572;SourceNR-ARFC... |
| 2024-09-20 22:21:38.153 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.163 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.299 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.299 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3258425 | 1 | 11.8615 | 15.9446 | -116.0289 | 8.0736 | 160.2444 | 0.0130 | 0.0047 |
| 2024_09_20 22:00 | 3212857 | 2 | 11.6790 | 15.7247 | -114.0469 | 15.9867 | 121.6964 | 0.0163 | 0.0073 |
| 2024_09_20 22:00 | 3279869 | 3 | 18.8601 | 6.4242 | -116.7829 | 6.7390 | 111.8121 | 0.0001 | 0.0171 |
| 2024_09_20 22:00 | 3231299 | 4 | 12.9726 | 12.6324 | -115.3541 | 5.7505 | 124.5577 | 0.0076 | 0.0002 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413433_FF22DCDC | 504990 | 781 | -84.7 | 504990 | 683 | -91.9 | 504990 | 752 | -99.6 | 504990 | 766 |
| MR_1774413433_E96E3F1E | 504990 | 781 | -84.5 | 504990 | 683 | -91.6 | 504990 | 752 | -97.0 | 504990 | 766 |
| MR_1774413433_BBE5E4FC | 504990 | 781 | -83.6 | 504990 | 683 | -91.0 | 504990 | 752 | -97.1 | 504990 | 766 |
| MR_1774413433_B1D3AA77 | 504990 | 781 | -85.2 | 504990 | 683 | -89.3 | 504990 | 752 | -99.5 | 504990 | 766 |
| MR_1774413433_6804504D | 504990 | 781 | -87.0 | 504990 | 683 | -88.0 | 504990 | 752 | -98.9 | 504990 | 766 |
| MR_1774413433_8478EDCC | 504990 | 781 | -86.4 | 504990 | 683 | -88.9 | 504990 | 752 | -96.9 | 504990 | 766 |
| MR_1774413433_533ABC20 | 504990 | 781 | -87.3 | 504990 | 683 | -91.7 | 504990 | 752 | -98.7 | 504990 | 766 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 273: `3f1e8a1c-33c...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `3f1e8a1c-33c3-42fd-a216-8d9904a27e6b` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[273] topology](images/test_0273.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3251000_1
- `C2`: Adjust the azimuth of 3232379_4 by 50 degrees
- `C3`: Decrease transmission power for 3232379_4
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3232379_4
- `C5`: Decrease A3 Offset threshold for 3251000_1
- `C6`: Press down the tilt angle of 3232379_4 by 10 degrees
- `C7`: Add neighbor relationship between 3232379_4 and 3251000_1
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3232379_4
- `C9`: Check test server and transmission issues
- `C10`: Press down the tilt angle  of 3251000_1 by 10 degrees
- `C11`: Increase A3 Offset threshold for 3251000_1
- `C12`: Decrease transmission power for 3251000_1
- `C13`: Decrease A3 Offset threshold for 3232379_4
- `C14`: Adjust the azimuth of 3251000_1 by 50 degrees
- `C15`: Add neighbor relationship between 3217115_3 and 3251000_1
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3251000_1
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3251000_1
- `C18`: Increase A3 Offset threshold for 3232379_4
- `C19`: Insufficient data; more data is needed for judgment.
- `C20`: Increase transmission power for 3232379_4
- `C21`: Lift the tilt angle of 3232379_4 by 10 degrees
- `C22`: Lift the tilt angle  of 3251000_1 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.538 | MS1 | 121.4656721307 | 31.1446208106 | 526 | 504990 | -91.66 | 12.13 | 434.69 | 0.11 | 2.63 | 1591 |
| 2024-09-20 22:21:32.978 | MS1 | 121.4656671053 | 31.1446379659 | 526 | 504990 | -90.18 | 16.36 | 536.92 | 0.12 | 2.56 | 1588 |
| 2024-09-20 22:21:33.737 | MS1 | 121.4656663791 | 31.1446211038 | 526 | 504990 | -87.45 | 17.01 | 449.36 | 0.18 | 2.14 | 1593 |
| 2024-09-20 22:21:34.540 | MS1 | 121.4656580957 | 31.1446309122 | 526 | 504990 | -85.02 | 17.23 | 45.02 | 0.08 | 2.05 | 473 |
| 2024-09-20 22:21:35.334 | MS1 | 121.4656690205 | 31.1446276596 | 526 | 504990 | -86.17 | 12.53 | 73.42 | 0.10 | 2.71 | 485 |
| 2024-09-20 22:21:36.825 | MS1 | 121.4656689249 | 31.1446379009 | 526 | 504990 | -86.75 | 13.69 | 63.07 | 0.12 | 2.54 | 366 |
| 2024-09-20 22:21:37.215 | MS1 | 121.4656694970 | 31.1446192486 | 526 | 504990 | -89.69 | 11.81 | 99.23 | 0.11 | 2.54 | 300 |
| 2024-09-20 22:21:38.145 | MS1 | 121.4656629870 | 31.1446273150 | 526 | 504990 | -92.32 | 10.87 | 61.36 | 0.02 | 2.29 | 382 |
| 2024-09-20 22:21:39.828 | MS1 | 121.4656656866 | 31.1446259745 | 526 | 504990 | -89.90 | 9.47 | 101.71 | 0.09 | 2.39 | 328 |
| 2024-09-20 22:21:40.584 | MS1 | 121.4656770245 | 31.1446268621 | 526 | 504990 | -92.95 | 11.07 | 478.39 | 0.14 | 2.41 | 1566 |
| 2024-09-20 22:21:41.339 | MS1 | 121.4656736496 | 31.1446354767 | 526 | 504990 | -92.62 | 8.76 | 576.42 | 0.17 | 2.54 | 1573 |
| 2024-09-20 22:21:42.861 | MS1 | 121.4656618438 | 31.1446184952 | 526 | 504990 | -92.84 | 11.12 | 338.50 | 0.14 | 2.60 | 1595 |

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
| 3217115 | 3 | 121.4737584609 | 31.1536427981 | 318 | 0 | 10 | 37.3 | TDD | 958 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3232379 | 4 | 121.4641730070 | 31.1532157665 | 121 | 15 | 0 | 46.1 | TDD | 526 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3251000 | 1 | 121.4644132776 | 31.1477324829 | 280 | 7 | 9 | 27.3 | TDD | 488 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3264917 | 2 | 121.4705211230 | 31.1523280486 | 19 | 2 | 10 | 15.9 | TDD | 314 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |

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
| 2024-09-20 22:21:30.788 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.807 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:30.950 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.950 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.680 | NREventA3 | measId:2;ServCellPCI:572;Se... |
| 2024-09-20 22:21:37.920 | NRHandoverAttempt | SourcePCI:572;SourceNR-ARFC... |
| 2024-09-20 22:21:37.963 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.976 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.094 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.094 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3251000 | 1 | 10.4393 | 16.7898 | -115.1002 | 12.7538 | 134.0725 | 0.0161 | 0.0062 |
| 2024_09_20 22:00 | 3264917 | 2 | 6.5042 | 19.3062 | -116.0418 | 17.1067 | 109.7489 | 0.0102 | 0.0198 |
| 2024_09_20 22:00 | 3217115 | 3 | 13.0053 | 8.6927 | -116.0473 | 8.4042 | 151.2342 | 0.0042 | 0.0118 |
| 2024_09_20 22:00 | 3232379 | 4 | 10.7960 | 16.4757 | -117.4974 | 7.7898 | 162.9874 | 0.0188 | 0.0152 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412038_84EF4CB1 | 504990 | 526 | -86.2 | 504990 | 488 | -89.0 | 504990 | 958 | -95.5 | 504990 | 314 |
| MR_1774412038_AE56AC15 | 504990 | 526 | -85.6 | 504990 | 488 | -85.6 | 504990 | 958 | -94.4 | 504990 | 314 |
| MR_1774412038_B6FB7D8A | 504990 | 526 | -84.9 | 504990 | 488 | -87.2 | 504990 | 958 | -96.7 | 504990 | 314 |
| MR_1774412038_5A2FDAE4 | 504990 | 526 | -84.3 | 504990 | 488 | -89.2 | 504990 | 958 | -96.2 | 504990 | 314 |
| MR_1774412038_1AAE9D0B | 504990 | 526 | -86.6 | 504990 | 488 | -85.6 | 504990 | 958 | -97.4 | 504990 | 314 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 274: `7ebb3374-b85...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `7ebb3374-b857-43a3-9930-9359212530dd` |
| Tag | **multiple-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[274] topology](images/test_0274.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle  of 3260870_3 by 3 degrees
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3279566_1
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3260870_3
- `C4`: Insufficient data; more data is needed for judgment.
- `C5`: Add neighbor relationship between 3263193_2 and 3260870_3
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3260870_3
- `C7`: Add neighbor relationship between 3279566_1 and 3260870_3
- `C8`: Increase transmission power for 3260870_3
- `C9`: Decrease transmission power for 3279566_1
- `C10`: Increase A3 Offset threshold for 3279566_1
- `C11`: Decrease transmission power for 3260870_3
- `C12`: Increase transmission power for 3279566_1
- `C13`: Increase A3 Offset threshold for 3260870_3
- `C14`: Decrease A3 Offset threshold for 3279566_1
- `C15`: Press down the tilt angle of 3279566_1 by 4 degrees
- `C16`: Decrease A3 Offset threshold for 3260870_3
- `C17`: Press down the tilt angle  of 3260870_3 by 3 degrees
- `C18`: Adjust the azimuth of 3260870_3 by 24 degrees
- `C19`: Check test server and transmission issues
- `C20`: Lift the tilt angle of 3279566_1 by 4 degrees
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3279566_1
- `C22`: Adjust the azimuth of 3279566_1 by 48 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.944 | MS1 | 121.4656698256 | 31.1446189286 | 457 | 504990 | -82.16 | 13.19 | 580.77 | 0.19 | 2.75 | 1562 |
| 2024-09-20 22:21:32.357 | MS1 | 121.4656773590 | 31.1446322172 | 457 | 504990 | -83.74 | 15.75 | 423.94 | 0.19 | 2.60 | 1586 |
| 2024-09-20 22:21:33.325 | MS1 | 121.4656684012 | 31.1446341025 | 457 | 504990 | -81.73 | 16.97 | 509.13 | 0.03 | 2.26 | 1565 |
| 2024-09-20 22:21:34.893 | MS1 | 121.4656627075 | 31.1446353545 | 457 | 504990 | -92.49 | 2.88 | 69.12 | 0.01 | 1.40 | 1572 |
| 2024-09-20 22:21:35.457 | MS1 | 121.4656723643 | 31.1446245116 | 457 | 504990 | -90.17 | 1.95 | 87.00 | 0.03 | 1.49 | 1569 |
| 2024-09-20 22:21:36.811 | MS1 | 121.4656758546 | 31.1446378949 | 457 | 504990 | -90.83 | 0.46 | 75.95 | 0.06 | 1.07 | 1581 |
| 2024-09-20 22:21:37.498 | MS1 | 121.4656697271 | 31.1446241008 | 457 | 504990 | -94.31 | 2.53 | 70.84 | 0.09 | 1.18 | 1569 |
| 2024-09-20 22:21:38.674 | MS1 | 121.4656719140 | 31.1446299000 | 457 | 504990 | -87.95 | 0.29 | 90.10 | 0.05 | 1.11 | 1599 |
| 2024-09-20 22:21:39.811 | MS1 | 121.4656665481 | 31.1446349086 | 457 | 504990 | -85.22 | 3.40 | 57.77 | 0.06 | 1.09 | 1586 |
| 2024-09-20 22:21:40.349 | MS1 | 121.4656594787 | 31.1446259874 | 457 | 504990 | -77.12 | 17.31 | 458.41 | 0.13 | 2.63 | 1583 |
| 2024-09-20 22:21:41.363 | MS1 | 121.4656592950 | 31.1446302939 | 457 | 504990 | -82.95 | 17.70 | 354.00 | 0.03 | 2.67 | 1598 |
| 2024-09-20 22:21:42.932 | MS1 | 121.4656643007 | 31.1446258937 | 457 | 504990 | -78.07 | 14.70 | 566.56 | 0.10 | 2.52 | 1599 |

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
| 3241278 | 4 | 121.4662510382 | 31.1456792094 | 308 | 4 | 7 | 36.0 | TDD | 84 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3260870 | 3 | 121.4747476644 | 31.1515148342 | 204 | 2 | 3 | 16.8 | TDD | 621 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3263193 | 2 | 121.4697051846 | 31.1544011073 | 243 | 0 | 3 | 20.6 | TDD | 340 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3279566 | 1 | 121.4672327194 | 31.1472626008 | 159 | 1 | 6 | 15.9 | TDD | 457 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:31.596 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.621 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.766 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.766 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3279566 | 1 | 12.8530 | 19.4141 | -109.4511 | 14.8559 | 86.1185 | 0.0104 | 0.0093 |
| 2024_09_20 22:00 | 3263193 | 2 | 13.4066 | 9.8591 | -115.8757 | 17.7692 | 91.7749 | 0.0122 | 0.0182 |
| 2024_09_20 22:00 | 3260870 | 3 | 13.2847 | 12.5655 | -114.2970 | 14.1485 | 122.0704 | 0.0095 | 0.0137 |
| 2024_09_20 22:00 | 3241278 | 4 | 7.3570 | 5.3857 | -115.2773 | 10.1296 | 177.5757 | 0.0044 | 0.0190 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415283_CC57AF2B | 504990 | 457 | -92.3 | 504990 | 621 | -87.0 | 504990 | 340 | -95.6 | 504990 | 84 |
| MR_1774415283_A47AF4BA | 504990 | 457 | -90.6 | 504990 | 621 | -89.8 | 504990 | 340 | -96.3 | 504990 | 84 |
| MR_1774415283_D81F72B7 | 504990 | 457 | -94.1 | 504990 | 621 | -87.9 | 504990 | 340 | -95.7 | 504990 | 84 |
| MR_1774415283_6CEEDF25 | 504990 | 457 | -92.3 | 504990 | 621 | -86.9 | 504990 | 340 | -96.5 | 504990 | 84 |
| MR_1774415283_593298B0 | 504990 | 457 | -94.3 | 504990 | 621 | -89.9 | 504990 | 340 | -93.6 | 504990 | 84 |
| MR_1774415283_61CBBD4D | 504990 | 621 | -94.3 | 504990 | 457 | -89.5 | 504990 | 340 | -96.0 | 504990 | 84 |
| MR_1774415283_408CA82C | 504990 | 457 | -94.2 | 504990 | 621 | -90.0 | 504990 | 340 | -96.1 | 504990 | 84 |
| MR_1774415283_C1AD9476 | 504990 | 457 | -93.3 | 504990 | 621 | -88.9 | 504990 | 340 | -94.2 | 504990 | 84 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 275: `419dfe03-35a...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `419dfe03-35a4-44d7-a391-06b90de41872` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[275] topology](images/test_0275.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3271649_4 by 10 degrees
- `C2`: Increase transmission power for 3230086_1
- `C3`: Press down the tilt angle  of 3230086_1 by 2 degrees
- `C4`: Lift the tilt angle  of 3230086_1 by 2 degrees
- `C5`: Decrease A3 Offset threshold for 3230086_1
- `C6`: Adjust the azimuth of 3271649_4 by 39 degrees
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3230086_1
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3271649_4
- `C9`: Press down the tilt angle of 3271649_4 by 10 degrees
- `C10`: Decrease transmission power for 3230086_1
- `C11`: Decrease A3 Offset threshold for 3271649_4
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3271649_4
- `C13`: Adjust the azimuth of 3230086_1 by 25 degrees
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Decrease transmission power for 3271649_4
- `C16`: Check test server and transmission issues
- `C17`: Increase transmission power for 3271649_4
- `C18`: Add neighbor relationship between 3271649_4 and 3230086_1
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3230086_1
- `C20`: Add neighbor relationship between 3243152_3 and 3230086_1
- `C21`: Increase A3 Offset threshold for 3271649_4
- `C22`: Increase A3 Offset threshold for 3230086_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.433 | MS1 | 121.4656584408 | 31.1446200331 | 566 | 504990 | -77.50 | 12.90 | 330.91 | 0.16 | 2.57 | 1600 |
| 2024-09-20 22:21:32.815 | MS1 | 121.4656627985 | 31.1446193917 | 566 | 504990 | -77.25 | 17.18 | 374.11 | 0.12 | 2.04 | 1562 |
| 2024-09-20 22:21:33.862 | MS1 | 121.4656689699 | 31.1446192498 | 566 | 504990 | -83.80 | 14.74 | 511.58 | 0.11 | 2.28 | 1592 |
| 2024-09-20 22:21:34.761 | MS1 | 121.4656637052 | 31.1446357236 | 566 | 504990 | -89.57 | -2.77 | 32.76 | 0.05 | 1.46 | 1569 |
| 2024-09-20 22:21:35.519 | MS1 | 121.4656584753 | 31.1446234899 | 566 | 504990 | -86.83 | -1.89 | 73.50 | 0.09 | 1.10 | 1564 |
| 2024-09-20 22:21:36.636 | MS1 | 121.4656701686 | 31.1446358104 | 566 | 504990 | -85.47 | -3.77 | 33.19 | 0.09 | 1.14 | 1584 |
| 2024-09-20 22:21:37.758 | MS1 | 121.4656665559 | 31.1446343552 | 566 | 504990 | -92.20 | -0.66 | 34.76 | 0.05 | 1.22 | 1564 |
| 2024-09-20 22:21:38.470 | MS1 | 121.4656645034 | 31.1446374547 | 566 | 504990 | -78.00 | 12.24 | 552.92 | 0.04 | 1.11 | 1592 |
| 2024-09-20 22:21:39.535 | MS1 | 121.4656606659 | 31.1446357841 | 566 | 504990 | -78.56 | 15.07 | 349.00 | 0.03 | 1.01 | 1573 |
| 2024-09-20 22:21:40.234 | MS1 | 121.4656774958 | 31.1446360198 | 566 | 504990 | -81.36 | 16.59 | 434.33 | 0.05 | 2.55 | 1581 |
| 2024-09-20 22:21:41.392 | MS1 | 121.4656689207 | 31.1446197050 | 566 | 504990 | -84.82 | 14.21 | 309.44 | 0.05 | 2.49 | 1598 |
| 2024-09-20 22:21:42.448 | MS1 | 121.4656710979 | 31.1446331015 | 566 | 504990 | -81.70 | 17.63 | 425.76 | 0.01 | 2.88 | 1596 |

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
| 3230086 | 1 | 121.4754860119 | 31.1464089603 | 233 | 1 | 4 | 18.3 | TDD | 192 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3243152 | 3 | 121.4717679828 | 31.1456012520 | 274 | 14 | 12 | 47.5 | TDD | 558 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3271649 | 4 | 121.4643889576 | 31.1509641034 | 209 | 7 | 2 | 42.1 | TDD | 566 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3273942 | 2 | 121.4712777987 | 31.1443226811 | 1 | 1 | 3 | 23.5 | TDD | 385 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:30.805 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.826 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:30.953 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.953 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.619 | NREventA3 | measId:2;ServCellPCI:484;Se... |
| 2024-09-20 22:21:35.619 | NREventA3 | measId:2;ServCellPCI:484;Se... |
| 2024-09-20 22:21:36.619 | NREventA3 | measId:2;ServCellPCI:484;Se... |
| 2024-09-20 22:21:39.119 | NRRRCReestablishAttempt | PCI:484 |
| 2024-09-20 22:21:39.133 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.145 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:39.291 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.291 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3230086 | 1 | 8.4678 | 16.4193 | -117.2379 | 18.2375 | 167.9271 | 0.0047 | 0.0113 |
| 2024_09_20 22:00 | 3273942 | 2 | 17.1931 | 9.0945 | -115.3596 | 17.8659 | 91.5746 | 0.0017 | 0.0098 |
| 2024_09_20 22:00 | 3243152 | 3 | 10.9920 | 7.8806 | -114.1062 | 11.9639 | 153.7906 | 0.0107 | 0.0086 |
| 2024_09_20 22:00 | 3271649 | 4 | 7.3868 | 10.3120 | -114.8005 | 5.6444 | 135.8244 | 0.0117 | 0.1607 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416087_B97B6FEB | 504990 | 192 | -84.6 | 504990 | 566 | -88.6 | 504990 | 558 | -93.7 | 504990 | 385 |
| MR_1774416087_046082A4 | 504990 | 566 | -91.3 | 504990 | 192 | -83.7 | 504990 | 558 | -91.7 | 504990 | 385 |
| MR_1774416087_C2C03F07 | 504990 | 566 | -91.5 | 504990 | 192 | -87.1 | 504990 | 558 | -91.4 | 504990 | 385 |
| MR_1774416087_47100C7B | 504990 | 566 | -89.6 | 504990 | 192 | -85.7 | 504990 | 558 | -92.3 | 504990 | 385 |
| MR_1774416087_77165330 | 504990 | 192 | -84.6 | 504990 | 566 | -91.4 | 504990 | 558 | -91.1 | 504990 | 385 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 276: `bce6d685-3e1...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `bce6d685-3e1d-49e8-8cb5-3b98dc4774ff` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[276] topology](images/test_0276.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3273200_2
- `C2`: Increase transmission power for 3273200_2
- `C3`: Decrease A3 Offset threshold for 3215266_4
- `C4`: Press down the tilt angle  of 3215266_4 by 5 degrees
- `C5`: Increase transmission power for 3215266_4
- `C6`: Insufficient data; more data is needed for judgment.
- `C7`: Adjust the azimuth of 3215266_4 by 50 degrees
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3215266_4
- `C9`: Decrease transmission power for 3273200_2
- `C10`: Press down the tilt angle of 3273200_2 by 5 degrees
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3273200_2
- `C12`: Check test server and transmission issues
- `C13`: Decrease A3 Offset threshold for 3273200_2
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3215266_4
- `C15`: Decrease transmission power for 3215266_4
- `C16`: Lift the tilt angle  of 3215266_4 by 5 degrees
- `C17`: Lift the tilt angle of 3273200_2 by 5 degrees
- `C18`: Add neighbor relationship between 3273200_2 and 3215266_4
- `C19`: Adjust the azimuth of 3273200_2 by 41 degrees
- `C20`: Increase A3 Offset threshold for 3273200_2
- `C21`: Increase A3 Offset threshold for 3215266_4
- `C22`: Add neighbor relationship between 3235786_3 and 3215266_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.366 | MS1 | 121.4656642726 | 31.1446198670 | 281 | 504990 | -90.17 | 15.18 | 354.17 | 0.15 | 2.74 | 1589 |
| 2024-09-20 22:21:32.735 | MS1 | 121.4656644905 | 31.1446348414 | 281 | 504990 | -90.80 | 14.67 | 387.63 | 0.06 | 2.74 | 1595 |
| 2024-09-20 22:21:33.844 | MS1 | 121.4656714827 | 31.1446257225 | 281 | 504990 | -91.80 | 16.56 | 356.60 | 0.18 | 2.51 | 1577 |
| 2024-09-20 22:21:34.475 | MS1 | 121.4656613837 | 31.1446353887 | 281 | 504990 | -88.82 | 13.28 | 80.77 | 0.67 | 2.01 | 541 |
| 2024-09-20 22:21:35.717 | MS1 | 121.4656632485 | 31.1446240450 | 281 | 504990 | -87.77 | 17.03 | 83.14 | 0.59 | 2.18 | 633 |
| 2024-09-20 22:21:36.280 | MS1 | 121.4656599401 | 31.1446305176 | 281 | 504990 | -87.85 | 17.87 | 67.21 | 0.67 | 2.70 | 626 |
| 2024-09-20 22:21:37.592 | MS1 | 121.4656640931 | 31.1446257247 | 281 | 504990 | -90.49 | 10.64 | 100.90 | 0.57 | 2.22 | 507 |
| 2024-09-20 22:21:38.372 | MS1 | 121.4656620096 | 31.1446187769 | 281 | 504990 | -89.86 | 11.43 | 95.62 | 0.55 | 2.10 | 592 |
| 2024-09-20 22:21:39.406 | MS1 | 121.4656630342 | 31.1446298953 | 281 | 504990 | -92.19 | 7.11 | 86.95 | 0.55 | 2.57 | 680 |
| 2024-09-20 22:21:40.769 | MS1 | 121.4656645921 | 31.1446275648 | 281 | 504990 | -89.47 | 10.19 | 413.64 | 0.11 | 2.05 | 1600 |
| 2024-09-20 22:21:41.151 | MS1 | 121.4656629966 | 31.1446329491 | 281 | 504990 | -89.66 | 10.39 | 400.83 | 0.01 | 2.12 | 1572 |
| 2024-09-20 22:21:42.292 | MS1 | 121.4656624366 | 31.1446195298 | 281 | 504990 | -93.58 | 9.31 | 483.35 | 0.05 | 2.77 | 1564 |

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
| 3215126 | 1 | 121.4666157914 | 31.1552698899 | 142 | 5 | 10 | 45.1 | TDD | 576 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3215266 | 4 | 121.4651929365 | 31.1559831267 | 1 | 4 | 10 | 23.5 | TDD | 747 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3235786 | 3 | 121.4657165870 | 31.1476600552 | 160 | 0 | 7 | 34.4 | TDD | 363 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3273200 | 2 | 121.4740279458 | 31.1556822814 | 254 | 4 | 11 | 36.7 | TDD | 281 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:31.324 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.342 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.463 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.463 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.128 | NREventA3 | measId:2;ServCellPCI:430;Se... |
| 2024-09-20 22:21:38.368 | NRHandoverAttempt | SourcePCI:430;SourceNR-ARFC... |
| 2024-09-20 22:21:38.410 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.425 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.528 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.528 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3215126 | 1 | 10.6088 | 5.6828 | -116.1274 | 16.7614 | 103.6167 | 0.0101 | 0.0133 |
| 2024_09_20 22:00 | 3273200 | 2 | 12.9336 | 19.7154 | -117.5378 | 12.3799 | 99.8616 | 0.0001 | 0.0112 |
| 2024_09_20 22:00 | 3235786 | 3 | 11.8747 | 6.4461 | -117.2222 | 18.1566 | 132.9689 | 0.0174 | 0.0023 |
| 2024_09_20 22:00 | 3215266 | 4 | 12.3234 | 19.6378 | -115.9453 | 13.5389 | 176.4349 | 0.0168 | 0.0199 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412433_E7593B44 | 504990 | 281 | -89.0 | 504990 | 747 | -97.4 | 504990 | 363 | -99.4 | 504990 | 576 |
| MR_1774412433_1B5B349A | 504990 | 281 | -89.5 | 504990 | 747 | -98.8 | 504990 | 363 | -101.7 | 504990 | 576 |
| MR_1774412433_DB380932 | 504990 | 281 | -90.5 | 504990 | 747 | -99.0 | 504990 | 363 | -101.3 | 504990 | 576 |
| MR_1774412433_01F302AF | 504990 | 281 | -90.8 | 504990 | 747 | -99.6 | 504990 | 363 | -101.2 | 504990 | 576 |
| MR_1774412433_D667E60A | 504990 | 281 | -88.0 | 504990 | 747 | -98.1 | 504990 | 363 | -101.3 | 504990 | 576 |
| MR_1774412433_F6EFD517 | 504990 | 281 | -88.2 | 504990 | 747 | -98.8 | 504990 | 363 | -101.1 | 504990 | 576 |
| MR_1774412433_8708B2B5 | 504990 | 281 | -87.6 | 504990 | 747 | -100.1 | 504990 | 363 | -100.7 | 504990 | 576 |
| MR_1774412433_60DBAF9D | 504990 | 281 | -87.2 | 504990 | 747 | -100.1 | 504990 | 363 | -99.0 | 504990 | 576 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 277: `e233b67c-f5f...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `e233b67c-f5f4-409f-bf94-9f7fb9cb9497` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[277] topology](images/test_0277.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3259133_2 by 50 degrees
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3259133_2
- `C3`: Adjust the azimuth of 3215899_3 by 50 degrees
- `C4`: Increase A3 Offset threshold for 3215899_3
- `C5`: Lift the tilt angle of 3215899_3 by 10 degrees
- `C6`: Lift the tilt angle  of 3259133_2 by 10 degrees
- `C7`: Increase A3 Offset threshold for 3259133_2
- `C8`: Insufficient data; more data is needed for judgment.
- `C9`: Decrease A3 Offset threshold for 3215899_3
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3259133_2
- `C11`: Add neighbor relationship between 3215899_3 and 3259133_2
- `C12`: Decrease A3 Offset threshold for 3259133_2
- `C13`: Decrease transmission power for 3215899_3
- `C14`: Press down the tilt angle  of 3259133_2 by 10 degrees
- `C15`: Press down the tilt angle of 3215899_3 by 10 degrees
- `C16`: Check test server and transmission issues
- `C17`: Add neighbor relationship between 3222673_4 and 3259133_2
- `C18`: Increase transmission power for 3259133_2
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3215899_3
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3215899_3
- `C21`: Increase transmission power for 3215899_3
- `C22`: Decrease transmission power for 3259133_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.394 | MS1 | 121.4656667114 | 31.1446273149 | 774 | 504990 | -91.02 | 16.27 | 343.63 | 0.02 | 2.03 | 1563 |
| 2024-09-20 22:21:32.214 | MS1 | 121.4656605871 | 31.1446190889 | 774 | 504990 | -91.11 | 13.87 | 575.94 | 0.04 | 2.48 | 1576 |
| 2024-09-20 22:21:33.449 | MS1 | 121.4656692725 | 31.1446236808 | 774 | 504990 | -88.65 | 17.18 | 542.37 | 0.04 | 2.53 | 1561 |
| 2024-09-20 22:21:34.881 | MS1 | 121.4656671212 | 31.1446282552 | 774 | 504990 | -87.01 | 16.36 | 55.70 | 0.12 | 2.71 | 431 |
| 2024-09-20 22:21:35.406 | MS1 | 121.4656611666 | 31.1446193983 | 774 | 504990 | -90.66 | 12.53 | 50.66 | 0.15 | 2.94 | 379 |
| 2024-09-20 22:21:36.568 | MS1 | 121.4656583509 | 31.1446243549 | 774 | 504990 | -86.61 | 13.33 | 78.36 | 0.08 | 2.70 | 447 |
| 2024-09-20 22:21:37.753 | MS1 | 121.4656776019 | 31.1446281561 | 774 | 504990 | -91.84 | 11.57 | 52.47 | 0.03 | 2.25 | 331 |
| 2024-09-20 22:21:38.863 | MS1 | 121.4656676901 | 31.1446318902 | 774 | 504990 | -93.10 | 12.38 | 63.02 | 0.08 | 2.58 | 387 |
| 2024-09-20 22:21:39.919 | MS1 | 121.4656717880 | 31.1446288909 | 774 | 504990 | -91.23 | 10.19 | 50.66 | 0.08 | 2.12 | 466 |
| 2024-09-20 22:21:40.696 | MS1 | 121.4656664690 | 31.1446368142 | 774 | 504990 | -89.93 | 9.37 | 583.39 | 0.18 | 2.38 | 1566 |
| 2024-09-20 22:21:41.504 | MS1 | 121.4656663782 | 31.1446244879 | 774 | 504990 | -89.75 | 12.66 | 590.39 | 0.06 | 2.60 | 1575 |
| 2024-09-20 22:21:42.921 | MS1 | 121.4656747815 | 31.1446250405 | 774 | 504990 | -89.71 | 10.63 | 478.96 | 0.07 | 2.91 | 1575 |

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
| 3215899 | 3 | 121.4687301622 | 31.1482846697 | 8 | 14 | 5 | 24.3 | TDD | 774 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3222673 | 4 | 121.4662706228 | 31.1440165177 | 196 | 7 | 11 | 31.0 | TDD | 750 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3252692 | 1 | 121.4756916014 | 31.1469188275 | 228 | 13 | 5 | 31.2 | TDD | 680 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3259133 | 2 | 121.4665399591 | 31.1524486243 | 4 | 15 | 8 | 24.9 | TDD | 541 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |

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
| 2024-09-20 22:21:31.561 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.576 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.680 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.680 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.431 | NREventA3 | measId:2;ServCellPCI:880;Se... |
| 2024-09-20 22:21:38.671 | NRHandoverAttempt | SourcePCI:880;SourceNR-ARFC... |
| 2024-09-20 22:21:38.701 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.715 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.857 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.857 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3252692 | 1 | 14.9656 | 11.6239 | -117.7686 | 19.9276 | 89.7816 | 0.0025 | 0.0144 |
| 2024_09_20 22:00 | 3259133 | 2 | 16.8833 | 14.7461 | -114.2714 | 9.9105 | 106.8022 | 0.0117 | 0.0074 |
| 2024_09_20 22:00 | 3215899 | 3 | 16.2711 | 8.5532 | -114.6803 | 13.7793 | 142.1118 | 0.0082 | 0.0171 |
| 2024_09_20 22:00 | 3222673 | 4 | 6.0493 | 18.0700 | -115.4498 | 5.3518 | 163.8772 | 0.0197 | 0.0064 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416891_7EB69E5A | 504990 | 774 | -86.7 | 504990 | 541 | -90.3 | 504990 | 750 | -97.4 | 504990 | 680 |
| MR_1774416891_1EED5143 | 504990 | 774 | -85.3 | 504990 | 541 | -88.5 | 504990 | 750 | -94.7 | 504990 | 680 |
| MR_1774416891_F49C0AC8 | 504990 | 774 | -88.2 | 504990 | 541 | -87.6 | 504990 | 750 | -97.1 | 504990 | 680 |
| MR_1774416891_A3732476 | 504990 | 774 | -86.1 | 504990 | 541 | -87.3 | 504990 | 750 | -95.2 | 504990 | 680 |
| MR_1774416891_AE531284 | 504990 | 774 | -87.3 | 504990 | 541 | -89.1 | 504990 | 750 | -97.5 | 504990 | 680 |
| MR_1774416891_E8DF47E7 | 504990 | 774 | -87.7 | 504990 | 541 | -90.8 | 504990 | 750 | -94.9 | 504990 | 680 |
| MR_1774416891_29414AE2 | 504990 | 774 | -88.4 | 504990 | 541 | -89.8 | 504990 | 750 | -95.4 | 504990 | 680 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 278: `6d6dca89-d76...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `6d6dca89-d769-4ec6-8053-5d4b1a7481ba` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[278] topology](images/test_0278.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3221648_4
- `C2`: Add neighbor relationship between 3258370_1 and 3221648_4
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3221648_4
- `C4`: Adjust the azimuth of 3251130_3 by 41 degrees
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3221648_4
- `C6`: Press down the tilt angle  of 3221648_4 by 10 degrees
- `C7`: Adjust the azimuth of 3221648_4 by 50 degrees
- `C8`: Add neighbor relationship between 3251130_3 and 3221648_4
- `C9`: Increase A3 Offset threshold for 3251130_3
- `C10`: Lift the tilt angle  of 3221648_4 by 10 degrees
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3251130_3
- `C12`: Lift the tilt angle of 3251130_3 by 3 degrees
- `C13`: Check test server and transmission issues
- `C14`: Decrease A3 Offset threshold for 3251130_3
- `C15`: Insufficient data; more data is needed for judgment.
- `C16`: Press down the tilt angle of 3251130_3 by 3 degrees
- `C17`: Increase transmission power for 3221648_4
- `C18`: Increase transmission power for 3251130_3
- `C19`: Decrease transmission power for 3221648_4
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3251130_3
- `C21`: Decrease A3 Offset threshold for 3221648_4
- `C22`: Decrease transmission power for 3251130_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.672 | MS1 | 121.4656637311 | 31.1446211707 | 509 | 504990 | -86.58 | 17.66 | 421.79 | 0.00 | 2.30 | 1588 |
| 2024-09-20 22:21:32.208 | MS1 | 121.4656662957 | 31.1446351288 | 509 | 504990 | -88.70 | 14.71 | 430.45 | 0.01 | 2.40 | 1579 |
| 2024-09-20 22:21:33.416 | MS1 | 121.4656712508 | 31.1446214275 | 509 | 504990 | -87.39 | 15.09 | 469.10 | 0.17 | 2.17 | 1584 |
| 2024-09-20 22:21:34.515 | MS1 | 121.4656587045 | 31.1446294174 | 509 | 504990 | -89.61 | 13.87 | 65.25 | 0.58 | 2.88 | 539 |
| 2024-09-20 22:21:35.789 | MS1 | 121.4656644570 | 31.1446214313 | 509 | 504990 | -85.84 | 16.04 | 103.36 | 0.58 | 2.99 | 591 |
| 2024-09-20 22:21:36.685 | MS1 | 121.4656669109 | 31.1446316913 | 509 | 504990 | -91.87 | 12.87 | 99.32 | 0.68 | 2.34 | 550 |
| 2024-09-20 22:21:37.218 | MS1 | 121.4656653321 | 31.1446211249 | 509 | 504990 | -93.47 | 7.29 | 84.11 | 0.69 | 2.76 | 526 |
| 2024-09-20 22:21:38.508 | MS1 | 121.4656635362 | 31.1446184545 | 509 | 504990 | -89.52 | 11.19 | 57.42 | 0.62 | 2.63 | 576 |
| 2024-09-20 22:21:39.363 | MS1 | 121.4656699007 | 31.1446228473 | 509 | 504990 | -89.36 | 7.10 | 78.77 | 0.56 | 2.49 | 656 |
| 2024-09-20 22:21:40.161 | MS1 | 121.4656643165 | 31.1446276138 | 509 | 504990 | -92.04 | 12.73 | 574.26 | 0.02 | 2.71 | 1591 |
| 2024-09-20 22:21:41.915 | MS1 | 121.4656662252 | 31.1446186317 | 509 | 504990 | -91.67 | 8.29 | 428.61 | 0.02 | 2.40 | 1560 |
| 2024-09-20 22:21:42.474 | MS1 | 121.4656682715 | 31.1446325255 | 509 | 504990 | -91.54 | 11.46 | 459.70 | 0.15 | 2.10 | 1572 |

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
| 3221648 | 4 | 121.4752195642 | 31.1446646174 | 7 | 14 | 3 | 49.9 | TDD | 846 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3246333 | 2 | 121.4701160808 | 31.1443565622 | 259 | 10 | 4 | 46.5 | TDD | 627 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3251130 | 3 | 121.4739008831 | 31.1514621767 | 185 | 1 | 3 | 40.1 | TDD | 509 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3258370 | 1 | 121.4686489855 | 31.1504100419 | 237 | 15 | 10 | 23.7 | TDD | 664 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |

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
| 2024-09-20 22:21:31.501 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.520 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.654 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.654 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.395 | NREventA3 | measId:2;ServCellPCI:857;Se... |
| 2024-09-20 22:21:38.635 | NRHandoverAttempt | SourcePCI:857;SourceNR-ARFC... |
| 2024-09-20 22:21:38.667 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.682 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.809 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.809 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3258370 | 1 | 18.9324 | 8.9870 | -115.5078 | 12.7961 | 146.3273 | 0.0050 | 0.0098 |
| 2024_09_20 22:00 | 3246333 | 2 | 18.9113 | 9.1142 | -114.1468 | 19.2784 | 197.9627 | 0.0136 | 0.0144 |
| 2024_09_20 22:00 | 3251130 | 3 | 12.7451 | 8.8764 | -116.1137 | 8.7781 | 131.5237 | 0.0051 | 0.0130 |
| 2024_09_20 22:00 | 3221648 | 4 | 11.5231 | 11.9591 | -114.6022 | 17.2479 | 82.3126 | 0.0105 | 0.0121 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413036_4CBC0995 | 504990 | 509 | -90.6 | 504990 | 846 | -91.8 | 504990 | 664 | -100.3 | 504990 | 627 |
| MR_1774413036_84C957FB | 504990 | 509 | -89.5 | 504990 | 846 | -89.5 | 504990 | 664 | -101.2 | 504990 | 627 |
| MR_1774413036_501493EB | 504990 | 509 | -90.0 | 504990 | 846 | -89.7 | 504990 | 664 | -100.7 | 504990 | 627 |
| MR_1774413036_829AD993 | 504990 | 509 | -90.6 | 504990 | 846 | -88.9 | 504990 | 664 | -99.7 | 504990 | 627 |
| MR_1774413036_179F2E94 | 504990 | 509 | -89.5 | 504990 | 846 | -91.2 | 504990 | 664 | -102.7 | 504990 | 627 |
| MR_1774413036_79AFE4ED | 504990 | 509 | -88.9 | 504990 | 846 | -90.5 | 504990 | 664 | -99.1 | 504990 | 627 |
| MR_1774413036_290D907D | 504990 | 509 | -88.4 | 504990 | 846 | -91.8 | 504990 | 664 | -99.4 | 504990 | 627 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 279: `2cad12ac-b4a...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `2cad12ac-b4ad-44a0-bb96-5f11a15effe1` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[279] topology](images/test_0279.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3260442_2
- `C2`: Press down the tilt angle of 3260442_2 by 3 degrees
- `C3`: Add neighbor relationship between 3260442_2 and 3260743_4
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3260442_2
- `C5`: Press down the tilt angle  of 3260743_4 by 3 degrees
- `C6`: Decrease A3 Offset threshold for 3260442_2
- `C7`: Decrease transmission power for 3260743_4
- `C8`: Increase transmission power for 3260442_2
- `C9`: Increase A3 Offset threshold for 3260442_2
- `C10`: Adjust the azimuth of 3260442_2 by 11 degrees
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3260442_2
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3260743_4
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3260743_4
- `C14`: Check test server and transmission issues
- `C15`: Insufficient data; more data is needed for judgment.
- `C16`: Lift the tilt angle of 3260442_2 by 3 degrees
- `C17`: Lift the tilt angle  of 3260743_4 by 3 degrees
- `C18`: Adjust the azimuth of 3260743_4 by 23 degrees
- `C19`: Add neighbor relationship between 3231848_10 and 3260743_4
- `C20`: Decrease A3 Offset threshold for 3260743_4
- `C21`: Increase A3 Offset threshold for 3260743_4
- `C22`: Increase transmission power for 3260743_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.324 | MS1 | 121.4656720004 | 31.1446221798 | 872 | 504990 | -94.80 | 10.12 | 422.94 | 0.16 | 2.43 | 1560 |
| 2024-09-20 22:21:32.858 | MS1 | 121.4656643080 | 31.1446300789 | 243 | 504990 | -93.87 | 12.39 | 495.28 | 0.19 | 2.42 | 1588 |
| 2024-09-20 22:21:33.759 | MS1 | 121.4656647850 | 31.1446360519 | 6 | 504990 | -95.83 | 10.25 | 470.07 | 0.04 | 2.59 | 1590 |
| 2024-09-20 22:21:34.817 | MS1 | 121.4656779446 | 31.1446346386 | 66 | 152650 | -91.86 | 4.08 | 77.83 | 0.05 | 1.83 | 989 |
| 2024-09-20 22:21:35.273 | MS1 | 121.4656761116 | 31.1446241164 | 174 | 152650 | -90.44 | 7.47 | 64.66 | 0.02 | 1.85 | 989 |
| 2024-09-20 22:21:36.959 | MS1 | 121.4656643967 | 31.1446321231 | 584 | 152650 | -95.69 | 5.79 | 56.85 | 0.08 | 1.69 | 963 |
| 2024-09-20 22:21:37.760 | MS1 | 121.4656588271 | 31.1446186687 | 340 | 152650 | -93.54 | 3.35 | 79.37 | 0.17 | 1.61 | 920 |
| 2024-09-20 22:21:38.497 | MS1 | 121.4656740542 | 31.1446241718 | 66 | 152650 | -90.51 | 5.99 | 82.03 | 0.17 | 1.58 | 958 |
| 2024-09-20 22:21:39.193 | MS1 | 121.4656721144 | 31.1446232081 | 174 | 152650 | -92.01 | 6.86 | 73.63 | 0.05 | 1.74 | 991 |
| 2024-09-20 22:21:40.965 | MS1 | 121.4656715309 | 31.1446184869 | 584 | 152650 | -89.62 | 2.93 | 71.32 | 0.18 | 2.35 | 1567 |
| 2024-09-20 22:21:41.723 | MS1 | 121.4656741708 | 31.1446190072 | 340 | 152650 | -96.17 | 4.16 | 96.50 | 0.16 | 2.94 | 1597 |
| 2024-09-20 22:21:42.586 | MS1 | 121.4656628627 | 31.1446237203 | 66 | 152650 | -96.24 | 5.47 | 83.81 | 0.08 | 2.20 | 1563 |

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
| 3213137 | 9 | 121.4711887576 | 31.1515605303 | 232 | 7 | 1 | 20.4 | FDD | 262 | n1 | 152650 | 30M | 4T4R | 13 | 152650 |
| 3217500 | 7 | 121.4759847312 | 31.1512653295 | 318 | 8 | 9 | 0.8 | FDD | 416 | n1 | 152650 | 30M | 4T4R | 11 | 152650 |
| 3231848 | 10 | 121.4713009297 | 31.1502027178 | 141 | 7 | 0 | 23.3 | FDD | 584 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |
| 3232061 | 1 | 121.4726050940 | 31.1511702029 | 78 | 7 | 6 | 25.2 | TDD | 6 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3238824 | 13 | 121.4672351015 | 31.1530458095 | 335 | 15 | 1 | 9.3 | FDD | 340 | n1 | 152650 | 30M | 4T4R | 24 | 152650 |
| 3245905 | 12 | 121.4741666002 | 31.1504439984 | 353 | 13 | 4 | 24.0 | FDD | 174 | n1 | 152650 | 30M | 4T4R | 12 | 152650 |
| 3247805 | 8 | 121.4702329299 | 31.1455361928 | 325 | 10 | 4 | 29.5 | FDD | 66 | n1 | 152650 | 30M | 4T4R | 14 | 152650 |
| 3251585 | 3 | 121.4751319144 | 31.1445049488 | 251 | 1 | 8 | 3.5 | TDD | 330 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3256006 | 5 | 121.4696787482 | 31.1441741450 | 321 | 12 | 1 | 12.6 | TDD | 243 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3260442 | 2 | 121.4716468653 | 31.1518207919 | 226 | 1 | 9 | 29.5 | TDD | 872 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3260743 | 4 | 121.4716996728 | 31.1547609495 | 184 | 3 | 12 | 8.2 | TDD | 620 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3263180 | 11 | 121.4682688409 | 31.1455858120 | 323 | 1 | 5 | 23.7 | FDD | 203 | n1 | 152650 | 30M | 4T4R | 30 | 152650 |
| 3273888 | 6 | 121.4641654546 | 31.1454088103 | 258 | 11 | 11 | 17.8 | TDD | 158 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |

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
| 2024-09-20 22:21:31.406 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.427 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.577 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.577 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.300 | NREventA2 | measId:1;ServCellPCI:827;Se... |
| 2024-09-20 22:21:35.421 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.677 | NREventA5 | measId:3;ServCellPCI:827;Se... |
| 2024-09-20 22:21:35.719 | NRHandoverAttempt | SourcePCI:827;SourceNR-ARFC... |
| 2024-09-20 22:21:35.756 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.769 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:35.919 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.919 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3232061 | 1 | 13.5549 | 5.8115 | -117.2745 | 10.0386 | 190.7524 | 0.0084 | 0.0057 |
| 2024_09_20 22:00 | 3260442 | 2 | 8.7896 | 6.2628 | -117.2604 | 18.0481 | 156.7401 | 0.0180 | 0.0001 |
| 2024_09_20 22:00 | 3251585 | 3 | 15.3249 | 18.4082 | -117.1069 | 8.3171 | 104.8402 | 0.0050 | 0.0137 |
| 2024_09_20 22:00 | 3260743 | 4 | 6.7401 | 7.8191 | -116.9395 | 16.5813 | 151.8576 | 0.0061 | 0.0016 |
| 2024_09_20 22:00 | 3256006 | 5 | 5.9354 | 8.6024 | -117.7830 | 10.4537 | 108.3665 | 0.0134 | 0.0059 |
| 2024_09_20 22:00 | 3273888 | 6 | 15.6961 | 16.6440 | -116.6898 | 8.9525 | 96.0199 | 0.0160 | 0.0029 |
| 2024_09_20 22:00 | 3217500 | 7 | 9.9633 | 15.9977 | -115.8953 | 3.2019 | 39.4043 | 0.0096 | 0.0074 |
| 2024_09_20 22:00 | 3247805 | 8 | 8.2802 | 11.1918 | -117.8948 | 4.6187 | 53.1611 | 0.0112 | 0.0056 |
| 2024_09_20 22:00 | 3213137 | 9 | 9.0496 | 15.4971 | -114.6412 | 3.5412 | 52.9596 | 0.0082 | 0.0047 |
| 2024_09_20 22:00 | 3231848 | 10 | 13.1555 | 8.8379 | -116.8795 | 3.0646 | 37.2796 | 0.0042 | 0.0173 |
| 2024_09_20 22:00 | 3263180 | 11 | 6.0038 | 6.9828 | -114.5881 | 4.3645 | 56.8372 | 0.0107 | 0.0076 |
| 2024_09_20 22:00 | 3245905 | 12 | 11.5475 | 11.5634 | -117.9479 | 4.8262 | 29.8714 | 0.0075 | 0.0118 |
| 2024_09_20 22:00 | 3238824 | 13 | 6.8396 | 19.1514 | -114.7863 | 3.4359 | 53.7798 | 0.0090 | 0.0142 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413100_20E5E221 | 504990 | 6 | -94.2 | 504990 | 620 | -92.4 | 504990 | 330 | -99.4 | 504990 | 158 |
| MR_1774413100_86965FD5 | 152650 | 66 | -92.4 | 152650 | 262 | -93.6 | 152650 | 416 | -101.5 | 152650 | 203 |
| MR_1774413100_67C158D6 | 152650 | 66 | -91.5 | 152650 | 262 | -94.8 | 152650 | 416 | -102.8 | 152650 | 203 |
| MR_1774413100_2F86B1E7 | 504990 | 6 | -94.7 | 504990 | 620 | -95.9 | 504990 | 330 | -100.3 | 504990 | 158 |
| MR_1774413100_D24E37A6 | 504990 | 6 | -94.7 | 504990 | 620 | -95.0 | 504990 | 330 | -98.3 | 504990 | 158 |
| MR_1774413100_92460AB4 | 504990 | 6 | -96.3 | 504990 | 620 | -93.3 | 504990 | 330 | -99.7 | 504990 | 158 |
| MR_1774413100_52D569AA | 152650 | 66 | -90.9 | 152650 | 262 | -94.7 | 152650 | 416 | -102.7 | 152650 | 203 |

> *... 2개 열 생략 (전체 14열)*

---
