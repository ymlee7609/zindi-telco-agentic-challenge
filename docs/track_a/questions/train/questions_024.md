# Track A 문제 분석 — train[230]~train[239]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[230] ~ train[239] (10개)

## 목차

1. [문제 230: `136cdf81-9f6...`](#230) — single-answer, 정답: C20
2. [문제 231: `b900cda9-d68...`](#231) — single-answer, 정답: C9
3. [문제 232: `186330ab-ab4...`](#232) — single-answer, 정답: C9
4. [문제 233: `7c9453b6-35f...`](#233) — single-answer, 정답: C18
5. [문제 234: `15342671-786...`](#234) — single-answer, 정답: C3
6. [문제 235: `b50c251a-048...`](#235) — single-answer, 정답: C1
7. [문제 236: `2734d324-376...`](#236) — multiple-answer, 정답: C14|C16
8. [문제 237: `ace16cfa-7bb...`](#237) — single-answer, 정답: C7
9. [문제 238: `67499a69-dd1...`](#238) — single-answer, 정답: C21
10. [문제 239: `9e14afa9-2c4...`](#239) — single-answer, 정답: C12

---

### 문제 230: `136cdf81-9f6...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `136cdf81-9f6a-455d-965b-4fa30d82e303` |
| Tag | **single-answer** |
| 정답 | **C20** |
| C20 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[230] topology](images/train_0230.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3250808_3
- `C2`: Lift the tilt angle of 3258014_4 by 10 degrees
- `C3`: Decrease A3 Offset threshold for 3258014_4
- `C4`: Decrease transmission power for 3250808_3
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3258014_4
- `C6`: Increase A3 Offset threshold for 3258014_4
- `C7`: Decrease transmission power for 3258014_4
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3250808_3
- `C9`: Adjust the azimuth of 3250808_3 by 50 degrees
- `C10`: Add neighbor relationship between 3253982_2 and 3250808_3
- `C11`: Decrease A3 Offset threshold for 3250808_3
- `C12`: Increase transmission power for 3250808_3
- `C13`: Check test server and transmission issues
- `C14`: Adjust the azimuth of 3258014_4 by 45 degrees
- `C15`: Increase transmission power for 3258014_4
- `C16`: Lift the tilt angle  of 3250808_3 by 9 degrees
- `C17`: Add neighbor relationship between 3258014_4 and 3250808_3
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3258014_4
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3250808_3
- `C20`: Insufficient data; more data is needed for judgment. **← 정답**
- `C21`: Press down the tilt angle  of 3250808_3 by 9 degrees
- `C22`: Press down the tilt angle of 3258014_4 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.760 | MS1 | 121.4656723492 | 31.1446333850 | 934 | 504990 | -88.70 | 12.44 | 338.26 | 0.01 | 2.04 | 1563 |
| 2024-09-20 22:21:32.468 | MS1 | 121.4656671381 | 31.1446186899 | 934 | 504990 | -88.21 | 13.59 | 406.18 | 0.01 | 2.14 | 1572 |
| 2024-09-20 22:21:33.105 | MS1 | 121.4656665453 | 31.1446276217 | 934 | 504990 | -86.24 | 12.93 | 337.71 | 0.04 | 2.93 | 1587 |
| 2024-09-20 22:21:34.424 | MS1 | 121.4656704916 | 31.1446337849 | 934 | 504990 | -90.01 | 13.90 | 75.80 | 0.03 | 2.67 | 1569 |
| 2024-09-20 22:21:35.170 | MS1 | 121.4656730327 | 31.1446273480 | 934 | 504990 | -85.19 | 15.07 | 55.49 | 0.03 | 2.90 | 1578 |
| 2024-09-20 22:21:36.708 | MS1 | 121.4656596691 | 31.1446215238 | 934 | 504990 | -88.86 | 12.46 | 70.61 | 0.14 | 2.68 | 1585 |
| 2024-09-20 22:21:37.491 | MS1 | 121.4656670896 | 31.1446184357 | 934 | 504990 | -89.84 | 11.21 | 59.87 | 0.02 | 2.92 | 1583 |
| 2024-09-20 22:21:38.890 | MS1 | 121.4656721393 | 31.1446352155 | 934 | 504990 | -90.79 | 10.14 | 55.37 | 0.06 | 2.16 | 1561 |
| 2024-09-20 22:21:39.478 | MS1 | 121.4656743650 | 31.1446324677 | 934 | 504990 | -89.91 | 8.35 | 65.28 | 0.04 | 2.92 | 1592 |
| 2024-09-20 22:21:40.254 | MS1 | 121.4656709758 | 31.1446302169 | 934 | 504990 | -92.72 | 12.89 | 461.30 | 0.07 | 2.88 | 1572 |
| 2024-09-20 22:21:41.814 | MS1 | 121.4656610912 | 31.1446225901 | 934 | 504990 | -92.39 | 12.61 | 556.09 | 0.19 | 2.14 | 1569 |
| 2024-09-20 22:21:42.747 | MS1 | 121.4656770938 | 31.1446287403 | 934 | 504990 | -90.57 | 9.53 | 394.57 | 0.10 | 2.30 | 1592 |

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
| 3224917 | 1 | 121.4686613919 | 31.1501666285 | 330 | 4 | 2 | 30.5 | TDD | 297 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3250808 | 3 | 121.4759745604 | 31.1457765730 | 92 | 8 | 6 | 24.5 | TDD | 124 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3253982 | 2 | 121.4682477113 | 31.1540081253 | 302 | 9 | 6 | 22.2 | TDD | 579 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3258014 | 4 | 121.4657839029 | 31.1476028443 | 137 | 13 | 10 | 37.7 | TDD | 934 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |

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
| 2024-09-20 22:21:31.121 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.139 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.263 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.263 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.942 | NREventA3 | measId:2;ServCellPCI:384;Se... |
| 2024-09-20 22:21:38.182 | NRHandoverAttempt | SourcePCI:384;SourceNR-ARFC... |
| 2024-09-20 22:21:38.227 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.239 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.365 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.365 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3224917 | 1 | 80.0624 | 91.0830 | -117.3040 | 17.9659 | 167.8915 | 0.0130 | 0.0019 |
| 2024_09_19 22:00 | 3253982 | 2 | 82.2326 | 75.7651 | -116.6169 | 12.2634 | 153.5397 | 0.0118 | 0.0170 |
| 2024_09_19 22:00 | 3250808 | 3 | 83.8307 | 78.7737 | -116.6368 | 9.8311 | 108.0363 | 0.0165 | 0.0167 |
| 2024_09_19 22:00 | 3258014 | 4 | 85.8249 | 80.1497 | -117.3622 | 7.9545 | 89.3703 | 0.0053 | 0.0079 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416619_C0646302 | 504990 | 934 | -89.6 | 504990 | 124 | -95.6 | 504990 | 579 | -103.3 | 504990 | 297 |
| MR_1774416619_5C08734E | 504990 | 934 | -90.5 | 504990 | 124 | -93.7 | 504990 | 579 | -103.8 | 504990 | 297 |
| MR_1774416619_B23A6512 | 504990 | 934 | -90.0 | 504990 | 124 | -95.2 | 504990 | 579 | -100.1 | 504990 | 297 |
| MR_1774416619_8F68F3CF | 504990 | 934 | -88.3 | 504990 | 124 | -96.4 | 504990 | 579 | -102.2 | 504990 | 297 |
| MR_1774416619_8BF03F65 | 504990 | 934 | -88.6 | 504990 | 124 | -95.8 | 504990 | 579 | -101.6 | 504990 | 297 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 231: `b900cda9-d68...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `b900cda9-d685-42d3-bc77-03e704a36403` |
| Tag | **single-answer** |
| 정답 | **C9** |
| C9 의미 | Decrease A3 Offset threshold for 3253371_3 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[231] topology](images/train_0231.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3253371_3 and 3254528_4
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3253371_3
- `C3`: Increase A3 Offset threshold for 3254528_4
- `C4`: Lift the tilt angle of 3253371_3 by 10 degrees
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3254528_4
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3254528_4
- `C7`: Adjust the azimuth of 3254528_4 by 50 degrees
- `C8`: Increase A3 Offset threshold for 3253371_3
- `C9`: Decrease A3 Offset threshold for 3253371_3 **← 정답**
- `C10`: Press down the tilt angle of 3253371_3 by 10 degrees
- `C11`: Increase transmission power for 3254528_4
- `C12`: Adjust the azimuth of 3253371_3 by 50 degrees
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3253371_3
- `C14`: Lift the tilt angle  of 3254528_4 by 6 degrees
- `C15`: Decrease transmission power for 3254528_4
- `C16`: Increase transmission power for 3253371_3
- `C17`: Decrease transmission power for 3253371_3
- `C18`: Insufficient data; more data is needed for judgment.
- `C19`: Decrease A3 Offset threshold for 3254528_4
- `C20`: Press down the tilt angle  of 3254528_4 by 6 degrees
- `C21`: Add neighbor relationship between 3246732_2 and 3254528_4
- `C22`: Check test server and transmission issues

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.345 | MS1 | 121.4656611514 | 31.1446329450 | 349 | 504990 | -76.49 | 12.30 | 360.90 | 0.11 | 2.29 | 1586 |
| 2024-09-20 22:21:32.903 | MS1 | 121.4656685002 | 31.1446302427 | 349 | 504990 | -83.41 | 15.12 | 385.51 | 0.19 | 2.90 | 1571 |
| 2024-09-20 22:21:33.162 | MS1 | 121.4656646767 | 31.1446284306 | 349 | 504990 | -79.91 | 14.48 | 444.86 | 0.12 | 2.77 | 1572 |
| 2024-09-20 22:21:34.249 | MS1 | 121.4656632594 | 31.1446274304 | 349 | 504990 | -88.59 | -2.72 | 60.94 | 0.13 | 1.30 | 1593 |
| 2024-09-20 22:21:35.258 | MS1 | 121.4656696030 | 31.1446255464 | 349 | 504990 | -84.54 | -1.20 | 58.85 | 0.01 | 1.50 | 1572 |
| 2024-09-20 22:21:36.356 | MS1 | 121.4656714636 | 31.1446269804 | 349 | 504990 | -88.57 | -1.30 | 64.90 | 0.18 | 1.17 | 1563 |
| 2024-09-20 22:21:37.675 | MS1 | 121.4656595677 | 31.1446268498 | 349 | 504990 | -90.73 | -2.24 | 72.89 | 0.14 | 1.24 | 1570 |
| 2024-09-20 22:21:38.475 | MS1 | 121.4656774769 | 31.1446307113 | 349 | 504990 | -85.39 | -2.43 | 61.52 | 0.09 | 1.03 | 1595 |
| 2024-09-20 22:21:39.241 | MS1 | 121.4656620985 | 31.1446327090 | 174 | 504990 | -82.47 | 14.95 | 285.47 | 0.01 | 1.06 | 1597 |
| 2024-09-20 22:21:40.404 | MS1 | 121.4656595156 | 31.1446188063 | 174 | 504990 | -75.60 | 17.44 | 305.98 | 0.14 | 2.73 | 1572 |
| 2024-09-20 22:21:41.346 | MS1 | 121.4656608717 | 31.1446290101 | 174 | 504990 | -80.33 | 14.93 | 398.58 | 0.11 | 2.03 | 1570 |
| 2024-09-20 22:21:42.300 | MS1 | 121.4656715211 | 31.1446323906 | 174 | 504990 | -82.33 | 14.71 | 569.12 | 0.04 | 2.43 | 1587 |

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
| 3246732 | 2 | 121.4671396333 | 31.1549140230 | 355 | 12 | 7 | 49.7 | TDD | 274 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3248515 | 1 | 121.4705744085 | 31.1505229630 | 243 | 10 | 6 | 25.8 | TDD | 176 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3253371 | 3 | 121.4663497894 | 31.1522756195 | 331 | 8 | 10 | 25.9 | TDD | 349 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3254528 | 4 | 121.4648150024 | 31.1508964049 | 322 | 2 | 6 | 44.0 | TDD | 174 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |

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
| 2024-09-20 22:21:31.543 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.563 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.668 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.668 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.357 | NREventA3 | measId:2;ServCellPCI:1006;S... |
| 2024-09-20 22:21:38.597 | NRHandoverAttempt | SourcePCI:1006;SourceNR-ARF... |
| 2024-09-20 22:21:38.642 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.653 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.774 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.774 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3248515 | 1 | 19.8450 | 13.5769 | -114.9891 | 10.2224 | 97.4217 | 0.0085 | 0.0197 |
| 2024_09_20 22:00 | 3246732 | 2 | 17.2303 | 13.9392 | -114.7836 | 8.7501 | 129.9945 | 0.0163 | 0.0128 |
| 2024_09_20 22:00 | 3253371 | 3 | 18.8121 | 16.3003 | -114.2015 | 7.0970 | 101.8489 | 0.0055 | 0.1716 |
| 2024_09_20 22:00 | 3254528 | 4 | 11.5546 | 12.1973 | -116.7264 | 7.2058 | 119.3459 | 0.0043 | 0.0094 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415366_FF941A36 | 504990 | 349 | -86.9 | 504990 | 174 | -82.1 | 504990 | 274 | -81.7 | 504990 | 176 |
| MR_1774415366_45DFA031 | 504990 | 349 | -87.0 | 504990 | 174 | -82.5 | 504990 | 274 | -82.0 | 504990 | 176 |
| MR_1774415366_6302D912 | 504990 | 174 | -81.9 | 504990 | 349 | -86.7 | 504990 | 274 | -82.5 | 504990 | 176 |
| MR_1774415366_451E30AC | 504990 | 349 | -87.0 | 504990 | 174 | -81.5 | 504990 | 274 | -83.3 | 504990 | 176 |
| MR_1774415366_16BC1DC7 | 504990 | 349 | -90.2 | 504990 | 174 | -81.5 | 504990 | 274 | -83.4 | 504990 | 176 |
| MR_1774415366_7AF4A16C | 504990 | 349 | -87.2 | 504990 | 174 | -83.2 | 504990 | 274 | -82.6 | 504990 | 176 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 232: `186330ab-ab4...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `186330ab-ab47-44c1-acc8-a4564d5a1b03` |
| Tag | **single-answer** |
| 정답 | **C9** |
| C9 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[232] topology](images/train_0232.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3274767_3
- `C2`: Increase A3 Offset threshold for 3274767_3
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3235585_2
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3274767_3
- `C5`: Adjust the azimuth of 3235585_2 by 50 degrees
- `C6`: Decrease A3 Offset threshold for 3235585_2
- `C7`: Lift the tilt angle of 3274767_3 by 1 degrees
- `C8`: Adjust the azimuth of 3274767_3 by 50 degrees
- `C9`: Insufficient data; more data is needed for judgment. **← 정답**
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3235585_2
- `C11`: Lift the tilt angle  of 3235585_2 by 8 degrees
- `C12`: Increase transmission power for 3274767_3
- `C13`: Add neighbor relationship between 3274767_3 and 3235585_2
- `C14`: Decrease transmission power for 3274767_3
- `C15`: Increase A3 Offset threshold for 3235585_2
- `C16`: Press down the tilt angle of 3274767_3 by 1 degrees
- `C17`: Increase transmission power for 3235585_2
- `C18`: Check test server and transmission issues
- `C19`: Add neighbor relationship between 3235752_1 and 3235585_2
- `C20`: Press down the tilt angle  of 3235585_2 by 8 degrees
- `C21`: Decrease transmission power for 3235585_2
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3274767_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.701 | MS1 | 121.4656767305 | 31.1446207709 | 556 | 504990 | -90.82 | 16.96 | 457.35 | 0.03 | 2.80 | 1584 |
| 2024-09-20 22:21:32.941 | MS1 | 121.4656637088 | 31.1446299629 | 556 | 504990 | -90.28 | 17.88 | 579.80 | 0.04 | 2.39 | 1589 |
| 2024-09-20 22:21:33.472 | MS1 | 121.4656771622 | 31.1446198832 | 556 | 504990 | -85.23 | 16.03 | 586.70 | 0.14 | 2.67 | 1582 |
| 2024-09-20 22:21:34.388 | MS1 | 121.4656715005 | 31.1446307066 | 556 | 504990 | -90.14 | 17.02 | 63.93 | 0.02 | 2.93 | 1596 |
| 2024-09-20 22:21:35.370 | MS1 | 121.4656586514 | 31.1446271067 | 556 | 504990 | -87.50 | 17.43 | 78.36 | 0.04 | 2.40 | 1584 |
| 2024-09-20 22:21:36.106 | MS1 | 121.4656711506 | 31.1446358530 | 556 | 504990 | -88.84 | 17.78 | 65.77 | 0.01 | 2.40 | 1566 |
| 2024-09-20 22:21:37.905 | MS1 | 121.4656596058 | 31.1446319068 | 556 | 504990 | -91.82 | 11.11 | 100.69 | 0.17 | 2.75 | 1575 |
| 2024-09-20 22:21:38.423 | MS1 | 121.4656699333 | 31.1446214959 | 556 | 504990 | -90.73 | 12.06 | 73.76 | 0.03 | 2.31 | 1586 |
| 2024-09-20 22:21:39.144 | MS1 | 121.4656643163 | 31.1446254037 | 556 | 504990 | -90.36 | 10.45 | 72.36 | 0.06 | 2.51 | 1569 |
| 2024-09-20 22:21:40.710 | MS1 | 121.4656665394 | 31.1446369541 | 556 | 504990 | -93.75 | 10.18 | 374.06 | 0.03 | 2.41 | 1581 |
| 2024-09-20 22:21:41.719 | MS1 | 121.4656645056 | 31.1446245401 | 556 | 504990 | -91.28 | 11.49 | 410.76 | 0.10 | 2.69 | 1562 |
| 2024-09-20 22:21:42.183 | MS1 | 121.4656679671 | 31.1446224343 | 556 | 504990 | -90.06 | 12.70 | 324.81 | 0.15 | 2.14 | 1599 |

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
| 3213735 | 4 | 121.4753613381 | 31.1545290687 | 156 | 15 | 11 | 34.0 | TDD | 672 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3235585 | 2 | 121.4678734493 | 31.1548872948 | 346 | 6 | 5 | 45.4 | TDD | 218 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3235752 | 1 | 121.4657238659 | 31.1475306552 | 339 | 12 | 12 | 28.4 | TDD | 392 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3274767 | 3 | 121.4759358580 | 31.1536132828 | 302 | 0 | 6 | 19.2 | TDD | 556 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |

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
| 2024-09-20 22:21:31.045 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.070 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.200 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.200 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.905 | NREventA3 | measId:2;ServCellPCI:368;Se... |
| 2024-09-20 22:21:38.145 | NRHandoverAttempt | SourcePCI:368;SourceNR-ARFC... |
| 2024-09-20 22:21:38.179 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.194 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.338 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.338 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3235752 | 1 | 82.5526 | 78.7211 | -114.0266 | 13.1564 | 106.4756 | 0.0003 | 0.0051 |
| 2024_09_19 22:00 | 3235585 | 2 | 89.8305 | 85.5974 | -115.3850 | 16.0626 | 83.1402 | 0.0164 | 0.0025 |
| 2024_09_19 22:00 | 3274767 | 3 | 76.8289 | 90.2019 | -114.7135 | 5.5797 | 137.9837 | 0.0113 | 0.0036 |
| 2024_09_19 22:00 | 3213735 | 4 | 86.7136 | 84.1365 | -117.0207 | 17.0837 | 184.5424 | 0.0025 | 0.0004 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414084_8BF2EA4E | 504990 | 556 | -88.5 | 504990 | 218 | -95.4 | 504990 | 392 | -101.6 | 504990 | 672 |
| MR_1774414084_BEA2AF4F | 504990 | 556 | -91.3 | 504990 | 218 | -95.2 | 504990 | 392 | -104.3 | 504990 | 672 |
| MR_1774414084_6478A16B | 504990 | 556 | -89.7 | 504990 | 218 | -96.5 | 504990 | 392 | -102.9 | 504990 | 672 |
| MR_1774414084_545E11B8 | 504990 | 556 | -88.9 | 504990 | 218 | -94.8 | 504990 | 392 | -103.9 | 504990 | 672 |
| MR_1774414084_8D88F773 | 504990 | 556 | -89.0 | 504990 | 218 | -97.9 | 504990 | 392 | -102.8 | 504990 | 672 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 233: `7c9453b6-35f...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `7c9453b6-35fc-4fc7-95ed-1bf09d629849` |
| Tag | **single-answer** |
| 정답 | **C18** |
| C18 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[233] topology](images/train_0233.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3250114_1
- `C2`: Lift the tilt angle  of 3250114_1 by 1 degrees
- `C3`: Increase transmission power for 3250114_1
- `C4`: Check test server and transmission issues
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3266135_4
- `C6`: Increase A3 Offset threshold for 3266135_4
- `C7`: Decrease A3 Offset threshold for 3250114_1
- `C8`: Increase transmission power for 3266135_4
- `C9`: Decrease A3 Offset threshold for 3266135_4
- `C10`: Decrease transmission power for 3266135_4
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3266135_4
- `C12`: Press down the tilt angle  of 3250114_1 by 1 degrees
- `C13`: Increase A3 Offset threshold for 3250114_1
- `C14`: Adjust the azimuth of 3266135_4 by 50 degrees
- `C15`: Lift the tilt angle of 3266135_4 by 8 degrees
- `C16`: Press down the tilt angle of 3266135_4 by 8 degrees
- `C17`: Adjust the azimuth of 3250114_1 by 50 degrees
- `C18`: Insufficient data; more data is needed for judgment. **← 정답**
- `C19`: Add neighbor relationship between 3266135_4 and 3250114_1
- `C20`: Add neighbor relationship between 3264753_3 and 3250114_1
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3250114_1
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3250114_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.967 | MS1 | 121.4656732707 | 31.1446260074 | 174 | 504990 | -89.77 | 15.65 | 474.84 | 0.13 | 2.69 | 1594 |
| 2024-09-20 22:21:32.955 | MS1 | 121.4656730666 | 31.1446319945 | 174 | 504990 | -89.55 | 13.24 | 474.56 | 0.12 | 2.57 | 1595 |
| 2024-09-20 22:21:33.987 | MS1 | 121.4656640964 | 31.1446344299 | 174 | 504990 | -89.96 | 13.49 | 603.00 | 0.13 | 2.16 | 1590 |
| 2024-09-20 22:21:34.560 | MS1 | 121.4656768927 | 31.1446311502 | 174 | 504990 | -88.43 | 14.01 | 95.99 | 0.15 | 2.30 | 1599 |
| 2024-09-20 22:21:35.935 | MS1 | 121.4656675226 | 31.1446291310 | 174 | 504990 | -86.22 | 17.69 | 54.67 | 0.11 | 2.84 | 1566 |
| 2024-09-20 22:21:36.472 | MS1 | 121.4656633911 | 31.1446305107 | 174 | 504990 | -89.63 | 17.90 | 108.44 | 0.06 | 2.12 | 1571 |
| 2024-09-20 22:21:37.565 | MS1 | 121.4656705018 | 31.1446241940 | 174 | 504990 | -90.19 | 11.61 | 88.77 | 0.08 | 2.03 | 1592 |
| 2024-09-20 22:21:38.185 | MS1 | 121.4656779428 | 31.1446303649 | 174 | 504990 | -92.63 | 7.28 | 77.19 | 0.16 | 2.02 | 1561 |
| 2024-09-20 22:21:39.334 | MS1 | 121.4656768707 | 31.1446295905 | 174 | 504990 | -93.65 | 11.85 | 70.55 | 0.19 | 2.51 | 1572 |
| 2024-09-20 22:21:40.443 | MS1 | 121.4656626855 | 31.1446202234 | 174 | 504990 | -92.63 | 10.78 | 566.04 | 0.04 | 2.95 | 1577 |
| 2024-09-20 22:21:41.611 | MS1 | 121.4656662665 | 31.1446185356 | 174 | 504990 | -90.05 | 10.36 | 368.89 | 0.12 | 2.99 | 1571 |
| 2024-09-20 22:21:42.960 | MS1 | 121.4656666510 | 31.1446249916 | 174 | 504990 | -89.10 | 8.50 | 404.31 | 0.04 | 2.11 | 1572 |

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
| 3250114 | 1 | 121.4679948420 | 31.1559605955 | 346 | 0 | 2 | 29.9 | TDD | 728 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3264753 | 3 | 121.4710338483 | 31.1548003850 | 317 | 8 | 5 | 47.8 | TDD | 325 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3266135 | 4 | 121.4702551494 | 31.1456476982 | 117 | 3 | 5 | 43.2 | TDD | 174 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3275909 | 2 | 121.4719488399 | 31.1486900605 | 213 | 4 | 9 | 25.1 | TDD | 995 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:31.396 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.421 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.529 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.529 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.199 | NREventA3 | measId:2;ServCellPCI:470;Se... |
| 2024-09-20 22:21:38.439 | NRHandoverAttempt | SourcePCI:470;SourceNR-ARFC... |
| 2024-09-20 22:21:38.479 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.494 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.638 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.638 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3250114 | 1 | 75.0126 | 81.1500 | -115.6993 | 11.1589 | 172.7817 | 0.0036 | 0.0035 |
| 2024_09_19 22:00 | 3275909 | 2 | 94.1252 | 78.6202 | -115.7165 | 6.1478 | 99.6733 | 0.0037 | 0.0117 |
| 2024_09_19 22:00 | 3264753 | 3 | 88.6688 | 94.2725 | -115.7494 | 18.6711 | 109.3753 | 0.0150 | 0.0046 |
| 2024_09_19 22:00 | 3266135 | 4 | 91.3219 | 78.7004 | -117.8275 | 8.5735 | 109.6412 | 0.0069 | 0.0090 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414396_FE5ADF47 | 504990 | 174 | -87.1 | 504990 | 728 | -93.5 | 504990 | 325 | -104.6 | 504990 | 995 |
| MR_1774414396_437929E2 | 504990 | 174 | -89.0 | 504990 | 728 | -91.9 | 504990 | 325 | -101.8 | 504990 | 995 |
| MR_1774414396_ACBCF9DA | 504990 | 174 | -88.5 | 504990 | 728 | -92.1 | 504990 | 325 | -101.0 | 504990 | 995 |
| MR_1774414396_381A50A4 | 504990 | 174 | -89.4 | 504990 | 728 | -93.5 | 504990 | 325 | -103.8 | 504990 | 995 |
| MR_1774414396_622F6B6A | 504990 | 174 | -87.4 | 504990 | 728 | -90.4 | 504990 | 325 | -100.8 | 504990 | 995 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 234: `15342671-786...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `15342671-786a-4adb-b53f-bfd062fc3d71` |
| Tag | **single-answer** |
| 정답 | **C3** |
| C3 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3231848_2 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[234] topology](images/train_0234.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3231848_2 by 5 degrees
- `C2`: Increase A3 Offset threshold for 3231848_2
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3231848_2 **← 정답**
- `C4`: Add neighbor relationship between 3232657_3 and 3268378_1
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3268378_1
- `C6`: Increase A3 Offset threshold for 3268378_1
- `C7`: Add neighbor relationship between 3231848_2 and 3268378_1
- `C8`: Decrease A3 Offset threshold for 3231848_2
- `C9`: Decrease transmission power for 3231848_2
- `C10`: Decrease transmission power for 3268378_1
- `C11`: Increase transmission power for 3268378_1
- `C12`: Check test server and transmission issues
- `C13`: Adjust the azimuth of 3268378_1 by 50 degrees
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3231848_2
- `C15`: Increase transmission power for 3231848_2
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3268378_1
- `C17`: Lift the tilt angle  of 3268378_1 by 3 degrees
- `C18`: Insufficient data; more data is needed for judgment.
- `C19`: Lift the tilt angle of 3231848_2 by 5 degrees
- `C20`: Press down the tilt angle  of 3268378_1 by 3 degrees
- `C21`: Adjust the azimuth of 3231848_2 by 44 degrees
- `C22`: Decrease A3 Offset threshold for 3268378_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.736 | MS1 | 121.4656665014 | 31.1446202681 | 523 | 504990 | -91.54 | 15.82 | 317.29 | 0.19 | 2.33 | 1600 |
| 2024-09-20 22:21:32.105 | MS1 | 121.4656642567 | 31.1446241393 | 523 | 504990 | -85.78 | 12.61 | 481.78 | 0.13 | 2.47 | 1567 |
| 2024-09-20 22:21:33.357 | MS1 | 121.4656619520 | 31.1446314973 | 523 | 504990 | -88.21 | 17.73 | 571.32 | 0.02 | 2.82 | 1575 |
| 2024-09-20 22:21:34.708 | MS1 | 121.4656691373 | 31.1446300668 | 523 | 504990 | -90.15 | 13.20 | 99.24 | 0.61 | 2.31 | 642 |
| 2024-09-20 22:21:35.792 | MS1 | 121.4656649919 | 31.1446208784 | 523 | 504990 | -91.49 | 17.26 | 109.04 | 0.56 | 2.21 | 679 |
| 2024-09-20 22:21:36.110 | MS1 | 121.4656738404 | 31.1446329518 | 523 | 504990 | -88.45 | 14.70 | 53.26 | 0.62 | 2.90 | 616 |
| 2024-09-20 22:21:37.230 | MS1 | 121.4656607897 | 31.1446233631 | 523 | 504990 | -90.42 | 9.82 | 87.11 | 0.57 | 2.75 | 565 |
| 2024-09-20 22:21:38.279 | MS1 | 121.4656639117 | 31.1446323696 | 523 | 504990 | -91.06 | 12.75 | 85.86 | 0.54 | 2.32 | 651 |
| 2024-09-20 22:21:39.982 | MS1 | 121.4656764819 | 31.1446375295 | 523 | 504990 | -93.88 | 8.12 | 75.63 | 0.55 | 2.25 | 620 |
| 2024-09-20 22:21:40.799 | MS1 | 121.4656648081 | 31.1446276768 | 523 | 504990 | -89.81 | 11.47 | 344.35 | 0.15 | 2.35 | 1561 |
| 2024-09-20 22:21:41.442 | MS1 | 121.4656638512 | 31.1446216918 | 523 | 504990 | -91.22 | 9.67 | 574.86 | 0.06 | 2.54 | 1597 |
| 2024-09-20 22:21:42.886 | MS1 | 121.4656595181 | 31.1446370888 | 523 | 504990 | -92.85 | 7.99 | 418.14 | 0.17 | 2.83 | 1579 |

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
| 3211640 | 4 | 121.4646087533 | 31.1468771101 | 34 | 14 | 12 | 37.9 | TDD | 739 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3231848 | 2 | 121.4656717791 | 31.1491173007 | 224 | 1 | 0 | 38.0 | TDD | 523 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3232657 | 3 | 121.4651156842 | 31.1479582960 | 24 | 4 | 11 | 39.1 | TDD | 419 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3268378 | 1 | 121.4749577125 | 31.1508860282 | 121 | 2 | 4 | 24.3 | TDD | 295 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |

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
| 2024-09-20 22:21:31.185 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.200 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.338 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.338 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.021 | NREventA3 | measId:2;ServCellPCI:141;Se... |
| 2024-09-20 22:21:38.261 | NRHandoverAttempt | SourcePCI:141;SourceNR-ARFC... |
| 2024-09-20 22:21:38.300 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.311 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.439 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.439 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3268378 | 1 | 18.4029 | 14.5322 | -117.5051 | 5.3391 | 187.7063 | 0.0164 | 0.0125 |
| 2024_09_20 22:00 | 3231848 | 2 | 13.7674 | 8.1667 | -117.4971 | 13.4399 | 194.2232 | 0.0063 | 0.0038 |
| 2024_09_20 22:00 | 3232657 | 3 | 6.4825 | 13.3957 | -117.5930 | 10.2688 | 169.5026 | 0.0062 | 0.0092 |
| 2024_09_20 22:00 | 3211640 | 4 | 15.9100 | 8.6890 | -114.9950 | 10.7962 | 117.6521 | 0.0045 | 0.0187 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414736_2B86FB13 | 504990 | 523 | -90.9 | 504990 | 295 | -92.0 | 504990 | 419 | -102.2 | 504990 | 739 |
| MR_1774414736_41C053BE | 504990 | 523 | -90.7 | 504990 | 295 | -95.4 | 504990 | 419 | -102.5 | 504990 | 739 |
| MR_1774414736_2F34D79D | 504990 | 523 | -90.3 | 504990 | 295 | -92.1 | 504990 | 419 | -103.4 | 504990 | 739 |
| MR_1774414736_4A77FCC5 | 504990 | 523 | -91.8 | 504990 | 295 | -92.1 | 504990 | 419 | -102.4 | 504990 | 739 |
| MR_1774414736_073BB1B0 | 504990 | 523 | -88.4 | 504990 | 295 | -95.3 | 504990 | 419 | -102.2 | 504990 | 739 |
| MR_1774414736_D718021B | 504990 | 523 | -90.7 | 504990 | 295 | -95.0 | 504990 | 419 | -104.5 | 504990 | 739 |
| MR_1774414736_D089F402 | 504990 | 523 | -91.7 | 504990 | 295 | -93.1 | 504990 | 419 | -100.9 | 504990 | 739 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 235: `b50c251a-048...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `b50c251a-048d-4737-bd3e-586135aa1cda` |
| Tag | **single-answer** |
| 정답 | **C1** |
| C1 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[235] topology](images/train_0235.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment. **← 정답**
- `C2`: Add neighbor relationship between 3270636_4 and 3211651_3
- `C3`: Increase transmission power for 3211651_3
- `C4`: Press down the tilt angle of 3218070_2 by 7 degrees
- `C5`: Lift the tilt angle  of 3211651_3 by 10 degrees
- `C6`: Add neighbor relationship between 3218070_2 and 3211651_3
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3218070_2
- `C8`: Decrease transmission power for 3218070_2
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3211651_3
- `C10`: Increase transmission power for 3218070_2
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3211651_3
- `C12`: Decrease transmission power for 3211651_3
- `C13`: Check test server and transmission issues
- `C14`: Lift the tilt angle of 3218070_2 by 7 degrees
- `C15`: Decrease A3 Offset threshold for 3218070_2
- `C16`: Decrease A3 Offset threshold for 3211651_3
- `C17`: Adjust the azimuth of 3211651_3 by 50 degrees
- `C18`: Press down the tilt angle  of 3211651_3 by 10 degrees
- `C19`: Adjust the azimuth of 3218070_2 by 50 degrees
- `C20`: Increase A3 Offset threshold for 3211651_3
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3218070_2
- `C22`: Increase A3 Offset threshold for 3218070_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.815 | MS1 | 121.4656667326 | 31.1446190181 | 970 | 504990 | -87.99 | 15.30 | 471.85 | 0.17 | 2.18 | 1566 |
| 2024-09-20 22:21:32.895 | MS1 | 121.4656744726 | 31.1446262609 | 970 | 504990 | -86.13 | 12.34 | 584.66 | 0.18 | 2.36 | 1565 |
| 2024-09-20 22:21:33.780 | MS1 | 121.4656714659 | 31.1446351574 | 970 | 504990 | -87.41 | 13.31 | 397.95 | 0.01 | 2.14 | 1581 |
| 2024-09-20 22:21:34.347 | MS1 | 121.4656639032 | 31.1446314327 | 970 | 504990 | -86.23 | 13.04 | 82.43 | 0.01 | 2.95 | 1589 |
| 2024-09-20 22:21:35.819 | MS1 | 121.4656590934 | 31.1446211795 | 970 | 504990 | -90.37 | 12.35 | 97.10 | 0.02 | 2.45 | 1579 |
| 2024-09-20 22:21:36.579 | MS1 | 121.4656643220 | 31.1446240016 | 970 | 504990 | -87.17 | 16.30 | 101.77 | 0.10 | 2.84 | 1591 |
| 2024-09-20 22:21:37.608 | MS1 | 121.4656732939 | 31.1446357611 | 970 | 504990 | -93.32 | 9.59 | 69.67 | 0.01 | 2.77 | 1585 |
| 2024-09-20 22:21:38.125 | MS1 | 121.4656714213 | 31.1446185767 | 970 | 504990 | -89.78 | 11.51 | 77.00 | 0.07 | 2.45 | 1595 |
| 2024-09-20 22:21:39.551 | MS1 | 121.4656706686 | 31.1446302101 | 970 | 504990 | -90.66 | 10.44 | 66.08 | 0.20 | 2.24 | 1589 |
| 2024-09-20 22:21:40.948 | MS1 | 121.4656596372 | 31.1446339524 | 970 | 504990 | -91.04 | 11.25 | 386.41 | 0.06 | 2.06 | 1581 |
| 2024-09-20 22:21:41.188 | MS1 | 121.4656623791 | 31.1446352571 | 970 | 504990 | -91.88 | 11.31 | 294.91 | 0.14 | 2.47 | 1570 |
| 2024-09-20 22:21:42.237 | MS1 | 121.4656657877 | 31.1446324707 | 970 | 504990 | -91.04 | 11.64 | 307.18 | 0.17 | 2.58 | 1568 |

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
| 3211651 | 3 | 121.4660015374 | 31.1466643765 | 106 | 4 | 8 | 30.5 | TDD | 918 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3218070 | 2 | 121.4673932983 | 31.1520109251 | 247 | 4 | 6 | 40.4 | TDD | 970 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3235395 | 1 | 121.4673489219 | 31.1540062902 | 154 | 13 | 10 | 31.6 | TDD | 937 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3270636 | 4 | 121.4709607199 | 31.1488099608 | 237 | 0 | 12 | 23.7 | TDD | 79 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:31.061 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.084 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.208 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.208 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.912 | NREventA3 | measId:2;ServCellPCI:108;Se... |
| 2024-09-20 22:21:38.152 | NRHandoverAttempt | SourcePCI:108;SourceNR-ARFC... |
| 2024-09-20 22:21:38.189 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.201 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.327 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.327 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3235395 | 1 | 88.4814 | 89.0712 | -116.1984 | 15.4426 | 171.2415 | 0.0096 | 0.0031 |
| 2024_09_19 22:00 | 3218070 | 2 | 93.4744 | 89.2643 | -114.5586 | 14.7387 | 99.2074 | 0.0030 | 0.0008 |
| 2024_09_19 22:00 | 3211651 | 3 | 87.8729 | 92.1888 | -115.6222 | 13.5898 | 195.4724 | 0.0067 | 0.0187 |
| 2024_09_19 22:00 | 3270636 | 4 | 84.5275 | 93.6597 | -117.2375 | 8.9666 | 109.0393 | 0.0006 | 0.0130 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412107_52B13CC5 | 504990 | 970 | -87.1 | 504990 | 918 | -93.2 | 504990 | 79 | -94.7 | 504990 | 937 |
| MR_1774412107_B3DAA7A4 | 504990 | 970 | -85.3 | 504990 | 918 | -92.4 | 504990 | 79 | -97.3 | 504990 | 937 |
| MR_1774412107_E9115C22 | 504990 | 970 | -84.3 | 504990 | 918 | -94.5 | 504990 | 79 | -95.3 | 504990 | 937 |
| MR_1774412107_052675FE | 504990 | 970 | -85.8 | 504990 | 918 | -94.7 | 504990 | 79 | -98.2 | 504990 | 937 |
| MR_1774412107_409763CC | 504990 | 970 | -87.3 | 504990 | 918 | -93.0 | 504990 | 79 | -96.5 | 504990 | 937 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 236: `2734d324-376...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `2734d324-3760-42a5-af15-64673ee23f7b` |
| Tag | **multiple-answer** |
| 정답 | **C14|C16** |
| C14 의미 | Increase transmission power for 3211936_1 |
| C16 의미 | Adjust the azimuth of 3211936_1 by 50 degrees |
| 패턴 분류 | **P4 Coverage (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[236] topology](images/train_0236.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3211936_1
- `C2`: Lift the tilt angle of 3211936_1 by 10 degrees
- `C3`: Decrease transmission power for 3260175_3
- `C4`: Increase transmission power for 3260175_3
- `C5`: Check test server and transmission issues
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3211936_1
- `C7`: Decrease transmission power for 3211936_1
- `C8`: Add neighbor relationship between 3223864_2 and 3260175_3
- `C9`: Increase A3 Offset threshold for 3260175_3
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3260175_3
- `C11`: Increase A3 Offset threshold for 3211936_1
- `C12`: Press down the tilt angle of 3211936_1 by 10 degrees
- `C13`: Press down the tilt angle  of 3260175_3 by 5 degrees
- `C14`: Increase transmission power for 3211936_1 **← 정답**
- `C15`: Adjust the azimuth of 3260175_3 by 46 degrees
- `C16`: Adjust the azimuth of 3211936_1 by 50 degrees **← 정답**
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3260175_3
- `C18`: Add neighbor relationship between 3211936_1 and 3260175_3
- `C19`: Lift the tilt angle  of 3260175_3 by 5 degrees
- `C20`: Insufficient data; more data is needed for judgment.
- `C21`: Decrease A3 Offset threshold for 3260175_3
- `C22`: Decrease A3 Offset threshold for 3211936_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.210 | MS1 | 121.4656753807 | 31.1446180286 | 352 | 504990 | -93.04 | 17.62 | 507.45 | 0.10 | 2.62 | 1575 |
| 2024-09-20 22:21:32.113 | MS1 | 121.4656706906 | 31.1446214594 | 352 | 504990 | -88.31 | 17.77 | 434.36 | 0.16 | 2.88 | 1560 |
| 2024-09-20 22:21:33.849 | MS1 | 121.4656637745 | 31.1446202998 | 352 | 504990 | -85.01 | 13.63 | 309.19 | 0.15 | 2.87 | 1585 |
| 2024-09-20 22:21:34.222 | MS1 | 121.4656730948 | 31.1446290251 | 352 | 504990 | -106.12 | 0.62 | 42.10 | 0.13 | 1.02 | 1577 |
| 2024-09-20 22:21:35.878 | MS1 | 121.4656775926 | 31.1446212952 | 352 | 504990 | -105.90 | -1.66 | 58.19 | 0.10 | 1.13 | 1596 |
| 2024-09-20 22:21:36.365 | MS1 | 121.4656620780 | 31.1446326750 | 352 | 504990 | -100.73 | -1.69 | 64.16 | 0.15 | 1.21 | 1565 |
| 2024-09-20 22:21:37.189 | MS1 | 121.4656632053 | 31.1446305455 | 352 | 504990 | -108.81 | -0.66 | 28.91 | 0.12 | 1.32 | 1562 |
| 2024-09-20 22:21:38.257 | MS1 | 121.4656694200 | 31.1446202959 | 352 | 504990 | -101.18 | -1.31 | 62.48 | 0.17 | 1.49 | 1586 |
| 2024-09-20 22:21:39.504 | MS1 | 121.4656629655 | 31.1446277860 | 352 | 504990 | -108.76 | -1.91 | 35.44 | 0.19 | 1.40 | 1578 |
| 2024-09-20 22:21:40.345 | MS1 | 121.4656691383 | 31.1446319079 | 352 | 504990 | -88.97 | 12.25 | 401.45 | 0.18 | 2.03 | 1580 |
| 2024-09-20 22:21:41.196 | MS1 | 121.4656683585 | 31.1446211646 | 352 | 504990 | -94.68 | 17.87 | 301.26 | 0.14 | 2.78 | 1590 |
| 2024-09-20 22:21:42.140 | MS1 | 121.4656676732 | 31.1446191915 | 352 | 504990 | -93.98 | 12.46 | 449.56 | 0.13 | 2.93 | 1560 |

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
| 3211936 | 1 | 121.4754461222 | 31.1459141659 | 332 | 15 | 9 | 37.4 | TDD | 352 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3223864 | 2 | 121.4642271194 | 31.1551207404 | 315 | 15 | 6 | 17.7 | TDD | 537 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3260175 | 3 | 121.4720311124 | 31.1485377105 | 188 | 2 | 7 | 34.2 | TDD | 819 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3265678 | 4 | 121.4640922843 | 31.1496571231 | 260 | 15 | 7 | 45.7 | TDD | 798 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |

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
| 2024-09-20 22:21:31.141 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.163 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.295 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.295 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.448 | NREventA2 | measId:1;ServCellPCI:165;Se... |
| 2024-09-20 22:21:34.582 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3211936 | 1 | 16.6053 | 15.6286 | -114.4181 | 5.8761 | 161.4958 | 0.1942 | 0.0166 |
| 2024_09_20 22:00 | 3223864 | 2 | 15.1209 | 9.0374 | -115.2306 | 17.4141 | 161.5715 | 0.0006 | 0.0071 |
| 2024_09_20 22:00 | 3260175 | 3 | 14.3461 | 6.6796 | -117.9201 | 18.9118 | 165.6634 | 0.0077 | 0.0070 |
| 2024_09_20 22:00 | 3265678 | 4 | 7.8267 | 12.8821 | -115.1403 | 19.2634 | 106.3972 | 0.0033 | 0.0051 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414638_43C8C65B | 504990 | 352 | -105.0 | 504990 | 819 | -109.8 | 504990 | 537 | -117.8 | 504990 | 798 |
| MR_1774414638_B9185F43 | 504990 | 352 | -107.8 | 504990 | 819 | -108.5 | 504990 | 537 | -115.3 | 504990 | 798 |
| MR_1774414638_1E539E4A | 504990 | 352 | -107.4 | 504990 | 819 | -111.6 | 504990 | 537 | -117.9 | 504990 | 798 |
| MR_1774414638_52B9C93C | 504990 | 352 | -105.0 | 504990 | 819 | -111.2 | 504990 | 537 | -118.9 | 504990 | 798 |
| MR_1774414638_090C33DF | 504990 | 352 | -107.1 | 504990 | 819 | -108.2 | 504990 | 537 | -115.6 | 504990 | 798 |
| MR_1774414638_5BA5D000 | 504990 | 352 | -106.6 | 504990 | 819 | -111.0 | 504990 | 537 | -118.3 | 504990 | 798 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 237: `ace16cfa-7bb...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `ace16cfa-7bb9-4330-9645-cb37458bd330` |
| Tag | **single-answer** |
| 정답 | **C7** |
| C7 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[237] topology](images/train_0237.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3279708_1
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3245050_3
- `C3`: Add neighbor relationship between 3249634_2 and 3279708_1
- `C4`: Decrease transmission power for 3245050_3
- `C5`: Increase transmission power for 3245050_3
- `C6`: Lift the tilt angle  of 3279708_1 by 10 degrees
- `C7`: Check test server and transmission issues **← 정답**
- `C8`: Insufficient data; more data is needed for judgment.
- `C9`: Decrease A3 Offset threshold for 3279708_1
- `C10`: Adjust the azimuth of 3245050_3 by 27 degrees
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3245050_3
- `C12`: Press down the tilt angle  of 3279708_1 by 10 degrees
- `C13`: Increase A3 Offset threshold for 3245050_3
- `C14`: Increase A3 Offset threshold for 3279708_1
- `C15`: Decrease transmission power for 3279708_1
- `C16`: Add neighbor relationship between 3245050_3 and 3279708_1
- `C17`: Decrease A3 Offset threshold for 3245050_3
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3279708_1
- `C19`: Lift the tilt angle of 3245050_3 by 10 degrees
- `C20`: Press down the tilt angle of 3245050_3 by 10 degrees
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3279708_1
- `C22`: Adjust the azimuth of 3279708_1 by 32 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.107 | MS1 | 121.4656778411 | 31.1446353662 | 109 | 504990 | -87.65 | 13.70 | 326.40 | 0.07 | 2.06 | 1586 |
| 2024-09-20 22:21:32.405 | MS1 | 121.4656770768 | 31.1446204898 | 109 | 504990 | -89.40 | 16.75 | 327.66 | 0.11 | 2.30 | 1580 |
| 2024-09-20 22:21:33.454 | MS1 | 121.4656633381 | 31.1446377349 | 109 | 504990 | -87.37 | 13.79 | 324.82 | 0.02 | 2.02 | 1563 |
| 2024-09-20 22:21:34.393 | MS1 | 121.4656710096 | 31.1446275126 | 109 | 504990 | -87.89 | 17.66 | 90.02 | 0.18 | 2.33 | 491 |
| 2024-09-20 22:21:35.338 | MS1 | 121.4656657764 | 31.1446374699 | 109 | 504990 | -90.74 | 16.45 | 75.07 | 0.06 | 2.89 | 436 |
| 2024-09-20 22:21:36.871 | MS1 | 121.4656772020 | 31.1446191324 | 109 | 504990 | -87.60 | 13.33 | 70.17 | 0.05 | 2.77 | 413 |
| 2024-09-20 22:21:37.691 | MS1 | 121.4656721819 | 31.1446185726 | 109 | 504990 | -90.17 | 11.80 | 66.28 | 0.18 | 2.67 | 429 |
| 2024-09-20 22:21:38.250 | MS1 | 121.4656630333 | 31.1446283495 | 109 | 504990 | -89.82 | 8.40 | 64.56 | 0.06 | 2.14 | 336 |
| 2024-09-20 22:21:39.651 | MS1 | 121.4656641035 | 31.1446299625 | 109 | 504990 | -93.26 | 10.19 | 64.60 | 0.04 | 2.41 | 413 |
| 2024-09-20 22:21:40.325 | MS1 | 121.4656775700 | 31.1446273182 | 109 | 504990 | -92.33 | 8.68 | 509.48 | 0.05 | 2.63 | 1574 |
| 2024-09-20 22:21:41.223 | MS1 | 121.4656630727 | 31.1446375950 | 109 | 504990 | -92.24 | 8.09 | 466.50 | 0.14 | 2.27 | 1597 |
| 2024-09-20 22:21:42.840 | MS1 | 121.4656611133 | 31.1446259019 | 109 | 504990 | -90.54 | 8.11 | 540.41 | 0.10 | 2.56 | 1587 |

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
| 3228010 | 4 | 121.4748778229 | 31.1523239405 | 176 | 6 | 10 | 34.2 | TDD | 86 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3245050 | 3 | 121.4694071566 | 31.1480958867 | 250 | 9 | 9 | 43.6 | TDD | 109 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3249634 | 2 | 121.4656105897 | 31.1507822426 | 147 | 5 | 2 | 36.7 | TDD | 937 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3279708 | 1 | 121.4729004046 | 31.1523419394 | 187 | 14 | 3 | 23.7 | TDD | 200 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |

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
| 2024-09-20 22:21:30.855 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:30.986 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.986 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.654 | NREventA3 | measId:2;ServCellPCI:976;Se... |
| 2024-09-20 22:21:37.894 | NRHandoverAttempt | SourcePCI:976;SourceNR-ARFC... |
| 2024-09-20 22:21:37.944 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.957 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.063 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.063 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3279708 | 1 | 7.2796 | 16.2016 | -114.7225 | 12.5012 | 161.6495 | 0.0024 | 0.0023 |
| 2024_09_20 22:00 | 3249634 | 2 | 18.4808 | 18.4984 | -115.0059 | 9.1152 | 155.7006 | 0.0089 | 0.0189 |
| 2024_09_20 22:00 | 3245050 | 3 | 17.7931 | 13.6792 | -115.9871 | 18.4800 | 179.3564 | 0.0191 | 0.0060 |
| 2024_09_20 22:00 | 3228010 | 4 | 6.8280 | 19.6763 | -117.5696 | 8.1606 | 179.0984 | 0.0017 | 0.0171 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412052_251669D9 | 504990 | 109 | -87.3 | 504990 | 200 | -87.9 | 504990 | 937 | -97.0 | 504990 | 86 |
| MR_1774412052_C23976FF | 504990 | 109 | -87.8 | 504990 | 200 | -90.2 | 504990 | 937 | -100.6 | 504990 | 86 |
| MR_1774412052_0FF33E15 | 504990 | 109 | -87.2 | 504990 | 200 | -88.2 | 504990 | 937 | -99.8 | 504990 | 86 |
| MR_1774412052_3DDE15E1 | 504990 | 109 | -86.8 | 504990 | 200 | -89.4 | 504990 | 937 | -100.6 | 504990 | 86 |
| MR_1774412052_87584CA4 | 504990 | 109 | -89.5 | 504990 | 200 | -87.2 | 504990 | 937 | -100.4 | 504990 | 86 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 238: `67499a69-dd1...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `67499a69-dd14-41cd-8d15-c50f6af8b7f3` |
| Tag | **single-answer** |
| 정답 | **C21** |
| C21 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3262424_2 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[238] topology](images/train_0238.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3262424_2 by 4 degrees
- `C2`: Increase transmission power for 3263857_1
- `C3`: Adjust the azimuth of 3263857_1 by 50 degrees
- `C4`: Lift the tilt angle  of 3263857_1 by 5 degrees
- `C5`: Increase transmission power for 3262424_2
- `C6`: Decrease transmission power for 3262424_2
- `C7`: Press down the tilt angle  of 3263857_1 by 5 degrees
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3263857_1
- `C9`: Decrease transmission power for 3263857_1
- `C10`: Decrease A3 Offset threshold for 3262424_2
- `C11`: Add neighbor relationship between 3262424_2 and 3263857_1
- `C12`: Adjust the azimuth of 3262424_2 by 23 degrees
- `C13`: Press down the tilt angle of 3262424_2 by 4 degrees
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Add neighbor relationship between 3213221_4 and 3263857_1
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3263857_1
- `C17`: Decrease A3 Offset threshold for 3263857_1
- `C18`: Increase A3 Offset threshold for 3263857_1
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3262424_2
- `C20`: Check test server and transmission issues
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3262424_2 **← 정답**
- `C22`: Increase A3 Offset threshold for 3262424_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.248 | MS1 | 121.4656587040 | 31.1446189132 | 882 | 504990 | -85.33 | 13.39 | 398.58 | 0.20 | 2.78 | 1595 |
| 2024-09-20 22:21:32.534 | MS1 | 121.4656603642 | 31.1446190106 | 882 | 504990 | -88.61 | 14.18 | 438.35 | 0.08 | 2.14 | 1586 |
| 2024-09-20 22:21:33.574 | MS1 | 121.4656722346 | 31.1446334843 | 882 | 504990 | -89.39 | 12.68 | 468.52 | 0.16 | 2.98 | 1586 |
| 2024-09-20 22:21:34.157 | MS1 | 121.4656733400 | 31.1446364864 | 882 | 504990 | -88.27 | 17.44 | 87.79 | 0.54 | 2.19 | 585 |
| 2024-09-20 22:21:35.710 | MS1 | 121.4656617015 | 31.1446269361 | 882 | 504990 | -90.93 | 16.58 | 75.54 | 0.53 | 2.34 | 512 |
| 2024-09-20 22:21:36.680 | MS1 | 121.4656724134 | 31.1446379552 | 882 | 504990 | -89.28 | 13.27 | 87.54 | 0.57 | 2.61 | 650 |
| 2024-09-20 22:21:37.644 | MS1 | 121.4656619642 | 31.1446182522 | 882 | 504990 | -90.50 | 10.68 | 70.78 | 0.56 | 2.82 | 687 |
| 2024-09-20 22:21:38.114 | MS1 | 121.4656733210 | 31.1446308167 | 882 | 504990 | -90.38 | 9.42 | 93.38 | 0.69 | 2.45 | 669 |
| 2024-09-20 22:21:39.504 | MS1 | 121.4656605368 | 31.1446275544 | 882 | 504990 | -92.64 | 11.99 | 106.50 | 0.62 | 2.44 | 607 |
| 2024-09-20 22:21:40.790 | MS1 | 121.4656767131 | 31.1446194710 | 882 | 504990 | -93.82 | 9.75 | 338.06 | 0.05 | 2.01 | 1561 |
| 2024-09-20 22:21:41.670 | MS1 | 121.4656613154 | 31.1446345875 | 882 | 504990 | -92.59 | 9.53 | 535.88 | 0.16 | 2.12 | 1589 |
| 2024-09-20 22:21:42.491 | MS1 | 121.4656703881 | 31.1446237817 | 882 | 504990 | -90.85 | 8.24 | 374.91 | 0.02 | 2.43 | 1566 |

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
| 3213221 | 4 | 121.4697585193 | 31.1558824698 | 104 | 15 | 2 | 24.3 | TDD | 658 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3262424 | 2 | 121.4748661056 | 31.1449162595 | 245 | 2 | 4 | 29.8 | TDD | 882 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3263857 | 1 | 121.4719950351 | 31.1554293974 | 318 | 3 | 4 | 45.0 | TDD | 273 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3271622 | 3 | 121.4737690845 | 31.1547508068 | 210 | 6 | 3 | 31.1 | TDD | 974 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |

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
| 2024-09-20 22:21:30.989 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.014 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.148 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.148 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.815 | NREventA3 | measId:2;ServCellPCI:828;Se... |
| 2024-09-20 22:21:38.055 | NRHandoverAttempt | SourcePCI:828;SourceNR-ARFC... |
| 2024-09-20 22:21:38.098 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.108 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.231 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.231 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3263857 | 1 | 7.8577 | 14.0567 | -115.2647 | 12.6525 | 139.2998 | 0.0120 | 0.0064 |
| 2024_09_20 22:00 | 3262424 | 2 | 14.8765 | 18.4826 | -117.0823 | 17.4358 | 180.7802 | 0.0195 | 0.0173 |
| 2024_09_20 22:00 | 3271622 | 3 | 13.0099 | 7.3697 | -114.2587 | 10.5274 | 140.1226 | 0.0046 | 0.0145 |
| 2024_09_20 22:00 | 3213221 | 4 | 15.7852 | 9.9634 | -114.7363 | 14.8569 | 133.4226 | 0.0092 | 0.0149 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412620_CB43BFDB | 504990 | 882 | -86.6 | 504990 | 273 | -96.3 | 504990 | 658 | -101.5 | 504990 | 974 |
| MR_1774412620_35335626 | 504990 | 882 | -88.5 | 504990 | 273 | -100.0 | 504990 | 658 | -100.1 | 504990 | 974 |
| MR_1774412620_464A6732 | 504990 | 882 | -88.2 | 504990 | 273 | -100.1 | 504990 | 658 | -100.1 | 504990 | 974 |
| MR_1774412620_DFED0DC2 | 504990 | 882 | -86.8 | 504990 | 273 | -98.6 | 504990 | 658 | -100.0 | 504990 | 974 |
| MR_1774412620_4712A55B | 504990 | 882 | -87.7 | 504990 | 273 | -97.6 | 504990 | 658 | -103.4 | 504990 | 974 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 239: `9e14afa9-2c4...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `9e14afa9-2c47-4c2c-b6a3-e050053d687f` |
| Tag | **single-answer** |
| 정답 | **C12** |
| C12 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3244079_5 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[239] topology](images/train_0239.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3237816_2 by 26 degrees
- `C2`: Increase transmission power for 3244079_5
- `C3`: Add neighbor relationship between 3216434_12 and 3237816_2
- `C4`: Press down the tilt angle  of 3237816_2 by 6 degrees
- `C5`: Decrease A3 Offset threshold for 3244079_5
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3244079_5
- `C7`: Decrease A3 Offset threshold for 3237816_2
- `C8`: Lift the tilt angle of 3244079_5 by 1 degrees
- `C9`: Add neighbor relationship between 3244079_5 and 3237816_2
- `C10`: Decrease transmission power for 3237816_2
- `C11`: Adjust the azimuth of 3244079_5 by 30 degrees
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3244079_5 **← 정답**
- `C13`: Insufficient data; more data is needed for judgment.
- `C14`: Press down the tilt angle of 3244079_5 by 1 degrees
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3237816_2
- `C16`: Lift the tilt angle  of 3237816_2 by 6 degrees
- `C17`: Increase A3 Offset threshold for 3244079_5
- `C18`: Check test server and transmission issues
- `C19`: Increase transmission power for 3237816_2
- `C20`: Increase A3 Offset threshold for 3237816_2
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3237816_2
- `C22`: Decrease transmission power for 3244079_5

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.937 | MS1 | 121.4656657657 | 31.1446299052 | 977 | 504990 | -95.67 | 11.12 | 549.57 | 0.09 | 2.40 | 1591 |
| 2024-09-20 22:21:32.626 | MS1 | 121.4656648670 | 31.1446189141 | 735 | 504990 | -95.42 | 12.26 | 527.41 | 0.16 | 2.95 | 1571 |
| 2024-09-20 22:21:33.355 | MS1 | 121.4656580778 | 31.1446274924 | 303 | 504990 | -93.71 | 10.45 | 508.38 | 0.12 | 2.27 | 1581 |
| 2024-09-20 22:21:34.757 | MS1 | 121.4656759583 | 31.1446261053 | 243 | 152650 | -87.17 | 7.42 | 81.85 | 0.15 | 1.98 | 988 |
| 2024-09-20 22:21:35.968 | MS1 | 121.4656586629 | 31.1446299466 | 32 | 152650 | -87.34 | 6.42 | 44.99 | 0.16 | 1.51 | 937 |
| 2024-09-20 22:21:36.520 | MS1 | 121.4656628997 | 31.1446320136 | 596 | 152650 | -87.93 | 7.00 | 53.29 | 0.15 | 1.81 | 992 |
| 2024-09-20 22:21:37.169 | MS1 | 121.4656604669 | 31.1446195287 | 187 | 152650 | -93.06 | 4.93 | 60.14 | 0.14 | 1.81 | 941 |
| 2024-09-20 22:21:38.763 | MS1 | 121.4656699871 | 31.1446281509 | 243 | 152650 | -96.38 | 7.72 | 88.19 | 0.07 | 1.53 | 936 |
| 2024-09-20 22:21:39.702 | MS1 | 121.4656733047 | 31.1446246033 | 32 | 152650 | -96.47 | 6.28 | 87.05 | 0.05 | 1.68 | 989 |
| 2024-09-20 22:21:40.740 | MS1 | 121.4656618217 | 31.1446187627 | 596 | 152650 | -90.51 | 3.77 | 70.91 | 0.04 | 2.28 | 1561 |
| 2024-09-20 22:21:41.231 | MS1 | 121.4656695980 | 31.1446186239 | 187 | 152650 | -91.88 | 4.66 | 60.78 | 0.05 | 2.47 | 1579 |
| 2024-09-20 22:21:42.671 | MS1 | 121.4656611254 | 31.1446343329 | 243 | 152650 | -92.88 | 7.85 | 96.06 | 0.08 | 2.46 | 1573 |

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
| 3210755 | 7 | 121.4693942730 | 31.1544438716 | 185 | 6 | 0 | 17.0 | FDD | 32 | n1 | 152650 | 30M | 4T4R | 24 | 152650 |
| 3214381 | 1 | 121.4645238634 | 31.1556093270 | 217 | 1 | 10 | 4.4 | TDD | 742 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3216434 | 12 | 121.4701821425 | 31.1520546005 | 170 | 12 | 0 | 11.6 | FDD | 596 | n1 | 152650 | 30M | 4T4R | 30 | 152650 |
| 3218377 | 10 | 121.4662769044 | 31.1541637631 | 68 | 7 | 2 | 19.9 | FDD | 721 | n1 | 152650 | 30M | 4T4R | 29 | 152650 |
| 3221903 | 11 | 121.4647509705 | 31.1482387118 | 253 | 7 | 1 | 1.8 | FDD | 243 | n1 | 152650 | 30M | 4T4R | 28 | 152650 |
| 3224385 | 13 | 121.4714614554 | 31.1444504644 | 19 | 6 | 4 | 15.5 | FDD | 187 | n1 | 152650 | 30M | 4T4R | 15 | 152650 |
| 3226052 | 6 | 121.4732792169 | 31.1512128166 | 27 | 0 | 11 | 28.6 | TDD | 735 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3237816 | 2 | 121.4746697653 | 31.1538185573 | 194 | 5 | 4 | 12.9 | TDD | 358 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3242545 | 3 | 121.4739061989 | 31.1538504625 | 101 | 12 | 7 | 17.0 | TDD | 679 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3244079 | 5 | 121.4687018011 | 31.1466754966 | 202 | 1 | 5 | 1.3 | TDD | 977 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3263475 | 8 | 121.4713340778 | 31.1517165011 | 131 | 12 | 11 | 4.3 | FDD | 70 | n1 | 152650 | 30M | 4T4R | 26 | 152650 |
| 3269034 | 9 | 121.4701548341 | 31.1518834251 | 268 | 7 | 1 | 21.8 | FDD | 968 | n1 | 152650 | 30M | 4T4R | 11 | 152650 |
| 3276912 | 4 | 121.4658948496 | 31.1520192597 | 281 | 7 | 1 | 27.5 | TDD | 303 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |

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
| 2024-09-20 22:21:30.984 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.000 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.100 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.100 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.884 | NREventA2 | measId:1;ServCellPCI:628;Se... |
| 2024-09-20 22:21:34.996 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.283 | NREventA5 | measId:3;ServCellPCI:628;Se... |
| 2024-09-20 22:21:35.336 | NRHandoverAttempt | SourcePCI:628;SourceNR-ARFC... |
| 2024-09-20 22:21:35.372 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.382 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:35.503 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.503 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3214381 | 1 | 15.8290 | 17.3743 | -115.9782 | 17.4911 | 141.5262 | 0.0147 | 0.0021 |
| 2024_09_20 22:00 | 3237816 | 2 | 9.0133 | 11.9716 | -117.9865 | 11.6965 | 172.9268 | 0.0119 | 0.0103 |
| 2024_09_20 22:00 | 3242545 | 3 | 10.8186 | 18.4393 | -117.7128 | 16.3186 | 169.0794 | 0.0115 | 0.0125 |
| 2024_09_20 22:00 | 3276912 | 4 | 19.2221 | 11.9180 | -116.2498 | 13.1631 | 119.8129 | 0.0198 | 0.0054 |
| 2024_09_20 22:00 | 3244079 | 5 | 8.1498 | 18.6679 | -116.6071 | 6.2483 | 107.8201 | 0.0181 | 0.0091 |
| 2024_09_20 22:00 | 3226052 | 6 | 15.8510 | 5.1010 | -117.1141 | 12.1589 | 154.6118 | 0.0183 | 0.0051 |
| 2024_09_20 22:00 | 3210755 | 7 | 18.0422 | 18.5103 | -114.7910 | 3.4117 | 24.0056 | 0.0108 | 0.0163 |
| 2024_09_20 22:00 | 3263475 | 8 | 7.1237 | 12.5764 | -114.7199 | 3.0551 | 46.3596 | 0.0020 | 0.0094 |
| 2024_09_20 22:00 | 3269034 | 9 | 19.5606 | 17.7954 | -115.1903 | 4.1916 | 54.4080 | 0.0053 | 0.0157 |
| 2024_09_20 22:00 | 3218377 | 10 | 10.3739 | 14.6266 | -116.9590 | 3.0213 | 37.5922 | 0.0181 | 0.0091 |
| 2024_09_20 22:00 | 3221903 | 11 | 16.8575 | 7.0888 | -117.5812 | 4.0024 | 41.6223 | 0.0008 | 0.0014 |
| 2024_09_20 22:00 | 3216434 | 12 | 7.1219 | 19.5202 | -115.8480 | 4.1874 | 49.4051 | 0.0017 | 0.0034 |
| 2024_09_20 22:00 | 3224385 | 13 | 15.0398 | 15.9105 | -115.2079 | 3.6887 | 58.3928 | 0.0102 | 0.0169 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416966_AD92F257 | 152650 | 243 | -88.6 | 152650 | 968 | -91.5 | 152650 | 70 | -94.5 | 152650 | 721 |
| MR_1774416966_C8B00DF5 | 152650 | 243 | -88.9 | 152650 | 968 | -89.9 | 152650 | 70 | -94.5 | 152650 | 721 |
| MR_1774416966_46B87ED4 | 504990 | 303 | -92.9 | 504990 | 358 | -91.2 | 504990 | 742 | -93.5 | 504990 | 679 |
| MR_1774416966_68418EDE | 504990 | 303 | -93.6 | 504990 | 358 | -88.1 | 504990 | 742 | -93.9 | 504990 | 679 |
| MR_1774416966_B157E3FE | 152650 | 243 | -88.7 | 152650 | 968 | -90.9 | 152650 | 70 | -93.8 | 152650 | 721 |
| MR_1774416966_8A413152 | 504990 | 303 | -94.8 | 504990 | 358 | -88.0 | 504990 | 742 | -95.3 | 504990 | 679 |

> *... 2개 열 생략 (전체 14열)*

---
