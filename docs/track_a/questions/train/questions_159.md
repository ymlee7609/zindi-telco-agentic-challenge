# Track A 문제 분석 — train[1580]~train[1589]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[1580] ~ train[1589] (10개)

## 목차

1. [문제 1580: `dfdaa760-77c...`](#1580) — single-answer, 정답: C10
2. [문제 1581: `9dffc96e-4e6...`](#1581) — single-answer, 정답: C18
3. [문제 1582: `35c2731b-6d2...`](#1582) — single-answer, 정답: C17
4. [문제 1583: `1d893e85-d7c...`](#1583) — single-answer, 정답: C5
5. [문제 1584: `a2ab62a8-b7e...`](#1584) — multiple-answer, 정답: C1|C13|C14|C21
6. [문제 1585: `c79c9e9c-1e8...`](#1585) — single-answer, 정답: C1
7. [문제 1586: `15ac0c8a-9e0...`](#1586) — single-answer, 정답: C14
8. [문제 1587: `013d249c-921...`](#1587) — multiple-answer, 정답: C11|C14
9. [문제 1588: `1872a53a-39e...`](#1588) — single-answer, 정답: C11
10. [문제 1589: `84aa1488-f26...`](#1589) — multiple-answer, 정답: C14|C17

---

### 문제 1580: `dfdaa760-77c...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `dfdaa760-77cf-4a52-849b-0bff1c66e688` |
| Tag | **single-answer** |
| 정답 | **C10** |
| C10 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1580] topology](images/train_1580.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3241751_2 and 3218120_3
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3278471_4
- `C3`: Decrease A3 Offset threshold for 3218120_3
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3278471_4
- `C5`: Increase A3 Offset threshold for 3278471_4
- `C6`: Adjust the azimuth of 3278471_4 by 50 degrees
- `C7`: Increase transmission power for 3278471_4
- `C8`: Increase transmission power for 3218120_3
- `C9`: Decrease transmission power for 3278471_4
- `C10`: Insufficient data; more data is needed for judgment. **← 정답**
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3218120_3
- `C12`: Adjust the azimuth of 3218120_3 by 13 degrees
- `C13`: Lift the tilt angle  of 3218120_3 by 3 degrees
- `C14`: Lift the tilt angle of 3278471_4 by 10 degrees
- `C15`: Check test server and transmission issues
- `C16`: Decrease A3 Offset threshold for 3278471_4
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3218120_3
- `C18`: Decrease transmission power for 3218120_3
- `C19`: Add neighbor relationship between 3278471_4 and 3218120_3
- `C20`: Increase A3 Offset threshold for 3218120_3
- `C21`: Press down the tilt angle  of 3218120_3 by 3 degrees
- `C22`: Press down the tilt angle of 3278471_4 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.775 | MS1 | 121.4656640001 | 31.1446263892 | 151 | 504990 | -91.27 | 15.77 | 413.42 | 0.08 | 2.02 | 1571 |
| 2024-09-20 22:21:32.912 | MS1 | 121.4656737380 | 31.1446349019 | 151 | 504990 | -86.88 | 15.39 | 344.19 | 0.02 | 2.89 | 1570 |
| 2024-09-20 22:21:33.151 | MS1 | 121.4656703646 | 31.1446346635 | 151 | 504990 | -89.31 | 13.07 | 568.93 | 0.12 | 2.37 | 1587 |
| 2024-09-20 22:21:34.857 | MS1 | 121.4656741730 | 31.1446354170 | 151 | 504990 | -90.89 | 14.44 | 57.49 | 0.16 | 2.56 | 1574 |
| 2024-09-20 22:21:35.441 | MS1 | 121.4656657981 | 31.1446275959 | 151 | 504990 | -89.39 | 14.80 | 86.02 | 0.06 | 2.78 | 1578 |
| 2024-09-20 22:21:36.924 | MS1 | 121.4656725939 | 31.1446223901 | 151 | 504990 | -91.39 | 16.93 | 84.27 | 0.10 | 2.43 | 1583 |
| 2024-09-20 22:21:37.374 | MS1 | 121.4656670037 | 31.1446316561 | 151 | 504990 | -90.26 | 9.72 | 86.68 | 0.18 | 2.02 | 1587 |
| 2024-09-20 22:21:38.529 | MS1 | 121.4656679931 | 31.1446213707 | 151 | 504990 | -93.22 | 12.29 | 82.02 | 0.06 | 2.14 | 1560 |
| 2024-09-20 22:21:39.392 | MS1 | 121.4656632998 | 31.1446346486 | 151 | 504990 | -93.75 | 8.34 | 55.24 | 0.03 | 2.72 | 1574 |
| 2024-09-20 22:21:40.261 | MS1 | 121.4656741932 | 31.1446268625 | 151 | 504990 | -92.74 | 8.62 | 294.27 | 0.19 | 2.58 | 1581 |
| 2024-09-20 22:21:41.935 | MS1 | 121.4656610507 | 31.1446302986 | 151 | 504990 | -92.27 | 7.14 | 447.98 | 0.10 | 2.76 | 1595 |
| 2024-09-20 22:21:42.534 | MS1 | 121.4656677275 | 31.1446186826 | 151 | 504990 | -89.78 | 12.32 | 552.03 | 0.09 | 2.88 | 1561 |

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
| 3218120 | 3 | 121.4722063874 | 31.1459203362 | 270 | 1 | 6 | 26.7 | TDD | 246 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3224453 | 1 | 121.4699376701 | 31.1479990716 | 347 | 5 | 2 | 49.4 | TDD | 561 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3241751 | 2 | 121.4689084462 | 31.1462679548 | 69 | 3 | 5 | 29.6 | TDD | 458 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3278471 | 4 | 121.4652403634 | 31.1469989736 | 281 | 3 | 12 | 31.2 | TDD | 151 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |

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
| 2024-09-20 22:21:30.734 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.757 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:30.857 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.857 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.625 | NREventA3 | measId:2;ServCellPCI:908;Se... |
| 2024-09-20 22:21:37.865 | NRHandoverAttempt | SourcePCI:908;SourceNR-ARFC... |
| 2024-09-20 22:21:37.905 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.918 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.057 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.057 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3224453 | 1 | 85.7685 | 84.2543 | -115.8456 | 12.5878 | 95.0590 | 0.0125 | 0.0140 |
| 2024_09_19 22:00 | 3241751 | 2 | 92.7521 | 93.1649 | -117.4850 | 14.5425 | 145.6029 | 0.0002 | 0.0109 |
| 2024_09_19 22:00 | 3218120 | 3 | 75.9037 | 76.3575 | -116.8586 | 19.3398 | 199.1401 | 0.0145 | 0.0192 |
| 2024_09_19 22:00 | 3278471 | 4 | 78.8083 | 76.3165 | -114.6463 | 6.7498 | 118.9575 | 0.0157 | 0.0098 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415733_5BDB60E9 | 504990 | 151 | -92.2 | 504990 | 246 | -92.1 | 504990 | 458 | -104.8 | 504990 | 561 |
| MR_1774415733_7C093025 | 504990 | 151 | -90.2 | 504990 | 246 | -92.6 | 504990 | 458 | -104.6 | 504990 | 561 |
| MR_1774415733_6F372855 | 504990 | 151 | -91.4 | 504990 | 246 | -92.4 | 504990 | 458 | -103.5 | 504990 | 561 |
| MR_1774415733_CCF82FEE | 504990 | 151 | -89.8 | 504990 | 246 | -90.7 | 504990 | 458 | -103.3 | 504990 | 561 |
| MR_1774415733_FC2E9E0E | 504990 | 151 | -92.6 | 504990 | 246 | -91.6 | 504990 | 458 | -103.6 | 504990 | 561 |
| MR_1774415733_2E67BA8C | 504990 | 151 | -91.6 | 504990 | 246 | -92.3 | 504990 | 458 | -101.9 | 504990 | 561 |
| MR_1774415733_79DC356C | 504990 | 151 | -91.0 | 504990 | 246 | -93.0 | 504990 | 458 | -101.7 | 504990 | 561 |
| MR_1774415733_A6D1EBBB | 504990 | 151 | -91.9 | 504990 | 246 | -92.2 | 504990 | 458 | -101.4 | 504990 | 561 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1581: `9dffc96e-4e6...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `9dffc96e-4e6c-4ef9-81b9-7a2a1c0d0845` |
| Tag | **single-answer** |
| 정답 | **C18** |
| C18 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3259107_3 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1581] topology](images/train_1581.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3266040_4
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3266040_4
- `C3`: Insufficient data; more data is needed for judgment.
- `C4`: Increase A3 Offset threshold for 3266040_4
- `C5`: Decrease transmission power for 3266040_4
- `C6`: Press down the tilt angle  of 3266040_4 by 9 degrees
- `C7`: Increase transmission power for 3259107_3
- `C8`: Decrease transmission power for 3259107_3
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3259107_3
- `C10`: Press down the tilt angle of 3259107_3 by 6 degrees
- `C11`: Check test server and transmission issues
- `C12`: Adjust the azimuth of 3266040_4 by 50 degrees
- `C13`: Adjust the azimuth of 3259107_3 by 4 degrees
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3266040_4
- `C15`: Decrease A3 Offset threshold for 3259107_3
- `C16`: Decrease A3 Offset threshold for 3266040_4
- `C17`: Lift the tilt angle  of 3266040_4 by 9 degrees
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3259107_3 **← 정답**
- `C19`: Add neighbor relationship between 3222021_1 and 3266040_4
- `C20`: Increase A3 Offset threshold for 3259107_3
- `C21`: Add neighbor relationship between 3259107_3 and 3266040_4
- `C22`: Lift the tilt angle of 3259107_3 by 6 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.591 | MS1 | 121.4656662041 | 31.1446205234 | 958 | 504990 | -89.06 | 17.93 | 600.41 | 0.03 | 2.97 | 1566 |
| 2024-09-20 22:21:32.393 | MS1 | 121.4656644254 | 31.1446302307 | 958 | 504990 | -86.98 | 14.54 | 493.55 | 0.11 | 2.55 | 1591 |
| 2024-09-20 22:21:33.540 | MS1 | 121.4656703810 | 31.1446316679 | 958 | 504990 | -85.51 | 13.96 | 568.22 | 0.07 | 2.75 | 1571 |
| 2024-09-20 22:21:34.255 | MS1 | 121.4656728446 | 31.1446344835 | 958 | 504990 | -91.98 | 13.36 | 96.69 | 0.60 | 2.17 | 584 |
| 2024-09-20 22:21:35.620 | MS1 | 121.4656598014 | 31.1446254194 | 958 | 504990 | -88.43 | 17.80 | 95.04 | 0.67 | 2.91 | 626 |
| 2024-09-20 22:21:36.574 | MS1 | 121.4656636077 | 31.1446244914 | 958 | 504990 | -86.93 | 16.75 | 86.54 | 0.65 | 2.10 | 668 |
| 2024-09-20 22:21:37.282 | MS1 | 121.4656650130 | 31.1446283415 | 958 | 504990 | -89.48 | 12.47 | 76.29 | 0.51 | 2.93 | 508 |
| 2024-09-20 22:21:38.998 | MS1 | 121.4656613869 | 31.1446199593 | 958 | 504990 | -92.61 | 8.65 | 58.09 | 0.53 | 2.27 | 601 |
| 2024-09-20 22:21:39.188 | MS1 | 121.4656628145 | 31.1446195910 | 958 | 504990 | -93.82 | 12.57 | 72.62 | 0.66 | 2.61 | 683 |
| 2024-09-20 22:21:40.178 | MS1 | 121.4656672606 | 31.1446283217 | 958 | 504990 | -90.42 | 10.36 | 505.28 | 0.14 | 2.90 | 1584 |
| 2024-09-20 22:21:41.921 | MS1 | 121.4656750365 | 31.1446218868 | 958 | 504990 | -92.22 | 8.61 | 585.12 | 0.03 | 2.64 | 1580 |
| 2024-09-20 22:21:42.206 | MS1 | 121.4656744519 | 31.1446284114 | 958 | 504990 | -93.32 | 12.48 | 582.25 | 0.17 | 2.48 | 1561 |

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
| 3222021 | 1 | 121.4747248275 | 31.1524501956 | 90 | 6 | 4 | 28.1 | TDD | 674 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3224509 | 2 | 121.4655063632 | 31.1544642280 | 22 | 14 | 4 | 32.2 | TDD | 818 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3259107 | 3 | 121.4755065164 | 31.1520614610 | 233 | 4 | 8 | 39.6 | TDD | 958 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3266040 | 4 | 121.4720814700 | 31.1482857287 | 68 | 7 | 11 | 27.1 | TDD | 759 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |

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
| 2024-09-20 22:21:31.095 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.112 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.261 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.261 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.935 | NREventA3 | measId:2;ServCellPCI:760;Se... |
| 2024-09-20 22:21:38.175 | NRHandoverAttempt | SourcePCI:760;SourceNR-ARFC... |
| 2024-09-20 22:21:38.217 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.229 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.335 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.335 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3222021 | 1 | 6.7701 | 6.3964 | -115.0604 | 16.8875 | 177.0999 | 0.0122 | 0.0161 |
| 2024_09_20 22:00 | 3224509 | 2 | 15.6897 | 6.4361 | -115.1976 | 10.2330 | 115.9372 | 0.0147 | 0.0135 |
| 2024_09_20 22:00 | 3259107 | 3 | 9.1496 | 12.2097 | -114.6426 | 12.0873 | 162.2535 | 0.0193 | 0.0018 |
| 2024_09_20 22:00 | 3266040 | 4 | 9.4475 | 5.9172 | -117.2077 | 15.6743 | 82.6313 | 0.0065 | 0.0167 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416769_2051270C | 504990 | 958 | -90.7 | 504990 | 759 | -99.9 | 504990 | 674 | -106.9 | 504990 | 818 |
| MR_1774416769_53998DF8 | 504990 | 958 | -92.6 | 504990 | 759 | -97.1 | 504990 | 674 | -106.3 | 504990 | 818 |
| MR_1774416769_55038840 | 504990 | 958 | -92.3 | 504990 | 759 | -98.5 | 504990 | 674 | -105.8 | 504990 | 818 |
| MR_1774416769_B0903F22 | 504990 | 958 | -93.3 | 504990 | 759 | -97.7 | 504990 | 674 | -107.7 | 504990 | 818 |
| MR_1774416769_4FB44577 | 504990 | 958 | -91.2 | 504990 | 759 | -99.0 | 504990 | 674 | -107.8 | 504990 | 818 |
| MR_1774416769_EFAC073D | 504990 | 958 | -93.9 | 504990 | 759 | -97.3 | 504990 | 674 | -108.5 | 504990 | 818 |
| MR_1774416769_F44F1AF3 | 504990 | 958 | -92.7 | 504990 | 759 | -98.6 | 504990 | 674 | -106.6 | 504990 | 818 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1582: `35c2731b-6d2...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `35c2731b-6d2b-4fa7-b506-57a39d41bb93` |
| Tag | **single-answer** |
| 정답 | **C17** |
| C17 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1582] topology](images/train_1582.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3252413_4
- `C2`: Press down the tilt angle of 3210187_2 by 10 degrees
- `C3`: Lift the tilt angle  of 3252413_4 by 10 degrees
- `C4`: Increase transmission power for 3252413_4
- `C5`: Add neighbor relationship between 3210187_2 and 3252413_4
- `C6`: Add neighbor relationship between 3245815_1 and 3252413_4
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3210187_2
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3210187_2
- `C9`: Adjust the azimuth of 3210187_2 by 44 degrees
- `C10`: Adjust the azimuth of 3252413_4 by 50 degrees
- `C11`: Decrease transmission power for 3252413_4
- `C12`: Increase transmission power for 3210187_2
- `C13`: Press down the tilt angle  of 3252413_4 by 10 degrees
- `C14`: Check test server and transmission issues
- `C15`: Decrease transmission power for 3210187_2
- `C16`: Increase A3 Offset threshold for 3210187_2
- `C17`: Insufficient data; more data is needed for judgment. **← 정답**
- `C18`: Decrease A3 Offset threshold for 3252413_4
- `C19`: Lift the tilt angle of 3210187_2 by 10 degrees
- `C20`: Decrease A3 Offset threshold for 3210187_2
- `C21`: Increase A3 Offset threshold for 3252413_4
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3252413_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.332 | MS1 | 121.4656729188 | 31.1446284469 | 117 | 504990 | -85.77 | 13.30 | 451.62 | 0.01 | 2.46 | 1563 |
| 2024-09-20 22:21:32.175 | MS1 | 121.4656761967 | 31.1446194459 | 117 | 504990 | -86.35 | 12.81 | 352.41 | 0.10 | 2.36 | 1570 |
| 2024-09-20 22:21:33.937 | MS1 | 121.4656765888 | 31.1446273533 | 117 | 504990 | -85.86 | 15.73 | 305.85 | 0.07 | 2.08 | 1567 |
| 2024-09-20 22:21:34.867 | MS1 | 121.4656595170 | 31.1446190711 | 117 | 504990 | -87.84 | 13.73 | 62.63 | 0.15 | 2.47 | 1582 |
| 2024-09-20 22:21:35.492 | MS1 | 121.4656755173 | 31.1446331019 | 117 | 504990 | -85.90 | 12.84 | 73.37 | 0.12 | 2.60 | 1598 |
| 2024-09-20 22:21:36.460 | MS1 | 121.4656604761 | 31.1446347056 | 117 | 504990 | -86.89 | 13.10 | 90.95 | 0.16 | 2.86 | 1586 |
| 2024-09-20 22:21:37.529 | MS1 | 121.4656636977 | 31.1446226602 | 117 | 504990 | -89.93 | 11.94 | 70.00 | 0.03 | 2.34 | 1580 |
| 2024-09-20 22:21:38.887 | MS1 | 121.4656741606 | 31.1446235292 | 117 | 504990 | -89.44 | 7.76 | 55.27 | 0.08 | 2.60 | 1580 |
| 2024-09-20 22:21:39.442 | MS1 | 121.4656747065 | 31.1446349296 | 117 | 504990 | -91.50 | 10.53 | 56.39 | 0.20 | 2.16 | 1570 |
| 2024-09-20 22:21:40.960 | MS1 | 121.4656670216 | 31.1446270473 | 117 | 504990 | -90.58 | 8.56 | 530.64 | 0.06 | 2.31 | 1575 |
| 2024-09-20 22:21:41.706 | MS1 | 121.4656630086 | 31.1446366348 | 117 | 504990 | -89.06 | 8.26 | 557.80 | 0.09 | 2.22 | 1597 |
| 2024-09-20 22:21:42.228 | MS1 | 121.4656603880 | 31.1446192984 | 117 | 504990 | -91.40 | 8.74 | 482.84 | 0.17 | 2.16 | 1579 |

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
| 3210187 | 2 | 121.4657802603 | 31.1497662427 | 137 | 8 | 12 | 29.4 | TDD | 117 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3245815 | 1 | 121.4657621174 | 31.1449237916 | 143 | 6 | 4 | 47.8 | TDD | 569 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3252413 | 4 | 121.4671512004 | 31.1482897122 | 133 | 14 | 5 | 32.0 | TDD | 758 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3278061 | 3 | 121.4758767799 | 31.1482438883 | 188 | 10 | 2 | 17.0 | TDD | 565 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |

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
| 2024-09-20 22:21:30.943 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.961 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.081 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.081 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.795 | NREventA3 | measId:2;ServCellPCI:107;Se... |
| 2024-09-20 22:21:38.035 | NRHandoverAttempt | SourcePCI:107;SourceNR-ARFC... |
| 2024-09-20 22:21:38.065 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.080 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.190 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.190 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3245815 | 1 | 83.4642 | 76.8708 | -114.1958 | 11.3408 | 143.4547 | 0.0145 | 0.0029 |
| 2024_09_19 22:00 | 3210187 | 2 | 88.3179 | 78.5447 | -115.7820 | 19.5499 | 85.0743 | 0.0187 | 0.0040 |
| 2024_09_19 22:00 | 3278061 | 3 | 86.3991 | 78.5108 | -117.3720 | 11.8354 | 119.3118 | 0.0110 | 0.0187 |
| 2024_09_19 22:00 | 3252413 | 4 | 80.7261 | 83.0614 | -114.6863 | 16.4176 | 186.0677 | 0.0015 | 0.0193 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415469_775B8367 | 504990 | 117 | -89.7 | 504990 | 758 | -96.5 | 504990 | 569 | -102.4 | 504990 | 565 |
| MR_1774415469_C07E47A8 | 504990 | 117 | -87.2 | 504990 | 758 | -95.2 | 504990 | 569 | -98.7 | 504990 | 565 |
| MR_1774415469_034D0088 | 504990 | 117 | -87.6 | 504990 | 758 | -98.4 | 504990 | 569 | -100.0 | 504990 | 565 |
| MR_1774415469_63DE5C48 | 504990 | 117 | -88.3 | 504990 | 758 | -98.7 | 504990 | 569 | -99.1 | 504990 | 565 |
| MR_1774415469_B14FA6B8 | 504990 | 117 | -89.2 | 504990 | 758 | -95.6 | 504990 | 569 | -101.4 | 504990 | 565 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1583: `1d893e85-d7c...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `1d893e85-d7c8-4c99-8dbb-2ebcbc91b3aa` |
| Tag | **single-answer** |
| 정답 | **C5** |
| C5 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3241516_1 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1583] topology](images/train_1583.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Check test server and transmission issues
- `C2`: Decrease A3 Offset threshold for 3249463_3
- `C3`: Increase A3 Offset threshold for 3249463_3
- `C4`: Press down the tilt angle of 3241516_1 by 5 degrees
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3241516_1 **← 정답**
- `C6`: Decrease transmission power for 3241516_1
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3249463_3
- `C8`: Lift the tilt angle of 3241516_1 by 5 degrees
- `C9`: Increase transmission power for 3241516_1
- `C10`: Press down the tilt angle  of 3249463_3 by 10 degrees
- `C11`: Increase transmission power for 3249463_3
- `C12`: Decrease A3 Offset threshold for 3241516_1
- `C13`: Adjust the azimuth of 3249463_3 by 50 degrees
- `C14`: Add neighbor relationship between 3241516_1 and 3249463_3
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3241516_1
- `C16`: Increase A3 Offset threshold for 3241516_1
- `C17`: Adjust the azimuth of 3241516_1 by 24 degrees
- `C18`: Lift the tilt angle  of 3249463_3 by 10 degrees
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3249463_3
- `C20`: Decrease transmission power for 3249463_3
- `C21`: Insufficient data; more data is needed for judgment.
- `C22`: Add neighbor relationship between 3262804_2 and 3249463_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.597 | MS1 | 121.4656779439 | 31.1446378790 | 18 | 504990 | -88.12 | 17.21 | 571.72 | 0.19 | 2.52 | 1596 |
| 2024-09-20 22:21:32.920 | MS1 | 121.4656693128 | 31.1446346580 | 18 | 504990 | -86.54 | 14.58 | 371.43 | 0.02 | 2.88 | 1575 |
| 2024-09-20 22:21:33.842 | MS1 | 121.4656770733 | 31.1446299148 | 18 | 504990 | -90.08 | 12.30 | 514.59 | 0.09 | 2.67 | 1563 |
| 2024-09-20 22:21:34.980 | MS1 | 121.4656653864 | 31.1446325334 | 18 | 504990 | -85.88 | 13.54 | 100.52 | 0.52 | 2.63 | 507 |
| 2024-09-20 22:21:35.195 | MS1 | 121.4656775472 | 31.1446357911 | 18 | 504990 | -88.16 | 13.88 | 50.86 | 0.65 | 2.44 | 618 |
| 2024-09-20 22:21:36.272 | MS1 | 121.4656619848 | 31.1446306907 | 18 | 504990 | -89.92 | 15.44 | 72.03 | 0.68 | 2.83 | 533 |
| 2024-09-20 22:21:37.973 | MS1 | 121.4656646962 | 31.1446341218 | 18 | 504990 | -91.57 | 12.68 | 77.49 | 0.63 | 2.24 | 604 |
| 2024-09-20 22:21:38.805 | MS1 | 121.4656696867 | 31.1446238553 | 18 | 504990 | -90.23 | 7.70 | 54.59 | 0.63 | 2.48 | 517 |
| 2024-09-20 22:21:39.946 | MS1 | 121.4656634760 | 31.1446366658 | 18 | 504990 | -90.72 | 9.59 | 78.34 | 0.61 | 2.47 | 680 |
| 2024-09-20 22:21:40.556 | MS1 | 121.4656690454 | 31.1446343369 | 18 | 504990 | -90.52 | 12.38 | 383.91 | 0.05 | 2.27 | 1600 |
| 2024-09-20 22:21:41.821 | MS1 | 121.4656638870 | 31.1446340782 | 18 | 504990 | -93.74 | 12.89 | 399.71 | 0.14 | 2.13 | 1589 |
| 2024-09-20 22:21:42.655 | MS1 | 121.4656671087 | 31.1446342874 | 18 | 504990 | -89.37 | 12.71 | 331.11 | 0.11 | 2.37 | 1568 |

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
| 3241516 | 1 | 121.4697056295 | 31.1521978027 | 229 | 2 | 0 | 45.2 | TDD | 18 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3249463 | 3 | 121.4658096931 | 31.1470685876 | 56 | 2 | 6 | 40.2 | TDD | 406 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3261797 | 4 | 121.4696738898 | 31.1533534241 | 271 | 8 | 12 | 32.5 | TDD | 823 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3262804 | 2 | 121.4725452886 | 31.1494282141 | 329 | 10 | 3 | 39.6 | TDD | 996 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |

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
| 2024-09-20 22:21:31.217 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.238 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.375 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.375 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.061 | NREventA3 | measId:2;ServCellPCI:909;Se... |
| 2024-09-20 22:21:38.301 | NRHandoverAttempt | SourcePCI:909;SourceNR-ARFC... |
| 2024-09-20 22:21:38.337 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.349 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.475 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.475 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3241516 | 1 | 8.4853 | 16.9226 | -117.1812 | 19.8131 | 182.9665 | 0.0118 | 0.0121 |
| 2024_09_20 22:00 | 3262804 | 2 | 8.3469 | 18.0115 | -116.8300 | 8.2362 | 90.5642 | 0.0011 | 0.0078 |
| 2024_09_20 22:00 | 3249463 | 3 | 9.3270 | 6.3184 | -114.9469 | 5.2920 | 88.3676 | 0.0088 | 0.0062 |
| 2024_09_20 22:00 | 3261797 | 4 | 7.7522 | 9.6832 | -114.5846 | 6.2240 | 118.5568 | 0.0193 | 0.0069 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417172_9360711A | 504990 | 18 | -86.7 | 504990 | 406 | -92.8 | 504990 | 996 | -99.2 | 504990 | 823 |
| MR_1774417172_75A3BC45 | 504990 | 18 | -89.3 | 504990 | 406 | -95.3 | 504990 | 996 | -96.0 | 504990 | 823 |
| MR_1774417172_4430A845 | 504990 | 18 | -89.1 | 504990 | 406 | -95.0 | 504990 | 996 | -96.7 | 504990 | 823 |
| MR_1774417172_5D597FF8 | 504990 | 18 | -89.9 | 504990 | 406 | -93.9 | 504990 | 996 | -96.2 | 504990 | 823 |
| MR_1774417172_B1AE9753 | 504990 | 18 | -86.2 | 504990 | 406 | -96.3 | 504990 | 996 | -95.9 | 504990 | 823 |
| MR_1774417172_CAD69187 | 504990 | 18 | -86.7 | 504990 | 406 | -96.0 | 504990 | 996 | -98.9 | 504990 | 823 |
| MR_1774417172_C81564E2 | 504990 | 18 | -88.5 | 504990 | 406 | -92.8 | 504990 | 996 | -97.5 | 504990 | 823 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1584: `a2ab62a8-b7e...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `a2ab62a8-b7e1-4f40-a477-021589e1d75d` |
| Tag | **multiple-answer** |
| 정답 | **C1|C13|C14|C21** |
| C1 의미 | Press down the tilt angle  of 3236914_1 by 6 degrees |
| C13 의미 | Decrease transmission power for 3236914_1 |
| C14 의미 | Increase A3 Offset threshold for 3236914_1 |
| C21 의미 | Increase A3 Offset threshold for 3266155_5 |
| 패턴 분류 | **P3 Overshoot (tilt)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1584] topology](images/train_1584.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 5 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 5개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3236914_1 by 6 degrees **← 정답**
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3236914_1
- `C3`: Decrease A3 Offset threshold for 3236914_1
- `C4`: Add neighbor relationship between 3247905_2 and 3236914_1
- `C5`: Insufficient data; more data is needed for judgment.
- `C6`: Press down the tilt angle of 3266155_5 by 5 degrees
- `C7`: Lift the tilt angle of 3266155_5 by 5 degrees
- `C8`: Lift the tilt angle  of 3236914_1 by 6 degrees
- `C9`: Check test server and transmission issues
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3236914_1
- `C11`: Adjust the azimuth of 3266155_5 by 0 degrees
- `C12`: Decrease transmission power for 3266155_5
- `C13`: Decrease transmission power for 3236914_1 **← 정답**
- `C14`: Increase A3 Offset threshold for 3236914_1 **← 정답**
- `C15`: Add neighbor relationship between 3266155_5 and 3236914_1
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3266155_5
- `C17`: Decrease A3 Offset threshold for 3266155_5
- `C18`: Increase transmission power for 3236914_1
- `C19`: Adjust the azimuth of 3236914_1 by 36 degrees
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3266155_5
- `C21`: Increase A3 Offset threshold for 3266155_5 **← 정답**
- `C22`: Increase transmission power for 3266155_5

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.226 | MS1 | 121.4656647426 | 31.1446321584 | 952 | 504990 | -81.52 | 13.95 | 475.48 | 0.18 | 2.61 | 1563 |
| 2024-09-20 22:21:32.920 | MS1 | 121.4656655058 | 31.1446246195 | 952 | 504990 | -76.46 | 13.21 | 420.86 | 0.08 | 2.25 | 1568 |
| 2024-09-20 22:21:33.516 | MS1 | 121.4656745796 | 31.1446325245 | 952 | 504990 | -77.50 | 12.02 | 423.72 | 0.14 | 2.42 | 1600 |
| 2024-09-20 22:21:34.628 | MS1 | 121.4656754708 | 31.1446196331 | 149 | 504990 | -89.58 | 1.24 | 38.50 | 0.07 | 1.14 | 1578 |
| 2024-09-20 22:21:35.313 | MS1 | 121.4656693480 | 31.1446313246 | 149 | 504990 | -89.27 | 3.62 | 46.02 | 0.15 | 1.22 | 1585 |
| 2024-09-20 22:21:36.650 | MS1 | 121.4656776859 | 31.1446333074 | 952 | 504990 | -85.40 | 3.42 | 36.97 | 0.02 | 1.31 | 1595 |
| 2024-09-20 22:21:37.103 | MS1 | 121.4656676630 | 31.1446275590 | 952 | 504990 | -89.80 | 2.04 | 41.77 | 0.10 | 1.36 | 1578 |
| 2024-09-20 22:21:38.834 | MS1 | 121.4656737751 | 31.1446253691 | 149 | 504990 | -86.88 | 4.47 | 70.93 | 0.17 | 1.12 | 1579 |
| 2024-09-20 22:21:39.252 | MS1 | 121.4656680256 | 31.1446206605 | 149 | 504990 | -83.56 | 4.56 | 67.56 | 0.16 | 1.46 | 1572 |
| 2024-09-20 22:21:40.443 | MS1 | 121.4656712803 | 31.1446342173 | 149 | 504990 | -84.45 | 15.86 | 505.23 | 0.02 | 2.04 | 1570 |
| 2024-09-20 22:21:41.683 | MS1 | 121.4656656684 | 31.1446213492 | 149 | 504990 | -83.59 | 13.56 | 481.95 | 0.08 | 2.21 | 1597 |
| 2024-09-20 22:21:42.871 | MS1 | 121.4656630782 | 31.1446182595 | 149 | 504990 | -81.73 | 15.87 | 351.68 | 0.14 | 2.43 | 1595 |

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
| 3222204 | 3 | 121.4655058304 | 31.1505404278 | 13 | 3 | 9 | 24.9 | TDD | 626 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3236914 | 1 | 121.4680119763 | 31.1485860719 | 243 | 3 | 10 | 22.9 | TDD | 143 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3239296 | 4 | 121.4731007220 | 31.1501043366 | 323 | 0 | 0 | 25.7 | TDD | 149 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3247905 | 2 | 121.4644435148 | 31.1449506411 | 356 | 12 | 7 | 26.3 | TDD | 176 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3266155 | 5 | 121.4719241627 | 31.1559210766 | 205 | 3 | 11 | 48.2 | TDD | 952 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |

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
| 2024-09-20 22:21:30.940 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.957 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.106 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.106 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:33.757 | NREventA3 | measId:2;ServCellPCI:172;Se... |
| 2024-09-20 22:21:33.997 | NRHandoverAttempt | SourcePCI:172;SourceNR-ARFC... |
| 2024-09-20 22:21:34.033 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:34.045 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:34.182 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:34.182 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.757 | NREventA3 | measId:2;ServCellPCI:527;Se... |
| 2024-09-20 22:21:35.997 | NRHandoverAttempt | SourcePCI:527;SourceNR-ARFC... |
| 2024-09-20 22:21:36.027 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:36.037 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:36.177 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.177 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.757 | NREventA3 | measId:2;ServCellPCI:172;Se... |
| 2024-09-20 22:21:37.997 | NRHandoverAttempt | SourcePCI:172;SourceNR-ARFC... |
| 2024-09-20 22:21:38.036 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.051 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.179 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.179 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3236914 | 1 | 6.2482 | 14.1942 | -115.3441 | 5.9884 | 137.7099 | 0.0057 | 0.0155 |
| 2024_09_20 22:00 | 3247905 | 2 | 8.1252 | 7.6171 | -114.4301 | 12.3583 | 159.3608 | 0.0190 | 0.0195 |
| 2024_09_20 22:00 | 3222204 | 3 | 8.6231 | 7.3457 | -116.7525 | 15.9754 | 135.8111 | 0.0122 | 0.0160 |
| 2024_09_20 22:00 | 3239296 | 4 | 16.2538 | 16.7531 | -115.6326 | 8.4837 | 186.7089 | 0.0154 | 0.0109 |
| 2024_09_20 22:00 | 3266155 | 5 | 6.5880 | 17.9252 | -114.6848 | 11.4100 | 117.9482 | 0.0050 | 0.0152 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416593_10EB7C12 | 504990 | 952 | -90.6 | 504990 | 149 | -88.2 | 504990 | 143 | -90.4 | 504990 | 176 |
| MR_1774416593_5F51EF7C | 504990 | 149 | -90.6 | 504990 | 952 | -88.6 | 504990 | 143 | -91.4 | 504990 | 176 |
| MR_1774416593_C83491CA | 504990 | 952 | -91.1 | 504990 | 149 | -90.8 | 504990 | 143 | -91.1 | 504990 | 176 |
| MR_1774416593_3B528AEE | 504990 | 952 | -91.1 | 504990 | 149 | -88.5 | 504990 | 143 | -90.1 | 504990 | 176 |
| MR_1774416593_EFA0FF03 | 504990 | 952 | -91.0 | 504990 | 149 | -90.9 | 504990 | 143 | -88.1 | 504990 | 176 |
| MR_1774416593_C6027568 | 504990 | 149 | -89.4 | 504990 | 952 | -90.8 | 504990 | 143 | -90.6 | 504990 | 176 |
| MR_1774416593_71812CDE | 504990 | 149 | -91.4 | 504990 | 952 | -90.1 | 504990 | 143 | -88.3 | 504990 | 176 |
| MR_1774416593_78DBE926 | 504990 | 952 | -87.6 | 504990 | 149 | -89.6 | 504990 | 143 | -92.0 | 504990 | 176 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1585: `c79c9e9c-1e8...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `c79c9e9c-1e8e-4784-9345-3ce19d9e248f` |
| Tag | **single-answer** |
| 정답 | **C1** |
| C1 의미 | Lift the tilt angle  of 3245353_3 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1585] topology](images/train_1585.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle  of 3245353_3 by 10 degrees **← 정답**
- `C2`: Insufficient data; more data is needed for judgment.
- `C3`: Decrease transmission power for 3241995_1
- `C4`: Add neighbor relationship between 3276421_2 and 3241995_1
- `C5`: Increase A3 Offset threshold for 3241995_1
- `C6`: Press down the tilt angle of 3276421_2 by 2 degrees
- `C7`: Lift the tilt angle of 3276421_2 by 2 degrees
- `C8`: Add neighbor relationship between 3245353_3 and 3241995_1
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3276421_2
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3276421_2
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3241995_1
- `C12`: Adjust the azimuth of 3245353_3 by 50 degrees
- `C13`: Press down the tilt angle  of 3245353_3 by 10 degrees
- `C14`: Decrease transmission power for 3276421_2
- `C15`: Increase A3 Offset threshold for 3276421_2
- `C16`: Adjust the azimuth of 3276421_2 by 40 degrees
- `C17`: Decrease A3 Offset threshold for 3276421_2
- `C18`: Increase transmission power for 3241995_1
- `C19`: Increase transmission power for 3276421_2
- `C20`: Decrease A3 Offset threshold for 3241995_1
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3241995_1
- `C22`: Check test server and transmission issues

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.350 | MS1 | 121.4656635700 | 31.1446367647 | 899 | 504990 | -90.65 | 17.37 | 505.59 | 0.14 | 2.57 | 1592 |
| 2024-09-20 22:21:32.752 | MS1 | 121.4656616223 | 31.1446184438 | 899 | 504990 | -91.63 | 16.50 | 355.61 | 0.02 | 2.23 | 1593 |
| 2024-09-20 22:21:33.542 | MS1 | 121.4656662806 | 31.1446288841 | 899 | 504990 | -90.41 | 17.38 | 468.76 | 0.17 | 2.68 | 1582 |
| 2024-09-20 22:21:34.592 | MS1 | 121.4656687172 | 31.1446281078 | 899 | 504990 | -88.87 | 14.07 | 65.01 | 0.01 | 2.93 | 1564 |
| 2024-09-20 22:21:35.127 | MS1 | 121.4656771425 | 31.1446257064 | 899 | 504990 | -86.20 | 12.98 | 76.67 | 0.14 | 2.57 | 1600 |
| 2024-09-20 22:21:36.522 | MS1 | 121.4656634342 | 31.1446363719 | 899 | 504990 | -87.21 | 16.46 | 65.80 | 0.18 | 2.02 | 1600 |
| 2024-09-20 22:21:37.499 | MS1 | 121.4656593032 | 31.1446258253 | 899 | 504990 | -91.31 | 8.99 | 77.67 | 0.12 | 2.49 | 1599 |
| 2024-09-20 22:21:38.742 | MS1 | 121.4656736902 | 31.1446274279 | 899 | 504990 | -90.81 | 9.91 | 61.26 | 0.17 | 2.67 | 1581 |
| 2024-09-20 22:21:39.807 | MS1 | 121.4656699547 | 31.1446237759 | 899 | 504990 | -91.90 | 12.77 | 100.70 | 0.13 | 2.27 | 1579 |
| 2024-09-20 22:21:40.153 | MS1 | 121.4656700151 | 31.1446335545 | 899 | 504990 | -90.19 | 9.20 | 459.18 | 0.02 | 2.76 | 1564 |
| 2024-09-20 22:21:41.417 | MS1 | 121.4656657820 | 31.1446189577 | 899 | 504990 | -91.05 | 8.69 | 333.85 | 0.04 | 2.50 | 1561 |
| 2024-09-20 22:21:42.309 | MS1 | 121.4656631600 | 31.1446371747 | 899 | 504990 | -92.73 | 9.84 | 317.89 | 0.00 | 2.67 | 1599 |

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
| 3240394 | 4 | 121.4691278923 | 31.1530915695 | 243 | 4 | 0 | 23.9 | TDD | 573 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3241995 | 1 | 121.4711680302 | 31.1475070417 | 310 | 14 | 8 | 24.8 | TDD | 560 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3245353 | 3 | 121.4731153260 | 31.1516318970 | 44 | 5 | 1 | 33.2 | TDD | 588 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3276421 | 2 | 121.4758468033 | 31.1518869356 | 190 | 1 | 6 | 25.6 | TDD | 899 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |

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
| 2024-09-20 22:21:31.622 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.637 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.760 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.760 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.422 | NREventA3 | measId:2;ServCellPCI:161;Se... |
| 2024-09-20 22:21:38.662 | NRHandoverAttempt | SourcePCI:161;SourceNR-ARFC... |
| 2024-09-20 22:21:38.693 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.703 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.804 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.804 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3241995 | 1 | 19.4950 | 14.2970 | -115.9825 | 13.3288 | 149.8995 | 0.0030 | 0.0063 |
| 2024_09_20 22:00 | 3276421 | 2 | 85.9154 | 82.3647 | -115.4828 | 19.2328 | 95.6643 | 0.0003 | 0.0100 |
| 2024_09_20 22:00 | 3245353 | 3 | 13.6611 | 9.0051 | -116.9540 | 12.4592 | 146.7255 | 0.0102 | 0.0091 |
| 2024_09_20 22:00 | 3240394 | 4 | 14.7269 | 12.6165 | -117.0335 | 15.9804 | 115.3173 | 0.0198 | 0.0181 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414883_56C6C420 | 504990 | 899 | -90.2 | 504990 | 560 | -93.7 | 504990 | 588 | -101.0 | 504990 | 573 |
| MR_1774414883_24937007 | 504990 | 899 | -89.8 | 504990 | 560 | -93.5 | 504990 | 588 | -103.9 | 504990 | 573 |
| MR_1774414883_6AC79F74 | 504990 | 899 | -87.6 | 504990 | 560 | -95.4 | 504990 | 588 | -104.4 | 504990 | 573 |
| MR_1774414883_FBC46B1B | 504990 | 899 | -89.6 | 504990 | 560 | -93.4 | 504990 | 588 | -101.1 | 504990 | 573 |
| MR_1774414883_EEE93051 | 504990 | 899 | -88.3 | 504990 | 560 | -92.9 | 504990 | 588 | -104.6 | 504990 | 573 |
| MR_1774414883_4A0F86E1 | 504990 | 899 | -87.2 | 504990 | 560 | -93.6 | 504990 | 588 | -104.3 | 504990 | 573 |
| MR_1774414883_CCC9AE06 | 504990 | 899 | -90.3 | 504990 | 560 | -93.3 | 504990 | 588 | -104.1 | 504990 | 573 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1586: `15ac0c8a-9e0...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `15ac0c8a-9e08-4d6a-bf9c-9e4fcd18daba` |
| Tag | **single-answer** |
| 정답 | **C14** |
| C14 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3218503_4 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1586] topology](images/train_1586.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3253677_1 by 5 degrees
- `C2`: Adjust the azimuth of 3218503_4 by 2 degrees
- `C3`: Insufficient data; more data is needed for judgment.
- `C4`: Increase A3 Offset threshold for 3218503_4
- `C5`: Lift the tilt angle  of 3253677_1 by 5 degrees
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3253677_1
- `C7`: Decrease transmission power for 3253677_1
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3218503_4
- `C9`: Lift the tilt angle of 3218503_4 by 4 degrees
- `C10`: Press down the tilt angle of 3218503_4 by 4 degrees
- `C11`: Add neighbor relationship between 3218503_4 and 3253677_1
- `C12`: Decrease transmission power for 3218503_4
- `C13`: Add neighbor relationship between 3216900_3 and 3253677_1
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3218503_4 **← 정답**
- `C15`: Increase transmission power for 3218503_4
- `C16`: Adjust the azimuth of 3253677_1 by 50 degrees
- `C17`: Decrease A3 Offset threshold for 3253677_1
- `C18`: Check test server and transmission issues
- `C19`: Increase transmission power for 3253677_1
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3253677_1
- `C21`: Decrease A3 Offset threshold for 3218503_4
- `C22`: Increase A3 Offset threshold for 3253677_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.976 | MS1 | 121.4656757380 | 31.1446229620 | 767 | 504990 | -89.31 | 16.51 | 459.24 | 0.15 | 2.26 | 1582 |
| 2024-09-20 22:21:32.344 | MS1 | 121.4656772615 | 31.1446348598 | 767 | 504990 | -87.79 | 13.29 | 350.13 | 0.16 | 2.68 | 1580 |
| 2024-09-20 22:21:33.923 | MS1 | 121.4656603055 | 31.1446344150 | 767 | 504990 | -89.96 | 15.06 | 411.43 | 0.01 | 2.22 | 1576 |
| 2024-09-20 22:21:34.934 | MS1 | 121.4656753652 | 31.1446232314 | 767 | 504990 | -90.78 | 17.07 | 60.35 | 0.64 | 2.36 | 635 |
| 2024-09-20 22:21:35.681 | MS1 | 121.4656679586 | 31.1446214754 | 767 | 504990 | -86.42 | 16.48 | 65.52 | 0.64 | 2.88 | 659 |
| 2024-09-20 22:21:36.203 | MS1 | 121.4656640872 | 31.1446316363 | 767 | 504990 | -89.59 | 12.29 | 73.82 | 0.68 | 2.08 | 622 |
| 2024-09-20 22:21:37.304 | MS1 | 121.4656658141 | 31.1446233865 | 767 | 504990 | -89.25 | 12.29 | 82.07 | 0.50 | 2.97 | 521 |
| 2024-09-20 22:21:38.200 | MS1 | 121.4656666617 | 31.1446356102 | 767 | 504990 | -89.66 | 8.12 | 81.13 | 0.52 | 2.61 | 605 |
| 2024-09-20 22:21:39.502 | MS1 | 121.4656679919 | 31.1446307371 | 767 | 504990 | -91.77 | 7.49 | 66.18 | 0.68 | 2.14 | 643 |
| 2024-09-20 22:21:40.645 | MS1 | 121.4656774332 | 31.1446334321 | 767 | 504990 | -92.76 | 11.49 | 421.49 | 0.12 | 2.17 | 1571 |
| 2024-09-20 22:21:41.853 | MS1 | 121.4656581466 | 31.1446289969 | 767 | 504990 | -91.79 | 12.85 | 488.46 | 0.11 | 2.90 | 1588 |
| 2024-09-20 22:21:42.497 | MS1 | 121.4656633497 | 31.1446305510 | 767 | 504990 | -89.37 | 7.47 | 576.44 | 0.15 | 2.75 | 1583 |

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
| 3216900 | 3 | 121.4752492788 | 31.1494863620 | 353 | 6 | 4 | 36.8 | TDD | 219 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3218503 | 4 | 121.4696019881 | 31.1546427633 | 197 | 3 | 6 | 28.2 | TDD | 767 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3251902 | 2 | 121.4644837383 | 31.1521984175 | 276 | 0 | 5 | 48.2 | TDD | 505 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3253677 | 1 | 121.4745877741 | 31.1511688267 | 65 | 4 | 8 | 28.3 | TDD | 488 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |

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
| 2024-09-20 22:21:31.498 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.522 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.636 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.636 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.397 | NREventA3 | measId:2;ServCellPCI:970;Se... |
| 2024-09-20 22:21:38.637 | NRHandoverAttempt | SourcePCI:970;SourceNR-ARFC... |
| 2024-09-20 22:21:38.667 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.678 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.807 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.807 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3253677 | 1 | 5.5194 | 7.8343 | -116.9263 | 15.1361 | 149.3079 | 0.0019 | 0.0084 |
| 2024_09_20 22:00 | 3251902 | 2 | 12.9348 | 11.8153 | -116.9951 | 7.8838 | 146.4826 | 0.0022 | 0.0064 |
| 2024_09_20 22:00 | 3216900 | 3 | 16.7967 | 19.9243 | -114.8877 | 10.3646 | 114.6520 | 0.0090 | 0.0121 |
| 2024_09_20 22:00 | 3218503 | 4 | 15.3365 | 10.4585 | -115.2733 | 17.0810 | 170.6029 | 0.0148 | 0.0088 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416599_CA52BF3E | 504990 | 767 | -91.6 | 504990 | 488 | -98.1 | 504990 | 219 | -100.2 | 504990 | 505 |
| MR_1774416599_577A3610 | 504990 | 767 | -92.0 | 504990 | 488 | -99.3 | 504990 | 219 | -101.5 | 504990 | 505 |
| MR_1774416599_74600B41 | 504990 | 767 | -89.1 | 504990 | 488 | -99.3 | 504990 | 219 | -101.3 | 504990 | 505 |
| MR_1774416599_2D63E696 | 504990 | 767 | -91.9 | 504990 | 488 | -99.7 | 504990 | 219 | -100.5 | 504990 | 505 |
| MR_1774416599_67D9E18C | 504990 | 767 | -89.5 | 504990 | 488 | -98.0 | 504990 | 219 | -102.9 | 504990 | 505 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1587: `013d249c-921...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `013d249c-9215-4451-af7d-78c58b471295` |
| Tag | **multiple-answer** |
| 정답 | **C11|C14** |
| C11 의미 | Press down the tilt angle  of 3244646_3 by 4 degrees |
| C14 의미 | Decrease transmission power for 3244646_3 |
| 패턴 분류 | **P3 Overshoot (tilt)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1587] topology](images/train_1587.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3239926_1 and 3244646_3
- `C2`: Check test server and transmission issues
- `C3`: Add neighbor relationship between 3211483_4 and 3244646_3
- `C4`: Increase A3 Offset threshold for 3239926_1
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3239926_1
- `C6`: Increase transmission power for 3244646_3
- `C7`: Adjust the azimuth of 3239926_1 by 47 degrees
- `C8`: Decrease transmission power for 3239926_1
- `C9`: Decrease A3 Offset threshold for 3239926_1
- `C10`: Insufficient data; more data is needed for judgment.
- `C11`: Press down the tilt angle  of 3244646_3 by 4 degrees **← 정답**
- `C12`: Lift the tilt angle  of 3244646_3 by 4 degrees
- `C13`: Press down the tilt angle of 3239926_1 by 4 degrees
- `C14`: Decrease transmission power for 3244646_3 **← 정답**
- `C15`: Increase transmission power for 3239926_1
- `C16`: Adjust the azimuth of 3244646_3 by 15 degrees
- `C17`: Increase A3 Offset threshold for 3244646_3
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3244646_3
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3244646_3
- `C20`: Lift the tilt angle of 3239926_1 by 4 degrees
- `C21`: Decrease A3 Offset threshold for 3244646_3
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3239926_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.270 | MS1 | 121.4656604099 | 31.1446203974 | 552 | 504990 | -76.01 | 17.06 | 487.59 | 0.15 | 2.11 | 1561 |
| 2024-09-20 22:21:32.994 | MS1 | 121.4656677532 | 31.1446333844 | 552 | 504990 | -75.18 | 14.24 | 395.39 | 0.00 | 2.89 | 1599 |
| 2024-09-20 22:21:33.978 | MS1 | 121.4656581132 | 31.1446341314 | 552 | 504990 | -83.01 | 16.98 | 450.02 | 0.01 | 2.10 | 1574 |
| 2024-09-20 22:21:34.487 | MS1 | 121.4656628091 | 31.1446241507 | 552 | 504990 | -85.16 | 0.94 | 41.91 | 0.02 | 1.49 | 1588 |
| 2024-09-20 22:21:35.857 | MS1 | 121.4656592868 | 31.1446356165 | 552 | 504990 | -94.95 | 1.10 | 31.56 | 0.17 | 1.39 | 1599 |
| 2024-09-20 22:21:36.892 | MS1 | 121.4656694927 | 31.1446283690 | 552 | 504990 | -91.26 | 2.14 | 57.77 | 0.13 | 1.09 | 1566 |
| 2024-09-20 22:21:37.396 | MS1 | 121.4656704245 | 31.1446293435 | 552 | 504990 | -92.66 | 3.38 | 40.05 | 0.19 | 1.38 | 1581 |
| 2024-09-20 22:21:38.140 | MS1 | 121.4656737592 | 31.1446236512 | 552 | 504990 | -88.68 | 3.41 | 94.93 | 0.18 | 1.19 | 1576 |
| 2024-09-20 22:21:39.593 | MS1 | 121.4656774450 | 31.1446323666 | 552 | 504990 | -85.10 | 1.45 | 52.06 | 0.13 | 1.42 | 1584 |
| 2024-09-20 22:21:40.866 | MS1 | 121.4656596612 | 31.1446360974 | 552 | 504990 | -75.84 | 13.77 | 362.65 | 0.08 | 2.42 | 1581 |
| 2024-09-20 22:21:41.154 | MS1 | 121.4656648243 | 31.1446379000 | 552 | 504990 | -78.62 | 14.46 | 371.03 | 0.18 | 2.88 | 1596 |
| 2024-09-20 22:21:42.146 | MS1 | 121.4656644620 | 31.1446321840 | 552 | 504990 | -83.50 | 14.95 | 457.40 | 0.07 | 2.95 | 1592 |

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
| 3211483 | 4 | 121.4748749569 | 31.1465553222 | 306 | 8 | 9 | 31.4 | TDD | 629 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3228914 | 2 | 121.4642116806 | 31.1493882513 | 39 | 8 | 0 | 32.4 | TDD | 417 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3239926 | 1 | 121.4709618335 | 31.1536078295 | 254 | 2 | 2 | 41.3 | TDD | 552 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3244646 | 3 | 121.4743528137 | 31.1541211068 | 233 | 2 | 4 | 46.9 | TDD | 316 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |

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
| 2024-09-20 22:21:31.272 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.292 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.398 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.398 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3239926 | 1 | 19.2356 | 8.3822 | -109.5025 | 19.8245 | 173.4694 | 0.0010 | 0.0140 |
| 2024_09_20 22:00 | 3228914 | 2 | 12.2767 | 7.4268 | -115.6480 | 17.2633 | 150.2819 | 0.0079 | 0.0025 |
| 2024_09_20 22:00 | 3244646 | 3 | 10.4434 | 6.5568 | -116.7055 | 16.8029 | 137.3549 | 0.0026 | 0.0021 |
| 2024_09_20 22:00 | 3211483 | 4 | 17.3520 | 8.0859 | -114.3170 | 12.9497 | 126.6372 | 0.0089 | 0.0166 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416857_B5D0CBCB | 504990 | 316 | -84.4 | 504990 | 552 | -82.4 | 504990 | 629 | -85.3 | 504990 | 417 |
| MR_1774416857_01272903 | 504990 | 552 | -85.8 | 504990 | 316 | -84.4 | 504990 | 629 | -86.1 | 504990 | 417 |
| MR_1774416857_2FCD9530 | 504990 | 552 | -85.2 | 504990 | 316 | -82.4 | 504990 | 629 | -85.0 | 504990 | 417 |
| MR_1774416857_61FFB933 | 504990 | 316 | -85.9 | 504990 | 552 | -85.6 | 504990 | 629 | -87.8 | 504990 | 417 |
| MR_1774416857_51A83C9F | 504990 | 552 | -86.5 | 504990 | 316 | -83.3 | 504990 | 629 | -85.3 | 504990 | 417 |
| MR_1774416857_A528706A | 504990 | 316 | -84.3 | 504990 | 552 | -85.2 | 504990 | 629 | -88.6 | 504990 | 417 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1588: `1872a53a-39e...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `1872a53a-39e3-487b-80f2-2a56d43e227d` |
| Tag | **single-answer** |
| 정답 | **C11** |
| C11 의미 | Decrease A3 Offset threshold for 3230342_1 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1588] topology](images/train_1588.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3217680_4 by 6 degrees
- `C2`: Insufficient data; more data is needed for judgment.
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3230342_1
- `C4`: Check test server and transmission issues
- `C5`: Increase A3 Offset threshold for 3217680_4
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3217680_4
- `C7`: Lift the tilt angle  of 3217680_4 by 6 degrees
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3217680_4
- `C9`: Increase A3 Offset threshold for 3230342_1
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3230342_1
- `C11`: Decrease A3 Offset threshold for 3230342_1 **← 정답**
- `C12`: Decrease A3 Offset threshold for 3217680_4
- `C13`: Decrease transmission power for 3217680_4
- `C14`: Adjust the azimuth of 3230342_1 by 4 degrees
- `C15`: Lift the tilt angle of 3230342_1 by 10 degrees
- `C16`: Add neighbor relationship between 3230342_1 and 3217680_4
- `C17`: Increase transmission power for 3217680_4
- `C18`: Decrease transmission power for 3230342_1
- `C19`: Add neighbor relationship between 3259843_3 and 3217680_4
- `C20`: Adjust the azimuth of 3217680_4 by 50 degrees
- `C21`: Increase transmission power for 3230342_1
- `C22`: Press down the tilt angle of 3230342_1 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.741 | MS1 | 121.4656751239 | 31.1446264629 | 632 | 504990 | -80.84 | 17.19 | 414.82 | 0.01 | 2.28 | 1591 |
| 2024-09-20 22:21:32.400 | MS1 | 121.4656763685 | 31.1446240569 | 632 | 504990 | -78.14 | 15.18 | 542.30 | 0.01 | 2.77 | 1565 |
| 2024-09-20 22:21:33.464 | MS1 | 121.4656639470 | 31.1446372543 | 632 | 504990 | -75.60 | 12.09 | 587.33 | 0.05 | 2.94 | 1600 |
| 2024-09-20 22:21:34.406 | MS1 | 121.4656740720 | 31.1446279320 | 632 | 504990 | -86.14 | -3.27 | 70.65 | 0.02 | 1.11 | 1600 |
| 2024-09-20 22:21:35.772 | MS1 | 121.4656703608 | 31.1446252941 | 632 | 504990 | -87.27 | -1.58 | 65.08 | 0.07 | 1.13 | 1588 |
| 2024-09-20 22:21:36.740 | MS1 | 121.4656589618 | 31.1446281016 | 632 | 504990 | -83.44 | -1.54 | 44.37 | 0.14 | 1.35 | 1563 |
| 2024-09-20 22:21:37.499 | MS1 | 121.4656730397 | 31.1446233965 | 632 | 504990 | -91.37 | -1.10 | 58.64 | 0.02 | 1.08 | 1579 |
| 2024-09-20 22:21:38.735 | MS1 | 121.4656644544 | 31.1446364453 | 632 | 504990 | -92.38 | -3.04 | 41.68 | 0.18 | 1.33 | 1596 |
| 2024-09-20 22:21:39.637 | MS1 | 121.4656717461 | 31.1446207324 | 432 | 504990 | -78.57 | 17.44 | 260.69 | 0.11 | 1.29 | 1561 |
| 2024-09-20 22:21:40.768 | MS1 | 121.4656596617 | 31.1446222298 | 432 | 504990 | -82.74 | 14.94 | 457.45 | 0.05 | 2.03 | 1597 |
| 2024-09-20 22:21:41.994 | MS1 | 121.4656653454 | 31.1446194319 | 432 | 504990 | -81.93 | 12.90 | 477.12 | 0.09 | 2.12 | 1597 |
| 2024-09-20 22:21:42.136 | MS1 | 121.4656647701 | 31.1446301621 | 432 | 504990 | -75.02 | 15.62 | 409.52 | 0.02 | 2.47 | 1595 |

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
| 3213919 | 2 | 121.4736286422 | 31.1477439399 | 157 | 8 | 8 | 36.5 | TDD | 447 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3217680 | 4 | 121.4754065028 | 31.1492366561 | 98 | 3 | 8 | 46.9 | TDD | 432 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3230342 | 1 | 121.4664775501 | 31.1485633361 | 186 | 11 | 12 | 37.8 | TDD | 632 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3259843 | 3 | 121.4723202209 | 31.1450024341 | 102 | 4 | 11 | 25.7 | TDD | 206 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:31.111 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.237 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.237 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.954 | NREventA3 | measId:2;ServCellPCI:953;Se... |
| 2024-09-20 22:21:38.194 | NRHandoverAttempt | SourcePCI:953;SourceNR-ARFC... |
| 2024-09-20 22:21:38.244 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.255 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.356 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.356 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3230342 | 1 | 9.6990 | 19.0238 | -116.2126 | 18.9967 | 170.5257 | 0.0020 | 0.1333 |
| 2024_09_20 22:00 | 3213919 | 2 | 17.5503 | 8.9997 | -116.8048 | 14.8517 | 126.4154 | 0.0018 | 0.0040 |
| 2024_09_20 22:00 | 3259843 | 3 | 9.9565 | 7.3105 | -115.2727 | 18.1342 | 132.3526 | 0.0017 | 0.0068 |
| 2024_09_20 22:00 | 3217680 | 4 | 13.2286 | 8.2989 | -115.0948 | 8.6592 | 122.8486 | 0.0074 | 0.0029 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415709_C8BF31A0 | 504990 | 632 | -88.1 | 504990 | 432 | -81.4 | 504990 | 206 | -87.9 | 504990 | 447 |
| MR_1774415709_3889BC99 | 504990 | 432 | -81.8 | 504990 | 632 | -86.2 | 504990 | 206 | -85.8 | 504990 | 447 |
| MR_1774415709_BEC498A3 | 504990 | 432 | -81.7 | 504990 | 632 | -87.0 | 504990 | 206 | -89.2 | 504990 | 447 |
| MR_1774415709_A826929A | 504990 | 632 | -86.4 | 504990 | 432 | -83.2 | 504990 | 206 | -86.4 | 504990 | 447 |
| MR_1774415709_C2CFBF75 | 504990 | 632 | -86.4 | 504990 | 432 | -80.3 | 504990 | 206 | -87.7 | 504990 | 447 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1589: `84aa1488-f26...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `84aa1488-f26a-485f-8113-ccf2bf903c3c` |
| Tag | **multiple-answer** |
| 정답 | **C14|C17** |
| C14 의미 | Increase transmission power for 3224993_3 |
| C17 의미 | Adjust the azimuth of 3224993_3 by 50 degrees |
| 패턴 분류 | **P4 Coverage (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1589] topology](images/train_1589.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3224993_3
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3253649_1
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3224993_3
- `C4`: Decrease transmission power for 3253649_1
- `C5`: Decrease A3 Offset threshold for 3253649_1
- `C6`: Add neighbor relationship between 3224993_3 and 3253649_1
- `C7`: Lift the tilt angle  of 3253649_1 by 3 degrees
- `C8`: Press down the tilt angle of 3224993_3 by 7 degrees
- `C9`: Insufficient data; more data is needed for judgment.
- `C10`: Press down the tilt angle  of 3253649_1 by 3 degrees
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3224993_3
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3253649_1
- `C13`: Increase transmission power for 3253649_1
- `C14`: Increase transmission power for 3224993_3 **← 정답**
- `C15`: Lift the tilt angle of 3224993_3 by 7 degrees
- `C16`: Increase A3 Offset threshold for 3253649_1
- `C17`: Adjust the azimuth of 3224993_3 by 50 degrees **← 정답**
- `C18`: Decrease transmission power for 3224993_3
- `C19`: Add neighbor relationship between 3216720_2 and 3253649_1
- `C20`: Increase A3 Offset threshold for 3224993_3
- `C21`: Check test server and transmission issues
- `C22`: Adjust the azimuth of 3253649_1 by 18 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.274 | MS1 | 121.4656609788 | 31.1446379182 | 723 | 504990 | -85.71 | 17.89 | 426.94 | 0.18 | 2.92 | 1586 |
| 2024-09-20 22:21:32.627 | MS1 | 121.4656585784 | 31.1446370137 | 723 | 504990 | -88.91 | 17.79 | 564.26 | 0.12 | 2.71 | 1599 |
| 2024-09-20 22:21:33.665 | MS1 | 121.4656627870 | 31.1446207579 | 723 | 504990 | -87.89 | 14.05 | 404.84 | 0.13 | 2.26 | 1593 |
| 2024-09-20 22:21:34.160 | MS1 | 121.4656651059 | 31.1446224388 | 723 | 504990 | -101.47 | -1.30 | 55.49 | 0.08 | 1.15 | 1569 |
| 2024-09-20 22:21:35.220 | MS1 | 121.4656658534 | 31.1446304226 | 723 | 504990 | -107.14 | 1.11 | 68.55 | 0.15 | 1.15 | 1571 |
| 2024-09-20 22:21:36.172 | MS1 | 121.4656652396 | 31.1446378861 | 723 | 504990 | -105.36 | -0.16 | 58.98 | 0.09 | 1.26 | 1592 |
| 2024-09-20 22:21:37.124 | MS1 | 121.4656717094 | 31.1446322353 | 723 | 504990 | -106.21 | -1.58 | 37.47 | 0.16 | 1.25 | 1562 |
| 2024-09-20 22:21:38.927 | MS1 | 121.4656620367 | 31.1446204066 | 723 | 504990 | -103.09 | 1.37 | 35.41 | 0.06 | 1.49 | 1568 |
| 2024-09-20 22:21:39.112 | MS1 | 121.4656776781 | 31.1446365966 | 723 | 504990 | -107.99 | -0.73 | 71.29 | 0.05 | 1.40 | 1587 |
| 2024-09-20 22:21:40.208 | MS1 | 121.4656704730 | 31.1446351058 | 723 | 504990 | -90.33 | 17.17 | 491.10 | 0.17 | 2.55 | 1580 |
| 2024-09-20 22:21:41.725 | MS1 | 121.4656697245 | 31.1446248553 | 723 | 504990 | -90.81 | 15.31 | 334.47 | 0.05 | 2.22 | 1588 |
| 2024-09-20 22:21:42.499 | MS1 | 121.4656701568 | 31.1446248391 | 723 | 504990 | -93.14 | 14.26 | 331.20 | 0.13 | 2.60 | 1570 |

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
| 3216720 | 2 | 121.4647259817 | 31.1471784869 | 299 | 1 | 8 | 29.6 | TDD | 162 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3217504 | 4 | 121.4731078038 | 31.1464034954 | 167 | 10 | 9 | 23.4 | TDD | 644 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3224993 | 3 | 121.4759317158 | 31.1558065285 | 291 | 6 | 12 | 36.2 | TDD | 723 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3253649 | 1 | 121.4754565140 | 31.1445173429 | 289 | 1 | 12 | 31.2 | TDD | 904 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:31.381 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.406 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.542 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.542 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.729 | NREventA2 | measId:1;ServCellPCI:465;Se... |
| 2024-09-20 22:21:34.844 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3253649 | 1 | 12.0638 | 17.2664 | -117.4618 | 17.2504 | 164.4242 | 0.0172 | 0.0004 |
| 2024_09_20 22:00 | 3216720 | 2 | 18.1489 | 19.2103 | -117.1390 | 11.6525 | 144.0381 | 0.0164 | 0.0124 |
| 2024_09_20 22:00 | 3224993 | 3 | 9.5728 | 8.1629 | -117.8926 | 15.7189 | 180.6403 | 0.1045 | 0.0012 |
| 2024_09_20 22:00 | 3217504 | 4 | 6.6056 | 13.0493 | -116.0413 | 18.0967 | 98.3183 | 0.0091 | 0.0192 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413429_6D4D84C0 | 504990 | 723 | -99.6 | 504990 | 904 | -105.7 | 504990 | 162 | -110.5 | 504990 | 644 |
| MR_1774413429_E02EA02D | 504990 | 723 | -101.3 | 504990 | 904 | -105.3 | 504990 | 162 | -107.4 | 504990 | 644 |
| MR_1774413429_584F7FDA | 504990 | 723 | -102.0 | 504990 | 904 | -106.8 | 504990 | 162 | -108.3 | 504990 | 644 |
| MR_1774413429_B4FF3FD6 | 504990 | 723 | -102.4 | 504990 | 904 | -104.8 | 504990 | 162 | -108.5 | 504990 | 644 |
| MR_1774413429_79EF4B7F | 504990 | 723 | -103.4 | 504990 | 904 | -105.0 | 504990 | 162 | -107.2 | 504990 | 644 |
| MR_1774413429_3344FFC0 | 504990 | 723 | -100.7 | 504990 | 904 | -106.8 | 504990 | 162 | -108.9 | 504990 | 644 |
| MR_1774413429_0BB8FC3D | 504990 | 723 | -101.1 | 504990 | 904 | -106.4 | 504990 | 162 | -110.0 | 504990 | 644 |
| MR_1774413429_8A5BF18C | 504990 | 723 | -100.0 | 504990 | 904 | -104.3 | 504990 | 162 | -109.2 | 504990 | 644 |

> *... 2개 열 생략 (전체 14열)*

---
