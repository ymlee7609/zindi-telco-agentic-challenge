# Track A 문제 분석 — test[350]~test[359]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/test.json`
> 범위: test[350] ~ test[359] (10개)

## 목차

1. [문제 350: `4bce96d9-0d8...`](#350) — single-answer
2. [문제 351: `16b206a7-202...`](#351) — single-answer
3. [문제 352: `69e49b75-5ee...`](#352) — single-answer
4. [문제 353: `f457bbd4-7a7...`](#353) — single-answer
5. [문제 354: `67cd4921-94f...`](#354) — single-answer
6. [문제 355: `794d2dec-0dc...`](#355) — single-answer
7. [문제 356: `e109a460-d8b...`](#356) — single-answer
8. [문제 357: `bc9fb314-bfb...`](#357) — multiple-answer
9. [문제 358: `9a762276-78d...`](#358) — single-answer
10. [문제 359: `2de48943-77b...`](#359) — single-answer

---

### 문제 350: `4bce96d9-0d8...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `4bce96d9-0d8f-41cc-958e-43e45ae91bff` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[350] topology](images/test_0350.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3255081_3
- `C2`: Increase A3 Offset threshold for 3255081_3
- `C3`: Press down the tilt angle of 3255081_3 by 10 degrees
- `C4`: Increase A3 Offset threshold for 3236506_4
- `C5`: Add neighbor relationship between 3255081_3 and 3236506_4
- `C6`: Increase transmission power for 3236506_4
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3255081_3
- `C8`: Adjust the azimuth of 3255081_3 by 32 degrees
- `C9`: Adjust the azimuth of 3236506_4 by 50 degrees
- `C10`: Add neighbor relationship between 3243685_1 and 3236506_4
- `C11`: Decrease transmission power for 3236506_4
- `C12`: Check test server and transmission issues
- `C13`: Lift the tilt angle of 3255081_3 by 10 degrees
- `C14`: Press down the tilt angle  of 3236506_4 by 10 degrees
- `C15`: Decrease A3 Offset threshold for 3255081_3
- `C16`: Decrease A3 Offset threshold for 3236506_4
- `C17`: Decrease transmission power for 3255081_3
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3236506_4
- `C19`: Increase transmission power for 3255081_3
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3236506_4
- `C21`: Insufficient data; more data is needed for judgment.
- `C22`: Lift the tilt angle  of 3236506_4 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.325 | MS1 | 121.4656662595 | 31.1446376553 | 349 | 504990 | -86.50 | 12.28 | 355.80 | 0.19 | 2.35 | 1569 |
| 2024-09-20 22:21:32.534 | MS1 | 121.4656585978 | 31.1446271224 | 349 | 504990 | -91.35 | 15.84 | 427.26 | 0.14 | 2.73 | 1596 |
| 2024-09-20 22:21:33.688 | MS1 | 121.4656675045 | 31.1446318915 | 349 | 504990 | -90.22 | 17.99 | 494.36 | 0.16 | 2.74 | 1587 |
| 2024-09-20 22:21:34.119 | MS1 | 121.4656634581 | 31.1446250829 | 349 | 504990 | -87.38 | 16.79 | 63.31 | 0.07 | 2.79 | 1566 |
| 2024-09-20 22:21:35.186 | MS1 | 121.4656711133 | 31.1446299341 | 349 | 504990 | -87.59 | 12.80 | 56.07 | 0.06 | 2.34 | 1568 |
| 2024-09-20 22:21:36.527 | MS1 | 121.4656762872 | 31.1446288372 | 349 | 504990 | -88.20 | 16.62 | 67.59 | 0.08 | 2.61 | 1587 |
| 2024-09-20 22:21:37.945 | MS1 | 121.4656724461 | 31.1446339064 | 349 | 504990 | -90.29 | 7.25 | 82.70 | 0.17 | 2.71 | 1564 |
| 2024-09-20 22:21:38.509 | MS1 | 121.4656763670 | 31.1446303724 | 349 | 504990 | -93.00 | 11.90 | 89.49 | 0.04 | 2.50 | 1572 |
| 2024-09-20 22:21:39.574 | MS1 | 121.4656724040 | 31.1446318898 | 349 | 504990 | -89.64 | 10.73 | 83.15 | 0.20 | 2.24 | 1578 |
| 2024-09-20 22:21:40.535 | MS1 | 121.4656706894 | 31.1446216664 | 349 | 504990 | -92.50 | 8.60 | 452.13 | 0.08 | 2.93 | 1578 |
| 2024-09-20 22:21:41.381 | MS1 | 121.4656646498 | 31.1446318262 | 349 | 504990 | -90.35 | 7.53 | 329.61 | 0.09 | 2.74 | 1593 |
| 2024-09-20 22:21:42.443 | MS1 | 121.4656732757 | 31.1446299823 | 349 | 504990 | -92.82 | 12.79 | 397.67 | 0.14 | 2.27 | 1594 |

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
| 3218364 | 2 | 121.4647743603 | 31.1557268010 | 57 | 7 | 5 | 20.0 | TDD | 840 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3236506 | 4 | 121.4641813648 | 31.1489157727 | 306 | 13 | 11 | 16.2 | TDD | 127 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3243685 | 1 | 121.4708723719 | 31.1490988769 | 27 | 15 | 10 | 25.2 | TDD | 656 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3255081 | 3 | 121.4661268024 | 31.1552108820 | 214 | 13 | 5 | 27.1 | TDD | 349 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:31.357 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.376 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.499 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.499 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.172 | NREventA3 | measId:2;ServCellPCI:173;Se... |
| 2024-09-20 22:21:38.412 | NRHandoverAttempt | SourcePCI:173;SourceNR-ARFC... |
| 2024-09-20 22:21:38.446 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.460 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.571 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.571 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3243685 | 1 | 82.5426 | 84.7382 | -115.2063 | 16.7236 | 83.2352 | 0.0159 | 0.0159 |
| 2024_09_19 22:00 | 3218364 | 2 | 86.6527 | 78.1408 | -115.8508 | 8.0997 | 154.2904 | 0.0154 | 0.0036 |
| 2024_09_19 22:00 | 3255081 | 3 | 89.3145 | 91.5913 | -114.8106 | 18.1016 | 120.8277 | 0.0083 | 0.0122 |
| 2024_09_19 22:00 | 3236506 | 4 | 89.0129 | 79.3332 | -117.6126 | 8.6269 | 141.2474 | 0.0102 | 0.0072 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416307_7485A1D5 | 504990 | 349 | -87.6 | 504990 | 127 | -88.4 | 504990 | 656 | -97.0 | 504990 | 840 |
| MR_1774416307_32554B9E | 504990 | 349 | -86.5 | 504990 | 127 | -90.8 | 504990 | 656 | -98.3 | 504990 | 840 |
| MR_1774416307_BFFB17FE | 504990 | 349 | -87.5 | 504990 | 127 | -89.5 | 504990 | 656 | -97.1 | 504990 | 840 |
| MR_1774416307_1A5A5143 | 504990 | 349 | -87.7 | 504990 | 127 | -90.8 | 504990 | 656 | -97.5 | 504990 | 840 |
| MR_1774416307_C009868C | 504990 | 349 | -86.9 | 504990 | 127 | -90.2 | 504990 | 656 | -96.5 | 504990 | 840 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 351: `16b206a7-202...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `16b206a7-2020-436d-9913-2b930f4bc8d8` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[351] topology](images/test_0351.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3227355_3
- `C2`: Adjust the azimuth of 3227355_3 by 50 degrees
- `C3`: Adjust the azimuth of 3234863_1 by 50 degrees
- `C4`: Decrease A3 Offset threshold for 3234863_1
- `C5`: Increase transmission power for 3227355_3
- `C6`: Press down the tilt angle of 3234863_1 by 1 degrees
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3234863_1
- `C8`: Decrease transmission power for 3227355_3
- `C9`: Increase A3 Offset threshold for 3234863_1
- `C10`: Decrease A3 Offset threshold for 3227355_3
- `C11`: Lift the tilt angle of 3234863_1 by 1 degrees
- `C12`: Check test server and transmission issues
- `C13`: Add neighbor relationship between 3242483_2 and 3227355_3
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3234863_1
- `C15`: Increase A3 Offset threshold for 3227355_3
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3227355_3
- `C17`: Lift the tilt angle  of 3227355_3 by 8 degrees
- `C18`: Decrease transmission power for 3234863_1
- `C19`: Add neighbor relationship between 3234863_1 and 3227355_3
- `C20`: Press down the tilt angle  of 3227355_3 by 8 degrees
- `C21`: Increase transmission power for 3234863_1
- `C22`: Insufficient data; more data is needed for judgment.

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.400 | MS1 | 121.4656731199 | 31.1446348111 | 210 | 504990 | -86.61 | 17.52 | 461.59 | 0.18 | 2.53 | 1578 |
| 2024-09-20 22:21:32.221 | MS1 | 121.4656692621 | 31.1446296993 | 210 | 504990 | -87.43 | 13.80 | 501.74 | 0.16 | 2.08 | 1589 |
| 2024-09-20 22:21:33.589 | MS1 | 121.4656745333 | 31.1446194953 | 210 | 504990 | -87.83 | 13.62 | 440.59 | 0.08 | 2.26 | 1561 |
| 2024-09-20 22:21:34.929 | MS1 | 121.4656679085 | 31.1446374623 | 210 | 504990 | -89.12 | 13.35 | 65.63 | 0.19 | 2.22 | 1563 |
| 2024-09-20 22:21:35.967 | MS1 | 121.4656754714 | 31.1446188719 | 210 | 504990 | -91.74 | 16.51 | 89.39 | 0.15 | 2.94 | 1579 |
| 2024-09-20 22:21:36.829 | MS1 | 121.4656760991 | 31.1446212375 | 210 | 504990 | -89.64 | 16.65 | 66.45 | 0.19 | 2.57 | 1577 |
| 2024-09-20 22:21:37.830 | MS1 | 121.4656632281 | 31.1446366858 | 210 | 504990 | -90.76 | 10.73 | 85.34 | 0.19 | 2.10 | 1589 |
| 2024-09-20 22:21:38.349 | MS1 | 121.4656633014 | 31.1446266135 | 210 | 504990 | -92.49 | 9.09 | 65.85 | 0.18 | 2.13 | 1591 |
| 2024-09-20 22:21:39.352 | MS1 | 121.4656623447 | 31.1446271333 | 210 | 504990 | -90.47 | 7.76 | 98.82 | 0.03 | 2.46 | 1570 |
| 2024-09-20 22:21:40.456 | MS1 | 121.4656724183 | 31.1446229067 | 210 | 504990 | -92.06 | 7.69 | 527.96 | 0.14 | 2.57 | 1563 |
| 2024-09-20 22:21:41.217 | MS1 | 121.4656711741 | 31.1446215992 | 210 | 504990 | -93.57 | 12.89 | 530.74 | 0.10 | 2.12 | 1580 |
| 2024-09-20 22:21:42.728 | MS1 | 121.4656732424 | 31.1446216867 | 210 | 504990 | -90.68 | 10.27 | 534.89 | 0.18 | 2.28 | 1561 |

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
| 3227355 | 3 | 121.4731484711 | 31.1480310714 | 81 | 6 | 7 | 27.4 | TDD | 354 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3234863 | 1 | 121.4732035011 | 31.1533394497 | 342 | 0 | 11 | 18.6 | TDD | 210 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3242483 | 2 | 121.4708057953 | 31.1514995309 | 182 | 3 | 2 | 27.2 | TDD | 262 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3253569 | 4 | 121.4748376977 | 31.1469270235 | 58 | 4 | 3 | 35.4 | TDD | 79 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |

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
| 2024-09-20 22:21:31.485 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.627 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.627 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.280 | NREventA3 | measId:2;ServCellPCI:267;Se... |
| 2024-09-20 22:21:38.520 | NRHandoverAttempt | SourcePCI:267;SourceNR-ARFC... |
| 2024-09-20 22:21:38.551 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.565 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.713 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.713 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3234863 | 1 | 90.3740 | 88.0514 | -114.9315 | 15.6205 | 149.5801 | 0.0158 | 0.0101 |
| 2024_09_19 22:00 | 3242483 | 2 | 75.5910 | 79.2860 | -114.3667 | 5.7504 | 170.0984 | 0.0090 | 0.0120 |
| 2024_09_19 22:00 | 3227355 | 3 | 92.8013 | 94.6573 | -115.8880 | 18.8934 | 164.1424 | 0.0190 | 0.0117 |
| 2024_09_19 22:00 | 3253569 | 4 | 75.7876 | 86.7467 | -115.0891 | 10.6260 | 120.4768 | 0.0039 | 0.0200 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414493_8C326CB9 | 504990 | 210 | -88.5 | 504990 | 354 | -96.4 | 504990 | 262 | -102.7 | 504990 | 79 |
| MR_1774414493_926B9EC3 | 504990 | 210 | -89.3 | 504990 | 354 | -95.3 | 504990 | 262 | -104.3 | 504990 | 79 |
| MR_1774414493_29A12814 | 504990 | 210 | -90.4 | 504990 | 354 | -97.4 | 504990 | 262 | -103.1 | 504990 | 79 |
| MR_1774414493_B495BE96 | 504990 | 210 | -89.7 | 504990 | 354 | -96.6 | 504990 | 262 | -102.4 | 504990 | 79 |
| MR_1774414493_59120FBD | 504990 | 210 | -87.9 | 504990 | 354 | -96.1 | 504990 | 262 | -101.6 | 504990 | 79 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 352: `69e49b75-5ee...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `69e49b75-5eee-454d-ba9a-125ac072c68a` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[352] topology](images/test_0352.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3267183_4 and 3218261_1
- `C2`: Check test server and transmission issues
- `C3`: Lift the tilt angle  of 3218261_1 by 10 degrees
- `C4`: Adjust the azimuth of 3218261_1 by 50 degrees
- `C5`: Increase transmission power for 3220882_2
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3220882_2
- `C7`: Increase A3 Offset threshold for 3218261_1
- `C8`: Lift the tilt angle of 3220882_2 by 10 degrees
- `C9`: Adjust the azimuth of 3220882_2 by 50 degrees
- `C10`: Decrease transmission power for 3218261_1
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3220882_2
- `C12`: Press down the tilt angle of 3220882_2 by 10 degrees
- `C13`: Decrease A3 Offset threshold for 3218261_1
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3218261_1
- `C16`: Decrease transmission power for 3220882_2
- `C17`: Increase A3 Offset threshold for 3220882_2
- `C18`: Press down the tilt angle  of 3218261_1 by 10 degrees
- `C19`: Increase transmission power for 3218261_1
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3218261_1
- `C21`: Decrease A3 Offset threshold for 3220882_2
- `C22`: Add neighbor relationship between 3220882_2 and 3218261_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.724 | MS1 | 121.4656744262 | 31.1446309593 | 171 | 504990 | -78.77 | 15.58 | 558.19 | 0.14 | 2.37 | 1573 |
| 2024-09-20 22:21:32.184 | MS1 | 121.4656734162 | 31.1446220213 | 171 | 504990 | -78.90 | 16.96 | 390.44 | 0.00 | 2.87 | 1584 |
| 2024-09-20 22:21:33.754 | MS1 | 121.4656687170 | 31.1446330251 | 171 | 504990 | -77.89 | 14.28 | 409.87 | 0.01 | 2.17 | 1570 |
| 2024-09-20 22:21:34.718 | MS1 | 121.4656723128 | 31.1446219505 | 171 | 504990 | -92.04 | -3.43 | 46.60 | 0.04 | 1.35 | 1568 |
| 2024-09-20 22:21:35.212 | MS1 | 121.4656724989 | 31.1446237424 | 171 | 504990 | -90.92 | -1.28 | 39.37 | 0.14 | 1.48 | 1582 |
| 2024-09-20 22:21:36.823 | MS1 | 121.4656620359 | 31.1446334511 | 171 | 504990 | -85.38 | -2.36 | 57.28 | 0.01 | 1.05 | 1583 |
| 2024-09-20 22:21:37.585 | MS1 | 121.4656670619 | 31.1446320857 | 171 | 504990 | -85.00 | -2.83 | 67.97 | 0.05 | 1.38 | 1598 |
| 2024-09-20 22:21:38.619 | MS1 | 121.4656618210 | 31.1446272992 | 171 | 504990 | -91.06 | -3.82 | 64.43 | 0.17 | 1.07 | 1571 |
| 2024-09-20 22:21:39.942 | MS1 | 121.4656585048 | 31.1446220916 | 618 | 504990 | -82.04 | 15.17 | 245.01 | 0.18 | 1.22 | 1568 |
| 2024-09-20 22:21:40.815 | MS1 | 121.4656766892 | 31.1446269771 | 618 | 504990 | -77.64 | 15.07 | 443.08 | 0.16 | 2.59 | 1562 |
| 2024-09-20 22:21:41.279 | MS1 | 121.4656695087 | 31.1446295283 | 618 | 504990 | -81.85 | 15.58 | 536.08 | 0.11 | 2.55 | 1597 |
| 2024-09-20 22:21:42.394 | MS1 | 121.4656695597 | 31.1446250164 | 618 | 504990 | -83.20 | 13.07 | 331.09 | 0.14 | 2.19 | 1561 |

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
| 3216189 | 3 | 121.4653796900 | 31.1498899097 | 93 | 12 | 0 | 15.2 | TDD | 403 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3218261 | 1 | 121.4668052577 | 31.1520036366 | 91 | 10 | 9 | 25.4 | TDD | 618 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3220882 | 2 | 121.4675427512 | 31.1484255921 | 322 | 9 | 1 | 34.6 | TDD | 171 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3267183 | 4 | 121.4649234837 | 31.1452050323 | 216 | 5 | 8 | 20.5 | TDD | 647 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |

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
| 2024-09-20 22:21:31.346 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.366 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.515 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.515 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.209 | NREventA3 | measId:2;ServCellPCI:662;Se... |
| 2024-09-20 22:21:38.449 | NRHandoverAttempt | SourcePCI:662;SourceNR-ARFC... |
| 2024-09-20 22:21:38.498 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.513 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.630 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.630 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3218261 | 1 | 10.4288 | 14.8408 | -117.7969 | 7.4310 | 139.8458 | 0.0008 | 0.0150 |
| 2024_09_20 22:00 | 3220882 | 2 | 7.7747 | 11.2126 | -116.8783 | 13.8557 | 81.9286 | 0.0114 | 0.1485 |
| 2024_09_20 22:00 | 3216189 | 3 | 7.8079 | 8.3508 | -116.2336 | 17.9680 | 192.6755 | 0.0187 | 0.0196 |
| 2024_09_20 22:00 | 3267183 | 4 | 10.2835 | 13.1509 | -117.1238 | 8.6592 | 107.8416 | 0.0084 | 0.0120 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774411967_215DB889 | 504990 | 618 | -87.6 | 504990 | 171 | -91.4 | 504990 | 647 | -89.7 | 504990 | 403 |
| MR_1774411967_5EE76CED | 504990 | 618 | -89.4 | 504990 | 171 | -91.0 | 504990 | 647 | -87.8 | 504990 | 403 |
| MR_1774411967_2CCF3435 | 504990 | 171 | -93.8 | 504990 | 618 | -88.3 | 504990 | 647 | -89.8 | 504990 | 403 |
| MR_1774411967_C5FC0319 | 504990 | 618 | -89.2 | 504990 | 171 | -91.7 | 504990 | 647 | -89.8 | 504990 | 403 |
| MR_1774411967_2CAC633B | 504990 | 618 | -86.4 | 504990 | 171 | -92.4 | 504990 | 647 | -88.9 | 504990 | 403 |
| MR_1774411967_2DBF05A1 | 504990 | 618 | -86.8 | 504990 | 171 | -91.4 | 504990 | 647 | -87.8 | 504990 | 403 |
| MR_1774411967_9916ED86 | 504990 | 618 | -89.5 | 504990 | 171 | -93.4 | 504990 | 647 | -87.0 | 504990 | 403 |
| MR_1774411967_63A50DE0 | 504990 | 171 | -91.0 | 504990 | 618 | -87.6 | 504990 | 647 | -89.1 | 504990 | 403 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 353: `f457bbd4-7a7...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `f457bbd4-7a7a-4deb-b21d-4c0f469d97bc` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[353] topology](images/test_0353.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3218854_1 by 50 degrees
- `C2`: Lift the tilt angle of 3218854_1 by 6 degrees
- `C3`: Check test server and transmission issues
- `C4`: Decrease transmission power for 3218854_1
- `C5`: Increase A3 Offset threshold for 3218854_1
- `C6`: Lift the tilt angle  of 3278419_2 by 6 degrees
- `C7`: Press down the tilt angle of 3218854_1 by 6 degrees
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3218854_1
- `C9`: Adjust the azimuth of 3278419_2 by 18 degrees
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3278419_2
- `C11`: Add neighbor relationship between 3218854_1 and 3278419_2
- `C12`: Decrease A3 Offset threshold for 3278419_2
- `C13`: Add neighbor relationship between 3227311_3 and 3278419_2
- `C14`: Press down the tilt angle  of 3278419_2 by 6 degrees
- `C15`: Increase A3 Offset threshold for 3278419_2
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3218854_1
- `C17`: Decrease transmission power for 3278419_2
- `C18`: Decrease A3 Offset threshold for 3218854_1
- `C19`: Increase transmission power for 3278419_2
- `C20`: Increase transmission power for 3218854_1
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3278419_2
- `C22`: Insufficient data; more data is needed for judgment.

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.259 | MS1 | 121.4656661642 | 31.1446247219 | 712 | 504990 | -79.04 | 16.42 | 524.22 | 0.01 | 2.83 | 1576 |
| 2024-09-20 22:21:32.938 | MS1 | 121.4656776662 | 31.1446276584 | 712 | 504990 | -77.72 | 15.71 | 583.16 | 0.06 | 2.32 | 1585 |
| 2024-09-20 22:21:33.511 | MS1 | 121.4656718519 | 31.1446371909 | 712 | 504990 | -82.49 | 12.55 | 302.40 | 0.19 | 2.07 | 1575 |
| 2024-09-20 22:21:34.177 | MS1 | 121.4656642481 | 31.1446379126 | 712 | 504990 | -90.31 | -2.46 | 42.20 | 0.03 | 1.42 | 1593 |
| 2024-09-20 22:21:35.373 | MS1 | 121.4656749385 | 31.1446187883 | 712 | 504990 | -89.05 | -0.43 | 46.52 | 0.07 | 1.36 | 1580 |
| 2024-09-20 22:21:36.395 | MS1 | 121.4656647689 | 31.1446320395 | 712 | 504990 | -93.42 | -0.70 | 46.53 | 0.19 | 1.00 | 1590 |
| 2024-09-20 22:21:37.333 | MS1 | 121.4656596108 | 31.1446196223 | 712 | 504990 | -85.33 | -2.38 | 33.71 | 0.07 | 1.35 | 1565 |
| 2024-09-20 22:21:38.228 | MS1 | 121.4656592267 | 31.1446263293 | 712 | 504990 | -78.16 | 12.95 | 553.41 | 0.12 | 1.14 | 1566 |
| 2024-09-20 22:21:39.153 | MS1 | 121.4656674042 | 31.1446207148 | 712 | 504990 | -79.70 | 15.98 | 543.53 | 0.14 | 1.28 | 1590 |
| 2024-09-20 22:21:40.305 | MS1 | 121.4656759383 | 31.1446356792 | 712 | 504990 | -84.36 | 17.77 | 349.90 | 0.05 | 2.39 | 1573 |
| 2024-09-20 22:21:41.278 | MS1 | 121.4656615775 | 31.1446375123 | 712 | 504990 | -82.64 | 15.43 | 566.51 | 0.15 | 2.65 | 1573 |
| 2024-09-20 22:21:42.839 | MS1 | 121.4656763697 | 31.1446234825 | 712 | 504990 | -83.97 | 16.58 | 358.77 | 0.08 | 2.56 | 1582 |

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
| 3218854 | 1 | 121.4702932022 | 31.1503431801 | 32 | 3 | 0 | 40.4 | TDD | 712 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3222398 | 4 | 121.4651024864 | 31.1524794348 | 116 | 12 | 10 | 38.2 | TDD | 693 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3227311 | 3 | 121.4661199670 | 31.1551235512 | 154 | 0 | 10 | 24.7 | TDD | 717 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3278419 | 2 | 121.4732047876 | 31.1553180711 | 229 | 4 | 9 | 44.3 | TDD | 401 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:31.063 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.209 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.209 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.937 | NREventA3 | measId:2;ServCellPCI:234;Se... |
| 2024-09-20 22:21:35.937 | NREventA3 | measId:2;ServCellPCI:234;Se... |
| 2024-09-20 22:21:36.937 | NREventA3 | measId:2;ServCellPCI:234;Se... |
| 2024-09-20 22:21:39.437 | NRRRCReestablishAttempt | PCI:234 |
| 2024-09-20 22:21:39.452 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.462 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:39.605 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.605 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3218854 | 1 | 10.3907 | 17.9721 | -116.4473 | 12.9678 | 81.7174 | 0.0180 | 0.1612 |
| 2024_09_20 22:00 | 3278419 | 2 | 12.7660 | 7.2582 | -114.4955 | 19.5040 | 191.4680 | 0.0071 | 0.0130 |
| 2024_09_20 22:00 | 3227311 | 3 | 18.3280 | 19.3209 | -117.7663 | 9.8374 | 193.5864 | 0.0144 | 0.0085 |
| 2024_09_20 22:00 | 3222398 | 4 | 16.0185 | 8.4682 | -116.6281 | 8.6308 | 162.8990 | 0.0121 | 0.0143 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412695_ECD3BFB1 | 504990 | 401 | -85.6 | 504990 | 712 | -92.0 | 504990 | 717 | -93.7 | 504990 | 693 |
| MR_1774412695_175DF729 | 504990 | 401 | -83.9 | 504990 | 712 | -91.9 | 504990 | 717 | -93.9 | 504990 | 693 |
| MR_1774412695_01ECE646 | 504990 | 401 | -85.8 | 504990 | 712 | -89.9 | 504990 | 717 | -91.9 | 504990 | 693 |
| MR_1774412695_57E09716 | 504990 | 712 | -90.9 | 504990 | 401 | -84.1 | 504990 | 717 | -93.0 | 504990 | 693 |
| MR_1774412695_FE542D71 | 504990 | 712 | -88.8 | 504990 | 401 | -85.3 | 504990 | 717 | -93.2 | 504990 | 693 |
| MR_1774412695_FC2230AD | 504990 | 712 | -91.9 | 504990 | 401 | -84.9 | 504990 | 717 | -95.6 | 504990 | 693 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 354: `67cd4921-94f...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `67cd4921-94f0-4f21-830a-350bb4b389e5` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[354] topology](images/test_0354.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3247079_3 by 9 degrees
- `C2`: Decrease transmission power for 3247079_3
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3247079_3
- `C4`: Press down the tilt angle  of 3278132_2 by 4 degrees
- `C5`: Decrease A3 Offset threshold for 3278132_2
- `C6`: Adjust the azimuth of 3278132_2 by 50 degrees
- `C7`: Insufficient data; more data is needed for judgment.
- `C8`: Increase transmission power for 3247079_3
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3278132_2
- `C10`: Decrease transmission power for 3278132_2
- `C11`: Add neighbor relationship between 3247079_3 and 3278132_2
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3278132_2
- `C13`: Increase transmission power for 3278132_2
- `C14`: Adjust the azimuth of 3247079_3 by 50 degrees
- `C15`: Decrease A3 Offset threshold for 3247079_3
- `C16`: Check test server and transmission issues
- `C17`: Increase A3 Offset threshold for 3247079_3
- `C18`: Lift the tilt angle  of 3278132_2 by 4 degrees
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3247079_3
- `C20`: Lift the tilt angle of 3247079_3 by 9 degrees
- `C21`: Increase A3 Offset threshold for 3278132_2
- `C22`: Add neighbor relationship between 3249097_4 and 3278132_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.743 | MS1 | 121.4656762084 | 31.1446198899 | 862 | 504990 | -86.38 | 17.33 | 571.52 | 0.05 | 2.91 | 1600 |
| 2024-09-20 22:21:32.857 | MS1 | 121.4656598318 | 31.1446359750 | 862 | 504990 | -90.30 | 16.43 | 321.01 | 0.03 | 2.90 | 1592 |
| 2024-09-20 22:21:33.650 | MS1 | 121.4656765797 | 31.1446327204 | 862 | 504990 | -86.91 | 14.80 | 338.63 | 0.10 | 2.20 | 1593 |
| 2024-09-20 22:21:34.241 | MS1 | 121.4656615070 | 31.1446312603 | 862 | 504990 | -88.86 | 16.68 | 64.37 | 0.04 | 2.33 | 465 |
| 2024-09-20 22:21:35.936 | MS1 | 121.4656775230 | 31.1446362197 | 862 | 504990 | -87.52 | 14.03 | 57.73 | 0.13 | 2.46 | 448 |
| 2024-09-20 22:21:36.940 | MS1 | 121.4656585662 | 31.1446347547 | 862 | 504990 | -86.54 | 12.86 | 107.41 | 0.09 | 2.52 | 495 |
| 2024-09-20 22:21:37.824 | MS1 | 121.4656702992 | 31.1446308241 | 862 | 504990 | -89.25 | 12.94 | 74.84 | 0.15 | 2.44 | 367 |
| 2024-09-20 22:21:38.645 | MS1 | 121.4656584693 | 31.1446206063 | 862 | 504990 | -93.75 | 10.46 | 62.71 | 0.02 | 2.15 | 357 |
| 2024-09-20 22:21:39.467 | MS1 | 121.4656681978 | 31.1446306379 | 862 | 504990 | -92.16 | 7.28 | 79.66 | 0.10 | 2.33 | 372 |
| 2024-09-20 22:21:40.785 | MS1 | 121.4656670008 | 31.1446185409 | 862 | 504990 | -91.91 | 7.34 | 401.50 | 0.15 | 2.53 | 1589 |
| 2024-09-20 22:21:41.403 | MS1 | 121.4656598848 | 31.1446266224 | 862 | 504990 | -90.97 | 12.89 | 570.75 | 0.19 | 2.46 | 1595 |
| 2024-09-20 22:21:42.688 | MS1 | 121.4656581599 | 31.1446301035 | 862 | 504990 | -91.50 | 7.85 | 551.38 | 0.18 | 2.97 | 1566 |

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
| 3217433 | 1 | 121.4683732770 | 31.1541253378 | 122 | 14 | 3 | 20.4 | TDD | 16 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3247079 | 3 | 121.4676953700 | 31.1538676620 | 126 | 7 | 10 | 31.8 | TDD | 862 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3249097 | 4 | 121.4714544408 | 31.1454170758 | 206 | 3 | 8 | 18.8 | TDD | 935 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3278132 | 2 | 121.4673831688 | 31.1477589280 | 65 | 0 | 1 | 29.7 | TDD | 293 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |

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
| 2024-09-20 22:21:31.603 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.620 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.742 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.742 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.422 | NREventA3 | measId:2;ServCellPCI:947;Se... |
| 2024-09-20 22:21:38.662 | NRHandoverAttempt | SourcePCI:947;SourceNR-ARFC... |
| 2024-09-20 22:21:38.696 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.706 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.818 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.818 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3217433 | 1 | 17.0197 | 11.8007 | -116.8782 | 10.4386 | 146.2753 | 0.0021 | 0.0013 |
| 2024_09_20 22:00 | 3278132 | 2 | 5.3611 | 18.5141 | -114.7441 | 13.5150 | 131.4758 | 0.0009 | 0.0196 |
| 2024_09_20 22:00 | 3247079 | 3 | 10.3396 | 18.4149 | -115.7347 | 8.3133 | 105.8820 | 0.0147 | 0.0049 |
| 2024_09_20 22:00 | 3249097 | 4 | 12.9000 | 14.4282 | -114.9827 | 11.8094 | 134.5074 | 0.0051 | 0.0069 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414116_7C83E0BD | 504990 | 862 | -88.0 | 504990 | 293 | -91.3 | 504990 | 935 | -102.1 | 504990 | 16 |
| MR_1774414116_28B4F0C3 | 504990 | 862 | -90.1 | 504990 | 293 | -94.0 | 504990 | 935 | -101.3 | 504990 | 16 |
| MR_1774414116_55F5681B | 504990 | 862 | -87.0 | 504990 | 293 | -92.3 | 504990 | 935 | -100.1 | 504990 | 16 |
| MR_1774414116_DFDF00A5 | 504990 | 862 | -88.2 | 504990 | 293 | -93.1 | 504990 | 935 | -99.7 | 504990 | 16 |
| MR_1774414116_7843C2EB | 504990 | 862 | -88.1 | 504990 | 293 | -91.6 | 504990 | 935 | -99.0 | 504990 | 16 |
| MR_1774414116_8BF16B07 | 504990 | 862 | -87.7 | 504990 | 293 | -90.8 | 504990 | 935 | -99.9 | 504990 | 16 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 355: `794d2dec-0dc...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `794d2dec-0dce-43a3-8946-01f15a9fbace` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[355] topology](images/test_0355.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3235092_4
- `C2`: Lift the tilt angle  of 3248201_2 by 10 degrees
- `C3`: Insufficient data; more data is needed for judgment.
- `C4`: Add neighbor relationship between 3217705_1 and 3248201_2
- `C5`: Increase transmission power for 3248201_2
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3248201_2
- `C7`: Press down the tilt angle of 3235092_4 by 10 degrees
- `C8`: Adjust the azimuth of 3248201_2 by 50 degrees
- `C9`: Decrease A3 Offset threshold for 3235092_4
- `C10`: Decrease transmission power for 3235092_4
- `C11`: Check test server and transmission issues
- `C12`: Press down the tilt angle  of 3248201_2 by 10 degrees
- `C13`: Increase transmission power for 3235092_4
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3248201_2
- `C15`: Increase A3 Offset threshold for 3248201_2
- `C16`: Decrease transmission power for 3248201_2
- `C17`: Decrease A3 Offset threshold for 3248201_2
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3235092_4
- `C19`: Add neighbor relationship between 3235092_4 and 3248201_2
- `C20`: Lift the tilt angle of 3235092_4 by 10 degrees
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3235092_4
- `C22`: Adjust the azimuth of 3235092_4 by 1 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.174 | MS1 | 121.4656647626 | 31.1446376947 | 654 | 504990 | -87.72 | 14.36 | 539.41 | 0.06 | 2.10 | 1571 |
| 2024-09-20 22:21:32.274 | MS1 | 121.4656763063 | 31.1446321966 | 654 | 504990 | -86.47 | 16.30 | 342.55 | 0.02 | 2.90 | 1577 |
| 2024-09-20 22:21:33.143 | MS1 | 121.4656693634 | 31.1446313940 | 654 | 504990 | -90.07 | 17.39 | 533.46 | 0.17 | 2.40 | 1579 |
| 2024-09-20 22:21:34.676 | MS1 | 121.4656623763 | 31.1446294830 | 654 | 504990 | -91.82 | 14.64 | 57.14 | 0.10 | 2.47 | 1578 |
| 2024-09-20 22:21:35.423 | MS1 | 121.4656649893 | 31.1446237924 | 654 | 504990 | -91.57 | 14.12 | 68.17 | 0.06 | 2.36 | 1579 |
| 2024-09-20 22:21:36.808 | MS1 | 121.4656632779 | 31.1446315111 | 654 | 504990 | -87.75 | 12.09 | 87.80 | 0.13 | 2.70 | 1567 |
| 2024-09-20 22:21:37.743 | MS1 | 121.4656720408 | 31.1446294572 | 654 | 504990 | -92.98 | 9.25 | 59.30 | 0.06 | 2.64 | 1582 |
| 2024-09-20 22:21:38.863 | MS1 | 121.4656712211 | 31.1446290549 | 654 | 504990 | -93.15 | 10.97 | 71.59 | 0.10 | 2.71 | 1590 |
| 2024-09-20 22:21:39.835 | MS1 | 121.4656590443 | 31.1446204962 | 654 | 504990 | -93.42 | 9.60 | 80.10 | 0.03 | 2.36 | 1596 |
| 2024-09-20 22:21:40.839 | MS1 | 121.4656623785 | 31.1446294041 | 654 | 504990 | -91.24 | 9.40 | 505.34 | 0.10 | 2.38 | 1584 |
| 2024-09-20 22:21:41.223 | MS1 | 121.4656660287 | 31.1446341383 | 654 | 504990 | -90.21 | 11.90 | 496.88 | 0.17 | 2.37 | 1586 |
| 2024-09-20 22:21:42.564 | MS1 | 121.4656641838 | 31.1446247687 | 654 | 504990 | -90.39 | 8.17 | 399.12 | 0.12 | 2.06 | 1596 |

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
| 3217705 | 1 | 121.4740886008 | 31.1441853825 | 160 | 1 | 10 | 20.2 | TDD | 104 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3225587 | 3 | 121.4756632064 | 31.1444714275 | 95 | 7 | 9 | 19.0 | TDD | 739 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3235092 | 4 | 121.4674075851 | 31.1488047536 | 199 | 11 | 3 | 32.2 | TDD | 654 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3248201 | 2 | 121.4729739463 | 31.1488863294 | 2 | 15 | 2 | 35.5 | TDD | 482 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:31.506 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.613 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.613 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.331 | NREventA3 | measId:2;ServCellPCI:762;Se... |
| 2024-09-20 22:21:38.571 | NRHandoverAttempt | SourcePCI:762;SourceNR-ARFC... |
| 2024-09-20 22:21:38.601 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.612 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.732 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.732 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3217705 | 1 | 80.2654 | 83.8704 | -116.3360 | 10.2353 | 190.2694 | 0.0130 | 0.0116 |
| 2024_09_19 22:00 | 3248201 | 2 | 92.9829 | 79.4010 | -117.5343 | 11.8921 | 97.8371 | 0.0172 | 0.0082 |
| 2024_09_19 22:00 | 3225587 | 3 | 86.7885 | 84.5968 | -116.4727 | 17.7283 | 176.2028 | 0.0071 | 0.0051 |
| 2024_09_19 22:00 | 3235092 | 4 | 91.2272 | 81.5902 | -114.2078 | 6.8129 | 192.3989 | 0.0005 | 0.0200 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412041_5082F9D3 | 504990 | 654 | -93.3 | 504990 | 482 | -93.5 | 504990 | 104 | -97.7 | 504990 | 739 |
| MR_1774412041_7776ABB4 | 504990 | 654 | -90.2 | 504990 | 482 | -94.3 | 504990 | 104 | -100.0 | 504990 | 739 |
| MR_1774412041_B70945E1 | 504990 | 654 | -91.5 | 504990 | 482 | -93.7 | 504990 | 104 | -100.0 | 504990 | 739 |
| MR_1774412041_C751A7A8 | 504990 | 654 | -90.5 | 504990 | 482 | -94.9 | 504990 | 104 | -97.8 | 504990 | 739 |
| MR_1774412041_2298CFA2 | 504990 | 654 | -92.2 | 504990 | 482 | -92.2 | 504990 | 104 | -100.2 | 504990 | 739 |
| MR_1774412041_50ED93FB | 504990 | 654 | -90.1 | 504990 | 482 | -92.4 | 504990 | 104 | -99.2 | 504990 | 739 |
| MR_1774412041_316FDE05 | 504990 | 654 | -92.4 | 504990 | 482 | -95.0 | 504990 | 104 | -100.2 | 504990 | 739 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 356: `e109a460-d8b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `e109a460-d8b1-43cd-bdd1-e20c29267564` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[356] topology](images/test_0356.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3224694_4
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3224694_4
- `C3`: Lift the tilt angle of 3267614_1 by 10 degrees
- `C4`: Decrease transmission power for 3224694_4
- `C5`: Adjust the azimuth of 3224694_4 by 26 degrees
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3267614_1
- `C7`: Press down the tilt angle of 3267614_1 by 10 degrees
- `C8`: Press down the tilt angle  of 3224694_4 by 10 degrees
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3267614_1
- `C10`: Increase transmission power for 3224694_4
- `C11`: Insufficient data; more data is needed for judgment.
- `C12`: Decrease A3 Offset threshold for 3267614_1
- `C13`: Add neighbor relationship between 3267614_1 and 3224694_4
- `C14`: Increase A3 Offset threshold for 3267614_1
- `C15`: Decrease transmission power for 3267614_1
- `C16`: Increase transmission power for 3267614_1
- `C17`: Check test server and transmission issues
- `C18`: Adjust the azimuth of 3267614_1 by 50 degrees
- `C19`: Add neighbor relationship between 3263788_2 and 3224694_4
- `C20`: Decrease A3 Offset threshold for 3224694_4
- `C21`: Lift the tilt angle  of 3224694_4 by 10 degrees
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3224694_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.799 | MS1 | 121.4656587090 | 31.1446368722 | 353 | 504990 | -84.11 | 17.60 | 501.27 | 0.12 | 2.12 | 1587 |
| 2024-09-20 22:21:32.195 | MS1 | 121.4656689938 | 31.1446278958 | 353 | 504990 | -79.45 | 12.96 | 450.26 | 0.13 | 2.45 | 1586 |
| 2024-09-20 22:21:33.517 | MS1 | 121.4656593623 | 31.1446232572 | 353 | 504990 | -79.26 | 15.64 | 568.93 | 0.01 | 2.17 | 1599 |
| 2024-09-20 22:21:34.182 | MS1 | 121.4656635515 | 31.1446274160 | 353 | 504990 | -89.82 | -2.30 | 43.19 | 0.12 | 1.27 | 1580 |
| 2024-09-20 22:21:35.824 | MS1 | 121.4656612423 | 31.1446211272 | 353 | 504990 | -83.93 | -1.12 | 49.59 | 0.06 | 1.14 | 1570 |
| 2024-09-20 22:21:36.876 | MS1 | 121.4656634058 | 31.1446335656 | 353 | 504990 | -88.10 | -3.50 | 68.61 | 0.11 | 1.26 | 1593 |
| 2024-09-20 22:21:37.504 | MS1 | 121.4656719553 | 31.1446371938 | 353 | 504990 | -89.57 | -3.26 | 25.29 | 0.05 | 1.01 | 1571 |
| 2024-09-20 22:21:38.490 | MS1 | 121.4656643995 | 31.1446361128 | 353 | 504990 | -92.51 | -3.08 | 64.06 | 0.02 | 1.28 | 1576 |
| 2024-09-20 22:21:39.159 | MS1 | 121.4656627142 | 31.1446210734 | 446 | 504990 | -79.05 | 13.12 | 213.94 | 0.06 | 1.10 | 1571 |
| 2024-09-20 22:21:40.682 | MS1 | 121.4656612734 | 31.1446258712 | 446 | 504990 | -76.45 | 16.66 | 343.60 | 0.15 | 2.98 | 1562 |
| 2024-09-20 22:21:41.801 | MS1 | 121.4656587978 | 31.1446318930 | 446 | 504990 | -82.85 | 15.68 | 562.39 | 0.02 | 2.07 | 1593 |
| 2024-09-20 22:21:42.912 | MS1 | 121.4656665498 | 31.1446190740 | 446 | 504990 | -84.05 | 15.27 | 446.75 | 0.19 | 2.36 | 1595 |

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
| 3224694 | 4 | 121.4695169610 | 31.1452933884 | 285 | 9 | 7 | 20.0 | TDD | 446 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3242875 | 3 | 121.4749670469 | 31.1476903089 | 263 | 13 | 6 | 35.2 | TDD | 572 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3263788 | 2 | 121.4687524052 | 31.1446927187 | 28 | 5 | 4 | 31.8 | TDD | 425 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3267614 | 1 | 121.4759633943 | 31.1546995765 | 25 | 9 | 11 | 27.4 | TDD | 353 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |

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
| 2024-09-20 22:21:30.831 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.852 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:30.952 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.952 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.704 | NREventA3 | measId:2;ServCellPCI:137;Se... |
| 2024-09-20 22:21:37.944 | NRHandoverAttempt | SourcePCI:137;SourceNR-ARFC... |
| 2024-09-20 22:21:37.978 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.989 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.110 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.110 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3267614 | 1 | 14.1712 | 10.7178 | -116.5216 | 15.1897 | 190.4548 | 0.0123 | 0.1898 |
| 2024_09_20 22:00 | 3263788 | 2 | 15.2298 | 13.7389 | -114.7656 | 18.2294 | 104.8033 | 0.0190 | 0.0022 |
| 2024_09_20 22:00 | 3242875 | 3 | 14.7807 | 14.8491 | -116.9651 | 7.2455 | 164.8928 | 0.0105 | 0.0031 |
| 2024_09_20 22:00 | 3224694 | 4 | 17.6451 | 9.3943 | -114.5024 | 14.7705 | 94.6296 | 0.0009 | 0.0065 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413621_B5C02730 | 504990 | 446 | -86.2 | 504990 | 353 | -88.5 | 504990 | 425 | -84.2 | 504990 | 572 |
| MR_1774413621_760F7650 | 504990 | 446 | -86.8 | 504990 | 353 | -87.9 | 504990 | 425 | -84.9 | 504990 | 572 |
| MR_1774413621_D323DE59 | 504990 | 353 | -88.4 | 504990 | 446 | -84.7 | 504990 | 425 | -86.4 | 504990 | 572 |
| MR_1774413621_FC524A90 | 504990 | 353 | -91.5 | 504990 | 446 | -86.5 | 504990 | 425 | -85.9 | 504990 | 572 |
| MR_1774413621_1E6186D1 | 504990 | 446 | -86.2 | 504990 | 353 | -90.6 | 504990 | 425 | -84.2 | 504990 | 572 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 357: `bc9fb314-bfb...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `bc9fb314-bfbc-4199-8e62-71fec2d90ee0` |
| Tag | **multiple-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[357] topology](images/test_0357.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 5 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 5개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3245882_3
- `C2`: Check test server and transmission issues
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3239799_1
- `C4`: Decrease A3 Offset threshold for 3239799_1
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3239799_1
- `C6`: Decrease A3 Offset threshold for 3245882_3
- `C7`: Add neighbor relationship between 3263784_4 and 3245882_3
- `C8`: Adjust the azimuth of 3239799_1 by 16 degrees
- `C9`: Increase A3 Offset threshold for 3245882_3
- `C10`: Insufficient data; more data is needed for judgment.
- `C11`: Increase transmission power for 3245882_3
- `C12`: Increase transmission power for 3239799_1
- `C13`: Lift the tilt angle  of 3245882_3 by 3 degrees
- `C14`: Decrease transmission power for 3245882_3
- `C15`: Adjust the azimuth of 3245882_3 by 47 degrees
- `C16`: Add neighbor relationship between 3239799_1 and 3245882_3
- `C17`: Decrease transmission power for 3239799_1
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3245882_3
- `C19`: Press down the tilt angle  of 3245882_3 by 3 degrees
- `C20`: Lift the tilt angle of 3239799_1 by 3 degrees
- `C21`: Increase A3 Offset threshold for 3239799_1
- `C22`: Press down the tilt angle of 3239799_1 by 3 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.939 | MS1 | 121.4656583469 | 31.1446260371 | 391 | 504990 | -77.93 | 14.17 | 419.30 | 0.15 | 2.63 | 1560 |
| 2024-09-20 22:21:32.688 | MS1 | 121.4656650066 | 31.1446191554 | 391 | 504990 | -76.93 | 15.01 | 581.85 | 0.10 | 2.05 | 1600 |
| 2024-09-20 22:21:33.597 | MS1 | 121.4656701183 | 31.1446195402 | 391 | 504990 | -80.96 | 17.11 | 534.72 | 0.11 | 2.35 | 1592 |
| 2024-09-20 22:21:34.587 | MS1 | 121.4656675115 | 31.1446347101 | 381 | 504990 | -89.39 | 4.90 | 46.15 | 0.19 | 1.33 | 1597 |
| 2024-09-20 22:21:35.160 | MS1 | 121.4656684237 | 31.1446185758 | 381 | 504990 | -85.10 | 3.23 | 41.63 | 0.09 | 1.29 | 1568 |
| 2024-09-20 22:21:36.977 | MS1 | 121.4656595808 | 31.1446348054 | 391 | 504990 | -82.57 | 4.44 | 59.91 | 0.19 | 1.11 | 1563 |
| 2024-09-20 22:21:37.466 | MS1 | 121.4656607418 | 31.1446234036 | 391 | 504990 | -80.94 | 4.59 | 37.71 | 0.12 | 1.22 | 1570 |
| 2024-09-20 22:21:38.957 | MS1 | 121.4656651513 | 31.1446285661 | 381 | 504990 | -87.35 | 1.02 | 29.54 | 0.03 | 1.23 | 1564 |
| 2024-09-20 22:21:39.850 | MS1 | 121.4656735261 | 31.1446270708 | 381 | 504990 | -84.55 | 2.88 | 64.08 | 0.19 | 1.45 | 1566 |
| 2024-09-20 22:21:40.280 | MS1 | 121.4656597021 | 31.1446271486 | 381 | 504990 | -80.65 | 12.76 | 529.82 | 0.13 | 2.36 | 1592 |
| 2024-09-20 22:21:41.236 | MS1 | 121.4656598980 | 31.1446305922 | 381 | 504990 | -79.37 | 15.13 | 560.22 | 0.16 | 2.67 | 1586 |
| 2024-09-20 22:21:42.141 | MS1 | 121.4656697350 | 31.1446355002 | 381 | 504990 | -78.52 | 14.25 | 404.77 | 0.06 | 2.40 | 1576 |

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
| 3218638 | 5 | 121.4641337318 | 31.1553883776 | 309 | 7 | 1 | 28.7 | TDD | 381 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3239799 | 1 | 121.4692068231 | 31.1446977552 | 253 | 0 | 11 | 17.1 | TDD | 391 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3245882 | 3 | 121.4731702688 | 31.1515883200 | 270 | 2 | 6 | 18.1 | TDD | 374 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3263784 | 4 | 121.4753073233 | 31.1442188368 | 262 | 8 | 5 | 33.7 | TDD | 923 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3266953 | 2 | 121.4708498875 | 31.1533428471 | 274 | 11 | 12 | 28.9 | TDD | 43 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:31.126 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.145 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.248 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.248 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:33.993 | NREventA3 | measId:2;ServCellPCI:119;Se... |
| 2024-09-20 22:21:34.233 | NRHandoverAttempt | SourcePCI:119;SourceNR-ARFC... |
| 2024-09-20 22:21:34.270 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:34.283 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:34.396 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:34.396 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.993 | NREventA3 | measId:2;ServCellPCI:43;Ser... |
| 2024-09-20 22:21:36.233 | NRHandoverAttempt | SourcePCI:43;SourceNR-ARFCN... |
| 2024-09-20 22:21:36.266 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:36.280 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:36.399 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.399 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.993 | NREventA3 | measId:2;ServCellPCI:119;Se... |
| 2024-09-20 22:21:38.233 | NRHandoverAttempt | SourcePCI:119;SourceNR-ARFC... |
| 2024-09-20 22:21:38.271 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.286 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.422 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.422 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3239799 | 1 | 9.9788 | 14.0266 | -115.4156 | 18.9916 | 155.7581 | 0.0161 | 0.0060 |
| 2024_09_20 22:00 | 3266953 | 2 | 19.7496 | 14.9218 | -117.0942 | 9.9484 | 187.2780 | 0.0057 | 0.0135 |
| 2024_09_20 22:00 | 3245882 | 3 | 16.0998 | 11.9468 | -114.2197 | 9.9342 | 180.9396 | 0.0178 | 0.0166 |
| 2024_09_20 22:00 | 3263784 | 4 | 9.1670 | 12.2166 | -115.1752 | 11.4400 | 155.7691 | 0.0097 | 0.0010 |
| 2024_09_20 22:00 | 3218638 | 5 | 8.5018 | 18.2508 | -117.6965 | 5.7802 | 92.0711 | 0.0102 | 0.0117 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414251_A4C12E3A | 504990 | 381 | -91.3 | 504990 | 391 | -86.6 | 504990 | 374 | -90.8 | 504990 | 923 |
| MR_1774414251_5E02F78F | 504990 | 381 | -89.6 | 504990 | 391 | -90.2 | 504990 | 374 | -88.4 | 504990 | 923 |
| MR_1774414251_783BD9AE | 504990 | 381 | -87.8 | 504990 | 391 | -90.0 | 504990 | 374 | -91.2 | 504990 | 923 |
| MR_1774414251_4339BE60 | 504990 | 381 | -88.6 | 504990 | 391 | -87.2 | 504990 | 374 | -89.7 | 504990 | 923 |
| MR_1774414251_376A308E | 504990 | 381 | -89.9 | 504990 | 391 | -88.9 | 504990 | 374 | -89.0 | 504990 | 923 |
| MR_1774414251_F30C04C9 | 504990 | 391 | -88.3 | 504990 | 381 | -87.1 | 504990 | 374 | -89.8 | 504990 | 923 |
| MR_1774414251_4F34B1EF | 504990 | 381 | -88.0 | 504990 | 391 | -88.5 | 504990 | 374 | -91.2 | 504990 | 923 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 358: `9a762276-78d...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `9a762276-78d6-44d4-9730-5f12234556cf` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[358] topology](images/test_0358.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3230564_3 by 10 degrees
- `C2`: Adjust the azimuth of 3264243_2 by 11 degrees
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3230564_3
- `C4`: Press down the tilt angle of 3230564_3 by 10 degrees
- `C5`: Add neighbor relationship between 3252651_1 and 3264243_2
- `C6`: Press down the tilt angle  of 3264243_2 by 4 degrees
- `C7`: Decrease transmission power for 3230564_3
- `C8`: Increase transmission power for 3264243_2
- `C9`: Check test server and transmission issues
- `C10`: Increase A3 Offset threshold for 3230564_3
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3264243_2
- `C12`: Decrease A3 Offset threshold for 3264243_2
- `C13`: Decrease A3 Offset threshold for 3230564_3
- `C14`: Decrease transmission power for 3264243_2
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3264243_2
- `C16`: Lift the tilt angle  of 3264243_2 by 4 degrees
- `C17`: Increase transmission power for 3230564_3
- `C18`: Add neighbor relationship between 3230564_3 and 3264243_2
- `C19`: Increase A3 Offset threshold for 3264243_2
- `C20`: Insufficient data; more data is needed for judgment.
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3230564_3
- `C22`: Adjust the azimuth of 3230564_3 by 50 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.638 | MS1 | 121.4656585932 | 31.1446199493 | 693 | 504990 | -76.30 | 17.85 | 409.66 | 0.01 | 2.04 | 1591 |
| 2024-09-20 22:21:32.184 | MS1 | 121.4656749102 | 31.1446185700 | 693 | 504990 | -83.39 | 17.53 | 454.11 | 0.14 | 2.01 | 1589 |
| 2024-09-20 22:21:33.824 | MS1 | 121.4656636557 | 31.1446210846 | 693 | 504990 | -76.23 | 13.04 | 568.97 | 0.05 | 2.13 | 1570 |
| 2024-09-20 22:21:34.230 | MS1 | 121.4656647664 | 31.1446337904 | 693 | 504990 | -90.85 | -3.77 | 28.81 | 0.12 | 1.44 | 1590 |
| 2024-09-20 22:21:35.323 | MS1 | 121.4656715013 | 31.1446281982 | 693 | 504990 | -89.95 | -3.24 | 63.30 | 0.08 | 1.23 | 1585 |
| 2024-09-20 22:21:36.592 | MS1 | 121.4656636087 | 31.1446318814 | 693 | 504990 | -93.63 | -2.82 | 68.76 | 0.10 | 1.24 | 1573 |
| 2024-09-20 22:21:37.290 | MS1 | 121.4656754290 | 31.1446322037 | 693 | 504990 | -94.11 | -3.82 | 37.61 | 0.16 | 1.24 | 1590 |
| 2024-09-20 22:21:38.939 | MS1 | 121.4656672028 | 31.1446222848 | 693 | 504990 | -83.73 | 17.70 | 375.32 | 0.02 | 1.25 | 1582 |
| 2024-09-20 22:21:39.842 | MS1 | 121.4656618485 | 31.1446202745 | 693 | 504990 | -78.24 | 14.85 | 573.81 | 0.01 | 1.21 | 1585 |
| 2024-09-20 22:21:40.504 | MS1 | 121.4656580532 | 31.1446192404 | 693 | 504990 | -84.45 | 14.47 | 367.57 | 0.15 | 2.54 | 1586 |
| 2024-09-20 22:21:41.198 | MS1 | 121.4656766887 | 31.1446283275 | 693 | 504990 | -82.50 | 13.12 | 304.74 | 0.02 | 2.17 | 1597 |
| 2024-09-20 22:21:42.136 | MS1 | 121.4656743124 | 31.1446195039 | 693 | 504990 | -84.71 | 16.56 | 377.36 | 0.07 | 2.11 | 1580 |

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
| 3222280 | 4 | 121.4674954553 | 31.1505590308 | 121 | 7 | 10 | 49.3 | TDD | 622 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3230564 | 3 | 121.4682271325 | 31.1541623497 | 125 | 13 | 4 | 20.0 | TDD | 693 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3252651 | 1 | 121.4657290159 | 31.1542204705 | 244 | 7 | 8 | 37.0 | TDD | 248 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3264243 | 2 | 121.4724950328 | 31.1533524179 | 225 | 3 | 11 | 29.3 | TDD | 604 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:31.566 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.588 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.734 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.734 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.392 | NREventA3 | measId:2;ServCellPCI:625;Se... |
| 2024-09-20 22:21:36.392 | NREventA3 | measId:2;ServCellPCI:625;Se... |
| 2024-09-20 22:21:37.392 | NREventA3 | measId:2;ServCellPCI:625;Se... |
| 2024-09-20 22:21:39.892 | NRRRCReestablishAttempt | PCI:625 |
| 2024-09-20 22:21:39.911 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.923 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:40.054 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:40.054 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3252651 | 1 | 16.8278 | 15.1630 | -114.6391 | 15.4690 | 98.6788 | 0.0147 | 0.0025 |
| 2024_09_20 22:00 | 3264243 | 2 | 5.6040 | 8.9316 | -115.4407 | 13.0236 | 99.3164 | 0.0007 | 0.0092 |
| 2024_09_20 22:00 | 3230564 | 3 | 19.2919 | 18.7572 | -114.4329 | 11.9973 | 196.1981 | 0.0081 | 0.1033 |
| 2024_09_20 22:00 | 3222280 | 4 | 6.9602 | 5.1251 | -114.6825 | 6.0700 | 120.3066 | 0.0121 | 0.0042 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413228_340BEC6D | 504990 | 693 | -89.1 | 504990 | 604 | -88.1 | 504990 | 248 | -90.6 | 504990 | 622 |
| MR_1774413228_3E525F0D | 504990 | 693 | -89.5 | 504990 | 604 | -84.6 | 504990 | 248 | -93.0 | 504990 | 622 |
| MR_1774413228_1CCDD488 | 504990 | 693 | -91.3 | 504990 | 604 | -87.4 | 504990 | 248 | -90.3 | 504990 | 622 |
| MR_1774413228_0E35B8CC | 504990 | 693 | -91.6 | 504990 | 604 | -86.0 | 504990 | 248 | -93.1 | 504990 | 622 |
| MR_1774413228_00C37D30 | 504990 | 604 | -87.3 | 504990 | 693 | -91.3 | 504990 | 248 | -92.6 | 504990 | 622 |
| MR_1774413228_40B1DEAB | 504990 | 693 | -91.6 | 504990 | 604 | -86.1 | 504990 | 248 | -90.2 | 504990 | 622 |
| MR_1774413228_A92DB3BA | 504990 | 693 | -89.3 | 504990 | 604 | -85.8 | 504990 | 248 | -90.2 | 504990 | 622 |
| MR_1774413228_2EDA0A94 | 504990 | 693 | -91.6 | 504990 | 604 | -87.7 | 504990 | 248 | -89.3 | 504990 | 622 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 359: `2de48943-77b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `2de48943-77ba-40ab-9626-b9ae783730f1` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[359] topology](images/test_0359.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3251236_2 by 4 degrees
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3251236_2
- `C3`: Increase A3 Offset threshold for 3251236_2
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3274569_4
- `C5`: Press down the tilt angle  of 3274569_4 by 10 degrees
- `C6`: Insufficient data; more data is needed for judgment.
- `C7`: Add neighbor relationship between 3219473_1 and 3274569_4
- `C8`: Press down the tilt angle of 3251236_2 by 4 degrees
- `C9`: Increase transmission power for 3251236_2
- `C10`: Decrease A3 Offset threshold for 3251236_2
- `C11`: Adjust the azimuth of 3251236_2 by 50 degrees
- `C12`: Add neighbor relationship between 3251236_2 and 3274569_4
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3251236_2
- `C14`: Decrease transmission power for 3251236_2
- `C15`: Check test server and transmission issues
- `C16`: Decrease transmission power for 3274569_4
- `C17`: Increase transmission power for 3274569_4
- `C18`: Increase A3 Offset threshold for 3274569_4
- `C19`: Decrease A3 Offset threshold for 3274569_4
- `C20`: Lift the tilt angle  of 3274569_4 by 10 degrees
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3274569_4
- `C22`: Adjust the azimuth of 3274569_4 by 50 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.834 | MS1 | 121.4656602070 | 31.1446330216 | 828 | 504990 | -90.85 | 14.07 | 485.52 | 0.15 | 2.54 | 1591 |
| 2024-09-20 22:21:32.567 | MS1 | 121.4656725457 | 31.1446193489 | 828 | 504990 | -90.68 | 12.65 | 401.87 | 0.15 | 2.75 | 1571 |
| 2024-09-20 22:21:33.342 | MS1 | 121.4656616491 | 31.1446205683 | 828 | 504990 | -86.10 | 16.27 | 331.83 | 0.10 | 2.70 | 1590 |
| 2024-09-20 22:21:34.672 | MS1 | 121.4656594808 | 31.1446210394 | 828 | 504990 | -88.29 | 15.39 | 65.71 | 0.06 | 2.69 | 389 |
| 2024-09-20 22:21:35.327 | MS1 | 121.4656641389 | 31.1446279656 | 828 | 504990 | -90.54 | 16.35 | 61.14 | 0.01 | 2.66 | 414 |
| 2024-09-20 22:21:36.188 | MS1 | 121.4656693204 | 31.1446200653 | 828 | 504990 | -87.91 | 16.87 | 81.01 | 0.03 | 2.33 | 319 |
| 2024-09-20 22:21:37.125 | MS1 | 121.4656718493 | 31.1446245411 | 828 | 504990 | -92.85 | 8.31 | 56.36 | 0.06 | 2.45 | 329 |
| 2024-09-20 22:21:38.298 | MS1 | 121.4656686902 | 31.1446273275 | 828 | 504990 | -93.41 | 7.42 | 42.54 | 0.11 | 2.07 | 446 |
| 2024-09-20 22:21:39.116 | MS1 | 121.4656616043 | 31.1446238586 | 828 | 504990 | -91.29 | 7.30 | 56.40 | 0.17 | 2.87 | 416 |
| 2024-09-20 22:21:40.323 | MS1 | 121.4656761663 | 31.1446294992 | 828 | 504990 | -91.02 | 7.44 | 362.72 | 0.05 | 2.54 | 1575 |
| 2024-09-20 22:21:41.688 | MS1 | 121.4656687876 | 31.1446360113 | 828 | 504990 | -91.48 | 11.25 | 415.39 | 0.13 | 2.66 | 1574 |
| 2024-09-20 22:21:42.971 | MS1 | 121.4656682046 | 31.1446266920 | 828 | 504990 | -90.55 | 11.41 | 593.19 | 0.14 | 2.47 | 1587 |

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
| 3212430 | 3 | 121.4664952179 | 31.1510521128 | 222 | 8 | 9 | 42.1 | TDD | 765 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3219473 | 1 | 121.4678353948 | 31.1519136827 | 237 | 11 | 1 | 35.8 | TDD | 736 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3251236 | 2 | 121.4752333676 | 31.1458348454 | 343 | 2 | 0 | 31.6 | TDD | 828 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3274569 | 4 | 121.4733233554 | 31.1484778909 | 351 | 10 | 4 | 33.1 | TDD | 909 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |

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
| 2024-09-20 22:21:31.487 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.511 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.623 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.623 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.325 | NREventA3 | measId:2;ServCellPCI:754;Se... |
| 2024-09-20 22:21:38.565 | NRHandoverAttempt | SourcePCI:754;SourceNR-ARFC... |
| 2024-09-20 22:21:38.595 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.606 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.748 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.748 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3219473 | 1 | 13.1249 | 19.9112 | -115.6866 | 18.6133 | 132.7149 | 0.0008 | 0.0158 |
| 2024_09_20 22:00 | 3251236 | 2 | 8.9690 | 19.0405 | -115.7208 | 15.6621 | 95.2504 | 0.0060 | 0.0119 |
| 2024_09_20 22:00 | 3212430 | 3 | 6.1132 | 11.8989 | -116.3237 | 16.8639 | 126.0273 | 0.0180 | 0.0110 |
| 2024_09_20 22:00 | 3274569 | 4 | 17.1504 | 17.2069 | -115.9855 | 9.5246 | 111.8223 | 0.0033 | 0.0166 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414650_D93DA8AE | 504990 | 828 | -88.1 | 504990 | 909 | -96.9 | 504990 | 736 | -100.3 | 504990 | 765 |
| MR_1774414650_4224FAA1 | 504990 | 828 | -89.0 | 504990 | 909 | -98.6 | 504990 | 736 | -97.4 | 504990 | 765 |
| MR_1774414650_9C1ADA02 | 504990 | 828 | -89.7 | 504990 | 909 | -95.9 | 504990 | 736 | -101.1 | 504990 | 765 |
| MR_1774414650_F5ED7A11 | 504990 | 828 | -87.7 | 504990 | 909 | -97.7 | 504990 | 736 | -100.4 | 504990 | 765 |
| MR_1774414650_82C28875 | 504990 | 828 | -88.4 | 504990 | 909 | -97.8 | 504990 | 736 | -100.8 | 504990 | 765 |

> *... 2개 열 생략 (전체 14열)*

---
