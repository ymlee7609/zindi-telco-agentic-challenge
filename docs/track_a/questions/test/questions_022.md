# Track A 문제 분석 — test[210]~test[219]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/test.json`
> 범위: test[210] ~ test[219] (10개)

## 목차

1. [문제 210: `3f2036ca-163...`](#210) — single-answer
2. [문제 211: `a778a705-e92...`](#211) — single-answer
3. [문제 212: `542b638a-484...`](#212) — single-answer
4. [문제 213: `3febfe40-bc4...`](#213) — single-answer
5. [문제 214: `03bf382e-b3b...`](#214) — single-answer
6. [문제 215: `bd11e64e-ed0...`](#215) — single-answer
7. [문제 216: `2c5f5b73-426...`](#216) — single-answer
8. [문제 217: `7a44dd46-f96...`](#217) — single-answer
9. [문제 218: `59be7f74-123...`](#218) — single-answer
10. [문제 219: `73db8c81-a46...`](#219) — single-answer

---

### 문제 210: `3f2036ca-163...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `3f2036ca-1638-408d-b704-90aeff6a2b6d` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[210] topology](images/test_0210.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3238870_2 by 50 degrees
- `C2`: Increase transmission power for 3262157_1
- `C3`: Lift the tilt angle  of 3262157_1 by 5 degrees
- `C4`: Decrease A3 Offset threshold for 3262157_1
- `C5`: Decrease A3 Offset threshold for 3238870_2
- `C6`: Adjust the azimuth of 3262157_1 by 50 degrees
- `C7`: Lift the tilt angle of 3238870_2 by 7 degrees
- `C8`: Press down the tilt angle of 3238870_2 by 7 degrees
- `C9`: Increase transmission power for 3238870_2
- `C10`: Check test server and transmission issues
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3238870_2
- `C12`: Add neighbor relationship between 3238870_2 and 3262157_1
- `C13`: Increase A3 Offset threshold for 3262157_1
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Decrease transmission power for 3238870_2
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3262157_1
- `C17`: Add neighbor relationship between 3252387_4 and 3262157_1
- `C18`: Decrease transmission power for 3262157_1
- `C19`: Press down the tilt angle  of 3262157_1 by 5 degrees
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3238870_2
- `C21`: Increase A3 Offset threshold for 3238870_2
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3262157_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.303 | MS1 | 121.4656729705 | 31.1446279977 | 532 | 504990 | -75.72 | 16.67 | 580.54 | 0.03 | 2.33 | 1586 |
| 2024-09-20 22:21:32.119 | MS1 | 121.4656686399 | 31.1446220547 | 532 | 504990 | -75.04 | 12.97 | 360.85 | 0.10 | 2.66 | 1582 |
| 2024-09-20 22:21:33.753 | MS1 | 121.4656773185 | 31.1446203777 | 532 | 504990 | -83.88 | 17.15 | 579.20 | 0.09 | 2.52 | 1581 |
| 2024-09-20 22:21:34.644 | MS1 | 121.4656762737 | 31.1446355779 | 532 | 504990 | -92.36 | -2.72 | 51.38 | 0.01 | 1.43 | 1566 |
| 2024-09-20 22:21:35.135 | MS1 | 121.4656619924 | 31.1446203622 | 532 | 504990 | -91.07 | -0.99 | 48.59 | 0.08 | 1.15 | 1591 |
| 2024-09-20 22:21:36.975 | MS1 | 121.4656727577 | 31.1446292063 | 532 | 504990 | -88.94 | -2.63 | 68.98 | 0.08 | 1.07 | 1561 |
| 2024-09-20 22:21:37.996 | MS1 | 121.4656637439 | 31.1446239880 | 532 | 504990 | -94.75 | -0.00 | 66.03 | 0.09 | 1.39 | 1569 |
| 2024-09-20 22:21:38.221 | MS1 | 121.4656757792 | 31.1446322472 | 532 | 504990 | -77.81 | 16.34 | 429.29 | 0.19 | 1.40 | 1575 |
| 2024-09-20 22:21:39.514 | MS1 | 121.4656745727 | 31.1446365881 | 532 | 504990 | -79.04 | 14.76 | 458.52 | 0.01 | 1.21 | 1568 |
| 2024-09-20 22:21:40.663 | MS1 | 121.4656596960 | 31.1446291730 | 532 | 504990 | -75.84 | 17.58 | 441.78 | 0.01 | 2.50 | 1595 |
| 2024-09-20 22:21:41.392 | MS1 | 121.4656756774 | 31.1446260073 | 532 | 504990 | -84.29 | 12.11 | 472.08 | 0.05 | 2.42 | 1572 |
| 2024-09-20 22:21:42.529 | MS1 | 121.4656616949 | 31.1446369646 | 532 | 504990 | -84.83 | 15.90 | 423.26 | 0.01 | 2.57 | 1563 |

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
| 3238870 | 2 | 121.4683443437 | 31.1513621900 | 252 | 4 | 4 | 48.3 | TDD | 532 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3241256 | 3 | 121.4756037600 | 31.1484369781 | 230 | 1 | 2 | 33.8 | TDD | 1 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3252387 | 4 | 121.4729422128 | 31.1551055351 | 147 | 15 | 11 | 39.8 | TDD | 639 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3262157 | 1 | 121.4709306316 | 31.1532276569 | 158 | 4 | 4 | 22.7 | TDD | 985 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:31.500 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.520 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.633 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.633 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.376 | NREventA3 | measId:2;ServCellPCI:983;Se... |
| 2024-09-20 22:21:36.376 | NREventA3 | measId:2;ServCellPCI:983;Se... |
| 2024-09-20 22:21:37.376 | NREventA3 | measId:2;ServCellPCI:983;Se... |
| 2024-09-20 22:21:39.876 | NRRRCReestablishAttempt | PCI:983 |
| 2024-09-20 22:21:39.893 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.905 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:40.031 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:40.031 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3262157 | 1 | 6.9781 | 17.8649 | -114.7808 | 11.4261 | 92.5366 | 0.0176 | 0.0053 |
| 2024_09_20 22:00 | 3238870 | 2 | 17.8235 | 10.9475 | -114.6082 | 13.5484 | 145.8302 | 0.0133 | 0.1367 |
| 2024_09_20 22:00 | 3241256 | 3 | 15.6869 | 14.5359 | -114.4658 | 18.0046 | 124.4231 | 0.0095 | 0.0180 |
| 2024_09_20 22:00 | 3252387 | 4 | 12.8633 | 8.2414 | -117.9577 | 9.7316 | 133.9042 | 0.0093 | 0.0007 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416155_2DDB7B13 | 504990 | 532 | -92.6 | 504990 | 985 | -86.0 | 504990 | 639 | -93.2 | 504990 | 1 |
| MR_1774416155_C2874D2E | 504990 | 985 | -87.4 | 504990 | 532 | -91.5 | 504990 | 639 | -92.1 | 504990 | 1 |
| MR_1774416155_1D512DD3 | 504990 | 985 | -85.6 | 504990 | 532 | -91.1 | 504990 | 639 | -93.0 | 504990 | 1 |
| MR_1774416155_43FD0159 | 504990 | 532 | -94.3 | 504990 | 985 | -87.3 | 504990 | 639 | -93.0 | 504990 | 1 |
| MR_1774416155_34061E6C | 504990 | 532 | -92.7 | 504990 | 985 | -87.8 | 504990 | 639 | -91.5 | 504990 | 1 |
| MR_1774416155_44F6CD07 | 504990 | 532 | -92.6 | 504990 | 985 | -86.0 | 504990 | 639 | -92.2 | 504990 | 1 |
| MR_1774416155_FEC6D5C9 | 504990 | 985 | -85.4 | 504990 | 532 | -92.9 | 504990 | 639 | -90.6 | 504990 | 1 |
| MR_1774416155_20BB76E3 | 504990 | 532 | -91.0 | 504990 | 985 | -85.1 | 504990 | 639 | -93.5 | 504990 | 1 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 211: `a778a705-e92...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `a778a705-e927-49bd-8053-747b56802869` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[211] topology](images/test_0211.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3252200_2 and 3248329_3
- `C2`: Insufficient data; more data is needed for judgment.
- `C3`: Decrease A3 Offset threshold for 3252200_2
- `C4`: Decrease transmission power for 3248329_3
- `C5`: Adjust the azimuth of 3248329_3 by 15 degrees
- `C6`: Press down the tilt angle  of 3248329_3 by 6 degrees
- `C7`: Decrease transmission power for 3252200_2
- `C8`: Adjust the azimuth of 3252200_2 by 50 degrees
- `C9`: Decrease A3 Offset threshold for 3248329_3
- `C10`: Increase A3 Offset threshold for 3252200_2
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3252200_2
- `C12`: Lift the tilt angle of 3252200_2 by 10 degrees
- `C13`: Check test server and transmission issues
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3248329_3
- `C15`: Add neighbor relationship between 3215205_1 and 3248329_3
- `C16`: Lift the tilt angle  of 3248329_3 by 6 degrees
- `C17`: Press down the tilt angle of 3252200_2 by 10 degrees
- `C18`: Increase A3 Offset threshold for 3248329_3
- `C19`: Increase transmission power for 3248329_3
- `C20`: Increase transmission power for 3252200_2
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3248329_3
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3252200_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.354 | MS1 | 121.4656642143 | 31.1446366820 | 837 | 504990 | -79.48 | 17.83 | 413.16 | 0.06 | 2.36 | 1569 |
| 2024-09-20 22:21:32.186 | MS1 | 121.4656699698 | 31.1446301887 | 837 | 504990 | -84.19 | 17.68 | 511.33 | 0.03 | 2.40 | 1575 |
| 2024-09-20 22:21:33.395 | MS1 | 121.4656687027 | 31.1446339541 | 837 | 504990 | -78.89 | 16.58 | 566.26 | 0.09 | 2.71 | 1584 |
| 2024-09-20 22:21:34.420 | MS1 | 121.4656724698 | 31.1446376187 | 837 | 504990 | -92.42 | -2.07 | 48.04 | 0.09 | 1.06 | 1578 |
| 2024-09-20 22:21:35.853 | MS1 | 121.4656735938 | 31.1446220254 | 837 | 504990 | -90.53 | -2.60 | 49.05 | 0.15 | 1.16 | 1596 |
| 2024-09-20 22:21:36.690 | MS1 | 121.4656762076 | 31.1446271744 | 837 | 504990 | -93.45 | -1.50 | 64.74 | 0.14 | 1.28 | 1599 |
| 2024-09-20 22:21:37.608 | MS1 | 121.4656635599 | 31.1446342791 | 837 | 504990 | -89.62 | -2.10 | 45.34 | 0.09 | 1.24 | 1591 |
| 2024-09-20 22:21:38.293 | MS1 | 121.4656652652 | 31.1446257847 | 837 | 504990 | -75.32 | 12.79 | 451.59 | 0.20 | 1.08 | 1569 |
| 2024-09-20 22:21:39.577 | MS1 | 121.4656652559 | 31.1446360862 | 837 | 504990 | -77.39 | 13.06 | 463.17 | 0.00 | 1.21 | 1572 |
| 2024-09-20 22:21:40.311 | MS1 | 121.4656613076 | 31.1446358439 | 837 | 504990 | -79.95 | 12.17 | 547.65 | 0.03 | 2.69 | 1572 |
| 2024-09-20 22:21:41.813 | MS1 | 121.4656727274 | 31.1446308975 | 837 | 504990 | -84.99 | 12.20 | 499.44 | 0.01 | 2.61 | 1599 |
| 2024-09-20 22:21:42.455 | MS1 | 121.4656680648 | 31.1446218243 | 837 | 504990 | -77.29 | 15.43 | 418.21 | 0.18 | 2.05 | 1574 |

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
| 3215205 | 1 | 121.4733191895 | 31.1474363952 | 325 | 7 | 12 | 37.1 | TDD | 892 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3248329 | 3 | 121.4753513544 | 31.1464314607 | 273 | 3 | 3 | 46.3 | TDD | 397 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3252200 | 2 | 121.4736358658 | 31.1507859842 | 20 | 9 | 1 | 26.4 | TDD | 837 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3271709 | 4 | 121.4712389310 | 31.1451736325 | 65 | 7 | 3 | 26.6 | TDD | 52 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |

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
| 2024-09-20 22:21:31.422 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.444 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.564 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.564 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.243 | NREventA3 | measId:2;ServCellPCI:31;Ser... |
| 2024-09-20 22:21:36.243 | NREventA3 | measId:2;ServCellPCI:31;Ser... |
| 2024-09-20 22:21:37.243 | NREventA3 | measId:2;ServCellPCI:31;Ser... |
| 2024-09-20 22:21:39.743 | NRRRCReestablishAttempt | PCI:31 |
| 2024-09-20 22:21:39.754 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.767 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:39.911 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.911 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3215205 | 1 | 19.4675 | 10.7333 | -115.7625 | 17.4097 | 131.9776 | 0.0124 | 0.0033 |
| 2024_09_20 22:00 | 3252200 | 2 | 14.3688 | 8.3514 | -116.9621 | 18.3568 | 163.6955 | 0.0060 | 0.1521 |
| 2024_09_20 22:00 | 3248329 | 3 | 19.0052 | 13.5586 | -117.4318 | 9.5808 | 110.1318 | 0.0188 | 0.0096 |
| 2024_09_20 22:00 | 3271709 | 4 | 14.9154 | 14.8161 | -115.0279 | 14.4428 | 126.8636 | 0.0102 | 0.0127 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416203_AB45005D | 504990 | 837 | -92.5 | 504990 | 397 | -86.2 | 504990 | 892 | -96.6 | 504990 | 52 |
| MR_1774416203_B0554EA7 | 504990 | 397 | -87.2 | 504990 | 837 | -94.2 | 504990 | 892 | -95.4 | 504990 | 52 |
| MR_1774416203_4A337107 | 504990 | 837 | -92.1 | 504990 | 397 | -87.6 | 504990 | 892 | -93.7 | 504990 | 52 |
| MR_1774416203_85182797 | 504990 | 837 | -92.7 | 504990 | 397 | -88.7 | 504990 | 892 | -96.6 | 504990 | 52 |
| MR_1774416203_3DDFCEDB | 504990 | 837 | -90.7 | 504990 | 397 | -88.4 | 504990 | 892 | -95.2 | 504990 | 52 |
| MR_1774416203_DE40DD8E | 504990 | 837 | -92.8 | 504990 | 397 | -86.5 | 504990 | 892 | -95.0 | 504990 | 52 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 212: `542b638a-484...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `542b638a-4845-46a4-a772-bc8da935fd28` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[212] topology](images/test_0212.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment.
- `C2`: Adjust the azimuth of 3242706_3 by 10 degrees
- `C3`: Increase transmission power for 3242706_3
- `C4`: Decrease transmission power for 3223797_1
- `C5`: Lift the tilt angle  of 3242706_3 by 5 degrees
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3242706_3
- `C7`: Decrease A3 Offset threshold for 3242706_3
- `C8`: Add neighbor relationship between 3246663_2 and 3242706_3
- `C9`: Increase A3 Offset threshold for 3242706_3
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3223797_1
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3242706_3
- `C12`: Increase A3 Offset threshold for 3223797_1
- `C13`: Press down the tilt angle of 3223797_1 by 10 degrees
- `C14`: Press down the tilt angle  of 3242706_3 by 5 degrees
- `C15`: Check test server and transmission issues
- `C16`: Decrease transmission power for 3242706_3
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3223797_1
- `C18`: Increase transmission power for 3223797_1
- `C19`: Add neighbor relationship between 3223797_1 and 3242706_3
- `C20`: Adjust the azimuth of 3223797_1 by 50 degrees
- `C21`: Lift the tilt angle of 3223797_1 by 10 degrees
- `C22`: Decrease A3 Offset threshold for 3223797_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.295 | MS1 | 121.4656766051 | 31.1446336782 | 410 | 504990 | -76.00 | 17.49 | 522.69 | 0.19 | 2.07 | 1567 |
| 2024-09-20 22:21:32.573 | MS1 | 121.4656629872 | 31.1446348981 | 410 | 504990 | -77.25 | 17.13 | 354.34 | 0.08 | 2.22 | 1582 |
| 2024-09-20 22:21:33.539 | MS1 | 121.4656696704 | 31.1446210040 | 410 | 504990 | -77.87 | 13.70 | 571.89 | 0.12 | 2.53 | 1571 |
| 2024-09-20 22:21:34.456 | MS1 | 121.4656683177 | 31.1446363850 | 410 | 504990 | -87.15 | -2.67 | 49.52 | 0.20 | 1.32 | 1590 |
| 2024-09-20 22:21:35.390 | MS1 | 121.4656720846 | 31.1446305014 | 410 | 504990 | -94.82 | -1.61 | 56.42 | 0.13 | 1.34 | 1560 |
| 2024-09-20 22:21:36.119 | MS1 | 121.4656777145 | 31.1446225792 | 410 | 504990 | -88.36 | -2.86 | 60.72 | 0.16 | 1.19 | 1564 |
| 2024-09-20 22:21:37.830 | MS1 | 121.4656767029 | 31.1446233921 | 410 | 504990 | -86.44 | -1.51 | 43.61 | 0.01 | 1.03 | 1568 |
| 2024-09-20 22:21:38.213 | MS1 | 121.4656593820 | 31.1446247540 | 410 | 504990 | -78.45 | 17.50 | 323.02 | 0.09 | 1.28 | 1572 |
| 2024-09-20 22:21:39.478 | MS1 | 121.4656627009 | 31.1446330456 | 410 | 504990 | -82.15 | 17.29 | 495.92 | 0.13 | 1.13 | 1560 |
| 2024-09-20 22:21:40.544 | MS1 | 121.4656607593 | 31.1446361757 | 410 | 504990 | -83.74 | 15.56 | 419.34 | 0.14 | 2.76 | 1568 |
| 2024-09-20 22:21:41.161 | MS1 | 121.4656778662 | 31.1446336835 | 410 | 504990 | -84.57 | 14.91 | 318.80 | 0.14 | 2.81 | 1575 |
| 2024-09-20 22:21:42.817 | MS1 | 121.4656740442 | 31.1446328147 | 410 | 504990 | -79.41 | 12.55 | 436.16 | 0.15 | 2.03 | 1580 |

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
| 3223275 | 4 | 121.4646044665 | 31.1458594558 | 231 | 2 | 8 | 25.7 | TDD | 574 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3223797 | 1 | 121.4697003918 | 31.1498978665 | 344 | 7 | 11 | 33.0 | TDD | 410 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3242706 | 3 | 121.4695355106 | 31.1472072161 | 222 | 1 | 3 | 34.5 | TDD | 677 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3246663 | 2 | 121.4750972082 | 31.1475167296 | 104 | 6 | 10 | 42.2 | TDD | 723 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

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
| 2024-09-20 22:21:31.289 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.309 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.419 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.419 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.169 | NREventA3 | measId:2;ServCellPCI:860;Se... |
| 2024-09-20 22:21:36.169 | NREventA3 | measId:2;ServCellPCI:860;Se... |
| 2024-09-20 22:21:37.169 | NREventA3 | measId:2;ServCellPCI:860;Se... |
| 2024-09-20 22:21:39.669 | NRRRCReestablishAttempt | PCI:860 |
| 2024-09-20 22:21:39.683 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.693 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:39.821 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.821 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3223797 | 1 | 11.9403 | 18.3595 | -116.8950 | 18.7873 | 189.6815 | 0.0118 | 0.1699 |
| 2024_09_20 22:00 | 3246663 | 2 | 19.6575 | 15.1636 | -115.8638 | 17.6163 | 98.5349 | 0.0127 | 0.0200 |
| 2024_09_20 22:00 | 3242706 | 3 | 11.5534 | 9.9392 | -115.4256 | 10.0371 | 101.6798 | 0.0128 | 0.0153 |
| 2024_09_20 22:00 | 3223275 | 4 | 10.3562 | 19.4176 | -115.8515 | 12.8617 | 135.5794 | 0.0091 | 0.0017 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412079_71A4150A | 504990 | 410 | -86.6 | 504990 | 677 | -82.8 | 504990 | 723 | -93.2 | 504990 | 574 |
| MR_1774412079_1AE88EF7 | 504990 | 410 | -89.1 | 504990 | 677 | -84.0 | 504990 | 723 | -91.9 | 504990 | 574 |
| MR_1774412079_D917CC88 | 504990 | 677 | -80.9 | 504990 | 410 | -87.8 | 504990 | 723 | -92.4 | 504990 | 574 |
| MR_1774412079_B577C2C2 | 504990 | 410 | -86.1 | 504990 | 677 | -81.0 | 504990 | 723 | -92.2 | 504990 | 574 |
| MR_1774412079_99BBEA44 | 504990 | 410 | -87.3 | 504990 | 677 | -84.5 | 504990 | 723 | -92.0 | 504990 | 574 |
| MR_1774412079_7E310568 | 504990 | 410 | -88.5 | 504990 | 677 | -84.0 | 504990 | 723 | -93.1 | 504990 | 574 |
| MR_1774412079_31039A0E | 504990 | 410 | -88.1 | 504990 | 677 | -81.3 | 504990 | 723 | -90.6 | 504990 | 574 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 213: `3febfe40-bc4...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `3febfe40-bc43-4dde-b9ac-f4a67d2c1d6c` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[213] topology](images/test_0213.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3231963_1
- `C2`: Decrease transmission power for 3231963_1
- `C3`: Decrease A3 Offset threshold for 3274793_2
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3274793_2
- `C5`: Add neighbor relationship between 3256953_4 and 3274793_2
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3231963_1
- `C7`: Insufficient data; more data is needed for judgment.
- `C8`: Press down the tilt angle of 3231963_1 by 5 degrees
- `C9`: Increase transmission power for 3231963_1
- `C10`: Press down the tilt angle  of 3274793_2 by 6 degrees
- `C11`: Increase A3 Offset threshold for 3231963_1
- `C12`: Check test server and transmission issues
- `C13`: Increase transmission power for 3274793_2
- `C14`: Add neighbor relationship between 3231963_1 and 3274793_2
- `C15`: Lift the tilt angle of 3231963_1 by 5 degrees
- `C16`: Lift the tilt angle  of 3274793_2 by 6 degrees
- `C17`: Increase A3 Offset threshold for 3274793_2
- `C18`: Decrease transmission power for 3274793_2
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3274793_2
- `C20`: Adjust the azimuth of 3274793_2 by 50 degrees
- `C21`: Decrease A3 Offset threshold for 3231963_1
- `C22`: Adjust the azimuth of 3231963_1 by 50 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.455 | MS1 | 121.4656647570 | 31.1446312099 | 152 | 504990 | -88.75 | 16.96 | 528.06 | 0.16 | 2.36 | 1586 |
| 2024-09-20 22:21:32.426 | MS1 | 121.4656626902 | 31.1446195123 | 152 | 504990 | -89.49 | 12.04 | 512.56 | 0.09 | 2.76 | 1578 |
| 2024-09-20 22:21:33.917 | MS1 | 121.4656614490 | 31.1446291211 | 152 | 504990 | -90.29 | 16.91 | 486.08 | 0.04 | 2.68 | 1591 |
| 2024-09-20 22:21:34.438 | MS1 | 121.4656604385 | 31.1446195388 | 152 | 504990 | -91.93 | 14.08 | 66.57 | 0.20 | 2.47 | 493 |
| 2024-09-20 22:21:35.362 | MS1 | 121.4656652254 | 31.1446323763 | 152 | 504990 | -89.00 | 14.05 | 72.36 | 0.04 | 2.78 | 422 |
| 2024-09-20 22:21:36.290 | MS1 | 121.4656707764 | 31.1446291270 | 152 | 504990 | -85.96 | 13.73 | 49.84 | 0.11 | 2.78 | 441 |
| 2024-09-20 22:21:37.843 | MS1 | 121.4656662264 | 31.1446283171 | 152 | 504990 | -92.46 | 12.72 | 62.16 | 0.07 | 2.81 | 484 |
| 2024-09-20 22:21:38.906 | MS1 | 121.4656728922 | 31.1446215031 | 152 | 504990 | -93.78 | 8.27 | 64.55 | 0.11 | 2.49 | 409 |
| 2024-09-20 22:21:39.692 | MS1 | 121.4656706057 | 31.1446365251 | 152 | 504990 | -90.51 | 10.95 | 71.30 | 0.07 | 2.99 | 414 |
| 2024-09-20 22:21:40.177 | MS1 | 121.4656660075 | 31.1446303582 | 152 | 504990 | -89.87 | 7.44 | 371.76 | 0.15 | 2.64 | 1588 |
| 2024-09-20 22:21:41.828 | MS1 | 121.4656598267 | 31.1446288080 | 152 | 504990 | -92.24 | 10.95 | 532.53 | 0.17 | 2.97 | 1598 |
| 2024-09-20 22:21:42.526 | MS1 | 121.4656699926 | 31.1446200240 | 152 | 504990 | -89.69 | 12.73 | 431.27 | 0.16 | 2.07 | 1598 |

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
| 3228402 | 3 | 121.4665670304 | 31.1476984146 | 244 | 13 | 7 | 36.5 | TDD | 840 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3231963 | 1 | 121.4652773706 | 31.1472753595 | 355 | 2 | 0 | 17.4 | TDD | 152 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3256953 | 4 | 121.4647696959 | 31.1450220492 | 314 | 2 | 10 | 47.3 | TDD | 860 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3274793 | 2 | 121.4697346992 | 31.1553302969 | 51 | 5 | 10 | 19.0 | TDD | 370 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |

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
| 2024-09-20 22:21:31.143 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.168 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.290 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.290 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.001 | NREventA3 | measId:2;ServCellPCI:162;Se... |
| 2024-09-20 22:21:38.241 | NRHandoverAttempt | SourcePCI:162;SourceNR-ARFC... |
| 2024-09-20 22:21:38.282 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.293 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.400 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.400 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3231963 | 1 | 16.9388 | 9.4893 | -114.1586 | 6.4070 | 178.5313 | 0.0185 | 0.0170 |
| 2024_09_20 22:00 | 3274793 | 2 | 7.4439 | 6.0206 | -115.0772 | 15.2456 | 196.2015 | 0.0110 | 0.0011 |
| 2024_09_20 22:00 | 3228402 | 3 | 18.8927 | 11.8117 | -116.2916 | 16.9777 | 190.8964 | 0.0162 | 0.0043 |
| 2024_09_20 22:00 | 3256953 | 4 | 10.0307 | 9.1208 | -117.7578 | 8.0526 | 128.1365 | 0.0183 | 0.0089 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415877_A0410A00 | 504990 | 152 | -92.2 | 504990 | 370 | -93.5 | 504990 | 860 | -105.8 | 504990 | 840 |
| MR_1774415877_D325010B | 504990 | 152 | -92.8 | 504990 | 370 | -91.8 | 504990 | 860 | -107.9 | 504990 | 840 |
| MR_1774415877_AC80FD4A | 504990 | 152 | -90.7 | 504990 | 370 | -94.8 | 504990 | 860 | -108.8 | 504990 | 840 |
| MR_1774415877_093A6FDB | 504990 | 152 | -93.3 | 504990 | 370 | -92.3 | 504990 | 860 | -107.5 | 504990 | 840 |
| MR_1774415877_0A1EA8A6 | 504990 | 152 | -90.1 | 504990 | 370 | -93.5 | 504990 | 860 | -105.9 | 504990 | 840 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 214: `03bf382e-b3b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `03bf382e-b3b6-4673-b4b1-621f077694e2` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[214] topology](images/test_0214.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3256266_4 by 42 degrees
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3255770_3
- `C3`: Increase A3 Offset threshold for 3255770_3
- `C4`: Decrease transmission power for 3256266_4
- `C5`: Adjust the azimuth of 3253396_2 by 50 degrees
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3255770_3
- `C7`: Increase transmission power for 3255770_3
- `C8`: Lift the tilt angle  of 3253396_2 by 10 degrees
- `C9`: Add neighbor relationship between 3256266_4 and 3255770_3
- `C10`: Insufficient data; more data is needed for judgment.
- `C11`: Decrease A3 Offset threshold for 3255770_3
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3256266_4
- `C13`: Increase A3 Offset threshold for 3256266_4
- `C14`: Lift the tilt angle of 3256266_4 by 5 degrees
- `C15`: Press down the tilt angle of 3256266_4 by 5 degrees
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3256266_4
- `C17`: Decrease transmission power for 3255770_3
- `C18`: Press down the tilt angle  of 3253396_2 by 10 degrees
- `C19`: Add neighbor relationship between 3253396_2 and 3255770_3
- `C20`: Check test server and transmission issues
- `C21`: Increase transmission power for 3256266_4
- `C22`: Decrease A3 Offset threshold for 3256266_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.822 | MS1 | 121.4656752816 | 31.1446330679 | 119 | 504990 | -85.84 | 15.84 | 470.47 | 0.01 | 2.12 | 1591 |
| 2024-09-20 22:21:32.876 | MS1 | 121.4656615772 | 31.1446197982 | 119 | 504990 | -90.91 | 14.57 | 298.86 | 0.16 | 2.82 | 1584 |
| 2024-09-20 22:21:33.961 | MS1 | 121.4656670136 | 31.1446324515 | 119 | 504990 | -90.77 | 14.60 | 442.36 | 0.03 | 2.37 | 1583 |
| 2024-09-20 22:21:34.651 | MS1 | 121.4656746706 | 31.1446214937 | 119 | 504990 | -89.76 | 12.68 | 60.65 | 0.10 | 2.89 | 1565 |
| 2024-09-20 22:21:35.704 | MS1 | 121.4656631619 | 31.1446331196 | 119 | 504990 | -91.13 | 15.12 | 54.24 | 0.09 | 2.06 | 1589 |
| 2024-09-20 22:21:36.501 | MS1 | 121.4656748760 | 31.1446300217 | 119 | 504990 | -87.43 | 15.80 | 95.10 | 0.16 | 2.87 | 1590 |
| 2024-09-20 22:21:37.507 | MS1 | 121.4656721961 | 31.1446274434 | 119 | 504990 | -89.31 | 10.85 | 60.63 | 0.03 | 2.94 | 1599 |
| 2024-09-20 22:21:38.812 | MS1 | 121.4656648924 | 31.1446331188 | 119 | 504990 | -89.33 | 11.27 | 61.50 | 0.02 | 2.84 | 1588 |
| 2024-09-20 22:21:39.829 | MS1 | 121.4656583743 | 31.1446339974 | 119 | 504990 | -91.55 | 12.44 | 78.72 | 0.02 | 2.22 | 1579 |
| 2024-09-20 22:21:40.404 | MS1 | 121.4656775223 | 31.1446273484 | 119 | 504990 | -89.64 | 10.81 | 357.05 | 0.11 | 2.31 | 1592 |
| 2024-09-20 22:21:41.508 | MS1 | 121.4656637215 | 31.1446261396 | 119 | 504990 | -89.15 | 11.12 | 343.83 | 0.17 | 2.08 | 1575 |
| 2024-09-20 22:21:42.121 | MS1 | 121.4656669151 | 31.1446208165 | 119 | 504990 | -92.39 | 11.58 | 506.17 | 0.03 | 2.76 | 1571 |

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
| 3222755 | 1 | 121.4737162150 | 31.1523030879 | 7 | 2 | 3 | 37.1 | TDD | 185 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3253396 | 2 | 121.4758196972 | 31.1516802000 | 318 | 15 | 0 | 20.3 | TDD | 83 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3255770 | 3 | 121.4678306791 | 31.1473412434 | 265 | 11 | 11 | 41.7 | TDD | 524 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3256266 | 4 | 121.4652034918 | 31.1527286958 | 219 | 3 | 8 | 33.1 | TDD | 119 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:31.509 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.532 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.649 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.649 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.385 | NREventA3 | measId:2;ServCellPCI:446;Se... |
| 2024-09-20 22:21:38.625 | NRHandoverAttempt | SourcePCI:446;SourceNR-ARFC... |
| 2024-09-20 22:21:38.665 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.677 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.806 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.806 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3222755 | 1 | 14.3026 | 15.1387 | -115.6208 | 6.6677 | 187.2986 | 0.0053 | 0.0004 |
| 2024_09_20 22:00 | 3253396 | 2 | 13.0884 | 16.9276 | -114.6204 | 13.0176 | 96.3092 | 0.0173 | 0.0194 |
| 2024_09_20 22:00 | 3255770 | 3 | 8.3086 | 16.4511 | -117.4824 | 17.9099 | 140.3859 | 0.0096 | 0.0052 |
| 2024_09_20 22:00 | 3256266 | 4 | 87.6680 | 93.3066 | -115.9067 | 7.7735 | 154.0899 | 0.0177 | 0.0043 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415117_D9753CD5 | 504990 | 119 | -89.2 | 504990 | 524 | -98.6 | 504990 | 83 | -103.5 | 504990 | 185 |
| MR_1774415117_398F9D3E | 504990 | 119 | -91.5 | 504990 | 524 | -97.9 | 504990 | 83 | -104.2 | 504990 | 185 |
| MR_1774415117_4FCBF7C1 | 504990 | 119 | -88.9 | 504990 | 524 | -98.6 | 504990 | 83 | -103.8 | 504990 | 185 |
| MR_1774415117_3F415D3D | 504990 | 119 | -90.2 | 504990 | 524 | -97.4 | 504990 | 83 | -102.8 | 504990 | 185 |
| MR_1774415117_BD23C081 | 504990 | 119 | -90.6 | 504990 | 524 | -98.9 | 504990 | 83 | -103.6 | 504990 | 185 |
| MR_1774415117_71F41F02 | 504990 | 119 | -88.9 | 504990 | 524 | -97.2 | 504990 | 83 | -102.9 | 504990 | 185 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 215: `bd11e64e-ed0...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `bd11e64e-ed00-42df-97e2-1cd01295bc4f` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[215] topology](images/test_0215.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3274895_1
- `C2`: Increase A3 Offset threshold for 3274895_1
- `C3`: Increase A3 Offset threshold for 3228669_2
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3274895_1
- `C5`: Adjust the azimuth of 3274895_1 by 50 degrees
- `C6`: Add neighbor relationship between 3228669_2 and 3274895_1
- `C7`: Lift the tilt angle  of 3274895_1 by 5 degrees
- `C8`: Insufficient data; more data is needed for judgment.
- `C9`: Decrease A3 Offset threshold for 3274895_1
- `C10`: Increase transmission power for 3274895_1
- `C11`: Lift the tilt angle of 3228669_2 by 10 degrees
- `C12`: Press down the tilt angle of 3228669_2 by 10 degrees
- `C13`: Check test server and transmission issues
- `C14`: Increase transmission power for 3228669_2
- `C15`: Adjust the azimuth of 3228669_2 by 50 degrees
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3228669_2
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3228669_2
- `C18`: Decrease A3 Offset threshold for 3228669_2
- `C19`: Press down the tilt angle  of 3274895_1 by 5 degrees
- `C20`: Decrease transmission power for 3228669_2
- `C21`: Decrease transmission power for 3274895_1
- `C22`: Add neighbor relationship between 3241878_3 and 3274895_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.348 | MS1 | 121.4656751746 | 31.1446307691 | 753 | 504990 | -88.00 | 12.04 | 506.54 | 0.07 | 2.51 | 1573 |
| 2024-09-20 22:21:32.377 | MS1 | 121.4656750669 | 31.1446250226 | 753 | 504990 | -92.00 | 15.44 | 409.82 | 0.08 | 2.87 | 1599 |
| 2024-09-20 22:21:33.808 | MS1 | 121.4656723465 | 31.1446348924 | 753 | 504990 | -89.09 | 13.64 | 602.08 | 0.15 | 2.01 | 1588 |
| 2024-09-20 22:21:34.621 | MS1 | 121.4656699256 | 31.1446294390 | 753 | 504990 | -85.27 | 13.30 | 83.84 | 0.08 | 2.09 | 359 |
| 2024-09-20 22:21:35.479 | MS1 | 121.4656697440 | 31.1446256913 | 753 | 504990 | -90.76 | 17.06 | 56.47 | 0.02 | 2.63 | 406 |
| 2024-09-20 22:21:36.167 | MS1 | 121.4656702331 | 31.1446376054 | 753 | 504990 | -87.90 | 12.32 | 103.45 | 0.04 | 2.20 | 423 |
| 2024-09-20 22:21:37.286 | MS1 | 121.4656770650 | 31.1446332110 | 753 | 504990 | -92.01 | 7.14 | 95.36 | 0.03 | 2.79 | 332 |
| 2024-09-20 22:21:38.740 | MS1 | 121.4656747456 | 31.1446186501 | 753 | 504990 | -93.47 | 12.63 | 56.72 | 0.03 | 2.03 | 330 |
| 2024-09-20 22:21:39.302 | MS1 | 121.4656648500 | 31.1446350462 | 753 | 504990 | -89.01 | 8.83 | 101.51 | 0.10 | 3.00 | 416 |
| 2024-09-20 22:21:40.252 | MS1 | 121.4656631705 | 31.1446217991 | 753 | 504990 | -91.64 | 10.90 | 427.72 | 0.05 | 2.94 | 1586 |
| 2024-09-20 22:21:41.400 | MS1 | 121.4656690767 | 31.1446289918 | 753 | 504990 | -90.02 | 7.58 | 319.69 | 0.11 | 2.49 | 1586 |
| 2024-09-20 22:21:42.736 | MS1 | 121.4656747688 | 31.1446349951 | 753 | 504990 | -93.94 | 7.44 | 448.50 | 0.14 | 2.78 | 1599 |

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
| 3228669 | 2 | 121.4664392532 | 31.1460127327 | 294 | 13 | 5 | 29.0 | TDD | 753 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3241878 | 3 | 121.4758074602 | 31.1481582805 | 51 | 3 | 11 | 18.9 | TDD | 732 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3274895 | 1 | 121.4727796143 | 31.1554552612 | 85 | 4 | 6 | 21.3 | TDD | 176 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3279096 | 4 | 121.4714077394 | 31.1491422040 | 111 | 8 | 3 | 30.3 | TDD | 844 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |

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
| 2024-09-20 22:21:31.047 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.065 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.202 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.202 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.912 | NREventA3 | measId:2;ServCellPCI:808;Se... |
| 2024-09-20 22:21:38.152 | NRHandoverAttempt | SourcePCI:808;SourceNR-ARFC... |
| 2024-09-20 22:21:38.190 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.204 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.325 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.325 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3274895 | 1 | 6.1767 | 13.4559 | -117.6572 | 9.3365 | 99.4757 | 0.0117 | 0.0110 |
| 2024_09_20 22:00 | 3228669 | 2 | 18.8226 | 6.0647 | -117.3133 | 14.5915 | 141.7847 | 0.0056 | 0.0148 |
| 2024_09_20 22:00 | 3241878 | 3 | 9.0875 | 11.3502 | -115.6318 | 14.0758 | 152.3548 | 0.0185 | 0.0063 |
| 2024_09_20 22:00 | 3279096 | 4 | 8.1380 | 11.1991 | -116.3373 | 5.4103 | 173.1395 | 0.0116 | 0.0062 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412675_A3DE691E | 504990 | 753 | -84.5 | 504990 | 176 | -90.7 | 504990 | 732 | -100.2 | 504990 | 844 |
| MR_1774412675_905BDE69 | 504990 | 753 | -86.4 | 504990 | 176 | -89.1 | 504990 | 732 | -99.1 | 504990 | 844 |
| MR_1774412675_D62EE14A | 504990 | 753 | -85.0 | 504990 | 176 | -90.8 | 504990 | 732 | -100.4 | 504990 | 844 |
| MR_1774412675_D29298D7 | 504990 | 753 | -85.4 | 504990 | 176 | -90.9 | 504990 | 732 | -98.3 | 504990 | 844 |
| MR_1774412675_5DBA1939 | 504990 | 753 | -86.9 | 504990 | 176 | -90.2 | 504990 | 732 | -98.5 | 504990 | 844 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 216: `2c5f5b73-426...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `2c5f5b73-4264-407c-8a5f-8a17b92aa827` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[216] topology](images/test_0216.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Check test server and transmission issues
- `C2`: Adjust the azimuth of 3227490_4 by 50 degrees
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3217313_3
- `C4`: Press down the tilt angle of 3217313_3 by 1 degrees
- `C5`: Increase transmission power for 3227490_4
- `C6`: Increase A3 Offset threshold for 3227490_4
- `C7`: Decrease A3 Offset threshold for 3227490_4
- `C8`: Decrease transmission power for 3217313_3
- `C9`: Press down the tilt angle  of 3227490_4 by 10 degrees
- `C10`: Increase transmission power for 3217313_3
- `C11`: Lift the tilt angle of 3217313_3 by 1 degrees
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3227490_4
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3217313_3
- `C14`: Increase A3 Offset threshold for 3217313_3
- `C15`: Add neighbor relationship between 3210609_1 and 3227490_4
- `C16`: Lift the tilt angle  of 3227490_4 by 10 degrees
- `C17`: Decrease A3 Offset threshold for 3217313_3
- `C18`: Adjust the azimuth of 3217313_3 by 9 degrees
- `C19`: Decrease transmission power for 3227490_4
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3227490_4
- `C21`: Add neighbor relationship between 3217313_3 and 3227490_4
- `C22`: Insufficient data; more data is needed for judgment.

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.833 | MS1 | 121.4656582599 | 31.1446180708 | 468 | 504990 | -88.86 | 15.86 | 399.05 | 0.13 | 2.10 | 1593 |
| 2024-09-20 22:21:32.517 | MS1 | 121.4656664441 | 31.1446357120 | 468 | 504990 | -88.54 | 13.22 | 342.25 | 0.11 | 2.57 | 1583 |
| 2024-09-20 22:21:33.119 | MS1 | 121.4656696222 | 31.1446290525 | 468 | 504990 | -88.37 | 16.61 | 319.87 | 0.01 | 2.99 | 1593 |
| 2024-09-20 22:21:34.163 | MS1 | 121.4656721658 | 31.1446373812 | 468 | 504990 | -91.59 | 16.36 | 77.29 | 0.54 | 2.25 | 604 |
| 2024-09-20 22:21:35.652 | MS1 | 121.4656633462 | 31.1446215736 | 468 | 504990 | -90.40 | 16.15 | 49.27 | 0.60 | 2.55 | 599 |
| 2024-09-20 22:21:36.971 | MS1 | 121.4656756433 | 31.1446244491 | 468 | 504990 | -90.37 | 15.96 | 63.46 | 0.51 | 2.20 | 506 |
| 2024-09-20 22:21:37.739 | MS1 | 121.4656748239 | 31.1446330663 | 468 | 504990 | -89.40 | 11.10 | 102.79 | 0.66 | 2.06 | 508 |
| 2024-09-20 22:21:38.337 | MS1 | 121.4656641646 | 31.1446243439 | 468 | 504990 | -92.41 | 12.41 | 85.16 | 0.53 | 2.87 | 591 |
| 2024-09-20 22:21:39.351 | MS1 | 121.4656652399 | 31.1446216441 | 468 | 504990 | -93.65 | 9.09 | 60.25 | 0.59 | 2.41 | 517 |
| 2024-09-20 22:21:40.134 | MS1 | 121.4656591407 | 31.1446311125 | 468 | 504990 | -90.98 | 8.65 | 397.49 | 0.16 | 2.92 | 1586 |
| 2024-09-20 22:21:41.997 | MS1 | 121.4656746319 | 31.1446191218 | 468 | 504990 | -90.73 | 7.77 | 581.93 | 0.07 | 2.72 | 1563 |
| 2024-09-20 22:21:42.364 | MS1 | 121.4656685072 | 31.1446339895 | 468 | 504990 | -91.61 | 8.75 | 439.07 | 0.03 | 2.60 | 1591 |

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
| 3210609 | 1 | 121.4758219662 | 31.1447064510 | 172 | 8 | 2 | 33.6 | TDD | 689 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3217313 | 3 | 121.4718426919 | 31.1554249124 | 215 | 0 | 10 | 25.2 | TDD | 468 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3227490 | 4 | 121.4740523709 | 31.1498322634 | 5 | 15 | 2 | 49.1 | TDD | 583 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3243513 | 2 | 121.4709176193 | 31.1470033914 | 4 | 10 | 7 | 38.5 | TDD | 899 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

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
| 2024-09-20 22:21:30.798 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.823 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:30.956 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.956 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.677 | NREventA3 | measId:2;ServCellPCI:778;Se... |
| 2024-09-20 22:21:37.917 | NRHandoverAttempt | SourcePCI:778;SourceNR-ARFC... |
| 2024-09-20 22:21:37.947 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.959 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.075 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.075 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3210609 | 1 | 6.0008 | 13.8483 | -114.6997 | 10.2822 | 92.7543 | 0.0159 | 0.0164 |
| 2024_09_20 22:00 | 3243513 | 2 | 7.9961 | 11.9121 | -117.0057 | 11.6665 | 104.2567 | 0.0027 | 0.0052 |
| 2024_09_20 22:00 | 3217313 | 3 | 10.2828 | 7.3696 | -116.3522 | 13.3542 | 105.5375 | 0.0179 | 0.0168 |
| 2024_09_20 22:00 | 3227490 | 4 | 14.2620 | 14.7378 | -117.0378 | 15.4127 | 154.5671 | 0.0048 | 0.0045 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412961_7A8517D7 | 504990 | 468 | -93.0 | 504990 | 583 | -93.8 | 504990 | 689 | -104.5 | 504990 | 899 |
| MR_1774412961_58E389C8 | 504990 | 468 | -91.9 | 504990 | 583 | -91.9 | 504990 | 689 | -105.4 | 504990 | 899 |
| MR_1774412961_4F9E6AE5 | 504990 | 468 | -91.8 | 504990 | 583 | -92.2 | 504990 | 689 | -104.9 | 504990 | 899 |
| MR_1774412961_D0942596 | 504990 | 468 | -92.9 | 504990 | 583 | -95.6 | 504990 | 689 | -107.2 | 504990 | 899 |
| MR_1774412961_3A72ECB2 | 504990 | 468 | -90.8 | 504990 | 583 | -93.8 | 504990 | 689 | -104.5 | 504990 | 899 |
| MR_1774412961_69258E8B | 504990 | 468 | -93.1 | 504990 | 583 | -95.7 | 504990 | 689 | -107.6 | 504990 | 899 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 217: `7a44dd46-f96...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `7a44dd46-f96f-4f7d-b015-9d4f5f61aa1c` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[217] topology](images/test_0217.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3260200_3
- `C2`: Press down the tilt angle  of 3260200_3 by 10 degrees
- `C3`: Decrease A3 Offset threshold for 3260200_3
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3210337_4
- `C5`: Check test server and transmission issues
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3260200_3
- `C7`: Press down the tilt angle of 3210337_4 by 8 degrees
- `C8`: Increase A3 Offset threshold for 3260200_3
- `C9`: Increase A3 Offset threshold for 3210337_4
- `C10`: Adjust the azimuth of 3210337_4 by 50 degrees
- `C11`: Add neighbor relationship between 3210337_4 and 3260200_3
- `C12`: Decrease transmission power for 3210337_4
- `C13`: Adjust the azimuth of 3260200_3 by 50 degrees
- `C14`: Decrease A3 Offset threshold for 3210337_4
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3210337_4
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3260200_3
- `C17`: Insufficient data; more data is needed for judgment.
- `C18`: Increase transmission power for 3210337_4
- `C19`: Add neighbor relationship between 3217395_2 and 3260200_3
- `C20`: Decrease transmission power for 3260200_3
- `C21`: Lift the tilt angle of 3210337_4 by 8 degrees
- `C22`: Lift the tilt angle  of 3260200_3 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.261 | MS1 | 121.4656679517 | 31.1446370775 | 333 | 504990 | -91.05 | 15.76 | 501.76 | 0.11 | 2.89 | 1571 |
| 2024-09-20 22:21:32.660 | MS1 | 121.4656589983 | 31.1446271785 | 333 | 504990 | -91.87 | 17.38 | 335.94 | 0.11 | 2.06 | 1581 |
| 2024-09-20 22:21:33.729 | MS1 | 121.4656741536 | 31.1446202514 | 333 | 504990 | -86.88 | 13.47 | 507.20 | 0.13 | 2.57 | 1587 |
| 2024-09-20 22:21:34.669 | MS1 | 121.4656748147 | 31.1446253455 | 333 | 504990 | -88.46 | 16.30 | 72.75 | 0.11 | 2.29 | 423 |
| 2024-09-20 22:21:35.623 | MS1 | 121.4656687347 | 31.1446378397 | 333 | 504990 | -89.70 | 16.02 | 87.60 | 0.11 | 2.45 | 476 |
| 2024-09-20 22:21:36.493 | MS1 | 121.4656673620 | 31.1446181188 | 333 | 504990 | -87.93 | 15.45 | 87.60 | 0.16 | 2.22 | 360 |
| 2024-09-20 22:21:37.630 | MS1 | 121.4656680479 | 31.1446224159 | 333 | 504990 | -92.85 | 9.25 | 53.99 | 0.09 | 2.11 | 383 |
| 2024-09-20 22:21:38.153 | MS1 | 121.4656726036 | 31.1446270403 | 333 | 504990 | -93.05 | 7.01 | 85.79 | 0.04 | 2.13 | 382 |
| 2024-09-20 22:21:39.194 | MS1 | 121.4656714881 | 31.1446195341 | 333 | 504990 | -89.57 | 11.72 | 59.17 | 0.20 | 2.72 | 313 |
| 2024-09-20 22:21:40.340 | MS1 | 121.4656588546 | 31.1446217916 | 333 | 504990 | -90.08 | 12.23 | 557.99 | 0.05 | 2.09 | 1573 |
| 2024-09-20 22:21:41.239 | MS1 | 121.4656650005 | 31.1446294244 | 333 | 504990 | -92.30 | 7.23 | 569.18 | 0.14 | 2.63 | 1593 |
| 2024-09-20 22:21:42.819 | MS1 | 121.4656744509 | 31.1446285016 | 333 | 504990 | -92.65 | 12.43 | 338.22 | 0.13 | 2.45 | 1590 |

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
| 3210337 | 4 | 121.4699928639 | 31.1453609212 | 49 | 2 | 1 | 41.4 | TDD | 333 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3217395 | 2 | 121.4695821508 | 31.1537689689 | 62 | 13 | 10 | 21.9 | TDD | 603 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3232869 | 1 | 121.4718604697 | 31.1470462862 | 324 | 11 | 10 | 28.8 | TDD | 577 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3260200 | 3 | 121.4642521904 | 31.1530632774 | 29 | 15 | 6 | 48.3 | TDD | 441 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |

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
| 2024-09-20 22:21:30.809 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.833 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:30.957 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.957 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.661 | NREventA3 | measId:2;ServCellPCI:205;Se... |
| 2024-09-20 22:21:37.901 | NRHandoverAttempt | SourcePCI:205;SourceNR-ARFC... |
| 2024-09-20 22:21:37.951 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.963 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.083 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.083 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3232869 | 1 | 14.9936 | 12.4727 | -115.2762 | 10.4276 | 198.3862 | 0.0019 | 0.0121 |
| 2024_09_20 22:00 | 3217395 | 2 | 11.0190 | 13.9332 | -114.2213 | 17.0091 | 121.6543 | 0.0088 | 0.0195 |
| 2024_09_20 22:00 | 3260200 | 3 | 13.2063 | 6.6482 | -117.4726 | 7.3545 | 105.8216 | 0.0061 | 0.0121 |
| 2024_09_20 22:00 | 3210337 | 4 | 16.8540 | 17.6112 | -117.5613 | 9.2275 | 132.2984 | 0.0190 | 0.0039 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412060_1E949084 | 504990 | 333 | -90.0 | 504990 | 441 | -90.6 | 504990 | 603 | -94.7 | 504990 | 577 |
| MR_1774412060_2F36D20A | 504990 | 333 | -88.8 | 504990 | 441 | -89.0 | 504990 | 603 | -96.0 | 504990 | 577 |
| MR_1774412060_829B1147 | 504990 | 333 | -90.4 | 504990 | 441 | -92.2 | 504990 | 603 | -95.3 | 504990 | 577 |
| MR_1774412060_EA9D9CBF | 504990 | 333 | -89.3 | 504990 | 441 | -90.9 | 504990 | 603 | -93.3 | 504990 | 577 |
| MR_1774412060_29E923BC | 504990 | 333 | -87.7 | 504990 | 441 | -91.0 | 504990 | 603 | -93.7 | 504990 | 577 |
| MR_1774412060_59E73BFB | 504990 | 333 | -88.0 | 504990 | 441 | -89.0 | 504990 | 603 | -94.0 | 504990 | 577 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 218: `59be7f74-123...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `59be7f74-123a-4f3a-b9fe-bbb9c77b7861` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[218] topology](images/test_0218.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3268635_2 by 50 degrees
- `C2`: Insufficient data; more data is needed for judgment.
- `C3`: Add neighbor relationship between 3230538_3 and 3268635_2
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3230538_3
- `C5`: Adjust the azimuth of 3230538_3 by 49 degrees
- `C6`: Increase A3 Offset threshold for 3230538_3
- `C7`: Decrease transmission power for 3230538_3
- `C8`: Decrease A3 Offset threshold for 3230538_3
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3268635_2
- `C10`: Add neighbor relationship between 3231916_4 and 3268635_2
- `C11`: Increase A3 Offset threshold for 3268635_2
- `C12`: Decrease transmission power for 3268635_2
- `C13`: Press down the tilt angle of 3230538_3 by 6 degrees
- `C14`: Increase transmission power for 3230538_3
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3268635_2
- `C16`: Lift the tilt angle  of 3268635_2 by 10 degrees
- `C17`: Lift the tilt angle of 3230538_3 by 6 degrees
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3230538_3
- `C19`: Decrease A3 Offset threshold for 3268635_2
- `C20`: Check test server and transmission issues
- `C21`: Press down the tilt angle  of 3268635_2 by 10 degrees
- `C22`: Increase transmission power for 3268635_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.492 | MS1 | 121.4656660215 | 31.1446310953 | 892 | 504990 | -87.14 | 14.13 | 311.85 | 0.15 | 2.30 | 1593 |
| 2024-09-20 22:21:32.150 | MS1 | 121.4656608656 | 31.1446251658 | 892 | 504990 | -88.81 | 14.30 | 607.65 | 0.15 | 2.96 | 1565 |
| 2024-09-20 22:21:33.364 | MS1 | 121.4656677695 | 31.1446241102 | 892 | 504990 | -86.80 | 12.46 | 366.69 | 0.01 | 2.09 | 1580 |
| 2024-09-20 22:21:34.961 | MS1 | 121.4656601118 | 31.1446199061 | 892 | 504990 | -90.19 | 17.89 | 77.86 | 0.66 | 2.17 | 671 |
| 2024-09-20 22:21:35.159 | MS1 | 121.4656611787 | 31.1446232057 | 892 | 504990 | -87.06 | 15.52 | 58.02 | 0.68 | 2.14 | 637 |
| 2024-09-20 22:21:36.734 | MS1 | 121.4656720377 | 31.1446315409 | 892 | 504990 | -85.82 | 17.89 | 45.41 | 0.58 | 2.33 | 608 |
| 2024-09-20 22:21:37.895 | MS1 | 121.4656696510 | 31.1446279348 | 892 | 504990 | -90.36 | 12.64 | 72.83 | 0.54 | 2.40 | 516 |
| 2024-09-20 22:21:38.648 | MS1 | 121.4656580600 | 31.1446204512 | 892 | 504990 | -89.05 | 7.93 | 61.71 | 0.58 | 2.31 | 575 |
| 2024-09-20 22:21:39.445 | MS1 | 121.4656643309 | 31.1446305861 | 892 | 504990 | -92.02 | 9.64 | 56.99 | 0.54 | 2.25 | 548 |
| 2024-09-20 22:21:40.243 | MS1 | 121.4656710917 | 31.1446201847 | 892 | 504990 | -93.83 | 12.70 | 370.59 | 0.14 | 2.62 | 1590 |
| 2024-09-20 22:21:41.935 | MS1 | 121.4656694020 | 31.1446366698 | 892 | 504990 | -92.85 | 8.60 | 598.09 | 0.11 | 2.77 | 1564 |
| 2024-09-20 22:21:42.211 | MS1 | 121.4656779897 | 31.1446315195 | 892 | 504990 | -90.01 | 11.50 | 529.53 | 0.14 | 2.25 | 1572 |

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
| 3230538 | 3 | 121.4692798839 | 31.1458702712 | 297 | 1 | 8 | 30.9 | TDD | 892 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3231916 | 4 | 121.4727068652 | 31.1511672408 | 280 | 6 | 0 | 48.8 | TDD | 858 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3254848 | 1 | 121.4704526277 | 31.1453419440 | 32 | 10 | 6 | 49.4 | TDD | 706 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3268635 | 2 | 121.4684393154 | 31.1555645145 | 10 | 11 | 12 | 49.5 | TDD | 277 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |

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
| 2024-09-20 22:21:31.295 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.318 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.433 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.433 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.155 | NREventA3 | measId:2;ServCellPCI:206;Se... |
| 2024-09-20 22:21:38.395 | NRHandoverAttempt | SourcePCI:206;SourceNR-ARFC... |
| 2024-09-20 22:21:38.439 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.449 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.564 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.564 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3254848 | 1 | 11.7252 | 7.3998 | -115.3440 | 19.5149 | 109.9216 | 0.0144 | 0.0186 |
| 2024_09_20 22:00 | 3268635 | 2 | 17.5896 | 16.1380 | -116.8362 | 5.0313 | 133.8728 | 0.0047 | 0.0144 |
| 2024_09_20 22:00 | 3230538 | 3 | 5.7242 | 6.6798 | -117.2906 | 11.4833 | 185.5831 | 0.0137 | 0.0150 |
| 2024_09_20 22:00 | 3231916 | 4 | 7.1755 | 14.8998 | -115.3781 | 5.7423 | 164.1615 | 0.0088 | 0.0176 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417033_DE24903A | 504990 | 892 | -89.6 | 504990 | 277 | -97.4 | 504990 | 858 | -98.1 | 504990 | 706 |
| MR_1774417033_39B36619 | 504990 | 892 | -91.9 | 504990 | 277 | -95.7 | 504990 | 858 | -100.7 | 504990 | 706 |
| MR_1774417033_5DD05836 | 504990 | 892 | -91.2 | 504990 | 277 | -96.2 | 504990 | 858 | -101.2 | 504990 | 706 |
| MR_1774417033_F52F56F9 | 504990 | 892 | -88.4 | 504990 | 277 | -95.5 | 504990 | 858 | -99.2 | 504990 | 706 |
| MR_1774417033_B699DDE9 | 504990 | 892 | -91.1 | 504990 | 277 | -96.6 | 504990 | 858 | -100.0 | 504990 | 706 |
| MR_1774417033_340ADAF3 | 504990 | 892 | -90.6 | 504990 | 277 | -97.6 | 504990 | 858 | -99.3 | 504990 | 706 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 219: `73db8c81-a46...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `73db8c81-a46e-416f-afa5-d8d18b81acf5` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[219] topology](images/test_0219.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3263697_3
- `C2`: Increase transmission power for 3229168_1
- `C3`: Press down the tilt angle of 3263697_3 by 10 degrees
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3229168_1
- `C5`: Add neighbor relationship between 3267496_2 and 3229168_1
- `C6`: Adjust the azimuth of 3263697_3 by 50 degrees
- `C7`: Press down the tilt angle  of 3229168_1 by 10 degrees
- `C8`: Decrease transmission power for 3263697_3
- `C9`: Check test server and transmission issues
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3263697_3
- `C11`: Increase A3 Offset threshold for 3229168_1
- `C12`: Decrease A3 Offset threshold for 3229168_1
- `C13`: Increase A3 Offset threshold for 3263697_3
- `C14`: Add neighbor relationship between 3263697_3 and 3229168_1
- `C15`: Lift the tilt angle  of 3229168_1 by 10 degrees
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3229168_1
- `C17`: Insufficient data; more data is needed for judgment.
- `C18`: Increase transmission power for 3263697_3
- `C19`: Lift the tilt angle of 3263697_3 by 10 degrees
- `C20`: Decrease transmission power for 3229168_1
- `C21`: Adjust the azimuth of 3229168_1 by 50 degrees
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3263697_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.921 | MS1 | 121.4656610528 | 31.1446374959 | 405 | 504990 | -80.76 | 16.34 | 509.29 | 0.19 | 2.13 | 1574 |
| 2024-09-20 22:21:32.672 | MS1 | 121.4656614235 | 31.1446255695 | 405 | 504990 | -78.56 | 17.02 | 426.01 | 0.11 | 2.04 | 1596 |
| 2024-09-20 22:21:33.122 | MS1 | 121.4656621749 | 31.1446253121 | 405 | 504990 | -84.33 | 16.91 | 352.96 | 0.08 | 2.07 | 1587 |
| 2024-09-20 22:21:34.546 | MS1 | 121.4656600227 | 31.1446186379 | 405 | 504990 | -87.91 | -2.45 | 45.61 | 0.20 | 1.06 | 1563 |
| 2024-09-20 22:21:35.211 | MS1 | 121.4656625149 | 31.1446246466 | 405 | 504990 | -90.86 | -1.52 | 75.90 | 0.06 | 1.10 | 1586 |
| 2024-09-20 22:21:36.213 | MS1 | 121.4656638391 | 31.1446373756 | 405 | 504990 | -83.83 | -1.74 | 28.37 | 0.01 | 1.12 | 1572 |
| 2024-09-20 22:21:37.541 | MS1 | 121.4656647810 | 31.1446226692 | 405 | 504990 | -91.40 | -0.64 | 34.99 | 0.15 | 1.03 | 1592 |
| 2024-09-20 22:21:38.892 | MS1 | 121.4656759101 | 31.1446216916 | 405 | 504990 | -87.65 | -3.50 | 68.38 | 0.16 | 1.11 | 1567 |
| 2024-09-20 22:21:39.727 | MS1 | 121.4656601484 | 31.1446303269 | 1 | 504990 | -80.82 | 17.35 | 272.23 | 0.17 | 1.30 | 1593 |
| 2024-09-20 22:21:40.548 | MS1 | 121.4656735484 | 31.1446307553 | 1 | 504990 | -76.53 | 12.85 | 471.24 | 0.09 | 2.63 | 1577 |
| 2024-09-20 22:21:41.772 | MS1 | 121.4656604278 | 31.1446252877 | 1 | 504990 | -79.02 | 15.38 | 539.04 | 0.12 | 2.97 | 1592 |
| 2024-09-20 22:21:42.674 | MS1 | 121.4656603318 | 31.1446196351 | 1 | 504990 | -79.43 | 17.19 | 509.23 | 0.15 | 2.72 | 1577 |

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
| 3229168 | 1 | 121.4642164431 | 31.1541999450 | 0 | 14 | 6 | 49.6 | TDD | 1 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3263697 | 3 | 121.4670148493 | 31.1441949443 | 68 | 15 | 8 | 25.6 | TDD | 405 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3267496 | 2 | 121.4641576031 | 31.1506243316 | 318 | 3 | 7 | 34.9 | TDD | 170 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3276138 | 4 | 121.4706918592 | 31.1465865904 | 84 | 15 | 9 | 21.7 | TDD | 706 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

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
| 2024-09-20 22:21:31.370 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.392 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.500 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.500 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.238 | NREventA3 | measId:2;ServCellPCI:135;Se... |
| 2024-09-20 22:21:38.478 | NRHandoverAttempt | SourcePCI:135;SourceNR-ARFC... |
| 2024-09-20 22:21:38.514 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.525 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.670 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.670 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3229168 | 1 | 15.8698 | 5.1552 | -116.0852 | 16.4499 | 157.8266 | 0.0090 | 0.0184 |
| 2024_09_20 22:00 | 3267496 | 2 | 16.6440 | 11.6947 | -116.5630 | 13.8843 | 140.1417 | 0.0174 | 0.0067 |
| 2024_09_20 22:00 | 3263697 | 3 | 12.2309 | 5.8645 | -117.4534 | 16.2371 | 91.7919 | 0.0000 | 0.1848 |
| 2024_09_20 22:00 | 3276138 | 4 | 10.5989 | 5.7666 | -117.7399 | 9.4918 | 157.1847 | 0.0079 | 0.0164 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416968_7CEEB779 | 504990 | 405 | -88.4 | 504990 | 1 | -83.3 | 504990 | 170 | -89.1 | 504990 | 706 |
| MR_1774416968_49D6EADB | 504990 | 405 | -88.2 | 504990 | 1 | -84.0 | 504990 | 170 | -90.3 | 504990 | 706 |
| MR_1774416968_4E4FFA04 | 504990 | 1 | -80.4 | 504990 | 405 | -89.5 | 504990 | 170 | -91.0 | 504990 | 706 |
| MR_1774416968_5E9BE42E | 504990 | 405 | -89.3 | 504990 | 1 | -82.8 | 504990 | 170 | -89.7 | 504990 | 706 |
| MR_1774416968_F777E9DF | 504990 | 405 | -87.2 | 504990 | 1 | -82.3 | 504990 | 170 | -91.8 | 504990 | 706 |

> *... 2개 열 생략 (전체 14열)*

---
