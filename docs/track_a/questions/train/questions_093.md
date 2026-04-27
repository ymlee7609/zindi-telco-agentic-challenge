# Track A 문제 분석 — train[920]~train[929]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[920] ~ train[929] (10개)

## 목차

1. [문제 920: `3606a2ec-f92...`](#920) — single-answer, 정답: C13
2. [문제 921: `d0e4e1fb-101...`](#921) — single-answer, 정답: C4
3. [문제 922: `3c650d7d-0be...`](#922) — single-answer, 정답: C9
4. [문제 923: `0b36fd71-db4...`](#923) — single-answer, 정답: C19
5. [문제 924: `3b59b81b-b89...`](#924) — single-answer, 정답: C8
6. [문제 925: `469edf46-777...`](#925) — single-answer, 정답: C20
7. [문제 926: `e5d002bb-ef9...`](#926) — single-answer, 정답: C14
8. [문제 927: `cfd9f8b6-d02...`](#927) — single-answer, 정답: C5
9. [문제 928: `82db9ad7-3dd...`](#928) — single-answer, 정답: C18
10. [문제 929: `ce479f6a-380...`](#929) — multiple-answer, 정답: C12|C19

---

### 문제 920: `3606a2ec-f92...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `3606a2ec-f924-4b46-a32e-11191fb316c7` |
| Tag | **single-answer** |
| 정답 | **C13** |
| C13 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3238686_3 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[920] topology](images/train_0920.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3238686_3 by 4 degrees
- `C2`: Decrease transmission power for 3238686_3
- `C3`: Insufficient data; more data is needed for judgment.
- `C4`: Add neighbor relationship between 3218578_8 and 3267754_5
- `C5`: Increase A3 Offset threshold for 3267754_5
- `C6`: Adjust the azimuth of 3267754_5 by 1 degrees
- `C7`: Lift the tilt angle of 3238686_3 by 4 degrees
- `C8`: Increase transmission power for 3238686_3
- `C9`: Check test server and transmission issues
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3267754_5
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3267754_5
- `C12`: Press down the tilt angle  of 3267754_5 by 2 degrees
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3238686_3 **← 정답**
- `C14`: Decrease A3 Offset threshold for 3267754_5
- `C15`: Increase transmission power for 3267754_5
- `C16`: Lift the tilt angle  of 3267754_5 by 2 degrees
- `C17`: Adjust the azimuth of 3238686_3 by 21 degrees
- `C18`: Decrease A3 Offset threshold for 3238686_3
- `C19`: Increase A3 Offset threshold for 3238686_3
- `C20`: Decrease transmission power for 3267754_5
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3238686_3
- `C22`: Add neighbor relationship between 3238686_3 and 3267754_5

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.605 | MS1 | 121.4656706817 | 31.1446205761 | 777 | 504990 | -93.80 | 11.83 | 352.19 | 0.13 | 2.02 | 1568 |
| 2024-09-20 22:21:32.635 | MS1 | 121.4656759483 | 31.1446313964 | 957 | 504990 | -94.08 | 14.82 | 340.49 | 0.09 | 2.44 | 1573 |
| 2024-09-20 22:21:33.625 | MS1 | 121.4656715626 | 31.1446263749 | 191 | 504990 | -95.42 | 9.36 | 337.26 | 0.17 | 2.80 | 1585 |
| 2024-09-20 22:21:34.556 | MS1 | 121.4656696964 | 31.1446340811 | 25 | 152650 | -92.81 | 2.33 | 79.75 | 0.11 | 1.89 | 944 |
| 2024-09-20 22:21:35.272 | MS1 | 121.4656718315 | 31.1446266058 | 464 | 152650 | -89.94 | 2.94 | 54.23 | 0.04 | 1.75 | 950 |
| 2024-09-20 22:21:36.598 | MS1 | 121.4656758515 | 31.1446255721 | 270 | 152650 | -95.20 | 3.70 | 59.55 | 0.05 | 1.84 | 991 |
| 2024-09-20 22:21:37.659 | MS1 | 121.4656645290 | 31.1446203347 | 124 | 152650 | -93.24 | 4.49 | 91.99 | 0.14 | 1.82 | 953 |
| 2024-09-20 22:21:38.617 | MS1 | 121.4656676288 | 31.1446315186 | 25 | 152650 | -92.39 | 4.20 | 77.19 | 0.05 | 1.59 | 943 |
| 2024-09-20 22:21:39.864 | MS1 | 121.4656640737 | 31.1446375444 | 464 | 152650 | -88.89 | 3.24 | 78.39 | 0.08 | 1.83 | 956 |
| 2024-09-20 22:21:40.510 | MS1 | 121.4656648756 | 31.1446297299 | 270 | 152650 | -91.61 | 6.05 | 72.21 | 0.09 | 2.31 | 1593 |
| 2024-09-20 22:21:41.839 | MS1 | 121.4656604427 | 31.1446259680 | 124 | 152650 | -91.38 | 2.07 | 91.87 | 0.10 | 2.82 | 1569 |
| 2024-09-20 22:21:42.919 | MS1 | 121.4656648083 | 31.1446368373 | 25 | 152650 | -96.67 | 2.47 | 83.20 | 0.06 | 2.90 | 1560 |

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
| 3215040 | 7 | 121.4733912586 | 31.1541134558 | 238 | 6 | 12 | 28.9 | FDD | 902 | n1 | 152650 | 30M | 4T4R | 29 | 152650 |
| 3218578 | 8 | 121.4695198601 | 31.1543911572 | 201 | 5 | 12 | 23.9 | FDD | 270 | n1 | 152650 | 30M | 4T4R | 30 | 152650 |
| 3222158 | 13 | 121.4642466875 | 31.1480439369 | 76 | 8 | 7 | 10.4 | FDD | 124 | n1 | 152650 | 30M | 4T4R | 12 | 152650 |
| 3234209 | 2 | 121.4713148670 | 31.1547626895 | 273 | 7 | 7 | 1.5 | TDD | 72 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3236301 | 6 | 121.4756719941 | 31.1456865319 | 65 | 4 | 5 | 19.3 | TDD | 191 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3238686 | 3 | 121.4684796384 | 31.1477892903 | 196 | 1 | 2 | 25.4 | TDD | 777 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3246391 | 1 | 121.4678078833 | 31.1540907997 | 63 | 8 | 3 | 2.0 | TDD | 2 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3246938 | 12 | 121.4692412994 | 31.1509870508 | 322 | 11 | 7 | 10.6 | FDD | 25 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |
| 3251220 | 9 | 121.4726420595 | 31.1524202882 | 30 | 9 | 4 | 14.7 | FDD | 464 | n1 | 152650 | 30M | 4T4R | 17 | 152650 |
| 3258256 | 4 | 121.4690173377 | 31.1530364080 | 244 | 3 | 1 | 9.5 | TDD | 957 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3267754 | 5 | 121.4745429528 | 31.1538351810 | 219 | 1 | 5 | 20.3 | TDD | 990 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3272746 | 11 | 121.4660816810 | 31.1549712612 | 31 | 12 | 5 | 6.4 | FDD | 724 | n1 | 152650 | 30M | 4T4R | 28 | 152650 |
| 3274806 | 10 | 121.4701737870 | 31.1489877716 | 286 | 4 | 0 | 14.5 | FDD | 144 | n1 | 152650 | 30M | 4T4R | 13 | 152650 |

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
| 2024-09-20 22:21:31.525 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.545 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.660 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.660 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.372 | NREventA2 | measId:1;ServCellPCI:146;Se... |
| 2024-09-20 22:21:35.486 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.744 | NREventA5 | measId:3;ServCellPCI:146;Se... |
| 2024-09-20 22:21:35.786 | NRHandoverAttempt | SourcePCI:146;SourceNR-ARFC... |
| 2024-09-20 22:21:35.816 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.830 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:35.968 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.968 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3246391 | 1 | 6.0655 | 17.7437 | -116.4134 | 8.4483 | 173.0138 | 0.0130 | 0.0013 |
| 2024_09_20 22:00 | 3234209 | 2 | 6.1204 | 6.0921 | -117.0713 | 18.7610 | 91.4604 | 0.0035 | 0.0195 |
| 2024_09_20 22:00 | 3238686 | 3 | 8.1351 | 13.7907 | -117.3352 | 18.6129 | 82.1542 | 0.0136 | 0.0012 |
| 2024_09_20 22:00 | 3258256 | 4 | 9.9144 | 13.4528 | -116.9158 | 6.7098 | 154.9653 | 0.0110 | 0.0061 |
| 2024_09_20 22:00 | 3267754 | 5 | 7.7751 | 5.3037 | -115.4048 | 5.5495 | 104.5643 | 0.0037 | 0.0063 |
| 2024_09_20 22:00 | 3236301 | 6 | 18.4793 | 6.0844 | -114.6412 | 15.1164 | 80.4093 | 0.0119 | 0.0156 |
| 2024_09_20 22:00 | 3215040 | 7 | 19.4810 | 18.1679 | -114.1601 | 4.3629 | 46.1175 | 0.0184 | 0.0200 |
| 2024_09_20 22:00 | 3218578 | 8 | 16.6474 | 19.0790 | -117.1434 | 3.3542 | 55.5771 | 0.0029 | 0.0001 |
| 2024_09_20 22:00 | 3251220 | 9 | 6.2304 | 19.3004 | -114.1173 | 4.4423 | 20.6612 | 0.0184 | 0.0078 |
| 2024_09_20 22:00 | 3274806 | 10 | 12.9020 | 12.5996 | -116.0741 | 4.6054 | 29.4195 | 0.0198 | 0.0033 |
| 2024_09_20 22:00 | 3272746 | 11 | 6.3003 | 14.5637 | -115.5134 | 3.9595 | 25.4246 | 0.0194 | 0.0089 |
| 2024_09_20 22:00 | 3246938 | 12 | 11.8559 | 10.5119 | -115.5384 | 4.8439 | 29.1247 | 0.0142 | 0.0029 |
| 2024_09_20 22:00 | 3222158 | 13 | 5.1743 | 7.7501 | -117.1988 | 3.1172 | 51.6341 | 0.0108 | 0.0023 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413728_9E154342 | 152650 | 25 | -92.8 | 152650 | 144 | -94.9 | 152650 | 902 | -97.5 | 152650 | 724 |
| MR_1774413728_2183095C | 504990 | 191 | -93.8 | 504990 | 990 | -93.0 | 504990 | 72 | -98.2 | 504990 | 2 |
| MR_1774413728_E39742F5 | 152650 | 25 | -94.6 | 152650 | 144 | -93.5 | 152650 | 902 | -100.1 | 152650 | 724 |
| MR_1774413728_DFC5C4A5 | 152650 | 25 | -93.2 | 152650 | 144 | -97.0 | 152650 | 902 | -99.6 | 152650 | 724 |
| MR_1774413728_AFB7F6C3 | 504990 | 191 | -94.6 | 504990 | 990 | -92.1 | 504990 | 72 | -97.6 | 504990 | 2 |
| MR_1774413728_2139806C | 152650 | 25 | -91.5 | 152650 | 144 | -96.9 | 152650 | 902 | -98.1 | 152650 | 724 |
| MR_1774413728_35FDE1B9 | 152650 | 25 | -92.8 | 152650 | 144 | -95.5 | 152650 | 902 | -96.9 | 152650 | 724 |
| MR_1774413728_B5BEDD2B | 152650 | 25 | -94.4 | 152650 | 144 | -94.7 | 152650 | 902 | -98.1 | 152650 | 724 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 921: `d0e4e1fb-101...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `d0e4e1fb-101f-4822-b05c-7b1fbefa21f4` |
| Tag | **single-answer** |
| 정답 | **C4** |
| C4 의미 | Decrease A3 Offset threshold for 3247490_3 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[921] topology](images/train_0921.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Check test server and transmission issues
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3247490_3
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3240150_2
- `C4`: Decrease A3 Offset threshold for 3247490_3 **← 정답**
- `C5`: Increase transmission power for 3247490_3
- `C6`: Add neighbor relationship between 3216944_4 and 3240150_2
- `C7`: Increase A3 Offset threshold for 3247490_3
- `C8`: Press down the tilt angle of 3247490_3 by 10 degrees
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3240150_2
- `C10`: Add neighbor relationship between 3247490_3 and 3240150_2
- `C11`: Press down the tilt angle  of 3240150_2 by 8 degrees
- `C12`: Lift the tilt angle of 3247490_3 by 10 degrees
- `C13`: Decrease transmission power for 3247490_3
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3247490_3
- `C15`: Lift the tilt angle  of 3240150_2 by 8 degrees
- `C16`: Increase transmission power for 3240150_2
- `C17`: Insufficient data; more data is needed for judgment.
- `C18`: Adjust the azimuth of 3240150_2 by 38 degrees
- `C19`: Adjust the azimuth of 3247490_3 by 50 degrees
- `C20`: Decrease transmission power for 3240150_2
- `C21`: Increase A3 Offset threshold for 3240150_2
- `C22`: Decrease A3 Offset threshold for 3240150_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.158 | MS1 | 121.4656729870 | 31.1446234657 | 974 | 504990 | -84.45 | 15.37 | 349.98 | 0.10 | 2.02 | 1561 |
| 2024-09-20 22:21:32.455 | MS1 | 121.4656649529 | 31.1446370310 | 974 | 504990 | -81.56 | 13.60 | 528.34 | 0.02 | 2.48 | 1598 |
| 2024-09-20 22:21:33.474 | MS1 | 121.4656737099 | 31.1446353944 | 974 | 504990 | -75.92 | 17.97 | 408.51 | 0.17 | 2.74 | 1584 |
| 2024-09-20 22:21:34.424 | MS1 | 121.4656655096 | 31.1446318361 | 974 | 504990 | -90.01 | -0.90 | 60.06 | 0.11 | 1.11 | 1588 |
| 2024-09-20 22:21:35.104 | MS1 | 121.4656622530 | 31.1446323595 | 974 | 504990 | -88.31 | -1.41 | 33.84 | 0.10 | 1.03 | 1593 |
| 2024-09-20 22:21:36.141 | MS1 | 121.4656630914 | 31.1446309204 | 974 | 504990 | -87.15 | -2.44 | 67.25 | 0.09 | 1.30 | 1585 |
| 2024-09-20 22:21:37.275 | MS1 | 121.4656703658 | 31.1446240317 | 974 | 504990 | -84.25 | -1.34 | 40.42 | 0.17 | 1.09 | 1577 |
| 2024-09-20 22:21:38.363 | MS1 | 121.4656750566 | 31.1446268996 | 974 | 504990 | -92.26 | -0.34 | 36.99 | 0.10 | 1.09 | 1572 |
| 2024-09-20 22:21:39.569 | MS1 | 121.4656593992 | 31.1446287658 | 187 | 504990 | -84.84 | 16.07 | 264.43 | 0.20 | 1.38 | 1597 |
| 2024-09-20 22:21:40.294 | MS1 | 121.4656764934 | 31.1446341685 | 187 | 504990 | -75.68 | 16.46 | 481.23 | 0.17 | 2.11 | 1589 |
| 2024-09-20 22:21:41.143 | MS1 | 121.4656657593 | 31.1446255743 | 187 | 504990 | -82.38 | 14.14 | 483.56 | 0.02 | 2.08 | 1592 |
| 2024-09-20 22:21:42.307 | MS1 | 121.4656626158 | 31.1446317814 | 187 | 504990 | -76.97 | 12.85 | 400.43 | 0.14 | 2.86 | 1584 |

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
| 3216944 | 4 | 121.4702031530 | 31.1534348796 | 4 | 14 | 8 | 22.8 | TDD | 1007 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3240150 | 2 | 121.4690844980 | 31.1491847394 | 251 | 4 | 4 | 42.1 | TDD | 187 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3247490 | 3 | 121.4753467857 | 31.1529144803 | 282 | 14 | 5 | 22.2 | TDD | 974 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3270428 | 1 | 121.4729195981 | 31.1441572359 | 25 | 8 | 8 | 48.6 | TDD | 19 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |

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
| 2024-09-20 22:21:31.216 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.233 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.364 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.364 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.036 | NREventA3 | measId:2;ServCellPCI:294;Se... |
| 2024-09-20 22:21:38.276 | NRHandoverAttempt | SourcePCI:294;SourceNR-ARFC... |
| 2024-09-20 22:21:38.312 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.322 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.427 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.427 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3270428 | 1 | 19.2118 | 15.5643 | -115.7473 | 12.3811 | 137.6034 | 0.0026 | 0.0188 |
| 2024_09_20 22:00 | 3240150 | 2 | 18.8345 | 13.1035 | -115.9935 | 13.6429 | 137.0767 | 0.0122 | 0.0194 |
| 2024_09_20 22:00 | 3247490 | 3 | 13.3471 | 5.2267 | -115.2119 | 11.8081 | 86.9952 | 0.0059 | 0.1288 |
| 2024_09_20 22:00 | 3216944 | 4 | 16.4801 | 10.5602 | -116.7554 | 11.4481 | 92.4053 | 0.0147 | 0.0174 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415243_14CDF418 | 504990 | 187 | -85.6 | 504990 | 974 | -89.8 | 504990 | 1007 | -93.0 | 504990 | 19 |
| MR_1774415243_4745BA12 | 504990 | 974 | -89.5 | 504990 | 187 | -84.2 | 504990 | 1007 | -93.9 | 504990 | 19 |
| MR_1774415243_59605C4F | 504990 | 187 | -84.2 | 504990 | 974 | -88.7 | 504990 | 1007 | -92.2 | 504990 | 19 |
| MR_1774415243_47234943 | 504990 | 187 | -84.5 | 504990 | 974 | -88.1 | 504990 | 1007 | -95.8 | 504990 | 19 |
| MR_1774415243_9BFDEBB7 | 504990 | 974 | -90.6 | 504990 | 187 | -82.9 | 504990 | 1007 | -94.1 | 504990 | 19 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 922: `3c650d7d-0be...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `3c650d7d-0bec-4077-b156-c98ded2f258d` |
| Tag | **single-answer** |
| 정답 | **C9** |
| C9 의미 | Decrease A3 Offset threshold for 3269513_1 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[922] topology](images/train_0922.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3261693_4 and 3218968_3
- `C2`: Insufficient data; more data is needed for judgment.
- `C3`: Increase transmission power for 3218968_3
- `C4`: Adjust the azimuth of 3218968_3 by 50 degrees
- `C5`: Check test server and transmission issues
- `C6`: Press down the tilt angle of 3269513_1 by 7 degrees
- `C7`: Press down the tilt angle  of 3218968_3 by 10 degrees
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3218968_3
- `C9`: Decrease A3 Offset threshold for 3269513_1 **← 정답**
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3269513_1
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3218968_3
- `C12`: Decrease transmission power for 3269513_1
- `C13`: Add neighbor relationship between 3269513_1 and 3218968_3
- `C14`: Increase A3 Offset threshold for 3218968_3
- `C15`: Decrease transmission power for 3218968_3
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3269513_1
- `C17`: Lift the tilt angle  of 3218968_3 by 10 degrees
- `C18`: Increase A3 Offset threshold for 3269513_1
- `C19`: Lift the tilt angle of 3269513_1 by 7 degrees
- `C20`: Decrease A3 Offset threshold for 3218968_3
- `C21`: Increase transmission power for 3269513_1
- `C22`: Adjust the azimuth of 3269513_1 by 26 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.632 | MS1 | 121.4656618386 | 31.1446279439 | 202 | 504990 | -77.27 | 13.88 | 341.33 | 0.05 | 2.48 | 1576 |
| 2024-09-20 22:21:32.714 | MS1 | 121.4656761076 | 31.1446268585 | 202 | 504990 | -76.30 | 16.58 | 360.58 | 0.04 | 2.35 | 1592 |
| 2024-09-20 22:21:33.517 | MS1 | 121.4656759058 | 31.1446280286 | 202 | 504990 | -84.42 | 12.73 | 454.18 | 0.08 | 2.07 | 1563 |
| 2024-09-20 22:21:34.258 | MS1 | 121.4656719008 | 31.1446376287 | 202 | 504990 | -86.99 | -2.11 | 41.07 | 0.20 | 1.17 | 1591 |
| 2024-09-20 22:21:35.876 | MS1 | 121.4656632884 | 31.1446374202 | 202 | 504990 | -89.76 | -3.57 | 52.61 | 0.19 | 1.27 | 1584 |
| 2024-09-20 22:21:36.598 | MS1 | 121.4656772133 | 31.1446180134 | 202 | 504990 | -83.86 | -1.29 | 40.73 | 0.18 | 1.16 | 1590 |
| 2024-09-20 22:21:37.324 | MS1 | 121.4656582212 | 31.1446251452 | 202 | 504990 | -85.77 | -3.38 | 49.65 | 0.02 | 1.34 | 1581 |
| 2024-09-20 22:21:38.195 | MS1 | 121.4656715320 | 31.1446288643 | 202 | 504990 | -88.39 | -2.69 | 48.69 | 0.07 | 1.39 | 1581 |
| 2024-09-20 22:21:39.110 | MS1 | 121.4656689241 | 31.1446284821 | 445 | 504990 | -79.53 | 15.15 | 197.51 | 0.13 | 1.25 | 1570 |
| 2024-09-20 22:21:40.452 | MS1 | 121.4656655734 | 31.1446295951 | 445 | 504990 | -84.71 | 16.25 | 583.36 | 0.19 | 2.56 | 1587 |
| 2024-09-20 22:21:41.104 | MS1 | 121.4656742273 | 31.1446246721 | 445 | 504990 | -82.67 | 17.27 | 554.63 | 0.15 | 2.32 | 1586 |
| 2024-09-20 22:21:42.862 | MS1 | 121.4656646005 | 31.1446246185 | 445 | 504990 | -82.70 | 17.44 | 471.51 | 0.15 | 2.03 | 1567 |

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
| 3218968 | 3 | 121.4644881121 | 31.1453405512 | 184 | 7 | 10 | 15.9 | TDD | 445 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3227262 | 2 | 121.4674505595 | 31.1443303665 | 9 | 13 | 6 | 44.5 | TDD | 554 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3261693 | 4 | 121.4661550396 | 31.1531687560 | 286 | 2 | 0 | 23.2 | TDD | 975 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3269513 | 1 | 121.4727043453 | 31.1556971854 | 182 | 5 | 11 | 40.3 | TDD | 202 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |

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
| 2024-09-20 22:21:31.120 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.137 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.272 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.272 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.943 | NREventA3 | measId:2;ServCellPCI:140;Se... |
| 2024-09-20 22:21:38.183 | NRHandoverAttempt | SourcePCI:140;SourceNR-ARFC... |
| 2024-09-20 22:21:38.213 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.223 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.357 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.357 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3269513 | 1 | 6.1492 | 8.9930 | -115.3996 | 10.4763 | 124.0871 | 0.0041 | 0.1879 |
| 2024_09_20 22:00 | 3227262 | 2 | 18.2796 | 8.7943 | -116.3305 | 13.5317 | 109.6633 | 0.0005 | 0.0087 |
| 2024_09_20 22:00 | 3218968 | 3 | 5.0680 | 9.5760 | -115.6311 | 14.3273 | 178.9852 | 0.0041 | 0.0176 |
| 2024_09_20 22:00 | 3261693 | 4 | 10.8667 | 11.5506 | -117.7261 | 15.4716 | 136.9539 | 0.0079 | 0.0099 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412633_729C28BB | 504990 | 202 | -88.6 | 504990 | 445 | -81.2 | 504990 | 975 | -83.4 | 504990 | 554 |
| MR_1774412633_7567EB02 | 504990 | 202 | -87.6 | 504990 | 445 | -83.3 | 504990 | 975 | -85.3 | 504990 | 554 |
| MR_1774412633_6A9CCBDC | 504990 | 202 | -87.2 | 504990 | 445 | -83.1 | 504990 | 975 | -84.1 | 504990 | 554 |
| MR_1774412633_329DB5BC | 504990 | 202 | -88.9 | 504990 | 445 | -81.9 | 504990 | 975 | -83.1 | 504990 | 554 |
| MR_1774412633_D032A307 | 504990 | 445 | -81.1 | 504990 | 202 | -85.7 | 504990 | 975 | -82.7 | 504990 | 554 |
| MR_1774412633_F131C55A | 504990 | 202 | -86.3 | 504990 | 445 | -81.2 | 504990 | 975 | -85.1 | 504990 | 554 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 923: `0b36fd71-db4...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `0b36fd71-db44-4080-a7de-e2b8598ab0b0` |
| Tag | **single-answer** |
| 정답 | **C19** |
| C19 의미 | Decrease A3 Offset threshold for 3226530_1 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[923] topology](images/train_0923.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3226530_1
- `C2`: Decrease transmission power for 3219328_3
- `C3`: Add neighbor relationship between 3226530_1 and 3219328_3
- `C4`: Insufficient data; more data is needed for judgment.
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3219328_3
- `C6`: Decrease transmission power for 3226530_1
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3219328_3
- `C8`: Increase transmission power for 3219328_3
- `C9`: Press down the tilt angle  of 3219328_3 by 2 degrees
- `C10`: Lift the tilt angle  of 3219328_3 by 2 degrees
- `C11`: Lift the tilt angle of 3226530_1 by 4 degrees
- `C12`: Add neighbor relationship between 3226069_2 and 3219328_3
- `C13`: Adjust the azimuth of 3219328_3 by 50 degrees
- `C14`: Press down the tilt angle of 3226530_1 by 4 degrees
- `C15`: Decrease A3 Offset threshold for 3219328_3
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3226530_1
- `C17`: Adjust the azimuth of 3226530_1 by 26 degrees
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3226530_1
- `C19`: Decrease A3 Offset threshold for 3226530_1 **← 정답**
- `C20`: Increase A3 Offset threshold for 3219328_3
- `C21`: Check test server and transmission issues
- `C22`: Increase transmission power for 3226530_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.713 | MS1 | 121.4656666954 | 31.1446210785 | 753 | 504990 | -82.19 | 16.76 | 488.72 | 0.12 | 2.23 | 1562 |
| 2024-09-20 22:21:32.430 | MS1 | 121.4656651130 | 31.1446265709 | 753 | 504990 | -80.34 | 14.85 | 580.31 | 0.09 | 2.12 | 1572 |
| 2024-09-20 22:21:33.353 | MS1 | 121.4656619963 | 31.1446227691 | 753 | 504990 | -79.78 | 16.00 | 354.02 | 0.15 | 2.64 | 1575 |
| 2024-09-20 22:21:34.454 | MS1 | 121.4656638401 | 31.1446305458 | 753 | 504990 | -85.63 | -3.99 | 62.34 | 0.08 | 1.38 | 1577 |
| 2024-09-20 22:21:35.782 | MS1 | 121.4656685511 | 31.1446316930 | 753 | 504990 | -87.08 | -2.12 | 33.76 | 0.12 | 1.24 | 1587 |
| 2024-09-20 22:21:36.532 | MS1 | 121.4656667074 | 31.1446361490 | 753 | 504990 | -88.51 | -1.00 | 41.03 | 0.15 | 1.10 | 1571 |
| 2024-09-20 22:21:37.737 | MS1 | 121.4656717973 | 31.1446238440 | 753 | 504990 | -87.93 | -0.16 | 58.73 | 0.10 | 1.41 | 1561 |
| 2024-09-20 22:21:38.782 | MS1 | 121.4656759834 | 31.1446200858 | 753 | 504990 | -90.66 | -0.29 | 50.53 | 0.19 | 1.42 | 1579 |
| 2024-09-20 22:21:39.162 | MS1 | 121.4656692152 | 31.1446357387 | 758 | 504990 | -77.23 | 14.93 | 252.71 | 0.13 | 1.28 | 1561 |
| 2024-09-20 22:21:40.253 | MS1 | 121.4656688417 | 31.1446272784 | 758 | 504990 | -76.08 | 16.99 | 475.30 | 0.09 | 2.84 | 1587 |
| 2024-09-20 22:21:41.209 | MS1 | 121.4656754190 | 31.1446195428 | 758 | 504990 | -84.46 | 15.88 | 472.48 | 0.08 | 2.15 | 1588 |
| 2024-09-20 22:21:42.717 | MS1 | 121.4656679775 | 31.1446266552 | 758 | 504990 | -79.19 | 17.74 | 323.91 | 0.02 | 2.84 | 1577 |

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
| 3219328 | 3 | 121.4723867782 | 31.1534043883 | 101 | 0 | 6 | 35.2 | TDD | 758 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3226069 | 2 | 121.4665472893 | 31.1461370151 | 19 | 8 | 2 | 25.9 | TDD | 515 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3226530 | 1 | 121.4710475291 | 31.1535709549 | 181 | 3 | 8 | 27.0 | TDD | 753 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3263632 | 4 | 121.4759468863 | 31.1453390204 | 121 | 4 | 3 | 45.4 | TDD | 927 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:31.201 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.216 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.340 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.340 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.034 | NREventA3 | measId:2;ServCellPCI:93;Ser... |
| 2024-09-20 22:21:38.274 | NRHandoverAttempt | SourcePCI:93;SourceNR-ARFCN... |
| 2024-09-20 22:21:38.322 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.334 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.443 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.443 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3226530 | 1 | 5.2276 | 17.1310 | -116.2488 | 18.3797 | 92.2954 | 0.0072 | 0.1176 |
| 2024_09_20 22:00 | 3226069 | 2 | 10.5292 | 18.1923 | -117.1124 | 6.6196 | 134.7340 | 0.0046 | 0.0017 |
| 2024_09_20 22:00 | 3219328 | 3 | 19.4614 | 18.0336 | -116.0814 | 11.0303 | 92.4833 | 0.0200 | 0.0031 |
| 2024_09_20 22:00 | 3263632 | 4 | 14.1618 | 17.3467 | -116.3108 | 13.7366 | 108.5436 | 0.0018 | 0.0045 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414188_938E493D | 504990 | 753 | -86.2 | 504990 | 758 | -78.4 | 504990 | 515 | -79.5 | 504990 | 927 |
| MR_1774414188_6D226F24 | 504990 | 753 | -85.3 | 504990 | 758 | -76.8 | 504990 | 515 | -81.6 | 504990 | 927 |
| MR_1774414188_065BDAC5 | 504990 | 753 | -87.6 | 504990 | 758 | -79.8 | 504990 | 515 | -79.0 | 504990 | 927 |
| MR_1774414188_7E17B393 | 504990 | 753 | -85.0 | 504990 | 758 | -76.7 | 504990 | 515 | -78.4 | 504990 | 927 |
| MR_1774414188_4021D839 | 504990 | 758 | -77.1 | 504990 | 753 | -83.8 | 504990 | 515 | -81.5 | 504990 | 927 |
| MR_1774414188_2A3729E1 | 504990 | 753 | -84.7 | 504990 | 758 | -78.8 | 504990 | 515 | -80.5 | 504990 | 927 |
| MR_1774414188_5BB790B2 | 504990 | 753 | -84.8 | 504990 | 758 | -79.7 | 504990 | 515 | -81.0 | 504990 | 927 |
| MR_1774414188_D02EEA17 | 504990 | 753 | -86.9 | 504990 | 758 | -79.4 | 504990 | 515 | -82.3 | 504990 | 927 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 924: `3b59b81b-b89...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `3b59b81b-b894-4cb6-a3e5-9e9eddb1b745` |
| Tag | **single-answer** |
| 정답 | **C8** |
| C8 의미 | Decrease A3 Offset threshold for 3262241_1 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[924] topology](images/train_0924.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3262241_1 by 50 degrees
- `C2`: Lift the tilt angle of 3262241_1 by 10 degrees
- `C3`: Increase A3 Offset threshold for 3236556_2
- `C4`: Press down the tilt angle  of 3236556_2 by 3 degrees
- `C5`: Lift the tilt angle  of 3236556_2 by 3 degrees
- `C6`: Increase transmission power for 3236556_2
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3236556_2
- `C8`: Decrease A3 Offset threshold for 3262241_1 **← 정답**
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3262241_1
- `C10`: Adjust the azimuth of 3236556_2 by 50 degrees
- `C11`: Decrease A3 Offset threshold for 3236556_2
- `C12`: Add neighbor relationship between 3262241_1 and 3236556_2
- `C13`: Increase transmission power for 3262241_1
- `C14`: Increase A3 Offset threshold for 3262241_1
- `C15`: Press down the tilt angle of 3262241_1 by 10 degrees
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3262241_1
- `C17`: Add neighbor relationship between 3221609_3 and 3236556_2
- `C18`: Decrease transmission power for 3262241_1
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3236556_2
- `C20`: Check test server and transmission issues
- `C21`: Insufficient data; more data is needed for judgment.
- `C22`: Decrease transmission power for 3236556_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.323 | MS1 | 121.4656698461 | 31.1446216717 | 832 | 504990 | -83.24 | 16.50 | 323.27 | 0.02 | 2.77 | 1570 |
| 2024-09-20 22:21:32.208 | MS1 | 121.4656677937 | 31.1446371242 | 832 | 504990 | -84.18 | 13.99 | 349.94 | 0.08 | 2.34 | 1564 |
| 2024-09-20 22:21:33.984 | MS1 | 121.4656691067 | 31.1446235478 | 832 | 504990 | -77.47 | 14.49 | 338.86 | 0.15 | 2.66 | 1577 |
| 2024-09-20 22:21:34.897 | MS1 | 121.4656624765 | 31.1446366446 | 832 | 504990 | -87.89 | -1.74 | 64.60 | 0.17 | 1.16 | 1569 |
| 2024-09-20 22:21:35.308 | MS1 | 121.4656695592 | 31.1446336043 | 832 | 504990 | -84.98 | -0.57 | 47.63 | 0.06 | 1.40 | 1578 |
| 2024-09-20 22:21:36.837 | MS1 | 121.4656751253 | 31.1446303300 | 832 | 504990 | -83.67 | -2.15 | 56.48 | 0.06 | 1.35 | 1588 |
| 2024-09-20 22:21:37.598 | MS1 | 121.4656733472 | 31.1446312526 | 832 | 504990 | -85.57 | -3.39 | 48.61 | 0.10 | 1.33 | 1575 |
| 2024-09-20 22:21:38.601 | MS1 | 121.4656692377 | 31.1446259845 | 832 | 504990 | -83.30 | -1.55 | 34.36 | 0.05 | 1.32 | 1599 |
| 2024-09-20 22:21:39.288 | MS1 | 121.4656580015 | 31.1446203980 | 180 | 504990 | -83.59 | 17.61 | 170.30 | 0.10 | 1.21 | 1584 |
| 2024-09-20 22:21:40.908 | MS1 | 121.4656764327 | 31.1446304693 | 180 | 504990 | -80.57 | 13.83 | 318.81 | 0.04 | 2.82 | 1583 |
| 2024-09-20 22:21:41.949 | MS1 | 121.4656606784 | 31.1446213286 | 180 | 504990 | -78.06 | 14.88 | 405.87 | 0.08 | 2.22 | 1577 |
| 2024-09-20 22:21:42.393 | MS1 | 121.4656596257 | 31.1446306616 | 180 | 504990 | -75.48 | 15.08 | 508.76 | 0.06 | 2.83 | 1568 |

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
| 3221609 | 3 | 121.4708555412 | 31.1473657050 | 106 | 3 | 3 | 42.0 | TDD | 411 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3236556 | 2 | 121.4676532092 | 31.1491786761 | 86 | 0 | 8 | 25.8 | TDD | 180 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3245110 | 4 | 121.4748103291 | 31.1500399527 | 195 | 3 | 11 | 42.1 | TDD | 404 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3262241 | 1 | 121.4710043085 | 31.1477670632 | 119 | 9 | 3 | 38.4 | TDD | 832 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:31.107 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.129 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.279 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.279 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.975 | NREventA3 | measId:2;ServCellPCI:579;Se... |
| 2024-09-20 22:21:38.215 | NRHandoverAttempt | SourcePCI:579;SourceNR-ARFC... |
| 2024-09-20 22:21:38.264 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.278 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.397 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.397 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3262241 | 1 | 7.8335 | 16.6478 | -115.3102 | 7.2649 | 92.9456 | 0.0127 | 0.1618 |
| 2024_09_20 22:00 | 3236556 | 2 | 8.3230 | 11.2644 | -117.3096 | 11.9037 | 196.2858 | 0.0073 | 0.0134 |
| 2024_09_20 22:00 | 3221609 | 3 | 17.7013 | 18.8230 | -116.8038 | 14.1228 | 175.3621 | 0.0184 | 0.0028 |
| 2024_09_20 22:00 | 3245110 | 4 | 17.7983 | 17.8489 | -114.3261 | 11.4824 | 89.4599 | 0.0170 | 0.0109 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416662_F492113D | 504990 | 180 | -83.6 | 504990 | 832 | -88.6 | 504990 | 411 | -87.3 | 504990 | 404 |
| MR_1774416662_BF2C9026 | 504990 | 832 | -87.9 | 504990 | 180 | -81.8 | 504990 | 411 | -86.7 | 504990 | 404 |
| MR_1774416662_BC1AF955 | 504990 | 832 | -86.8 | 504990 | 180 | -81.8 | 504990 | 411 | -86.8 | 504990 | 404 |
| MR_1774416662_BA14D791 | 504990 | 832 | -87.0 | 504990 | 180 | -84.0 | 504990 | 411 | -85.3 | 504990 | 404 |
| MR_1774416662_AAFA42F4 | 504990 | 832 | -88.4 | 504990 | 180 | -84.1 | 504990 | 411 | -86.7 | 504990 | 404 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 925: `469edf46-777...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `469edf46-7774-416a-8f79-4690d07b7520` |
| Tag | **single-answer** |
| 정답 | **C20** |
| C20 의미 | Add neighbor relationship between 3233866_2 and 3277302_3 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[925] topology](images/train_0925.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3233866_2
- `C2`: Press down the tilt angle of 3233866_2 by 6 degrees
- `C3`: Decrease transmission power for 3233866_2
- `C4`: Lift the tilt angle  of 3277302_3 by 4 degrees
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3277302_3
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3277302_3
- `C7`: Lift the tilt angle of 3233866_2 by 6 degrees
- `C8`: Adjust the azimuth of 3233866_2 by 50 degrees
- `C9`: Decrease A3 Offset threshold for 3233866_2
- `C10`: Increase A3 Offset threshold for 3277302_3
- `C11`: Increase transmission power for 3233866_2
- `C12`: Decrease A3 Offset threshold for 3277302_3
- `C13`: Add neighbor relationship between 3260518_1 and 3277302_3
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3233866_2
- `C16`: Increase transmission power for 3277302_3
- `C17`: Decrease transmission power for 3277302_3
- `C18`: Press down the tilt angle  of 3277302_3 by 4 degrees
- `C19`: Adjust the azimuth of 3277302_3 by 28 degrees
- `C20`: Add neighbor relationship between 3233866_2 and 3277302_3 **← 정답**
- `C21`: Increase A3 Offset threshold for 3233866_2
- `C22`: Check test server and transmission issues

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.800 | MS1 | 121.4656769303 | 31.1446368724 | 461 | 504990 | -83.51 | 13.84 | 513.48 | 0.04 | 2.70 | 1586 |
| 2024-09-20 22:21:32.231 | MS1 | 121.4656681676 | 31.1446313414 | 461 | 504990 | -77.05 | 12.64 | 358.22 | 0.15 | 2.68 | 1590 |
| 2024-09-20 22:21:33.216 | MS1 | 121.4656711136 | 31.1446268838 | 461 | 504990 | -76.98 | 17.99 | 421.84 | 0.03 | 2.57 | 1593 |
| 2024-09-20 22:21:34.827 | MS1 | 121.4656648014 | 31.1446349283 | 461 | 504990 | -87.08 | -2.24 | 49.47 | 0.06 | 1.45 | 1565 |
| 2024-09-20 22:21:35.268 | MS1 | 121.4656586724 | 31.1446227967 | 461 | 504990 | -94.38 | -2.99 | 46.67 | 0.08 | 1.42 | 1577 |
| 2024-09-20 22:21:36.883 | MS1 | 121.4656709243 | 31.1446273521 | 461 | 504990 | -87.52 | -2.54 | 64.48 | 0.13 | 1.29 | 1581 |
| 2024-09-20 22:21:37.910 | MS1 | 121.4656629902 | 31.1446314742 | 461 | 504990 | -93.50 | -0.22 | 61.98 | 0.01 | 1.46 | 1565 |
| 2024-09-20 22:21:38.129 | MS1 | 121.4656730872 | 31.1446202082 | 461 | 504990 | -76.53 | 16.27 | 532.24 | 0.18 | 1.10 | 1572 |
| 2024-09-20 22:21:39.239 | MS1 | 121.4656711567 | 31.1446184369 | 461 | 504990 | -79.84 | 16.80 | 447.47 | 0.18 | 1.30 | 1589 |
| 2024-09-20 22:21:40.165 | MS1 | 121.4656772147 | 31.1446353546 | 461 | 504990 | -82.10 | 14.40 | 397.14 | 0.09 | 2.49 | 1583 |
| 2024-09-20 22:21:41.575 | MS1 | 121.4656671867 | 31.1446203296 | 461 | 504990 | -84.92 | 17.25 | 445.36 | 0.00 | 2.11 | 1570 |
| 2024-09-20 22:21:42.598 | MS1 | 121.4656723843 | 31.1446334060 | 461 | 504990 | -78.42 | 17.22 | 553.46 | 0.09 | 2.35 | 1582 |

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
| 3233866 | 2 | 121.4704054659 | 31.1541602569 | 118 | 4 | 4 | 42.6 | TDD | 461 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3244836 | 4 | 121.4757339764 | 31.1469439124 | 345 | 11 | 0 | 27.2 | TDD | 677 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3260518 | 1 | 121.4650348471 | 31.1542009748 | 228 | 2 | 0 | 43.2 | TDD | 235 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3277302 | 3 | 121.4710932492 | 31.1502461607 | 248 | 1 | 10 | 46.9 | TDD | 133 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

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
| 2024-09-20 22:21:31.616 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.640 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.755 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.755 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.419 | NREventA3 | measId:2;ServCellPCI:464;Se... |
| 2024-09-20 22:21:36.419 | NREventA3 | measId:2;ServCellPCI:464;Se... |
| 2024-09-20 22:21:37.419 | NREventA3 | measId:2;ServCellPCI:464;Se... |
| 2024-09-20 22:21:39.919 | NRRRCReestablishAttempt | PCI:464 |
| 2024-09-20 22:21:39.934 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.949 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:40.091 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:40.091 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3260518 | 1 | 19.5893 | 12.0550 | -115.0181 | 5.5927 | 137.0884 | 0.0004 | 0.0158 |
| 2024_09_20 22:00 | 3233866 | 2 | 8.4944 | 8.6866 | -115.4303 | 10.2842 | 166.0525 | 0.0109 | 0.1213 |
| 2024_09_20 22:00 | 3277302 | 3 | 13.5228 | 18.3421 | -114.8510 | 8.9918 | 136.4656 | 0.0019 | 0.0019 |
| 2024_09_20 22:00 | 3244836 | 4 | 14.6449 | 5.0109 | -117.5473 | 11.6555 | 83.2369 | 0.0148 | 0.0082 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412277_3DC36328 | 504990 | 133 | -82.8 | 504990 | 461 | -87.0 | 504990 | 235 | -89.7 | 504990 | 677 |
| MR_1774412277_F9AB6AD7 | 504990 | 133 | -84.4 | 504990 | 461 | -85.6 | 504990 | 235 | -87.4 | 504990 | 677 |
| MR_1774412277_5FB23F05 | 504990 | 133 | -82.7 | 504990 | 461 | -88.1 | 504990 | 235 | -87.3 | 504990 | 677 |
| MR_1774412277_A44267B9 | 504990 | 461 | -85.3 | 504990 | 133 | -83.0 | 504990 | 235 | -87.5 | 504990 | 677 |
| MR_1774412277_919F61E6 | 504990 | 133 | -82.0 | 504990 | 461 | -87.6 | 504990 | 235 | -89.8 | 504990 | 677 |
| MR_1774412277_7D382149 | 504990 | 461 | -88.3 | 504990 | 133 | -83.9 | 504990 | 235 | -89.0 | 504990 | 677 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 926: `e5d002bb-ef9...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `e5d002bb-ef91-4456-bc2f-c2999e94ddb2` |
| Tag | **single-answer** |
| 정답 | **C14** |
| C14 의미 | Add neighbor relationship between 3221495_1 and 3267978_4 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[926] topology](images/train_0926.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3267978_4 by 6 degrees
- `C2`: Insufficient data; more data is needed for judgment.
- `C3`: Increase transmission power for 3267978_4
- `C4`: Lift the tilt angle of 3221495_1 by 8 degrees
- `C5`: Lift the tilt angle  of 3267978_4 by 6 degrees
- `C6`: Decrease A3 Offset threshold for 3221495_1
- `C7`: Press down the tilt angle of 3221495_1 by 8 degrees
- `C8`: Check test server and transmission issues
- `C9`: Decrease transmission power for 3267978_4
- `C10`: Increase A3 Offset threshold for 3267978_4
- `C11`: Adjust the azimuth of 3221495_1 by 50 degrees
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3221495_1
- `C13`: Increase transmission power for 3221495_1
- `C14`: Add neighbor relationship between 3221495_1 and 3267978_4 **← 정답**
- `C15`: Increase A3 Offset threshold for 3221495_1
- `C16`: Decrease transmission power for 3221495_1
- `C17`: Add neighbor relationship between 3256740_3 and 3267978_4
- `C18`: Decrease A3 Offset threshold for 3267978_4
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3221495_1
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3267978_4
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3267978_4
- `C22`: Adjust the azimuth of 3267978_4 by 3 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.209 | MS1 | 121.4656727109 | 31.1446349396 | 384 | 504990 | -81.82 | 13.67 | 322.85 | 0.04 | 2.23 | 1582 |
| 2024-09-20 22:21:32.106 | MS1 | 121.4656667416 | 31.1446310495 | 384 | 504990 | -84.14 | 15.21 | 577.25 | 0.05 | 2.10 | 1600 |
| 2024-09-20 22:21:33.181 | MS1 | 121.4656609593 | 31.1446319300 | 384 | 504990 | -82.35 | 12.39 | 514.18 | 0.14 | 2.16 | 1582 |
| 2024-09-20 22:21:34.924 | MS1 | 121.4656770100 | 31.1446238175 | 384 | 504990 | -88.29 | -0.45 | 72.17 | 0.01 | 1.28 | 1563 |
| 2024-09-20 22:21:35.767 | MS1 | 121.4656744982 | 31.1446213495 | 384 | 504990 | -92.92 | -3.82 | 48.66 | 0.01 | 1.45 | 1570 |
| 2024-09-20 22:21:36.144 | MS1 | 121.4656735188 | 31.1446185177 | 384 | 504990 | -85.19 | -3.69 | 32.82 | 0.15 | 1.29 | 1564 |
| 2024-09-20 22:21:37.213 | MS1 | 121.4656707134 | 31.1446271520 | 384 | 504990 | -93.10 | -2.60 | 60.16 | 0.16 | 1.45 | 1578 |
| 2024-09-20 22:21:38.522 | MS1 | 121.4656660242 | 31.1446294778 | 384 | 504990 | -76.42 | 13.25 | 435.46 | 0.04 | 1.50 | 1579 |
| 2024-09-20 22:21:39.302 | MS1 | 121.4656769340 | 31.1446200168 | 384 | 504990 | -77.64 | 15.21 | 580.69 | 0.04 | 1.00 | 1576 |
| 2024-09-20 22:21:40.838 | MS1 | 121.4656616608 | 31.1446238597 | 384 | 504990 | -75.88 | 15.18 | 385.21 | 0.14 | 2.88 | 1579 |
| 2024-09-20 22:21:41.494 | MS1 | 121.4656617005 | 31.1446300291 | 384 | 504990 | -78.41 | 14.75 | 557.66 | 0.05 | 2.85 | 1579 |
| 2024-09-20 22:21:42.938 | MS1 | 121.4656772745 | 31.1446182106 | 384 | 504990 | -77.62 | 13.92 | 464.58 | 0.06 | 2.37 | 1569 |

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
| 3221495 | 1 | 121.4696097269 | 31.1528403552 | 344 | 5 | 4 | 46.5 | TDD | 384 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3256740 | 3 | 121.4726038333 | 31.1514444361 | 341 | 8 | 0 | 25.5 | TDD | 667 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3257925 | 2 | 121.4690738838 | 31.1517543562 | 91 | 7 | 12 | 42.0 | TDD | 210 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3267978 | 4 | 121.4708188958 | 31.1440391243 | 280 | 2 | 10 | 32.0 | TDD | 330 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:31.597 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.617 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.720 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.720 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.413 | NREventA3 | measId:2;ServCellPCI:706;Se... |
| 2024-09-20 22:21:36.413 | NREventA3 | measId:2;ServCellPCI:706;Se... |
| 2024-09-20 22:21:37.413 | NREventA3 | measId:2;ServCellPCI:706;Se... |
| 2024-09-20 22:21:39.913 | NRRRCReestablishAttempt | PCI:706 |
| 2024-09-20 22:21:39.929 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.944 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:40.069 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:40.069 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3221495 | 1 | 12.4303 | 9.3336 | -117.1241 | 10.9466 | 182.2565 | 0.0088 | 0.1893 |
| 2024_09_20 22:00 | 3257925 | 2 | 6.7555 | 11.7759 | -117.5569 | 8.4701 | 198.0496 | 0.0012 | 0.0119 |
| 2024_09_20 22:00 | 3256740 | 3 | 14.2464 | 17.2032 | -117.2065 | 17.5619 | 182.7071 | 0.0020 | 0.0070 |
| 2024_09_20 22:00 | 3267978 | 4 | 11.7708 | 14.6569 | -117.1062 | 9.4102 | 81.0871 | 0.0170 | 0.0078 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414537_83F0D846 | 504990 | 330 | -84.0 | 504990 | 384 | -88.9 | 504990 | 667 | -91.2 | 504990 | 210 |
| MR_1774414537_23EF7741 | 504990 | 384 | -90.2 | 504990 | 330 | -84.6 | 504990 | 667 | -89.1 | 504990 | 210 |
| MR_1774414537_3BB94393 | 504990 | 330 | -83.4 | 504990 | 384 | -88.7 | 504990 | 667 | -91.7 | 504990 | 210 |
| MR_1774414537_EE3271B5 | 504990 | 330 | -81.3 | 504990 | 384 | -86.9 | 504990 | 667 | -91.2 | 504990 | 210 |
| MR_1774414537_97176222 | 504990 | 330 | -81.2 | 504990 | 384 | -88.6 | 504990 | 667 | -89.3 | 504990 | 210 |
| MR_1774414537_03692161 | 504990 | 330 | -83.9 | 504990 | 384 | -90.0 | 504990 | 667 | -90.5 | 504990 | 210 |
| MR_1774414537_E0AB5D19 | 504990 | 330 | -81.7 | 504990 | 384 | -90.2 | 504990 | 667 | -90.2 | 504990 | 210 |
| MR_1774414537_79021C8B | 504990 | 384 | -89.7 | 504990 | 330 | -80.9 | 504990 | 667 | -88.6 | 504990 | 210 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 927: `cfd9f8b6-d02...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `cfd9f8b6-d020-47f6-974f-456a67ce08f0` |
| Tag | **single-answer** |
| 정답 | **C5** |
| C5 의미 | Lift the tilt angle  of 3269478_3 by 8 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[927] topology](images/train_0927.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Check test server and transmission issues
- `C2`: Increase A3 Offset threshold for 3255849_2
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3255849_2
- `C4`: Decrease transmission power for 3255849_2
- `C5`: Lift the tilt angle  of 3269478_3 by 8 degrees **← 정답**
- `C6`: Lift the tilt angle of 3255849_2 by 5 degrees
- `C7`: Add neighbor relationship between 3255849_2 and 3232819_1
- `C8`: Increase transmission power for 3255849_2
- `C9`: Add neighbor relationship between 3269478_3 and 3232819_1
- `C10`: Press down the tilt angle of 3255849_2 by 5 degrees
- `C11`: Adjust the azimuth of 3269478_3 by 50 degrees
- `C12`: Increase A3 Offset threshold for 3232819_1
- `C13`: Adjust the azimuth of 3255849_2 by 40 degrees
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Increase transmission power for 3232819_1
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3232819_1
- `C17`: Decrease A3 Offset threshold for 3255849_2
- `C18`: Decrease transmission power for 3232819_1
- `C19`: Decrease A3 Offset threshold for 3232819_1
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3232819_1
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3255849_2
- `C22`: Press down the tilt angle  of 3269478_3 by 8 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.956 | MS1 | 121.4656682507 | 31.1446313497 | 929 | 504990 | -89.37 | 15.12 | 467.96 | 0.03 | 2.70 | 1562 |
| 2024-09-20 22:21:32.416 | MS1 | 121.4656669993 | 31.1446185877 | 929 | 504990 | -91.81 | 14.52 | 318.61 | 0.14 | 2.55 | 1597 |
| 2024-09-20 22:21:33.714 | MS1 | 121.4656671524 | 31.1446209534 | 929 | 504990 | -87.51 | 17.77 | 344.73 | 0.04 | 2.97 | 1560 |
| 2024-09-20 22:21:34.199 | MS1 | 121.4656674245 | 31.1446336648 | 929 | 504990 | -85.30 | 14.28 | 86.83 | 0.17 | 2.14 | 1569 |
| 2024-09-20 22:21:35.438 | MS1 | 121.4656760437 | 31.1446368557 | 929 | 504990 | -88.32 | 17.97 | 97.38 | 0.03 | 2.44 | 1599 |
| 2024-09-20 22:21:36.671 | MS1 | 121.4656602427 | 31.1446243776 | 929 | 504990 | -91.36 | 13.23 | 50.09 | 0.17 | 2.48 | 1598 |
| 2024-09-20 22:21:37.158 | MS1 | 121.4656709718 | 31.1446371201 | 929 | 504990 | -91.32 | 12.03 | 87.55 | 0.14 | 2.39 | 1560 |
| 2024-09-20 22:21:38.586 | MS1 | 121.4656587457 | 31.1446292768 | 929 | 504990 | -89.49 | 12.01 | 90.17 | 0.03 | 2.37 | 1561 |
| 2024-09-20 22:21:39.583 | MS1 | 121.4656712928 | 31.1446214125 | 929 | 504990 | -92.99 | 7.04 | 90.51 | 0.09 | 2.24 | 1592 |
| 2024-09-20 22:21:40.506 | MS1 | 121.4656747821 | 31.1446312861 | 929 | 504990 | -90.61 | 11.94 | 386.85 | 0.05 | 2.52 | 1566 |
| 2024-09-20 22:21:41.733 | MS1 | 121.4656649395 | 31.1446217310 | 929 | 504990 | -92.95 | 10.56 | 597.37 | 0.14 | 2.41 | 1569 |
| 2024-09-20 22:21:42.936 | MS1 | 121.4656600498 | 31.1446368369 | 929 | 504990 | -93.59 | 9.49 | 334.70 | 0.08 | 2.11 | 1587 |

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
| 3211037 | 4 | 121.4646213080 | 31.1530409926 | 209 | 0 | 10 | 30.4 | TDD | 303 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3232819 | 1 | 121.4668761261 | 31.1500161370 | 290 | 3 | 4 | 50.0 | TDD | 927 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3255849 | 2 | 121.4725286930 | 31.1448560704 | 308 | 1 | 1 | 46.7 | TDD | 929 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3269478 | 3 | 121.4660407692 | 31.1554262368 | 288 | 13 | 3 | 21.3 | TDD | 955 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

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
| 2024-09-20 22:21:30.774 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.793 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:30.903 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.903 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.640 | NREventA3 | measId:2;ServCellPCI:36;Ser... |
| 2024-09-20 22:21:37.880 | NRHandoverAttempt | SourcePCI:36;SourceNR-ARFCN... |
| 2024-09-20 22:21:37.910 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.920 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.035 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.035 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3232819 | 1 | 8.5642 | 8.5692 | -114.1768 | 12.1767 | 145.4600 | 0.0093 | 0.0177 |
| 2024_09_20 22:00 | 3255849 | 2 | 79.1697 | 77.3862 | -115.4864 | 16.9889 | 192.9297 | 0.0152 | 0.0159 |
| 2024_09_20 22:00 | 3269478 | 3 | 17.7118 | 6.0507 | -115.0060 | 13.2441 | 151.6750 | 0.0161 | 0.0118 |
| 2024_09_20 22:00 | 3211037 | 4 | 18.9908 | 14.7836 | -117.0466 | 9.9599 | 164.4754 | 0.0004 | 0.0193 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412093_20ADB796 | 504990 | 929 | -85.7 | 504990 | 927 | -92.2 | 504990 | 955 | -92.2 | 504990 | 303 |
| MR_1774412093_1ABB4A40 | 504990 | 929 | -87.1 | 504990 | 927 | -92.6 | 504990 | 955 | -94.6 | 504990 | 303 |
| MR_1774412093_6D90E61D | 504990 | 929 | -85.1 | 504990 | 927 | -92.0 | 504990 | 955 | -94.4 | 504990 | 303 |
| MR_1774412093_4801D126 | 504990 | 929 | -84.8 | 504990 | 927 | -93.4 | 504990 | 955 | -93.1 | 504990 | 303 |
| MR_1774412093_7A678A95 | 504990 | 929 | -86.7 | 504990 | 927 | -92.8 | 504990 | 955 | -92.4 | 504990 | 303 |
| MR_1774412093_EBC6DCA2 | 504990 | 929 | -85.8 | 504990 | 927 | -92.9 | 504990 | 955 | -92.0 | 504990 | 303 |
| MR_1774412093_A45B3AA4 | 504990 | 929 | -85.1 | 504990 | 927 | -92.4 | 504990 | 955 | -93.2 | 504990 | 303 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 928: `82db9ad7-3dd...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `82db9ad7-3dd7-4293-867b-c4b751bd5f4c` |
| Tag | **single-answer** |
| 정답 | **C18** |
| C18 의미 | Lift the tilt angle  of 3268740_1 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[928] topology](images/train_0928.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3229933_3
- `C2`: Increase transmission power for 3229933_3
- `C3`: Add neighbor relationship between 3268740_1 and 3255856_2
- `C4`: Increase transmission power for 3255856_2
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3229933_3
- `C6`: Press down the tilt angle of 3229933_3 by 3 degrees
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3255856_2
- `C8`: Adjust the azimuth of 3229933_3 by 3 degrees
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3255856_2
- `C10`: Decrease transmission power for 3229933_3
- `C11`: Lift the tilt angle of 3229933_3 by 3 degrees
- `C12`: Press down the tilt angle  of 3268740_1 by 10 degrees
- `C13`: Insufficient data; more data is needed for judgment.
- `C14`: Increase A3 Offset threshold for 3255856_2
- `C15`: Adjust the azimuth of 3268740_1 by 50 degrees
- `C16`: Decrease A3 Offset threshold for 3229933_3
- `C17`: Increase A3 Offset threshold for 3229933_3
- `C18`: Lift the tilt angle  of 3268740_1 by 10 degrees **← 정답**
- `C19`: Add neighbor relationship between 3229933_3 and 3255856_2
- `C20`: Decrease A3 Offset threshold for 3255856_2
- `C21`: Decrease transmission power for 3255856_2
- `C22`: Check test server and transmission issues

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.113 | MS1 | 121.4656742350 | 31.1446364458 | 36 | 504990 | -90.36 | 14.67 | 330.93 | 0.02 | 2.99 | 1571 |
| 2024-09-20 22:21:32.722 | MS1 | 121.4656717563 | 31.1446352046 | 36 | 504990 | -85.67 | 16.87 | 367.17 | 0.05 | 2.46 | 1567 |
| 2024-09-20 22:21:33.540 | MS1 | 121.4656669333 | 31.1446266753 | 36 | 504990 | -89.36 | 15.33 | 590.72 | 0.04 | 2.66 | 1573 |
| 2024-09-20 22:21:34.865 | MS1 | 121.4656761899 | 31.1446283792 | 36 | 504990 | -91.03 | 14.99 | 91.50 | 0.19 | 2.95 | 1599 |
| 2024-09-20 22:21:35.189 | MS1 | 121.4656595213 | 31.1446230286 | 36 | 504990 | -89.37 | 17.05 | 61.45 | 0.16 | 2.11 | 1585 |
| 2024-09-20 22:21:36.882 | MS1 | 121.4656641878 | 31.1446214642 | 36 | 504990 | -91.95 | 13.63 | 76.11 | 0.20 | 2.03 | 1598 |
| 2024-09-20 22:21:37.890 | MS1 | 121.4656725499 | 31.1446292457 | 36 | 504990 | -92.76 | 9.75 | 77.32 | 0.02 | 2.48 | 1583 |
| 2024-09-20 22:21:38.928 | MS1 | 121.4656736413 | 31.1446267903 | 36 | 504990 | -91.15 | 8.41 | 49.25 | 0.06 | 2.84 | 1592 |
| 2024-09-20 22:21:39.844 | MS1 | 121.4656653243 | 31.1446181963 | 36 | 504990 | -89.17 | 12.18 | 59.47 | 0.02 | 2.36 | 1582 |
| 2024-09-20 22:21:40.849 | MS1 | 121.4656624977 | 31.1446225318 | 36 | 504990 | -90.48 | 8.59 | 360.61 | 0.10 | 2.56 | 1573 |
| 2024-09-20 22:21:41.404 | MS1 | 121.4656704561 | 31.1446329134 | 36 | 504990 | -92.74 | 11.49 | 503.69 | 0.14 | 2.51 | 1563 |
| 2024-09-20 22:21:42.136 | MS1 | 121.4656620059 | 31.1446326878 | 36 | 504990 | -90.35 | 8.33 | 579.97 | 0.08 | 2.22 | 1567 |

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
| 3229933 | 3 | 121.4685340159 | 31.1518527912 | 202 | 2 | 6 | 21.9 | TDD | 36 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3255856 | 2 | 121.4719318101 | 31.1552552102 | 157 | 15 | 4 | 37.0 | TDD | 741 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3268740 | 1 | 121.4646082517 | 31.1455376181 | 3 | 12 | 12 | 22.4 | TDD | 996 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3271030 | 4 | 121.4702067220 | 31.1519049756 | 231 | 9 | 6 | 26.3 | TDD | 391 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |

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
| 2024-09-20 22:21:30.828 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.845 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:30.948 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.948 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.675 | NREventA3 | measId:2;ServCellPCI:617;Se... |
| 2024-09-20 22:21:37.915 | NRHandoverAttempt | SourcePCI:617;SourceNR-ARFC... |
| 2024-09-20 22:21:37.954 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.969 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.117 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.117 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3268740 | 1 | 11.6283 | 13.6889 | -114.2650 | 11.2326 | 146.5650 | 0.0167 | 0.0025 |
| 2024_09_20 22:00 | 3255856 | 2 | 8.3615 | 9.7800 | -114.9229 | 19.6021 | 97.9723 | 0.0124 | 0.0065 |
| 2024_09_20 22:00 | 3229933 | 3 | 82.0078 | 83.2536 | -115.6232 | 5.0094 | 157.5157 | 0.0074 | 0.0003 |
| 2024_09_20 22:00 | 3271030 | 4 | 7.8455 | 18.9430 | -117.0479 | 13.2051 | 122.1781 | 0.0032 | 0.0066 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414034_3F51A065 | 504990 | 36 | -92.6 | 504990 | 741 | -100.7 | 504990 | 996 | -106.1 | 504990 | 391 |
| MR_1774414034_F6A94E67 | 504990 | 36 | -90.4 | 504990 | 741 | -100.8 | 504990 | 996 | -105.2 | 504990 | 391 |
| MR_1774414034_B938294F | 504990 | 36 | -90.8 | 504990 | 741 | -101.0 | 504990 | 996 | -106.2 | 504990 | 391 |
| MR_1774414034_8EE94280 | 504990 | 36 | -90.8 | 504990 | 741 | -98.5 | 504990 | 996 | -103.7 | 504990 | 391 |
| MR_1774414034_6EF28171 | 504990 | 36 | -91.6 | 504990 | 741 | -101.6 | 504990 | 996 | -105.9 | 504990 | 391 |
| MR_1774414034_E8A4C8FC | 504990 | 36 | -92.8 | 504990 | 741 | -100.2 | 504990 | 996 | -105.7 | 504990 | 391 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 929: `ce479f6a-380...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `ce479f6a-3804-43b9-b055-ba47e8cfd078` |
| Tag | **multiple-answer** |
| 정답 | **C12|C19** |
| C12 의미 | Increase transmission power for 3243959_4 |
| C19 의미 | Adjust the azimuth of 3243959_4 by 30 degrees |
| 패턴 분류 | **P4 Coverage (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[929] topology](images/train_0929.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3266496_1 by 16 degrees
- `C2`: Insufficient data; more data is needed for judgment.
- `C3`: Decrease A3 Offset threshold for 3266496_1
- `C4`: Lift the tilt angle of 3243959_4 by 10 degrees
- `C5`: Press down the tilt angle of 3243959_4 by 10 degrees
- `C6`: Decrease transmission power for 3266496_1
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3243959_4
- `C8`: Lift the tilt angle  of 3266496_1 by 3 degrees
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3266496_1
- `C10`: Increase A3 Offset threshold for 3266496_1
- `C11`: Increase A3 Offset threshold for 3243959_4
- `C12`: Increase transmission power for 3243959_4 **← 정답**
- `C13`: Add neighbor relationship between 3243959_4 and 3266496_1
- `C14`: Check test server and transmission issues
- `C15`: Press down the tilt angle  of 3266496_1 by 3 degrees
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3243959_4
- `C17`: Increase transmission power for 3266496_1
- `C18`: Decrease transmission power for 3243959_4
- `C19`: Adjust the azimuth of 3243959_4 by 30 degrees **← 정답**
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3266496_1
- `C21`: Decrease A3 Offset threshold for 3243959_4
- `C22`: Add neighbor relationship between 3219782_2 and 3266496_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.810 | MS1 | 121.4656638548 | 31.1446356801 | 751 | 504990 | -92.95 | 16.82 | 423.35 | 0.03 | 2.58 | 1563 |
| 2024-09-20 22:21:32.660 | MS1 | 121.4656653942 | 31.1446225770 | 751 | 504990 | -88.24 | 15.96 | 484.61 | 0.19 | 2.32 | 1560 |
| 2024-09-20 22:21:33.322 | MS1 | 121.4656728876 | 31.1446233013 | 751 | 504990 | -86.50 | 13.69 | 380.72 | 0.03 | 2.00 | 1594 |
| 2024-09-20 22:21:34.341 | MS1 | 121.4656647035 | 31.1446326622 | 751 | 504990 | -105.96 | -1.53 | 67.60 | 0.05 | 1.48 | 1578 |
| 2024-09-20 22:21:35.283 | MS1 | 121.4656674225 | 31.1446360593 | 751 | 504990 | -108.51 | -1.53 | 26.34 | 0.10 | 1.35 | 1579 |
| 2024-09-20 22:21:36.737 | MS1 | 121.4656682602 | 31.1446255376 | 751 | 504990 | -102.32 | 0.04 | 48.34 | 0.01 | 1.34 | 1585 |
| 2024-09-20 22:21:37.363 | MS1 | 121.4656666552 | 31.1446343391 | 751 | 504990 | -104.02 | 0.75 | 27.93 | 0.01 | 1.23 | 1596 |
| 2024-09-20 22:21:38.519 | MS1 | 121.4656755240 | 31.1446283597 | 751 | 504990 | -102.69 | 1.98 | 35.66 | 0.20 | 1.27 | 1592 |
| 2024-09-20 22:21:39.571 | MS1 | 121.4656669267 | 31.1446206732 | 751 | 504990 | -106.53 | 0.82 | 16.76 | 0.03 | 1.32 | 1583 |
| 2024-09-20 22:21:40.375 | MS1 | 121.4656601324 | 31.1446230855 | 751 | 504990 | -90.49 | 13.97 | 535.25 | 0.02 | 2.15 | 1590 |
| 2024-09-20 22:21:41.274 | MS1 | 121.4656701301 | 31.1446249023 | 751 | 504990 | -89.63 | 13.58 | 407.15 | 0.04 | 2.20 | 1568 |
| 2024-09-20 22:21:42.294 | MS1 | 121.4656595003 | 31.1446184475 | 751 | 504990 | -87.85 | 15.40 | 420.19 | 0.06 | 2.88 | 1594 |

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
| 3219782 | 2 | 121.4743340536 | 31.1468078095 | 199 | 9 | 1 | 29.9 | TDD | 12 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3243959 | 4 | 121.4645261787 | 31.1485743064 | 136 | 12 | 3 | 31.0 | TDD | 751 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3247085 | 3 | 121.4749437968 | 31.1503137363 | 257 | 1 | 6 | 20.1 | TDD | 430 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3266496 | 1 | 121.4753673687 | 31.1509068630 | 249 | 1 | 5 | 43.5 | TDD | 857 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:31.541 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.559 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.672 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.672 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.900 | NREventA2 | measId:1;ServCellPCI:211;Se... |
| 2024-09-20 22:21:35.004 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3266496 | 1 | 10.4341 | 19.7710 | -114.0195 | 15.9953 | 89.7637 | 0.0060 | 0.0006 |
| 2024_09_20 22:00 | 3219782 | 2 | 17.9204 | 18.7410 | -117.5058 | 18.5887 | 104.3522 | 0.0133 | 0.0099 |
| 2024_09_20 22:00 | 3247085 | 3 | 6.8805 | 18.6739 | -114.3629 | 14.5334 | 101.8586 | 0.0194 | 0.0161 |
| 2024_09_20 22:00 | 3243959 | 4 | 14.5147 | 13.5691 | -114.1238 | 12.5052 | 127.8876 | 0.1273 | 0.0195 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416334_FB1990D4 | 504990 | 751 | -107.8 | 504990 | 857 | -111.6 | 504990 | 12 | -114.5 | 504990 | 430 |
| MR_1774416334_94C74F2D | 504990 | 751 | -107.9 | 504990 | 857 | -108.5 | 504990 | 12 | -112.7 | 504990 | 430 |
| MR_1774416334_B92BA94D | 504990 | 751 | -106.1 | 504990 | 857 | -110.8 | 504990 | 12 | -115.3 | 504990 | 430 |
| MR_1774416334_06A1EAAD | 504990 | 751 | -105.8 | 504990 | 857 | -110.6 | 504990 | 12 | -116.1 | 504990 | 430 |
| MR_1774416334_C80545AE | 504990 | 751 | -107.4 | 504990 | 857 | -111.4 | 504990 | 12 | -115.3 | 504990 | 430 |

> *... 2개 열 생략 (전체 14열)*

---
