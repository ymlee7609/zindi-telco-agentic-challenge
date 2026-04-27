# Track A 문제 분석 — test[110]~test[119]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/test.json`
> 범위: test[110] ~ test[119] (10개)

## 목차

1. [문제 110: `5e215d49-b42...`](#110) — single-answer
2. [문제 111: `2e81aa4e-959...`](#111) — single-answer
3. [문제 112: `93ec9988-f07...`](#112) — single-answer
4. [문제 113: `18446dfd-846...`](#113) — single-answer
5. [문제 114: `7aec481f-6b4...`](#114) — single-answer
6. [문제 115: `9551a39a-122...`](#115) — multiple-answer
7. [문제 116: `83fdbfdb-16e...`](#116) — single-answer
8. [문제 117: `27f00cc5-f01...`](#117) — multiple-answer
9. [문제 118: `2a890bdb-5c8...`](#118) — single-answer
10. [문제 119: `76c6d898-030...`](#119) — single-answer

---

### 문제 110: `5e215d49-b42...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `5e215d49-b429-4c62-a937-4f9322f1673d` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[110] topology](images/test_0110.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment.
- `C2`: Press down the tilt angle  of 3268304_1 by 2 degrees
- `C3`: Increase A3 Offset threshold for 3268304_1
- `C4`: Decrease transmission power for 3268304_1
- `C5`: Adjust the azimuth of 3268304_1 by 48 degrees
- `C6`: Decrease A3 Offset threshold for 3254259_6
- `C7`: Add neighbor relationship between 3254259_6 and 3268304_1
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3268304_1
- `C9`: Increase A3 Offset threshold for 3254259_6
- `C10`: Decrease A3 Offset threshold for 3268304_1
- `C11`: Lift the tilt angle  of 3268304_1 by 2 degrees
- `C12`: Adjust the azimuth of 3254259_6 by 3 degrees
- `C13`: Increase transmission power for 3254259_6
- `C14`: Decrease transmission power for 3254259_6
- `C15`: Press down the tilt angle of 3254259_6 by 0 degrees
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3254259_6
- `C17`: Add neighbor relationship between 3273916_7 and 3268304_1
- `C18`: Check test server and transmission issues
- `C19`: Lift the tilt angle of 3254259_6 by 0 degrees
- `C20`: Increase transmission power for 3268304_1
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3254259_6
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3268304_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.896 | MS1 | 121.4656670892 | 31.1446365112 | 985 | 504990 | -95.71 | 9.15 | 500.27 | 0.14 | 2.09 | 1577 |
| 2024-09-20 22:21:32.257 | MS1 | 121.4656747979 | 31.1446197812 | 745 | 504990 | -93.60 | 12.67 | 573.81 | 0.04 | 2.22 | 1580 |
| 2024-09-20 22:21:33.949 | MS1 | 121.4656766801 | 31.1446355821 | 168 | 504990 | -93.12 | 13.40 | 397.68 | 0.09 | 2.64 | 1562 |
| 2024-09-20 22:21:34.261 | MS1 | 121.4656699769 | 31.1446346171 | 565 | 152650 | -88.48 | 5.77 | 68.70 | 0.04 | 1.64 | 969 |
| 2024-09-20 22:21:35.784 | MS1 | 121.4656682628 | 31.1446223111 | 351 | 152650 | -87.32 | 4.86 | 67.05 | 0.08 | 1.92 | 916 |
| 2024-09-20 22:21:36.978 | MS1 | 121.4656691080 | 31.1446288533 | 32 | 152650 | -94.59 | 4.13 | 55.13 | 0.09 | 1.63 | 917 |
| 2024-09-20 22:21:37.534 | MS1 | 121.4656583519 | 31.1446211983 | 121 | 152650 | -90.53 | 3.35 | 64.88 | 0.11 | 1.95 | 905 |
| 2024-09-20 22:21:38.230 | MS1 | 121.4656602220 | 31.1446315991 | 565 | 152650 | -93.13 | 4.94 | 72.58 | 0.05 | 1.80 | 922 |
| 2024-09-20 22:21:39.585 | MS1 | 121.4656694387 | 31.1446251607 | 351 | 152650 | -90.29 | 5.73 | 97.95 | 0.05 | 1.58 | 917 |
| 2024-09-20 22:21:40.108 | MS1 | 121.4656648176 | 31.1446209577 | 32 | 152650 | -95.09 | 2.67 | 69.39 | 0.16 | 2.25 | 1594 |
| 2024-09-20 22:21:41.649 | MS1 | 121.4656743735 | 31.1446256292 | 121 | 152650 | -96.52 | 2.77 | 51.85 | 0.10 | 2.18 | 1568 |
| 2024-09-20 22:21:42.277 | MS1 | 121.4656627603 | 31.1446295703 | 565 | 152650 | -93.13 | 7.68 | 79.79 | 0.02 | 2.17 | 1571 |

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
| 3212858 | 11 | 121.4750270736 | 31.1477867621 | 171 | 15 | 4 | 3.1 | FDD | 823 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |
| 3227915 | 9 | 121.4719356471 | 31.1540956905 | 95 | 15 | 5 | 2.1 | FDD | 441 | n1 | 152650 | 30M | 4T4R | 15 | 152650 |
| 3228709 | 13 | 121.4741642906 | 31.1494854432 | 38 | 15 | 7 | 6.0 | FDD | 351 | n1 | 152650 | 30M | 4T4R | 27 | 152650 |
| 3231232 | 2 | 121.4662560297 | 31.1450396974 | 47 | 13 | 8 | 10.0 | TDD | 168 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3239200 | 4 | 121.4645295010 | 31.1444399752 | 284 | 10 | 6 | 10.9 | TDD | 10 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3242765 | 8 | 121.4716627707 | 31.1502515030 | 81 | 15 | 7 | 28.3 | FDD | 33 | n1 | 152650 | 30M | 4T4R | 15 | 152650 |
| 3254259 | 6 | 121.4686172967 | 31.1521777266 | 195 | 0 | 9 | 1.2 | TDD | 985 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3257451 | 5 | 121.4664394706 | 31.1491414719 | 5 | 15 | 1 | 15.8 | TDD | 825 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3265390 | 12 | 121.4673721671 | 31.1553211196 | 317 | 14 | 2 | 9.5 | FDD | 121 | n1 | 152650 | 30M | 4T4R | 19 | 152650 |
| 3268304 | 1 | 121.4734296859 | 31.1539089570 | 168 | 1 | 3 | 28.7 | TDD | 416 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3272613 | 3 | 121.4713195529 | 31.1559616840 | 286 | 12 | 10 | 13.6 | TDD | 745 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3272854 | 10 | 121.4656917804 | 31.1518237254 | 35 | 12 | 12 | 20.1 | FDD | 565 | n1 | 152650 | 30M | 4T4R | 23 | 152650 |
| 3273916 | 7 | 121.4685009248 | 31.1529963157 | 177 | 11 | 1 | 25.7 | FDD | 32 | n1 | 152650 | 30M | 4T4R | 20 | 152650 |

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
| 2024-09-20 22:21:31.475 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.499 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.603 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.603 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.277 | NREventA2 | measId:1;ServCellPCI:579;Se... |
| 2024-09-20 22:21:35.414 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.676 | NREventA5 | measId:3;ServCellPCI:579;Se... |
| 2024-09-20 22:21:35.709 | NRHandoverAttempt | SourcePCI:579;SourceNR-ARFC... |
| 2024-09-20 22:21:35.750 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.764 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:35.866 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.866 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3268304 | 1 | 7.8573 | 15.4183 | -115.5298 | 6.7631 | 145.7526 | 0.0049 | 0.0194 |
| 2024_09_20 22:00 | 3231232 | 2 | 13.1987 | 10.1296 | -114.6116 | 11.0737 | 169.4875 | 0.0188 | 0.0036 |
| 2024_09_20 22:00 | 3272613 | 3 | 13.6003 | 15.0213 | -116.5006 | 16.3007 | 145.1271 | 0.0083 | 0.0026 |
| 2024_09_20 22:00 | 3239200 | 4 | 19.5732 | 6.5981 | -114.7638 | 9.1781 | 171.6578 | 0.0002 | 0.0034 |
| 2024_09_20 22:00 | 3257451 | 5 | 12.7118 | 14.5826 | -115.7407 | 7.5994 | 97.7683 | 0.0082 | 0.0009 |
| 2024_09_20 22:00 | 3254259 | 6 | 19.4115 | 8.6084 | -114.5333 | 8.2613 | 141.4084 | 0.0042 | 0.0017 |
| 2024_09_20 22:00 | 3273916 | 7 | 12.6900 | 7.8646 | -115.9128 | 3.5969 | 31.8200 | 0.0060 | 0.0100 |
| 2024_09_20 22:00 | 3242765 | 8 | 11.8486 | 10.1769 | -114.6679 | 4.4378 | 35.3195 | 0.0021 | 0.0158 |
| 2024_09_20 22:00 | 3227915 | 9 | 15.2405 | 11.2815 | -115.9421 | 3.6974 | 46.6271 | 0.0188 | 0.0077 |
| 2024_09_20 22:00 | 3272854 | 10 | 16.2396 | 5.0549 | -115.9466 | 3.2157 | 56.7184 | 0.0021 | 0.0068 |
| 2024_09_20 22:00 | 3212858 | 11 | 18.7323 | 16.0722 | -117.9405 | 3.7911 | 57.2468 | 0.0021 | 0.0041 |
| 2024_09_20 22:00 | 3265390 | 12 | 10.3127 | 15.8083 | -117.7422 | 3.1752 | 38.1681 | 0.0082 | 0.0130 |
| 2024_09_20 22:00 | 3228709 | 13 | 15.6806 | 14.9863 | -115.0491 | 4.3960 | 49.5696 | 0.0087 | 0.0007 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414900_84C0C795 | 152650 | 565 | -88.2 | 152650 | 33 | -96.5 | 152650 | 441 | -99.1 | 152650 | 823 |
| MR_1774414900_61B683C0 | 152650 | 565 | -87.9 | 152650 | 33 | -94.7 | 152650 | 441 | -97.8 | 152650 | 823 |
| MR_1774414900_48220B05 | 152650 | 565 | -90.1 | 152650 | 33 | -94.3 | 152650 | 441 | -99.8 | 152650 | 823 |
| MR_1774414900_12BF631F | 152650 | 565 | -86.5 | 152650 | 33 | -93.2 | 152650 | 441 | -100.0 | 152650 | 823 |
| MR_1774414900_08C4C6B1 | 504990 | 168 | -92.0 | 504990 | 416 | -94.0 | 504990 | 825 | -96.0 | 504990 | 10 |
| MR_1774414900_35FBE28D | 504990 | 168 | -94.7 | 504990 | 416 | -92.7 | 504990 | 825 | -96.4 | 504990 | 10 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 111: `2e81aa4e-959...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `2e81aa4e-959b-429e-8796-17898462900d` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[111] topology](images/test_0111.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3219818_1
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3219818_1
- `C3`: Decrease transmission power for 3260626_4
- `C4`: Adjust the azimuth of 3260626_4 by 47 degrees
- `C5`: Decrease A3 Offset threshold for 3219818_1
- `C6`: Decrease transmission power for 3219818_1
- `C7`: Lift the tilt angle  of 3260626_4 by 5 degrees
- `C8`: Press down the tilt angle  of 3260626_4 by 5 degrees
- `C9`: Add neighbor relationship between 3219818_1 and 3260626_4
- `C10`: Increase transmission power for 3260626_4
- `C11`: Increase A3 Offset threshold for 3219818_1
- `C12`: Lift the tilt angle of 3219818_1 by 10 degrees
- `C13`: Press down the tilt angle of 3219818_1 by 10 degrees
- `C14`: Check test server and transmission issues
- `C15`: Increase transmission power for 3219818_1
- `C16`: Add neighbor relationship between 3233226_3 and 3260626_4
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3260626_4
- `C18`: Increase A3 Offset threshold for 3260626_4
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3260626_4
- `C20`: Adjust the azimuth of 3219818_1 by 50 degrees
- `C21`: Decrease A3 Offset threshold for 3260626_4
- `C22`: Insufficient data; more data is needed for judgment.

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.880 | MS1 | 121.4656683873 | 31.1446268576 | 954 | 504990 | -82.54 | 12.25 | 420.74 | 0.14 | 2.82 | 1584 |
| 2024-09-20 22:21:32.470 | MS1 | 121.4656607431 | 31.1446261236 | 954 | 504990 | -83.03 | 15.29 | 553.47 | 0.13 | 2.69 | 1593 |
| 2024-09-20 22:21:33.825 | MS1 | 121.4656593197 | 31.1446318322 | 954 | 504990 | -79.11 | 14.22 | 347.92 | 0.02 | 2.64 | 1580 |
| 2024-09-20 22:21:34.845 | MS1 | 121.4656726450 | 31.1446235678 | 954 | 504990 | -88.78 | -2.78 | 21.34 | 0.06 | 1.20 | 1589 |
| 2024-09-20 22:21:35.457 | MS1 | 121.4656766375 | 31.1446328762 | 954 | 504990 | -91.98 | -0.21 | 53.54 | 0.16 | 1.38 | 1589 |
| 2024-09-20 22:21:36.393 | MS1 | 121.4656596334 | 31.1446306763 | 954 | 504990 | -94.87 | -2.38 | 40.48 | 0.06 | 1.04 | 1572 |
| 2024-09-20 22:21:37.833 | MS1 | 121.4656683068 | 31.1446339710 | 954 | 504990 | -91.48 | -1.65 | 52.99 | 0.18 | 1.22 | 1563 |
| 2024-09-20 22:21:38.663 | MS1 | 121.4656595965 | 31.1446256637 | 954 | 504990 | -80.15 | 12.75 | 458.85 | 0.16 | 1.46 | 1576 |
| 2024-09-20 22:21:39.957 | MS1 | 121.4656767696 | 31.1446378369 | 954 | 504990 | -78.11 | 17.74 | 423.98 | 0.12 | 1.24 | 1591 |
| 2024-09-20 22:21:40.372 | MS1 | 121.4656654578 | 31.1446305307 | 954 | 504990 | -78.51 | 12.27 | 458.50 | 0.18 | 2.56 | 1583 |
| 2024-09-20 22:21:41.193 | MS1 | 121.4656748468 | 31.1446188832 | 954 | 504990 | -76.80 | 17.18 | 499.81 | 0.01 | 2.84 | 1572 |
| 2024-09-20 22:21:42.481 | MS1 | 121.4656766585 | 31.1446342467 | 954 | 504990 | -84.04 | 13.94 | 511.07 | 0.17 | 2.99 | 1561 |

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
| 3219818 | 1 | 121.4702642611 | 31.1471724928 | 159 | 12 | 4 | 25.0 | TDD | 954 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3233226 | 3 | 121.4657698067 | 31.1513357064 | 73 | 1 | 6 | 31.8 | TDD | 414 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3250686 | 2 | 121.4702917391 | 31.1516178530 | 67 | 2 | 9 | 39.1 | TDD | 851 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3260626 | 4 | 121.4657995451 | 31.1537494158 | 134 | 4 | 12 | 15.6 | TDD | 254 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:31.081 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.101 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.229 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.229 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.899 | NREventA3 | measId:2;ServCellPCI:57;Ser... |
| 2024-09-20 22:21:35.899 | NREventA3 | measId:2;ServCellPCI:57;Ser... |
| 2024-09-20 22:21:36.899 | NREventA3 | measId:2;ServCellPCI:57;Ser... |
| 2024-09-20 22:21:39.399 | NRRRCReestablishAttempt | PCI:57 |
| 2024-09-20 22:21:39.411 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.422 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:39.557 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.557 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3219818 | 1 | 12.2269 | 16.2481 | -114.0474 | 8.2667 | 129.1236 | 0.0137 | 0.1804 |
| 2024_09_20 22:00 | 3250686 | 2 | 8.9519 | 11.7323 | -115.2300 | 12.9845 | 167.8722 | 0.0044 | 0.0013 |
| 2024_09_20 22:00 | 3233226 | 3 | 10.5951 | 5.0756 | -116.7481 | 7.9827 | 193.8755 | 0.0124 | 0.0183 |
| 2024_09_20 22:00 | 3260626 | 4 | 5.0082 | 14.9913 | -114.8443 | 14.2157 | 192.9674 | 0.0054 | 0.0200 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413036_F45A63BB | 504990 | 954 | -87.6 | 504990 | 254 | -82.9 | 504990 | 414 | -88.3 | 504990 | 851 |
| MR_1774413036_A6AC2B95 | 504990 | 254 | -84.7 | 504990 | 954 | -90.6 | 504990 | 414 | -88.9 | 504990 | 851 |
| MR_1774413036_E91881A9 | 504990 | 254 | -82.9 | 504990 | 954 | -87.8 | 504990 | 414 | -88.0 | 504990 | 851 |
| MR_1774413036_EE7B68FB | 504990 | 954 | -89.5 | 504990 | 254 | -83.5 | 504990 | 414 | -87.4 | 504990 | 851 |
| MR_1774413036_BD21FA62 | 504990 | 954 | -89.9 | 504990 | 254 | -84.5 | 504990 | 414 | -86.0 | 504990 | 851 |
| MR_1774413036_ED741812 | 504990 | 254 | -84.4 | 504990 | 954 | -87.0 | 504990 | 414 | -86.9 | 504990 | 851 |
| MR_1774413036_6CD1D123 | 504990 | 954 | -90.6 | 504990 | 254 | -83.0 | 504990 | 414 | -87.2 | 504990 | 851 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 112: `93ec9988-f07...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `93ec9988-f07a-4b8e-9a8d-3723ac0f840a` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[112] topology](images/test_0112.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3245027_3
- `C2`: Decrease transmission power for 3245027_3
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3245027_3
- `C4`: Decrease transmission power for 3248694_1
- `C5`: Increase transmission power for 3245027_3
- `C6`: Increase transmission power for 3248694_1
- `C7`: Adjust the azimuth of 3245027_3 by 50 degrees
- `C8`: Check test server and transmission issues
- `C9`: Lift the tilt angle  of 3248694_1 by 6 degrees
- `C10`: Insufficient data; more data is needed for judgment.
- `C11`: Press down the tilt angle  of 3248694_1 by 6 degrees
- `C12`: Lift the tilt angle of 3245027_3 by 7 degrees
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3248694_1
- `C14`: Press down the tilt angle of 3245027_3 by 7 degrees
- `C15`: Decrease A3 Offset threshold for 3245027_3
- `C16`: Add neighbor relationship between 3245027_3 and 3248694_1
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3248694_1
- `C18`: Decrease A3 Offset threshold for 3248694_1
- `C19`: Increase A3 Offset threshold for 3245027_3
- `C20`: Adjust the azimuth of 3248694_1 by 46 degrees
- `C21`: Add neighbor relationship between 3249936_4 and 3248694_1
- `C22`: Increase A3 Offset threshold for 3248694_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.184 | MS1 | 121.4656652561 | 31.1446186074 | 971 | 504990 | -84.23 | 13.66 | 413.07 | 0.05 | 2.78 | 1595 |
| 2024-09-20 22:21:32.684 | MS1 | 121.4656614776 | 31.1446198197 | 971 | 504990 | -79.61 | 16.68 | 335.10 | 0.13 | 2.46 | 1576 |
| 2024-09-20 22:21:33.140 | MS1 | 121.4656758926 | 31.1446344591 | 971 | 504990 | -79.55 | 13.00 | 306.45 | 0.04 | 2.50 | 1592 |
| 2024-09-20 22:21:34.746 | MS1 | 121.4656655560 | 31.1446295489 | 971 | 504990 | -90.09 | -3.70 | 49.47 | 0.18 | 1.35 | 1581 |
| 2024-09-20 22:21:35.292 | MS1 | 121.4656656330 | 31.1446342679 | 971 | 504990 | -92.87 | -1.84 | 65.36 | 0.09 | 1.03 | 1596 |
| 2024-09-20 22:21:36.338 | MS1 | 121.4656654852 | 31.1446370569 | 971 | 504990 | -87.93 | -0.47 | 46.53 | 0.04 | 1.10 | 1593 |
| 2024-09-20 22:21:37.490 | MS1 | 121.4656658486 | 31.1446199852 | 971 | 504990 | -91.62 | -3.88 | 24.11 | 0.18 | 1.44 | 1580 |
| 2024-09-20 22:21:38.596 | MS1 | 121.4656670063 | 31.1446327218 | 971 | 504990 | -78.28 | 17.82 | 456.94 | 0.10 | 1.20 | 1595 |
| 2024-09-20 22:21:39.839 | MS1 | 121.4656706842 | 31.1446317064 | 971 | 504990 | -83.29 | 13.18 | 368.97 | 0.13 | 1.01 | 1592 |
| 2024-09-20 22:21:40.311 | MS1 | 121.4656651771 | 31.1446307654 | 971 | 504990 | -79.00 | 16.59 | 347.90 | 0.04 | 2.87 | 1591 |
| 2024-09-20 22:21:41.397 | MS1 | 121.4656695915 | 31.1446292141 | 971 | 504990 | -83.68 | 16.09 | 435.57 | 0.08 | 2.10 | 1587 |
| 2024-09-20 22:21:42.361 | MS1 | 121.4656776614 | 31.1446305794 | 971 | 504990 | -83.08 | 14.57 | 361.79 | 0.18 | 2.91 | 1562 |

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
| 3245027 | 3 | 121.4659549310 | 31.1544642152 | 9 | 5 | 10 | 36.9 | TDD | 971 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3248694 | 1 | 121.4650521389 | 31.1483291352 | 218 | 2 | 0 | 27.0 | TDD | 496 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3249936 | 4 | 121.4650547996 | 31.1499215958 | 166 | 0 | 5 | 19.5 | TDD | 712 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3265941 | 2 | 121.4750129859 | 31.1538252374 | 102 | 10 | 7 | 21.7 | TDD | 26 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:30.754 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.773 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:30.904 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.904 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.643 | NREventA3 | measId:2;ServCellPCI:566;Se... |
| 2024-09-20 22:21:35.643 | NREventA3 | measId:2;ServCellPCI:566;Se... |
| 2024-09-20 22:21:36.643 | NREventA3 | measId:2;ServCellPCI:566;Se... |
| 2024-09-20 22:21:39.143 | NRRRCReestablishAttempt | PCI:566 |
| 2024-09-20 22:21:39.155 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.166 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:39.312 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.312 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3248694 | 1 | 15.7407 | 16.8390 | -116.6152 | 9.2999 | 159.7434 | 0.0142 | 0.0020 |
| 2024_09_20 22:00 | 3265941 | 2 | 13.4393 | 6.0253 | -114.0693 | 10.9439 | 163.4789 | 0.0031 | 0.0003 |
| 2024_09_20 22:00 | 3245027 | 3 | 12.9156 | 6.6883 | -115.8189 | 10.5693 | 131.0888 | 0.0044 | 0.1109 |
| 2024_09_20 22:00 | 3249936 | 4 | 7.0182 | 5.3311 | -114.8665 | 18.5519 | 137.7950 | 0.0018 | 0.0173 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414309_EC1CBDCE | 504990 | 971 | -90.6 | 504990 | 496 | -83.5 | 504990 | 712 | -87.1 | 504990 | 26 |
| MR_1774414309_26AD6F54 | 504990 | 496 | -82.5 | 504990 | 971 | -90.1 | 504990 | 712 | -89.2 | 504990 | 26 |
| MR_1774414309_22F9A0FB | 504990 | 496 | -82.3 | 504990 | 971 | -88.7 | 504990 | 712 | -88.8 | 504990 | 26 |
| MR_1774414309_8C1225C6 | 504990 | 971 | -91.1 | 504990 | 496 | -83.9 | 504990 | 712 | -88.7 | 504990 | 26 |
| MR_1774414309_0D8C2463 | 504990 | 971 | -88.9 | 504990 | 496 | -82.5 | 504990 | 712 | -88.0 | 504990 | 26 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 113: `18446dfd-846...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `18446dfd-8464-4331-98b8-c91c8561db98` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[113] topology](images/test_0113.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3225516_4 by 10 degrees
- `C2`: Increase transmission power for 3216107_1
- `C3`: Add neighbor relationship between 3278746_2 and 3225516_4
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3225516_4
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3225516_4
- `C6`: Check test server and transmission issues
- `C7`: Increase A3 Offset threshold for 3225516_4
- `C8`: Decrease A3 Offset threshold for 3216107_1
- `C9`: Adjust the azimuth of 3225516_4 by 50 degrees
- `C10`: Decrease A3 Offset threshold for 3225516_4
- `C11`: Add neighbor relationship between 3216107_1 and 3225516_4
- `C12`: Adjust the azimuth of 3216107_1 by 42 degrees
- `C13`: Decrease transmission power for 3216107_1
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3216107_1
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3216107_1
- `C16`: Lift the tilt angle of 3216107_1 by 1 degrees
- `C17`: Lift the tilt angle  of 3225516_4 by 10 degrees
- `C18`: Insufficient data; more data is needed for judgment.
- `C19`: Increase transmission power for 3225516_4
- `C20`: Decrease transmission power for 3225516_4
- `C21`: Press down the tilt angle of 3216107_1 by 1 degrees
- `C22`: Increase A3 Offset threshold for 3216107_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.355 | MS1 | 121.4656603202 | 31.1446205493 | 473 | 504990 | -85.68 | 17.35 | 310.10 | 0.12 | 2.62 | 1599 |
| 2024-09-20 22:21:32.820 | MS1 | 121.4656751008 | 31.1446185516 | 473 | 504990 | -86.53 | 12.12 | 463.21 | 0.18 | 2.53 | 1571 |
| 2024-09-20 22:21:33.846 | MS1 | 121.4656699095 | 31.1446321622 | 473 | 504990 | -85.63 | 15.85 | 477.61 | 0.13 | 2.83 | 1579 |
| 2024-09-20 22:21:34.957 | MS1 | 121.4656775591 | 31.1446203950 | 473 | 504990 | -89.69 | 15.48 | 85.10 | 0.60 | 2.94 | 643 |
| 2024-09-20 22:21:35.868 | MS1 | 121.4656767111 | 31.1446277642 | 473 | 504990 | -86.80 | 14.01 | 89.24 | 0.53 | 2.45 | 567 |
| 2024-09-20 22:21:36.549 | MS1 | 121.4656679629 | 31.1446286103 | 473 | 504990 | -87.38 | 16.79 | 72.85 | 0.67 | 2.92 | 694 |
| 2024-09-20 22:21:37.620 | MS1 | 121.4656691359 | 31.1446226544 | 473 | 504990 | -89.06 | 7.60 | 85.42 | 0.52 | 2.42 | 691 |
| 2024-09-20 22:21:38.574 | MS1 | 121.4656682271 | 31.1446272358 | 473 | 504990 | -93.61 | 8.33 | 72.49 | 0.51 | 2.63 | 643 |
| 2024-09-20 22:21:39.379 | MS1 | 121.4656608654 | 31.1446322532 | 473 | 504990 | -92.43 | 8.04 | 84.00 | 0.68 | 2.38 | 573 |
| 2024-09-20 22:21:40.909 | MS1 | 121.4656689986 | 31.1446370693 | 473 | 504990 | -93.75 | 11.48 | 419.01 | 0.17 | 2.21 | 1581 |
| 2024-09-20 22:21:41.629 | MS1 | 121.4656666321 | 31.1446261582 | 473 | 504990 | -89.25 | 8.19 | 310.08 | 0.07 | 2.33 | 1576 |
| 2024-09-20 22:21:42.865 | MS1 | 121.4656632528 | 31.1446275223 | 473 | 504990 | -91.64 | 11.17 | 450.41 | 0.12 | 2.31 | 1572 |

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
| 3216107 | 1 | 121.4756097303 | 31.1453812423 | 307 | 0 | 6 | 15.6 | TDD | 473 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3225516 | 4 | 121.4704691256 | 31.1483910710 | 124 | 15 | 2 | 31.8 | TDD | 15 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3270877 | 3 | 121.4747879969 | 31.1510818641 | 235 | 7 | 1 | 49.8 | TDD | 291 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3278746 | 2 | 121.4700393354 | 31.1517438419 | 274 | 1 | 3 | 40.3 | TDD | 106 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:31.117 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.263 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.263 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.941 | NREventA3 | measId:2;ServCellPCI:938;Se... |
| 2024-09-20 22:21:38.181 | NRHandoverAttempt | SourcePCI:938;SourceNR-ARFC... |
| 2024-09-20 22:21:38.227 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.238 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.363 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.363 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3216107 | 1 | 10.0320 | 13.0498 | -114.1868 | 9.8946 | 142.5979 | 0.0035 | 0.0032 |
| 2024_09_20 22:00 | 3278746 | 2 | 6.4938 | 15.6986 | -117.6917 | 7.1130 | 145.1447 | 0.0023 | 0.0034 |
| 2024_09_20 22:00 | 3270877 | 3 | 15.6758 | 7.7514 | -116.3164 | 14.6586 | 126.3256 | 0.0008 | 0.0009 |
| 2024_09_20 22:00 | 3225516 | 4 | 13.5603 | 14.0661 | -116.9586 | 12.2350 | 190.8127 | 0.0192 | 0.0020 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413126_4DA7C952 | 504990 | 473 | -88.3 | 504990 | 15 | -92.7 | 504990 | 106 | -97.2 | 504990 | 291 |
| MR_1774413126_3BCF7994 | 504990 | 473 | -88.4 | 504990 | 15 | -90.9 | 504990 | 106 | -97.6 | 504990 | 291 |
| MR_1774413126_454FCE86 | 504990 | 473 | -88.4 | 504990 | 15 | -92.1 | 504990 | 106 | -98.8 | 504990 | 291 |
| MR_1774413126_5D824C0C | 504990 | 473 | -91.5 | 504990 | 15 | -90.9 | 504990 | 106 | -100.6 | 504990 | 291 |
| MR_1774413126_DDE3A853 | 504990 | 473 | -91.5 | 504990 | 15 | -91.9 | 504990 | 106 | -98.7 | 504990 | 291 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 114: `7aec481f-6b4...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `7aec481f-6b42-4e6d-a25c-9c90c5f616c8` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[114] topology](images/test_0114.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3224785_1 and 3240227_4
- `C2`: Check test server and transmission issues
- `C3`: Adjust the azimuth of 3224785_1 by 50 degrees
- `C4`: Lift the tilt angle  of 3240227_4 by 3 degrees
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3240227_4
- `C6`: Insufficient data; more data is needed for judgment.
- `C7`: Press down the tilt angle  of 3240227_4 by 3 degrees
- `C8`: Increase transmission power for 3224785_1
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3224785_1
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3240227_4
- `C11`: Increase transmission power for 3240227_4
- `C12`: Decrease transmission power for 3240227_4
- `C13`: Increase A3 Offset threshold for 3224785_1
- `C14`: Add neighbor relationship between 3244550_3 and 3240227_4
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3224785_1
- `C16`: Lift the tilt angle of 3224785_1 by 10 degrees
- `C17`: Decrease A3 Offset threshold for 3240227_4
- `C18`: Decrease A3 Offset threshold for 3224785_1
- `C19`: Increase A3 Offset threshold for 3240227_4
- `C20`: Adjust the azimuth of 3240227_4 by 29 degrees
- `C21`: Press down the tilt angle of 3224785_1 by 10 degrees
- `C22`: Decrease transmission power for 3224785_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.910 | MS1 | 121.4656654868 | 31.1446356574 | 96 | 504990 | -83.84 | 15.26 | 574.36 | 0.03 | 2.68 | 1590 |
| 2024-09-20 22:21:32.376 | MS1 | 121.4656741515 | 31.1446206484 | 96 | 504990 | -78.46 | 12.37 | 523.76 | 0.17 | 2.13 | 1587 |
| 2024-09-20 22:21:33.692 | MS1 | 121.4656765734 | 31.1446352151 | 96 | 504990 | -84.73 | 14.19 | 421.77 | 0.19 | 2.80 | 1562 |
| 2024-09-20 22:21:34.324 | MS1 | 121.4656688324 | 31.1446309517 | 96 | 504990 | -84.17 | -1.58 | 79.70 | 0.03 | 1.06 | 1562 |
| 2024-09-20 22:21:35.111 | MS1 | 121.4656762419 | 31.1446269759 | 96 | 504990 | -91.86 | -2.10 | 40.52 | 0.06 | 1.47 | 1598 |
| 2024-09-20 22:21:36.214 | MS1 | 121.4656585077 | 31.1446318510 | 96 | 504990 | -88.61 | -0.26 | 71.10 | 0.06 | 1.31 | 1594 |
| 2024-09-20 22:21:37.141 | MS1 | 121.4656682513 | 31.1446239097 | 96 | 504990 | -91.67 | -1.86 | 64.76 | 0.03 | 1.00 | 1590 |
| 2024-09-20 22:21:38.255 | MS1 | 121.4656599594 | 31.1446310820 | 96 | 504990 | -90.75 | -2.19 | 64.32 | 0.10 | 1.18 | 1599 |
| 2024-09-20 22:21:39.265 | MS1 | 121.4656607080 | 31.1446227899 | 502 | 504990 | -78.07 | 16.26 | 204.86 | 0.18 | 1.48 | 1564 |
| 2024-09-20 22:21:40.319 | MS1 | 121.4656697510 | 31.1446192164 | 502 | 504990 | -76.62 | 12.08 | 365.18 | 0.10 | 2.05 | 1598 |
| 2024-09-20 22:21:41.774 | MS1 | 121.4656658131 | 31.1446334616 | 502 | 504990 | -84.04 | 13.04 | 330.24 | 0.15 | 2.51 | 1563 |
| 2024-09-20 22:21:42.896 | MS1 | 121.4656687526 | 31.1446247802 | 502 | 504990 | -83.92 | 14.88 | 578.00 | 0.15 | 2.93 | 1585 |

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
| 3224785 | 1 | 121.4751714489 | 31.1481762368 | 95 | 10 | 0 | 28.8 | TDD | 96 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3240227 | 4 | 121.4679679587 | 31.1546690611 | 162 | 1 | 1 | 39.4 | TDD | 502 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3244550 | 3 | 121.4735473608 | 31.1475382194 | 115 | 10 | 7 | 28.0 | TDD | 149 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3279741 | 2 | 121.4718339562 | 31.1556328989 | 335 | 14 | 9 | 28.5 | TDD | 624 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |

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
| 2024-09-20 22:21:31.549 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.573 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.719 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.719 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.351 | NREventA3 | measId:2;ServCellPCI:196;Se... |
| 2024-09-20 22:21:38.591 | NRHandoverAttempt | SourcePCI:196;SourceNR-ARFC... |
| 2024-09-20 22:21:38.629 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.643 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.747 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.747 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3224785 | 1 | 11.3296 | 17.0037 | -116.4725 | 13.8780 | 155.9527 | 0.0051 | 0.1577 |
| 2024_09_20 22:00 | 3279741 | 2 | 12.9143 | 13.0083 | -117.2014 | 10.4022 | 112.6441 | 0.0002 | 0.0038 |
| 2024_09_20 22:00 | 3244550 | 3 | 11.8610 | 6.3059 | -114.4562 | 11.6398 | 108.3633 | 0.0069 | 0.0109 |
| 2024_09_20 22:00 | 3240227 | 4 | 19.6946 | 8.4535 | -116.2977 | 18.5889 | 194.6468 | 0.0063 | 0.0118 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412080_4B7717F3 | 504990 | 502 | -77.9 | 504990 | 96 | -83.3 | 504990 | 149 | -81.5 | 504990 | 624 |
| MR_1774412080_0FBF51D5 | 504990 | 502 | -77.9 | 504990 | 96 | -83.3 | 504990 | 149 | -82.3 | 504990 | 624 |
| MR_1774412080_A76F5751 | 504990 | 502 | -77.0 | 504990 | 96 | -85.9 | 504990 | 149 | -85.1 | 504990 | 624 |
| MR_1774412080_F8EB069F | 504990 | 502 | -80.5 | 504990 | 96 | -85.0 | 504990 | 149 | -83.3 | 504990 | 624 |
| MR_1774412080_456CF092 | 504990 | 96 | -82.2 | 504990 | 502 | -80.7 | 504990 | 149 | -84.8 | 504990 | 624 |
| MR_1774412080_B3A4F97E | 504990 | 96 | -82.2 | 504990 | 502 | -79.4 | 504990 | 149 | -84.2 | 504990 | 624 |
| MR_1774412080_BCC49FEA | 504990 | 502 | -80.7 | 504990 | 96 | -83.1 | 504990 | 149 | -84.9 | 504990 | 624 |
| MR_1774412080_AA5D5656 | 504990 | 502 | -79.2 | 504990 | 96 | -83.5 | 504990 | 149 | -84.8 | 504990 | 624 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 115: `9551a39a-122...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `9551a39a-1226-4739-89bf-8cf8e2528b3d` |
| Tag | **multiple-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[115] topology](images/test_0115.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 5 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 5개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3256122_4 by 4 degrees
- `C2`: Add neighbor relationship between 3250010_5 and 3214199_1
- `C3`: Decrease A3 Offset threshold for 3256122_4
- `C4`: Insufficient data; more data is needed for judgment.
- `C5`: Increase A3 Offset threshold for 3214199_1
- `C6`: Lift the tilt angle of 3256122_4 by 4 degrees
- `C7`: Increase transmission power for 3256122_4
- `C8`: Decrease transmission power for 3214199_1
- `C9`: Adjust the azimuth of 3256122_4 by 24 degrees
- `C10`: Increase transmission power for 3214199_1
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3214199_1
- `C12`: Increase A3 Offset threshold for 3256122_4
- `C13`: Press down the tilt angle  of 3214199_1 by 5 degrees
- `C14`: Decrease transmission power for 3256122_4
- `C15`: Lift the tilt angle  of 3214199_1 by 5 degrees
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3256122_4
- `C17`: Add neighbor relationship between 3256122_4 and 3214199_1
- `C18`: Check test server and transmission issues
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3214199_1
- `C20`: Decrease A3 Offset threshold for 3214199_1
- `C21`: Adjust the azimuth of 3214199_1 by 39 degrees
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3256122_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.583 | MS1 | 121.4656583850 | 31.1446253261 | 953 | 504990 | -78.49 | 16.41 | 313.84 | 0.08 | 2.99 | 1562 |
| 2024-09-20 22:21:32.206 | MS1 | 121.4656624339 | 31.1446263597 | 953 | 504990 | -80.09 | 13.16 | 555.77 | 0.06 | 2.41 | 1576 |
| 2024-09-20 22:21:33.308 | MS1 | 121.4656759512 | 31.1446237618 | 953 | 504990 | -77.72 | 14.85 | 414.75 | 0.19 | 2.70 | 1569 |
| 2024-09-20 22:21:34.133 | MS1 | 121.4656599974 | 31.1446212808 | 626 | 504990 | -82.16 | 1.25 | 54.76 | 0.19 | 1.26 | 1593 |
| 2024-09-20 22:21:35.429 | MS1 | 121.4656663778 | 31.1446338427 | 626 | 504990 | -88.78 | 4.37 | 36.07 | 0.17 | 1.13 | 1562 |
| 2024-09-20 22:21:36.561 | MS1 | 121.4656639792 | 31.1446303231 | 953 | 504990 | -80.87 | 2.82 | 64.35 | 0.19 | 1.47 | 1594 |
| 2024-09-20 22:21:37.916 | MS1 | 121.4656651443 | 31.1446234660 | 953 | 504990 | -85.03 | 3.44 | 52.33 | 0.01 | 1.50 | 1572 |
| 2024-09-20 22:21:38.485 | MS1 | 121.4656745169 | 31.1446267814 | 626 | 504990 | -83.05 | 2.72 | 35.75 | 0.15 | 1.38 | 1587 |
| 2024-09-20 22:21:39.857 | MS1 | 121.4656748527 | 31.1446371859 | 626 | 504990 | -89.29 | 1.91 | 66.36 | 0.08 | 1.07 | 1562 |
| 2024-09-20 22:21:40.170 | MS1 | 121.4656617909 | 31.1446311815 | 626 | 504990 | -83.93 | 16.07 | 416.42 | 0.11 | 2.99 | 1587 |
| 2024-09-20 22:21:41.131 | MS1 | 121.4656721754 | 31.1446296598 | 626 | 504990 | -79.22 | 17.60 | 366.72 | 0.16 | 2.85 | 1573 |
| 2024-09-20 22:21:42.538 | MS1 | 121.4656764045 | 31.1446335478 | 626 | 504990 | -78.33 | 15.86 | 418.75 | 0.08 | 2.68 | 1585 |

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
| 3214199 | 1 | 121.4700844462 | 31.1531398050 | 165 | 3 | 11 | 43.1 | TDD | 496 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3229309 | 2 | 121.4712352698 | 31.1472809795 | 26 | 15 | 5 | 19.2 | TDD | 626 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3234000 | 3 | 121.4693736867 | 31.1508179030 | 76 | 13 | 8 | 47.9 | TDD | 180 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3250010 | 5 | 121.4697970517 | 31.1466401636 | 121 | 4 | 10 | 17.7 | TDD | 447 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3256122 | 4 | 121.4735901503 | 31.1532594742 | 194 | 2 | 0 | 38.3 | TDD | 953 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |

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
| 2024-09-20 22:21:31.620 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.753 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.753 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.435 | NREventA3 | measId:2;ServCellPCI:781;Se... |
| 2024-09-20 22:21:34.675 | NRHandoverAttempt | SourcePCI:781;SourceNR-ARFC... |
| 2024-09-20 22:21:34.717 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:34.732 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:34.874 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:34.874 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:36.435 | NREventA3 | measId:2;ServCellPCI:630;Se... |
| 2024-09-20 22:21:36.675 | NRHandoverAttempt | SourcePCI:630;SourceNR-ARFC... |
| 2024-09-20 22:21:36.724 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:36.737 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:36.877 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.877 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.435 | NREventA3 | measId:2;ServCellPCI:781;Se... |
| 2024-09-20 22:21:38.675 | NRHandoverAttempt | SourcePCI:781;SourceNR-ARFC... |
| 2024-09-20 22:21:38.707 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.720 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.868 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.868 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3214199 | 1 | 7.0238 | 10.6482 | -114.1273 | 5.4839 | 147.4365 | 0.0090 | 0.0150 |
| 2024_09_20 22:00 | 3229309 | 2 | 16.4453 | 7.1855 | -114.1062 | 16.7765 | 138.6787 | 0.0046 | 0.0092 |
| 2024_09_20 22:00 | 3234000 | 3 | 9.4007 | 13.6122 | -117.3826 | 13.1169 | 164.6419 | 0.0003 | 0.0024 |
| 2024_09_20 22:00 | 3256122 | 4 | 17.6489 | 8.8693 | -115.4063 | 17.2715 | 140.9087 | 0.0173 | 0.0199 |
| 2024_09_20 22:00 | 3250010 | 5 | 10.1121 | 12.3753 | -115.2463 | 12.5991 | 136.7943 | 0.0112 | 0.0009 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412881_8A56DFC7 | 504990 | 626 | -83.8 | 504990 | 953 | -84.5 | 504990 | 496 | -86.5 | 504990 | 447 |
| MR_1774412881_D2F78FFC | 504990 | 626 | -81.5 | 504990 | 953 | -83.2 | 504990 | 496 | -90.0 | 504990 | 447 |
| MR_1774412881_480A82EB | 504990 | 626 | -81.9 | 504990 | 953 | -82.1 | 504990 | 496 | -88.1 | 504990 | 447 |
| MR_1774412881_5E61563D | 504990 | 626 | -81.0 | 504990 | 953 | -82.2 | 504990 | 496 | -88.2 | 504990 | 447 |
| MR_1774412881_1EDE297E | 504990 | 626 | -83.5 | 504990 | 953 | -84.7 | 504990 | 496 | -87.1 | 504990 | 447 |
| MR_1774412881_7F4CD1E5 | 504990 | 953 | -81.9 | 504990 | 626 | -82.9 | 504990 | 496 | -87.0 | 504990 | 447 |
| MR_1774412881_13E90939 | 504990 | 626 | -80.7 | 504990 | 953 | -82.2 | 504990 | 496 | -90.1 | 504990 | 447 |
| MR_1774412881_D4F7AADC | 504990 | 626 | -83.6 | 504990 | 953 | -81.3 | 504990 | 496 | -89.1 | 504990 | 447 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 116: `83fdbfdb-16e...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `83fdbfdb-16e1-4ba9-b362-6d37ccbd0ef9` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[116] topology](images/test_0116.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3211741_2 by 10 degrees
- `C2`: Press down the tilt angle of 3215563_1 by 5 degrees
- `C3`: Insufficient data; more data is needed for judgment.
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3215539_4
- `C5`: Adjust the azimuth of 3211741_2 by 6 degrees
- `C6`: Add neighbor relationship between 3211741_2 and 3215539_4
- `C7`: Increase transmission power for 3215539_4
- `C8`: Lift the tilt angle  of 3211741_2 by 10 degrees
- `C9`: Add neighbor relationship between 3215563_1 and 3215539_4
- `C10`: Adjust the azimuth of 3215563_1 by 33 degrees
- `C11`: Check test server and transmission issues
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3215563_1
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3215539_4
- `C14`: Increase A3 Offset threshold for 3215563_1
- `C15`: Lift the tilt angle of 3215563_1 by 5 degrees
- `C16`: Increase transmission power for 3215563_1
- `C17`: Decrease A3 Offset threshold for 3215563_1
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3215563_1
- `C19`: Decrease transmission power for 3215539_4
- `C20`: Increase A3 Offset threshold for 3215539_4
- `C21`: Decrease transmission power for 3215563_1
- `C22`: Decrease A3 Offset threshold for 3215539_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.462 | MS1 | 121.4656614874 | 31.1446327285 | 767 | 504990 | -86.98 | 15.50 | 431.07 | 0.06 | 2.16 | 1563 |
| 2024-09-20 22:21:32.160 | MS1 | 121.4656709946 | 31.1446225616 | 767 | 504990 | -90.46 | 12.64 | 372.90 | 0.17 | 2.06 | 1580 |
| 2024-09-20 22:21:33.950 | MS1 | 121.4656603588 | 31.1446293167 | 767 | 504990 | -88.73 | 12.82 | 565.99 | 0.18 | 2.87 | 1583 |
| 2024-09-20 22:21:34.542 | MS1 | 121.4656719749 | 31.1446198971 | 767 | 504990 | -90.88 | 12.89 | 63.61 | 0.13 | 2.23 | 1598 |
| 2024-09-20 22:21:35.368 | MS1 | 121.4656671733 | 31.1446265365 | 767 | 504990 | -88.65 | 17.61 | 104.96 | 0.09 | 2.76 | 1585 |
| 2024-09-20 22:21:36.532 | MS1 | 121.4656677201 | 31.1446317361 | 767 | 504990 | -87.34 | 17.85 | 90.72 | 0.12 | 2.27 | 1579 |
| 2024-09-20 22:21:37.878 | MS1 | 121.4656750827 | 31.1446238446 | 767 | 504990 | -89.54 | 12.70 | 70.66 | 0.05 | 2.10 | 1578 |
| 2024-09-20 22:21:38.290 | MS1 | 121.4656660160 | 31.1446280771 | 767 | 504990 | -90.16 | 10.20 | 66.73 | 0.15 | 2.77 | 1587 |
| 2024-09-20 22:21:39.635 | MS1 | 121.4656730722 | 31.1446263854 | 767 | 504990 | -92.52 | 9.86 | 100.92 | 0.08 | 2.55 | 1593 |
| 2024-09-20 22:21:40.395 | MS1 | 121.4656740285 | 31.1446324376 | 767 | 504990 | -92.08 | 11.29 | 318.36 | 0.04 | 2.13 | 1563 |
| 2024-09-20 22:21:41.908 | MS1 | 121.4656717866 | 31.1446326354 | 767 | 504990 | -92.02 | 11.87 | 505.32 | 0.03 | 2.88 | 1596 |
| 2024-09-20 22:21:42.275 | MS1 | 121.4656601675 | 31.1446326069 | 767 | 504990 | -90.66 | 9.19 | 343.69 | 0.08 | 2.48 | 1600 |

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
| 3211741 | 2 | 121.4725857998 | 31.1548219197 | 281 | 2 | 4 | 47.4 | TDD | 839 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3215539 | 4 | 121.4690073443 | 31.1440705721 | 275 | 8 | 9 | 35.3 | TDD | 775 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3215563 | 1 | 121.4651397309 | 31.1526943389 | 144 | 3 | 5 | 39.1 | TDD | 767 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3228815 | 3 | 121.4663979922 | 31.1500412884 | 204 | 12 | 10 | 47.7 | TDD | 630 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |

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
| 2024-09-20 22:21:31.326 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.341 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.451 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.451 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.216 | NREventA3 | measId:2;ServCellPCI:99;Ser... |
| 2024-09-20 22:21:38.456 | NRHandoverAttempt | SourcePCI:99;SourceNR-ARFCN... |
| 2024-09-20 22:21:38.489 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.503 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.612 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.612 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3215563 | 1 | 78.8019 | 86.4317 | -116.8831 | 8.6124 | 154.9926 | 0.0002 | 0.0124 |
| 2024_09_20 22:00 | 3211741 | 2 | 8.4671 | 7.3340 | -114.0283 | 18.0361 | 116.1834 | 0.0085 | 0.0025 |
| 2024_09_20 22:00 | 3228815 | 3 | 8.3498 | 13.9895 | -114.5987 | 13.9306 | 142.2469 | 0.0005 | 0.0073 |
| 2024_09_20 22:00 | 3215539 | 4 | 16.8784 | 5.5615 | -114.2899 | 15.6412 | 131.6225 | 0.0170 | 0.0199 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412084_59FECF41 | 504990 | 767 | -90.6 | 504990 | 775 | -99.7 | 504990 | 839 | -103.2 | 504990 | 630 |
| MR_1774412084_B3ED4080 | 504990 | 767 | -90.9 | 504990 | 775 | -97.6 | 504990 | 839 | -104.1 | 504990 | 630 |
| MR_1774412084_13D632B8 | 504990 | 767 | -92.6 | 504990 | 775 | -99.2 | 504990 | 839 | -101.4 | 504990 | 630 |
| MR_1774412084_1D087147 | 504990 | 767 | -92.5 | 504990 | 775 | -98.2 | 504990 | 839 | -104.7 | 504990 | 630 |
| MR_1774412084_ABE409E2 | 504990 | 767 | -92.9 | 504990 | 775 | -98.7 | 504990 | 839 | -103.3 | 504990 | 630 |
| MR_1774412084_75BA302F | 504990 | 767 | -90.3 | 504990 | 775 | -98.0 | 504990 | 839 | -101.7 | 504990 | 630 |
| MR_1774412084_910A428D | 504990 | 767 | -90.0 | 504990 | 775 | -96.4 | 504990 | 839 | -105.2 | 504990 | 630 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 117: `27f00cc5-f01...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `27f00cc5-f01a-4beb-82d8-a992850aabed` |
| Tag | **multiple-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[117] topology](images/test_0117.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3260202_3 and 3235611_1
- `C2`: Adjust the azimuth of 3235611_1 by 16 degrees
- `C3`: Insufficient data; more data is needed for judgment.
- `C4`: Decrease A3 Offset threshold for 3235611_1
- `C5`: Increase A3 Offset threshold for 3229023_2
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3235611_1
- `C7`: Decrease transmission power for 3235611_1
- `C8`: Increase transmission power for 3235611_1
- `C9`: Decrease transmission power for 3229023_2
- `C10`: Lift the tilt angle of 3229023_2 by 4 degrees
- `C11`: Lift the tilt angle  of 3235611_1 by 6 degrees
- `C12`: Increase A3 Offset threshold for 3235611_1
- `C13`: Add neighbor relationship between 3229023_2 and 3235611_1
- `C14`: Press down the tilt angle of 3229023_2 by 4 degrees
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3229023_2
- `C16`: Adjust the azimuth of 3229023_2 by 1 degrees
- `C17`: Check test server and transmission issues
- `C18`: Increase transmission power for 3229023_2
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3229023_2
- `C20`: Press down the tilt angle  of 3235611_1 by 6 degrees
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3235611_1
- `C22`: Decrease A3 Offset threshold for 3229023_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.296 | MS1 | 121.4656776412 | 31.1446300153 | 49 | 504990 | -77.47 | 12.52 | 370.26 | 0.10 | 2.93 | 1568 |
| 2024-09-20 22:21:32.265 | MS1 | 121.4656767832 | 31.1446311990 | 49 | 504990 | -76.24 | 15.51 | 377.06 | 0.17 | 2.56 | 1569 |
| 2024-09-20 22:21:33.586 | MS1 | 121.4656635506 | 31.1446376839 | 49 | 504990 | -76.65 | 12.94 | 452.67 | 0.14 | 2.13 | 1588 |
| 2024-09-20 22:21:34.205 | MS1 | 121.4656587031 | 31.1446229888 | 49 | 504990 | -94.08 | 1.78 | 56.92 | 0.06 | 1.39 | 1597 |
| 2024-09-20 22:21:35.685 | MS1 | 121.4656710497 | 31.1446254370 | 49 | 504990 | -91.38 | 2.50 | 87.92 | 0.15 | 1.00 | 1583 |
| 2024-09-20 22:21:36.703 | MS1 | 121.4656736423 | 31.1446201990 | 49 | 504990 | -85.32 | 0.77 | 75.02 | 0.05 | 1.19 | 1568 |
| 2024-09-20 22:21:37.228 | MS1 | 121.4656743643 | 31.1446312587 | 49 | 504990 | -87.20 | 2.16 | 45.29 | 0.02 | 1.36 | 1572 |
| 2024-09-20 22:21:38.399 | MS1 | 121.4656642270 | 31.1446333284 | 49 | 504990 | -86.16 | 2.73 | 52.60 | 0.02 | 1.35 | 1600 |
| 2024-09-20 22:21:39.918 | MS1 | 121.4656626074 | 31.1446219749 | 49 | 504990 | -89.09 | 1.86 | 96.19 | 0.18 | 1.49 | 1585 |
| 2024-09-20 22:21:40.337 | MS1 | 121.4656682473 | 31.1446313884 | 49 | 504990 | -76.44 | 13.42 | 483.96 | 0.17 | 2.85 | 1576 |
| 2024-09-20 22:21:41.931 | MS1 | 121.4656645930 | 31.1446316429 | 49 | 504990 | -79.70 | 16.00 | 344.19 | 0.17 | 2.57 | 1565 |
| 2024-09-20 22:21:42.928 | MS1 | 121.4656766189 | 31.1446202167 | 49 | 504990 | -78.56 | 12.38 | 493.12 | 0.01 | 2.20 | 1577 |

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
| 3222425 | 4 | 121.4745141939 | 31.1517442926 | 129 | 1 | 6 | 44.8 | TDD | 502 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3229023 | 2 | 121.4716419067 | 31.1517031407 | 215 | 1 | 1 | 44.1 | TDD | 49 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3235611 | 1 | 121.4726266809 | 31.1535139569 | 230 | 4 | 4 | 33.8 | TDD | 408 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3260202 | 3 | 121.4690082417 | 31.1545532463 | 345 | 13 | 2 | 46.3 | TDD | 974 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |

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
| 2024-09-20 22:21:31.142 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.163 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.312 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.312 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3235611 | 1 | 18.4934 | 16.4270 | -116.2876 | 18.9388 | 113.9770 | 0.0002 | 0.0152 |
| 2024_09_20 22:00 | 3229023 | 2 | 16.8877 | 9.8242 | -109.5241 | 13.8880 | 100.2127 | 0.0027 | 0.0008 |
| 2024_09_20 22:00 | 3260202 | 3 | 7.1597 | 13.0783 | -114.4285 | 5.9174 | 121.3708 | 0.0116 | 0.0065 |
| 2024_09_20 22:00 | 3222425 | 4 | 17.1225 | 10.7675 | -117.5092 | 12.0834 | 87.1952 | 0.0194 | 0.0077 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415774_CFDE61A8 | 504990 | 408 | -95.6 | 504990 | 49 | -91.7 | 504990 | 974 | -91.0 | 504990 | 502 |
| MR_1774415774_448CF5C9 | 504990 | 408 | -93.1 | 504990 | 49 | -92.8 | 504990 | 974 | -93.8 | 504990 | 502 |
| MR_1774415774_54550084 | 504990 | 408 | -95.5 | 504990 | 49 | -91.1 | 504990 | 974 | -92.5 | 504990 | 502 |
| MR_1774415774_29741D1E | 504990 | 49 | -92.3 | 504990 | 408 | -91.4 | 504990 | 974 | -93.4 | 504990 | 502 |
| MR_1774415774_EEB0B73A | 504990 | 49 | -96.0 | 504990 | 408 | -90.5 | 504990 | 974 | -93.8 | 504990 | 502 |
| MR_1774415774_4DF5D7A4 | 504990 | 49 | -93.2 | 504990 | 408 | -91.9 | 504990 | 974 | -91.2 | 504990 | 502 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 118: `2a890bdb-5c8...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `2a890bdb-5c85-4ada-83d6-01eb7207d002` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[118] topology](images/test_0118.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3279123_1
- `C2`: Adjust the azimuth of 3279123_1 by 50 degrees
- `C3`: Press down the tilt angle  of 3279123_1 by 10 degrees
- `C4`: Decrease transmission power for 3279123_1
- `C5`: Insufficient data; more data is needed for judgment.
- `C6`: Add neighbor relationship between 3254009_3 and 3279123_1
- `C7`: Decrease transmission power for 3275174_4
- `C8`: Increase A3 Offset threshold for 3279123_1
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3279123_1
- `C10`: Lift the tilt angle of 3275174_4 by 10 degrees
- `C11`: Increase transmission power for 3275174_4
- `C12`: Decrease A3 Offset threshold for 3275174_4
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3275174_4
- `C14`: Increase A3 Offset threshold for 3275174_4
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3275174_4
- `C16`: Check test server and transmission issues
- `C17`: Decrease A3 Offset threshold for 3279123_1
- `C18`: Increase transmission power for 3279123_1
- `C19`: Add neighbor relationship between 3275174_4 and 3279123_1
- `C20`: Press down the tilt angle of 3275174_4 by 10 degrees
- `C21`: Lift the tilt angle  of 3279123_1 by 10 degrees
- `C22`: Adjust the azimuth of 3275174_4 by 50 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.135 | MS1 | 121.4656635546 | 31.1446253083 | 911 | 504990 | -91.31 | 12.58 | 513.10 | 0.19 | 2.10 | 1569 |
| 2024-09-20 22:21:32.101 | MS1 | 121.4656615585 | 31.1446201758 | 911 | 504990 | -85.19 | 15.54 | 356.17 | 0.15 | 2.93 | 1560 |
| 2024-09-20 22:21:33.373 | MS1 | 121.4656744042 | 31.1446364062 | 911 | 504990 | -89.03 | 12.52 | 325.60 | 0.17 | 2.64 | 1566 |
| 2024-09-20 22:21:34.842 | MS1 | 121.4656600690 | 31.1446322788 | 911 | 504990 | -87.99 | 12.66 | 77.12 | 0.13 | 2.77 | 438 |
| 2024-09-20 22:21:35.859 | MS1 | 121.4656695755 | 31.1446323670 | 911 | 504990 | -87.93 | 14.84 | 58.18 | 0.19 | 2.14 | 473 |
| 2024-09-20 22:21:36.838 | MS1 | 121.4656694208 | 31.1446260302 | 911 | 504990 | -87.38 | 17.40 | 77.19 | 0.15 | 2.29 | 461 |
| 2024-09-20 22:21:37.723 | MS1 | 121.4656712496 | 31.1446191652 | 911 | 504990 | -93.56 | 9.34 | 77.19 | 0.00 | 2.75 | 386 |
| 2024-09-20 22:21:38.960 | MS1 | 121.4656618349 | 31.1446314308 | 911 | 504990 | -92.09 | 7.13 | 65.51 | 0.18 | 2.33 | 436 |
| 2024-09-20 22:21:39.748 | MS1 | 121.4656631517 | 31.1446296169 | 911 | 504990 | -92.84 | 9.91 | 72.17 | 0.11 | 2.31 | 441 |
| 2024-09-20 22:21:40.446 | MS1 | 121.4656755043 | 31.1446208232 | 911 | 504990 | -91.96 | 8.13 | 358.33 | 0.18 | 2.59 | 1577 |
| 2024-09-20 22:21:41.754 | MS1 | 121.4656671453 | 31.1446267962 | 911 | 504990 | -91.05 | 7.42 | 365.43 | 0.13 | 2.38 | 1562 |
| 2024-09-20 22:21:42.562 | MS1 | 121.4656605155 | 31.1446359665 | 911 | 504990 | -91.53 | 12.87 | 520.32 | 0.16 | 2.93 | 1561 |

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
| 3215981 | 2 | 121.4656660942 | 31.1440779287 | 142 | 8 | 10 | 47.2 | TDD | 827 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3254009 | 3 | 121.4713602160 | 31.1442111436 | 6 | 11 | 0 | 43.3 | TDD | 531 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3275174 | 4 | 121.4678146018 | 31.1454087211 | 124 | 10 | 3 | 35.9 | TDD | 911 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3279123 | 1 | 121.4710597274 | 31.1473108295 | 337 | 12 | 0 | 47.5 | TDD | 3 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |

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
| 2024-09-20 22:21:31.128 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.145 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.284 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.284 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.021 | NREventA3 | measId:2;ServCellPCI:356;Se... |
| 2024-09-20 22:21:38.261 | NRHandoverAttempt | SourcePCI:356;SourceNR-ARFC... |
| 2024-09-20 22:21:38.308 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.319 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.455 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.455 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3279123 | 1 | 10.2196 | 7.3274 | -116.1498 | 13.2872 | 91.0732 | 0.0169 | 0.0185 |
| 2024_09_20 22:00 | 3215981 | 2 | 5.2600 | 9.9187 | -114.5293 | 15.7976 | 163.0615 | 0.0083 | 0.0112 |
| 2024_09_20 22:00 | 3254009 | 3 | 16.4544 | 14.8489 | -115.6747 | 13.7003 | 123.6122 | 0.0018 | 0.0163 |
| 2024_09_20 22:00 | 3275174 | 4 | 8.6533 | 5.1658 | -115.1305 | 18.2326 | 125.5959 | 0.0077 | 0.0039 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415149_4A7B06B7 | 504990 | 911 | -88.3 | 504990 | 3 | -90.1 | 504990 | 531 | -94.3 | 504990 | 827 |
| MR_1774415149_C9191E86 | 504990 | 911 | -87.8 | 504990 | 3 | -92.0 | 504990 | 531 | -97.3 | 504990 | 827 |
| MR_1774415149_7F73CA38 | 504990 | 911 | -89.0 | 504990 | 3 | -92.2 | 504990 | 531 | -95.3 | 504990 | 827 |
| MR_1774415149_88A81635 | 504990 | 911 | -89.2 | 504990 | 3 | -89.9 | 504990 | 531 | -94.5 | 504990 | 827 |
| MR_1774415149_9D90E7E7 | 504990 | 911 | -86.7 | 504990 | 3 | -90.7 | 504990 | 531 | -96.5 | 504990 | 827 |
| MR_1774415149_B221892C | 504990 | 911 | -89.5 | 504990 | 3 | -92.8 | 504990 | 531 | -94.4 | 504990 | 827 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 119: `76c6d898-030...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `76c6d898-030f-4abc-856e-4bce69c10373` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[119] topology](images/test_0119.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3244064_4
- `C2`: Lift the tilt angle  of 3223483_3 by 10 degrees
- `C3`: Insufficient data; more data is needed for judgment.
- `C4`: Increase A3 Offset threshold for 3216869_2
- `C5`: Adjust the azimuth of 3244064_4 by 22 degrees
- `C6`: Press down the tilt angle  of 3223483_3 by 10 degrees
- `C7`: Add neighbor relationship between 3223483_3 and 3216869_2
- `C8`: Increase A3 Offset threshold for 3244064_4
- `C9`: Increase transmission power for 3216869_2
- `C10`: Adjust the azimuth of 3223483_3 by 50 degrees
- `C11`: Decrease A3 Offset threshold for 3216869_2
- `C12`: Press down the tilt angle of 3244064_4 by 4 degrees
- `C13`: Decrease A3 Offset threshold for 3244064_4
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3244064_4
- `C15`: Decrease transmission power for 3216869_2
- `C16`: Lift the tilt angle of 3244064_4 by 4 degrees
- `C17`: Add neighbor relationship between 3244064_4 and 3216869_2
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3244064_4
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3216869_2
- `C20`: Check test server and transmission issues
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3216869_2
- `C22`: Increase transmission power for 3244064_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.884 | MS1 | 121.4656650303 | 31.1446276662 | 207 | 504990 | -90.74 | 16.90 | 423.12 | 0.06 | 2.54 | 1566 |
| 2024-09-20 22:21:32.670 | MS1 | 121.4656585552 | 31.1446304778 | 207 | 504990 | -88.05 | 14.65 | 582.29 | 0.09 | 2.27 | 1581 |
| 2024-09-20 22:21:33.305 | MS1 | 121.4656719235 | 31.1446267146 | 207 | 504990 | -88.82 | 14.78 | 350.99 | 0.11 | 2.37 | 1575 |
| 2024-09-20 22:21:34.474 | MS1 | 121.4656709548 | 31.1446192331 | 207 | 504990 | -91.45 | 15.46 | 63.48 | 0.19 | 2.86 | 1600 |
| 2024-09-20 22:21:35.728 | MS1 | 121.4656763463 | 31.1446200333 | 207 | 504990 | -88.35 | 14.76 | 75.08 | 0.09 | 2.59 | 1587 |
| 2024-09-20 22:21:36.603 | MS1 | 121.4656606881 | 31.1446344596 | 207 | 504990 | -91.58 | 13.15 | 57.49 | 0.05 | 2.62 | 1600 |
| 2024-09-20 22:21:37.168 | MS1 | 121.4656732871 | 31.1446374810 | 207 | 504990 | -90.09 | 7.81 | 75.44 | 0.12 | 2.04 | 1561 |
| 2024-09-20 22:21:38.466 | MS1 | 121.4656740413 | 31.1446207376 | 207 | 504990 | -89.39 | 8.54 | 94.51 | 0.03 | 2.86 | 1564 |
| 2024-09-20 22:21:39.409 | MS1 | 121.4656776336 | 31.1446277345 | 207 | 504990 | -92.32 | 11.02 | 90.75 | 0.03 | 2.75 | 1561 |
| 2024-09-20 22:21:40.899 | MS1 | 121.4656673182 | 31.1446189603 | 207 | 504990 | -91.46 | 7.97 | 360.09 | 0.13 | 2.80 | 1568 |
| 2024-09-20 22:21:41.579 | MS1 | 121.4656709601 | 31.1446237779 | 207 | 504990 | -91.80 | 12.40 | 547.71 | 0.06 | 2.44 | 1563 |
| 2024-09-20 22:21:42.671 | MS1 | 121.4656708342 | 31.1446206659 | 207 | 504990 | -89.65 | 12.18 | 406.97 | 0.02 | 2.07 | 1564 |

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
| 3216869 | 2 | 121.4654120866 | 31.1454546001 | 344 | 0 | 3 | 17.6 | TDD | 524 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3223483 | 3 | 121.4698805842 | 31.1466014825 | 352 | 1 | 11 | 49.0 | TDD | 285 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3244064 | 4 | 121.4754440173 | 31.1495460232 | 218 | 3 | 3 | 26.7 | TDD | 207 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3253699 | 1 | 121.4672548544 | 31.1442352620 | 0 | 0 | 7 | 31.2 | TDD | 425 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |

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
| 2024-09-20 22:21:30.924 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.946 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.053 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.053 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.761 | NREventA3 | measId:2;ServCellPCI:821;Se... |
| 2024-09-20 22:21:38.001 | NRHandoverAttempt | SourcePCI:821;SourceNR-ARFC... |
| 2024-09-20 22:21:38.045 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.058 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.161 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.161 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3253699 | 1 | 14.3105 | 17.3715 | -114.4517 | 6.4050 | 136.2878 | 0.0192 | 0.0114 |
| 2024_09_20 22:00 | 3216869 | 2 | 15.9807 | 13.1123 | -115.4593 | 10.8872 | 119.0439 | 0.0016 | 0.0008 |
| 2024_09_20 22:00 | 3223483 | 3 | 13.4305 | 15.2943 | -117.5999 | 19.5427 | 144.5516 | 0.0099 | 0.0140 |
| 2024_09_20 22:00 | 3244064 | 4 | 91.7344 | 91.4685 | -117.5344 | 17.9212 | 110.5541 | 0.0083 | 0.0099 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413596_1DBBC27C | 504990 | 207 | -92.2 | 504990 | 524 | -100.2 | 504990 | 285 | -104.6 | 504990 | 425 |
| MR_1774413596_26BE60D9 | 504990 | 207 | -91.6 | 504990 | 524 | -96.6 | 504990 | 285 | -106.9 | 504990 | 425 |
| MR_1774413596_77FCDA48 | 504990 | 207 | -90.4 | 504990 | 524 | -98.3 | 504990 | 285 | -106.1 | 504990 | 425 |
| MR_1774413596_BAC29110 | 504990 | 207 | -89.5 | 504990 | 524 | -98.8 | 504990 | 285 | -104.7 | 504990 | 425 |
| MR_1774413596_C2AAD87C | 504990 | 207 | -90.5 | 504990 | 524 | -99.3 | 504990 | 285 | -104.1 | 504990 | 425 |
| MR_1774413596_E51566F4 | 504990 | 207 | -91.4 | 504990 | 524 | -97.2 | 504990 | 285 | -106.7 | 504990 | 425 |
| MR_1774413596_4CEAE90E | 504990 | 207 | -91.3 | 504990 | 524 | -98.8 | 504990 | 285 | -105.6 | 504990 | 425 |
| MR_1774413596_A1249409 | 504990 | 207 | -90.5 | 504990 | 524 | -98.4 | 504990 | 285 | -106.6 | 504990 | 425 |

> *... 2개 열 생략 (전체 14열)*

---
