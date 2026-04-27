# Track A 문제 분석 — train[220]~train[229]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[220] ~ train[229] (10개)

## 목차

1. [문제 220: `07838d79-07a...`](#220) — single-answer, 정답: C21
2. [문제 221: `a81c6c9d-951...`](#221) — single-answer, 정답: C9
3. [문제 222: `40bde359-8f5...`](#222) — single-answer, 정답: C7
4. [문제 223: `ba854d32-31f...`](#223) — single-answer, 정답: C14
5. [문제 224: `ea295e35-374...`](#224) — single-answer, 정답: C10
6. [문제 225: `bb084b4f-adb...`](#225) — single-answer, 정답: C22
7. [문제 226: `48cbb26f-71b...`](#226) — multiple-answer, 정답: C13|C14
8. [문제 227: `4b23d3ae-6e6...`](#227) — single-answer, 정답: C21
9. [문제 228: `1a8b1f36-32c...`](#228) — single-answer, 정답: C13
10. [문제 229: `49420af9-e09...`](#229) — single-answer, 정답: C21

---

### 문제 220: `07838d79-07a...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `07838d79-07a7-4d13-bc98-2ffd81abf360` |
| Tag | **single-answer** |
| 정답 | **C21** |
| C21 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3214491_1 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[220] topology](images/train_0220.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3264307_2
- `C2`: Adjust the azimuth of 3214491_1 by 22 degrees
- `C3`: Decrease transmission power for 3214491_1
- `C4`: Increase transmission power for 3264307_2
- `C5`: Check test server and transmission issues
- `C6`: Increase transmission power for 3214491_1
- `C7`: Increase A3 Offset threshold for 3214491_1
- `C8`: Add neighbor relationship between 3237964_11 and 3264307_2
- `C9`: Press down the tilt angle  of 3264307_2 by 6 degrees
- `C10`: Lift the tilt angle  of 3264307_2 by 6 degrees
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3264307_2
- `C12`: Decrease A3 Offset threshold for 3214491_1
- `C13`: Press down the tilt angle of 3214491_1 by 5 degrees
- `C14`: Decrease A3 Offset threshold for 3264307_2
- `C15`: Adjust the azimuth of 3264307_2 by 15 degrees
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3264307_2
- `C17`: Lift the tilt angle of 3214491_1 by 5 degrees
- `C18`: Decrease transmission power for 3264307_2
- `C19`: Add neighbor relationship between 3214491_1 and 3264307_2
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3214491_1
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3214491_1 **← 정답**
- `C22`: Insufficient data; more data is needed for judgment.

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.883 | MS1 | 121.4656624242 | 31.1446337487 | 704 | 504990 | -94.27 | 9.35 | 423.27 | 0.12 | 2.58 | 1581 |
| 2024-09-20 22:21:32.758 | MS1 | 121.4656688585 | 31.1446318536 | 142 | 504990 | -93.27 | 10.71 | 328.14 | 0.09 | 2.10 | 1587 |
| 2024-09-20 22:21:33.624 | MS1 | 121.4656705102 | 31.1446299825 | 984 | 504990 | -93.86 | 11.78 | 550.88 | 0.04 | 2.52 | 1564 |
| 2024-09-20 22:21:34.410 | MS1 | 121.4656680475 | 31.1446291058 | 406 | 152650 | -95.32 | 3.54 | 86.31 | 0.12 | 1.87 | 950 |
| 2024-09-20 22:21:35.261 | MS1 | 121.4656716300 | 31.1446236431 | 958 | 152650 | -87.41 | 6.90 | 81.37 | 0.03 | 1.87 | 986 |
| 2024-09-20 22:21:36.960 | MS1 | 121.4656741821 | 31.1446318521 | 796 | 152650 | -96.47 | 6.81 | 96.27 | 0.13 | 1.61 | 932 |
| 2024-09-20 22:21:37.689 | MS1 | 121.4656699624 | 31.1446256841 | 863 | 152650 | -91.09 | 4.93 | 65.41 | 0.08 | 1.96 | 960 |
| 2024-09-20 22:21:38.981 | MS1 | 121.4656599421 | 31.1446247121 | 406 | 152650 | -96.28 | 4.51 | 90.29 | 0.10 | 1.96 | 986 |
| 2024-09-20 22:21:39.239 | MS1 | 121.4656607863 | 31.1446266121 | 958 | 152650 | -95.74 | 6.32 | 68.95 | 0.15 | 1.92 | 920 |
| 2024-09-20 22:21:40.194 | MS1 | 121.4656673219 | 31.1446337753 | 796 | 152650 | -89.02 | 2.55 | 86.89 | 0.14 | 2.73 | 1566 |
| 2024-09-20 22:21:41.756 | MS1 | 121.4656664292 | 31.1446294037 | 863 | 152650 | -87.53 | 5.77 | 68.06 | 0.03 | 2.81 | 1566 |
| 2024-09-20 22:21:42.224 | MS1 | 121.4656714408 | 31.1446284107 | 406 | 152650 | -92.91 | 5.96 | 52.44 | 0.04 | 2.83 | 1565 |

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
| 3211727 | 5 | 121.4682160327 | 31.1464280302 | 267 | 12 | 8 | 13.4 | TDD | 27 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3214491 | 1 | 121.4730937487 | 31.1539962741 | 192 | 4 | 8 | 22.9 | TDD | 704 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3223495 | 13 | 121.4646698071 | 31.1534934462 | 300 | 4 | 0 | 8.3 | FDD | 863 | n1 | 152650 | 30M | 4T4R | 25 | 152650 |
| 3225550 | 4 | 121.4669972989 | 31.1557895345 | 296 | 11 | 4 | 12.8 | TDD | 984 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3237964 | 11 | 121.4650317566 | 31.1461837400 | 321 | 4 | 3 | 6.0 | FDD | 796 | n1 | 152650 | 30M | 4T4R | 18 | 152650 |
| 3241507 | 7 | 121.4705976902 | 31.1449784458 | 160 | 12 | 4 | 0.4 | FDD | 168 | n1 | 152650 | 30M | 4T4R | 28 | 152650 |
| 3241689 | 8 | 121.4712294077 | 31.1488001135 | 207 | 3 | 9 | 23.5 | FDD | 406 | n1 | 152650 | 30M | 4T4R | 22 | 152650 |
| 3253080 | 6 | 121.4669437873 | 31.1513616535 | 348 | 2 | 11 | 13.2 | TDD | 191 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3256663 | 10 | 121.4697419771 | 31.1509140288 | 281 | 0 | 5 | 5.0 | FDD | 729 | n1 | 152650 | 30M | 4T4R | 13 | 152650 |
| 3264307 | 2 | 121.4694341018 | 31.1552866089 | 212 | 5 | 3 | 12.0 | TDD | 707 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3270493 | 9 | 121.4740597240 | 31.1511765171 | 224 | 2 | 3 | 6.3 | FDD | 56 | n1 | 152650 | 30M | 4T4R | 11 | 152650 |
| 3270865 | 3 | 121.4742890501 | 31.1511145402 | 246 | 12 | 1 | 3.2 | TDD | 142 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3271164 | 12 | 121.4742035169 | 31.1554423834 | 226 | 12 | 3 | 29.5 | FDD | 958 | n1 | 152650 | 30M | 4T4R | 25 | 152650 |

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
| 2024-09-20 22:21:31.019 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.168 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.168 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.894 | NREventA2 | measId:1;ServCellPCI:408;Se... |
| 2024-09-20 22:21:35.013 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.256 | NREventA5 | measId:3;ServCellPCI:408;Se... |
| 2024-09-20 22:21:35.300 | NRHandoverAttempt | SourcePCI:408;SourceNR-ARFC... |
| 2024-09-20 22:21:35.344 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.356 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:35.506 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.506 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3214491 | 1 | 15.4478 | 7.4734 | -114.7393 | 12.9844 | 190.4453 | 0.0050 | 0.0200 |
| 2024_09_20 22:00 | 3264307 | 2 | 11.7165 | 19.0840 | -116.5164 | 15.1003 | 197.9941 | 0.0117 | 0.0145 |
| 2024_09_20 22:00 | 3270865 | 3 | 7.5046 | 19.7132 | -117.4530 | 9.2958 | 196.6800 | 0.0092 | 0.0103 |
| 2024_09_20 22:00 | 3225550 | 4 | 17.5103 | 7.6624 | -115.9262 | 11.6956 | 93.9993 | 0.0150 | 0.0140 |
| 2024_09_20 22:00 | 3211727 | 5 | 11.7362 | 6.5393 | -114.2425 | 6.6875 | 115.8277 | 0.0026 | 0.0142 |
| 2024_09_20 22:00 | 3253080 | 6 | 7.6143 | 12.4453 | -115.8699 | 5.8756 | 106.9042 | 0.0105 | 0.0122 |
| 2024_09_20 22:00 | 3241507 | 7 | 12.8752 | 13.6659 | -115.1092 | 3.7284 | 56.5207 | 0.0185 | 0.0185 |
| 2024_09_20 22:00 | 3241689 | 8 | 12.4263 | 18.0367 | -117.9829 | 3.8541 | 48.6239 | 0.0052 | 0.0093 |
| 2024_09_20 22:00 | 3270493 | 9 | 14.6564 | 11.1706 | -115.1830 | 3.9317 | 46.1188 | 0.0114 | 0.0087 |
| 2024_09_20 22:00 | 3256663 | 10 | 13.2647 | 10.6098 | -116.1555 | 3.9961 | 24.7204 | 0.0109 | 0.0111 |
| 2024_09_20 22:00 | 3237964 | 11 | 5.6806 | 7.6085 | -115.9357 | 4.8121 | 40.7342 | 0.0068 | 0.0103 |
| 2024_09_20 22:00 | 3271164 | 12 | 18.1807 | 14.8874 | -115.2206 | 4.1277 | 24.5371 | 0.0131 | 0.0087 |
| 2024_09_20 22:00 | 3223495 | 13 | 11.2971 | 14.7362 | -117.6800 | 4.7490 | 20.0314 | 0.0052 | 0.0087 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415214_E81B6A7F | 152650 | 406 | -95.7 | 152650 | 729 | -101.7 | 152650 | 168 | -106.3 | 152650 | 56 |
| MR_1774415214_CA2412F1 | 504990 | 984 | -92.5 | 504990 | 707 | -91.9 | 504990 | 191 | -95.2 | 504990 | 27 |
| MR_1774415214_ED158BD0 | 504990 | 984 | -93.7 | 504990 | 707 | -93.5 | 504990 | 191 | -96.0 | 504990 | 27 |
| MR_1774415214_0075CB7D | 152650 | 406 | -93.8 | 152650 | 729 | -103.1 | 152650 | 168 | -107.4 | 152650 | 56 |
| MR_1774415214_FFEA6D70 | 152650 | 406 | -94.3 | 152650 | 729 | -99.8 | 152650 | 168 | -106.5 | 152650 | 56 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 221: `a81c6c9d-951...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `a81c6c9d-9513-49eb-b5c2-35d1bb34b707` |
| Tag | **single-answer** |
| 정답 | **C9** |
| C9 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[221] topology](images/train_0221.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3270301_2
- `C2`: Lift the tilt angle of 3270301_2 by 10 degrees
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3211325_1
- `C4`: Increase A3 Offset threshold for 3270301_2
- `C5`: Adjust the azimuth of 3211325_1 by 3 degrees
- `C6`: Add neighbor relationship between 3270301_2 and 3211325_1
- `C7`: Add neighbor relationship between 3272405_3 and 3211325_1
- `C8`: Adjust the azimuth of 3270301_2 by 50 degrees
- `C9`: Check test server and transmission issues **← 정답**
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3270301_2
- `C11`: Lift the tilt angle  of 3211325_1 by 3 degrees
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3270301_2
- `C13`: Increase transmission power for 3211325_1
- `C14`: Press down the tilt angle of 3270301_2 by 10 degrees
- `C15`: Insufficient data; more data is needed for judgment.
- `C16`: Increase transmission power for 3270301_2
- `C17`: Increase A3 Offset threshold for 3211325_1
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3211325_1
- `C19`: Decrease transmission power for 3211325_1
- `C20`: Press down the tilt angle  of 3211325_1 by 3 degrees
- `C21`: Decrease A3 Offset threshold for 3211325_1
- `C22`: Decrease transmission power for 3270301_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.878 | MS1 | 121.4656770836 | 31.1446204953 | 25 | 504990 | -88.32 | 12.91 | 318.61 | 0.08 | 2.95 | 1561 |
| 2024-09-20 22:21:32.550 | MS1 | 121.4656618212 | 31.1446208128 | 25 | 504990 | -89.42 | 17.56 | 338.36 | 0.07 | 2.26 | 1566 |
| 2024-09-20 22:21:33.687 | MS1 | 121.4656690958 | 31.1446184521 | 25 | 504990 | -88.49 | 14.35 | 587.54 | 0.16 | 2.17 | 1577 |
| 2024-09-20 22:21:34.972 | MS1 | 121.4656768225 | 31.1446254611 | 25 | 504990 | -85.01 | 17.01 | 45.69 | 0.19 | 2.09 | 329 |
| 2024-09-20 22:21:35.782 | MS1 | 121.4656609042 | 31.1446317087 | 25 | 504990 | -91.98 | 17.39 | 73.48 | 0.07 | 2.20 | 369 |
| 2024-09-20 22:21:36.131 | MS1 | 121.4656725562 | 31.1446290527 | 25 | 504990 | -87.38 | 13.41 | 69.87 | 0.12 | 2.40 | 454 |
| 2024-09-20 22:21:37.786 | MS1 | 121.4656774027 | 31.1446262208 | 25 | 504990 | -93.66 | 12.08 | 46.63 | 0.06 | 3.00 | 456 |
| 2024-09-20 22:21:38.256 | MS1 | 121.4656676173 | 31.1446303728 | 25 | 504990 | -89.01 | 9.60 | 59.08 | 0.02 | 2.31 | 457 |
| 2024-09-20 22:21:39.812 | MS1 | 121.4656611131 | 31.1446309482 | 25 | 504990 | -91.00 | 7.64 | 87.73 | 0.05 | 2.10 | 446 |
| 2024-09-20 22:21:40.664 | MS1 | 121.4656614505 | 31.1446259049 | 25 | 504990 | -90.09 | 12.87 | 339.27 | 0.18 | 2.22 | 1599 |
| 2024-09-20 22:21:41.868 | MS1 | 121.4656751318 | 31.1446224785 | 25 | 504990 | -92.78 | 11.22 | 505.95 | 0.20 | 2.96 | 1597 |
| 2024-09-20 22:21:42.446 | MS1 | 121.4656613718 | 31.1446267106 | 25 | 504990 | -93.65 | 12.14 | 441.07 | 0.07 | 2.87 | 1576 |

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
| 3211325 | 1 | 121.4756027345 | 31.1511385937 | 230 | 2 | 8 | 19.9 | TDD | 600 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3240122 | 4 | 121.4756592237 | 31.1474201282 | 102 | 14 | 1 | 18.3 | TDD | 33 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3270301 | 2 | 121.4689342954 | 31.1468292233 | 182 | 13 | 6 | 41.7 | TDD | 25 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3272405 | 3 | 121.4673868676 | 31.1539605038 | 175 | 11 | 4 | 15.8 | TDD | 639 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |

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
| 2024-09-20 22:21:31.547 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.569 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.674 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.674 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.436 | NREventA3 | measId:2;ServCellPCI:939;Se... |
| 2024-09-20 22:21:38.676 | NRHandoverAttempt | SourcePCI:939;SourceNR-ARFC... |
| 2024-09-20 22:21:38.725 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.737 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.860 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.860 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3211325 | 1 | 11.6956 | 15.7879 | -116.6638 | 18.7516 | 84.3318 | 0.0071 | 0.0070 |
| 2024_09_20 22:00 | 3270301 | 2 | 7.8692 | 7.0136 | -117.0495 | 8.2454 | 81.6766 | 0.0051 | 0.0019 |
| 2024_09_20 22:00 | 3272405 | 3 | 8.7283 | 6.2724 | -117.8273 | 8.9066 | 196.4120 | 0.0144 | 0.0153 |
| 2024_09_20 22:00 | 3240122 | 4 | 16.2141 | 16.8189 | -114.3335 | 17.6230 | 114.4325 | 0.0199 | 0.0142 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774411990_1FBC2120 | 504990 | 25 | -86.9 | 504990 | 600 | -90.6 | 504990 | 639 | -95.0 | 504990 | 33 |
| MR_1774411990_62AB891A | 504990 | 25 | -86.3 | 504990 | 600 | -90.2 | 504990 | 639 | -94.4 | 504990 | 33 |
| MR_1774411990_E595B96B | 504990 | 25 | -84.9 | 504990 | 600 | -90.5 | 504990 | 639 | -96.3 | 504990 | 33 |
| MR_1774411990_E080E560 | 504990 | 25 | -84.9 | 504990 | 600 | -91.1 | 504990 | 639 | -95.2 | 504990 | 33 |
| MR_1774411990_1B230DBE | 504990 | 25 | -86.5 | 504990 | 600 | -90.8 | 504990 | 639 | -96.7 | 504990 | 33 |
| MR_1774411990_72ED98BD | 504990 | 25 | -86.6 | 504990 | 600 | -91.3 | 504990 | 639 | -95.2 | 504990 | 33 |
| MR_1774411990_87AB896D | 504990 | 25 | -86.6 | 504990 | 600 | -92.4 | 504990 | 639 | -93.4 | 504990 | 33 |
| MR_1774411990_6E4B6971 | 504990 | 25 | -84.9 | 504990 | 600 | -91.9 | 504990 | 639 | -96.6 | 504990 | 33 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 222: `40bde359-8f5...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `40bde359-8f5b-4d0d-9699-1d62ffac825a` |
| Tag | **single-answer** |
| 정답 | **C7** |
| C7 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[222] topology](images/train_0222.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3261636_1 and 3240104_3
- `C2`: Decrease A3 Offset threshold for 3259595_2
- `C3`: Press down the tilt angle  of 3240104_3 by 10 degrees
- `C4`: Adjust the azimuth of 3240104_3 by 50 degrees
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3259595_2
- `C6`: Adjust the azimuth of 3259595_2 by 50 degrees
- `C7`: Check test server and transmission issues **← 정답**
- `C8`: Increase transmission power for 3240104_3
- `C9`: Lift the tilt angle of 3259595_2 by 10 degrees
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3240104_3
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3240104_3
- `C12`: Increase A3 Offset threshold for 3240104_3
- `C13`: Decrease transmission power for 3240104_3
- `C14`: Increase A3 Offset threshold for 3259595_2
- `C15`: Increase transmission power for 3259595_2
- `C16`: Press down the tilt angle of 3259595_2 by 10 degrees
- `C17`: Insufficient data; more data is needed for judgment.
- `C18`: Add neighbor relationship between 3259595_2 and 3240104_3
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3259595_2
- `C20`: Lift the tilt angle  of 3240104_3 by 10 degrees
- `C21`: Decrease transmission power for 3259595_2
- `C22`: Decrease A3 Offset threshold for 3240104_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.280 | MS1 | 121.4656744703 | 31.1446349206 | 714 | 504990 | -88.76 | 16.84 | 385.84 | 0.17 | 2.07 | 1597 |
| 2024-09-20 22:21:32.119 | MS1 | 121.4656653563 | 31.1446215108 | 714 | 504990 | -89.74 | 12.31 | 536.70 | 0.17 | 2.50 | 1562 |
| 2024-09-20 22:21:33.898 | MS1 | 121.4656676193 | 31.1446191679 | 714 | 504990 | -91.92 | 13.36 | 488.24 | 0.06 | 2.31 | 1585 |
| 2024-09-20 22:21:34.524 | MS1 | 121.4656721147 | 31.1446245176 | 714 | 504990 | -85.77 | 17.01 | 83.87 | 0.09 | 2.42 | 405 |
| 2024-09-20 22:21:35.929 | MS1 | 121.4656671673 | 31.1446286921 | 714 | 504990 | -89.00 | 12.13 | 89.96 | 0.08 | 2.40 | 433 |
| 2024-09-20 22:21:36.379 | MS1 | 121.4656597672 | 31.1446374547 | 714 | 504990 | -91.52 | 15.32 | 70.58 | 0.06 | 2.85 | 447 |
| 2024-09-20 22:21:37.354 | MS1 | 121.4656677421 | 31.1446337889 | 714 | 504990 | -93.56 | 7.54 | 100.83 | 0.01 | 2.58 | 456 |
| 2024-09-20 22:21:38.666 | MS1 | 121.4656702281 | 31.1446242138 | 714 | 504990 | -93.60 | 11.31 | 89.09 | 0.15 | 2.60 | 496 |
| 2024-09-20 22:21:39.938 | MS1 | 121.4656593967 | 31.1446209920 | 714 | 504990 | -93.74 | 12.34 | 103.02 | 0.19 | 2.60 | 333 |
| 2024-09-20 22:21:40.120 | MS1 | 121.4656764585 | 31.1446290449 | 714 | 504990 | -90.15 | 9.92 | 406.27 | 0.09 | 2.77 | 1569 |
| 2024-09-20 22:21:41.383 | MS1 | 121.4656598113 | 31.1446266863 | 714 | 504990 | -90.03 | 11.50 | 401.09 | 0.19 | 2.06 | 1576 |
| 2024-09-20 22:21:42.507 | MS1 | 121.4656664721 | 31.1446361954 | 714 | 504990 | -90.99 | 8.74 | 472.02 | 0.19 | 2.86 | 1585 |

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
| 3240104 | 3 | 121.4741658878 | 31.1461345839 | 0 | 12 | 4 | 16.3 | TDD | 203 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3247913 | 4 | 121.4648761357 | 31.1443776957 | 49 | 0 | 1 | 48.5 | TDD | 376 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3259595 | 2 | 121.4728482355 | 31.1458465250 | 325 | 8 | 8 | 49.8 | TDD | 714 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3261636 | 1 | 121.4745944030 | 31.1473518169 | 18 | 1 | 2 | 49.4 | TDD | 72 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |

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
| 2024-09-20 22:21:31.612 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.637 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.765 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.765 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.485 | NREventA3 | measId:2;ServCellPCI:671;Se... |
| 2024-09-20 22:21:38.725 | NRHandoverAttempt | SourcePCI:671;SourceNR-ARFC... |
| 2024-09-20 22:21:38.760 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.775 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.891 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.891 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3261636 | 1 | 17.3518 | 8.5195 | -114.9254 | 14.6674 | 194.7048 | 0.0077 | 0.0092 |
| 2024_09_20 22:00 | 3259595 | 2 | 15.0253 | 15.0649 | -116.0385 | 10.4473 | 96.3734 | 0.0182 | 0.0182 |
| 2024_09_20 22:00 | 3240104 | 3 | 18.0134 | 14.1273 | -117.9899 | 5.9393 | 179.5596 | 0.0110 | 0.0093 |
| 2024_09_20 22:00 | 3247913 | 4 | 7.5829 | 9.1036 | -115.8409 | 5.6535 | 175.8715 | 0.0067 | 0.0183 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412438_8FC50CBC | 504990 | 714 | -84.4 | 504990 | 203 | -90.1 | 504990 | 72 | -97.2 | 504990 | 376 |
| MR_1774412438_1E4173B9 | 504990 | 714 | -83.8 | 504990 | 203 | -89.6 | 504990 | 72 | -94.8 | 504990 | 376 |
| MR_1774412438_DB6866C7 | 504990 | 714 | -86.4 | 504990 | 203 | -89.2 | 504990 | 72 | -95.6 | 504990 | 376 |
| MR_1774412438_D13A45C6 | 504990 | 714 | -87.3 | 504990 | 203 | -88.5 | 504990 | 72 | -95.2 | 504990 | 376 |
| MR_1774412438_8BA090D2 | 504990 | 714 | -86.7 | 504990 | 203 | -90.5 | 504990 | 72 | -98.2 | 504990 | 376 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 223: `ba854d32-31f...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `ba854d32-31fb-4090-a498-e375679c4044` |
| Tag | **single-answer** |
| 정답 | **C14** |
| C14 의미 | Add neighbor relationship between 3222965_2 and 3214705_1 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[223] topology](images/train_0223.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3214705_1
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3222965_2
- `C3`: Decrease transmission power for 3222965_2
- `C4`: Adjust the azimuth of 3222965_2 by 15 degrees
- `C5`: Decrease transmission power for 3214705_1
- `C6`: Adjust the azimuth of 3214705_1 by 16 degrees
- `C7`: Lift the tilt angle of 3222965_2 by 10 degrees
- `C8`: Press down the tilt angle of 3222965_2 by 10 degrees
- `C9`: Increase A3 Offset threshold for 3214705_1
- `C10`: Check test server and transmission issues
- `C11`: Insufficient data; more data is needed for judgment.
- `C12`: Press down the tilt angle  of 3214705_1 by 3 degrees
- `C13`: Lift the tilt angle  of 3214705_1 by 3 degrees
- `C14`: Add neighbor relationship between 3222965_2 and 3214705_1 **← 정답**
- `C15`: Increase transmission power for 3214705_1
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3214705_1
- `C17`: Increase transmission power for 3222965_2
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3214705_1
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3222965_2
- `C20`: Decrease A3 Offset threshold for 3222965_2
- `C21`: Add neighbor relationship between 3210697_3 and 3214705_1
- `C22`: Increase A3 Offset threshold for 3222965_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.815 | MS1 | 121.4656733125 | 31.1446314286 | 370 | 504990 | -83.37 | 13.98 | 347.92 | 0.00 | 2.47 | 1593 |
| 2024-09-20 22:21:32.990 | MS1 | 121.4656589785 | 31.1446317892 | 370 | 504990 | -80.21 | 15.86 | 450.73 | 0.15 | 2.58 | 1582 |
| 2024-09-20 22:21:33.677 | MS1 | 121.4656694827 | 31.1446190347 | 370 | 504990 | -80.03 | 16.16 | 450.21 | 0.04 | 2.26 | 1586 |
| 2024-09-20 22:21:34.651 | MS1 | 121.4656673255 | 31.1446364040 | 370 | 504990 | -86.36 | -3.00 | 38.84 | 0.01 | 1.50 | 1568 |
| 2024-09-20 22:21:35.222 | MS1 | 121.4656595330 | 31.1446284534 | 370 | 504990 | -92.19 | -2.77 | 63.56 | 0.16 | 1.14 | 1588 |
| 2024-09-20 22:21:36.280 | MS1 | 121.4656724749 | 31.1446366353 | 370 | 504990 | -86.13 | -0.14 | 40.66 | 0.06 | 1.18 | 1560 |
| 2024-09-20 22:21:37.345 | MS1 | 121.4656773672 | 31.1446377290 | 370 | 504990 | -92.45 | -1.67 | 52.77 | 0.17 | 1.11 | 1596 |
| 2024-09-20 22:21:38.848 | MS1 | 121.4656648798 | 31.1446297047 | 370 | 504990 | -77.44 | 16.52 | 313.53 | 0.06 | 1.16 | 1583 |
| 2024-09-20 22:21:39.244 | MS1 | 121.4656622966 | 31.1446294022 | 370 | 504990 | -81.69 | 13.78 | 352.60 | 0.01 | 1.23 | 1585 |
| 2024-09-20 22:21:40.660 | MS1 | 121.4656693967 | 31.1446211718 | 370 | 504990 | -76.96 | 15.02 | 567.29 | 0.07 | 2.76 | 1591 |
| 2024-09-20 22:21:41.452 | MS1 | 121.4656690299 | 31.1446308419 | 370 | 504990 | -81.92 | 13.31 | 525.00 | 0.19 | 2.31 | 1581 |
| 2024-09-20 22:21:42.323 | MS1 | 121.4656695671 | 31.1446234944 | 370 | 504990 | -79.01 | 17.26 | 301.18 | 0.14 | 2.13 | 1574 |

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
| 3210697 | 3 | 121.4663062603 | 31.1472038984 | 88 | 1 | 8 | 22.9 | TDD | 482 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3214705 | 1 | 121.4707057253 | 31.1446930840 | 253 | 1 | 7 | 16.9 | TDD | 313 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3222965 | 2 | 121.4646159718 | 31.1526737619 | 159 | 14 | 12 | 41.1 | TDD | 370 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3233625 | 4 | 121.4727386583 | 31.1559691034 | 108 | 9 | 10 | 31.5 | TDD | 340 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:31.405 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.421 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.530 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.530 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.298 | NREventA3 | measId:2;ServCellPCI:762;Se... |
| 2024-09-20 22:21:36.298 | NREventA3 | measId:2;ServCellPCI:762;Se... |
| 2024-09-20 22:21:37.298 | NREventA3 | measId:2;ServCellPCI:762;Se... |
| 2024-09-20 22:21:39.798 | NRRRCReestablishAttempt | PCI:762 |
| 2024-09-20 22:21:39.816 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.831 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:39.968 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.968 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3214705 | 1 | 17.6002 | 14.9641 | -117.3532 | 12.4321 | 189.2376 | 0.0065 | 0.0020 |
| 2024_09_20 22:00 | 3222965 | 2 | 12.7052 | 12.7070 | -115.1250 | 5.8247 | 106.8208 | 0.0002 | 0.1182 |
| 2024_09_20 22:00 | 3210697 | 3 | 16.2057 | 17.0303 | -114.1851 | 10.8215 | 110.0204 | 0.0158 | 0.0079 |
| 2024_09_20 22:00 | 3233625 | 4 | 17.2284 | 10.1116 | -116.1504 | 18.5382 | 131.0598 | 0.0134 | 0.0184 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413557_D25CE8C8 | 504990 | 370 | -87.5 | 504990 | 313 | -79.6 | 504990 | 482 | -84.9 | 504990 | 340 |
| MR_1774413557_9603B614 | 504990 | 313 | -79.5 | 504990 | 370 | -85.7 | 504990 | 482 | -85.4 | 504990 | 340 |
| MR_1774413557_2045393F | 504990 | 370 | -88.0 | 504990 | 313 | -80.3 | 504990 | 482 | -84.1 | 504990 | 340 |
| MR_1774413557_2571301D | 504990 | 370 | -84.5 | 504990 | 313 | -80.8 | 504990 | 482 | -83.3 | 504990 | 340 |
| MR_1774413557_A3E09D7F | 504990 | 313 | -79.8 | 504990 | 370 | -85.8 | 504990 | 482 | -82.3 | 504990 | 340 |
| MR_1774413557_A0E4EB48 | 504990 | 370 | -87.5 | 504990 | 313 | -80.0 | 504990 | 482 | -86.2 | 504990 | 340 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 224: `ea295e35-374...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `ea295e35-374b-480f-a247-6677d8d95a4c` |
| Tag | **single-answer** |
| 정답 | **C10** |
| C10 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[224] topology](images/train_0224.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3249921_2
- `C2`: Increase A3 Offset threshold for 3249921_2
- `C3`: Add neighbor relationship between 3276601_4 and 3278560_1
- `C4`: Lift the tilt angle of 3249921_2 by 10 degrees
- `C5`: Insufficient data; more data is needed for judgment.
- `C6`: Decrease A3 Offset threshold for 3278560_1
- `C7`: Increase A3 Offset threshold for 3278560_1
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3278560_1
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3249921_2
- `C10`: Check test server and transmission issues **← 정답**
- `C11`: Press down the tilt angle  of 3278560_1 by 4 degrees
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3278560_1
- `C13`: Decrease transmission power for 3278560_1
- `C14`: Decrease transmission power for 3249921_2
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3249921_2
- `C16`: Lift the tilt angle  of 3278560_1 by 4 degrees
- `C17`: Press down the tilt angle of 3249921_2 by 10 degrees
- `C18`: Increase transmission power for 3278560_1
- `C19`: Adjust the azimuth of 3249921_2 by 50 degrees
- `C20`: Adjust the azimuth of 3278560_1 by 50 degrees
- `C21`: Add neighbor relationship between 3249921_2 and 3278560_1
- `C22`: Increase transmission power for 3249921_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.173 | MS1 | 121.4656597690 | 31.1446244813 | 695 | 504990 | -86.97 | 15.21 | 405.49 | 0.03 | 2.23 | 1575 |
| 2024-09-20 22:21:32.329 | MS1 | 121.4656613732 | 31.1446348440 | 695 | 504990 | -89.30 | 17.58 | 381.10 | 0.08 | 2.48 | 1577 |
| 2024-09-20 22:21:33.304 | MS1 | 121.4656684719 | 31.1446334542 | 695 | 504990 | -91.81 | 14.03 | 388.40 | 0.07 | 2.49 | 1598 |
| 2024-09-20 22:21:34.152 | MS1 | 121.4656597090 | 31.1446291473 | 695 | 504990 | -87.03 | 12.15 | 58.23 | 0.16 | 2.21 | 420 |
| 2024-09-20 22:21:35.337 | MS1 | 121.4656761873 | 31.1446361175 | 695 | 504990 | -91.14 | 15.32 | 66.70 | 0.08 | 2.65 | 430 |
| 2024-09-20 22:21:36.796 | MS1 | 121.4656708096 | 31.1446264659 | 695 | 504990 | -86.84 | 13.94 | 55.09 | 0.15 | 2.15 | 356 |
| 2024-09-20 22:21:37.257 | MS1 | 121.4656764893 | 31.1446283788 | 695 | 504990 | -90.56 | 9.28 | 73.03 | 0.13 | 2.29 | 497 |
| 2024-09-20 22:21:38.783 | MS1 | 121.4656655263 | 31.1446285840 | 695 | 504990 | -90.64 | 11.42 | 55.77 | 0.10 | 2.31 | 329 |
| 2024-09-20 22:21:39.902 | MS1 | 121.4656763820 | 31.1446243102 | 695 | 504990 | -89.25 | 10.32 | 63.54 | 0.20 | 2.25 | 487 |
| 2024-09-20 22:21:40.749 | MS1 | 121.4656580065 | 31.1446288831 | 695 | 504990 | -92.24 | 12.80 | 573.75 | 0.15 | 2.08 | 1560 |
| 2024-09-20 22:21:41.435 | MS1 | 121.4656736549 | 31.1446368259 | 695 | 504990 | -91.28 | 12.26 | 403.06 | 0.12 | 2.02 | 1579 |
| 2024-09-20 22:21:42.298 | MS1 | 121.4656758161 | 31.1446279190 | 695 | 504990 | -90.59 | 11.13 | 601.76 | 0.13 | 2.80 | 1588 |

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
| 3249921 | 2 | 121.4732081970 | 31.1511321473 | 78 | 13 | 2 | 16.9 | TDD | 695 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3251099 | 3 | 121.4726799293 | 31.1474690531 | 248 | 7 | 0 | 42.9 | TDD | 463 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3276601 | 4 | 121.4727039760 | 31.1442580163 | 13 | 4 | 4 | 23.7 | TDD | 903 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3278560 | 1 | 121.4758254722 | 31.1462320243 | 76 | 2 | 2 | 37.6 | TDD | 32 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |

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
| 2024-09-20 22:21:31.558 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.579 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.716 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.716 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.420 | NREventA3 | measId:2;ServCellPCI:389;Se... |
| 2024-09-20 22:21:38.660 | NRHandoverAttempt | SourcePCI:389;SourceNR-ARFC... |
| 2024-09-20 22:21:38.706 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.718 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.824 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.824 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3278560 | 1 | 9.9501 | 7.2973 | -115.5858 | 19.5429 | 186.6560 | 0.0024 | 0.0074 |
| 2024_09_20 22:00 | 3249921 | 2 | 9.3956 | 13.1757 | -115.5356 | 7.8761 | 82.2187 | 0.0149 | 0.0128 |
| 2024_09_20 22:00 | 3251099 | 3 | 7.0785 | 15.6880 | -117.6163 | 12.2553 | 114.3247 | 0.0102 | 0.0127 |
| 2024_09_20 22:00 | 3276601 | 4 | 7.0319 | 16.9752 | -117.6391 | 5.5646 | 193.9692 | 0.0086 | 0.0156 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416161_FAAB7A1F | 504990 | 695 | -86.8 | 504990 | 32 | -87.4 | 504990 | 903 | -99.0 | 504990 | 463 |
| MR_1774416161_01022D66 | 504990 | 695 | -86.3 | 504990 | 32 | -86.9 | 504990 | 903 | -99.1 | 504990 | 463 |
| MR_1774416161_43AD05BC | 504990 | 695 | -88.7 | 504990 | 32 | -89.0 | 504990 | 903 | -96.0 | 504990 | 463 |
| MR_1774416161_A6A6E275 | 504990 | 695 | -86.9 | 504990 | 32 | -90.4 | 504990 | 903 | -97.7 | 504990 | 463 |
| MR_1774416161_E81BF01E | 504990 | 695 | -85.8 | 504990 | 32 | -89.5 | 504990 | 903 | -97.4 | 504990 | 463 |
| MR_1774416161_A51305C5 | 504990 | 695 | -88.9 | 504990 | 32 | -90.3 | 504990 | 903 | -97.3 | 504990 | 463 |
| MR_1774416161_EC36538B | 504990 | 695 | -85.3 | 504990 | 32 | -87.0 | 504990 | 903 | -96.0 | 504990 | 463 |
| MR_1774416161_8E9C4394 | 504990 | 695 | -87.9 | 504990 | 32 | -88.7 | 504990 | 903 | -99.3 | 504990 | 463 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 225: `bb084b4f-adb...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `bb084b4f-adbe-47f5-a042-fca66ce8f21c` |
| Tag | **single-answer** |
| 정답 | **C22** |
| C22 의미 | Add neighbor relationship between 3252201_1 and 3212980_3 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[225] topology](images/train_0225.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3212980_3
- `C2`: Increase transmission power for 3212980_3
- `C3`: Decrease A3 Offset threshold for 3212980_3
- `C4`: Lift the tilt angle  of 3212980_3 by 1 degrees
- `C5`: Adjust the azimuth of 3212980_3 by 35 degrees
- `C6`: Press down the tilt angle  of 3212980_3 by 1 degrees
- `C7`: Decrease transmission power for 3252201_1
- `C8`: Increase A3 Offset threshold for 3212980_3
- `C9`: Decrease A3 Offset threshold for 3252201_1
- `C10`: Increase transmission power for 3252201_1
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3252201_1
- `C12`: Adjust the azimuth of 3252201_1 by 50 degrees
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3212980_3
- `C14`: Decrease transmission power for 3212980_3
- `C15`: Press down the tilt angle of 3252201_1 by 10 degrees
- `C16`: Add neighbor relationship between 3234113_4 and 3212980_3
- `C17`: Increase A3 Offset threshold for 3252201_1
- `C18`: Lift the tilt angle of 3252201_1 by 10 degrees
- `C19`: Insufficient data; more data is needed for judgment.
- `C20`: Check test server and transmission issues
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3252201_1
- `C22`: Add neighbor relationship between 3252201_1 and 3212980_3 **← 정답**

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.819 | MS1 | 121.4656760032 | 31.1446265066 | 684 | 504990 | -75.27 | 16.88 | 504.90 | 0.14 | 2.02 | 1585 |
| 2024-09-20 22:21:32.852 | MS1 | 121.4656689620 | 31.1446251888 | 684 | 504990 | -75.34 | 14.48 | 368.30 | 0.08 | 2.17 | 1598 |
| 2024-09-20 22:21:33.569 | MS1 | 121.4656747308 | 31.1446343521 | 684 | 504990 | -76.47 | 14.65 | 331.15 | 0.09 | 2.82 | 1594 |
| 2024-09-20 22:21:34.665 | MS1 | 121.4656585954 | 31.1446192713 | 684 | 504990 | -85.71 | -0.15 | 66.24 | 0.09 | 1.17 | 1599 |
| 2024-09-20 22:21:35.107 | MS1 | 121.4656611357 | 31.1446278136 | 684 | 504990 | -88.80 | -2.65 | 38.51 | 0.14 | 1.22 | 1562 |
| 2024-09-20 22:21:36.428 | MS1 | 121.4656640074 | 31.1446304794 | 684 | 504990 | -92.04 | -3.91 | 46.46 | 0.05 | 1.04 | 1571 |
| 2024-09-20 22:21:37.922 | MS1 | 121.4656735910 | 31.1446312505 | 684 | 504990 | -87.67 | -2.18 | 66.19 | 0.07 | 1.47 | 1561 |
| 2024-09-20 22:21:38.284 | MS1 | 121.4656776954 | 31.1446317351 | 684 | 504990 | -79.25 | 12.31 | 436.70 | 0.15 | 1.23 | 1569 |
| 2024-09-20 22:21:39.997 | MS1 | 121.4656743565 | 31.1446245302 | 684 | 504990 | -80.62 | 14.16 | 394.57 | 0.02 | 1.00 | 1575 |
| 2024-09-20 22:21:40.810 | MS1 | 121.4656670689 | 31.1446250129 | 684 | 504990 | -81.78 | 13.94 | 491.20 | 0.01 | 2.62 | 1564 |
| 2024-09-20 22:21:41.347 | MS1 | 121.4656621843 | 31.1446241787 | 684 | 504990 | -77.68 | 17.07 | 577.14 | 0.05 | 2.33 | 1576 |
| 2024-09-20 22:21:42.313 | MS1 | 121.4656692961 | 31.1446346432 | 684 | 504990 | -84.07 | 14.78 | 527.85 | 0.02 | 2.89 | 1563 |

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
| 3212980 | 3 | 121.4751419624 | 31.1503331416 | 270 | 0 | 8 | 15.3 | TDD | 932 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3234113 | 4 | 121.4728710171 | 31.1499325009 | 345 | 7 | 11 | 18.3 | TDD | 797 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3252201 | 1 | 121.4710628865 | 31.1459435770 | 333 | 10 | 3 | 22.5 | TDD | 684 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3253558 | 2 | 121.4699673024 | 31.1497624689 | 259 | 5 | 2 | 44.5 | TDD | 1003 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |

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
| 2024-09-20 22:21:30.920 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.940 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.079 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.079 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.722 | NREventA3 | measId:2;ServCellPCI:159;Se... |
| 2024-09-20 22:21:35.722 | NREventA3 | measId:2;ServCellPCI:159;Se... |
| 2024-09-20 22:21:36.722 | NREventA3 | measId:2;ServCellPCI:159;Se... |
| 2024-09-20 22:21:39.222 | NRRRCReestablishAttempt | PCI:159 |
| 2024-09-20 22:21:39.233 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.243 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:39.384 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.384 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3252201 | 1 | 7.5682 | 11.3344 | -114.6691 | 15.5703 | 181.1491 | 0.0119 | 0.1991 |
| 2024_09_20 22:00 | 3253558 | 2 | 10.9450 | 9.8215 | -116.2716 | 7.1084 | 191.8576 | 0.0123 | 0.0158 |
| 2024_09_20 22:00 | 3212980 | 3 | 18.4541 | 16.8556 | -114.6581 | 19.5771 | 162.6058 | 0.0155 | 0.0024 |
| 2024_09_20 22:00 | 3234113 | 4 | 8.1409 | 6.5060 | -117.7543 | 9.2122 | 117.3270 | 0.0082 | 0.0086 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415354_8B02CA8B | 504990 | 684 | -87.3 | 504990 | 932 | -82.4 | 504990 | 797 | -90.0 | 504990 | 1003 |
| MR_1774415354_35074B27 | 504990 | 932 | -80.6 | 504990 | 684 | -84.2 | 504990 | 797 | -88.9 | 504990 | 1003 |
| MR_1774415354_FF26ED3D | 504990 | 684 | -87.1 | 504990 | 932 | -81.2 | 504990 | 797 | -89.7 | 504990 | 1003 |
| MR_1774415354_4A8BDB95 | 504990 | 932 | -79.5 | 504990 | 684 | -85.3 | 504990 | 797 | -90.0 | 504990 | 1003 |
| MR_1774415354_41FCDA9A | 504990 | 932 | -81.8 | 504990 | 684 | -84.9 | 504990 | 797 | -89.8 | 504990 | 1003 |
| MR_1774415354_8244205F | 504990 | 684 | -85.7 | 504990 | 932 | -79.3 | 504990 | 797 | -90.0 | 504990 | 1003 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 226: `48cbb26f-71b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `48cbb26f-71b3-4013-8563-71c3a878f5bd` |
| Tag | **multiple-answer** |
| 정답 | **C13|C14** |
| C13 의미 | Decrease transmission power for 3239138_1 |
| C14 의미 | Press down the tilt angle  of 3239138_1 by 1 degrees |
| 패턴 분류 | **P3 Overshoot (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[226] topology](images/train_0226.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3239138_1
- `C2`: Increase transmission power for 3239138_1
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3239138_1
- `C4`: Decrease A3 Offset threshold for 3239138_1
- `C5`: Adjust the azimuth of 3279556_2 by 34 degrees
- `C6`: Adjust the azimuth of 3239138_1 by 14 degrees
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3279556_2
- `C8`: Check test server and transmission issues
- `C9`: Lift the tilt angle  of 3239138_1 by 1 degrees
- `C10`: Press down the tilt angle of 3279556_2 by 4 degrees
- `C11`: Lift the tilt angle of 3279556_2 by 4 degrees
- `C12`: Add neighbor relationship between 3212060_4 and 3239138_1
- `C13`: Decrease transmission power for 3239138_1 **← 정답**
- `C14`: Press down the tilt angle  of 3239138_1 by 1 degrees **← 정답**
- `C15`: Add neighbor relationship between 3279556_2 and 3239138_1
- `C16`: Increase A3 Offset threshold for 3279556_2
- `C17`: Increase transmission power for 3279556_2
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3279556_2
- `C19`: Insufficient data; more data is needed for judgment.
- `C20`: Decrease A3 Offset threshold for 3279556_2
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3239138_1
- `C22`: Decrease transmission power for 3279556_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.989 | MS1 | 121.4656610109 | 31.1446303724 | 810 | 504990 | -75.79 | 12.75 | 484.58 | 0.08 | 2.04 | 1588 |
| 2024-09-20 22:21:32.941 | MS1 | 121.4656648835 | 31.1446197762 | 810 | 504990 | -75.01 | 12.40 | 430.58 | 0.11 | 2.28 | 1588 |
| 2024-09-20 22:21:33.399 | MS1 | 121.4656656106 | 31.1446205235 | 810 | 504990 | -83.06 | 15.18 | 388.63 | 0.16 | 2.61 | 1577 |
| 2024-09-20 22:21:34.835 | MS1 | 121.4656596036 | 31.1446365430 | 810 | 504990 | -88.69 | 2.49 | 63.08 | 0.01 | 1.05 | 1565 |
| 2024-09-20 22:21:35.662 | MS1 | 121.4656756018 | 31.1446370275 | 810 | 504990 | -85.19 | 2.29 | 45.87 | 0.06 | 1.18 | 1578 |
| 2024-09-20 22:21:36.307 | MS1 | 121.4656750325 | 31.1446186759 | 810 | 504990 | -85.94 | 0.72 | 76.79 | 0.01 | 1.35 | 1569 |
| 2024-09-20 22:21:37.276 | MS1 | 121.4656628138 | 31.1446365779 | 810 | 504990 | -87.50 | 3.77 | 80.23 | 0.09 | 1.29 | 1568 |
| 2024-09-20 22:21:38.511 | MS1 | 121.4656734036 | 31.1446351408 | 810 | 504990 | -91.67 | 2.48 | 36.63 | 0.03 | 1.04 | 1594 |
| 2024-09-20 22:21:39.683 | MS1 | 121.4656757299 | 31.1446229436 | 810 | 504990 | -89.70 | 3.71 | 44.14 | 0.16 | 1.30 | 1584 |
| 2024-09-20 22:21:40.418 | MS1 | 121.4656777551 | 31.1446247945 | 810 | 504990 | -84.32 | 16.05 | 454.61 | 0.14 | 2.71 | 1586 |
| 2024-09-20 22:21:41.353 | MS1 | 121.4656596082 | 31.1446363468 | 810 | 504990 | -79.26 | 12.36 | 367.60 | 0.15 | 2.50 | 1585 |
| 2024-09-20 22:21:42.192 | MS1 | 121.4656742613 | 31.1446242627 | 810 | 504990 | -76.89 | 15.39 | 460.23 | 0.11 | 2.43 | 1562 |

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
| 3212060 | 4 | 121.4654220505 | 31.1472619273 | 282 | 11 | 4 | 36.2 | TDD | 791 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3239138 | 1 | 121.4693559366 | 31.1518942763 | 189 | 0 | 2 | 17.5 | TDD | 153 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3261113 | 3 | 121.4701096488 | 31.1509872891 | 319 | 4 | 1 | 27.5 | TDD | 678 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3279556 | 2 | 121.4689800895 | 31.1529365206 | 233 | 2 | 2 | 28.5 | TDD | 810 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |

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
| 2024-09-20 22:21:31.302 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.321 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.440 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.440 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3239138 | 1 | 11.5945 | 18.6361 | -116.1014 | 9.9954 | 81.8115 | 0.0085 | 0.0078 |
| 2024_09_20 22:00 | 3279556 | 2 | 5.7617 | 8.2132 | -108.7845 | 13.2689 | 108.9717 | 0.0146 | 0.0161 |
| 2024_09_20 22:00 | 3261113 | 3 | 17.2048 | 9.3326 | -115.9598 | 7.3516 | 193.5049 | 0.0039 | 0.0179 |
| 2024_09_20 22:00 | 3212060 | 4 | 19.0032 | 15.5619 | -116.3469 | 6.8901 | 122.3895 | 0.0137 | 0.0055 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414004_5184798A | 504990 | 810 | -87.0 | 504990 | 153 | -87.8 | 504990 | 791 | -86.2 | 504990 | 678 |
| MR_1774414004_BC040AE8 | 504990 | 810 | -88.5 | 504990 | 153 | -88.3 | 504990 | 791 | -87.4 | 504990 | 678 |
| MR_1774414004_7C57AD7A | 504990 | 810 | -87.1 | 504990 | 153 | -85.8 | 504990 | 791 | -86.9 | 504990 | 678 |
| MR_1774414004_FDD5609E | 504990 | 153 | -86.8 | 504990 | 810 | -84.7 | 504990 | 791 | -86.1 | 504990 | 678 |
| MR_1774414004_29CF6E8D | 504990 | 153 | -86.8 | 504990 | 810 | -86.9 | 504990 | 791 | -84.9 | 504990 | 678 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 227: `4b23d3ae-6e6...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `4b23d3ae-6e67-4749-8cc8-3ef8600171ca` |
| Tag | **single-answer** |
| 정답 | **C21** |
| C21 의미 | Lift the tilt angle  of 3275931_4 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[227] topology](images/train_0227.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3257022_3
- `C2`: Decrease transmission power for 3210831_1
- `C3`: Check test server and transmission issues
- `C4`: Lift the tilt angle of 3210831_1 by 2 degrees
- `C5`: Increase transmission power for 3257022_3
- `C6`: Increase transmission power for 3210831_1
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3210831_1
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3210831_1
- `C9`: Press down the tilt angle of 3210831_1 by 2 degrees
- `C10`: Add neighbor relationship between 3210831_1 and 3257022_3
- `C11`: Adjust the azimuth of 3275931_4 by 50 degrees
- `C12`: Increase A3 Offset threshold for 3257022_3
- `C13`: Adjust the azimuth of 3210831_1 by 13 degrees
- `C14`: Decrease A3 Offset threshold for 3210831_1
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3257022_3
- `C16`: Increase A3 Offset threshold for 3210831_1
- `C17`: Press down the tilt angle  of 3275931_4 by 10 degrees
- `C18`: Insufficient data; more data is needed for judgment.
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3257022_3
- `C20`: Decrease transmission power for 3257022_3
- `C21`: Lift the tilt angle  of 3275931_4 by 10 degrees **← 정답**
- `C22`: Add neighbor relationship between 3275931_4 and 3257022_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.273 | MS1 | 121.4656721105 | 31.1446333275 | 176 | 504990 | -87.81 | 12.94 | 507.39 | 0.01 | 2.56 | 1593 |
| 2024-09-20 22:21:32.698 | MS1 | 121.4656778972 | 31.1446263560 | 176 | 504990 | -89.75 | 12.06 | 316.01 | 0.17 | 2.78 | 1580 |
| 2024-09-20 22:21:33.447 | MS1 | 121.4656670982 | 31.1446292227 | 176 | 504990 | -91.73 | 16.42 | 400.24 | 0.05 | 2.17 | 1560 |
| 2024-09-20 22:21:34.574 | MS1 | 121.4656638941 | 31.1446280794 | 176 | 504990 | -87.38 | 15.88 | 89.13 | 0.02 | 2.11 | 1566 |
| 2024-09-20 22:21:35.310 | MS1 | 121.4656759735 | 31.1446271113 | 176 | 504990 | -85.82 | 15.72 | 83.60 | 0.02 | 2.33 | 1594 |
| 2024-09-20 22:21:36.899 | MS1 | 121.4656688377 | 31.1446303099 | 176 | 504990 | -90.75 | 12.43 | 77.37 | 0.04 | 2.90 | 1566 |
| 2024-09-20 22:21:37.976 | MS1 | 121.4656662311 | 31.1446207691 | 176 | 504990 | -92.83 | 8.73 | 50.99 | 0.10 | 2.81 | 1584 |
| 2024-09-20 22:21:38.576 | MS1 | 121.4656732794 | 31.1446288021 | 176 | 504990 | -90.43 | 7.71 | 74.86 | 0.18 | 2.13 | 1587 |
| 2024-09-20 22:21:39.169 | MS1 | 121.4656621379 | 31.1446358137 | 176 | 504990 | -90.94 | 8.85 | 90.33 | 0.06 | 2.66 | 1569 |
| 2024-09-20 22:21:40.511 | MS1 | 121.4656611937 | 31.1446183213 | 176 | 504990 | -93.26 | 12.37 | 470.00 | 0.11 | 2.53 | 1561 |
| 2024-09-20 22:21:41.574 | MS1 | 121.4656636893 | 31.1446379147 | 176 | 504990 | -90.08 | 8.32 | 497.66 | 0.15 | 2.58 | 1563 |
| 2024-09-20 22:21:42.559 | MS1 | 121.4656688479 | 31.1446333818 | 176 | 504990 | -89.55 | 10.92 | 402.41 | 0.17 | 2.99 | 1572 |

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
| 3210831 | 1 | 121.4691480871 | 31.1542377933 | 184 | 1 | 9 | 26.4 | TDD | 176 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3257022 | 3 | 121.4653063387 | 31.1494927495 | 34 | 7 | 1 | 34.6 | TDD | 284 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3273324 | 2 | 121.4726115121 | 31.1465804541 | 198 | 7 | 1 | 23.3 | TDD | 209 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3275931 | 4 | 121.4696753724 | 31.1463713562 | 25 | 5 | 6 | 26.4 | TDD | 469 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |

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
| 2024-09-20 22:21:30.861 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:30.968 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.968 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.658 | NREventA3 | measId:2;ServCellPCI:281;Se... |
| 2024-09-20 22:21:37.898 | NRHandoverAttempt | SourcePCI:281;SourceNR-ARFC... |
| 2024-09-20 22:21:37.942 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.956 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.067 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.067 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3210831 | 1 | 78.8512 | 91.5788 | -114.0769 | 11.0194 | 144.2236 | 0.0091 | 0.0083 |
| 2024_09_20 22:00 | 3273324 | 2 | 17.5103 | 19.7840 | -115.2348 | 15.9639 | 149.9288 | 0.0175 | 0.0119 |
| 2024_09_20 22:00 | 3257022 | 3 | 18.7204 | 13.4290 | -117.9565 | 10.5041 | 92.9483 | 0.0014 | 0.0008 |
| 2024_09_20 22:00 | 3275931 | 4 | 7.4800 | 18.3513 | -114.6552 | 19.9260 | 149.2316 | 0.0093 | 0.0153 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413948_440C5554 | 504990 | 176 | -87.5 | 504990 | 284 | -95.7 | 504990 | 469 | -101.1 | 504990 | 209 |
| MR_1774413948_DF58C3A3 | 504990 | 176 | -87.5 | 504990 | 284 | -96.5 | 504990 | 469 | -101.1 | 504990 | 209 |
| MR_1774413948_C09B8713 | 504990 | 176 | -86.7 | 504990 | 284 | -96.8 | 504990 | 469 | -99.3 | 504990 | 209 |
| MR_1774413948_8F3ECF5A | 504990 | 176 | -85.9 | 504990 | 284 | -95.5 | 504990 | 469 | -100.7 | 504990 | 209 |
| MR_1774413948_54E30A38 | 504990 | 176 | -87.5 | 504990 | 284 | -94.0 | 504990 | 469 | -97.8 | 504990 | 209 |
| MR_1774413948_4D306885 | 504990 | 176 | -86.7 | 504990 | 284 | -93.9 | 504990 | 469 | -99.2 | 504990 | 209 |
| MR_1774413948_C2573A91 | 504990 | 176 | -89.3 | 504990 | 284 | -95.0 | 504990 | 469 | -99.2 | 504990 | 209 |
| MR_1774413948_B2CB19E1 | 504990 | 176 | -86.0 | 504990 | 284 | -97.2 | 504990 | 469 | -98.6 | 504990 | 209 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 228: `1a8b1f36-32c...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `1a8b1f36-32c7-4250-862a-a91f041ec301` |
| Tag | **single-answer** |
| 정답 | **C13** |
| C13 의미 | Decrease A3 Offset threshold for 3255021_1 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[228] topology](images/train_0228.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3236714_3 by 43 degrees
- `C2`: Decrease A3 Offset threshold for 3236714_3
- `C3`: Add neighbor relationship between 3255021_1 and 3236714_3
- `C4`: Press down the tilt angle of 3255021_1 by 5 degrees
- `C5`: Increase A3 Offset threshold for 3255021_1
- `C6`: Decrease transmission power for 3255021_1
- `C7`: Lift the tilt angle  of 3236714_3 by 8 degrees
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3236714_3
- `C9`: Add neighbor relationship between 3233425_2 and 3236714_3
- `C10`: Increase transmission power for 3255021_1
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3236714_3
- `C12`: Insufficient data; more data is needed for judgment.
- `C13`: Decrease A3 Offset threshold for 3255021_1 **← 정답**
- `C14`: Increase A3 Offset threshold for 3236714_3
- `C15`: Decrease transmission power for 3236714_3
- `C16`: Check test server and transmission issues
- `C17`: Adjust the azimuth of 3255021_1 by 50 degrees
- `C18`: Increase transmission power for 3236714_3
- `C19`: Lift the tilt angle of 3255021_1 by 5 degrees
- `C20`: Press down the tilt angle  of 3236714_3 by 8 degrees
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3255021_1
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3255021_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.759 | MS1 | 121.4656598202 | 31.1446225909 | 404 | 504990 | -76.57 | 17.56 | 305.37 | 0.08 | 2.09 | 1574 |
| 2024-09-20 22:21:32.610 | MS1 | 121.4656599776 | 31.1446241314 | 404 | 504990 | -79.48 | 17.89 | 433.71 | 0.10 | 2.06 | 1584 |
| 2024-09-20 22:21:33.823 | MS1 | 121.4656634450 | 31.1446305920 | 404 | 504990 | -79.21 | 16.82 | 466.84 | 0.19 | 2.47 | 1595 |
| 2024-09-20 22:21:34.266 | MS1 | 121.4656735925 | 31.1446272676 | 404 | 504990 | -85.60 | -2.98 | 53.78 | 0.18 | 1.38 | 1598 |
| 2024-09-20 22:21:35.751 | MS1 | 121.4656590357 | 31.1446216681 | 404 | 504990 | -90.05 | -3.68 | 63.97 | 0.11 | 1.23 | 1567 |
| 2024-09-20 22:21:36.297 | MS1 | 121.4656634171 | 31.1446214153 | 404 | 504990 | -88.01 | -1.41 | 53.90 | 0.06 | 1.27 | 1595 |
| 2024-09-20 22:21:37.711 | MS1 | 121.4656708238 | 31.1446319443 | 404 | 504990 | -87.47 | -3.15 | 49.88 | 0.13 | 1.30 | 1561 |
| 2024-09-20 22:21:38.632 | MS1 | 121.4656662461 | 31.1446311952 | 404 | 504990 | -83.91 | -3.90 | 52.48 | 0.18 | 1.38 | 1581 |
| 2024-09-20 22:21:39.867 | MS1 | 121.4656622584 | 31.1446185812 | 180 | 504990 | -84.97 | 17.54 | 194.74 | 0.10 | 1.50 | 1584 |
| 2024-09-20 22:21:40.472 | MS1 | 121.4656592199 | 31.1446338931 | 180 | 504990 | -82.75 | 16.20 | 436.32 | 0.08 | 2.63 | 1584 |
| 2024-09-20 22:21:41.228 | MS1 | 121.4656622425 | 31.1446235929 | 180 | 504990 | -81.21 | 15.46 | 359.97 | 0.19 | 2.81 | 1568 |
| 2024-09-20 22:21:42.884 | MS1 | 121.4656623125 | 31.1446272968 | 180 | 504990 | -82.95 | 17.09 | 361.81 | 0.05 | 2.82 | 1565 |

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
| 3233425 | 2 | 121.4727978806 | 31.1479238048 | 25 | 12 | 3 | 39.4 | TDD | 970 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3236714 | 3 | 121.4705751772 | 31.1533719317 | 249 | 7 | 0 | 17.8 | TDD | 180 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3240182 | 4 | 121.4693870409 | 31.1455765576 | 129 | 7 | 5 | 18.8 | TDD | 4 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3255021 | 1 | 121.4740203694 | 31.1544161050 | 313 | 3 | 6 | 43.6 | TDD | 404 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |

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
| 2024-09-20 22:21:31.493 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.512 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.650 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.650 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.346 | NREventA3 | measId:2;ServCellPCI:556;Se... |
| 2024-09-20 22:21:38.586 | NRHandoverAttempt | SourcePCI:556;SourceNR-ARFC... |
| 2024-09-20 22:21:38.634 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.649 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.774 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.774 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3255021 | 1 | 7.0416 | 14.6590 | -116.1823 | 15.5779 | 85.3435 | 0.0015 | 0.1355 |
| 2024_09_20 22:00 | 3233425 | 2 | 13.0063 | 15.8643 | -116.6672 | 7.8087 | 187.8725 | 0.0146 | 0.0020 |
| 2024_09_20 22:00 | 3236714 | 3 | 7.4830 | 8.5381 | -116.8651 | 10.0911 | 144.9965 | 0.0181 | 0.0081 |
| 2024_09_20 22:00 | 3240182 | 4 | 8.6038 | 17.9598 | -117.3206 | 15.0392 | 161.3588 | 0.0067 | 0.0088 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412373_B6691019 | 504990 | 180 | -81.4 | 504990 | 404 | -86.4 | 504990 | 970 | -83.1 | 504990 | 4 |
| MR_1774412373_BFEFE5ED | 504990 | 404 | -84.1 | 504990 | 180 | -80.2 | 504990 | 970 | -80.3 | 504990 | 4 |
| MR_1774412373_91B41FD2 | 504990 | 404 | -86.4 | 504990 | 180 | -82.2 | 504990 | 970 | -79.9 | 504990 | 4 |
| MR_1774412373_99C866C0 | 504990 | 404 | -84.7 | 504990 | 180 | -80.7 | 504990 | 970 | -81.0 | 504990 | 4 |
| MR_1774412373_953471DB | 504990 | 180 | -79.1 | 504990 | 404 | -83.8 | 504990 | 970 | -80.0 | 504990 | 4 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 229: `49420af9-e09...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `49420af9-e091-4a3c-b179-e030d3e2552f` |
| Tag | **single-answer** |
| 정답 | **C21** |
| C21 의미 | Decrease A3 Offset threshold for 3269968_2 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[229] topology](images/train_0229.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3254057_3
- `C2`: Check test server and transmission issues
- `C3`: Insufficient data; more data is needed for judgment.
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3269968_2
- `C5`: Add neighbor relationship between 3269968_2 and 3254057_3
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3269968_2
- `C7`: Decrease transmission power for 3269968_2
- `C8`: Press down the tilt angle  of 3254057_3 by 10 degrees
- `C9`: Increase transmission power for 3269968_2
- `C10`: Press down the tilt angle of 3269968_2 by 10 degrees
- `C11`: Increase A3 Offset threshold for 3254057_3
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3254057_3
- `C13`: Adjust the azimuth of 3269968_2 by 50 degrees
- `C14`: Decrease A3 Offset threshold for 3254057_3
- `C15`: Increase A3 Offset threshold for 3269968_2
- `C16`: Lift the tilt angle of 3269968_2 by 10 degrees
- `C17`: Add neighbor relationship between 3258724_4 and 3254057_3
- `C18`: Adjust the azimuth of 3254057_3 by 44 degrees
- `C19`: Lift the tilt angle  of 3254057_3 by 10 degrees
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3254057_3
- `C21`: Decrease A3 Offset threshold for 3269968_2 **← 정답**
- `C22`: Decrease transmission power for 3254057_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.242 | MS1 | 121.4656727501 | 31.1446252380 | 652 | 504990 | -82.50 | 12.27 | 465.60 | 0.11 | 2.03 | 1599 |
| 2024-09-20 22:21:32.453 | MS1 | 121.4656646210 | 31.1446367430 | 652 | 504990 | -80.50 | 12.23 | 305.42 | 0.20 | 2.11 | 1577 |
| 2024-09-20 22:21:33.868 | MS1 | 121.4656730494 | 31.1446289164 | 652 | 504990 | -81.37 | 13.78 | 390.25 | 0.07 | 2.22 | 1587 |
| 2024-09-20 22:21:34.354 | MS1 | 121.4656585452 | 31.1446277765 | 652 | 504990 | -85.59 | -3.79 | 82.86 | 0.00 | 1.09 | 1568 |
| 2024-09-20 22:21:35.476 | MS1 | 121.4656725562 | 31.1446193749 | 652 | 504990 | -86.38 | -0.56 | 50.85 | 0.03 | 1.10 | 1595 |
| 2024-09-20 22:21:36.159 | MS1 | 121.4656712314 | 31.1446335087 | 652 | 504990 | -86.62 | -1.55 | 64.79 | 0.18 | 1.14 | 1563 |
| 2024-09-20 22:21:37.249 | MS1 | 121.4656717199 | 31.1446356551 | 652 | 504990 | -89.90 | -1.23 | 48.91 | 0.12 | 1.20 | 1573 |
| 2024-09-20 22:21:38.958 | MS1 | 121.4656695473 | 31.1446306567 | 652 | 504990 | -89.11 | -1.32 | 42.29 | 0.01 | 1.11 | 1563 |
| 2024-09-20 22:21:39.708 | MS1 | 121.4656702614 | 31.1446356556 | 125 | 504990 | -84.73 | 14.32 | 161.97 | 0.00 | 1.08 | 1574 |
| 2024-09-20 22:21:40.194 | MS1 | 121.4656625893 | 31.1446262327 | 125 | 504990 | -82.89 | 17.61 | 408.64 | 0.04 | 2.53 | 1562 |
| 2024-09-20 22:21:41.513 | MS1 | 121.4656748916 | 31.1446251808 | 125 | 504990 | -78.19 | 13.99 | 402.51 | 0.11 | 2.49 | 1589 |
| 2024-09-20 22:21:42.362 | MS1 | 121.4656655884 | 31.1446216603 | 125 | 504990 | -82.77 | 15.39 | 555.68 | 0.08 | 2.77 | 1591 |

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
| 3232053 | 1 | 121.4695568823 | 31.1478958794 | 138 | 6 | 12 | 31.9 | TDD | 619 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3254057 | 3 | 121.4721447335 | 31.1473106921 | 200 | 8 | 10 | 26.7 | TDD | 125 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3258724 | 4 | 121.4759771098 | 31.1472789487 | 159 | 0 | 4 | 19.1 | TDD | 334 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3269968 | 2 | 121.4709300025 | 31.1479871660 | 335 | 13 | 6 | 17.6 | TDD | 652 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:31.083 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.107 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.215 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.215 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.898 | NREventA3 | measId:2;ServCellPCI:742;Se... |
| 2024-09-20 22:21:38.138 | NRHandoverAttempt | SourcePCI:742;SourceNR-ARFC... |
| 2024-09-20 22:21:38.172 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.183 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.301 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.301 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3232053 | 1 | 13.6002 | 7.6036 | -116.1494 | 17.7964 | 148.8293 | 0.0004 | 0.0148 |
| 2024_09_20 22:00 | 3269968 | 2 | 9.3228 | 13.2186 | -114.2980 | 19.5162 | 126.7768 | 0.0050 | 0.1205 |
| 2024_09_20 22:00 | 3254057 | 3 | 17.2377 | 10.5469 | -115.6886 | 11.6036 | 181.7703 | 0.0023 | 0.0192 |
| 2024_09_20 22:00 | 3258724 | 4 | 5.6104 | 13.3943 | -116.4553 | 19.6814 | 159.7872 | 0.0076 | 0.0058 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414433_C06876A3 | 504990 | 652 | -84.1 | 504990 | 125 | -78.9 | 504990 | 334 | -80.6 | 504990 | 619 |
| MR_1774414433_75E45A63 | 504990 | 652 | -84.7 | 504990 | 125 | -78.7 | 504990 | 334 | -82.8 | 504990 | 619 |
| MR_1774414433_F203BD36 | 504990 | 652 | -84.8 | 504990 | 125 | -81.4 | 504990 | 334 | -79.8 | 504990 | 619 |
| MR_1774414433_8FACB2FE | 504990 | 125 | -78.3 | 504990 | 652 | -85.0 | 504990 | 334 | -80.1 | 504990 | 619 |
| MR_1774414433_05FE9DF7 | 504990 | 125 | -80.6 | 504990 | 652 | -84.5 | 504990 | 334 | -79.8 | 504990 | 619 |
| MR_1774414433_F9ED4041 | 504990 | 125 | -78.7 | 504990 | 652 | -87.5 | 504990 | 334 | -82.2 | 504990 | 619 |
| MR_1774414433_14048391 | 504990 | 125 | -80.4 | 504990 | 652 | -84.0 | 504990 | 334 | -81.5 | 504990 | 619 |

> *... 2개 열 생략 (전체 14열)*

---
