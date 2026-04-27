# Track A 문제 분석 — train[1150]~train[1159]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[1150] ~ train[1159] (10개)

## 목차

1. [문제 1150: `7fd5973d-640...`](#1150) — single-answer, 정답: C10
2. [문제 1151: `d7c9cc7c-c81...`](#1151) — single-answer, 정답: C11
3. [문제 1152: `edeb769a-280...`](#1152) — single-answer, 정답: C15
4. [문제 1153: `126877f7-f33...`](#1153) — multiple-answer, 정답: C5|C8|C14|C21
5. [문제 1154: `b92e4ba1-0c6...`](#1154) — multiple-answer, 정답: C11|C19
6. [문제 1155: `b6c6a59a-8cf...`](#1155) — single-answer, 정답: C21
7. [문제 1156: `bbd791a9-040...`](#1156) — single-answer, 정답: C7
8. [문제 1157: `4d06b726-985...`](#1157) — single-answer, 정답: C17
9. [문제 1158: `23c8a4ea-6ba...`](#1158) — single-answer, 정답: C14
10. [문제 1159: `9627c5d2-dc4...`](#1159) — single-answer, 정답: C19

---

### 문제 1150: `7fd5973d-640...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `7fd5973d-6409-4dc6-ae5b-b44022e8a12b` |
| Tag | **single-answer** |
| 정답 | **C10** |
| C10 의미 | Lift the tilt angle  of 3249496_3 by 4 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1150] topology](images/train_1150.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3238015_4 by 5 degrees
- `C2`: Add neighbor relationship between 3238015_4 and 3256133_1
- `C3`: Decrease transmission power for 3256133_1
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3238015_4
- `C5`: Adjust the azimuth of 3249496_3 by 50 degrees
- `C6`: Press down the tilt angle of 3238015_4 by 5 degrees
- `C7`: Press down the tilt angle  of 3249496_3 by 4 degrees
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3256133_1
- `C9`: Decrease A3 Offset threshold for 3238015_4
- `C10`: Lift the tilt angle  of 3249496_3 by 4 degrees **← 정답**
- `C11`: Increase transmission power for 3238015_4
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3238015_4
- `C13`: Check test server and transmission issues
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Add neighbor relationship between 3249496_3 and 3256133_1
- `C16`: Increase A3 Offset threshold for 3238015_4
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3256133_1
- `C18`: Increase transmission power for 3256133_1
- `C19`: Increase A3 Offset threshold for 3256133_1
- `C20`: Adjust the azimuth of 3238015_4 by 39 degrees
- `C21`: Decrease transmission power for 3238015_4
- `C22`: Decrease A3 Offset threshold for 3256133_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.259 | MS1 | 121.4656588324 | 31.1446272719 | 839 | 504990 | -86.71 | 12.05 | 454.10 | 0.17 | 2.92 | 1593 |
| 2024-09-20 22:21:32.743 | MS1 | 121.4656645217 | 31.1446357033 | 839 | 504990 | -85.43 | 13.03 | 549.90 | 0.11 | 2.86 | 1570 |
| 2024-09-20 22:21:33.812 | MS1 | 121.4656729146 | 31.1446298655 | 839 | 504990 | -89.20 | 15.13 | 507.83 | 0.04 | 2.14 | 1569 |
| 2024-09-20 22:21:34.840 | MS1 | 121.4656720147 | 31.1446362252 | 839 | 504990 | -88.62 | 15.57 | 94.40 | 0.13 | 2.85 | 1598 |
| 2024-09-20 22:21:35.743 | MS1 | 121.4656678577 | 31.1446333271 | 839 | 504990 | -89.79 | 17.08 | 88.30 | 0.03 | 2.13 | 1569 |
| 2024-09-20 22:21:36.308 | MS1 | 121.4656591235 | 31.1446356059 | 839 | 504990 | -87.68 | 17.84 | 87.77 | 0.12 | 2.42 | 1597 |
| 2024-09-20 22:21:37.937 | MS1 | 121.4656647701 | 31.1446186178 | 839 | 504990 | -89.22 | 8.59 | 82.72 | 0.03 | 2.55 | 1585 |
| 2024-09-20 22:21:38.191 | MS1 | 121.4656613661 | 31.1446196826 | 839 | 504990 | -92.53 | 7.17 | 56.31 | 0.14 | 2.74 | 1587 |
| 2024-09-20 22:21:39.229 | MS1 | 121.4656615459 | 31.1446305121 | 839 | 504990 | -91.66 | 10.45 | 65.80 | 0.16 | 2.60 | 1570 |
| 2024-09-20 22:21:40.500 | MS1 | 121.4656649334 | 31.1446325026 | 839 | 504990 | -90.77 | 12.42 | 536.77 | 0.17 | 2.56 | 1570 |
| 2024-09-20 22:21:41.770 | MS1 | 121.4656664051 | 31.1446346037 | 839 | 504990 | -90.46 | 12.22 | 348.04 | 0.03 | 2.33 | 1592 |
| 2024-09-20 22:21:42.697 | MS1 | 121.4656581926 | 31.1446310546 | 839 | 504990 | -93.69 | 12.36 | 558.00 | 0.08 | 2.89 | 1569 |

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
| 3216247 | 2 | 121.4723708482 | 31.1504469183 | 189 | 15 | 3 | 34.0 | TDD | 640 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3238015 | 4 | 121.4641570458 | 31.1546654437 | 212 | 3 | 5 | 47.7 | TDD | 839 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3249496 | 3 | 121.4679816026 | 31.1465929032 | 50 | 8 | 10 | 46.8 | TDD | 638 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3256133 | 1 | 121.4704476010 | 31.1496496449 | 327 | 2 | 3 | 25.0 | TDD | 504 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |

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
| 2024-09-20 22:21:31.374 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.399 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.527 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.527 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.273 | NREventA3 | measId:2;ServCellPCI:6;Serv... |
| 2024-09-20 22:21:38.513 | NRHandoverAttempt | SourcePCI:6;SourceNR-ARFCN:... |
| 2024-09-20 22:21:38.552 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.565 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.672 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.672 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3256133 | 1 | 9.6634 | 10.1171 | -116.9244 | 15.7173 | 160.2696 | 0.0035 | 0.0003 |
| 2024_09_20 22:00 | 3216247 | 2 | 9.9270 | 19.6807 | -117.3020 | 12.0505 | 174.2031 | 0.0050 | 0.0122 |
| 2024_09_20 22:00 | 3249496 | 3 | 10.0989 | 12.2932 | -115.4050 | 13.8954 | 80.2803 | 0.0063 | 0.0190 |
| 2024_09_20 22:00 | 3238015 | 4 | 94.7463 | 82.0434 | -116.8423 | 18.8019 | 82.5134 | 0.0002 | 0.0138 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416852_CB070B09 | 504990 | 839 | -89.7 | 504990 | 504 | -93.2 | 504990 | 638 | -102.5 | 504990 | 640 |
| MR_1774416852_912300A9 | 504990 | 839 | -88.4 | 504990 | 504 | -94.0 | 504990 | 638 | -99.1 | 504990 | 640 |
| MR_1774416852_8CDFD25F | 504990 | 839 | -88.9 | 504990 | 504 | -95.1 | 504990 | 638 | -101.4 | 504990 | 640 |
| MR_1774416852_2B27F8E9 | 504990 | 839 | -89.7 | 504990 | 504 | -95.0 | 504990 | 638 | -102.0 | 504990 | 640 |
| MR_1774416852_CAEE6C12 | 504990 | 839 | -86.7 | 504990 | 504 | -92.1 | 504990 | 638 | -99.5 | 504990 | 640 |
| MR_1774416852_85E2F8AF | 504990 | 839 | -88.1 | 504990 | 504 | -91.6 | 504990 | 638 | -98.7 | 504990 | 640 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1151: `d7c9cc7c-c81...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `d7c9cc7c-c819-4f6e-9360-9c62d3f309fc` |
| Tag | **single-answer** |
| 정답 | **C11** |
| C11 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1151] topology](images/train_1151.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3241373_3 by 50 degrees
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3228479_2
- `C3`: Check test server and transmission issues
- `C4`: Lift the tilt angle of 3228479_2 by 2 degrees
- `C5`: Adjust the azimuth of 3228479_2 by 50 degrees
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3228479_2
- `C7`: Decrease A3 Offset threshold for 3241373_3
- `C8`: Press down the tilt angle  of 3241373_3 by 10 degrees
- `C9`: Press down the tilt angle of 3228479_2 by 2 degrees
- `C10`: Increase transmission power for 3241373_3
- `C11`: Insufficient data; more data is needed for judgment. **← 정답**
- `C12`: Increase A3 Offset threshold for 3241373_3
- `C13`: Increase transmission power for 3228479_2
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3241373_3
- `C15`: Lift the tilt angle  of 3241373_3 by 10 degrees
- `C16`: Decrease transmission power for 3228479_2
- `C17`: Add neighbor relationship between 3228479_2 and 3241373_3
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3241373_3
- `C19`: Decrease A3 Offset threshold for 3228479_2
- `C20`: Decrease transmission power for 3241373_3
- `C21`: Add neighbor relationship between 3238628_4 and 3241373_3
- `C22`: Increase A3 Offset threshold for 3228479_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.423 | MS1 | 121.4656768755 | 31.1446304508 | 690 | 504990 | -86.97 | 14.00 | 573.72 | 0.10 | 2.35 | 1580 |
| 2024-09-20 22:21:32.629 | MS1 | 121.4656637549 | 31.1446209486 | 690 | 504990 | -90.46 | 14.54 | 477.04 | 0.14 | 2.91 | 1580 |
| 2024-09-20 22:21:33.981 | MS1 | 121.4656614581 | 31.1446355133 | 690 | 504990 | -88.50 | 14.61 | 413.50 | 0.03 | 2.03 | 1585 |
| 2024-09-20 22:21:34.772 | MS1 | 121.4656674993 | 31.1446193834 | 690 | 504990 | -88.05 | 16.62 | 47.09 | 0.06 | 2.06 | 1584 |
| 2024-09-20 22:21:35.533 | MS1 | 121.4656662921 | 31.1446253009 | 690 | 504990 | -89.62 | 13.07 | 65.07 | 0.17 | 2.68 | 1576 |
| 2024-09-20 22:21:36.233 | MS1 | 121.4656604731 | 31.1446284323 | 690 | 504990 | -90.13 | 13.12 | 73.04 | 0.02 | 2.64 | 1586 |
| 2024-09-20 22:21:37.218 | MS1 | 121.4656665801 | 31.1446371244 | 690 | 504990 | -92.12 | 7.10 | 65.43 | 0.06 | 2.07 | 1561 |
| 2024-09-20 22:21:38.570 | MS1 | 121.4656673183 | 31.1446300038 | 690 | 504990 | -89.14 | 9.33 | 75.24 | 0.20 | 2.20 | 1590 |
| 2024-09-20 22:21:39.567 | MS1 | 121.4656609517 | 31.1446290807 | 690 | 504990 | -90.65 | 10.37 | 61.70 | 0.04 | 2.06 | 1594 |
| 2024-09-20 22:21:40.992 | MS1 | 121.4656623487 | 31.1446374674 | 690 | 504990 | -91.84 | 11.06 | 400.51 | 0.13 | 2.39 | 1565 |
| 2024-09-20 22:21:41.399 | MS1 | 121.4656607644 | 31.1446363196 | 690 | 504990 | -93.48 | 11.50 | 424.60 | 0.09 | 2.57 | 1592 |
| 2024-09-20 22:21:42.131 | MS1 | 121.4656699741 | 31.1446244807 | 690 | 504990 | -91.57 | 11.07 | 456.39 | 0.14 | 2.66 | 1567 |

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
| 3228479 | 2 | 121.4723845894 | 31.1552726079 | 60 | 1 | 9 | 18.9 | TDD | 690 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3235918 | 1 | 121.4711638126 | 31.1485213849 | 309 | 7 | 3 | 34.3 | TDD | 632 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3238628 | 4 | 121.4672166341 | 31.1455088834 | 25 | 12 | 9 | 35.1 | TDD | 237 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3241373 | 3 | 121.4643329277 | 31.1469654141 | 40 | 9 | 8 | 21.1 | TDD | 795 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:30.770 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.787 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:30.922 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.922 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.646 | NREventA3 | measId:2;ServCellPCI:580;Se... |
| 2024-09-20 22:21:37.886 | NRHandoverAttempt | SourcePCI:580;SourceNR-ARFC... |
| 2024-09-20 22:21:37.929 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.939 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.063 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.063 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3235918 | 1 | 93.2527 | 88.7223 | -115.9987 | 7.0286 | 109.2110 | 0.0021 | 0.0006 |
| 2024_09_19 22:00 | 3228479 | 2 | 83.4543 | 91.7553 | -116.5540 | 19.9276 | 191.3604 | 0.0048 | 0.0119 |
| 2024_09_19 22:00 | 3241373 | 3 | 90.3885 | 92.4194 | -114.3329 | 13.9161 | 121.0994 | 0.0141 | 0.0135 |
| 2024_09_19 22:00 | 3238628 | 4 | 87.1769 | 81.4188 | -117.0126 | 19.3335 | 175.2519 | 0.0019 | 0.0010 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413283_11A82B7F | 504990 | 690 | -88.9 | 504990 | 795 | -92.7 | 504990 | 237 | -98.5 | 504990 | 632 |
| MR_1774413283_E7E897A8 | 504990 | 690 | -88.8 | 504990 | 795 | -91.9 | 504990 | 237 | -98.7 | 504990 | 632 |
| MR_1774413283_FFD1619E | 504990 | 690 | -88.7 | 504990 | 795 | -92.1 | 504990 | 237 | -100.3 | 504990 | 632 |
| MR_1774413283_7A52E9A2 | 504990 | 690 | -86.5 | 504990 | 795 | -92.2 | 504990 | 237 | -99.8 | 504990 | 632 |
| MR_1774413283_E4A72998 | 504990 | 690 | -89.7 | 504990 | 795 | -95.0 | 504990 | 237 | -98.4 | 504990 | 632 |
| MR_1774413283_64BD7585 | 504990 | 690 | -86.6 | 504990 | 795 | -94.9 | 504990 | 237 | -97.4 | 504990 | 632 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1152: `edeb769a-280...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `edeb769a-280b-4c69-b92e-ec220d6bc197` |
| Tag | **single-answer** |
| 정답 | **C15** |
| C15 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1152] topology](images/train_1152.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3245300_1 by 10 degrees
- `C2`: Decrease transmission power for 3273155_2
- `C3`: Add neighbor relationship between 3243852_4 and 3273155_2
- `C4`: Press down the tilt angle  of 3273155_2 by 10 degrees
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3245300_1
- `C6`: Lift the tilt angle of 3245300_1 by 10 degrees
- `C7`: Adjust the azimuth of 3273155_2 by 18 degrees
- `C8`: Increase transmission power for 3273155_2
- `C9`: Adjust the azimuth of 3245300_1 by 39 degrees
- `C10`: Increase A3 Offset threshold for 3245300_1
- `C11`: Increase transmission power for 3245300_1
- `C12`: Increase A3 Offset threshold for 3273155_2
- `C13`: Decrease A3 Offset threshold for 3245300_1
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3245300_1
- `C15`: Insufficient data; more data is needed for judgment. **← 정답**
- `C16`: Lift the tilt angle  of 3273155_2 by 10 degrees
- `C17`: Decrease A3 Offset threshold for 3273155_2
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3273155_2
- `C19`: Decrease transmission power for 3245300_1
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3273155_2
- `C21`: Add neighbor relationship between 3245300_1 and 3273155_2
- `C22`: Check test server and transmission issues

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.631 | MS1 | 121.4656607953 | 31.1446244818 | 17 | 504990 | -90.27 | 14.94 | 374.76 | 0.05 | 2.54 | 1563 |
| 2024-09-20 22:21:32.974 | MS1 | 121.4656618800 | 31.1446358028 | 17 | 504990 | -91.11 | 13.93 | 430.02 | 0.13 | 2.11 | 1560 |
| 2024-09-20 22:21:33.997 | MS1 | 121.4656721330 | 31.1446205574 | 17 | 504990 | -90.53 | 14.32 | 474.09 | 0.02 | 2.98 | 1565 |
| 2024-09-20 22:21:34.490 | MS1 | 121.4656652708 | 31.1446360604 | 17 | 504990 | -85.40 | 12.30 | 96.08 | 0.15 | 2.22 | 1561 |
| 2024-09-20 22:21:35.401 | MS1 | 121.4656702448 | 31.1446227773 | 17 | 504990 | -90.69 | 12.58 | 91.11 | 0.04 | 2.86 | 1590 |
| 2024-09-20 22:21:36.532 | MS1 | 121.4656706654 | 31.1446316381 | 17 | 504990 | -91.28 | 13.66 | 59.92 | 0.10 | 2.26 | 1588 |
| 2024-09-20 22:21:37.437 | MS1 | 121.4656643297 | 31.1446251686 | 17 | 504990 | -89.36 | 12.10 | 87.26 | 0.08 | 2.71 | 1574 |
| 2024-09-20 22:21:38.469 | MS1 | 121.4656735645 | 31.1446333883 | 17 | 504990 | -93.19 | 10.07 | 87.17 | 0.17 | 2.77 | 1591 |
| 2024-09-20 22:21:39.221 | MS1 | 121.4656707614 | 31.1446321058 | 17 | 504990 | -93.88 | 8.07 | 77.76 | 0.19 | 2.13 | 1573 |
| 2024-09-20 22:21:40.758 | MS1 | 121.4656580150 | 31.1446258826 | 17 | 504990 | -89.42 | 10.84 | 385.41 | 0.10 | 2.20 | 1568 |
| 2024-09-20 22:21:41.807 | MS1 | 121.4656760372 | 31.1446377177 | 17 | 504990 | -91.87 | 7.37 | 428.69 | 0.06 | 2.29 | 1597 |
| 2024-09-20 22:21:42.945 | MS1 | 121.4656611067 | 31.1446344697 | 17 | 504990 | -89.35 | 8.66 | 489.52 | 0.13 | 2.95 | 1580 |

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
| 3242972 | 3 | 121.4646995906 | 31.1442975319 | 46 | 9 | 2 | 22.7 | TDD | 740 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3243852 | 4 | 121.4753082758 | 31.1485054370 | 208 | 14 | 3 | 24.4 | TDD | 550 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3245300 | 1 | 121.4690874818 | 31.1469330340 | 193 | 15 | 8 | 31.8 | TDD | 17 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3273155 | 2 | 121.4740344368 | 31.1504368713 | 213 | 9 | 1 | 39.0 | TDD | 878 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |

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
| 2024-09-20 22:21:31.433 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.556 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.556 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.212 | NREventA3 | measId:2;ServCellPCI:995;Se... |
| 2024-09-20 22:21:38.452 | NRHandoverAttempt | SourcePCI:995;SourceNR-ARFC... |
| 2024-09-20 22:21:38.496 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.508 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.648 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.648 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3245300 | 1 | 92.3560 | 93.0058 | -115.2002 | 11.2012 | 108.5143 | 0.0130 | 0.0040 |
| 2024_09_19 22:00 | 3273155 | 2 | 94.2121 | 94.8462 | -117.5019 | 7.9227 | 103.8789 | 0.0028 | 0.0033 |
| 2024_09_19 22:00 | 3242972 | 3 | 82.0227 | 89.1863 | -114.4746 | 16.2563 | 106.4223 | 0.0146 | 0.0040 |
| 2024_09_19 22:00 | 3243852 | 4 | 89.7472 | 91.2916 | -116.0523 | 9.6016 | 107.8446 | 0.0104 | 0.0100 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413048_1CBDAD72 | 504990 | 17 | -84.6 | 504990 | 878 | -87.9 | 504990 | 550 | -101.9 | 504990 | 740 |
| MR_1774413048_F72D25EB | 504990 | 17 | -85.7 | 504990 | 878 | -86.4 | 504990 | 550 | -101.4 | 504990 | 740 |
| MR_1774413048_84828D0A | 504990 | 17 | -85.0 | 504990 | 878 | -86.0 | 504990 | 550 | -98.4 | 504990 | 740 |
| MR_1774413048_475879AF | 504990 | 17 | -85.0 | 504990 | 878 | -87.3 | 504990 | 550 | -101.6 | 504990 | 740 |
| MR_1774413048_789BB2A5 | 504990 | 17 | -87.4 | 504990 | 878 | -87.8 | 504990 | 550 | -100.5 | 504990 | 740 |
| MR_1774413048_0F966250 | 504990 | 17 | -84.6 | 504990 | 878 | -87.0 | 504990 | 550 | -99.1 | 504990 | 740 |
| MR_1774413048_D036395C | 504990 | 17 | -86.4 | 504990 | 878 | -86.5 | 504990 | 550 | -101.4 | 504990 | 740 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1153: `126877f7-f33...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `126877f7-f338-4283-bd26-375829888301` |
| Tag | **multiple-answer** |
| 정답 | **C5|C8|C14|C21** |
| C5 의미 | Increase A3 Offset threshold for 3275462_3 |
| C8 의미 | Increase A3 Offset threshold for 3269240_5 |
| C14 의미 | Decrease transmission power for 3275462_3 |
| C21 의미 | Press down the tilt angle  of 3275462_3 by 5 degrees |
| 패턴 분류 | **P2 Ping-pong** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1153] topology](images/train_1153.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 5 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 5개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Check test server and transmission issues
- `C2`: Add neighbor relationship between 3269240_5 and 3275462_3
- `C3`: Decrease transmission power for 3269240_5
- `C4`: Decrease A3 Offset threshold for 3269240_5
- `C5`: Increase A3 Offset threshold for 3275462_3 **← 정답**
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3269240_5
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3275462_3
- `C8`: Increase A3 Offset threshold for 3269240_5 **← 정답**
- `C9`: Insufficient data; more data is needed for judgment.
- `C10`: Add neighbor relationship between 3261205_1 and 3275462_3
- `C11`: Increase transmission power for 3275462_3
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3269240_5
- `C13`: Lift the tilt angle  of 3275462_3 by 5 degrees
- `C14`: Decrease transmission power for 3275462_3 **← 정답**
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3275462_3
- `C16`: Adjust the azimuth of 3275462_3 by 42 degrees
- `C17`: Lift the tilt angle of 3269240_5 by 4 degrees
- `C18`: Decrease A3 Offset threshold for 3275462_3
- `C19`: Adjust the azimuth of 3269240_5 by 2 degrees
- `C20`: Increase transmission power for 3269240_5
- `C21`: Press down the tilt angle  of 3275462_3 by 5 degrees **← 정답**
- `C22`: Press down the tilt angle of 3269240_5 by 4 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.951 | MS1 | 121.4656747926 | 31.1446307171 | 829 | 504990 | -78.21 | 13.36 | 457.08 | 0.12 | 2.10 | 1566 |
| 2024-09-20 22:21:32.707 | MS1 | 121.4656722500 | 31.1446295065 | 829 | 504990 | -79.11 | 16.72 | 580.01 | 0.15 | 2.16 | 1568 |
| 2024-09-20 22:21:33.171 | MS1 | 121.4656665815 | 31.1446226564 | 829 | 504990 | -79.43 | 14.50 | 453.48 | 0.02 | 2.54 | 1571 |
| 2024-09-20 22:21:34.743 | MS1 | 121.4656707249 | 31.1446315907 | 758 | 504990 | -83.56 | 1.51 | 69.33 | 0.00 | 1.07 | 1591 |
| 2024-09-20 22:21:35.796 | MS1 | 121.4656697645 | 31.1446188102 | 758 | 504990 | -89.28 | 2.48 | 32.40 | 0.19 | 1.20 | 1592 |
| 2024-09-20 22:21:36.952 | MS1 | 121.4656621517 | 31.1446198604 | 829 | 504990 | -82.44 | 1.35 | 49.62 | 0.00 | 1.19 | 1587 |
| 2024-09-20 22:21:37.929 | MS1 | 121.4656710894 | 31.1446281774 | 829 | 504990 | -89.29 | 3.66 | 83.47 | 0.19 | 1.01 | 1593 |
| 2024-09-20 22:21:38.303 | MS1 | 121.4656666170 | 31.1446220706 | 758 | 504990 | -83.53 | 3.26 | 68.56 | 0.11 | 1.50 | 1573 |
| 2024-09-20 22:21:39.153 | MS1 | 121.4656701361 | 31.1446197537 | 758 | 504990 | -87.41 | 4.07 | 62.91 | 0.16 | 1.29 | 1590 |
| 2024-09-20 22:21:40.455 | MS1 | 121.4656646520 | 31.1446245067 | 758 | 504990 | -79.09 | 12.68 | 511.95 | 0.04 | 2.21 | 1570 |
| 2024-09-20 22:21:41.226 | MS1 | 121.4656694995 | 31.1446205315 | 758 | 504990 | -75.36 | 13.39 | 601.54 | 0.09 | 2.58 | 1589 |
| 2024-09-20 22:21:42.310 | MS1 | 121.4656595420 | 31.1446317340 | 758 | 504990 | -84.97 | 17.45 | 315.30 | 0.17 | 2.01 | 1570 |

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
| 3216283 | 4 | 121.4714259826 | 31.1478424387 | 330 | 12 | 3 | 38.6 | TDD | 758 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3241156 | 2 | 121.4656795125 | 31.1553839572 | 90 | 3 | 2 | 17.5 | TDD | 233 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3261205 | 1 | 121.4749469250 | 31.1488858982 | 44 | 5 | 8 | 39.1 | TDD | 327 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3269240 | 5 | 121.4681767917 | 31.1509592946 | 197 | 2 | 12 | 32.4 | TDD | 829 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3275462 | 3 | 121.4653567629 | 31.1529589583 | 136 | 3 | 11 | 24.6 | TDD | 908 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:31.226 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.249 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.382 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.382 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.037 | NREventA3 | measId:2;ServCellPCI:942;Se... |
| 2024-09-20 22:21:34.277 | NRHandoverAttempt | SourcePCI:942;SourceNR-ARFC... |
| 2024-09-20 22:21:34.313 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:34.327 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:34.456 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:34.456 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:36.037 | NREventA3 | measId:2;ServCellPCI:504;Se... |
| 2024-09-20 22:21:36.277 | NRHandoverAttempt | SourcePCI:504;SourceNR-ARFC... |
| 2024-09-20 22:21:36.325 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:36.339 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:36.442 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.442 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.037 | NREventA3 | measId:2;ServCellPCI:942;Se... |
| 2024-09-20 22:21:38.277 | NRHandoverAttempt | SourcePCI:942;SourceNR-ARFC... |
| 2024-09-20 22:21:38.309 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.323 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.431 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.431 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3261205 | 1 | 10.9377 | 5.6106 | -116.4406 | 5.4460 | 101.0221 | 0.0128 | 0.0070 |
| 2024_09_20 22:00 | 3241156 | 2 | 17.0052 | 14.2056 | -114.1861 | 12.3445 | 172.6689 | 0.0085 | 0.0081 |
| 2024_09_20 22:00 | 3275462 | 3 | 6.6627 | 18.2371 | -114.9306 | 17.9349 | 135.0880 | 0.0059 | 0.0016 |
| 2024_09_20 22:00 | 3216283 | 4 | 14.4115 | 17.6671 | -117.0746 | 16.2409 | 180.3381 | 0.0156 | 0.0199 |
| 2024_09_20 22:00 | 3269240 | 5 | 8.5733 | 7.8848 | -117.1893 | 18.0607 | 127.6219 | 0.0196 | 0.0000 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416474_85FB59E4 | 504990 | 758 | -81.9 | 504990 | 829 | -81.8 | 504990 | 908 | -82.2 | 504990 | 327 |
| MR_1774416474_7D4C5149 | 504990 | 758 | -82.3 | 504990 | 829 | -84.2 | 504990 | 908 | -85.0 | 504990 | 327 |
| MR_1774416474_35F01E64 | 504990 | 829 | -84.8 | 504990 | 758 | -82.6 | 504990 | 908 | -82.2 | 504990 | 327 |
| MR_1774416474_8D8DAE3D | 504990 | 829 | -84.3 | 504990 | 758 | -81.1 | 504990 | 908 | -85.8 | 504990 | 327 |
| MR_1774416474_856EA09E | 504990 | 829 | -84.6 | 504990 | 758 | -82.7 | 504990 | 908 | -84.0 | 504990 | 327 |
| MR_1774416474_64CE86DD | 504990 | 829 | -84.3 | 504990 | 758 | -84.1 | 504990 | 908 | -82.6 | 504990 | 327 |
| MR_1774416474_10DC1096 | 504990 | 829 | -82.0 | 504990 | 758 | -81.2 | 504990 | 908 | -85.9 | 504990 | 327 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1154: `b92e4ba1-0c6...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `b92e4ba1-0c6d-437d-bac5-56627140d9e8` |
| Tag | **multiple-answer** |
| 정답 | **C11|C19** |
| C11 의미 | Increase transmission power for 3219869_1 |
| C19 의미 | Adjust the azimuth of 3219869_1 by 50 degrees |
| 패턴 분류 | **P4 Coverage (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1154] topology](images/train_1154.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3219869_1
- `C2`: Decrease transmission power for 3222651_4
- `C3`: Decrease A3 Offset threshold for 3222651_4
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3219869_1
- `C5`: Decrease A3 Offset threshold for 3219869_1
- `C6`: Increase A3 Offset threshold for 3222651_4
- `C7`: Decrease transmission power for 3219869_1
- `C8`: Press down the tilt angle  of 3222651_4 by 4 degrees
- `C9`: Check test server and transmission issues
- `C10`: Lift the tilt angle  of 3222651_4 by 4 degrees
- `C11`: Increase transmission power for 3219869_1 **← 정답**
- `C12`: Adjust the azimuth of 3222651_4 by 14 degrees
- `C13`: Increase transmission power for 3222651_4
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3222651_4
- `C15`: Add neighbor relationship between 3247715_3 and 3222651_4
- `C16`: Lift the tilt angle of 3219869_1 by 10 degrees
- `C17`: Insufficient data; more data is needed for judgment.
- `C18`: Add neighbor relationship between 3219869_1 and 3222651_4
- `C19`: Adjust the azimuth of 3219869_1 by 50 degrees **← 정답**
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3222651_4
- `C21`: Increase A3 Offset threshold for 3219869_1
- `C22`: Press down the tilt angle of 3219869_1 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.357 | MS1 | 121.4656627145 | 31.1446373625 | 112 | 504990 | -87.50 | 14.85 | 478.53 | 0.09 | 2.95 | 1593 |
| 2024-09-20 22:21:32.270 | MS1 | 121.4656750986 | 31.1446241334 | 112 | 504990 | -86.04 | 17.44 | 586.07 | 0.01 | 2.80 | 1582 |
| 2024-09-20 22:21:33.204 | MS1 | 121.4656729461 | 31.1446261086 | 112 | 504990 | -94.67 | 13.80 | 407.99 | 0.06 | 2.74 | 1580 |
| 2024-09-20 22:21:34.823 | MS1 | 121.4656629715 | 31.1446296902 | 112 | 504990 | -100.99 | 1.07 | 37.40 | 0.18 | 1.44 | 1591 |
| 2024-09-20 22:21:35.816 | MS1 | 121.4656660317 | 31.1446208886 | 112 | 504990 | -104.62 | 1.62 | 72.63 | 0.06 | 1.28 | 1562 |
| 2024-09-20 22:21:36.476 | MS1 | 121.4656619769 | 31.1446339845 | 112 | 504990 | -105.73 | 0.99 | 38.95 | 0.16 | 1.22 | 1599 |
| 2024-09-20 22:21:37.223 | MS1 | 121.4656611840 | 31.1446261175 | 112 | 504990 | -100.50 | -0.56 | 38.51 | 0.17 | 1.41 | 1569 |
| 2024-09-20 22:21:38.299 | MS1 | 121.4656761544 | 31.1446351764 | 112 | 504990 | -103.76 | 1.66 | 32.05 | 0.10 | 1.41 | 1583 |
| 2024-09-20 22:21:39.226 | MS1 | 121.4656761685 | 31.1446214846 | 112 | 504990 | -106.59 | -1.08 | 72.38 | 0.14 | 1.24 | 1584 |
| 2024-09-20 22:21:40.997 | MS1 | 121.4656718070 | 31.1446338889 | 112 | 504990 | -88.27 | 13.56 | 338.13 | 0.06 | 2.52 | 1569 |
| 2024-09-20 22:21:41.573 | MS1 | 121.4656602742 | 31.1446292897 | 112 | 504990 | -94.02 | 14.84 | 557.46 | 0.06 | 2.04 | 1560 |
| 2024-09-20 22:21:42.150 | MS1 | 121.4656675769 | 31.1446354990 | 112 | 504990 | -89.97 | 13.03 | 362.13 | 0.01 | 2.62 | 1594 |

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
| 3219869 | 1 | 121.4740094760 | 31.1507124830 | 282 | 8 | 4 | 35.5 | TDD | 112 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3222651 | 4 | 121.4671670357 | 31.1536476414 | 174 | 3 | 9 | 24.3 | TDD | 878 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3247715 | 3 | 121.4649314586 | 31.1485290379 | 66 | 11 | 11 | 21.0 | TDD | 869 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3251214 | 2 | 121.4657087271 | 31.1474887470 | 126 | 9 | 10 | 47.1 | TDD | 409 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:30.759 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.775 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:30.923 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.923 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.110 | NREventA2 | measId:1;ServCellPCI:910;Se... |
| 2024-09-20 22:21:34.226 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3219869 | 1 | 13.0630 | 9.0158 | -114.5164 | 13.4350 | 143.4594 | 0.1103 | 0.0022 |
| 2024_09_20 22:00 | 3251214 | 2 | 6.1698 | 11.9758 | -115.7916 | 17.2323 | 88.2472 | 0.0198 | 0.0136 |
| 2024_09_20 22:00 | 3247715 | 3 | 5.7030 | 7.7186 | -115.2170 | 14.5792 | 191.0862 | 0.0054 | 0.0083 |
| 2024_09_20 22:00 | 3222651 | 4 | 6.3305 | 15.4293 | -114.7533 | 15.8772 | 82.9505 | 0.0166 | 0.0029 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412818_7212EB5A | 504990 | 112 | -101.4 | 504990 | 878 | -102.4 | 504990 | 869 | -111.4 | 504990 | 409 |
| MR_1774412818_87836639 | 504990 | 112 | -101.3 | 504990 | 878 | -103.5 | 504990 | 869 | -109.9 | 504990 | 409 |
| MR_1774412818_6D612FB0 | 504990 | 112 | -99.7 | 504990 | 878 | -103.4 | 504990 | 869 | -109.7 | 504990 | 409 |
| MR_1774412818_FF81A40C | 504990 | 112 | -99.3 | 504990 | 878 | -103.9 | 504990 | 869 | -109.3 | 504990 | 409 |
| MR_1774412818_8D59C64B | 504990 | 112 | -103.0 | 504990 | 878 | -104.6 | 504990 | 869 | -110.6 | 504990 | 409 |
| MR_1774412818_2581AB06 | 504990 | 112 | -100.3 | 504990 | 878 | -102.7 | 504990 | 869 | -109.9 | 504990 | 409 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1155: `b6c6a59a-8cf...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `b6c6a59a-8cfb-4d6c-b9b5-5b19abe826c5` |
| Tag | **single-answer** |
| 정답 | **C21** |
| C21 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1155] topology](images/train_1155.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment.
- `C2`: Lift the tilt angle of 3225769_1 by 1 degrees
- `C3`: Decrease transmission power for 3247872_3
- `C4`: Increase transmission power for 3247872_3
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3225769_1
- `C6`: Add neighbor relationship between 3260601_2 and 3247872_3
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3225769_1
- `C8`: Increase A3 Offset threshold for 3247872_3
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3247872_3
- `C10`: Press down the tilt angle  of 3247872_3 by 10 degrees
- `C11`: Press down the tilt angle of 3225769_1 by 1 degrees
- `C12`: Decrease A3 Offset threshold for 3225769_1
- `C13`: Add neighbor relationship between 3225769_1 and 3247872_3
- `C14`: Increase A3 Offset threshold for 3225769_1
- `C15`: Adjust the azimuth of 3225769_1 by 50 degrees
- `C16`: Adjust the azimuth of 3247872_3 by 36 degrees
- `C17`: Increase transmission power for 3225769_1
- `C18`: Decrease transmission power for 3225769_1
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3247872_3
- `C20`: Lift the tilt angle  of 3247872_3 by 10 degrees
- `C21`: Check test server and transmission issues **← 정답**
- `C22`: Decrease A3 Offset threshold for 3247872_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.800 | MS1 | 121.4656610597 | 31.1446287210 | 320 | 504990 | -88.43 | 15.75 | 325.20 | 0.12 | 2.99 | 1585 |
| 2024-09-20 22:21:32.787 | MS1 | 121.4656718406 | 31.1446350074 | 320 | 504990 | -91.06 | 12.14 | 536.50 | 0.13 | 2.13 | 1590 |
| 2024-09-20 22:21:33.900 | MS1 | 121.4656626296 | 31.1446220133 | 320 | 504990 | -86.54 | 16.35 | 509.36 | 0.05 | 2.52 | 1578 |
| 2024-09-20 22:21:34.913 | MS1 | 121.4656728290 | 31.1446373167 | 320 | 504990 | -89.32 | 12.91 | 65.24 | 0.05 | 2.05 | 405 |
| 2024-09-20 22:21:35.334 | MS1 | 121.4656714943 | 31.1446196500 | 320 | 504990 | -88.95 | 12.51 | 63.96 | 0.12 | 2.24 | 410 |
| 2024-09-20 22:21:36.358 | MS1 | 121.4656742044 | 31.1446228854 | 320 | 504990 | -86.90 | 16.29 | 60.46 | 0.16 | 2.24 | 414 |
| 2024-09-20 22:21:37.634 | MS1 | 121.4656704031 | 31.1446378850 | 320 | 504990 | -89.47 | 8.21 | 73.01 | 0.15 | 2.48 | 359 |
| 2024-09-20 22:21:38.105 | MS1 | 121.4656737591 | 31.1446354868 | 320 | 504990 | -91.70 | 12.76 | 42.62 | 0.03 | 2.47 | 500 |
| 2024-09-20 22:21:39.853 | MS1 | 121.4656691190 | 31.1446255377 | 320 | 504990 | -92.47 | 11.10 | 55.69 | 0.01 | 2.11 | 331 |
| 2024-09-20 22:21:40.163 | MS1 | 121.4656657943 | 31.1446357727 | 320 | 504990 | -89.50 | 7.73 | 323.65 | 0.15 | 3.00 | 1599 |
| 2024-09-20 22:21:41.926 | MS1 | 121.4656729092 | 31.1446321392 | 320 | 504990 | -92.20 | 12.06 | 310.97 | 0.16 | 2.54 | 1585 |
| 2024-09-20 22:21:42.951 | MS1 | 121.4656634407 | 31.1446187208 | 320 | 504990 | -92.88 | 9.22 | 448.52 | 0.19 | 2.66 | 1575 |

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
| 3225769 | 1 | 121.4717654776 | 31.1494817539 | 156 | 0 | 11 | 20.2 | TDD | 320 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3247872 | 3 | 121.4645213154 | 31.1462572532 | 185 | 15 | 1 | 33.0 | TDD | 600 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3260601 | 2 | 121.4708284192 | 31.1449789649 | 133 | 8 | 8 | 27.7 | TDD | 785 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3278498 | 4 | 121.4693270436 | 31.1529352676 | 220 | 11 | 11 | 43.4 | TDD | 899 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:31.561 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.582 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.702 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.702 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.434 | NREventA3 | measId:2;ServCellPCI:612;Se... |
| 2024-09-20 22:21:38.674 | NRHandoverAttempt | SourcePCI:612;SourceNR-ARFC... |
| 2024-09-20 22:21:38.721 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.731 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.861 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.861 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3225769 | 1 | 16.4779 | 13.5215 | -117.7610 | 8.6760 | 113.1288 | 0.0116 | 0.0104 |
| 2024_09_20 22:00 | 3260601 | 2 | 19.9702 | 13.6551 | -117.4353 | 12.3533 | 196.7617 | 0.0110 | 0.0047 |
| 2024_09_20 22:00 | 3247872 | 3 | 7.9471 | 19.7823 | -117.6750 | 18.6994 | 138.3388 | 0.0033 | 0.0042 |
| 2024_09_20 22:00 | 3278498 | 4 | 9.5840 | 12.2651 | -115.2979 | 19.4004 | 168.6468 | 0.0034 | 0.0007 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412297_9B6742D9 | 504990 | 320 | -88.9 | 504990 | 600 | -94.4 | 504990 | 785 | -101.5 | 504990 | 899 |
| MR_1774412297_DB4E5EDF | 504990 | 320 | -89.0 | 504990 | 600 | -93.6 | 504990 | 785 | -99.9 | 504990 | 899 |
| MR_1774412297_013664D4 | 504990 | 320 | -87.8 | 504990 | 600 | -94.3 | 504990 | 785 | -101.8 | 504990 | 899 |
| MR_1774412297_10C1E04A | 504990 | 320 | -88.7 | 504990 | 600 | -94.7 | 504990 | 785 | -98.9 | 504990 | 899 |
| MR_1774412297_62F610A8 | 504990 | 320 | -89.9 | 504990 | 600 | -94.7 | 504990 | 785 | -101.3 | 504990 | 899 |
| MR_1774412297_B003B5FE | 504990 | 320 | -89.5 | 504990 | 600 | -91.8 | 504990 | 785 | -99.0 | 504990 | 899 |
| MR_1774412297_B3ACEAEA | 504990 | 320 | -89.6 | 504990 | 600 | -90.9 | 504990 | 785 | -98.7 | 504990 | 899 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1156: `bbd791a9-040...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `bbd791a9-0404-4220-8355-cafbb98dce4b` |
| Tag | **single-answer** |
| 정답 | **C7** |
| C7 의미 | Add neighbor relationship between 3224334_4 and 3253564_3 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1156] topology](images/train_1156.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle  of 3253564_3 by 4 degrees
- `C2`: Adjust the azimuth of 3224334_4 by 50 degrees
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3253564_3
- `C4`: Add neighbor relationship between 3259578_2 and 3253564_3
- `C5`: Decrease A3 Offset threshold for 3224334_4
- `C6`: Decrease transmission power for 3253564_3
- `C7`: Add neighbor relationship between 3224334_4 and 3253564_3 **← 정답**
- `C8`: Check test server and transmission issues
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3253564_3
- `C10`: Increase A3 Offset threshold for 3253564_3
- `C11`: Press down the tilt angle of 3224334_4 by 6 degrees
- `C12`: Lift the tilt angle of 3224334_4 by 6 degrees
- `C13`: Decrease A3 Offset threshold for 3253564_3
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3224334_4
- `C15`: Decrease transmission power for 3224334_4
- `C16`: Increase transmission power for 3224334_4
- `C17`: Increase A3 Offset threshold for 3224334_4
- `C18`: Increase transmission power for 3253564_3
- `C19`: Insufficient data; more data is needed for judgment.
- `C20`: Adjust the azimuth of 3253564_3 by 30 degrees
- `C21`: Press down the tilt angle  of 3253564_3 by 4 degrees
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3224334_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.482 | MS1 | 121.4656649364 | 31.1446234454 | 983 | 504990 | -78.74 | 15.63 | 574.64 | 0.06 | 2.92 | 1586 |
| 2024-09-20 22:21:32.300 | MS1 | 121.4656646965 | 31.1446243780 | 983 | 504990 | -83.96 | 17.56 | 304.08 | 0.19 | 2.84 | 1597 |
| 2024-09-20 22:21:33.861 | MS1 | 121.4656585663 | 31.1446243424 | 983 | 504990 | -83.37 | 15.40 | 592.28 | 0.19 | 2.56 | 1586 |
| 2024-09-20 22:21:34.682 | MS1 | 121.4656728335 | 31.1446320907 | 983 | 504990 | -91.87 | -3.63 | 69.72 | 0.12 | 1.38 | 1585 |
| 2024-09-20 22:21:35.154 | MS1 | 121.4656777426 | 31.1446184834 | 983 | 504990 | -87.63 | -1.79 | 47.14 | 0.15 | 1.38 | 1581 |
| 2024-09-20 22:21:36.123 | MS1 | 121.4656606241 | 31.1446245951 | 983 | 504990 | -89.86 | -1.98 | 48.03 | 0.04 | 1.20 | 1579 |
| 2024-09-20 22:21:37.622 | MS1 | 121.4656690252 | 31.1446224091 | 983 | 504990 | -89.45 | -0.12 | 40.96 | 0.01 | 1.21 | 1565 |
| 2024-09-20 22:21:38.627 | MS1 | 121.4656624901 | 31.1446282485 | 983 | 504990 | -84.12 | 16.43 | 300.38 | 0.05 | 1.27 | 1570 |
| 2024-09-20 22:21:39.996 | MS1 | 121.4656592424 | 31.1446198909 | 983 | 504990 | -84.49 | 14.40 | 430.39 | 0.17 | 1.11 | 1570 |
| 2024-09-20 22:21:40.182 | MS1 | 121.4656738900 | 31.1446327461 | 983 | 504990 | -83.76 | 17.19 | 569.79 | 0.15 | 2.21 | 1582 |
| 2024-09-20 22:21:41.330 | MS1 | 121.4656778102 | 31.1446221096 | 983 | 504990 | -82.89 | 16.62 | 481.55 | 0.05 | 2.36 | 1587 |
| 2024-09-20 22:21:42.723 | MS1 | 121.4656661598 | 31.1446236669 | 983 | 504990 | -78.55 | 16.75 | 341.66 | 0.08 | 2.93 | 1579 |

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
| 3224334 | 4 | 121.4722921023 | 31.1495721284 | 172 | 4 | 3 | 23.9 | TDD | 983 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3253564 | 3 | 121.4756253649 | 31.1499068315 | 268 | 3 | 6 | 20.1 | TDD | 774 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3256055 | 1 | 121.4652488208 | 31.1501800010 | 269 | 5 | 9 | 20.3 | TDD | 868 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3259578 | 2 | 121.4753963440 | 31.1484661825 | 132 | 15 | 12 | 42.4 | TDD | 573 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:30.769 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.789 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:30.920 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.920 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.656 | NREventA3 | measId:2;ServCellPCI:610;Se... |
| 2024-09-20 22:21:35.656 | NREventA3 | measId:2;ServCellPCI:610;Se... |
| 2024-09-20 22:21:36.656 | NREventA3 | measId:2;ServCellPCI:610;Se... |
| 2024-09-20 22:21:39.156 | NRRRCReestablishAttempt | PCI:610 |
| 2024-09-20 22:21:39.172 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.185 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:39.313 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.313 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3256055 | 1 | 6.3826 | 5.9101 | -116.9763 | 13.4132 | 117.5972 | 0.0171 | 0.0148 |
| 2024_09_20 22:00 | 3259578 | 2 | 17.6351 | 13.9814 | -115.6024 | 15.2755 | 168.8124 | 0.0129 | 0.0048 |
| 2024_09_20 22:00 | 3253564 | 3 | 13.2243 | 16.6807 | -114.5727 | 15.2239 | 189.4726 | 0.0125 | 0.0183 |
| 2024_09_20 22:00 | 3224334 | 4 | 18.4201 | 5.9401 | -115.9330 | 15.3039 | 134.0476 | 0.0036 | 0.1160 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415230_FD28FFAC | 504990 | 774 | -86.0 | 504990 | 983 | -93.8 | 504990 | 573 | -88.7 | 504990 | 868 |
| MR_1774415230_B0C9B3F8 | 504990 | 774 | -87.9 | 504990 | 983 | -92.7 | 504990 | 573 | -89.2 | 504990 | 868 |
| MR_1774415230_8BF2573A | 504990 | 983 | -90.1 | 504990 | 774 | -85.6 | 504990 | 573 | -88.4 | 504990 | 868 |
| MR_1774415230_44ABE129 | 504990 | 983 | -91.1 | 504990 | 774 | -85.4 | 504990 | 573 | -90.8 | 504990 | 868 |
| MR_1774415230_6B6F78FE | 504990 | 983 | -92.8 | 504990 | 774 | -86.7 | 504990 | 573 | -90.8 | 504990 | 868 |
| MR_1774415230_EC155621 | 504990 | 983 | -93.6 | 504990 | 774 | -87.1 | 504990 | 573 | -87.9 | 504990 | 868 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1157: `4d06b726-985...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `4d06b726-9857-4f83-bafe-7fc935243553` |
| Tag | **single-answer** |
| 정답 | **C17** |
| C17 의미 | Decrease A3 Offset threshold for 3235726_3 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1157] topology](images/train_1157.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3235726_3
- `C2`: Increase transmission power for 3256923_4
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3235726_3
- `C4`: Adjust the azimuth of 3235726_3 by 50 degrees
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3256923_4
- `C6`: Decrease transmission power for 3256923_4
- `C7`: Increase A3 Offset threshold for 3256923_4
- `C8`: Lift the tilt angle of 3235726_3 by 10 degrees
- `C9`: Lift the tilt angle  of 3256923_4 by 8 degrees
- `C10`: Check test server and transmission issues
- `C11`: Adjust the azimuth of 3256923_4 by 50 degrees
- `C12`: Press down the tilt angle of 3235726_3 by 10 degrees
- `C13`: Decrease A3 Offset threshold for 3256923_4
- `C14`: Increase transmission power for 3235726_3
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3256923_4
- `C16`: Decrease transmission power for 3235726_3
- `C17`: Decrease A3 Offset threshold for 3235726_3 **← 정답**
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3235726_3
- `C19`: Press down the tilt angle  of 3256923_4 by 8 degrees
- `C20`: Add neighbor relationship between 3255337_1 and 3256923_4
- `C21`: Add neighbor relationship between 3235726_3 and 3256923_4
- `C22`: Insufficient data; more data is needed for judgment.

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.711 | MS1 | 121.4656758150 | 31.1446265377 | 963 | 504990 | -76.54 | 17.78 | 303.19 | 0.16 | 2.04 | 1567 |
| 2024-09-20 22:21:32.677 | MS1 | 121.4656676031 | 31.1446350304 | 963 | 504990 | -77.70 | 13.99 | 431.54 | 0.02 | 2.27 | 1595 |
| 2024-09-20 22:21:33.732 | MS1 | 121.4656637684 | 31.1446343188 | 963 | 504990 | -78.13 | 17.37 | 335.07 | 0.05 | 2.86 | 1566 |
| 2024-09-20 22:21:34.738 | MS1 | 121.4656679837 | 31.1446346809 | 963 | 504990 | -83.64 | -2.23 | 34.77 | 0.09 | 1.45 | 1574 |
| 2024-09-20 22:21:35.670 | MS1 | 121.4656730176 | 31.1446214541 | 963 | 504990 | -92.08 | -1.69 | 42.65 | 0.11 | 1.08 | 1563 |
| 2024-09-20 22:21:36.135 | MS1 | 121.4656646418 | 31.1446288556 | 963 | 504990 | -91.13 | -2.49 | 76.79 | 0.20 | 1.14 | 1589 |
| 2024-09-20 22:21:37.863 | MS1 | 121.4656611762 | 31.1446289426 | 963 | 504990 | -92.41 | -3.64 | 54.77 | 0.10 | 1.05 | 1575 |
| 2024-09-20 22:21:38.522 | MS1 | 121.4656589113 | 31.1446244913 | 963 | 504990 | -92.11 | -2.39 | 54.76 | 0.10 | 1.47 | 1598 |
| 2024-09-20 22:21:39.931 | MS1 | 121.4656661344 | 31.1446309805 | 518 | 504990 | -76.00 | 15.94 | 232.45 | 0.17 | 1.25 | 1588 |
| 2024-09-20 22:21:40.499 | MS1 | 121.4656660504 | 31.1446238200 | 518 | 504990 | -75.32 | 12.60 | 566.12 | 0.14 | 2.35 | 1576 |
| 2024-09-20 22:21:41.558 | MS1 | 121.4656717235 | 31.1446256359 | 518 | 504990 | -75.95 | 17.30 | 497.43 | 0.15 | 2.84 | 1599 |
| 2024-09-20 22:21:42.142 | MS1 | 121.4656735058 | 31.1446367908 | 518 | 504990 | -79.53 | 14.69 | 483.11 | 0.01 | 2.16 | 1595 |

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
| 3218002 | 2 | 121.4722215042 | 31.1509440042 | 29 | 14 | 10 | 19.8 | TDD | 402 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3235726 | 3 | 121.4676053228 | 31.1497460568 | 119 | 15 | 3 | 21.6 | TDD | 963 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3255337 | 1 | 121.4657899335 | 31.1445736538 | 260 | 3 | 7 | 45.6 | TDD | 496 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3256923 | 4 | 121.4717530053 | 31.1505942269 | 353 | 6 | 2 | 38.1 | TDD | 518 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |

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
| 2024-09-20 22:21:31.209 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.230 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.337 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.337 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.092 | NREventA3 | measId:2;ServCellPCI:611;Se... |
| 2024-09-20 22:21:38.332 | NRHandoverAttempt | SourcePCI:611;SourceNR-ARFC... |
| 2024-09-20 22:21:38.370 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.381 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.484 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.484 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3255337 | 1 | 17.9824 | 13.3230 | -115.0043 | 8.7676 | 143.3051 | 0.0057 | 0.0009 |
| 2024_09_20 22:00 | 3218002 | 2 | 11.8550 | 10.4282 | -115.2100 | 14.4464 | 161.5553 | 0.0167 | 0.0120 |
| 2024_09_20 22:00 | 3235726 | 3 | 9.3601 | 16.7391 | -114.9563 | 5.4687 | 199.2336 | 0.0191 | 0.1634 |
| 2024_09_20 22:00 | 3256923 | 4 | 12.3440 | 9.2029 | -117.7314 | 16.4343 | 176.4277 | 0.0067 | 0.0162 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416209_C5A275F5 | 504990 | 963 | -82.8 | 504990 | 518 | -77.7 | 504990 | 496 | -79.6 | 504990 | 402 |
| MR_1774416209_4AE214D7 | 504990 | 518 | -78.3 | 504990 | 963 | -81.8 | 504990 | 496 | -77.7 | 504990 | 402 |
| MR_1774416209_0761E697 | 504990 | 963 | -85.1 | 504990 | 518 | -77.1 | 504990 | 496 | -79.4 | 504990 | 402 |
| MR_1774416209_F81EAE32 | 504990 | 963 | -84.5 | 504990 | 518 | -80.0 | 504990 | 496 | -81.2 | 504990 | 402 |
| MR_1774416209_EA083B9C | 504990 | 963 | -83.3 | 504990 | 518 | -79.8 | 504990 | 496 | -81.6 | 504990 | 402 |
| MR_1774416209_3E32F8DA | 504990 | 518 | -77.7 | 504990 | 963 | -82.0 | 504990 | 496 | -80.6 | 504990 | 402 |
| MR_1774416209_2A9BF53D | 504990 | 518 | -77.6 | 504990 | 963 | -83.1 | 504990 | 496 | -80.8 | 504990 | 402 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1158: `23c8a4ea-6ba...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `23c8a4ea-6ba7-4918-8f66-7b8087acaa09` |
| Tag | **single-answer** |
| 정답 | **C14** |
| C14 의미 | Lift the tilt angle  of 3219886_3 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1158] topology](images/train_1158.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3236099_1
- `C2`: Increase transmission power for 3236099_1
- `C3`: Press down the tilt angle of 3236099_1 by 4 degrees
- `C4`: Check test server and transmission issues
- `C5`: Decrease transmission power for 3236099_1
- `C6`: Adjust the azimuth of 3219886_3 by 50 degrees
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3221686_4
- `C8`: Press down the tilt angle  of 3219886_3 by 10 degrees
- `C9`: Lift the tilt angle of 3236099_1 by 4 degrees
- `C10`: Add neighbor relationship between 3236099_1 and 3221686_4
- `C11`: Increase transmission power for 3221686_4
- `C12`: Adjust the azimuth of 3236099_1 by 31 degrees
- `C13`: Insufficient data; more data is needed for judgment.
- `C14`: Lift the tilt angle  of 3219886_3 by 10 degrees **← 정답**
- `C15`: Decrease A3 Offset threshold for 3236099_1
- `C16`: Increase A3 Offset threshold for 3221686_4
- `C17`: Decrease transmission power for 3221686_4
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3221686_4
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3236099_1
- `C20`: Add neighbor relationship between 3219886_3 and 3221686_4
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3236099_1
- `C22`: Decrease A3 Offset threshold for 3221686_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.962 | MS1 | 121.4656584587 | 31.1446371235 | 268 | 504990 | -89.28 | 17.19 | 330.19 | 0.05 | 2.35 | 1561 |
| 2024-09-20 22:21:32.628 | MS1 | 121.4656687849 | 31.1446188173 | 268 | 504990 | -90.04 | 14.10 | 413.29 | 0.18 | 2.79 | 1560 |
| 2024-09-20 22:21:33.382 | MS1 | 121.4656655194 | 31.1446193598 | 268 | 504990 | -86.91 | 13.26 | 412.51 | 0.20 | 2.79 | 1589 |
| 2024-09-20 22:21:34.721 | MS1 | 121.4656711024 | 31.1446235324 | 268 | 504990 | -90.79 | 16.18 | 78.07 | 0.02 | 2.57 | 1591 |
| 2024-09-20 22:21:35.151 | MS1 | 121.4656619057 | 31.1446365956 | 268 | 504990 | -90.36 | 16.92 | 87.29 | 0.01 | 2.13 | 1586 |
| 2024-09-20 22:21:36.419 | MS1 | 121.4656728933 | 31.1446332051 | 268 | 504990 | -85.62 | 13.62 | 53.24 | 0.04 | 2.37 | 1567 |
| 2024-09-20 22:21:37.406 | MS1 | 121.4656727659 | 31.1446312149 | 268 | 504990 | -91.79 | 8.97 | 82.39 | 0.03 | 2.21 | 1598 |
| 2024-09-20 22:21:38.741 | MS1 | 121.4656629184 | 31.1446372547 | 268 | 504990 | -93.93 | 8.08 | 82.75 | 0.13 | 2.02 | 1563 |
| 2024-09-20 22:21:39.218 | MS1 | 121.4656748854 | 31.1446361703 | 268 | 504990 | -92.24 | 12.95 | 96.63 | 0.16 | 2.87 | 1562 |
| 2024-09-20 22:21:40.888 | MS1 | 121.4656608495 | 31.1446280719 | 268 | 504990 | -90.79 | 10.27 | 392.06 | 0.13 | 2.96 | 1578 |
| 2024-09-20 22:21:41.812 | MS1 | 121.4656640273 | 31.1446297381 | 268 | 504990 | -93.51 | 7.69 | 599.25 | 0.06 | 3.00 | 1570 |
| 2024-09-20 22:21:42.582 | MS1 | 121.4656701562 | 31.1446191397 | 268 | 504990 | -92.96 | 9.74 | 376.92 | 0.11 | 2.87 | 1574 |

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
| 3211211 | 2 | 121.4669965785 | 31.1486075940 | 350 | 12 | 7 | 45.3 | TDD | 525 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3219886 | 3 | 121.4652374775 | 31.1535653204 | 58 | 1 | 8 | 41.1 | TDD | 934 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3221686 | 4 | 121.4718547854 | 31.1479510489 | 61 | 12 | 9 | 18.5 | TDD | 55 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3236099 | 1 | 121.4673246100 | 31.1507739185 | 224 | 1 | 0 | 33.7 | TDD | 268 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |

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
| 2024-09-20 22:21:31.101 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.121 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.267 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.267 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.963 | NREventA3 | measId:2;ServCellPCI:3;Serv... |
| 2024-09-20 22:21:38.203 | NRHandoverAttempt | SourcePCI:3;SourceNR-ARFCN:... |
| 2024-09-20 22:21:38.235 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.248 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.349 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.349 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3236099 | 1 | 80.0941 | 84.6829 | -117.4510 | 10.7958 | 129.1094 | 0.0006 | 0.0080 |
| 2024_09_20 22:00 | 3211211 | 2 | 18.0051 | 6.0913 | -114.2540 | 16.3629 | 193.7873 | 0.0104 | 0.0139 |
| 2024_09_20 22:00 | 3219886 | 3 | 16.4914 | 10.6135 | -114.7892 | 14.8803 | 105.2815 | 0.0061 | 0.0131 |
| 2024_09_20 22:00 | 3221686 | 4 | 14.2273 | 5.8239 | -117.2448 | 9.8531 | 198.0043 | 0.0150 | 0.0109 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413547_D59F4AB7 | 504990 | 268 | -90.3 | 504990 | 55 | -98.0 | 504990 | 934 | -106.3 | 504990 | 525 |
| MR_1774413547_536DBF48 | 504990 | 268 | -92.2 | 504990 | 55 | -96.3 | 504990 | 934 | -103.8 | 504990 | 525 |
| MR_1774413547_879EFB0F | 504990 | 268 | -89.7 | 504990 | 55 | -96.6 | 504990 | 934 | -104.8 | 504990 | 525 |
| MR_1774413547_C4B56813 | 504990 | 268 | -92.8 | 504990 | 55 | -96.2 | 504990 | 934 | -103.4 | 504990 | 525 |
| MR_1774413547_C88D66F3 | 504990 | 268 | -90.5 | 504990 | 55 | -95.9 | 504990 | 934 | -103.7 | 504990 | 525 |
| MR_1774413547_485D986E | 504990 | 268 | -92.7 | 504990 | 55 | -95.9 | 504990 | 934 | -105.5 | 504990 | 525 |
| MR_1774413547_F9E3C897 | 504990 | 268 | -91.7 | 504990 | 55 | -95.3 | 504990 | 934 | -104.7 | 504990 | 525 |
| MR_1774413547_461E0572 | 504990 | 268 | -92.5 | 504990 | 55 | -95.3 | 504990 | 934 | -106.7 | 504990 | 525 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1159: `9627c5d2-dc4...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `9627c5d2-dc47-4206-ba8e-4029673bb0ff` |
| Tag | **single-answer** |
| 정답 | **C19** |
| C19 의미 | Lift the tilt angle  of 3258382_4 by 8 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1159] topology](images/train_1159.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3235603_2
- `C2`: Press down the tilt angle of 3239118_1 by 5 degrees
- `C3`: Add neighbor relationship between 3239118_1 and 3235603_2
- `C4`: Insufficient data; more data is needed for judgment.
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3235603_2
- `C6`: Check test server and transmission issues
- `C7`: Adjust the azimuth of 3258382_4 by 50 degrees
- `C8`: Add neighbor relationship between 3258382_4 and 3235603_2
- `C9`: Increase transmission power for 3239118_1
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3239118_1
- `C11`: Lift the tilt angle of 3239118_1 by 5 degrees
- `C12`: Decrease A3 Offset threshold for 3239118_1
- `C13`: Adjust the azimuth of 3239118_1 by 31 degrees
- `C14`: Decrease A3 Offset threshold for 3235603_2
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3239118_1
- `C16`: Increase transmission power for 3235603_2
- `C17`: Increase A3 Offset threshold for 3235603_2
- `C18`: Press down the tilt angle  of 3258382_4 by 8 degrees
- `C19`: Lift the tilt angle  of 3258382_4 by 8 degrees **← 정답**
- `C20`: Decrease transmission power for 3239118_1
- `C21`: Increase A3 Offset threshold for 3239118_1
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3235603_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.788 | MS1 | 121.4656770722 | 31.1446355132 | 514 | 504990 | -90.32 | 16.98 | 509.84 | 0.06 | 2.50 | 1565 |
| 2024-09-20 22:21:32.669 | MS1 | 121.4656623885 | 31.1446324092 | 514 | 504990 | -88.22 | 13.34 | 483.96 | 0.09 | 2.82 | 1582 |
| 2024-09-20 22:21:33.138 | MS1 | 121.4656721422 | 31.1446211529 | 514 | 504990 | -90.02 | 13.97 | 532.16 | 0.19 | 2.19 | 1564 |
| 2024-09-20 22:21:34.448 | MS1 | 121.4656714455 | 31.1446377812 | 514 | 504990 | -91.72 | 17.79 | 95.67 | 0.05 | 2.26 | 1577 |
| 2024-09-20 22:21:35.591 | MS1 | 121.4656741148 | 31.1446328133 | 514 | 504990 | -89.95 | 15.09 | 72.83 | 0.07 | 2.61 | 1573 |
| 2024-09-20 22:21:36.333 | MS1 | 121.4656677622 | 31.1446337061 | 514 | 504990 | -87.37 | 15.86 | 61.16 | 0.03 | 2.20 | 1568 |
| 2024-09-20 22:21:37.737 | MS1 | 121.4656642411 | 31.1446192128 | 514 | 504990 | -93.76 | 11.48 | 77.44 | 0.04 | 2.27 | 1574 |
| 2024-09-20 22:21:38.169 | MS1 | 121.4656711150 | 31.1446289731 | 514 | 504990 | -91.82 | 7.48 | 47.48 | 0.13 | 2.48 | 1592 |
| 2024-09-20 22:21:39.192 | MS1 | 121.4656645558 | 31.1446374346 | 514 | 504990 | -92.87 | 12.46 | 90.75 | 0.05 | 2.10 | 1598 |
| 2024-09-20 22:21:40.701 | MS1 | 121.4656582196 | 31.1446297843 | 514 | 504990 | -91.00 | 11.72 | 514.01 | 0.17 | 2.62 | 1566 |
| 2024-09-20 22:21:41.197 | MS1 | 121.4656596886 | 31.1446184336 | 514 | 504990 | -93.63 | 7.04 | 602.23 | 0.07 | 2.89 | 1569 |
| 2024-09-20 22:21:42.253 | MS1 | 121.4656607755 | 31.1446255020 | 514 | 504990 | -89.72 | 11.66 | 362.40 | 0.07 | 2.82 | 1565 |

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
| 3235603 | 2 | 121.4734744809 | 31.1452371606 | 54 | 5 | 3 | 36.1 | TDD | 684 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3239118 | 1 | 121.4652642850 | 31.1537197410 | 209 | 2 | 2 | 47.0 | TDD | 514 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3255096 | 3 | 121.4696623334 | 31.1528659120 | 264 | 8 | 1 | 39.8 | TDD | 290 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3258382 | 4 | 121.4660655151 | 31.1522132120 | 32 | 10 | 3 | 35.4 | TDD | 607 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |

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
| 2024-09-20 22:21:31.567 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.584 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.715 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.715 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.413 | NREventA3 | measId:2;ServCellPCI:895;Se... |
| 2024-09-20 22:21:38.653 | NRHandoverAttempt | SourcePCI:895;SourceNR-ARFC... |
| 2024-09-20 22:21:38.688 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.699 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.839 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.839 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3239118 | 1 | 84.2921 | 94.0783 | -115.3523 | 9.2644 | 182.3241 | 0.0181 | 0.0062 |
| 2024_09_20 22:00 | 3235603 | 2 | 16.9968 | 18.1765 | -116.2336 | 18.7033 | 108.1555 | 0.0091 | 0.0107 |
| 2024_09_20 22:00 | 3255096 | 3 | 14.0980 | 13.5415 | -115.9411 | 19.0236 | 183.7791 | 0.0027 | 0.0052 |
| 2024_09_20 22:00 | 3258382 | 4 | 12.2155 | 6.2593 | -116.8985 | 8.4356 | 155.2352 | 0.0011 | 0.0107 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413151_6F8295F9 | 504990 | 514 | -90.0 | 504990 | 684 | -99.5 | 504990 | 607 | -97.8 | 504990 | 290 |
| MR_1774413151_D4F14F4D | 504990 | 514 | -92.9 | 504990 | 684 | -96.4 | 504990 | 607 | -97.4 | 504990 | 290 |
| MR_1774413151_7610994E | 504990 | 514 | -91.7 | 504990 | 684 | -96.6 | 504990 | 607 | -99.3 | 504990 | 290 |
| MR_1774413151_CD4392BC | 504990 | 514 | -93.4 | 504990 | 684 | -96.8 | 504990 | 607 | -101.1 | 504990 | 290 |
| MR_1774413151_BF4541A8 | 504990 | 514 | -90.3 | 504990 | 684 | -98.1 | 504990 | 607 | -98.6 | 504990 | 290 |
| MR_1774413151_C7851B44 | 504990 | 514 | -91.5 | 504990 | 684 | -98.7 | 504990 | 607 | -100.2 | 504990 | 290 |

> *... 2개 열 생략 (전체 14열)*

---
