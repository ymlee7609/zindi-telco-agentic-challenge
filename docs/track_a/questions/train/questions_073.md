# Track A 문제 분석 — train[720]~train[729]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[720] ~ train[729] (10개)

## 목차

1. [문제 720: `53960a5b-17a...`](#720) — single-answer, 정답: C3
2. [문제 721: `e3a255cd-7b5...`](#721) — single-answer, 정답: C16
3. [문제 722: `5f830b06-458...`](#722) — single-answer, 정답: C11
4. [문제 723: `59390ace-7c8...`](#723) — single-answer, 정답: C22
5. [문제 724: `dd081817-aa0...`](#724) — single-answer, 정답: C5
6. [문제 725: `da107c99-e24...`](#725) — single-answer, 정답: C1
7. [문제 726: `21b623cd-70f...`](#726) — single-answer, 정답: C9
8. [문제 727: `14287718-131...`](#727) — single-answer, 정답: C3
9. [문제 728: `d58adad2-e1c...`](#728) — single-answer, 정답: C17
10. [문제 729: `3cf7aeec-9a1...`](#729) — single-answer, 정답: C15

---

### 문제 720: `53960a5b-17a...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `53960a5b-17a5-4230-bc75-986ba9397461` |
| Tag | **single-answer** |
| 정답 | **C3** |
| C3 의미 | Decrease A3 Offset threshold for 3220464_3 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[720] topology](images/train_0720.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3218012_1
- `C2`: Add neighbor relationship between 3220464_3 and 3218012_1
- `C3`: Decrease A3 Offset threshold for 3220464_3 **← 정답**
- `C4`: Increase A3 Offset threshold for 3218012_1
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3218012_1
- `C6`: Decrease transmission power for 3218012_1
- `C7`: Increase transmission power for 3220464_3
- `C8`: Adjust the azimuth of 3220464_3 by 50 degrees
- `C9`: Increase A3 Offset threshold for 3220464_3
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3220464_3
- `C11`: Lift the tilt angle of 3220464_3 by 6 degrees
- `C12`: Add neighbor relationship between 3237103_2 and 3218012_1
- `C13`: Press down the tilt angle  of 3218012_1 by 10 degrees
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3220464_3
- `C16`: Press down the tilt angle of 3220464_3 by 6 degrees
- `C17`: Decrease A3 Offset threshold for 3218012_1
- `C18`: Adjust the azimuth of 3218012_1 by 50 degrees
- `C19`: Check test server and transmission issues
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3218012_1
- `C21`: Decrease transmission power for 3220464_3
- `C22`: Lift the tilt angle  of 3218012_1 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.890 | MS1 | 121.4656701350 | 31.1446259896 | 666 | 504990 | -82.90 | 12.38 | 308.82 | 0.17 | 2.68 | 1586 |
| 2024-09-20 22:21:32.487 | MS1 | 121.4656758723 | 31.1446239752 | 666 | 504990 | -84.04 | 17.46 | 441.05 | 0.02 | 2.63 | 1579 |
| 2024-09-20 22:21:33.363 | MS1 | 121.4656767668 | 31.1446262435 | 666 | 504990 | -76.79 | 16.55 | 346.97 | 0.02 | 2.23 | 1569 |
| 2024-09-20 22:21:34.360 | MS1 | 121.4656661692 | 31.1446188081 | 666 | 504990 | -89.95 | -2.49 | 65.12 | 0.10 | 1.31 | 1568 |
| 2024-09-20 22:21:35.639 | MS1 | 121.4656720262 | 31.1446281826 | 666 | 504990 | -92.19 | -1.40 | 40.06 | 0.13 | 1.16 | 1568 |
| 2024-09-20 22:21:36.277 | MS1 | 121.4656615763 | 31.1446277988 | 666 | 504990 | -89.41 | -3.04 | 44.92 | 0.05 | 1.09 | 1579 |
| 2024-09-20 22:21:37.447 | MS1 | 121.4656767974 | 31.1446373376 | 666 | 504990 | -91.04 | -1.16 | 38.28 | 0.10 | 1.42 | 1573 |
| 2024-09-20 22:21:38.607 | MS1 | 121.4656707838 | 31.1446327628 | 666 | 504990 | -90.05 | -0.48 | 35.30 | 0.19 | 1.24 | 1567 |
| 2024-09-20 22:21:39.946 | MS1 | 121.4656665747 | 31.1446201291 | 528 | 504990 | -79.32 | 12.50 | 245.14 | 0.07 | 1.21 | 1589 |
| 2024-09-20 22:21:40.529 | MS1 | 121.4656668951 | 31.1446195465 | 528 | 504990 | -82.03 | 14.29 | 476.34 | 0.16 | 2.76 | 1587 |
| 2024-09-20 22:21:41.265 | MS1 | 121.4656751547 | 31.1446197859 | 528 | 504990 | -84.63 | 17.50 | 485.17 | 0.18 | 2.31 | 1563 |
| 2024-09-20 22:21:42.213 | MS1 | 121.4656651591 | 31.1446328344 | 528 | 504990 | -79.36 | 14.65 | 590.49 | 0.08 | 2.88 | 1571 |

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
| 3218012 | 1 | 121.4706738881 | 31.1477417366 | 118 | 13 | 3 | 36.9 | TDD | 528 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3220464 | 3 | 121.4757432574 | 31.1498485861 | 24 | 4 | 8 | 36.6 | TDD | 666 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3237103 | 2 | 121.4700123402 | 31.1492186797 | 65 | 7 | 6 | 22.3 | TDD | 345 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3250050 | 4 | 121.4744049085 | 31.1559663548 | 299 | 10 | 5 | 36.8 | TDD | 824 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:31.005 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.148 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.148 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.884 | NREventA3 | measId:2;ServCellPCI:975;Se... |
| 2024-09-20 22:21:38.124 | NRHandoverAttempt | SourcePCI:975;SourceNR-ARFC... |
| 2024-09-20 22:21:38.160 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.175 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.289 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.289 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3218012 | 1 | 19.6679 | 15.6906 | -116.2264 | 10.4695 | 174.5811 | 0.0167 | 0.0040 |
| 2024_09_20 22:00 | 3237103 | 2 | 13.7027 | 14.9622 | -115.5660 | 13.0579 | 196.9636 | 0.0162 | 0.0083 |
| 2024_09_20 22:00 | 3220464 | 3 | 9.6491 | 11.6687 | -116.0076 | 12.3199 | 113.6983 | 0.0058 | 0.1197 |
| 2024_09_20 22:00 | 3250050 | 4 | 10.9726 | 9.8761 | -115.4950 | 10.0812 | 179.9905 | 0.0183 | 0.0159 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412939_2E759AFC | 504990 | 666 | -89.4 | 504990 | 528 | -86.0 | 504990 | 345 | -88.9 | 504990 | 824 |
| MR_1774412939_4ADC2D25 | 504990 | 666 | -89.4 | 504990 | 528 | -85.7 | 504990 | 345 | -88.7 | 504990 | 824 |
| MR_1774412939_3A7EFC05 | 504990 | 666 | -88.6 | 504990 | 528 | -82.8 | 504990 | 345 | -89.9 | 504990 | 824 |
| MR_1774412939_D69E108D | 504990 | 666 | -90.7 | 504990 | 528 | -86.2 | 504990 | 345 | -91.0 | 504990 | 824 |
| MR_1774412939_F37BE41B | 504990 | 528 | -85.9 | 504990 | 666 | -91.2 | 504990 | 345 | -91.9 | 504990 | 824 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 721: `e3a255cd-7b5...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `e3a255cd-7b58-4eec-a3fa-2cdebe47690e` |
| Tag | **single-answer** |
| 정답 | **C16** |
| C16 의미 | Lift the tilt angle  of 3254761_1 by 5 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[721] topology](images/train_0721.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3247130_2 by 7 degrees
- `C2`: Add neighbor relationship between 3254761_1 and 3254107_4
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3254107_4
- `C4`: Adjust the azimuth of 3254761_1 by 32 degrees
- `C5`: Decrease A3 Offset threshold for 3254107_4
- `C6`: Increase transmission power for 3247130_2
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3247130_2
- `C8`: Increase A3 Offset threshold for 3254107_4
- `C9`: Decrease transmission power for 3247130_2
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3254107_4
- `C11`: Check test server and transmission issues
- `C12`: Decrease transmission power for 3254107_4
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3247130_2
- `C14`: Add neighbor relationship between 3247130_2 and 3254107_4
- `C15`: Increase A3 Offset threshold for 3247130_2
- `C16`: Lift the tilt angle  of 3254761_1 by 5 degrees **← 정답**
- `C17`: Decrease A3 Offset threshold for 3247130_2
- `C18`: Press down the tilt angle  of 3254761_1 by 5 degrees
- `C19`: Insufficient data; more data is needed for judgment.
- `C20`: Lift the tilt angle of 3247130_2 by 2 degrees
- `C21`: Increase transmission power for 3254107_4
- `C22`: Press down the tilt angle of 3247130_2 by 2 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.320 | MS1 | 121.4656670818 | 31.1446298380 | 220 | 504990 | -89.65 | 12.43 | 494.97 | 0.13 | 2.34 | 1590 |
| 2024-09-20 22:21:32.959 | MS1 | 121.4656647508 | 31.1446263185 | 220 | 504990 | -87.89 | 13.74 | 444.09 | 0.11 | 2.32 | 1584 |
| 2024-09-20 22:21:33.697 | MS1 | 121.4656688919 | 31.1446365434 | 220 | 504990 | -85.99 | 12.59 | 518.35 | 0.03 | 2.43 | 1594 |
| 2024-09-20 22:21:34.412 | MS1 | 121.4656715944 | 31.1446285273 | 220 | 504990 | -86.62 | 17.08 | 82.06 | 0.00 | 2.09 | 1595 |
| 2024-09-20 22:21:35.743 | MS1 | 121.4656750892 | 31.1446265313 | 220 | 504990 | -90.57 | 13.46 | 81.76 | 0.10 | 2.54 | 1575 |
| 2024-09-20 22:21:36.543 | MS1 | 121.4656731216 | 31.1446197827 | 220 | 504990 | -85.85 | 16.65 | 63.63 | 0.19 | 2.70 | 1588 |
| 2024-09-20 22:21:37.276 | MS1 | 121.4656615110 | 31.1446362597 | 220 | 504990 | -90.03 | 12.09 | 72.17 | 0.10 | 2.31 | 1597 |
| 2024-09-20 22:21:38.287 | MS1 | 121.4656676464 | 31.1446336660 | 220 | 504990 | -92.37 | 10.96 | 57.34 | 0.20 | 2.60 | 1598 |
| 2024-09-20 22:21:39.187 | MS1 | 121.4656661286 | 31.1446221499 | 220 | 504990 | -89.10 | 7.28 | 97.27 | 0.09 | 2.45 | 1569 |
| 2024-09-20 22:21:40.950 | MS1 | 121.4656714071 | 31.1446188570 | 220 | 504990 | -92.13 | 12.73 | 422.12 | 0.06 | 2.56 | 1569 |
| 2024-09-20 22:21:41.120 | MS1 | 121.4656640537 | 31.1446245644 | 220 | 504990 | -89.83 | 7.75 | 365.69 | 0.07 | 2.18 | 1586 |
| 2024-09-20 22:21:42.316 | MS1 | 121.4656767520 | 31.1446274500 | 220 | 504990 | -90.14 | 11.95 | 537.60 | 0.03 | 2.36 | 1599 |

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
| 3214885 | 3 | 121.4686582719 | 31.1475855017 | 261 | 9 | 1 | 28.8 | TDD | 196 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3247130 | 2 | 121.4735591773 | 31.1551253691 | 220 | 1 | 6 | 24.6 | TDD | 220 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3254107 | 4 | 121.4753111593 | 31.1479929562 | 280 | 3 | 4 | 41.5 | TDD | 55 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3254761 | 1 | 121.4665306027 | 31.1500773671 | 116 | 4 | 11 | 40.5 | TDD | 610 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |

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
| 2024-09-20 22:21:31.093 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.110 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.254 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.254 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.903 | NREventA3 | measId:2;ServCellPCI:754;Se... |
| 2024-09-20 22:21:38.143 | NRHandoverAttempt | SourcePCI:754;SourceNR-ARFC... |
| 2024-09-20 22:21:38.174 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.187 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.335 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.335 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3254761 | 1 | 7.9511 | 12.4527 | -114.8331 | 7.3885 | 82.1834 | 0.0002 | 0.0035 |
| 2024_09_20 22:00 | 3247130 | 2 | 76.0554 | 80.6251 | -115.5803 | 9.8980 | 192.2968 | 0.0147 | 0.0027 |
| 2024_09_20 22:00 | 3214885 | 3 | 16.0771 | 19.6510 | -117.4985 | 6.5287 | 115.3918 | 0.0076 | 0.0027 |
| 2024_09_20 22:00 | 3254107 | 4 | 9.9900 | 8.8040 | -114.0525 | 11.1687 | 185.3069 | 0.0125 | 0.0156 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415882_48CF9915 | 504990 | 220 | -86.6 | 504990 | 55 | -86.2 | 504990 | 610 | -92.5 | 504990 | 196 |
| MR_1774415882_8D14D2F4 | 504990 | 220 | -88.2 | 504990 | 55 | -86.4 | 504990 | 610 | -94.0 | 504990 | 196 |
| MR_1774415882_DE13E101 | 504990 | 220 | -85.9 | 504990 | 55 | -89.1 | 504990 | 610 | -95.8 | 504990 | 196 |
| MR_1774415882_9EE2699B | 504990 | 220 | -88.1 | 504990 | 55 | -86.3 | 504990 | 610 | -92.2 | 504990 | 196 |
| MR_1774415882_2052B3F0 | 504990 | 220 | -85.6 | 504990 | 55 | -88.1 | 504990 | 610 | -95.7 | 504990 | 196 |
| MR_1774415882_35CEFE2B | 504990 | 220 | -88.1 | 504990 | 55 | -88.5 | 504990 | 610 | -93.9 | 504990 | 196 |
| MR_1774415882_B8844436 | 504990 | 220 | -88.3 | 504990 | 55 | -89.6 | 504990 | 610 | -93.9 | 504990 | 196 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 722: `5f830b06-458...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `5f830b06-458b-49be-8ae5-64f964aa7b98` |
| Tag | **single-answer** |
| 정답 | **C11** |
| C11 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3260172_3 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[722] topology](images/train_0722.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3234118_1
- `C2`: Lift the tilt angle  of 3234118_1 by 10 degrees
- `C3`: Adjust the azimuth of 3260172_3 by 20 degrees
- `C4`: Increase transmission power for 3260172_3
- `C5`: Add neighbor relationship between 3260172_3 and 3234118_1
- `C6`: Decrease transmission power for 3234118_1
- `C7`: Decrease A3 Offset threshold for 3260172_3
- `C8`: Decrease A3 Offset threshold for 3234118_1
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3234118_1
- `C10`: Increase transmission power for 3234118_1
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3260172_3 **← 정답**
- `C12`: Adjust the azimuth of 3234118_1 by 50 degrees
- `C13`: Lift the tilt angle of 3260172_3 by 4 degrees
- `C14`: Add neighbor relationship between 3216871_4 and 3234118_1
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3234118_1
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3260172_3
- `C17`: Insufficient data; more data is needed for judgment.
- `C18`: Increase A3 Offset threshold for 3260172_3
- `C19`: Press down the tilt angle of 3260172_3 by 4 degrees
- `C20`: Press down the tilt angle  of 3234118_1 by 10 degrees
- `C21`: Check test server and transmission issues
- `C22`: Decrease transmission power for 3260172_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.823 | MS1 | 121.4656653152 | 31.1446190879 | 772 | 504990 | -88.70 | 15.89 | 334.85 | 0.07 | 2.21 | 1570 |
| 2024-09-20 22:21:32.693 | MS1 | 121.4656626296 | 31.1446216202 | 772 | 504990 | -87.73 | 16.40 | 459.77 | 0.09 | 2.24 | 1588 |
| 2024-09-20 22:21:33.814 | MS1 | 121.4656735852 | 31.1446207722 | 772 | 504990 | -88.42 | 14.10 | 416.85 | 0.06 | 2.10 | 1575 |
| 2024-09-20 22:21:34.763 | MS1 | 121.4656711290 | 31.1446237214 | 772 | 504990 | -85.02 | 12.90 | 67.39 | 0.55 | 2.88 | 636 |
| 2024-09-20 22:21:35.547 | MS1 | 121.4656768685 | 31.1446285808 | 772 | 504990 | -91.45 | 12.33 | 67.89 | 0.60 | 2.32 | 513 |
| 2024-09-20 22:21:36.877 | MS1 | 121.4656643439 | 31.1446272331 | 772 | 504990 | -86.60 | 12.13 | 66.91 | 0.59 | 2.61 | 673 |
| 2024-09-20 22:21:37.751 | MS1 | 121.4656760858 | 31.1446262096 | 772 | 504990 | -92.94 | 9.18 | 83.97 | 0.64 | 2.29 | 564 |
| 2024-09-20 22:21:38.874 | MS1 | 121.4656768444 | 31.1446260827 | 772 | 504990 | -92.90 | 7.56 | 56.34 | 0.59 | 2.13 | 638 |
| 2024-09-20 22:21:39.427 | MS1 | 121.4656694004 | 31.1446318266 | 772 | 504990 | -90.08 | 9.76 | 86.31 | 0.65 | 2.48 | 536 |
| 2024-09-20 22:21:40.623 | MS1 | 121.4656700319 | 31.1446306277 | 772 | 504990 | -92.68 | 10.03 | 560.39 | 0.08 | 2.45 | 1570 |
| 2024-09-20 22:21:41.215 | MS1 | 121.4656635819 | 31.1446322186 | 772 | 504990 | -93.17 | 10.95 | 386.53 | 0.03 | 2.57 | 1572 |
| 2024-09-20 22:21:42.762 | MS1 | 121.4656747927 | 31.1446337175 | 772 | 504990 | -89.39 | 8.25 | 322.47 | 0.18 | 2.18 | 1595 |

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
| 3216871 | 4 | 121.4747694654 | 31.1508104182 | 108 | 6 | 11 | 31.4 | TDD | 127 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3234118 | 1 | 121.4649960760 | 31.1542222518 | 61 | 13 | 12 | 38.9 | TDD | 16 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3239050 | 2 | 121.4669601502 | 31.1456357755 | 178 | 10 | 6 | 15.1 | TDD | 58 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3260172 | 3 | 121.4723734986 | 31.1466131003 | 271 | 1 | 2 | 29.9 | TDD | 772 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |

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
| 2024-09-20 22:21:31.208 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.232 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.349 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.349 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.060 | NREventA3 | measId:2;ServCellPCI:3;Serv... |
| 2024-09-20 22:21:38.300 | NRHandoverAttempt | SourcePCI:3;SourceNR-ARFCN:... |
| 2024-09-20 22:21:38.338 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.352 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.498 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.498 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3234118 | 1 | 13.0016 | 5.8801 | -117.4588 | 12.8526 | 149.0839 | 0.0194 | 0.0088 |
| 2024_09_20 22:00 | 3239050 | 2 | 15.2757 | 18.5731 | -116.7983 | 13.8381 | 80.0982 | 0.0095 | 0.0009 |
| 2024_09_20 22:00 | 3260172 | 3 | 17.6046 | 11.8712 | -116.3599 | 13.0461 | 183.0910 | 0.0003 | 0.0169 |
| 2024_09_20 22:00 | 3216871 | 4 | 16.3111 | 14.5782 | -116.7159 | 5.7341 | 95.5526 | 0.0115 | 0.0075 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416539_B3E87E1C | 504990 | 772 | -86.3 | 504990 | 16 | -89.2 | 504990 | 127 | -93.4 | 504990 | 58 |
| MR_1774416539_F7B54F24 | 504990 | 772 | -84.2 | 504990 | 16 | -90.5 | 504990 | 127 | -96.3 | 504990 | 58 |
| MR_1774416539_9EC3DA49 | 504990 | 772 | -84.6 | 504990 | 16 | -87.5 | 504990 | 127 | -94.3 | 504990 | 58 |
| MR_1774416539_B381FD88 | 504990 | 772 | -84.7 | 504990 | 16 | -88.3 | 504990 | 127 | -94.6 | 504990 | 58 |
| MR_1774416539_AC39CDBF | 504990 | 772 | -84.1 | 504990 | 16 | -89.5 | 504990 | 127 | -96.7 | 504990 | 58 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 723: `59390ace-7c8...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `59390ace-7c89-429d-a4d0-35ecfd22520c` |
| Tag | **single-answer** |
| 정답 | **C22** |
| C22 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3261783_2 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[723] topology](images/train_0723.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3260744_4
- `C2`: Decrease A3 Offset threshold for 3261783_2
- `C3`: Adjust the azimuth of 3261783_2 by 39 degrees
- `C4`: Press down the tilt angle  of 3260744_4 by 10 degrees
- `C5`: Insufficient data; more data is needed for judgment.
- `C6`: Increase transmission power for 3260744_4
- `C7`: Decrease transmission power for 3260744_4
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3260744_4
- `C9`: Increase transmission power for 3261783_2
- `C10`: Increase A3 Offset threshold for 3261783_2
- `C11`: Decrease transmission power for 3261783_2
- `C12`: Add neighbor relationship between 3261783_2 and 3260744_4
- `C13`: Decrease A3 Offset threshold for 3260744_4
- `C14`: Lift the tilt angle  of 3260744_4 by 10 degrees
- `C15`: Add neighbor relationship between 3270961_1 and 3260744_4
- `C16`: Increase A3 Offset threshold for 3260744_4
- `C17`: Adjust the azimuth of 3260744_4 by 50 degrees
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3261783_2
- `C19`: Check test server and transmission issues
- `C20`: Press down the tilt angle of 3261783_2 by 4 degrees
- `C21`: Lift the tilt angle of 3261783_2 by 4 degrees
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3261783_2 **← 정답**

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.864 | MS1 | 121.4656623112 | 31.1446230281 | 531 | 504990 | -91.66 | 14.33 | 505.88 | 0.18 | 2.42 | 1560 |
| 2024-09-20 22:21:32.475 | MS1 | 121.4656690226 | 31.1446327555 | 531 | 504990 | -89.90 | 15.00 | 383.97 | 0.16 | 2.91 | 1565 |
| 2024-09-20 22:21:33.146 | MS1 | 121.4656622094 | 31.1446311938 | 531 | 504990 | -86.12 | 16.69 | 593.42 | 0.06 | 2.68 | 1560 |
| 2024-09-20 22:21:34.391 | MS1 | 121.4656616414 | 31.1446264224 | 531 | 504990 | -90.71 | 13.42 | 108.02 | 0.51 | 2.47 | 602 |
| 2024-09-20 22:21:35.232 | MS1 | 121.4656731455 | 31.1446184527 | 531 | 504990 | -89.09 | 14.47 | 53.81 | 0.66 | 2.73 | 576 |
| 2024-09-20 22:21:36.528 | MS1 | 121.4656770773 | 31.1446329942 | 531 | 504990 | -89.72 | 14.26 | 88.64 | 0.65 | 2.64 | 562 |
| 2024-09-20 22:21:37.982 | MS1 | 121.4656653752 | 31.1446200983 | 531 | 504990 | -93.64 | 10.42 | 70.32 | 0.59 | 2.47 | 540 |
| 2024-09-20 22:21:38.517 | MS1 | 121.4656673185 | 31.1446245165 | 531 | 504990 | -93.66 | 9.72 | 61.97 | 0.66 | 2.77 | 546 |
| 2024-09-20 22:21:39.452 | MS1 | 121.4656688431 | 31.1446359803 | 531 | 504990 | -93.77 | 9.16 | 70.12 | 0.52 | 2.71 | 677 |
| 2024-09-20 22:21:40.814 | MS1 | 121.4656705587 | 31.1446267931 | 531 | 504990 | -89.08 | 9.55 | 482.59 | 0.16 | 2.97 | 1569 |
| 2024-09-20 22:21:41.404 | MS1 | 121.4656614279 | 31.1446249392 | 531 | 504990 | -90.95 | 12.15 | 473.53 | 0.14 | 2.80 | 1575 |
| 2024-09-20 22:21:42.903 | MS1 | 121.4656613093 | 31.1446337813 | 531 | 504990 | -92.56 | 10.54 | 491.02 | 0.02 | 2.79 | 1569 |

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
| 3260744 | 4 | 121.4728661776 | 31.1467550723 | 308 | 14 | 6 | 48.0 | TDD | 718 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3261783 | 2 | 121.4652575522 | 31.1526275400 | 138 | 2 | 8 | 33.0 | TDD | 531 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3270961 | 1 | 121.4702443019 | 31.1526189230 | 193 | 2 | 12 | 26.9 | TDD | 754 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3271936 | 3 | 121.4749251981 | 31.1462756145 | 213 | 2 | 8 | 30.1 | TDD | 564 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |

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
| 2024-09-20 22:21:30.813 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.833 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:30.935 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.935 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.619 | NREventA3 | measId:2;ServCellPCI:319;Se... |
| 2024-09-20 22:21:37.859 | NRHandoverAttempt | SourcePCI:319;SourceNR-ARFC... |
| 2024-09-20 22:21:37.908 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.921 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.037 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.037 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3270961 | 1 | 12.3178 | 12.5689 | -116.5293 | 17.9580 | 120.1429 | 0.0185 | 0.0158 |
| 2024_09_20 22:00 | 3261783 | 2 | 11.4669 | 17.8205 | -114.1880 | 6.8660 | 182.7234 | 0.0183 | 0.0104 |
| 2024_09_20 22:00 | 3271936 | 3 | 15.6696 | 7.5169 | -117.6402 | 7.3358 | 84.0432 | 0.0176 | 0.0116 |
| 2024_09_20 22:00 | 3260744 | 4 | 18.3109 | 7.4448 | -117.6492 | 17.4563 | 103.0909 | 0.0144 | 0.0030 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414085_B47957E5 | 504990 | 531 | -88.6 | 504990 | 718 | -94.3 | 504990 | 754 | -100.2 | 504990 | 564 |
| MR_1774414085_491ED384 | 504990 | 531 | -89.0 | 504990 | 718 | -97.0 | 504990 | 754 | -99.6 | 504990 | 564 |
| MR_1774414085_4D07DFB5 | 504990 | 531 | -88.6 | 504990 | 718 | -98.0 | 504990 | 754 | -96.8 | 504990 | 564 |
| MR_1774414085_CB998D4E | 504990 | 531 | -91.0 | 504990 | 718 | -96.3 | 504990 | 754 | -98.6 | 504990 | 564 |
| MR_1774414085_7453A2FA | 504990 | 531 | -87.3 | 504990 | 718 | -97.6 | 504990 | 754 | -99.2 | 504990 | 564 |
| MR_1774414085_B3FF9563 | 504990 | 531 | -89.7 | 504990 | 718 | -95.6 | 504990 | 754 | -100.1 | 504990 | 564 |
| MR_1774414085_F95F20D4 | 504990 | 531 | -90.4 | 504990 | 718 | -95.3 | 504990 | 754 | -97.5 | 504990 | 564 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 724: `dd081817-aa0...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `dd081817-aa0a-4cd1-b193-1c6f40b36c69` |
| Tag | **single-answer** |
| 정답 | **C5** |
| C5 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3212538_2 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[724] topology](images/train_0724.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3279570_4 by 10 degrees
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3279570_4
- `C3`: Increase A3 Offset threshold for 3212538_2
- `C4`: Adjust the azimuth of 3212538_2 by 37 degrees
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3212538_2 **← 정답**
- `C6`: Check test server and transmission issues
- `C7`: Decrease transmission power for 3212538_2
- `C8`: Increase transmission power for 3212538_2
- `C9`: Press down the tilt angle of 3212538_2 by 2 degrees
- `C10`: Add neighbor relationship between 3210544_1 and 3279570_4
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3279570_4
- `C12`: Insufficient data; more data is needed for judgment.
- `C13`: Add neighbor relationship between 3212538_2 and 3279570_4
- `C14`: Lift the tilt angle of 3212538_2 by 2 degrees
- `C15`: Decrease transmission power for 3279570_4
- `C16`: Decrease A3 Offset threshold for 3279570_4
- `C17`: Adjust the azimuth of 3279570_4 by 50 degrees
- `C18`: Increase A3 Offset threshold for 3279570_4
- `C19`: Lift the tilt angle  of 3279570_4 by 10 degrees
- `C20`: Increase transmission power for 3279570_4
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3212538_2
- `C22`: Decrease A3 Offset threshold for 3212538_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.743 | MS1 | 121.4656731647 | 31.1446293234 | 434 | 504990 | -89.51 | 14.50 | 329.39 | 0.17 | 2.64 | 1569 |
| 2024-09-20 22:21:32.677 | MS1 | 121.4656688695 | 31.1446198143 | 434 | 504990 | -86.10 | 14.48 | 314.76 | 0.02 | 2.09 | 1593 |
| 2024-09-20 22:21:33.992 | MS1 | 121.4656723807 | 31.1446319258 | 434 | 504990 | -90.07 | 14.54 | 325.06 | 0.08 | 2.93 | 1579 |
| 2024-09-20 22:21:34.477 | MS1 | 121.4656685433 | 31.1446305446 | 434 | 504990 | -87.68 | 17.89 | 87.47 | 0.62 | 2.23 | 500 |
| 2024-09-20 22:21:35.302 | MS1 | 121.4656705114 | 31.1446203496 | 434 | 504990 | -88.67 | 15.56 | 70.62 | 0.61 | 2.53 | 633 |
| 2024-09-20 22:21:36.122 | MS1 | 121.4656763894 | 31.1446346535 | 434 | 504990 | -85.85 | 15.35 | 92.57 | 0.58 | 2.17 | 603 |
| 2024-09-20 22:21:37.107 | MS1 | 121.4656668380 | 31.1446218078 | 434 | 504990 | -92.50 | 12.85 | 100.51 | 0.62 | 2.62 | 636 |
| 2024-09-20 22:21:38.914 | MS1 | 121.4656583724 | 31.1446182346 | 434 | 504990 | -93.57 | 11.16 | 58.18 | 0.52 | 2.01 | 665 |
| 2024-09-20 22:21:39.706 | MS1 | 121.4656643322 | 31.1446365294 | 434 | 504990 | -91.71 | 11.49 | 64.30 | 0.55 | 2.30 | 681 |
| 2024-09-20 22:21:40.971 | MS1 | 121.4656597804 | 31.1446263006 | 434 | 504990 | -92.67 | 12.84 | 357.85 | 0.17 | 2.31 | 1570 |
| 2024-09-20 22:21:41.242 | MS1 | 121.4656749762 | 31.1446184613 | 434 | 504990 | -93.46 | 8.03 | 602.98 | 0.14 | 2.64 | 1580 |
| 2024-09-20 22:21:42.247 | MS1 | 121.4656675358 | 31.1446273829 | 434 | 504990 | -93.40 | 11.79 | 413.71 | 0.00 | 2.79 | 1563 |

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
| 3210544 | 1 | 121.4660578180 | 31.1465985516 | 150 | 5 | 0 | 44.0 | TDD | 745 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3212538 | 2 | 121.4676845382 | 31.1494539404 | 163 | 0 | 0 | 18.0 | TDD | 434 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3275735 | 3 | 121.4669900726 | 31.1511500624 | 125 | 7 | 0 | 24.9 | TDD | 955 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3279570 | 4 | 121.4661559525 | 31.1467091370 | 320 | 7 | 1 | 48.8 | TDD | 743 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |

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
| 2024-09-20 22:21:31.494 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.517 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.652 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.652 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.362 | NREventA3 | measId:2;ServCellPCI:649;Se... |
| 2024-09-20 22:21:38.602 | NRHandoverAttempt | SourcePCI:649;SourceNR-ARFC... |
| 2024-09-20 22:21:38.643 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.658 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.802 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.802 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3210544 | 1 | 16.2905 | 6.4025 | -114.8812 | 13.0226 | 152.8565 | 0.0106 | 0.0104 |
| 2024_09_20 22:00 | 3212538 | 2 | 19.4051 | 8.3962 | -117.8072 | 7.5793 | 152.6833 | 0.0155 | 0.0013 |
| 2024_09_20 22:00 | 3275735 | 3 | 14.4523 | 14.9575 | -116.9198 | 6.0504 | 135.5330 | 0.0178 | 0.0139 |
| 2024_09_20 22:00 | 3279570 | 4 | 7.4752 | 9.8031 | -117.9934 | 7.3413 | 164.8865 | 0.0084 | 0.0001 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416490_D83EBC12 | 504990 | 434 | -88.7 | 504990 | 743 | -98.6 | 504990 | 745 | -99.5 | 504990 | 955 |
| MR_1774416490_21A50C4B | 504990 | 434 | -89.3 | 504990 | 743 | -96.2 | 504990 | 745 | -97.7 | 504990 | 955 |
| MR_1774416490_7F506DE9 | 504990 | 434 | -89.1 | 504990 | 743 | -99.1 | 504990 | 745 | -97.7 | 504990 | 955 |
| MR_1774416490_C799FA20 | 504990 | 434 | -86.0 | 504990 | 743 | -97.2 | 504990 | 745 | -98.0 | 504990 | 955 |
| MR_1774416490_26B0DE04 | 504990 | 434 | -86.4 | 504990 | 743 | -97.7 | 504990 | 745 | -100.4 | 504990 | 955 |
| MR_1774416490_44AC72E2 | 504990 | 434 | -88.7 | 504990 | 743 | -97.8 | 504990 | 745 | -98.6 | 504990 | 955 |
| MR_1774416490_D29A0D22 | 504990 | 434 | -89.0 | 504990 | 743 | -96.9 | 504990 | 745 | -98.6 | 504990 | 955 |
| MR_1774416490_23F4F667 | 504990 | 434 | -87.9 | 504990 | 743 | -96.7 | 504990 | 745 | -97.1 | 504990 | 955 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 725: `da107c99-e24...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `da107c99-e245-42ea-9c54-03ed8ec6ea63` |
| Tag | **single-answer** |
| 정답 | **C1** |
| C1 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3237140_5 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[725] topology](images/train_0725.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3237140_5 **← 정답**
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3231737_4
- `C3`: Increase transmission power for 3237140_5
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3231737_4
- `C5`: Decrease A3 Offset threshold for 3237140_5
- `C6`: Insufficient data; more data is needed for judgment.
- `C7`: Lift the tilt angle of 3237140_5 by 4 degrees
- `C8`: Add neighbor relationship between 3274362_11 and 3231737_4
- `C9`: Increase transmission power for 3231737_4
- `C10`: Lift the tilt angle  of 3231737_4 by 4 degrees
- `C11`: Add neighbor relationship between 3237140_5 and 3231737_4
- `C12`: Decrease transmission power for 3231737_4
- `C13`: Decrease A3 Offset threshold for 3231737_4
- `C14`: Increase A3 Offset threshold for 3237140_5
- `C15`: Increase A3 Offset threshold for 3231737_4
- `C16`: Adjust the azimuth of 3231737_4 by 3 degrees
- `C17`: Press down the tilt angle of 3237140_5 by 4 degrees
- `C18`: Adjust the azimuth of 3237140_5 by 50 degrees
- `C19`: Decrease transmission power for 3237140_5
- `C20`: Press down the tilt angle  of 3231737_4 by 4 degrees
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3237140_5
- `C22`: Check test server and transmission issues

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.348 | MS1 | 121.4656677635 | 31.1446226706 | 685 | 504990 | -95.44 | 13.37 | 458.56 | 0.13 | 2.61 | 1579 |
| 2024-09-20 22:21:32.673 | MS1 | 121.4656619101 | 31.1446370130 | 824 | 504990 | -93.10 | 13.38 | 596.21 | 0.02 | 2.96 | 1597 |
| 2024-09-20 22:21:33.744 | MS1 | 121.4656740896 | 31.1446310496 | 128 | 504990 | -93.05 | 10.77 | 574.16 | 0.15 | 2.25 | 1582 |
| 2024-09-20 22:21:34.279 | MS1 | 121.4656722699 | 31.1446327967 | 844 | 152650 | -91.56 | 5.07 | 78.33 | 0.00 | 1.96 | 901 |
| 2024-09-20 22:21:35.907 | MS1 | 121.4656730863 | 31.1446256454 | 764 | 152650 | -96.62 | 5.17 | 86.99 | 0.17 | 1.89 | 955 |
| 2024-09-20 22:21:36.746 | MS1 | 121.4656736233 | 31.1446268583 | 87 | 152650 | -88.77 | 7.55 | 79.86 | 0.17 | 1.83 | 941 |
| 2024-09-20 22:21:37.951 | MS1 | 121.4656694204 | 31.1446358072 | 574 | 152650 | -92.31 | 5.38 | 74.10 | 0.11 | 1.92 | 996 |
| 2024-09-20 22:21:38.774 | MS1 | 121.4656680588 | 31.1446201121 | 844 | 152650 | -90.27 | 3.91 | 81.42 | 0.04 | 1.97 | 982 |
| 2024-09-20 22:21:39.694 | MS1 | 121.4656724563 | 31.1446220335 | 764 | 152650 | -89.98 | 3.20 | 102.50 | 0.03 | 1.59 | 903 |
| 2024-09-20 22:21:40.397 | MS1 | 121.4656676010 | 31.1446181100 | 87 | 152650 | -88.58 | 2.76 | 65.90 | 0.11 | 2.11 | 1594 |
| 2024-09-20 22:21:41.892 | MS1 | 121.4656649040 | 31.1446370135 | 574 | 152650 | -89.07 | 7.85 | 57.23 | 0.07 | 2.88 | 1573 |
| 2024-09-20 22:21:42.482 | MS1 | 121.4656693811 | 31.1446276104 | 844 | 152650 | -93.81 | 2.08 | 62.40 | 0.19 | 2.95 | 1593 |

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
| 3211202 | 3 | 121.4646287798 | 31.1513454588 | 354 | 8 | 12 | 28.6 | TDD | 233 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3211594 | 2 | 121.4659193507 | 31.1459169057 | 101 | 12 | 12 | 25.7 | TDD | 520 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3221307 | 7 | 121.4656736519 | 31.1517768419 | 122 | 15 | 6 | 0.7 | FDD | 962 | n1 | 152650 | 30M | 4T4R | 18 | 152650 |
| 3221789 | 13 | 121.4712278328 | 31.1557423650 | 137 | 8 | 11 | 29.6 | FDD | 574 | n1 | 152650 | 30M | 4T4R | 21 | 152650 |
| 3231737 | 4 | 121.4705354969 | 31.1451160261 | 266 | 1 | 4 | 21.4 | TDD | 107 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3237140 | 5 | 121.4699728131 | 31.1474100501 | 283 | 2 | 4 | 18.1 | TDD | 685 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3241747 | 10 | 121.4704137139 | 31.1516673652 | 35 | 0 | 8 | 17.1 | FDD | 978 | n1 | 152650 | 30M | 4T4R | 30 | 152650 |
| 3241927 | 9 | 121.4729347565 | 31.1485484618 | 254 | 8 | 12 | 11.2 | FDD | 239 | n1 | 152650 | 30M | 4T4R | 10 | 152650 |
| 3242276 | 6 | 121.4689975792 | 31.1548150204 | 343 | 13 | 5 | 25.3 | TDD | 824 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3243749 | 8 | 121.4651015981 | 31.1481886292 | 252 | 14 | 6 | 20.2 | FDD | 844 | n1 | 152650 | 30M | 4T4R | 21 | 152650 |
| 3259251 | 12 | 121.4745126264 | 31.1445440439 | 183 | 4 | 5 | 5.2 | FDD | 764 | n1 | 152650 | 30M | 4T4R | 25 | 152650 |
| 3269226 | 1 | 121.4723283774 | 31.1488413690 | 293 | 11 | 7 | 13.6 | TDD | 128 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3274362 | 11 | 121.4695226642 | 31.1489270526 | 326 | 1 | 2 | 19.2 | FDD | 87 | n1 | 152650 | 30M | 4T4R | 26 | 152650 |

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
| 2024-09-20 22:21:31.626 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.651 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.799 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.799 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.490 | NREventA2 | measId:1;ServCellPCI:994;Se... |
| 2024-09-20 22:21:35.619 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.838 | NREventA5 | measId:3;ServCellPCI:994;Se... |
| 2024-09-20 22:21:35.876 | NRHandoverAttempt | SourcePCI:994;SourceNR-ARFC... |
| 2024-09-20 22:21:35.911 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.926 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:36.049 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.049 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3269226 | 1 | 7.5890 | 5.1116 | -115.8384 | 6.3957 | 94.1473 | 0.0191 | 0.0160 |
| 2024_09_20 22:00 | 3211594 | 2 | 5.6108 | 17.1864 | -114.6430 | 7.0917 | 133.8522 | 0.0139 | 0.0184 |
| 2024_09_20 22:00 | 3211202 | 3 | 19.1983 | 17.6609 | -114.3578 | 12.2316 | 136.0501 | 0.0149 | 0.0186 |
| 2024_09_20 22:00 | 3231737 | 4 | 6.4505 | 15.2123 | -114.0242 | 15.4268 | 101.2360 | 0.0145 | 0.0189 |
| 2024_09_20 22:00 | 3237140 | 5 | 17.2176 | 5.6489 | -116.2819 | 8.2787 | 108.8715 | 0.0086 | 0.0091 |
| 2024_09_20 22:00 | 3242276 | 6 | 11.0803 | 16.1194 | -116.6938 | 15.4991 | 132.6128 | 0.0095 | 0.0062 |
| 2024_09_20 22:00 | 3221307 | 7 | 16.5616 | 5.8349 | -114.7529 | 4.2578 | 32.4396 | 0.0090 | 0.0187 |
| 2024_09_20 22:00 | 3243749 | 8 | 10.2086 | 14.6619 | -117.4201 | 4.8354 | 47.3684 | 0.0034 | 0.0193 |
| 2024_09_20 22:00 | 3241927 | 9 | 17.6237 | 7.7149 | -115.3295 | 3.4639 | 44.5757 | 0.0042 | 0.0129 |
| 2024_09_20 22:00 | 3241747 | 10 | 8.6499 | 19.8554 | -117.4090 | 3.0334 | 41.3614 | 0.0138 | 0.0045 |
| 2024_09_20 22:00 | 3274362 | 11 | 18.0162 | 15.0529 | -115.2788 | 3.9947 | 40.6587 | 0.0112 | 0.0152 |
| 2024_09_20 22:00 | 3259251 | 12 | 11.8178 | 15.0071 | -116.5829 | 4.6696 | 57.2901 | 0.0083 | 0.0156 |
| 2024_09_20 22:00 | 3221789 | 13 | 19.0353 | 6.1495 | -115.6521 | 4.1504 | 26.8452 | 0.0039 | 0.0191 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414599_9AE33B98 | 152650 | 844 | -93.5 | 152650 | 239 | -97.1 | 152650 | 962 | -98.6 | 152650 | 978 |
| MR_1774414599_7E819AC7 | 152650 | 844 | -92.9 | 152650 | 239 | -98.0 | 152650 | 962 | -100.0 | 152650 | 978 |
| MR_1774414599_23C12514 | 504990 | 128 | -91.5 | 504990 | 107 | -89.5 | 504990 | 233 | -98.1 | 504990 | 520 |
| MR_1774414599_9822BF24 | 504990 | 128 | -92.7 | 504990 | 107 | -88.0 | 504990 | 233 | -96.8 | 504990 | 520 |
| MR_1774414599_367DE1CB | 504990 | 128 | -94.6 | 504990 | 107 | -86.3 | 504990 | 233 | -95.4 | 504990 | 520 |
| MR_1774414599_6072A802 | 152650 | 844 | -91.8 | 152650 | 239 | -98.2 | 152650 | 962 | -98.2 | 152650 | 978 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 726: `21b623cd-70f...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `21b623cd-70fa-4e43-8ec1-678b5c907335` |
| Tag | **single-answer** |
| 정답 | **C9** |
| C9 의미 | Add neighbor relationship between 3242495_4 and 3262921_3 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[726] topology](images/train_0726.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3262921_3
- `C2`: Adjust the azimuth of 3262921_3 by 37 degrees
- `C3`: Decrease A3 Offset threshold for 3262921_3
- `C4`: Insufficient data; more data is needed for judgment.
- `C5`: Lift the tilt angle  of 3262921_3 by 4 degrees
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3262921_3
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3262921_3
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3242495_4
- `C9`: Add neighbor relationship between 3242495_4 and 3262921_3 **← 정답**
- `C10`: Decrease transmission power for 3262921_3
- `C11`: Check test server and transmission issues
- `C12`: Lift the tilt angle of 3242495_4 by 10 degrees
- `C13`: Increase transmission power for 3242495_4
- `C14`: Increase A3 Offset threshold for 3262921_3
- `C15`: Increase A3 Offset threshold for 3242495_4
- `C16`: Press down the tilt angle  of 3262921_3 by 4 degrees
- `C17`: Decrease A3 Offset threshold for 3242495_4
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3242495_4
- `C19`: Press down the tilt angle of 3242495_4 by 10 degrees
- `C20`: Decrease transmission power for 3242495_4
- `C21`: Add neighbor relationship between 3261692_1 and 3262921_3
- `C22`: Adjust the azimuth of 3242495_4 by 50 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.501 | MS1 | 121.4656623217 | 31.1446222311 | 247 | 504990 | -77.37 | 12.10 | 588.36 | 0.04 | 2.33 | 1598 |
| 2024-09-20 22:21:32.704 | MS1 | 121.4656737830 | 31.1446323599 | 247 | 504990 | -76.54 | 17.44 | 323.32 | 0.11 | 2.81 | 1574 |
| 2024-09-20 22:21:33.807 | MS1 | 121.4656584628 | 31.1446236425 | 247 | 504990 | -77.97 | 16.74 | 579.95 | 0.08 | 2.46 | 1566 |
| 2024-09-20 22:21:34.497 | MS1 | 121.4656744812 | 31.1446302950 | 247 | 504990 | -91.58 | -1.03 | 58.63 | 0.05 | 1.18 | 1579 |
| 2024-09-20 22:21:35.911 | MS1 | 121.4656692434 | 31.1446278259 | 247 | 504990 | -89.21 | -1.48 | 53.36 | 0.08 | 1.49 | 1569 |
| 2024-09-20 22:21:36.329 | MS1 | 121.4656594960 | 31.1446228536 | 247 | 504990 | -94.68 | -2.37 | 61.57 | 0.03 | 1.01 | 1576 |
| 2024-09-20 22:21:37.193 | MS1 | 121.4656592286 | 31.1446191028 | 247 | 504990 | -88.89 | -3.79 | 41.42 | 0.10 | 1.45 | 1565 |
| 2024-09-20 22:21:38.102 | MS1 | 121.4656583608 | 31.1446266323 | 247 | 504990 | -83.24 | 16.29 | 561.02 | 0.10 | 1.23 | 1578 |
| 2024-09-20 22:21:39.741 | MS1 | 121.4656638819 | 31.1446180590 | 247 | 504990 | -80.00 | 14.93 | 396.49 | 0.11 | 1.50 | 1560 |
| 2024-09-20 22:21:40.595 | MS1 | 121.4656694397 | 31.1446301150 | 247 | 504990 | -84.17 | 13.09 | 487.06 | 0.17 | 2.91 | 1590 |
| 2024-09-20 22:21:41.148 | MS1 | 121.4656777948 | 31.1446332541 | 247 | 504990 | -75.33 | 14.09 | 438.14 | 0.15 | 2.29 | 1598 |
| 2024-09-20 22:21:42.779 | MS1 | 121.4656614982 | 31.1446369142 | 247 | 504990 | -77.18 | 15.94 | 374.42 | 0.03 | 2.13 | 1580 |

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
| 3242495 | 4 | 121.4650780820 | 31.1533680840 | 54 | 11 | 10 | 32.9 | TDD | 247 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3261692 | 1 | 121.4701673897 | 31.1556339050 | 190 | 0 | 3 | 29.1 | TDD | 154 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3262206 | 2 | 121.4666991015 | 31.1523613226 | 98 | 11 | 10 | 47.2 | TDD | 842 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3262921 | 3 | 121.4735656840 | 31.1483905684 | 204 | 3 | 11 | 20.8 | TDD | 102 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:31.586 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.686 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.686 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.413 | NREventA3 | measId:2;ServCellPCI:544;Se... |
| 2024-09-20 22:21:36.413 | NREventA3 | measId:2;ServCellPCI:544;Se... |
| 2024-09-20 22:21:37.413 | NREventA3 | measId:2;ServCellPCI:544;Se... |
| 2024-09-20 22:21:39.913 | NRRRCReestablishAttempt | PCI:544 |
| 2024-09-20 22:21:39.930 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.943 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:40.077 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:40.077 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3261692 | 1 | 15.9103 | 5.4494 | -117.8552 | 10.7122 | 187.0287 | 0.0109 | 0.0037 |
| 2024_09_20 22:00 | 3262206 | 2 | 15.6106 | 14.9479 | -115.6942 | 6.9782 | 84.3168 | 0.0021 | 0.0172 |
| 2024_09_20 22:00 | 3262921 | 3 | 7.5971 | 11.1035 | -117.2922 | 8.0885 | 144.8577 | 0.0071 | 0.0028 |
| 2024_09_20 22:00 | 3242495 | 4 | 15.5013 | 8.6951 | -117.9436 | 9.9122 | 131.3144 | 0.0086 | 0.1810 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413490_B549D7B6 | 504990 | 102 | -86.9 | 504990 | 247 | -91.7 | 504990 | 154 | -89.4 | 504990 | 842 |
| MR_1774413490_8AF67BA5 | 504990 | 102 | -87.8 | 504990 | 247 | -90.5 | 504990 | 154 | -88.9 | 504990 | 842 |
| MR_1774413490_9DD651AF | 504990 | 102 | -86.8 | 504990 | 247 | -92.6 | 504990 | 154 | -90.0 | 504990 | 842 |
| MR_1774413490_5D9230AE | 504990 | 247 | -91.5 | 504990 | 102 | -85.9 | 504990 | 154 | -89.4 | 504990 | 842 |
| MR_1774413490_719BBD31 | 504990 | 247 | -93.5 | 504990 | 102 | -87.0 | 504990 | 154 | -89.1 | 504990 | 842 |
| MR_1774413490_9F7DD38C | 504990 | 102 | -85.4 | 504990 | 247 | -93.2 | 504990 | 154 | -90.6 | 504990 | 842 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 727: `14287718-131...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `14287718-1317-4bcb-b45f-74aaefacd32c` |
| Tag | **single-answer** |
| 정답 | **C3** |
| C3 의미 | Decrease A3 Offset threshold for 3259256_3 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[727] topology](images/train_0727.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3259256_3
- `C2`: Add neighbor relationship between 3259256_3 and 3237599_1
- `C3`: Decrease A3 Offset threshold for 3259256_3 **← 정답**
- `C4`: Insufficient data; more data is needed for judgment.
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3237599_1
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3259256_3
- `C7`: Decrease transmission power for 3259256_3
- `C8`: Decrease A3 Offset threshold for 3237599_1
- `C9`: Adjust the azimuth of 3259256_3 by 50 degrees
- `C10`: Increase transmission power for 3237599_1
- `C11`: Check test server and transmission issues
- `C12`: Increase transmission power for 3259256_3
- `C13`: Lift the tilt angle of 3259256_3 by 10 degrees
- `C14`: Lift the tilt angle  of 3237599_1 by 7 degrees
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3237599_1
- `C16`: Decrease transmission power for 3237599_1
- `C17`: Press down the tilt angle of 3259256_3 by 10 degrees
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3259256_3
- `C19`: Adjust the azimuth of 3237599_1 by 50 degrees
- `C20`: Increase A3 Offset threshold for 3237599_1
- `C21`: Add neighbor relationship between 3278627_2 and 3237599_1
- `C22`: Press down the tilt angle  of 3237599_1 by 7 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.185 | MS1 | 121.4656746988 | 31.1446290145 | 799 | 504990 | -80.11 | 16.41 | 325.47 | 0.08 | 2.50 | 1585 |
| 2024-09-20 22:21:32.572 | MS1 | 121.4656719210 | 31.1446226189 | 799 | 504990 | -80.36 | 15.98 | 438.02 | 0.03 | 2.22 | 1600 |
| 2024-09-20 22:21:33.453 | MS1 | 121.4656628694 | 31.1446259497 | 799 | 504990 | -79.32 | 13.46 | 405.69 | 0.05 | 2.52 | 1566 |
| 2024-09-20 22:21:34.224 | MS1 | 121.4656601123 | 31.1446278707 | 799 | 504990 | -86.48 | -0.43 | 45.31 | 0.16 | 1.38 | 1565 |
| 2024-09-20 22:21:35.760 | MS1 | 121.4656659344 | 31.1446281784 | 799 | 504990 | -91.84 | -2.53 | 42.27 | 0.11 | 1.00 | 1576 |
| 2024-09-20 22:21:36.791 | MS1 | 121.4656590779 | 31.1446203576 | 799 | 504990 | -83.54 | -1.93 | 70.10 | 0.09 | 1.19 | 1570 |
| 2024-09-20 22:21:37.639 | MS1 | 121.4656651397 | 31.1446290767 | 799 | 504990 | -91.73 | -2.99 | 66.82 | 0.06 | 1.35 | 1560 |
| 2024-09-20 22:21:38.511 | MS1 | 121.4656650490 | 31.1446231814 | 799 | 504990 | -88.92 | -2.46 | 44.52 | 0.00 | 1.02 | 1567 |
| 2024-09-20 22:21:39.608 | MS1 | 121.4656731077 | 31.1446193296 | 152 | 504990 | -82.45 | 17.69 | 177.07 | 0.12 | 1.42 | 1589 |
| 2024-09-20 22:21:40.850 | MS1 | 121.4656742085 | 31.1446345130 | 152 | 504990 | -77.71 | 16.86 | 525.77 | 0.07 | 2.89 | 1571 |
| 2024-09-20 22:21:41.973 | MS1 | 121.4656775074 | 31.1446234283 | 152 | 504990 | -84.83 | 12.23 | 577.87 | 0.13 | 2.06 | 1585 |
| 2024-09-20 22:21:42.578 | MS1 | 121.4656700579 | 31.1446231024 | 152 | 504990 | -77.93 | 15.28 | 465.02 | 0.14 | 2.08 | 1594 |

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
| 3237599 | 1 | 121.4699373392 | 31.1556409457 | 297 | 6 | 9 | 32.1 | TDD | 152 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3259256 | 3 | 121.4741247315 | 31.1444090530 | 42 | 11 | 10 | 33.5 | TDD | 799 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3264514 | 4 | 121.4741897380 | 31.1468286249 | 88 | 11 | 8 | 37.5 | TDD | 943 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3278627 | 2 | 121.4711744803 | 31.1527621193 | 52 | 7 | 9 | 17.0 | TDD | 728 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:31.099 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.244 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.244 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.883 | NREventA3 | measId:2;ServCellPCI:44;Ser... |
| 2024-09-20 22:21:38.123 | NRHandoverAttempt | SourcePCI:44;SourceNR-ARFCN... |
| 2024-09-20 22:21:38.169 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.182 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.312 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.312 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3237599 | 1 | 16.6885 | 6.3691 | -115.5117 | 16.1193 | 106.7527 | 0.0190 | 0.0065 |
| 2024_09_20 22:00 | 3278627 | 2 | 14.0760 | 6.1151 | -116.2271 | 10.5123 | 199.1155 | 0.0028 | 0.0136 |
| 2024_09_20 22:00 | 3259256 | 3 | 13.7204 | 18.0882 | -117.7773 | 19.6994 | 157.9853 | 0.0166 | 0.1314 |
| 2024_09_20 22:00 | 3264514 | 4 | 6.7926 | 13.5035 | -117.4518 | 15.2729 | 96.7341 | 0.0026 | 0.0078 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412668_BF62CDA1 | 504990 | 152 | -80.8 | 504990 | 799 | -87.1 | 504990 | 728 | -81.9 | 504990 | 943 |
| MR_1774412668_48F9E706 | 504990 | 799 | -85.0 | 504990 | 152 | -80.3 | 504990 | 728 | -82.7 | 504990 | 943 |
| MR_1774412668_A6679FA5 | 504990 | 799 | -88.4 | 504990 | 152 | -80.0 | 504990 | 728 | -83.1 | 504990 | 943 |
| MR_1774412668_AAACFE2D | 504990 | 152 | -79.7 | 504990 | 799 | -87.5 | 504990 | 728 | -83.0 | 504990 | 943 |
| MR_1774412668_E5119874 | 504990 | 799 | -84.8 | 504990 | 152 | -81.7 | 504990 | 728 | -82.0 | 504990 | 943 |
| MR_1774412668_312450CA | 504990 | 799 | -86.5 | 504990 | 152 | -82.8 | 504990 | 728 | -80.7 | 504990 | 943 |
| MR_1774412668_31459F9F | 504990 | 799 | -84.5 | 504990 | 152 | -79.2 | 504990 | 728 | -81.1 | 504990 | 943 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 728: `d58adad2-e1c...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `d58adad2-e1c0-4020-b66c-27b06fe079f2` |
| Tag | **single-answer** |
| 정답 | **C17** |
| C17 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[728] topology](images/train_0728.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment.
- `C2`: Increase A3 Offset threshold for 3253345_1
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3239418_3
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3239418_3
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3253345_1
- `C6`: Adjust the azimuth of 3239418_3 by 50 degrees
- `C7`: Adjust the azimuth of 3253345_1 by 50 degrees
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3253345_1
- `C9`: Press down the tilt angle of 3253345_1 by 7 degrees
- `C10`: Decrease transmission power for 3239418_3
- `C11`: Increase transmission power for 3239418_3
- `C12`: Press down the tilt angle  of 3239418_3 by 2 degrees
- `C13`: Lift the tilt angle of 3253345_1 by 7 degrees
- `C14`: Decrease A3 Offset threshold for 3253345_1
- `C15`: Lift the tilt angle  of 3239418_3 by 2 degrees
- `C16`: Decrease transmission power for 3253345_1
- `C17`: Check test server and transmission issues **← 정답**
- `C18`: Increase A3 Offset threshold for 3239418_3
- `C19`: Decrease A3 Offset threshold for 3239418_3
- `C20`: Add neighbor relationship between 3227629_4 and 3239418_3
- `C21`: Add neighbor relationship between 3253345_1 and 3239418_3
- `C22`: Increase transmission power for 3253345_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.861 | MS1 | 121.4656684929 | 31.1446269119 | 420 | 504990 | -91.76 | 17.38 | 475.95 | 0.14 | 2.27 | 1585 |
| 2024-09-20 22:21:32.713 | MS1 | 121.4656640711 | 31.1446227478 | 420 | 504990 | -85.62 | 12.99 | 310.54 | 0.16 | 2.03 | 1595 |
| 2024-09-20 22:21:33.995 | MS1 | 121.4656745389 | 31.1446241167 | 420 | 504990 | -89.47 | 13.48 | 591.50 | 0.17 | 2.37 | 1560 |
| 2024-09-20 22:21:34.941 | MS1 | 121.4656661960 | 31.1446274993 | 420 | 504990 | -86.46 | 16.36 | 56.12 | 0.10 | 2.06 | 328 |
| 2024-09-20 22:21:35.294 | MS1 | 121.4656597221 | 31.1446210113 | 420 | 504990 | -86.70 | 13.43 | 91.33 | 0.15 | 2.08 | 420 |
| 2024-09-20 22:21:36.537 | MS1 | 121.4656744858 | 31.1446370544 | 420 | 504990 | -90.67 | 17.17 | 69.40 | 0.10 | 2.08 | 400 |
| 2024-09-20 22:21:37.248 | MS1 | 121.4656775104 | 31.1446351391 | 420 | 504990 | -92.85 | 9.39 | 54.97 | 0.14 | 2.08 | 319 |
| 2024-09-20 22:21:38.332 | MS1 | 121.4656752569 | 31.1446374468 | 420 | 504990 | -91.18 | 11.32 | 95.52 | 0.04 | 2.51 | 342 |
| 2024-09-20 22:21:39.613 | MS1 | 121.4656658971 | 31.1446282087 | 420 | 504990 | -91.32 | 10.57 | 41.15 | 0.13 | 2.84 | 486 |
| 2024-09-20 22:21:40.711 | MS1 | 121.4656733111 | 31.1446349953 | 420 | 504990 | -89.54 | 9.53 | 557.26 | 0.05 | 2.59 | 1580 |
| 2024-09-20 22:21:41.573 | MS1 | 121.4656699649 | 31.1446197262 | 420 | 504990 | -93.37 | 11.01 | 594.27 | 0.09 | 2.68 | 1592 |
| 2024-09-20 22:21:42.342 | MS1 | 121.4656757965 | 31.1446211114 | 420 | 504990 | -92.10 | 7.30 | 509.38 | 0.16 | 2.68 | 1567 |

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
| 3226393 | 2 | 121.4642102971 | 31.1511486192 | 266 | 6 | 6 | 16.7 | TDD | 451 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3227629 | 4 | 121.4758561942 | 31.1514979936 | 194 | 10 | 11 | 35.3 | TDD | 94 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3239418 | 3 | 121.4653955666 | 31.1544147522 | 303 | 0 | 0 | 35.6 | TDD | 132 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3253345 | 1 | 121.4749812262 | 31.1498673906 | 60 | 6 | 9 | 20.2 | TDD | 420 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:31.577 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.593 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.695 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.695 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.439 | NREventA3 | measId:2;ServCellPCI:332;Se... |
| 2024-09-20 22:21:38.679 | NRHandoverAttempt | SourcePCI:332;SourceNR-ARFC... |
| 2024-09-20 22:21:38.728 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.742 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.888 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.888 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3253345 | 1 | 8.3420 | 9.2625 | -117.0595 | 12.2717 | 147.1374 | 0.0071 | 0.0147 |
| 2024_09_20 22:00 | 3226393 | 2 | 16.1603 | 8.8037 | -117.1865 | 11.1786 | 175.2298 | 0.0087 | 0.0063 |
| 2024_09_20 22:00 | 3239418 | 3 | 10.7482 | 19.5789 | -115.4287 | 10.2656 | 87.1120 | 0.0076 | 0.0012 |
| 2024_09_20 22:00 | 3227629 | 4 | 11.6411 | 9.6722 | -115.9971 | 17.7908 | 134.9786 | 0.0008 | 0.0003 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416785_75AEFE26 | 504990 | 420 | -86.1 | 504990 | 132 | -95.4 | 504990 | 94 | -99.5 | 504990 | 451 |
| MR_1774416785_EBFF9DE7 | 504990 | 420 | -86.3 | 504990 | 132 | -94.1 | 504990 | 94 | -99.1 | 504990 | 451 |
| MR_1774416785_63EBA929 | 504990 | 420 | -85.0 | 504990 | 132 | -95.0 | 504990 | 94 | -96.4 | 504990 | 451 |
| MR_1774416785_A3A49C6D | 504990 | 420 | -87.3 | 504990 | 132 | -95.4 | 504990 | 94 | -97.8 | 504990 | 451 |
| MR_1774416785_C5B111DA | 504990 | 420 | -86.1 | 504990 | 132 | -93.9 | 504990 | 94 | -98.3 | 504990 | 451 |
| MR_1774416785_2DBB3BA3 | 504990 | 420 | -86.4 | 504990 | 132 | -91.7 | 504990 | 94 | -97.6 | 504990 | 451 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 729: `3cf7aeec-9a1...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `3cf7aeec-9a11-461a-94a0-2839874b013f` |
| Tag | **single-answer** |
| 정답 | **C15** |
| C15 의미 | Decrease A3 Offset threshold for 3239038_3 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[729] topology](images/train_0729.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3239038_3
- `C2`: Add neighbor relationship between 3247917_2 and 3261570_1
- `C3`: Decrease A3 Offset threshold for 3261570_1
- `C4`: Lift the tilt angle of 3239038_3 by 10 degrees
- `C5`: Add neighbor relationship between 3239038_3 and 3261570_1
- `C6`: Increase transmission power for 3239038_3
- `C7`: Decrease transmission power for 3261570_1
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3261570_1
- `C9`: Increase A3 Offset threshold for 3261570_1
- `C10`: Insufficient data; more data is needed for judgment.
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3261570_1
- `C12`: Increase A3 Offset threshold for 3239038_3
- `C13`: Press down the tilt angle  of 3261570_1 by 3 degrees
- `C14`: Increase transmission power for 3261570_1
- `C15`: Decrease A3 Offset threshold for 3239038_3 **← 정답**
- `C16`: Adjust the azimuth of 3261570_1 by 50 degrees
- `C17`: Check test server and transmission issues
- `C18`: Lift the tilt angle  of 3261570_1 by 3 degrees
- `C19`: Press down the tilt angle of 3239038_3 by 10 degrees
- `C20`: Decrease transmission power for 3239038_3
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3239038_3
- `C22`: Adjust the azimuth of 3239038_3 by 13 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.429 | MS1 | 121.4656659699 | 31.1446195583 | 309 | 504990 | -79.46 | 13.79 | 323.52 | 0.06 | 2.27 | 1595 |
| 2024-09-20 22:21:32.442 | MS1 | 121.4656710477 | 31.1446344442 | 309 | 504990 | -84.47 | 16.25 | 385.11 | 0.17 | 2.28 | 1579 |
| 2024-09-20 22:21:33.508 | MS1 | 121.4656693699 | 31.1446301690 | 309 | 504990 | -81.63 | 12.90 | 414.82 | 0.00 | 2.19 | 1583 |
| 2024-09-20 22:21:34.771 | MS1 | 121.4656613166 | 31.1446295634 | 309 | 504990 | -90.11 | -1.69 | 71.89 | 0.16 | 1.42 | 1580 |
| 2024-09-20 22:21:35.888 | MS1 | 121.4656608991 | 31.1446364514 | 309 | 504990 | -85.93 | -0.88 | 31.72 | 0.01 | 1.45 | 1574 |
| 2024-09-20 22:21:36.788 | MS1 | 121.4656704028 | 31.1446231879 | 309 | 504990 | -90.48 | -0.24 | 58.48 | 0.16 | 1.36 | 1568 |
| 2024-09-20 22:21:37.216 | MS1 | 121.4656702688 | 31.1446292170 | 309 | 504990 | -86.18 | -1.98 | 54.86 | 0.05 | 1.29 | 1600 |
| 2024-09-20 22:21:38.936 | MS1 | 121.4656590719 | 31.1446238326 | 309 | 504990 | -88.09 | -3.16 | 45.55 | 0.04 | 1.44 | 1600 |
| 2024-09-20 22:21:39.565 | MS1 | 121.4656648229 | 31.1446285606 | 978 | 504990 | -81.19 | 16.58 | 249.56 | 0.08 | 1.39 | 1579 |
| 2024-09-20 22:21:40.851 | MS1 | 121.4656596636 | 31.1446296394 | 978 | 504990 | -82.24 | 13.68 | 475.74 | 0.19 | 2.81 | 1565 |
| 2024-09-20 22:21:41.872 | MS1 | 121.4656747146 | 31.1446315300 | 978 | 504990 | -79.94 | 15.94 | 314.06 | 0.09 | 2.51 | 1563 |
| 2024-09-20 22:21:42.334 | MS1 | 121.4656775781 | 31.1446357413 | 978 | 504990 | -78.47 | 13.74 | 347.61 | 0.03 | 2.83 | 1593 |

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
| 3230249 | 4 | 121.4737195479 | 31.1443269565 | 338 | 2 | 3 | 27.4 | TDD | 382 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3239038 | 3 | 121.4675177244 | 31.1445329515 | 261 | 12 | 4 | 49.3 | TDD | 309 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3247917 | 2 | 121.4759675972 | 31.1530730359 | 32 | 0 | 8 | 26.2 | TDD | 859 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3261570 | 1 | 121.4709262612 | 31.1508672982 | 270 | 0 | 9 | 42.8 | TDD | 978 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:30.777 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:30.899 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.899 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.635 | NREventA3 | measId:2;ServCellPCI:269;Se... |
| 2024-09-20 22:21:37.875 | NRHandoverAttempt | SourcePCI:269;SourceNR-ARFC... |
| 2024-09-20 22:21:37.923 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.935 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.083 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.083 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3261570 | 1 | 15.5862 | 12.0030 | -114.0653 | 19.9891 | 164.1427 | 0.0050 | 0.0033 |
| 2024_09_20 22:00 | 3247917 | 2 | 8.5388 | 15.7389 | -114.6444 | 8.8956 | 124.3204 | 0.0092 | 0.0013 |
| 2024_09_20 22:00 | 3239038 | 3 | 7.2032 | 19.1620 | -116.8444 | 15.2513 | 96.6928 | 0.0195 | 0.1483 |
| 2024_09_20 22:00 | 3230249 | 4 | 18.4654 | 14.3727 | -114.2018 | 13.3854 | 89.3524 | 0.0051 | 0.0168 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412015_77A598E9 | 504990 | 309 | -88.5 | 504990 | 978 | -86.7 | 504990 | 859 | -86.3 | 504990 | 382 |
| MR_1774412015_499B0489 | 504990 | 309 | -88.7 | 504990 | 978 | -85.4 | 504990 | 859 | -83.5 | 504990 | 382 |
| MR_1774412015_89EA5686 | 504990 | 978 | -84.1 | 504990 | 309 | -89.1 | 504990 | 859 | -85.7 | 504990 | 382 |
| MR_1774412015_DFB45822 | 504990 | 309 | -88.4 | 504990 | 978 | -83.2 | 504990 | 859 | -84.4 | 504990 | 382 |
| MR_1774412015_0069971F | 504990 | 978 | -83.0 | 504990 | 309 | -88.8 | 504990 | 859 | -86.9 | 504990 | 382 |

> *... 2개 열 생략 (전체 14열)*

---
