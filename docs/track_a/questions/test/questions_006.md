# Track A 문제 분석 — test[50]~test[59]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/test.json`
> 범위: test[50] ~ test[59] (10개)

## 목차

1. [문제 50: `eb655747-35b...`](#50) — single-answer
2. [문제 51: `2e3d9609-f71...`](#51) — single-answer
3. [문제 52: `7283e6f7-0f5...`](#52) — single-answer
4. [문제 53: `e9d5b45b-6be...`](#53) — single-answer
5. [문제 54: `07fb0741-dbe...`](#54) — single-answer
6. [문제 55: `eb31cd59-dac...`](#55) — single-answer
7. [문제 56: `09a398d6-d9a...`](#56) — single-answer
8. [문제 57: `33780221-c9b...`](#57) — single-answer
9. [문제 58: `059e81bf-125...`](#58) — multiple-answer
10. [문제 59: `2c8c8f98-5c3...`](#59) — single-answer

---

### 문제 50: `eb655747-35b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `eb655747-35b4-4ea2-bf73-5bb03e299faa` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[50] topology](images/test_0050.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3243392_5
- `C2`: Press down the tilt angle  of 3243392_5 by 2 degrees
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3243392_5
- `C4`: Adjust the azimuth of 3243392_5 by 29 degrees
- `C5`: Insufficient data; more data is needed for judgment.
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3221599_4
- `C7`: Adjust the azimuth of 3221599_4 by 0 degrees
- `C8`: Add neighbor relationship between 3221599_4 and 3243392_5
- `C9`: Check test server and transmission issues
- `C10`: Increase A3 Offset threshold for 3243392_5
- `C11`: Decrease A3 Offset threshold for 3221599_4
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3243392_5
- `C13`: Decrease transmission power for 3243392_5
- `C14`: Increase A3 Offset threshold for 3221599_4
- `C15`: Lift the tilt angle of 3221599_4 by 5 degrees
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3221599_4
- `C17`: Increase transmission power for 3221599_4
- `C18`: Add neighbor relationship between 3244920_10 and 3243392_5
- `C19`: Press down the tilt angle of 3221599_4 by 5 degrees
- `C20`: Decrease transmission power for 3221599_4
- `C21`: Lift the tilt angle  of 3243392_5 by 2 degrees
- `C22`: Increase transmission power for 3243392_5

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.801 | MS1 | 121.4656626822 | 31.1446320413 | 684 | 504990 | -93.41 | 9.41 | 449.90 | 0.11 | 2.91 | 1590 |
| 2024-09-20 22:21:32.264 | MS1 | 121.4656699544 | 31.1446233102 | 296 | 504990 | -94.47 | 13.48 | 437.70 | 0.17 | 2.97 | 1580 |
| 2024-09-20 22:21:33.618 | MS1 | 121.4656603320 | 31.1446260456 | 65 | 504990 | -95.45 | 14.56 | 487.22 | 0.01 | 2.58 | 1570 |
| 2024-09-20 22:21:34.200 | MS1 | 121.4656585559 | 31.1446355451 | 793 | 152650 | -91.84 | 7.68 | 62.97 | 0.14 | 1.91 | 924 |
| 2024-09-20 22:21:35.123 | MS1 | 121.4656631410 | 31.1446341832 | 286 | 152650 | -93.31 | 7.88 | 49.87 | 0.16 | 1.78 | 973 |
| 2024-09-20 22:21:36.572 | MS1 | 121.4656773928 | 31.1446301150 | 563 | 152650 | -88.32 | 6.65 | 89.38 | 0.15 | 1.71 | 913 |
| 2024-09-20 22:21:37.584 | MS1 | 121.4656738597 | 31.1446235053 | 389 | 152650 | -91.95 | 7.76 | 52.66 | 0.01 | 1.50 | 989 |
| 2024-09-20 22:21:38.861 | MS1 | 121.4656775898 | 31.1446284070 | 793 | 152650 | -90.26 | 7.14 | 71.18 | 0.02 | 1.91 | 971 |
| 2024-09-20 22:21:39.399 | MS1 | 121.4656639411 | 31.1446375100 | 286 | 152650 | -92.43 | 3.99 | 61.37 | 0.06 | 1.65 | 962 |
| 2024-09-20 22:21:40.635 | MS1 | 121.4656774896 | 31.1446234240 | 563 | 152650 | -88.59 | 7.23 | 74.93 | 0.15 | 2.97 | 1589 |
| 2024-09-20 22:21:41.189 | MS1 | 121.4656645951 | 31.1446193178 | 389 | 152650 | -89.01 | 5.90 | 68.62 | 0.06 | 2.05 | 1578 |
| 2024-09-20 22:21:42.893 | MS1 | 121.4656747067 | 31.1446332898 | 793 | 152650 | -96.18 | 5.66 | 51.64 | 0.14 | 2.44 | 1563 |

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
| 3210597 | 3 | 121.4657379810 | 31.1441434624 | 217 | 11 | 3 | 22.3 | TDD | 296 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3215909 | 13 | 121.4727043632 | 31.1553541360 | 250 | 8 | 11 | 17.8 | FDD | 286 | n1 | 152650 | 30M | 4T4R | 30 | 152650 |
| 3221599 | 4 | 121.4743848864 | 31.1505705342 | 232 | 5 | 3 | 4.2 | TDD | 684 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3240072 | 7 | 121.4703028311 | 31.1502267467 | 90 | 0 | 11 | 2.3 | FDD | 389 | n1 | 152650 | 30M | 4T4R | 17 | 152650 |
| 3243255 | 8 | 121.4650543806 | 31.1523612474 | 47 | 7 | 3 | 29.4 | FDD | 881 | n1 | 152650 | 30M | 4T4R | 24 | 152650 |
| 3243392 | 5 | 121.4684948925 | 31.1467047653 | 258 | 1 | 12 | 6.9 | TDD | 244 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3244920 | 10 | 121.4728743881 | 31.1516417459 | 6 | 9 | 2 | 3.7 | FDD | 563 | n1 | 152650 | 30M | 4T4R | 27 | 152650 |
| 3252685 | 11 | 121.4735861729 | 31.1559497779 | 8 | 13 | 0 | 5.3 | FDD | 87 | n1 | 152650 | 30M | 4T4R | 15 | 152650 |
| 3255945 | 2 | 121.4750670279 | 31.1531077769 | 357 | 2 | 10 | 7.1 | TDD | 391 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3258614 | 9 | 121.4657712012 | 31.1530325014 | 167 | 7 | 2 | 26.3 | FDD | 665 | n1 | 152650 | 30M | 4T4R | 26 | 152650 |
| 3273468 | 6 | 121.4702338107 | 31.1519650754 | 241 | 5 | 11 | 2.4 | TDD | 319 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3275446 | 1 | 121.4703134676 | 31.1456781332 | 1 | 13 | 1 | 12.5 | TDD | 65 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3276783 | 12 | 121.4662778603 | 31.1541426247 | 71 | 7 | 5 | 3.4 | FDD | 793 | n1 | 152650 | 30M | 4T4R | 20 | 152650 |

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
| 2024-09-20 22:21:30.740 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.762 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:30.864 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.864 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.630 | NREventA2 | measId:1;ServCellPCI:447;Se... |
| 2024-09-20 22:21:34.772 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:34.979 | NREventA5 | measId:3;ServCellPCI:447;Se... |
| 2024-09-20 22:21:35.023 | NRHandoverAttempt | SourcePCI:447;SourceNR-ARFC... |
| 2024-09-20 22:21:35.050 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.062 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:35.210 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.210 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3275446 | 1 | 17.7438 | 19.2923 | -117.1628 | 6.9902 | 100.8053 | 0.0044 | 0.0106 |
| 2024_09_20 22:00 | 3255945 | 2 | 11.1033 | 10.7716 | -116.7932 | 16.8355 | 101.0722 | 0.0046 | 0.0152 |
| 2024_09_20 22:00 | 3210597 | 3 | 7.9015 | 11.6737 | -116.2258 | 14.9827 | 98.0986 | 0.0095 | 0.0083 |
| 2024_09_20 22:00 | 3221599 | 4 | 12.7299 | 17.8186 | -117.8046 | 11.4702 | 168.8685 | 0.0060 | 0.0000 |
| 2024_09_20 22:00 | 3243392 | 5 | 14.2902 | 12.0787 | -116.7682 | 16.7232 | 162.7237 | 0.0105 | 0.0027 |
| 2024_09_20 22:00 | 3273468 | 6 | 16.6529 | 6.1792 | -114.4947 | 7.3275 | 96.9337 | 0.0050 | 0.0150 |
| 2024_09_20 22:00 | 3240072 | 7 | 8.6003 | 8.9067 | -114.6646 | 4.7450 | 48.9151 | 0.0154 | 0.0124 |
| 2024_09_20 22:00 | 3243255 | 8 | 7.4896 | 8.4062 | -117.5304 | 4.1437 | 23.0387 | 0.0015 | 0.0040 |
| 2024_09_20 22:00 | 3258614 | 9 | 9.2749 | 12.9120 | -117.4302 | 3.6371 | 34.7251 | 0.0050 | 0.0004 |
| 2024_09_20 22:00 | 3244920 | 10 | 9.5439 | 9.6747 | -116.1047 | 4.8986 | 52.3177 | 0.0149 | 0.0007 |
| 2024_09_20 22:00 | 3252685 | 11 | 8.9271 | 11.6867 | -116.3971 | 3.1834 | 20.9181 | 0.0023 | 0.0010 |
| 2024_09_20 22:00 | 3276783 | 12 | 13.7763 | 11.9038 | -117.7615 | 3.0480 | 31.8781 | 0.0121 | 0.0181 |
| 2024_09_20 22:00 | 3215909 | 13 | 5.3381 | 6.5112 | -117.7022 | 4.6108 | 36.0763 | 0.0046 | 0.0098 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414178_3CF8B0DB | 152650 | 793 | -90.3 | 152650 | 881 | -96.3 | 152650 | 87 | -102.7 | 152650 | 665 |
| MR_1774414178_F3828300 | 504990 | 65 | -96.6 | 504990 | 244 | -97.2 | 504990 | 319 | -98.4 | 504990 | 391 |
| MR_1774414178_D9FEFEE0 | 152650 | 793 | -91.9 | 152650 | 881 | -95.7 | 152650 | 87 | -103.1 | 152650 | 665 |
| MR_1774414178_FE12350B | 152650 | 793 | -93.0 | 152650 | 881 | -98.7 | 152650 | 87 | -102.3 | 152650 | 665 |
| MR_1774414178_C47E841A | 504990 | 65 | -95.1 | 504990 | 244 | -95.8 | 504990 | 319 | -96.0 | 504990 | 391 |
| MR_1774414178_AC843C2D | 152650 | 793 | -91.4 | 152650 | 881 | -95.7 | 152650 | 87 | -102.3 | 152650 | 665 |
| MR_1774414178_A6D21546 | 504990 | 65 | -94.1 | 504990 | 244 | -94.6 | 504990 | 319 | -98.8 | 504990 | 391 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 51: `2e3d9609-f71...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `2e3d9609-f71f-4344-b2e7-ca6620fa1224` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[51] topology](images/test_0051.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3279552_1
- `C2`: Check test server and transmission issues
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3273372_3
- `C4`: Increase transmission power for 3273372_3
- `C5`: Decrease A3 Offset threshold for 3273372_3
- `C6`: Insufficient data; more data is needed for judgment.
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3279552_1
- `C8`: Press down the tilt angle  of 3273372_3 by 4 degrees
- `C9`: Increase A3 Offset threshold for 3279552_1
- `C10`: Increase transmission power for 3279552_1
- `C11`: Add neighbor relationship between 3279552_1 and 3273372_3
- `C12`: Decrease transmission power for 3273372_3
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3279552_1
- `C14`: Lift the tilt angle of 3279552_1 by 3 degrees
- `C15`: Decrease A3 Offset threshold for 3279552_1
- `C16`: Adjust the azimuth of 3279552_1 by 45 degrees
- `C17`: Adjust the azimuth of 3273372_3 by 50 degrees
- `C18`: Increase A3 Offset threshold for 3273372_3
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3273372_3
- `C20`: Add neighbor relationship between 3264479_2 and 3273372_3
- `C21`: Lift the tilt angle  of 3273372_3 by 4 degrees
- `C22`: Press down the tilt angle of 3279552_1 by 3 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.805 | MS1 | 121.4656744859 | 31.1446276358 | 474 | 504990 | -86.81 | 13.92 | 570.86 | 0.10 | 2.76 | 1597 |
| 2024-09-20 22:21:32.828 | MS1 | 121.4656585604 | 31.1446196541 | 474 | 504990 | -86.42 | 16.69 | 487.09 | 0.00 | 2.21 | 1580 |
| 2024-09-20 22:21:33.291 | MS1 | 121.4656746936 | 31.1446326848 | 474 | 504990 | -86.68 | 14.60 | 361.52 | 0.02 | 2.23 | 1586 |
| 2024-09-20 22:21:34.500 | MS1 | 121.4656613512 | 31.1446377937 | 474 | 504990 | -90.94 | 12.20 | 63.08 | 0.66 | 2.91 | 534 |
| 2024-09-20 22:21:35.913 | MS1 | 121.4656717771 | 31.1446309511 | 474 | 504990 | -87.04 | 17.55 | 90.16 | 0.63 | 2.92 | 620 |
| 2024-09-20 22:21:36.126 | MS1 | 121.4656640091 | 31.1446378445 | 474 | 504990 | -86.18 | 17.21 | 77.98 | 0.70 | 2.28 | 631 |
| 2024-09-20 22:21:37.241 | MS1 | 121.4656751243 | 31.1446222227 | 474 | 504990 | -91.74 | 9.27 | 75.17 | 0.59 | 2.97 | 545 |
| 2024-09-20 22:21:38.840 | MS1 | 121.4656684590 | 31.1446216897 | 474 | 504990 | -93.70 | 8.34 | 50.59 | 0.66 | 2.34 | 515 |
| 2024-09-20 22:21:39.339 | MS1 | 121.4656606957 | 31.1446181967 | 474 | 504990 | -90.56 | 11.18 | 75.52 | 0.60 | 2.59 | 663 |
| 2024-09-20 22:21:40.325 | MS1 | 121.4656770084 | 31.1446333004 | 474 | 504990 | -90.36 | 10.98 | 311.53 | 0.08 | 2.72 | 1577 |
| 2024-09-20 22:21:41.281 | MS1 | 121.4656595180 | 31.1446362427 | 474 | 504990 | -89.31 | 12.91 | 452.36 | 0.12 | 2.49 | 1584 |
| 2024-09-20 22:21:42.166 | MS1 | 121.4656715025 | 31.1446270856 | 474 | 504990 | -90.27 | 10.68 | 394.45 | 0.18 | 2.10 | 1576 |

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
| 3264479 | 2 | 121.4673002336 | 31.1525175602 | 331 | 8 | 9 | 16.6 | TDD | 164 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3273372 | 3 | 121.4746002841 | 31.1446615741 | 328 | 3 | 9 | 20.2 | TDD | 461 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3278122 | 4 | 121.4646413790 | 31.1519186422 | 239 | 0 | 7 | 49.2 | TDD | 645 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3279552 | 1 | 121.4748026445 | 31.1559279886 | 260 | 2 | 11 | 38.7 | TDD | 474 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:31.019 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.037 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.173 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.173 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.870 | NREventA3 | measId:2;ServCellPCI:636;Se... |
| 2024-09-20 22:21:38.110 | NRHandoverAttempt | SourcePCI:636;SourceNR-ARFC... |
| 2024-09-20 22:21:38.152 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.164 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.285 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.285 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3279552 | 1 | 18.6400 | 8.4447 | -116.1295 | 19.9156 | 92.8577 | 0.0102 | 0.0097 |
| 2024_09_20 22:00 | 3264479 | 2 | 14.0770 | 16.7005 | -115.5296 | 10.6265 | 154.9577 | 0.0123 | 0.0028 |
| 2024_09_20 22:00 | 3273372 | 3 | 5.2991 | 6.0387 | -115.9925 | 6.4486 | 88.5127 | 0.0056 | 0.0106 |
| 2024_09_20 22:00 | 3278122 | 4 | 5.1788 | 5.7650 | -117.7467 | 7.8735 | 94.6608 | 0.0077 | 0.0196 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413797_EECFBA99 | 504990 | 474 | -90.9 | 504990 | 461 | -100.9 | 504990 | 164 | -104.7 | 504990 | 645 |
| MR_1774413797_69F50A82 | 504990 | 474 | -92.3 | 504990 | 461 | -97.1 | 504990 | 164 | -105.3 | 504990 | 645 |
| MR_1774413797_EEC9D8DE | 504990 | 474 | -91.3 | 504990 | 461 | -97.3 | 504990 | 164 | -106.7 | 504990 | 645 |
| MR_1774413797_9247E2F0 | 504990 | 474 | -91.1 | 504990 | 461 | -100.8 | 504990 | 164 | -104.8 | 504990 | 645 |
| MR_1774413797_889C0F94 | 504990 | 474 | -90.1 | 504990 | 461 | -100.6 | 504990 | 164 | -104.8 | 504990 | 645 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 52: `7283e6f7-0f5...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `7283e6f7-0f5a-45da-805e-8d710e5ceaf2` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[52] topology](images/test_0052.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3234041_2 by 5 degrees
- `C2`: Increase transmission power for 3234041_2
- `C3`: Insufficient data; more data is needed for judgment.
- `C4`: Lift the tilt angle  of 3219540_4 by 10 degrees
- `C5`: Decrease A3 Offset threshold for 3234041_2
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3234041_2
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3234041_2
- `C8`: Decrease transmission power for 3234041_2
- `C9`: Decrease transmission power for 3219540_4
- `C10`: Check test server and transmission issues
- `C11`: Press down the tilt angle of 3234041_2 by 5 degrees
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3219540_4
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3219540_4
- `C14`: Add neighbor relationship between 3220537_1 and 3219540_4
- `C15`: Adjust the azimuth of 3234041_2 by 18 degrees
- `C16`: Press down the tilt angle  of 3219540_4 by 10 degrees
- `C17`: Add neighbor relationship between 3234041_2 and 3219540_4
- `C18`: Adjust the azimuth of 3219540_4 by 50 degrees
- `C19`: Increase transmission power for 3219540_4
- `C20`: Decrease A3 Offset threshold for 3219540_4
- `C21`: Increase A3 Offset threshold for 3219540_4
- `C22`: Increase A3 Offset threshold for 3234041_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.909 | MS1 | 121.4656682254 | 31.1446210411 | 276 | 504990 | -87.34 | 17.46 | 505.66 | 0.10 | 2.95 | 1593 |
| 2024-09-20 22:21:32.785 | MS1 | 121.4656774515 | 31.1446346345 | 276 | 504990 | -88.62 | 15.75 | 557.81 | 0.07 | 2.32 | 1569 |
| 2024-09-20 22:21:33.506 | MS1 | 121.4656595303 | 31.1446378138 | 276 | 504990 | -87.62 | 12.35 | 459.83 | 0.12 | 2.56 | 1575 |
| 2024-09-20 22:21:34.174 | MS1 | 121.4656641873 | 31.1446319158 | 276 | 504990 | -91.36 | 13.58 | 76.32 | 0.65 | 2.38 | 636 |
| 2024-09-20 22:21:35.996 | MS1 | 121.4656583056 | 31.1446375057 | 276 | 504990 | -88.44 | 17.89 | 48.81 | 0.53 | 2.59 | 536 |
| 2024-09-20 22:21:36.375 | MS1 | 121.4656667488 | 31.1446326679 | 276 | 504990 | -85.58 | 12.40 | 73.97 | 0.55 | 2.81 | 665 |
| 2024-09-20 22:21:37.622 | MS1 | 121.4656716813 | 31.1446235259 | 276 | 504990 | -89.84 | 10.57 | 54.12 | 0.53 | 2.33 | 662 |
| 2024-09-20 22:21:38.965 | MS1 | 121.4656604170 | 31.1446347986 | 276 | 504990 | -92.55 | 10.60 | 80.47 | 0.69 | 2.42 | 546 |
| 2024-09-20 22:21:39.142 | MS1 | 121.4656684075 | 31.1446230294 | 276 | 504990 | -89.69 | 10.72 | 80.30 | 0.66 | 2.41 | 534 |
| 2024-09-20 22:21:40.135 | MS1 | 121.4656778145 | 31.1446191432 | 276 | 504990 | -93.52 | 8.99 | 555.29 | 0.06 | 2.80 | 1567 |
| 2024-09-20 22:21:41.316 | MS1 | 121.4656654995 | 31.1446332995 | 276 | 504990 | -91.41 | 8.28 | 444.04 | 0.08 | 2.37 | 1590 |
| 2024-09-20 22:21:42.210 | MS1 | 121.4656706788 | 31.1446304373 | 276 | 504990 | -93.37 | 10.46 | 540.09 | 0.13 | 2.50 | 1567 |

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
| 3219540 | 4 | 121.4724490089 | 31.1473401565 | 306 | 10 | 12 | 25.4 | TDD | 159 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3220537 | 1 | 121.4700946477 | 31.1456582601 | 79 | 13 | 6 | 17.0 | TDD | 667 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3234041 | 2 | 121.4714381356 | 31.1540127707 | 190 | 3 | 5 | 32.7 | TDD | 276 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3245607 | 3 | 121.4660254009 | 31.1451684470 | 173 | 0 | 8 | 49.6 | TDD | 61 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |

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
| 2024-09-20 22:21:31.009 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.030 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.132 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.132 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.892 | NREventA3 | measId:2;ServCellPCI:944;Se... |
| 2024-09-20 22:21:38.132 | NRHandoverAttempt | SourcePCI:944;SourceNR-ARFC... |
| 2024-09-20 22:21:38.167 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.181 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.329 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.329 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3220537 | 1 | 15.5432 | 19.1509 | -116.0912 | 5.0643 | 117.1896 | 0.0011 | 0.0180 |
| 2024_09_20 22:00 | 3234041 | 2 | 10.6927 | 16.0621 | -116.7282 | 11.6992 | 104.3510 | 0.0099 | 0.0187 |
| 2024_09_20 22:00 | 3245607 | 3 | 12.8027 | 5.6553 | -115.0206 | 6.8338 | 130.8183 | 0.0081 | 0.0114 |
| 2024_09_20 22:00 | 3219540 | 4 | 12.6533 | 10.7762 | -117.5034 | 9.3994 | 169.4576 | 0.0110 | 0.0134 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416111_439B292B | 504990 | 276 | -91.2 | 504990 | 159 | -90.6 | 504990 | 667 | -102.6 | 504990 | 61 |
| MR_1774416111_C0465D92 | 504990 | 276 | -89.7 | 504990 | 159 | -91.2 | 504990 | 667 | -105.1 | 504990 | 61 |
| MR_1774416111_7393A5C1 | 504990 | 276 | -89.6 | 504990 | 159 | -92.9 | 504990 | 667 | -105.2 | 504990 | 61 |
| MR_1774416111_BBB11331 | 504990 | 276 | -92.0 | 504990 | 159 | -90.4 | 504990 | 667 | -104.1 | 504990 | 61 |
| MR_1774416111_29FFFC13 | 504990 | 276 | -92.0 | 504990 | 159 | -90.8 | 504990 | 667 | -102.4 | 504990 | 61 |
| MR_1774416111_1E3B7350 | 504990 | 276 | -91.2 | 504990 | 159 | -91.1 | 504990 | 667 | -104.8 | 504990 | 61 |
| MR_1774416111_08AA98DE | 504990 | 276 | -93.0 | 504990 | 159 | -92.1 | 504990 | 667 | -105.6 | 504990 | 61 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 53: `e9d5b45b-6be...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `e9d5b45b-6be6-432d-8289-36892bf73426` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[53] topology](images/test_0053.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3241680_3
- `C2`: Lift the tilt angle  of 3279360_1 by 10 degrees
- `C3`: Press down the tilt angle of 3241680_3 by 10 degrees
- `C4`: Check test server and transmission issues
- `C5`: Increase transmission power for 3241680_3
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3279360_1
- `C7`: Press down the tilt angle  of 3279360_1 by 10 degrees
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3241680_3
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3241680_3
- `C10`: Adjust the azimuth of 3279360_1 by 2 degrees
- `C11`: Decrease transmission power for 3279360_1
- `C12`: Decrease A3 Offset threshold for 3279360_1
- `C13`: Adjust the azimuth of 3241680_3 by 50 degrees
- `C14`: Decrease transmission power for 3241680_3
- `C15`: Lift the tilt angle of 3241680_3 by 10 degrees
- `C16`: Increase transmission power for 3279360_1
- `C17`: Increase A3 Offset threshold for 3279360_1
- `C18`: Add neighbor relationship between 3274505_2 and 3279360_1
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3279360_1
- `C20`: Insufficient data; more data is needed for judgment.
- `C21`: Add neighbor relationship between 3241680_3 and 3279360_1
- `C22`: Decrease A3 Offset threshold for 3241680_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.163 | MS1 | 121.4656727244 | 31.1446332398 | 22 | 504990 | -89.52 | 14.57 | 323.88 | 0.14 | 2.99 | 1566 |
| 2024-09-20 22:21:32.655 | MS1 | 121.4656769253 | 31.1446256268 | 22 | 504990 | -86.43 | 17.17 | 374.93 | 0.18 | 2.62 | 1597 |
| 2024-09-20 22:21:33.245 | MS1 | 121.4656679123 | 31.1446274263 | 22 | 504990 | -88.57 | 12.54 | 584.57 | 0.06 | 2.16 | 1587 |
| 2024-09-20 22:21:34.127 | MS1 | 121.4656650540 | 31.1446244668 | 22 | 504990 | -85.90 | 12.89 | 67.59 | 0.10 | 2.07 | 390 |
| 2024-09-20 22:21:35.281 | MS1 | 121.4656726526 | 31.1446233908 | 22 | 504990 | -86.71 | 12.29 | 84.85 | 0.06 | 2.28 | 461 |
| 2024-09-20 22:21:36.914 | MS1 | 121.4656645004 | 31.1446223899 | 22 | 504990 | -87.58 | 16.74 | 104.95 | 0.06 | 2.50 | 301 |
| 2024-09-20 22:21:37.561 | MS1 | 121.4656619129 | 31.1446283283 | 22 | 504990 | -93.28 | 7.59 | 91.01 | 0.19 | 2.65 | 420 |
| 2024-09-20 22:21:38.147 | MS1 | 121.4656620295 | 31.1446288619 | 22 | 504990 | -92.46 | 10.39 | 74.02 | 0.11 | 2.45 | 454 |
| 2024-09-20 22:21:39.782 | MS1 | 121.4656698600 | 31.1446272296 | 22 | 504990 | -90.49 | 11.07 | 77.18 | 0.10 | 2.56 | 462 |
| 2024-09-20 22:21:40.825 | MS1 | 121.4656602313 | 31.1446280445 | 22 | 504990 | -93.85 | 10.15 | 496.15 | 0.19 | 2.31 | 1597 |
| 2024-09-20 22:21:41.145 | MS1 | 121.4656694674 | 31.1446256178 | 22 | 504990 | -93.75 | 8.44 | 479.78 | 0.11 | 2.31 | 1586 |
| 2024-09-20 22:21:42.790 | MS1 | 121.4656776900 | 31.1446342666 | 22 | 504990 | -90.29 | 12.74 | 538.09 | 0.19 | 2.12 | 1566 |

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
| 3215233 | 4 | 121.4645285143 | 31.1530316919 | 221 | 1 | 4 | 28.5 | TDD | 386 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3241680 | 3 | 121.4748536975 | 31.1488204330 | 331 | 8 | 2 | 33.2 | TDD | 22 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3274505 | 2 | 121.4731952963 | 31.1442343701 | 25 | 12 | 8 | 18.7 | TDD | 7 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3279360 | 1 | 121.4684917213 | 31.1475738437 | 217 | 14 | 9 | 40.2 | TDD | 562 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |

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
| 2024-09-20 22:21:30.988 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.009 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.135 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.135 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.828 | NREventA3 | measId:2;ServCellPCI:159;Se... |
| 2024-09-20 22:21:38.068 | NRHandoverAttempt | SourcePCI:159;SourceNR-ARFC... |
| 2024-09-20 22:21:38.102 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.113 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.247 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.247 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3279360 | 1 | 19.7466 | 7.7344 | -115.0119 | 10.8939 | 172.3154 | 0.0055 | 0.0095 |
| 2024_09_20 22:00 | 3274505 | 2 | 14.3921 | 11.0178 | -117.1312 | 14.4520 | 170.8313 | 0.0084 | 0.0054 |
| 2024_09_20 22:00 | 3241680 | 3 | 18.4429 | 8.7643 | -117.1905 | 19.6920 | 126.9031 | 0.0193 | 0.0151 |
| 2024_09_20 22:00 | 3215233 | 4 | 7.1626 | 15.6651 | -116.8532 | 18.4176 | 121.1488 | 0.0168 | 0.0011 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413911_A80B577F | 504990 | 22 | -85.4 | 504990 | 562 | -91.8 | 504990 | 7 | -98.1 | 504990 | 386 |
| MR_1774413911_261BB503 | 504990 | 22 | -84.4 | 504990 | 562 | -90.9 | 504990 | 7 | -98.4 | 504990 | 386 |
| MR_1774413911_6CF4D236 | 504990 | 22 | -84.7 | 504990 | 562 | -88.8 | 504990 | 7 | -98.6 | 504990 | 386 |
| MR_1774413911_A91CF981 | 504990 | 22 | -86.8 | 504990 | 562 | -90.2 | 504990 | 7 | -99.0 | 504990 | 386 |
| MR_1774413911_5E715BCF | 504990 | 22 | -86.4 | 504990 | 562 | -90.2 | 504990 | 7 | -99.8 | 504990 | 386 |
| MR_1774413911_1C929047 | 504990 | 22 | -87.8 | 504990 | 562 | -88.5 | 504990 | 7 | -98.1 | 504990 | 386 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 54: `07fb0741-dbe...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `07fb0741-dbe8-488b-a5a3-2f51e20533ea` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[54] topology](images/test_0054.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3275998_4
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3235122_3
- `C3`: Press down the tilt angle of 3235122_3 by 5 degrees
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3275998_4
- `C5`: Press down the tilt angle  of 3275998_4 by 6 degrees
- `C6`: Add neighbor relationship between 3269731_8 and 3275998_4
- `C7`: Add neighbor relationship between 3235122_3 and 3275998_4
- `C8`: Check test server and transmission issues
- `C9`: Increase A3 Offset threshold for 3275998_4
- `C10`: Lift the tilt angle of 3235122_3 by 5 degrees
- `C11`: Increase transmission power for 3275998_4
- `C12`: Decrease transmission power for 3275998_4
- `C13`: Decrease transmission power for 3235122_3
- `C14`: Lift the tilt angle  of 3275998_4 by 6 degrees
- `C15`: Increase A3 Offset threshold for 3235122_3
- `C16`: Adjust the azimuth of 3275998_4 by 40 degrees
- `C17`: Decrease A3 Offset threshold for 3235122_3
- `C18`: Adjust the azimuth of 3235122_3 by 11 degrees
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3275998_4
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3235122_3
- `C21`: Insufficient data; more data is needed for judgment.
- `C22`: Increase transmission power for 3235122_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.856 | MS1 | 121.4656674332 | 31.1446270296 | 387 | 504990 | -94.00 | 13.52 | 378.50 | 0.20 | 2.61 | 1571 |
| 2024-09-20 22:21:32.293 | MS1 | 121.4656757021 | 31.1446185514 | 402 | 504990 | -93.57 | 12.81 | 568.01 | 0.15 | 2.48 | 1583 |
| 2024-09-20 22:21:33.147 | MS1 | 121.4656715184 | 31.1446339617 | 797 | 504990 | -95.26 | 11.90 | 390.43 | 0.18 | 2.94 | 1580 |
| 2024-09-20 22:21:34.764 | MS1 | 121.4656758705 | 31.1446321807 | 238 | 152650 | -91.96 | 5.89 | 81.87 | 0.10 | 1.64 | 984 |
| 2024-09-20 22:21:35.203 | MS1 | 121.4656711883 | 31.1446296851 | 791 | 152650 | -93.67 | 5.20 | 58.87 | 0.01 | 1.73 | 975 |
| 2024-09-20 22:21:36.123 | MS1 | 121.4656742694 | 31.1446354391 | 267 | 152650 | -94.26 | 4.27 | 93.79 | 0.06 | 1.79 | 987 |
| 2024-09-20 22:21:37.429 | MS1 | 121.4656660627 | 31.1446313354 | 504 | 152650 | -87.60 | 6.57 | 75.46 | 0.09 | 1.51 | 922 |
| 2024-09-20 22:21:38.462 | MS1 | 121.4656749758 | 31.1446208515 | 238 | 152650 | -95.14 | 4.97 | 71.39 | 0.03 | 1.68 | 991 |
| 2024-09-20 22:21:39.853 | MS1 | 121.4656637995 | 31.1446248380 | 791 | 152650 | -89.96 | 3.09 | 93.75 | 0.10 | 1.53 | 951 |
| 2024-09-20 22:21:40.166 | MS1 | 121.4656773386 | 31.1446323962 | 267 | 152650 | -94.05 | 5.33 | 83.89 | 0.05 | 2.09 | 1574 |
| 2024-09-20 22:21:41.104 | MS1 | 121.4656738725 | 31.1446327250 | 504 | 152650 | -89.30 | 6.10 | 96.83 | 0.13 | 2.76 | 1564 |
| 2024-09-20 22:21:42.957 | MS1 | 121.4656677275 | 31.1446306886 | 238 | 152650 | -87.25 | 3.17 | 79.23 | 0.09 | 2.15 | 1580 |

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
| 3215692 | 12 | 121.4733059010 | 31.1533927111 | 350 | 10 | 12 | 4.4 | FDD | 504 | n1 | 152650 | 30M | 4T4R | 29 | 152650 |
| 3226798 | 11 | 121.4752564977 | 31.1496505184 | 101 | 6 | 6 | 6.6 | FDD | 791 | n1 | 152650 | 30M | 4T4R | 25 | 152650 |
| 3233283 | 7 | 121.4732404308 | 31.1475147721 | 208 | 1 | 5 | 2.8 | FDD | 546 | n1 | 152650 | 30M | 4T4R | 12 | 152650 |
| 3234690 | 5 | 121.4652895998 | 31.1453775527 | 243 | 0 | 9 | 21.1 | TDD | 402 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3235122 | 3 | 121.4672652572 | 31.1507172584 | 204 | 4 | 12 | 8.4 | TDD | 387 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3240225 | 6 | 121.4689209524 | 31.1524334616 | 160 | 8 | 6 | 8.6 | TDD | 797 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3254296 | 1 | 121.4757721710 | 31.1468520703 | 308 | 13 | 1 | 24.8 | TDD | 193 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3257969 | 9 | 121.4758366823 | 31.1453628838 | 177 | 11 | 2 | 8.6 | FDD | 238 | n1 | 152650 | 30M | 4T4R | 27 | 152650 |
| 3264120 | 2 | 121.4720363242 | 31.1555945846 | 6 | 8 | 11 | 13.8 | TDD | 737 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3269731 | 8 | 121.4731869450 | 31.1552639820 | 86 | 6 | 11 | 2.3 | FDD | 267 | n1 | 152650 | 30M | 4T4R | 22 | 152650 |
| 3270114 | 10 | 121.4645797637 | 31.1455896366 | 12 | 12 | 6 | 9.4 | FDD | 20 | n1 | 152650 | 30M | 4T4R | 25 | 152650 |
| 3272657 | 13 | 121.4641191324 | 31.1539130582 | 338 | 15 | 10 | 18.6 | FDD | 730 | n1 | 152650 | 30M | 4T4R | 15 | 152650 |
| 3275998 | 4 | 121.4663756258 | 31.1509125888 | 145 | 4 | 11 | 24.2 | TDD | 554 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:30.773 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.795 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:30.941 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.941 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.650 | NREventA2 | measId:1;ServCellPCI:15;Ser... |
| 2024-09-20 22:21:34.752 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:34.978 | NREventA5 | measId:3;ServCellPCI:15;Ser... |
| 2024-09-20 22:21:35.029 | NRHandoverAttempt | SourcePCI:15;SourceNR-ARFCN... |
| 2024-09-20 22:21:35.050 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.061 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:35.209 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.209 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3254296 | 1 | 5.3524 | 13.2509 | -114.5990 | 12.2802 | 125.4104 | 0.0054 | 0.0018 |
| 2024_09_20 22:00 | 3264120 | 2 | 6.3056 | 13.1625 | -115.1272 | 15.4991 | 136.6270 | 0.0189 | 0.0062 |
| 2024_09_20 22:00 | 3235122 | 3 | 17.9604 | 12.8502 | -115.4109 | 18.4527 | 198.9616 | 0.0094 | 0.0027 |
| 2024_09_20 22:00 | 3275998 | 4 | 17.0151 | 9.9808 | -117.0828 | 10.8657 | 178.6217 | 0.0054 | 0.0159 |
| 2024_09_20 22:00 | 3234690 | 5 | 8.0515 | 17.6960 | -115.0733 | 8.6816 | 129.7715 | 0.0044 | 0.0009 |
| 2024_09_20 22:00 | 3240225 | 6 | 19.7571 | 15.1729 | -117.3711 | 13.2323 | 114.4026 | 0.0124 | 0.0020 |
| 2024_09_20 22:00 | 3233283 | 7 | 19.3060 | 13.8961 | -116.7212 | 3.2053 | 47.1724 | 0.0058 | 0.0200 |
| 2024_09_20 22:00 | 3269731 | 8 | 14.7754 | 19.0773 | -114.6823 | 4.6561 | 52.4153 | 0.0065 | 0.0127 |
| 2024_09_20 22:00 | 3257969 | 9 | 15.3590 | 17.2771 | -116.8619 | 3.6949 | 53.1277 | 0.0020 | 0.0037 |
| 2024_09_20 22:00 | 3270114 | 10 | 13.7482 | 17.7292 | -114.4342 | 3.4581 | 43.7291 | 0.0198 | 0.0004 |
| 2024_09_20 22:00 | 3226798 | 11 | 6.9018 | 5.7110 | -116.3617 | 4.3687 | 53.5126 | 0.0031 | 0.0129 |
| 2024_09_20 22:00 | 3215692 | 12 | 5.5731 | 19.8299 | -117.3808 | 3.6686 | 40.1717 | 0.0149 | 0.0069 |
| 2024_09_20 22:00 | 3272657 | 13 | 8.5251 | 16.2253 | -117.2596 | 3.8753 | 55.5569 | 0.0170 | 0.0029 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415116_7CAD0BD5 | 504990 | 797 | -96.9 | 504990 | 554 | -97.0 | 504990 | 193 | -97.4 | 504990 | 737 |
| MR_1774415116_74748B77 | 152650 | 238 | -93.7 | 152650 | 20 | -97.2 | 152650 | 546 | -100.7 | 152650 | 730 |
| MR_1774415116_F119B7EF | 152650 | 238 | -90.1 | 152650 | 20 | -96.7 | 152650 | 546 | -100.1 | 152650 | 730 |
| MR_1774415116_1E3F3E0F | 504990 | 797 | -96.0 | 504990 | 554 | -97.2 | 504990 | 193 | -99.6 | 504990 | 737 |
| MR_1774415116_3E6CD6EB | 152650 | 238 | -93.0 | 152650 | 20 | -96.3 | 152650 | 546 | -101.2 | 152650 | 730 |
| MR_1774415116_664B97D1 | 152650 | 238 | -90.9 | 152650 | 20 | -99.4 | 152650 | 546 | -100.6 | 152650 | 730 |
| MR_1774415116_76B6A10D | 152650 | 238 | -91.1 | 152650 | 20 | -98.4 | 152650 | 546 | -99.5 | 152650 | 730 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 55: `eb31cd59-dac...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `eb31cd59-dac8-42a0-96ef-3aae0b056a09` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[55] topology](images/test_0055.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3274147_3 by 5 degrees
- `C2`: Press down the tilt angle of 3252034_2 by 4 degrees
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3274147_3
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3252034_2
- `C5`: Decrease A3 Offset threshold for 3274147_3
- `C6`: Adjust the azimuth of 3274147_3 by 50 degrees
- `C7`: Decrease transmission power for 3252034_2
- `C8`: Add neighbor relationship between 3252034_2 and 3274147_3
- `C9`: Increase transmission power for 3252034_2
- `C10`: Lift the tilt angle  of 3274147_3 by 5 degrees
- `C11`: Decrease A3 Offset threshold for 3252034_2
- `C12`: Lift the tilt angle of 3252034_2 by 4 degrees
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3274147_3
- `C14`: Increase A3 Offset threshold for 3274147_3
- `C15`: Check test server and transmission issues
- `C16`: Increase transmission power for 3274147_3
- `C17`: Decrease transmission power for 3274147_3
- `C18`: Insufficient data; more data is needed for judgment.
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3252034_2
- `C20`: Add neighbor relationship between 3244778_4 and 3274147_3
- `C21`: Adjust the azimuth of 3252034_2 by 2 degrees
- `C22`: Increase A3 Offset threshold for 3252034_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.190 | MS1 | 121.4656655588 | 31.1446286887 | 970 | 504990 | -91.23 | 12.96 | 595.88 | 0.08 | 2.02 | 1569 |
| 2024-09-20 22:21:32.939 | MS1 | 121.4656705706 | 31.1446239666 | 970 | 504990 | -89.61 | 12.65 | 400.46 | 0.02 | 2.03 | 1585 |
| 2024-09-20 22:21:33.470 | MS1 | 121.4656676159 | 31.1446210994 | 970 | 504990 | -90.27 | 17.83 | 503.39 | 0.05 | 2.93 | 1565 |
| 2024-09-20 22:21:34.981 | MS1 | 121.4656745399 | 31.1446306806 | 970 | 504990 | -86.70 | 14.27 | 102.84 | 0.58 | 2.88 | 544 |
| 2024-09-20 22:21:35.654 | MS1 | 121.4656702152 | 31.1446306703 | 970 | 504990 | -86.78 | 17.25 | 75.21 | 0.65 | 2.87 | 621 |
| 2024-09-20 22:21:36.920 | MS1 | 121.4656713996 | 31.1446316317 | 970 | 504990 | -92.00 | 15.00 | 80.07 | 0.54 | 2.69 | 592 |
| 2024-09-20 22:21:37.509 | MS1 | 121.4656682977 | 31.1446231350 | 970 | 504990 | -92.72 | 8.72 | 86.39 | 0.63 | 2.05 | 587 |
| 2024-09-20 22:21:38.269 | MS1 | 121.4656679708 | 31.1446325030 | 970 | 504990 | -92.90 | 11.95 | 94.92 | 0.55 | 2.51 | 642 |
| 2024-09-20 22:21:39.973 | MS1 | 121.4656740045 | 31.1446223557 | 970 | 504990 | -93.72 | 11.60 | 59.23 | 0.59 | 2.22 | 693 |
| 2024-09-20 22:21:40.316 | MS1 | 121.4656609547 | 31.1446305402 | 970 | 504990 | -93.35 | 8.32 | 593.65 | 0.14 | 2.80 | 1590 |
| 2024-09-20 22:21:41.939 | MS1 | 121.4656612696 | 31.1446240140 | 970 | 504990 | -89.63 | 7.38 | 523.31 | 0.17 | 2.75 | 1600 |
| 2024-09-20 22:21:42.961 | MS1 | 121.4656653875 | 31.1446261529 | 970 | 504990 | -91.61 | 9.61 | 415.67 | 0.12 | 2.88 | 1597 |

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
| 3214255 | 1 | 121.4749271938 | 31.1444760899 | 5 | 4 | 12 | 43.5 | TDD | 913 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3244778 | 4 | 121.4685605565 | 31.1448669566 | 87 | 13 | 5 | 22.7 | TDD | 106 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3252034 | 2 | 121.4709999143 | 31.1521507157 | 209 | 2 | 4 | 39.7 | TDD | 970 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3274147 | 3 | 121.4740374293 | 31.1453106905 | 7 | 3 | 6 | 25.1 | TDD | 1006 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |

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
| 2024-09-20 22:21:31.456 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.475 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.581 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.581 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.347 | NREventA3 | measId:2;ServCellPCI:658;Se... |
| 2024-09-20 22:21:38.587 | NRHandoverAttempt | SourcePCI:658;SourceNR-ARFC... |
| 2024-09-20 22:21:38.627 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.639 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.775 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.775 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3214255 | 1 | 15.6118 | 5.3601 | -115.6927 | 14.6541 | 174.0970 | 0.0082 | 0.0166 |
| 2024_09_20 22:00 | 3252034 | 2 | 19.2956 | 19.0086 | -117.9070 | 17.4618 | 132.8048 | 0.0134 | 0.0158 |
| 2024_09_20 22:00 | 3274147 | 3 | 5.4912 | 16.5510 | -117.5137 | 16.3470 | 161.0133 | 0.0191 | 0.0001 |
| 2024_09_20 22:00 | 3244778 | 4 | 18.5978 | 17.1565 | -117.9869 | 6.9969 | 121.1139 | 0.0184 | 0.0154 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413632_B999777F | 504990 | 970 | -85.8 | 504990 | 1006 | -88.1 | 504990 | 106 | -97.4 | 504990 | 913 |
| MR_1774413632_079C248D | 504990 | 970 | -86.3 | 504990 | 1006 | -88.7 | 504990 | 106 | -100.3 | 504990 | 913 |
| MR_1774413632_318CD757 | 504990 | 970 | -85.4 | 504990 | 1006 | -89.4 | 504990 | 106 | -100.4 | 504990 | 913 |
| MR_1774413632_01678CAE | 504990 | 970 | -84.9 | 504990 | 1006 | -90.5 | 504990 | 106 | -98.4 | 504990 | 913 |
| MR_1774413632_DE9A6A70 | 504990 | 970 | -86.2 | 504990 | 1006 | -88.9 | 504990 | 106 | -100.7 | 504990 | 913 |
| MR_1774413632_18A1EF8C | 504990 | 970 | -88.7 | 504990 | 1006 | -89.3 | 504990 | 106 | -99.5 | 504990 | 913 |
| MR_1774413632_8D304C4A | 504990 | 970 | -85.2 | 504990 | 1006 | -91.1 | 504990 | 106 | -97.5 | 504990 | 913 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 56: `09a398d6-d9a...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `09a398d6-d9af-4eb6-8cf7-cc0db6cdada9` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[56] topology](images/test_0056.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3259372_4 by 10 degrees
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3259372_4
- `C3`: Add neighbor relationship between 3229055_3 and 3259372_4
- `C4`: Increase A3 Offset threshold for 3259372_4
- `C5`: Decrease A3 Offset threshold for 3229055_3
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3259372_4
- `C7`: Increase A3 Offset threshold for 3229055_3
- `C8`: Lift the tilt angle of 3229055_3 by 10 degrees
- `C9`: Decrease transmission power for 3229055_3
- `C10`: Increase transmission power for 3259372_4
- `C11`: Decrease A3 Offset threshold for 3259372_4
- `C12`: Insufficient data; more data is needed for judgment.
- `C13`: Decrease transmission power for 3259372_4
- `C14`: Press down the tilt angle of 3229055_3 by 10 degrees
- `C15`: Check test server and transmission issues
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3229055_3
- `C17`: Adjust the azimuth of 3259372_4 by 50 degrees
- `C18`: Adjust the azimuth of 3229055_3 by 50 degrees
- `C19`: Lift the tilt angle  of 3259372_4 by 10 degrees
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3229055_3
- `C21`: Add neighbor relationship between 3233618_2 and 3259372_4
- `C22`: Increase transmission power for 3229055_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.836 | MS1 | 121.4656662682 | 31.1446308276 | 886 | 504990 | -87.69 | 13.32 | 489.80 | 0.15 | 2.04 | 1561 |
| 2024-09-20 22:21:32.239 | MS1 | 121.4656728278 | 31.1446186287 | 886 | 504990 | -91.07 | 12.94 | 495.17 | 0.09 | 2.64 | 1589 |
| 2024-09-20 22:21:33.434 | MS1 | 121.4656598462 | 31.1446354134 | 886 | 504990 | -91.00 | 17.06 | 473.36 | 0.14 | 2.44 | 1562 |
| 2024-09-20 22:21:34.311 | MS1 | 121.4656672335 | 31.1446346417 | 886 | 504990 | -87.39 | 13.42 | 54.41 | 0.12 | 2.12 | 474 |
| 2024-09-20 22:21:35.892 | MS1 | 121.4656769359 | 31.1446302850 | 886 | 504990 | -89.36 | 16.69 | 91.17 | 0.19 | 2.47 | 469 |
| 2024-09-20 22:21:36.576 | MS1 | 121.4656742814 | 31.1446348973 | 886 | 504990 | -85.30 | 17.24 | 76.54 | 0.03 | 2.73 | 397 |
| 2024-09-20 22:21:37.459 | MS1 | 121.4656778358 | 31.1446318634 | 886 | 504990 | -89.76 | 7.37 | 79.82 | 0.17 | 2.08 | 345 |
| 2024-09-20 22:21:38.207 | MS1 | 121.4656744308 | 31.1446354896 | 886 | 504990 | -92.27 | 12.81 | 75.34 | 0.13 | 2.22 | 355 |
| 2024-09-20 22:21:39.129 | MS1 | 121.4656647870 | 31.1446329569 | 886 | 504990 | -91.70 | 10.77 | 99.15 | 0.20 | 2.99 | 336 |
| 2024-09-20 22:21:40.882 | MS1 | 121.4656714899 | 31.1446340829 | 886 | 504990 | -92.98 | 9.34 | 439.48 | 0.10 | 2.77 | 1564 |
| 2024-09-20 22:21:41.878 | MS1 | 121.4656755082 | 31.1446231849 | 886 | 504990 | -89.54 | 11.08 | 338.08 | 0.19 | 2.34 | 1587 |
| 2024-09-20 22:21:42.914 | MS1 | 121.4656706454 | 31.1446334220 | 886 | 504990 | -93.58 | 10.12 | 333.70 | 0.18 | 2.38 | 1597 |

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
| 3229055 | 3 | 121.4666707266 | 31.1488136664 | 311 | 12 | 8 | 36.3 | TDD | 886 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3233618 | 2 | 121.4682332440 | 31.1496018254 | 251 | 2 | 5 | 21.0 | TDD | 636 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3250649 | 1 | 121.4743632733 | 31.1493324348 | 354 | 8 | 12 | 26.9 | TDD | 203 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3259372 | 4 | 121.4678372591 | 31.1496114218 | 294 | 11 | 5 | 15.5 | TDD | 807 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

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
| 2024-09-20 22:21:31.071 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.093 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.218 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.218 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.928 | NREventA3 | measId:2;ServCellPCI:892;Se... |
| 2024-09-20 22:21:38.168 | NRHandoverAttempt | SourcePCI:892;SourceNR-ARFC... |
| 2024-09-20 22:21:38.214 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.228 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.375 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.375 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3250649 | 1 | 6.9255 | 7.4536 | -116.6870 | 15.5652 | 181.4416 | 0.0177 | 0.0163 |
| 2024_09_20 22:00 | 3233618 | 2 | 15.8227 | 12.2823 | -117.1885 | 9.0443 | 113.5398 | 0.0116 | 0.0171 |
| 2024_09_20 22:00 | 3229055 | 3 | 12.2011 | 10.7672 | -117.2148 | 17.3270 | 109.2356 | 0.0187 | 0.0192 |
| 2024_09_20 22:00 | 3259372 | 4 | 10.4268 | 18.2292 | -116.8015 | 6.9421 | 192.2576 | 0.0168 | 0.0127 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415606_49D7A560 | 504990 | 886 | -88.0 | 504990 | 807 | -88.9 | 504990 | 636 | -99.9 | 504990 | 203 |
| MR_1774415606_2DBDC1DE | 504990 | 886 | -88.6 | 504990 | 807 | -87.9 | 504990 | 636 | -97.4 | 504990 | 203 |
| MR_1774415606_73DBE7A7 | 504990 | 886 | -89.3 | 504990 | 807 | -89.2 | 504990 | 636 | -98.5 | 504990 | 203 |
| MR_1774415606_6AC501F5 | 504990 | 886 | -87.7 | 504990 | 807 | -88.0 | 504990 | 636 | -96.9 | 504990 | 203 |
| MR_1774415606_EA3F5207 | 504990 | 886 | -88.2 | 504990 | 807 | -89.2 | 504990 | 636 | -100.0 | 504990 | 203 |
| MR_1774415606_F4A528C2 | 504990 | 886 | -86.5 | 504990 | 807 | -88.6 | 504990 | 636 | -97.0 | 504990 | 203 |
| MR_1774415606_EA0B7132 | 504990 | 886 | -85.9 | 504990 | 807 | -87.7 | 504990 | 636 | -99.7 | 504990 | 203 |
| MR_1774415606_6B79FEF5 | 504990 | 886 | -88.6 | 504990 | 807 | -87.7 | 504990 | 636 | -99.4 | 504990 | 203 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 57: `33780221-c9b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `33780221-c9be-4da1-b5c8-1fb5fb87fd7c` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[57] topology](images/test_0057.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3274635_3 and 3243077_2
- `C2`: Press down the tilt angle of 3243075_1 by 10 degrees
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3243075_1
- `C4`: Adjust the azimuth of 3243075_1 by 50 degrees
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3243077_2
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3243075_1
- `C7`: Add neighbor relationship between 3243075_1 and 3243077_2
- `C8`: Adjust the azimuth of 3243077_2 by 50 degrees
- `C9`: Increase transmission power for 3243075_1
- `C10`: Decrease A3 Offset threshold for 3243075_1
- `C11`: Increase A3 Offset threshold for 3243077_2
- `C12`: Increase transmission power for 3243077_2
- `C13`: Lift the tilt angle of 3243075_1 by 10 degrees
- `C14`: Increase A3 Offset threshold for 3243075_1
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3243077_2
- `C16`: Decrease A3 Offset threshold for 3243077_2
- `C17`: Insufficient data; more data is needed for judgment.
- `C18`: Decrease transmission power for 3243077_2
- `C19`: Decrease transmission power for 3243075_1
- `C20`: Press down the tilt angle  of 3243077_2 by 6 degrees
- `C21`: Check test server and transmission issues
- `C22`: Lift the tilt angle  of 3243077_2 by 6 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.191 | MS1 | 121.4656758988 | 31.1446186590 | 882 | 504990 | -80.29 | 14.97 | 553.17 | 0.12 | 2.16 | 1583 |
| 2024-09-20 22:21:32.274 | MS1 | 121.4656752956 | 31.1446327605 | 882 | 504990 | -75.98 | 14.82 | 529.57 | 0.04 | 2.84 | 1582 |
| 2024-09-20 22:21:33.850 | MS1 | 121.4656756346 | 31.1446222375 | 882 | 504990 | -75.27 | 12.13 | 443.96 | 0.11 | 2.90 | 1591 |
| 2024-09-20 22:21:34.640 | MS1 | 121.4656729106 | 31.1446273562 | 882 | 504990 | -90.60 | -2.37 | 41.21 | 0.14 | 1.12 | 1584 |
| 2024-09-20 22:21:35.170 | MS1 | 121.4656655087 | 31.1446308831 | 882 | 504990 | -88.00 | -1.72 | 52.60 | 0.11 | 1.41 | 1561 |
| 2024-09-20 22:21:36.976 | MS1 | 121.4656768420 | 31.1446298600 | 882 | 504990 | -91.19 | -3.95 | 34.00 | 0.18 | 1.04 | 1575 |
| 2024-09-20 22:21:37.111 | MS1 | 121.4656724112 | 31.1446275438 | 882 | 504990 | -84.81 | -1.26 | 64.47 | 0.02 | 1.01 | 1580 |
| 2024-09-20 22:21:38.886 | MS1 | 121.4656627045 | 31.1446332694 | 882 | 504990 | -92.24 | -1.63 | 69.22 | 0.19 | 1.16 | 1600 |
| 2024-09-20 22:21:39.259 | MS1 | 121.4656604313 | 31.1446192649 | 652 | 504990 | -83.90 | 17.98 | 169.90 | 0.12 | 1.27 | 1589 |
| 2024-09-20 22:21:40.862 | MS1 | 121.4656698705 | 31.1446280009 | 652 | 504990 | -76.73 | 13.32 | 394.87 | 0.02 | 2.67 | 1579 |
| 2024-09-20 22:21:41.491 | MS1 | 121.4656623879 | 31.1446354897 | 652 | 504990 | -83.12 | 15.04 | 479.66 | 0.01 | 2.62 | 1571 |
| 2024-09-20 22:21:42.527 | MS1 | 121.4656717948 | 31.1446368800 | 652 | 504990 | -76.37 | 16.54 | 562.58 | 0.03 | 2.43 | 1594 |

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
| 3235561 | 4 | 121.4726893677 | 31.1507269541 | 276 | 1 | 8 | 23.2 | TDD | 135 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3243075 | 1 | 121.4692274271 | 31.1505110430 | 354 | 15 | 1 | 27.3 | TDD | 882 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3243077 | 2 | 121.4724284931 | 31.1492952423 | 0 | 3 | 5 | 43.2 | TDD | 652 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3274635 | 3 | 121.4688994740 | 31.1475105079 | 184 | 10 | 7 | 39.5 | TDD | 594 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |

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
| 2024-09-20 22:21:31.138 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.158 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.292 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.292 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.993 | NREventA3 | measId:2;ServCellPCI:245;Se... |
| 2024-09-20 22:21:38.233 | NRHandoverAttempt | SourcePCI:245;SourceNR-ARFC... |
| 2024-09-20 22:21:38.263 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.274 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.408 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.408 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3243075 | 1 | 19.6956 | 17.1924 | -114.2174 | 16.8077 | 154.1755 | 0.0057 | 0.1189 |
| 2024_09_20 22:00 | 3243077 | 2 | 14.5199 | 6.1491 | -117.1671 | 19.1829 | 100.7094 | 0.0161 | 0.0185 |
| 2024_09_20 22:00 | 3274635 | 3 | 11.7592 | 8.6023 | -116.8264 | 17.3181 | 117.2626 | 0.0141 | 0.0121 |
| 2024_09_20 22:00 | 3235561 | 4 | 9.8304 | 5.1995 | -117.5713 | 13.8448 | 105.9417 | 0.0138 | 0.0128 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415086_25A4BBD5 | 504990 | 652 | -84.5 | 504990 | 882 | -89.3 | 504990 | 594 | -84.4 | 504990 | 135 |
| MR_1774415086_40E388E8 | 504990 | 882 | -88.6 | 504990 | 652 | -84.4 | 504990 | 594 | -87.2 | 504990 | 135 |
| MR_1774415086_57EED9F8 | 504990 | 882 | -91.1 | 504990 | 652 | -84.4 | 504990 | 594 | -87.6 | 504990 | 135 |
| MR_1774415086_436C468E | 504990 | 882 | -91.9 | 504990 | 652 | -84.1 | 504990 | 594 | -84.1 | 504990 | 135 |
| MR_1774415086_407F89C1 | 504990 | 882 | -90.9 | 504990 | 652 | -86.4 | 504990 | 594 | -84.4 | 504990 | 135 |
| MR_1774415086_7B742477 | 504990 | 882 | -90.8 | 504990 | 652 | -86.0 | 504990 | 594 | -87.1 | 504990 | 135 |
| MR_1774415086_573B5947 | 504990 | 882 | -90.1 | 504990 | 652 | -86.8 | 504990 | 594 | -84.2 | 504990 | 135 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 58: `059e81bf-125...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `059e81bf-125a-4500-82c4-9a636ed2f76e` |
| Tag | **multiple-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[58] topology](images/test_0058.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3231091_3 by 2 degrees
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3231091_3
- `C3`: Increase transmission power for 3231091_3
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3250847_4
- `C5`: Press down the tilt angle  of 3250847_4 by 4 degrees
- `C6`: Adjust the azimuth of 3250847_4 by 21 degrees
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3250847_4
- `C8`: Add neighbor relationship between 3231091_3 and 3250847_4
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3231091_3
- `C10`: Add neighbor relationship between 3233188_1 and 3250847_4
- `C11`: Lift the tilt angle  of 3250847_4 by 4 degrees
- `C12`: Check test server and transmission issues
- `C13`: Decrease A3 Offset threshold for 3231091_3
- `C14`: Press down the tilt angle of 3231091_3 by 2 degrees
- `C15`: Decrease transmission power for 3231091_3
- `C16`: Decrease A3 Offset threshold for 3250847_4
- `C17`: Adjust the azimuth of 3231091_3 by 8 degrees
- `C18`: Increase A3 Offset threshold for 3250847_4
- `C19`: Decrease transmission power for 3250847_4
- `C20`: Increase transmission power for 3250847_4
- `C21`: Insufficient data; more data is needed for judgment.
- `C22`: Increase A3 Offset threshold for 3231091_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.308 | MS1 | 121.4656622666 | 31.1446311807 | 998 | 504990 | -76.07 | 15.76 | 392.11 | 0.10 | 2.72 | 1581 |
| 2024-09-20 22:21:32.207 | MS1 | 121.4656676341 | 31.1446222601 | 998 | 504990 | -79.00 | 15.48 | 294.95 | 0.16 | 2.91 | 1569 |
| 2024-09-20 22:21:33.215 | MS1 | 121.4656591237 | 31.1446258242 | 998 | 504990 | -81.49 | 12.92 | 460.90 | 0.09 | 2.99 | 1593 |
| 2024-09-20 22:21:34.336 | MS1 | 121.4656635086 | 31.1446304669 | 998 | 504990 | -94.18 | 0.95 | 36.24 | 0.04 | 1.48 | 1584 |
| 2024-09-20 22:21:35.834 | MS1 | 121.4656743805 | 31.1446231225 | 998 | 504990 | -88.95 | 3.04 | 44.39 | 0.07 | 1.18 | 1575 |
| 2024-09-20 22:21:36.144 | MS1 | 121.4656725941 | 31.1446374899 | 998 | 504990 | -94.99 | 2.19 | 69.06 | 0.06 | 1.18 | 1583 |
| 2024-09-20 22:21:37.900 | MS1 | 121.4656696391 | 31.1446241026 | 998 | 504990 | -89.94 | 2.69 | 53.61 | 0.20 | 1.01 | 1567 |
| 2024-09-20 22:21:38.834 | MS1 | 121.4656613547 | 31.1446266898 | 998 | 504990 | -86.41 | 0.47 | 47.13 | 0.03 | 1.44 | 1567 |
| 2024-09-20 22:21:39.217 | MS1 | 121.4656739060 | 31.1446227767 | 998 | 504990 | -91.26 | 3.54 | 85.12 | 0.07 | 1.35 | 1567 |
| 2024-09-20 22:21:40.488 | MS1 | 121.4656744185 | 31.1446253323 | 998 | 504990 | -84.88 | 13.73 | 574.36 | 0.04 | 2.78 | 1592 |
| 2024-09-20 22:21:41.882 | MS1 | 121.4656655600 | 31.1446356267 | 998 | 504990 | -76.84 | 16.81 | 390.42 | 0.06 | 2.78 | 1561 |
| 2024-09-20 22:21:42.594 | MS1 | 121.4656670814 | 31.1446372107 | 998 | 504990 | -76.32 | 12.71 | 330.67 | 0.17 | 2.08 | 1567 |

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
| 3227747 | 2 | 121.4705572728 | 31.1511226152 | 167 | 6 | 10 | 46.6 | TDD | 802 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3231091 | 3 | 121.4660496560 | 31.1551808812 | 174 | 1 | 10 | 17.1 | TDD | 998 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3233188 | 1 | 121.4740217198 | 31.1492174038 | 222 | 14 | 12 | 16.2 | TDD | 298 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3250847 | 4 | 121.4703039789 | 31.1527514997 | 227 | 2 | 6 | 27.5 | TDD | 231 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |

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
| 2024-09-20 22:21:31.386 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.403 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.515 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.515 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3233188 | 1 | 11.1916 | 10.6040 | -117.3730 | 11.8387 | 171.3951 | 0.0181 | 0.0193 |
| 2024_09_20 22:00 | 3227747 | 2 | 7.1889 | 10.9911 | -114.3618 | 9.0153 | 181.9996 | 0.0167 | 0.0033 |
| 2024_09_20 22:00 | 3231091 | 3 | 13.7504 | 10.2627 | -108.5402 | 16.6724 | 161.8243 | 0.0136 | 0.0134 |
| 2024_09_20 22:00 | 3250847 | 4 | 12.3635 | 19.5098 | -116.1534 | 17.8633 | 139.6948 | 0.0123 | 0.0142 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415910_251DA0A5 | 504990 | 998 | -93.5 | 504990 | 231 | -92.9 | 504990 | 298 | -91.6 | 504990 | 802 |
| MR_1774415910_43B5176D | 504990 | 998 | -93.5 | 504990 | 231 | -93.5 | 504990 | 298 | -92.7 | 504990 | 802 |
| MR_1774415910_84E5B7DC | 504990 | 998 | -95.7 | 504990 | 231 | -91.4 | 504990 | 298 | -93.9 | 504990 | 802 |
| MR_1774415910_DCAC4BF9 | 504990 | 998 | -93.4 | 504990 | 231 | -93.5 | 504990 | 298 | -94.8 | 504990 | 802 |
| MR_1774415910_A0D1E870 | 504990 | 998 | -94.1 | 504990 | 231 | -93.3 | 504990 | 298 | -91.3 | 504990 | 802 |
| MR_1774415910_31236DCC | 504990 | 231 | -92.8 | 504990 | 998 | -92.6 | 504990 | 298 | -92.0 | 504990 | 802 |
| MR_1774415910_DCB0952A | 504990 | 998 | -96.1 | 504990 | 231 | -91.7 | 504990 | 298 | -94.8 | 504990 | 802 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 59: `2c8c8f98-5c3...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `2c8c8f98-5c31-4f15-af64-61c445a37b09` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[59] topology](images/test_0059.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3212907_3 by 6 degrees
- `C2`: Increase A3 Offset threshold for 3277249_1
- `C3`: Decrease A3 Offset threshold for 3212907_3
- `C4`: Decrease transmission power for 3212907_3
- `C5`: Insufficient data; more data is needed for judgment.
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3277249_1
- `C7`: Decrease A3 Offset threshold for 3277249_1
- `C8`: Lift the tilt angle of 3277249_1 by 4 degrees
- `C9`: Add neighbor relationship between 3248381_2 and 3212907_3
- `C10`: Increase transmission power for 3212907_3
- `C11`: Adjust the azimuth of 3277249_1 by 8 degrees
- `C12`: Check test server and transmission issues
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3277249_1
- `C14`: Lift the tilt angle  of 3212907_3 by 6 degrees
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3212907_3
- `C16`: Increase A3 Offset threshold for 3212907_3
- `C17`: Increase transmission power for 3277249_1
- `C18`: Add neighbor relationship between 3277249_1 and 3212907_3
- `C19`: Decrease transmission power for 3277249_1
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3212907_3
- `C21`: Press down the tilt angle of 3277249_1 by 4 degrees
- `C22`: Adjust the azimuth of 3212907_3 by 50 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.544 | MS1 | 121.4656611137 | 31.1446346762 | 698 | 504990 | -90.53 | 14.21 | 422.55 | 0.15 | 2.52 | 1583 |
| 2024-09-20 22:21:32.457 | MS1 | 121.4656728248 | 31.1446316575 | 698 | 504990 | -87.56 | 14.16 | 429.83 | 0.07 | 2.48 | 1583 |
| 2024-09-20 22:21:33.639 | MS1 | 121.4656660719 | 31.1446281086 | 698 | 504990 | -88.05 | 17.09 | 506.88 | 0.05 | 2.48 | 1597 |
| 2024-09-20 22:21:34.748 | MS1 | 121.4656726345 | 31.1446321041 | 698 | 504990 | -88.53 | 15.08 | 55.74 | 0.54 | 2.78 | 691 |
| 2024-09-20 22:21:35.704 | MS1 | 121.4656735441 | 31.1446342043 | 698 | 504990 | -87.00 | 17.44 | 84.59 | 0.65 | 2.57 | 683 |
| 2024-09-20 22:21:36.921 | MS1 | 121.4656622851 | 31.1446281902 | 698 | 504990 | -91.07 | 13.69 | 76.46 | 0.63 | 2.01 | 517 |
| 2024-09-20 22:21:37.356 | MS1 | 121.4656649490 | 31.1446358774 | 698 | 504990 | -93.82 | 11.15 | 62.57 | 0.52 | 2.57 | 509 |
| 2024-09-20 22:21:38.926 | MS1 | 121.4656761299 | 31.1446291992 | 698 | 504990 | -89.32 | 12.06 | 79.43 | 0.60 | 2.81 | 518 |
| 2024-09-20 22:21:39.766 | MS1 | 121.4656632757 | 31.1446186051 | 698 | 504990 | -89.54 | 12.60 | 57.04 | 0.53 | 2.18 | 647 |
| 2024-09-20 22:21:40.163 | MS1 | 121.4656719569 | 31.1446207735 | 698 | 504990 | -90.06 | 8.31 | 367.23 | 0.11 | 2.64 | 1589 |
| 2024-09-20 22:21:41.268 | MS1 | 121.4656731834 | 31.1446226829 | 698 | 504990 | -91.58 | 8.12 | 569.97 | 0.06 | 2.50 | 1596 |
| 2024-09-20 22:21:42.427 | MS1 | 121.4656732078 | 31.1446318483 | 698 | 504990 | -89.32 | 10.49 | 519.23 | 0.05 | 2.89 | 1561 |

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
| 3212907 | 3 | 121.4745099566 | 31.1519151090 | 332 | 5 | 8 | 28.1 | TDD | 98 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3230192 | 4 | 121.4652001654 | 31.1446099760 | 354 | 11 | 10 | 46.5 | TDD | 751 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3248381 | 2 | 121.4709936364 | 31.1489209235 | 50 | 2 | 6 | 21.6 | TDD | 791 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3277249 | 1 | 121.4690320581 | 31.1530653281 | 191 | 2 | 5 | 34.2 | TDD | 698 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |

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
| 2024-09-20 22:21:30.894 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.909 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.020 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.020 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.784 | NREventA3 | measId:2;ServCellPCI:956;Se... |
| 2024-09-20 22:21:38.024 | NRHandoverAttempt | SourcePCI:956;SourceNR-ARFC... |
| 2024-09-20 22:21:38.063 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.078 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.224 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.224 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3277249 | 1 | 12.9898 | 5.9999 | -117.2032 | 16.3100 | 118.9543 | 0.0037 | 0.0020 |
| 2024_09_20 22:00 | 3248381 | 2 | 6.7895 | 9.7353 | -117.7768 | 16.1184 | 163.3097 | 0.0061 | 0.0124 |
| 2024_09_20 22:00 | 3212907 | 3 | 10.1133 | 15.3441 | -114.2080 | 18.5471 | 175.5400 | 0.0174 | 0.0014 |
| 2024_09_20 22:00 | 3230192 | 4 | 19.3743 | 12.4819 | -116.3748 | 12.8115 | 176.1369 | 0.0125 | 0.0116 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413254_5CB294A7 | 504990 | 698 | -86.9 | 504990 | 98 | -88.6 | 504990 | 791 | -96.6 | 504990 | 751 |
| MR_1774413254_B4056ED8 | 504990 | 698 | -88.9 | 504990 | 98 | -87.8 | 504990 | 791 | -98.0 | 504990 | 751 |
| MR_1774413254_479990DD | 504990 | 698 | -86.9 | 504990 | 98 | -90.9 | 504990 | 791 | -97.1 | 504990 | 751 |
| MR_1774413254_7B12486C | 504990 | 698 | -87.2 | 504990 | 98 | -89.7 | 504990 | 791 | -97.2 | 504990 | 751 |
| MR_1774413254_775F91DE | 504990 | 698 | -88.3 | 504990 | 98 | -90.1 | 504990 | 791 | -97.3 | 504990 | 751 |
| MR_1774413254_4C51DBD6 | 504990 | 698 | -88.3 | 504990 | 98 | -87.5 | 504990 | 791 | -96.6 | 504990 | 751 |
| MR_1774413254_B76CA2D6 | 504990 | 698 | -87.7 | 504990 | 98 | -88.1 | 504990 | 791 | -98.2 | 504990 | 751 |

> *... 2개 열 생략 (전체 14열)*

---
