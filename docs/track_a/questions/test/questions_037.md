# Track A 문제 분석 — test[360]~test[369]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/test.json`
> 범위: test[360] ~ test[369] (10개)

## 목차

1. [문제 360: `b30e0689-def...`](#360) — single-answer
2. [문제 361: `f5c9bb3b-578...`](#361) — single-answer
3. [문제 362: `21be2d5e-b39...`](#362) — single-answer
4. [문제 363: `41ceeb25-c8d...`](#363) — single-answer
5. [문제 364: `2d1e7246-b1c...`](#364) — multiple-answer
6. [문제 365: `41f61b30-e7a...`](#365) — single-answer
7. [문제 366: `fa81d4d7-44b...`](#366) — single-answer
8. [문제 367: `0e12307c-6cd...`](#367) — single-answer
9. [문제 368: `8928b6a6-174...`](#368) — single-answer
10. [문제 369: `1548ce1d-00f...`](#369) — multiple-answer

---

### 문제 360: `b30e0689-def...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `b30e0689-deff-4b89-b65f-2345a6fcb378` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[360] topology](images/test_0360.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3248177_3 by 6 degrees
- `C2`: Decrease A3 Offset threshold for 3271513_1
- `C3`: Increase transmission power for 3271513_1
- `C4`: Decrease transmission power for 3248177_3
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3271513_1
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3248177_3
- `C7`: Increase A3 Offset threshold for 3271513_1
- `C8`: Increase transmission power for 3248177_3
- `C9`: Adjust the azimuth of 3248177_3 by 31 degrees
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3248177_3
- `C11`: Lift the tilt angle of 3248177_3 by 6 degrees
- `C12`: Increase A3 Offset threshold for 3248177_3
- `C13`: Check test server and transmission issues
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Decrease transmission power for 3271513_1
- `C16`: Add neighbor relationship between 3256356_2 and 3271513_1
- `C17`: Add neighbor relationship between 3248177_3 and 3271513_1
- `C18`: Decrease A3 Offset threshold for 3248177_3
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3271513_1
- `C20`: Lift the tilt angle  of 3271513_1 by 10 degrees
- `C21`: Press down the tilt angle  of 3271513_1 by 10 degrees
- `C22`: Adjust the azimuth of 3271513_1 by 50 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.875 | MS1 | 121.4656624335 | 31.1446231210 | 14 | 504990 | -87.22 | 13.41 | 357.35 | 0.03 | 2.38 | 1567 |
| 2024-09-20 22:21:32.146 | MS1 | 121.4656606325 | 31.1446211993 | 14 | 504990 | -88.84 | 17.49 | 538.60 | 0.17 | 2.27 | 1595 |
| 2024-09-20 22:21:33.250 | MS1 | 121.4656688410 | 31.1446283208 | 14 | 504990 | -88.60 | 17.41 | 311.99 | 0.16 | 2.26 | 1581 |
| 2024-09-20 22:21:34.449 | MS1 | 121.4656584448 | 31.1446218723 | 14 | 504990 | -89.25 | 13.38 | 54.01 | 0.66 | 2.90 | 593 |
| 2024-09-20 22:21:35.520 | MS1 | 121.4656662791 | 31.1446207057 | 14 | 504990 | -86.57 | 14.67 | 85.41 | 0.53 | 2.94 | 547 |
| 2024-09-20 22:21:36.833 | MS1 | 121.4656686687 | 31.1446330404 | 14 | 504990 | -85.95 | 17.75 | 56.07 | 0.63 | 2.04 | 608 |
| 2024-09-20 22:21:37.392 | MS1 | 121.4656604345 | 31.1446308601 | 14 | 504990 | -92.85 | 9.66 | 66.98 | 0.54 | 2.41 | 528 |
| 2024-09-20 22:21:38.877 | MS1 | 121.4656741923 | 31.1446332728 | 14 | 504990 | -91.36 | 7.11 | 59.93 | 0.61 | 2.38 | 537 |
| 2024-09-20 22:21:39.342 | MS1 | 121.4656719692 | 31.1446355800 | 14 | 504990 | -90.58 | 10.64 | 70.67 | 0.58 | 2.93 | 581 |
| 2024-09-20 22:21:40.449 | MS1 | 121.4656698407 | 31.1446348964 | 14 | 504990 | -90.39 | 11.08 | 487.47 | 0.11 | 2.38 | 1591 |
| 2024-09-20 22:21:41.282 | MS1 | 121.4656633939 | 31.1446301316 | 14 | 504990 | -89.98 | 11.81 | 416.88 | 0.16 | 2.61 | 1564 |
| 2024-09-20 22:21:42.890 | MS1 | 121.4656696098 | 31.1446232577 | 14 | 504990 | -93.48 | 7.54 | 458.95 | 0.09 | 2.57 | 1565 |

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
| 3232644 | 4 | 121.4662752667 | 31.1506500369 | 182 | 4 | 9 | 43.1 | TDD | 215 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3248177 | 3 | 121.4666743399 | 31.1515870600 | 218 | 3 | 7 | 40.0 | TDD | 14 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3256356 | 2 | 121.4718911529 | 31.1485294029 | 321 | 3 | 6 | 42.4 | TDD | 364 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3271513 | 1 | 121.4754561134 | 31.1499196807 | 52 | 10 | 4 | 31.7 | TDD | 555 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |

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
| 2024-09-20 22:21:30.773 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.793 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:30.924 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.924 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.648 | NREventA3 | measId:2;ServCellPCI:102;Se... |
| 2024-09-20 22:21:37.888 | NRHandoverAttempt | SourcePCI:102;SourceNR-ARFC... |
| 2024-09-20 22:21:37.923 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.934 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.072 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.072 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3271513 | 1 | 12.3640 | 16.2543 | -114.5735 | 12.3506 | 162.1984 | 0.0060 | 0.0121 |
| 2024_09_20 22:00 | 3256356 | 2 | 12.4003 | 18.0263 | -114.1832 | 7.0163 | 80.2696 | 0.0022 | 0.0014 |
| 2024_09_20 22:00 | 3248177 | 3 | 19.2928 | 17.4272 | -115.9705 | 19.7773 | 142.1217 | 0.0082 | 0.0130 |
| 2024_09_20 22:00 | 3232644 | 4 | 18.0322 | 14.7690 | -114.8334 | 12.2702 | 115.7508 | 0.0010 | 0.0069 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412310_2C1CBFD6 | 504990 | 14 | -88.3 | 504990 | 555 | -90.3 | 504990 | 364 | -104.0 | 504990 | 215 |
| MR_1774412310_46C240F6 | 504990 | 14 | -89.2 | 504990 | 555 | -90.8 | 504990 | 364 | -103.4 | 504990 | 215 |
| MR_1774412310_8E679906 | 504990 | 14 | -90.9 | 504990 | 555 | -90.1 | 504990 | 364 | -103.0 | 504990 | 215 |
| MR_1774412310_8C6780CD | 504990 | 14 | -87.9 | 504990 | 555 | -91.1 | 504990 | 364 | -102.8 | 504990 | 215 |
| MR_1774412310_5D8268C6 | 504990 | 14 | -88.5 | 504990 | 555 | -91.5 | 504990 | 364 | -104.4 | 504990 | 215 |
| MR_1774412310_B8BEBE20 | 504990 | 14 | -90.5 | 504990 | 555 | -91.4 | 504990 | 364 | -103.4 | 504990 | 215 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 361: `f5c9bb3b-578...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `f5c9bb3b-5782-45fe-af49-27cb8809fe8f` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[361] topology](images/test_0361.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3271650_3
- `C2`: Check test server and transmission issues
- `C3`: Add neighbor relationship between 3271650_3 and 3243026_4
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3271650_3
- `C5`: Press down the tilt angle of 3271650_3 by 2 degrees
- `C6`: Decrease transmission power for 3271650_3
- `C7`: Press down the tilt angle  of 3243026_4 by 6 degrees
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3243026_4
- `C9`: Add neighbor relationship between 3221076_8 and 3243026_4
- `C10`: Lift the tilt angle  of 3243026_4 by 6 degrees
- `C11`: Adjust the azimuth of 3271650_3 by 13 degrees
- `C12`: Increase transmission power for 3243026_4
- `C13`: Decrease transmission power for 3243026_4
- `C14`: Increase A3 Offset threshold for 3243026_4
- `C15`: Increase transmission power for 3271650_3
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3243026_4
- `C17`: Adjust the azimuth of 3243026_4 by 22 degrees
- `C18`: Insufficient data; more data is needed for judgment.
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3271650_3
- `C20`: Decrease A3 Offset threshold for 3243026_4
- `C21`: Lift the tilt angle of 3271650_3 by 2 degrees
- `C22`: Increase A3 Offset threshold for 3271650_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.744 | MS1 | 121.4656671944 | 31.1446257709 | 561 | 504990 | -95.71 | 14.76 | 588.64 | 0.20 | 2.50 | 1591 |
| 2024-09-20 22:21:32.499 | MS1 | 121.4656640340 | 31.1446319449 | 128 | 504990 | -93.88 | 10.10 | 365.70 | 0.04 | 2.10 | 1581 |
| 2024-09-20 22:21:33.736 | MS1 | 121.4656715851 | 31.1446310465 | 293 | 504990 | -95.01 | 10.43 | 352.02 | 0.06 | 2.34 | 1594 |
| 2024-09-20 22:21:34.471 | MS1 | 121.4656623972 | 31.1446245471 | 722 | 152650 | -95.93 | 3.95 | 57.97 | 0.06 | 1.89 | 900 |
| 2024-09-20 22:21:35.517 | MS1 | 121.4656585400 | 31.1446272700 | 814 | 152650 | -89.02 | 5.18 | 69.54 | 0.12 | 1.53 | 931 |
| 2024-09-20 22:21:36.927 | MS1 | 121.4656747859 | 31.1446225956 | 331 | 152650 | -92.51 | 5.12 | 85.93 | 0.19 | 1.82 | 903 |
| 2024-09-20 22:21:37.537 | MS1 | 121.4656678746 | 31.1446325666 | 342 | 152650 | -94.97 | 2.51 | 87.54 | 0.00 | 1.70 | 949 |
| 2024-09-20 22:21:38.874 | MS1 | 121.4656684391 | 31.1446242678 | 722 | 152650 | -93.80 | 3.90 | 72.05 | 0.09 | 1.91 | 952 |
| 2024-09-20 22:21:39.392 | MS1 | 121.4656589546 | 31.1446191525 | 814 | 152650 | -94.74 | 3.13 | 68.93 | 0.19 | 1.61 | 995 |
| 2024-09-20 22:21:40.514 | MS1 | 121.4656751457 | 31.1446229503 | 331 | 152650 | -89.35 | 3.16 | 60.85 | 0.06 | 2.85 | 1595 |
| 2024-09-20 22:21:41.721 | MS1 | 121.4656628588 | 31.1446182270 | 342 | 152650 | -92.67 | 7.19 | 90.59 | 0.07 | 2.59 | 1586 |
| 2024-09-20 22:21:42.298 | MS1 | 121.4656759734 | 31.1446341085 | 722 | 152650 | -93.94 | 4.30 | 73.96 | 0.17 | 2.47 | 1598 |

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
| 3211732 | 5 | 121.4727989881 | 31.1472828578 | 70 | 14 | 5 | 19.7 | TDD | 251 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3214607 | 2 | 121.4691968900 | 31.1440046038 | 57 | 7 | 9 | 3.1 | TDD | 293 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3221076 | 8 | 121.4648460617 | 31.1532766794 | 343 | 13 | 7 | 0.4 | FDD | 331 | n1 | 152650 | 30M | 4T4R | 19 | 152650 |
| 3223028 | 10 | 121.4670495364 | 31.1446123463 | 300 | 8 | 8 | 2.9 | FDD | 722 | n1 | 152650 | 30M | 4T4R | 26 | 152650 |
| 3230964 | 9 | 121.4699963201 | 31.1464595985 | 146 | 7 | 2 | 29.9 | FDD | 814 | n1 | 152650 | 30M | 4T4R | 23 | 152650 |
| 3234646 | 6 | 121.4701043800 | 31.1557446013 | 95 | 11 | 11 | 21.6 | TDD | 667 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3243026 | 4 | 121.4752111773 | 31.1487192491 | 265 | 4 | 8 | 26.7 | TDD | 753 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3247869 | 7 | 121.4737764884 | 31.1441544506 | 348 | 5 | 4 | 12.7 | FDD | 674 | n1 | 152650 | 30M | 4T4R | 27 | 152650 |
| 3250318 | 11 | 121.4706812668 | 31.1469821921 | 315 | 13 | 10 | 19.7 | FDD | 19 | n1 | 152650 | 30M | 4T4R | 24 | 152650 |
| 3252257 | 12 | 121.4640866935 | 31.1536829600 | 283 | 8 | 11 | 20.5 | FDD | 787 | n1 | 152650 | 30M | 4T4R | 15 | 152650 |
| 3262736 | 1 | 121.4709045168 | 31.1448982150 | 144 | 11 | 1 | 6.2 | TDD | 128 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3267778 | 13 | 121.4735275330 | 31.1533109704 | 309 | 0 | 2 | 1.9 | FDD | 342 | n1 | 152650 | 30M | 4T4R | 15 | 152650 |
| 3271650 | 3 | 121.4747714093 | 31.1510268441 | 218 | 1 | 3 | 13.4 | TDD | 561 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:30.956 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.102 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.102 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.804 | NREventA2 | measId:1;ServCellPCI:834;Se... |
| 2024-09-20 22:21:34.921 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.220 | NREventA5 | measId:3;ServCellPCI:834;Se... |
| 2024-09-20 22:21:35.254 | NRHandoverAttempt | SourcePCI:834;SourceNR-ARFC... |
| 2024-09-20 22:21:35.300 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.311 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:35.426 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.426 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3262736 | 1 | 18.3423 | 6.5724 | -117.9451 | 19.8492 | 83.7670 | 0.0078 | 0.0154 |
| 2024_09_20 22:00 | 3214607 | 2 | 19.7231 | 19.4491 | -117.5090 | 14.4120 | 185.8801 | 0.0067 | 0.0010 |
| 2024_09_20 22:00 | 3271650 | 3 | 5.7905 | 5.1135 | -115.7186 | 17.9148 | 194.7276 | 0.0167 | 0.0099 |
| 2024_09_20 22:00 | 3243026 | 4 | 15.9751 | 16.1409 | -115.5141 | 13.8456 | 91.6384 | 0.0176 | 0.0065 |
| 2024_09_20 22:00 | 3211732 | 5 | 10.2163 | 5.6810 | -117.4995 | 5.4162 | 189.2883 | 0.0140 | 0.0173 |
| 2024_09_20 22:00 | 3234646 | 6 | 12.3748 | 5.2573 | -114.4785 | 18.9905 | 180.6719 | 0.0146 | 0.0186 |
| 2024_09_20 22:00 | 3247869 | 7 | 16.2752 | 8.7591 | -117.4419 | 3.9321 | 45.7346 | 0.0013 | 0.0133 |
| 2024_09_20 22:00 | 3221076 | 8 | 13.4256 | 12.5745 | -115.4651 | 4.6879 | 28.1331 | 0.0144 | 0.0145 |
| 2024_09_20 22:00 | 3230964 | 9 | 15.8871 | 16.7856 | -115.7260 | 3.0609 | 24.7104 | 0.0189 | 0.0165 |
| 2024_09_20 22:00 | 3223028 | 10 | 9.4134 | 7.4969 | -115.8857 | 4.7093 | 22.5892 | 0.0003 | 0.0125 |
| 2024_09_20 22:00 | 3250318 | 11 | 8.5545 | 11.3445 | -117.8585 | 4.6124 | 26.0974 | 0.0083 | 0.0058 |
| 2024_09_20 22:00 | 3252257 | 12 | 6.1412 | 8.4977 | -117.0306 | 4.9387 | 38.3614 | 0.0122 | 0.0132 |
| 2024_09_20 22:00 | 3267778 | 13 | 7.5775 | 5.7901 | -114.0455 | 4.1263 | 41.9378 | 0.0035 | 0.0094 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412353_9C65258A | 504990 | 293 | -93.3 | 504990 | 753 | -96.3 | 504990 | 251 | -101.7 | 504990 | 667 |
| MR_1774412353_A51AD12C | 504990 | 293 | -94.6 | 504990 | 753 | -93.7 | 504990 | 251 | -101.0 | 504990 | 667 |
| MR_1774412353_8F773A3D | 504990 | 293 | -94.9 | 504990 | 753 | -94.8 | 504990 | 251 | -100.2 | 504990 | 667 |
| MR_1774412353_1F7D278E | 152650 | 722 | -96.4 | 152650 | 19 | -99.3 | 152650 | 674 | -107.9 | 152650 | 787 |
| MR_1774412353_ADBD4152 | 504990 | 293 | -97.0 | 504990 | 753 | -96.0 | 504990 | 251 | -101.9 | 504990 | 667 |
| MR_1774412353_31554A28 | 504990 | 293 | -95.1 | 504990 | 753 | -95.0 | 504990 | 251 | -101.4 | 504990 | 667 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 362: `21be2d5e-b39...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `21be2d5e-b394-4e4a-b445-9b6cb8f2865c` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[362] topology](images/test_0362.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3241343_1
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3254642_4
- `C3`: Adjust the azimuth of 3241343_1 by 50 degrees
- `C4`: Decrease transmission power for 3254642_4
- `C5`: Press down the tilt angle of 3241343_1 by 7 degrees
- `C6`: Lift the tilt angle of 3241343_1 by 7 degrees
- `C7`: Increase transmission power for 3241343_1
- `C8`: Decrease A3 Offset threshold for 3254642_4
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3254642_4
- `C10`: Adjust the azimuth of 3254642_4 by 50 degrees
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3241343_1
- `C12`: Check test server and transmission issues
- `C13`: Press down the tilt angle  of 3254642_4 by 10 degrees
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Increase A3 Offset threshold for 3254642_4
- `C16`: Increase A3 Offset threshold for 3241343_1
- `C17`: Add neighbor relationship between 3271877_3 and 3254642_4
- `C18`: Add neighbor relationship between 3241343_1 and 3254642_4
- `C19`: Lift the tilt angle  of 3254642_4 by 10 degrees
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3241343_1
- `C21`: Increase transmission power for 3254642_4
- `C22`: Decrease transmission power for 3241343_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.727 | MS1 | 121.4656750772 | 31.1446347837 | 841 | 504990 | -86.75 | 16.37 | 457.27 | 0.11 | 2.90 | 1592 |
| 2024-09-20 22:21:32.193 | MS1 | 121.4656596527 | 31.1446289778 | 841 | 504990 | -87.55 | 17.26 | 440.39 | 0.07 | 2.25 | 1565 |
| 2024-09-20 22:21:33.146 | MS1 | 121.4656758062 | 31.1446338684 | 841 | 504990 | -90.53 | 14.80 | 341.71 | 0.17 | 2.50 | 1566 |
| 2024-09-20 22:21:34.727 | MS1 | 121.4656648698 | 31.1446310449 | 841 | 504990 | -86.97 | 15.02 | 78.67 | 0.08 | 2.33 | 1585 |
| 2024-09-20 22:21:35.386 | MS1 | 121.4656639814 | 31.1446230789 | 841 | 504990 | -91.60 | 16.45 | 87.27 | 0.08 | 2.25 | 1567 |
| 2024-09-20 22:21:36.777 | MS1 | 121.4656676426 | 31.1446316783 | 841 | 504990 | -85.37 | 17.78 | 85.65 | 0.17 | 2.19 | 1574 |
| 2024-09-20 22:21:37.476 | MS1 | 121.4656692961 | 31.1446346925 | 841 | 504990 | -90.46 | 10.03 | 81.40 | 0.01 | 2.90 | 1574 |
| 2024-09-20 22:21:38.439 | MS1 | 121.4656722828 | 31.1446346209 | 841 | 504990 | -90.44 | 9.48 | 78.62 | 0.07 | 2.62 | 1571 |
| 2024-09-20 22:21:39.845 | MS1 | 121.4656736060 | 31.1446236456 | 841 | 504990 | -92.90 | 8.36 | 79.41 | 0.04 | 2.71 | 1575 |
| 2024-09-20 22:21:40.345 | MS1 | 121.4656779299 | 31.1446298039 | 841 | 504990 | -89.75 | 11.15 | 570.68 | 0.18 | 2.99 | 1579 |
| 2024-09-20 22:21:41.403 | MS1 | 121.4656684319 | 31.1446276738 | 841 | 504990 | -92.16 | 9.28 | 527.63 | 0.12 | 2.36 | 1580 |
| 2024-09-20 22:21:42.262 | MS1 | 121.4656645720 | 31.1446182102 | 841 | 504990 | -93.43 | 12.87 | 449.02 | 0.08 | 2.06 | 1599 |

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
| 3241343 | 1 | 121.4759799199 | 31.1550732657 | 27 | 6 | 4 | 32.5 | TDD | 841 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3254642 | 4 | 121.4658099475 | 31.1559654089 | 127 | 10 | 0 | 15.4 | TDD | 925 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3271877 | 3 | 121.4649573375 | 31.1532380215 | 307 | 15 | 0 | 41.6 | TDD | 781 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3277588 | 2 | 121.4739508980 | 31.1499202490 | 26 | 11 | 10 | 23.0 | TDD | 581 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:30.873 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.892 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:30.996 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.996 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.759 | NREventA3 | measId:2;ServCellPCI:359;Se... |
| 2024-09-20 22:21:37.999 | NRHandoverAttempt | SourcePCI:359;SourceNR-ARFC... |
| 2024-09-20 22:21:38.041 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.055 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.157 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.157 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3241343 | 1 | 89.6910 | 79.9186 | -114.6749 | 7.0464 | 100.0652 | 0.0027 | 0.0013 |
| 2024_09_19 22:00 | 3277588 | 2 | 85.6652 | 86.6623 | -114.0914 | 6.5834 | 152.1391 | 0.0190 | 0.0174 |
| 2024_09_19 22:00 | 3271877 | 3 | 84.1683 | 93.1338 | -117.0248 | 8.5913 | 104.5745 | 0.0101 | 0.0124 |
| 2024_09_19 22:00 | 3254642 | 4 | 82.6026 | 80.6879 | -114.3243 | 11.8141 | 180.4009 | 0.0064 | 0.0038 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413329_92B1AA41 | 504990 | 841 | -88.8 | 504990 | 925 | -89.1 | 504990 | 781 | -96.4 | 504990 | 581 |
| MR_1774413329_A98852DE | 504990 | 841 | -85.1 | 504990 | 925 | -88.9 | 504990 | 781 | -96.8 | 504990 | 581 |
| MR_1774413329_C7619B1D | 504990 | 841 | -88.4 | 504990 | 925 | -89.2 | 504990 | 781 | -94.6 | 504990 | 581 |
| MR_1774413329_34C6753B | 504990 | 841 | -88.9 | 504990 | 925 | -88.8 | 504990 | 781 | -97.3 | 504990 | 581 |
| MR_1774413329_177B4C97 | 504990 | 841 | -86.7 | 504990 | 925 | -89.3 | 504990 | 781 | -96.9 | 504990 | 581 |
| MR_1774413329_EF092E1B | 504990 | 841 | -85.9 | 504990 | 925 | -87.1 | 504990 | 781 | -95.4 | 504990 | 581 |
| MR_1774413329_B049EFB4 | 504990 | 841 | -88.9 | 504990 | 925 | -86.3 | 504990 | 781 | -94.3 | 504990 | 581 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 363: `41ceeb25-c8d...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `41ceeb25-c8d1-4826-9be5-fd8e05fe5567` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[363] topology](images/test_0363.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3212341_4
- `C2`: Add neighbor relationship between 3212341_4 and 3259859_2
- `C3`: Decrease transmission power for 3259859_2
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3259859_2
- `C5`: Increase A3 Offset threshold for 3259859_2
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3259859_2
- `C7`: Insufficient data; more data is needed for judgment.
- `C8`: Adjust the azimuth of 3259859_2 by 50 degrees
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3212341_4
- `C10`: Decrease A3 Offset threshold for 3259859_2
- `C11`: Increase transmission power for 3212341_4
- `C12`: Lift the tilt angle of 3212341_4 by 10 degrees
- `C13`: Add neighbor relationship between 3278353_1 and 3259859_2
- `C14`: Increase A3 Offset threshold for 3212341_4
- `C15`: Press down the tilt angle  of 3259859_2 by 8 degrees
- `C16`: Press down the tilt angle of 3212341_4 by 10 degrees
- `C17`: Adjust the azimuth of 3212341_4 by 50 degrees
- `C18`: Check test server and transmission issues
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3212341_4
- `C20`: Lift the tilt angle  of 3259859_2 by 8 degrees
- `C21`: Increase transmission power for 3259859_2
- `C22`: Decrease transmission power for 3212341_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.163 | MS1 | 121.4656663278 | 31.1446367502 | 428 | 504990 | -88.76 | 14.84 | 348.88 | 0.12 | 2.38 | 1565 |
| 2024-09-20 22:21:32.372 | MS1 | 121.4656646019 | 31.1446215724 | 428 | 504990 | -85.18 | 14.96 | 445.98 | 0.14 | 2.46 | 1578 |
| 2024-09-20 22:21:33.707 | MS1 | 121.4656716017 | 31.1446351731 | 428 | 504990 | -89.67 | 16.59 | 308.13 | 0.17 | 2.15 | 1580 |
| 2024-09-20 22:21:34.151 | MS1 | 121.4656669495 | 31.1446260429 | 428 | 504990 | -88.49 | 13.00 | 86.63 | 0.17 | 2.96 | 1597 |
| 2024-09-20 22:21:35.760 | MS1 | 121.4656677741 | 31.1446221982 | 428 | 504990 | -87.17 | 16.28 | 84.17 | 0.01 | 2.47 | 1575 |
| 2024-09-20 22:21:36.848 | MS1 | 121.4656661849 | 31.1446186668 | 428 | 504990 | -90.59 | 16.53 | 75.55 | 0.05 | 2.35 | 1599 |
| 2024-09-20 22:21:37.664 | MS1 | 121.4656582076 | 31.1446306896 | 428 | 504990 | -90.33 | 8.07 | 62.86 | 0.02 | 2.18 | 1588 |
| 2024-09-20 22:21:38.763 | MS1 | 121.4656678100 | 31.1446374909 | 428 | 504990 | -90.39 | 7.79 | 78.05 | 0.12 | 2.27 | 1593 |
| 2024-09-20 22:21:39.701 | MS1 | 121.4656583516 | 31.1446351623 | 428 | 504990 | -93.82 | 7.18 | 69.70 | 0.06 | 2.27 | 1567 |
| 2024-09-20 22:21:40.691 | MS1 | 121.4656647754 | 31.1446277558 | 428 | 504990 | -90.96 | 8.13 | 511.39 | 0.18 | 2.14 | 1594 |
| 2024-09-20 22:21:41.987 | MS1 | 121.4656618488 | 31.1446222816 | 428 | 504990 | -90.78 | 10.38 | 306.19 | 0.15 | 2.50 | 1584 |
| 2024-09-20 22:21:42.984 | MS1 | 121.4656597636 | 31.1446322004 | 428 | 504990 | -92.97 | 9.35 | 586.23 | 0.12 | 2.82 | 1567 |

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
| 3212341 | 4 | 121.4708056504 | 31.1455658633 | 98 | 10 | 6 | 17.3 | TDD | 428 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3259859 | 2 | 121.4681248684 | 31.1464388145 | 328 | 2 | 7 | 32.1 | TDD | 626 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3265191 | 3 | 121.4736947028 | 31.1505861781 | 199 | 5 | 2 | 27.3 | TDD | 347 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3278353 | 1 | 121.4686085164 | 31.1507601833 | 113 | 11 | 11 | 16.9 | TDD | 520 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:31.300 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.319 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.450 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.450 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.136 | NREventA3 | measId:2;ServCellPCI:326;Se... |
| 2024-09-20 22:21:38.376 | NRHandoverAttempt | SourcePCI:326;SourceNR-ARFC... |
| 2024-09-20 22:21:38.406 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.420 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.554 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.554 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3278353 | 1 | 94.0150 | 80.0480 | -117.9076 | 12.5271 | 178.5997 | 0.0152 | 0.0054 |
| 2024_09_19 22:00 | 3259859 | 2 | 88.9220 | 77.3592 | -116.3720 | 14.0346 | 177.5583 | 0.0116 | 0.0119 |
| 2024_09_19 22:00 | 3265191 | 3 | 81.3171 | 77.9490 | -114.6137 | 9.0291 | 126.5178 | 0.0093 | 0.0139 |
| 2024_09_19 22:00 | 3212341 | 4 | 76.2551 | 82.8511 | -116.5045 | 10.6152 | 138.0335 | 0.0128 | 0.0058 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412263_77946EB4 | 504990 | 428 | -87.5 | 504990 | 626 | -94.0 | 504990 | 520 | -96.5 | 504990 | 347 |
| MR_1774412263_F503CD8B | 504990 | 428 | -88.4 | 504990 | 626 | -90.2 | 504990 | 520 | -97.6 | 504990 | 347 |
| MR_1774412263_7D9AEAB6 | 504990 | 428 | -87.9 | 504990 | 626 | -94.0 | 504990 | 520 | -98.6 | 504990 | 347 |
| MR_1774412263_36D19886 | 504990 | 428 | -87.3 | 504990 | 626 | -90.8 | 504990 | 520 | -97.8 | 504990 | 347 |
| MR_1774412263_3A165CB6 | 504990 | 428 | -89.6 | 504990 | 626 | -90.4 | 504990 | 520 | -100.0 | 504990 | 347 |
| MR_1774412263_E96436A5 | 504990 | 428 | -86.9 | 504990 | 626 | -93.1 | 504990 | 520 | -99.6 | 504990 | 347 |
| MR_1774412263_F4826810 | 504990 | 428 | -90.2 | 504990 | 626 | -91.3 | 504990 | 520 | -100.0 | 504990 | 347 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 364: `2d1e7246-b1c...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `2d1e7246-b1cf-4f23-bc36-9113b4ee09c3` |
| Tag | **multiple-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[364] topology](images/test_0364.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3232788_4
- `C2`: Decrease A3 Offset threshold for 3262174_1
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3232788_4
- `C4`: Adjust the azimuth of 3232788_4 by 4 degrees
- `C5`: Decrease transmission power for 3262174_1
- `C6`: Press down the tilt angle of 3262174_1 by 10 degrees
- `C7`: Adjust the azimuth of 3262174_1 by 25 degrees
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3262174_1
- `C9`: Insufficient data; more data is needed for judgment.
- `C10`: Decrease transmission power for 3232788_4
- `C11`: Add neighbor relationship between 3223525_2 and 3232788_4
- `C12`: Check test server and transmission issues
- `C13`: Increase transmission power for 3232788_4
- `C14`: Lift the tilt angle of 3262174_1 by 10 degrees
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3232788_4
- `C16`: Decrease A3 Offset threshold for 3232788_4
- `C17`: Increase A3 Offset threshold for 3262174_1
- `C18`: Add neighbor relationship between 3262174_1 and 3232788_4
- `C19`: Lift the tilt angle  of 3232788_4 by 2 degrees
- `C20`: Press down the tilt angle  of 3232788_4 by 2 degrees
- `C21`: Increase transmission power for 3262174_1
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3262174_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.633 | MS1 | 121.4656706904 | 31.1446278962 | 304 | 504990 | -94.78 | 13.10 | 456.06 | 0.15 | 2.36 | 1575 |
| 2024-09-20 22:21:32.900 | MS1 | 121.4656779920 | 31.1446211393 | 304 | 504990 | -92.44 | 12.21 | 569.23 | 0.18 | 2.73 | 1577 |
| 2024-09-20 22:21:33.896 | MS1 | 121.4656741271 | 31.1446308453 | 304 | 504990 | -89.86 | 13.65 | 507.62 | 0.13 | 2.67 | 1597 |
| 2024-09-20 22:21:34.281 | MS1 | 121.4656635194 | 31.1446226037 | 304 | 504990 | -105.42 | -1.84 | 73.73 | 0.10 | 1.15 | 1594 |
| 2024-09-20 22:21:35.717 | MS1 | 121.4656721342 | 31.1446278065 | 304 | 504990 | -100.13 | -1.82 | 36.23 | 0.06 | 1.01 | 1560 |
| 2024-09-20 22:21:36.587 | MS1 | 121.4656731661 | 31.1446273743 | 304 | 504990 | -105.33 | 0.62 | 72.41 | 0.12 | 1.47 | 1573 |
| 2024-09-20 22:21:37.527 | MS1 | 121.4656635860 | 31.1446261914 | 304 | 504990 | -103.44 | 0.17 | 43.88 | 0.01 | 1.38 | 1597 |
| 2024-09-20 22:21:38.950 | MS1 | 121.4656757251 | 31.1446214481 | 304 | 504990 | -108.88 | 0.65 | 24.80 | 0.01 | 1.16 | 1589 |
| 2024-09-20 22:21:39.726 | MS1 | 121.4656733586 | 31.1446290678 | 304 | 504990 | -108.79 | 1.03 | 67.00 | 0.09 | 1.02 | 1598 |
| 2024-09-20 22:21:40.328 | MS1 | 121.4656719466 | 31.1446366463 | 304 | 504990 | -92.15 | 14.53 | 513.48 | 0.19 | 2.55 | 1576 |
| 2024-09-20 22:21:41.757 | MS1 | 121.4656744508 | 31.1446197799 | 304 | 504990 | -87.88 | 17.95 | 447.00 | 0.01 | 2.25 | 1587 |
| 2024-09-20 22:21:42.235 | MS1 | 121.4656725237 | 31.1446325871 | 304 | 504990 | -85.41 | 13.16 | 506.93 | 0.09 | 2.57 | 1573 |

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
| 3222997 | 3 | 121.4658108486 | 31.1473100473 | 214 | 7 | 4 | 31.8 | TDD | 869 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3223525 | 2 | 121.4728538301 | 31.1492057237 | 46 | 14 | 4 | 26.3 | TDD | 844 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3232788 | 4 | 121.4746014459 | 31.1557911104 | 210 | 1 | 5 | 39.1 | TDD | 751 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3262174 | 1 | 121.4671240724 | 31.1471998334 | 231 | 13 | 1 | 16.1 | TDD | 304 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |

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
| 2024-09-20 22:21:30.762 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.783 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:30.895 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.895 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.133 | NREventA2 | measId:1;ServCellPCI:384;Se... |
| 2024-09-20 22:21:34.263 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3262174 | 1 | 5.7687 | 5.5306 | -116.2844 | 19.3253 | 139.1716 | 0.1530 | 0.0116 |
| 2024_09_20 22:00 | 3223525 | 2 | 19.7493 | 7.3913 | -117.1178 | 7.4054 | 111.5106 | 0.0170 | 0.0087 |
| 2024_09_20 22:00 | 3222997 | 3 | 9.4889 | 5.1644 | -115.3918 | 5.0674 | 119.3709 | 0.0123 | 0.0003 |
| 2024_09_20 22:00 | 3232788 | 4 | 12.6446 | 13.4620 | -114.8192 | 17.2969 | 152.3309 | 0.0034 | 0.0031 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415468_3FFDB5B1 | 504990 | 304 | -106.2 | 504990 | 751 | -110.3 | 504990 | 844 | -115.1 | 504990 | 869 |
| MR_1774415468_05B65EDF | 504990 | 304 | -106.5 | 504990 | 751 | -110.2 | 504990 | 844 | -116.5 | 504990 | 869 |
| MR_1774415468_79E2963D | 504990 | 304 | -104.7 | 504990 | 751 | -110.3 | 504990 | 844 | -118.6 | 504990 | 869 |
| MR_1774415468_DBF2A4CA | 504990 | 304 | -104.6 | 504990 | 751 | -110.1 | 504990 | 844 | -118.7 | 504990 | 869 |
| MR_1774415468_158461B6 | 504990 | 304 | -106.8 | 504990 | 751 | -110.8 | 504990 | 844 | -115.3 | 504990 | 869 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 365: `41f61b30-e7a...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `41f61b30-e7a5-4824-9a3b-e54bcc194e19` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[365] topology](images/test_0365.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3258315_2 by 10 degrees
- `C2`: Press down the tilt angle  of 3236723_3 by 10 degrees
- `C3`: Decrease transmission power for 3258315_2
- `C4`: Press down the tilt angle of 3258315_2 by 10 degrees
- `C5`: Increase transmission power for 3236723_3
- `C6`: Insufficient data; more data is needed for judgment.
- `C7`: Adjust the azimuth of 3258315_2 by 50 degrees
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3236723_3
- `C9`: Decrease A3 Offset threshold for 3236723_3
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3236723_3
- `C11`: Adjust the azimuth of 3236723_3 by 50 degrees
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3258315_2
- `C13`: Check test server and transmission issues
- `C14`: Increase A3 Offset threshold for 3236723_3
- `C15`: Add neighbor relationship between 3265903_1 and 3236723_3
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3258315_2
- `C17`: Decrease A3 Offset threshold for 3258315_2
- `C18`: Decrease transmission power for 3236723_3
- `C19`: Increase A3 Offset threshold for 3258315_2
- `C20`: Lift the tilt angle  of 3236723_3 by 10 degrees
- `C21`: Increase transmission power for 3258315_2
- `C22`: Add neighbor relationship between 3258315_2 and 3236723_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.946 | MS1 | 121.4656754166 | 31.1446354807 | 546 | 504990 | -86.74 | 17.47 | 389.89 | 0.20 | 2.13 | 1577 |
| 2024-09-20 22:21:32.379 | MS1 | 121.4656591282 | 31.1446265384 | 546 | 504990 | -86.55 | 14.03 | 341.42 | 0.18 | 2.74 | 1577 |
| 2024-09-20 22:21:33.584 | MS1 | 121.4656712485 | 31.1446271638 | 546 | 504990 | -91.83 | 12.13 | 589.27 | 0.09 | 2.67 | 1577 |
| 2024-09-20 22:21:34.940 | MS1 | 121.4656702464 | 31.1446276170 | 546 | 504990 | -90.91 | 17.78 | 55.76 | 0.02 | 2.42 | 425 |
| 2024-09-20 22:21:35.848 | MS1 | 121.4656777095 | 31.1446289878 | 546 | 504990 | -87.48 | 13.58 | 99.69 | 0.14 | 2.08 | 322 |
| 2024-09-20 22:21:36.364 | MS1 | 121.4656596921 | 31.1446183284 | 546 | 504990 | -87.84 | 16.01 | 50.94 | 0.14 | 2.76 | 444 |
| 2024-09-20 22:21:37.504 | MS1 | 121.4656751556 | 31.1446291930 | 546 | 504990 | -90.39 | 11.85 | 72.49 | 0.01 | 2.48 | 375 |
| 2024-09-20 22:21:38.723 | MS1 | 121.4656729882 | 31.1446306326 | 546 | 504990 | -89.93 | 8.10 | 85.11 | 0.15 | 2.26 | 435 |
| 2024-09-20 22:21:39.523 | MS1 | 121.4656582478 | 31.1446283625 | 546 | 504990 | -89.01 | 11.26 | 82.99 | 0.19 | 2.57 | 477 |
| 2024-09-20 22:21:40.266 | MS1 | 121.4656689641 | 31.1446281140 | 546 | 504990 | -92.77 | 7.55 | 330.07 | 0.04 | 2.97 | 1575 |
| 2024-09-20 22:21:41.916 | MS1 | 121.4656635874 | 31.1446297391 | 546 | 504990 | -91.35 | 10.93 | 542.72 | 0.18 | 2.31 | 1576 |
| 2024-09-20 22:21:42.853 | MS1 | 121.4656635541 | 31.1446337407 | 546 | 504990 | -90.39 | 7.10 | 514.36 | 0.12 | 2.78 | 1565 |

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
| 3232296 | 4 | 121.4710509109 | 31.1499340979 | 21 | 13 | 4 | 47.2 | TDD | 55 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3236723 | 3 | 121.4645633068 | 31.1531422357 | 95 | 9 | 3 | 18.6 | TDD | 461 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3258315 | 2 | 121.4747907674 | 31.1554479035 | 144 | 10 | 11 | 37.0 | TDD | 546 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3265903 | 1 | 121.4647712906 | 31.1496638350 | 39 | 5 | 10 | 28.7 | TDD | 88 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:31.300 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.318 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.458 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.458 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.126 | NREventA3 | measId:2;ServCellPCI:692;Se... |
| 2024-09-20 22:21:38.366 | NRHandoverAttempt | SourcePCI:692;SourceNR-ARFC... |
| 2024-09-20 22:21:38.412 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.427 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.563 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.563 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3265903 | 1 | 17.7213 | 12.1084 | -117.6633 | 17.9250 | 157.4767 | 0.0007 | 0.0044 |
| 2024_09_20 22:00 | 3258315 | 2 | 18.6756 | 8.9819 | -116.1939 | 11.1673 | 171.9053 | 0.0101 | 0.0157 |
| 2024_09_20 22:00 | 3236723 | 3 | 19.9860 | 10.8314 | -117.7685 | 13.4172 | 166.3794 | 0.0143 | 0.0165 |
| 2024_09_20 22:00 | 3232296 | 4 | 5.6949 | 15.2098 | -117.9146 | 19.1219 | 95.3280 | 0.0039 | 0.0095 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414521_A71857C5 | 504990 | 546 | -92.6 | 504990 | 461 | -92.0 | 504990 | 88 | -98.8 | 504990 | 55 |
| MR_1774414521_2430407D | 504990 | 546 | -90.4 | 504990 | 461 | -91.9 | 504990 | 88 | -101.7 | 504990 | 55 |
| MR_1774414521_BFC0F1FF | 504990 | 546 | -92.4 | 504990 | 461 | -92.3 | 504990 | 88 | -100.5 | 504990 | 55 |
| MR_1774414521_3280B93F | 504990 | 546 | -92.1 | 504990 | 461 | -89.8 | 504990 | 88 | -98.4 | 504990 | 55 |
| MR_1774414521_2A411E58 | 504990 | 546 | -92.0 | 504990 | 461 | -91.3 | 504990 | 88 | -98.0 | 504990 | 55 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 366: `fa81d4d7-44b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `fa81d4d7-44b9-4431-b229-60c6fb71d723` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[366] topology](images/test_0366.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3236155_2
- `C2`: Increase transmission power for 3236155_2
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3262383_4
- `C4`: Adjust the azimuth of 3236155_2 by 50 degrees
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3262383_4
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3236155_2
- `C7`: Increase transmission power for 3262383_4
- `C8`: Press down the tilt angle  of 3262383_4 by 7 degrees
- `C9`: Decrease A3 Offset threshold for 3262383_4
- `C10`: Add neighbor relationship between 3230457_1 and 3262383_4
- `C11`: Decrease transmission power for 3262383_4
- `C12`: Adjust the azimuth of 3262383_4 by 32 degrees
- `C13`: Decrease A3 Offset threshold for 3236155_2
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Add neighbor relationship between 3236155_2 and 3262383_4
- `C16`: Lift the tilt angle of 3236155_2 by 5 degrees
- `C17`: Increase A3 Offset threshold for 3236155_2
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3236155_2
- `C19`: Press down the tilt angle of 3236155_2 by 5 degrees
- `C20`: Check test server and transmission issues
- `C21`: Lift the tilt angle  of 3262383_4 by 7 degrees
- `C22`: Increase A3 Offset threshold for 3262383_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.981 | MS1 | 121.4656614937 | 31.1446293170 | 867 | 504990 | -78.26 | 16.67 | 564.11 | 0.17 | 2.92 | 1600 |
| 2024-09-20 22:21:32.482 | MS1 | 121.4656689799 | 31.1446273889 | 867 | 504990 | -83.54 | 12.44 | 430.90 | 0.16 | 2.48 | 1591 |
| 2024-09-20 22:21:33.128 | MS1 | 121.4656655216 | 31.1446371529 | 867 | 504990 | -80.83 | 14.18 | 535.88 | 0.17 | 2.97 | 1579 |
| 2024-09-20 22:21:34.905 | MS1 | 121.4656686906 | 31.1446369345 | 867 | 504990 | -86.10 | -1.62 | 50.43 | 0.19 | 1.50 | 1586 |
| 2024-09-20 22:21:35.320 | MS1 | 121.4656636257 | 31.1446198285 | 867 | 504990 | -90.64 | -3.20 | 39.83 | 0.12 | 1.12 | 1600 |
| 2024-09-20 22:21:36.341 | MS1 | 121.4656594750 | 31.1446337124 | 867 | 504990 | -88.75 | -0.94 | 65.04 | 0.13 | 1.46 | 1575 |
| 2024-09-20 22:21:37.914 | MS1 | 121.4656778331 | 31.1446231022 | 867 | 504990 | -87.07 | -3.27 | 71.99 | 0.04 | 1.25 | 1572 |
| 2024-09-20 22:21:38.583 | MS1 | 121.4656641578 | 31.1446340917 | 867 | 504990 | -90.45 | -3.04 | 43.00 | 0.01 | 1.13 | 1563 |
| 2024-09-20 22:21:39.466 | MS1 | 121.4656600069 | 31.1446182401 | 367 | 504990 | -84.54 | 17.00 | 155.16 | 0.01 | 1.02 | 1594 |
| 2024-09-20 22:21:40.442 | MS1 | 121.4656580719 | 31.1446228730 | 367 | 504990 | -82.82 | 15.64 | 307.01 | 0.10 | 2.05 | 1581 |
| 2024-09-20 22:21:41.180 | MS1 | 121.4656612989 | 31.1446330326 | 367 | 504990 | -77.19 | 12.19 | 441.89 | 0.12 | 2.46 | 1584 |
| 2024-09-20 22:21:42.295 | MS1 | 121.4656603602 | 31.1446316240 | 367 | 504990 | -81.70 | 17.30 | 582.68 | 0.13 | 2.24 | 1566 |

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
| 3230457 | 1 | 121.4661581071 | 31.1479677453 | 43 | 4 | 5 | 28.3 | TDD | 280 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3236155 | 2 | 121.4721331200 | 31.1545857136 | 269 | 4 | 0 | 20.6 | TDD | 867 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3262383 | 4 | 121.4677984681 | 31.1481098568 | 240 | 3 | 9 | 30.4 | TDD | 367 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3275219 | 3 | 121.4724000872 | 31.1443780753 | 123 | 6 | 11 | 23.6 | TDD | 104 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |

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
| 2024-09-20 22:21:31.371 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.390 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.510 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.510 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.189 | NREventA3 | measId:2;ServCellPCI:648;Se... |
| 2024-09-20 22:21:38.429 | NRHandoverAttempt | SourcePCI:648;SourceNR-ARFC... |
| 2024-09-20 22:21:38.471 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.485 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.608 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.608 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3230457 | 1 | 11.5006 | 16.6946 | -116.2424 | 7.6478 | 158.0611 | 0.0056 | 0.0167 |
| 2024_09_20 22:00 | 3236155 | 2 | 19.3487 | 14.6182 | -115.9864 | 6.2136 | 105.9132 | 0.0015 | 0.1267 |
| 2024_09_20 22:00 | 3275219 | 3 | 13.2918 | 9.1091 | -114.8229 | 10.1684 | 180.6356 | 0.0001 | 0.0166 |
| 2024_09_20 22:00 | 3262383 | 4 | 6.9040 | 12.8333 | -115.1545 | 6.0931 | 186.0361 | 0.0149 | 0.0169 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412812_7F97F99A | 504990 | 367 | -79.4 | 504990 | 867 | -87.5 | 504990 | 280 | -83.9 | 504990 | 104 |
| MR_1774412812_113413D4 | 504990 | 367 | -82.0 | 504990 | 867 | -84.8 | 504990 | 280 | -87.4 | 504990 | 104 |
| MR_1774412812_2F39B57A | 504990 | 867 | -86.4 | 504990 | 367 | -79.5 | 504990 | 280 | -84.2 | 504990 | 104 |
| MR_1774412812_13378439 | 504990 | 367 | -81.2 | 504990 | 867 | -85.0 | 504990 | 280 | -85.2 | 504990 | 104 |
| MR_1774412812_A42978A3 | 504990 | 367 | -83.0 | 504990 | 867 | -84.1 | 504990 | 280 | -86.9 | 504990 | 104 |
| MR_1774412812_6AF78C85 | 504990 | 367 | -81.9 | 504990 | 867 | -84.3 | 504990 | 280 | -84.7 | 504990 | 104 |
| MR_1774412812_63471D79 | 504990 | 867 | -85.2 | 504990 | 367 | -81.2 | 504990 | 280 | -86.6 | 504990 | 104 |
| MR_1774412812_44801D50 | 504990 | 367 | -79.4 | 504990 | 867 | -87.7 | 504990 | 280 | -87.6 | 504990 | 104 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 367: `0e12307c-6cd...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `0e12307c-6cdd-4842-a5fd-a8e4ce89a3be` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[367] topology](images/test_0367.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3233807_1
- `C2`: Add neighbor relationship between 3278696_2 and 3213011_4
- `C3`: Increase transmission power for 3213011_4
- `C4`: Insufficient data; more data is needed for judgment.
- `C5`: Adjust the azimuth of 3233807_1 by 33 degrees
- `C6`: Press down the tilt angle  of 3213011_4 by 2 degrees
- `C7`: Increase A3 Offset threshold for 3213011_4
- `C8`: Increase A3 Offset threshold for 3233807_1
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3213011_4
- `C10`: Add neighbor relationship between 3233807_1 and 3213011_4
- `C11`: Decrease A3 Offset threshold for 3213011_4
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3213011_4
- `C13`: Decrease A3 Offset threshold for 3233807_1
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3233807_1
- `C15`: Decrease transmission power for 3213011_4
- `C16`: Lift the tilt angle  of 3213011_4 by 2 degrees
- `C17`: Press down the tilt angle of 3233807_1 by 10 degrees
- `C18`: Increase transmission power for 3233807_1
- `C19`: Check test server and transmission issues
- `C20`: Adjust the azimuth of 3213011_4 by 36 degrees
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3233807_1
- `C22`: Lift the tilt angle of 3233807_1 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.330 | MS1 | 121.4656778043 | 31.1446230622 | 632 | 504990 | -80.31 | 16.76 | 589.51 | 0.19 | 2.85 | 1578 |
| 2024-09-20 22:21:32.811 | MS1 | 121.4656631918 | 31.1446317835 | 632 | 504990 | -75.13 | 16.90 | 484.59 | 0.05 | 2.99 | 1572 |
| 2024-09-20 22:21:33.147 | MS1 | 121.4656672861 | 31.1446367927 | 632 | 504990 | -78.03 | 14.08 | 458.68 | 0.15 | 2.60 | 1587 |
| 2024-09-20 22:21:34.627 | MS1 | 121.4656738158 | 31.1446329810 | 632 | 504990 | -87.69 | -0.83 | 57.56 | 0.00 | 1.20 | 1572 |
| 2024-09-20 22:21:35.697 | MS1 | 121.4656585586 | 31.1446236608 | 632 | 504990 | -90.83 | -0.36 | 44.70 | 0.05 | 1.02 | 1580 |
| 2024-09-20 22:21:36.267 | MS1 | 121.4656714756 | 31.1446272385 | 632 | 504990 | -89.53 | -2.25 | 46.84 | 0.09 | 1.26 | 1566 |
| 2024-09-20 22:21:37.541 | MS1 | 121.4656739692 | 31.1446333330 | 632 | 504990 | -91.03 | -1.04 | 57.25 | 0.01 | 1.39 | 1583 |
| 2024-09-20 22:21:38.248 | MS1 | 121.4656692134 | 31.1446290515 | 632 | 504990 | -76.46 | 16.71 | 370.55 | 0.08 | 1.16 | 1562 |
| 2024-09-20 22:21:39.220 | MS1 | 121.4656694691 | 31.1446217615 | 632 | 504990 | -83.59 | 16.86 | 394.22 | 0.18 | 1.05 | 1600 |
| 2024-09-20 22:21:40.480 | MS1 | 121.4656661962 | 31.1446336742 | 632 | 504990 | -82.24 | 12.79 | 540.31 | 0.11 | 2.42 | 1579 |
| 2024-09-20 22:21:41.187 | MS1 | 121.4656712699 | 31.1446209820 | 632 | 504990 | -80.03 | 16.39 | 344.35 | 0.11 | 2.20 | 1569 |
| 2024-09-20 22:21:42.275 | MS1 | 121.4656594009 | 31.1446295156 | 632 | 504990 | -78.31 | 15.14 | 324.09 | 0.19 | 2.43 | 1566 |

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
| 3213011 | 4 | 121.4733929864 | 31.1526886069 | 183 | 1 | 10 | 28.4 | TDD | 839 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3233807 | 1 | 121.4664617897 | 31.1542639713 | 151 | 10 | 9 | 49.5 | TDD | 632 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3234717 | 3 | 121.4720320552 | 31.1537398378 | 279 | 5 | 12 | 40.2 | TDD | 190 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3278696 | 2 | 121.4679507124 | 31.1472995832 | 240 | 2 | 10 | 48.5 | TDD | 677 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |

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
| 2024-09-20 22:21:31.224 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.245 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.391 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.391 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.082 | NREventA3 | measId:2;ServCellPCI:681;Se... |
| 2024-09-20 22:21:36.082 | NREventA3 | measId:2;ServCellPCI:681;Se... |
| 2024-09-20 22:21:37.082 | NREventA3 | measId:2;ServCellPCI:681;Se... |
| 2024-09-20 22:21:39.582 | NRRRCReestablishAttempt | PCI:681 |
| 2024-09-20 22:21:39.602 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.615 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:39.756 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.756 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3233807 | 1 | 15.0939 | 8.0448 | -117.6104 | 11.5346 | 122.5975 | 0.0195 | 0.1281 |
| 2024_09_20 22:00 | 3278696 | 2 | 15.2437 | 16.5118 | -116.0697 | 9.9842 | 176.8246 | 0.0096 | 0.0008 |
| 2024_09_20 22:00 | 3234717 | 3 | 9.9330 | 10.9344 | -115.3893 | 19.8517 | 192.0631 | 0.0048 | 0.0021 |
| 2024_09_20 22:00 | 3213011 | 4 | 16.9198 | 15.0789 | -115.1330 | 7.5225 | 139.2579 | 0.0058 | 0.0158 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416298_1D1C47AF | 504990 | 632 | -86.3 | 504990 | 839 | -84.2 | 504990 | 677 | -88.2 | 504990 | 190 |
| MR_1774416298_3F801E05 | 504990 | 839 | -83.0 | 504990 | 632 | -88.6 | 504990 | 677 | -90.6 | 504990 | 190 |
| MR_1774416298_22D46ED6 | 504990 | 632 | -88.2 | 504990 | 839 | -81.5 | 504990 | 677 | -87.1 | 504990 | 190 |
| MR_1774416298_555B33DB | 504990 | 839 | -84.6 | 504990 | 632 | -88.1 | 504990 | 677 | -88.3 | 504990 | 190 |
| MR_1774416298_03F101E9 | 504990 | 632 | -89.5 | 504990 | 839 | -85.1 | 504990 | 677 | -90.5 | 504990 | 190 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 368: `8928b6a6-174...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `8928b6a6-1748-4867-a93a-bee588505280` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[368] topology](images/test_0368.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3274280_1
- `C2`: Insufficient data; more data is needed for judgment.
- `C3`: Decrease transmission power for 3220956_2
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3220956_2
- `C5`: Lift the tilt angle of 3220956_2 by 3 degrees
- `C6`: Lift the tilt angle  of 3274280_1 by 10 degrees
- `C7`: Increase A3 Offset threshold for 3220956_2
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3220956_2
- `C9`: Press down the tilt angle  of 3274280_1 by 10 degrees
- `C10`: Increase transmission power for 3220956_2
- `C11`: Decrease transmission power for 3274280_1
- `C12`: Press down the tilt angle of 3220956_2 by 3 degrees
- `C13`: Check test server and transmission issues
- `C14`: Adjust the azimuth of 3220956_2 by 50 degrees
- `C15`: Decrease A3 Offset threshold for 3274280_1
- `C16`: Add neighbor relationship between 3276523_3 and 3274280_1
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3274280_1
- `C18`: Adjust the azimuth of 3274280_1 by 50 degrees
- `C19`: Add neighbor relationship between 3220956_2 and 3274280_1
- `C20`: Decrease A3 Offset threshold for 3220956_2
- `C21`: Increase transmission power for 3274280_1
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3274280_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.561 | MS1 | 121.4656679391 | 31.1446233267 | 850 | 504990 | -90.73 | 15.27 | 400.61 | 0.05 | 2.39 | 1576 |
| 2024-09-20 22:21:32.246 | MS1 | 121.4656583127 | 31.1446328134 | 850 | 504990 | -89.11 | 14.78 | 574.83 | 0.13 | 2.09 | 1569 |
| 2024-09-20 22:21:33.583 | MS1 | 121.4656706862 | 31.1446314679 | 850 | 504990 | -88.80 | 14.52 | 568.04 | 0.16 | 2.04 | 1567 |
| 2024-09-20 22:21:34.668 | MS1 | 121.4656649088 | 31.1446271225 | 850 | 504990 | -85.05 | 15.20 | 65.46 | 0.05 | 2.03 | 1568 |
| 2024-09-20 22:21:35.912 | MS1 | 121.4656646259 | 31.1446369083 | 850 | 504990 | -90.49 | 15.15 | 99.92 | 0.06 | 2.44 | 1590 |
| 2024-09-20 22:21:36.489 | MS1 | 121.4656769682 | 31.1446260442 | 850 | 504990 | -88.55 | 14.59 | 89.89 | 0.07 | 2.70 | 1598 |
| 2024-09-20 22:21:37.278 | MS1 | 121.4656590663 | 31.1446189397 | 850 | 504990 | -89.09 | 10.07 | 87.05 | 0.14 | 2.80 | 1571 |
| 2024-09-20 22:21:38.389 | MS1 | 121.4656614822 | 31.1446257148 | 850 | 504990 | -92.54 | 9.37 | 98.99 | 0.07 | 2.36 | 1563 |
| 2024-09-20 22:21:39.859 | MS1 | 121.4656694549 | 31.1446331023 | 850 | 504990 | -90.10 | 10.14 | 90.95 | 0.10 | 2.66 | 1582 |
| 2024-09-20 22:21:40.610 | MS1 | 121.4656699195 | 31.1446378970 | 850 | 504990 | -93.66 | 8.65 | 418.66 | 0.19 | 2.69 | 1588 |
| 2024-09-20 22:21:41.444 | MS1 | 121.4656741134 | 31.1446218849 | 850 | 504990 | -90.28 | 8.82 | 428.01 | 0.09 | 2.24 | 1570 |
| 2024-09-20 22:21:42.929 | MS1 | 121.4656714694 | 31.1446216605 | 850 | 504990 | -91.76 | 10.85 | 333.59 | 0.12 | 2.39 | 1599 |

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
| 3220956 | 2 | 121.4660473533 | 31.1558883144 | 281 | 1 | 6 | 39.2 | TDD | 850 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3274280 | 1 | 121.4677917346 | 31.1545541734 | 92 | 15 | 3 | 33.4 | TDD | 169 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3276523 | 3 | 121.4688369370 | 31.1488610910 | 58 | 2 | 5 | 33.5 | TDD | 851 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3279249 | 4 | 121.4701031604 | 31.1440109969 | 9 | 4 | 2 | 30.6 | TDD | 451 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |

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
| 2024-09-20 22:21:31.304 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.322 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.430 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.430 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.202 | NREventA3 | measId:2;ServCellPCI:587;Se... |
| 2024-09-20 22:21:38.442 | NRHandoverAttempt | SourcePCI:587;SourceNR-ARFC... |
| 2024-09-20 22:21:38.478 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.491 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.594 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.594 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3274280 | 1 | 84.6277 | 85.0467 | -115.7238 | 7.7575 | 195.7114 | 0.0157 | 0.0156 |
| 2024_09_19 22:00 | 3220956 | 2 | 87.8657 | 83.1251 | -115.0544 | 18.6394 | 82.5960 | 0.0066 | 0.0115 |
| 2024_09_19 22:00 | 3276523 | 3 | 88.6391 | 85.3743 | -117.8627 | 18.4409 | 160.3279 | 0.0033 | 0.0002 |
| 2024_09_19 22:00 | 3279249 | 4 | 91.2135 | 91.1728 | -114.0865 | 7.1489 | 158.9559 | 0.0015 | 0.0080 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417215_AFE981B8 | 504990 | 850 | -84.1 | 504990 | 169 | -92.9 | 504990 | 851 | -98.1 | 504990 | 451 |
| MR_1774417215_766729AB | 504990 | 850 | -85.6 | 504990 | 169 | -92.8 | 504990 | 851 | -100.2 | 504990 | 451 |
| MR_1774417215_C4B4D340 | 504990 | 850 | -86.3 | 504990 | 169 | -91.7 | 504990 | 851 | -98.2 | 504990 | 451 |
| MR_1774417215_2AA98D96 | 504990 | 850 | -83.4 | 504990 | 169 | -91.7 | 504990 | 851 | -99.9 | 504990 | 451 |
| MR_1774417215_EF216B3C | 504990 | 850 | -83.9 | 504990 | 169 | -90.2 | 504990 | 851 | -98.0 | 504990 | 451 |
| MR_1774417215_3604CB4E | 504990 | 850 | -86.3 | 504990 | 169 | -91.0 | 504990 | 851 | -98.2 | 504990 | 451 |
| MR_1774417215_DC0442F0 | 504990 | 850 | -85.5 | 504990 | 169 | -90.8 | 504990 | 851 | -97.7 | 504990 | 451 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 369: `1548ce1d-00f...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `1548ce1d-00fd-46f4-92ef-e9e2e5634b79` |
| Tag | **multiple-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[369] topology](images/test_0369.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3234649_2 by 4 degrees
- `C2`: Add neighbor relationship between 3221890_4 and 3234649_2
- `C3`: Decrease A3 Offset threshold for 3234649_2
- `C4`: Increase A3 Offset threshold for 3221890_4
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3234649_2
- `C6`: Add neighbor relationship between 3254764_1 and 3234649_2
- `C7`: Decrease transmission power for 3234649_2
- `C8`: Adjust the azimuth of 3221890_4 by 38 degrees
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3221890_4
- `C10`: Increase A3 Offset threshold for 3234649_2
- `C11`: Decrease A3 Offset threshold for 3221890_4
- `C12`: Lift the tilt angle of 3221890_4 by 2 degrees
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3221890_4
- `C14`: Adjust the azimuth of 3234649_2 by 17 degrees
- `C15`: Insufficient data; more data is needed for judgment.
- `C16`: Press down the tilt angle of 3221890_4 by 2 degrees
- `C17`: Check test server and transmission issues
- `C18`: Decrease transmission power for 3221890_4
- `C19`: Increase transmission power for 3221890_4
- `C20`: Lift the tilt angle  of 3234649_2 by 4 degrees
- `C21`: Increase transmission power for 3234649_2
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3234649_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.312 | MS1 | 121.4656735637 | 31.1446293936 | 7 | 504990 | -76.54 | 13.77 | 440.01 | 0.05 | 2.54 | 1583 |
| 2024-09-20 22:21:32.109 | MS1 | 121.4656678870 | 31.1446192904 | 7 | 504990 | -78.99 | 15.83 | 454.46 | 0.03 | 2.68 | 1587 |
| 2024-09-20 22:21:33.686 | MS1 | 121.4656700208 | 31.1446238942 | 7 | 504990 | -83.78 | 16.35 | 341.87 | 0.04 | 2.35 | 1589 |
| 2024-09-20 22:21:34.686 | MS1 | 121.4656716574 | 31.1446290799 | 7 | 504990 | -85.67 | 0.86 | 64.50 | 0.17 | 1.13 | 1566 |
| 2024-09-20 22:21:35.784 | MS1 | 121.4656727917 | 31.1446285838 | 7 | 504990 | -94.51 | 2.58 | 87.03 | 0.07 | 1.50 | 1589 |
| 2024-09-20 22:21:36.273 | MS1 | 121.4656583365 | 31.1446378539 | 7 | 504990 | -85.69 | 3.70 | 48.96 | 0.14 | 1.13 | 1593 |
| 2024-09-20 22:21:37.176 | MS1 | 121.4656703592 | 31.1446350114 | 7 | 504990 | -87.94 | 1.61 | 84.76 | 0.12 | 1.10 | 1595 |
| 2024-09-20 22:21:38.627 | MS1 | 121.4656691055 | 31.1446371205 | 7 | 504990 | -90.49 | 1.17 | 49.85 | 0.03 | 1.29 | 1590 |
| 2024-09-20 22:21:39.143 | MS1 | 121.4656630698 | 31.1446233906 | 7 | 504990 | -86.60 | 3.14 | 71.30 | 0.20 | 1.05 | 1572 |
| 2024-09-20 22:21:40.980 | MS1 | 121.4656779201 | 31.1446299731 | 7 | 504990 | -82.06 | 16.62 | 578.51 | 0.01 | 2.79 | 1597 |
| 2024-09-20 22:21:41.748 | MS1 | 121.4656686103 | 31.1446190711 | 7 | 504990 | -83.55 | 17.04 | 373.15 | 0.11 | 2.77 | 1575 |
| 2024-09-20 22:21:42.873 | MS1 | 121.4656635102 | 31.1446227894 | 7 | 504990 | -78.50 | 17.67 | 519.29 | 0.18 | 2.15 | 1582 |

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
| 3221890 | 4 | 121.4730274653 | 31.1527522075 | 256 | 0 | 3 | 42.9 | TDD | 7 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3234649 | 2 | 121.4685532690 | 31.1484010901 | 230 | 2 | 12 | 16.7 | TDD | 89 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3253994 | 3 | 121.4678411961 | 31.1530655738 | 32 | 14 | 0 | 34.5 | TDD | 685 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3254764 | 1 | 121.4685393951 | 31.1531146620 | 79 | 8 | 3 | 46.4 | TDD | 960 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |

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
| 2024-09-20 22:21:31.134 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.159 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.281 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.281 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3254764 | 1 | 8.2078 | 16.2993 | -117.4435 | 6.3556 | 126.4703 | 0.0158 | 0.0037 |
| 2024_09_20 22:00 | 3234649 | 2 | 9.9846 | 11.6400 | -114.5097 | 11.4539 | 132.8441 | 0.0151 | 0.0053 |
| 2024_09_20 22:00 | 3253994 | 3 | 14.7110 | 17.8938 | -116.8561 | 11.7108 | 172.9215 | 0.0094 | 0.0166 |
| 2024_09_20 22:00 | 3221890 | 4 | 5.9761 | 5.6824 | -108.1335 | 17.0742 | 110.5068 | 0.0075 | 0.0068 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414138_864EFDC5 | 504990 | 7 | -85.6 | 504990 | 89 | -84.5 | 504990 | 960 | -84.8 | 504990 | 685 |
| MR_1774414138_4806B4B9 | 504990 | 7 | -83.9 | 504990 | 89 | -85.3 | 504990 | 960 | -83.6 | 504990 | 685 |
| MR_1774414138_6C009255 | 504990 | 89 | -85.0 | 504990 | 7 | -83.2 | 504990 | 960 | -84.0 | 504990 | 685 |
| MR_1774414138_11798B4D | 504990 | 89 | -87.5 | 504990 | 7 | -82.4 | 504990 | 960 | -86.5 | 504990 | 685 |
| MR_1774414138_A4EDB3C5 | 504990 | 7 | -85.8 | 504990 | 89 | -83.4 | 504990 | 960 | -83.5 | 504990 | 685 |
| MR_1774414138_D982A16C | 504990 | 7 | -85.4 | 504990 | 89 | -81.8 | 504990 | 960 | -85.2 | 504990 | 685 |

> *... 2개 열 생략 (전체 14열)*

---
