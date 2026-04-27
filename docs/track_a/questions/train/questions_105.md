# Track A 문제 분석 — train[1040]~train[1049]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[1040] ~ train[1049] (10개)

## 목차

1. [문제 1040: `a9862e4a-52d...`](#1040) — single-answer, 정답: C9
2. [문제 1041: `b9b66474-362...`](#1041) — single-answer, 정답: C1
3. [문제 1042: `8261351d-e0d...`](#1042) — single-answer, 정답: C12
4. [문제 1043: `6fdedead-b31...`](#1043) — single-answer, 정답: C19
5. [문제 1044: `57130756-1de...`](#1044) — single-answer, 정답: C11
6. [문제 1045: `b79a15a4-65e...`](#1045) — single-answer, 정답: C20
7. [문제 1046: `2a01082b-bc5...`](#1046) — single-answer, 정답: C9
8. [문제 1047: `007bb996-f6a...`](#1047) — single-answer, 정답: C13
9. [문제 1048: `28d2a7cd-028...`](#1048) — single-answer, 정답: C8
10. [문제 1049: `63a79ea1-29f...`](#1049) — single-answer, 정답: C15

---

### 문제 1040: `a9862e4a-52d...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `a9862e4a-52d9-4714-86c3-8d913cc71810` |
| Tag | **single-answer** |
| 정답 | **C9** |
| C9 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3254436_5 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1040] topology](images/train_1040.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3254436_5
- `C2`: Press down the tilt angle of 3254436_5 by 4 degrees
- `C3`: Add neighbor relationship between 3254436_5 and 3246911_2
- `C4`: Adjust the azimuth of 3254436_5 by 42 degrees
- `C5`: Increase A3 Offset threshold for 3246911_2
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3246911_2
- `C7`: Decrease transmission power for 3246911_2
- `C8`: Increase A3 Offset threshold for 3254436_5
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3254436_5 **← 정답**
- `C10`: Increase transmission power for 3246911_2
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3254436_5
- `C12`: Lift the tilt angle of 3254436_5 by 4 degrees
- `C13`: Check test server and transmission issues
- `C14`: Decrease transmission power for 3254436_5
- `C15`: Adjust the azimuth of 3246911_2 by 31 degrees
- `C16`: Decrease A3 Offset threshold for 3246911_2
- `C17`: Decrease A3 Offset threshold for 3254436_5
- `C18`: Insufficient data; more data is needed for judgment.
- `C19`: Lift the tilt angle  of 3246911_2 by 5 degrees
- `C20`: Add neighbor relationship between 3247090_9 and 3246911_2
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3246911_2
- `C22`: Press down the tilt angle  of 3246911_2 by 5 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.437 | MS1 | 121.4656627670 | 31.1446262630 | 530 | 504990 | -95.83 | 11.48 | 489.32 | 0.18 | 2.47 | 1597 |
| 2024-09-20 22:21:32.144 | MS1 | 121.4656601391 | 31.1446291678 | 335 | 504990 | -95.24 | 12.70 | 573.83 | 0.00 | 2.65 | 1584 |
| 2024-09-20 22:21:33.832 | MS1 | 121.4656654273 | 31.1446241276 | 294 | 504990 | -94.65 | 10.80 | 408.87 | 0.05 | 2.46 | 1600 |
| 2024-09-20 22:21:34.557 | MS1 | 121.4656590079 | 31.1446354721 | 835 | 152650 | -89.34 | 4.17 | 78.64 | 0.06 | 1.93 | 903 |
| 2024-09-20 22:21:35.808 | MS1 | 121.4656737796 | 31.1446198063 | 291 | 152650 | -96.96 | 7.51 | 67.45 | 0.18 | 1.88 | 944 |
| 2024-09-20 22:21:36.952 | MS1 | 121.4656750969 | 31.1446285157 | 359 | 152650 | -88.06 | 7.12 | 79.63 | 0.15 | 1.57 | 930 |
| 2024-09-20 22:21:37.877 | MS1 | 121.4656616711 | 31.1446274282 | 351 | 152650 | -95.70 | 3.23 | 80.32 | 0.19 | 1.98 | 988 |
| 2024-09-20 22:21:38.629 | MS1 | 121.4656636057 | 31.1446321750 | 835 | 152650 | -94.39 | 6.97 | 63.58 | 0.11 | 1.88 | 991 |
| 2024-09-20 22:21:39.935 | MS1 | 121.4656764456 | 31.1446267339 | 291 | 152650 | -95.69 | 4.51 | 96.60 | 0.17 | 1.70 | 996 |
| 2024-09-20 22:21:40.264 | MS1 | 121.4656630483 | 31.1446217532 | 359 | 152650 | -89.11 | 7.42 | 89.51 | 0.20 | 2.48 | 1568 |
| 2024-09-20 22:21:41.436 | MS1 | 121.4656770759 | 31.1446328202 | 351 | 152650 | -93.41 | 3.35 | 91.35 | 0.20 | 2.24 | 1579 |
| 2024-09-20 22:21:42.834 | MS1 | 121.4656772594 | 31.1446221796 | 835 | 152650 | -92.82 | 7.75 | 49.53 | 0.19 | 2.12 | 1594 |

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
| 3212668 | 11 | 121.4646692836 | 31.1487667261 | 319 | 0 | 8 | 8.4 | FDD | 282 | n1 | 152650 | 30M | 4T4R | 21 | 152650 |
| 3215377 | 4 | 121.4702912744 | 31.1493267660 | 277 | 5 | 11 | 15.9 | TDD | 593 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3215737 | 12 | 121.4707952033 | 31.1447505076 | 86 | 6 | 7 | 24.7 | FDD | 445 | n1 | 152650 | 30M | 4T4R | 29 | 152650 |
| 3232182 | 1 | 121.4653368489 | 31.1455186762 | 273 | 2 | 12 | 2.0 | TDD | 294 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3232504 | 10 | 121.4658741789 | 31.1476400246 | 262 | 11 | 4 | 1.2 | FDD | 466 | n1 | 152650 | 30M | 4T4R | 13 | 152650 |
| 3234402 | 7 | 121.4647468465 | 31.1454832243 | 231 | 6 | 6 | 18.9 | FDD | 291 | n1 | 152650 | 30M | 4T4R | 10 | 152650 |
| 3236569 | 6 | 121.4733754310 | 31.1443725478 | 120 | 5 | 1 | 6.5 | TDD | 793 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3246911 | 2 | 121.4669469853 | 31.1538905646 | 218 | 4 | 2 | 14.4 | TDD | 937 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3247090 | 9 | 121.4723625372 | 31.1558665949 | 49 | 2 | 8 | 17.9 | FDD | 359 | n1 | 152650 | 30M | 4T4R | 26 | 152650 |
| 3251539 | 3 | 121.4674295421 | 31.1445108289 | 290 | 13 | 0 | 15.3 | TDD | 335 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3254436 | 5 | 121.4667079034 | 31.1552398874 | 227 | 3 | 4 | 20.4 | TDD | 530 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3258640 | 8 | 121.4698402811 | 31.1495917273 | 109 | 5 | 8 | 24.4 | FDD | 835 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |
| 3263191 | 13 | 121.4749083740 | 31.1530656571 | 355 | 12 | 4 | 19.1 | FDD | 351 | n1 | 152650 | 30M | 4T4R | 20 | 152650 |

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
| 2024-09-20 22:21:31.330 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.353 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.476 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.476 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.165 | NREventA2 | measId:1;ServCellPCI:518;Se... |
| 2024-09-20 22:21:35.311 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.579 | NREventA5 | measId:3;ServCellPCI:518;Se... |
| 2024-09-20 22:21:35.613 | NRHandoverAttempt | SourcePCI:518;SourceNR-ARFC... |
| 2024-09-20 22:21:35.663 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.677 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:35.804 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.804 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3232182 | 1 | 12.6790 | 8.9243 | -117.7624 | 5.1854 | 110.4818 | 0.0135 | 0.0071 |
| 2024_09_20 22:00 | 3246911 | 2 | 6.0985 | 18.0356 | -114.9406 | 14.2743 | 123.8425 | 0.0065 | 0.0058 |
| 2024_09_20 22:00 | 3251539 | 3 | 13.6255 | 12.0978 | -114.3826 | 19.1134 | 139.7168 | 0.0097 | 0.0099 |
| 2024_09_20 22:00 | 3215377 | 4 | 17.6436 | 12.6713 | -115.3666 | 11.8379 | 146.8458 | 0.0052 | 0.0199 |
| 2024_09_20 22:00 | 3254436 | 5 | 14.5770 | 19.8358 | -116.9993 | 19.5717 | 86.8052 | 0.0160 | 0.0035 |
| 2024_09_20 22:00 | 3236569 | 6 | 14.0890 | 11.7603 | -114.2214 | 11.5486 | 105.5316 | 0.0145 | 0.0073 |
| 2024_09_20 22:00 | 3234402 | 7 | 15.3472 | 12.5906 | -114.1337 | 3.2754 | 52.6757 | 0.0140 | 0.0193 |
| 2024_09_20 22:00 | 3258640 | 8 | 5.8222 | 10.7704 | -117.6395 | 3.4640 | 59.0438 | 0.0065 | 0.0176 |
| 2024_09_20 22:00 | 3247090 | 9 | 9.9194 | 9.6741 | -117.7316 | 3.7969 | 58.2703 | 0.0159 | 0.0135 |
| 2024_09_20 22:00 | 3232504 | 10 | 17.6963 | 7.2849 | -114.0980 | 3.1637 | 20.2165 | 0.0195 | 0.0056 |
| 2024_09_20 22:00 | 3212668 | 11 | 16.1797 | 7.5900 | -115.3180 | 4.9221 | 59.4566 | 0.0020 | 0.0015 |
| 2024_09_20 22:00 | 3215737 | 12 | 11.7555 | 12.6077 | -117.6039 | 3.1135 | 32.8863 | 0.0003 | 0.0176 |
| 2024_09_20 22:00 | 3263191 | 13 | 10.5638 | 17.4119 | -114.9412 | 3.0239 | 52.9586 | 0.0076 | 0.0083 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414721_67917C26 | 504990 | 294 | -95.7 | 504990 | 937 | -93.5 | 504990 | 793 | -96.1 | 504990 | 593 |
| MR_1774414721_477873CB | 152650 | 835 | -88.1 | 152650 | 282 | -94.3 | 152650 | 466 | -98.5 | 152650 | 445 |
| MR_1774414721_F5221ED1 | 152650 | 835 | -88.8 | 152650 | 282 | -96.6 | 152650 | 466 | -98.6 | 152650 | 445 |
| MR_1774414721_4D2BA67E | 152650 | 835 | -89.9 | 152650 | 282 | -96.1 | 152650 | 466 | -97.5 | 152650 | 445 |
| MR_1774414721_837DE830 | 152650 | 835 | -88.2 | 152650 | 282 | -95.9 | 152650 | 466 | -95.5 | 152650 | 445 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1041: `b9b66474-362...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `b9b66474-362a-430c-bf64-5b1dd49254a0` |
| Tag | **single-answer** |
| 정답 | **C1** |
| C1 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3217631_3 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1041] topology](images/train_1041.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3217631_3 **← 정답**
- `C2`: Decrease transmission power for 3217631_3
- `C3`: Lift the tilt angle  of 3225218_4 by 4 degrees
- `C4`: Insufficient data; more data is needed for judgment.
- `C5`: Add neighbor relationship between 3217631_3 and 3225218_4
- `C6`: Increase transmission power for 3225218_4
- `C7`: Decrease A3 Offset threshold for 3225218_4
- `C8`: Decrease transmission power for 3225218_4
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3225218_4
- `C10`: Add neighbor relationship between 3278271_12 and 3225218_4
- `C11`: Adjust the azimuth of 3217631_3 by 8 degrees
- `C12`: Check test server and transmission issues
- `C13`: Press down the tilt angle  of 3225218_4 by 4 degrees
- `C14`: Lift the tilt angle of 3217631_3 by 6 degrees
- `C15`: Increase A3 Offset threshold for 3217631_3
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3217631_3
- `C17`: Decrease A3 Offset threshold for 3217631_3
- `C18`: Adjust the azimuth of 3225218_4 by 45 degrees
- `C19`: Increase transmission power for 3217631_3
- `C20`: Increase A3 Offset threshold for 3225218_4
- `C21`: Press down the tilt angle of 3217631_3 by 6 degrees
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3225218_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.853 | MS1 | 121.4656613951 | 31.1446275937 | 233 | 504990 | -94.92 | 10.63 | 427.69 | 0.16 | 2.70 | 1570 |
| 2024-09-20 22:21:32.843 | MS1 | 121.4656664418 | 31.1446219360 | 548 | 504990 | -93.46 | 10.36 | 603.91 | 0.08 | 2.22 | 1564 |
| 2024-09-20 22:21:33.295 | MS1 | 121.4656611110 | 31.1446216417 | 712 | 504990 | -95.67 | 14.10 | 424.83 | 0.16 | 2.32 | 1577 |
| 2024-09-20 22:21:34.709 | MS1 | 121.4656732154 | 31.1446357121 | 1005 | 152650 | -87.80 | 2.62 | 98.09 | 0.20 | 1.81 | 991 |
| 2024-09-20 22:21:35.688 | MS1 | 121.4656630944 | 31.1446324263 | 862 | 152650 | -93.70 | 4.06 | 76.55 | 0.16 | 1.95 | 914 |
| 2024-09-20 22:21:36.639 | MS1 | 121.4656729291 | 31.1446268105 | 443 | 152650 | -90.98 | 7.10 | 90.02 | 0.13 | 1.60 | 958 |
| 2024-09-20 22:21:37.242 | MS1 | 121.4656712196 | 31.1446349093 | 838 | 152650 | -90.06 | 3.06 | 68.11 | 0.15 | 1.61 | 938 |
| 2024-09-20 22:21:38.782 | MS1 | 121.4656679112 | 31.1446358951 | 1005 | 152650 | -96.64 | 5.77 | 66.18 | 0.06 | 1.84 | 964 |
| 2024-09-20 22:21:39.203 | MS1 | 121.4656670295 | 31.1446294797 | 862 | 152650 | -90.63 | 4.64 | 61.37 | 0.08 | 1.67 | 957 |
| 2024-09-20 22:21:40.861 | MS1 | 121.4656748412 | 31.1446333553 | 443 | 152650 | -92.88 | 6.49 | 67.80 | 0.02 | 2.38 | 1578 |
| 2024-09-20 22:21:41.522 | MS1 | 121.4656676143 | 31.1446226328 | 838 | 152650 | -94.54 | 7.85 | 87.52 | 0.10 | 2.68 | 1570 |
| 2024-09-20 22:21:42.270 | MS1 | 121.4656759915 | 31.1446294252 | 1005 | 152650 | -90.99 | 3.92 | 60.83 | 0.07 | 2.93 | 1594 |

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
| 3210776 | 2 | 121.4727366573 | 31.1446016372 | 359 | 15 | 11 | 27.7 | TDD | 712 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3212680 | 7 | 121.4647686273 | 31.1503277686 | 286 | 14 | 3 | 29.2 | FDD | 838 | n1 | 152650 | 30M | 4T4R | 25 | 152650 |
| 3217631 | 3 | 121.4673216806 | 31.1520447615 | 183 | 4 | 1 | 27.3 | TDD | 233 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3222723 | 13 | 121.4748851439 | 31.1476708924 | 34 | 6 | 12 | 5.2 | FDD | 862 | n1 | 152650 | 30M | 4T4R | 14 | 152650 |
| 3225218 | 4 | 121.4717105283 | 31.1488459250 | 276 | 3 | 6 | 7.2 | TDD | 425 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3228956 | 1 | 121.4646131038 | 31.1495107191 | 31 | 3 | 6 | 4.3 | TDD | 548 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3231649 | 6 | 121.4665328193 | 31.1504281635 | 253 | 0 | 10 | 5.4 | TDD | 701 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3239674 | 11 | 121.4680340340 | 31.1481315607 | 283 | 8 | 12 | 20.8 | FDD | 282 | n1 | 152650 | 30M | 4T4R | 15 | 152650 |
| 3250749 | 9 | 121.4748855727 | 31.1539138116 | 231 | 1 | 12 | 1.4 | FDD | 557 | n1 | 152650 | 30M | 4T4R | 24 | 152650 |
| 3257897 | 10 | 121.4702342369 | 31.1508009779 | 132 | 4 | 5 | 2.9 | FDD | 822 | n1 | 152650 | 30M | 4T4R | 24 | 152650 |
| 3263670 | 8 | 121.4655502442 | 31.1441075401 | 331 | 10 | 4 | 24.5 | FDD | 1005 | n1 | 152650 | 30M | 4T4R | 30 | 152650 |
| 3278271 | 12 | 121.4691101777 | 31.1537844303 | 104 | 14 | 2 | 18.0 | FDD | 443 | n1 | 152650 | 30M | 4T4R | 10 | 152650 |
| 3278321 | 5 | 121.4666996627 | 31.1483211039 | 158 | 1 | 8 | 25.2 | TDD | 340 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |

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
| 2024-09-20 22:21:31.034 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.049 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.198 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.198 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.925 | NREventA2 | measId:1;ServCellPCI:185;Se... |
| 2024-09-20 22:21:35.029 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.315 | NREventA5 | measId:3;ServCellPCI:185;Se... |
| 2024-09-20 22:21:35.386 | NRHandoverAttempt | SourcePCI:185;SourceNR-ARFC... |
| 2024-09-20 22:21:35.407 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.421 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:35.538 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.538 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3228956 | 1 | 8.3229 | 18.2630 | -117.4457 | 7.8076 | 99.5276 | 0.0037 | 0.0096 |
| 2024_09_20 22:00 | 3210776 | 2 | 15.9280 | 10.2514 | -116.4541 | 6.7746 | 130.4728 | 0.0166 | 0.0179 |
| 2024_09_20 22:00 | 3217631 | 3 | 13.9764 | 7.7772 | -114.1142 | 17.7588 | 110.2458 | 0.0026 | 0.0098 |
| 2024_09_20 22:00 | 3225218 | 4 | 11.0710 | 5.9838 | -117.5950 | 5.3684 | 124.0209 | 0.0041 | 0.0086 |
| 2024_09_20 22:00 | 3278321 | 5 | 14.2712 | 5.3311 | -114.4334 | 10.2021 | 88.9381 | 0.0191 | 0.0178 |
| 2024_09_20 22:00 | 3231649 | 6 | 13.7201 | 10.3428 | -116.9203 | 12.2973 | 199.6136 | 0.0192 | 0.0161 |
| 2024_09_20 22:00 | 3212680 | 7 | 7.6429 | 17.7425 | -116.4698 | 3.3542 | 48.8758 | 0.0189 | 0.0159 |
| 2024_09_20 22:00 | 3263670 | 8 | 19.8533 | 6.6714 | -114.2111 | 3.5117 | 29.7569 | 0.0061 | 0.0107 |
| 2024_09_20 22:00 | 3250749 | 9 | 18.6931 | 16.4288 | -114.6877 | 3.3204 | 39.1885 | 0.0132 | 0.0058 |
| 2024_09_20 22:00 | 3257897 | 10 | 13.5992 | 14.2886 | -115.5909 | 4.3610 | 48.1991 | 0.0138 | 0.0151 |
| 2024_09_20 22:00 | 3239674 | 11 | 11.0009 | 18.6430 | -115.6829 | 4.5580 | 47.8453 | 0.0137 | 0.0135 |
| 2024_09_20 22:00 | 3278271 | 12 | 7.8724 | 11.2267 | -114.0577 | 3.7738 | 38.9728 | 0.0036 | 0.0106 |
| 2024_09_20 22:00 | 3222723 | 13 | 11.0135 | 13.9125 | -115.3871 | 3.8266 | 53.2327 | 0.0108 | 0.0104 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415158_A997B504 | 504990 | 712 | -97.5 | 504990 | 425 | -100.2 | 504990 | 701 | -101.4 | 504990 | 340 |
| MR_1774415158_5783F95E | 504990 | 712 | -96.3 | 504990 | 425 | -99.7 | 504990 | 701 | -101.1 | 504990 | 340 |
| MR_1774415158_A3D303D0 | 504990 | 712 | -94.9 | 504990 | 425 | -99.9 | 504990 | 701 | -98.0 | 504990 | 340 |
| MR_1774415158_CA629EA3 | 152650 | 1005 | -87.1 | 152650 | 822 | -92.6 | 152650 | 557 | -96.2 | 152650 | 282 |
| MR_1774415158_EFED22CD | 504990 | 712 | -96.7 | 504990 | 425 | -97.5 | 504990 | 701 | -101.2 | 504990 | 340 |
| MR_1774415158_A4524ED6 | 152650 | 1005 | -88.3 | 152650 | 822 | -92.1 | 152650 | 557 | -94.9 | 152650 | 282 |
| MR_1774415158_E22245D0 | 152650 | 1005 | -88.9 | 152650 | 822 | -91.6 | 152650 | 557 | -95.9 | 152650 | 282 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1042: `8261351d-e0d...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `8261351d-e0d7-445b-8139-f9660a34c9e5` |
| Tag | **single-answer** |
| 정답 | **C12** |
| C12 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1042] topology](images/train_1042.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3267395_1
- `C2`: Adjust the azimuth of 3276271_3 by 37 degrees
- `C3`: Add neighbor relationship between 3256887_4 and 3276271_3
- `C4`: Lift the tilt angle of 3267395_1 by 6 degrees
- `C5`: Insufficient data; more data is needed for judgment.
- `C6`: Decrease A3 Offset threshold for 3276271_3
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3276271_3
- `C8`: Increase A3 Offset threshold for 3267395_1
- `C9`: Adjust the azimuth of 3267395_1 by 42 degrees
- `C10`: Increase A3 Offset threshold for 3276271_3
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3276271_3
- `C12`: Check test server and transmission issues **← 정답**
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3267395_1
- `C14`: Decrease transmission power for 3276271_3
- `C15`: Press down the tilt angle of 3267395_1 by 6 degrees
- `C16`: Decrease A3 Offset threshold for 3267395_1
- `C17`: Increase transmission power for 3267395_1
- `C18`: Increase transmission power for 3276271_3
- `C19`: Add neighbor relationship between 3267395_1 and 3276271_3
- `C20`: Lift the tilt angle  of 3276271_3 by 6 degrees
- `C21`: Press down the tilt angle  of 3276271_3 by 6 degrees
- `C22`: Decrease transmission power for 3267395_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.916 | MS1 | 121.4656732082 | 31.1446254296 | 255 | 504990 | -85.52 | 14.66 | 403.23 | 0.19 | 2.70 | 1592 |
| 2024-09-20 22:21:32.451 | MS1 | 121.4656666197 | 31.1446357450 | 255 | 504990 | -91.86 | 12.86 | 341.99 | 0.10 | 2.31 | 1584 |
| 2024-09-20 22:21:33.914 | MS1 | 121.4656580569 | 31.1446205420 | 255 | 504990 | -88.78 | 16.99 | 338.16 | 0.01 | 2.29 | 1574 |
| 2024-09-20 22:21:34.723 | MS1 | 121.4656638539 | 31.1446256087 | 255 | 504990 | -86.87 | 15.05 | 86.93 | 0.05 | 2.67 | 486 |
| 2024-09-20 22:21:35.495 | MS1 | 121.4656716548 | 31.1446364685 | 255 | 504990 | -90.17 | 16.94 | 89.99 | 0.12 | 2.51 | 443 |
| 2024-09-20 22:21:36.612 | MS1 | 121.4656702148 | 31.1446367737 | 255 | 504990 | -88.47 | 17.37 | 86.82 | 0.02 | 2.41 | 490 |
| 2024-09-20 22:21:37.648 | MS1 | 121.4656623835 | 31.1446376853 | 255 | 504990 | -90.24 | 10.24 | 62.66 | 0.12 | 2.88 | 304 |
| 2024-09-20 22:21:38.732 | MS1 | 121.4656775566 | 31.1446342218 | 255 | 504990 | -91.26 | 9.57 | 62.07 | 0.13 | 2.05 | 339 |
| 2024-09-20 22:21:39.667 | MS1 | 121.4656627719 | 31.1446271213 | 255 | 504990 | -91.03 | 7.34 | 57.78 | 0.15 | 2.70 | 420 |
| 2024-09-20 22:21:40.347 | MS1 | 121.4656763566 | 31.1446332531 | 255 | 504990 | -93.75 | 12.43 | 512.14 | 0.01 | 2.17 | 1587 |
| 2024-09-20 22:21:41.831 | MS1 | 121.4656640894 | 31.1446307201 | 255 | 504990 | -90.42 | 11.52 | 601.48 | 0.01 | 2.62 | 1598 |
| 2024-09-20 22:21:42.980 | MS1 | 121.4656613292 | 31.1446294085 | 255 | 504990 | -92.34 | 12.30 | 429.62 | 0.06 | 2.11 | 1577 |

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
| 3256887 | 4 | 121.4704007584 | 31.1520291560 | 94 | 1 | 2 | 38.6 | TDD | 999 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3262403 | 2 | 121.4667609033 | 31.1511680622 | 312 | 2 | 6 | 46.5 | TDD | 690 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3267395 | 1 | 121.4726453533 | 31.1442394408 | 232 | 4 | 0 | 25.3 | TDD | 255 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3276271 | 3 | 121.4708532647 | 31.1479480584 | 270 | 3 | 1 | 27.7 | TDD | 786 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |

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
| 2024-09-20 22:21:30.760 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.779 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:30.879 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.879 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.605 | NREventA3 | measId:2;ServCellPCI:162;Se... |
| 2024-09-20 22:21:37.845 | NRHandoverAttempt | SourcePCI:162;SourceNR-ARFC... |
| 2024-09-20 22:21:37.879 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.894 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.042 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.042 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3267395 | 1 | 10.7799 | 5.2847 | -115.5168 | 9.0002 | 157.1057 | 0.0072 | 0.0073 |
| 2024_09_20 22:00 | 3262403 | 2 | 15.4895 | 5.3562 | -117.4361 | 5.1198 | 113.2232 | 0.0015 | 0.0141 |
| 2024_09_20 22:00 | 3276271 | 3 | 11.7741 | 7.8609 | -117.1084 | 9.0308 | 172.8432 | 0.0127 | 0.0033 |
| 2024_09_20 22:00 | 3256887 | 4 | 13.3858 | 9.6796 | -115.6265 | 15.9336 | 170.2726 | 0.0041 | 0.0136 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412957_8355E6A0 | 504990 | 255 | -87.7 | 504990 | 786 | -88.0 | 504990 | 999 | -100.4 | 504990 | 690 |
| MR_1774412957_3D56EB12 | 504990 | 255 | -85.9 | 504990 | 786 | -89.3 | 504990 | 999 | -100.8 | 504990 | 690 |
| MR_1774412957_9E0A2C68 | 504990 | 255 | -88.8 | 504990 | 786 | -88.4 | 504990 | 999 | -100.5 | 504990 | 690 |
| MR_1774412957_614C72F4 | 504990 | 255 | -88.6 | 504990 | 786 | -87.8 | 504990 | 999 | -99.6 | 504990 | 690 |
| MR_1774412957_35F68745 | 504990 | 255 | -86.4 | 504990 | 786 | -88.7 | 504990 | 999 | -99.3 | 504990 | 690 |
| MR_1774412957_576A940E | 504990 | 255 | -86.3 | 504990 | 786 | -88.0 | 504990 | 999 | -99.5 | 504990 | 690 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1043: `6fdedead-b31...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `6fdedead-b315-4d99-bb30-c335797c3bf4` |
| Tag | **single-answer** |
| 정답 | **C19** |
| C19 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3276012_3 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1043] topology](images/train_1043.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3253757_2 and 3231913_1
- `C2`: Adjust the azimuth of 3231913_1 by 50 degrees
- `C3`: Lift the tilt angle  of 3231913_1 by 4 degrees
- `C4`: Decrease transmission power for 3276012_3
- `C5`: Insufficient data; more data is needed for judgment.
- `C6`: Decrease A3 Offset threshold for 3231913_1
- `C7`: Increase A3 Offset threshold for 3276012_3
- `C8`: Press down the tilt angle  of 3231913_1 by 4 degrees
- `C9`: Press down the tilt angle of 3276012_3 by 5 degrees
- `C10`: Decrease transmission power for 3231913_1
- `C11`: Add neighbor relationship between 3276012_3 and 3231913_1
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3231913_1
- `C13`: Decrease A3 Offset threshold for 3276012_3
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3276012_3
- `C15`: Lift the tilt angle of 3276012_3 by 5 degrees
- `C16`: Increase transmission power for 3276012_3
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3231913_1
- `C18`: Increase A3 Offset threshold for 3231913_1
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3276012_3 **← 정답**
- `C20`: Increase transmission power for 3231913_1
- `C21`: Check test server and transmission issues
- `C22`: Adjust the azimuth of 3276012_3 by 25 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.286 | MS1 | 121.4656772180 | 31.1446240336 | 1004 | 504990 | -87.46 | 14.38 | 522.47 | 0.19 | 2.24 | 1599 |
| 2024-09-20 22:21:32.307 | MS1 | 121.4656674049 | 31.1446257894 | 1004 | 504990 | -85.41 | 14.20 | 300.10 | 0.08 | 2.20 | 1600 |
| 2024-09-20 22:21:33.179 | MS1 | 121.4656684889 | 31.1446201685 | 1004 | 504990 | -86.43 | 15.65 | 433.01 | 0.18 | 2.28 | 1597 |
| 2024-09-20 22:21:34.756 | MS1 | 121.4656740756 | 31.1446290004 | 1004 | 504990 | -87.06 | 12.73 | 102.11 | 0.53 | 2.48 | 536 |
| 2024-09-20 22:21:35.878 | MS1 | 121.4656602654 | 31.1446256224 | 1004 | 504990 | -85.27 | 13.42 | 74.50 | 0.51 | 2.96 | 699 |
| 2024-09-20 22:21:36.488 | MS1 | 121.4656615220 | 31.1446292977 | 1004 | 504990 | -87.41 | 14.04 | 80.34 | 0.65 | 2.57 | 579 |
| 2024-09-20 22:21:37.208 | MS1 | 121.4656641553 | 31.1446190645 | 1004 | 504990 | -89.62 | 9.13 | 60.48 | 0.61 | 2.09 | 584 |
| 2024-09-20 22:21:38.187 | MS1 | 121.4656601252 | 31.1446324510 | 1004 | 504990 | -90.95 | 7.09 | 81.62 | 0.61 | 2.09 | 522 |
| 2024-09-20 22:21:39.221 | MS1 | 121.4656653687 | 31.1446356210 | 1004 | 504990 | -90.55 | 12.91 | 49.02 | 0.53 | 2.73 | 687 |
| 2024-09-20 22:21:40.543 | MS1 | 121.4656746645 | 31.1446335807 | 1004 | 504990 | -91.83 | 12.15 | 364.95 | 0.06 | 2.29 | 1569 |
| 2024-09-20 22:21:41.101 | MS1 | 121.4656683355 | 31.1446361640 | 1004 | 504990 | -93.50 | 10.75 | 388.48 | 0.09 | 2.04 | 1564 |
| 2024-09-20 22:21:42.619 | MS1 | 121.4656721885 | 31.1446275941 | 1004 | 504990 | -89.78 | 7.87 | 377.89 | 0.01 | 2.09 | 1585 |

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
| 3231913 | 1 | 121.4757196638 | 31.1476318949 | 120 | 2 | 12 | 27.3 | TDD | 736 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3240343 | 4 | 121.4715024889 | 31.1457359225 | 144 | 1 | 3 | 23.3 | TDD | 495 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3253757 | 2 | 121.4753386906 | 31.1513238067 | 12 | 12 | 5 | 16.8 | TDD | 11 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3276012 | 3 | 121.4706222667 | 31.1469234947 | 267 | 3 | 10 | 16.4 | TDD | 1004 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:30.819 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.836 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:30.961 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.961 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.684 | NREventA3 | measId:2;ServCellPCI:883;Se... |
| 2024-09-20 22:21:37.924 | NRHandoverAttempt | SourcePCI:883;SourceNR-ARFC... |
| 2024-09-20 22:21:37.955 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.970 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.094 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.094 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3231913 | 1 | 17.7697 | 13.0490 | -114.1556 | 14.4550 | 166.7692 | 0.0133 | 0.0153 |
| 2024_09_20 22:00 | 3253757 | 2 | 5.2406 | 7.5134 | -115.8311 | 15.9689 | 190.2167 | 0.0154 | 0.0164 |
| 2024_09_20 22:00 | 3276012 | 3 | 9.1535 | 10.0031 | -117.3062 | 13.0697 | 89.1191 | 0.0161 | 0.0024 |
| 2024_09_20 22:00 | 3240343 | 4 | 11.2968 | 5.3031 | -114.7450 | 15.5768 | 122.8836 | 0.0194 | 0.0054 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416716_07A642B7 | 504990 | 1004 | -83.5 | 504990 | 736 | -96.2 | 504990 | 11 | -98.7 | 504990 | 495 |
| MR_1774416716_3476DDD1 | 504990 | 1004 | -84.9 | 504990 | 736 | -94.6 | 504990 | 11 | -98.6 | 504990 | 495 |
| MR_1774416716_E95DDA63 | 504990 | 1004 | -85.4 | 504990 | 736 | -93.7 | 504990 | 11 | -95.9 | 504990 | 495 |
| MR_1774416716_3FBAA9E1 | 504990 | 1004 | -86.9 | 504990 | 736 | -92.6 | 504990 | 11 | -96.3 | 504990 | 495 |
| MR_1774416716_81ED6DF8 | 504990 | 1004 | -85.7 | 504990 | 736 | -94.6 | 504990 | 11 | -96.9 | 504990 | 495 |
| MR_1774416716_01586517 | 504990 | 1004 | -86.5 | 504990 | 736 | -95.8 | 504990 | 11 | -97.4 | 504990 | 495 |
| MR_1774416716_54D595D5 | 504990 | 1004 | -84.0 | 504990 | 736 | -93.8 | 504990 | 11 | -97.4 | 504990 | 495 |
| MR_1774416716_CA403FFF | 504990 | 1004 | -85.2 | 504990 | 736 | -96.2 | 504990 | 11 | -96.6 | 504990 | 495 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1044: `57130756-1de...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `57130756-1de5-4901-bebd-a867cdc68d3e` |
| Tag | **single-answer** |
| 정답 | **C11** |
| C11 의미 | Lift the tilt angle  of 3252725_1 by 8 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1044] topology](images/train_1044.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment.
- `C2`: Decrease transmission power for 3221206_4
- `C3`: Adjust the azimuth of 3252725_1 by 50 degrees
- `C4`: Increase transmission power for 3235981_2
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3221206_4
- `C6`: Decrease A3 Offset threshold for 3221206_4
- `C7`: Decrease A3 Offset threshold for 3235981_2
- `C8`: Increase A3 Offset threshold for 3221206_4
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3235981_2
- `C10`: Adjust the azimuth of 3235981_2 by 28 degrees
- `C11`: Lift the tilt angle  of 3252725_1 by 8 degrees **← 정답**
- `C12`: Check test server and transmission issues
- `C13`: Lift the tilt angle of 3235981_2 by 4 degrees
- `C14`: Add neighbor relationship between 3252725_1 and 3221206_4
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3221206_4
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3235981_2
- `C17`: Increase A3 Offset threshold for 3235981_2
- `C18`: Add neighbor relationship between 3235981_2 and 3221206_4
- `C19`: Increase transmission power for 3221206_4
- `C20`: Decrease transmission power for 3235981_2
- `C21`: Press down the tilt angle  of 3252725_1 by 8 degrees
- `C22`: Press down the tilt angle of 3235981_2 by 4 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.933 | MS1 | 121.4656603975 | 31.1446310821 | 561 | 504990 | -89.21 | 17.60 | 434.47 | 0.14 | 2.18 | 1562 |
| 2024-09-20 22:21:32.531 | MS1 | 121.4656732658 | 31.1446257342 | 561 | 504990 | -90.29 | 16.77 | 457.28 | 0.13 | 2.20 | 1565 |
| 2024-09-20 22:21:33.368 | MS1 | 121.4656743487 | 31.1446362413 | 561 | 504990 | -86.68 | 16.70 | 481.77 | 0.20 | 2.00 | 1561 |
| 2024-09-20 22:21:34.247 | MS1 | 121.4656660273 | 31.1446196794 | 561 | 504990 | -87.98 | 12.77 | 48.07 | 0.10 | 2.50 | 1594 |
| 2024-09-20 22:21:35.793 | MS1 | 121.4656638776 | 31.1446282888 | 561 | 504990 | -88.10 | 14.30 | 53.38 | 0.15 | 2.85 | 1560 |
| 2024-09-20 22:21:36.958 | MS1 | 121.4656669449 | 31.1446326844 | 561 | 504990 | -86.29 | 13.32 | 77.66 | 0.00 | 2.79 | 1584 |
| 2024-09-20 22:21:37.596 | MS1 | 121.4656634828 | 31.1446267559 | 561 | 504990 | -92.38 | 12.33 | 81.39 | 0.13 | 2.95 | 1568 |
| 2024-09-20 22:21:38.374 | MS1 | 121.4656677037 | 31.1446237441 | 561 | 504990 | -93.38 | 9.59 | 85.41 | 0.03 | 2.87 | 1573 |
| 2024-09-20 22:21:39.559 | MS1 | 121.4656637301 | 31.1446269576 | 561 | 504990 | -91.85 | 10.90 | 90.48 | 0.16 | 2.16 | 1584 |
| 2024-09-20 22:21:40.413 | MS1 | 121.4656721598 | 31.1446361656 | 561 | 504990 | -92.73 | 12.39 | 343.18 | 0.12 | 2.85 | 1588 |
| 2024-09-20 22:21:41.534 | MS1 | 121.4656671053 | 31.1446263811 | 561 | 504990 | -91.84 | 10.73 | 578.90 | 0.00 | 2.08 | 1571 |
| 2024-09-20 22:21:42.461 | MS1 | 121.4656767000 | 31.1446322067 | 561 | 504990 | -93.85 | 10.17 | 425.23 | 0.02 | 2.98 | 1566 |

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
| 3221206 | 4 | 121.4748675784 | 31.1559684289 | 36 | 7 | 1 | 17.0 | TDD | 303 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3235981 | 2 | 121.4685841116 | 31.1552366357 | 165 | 2 | 8 | 49.9 | TDD | 561 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3252725 | 1 | 121.4669223931 | 31.1548674971 | 19 | 7 | 7 | 19.8 | TDD | 128 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3272419 | 3 | 121.4739069761 | 31.1444314673 | 120 | 14 | 2 | 45.7 | TDD | 797 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |

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
| 2024-09-20 22:21:30.980 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.005 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.138 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.138 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.826 | NREventA3 | measId:2;ServCellPCI:222;Se... |
| 2024-09-20 22:21:38.066 | NRHandoverAttempt | SourcePCI:222;SourceNR-ARFC... |
| 2024-09-20 22:21:38.108 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.118 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.239 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.239 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3252725 | 1 | 5.0741 | 12.0123 | -116.4612 | 16.7104 | 131.2387 | 0.0050 | 0.0034 |
| 2024_09_20 22:00 | 3235981 | 2 | 87.8485 | 86.2409 | -117.1942 | 11.1637 | 150.1959 | 0.0011 | 0.0083 |
| 2024_09_20 22:00 | 3272419 | 3 | 13.8556 | 11.9190 | -116.5031 | 19.0781 | 85.2629 | 0.0181 | 0.0152 |
| 2024_09_20 22:00 | 3221206 | 4 | 15.2157 | 16.9438 | -115.7637 | 18.1050 | 110.2363 | 0.0198 | 0.0134 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414518_556963C9 | 504990 | 561 | -86.7 | 504990 | 303 | -87.9 | 504990 | 128 | -93.7 | 504990 | 797 |
| MR_1774414518_0CCED3B7 | 504990 | 561 | -87.2 | 504990 | 303 | -89.2 | 504990 | 128 | -96.2 | 504990 | 797 |
| MR_1774414518_D52D9B2B | 504990 | 561 | -89.2 | 504990 | 303 | -88.0 | 504990 | 128 | -95.5 | 504990 | 797 |
| MR_1774414518_10B7A6D5 | 504990 | 561 | -87.1 | 504990 | 303 | -87.3 | 504990 | 128 | -96.5 | 504990 | 797 |
| MR_1774414518_E327747F | 504990 | 561 | -87.2 | 504990 | 303 | -89.5 | 504990 | 128 | -94.4 | 504990 | 797 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1045: `b79a15a4-65e...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `b79a15a4-65e8-4b0b-a736-180fa997f212` |
| Tag | **single-answer** |
| 정답 | **C20** |
| C20 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3217863_3 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1045] topology](images/train_1045.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3217863_3 by 4 degrees
- `C2`: Adjust the azimuth of 3217863_3 by 21 degrees
- `C3`: Insufficient data; more data is needed for judgment.
- `C4`: Lift the tilt angle  of 3253383_4 by 2 degrees
- `C5`: Increase transmission power for 3253383_4
- `C6`: Press down the tilt angle  of 3253383_4 by 2 degrees
- `C7`: Increase A3 Offset threshold for 3217863_3
- `C8`: Add neighbor relationship between 3217863_3 and 3253383_4
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3217863_3
- `C10`: Decrease transmission power for 3217863_3
- `C11`: Decrease transmission power for 3253383_4
- `C12`: Increase A3 Offset threshold for 3253383_4
- `C13`: Check test server and transmission issues
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3253383_4
- `C15`: Decrease A3 Offset threshold for 3217863_3
- `C16`: Press down the tilt angle of 3217863_3 by 4 degrees
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3253383_4
- `C18`: Add neighbor relationship between 3259052_13 and 3253383_4
- `C19`: Adjust the azimuth of 3253383_4 by 46 degrees
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3217863_3 **← 정답**
- `C21`: Increase transmission power for 3217863_3
- `C22`: Decrease A3 Offset threshold for 3253383_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.100 | MS1 | 121.4656655306 | 31.1446290070 | 134 | 504990 | -95.35 | 9.31 | 409.12 | 0.04 | 2.65 | 1562 |
| 2024-09-20 22:21:32.392 | MS1 | 121.4656581911 | 31.1446243596 | 256 | 504990 | -95.75 | 14.13 | 361.00 | 0.11 | 2.87 | 1580 |
| 2024-09-20 22:21:33.584 | MS1 | 121.4656734444 | 31.1446254728 | 559 | 504990 | -95.19 | 12.84 | 294.11 | 0.03 | 2.65 | 1591 |
| 2024-09-20 22:21:34.752 | MS1 | 121.4656589312 | 31.1446345480 | 515 | 152650 | -96.89 | 3.06 | 63.47 | 0.16 | 1.50 | 1000 |
| 2024-09-20 22:21:35.355 | MS1 | 121.4656608314 | 31.1446377599 | 909 | 152650 | -90.09 | 5.98 | 94.80 | 0.07 | 1.74 | 987 |
| 2024-09-20 22:21:36.659 | MS1 | 121.4656646599 | 31.1446204472 | 703 | 152650 | -91.23 | 2.72 | 58.64 | 0.04 | 1.68 | 921 |
| 2024-09-20 22:21:37.185 | MS1 | 121.4656773494 | 31.1446375662 | 296 | 152650 | -92.17 | 3.10 | 53.13 | 0.02 | 1.50 | 934 |
| 2024-09-20 22:21:38.961 | MS1 | 121.4656704155 | 31.1446188044 | 515 | 152650 | -92.85 | 3.57 | 83.60 | 0.02 | 1.89 | 976 |
| 2024-09-20 22:21:39.313 | MS1 | 121.4656696585 | 31.1446217566 | 909 | 152650 | -89.44 | 4.19 | 81.82 | 0.17 | 1.96 | 954 |
| 2024-09-20 22:21:40.869 | MS1 | 121.4656740666 | 31.1446277277 | 703 | 152650 | -95.30 | 2.50 | 56.11 | 0.06 | 2.86 | 1569 |
| 2024-09-20 22:21:41.973 | MS1 | 121.4656743601 | 31.1446315368 | 296 | 152650 | -88.53 | 4.01 | 71.90 | 0.05 | 2.83 | 1563 |
| 2024-09-20 22:21:42.938 | MS1 | 121.4656617374 | 31.1446291023 | 515 | 152650 | -87.20 | 6.29 | 72.29 | 0.10 | 2.58 | 1580 |

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
| 3217117 | 12 | 121.4688354072 | 31.1473080662 | 4 | 13 | 1 | 16.7 | FDD | 982 | n1 | 152650 | 30M | 4T4R | 20 | 152650 |
| 3217863 | 3 | 121.4719220683 | 31.1518379235 | 196 | 2 | 1 | 26.6 | TDD | 134 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3221280 | 6 | 121.4640911455 | 31.1505296124 | 223 | 7 | 2 | 21.4 | TDD | 445 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3221568 | 5 | 121.4734319537 | 31.1507333297 | 297 | 0 | 8 | 27.3 | TDD | 559 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3225020 | 10 | 121.4752188662 | 31.1499805523 | 294 | 11 | 5 | 7.0 | FDD | 686 | n1 | 152650 | 30M | 4T4R | 19 | 152650 |
| 3235991 | 9 | 121.4685377661 | 31.1545171735 | 199 | 10 | 8 | 12.3 | FDD | 909 | n1 | 152650 | 30M | 4T4R | 15 | 152650 |
| 3237822 | 2 | 121.4702686844 | 31.1459072005 | 195 | 1 | 1 | 16.3 | TDD | 481 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3245558 | 8 | 121.4661148247 | 31.1471315128 | 69 | 11 | 12 | 19.6 | FDD | 296 | n1 | 152650 | 30M | 4T4R | 18 | 152650 |
| 3246574 | 11 | 121.4735854872 | 31.1521226207 | 69 | 8 | 12 | 2.7 | FDD | 21 | n1 | 152650 | 30M | 4T4R | 27 | 152650 |
| 3253383 | 4 | 121.4713193526 | 31.1485812477 | 185 | 2 | 0 | 5.3 | TDD | 719 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3255153 | 7 | 121.4758135182 | 31.1533306899 | 242 | 1 | 7 | 19.2 | FDD | 515 | n1 | 152650 | 30M | 4T4R | 23 | 152650 |
| 3259052 | 13 | 121.4641727984 | 31.1548890079 | 157 | 12 | 10 | 15.5 | FDD | 703 | n1 | 152650 | 30M | 4T4R | 23 | 152650 |
| 3275040 | 1 | 121.4730364399 | 31.1537179791 | 79 | 12 | 2 | 15.3 | TDD | 256 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:31.536 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.559 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.675 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.675 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.344 | NREventA2 | measId:1;ServCellPCI:205;Se... |
| 2024-09-20 22:21:35.473 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.740 | NREventA5 | measId:3;ServCellPCI:205;Se... |
| 2024-09-20 22:21:35.792 | NRHandoverAttempt | SourcePCI:205;SourceNR-ARFC... |
| 2024-09-20 22:21:35.818 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.833 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:35.946 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.946 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3275040 | 1 | 14.4818 | 13.3605 | -114.6319 | 10.8263 | 185.2338 | 0.0068 | 0.0182 |
| 2024_09_20 22:00 | 3237822 | 2 | 5.1365 | 6.0132 | -114.8783 | 12.0439 | 149.7216 | 0.0132 | 0.0057 |
| 2024_09_20 22:00 | 3217863 | 3 | 7.7169 | 10.9231 | -117.4672 | 5.8835 | 185.3242 | 0.0104 | 0.0066 |
| 2024_09_20 22:00 | 3253383 | 4 | 11.9547 | 11.7320 | -114.7448 | 16.0586 | 182.8012 | 0.0135 | 0.0061 |
| 2024_09_20 22:00 | 3221568 | 5 | 6.7864 | 16.1989 | -116.3277 | 14.8742 | 148.1343 | 0.0091 | 0.0025 |
| 2024_09_20 22:00 | 3221280 | 6 | 9.1877 | 11.7709 | -117.9121 | 5.8799 | 84.7311 | 0.0084 | 0.0018 |
| 2024_09_20 22:00 | 3255153 | 7 | 11.5750 | 5.0125 | -114.6257 | 3.7600 | 49.3411 | 0.0069 | 0.0020 |
| 2024_09_20 22:00 | 3245558 | 8 | 15.9723 | 8.4974 | -114.2234 | 4.2838 | 30.6603 | 0.0041 | 0.0073 |
| 2024_09_20 22:00 | 3235991 | 9 | 6.0509 | 17.3310 | -114.3963 | 3.3024 | 51.0137 | 0.0039 | 0.0133 |
| 2024_09_20 22:00 | 3225020 | 10 | 14.4592 | 12.7267 | -115.7952 | 3.7004 | 27.8311 | 0.0120 | 0.0143 |
| 2024_09_20 22:00 | 3246574 | 11 | 16.2993 | 5.9499 | -116.6548 | 3.0445 | 33.7546 | 0.0112 | 0.0138 |
| 2024_09_20 22:00 | 3217117 | 12 | 10.0558 | 6.9351 | -117.1246 | 3.2506 | 47.0300 | 0.0044 | 0.0013 |
| 2024_09_20 22:00 | 3259052 | 13 | 5.6225 | 12.7868 | -116.7545 | 3.5433 | 52.3162 | 0.0075 | 0.0043 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415968_615E17C9 | 152650 | 515 | -98.5 | 152650 | 21 | -101.1 | 152650 | 982 | -104.6 | 152650 | 686 |
| MR_1774415968_303A70E4 | 504990 | 559 | -95.3 | 504990 | 719 | -94.8 | 504990 | 445 | -97.3 | 504990 | 481 |
| MR_1774415968_0FFA83A9 | 152650 | 515 | -98.4 | 152650 | 21 | -100.2 | 152650 | 982 | -102.7 | 152650 | 686 |
| MR_1774415968_A3638B7D | 504990 | 559 | -94.7 | 504990 | 719 | -98.0 | 504990 | 445 | -96.2 | 504990 | 481 |
| MR_1774415968_6F385CEA | 152650 | 515 | -96.8 | 152650 | 21 | -102.0 | 152650 | 982 | -105.7 | 152650 | 686 |
| MR_1774415968_B33638A8 | 504990 | 559 | -93.3 | 504990 | 719 | -95.6 | 504990 | 445 | -97.9 | 504990 | 481 |
| MR_1774415968_8FB49AAC | 504990 | 559 | -96.1 | 504990 | 719 | -97.2 | 504990 | 445 | -97.2 | 504990 | 481 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1046: `2a01082b-bc5...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `2a01082b-bc50-449b-86e8-e5aca627dec0` |
| Tag | **single-answer** |
| 정답 | **C9** |
| C9 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3234671_4 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1046] topology](images/train_1046.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3232238_2
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3232238_2
- `C3`: Increase A3 Offset threshold for 3232238_2
- `C4`: Decrease transmission power for 3234671_4
- `C5`: Adjust the azimuth of 3234671_4 by 5 degrees
- `C6`: Increase A3 Offset threshold for 3234671_4
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3234671_4
- `C8`: Adjust the azimuth of 3232238_2 by 43 degrees
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3234671_4 **← 정답**
- `C10`: Press down the tilt angle  of 3232238_2 by 2 degrees
- `C11`: Increase transmission power for 3234671_4
- `C12`: Add neighbor relationship between 3234671_4 and 3232238_2
- `C13`: Decrease A3 Offset threshold for 3234671_4
- `C14`: Lift the tilt angle  of 3232238_2 by 2 degrees
- `C15`: Insufficient data; more data is needed for judgment.
- `C16`: Decrease A3 Offset threshold for 3232238_2
- `C17`: Decrease transmission power for 3232238_2
- `C18`: Check test server and transmission issues
- `C19`: Press down the tilt angle of 3234671_4 by 4 degrees
- `C20`: Add neighbor relationship between 3236208_12 and 3232238_2
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3232238_2
- `C22`: Lift the tilt angle of 3234671_4 by 4 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.901 | MS1 | 121.4656613248 | 31.1446281639 | 774 | 504990 | -95.39 | 9.49 | 442.20 | 0.07 | 2.42 | 1593 |
| 2024-09-20 22:21:32.740 | MS1 | 121.4656692563 | 31.1446262355 | 450 | 504990 | -94.41 | 10.12 | 332.81 | 0.14 | 2.49 | 1574 |
| 2024-09-20 22:21:33.683 | MS1 | 121.4656584078 | 31.1446188949 | 780 | 504990 | -95.00 | 14.40 | 470.48 | 0.01 | 3.00 | 1597 |
| 2024-09-20 22:21:34.375 | MS1 | 121.4656741709 | 31.1446243155 | 462 | 152650 | -90.83 | 4.86 | 71.81 | 0.06 | 1.90 | 984 |
| 2024-09-20 22:21:35.130 | MS1 | 121.4656705140 | 31.1446181544 | 769 | 152650 | -92.47 | 6.25 | 93.14 | 0.16 | 1.59 | 986 |
| 2024-09-20 22:21:36.443 | MS1 | 121.4656734842 | 31.1446269982 | 726 | 152650 | -95.90 | 4.11 | 65.68 | 0.02 | 1.74 | 988 |
| 2024-09-20 22:21:37.470 | MS1 | 121.4656646462 | 31.1446376888 | 151 | 152650 | -87.13 | 4.63 | 89.55 | 0.11 | 1.84 | 974 |
| 2024-09-20 22:21:38.427 | MS1 | 121.4656636132 | 31.1446232663 | 462 | 152650 | -90.57 | 3.72 | 76.11 | 0.07 | 1.84 | 948 |
| 2024-09-20 22:21:39.209 | MS1 | 121.4656668856 | 31.1446319663 | 769 | 152650 | -87.36 | 5.50 | 74.26 | 0.14 | 1.70 | 934 |
| 2024-09-20 22:21:40.248 | MS1 | 121.4656713696 | 31.1446287293 | 726 | 152650 | -96.26 | 5.31 | 90.07 | 0.17 | 2.23 | 1593 |
| 2024-09-20 22:21:41.979 | MS1 | 121.4656715476 | 31.1446237187 | 151 | 152650 | -93.78 | 7.95 | 50.17 | 0.12 | 2.71 | 1587 |
| 2024-09-20 22:21:42.645 | MS1 | 121.4656697540 | 31.1446378537 | 462 | 152650 | -87.53 | 2.70 | 82.00 | 0.14 | 2.21 | 1586 |

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
| 3213710 | 9 | 121.4757725729 | 31.1461325610 | 334 | 9 | 8 | 10.7 | FDD | 523 | n1 | 152650 | 30M | 4T4R | 24 | 152650 |
| 3225721 | 8 | 121.4657517284 | 31.1558228072 | 309 | 8 | 6 | 12.1 | FDD | 329 | n1 | 152650 | 30M | 4T4R | 14 | 152650 |
| 3228105 | 6 | 121.4758889520 | 31.1541044658 | 197 | 6 | 5 | 22.3 | TDD | 780 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3232238 | 2 | 121.4728890820 | 31.1450004480 | 224 | 0 | 12 | 19.9 | TDD | 258 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3234671 | 4 | 121.4706925172 | 31.1557592408 | 196 | 3 | 2 | 20.7 | TDD | 774 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3236208 | 12 | 121.4666634074 | 31.1490441602 | 240 | 3 | 2 | 16.9 | FDD | 726 | n1 | 152650 | 30M | 4T4R | 18 | 152650 |
| 3242750 | 10 | 121.4726818877 | 31.1462774353 | 320 | 3 | 8 | 23.3 | FDD | 462 | n1 | 152650 | 30M | 4T4R | 10 | 152650 |
| 3249526 | 11 | 121.4670392454 | 31.1549710731 | 201 | 2 | 0 | 29.7 | FDD | 497 | n1 | 152650 | 30M | 4T4R | 22 | 152650 |
| 3251088 | 5 | 121.4737991618 | 31.1445043329 | 245 | 0 | 12 | 25.1 | TDD | 586 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3253716 | 13 | 121.4729922577 | 31.1460800846 | 237 | 14 | 0 | 27.9 | FDD | 151 | n1 | 152650 | 30M | 4T4R | 25 | 152650 |
| 3262547 | 7 | 121.4703985938 | 31.1507755149 | 197 | 9 | 12 | 3.1 | FDD | 769 | n1 | 152650 | 30M | 4T4R | 11 | 152650 |
| 3273937 | 3 | 121.4692210611 | 31.1534782623 | 9 | 5 | 7 | 25.5 | TDD | 290 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3274843 | 1 | 121.4682958380 | 31.1559857458 | 240 | 12 | 3 | 2.7 | TDD | 450 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |

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
| 2024-09-20 22:21:30.838 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.862 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:30.969 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.969 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.687 | NREventA2 | measId:1;ServCellPCI:170;Se... |
| 2024-09-20 22:21:34.811 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.090 | NREventA5 | measId:3;ServCellPCI:170;Se... |
| 2024-09-20 22:21:35.165 | NRHandoverAttempt | SourcePCI:170;SourceNR-ARFC... |
| 2024-09-20 22:21:35.204 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.218 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:35.343 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.343 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3274843 | 1 | 7.3749 | 6.5899 | -115.4372 | 13.1768 | 89.7235 | 0.0046 | 0.0010 |
| 2024_09_20 22:00 | 3232238 | 2 | 12.1651 | 9.4127 | -114.3152 | 9.1605 | 137.9663 | 0.0180 | 0.0115 |
| 2024_09_20 22:00 | 3273937 | 3 | 14.0211 | 17.2850 | -117.0718 | 14.3439 | 140.5998 | 0.0069 | 0.0129 |
| 2024_09_20 22:00 | 3234671 | 4 | 9.0683 | 7.0971 | -117.8268 | 19.4747 | 123.3905 | 0.0192 | 0.0188 |
| 2024_09_20 22:00 | 3251088 | 5 | 15.8480 | 8.6028 | -115.0822 | 8.5799 | 104.4346 | 0.0082 | 0.0071 |
| 2024_09_20 22:00 | 3228105 | 6 | 18.3932 | 10.4548 | -115.6451 | 14.5266 | 142.1707 | 0.0156 | 0.0127 |
| 2024_09_20 22:00 | 3262547 | 7 | 15.1600 | 10.0542 | -115.7939 | 4.8442 | 38.1939 | 0.0070 | 0.0142 |
| 2024_09_20 22:00 | 3225721 | 8 | 10.6743 | 19.2583 | -115.5039 | 4.5014 | 25.7431 | 0.0024 | 0.0012 |
| 2024_09_20 22:00 | 3213710 | 9 | 14.8817 | 10.6306 | -114.1337 | 3.7157 | 55.9120 | 0.0022 | 0.0025 |
| 2024_09_20 22:00 | 3242750 | 10 | 17.8582 | 17.5868 | -117.2956 | 4.9191 | 33.5780 | 0.0162 | 0.0144 |
| 2024_09_20 22:00 | 3249526 | 11 | 10.7495 | 17.6457 | -117.3493 | 4.0756 | 44.1024 | 0.0131 | 0.0106 |
| 2024_09_20 22:00 | 3236208 | 12 | 12.7212 | 17.6558 | -117.6364 | 4.4174 | 40.8655 | 0.0168 | 0.0007 |
| 2024_09_20 22:00 | 3253716 | 13 | 11.9137 | 9.5208 | -115.5202 | 4.0191 | 57.7206 | 0.0013 | 0.0053 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414419_EC607326 | 504990 | 780 | -94.9 | 504990 | 258 | -96.7 | 504990 | 586 | -96.6 | 504990 | 290 |
| MR_1774414419_14C061BE | 504990 | 780 | -94.0 | 504990 | 258 | -96.6 | 504990 | 586 | -98.1 | 504990 | 290 |
| MR_1774414419_12A49363 | 504990 | 780 | -93.1 | 504990 | 258 | -94.8 | 504990 | 586 | -99.1 | 504990 | 290 |
| MR_1774414419_A9ABDA4B | 152650 | 462 | -89.4 | 152650 | 523 | -98.6 | 152650 | 329 | -100.7 | 152650 | 497 |
| MR_1774414419_5F67EC7F | 152650 | 462 | -91.7 | 152650 | 523 | -96.4 | 152650 | 329 | -99.6 | 152650 | 497 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1047: `007bb996-f6a...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `007bb996-f6af-4614-8415-ea636a12771b` |
| Tag | **single-answer** |
| 정답 | **C13** |
| C13 의미 | Add neighbor relationship between 3261529_3 and 3222313_2 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1047] topology](images/train_1047.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle  of 3222313_2 by 3 degrees
- `C2`: Increase A3 Offset threshold for 3222313_2
- `C3`: Decrease A3 Offset threshold for 3261529_3
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3222313_2
- `C5`: Increase transmission power for 3222313_2
- `C6`: Adjust the azimuth of 3222313_2 by 39 degrees
- `C7`: Check test server and transmission issues
- `C8`: Add neighbor relationship between 3279380_1 and 3222313_2
- `C9`: Decrease A3 Offset threshold for 3222313_2
- `C10`: Decrease transmission power for 3261529_3
- `C11`: Press down the tilt angle  of 3222313_2 by 3 degrees
- `C12`: Press down the tilt angle of 3261529_3 by 10 degrees
- `C13`: Add neighbor relationship between 3261529_3 and 3222313_2 **← 정답**
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3222313_2
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3261529_3
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3261529_3
- `C17`: Lift the tilt angle of 3261529_3 by 10 degrees
- `C18`: Insufficient data; more data is needed for judgment.
- `C19`: Adjust the azimuth of 3261529_3 by 50 degrees
- `C20`: Increase A3 Offset threshold for 3261529_3
- `C21`: Decrease transmission power for 3222313_2
- `C22`: Increase transmission power for 3261529_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.240 | MS1 | 121.4656642287 | 31.1446229097 | 839 | 504990 | -82.36 | 13.88 | 381.97 | 0.05 | 2.34 | 1573 |
| 2024-09-20 22:21:32.694 | MS1 | 121.4656725659 | 31.1446240806 | 839 | 504990 | -84.41 | 15.48 | 354.40 | 0.12 | 2.93 | 1589 |
| 2024-09-20 22:21:33.746 | MS1 | 121.4656599804 | 31.1446198088 | 839 | 504990 | -83.31 | 13.87 | 336.57 | 0.16 | 2.39 | 1564 |
| 2024-09-20 22:21:34.627 | MS1 | 121.4656676011 | 31.1446264883 | 839 | 504990 | -90.41 | -3.21 | 51.61 | 0.01 | 1.39 | 1585 |
| 2024-09-20 22:21:35.779 | MS1 | 121.4656769953 | 31.1446268410 | 839 | 504990 | -94.15 | -1.78 | 57.07 | 0.15 | 1.24 | 1585 |
| 2024-09-20 22:21:36.961 | MS1 | 121.4656714375 | 31.1446311720 | 839 | 504990 | -89.46 | -0.20 | 59.77 | 0.00 | 1.41 | 1594 |
| 2024-09-20 22:21:37.424 | MS1 | 121.4656612162 | 31.1446369598 | 839 | 504990 | -88.19 | -1.02 | 55.27 | 0.19 | 1.30 | 1577 |
| 2024-09-20 22:21:38.758 | MS1 | 121.4656716364 | 31.1446186824 | 839 | 504990 | -82.39 | 14.42 | 584.98 | 0.02 | 1.46 | 1577 |
| 2024-09-20 22:21:39.831 | MS1 | 121.4656729631 | 31.1446329080 | 839 | 504990 | -80.14 | 17.85 | 557.04 | 0.10 | 1.22 | 1585 |
| 2024-09-20 22:21:40.812 | MS1 | 121.4656628778 | 31.1446372027 | 839 | 504990 | -79.12 | 16.72 | 451.43 | 0.17 | 2.51 | 1590 |
| 2024-09-20 22:21:41.663 | MS1 | 121.4656607114 | 31.1446198419 | 839 | 504990 | -84.67 | 15.82 | 496.07 | 0.04 | 2.91 | 1590 |
| 2024-09-20 22:21:42.457 | MS1 | 121.4656612604 | 31.1446339152 | 839 | 504990 | -79.75 | 13.76 | 559.12 | 0.04 | 2.04 | 1565 |

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
| 3222313 | 2 | 121.4714222813 | 31.1477722219 | 276 | 1 | 11 | 20.8 | TDD | 977 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3261529 | 3 | 121.4741876337 | 31.1529524812 | 301 | 15 | 10 | 18.4 | TDD | 839 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3269460 | 4 | 121.4697462402 | 31.1511801981 | 189 | 4 | 11 | 41.7 | TDD | 313 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3279380 | 1 | 121.4647908272 | 31.1451973185 | 235 | 14 | 10 | 16.1 | TDD | 976 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |

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
| 2024-09-20 22:21:31.533 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.638 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.638 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.371 | NREventA3 | measId:2;ServCellPCI:966;Se... |
| 2024-09-20 22:21:36.371 | NREventA3 | measId:2;ServCellPCI:966;Se... |
| 2024-09-20 22:21:37.371 | NREventA3 | measId:2;ServCellPCI:966;Se... |
| 2024-09-20 22:21:39.871 | NRRRCReestablishAttempt | PCI:966 |
| 2024-09-20 22:21:39.888 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.902 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:40.036 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:40.036 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3279380 | 1 | 15.9243 | 18.6501 | -115.8828 | 6.6648 | 151.4455 | 0.0168 | 0.0119 |
| 2024_09_20 22:00 | 3222313 | 2 | 14.6524 | 8.2315 | -116.2802 | 18.4518 | 140.9029 | 0.0003 | 0.0151 |
| 2024_09_20 22:00 | 3261529 | 3 | 9.3666 | 6.8428 | -115.1508 | 18.1308 | 115.6209 | 0.0080 | 0.1327 |
| 2024_09_20 22:00 | 3269460 | 4 | 10.8420 | 13.0827 | -117.1520 | 12.3158 | 175.7172 | 0.0041 | 0.0083 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414355_38BFF31F | 504990 | 977 | -87.5 | 504990 | 839 | -91.1 | 504990 | 976 | -89.7 | 504990 | 313 |
| MR_1774414355_95AAC3FB | 504990 | 977 | -84.6 | 504990 | 839 | -88.9 | 504990 | 976 | -90.1 | 504990 | 313 |
| MR_1774414355_D30F3DDA | 504990 | 977 | -85.6 | 504990 | 839 | -89.6 | 504990 | 976 | -89.8 | 504990 | 313 |
| MR_1774414355_D82CB091 | 504990 | 839 | -88.7 | 504990 | 977 | -84.5 | 504990 | 976 | -91.5 | 504990 | 313 |
| MR_1774414355_F1D25D40 | 504990 | 839 | -91.5 | 504990 | 977 | -85.8 | 504990 | 976 | -88.4 | 504990 | 313 |
| MR_1774414355_1AD8C5C2 | 504990 | 977 | -87.5 | 504990 | 839 | -90.2 | 504990 | 976 | -90.9 | 504990 | 313 |
| MR_1774414355_DBA51FF4 | 504990 | 839 | -88.9 | 504990 | 977 | -84.6 | 504990 | 976 | -88.5 | 504990 | 313 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1048: `28d2a7cd-028...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `28d2a7cd-0283-4d1e-be16-c1a5e32311aa` |
| Tag | **single-answer** |
| 정답 | **C8** |
| C8 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1048] topology](images/train_1048.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3226817_2
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3226817_2
- `C3`: Add neighbor relationship between 3226817_2 and 3265670_1
- `C4`: Press down the tilt angle  of 3265670_1 by 10 degrees
- `C5`: Press down the tilt angle of 3226817_2 by 10 degrees
- `C6`: Increase transmission power for 3265670_1
- `C7`: Add neighbor relationship between 3251489_3 and 3265670_1
- `C8`: Insufficient data; more data is needed for judgment. **← 정답**
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3226817_2
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3265670_1
- `C11`: Increase A3 Offset threshold for 3226817_2
- `C12`: Decrease transmission power for 3226817_2
- `C13`: Adjust the azimuth of 3226817_2 by 35 degrees
- `C14`: Increase A3 Offset threshold for 3265670_1
- `C15`: Decrease A3 Offset threshold for 3265670_1
- `C16`: Lift the tilt angle  of 3265670_1 by 10 degrees
- `C17`: Adjust the azimuth of 3265670_1 by 50 degrees
- `C18`: Lift the tilt angle of 3226817_2 by 10 degrees
- `C19`: Decrease transmission power for 3265670_1
- `C20`: Increase transmission power for 3226817_2
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3265670_1
- `C22`: Check test server and transmission issues

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.457 | MS1 | 121.4656644943 | 31.1446293248 | 873 | 504990 | -85.17 | 15.76 | 358.30 | 0.11 | 2.08 | 1584 |
| 2024-09-20 22:21:32.125 | MS1 | 121.4656648266 | 31.1446180026 | 873 | 504990 | -86.59 | 16.89 | 303.32 | 0.16 | 2.63 | 1596 |
| 2024-09-20 22:21:33.911 | MS1 | 121.4656779722 | 31.1446287782 | 873 | 504990 | -85.59 | 12.41 | 551.57 | 0.01 | 2.68 | 1578 |
| 2024-09-20 22:21:34.995 | MS1 | 121.4656727167 | 31.1446209848 | 873 | 504990 | -86.98 | 16.42 | 86.36 | 0.15 | 2.95 | 1585 |
| 2024-09-20 22:21:35.650 | MS1 | 121.4656608858 | 31.1446190229 | 873 | 504990 | -87.99 | 14.44 | 106.14 | 0.12 | 2.38 | 1580 |
| 2024-09-20 22:21:36.826 | MS1 | 121.4656619040 | 31.1446188450 | 873 | 504990 | -89.49 | 12.65 | 89.47 | 0.12 | 2.75 | 1565 |
| 2024-09-20 22:21:37.671 | MS1 | 121.4656719649 | 31.1446348486 | 873 | 504990 | -89.36 | 8.94 | 82.77 | 0.16 | 2.89 | 1598 |
| 2024-09-20 22:21:38.213 | MS1 | 121.4656736876 | 31.1446265256 | 873 | 504990 | -93.72 | 9.32 | 63.31 | 0.17 | 2.72 | 1580 |
| 2024-09-20 22:21:39.163 | MS1 | 121.4656640344 | 31.1446229727 | 873 | 504990 | -89.04 | 8.74 | 99.03 | 0.18 | 2.42 | 1587 |
| 2024-09-20 22:21:40.793 | MS1 | 121.4656759864 | 31.1446339083 | 873 | 504990 | -91.14 | 9.28 | 352.91 | 0.06 | 2.18 | 1593 |
| 2024-09-20 22:21:41.889 | MS1 | 121.4656734915 | 31.1446360961 | 873 | 504990 | -90.57 | 9.17 | 521.09 | 0.08 | 2.10 | 1580 |
| 2024-09-20 22:21:42.371 | MS1 | 121.4656677001 | 31.1446306764 | 873 | 504990 | -93.88 | 12.78 | 347.66 | 0.08 | 2.42 | 1570 |

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
| 3226817 | 2 | 121.4650465507 | 31.1463547509 | 128 | 3 | 1 | 44.5 | TDD | 873 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3251489 | 3 | 121.4727480772 | 31.1504328086 | 272 | 4 | 4 | 46.7 | TDD | 875 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3252537 | 4 | 121.4670067897 | 31.1466428427 | 64 | 12 | 5 | 29.9 | TDD | 993 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3265670 | 1 | 121.4695098913 | 31.1482336784 | 355 | 9 | 11 | 34.6 | TDD | 717 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |

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
| 2024-09-20 22:21:31.467 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.487 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.594 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.594 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.307 | NREventA3 | measId:2;ServCellPCI:891;Se... |
| 2024-09-20 22:21:38.547 | NRHandoverAttempt | SourcePCI:891;SourceNR-ARFC... |
| 2024-09-20 22:21:38.586 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.601 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.751 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.751 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3265670 | 1 | 83.5539 | 90.2622 | -116.2402 | 5.5138 | 144.5969 | 0.0070 | 0.0171 |
| 2024_09_19 22:00 | 3226817 | 2 | 83.4647 | 77.5083 | -117.0252 | 13.6933 | 180.2529 | 0.0171 | 0.0151 |
| 2024_09_19 22:00 | 3251489 | 3 | 89.0236 | 92.6960 | -115.0856 | 18.6610 | 94.5095 | 0.0157 | 0.0119 |
| 2024_09_19 22:00 | 3252537 | 4 | 77.6605 | 84.1649 | -114.9550 | 17.3106 | 135.3592 | 0.0014 | 0.0098 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414604_67CE0EF9 | 504990 | 873 | -88.0 | 504990 | 717 | -93.1 | 504990 | 875 | -97.2 | 504990 | 993 |
| MR_1774414604_C34A2566 | 504990 | 873 | -87.0 | 504990 | 717 | -96.2 | 504990 | 875 | -94.7 | 504990 | 993 |
| MR_1774414604_91242216 | 504990 | 873 | -86.9 | 504990 | 717 | -95.0 | 504990 | 875 | -96.0 | 504990 | 993 |
| MR_1774414604_8D632A70 | 504990 | 873 | -86.0 | 504990 | 717 | -95.1 | 504990 | 875 | -93.7 | 504990 | 993 |
| MR_1774414604_A287533A | 504990 | 873 | -86.9 | 504990 | 717 | -94.9 | 504990 | 875 | -94.6 | 504990 | 993 |
| MR_1774414604_800E3D38 | 504990 | 873 | -87.2 | 504990 | 717 | -96.9 | 504990 | 875 | -97.0 | 504990 | 993 |
| MR_1774414604_03EA0C3F | 504990 | 873 | -88.9 | 504990 | 717 | -94.8 | 504990 | 875 | -94.8 | 504990 | 993 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1049: `63a79ea1-29f...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `63a79ea1-29f8-4c46-89dc-c5519ce006d8` |
| Tag | **single-answer** |
| 정답 | **C15** |
| C15 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1049] topology](images/train_1049.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3260833_4 by 50 degrees
- `C2`: Decrease transmission power for 3245898_2
- `C3`: Decrease A3 Offset threshold for 3245898_2
- `C4`: Check test server and transmission issues
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3245898_2
- `C6`: Adjust the azimuth of 3245898_2 by 50 degrees
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3260833_4
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3260833_4
- `C9`: Add neighbor relationship between 3245898_2 and 3260833_4
- `C10`: Increase transmission power for 3245898_2
- `C11`: Decrease A3 Offset threshold for 3260833_4
- `C12`: Increase A3 Offset threshold for 3260833_4
- `C13`: Decrease transmission power for 3260833_4
- `C14`: Increase A3 Offset threshold for 3245898_2
- `C15`: Insufficient data; more data is needed for judgment. **← 정답**
- `C16`: Lift the tilt angle  of 3260833_4 by 10 degrees
- `C17`: Add neighbor relationship between 3224998_3 and 3260833_4
- `C18`: Press down the tilt angle  of 3260833_4 by 10 degrees
- `C19`: Increase transmission power for 3260833_4
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3245898_2
- `C21`: Lift the tilt angle of 3245898_2 by 10 degrees
- `C22`: Press down the tilt angle of 3245898_2 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.344 | MS1 | 121.4656711882 | 31.1446337309 | 626 | 504990 | -89.98 | 12.81 | 405.34 | 0.02 | 2.11 | 1579 |
| 2024-09-20 22:21:32.785 | MS1 | 121.4656704153 | 31.1446241130 | 626 | 504990 | -88.12 | 12.18 | 484.65 | 0.01 | 2.63 | 1597 |
| 2024-09-20 22:21:33.635 | MS1 | 121.4656774556 | 31.1446305778 | 626 | 504990 | -86.94 | 14.29 | 450.51 | 0.00 | 2.85 | 1565 |
| 2024-09-20 22:21:34.528 | MS1 | 121.4656727492 | 31.1446362821 | 626 | 504990 | -89.41 | 16.49 | 68.47 | 0.04 | 2.94 | 1599 |
| 2024-09-20 22:21:35.861 | MS1 | 121.4656580550 | 31.1446293184 | 626 | 504990 | -89.80 | 12.62 | 81.54 | 0.01 | 2.92 | 1594 |
| 2024-09-20 22:21:36.628 | MS1 | 121.4656653884 | 31.1446368563 | 626 | 504990 | -91.73 | 16.07 | 63.06 | 0.01 | 2.84 | 1580 |
| 2024-09-20 22:21:37.589 | MS1 | 121.4656732214 | 31.1446205673 | 626 | 504990 | -91.27 | 8.54 | 85.14 | 0.06 | 2.60 | 1568 |
| 2024-09-20 22:21:38.256 | MS1 | 121.4656653942 | 31.1446318129 | 626 | 504990 | -90.49 | 10.53 | 78.61 | 0.18 | 2.22 | 1596 |
| 2024-09-20 22:21:39.609 | MS1 | 121.4656605768 | 31.1446224529 | 626 | 504990 | -91.84 | 10.20 | 60.14 | 0.11 | 2.89 | 1584 |
| 2024-09-20 22:21:40.952 | MS1 | 121.4656633014 | 31.1446273122 | 626 | 504990 | -91.04 | 10.95 | 564.33 | 0.07 | 2.64 | 1583 |
| 2024-09-20 22:21:41.951 | MS1 | 121.4656652360 | 31.1446283398 | 626 | 504990 | -92.72 | 12.20 | 360.24 | 0.07 | 2.68 | 1589 |
| 2024-09-20 22:21:42.471 | MS1 | 121.4656688273 | 31.1446346281 | 626 | 504990 | -91.14 | 9.53 | 413.23 | 0.08 | 2.33 | 1581 |

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
| 3224998 | 3 | 121.4697083783 | 31.1511567595 | 60 | 2 | 3 | 36.2 | TDD | 683 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3236987 | 1 | 121.4660014521 | 31.1496270608 | 48 | 15 | 1 | 18.0 | TDD | 97 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3245898 | 2 | 121.4748133831 | 31.1520097302 | 282 | 9 | 3 | 36.3 | TDD | 626 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3260833 | 4 | 121.4661299074 | 31.1453290186 | 16 | 7 | 8 | 34.0 | TDD | 394 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |

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
| 2024-09-20 22:21:31.350 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.370 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.518 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.518 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.173 | NREventA3 | measId:2;ServCellPCI:743;Se... |
| 2024-09-20 22:21:38.413 | NRHandoverAttempt | SourcePCI:743;SourceNR-ARFC... |
| 2024-09-20 22:21:38.444 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.456 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.574 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.574 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3236987 | 1 | 92.1732 | 93.5200 | -115.3912 | 18.6537 | 133.4738 | 0.0147 | 0.0040 |
| 2024_09_19 22:00 | 3245898 | 2 | 88.9424 | 81.0237 | -117.0780 | 18.5738 | 122.4450 | 0.0188 | 0.0170 |
| 2024_09_19 22:00 | 3224998 | 3 | 89.3531 | 75.2404 | -116.5215 | 17.3457 | 190.6826 | 0.0114 | 0.0168 |
| 2024_09_19 22:00 | 3260833 | 4 | 90.1566 | 85.9562 | -115.2842 | 13.7904 | 198.2159 | 0.0084 | 0.0182 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412115_4DDEBCC9 | 504990 | 626 | -87.9 | 504990 | 394 | -93.8 | 504990 | 683 | -98.9 | 504990 | 97 |
| MR_1774412115_6E8D803D | 504990 | 626 | -88.7 | 504990 | 394 | -95.2 | 504990 | 683 | -95.9 | 504990 | 97 |
| MR_1774412115_FAB4C037 | 504990 | 626 | -87.4 | 504990 | 394 | -96.0 | 504990 | 683 | -98.3 | 504990 | 97 |
| MR_1774412115_61F46D04 | 504990 | 626 | -88.8 | 504990 | 394 | -95.4 | 504990 | 683 | -97.2 | 504990 | 97 |
| MR_1774412115_AE49F165 | 504990 | 626 | -87.6 | 504990 | 394 | -92.3 | 504990 | 683 | -95.7 | 504990 | 97 |
| MR_1774412115_4E73E24D | 504990 | 626 | -90.7 | 504990 | 394 | -93.3 | 504990 | 683 | -96.2 | 504990 | 97 |
| MR_1774412115_DC606025 | 504990 | 626 | -87.5 | 504990 | 394 | -93.3 | 504990 | 683 | -97.2 | 504990 | 97 |
| MR_1774412115_B20D5389 | 504990 | 626 | -87.7 | 504990 | 394 | -92.3 | 504990 | 683 | -99.0 | 504990 | 97 |

> *... 2개 열 생략 (전체 14열)*

---
