# Track A 문제 분석 — test[130]~test[139]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/test.json`
> 범위: test[130] ~ test[139] (10개)

## 목차

1. [문제 130: `affbf4ce-542...`](#130) — single-answer
2. [문제 131: `0f78678a-8d2...`](#131) — single-answer
3. [문제 132: `0ff664c2-3c3...`](#132) — single-answer
4. [문제 133: `1f265be2-204...`](#133) — single-answer
5. [문제 134: `f3a0ae80-aea...`](#134) — single-answer
6. [문제 135: `40e306bc-411...`](#135) — single-answer
7. [문제 136: `6074cfac-e2e...`](#136) — single-answer
8. [문제 137: `04d5399b-13d...`](#137) — multiple-answer
9. [문제 138: `fca75eb4-a6a...`](#138) — single-answer
10. [문제 139: `afa24180-af8...`](#139) — single-answer

---

### 문제 130: `affbf4ce-542...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `affbf4ce-5420-4dbd-ac8e-ac15bb72c227` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[130] topology](images/test_0130.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3225388_2
- `C2`: Adjust the azimuth of 3225388_2 by 50 degrees
- `C3`: Increase transmission power for 3258759_1
- `C4`: Increase A3 Offset threshold for 3258759_1
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3258759_1
- `C6`: Press down the tilt angle  of 3225388_2 by 3 degrees
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3225388_2
- `C8`: Decrease A3 Offset threshold for 3258759_1
- `C9`: Check test server and transmission issues
- `C10`: Insufficient data; more data is needed for judgment.
- `C11`: Add neighbor relationship between 3237991_4 and 3225388_2
- `C12`: Increase A3 Offset threshold for 3225388_2
- `C13`: Decrease A3 Offset threshold for 3225388_2
- `C14`: Lift the tilt angle of 3258759_1 by 10 degrees
- `C15`: Press down the tilt angle of 3258759_1 by 10 degrees
- `C16`: Add neighbor relationship between 3258759_1 and 3225388_2
- `C17`: Adjust the azimuth of 3258759_1 by 50 degrees
- `C18`: Decrease transmission power for 3258759_1
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3225388_2
- `C20`: Decrease transmission power for 3225388_2
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3258759_1
- `C22`: Lift the tilt angle  of 3225388_2 by 3 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.881 | MS1 | 121.4656696887 | 31.1446278140 | 938 | 504990 | -85.24 | 12.81 | 381.03 | 0.19 | 2.19 | 1573 |
| 2024-09-20 22:21:32.850 | MS1 | 121.4656724369 | 31.1446313537 | 938 | 504990 | -89.42 | 13.68 | 598.73 | 0.17 | 2.81 | 1567 |
| 2024-09-20 22:21:33.371 | MS1 | 121.4656604847 | 31.1446274729 | 938 | 504990 | -86.91 | 12.00 | 531.55 | 0.01 | 2.07 | 1571 |
| 2024-09-20 22:21:34.365 | MS1 | 121.4656668441 | 31.1446246469 | 938 | 504990 | -91.70 | 13.19 | 70.47 | 0.14 | 2.30 | 444 |
| 2024-09-20 22:21:35.349 | MS1 | 121.4656634315 | 31.1446354255 | 938 | 504990 | -89.46 | 13.07 | 87.59 | 0.11 | 2.48 | 391 |
| 2024-09-20 22:21:36.189 | MS1 | 121.4656750285 | 31.1446198130 | 938 | 504990 | -85.35 | 15.56 | 94.30 | 0.20 | 2.41 | 311 |
| 2024-09-20 22:21:37.995 | MS1 | 121.4656754324 | 31.1446188252 | 938 | 504990 | -89.63 | 9.82 | 72.36 | 0.11 | 2.73 | 302 |
| 2024-09-20 22:21:38.457 | MS1 | 121.4656669937 | 31.1446299790 | 938 | 504990 | -92.34 | 12.47 | 67.16 | 0.07 | 2.98 | 409 |
| 2024-09-20 22:21:39.577 | MS1 | 121.4656659425 | 31.1446189596 | 938 | 504990 | -89.09 | 9.00 | 62.42 | 0.10 | 2.93 | 329 |
| 2024-09-20 22:21:40.208 | MS1 | 121.4656666049 | 31.1446313196 | 938 | 504990 | -91.42 | 10.12 | 458.76 | 0.03 | 2.70 | 1573 |
| 2024-09-20 22:21:41.360 | MS1 | 121.4656655408 | 31.1446358631 | 938 | 504990 | -90.18 | 12.36 | 321.71 | 0.07 | 2.22 | 1561 |
| 2024-09-20 22:21:42.317 | MS1 | 121.4656600273 | 31.1446329291 | 938 | 504990 | -89.91 | 12.58 | 529.44 | 0.17 | 2.96 | 1566 |

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
| 3224492 | 3 | 121.4756207994 | 31.1478339286 | 218 | 6 | 5 | 23.8 | TDD | 589 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3225388 | 2 | 121.4751837109 | 31.1507120218 | 67 | 1 | 6 | 43.9 | TDD | 731 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3237991 | 4 | 121.4729243004 | 31.1552326951 | 102 | 8 | 8 | 35.7 | TDD | 886 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3258759 | 1 | 121.4721689845 | 31.1528591950 | 275 | 9 | 0 | 41.0 | TDD | 938 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |

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
| 2024-09-20 22:21:31.001 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.025 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.150 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.150 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.842 | NREventA3 | measId:2;ServCellPCI:222;Se... |
| 2024-09-20 22:21:38.082 | NRHandoverAttempt | SourcePCI:222;SourceNR-ARFC... |
| 2024-09-20 22:21:38.123 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.138 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.250 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.250 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3258759 | 1 | 18.2346 | 11.3436 | -117.7738 | 8.4720 | 143.1208 | 0.0083 | 0.0018 |
| 2024_09_20 22:00 | 3225388 | 2 | 13.7558 | 18.4477 | -117.3350 | 12.8242 | 82.1582 | 0.0173 | 0.0198 |
| 2024_09_20 22:00 | 3224492 | 3 | 7.9030 | 5.5129 | -117.0152 | 9.5130 | 99.1171 | 0.0069 | 0.0127 |
| 2024_09_20 22:00 | 3237991 | 4 | 10.1410 | 13.6120 | -117.9998 | 5.1707 | 107.6118 | 0.0164 | 0.0058 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413228_AC03084A | 504990 | 938 | -92.5 | 504990 | 731 | -96.4 | 504990 | 886 | -108.3 | 504990 | 589 |
| MR_1774413228_C7755D26 | 504990 | 938 | -89.8 | 504990 | 731 | -96.4 | 504990 | 886 | -105.1 | 504990 | 589 |
| MR_1774413228_D3D00A6F | 504990 | 938 | -92.1 | 504990 | 731 | -96.6 | 504990 | 886 | -106.0 | 504990 | 589 |
| MR_1774413228_E47A9ADB | 504990 | 938 | -90.6 | 504990 | 731 | -96.7 | 504990 | 886 | -108.3 | 504990 | 589 |
| MR_1774413228_D44B80C5 | 504990 | 938 | -93.7 | 504990 | 731 | -96.5 | 504990 | 886 | -105.8 | 504990 | 589 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 131: `0f78678a-8d2...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `0f78678a-8d25-408c-88fc-a1fcc2f99712` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[131] topology](images/test_0131.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3239520_1
- `C2`: Increase A3 Offset threshold for 3267425_2
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3267425_2
- `C4`: Press down the tilt angle  of 3267425_2 by 5 degrees
- `C5`: Decrease A3 Offset threshold for 3267425_2
- `C6`: Add neighbor relationship between 3239520_1 and 3267425_2
- `C7`: Adjust the azimuth of 3239520_1 by 50 degrees
- `C8`: Press down the tilt angle of 3239520_1 by 10 degrees
- `C9`: Lift the tilt angle  of 3267425_2 by 5 degrees
- `C10`: Insufficient data; more data is needed for judgment.
- `C11`: Decrease transmission power for 3267425_2
- `C12`: Decrease A3 Offset threshold for 3239520_1
- `C13`: Lift the tilt angle of 3239520_1 by 10 degrees
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3267425_2
- `C15`: Increase transmission power for 3239520_1
- `C16`: Increase A3 Offset threshold for 3239520_1
- `C17`: Decrease transmission power for 3239520_1
- `C18`: Add neighbor relationship between 3242063_3 and 3267425_2
- `C19`: Increase transmission power for 3267425_2
- `C20`: Check test server and transmission issues
- `C21`: Adjust the azimuth of 3267425_2 by 25 degrees
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3239520_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.545 | MS1 | 121.4656616152 | 31.1446224145 | 342 | 504990 | -81.79 | 12.85 | 410.59 | 0.08 | 2.69 | 1560 |
| 2024-09-20 22:21:32.129 | MS1 | 121.4656655137 | 31.1446281814 | 342 | 504990 | -75.19 | 14.04 | 346.86 | 0.11 | 2.10 | 1591 |
| 2024-09-20 22:21:33.499 | MS1 | 121.4656741901 | 31.1446348044 | 342 | 504990 | -82.53 | 12.38 | 600.74 | 0.12 | 2.23 | 1590 |
| 2024-09-20 22:21:34.408 | MS1 | 121.4656770459 | 31.1446365918 | 342 | 504990 | -85.25 | -3.22 | 64.56 | 0.03 | 1.04 | 1566 |
| 2024-09-20 22:21:35.204 | MS1 | 121.4656627305 | 31.1446363420 | 342 | 504990 | -87.43 | -2.84 | 55.84 | 0.07 | 1.23 | 1574 |
| 2024-09-20 22:21:36.159 | MS1 | 121.4656717935 | 31.1446205071 | 342 | 504990 | -85.70 | -2.39 | 70.82 | 0.18 | 1.27 | 1561 |
| 2024-09-20 22:21:37.178 | MS1 | 121.4656757242 | 31.1446324473 | 342 | 504990 | -91.56 | -1.91 | 59.88 | 0.12 | 1.19 | 1590 |
| 2024-09-20 22:21:38.930 | MS1 | 121.4656746085 | 31.1446211171 | 342 | 504990 | -75.96 | 13.42 | 316.39 | 0.11 | 1.26 | 1561 |
| 2024-09-20 22:21:39.521 | MS1 | 121.4656612387 | 31.1446348526 | 342 | 504990 | -82.43 | 16.65 | 401.53 | 0.01 | 1.26 | 1598 |
| 2024-09-20 22:21:40.133 | MS1 | 121.4656761595 | 31.1446193089 | 342 | 504990 | -84.35 | 12.94 | 528.21 | 0.09 | 2.65 | 1594 |
| 2024-09-20 22:21:41.155 | MS1 | 121.4656610785 | 31.1446236370 | 342 | 504990 | -81.45 | 14.72 | 323.06 | 0.14 | 2.79 | 1594 |
| 2024-09-20 22:21:42.138 | MS1 | 121.4656640134 | 31.1446257180 | 342 | 504990 | -82.32 | 14.65 | 443.78 | 0.00 | 2.93 | 1589 |

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
| 3239520 | 1 | 121.4693165074 | 31.1509231505 | 114 | 12 | 4 | 24.0 | TDD | 342 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3242063 | 3 | 121.4719531129 | 31.1456366618 | 58 | 2 | 4 | 34.1 | TDD | 350 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3267425 | 2 | 121.4750517272 | 31.1548011252 | 243 | 4 | 4 | 19.7 | TDD | 107 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3273514 | 4 | 121.4722399777 | 31.1443827737 | 314 | 15 | 7 | 46.7 | TDD | 671 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |

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
| 2024-09-20 22:21:31.363 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.388 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.500 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.500 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.163 | NREventA3 | measId:2;ServCellPCI:767;Se... |
| 2024-09-20 22:21:36.163 | NREventA3 | measId:2;ServCellPCI:767;Se... |
| 2024-09-20 22:21:37.163 | NREventA3 | measId:2;ServCellPCI:767;Se... |
| 2024-09-20 22:21:39.663 | NRRRCReestablishAttempt | PCI:767 |
| 2024-09-20 22:21:39.679 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.692 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:39.838 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.838 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3239520 | 1 | 13.9971 | 17.6548 | -115.5388 | 8.3961 | 121.3530 | 0.0163 | 0.1833 |
| 2024_09_20 22:00 | 3267425 | 2 | 16.6413 | 9.9527 | -114.8375 | 12.8302 | 125.3703 | 0.0054 | 0.0015 |
| 2024_09_20 22:00 | 3242063 | 3 | 17.8116 | 17.2460 | -117.0574 | 11.5632 | 186.8860 | 0.0151 | 0.0097 |
| 2024_09_20 22:00 | 3273514 | 4 | 11.3505 | 10.3888 | -117.8788 | 8.5120 | 136.7837 | 0.0024 | 0.0151 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412545_627ADF06 | 504990 | 342 | -85.0 | 504990 | 107 | -81.2 | 504990 | 350 | -87.5 | 504990 | 671 |
| MR_1774412545_A7412215 | 504990 | 342 | -84.1 | 504990 | 107 | -80.4 | 504990 | 350 | -86.7 | 504990 | 671 |
| MR_1774412545_791A95DF | 504990 | 342 | -84.5 | 504990 | 107 | -78.8 | 504990 | 350 | -86.5 | 504990 | 671 |
| MR_1774412545_8BA14F96 | 504990 | 342 | -84.3 | 504990 | 107 | -81.4 | 504990 | 350 | -86.0 | 504990 | 671 |
| MR_1774412545_9D15F58C | 504990 | 342 | -84.7 | 504990 | 107 | -81.5 | 504990 | 350 | -88.4 | 504990 | 671 |
| MR_1774412545_2E78B5E2 | 504990 | 107 | -78.6 | 504990 | 342 | -84.2 | 504990 | 350 | -89.2 | 504990 | 671 |
| MR_1774412545_2E80B170 | 504990 | 342 | -84.7 | 504990 | 107 | -79.3 | 504990 | 350 | -89.5 | 504990 | 671 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 132: `0ff664c2-3c3...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `0ff664c2-3c3d-4945-89f9-3c9201d18f2d` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[132] topology](images/test_0132.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3272861_3
- `C2`: Increase A3 Offset threshold for 3267381_2
- `C3`: Adjust the azimuth of 3272861_3 by 24 degrees
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3272861_3
- `C5`: Press down the tilt angle  of 3267381_2 by 10 degrees
- `C6`: Increase transmission power for 3272861_3
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3267381_2
- `C8`: Check test server and transmission issues
- `C9`: Decrease A3 Offset threshold for 3272861_3
- `C10`: Press down the tilt angle of 3272861_3 by 10 degrees
- `C11`: Lift the tilt angle of 3272861_3 by 10 degrees
- `C12`: Decrease A3 Offset threshold for 3267381_2
- `C13`: Insufficient data; more data is needed for judgment.
- `C14`: Lift the tilt angle  of 3267381_2 by 10 degrees
- `C15`: Increase transmission power for 3267381_2
- `C16`: Decrease transmission power for 3272861_3
- `C17`: Decrease transmission power for 3267381_2
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3267381_2
- `C19`: Add neighbor relationship between 3244014_1 and 3267381_2
- `C20`: Increase A3 Offset threshold for 3272861_3
- `C21`: Add neighbor relationship between 3272861_3 and 3267381_2
- `C22`: Adjust the azimuth of 3267381_2 by 19 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.113 | MS1 | 121.4656592961 | 31.1446302353 | 188 | 504990 | -86.62 | 17.89 | 314.40 | 0.09 | 2.99 | 1587 |
| 2024-09-20 22:21:32.961 | MS1 | 121.4656600474 | 31.1446183256 | 188 | 504990 | -88.49 | 12.16 | 363.07 | 0.19 | 2.61 | 1578 |
| 2024-09-20 22:21:33.958 | MS1 | 121.4656769826 | 31.1446249983 | 188 | 504990 | -89.35 | 16.30 | 441.17 | 0.06 | 2.02 | 1596 |
| 2024-09-20 22:21:34.772 | MS1 | 121.4656580439 | 31.1446323048 | 188 | 504990 | -91.69 | 14.71 | 80.73 | 0.13 | 2.34 | 341 |
| 2024-09-20 22:21:35.229 | MS1 | 121.4656656943 | 31.1446313639 | 188 | 504990 | -91.46 | 13.41 | 62.36 | 0.08 | 2.54 | 398 |
| 2024-09-20 22:21:36.566 | MS1 | 121.4656658917 | 31.1446304327 | 188 | 504990 | -89.53 | 16.32 | 61.56 | 0.18 | 2.07 | 436 |
| 2024-09-20 22:21:37.387 | MS1 | 121.4656745557 | 31.1446250803 | 188 | 504990 | -90.24 | 8.74 | 61.07 | 0.17 | 2.55 | 310 |
| 2024-09-20 22:21:38.142 | MS1 | 121.4656609760 | 31.1446225640 | 188 | 504990 | -92.75 | 8.38 | 53.30 | 0.17 | 2.55 | 320 |
| 2024-09-20 22:21:39.524 | MS1 | 121.4656767117 | 31.1446217068 | 188 | 504990 | -89.42 | 11.85 | 48.14 | 0.11 | 2.60 | 408 |
| 2024-09-20 22:21:40.473 | MS1 | 121.4656595678 | 31.1446184135 | 188 | 504990 | -90.61 | 7.70 | 508.57 | 0.18 | 2.95 | 1596 |
| 2024-09-20 22:21:41.766 | MS1 | 121.4656650726 | 31.1446314081 | 188 | 504990 | -92.00 | 11.76 | 426.83 | 0.10 | 2.41 | 1569 |
| 2024-09-20 22:21:42.948 | MS1 | 121.4656718453 | 31.1446242103 | 188 | 504990 | -89.65 | 11.74 | 407.20 | 0.01 | 2.27 | 1586 |

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
| 3240330 | 4 | 121.4666964354 | 31.1489566080 | 124 | 0 | 8 | 15.9 | TDD | 81 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3244014 | 1 | 121.4646214272 | 31.1442209709 | 104 | 2 | 3 | 49.4 | TDD | 768 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3267381 | 2 | 121.4696390468 | 31.1456486855 | 234 | 10 | 10 | 43.9 | TDD | 153 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3272861 | 3 | 121.4759149427 | 31.1492218347 | 266 | 11 | 5 | 45.4 | TDD | 188 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |

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
| 2024-09-20 22:21:31.470 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.494 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.612 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.612 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.370 | NREventA3 | measId:2;ServCellPCI:39;Ser... |
| 2024-09-20 22:21:38.610 | NRHandoverAttempt | SourcePCI:39;SourceNR-ARFCN... |
| 2024-09-20 22:21:38.660 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.674 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.819 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.819 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3244014 | 1 | 14.0755 | 8.4307 | -114.5729 | 7.7489 | 190.1820 | 0.0060 | 0.0040 |
| 2024_09_20 22:00 | 3267381 | 2 | 18.4594 | 10.3962 | -114.9785 | 11.5764 | 104.7101 | 0.0054 | 0.0110 |
| 2024_09_20 22:00 | 3272861 | 3 | 17.7147 | 15.4708 | -115.4476 | 13.7799 | 134.9242 | 0.0143 | 0.0025 |
| 2024_09_20 22:00 | 3240330 | 4 | 11.7153 | 8.6347 | -116.0017 | 19.5459 | 107.6489 | 0.0176 | 0.0011 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414004_955F26EC | 504990 | 188 | -90.8 | 504990 | 153 | -99.7 | 504990 | 768 | -103.3 | 504990 | 81 |
| MR_1774414004_F84FB5AD | 504990 | 188 | -92.6 | 504990 | 153 | -100.2 | 504990 | 768 | -104.6 | 504990 | 81 |
| MR_1774414004_92BECE31 | 504990 | 188 | -92.0 | 504990 | 153 | -99.6 | 504990 | 768 | -103.9 | 504990 | 81 |
| MR_1774414004_86F6AC72 | 504990 | 188 | -91.3 | 504990 | 153 | -99.5 | 504990 | 768 | -105.6 | 504990 | 81 |
| MR_1774414004_4C7281A5 | 504990 | 188 | -89.9 | 504990 | 153 | -99.4 | 504990 | 768 | -105.2 | 504990 | 81 |
| MR_1774414004_4A2D2416 | 504990 | 188 | -91.4 | 504990 | 153 | -100.7 | 504990 | 768 | -104.9 | 504990 | 81 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 133: `1f265be2-204...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `1f265be2-2043-48bd-81ed-37debc7f375e` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[133] topology](images/test_0133.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3242769_4
- `C2`: Lift the tilt angle  of 3242769_4 by 2 degrees
- `C3`: Increase transmission power for 3242769_4
- `C4`: Decrease transmission power for 3242769_4
- `C5`: Adjust the azimuth of 3242769_4 by 6 degrees
- `C6`: Add neighbor relationship between 3241266_5 and 3242769_4
- `C7`: Lift the tilt angle of 3241266_5 by 3 degrees
- `C8`: Decrease transmission power for 3241266_5
- `C9`: Add neighbor relationship between 3227710_13 and 3242769_4
- `C10`: Increase A3 Offset threshold for 3242769_4
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3241266_5
- `C12`: Press down the tilt angle  of 3242769_4 by 2 degrees
- `C13`: Press down the tilt angle of 3241266_5 by 3 degrees
- `C14`: Check test server and transmission issues
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3242769_4
- `C16`: Insufficient data; more data is needed for judgment.
- `C17`: Increase transmission power for 3241266_5
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3242769_4
- `C19`: Adjust the azimuth of 3241266_5 by 8 degrees
- `C20`: Decrease A3 Offset threshold for 3241266_5
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3241266_5
- `C22`: Increase A3 Offset threshold for 3241266_5

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.337 | MS1 | 121.4656674823 | 31.1446207742 | 475 | 504990 | -94.92 | 10.28 | 347.09 | 0.00 | 2.34 | 1597 |
| 2024-09-20 22:21:32.137 | MS1 | 121.4656649456 | 31.1446329829 | 621 | 504990 | -93.51 | 10.18 | 515.80 | 0.13 | 2.57 | 1590 |
| 2024-09-20 22:21:33.487 | MS1 | 121.4656657966 | 31.1446255230 | 350 | 504990 | -94.37 | 12.17 | 330.52 | 0.06 | 2.85 | 1599 |
| 2024-09-20 22:21:34.924 | MS1 | 121.4656701269 | 31.1446239976 | 995 | 152650 | -87.12 | 3.31 | 58.56 | 0.18 | 1.83 | 945 |
| 2024-09-20 22:21:35.329 | MS1 | 121.4656650301 | 31.1446242227 | 88 | 152650 | -92.24 | 2.13 | 79.72 | 0.10 | 1.80 | 931 |
| 2024-09-20 22:21:36.395 | MS1 | 121.4656731233 | 31.1446208146 | 123 | 152650 | -92.43 | 7.96 | 77.09 | 0.04 | 1.73 | 938 |
| 2024-09-20 22:21:37.821 | MS1 | 121.4656740972 | 31.1446188139 | 259 | 152650 | -91.89 | 4.14 | 67.57 | 0.12 | 1.88 | 963 |
| 2024-09-20 22:21:38.710 | MS1 | 121.4656736810 | 31.1446202830 | 995 | 152650 | -92.29 | 5.90 | 87.68 | 0.18 | 1.56 | 964 |
| 2024-09-20 22:21:39.612 | MS1 | 121.4656635748 | 31.1446319291 | 88 | 152650 | -88.12 | 7.58 | 91.28 | 0.17 | 1.83 | 944 |
| 2024-09-20 22:21:40.558 | MS1 | 121.4656668826 | 31.1446188343 | 123 | 152650 | -95.19 | 4.90 | 88.61 | 0.09 | 2.50 | 1599 |
| 2024-09-20 22:21:41.497 | MS1 | 121.4656647089 | 31.1446351272 | 259 | 152650 | -92.46 | 2.49 | 64.16 | 0.06 | 2.93 | 1588 |
| 2024-09-20 22:21:42.843 | MS1 | 121.4656670249 | 31.1446226470 | 995 | 152650 | -87.46 | 7.42 | 58.36 | 0.02 | 2.87 | 1569 |

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
| 3210871 | 2 | 121.4759984485 | 31.1499564396 | 134 | 4 | 10 | 10.1 | TDD | 621 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3213450 | 12 | 121.4710004308 | 31.1522283967 | 276 | 3 | 5 | 28.5 | FDD | 88 | n1 | 152650 | 30M | 4T4R | 21 | 152650 |
| 3224651 | 6 | 121.4651371321 | 31.1537009484 | 136 | 4 | 11 | 11.5 | TDD | 350 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3227710 | 13 | 121.4654400982 | 31.1499074481 | 171 | 0 | 10 | 26.4 | FDD | 123 | n1 | 152650 | 30M | 4T4R | 27 | 152650 |
| 3231818 | 10 | 121.4666911142 | 31.1467723303 | 240 | 6 | 5 | 19.1 | FDD | 691 | n1 | 152650 | 30M | 4T4R | 14 | 152650 |
| 3233367 | 7 | 121.4725319228 | 31.1545668821 | 111 | 10 | 0 | 0.7 | FDD | 995 | n1 | 152650 | 30M | 4T4R | 19 | 152650 |
| 3241266 | 5 | 121.4663327827 | 31.1538434714 | 176 | 2 | 1 | 25.2 | TDD | 475 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3242769 | 4 | 121.4651985082 | 31.1523574311 | 171 | 1 | 10 | 14.2 | TDD | 346 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3259654 | 11 | 121.4734078862 | 31.1443131694 | 309 | 6 | 5 | 18.3 | FDD | 468 | n1 | 152650 | 30M | 4T4R | 28 | 152650 |
| 3267591 | 9 | 121.4657161724 | 31.1531478891 | 122 | 7 | 11 | 12.5 | FDD | 635 | n1 | 152650 | 30M | 4T4R | 29 | 152650 |
| 3273815 | 8 | 121.4650581036 | 31.1460233290 | 89 | 14 | 7 | 6.6 | FDD | 259 | n1 | 152650 | 30M | 4T4R | 29 | 152650 |
| 3273986 | 3 | 121.4665772299 | 31.1522381914 | 88 | 4 | 2 | 19.4 | TDD | 116 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3275750 | 1 | 121.4742280030 | 31.1478223936 | 59 | 15 | 10 | 20.4 | TDD | 3 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |

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
| 2024-09-20 22:21:31.635 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.773 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.773 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.443 | NREventA2 | measId:1;ServCellPCI:541;Se... |
| 2024-09-20 22:21:35.548 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.812 | NREventA5 | measId:3;ServCellPCI:541;Se... |
| 2024-09-20 22:21:35.884 | NRHandoverAttempt | SourcePCI:541;SourceNR-ARFC... |
| 2024-09-20 22:21:35.919 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.932 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:36.055 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.055 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3275750 | 1 | 5.2863 | 6.9124 | -115.2255 | 7.7575 | 152.3930 | 0.0117 | 0.0020 |
| 2024_09_20 22:00 | 3210871 | 2 | 12.6857 | 18.1541 | -117.8739 | 14.6103 | 99.5939 | 0.0066 | 0.0011 |
| 2024_09_20 22:00 | 3273986 | 3 | 11.6933 | 9.9822 | -114.6551 | 14.6736 | 182.8980 | 0.0049 | 0.0182 |
| 2024_09_20 22:00 | 3242769 | 4 | 17.1225 | 12.4163 | -117.1221 | 11.0252 | 168.2378 | 0.0154 | 0.0168 |
| 2024_09_20 22:00 | 3241266 | 5 | 8.0095 | 18.3405 | -114.0616 | 10.1245 | 142.9145 | 0.0026 | 0.0073 |
| 2024_09_20 22:00 | 3224651 | 6 | 8.7555 | 5.6448 | -114.0729 | 13.7249 | 172.8288 | 0.0065 | 0.0082 |
| 2024_09_20 22:00 | 3233367 | 7 | 7.7134 | 19.5891 | -115.8520 | 3.4305 | 26.1066 | 0.0119 | 0.0147 |
| 2024_09_20 22:00 | 3273815 | 8 | 9.5907 | 19.4287 | -115.7969 | 4.0432 | 29.0713 | 0.0097 | 0.0168 |
| 2024_09_20 22:00 | 3267591 | 9 | 16.5003 | 17.3623 | -115.9330 | 4.3939 | 31.4758 | 0.0066 | 0.0145 |
| 2024_09_20 22:00 | 3231818 | 10 | 18.5815 | 12.1216 | -114.6466 | 4.9617 | 33.4541 | 0.0102 | 0.0005 |
| 2024_09_20 22:00 | 3259654 | 11 | 15.6640 | 13.3308 | -117.6639 | 3.1056 | 25.1809 | 0.0029 | 0.0040 |
| 2024_09_20 22:00 | 3213450 | 12 | 8.7430 | 7.2428 | -117.2771 | 3.2518 | 23.9670 | 0.0196 | 0.0088 |
| 2024_09_20 22:00 | 3227710 | 13 | 14.8545 | 11.1286 | -117.6488 | 3.5311 | 49.8832 | 0.0147 | 0.0194 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414579_B3257B43 | 152650 | 995 | -85.8 | 152650 | 468 | -88.1 | 152650 | 691 | -97.3 | 152650 | 635 |
| MR_1774414579_F9AD3FE1 | 152650 | 995 | -88.2 | 152650 | 468 | -88.5 | 152650 | 691 | -99.6 | 152650 | 635 |
| MR_1774414579_6E57FCC3 | 152650 | 995 | -88.3 | 152650 | 468 | -88.7 | 152650 | 691 | -100.3 | 152650 | 635 |
| MR_1774414579_8965F3CC | 152650 | 995 | -85.6 | 152650 | 468 | -87.9 | 152650 | 691 | -97.9 | 152650 | 635 |
| MR_1774414579_F5730B38 | 152650 | 995 | -85.5 | 152650 | 468 | -90.2 | 152650 | 691 | -99.8 | 152650 | 635 |
| MR_1774414579_25F4EC95 | 504990 | 350 | -94.7 | 504990 | 346 | -93.8 | 504990 | 3 | -98.4 | 504990 | 116 |
| MR_1774414579_D530CE46 | 152650 | 995 | -85.5 | 152650 | 468 | -88.9 | 152650 | 691 | -97.1 | 152650 | 635 |
| MR_1774414579_E87DC396 | 504990 | 350 | -93.0 | 504990 | 346 | -97.6 | 504990 | 3 | -100.8 | 504990 | 116 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 134: `f3a0ae80-aea...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `f3a0ae80-aea9-416c-8f89-953d49610a85` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[134] topology](images/test_0134.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment.
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3245871_4
- `C3`: Increase A3 Offset threshold for 3245871_4
- `C4`: Press down the tilt angle  of 3245871_4 by 8 degrees
- `C5`: Decrease transmission power for 3245871_4
- `C6`: Increase A3 Offset threshold for 3226766_2
- `C7`: Check test server and transmission issues
- `C8`: Increase transmission power for 3226766_2
- `C9`: Add neighbor relationship between 3226766_2 and 3245871_4
- `C10`: Decrease A3 Offset threshold for 3226766_2
- `C11`: Adjust the azimuth of 3245871_4 by 50 degrees
- `C12`: Adjust the azimuth of 3226766_2 by 47 degrees
- `C13`: Press down the tilt angle of 3226766_2 by 10 degrees
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3245871_4
- `C15`: Lift the tilt angle of 3226766_2 by 10 degrees
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3226766_2
- `C17`: Decrease A3 Offset threshold for 3245871_4
- `C18`: Add neighbor relationship between 3272419_1 and 3245871_4
- `C19`: Increase transmission power for 3245871_4
- `C20`: Lift the tilt angle  of 3245871_4 by 8 degrees
- `C21`: Decrease transmission power for 3226766_2
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3226766_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.286 | MS1 | 121.4656726087 | 31.1446267333 | 967 | 504990 | -83.05 | 13.56 | 473.29 | 0.01 | 2.84 | 1593 |
| 2024-09-20 22:21:32.148 | MS1 | 121.4656751499 | 31.1446278784 | 967 | 504990 | -77.07 | 15.38 | 556.60 | 0.11 | 2.28 | 1595 |
| 2024-09-20 22:21:33.240 | MS1 | 121.4656677376 | 31.1446183138 | 967 | 504990 | -77.60 | 15.92 | 565.69 | 0.17 | 2.15 | 1563 |
| 2024-09-20 22:21:34.484 | MS1 | 121.4656722190 | 31.1446258057 | 967 | 504990 | -92.91 | -2.26 | 39.39 | 0.15 | 1.25 | 1561 |
| 2024-09-20 22:21:35.730 | MS1 | 121.4656610232 | 31.1446306105 | 967 | 504990 | -88.79 | -2.06 | 62.76 | 0.02 | 1.00 | 1588 |
| 2024-09-20 22:21:36.494 | MS1 | 121.4656775898 | 31.1446369911 | 967 | 504990 | -92.94 | -2.94 | 30.66 | 0.20 | 1.14 | 1565 |
| 2024-09-20 22:21:37.614 | MS1 | 121.4656609906 | 31.1446350709 | 967 | 504990 | -91.29 | -2.27 | 68.98 | 0.04 | 1.05 | 1564 |
| 2024-09-20 22:21:38.322 | MS1 | 121.4656740127 | 31.1446252479 | 967 | 504990 | -87.12 | -3.31 | 67.37 | 0.18 | 1.25 | 1577 |
| 2024-09-20 22:21:39.754 | MS1 | 121.4656777976 | 31.1446256147 | 399 | 504990 | -81.38 | 14.55 | 280.53 | 0.14 | 1.37 | 1582 |
| 2024-09-20 22:21:40.860 | MS1 | 121.4656762708 | 31.1446271901 | 399 | 504990 | -84.19 | 13.08 | 336.60 | 0.06 | 2.72 | 1564 |
| 2024-09-20 22:21:41.590 | MS1 | 121.4656607423 | 31.1446236970 | 399 | 504990 | -76.49 | 13.08 | 352.64 | 0.06 | 2.90 | 1572 |
| 2024-09-20 22:21:42.736 | MS1 | 121.4656728992 | 31.1446352464 | 399 | 504990 | -83.00 | 16.59 | 549.62 | 0.07 | 2.19 | 1575 |

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
| 3226766 | 2 | 121.4734658922 | 31.1489286396 | 284 | 15 | 11 | 22.6 | TDD | 967 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3236152 | 3 | 121.4759302909 | 31.1553633965 | 297 | 3 | 12 | 30.8 | TDD | 797 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3245871 | 4 | 121.4755468083 | 31.1516776624 | 89 | 6 | 6 | 49.9 | TDD | 399 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3272419 | 1 | 121.4727897825 | 31.1552798971 | 8 | 2 | 0 | 28.8 | TDD | 191 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |

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
| 2024-09-20 22:21:31.337 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.361 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.499 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.499 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.211 | NREventA3 | measId:2;ServCellPCI:99;Ser... |
| 2024-09-20 22:21:38.451 | NRHandoverAttempt | SourcePCI:99;SourceNR-ARFCN... |
| 2024-09-20 22:21:38.491 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.503 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.630 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.630 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3272419 | 1 | 14.4750 | 15.4465 | -117.6203 | 19.1207 | 95.6553 | 0.0178 | 0.0088 |
| 2024_09_20 22:00 | 3226766 | 2 | 17.2258 | 14.5567 | -114.3923 | 16.6043 | 80.4155 | 0.0194 | 0.1383 |
| 2024_09_20 22:00 | 3236152 | 3 | 17.2351 | 12.8986 | -115.3575 | 6.4936 | 143.9253 | 0.0175 | 0.0133 |
| 2024_09_20 22:00 | 3245871 | 4 | 9.9166 | 14.8258 | -115.7174 | 13.1417 | 151.8327 | 0.0197 | 0.0192 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412971_AF44D56A | 504990 | 399 | -86.2 | 504990 | 967 | -93.4 | 504990 | 191 | -97.4 | 504990 | 797 |
| MR_1774412971_AB03A36D | 504990 | 967 | -92.3 | 504990 | 399 | -86.4 | 504990 | 191 | -95.4 | 504990 | 797 |
| MR_1774412971_5D7D13E3 | 504990 | 967 | -94.5 | 504990 | 399 | -89.0 | 504990 | 191 | -95.4 | 504990 | 797 |
| MR_1774412971_A72AE51F | 504990 | 967 | -93.2 | 504990 | 399 | -87.3 | 504990 | 191 | -96.2 | 504990 | 797 |
| MR_1774412971_EE1F8D0B | 504990 | 967 | -91.9 | 504990 | 399 | -86.1 | 504990 | 191 | -96.5 | 504990 | 797 |
| MR_1774412971_93A20382 | 504990 | 967 | -91.1 | 504990 | 399 | -86.8 | 504990 | 191 | -95.8 | 504990 | 797 |
| MR_1774412971_4D3C1A32 | 504990 | 399 | -88.4 | 504990 | 967 | -94.1 | 504990 | 191 | -96.0 | 504990 | 797 |
| MR_1774412971_F7BB1752 | 504990 | 967 | -91.0 | 504990 | 399 | -89.0 | 504990 | 191 | -97.7 | 504990 | 797 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 135: `40e306bc-411...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `40e306bc-4110-4efc-9a01-48fd671429b0` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[135] topology](images/test_0135.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment.
- `C2`: Add neighbor relationship between 3224021_1 and 3269129_3
- `C3`: Decrease A3 Offset threshold for 3224021_1
- `C4`: Lift the tilt angle  of 3269129_3 by 3 degrees
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3269129_3
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3224021_1
- `C7`: Increase A3 Offset threshold for 3269129_3
- `C8`: Adjust the azimuth of 3269129_3 by 26 degrees
- `C9`: Press down the tilt angle of 3224021_1 by 8 degrees
- `C10`: Increase transmission power for 3269129_3
- `C11`: Increase A3 Offset threshold for 3224021_1
- `C12`: Check test server and transmission issues
- `C13`: Add neighbor relationship between 3217814_2 and 3269129_3
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3224021_1
- `C15`: Decrease transmission power for 3224021_1
- `C16`: Decrease transmission power for 3269129_3
- `C17`: Decrease A3 Offset threshold for 3269129_3
- `C18`: Adjust the azimuth of 3224021_1 by 50 degrees
- `C19`: Press down the tilt angle  of 3269129_3 by 3 degrees
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3269129_3
- `C21`: Lift the tilt angle of 3224021_1 by 8 degrees
- `C22`: Increase transmission power for 3224021_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.734 | MS1 | 121.4656759488 | 31.1446191056 | 920 | 504990 | -89.48 | 15.98 | 398.68 | 0.02 | 2.58 | 1576 |
| 2024-09-20 22:21:32.590 | MS1 | 121.4656706901 | 31.1446197175 | 920 | 504990 | -89.59 | 13.11 | 524.37 | 0.01 | 2.24 | 1595 |
| 2024-09-20 22:21:33.584 | MS1 | 121.4656776492 | 31.1446223267 | 920 | 504990 | -90.89 | 15.12 | 527.59 | 0.08 | 2.97 | 1574 |
| 2024-09-20 22:21:34.456 | MS1 | 121.4656589106 | 31.1446193363 | 920 | 504990 | -89.22 | 17.86 | 66.50 | 0.04 | 2.48 | 446 |
| 2024-09-20 22:21:35.484 | MS1 | 121.4656662586 | 31.1446212439 | 920 | 504990 | -91.20 | 12.07 | 82.20 | 0.02 | 2.26 | 371 |
| 2024-09-20 22:21:36.529 | MS1 | 121.4656632073 | 31.1446239434 | 920 | 504990 | -91.07 | 16.95 | 55.70 | 0.02 | 2.79 | 312 |
| 2024-09-20 22:21:37.355 | MS1 | 121.4656710751 | 31.1446238740 | 920 | 504990 | -93.57 | 7.04 | 61.30 | 0.03 | 2.98 | 338 |
| 2024-09-20 22:21:38.567 | MS1 | 121.4656760276 | 31.1446323916 | 920 | 504990 | -92.02 | 11.17 | 94.58 | 0.18 | 2.47 | 373 |
| 2024-09-20 22:21:39.958 | MS1 | 121.4656632655 | 31.1446236649 | 920 | 504990 | -89.42 | 8.20 | 68.38 | 0.09 | 2.45 | 317 |
| 2024-09-20 22:21:40.874 | MS1 | 121.4656658715 | 31.1446235292 | 920 | 504990 | -90.69 | 7.25 | 591.74 | 0.08 | 2.38 | 1600 |
| 2024-09-20 22:21:41.868 | MS1 | 121.4656775081 | 31.1446340933 | 920 | 504990 | -93.86 | 7.04 | 327.95 | 0.16 | 2.13 | 1586 |
| 2024-09-20 22:21:42.238 | MS1 | 121.4656655572 | 31.1446218664 | 920 | 504990 | -93.32 | 7.12 | 553.77 | 0.06 | 2.29 | 1582 |

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
| 3211109 | 4 | 121.4720992545 | 31.1529278947 | 195 | 4 | 1 | 17.7 | TDD | 49 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3217814 | 2 | 121.4682779549 | 31.1523275514 | 141 | 12 | 12 | 48.5 | TDD | 401 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3224021 | 1 | 121.4664182509 | 31.1534992571 | 267 | 6 | 4 | 33.8 | TDD | 920 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3269129 | 3 | 121.4691123053 | 31.1515391676 | 177 | 1 | 4 | 24.3 | TDD | 167 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |

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
| 2024-09-20 22:21:31.195 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.215 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.353 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.353 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.089 | NREventA3 | measId:2;ServCellPCI:363;Se... |
| 2024-09-20 22:21:38.329 | NRHandoverAttempt | SourcePCI:363;SourceNR-ARFC... |
| 2024-09-20 22:21:38.370 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.384 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.501 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.501 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3224021 | 1 | 11.1461 | 12.6246 | -115.9505 | 14.1998 | 97.4636 | 0.0177 | 0.0033 |
| 2024_09_20 22:00 | 3217814 | 2 | 14.9260 | 8.5741 | -116.1110 | 13.9523 | 114.7993 | 0.0005 | 0.0127 |
| 2024_09_20 22:00 | 3269129 | 3 | 12.1804 | 8.0702 | -115.0884 | 12.1202 | 194.7735 | 0.0082 | 0.0005 |
| 2024_09_20 22:00 | 3211109 | 4 | 12.9778 | 5.3086 | -116.2220 | 10.7380 | 81.4770 | 0.0194 | 0.0038 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417036_D11D2E04 | 504990 | 920 | -90.0 | 504990 | 167 | -89.2 | 504990 | 401 | -98.4 | 504990 | 49 |
| MR_1774417036_D42EBCB8 | 504990 | 920 | -87.6 | 504990 | 167 | -91.1 | 504990 | 401 | -99.0 | 504990 | 49 |
| MR_1774417036_19ED91D3 | 504990 | 920 | -89.2 | 504990 | 167 | -92.0 | 504990 | 401 | -97.4 | 504990 | 49 |
| MR_1774417036_E614DABC | 504990 | 920 | -87.7 | 504990 | 167 | -88.6 | 504990 | 401 | -98.2 | 504990 | 49 |
| MR_1774417036_95C023D6 | 504990 | 920 | -87.5 | 504990 | 167 | -89.2 | 504990 | 401 | -98.7 | 504990 | 49 |
| MR_1774417036_1F06B029 | 504990 | 920 | -89.8 | 504990 | 167 | -92.1 | 504990 | 401 | -98.0 | 504990 | 49 |
| MR_1774417036_C789F84A | 504990 | 920 | -91.1 | 504990 | 167 | -88.4 | 504990 | 401 | -98.4 | 504990 | 49 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 136: `6074cfac-e2e...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `6074cfac-e2e7-4207-ba0f-14c3361097da` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[136] topology](images/test_0136.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3278183_4 by 1 degrees
- `C2`: Lift the tilt angle of 3256063_1 by 4 degrees
- `C3`: Adjust the azimuth of 3256063_1 by 7 degrees
- `C4`: Increase transmission power for 3278183_4
- `C5`: Check test server and transmission issues
- `C6`: Lift the tilt angle  of 3278183_4 by 1 degrees
- `C7`: Add neighbor relationship between 3210403_3 and 3278183_4
- `C8`: Decrease transmission power for 3256063_1
- `C9`: Adjust the azimuth of 3278183_4 by 50 degrees
- `C10`: Decrease A3 Offset threshold for 3256063_1
- `C11`: Increase transmission power for 3256063_1
- `C12`: Add neighbor relationship between 3256063_1 and 3278183_4
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3256063_1
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3278183_4
- `C15`: Insufficient data; more data is needed for judgment.
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3256063_1
- `C17`: Increase A3 Offset threshold for 3278183_4
- `C18`: Press down the tilt angle of 3256063_1 by 4 degrees
- `C19`: Increase A3 Offset threshold for 3256063_1
- `C20`: Decrease A3 Offset threshold for 3278183_4
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3278183_4
- `C22`: Decrease transmission power for 3278183_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.664 | MS1 | 121.4656649595 | 31.1446361874 | 617 | 504990 | -85.76 | 16.01 | 512.34 | 0.04 | 2.40 | 1599 |
| 2024-09-20 22:21:32.622 | MS1 | 121.4656766360 | 31.1446187075 | 617 | 504990 | -87.50 | 12.60 | 459.38 | 0.11 | 2.00 | 1586 |
| 2024-09-20 22:21:33.826 | MS1 | 121.4656705864 | 31.1446190049 | 617 | 504990 | -86.97 | 12.91 | 391.18 | 0.17 | 2.88 | 1600 |
| 2024-09-20 22:21:34.292 | MS1 | 121.4656769836 | 31.1446354303 | 617 | 504990 | -90.63 | 16.45 | 75.08 | 0.01 | 2.15 | 1599 |
| 2024-09-20 22:21:35.194 | MS1 | 121.4656748959 | 31.1446223828 | 617 | 504990 | -89.37 | 12.62 | 95.16 | 0.08 | 2.67 | 1594 |
| 2024-09-20 22:21:36.143 | MS1 | 121.4656594426 | 31.1446351795 | 617 | 504990 | -90.60 | 15.86 | 44.22 | 0.12 | 2.59 | 1572 |
| 2024-09-20 22:21:37.665 | MS1 | 121.4656755177 | 31.1446236043 | 617 | 504990 | -90.80 | 12.42 | 72.24 | 0.09 | 2.55 | 1573 |
| 2024-09-20 22:21:38.491 | MS1 | 121.4656599459 | 31.1446330650 | 617 | 504990 | -92.92 | 11.86 | 91.54 | 0.19 | 2.44 | 1568 |
| 2024-09-20 22:21:39.978 | MS1 | 121.4656657830 | 31.1446293600 | 617 | 504990 | -89.75 | 12.90 | 81.85 | 0.01 | 2.20 | 1569 |
| 2024-09-20 22:21:40.760 | MS1 | 121.4656750240 | 31.1446342714 | 617 | 504990 | -93.05 | 11.73 | 320.17 | 0.03 | 2.90 | 1560 |
| 2024-09-20 22:21:41.687 | MS1 | 121.4656669332 | 31.1446255559 | 617 | 504990 | -92.64 | 10.52 | 359.15 | 0.19 | 2.85 | 1577 |
| 2024-09-20 22:21:42.256 | MS1 | 121.4656597661 | 31.1446209858 | 617 | 504990 | -89.52 | 8.50 | 583.28 | 0.20 | 2.52 | 1565 |

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
| 3210403 | 3 | 121.4753636988 | 31.1508629349 | 74 | 12 | 7 | 33.5 | TDD | 740 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3252148 | 2 | 121.4755641779 | 31.1466222153 | 265 | 2 | 1 | 32.3 | TDD | 153 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3256063 | 1 | 121.4744478665 | 31.1484383956 | 236 | 2 | 7 | 33.5 | TDD | 617 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3278183 | 4 | 121.4694800982 | 31.1557571321 | 5 | 0 | 3 | 31.4 | TDD | 493 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:31.640 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.660 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.799 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.799 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.495 | NREventA3 | measId:2;ServCellPCI:357;Se... |
| 2024-09-20 22:21:38.735 | NRHandoverAttempt | SourcePCI:357;SourceNR-ARFC... |
| 2024-09-20 22:21:38.780 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.795 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.941 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.941 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3256063 | 1 | 86.4831 | 79.3037 | -117.0092 | 6.3444 | 164.5918 | 0.0030 | 0.0200 |
| 2024_09_19 22:00 | 3252148 | 2 | 82.2819 | 93.5877 | -117.6698 | 7.8982 | 199.8686 | 0.0025 | 0.0035 |
| 2024_09_19 22:00 | 3210403 | 3 | 83.1143 | 86.6398 | -116.6054 | 15.7275 | 122.2258 | 0.0129 | 0.0112 |
| 2024_09_19 22:00 | 3278183 | 4 | 80.7407 | 86.8689 | -116.6877 | 14.1929 | 127.6981 | 0.0028 | 0.0163 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413643_9AF763CA | 504990 | 617 | -88.9 | 504990 | 493 | -97.1 | 504990 | 740 | -98.9 | 504990 | 153 |
| MR_1774413643_8196C047 | 504990 | 617 | -89.7 | 504990 | 493 | -97.8 | 504990 | 740 | -100.8 | 504990 | 153 |
| MR_1774413643_04996BFC | 504990 | 617 | -89.0 | 504990 | 493 | -96.9 | 504990 | 740 | -99.3 | 504990 | 153 |
| MR_1774413643_5732DC72 | 504990 | 617 | -90.2 | 504990 | 493 | -95.4 | 504990 | 740 | -100.1 | 504990 | 153 |
| MR_1774413643_8C433026 | 504990 | 617 | -91.8 | 504990 | 493 | -96.3 | 504990 | 740 | -101.3 | 504990 | 153 |
| MR_1774413643_35AACAA0 | 504990 | 617 | -92.1 | 504990 | 493 | -95.3 | 504990 | 740 | -99.4 | 504990 | 153 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 137: `04d5399b-13d...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `04d5399b-13dd-4878-bf24-f420290476a1` |
| Tag | **multiple-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[137] topology](images/test_0137.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3274250_3 by 5 degrees
- `C2`: Adjust the azimuth of 3274250_3 by 28 degrees
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3274250_3
- `C4`: Add neighbor relationship between 3255328_2 and 3274250_3
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3274250_3
- `C6`: Decrease transmission power for 3274250_3
- `C7`: Decrease A3 Offset threshold for 3274250_3
- `C8`: Adjust the azimuth of 3255328_2 by 39 degrees
- `C9`: Decrease transmission power for 3255328_2
- `C10`: Lift the tilt angle of 3255328_2 by 5 degrees
- `C11`: Insufficient data; more data is needed for judgment.
- `C12`: Add neighbor relationship between 3261836_4 and 3274250_3
- `C13`: Press down the tilt angle of 3255328_2 by 5 degrees
- `C14`: Check test server and transmission issues
- `C15`: Increase A3 Offset threshold for 3274250_3
- `C16`: Increase transmission power for 3255328_2
- `C17`: Increase transmission power for 3274250_3
- `C18`: Lift the tilt angle  of 3274250_3 by 5 degrees
- `C19`: Decrease A3 Offset threshold for 3255328_2
- `C20`: Increase A3 Offset threshold for 3255328_2
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3255328_2
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3255328_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.856 | MS1 | 121.4656722880 | 31.1446295714 | 53 | 504990 | -75.74 | 13.10 | 366.24 | 0.05 | 2.46 | 1564 |
| 2024-09-20 22:21:32.961 | MS1 | 121.4656628923 | 31.1446283603 | 53 | 504990 | -75.72 | 17.02 | 426.61 | 0.06 | 2.43 | 1569 |
| 2024-09-20 22:21:33.460 | MS1 | 121.4656702823 | 31.1446326893 | 53 | 504990 | -75.86 | 14.38 | 401.79 | 0.11 | 2.82 | 1568 |
| 2024-09-20 22:21:34.160 | MS1 | 121.4656646626 | 31.1446297501 | 53 | 504990 | -91.10 | 1.13 | 90.75 | 0.17 | 1.37 | 1573 |
| 2024-09-20 22:21:35.477 | MS1 | 121.4656608915 | 31.1446217512 | 53 | 504990 | -92.12 | 1.87 | 59.00 | 0.18 | 1.01 | 1576 |
| 2024-09-20 22:21:36.435 | MS1 | 121.4656588813 | 31.1446207944 | 53 | 504990 | -89.06 | 0.04 | 73.95 | 0.13 | 1.41 | 1589 |
| 2024-09-20 22:21:37.620 | MS1 | 121.4656606255 | 31.1446312754 | 53 | 504990 | -93.32 | 2.03 | 53.45 | 0.01 | 1.06 | 1583 |
| 2024-09-20 22:21:38.530 | MS1 | 121.4656608394 | 31.1446319994 | 53 | 504990 | -87.98 | 0.92 | 78.03 | 0.08 | 1.47 | 1567 |
| 2024-09-20 22:21:39.955 | MS1 | 121.4656656893 | 31.1446319260 | 53 | 504990 | -89.39 | 0.67 | 73.92 | 0.16 | 1.35 | 1575 |
| 2024-09-20 22:21:40.563 | MS1 | 121.4656686524 | 31.1446244169 | 53 | 504990 | -78.88 | 15.79 | 430.91 | 0.17 | 2.06 | 1571 |
| 2024-09-20 22:21:41.293 | MS1 | 121.4656673965 | 31.1446312128 | 53 | 504990 | -76.48 | 16.55 | 377.13 | 0.13 | 2.76 | 1598 |
| 2024-09-20 22:21:42.152 | MS1 | 121.4656681671 | 31.1446340246 | 53 | 504990 | -81.72 | 16.08 | 456.86 | 0.04 | 2.48 | 1581 |

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
| 3223308 | 1 | 121.4736095567 | 31.1500275533 | 163 | 11 | 5 | 43.3 | TDD | 666 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3255328 | 2 | 121.4685105454 | 31.1527389732 | 158 | 3 | 7 | 29.4 | TDD | 53 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3261836 | 4 | 121.4751355893 | 31.1551484627 | 354 | 13 | 4 | 21.8 | TDD | 655 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3274250 | 3 | 121.4693492462 | 31.1468182804 | 207 | 0 | 10 | 36.5 | TDD | 599 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |

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
| 2024-09-20 22:21:31.104 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.127 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.274 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.274 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3223308 | 1 | 8.2344 | 17.7638 | -117.3217 | 5.0460 | 191.3049 | 0.0180 | 0.0163 |
| 2024_09_20 22:00 | 3255328 | 2 | 12.6140 | 17.8338 | -108.2949 | 13.7253 | 88.5785 | 0.0183 | 0.0031 |
| 2024_09_20 22:00 | 3274250 | 3 | 10.3334 | 6.0060 | -116.5336 | 10.3758 | 129.1729 | 0.0067 | 0.0185 |
| 2024_09_20 22:00 | 3261836 | 4 | 16.0349 | 7.5807 | -116.6160 | 12.8841 | 154.4976 | 0.0166 | 0.0118 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413121_898DBC12 | 504990 | 599 | -90.4 | 504990 | 53 | -86.8 | 504990 | 655 | -90.2 | 504990 | 666 |
| MR_1774413121_6B1DE141 | 504990 | 599 | -90.3 | 504990 | 53 | -89.3 | 504990 | 655 | -90.5 | 504990 | 666 |
| MR_1774413121_8FC7AE38 | 504990 | 53 | -91.3 | 504990 | 599 | -87.3 | 504990 | 655 | -91.3 | 504990 | 666 |
| MR_1774413121_C3DF6166 | 504990 | 53 | -92.7 | 504990 | 599 | -88.7 | 504990 | 655 | -92.2 | 504990 | 666 |
| MR_1774413121_C8687B4A | 504990 | 599 | -90.4 | 504990 | 53 | -86.1 | 504990 | 655 | -93.0 | 504990 | 666 |
| MR_1774413121_E113B501 | 504990 | 599 | -90.4 | 504990 | 53 | -89.1 | 504990 | 655 | -92.7 | 504990 | 666 |
| MR_1774413121_B2A166D6 | 504990 | 599 | -92.5 | 504990 | 53 | -88.1 | 504990 | 655 | -90.0 | 504990 | 666 |
| MR_1774413121_BBA35F11 | 504990 | 53 | -90.0 | 504990 | 599 | -86.3 | 504990 | 655 | -90.6 | 504990 | 666 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 138: `fca75eb4-a6a...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `fca75eb4-a6a8-44f0-961c-38fd3d1782d1` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[138] topology](images/test_0138.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3242265_2 by 3 degrees
- `C2`: Insufficient data; more data is needed for judgment.
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3261423_3
- `C4`: Lift the tilt angle  of 3228182_4 by 8 degrees
- `C5`: Check test server and transmission issues
- `C6`: Press down the tilt angle  of 3228182_4 by 8 degrees
- `C7`: Decrease A3 Offset threshold for 3261423_3
- `C8`: Decrease transmission power for 3261423_3
- `C9`: Press down the tilt angle of 3242265_2 by 3 degrees
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3242265_2
- `C11`: Decrease transmission power for 3242265_2
- `C12`: Increase transmission power for 3261423_3
- `C13`: Increase transmission power for 3242265_2
- `C14`: Decrease A3 Offset threshold for 3242265_2
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3242265_2
- `C16`: Add neighbor relationship between 3242265_2 and 3261423_3
- `C17`: Increase A3 Offset threshold for 3242265_2
- `C18`: Adjust the azimuth of 3242265_2 by 37 degrees
- `C19`: Increase A3 Offset threshold for 3261423_3
- `C20`: Add neighbor relationship between 3228182_4 and 3261423_3
- `C21`: Adjust the azimuth of 3228182_4 by 34 degrees
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3261423_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.633 | MS1 | 121.4656632555 | 31.1446252575 | 698 | 504990 | -85.39 | 16.99 | 329.13 | 0.09 | 2.51 | 1596 |
| 2024-09-20 22:21:32.923 | MS1 | 121.4656605579 | 31.1446269396 | 698 | 504990 | -90.33 | 13.60 | 525.82 | 0.20 | 2.58 | 1574 |
| 2024-09-20 22:21:33.778 | MS1 | 121.4656749607 | 31.1446289833 | 698 | 504990 | -85.05 | 12.63 | 420.62 | 0.08 | 2.58 | 1574 |
| 2024-09-20 22:21:34.470 | MS1 | 121.4656731190 | 31.1446319091 | 698 | 504990 | -90.48 | 15.59 | 88.54 | 0.16 | 2.07 | 1577 |
| 2024-09-20 22:21:35.442 | MS1 | 121.4656698070 | 31.1446352941 | 698 | 504990 | -85.39 | 17.07 | 79.10 | 0.09 | 2.58 | 1595 |
| 2024-09-20 22:21:36.425 | MS1 | 121.4656634806 | 31.1446341978 | 698 | 504990 | -88.87 | 16.54 | 62.50 | 0.05 | 2.95 | 1592 |
| 2024-09-20 22:21:37.448 | MS1 | 121.4656647410 | 31.1446228954 | 698 | 504990 | -92.44 | 12.92 | 85.63 | 0.07 | 2.31 | 1584 |
| 2024-09-20 22:21:38.211 | MS1 | 121.4656637224 | 31.1446313841 | 698 | 504990 | -92.41 | 10.03 | 90.62 | 0.03 | 2.41 | 1584 |
| 2024-09-20 22:21:39.915 | MS1 | 121.4656653049 | 31.1446332498 | 698 | 504990 | -90.88 | 12.58 | 51.23 | 0.04 | 2.68 | 1599 |
| 2024-09-20 22:21:40.674 | MS1 | 121.4656677664 | 31.1446283390 | 698 | 504990 | -91.12 | 12.33 | 585.52 | 0.18 | 2.30 | 1572 |
| 2024-09-20 22:21:41.449 | MS1 | 121.4656634311 | 31.1446308425 | 698 | 504990 | -93.59 | 11.33 | 331.35 | 0.12 | 2.81 | 1588 |
| 2024-09-20 22:21:42.221 | MS1 | 121.4656593443 | 31.1446227285 | 698 | 504990 | -92.55 | 12.19 | 533.39 | 0.02 | 2.76 | 1575 |

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
| 3228182 | 4 | 121.4750337395 | 31.1517664539 | 25 | 15 | 12 | 16.5 | TDD | 61 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3242265 | 2 | 121.4700475606 | 31.1534956502 | 166 | 2 | 4 | 24.2 | TDD | 698 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3251562 | 1 | 121.4672591930 | 31.1456557995 | 149 | 6 | 8 | 31.5 | TDD | 680 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3261423 | 3 | 121.4723432996 | 31.1467347878 | 284 | 4 | 12 | 45.3 | TDD | 978 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |

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
| 2024-09-20 22:21:31.439 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.459 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.587 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.587 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.331 | NREventA3 | measId:2;ServCellPCI:780;Se... |
| 2024-09-20 22:21:38.571 | NRHandoverAttempt | SourcePCI:780;SourceNR-ARFC... |
| 2024-09-20 22:21:38.619 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.633 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.733 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.733 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3251562 | 1 | 12.2024 | 16.5112 | -115.0082 | 5.2247 | 138.7678 | 0.0049 | 0.0041 |
| 2024_09_20 22:00 | 3242265 | 2 | 86.5390 | 86.0948 | -115.8102 | 19.8055 | 105.1617 | 0.0033 | 0.0032 |
| 2024_09_20 22:00 | 3261423 | 3 | 15.3590 | 9.7686 | -116.6502 | 6.9143 | 116.2851 | 0.0008 | 0.0043 |
| 2024_09_20 22:00 | 3228182 | 4 | 9.5060 | 19.8050 | -115.6853 | 5.1061 | 172.3350 | 0.0131 | 0.0151 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415755_3C3B0871 | 504990 | 698 | -89.8 | 504990 | 978 | -97.6 | 504990 | 61 | -101.7 | 504990 | 680 |
| MR_1774415755_069AE7F0 | 504990 | 698 | -92.0 | 504990 | 978 | -96.8 | 504990 | 61 | -101.1 | 504990 | 680 |
| MR_1774415755_B22815D6 | 504990 | 698 | -91.7 | 504990 | 978 | -98.8 | 504990 | 61 | -101.2 | 504990 | 680 |
| MR_1774415755_CD7D8469 | 504990 | 698 | -91.4 | 504990 | 978 | -97.0 | 504990 | 61 | -104.3 | 504990 | 680 |
| MR_1774415755_5C4C912C | 504990 | 698 | -90.6 | 504990 | 978 | -99.0 | 504990 | 61 | -101.6 | 504990 | 680 |
| MR_1774415755_A6963160 | 504990 | 698 | -89.3 | 504990 | 978 | -98.9 | 504990 | 61 | -103.0 | 504990 | 680 |
| MR_1774415755_1CBA597F | 504990 | 698 | -90.7 | 504990 | 978 | -98.5 | 504990 | 61 | -104.1 | 504990 | 680 |
| MR_1774415755_29D5C489 | 504990 | 698 | -91.4 | 504990 | 978 | -98.4 | 504990 | 61 | -104.7 | 504990 | 680 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 139: `afa24180-af8...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `afa24180-af8d-4560-bb0e-2416d263b770` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[139] topology](images/test_0139.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3279541_1
- `C2`: Increase A3 Offset threshold for 3279541_1
- `C3`: Check test server and transmission issues
- `C4`: Decrease A3 Offset threshold for 3272400_2
- `C5`: Press down the tilt angle  of 3272400_2 by 10 degrees
- `C6`: Insufficient data; more data is needed for judgment.
- `C7`: Decrease A3 Offset threshold for 3279541_1
- `C8`: Add neighbor relationship between 3279541_1 and 3272400_2
- `C9`: Adjust the azimuth of 3279541_1 by 24 degrees
- `C10`: Decrease transmission power for 3279541_1
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3272400_2
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3279541_1
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3279541_1
- `C14`: Adjust the azimuth of 3272400_2 by 50 degrees
- `C15`: Increase transmission power for 3272400_2
- `C16`: Press down the tilt angle of 3279541_1 by 4 degrees
- `C17`: Increase A3 Offset threshold for 3272400_2
- `C18`: Add neighbor relationship between 3223269_4 and 3272400_2
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3272400_2
- `C20`: Decrease transmission power for 3272400_2
- `C21`: Lift the tilt angle  of 3272400_2 by 10 degrees
- `C22`: Lift the tilt angle of 3279541_1 by 4 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.922 | MS1 | 121.4656697379 | 31.1446331334 | 456 | 504990 | -90.68 | 17.48 | 339.77 | 0.17 | 2.01 | 1589 |
| 2024-09-20 22:21:32.636 | MS1 | 121.4656696884 | 31.1446281722 | 456 | 504990 | -88.73 | 17.02 | 366.38 | 0.05 | 2.92 | 1573 |
| 2024-09-20 22:21:33.522 | MS1 | 121.4656602743 | 31.1446367041 | 456 | 504990 | -85.85 | 14.26 | 325.09 | 0.03 | 2.10 | 1566 |
| 2024-09-20 22:21:34.110 | MS1 | 121.4656633139 | 31.1446191799 | 456 | 504990 | -87.56 | 12.46 | 85.72 | 0.63 | 2.48 | 601 |
| 2024-09-20 22:21:35.832 | MS1 | 121.4656736967 | 31.1446321575 | 456 | 504990 | -89.51 | 15.01 | 80.34 | 0.50 | 2.64 | 518 |
| 2024-09-20 22:21:36.480 | MS1 | 121.4656644872 | 31.1446189704 | 456 | 504990 | -87.36 | 16.68 | 95.02 | 0.59 | 2.29 | 584 |
| 2024-09-20 22:21:37.873 | MS1 | 121.4656643485 | 31.1446302938 | 456 | 504990 | -92.60 | 7.40 | 88.90 | 0.63 | 2.28 | 564 |
| 2024-09-20 22:21:38.570 | MS1 | 121.4656721765 | 31.1446240939 | 456 | 504990 | -89.78 | 7.13 | 70.08 | 0.65 | 2.73 | 696 |
| 2024-09-20 22:21:39.386 | MS1 | 121.4656605581 | 31.1446351899 | 456 | 504990 | -91.38 | 11.02 | 91.11 | 0.53 | 2.29 | 566 |
| 2024-09-20 22:21:40.310 | MS1 | 121.4656706648 | 31.1446210689 | 456 | 504990 | -92.52 | 9.87 | 487.29 | 0.19 | 2.28 | 1568 |
| 2024-09-20 22:21:41.193 | MS1 | 121.4656643969 | 31.1446290327 | 456 | 504990 | -93.37 | 11.45 | 492.36 | 0.18 | 2.75 | 1592 |
| 2024-09-20 22:21:42.321 | MS1 | 121.4656621421 | 31.1446291784 | 456 | 504990 | -89.69 | 7.03 | 455.77 | 0.09 | 2.74 | 1586 |

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
| 3223269 | 4 | 121.4683081313 | 31.1553179746 | 237 | 10 | 3 | 35.9 | TDD | 12 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3272400 | 2 | 121.4689594747 | 31.1448757218 | 73 | 15 | 9 | 35.6 | TDD | 913 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3272662 | 3 | 121.4745855775 | 31.1462005226 | 113 | 4 | 2 | 18.8 | TDD | 459 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3279541 | 1 | 121.4735333233 | 31.1471644127 | 273 | 1 | 0 | 39.4 | TDD | 456 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:31.288 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.313 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.455 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.455 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.164 | NREventA3 | measId:2;ServCellPCI:921;Se... |
| 2024-09-20 22:21:38.404 | NRHandoverAttempt | SourcePCI:921;SourceNR-ARFC... |
| 2024-09-20 22:21:38.436 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.446 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.560 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.560 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3279541 | 1 | 6.7543 | 5.5103 | -114.5797 | 10.9404 | 186.3018 | 0.0012 | 0.0168 |
| 2024_09_20 22:00 | 3272400 | 2 | 11.7901 | 10.1730 | -115.6983 | 8.5568 | 187.8064 | 0.0119 | 0.0058 |
| 2024_09_20 22:00 | 3272662 | 3 | 12.7989 | 9.2398 | -115.7993 | 7.9154 | 132.3187 | 0.0185 | 0.0051 |
| 2024_09_20 22:00 | 3223269 | 4 | 7.4459 | 15.5665 | -114.4473 | 12.2084 | 154.0333 | 0.0066 | 0.0106 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414635_30923D87 | 504990 | 456 | -85.7 | 504990 | 913 | -95.2 | 504990 | 12 | -101.6 | 504990 | 459 |
| MR_1774414635_77AC6E3C | 504990 | 456 | -87.7 | 504990 | 913 | -98.6 | 504990 | 12 | -101.4 | 504990 | 459 |
| MR_1774414635_DD713A6C | 504990 | 456 | -86.7 | 504990 | 913 | -98.5 | 504990 | 12 | -100.6 | 504990 | 459 |
| MR_1774414635_D1D719DE | 504990 | 456 | -85.6 | 504990 | 913 | -97.1 | 504990 | 12 | -99.9 | 504990 | 459 |
| MR_1774414635_EF52514E | 504990 | 456 | -86.4 | 504990 | 913 | -98.5 | 504990 | 12 | -99.1 | 504990 | 459 |

> *... 2개 열 생략 (전체 14열)*

---
