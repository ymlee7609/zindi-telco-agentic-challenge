# Track A 문제 분석 — train[1220]~train[1229]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[1220] ~ train[1229] (10개)

## 목차

1. [문제 1220: `6f55d9ee-cf6...`](#1220) — multiple-answer, 정답: C7|C22
2. [문제 1221: `4c02386c-3ab...`](#1221) — single-answer, 정답: C21
3. [문제 1222: `df1443d0-ac2...`](#1222) — multiple-answer, 정답: C12|C13|C16|C22
4. [문제 1223: `9bc40673-b1b...`](#1223) — single-answer, 정답: C16
5. [문제 1224: `a53c5680-5da...`](#1224) — single-answer, 정답: C17
6. [문제 1225: `ac56ed6f-d1b...`](#1225) — single-answer, 정답: C8
7. [문제 1226: `36f3fc01-ba0...`](#1226) — single-answer, 정답: C21
8. [문제 1227: `33f2cc7f-79f...`](#1227) — multiple-answer, 정답: C11|C12|C14|C18
9. [문제 1228: `511f8a40-d25...`](#1228) — single-answer, 정답: C19
10. [문제 1229: `0e512699-46a...`](#1229) — single-answer, 정답: C2

---

### 문제 1220: `6f55d9ee-cf6...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `6f55d9ee-cf65-4b4e-b376-41d676161199` |
| Tag | **multiple-answer** |
| 정답 | **C7|C22** |
| C7 의미 | Press down the tilt angle  of 3277603_4 by 2 degrees |
| C22 의미 | Decrease transmission power for 3277603_4 |
| 패턴 분류 | **P3 Overshoot (tilt)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1220] topology](images/train_1220.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3277725_2 and 3277603_4
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3210642_1
- `C3`: Lift the tilt angle of 3210642_1 by 5 degrees
- `C4`: Increase A3 Offset threshold for 3210642_1
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3277603_4
- `C6`: Decrease transmission power for 3210642_1
- `C7`: Press down the tilt angle  of 3277603_4 by 2 degrees **← 정답**
- `C8`: Adjust the azimuth of 3210642_1 by 10 degrees
- `C9`: Decrease A3 Offset threshold for 3277603_4
- `C10`: Check test server and transmission issues
- `C11`: Adjust the azimuth of 3277603_4 by 5 degrees
- `C12`: Decrease A3 Offset threshold for 3210642_1
- `C13`: Press down the tilt angle of 3210642_1 by 5 degrees
- `C14`: Increase transmission power for 3277603_4
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3210642_1
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3277603_4
- `C17`: Lift the tilt angle  of 3277603_4 by 2 degrees
- `C18`: Add neighbor relationship between 3210642_1 and 3277603_4
- `C19`: Insufficient data; more data is needed for judgment.
- `C20`: Increase transmission power for 3210642_1
- `C21`: Increase A3 Offset threshold for 3277603_4
- `C22`: Decrease transmission power for 3277603_4 **← 정답**

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.574 | MS1 | 121.4656769455 | 31.1446187420 | 681 | 504990 | -77.80 | 17.85 | 366.65 | 0.13 | 2.91 | 1588 |
| 2024-09-20 22:21:32.110 | MS1 | 121.4656649354 | 31.1446195649 | 681 | 504990 | -76.55 | 16.03 | 461.92 | 0.16 | 2.06 | 1568 |
| 2024-09-20 22:21:33.748 | MS1 | 121.4656716867 | 31.1446274087 | 681 | 504990 | -78.21 | 16.80 | 346.72 | 0.02 | 2.46 | 1566 |
| 2024-09-20 22:21:34.525 | MS1 | 121.4656590614 | 31.1446266375 | 681 | 504990 | -91.94 | 3.70 | 58.59 | 0.18 | 1.46 | 1578 |
| 2024-09-20 22:21:35.666 | MS1 | 121.4656663464 | 31.1446362201 | 681 | 504990 | -86.96 | 1.39 | 68.32 | 0.12 | 1.12 | 1578 |
| 2024-09-20 22:21:36.576 | MS1 | 121.4656647259 | 31.1446225670 | 681 | 504990 | -86.09 | 0.59 | 92.79 | 0.15 | 1.12 | 1564 |
| 2024-09-20 22:21:37.564 | MS1 | 121.4656673480 | 31.1446216200 | 681 | 504990 | -93.41 | 2.07 | 60.61 | 0.19 | 1.46 | 1571 |
| 2024-09-20 22:21:38.146 | MS1 | 121.4656751239 | 31.1446205647 | 681 | 504990 | -88.06 | 0.47 | 64.46 | 0.15 | 1.14 | 1585 |
| 2024-09-20 22:21:39.821 | MS1 | 121.4656707449 | 31.1446282522 | 681 | 504990 | -92.99 | 0.07 | 64.47 | 0.01 | 1.47 | 1593 |
| 2024-09-20 22:21:40.590 | MS1 | 121.4656703581 | 31.1446298550 | 681 | 504990 | -77.61 | 15.51 | 484.93 | 0.11 | 2.11 | 1561 |
| 2024-09-20 22:21:41.854 | MS1 | 121.4656761308 | 31.1446282193 | 681 | 504990 | -81.80 | 13.70 | 462.79 | 0.15 | 2.37 | 1597 |
| 2024-09-20 22:21:42.313 | MS1 | 121.4656770619 | 31.1446329638 | 681 | 504990 | -79.65 | 15.52 | 353.05 | 0.08 | 2.56 | 1569 |

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
| 3210642 | 1 | 121.4716412074 | 31.1478355883 | 228 | 3 | 9 | 18.4 | TDD | 681 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3226220 | 3 | 121.4740817821 | 31.1524972052 | 162 | 1 | 6 | 15.4 | TDD | 859 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3277603 | 4 | 121.4750677852 | 31.1510252170 | 227 | 1 | 4 | 23.8 | TDD | 791 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3277725 | 2 | 121.4752147841 | 31.1465223368 | 105 | 5 | 3 | 34.5 | TDD | 409 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |

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
| 2024-09-20 22:21:31.468 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.493 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.597 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.597 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3210642 | 1 | 5.2612 | 12.1204 | -109.1173 | 11.5964 | 188.7857 | 0.0136 | 0.0072 |
| 2024_09_20 22:00 | 3277725 | 2 | 11.2652 | 19.4703 | -116.3575 | 17.0889 | 84.4336 | 0.0188 | 0.0012 |
| 2024_09_20 22:00 | 3226220 | 3 | 16.6831 | 17.8899 | -114.6600 | 10.2570 | 190.5282 | 0.0080 | 0.0165 |
| 2024_09_20 22:00 | 3277603 | 4 | 16.0262 | 11.7486 | -116.3030 | 18.1763 | 135.9920 | 0.0085 | 0.0007 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412908_78BFC0C4 | 504990 | 791 | -92.3 | 504990 | 681 | -89.4 | 504990 | 409 | -93.4 | 504990 | 859 |
| MR_1774412908_BE4356CF | 504990 | 681 | -90.9 | 504990 | 791 | -89.1 | 504990 | 409 | -93.5 | 504990 | 859 |
| MR_1774412908_B3E57EFD | 504990 | 791 | -92.2 | 504990 | 681 | -86.7 | 504990 | 409 | -91.6 | 504990 | 859 |
| MR_1774412908_E47AED22 | 504990 | 791 | -92.1 | 504990 | 681 | -86.3 | 504990 | 409 | -93.1 | 504990 | 859 |
| MR_1774412908_D79882A6 | 504990 | 791 | -90.0 | 504990 | 681 | -86.3 | 504990 | 409 | -91.3 | 504990 | 859 |
| MR_1774412908_66F09959 | 504990 | 791 | -93.8 | 504990 | 681 | -88.0 | 504990 | 409 | -92.6 | 504990 | 859 |
| MR_1774412908_8C940163 | 504990 | 681 | -91.3 | 504990 | 791 | -90.0 | 504990 | 409 | -94.0 | 504990 | 859 |
| MR_1774412908_8CECD341 | 504990 | 681 | -91.4 | 504990 | 791 | -89.5 | 504990 | 409 | -91.4 | 504990 | 859 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1221: `4c02386c-3ab...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `4c02386c-3abe-4557-81c5-11f7f825e87d` |
| Tag | **single-answer** |
| 정답 | **C21** |
| C21 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1221] topology](images/train_1221.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle  of 3260600_3 by 5 degrees
- `C2`: Add neighbor relationship between 3265998_1 and 3260600_3
- `C3`: Increase transmission power for 3265998_1
- `C4`: Press down the tilt angle  of 3260600_3 by 5 degrees
- `C5`: Check test server and transmission issues
- `C6`: Decrease transmission power for 3265998_1
- `C7`: Increase transmission power for 3260600_3
- `C8`: Decrease A3 Offset threshold for 3260600_3
- `C9`: Increase A3 Offset threshold for 3260600_3
- `C10`: Increase A3 Offset threshold for 3265998_1
- `C11`: Lift the tilt angle of 3265998_1 by 10 degrees
- `C12`: Decrease transmission power for 3260600_3
- `C13`: Decrease A3 Offset threshold for 3265998_1
- `C14`: Press down the tilt angle of 3265998_1 by 10 degrees
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3265998_1
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3260600_3
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3260600_3
- `C18`: Add neighbor relationship between 3273465_2 and 3260600_3
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3265998_1
- `C20`: Adjust the azimuth of 3260600_3 by 50 degrees
- `C21`: Insufficient data; more data is needed for judgment. **← 정답**
- `C22`: Adjust the azimuth of 3265998_1 by 3 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.695 | MS1 | 121.4656750534 | 31.1446245266 | 728 | 504990 | -89.36 | 12.08 | 548.04 | 0.04 | 2.89 | 1578 |
| 2024-09-20 22:21:32.563 | MS1 | 121.4656695401 | 31.1446195337 | 728 | 504990 | -89.53 | 12.08 | 387.40 | 0.15 | 2.18 | 1577 |
| 2024-09-20 22:21:33.552 | MS1 | 121.4656675229 | 31.1446280838 | 728 | 504990 | -90.26 | 15.79 | 392.43 | 0.14 | 2.88 | 1575 |
| 2024-09-20 22:21:34.149 | MS1 | 121.4656652246 | 31.1446182441 | 728 | 504990 | -85.87 | 16.40 | 78.61 | 0.04 | 2.31 | 1596 |
| 2024-09-20 22:21:35.447 | MS1 | 121.4656640198 | 31.1446371097 | 728 | 504990 | -88.56 | 14.87 | 55.36 | 0.20 | 2.53 | 1563 |
| 2024-09-20 22:21:36.670 | MS1 | 121.4656690044 | 31.1446336520 | 728 | 504990 | -85.07 | 13.18 | 89.03 | 0.01 | 2.66 | 1576 |
| 2024-09-20 22:21:37.997 | MS1 | 121.4656771964 | 31.1446194631 | 728 | 504990 | -93.58 | 10.08 | 79.31 | 0.07 | 2.45 | 1568 |
| 2024-09-20 22:21:38.687 | MS1 | 121.4656657743 | 31.1446213813 | 728 | 504990 | -90.52 | 11.66 | 62.07 | 0.17 | 2.60 | 1595 |
| 2024-09-20 22:21:39.515 | MS1 | 121.4656775402 | 31.1446319033 | 728 | 504990 | -89.02 | 9.52 | 72.45 | 0.10 | 2.52 | 1594 |
| 2024-09-20 22:21:40.471 | MS1 | 121.4656588526 | 31.1446331452 | 728 | 504990 | -89.19 | 12.86 | 392.39 | 0.18 | 2.07 | 1597 |
| 2024-09-20 22:21:41.490 | MS1 | 121.4656663677 | 31.1446347160 | 728 | 504990 | -89.41 | 12.12 | 317.12 | 0.00 | 2.17 | 1586 |
| 2024-09-20 22:21:42.303 | MS1 | 121.4656595399 | 31.1446219291 | 728 | 504990 | -93.83 | 12.19 | 496.48 | 0.19 | 2.27 | 1598 |

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
| 3260600 | 3 | 121.4678000641 | 31.1477742728 | 273 | 2 | 11 | 21.7 | TDD | 48 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3265998 | 1 | 121.4720804655 | 31.1535072478 | 215 | 14 | 5 | 32.9 | TDD | 728 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3273465 | 2 | 121.4640592581 | 31.1517943991 | 195 | 14 | 6 | 22.6 | TDD | 57 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3278423 | 4 | 121.4723840053 | 31.1558740752 | 296 | 3 | 7 | 43.7 | TDD | 912 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |

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
| 2024-09-20 22:21:31.524 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.650 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.650 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.399 | NREventA3 | measId:2;ServCellPCI:160;Se... |
| 2024-09-20 22:21:38.639 | NRHandoverAttempt | SourcePCI:160;SourceNR-ARFC... |
| 2024-09-20 22:21:38.670 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.680 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.812 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.812 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3265998 | 1 | 89.4584 | 78.6769 | -117.8081 | 13.4583 | 103.8968 | 0.0029 | 0.0025 |
| 2024_09_19 22:00 | 3273465 | 2 | 84.7969 | 85.3875 | -116.6952 | 8.6797 | 150.4970 | 0.0186 | 0.0065 |
| 2024_09_19 22:00 | 3260600 | 3 | 92.1106 | 92.7020 | -115.9664 | 13.0507 | 191.3266 | 0.0167 | 0.0116 |
| 2024_09_19 22:00 | 3278423 | 4 | 93.9690 | 81.0116 | -115.3356 | 14.2899 | 195.6596 | 0.0159 | 0.0155 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415092_0D1DEEB4 | 504990 | 728 | -85.7 | 504990 | 48 | -87.4 | 504990 | 57 | -95.2 | 504990 | 912 |
| MR_1774415092_D67CE55B | 504990 | 728 | -87.7 | 504990 | 48 | -87.1 | 504990 | 57 | -97.1 | 504990 | 912 |
| MR_1774415092_F9885357 | 504990 | 728 | -87.6 | 504990 | 48 | -84.7 | 504990 | 57 | -94.9 | 504990 | 912 |
| MR_1774415092_6F37A7B3 | 504990 | 728 | -85.9 | 504990 | 48 | -87.1 | 504990 | 57 | -94.6 | 504990 | 912 |
| MR_1774415092_24A3D871 | 504990 | 728 | -86.6 | 504990 | 48 | -85.8 | 504990 | 57 | -97.4 | 504990 | 912 |
| MR_1774415092_284DD7A0 | 504990 | 728 | -87.5 | 504990 | 48 | -87.1 | 504990 | 57 | -95.2 | 504990 | 912 |
| MR_1774415092_8814A26F | 504990 | 728 | -87.2 | 504990 | 48 | -85.2 | 504990 | 57 | -94.8 | 504990 | 912 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1222: `df1443d0-ac2...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `df1443d0-ac2c-4a34-8dac-2778025b9865` |
| Tag | **multiple-answer** |
| 정답 | **C12|C13|C16|C22** |
| C12 의미 | Increase A3 Offset threshold for 3275887_4 |
| C13 의미 | Decrease transmission power for 3275887_4 |
| C16 의미 | Increase A3 Offset threshold for 3249101_5 |
| C22 의미 | Press down the tilt angle  of 3275887_4 by 2 degrees |
| 패턴 분류 | **P2 Ping-pong** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1222] topology](images/train_1222.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 5 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 5개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3275887_4
- `C2`: Check test server and transmission issues
- `C3`: Decrease A3 Offset threshold for 3249101_5
- `C4`: Decrease transmission power for 3249101_5
- `C5`: Decrease A3 Offset threshold for 3275887_4
- `C6`: Add neighbor relationship between 3249101_5 and 3275887_4
- `C7`: Adjust the azimuth of 3249101_5 by 40 degrees
- `C8`: Adjust the azimuth of 3275887_4 by 37 degrees
- `C9`: Lift the tilt angle  of 3275887_4 by 2 degrees
- `C10`: Add neighbor relationship between 3254643_1 and 3275887_4
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3249101_5
- `C12`: Increase A3 Offset threshold for 3275887_4 **← 정답**
- `C13`: Decrease transmission power for 3275887_4 **← 정답**
- `C14`: Lift the tilt angle of 3249101_5 by 4 degrees
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3249101_5
- `C16`: Increase A3 Offset threshold for 3249101_5 **← 정답**
- `C17`: Insufficient data; more data is needed for judgment.
- `C18`: Increase transmission power for 3249101_5
- `C19`: Increase transmission power for 3275887_4
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3275887_4
- `C21`: Press down the tilt angle of 3249101_5 by 4 degrees
- `C22`: Press down the tilt angle  of 3275887_4 by 2 degrees **← 정답**

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.128 | MS1 | 121.4656606469 | 31.1446364067 | 62 | 504990 | -81.61 | 14.00 | 456.74 | 0.08 | 2.72 | 1600 |
| 2024-09-20 22:21:32.708 | MS1 | 121.4656641785 | 31.1446374548 | 62 | 504990 | -75.18 | 13.80 | 582.80 | 0.05 | 2.36 | 1573 |
| 2024-09-20 22:21:33.317 | MS1 | 121.4656739301 | 31.1446236868 | 62 | 504990 | -83.81 | 14.90 | 548.65 | 0.11 | 2.10 | 1584 |
| 2024-09-20 22:21:34.772 | MS1 | 121.4656610850 | 31.1446371124 | 725 | 504990 | -83.54 | 2.64 | 78.78 | 0.06 | 1.11 | 1584 |
| 2024-09-20 22:21:35.105 | MS1 | 121.4656744769 | 31.1446277902 | 725 | 504990 | -83.46 | 3.48 | 52.84 | 0.05 | 1.17 | 1582 |
| 2024-09-20 22:21:36.833 | MS1 | 121.4656587024 | 31.1446185490 | 62 | 504990 | -80.20 | 3.76 | 80.06 | 0.03 | 1.39 | 1600 |
| 2024-09-20 22:21:37.973 | MS1 | 121.4656741875 | 31.1446313342 | 62 | 504990 | -86.10 | 4.21 | 81.91 | 0.07 | 1.34 | 1569 |
| 2024-09-20 22:21:38.341 | MS1 | 121.4656617155 | 31.1446246911 | 725 | 504990 | -85.52 | 2.05 | 79.39 | 0.12 | 1.48 | 1576 |
| 2024-09-20 22:21:39.181 | MS1 | 121.4656747923 | 31.1446258843 | 725 | 504990 | -88.54 | 4.69 | 66.25 | 0.13 | 1.44 | 1600 |
| 2024-09-20 22:21:40.700 | MS1 | 121.4656681911 | 31.1446322714 | 725 | 504990 | -75.87 | 13.87 | 570.41 | 0.05 | 2.26 | 1567 |
| 2024-09-20 22:21:41.501 | MS1 | 121.4656665259 | 31.1446199449 | 725 | 504990 | -77.25 | 17.77 | 362.38 | 0.04 | 2.39 | 1571 |
| 2024-09-20 22:21:42.381 | MS1 | 121.4656655499 | 31.1446231837 | 725 | 504990 | -84.80 | 17.92 | 465.34 | 0.16 | 2.23 | 1597 |

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
| 3234814 | 2 | 121.4655196885 | 31.1475641431 | 105 | 2 | 10 | 25.3 | TDD | 683 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3249101 | 5 | 121.4719814725 | 31.1464772546 | 291 | 0 | 6 | 42.4 | TDD | 62 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3254643 | 1 | 121.4725801791 | 31.1556412118 | 158 | 14 | 9 | 43.1 | TDD | 641 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3266236 | 3 | 121.4695887887 | 31.1455955601 | 119 | 15 | 0 | 29.7 | TDD | 725 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3275887 | 4 | 121.4708197724 | 31.1556083687 | 165 | 0 | 12 | 45.7 | TDD | 29 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |

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
| 2024-09-20 22:21:31.156 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.271 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.271 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.036 | NREventA3 | measId:2;ServCellPCI:333;Se... |
| 2024-09-20 22:21:34.276 | NRHandoverAttempt | SourcePCI:333;SourceNR-ARFC... |
| 2024-09-20 22:21:34.321 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:34.331 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:34.452 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:34.452 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:36.036 | NREventA3 | measId:2;ServCellPCI:840;Se... |
| 2024-09-20 22:21:36.276 | NRHandoverAttempt | SourcePCI:840;SourceNR-ARFC... |
| 2024-09-20 22:21:36.314 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:36.329 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:36.445 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.445 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.036 | NREventA3 | measId:2;ServCellPCI:333;Se... |
| 2024-09-20 22:21:38.276 | NRHandoverAttempt | SourcePCI:333;SourceNR-ARFC... |
| 2024-09-20 22:21:38.319 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.334 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.434 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.434 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3254643 | 1 | 10.2004 | 17.8472 | -117.3770 | 5.9518 | 187.5463 | 0.0023 | 0.0110 |
| 2024_09_20 22:00 | 3234814 | 2 | 13.5843 | 5.5015 | -114.7726 | 13.8543 | 110.2991 | 0.0181 | 0.0113 |
| 2024_09_20 22:00 | 3266236 | 3 | 5.7886 | 8.8517 | -116.1049 | 14.3297 | 103.1048 | 0.0041 | 0.0122 |
| 2024_09_20 22:00 | 3275887 | 4 | 10.1356 | 12.0715 | -117.7435 | 18.0645 | 194.4926 | 0.0094 | 0.0098 |
| 2024_09_20 22:00 | 3249101 | 5 | 17.1853 | 14.4387 | -117.1894 | 12.5474 | 122.2417 | 0.0109 | 0.0047 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415942_B614FED9 | 504990 | 725 | -83.1 | 504990 | 62 | -82.6 | 504990 | 29 | -84.5 | 504990 | 641 |
| MR_1774415942_7C74F2F1 | 504990 | 62 | -82.5 | 504990 | 725 | -82.6 | 504990 | 29 | -86.5 | 504990 | 641 |
| MR_1774415942_313A326A | 504990 | 62 | -82.0 | 504990 | 725 | -85.1 | 504990 | 29 | -83.5 | 504990 | 641 |
| MR_1774415942_74341EA1 | 504990 | 725 | -85.4 | 504990 | 62 | -83.0 | 504990 | 29 | -85.9 | 504990 | 641 |
| MR_1774415942_C4D1AFD9 | 504990 | 62 | -83.5 | 504990 | 725 | -82.9 | 504990 | 29 | -84.3 | 504990 | 641 |
| MR_1774415942_2974171D | 504990 | 62 | -81.7 | 504990 | 725 | -82.6 | 504990 | 29 | -85.6 | 504990 | 641 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1223: `9bc40673-b1b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `9bc40673-b1be-406b-8e7e-913f3ade24e1` |
| Tag | **single-answer** |
| 정답 | **C16** |
| C16 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1223] topology](images/train_1223.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3246871_3 by 50 degrees
- `C2`: Lift the tilt angle of 3277518_4 by 10 degrees
- `C3`: Increase A3 Offset threshold for 3277518_4
- `C4`: Adjust the azimuth of 3277518_4 by 50 degrees
- `C5`: Add neighbor relationship between 3277518_4 and 3246871_3
- `C6`: Add neighbor relationship between 3227010_2 and 3246871_3
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3246871_3
- `C8`: Insufficient data; more data is needed for judgment.
- `C9`: Increase A3 Offset threshold for 3246871_3
- `C10`: Increase transmission power for 3246871_3
- `C11`: Press down the tilt angle of 3277518_4 by 10 degrees
- `C12`: Decrease transmission power for 3246871_3
- `C13`: Decrease A3 Offset threshold for 3246871_3
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3277518_4
- `C15`: Decrease A3 Offset threshold for 3277518_4
- `C16`: Check test server and transmission issues **← 정답**
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3246871_3
- `C18`: Decrease transmission power for 3277518_4
- `C19`: Lift the tilt angle  of 3246871_3 by 10 degrees
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3277518_4
- `C21`: Increase transmission power for 3277518_4
- `C22`: Press down the tilt angle  of 3246871_3 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.690 | MS1 | 121.4656618215 | 31.1446284406 | 566 | 504990 | -87.43 | 14.98 | 342.29 | 0.06 | 2.00 | 1566 |
| 2024-09-20 22:21:32.169 | MS1 | 121.4656659641 | 31.1446340464 | 566 | 504990 | -89.27 | 14.77 | 302.37 | 0.08 | 2.84 | 1598 |
| 2024-09-20 22:21:33.619 | MS1 | 121.4656653833 | 31.1446370180 | 566 | 504990 | -88.55 | 15.05 | 487.72 | 0.11 | 2.42 | 1590 |
| 2024-09-20 22:21:34.655 | MS1 | 121.4656747585 | 31.1446206990 | 566 | 504990 | -85.99 | 13.29 | 85.03 | 0.13 | 2.09 | 356 |
| 2024-09-20 22:21:35.880 | MS1 | 121.4656594381 | 31.1446259990 | 566 | 504990 | -89.66 | 14.88 | 78.53 | 0.15 | 2.11 | 422 |
| 2024-09-20 22:21:36.811 | MS1 | 121.4656684144 | 31.1446232738 | 566 | 504990 | -86.53 | 14.33 | 83.40 | 0.14 | 2.25 | 387 |
| 2024-09-20 22:21:37.913 | MS1 | 121.4656724044 | 31.1446358885 | 566 | 504990 | -90.04 | 9.25 | 81.02 | 0.05 | 2.87 | 419 |
| 2024-09-20 22:21:38.215 | MS1 | 121.4656762241 | 31.1446189230 | 566 | 504990 | -90.20 | 9.39 | 46.25 | 0.09 | 2.74 | 499 |
| 2024-09-20 22:21:39.714 | MS1 | 121.4656632689 | 31.1446350875 | 566 | 504990 | -89.26 | 12.57 | 92.33 | 0.02 | 2.68 | 328 |
| 2024-09-20 22:21:40.997 | MS1 | 121.4656591216 | 31.1446231234 | 566 | 504990 | -90.79 | 11.29 | 391.82 | 0.19 | 2.65 | 1582 |
| 2024-09-20 22:21:41.203 | MS1 | 121.4656585773 | 31.1446294386 | 566 | 504990 | -92.47 | 10.66 | 469.53 | 0.05 | 2.40 | 1577 |
| 2024-09-20 22:21:42.257 | MS1 | 121.4656663467 | 31.1446313446 | 566 | 504990 | -93.10 | 12.48 | 529.95 | 0.07 | 2.45 | 1596 |

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
| 3227010 | 2 | 121.4673672852 | 31.1553526093 | 72 | 12 | 8 | 33.7 | TDD | 498 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3246871 | 3 | 121.4735328521 | 31.1509129462 | 138 | 12 | 0 | 28.0 | TDD | 957 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3247518 | 1 | 121.4755261161 | 31.1510229139 | 69 | 14 | 0 | 20.3 | TDD | 930 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3277518 | 4 | 121.4693887134 | 31.1457411772 | 100 | 10 | 3 | 38.6 | TDD | 566 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:31.377 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.402 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.524 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.524 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.247 | NREventA3 | measId:2;ServCellPCI:890;Se... |
| 2024-09-20 22:21:38.487 | NRHandoverAttempt | SourcePCI:890;SourceNR-ARFC... |
| 2024-09-20 22:21:38.519 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.531 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.677 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.677 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3247518 | 1 | 12.6068 | 10.1310 | -115.5616 | 7.6097 | 108.6303 | 0.0181 | 0.0178 |
| 2024_09_20 22:00 | 3227010 | 2 | 7.5611 | 7.7721 | -116.0104 | 8.4373 | 195.2991 | 0.0059 | 0.0150 |
| 2024_09_20 22:00 | 3246871 | 3 | 6.2350 | 15.8943 | -115.9061 | 17.2515 | 158.5167 | 0.0005 | 0.0056 |
| 2024_09_20 22:00 | 3277518 | 4 | 7.9697 | 12.6693 | -117.9985 | 14.1896 | 98.8432 | 0.0132 | 0.0058 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414485_8484F92D | 504990 | 566 | -86.1 | 504990 | 957 | -89.8 | 504990 | 498 | -101.7 | 504990 | 930 |
| MR_1774414485_3CC2069C | 504990 | 566 | -84.2 | 504990 | 957 | -91.8 | 504990 | 498 | -101.4 | 504990 | 930 |
| MR_1774414485_505E2DC3 | 504990 | 566 | -86.1 | 504990 | 957 | -90.1 | 504990 | 498 | -99.0 | 504990 | 930 |
| MR_1774414485_00861C05 | 504990 | 566 | -86.5 | 504990 | 957 | -90.5 | 504990 | 498 | -101.6 | 504990 | 930 |
| MR_1774414485_4BC2A845 | 504990 | 566 | -84.4 | 504990 | 957 | -90.0 | 504990 | 498 | -99.9 | 504990 | 930 |
| MR_1774414485_C406A315 | 504990 | 566 | -85.5 | 504990 | 957 | -90.1 | 504990 | 498 | -100.8 | 504990 | 930 |
| MR_1774414485_F9B5D207 | 504990 | 566 | -85.9 | 504990 | 957 | -91.1 | 504990 | 498 | -100.4 | 504990 | 930 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1224: `a53c5680-5da...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `a53c5680-5da2-4efc-b9b1-56ba4d1dfe4b` |
| Tag | **single-answer** |
| 정답 | **C17** |
| C17 의미 | Add neighbor relationship between 3220764_2 and 3264161_3 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1224] topology](images/train_1224.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3264161_3 by 5 degrees
- `C2`: Decrease transmission power for 3264161_3
- `C3`: Lift the tilt angle of 3220764_2 by 4 degrees
- `C4`: Check test server and transmission issues
- `C5`: Insufficient data; more data is needed for judgment.
- `C6`: Increase transmission power for 3220764_2
- `C7`: Lift the tilt angle  of 3264161_3 by 5 degrees
- `C8`: Decrease transmission power for 3220764_2
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3220764_2
- `C10`: Decrease A3 Offset threshold for 3220764_2
- `C11`: Decrease A3 Offset threshold for 3264161_3
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3264161_3
- `C13`: Press down the tilt angle of 3220764_2 by 4 degrees
- `C14`: Increase transmission power for 3264161_3
- `C15`: Increase A3 Offset threshold for 3220764_2
- `C16`: Increase A3 Offset threshold for 3264161_3
- `C17`: Add neighbor relationship between 3220764_2 and 3264161_3 **← 정답**
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3264161_3
- `C19`: Adjust the azimuth of 3264161_3 by 37 degrees
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3220764_2
- `C21`: Adjust the azimuth of 3220764_2 by 50 degrees
- `C22`: Add neighbor relationship between 3250032_4 and 3264161_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.936 | MS1 | 121.4656778432 | 31.1446337315 | 20 | 504990 | -82.10 | 15.35 | 346.66 | 0.07 | 2.86 | 1576 |
| 2024-09-20 22:21:32.715 | MS1 | 121.4656609938 | 31.1446213923 | 20 | 504990 | -83.10 | 17.66 | 391.65 | 0.12 | 2.96 | 1563 |
| 2024-09-20 22:21:33.570 | MS1 | 121.4656764654 | 31.1446228405 | 20 | 504990 | -79.12 | 17.54 | 401.34 | 0.18 | 2.02 | 1583 |
| 2024-09-20 22:21:34.329 | MS1 | 121.4656604379 | 31.1446352481 | 20 | 504990 | -89.16 | -3.67 | 48.93 | 0.18 | 1.21 | 1572 |
| 2024-09-20 22:21:35.777 | MS1 | 121.4656749830 | 31.1446244026 | 20 | 504990 | -88.90 | -3.30 | 65.05 | 0.08 | 1.07 | 1593 |
| 2024-09-20 22:21:36.712 | MS1 | 121.4656701875 | 31.1446258424 | 20 | 504990 | -90.70 | -3.13 | 41.23 | 0.20 | 1.34 | 1569 |
| 2024-09-20 22:21:37.400 | MS1 | 121.4656599250 | 31.1446321107 | 20 | 504990 | -85.33 | -3.50 | 78.85 | 0.05 | 1.17 | 1581 |
| 2024-09-20 22:21:38.876 | MS1 | 121.4656659251 | 31.1446222291 | 20 | 504990 | -82.56 | 17.29 | 298.33 | 0.10 | 1.02 | 1578 |
| 2024-09-20 22:21:39.561 | MS1 | 121.4656611699 | 31.1446183402 | 20 | 504990 | -84.48 | 13.03 | 525.22 | 0.09 | 1.01 | 1596 |
| 2024-09-20 22:21:40.736 | MS1 | 121.4656665368 | 31.1446212515 | 20 | 504990 | -78.21 | 13.85 | 380.62 | 0.18 | 2.68 | 1575 |
| 2024-09-20 22:21:41.444 | MS1 | 121.4656628834 | 31.1446250421 | 20 | 504990 | -81.07 | 13.49 | 390.72 | 0.02 | 2.80 | 1595 |
| 2024-09-20 22:21:42.199 | MS1 | 121.4656609078 | 31.1446242796 | 20 | 504990 | -77.53 | 14.81 | 305.32 | 0.07 | 2.29 | 1567 |

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
| 3220764 | 2 | 121.4712413451 | 31.1537022531 | 69 | 2 | 4 | 48.9 | TDD | 20 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3245317 | 1 | 121.4758662003 | 31.1528741895 | 60 | 15 | 12 | 36.8 | TDD | 528 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3250032 | 4 | 121.4734499914 | 31.1540715116 | 16 | 11 | 3 | 37.9 | TDD | 852 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3264161 | 3 | 121.4661966010 | 31.1492442524 | 223 | 0 | 8 | 49.2 | TDD | 261 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |

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
| 2024-09-20 22:21:30.899 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.919 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.022 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.022 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.752 | NREventA3 | measId:2;ServCellPCI:39;Ser... |
| 2024-09-20 22:21:35.752 | NREventA3 | measId:2;ServCellPCI:39;Ser... |
| 2024-09-20 22:21:36.752 | NREventA3 | measId:2;ServCellPCI:39;Ser... |
| 2024-09-20 22:21:39.252 | NRRRCReestablishAttempt | PCI:39 |
| 2024-09-20 22:21:39.272 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.282 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:39.426 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.426 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3245317 | 1 | 9.3482 | 18.0782 | -114.4794 | 11.2968 | 142.8004 | 0.0154 | 0.0133 |
| 2024_09_20 22:00 | 3220764 | 2 | 12.8833 | 6.3626 | -116.6993 | 9.1970 | 175.2734 | 0.0102 | 0.1441 |
| 2024_09_20 22:00 | 3264161 | 3 | 16.5377 | 17.3691 | -115.6918 | 14.5596 | 94.0122 | 0.0135 | 0.0185 |
| 2024_09_20 22:00 | 3250032 | 4 | 8.8608 | 6.2911 | -115.5709 | 5.8051 | 114.2218 | 0.0015 | 0.0101 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412262_B024E17E | 504990 | 261 | -84.5 | 504990 | 20 | -90.2 | 504990 | 852 | -86.1 | 504990 | 528 |
| MR_1774412262_1C196510 | 504990 | 20 | -88.3 | 504990 | 261 | -83.5 | 504990 | 852 | -87.5 | 504990 | 528 |
| MR_1774412262_70749F8C | 504990 | 261 | -83.4 | 504990 | 20 | -89.4 | 504990 | 852 | -88.1 | 504990 | 528 |
| MR_1774412262_E72B095F | 504990 | 20 | -88.2 | 504990 | 261 | -86.1 | 504990 | 852 | -86.5 | 504990 | 528 |
| MR_1774412262_7ACA6B47 | 504990 | 261 | -85.9 | 504990 | 20 | -87.2 | 504990 | 852 | -87.9 | 504990 | 528 |
| MR_1774412262_852E1951 | 504990 | 261 | -84.0 | 504990 | 20 | -89.9 | 504990 | 852 | -88.4 | 504990 | 528 |
| MR_1774412262_A98C2004 | 504990 | 261 | -82.6 | 504990 | 20 | -90.1 | 504990 | 852 | -88.5 | 504990 | 528 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1225: `ac56ed6f-d1b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `ac56ed6f-d1bf-459d-87e3-48f842a6642d` |
| Tag | **single-answer** |
| 정답 | **C8** |
| C8 의미 | Decrease A3 Offset threshold for 3232676_4 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1225] topology](images/train_1225.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Check test server and transmission issues
- `C2`: Increase transmission power for 3232676_4
- `C3`: Increase transmission power for 3276936_1
- `C4`: Add neighbor relationship between 3217515_2 and 3276936_1
- `C5`: Decrease A3 Offset threshold for 3276936_1
- `C6`: Lift the tilt angle  of 3276936_1 by 10 degrees
- `C7`: Adjust the azimuth of 3232676_4 by 50 degrees
- `C8`: Decrease A3 Offset threshold for 3232676_4 **← 정답**
- `C9`: Adjust the azimuth of 3276936_1 by 50 degrees
- `C10`: Press down the tilt angle of 3232676_4 by 9 degrees
- `C11`: Increase A3 Offset threshold for 3232676_4
- `C12`: Add neighbor relationship between 3232676_4 and 3276936_1
- `C13`: Lift the tilt angle of 3232676_4 by 9 degrees
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3232676_4
- `C15`: Decrease transmission power for 3276936_1
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3232676_4
- `C17`: Insufficient data; more data is needed for judgment.
- `C18`: Decrease transmission power for 3232676_4
- `C19`: Increase A3 Offset threshold for 3276936_1
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3276936_1
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3276936_1
- `C22`: Press down the tilt angle  of 3276936_1 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.285 | MS1 | 121.4656736631 | 31.1446264281 | 439 | 504990 | -82.83 | 16.06 | 465.15 | 0.04 | 2.73 | 1560 |
| 2024-09-20 22:21:32.706 | MS1 | 121.4656758018 | 31.1446363284 | 439 | 504990 | -78.32 | 16.62 | 570.06 | 0.03 | 2.71 | 1580 |
| 2024-09-20 22:21:33.134 | MS1 | 121.4656711506 | 31.1446361588 | 439 | 504990 | -77.78 | 16.26 | 405.80 | 0.02 | 2.44 | 1580 |
| 2024-09-20 22:21:34.766 | MS1 | 121.4656740729 | 31.1446308827 | 439 | 504990 | -91.18 | -0.52 | 57.64 | 0.14 | 1.10 | 1588 |
| 2024-09-20 22:21:35.760 | MS1 | 121.4656762242 | 31.1446323183 | 439 | 504990 | -85.76 | -1.58 | 71.89 | 0.16 | 1.29 | 1591 |
| 2024-09-20 22:21:36.320 | MS1 | 121.4656716754 | 31.1446264037 | 439 | 504990 | -83.40 | -2.66 | 39.88 | 0.12 | 1.35 | 1580 |
| 2024-09-20 22:21:37.641 | MS1 | 121.4656709112 | 31.1446317840 | 439 | 504990 | -92.39 | -2.57 | 80.77 | 0.18 | 1.14 | 1587 |
| 2024-09-20 22:21:38.798 | MS1 | 121.4656743134 | 31.1446375412 | 439 | 504990 | -91.18 | -2.37 | 76.29 | 0.04 | 1.46 | 1578 |
| 2024-09-20 22:21:39.278 | MS1 | 121.4656716775 | 31.1446373664 | 730 | 504990 | -81.04 | 17.93 | 176.11 | 0.17 | 1.42 | 1587 |
| 2024-09-20 22:21:40.181 | MS1 | 121.4656742167 | 31.1446210721 | 730 | 504990 | -75.22 | 12.07 | 296.83 | 0.09 | 2.17 | 1594 |
| 2024-09-20 22:21:41.105 | MS1 | 121.4656668414 | 31.1446351029 | 730 | 504990 | -81.75 | 12.23 | 574.41 | 0.07 | 2.06 | 1580 |
| 2024-09-20 22:21:42.893 | MS1 | 121.4656716372 | 31.1446284710 | 730 | 504990 | -80.29 | 15.09 | 346.90 | 0.11 | 2.71 | 1566 |

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
| 3217515 | 2 | 121.4752600634 | 31.1479733331 | 267 | 2 | 3 | 31.4 | TDD | 499 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3232676 | 4 | 121.4689443878 | 31.1455993056 | 132 | 2 | 6 | 42.3 | TDD | 439 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3254585 | 3 | 121.4757844253 | 31.1465088101 | 294 | 11 | 5 | 38.7 | TDD | 852 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3276936 | 1 | 121.4700491276 | 31.1501594724 | 44 | 13 | 1 | 41.5 | TDD | 730 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |

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
| 2024-09-20 22:21:31.407 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.537 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.537 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.205 | NREventA3 | measId:2;ServCellPCI:353;Se... |
| 2024-09-20 22:21:38.445 | NRHandoverAttempt | SourcePCI:353;SourceNR-ARFC... |
| 2024-09-20 22:21:38.479 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.492 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.614 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.614 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3276936 | 1 | 8.5116 | 5.5802 | -116.1295 | 9.7807 | 85.3651 | 0.0041 | 0.0005 |
| 2024_09_20 22:00 | 3217515 | 2 | 16.6654 | 9.1302 | -117.9928 | 9.8702 | 123.9290 | 0.0160 | 0.0080 |
| 2024_09_20 22:00 | 3254585 | 3 | 6.3384 | 12.6864 | -117.8573 | 10.1762 | 178.4798 | 0.0196 | 0.0042 |
| 2024_09_20 22:00 | 3232676 | 4 | 9.1932 | 18.5047 | -114.2384 | 16.8734 | 120.0118 | 0.0018 | 0.1982 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415240_F7D12565 | 504990 | 439 | -91.9 | 504990 | 730 | -84.9 | 504990 | 499 | -89.3 | 504990 | 852 |
| MR_1774415240_053F5D7A | 504990 | 439 | -92.4 | 504990 | 730 | -87.5 | 504990 | 499 | -89.1 | 504990 | 852 |
| MR_1774415240_8C82D831 | 504990 | 439 | -92.0 | 504990 | 730 | -86.8 | 504990 | 499 | -90.6 | 504990 | 852 |
| MR_1774415240_D11AFCE6 | 504990 | 439 | -91.0 | 504990 | 730 | -84.9 | 504990 | 499 | -87.0 | 504990 | 852 |
| MR_1774415240_4E93623A | 504990 | 730 | -87.1 | 504990 | 439 | -89.9 | 504990 | 499 | -89.5 | 504990 | 852 |
| MR_1774415240_74B93DFA | 504990 | 439 | -90.8 | 504990 | 730 | -85.5 | 504990 | 499 | -90.5 | 504990 | 852 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1226: `36f3fc01-ba0...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `36f3fc01-ba06-4300-9487-ccf0b719b8cc` |
| Tag | **single-answer** |
| 정답 | **C21** |
| C21 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3269964_2 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1226] topology](images/train_1226.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3265135_1
- `C2`: Increase A3 Offset threshold for 3269964_2
- `C3`: Press down the tilt angle  of 3265135_1 by 6 degrees
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3265135_1
- `C5`: Add neighbor relationship between 3269964_2 and 3265135_1
- `C6`: Insufficient data; more data is needed for judgment.
- `C7`: Increase transmission power for 3265135_1
- `C8`: Increase transmission power for 3269964_2
- `C9`: Lift the tilt angle of 3269964_2 by 0 degrees
- `C10`: Lift the tilt angle  of 3265135_1 by 6 degrees
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3269964_2
- `C12`: Decrease A3 Offset threshold for 3269964_2
- `C13`: Decrease transmission power for 3265135_1
- `C14`: Check test server and transmission issues
- `C15`: Adjust the azimuth of 3269964_2 by 2 degrees
- `C16`: Increase A3 Offset threshold for 3265135_1
- `C17`: Decrease transmission power for 3269964_2
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3265135_1
- `C19`: Adjust the azimuth of 3265135_1 by 12 degrees
- `C20`: Press down the tilt angle of 3269964_2 by 0 degrees
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3269964_2 **← 정답**
- `C22`: Add neighbor relationship between 3249539_12 and 3265135_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.275 | MS1 | 121.4656634250 | 31.1446350478 | 136 | 504990 | -93.45 | 10.04 | 410.51 | 0.03 | 2.46 | 1582 |
| 2024-09-20 22:21:32.718 | MS1 | 121.4656644113 | 31.1446275691 | 888 | 504990 | -93.71 | 10.82 | 338.63 | 0.07 | 2.59 | 1577 |
| 2024-09-20 22:21:33.355 | MS1 | 121.4656736097 | 31.1446289338 | 747 | 504990 | -95.08 | 13.24 | 590.67 | 0.12 | 2.40 | 1569 |
| 2024-09-20 22:21:34.824 | MS1 | 121.4656730791 | 31.1446191508 | 53 | 152650 | -89.14 | 4.76 | 70.37 | 0.03 | 1.89 | 958 |
| 2024-09-20 22:21:35.213 | MS1 | 121.4656630693 | 31.1446262532 | 220 | 152650 | -89.96 | 5.93 | 62.92 | 0.02 | 1.96 | 915 |
| 2024-09-20 22:21:36.710 | MS1 | 121.4656692857 | 31.1446197298 | 185 | 152650 | -93.44 | 4.90 | 65.22 | 0.20 | 1.90 | 998 |
| 2024-09-20 22:21:37.795 | MS1 | 121.4656728913 | 31.1446317388 | 718 | 152650 | -89.59 | 4.53 | 69.22 | 0.19 | 1.65 | 986 |
| 2024-09-20 22:21:38.795 | MS1 | 121.4656657232 | 31.1446362341 | 53 | 152650 | -87.71 | 2.60 | 48.34 | 0.04 | 1.96 | 962 |
| 2024-09-20 22:21:39.494 | MS1 | 121.4656581653 | 31.1446191949 | 220 | 152650 | -87.78 | 7.02 | 102.11 | 0.16 | 1.98 | 946 |
| 2024-09-20 22:21:40.960 | MS1 | 121.4656706039 | 31.1446336653 | 185 | 152650 | -89.52 | 6.71 | 67.69 | 0.12 | 2.69 | 1570 |
| 2024-09-20 22:21:41.752 | MS1 | 121.4656756114 | 31.1446269851 | 718 | 152650 | -89.16 | 6.00 | 63.08 | 0.03 | 2.45 | 1576 |
| 2024-09-20 22:21:42.242 | MS1 | 121.4656632743 | 31.1446252775 | 53 | 152650 | -96.26 | 4.21 | 83.72 | 0.06 | 2.34 | 1564 |

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
| 3210595 | 3 | 121.4687092803 | 31.1544917959 | 283 | 8 | 1 | 1.8 | TDD | 747 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3215985 | 9 | 121.4742311684 | 31.1547098941 | 249 | 0 | 4 | 15.2 | FDD | 754 | n1 | 152650 | 30M | 4T4R | 27 | 152650 |
| 3227978 | 6 | 121.4673423438 | 31.1484682864 | 56 | 6 | 7 | 26.5 | TDD | 184 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3232491 | 5 | 121.4644619133 | 31.1536482563 | 223 | 2 | 8 | 3.6 | TDD | 888 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3237086 | 4 | 121.4728639307 | 31.1535556563 | 206 | 8 | 9 | 6.1 | TDD | 563 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3245140 | 7 | 121.4640090097 | 31.1464168870 | 119 | 15 | 7 | 0.3 | FDD | 962 | n1 | 152650 | 30M | 4T4R | 14 | 152650 |
| 3245352 | 10 | 121.4673662172 | 31.1552238899 | 33 | 4 | 2 | 15.9 | FDD | 532 | n1 | 152650 | 30M | 4T4R | 10 | 152650 |
| 3249539 | 12 | 121.4651561611 | 31.1444871614 | 331 | 0 | 5 | 23.5 | FDD | 185 | n1 | 152650 | 30M | 4T4R | 23 | 152650 |
| 3251903 | 8 | 121.4733023308 | 31.1496406740 | 356 | 0 | 1 | 10.8 | FDD | 718 | n1 | 152650 | 30M | 4T4R | 19 | 152650 |
| 3252025 | 11 | 121.4687854765 | 31.1520327140 | 59 | 5 | 3 | 7.0 | FDD | 53 | n1 | 152650 | 30M | 4T4R | 27 | 152650 |
| 3265135 | 1 | 121.4710916603 | 31.1515497214 | 202 | 5 | 7 | 8.6 | TDD | 454 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3269964 | 2 | 121.4742642828 | 31.1539891533 | 216 | 0 | 11 | 4.5 | TDD | 136 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3279734 | 13 | 121.4652241308 | 31.1508775012 | 64 | 11 | 6 | 19.0 | FDD | 220 | n1 | 152650 | 30M | 4T4R | 21 | 152650 |

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
| 2024-09-20 22:21:31.053 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.077 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.210 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.210 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.942 | NREventA2 | measId:1;ServCellPCI:515;Se... |
| 2024-09-20 22:21:35.057 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.279 | NREventA5 | measId:3;ServCellPCI:515;Se... |
| 2024-09-20 22:21:35.334 | NRHandoverAttempt | SourcePCI:515;SourceNR-ARFC... |
| 2024-09-20 22:21:35.377 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.391 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:35.528 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.528 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3265135 | 1 | 12.4984 | 18.1074 | -114.8964 | 6.1702 | 96.2217 | 0.0132 | 0.0178 |
| 2024_09_20 22:00 | 3269964 | 2 | 14.5871 | 14.7725 | -115.9149 | 15.2131 | 87.4768 | 0.0186 | 0.0101 |
| 2024_09_20 22:00 | 3210595 | 3 | 10.2157 | 11.0192 | -117.8529 | 9.8018 | 166.4441 | 0.0036 | 0.0135 |
| 2024_09_20 22:00 | 3237086 | 4 | 7.7367 | 15.8683 | -116.5063 | 5.6370 | 121.7594 | 0.0125 | 0.0003 |
| 2024_09_20 22:00 | 3232491 | 5 | 17.6543 | 14.7633 | -117.7272 | 17.0452 | 142.0062 | 0.0152 | 0.0106 |
| 2024_09_20 22:00 | 3227978 | 6 | 5.5503 | 18.1699 | -115.3685 | 18.4473 | 178.3165 | 0.0052 | 0.0103 |
| 2024_09_20 22:00 | 3245140 | 7 | 8.3796 | 14.9171 | -116.8990 | 4.0738 | 58.0437 | 0.0152 | 0.0057 |
| 2024_09_20 22:00 | 3251903 | 8 | 13.8306 | 14.4923 | -114.7721 | 3.2989 | 45.1982 | 0.0041 | 0.0177 |
| 2024_09_20 22:00 | 3215985 | 9 | 10.0004 | 12.9490 | -115.0830 | 3.5727 | 23.2147 | 0.0107 | 0.0169 |
| 2024_09_20 22:00 | 3245352 | 10 | 17.8918 | 17.7119 | -117.5808 | 3.7260 | 50.7426 | 0.0086 | 0.0124 |
| 2024_09_20 22:00 | 3252025 | 11 | 15.5865 | 10.1704 | -115.0193 | 4.3120 | 27.0514 | 0.0158 | 0.0018 |
| 2024_09_20 22:00 | 3249539 | 12 | 10.7724 | 9.9755 | -114.9274 | 3.4979 | 53.2778 | 0.0029 | 0.0041 |
| 2024_09_20 22:00 | 3279734 | 13 | 8.5962 | 15.8202 | -117.7606 | 3.7953 | 50.8050 | 0.0132 | 0.0136 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413126_D5D13036 | 152650 | 53 | -89.2 | 152650 | 962 | -91.4 | 152650 | 532 | -97.3 | 152650 | 754 |
| MR_1774413126_8647A5C7 | 152650 | 53 | -87.6 | 152650 | 962 | -92.8 | 152650 | 532 | -97.9 | 152650 | 754 |
| MR_1774413126_C2AA2301 | 152650 | 53 | -87.8 | 152650 | 962 | -91.7 | 152650 | 532 | -97.1 | 152650 | 754 |
| MR_1774413126_B5F38903 | 152650 | 53 | -89.8 | 152650 | 962 | -94.0 | 152650 | 532 | -97.0 | 152650 | 754 |
| MR_1774413126_80DBD442 | 504990 | 747 | -94.9 | 504990 | 454 | -98.0 | 504990 | 563 | -96.5 | 504990 | 184 |
| MR_1774413126_1D534837 | 152650 | 53 | -88.4 | 152650 | 962 | -92.7 | 152650 | 532 | -98.3 | 152650 | 754 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1227: `33f2cc7f-79f...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `33f2cc7f-79f9-4385-86c7-c6789ee35a93` |
| Tag | **multiple-answer** |
| 정답 | **C11|C12|C14|C18** |
| C11 의미 | Increase A3 Offset threshold for 3271537_2 |
| C12 의미 | Increase A3 Offset threshold for 3234230_3 |
| C14 의미 | Decrease transmission power for 3234230_3 |
| C18 의미 | Press down the tilt angle  of 3234230_3 by 4 degrees |
| 패턴 분류 | **P2 Ping-pong** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1227] topology](images/train_1227.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 5 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 5개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3257723_5 and 3234230_3
- `C2`: Press down the tilt angle of 3271537_2 by 3 degrees
- `C3`: Increase transmission power for 3271537_2
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3234230_3
- `C5`: Insufficient data; more data is needed for judgment.
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3234230_3
- `C7`: Adjust the azimuth of 3271537_2 by 11 degrees
- `C8`: Decrease A3 Offset threshold for 3234230_3
- `C9`: Adjust the azimuth of 3234230_3 by 46 degrees
- `C10`: Lift the tilt angle  of 3234230_3 by 4 degrees
- `C11`: Increase A3 Offset threshold for 3271537_2 **← 정답**
- `C12`: Increase A3 Offset threshold for 3234230_3 **← 정답**
- `C13`: Add neighbor relationship between 3271537_2 and 3234230_3
- `C14`: Decrease transmission power for 3234230_3 **← 정답**
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3271537_2
- `C16`: Decrease A3 Offset threshold for 3271537_2
- `C17`: Lift the tilt angle of 3271537_2 by 3 degrees
- `C18`: Press down the tilt angle  of 3234230_3 by 4 degrees **← 정답**
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3271537_2
- `C20`: Check test server and transmission issues
- `C21`: Increase transmission power for 3234230_3
- `C22`: Decrease transmission power for 3271537_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.273 | MS1 | 121.4656600217 | 31.1446201366 | 473 | 504990 | -82.48 | 13.54 | 550.04 | 0.15 | 2.97 | 1574 |
| 2024-09-20 22:21:32.275 | MS1 | 121.4656676690 | 31.1446350825 | 473 | 504990 | -75.22 | 13.93 | 460.96 | 0.17 | 2.66 | 1571 |
| 2024-09-20 22:21:33.287 | MS1 | 121.4656582480 | 31.1446366837 | 473 | 504990 | -80.67 | 15.34 | 425.18 | 0.07 | 2.93 | 1588 |
| 2024-09-20 22:21:34.201 | MS1 | 121.4656673222 | 31.1446198922 | 123 | 504990 | -83.33 | 2.91 | 68.10 | 0.07 | 1.33 | 1594 |
| 2024-09-20 22:21:35.476 | MS1 | 121.4656765819 | 31.1446376410 | 123 | 504990 | -88.94 | 4.70 | 57.57 | 0.11 | 1.40 | 1565 |
| 2024-09-20 22:21:36.291 | MS1 | 121.4656687490 | 31.1446377230 | 473 | 504990 | -85.90 | 4.27 | 53.23 | 0.14 | 1.22 | 1563 |
| 2024-09-20 22:21:37.144 | MS1 | 121.4656729712 | 31.1446190642 | 473 | 504990 | -85.78 | 3.57 | 41.19 | 0.01 | 1.48 | 1583 |
| 2024-09-20 22:21:38.524 | MS1 | 121.4656716088 | 31.1446299653 | 123 | 504990 | -83.52 | 2.33 | 71.53 | 0.08 | 1.01 | 1595 |
| 2024-09-20 22:21:39.758 | MS1 | 121.4656643044 | 31.1446246512 | 123 | 504990 | -88.46 | 2.40 | 58.23 | 0.11 | 1.37 | 1565 |
| 2024-09-20 22:21:40.513 | MS1 | 121.4656667845 | 31.1446225022 | 123 | 504990 | -80.94 | 13.80 | 465.30 | 0.14 | 2.49 | 1569 |
| 2024-09-20 22:21:41.871 | MS1 | 121.4656695678 | 31.1446256884 | 123 | 504990 | -80.01 | 17.88 | 311.18 | 0.08 | 2.25 | 1569 |
| 2024-09-20 22:21:42.186 | MS1 | 121.4656752996 | 31.1446187186 | 123 | 504990 | -76.78 | 17.38 | 432.90 | 0.14 | 2.88 | 1564 |

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
| 3217367 | 1 | 121.4690794444 | 31.1504401427 | 313 | 9 | 2 | 15.9 | TDD | 68 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3234230 | 3 | 121.4673922903 | 31.1486125171 | 154 | 0 | 1 | 35.9 | TDD | 826 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3248184 | 4 | 121.4650711996 | 31.1511314909 | 223 | 3 | 11 | 28.2 | TDD | 123 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3257723 | 5 | 121.4724011809 | 31.1550176600 | 14 | 2 | 11 | 30.1 | TDD | 829 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3271537 | 2 | 121.4653003579 | 31.1510449808 | 188 | 0 | 3 | 38.9 | TDD | 473 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |

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
| 2024-09-20 22:21:30.987 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.002 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.102 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.102 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:33.832 | NREventA3 | measId:2;ServCellPCI:742;Se... |
| 2024-09-20 22:21:34.072 | NRHandoverAttempt | SourcePCI:742;SourceNR-ARFC... |
| 2024-09-20 22:21:34.115 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:34.128 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:34.273 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:34.273 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.832 | NREventA3 | measId:2;ServCellPCI:88;Ser... |
| 2024-09-20 22:21:36.072 | NRHandoverAttempt | SourcePCI:88;SourceNR-ARFCN... |
| 2024-09-20 22:21:36.111 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:36.122 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:36.239 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.239 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.832 | NREventA3 | measId:2;ServCellPCI:742;Se... |
| 2024-09-20 22:21:38.072 | NRHandoverAttempt | SourcePCI:742;SourceNR-ARFC... |
| 2024-09-20 22:21:38.102 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.116 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.221 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.221 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3217367 | 1 | 18.1088 | 6.2837 | -117.7842 | 5.1672 | 99.3516 | 0.0116 | 0.0077 |
| 2024_09_20 22:00 | 3271537 | 2 | 12.5873 | 9.7924 | -116.1390 | 11.7907 | 96.5604 | 0.0169 | 0.0188 |
| 2024_09_20 22:00 | 3234230 | 3 | 10.3870 | 5.3048 | -114.2398 | 5.2529 | 107.3441 | 0.0156 | 0.0015 |
| 2024_09_20 22:00 | 3248184 | 4 | 11.5441 | 19.4758 | -116.4740 | 6.4465 | 165.4533 | 0.0152 | 0.0005 |
| 2024_09_20 22:00 | 3257723 | 5 | 7.1025 | 15.3258 | -114.0585 | 7.7784 | 177.8191 | 0.0104 | 0.0152 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413258_94CC8516 | 504990 | 123 | -82.6 | 504990 | 473 | -82.6 | 504990 | 826 | -87.4 | 504990 | 829 |
| MR_1774413258_7C53D9EE | 504990 | 123 | -81.7 | 504990 | 473 | -85.8 | 504990 | 826 | -86.9 | 504990 | 829 |
| MR_1774413258_9BEC6224 | 504990 | 123 | -81.5 | 504990 | 473 | -83.1 | 504990 | 826 | -86.4 | 504990 | 829 |
| MR_1774413258_BE720E4E | 504990 | 473 | -84.7 | 504990 | 123 | -84.1 | 504990 | 826 | -84.8 | 504990 | 829 |
| MR_1774413258_A244D603 | 504990 | 473 | -85.3 | 504990 | 123 | -84.6 | 504990 | 826 | -87.7 | 504990 | 829 |
| MR_1774413258_B7F0DC3E | 504990 | 473 | -84.9 | 504990 | 123 | -82.4 | 504990 | 826 | -88.2 | 504990 | 829 |
| MR_1774413258_B976E405 | 504990 | 473 | -84.9 | 504990 | 123 | -85.2 | 504990 | 826 | -85.6 | 504990 | 829 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1228: `511f8a40-d25...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `511f8a40-d252-42de-a5dd-268f57ddf88d` |
| Tag | **single-answer** |
| 정답 | **C19** |
| C19 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1228] topology](images/train_1228.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3254435_4
- `C2`: Adjust the azimuth of 3276403_2 by 50 degrees
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3254435_4
- `C4`: Increase A3 Offset threshold for 3276403_2
- `C5`: Add neighbor relationship between 3212859_3 and 3254435_4
- `C6`: Decrease A3 Offset threshold for 3276403_2
- `C7`: Press down the tilt angle  of 3254435_4 by 4 degrees
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3276403_2
- `C9`: Add neighbor relationship between 3276403_2 and 3254435_4
- `C10`: Lift the tilt angle of 3276403_2 by 7 degrees
- `C11`: Press down the tilt angle of 3276403_2 by 7 degrees
- `C12`: Increase transmission power for 3276403_2
- `C13`: Decrease transmission power for 3254435_4
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3276403_2
- `C15`: Increase transmission power for 3254435_4
- `C16`: Increase A3 Offset threshold for 3254435_4
- `C17`: Adjust the azimuth of 3254435_4 by 42 degrees
- `C18`: Insufficient data; more data is needed for judgment.
- `C19`: Check test server and transmission issues **← 정답**
- `C20`: Decrease transmission power for 3276403_2
- `C21`: Lift the tilt angle  of 3254435_4 by 4 degrees
- `C22`: Decrease A3 Offset threshold for 3254435_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.521 | MS1 | 121.4656669308 | 31.1446239557 | 652 | 504990 | -87.36 | 14.62 | 360.05 | 0.03 | 2.51 | 1586 |
| 2024-09-20 22:21:32.246 | MS1 | 121.4656642078 | 31.1446313409 | 652 | 504990 | -85.17 | 13.61 | 536.42 | 0.01 | 2.51 | 1567 |
| 2024-09-20 22:21:33.348 | MS1 | 121.4656585629 | 31.1446325352 | 652 | 504990 | -85.89 | 16.36 | 374.47 | 0.12 | 2.92 | 1591 |
| 2024-09-20 22:21:34.625 | MS1 | 121.4656586033 | 31.1446324035 | 652 | 504990 | -86.12 | 15.30 | 62.68 | 0.09 | 2.19 | 499 |
| 2024-09-20 22:21:35.365 | MS1 | 121.4656744774 | 31.1446208330 | 652 | 504990 | -89.41 | 17.77 | 85.07 | 0.20 | 2.05 | 321 |
| 2024-09-20 22:21:36.251 | MS1 | 121.4656615331 | 31.1446272381 | 652 | 504990 | -87.82 | 13.59 | 57.15 | 0.20 | 2.08 | 339 |
| 2024-09-20 22:21:37.553 | MS1 | 121.4656762302 | 31.1446355444 | 652 | 504990 | -90.94 | 12.74 | 71.76 | 0.07 | 2.75 | 304 |
| 2024-09-20 22:21:38.687 | MS1 | 121.4656762176 | 31.1446182238 | 652 | 504990 | -89.77 | 11.19 | 82.49 | 0.09 | 2.76 | 391 |
| 2024-09-20 22:21:39.719 | MS1 | 121.4656703714 | 31.1446233189 | 652 | 504990 | -92.65 | 10.31 | 76.78 | 0.02 | 2.19 | 367 |
| 2024-09-20 22:21:40.814 | MS1 | 121.4656638796 | 31.1446226322 | 652 | 504990 | -90.75 | 9.10 | 355.48 | 0.16 | 2.57 | 1595 |
| 2024-09-20 22:21:41.960 | MS1 | 121.4656768759 | 31.1446308522 | 652 | 504990 | -92.56 | 11.00 | 566.29 | 0.15 | 2.74 | 1567 |
| 2024-09-20 22:21:42.542 | MS1 | 121.4656620003 | 31.1446352549 | 652 | 504990 | -91.07 | 10.30 | 568.14 | 0.05 | 2.57 | 1577 |

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
| 3212859 | 3 | 121.4671405113 | 31.1454886856 | 359 | 4 | 4 | 15.5 | TDD | 163 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3254435 | 4 | 121.4645837067 | 31.1520846194 | 131 | 3 | 1 | 18.6 | TDD | 679 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3271266 | 1 | 121.4680312712 | 31.1531889224 | 58 | 10 | 5 | 20.9 | TDD | 11 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3276403 | 2 | 121.4757406729 | 31.1531290054 | 32 | 6 | 0 | 19.6 | TDD | 652 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

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
| 2024-09-20 22:21:31.156 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.177 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.283 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.283 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.961 | NREventA3 | measId:2;ServCellPCI:866;Se... |
| 2024-09-20 22:21:38.201 | NRHandoverAttempt | SourcePCI:866;SourceNR-ARFC... |
| 2024-09-20 22:21:38.238 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.252 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.385 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.385 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3271266 | 1 | 5.8463 | 15.2145 | -117.3074 | 5.8628 | 124.6549 | 0.0043 | 0.0105 |
| 2024_09_20 22:00 | 3276403 | 2 | 5.9584 | 15.5407 | -117.7633 | 14.7331 | 152.5303 | 0.0103 | 0.0016 |
| 2024_09_20 22:00 | 3212859 | 3 | 8.1883 | 5.0031 | -114.7299 | 13.9608 | 196.1872 | 0.0157 | 0.0007 |
| 2024_09_20 22:00 | 3254435 | 4 | 16.8001 | 18.7770 | -115.8006 | 13.4004 | 90.9457 | 0.0037 | 0.0087 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413599_E693D47E | 504990 | 652 | -87.9 | 504990 | 679 | -92.3 | 504990 | 163 | -99.8 | 504990 | 11 |
| MR_1774413599_193BD8B9 | 504990 | 652 | -86.8 | 504990 | 679 | -90.4 | 504990 | 163 | -97.9 | 504990 | 11 |
| MR_1774413599_E9845233 | 504990 | 652 | -85.9 | 504990 | 679 | -89.7 | 504990 | 163 | -97.3 | 504990 | 11 |
| MR_1774413599_D6AD08C6 | 504990 | 652 | -86.9 | 504990 | 679 | -91.0 | 504990 | 163 | -98.5 | 504990 | 11 |
| MR_1774413599_80EE9907 | 504990 | 652 | -87.6 | 504990 | 679 | -90.4 | 504990 | 163 | -98.4 | 504990 | 11 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1229: `0e512699-46a...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `0e512699-46a6-451b-8e19-8987b1a6b21e` |
| Tag | **single-answer** |
| 정답 | **C2** |
| C2 의미 | Lift the tilt angle  of 3227471_4 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1229] topology](images/train_1229.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3213003_3
- `C2`: Lift the tilt angle  of 3227471_4 by 10 degrees **← 정답**
- `C3`: Lift the tilt angle of 3213003_3 by 5 degrees
- `C4`: Adjust the azimuth of 3227471_4 by 50 degrees
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3250355_2
- `C6`: Press down the tilt angle  of 3227471_4 by 10 degrees
- `C7`: Press down the tilt angle of 3213003_3 by 5 degrees
- `C8`: Increase transmission power for 3250355_2
- `C9`: Check test server and transmission issues
- `C10`: Decrease A3 Offset threshold for 3213003_3
- `C11`: Insufficient data; more data is needed for judgment.
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3213003_3
- `C13`: Decrease transmission power for 3250355_2
- `C14`: Add neighbor relationship between 3227471_4 and 3250355_2
- `C15`: Decrease A3 Offset threshold for 3250355_2
- `C16`: Increase transmission power for 3213003_3
- `C17`: Increase A3 Offset threshold for 3213003_3
- `C18`: Add neighbor relationship between 3213003_3 and 3250355_2
- `C19`: Decrease transmission power for 3213003_3
- `C20`: Adjust the azimuth of 3213003_3 by 40 degrees
- `C21`: Increase A3 Offset threshold for 3250355_2
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3250355_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.872 | MS1 | 121.4656612931 | 31.1446218230 | 782 | 504990 | -85.97 | 12.07 | 591.51 | 0.01 | 2.72 | 1570 |
| 2024-09-20 22:21:32.665 | MS1 | 121.4656604673 | 31.1446233869 | 782 | 504990 | -90.36 | 15.60 | 439.79 | 0.17 | 2.10 | 1576 |
| 2024-09-20 22:21:33.729 | MS1 | 121.4656627701 | 31.1446273678 | 782 | 504990 | -90.25 | 16.73 | 391.02 | 0.17 | 2.71 | 1579 |
| 2024-09-20 22:21:34.405 | MS1 | 121.4656674023 | 31.1446310295 | 782 | 504990 | -89.30 | 17.98 | 79.69 | 0.02 | 2.76 | 1578 |
| 2024-09-20 22:21:35.384 | MS1 | 121.4656655587 | 31.1446379808 | 782 | 504990 | -88.43 | 15.93 | 67.18 | 0.18 | 2.67 | 1572 |
| 2024-09-20 22:21:36.235 | MS1 | 121.4656776247 | 31.1446295441 | 782 | 504990 | -89.21 | 12.48 | 89.38 | 0.12 | 2.45 | 1571 |
| 2024-09-20 22:21:37.458 | MS1 | 121.4656642725 | 31.1446212563 | 782 | 504990 | -93.44 | 10.84 | 92.74 | 0.02 | 2.07 | 1590 |
| 2024-09-20 22:21:38.616 | MS1 | 121.4656638044 | 31.1446217322 | 782 | 504990 | -90.06 | 9.69 | 62.80 | 0.15 | 2.64 | 1581 |
| 2024-09-20 22:21:39.706 | MS1 | 121.4656732419 | 31.1446312058 | 782 | 504990 | -92.36 | 10.72 | 62.67 | 0.04 | 2.58 | 1593 |
| 2024-09-20 22:21:40.242 | MS1 | 121.4656607525 | 31.1446267539 | 782 | 504990 | -91.27 | 12.37 | 366.92 | 0.07 | 2.36 | 1594 |
| 2024-09-20 22:21:41.317 | MS1 | 121.4656746712 | 31.1446197460 | 782 | 504990 | -93.55 | 7.66 | 396.12 | 0.07 | 2.47 | 1592 |
| 2024-09-20 22:21:42.803 | MS1 | 121.4656678712 | 31.1446298777 | 782 | 504990 | -90.66 | 11.91 | 597.46 | 0.12 | 2.71 | 1593 |

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
| 3213003 | 3 | 121.4738883708 | 31.1461374960 | 298 | 2 | 0 | 47.8 | TDD | 782 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3227471 | 4 | 121.4654491575 | 31.1498573968 | 53 | 12 | 5 | 19.1 | TDD | 642 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3231696 | 1 | 121.4656892524 | 31.1440195442 | 120 | 14 | 0 | 17.2 | TDD | 8 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3250355 | 2 | 121.4667506899 | 31.1449938486 | 34 | 6 | 1 | 19.1 | TDD | 338 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:31.432 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.454 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.585 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.585 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.241 | NREventA3 | measId:2;ServCellPCI:853;Se... |
| 2024-09-20 22:21:38.481 | NRHandoverAttempt | SourcePCI:853;SourceNR-ARFC... |
| 2024-09-20 22:21:38.530 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.545 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.662 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.662 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3231696 | 1 | 12.3802 | 8.2055 | -117.0517 | 11.3131 | 86.0533 | 0.0148 | 0.0177 |
| 2024_09_20 22:00 | 3250355 | 2 | 8.3565 | 11.1590 | -115.1442 | 14.9113 | 147.8452 | 0.0006 | 0.0155 |
| 2024_09_20 22:00 | 3213003 | 3 | 82.5839 | 78.6100 | -117.7358 | 14.4503 | 88.0611 | 0.0142 | 0.0045 |
| 2024_09_20 22:00 | 3227471 | 4 | 10.5274 | 5.8361 | -116.5644 | 18.2007 | 123.3350 | 0.0048 | 0.0143 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415395_9BE92166 | 504990 | 782 | -88.4 | 504990 | 338 | -91.3 | 504990 | 642 | -100.4 | 504990 | 8 |
| MR_1774415395_3A71A800 | 504990 | 782 | -88.9 | 504990 | 338 | -90.7 | 504990 | 642 | -101.8 | 504990 | 8 |
| MR_1774415395_42FAC66B | 504990 | 782 | -89.8 | 504990 | 338 | -94.0 | 504990 | 642 | -101.2 | 504990 | 8 |
| MR_1774415395_66E61775 | 504990 | 782 | -90.8 | 504990 | 338 | -93.5 | 504990 | 642 | -102.1 | 504990 | 8 |
| MR_1774415395_3CD2583C | 504990 | 782 | -88.6 | 504990 | 338 | -92.3 | 504990 | 642 | -101.8 | 504990 | 8 |

> *... 2개 열 생략 (전체 14열)*

---
