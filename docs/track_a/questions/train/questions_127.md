# Track A 문제 분석 — train[1260]~train[1269]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[1260] ~ train[1269] (10개)

## 목차

1. [문제 1260: `cd8b74a5-55d...`](#1260) — single-answer, 정답: C15
2. [문제 1261: `bf4cb16a-9f1...`](#1261) — single-answer, 정답: C12
3. [문제 1262: `de991641-3d5...`](#1262) — single-answer, 정답: C16
4. [문제 1263: `4c47e5c2-bce...`](#1263) — single-answer, 정답: C1
5. [문제 1264: `8a756c08-6cb...`](#1264) — multiple-answer, 정답: C3|C17
6. [문제 1265: `a92730d1-558...`](#1265) — single-answer, 정답: C7
7. [문제 1266: `9ceaf783-e38...`](#1266) — single-answer, 정답: C6
8. [문제 1267: `3d8c2601-03e...`](#1267) — single-answer, 정답: C18
9. [문제 1268: `78416498-7f2...`](#1268) — single-answer, 정답: C16
10. [문제 1269: `c1d49dd3-788...`](#1269) — single-answer, 정답: C8

---

### 문제 1260: `cd8b74a5-55d...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `cd8b74a5-55d3-4de2-bf97-38db59d091a1` |
| Tag | **single-answer** |
| 정답 | **C15** |
| C15 의미 | Lift the tilt angle  of 3218357_2 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1260] topology](images/train_1260.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3262015_3
- `C2`: Press down the tilt angle  of 3218357_2 by 10 degrees
- `C3`: Increase transmission power for 3250269_4
- `C4`: Check test server and transmission issues
- `C5`: Lift the tilt angle of 3262015_3 by 2 degrees
- `C6`: Increase A3 Offset threshold for 3250269_4
- `C7`: Adjust the azimuth of 3218357_2 by 50 degrees
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3262015_3
- `C9`: Add neighbor relationship between 3218357_2 and 3250269_4
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3250269_4
- `C11`: Press down the tilt angle of 3262015_3 by 2 degrees
- `C12`: Decrease A3 Offset threshold for 3250269_4
- `C13`: Adjust the azimuth of 3262015_3 by 5 degrees
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3262015_3
- `C15`: Lift the tilt angle  of 3218357_2 by 10 degrees **← 정답**
- `C16`: Insufficient data; more data is needed for judgment.
- `C17`: Decrease A3 Offset threshold for 3262015_3
- `C18`: Increase A3 Offset threshold for 3262015_3
- `C19`: Add neighbor relationship between 3262015_3 and 3250269_4
- `C20`: Increase transmission power for 3262015_3
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3250269_4
- `C22`: Decrease transmission power for 3250269_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.319 | MS1 | 121.4656732189 | 31.1446180476 | 508 | 504990 | -85.87 | 13.31 | 513.04 | 0.12 | 2.64 | 1561 |
| 2024-09-20 22:21:32.442 | MS1 | 121.4656630866 | 31.1446329722 | 508 | 504990 | -90.34 | 15.75 | 380.00 | 0.03 | 2.63 | 1580 |
| 2024-09-20 22:21:33.231 | MS1 | 121.4656627637 | 31.1446282187 | 508 | 504990 | -91.67 | 14.46 | 508.74 | 0.16 | 2.06 | 1598 |
| 2024-09-20 22:21:34.517 | MS1 | 121.4656692753 | 31.1446240485 | 508 | 504990 | -91.01 | 14.44 | 60.12 | 0.03 | 2.99 | 1597 |
| 2024-09-20 22:21:35.608 | MS1 | 121.4656753699 | 31.1446192098 | 508 | 504990 | -90.76 | 16.61 | 80.76 | 0.17 | 2.45 | 1600 |
| 2024-09-20 22:21:36.899 | MS1 | 121.4656725884 | 31.1446222898 | 508 | 504990 | -86.73 | 17.10 | 82.66 | 0.10 | 2.72 | 1587 |
| 2024-09-20 22:21:37.282 | MS1 | 121.4656728931 | 31.1446366105 | 508 | 504990 | -91.85 | 12.85 | 56.35 | 0.09 | 2.28 | 1574 |
| 2024-09-20 22:21:38.772 | MS1 | 121.4656594743 | 31.1446292971 | 508 | 504990 | -90.09 | 9.57 | 61.10 | 0.03 | 2.97 | 1591 |
| 2024-09-20 22:21:39.126 | MS1 | 121.4656640558 | 31.1446228599 | 508 | 504990 | -89.05 | 12.41 | 65.80 | 0.02 | 2.24 | 1595 |
| 2024-09-20 22:21:40.575 | MS1 | 121.4656763836 | 31.1446244799 | 508 | 504990 | -93.86 | 12.64 | 381.05 | 0.09 | 2.01 | 1585 |
| 2024-09-20 22:21:41.492 | MS1 | 121.4656756736 | 31.1446205597 | 508 | 504990 | -92.95 | 8.07 | 358.12 | 0.20 | 2.85 | 1584 |
| 2024-09-20 22:21:42.358 | MS1 | 121.4656594548 | 31.1446325066 | 508 | 504990 | -93.50 | 7.02 | 534.47 | 0.15 | 2.48 | 1596 |

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
| 3218357 | 2 | 121.4704227046 | 31.1557098416 | 5 | 14 | 1 | 32.7 | TDD | 650 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3231691 | 1 | 121.4755105189 | 31.1482800179 | 209 | 3 | 0 | 19.3 | TDD | 401 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3250269 | 4 | 121.4661653330 | 31.1446641554 | 104 | 15 | 7 | 44.9 | TDD | 631 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3262015 | 3 | 121.4709325460 | 31.1506084921 | 212 | 0 | 9 | 23.9 | TDD | 508 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:31.136 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.152 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.275 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.275 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.936 | NREventA3 | measId:2;ServCellPCI:465;Se... |
| 2024-09-20 22:21:38.176 | NRHandoverAttempt | SourcePCI:465;SourceNR-ARFC... |
| 2024-09-20 22:21:38.219 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.233 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.351 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.351 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3231691 | 1 | 8.6233 | 18.7658 | -115.0079 | 10.0512 | 198.1983 | 0.0047 | 0.0016 |
| 2024_09_20 22:00 | 3218357 | 2 | 14.5737 | 19.0864 | -116.9168 | 5.1004 | 138.8437 | 0.0165 | 0.0182 |
| 2024_09_20 22:00 | 3262015 | 3 | 91.0002 | 83.8589 | -116.9053 | 17.6839 | 139.7490 | 0.0037 | 0.0122 |
| 2024_09_20 22:00 | 3250269 | 4 | 9.0920 | 16.5795 | -114.0754 | 19.6312 | 110.0187 | 0.0113 | 0.0095 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415343_29B74A60 | 504990 | 508 | -90.6 | 504990 | 631 | -91.8 | 504990 | 650 | -104.6 | 504990 | 401 |
| MR_1774415343_1FB209A9 | 504990 | 508 | -90.0 | 504990 | 631 | -92.9 | 504990 | 650 | -104.7 | 504990 | 401 |
| MR_1774415343_E08B034C | 504990 | 508 | -89.3 | 504990 | 631 | -94.8 | 504990 | 650 | -105.7 | 504990 | 401 |
| MR_1774415343_07FF22A7 | 504990 | 508 | -89.8 | 504990 | 631 | -92.0 | 504990 | 650 | -103.9 | 504990 | 401 |
| MR_1774415343_B407EE26 | 504990 | 508 | -90.5 | 504990 | 631 | -93.7 | 504990 | 650 | -102.1 | 504990 | 401 |
| MR_1774415343_97A7353A | 504990 | 508 | -89.5 | 504990 | 631 | -93.6 | 504990 | 650 | -104.0 | 504990 | 401 |
| MR_1774415343_033C024E | 504990 | 508 | -91.3 | 504990 | 631 | -94.8 | 504990 | 650 | -102.6 | 504990 | 401 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1261: `bf4cb16a-9f1...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `bf4cb16a-9f11-45d8-a40f-aed767fd21bf` |
| Tag | **single-answer** |
| 정답 | **C12** |
| C12 의미 | Add neighbor relationship between 3247693_2 and 3272836_3 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1261] topology](images/train_1261.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3272836_3
- `C2`: Decrease A3 Offset threshold for 3247693_2
- `C3`: Decrease A3 Offset threshold for 3272836_3
- `C4`: Decrease transmission power for 3247693_2
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3272836_3
- `C6`: Add neighbor relationship between 3236356_1 and 3272836_3
- `C7`: Insufficient data; more data is needed for judgment.
- `C8`: Press down the tilt angle of 3247693_2 by 10 degrees
- `C9`: Adjust the azimuth of 3247693_2 by 37 degrees
- `C10`: Adjust the azimuth of 3272836_3 by 44 degrees
- `C11`: Increase transmission power for 3247693_2
- `C12`: Add neighbor relationship between 3247693_2 and 3272836_3 **← 정답**
- `C13`: Lift the tilt angle  of 3272836_3 by 3 degrees
- `C14`: Press down the tilt angle  of 3272836_3 by 3 degrees
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3247693_2
- `C16`: Increase transmission power for 3272836_3
- `C17`: Lift the tilt angle of 3247693_2 by 10 degrees
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3272836_3
- `C19`: Decrease transmission power for 3272836_3
- `C20`: Check test server and transmission issues
- `C21`: Increase A3 Offset threshold for 3247693_2
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3247693_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.344 | MS1 | 121.4656607012 | 31.1446294540 | 634 | 504990 | -77.78 | 15.34 | 462.70 | 0.05 | 2.18 | 1598 |
| 2024-09-20 22:21:32.973 | MS1 | 121.4656733005 | 31.1446212943 | 634 | 504990 | -77.32 | 16.58 | 413.83 | 0.09 | 2.38 | 1593 |
| 2024-09-20 22:21:33.691 | MS1 | 121.4656732045 | 31.1446273397 | 634 | 504990 | -81.96 | 15.94 | 582.82 | 0.05 | 2.24 | 1596 |
| 2024-09-20 22:21:34.348 | MS1 | 121.4656650896 | 31.1446374965 | 634 | 504990 | -87.78 | -0.47 | 37.38 | 0.10 | 1.07 | 1592 |
| 2024-09-20 22:21:35.120 | MS1 | 121.4656592060 | 31.1446194630 | 634 | 504990 | -94.14 | -1.51 | 28.74 | 0.13 | 1.18 | 1577 |
| 2024-09-20 22:21:36.358 | MS1 | 121.4656620520 | 31.1446185631 | 634 | 504990 | -94.64 | -2.27 | 55.78 | 0.20 | 1.41 | 1564 |
| 2024-09-20 22:21:37.838 | MS1 | 121.4656643131 | 31.1446297222 | 634 | 504990 | -93.79 | -0.94 | 29.42 | 0.10 | 1.35 | 1590 |
| 2024-09-20 22:21:38.222 | MS1 | 121.4656757775 | 31.1446377772 | 634 | 504990 | -78.71 | 14.76 | 520.60 | 0.05 | 1.38 | 1562 |
| 2024-09-20 22:21:39.267 | MS1 | 121.4656624629 | 31.1446319303 | 634 | 504990 | -82.30 | 14.29 | 302.69 | 0.01 | 1.33 | 1584 |
| 2024-09-20 22:21:40.696 | MS1 | 121.4656644341 | 31.1446306382 | 634 | 504990 | -76.43 | 15.24 | 299.98 | 0.00 | 2.38 | 1589 |
| 2024-09-20 22:21:41.864 | MS1 | 121.4656721814 | 31.1446197967 | 634 | 504990 | -77.52 | 15.47 | 488.42 | 0.02 | 2.59 | 1599 |
| 2024-09-20 22:21:42.404 | MS1 | 121.4656637681 | 31.1446188013 | 634 | 504990 | -77.48 | 15.44 | 393.43 | 0.02 | 2.68 | 1563 |

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
| 3236356 | 1 | 121.4655793347 | 31.1537800210 | 33 | 13 | 11 | 42.3 | TDD | 480 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3242595 | 4 | 121.4668650247 | 31.1517618014 | 62 | 4 | 9 | 32.9 | TDD | 807 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3247693 | 2 | 121.4759354122 | 31.1448188657 | 306 | 15 | 0 | 19.2 | TDD | 634 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3272836 | 3 | 121.4719776033 | 31.1542940797 | 165 | 2 | 1 | 17.8 | TDD | 567 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |

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
| 2024-09-20 22:21:31.286 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.302 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.420 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.420 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.170 | NREventA3 | measId:2;ServCellPCI:330;Se... |
| 2024-09-20 22:21:36.170 | NREventA3 | measId:2;ServCellPCI:330;Se... |
| 2024-09-20 22:21:37.170 | NREventA3 | measId:2;ServCellPCI:330;Se... |
| 2024-09-20 22:21:39.670 | NRRRCReestablishAttempt | PCI:330 |
| 2024-09-20 22:21:39.680 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.693 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:39.816 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.816 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3236356 | 1 | 11.2678 | 9.6866 | -114.7496 | 11.1894 | 190.2709 | 0.0149 | 0.0133 |
| 2024_09_20 22:00 | 3247693 | 2 | 13.9064 | 18.9393 | -117.3557 | 11.0634 | 161.3455 | 0.0003 | 0.1351 |
| 2024_09_20 22:00 | 3272836 | 3 | 13.4497 | 14.5298 | -114.2828 | 8.7932 | 86.9452 | 0.0045 | 0.0133 |
| 2024_09_20 22:00 | 3242595 | 4 | 9.1786 | 10.9627 | -116.7218 | 9.3623 | 126.1815 | 0.0062 | 0.0016 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412819_99DA8DDB | 504990 | 634 | -86.0 | 504990 | 567 | -83.4 | 504990 | 480 | -90.5 | 504990 | 807 |
| MR_1774412819_4D3CC6CA | 504990 | 634 | -87.0 | 504990 | 567 | -83.5 | 504990 | 480 | -91.2 | 504990 | 807 |
| MR_1774412819_67B35576 | 504990 | 634 | -89.6 | 504990 | 567 | -83.3 | 504990 | 480 | -93.2 | 504990 | 807 |
| MR_1774412819_2529E256 | 504990 | 567 | -80.6 | 504990 | 634 | -86.9 | 504990 | 480 | -91.9 | 504990 | 807 |
| MR_1774412819_8146790B | 504990 | 634 | -87.2 | 504990 | 567 | -81.9 | 504990 | 480 | -92.2 | 504990 | 807 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1262: `de991641-3d5...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `de991641-3d5d-4166-aa1a-00cdf0ef9ba4` |
| Tag | **single-answer** |
| 정답 | **C16** |
| C16 의미 | Add neighbor relationship between 3255305_3 and 3262657_4 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1262] topology](images/train_1262.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3255305_3
- `C2`: Lift the tilt angle  of 3262657_4 by 5 degrees
- `C3`: Press down the tilt angle  of 3262657_4 by 5 degrees
- `C4`: Adjust the azimuth of 3255305_3 by 17 degrees
- `C5`: Check test server and transmission issues
- `C6`: Decrease A3 Offset threshold for 3255305_3
- `C7`: Increase A3 Offset threshold for 3255305_3
- `C8`: Decrease transmission power for 3255305_3
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3262657_4
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3262657_4
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3255305_3
- `C12`: Increase transmission power for 3255305_3
- `C13`: Add neighbor relationship between 3253974_1 and 3262657_4
- `C14`: Increase A3 Offset threshold for 3262657_4
- `C15`: Decrease transmission power for 3262657_4
- `C16`: Add neighbor relationship between 3255305_3 and 3262657_4 **← 정답**
- `C17`: Increase transmission power for 3262657_4
- `C18`: Decrease A3 Offset threshold for 3262657_4
- `C19`: Adjust the azimuth of 3262657_4 by 25 degrees
- `C20`: Insufficient data; more data is needed for judgment.
- `C21`: Lift the tilt angle of 3255305_3 by 7 degrees
- `C22`: Press down the tilt angle of 3255305_3 by 7 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.597 | MS1 | 121.4656644861 | 31.1446247884 | 388 | 504990 | -80.69 | 13.66 | 331.98 | 0.18 | 2.52 | 1580 |
| 2024-09-20 22:21:32.291 | MS1 | 121.4656615701 | 31.1446262546 | 388 | 504990 | -81.24 | 12.87 | 531.33 | 0.04 | 2.17 | 1575 |
| 2024-09-20 22:21:33.770 | MS1 | 121.4656739092 | 31.1446276977 | 388 | 504990 | -77.52 | 15.52 | 390.97 | 0.04 | 2.97 | 1567 |
| 2024-09-20 22:21:34.288 | MS1 | 121.4656585227 | 31.1446201534 | 388 | 504990 | -89.08 | -3.32 | 37.90 | 0.12 | 1.42 | 1578 |
| 2024-09-20 22:21:35.742 | MS1 | 121.4656690173 | 31.1446311456 | 388 | 504990 | -87.12 | -2.64 | 72.73 | 0.06 | 1.38 | 1592 |
| 2024-09-20 22:21:36.684 | MS1 | 121.4656629230 | 31.1446268543 | 388 | 504990 | -93.58 | -2.83 | 40.92 | 0.14 | 1.18 | 1562 |
| 2024-09-20 22:21:37.545 | MS1 | 121.4656659701 | 31.1446374303 | 388 | 504990 | -93.56 | -2.85 | 53.05 | 0.11 | 1.18 | 1599 |
| 2024-09-20 22:21:38.559 | MS1 | 121.4656674092 | 31.1446229754 | 388 | 504990 | -82.76 | 13.47 | 441.75 | 0.11 | 1.09 | 1576 |
| 2024-09-20 22:21:39.891 | MS1 | 121.4656711855 | 31.1446368040 | 388 | 504990 | -77.46 | 12.18 | 449.16 | 0.03 | 1.28 | 1584 |
| 2024-09-20 22:21:40.845 | MS1 | 121.4656581646 | 31.1446221046 | 388 | 504990 | -84.96 | 15.47 | 444.95 | 0.15 | 2.20 | 1575 |
| 2024-09-20 22:21:41.249 | MS1 | 121.4656661936 | 31.1446273134 | 388 | 504990 | -79.14 | 13.18 | 394.05 | 0.13 | 2.30 | 1566 |
| 2024-09-20 22:21:42.795 | MS1 | 121.4656773561 | 31.1446241656 | 388 | 504990 | -79.58 | 16.27 | 422.97 | 0.06 | 2.94 | 1570 |

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
| 3253974 | 1 | 121.4676430037 | 31.1450238006 | 172 | 3 | 5 | 17.0 | TDD | 201 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3255305 | 3 | 121.4725302686 | 31.1481182138 | 222 | 4 | 4 | 45.2 | TDD | 388 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3256170 | 2 | 121.4749152323 | 31.1529165537 | 310 | 10 | 12 | 39.9 | TDD | 626 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3262657 | 4 | 121.4723855769 | 31.1548639088 | 184 | 3 | 11 | 49.5 | TDD | 605 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:31.015 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.039 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.145 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.145 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.915 | NREventA3 | measId:2;ServCellPCI:834;Se... |
| 2024-09-20 22:21:35.915 | NREventA3 | measId:2;ServCellPCI:834;Se... |
| 2024-09-20 22:21:36.915 | NREventA3 | measId:2;ServCellPCI:834;Se... |
| 2024-09-20 22:21:39.415 | NRRRCReestablishAttempt | PCI:834 |
| 2024-09-20 22:21:39.427 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.441 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:39.565 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.565 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3253974 | 1 | 5.8346 | 10.4187 | -115.9738 | 10.0789 | 97.8676 | 0.0054 | 0.0189 |
| 2024_09_20 22:00 | 3256170 | 2 | 7.1769 | 11.3141 | -115.1262 | 12.9632 | 106.5519 | 0.0078 | 0.0040 |
| 2024_09_20 22:00 | 3255305 | 3 | 8.6669 | 8.0792 | -116.4046 | 18.3331 | 191.6005 | 0.0079 | 0.1905 |
| 2024_09_20 22:00 | 3262657 | 4 | 19.8768 | 18.0211 | -115.6282 | 15.2687 | 153.9777 | 0.0156 | 0.0175 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414015_71312A6D | 504990 | 605 | -83.0 | 504990 | 388 | -87.2 | 504990 | 201 | -94.2 | 504990 | 626 |
| MR_1774414015_36FB7916 | 504990 | 388 | -89.1 | 504990 | 605 | -83.4 | 504990 | 201 | -91.6 | 504990 | 626 |
| MR_1774414015_5696E21A | 504990 | 605 | -82.6 | 504990 | 388 | -87.8 | 504990 | 201 | -93.0 | 504990 | 626 |
| MR_1774414015_FAC9A89C | 504990 | 605 | -86.0 | 504990 | 388 | -90.0 | 504990 | 201 | -92.8 | 504990 | 626 |
| MR_1774414015_1C1895A1 | 504990 | 605 | -86.0 | 504990 | 388 | -87.2 | 504990 | 201 | -92.3 | 504990 | 626 |
| MR_1774414015_0A608D36 | 504990 | 605 | -85.9 | 504990 | 388 | -87.3 | 504990 | 201 | -91.5 | 504990 | 626 |
| MR_1774414015_AB958F32 | 504990 | 388 | -89.3 | 504990 | 605 | -83.3 | 504990 | 201 | -93.4 | 504990 | 626 |
| MR_1774414015_D4C161B1 | 504990 | 605 | -86.0 | 504990 | 388 | -90.4 | 504990 | 201 | -94.3 | 504990 | 626 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1263: `4c47e5c2-bce...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `4c47e5c2-bcea-473c-8eec-8c87ff82eb22` |
| Tag | **single-answer** |
| 정답 | **C1** |
| C1 의미 | Lift the tilt angle  of 3263898_3 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1263] topology](images/train_1263.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle  of 3263898_3 by 10 degrees **← 정답**
- `C2`: Decrease A3 Offset threshold for 3231205_1
- `C3`: Lift the tilt angle of 3278233_2 by 5 degrees
- `C4`: Add neighbor relationship between 3278233_2 and 3231205_1
- `C5`: Press down the tilt angle  of 3263898_3 by 10 degrees
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3278233_2
- `C7`: Check test server and transmission issues
- `C8`: Decrease transmission power for 3278233_2
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3278233_2
- `C10`: Decrease transmission power for 3231205_1
- `C11`: Adjust the azimuth of 3278233_2 by 50 degrees
- `C12`: Adjust the azimuth of 3263898_3 by 50 degrees
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3231205_1
- `C14`: Increase A3 Offset threshold for 3231205_1
- `C15`: Increase A3 Offset threshold for 3278233_2
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3231205_1
- `C17`: Increase transmission power for 3231205_1
- `C18`: Increase transmission power for 3278233_2
- `C19`: Add neighbor relationship between 3263898_3 and 3231205_1
- `C20`: Insufficient data; more data is needed for judgment.
- `C21`: Decrease A3 Offset threshold for 3278233_2
- `C22`: Press down the tilt angle of 3278233_2 by 5 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.262 | MS1 | 121.4656711418 | 31.1446366651 | 964 | 504990 | -85.70 | 12.94 | 448.85 | 0.11 | 2.23 | 1562 |
| 2024-09-20 22:21:32.110 | MS1 | 121.4656777347 | 31.1446226604 | 964 | 504990 | -90.35 | 12.74 | 580.87 | 0.02 | 2.95 | 1578 |
| 2024-09-20 22:21:33.771 | MS1 | 121.4656653284 | 31.1446291317 | 964 | 504990 | -91.05 | 17.13 | 516.71 | 0.13 | 2.76 | 1568 |
| 2024-09-20 22:21:34.561 | MS1 | 121.4656682206 | 31.1446208227 | 964 | 504990 | -85.10 | 17.54 | 72.56 | 0.03 | 2.47 | 1565 |
| 2024-09-20 22:21:35.441 | MS1 | 121.4656599146 | 31.1446264727 | 964 | 504990 | -88.58 | 12.28 | 83.65 | 0.03 | 2.58 | 1597 |
| 2024-09-20 22:21:36.619 | MS1 | 121.4656685805 | 31.1446301149 | 964 | 504990 | -91.55 | 16.91 | 55.86 | 0.16 | 2.22 | 1568 |
| 2024-09-20 22:21:37.269 | MS1 | 121.4656627040 | 31.1446291543 | 964 | 504990 | -92.11 | 11.77 | 84.71 | 0.06 | 2.96 | 1594 |
| 2024-09-20 22:21:38.103 | MS1 | 121.4656745309 | 31.1446355540 | 964 | 504990 | -90.23 | 10.36 | 81.38 | 0.15 | 2.36 | 1587 |
| 2024-09-20 22:21:39.857 | MS1 | 121.4656775003 | 31.1446249346 | 964 | 504990 | -89.76 | 11.89 | 66.32 | 0.08 | 2.32 | 1599 |
| 2024-09-20 22:21:40.117 | MS1 | 121.4656635046 | 31.1446348057 | 964 | 504990 | -93.72 | 7.39 | 558.33 | 0.16 | 2.97 | 1566 |
| 2024-09-20 22:21:41.219 | MS1 | 121.4656652625 | 31.1446315432 | 964 | 504990 | -91.27 | 7.48 | 376.76 | 0.01 | 2.40 | 1576 |
| 2024-09-20 22:21:42.605 | MS1 | 121.4656688687 | 31.1446280957 | 964 | 504990 | -92.20 | 8.82 | 405.14 | 0.03 | 2.40 | 1564 |

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
| 3212298 | 4 | 121.4711002523 | 31.1445781899 | 348 | 11 | 6 | 42.6 | TDD | 847 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3231205 | 1 | 121.4703618223 | 31.1522468347 | 4 | 13 | 2 | 22.8 | TDD | 623 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3263898 | 3 | 121.4667518766 | 31.1468282011 | 128 | 10 | 7 | 49.1 | TDD | 901 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3278233 | 2 | 121.4697475432 | 31.1468857398 | 287 | 0 | 12 | 39.9 | TDD | 964 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |

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
| 2024-09-20 22:21:31.154 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.174 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.318 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.318 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.048 | NREventA3 | measId:2;ServCellPCI:521;Se... |
| 2024-09-20 22:21:38.288 | NRHandoverAttempt | SourcePCI:521;SourceNR-ARFC... |
| 2024-09-20 22:21:38.323 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.334 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.468 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.468 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3231205 | 1 | 9.5858 | 9.7351 | -117.7281 | 15.3418 | 186.2817 | 0.0195 | 0.0107 |
| 2024_09_20 22:00 | 3278233 | 2 | 86.5673 | 82.8768 | -116.7766 | 10.0615 | 123.6430 | 0.0020 | 0.0077 |
| 2024_09_20 22:00 | 3263898 | 3 | 13.4635 | 11.1548 | -117.7080 | 16.0827 | 142.0162 | 0.0086 | 0.0198 |
| 2024_09_20 22:00 | 3212298 | 4 | 10.7898 | 6.3592 | -115.2579 | 19.5324 | 101.5570 | 0.0081 | 0.0033 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413430_C07FA1ED | 504990 | 964 | -83.4 | 504990 | 623 | -90.1 | 504990 | 901 | -99.9 | 504990 | 847 |
| MR_1774413430_5C2EC5B1 | 504990 | 964 | -83.6 | 504990 | 623 | -91.1 | 504990 | 901 | -99.4 | 504990 | 847 |
| MR_1774413430_BF6AB058 | 504990 | 964 | -83.5 | 504990 | 623 | -93.1 | 504990 | 901 | -100.0 | 504990 | 847 |
| MR_1774413430_B274D7C4 | 504990 | 964 | -85.1 | 504990 | 623 | -93.9 | 504990 | 901 | -100.3 | 504990 | 847 |
| MR_1774413430_2378A136 | 504990 | 964 | -85.9 | 504990 | 623 | -90.1 | 504990 | 901 | -97.1 | 504990 | 847 |
| MR_1774413430_51931729 | 504990 | 964 | -85.8 | 504990 | 623 | -93.9 | 504990 | 901 | -98.6 | 504990 | 847 |
| MR_1774413430_2D1AE78B | 504990 | 964 | -86.4 | 504990 | 623 | -92.3 | 504990 | 901 | -100.6 | 504990 | 847 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1264: `8a756c08-6cb...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `8a756c08-6cbb-4527-ae51-23db4fbe3c80` |
| Tag | **multiple-answer** |
| 정답 | **C3|C17** |
| C3 의미 | Decrease transmission power for 3261445_1 |
| C17 의미 | Press down the tilt angle  of 3261445_1 by 4 degrees |
| 패턴 분류 | **P3 Overshoot (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1264] topology](images/train_1264.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3229946_2 by 23 degrees
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3261445_1
- `C3`: Decrease transmission power for 3261445_1 **← 정답**
- `C4`: Insufficient data; more data is needed for judgment.
- `C5`: Add neighbor relationship between 3212942_4 and 3261445_1
- `C6`: Add neighbor relationship between 3229946_2 and 3261445_1
- `C7`: Increase transmission power for 3261445_1
- `C8`: Decrease transmission power for 3229946_2
- `C9`: Increase transmission power for 3229946_2
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3229946_2
- `C11`: Increase A3 Offset threshold for 3229946_2
- `C12`: Press down the tilt angle of 3229946_2 by 6 degrees
- `C13`: Lift the tilt angle of 3229946_2 by 6 degrees
- `C14`: Lift the tilt angle  of 3261445_1 by 4 degrees
- `C15`: Increase A3 Offset threshold for 3261445_1
- `C16`: Decrease A3 Offset threshold for 3261445_1
- `C17`: Press down the tilt angle  of 3261445_1 by 4 degrees **← 정답**
- `C18`: Adjust the azimuth of 3261445_1 by 19 degrees
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3229946_2
- `C20`: Check test server and transmission issues
- `C21`: Decrease A3 Offset threshold for 3229946_2
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3261445_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.310 | MS1 | 121.4656637794 | 31.1446290826 | 367 | 504990 | -78.67 | 13.54 | 580.80 | 0.05 | 2.14 | 1561 |
| 2024-09-20 22:21:32.898 | MS1 | 121.4656609454 | 31.1446285816 | 367 | 504990 | -78.13 | 12.16 | 443.15 | 0.08 | 2.64 | 1598 |
| 2024-09-20 22:21:33.292 | MS1 | 121.4656629276 | 31.1446365059 | 367 | 504990 | -82.54 | 15.05 | 439.52 | 0.17 | 2.97 | 1568 |
| 2024-09-20 22:21:34.380 | MS1 | 121.4656689461 | 31.1446326666 | 367 | 504990 | -90.80 | 0.31 | 76.53 | 0.20 | 1.36 | 1600 |
| 2024-09-20 22:21:35.383 | MS1 | 121.4656683622 | 31.1446366711 | 367 | 504990 | -93.20 | 1.43 | 66.43 | 0.17 | 1.20 | 1591 |
| 2024-09-20 22:21:36.267 | MS1 | 121.4656586393 | 31.1446355912 | 367 | 504990 | -92.45 | 1.46 | 92.61 | 0.19 | 1.30 | 1572 |
| 2024-09-20 22:21:37.446 | MS1 | 121.4656703432 | 31.1446353844 | 367 | 504990 | -86.04 | 0.09 | 50.80 | 0.12 | 1.06 | 1596 |
| 2024-09-20 22:21:38.690 | MS1 | 121.4656659748 | 31.1446345188 | 367 | 504990 | -86.30 | 1.97 | 57.21 | 0.01 | 1.02 | 1578 |
| 2024-09-20 22:21:39.614 | MS1 | 121.4656606465 | 31.1446289375 | 367 | 504990 | -88.07 | 1.72 | 49.68 | 0.02 | 1.07 | 1579 |
| 2024-09-20 22:21:40.755 | MS1 | 121.4656694953 | 31.1446313828 | 367 | 504990 | -82.11 | 17.58 | 501.79 | 0.10 | 2.01 | 1569 |
| 2024-09-20 22:21:41.597 | MS1 | 121.4656585291 | 31.1446238625 | 367 | 504990 | -82.54 | 14.94 | 494.25 | 0.11 | 2.24 | 1595 |
| 2024-09-20 22:21:42.197 | MS1 | 121.4656680799 | 31.1446324817 | 367 | 504990 | -78.55 | 13.06 | 501.25 | 0.01 | 2.32 | 1587 |

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
| 3212942 | 4 | 121.4687564326 | 31.1512627989 | 63 | 11 | 3 | 48.0 | TDD | 847 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3229946 | 2 | 121.4717574474 | 31.1528651065 | 189 | 4 | 3 | 34.9 | TDD | 367 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3250358 | 3 | 121.4691779821 | 31.1449664190 | 17 | 1 | 2 | 47.9 | TDD | 454 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3261445 | 1 | 121.4653689915 | 31.1526430498 | 159 | 3 | 1 | 23.3 | TDD | 120 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |

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
| 2024-09-20 22:21:30.812 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.827 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:30.963 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.963 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3261445 | 1 | 5.7748 | 12.7499 | -114.7602 | 10.5151 | 198.5706 | 0.0117 | 0.0160 |
| 2024_09_20 22:00 | 3229946 | 2 | 18.5094 | 15.7799 | -108.0917 | 10.0189 | 160.8379 | 0.0105 | 0.0167 |
| 2024_09_20 22:00 | 3250358 | 3 | 14.2166 | 11.6388 | -114.6123 | 13.4314 | 149.7245 | 0.0150 | 0.0044 |
| 2024_09_20 22:00 | 3212942 | 4 | 10.4126 | 9.9648 | -114.9271 | 17.2949 | 182.9062 | 0.0092 | 0.0075 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416172_F3288C72 | 504990 | 367 | -89.9 | 504990 | 120 | -88.5 | 504990 | 847 | -91.2 | 504990 | 454 |
| MR_1774416172_965DF18F | 504990 | 367 | -89.2 | 504990 | 120 | -87.8 | 504990 | 847 | -88.9 | 504990 | 454 |
| MR_1774416172_40A665F4 | 504990 | 367 | -90.2 | 504990 | 120 | -90.5 | 504990 | 847 | -91.1 | 504990 | 454 |
| MR_1774416172_564781BE | 504990 | 120 | -88.8 | 504990 | 367 | -89.1 | 504990 | 847 | -88.7 | 504990 | 454 |
| MR_1774416172_1675165D | 504990 | 367 | -92.7 | 504990 | 120 | -88.9 | 504990 | 847 | -89.0 | 504990 | 454 |
| MR_1774416172_A857969E | 504990 | 120 | -90.2 | 504990 | 367 | -90.0 | 504990 | 847 | -88.3 | 504990 | 454 |
| MR_1774416172_F42A5D05 | 504990 | 367 | -91.1 | 504990 | 120 | -88.2 | 504990 | 847 | -91.5 | 504990 | 454 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1265: `a92730d1-558...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `a92730d1-5586-44e3-9799-d809afe925d8` |
| Tag | **single-answer** |
| 정답 | **C7** |
| C7 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3252158_2 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1265] topology](images/train_1265.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3275185_4 by 24 degrees
- `C2`: Insufficient data; more data is needed for judgment.
- `C3`: Adjust the azimuth of 3252158_2 by 14 degrees
- `C4`: Increase A3 Offset threshold for 3252158_2
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3275185_4
- `C6`: Press down the tilt angle of 3252158_2 by 5 degrees
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3252158_2 **← 정답**
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3252158_2
- `C9`: Lift the tilt angle  of 3275185_4 by 1 degrees
- `C10`: Increase transmission power for 3275185_4
- `C11`: Add neighbor relationship between 3257505_8 and 3275185_4
- `C12`: Press down the tilt angle  of 3275185_4 by 1 degrees
- `C13`: Decrease transmission power for 3252158_2
- `C14`: Check test server and transmission issues
- `C15`: Decrease A3 Offset threshold for 3252158_2
- `C16`: Increase transmission power for 3252158_2
- `C17`: Add neighbor relationship between 3252158_2 and 3275185_4
- `C18`: Decrease A3 Offset threshold for 3275185_4
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3275185_4
- `C20`: Increase A3 Offset threshold for 3275185_4
- `C21`: Lift the tilt angle of 3252158_2 by 5 degrees
- `C22`: Decrease transmission power for 3275185_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.121 | MS1 | 121.4656726454 | 31.1446338837 | 753 | 504990 | -93.78 | 10.00 | 396.86 | 0.18 | 2.99 | 1577 |
| 2024-09-20 22:21:32.340 | MS1 | 121.4656644616 | 31.1446184510 | 991 | 504990 | -93.27 | 11.69 | 447.48 | 0.01 | 2.57 | 1577 |
| 2024-09-20 22:21:33.257 | MS1 | 121.4656588090 | 31.1446357979 | 114 | 504990 | -93.04 | 9.67 | 395.86 | 0.13 | 2.60 | 1597 |
| 2024-09-20 22:21:34.737 | MS1 | 121.4656600459 | 31.1446360733 | 160 | 152650 | -93.61 | 3.14 | 94.67 | 0.13 | 1.50 | 994 |
| 2024-09-20 22:21:35.989 | MS1 | 121.4656664500 | 31.1446377455 | 498 | 152650 | -89.48 | 7.42 | 97.25 | 0.13 | 1.94 | 942 |
| 2024-09-20 22:21:36.766 | MS1 | 121.4656694897 | 31.1446211430 | 711 | 152650 | -91.00 | 6.90 | 58.31 | 0.18 | 1.70 | 901 |
| 2024-09-20 22:21:37.331 | MS1 | 121.4656662355 | 31.1446312228 | 217 | 152650 | -94.10 | 2.94 | 87.48 | 0.06 | 1.66 | 922 |
| 2024-09-20 22:21:38.220 | MS1 | 121.4656638693 | 31.1446254974 | 160 | 152650 | -95.50 | 5.02 | 65.29 | 0.13 | 1.61 | 1000 |
| 2024-09-20 22:21:39.112 | MS1 | 121.4656644930 | 31.1446254407 | 498 | 152650 | -92.15 | 7.56 | 64.58 | 0.06 | 1.99 | 962 |
| 2024-09-20 22:21:40.726 | MS1 | 121.4656651418 | 31.1446222975 | 711 | 152650 | -91.14 | 4.64 | 88.53 | 0.15 | 2.74 | 1565 |
| 2024-09-20 22:21:41.748 | MS1 | 121.4656704573 | 31.1446240444 | 217 | 152650 | -92.44 | 5.47 | 51.10 | 0.18 | 2.07 | 1591 |
| 2024-09-20 22:21:42.178 | MS1 | 121.4656659214 | 31.1446356414 | 160 | 152650 | -91.39 | 7.22 | 67.85 | 0.17 | 2.39 | 1583 |

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
| 3215592 | 6 | 121.4715760521 | 31.1444644765 | 107 | 12 | 7 | 3.0 | TDD | 991 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3216052 | 5 | 121.4712908273 | 31.1519287552 | 11 | 1 | 5 | 23.1 | TDD | 790 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3220111 | 12 | 121.4749593332 | 31.1508905451 | 125 | 14 | 11 | 0.2 | FDD | 604 | n1 | 152650 | 30M | 4T4R | 30 | 152650 |
| 3243141 | 9 | 121.4676882246 | 31.1522217922 | 176 | 3 | 10 | 28.5 | FDD | 267 | n1 | 152650 | 30M | 4T4R | 18 | 152650 |
| 3252130 | 10 | 121.4687722207 | 31.1557175023 | 132 | 7 | 7 | 19.6 | FDD | 498 | n1 | 152650 | 30M | 4T4R | 12 | 152650 |
| 3252158 | 2 | 121.4656647499 | 31.1545075407 | 194 | 4 | 11 | 16.9 | TDD | 753 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3253497 | 7 | 121.4673554109 | 31.1493082145 | 245 | 2 | 6 | 27.7 | FDD | 160 | n1 | 152650 | 30M | 4T4R | 27 | 152650 |
| 3256884 | 1 | 121.4643953094 | 31.1458312846 | 49 | 2 | 9 | 24.4 | TDD | 384 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3257505 | 8 | 121.4669739856 | 31.1461497643 | 66 | 14 | 7 | 13.0 | FDD | 711 | n1 | 152650 | 30M | 4T4R | 20 | 152650 |
| 3268560 | 11 | 121.4657521729 | 31.1529909288 | 54 | 7 | 7 | 2.1 | FDD | 217 | n1 | 152650 | 30M | 4T4R | 30 | 152650 |
| 3275185 | 4 | 121.4702654770 | 31.1471538932 | 213 | 0 | 6 | 8.2 | TDD | 789 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3277587 | 3 | 121.4651142307 | 31.1462483853 | 312 | 0 | 9 | 25.5 | TDD | 114 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3278519 | 13 | 121.4714285356 | 31.1471951504 | 56 | 3 | 12 | 8.1 | FDD | 670 | n1 | 152650 | 30M | 4T4R | 27 | 152650 |

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
| 2024-09-20 22:21:31.338 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.357 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.460 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.460 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.229 | NREventA2 | measId:1;ServCellPCI:299;Se... |
| 2024-09-20 22:21:35.344 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.560 | NREventA5 | measId:3;ServCellPCI:299;Se... |
| 2024-09-20 22:21:35.597 | NRHandoverAttempt | SourcePCI:299;SourceNR-ARFC... |
| 2024-09-20 22:21:35.636 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.647 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:35.754 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.754 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3256884 | 1 | 12.7578 | 7.6201 | -117.7015 | 11.5127 | 170.5969 | 0.0017 | 0.0058 |
| 2024_09_20 22:00 | 3252158 | 2 | 17.5429 | 11.8104 | -116.2545 | 18.0696 | 158.8715 | 0.0192 | 0.0019 |
| 2024_09_20 22:00 | 3277587 | 3 | 11.7281 | 16.9594 | -115.6107 | 16.7798 | 113.0967 | 0.0141 | 0.0082 |
| 2024_09_20 22:00 | 3275185 | 4 | 13.2011 | 17.4712 | -114.1710 | 14.0282 | 170.2220 | 0.0119 | 0.0067 |
| 2024_09_20 22:00 | 3216052 | 5 | 15.8599 | 18.6653 | -117.3491 | 17.8890 | 93.8620 | 0.0067 | 0.0131 |
| 2024_09_20 22:00 | 3215592 | 6 | 7.4906 | 12.8079 | -115.6037 | 10.7150 | 133.7878 | 0.0113 | 0.0136 |
| 2024_09_20 22:00 | 3253497 | 7 | 13.5109 | 17.4117 | -116.1141 | 3.5402 | 57.5969 | 0.0098 | 0.0185 |
| 2024_09_20 22:00 | 3257505 | 8 | 11.5790 | 19.2829 | -117.2964 | 3.6494 | 48.2170 | 0.0189 | 0.0050 |
| 2024_09_20 22:00 | 3243141 | 9 | 19.1909 | 6.8419 | -116.9248 | 3.5480 | 50.3461 | 0.0136 | 0.0030 |
| 2024_09_20 22:00 | 3252130 | 10 | 7.7605 | 6.7215 | -116.9578 | 3.6828 | 39.0626 | 0.0143 | 0.0017 |
| 2024_09_20 22:00 | 3268560 | 11 | 6.1038 | 6.8542 | -117.0446 | 4.9112 | 47.3328 | 0.0002 | 0.0113 |
| 2024_09_20 22:00 | 3220111 | 12 | 15.9912 | 14.6117 | -115.5266 | 3.5111 | 52.9134 | 0.0166 | 0.0168 |
| 2024_09_20 22:00 | 3278519 | 13 | 9.2171 | 16.7842 | -117.8911 | 3.2002 | 45.1176 | 0.0026 | 0.0106 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417048_5B3A9016 | 504990 | 114 | -92.0 | 504990 | 789 | -92.8 | 504990 | 384 | -99.0 | 504990 | 790 |
| MR_1774417048_485B9A14 | 152650 | 160 | -91.9 | 152650 | 604 | -99.0 | 152650 | 267 | -103.9 | 152650 | 670 |
| MR_1774417048_CD04C746 | 504990 | 114 | -93.0 | 504990 | 789 | -93.9 | 504990 | 384 | -99.5 | 504990 | 790 |
| MR_1774417048_0326C9DC | 152650 | 160 | -93.6 | 152650 | 604 | -99.0 | 152650 | 267 | -104.5 | 152650 | 670 |
| MR_1774417048_BE06AD9C | 152650 | 160 | -93.9 | 152650 | 604 | -98.3 | 152650 | 267 | -104.7 | 152650 | 670 |
| MR_1774417048_761C0888 | 152650 | 160 | -93.3 | 152650 | 604 | -95.6 | 152650 | 267 | -106.6 | 152650 | 670 |
| MR_1774417048_B5328994 | 504990 | 114 | -95.0 | 504990 | 789 | -91.9 | 504990 | 384 | -100.0 | 504990 | 790 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1266: `9ceaf783-e38...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `9ceaf783-e38a-4794-9a73-f66f036c82de` |
| Tag | **single-answer** |
| 정답 | **C6** |
| C6 의미 | Lift the tilt angle  of 3233223_4 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1266] topology](images/train_1266.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3233223_4 by 10 degrees
- `C2`: Increase A3 Offset threshold for 3219312_1
- `C3`: Increase transmission power for 3219312_1
- `C4`: Increase transmission power for 3220563_3
- `C5`: Decrease A3 Offset threshold for 3219312_1
- `C6`: Lift the tilt angle  of 3233223_4 by 10 degrees **← 정답**
- `C7`: Check test server and transmission issues
- `C8`: Adjust the azimuth of 3219312_1 by 2 degrees
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3220563_3
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3219312_1
- `C11`: Increase A3 Offset threshold for 3220563_3
- `C12`: Add neighbor relationship between 3219312_1 and 3220563_3
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3219312_1
- `C14`: Add neighbor relationship between 3233223_4 and 3220563_3
- `C15`: Insufficient data; more data is needed for judgment.
- `C16`: Decrease transmission power for 3219312_1
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3220563_3
- `C18`: Decrease transmission power for 3220563_3
- `C19`: Adjust the azimuth of 3233223_4 by 49 degrees
- `C20`: Decrease A3 Offset threshold for 3220563_3
- `C21`: Lift the tilt angle of 3219312_1 by 5 degrees
- `C22`: Press down the tilt angle of 3219312_1 by 5 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.492 | MS1 | 121.4656595839 | 31.1446253558 | 657 | 504990 | -91.96 | 14.85 | 484.95 | 0.04 | 2.26 | 1562 |
| 2024-09-20 22:21:32.730 | MS1 | 121.4656764412 | 31.1446290338 | 657 | 504990 | -88.72 | 13.13 | 466.03 | 0.18 | 2.64 | 1599 |
| 2024-09-20 22:21:33.996 | MS1 | 121.4656618157 | 31.1446204452 | 657 | 504990 | -91.95 | 12.59 | 522.67 | 0.10 | 2.93 | 1596 |
| 2024-09-20 22:21:34.144 | MS1 | 121.4656671857 | 31.1446187685 | 657 | 504990 | -89.61 | 17.20 | 74.46 | 0.18 | 2.27 | 1571 |
| 2024-09-20 22:21:35.847 | MS1 | 121.4656728986 | 31.1446186071 | 657 | 504990 | -87.68 | 12.63 | 46.26 | 0.20 | 2.54 | 1599 |
| 2024-09-20 22:21:36.373 | MS1 | 121.4656742447 | 31.1446222293 | 657 | 504990 | -91.97 | 14.37 | 85.48 | 0.10 | 2.00 | 1577 |
| 2024-09-20 22:21:37.702 | MS1 | 121.4656612867 | 31.1446355766 | 657 | 504990 | -93.70 | 9.49 | 55.69 | 0.02 | 2.27 | 1576 |
| 2024-09-20 22:21:38.353 | MS1 | 121.4656611755 | 31.1446272216 | 657 | 504990 | -91.17 | 11.88 | 82.42 | 0.14 | 2.60 | 1600 |
| 2024-09-20 22:21:39.936 | MS1 | 121.4656714005 | 31.1446262574 | 657 | 504990 | -91.67 | 9.91 | 65.89 | 0.19 | 2.46 | 1586 |
| 2024-09-20 22:21:40.513 | MS1 | 121.4656682213 | 31.1446229552 | 657 | 504990 | -92.62 | 11.51 | 342.31 | 0.16 | 2.49 | 1561 |
| 2024-09-20 22:21:41.168 | MS1 | 121.4656607635 | 31.1446350628 | 657 | 504990 | -92.06 | 12.54 | 484.73 | 0.17 | 2.39 | 1585 |
| 2024-09-20 22:21:42.633 | MS1 | 121.4656628661 | 31.1446193523 | 657 | 504990 | -91.19 | 7.42 | 301.40 | 0.05 | 2.92 | 1585 |

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
| 3219312 | 1 | 121.4681974247 | 31.1444714085 | 272 | 0 | 10 | 23.0 | TDD | 657 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3220563 | 3 | 121.4714185624 | 31.1529936993 | 161 | 8 | 10 | 41.5 | TDD | 667 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3233223 | 4 | 121.4676191350 | 31.1483339692 | 116 | 14 | 1 | 44.1 | TDD | 679 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3244951 | 2 | 121.4651001685 | 31.1468162499 | 72 | 9 | 8 | 32.7 | TDD | 267 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |

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
| 2024-09-20 22:21:31.385 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.402 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.527 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.527 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.201 | NREventA3 | measId:2;ServCellPCI:583;Se... |
| 2024-09-20 22:21:38.441 | NRHandoverAttempt | SourcePCI:583;SourceNR-ARFC... |
| 2024-09-20 22:21:38.477 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.488 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.591 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.591 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3219312 | 1 | 94.6756 | 85.1528 | -115.4827 | 12.4137 | 111.8467 | 0.0001 | 0.0052 |
| 2024_09_20 22:00 | 3244951 | 2 | 9.2451 | 12.3265 | -116.5533 | 17.4104 | 148.1937 | 0.0107 | 0.0024 |
| 2024_09_20 22:00 | 3220563 | 3 | 6.6761 | 7.7558 | -115.7431 | 14.3074 | 178.9684 | 0.0003 | 0.0022 |
| 2024_09_20 22:00 | 3233223 | 4 | 14.2228 | 12.1159 | -114.4279 | 19.6049 | 152.7452 | 0.0004 | 0.0101 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414069_C9AA8339 | 504990 | 657 | -89.5 | 504990 | 667 | -90.1 | 504990 | 679 | -99.5 | 504990 | 267 |
| MR_1774414069_566FBF91 | 504990 | 657 | -91.1 | 504990 | 667 | -90.8 | 504990 | 679 | -101.5 | 504990 | 267 |
| MR_1774414069_B449DC73 | 504990 | 657 | -87.9 | 504990 | 667 | -90.9 | 504990 | 679 | -101.0 | 504990 | 267 |
| MR_1774414069_00A875A2 | 504990 | 657 | -91.5 | 504990 | 667 | -92.2 | 504990 | 679 | -98.5 | 504990 | 267 |
| MR_1774414069_BF308A22 | 504990 | 657 | -87.9 | 504990 | 667 | -91.1 | 504990 | 679 | -100.0 | 504990 | 267 |
| MR_1774414069_6D2E5C15 | 504990 | 657 | -91.0 | 504990 | 667 | -89.3 | 504990 | 679 | -98.6 | 504990 | 267 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1267: `3d8c2601-03e...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `3d8c2601-03e5-4cb5-a131-c6ca463804da` |
| Tag | **single-answer** |
| 정답 | **C18** |
| C18 의미 | Lift the tilt angle  of 3234726_3 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1267] topology](images/train_1267.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3267694_2
- `C2`: Press down the tilt angle  of 3234726_3 by 10 degrees
- `C3`: Increase A3 Offset threshold for 3267391_1
- `C4`: Check test server and transmission issues
- `C5`: Increase transmission power for 3267391_1
- `C6`: Decrease A3 Offset threshold for 3267694_2
- `C7`: Decrease A3 Offset threshold for 3267391_1
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3267694_2
- `C9`: Increase transmission power for 3267694_2
- `C10`: Lift the tilt angle of 3267391_1 by 3 degrees
- `C11`: Increase A3 Offset threshold for 3267694_2
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3267391_1
- `C13`: Adjust the azimuth of 3267391_1 by 2 degrees
- `C14`: Decrease transmission power for 3267391_1
- `C15`: Insufficient data; more data is needed for judgment.
- `C16`: Decrease transmission power for 3267694_2
- `C17`: Add neighbor relationship between 3267391_1 and 3267694_2
- `C18`: Lift the tilt angle  of 3234726_3 by 10 degrees **← 정답**
- `C19`: Adjust the azimuth of 3234726_3 by 37 degrees
- `C20`: Press down the tilt angle of 3267391_1 by 3 degrees
- `C21`: Add neighbor relationship between 3234726_3 and 3267694_2
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3267391_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.817 | MS1 | 121.4656750795 | 31.1446327590 | 305 | 504990 | -89.91 | 12.23 | 409.73 | 0.13 | 2.19 | 1598 |
| 2024-09-20 22:21:32.760 | MS1 | 121.4656669019 | 31.1446203734 | 305 | 504990 | -89.88 | 14.74 | 585.42 | 0.13 | 2.77 | 1597 |
| 2024-09-20 22:21:33.785 | MS1 | 121.4656753857 | 31.1446221578 | 305 | 504990 | -89.98 | 13.17 | 565.61 | 0.02 | 2.76 | 1598 |
| 2024-09-20 22:21:34.830 | MS1 | 121.4656700361 | 31.1446185626 | 305 | 504990 | -87.58 | 17.73 | 107.11 | 0.19 | 2.53 | 1564 |
| 2024-09-20 22:21:35.249 | MS1 | 121.4656632946 | 31.1446240469 | 305 | 504990 | -90.13 | 13.31 | 62.91 | 0.06 | 2.10 | 1600 |
| 2024-09-20 22:21:36.286 | MS1 | 121.4656582722 | 31.1446355555 | 305 | 504990 | -86.62 | 14.01 | 48.91 | 0.06 | 2.72 | 1578 |
| 2024-09-20 22:21:37.357 | MS1 | 121.4656725596 | 31.1446234666 | 305 | 504990 | -91.12 | 9.50 | 76.19 | 0.13 | 2.64 | 1581 |
| 2024-09-20 22:21:38.264 | MS1 | 121.4656734363 | 31.1446304455 | 305 | 504990 | -92.22 | 10.49 | 98.10 | 0.15 | 2.78 | 1586 |
| 2024-09-20 22:21:39.577 | MS1 | 121.4656656931 | 31.1446210616 | 305 | 504990 | -89.65 | 7.06 | 64.60 | 0.07 | 2.75 | 1574 |
| 2024-09-20 22:21:40.581 | MS1 | 121.4656639247 | 31.1446224280 | 305 | 504990 | -92.54 | 7.61 | 517.42 | 0.00 | 2.11 | 1586 |
| 2024-09-20 22:21:41.966 | MS1 | 121.4656776995 | 31.1446298706 | 305 | 504990 | -91.31 | 7.47 | 555.36 | 0.06 | 2.43 | 1573 |
| 2024-09-20 22:21:42.187 | MS1 | 121.4656582119 | 31.1446368825 | 305 | 504990 | -92.46 | 11.47 | 482.38 | 0.01 | 2.49 | 1572 |

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
| 3234726 | 3 | 121.4708689679 | 31.1547412958 | 39 | 3 | 10 | 29.3 | TDD | 982 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3235482 | 4 | 121.4711624602 | 31.1440091199 | 345 | 14 | 0 | 17.0 | TDD | 998 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3267391 | 1 | 121.4658131375 | 31.1559252045 | 183 | 1 | 1 | 34.0 | TDD | 305 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3267694 | 2 | 121.4726027602 | 31.1534992551 | 251 | 14 | 6 | 34.4 | TDD | 412 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |

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
| 2024-09-20 22:21:30.928 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.953 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.096 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.096 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.784 | NREventA3 | measId:2;ServCellPCI:218;Se... |
| 2024-09-20 22:21:38.024 | NRHandoverAttempt | SourcePCI:218;SourceNR-ARFC... |
| 2024-09-20 22:21:38.065 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.079 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.215 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.215 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3267391 | 1 | 87.9101 | 85.4954 | -114.4213 | 7.6198 | 99.4381 | 0.0136 | 0.0065 |
| 2024_09_20 22:00 | 3267694 | 2 | 15.1808 | 14.3000 | -114.7725 | 11.3297 | 87.4301 | 0.0005 | 0.0126 |
| 2024_09_20 22:00 | 3234726 | 3 | 6.2603 | 14.5870 | -116.4813 | 10.3879 | 197.6904 | 0.0104 | 0.0108 |
| 2024_09_20 22:00 | 3235482 | 4 | 15.6066 | 7.1768 | -116.4974 | 12.6615 | 132.9277 | 0.0138 | 0.0097 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412074_6E5D1078 | 504990 | 305 | -89.9 | 504990 | 412 | -99.2 | 504990 | 982 | -105.7 | 504990 | 998 |
| MR_1774412074_D597CBB8 | 504990 | 305 | -88.5 | 504990 | 412 | -97.7 | 504990 | 982 | -104.4 | 504990 | 998 |
| MR_1774412074_F9F36A97 | 504990 | 305 | -88.8 | 504990 | 412 | -99.9 | 504990 | 982 | -104.4 | 504990 | 998 |
| MR_1774412074_3D104035 | 504990 | 305 | -90.2 | 504990 | 412 | -100.1 | 504990 | 982 | -105.0 | 504990 | 998 |
| MR_1774412074_0504596E | 504990 | 305 | -90.9 | 504990 | 412 | -97.5 | 504990 | 982 | -104.4 | 504990 | 998 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1268: `78416498-7f2...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `78416498-7f28-49c1-a6c4-ec6ee673c75a` |
| Tag | **single-answer** |
| 정답 | **C16** |
| C16 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3260537_3 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1268] topology](images/train_1268.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3261839_1
- `C2`: Decrease transmission power for 3261839_1
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3261839_1
- `C4`: Increase A3 Offset threshold for 3260537_3
- `C5`: Check test server and transmission issues
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3260537_3
- `C7`: Lift the tilt angle  of 3261839_1 by 10 degrees
- `C8`: Adjust the azimuth of 3261839_1 by 50 degrees
- `C9`: Decrease A3 Offset threshold for 3261839_1
- `C10`: Lift the tilt angle of 3260537_3 by 5 degrees
- `C11`: Increase transmission power for 3260537_3
- `C12`: Decrease transmission power for 3260537_3
- `C13`: Increase transmission power for 3261839_1
- `C14`: Increase A3 Offset threshold for 3261839_1
- `C15`: Insufficient data; more data is needed for judgment.
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3260537_3 **← 정답**
- `C17`: Add neighbor relationship between 3260537_3 and 3261839_1
- `C18`: Press down the tilt angle of 3260537_3 by 5 degrees
- `C19`: Adjust the azimuth of 3260537_3 by 37 degrees
- `C20`: Press down the tilt angle  of 3261839_1 by 10 degrees
- `C21`: Decrease A3 Offset threshold for 3260537_3
- `C22`: Add neighbor relationship between 3217584_2 and 3261839_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.814 | MS1 | 121.4656711265 | 31.1446376010 | 772 | 504990 | -89.96 | 13.44 | 511.01 | 0.03 | 2.06 | 1569 |
| 2024-09-20 22:21:32.130 | MS1 | 121.4656728460 | 31.1446291311 | 772 | 504990 | -90.05 | 17.83 | 510.35 | 0.14 | 2.59 | 1570 |
| 2024-09-20 22:21:33.548 | MS1 | 121.4656591380 | 31.1446252622 | 772 | 504990 | -91.13 | 17.63 | 541.31 | 0.17 | 2.52 | 1581 |
| 2024-09-20 22:21:34.214 | MS1 | 121.4656701567 | 31.1446264636 | 772 | 504990 | -87.57 | 14.93 | 54.53 | 0.67 | 2.23 | 512 |
| 2024-09-20 22:21:35.532 | MS1 | 121.4656700829 | 31.1446304082 | 772 | 504990 | -89.93 | 16.20 | 53.08 | 0.59 | 2.45 | 596 |
| 2024-09-20 22:21:36.724 | MS1 | 121.4656623582 | 31.1446242583 | 772 | 504990 | -87.92 | 12.37 | 82.27 | 0.64 | 2.65 | 660 |
| 2024-09-20 22:21:37.593 | MS1 | 121.4656670426 | 31.1446200486 | 772 | 504990 | -93.95 | 10.18 | 74.29 | 0.67 | 2.56 | 640 |
| 2024-09-20 22:21:38.151 | MS1 | 121.4656646889 | 31.1446339079 | 772 | 504990 | -89.17 | 10.58 | 82.55 | 0.68 | 2.34 | 567 |
| 2024-09-20 22:21:39.857 | MS1 | 121.4656700420 | 31.1446337867 | 772 | 504990 | -90.90 | 7.65 | 76.42 | 0.67 | 2.82 | 528 |
| 2024-09-20 22:21:40.632 | MS1 | 121.4656607409 | 31.1446189926 | 772 | 504990 | -90.72 | 12.47 | 317.94 | 0.06 | 2.98 | 1578 |
| 2024-09-20 22:21:41.883 | MS1 | 121.4656702699 | 31.1446266574 | 772 | 504990 | -89.87 | 9.65 | 522.55 | 0.18 | 2.70 | 1564 |
| 2024-09-20 22:21:42.256 | MS1 | 121.4656602395 | 31.1446214805 | 772 | 504990 | -89.31 | 11.38 | 494.79 | 0.12 | 2.52 | 1574 |

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
| 3217584 | 2 | 121.4728516335 | 31.1464104201 | 237 | 11 | 9 | 45.5 | TDD | 441 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3237159 | 4 | 121.4665297268 | 31.1544120310 | 225 | 8 | 12 | 27.5 | TDD | 885 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3260537 | 3 | 121.4731973528 | 31.1449652585 | 230 | 2 | 6 | 40.5 | TDD | 772 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3261839 | 1 | 121.4739337215 | 31.1469559901 | 9 | 9 | 5 | 35.2 | TDD | 176 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |

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
| 2024-09-20 22:21:31.445 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.469 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.590 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.590 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.343 | NREventA3 | measId:2;ServCellPCI:341;Se... |
| 2024-09-20 22:21:38.583 | NRHandoverAttempt | SourcePCI:341;SourceNR-ARFC... |
| 2024-09-20 22:21:38.619 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.634 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.753 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.753 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3261839 | 1 | 7.3074 | 17.3187 | -116.6920 | 15.9342 | 84.8941 | 0.0058 | 0.0117 |
| 2024_09_20 22:00 | 3217584 | 2 | 19.9706 | 5.2842 | -114.3709 | 8.7470 | 131.9322 | 0.0072 | 0.0146 |
| 2024_09_20 22:00 | 3260537 | 3 | 8.0460 | 18.0037 | -114.1588 | 19.7974 | 166.6688 | 0.0152 | 0.0109 |
| 2024_09_20 22:00 | 3237159 | 4 | 14.9675 | 5.2564 | -117.6102 | 5.9584 | 106.9480 | 0.0137 | 0.0053 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412403_3C165DCF | 504990 | 772 | -88.4 | 504990 | 176 | -92.0 | 504990 | 441 | -99.4 | 504990 | 885 |
| MR_1774412403_8A9CC1EF | 504990 | 772 | -85.7 | 504990 | 176 | -89.4 | 504990 | 441 | -100.7 | 504990 | 885 |
| MR_1774412403_68355F89 | 504990 | 772 | -86.4 | 504990 | 176 | -92.6 | 504990 | 441 | -99.7 | 504990 | 885 |
| MR_1774412403_9B9136CE | 504990 | 772 | -88.3 | 504990 | 176 | -89.4 | 504990 | 441 | -100.2 | 504990 | 885 |
| MR_1774412403_1C31DED2 | 504990 | 772 | -88.5 | 504990 | 176 | -91.8 | 504990 | 441 | -100.9 | 504990 | 885 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1269: `c1d49dd3-788...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `c1d49dd3-7888-448c-8735-f72938b8edae` |
| Tag | **single-answer** |
| 정답 | **C8** |
| C8 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3215833_3 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1269] topology](images/train_1269.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3263592_4
- `C2`: Insufficient data; more data is needed for judgment.
- `C3`: Press down the tilt angle of 3215833_3 by 3 degrees
- `C4`: Decrease A3 Offset threshold for 3215833_3
- `C5`: Increase transmission power for 3215833_3
- `C6`: Press down the tilt angle  of 3263592_4 by 2 degrees
- `C7`: Decrease transmission power for 3263592_4
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3215833_3 **← 정답**
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3263592_4
- `C10`: Lift the tilt angle of 3215833_3 by 3 degrees
- `C11`: Adjust the azimuth of 3215833_3 by 31 degrees
- `C12`: Add neighbor relationship between 3241496_10 and 3263592_4
- `C13`: Lift the tilt angle  of 3263592_4 by 2 degrees
- `C14`: Decrease A3 Offset threshold for 3263592_4
- `C15`: Increase A3 Offset threshold for 3263592_4
- `C16`: Check test server and transmission issues
- `C17`: Adjust the azimuth of 3263592_4 by 29 degrees
- `C18`: Decrease transmission power for 3215833_3
- `C19`: Increase transmission power for 3263592_4
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3215833_3
- `C21`: Increase A3 Offset threshold for 3215833_3
- `C22`: Add neighbor relationship between 3215833_3 and 3263592_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.620 | MS1 | 121.4656653802 | 31.1446213354 | 722 | 504990 | -94.05 | 9.27 | 437.73 | 0.02 | 2.85 | 1568 |
| 2024-09-20 22:21:32.878 | MS1 | 121.4656625469 | 31.1446318210 | 156 | 504990 | -93.81 | 9.12 | 448.31 | 0.14 | 2.76 | 1592 |
| 2024-09-20 22:21:33.211 | MS1 | 121.4656647644 | 31.1446263219 | 259 | 504990 | -94.80 | 11.57 | 397.82 | 0.03 | 2.70 | 1600 |
| 2024-09-20 22:21:34.236 | MS1 | 121.4656756722 | 31.1446331037 | 964 | 152650 | -87.44 | 2.82 | 46.03 | 0.08 | 1.85 | 985 |
| 2024-09-20 22:21:35.866 | MS1 | 121.4656648862 | 31.1446348995 | 443 | 152650 | -90.30 | 6.03 | 67.08 | 0.06 | 1.78 | 927 |
| 2024-09-20 22:21:36.714 | MS1 | 121.4656652306 | 31.1446258164 | 977 | 152650 | -89.18 | 5.33 | 88.47 | 0.02 | 1.65 | 938 |
| 2024-09-20 22:21:37.126 | MS1 | 121.4656749614 | 31.1446275499 | 303 | 152650 | -88.67 | 3.82 | 75.80 | 0.06 | 1.77 | 900 |
| 2024-09-20 22:21:38.701 | MS1 | 121.4656601092 | 31.1446238192 | 964 | 152650 | -89.37 | 5.36 | 63.86 | 0.15 | 1.62 | 982 |
| 2024-09-20 22:21:39.320 | MS1 | 121.4656778156 | 31.1446257939 | 443 | 152650 | -91.17 | 4.08 | 80.28 | 0.10 | 1.83 | 989 |
| 2024-09-20 22:21:40.242 | MS1 | 121.4656585853 | 31.1446306866 | 977 | 152650 | -94.05 | 3.83 | 88.27 | 0.16 | 2.62 | 1587 |
| 2024-09-20 22:21:41.884 | MS1 | 121.4656746414 | 31.1446214524 | 303 | 152650 | -93.03 | 6.46 | 88.47 | 0.07 | 2.18 | 1594 |
| 2024-09-20 22:21:42.985 | MS1 | 121.4656603336 | 31.1446368657 | 964 | 152650 | -96.85 | 4.84 | 87.50 | 0.11 | 2.96 | 1583 |

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
| 3213817 | 2 | 121.4754822264 | 31.1526052378 | 79 | 0 | 4 | 14.6 | TDD | 259 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3215249 | 7 | 121.4706563443 | 31.1471458844 | 101 | 5 | 1 | 25.8 | FDD | 964 | n1 | 152650 | 30M | 4T4R | 19 | 152650 |
| 3215833 | 3 | 121.4651250351 | 31.1510008430 | 145 | 1 | 8 | 29.2 | TDD | 722 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3218308 | 5 | 121.4720648376 | 31.1444546387 | 40 | 14 | 12 | 10.9 | TDD | 156 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3222332 | 12 | 121.4658813482 | 31.1513360995 | 215 | 3 | 12 | 1.4 | FDD | 443 | n1 | 152650 | 30M | 4T4R | 19 | 152650 |
| 3225812 | 1 | 121.4664389669 | 31.1462729053 | 118 | 8 | 0 | 21.0 | TDD | 416 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3225817 | 6 | 121.4739286420 | 31.1459923866 | 253 | 7 | 3 | 6.4 | TDD | 894 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3225939 | 9 | 121.4716942965 | 31.1492900674 | 34 | 0 | 12 | 14.5 | FDD | 303 | n1 | 152650 | 30M | 4T4R | 26 | 152650 |
| 3241496 | 10 | 121.4735768408 | 31.1472450291 | 245 | 4 | 2 | 20.8 | FDD | 977 | n1 | 152650 | 30M | 4T4R | 28 | 152650 |
| 3244143 | 8 | 121.4732087503 | 31.1481389171 | 114 | 13 | 7 | 21.4 | FDD | 363 | n1 | 152650 | 30M | 4T4R | 11 | 152650 |
| 3247430 | 13 | 121.4718808395 | 31.1539812259 | 171 | 14 | 2 | 16.7 | FDD | 508 | n1 | 152650 | 30M | 4T4R | 28 | 152650 |
| 3263592 | 4 | 121.4725755315 | 31.1545571121 | 182 | 2 | 6 | 7.8 | TDD | 56 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3279927 | 11 | 121.4719128727 | 31.1537026263 | 17 | 6 | 8 | 20.2 | FDD | 984 | n1 | 152650 | 30M | 4T4R | 24 | 152650 |

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
| 2024-09-20 22:21:31.321 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.346 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.472 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.472 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.149 | NREventA2 | measId:1;ServCellPCI:710;Se... |
| 2024-09-20 22:21:35.292 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.536 | NREventA5 | measId:3;ServCellPCI:710;Se... |
| 2024-09-20 22:21:35.607 | NRHandoverAttempt | SourcePCI:710;SourceNR-ARFC... |
| 2024-09-20 22:21:35.639 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.649 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:35.789 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.789 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3225812 | 1 | 9.8448 | 11.5787 | -116.7744 | 13.7102 | 155.2437 | 0.0065 | 0.0097 |
| 2024_09_20 22:00 | 3213817 | 2 | 16.4300 | 14.0593 | -115.0619 | 18.5103 | 181.9878 | 0.0187 | 0.0172 |
| 2024_09_20 22:00 | 3215833 | 3 | 12.6468 | 15.4315 | -116.2793 | 15.8147 | 123.3173 | 0.0031 | 0.0165 |
| 2024_09_20 22:00 | 3263592 | 4 | 7.9063 | 13.3167 | -114.1811 | 11.3242 | 171.8160 | 0.0055 | 0.0082 |
| 2024_09_20 22:00 | 3218308 | 5 | 18.2245 | 15.5922 | -116.7956 | 9.5667 | 150.6212 | 0.0025 | 0.0113 |
| 2024_09_20 22:00 | 3225817 | 6 | 12.9613 | 11.3660 | -115.9919 | 14.2608 | 190.8963 | 0.0018 | 0.0064 |
| 2024_09_20 22:00 | 3215249 | 7 | 12.5237 | 16.5880 | -115.4499 | 4.8552 | 25.4203 | 0.0191 | 0.0184 |
| 2024_09_20 22:00 | 3244143 | 8 | 8.1418 | 16.4641 | -116.8146 | 4.8473 | 33.9355 | 0.0111 | 0.0128 |
| 2024_09_20 22:00 | 3225939 | 9 | 17.7169 | 6.1822 | -114.3149 | 4.8944 | 28.2114 | 0.0018 | 0.0105 |
| 2024_09_20 22:00 | 3241496 | 10 | 6.1164 | 11.7467 | -114.8210 | 3.3034 | 47.4588 | 0.0130 | 0.0087 |
| 2024_09_20 22:00 | 3279927 | 11 | 10.3091 | 18.0692 | -115.2352 | 4.8179 | 59.6964 | 0.0036 | 0.0084 |
| 2024_09_20 22:00 | 3222332 | 12 | 10.3409 | 9.7059 | -115.8987 | 4.1426 | 26.2714 | 0.0029 | 0.0100 |
| 2024_09_20 22:00 | 3247430 | 13 | 17.0629 | 18.7540 | -114.6933 | 4.0730 | 28.1237 | 0.0048 | 0.0097 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412651_DEFA15C5 | 504990 | 259 | -96.0 | 504990 | 56 | -90.6 | 504990 | 894 | -96.1 | 504990 | 416 |
| MR_1774412651_9A978BF4 | 152650 | 964 | -86.4 | 152650 | 508 | -90.9 | 152650 | 363 | -98.0 | 152650 | 984 |
| MR_1774412651_2865FC3A | 152650 | 964 | -86.4 | 152650 | 508 | -93.4 | 152650 | 363 | -98.9 | 152650 | 984 |
| MR_1774412651_61A7BD39 | 152650 | 964 | -87.4 | 152650 | 508 | -91.9 | 152650 | 363 | -100.7 | 152650 | 984 |
| MR_1774412651_DDEF8CD6 | 504990 | 259 | -94.9 | 504990 | 56 | -91.7 | 504990 | 894 | -98.8 | 504990 | 416 |
| MR_1774412651_9E00C995 | 152650 | 964 | -87.7 | 152650 | 508 | -91.7 | 152650 | 363 | -97.4 | 152650 | 984 |
| MR_1774412651_C06D475C | 152650 | 964 | -85.8 | 152650 | 508 | -92.4 | 152650 | 363 | -98.7 | 152650 | 984 |
| MR_1774412651_5EDA2BAF | 504990 | 259 | -96.3 | 504990 | 56 | -91.1 | 504990 | 894 | -95.7 | 504990 | 416 |

> *... 2개 열 생략 (전체 14열)*

---
