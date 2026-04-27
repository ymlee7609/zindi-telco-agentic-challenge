# Track A 문제 분석 — test[420]~test[429]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/test.json`
> 범위: test[420] ~ test[429] (10개)

## 목차

1. [문제 420: `38447098-245...`](#420) — single-answer
2. [문제 421: `dabca732-6b6...`](#421) — multiple-answer
3. [문제 422: `c92759f6-59b...`](#422) — single-answer
4. [문제 423: `87f2ea40-2bc...`](#423) — single-answer
5. [문제 424: `0a7dad77-54c...`](#424) — single-answer
6. [문제 425: `9a924492-dc1...`](#425) — single-answer
7. [문제 426: `8205389e-d63...`](#426) — single-answer
8. [문제 427: `279df29d-cd9...`](#427) — single-answer
9. [문제 428: `375b6cf0-1d6...`](#428) — single-answer
10. [문제 429: `162e9a74-99c...`](#429) — single-answer

---

### 문제 420: `38447098-245...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `38447098-245d-45c3-8dc2-1be1207deac7` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[420] topology](images/test_0420.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3262724_3
- `C2`: Increase A3 Offset threshold for 3262724_3
- `C3`: Decrease transmission power for 3240703_4
- `C4`: Increase transmission power for 3240703_4
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3262724_3
- `C6`: Insufficient data; more data is needed for judgment.
- `C7`: Lift the tilt angle of 3240703_4 by 2 degrees
- `C8`: Increase A3 Offset threshold for 3240703_4
- `C9`: Increase transmission power for 3262724_3
- `C10`: Add neighbor relationship between 3240703_4 and 3262724_3
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3240703_4
- `C12`: Decrease A3 Offset threshold for 3262724_3
- `C13`: Lift the tilt angle  of 3262724_3 by 10 degrees
- `C14`: Check test server and transmission issues
- `C15`: Press down the tilt angle  of 3262724_3 by 10 degrees
- `C16`: Adjust the azimuth of 3262724_3 by 50 degrees
- `C17`: Press down the tilt angle of 3240703_4 by 2 degrees
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3240703_4
- `C19`: Add neighbor relationship between 3254322_2 and 3262724_3
- `C20`: Adjust the azimuth of 3240703_4 by 29 degrees
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3262724_3
- `C22`: Decrease A3 Offset threshold for 3240703_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.516 | MS1 | 121.4656610295 | 31.1446226747 | 115 | 504990 | -86.54 | 12.79 | 566.77 | 0.11 | 2.33 | 1600 |
| 2024-09-20 22:21:32.212 | MS1 | 121.4656755690 | 31.1446242885 | 115 | 504990 | -88.16 | 17.54 | 527.61 | 0.18 | 2.31 | 1577 |
| 2024-09-20 22:21:33.712 | MS1 | 121.4656764956 | 31.1446264839 | 115 | 504990 | -86.89 | 14.27 | 526.11 | 0.14 | 2.33 | 1577 |
| 2024-09-20 22:21:34.424 | MS1 | 121.4656654507 | 31.1446236469 | 115 | 504990 | -89.00 | 14.04 | 88.60 | 0.50 | 2.03 | 559 |
| 2024-09-20 22:21:35.576 | MS1 | 121.4656590097 | 31.1446218585 | 115 | 504990 | -89.07 | 13.36 | 97.71 | 0.54 | 2.97 | 636 |
| 2024-09-20 22:21:36.280 | MS1 | 121.4656623123 | 31.1446244331 | 115 | 504990 | -89.73 | 16.16 | 55.29 | 0.51 | 2.94 | 682 |
| 2024-09-20 22:21:37.370 | MS1 | 121.4656647516 | 31.1446284012 | 115 | 504990 | -92.28 | 8.65 | 62.81 | 0.66 | 2.55 | 611 |
| 2024-09-20 22:21:38.878 | MS1 | 121.4656624989 | 31.1446373311 | 115 | 504990 | -89.14 | 11.53 | 81.42 | 0.56 | 2.51 | 632 |
| 2024-09-20 22:21:39.176 | MS1 | 121.4656763288 | 31.1446324803 | 115 | 504990 | -90.96 | 7.69 | 95.50 | 0.61 | 2.64 | 595 |
| 2024-09-20 22:21:40.248 | MS1 | 121.4656674986 | 31.1446202486 | 115 | 504990 | -93.71 | 10.58 | 339.42 | 0.04 | 2.68 | 1591 |
| 2024-09-20 22:21:41.728 | MS1 | 121.4656637291 | 31.1446360813 | 115 | 504990 | -91.12 | 10.11 | 435.37 | 0.10 | 2.64 | 1579 |
| 2024-09-20 22:21:42.219 | MS1 | 121.4656676630 | 31.1446365542 | 115 | 504990 | -91.01 | 8.03 | 459.60 | 0.10 | 2.80 | 1583 |

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
| 3216412 | 1 | 121.4734800313 | 31.1531380948 | 290 | 7 | 7 | 41.3 | TDD | 152 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3240703 | 4 | 121.4755820724 | 31.1555719809 | 247 | 1 | 7 | 36.2 | TDD | 115 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3254322 | 2 | 121.4751818363 | 31.1485620112 | 133 | 14 | 5 | 35.4 | TDD | 641 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3262724 | 3 | 121.4758710792 | 31.1501183433 | 71 | 14 | 0 | 46.0 | TDD | 834 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |

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
| 2024-09-20 22:21:31.031 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.047 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.165 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.165 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.911 | NREventA3 | measId:2;ServCellPCI:384;Se... |
| 2024-09-20 22:21:38.151 | NRHandoverAttempt | SourcePCI:384;SourceNR-ARFC... |
| 2024-09-20 22:21:38.188 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.200 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.304 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.304 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3216412 | 1 | 12.6935 | 5.7903 | -115.3634 | 15.2459 | 156.2953 | 0.0051 | 0.0140 |
| 2024_09_20 22:00 | 3254322 | 2 | 7.6998 | 9.6232 | -116.8335 | 19.4453 | 80.5021 | 0.0186 | 0.0135 |
| 2024_09_20 22:00 | 3262724 | 3 | 11.4087 | 17.7147 | -114.7377 | 15.9767 | 120.2647 | 0.0036 | 0.0029 |
| 2024_09_20 22:00 | 3240703 | 4 | 10.8438 | 8.4976 | -117.0766 | 16.4889 | 81.5503 | 0.0046 | 0.0165 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412742_CBD054AB | 504990 | 115 | -87.2 | 504990 | 834 | -91.4 | 504990 | 641 | -97.4 | 504990 | 152 |
| MR_1774412742_C955BA8F | 504990 | 115 | -88.4 | 504990 | 834 | -89.8 | 504990 | 641 | -97.4 | 504990 | 152 |
| MR_1774412742_A5F7C877 | 504990 | 115 | -89.9 | 504990 | 834 | -90.9 | 504990 | 641 | -95.3 | 504990 | 152 |
| MR_1774412742_6DB865E7 | 504990 | 115 | -87.4 | 504990 | 834 | -91.5 | 504990 | 641 | -95.2 | 504990 | 152 |
| MR_1774412742_601A25E9 | 504990 | 115 | -89.9 | 504990 | 834 | -91.4 | 504990 | 641 | -96.2 | 504990 | 152 |
| MR_1774412742_70427CEA | 504990 | 115 | -89.7 | 504990 | 834 | -90.7 | 504990 | 641 | -96.0 | 504990 | 152 |
| MR_1774412742_B6E6A126 | 504990 | 115 | -90.8 | 504990 | 834 | -91.0 | 504990 | 641 | -95.0 | 504990 | 152 |
| MR_1774412742_65F6623D | 504990 | 115 | -90.0 | 504990 | 834 | -91.6 | 504990 | 641 | -97.2 | 504990 | 152 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 421: `dabca732-6b6...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `dabca732-6b66-49c5-ba5b-b2ac8cca1437` |
| Tag | **multiple-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[421] topology](images/test_0421.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle  of 3264203_4 by 2 degrees
- `C2`: Adjust the azimuth of 3218042_2 by 50 degrees
- `C3`: Increase transmission power for 3218042_2
- `C4`: Increase A3 Offset threshold for 3218042_2
- `C5`: Decrease transmission power for 3264203_4
- `C6`: Increase A3 Offset threshold for 3264203_4
- `C7`: Increase transmission power for 3264203_4
- `C8`: Check test server and transmission issues
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3218042_2
- `C10`: Decrease A3 Offset threshold for 3264203_4
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3264203_4
- `C12`: Add neighbor relationship between 3214437_3 and 3264203_4
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3218042_2
- `C14`: Press down the tilt angle of 3218042_2 by 6 degrees
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3264203_4
- `C16`: Adjust the azimuth of 3264203_4 by 23 degrees
- `C17`: Decrease transmission power for 3218042_2
- `C18`: Insufficient data; more data is needed for judgment.
- `C19`: Add neighbor relationship between 3218042_2 and 3264203_4
- `C20`: Press down the tilt angle  of 3264203_4 by 2 degrees
- `C21`: Decrease A3 Offset threshold for 3218042_2
- `C22`: Lift the tilt angle of 3218042_2 by 6 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.444 | MS1 | 121.4656660320 | 31.1446347152 | 277 | 504990 | -83.25 | 17.47 | 467.35 | 0.10 | 2.43 | 1580 |
| 2024-09-20 22:21:32.618 | MS1 | 121.4656591047 | 31.1446225376 | 277 | 504990 | -77.00 | 13.07 | 436.39 | 0.13 | 2.08 | 1593 |
| 2024-09-20 22:21:33.711 | MS1 | 121.4656615649 | 31.1446223095 | 277 | 504990 | -76.04 | 12.74 | 348.28 | 0.16 | 2.64 | 1599 |
| 2024-09-20 22:21:34.287 | MS1 | 121.4656751640 | 31.1446214404 | 277 | 504990 | -85.16 | 2.25 | 96.72 | 0.17 | 1.13 | 1569 |
| 2024-09-20 22:21:35.646 | MS1 | 121.4656627231 | 31.1446353868 | 277 | 504990 | -86.06 | 0.60 | 77.33 | 0.09 | 1.31 | 1569 |
| 2024-09-20 22:21:36.730 | MS1 | 121.4656733877 | 31.1446220863 | 277 | 504990 | -88.67 | 1.38 | 66.53 | 0.12 | 1.05 | 1569 |
| 2024-09-20 22:21:37.485 | MS1 | 121.4656602064 | 31.1446301171 | 277 | 504990 | -94.49 | 0.83 | 44.77 | 0.05 | 1.48 | 1583 |
| 2024-09-20 22:21:38.341 | MS1 | 121.4656729804 | 31.1446344091 | 277 | 504990 | -94.04 | 2.96 | 45.50 | 0.16 | 1.03 | 1566 |
| 2024-09-20 22:21:39.846 | MS1 | 121.4656701687 | 31.1446184963 | 277 | 504990 | -93.07 | 2.71 | 54.48 | 0.02 | 1.12 | 1580 |
| 2024-09-20 22:21:40.480 | MS1 | 121.4656622592 | 31.1446362364 | 277 | 504990 | -78.38 | 15.62 | 466.47 | 0.17 | 2.31 | 1569 |
| 2024-09-20 22:21:41.793 | MS1 | 121.4656752444 | 31.1446356339 | 277 | 504990 | -82.11 | 16.23 | 345.31 | 0.01 | 2.66 | 1582 |
| 2024-09-20 22:21:42.619 | MS1 | 121.4656756702 | 31.1446190473 | 277 | 504990 | -79.34 | 15.95 | 574.24 | 0.17 | 2.23 | 1587 |

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
| 3213340 | 1 | 121.4660633063 | 31.1452670181 | 178 | 8 | 2 | 39.2 | TDD | 138 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3214437 | 3 | 121.4710160280 | 31.1502388346 | 224 | 12 | 3 | 42.5 | TDD | 861 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3218042 | 2 | 121.4640431100 | 31.1500905087 | 116 | 4 | 0 | 18.8 | TDD | 277 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3264203 | 4 | 121.4656612286 | 31.1537970800 | 203 | 1 | 1 | 25.6 | TDD | 22 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |

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
| 2024-09-20 22:21:31.041 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.057 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.177 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.177 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3213340 | 1 | 15.1719 | 6.7522 | -115.6884 | 14.8674 | 192.5505 | 0.0098 | 0.0178 |
| 2024_09_20 22:00 | 3218042 | 2 | 14.1452 | 6.5412 | -108.4413 | 12.4121 | 111.2959 | 0.0029 | 0.0093 |
| 2024_09_20 22:00 | 3214437 | 3 | 11.6036 | 7.1761 | -114.6416 | 18.4355 | 133.5882 | 0.0060 | 0.0104 |
| 2024_09_20 22:00 | 3264203 | 4 | 7.6025 | 14.5093 | -116.2904 | 13.1968 | 157.6150 | 0.0012 | 0.0029 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416295_4599C812 | 504990 | 277 | -86.1 | 504990 | 22 | -85.4 | 504990 | 861 | -87.5 | 504990 | 138 |
| MR_1774416295_B3320CA1 | 504990 | 277 | -84.1 | 504990 | 22 | -83.7 | 504990 | 861 | -86.3 | 504990 | 138 |
| MR_1774416295_4937A26E | 504990 | 277 | -83.4 | 504990 | 22 | -84.1 | 504990 | 861 | -87.9 | 504990 | 138 |
| MR_1774416295_50131725 | 504990 | 22 | -84.1 | 504990 | 277 | -83.1 | 504990 | 861 | -86.6 | 504990 | 138 |
| MR_1774416295_C90F0755 | 504990 | 277 | -83.5 | 504990 | 22 | -84.0 | 504990 | 861 | -84.3 | 504990 | 138 |
| MR_1774416295_E26A3F1D | 504990 | 277 | -86.6 | 504990 | 22 | -84.6 | 504990 | 861 | -86.7 | 504990 | 138 |
| MR_1774416295_906E39B1 | 504990 | 277 | -86.6 | 504990 | 22 | -86.7 | 504990 | 861 | -86.7 | 504990 | 138 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 422: `c92759f6-59b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `c92759f6-59b4-41ea-9248-16b1a73dd166` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[422] topology](images/test_0422.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment.
- `C2`: Add neighbor relationship between 3242021_3 and 3259493_2
- `C3`: Increase A3 Offset threshold for 3274495_1
- `C4`: Decrease A3 Offset threshold for 3259493_2
- `C5`: Lift the tilt angle  of 3259493_2 by 7 degrees
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3259493_2
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3274495_1
- `C8`: Adjust the azimuth of 3259493_2 by 27 degrees
- `C9`: Adjust the azimuth of 3274495_1 by 50 degrees
- `C10`: Increase transmission power for 3274495_1
- `C11`: Increase transmission power for 3259493_2
- `C12`: Decrease transmission power for 3259493_2
- `C13`: Press down the tilt angle of 3274495_1 by 10 degrees
- `C14`: Increase A3 Offset threshold for 3259493_2
- `C15`: Check test server and transmission issues
- `C16`: Lift the tilt angle of 3274495_1 by 10 degrees
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3259493_2
- `C18`: Add neighbor relationship between 3274495_1 and 3259493_2
- `C19`: Press down the tilt angle  of 3259493_2 by 7 degrees
- `C20`: Decrease transmission power for 3274495_1
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3274495_1
- `C22`: Decrease A3 Offset threshold for 3274495_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.101 | MS1 | 121.4656662075 | 31.1446300126 | 432 | 504990 | -88.99 | 16.97 | 429.47 | 0.09 | 2.73 | 1578 |
| 2024-09-20 22:21:32.781 | MS1 | 121.4656626283 | 31.1446239858 | 432 | 504990 | -90.34 | 17.30 | 383.78 | 0.12 | 2.45 | 1585 |
| 2024-09-20 22:21:33.584 | MS1 | 121.4656696243 | 31.1446274041 | 432 | 504990 | -89.98 | 12.54 | 316.92 | 0.19 | 2.02 | 1587 |
| 2024-09-20 22:21:34.232 | MS1 | 121.4656720730 | 31.1446370337 | 432 | 504990 | -87.07 | 12.29 | 68.68 | 0.08 | 2.04 | 1564 |
| 2024-09-20 22:21:35.419 | MS1 | 121.4656696962 | 31.1446363385 | 432 | 504990 | -88.82 | 14.32 | 72.99 | 0.20 | 2.45 | 1590 |
| 2024-09-20 22:21:36.221 | MS1 | 121.4656616701 | 31.1446301761 | 432 | 504990 | -91.97 | 16.53 | 104.81 | 0.03 | 2.84 | 1594 |
| 2024-09-20 22:21:37.513 | MS1 | 121.4656677686 | 31.1446271405 | 432 | 504990 | -93.96 | 9.04 | 85.27 | 0.07 | 2.29 | 1577 |
| 2024-09-20 22:21:38.341 | MS1 | 121.4656734228 | 31.1446341622 | 432 | 504990 | -89.69 | 12.88 | 68.01 | 0.14 | 2.40 | 1595 |
| 2024-09-20 22:21:39.580 | MS1 | 121.4656667748 | 31.1446295085 | 432 | 504990 | -93.13 | 11.87 | 61.86 | 0.12 | 2.54 | 1571 |
| 2024-09-20 22:21:40.178 | MS1 | 121.4656747446 | 31.1446304911 | 432 | 504990 | -91.66 | 8.10 | 520.17 | 0.06 | 2.29 | 1581 |
| 2024-09-20 22:21:41.964 | MS1 | 121.4656623547 | 31.1446341600 | 432 | 504990 | -92.12 | 10.28 | 463.71 | 0.06 | 2.78 | 1569 |
| 2024-09-20 22:21:42.279 | MS1 | 121.4656720328 | 31.1446359236 | 432 | 504990 | -90.11 | 10.66 | 483.84 | 0.16 | 2.81 | 1566 |

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
| 3214009 | 4 | 121.4719599862 | 31.1469626401 | 57 | 2 | 2 | 34.8 | TDD | 437 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3242021 | 3 | 121.4648528799 | 31.1520345547 | 250 | 14 | 8 | 22.9 | TDD | 283 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3259493 | 2 | 121.4719166201 | 31.1472552037 | 217 | 3 | 0 | 40.9 | TDD | 161 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3274495 | 1 | 121.4646528040 | 31.1476559359 | 276 | 14 | 1 | 23.2 | TDD | 432 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |

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
| 2024-09-20 22:21:31.516 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.539 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.673 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.673 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.348 | NREventA3 | measId:2;ServCellPCI:460;Se... |
| 2024-09-20 22:21:38.588 | NRHandoverAttempt | SourcePCI:460;SourceNR-ARFC... |
| 2024-09-20 22:21:38.626 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.638 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.750 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.750 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3274495 | 1 | 76.8969 | 80.5756 | -114.0935 | 15.4026 | 176.3029 | 0.0076 | 0.0197 |
| 2024_09_19 22:00 | 3259493 | 2 | 88.7681 | 76.4330 | -114.7356 | 19.0579 | 170.4869 | 0.0175 | 0.0051 |
| 2024_09_19 22:00 | 3242021 | 3 | 92.7112 | 86.7270 | -114.6506 | 5.3079 | 190.5992 | 0.0034 | 0.0120 |
| 2024_09_19 22:00 | 3214009 | 4 | 81.6935 | 83.2010 | -117.4883 | 7.0499 | 167.7011 | 0.0051 | 0.0060 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414902_E3298281 | 504990 | 432 | -87.4 | 504990 | 161 | -93.4 | 504990 | 283 | -95.4 | 504990 | 437 |
| MR_1774414902_199C53D2 | 504990 | 432 | -88.5 | 504990 | 161 | -95.1 | 504990 | 283 | -95.6 | 504990 | 437 |
| MR_1774414902_7575929F | 504990 | 432 | -87.7 | 504990 | 161 | -94.8 | 504990 | 283 | -95.8 | 504990 | 437 |
| MR_1774414902_0C650D86 | 504990 | 432 | -88.5 | 504990 | 161 | -92.4 | 504990 | 283 | -94.8 | 504990 | 437 |
| MR_1774414902_D90117F6 | 504990 | 432 | -86.7 | 504990 | 161 | -93.1 | 504990 | 283 | -96.5 | 504990 | 437 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 423: `87f2ea40-2bc...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `87f2ea40-2bc5-463d-89a1-4b595641adfd` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[423] topology](images/test_0423.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3248672_2
- `C2`: Adjust the azimuth of 3248672_2 by 50 degrees
- `C3`: Insufficient data; more data is needed for judgment.
- `C4`: Increase A3 Offset threshold for 3248672_2
- `C5`: Decrease transmission power for 3248672_2
- `C6`: Increase transmission power for 3232636_1
- `C7`: Adjust the azimuth of 3232636_1 by 21 degrees
- `C8`: Increase transmission power for 3248672_2
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3232636_1
- `C10`: Decrease A3 Offset threshold for 3232636_1
- `C11`: Press down the tilt angle  of 3232636_1 by 2 degrees
- `C12`: Press down the tilt angle of 3248672_2 by 10 degrees
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3248672_2
- `C14`: Decrease transmission power for 3232636_1
- `C15`: Lift the tilt angle  of 3232636_1 by 2 degrees
- `C16`: Increase A3 Offset threshold for 3232636_1
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3248672_2
- `C18`: Lift the tilt angle of 3248672_2 by 10 degrees
- `C19`: Add neighbor relationship between 3248672_2 and 3232636_1
- `C20`: Add neighbor relationship between 3261666_4 and 3232636_1
- `C21`: Check test server and transmission issues
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3232636_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.112 | MS1 | 121.4656585025 | 31.1446292579 | 554 | 504990 | -81.30 | 17.93 | 601.51 | 0.08 | 2.39 | 1564 |
| 2024-09-20 22:21:32.400 | MS1 | 121.4656580826 | 31.1446301352 | 554 | 504990 | -80.63 | 14.67 | 570.45 | 0.16 | 2.25 | 1584 |
| 2024-09-20 22:21:33.751 | MS1 | 121.4656593990 | 31.1446216236 | 554 | 504990 | -83.11 | 13.05 | 384.46 | 0.18 | 2.06 | 1592 |
| 2024-09-20 22:21:34.542 | MS1 | 121.4656640672 | 31.1446316000 | 554 | 504990 | -91.94 | -3.70 | 49.70 | 0.06 | 1.26 | 1597 |
| 2024-09-20 22:21:35.372 | MS1 | 121.4656692528 | 31.1446312634 | 554 | 504990 | -90.64 | -0.96 | 63.04 | 0.01 | 1.11 | 1582 |
| 2024-09-20 22:21:36.568 | MS1 | 121.4656671543 | 31.1446259632 | 554 | 504990 | -91.10 | -0.52 | 66.40 | 0.14 | 1.43 | 1574 |
| 2024-09-20 22:21:37.691 | MS1 | 121.4656616490 | 31.1446344893 | 554 | 504990 | -92.41 | -3.09 | 56.45 | 0.06 | 1.49 | 1566 |
| 2024-09-20 22:21:38.490 | MS1 | 121.4656630997 | 31.1446233853 | 554 | 504990 | -84.53 | 16.15 | 459.12 | 0.17 | 1.23 | 1565 |
| 2024-09-20 22:21:39.325 | MS1 | 121.4656640036 | 31.1446240977 | 554 | 504990 | -85.00 | 17.27 | 431.33 | 0.14 | 1.20 | 1565 |
| 2024-09-20 22:21:40.604 | MS1 | 121.4656594257 | 31.1446337389 | 554 | 504990 | -84.76 | 13.68 | 353.00 | 0.07 | 2.38 | 1590 |
| 2024-09-20 22:21:41.358 | MS1 | 121.4656667020 | 31.1446312686 | 554 | 504990 | -76.26 | 16.32 | 375.72 | 0.11 | 2.72 | 1589 |
| 2024-09-20 22:21:42.442 | MS1 | 121.4656619702 | 31.1446331797 | 554 | 504990 | -77.27 | 14.46 | 357.00 | 0.02 | 2.10 | 1595 |

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
| 3230734 | 3 | 121.4710725832 | 31.1474059086 | 14 | 10 | 11 | 40.8 | TDD | 473 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3232636 | 1 | 121.4746288279 | 31.1440292472 | 253 | 0 | 2 | 23.2 | TDD | 489 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3248672 | 2 | 121.4664256030 | 31.1495471511 | 341 | 12 | 3 | 18.0 | TDD | 554 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3261666 | 4 | 121.4671461899 | 31.1507520720 | 214 | 1 | 3 | 30.7 | TDD | 662 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |

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
| 2024-09-20 22:21:31.321 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.343 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.474 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.474 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.220 | NREventA3 | measId:2;ServCellPCI:927;Se... |
| 2024-09-20 22:21:36.220 | NREventA3 | measId:2;ServCellPCI:927;Se... |
| 2024-09-20 22:21:37.220 | NREventA3 | measId:2;ServCellPCI:927;Se... |
| 2024-09-20 22:21:39.720 | NRRRCReestablishAttempt | PCI:927 |
| 2024-09-20 22:21:39.730 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.742 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:39.884 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.884 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3232636 | 1 | 18.2047 | 19.9967 | -117.5610 | 14.8667 | 126.1565 | 0.0167 | 0.0107 |
| 2024_09_20 22:00 | 3248672 | 2 | 10.5462 | 5.3755 | -117.4056 | 16.9249 | 151.8054 | 0.0043 | 0.1993 |
| 2024_09_20 22:00 | 3230734 | 3 | 18.5164 | 11.9726 | -114.5856 | 14.6152 | 179.6721 | 0.0038 | 0.0148 |
| 2024_09_20 22:00 | 3261666 | 4 | 9.4720 | 9.7808 | -115.8185 | 7.5400 | 103.3124 | 0.0017 | 0.0087 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415656_CA69A5C3 | 504990 | 554 | -90.5 | 504990 | 489 | -86.2 | 504990 | 662 | -87.3 | 504990 | 473 |
| MR_1774415656_F302653B | 504990 | 489 | -85.1 | 504990 | 554 | -91.4 | 504990 | 662 | -85.7 | 504990 | 473 |
| MR_1774415656_A3F73F1C | 504990 | 489 | -86.0 | 504990 | 554 | -93.2 | 504990 | 662 | -87.1 | 504990 | 473 |
| MR_1774415656_D9E3270B | 504990 | 554 | -92.4 | 504990 | 489 | -85.5 | 504990 | 662 | -86.7 | 504990 | 473 |
| MR_1774415656_45EDA609 | 504990 | 554 | -90.4 | 504990 | 489 | -85.3 | 504990 | 662 | -86.4 | 504990 | 473 |
| MR_1774415656_DF5EEC34 | 504990 | 554 | -91.6 | 504990 | 489 | -85.1 | 504990 | 662 | -85.2 | 504990 | 473 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 424: `0a7dad77-54c...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `0a7dad77-54c7-4efb-9ae4-1cdb2507cda1` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[424] topology](images/test_0424.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3215448_2 and 3213514_4
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3213514_4
- `C3`: Press down the tilt angle  of 3213514_4 by 3 degrees
- `C4`: Lift the tilt angle of 3215448_2 by 10 degrees
- `C5`: Increase A3 Offset threshold for 3215448_2
- `C6`: Decrease transmission power for 3215448_2
- `C7`: Lift the tilt angle  of 3213514_4 by 3 degrees
- `C8`: Decrease transmission power for 3213514_4
- `C9`: Check test server and transmission issues
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3213514_4
- `C11`: Decrease A3 Offset threshold for 3213514_4
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3215448_2
- `C13`: Insufficient data; more data is needed for judgment.
- `C14`: Press down the tilt angle of 3215448_2 by 10 degrees
- `C15`: Increase transmission power for 3213514_4
- `C16`: Add neighbor relationship between 3223973_1 and 3213514_4
- `C17`: Increase A3 Offset threshold for 3213514_4
- `C18`: Adjust the azimuth of 3215448_2 by 41 degrees
- `C19`: Increase transmission power for 3215448_2
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3215448_2
- `C21`: Adjust the azimuth of 3213514_4 by 50 degrees
- `C22`: Decrease A3 Offset threshold for 3215448_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.933 | MS1 | 121.4656636375 | 31.1446200415 | 638 | 504990 | -87.70 | 17.59 | 381.16 | 0.11 | 2.70 | 1561 |
| 2024-09-20 22:21:32.202 | MS1 | 121.4656615156 | 31.1446195481 | 638 | 504990 | -87.42 | 17.86 | 408.62 | 0.01 | 2.25 | 1577 |
| 2024-09-20 22:21:33.225 | MS1 | 121.4656644457 | 31.1446230113 | 638 | 504990 | -87.47 | 13.96 | 587.35 | 0.06 | 2.18 | 1596 |
| 2024-09-20 22:21:34.691 | MS1 | 121.4656761366 | 31.1446196772 | 638 | 504990 | -90.93 | 16.78 | 58.19 | 0.10 | 2.97 | 1599 |
| 2024-09-20 22:21:35.402 | MS1 | 121.4656736871 | 31.1446180714 | 638 | 504990 | -91.83 | 17.35 | 60.98 | 0.09 | 2.93 | 1574 |
| 2024-09-20 22:21:36.398 | MS1 | 121.4656755161 | 31.1446222267 | 638 | 504990 | -86.88 | 16.13 | 80.73 | 0.12 | 2.76 | 1569 |
| 2024-09-20 22:21:37.729 | MS1 | 121.4656670972 | 31.1446291215 | 638 | 504990 | -89.78 | 7.54 | 74.28 | 0.17 | 2.03 | 1598 |
| 2024-09-20 22:21:38.880 | MS1 | 121.4656633325 | 31.1446271796 | 638 | 504990 | -90.80 | 12.85 | 78.74 | 0.09 | 2.57 | 1568 |
| 2024-09-20 22:21:39.905 | MS1 | 121.4656715749 | 31.1446227249 | 638 | 504990 | -93.14 | 8.80 | 86.99 | 0.02 | 2.04 | 1576 |
| 2024-09-20 22:21:40.674 | MS1 | 121.4656753160 | 31.1446216861 | 638 | 504990 | -92.48 | 7.63 | 554.07 | 0.09 | 2.69 | 1561 |
| 2024-09-20 22:21:41.145 | MS1 | 121.4656725401 | 31.1446350120 | 638 | 504990 | -91.46 | 10.18 | 555.52 | 0.08 | 2.06 | 1571 |
| 2024-09-20 22:21:42.584 | MS1 | 121.4656731599 | 31.1446352334 | 638 | 504990 | -92.74 | 7.83 | 383.43 | 0.06 | 2.13 | 1583 |

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
| 3213514 | 4 | 121.4693777434 | 31.1469605011 | 112 | 0 | 3 | 20.9 | TDD | 654 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3215448 | 2 | 121.4725762647 | 31.1518511519 | 178 | 14 | 3 | 24.3 | TDD | 638 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3223973 | 1 | 121.4717320891 | 31.1467002856 | 236 | 14 | 12 | 46.2 | TDD | 610 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3238238 | 3 | 121.4713665101 | 31.1500756319 | 310 | 13 | 12 | 41.8 | TDD | 997 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |

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
| 2024-09-20 22:21:30.790 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.810 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:30.912 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.912 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.654 | NREventA3 | measId:2;ServCellPCI:181;Se... |
| 2024-09-20 22:21:37.894 | NRHandoverAttempt | SourcePCI:181;SourceNR-ARFC... |
| 2024-09-20 22:21:37.942 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.955 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.081 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.081 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3223973 | 1 | 76.1232 | 94.7316 | -117.3585 | 11.3035 | 85.1080 | 0.0067 | 0.0080 |
| 2024_09_19 22:00 | 3215448 | 2 | 84.7271 | 79.6849 | -116.4763 | 10.9268 | 129.1002 | 0.0121 | 0.0140 |
| 2024_09_19 22:00 | 3238238 | 3 | 91.8203 | 93.0521 | -116.5183 | 11.7020 | 99.2543 | 0.0102 | 0.0101 |
| 2024_09_19 22:00 | 3213514 | 4 | 85.8256 | 90.6486 | -117.5856 | 19.1853 | 188.5971 | 0.0067 | 0.0119 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413563_2C277191 | 504990 | 638 | -91.0 | 504990 | 654 | -97.2 | 504990 | 610 | -101.4 | 504990 | 997 |
| MR_1774413563_CA76183F | 504990 | 638 | -91.1 | 504990 | 654 | -98.8 | 504990 | 610 | -103.7 | 504990 | 997 |
| MR_1774413563_3E17870D | 504990 | 638 | -92.1 | 504990 | 654 | -96.6 | 504990 | 610 | -104.6 | 504990 | 997 |
| MR_1774413563_68EB5046 | 504990 | 638 | -90.1 | 504990 | 654 | -96.0 | 504990 | 610 | -104.7 | 504990 | 997 |
| MR_1774413563_32A17EBF | 504990 | 638 | -92.9 | 504990 | 654 | -98.2 | 504990 | 610 | -101.6 | 504990 | 997 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 425: `9a924492-dc1...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `9a924492-dc1f-467f-b815-b82be0bfef98` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[425] topology](images/test_0425.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3210730_4
- `C2`: Add neighbor relationship between 3253338_1 and 3210730_4
- `C3`: Press down the tilt angle of 3240455_2 by 4 degrees
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3210730_4
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3240455_2
- `C6`: Increase transmission power for 3210730_4
- `C7`: Decrease A3 Offset threshold for 3240455_2
- `C8`: Adjust the azimuth of 3210730_4 by 33 degrees
- `C9`: Decrease transmission power for 3210730_4
- `C10`: Lift the tilt angle of 3240455_2 by 4 degrees
- `C11`: Decrease A3 Offset threshold for 3210730_4
- `C12`: Decrease transmission power for 3240455_2
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3210730_4
- `C14`: Adjust the azimuth of 3240455_2 by 50 degrees
- `C15`: Insufficient data; more data is needed for judgment.
- `C16`: Press down the tilt angle  of 3210730_4 by 3 degrees
- `C17`: Increase transmission power for 3240455_2
- `C18`: Lift the tilt angle  of 3210730_4 by 3 degrees
- `C19`: Check test server and transmission issues
- `C20`: Increase A3 Offset threshold for 3240455_2
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3240455_2
- `C22`: Add neighbor relationship between 3240455_2 and 3210730_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.189 | MS1 | 121.4656699363 | 31.1446290792 | 411 | 504990 | -83.97 | 16.70 | 521.87 | 0.16 | 2.72 | 1589 |
| 2024-09-20 22:21:32.882 | MS1 | 121.4656685858 | 31.1446352826 | 411 | 504990 | -81.07 | 12.39 | 467.74 | 0.08 | 2.48 | 1573 |
| 2024-09-20 22:21:33.433 | MS1 | 121.4656612544 | 31.1446242507 | 411 | 504990 | -77.18 | 16.92 | 412.03 | 0.04 | 2.01 | 1590 |
| 2024-09-20 22:21:34.852 | MS1 | 121.4656598412 | 31.1446203442 | 411 | 504990 | -93.93 | -0.96 | 37.81 | 0.07 | 1.06 | 1560 |
| 2024-09-20 22:21:35.356 | MS1 | 121.4656755139 | 31.1446337167 | 411 | 504990 | -89.40 | -3.73 | 66.14 | 0.05 | 1.32 | 1566 |
| 2024-09-20 22:21:36.351 | MS1 | 121.4656747084 | 31.1446225467 | 411 | 504990 | -90.73 | -2.63 | 61.74 | 0.16 | 1.14 | 1560 |
| 2024-09-20 22:21:37.596 | MS1 | 121.4656731637 | 31.1446278759 | 411 | 504990 | -90.95 | -2.24 | 60.74 | 0.06 | 1.09 | 1598 |
| 2024-09-20 22:21:38.835 | MS1 | 121.4656668941 | 31.1446349697 | 411 | 504990 | -80.91 | 15.24 | 306.28 | 0.09 | 1.29 | 1582 |
| 2024-09-20 22:21:39.877 | MS1 | 121.4656707255 | 31.1446361310 | 411 | 504990 | -78.12 | 14.99 | 507.31 | 0.02 | 1.34 | 1584 |
| 2024-09-20 22:21:40.152 | MS1 | 121.4656673410 | 31.1446257313 | 411 | 504990 | -77.40 | 14.46 | 573.38 | 0.13 | 2.61 | 1566 |
| 2024-09-20 22:21:41.402 | MS1 | 121.4656600060 | 31.1446240399 | 411 | 504990 | -78.80 | 12.28 | 379.10 | 0.16 | 2.93 | 1578 |
| 2024-09-20 22:21:42.510 | MS1 | 121.4656716527 | 31.1446206283 | 411 | 504990 | -77.57 | 15.78 | 412.65 | 0.16 | 2.18 | 1590 |

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
| 3210730 | 4 | 121.4659046237 | 31.1510143576 | 149 | 0 | 5 | 38.4 | TDD | 302 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3224647 | 3 | 121.4711371978 | 31.1480371769 | 95 | 0 | 6 | 17.7 | TDD | 667 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3240455 | 2 | 121.4725567262 | 31.1463824984 | 137 | 1 | 9 | 31.2 | TDD | 411 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3253338 | 1 | 121.4730292204 | 31.1500378947 | 224 | 13 | 7 | 28.0 | TDD | 331 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:31.236 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.251 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.375 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.375 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.099 | NREventA3 | measId:2;ServCellPCI:327;Se... |
| 2024-09-20 22:21:36.099 | NREventA3 | measId:2;ServCellPCI:327;Se... |
| 2024-09-20 22:21:37.099 | NREventA3 | measId:2;ServCellPCI:327;Se... |
| 2024-09-20 22:21:39.599 | NRRRCReestablishAttempt | PCI:327 |
| 2024-09-20 22:21:39.615 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.629 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:39.777 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.777 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3253338 | 1 | 17.3341 | 5.4653 | -117.8078 | 5.6303 | 125.0685 | 0.0067 | 0.0073 |
| 2024_09_20 22:00 | 3240455 | 2 | 14.7842 | 9.2300 | -117.5856 | 7.3614 | 125.1212 | 0.0044 | 0.1484 |
| 2024_09_20 22:00 | 3224647 | 3 | 10.9543 | 13.8024 | -117.5765 | 15.2982 | 137.6481 | 0.0041 | 0.0138 |
| 2024_09_20 22:00 | 3210730 | 4 | 10.5351 | 12.7491 | -116.9737 | 12.8012 | 98.5530 | 0.0004 | 0.0192 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412919_2873BAAD | 504990 | 411 | -93.9 | 504990 | 302 | -88.0 | 504990 | 331 | -92.8 | 504990 | 667 |
| MR_1774412919_E422FA3E | 504990 | 302 | -88.0 | 504990 | 411 | -93.2 | 504990 | 331 | -90.2 | 504990 | 667 |
| MR_1774412919_0D4D7C47 | 504990 | 302 | -89.2 | 504990 | 411 | -93.4 | 504990 | 331 | -91.3 | 504990 | 667 |
| MR_1774412919_BE8D95D7 | 504990 | 302 | -89.9 | 504990 | 411 | -95.1 | 504990 | 331 | -92.4 | 504990 | 667 |
| MR_1774412919_65B00985 | 504990 | 302 | -90.3 | 504990 | 411 | -95.6 | 504990 | 331 | -92.6 | 504990 | 667 |
| MR_1774412919_4A0FA90E | 504990 | 302 | -88.5 | 504990 | 411 | -93.4 | 504990 | 331 | -90.7 | 504990 | 667 |
| MR_1774412919_3589325B | 504990 | 411 | -93.7 | 504990 | 302 | -87.5 | 504990 | 331 | -91.0 | 504990 | 667 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 426: `8205389e-d63...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `8205389e-d634-4007-8260-f333bbdf4d10` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[426] topology](images/test_0426.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3261709_4 and 3263178_3
- `C2`: Increase transmission power for 3273979_1
- `C3`: Lift the tilt angle  of 3263178_3 by 10 degrees
- `C4`: Decrease transmission power for 3263178_3
- `C5`: Add neighbor relationship between 3273979_1 and 3263178_3
- `C6`: Press down the tilt angle  of 3263178_3 by 10 degrees
- `C7`: Press down the tilt angle of 3273979_1 by 2 degrees
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3263178_3
- `C9`: Adjust the azimuth of 3273979_1 by 50 degrees
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3273979_1
- `C11`: Check test server and transmission issues
- `C12`: Increase A3 Offset threshold for 3263178_3
- `C13`: Adjust the azimuth of 3263178_3 by 50 degrees
- `C14`: Lift the tilt angle of 3273979_1 by 2 degrees
- `C15`: Decrease A3 Offset threshold for 3273979_1
- `C16`: Decrease A3 Offset threshold for 3263178_3
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3263178_3
- `C18`: Increase A3 Offset threshold for 3273979_1
- `C19`: Insufficient data; more data is needed for judgment.
- `C20`: Decrease transmission power for 3273979_1
- `C21`: Increase transmission power for 3263178_3
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3273979_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.510 | MS1 | 121.4656633236 | 31.1446254699 | 432 | 504990 | -77.66 | 15.85 | 583.99 | 0.02 | 2.79 | 1579 |
| 2024-09-20 22:21:32.379 | MS1 | 121.4656673788 | 31.1446335249 | 432 | 504990 | -83.71 | 12.71 | 589.51 | 0.13 | 2.95 | 1580 |
| 2024-09-20 22:21:33.915 | MS1 | 121.4656620850 | 31.1446332824 | 432 | 504990 | -83.12 | 17.93 | 388.18 | 0.01 | 2.62 | 1590 |
| 2024-09-20 22:21:34.728 | MS1 | 121.4656721655 | 31.1446207410 | 432 | 504990 | -84.84 | -1.38 | 43.68 | 0.05 | 1.36 | 1585 |
| 2024-09-20 22:21:35.379 | MS1 | 121.4656761475 | 31.1446205102 | 432 | 504990 | -83.87 | -2.01 | 29.93 | 0.09 | 1.06 | 1579 |
| 2024-09-20 22:21:36.592 | MS1 | 121.4656721138 | 31.1446309751 | 432 | 504990 | -88.92 | -2.34 | 29.96 | 0.01 | 1.15 | 1573 |
| 2024-09-20 22:21:37.197 | MS1 | 121.4656728710 | 31.1446270696 | 432 | 504990 | -83.80 | -0.22 | 33.62 | 0.17 | 1.46 | 1594 |
| 2024-09-20 22:21:38.537 | MS1 | 121.4656700508 | 31.1446303005 | 432 | 504990 | -88.08 | -0.70 | 76.27 | 0.01 | 1.09 | 1560 |
| 2024-09-20 22:21:39.170 | MS1 | 121.4656627739 | 31.1446226532 | 517 | 504990 | -82.36 | 15.54 | 209.14 | 0.02 | 1.08 | 1560 |
| 2024-09-20 22:21:40.411 | MS1 | 121.4656744162 | 31.1446343154 | 517 | 504990 | -83.00 | 14.65 | 361.69 | 0.04 | 2.57 | 1579 |
| 2024-09-20 22:21:41.767 | MS1 | 121.4656631546 | 31.1446199284 | 517 | 504990 | -80.53 | 13.00 | 432.73 | 0.19 | 2.94 | 1597 |
| 2024-09-20 22:21:42.262 | MS1 | 121.4656747192 | 31.1446287785 | 517 | 504990 | -79.83 | 12.23 | 415.47 | 0.06 | 2.89 | 1589 |

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
| 3256141 | 2 | 121.4703329525 | 31.1503569304 | 98 | 3 | 12 | 16.4 | TDD | 866 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3261709 | 4 | 121.4711084012 | 31.1550240526 | 150 | 15 | 8 | 25.7 | TDD | 254 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3263178 | 3 | 121.4693191742 | 31.1555605133 | 112 | 9 | 6 | 19.9 | TDD | 517 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3273979 | 1 | 121.4669802696 | 31.1532974451 | 285 | 1 | 11 | 24.4 | TDD | 432 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |

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
| 2024-09-20 22:21:31.488 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.503 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.649 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.649 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.324 | NREventA3 | measId:2;ServCellPCI:821;Se... |
| 2024-09-20 22:21:38.564 | NRHandoverAttempt | SourcePCI:821;SourceNR-ARFC... |
| 2024-09-20 22:21:38.603 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.614 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.715 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.715 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3273979 | 1 | 9.1165 | 11.5963 | -116.7890 | 7.7594 | 86.4339 | 0.0005 | 0.1695 |
| 2024_09_20 22:00 | 3256141 | 2 | 18.9569 | 11.4504 | -117.1989 | 14.5505 | 105.6301 | 0.0135 | 0.0137 |
| 2024_09_20 22:00 | 3263178 | 3 | 5.3474 | 6.4908 | -115.1522 | 6.8349 | 176.4565 | 0.0134 | 0.0018 |
| 2024_09_20 22:00 | 3261709 | 4 | 7.5335 | 16.9532 | -115.8565 | 17.3074 | 129.0896 | 0.0039 | 0.0104 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415678_545F8279 | 504990 | 517 | -78.1 | 504990 | 432 | -84.1 | 504990 | 254 | -78.4 | 504990 | 866 |
| MR_1774415678_8100EB62 | 504990 | 517 | -76.0 | 504990 | 432 | -85.1 | 504990 | 254 | -80.1 | 504990 | 866 |
| MR_1774415678_4DDC1341 | 504990 | 517 | -76.2 | 504990 | 432 | -84.1 | 504990 | 254 | -80.7 | 504990 | 866 |
| MR_1774415678_397424D7 | 504990 | 432 | -84.3 | 504990 | 517 | -75.4 | 504990 | 254 | -80.3 | 504990 | 866 |
| MR_1774415678_FB6DB679 | 504990 | 432 | -83.4 | 504990 | 517 | -76.0 | 504990 | 254 | -79.2 | 504990 | 866 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 427: `279df29d-cd9...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `279df29d-cd9e-4bd4-bdc3-e443a781f3ae` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[427] topology](images/test_0427.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3236186_4
- `C2`: Decrease transmission power for 3254391_1
- `C3`: Lift the tilt angle  of 3236186_4 by 8 degrees
- `C4`: Add neighbor relationship between 3215513_2 and 3236186_4
- `C5`: Decrease A3 Offset threshold for 3254391_1
- `C6`: Press down the tilt angle of 3254391_1 by 9 degrees
- `C7`: Increase A3 Offset threshold for 3254391_1
- `C8`: Check test server and transmission issues
- `C9`: Insufficient data; more data is needed for judgment.
- `C10`: Adjust the azimuth of 3254391_1 by 50 degrees
- `C11`: Adjust the azimuth of 3236186_4 by 4 degrees
- `C12`: Press down the tilt angle  of 3236186_4 by 8 degrees
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3236186_4
- `C14`: Lift the tilt angle of 3254391_1 by 9 degrees
- `C15`: Decrease A3 Offset threshold for 3236186_4
- `C16`: Increase transmission power for 3254391_1
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3236186_4
- `C18`: Increase A3 Offset threshold for 3236186_4
- `C19`: Increase transmission power for 3236186_4
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3254391_1
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3254391_1
- `C22`: Add neighbor relationship between 3254391_1 and 3236186_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.327 | MS1 | 121.4656773929 | 31.1446195285 | 864 | 504990 | -83.92 | 14.05 | 308.97 | 0.15 | 2.54 | 1581 |
| 2024-09-20 22:21:32.180 | MS1 | 121.4656607239 | 31.1446305833 | 864 | 504990 | -83.70 | 16.01 | 574.26 | 0.06 | 2.35 | 1582 |
| 2024-09-20 22:21:33.856 | MS1 | 121.4656601464 | 31.1446377274 | 864 | 504990 | -76.69 | 12.75 | 326.52 | 0.09 | 2.46 | 1575 |
| 2024-09-20 22:21:34.585 | MS1 | 121.4656612110 | 31.1446267974 | 864 | 504990 | -92.93 | -2.57 | 78.65 | 0.18 | 1.02 | 1573 |
| 2024-09-20 22:21:35.794 | MS1 | 121.4656732903 | 31.1446272072 | 864 | 504990 | -89.65 | -3.44 | 60.43 | 0.05 | 1.21 | 1598 |
| 2024-09-20 22:21:36.166 | MS1 | 121.4656612634 | 31.1446302593 | 864 | 504990 | -90.57 | -3.68 | 34.54 | 0.05 | 1.21 | 1567 |
| 2024-09-20 22:21:37.279 | MS1 | 121.4656600235 | 31.1446368257 | 864 | 504990 | -85.87 | -0.29 | 48.63 | 0.00 | 1.26 | 1569 |
| 2024-09-20 22:21:38.856 | MS1 | 121.4656642846 | 31.1446309376 | 864 | 504990 | -92.83 | -2.17 | 50.40 | 0.10 | 1.15 | 1572 |
| 2024-09-20 22:21:39.882 | MS1 | 121.4656716985 | 31.1446259903 | 814 | 504990 | -79.64 | 12.31 | 265.86 | 0.18 | 1.05 | 1563 |
| 2024-09-20 22:21:40.370 | MS1 | 121.4656669914 | 31.1446288052 | 814 | 504990 | -80.08 | 13.26 | 467.41 | 0.10 | 2.87 | 1581 |
| 2024-09-20 22:21:41.509 | MS1 | 121.4656746863 | 31.1446210533 | 814 | 504990 | -79.04 | 17.71 | 502.38 | 0.15 | 2.86 | 1575 |
| 2024-09-20 22:21:42.801 | MS1 | 121.4656612038 | 31.1446192978 | 814 | 504990 | -76.34 | 15.74 | 560.85 | 0.10 | 2.30 | 1581 |

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
| 3212100 | 3 | 121.4688676108 | 31.1527970945 | 79 | 14 | 0 | 16.4 | TDD | 309 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3215513 | 2 | 121.4697207373 | 31.1554233955 | 203 | 3 | 12 | 35.0 | TDD | 812 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3236186 | 4 | 121.4701504969 | 31.1551322801 | 196 | 6 | 6 | 37.1 | TDD | 814 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3254391 | 1 | 121.4708245465 | 31.1501834388 | 288 | 6 | 6 | 36.9 | TDD | 864 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:31.620 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.638 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.780 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.780 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.489 | NREventA3 | measId:2;ServCellPCI:568;Se... |
| 2024-09-20 22:21:38.729 | NRHandoverAttempt | SourcePCI:568;SourceNR-ARFC... |
| 2024-09-20 22:21:38.764 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.775 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.891 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.891 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3254391 | 1 | 16.5484 | 18.0797 | -116.8626 | 8.0873 | 197.9222 | 0.0177 | 0.1663 |
| 2024_09_20 22:00 | 3215513 | 2 | 7.0538 | 13.3856 | -116.7594 | 6.1919 | 101.2850 | 0.0073 | 0.0041 |
| 2024_09_20 22:00 | 3212100 | 3 | 17.4658 | 12.5147 | -117.8623 | 9.4822 | 170.0524 | 0.0008 | 0.0165 |
| 2024_09_20 22:00 | 3236186 | 4 | 15.4598 | 18.2498 | -117.5815 | 5.2319 | 175.0165 | 0.0041 | 0.0134 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414914_54289A8F | 504990 | 864 | -93.9 | 504990 | 814 | -87.2 | 504990 | 812 | -87.9 | 504990 | 309 |
| MR_1774414914_64912C65 | 504990 | 814 | -86.8 | 504990 | 864 | -91.4 | 504990 | 812 | -90.1 | 504990 | 309 |
| MR_1774414914_130A3B0A | 504990 | 814 | -87.3 | 504990 | 864 | -92.8 | 504990 | 812 | -89.6 | 504990 | 309 |
| MR_1774414914_4F4FB31F | 504990 | 864 | -91.9 | 504990 | 814 | -86.5 | 504990 | 812 | -86.6 | 504990 | 309 |
| MR_1774414914_2BF2600C | 504990 | 864 | -93.6 | 504990 | 814 | -89.1 | 504990 | 812 | -88.2 | 504990 | 309 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 428: `375b6cf0-1d6...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `375b6cf0-1d6d-46c0-8a81-ef9bf11ce9d6` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[428] topology](images/test_0428.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3235415_6 by 6 degrees
- `C2`: Check test server and transmission issues
- `C3`: Increase A3 Offset threshold for 3235415_6
- `C4`: Decrease A3 Offset threshold for 3235415_6
- `C5`: Add neighbor relationship between 3279863_10 and 3235415_6
- `C6`: Adjust the azimuth of 3235415_6 by 20 degrees
- `C7`: Add neighbor relationship between 3225528_5 and 3235415_6
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3235415_6
- `C9`: Increase A3 Offset threshold for 3225528_5
- `C10`: Adjust the azimuth of 3225528_5 by 17 degrees
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3225528_5
- `C12`: Lift the tilt angle of 3225528_5 by 3 degrees
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3225528_5
- `C14`: Decrease A3 Offset threshold for 3225528_5
- `C15`: Decrease transmission power for 3225528_5
- `C16`: Increase transmission power for 3235415_6
- `C17`: Decrease transmission power for 3235415_6
- `C18`: Lift the tilt angle  of 3235415_6 by 6 degrees
- `C19`: Press down the tilt angle of 3225528_5 by 3 degrees
- `C20`: Insufficient data; more data is needed for judgment.
- `C21`: Increase transmission power for 3225528_5
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3235415_6

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.956 | MS1 | 121.4656661073 | 31.1446214057 | 633 | 504990 | -95.45 | 10.39 | 543.66 | 0.16 | 2.39 | 1578 |
| 2024-09-20 22:21:32.651 | MS1 | 121.4656726280 | 31.1446298777 | 778 | 504990 | -95.12 | 12.34 | 460.04 | 0.12 | 2.77 | 1585 |
| 2024-09-20 22:21:33.839 | MS1 | 121.4656602404 | 31.1446302955 | 67 | 504990 | -94.95 | 13.00 | 541.38 | 0.15 | 2.18 | 1576 |
| 2024-09-20 22:21:34.165 | MS1 | 121.4656759318 | 31.1446300950 | 805 | 152650 | -92.84 | 2.33 | 86.42 | 0.09 | 1.93 | 988 |
| 2024-09-20 22:21:35.799 | MS1 | 121.4656610019 | 31.1446259088 | 978 | 152650 | -92.40 | 5.64 | 67.88 | 0.05 | 1.55 | 981 |
| 2024-09-20 22:21:36.591 | MS1 | 121.4656663128 | 31.1446349561 | 429 | 152650 | -89.08 | 5.79 | 47.06 | 0.01 | 1.70 | 917 |
| 2024-09-20 22:21:37.720 | MS1 | 121.4656706586 | 31.1446223136 | 52 | 152650 | -92.22 | 2.59 | 63.83 | 0.11 | 1.75 | 920 |
| 2024-09-20 22:21:38.634 | MS1 | 121.4656678979 | 31.1446254164 | 805 | 152650 | -91.78 | 2.14 | 60.43 | 0.18 | 1.57 | 916 |
| 2024-09-20 22:21:39.275 | MS1 | 121.4656675766 | 31.1446278447 | 978 | 152650 | -95.54 | 2.28 | 62.90 | 0.04 | 1.65 | 928 |
| 2024-09-20 22:21:40.206 | MS1 | 121.4656753164 | 31.1446303981 | 429 | 152650 | -89.03 | 4.78 | 51.22 | 0.17 | 2.96 | 1599 |
| 2024-09-20 22:21:41.517 | MS1 | 121.4656671618 | 31.1446291553 | 52 | 152650 | -93.70 | 7.81 | 62.93 | 0.17 | 2.69 | 1594 |
| 2024-09-20 22:21:42.977 | MS1 | 121.4656746862 | 31.1446208377 | 805 | 152650 | -87.03 | 3.47 | 57.38 | 0.16 | 2.73 | 1588 |

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
| 3214227 | 1 | 121.4725914175 | 31.1453825571 | 241 | 9 | 2 | 25.4 | TDD | 514 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3225528 | 5 | 121.4709835213 | 31.1539152835 | 189 | 2 | 1 | 27.5 | TDD | 633 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3235415 | 6 | 121.4679123664 | 31.1473450814 | 195 | 5 | 2 | 4.8 | TDD | 189 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3241382 | 2 | 121.4714399526 | 31.1548737118 | 15 | 6 | 8 | 17.6 | TDD | 67 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3243527 | 9 | 121.4665780564 | 31.1440557408 | 27 | 6 | 10 | 8.0 | FDD | 715 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |
| 3245779 | 3 | 121.4691337450 | 31.1492383686 | 89 | 14 | 2 | 5.5 | TDD | 778 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3251412 | 13 | 121.4701303373 | 31.1500719706 | 42 | 13 | 8 | 19.4 | FDD | 92 | n1 | 152650 | 30M | 4T4R | 15 | 152650 |
| 3252042 | 7 | 121.4726437978 | 31.1500449990 | 86 | 15 | 10 | 22.9 | FDD | 643 | n1 | 152650 | 30M | 4T4R | 25 | 152650 |
| 3254440 | 12 | 121.4701365519 | 31.1458822714 | 208 | 4 | 12 | 0.5 | FDD | 52 | n1 | 152650 | 30M | 4T4R | 26 | 152650 |
| 3262111 | 4 | 121.4753081066 | 31.1445146634 | 328 | 13 | 9 | 5.2 | TDD | 979 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3263150 | 11 | 121.4747724543 | 31.1463250728 | 99 | 12 | 0 | 1.9 | FDD | 978 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |
| 3263236 | 8 | 121.4741211392 | 31.1531057426 | 323 | 11 | 6 | 27.4 | FDD | 805 | n1 | 152650 | 30M | 4T4R | 18 | 152650 |
| 3279863 | 10 | 121.4649538818 | 31.1484565177 | 315 | 12 | 2 | 25.2 | FDD | 429 | n1 | 152650 | 30M | 4T4R | 10 | 152650 |

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
| 2024-09-20 22:21:31.276 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.297 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.427 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.427 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.114 | NREventA2 | measId:1;ServCellPCI:512;Se... |
| 2024-09-20 22:21:35.244 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.515 | NREventA5 | measId:3;ServCellPCI:512;Se... |
| 2024-09-20 22:21:35.549 | NRHandoverAttempt | SourcePCI:512;SourceNR-ARFC... |
| 2024-09-20 22:21:35.593 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.608 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:35.753 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.753 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3214227 | 1 | 13.0270 | 18.8137 | -114.1821 | 17.9368 | 115.6680 | 0.0132 | 0.0035 |
| 2024_09_20 22:00 | 3241382 | 2 | 19.1582 | 14.4776 | -115.9364 | 5.1132 | 115.3139 | 0.0117 | 0.0139 |
| 2024_09_20 22:00 | 3245779 | 3 | 15.0877 | 17.1543 | -117.2344 | 16.5527 | 145.5183 | 0.0095 | 0.0131 |
| 2024_09_20 22:00 | 3262111 | 4 | 15.2626 | 7.6205 | -117.2343 | 18.6283 | 197.0156 | 0.0142 | 0.0189 |
| 2024_09_20 22:00 | 3225528 | 5 | 16.8804 | 10.1776 | -115.2340 | 6.1383 | 94.7558 | 0.0174 | 0.0083 |
| 2024_09_20 22:00 | 3235415 | 6 | 18.3060 | 14.3225 | -117.3929 | 15.6424 | 148.5271 | 0.0185 | 0.0049 |
| 2024_09_20 22:00 | 3252042 | 7 | 10.0894 | 14.9026 | -114.5445 | 4.1080 | 55.4181 | 0.0085 | 0.0079 |
| 2024_09_20 22:00 | 3263236 | 8 | 6.5955 | 5.6205 | -114.4085 | 3.9012 | 26.7780 | 0.0037 | 0.0035 |
| 2024_09_20 22:00 | 3243527 | 9 | 13.0533 | 14.9579 | -116.9304 | 4.3385 | 42.8065 | 0.0014 | 0.0193 |
| 2024_09_20 22:00 | 3279863 | 10 | 16.2049 | 13.8647 | -117.9475 | 4.8497 | 42.2546 | 0.0078 | 0.0020 |
| 2024_09_20 22:00 | 3263150 | 11 | 8.3919 | 18.8143 | -114.7900 | 3.2752 | 34.5187 | 0.0055 | 0.0090 |
| 2024_09_20 22:00 | 3254440 | 12 | 14.6588 | 14.2833 | -114.3657 | 3.6795 | 33.5470 | 0.0176 | 0.0027 |
| 2024_09_20 22:00 | 3251412 | 13 | 6.5237 | 10.0511 | -117.6625 | 4.1914 | 48.4508 | 0.0162 | 0.0044 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414201_58253DE6 | 504990 | 67 | -93.2 | 504990 | 189 | -92.1 | 504990 | 979 | -97.6 | 504990 | 514 |
| MR_1774414201_B7C9E414 | 504990 | 67 | -96.5 | 504990 | 189 | -90.1 | 504990 | 979 | -97.3 | 504990 | 514 |
| MR_1774414201_D4C7C888 | 504990 | 67 | -95.4 | 504990 | 189 | -91.0 | 504990 | 979 | -98.5 | 504990 | 514 |
| MR_1774414201_A85101D1 | 152650 | 805 | -92.8 | 152650 | 643 | -99.6 | 152650 | 715 | -101.4 | 152650 | 92 |
| MR_1774414201_782BDF0C | 504990 | 67 | -95.7 | 504990 | 189 | -91.9 | 504990 | 979 | -97.7 | 504990 | 514 |
| MR_1774414201_6CFDBC7B | 504990 | 67 | -94.7 | 504990 | 189 | -92.3 | 504990 | 979 | -99.5 | 504990 | 514 |
| MR_1774414201_288C5CDA | 504990 | 67 | -93.8 | 504990 | 189 | -91.6 | 504990 | 979 | -96.9 | 504990 | 514 |
| MR_1774414201_1667FA6F | 504990 | 67 | -94.4 | 504990 | 189 | -91.5 | 504990 | 979 | -100.8 | 504990 | 514 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 429: `162e9a74-99c...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `162e9a74-99c1-48bf-9a7f-ff461ae88dec` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[429] topology](images/test_0429.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3225791_2 by 4 degrees
- `C2`: Add neighbor relationship between 3238774_3 and 3275114_4
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3225791_2
- `C4`: Press down the tilt angle of 3225791_2 by 4 degrees
- `C5`: Check test server and transmission issues
- `C6`: Insufficient data; more data is needed for judgment.
- `C7`: Adjust the azimuth of 3275114_4 by 50 degrees
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3275114_4
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3225791_2
- `C10`: Press down the tilt angle  of 3275114_4 by 10 degrees
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3275114_4
- `C12`: Decrease A3 Offset threshold for 3225791_2
- `C13`: Increase A3 Offset threshold for 3225791_2
- `C14`: Add neighbor relationship between 3225791_2 and 3275114_4
- `C15`: Adjust the azimuth of 3225791_2 by 37 degrees
- `C16`: Decrease transmission power for 3225791_2
- `C17`: Increase transmission power for 3275114_4
- `C18`: Decrease A3 Offset threshold for 3275114_4
- `C19`: Increase A3 Offset threshold for 3275114_4
- `C20`: Increase transmission power for 3225791_2
- `C21`: Lift the tilt angle  of 3275114_4 by 10 degrees
- `C22`: Decrease transmission power for 3275114_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.307 | MS1 | 121.4656679596 | 31.1446309654 | 388 | 504990 | -90.69 | 12.90 | 406.16 | 0.08 | 2.93 | 1592 |
| 2024-09-20 22:21:32.956 | MS1 | 121.4656612319 | 31.1446360740 | 388 | 504990 | -89.23 | 12.79 | 572.71 | 0.15 | 2.87 | 1577 |
| 2024-09-20 22:21:33.168 | MS1 | 121.4656605486 | 31.1446289528 | 388 | 504990 | -89.68 | 17.35 | 497.34 | 0.16 | 2.43 | 1560 |
| 2024-09-20 22:21:34.397 | MS1 | 121.4656778443 | 31.1446211062 | 388 | 504990 | -91.23 | 12.47 | 75.24 | 0.04 | 2.41 | 1599 |
| 2024-09-20 22:21:35.902 | MS1 | 121.4656661260 | 31.1446339569 | 388 | 504990 | -87.75 | 16.16 | 59.26 | 0.18 | 2.95 | 1583 |
| 2024-09-20 22:21:36.876 | MS1 | 121.4656751082 | 31.1446313778 | 388 | 504990 | -85.58 | 13.77 | 95.42 | 0.16 | 2.42 | 1590 |
| 2024-09-20 22:21:37.290 | MS1 | 121.4656766486 | 31.1446194181 | 388 | 504990 | -93.04 | 11.31 | 86.30 | 0.10 | 2.16 | 1593 |
| 2024-09-20 22:21:38.906 | MS1 | 121.4656629700 | 31.1446362253 | 388 | 504990 | -90.76 | 10.10 | 75.49 | 0.05 | 2.29 | 1560 |
| 2024-09-20 22:21:39.306 | MS1 | 121.4656713434 | 31.1446198193 | 388 | 504990 | -92.59 | 7.11 | 79.24 | 0.10 | 2.28 | 1590 |
| 2024-09-20 22:21:40.265 | MS1 | 121.4656629944 | 31.1446349561 | 388 | 504990 | -90.46 | 11.14 | 444.51 | 0.12 | 2.48 | 1567 |
| 2024-09-20 22:21:41.693 | MS1 | 121.4656614773 | 31.1446367829 | 388 | 504990 | -92.83 | 9.72 | 496.37 | 0.12 | 2.00 | 1590 |
| 2024-09-20 22:21:42.524 | MS1 | 121.4656758337 | 31.1446270712 | 388 | 504990 | -92.73 | 8.59 | 573.55 | 0.01 | 2.63 | 1589 |

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
| 3213407 | 1 | 121.4704209517 | 31.1461271881 | 269 | 5 | 7 | 30.2 | TDD | 258 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3225791 | 2 | 121.4721304810 | 31.1553187443 | 244 | 3 | 12 | 15.7 | TDD | 388 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3238774 | 3 | 121.4692457866 | 31.1440147941 | 223 | 9 | 10 | 42.1 | TDD | 69 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3275114 | 4 | 121.4647617356 | 31.1476536839 | 278 | 10 | 4 | 40.8 | TDD | 693 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:31.590 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.606 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.718 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.718 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.393 | NREventA3 | measId:2;ServCellPCI:285;Se... |
| 2024-09-20 22:21:38.633 | NRHandoverAttempt | SourcePCI:285;SourceNR-ARFC... |
| 2024-09-20 22:21:38.673 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.684 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.799 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.799 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3213407 | 1 | 82.7935 | 86.9837 | -114.9062 | 19.7070 | 167.2840 | 0.0162 | 0.0148 |
| 2024_09_19 22:00 | 3225791 | 2 | 87.7571 | 92.0314 | -117.5428 | 17.1270 | 170.7228 | 0.0103 | 0.0041 |
| 2024_09_19 22:00 | 3238774 | 3 | 76.2440 | 82.0560 | -115.2856 | 8.8821 | 99.3183 | 0.0033 | 0.0139 |
| 2024_09_19 22:00 | 3275114 | 4 | 83.2330 | 78.7655 | -116.7786 | 5.7330 | 101.6035 | 0.0033 | 0.0061 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416590_F237A3AC | 504990 | 388 | -90.8 | 504990 | 693 | -93.3 | 504990 | 69 | -104.7 | 504990 | 258 |
| MR_1774416590_2B103E32 | 504990 | 388 | -90.9 | 504990 | 693 | -92.6 | 504990 | 69 | -104.3 | 504990 | 258 |
| MR_1774416590_0D3A96CA | 504990 | 388 | -90.3 | 504990 | 693 | -90.9 | 504990 | 69 | -103.6 | 504990 | 258 |
| MR_1774416590_6AF14DF0 | 504990 | 388 | -91.1 | 504990 | 693 | -91.2 | 504990 | 69 | -105.5 | 504990 | 258 |
| MR_1774416590_D3CD133A | 504990 | 388 | -93.0 | 504990 | 693 | -90.4 | 504990 | 69 | -104.9 | 504990 | 258 |

> *... 2개 열 생략 (전체 14열)*

---
