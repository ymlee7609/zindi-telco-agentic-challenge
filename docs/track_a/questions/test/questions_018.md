# Track A 문제 분석 — test[170]~test[179]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/test.json`
> 범위: test[170] ~ test[179] (10개)

## 목차

1. [문제 170: `1cfe8e26-cff...`](#170) — single-answer
2. [문제 171: `307d34ee-e10...`](#171) — single-answer
3. [문제 172: `23e9c24c-7bd...`](#172) — single-answer
4. [문제 173: `6b1084e5-330...`](#173) — single-answer
5. [문제 174: `8f99cfa5-803...`](#174) — single-answer
6. [문제 175: `c55410a3-6e1...`](#175) — single-answer
7. [문제 176: `92a570c8-97e...`](#176) — single-answer
8. [문제 177: `40d54730-655...`](#177) — single-answer
9. [문제 178: `35463934-73a...`](#178) — single-answer
10. [문제 179: `3fc6dd90-c8f...`](#179) — single-answer

---

### 문제 170: `1cfe8e26-cff...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `1cfe8e26-cff1-435d-975e-7db5f634c930` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[170] topology](images/test_0170.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3214533_1
- `C2`: Add neighbor relationship between 3219727_4 and 3214533_1
- `C3`: Lift the tilt angle of 3227576_2 by 2 degrees
- `C4`: Decrease transmission power for 3227576_2
- `C5`: Increase A3 Offset threshold for 3214533_1
- `C6`: Add neighbor relationship between 3227576_2 and 3214533_1
- `C7`: Decrease A3 Offset threshold for 3227576_2
- `C8`: Adjust the azimuth of 3227576_2 by 3 degrees
- `C9`: Adjust the azimuth of 3219727_4 by 50 degrees
- `C10`: Press down the tilt angle  of 3219727_4 by 10 degrees
- `C11`: Decrease transmission power for 3214533_1
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3227576_2
- `C13`: Lift the tilt angle  of 3219727_4 by 10 degrees
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3214533_1
- `C15`: Increase A3 Offset threshold for 3227576_2
- `C16`: Press down the tilt angle of 3227576_2 by 2 degrees
- `C17`: Decrease A3 Offset threshold for 3214533_1
- `C18`: Insufficient data; more data is needed for judgment.
- `C19`: Check test server and transmission issues
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3227576_2
- `C21`: Increase transmission power for 3214533_1
- `C22`: Increase transmission power for 3227576_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.371 | MS1 | 121.4656753261 | 31.1446338409 | 485 | 504990 | -87.97 | 14.60 | 377.20 | 0.11 | 2.21 | 1588 |
| 2024-09-20 22:21:32.547 | MS1 | 121.4656700116 | 31.1446286475 | 485 | 504990 | -89.56 | 18.00 | 436.45 | 0.18 | 2.12 | 1588 |
| 2024-09-20 22:21:33.944 | MS1 | 121.4656590214 | 31.1446361742 | 485 | 504990 | -89.11 | 17.38 | 549.93 | 0.02 | 2.99 | 1597 |
| 2024-09-20 22:21:34.935 | MS1 | 121.4656768764 | 31.1446335254 | 485 | 504990 | -89.80 | 13.84 | 56.66 | 0.09 | 2.29 | 1579 |
| 2024-09-20 22:21:35.977 | MS1 | 121.4656696228 | 31.1446294783 | 485 | 504990 | -86.96 | 17.85 | 90.89 | 0.16 | 2.79 | 1585 |
| 2024-09-20 22:21:36.968 | MS1 | 121.4656590464 | 31.1446269721 | 485 | 504990 | -91.57 | 14.86 | 94.02 | 0.05 | 2.90 | 1577 |
| 2024-09-20 22:21:37.355 | MS1 | 121.4656649459 | 31.1446188604 | 485 | 504990 | -92.38 | 8.26 | 59.51 | 0.16 | 2.62 | 1595 |
| 2024-09-20 22:21:38.848 | MS1 | 121.4656661171 | 31.1446363264 | 485 | 504990 | -92.42 | 12.36 | 105.62 | 0.19 | 2.73 | 1573 |
| 2024-09-20 22:21:39.513 | MS1 | 121.4656764549 | 31.1446238249 | 485 | 504990 | -90.71 | 9.59 | 57.29 | 0.20 | 2.47 | 1581 |
| 2024-09-20 22:21:40.115 | MS1 | 121.4656765596 | 31.1446331668 | 485 | 504990 | -91.09 | 9.20 | 400.70 | 0.18 | 2.58 | 1585 |
| 2024-09-20 22:21:41.998 | MS1 | 121.4656733660 | 31.1446365995 | 485 | 504990 | -91.25 | 8.05 | 353.85 | 0.15 | 2.32 | 1567 |
| 2024-09-20 22:21:42.472 | MS1 | 121.4656604426 | 31.1446226324 | 485 | 504990 | -93.28 | 12.00 | 440.23 | 0.09 | 2.36 | 1575 |

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
| 3214533 | 1 | 121.4685048362 | 31.1443606094 | 330 | 0 | 7 | 47.0 | TDD | 400 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3219727 | 4 | 121.4719776028 | 31.1538617654 | 60 | 8 | 8 | 28.9 | TDD | 998 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3227576 | 2 | 121.4648442094 | 31.1545336633 | 179 | 0 | 4 | 33.9 | TDD | 485 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3248043 | 3 | 121.4724356822 | 31.1450400545 | 274 | 2 | 2 | 38.9 | TDD | 285 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |

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
| 2024-09-20 22:21:31.421 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.443 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.553 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.553 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.281 | NREventA3 | measId:2;ServCellPCI:805;Se... |
| 2024-09-20 22:21:38.521 | NRHandoverAttempt | SourcePCI:805;SourceNR-ARFC... |
| 2024-09-20 22:21:38.561 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.572 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.705 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.705 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3214533 | 1 | 12.4428 | 16.0479 | -116.3684 | 9.3752 | 96.7498 | 0.0046 | 0.0160 |
| 2024_09_20 22:00 | 3227576 | 2 | 76.5541 | 87.1659 | -116.4372 | 9.4738 | 152.9321 | 0.0021 | 0.0115 |
| 2024_09_20 22:00 | 3248043 | 3 | 19.8485 | 14.9092 | -114.9065 | 5.8088 | 93.5168 | 0.0148 | 0.0177 |
| 2024_09_20 22:00 | 3219727 | 4 | 19.8683 | 15.1811 | -117.7919 | 10.3990 | 131.7654 | 0.0023 | 0.0060 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413824_74D410C1 | 504990 | 485 | -88.8 | 504990 | 400 | -99.0 | 504990 | 998 | -102.2 | 504990 | 285 |
| MR_1774413824_5E0BEBDE | 504990 | 485 | -87.9 | 504990 | 400 | -98.3 | 504990 | 998 | -104.6 | 504990 | 285 |
| MR_1774413824_130A646E | 504990 | 485 | -89.0 | 504990 | 400 | -96.7 | 504990 | 998 | -103.9 | 504990 | 285 |
| MR_1774413824_973BBFBF | 504990 | 485 | -90.0 | 504990 | 400 | -96.7 | 504990 | 998 | -102.5 | 504990 | 285 |
| MR_1774413824_B98D9261 | 504990 | 485 | -89.7 | 504990 | 400 | -96.5 | 504990 | 998 | -104.4 | 504990 | 285 |
| MR_1774413824_DC3F9A2D | 504990 | 485 | -88.8 | 504990 | 400 | -96.8 | 504990 | 998 | -102.6 | 504990 | 285 |
| MR_1774413824_55CAD71C | 504990 | 485 | -88.6 | 504990 | 400 | -98.5 | 504990 | 998 | -103.2 | 504990 | 285 |
| MR_1774413824_490E269E | 504990 | 485 | -91.0 | 504990 | 400 | -98.5 | 504990 | 998 | -100.8 | 504990 | 285 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 171: `307d34ee-e10...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `307d34ee-e100-4b49-b223-6c5292db2945` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[171] topology](images/test_0171.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3224973_6 by 28 degrees
- `C2`: Add neighbor relationship between 3224973_6 and 3249209_2
- `C3`: Press down the tilt angle of 3224973_6 by 2 degrees
- `C4`: Insufficient data; more data is needed for judgment.
- `C5`: Decrease A3 Offset threshold for 3249209_2
- `C6`: Adjust the azimuth of 3249209_2 by 14 degrees
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3249209_2
- `C8`: Decrease transmission power for 3224973_6
- `C9`: Increase A3 Offset threshold for 3224973_6
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3249209_2
- `C11`: Lift the tilt angle of 3224973_6 by 2 degrees
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3224973_6
- `C13`: Decrease A3 Offset threshold for 3224973_6
- `C14`: Check test server and transmission issues
- `C15`: Lift the tilt angle  of 3249209_2 by 4 degrees
- `C16`: Press down the tilt angle  of 3249209_2 by 4 degrees
- `C17`: Increase A3 Offset threshold for 3249209_2
- `C18`: Increase transmission power for 3249209_2
- `C19`: Add neighbor relationship between 3248851_10 and 3249209_2
- `C20`: Decrease transmission power for 3249209_2
- `C21`: Increase transmission power for 3224973_6
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3224973_6

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.314 | MS1 | 121.4656599540 | 31.1446305474 | 412 | 504990 | -94.67 | 12.77 | 335.13 | 0.16 | 2.12 | 1576 |
| 2024-09-20 22:21:32.267 | MS1 | 121.4656643904 | 31.1446252723 | 268 | 504990 | -95.69 | 9.91 | 339.29 | 0.08 | 2.32 | 1560 |
| 2024-09-20 22:21:33.449 | MS1 | 121.4656755708 | 31.1446351338 | 982 | 504990 | -93.09 | 11.68 | 505.04 | 0.15 | 2.59 | 1587 |
| 2024-09-20 22:21:34.313 | MS1 | 121.4656640236 | 31.1446196131 | 742 | 152650 | -93.91 | 6.16 | 63.11 | 0.16 | 1.96 | 948 |
| 2024-09-20 22:21:35.260 | MS1 | 121.4656702460 | 31.1446278779 | 343 | 152650 | -94.68 | 7.49 | 43.47 | 0.02 | 1.67 | 900 |
| 2024-09-20 22:21:36.142 | MS1 | 121.4656587781 | 31.1446213014 | 300 | 152650 | -91.10 | 2.77 | 75.22 | 0.02 | 1.65 | 989 |
| 2024-09-20 22:21:37.543 | MS1 | 121.4656677470 | 31.1446344051 | 448 | 152650 | -92.87 | 6.11 | 80.04 | 0.18 | 1.96 | 910 |
| 2024-09-20 22:21:38.898 | MS1 | 121.4656646026 | 31.1446181783 | 742 | 152650 | -93.76 | 5.64 | 55.86 | 0.16 | 1.68 | 949 |
| 2024-09-20 22:21:39.874 | MS1 | 121.4656661624 | 31.1446349342 | 343 | 152650 | -95.81 | 6.85 | 56.81 | 0.18 | 1.51 | 934 |
| 2024-09-20 22:21:40.342 | MS1 | 121.4656687110 | 31.1446371403 | 300 | 152650 | -94.78 | 2.90 | 68.80 | 0.02 | 2.25 | 1576 |
| 2024-09-20 22:21:41.295 | MS1 | 121.4656621842 | 31.1446269974 | 448 | 152650 | -88.95 | 7.90 | 63.69 | 0.17 | 2.17 | 1567 |
| 2024-09-20 22:21:42.912 | MS1 | 121.4656773446 | 31.1446368460 | 742 | 152650 | -94.78 | 7.58 | 88.15 | 0.08 | 2.76 | 1569 |

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
| 3210448 | 3 | 121.4753794824 | 31.1479468286 | 82 | 11 | 8 | 27.5 | TDD | 268 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3212505 | 11 | 121.4748886305 | 31.1538380844 | 161 | 2 | 11 | 7.2 | FDD | 725 | n1 | 152650 | 30M | 4T4R | 30 | 152650 |
| 3219162 | 4 | 121.4659195056 | 31.1443359272 | 276 | 8 | 2 | 0.3 | TDD | 945 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3221027 | 8 | 121.4712777680 | 31.1528275053 | 298 | 15 | 7 | 26.0 | FDD | 742 | n1 | 152650 | 30M | 4T4R | 11 | 152650 |
| 3224973 | 6 | 121.4698466654 | 31.1523524759 | 233 | 0 | 1 | 27.8 | TDD | 412 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3239225 | 12 | 121.4694949267 | 31.1559797627 | 166 | 0 | 1 | 11.9 | FDD | 343 | n1 | 152650 | 30M | 4T4R | 21 | 152650 |
| 3248851 | 10 | 121.4727693784 | 31.1538716356 | 342 | 8 | 3 | 13.6 | FDD | 300 | n1 | 152650 | 30M | 4T4R | 13 | 152650 |
| 3249209 | 2 | 121.4702662138 | 31.1464899142 | 231 | 2 | 2 | 14.6 | TDD | 134 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3251435 | 1 | 121.4746781935 | 31.1523247201 | 83 | 11 | 3 | 5.4 | TDD | 612 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3254431 | 9 | 121.4748962019 | 31.1447656453 | 163 | 2 | 0 | 21.1 | FDD | 840 | n1 | 152650 | 30M | 4T4R | 29 | 152650 |
| 3263217 | 7 | 121.4698010529 | 31.1517966541 | 115 | 15 | 0 | 20.4 | FDD | 448 | n1 | 152650 | 30M | 4T4R | 18 | 152650 |
| 3267161 | 5 | 121.4709231728 | 31.1526726329 | 150 | 3 | 10 | 24.5 | TDD | 982 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3275150 | 13 | 121.4682796346 | 31.1506524601 | 195 | 10 | 9 | 20.4 | FDD | 186 | n1 | 152650 | 30M | 4T4R | 25 | 152650 |

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
| 2024-09-20 22:21:31.284 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.409 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.409 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.067 | NREventA2 | measId:1;ServCellPCI:370;Se... |
| 2024-09-20 22:21:35.178 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.429 | NREventA5 | measId:3;ServCellPCI:370;Se... |
| 2024-09-20 22:21:35.484 | NRHandoverAttempt | SourcePCI:370;SourceNR-ARFC... |
| 2024-09-20 22:21:35.522 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.532 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:35.650 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.650 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3251435 | 1 | 18.9781 | 9.7245 | -117.1559 | 8.3085 | 100.3422 | 0.0147 | 0.0015 |
| 2024_09_20 22:00 | 3249209 | 2 | 6.1451 | 9.5005 | -114.6067 | 13.0539 | 149.1958 | 0.0006 | 0.0044 |
| 2024_09_20 22:00 | 3210448 | 3 | 7.2601 | 15.6731 | -114.1308 | 11.6458 | 147.7912 | 0.0108 | 0.0036 |
| 2024_09_20 22:00 | 3219162 | 4 | 14.2492 | 12.5119 | -114.2870 | 11.9570 | 105.8240 | 0.0030 | 0.0010 |
| 2024_09_20 22:00 | 3267161 | 5 | 8.8092 | 8.8313 | -117.0966 | 9.0444 | 131.1923 | 0.0027 | 0.0099 |
| 2024_09_20 22:00 | 3224973 | 6 | 17.3968 | 9.9357 | -116.1031 | 5.0250 | 131.6786 | 0.0082 | 0.0196 |
| 2024_09_20 22:00 | 3263217 | 7 | 12.9528 | 10.1475 | -115.1169 | 3.0671 | 29.1149 | 0.0032 | 0.0032 |
| 2024_09_20 22:00 | 3221027 | 8 | 17.5549 | 11.3970 | -116.0534 | 3.8789 | 26.3952 | 0.0122 | 0.0104 |
| 2024_09_20 22:00 | 3254431 | 9 | 19.0095 | 9.4347 | -115.7736 | 3.3470 | 55.8050 | 0.0147 | 0.0043 |
| 2024_09_20 22:00 | 3248851 | 10 | 10.0182 | 15.8436 | -116.4348 | 3.9669 | 20.4016 | 0.0105 | 0.0002 |
| 2024_09_20 22:00 | 3212505 | 11 | 17.7456 | 5.3308 | -116.7438 | 3.0851 | 59.6357 | 0.0018 | 0.0131 |
| 2024_09_20 22:00 | 3239225 | 12 | 12.3842 | 12.8096 | -114.4360 | 4.9420 | 47.4494 | 0.0157 | 0.0126 |
| 2024_09_20 22:00 | 3275150 | 13 | 8.1262 | 18.0544 | -117.9446 | 4.3981 | 31.3762 | 0.0155 | 0.0140 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412087_EC6E5F75 | 504990 | 982 | -94.2 | 504990 | 134 | -96.2 | 504990 | 612 | -101.0 | 504990 | 945 |
| MR_1774412087_17FF57BC | 504990 | 982 | -92.1 | 504990 | 134 | -95.2 | 504990 | 612 | -99.4 | 504990 | 945 |
| MR_1774412087_76B9515F | 504990 | 982 | -94.2 | 504990 | 134 | -98.2 | 504990 | 612 | -98.0 | 504990 | 945 |
| MR_1774412087_939FAE9F | 504990 | 982 | -93.6 | 504990 | 134 | -97.8 | 504990 | 612 | -99.0 | 504990 | 945 |
| MR_1774412087_EB48DE1D | 152650 | 742 | -95.1 | 152650 | 725 | -98.8 | 152650 | 840 | -99.6 | 152650 | 186 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 172: `23e9c24c-7bd...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `23e9c24c-7bd6-4ff5-9df7-6889d4ec92b2` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[172] topology](images/test_0172.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3226988_1 by 3 degrees
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3226988_1
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3239309_2
- `C4`: Increase transmission power for 3226988_1
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3226988_1
- `C6`: Check test server and transmission issues
- `C7`: Decrease A3 Offset threshold for 3239309_2
- `C8`: Adjust the azimuth of 3226988_1 by 10 degrees
- `C9`: Decrease transmission power for 3226988_1
- `C10`: Decrease transmission power for 3239309_2
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3239309_2
- `C12`: Lift the tilt angle of 3239309_2 by 5 degrees
- `C13`: Decrease A3 Offset threshold for 3226988_1
- `C14`: Lift the tilt angle  of 3226988_1 by 3 degrees
- `C15`: Increase transmission power for 3239309_2
- `C16`: Adjust the azimuth of 3239309_2 by 50 degrees
- `C17`: Add neighbor relationship between 3239309_2 and 3226988_1
- `C18`: Increase A3 Offset threshold for 3239309_2
- `C19`: Increase A3 Offset threshold for 3226988_1
- `C20`: Insufficient data; more data is needed for judgment.
- `C21`: Press down the tilt angle of 3239309_2 by 5 degrees
- `C22`: Add neighbor relationship between 3268087_4 and 3226988_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.678 | MS1 | 121.4656687748 | 31.1446295383 | 4 | 504990 | -75.47 | 13.18 | 444.85 | 0.10 | 2.86 | 1590 |
| 2024-09-20 22:21:32.738 | MS1 | 121.4656611312 | 31.1446341602 | 4 | 504990 | -78.38 | 13.74 | 486.59 | 0.14 | 2.64 | 1563 |
| 2024-09-20 22:21:33.482 | MS1 | 121.4656667389 | 31.1446230432 | 4 | 504990 | -77.56 | 16.22 | 538.41 | 0.17 | 2.71 | 1599 |
| 2024-09-20 22:21:34.218 | MS1 | 121.4656677897 | 31.1446194590 | 4 | 504990 | -91.91 | -0.20 | 53.66 | 0.06 | 1.40 | 1560 |
| 2024-09-20 22:21:35.838 | MS1 | 121.4656748982 | 31.1446378461 | 4 | 504990 | -87.71 | -3.56 | 33.16 | 0.19 | 1.48 | 1577 |
| 2024-09-20 22:21:36.134 | MS1 | 121.4656742072 | 31.1446349503 | 4 | 504990 | -92.67 | -3.99 | 35.47 | 0.05 | 1.10 | 1578 |
| 2024-09-20 22:21:37.974 | MS1 | 121.4656710228 | 31.1446342597 | 4 | 504990 | -87.90 | -2.10 | 50.43 | 0.18 | 1.21 | 1570 |
| 2024-09-20 22:21:38.522 | MS1 | 121.4656675058 | 31.1446297275 | 4 | 504990 | -75.92 | 17.28 | 368.60 | 0.18 | 1.10 | 1600 |
| 2024-09-20 22:21:39.454 | MS1 | 121.4656698164 | 31.1446324949 | 4 | 504990 | -77.02 | 15.65 | 555.45 | 0.10 | 1.10 | 1568 |
| 2024-09-20 22:21:40.924 | MS1 | 121.4656692365 | 31.1446347356 | 4 | 504990 | -79.45 | 13.66 | 486.50 | 0.06 | 2.99 | 1578 |
| 2024-09-20 22:21:41.630 | MS1 | 121.4656773855 | 31.1446258408 | 4 | 504990 | -83.18 | 17.41 | 549.71 | 0.07 | 2.08 | 1584 |
| 2024-09-20 22:21:42.974 | MS1 | 121.4656610975 | 31.1446279586 | 4 | 504990 | -77.92 | 12.99 | 302.72 | 0.08 | 2.91 | 1588 |

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
| 3226988 | 1 | 121.4724598938 | 31.1442645602 | 284 | 0 | 3 | 38.4 | TDD | 952 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3239309 | 2 | 121.4731958167 | 31.1480920861 | 186 | 2 | 4 | 48.9 | TDD | 4 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3240096 | 3 | 121.4697604472 | 31.1476624272 | 134 | 3 | 3 | 24.6 | TDD | 965 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3268087 | 4 | 121.4677348306 | 31.1491006025 | 265 | 9 | 1 | 42.0 | TDD | 688 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |

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
| 2024-09-20 22:21:31.241 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.353 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.353 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.063 | NREventA3 | measId:2;ServCellPCI:103;Se... |
| 2024-09-20 22:21:36.063 | NREventA3 | measId:2;ServCellPCI:103;Se... |
| 2024-09-20 22:21:37.063 | NREventA3 | measId:2;ServCellPCI:103;Se... |
| 2024-09-20 22:21:39.563 | NRRRCReestablishAttempt | PCI:103 |
| 2024-09-20 22:21:39.578 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.593 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:39.716 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.716 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3226988 | 1 | 19.3358 | 10.1940 | -116.4159 | 8.4448 | 145.8389 | 0.0014 | 0.0055 |
| 2024_09_20 22:00 | 3239309 | 2 | 5.9124 | 5.7287 | -115.6470 | 13.3126 | 122.6629 | 0.0007 | 0.1980 |
| 2024_09_20 22:00 | 3240096 | 3 | 14.0351 | 12.4192 | -115.9810 | 19.6139 | 80.0694 | 0.0192 | 0.0139 |
| 2024_09_20 22:00 | 3268087 | 4 | 5.2158 | 15.4403 | -116.7659 | 17.3626 | 123.1283 | 0.0127 | 0.0086 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415464_5DA788A1 | 504990 | 952 | -85.3 | 504990 | 4 | -93.1 | 504990 | 688 | -89.0 | 504990 | 965 |
| MR_1774415464_419E59D3 | 504990 | 4 | -92.5 | 504990 | 952 | -86.6 | 504990 | 688 | -91.5 | 504990 | 965 |
| MR_1774415464_F5375AC8 | 504990 | 952 | -86.6 | 504990 | 4 | -92.6 | 504990 | 688 | -91.5 | 504990 | 965 |
| MR_1774415464_65A335C5 | 504990 | 952 | -86.6 | 504990 | 4 | -91.7 | 504990 | 688 | -89.9 | 504990 | 965 |
| MR_1774415464_072C236F | 504990 | 4 | -92.9 | 504990 | 952 | -88.5 | 504990 | 688 | -92.6 | 504990 | 965 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 173: `6b1084e5-330...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `6b1084e5-330e-452d-bd41-e1d9267b82bc` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[173] topology](images/test_0173.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3255735_1 and 3260876_3
- `C2`: Lift the tilt angle of 3273729_2 by 4 degrees
- `C3`: Decrease transmission power for 3273729_2
- `C4`: Adjust the azimuth of 3273729_2 by 50 degrees
- `C5`: Decrease transmission power for 3260876_3
- `C6`: Decrease A3 Offset threshold for 3260876_3
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3273729_2
- `C8`: Press down the tilt angle  of 3260876_3 by 10 degrees
- `C9`: Decrease A3 Offset threshold for 3273729_2
- `C10`: Add neighbor relationship between 3273729_2 and 3260876_3
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3260876_3
- `C12`: Increase A3 Offset threshold for 3273729_2
- `C13`: Insufficient data; more data is needed for judgment.
- `C14`: Increase transmission power for 3273729_2
- `C15`: Increase transmission power for 3260876_3
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3260876_3
- `C17`: Adjust the azimuth of 3260876_3 by 14 degrees
- `C18`: Check test server and transmission issues
- `C19`: Lift the tilt angle  of 3260876_3 by 10 degrees
- `C20`: Increase A3 Offset threshold for 3260876_3
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3273729_2
- `C22`: Press down the tilt angle of 3273729_2 by 4 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.313 | MS1 | 121.4656653829 | 31.1446362736 | 705 | 504990 | -88.85 | 12.10 | 573.18 | 0.01 | 2.67 | 1580 |
| 2024-09-20 22:21:32.105 | MS1 | 121.4656615168 | 31.1446197287 | 705 | 504990 | -88.79 | 14.32 | 556.53 | 0.13 | 2.82 | 1573 |
| 2024-09-20 22:21:33.537 | MS1 | 121.4656740149 | 31.1446222094 | 705 | 504990 | -85.48 | 15.20 | 516.16 | 0.12 | 2.79 | 1568 |
| 2024-09-20 22:21:34.437 | MS1 | 121.4656625908 | 31.1446293956 | 705 | 504990 | -91.21 | 16.54 | 72.33 | 0.16 | 2.40 | 399 |
| 2024-09-20 22:21:35.387 | MS1 | 121.4656705715 | 31.1446180367 | 705 | 504990 | -85.99 | 15.95 | 96.33 | 0.08 | 2.17 | 344 |
| 2024-09-20 22:21:36.364 | MS1 | 121.4656692456 | 31.1446257273 | 705 | 504990 | -85.69 | 12.60 | 68.67 | 0.13 | 2.14 | 300 |
| 2024-09-20 22:21:37.606 | MS1 | 121.4656684412 | 31.1446225374 | 705 | 504990 | -89.63 | 10.37 | 87.24 | 0.02 | 2.22 | 424 |
| 2024-09-20 22:21:38.399 | MS1 | 121.4656646351 | 31.1446211042 | 705 | 504990 | -92.24 | 12.17 | 89.63 | 0.05 | 2.80 | 494 |
| 2024-09-20 22:21:39.101 | MS1 | 121.4656685348 | 31.1446362649 | 705 | 504990 | -93.63 | 10.17 | 49.01 | 0.12 | 2.19 | 427 |
| 2024-09-20 22:21:40.610 | MS1 | 121.4656617404 | 31.1446254750 | 705 | 504990 | -93.96 | 9.36 | 570.27 | 0.15 | 2.29 | 1571 |
| 2024-09-20 22:21:41.604 | MS1 | 121.4656753708 | 31.1446217637 | 705 | 504990 | -93.21 | 12.51 | 589.01 | 0.11 | 2.86 | 1562 |
| 2024-09-20 22:21:42.682 | MS1 | 121.4656668297 | 31.1446276816 | 705 | 504990 | -91.26 | 11.22 | 398.06 | 0.10 | 2.66 | 1581 |

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
| 3240061 | 4 | 121.4683372658 | 31.1540163624 | 222 | 11 | 9 | 48.0 | TDD | 228 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3255735 | 1 | 121.4712943967 | 31.1548171562 | 199 | 15 | 12 | 28.1 | TDD | 136 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3260876 | 3 | 121.4647433452 | 31.1466207837 | 144 | 6 | 5 | 18.2 | TDD | 36 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3273729 | 2 | 121.4729572400 | 31.1448031338 | 165 | 2 | 11 | 29.2 | TDD | 705 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:31.066 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.086 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.208 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.208 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.890 | NREventA3 | measId:2;ServCellPCI:852;Se... |
| 2024-09-20 22:21:38.130 | NRHandoverAttempt | SourcePCI:852;SourceNR-ARFC... |
| 2024-09-20 22:21:38.178 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.192 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.318 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.318 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3255735 | 1 | 11.4276 | 9.5937 | -116.8463 | 16.9446 | 85.0452 | 0.0096 | 0.0062 |
| 2024_09_20 22:00 | 3273729 | 2 | 9.9454 | 5.1204 | -116.5408 | 8.4277 | 145.7885 | 0.0025 | 0.0004 |
| 2024_09_20 22:00 | 3260876 | 3 | 15.5470 | 5.7463 | -115.5526 | 17.0041 | 137.5488 | 0.0100 | 0.0178 |
| 2024_09_20 22:00 | 3240061 | 4 | 13.3931 | 13.3525 | -114.1756 | 15.8576 | 81.2134 | 0.0105 | 0.0061 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412793_07065BEA | 504990 | 705 | -91.9 | 504990 | 36 | -94.9 | 504990 | 136 | -102.3 | 504990 | 228 |
| MR_1774412793_F46D9145 | 504990 | 705 | -89.8 | 504990 | 36 | -91.6 | 504990 | 136 | -102.2 | 504990 | 228 |
| MR_1774412793_3B88F915 | 504990 | 705 | -90.7 | 504990 | 36 | -92.8 | 504990 | 136 | -102.7 | 504990 | 228 |
| MR_1774412793_53454916 | 504990 | 705 | -92.1 | 504990 | 36 | -92.1 | 504990 | 136 | -104.3 | 504990 | 228 |
| MR_1774412793_CCF10089 | 504990 | 705 | -90.2 | 504990 | 36 | -93.6 | 504990 | 136 | -104.3 | 504990 | 228 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 174: `8f99cfa5-803...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `8f99cfa5-8037-472b-bbe5-3c032b289470` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[174] topology](images/test_0174.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3266756_4 by 50 degrees
- `C2`: Increase transmission power for 3266756_4
- `C3`: Insufficient data; more data is needed for judgment.
- `C4`: Lift the tilt angle  of 3266756_4 by 10 degrees
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3266756_4
- `C6`: Increase A3 Offset threshold for 3266756_4
- `C7`: Decrease transmission power for 3266756_4
- `C8`: Increase transmission power for 3255422_1
- `C9`: Press down the tilt angle  of 3266756_4 by 10 degrees
- `C10`: Decrease transmission power for 3255422_1
- `C11`: Check test server and transmission issues
- `C12`: Press down the tilt angle of 3255422_1 by 10 degrees
- `C13`: Add neighbor relationship between 3276768_3 and 3266756_4
- `C14`: Lift the tilt angle of 3255422_1 by 10 degrees
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3266756_4
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3255422_1
- `C17`: Increase A3 Offset threshold for 3255422_1
- `C18`: Add neighbor relationship between 3255422_1 and 3266756_4
- `C19`: Decrease A3 Offset threshold for 3255422_1
- `C20`: Adjust the azimuth of 3255422_1 by 50 degrees
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3255422_1
- `C22`: Decrease A3 Offset threshold for 3266756_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.322 | MS1 | 121.4656739140 | 31.1446201743 | 121 | 504990 | -88.65 | 12.77 | 589.16 | 0.19 | 2.64 | 1585 |
| 2024-09-20 22:21:32.359 | MS1 | 121.4656700073 | 31.1446339408 | 121 | 504990 | -86.87 | 13.33 | 423.96 | 0.16 | 2.61 | 1586 |
| 2024-09-20 22:21:33.599 | MS1 | 121.4656713161 | 31.1446190913 | 121 | 504990 | -90.66 | 16.64 | 350.25 | 0.11 | 2.32 | 1586 |
| 2024-09-20 22:21:34.267 | MS1 | 121.4656730209 | 31.1446320220 | 121 | 504990 | -87.74 | 16.79 | 43.95 | 0.12 | 2.09 | 376 |
| 2024-09-20 22:21:35.999 | MS1 | 121.4656766978 | 31.1446233224 | 121 | 504990 | -89.20 | 15.58 | 88.52 | 0.07 | 2.86 | 372 |
| 2024-09-20 22:21:36.738 | MS1 | 121.4656734729 | 31.1446358702 | 121 | 504990 | -89.16 | 12.14 | 66.08 | 0.07 | 2.79 | 487 |
| 2024-09-20 22:21:37.183 | MS1 | 121.4656657173 | 31.1446238075 | 121 | 504990 | -90.51 | 7.11 | 76.75 | 0.07 | 2.73 | 473 |
| 2024-09-20 22:21:38.327 | MS1 | 121.4656592882 | 31.1446269530 | 121 | 504990 | -91.40 | 12.43 | 61.38 | 0.15 | 2.88 | 427 |
| 2024-09-20 22:21:39.263 | MS1 | 121.4656730773 | 31.1446248719 | 121 | 504990 | -91.39 | 7.38 | 84.40 | 0.10 | 2.47 | 478 |
| 2024-09-20 22:21:40.613 | MS1 | 121.4656719473 | 31.1446293238 | 121 | 504990 | -93.22 | 7.65 | 379.03 | 0.04 | 2.29 | 1578 |
| 2024-09-20 22:21:41.544 | MS1 | 121.4656718835 | 31.1446213508 | 121 | 504990 | -89.57 | 7.36 | 509.79 | 0.09 | 2.28 | 1600 |
| 2024-09-20 22:21:42.799 | MS1 | 121.4656601410 | 31.1446195982 | 121 | 504990 | -90.37 | 12.46 | 523.02 | 0.19 | 2.40 | 1594 |

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
| 3219941 | 2 | 121.4724879892 | 31.1471186524 | 29 | 12 | 8 | 40.1 | TDD | 315 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3255422 | 1 | 121.4678134369 | 31.1450133246 | 313 | 6 | 9 | 22.6 | TDD | 121 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3266756 | 4 | 121.4702756789 | 31.1519554767 | 74 | 14 | 8 | 46.7 | TDD | 865 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3276768 | 3 | 121.4671852498 | 31.1542757201 | 41 | 7 | 9 | 37.8 | TDD | 558 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |

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
| 2024-09-20 22:21:31.091 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.106 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.222 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.222 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.911 | NREventA3 | measId:2;ServCellPCI:948;Se... |
| 2024-09-20 22:21:38.151 | NRHandoverAttempt | SourcePCI:948;SourceNR-ARFC... |
| 2024-09-20 22:21:38.194 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.209 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.338 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.338 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3255422 | 1 | 17.0282 | 13.2078 | -116.7398 | 13.5152 | 139.1205 | 0.0065 | 0.0015 |
| 2024_09_20 22:00 | 3219941 | 2 | 5.8937 | 6.8613 | -116.8322 | 9.1809 | 138.0534 | 0.0023 | 0.0048 |
| 2024_09_20 22:00 | 3276768 | 3 | 10.7145 | 12.8076 | -115.9086 | 16.3453 | 140.5479 | 0.0181 | 0.0163 |
| 2024_09_20 22:00 | 3266756 | 4 | 5.5426 | 13.7545 | -114.6292 | 8.0480 | 198.1377 | 0.0057 | 0.0041 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414857_498384D3 | 504990 | 121 | -88.6 | 504990 | 865 | -89.8 | 504990 | 558 | -96.2 | 504990 | 315 |
| MR_1774414857_BC1CF934 | 504990 | 121 | -87.3 | 504990 | 865 | -90.1 | 504990 | 558 | -94.8 | 504990 | 315 |
| MR_1774414857_419E7E99 | 504990 | 121 | -87.7 | 504990 | 865 | -89.9 | 504990 | 558 | -96.9 | 504990 | 315 |
| MR_1774414857_F907F84C | 504990 | 121 | -86.5 | 504990 | 865 | -86.8 | 504990 | 558 | -95.5 | 504990 | 315 |
| MR_1774414857_1E3F71B1 | 504990 | 121 | -86.5 | 504990 | 865 | -86.5 | 504990 | 558 | -96.7 | 504990 | 315 |
| MR_1774414857_D6A3C776 | 504990 | 121 | -87.9 | 504990 | 865 | -86.8 | 504990 | 558 | -94.3 | 504990 | 315 |
| MR_1774414857_33216D66 | 504990 | 121 | -88.2 | 504990 | 865 | -89.8 | 504990 | 558 | -94.4 | 504990 | 315 |
| MR_1774414857_971C7C72 | 504990 | 121 | -85.9 | 504990 | 865 | -89.3 | 504990 | 558 | -94.5 | 504990 | 315 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 175: `c55410a3-6e1...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `c55410a3-6e19-4312-824f-7afd3d94b89c` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[175] topology](images/test_0175.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3276998_1
- `C2`: Press down the tilt angle of 3276998_1 by 4 degrees
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3226941_3
- `C4`: Adjust the azimuth of 3276998_1 by 41 degrees
- `C5`: Lift the tilt angle  of 3230094_2 by 10 degrees
- `C6`: Add neighbor relationship between 3276998_1 and 3226941_3
- `C7`: Insufficient data; more data is needed for judgment.
- `C8`: Increase transmission power for 3226941_3
- `C9`: Lift the tilt angle of 3276998_1 by 4 degrees
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3276998_1
- `C11`: Decrease transmission power for 3276998_1
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3226941_3
- `C13`: Decrease A3 Offset threshold for 3226941_3
- `C14`: Increase A3 Offset threshold for 3226941_3
- `C15`: Press down the tilt angle  of 3230094_2 by 10 degrees
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3276998_1
- `C17`: Decrease A3 Offset threshold for 3276998_1
- `C18`: Check test server and transmission issues
- `C19`: Add neighbor relationship between 3230094_2 and 3226941_3
- `C20`: Decrease transmission power for 3226941_3
- `C21`: Increase A3 Offset threshold for 3276998_1
- `C22`: Adjust the azimuth of 3230094_2 by 26 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.432 | MS1 | 121.4656666970 | 31.1446335862 | 624 | 504990 | -85.84 | 12.34 | 341.30 | 0.12 | 2.34 | 1561 |
| 2024-09-20 22:21:32.593 | MS1 | 121.4656693858 | 31.1446290936 | 624 | 504990 | -87.55 | 16.74 | 303.27 | 0.07 | 2.89 | 1567 |
| 2024-09-20 22:21:33.719 | MS1 | 121.4656664899 | 31.1446312822 | 624 | 504990 | -88.71 | 13.86 | 554.92 | 0.14 | 2.37 | 1588 |
| 2024-09-20 22:21:34.247 | MS1 | 121.4656764460 | 31.1446359466 | 624 | 504990 | -91.28 | 15.97 | 94.16 | 0.03 | 2.96 | 1565 |
| 2024-09-20 22:21:35.604 | MS1 | 121.4656667254 | 31.1446314759 | 624 | 504990 | -91.94 | 13.76 | 58.70 | 0.04 | 2.09 | 1591 |
| 2024-09-20 22:21:36.438 | MS1 | 121.4656642466 | 31.1446321514 | 624 | 504990 | -85.07 | 12.06 | 102.71 | 0.18 | 2.95 | 1595 |
| 2024-09-20 22:21:37.483 | MS1 | 121.4656720086 | 31.1446183009 | 624 | 504990 | -91.51 | 9.87 | 75.32 | 0.12 | 2.00 | 1584 |
| 2024-09-20 22:21:38.987 | MS1 | 121.4656596302 | 31.1446200626 | 624 | 504990 | -90.35 | 11.88 | 87.28 | 0.09 | 2.13 | 1588 |
| 2024-09-20 22:21:39.355 | MS1 | 121.4656689099 | 31.1446255765 | 624 | 504990 | -89.19 | 11.61 | 59.55 | 0.19 | 2.57 | 1573 |
| 2024-09-20 22:21:40.518 | MS1 | 121.4656692690 | 31.1446209837 | 624 | 504990 | -90.20 | 9.07 | 317.66 | 0.05 | 2.18 | 1599 |
| 2024-09-20 22:21:41.143 | MS1 | 121.4656740452 | 31.1446379383 | 624 | 504990 | -90.03 | 10.00 | 393.27 | 0.07 | 2.27 | 1583 |
| 2024-09-20 22:21:42.504 | MS1 | 121.4656647942 | 31.1446216071 | 624 | 504990 | -92.01 | 11.00 | 379.84 | 0.01 | 2.94 | 1583 |

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
| 3226941 | 3 | 121.4740507733 | 31.1481599426 | 270 | 15 | 1 | 27.0 | TDD | 172 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3230094 | 2 | 121.4649466222 | 31.1554136060 | 30 | 3 | 2 | 20.5 | TDD | 219 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3236842 | 4 | 121.4756572540 | 31.1523068522 | 25 | 14 | 4 | 29.9 | TDD | 952 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3276998 | 1 | 121.4690534283 | 31.1517527322 | 243 | 2 | 8 | 36.2 | TDD | 624 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

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
| 2024-09-20 22:21:30.852 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.869 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.017 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.017 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.695 | NREventA3 | measId:2;ServCellPCI:310;Se... |
| 2024-09-20 22:21:37.935 | NRHandoverAttempt | SourcePCI:310;SourceNR-ARFC... |
| 2024-09-20 22:21:37.965 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.976 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.095 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.095 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3276998 | 1 | 79.4811 | 92.5045 | -116.4342 | 11.6455 | 166.2311 | 0.0186 | 0.0113 |
| 2024_09_20 22:00 | 3230094 | 2 | 15.6043 | 12.7229 | -117.8868 | 9.2348 | 114.5421 | 0.0064 | 0.0085 |
| 2024_09_20 22:00 | 3226941 | 3 | 7.4877 | 19.8003 | -116.6579 | 6.4645 | 143.3348 | 0.0154 | 0.0003 |
| 2024_09_20 22:00 | 3236842 | 4 | 15.8909 | 7.2940 | -115.5510 | 15.1673 | 159.8471 | 0.0146 | 0.0010 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416974_89EC511C | 504990 | 624 | -92.9 | 504990 | 172 | -90.2 | 504990 | 219 | -97.4 | 504990 | 952 |
| MR_1774416974_90D50995 | 504990 | 624 | -90.0 | 504990 | 172 | -91.7 | 504990 | 219 | -97.2 | 504990 | 952 |
| MR_1774416974_0B929B58 | 504990 | 624 | -92.1 | 504990 | 172 | -90.3 | 504990 | 219 | -99.1 | 504990 | 952 |
| MR_1774416974_CDD0F6F5 | 504990 | 624 | -92.8 | 504990 | 172 | -93.7 | 504990 | 219 | -99.1 | 504990 | 952 |
| MR_1774416974_45E7E25D | 504990 | 624 | -89.7 | 504990 | 172 | -89.9 | 504990 | 219 | -100.5 | 504990 | 952 |
| MR_1774416974_8AAD4D7F | 504990 | 624 | -93.0 | 504990 | 172 | -89.9 | 504990 | 219 | -97.2 | 504990 | 952 |
| MR_1774416974_1671E814 | 504990 | 624 | -92.1 | 504990 | 172 | -91.5 | 504990 | 219 | -98.8 | 504990 | 952 |
| MR_1774416974_60175C28 | 504990 | 624 | -91.8 | 504990 | 172 | -90.2 | 504990 | 219 | -98.2 | 504990 | 952 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 176: `92a570c8-97e...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `92a570c8-97e1-4a18-973d-20f2539c7afd` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[176] topology](images/test_0176.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3249759_1
- `C2`: Adjust the azimuth of 3249759_1 by 49 degrees
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3249759_1
- `C4`: Increase A3 Offset threshold for 3249759_1
- `C5`: Decrease A3 Offset threshold for 3255076_3
- `C6`: Add neighbor relationship between 3257063_2 and 3249759_1
- `C7`: Lift the tilt angle of 3255076_3 by 5 degrees
- `C8`: Press down the tilt angle of 3255076_3 by 5 degrees
- `C9`: Insufficient data; more data is needed for judgment.
- `C10`: Check test server and transmission issues
- `C11`: Increase A3 Offset threshold for 3255076_3
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3255076_3
- `C13`: Add neighbor relationship between 3255076_3 and 3249759_1
- `C14`: Decrease transmission power for 3249759_1
- `C15`: Decrease transmission power for 3255076_3
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3255076_3
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3249759_1
- `C18`: Press down the tilt angle  of 3249759_1 by 5 degrees
- `C19`: Adjust the azimuth of 3255076_3 by 50 degrees
- `C20`: Increase transmission power for 3255076_3
- `C21`: Increase transmission power for 3249759_1
- `C22`: Lift the tilt angle  of 3249759_1 by 5 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.738 | MS1 | 121.4656757150 | 31.1446312912 | 845 | 504990 | -79.16 | 16.76 | 547.68 | 0.11 | 2.95 | 1597 |
| 2024-09-20 22:21:32.128 | MS1 | 121.4656584487 | 31.1446314871 | 845 | 504990 | -80.06 | 16.79 | 519.25 | 0.01 | 2.08 | 1579 |
| 2024-09-20 22:21:33.416 | MS1 | 121.4656762353 | 31.1446299359 | 845 | 504990 | -80.70 | 12.47 | 345.21 | 0.14 | 2.94 | 1566 |
| 2024-09-20 22:21:34.329 | MS1 | 121.4656641613 | 31.1446370857 | 845 | 504990 | -89.40 | -3.38 | 53.73 | 0.07 | 1.19 | 1587 |
| 2024-09-20 22:21:35.685 | MS1 | 121.4656743646 | 31.1446366579 | 845 | 504990 | -89.72 | -3.62 | 49.77 | 0.20 | 1.23 | 1561 |
| 2024-09-20 22:21:36.785 | MS1 | 121.4656713939 | 31.1446325470 | 845 | 504990 | -89.64 | -2.21 | 43.23 | 0.04 | 1.37 | 1564 |
| 2024-09-20 22:21:37.444 | MS1 | 121.4656632698 | 31.1446357636 | 845 | 504990 | -89.09 | -1.85 | 63.56 | 0.07 | 1.47 | 1589 |
| 2024-09-20 22:21:38.534 | MS1 | 121.4656765012 | 31.1446203974 | 845 | 504990 | -76.70 | 17.36 | 397.07 | 0.14 | 1.19 | 1575 |
| 2024-09-20 22:21:39.856 | MS1 | 121.4656615969 | 31.1446279653 | 845 | 504990 | -80.94 | 16.33 | 368.14 | 0.16 | 1.03 | 1571 |
| 2024-09-20 22:21:40.341 | MS1 | 121.4656735527 | 31.1446188880 | 845 | 504990 | -82.34 | 14.40 | 444.17 | 0.01 | 2.43 | 1588 |
| 2024-09-20 22:21:41.597 | MS1 | 121.4656726546 | 31.1446277089 | 845 | 504990 | -82.00 | 13.64 | 472.66 | 0.02 | 2.45 | 1585 |
| 2024-09-20 22:21:42.847 | MS1 | 121.4656716583 | 31.1446191711 | 845 | 504990 | -80.00 | 16.38 | 377.73 | 0.15 | 2.16 | 1579 |

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
| 3237600 | 4 | 121.4652503032 | 31.1447879108 | 104 | 7 | 11 | 41.7 | TDD | 557 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3249759 | 1 | 121.4648718325 | 31.1547949881 | 225 | 3 | 7 | 39.2 | TDD | 168 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3255076 | 3 | 121.4654291510 | 31.1557513257 | 26 | 4 | 7 | 16.3 | TDD | 845 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3257063 | 2 | 121.4645575491 | 31.1474851203 | 5 | 2 | 9 | 16.8 | TDD | 161 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:31.651 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.675 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.784 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.784 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.497 | NREventA3 | measId:2;ServCellPCI:471;Se... |
| 2024-09-20 22:21:36.497 | NREventA3 | measId:2;ServCellPCI:471;Se... |
| 2024-09-20 22:21:37.497 | NREventA3 | measId:2;ServCellPCI:471;Se... |
| 2024-09-20 22:21:39.997 | NRRRCReestablishAttempt | PCI:471 |
| 2024-09-20 22:21:40.008 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:40.021 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:40.153 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:40.153 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3249759 | 1 | 9.7174 | 6.9258 | -115.7869 | 8.7392 | 179.0309 | 0.0050 | 0.0033 |
| 2024_09_20 22:00 | 3257063 | 2 | 13.6044 | 16.7555 | -115.9050 | 11.6613 | 124.1178 | 0.0004 | 0.0015 |
| 2024_09_20 22:00 | 3255076 | 3 | 15.2542 | 19.9261 | -114.0440 | 5.7247 | 106.4030 | 0.0197 | 0.1959 |
| 2024_09_20 22:00 | 3237600 | 4 | 17.0721 | 5.1036 | -116.4338 | 9.4039 | 151.0719 | 0.0185 | 0.0183 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413460_ACAD906A | 504990 | 168 | -82.9 | 504990 | 845 | -90.9 | 504990 | 161 | -86.7 | 504990 | 557 |
| MR_1774413460_06F0060D | 504990 | 168 | -84.3 | 504990 | 845 | -90.1 | 504990 | 161 | -86.2 | 504990 | 557 |
| MR_1774413460_B6C97B7A | 504990 | 168 | -83.6 | 504990 | 845 | -89.7 | 504990 | 161 | -89.0 | 504990 | 557 |
| MR_1774413460_A463270B | 504990 | 845 | -87.5 | 504990 | 168 | -83.9 | 504990 | 161 | -88.2 | 504990 | 557 |
| MR_1774413460_D12EFDC0 | 504990 | 845 | -90.4 | 504990 | 168 | -85.9 | 504990 | 161 | -87.5 | 504990 | 557 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 177: `40d54730-655...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `40d54730-655e-401e-9b62-3ee9d30b9227` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[177] topology](images/test_0177.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3239698_3
- `C2`: Check test server and transmission issues
- `C3`: Decrease A3 Offset threshold for 3243692_2
- `C4`: Press down the tilt angle  of 3243692_2 by 10 degrees
- `C5`: Decrease transmission power for 3243692_2
- `C6`: Add neighbor relationship between 3264969_1 and 3243692_2
- `C7`: Insufficient data; more data is needed for judgment.
- `C8`: Increase A3 Offset threshold for 3239698_3
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3243692_2
- `C10`: Add neighbor relationship between 3239698_3 and 3243692_2
- `C11`: Increase transmission power for 3243692_2
- `C12`: Press down the tilt angle of 3239698_3 by 10 degrees
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3243692_2
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3239698_3
- `C15`: Increase A3 Offset threshold for 3243692_2
- `C16`: Lift the tilt angle of 3239698_3 by 10 degrees
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3239698_3
- `C18`: Decrease transmission power for 3239698_3
- `C19`: Adjust the azimuth of 3239698_3 by 8 degrees
- `C20`: Adjust the azimuth of 3243692_2 by 50 degrees
- `C21`: Decrease A3 Offset threshold for 3239698_3
- `C22`: Lift the tilt angle  of 3243692_2 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.602 | MS1 | 121.4656625156 | 31.1446271046 | 853 | 504990 | -87.72 | 17.89 | 580.88 | 0.17 | 2.06 | 1589 |
| 2024-09-20 22:21:32.933 | MS1 | 121.4656607230 | 31.1446334602 | 853 | 504990 | -86.83 | 17.70 | 549.26 | 0.01 | 2.40 | 1561 |
| 2024-09-20 22:21:33.123 | MS1 | 121.4656617650 | 31.1446284725 | 853 | 504990 | -91.49 | 15.95 | 485.02 | 0.04 | 2.99 | 1566 |
| 2024-09-20 22:21:34.920 | MS1 | 121.4656728678 | 31.1446272119 | 853 | 504990 | -91.40 | 16.93 | 68.47 | 0.14 | 2.78 | 372 |
| 2024-09-20 22:21:35.875 | MS1 | 121.4656703147 | 31.1446219275 | 853 | 504990 | -91.99 | 15.44 | 103.86 | 0.20 | 2.44 | 374 |
| 2024-09-20 22:21:36.580 | MS1 | 121.4656650742 | 31.1446301284 | 853 | 504990 | -85.10 | 17.10 | 85.15 | 0.15 | 2.36 | 450 |
| 2024-09-20 22:21:37.239 | MS1 | 121.4656721958 | 31.1446192502 | 853 | 504990 | -92.97 | 10.27 | 89.15 | 0.03 | 2.10 | 415 |
| 2024-09-20 22:21:38.504 | MS1 | 121.4656722412 | 31.1446282646 | 853 | 504990 | -89.52 | 8.97 | 95.02 | 0.14 | 2.85 | 362 |
| 2024-09-20 22:21:39.408 | MS1 | 121.4656694347 | 31.1446299270 | 853 | 504990 | -91.87 | 12.77 | 102.33 | 0.01 | 2.53 | 456 |
| 2024-09-20 22:21:40.673 | MS1 | 121.4656741181 | 31.1446254122 | 853 | 504990 | -92.09 | 10.28 | 385.40 | 0.06 | 2.54 | 1560 |
| 2024-09-20 22:21:41.156 | MS1 | 121.4656730740 | 31.1446314922 | 853 | 504990 | -92.15 | 9.83 | 485.89 | 0.07 | 2.27 | 1594 |
| 2024-09-20 22:21:42.125 | MS1 | 121.4656672491 | 31.1446289334 | 853 | 504990 | -91.50 | 11.67 | 466.63 | 0.04 | 2.67 | 1586 |

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
| 3239698 | 3 | 121.4731570531 | 31.1559425990 | 218 | 14 | 9 | 23.0 | TDD | 853 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3243692 | 2 | 121.4658234287 | 31.1463577728 | 335 | 2 | 1 | 43.8 | TDD | 994 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3253747 | 4 | 121.4712972365 | 31.1537095274 | 320 | 3 | 2 | 16.9 | TDD | 527 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3264969 | 1 | 121.4668678202 | 31.1524172610 | 306 | 2 | 2 | 33.4 | TDD | 161 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:31.006 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.028 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.133 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.133 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.890 | NREventA3 | measId:2;ServCellPCI:772;Se... |
| 2024-09-20 22:21:38.130 | NRHandoverAttempt | SourcePCI:772;SourceNR-ARFC... |
| 2024-09-20 22:21:38.165 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.177 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.295 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.295 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3264969 | 1 | 11.5658 | 19.8480 | -116.3365 | 10.0317 | 122.6678 | 0.0174 | 0.0191 |
| 2024_09_20 22:00 | 3243692 | 2 | 17.3056 | 8.3521 | -116.0891 | 8.5262 | 123.2134 | 0.0114 | 0.0129 |
| 2024_09_20 22:00 | 3239698 | 3 | 16.8782 | 9.4619 | -114.0527 | 17.3316 | 198.2474 | 0.0176 | 0.0039 |
| 2024_09_20 22:00 | 3253747 | 4 | 18.2883 | 17.1606 | -115.8374 | 14.9242 | 116.3420 | 0.0162 | 0.0198 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415067_755C1CAC | 504990 | 853 | -89.6 | 504990 | 994 | -100.1 | 504990 | 161 | -101.6 | 504990 | 527 |
| MR_1774415067_05F2F4C6 | 504990 | 853 | -90.3 | 504990 | 994 | -99.5 | 504990 | 161 | -103.1 | 504990 | 527 |
| MR_1774415067_88EA0127 | 504990 | 853 | -92.8 | 504990 | 994 | -100.1 | 504990 | 161 | -103.5 | 504990 | 527 |
| MR_1774415067_907DF4CA | 504990 | 853 | -89.4 | 504990 | 994 | -102.9 | 504990 | 161 | -102.5 | 504990 | 527 |
| MR_1774415067_507AD933 | 504990 | 853 | -90.3 | 504990 | 994 | -99.7 | 504990 | 161 | -103.7 | 504990 | 527 |
| MR_1774415067_FD68ED11 | 504990 | 853 | -92.1 | 504990 | 994 | -103.0 | 504990 | 161 | -102.6 | 504990 | 527 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 178: `35463934-73a...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `35463934-73a0-4d66-8372-b2f65b8b081e` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[178] topology](images/test_0178.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3266895_4
- `C2`: Add neighbor relationship between 3278060_2 and 3266895_4
- `C3`: Adjust the azimuth of 3278060_2 by 36 degrees
- `C4`: Press down the tilt angle  of 3278060_2 by 9 degrees
- `C5`: Adjust the azimuth of 3235610_1 by 34 degrees
- `C6`: Decrease A3 Offset threshold for 3266895_4
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3235610_1
- `C8`: Add neighbor relationship between 3235610_1 and 3266895_4
- `C9`: Increase A3 Offset threshold for 3235610_1
- `C10`: Decrease transmission power for 3235610_1
- `C11`: Increase transmission power for 3266895_4
- `C12`: Lift the tilt angle of 3235610_1 by 6 degrees
- `C13`: Lift the tilt angle  of 3278060_2 by 9 degrees
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3266895_4
- `C15`: Check test server and transmission issues
- `C16`: Increase A3 Offset threshold for 3266895_4
- `C17`: Increase transmission power for 3235610_1
- `C18`: Decrease transmission power for 3266895_4
- `C19`: Decrease A3 Offset threshold for 3235610_1
- `C20`: Insufficient data; more data is needed for judgment.
- `C21`: Press down the tilt angle of 3235610_1 by 6 degrees
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3235610_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.374 | MS1 | 121.4656732769 | 31.1446237647 | 65 | 504990 | -89.32 | 17.14 | 492.11 | 0.07 | 2.01 | 1599 |
| 2024-09-20 22:21:32.378 | MS1 | 121.4656699430 | 31.1446203243 | 65 | 504990 | -85.39 | 16.37 | 491.13 | 0.17 | 2.02 | 1599 |
| 2024-09-20 22:21:33.562 | MS1 | 121.4656771128 | 31.1446225154 | 65 | 504990 | -91.58 | 15.54 | 550.59 | 0.15 | 2.52 | 1597 |
| 2024-09-20 22:21:34.126 | MS1 | 121.4656614753 | 31.1446218702 | 65 | 504990 | -89.13 | 13.33 | 93.50 | 0.05 | 2.91 | 1568 |
| 2024-09-20 22:21:35.710 | MS1 | 121.4656733467 | 31.1446310537 | 65 | 504990 | -89.65 | 15.54 | 68.02 | 0.04 | 2.18 | 1591 |
| 2024-09-20 22:21:36.362 | MS1 | 121.4656707634 | 31.1446201211 | 65 | 504990 | -90.52 | 13.35 | 89.31 | 0.20 | 2.36 | 1561 |
| 2024-09-20 22:21:37.464 | MS1 | 121.4656697935 | 31.1446267207 | 65 | 504990 | -92.97 | 7.75 | 76.65 | 0.08 | 2.29 | 1565 |
| 2024-09-20 22:21:38.143 | MS1 | 121.4656648097 | 31.1446365386 | 65 | 504990 | -91.69 | 11.15 | 85.31 | 0.08 | 2.69 | 1600 |
| 2024-09-20 22:21:39.566 | MS1 | 121.4656610175 | 31.1446274535 | 65 | 504990 | -91.09 | 12.21 | 70.10 | 0.02 | 2.15 | 1563 |
| 2024-09-20 22:21:40.938 | MS1 | 121.4656680731 | 31.1446231678 | 65 | 504990 | -90.70 | 7.73 | 475.37 | 0.11 | 2.04 | 1570 |
| 2024-09-20 22:21:41.289 | MS1 | 121.4656743647 | 31.1446324444 | 65 | 504990 | -92.95 | 8.96 | 408.86 | 0.18 | 2.17 | 1590 |
| 2024-09-20 22:21:42.140 | MS1 | 121.4656733064 | 31.1446349799 | 65 | 504990 | -90.10 | 9.81 | 609.65 | 0.18 | 2.85 | 1589 |

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
| 3216518 | 3 | 121.4680067541 | 31.1454793899 | 170 | 14 | 7 | 29.9 | TDD | 181 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3235610 | 1 | 121.4716537668 | 31.1476602974 | 205 | 2 | 2 | 41.5 | TDD | 65 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3266895 | 4 | 121.4737042241 | 31.1528430955 | 256 | 8 | 0 | 22.4 | TDD | 367 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3278060 | 2 | 121.4666531142 | 31.1528973373 | 67 | 14 | 1 | 46.9 | TDD | 915 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |

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
| 2024-09-20 22:21:31.030 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.050 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.179 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.179 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.881 | NREventA3 | measId:2;ServCellPCI:607;Se... |
| 2024-09-20 22:21:38.121 | NRHandoverAttempt | SourcePCI:607;SourceNR-ARFC... |
| 2024-09-20 22:21:38.152 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.163 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.276 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.276 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3235610 | 1 | 92.0305 | 87.0156 | -116.1972 | 8.4620 | 183.5310 | 0.0033 | 0.0011 |
| 2024_09_20 22:00 | 3278060 | 2 | 10.9420 | 11.0125 | -114.3875 | 11.8702 | 98.8276 | 0.0046 | 0.0147 |
| 2024_09_20 22:00 | 3216518 | 3 | 19.0122 | 19.2928 | -114.2896 | 13.4426 | 189.2379 | 0.0167 | 0.0177 |
| 2024_09_20 22:00 | 3266895 | 4 | 8.4907 | 17.8007 | -114.1735 | 13.5736 | 174.1863 | 0.0159 | 0.0178 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415302_41A3CAE1 | 504990 | 65 | -90.2 | 504990 | 367 | -93.1 | 504990 | 915 | -100.8 | 504990 | 181 |
| MR_1774415302_013ACD13 | 504990 | 65 | -87.2 | 504990 | 367 | -94.5 | 504990 | 915 | -97.9 | 504990 | 181 |
| MR_1774415302_69E84C7A | 504990 | 65 | -88.9 | 504990 | 367 | -94.0 | 504990 | 915 | -101.2 | 504990 | 181 |
| MR_1774415302_CF3F223F | 504990 | 65 | -88.9 | 504990 | 367 | -93.9 | 504990 | 915 | -98.0 | 504990 | 181 |
| MR_1774415302_F37E2DD5 | 504990 | 65 | -87.4 | 504990 | 367 | -94.4 | 504990 | 915 | -100.5 | 504990 | 181 |
| MR_1774415302_EF124AAB | 504990 | 65 | -91.1 | 504990 | 367 | -94.7 | 504990 | 915 | -98.6 | 504990 | 181 |
| MR_1774415302_2F6499D7 | 504990 | 65 | -87.7 | 504990 | 367 | -92.3 | 504990 | 915 | -99.5 | 504990 | 181 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 179: `3fc6dd90-c8f...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `3fc6dd90-c8f7-4982-9713-83fcb66acde5` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[179] topology](images/test_0179.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3222614_2
- `C2`: Add neighbor relationship between 3222766_3 and 3241677_1
- `C3`: Adjust the azimuth of 3222614_2 by 43 degrees
- `C4`: Check test server and transmission issues
- `C5`: Decrease transmission power for 3241677_1
- `C6`: Decrease A3 Offset threshold for 3222614_2
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3222614_2
- `C8`: Press down the tilt angle  of 3222766_3 by 10 degrees
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3241677_1
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3241677_1
- `C11`: Decrease transmission power for 3222614_2
- `C12`: Lift the tilt angle of 3222614_2 by 5 degrees
- `C13`: Increase transmission power for 3222614_2
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Increase transmission power for 3241677_1
- `C16`: Press down the tilt angle of 3222614_2 by 5 degrees
- `C17`: Increase A3 Offset threshold for 3222614_2
- `C18`: Decrease A3 Offset threshold for 3241677_1
- `C19`: Increase A3 Offset threshold for 3241677_1
- `C20`: Add neighbor relationship between 3222614_2 and 3241677_1
- `C21`: Adjust the azimuth of 3222766_3 by 50 degrees
- `C22`: Lift the tilt angle  of 3222766_3 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.101 | MS1 | 121.4656761601 | 31.1446329638 | 119 | 504990 | -87.32 | 12.97 | 428.80 | 0.18 | 2.52 | 1596 |
| 2024-09-20 22:21:32.504 | MS1 | 121.4656708672 | 31.1446213500 | 119 | 504990 | -87.60 | 17.11 | 485.32 | 0.17 | 2.57 | 1567 |
| 2024-09-20 22:21:33.374 | MS1 | 121.4656759623 | 31.1446208676 | 119 | 504990 | -86.64 | 16.71 | 591.85 | 0.04 | 2.53 | 1581 |
| 2024-09-20 22:21:34.386 | MS1 | 121.4656588608 | 31.1446300344 | 119 | 504990 | -90.14 | 17.72 | 79.54 | 0.07 | 2.50 | 1577 |
| 2024-09-20 22:21:35.763 | MS1 | 121.4656598267 | 31.1446336391 | 119 | 504990 | -87.22 | 13.82 | 83.26 | 0.11 | 2.95 | 1599 |
| 2024-09-20 22:21:36.418 | MS1 | 121.4656763390 | 31.1446261493 | 119 | 504990 | -86.41 | 16.77 | 90.12 | 0.13 | 2.86 | 1566 |
| 2024-09-20 22:21:37.655 | MS1 | 121.4656667267 | 31.1446189138 | 119 | 504990 | -90.63 | 10.31 | 72.50 | 0.13 | 2.91 | 1597 |
| 2024-09-20 22:21:38.544 | MS1 | 121.4656672420 | 31.1446223451 | 119 | 504990 | -90.87 | 7.44 | 94.96 | 0.19 | 2.19 | 1576 |
| 2024-09-20 22:21:39.751 | MS1 | 121.4656697078 | 31.1446285832 | 119 | 504990 | -91.49 | 9.26 | 63.87 | 0.18 | 2.74 | 1582 |
| 2024-09-20 22:21:40.209 | MS1 | 121.4656670111 | 31.1446203199 | 119 | 504990 | -93.26 | 10.72 | 444.30 | 0.00 | 2.98 | 1576 |
| 2024-09-20 22:21:41.531 | MS1 | 121.4656659814 | 31.1446299357 | 119 | 504990 | -93.72 | 7.19 | 423.79 | 0.08 | 2.00 | 1591 |
| 2024-09-20 22:21:42.150 | MS1 | 121.4656745272 | 31.1446308009 | 119 | 504990 | -90.12 | 7.77 | 519.09 | 0.02 | 2.96 | 1589 |

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
| 3222614 | 2 | 121.4674263719 | 31.1550216017 | 145 | 3 | 5 | 31.1 | TDD | 119 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3222766 | 3 | 121.4678426526 | 31.1446735388 | 350 | 9 | 8 | 35.6 | TDD | 421 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3225874 | 4 | 121.4707499313 | 31.1540065767 | 183 | 8 | 11 | 19.1 | TDD | 871 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3241677 | 1 | 121.4655464761 | 31.1518869138 | 276 | 11 | 12 | 46.6 | TDD | 851 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |

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
| 2024-09-20 22:21:31.249 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.266 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.393 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.393 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.078 | NREventA3 | measId:2;ServCellPCI:972;Se... |
| 2024-09-20 22:21:38.318 | NRHandoverAttempt | SourcePCI:972;SourceNR-ARFC... |
| 2024-09-20 22:21:38.350 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.365 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.492 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.492 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3241677 | 1 | 14.1242 | 10.2810 | -117.8319 | 9.6134 | 153.8657 | 0.0030 | 0.0073 |
| 2024_09_20 22:00 | 3222614 | 2 | 77.3671 | 84.8175 | -117.6936 | 6.2293 | 194.2210 | 0.0021 | 0.0037 |
| 2024_09_20 22:00 | 3222766 | 3 | 13.1434 | 12.4482 | -117.4381 | 16.1743 | 103.0216 | 0.0043 | 0.0005 |
| 2024_09_20 22:00 | 3225874 | 4 | 12.8374 | 15.6471 | -116.4967 | 18.3440 | 159.5484 | 0.0075 | 0.0177 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415124_D71E7C1C | 504990 | 119 | -88.8 | 504990 | 851 | -93.2 | 504990 | 421 | -97.6 | 504990 | 871 |
| MR_1774415124_56266E2C | 504990 | 119 | -91.8 | 504990 | 851 | -94.3 | 504990 | 421 | -98.3 | 504990 | 871 |
| MR_1774415124_10D6D84D | 504990 | 119 | -89.4 | 504990 | 851 | -91.0 | 504990 | 421 | -98.4 | 504990 | 871 |
| MR_1774415124_6843EADD | 504990 | 119 | -90.4 | 504990 | 851 | -91.5 | 504990 | 421 | -96.6 | 504990 | 871 |
| MR_1774415124_918B83DD | 504990 | 119 | -90.7 | 504990 | 851 | -94.7 | 504990 | 421 | -97.7 | 504990 | 871 |
| MR_1774415124_F79EB203 | 504990 | 119 | -89.7 | 504990 | 851 | -92.7 | 504990 | 421 | -98.3 | 504990 | 871 |
| MR_1774415124_DAC946D8 | 504990 | 119 | -91.2 | 504990 | 851 | -93.6 | 504990 | 421 | -99.2 | 504990 | 871 |
| MR_1774415124_256B20EB | 504990 | 119 | -90.9 | 504990 | 851 | -91.4 | 504990 | 421 | -96.6 | 504990 | 871 |

> *... 2개 열 생략 (전체 14열)*

---
