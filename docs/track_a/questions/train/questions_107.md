# Track A 문제 분석 — train[1060]~train[1069]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[1060] ~ train[1069] (10개)

## 목차

1. [문제 1060: `33edd430-682...`](#1060) — single-answer, 정답: C6
2. [문제 1061: `62abd7a5-8e2...`](#1061) — single-answer, 정답: C16
3. [문제 1062: `b9e30919-f7c...`](#1062) — single-answer, 정답: C16
4. [문제 1063: `9ac13ba6-f92...`](#1063) — single-answer, 정답: C10
5. [문제 1064: `9fbf0c90-367...`](#1064) — single-answer, 정답: C22
6. [문제 1065: `988bff1a-f0c...`](#1065) — single-answer, 정답: C2
7. [문제 1066: `09dfa577-baf...`](#1066) — single-answer, 정답: C1
8. [문제 1067: `48c8f66e-659...`](#1067) — single-answer, 정답: C6
9. [문제 1068: `0a98495c-99a...`](#1068) — single-answer, 정답: C15
10. [문제 1069: `b39ea4a1-fd0...`](#1069) — single-answer, 정답: C18

---

### 문제 1060: `33edd430-682...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `33edd430-682f-48c0-8bf7-50e00a29a9ba` |
| Tag | **single-answer** |
| 정답 | **C6** |
| C6 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3274436_6 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1060] topology](images/train_1060.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3242726_4 by 5 degrees
- `C2`: Decrease transmission power for 3274436_6
- `C3`: Increase transmission power for 3274436_6
- `C4`: Decrease A3 Offset threshold for 3242726_4
- `C5`: Increase A3 Offset threshold for 3274436_6
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3274436_6 **← 정답**
- `C7`: Adjust the azimuth of 3274436_6 by 1 degrees
- `C8`: Add neighbor relationship between 3274436_6 and 3242726_4
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3274436_6
- `C10`: Lift the tilt angle  of 3242726_4 by 5 degrees
- `C11`: Decrease transmission power for 3242726_4
- `C12`: Press down the tilt angle of 3274436_6 by 6 degrees
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3242726_4
- `C14`: Increase A3 Offset threshold for 3242726_4
- `C15`: Increase transmission power for 3242726_4
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3242726_4
- `C17`: Check test server and transmission issues
- `C18`: Add neighbor relationship between 3240749_11 and 3242726_4
- `C19`: Decrease A3 Offset threshold for 3274436_6
- `C20`: Insufficient data; more data is needed for judgment.
- `C21`: Lift the tilt angle of 3274436_6 by 6 degrees
- `C22`: Adjust the azimuth of 3242726_4 by 33 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.474 | MS1 | 121.4656761538 | 31.1446263217 | 798 | 504990 | -94.41 | 13.54 | 570.73 | 0.17 | 2.25 | 1597 |
| 2024-09-20 22:21:32.963 | MS1 | 121.4656739259 | 31.1446270524 | 283 | 504990 | -94.08 | 11.80 | 353.45 | 0.04 | 2.42 | 1575 |
| 2024-09-20 22:21:33.599 | MS1 | 121.4656664255 | 31.1446191792 | 368 | 504990 | -94.35 | 10.61 | 535.84 | 0.12 | 2.98 | 1588 |
| 2024-09-20 22:21:34.158 | MS1 | 121.4656614965 | 31.1446285480 | 581 | 152650 | -94.95 | 3.49 | 59.39 | 0.11 | 1.74 | 989 |
| 2024-09-20 22:21:35.299 | MS1 | 121.4656746634 | 31.1446329570 | 905 | 152650 | -95.46 | 6.48 | 75.44 | 0.13 | 1.87 | 982 |
| 2024-09-20 22:21:36.868 | MS1 | 121.4656658854 | 31.1446354042 | 467 | 152650 | -89.13 | 4.18 | 57.41 | 0.11 | 1.69 | 992 |
| 2024-09-20 22:21:37.939 | MS1 | 121.4656668969 | 31.1446327038 | 578 | 152650 | -96.73 | 2.42 | 67.77 | 0.16 | 1.59 | 938 |
| 2024-09-20 22:21:38.350 | MS1 | 121.4656606625 | 31.1446254089 | 581 | 152650 | -94.34 | 3.67 | 92.01 | 0.18 | 1.71 | 907 |
| 2024-09-20 22:21:39.250 | MS1 | 121.4656709192 | 31.1446301164 | 905 | 152650 | -95.17 | 7.97 | 74.58 | 0.14 | 1.83 | 926 |
| 2024-09-20 22:21:40.739 | MS1 | 121.4656613982 | 31.1446315175 | 467 | 152650 | -91.58 | 5.49 | 64.90 | 0.04 | 2.39 | 1560 |
| 2024-09-20 22:21:41.158 | MS1 | 121.4656639510 | 31.1446194538 | 578 | 152650 | -89.48 | 5.85 | 74.45 | 0.02 | 2.08 | 1585 |
| 2024-09-20 22:21:42.124 | MS1 | 121.4656628664 | 31.1446324597 | 581 | 152650 | -93.77 | 6.50 | 99.83 | 0.06 | 2.35 | 1584 |

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
| 3210051 | 13 | 121.4727382372 | 31.1530599323 | 55 | 7 | 5 | 13.4 | FDD | 187 | n1 | 152650 | 30M | 4T4R | 24 | 152650 |
| 3225826 | 1 | 121.4700117709 | 31.1559462582 | 246 | 2 | 8 | 9.6 | TDD | 429 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3229478 | 3 | 121.4720267617 | 31.1474695960 | 326 | 7 | 7 | 8.6 | TDD | 501 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3231042 | 10 | 121.4653376235 | 31.1544210957 | 12 | 1 | 6 | 18.6 | FDD | 1006 | n1 | 152650 | 30M | 4T4R | 24 | 152650 |
| 3240749 | 11 | 121.4708054275 | 31.1506398968 | 181 | 12 | 4 | 18.6 | FDD | 467 | n1 | 152650 | 30M | 4T4R | 29 | 152650 |
| 3242726 | 4 | 121.4656189652 | 31.1536328809 | 147 | 4 | 2 | 20.4 | TDD | 154 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3247514 | 9 | 121.4735104016 | 31.1521450302 | 226 | 3 | 9 | 4.9 | FDD | 905 | n1 | 152650 | 30M | 4T4R | 18 | 152650 |
| 3250818 | 7 | 121.4708866574 | 31.1470690364 | 90 | 4 | 9 | 17.2 | FDD | 578 | n1 | 152650 | 30M | 4T4R | 23 | 152650 |
| 3264321 | 2 | 121.4699755863 | 31.1447067474 | 131 | 3 | 8 | 14.2 | TDD | 368 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3273137 | 12 | 121.4661421693 | 31.1442218700 | 152 | 3 | 10 | 17.3 | FDD | 630 | n1 | 152650 | 30M | 4T4R | 15 | 152650 |
| 3274436 | 6 | 121.4693986023 | 31.1533777943 | 201 | 5 | 1 | 9.9 | TDD | 798 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3275429 | 5 | 121.4656277689 | 31.1558008623 | 85 | 3 | 12 | 18.0 | TDD | 283 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3278214 | 8 | 121.4693141081 | 31.1556583921 | 326 | 6 | 2 | 14.5 | FDD | 581 | n1 | 152650 | 30M | 4T4R | 30 | 152650 |

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
| 2024-09-20 22:21:31.013 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.035 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.138 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.138 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.911 | NREventA2 | measId:1;ServCellPCI:242;Se... |
| 2024-09-20 22:21:35.021 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.238 | NREventA5 | measId:3;ServCellPCI:242;Se... |
| 2024-09-20 22:21:35.292 | NRHandoverAttempt | SourcePCI:242;SourceNR-ARFC... |
| 2024-09-20 22:21:35.325 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.339 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:35.467 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.467 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3225826 | 1 | 11.8885 | 9.8164 | -114.9753 | 13.3021 | 112.0243 | 0.0004 | 0.0033 |
| 2024_09_20 22:00 | 3264321 | 2 | 11.9452 | 15.4931 | -116.5265 | 12.5281 | 197.8142 | 0.0024 | 0.0118 |
| 2024_09_20 22:00 | 3229478 | 3 | 12.5075 | 7.7632 | -115.9013 | 18.6509 | 151.5812 | 0.0102 | 0.0098 |
| 2024_09_20 22:00 | 3242726 | 4 | 15.3188 | 12.5040 | -114.1710 | 17.6843 | 85.0175 | 0.0041 | 0.0139 |
| 2024_09_20 22:00 | 3275429 | 5 | 13.9019 | 14.6935 | -117.6425 | 15.6618 | 91.4623 | 0.0068 | 0.0068 |
| 2024_09_20 22:00 | 3274436 | 6 | 7.8164 | 6.3132 | -117.7738 | 6.3558 | 82.1825 | 0.0050 | 0.0139 |
| 2024_09_20 22:00 | 3250818 | 7 | 15.5216 | 9.5528 | -114.1291 | 4.3935 | 40.6562 | 0.0058 | 0.0122 |
| 2024_09_20 22:00 | 3278214 | 8 | 6.1921 | 19.4728 | -114.7190 | 4.3441 | 44.2978 | 0.0049 | 0.0039 |
| 2024_09_20 22:00 | 3247514 | 9 | 10.5534 | 5.2202 | -117.0846 | 4.9271 | 51.6713 | 0.0059 | 0.0094 |
| 2024_09_20 22:00 | 3231042 | 10 | 11.7231 | 16.5243 | -117.6420 | 4.4617 | 33.2399 | 0.0085 | 0.0086 |
| 2024_09_20 22:00 | 3240749 | 11 | 15.1686 | 8.1241 | -116.7340 | 4.9287 | 50.9595 | 0.0084 | 0.0172 |
| 2024_09_20 22:00 | 3273137 | 12 | 13.9048 | 17.1751 | -116.1563 | 3.9521 | 29.3471 | 0.0043 | 0.0127 |
| 2024_09_20 22:00 | 3210051 | 13 | 8.7697 | 5.0125 | -117.0252 | 3.3891 | 39.5925 | 0.0087 | 0.0057 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414213_A4BDF10A | 152650 | 581 | -94.6 | 152650 | 1006 | -97.6 | 152650 | 187 | -103.1 | 152650 | 630 |
| MR_1774414213_D8E26D57 | 504990 | 368 | -93.2 | 504990 | 154 | -90.2 | 504990 | 429 | -99.1 | 504990 | 501 |
| MR_1774414213_1C3C741F | 152650 | 581 | -94.3 | 152650 | 1006 | -97.4 | 152650 | 187 | -104.6 | 152650 | 630 |
| MR_1774414213_26FA9367 | 504990 | 368 | -94.3 | 504990 | 154 | -93.3 | 504990 | 429 | -97.5 | 504990 | 501 |
| MR_1774414213_0AF54258 | 504990 | 368 | -94.2 | 504990 | 154 | -92.2 | 504990 | 429 | -96.6 | 504990 | 501 |
| MR_1774414213_4B5E4E06 | 152650 | 581 | -94.6 | 152650 | 1006 | -96.3 | 152650 | 187 | -103.8 | 152650 | 630 |
| MR_1774414213_0FA93573 | 504990 | 368 | -95.9 | 504990 | 154 | -91.8 | 504990 | 429 | -97.1 | 504990 | 501 |
| MR_1774414213_87F8EFAB | 504990 | 368 | -92.9 | 504990 | 154 | -91.6 | 504990 | 429 | -98.0 | 504990 | 501 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1061: `62abd7a5-8e2...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `62abd7a5-8e29-46a2-876b-fb5625111816` |
| Tag | **single-answer** |
| 정답 | **C16** |
| C16 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3242035_3 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1061] topology](images/train_1061.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3242035_3
- `C2`: Decrease transmission power for 3216488_4
- `C3`: Lift the tilt angle of 3242035_3 by 5 degrees
- `C4`: Adjust the azimuth of 3216488_4 by 50 degrees
- `C5`: Increase transmission power for 3216488_4
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3216488_4
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3216488_4
- `C8`: Add neighbor relationship between 3262347_1 and 3216488_4
- `C9`: Add neighbor relationship between 3242035_3 and 3216488_4
- `C10`: Lift the tilt angle  of 3216488_4 by 3 degrees
- `C11`: Decrease transmission power for 3242035_3
- `C12`: Insufficient data; more data is needed for judgment.
- `C13`: Decrease A3 Offset threshold for 3242035_3
- `C14`: Check test server and transmission issues
- `C15`: Increase A3 Offset threshold for 3242035_3
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3242035_3 **← 정답**
- `C17`: Increase A3 Offset threshold for 3216488_4
- `C18`: Decrease A3 Offset threshold for 3216488_4
- `C19`: Press down the tilt angle of 3242035_3 by 5 degrees
- `C20`: Increase transmission power for 3242035_3
- `C21`: Press down the tilt angle  of 3216488_4 by 3 degrees
- `C22`: Adjust the azimuth of 3242035_3 by 34 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.249 | MS1 | 121.4656640494 | 31.1446351760 | 28 | 504990 | -90.93 | 16.82 | 306.13 | 0.09 | 2.16 | 1580 |
| 2024-09-20 22:21:32.227 | MS1 | 121.4656588022 | 31.1446207172 | 28 | 504990 | -90.28 | 14.64 | 398.13 | 0.15 | 2.68 | 1566 |
| 2024-09-20 22:21:33.549 | MS1 | 121.4656687764 | 31.1446362270 | 28 | 504990 | -89.25 | 16.13 | 453.60 | 0.16 | 2.63 | 1571 |
| 2024-09-20 22:21:34.203 | MS1 | 121.4656632791 | 31.1446278421 | 28 | 504990 | -86.42 | 12.14 | 69.02 | 0.68 | 2.25 | 665 |
| 2024-09-20 22:21:35.628 | MS1 | 121.4656666511 | 31.1446328716 | 28 | 504990 | -88.65 | 14.50 | 77.70 | 0.55 | 2.14 | 537 |
| 2024-09-20 22:21:36.420 | MS1 | 121.4656766632 | 31.1446355110 | 28 | 504990 | -86.49 | 13.33 | 93.70 | 0.52 | 2.36 | 582 |
| 2024-09-20 22:21:37.770 | MS1 | 121.4656779791 | 31.1446295191 | 28 | 504990 | -89.46 | 12.93 | 86.49 | 0.62 | 2.32 | 587 |
| 2024-09-20 22:21:38.986 | MS1 | 121.4656626442 | 31.1446244533 | 28 | 504990 | -91.56 | 7.49 | 86.61 | 0.58 | 2.29 | 536 |
| 2024-09-20 22:21:39.599 | MS1 | 121.4656654995 | 31.1446258644 | 28 | 504990 | -92.79 | 8.75 | 69.77 | 0.53 | 2.37 | 511 |
| 2024-09-20 22:21:40.186 | MS1 | 121.4656732976 | 31.1446202279 | 28 | 504990 | -90.23 | 11.49 | 497.16 | 0.17 | 2.35 | 1589 |
| 2024-09-20 22:21:41.201 | MS1 | 121.4656720736 | 31.1446219518 | 28 | 504990 | -91.48 | 9.86 | 365.19 | 0.11 | 2.21 | 1574 |
| 2024-09-20 22:21:42.915 | MS1 | 121.4656675476 | 31.1446340446 | 28 | 504990 | -93.21 | 12.31 | 343.87 | 0.02 | 2.79 | 1567 |

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
| 3216488 | 4 | 121.4735903214 | 31.1477900074 | 88 | 0 | 11 | 46.9 | TDD | 758 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3235080 | 2 | 121.4723191463 | 31.1533657636 | 27 | 3 | 4 | 35.0 | TDD | 586 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3242035 | 3 | 121.4723845865 | 31.1473891734 | 278 | 3 | 6 | 21.3 | TDD | 28 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3262347 | 1 | 121.4641280781 | 31.1493236948 | 277 | 14 | 5 | 26.7 | TDD | 785 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |

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
| 2024-09-20 22:21:30.915 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.937 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.065 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.065 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.798 | NREventA3 | measId:2;ServCellPCI:281;Se... |
| 2024-09-20 22:21:38.038 | NRHandoverAttempt | SourcePCI:281;SourceNR-ARFC... |
| 2024-09-20 22:21:38.079 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.089 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.201 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.201 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3262347 | 1 | 14.8228 | 15.9891 | -114.7803 | 17.6953 | 91.0579 | 0.0153 | 0.0148 |
| 2024_09_20 22:00 | 3235080 | 2 | 19.1178 | 13.9837 | -116.8185 | 7.6078 | 139.5608 | 0.0047 | 0.0023 |
| 2024_09_20 22:00 | 3242035 | 3 | 8.5319 | 9.4900 | -116.6135 | 13.4776 | 147.5865 | 0.0106 | 0.0092 |
| 2024_09_20 22:00 | 3216488 | 4 | 16.3935 | 11.3451 | -114.6495 | 14.2647 | 160.4075 | 0.0011 | 0.0093 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412609_AC0B5BFF | 504990 | 28 | -85.5 | 504990 | 758 | -93.4 | 504990 | 785 | -92.8 | 504990 | 586 |
| MR_1774412609_34319DE7 | 504990 | 28 | -86.8 | 504990 | 758 | -92.1 | 504990 | 785 | -94.4 | 504990 | 586 |
| MR_1774412609_55D0312A | 504990 | 28 | -86.0 | 504990 | 758 | -93.5 | 504990 | 785 | -91.9 | 504990 | 586 |
| MR_1774412609_8788891A | 504990 | 28 | -86.9 | 504990 | 758 | -93.5 | 504990 | 785 | -90.9 | 504990 | 586 |
| MR_1774412609_DC50366A | 504990 | 28 | -85.7 | 504990 | 758 | -93.1 | 504990 | 785 | -93.6 | 504990 | 586 |
| MR_1774412609_00FB155B | 504990 | 28 | -84.5 | 504990 | 758 | -94.2 | 504990 | 785 | -90.8 | 504990 | 586 |
| MR_1774412609_C94B0866 | 504990 | 28 | -87.7 | 504990 | 758 | -91.7 | 504990 | 785 | -94.2 | 504990 | 586 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1062: `b9e30919-f7c...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `b9e30919-f7c6-45dc-8f53-2aa1798fffc6` |
| Tag | **single-answer** |
| 정답 | **C16** |
| C16 의미 | Add neighbor relationship between 3273798_1 and 3231579_3 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1062] topology](images/train_1062.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment.
- `C2`: Increase A3 Offset threshold for 3273798_1
- `C3`: Decrease A3 Offset threshold for 3231579_3
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3273798_1
- `C5`: Check test server and transmission issues
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3231579_3
- `C7`: Decrease A3 Offset threshold for 3273798_1
- `C8`: Increase transmission power for 3273798_1
- `C9`: Lift the tilt angle  of 3231579_3 by 2 degrees
- `C10`: Press down the tilt angle of 3273798_1 by 10 degrees
- `C11`: Adjust the azimuth of 3273798_1 by 50 degrees
- `C12`: Increase transmission power for 3231579_3
- `C13`: Decrease transmission power for 3273798_1
- `C14`: Add neighbor relationship between 3277086_2 and 3231579_3
- `C15`: Press down the tilt angle  of 3231579_3 by 2 degrees
- `C16`: Add neighbor relationship between 3273798_1 and 3231579_3 **← 정답**
- `C17`: Increase A3 Offset threshold for 3231579_3
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3273798_1
- `C19`: Decrease transmission power for 3231579_3
- `C20`: Adjust the azimuth of 3231579_3 by 38 degrees
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3231579_3
- `C22`: Lift the tilt angle of 3273798_1 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.205 | MS1 | 121.4656751521 | 31.1446216788 | 688 | 504990 | -82.82 | 13.72 | 422.86 | 0.17 | 2.00 | 1600 |
| 2024-09-20 22:21:32.497 | MS1 | 121.4656722629 | 31.1446204227 | 688 | 504990 | -79.73 | 15.75 | 332.00 | 0.08 | 2.18 | 1577 |
| 2024-09-20 22:21:33.401 | MS1 | 121.4656603036 | 31.1446321035 | 688 | 504990 | -83.05 | 14.67 | 314.63 | 0.00 | 2.18 | 1598 |
| 2024-09-20 22:21:34.514 | MS1 | 121.4656686750 | 31.1446205490 | 688 | 504990 | -87.86 | -0.60 | 43.84 | 0.17 | 1.42 | 1572 |
| 2024-09-20 22:21:35.546 | MS1 | 121.4656639791 | 31.1446317616 | 688 | 504990 | -92.48 | -0.01 | 59.89 | 0.12 | 1.08 | 1577 |
| 2024-09-20 22:21:36.457 | MS1 | 121.4656694102 | 31.1446314643 | 688 | 504990 | -89.03 | -2.51 | 39.48 | 0.00 | 1.05 | 1563 |
| 2024-09-20 22:21:37.665 | MS1 | 121.4656626406 | 31.1446225561 | 688 | 504990 | -87.86 | -3.81 | 40.24 | 0.19 | 1.47 | 1593 |
| 2024-09-20 22:21:38.994 | MS1 | 121.4656726384 | 31.1446216242 | 688 | 504990 | -79.19 | 17.40 | 571.78 | 0.19 | 1.09 | 1561 |
| 2024-09-20 22:21:39.758 | MS1 | 121.4656689773 | 31.1446197105 | 688 | 504990 | -83.15 | 16.13 | 438.40 | 0.16 | 1.02 | 1566 |
| 2024-09-20 22:21:40.889 | MS1 | 121.4656776721 | 31.1446362979 | 688 | 504990 | -81.43 | 17.66 | 432.53 | 0.05 | 2.20 | 1575 |
| 2024-09-20 22:21:41.595 | MS1 | 121.4656701414 | 31.1446320372 | 688 | 504990 | -76.92 | 15.07 | 354.16 | 0.19 | 2.97 | 1597 |
| 2024-09-20 22:21:42.319 | MS1 | 121.4656599511 | 31.1446180173 | 688 | 504990 | -79.67 | 13.09 | 505.87 | 0.13 | 2.07 | 1579 |

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
| 3231579 | 3 | 121.4731530259 | 31.1454526868 | 225 | 1 | 6 | 17.0 | TDD | 165 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3242665 | 4 | 121.4675659211 | 31.1458582171 | 162 | 15 | 4 | 18.9 | TDD | 719 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3273798 | 1 | 121.4703294674 | 31.1486975832 | 346 | 15 | 4 | 15.0 | TDD | 688 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3277086 | 2 | 121.4712992959 | 31.1461893853 | 104 | 10 | 1 | 31.2 | TDD | 511 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:30.948 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.967 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.088 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.088 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.784 | NREventA3 | measId:2;ServCellPCI:417;Se... |
| 2024-09-20 22:21:35.784 | NREventA3 | measId:2;ServCellPCI:417;Se... |
| 2024-09-20 22:21:36.784 | NREventA3 | measId:2;ServCellPCI:417;Se... |
| 2024-09-20 22:21:39.284 | NRRRCReestablishAttempt | PCI:417 |
| 2024-09-20 22:21:39.295 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.306 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:39.434 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.434 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3273798 | 1 | 8.7881 | 12.2627 | -116.2685 | 8.4240 | 124.5310 | 0.0139 | 0.1956 |
| 2024_09_20 22:00 | 3277086 | 2 | 17.3381 | 19.5852 | -116.2718 | 18.1054 | 84.9482 | 0.0188 | 0.0082 |
| 2024_09_20 22:00 | 3231579 | 3 | 9.0802 | 9.0624 | -115.1634 | 5.9272 | 95.4684 | 0.0041 | 0.0181 |
| 2024_09_20 22:00 | 3242665 | 4 | 15.4609 | 6.0603 | -115.3552 | 5.3672 | 93.3622 | 0.0057 | 0.0174 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414877_DAB92B9F | 504990 | 165 | -82.2 | 504990 | 688 | -87.0 | 504990 | 511 | -90.2 | 504990 | 719 |
| MR_1774414877_244681FB | 504990 | 688 | -86.1 | 504990 | 165 | -84.3 | 504990 | 511 | -91.0 | 504990 | 719 |
| MR_1774414877_3B869E15 | 504990 | 688 | -88.3 | 504990 | 165 | -81.9 | 504990 | 511 | -89.1 | 504990 | 719 |
| MR_1774414877_BCB1750E | 504990 | 165 | -83.9 | 504990 | 688 | -86.1 | 504990 | 511 | -89.9 | 504990 | 719 |
| MR_1774414877_2D335614 | 504990 | 688 | -86.2 | 504990 | 165 | -81.3 | 504990 | 511 | -88.5 | 504990 | 719 |
| MR_1774414877_7817BB99 | 504990 | 688 | -86.0 | 504990 | 165 | -84.3 | 504990 | 511 | -87.6 | 504990 | 719 |
| MR_1774414877_654442A2 | 504990 | 165 | -84.2 | 504990 | 688 | -87.6 | 504990 | 511 | -88.7 | 504990 | 719 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1063: `9ac13ba6-f92...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `9ac13ba6-f920-4c3e-9d3d-ff8c26c62ce9` |
| Tag | **single-answer** |
| 정답 | **C10** |
| C10 의미 | Decrease A3 Offset threshold for 3261394_2 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1063] topology](images/train_1063.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3261394_2
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3251293_4
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3251293_4
- `C4`: Press down the tilt angle of 3261394_2 by 5 degrees
- `C5`: Add neighbor relationship between 3261394_2 and 3251293_4
- `C6`: Lift the tilt angle of 3261394_2 by 5 degrees
- `C7`: Insufficient data; more data is needed for judgment.
- `C8`: Increase transmission power for 3261394_2
- `C9`: Increase A3 Offset threshold for 3251293_4
- `C10`: Decrease A3 Offset threshold for 3261394_2 **← 정답**
- `C11`: Press down the tilt angle  of 3251293_4 by 10 degrees
- `C12`: Increase A3 Offset threshold for 3261394_2
- `C13`: Adjust the azimuth of 3261394_2 by 50 degrees
- `C14`: Decrease A3 Offset threshold for 3251293_4
- `C15`: Check test server and transmission issues
- `C16`: Lift the tilt angle  of 3251293_4 by 10 degrees
- `C17`: Adjust the azimuth of 3251293_4 by 50 degrees
- `C18`: Increase transmission power for 3251293_4
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3261394_2
- `C20`: Add neighbor relationship between 3279005_1 and 3251293_4
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3261394_2
- `C22`: Decrease transmission power for 3251293_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.631 | MS1 | 121.4656592292 | 31.1446221762 | 506 | 504990 | -77.05 | 17.87 | 431.85 | 0.05 | 2.69 | 1598 |
| 2024-09-20 22:21:32.268 | MS1 | 121.4656669840 | 31.1446379243 | 506 | 504990 | -83.63 | 15.42 | 431.73 | 0.11 | 2.02 | 1567 |
| 2024-09-20 22:21:33.438 | MS1 | 121.4656746776 | 31.1446195162 | 506 | 504990 | -79.51 | 16.13 | 499.81 | 0.11 | 2.13 | 1565 |
| 2024-09-20 22:21:34.842 | MS1 | 121.4656634537 | 31.1446224589 | 506 | 504990 | -86.78 | -1.13 | 52.69 | 0.06 | 1.24 | 1600 |
| 2024-09-20 22:21:35.529 | MS1 | 121.4656582401 | 31.1446224179 | 506 | 504990 | -89.40 | -3.99 | 72.43 | 0.12 | 1.08 | 1578 |
| 2024-09-20 22:21:36.648 | MS1 | 121.4656718417 | 31.1446280418 | 506 | 504990 | -91.86 | -2.91 | 63.69 | 0.02 | 1.17 | 1586 |
| 2024-09-20 22:21:37.771 | MS1 | 121.4656643695 | 31.1446312338 | 506 | 504990 | -89.86 | -2.82 | 72.96 | 0.10 | 1.35 | 1565 |
| 2024-09-20 22:21:38.631 | MS1 | 121.4656722118 | 31.1446293354 | 506 | 504990 | -88.26 | -1.27 | 26.72 | 0.04 | 1.01 | 1578 |
| 2024-09-20 22:21:39.915 | MS1 | 121.4656581752 | 31.1446190536 | 130 | 504990 | -78.34 | 12.92 | 274.10 | 0.07 | 1.25 | 1575 |
| 2024-09-20 22:21:40.905 | MS1 | 121.4656653036 | 31.1446190264 | 130 | 504990 | -76.97 | 16.27 | 515.87 | 0.05 | 2.34 | 1571 |
| 2024-09-20 22:21:41.336 | MS1 | 121.4656661544 | 31.1446305220 | 130 | 504990 | -81.56 | 15.35 | 404.54 | 0.20 | 2.10 | 1565 |
| 2024-09-20 22:21:42.205 | MS1 | 121.4656653389 | 31.1446300475 | 130 | 504990 | -80.87 | 12.83 | 571.19 | 0.11 | 2.79 | 1573 |

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
| 3249252 | 3 | 121.4705478865 | 31.1533258912 | 52 | 9 | 0 | 38.5 | TDD | 403 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3251293 | 4 | 121.4743304291 | 31.1466301229 | 52 | 15 | 3 | 31.7 | TDD | 130 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3261394 | 2 | 121.4750924197 | 31.1556666336 | 336 | 4 | 9 | 18.4 | TDD | 506 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3279005 | 1 | 121.4683084358 | 31.1450719074 | 292 | 5 | 7 | 31.1 | TDD | 73 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

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
| 2024-09-20 22:21:31.408 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.429 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.570 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.570 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.246 | NREventA3 | measId:2;ServCellPCI:411;Se... |
| 2024-09-20 22:21:38.486 | NRHandoverAttempt | SourcePCI:411;SourceNR-ARFC... |
| 2024-09-20 22:21:38.530 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.543 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.693 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.693 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3279005 | 1 | 19.3958 | 14.8148 | -117.1919 | 9.3844 | 109.1232 | 0.0115 | 0.0049 |
| 2024_09_20 22:00 | 3261394 | 2 | 9.6363 | 10.3335 | -117.6959 | 16.8180 | 191.6939 | 0.0106 | 0.1289 |
| 2024_09_20 22:00 | 3249252 | 3 | 6.9837 | 12.4088 | -114.7827 | 16.6475 | 170.5652 | 0.0171 | 0.0124 |
| 2024_09_20 22:00 | 3251293 | 4 | 6.0547 | 19.0733 | -117.3645 | 8.2732 | 96.7943 | 0.0002 | 0.0089 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416554_59E11B37 | 504990 | 506 | -85.6 | 504990 | 130 | -82.8 | 504990 | 73 | -84.3 | 504990 | 403 |
| MR_1774416554_4A9F1834 | 504990 | 506 | -86.0 | 504990 | 130 | -80.2 | 504990 | 73 | -83.8 | 504990 | 403 |
| MR_1774416554_EC989F0C | 504990 | 506 | -88.1 | 504990 | 130 | -80.2 | 504990 | 73 | -83.6 | 504990 | 403 |
| MR_1774416554_B9F72ACA | 504990 | 506 | -86.4 | 504990 | 130 | -81.6 | 504990 | 73 | -81.2 | 504990 | 403 |
| MR_1774416554_AA798F56 | 504990 | 506 | -88.5 | 504990 | 130 | -80.1 | 504990 | 73 | -81.2 | 504990 | 403 |
| MR_1774416554_2DA625DD | 504990 | 506 | -87.4 | 504990 | 130 | -80.4 | 504990 | 73 | -84.0 | 504990 | 403 |
| MR_1774416554_896F9B54 | 504990 | 506 | -86.8 | 504990 | 130 | -81.9 | 504990 | 73 | -82.3 | 504990 | 403 |
| MR_1774416554_41DCBF11 | 504990 | 130 | -83.4 | 504990 | 506 | -87.0 | 504990 | 73 | -83.7 | 504990 | 403 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1064: `9fbf0c90-367...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `9fbf0c90-3670-4bfd-ae7a-485a65e43269` |
| Tag | **single-answer** |
| 정답 | **C22** |
| C22 의미 | Decrease A3 Offset threshold for 3238021_1 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1064] topology](images/train_1064.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3238021_1 by 5 degrees
- `C2`: Increase A3 Offset threshold for 3238021_1
- `C3`: Check test server and transmission issues
- `C4`: Add neighbor relationship between 3269756_3 and 3266236_2
- `C5`: Decrease transmission power for 3266236_2
- `C6`: Insufficient data; more data is needed for judgment.
- `C7`: Adjust the azimuth of 3266236_2 by 50 degrees
- `C8`: Decrease transmission power for 3238021_1
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3238021_1
- `C10`: Increase transmission power for 3238021_1
- `C11`: Increase A3 Offset threshold for 3266236_2
- `C12`: Press down the tilt angle  of 3266236_2 by 10 degrees
- `C13`: Add neighbor relationship between 3238021_1 and 3266236_2
- `C14`: Decrease A3 Offset threshold for 3266236_2
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3238021_1
- `C16`: Lift the tilt angle of 3238021_1 by 5 degrees
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3266236_2
- `C18`: Increase transmission power for 3266236_2
- `C19`: Lift the tilt angle  of 3266236_2 by 10 degrees
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3266236_2
- `C21`: Adjust the azimuth of 3238021_1 by 50 degrees
- `C22`: Decrease A3 Offset threshold for 3238021_1 **← 정답**

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.361 | MS1 | 121.4656761781 | 31.1446310502 | 400 | 504990 | -76.63 | 14.44 | 446.08 | 0.03 | 2.51 | 1598 |
| 2024-09-20 22:21:32.616 | MS1 | 121.4656664441 | 31.1446305949 | 400 | 504990 | -83.68 | 13.64 | 321.55 | 0.11 | 2.19 | 1569 |
| 2024-09-20 22:21:33.622 | MS1 | 121.4656759097 | 31.1446357682 | 400 | 504990 | -75.75 | 15.08 | 544.17 | 0.04 | 2.91 | 1599 |
| 2024-09-20 22:21:34.243 | MS1 | 121.4656736012 | 31.1446250082 | 400 | 504990 | -84.43 | -3.82 | 55.76 | 0.05 | 1.29 | 1599 |
| 2024-09-20 22:21:35.202 | MS1 | 121.4656777423 | 31.1446280432 | 400 | 504990 | -89.26 | -1.02 | 73.72 | 0.03 | 1.01 | 1564 |
| 2024-09-20 22:21:36.962 | MS1 | 121.4656770131 | 31.1446199957 | 400 | 504990 | -88.82 | -3.35 | 63.00 | 0.15 | 1.43 | 1573 |
| 2024-09-20 22:21:37.405 | MS1 | 121.4656652457 | 31.1446363865 | 400 | 504990 | -83.60 | -2.95 | 66.83 | 0.06 | 1.38 | 1560 |
| 2024-09-20 22:21:38.621 | MS1 | 121.4656775879 | 31.1446244570 | 400 | 504990 | -91.03 | -1.11 | 62.98 | 0.04 | 1.17 | 1563 |
| 2024-09-20 22:21:39.644 | MS1 | 121.4656679640 | 31.1446266780 | 690 | 504990 | -81.58 | 14.39 | 294.23 | 0.14 | 1.42 | 1570 |
| 2024-09-20 22:21:40.524 | MS1 | 121.4656723753 | 31.1446273220 | 690 | 504990 | -83.74 | 14.82 | 303.76 | 0.13 | 2.07 | 1595 |
| 2024-09-20 22:21:41.699 | MS1 | 121.4656627006 | 31.1446333435 | 690 | 504990 | -84.23 | 12.90 | 356.16 | 0.10 | 2.74 | 1595 |
| 2024-09-20 22:21:42.543 | MS1 | 121.4656705429 | 31.1446203067 | 690 | 504990 | -80.94 | 15.52 | 339.50 | 0.17 | 2.11 | 1598 |

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
| 3238021 | 1 | 121.4752288320 | 31.1482051351 | 192 | 2 | 1 | 47.5 | TDD | 400 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3266236 | 2 | 121.4749139456 | 31.1443232868 | 145 | 12 | 11 | 40.3 | TDD | 690 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3269756 | 3 | 121.4650435578 | 31.1454541880 | 131 | 15 | 2 | 37.7 | TDD | 475 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3276001 | 4 | 121.4680375096 | 31.1469654816 | 342 | 9 | 10 | 25.8 | TDD | 719 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |

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
| 2024-09-20 22:21:31.507 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.525 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.639 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.639 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.349 | NREventA3 | measId:2;ServCellPCI:94;Ser... |
| 2024-09-20 22:21:38.589 | NRHandoverAttempt | SourcePCI:94;SourceNR-ARFCN... |
| 2024-09-20 22:21:38.626 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.640 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.775 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.775 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3238021 | 1 | 15.9254 | 16.4621 | -116.2579 | 8.9161 | 198.5536 | 0.0163 | 0.1412 |
| 2024_09_20 22:00 | 3266236 | 2 | 18.8596 | 6.8340 | -115.5831 | 11.5166 | 102.7949 | 0.0080 | 0.0121 |
| 2024_09_20 22:00 | 3269756 | 3 | 16.8900 | 7.8219 | -117.5238 | 12.4845 | 176.1060 | 0.0098 | 0.0013 |
| 2024_09_20 22:00 | 3276001 | 4 | 7.8163 | 12.8391 | -115.7650 | 6.4729 | 106.4264 | 0.0092 | 0.0091 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415891_8DFABBC5 | 504990 | 400 | -82.5 | 504990 | 690 | -78.3 | 504990 | 475 | -87.9 | 504990 | 719 |
| MR_1774415891_E788351D | 504990 | 400 | -82.7 | 504990 | 690 | -81.1 | 504990 | 475 | -86.0 | 504990 | 719 |
| MR_1774415891_FE558715 | 504990 | 690 | -79.3 | 504990 | 400 | -84.9 | 504990 | 475 | -87.9 | 504990 | 719 |
| MR_1774415891_890D2067 | 504990 | 690 | -80.5 | 504990 | 400 | -84.4 | 504990 | 475 | -85.7 | 504990 | 719 |
| MR_1774415891_8016014F | 504990 | 400 | -83.2 | 504990 | 690 | -80.9 | 504990 | 475 | -85.9 | 504990 | 719 |
| MR_1774415891_3FC36F42 | 504990 | 400 | -84.5 | 504990 | 690 | -79.1 | 504990 | 475 | -87.9 | 504990 | 719 |
| MR_1774415891_6BEF0695 | 504990 | 690 | -81.1 | 504990 | 400 | -84.1 | 504990 | 475 | -88.2 | 504990 | 719 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1065: `988bff1a-f0c...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `988bff1a-f0cc-41ce-9c24-2923ef3be41d` |
| Tag | **single-answer** |
| 정답 | **C2** |
| C2 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1065] topology](images/train_1065.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3267866_3 by 10 degrees
- `C2`: Check test server and transmission issues **← 정답**
- `C3`: Decrease transmission power for 3213400_2
- `C4`: Add neighbor relationship between 3257901_4 and 3267866_3
- `C5`: Adjust the azimuth of 3213400_2 by 50 degrees
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3267866_3
- `C7`: Increase transmission power for 3213400_2
- `C8`: Adjust the azimuth of 3267866_3 by 50 degrees
- `C9`: Lift the tilt angle of 3213400_2 by 6 degrees
- `C10`: Decrease A3 Offset threshold for 3213400_2
- `C11`: Lift the tilt angle  of 3267866_3 by 10 degrees
- `C12`: Decrease transmission power for 3267866_3
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3267866_3
- `C14`: Add neighbor relationship between 3213400_2 and 3267866_3
- `C15`: Decrease A3 Offset threshold for 3267866_3
- `C16`: Increase A3 Offset threshold for 3267866_3
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3213400_2
- `C18`: Insufficient data; more data is needed for judgment.
- `C19`: Press down the tilt angle of 3213400_2 by 6 degrees
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3213400_2
- `C21`: Increase A3 Offset threshold for 3213400_2
- `C22`: Increase transmission power for 3267866_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.543 | MS1 | 121.4656584446 | 31.1446298174 | 276 | 504990 | -86.68 | 14.20 | 510.92 | 0.01 | 2.65 | 1564 |
| 2024-09-20 22:21:32.950 | MS1 | 121.4656586398 | 31.1446253092 | 276 | 504990 | -87.33 | 12.71 | 436.04 | 0.03 | 2.29 | 1573 |
| 2024-09-20 22:21:33.248 | MS1 | 121.4656671464 | 31.1446292038 | 276 | 504990 | -86.55 | 15.19 | 316.95 | 0.02 | 2.14 | 1574 |
| 2024-09-20 22:21:34.993 | MS1 | 121.4656590322 | 31.1446292742 | 276 | 504990 | -89.94 | 17.96 | 92.76 | 0.11 | 2.79 | 480 |
| 2024-09-20 22:21:35.679 | MS1 | 121.4656648257 | 31.1446364947 | 276 | 504990 | -91.67 | 13.78 | 54.49 | 0.12 | 2.78 | 427 |
| 2024-09-20 22:21:36.964 | MS1 | 121.4656761150 | 31.1446290901 | 276 | 504990 | -91.22 | 13.41 | 57.95 | 0.00 | 2.32 | 488 |
| 2024-09-20 22:21:37.471 | MS1 | 121.4656711071 | 31.1446371720 | 276 | 504990 | -92.30 | 8.53 | 94.86 | 0.09 | 2.09 | 319 |
| 2024-09-20 22:21:38.764 | MS1 | 121.4656744350 | 31.1446326048 | 276 | 504990 | -91.17 | 8.63 | 93.21 | 0.18 | 2.49 | 472 |
| 2024-09-20 22:21:39.370 | MS1 | 121.4656709374 | 31.1446321661 | 276 | 504990 | -91.36 | 9.86 | 106.45 | 0.02 | 2.09 | 343 |
| 2024-09-20 22:21:40.476 | MS1 | 121.4656776054 | 31.1446189866 | 276 | 504990 | -91.65 | 8.96 | 328.64 | 0.05 | 2.53 | 1561 |
| 2024-09-20 22:21:41.357 | MS1 | 121.4656686083 | 31.1446254689 | 276 | 504990 | -92.82 | 10.13 | 298.19 | 0.04 | 2.24 | 1585 |
| 2024-09-20 22:21:42.125 | MS1 | 121.4656641003 | 31.1446318378 | 276 | 504990 | -93.07 | 11.29 | 350.01 | 0.15 | 2.87 | 1585 |

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
| 3213400 | 2 | 121.4649449318 | 31.1524845756 | 281 | 3 | 7 | 40.5 | TDD | 276 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3230444 | 1 | 121.4657662587 | 31.1525378734 | 255 | 0 | 0 | 35.2 | TDD | 184 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3257901 | 4 | 121.4686315713 | 31.1553074134 | 215 | 7 | 11 | 35.1 | TDD | 933 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3267866 | 3 | 121.4746990393 | 31.1494220125 | 355 | 7 | 5 | 49.0 | TDD | 477 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |

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
| 2024-09-20 22:21:31.167 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.186 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.296 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.296 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.004 | NREventA3 | measId:2;ServCellPCI:464;Se... |
| 2024-09-20 22:21:38.244 | NRHandoverAttempt | SourcePCI:464;SourceNR-ARFC... |
| 2024-09-20 22:21:38.288 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.301 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.421 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.421 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3230444 | 1 | 15.7655 | 10.7274 | -117.9057 | 6.2239 | 128.6703 | 0.0159 | 0.0045 |
| 2024_09_20 22:00 | 3213400 | 2 | 8.0444 | 12.7215 | -115.2204 | 11.5894 | 112.1443 | 0.0035 | 0.0052 |
| 2024_09_20 22:00 | 3267866 | 3 | 12.7252 | 15.2401 | -117.8583 | 19.4723 | 191.5549 | 0.0121 | 0.0194 |
| 2024_09_20 22:00 | 3257901 | 4 | 7.3559 | 12.2024 | -117.3680 | 13.1485 | 97.5712 | 0.0007 | 0.0080 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412007_06A9E155 | 504990 | 276 | -90.4 | 504990 | 477 | -92.1 | 504990 | 933 | -102.5 | 504990 | 184 |
| MR_1774412007_7AF48C3E | 504990 | 276 | -91.2 | 504990 | 477 | -94.6 | 504990 | 933 | -101.9 | 504990 | 184 |
| MR_1774412007_6F7A6D63 | 504990 | 276 | -91.2 | 504990 | 477 | -92.4 | 504990 | 933 | -102.4 | 504990 | 184 |
| MR_1774412007_3AF486DB | 504990 | 276 | -91.6 | 504990 | 477 | -92.7 | 504990 | 933 | -104.5 | 504990 | 184 |
| MR_1774412007_86133B2F | 504990 | 276 | -91.3 | 504990 | 477 | -95.1 | 504990 | 933 | -101.9 | 504990 | 184 |
| MR_1774412007_7ECCE39A | 504990 | 276 | -91.5 | 504990 | 477 | -94.1 | 504990 | 933 | -101.8 | 504990 | 184 |
| MR_1774412007_CE96003D | 504990 | 276 | -89.1 | 504990 | 477 | -94.4 | 504990 | 933 | -102.4 | 504990 | 184 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1066: `09dfa577-baf...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `09dfa577-baf0-4359-be13-b85e019fab2b` |
| Tag | **single-answer** |
| 정답 | **C1** |
| C1 의미 | Add neighbor relationship between 3255767_4 and 3224724_3 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1066] topology](images/train_1066.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3255767_4 and 3224724_3 **← 정답**
- `C2`: Increase transmission power for 3224724_3
- `C3`: Check test server and transmission issues
- `C4`: Adjust the azimuth of 3255767_4 by 50 degrees
- `C5`: Decrease A3 Offset threshold for 3255767_4
- `C6`: Press down the tilt angle  of 3224724_3 by 5 degrees
- `C7`: Decrease transmission power for 3255767_4
- `C8`: Lift the tilt angle of 3255767_4 by 8 degrees
- `C9`: Adjust the azimuth of 3224724_3 by 40 degrees
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3224724_3
- `C11`: Insufficient data; more data is needed for judgment.
- `C12`: Increase A3 Offset threshold for 3255767_4
- `C13`: Press down the tilt angle of 3255767_4 by 8 degrees
- `C14`: Increase transmission power for 3255767_4
- `C15`: Add neighbor relationship between 3223242_2 and 3224724_3
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3255767_4
- `C17`: Decrease A3 Offset threshold for 3224724_3
- `C18`: Decrease transmission power for 3224724_3
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3255767_4
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3224724_3
- `C21`: Lift the tilt angle  of 3224724_3 by 5 degrees
- `C22`: Increase A3 Offset threshold for 3224724_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.375 | MS1 | 121.4656740361 | 31.1446219255 | 831 | 504990 | -79.03 | 14.89 | 370.12 | 0.14 | 2.58 | 1599 |
| 2024-09-20 22:21:32.874 | MS1 | 121.4656748529 | 31.1446234689 | 831 | 504990 | -77.58 | 15.71 | 359.90 | 0.07 | 2.33 | 1585 |
| 2024-09-20 22:21:33.748 | MS1 | 121.4656714447 | 31.1446311974 | 831 | 504990 | -77.31 | 14.54 | 303.39 | 0.07 | 2.76 | 1582 |
| 2024-09-20 22:21:34.788 | MS1 | 121.4656684854 | 31.1446228252 | 831 | 504990 | -85.19 | -0.91 | 29.34 | 0.07 | 1.38 | 1564 |
| 2024-09-20 22:21:35.193 | MS1 | 121.4656743590 | 31.1446213209 | 831 | 504990 | -88.34 | -0.49 | 28.30 | 0.05 | 1.15 | 1568 |
| 2024-09-20 22:21:36.995 | MS1 | 121.4656727699 | 31.1446306747 | 831 | 504990 | -86.95 | -1.86 | 55.82 | 0.15 | 1.39 | 1570 |
| 2024-09-20 22:21:37.721 | MS1 | 121.4656704346 | 31.1446278719 | 831 | 504990 | -87.35 | -0.56 | 41.12 | 0.01 | 1.09 | 1585 |
| 2024-09-20 22:21:38.430 | MS1 | 121.4656582064 | 31.1446338751 | 831 | 504990 | -82.72 | 12.23 | 324.09 | 0.05 | 1.07 | 1576 |
| 2024-09-20 22:21:39.913 | MS1 | 121.4656700241 | 31.1446282282 | 831 | 504990 | -80.94 | 16.89 | 425.56 | 0.06 | 1.17 | 1573 |
| 2024-09-20 22:21:40.765 | MS1 | 121.4656696628 | 31.1446233530 | 831 | 504990 | -77.24 | 17.68 | 369.21 | 0.07 | 2.32 | 1597 |
| 2024-09-20 22:21:41.988 | MS1 | 121.4656739544 | 31.1446258762 | 831 | 504990 | -81.94 | 15.25 | 405.87 | 0.16 | 2.42 | 1571 |
| 2024-09-20 22:21:42.566 | MS1 | 121.4656768674 | 31.1446361978 | 831 | 504990 | -83.42 | 15.54 | 325.90 | 0.14 | 2.37 | 1597 |

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
| 3221742 | 1 | 121.4645336377 | 31.1500983474 | 8 | 2 | 4 | 36.7 | TDD | 611 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3223242 | 2 | 121.4694381871 | 31.1552654338 | 86 | 10 | 12 | 39.5 | TDD | 637 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3224724 | 3 | 121.4669663992 | 31.1469806510 | 245 | 2 | 12 | 17.0 | TDD | 134 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3255767 | 4 | 121.4697091266 | 31.1462542247 | 190 | 2 | 8 | 43.2 | TDD | 831 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |

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
| 2024-09-20 22:21:31.354 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.376 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.484 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.484 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.226 | NREventA3 | measId:2;ServCellPCI:449;Se... |
| 2024-09-20 22:21:36.226 | NREventA3 | measId:2;ServCellPCI:449;Se... |
| 2024-09-20 22:21:37.226 | NREventA3 | measId:2;ServCellPCI:449;Se... |
| 2024-09-20 22:21:39.726 | NRRRCReestablishAttempt | PCI:449 |
| 2024-09-20 22:21:39.744 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.754 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:39.885 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.885 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3221742 | 1 | 12.4888 | 15.0469 | -114.1581 | 16.6753 | 186.5207 | 0.0046 | 0.0074 |
| 2024_09_20 22:00 | 3223242 | 2 | 16.7690 | 16.8532 | -114.2056 | 19.3081 | 84.2706 | 0.0173 | 0.0086 |
| 2024_09_20 22:00 | 3224724 | 3 | 17.9979 | 5.7843 | -117.2116 | 6.4194 | 132.0564 | 0.0019 | 0.0052 |
| 2024_09_20 22:00 | 3255767 | 4 | 14.4166 | 9.1013 | -114.7448 | 12.8752 | 136.2899 | 0.0063 | 0.1711 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412477_6D5E02F0 | 504990 | 134 | -81.2 | 504990 | 831 | -85.1 | 504990 | 637 | -84.6 | 504990 | 611 |
| MR_1774412477_7D16E61D | 504990 | 134 | -81.8 | 504990 | 831 | -84.1 | 504990 | 637 | -88.1 | 504990 | 611 |
| MR_1774412477_3209E3A7 | 504990 | 134 | -82.5 | 504990 | 831 | -87.2 | 504990 | 637 | -88.0 | 504990 | 611 |
| MR_1774412477_508B9333 | 504990 | 831 | -83.4 | 504990 | 134 | -81.8 | 504990 | 637 | -86.0 | 504990 | 611 |
| MR_1774412477_A074A505 | 504990 | 134 | -82.6 | 504990 | 831 | -87.1 | 504990 | 637 | -88.4 | 504990 | 611 |
| MR_1774412477_22E12AA9 | 504990 | 831 | -86.4 | 504990 | 134 | -81.6 | 504990 | 637 | -86.8 | 504990 | 611 |
| MR_1774412477_28B05349 | 504990 | 134 | -81.8 | 504990 | 831 | -84.3 | 504990 | 637 | -85.4 | 504990 | 611 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1067: `48c8f66e-659...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `48c8f66e-6590-4be0-807b-0e8c0e74f7ac` |
| Tag | **single-answer** |
| 정답 | **C6** |
| C6 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1067] topology](images/train_1067.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3217541_1 and 3274529_3
- `C2`: Adjust the azimuth of 3274529_3 by 50 degrees
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3217541_1
- `C4`: Adjust the azimuth of 3217541_1 by 50 degrees
- `C5`: Decrease A3 Offset threshold for 3274529_3
- `C6`: Check test server and transmission issues **← 정답**
- `C7`: Increase A3 Offset threshold for 3217541_1
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3217541_1
- `C9`: Add neighbor relationship between 3223673_2 and 3274529_3
- `C10`: Decrease transmission power for 3274529_3
- `C11`: Increase transmission power for 3274529_3
- `C12`: Increase transmission power for 3217541_1
- `C13`: Increase A3 Offset threshold for 3274529_3
- `C14`: Press down the tilt angle of 3217541_1 by 5 degrees
- `C15`: Decrease A3 Offset threshold for 3217541_1
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3274529_3
- `C17`: Press down the tilt angle  of 3274529_3 by 4 degrees
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3274529_3
- `C19`: Decrease transmission power for 3217541_1
- `C20`: Lift the tilt angle of 3217541_1 by 5 degrees
- `C21`: Insufficient data; more data is needed for judgment.
- `C22`: Lift the tilt angle  of 3274529_3 by 4 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.782 | MS1 | 121.4656595526 | 31.1446374494 | 400 | 504990 | -85.81 | 12.58 | 516.51 | 0.09 | 2.14 | 1583 |
| 2024-09-20 22:21:32.327 | MS1 | 121.4656764398 | 31.1446271614 | 400 | 504990 | -87.68 | 13.57 | 448.85 | 0.03 | 2.40 | 1580 |
| 2024-09-20 22:21:33.369 | MS1 | 121.4656683935 | 31.1446255983 | 400 | 504990 | -88.95 | 12.17 | 531.19 | 0.10 | 2.62 | 1598 |
| 2024-09-20 22:21:34.373 | MS1 | 121.4656611405 | 31.1446188700 | 400 | 504990 | -90.55 | 12.45 | 50.95 | 0.01 | 2.19 | 359 |
| 2024-09-20 22:21:35.240 | MS1 | 121.4656778287 | 31.1446191847 | 400 | 504990 | -87.63 | 14.53 | 58.21 | 0.12 | 2.80 | 333 |
| 2024-09-20 22:21:36.677 | MS1 | 121.4656652529 | 31.1446307981 | 400 | 504990 | -89.15 | 15.59 | 73.62 | 0.14 | 2.58 | 342 |
| 2024-09-20 22:21:37.263 | MS1 | 121.4656769137 | 31.1446318381 | 400 | 504990 | -90.24 | 11.91 | 81.64 | 0.07 | 2.78 | 398 |
| 2024-09-20 22:21:38.625 | MS1 | 121.4656676408 | 31.1446326897 | 400 | 504990 | -92.67 | 8.69 | 101.43 | 0.08 | 2.31 | 497 |
| 2024-09-20 22:21:39.314 | MS1 | 121.4656598430 | 31.1446376349 | 400 | 504990 | -90.90 | 9.64 | 100.44 | 0.10 | 2.42 | 371 |
| 2024-09-20 22:21:40.184 | MS1 | 121.4656614547 | 31.1446352308 | 400 | 504990 | -89.57 | 10.04 | 477.16 | 0.14 | 2.02 | 1597 |
| 2024-09-20 22:21:41.613 | MS1 | 121.4656641029 | 31.1446353997 | 400 | 504990 | -90.92 | 8.43 | 401.57 | 0.04 | 2.10 | 1560 |
| 2024-09-20 22:21:42.461 | MS1 | 121.4656632645 | 31.1446307809 | 400 | 504990 | -91.73 | 11.52 | 416.67 | 0.04 | 2.86 | 1588 |

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
| 3217541 | 1 | 121.4747249665 | 31.1442795761 | 103 | 2 | 8 | 40.0 | TDD | 400 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3223673 | 2 | 121.4650546979 | 31.1476956419 | 203 | 6 | 4 | 43.9 | TDD | 201 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3225082 | 4 | 121.4711169242 | 31.1505194238 | 252 | 0 | 10 | 25.7 | TDD | 558 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3274529 | 3 | 121.4653044231 | 31.1526426523 | 29 | 2 | 10 | 31.4 | TDD | 763 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |

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
| 2024-09-20 22:21:30.951 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.973 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.089 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.089 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.766 | NREventA3 | measId:2;ServCellPCI:351;Se... |
| 2024-09-20 22:21:38.006 | NRHandoverAttempt | SourcePCI:351;SourceNR-ARFC... |
| 2024-09-20 22:21:38.041 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.051 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.164 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.164 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3217541 | 1 | 18.4235 | 17.1868 | -116.2591 | 11.9537 | 107.9271 | 0.0098 | 0.0013 |
| 2024_09_20 22:00 | 3223673 | 2 | 11.2252 | 11.7902 | -116.2726 | 15.3601 | 109.5874 | 0.0139 | 0.0073 |
| 2024_09_20 22:00 | 3274529 | 3 | 19.4823 | 17.1835 | -116.9216 | 15.2291 | 195.8036 | 0.0181 | 0.0161 |
| 2024_09_20 22:00 | 3225082 | 4 | 17.3748 | 7.8329 | -117.1885 | 12.8413 | 107.9328 | 0.0029 | 0.0160 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416596_ED1AC325 | 504990 | 400 | -91.2 | 504990 | 763 | -99.6 | 504990 | 201 | -101.1 | 504990 | 558 |
| MR_1774416596_D88529E0 | 504990 | 400 | -90.4 | 504990 | 763 | -97.4 | 504990 | 201 | -101.5 | 504990 | 558 |
| MR_1774416596_A7843975 | 504990 | 400 | -91.6 | 504990 | 763 | -97.0 | 504990 | 201 | -101.9 | 504990 | 558 |
| MR_1774416596_19F752EC | 504990 | 400 | -89.9 | 504990 | 763 | -99.9 | 504990 | 201 | -101.9 | 504990 | 558 |
| MR_1774416596_EE6408EE | 504990 | 400 | -92.1 | 504990 | 763 | -97.5 | 504990 | 201 | -98.8 | 504990 | 558 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1068: `0a98495c-99a...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `0a98495c-99ae-4f6a-93af-b16c8188fe83` |
| Tag | **single-answer** |
| 정답 | **C15** |
| C15 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3274966_2 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1068] topology](images/train_1068.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3274966_2 by 5 degrees
- `C2`: Increase transmission power for 3274966_2
- `C3`: Decrease transmission power for 3274966_2
- `C4`: Decrease transmission power for 3234761_3
- `C5`: Decrease A3 Offset threshold for 3274966_2
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3234761_3
- `C7`: Increase A3 Offset threshold for 3234761_3
- `C8`: Decrease A3 Offset threshold for 3234761_3
- `C9`: Insufficient data; more data is needed for judgment.
- `C10`: Increase transmission power for 3234761_3
- `C11`: Increase A3 Offset threshold for 3274966_2
- `C12`: Check test server and transmission issues
- `C13`: Lift the tilt angle  of 3234761_3 by 9 degrees
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3234761_3
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3274966_2 **← 정답**
- `C16`: Press down the tilt angle  of 3234761_3 by 9 degrees
- `C17`: Add neighbor relationship between 3274966_2 and 3234761_3
- `C18`: Adjust the azimuth of 3234761_3 by 50 degrees
- `C19`: Press down the tilt angle of 3274966_2 by 5 degrees
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3274966_2
- `C21`: Add neighbor relationship between 3210108_1 and 3234761_3
- `C22`: Adjust the azimuth of 3274966_2 by 2 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.457 | MS1 | 121.4656603412 | 31.1446193765 | 129 | 504990 | -86.61 | 15.56 | 470.40 | 0.17 | 2.57 | 1585 |
| 2024-09-20 22:21:32.706 | MS1 | 121.4656744245 | 31.1446180030 | 129 | 504990 | -86.85 | 14.98 | 495.75 | 0.06 | 2.47 | 1594 |
| 2024-09-20 22:21:33.504 | MS1 | 121.4656772991 | 31.1446285608 | 129 | 504990 | -88.07 | 12.08 | 415.17 | 0.08 | 2.10 | 1573 |
| 2024-09-20 22:21:34.333 | MS1 | 121.4656598301 | 31.1446294165 | 129 | 504990 | -87.49 | 12.72 | 66.95 | 0.60 | 2.60 | 660 |
| 2024-09-20 22:21:35.305 | MS1 | 121.4656617875 | 31.1446299299 | 129 | 504990 | -85.57 | 14.50 | 64.39 | 0.59 | 2.66 | 630 |
| 2024-09-20 22:21:36.999 | MS1 | 121.4656633407 | 31.1446333191 | 129 | 504990 | -91.24 | 16.95 | 75.84 | 0.66 | 2.69 | 581 |
| 2024-09-20 22:21:37.683 | MS1 | 121.4656632374 | 31.1446308440 | 129 | 504990 | -92.34 | 8.66 | 90.00 | 0.64 | 2.33 | 656 |
| 2024-09-20 22:21:38.566 | MS1 | 121.4656751235 | 31.1446230229 | 129 | 504990 | -92.52 | 8.08 | 96.34 | 0.58 | 2.12 | 658 |
| 2024-09-20 22:21:39.563 | MS1 | 121.4656595591 | 31.1446275210 | 129 | 504990 | -89.75 | 12.84 | 91.25 | 0.64 | 2.58 | 520 |
| 2024-09-20 22:21:40.652 | MS1 | 121.4656723470 | 31.1446358051 | 129 | 504990 | -92.96 | 12.93 | 505.51 | 0.10 | 2.60 | 1568 |
| 2024-09-20 22:21:41.502 | MS1 | 121.4656744945 | 31.1446235080 | 129 | 504990 | -93.21 | 8.71 | 596.94 | 0.07 | 2.69 | 1596 |
| 2024-09-20 22:21:42.451 | MS1 | 121.4656714354 | 31.1446250399 | 129 | 504990 | -91.81 | 11.00 | 442.15 | 0.20 | 2.67 | 1582 |

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
| 3210108 | 1 | 121.4724539228 | 31.1544389854 | 241 | 0 | 0 | 26.6 | TDD | 120 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3234761 | 3 | 121.4644250339 | 31.1544987525 | 357 | 8 | 4 | 16.6 | TDD | 681 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3252524 | 4 | 121.4712371308 | 31.1457471125 | 289 | 10 | 3 | 23.7 | TDD | 264 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3274966 | 2 | 121.4667544062 | 31.1487291988 | 195 | 3 | 2 | 16.7 | TDD | 129 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:30.955 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.976 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.122 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.122 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.780 | NREventA3 | measId:2;ServCellPCI:811;Se... |
| 2024-09-20 22:21:38.020 | NRHandoverAttempt | SourcePCI:811;SourceNR-ARFC... |
| 2024-09-20 22:21:38.067 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.081 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.227 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.227 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3210108 | 1 | 13.0741 | 6.3663 | -116.3097 | 11.1117 | 133.0788 | 0.0116 | 0.0181 |
| 2024_09_20 22:00 | 3274966 | 2 | 12.2681 | 13.5651 | -116.0401 | 7.1227 | 130.4233 | 0.0067 | 0.0178 |
| 2024_09_20 22:00 | 3234761 | 3 | 12.2929 | 14.0115 | -114.5667 | 15.4146 | 171.5357 | 0.0008 | 0.0059 |
| 2024_09_20 22:00 | 3252524 | 4 | 14.9255 | 13.1245 | -116.1260 | 18.9635 | 165.9257 | 0.0004 | 0.0021 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414499_70BA2E95 | 504990 | 129 | -88.1 | 504990 | 681 | -93.2 | 504990 | 120 | -95.1 | 504990 | 264 |
| MR_1774414499_996C9CCD | 504990 | 129 | -87.4 | 504990 | 681 | -91.7 | 504990 | 120 | -93.7 | 504990 | 264 |
| MR_1774414499_D030CD3F | 504990 | 129 | -85.6 | 504990 | 681 | -92.6 | 504990 | 120 | -94.4 | 504990 | 264 |
| MR_1774414499_DC4B6D67 | 504990 | 129 | -86.3 | 504990 | 681 | -92.4 | 504990 | 120 | -92.9 | 504990 | 264 |
| MR_1774414499_86A31627 | 504990 | 129 | -86.6 | 504990 | 681 | -91.1 | 504990 | 120 | -93.1 | 504990 | 264 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1069: `b39ea4a1-fd0...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `b39ea4a1-fd01-4e0e-816c-bac1ee1e8f10` |
| Tag | **single-answer** |
| 정답 | **C18** |
| C18 의미 | Add neighbor relationship between 3235592_3 and 3232273_1 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1069] topology](images/train_1069.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3232273_1
- `C2`: Increase transmission power for 3235592_3
- `C3`: Decrease A3 Offset threshold for 3232273_1
- `C4`: Decrease A3 Offset threshold for 3235592_3
- `C5`: Press down the tilt angle  of 3232273_1 by 2 degrees
- `C6`: Insufficient data; more data is needed for judgment.
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3235592_3
- `C8`: Check test server and transmission issues
- `C9`: Lift the tilt angle  of 3232273_1 by 2 degrees
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3235592_3
- `C11`: Add neighbor relationship between 3221855_2 and 3232273_1
- `C12`: Press down the tilt angle of 3235592_3 by 5 degrees
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3232273_1
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3232273_1
- `C15`: Adjust the azimuth of 3232273_1 by 48 degrees
- `C16`: Lift the tilt angle of 3235592_3 by 5 degrees
- `C17`: Decrease transmission power for 3235592_3
- `C18`: Add neighbor relationship between 3235592_3 and 3232273_1 **← 정답**
- `C19`: Increase transmission power for 3232273_1
- `C20`: Decrease transmission power for 3232273_1
- `C21`: Adjust the azimuth of 3235592_3 by 50 degrees
- `C22`: Increase A3 Offset threshold for 3235592_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.708 | MS1 | 121.4656716517 | 31.1446377159 | 254 | 504990 | -84.19 | 13.84 | 503.77 | 0.16 | 2.63 | 1580 |
| 2024-09-20 22:21:32.988 | MS1 | 121.4656767055 | 31.1446279865 | 254 | 504990 | -82.91 | 14.74 | 391.23 | 0.13 | 2.76 | 1592 |
| 2024-09-20 22:21:33.907 | MS1 | 121.4656755346 | 31.1446295030 | 254 | 504990 | -77.67 | 12.50 | 406.63 | 0.18 | 2.99 | 1593 |
| 2024-09-20 22:21:34.360 | MS1 | 121.4656620113 | 31.1446208910 | 254 | 504990 | -91.71 | -2.62 | 41.72 | 0.11 | 1.34 | 1596 |
| 2024-09-20 22:21:35.896 | MS1 | 121.4656616306 | 31.1446359198 | 254 | 504990 | -86.44 | -3.98 | 44.66 | 0.04 | 1.01 | 1578 |
| 2024-09-20 22:21:36.246 | MS1 | 121.4656726436 | 31.1446275585 | 254 | 504990 | -86.84 | -0.74 | 59.80 | 0.17 | 1.11 | 1579 |
| 2024-09-20 22:21:37.716 | MS1 | 121.4656664138 | 31.1446210348 | 254 | 504990 | -91.00 | -2.56 | 58.32 | 0.05 | 1.21 | 1592 |
| 2024-09-20 22:21:38.506 | MS1 | 121.4656586341 | 31.1446288735 | 254 | 504990 | -81.66 | 15.89 | 320.64 | 0.03 | 1.18 | 1591 |
| 2024-09-20 22:21:39.174 | MS1 | 121.4656604539 | 31.1446254772 | 254 | 504990 | -81.31 | 17.36 | 399.16 | 0.05 | 1.41 | 1575 |
| 2024-09-20 22:21:40.193 | MS1 | 121.4656726312 | 31.1446196026 | 254 | 504990 | -76.78 | 12.29 | 543.74 | 0.03 | 2.83 | 1592 |
| 2024-09-20 22:21:41.255 | MS1 | 121.4656708021 | 31.1446379467 | 254 | 504990 | -76.93 | 16.69 | 591.77 | 0.14 | 2.59 | 1588 |
| 2024-09-20 22:21:42.318 | MS1 | 121.4656661125 | 31.1446222944 | 254 | 504990 | -84.80 | 13.53 | 498.15 | 0.06 | 2.75 | 1581 |

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
| 3215187 | 4 | 121.4682520346 | 31.1524088920 | 64 | 6 | 3 | 31.1 | TDD | 407 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3221855 | 2 | 121.4657955438 | 31.1468796325 | 69 | 13 | 1 | 35.8 | TDD | 669 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3232273 | 1 | 121.4741712210 | 31.1497604218 | 283 | 1 | 6 | 21.9 | TDD | 860 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3235592 | 3 | 121.4691460291 | 31.1518469032 | 343 | 2 | 9 | 40.1 | TDD | 254 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |

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
| 2024-09-20 22:21:31.108 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.133 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.244 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.244 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.936 | NREventA3 | measId:2;ServCellPCI:542;Se... |
| 2024-09-20 22:21:35.936 | NREventA3 | measId:2;ServCellPCI:542;Se... |
| 2024-09-20 22:21:36.936 | NREventA3 | measId:2;ServCellPCI:542;Se... |
| 2024-09-20 22:21:39.436 | NRRRCReestablishAttempt | PCI:542 |
| 2024-09-20 22:21:39.451 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.464 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:39.584 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.584 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3232273 | 1 | 18.1419 | 17.6400 | -116.3338 | 17.4783 | 93.0931 | 0.0115 | 0.0155 |
| 2024_09_20 22:00 | 3221855 | 2 | 19.4473 | 9.8194 | -115.5728 | 9.8354 | 125.3149 | 0.0125 | 0.0198 |
| 2024_09_20 22:00 | 3235592 | 3 | 16.1321 | 15.8987 | -117.1638 | 5.7685 | 151.9044 | 0.0172 | 0.1643 |
| 2024_09_20 22:00 | 3215187 | 4 | 5.0180 | 12.8692 | -114.7917 | 10.5059 | 90.2803 | 0.0196 | 0.0067 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416982_7F985C44 | 504990 | 860 | -85.8 | 504990 | 254 | -90.4 | 504990 | 669 | -92.5 | 504990 | 407 |
| MR_1774416982_CC0C3778 | 504990 | 254 | -93.5 | 504990 | 860 | -87.8 | 504990 | 669 | -93.4 | 504990 | 407 |
| MR_1774416982_B01FD83F | 504990 | 254 | -91.2 | 504990 | 860 | -86.8 | 504990 | 669 | -93.7 | 504990 | 407 |
| MR_1774416982_8B7392AE | 504990 | 254 | -93.2 | 504990 | 860 | -87.3 | 504990 | 669 | -94.3 | 504990 | 407 |
| MR_1774416982_E8761CF2 | 504990 | 254 | -90.7 | 504990 | 860 | -88.7 | 504990 | 669 | -93.3 | 504990 | 407 |
| MR_1774416982_AC8A52AE | 504990 | 254 | -91.3 | 504990 | 860 | -85.3 | 504990 | 669 | -94.8 | 504990 | 407 |
| MR_1774416982_329BD295 | 504990 | 254 | -93.1 | 504990 | 860 | -85.6 | 504990 | 669 | -93.1 | 504990 | 407 |

> *... 2개 열 생략 (전체 14열)*

---
