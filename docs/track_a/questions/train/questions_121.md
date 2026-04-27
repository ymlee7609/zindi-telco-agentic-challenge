# Track A 문제 분석 — train[1200]~train[1209]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[1200] ~ train[1209] (10개)

## 목차

1. [문제 1200: `a63f5379-85b...`](#1200) — single-answer, 정답: C22
2. [문제 1201: `8e168583-f9d...`](#1201) — multiple-answer, 정답: C2|C12
3. [문제 1202: `62383fad-3c8...`](#1202) — single-answer, 정답: C17
4. [문제 1203: `f8070f83-41a...`](#1203) — single-answer, 정답: C19
5. [문제 1204: `a920f86c-b99...`](#1204) — single-answer, 정답: C18
6. [문제 1205: `6fe3bcb3-662...`](#1205) — single-answer, 정답: C7
7. [문제 1206: `1a47dec7-a77...`](#1206) — single-answer, 정답: C4
8. [문제 1207: `163e0528-3fe...`](#1207) — single-answer, 정답: C4
9. [문제 1208: `a1fddc2f-8c0...`](#1208) — single-answer, 정답: C12
10. [문제 1209: `7a021f13-b6e...`](#1209) — single-answer, 정답: C19

---

### 문제 1200: `a63f5379-85b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `a63f5379-85ba-426e-9b63-07234c2323b8` |
| Tag | **single-answer** |
| 정답 | **C22** |
| C22 의미 | Decrease A3 Offset threshold for 3274825_4 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1200] topology](images/train_1200.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3254433_2
- `C2`: Insufficient data; more data is needed for judgment.
- `C3`: Lift the tilt angle  of 3254433_2 by 10 degrees
- `C4`: Decrease transmission power for 3274825_4
- `C5`: Add neighbor relationship between 3274825_4 and 3254433_2
- `C6`: Check test server and transmission issues
- `C7`: Add neighbor relationship between 3219773_3 and 3254433_2
- `C8`: Increase A3 Offset threshold for 3254433_2
- `C9`: Increase A3 Offset threshold for 3274825_4
- `C10`: Press down the tilt angle of 3274825_4 by 10 degrees
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3254433_2
- `C12`: Adjust the azimuth of 3254433_2 by 50 degrees
- `C13`: Press down the tilt angle  of 3254433_2 by 10 degrees
- `C14`: Lift the tilt angle of 3274825_4 by 10 degrees
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3274825_4
- `C16`: Adjust the azimuth of 3274825_4 by 50 degrees
- `C17`: Decrease A3 Offset threshold for 3254433_2
- `C18`: Increase transmission power for 3274825_4
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3254433_2
- `C20`: Increase transmission power for 3254433_2
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3274825_4
- `C22`: Decrease A3 Offset threshold for 3274825_4 **← 정답**

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.308 | MS1 | 121.4656624248 | 31.1446337380 | 342 | 504990 | -78.96 | 14.53 | 324.97 | 0.13 | 2.64 | 1568 |
| 2024-09-20 22:21:32.480 | MS1 | 121.4656686647 | 31.1446253200 | 342 | 504990 | -82.04 | 17.12 | 511.01 | 0.11 | 2.80 | 1578 |
| 2024-09-20 22:21:33.612 | MS1 | 121.4656646841 | 31.1446240604 | 342 | 504990 | -76.19 | 16.50 | 321.94 | 0.00 | 2.88 | 1594 |
| 2024-09-20 22:21:34.606 | MS1 | 121.4656765577 | 31.1446352912 | 342 | 504990 | -92.61 | -1.99 | 34.85 | 0.13 | 1.47 | 1578 |
| 2024-09-20 22:21:35.143 | MS1 | 121.4656739158 | 31.1446193143 | 342 | 504990 | -88.82 | -2.96 | 63.54 | 0.19 | 1.20 | 1580 |
| 2024-09-20 22:21:36.579 | MS1 | 121.4656581227 | 31.1446373374 | 342 | 504990 | -88.87 | -3.88 | 83.33 | 0.03 | 1.24 | 1563 |
| 2024-09-20 22:21:37.615 | MS1 | 121.4656728354 | 31.1446208507 | 342 | 504990 | -85.10 | -0.66 | 61.51 | 0.02 | 1.29 | 1594 |
| 2024-09-20 22:21:38.227 | MS1 | 121.4656645110 | 31.1446277365 | 342 | 504990 | -84.77 | -2.71 | 76.00 | 0.17 | 1.31 | 1599 |
| 2024-09-20 22:21:39.232 | MS1 | 121.4656627969 | 31.1446256288 | 332 | 504990 | -77.27 | 14.54 | 268.90 | 0.16 | 1.31 | 1573 |
| 2024-09-20 22:21:40.336 | MS1 | 121.4656667127 | 31.1446299884 | 332 | 504990 | -82.84 | 14.33 | 404.87 | 0.17 | 2.20 | 1580 |
| 2024-09-20 22:21:41.521 | MS1 | 121.4656646865 | 31.1446336338 | 332 | 504990 | -84.60 | 17.30 | 354.30 | 0.05 | 2.82 | 1596 |
| 2024-09-20 22:21:42.143 | MS1 | 121.4656651505 | 31.1446362816 | 332 | 504990 | -77.69 | 14.97 | 587.48 | 0.17 | 2.43 | 1590 |

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
| 3219773 | 3 | 121.4673416032 | 31.1518223223 | 156 | 9 | 12 | 43.2 | TDD | 917 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3236482 | 1 | 121.4739140589 | 31.1454562477 | 260 | 3 | 9 | 34.6 | TDD | 353 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3254433 | 2 | 121.4725169862 | 31.1550112455 | 279 | 14 | 4 | 22.1 | TDD | 332 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3274825 | 4 | 121.4733153268 | 31.1525864580 | 311 | 14 | 4 | 25.5 | TDD | 342 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |

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
| 2024-09-20 22:21:31.389 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.410 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.546 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.546 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.251 | NREventA3 | measId:2;ServCellPCI:599;Se... |
| 2024-09-20 22:21:38.491 | NRHandoverAttempt | SourcePCI:599;SourceNR-ARFC... |
| 2024-09-20 22:21:38.530 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.543 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.672 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.672 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3236482 | 1 | 17.0330 | 13.9306 | -115.8083 | 16.2354 | 116.5541 | 0.0066 | 0.0094 |
| 2024_09_20 22:00 | 3254433 | 2 | 6.6751 | 10.5119 | -115.1110 | 10.5946 | 182.2415 | 0.0179 | 0.0124 |
| 2024_09_20 22:00 | 3219773 | 3 | 7.9141 | 18.0642 | -117.6782 | 15.4281 | 197.1081 | 0.0097 | 0.0166 |
| 2024_09_20 22:00 | 3274825 | 4 | 18.3046 | 8.8586 | -115.4109 | 8.2852 | 101.9771 | 0.0036 | 0.1467 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413146_F51BFE64 | 504990 | 332 | -87.6 | 504990 | 342 | -90.8 | 504990 | 917 | -91.4 | 504990 | 353 |
| MR_1774413146_5D7C79EB | 504990 | 332 | -85.8 | 504990 | 342 | -94.1 | 504990 | 917 | -88.3 | 504990 | 353 |
| MR_1774413146_B8C31127 | 504990 | 342 | -92.4 | 504990 | 332 | -86.9 | 504990 | 917 | -90.9 | 504990 | 353 |
| MR_1774413146_93B97152 | 504990 | 332 | -86.7 | 504990 | 342 | -93.5 | 504990 | 917 | -88.8 | 504990 | 353 |
| MR_1774413146_29C4722C | 504990 | 342 | -93.2 | 504990 | 332 | -88.6 | 504990 | 917 | -89.4 | 504990 | 353 |
| MR_1774413146_F4C6AE14 | 504990 | 332 | -88.4 | 504990 | 342 | -91.5 | 504990 | 917 | -91.0 | 504990 | 353 |
| MR_1774413146_99A3D485 | 504990 | 342 | -91.4 | 504990 | 332 | -86.5 | 504990 | 917 | -88.3 | 504990 | 353 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1201: `8e168583-f9d...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `8e168583-f9d9-4c19-9f6c-1666f20f7b19` |
| Tag | **multiple-answer** |
| 정답 | **C2|C12** |
| C2 의미 | Press down the tilt angle  of 3219521_2 by 3 degrees |
| C12 의미 | Decrease transmission power for 3219521_2 |
| 패턴 분류 | **P3 Overshoot (tilt)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1201] topology](images/train_1201.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3219521_2 by 22 degrees
- `C2`: Press down the tilt angle  of 3219521_2 by 3 degrees **← 정답**
- `C3`: Increase transmission power for 3219521_2
- `C4`: Increase A3 Offset threshold for 3240788_1
- `C5`: Press down the tilt angle of 3240788_1 by 2 degrees
- `C6`: Add neighbor relationship between 3245002_4 and 3219521_2
- `C7`: Lift the tilt angle  of 3219521_2 by 3 degrees
- `C8`: Add neighbor relationship between 3240788_1 and 3219521_2
- `C9`: Decrease A3 Offset threshold for 3219521_2
- `C10`: Check test server and transmission issues
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3240788_1
- `C12`: Decrease transmission power for 3219521_2 **← 정답**
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3219521_2
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3219521_2
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3240788_1
- `C16`: Increase A3 Offset threshold for 3219521_2
- `C17`: Increase transmission power for 3240788_1
- `C18`: Adjust the azimuth of 3240788_1 by 15 degrees
- `C19`: Lift the tilt angle of 3240788_1 by 2 degrees
- `C20`: Insufficient data; more data is needed for judgment.
- `C21`: Decrease A3 Offset threshold for 3240788_1
- `C22`: Decrease transmission power for 3240788_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.845 | MS1 | 121.4656776726 | 31.1446372769 | 549 | 504990 | -79.61 | 15.06 | 564.21 | 0.17 | 2.16 | 1578 |
| 2024-09-20 22:21:32.860 | MS1 | 121.4656606853 | 31.1446242307 | 549 | 504990 | -78.28 | 14.63 | 413.18 | 0.05 | 2.22 | 1566 |
| 2024-09-20 22:21:33.462 | MS1 | 121.4656622130 | 31.1446369970 | 549 | 504990 | -78.11 | 16.99 | 429.98 | 0.15 | 2.75 | 1584 |
| 2024-09-20 22:21:34.650 | MS1 | 121.4656678052 | 31.1446346405 | 549 | 504990 | -88.07 | 2.05 | 40.39 | 0.16 | 1.27 | 1578 |
| 2024-09-20 22:21:35.328 | MS1 | 121.4656778614 | 31.1446325742 | 549 | 504990 | -87.77 | 3.30 | 46.33 | 0.15 | 1.16 | 1568 |
| 2024-09-20 22:21:36.998 | MS1 | 121.4656731286 | 31.1446211826 | 549 | 504990 | -91.79 | 3.72 | 31.44 | 0.18 | 1.43 | 1577 |
| 2024-09-20 22:21:37.198 | MS1 | 121.4656633910 | 31.1446277535 | 549 | 504990 | -94.25 | 2.40 | 60.37 | 0.20 | 1.16 | 1595 |
| 2024-09-20 22:21:38.317 | MS1 | 121.4656664788 | 31.1446328189 | 549 | 504990 | -94.21 | 2.85 | 88.64 | 0.07 | 1.00 | 1593 |
| 2024-09-20 22:21:39.100 | MS1 | 121.4656603514 | 31.1446352775 | 549 | 504990 | -87.55 | 0.94 | 73.67 | 0.20 | 1.10 | 1571 |
| 2024-09-20 22:21:40.277 | MS1 | 121.4656732865 | 31.1446342381 | 549 | 504990 | -83.40 | 13.58 | 313.71 | 0.19 | 2.57 | 1585 |
| 2024-09-20 22:21:41.878 | MS1 | 121.4656591550 | 31.1446329715 | 549 | 504990 | -77.34 | 17.21 | 356.80 | 0.16 | 2.95 | 1577 |
| 2024-09-20 22:21:42.622 | MS1 | 121.4656587629 | 31.1446349577 | 549 | 504990 | -81.73 | 12.45 | 348.97 | 0.03 | 2.18 | 1579 |

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
| 3219521 | 2 | 121.4721716282 | 31.1465728828 | 229 | 1 | 4 | 24.0 | TDD | 539 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3233491 | 3 | 121.4739730140 | 31.1496095015 | 225 | 5 | 9 | 37.1 | TDD | 677 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3240788 | 1 | 121.4719796719 | 31.1513392671 | 204 | 1 | 12 | 20.5 | TDD | 549 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3245002 | 4 | 121.4747220927 | 31.1448396026 | 344 | 3 | 11 | 19.0 | TDD | 495 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |

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
| 2024-09-20 22:21:31.262 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.285 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.388 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.388 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3240788 | 1 | 16.0031 | 5.3223 | -109.9809 | 18.9904 | 129.6822 | 0.0182 | 0.0133 |
| 2024_09_20 22:00 | 3219521 | 2 | 19.5199 | 12.3700 | -117.6691 | 14.4228 | 116.5904 | 0.0138 | 0.0162 |
| 2024_09_20 22:00 | 3233491 | 3 | 15.4100 | 9.5064 | -115.1416 | 8.0376 | 106.2543 | 0.0042 | 0.0173 |
| 2024_09_20 22:00 | 3245002 | 4 | 10.5434 | 8.8731 | -115.5326 | 9.8634 | 101.1954 | 0.0094 | 0.0050 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414545_365F52EB | 504990 | 549 | -87.9 | 504990 | 539 | -87.0 | 504990 | 495 | -87.1 | 504990 | 677 |
| MR_1774414545_584F9AE6 | 504990 | 549 | -90.0 | 504990 | 539 | -84.2 | 504990 | 495 | -87.6 | 504990 | 677 |
| MR_1774414545_F3D6D987 | 504990 | 539 | -89.0 | 504990 | 549 | -86.6 | 504990 | 495 | -85.9 | 504990 | 677 |
| MR_1774414545_2AA43CD5 | 504990 | 539 | -87.1 | 504990 | 549 | -85.5 | 504990 | 495 | -87.8 | 504990 | 677 |
| MR_1774414545_E3BBE7EC | 504990 | 549 | -88.6 | 504990 | 539 | -83.3 | 504990 | 495 | -88.8 | 504990 | 677 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1202: `62383fad-3c8...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `62383fad-3c84-4bfb-b799-cd8cc6fa7940` |
| Tag | **single-answer** |
| 정답 | **C17** |
| C17 의미 | Add neighbor relationship between 3224576_1 and 3231556_2 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1202] topology](images/train_1202.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3231556_2
- `C2`: Decrease transmission power for 3231556_2
- `C3`: Increase transmission power for 3224576_1
- `C4`: Adjust the azimuth of 3231556_2 by 40 degrees
- `C5`: Increase A3 Offset threshold for 3224576_1
- `C6`: Decrease A3 Offset threshold for 3224576_1
- `C7`: Lift the tilt angle of 3224576_1 by 9 degrees
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3231556_2
- `C9`: Press down the tilt angle of 3224576_1 by 9 degrees
- `C10`: Add neighbor relationship between 3269970_3 and 3231556_2
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3224576_1
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3224576_1
- `C13`: Decrease transmission power for 3224576_1
- `C14`: Adjust the azimuth of 3224576_1 by 50 degrees
- `C15`: Press down the tilt angle  of 3231556_2 by 5 degrees
- `C16`: Check test server and transmission issues
- `C17`: Add neighbor relationship between 3224576_1 and 3231556_2 **← 정답**
- `C18`: Insufficient data; more data is needed for judgment.
- `C19`: Increase transmission power for 3231556_2
- `C20`: Increase A3 Offset threshold for 3231556_2
- `C21`: Decrease A3 Offset threshold for 3231556_2
- `C22`: Lift the tilt angle  of 3231556_2 by 5 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.167 | MS1 | 121.4656665436 | 31.1446293922 | 407 | 504990 | -80.87 | 12.32 | 582.91 | 0.19 | 2.47 | 1580 |
| 2024-09-20 22:21:32.793 | MS1 | 121.4656615886 | 31.1446194141 | 407 | 504990 | -81.21 | 13.15 | 441.86 | 0.20 | 2.84 | 1595 |
| 2024-09-20 22:21:33.136 | MS1 | 121.4656651938 | 31.1446209638 | 407 | 504990 | -82.86 | 13.07 | 408.29 | 0.07 | 2.64 | 1591 |
| 2024-09-20 22:21:34.190 | MS1 | 121.4656649040 | 31.1446341611 | 407 | 504990 | -88.76 | -2.53 | 51.98 | 0.01 | 1.42 | 1567 |
| 2024-09-20 22:21:35.313 | MS1 | 121.4656752623 | 31.1446217501 | 407 | 504990 | -86.31 | -2.16 | 45.22 | 0.20 | 1.46 | 1577 |
| 2024-09-20 22:21:36.121 | MS1 | 121.4656734533 | 31.1446197630 | 407 | 504990 | -90.98 | -0.80 | 71.60 | 0.12 | 1.40 | 1574 |
| 2024-09-20 22:21:37.325 | MS1 | 121.4656601519 | 31.1446287469 | 407 | 504990 | -86.58 | -2.46 | 49.88 | 0.07 | 1.18 | 1579 |
| 2024-09-20 22:21:38.340 | MS1 | 121.4656615097 | 31.1446215570 | 407 | 504990 | -84.09 | 14.68 | 468.62 | 0.20 | 1.09 | 1568 |
| 2024-09-20 22:21:39.305 | MS1 | 121.4656656117 | 31.1446274685 | 407 | 504990 | -75.93 | 14.96 | 347.65 | 0.14 | 1.44 | 1561 |
| 2024-09-20 22:21:40.160 | MS1 | 121.4656675139 | 31.1446238620 | 407 | 504990 | -80.54 | 17.02 | 572.09 | 0.02 | 2.95 | 1591 |
| 2024-09-20 22:21:41.665 | MS1 | 121.4656613675 | 31.1446197049 | 407 | 504990 | -82.16 | 17.55 | 326.83 | 0.11 | 2.08 | 1575 |
| 2024-09-20 22:21:42.897 | MS1 | 121.4656608987 | 31.1446212974 | 407 | 504990 | -77.36 | 14.53 | 544.49 | 0.03 | 2.78 | 1572 |

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
| 3224576 | 1 | 121.4714453273 | 31.1528823109 | 79 | 6 | 5 | 49.8 | TDD | 407 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3231556 | 2 | 121.4657124646 | 31.1549300405 | 220 | 3 | 5 | 32.4 | TDD | 273 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3260195 | 4 | 121.4702979724 | 31.1526270118 | 184 | 6 | 7 | 21.5 | TDD | 775 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3269970 | 3 | 121.4742273224 | 31.1526051744 | 320 | 2 | 11 | 36.8 | TDD | 971 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:31.011 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.030 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.157 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.157 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.859 | NREventA3 | measId:2;ServCellPCI:145;Se... |
| 2024-09-20 22:21:35.859 | NREventA3 | measId:2;ServCellPCI:145;Se... |
| 2024-09-20 22:21:36.859 | NREventA3 | measId:2;ServCellPCI:145;Se... |
| 2024-09-20 22:21:39.359 | NRRRCReestablishAttempt | PCI:145 |
| 2024-09-20 22:21:39.379 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.389 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:39.516 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.516 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3224576 | 1 | 13.0156 | 13.8087 | -114.1454 | 7.8895 | 144.6724 | 0.0054 | 0.1310 |
| 2024_09_20 22:00 | 3231556 | 2 | 15.8302 | 19.5346 | -117.8839 | 12.3851 | 80.4587 | 0.0178 | 0.0166 |
| 2024_09_20 22:00 | 3269970 | 3 | 15.0978 | 19.1211 | -115.3828 | 15.3715 | 143.6856 | 0.0059 | 0.0164 |
| 2024_09_20 22:00 | 3260195 | 4 | 13.1996 | 18.3208 | -117.2269 | 9.5972 | 137.1516 | 0.0095 | 0.0072 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412273_8A438BD4 | 504990 | 273 | -85.4 | 504990 | 407 | -90.0 | 504990 | 971 | -88.7 | 504990 | 775 |
| MR_1774412273_171B5A09 | 504990 | 407 | -88.0 | 504990 | 273 | -82.9 | 504990 | 971 | -86.6 | 504990 | 775 |
| MR_1774412273_15431E76 | 504990 | 273 | -84.4 | 504990 | 407 | -89.8 | 504990 | 971 | -85.5 | 504990 | 775 |
| MR_1774412273_EF98BD18 | 504990 | 407 | -90.7 | 504990 | 273 | -82.6 | 504990 | 971 | -87.0 | 504990 | 775 |
| MR_1774412273_80CF87B7 | 504990 | 407 | -88.4 | 504990 | 273 | -85.0 | 504990 | 971 | -88.4 | 504990 | 775 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1203: `f8070f83-41a...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `f8070f83-41a5-4c95-985b-f805f18c0029` |
| Tag | **single-answer** |
| 정답 | **C19** |
| C19 의미 | Add neighbor relationship between 3233700_1 and 3233553_2 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1203] topology](images/train_1203.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3233553_2
- `C2`: Decrease A3 Offset threshold for 3233700_1
- `C3`: Add neighbor relationship between 3254595_3 and 3233553_2
- `C4`: Increase A3 Offset threshold for 3233700_1
- `C5`: Adjust the azimuth of 3233553_2 by 38 degrees
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3233553_2
- `C7`: Insufficient data; more data is needed for judgment.
- `C8`: Press down the tilt angle  of 3233553_2 by 3 degrees
- `C9`: Press down the tilt angle of 3233700_1 by 1 degrees
- `C10`: Decrease A3 Offset threshold for 3233553_2
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3233553_2
- `C12`: Lift the tilt angle  of 3233553_2 by 3 degrees
- `C13`: Adjust the azimuth of 3233700_1 by 50 degrees
- `C14`: Lift the tilt angle of 3233700_1 by 1 degrees
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3233700_1
- `C16`: Increase transmission power for 3233553_2
- `C17`: Check test server and transmission issues
- `C18`: Decrease transmission power for 3233553_2
- `C19`: Add neighbor relationship between 3233700_1 and 3233553_2 **← 정답**
- `C20`: Decrease transmission power for 3233700_1
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3233700_1
- `C22`: Increase transmission power for 3233700_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.120 | MS1 | 121.4656760238 | 31.1446329105 | 408 | 504990 | -75.18 | 13.63 | 425.98 | 0.13 | 2.75 | 1591 |
| 2024-09-20 22:21:32.826 | MS1 | 121.4656740983 | 31.1446309676 | 408 | 504990 | -79.73 | 12.66 | 388.44 | 0.18 | 2.21 | 1587 |
| 2024-09-20 22:21:33.468 | MS1 | 121.4656660557 | 31.1446348475 | 408 | 504990 | -75.28 | 16.28 | 589.49 | 0.03 | 2.41 | 1585 |
| 2024-09-20 22:21:34.662 | MS1 | 121.4656725801 | 31.1446337437 | 408 | 504990 | -89.56 | -0.18 | 64.12 | 0.06 | 1.03 | 1582 |
| 2024-09-20 22:21:35.621 | MS1 | 121.4656601645 | 31.1446265006 | 408 | 504990 | -89.55 | -3.77 | 62.19 | 0.04 | 1.05 | 1562 |
| 2024-09-20 22:21:36.485 | MS1 | 121.4656731540 | 31.1446288814 | 408 | 504990 | -90.58 | -3.89 | 46.43 | 0.09 | 1.13 | 1591 |
| 2024-09-20 22:21:37.221 | MS1 | 121.4656765909 | 31.1446321650 | 408 | 504990 | -92.76 | -1.50 | 42.50 | 0.16 | 1.42 | 1560 |
| 2024-09-20 22:21:38.952 | MS1 | 121.4656698632 | 31.1446221045 | 408 | 504990 | -80.73 | 13.57 | 456.38 | 0.02 | 1.29 | 1564 |
| 2024-09-20 22:21:39.540 | MS1 | 121.4656659881 | 31.1446357810 | 408 | 504990 | -83.87 | 16.65 | 325.43 | 0.08 | 1.40 | 1564 |
| 2024-09-20 22:21:40.591 | MS1 | 121.4656592294 | 31.1446229647 | 408 | 504990 | -84.82 | 13.69 | 393.21 | 0.05 | 2.17 | 1590 |
| 2024-09-20 22:21:41.432 | MS1 | 121.4656730981 | 31.1446281001 | 408 | 504990 | -82.58 | 14.42 | 344.72 | 0.02 | 2.18 | 1580 |
| 2024-09-20 22:21:42.746 | MS1 | 121.4656581951 | 31.1446202318 | 408 | 504990 | -75.36 | 16.55 | 499.71 | 0.04 | 2.51 | 1599 |

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
| 3233553 | 2 | 121.4724694592 | 31.1543872834 | 249 | 2 | 11 | 16.2 | TDD | 665 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3233700 | 1 | 121.4758056227 | 31.1551225450 | 285 | 0 | 4 | 37.8 | TDD | 408 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3247694 | 4 | 121.4696121974 | 31.1498191294 | 43 | 5 | 8 | 47.3 | TDD | 638 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3254595 | 3 | 121.4687404928 | 31.1546067678 | 106 | 5 | 7 | 16.7 | TDD | 819 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |

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
| 2024-09-20 22:21:30.737 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.761 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:30.875 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.875 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.612 | NREventA3 | measId:2;ServCellPCI:507;Se... |
| 2024-09-20 22:21:35.612 | NREventA3 | measId:2;ServCellPCI:507;Se... |
| 2024-09-20 22:21:36.612 | NREventA3 | measId:2;ServCellPCI:507;Se... |
| 2024-09-20 22:21:39.112 | NRRRCReestablishAttempt | PCI:507 |
| 2024-09-20 22:21:39.122 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.134 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:39.256 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.256 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3233700 | 1 | 9.6802 | 11.7848 | -117.0674 | 12.6042 | 92.4493 | 0.0103 | 0.1587 |
| 2024_09_20 22:00 | 3233553 | 2 | 8.3972 | 9.2248 | -114.0225 | 12.3667 | 180.2628 | 0.0003 | 0.0126 |
| 2024_09_20 22:00 | 3254595 | 3 | 8.6607 | 9.1262 | -117.0864 | 10.6395 | 110.8853 | 0.0128 | 0.0035 |
| 2024_09_20 22:00 | 3247694 | 4 | 7.6885 | 7.4075 | -117.3115 | 12.3058 | 197.5363 | 0.0033 | 0.0041 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414992_E67E6559 | 504990 | 665 | -83.6 | 504990 | 408 | -90.2 | 504990 | 819 | -86.8 | 504990 | 638 |
| MR_1774414992_BCBF08CA | 504990 | 408 | -89.0 | 504990 | 665 | -84.8 | 504990 | 819 | -86.2 | 504990 | 638 |
| MR_1774414992_EB432F04 | 504990 | 665 | -86.1 | 504990 | 408 | -90.4 | 504990 | 819 | -88.6 | 504990 | 638 |
| MR_1774414992_0B6F8A94 | 504990 | 408 | -88.5 | 504990 | 665 | -84.2 | 504990 | 819 | -89.3 | 504990 | 638 |
| MR_1774414992_839F015A | 504990 | 408 | -89.5 | 504990 | 665 | -83.6 | 504990 | 819 | -89.0 | 504990 | 638 |
| MR_1774414992_A3D807F7 | 504990 | 665 | -83.4 | 504990 | 408 | -89.3 | 504990 | 819 | -85.9 | 504990 | 638 |
| MR_1774414992_4CF2E058 | 504990 | 665 | -84.1 | 504990 | 408 | -88.5 | 504990 | 819 | -86.6 | 504990 | 638 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1204: `a920f86c-b99...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `a920f86c-b99b-4cfd-8896-f0dce4fb38e5` |
| Tag | **single-answer** |
| 정답 | **C18** |
| C18 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3247359_1 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1204] topology](images/train_1204.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3219520_4
- `C2`: Lift the tilt angle of 3247359_1 by 3 degrees
- `C3`: Increase transmission power for 3247359_1
- `C4`: Increase A3 Offset threshold for 3247359_1
- `C5`: Decrease A3 Offset threshold for 3247359_1
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3247359_1
- `C7`: Decrease transmission power for 3219520_4
- `C8`: Check test server and transmission issues
- `C9`: Adjust the azimuth of 3219520_4 by 37 degrees
- `C10`: Lift the tilt angle  of 3219520_4 by 1 degrees
- `C11`: Press down the tilt angle  of 3219520_4 by 1 degrees
- `C12`: Insufficient data; more data is needed for judgment.
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3219520_4
- `C14`: Press down the tilt angle of 3247359_1 by 3 degrees
- `C15`: Increase A3 Offset threshold for 3219520_4
- `C16`: Decrease transmission power for 3247359_1
- `C17`: Decrease A3 Offset threshold for 3219520_4
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3247359_1 **← 정답**
- `C19`: Add neighbor relationship between 3247359_1 and 3219520_4
- `C20`: Adjust the azimuth of 3247359_1 by 22 degrees
- `C21`: Add neighbor relationship between 3268764_13 and 3219520_4
- `C22`: Increase transmission power for 3219520_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.191 | MS1 | 121.4656600900 | 31.1446286885 | 233 | 504990 | -93.26 | 14.38 | 317.41 | 0.14 | 2.39 | 1590 |
| 2024-09-20 22:21:32.441 | MS1 | 121.4656616842 | 31.1446210231 | 849 | 504990 | -94.01 | 10.84 | 493.68 | 0.04 | 2.69 | 1561 |
| 2024-09-20 22:21:33.909 | MS1 | 121.4656657252 | 31.1446211271 | 574 | 504990 | -94.50 | 13.21 | 525.46 | 0.08 | 2.82 | 1593 |
| 2024-09-20 22:21:34.967 | MS1 | 121.4656621148 | 31.1446213230 | 139 | 152650 | -88.53 | 6.16 | 56.25 | 0.05 | 1.71 | 989 |
| 2024-09-20 22:21:35.536 | MS1 | 121.4656598319 | 31.1446313293 | 477 | 152650 | -91.85 | 4.09 | 95.74 | 0.08 | 1.92 | 921 |
| 2024-09-20 22:21:36.426 | MS1 | 121.4656673087 | 31.1446245121 | 447 | 152650 | -89.37 | 3.32 | 63.18 | 0.11 | 1.87 | 924 |
| 2024-09-20 22:21:37.668 | MS1 | 121.4656607498 | 31.1446368197 | 666 | 152650 | -90.16 | 6.67 | 75.71 | 0.00 | 1.64 | 992 |
| 2024-09-20 22:21:38.362 | MS1 | 121.4656599028 | 31.1446282055 | 139 | 152650 | -90.70 | 4.86 | 53.30 | 0.19 | 1.64 | 986 |
| 2024-09-20 22:21:39.269 | MS1 | 121.4656763250 | 31.1446202538 | 477 | 152650 | -89.22 | 6.54 | 67.60 | 0.13 | 1.84 | 914 |
| 2024-09-20 22:21:40.984 | MS1 | 121.4656715979 | 31.1446371513 | 447 | 152650 | -95.73 | 5.46 | 51.36 | 0.19 | 2.68 | 1590 |
| 2024-09-20 22:21:41.717 | MS1 | 121.4656657273 | 31.1446182802 | 666 | 152650 | -94.33 | 4.69 | 57.81 | 0.18 | 2.31 | 1597 |
| 2024-09-20 22:21:42.751 | MS1 | 121.4656624449 | 31.1446272908 | 139 | 152650 | -91.14 | 4.59 | 48.56 | 0.05 | 2.69 | 1562 |

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
| 3215948 | 6 | 121.4716241832 | 31.1522226170 | 36 | 15 | 7 | 28.3 | TDD | 191 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3219520 | 4 | 121.4707862369 | 31.1536469590 | 169 | 1 | 5 | 9.7 | TDD | 278 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3225439 | 7 | 121.4701854999 | 31.1446339497 | 174 | 8 | 3 | 17.7 | FDD | 456 | n1 | 152650 | 30M | 4T4R | 24 | 152650 |
| 3230630 | 10 | 121.4653375149 | 31.1491361612 | 42 | 5 | 12 | 4.8 | FDD | 915 | n1 | 152650 | 30M | 4T4R | 27 | 152650 |
| 3232080 | 9 | 121.4726474759 | 31.1449974104 | 287 | 6 | 7 | 17.1 | FDD | 139 | n1 | 152650 | 30M | 4T4R | 24 | 152650 |
| 3237223 | 8 | 121.4677913942 | 31.1518773166 | 299 | 8 | 6 | 13.8 | FDD | 40 | n1 | 152650 | 30M | 4T4R | 22 | 152650 |
| 3238385 | 2 | 121.4680553030 | 31.1461795496 | 59 | 15 | 1 | 18.7 | TDD | 976 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3239493 | 12 | 121.4719417468 | 31.1473685534 | 351 | 1 | 6 | 9.1 | FDD | 477 | n1 | 152650 | 30M | 4T4R | 18 | 152650 |
| 3243873 | 3 | 121.4692207482 | 31.1544568676 | 255 | 14 | 9 | 0.1 | TDD | 849 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3247359 | 1 | 121.4724369825 | 31.1539253447 | 190 | 2 | 7 | 27.4 | TDD | 233 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3248325 | 11 | 121.4747768749 | 31.1519762134 | 94 | 0 | 0 | 29.9 | FDD | 666 | n1 | 152650 | 30M | 4T4R | 29 | 152650 |
| 3268764 | 13 | 121.4688662212 | 31.1537474584 | 87 | 6 | 11 | 1.7 | FDD | 447 | n1 | 152650 | 30M | 4T4R | 23 | 152650 |
| 3273500 | 5 | 121.4710392082 | 31.1488405122 | 108 | 5 | 0 | 16.4 | TDD | 574 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:31.236 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.261 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.383 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.383 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.135 | NREventA2 | measId:1;ServCellPCI:878;Se... |
| 2024-09-20 22:21:35.267 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.479 | NREventA5 | measId:3;ServCellPCI:878;Se... |
| 2024-09-20 22:21:35.550 | NRHandoverAttempt | SourcePCI:878;SourceNR-ARFC... |
| 2024-09-20 22:21:35.573 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.585 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:35.719 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.719 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3247359 | 1 | 10.7180 | 8.3746 | -117.5614 | 8.1311 | 82.6335 | 0.0120 | 0.0026 |
| 2024_09_20 22:00 | 3238385 | 2 | 10.9618 | 18.2291 | -115.7544 | 19.6630 | 136.2548 | 0.0156 | 0.0141 |
| 2024_09_20 22:00 | 3243873 | 3 | 16.8426 | 17.5830 | -114.8926 | 17.6030 | 97.4539 | 0.0074 | 0.0139 |
| 2024_09_20 22:00 | 3219520 | 4 | 8.3478 | 9.3600 | -116.9856 | 5.1369 | 145.3362 | 0.0188 | 0.0185 |
| 2024_09_20 22:00 | 3273500 | 5 | 18.4791 | 5.2708 | -116.9791 | 15.4386 | 183.3407 | 0.0029 | 0.0078 |
| 2024_09_20 22:00 | 3215948 | 6 | 5.1018 | 12.0764 | -116.0777 | 14.7281 | 101.5974 | 0.0041 | 0.0117 |
| 2024_09_20 22:00 | 3225439 | 7 | 18.7758 | 12.1617 | -117.6483 | 4.8719 | 23.0162 | 0.0100 | 0.0177 |
| 2024_09_20 22:00 | 3237223 | 8 | 19.4138 | 5.5844 | -114.4520 | 4.7099 | 57.6362 | 0.0190 | 0.0196 |
| 2024_09_20 22:00 | 3232080 | 9 | 7.5662 | 17.1062 | -117.1140 | 3.5357 | 43.6093 | 0.0188 | 0.0009 |
| 2024_09_20 22:00 | 3230630 | 10 | 14.4946 | 19.8913 | -116.8234 | 3.0687 | 40.5157 | 0.0025 | 0.0104 |
| 2024_09_20 22:00 | 3248325 | 11 | 18.9490 | 19.9712 | -115.7155 | 4.7653 | 42.5518 | 0.0039 | 0.0086 |
| 2024_09_20 22:00 | 3239493 | 12 | 9.5825 | 17.4036 | -114.7897 | 3.0165 | 27.9272 | 0.0171 | 0.0053 |
| 2024_09_20 22:00 | 3268764 | 13 | 14.2383 | 7.7544 | -116.8467 | 3.0791 | 37.9409 | 0.0105 | 0.0188 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413234_9E17940B | 152650 | 139 | -89.4 | 152650 | 456 | -94.6 | 152650 | 40 | -100.7 | 152650 | 915 |
| MR_1774413234_E50B9F70 | 504990 | 574 | -95.1 | 504990 | 278 | -92.0 | 504990 | 976 | -93.0 | 504990 | 191 |
| MR_1774413234_79985062 | 504990 | 574 | -92.6 | 504990 | 278 | -92.3 | 504990 | 976 | -93.9 | 504990 | 191 |
| MR_1774413234_03C31E08 | 152650 | 139 | -88.4 | 152650 | 456 | -94.5 | 152650 | 40 | -100.7 | 152650 | 915 |
| MR_1774413234_F8207038 | 504990 | 574 | -94.8 | 504990 | 278 | -88.9 | 504990 | 976 | -96.4 | 504990 | 191 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1205: `6fe3bcb3-662...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `6fe3bcb3-6627-422d-aa5c-c5fd0a44070c` |
| Tag | **single-answer** |
| 정답 | **C7** |
| C7 의미 | Add neighbor relationship between 3264326_2 and 3248705_3 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1205] topology](images/train_1205.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3264326_2
- `C2`: Adjust the azimuth of 3264326_2 by 50 degrees
- `C3`: Press down the tilt angle of 3264326_2 by 10 degrees
- `C4`: Increase transmission power for 3248705_3
- `C5`: Increase A3 Offset threshold for 3248705_3
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3248705_3
- `C7`: Add neighbor relationship between 3264326_2 and 3248705_3 **← 정답**
- `C8`: Decrease transmission power for 3248705_3
- `C9`: Lift the tilt angle  of 3248705_3 by 4 degrees
- `C10`: Add neighbor relationship between 3221035_1 and 3248705_3
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3248705_3
- `C12`: Check test server and transmission issues
- `C13`: Lift the tilt angle of 3264326_2 by 10 degrees
- `C14`: Adjust the azimuth of 3248705_3 by 13 degrees
- `C15`: Increase transmission power for 3264326_2
- `C16`: Press down the tilt angle  of 3248705_3 by 4 degrees
- `C17`: Insufficient data; more data is needed for judgment.
- `C18`: Decrease transmission power for 3264326_2
- `C19`: Decrease A3 Offset threshold for 3248705_3
- `C20`: Increase A3 Offset threshold for 3264326_2
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3264326_2
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3264326_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.662 | MS1 | 121.4656771232 | 31.1446373631 | 857 | 504990 | -79.78 | 14.39 | 478.12 | 0.08 | 2.32 | 1564 |
| 2024-09-20 22:21:32.261 | MS1 | 121.4656590792 | 31.1446231996 | 857 | 504990 | -81.17 | 17.71 | 465.58 | 0.08 | 2.87 | 1586 |
| 2024-09-20 22:21:33.441 | MS1 | 121.4656604054 | 31.1446264762 | 857 | 504990 | -84.48 | 17.02 | 291.58 | 0.14 | 2.95 | 1592 |
| 2024-09-20 22:21:34.760 | MS1 | 121.4656725377 | 31.1446201882 | 857 | 504990 | -88.97 | -3.22 | 53.66 | 0.16 | 1.42 | 1579 |
| 2024-09-20 22:21:35.286 | MS1 | 121.4656740928 | 31.1446318118 | 857 | 504990 | -85.70 | -3.45 | 42.91 | 0.10 | 1.33 | 1570 |
| 2024-09-20 22:21:36.839 | MS1 | 121.4656724453 | 31.1446291066 | 857 | 504990 | -92.92 | -3.71 | 47.85 | 0.01 | 1.48 | 1565 |
| 2024-09-20 22:21:37.348 | MS1 | 121.4656596512 | 31.1446307230 | 857 | 504990 | -90.57 | -0.77 | 72.65 | 0.18 | 1.15 | 1560 |
| 2024-09-20 22:21:38.591 | MS1 | 121.4656668759 | 31.1446288698 | 857 | 504990 | -76.17 | 15.11 | 378.98 | 0.17 | 1.41 | 1561 |
| 2024-09-20 22:21:39.603 | MS1 | 121.4656742946 | 31.1446260444 | 857 | 504990 | -76.52 | 17.50 | 555.16 | 0.05 | 1.18 | 1583 |
| 2024-09-20 22:21:40.299 | MS1 | 121.4656706814 | 31.1446271750 | 857 | 504990 | -76.53 | 15.60 | 448.02 | 0.08 | 2.22 | 1570 |
| 2024-09-20 22:21:41.368 | MS1 | 121.4656719401 | 31.1446190860 | 857 | 504990 | -82.57 | 13.16 | 508.60 | 0.07 | 2.81 | 1575 |
| 2024-09-20 22:21:42.811 | MS1 | 121.4656699891 | 31.1446349673 | 857 | 504990 | -80.72 | 14.41 | 524.72 | 0.05 | 2.44 | 1598 |

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
| 3221035 | 1 | 121.4715392299 | 31.1521706078 | 176 | 3 | 1 | 36.9 | TDD | 256 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3248705 | 3 | 121.4648999830 | 31.1553666141 | 189 | 2 | 7 | 45.2 | TDD | 170 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3264326 | 2 | 121.4690475314 | 31.1524402198 | 41 | 14 | 1 | 45.1 | TDD | 857 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3267997 | 4 | 121.4706991607 | 31.1521564809 | 21 | 9 | 8 | 40.8 | TDD | 750 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:31.227 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.242 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.378 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.378 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.042 | NREventA3 | measId:2;ServCellPCI:299;Se... |
| 2024-09-20 22:21:36.042 | NREventA3 | measId:2;ServCellPCI:299;Se... |
| 2024-09-20 22:21:37.042 | NREventA3 | measId:2;ServCellPCI:299;Se... |
| 2024-09-20 22:21:39.542 | NRRRCReestablishAttempt | PCI:299 |
| 2024-09-20 22:21:39.553 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.567 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:39.697 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.697 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3221035 | 1 | 19.8110 | 8.7094 | -117.7404 | 16.5232 | 140.0173 | 0.0160 | 0.0036 |
| 2024_09_20 22:00 | 3264326 | 2 | 17.7264 | 13.5051 | -117.2577 | 13.8891 | 164.0809 | 0.0192 | 0.1833 |
| 2024_09_20 22:00 | 3248705 | 3 | 14.3828 | 9.3458 | -114.1135 | 10.2126 | 175.8250 | 0.0018 | 0.0187 |
| 2024_09_20 22:00 | 3267997 | 4 | 11.2455 | 12.0691 | -116.7606 | 16.8841 | 121.6686 | 0.0136 | 0.0032 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412198_D6A20CC9 | 504990 | 857 | -90.2 | 504990 | 170 | -82.0 | 504990 | 256 | -91.6 | 504990 | 750 |
| MR_1774412198_009DB046 | 504990 | 170 | -83.8 | 504990 | 857 | -90.2 | 504990 | 256 | -89.6 | 504990 | 750 |
| MR_1774412198_9B0A25BA | 504990 | 170 | -83.3 | 504990 | 857 | -89.3 | 504990 | 256 | -88.0 | 504990 | 750 |
| MR_1774412198_4CF31CBF | 504990 | 857 | -90.9 | 504990 | 170 | -81.4 | 504990 | 256 | -88.2 | 504990 | 750 |
| MR_1774412198_C3014388 | 504990 | 857 | -89.3 | 504990 | 170 | -83.8 | 504990 | 256 | -88.2 | 504990 | 750 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1206: `1a47dec7-a77...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `1a47dec7-a775-4af9-bee3-72323167bb90` |
| Tag | **single-answer** |
| 정답 | **C4** |
| C4 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1206] topology](images/train_1206.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3226399_2 by 50 degrees
- `C2`: Insufficient data; more data is needed for judgment.
- `C3`: Lift the tilt angle  of 3271560_4 by 10 degrees
- `C4`: Check test server and transmission issues **← 정답**
- `C5`: Press down the tilt angle  of 3271560_4 by 10 degrees
- `C6`: Press down the tilt angle of 3226399_2 by 10 degrees
- `C7`: Decrease A3 Offset threshold for 3271560_4
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3226399_2
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3271560_4
- `C10`: Increase A3 Offset threshold for 3271560_4
- `C11`: Decrease transmission power for 3271560_4
- `C12`: Adjust the azimuth of 3271560_4 by 50 degrees
- `C13`: Add neighbor relationship between 3226399_2 and 3271560_4
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3226399_2
- `C15`: Increase transmission power for 3226399_2
- `C16`: Lift the tilt angle of 3226399_2 by 10 degrees
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3271560_4
- `C18`: Decrease transmission power for 3226399_2
- `C19`: Increase transmission power for 3271560_4
- `C20`: Add neighbor relationship between 3258178_1 and 3271560_4
- `C21`: Increase A3 Offset threshold for 3226399_2
- `C22`: Decrease A3 Offset threshold for 3226399_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.675 | MS1 | 121.4656765923 | 31.1446242018 | 857 | 504990 | -85.83 | 15.84 | 395.42 | 0.17 | 2.58 | 1560 |
| 2024-09-20 22:21:32.487 | MS1 | 121.4656664840 | 31.1446235141 | 857 | 504990 | -86.68 | 12.59 | 534.48 | 0.14 | 2.24 | 1570 |
| 2024-09-20 22:21:33.483 | MS1 | 121.4656636194 | 31.1446363831 | 857 | 504990 | -86.78 | 12.97 | 560.86 | 0.13 | 2.88 | 1584 |
| 2024-09-20 22:21:34.243 | MS1 | 121.4656739228 | 31.1446352565 | 857 | 504990 | -85.22 | 17.49 | 98.10 | 0.19 | 2.94 | 429 |
| 2024-09-20 22:21:35.778 | MS1 | 121.4656709377 | 31.1446255305 | 857 | 504990 | -91.28 | 15.48 | 69.69 | 0.17 | 2.42 | 454 |
| 2024-09-20 22:21:36.985 | MS1 | 121.4656685401 | 31.1446209242 | 857 | 504990 | -90.52 | 16.73 | 77.34 | 0.02 | 2.21 | 440 |
| 2024-09-20 22:21:37.320 | MS1 | 121.4656668499 | 31.1446241820 | 857 | 504990 | -91.80 | 7.65 | 76.39 | 0.03 | 2.19 | 328 |
| 2024-09-20 22:21:38.934 | MS1 | 121.4656670656 | 31.1446183827 | 857 | 504990 | -90.49 | 12.30 | 60.46 | 0.15 | 2.39 | 356 |
| 2024-09-20 22:21:39.111 | MS1 | 121.4656678495 | 31.1446353124 | 857 | 504990 | -89.93 | 8.26 | 64.24 | 0.18 | 2.94 | 386 |
| 2024-09-20 22:21:40.310 | MS1 | 121.4656706024 | 31.1446223162 | 857 | 504990 | -91.56 | 10.41 | 529.33 | 0.11 | 2.02 | 1599 |
| 2024-09-20 22:21:41.728 | MS1 | 121.4656730823 | 31.1446231516 | 857 | 504990 | -89.63 | 8.01 | 590.88 | 0.13 | 2.84 | 1587 |
| 2024-09-20 22:21:42.845 | MS1 | 121.4656644940 | 31.1446248328 | 857 | 504990 | -93.04 | 12.12 | 413.48 | 0.10 | 2.74 | 1575 |

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
| 3226399 | 2 | 121.4649482722 | 31.1485100945 | 20 | 10 | 12 | 31.9 | TDD | 857 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3238164 | 3 | 121.4675204692 | 31.1520324202 | 221 | 0 | 4 | 24.1 | TDD | 282 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3258178 | 1 | 121.4758362785 | 31.1452291442 | 63 | 12 | 11 | 26.3 | TDD | 168 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3271560 | 4 | 121.4697003891 | 31.1546599182 | 42 | 11 | 5 | 17.0 | TDD | 355 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |

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
| 2024-09-20 22:21:30.821 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.840 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:30.976 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.976 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.672 | NREventA3 | measId:2;ServCellPCI:44;Ser... |
| 2024-09-20 22:21:37.912 | NRHandoverAttempt | SourcePCI:44;SourceNR-ARFCN... |
| 2024-09-20 22:21:37.948 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.958 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.098 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.098 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3258178 | 1 | 9.0300 | 17.9512 | -115.4045 | 15.4575 | 165.0486 | 0.0171 | 0.0112 |
| 2024_09_20 22:00 | 3226399 | 2 | 7.9254 | 15.6875 | -114.7253 | 15.8204 | 93.4279 | 0.0075 | 0.0120 |
| 2024_09_20 22:00 | 3238164 | 3 | 19.2258 | 15.4068 | -114.6709 | 14.3683 | 171.7001 | 0.0141 | 0.0098 |
| 2024_09_20 22:00 | 3271560 | 4 | 13.9153 | 10.5801 | -117.1092 | 12.8090 | 184.1866 | 0.0165 | 0.0135 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413695_2FA3DB44 | 504990 | 857 | -84.7 | 504990 | 355 | -90.7 | 504990 | 168 | -100.6 | 504990 | 282 |
| MR_1774413695_96E2FFCB | 504990 | 857 | -85.9 | 504990 | 355 | -89.6 | 504990 | 168 | -100.2 | 504990 | 282 |
| MR_1774413695_64F80370 | 504990 | 857 | -85.1 | 504990 | 355 | -91.3 | 504990 | 168 | -97.0 | 504990 | 282 |
| MR_1774413695_6DBC2006 | 504990 | 857 | -84.6 | 504990 | 355 | -90.6 | 504990 | 168 | -96.9 | 504990 | 282 |
| MR_1774413695_859472E0 | 504990 | 857 | -86.5 | 504990 | 355 | -90.8 | 504990 | 168 | -96.9 | 504990 | 282 |
| MR_1774413695_6D36163B | 504990 | 857 | -83.5 | 504990 | 355 | -88.8 | 504990 | 168 | -98.9 | 504990 | 282 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1207: `163e0528-3fe...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `163e0528-3fe7-47dc-a2c3-660ff04277b0` |
| Tag | **single-answer** |
| 정답 | **C4** |
| C4 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3273143_4 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1207] topology](images/train_1207.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3273143_4 by 2 degrees
- `C2`: Adjust the azimuth of 3279575_3 by 37 degrees
- `C3`: Lift the tilt angle  of 3279575_3 by 4 degrees
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3273143_4 **← 정답**
- `C5`: Increase A3 Offset threshold for 3273143_4
- `C6`: Adjust the azimuth of 3273143_4 by 46 degrees
- `C7`: Decrease transmission power for 3273143_4
- `C8`: Lift the tilt angle of 3273143_4 by 2 degrees
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3273143_4
- `C10`: Decrease transmission power for 3279575_3
- `C11`: Decrease A3 Offset threshold for 3273143_4
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3279575_3
- `C13`: Insufficient data; more data is needed for judgment.
- `C14`: Decrease A3 Offset threshold for 3279575_3
- `C15`: Check test server and transmission issues
- `C16`: Increase A3 Offset threshold for 3279575_3
- `C17`: Add neighbor relationship between 3227608_7 and 3279575_3
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3279575_3
- `C19`: Add neighbor relationship between 3273143_4 and 3279575_3
- `C20`: Press down the tilt angle  of 3279575_3 by 4 degrees
- `C21`: Increase transmission power for 3273143_4
- `C22`: Increase transmission power for 3279575_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.436 | MS1 | 121.4656635591 | 31.1446324346 | 851 | 504990 | -95.99 | 10.84 | 399.61 | 0.18 | 2.90 | 1566 |
| 2024-09-20 22:21:32.450 | MS1 | 121.4656669358 | 31.1446281446 | 503 | 504990 | -95.59 | 10.37 | 544.99 | 0.00 | 2.93 | 1565 |
| 2024-09-20 22:21:33.926 | MS1 | 121.4656740464 | 31.1446349929 | 198 | 504990 | -94.52 | 10.34 | 524.46 | 0.18 | 2.55 | 1584 |
| 2024-09-20 22:21:34.226 | MS1 | 121.4656598926 | 31.1446263174 | 272 | 152650 | -96.46 | 2.87 | 73.82 | 0.17 | 1.78 | 934 |
| 2024-09-20 22:21:35.699 | MS1 | 121.4656713031 | 31.1446260539 | 63 | 152650 | -93.82 | 3.96 | 84.65 | 0.09 | 1.55 | 927 |
| 2024-09-20 22:21:36.774 | MS1 | 121.4656752530 | 31.1446274485 | 747 | 152650 | -94.71 | 6.37 | 66.12 | 0.03 | 1.72 | 963 |
| 2024-09-20 22:21:37.375 | MS1 | 121.4656652474 | 31.1446322282 | 819 | 152650 | -88.95 | 2.72 | 73.38 | 0.08 | 1.68 | 918 |
| 2024-09-20 22:21:38.283 | MS1 | 121.4656638880 | 31.1446341063 | 272 | 152650 | -90.78 | 5.64 | 83.28 | 0.06 | 1.64 | 919 |
| 2024-09-20 22:21:39.933 | MS1 | 121.4656666611 | 31.1446283892 | 63 | 152650 | -94.09 | 2.16 | 81.43 | 0.20 | 1.93 | 958 |
| 2024-09-20 22:21:40.894 | MS1 | 121.4656687964 | 31.1446219963 | 747 | 152650 | -90.61 | 3.06 | 82.70 | 0.15 | 2.04 | 1572 |
| 2024-09-20 22:21:41.186 | MS1 | 121.4656696410 | 31.1446317295 | 819 | 152650 | -88.87 | 7.81 | 88.31 | 0.03 | 2.83 | 1566 |
| 2024-09-20 22:21:42.108 | MS1 | 121.4656670104 | 31.1446209232 | 272 | 152650 | -92.38 | 2.09 | 97.83 | 0.14 | 2.61 | 1569 |

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
| 3212218 | 5 | 121.4662835054 | 31.1440443296 | 171 | 10 | 7 | 4.5 | TDD | 503 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3227608 | 7 | 121.4697022497 | 31.1539463422 | 341 | 15 | 10 | 26.3 | FDD | 747 | n1 | 152650 | 30M | 4T4R | 15 | 152650 |
| 3237506 | 2 | 121.4722364840 | 31.1481208373 | 304 | 10 | 3 | 29.1 | TDD | 198 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3238192 | 11 | 121.4694576788 | 31.1514387483 | 249 | 0 | 1 | 25.2 | FDD | 278 | n1 | 152650 | 30M | 4T4R | 15 | 152650 |
| 3240444 | 1 | 121.4746155972 | 31.1485625414 | 15 | 14 | 1 | 13.2 | TDD | 677 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3241905 | 6 | 121.4719331051 | 31.1485513268 | 72 | 1 | 8 | 29.2 | TDD | 247 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3250735 | 8 | 121.4730491343 | 31.1478832697 | 75 | 2 | 10 | 19.8 | FDD | 1005 | n1 | 152650 | 30M | 4T4R | 30 | 152650 |
| 3266638 | 13 | 121.4717420230 | 31.1479588733 | 269 | 1 | 9 | 15.1 | FDD | 63 | n1 | 152650 | 30M | 4T4R | 21 | 152650 |
| 3268430 | 12 | 121.4642792233 | 31.1559711058 | 224 | 6 | 5 | 10.0 | FDD | 854 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |
| 3271052 | 10 | 121.4748440871 | 31.1496581404 | 154 | 14 | 9 | 25.1 | FDD | 819 | n1 | 152650 | 30M | 4T4R | 27 | 152650 |
| 3273143 | 4 | 121.4676902030 | 31.1495251427 | 245 | 0 | 4 | 19.8 | TDD | 851 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3279318 | 9 | 121.4709388154 | 31.1494896737 | 278 | 14 | 4 | 14.6 | FDD | 272 | n1 | 152650 | 30M | 4T4R | 18 | 152650 |
| 3279575 | 3 | 121.4734392124 | 31.1448748407 | 231 | 2 | 5 | 21.1 | TDD | 108 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |

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
| 2024-09-20 22:21:31.488 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.610 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.610 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.346 | NREventA2 | measId:1;ServCellPCI:491;Se... |
| 2024-09-20 22:21:35.456 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.745 | NREventA5 | measId:3;ServCellPCI:491;Se... |
| 2024-09-20 22:21:35.781 | NRHandoverAttempt | SourcePCI:491;SourceNR-ARFC... |
| 2024-09-20 22:21:35.812 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.823 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:35.963 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.963 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3240444 | 1 | 12.2452 | 6.1628 | -116.7945 | 13.4627 | 165.5760 | 0.0040 | 0.0153 |
| 2024_09_20 22:00 | 3237506 | 2 | 6.9666 | 10.8485 | -116.3103 | 7.8354 | 148.7792 | 0.0040 | 0.0012 |
| 2024_09_20 22:00 | 3279575 | 3 | 5.3608 | 9.8865 | -114.7796 | 17.8233 | 125.4840 | 0.0174 | 0.0082 |
| 2024_09_20 22:00 | 3273143 | 4 | 9.2720 | 17.8665 | -114.4518 | 10.0391 | 131.1540 | 0.0005 | 0.0003 |
| 2024_09_20 22:00 | 3212218 | 5 | 11.3336 | 14.9572 | -116.5618 | 7.1020 | 112.3867 | 0.0055 | 0.0188 |
| 2024_09_20 22:00 | 3241905 | 6 | 15.3347 | 6.9481 | -115.7807 | 11.3159 | 115.4435 | 0.0017 | 0.0021 |
| 2024_09_20 22:00 | 3227608 | 7 | 7.8360 | 12.9648 | -117.9720 | 4.9781 | 21.9465 | 0.0057 | 0.0169 |
| 2024_09_20 22:00 | 3250735 | 8 | 12.1203 | 19.1625 | -115.3221 | 4.1325 | 26.4302 | 0.0190 | 0.0162 |
| 2024_09_20 22:00 | 3279318 | 9 | 8.2037 | 16.6534 | -116.4365 | 3.9199 | 52.1238 | 0.0199 | 0.0043 |
| 2024_09_20 22:00 | 3271052 | 10 | 11.8788 | 15.0210 | -115.6893 | 4.9448 | 43.3069 | 0.0174 | 0.0054 |
| 2024_09_20 22:00 | 3238192 | 11 | 17.5780 | 17.2185 | -117.4671 | 3.8458 | 35.8383 | 0.0098 | 0.0027 |
| 2024_09_20 22:00 | 3268430 | 12 | 9.4816 | 14.4054 | -114.7219 | 4.5096 | 35.6041 | 0.0170 | 0.0078 |
| 2024_09_20 22:00 | 3266638 | 13 | 8.8154 | 13.7895 | -114.4640 | 4.9714 | 47.0497 | 0.0143 | 0.0151 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416637_963C8EA7 | 152650 | 272 | -96.9 | 152650 | 1005 | -102.6 | 152650 | 278 | -102.4 | 152650 | 854 |
| MR_1774416637_D496D169 | 152650 | 272 | -95.7 | 152650 | 1005 | -101.6 | 152650 | 278 | -104.5 | 152650 | 854 |
| MR_1774416637_0AD3E046 | 152650 | 272 | -94.6 | 152650 | 1005 | -101.0 | 152650 | 278 | -102.3 | 152650 | 854 |
| MR_1774416637_84066E2D | 504990 | 198 | -94.2 | 504990 | 108 | -91.4 | 504990 | 677 | -94.6 | 504990 | 247 |
| MR_1774416637_D62EAF7B | 504990 | 198 | -93.6 | 504990 | 108 | -92.9 | 504990 | 677 | -94.8 | 504990 | 247 |
| MR_1774416637_F86F31BA | 504990 | 198 | -94.6 | 504990 | 108 | -91.0 | 504990 | 677 | -94.2 | 504990 | 247 |
| MR_1774416637_5A0D63B5 | 152650 | 272 | -97.5 | 152650 | 1005 | -101.8 | 152650 | 278 | -102.0 | 152650 | 854 |
| MR_1774416637_8AC85ED0 | 504990 | 198 | -93.4 | 504990 | 108 | -92.7 | 504990 | 677 | -94.7 | 504990 | 247 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1208: `a1fddc2f-8c0...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `a1fddc2f-8c03-408e-8968-48cf70c9f11a` |
| Tag | **single-answer** |
| 정답 | **C12** |
| C12 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1208] topology](images/train_1208.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3227859_1
- `C2`: Increase A3 Offset threshold for 3227859_1
- `C3`: Increase A3 Offset threshold for 3236747_4
- `C4`: Add neighbor relationship between 3230189_3 and 3227859_1
- `C5`: Adjust the azimuth of 3227859_1 by 20 degrees
- `C6`: Decrease transmission power for 3236747_4
- `C7`: Lift the tilt angle of 3236747_4 by 3 degrees
- `C8`: Add neighbor relationship between 3236747_4 and 3227859_1
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3236747_4
- `C10`: Increase transmission power for 3236747_4
- `C11`: Decrease transmission power for 3227859_1
- `C12`: Insufficient data; more data is needed for judgment. **← 정답**
- `C13`: Decrease A3 Offset threshold for 3236747_4
- `C14`: Decrease A3 Offset threshold for 3227859_1
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3236747_4
- `C16`: Press down the tilt angle of 3236747_4 by 3 degrees
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3227859_1
- `C18`: Increase transmission power for 3227859_1
- `C19`: Lift the tilt angle  of 3227859_1 by 4 degrees
- `C20`: Adjust the azimuth of 3236747_4 by 50 degrees
- `C21`: Press down the tilt angle  of 3227859_1 by 4 degrees
- `C22`: Check test server and transmission issues

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.553 | MS1 | 121.4656730933 | 31.1446376107 | 78 | 504990 | -86.17 | 12.22 | 388.09 | 0.07 | 2.47 | 1599 |
| 2024-09-20 22:21:32.844 | MS1 | 121.4656720517 | 31.1446362938 | 78 | 504990 | -88.85 | 14.55 | 495.10 | 0.15 | 2.07 | 1576 |
| 2024-09-20 22:21:33.899 | MS1 | 121.4656734295 | 31.1446213552 | 78 | 504990 | -88.71 | 13.37 | 409.32 | 0.03 | 2.01 | 1595 |
| 2024-09-20 22:21:34.885 | MS1 | 121.4656761115 | 31.1446184717 | 78 | 504990 | -91.41 | 16.52 | 87.18 | 0.20 | 2.23 | 1572 |
| 2024-09-20 22:21:35.774 | MS1 | 121.4656754253 | 31.1446236050 | 78 | 504990 | -86.74 | 12.74 | 56.21 | 0.02 | 2.13 | 1568 |
| 2024-09-20 22:21:36.574 | MS1 | 121.4656589706 | 31.1446281037 | 78 | 504990 | -86.06 | 14.28 | 84.35 | 0.18 | 2.05 | 1564 |
| 2024-09-20 22:21:37.833 | MS1 | 121.4656629666 | 31.1446193538 | 78 | 504990 | -92.25 | 10.14 | 68.43 | 0.04 | 2.28 | 1569 |
| 2024-09-20 22:21:38.799 | MS1 | 121.4656740106 | 31.1446196223 | 78 | 504990 | -91.61 | 10.93 | 87.95 | 0.08 | 2.01 | 1582 |
| 2024-09-20 22:21:39.205 | MS1 | 121.4656732760 | 31.1446286999 | 78 | 504990 | -92.14 | 10.60 | 63.06 | 0.07 | 2.36 | 1598 |
| 2024-09-20 22:21:40.830 | MS1 | 121.4656747061 | 31.1446271110 | 78 | 504990 | -93.74 | 7.77 | 554.23 | 0.06 | 2.15 | 1580 |
| 2024-09-20 22:21:41.434 | MS1 | 121.4656624565 | 31.1446356122 | 78 | 504990 | -93.59 | 7.37 | 458.88 | 0.11 | 2.28 | 1589 |
| 2024-09-20 22:21:42.362 | MS1 | 121.4656591196 | 31.1446285981 | 78 | 504990 | -89.87 | 9.04 | 462.47 | 0.20 | 2.66 | 1598 |

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
| 3227203 | 2 | 121.4729565968 | 31.1523059034 | 214 | 14 | 11 | 38.7 | TDD | 875 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3227859 | 1 | 121.4737570285 | 31.1442213125 | 293 | 2 | 1 | 31.5 | TDD | 705 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3230189 | 3 | 121.4659874490 | 31.1515597965 | 203 | 6 | 6 | 47.1 | TDD | 299 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3236747 | 4 | 121.4694539128 | 31.1550272718 | 90 | 1 | 9 | 38.3 | TDD | 78 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |

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
| 2024-09-20 22:21:31.040 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.061 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.181 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.181 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.923 | NREventA3 | measId:2;ServCellPCI:717;Se... |
| 2024-09-20 22:21:38.163 | NRHandoverAttempt | SourcePCI:717;SourceNR-ARFC... |
| 2024-09-20 22:21:38.196 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.209 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.331 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.331 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3227859 | 1 | 94.1263 | 90.7135 | -114.3682 | 9.2870 | 137.7759 | 0.0040 | 0.0083 |
| 2024_09_19 22:00 | 3227203 | 2 | 85.3431 | 92.1297 | -114.0444 | 6.4386 | 183.7282 | 0.0088 | 0.0056 |
| 2024_09_19 22:00 | 3230189 | 3 | 87.7987 | 82.2974 | -114.3514 | 11.3718 | 98.6508 | 0.0117 | 0.0186 |
| 2024_09_19 22:00 | 3236747 | 4 | 88.0228 | 76.1712 | -117.8908 | 5.2529 | 118.6940 | 0.0031 | 0.0127 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412806_1DF4C3C7 | 504990 | 78 | -92.6 | 504990 | 705 | -100.2 | 504990 | 299 | -105.1 | 504990 | 875 |
| MR_1774412806_E6D6F87B | 504990 | 78 | -91.3 | 504990 | 705 | -98.7 | 504990 | 299 | -108.3 | 504990 | 875 |
| MR_1774412806_CDB49758 | 504990 | 78 | -92.6 | 504990 | 705 | -98.9 | 504990 | 299 | -108.3 | 504990 | 875 |
| MR_1774412806_9DBAB727 | 504990 | 78 | -91.2 | 504990 | 705 | -99.3 | 504990 | 299 | -106.6 | 504990 | 875 |
| MR_1774412806_6252993F | 504990 | 78 | -90.6 | 504990 | 705 | -98.3 | 504990 | 299 | -106.8 | 504990 | 875 |
| MR_1774412806_8324E3D7 | 504990 | 78 | -90.2 | 504990 | 705 | -99.3 | 504990 | 299 | -107.3 | 504990 | 875 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1209: `7a021f13-b6e...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `7a021f13-b6eb-4cfb-96f8-265b2f417f23` |
| Tag | **single-answer** |
| 정답 | **C19** |
| C19 의미 | Lift the tilt angle  of 3220793_3 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1209] topology](images/train_1209.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3277537_1
- `C2`: Increase A3 Offset threshold for 3277537_1
- `C3`: Add neighbor relationship between 3220793_3 and 3220834_2
- `C4`: Decrease A3 Offset threshold for 3277537_1
- `C5`: Increase transmission power for 3220834_2
- `C6`: Decrease transmission power for 3277537_1
- `C7`: Decrease A3 Offset threshold for 3220834_2
- `C8`: Adjust the azimuth of 3277537_1 by 7 degrees
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3220834_2
- `C10`: Lift the tilt angle of 3277537_1 by 2 degrees
- `C11`: Press down the tilt angle  of 3220793_3 by 10 degrees
- `C12`: Insufficient data; more data is needed for judgment.
- `C13`: Press down the tilt angle of 3277537_1 by 2 degrees
- `C14`: Increase A3 Offset threshold for 3220834_2
- `C15`: Check test server and transmission issues
- `C16`: Decrease transmission power for 3220834_2
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3220834_2
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3277537_1
- `C19`: Lift the tilt angle  of 3220793_3 by 10 degrees **← 정답**
- `C20`: Add neighbor relationship between 3277537_1 and 3220834_2
- `C21`: Adjust the azimuth of 3220793_3 by 28 degrees
- `C22`: Increase transmission power for 3277537_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.289 | MS1 | 121.4656665412 | 31.1446296172 | 634 | 504990 | -85.46 | 13.24 | 386.46 | 0.17 | 2.40 | 1581 |
| 2024-09-20 22:21:32.450 | MS1 | 121.4656743069 | 31.1446339428 | 634 | 504990 | -91.79 | 14.61 | 522.44 | 0.13 | 2.14 | 1592 |
| 2024-09-20 22:21:33.931 | MS1 | 121.4656721313 | 31.1446287704 | 634 | 504990 | -86.98 | 17.03 | 408.94 | 0.15 | 2.98 | 1574 |
| 2024-09-20 22:21:34.525 | MS1 | 121.4656699027 | 31.1446191323 | 634 | 504990 | -91.17 | 13.75 | 88.83 | 0.03 | 2.91 | 1584 |
| 2024-09-20 22:21:35.636 | MS1 | 121.4656671397 | 31.1446221016 | 634 | 504990 | -87.93 | 13.35 | 50.35 | 0.07 | 2.09 | 1580 |
| 2024-09-20 22:21:36.877 | MS1 | 121.4656661552 | 31.1446311996 | 634 | 504990 | -90.96 | 17.40 | 52.99 | 0.01 | 2.38 | 1564 |
| 2024-09-20 22:21:37.690 | MS1 | 121.4656759667 | 31.1446325487 | 634 | 504990 | -93.70 | 12.93 | 90.28 | 0.12 | 2.62 | 1590 |
| 2024-09-20 22:21:38.600 | MS1 | 121.4656628629 | 31.1446190258 | 634 | 504990 | -91.37 | 9.73 | 53.98 | 0.06 | 2.94 | 1566 |
| 2024-09-20 22:21:39.475 | MS1 | 121.4656669644 | 31.1446308510 | 634 | 504990 | -93.85 | 12.25 | 70.54 | 0.11 | 2.74 | 1600 |
| 2024-09-20 22:21:40.384 | MS1 | 121.4656658480 | 31.1446299951 | 634 | 504990 | -91.58 | 11.36 | 544.18 | 0.16 | 2.56 | 1595 |
| 2024-09-20 22:21:41.935 | MS1 | 121.4656637585 | 31.1446375420 | 634 | 504990 | -91.20 | 7.06 | 526.22 | 0.17 | 2.38 | 1565 |
| 2024-09-20 22:21:42.988 | MS1 | 121.4656694563 | 31.1446305255 | 634 | 504990 | -89.97 | 7.09 | 505.11 | 0.16 | 2.24 | 1571 |

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
| 3220793 | 3 | 121.4689883128 | 31.1472515170 | 23 | 2 | 7 | 33.5 | TDD | 180 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3220834 | 2 | 121.4752329498 | 31.1537329513 | 194 | 10 | 8 | 47.8 | TDD | 436 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3240159 | 4 | 121.4748450593 | 31.1454426695 | 291 | 12 | 0 | 28.7 | TDD | 987 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3277537 | 1 | 121.4669096714 | 31.1523872048 | 195 | 1 | 4 | 15.3 | TDD | 634 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

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
| 2024-09-20 22:21:31.149 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.172 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.298 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.298 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.970 | NREventA3 | measId:2;ServCellPCI:157;Se... |
| 2024-09-20 22:21:38.210 | NRHandoverAttempt | SourcePCI:157;SourceNR-ARFC... |
| 2024-09-20 22:21:38.253 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.264 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.367 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.367 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3277537 | 1 | 89.2938 | 93.0705 | -114.4659 | 17.0263 | 163.6226 | 0.0141 | 0.0118 |
| 2024_09_20 22:00 | 3220834 | 2 | 14.2287 | 14.7214 | -116.1918 | 13.9468 | 160.9100 | 0.0194 | 0.0133 |
| 2024_09_20 22:00 | 3220793 | 3 | 6.6318 | 13.5668 | -116.1397 | 15.7352 | 104.9601 | 0.0041 | 0.0120 |
| 2024_09_20 22:00 | 3240159 | 4 | 9.1962 | 13.3996 | -117.5433 | 9.5146 | 137.4555 | 0.0009 | 0.0125 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415290_EFE20973 | 504990 | 634 | -90.6 | 504990 | 436 | -94.5 | 504990 | 180 | -98.3 | 504990 | 987 |
| MR_1774415290_7AA33B22 | 504990 | 634 | -89.6 | 504990 | 436 | -96.2 | 504990 | 180 | -99.6 | 504990 | 987 |
| MR_1774415290_6A5627FA | 504990 | 634 | -92.9 | 504990 | 436 | -94.6 | 504990 | 180 | -97.2 | 504990 | 987 |
| MR_1774415290_A4AAFC71 | 504990 | 634 | -89.5 | 504990 | 436 | -94.6 | 504990 | 180 | -100.0 | 504990 | 987 |
| MR_1774415290_0A917FFC | 504990 | 634 | -89.7 | 504990 | 436 | -93.1 | 504990 | 180 | -96.6 | 504990 | 987 |
| MR_1774415290_980FEA7C | 504990 | 634 | -91.1 | 504990 | 436 | -94.6 | 504990 | 180 | -98.3 | 504990 | 987 |
| MR_1774415290_45D7942B | 504990 | 634 | -92.3 | 504990 | 436 | -95.3 | 504990 | 180 | -97.7 | 504990 | 987 |
| MR_1774415290_3000DD1C | 504990 | 634 | -92.5 | 504990 | 436 | -96.5 | 504990 | 180 | -98.7 | 504990 | 987 |

> *... 2개 열 생략 (전체 14열)*

---
