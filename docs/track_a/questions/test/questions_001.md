# Track A 문제 분석 — test[0]~test[9]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/test.json`
> 범위: test[0] ~ test[9] (10개)

## 목차

1. [문제 0: `80e3aa96-815...`](#0) — single-answer
2. [문제 1: `f55a819f-3fb...`](#1) — single-answer
3. [문제 2: `2cd1f674-a41...`](#2) — single-answer
4. [문제 3: `923c459f-2ea...`](#3) — single-answer
5. [문제 4: `2e83ae4f-dca...`](#4) — single-answer
6. [문제 5: `cb846c3c-890...`](#5) — single-answer
7. [문제 6: `a082017c-d1c...`](#6) — single-answer
8. [문제 7: `39ae0e0f-cac...`](#7) — single-answer
9. [문제 8: `75a17b6a-ce1...`](#8) — single-answer
10. [문제 9: `c4e11e51-c97...`](#9) — single-answer

---

### 문제 0: `80e3aa96-815...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `80e3aa96-815d-4683-980c-16db42eab0ef` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[0] topology](images/test_0000.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3236601_2 and 3278642_3
- `C2`: Adjust the azimuth of 3278642_3 by 21 degrees
- `C3`: Decrease transmission power for 3236601_2
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3236601_2
- `C5`: Add neighbor relationship between 3279219_1 and 3278642_3
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3278642_3
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3278642_3
- `C8`: Adjust the azimuth of 3236601_2 by 50 degrees
- `C9`: Check test server and transmission issues
- `C10`: Decrease A3 Offset threshold for 3236601_2
- `C11`: Lift the tilt angle of 3236601_2 by 6 degrees
- `C12`: Increase transmission power for 3236601_2
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3236601_2
- `C14`: Increase A3 Offset threshold for 3278642_3
- `C15`: Increase A3 Offset threshold for 3236601_2
- `C16`: Insufficient data; more data is needed for judgment.
- `C17`: Press down the tilt angle  of 3278642_3 by 4 degrees
- `C18`: Lift the tilt angle  of 3278642_3 by 4 degrees
- `C19`: Increase transmission power for 3278642_3
- `C20`: Press down the tilt angle of 3236601_2 by 6 degrees
- `C21`: Decrease A3 Offset threshold for 3278642_3
- `C22`: Decrease transmission power for 3278642_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.395 | MS1 | 121.4656634389 | 31.1446290291 | 468 | 504990 | -77.35 | 17.25 | 389.76 | 0.08 | 2.05 | 1590 |
| 2024-09-20 22:21:32.356 | MS1 | 121.4656634008 | 31.1446365529 | 468 | 504990 | -77.33 | 12.22 | 330.71 | 0.10 | 2.79 | 1569 |
| 2024-09-20 22:21:33.248 | MS1 | 121.4656743291 | 31.1446377082 | 468 | 504990 | -76.76 | 14.31 | 514.31 | 0.05 | 2.09 | 1580 |
| 2024-09-20 22:21:34.838 | MS1 | 121.4656729024 | 31.1446280666 | 468 | 504990 | -91.57 | -3.85 | 33.16 | 0.18 | 1.23 | 1591 |
| 2024-09-20 22:21:35.925 | MS1 | 121.4656594716 | 31.1446229219 | 468 | 504990 | -94.27 | -3.89 | 73.45 | 0.07 | 1.11 | 1569 |
| 2024-09-20 22:21:36.765 | MS1 | 121.4656752586 | 31.1446258051 | 468 | 504990 | -85.68 | -3.75 | 29.24 | 0.18 | 1.09 | 1595 |
| 2024-09-20 22:21:37.275 | MS1 | 121.4656731532 | 31.1446233584 | 468 | 504990 | -86.25 | -1.57 | 37.97 | 0.05 | 1.12 | 1569 |
| 2024-09-20 22:21:38.503 | MS1 | 121.4656669871 | 31.1446353421 | 468 | 504990 | -84.48 | 17.52 | 517.28 | 0.04 | 1.35 | 1591 |
| 2024-09-20 22:21:39.814 | MS1 | 121.4656645775 | 31.1446361427 | 468 | 504990 | -75.21 | 15.92 | 393.00 | 0.17 | 1.33 | 1565 |
| 2024-09-20 22:21:40.201 | MS1 | 121.4656706239 | 31.1446367266 | 468 | 504990 | -80.06 | 16.17 | 522.29 | 0.08 | 2.13 | 1568 |
| 2024-09-20 22:21:41.904 | MS1 | 121.4656776894 | 31.1446215784 | 468 | 504990 | -83.95 | 13.72 | 470.37 | 0.13 | 2.60 | 1580 |
| 2024-09-20 22:21:42.353 | MS1 | 121.4656645278 | 31.1446304522 | 468 | 504990 | -81.77 | 13.75 | 409.71 | 0.15 | 2.56 | 1570 |

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
| 3236601 | 2 | 121.4709926020 | 31.1481572318 | 46 | 3 | 6 | 35.4 | TDD | 468 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3258117 | 4 | 121.4757901139 | 31.1461837028 | 290 | 12 | 9 | 49.3 | TDD | 638 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3278642 | 3 | 121.4644664799 | 31.1502698891 | 149 | 0 | 4 | 47.1 | TDD | 740 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3279219 | 1 | 121.4641482167 | 31.1545048116 | 98 | 1 | 3 | 16.0 | TDD | 426 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |

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
| 2024-09-20 22:21:31.328 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.353 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.458 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.458 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.164 | NREventA3 | measId:2;ServCellPCI:584;Se... |
| 2024-09-20 22:21:36.164 | NREventA3 | measId:2;ServCellPCI:584;Se... |
| 2024-09-20 22:21:37.164 | NREventA3 | measId:2;ServCellPCI:584;Se... |
| 2024-09-20 22:21:39.664 | NRRRCReestablishAttempt | PCI:584 |
| 2024-09-20 22:21:39.684 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.697 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:39.847 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.847 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3279219 | 1 | 19.2020 | 12.1167 | -117.5624 | 11.7839 | 124.1307 | 0.0119 | 0.0086 |
| 2024_09_20 22:00 | 3236601 | 2 | 17.0985 | 19.0797 | -116.1980 | 5.5245 | 189.0382 | 0.0079 | 0.1434 |
| 2024_09_20 22:00 | 3278642 | 3 | 19.3209 | 7.4854 | -117.8944 | 11.4814 | 164.7681 | 0.0173 | 0.0170 |
| 2024_09_20 22:00 | 3258117 | 4 | 8.7002 | 12.4941 | -115.6871 | 18.0351 | 163.8400 | 0.0132 | 0.0010 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416234_B4BAA8E1 | 504990 | 740 | -86.3 | 504990 | 468 | -90.2 | 504990 | 426 | -88.4 | 504990 | 638 |
| MR_1774416234_75EE042A | 504990 | 740 | -87.0 | 504990 | 468 | -90.9 | 504990 | 426 | -88.2 | 504990 | 638 |
| MR_1774416234_7BE6372D | 504990 | 468 | -92.0 | 504990 | 740 | -88.1 | 504990 | 426 | -89.1 | 504990 | 638 |
| MR_1774416234_8F51A01F | 504990 | 468 | -91.3 | 504990 | 740 | -87.1 | 504990 | 426 | -89.4 | 504990 | 638 |
| MR_1774416234_DCC0CCA4 | 504990 | 740 | -84.9 | 504990 | 468 | -93.1 | 504990 | 426 | -86.7 | 504990 | 638 |
| MR_1774416234_59AD0CF7 | 504990 | 468 | -90.0 | 504990 | 740 | -85.5 | 504990 | 426 | -86.6 | 504990 | 638 |
| MR_1774416234_763D9890 | 504990 | 740 | -88.6 | 504990 | 468 | -89.9 | 504990 | 426 | -89.7 | 504990 | 638 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1: `f55a819f-3fb...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `f55a819f-3fb9-4c8f-8859-a5b1649ff2d5` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[1] topology](images/test_0001.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3226176_1 by 37 degrees
- `C2`: Decrease A3 Offset threshold for 3210924_3
- `C3`: Decrease transmission power for 3226176_1
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3226176_1
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3210924_3
- `C6`: Check test server and transmission issues
- `C7`: Press down the tilt angle of 3226176_1 by 4 degrees
- `C8`: Increase transmission power for 3226176_1
- `C9`: Lift the tilt angle of 3226176_1 by 4 degrees
- `C10`: Lift the tilt angle  of 3210924_3 by 4 degrees
- `C11`: Insufficient data; more data is needed for judgment.
- `C12`: Increase A3 Offset threshold for 3210924_3
- `C13`: Press down the tilt angle  of 3210924_3 by 4 degrees
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3226176_1
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3210924_3
- `C16`: Increase A3 Offset threshold for 3226176_1
- `C17`: Increase transmission power for 3210924_3
- `C18`: Decrease transmission power for 3210924_3
- `C19`: Add neighbor relationship between 3226176_1 and 3210924_3
- `C20`: Adjust the azimuth of 3210924_3 by 23 degrees
- `C21`: Add neighbor relationship between 3246453_12 and 3210924_3
- `C22`: Decrease A3 Offset threshold for 3226176_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.367 | MS1 | 121.4656647375 | 31.1446328259 | 584 | 504990 | -93.49 | 13.48 | 355.55 | 0.09 | 2.31 | 1585 |
| 2024-09-20 22:21:32.238 | MS1 | 121.4656593652 | 31.1446269174 | 60 | 504990 | -93.59 | 10.61 | 565.36 | 0.07 | 2.51 | 1570 |
| 2024-09-20 22:21:33.598 | MS1 | 121.4656716403 | 31.1446306573 | 477 | 504990 | -94.29 | 12.65 | 310.19 | 0.14 | 2.70 | 1576 |
| 2024-09-20 22:21:34.787 | MS1 | 121.4656719393 | 31.1446259252 | 57 | 152650 | -93.61 | 2.56 | 79.36 | 0.05 | 1.83 | 934 |
| 2024-09-20 22:21:35.945 | MS1 | 121.4656617775 | 31.1446369976 | 589 | 152650 | -93.89 | 6.09 | 61.35 | 0.08 | 1.99 | 975 |
| 2024-09-20 22:21:36.934 | MS1 | 121.4656591455 | 31.1446296461 | 187 | 152650 | -89.58 | 2.47 | 60.32 | 0.01 | 1.98 | 904 |
| 2024-09-20 22:21:37.865 | MS1 | 121.4656624578 | 31.1446208273 | 172 | 152650 | -89.72 | 7.24 | 67.41 | 0.15 | 1.88 | 979 |
| 2024-09-20 22:21:38.563 | MS1 | 121.4656766416 | 31.1446204099 | 57 | 152650 | -91.07 | 3.65 | 72.15 | 0.20 | 1.50 | 994 |
| 2024-09-20 22:21:39.660 | MS1 | 121.4656621814 | 31.1446313564 | 589 | 152650 | -90.44 | 7.03 | 41.70 | 0.17 | 1.70 | 984 |
| 2024-09-20 22:21:40.539 | MS1 | 121.4656611872 | 31.1446216118 | 187 | 152650 | -87.81 | 2.29 | 52.50 | 0.20 | 2.99 | 1590 |
| 2024-09-20 22:21:41.494 | MS1 | 121.4656740608 | 31.1446227404 | 172 | 152650 | -89.73 | 4.01 | 53.61 | 0.19 | 2.35 | 1585 |
| 2024-09-20 22:21:42.161 | MS1 | 121.4656679305 | 31.1446196117 | 57 | 152650 | -95.59 | 6.34 | 73.53 | 0.02 | 2.52 | 1574 |

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
| 3210924 | 3 | 121.4705408862 | 31.1487386550 | 248 | 2 | 6 | 24.3 | TDD | 248 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3217667 | 5 | 121.4645817024 | 31.1520940560 | 191 | 6 | 2 | 10.0 | TDD | 477 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3226176 | 1 | 121.4689930479 | 31.1508337860 | 168 | 2 | 0 | 22.1 | TDD | 584 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3237522 | 13 | 121.4741494261 | 31.1502110965 | 228 | 11 | 8 | 12.4 | FDD | 889 | n1 | 152650 | 30M | 4T4R | 23 | 152650 |
| 3246453 | 12 | 121.4693246268 | 31.1494420627 | 32 | 5 | 8 | 26.7 | FDD | 187 | n1 | 152650 | 30M | 4T4R | 21 | 152650 |
| 3255575 | 2 | 121.4726543286 | 31.1537451231 | 315 | 7 | 6 | 29.2 | TDD | 15 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3257779 | 7 | 121.4737201497 | 31.1534482280 | 105 | 12 | 4 | 2.8 | FDD | 672 | n1 | 152650 | 30M | 4T4R | 28 | 152650 |
| 3258169 | 9 | 121.4671901540 | 31.1537655368 | 156 | 5 | 7 | 6.6 | FDD | 589 | n1 | 152650 | 30M | 4T4R | 28 | 152650 |
| 3259727 | 4 | 121.4655854438 | 31.1500441892 | 178 | 9 | 1 | 25.4 | TDD | 60 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3267722 | 8 | 121.4664727696 | 31.1451861612 | 55 | 0 | 7 | 22.5 | FDD | 172 | n1 | 152650 | 30M | 4T4R | 30 | 152650 |
| 3272766 | 11 | 121.4729294259 | 31.1479044088 | 239 | 2 | 1 | 19.6 | FDD | 57 | n1 | 152650 | 30M | 4T4R | 17 | 152650 |
| 3273575 | 6 | 121.4740234095 | 31.1453085125 | 171 | 6 | 6 | 10.0 | TDD | 30 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3276824 | 10 | 121.4715456391 | 31.1515528859 | 7 | 14 | 7 | 20.3 | FDD | 505 | n1 | 152650 | 30M | 4T4R | 30 | 152650 |

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
| 2024-09-20 22:21:31.440 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.463 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.606 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.606 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.256 | NREventA2 | measId:1;ServCellPCI:298;Se... |
| 2024-09-20 22:21:35.381 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.675 | NREventA5 | measId:3;ServCellPCI:298;Se... |
| 2024-09-20 22:21:35.735 | NRHandoverAttempt | SourcePCI:298;SourceNR-ARFC... |
| 2024-09-20 22:21:35.767 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.778 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:35.890 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.890 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3226176 | 1 | 9.0537 | 11.4218 | -117.9958 | 16.1946 | 130.3581 | 0.0057 | 0.0130 |
| 2024_09_20 22:00 | 3255575 | 2 | 11.0455 | 12.6459 | -114.0459 | 6.0667 | 112.7880 | 0.0056 | 0.0135 |
| 2024_09_20 22:00 | 3210924 | 3 | 16.8993 | 8.4811 | -117.2260 | 10.9500 | 84.2205 | 0.0005 | 0.0102 |
| 2024_09_20 22:00 | 3259727 | 4 | 19.4459 | 18.7629 | -117.1800 | 8.9230 | 115.6259 | 0.0095 | 0.0092 |
| 2024_09_20 22:00 | 3217667 | 5 | 10.4331 | 17.6304 | -115.2003 | 7.1579 | 89.6680 | 0.0161 | 0.0006 |
| 2024_09_20 22:00 | 3273575 | 6 | 18.6823 | 13.7064 | -115.8047 | 14.2513 | 183.5424 | 0.0065 | 0.0157 |
| 2024_09_20 22:00 | 3257779 | 7 | 8.4377 | 8.2207 | -116.4207 | 3.7092 | 30.1301 | 0.0150 | 0.0139 |
| 2024_09_20 22:00 | 3267722 | 8 | 18.4162 | 11.0802 | -114.5938 | 4.9849 | 56.5323 | 0.0154 | 0.0057 |
| 2024_09_20 22:00 | 3258169 | 9 | 12.4375 | 5.2539 | -116.1597 | 3.8999 | 31.5830 | 0.0135 | 0.0175 |
| 2024_09_20 22:00 | 3276824 | 10 | 10.0016 | 19.8198 | -115.1539 | 4.5928 | 41.9783 | 0.0090 | 0.0032 |
| 2024_09_20 22:00 | 3272766 | 11 | 18.3121 | 6.2596 | -117.7957 | 3.4999 | 55.3346 | 0.0101 | 0.0099 |
| 2024_09_20 22:00 | 3246453 | 12 | 12.5919 | 8.3276 | -115.3445 | 3.5276 | 27.6033 | 0.0178 | 0.0089 |
| 2024_09_20 22:00 | 3237522 | 13 | 13.5117 | 13.0582 | -114.9485 | 3.6030 | 55.9180 | 0.0102 | 0.0196 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415014_3A0DBBCC | 152650 | 57 | -95.2 | 152650 | 672 | -98.7 | 152650 | 505 | -102.6 | 152650 | 889 |
| MR_1774415014_FDA78D60 | 504990 | 477 | -96.0 | 504990 | 248 | -89.8 | 504990 | 15 | -96.4 | 504990 | 30 |
| MR_1774415014_3F574B45 | 152650 | 57 | -95.5 | 152650 | 672 | -98.2 | 152650 | 505 | -100.6 | 152650 | 889 |
| MR_1774415014_448C2933 | 504990 | 477 | -95.0 | 504990 | 248 | -90.8 | 504990 | 15 | -96.4 | 504990 | 30 |
| MR_1774415014_3E5AC0F1 | 504990 | 477 | -95.3 | 504990 | 248 | -89.6 | 504990 | 15 | -98.2 | 504990 | 30 |
| MR_1774415014_12FCA13C | 152650 | 57 | -95.2 | 152650 | 672 | -99.5 | 152650 | 505 | -104.2 | 152650 | 889 |
| MR_1774415014_62B77F0C | 152650 | 57 | -93.1 | 152650 | 672 | -97.0 | 152650 | 505 | -102.5 | 152650 | 889 |
| MR_1774415014_030E163E | 504990 | 477 | -92.6 | 504990 | 248 | -91.3 | 504990 | 15 | -97.6 | 504990 | 30 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 2: `2cd1f674-a41...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `2cd1f674-a411-4860-82c6-a16ba624b172` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[2] topology](images/test_0002.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3223153_4 by 50 degrees
- `C2`: Press down the tilt angle of 3223153_4 by 10 degrees
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3223153_4
- `C4`: Increase transmission power for 3223153_4
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3225681_3
- `C6`: Increase A3 Offset threshold for 3223153_4
- `C7`: Check test server and transmission issues
- `C8`: Insufficient data; more data is needed for judgment.
- `C9`: Increase A3 Offset threshold for 3225681_3
- `C10`: Add neighbor relationship between 3223153_4 and 3225681_3
- `C11`: Decrease transmission power for 3225681_3
- `C12`: Increase transmission power for 3225681_3
- `C13`: Decrease A3 Offset threshold for 3225681_3
- `C14`: Add neighbor relationship between 3216357_1 and 3225681_3
- `C15`: Lift the tilt angle  of 3225681_3 by 8 degrees
- `C16`: Press down the tilt angle  of 3225681_3 by 8 degrees
- `C17`: Decrease transmission power for 3223153_4
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3225681_3
- `C19`: Lift the tilt angle of 3223153_4 by 10 degrees
- `C20`: Decrease A3 Offset threshold for 3223153_4
- `C21`: Adjust the azimuth of 3225681_3 by 50 degrees
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3223153_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.340 | MS1 | 121.4656705241 | 31.1446281603 | 389 | 504990 | -90.67 | 17.29 | 332.58 | 0.14 | 2.67 | 1584 |
| 2024-09-20 22:21:32.125 | MS1 | 121.4656752956 | 31.1446377479 | 389 | 504990 | -85.35 | 12.76 | 312.49 | 0.03 | 2.99 | 1578 |
| 2024-09-20 22:21:33.443 | MS1 | 121.4656744731 | 31.1446337080 | 389 | 504990 | -91.47 | 12.55 | 442.32 | 0.16 | 2.48 | 1590 |
| 2024-09-20 22:21:34.325 | MS1 | 121.4656669920 | 31.1446183393 | 389 | 504990 | -85.86 | 14.07 | 95.03 | 0.13 | 2.81 | 1577 |
| 2024-09-20 22:21:35.804 | MS1 | 121.4656644204 | 31.1446319119 | 389 | 504990 | -91.92 | 17.03 | 78.87 | 0.12 | 2.88 | 1590 |
| 2024-09-20 22:21:36.372 | MS1 | 121.4656758530 | 31.1446230953 | 389 | 504990 | -89.95 | 15.55 | 56.74 | 0.03 | 2.23 | 1562 |
| 2024-09-20 22:21:37.584 | MS1 | 121.4656646965 | 31.1446291314 | 389 | 504990 | -91.49 | 8.18 | 52.94 | 0.03 | 2.15 | 1592 |
| 2024-09-20 22:21:38.837 | MS1 | 121.4656608124 | 31.1446330541 | 389 | 504990 | -89.04 | 9.12 | 54.46 | 0.13 | 2.26 | 1599 |
| 2024-09-20 22:21:39.121 | MS1 | 121.4656737471 | 31.1446326481 | 389 | 504990 | -90.74 | 8.78 | 57.05 | 0.12 | 2.29 | 1568 |
| 2024-09-20 22:21:40.166 | MS1 | 121.4656626562 | 31.1446289558 | 389 | 504990 | -90.84 | 9.56 | 466.21 | 0.18 | 2.79 | 1580 |
| 2024-09-20 22:21:41.112 | MS1 | 121.4656739271 | 31.1446221133 | 389 | 504990 | -91.85 | 8.66 | 554.60 | 0.06 | 2.63 | 1590 |
| 2024-09-20 22:21:42.966 | MS1 | 121.4656607583 | 31.1446285255 | 389 | 504990 | -90.91 | 8.18 | 483.31 | 0.17 | 2.11 | 1598 |

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
| 3216357 | 1 | 121.4668526613 | 31.1440215711 | 57 | 3 | 12 | 49.3 | TDD | 696 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3223153 | 4 | 121.4655592036 | 31.1503845990 | 6 | 11 | 4 | 45.1 | TDD | 389 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3225681 | 3 | 121.4687815052 | 31.1456804313 | 351 | 1 | 0 | 41.8 | TDD | 476 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3230923 | 2 | 121.4661567298 | 31.1456159126 | 143 | 1 | 4 | 39.1 | TDD | 273 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

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
| 2024-09-20 22:21:30.886 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.909 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.037 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.037 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.764 | NREventA3 | measId:2;ServCellPCI:718;Se... |
| 2024-09-20 22:21:38.004 | NRHandoverAttempt | SourcePCI:718;SourceNR-ARFC... |
| 2024-09-20 22:21:38.048 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.061 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.183 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.183 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3216357 | 1 | 94.0135 | 76.0138 | -114.1223 | 6.1987 | 162.4597 | 0.0133 | 0.0001 |
| 2024_09_19 22:00 | 3230923 | 2 | 90.5912 | 77.2581 | -116.7228 | 16.2028 | 96.6342 | 0.0045 | 0.0077 |
| 2024_09_19 22:00 | 3225681 | 3 | 76.1516 | 79.1293 | -115.2207 | 14.2870 | 188.5801 | 0.0068 | 0.0060 |
| 2024_09_19 22:00 | 3223153 | 4 | 93.6317 | 88.8262 | -116.3898 | 14.6928 | 129.2511 | 0.0082 | 0.0082 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416412_47845AF1 | 504990 | 389 | -85.3 | 504990 | 476 | -88.6 | 504990 | 696 | -93.4 | 504990 | 273 |
| MR_1774416412_2E3BDB7D | 504990 | 389 | -87.8 | 504990 | 476 | -90.7 | 504990 | 696 | -94.9 | 504990 | 273 |
| MR_1774416412_4E2255A0 | 504990 | 389 | -85.4 | 504990 | 476 | -89.6 | 504990 | 696 | -94.5 | 504990 | 273 |
| MR_1774416412_54B04568 | 504990 | 389 | -86.2 | 504990 | 476 | -90.0 | 504990 | 696 | -96.3 | 504990 | 273 |
| MR_1774416412_EAACD948 | 504990 | 389 | -84.6 | 504990 | 476 | -87.8 | 504990 | 696 | -95.5 | 504990 | 273 |
| MR_1774416412_6229D462 | 504990 | 389 | -87.1 | 504990 | 476 | -89.0 | 504990 | 696 | -95.9 | 504990 | 273 |
| MR_1774416412_FF54538A | 504990 | 389 | -84.8 | 504990 | 476 | -89.6 | 504990 | 696 | -95.2 | 504990 | 273 |
| MR_1774416412_5AE13EED | 504990 | 389 | -87.6 | 504990 | 476 | -90.5 | 504990 | 696 | -96.0 | 504990 | 273 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 3: `923c459f-2ea...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `923c459f-2ead-4c18-a204-751574ed6ae3` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[3] topology](images/test_0003.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3272734_2
- `C2`: Press down the tilt angle of 3272734_2 by 4 degrees
- `C3`: Insufficient data; more data is needed for judgment.
- `C4`: Decrease A3 Offset threshold for 3272734_2
- `C5`: Lift the tilt angle  of 3237388_1 by 4 degrees
- `C6`: Adjust the azimuth of 3237388_1 by 43 degrees
- `C7`: Press down the tilt angle  of 3237388_1 by 4 degrees
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3237388_1
- `C9`: Decrease A3 Offset threshold for 3237388_1
- `C10`: Decrease transmission power for 3237388_1
- `C11`: Increase transmission power for 3272734_2
- `C12`: Increase A3 Offset threshold for 3272734_2
- `C13`: Add neighbor relationship between 3272734_2 and 3237388_1
- `C14`: Add neighbor relationship between 3219191_12 and 3237388_1
- `C15`: Increase transmission power for 3237388_1
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3272734_2
- `C17`: Check test server and transmission issues
- `C18`: Increase A3 Offset threshold for 3237388_1
- `C19`: Adjust the azimuth of 3272734_2 by 45 degrees
- `C20`: Decrease transmission power for 3272734_2
- `C21`: Lift the tilt angle of 3272734_2 by 4 degrees
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3237388_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.685 | MS1 | 121.4656650252 | 31.1446327784 | 451 | 504990 | -95.04 | 9.43 | 427.31 | 0.04 | 2.20 | 1599 |
| 2024-09-20 22:21:32.807 | MS1 | 121.4656610117 | 31.1446214088 | 870 | 504990 | -95.83 | 12.24 | 535.50 | 0.02 | 2.36 | 1578 |
| 2024-09-20 22:21:33.282 | MS1 | 121.4656585091 | 31.1446308529 | 250 | 504990 | -94.83 | 12.63 | 540.08 | 0.16 | 2.91 | 1586 |
| 2024-09-20 22:21:34.638 | MS1 | 121.4656619443 | 31.1446328780 | 671 | 152650 | -92.92 | 5.26 | 98.18 | 0.01 | 1.70 | 956 |
| 2024-09-20 22:21:35.448 | MS1 | 121.4656675975 | 31.1446377961 | 560 | 152650 | -89.56 | 6.40 | 90.21 | 0.03 | 1.86 | 960 |
| 2024-09-20 22:21:36.811 | MS1 | 121.4656711332 | 31.1446348034 | 763 | 152650 | -94.00 | 3.51 | 54.23 | 0.20 | 1.81 | 926 |
| 2024-09-20 22:21:37.688 | MS1 | 121.4656588169 | 31.1446364876 | 137 | 152650 | -88.75 | 2.82 | 98.84 | 0.08 | 1.64 | 922 |
| 2024-09-20 22:21:38.201 | MS1 | 121.4656661998 | 31.1446264733 | 671 | 152650 | -87.63 | 2.29 | 69.48 | 0.10 | 1.65 | 915 |
| 2024-09-20 22:21:39.690 | MS1 | 121.4656702542 | 31.1446233547 | 560 | 152650 | -96.23 | 3.81 | 57.11 | 0.12 | 1.64 | 941 |
| 2024-09-20 22:21:40.125 | MS1 | 121.4656685827 | 31.1446338906 | 763 | 152650 | -95.29 | 2.26 | 66.83 | 0.04 | 2.00 | 1570 |
| 2024-09-20 22:21:41.117 | MS1 | 121.4656629830 | 31.1446318085 | 137 | 152650 | -88.59 | 4.76 | 62.93 | 0.09 | 2.38 | 1600 |
| 2024-09-20 22:21:42.396 | MS1 | 121.4656613003 | 31.1446311346 | 671 | 152650 | -88.42 | 2.62 | 65.23 | 0.04 | 2.31 | 1577 |

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
| 3211317 | 3 | 121.4677988406 | 31.1506445036 | 270 | 7 | 8 | 19.9 | TDD | 870 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3214704 | 7 | 121.4708007810 | 31.1455004269 | 253 | 15 | 11 | 20.9 | FDD | 795 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |
| 3217711 | 13 | 121.4741691287 | 31.1462408133 | 212 | 6 | 7 | 12.6 | FDD | 671 | n1 | 152650 | 30M | 4T4R | 12 | 152650 |
| 3219191 | 12 | 121.4676250807 | 31.1498740007 | 347 | 12 | 2 | 1.7 | FDD | 763 | n1 | 152650 | 30M | 4T4R | 14 | 152650 |
| 3226053 | 6 | 121.4648300487 | 31.1536695274 | 5 | 13 | 7 | 8.1 | TDD | 250 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3233136 | 8 | 121.4711661859 | 31.1489017660 | 243 | 0 | 12 | 28.3 | FDD | 776 | n1 | 152650 | 30M | 4T4R | 30 | 152650 |
| 3235453 | 11 | 121.4717231456 | 31.1516988759 | 304 | 9 | 11 | 15.7 | FDD | 951 | n1 | 152650 | 30M | 4T4R | 30 | 152650 |
| 3237388 | 1 | 121.4747901855 | 31.1495827153 | 281 | 3 | 3 | 12.4 | TDD | 866 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3243742 | 5 | 121.4657019905 | 31.1518204569 | 343 | 0 | 4 | 17.7 | TDD | 469 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3248934 | 9 | 121.4673993395 | 31.1497657127 | 113 | 0 | 10 | 22.3 | FDD | 137 | n1 | 152650 | 30M | 4T4R | 18 | 152650 |
| 3264802 | 4 | 121.4725126194 | 31.1450515347 | 270 | 10 | 7 | 26.8 | TDD | 779 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3272734 | 2 | 121.4652179786 | 31.1515996175 | 132 | 4 | 2 | 6.7 | TDD | 451 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3274261 | 10 | 121.4656666092 | 31.1460224223 | 216 | 7 | 0 | 0.9 | FDD | 560 | n1 | 152650 | 30M | 4T4R | 23 | 152650 |

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
| 2024-09-20 22:21:31.588 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.609 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.730 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.730 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.410 | NREventA2 | measId:1;ServCellPCI:896;Se... |
| 2024-09-20 22:21:35.559 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.762 | NREventA5 | measId:3;ServCellPCI:896;Se... |
| 2024-09-20 22:21:35.805 | NRHandoverAttempt | SourcePCI:896;SourceNR-ARFC... |
| 2024-09-20 22:21:35.855 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.869 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:35.982 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.982 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3237388 | 1 | 17.0211 | 13.3076 | -115.3809 | 14.9168 | 180.1411 | 0.0086 | 0.0129 |
| 2024_09_20 22:00 | 3272734 | 2 | 8.6016 | 9.0310 | -116.9751 | 6.7851 | 181.0770 | 0.0042 | 0.0044 |
| 2024_09_20 22:00 | 3211317 | 3 | 18.2618 | 6.0555 | -116.8183 | 13.5466 | 124.8545 | 0.0138 | 0.0091 |
| 2024_09_20 22:00 | 3264802 | 4 | 17.2880 | 14.0771 | -116.6730 | 5.0559 | 150.2240 | 0.0042 | 0.0111 |
| 2024_09_20 22:00 | 3243742 | 5 | 13.1240 | 9.6596 | -116.8014 | 12.1310 | 111.0624 | 0.0181 | 0.0144 |
| 2024_09_20 22:00 | 3226053 | 6 | 16.1884 | 12.5198 | -117.4809 | 5.2815 | 191.8206 | 0.0042 | 0.0005 |
| 2024_09_20 22:00 | 3214704 | 7 | 11.4589 | 14.0060 | -116.0595 | 4.2120 | 50.6088 | 0.0126 | 0.0007 |
| 2024_09_20 22:00 | 3233136 | 8 | 12.9418 | 17.1143 | -117.6490 | 4.0035 | 51.9410 | 0.0172 | 0.0129 |
| 2024_09_20 22:00 | 3248934 | 9 | 17.1070 | 5.5140 | -114.6189 | 4.7390 | 38.2703 | 0.0039 | 0.0069 |
| 2024_09_20 22:00 | 3274261 | 10 | 8.7112 | 6.8780 | -114.2271 | 3.1794 | 38.3501 | 0.0172 | 0.0077 |
| 2024_09_20 22:00 | 3235453 | 11 | 11.6614 | 7.4282 | -115.1791 | 3.4083 | 45.5475 | 0.0073 | 0.0139 |
| 2024_09_20 22:00 | 3219191 | 12 | 15.5234 | 5.0763 | -116.2937 | 4.1436 | 21.5336 | 0.0061 | 0.0169 |
| 2024_09_20 22:00 | 3217711 | 13 | 14.8443 | 8.9619 | -117.2554 | 3.0322 | 34.4200 | 0.0118 | 0.0040 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414033_D3E51E51 | 504990 | 250 | -95.1 | 504990 | 866 | -97.8 | 504990 | 469 | -101.8 | 504990 | 779 |
| MR_1774414033_7C104B87 | 152650 | 671 | -93.9 | 152650 | 951 | -95.3 | 152650 | 795 | -101.3 | 152650 | 776 |
| MR_1774414033_0716C5C5 | 504990 | 250 | -95.8 | 504990 | 866 | -98.1 | 504990 | 469 | -101.8 | 504990 | 779 |
| MR_1774414033_43EFF431 | 504990 | 250 | -93.5 | 504990 | 866 | -99.1 | 504990 | 469 | -102.5 | 504990 | 779 |
| MR_1774414033_6A007E5B | 504990 | 250 | -96.1 | 504990 | 866 | -98.1 | 504990 | 469 | -102.2 | 504990 | 779 |
| MR_1774414033_5A846A21 | 504990 | 250 | -96.7 | 504990 | 866 | -99.2 | 504990 | 469 | -101.5 | 504990 | 779 |
| MR_1774414033_71B0FAAB | 152650 | 671 | -91.9 | 152650 | 951 | -98.4 | 152650 | 795 | -101.7 | 152650 | 776 |
| MR_1774414033_D133C785 | 504990 | 250 | -96.4 | 504990 | 866 | -100.6 | 504990 | 469 | -102.3 | 504990 | 779 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 4: `2e83ae4f-dca...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `2e83ae4f-dca0-4931-bb13-d13d672e14e1` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[4] topology](images/test_0004.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3225778_2
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3225778_2
- `C3`: Check test server and transmission issues
- `C4`: Increase transmission power for 3263089_3
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3263089_3
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3263089_3
- `C7`: Lift the tilt angle  of 3263089_3 by 6 degrees
- `C8`: Decrease A3 Offset threshold for 3263089_3
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3225778_2
- `C10`: Increase transmission power for 3225778_2
- `C11`: Adjust the azimuth of 3263089_3 by 29 degrees
- `C12`: Adjust the azimuth of 3225778_2 by 50 degrees
- `C13`: Increase A3 Offset threshold for 3225778_2
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Decrease transmission power for 3225778_2
- `C16`: Press down the tilt angle  of 3263089_3 by 6 degrees
- `C17`: Increase A3 Offset threshold for 3263089_3
- `C18`: Lift the tilt angle of 3225778_2 by 10 degrees
- `C19`: Decrease transmission power for 3263089_3
- `C20`: Press down the tilt angle of 3225778_2 by 10 degrees
- `C21`: Add neighbor relationship between 3225778_2 and 3263089_3
- `C22`: Add neighbor relationship between 3227782_1 and 3263089_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.570 | MS1 | 121.4656663227 | 31.1446225186 | 522 | 504990 | -78.44 | 14.08 | 593.47 | 0.02 | 2.38 | 1580 |
| 2024-09-20 22:21:32.876 | MS1 | 121.4656593693 | 31.1446366425 | 522 | 504990 | -83.76 | 17.19 | 312.51 | 0.03 | 2.12 | 1596 |
| 2024-09-20 22:21:33.457 | MS1 | 121.4656703439 | 31.1446352643 | 522 | 504990 | -84.17 | 16.69 | 507.71 | 0.00 | 2.98 | 1592 |
| 2024-09-20 22:21:34.870 | MS1 | 121.4656760707 | 31.1446204879 | 522 | 504990 | -93.34 | -1.72 | 32.04 | 0.05 | 1.05 | 1577 |
| 2024-09-20 22:21:35.713 | MS1 | 121.4656710038 | 31.1446182826 | 522 | 504990 | -90.54 | -0.76 | 66.38 | 0.16 | 1.40 | 1564 |
| 2024-09-20 22:21:36.811 | MS1 | 121.4656633106 | 31.1446275184 | 522 | 504990 | -87.79 | -2.80 | 51.30 | 0.08 | 1.14 | 1591 |
| 2024-09-20 22:21:37.258 | MS1 | 121.4656656687 | 31.1446371468 | 522 | 504990 | -91.31 | -2.91 | 69.28 | 0.14 | 1.09 | 1573 |
| 2024-09-20 22:21:38.747 | MS1 | 121.4656765172 | 31.1446271640 | 522 | 504990 | -79.67 | 15.21 | 409.91 | 0.19 | 1.48 | 1560 |
| 2024-09-20 22:21:39.563 | MS1 | 121.4656759595 | 31.1446367910 | 522 | 504990 | -76.46 | 17.47 | 331.65 | 0.04 | 1.45 | 1562 |
| 2024-09-20 22:21:40.374 | MS1 | 121.4656703436 | 31.1446243115 | 522 | 504990 | -84.22 | 15.79 | 410.38 | 0.08 | 2.07 | 1585 |
| 2024-09-20 22:21:41.511 | MS1 | 121.4656654126 | 31.1446185181 | 522 | 504990 | -81.97 | 14.69 | 491.29 | 0.12 | 2.11 | 1595 |
| 2024-09-20 22:21:42.571 | MS1 | 121.4656729887 | 31.1446196344 | 522 | 504990 | -81.12 | 14.43 | 556.88 | 0.01 | 2.96 | 1593 |

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
| 3225778 | 2 | 121.4672219378 | 31.1542016380 | 12 | 9 | 10 | 15.5 | TDD | 522 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3227782 | 1 | 121.4744828347 | 31.1527198191 | 129 | 4 | 9 | 22.5 | TDD | 409 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3241636 | 4 | 121.4758616930 | 31.1469872485 | 348 | 9 | 8 | 35.1 | TDD | 474 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3263089 | 3 | 121.4750533257 | 31.1496370068 | 267 | 4 | 6 | 32.6 | TDD | 314 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |

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
| 2024-09-20 22:21:31.186 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.204 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.323 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.323 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.051 | NREventA3 | measId:2;ServCellPCI:97;Ser... |
| 2024-09-20 22:21:36.051 | NREventA3 | measId:2;ServCellPCI:97;Ser... |
| 2024-09-20 22:21:37.051 | NREventA3 | measId:2;ServCellPCI:97;Ser... |
| 2024-09-20 22:21:39.551 | NRRRCReestablishAttempt | PCI:97 |
| 2024-09-20 22:21:39.568 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.583 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:39.727 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.727 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3227782 | 1 | 10.7301 | 7.0549 | -114.9861 | 14.4879 | 163.8675 | 0.0179 | 0.0090 |
| 2024_09_20 22:00 | 3225778 | 2 | 9.9254 | 7.0896 | -116.8045 | 10.1601 | 159.6121 | 0.0080 | 0.1173 |
| 2024_09_20 22:00 | 3263089 | 3 | 11.5675 | 7.8323 | -115.7763 | 15.2305 | 88.0525 | 0.0061 | 0.0097 |
| 2024_09_20 22:00 | 3241636 | 4 | 11.8437 | 19.1889 | -114.3792 | 17.6058 | 139.3929 | 0.0043 | 0.0094 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415471_16203835 | 504990 | 522 | -93.1 | 504990 | 314 | -90.2 | 504990 | 409 | -88.9 | 504990 | 474 |
| MR_1774415471_FA4DDEBE | 504990 | 522 | -91.5 | 504990 | 314 | -89.8 | 504990 | 409 | -88.9 | 504990 | 474 |
| MR_1774415471_A4ACF4A8 | 504990 | 522 | -92.0 | 504990 | 314 | -89.7 | 504990 | 409 | -88.5 | 504990 | 474 |
| MR_1774415471_50183AC5 | 504990 | 314 | -89.3 | 504990 | 522 | -95.1 | 504990 | 409 | -90.6 | 504990 | 474 |
| MR_1774415471_A6AE6F70 | 504990 | 522 | -94.4 | 504990 | 314 | -86.6 | 504990 | 409 | -90.5 | 504990 | 474 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 5: `cb846c3c-890...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `cb846c3c-8900-4b40-917b-0bd848114d00` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[5] topology](images/test_0005.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3276433_4
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3218249_1
- `C3`: Decrease transmission power for 3218249_1
- `C4`: Add neighbor relationship between 3276433_4 and 3218249_1
- `C5`: Lift the tilt angle  of 3218249_1 by 10 degrees
- `C6`: Adjust the azimuth of 3218249_1 by 50 degrees
- `C7`: Increase transmission power for 3276433_4
- `C8`: Press down the tilt angle of 3276433_4 by 1 degrees
- `C9`: Increase A3 Offset threshold for 3276433_4
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3276433_4
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3276433_4
- `C12`: Lift the tilt angle of 3276433_4 by 1 degrees
- `C13`: Decrease A3 Offset threshold for 3218249_1
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3218249_1
- `C15`: Increase transmission power for 3218249_1
- `C16`: Check test server and transmission issues
- `C17`: Insufficient data; more data is needed for judgment.
- `C18`: Add neighbor relationship between 3215255_2 and 3218249_1
- `C19`: Press down the tilt angle  of 3218249_1 by 10 degrees
- `C20`: Decrease transmission power for 3276433_4
- `C21`: Increase A3 Offset threshold for 3218249_1
- `C22`: Adjust the azimuth of 3276433_4 by 20 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.968 | MS1 | 121.4656632984 | 31.1446352882 | 487 | 504990 | -91.21 | 16.86 | 577.64 | 0.05 | 2.01 | 1586 |
| 2024-09-20 22:21:32.410 | MS1 | 121.4656624750 | 31.1446308930 | 487 | 504990 | -85.29 | 17.45 | 593.89 | 0.09 | 2.41 | 1578 |
| 2024-09-20 22:21:33.260 | MS1 | 121.4656776907 | 31.1446274811 | 487 | 504990 | -89.53 | 12.62 | 447.60 | 0.11 | 2.63 | 1587 |
| 2024-09-20 22:21:34.223 | MS1 | 121.4656600638 | 31.1446294667 | 487 | 504990 | -88.02 | 14.16 | 76.53 | 0.55 | 2.05 | 691 |
| 2024-09-20 22:21:35.712 | MS1 | 121.4656726346 | 31.1446267941 | 487 | 504990 | -91.22 | 14.56 | 86.51 | 0.52 | 2.48 | 689 |
| 2024-09-20 22:21:36.134 | MS1 | 121.4656679333 | 31.1446313131 | 487 | 504990 | -90.05 | 13.30 | 77.44 | 0.65 | 2.10 | 627 |
| 2024-09-20 22:21:37.166 | MS1 | 121.4656604493 | 31.1446275575 | 487 | 504990 | -91.80 | 11.68 | 106.20 | 0.53 | 2.02 | 559 |
| 2024-09-20 22:21:38.333 | MS1 | 121.4656727261 | 31.1446273586 | 487 | 504990 | -92.62 | 10.35 | 67.80 | 0.69 | 2.29 | 691 |
| 2024-09-20 22:21:39.469 | MS1 | 121.4656702517 | 31.1446363094 | 487 | 504990 | -91.95 | 12.42 | 71.46 | 0.65 | 2.75 | 692 |
| 2024-09-20 22:21:40.396 | MS1 | 121.4656624687 | 31.1446358925 | 487 | 504990 | -91.64 | 10.86 | 437.29 | 0.10 | 2.99 | 1587 |
| 2024-09-20 22:21:41.199 | MS1 | 121.4656716739 | 31.1446218228 | 487 | 504990 | -91.54 | 11.36 | 469.37 | 0.10 | 3.00 | 1577 |
| 2024-09-20 22:21:42.859 | MS1 | 121.4656700676 | 31.1446335820 | 487 | 504990 | -89.68 | 9.92 | 369.67 | 0.01 | 2.96 | 1569 |

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
| 3215255 | 2 | 121.4691397961 | 31.1550500073 | 186 | 6 | 10 | 20.1 | TDD | 306 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3218249 | 1 | 121.4676483022 | 31.1443455111 | 87 | 13 | 11 | 27.8 | TDD | 8 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3262921 | 3 | 121.4663376285 | 31.1493782652 | 27 | 2 | 11 | 37.9 | TDD | 574 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3276433 | 4 | 121.4682972938 | 31.1542923952 | 173 | 0 | 1 | 16.0 | TDD | 487 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |

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
| 2024-09-20 22:21:31.476 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.494 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.641 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.641 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.312 | NREventA3 | measId:2;ServCellPCI:956;Se... |
| 2024-09-20 22:21:38.552 | NRHandoverAttempt | SourcePCI:956;SourceNR-ARFC... |
| 2024-09-20 22:21:38.587 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.600 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.706 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.706 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3218249 | 1 | 14.4059 | 13.4480 | -117.4658 | 13.0429 | 166.5952 | 0.0029 | 0.0113 |
| 2024_09_20 22:00 | 3215255 | 2 | 11.8512 | 14.2033 | -116.9153 | 17.9104 | 137.7188 | 0.0161 | 0.0055 |
| 2024_09_20 22:00 | 3262921 | 3 | 5.0823 | 10.3625 | -116.9220 | 10.7889 | 142.7180 | 0.0066 | 0.0144 |
| 2024_09_20 22:00 | 3276433 | 4 | 6.2615 | 11.3296 | -114.4956 | 13.9886 | 159.3745 | 0.0024 | 0.0100 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415714_3F8840E0 | 504990 | 487 | -88.4 | 504990 | 8 | -96.8 | 504990 | 306 | -96.1 | 504990 | 574 |
| MR_1774415714_90ACF5AB | 504990 | 487 | -86.8 | 504990 | 8 | -95.8 | 504990 | 306 | -97.0 | 504990 | 574 |
| MR_1774415714_4B172101 | 504990 | 487 | -86.9 | 504990 | 8 | -94.8 | 504990 | 306 | -96.3 | 504990 | 574 |
| MR_1774415714_5CEB7EF1 | 504990 | 487 | -90.0 | 504990 | 8 | -94.8 | 504990 | 306 | -96.3 | 504990 | 574 |
| MR_1774415714_C8B13EAA | 504990 | 487 | -87.7 | 504990 | 8 | -96.2 | 504990 | 306 | -95.5 | 504990 | 574 |
| MR_1774415714_392EFFA4 | 504990 | 487 | -86.3 | 504990 | 8 | -97.2 | 504990 | 306 | -95.3 | 504990 | 574 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 6: `a082017c-d1c...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `a082017c-d1cf-47c3-984b-48cd78048951` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[6] topology](images/test_0006.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3247967_5 by 6 degrees
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3247967_5
- `C3`: Decrease transmission power for 3263667_2
- `C4`: Lift the tilt angle  of 3247967_5 by 3 degrees
- `C5`: Press down the tilt angle  of 3247967_5 by 3 degrees
- `C6`: Add neighbor relationship between 3266686_7 and 3247967_5
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3263667_2
- `C8`: Press down the tilt angle of 3263667_2 by 3 degrees
- `C9`: Increase transmission power for 3247967_5
- `C10`: Decrease A3 Offset threshold for 3247967_5
- `C11`: Decrease A3 Offset threshold for 3263667_2
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3263667_2
- `C13`: Check test server and transmission issues
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3247967_5
- `C15`: Increase transmission power for 3263667_2
- `C16`: Adjust the azimuth of 3263667_2 by 18 degrees
- `C17`: Insufficient data; more data is needed for judgment.
- `C18`: Lift the tilt angle of 3263667_2 by 3 degrees
- `C19`: Decrease transmission power for 3247967_5
- `C20`: Increase A3 Offset threshold for 3263667_2
- `C21`: Add neighbor relationship between 3263667_2 and 3247967_5
- `C22`: Increase A3 Offset threshold for 3247967_5

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.347 | MS1 | 121.4656709279 | 31.1446366650 | 66 | 504990 | -93.66 | 12.67 | 325.79 | 0.12 | 2.46 | 1593 |
| 2024-09-20 22:21:32.579 | MS1 | 121.4656628324 | 31.1446268814 | 480 | 504990 | -93.05 | 11.60 | 489.11 | 0.13 | 2.39 | 1589 |
| 2024-09-20 22:21:33.648 | MS1 | 121.4656626600 | 31.1446267873 | 470 | 504990 | -94.40 | 9.86 | 356.70 | 0.15 | 2.37 | 1578 |
| 2024-09-20 22:21:34.962 | MS1 | 121.4656663869 | 31.1446310252 | 617 | 152650 | -94.84 | 2.18 | 96.66 | 0.15 | 1.62 | 993 |
| 2024-09-20 22:21:35.234 | MS1 | 121.4656607080 | 31.1446327177 | 30 | 152650 | -91.78 | 2.33 | 97.93 | 0.10 | 1.88 | 921 |
| 2024-09-20 22:21:36.245 | MS1 | 121.4656767064 | 31.1446186949 | 648 | 152650 | -92.24 | 3.75 | 62.62 | 0.18 | 1.77 | 983 |
| 2024-09-20 22:21:37.970 | MS1 | 121.4656637856 | 31.1446326937 | 175 | 152650 | -94.70 | 5.34 | 59.53 | 0.01 | 1.58 | 991 |
| 2024-09-20 22:21:38.329 | MS1 | 121.4656743421 | 31.1446259824 | 617 | 152650 | -96.37 | 5.97 | 88.31 | 0.03 | 1.54 | 924 |
| 2024-09-20 22:21:39.775 | MS1 | 121.4656732260 | 31.1446276561 | 30 | 152650 | -90.82 | 7.22 | 86.17 | 0.02 | 1.62 | 912 |
| 2024-09-20 22:21:40.580 | MS1 | 121.4656752738 | 31.1446202996 | 648 | 152650 | -90.56 | 6.10 | 68.09 | 0.19 | 2.84 | 1596 |
| 2024-09-20 22:21:41.529 | MS1 | 121.4656593176 | 31.1446299276 | 175 | 152650 | -94.21 | 4.81 | 49.96 | 0.19 | 2.93 | 1595 |
| 2024-09-20 22:21:42.148 | MS1 | 121.4656657300 | 31.1446192087 | 617 | 152650 | -94.55 | 2.40 | 81.23 | 0.06 | 2.49 | 1571 |

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
| 3216872 | 11 | 121.4727581085 | 31.1530943299 | 178 | 13 | 8 | 3.1 | FDD | 721 | n1 | 152650 | 30M | 4T4R | 30 | 152650 |
| 3220266 | 3 | 121.4755525840 | 31.1472082841 | 53 | 11 | 5 | 18.9 | TDD | 258 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3232611 | 8 | 121.4739474683 | 31.1515540602 | 38 | 0 | 0 | 1.0 | FDD | 617 | n1 | 152650 | 30M | 4T4R | 18 | 152650 |
| 3234956 | 6 | 121.4670831307 | 31.1530512952 | 85 | 5 | 1 | 15.6 | TDD | 470 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3239475 | 9 | 121.4743154188 | 31.1477611497 | 101 | 5 | 8 | 29.9 | FDD | 606 | n1 | 152650 | 30M | 4T4R | 23 | 152650 |
| 3243332 | 1 | 121.4657932278 | 31.1512566535 | 282 | 6 | 12 | 1.3 | TDD | 480 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3247046 | 13 | 121.4734129166 | 31.1512244894 | 73 | 9 | 3 | 19.8 | FDD | 30 | n1 | 152650 | 30M | 4T4R | 12 | 152650 |
| 3247967 | 5 | 121.4758946741 | 31.1500011997 | 232 | 2 | 4 | 25.3 | TDD | 882 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3260100 | 10 | 121.4710638590 | 31.1527139692 | 231 | 10 | 7 | 20.1 | FDD | 175 | n1 | 152650 | 30M | 4T4R | 20 | 152650 |
| 3263667 | 2 | 121.4748280070 | 31.1457699527 | 280 | 1 | 4 | 25.7 | TDD | 66 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3266686 | 7 | 121.4718519811 | 31.1479966031 | 84 | 12 | 9 | 12.7 | FDD | 648 | n1 | 152650 | 30M | 4T4R | 29 | 152650 |
| 3267708 | 12 | 121.4714334443 | 31.1554676649 | 173 | 3 | 3 | 25.3 | FDD | 54 | n1 | 152650 | 30M | 4T4R | 20 | 152650 |
| 3277529 | 4 | 121.4670531754 | 31.1514257528 | 85 | 3 | 3 | 29.6 | TDD | 556 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |

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
| 2024-09-20 22:21:31.483 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.503 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.606 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.606 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.301 | NREventA2 | measId:1;ServCellPCI:563;Se... |
| 2024-09-20 22:21:35.435 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.640 | NREventA5 | measId:3;ServCellPCI:563;Se... |
| 2024-09-20 22:21:35.696 | NRHandoverAttempt | SourcePCI:563;SourceNR-ARFC... |
| 2024-09-20 22:21:35.717 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.728 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:35.858 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.858 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3243332 | 1 | 5.2362 | 16.1087 | -117.8340 | 19.1761 | 173.3548 | 0.0062 | 0.0130 |
| 2024_09_20 22:00 | 3263667 | 2 | 18.5609 | 17.4565 | -114.5098 | 6.2726 | 191.9181 | 0.0093 | 0.0131 |
| 2024_09_20 22:00 | 3220266 | 3 | 6.5641 | 9.5584 | -117.9152 | 10.6834 | 129.1319 | 0.0070 | 0.0199 |
| 2024_09_20 22:00 | 3277529 | 4 | 7.5260 | 10.3231 | -114.5980 | 11.0089 | 92.0150 | 0.0064 | 0.0188 |
| 2024_09_20 22:00 | 3247967 | 5 | 5.0777 | 11.2056 | -114.2321 | 9.2904 | 153.5022 | 0.0171 | 0.0077 |
| 2024_09_20 22:00 | 3234956 | 6 | 15.9728 | 10.6207 | -117.8259 | 9.3743 | 172.9084 | 0.0141 | 0.0037 |
| 2024_09_20 22:00 | 3266686 | 7 | 12.0033 | 17.4799 | -117.9503 | 3.5161 | 49.6746 | 0.0116 | 0.0130 |
| 2024_09_20 22:00 | 3232611 | 8 | 17.1619 | 19.3763 | -114.1809 | 4.3477 | 39.1008 | 0.0116 | 0.0115 |
| 2024_09_20 22:00 | 3239475 | 9 | 12.1000 | 17.6206 | -115.8129 | 3.0154 | 26.5812 | 0.0177 | 0.0176 |
| 2024_09_20 22:00 | 3260100 | 10 | 9.5963 | 18.4770 | -116.5941 | 3.7209 | 35.1020 | 0.0069 | 0.0076 |
| 2024_09_20 22:00 | 3216872 | 11 | 11.8982 | 10.1892 | -114.7062 | 4.3319 | 36.4373 | 0.0157 | 0.0090 |
| 2024_09_20 22:00 | 3267708 | 12 | 5.8441 | 16.3615 | -117.9024 | 3.1493 | 56.0838 | 0.0180 | 0.0101 |
| 2024_09_20 22:00 | 3247046 | 13 | 15.3062 | 17.3935 | -117.5110 | 4.3979 | 59.4007 | 0.0158 | 0.0102 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413218_3A22BB5F | 152650 | 617 | -93.3 | 152650 | 54 | -97.6 | 152650 | 721 | -106.9 | 152650 | 606 |
| MR_1774413218_C2C5C72A | 152650 | 617 | -94.3 | 152650 | 54 | -98.8 | 152650 | 721 | -105.6 | 152650 | 606 |
| MR_1774413218_07B1AE40 | 504990 | 470 | -96.1 | 504990 | 882 | -96.1 | 504990 | 556 | -98.5 | 504990 | 258 |
| MR_1774413218_0BB41E39 | 152650 | 617 | -92.9 | 152650 | 54 | -96.2 | 152650 | 721 | -104.6 | 152650 | 606 |
| MR_1774413218_9B8B85E2 | 152650 | 617 | -96.0 | 152650 | 54 | -95.1 | 152650 | 721 | -105.3 | 152650 | 606 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 7: `39ae0e0f-cac...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `39ae0e0f-cac1-416b-ace8-b72ca6354807` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[7] topology](images/test_0007.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3277613_1
- `C2`: Adjust the azimuth of 3216597_4 by 47 degrees
- `C3`: Increase A3 Offset threshold for 3216597_4
- `C4`: Add neighbor relationship between 3277613_1 and 3216597_4
- `C5`: Increase transmission power for 3277613_1
- `C6`: Decrease A3 Offset threshold for 3216597_4
- `C7`: Lift the tilt angle of 3277613_1 by 10 degrees
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3277613_1
- `C9`: Increase A3 Offset threshold for 3277613_1
- `C10`: Decrease A3 Offset threshold for 3277613_1
- `C11`: Add neighbor relationship between 3278452_3 and 3216597_4
- `C12`: Adjust the azimuth of 3277613_1 by 11 degrees
- `C13`: Check test server and transmission issues
- `C14`: Decrease transmission power for 3277613_1
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3216597_4
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3216597_4
- `C17`: Increase transmission power for 3216597_4
- `C18`: Press down the tilt angle of 3277613_1 by 10 degrees
- `C19`: Decrease transmission power for 3216597_4
- `C20`: Press down the tilt angle  of 3216597_4 by 6 degrees
- `C21`: Lift the tilt angle  of 3216597_4 by 6 degrees
- `C22`: Insufficient data; more data is needed for judgment.

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.231 | MS1 | 121.4656650883 | 31.1446243820 | 642 | 504990 | -79.01 | 14.75 | 562.74 | 0.18 | 2.81 | 1591 |
| 2024-09-20 22:21:32.285 | MS1 | 121.4656667232 | 31.1446264149 | 642 | 504990 | -80.38 | 13.25 | 477.56 | 0.08 | 2.20 | 1583 |
| 2024-09-20 22:21:33.869 | MS1 | 121.4656661485 | 31.1446245808 | 642 | 504990 | -76.50 | 14.11 | 309.11 | 0.12 | 2.09 | 1562 |
| 2024-09-20 22:21:34.239 | MS1 | 121.4656748690 | 31.1446271629 | 642 | 504990 | -93.85 | -3.98 | 44.42 | 0.13 | 1.44 | 1569 |
| 2024-09-20 22:21:35.847 | MS1 | 121.4656698369 | 31.1446342444 | 642 | 504990 | -94.03 | -2.78 | 72.80 | 0.18 | 1.28 | 1599 |
| 2024-09-20 22:21:36.398 | MS1 | 121.4656731892 | 31.1446216855 | 642 | 504990 | -91.46 | -1.86 | 58.64 | 0.12 | 1.47 | 1561 |
| 2024-09-20 22:21:37.731 | MS1 | 121.4656678861 | 31.1446280202 | 642 | 504990 | -91.93 | -2.13 | 56.84 | 0.07 | 1.01 | 1574 |
| 2024-09-20 22:21:38.529 | MS1 | 121.4656769912 | 31.1446216346 | 642 | 504990 | -81.62 | 16.10 | 488.80 | 0.12 | 1.35 | 1581 |
| 2024-09-20 22:21:39.963 | MS1 | 121.4656651350 | 31.1446192256 | 642 | 504990 | -79.30 | 12.78 | 540.85 | 0.13 | 1.25 | 1574 |
| 2024-09-20 22:21:40.356 | MS1 | 121.4656611394 | 31.1446294720 | 642 | 504990 | -79.28 | 14.85 | 524.81 | 0.01 | 2.30 | 1581 |
| 2024-09-20 22:21:41.498 | MS1 | 121.4656661330 | 31.1446374073 | 642 | 504990 | -77.02 | 15.77 | 567.64 | 0.19 | 2.40 | 1573 |
| 2024-09-20 22:21:42.977 | MS1 | 121.4656664997 | 31.1446319221 | 642 | 504990 | -82.63 | 17.24 | 494.15 | 0.15 | 2.58 | 1564 |

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
| 3216597 | 4 | 121.4731959920 | 31.1552787133 | 164 | 4 | 12 | 44.7 | TDD | 98 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3258247 | 2 | 121.4732481541 | 31.1502532053 | 237 | 11 | 3 | 15.6 | TDD | 195 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3277613 | 1 | 121.4700006118 | 31.1490376394 | 209 | 10 | 1 | 20.6 | TDD | 642 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3278452 | 3 | 121.4709086432 | 31.1534122495 | 78 | 1 | 4 | 43.9 | TDD | 606 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |

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
| 2024-09-20 22:21:30.947 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.962 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.081 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.081 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.772 | NREventA3 | measId:2;ServCellPCI:216;Se... |
| 2024-09-20 22:21:35.772 | NREventA3 | measId:2;ServCellPCI:216;Se... |
| 2024-09-20 22:21:36.772 | NREventA3 | measId:2;ServCellPCI:216;Se... |
| 2024-09-20 22:21:39.272 | NRRRCReestablishAttempt | PCI:216 |
| 2024-09-20 22:21:39.282 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.297 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:39.418 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.418 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3277613 | 1 | 10.9281 | 10.6881 | -116.4450 | 14.3072 | 188.1596 | 0.0197 | 0.1438 |
| 2024_09_20 22:00 | 3258247 | 2 | 14.1112 | 16.2751 | -114.0018 | 9.3951 | 102.1149 | 0.0143 | 0.0005 |
| 2024_09_20 22:00 | 3278452 | 3 | 6.5501 | 19.7369 | -115.3332 | 8.0358 | 93.2300 | 0.0006 | 0.0161 |
| 2024_09_20 22:00 | 3216597 | 4 | 5.6393 | 12.4282 | -114.9975 | 16.8938 | 120.7865 | 0.0119 | 0.0133 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415375_333BDDE9 | 504990 | 642 | -93.8 | 504990 | 98 | -89.8 | 504990 | 606 | -90.2 | 504990 | 195 |
| MR_1774415375_EBA9EC7B | 504990 | 98 | -88.8 | 504990 | 642 | -95.7 | 504990 | 606 | -89.5 | 504990 | 195 |
| MR_1774415375_4DFCF7A9 | 504990 | 98 | -88.1 | 504990 | 642 | -92.2 | 504990 | 606 | -87.8 | 504990 | 195 |
| MR_1774415375_27DBDF74 | 504990 | 642 | -95.0 | 504990 | 98 | -90.7 | 504990 | 606 | -90.6 | 504990 | 195 |
| MR_1774415375_662087A3 | 504990 | 98 | -88.3 | 504990 | 642 | -93.5 | 504990 | 606 | -90.4 | 504990 | 195 |
| MR_1774415375_8D11E82D | 504990 | 642 | -93.3 | 504990 | 98 | -90.4 | 504990 | 606 | -89.0 | 504990 | 195 |
| MR_1774415375_CFCDB8FA | 504990 | 642 | -95.2 | 504990 | 98 | -90.6 | 504990 | 606 | -90.4 | 504990 | 195 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 8: `75a17b6a-ce1...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `75a17b6a-ce1b-4a5e-b843-bdd967e81580` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[8] topology](images/test_0008.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3272056_4
- `C2`: Insufficient data; more data is needed for judgment.
- `C3`: Add neighbor relationship between 3272056_4 and 3233502_2
- `C4`: Increase transmission power for 3272056_4
- `C5`: Decrease transmission power for 3233502_2
- `C6`: Check test server and transmission issues
- `C7`: Increase transmission power for 3233502_2
- `C8`: Adjust the azimuth of 3272056_4 by 9 degrees
- `C9`: Press down the tilt angle  of 3233502_2 by 1 degrees
- `C10`: Decrease A3 Offset threshold for 3272056_4
- `C11`: Add neighbor relationship between 3275270_1 and 3233502_2
- `C12`: Increase A3 Offset threshold for 3233502_2
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3272056_4
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3233502_2
- `C15`: Decrease A3 Offset threshold for 3233502_2
- `C16`: Press down the tilt angle of 3272056_4 by 10 degrees
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3233502_2
- `C18`: Decrease transmission power for 3272056_4
- `C19`: Lift the tilt angle  of 3233502_2 by 1 degrees
- `C20`: Lift the tilt angle of 3272056_4 by 10 degrees
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3272056_4
- `C22`: Adjust the azimuth of 3233502_2 by 25 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.679 | MS1 | 121.4656745323 | 31.1446287170 | 421 | 504990 | -80.78 | 12.32 | 474.31 | 0.07 | 2.29 | 1581 |
| 2024-09-20 22:21:32.229 | MS1 | 121.4656600702 | 31.1446326205 | 421 | 504990 | -75.20 | 12.96 | 549.07 | 0.03 | 2.03 | 1566 |
| 2024-09-20 22:21:33.526 | MS1 | 121.4656623155 | 31.1446337092 | 421 | 504990 | -82.23 | 16.38 | 499.65 | 0.03 | 2.71 | 1564 |
| 2024-09-20 22:21:34.158 | MS1 | 121.4656662080 | 31.1446282744 | 421 | 504990 | -88.65 | -1.49 | 59.62 | 0.07 | 1.19 | 1560 |
| 2024-09-20 22:21:35.498 | MS1 | 121.4656641112 | 31.1446197729 | 421 | 504990 | -86.22 | -2.94 | 34.97 | 0.04 | 1.13 | 1577 |
| 2024-09-20 22:21:36.711 | MS1 | 121.4656726685 | 31.1446239129 | 421 | 504990 | -86.02 | -3.84 | 27.74 | 0.02 | 1.12 | 1566 |
| 2024-09-20 22:21:37.150 | MS1 | 121.4656660549 | 31.1446239419 | 421 | 504990 | -91.33 | -1.19 | 56.18 | 0.09 | 1.38 | 1575 |
| 2024-09-20 22:21:38.163 | MS1 | 121.4656600165 | 31.1446206932 | 421 | 504990 | -84.36 | 13.64 | 376.30 | 0.08 | 1.13 | 1563 |
| 2024-09-20 22:21:39.793 | MS1 | 121.4656740196 | 31.1446187158 | 421 | 504990 | -81.01 | 13.01 | 530.96 | 0.02 | 1.03 | 1585 |
| 2024-09-20 22:21:40.747 | MS1 | 121.4656745302 | 31.1446345350 | 421 | 504990 | -77.44 | 13.03 | 500.25 | 0.02 | 2.73 | 1581 |
| 2024-09-20 22:21:41.985 | MS1 | 121.4656647162 | 31.1446335886 | 421 | 504990 | -81.84 | 15.72 | 435.00 | 0.09 | 2.61 | 1584 |
| 2024-09-20 22:21:42.219 | MS1 | 121.4656749635 | 31.1446354969 | 421 | 504990 | -81.85 | 17.26 | 552.41 | 0.19 | 2.85 | 1562 |

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
| 3211155 | 3 | 121.4723287425 | 31.1490316265 | 322 | 0 | 0 | 35.0 | TDD | 160 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3233502 | 2 | 121.4640857953 | 31.1546373387 | 197 | 0 | 12 | 26.5 | TDD | 637 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3272056 | 4 | 121.4662366537 | 31.1503217308 | 176 | 13 | 6 | 31.3 | TDD | 421 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3275270 | 1 | 121.4661270539 | 31.1479106638 | 10 | 0 | 9 | 28.1 | TDD | 88 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |

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
| 2024-09-20 22:21:31.382 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.397 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.530 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.530 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.218 | NREventA3 | measId:2;ServCellPCI:309;Se... |
| 2024-09-20 22:21:36.218 | NREventA3 | measId:2;ServCellPCI:309;Se... |
| 2024-09-20 22:21:37.218 | NREventA3 | measId:2;ServCellPCI:309;Se... |
| 2024-09-20 22:21:39.718 | NRRRCReestablishAttempt | PCI:309 |
| 2024-09-20 22:21:39.728 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.739 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:39.863 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.863 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3275270 | 1 | 6.9122 | 6.7260 | -114.7350 | 15.6417 | 156.1836 | 0.0097 | 0.0079 |
| 2024_09_20 22:00 | 3233502 | 2 | 5.7416 | 19.1039 | -114.2655 | 11.3066 | 85.1265 | 0.0164 | 0.0185 |
| 2024_09_20 22:00 | 3211155 | 3 | 5.6717 | 7.3232 | -116.5274 | 17.3777 | 174.0788 | 0.0051 | 0.0157 |
| 2024_09_20 22:00 | 3272056 | 4 | 15.5854 | 17.9514 | -114.1075 | 7.8027 | 103.9656 | 0.0137 | 0.1576 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414330_C4EA2F9C | 504990 | 421 | -90.4 | 504990 | 637 | -85.9 | 504990 | 88 | -91.4 | 504990 | 160 |
| MR_1774414330_65DB2E63 | 504990 | 421 | -87.1 | 504990 | 637 | -85.9 | 504990 | 88 | -94.0 | 504990 | 160 |
| MR_1774414330_97FDDC8D | 504990 | 637 | -83.2 | 504990 | 421 | -88.5 | 504990 | 88 | -92.1 | 504990 | 160 |
| MR_1774414330_F22E75AB | 504990 | 421 | -86.8 | 504990 | 637 | -85.6 | 504990 | 88 | -93.1 | 504990 | 160 |
| MR_1774414330_5E2207AD | 504990 | 637 | -83.6 | 504990 | 421 | -88.2 | 504990 | 88 | -93.9 | 504990 | 160 |
| MR_1774414330_02A178BF | 504990 | 637 | -84.6 | 504990 | 421 | -87.2 | 504990 | 88 | -94.3 | 504990 | 160 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 9: `c4e11e51-c97...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `c4e11e51-c978-4d39-bfc0-c298d2e7ac16` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[9] topology](images/test_0009.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3232723_1
- `C2`: Increase transmission power for 3228245_3
- `C3`: Decrease A3 Offset threshold for 3228245_3
- `C4`: Increase A3 Offset threshold for 3228245_3
- `C5`: Check test server and transmission issues
- `C6`: Increase transmission power for 3232723_1
- `C7`: Lift the tilt angle of 3232723_1 by 10 degrees
- `C8`: Adjust the azimuth of 3232723_1 by 50 degrees
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3228245_3
- `C10`: Decrease transmission power for 3232723_1
- `C11`: Add neighbor relationship between 3263580_4 and 3228245_3
- `C12`: Add neighbor relationship between 3232723_1 and 3228245_3
- `C13`: Press down the tilt angle of 3232723_1 by 10 degrees
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3228245_3
- `C15`: Press down the tilt angle  of 3228245_3 by 4 degrees
- `C16`: Adjust the azimuth of 3228245_3 by 50 degrees
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3232723_1
- `C18`: Decrease A3 Offset threshold for 3232723_1
- `C19`: Lift the tilt angle  of 3228245_3 by 4 degrees
- `C20`: Insufficient data; more data is needed for judgment.
- `C21`: Decrease transmission power for 3228245_3
- `C22`: Increase A3 Offset threshold for 3232723_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.344 | MS1 | 121.4656623147 | 31.1446288632 | 792 | 504990 | -77.92 | 17.41 | 481.14 | 0.10 | 2.64 | 1563 |
| 2024-09-20 22:21:32.346 | MS1 | 121.4656643510 | 31.1446293891 | 792 | 504990 | -84.88 | 17.04 | 523.14 | 0.06 | 2.19 | 1573 |
| 2024-09-20 22:21:33.559 | MS1 | 121.4656733996 | 31.1446362516 | 792 | 504990 | -78.27 | 12.16 | 550.18 | 0.14 | 2.82 | 1561 |
| 2024-09-20 22:21:34.252 | MS1 | 121.4656677609 | 31.1446213387 | 792 | 504990 | -84.89 | -3.39 | 53.64 | 0.11 | 1.43 | 1590 |
| 2024-09-20 22:21:35.732 | MS1 | 121.4656732665 | 31.1446230942 | 792 | 504990 | -84.31 | -3.76 | 28.46 | 0.11 | 1.41 | 1599 |
| 2024-09-20 22:21:36.332 | MS1 | 121.4656710204 | 31.1446201929 | 792 | 504990 | -86.50 | -2.62 | 60.66 | 0.18 | 1.29 | 1573 |
| 2024-09-20 22:21:37.571 | MS1 | 121.4656653878 | 31.1446364977 | 792 | 504990 | -91.59 | -0.70 | 30.19 | 0.06 | 1.22 | 1598 |
| 2024-09-20 22:21:38.221 | MS1 | 121.4656758685 | 31.1446314845 | 792 | 504990 | -83.00 | -2.68 | 58.94 | 0.14 | 1.08 | 1580 |
| 2024-09-20 22:21:39.131 | MS1 | 121.4656639259 | 31.1446313167 | 544 | 504990 | -82.18 | 17.16 | 193.44 | 0.01 | 1.28 | 1587 |
| 2024-09-20 22:21:40.822 | MS1 | 121.4656589684 | 31.1446270442 | 544 | 504990 | -76.31 | 12.58 | 382.33 | 0.19 | 2.27 | 1576 |
| 2024-09-20 22:21:41.821 | MS1 | 121.4656671676 | 31.1446329918 | 544 | 504990 | -81.55 | 15.86 | 456.28 | 0.16 | 2.60 | 1587 |
| 2024-09-20 22:21:42.354 | MS1 | 121.4656684339 | 31.1446277726 | 544 | 504990 | -84.81 | 12.70 | 384.23 | 0.11 | 2.94 | 1574 |

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
| 3228245 | 3 | 121.4692908896 | 31.1471924499 | 94 | 2 | 11 | 19.3 | TDD | 544 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3232723 | 1 | 121.4683701766 | 31.1460810982 | 53 | 5 | 3 | 24.1 | TDD | 792 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3239494 | 2 | 121.4656038341 | 31.1473004324 | 17 | 0 | 9 | 31.3 | TDD | 768 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3263580 | 4 | 121.4676484764 | 31.1554539048 | 141 | 2 | 3 | 19.7 | TDD | 975 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

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
| 2024-09-20 22:21:31.601 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.625 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.745 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.745 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.488 | NREventA3 | measId:2;ServCellPCI:696;Se... |
| 2024-09-20 22:21:38.728 | NRHandoverAttempt | SourcePCI:696;SourceNR-ARFC... |
| 2024-09-20 22:21:38.777 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.789 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.932 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.932 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3232723 | 1 | 19.7059 | 14.1815 | -117.2424 | 13.5639 | 125.3294 | 0.0122 | 0.1216 |
| 2024_09_20 22:00 | 3239494 | 2 | 6.0961 | 9.1503 | -115.1420 | 9.1457 | 142.8364 | 0.0051 | 0.0033 |
| 2024_09_20 22:00 | 3228245 | 3 | 19.3926 | 8.4764 | -116.8230 | 13.1960 | 166.3626 | 0.0182 | 0.0095 |
| 2024_09_20 22:00 | 3263580 | 4 | 19.7062 | 10.1443 | -117.4142 | 11.3770 | 156.0591 | 0.0046 | 0.0106 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414593_155B9007 | 504990 | 792 | -82.9 | 504990 | 544 | -80.7 | 504990 | 975 | -84.7 | 504990 | 768 |
| MR_1774414593_485B5EA2 | 504990 | 544 | -79.9 | 504990 | 792 | -85.6 | 504990 | 975 | -83.3 | 504990 | 768 |
| MR_1774414593_F7561F6F | 504990 | 792 | -83.2 | 504990 | 544 | -79.2 | 504990 | 975 | -82.6 | 504990 | 768 |
| MR_1774414593_61754E72 | 504990 | 792 | -83.0 | 504990 | 544 | -79.4 | 504990 | 975 | -83.6 | 504990 | 768 |
| MR_1774414593_E4E719D0 | 504990 | 544 | -81.0 | 504990 | 792 | -86.0 | 504990 | 975 | -85.4 | 504990 | 768 |
| MR_1774414593_B812FF2B | 504990 | 544 | -78.9 | 504990 | 792 | -85.3 | 504990 | 975 | -82.7 | 504990 | 768 |

> *... 2개 열 생략 (전체 14열)*

---
