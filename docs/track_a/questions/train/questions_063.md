# Track A 문제 분석 — train[620]~train[629]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[620] ~ train[629] (10개)

## 목차

1. [문제 620: `db1b033b-c29...`](#620) — single-answer, 정답: C2
2. [문제 621: `8c8a333b-cd5...`](#621) — single-answer, 정답: C9
3. [문제 622: `cc813d2f-949...`](#622) — single-answer, 정답: C4
4. [문제 623: `1948d698-857...`](#623) — single-answer, 정답: C2
5. [문제 624: `abbcdf08-69c...`](#624) — single-answer, 정답: C20
6. [문제 625: `739a8654-311...`](#625) — single-answer, 정답: C22
7. [문제 626: `34e946f6-051...`](#626) — single-answer, 정답: C13
8. [문제 627: `d9aaa93e-491...`](#627) — single-answer, 정답: C15
9. [문제 628: `b9881c31-f52...`](#628) — single-answer, 정답: C8
10. [문제 629: `bb51b94c-c99...`](#629) — single-answer, 정답: C7

---

### 문제 620: `db1b033b-c29...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `db1b033b-c291-43c0-8cfc-b311d4db0fa6` |
| Tag | **single-answer** |
| 정답 | **C2** |
| C2 의미 | Lift the tilt angle  of 3210417_4 by 7 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[620] topology](images/train_0620.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3210417_4 and 3263271_3
- `C2`: Lift the tilt angle  of 3210417_4 by 7 degrees **← 정답**
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3263271_3
- `C4`: Decrease transmission power for 3230153_2
- `C5`: Increase transmission power for 3263271_3
- `C6`: Decrease A3 Offset threshold for 3263271_3
- `C7`: Increase A3 Offset threshold for 3263271_3
- `C8`: Adjust the azimuth of 3230153_2 by 18 degrees
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3263271_3
- `C10`: Press down the tilt angle of 3230153_2 by 4 degrees
- `C11`: Decrease A3 Offset threshold for 3230153_2
- `C12`: Check test server and transmission issues
- `C13`: Lift the tilt angle of 3230153_2 by 4 degrees
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3230153_2
- `C15`: Add neighbor relationship between 3230153_2 and 3263271_3
- `C16`: Decrease transmission power for 3263271_3
- `C17`: Press down the tilt angle  of 3210417_4 by 7 degrees
- `C18`: Increase transmission power for 3230153_2
- `C19`: Adjust the azimuth of 3210417_4 by 50 degrees
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3230153_2
- `C21`: Insufficient data; more data is needed for judgment.
- `C22`: Increase A3 Offset threshold for 3230153_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.699 | MS1 | 121.4656626422 | 31.1446334733 | 601 | 504990 | -89.62 | 16.66 | 448.81 | 0.17 | 2.06 | 1566 |
| 2024-09-20 22:21:32.652 | MS1 | 121.4656754299 | 31.1446359087 | 601 | 504990 | -86.34 | 12.28 | 336.34 | 0.02 | 2.21 | 1560 |
| 2024-09-20 22:21:33.741 | MS1 | 121.4656621481 | 31.1446300342 | 601 | 504990 | -91.45 | 12.33 | 561.56 | 0.17 | 2.23 | 1578 |
| 2024-09-20 22:21:34.790 | MS1 | 121.4656608746 | 31.1446362457 | 601 | 504990 | -85.54 | 16.80 | 74.73 | 0.12 | 2.58 | 1564 |
| 2024-09-20 22:21:35.832 | MS1 | 121.4656711302 | 31.1446182688 | 601 | 504990 | -85.12 | 17.64 | 76.64 | 0.01 | 2.92 | 1596 |
| 2024-09-20 22:21:36.671 | MS1 | 121.4656742990 | 31.1446235208 | 601 | 504990 | -87.87 | 12.74 | 97.87 | 0.17 | 2.41 | 1574 |
| 2024-09-20 22:21:37.656 | MS1 | 121.4656750243 | 31.1446289443 | 601 | 504990 | -92.69 | 8.98 | 78.43 | 0.12 | 2.14 | 1596 |
| 2024-09-20 22:21:38.287 | MS1 | 121.4656596236 | 31.1446207596 | 601 | 504990 | -92.20 | 10.84 | 79.23 | 0.05 | 2.03 | 1580 |
| 2024-09-20 22:21:39.945 | MS1 | 121.4656580636 | 31.1446205033 | 601 | 504990 | -93.56 | 11.07 | 60.41 | 0.06 | 2.90 | 1572 |
| 2024-09-20 22:21:40.923 | MS1 | 121.4656665881 | 31.1446366695 | 601 | 504990 | -90.72 | 9.06 | 386.11 | 0.14 | 2.55 | 1599 |
| 2024-09-20 22:21:41.585 | MS1 | 121.4656689336 | 31.1446271775 | 601 | 504990 | -91.31 | 9.08 | 377.40 | 0.07 | 2.93 | 1581 |
| 2024-09-20 22:21:42.903 | MS1 | 121.4656629047 | 31.1446193174 | 601 | 504990 | -89.94 | 10.10 | 560.24 | 0.02 | 2.55 | 1596 |

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
| 3210417 | 4 | 121.4741859339 | 31.1516412894 | 68 | 5 | 9 | 27.1 | TDD | 964 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3230153 | 2 | 121.4645687884 | 31.1493169059 | 187 | 1 | 3 | 28.8 | TDD | 601 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3261604 | 1 | 121.4658969286 | 31.1536009232 | 174 | 7 | 2 | 36.5 | TDD | 472 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3263271 | 3 | 121.4683233150 | 31.1530878108 | 132 | 5 | 7 | 27.8 | TDD | 306 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:31.012 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.029 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.138 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.138 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.842 | NREventA3 | measId:2;ServCellPCI:905;Se... |
| 2024-09-20 22:21:38.082 | NRHandoverAttempt | SourcePCI:905;SourceNR-ARFC... |
| 2024-09-20 22:21:38.125 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.136 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.252 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.252 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3261604 | 1 | 17.6057 | 6.9471 | -115.0578 | 18.5553 | 105.4299 | 0.0023 | 0.0122 |
| 2024_09_20 22:00 | 3230153 | 2 | 77.8796 | 89.3243 | -115.7906 | 11.9183 | 194.4706 | 0.0168 | 0.0189 |
| 2024_09_20 22:00 | 3263271 | 3 | 7.4941 | 6.5146 | -114.3036 | 15.2020 | 148.1930 | 0.0184 | 0.0166 |
| 2024_09_20 22:00 | 3210417 | 4 | 11.3697 | 11.3509 | -114.9283 | 12.5530 | 138.2070 | 0.0175 | 0.0109 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774411989_E1458C3F | 504990 | 601 | -86.5 | 504990 | 306 | -91.6 | 504990 | 964 | -94.6 | 504990 | 472 |
| MR_1774411989_16CB3039 | 504990 | 601 | -86.2 | 504990 | 306 | -92.8 | 504990 | 964 | -94.2 | 504990 | 472 |
| MR_1774411989_6F82DF0C | 504990 | 601 | -84.7 | 504990 | 306 | -92.9 | 504990 | 964 | -93.9 | 504990 | 472 |
| MR_1774411989_F74B0D26 | 504990 | 601 | -87.4 | 504990 | 306 | -93.6 | 504990 | 964 | -94.2 | 504990 | 472 |
| MR_1774411989_82F9DF4E | 504990 | 601 | -85.1 | 504990 | 306 | -93.7 | 504990 | 964 | -95.4 | 504990 | 472 |
| MR_1774411989_B7E14402 | 504990 | 601 | -84.0 | 504990 | 306 | -93.8 | 504990 | 964 | -93.3 | 504990 | 472 |
| MR_1774411989_1C6685D7 | 504990 | 601 | -85.3 | 504990 | 306 | -91.6 | 504990 | 964 | -92.2 | 504990 | 472 |
| MR_1774411989_3C3C9BD3 | 504990 | 601 | -86.9 | 504990 | 306 | -92.9 | 504990 | 964 | -92.9 | 504990 | 472 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 621: `8c8a333b-cd5...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `8c8a333b-cd5a-40e9-9b13-910fd8f12475` |
| Tag | **single-answer** |
| 정답 | **C9** |
| C9 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3224508_4 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[621] topology](images/train_0621.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Check test server and transmission issues
- `C2`: Decrease transmission power for 3224508_4
- `C3`: Press down the tilt angle  of 3242754_5 by 0 degrees
- `C4`: Add neighbor relationship between 3224508_4 and 3242754_5
- `C5`: Increase transmission power for 3242754_5
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3242754_5
- `C7`: Decrease transmission power for 3242754_5
- `C8`: Decrease A3 Offset threshold for 3242754_5
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3224508_4 **← 정답**
- `C10`: Increase A3 Offset threshold for 3242754_5
- `C11`: Increase transmission power for 3224508_4
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3224508_4
- `C13`: Increase A3 Offset threshold for 3224508_4
- `C14`: Adjust the azimuth of 3242754_5 by 48 degrees
- `C15`: Decrease A3 Offset threshold for 3224508_4
- `C16`: Adjust the azimuth of 3224508_4 by 27 degrees
- `C17`: Lift the tilt angle  of 3242754_5 by 0 degrees
- `C18`: Insufficient data; more data is needed for judgment.
- `C19`: Add neighbor relationship between 3264451_13 and 3242754_5
- `C20`: Lift the tilt angle of 3224508_4 by 3 degrees
- `C21`: Press down the tilt angle of 3224508_4 by 3 degrees
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3242754_5

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.540 | MS1 | 121.4656621141 | 31.1446186550 | 31 | 504990 | -94.76 | 14.16 | 373.59 | 0.08 | 2.28 | 1587 |
| 2024-09-20 22:21:32.391 | MS1 | 121.4656746508 | 31.1446239841 | 25 | 504990 | -94.20 | 10.27 | 310.86 | 0.13 | 2.08 | 1576 |
| 2024-09-20 22:21:33.900 | MS1 | 121.4656604748 | 31.1446275133 | 351 | 504990 | -93.73 | 10.20 | 355.81 | 0.17 | 2.52 | 1569 |
| 2024-09-20 22:21:34.799 | MS1 | 121.4656777078 | 31.1446322424 | 232 | 152650 | -93.50 | 6.13 | 50.11 | 0.04 | 1.57 | 938 |
| 2024-09-20 22:21:35.795 | MS1 | 121.4656581898 | 31.1446352270 | 215 | 152650 | -96.39 | 3.31 | 69.98 | 0.19 | 1.59 | 916 |
| 2024-09-20 22:21:36.104 | MS1 | 121.4656629326 | 31.1446192529 | 829 | 152650 | -87.60 | 2.07 | 65.70 | 0.06 | 1.90 | 929 |
| 2024-09-20 22:21:37.133 | MS1 | 121.4656653998 | 31.1446204517 | 738 | 152650 | -94.91 | 5.63 | 65.45 | 0.01 | 1.61 | 916 |
| 2024-09-20 22:21:38.490 | MS1 | 121.4656724964 | 31.1446361461 | 232 | 152650 | -87.01 | 7.58 | 42.68 | 0.16 | 1.77 | 908 |
| 2024-09-20 22:21:39.149 | MS1 | 121.4656737790 | 31.1446185926 | 215 | 152650 | -88.04 | 7.39 | 72.56 | 0.10 | 1.75 | 910 |
| 2024-09-20 22:21:40.153 | MS1 | 121.4656680346 | 31.1446214093 | 829 | 152650 | -88.67 | 3.21 | 87.80 | 0.17 | 2.46 | 1591 |
| 2024-09-20 22:21:41.461 | MS1 | 121.4656607428 | 31.1446231824 | 738 | 152650 | -95.59 | 2.83 | 84.85 | 0.14 | 2.61 | 1566 |
| 2024-09-20 22:21:42.278 | MS1 | 121.4656601382 | 31.1446260383 | 232 | 152650 | -93.26 | 5.49 | 85.24 | 0.05 | 2.65 | 1574 |

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
| 3224508 | 4 | 121.4738804593 | 31.1520502621 | 250 | 2 | 2 | 14.1 | TDD | 31 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3224882 | 3 | 121.4724874773 | 31.1494525063 | 40 | 7 | 7 | 4.5 | TDD | 25 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3230297 | 6 | 121.4748654788 | 31.1557402388 | 18 | 5 | 12 | 26.7 | TDD | 351 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3236401 | 2 | 121.4693936677 | 31.1491579893 | 86 | 3 | 12 | 1.5 | TDD | 908 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3242754 | 5 | 121.4735085576 | 31.1529860680 | 267 | 0 | 1 | 5.7 | TDD | 798 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3242838 | 1 | 121.4643658014 | 31.1526554742 | 38 | 12 | 11 | 3.9 | TDD | 610 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3248049 | 10 | 121.4722543823 | 31.1458954433 | 172 | 9 | 4 | 24.6 | FDD | 912 | n1 | 152650 | 30M | 4T4R | 17 | 152650 |
| 3251030 | 8 | 121.4739464122 | 31.1460329929 | 225 | 0 | 8 | 3.6 | FDD | 738 | n1 | 152650 | 30M | 4T4R | 21 | 152650 |
| 3255444 | 11 | 121.4706160550 | 31.1458594368 | 295 | 5 | 9 | 3.9 | FDD | 215 | n1 | 152650 | 30M | 4T4R | 29 | 152650 |
| 3258058 | 12 | 121.4746006452 | 31.1442136329 | 349 | 11 | 5 | 18.7 | FDD | 666 | n1 | 152650 | 30M | 4T4R | 13 | 152650 |
| 3264451 | 13 | 121.4650816802 | 31.1456194944 | 102 | 7 | 0 | 18.4 | FDD | 829 | n1 | 152650 | 30M | 4T4R | 12 | 152650 |
| 3264919 | 9 | 121.4745800692 | 31.1518178255 | 141 | 2 | 1 | 5.6 | FDD | 232 | n1 | 152650 | 30M | 4T4R | 26 | 152650 |
| 3275882 | 7 | 121.4697550392 | 31.1507192174 | 105 | 11 | 3 | 9.0 | FDD | 32 | n1 | 152650 | 30M | 4T4R | 29 | 152650 |

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
| 2024-09-20 22:21:31.657 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.682 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.804 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.804 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.496 | NREventA2 | measId:1;ServCellPCI:884;Se... |
| 2024-09-20 22:21:35.624 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.923 | NREventA5 | measId:3;ServCellPCI:884;Se... |
| 2024-09-20 22:21:35.989 | NRHandoverAttempt | SourcePCI:884;SourceNR-ARFC... |
| 2024-09-20 22:21:36.023 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:36.038 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:36.184 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.184 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3242838 | 1 | 12.3146 | 14.1840 | -117.3003 | 19.9162 | 173.7356 | 0.0187 | 0.0036 |
| 2024_09_20 22:00 | 3236401 | 2 | 5.8243 | 8.4803 | -114.2847 | 19.2111 | 159.0494 | 0.0166 | 0.0099 |
| 2024_09_20 22:00 | 3224882 | 3 | 17.9479 | 14.2668 | -114.1174 | 13.8169 | 108.6123 | 0.0067 | 0.0187 |
| 2024_09_20 22:00 | 3224508 | 4 | 5.5487 | 18.1873 | -114.4418 | 15.2645 | 127.7664 | 0.0146 | 0.0086 |
| 2024_09_20 22:00 | 3242754 | 5 | 13.2225 | 17.0026 | -116.0638 | 16.6203 | 118.0497 | 0.0018 | 0.0102 |
| 2024_09_20 22:00 | 3230297 | 6 | 16.4627 | 12.5146 | -116.5413 | 10.7924 | 130.0061 | 0.0019 | 0.0156 |
| 2024_09_20 22:00 | 3275882 | 7 | 14.6177 | 7.5575 | -115.6432 | 4.1326 | 47.8785 | 0.0133 | 0.0026 |
| 2024_09_20 22:00 | 3251030 | 8 | 11.6046 | 11.5588 | -115.1413 | 4.4183 | 46.5544 | 0.0089 | 0.0164 |
| 2024_09_20 22:00 | 3264919 | 9 | 14.5238 | 9.5254 | -115.5139 | 4.8406 | 53.7671 | 0.0036 | 0.0109 |
| 2024_09_20 22:00 | 3248049 | 10 | 8.3515 | 6.8060 | -116.8818 | 4.9649 | 50.8609 | 0.0194 | 0.0187 |
| 2024_09_20 22:00 | 3255444 | 11 | 19.2366 | 17.0679 | -115.0964 | 4.8500 | 20.7270 | 0.0015 | 0.0138 |
| 2024_09_20 22:00 | 3258058 | 12 | 16.6400 | 8.1929 | -115.0197 | 4.1693 | 26.4729 | 0.0098 | 0.0041 |
| 2024_09_20 22:00 | 3264451 | 13 | 12.5326 | 14.9608 | -114.7376 | 3.0744 | 54.2489 | 0.0140 | 0.0142 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414809_AF0FA35E | 152650 | 232 | -93.8 | 152650 | 912 | -96.1 | 152650 | 666 | -101.7 | 152650 | 32 |
| MR_1774414809_01098D3A | 152650 | 232 | -95.0 | 152650 | 912 | -97.5 | 152650 | 666 | -101.2 | 152650 | 32 |
| MR_1774414809_3BCA4FF5 | 504990 | 351 | -93.6 | 504990 | 798 | -95.2 | 504990 | 610 | -99.3 | 504990 | 908 |
| MR_1774414809_FDAC2565 | 152650 | 232 | -93.2 | 152650 | 912 | -96.7 | 152650 | 666 | -101.8 | 152650 | 32 |
| MR_1774414809_FDCDEBAE | 504990 | 351 | -95.2 | 504990 | 798 | -95.6 | 504990 | 610 | -98.0 | 504990 | 908 |
| MR_1774414809_85C82E67 | 152650 | 232 | -93.6 | 152650 | 912 | -96.0 | 152650 | 666 | -100.2 | 152650 | 32 |
| MR_1774414809_5896C1E4 | 152650 | 232 | -92.3 | 152650 | 912 | -97.6 | 152650 | 666 | -100.6 | 152650 | 32 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 622: `cc813d2f-949...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `cc813d2f-9495-41fb-9a61-97f3a6934bb1` |
| Tag | **single-answer** |
| 정답 | **C4** |
| C4 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3265053_3 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[622] topology](images/train_0622.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3264324_1
- `C2`: Add neighbor relationship between 3269502_11 and 3264324_1
- `C3`: Press down the tilt angle of 3265053_3 by 3 degrees
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3265053_3 **← 정답**
- `C5`: Increase A3 Offset threshold for 3265053_3
- `C6`: Decrease transmission power for 3265053_3
- `C7`: Increase transmission power for 3265053_3
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3264324_1
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3264324_1
- `C10`: Insufficient data; more data is needed for judgment.
- `C11`: Increase A3 Offset threshold for 3264324_1
- `C12`: Add neighbor relationship between 3265053_3 and 3264324_1
- `C13`: Lift the tilt angle  of 3264324_1 by 6 degrees
- `C14`: Check test server and transmission issues
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3265053_3
- `C16`: Adjust the azimuth of 3264324_1 by 13 degrees
- `C17`: Decrease transmission power for 3264324_1
- `C18`: Decrease A3 Offset threshold for 3264324_1
- `C19`: Decrease A3 Offset threshold for 3265053_3
- `C20`: Press down the tilt angle  of 3264324_1 by 6 degrees
- `C21`: Lift the tilt angle of 3265053_3 by 3 degrees
- `C22`: Adjust the azimuth of 3265053_3 by 29 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.913 | MS1 | 121.4656590082 | 31.1446373707 | 778 | 504990 | -94.89 | 12.43 | 413.26 | 0.13 | 2.82 | 1595 |
| 2024-09-20 22:21:32.926 | MS1 | 121.4656706669 | 31.1446336484 | 668 | 504990 | -94.28 | 12.25 | 534.34 | 0.05 | 2.33 | 1583 |
| 2024-09-20 22:21:33.972 | MS1 | 121.4656632921 | 31.1446234694 | 649 | 504990 | -94.66 | 10.49 | 354.41 | 0.13 | 2.80 | 1597 |
| 2024-09-20 22:21:34.597 | MS1 | 121.4656695018 | 31.1446277529 | 284 | 152650 | -93.27 | 7.78 | 99.32 | 0.03 | 1.58 | 930 |
| 2024-09-20 22:21:35.195 | MS1 | 121.4656731516 | 31.1446321329 | 670 | 152650 | -95.06 | 4.31 | 84.49 | 0.01 | 1.92 | 977 |
| 2024-09-20 22:21:36.318 | MS1 | 121.4656771217 | 31.1446307792 | 507 | 152650 | -91.62 | 4.01 | 95.81 | 0.11 | 1.53 | 967 |
| 2024-09-20 22:21:37.267 | MS1 | 121.4656597513 | 31.1446215839 | 816 | 152650 | -91.08 | 3.45 | 62.86 | 0.10 | 1.68 | 903 |
| 2024-09-20 22:21:38.367 | MS1 | 121.4656608428 | 31.1446345702 | 284 | 152650 | -90.24 | 3.30 | 57.69 | 0.19 | 1.62 | 984 |
| 2024-09-20 22:21:39.716 | MS1 | 121.4656674356 | 31.1446267530 | 670 | 152650 | -90.18 | 5.44 | 75.29 | 0.09 | 1.92 | 943 |
| 2024-09-20 22:21:40.176 | MS1 | 121.4656720937 | 31.1446219790 | 507 | 152650 | -90.06 | 4.10 | 100.04 | 0.19 | 2.24 | 1584 |
| 2024-09-20 22:21:41.979 | MS1 | 121.4656639240 | 31.1446244740 | 816 | 152650 | -95.63 | 6.64 | 75.80 | 0.11 | 2.77 | 1599 |
| 2024-09-20 22:21:42.291 | MS1 | 121.4656583749 | 31.1446189631 | 284 | 152650 | -90.54 | 2.80 | 63.73 | 0.01 | 2.80 | 1580 |

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
| 3211919 | 2 | 121.4679707624 | 31.1466901671 | 123 | 12 | 11 | 23.2 | TDD | 649 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3213369 | 4 | 121.4655826830 | 31.1513951008 | 349 | 8 | 9 | 23.6 | TDD | 463 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3219488 | 6 | 121.4686836370 | 31.1523981198 | 71 | 1 | 1 | 14.5 | TDD | 668 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3221747 | 12 | 121.4684652512 | 31.1480339993 | 123 | 6 | 9 | 0.5 | FDD | 284 | n1 | 152650 | 30M | 4T4R | 28 | 152650 |
| 3223534 | 5 | 121.4701956712 | 31.1533741808 | 50 | 14 | 3 | 20.7 | TDD | 91 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3223879 | 8 | 121.4689414077 | 31.1493354456 | 188 | 0 | 5 | 0.9 | FDD | 145 | n1 | 152650 | 30M | 4T4R | 21 | 152650 |
| 3229637 | 9 | 121.4735020552 | 31.1461127303 | 140 | 1 | 1 | 25.3 | FDD | 958 | n1 | 152650 | 30M | 4T4R | 23 | 152650 |
| 3234519 | 10 | 121.4707146698 | 31.1548339332 | 267 | 12 | 7 | 24.5 | FDD | 792 | n1 | 152650 | 30M | 4T4R | 24 | 152650 |
| 3243008 | 13 | 121.4733481456 | 31.1523662542 | 347 | 9 | 5 | 18.4 | FDD | 670 | n1 | 152650 | 30M | 4T4R | 13 | 152650 |
| 3247450 | 7 | 121.4643642948 | 31.1499693140 | 65 | 3 | 9 | 19.0 | FDD | 816 | n1 | 152650 | 30M | 4T4R | 25 | 152650 |
| 3264324 | 1 | 121.4684005717 | 31.1468129912 | 214 | 2 | 11 | 24.4 | TDD | 488 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3265053 | 3 | 121.4714901893 | 31.1451801298 | 235 | 3 | 1 | 4.7 | TDD | 778 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3269502 | 11 | 121.4753156648 | 31.1532051723 | 175 | 12 | 3 | 4.6 | FDD | 507 | n1 | 152650 | 30M | 4T4R | 25 | 152650 |

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
| 2024-09-20 22:21:31.356 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.356 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.110 | NREventA2 | measId:1;ServCellPCI:266;Se... |
| 2024-09-20 22:21:35.214 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.478 | NREventA5 | measId:3;ServCellPCI:266;Se... |
| 2024-09-20 22:21:35.515 | NRHandoverAttempt | SourcePCI:266;SourceNR-ARFC... |
| 2024-09-20 22:21:35.539 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.552 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:35.694 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.694 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3264324 | 1 | 15.6177 | 5.9074 | -114.1459 | 15.4793 | 169.9023 | 0.0073 | 0.0102 |
| 2024_09_20 22:00 | 3211919 | 2 | 19.9509 | 16.0344 | -116.7918 | 13.9425 | 97.2599 | 0.0054 | 0.0093 |
| 2024_09_20 22:00 | 3265053 | 3 | 5.0723 | 12.3113 | -117.2685 | 15.1622 | 131.9980 | 0.0034 | 0.0169 |
| 2024_09_20 22:00 | 3213369 | 4 | 19.3854 | 10.6265 | -116.7689 | 5.5994 | 121.7323 | 0.0164 | 0.0089 |
| 2024_09_20 22:00 | 3223534 | 5 | 5.2629 | 5.3813 | -115.9373 | 11.4103 | 151.5798 | 0.0091 | 0.0033 |
| 2024_09_20 22:00 | 3219488 | 6 | 5.6804 | 11.3449 | -117.3073 | 6.3404 | 143.1300 | 0.0200 | 0.0160 |
| 2024_09_20 22:00 | 3247450 | 7 | 5.6680 | 16.3524 | -114.4553 | 3.0875 | 25.3166 | 0.0135 | 0.0121 |
| 2024_09_20 22:00 | 3223879 | 8 | 17.3692 | 10.2076 | -115.3720 | 3.1131 | 45.7689 | 0.0170 | 0.0032 |
| 2024_09_20 22:00 | 3229637 | 9 | 8.0837 | 5.1410 | -114.6079 | 3.0635 | 59.2690 | 0.0005 | 0.0052 |
| 2024_09_20 22:00 | 3234519 | 10 | 14.0297 | 17.9189 | -115.5392 | 4.5031 | 46.5885 | 0.0098 | 0.0155 |
| 2024_09_20 22:00 | 3269502 | 11 | 16.4671 | 11.0290 | -115.9103 | 3.1100 | 50.6518 | 0.0060 | 0.0035 |
| 2024_09_20 22:00 | 3221747 | 12 | 5.8797 | 13.7557 | -117.8508 | 4.4657 | 58.6729 | 0.0033 | 0.0200 |
| 2024_09_20 22:00 | 3243008 | 13 | 5.8451 | 7.9665 | -114.7256 | 3.1756 | 44.1386 | 0.0016 | 0.0125 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412337_89AACB67 | 504990 | 649 | -93.8 | 504990 | 488 | -93.6 | 504990 | 463 | -96.9 | 504990 | 91 |
| MR_1774412337_28AE7C6D | 152650 | 284 | -94.3 | 152650 | 145 | -99.4 | 152650 | 792 | -101.2 | 152650 | 958 |
| MR_1774412337_5A7F9411 | 504990 | 649 | -93.4 | 504990 | 488 | -94.3 | 504990 | 463 | -97.3 | 504990 | 91 |
| MR_1774412337_BF848720 | 504990 | 649 | -93.5 | 504990 | 488 | -91.1 | 504990 | 463 | -98.2 | 504990 | 91 |
| MR_1774412337_04B86AB7 | 504990 | 649 | -94.2 | 504990 | 488 | -93.3 | 504990 | 463 | -97.4 | 504990 | 91 |
| MR_1774412337_B74436A1 | 152650 | 284 | -91.9 | 152650 | 145 | -98.3 | 152650 | 792 | -98.4 | 152650 | 958 |
| MR_1774412337_2113599A | 504990 | 649 | -94.9 | 504990 | 488 | -91.4 | 504990 | 463 | -98.2 | 504990 | 91 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 623: `1948d698-857...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `1948d698-8578-4be9-a725-170f25b56063` |
| Tag | **single-answer** |
| 정답 | **C2** |
| C2 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3236012_4 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[623] topology](images/train_0623.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3236012_4 by 4 degrees
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3236012_4 **← 정답**
- `C3`: Press down the tilt angle  of 3247267_1 by 10 degrees
- `C4`: Adjust the azimuth of 3236012_4 by 5 degrees
- `C5`: Increase transmission power for 3236012_4
- `C6`: Add neighbor relationship between 3236012_4 and 3247267_1
- `C7`: Increase transmission power for 3247267_1
- `C8`: Lift the tilt angle  of 3247267_1 by 10 degrees
- `C9`: Decrease A3 Offset threshold for 3236012_4
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3247267_1
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3236012_4
- `C12`: Decrease A3 Offset threshold for 3247267_1
- `C13`: Adjust the azimuth of 3247267_1 by 50 degrees
- `C14`: Lift the tilt angle of 3236012_4 by 4 degrees
- `C15`: Insufficient data; more data is needed for judgment.
- `C16`: Increase A3 Offset threshold for 3247267_1
- `C17`: Add neighbor relationship between 3248019_2 and 3247267_1
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3247267_1
- `C19`: Decrease transmission power for 3247267_1
- `C20`: Decrease transmission power for 3236012_4
- `C21`: Check test server and transmission issues
- `C22`: Increase A3 Offset threshold for 3236012_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.303 | MS1 | 121.4656702566 | 31.1446376947 | 55 | 504990 | -90.18 | 13.16 | 487.84 | 0.08 | 2.55 | 1561 |
| 2024-09-20 22:21:32.654 | MS1 | 121.4656637443 | 31.1446296422 | 55 | 504990 | -89.85 | 14.14 | 537.57 | 0.06 | 2.08 | 1588 |
| 2024-09-20 22:21:33.713 | MS1 | 121.4656581886 | 31.1446319957 | 55 | 504990 | -91.18 | 13.93 | 363.93 | 0.09 | 2.04 | 1587 |
| 2024-09-20 22:21:34.615 | MS1 | 121.4656703164 | 31.1446210124 | 55 | 504990 | -91.20 | 15.41 | 60.93 | 0.68 | 2.80 | 597 |
| 2024-09-20 22:21:35.326 | MS1 | 121.4656756866 | 31.1446318210 | 55 | 504990 | -88.97 | 12.53 | 96.65 | 0.58 | 2.20 | 596 |
| 2024-09-20 22:21:36.684 | MS1 | 121.4656755087 | 31.1446364297 | 55 | 504990 | -85.52 | 13.93 | 83.98 | 0.66 | 2.22 | 598 |
| 2024-09-20 22:21:37.490 | MS1 | 121.4656720609 | 31.1446359942 | 55 | 504990 | -90.26 | 11.30 | 80.42 | 0.63 | 2.05 | 577 |
| 2024-09-20 22:21:38.479 | MS1 | 121.4656661541 | 31.1446182821 | 55 | 504990 | -91.47 | 8.51 | 52.75 | 0.66 | 2.36 | 587 |
| 2024-09-20 22:21:39.213 | MS1 | 121.4656761077 | 31.1446339022 | 55 | 504990 | -90.65 | 11.97 | 60.98 | 0.64 | 2.19 | 572 |
| 2024-09-20 22:21:40.316 | MS1 | 121.4656586807 | 31.1446283371 | 55 | 504990 | -92.06 | 11.06 | 316.55 | 0.18 | 2.02 | 1571 |
| 2024-09-20 22:21:41.772 | MS1 | 121.4656758723 | 31.1446330031 | 55 | 504990 | -89.41 | 7.50 | 336.62 | 0.16 | 2.67 | 1588 |
| 2024-09-20 22:21:42.574 | MS1 | 121.4656750242 | 31.1446256878 | 55 | 504990 | -91.58 | 7.34 | 572.89 | 0.06 | 2.61 | 1564 |

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
| 3236012 | 4 | 121.4642927604 | 31.1556188135 | 179 | 3 | 11 | 24.5 | TDD | 55 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3245136 | 3 | 121.4708289478 | 31.1499324733 | 320 | 0 | 2 | 17.2 | TDD | 121 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3247267 | 1 | 121.4720936598 | 31.1534425428 | 285 | 14 | 9 | 45.2 | TDD | 777 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3248019 | 2 | 121.4670459900 | 31.1547912341 | 290 | 12 | 10 | 24.1 | TDD | 307 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |

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
| 2024-09-20 22:21:31.290 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.311 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.446 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.446 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.186 | NREventA3 | measId:2;ServCellPCI:501;Se... |
| 2024-09-20 22:21:38.426 | NRHandoverAttempt | SourcePCI:501;SourceNR-ARFC... |
| 2024-09-20 22:21:38.460 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.472 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.594 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.594 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3247267 | 1 | 7.4973 | 19.1486 | -114.7401 | 14.0281 | 187.0990 | 0.0107 | 0.0040 |
| 2024_09_20 22:00 | 3248019 | 2 | 7.3371 | 6.9115 | -114.2231 | 18.2782 | 177.5374 | 0.0147 | 0.0075 |
| 2024_09_20 22:00 | 3245136 | 3 | 17.3532 | 9.1918 | -114.3068 | 6.1394 | 105.6585 | 0.0059 | 0.0170 |
| 2024_09_20 22:00 | 3236012 | 4 | 14.6211 | 15.3758 | -117.1492 | 15.0356 | 183.2823 | 0.0074 | 0.0065 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412599_C4A07539 | 504990 | 55 | -89.3 | 504990 | 777 | -101.9 | 504990 | 307 | -100.3 | 504990 | 121 |
| MR_1774412599_BCAEA3EA | 504990 | 55 | -92.0 | 504990 | 777 | -100.2 | 504990 | 307 | -99.4 | 504990 | 121 |
| MR_1774412599_F8436F69 | 504990 | 55 | -91.6 | 504990 | 777 | -102.0 | 504990 | 307 | -99.3 | 504990 | 121 |
| MR_1774412599_8671B448 | 504990 | 55 | -90.8 | 504990 | 777 | -101.8 | 504990 | 307 | -102.3 | 504990 | 121 |
| MR_1774412599_8E3D2E60 | 504990 | 55 | -89.6 | 504990 | 777 | -101.1 | 504990 | 307 | -100.6 | 504990 | 121 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 624: `abbcdf08-69c...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `abbcdf08-69c7-430d-9e50-33f7d0a27a01` |
| Tag | **single-answer** |
| 정답 | **C20** |
| C20 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[624] topology](images/train_0624.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3250321_1
- `C2`: Decrease A3 Offset threshold for 3221577_2
- `C3`: Adjust the azimuth of 3250321_1 by 50 degrees
- `C4`: Decrease A3 Offset threshold for 3250321_1
- `C5`: Lift the tilt angle  of 3250321_1 by 10 degrees
- `C6`: Decrease transmission power for 3221577_2
- `C7`: Increase transmission power for 3221577_2
- `C8`: Increase A3 Offset threshold for 3221577_2
- `C9`: Lift the tilt angle of 3221577_2 by 10 degrees
- `C10`: Press down the tilt angle  of 3250321_1 by 10 degrees
- `C11`: Increase transmission power for 3250321_1
- `C12`: Press down the tilt angle of 3221577_2 by 10 degrees
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3221577_2
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3221577_2
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3250321_1
- `C16`: Adjust the azimuth of 3221577_2 by 50 degrees
- `C17`: Check test server and transmission issues
- `C18`: Add neighbor relationship between 3254217_3 and 3250321_1
- `C19`: Add neighbor relationship between 3221577_2 and 3250321_1
- `C20`: Insufficient data; more data is needed for judgment. **← 정답**
- `C21`: Decrease transmission power for 3250321_1
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3250321_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.111 | MS1 | 121.4656632329 | 31.1446301174 | 321 | 504990 | -85.18 | 14.99 | 326.93 | 0.12 | 2.41 | 1562 |
| 2024-09-20 22:21:32.413 | MS1 | 121.4656685673 | 31.1446189347 | 321 | 504990 | -89.15 | 14.62 | 472.92 | 0.13 | 2.93 | 1584 |
| 2024-09-20 22:21:33.734 | MS1 | 121.4656707248 | 31.1446268539 | 321 | 504990 | -85.96 | 12.40 | 566.33 | 0.12 | 2.54 | 1582 |
| 2024-09-20 22:21:34.931 | MS1 | 121.4656701684 | 31.1446287845 | 321 | 504990 | -91.40 | 17.17 | 79.77 | 0.05 | 2.30 | 1581 |
| 2024-09-20 22:21:35.791 | MS1 | 121.4656598363 | 31.1446334102 | 321 | 504990 | -91.79 | 16.00 | 94.90 | 0.10 | 2.72 | 1568 |
| 2024-09-20 22:21:36.730 | MS1 | 121.4656715931 | 31.1446354183 | 321 | 504990 | -85.69 | 16.47 | 53.18 | 0.16 | 2.98 | 1581 |
| 2024-09-20 22:21:37.833 | MS1 | 121.4656604313 | 31.1446207596 | 321 | 504990 | -90.05 | 8.50 | 87.37 | 0.09 | 2.39 | 1599 |
| 2024-09-20 22:21:38.424 | MS1 | 121.4656675468 | 31.1446363806 | 321 | 504990 | -93.36 | 11.89 | 54.11 | 0.09 | 2.77 | 1589 |
| 2024-09-20 22:21:39.501 | MS1 | 121.4656654664 | 31.1446249870 | 321 | 504990 | -89.81 | 12.56 | 74.79 | 0.08 | 2.27 | 1585 |
| 2024-09-20 22:21:40.789 | MS1 | 121.4656653125 | 31.1446252565 | 321 | 504990 | -90.98 | 12.82 | 500.53 | 0.00 | 2.59 | 1568 |
| 2024-09-20 22:21:41.913 | MS1 | 121.4656585835 | 31.1446219526 | 321 | 504990 | -92.35 | 8.13 | 314.47 | 0.09 | 2.92 | 1570 |
| 2024-09-20 22:21:42.255 | MS1 | 121.4656585757 | 31.1446258779 | 321 | 504990 | -91.91 | 11.04 | 534.11 | 0.08 | 2.49 | 1586 |

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
| 3221577 | 2 | 121.4681869363 | 31.1455016102 | 22 | 12 | 5 | 42.7 | TDD | 321 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3237615 | 4 | 121.4654321551 | 31.1513569000 | 329 | 12 | 11 | 41.9 | TDD | 247 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3250321 | 1 | 121.4669427545 | 31.1466221036 | 284 | 5 | 7 | 49.0 | TDD | 8 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3254217 | 3 | 121.4663742013 | 31.1521030692 | 223 | 12 | 3 | 32.8 | TDD | 523 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |

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
| 2024-09-20 22:21:30.886 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.910 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.024 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.024 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.780 | NREventA3 | measId:2;ServCellPCI:758;Se... |
| 2024-09-20 22:21:38.020 | NRHandoverAttempt | SourcePCI:758;SourceNR-ARFC... |
| 2024-09-20 22:21:38.055 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.069 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.209 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.209 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3250321 | 1 | 87.1751 | 79.8608 | -115.3082 | 13.5501 | 160.3189 | 0.0027 | 0.0077 |
| 2024_09_19 22:00 | 3221577 | 2 | 93.7572 | 75.9947 | -116.1821 | 8.5324 | 137.0075 | 0.0164 | 0.0112 |
| 2024_09_19 22:00 | 3254217 | 3 | 91.3362 | 88.0756 | -117.0464 | 11.3191 | 85.9241 | 0.0005 | 0.0156 |
| 2024_09_19 22:00 | 3237615 | 4 | 93.0562 | 76.0795 | -114.8468 | 13.7302 | 198.7017 | 0.0114 | 0.0191 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415781_DFF35895 | 504990 | 321 | -90.0 | 504990 | 8 | -99.5 | 504990 | 523 | -104.1 | 504990 | 247 |
| MR_1774415781_5794B23F | 504990 | 321 | -93.1 | 504990 | 8 | -102.7 | 504990 | 523 | -102.9 | 504990 | 247 |
| MR_1774415781_7D4C238E | 504990 | 321 | -90.6 | 504990 | 8 | -99.0 | 504990 | 523 | -104.7 | 504990 | 247 |
| MR_1774415781_60E3D3B0 | 504990 | 321 | -91.3 | 504990 | 8 | -101.4 | 504990 | 523 | -105.0 | 504990 | 247 |
| MR_1774415781_B1781792 | 504990 | 321 | -90.0 | 504990 | 8 | -102.3 | 504990 | 523 | -103.3 | 504990 | 247 |
| MR_1774415781_B741BDED | 504990 | 321 | -92.6 | 504990 | 8 | -100.5 | 504990 | 523 | -105.3 | 504990 | 247 |
| MR_1774415781_C0103CCD | 504990 | 321 | -92.5 | 504990 | 8 | -101.0 | 504990 | 523 | -103.2 | 504990 | 247 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 625: `739a8654-311...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `739a8654-311c-4f55-b247-6c9157f0c36b` |
| Tag | **single-answer** |
| 정답 | **C22** |
| C22 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3242116_1 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[625] topology](images/train_0625.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3242116_1
- `C2`: Decrease A3 Offset threshold for 3242116_1
- `C3`: Lift the tilt angle of 3242116_1 by 3 degrees
- `C4`: Increase transmission power for 3242116_1
- `C5`: Lift the tilt angle  of 3221923_3 by 5 degrees
- `C6`: Increase A3 Offset threshold for 3242116_1
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3221923_3
- `C8`: Decrease A3 Offset threshold for 3221923_3
- `C9`: Press down the tilt angle  of 3221923_3 by 5 degrees
- `C10`: Adjust the azimuth of 3242116_1 by 24 degrees
- `C11`: Adjust the azimuth of 3221923_3 by 50 degrees
- `C12`: Add neighbor relationship between 3232051_2 and 3221923_3
- `C13`: Press down the tilt angle of 3242116_1 by 3 degrees
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Increase transmission power for 3221923_3
- `C16`: Decrease transmission power for 3221923_3
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3221923_3
- `C18`: Increase A3 Offset threshold for 3221923_3
- `C19`: Check test server and transmission issues
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3242116_1
- `C21`: Add neighbor relationship between 3242116_1 and 3221923_3
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3242116_1 **← 정답**

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.216 | MS1 | 121.4656642556 | 31.1446183315 | 471 | 504990 | -91.30 | 16.69 | 591.94 | 0.01 | 2.64 | 1586 |
| 2024-09-20 22:21:32.940 | MS1 | 121.4656748785 | 31.1446211898 | 471 | 504990 | -89.36 | 16.93 | 357.04 | 0.06 | 2.88 | 1580 |
| 2024-09-20 22:21:33.197 | MS1 | 121.4656588159 | 31.1446361651 | 471 | 504990 | -88.12 | 12.82 | 552.56 | 0.09 | 2.65 | 1576 |
| 2024-09-20 22:21:34.616 | MS1 | 121.4656687390 | 31.1446337409 | 471 | 504990 | -87.78 | 14.60 | 49.87 | 0.50 | 2.98 | 673 |
| 2024-09-20 22:21:35.739 | MS1 | 121.4656779324 | 31.1446322395 | 471 | 504990 | -89.98 | 15.52 | 92.98 | 0.67 | 2.72 | 552 |
| 2024-09-20 22:21:36.779 | MS1 | 121.4656762702 | 31.1446252395 | 471 | 504990 | -87.30 | 15.38 | 70.94 | 0.54 | 2.74 | 614 |
| 2024-09-20 22:21:37.928 | MS1 | 121.4656749916 | 31.1446183599 | 471 | 504990 | -92.65 | 12.80 | 88.66 | 0.62 | 2.12 | 526 |
| 2024-09-20 22:21:38.727 | MS1 | 121.4656705780 | 31.1446374793 | 471 | 504990 | -92.81 | 12.35 | 79.48 | 0.60 | 2.13 | 592 |
| 2024-09-20 22:21:39.227 | MS1 | 121.4656720211 | 31.1446268283 | 471 | 504990 | -92.53 | 9.24 | 62.18 | 0.59 | 2.40 | 535 |
| 2024-09-20 22:21:40.333 | MS1 | 121.4656735158 | 31.1446190329 | 471 | 504990 | -93.20 | 10.63 | 369.85 | 0.15 | 2.15 | 1571 |
| 2024-09-20 22:21:41.233 | MS1 | 121.4656771294 | 31.1446324925 | 471 | 504990 | -90.51 | 10.22 | 397.49 | 0.07 | 2.17 | 1585 |
| 2024-09-20 22:21:42.587 | MS1 | 121.4656637966 | 31.1446248418 | 471 | 504990 | -89.14 | 11.73 | 379.92 | 0.06 | 2.93 | 1585 |

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
| 3221923 | 3 | 121.4731512663 | 31.1495722205 | 37 | 3 | 0 | 27.0 | TDD | 118 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3232051 | 2 | 121.4700198542 | 31.1544107386 | 19 | 0 | 9 | 41.6 | TDD | 195 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3242116 | 1 | 121.4662409682 | 31.1510336969 | 160 | 0 | 1 | 37.1 | TDD | 471 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3251599 | 4 | 121.4676003790 | 31.1485392086 | 293 | 6 | 3 | 49.9 | TDD | 231 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:31.220 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.237 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.342 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.342 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.112 | NREventA3 | measId:2;ServCellPCI:824;Se... |
| 2024-09-20 22:21:38.352 | NRHandoverAttempt | SourcePCI:824;SourceNR-ARFC... |
| 2024-09-20 22:21:38.388 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.402 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.516 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.516 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3242116 | 1 | 19.9516 | 7.5195 | -117.7546 | 5.0252 | 131.0833 | 0.0041 | 0.0167 |
| 2024_09_20 22:00 | 3232051 | 2 | 11.9780 | 19.2325 | -117.5603 | 14.3835 | 180.9525 | 0.0066 | 0.0047 |
| 2024_09_20 22:00 | 3221923 | 3 | 18.2821 | 8.8440 | -114.8061 | 13.9299 | 173.5601 | 0.0002 | 0.0135 |
| 2024_09_20 22:00 | 3251599 | 4 | 8.7595 | 14.6082 | -117.7340 | 7.7938 | 144.2544 | 0.0163 | 0.0171 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414225_6781AF97 | 504990 | 471 | -89.7 | 504990 | 118 | -93.0 | 504990 | 195 | -96.0 | 504990 | 231 |
| MR_1774414225_E27276DC | 504990 | 471 | -86.5 | 504990 | 118 | -91.8 | 504990 | 195 | -95.6 | 504990 | 231 |
| MR_1774414225_154E9CC3 | 504990 | 471 | -87.6 | 504990 | 118 | -92.1 | 504990 | 195 | -93.9 | 504990 | 231 |
| MR_1774414225_9629FA2C | 504990 | 471 | -88.8 | 504990 | 118 | -90.3 | 504990 | 195 | -93.5 | 504990 | 231 |
| MR_1774414225_E7BE7BAB | 504990 | 471 | -88.3 | 504990 | 118 | -92.6 | 504990 | 195 | -95.3 | 504990 | 231 |
| MR_1774414225_A65957FD | 504990 | 471 | -88.0 | 504990 | 118 | -93.4 | 504990 | 195 | -93.9 | 504990 | 231 |
| MR_1774414225_0E7BF770 | 504990 | 471 | -86.4 | 504990 | 118 | -90.5 | 504990 | 195 | -97.4 | 504990 | 231 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 626: `34e946f6-051...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `34e946f6-0510-46bc-9705-8b4e24dc51dd` |
| Tag | **single-answer** |
| 정답 | **C13** |
| C13 의미 | Add neighbor relationship between 3253589_2 and 3227444_1 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[626] topology](images/train_0626.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3253589_2
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3253589_2
- `C3`: Adjust the azimuth of 3227444_1 by 5 degrees
- `C4`: Check test server and transmission issues
- `C5`: Decrease A3 Offset threshold for 3227444_1
- `C6`: Decrease transmission power for 3227444_1
- `C7`: Decrease transmission power for 3253589_2
- `C8`: Adjust the azimuth of 3253589_2 by 50 degrees
- `C9`: Increase transmission power for 3227444_1
- `C10`: Lift the tilt angle of 3253589_2 by 10 degrees
- `C11`: Increase A3 Offset threshold for 3253589_2
- `C12`: Insufficient data; more data is needed for judgment.
- `C13`: Add neighbor relationship between 3253589_2 and 3227444_1 **← 정답**
- `C14`: Press down the tilt angle of 3253589_2 by 10 degrees
- `C15`: Increase transmission power for 3253589_2
- `C16`: Press down the tilt angle  of 3227444_1 by 4 degrees
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3253589_2
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3227444_1
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3227444_1
- `C20`: Lift the tilt angle  of 3227444_1 by 4 degrees
- `C21`: Add neighbor relationship between 3217305_3 and 3227444_1
- `C22`: Increase A3 Offset threshold for 3227444_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.301 | MS1 | 121.4656581735 | 31.1446294355 | 342 | 504990 | -77.50 | 13.49 | 536.87 | 0.19 | 2.70 | 1587 |
| 2024-09-20 22:21:32.706 | MS1 | 121.4656654967 | 31.1446355655 | 342 | 504990 | -76.35 | 14.43 | 298.68 | 0.03 | 2.47 | 1565 |
| 2024-09-20 22:21:33.981 | MS1 | 121.4656750199 | 31.1446212670 | 342 | 504990 | -82.17 | 15.02 | 328.56 | 0.00 | 2.95 | 1560 |
| 2024-09-20 22:21:34.951 | MS1 | 121.4656767401 | 31.1446263061 | 342 | 504990 | -89.80 | -0.36 | 58.99 | 0.01 | 1.11 | 1570 |
| 2024-09-20 22:21:35.817 | MS1 | 121.4656736394 | 31.1446328205 | 342 | 504990 | -88.01 | -3.90 | 46.10 | 0.02 | 1.04 | 1587 |
| 2024-09-20 22:21:36.199 | MS1 | 121.4656751935 | 31.1446255196 | 342 | 504990 | -88.49 | -1.40 | 49.23 | 0.02 | 1.40 | 1587 |
| 2024-09-20 22:21:37.933 | MS1 | 121.4656619529 | 31.1446201560 | 342 | 504990 | -89.56 | -3.83 | 33.31 | 0.16 | 1.28 | 1564 |
| 2024-09-20 22:21:38.505 | MS1 | 121.4656731382 | 31.1446238200 | 342 | 504990 | -77.12 | 14.25 | 512.54 | 0.07 | 1.05 | 1599 |
| 2024-09-20 22:21:39.189 | MS1 | 121.4656751919 | 31.1446254884 | 342 | 504990 | -79.26 | 16.68 | 364.95 | 0.05 | 1.09 | 1586 |
| 2024-09-20 22:21:40.578 | MS1 | 121.4656597676 | 31.1446322589 | 342 | 504990 | -81.27 | 13.15 | 501.52 | 0.03 | 2.21 | 1583 |
| 2024-09-20 22:21:41.428 | MS1 | 121.4656660265 | 31.1446202441 | 342 | 504990 | -81.25 | 17.98 | 353.32 | 0.01 | 2.83 | 1563 |
| 2024-09-20 22:21:42.846 | MS1 | 121.4656628324 | 31.1446259098 | 342 | 504990 | -81.91 | 14.94 | 452.10 | 0.05 | 2.76 | 1598 |

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
| 3217305 | 3 | 121.4700260650 | 31.1528574830 | 3 | 3 | 7 | 21.7 | TDD | 979 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3227444 | 1 | 121.4730758940 | 31.1558751567 | 204 | 3 | 5 | 17.5 | TDD | 456 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3251951 | 4 | 121.4650118218 | 31.1457677553 | 85 | 10 | 4 | 32.2 | TDD | 318 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3253589 | 2 | 121.4695538995 | 31.1486337530 | 119 | 11 | 0 | 30.0 | TDD | 342 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |

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
| 2024-09-20 22:21:31.187 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.203 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.318 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.318 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.022 | NREventA3 | measId:2;ServCellPCI:128;Se... |
| 2024-09-20 22:21:36.022 | NREventA3 | measId:2;ServCellPCI:128;Se... |
| 2024-09-20 22:21:37.022 | NREventA3 | measId:2;ServCellPCI:128;Se... |
| 2024-09-20 22:21:39.522 | NRRRCReestablishAttempt | PCI:128 |
| 2024-09-20 22:21:39.538 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.551 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:39.697 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.697 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3227444 | 1 | 8.5951 | 7.8797 | -117.0499 | 11.5140 | 152.4434 | 0.0005 | 0.0151 |
| 2024_09_20 22:00 | 3253589 | 2 | 18.1540 | 12.2078 | -116.3419 | 19.1791 | 87.6558 | 0.0050 | 0.1925 |
| 2024_09_20 22:00 | 3217305 | 3 | 18.5032 | 18.6705 | -117.0536 | 18.0433 | 102.8199 | 0.0085 | 0.0067 |
| 2024_09_20 22:00 | 3251951 | 4 | 6.7146 | 16.9332 | -117.5653 | 12.3218 | 125.4787 | 0.0061 | 0.0059 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416023_9B5384C7 | 504990 | 342 | -90.1 | 504990 | 456 | -86.8 | 504990 | 979 | -91.9 | 504990 | 318 |
| MR_1774416023_05D477E0 | 504990 | 342 | -89.7 | 504990 | 456 | -83.8 | 504990 | 979 | -92.9 | 504990 | 318 |
| MR_1774416023_F8E1FAC0 | 504990 | 342 | -90.0 | 504990 | 456 | -86.1 | 504990 | 979 | -92.8 | 504990 | 318 |
| MR_1774416023_F7D43243 | 504990 | 342 | -90.6 | 504990 | 456 | -85.0 | 504990 | 979 | -90.2 | 504990 | 318 |
| MR_1774416023_B71B6623 | 504990 | 342 | -91.4 | 504990 | 456 | -85.2 | 504990 | 979 | -91.5 | 504990 | 318 |
| MR_1774416023_52F57318 | 504990 | 456 | -85.5 | 504990 | 342 | -90.6 | 504990 | 979 | -93.0 | 504990 | 318 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 627: `d9aaa93e-491...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `d9aaa93e-4917-4d22-81e3-4aa63f43f940` |
| Tag | **single-answer** |
| 정답 | **C15** |
| C15 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[627] topology](images/train_0627.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3279501_2
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3279501_2
- `C3`: Decrease transmission power for 3279425_4
- `C4`: Adjust the azimuth of 3279501_2 by 50 degrees
- `C5`: Increase transmission power for 3279425_4
- `C6`: Decrease A3 Offset threshold for 3279501_2
- `C7`: Add neighbor relationship between 3230001_3 and 3279425_4
- `C8`: Increase transmission power for 3279501_2
- `C9`: Add neighbor relationship between 3279501_2 and 3279425_4
- `C10`: Increase A3 Offset threshold for 3279501_2
- `C11`: Decrease A3 Offset threshold for 3279425_4
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3279425_4
- `C13`: Increase A3 Offset threshold for 3279425_4
- `C14`: Lift the tilt angle  of 3279425_4 by 9 degrees
- `C15`: Check test server and transmission issues **← 정답**
- `C16`: Lift the tilt angle of 3279501_2 by 10 degrees
- `C17`: Insufficient data; more data is needed for judgment.
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3279501_2
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3279425_4
- `C20`: Press down the tilt angle  of 3279425_4 by 9 degrees
- `C21`: Adjust the azimuth of 3279425_4 by 7 degrees
- `C22`: Press down the tilt angle of 3279501_2 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.578 | MS1 | 121.4656749578 | 31.1446200499 | 625 | 504990 | -85.78 | 16.37 | 425.16 | 0.08 | 2.63 | 1574 |
| 2024-09-20 22:21:32.379 | MS1 | 121.4656717532 | 31.1446184134 | 625 | 504990 | -91.29 | 14.86 | 378.39 | 0.08 | 2.77 | 1578 |
| 2024-09-20 22:21:33.512 | MS1 | 121.4656753823 | 31.1446316869 | 625 | 504990 | -87.87 | 17.30 | 512.37 | 0.19 | 2.08 | 1563 |
| 2024-09-20 22:21:34.671 | MS1 | 121.4656720830 | 31.1446330843 | 625 | 504990 | -87.19 | 15.11 | 96.57 | 0.06 | 2.01 | 467 |
| 2024-09-20 22:21:35.720 | MS1 | 121.4656739556 | 31.1446224544 | 625 | 504990 | -88.62 | 15.84 | 50.80 | 0.10 | 2.64 | 398 |
| 2024-09-20 22:21:36.954 | MS1 | 121.4656697750 | 31.1446316246 | 625 | 504990 | -85.95 | 15.25 | 55.66 | 0.07 | 2.03 | 410 |
| 2024-09-20 22:21:37.500 | MS1 | 121.4656720914 | 31.1446185095 | 625 | 504990 | -89.60 | 11.07 | 69.70 | 0.14 | 2.63 | 371 |
| 2024-09-20 22:21:38.497 | MS1 | 121.4656673609 | 31.1446187760 | 625 | 504990 | -89.19 | 9.88 | 52.45 | 0.17 | 2.80 | 321 |
| 2024-09-20 22:21:39.851 | MS1 | 121.4656682179 | 31.1446319375 | 625 | 504990 | -91.90 | 10.70 | 67.88 | 0.01 | 2.36 | 350 |
| 2024-09-20 22:21:40.455 | MS1 | 121.4656648866 | 31.1446190836 | 625 | 504990 | -92.46 | 7.62 | 362.64 | 0.17 | 2.47 | 1577 |
| 2024-09-20 22:21:41.185 | MS1 | 121.4656724742 | 31.1446374170 | 625 | 504990 | -93.76 | 11.23 | 600.51 | 0.14 | 2.66 | 1576 |
| 2024-09-20 22:21:42.148 | MS1 | 121.4656757120 | 31.1446356690 | 625 | 504990 | -93.92 | 7.88 | 338.98 | 0.12 | 2.75 | 1560 |

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
| 3230001 | 3 | 121.4711288749 | 31.1462036286 | 292 | 2 | 5 | 18.4 | TDD | 683 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3259325 | 1 | 121.4714220346 | 31.1493716675 | 168 | 5 | 3 | 26.3 | TDD | 72 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3279425 | 4 | 121.4692630130 | 31.1514607728 | 197 | 6 | 9 | 45.3 | TDD | 638 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3279501 | 2 | 121.4735873624 | 31.1529457682 | 316 | 10 | 10 | 29.0 | TDD | 625 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |

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
| 2024-09-20 22:21:31.026 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.041 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.168 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.168 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.872 | NREventA3 | measId:2;ServCellPCI:456;Se... |
| 2024-09-20 22:21:38.112 | NRHandoverAttempt | SourcePCI:456;SourceNR-ARFC... |
| 2024-09-20 22:21:38.157 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.171 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.276 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.276 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3259325 | 1 | 15.7841 | 11.7519 | -116.1946 | 16.9981 | 192.4184 | 0.0069 | 0.0041 |
| 2024_09_20 22:00 | 3279501 | 2 | 13.5671 | 17.3595 | -115.7480 | 16.2965 | 139.3533 | 0.0103 | 0.0103 |
| 2024_09_20 22:00 | 3230001 | 3 | 10.4681 | 10.7507 | -116.0493 | 18.9721 | 172.5185 | 0.0191 | 0.0010 |
| 2024_09_20 22:00 | 3279425 | 4 | 6.0851 | 16.8638 | -116.2874 | 7.2830 | 140.3043 | 0.0067 | 0.0082 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414944_EB2B56DA | 504990 | 625 | -87.2 | 504990 | 638 | -92.4 | 504990 | 683 | -94.6 | 504990 | 72 |
| MR_1774414944_B6BD2609 | 504990 | 625 | -86.9 | 504990 | 638 | -92.7 | 504990 | 683 | -95.2 | 504990 | 72 |
| MR_1774414944_4EE36343 | 504990 | 625 | -88.0 | 504990 | 638 | -92.1 | 504990 | 683 | -92.0 | 504990 | 72 |
| MR_1774414944_69F3F4E7 | 504990 | 625 | -87.5 | 504990 | 638 | -92.3 | 504990 | 683 | -92.5 | 504990 | 72 |
| MR_1774414944_C73C3CE4 | 504990 | 625 | -88.0 | 504990 | 638 | -91.7 | 504990 | 683 | -93.2 | 504990 | 72 |
| MR_1774414944_3F6A89EB | 504990 | 625 | -85.9 | 504990 | 638 | -92.4 | 504990 | 683 | -94.5 | 504990 | 72 |
| MR_1774414944_8145980A | 504990 | 625 | -86.7 | 504990 | 638 | -90.6 | 504990 | 683 | -93.1 | 504990 | 72 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 628: `b9881c31-f52...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `b9881c31-f520-42b4-add3-60572449b5f6` |
| Tag | **single-answer** |
| 정답 | **C8** |
| C8 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[628] topology](images/train_0628.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3242435_3
- `C2`: Decrease transmission power for 3259720_1
- `C3`: Increase A3 Offset threshold for 3259720_1
- `C4`: Press down the tilt angle  of 3259720_1 by 9 degrees
- `C5`: Lift the tilt angle of 3242435_3 by 10 degrees
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3242435_3
- `C7`: Check test server and transmission issues
- `C8`: Insufficient data; more data is needed for judgment. **← 정답**
- `C9`: Increase transmission power for 3259720_1
- `C10`: Decrease A3 Offset threshold for 3259720_1
- `C11`: Add neighbor relationship between 3215031_2 and 3259720_1
- `C12`: Decrease A3 Offset threshold for 3242435_3
- `C13`: Adjust the azimuth of 3259720_1 by 8 degrees
- `C14`: Adjust the azimuth of 3242435_3 by 19 degrees
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3259720_1
- `C16`: Decrease transmission power for 3242435_3
- `C17`: Increase A3 Offset threshold for 3242435_3
- `C18`: Press down the tilt angle of 3242435_3 by 10 degrees
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3259720_1
- `C20`: Add neighbor relationship between 3242435_3 and 3259720_1
- `C21`: Increase transmission power for 3242435_3
- `C22`: Lift the tilt angle  of 3259720_1 by 9 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.321 | MS1 | 121.4656650926 | 31.1446323666 | 454 | 504990 | -89.07 | 13.23 | 579.75 | 0.13 | 2.99 | 1574 |
| 2024-09-20 22:21:32.836 | MS1 | 121.4656774488 | 31.1446307762 | 454 | 504990 | -86.86 | 13.52 | 370.66 | 0.11 | 2.07 | 1591 |
| 2024-09-20 22:21:33.109 | MS1 | 121.4656642753 | 31.1446379934 | 454 | 504990 | -88.62 | 15.21 | 596.72 | 0.05 | 2.11 | 1585 |
| 2024-09-20 22:21:34.479 | MS1 | 121.4656753526 | 31.1446346993 | 454 | 504990 | -86.00 | 14.56 | 104.84 | 0.05 | 2.69 | 1565 |
| 2024-09-20 22:21:35.610 | MS1 | 121.4656606917 | 31.1446288631 | 454 | 504990 | -90.74 | 15.05 | 72.45 | 0.06 | 2.83 | 1560 |
| 2024-09-20 22:21:36.898 | MS1 | 121.4656661956 | 31.1446265572 | 454 | 504990 | -87.38 | 16.00 | 100.17 | 0.06 | 2.06 | 1566 |
| 2024-09-20 22:21:37.466 | MS1 | 121.4656750293 | 31.1446309178 | 454 | 504990 | -89.20 | 8.32 | 85.38 | 0.11 | 2.92 | 1580 |
| 2024-09-20 22:21:38.497 | MS1 | 121.4656602511 | 31.1446232034 | 454 | 504990 | -93.20 | 11.05 | 77.14 | 0.05 | 2.47 | 1576 |
| 2024-09-20 22:21:39.646 | MS1 | 121.4656654049 | 31.1446371792 | 454 | 504990 | -90.01 | 7.69 | 66.48 | 0.18 | 2.85 | 1565 |
| 2024-09-20 22:21:40.995 | MS1 | 121.4656673546 | 31.1446326617 | 454 | 504990 | -92.45 | 7.64 | 439.24 | 0.14 | 2.26 | 1594 |
| 2024-09-20 22:21:41.852 | MS1 | 121.4656600764 | 31.1446195511 | 454 | 504990 | -91.43 | 7.68 | 534.49 | 0.15 | 2.02 | 1566 |
| 2024-09-20 22:21:42.684 | MS1 | 121.4656612536 | 31.1446285399 | 454 | 504990 | -90.06 | 9.55 | 592.94 | 0.05 | 2.42 | 1567 |

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
| 3215031 | 2 | 121.4696357590 | 31.1514954582 | 111 | 8 | 5 | 46.3 | TDD | 370 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3238870 | 4 | 121.4714461060 | 31.1442305023 | 145 | 0 | 2 | 33.2 | TDD | 510 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3242435 | 3 | 121.4720239520 | 31.1442587494 | 293 | 13 | 7 | 49.0 | TDD | 454 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3259720 | 1 | 121.4748241977 | 31.1466274994 | 264 | 8 | 7 | 20.6 | TDD | 97 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |

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
| 2024-09-20 22:21:31.106 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.122 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.247 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.247 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.906 | NREventA3 | measId:2;ServCellPCI:434;Se... |
| 2024-09-20 22:21:38.146 | NRHandoverAttempt | SourcePCI:434;SourceNR-ARFC... |
| 2024-09-20 22:21:38.189 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.203 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.348 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.348 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3259720 | 1 | 93.9723 | 79.1643 | -116.9261 | 8.4593 | 114.7514 | 0.0109 | 0.0132 |
| 2024_09_19 22:00 | 3215031 | 2 | 77.8295 | 89.1176 | -116.9598 | 10.8887 | 99.1789 | 0.0075 | 0.0062 |
| 2024_09_19 22:00 | 3242435 | 3 | 75.0203 | 77.9448 | -115.4494 | 14.5376 | 152.9526 | 0.0105 | 0.0038 |
| 2024_09_19 22:00 | 3238870 | 4 | 78.7313 | 94.8184 | -117.9071 | 11.9962 | 144.2018 | 0.0116 | 0.0160 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414618_A3076399 | 504990 | 454 | -92.1 | 504990 | 97 | -95.7 | 504990 | 370 | -98.8 | 504990 | 510 |
| MR_1774414618_9F4A7B67 | 504990 | 454 | -89.1 | 504990 | 97 | -96.8 | 504990 | 370 | -97.8 | 504990 | 510 |
| MR_1774414618_3E4F2ABA | 504990 | 454 | -91.3 | 504990 | 97 | -95.4 | 504990 | 370 | -96.8 | 504990 | 510 |
| MR_1774414618_4243FEB6 | 504990 | 454 | -92.5 | 504990 | 97 | -97.9 | 504990 | 370 | -97.9 | 504990 | 510 |
| MR_1774414618_BC5EC7B8 | 504990 | 454 | -90.8 | 504990 | 97 | -96.9 | 504990 | 370 | -95.3 | 504990 | 510 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 629: `bb51b94c-c99...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `bb51b94c-c99a-4525-95dd-4667673ab9f2` |
| Tag | **single-answer** |
| 정답 | **C7** |
| C7 의미 | Lift the tilt angle  of 3230937_4 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[629] topology](images/train_0629.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3279145_1 by 4 degrees
- `C2`: Adjust the azimuth of 3230937_4 by 50 degrees
- `C3`: Increase transmission power for 3279145_1
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3237271_3
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3279145_1
- `C6`: Add neighbor relationship between 3230937_4 and 3237271_3
- `C7`: Lift the tilt angle  of 3230937_4 by 10 degrees **← 정답**
- `C8`: Adjust the azimuth of 3279145_1 by 29 degrees
- `C9`: Decrease A3 Offset threshold for 3279145_1
- `C10`: Insufficient data; more data is needed for judgment.
- `C11`: Decrease A3 Offset threshold for 3237271_3
- `C12`: Increase A3 Offset threshold for 3237271_3
- `C13`: Decrease transmission power for 3237271_3
- `C14`: Check test server and transmission issues
- `C15`: Increase A3 Offset threshold for 3279145_1
- `C16`: Press down the tilt angle  of 3230937_4 by 10 degrees
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3279145_1
- `C18`: Press down the tilt angle of 3279145_1 by 4 degrees
- `C19`: Increase transmission power for 3237271_3
- `C20`: Decrease transmission power for 3279145_1
- `C21`: Add neighbor relationship between 3279145_1 and 3237271_3
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3237271_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.879 | MS1 | 121.4656750331 | 31.1446352883 | 696 | 504990 | -85.55 | 16.00 | 454.98 | 0.07 | 2.59 | 1578 |
| 2024-09-20 22:21:32.330 | MS1 | 121.4656686398 | 31.1446314162 | 696 | 504990 | -85.75 | 12.43 | 425.72 | 0.08 | 2.33 | 1598 |
| 2024-09-20 22:21:33.868 | MS1 | 121.4656583525 | 31.1446363657 | 696 | 504990 | -90.54 | 15.18 | 422.97 | 0.09 | 2.73 | 1583 |
| 2024-09-20 22:21:34.188 | MS1 | 121.4656702447 | 31.1446340700 | 696 | 504990 | -88.15 | 14.50 | 74.14 | 0.10 | 2.14 | 1572 |
| 2024-09-20 22:21:35.733 | MS1 | 121.4656713109 | 31.1446210885 | 696 | 504990 | -86.17 | 16.17 | 78.47 | 0.18 | 2.78 | 1573 |
| 2024-09-20 22:21:36.633 | MS1 | 121.4656594780 | 31.1446367884 | 696 | 504990 | -88.72 | 15.13 | 87.70 | 0.06 | 2.32 | 1562 |
| 2024-09-20 22:21:37.249 | MS1 | 121.4656713508 | 31.1446182515 | 696 | 504990 | -91.04 | 7.53 | 77.47 | 0.20 | 2.68 | 1566 |
| 2024-09-20 22:21:38.755 | MS1 | 121.4656750742 | 31.1446361741 | 696 | 504990 | -93.45 | 8.66 | 86.95 | 0.14 | 2.20 | 1590 |
| 2024-09-20 22:21:39.370 | MS1 | 121.4656713106 | 31.1446303200 | 696 | 504990 | -90.08 | 8.79 | 103.59 | 0.11 | 2.00 | 1582 |
| 2024-09-20 22:21:40.509 | MS1 | 121.4656610311 | 31.1446229402 | 696 | 504990 | -93.07 | 7.31 | 597.15 | 0.07 | 2.63 | 1579 |
| 2024-09-20 22:21:41.316 | MS1 | 121.4656586447 | 31.1446229134 | 696 | 504990 | -91.69 | 12.66 | 490.18 | 0.03 | 2.96 | 1567 |
| 2024-09-20 22:21:42.866 | MS1 | 121.4656689574 | 31.1446216046 | 696 | 504990 | -93.16 | 11.79 | 333.27 | 0.05 | 2.66 | 1588 |

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
| 3217033 | 2 | 121.4748492538 | 31.1443435638 | 116 | 0 | 10 | 25.2 | TDD | 961 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3230937 | 4 | 121.4706186849 | 31.1443305859 | 61 | 13 | 10 | 16.1 | TDD | 206 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3237271 | 3 | 121.4693371244 | 31.1548026261 | 17 | 10 | 2 | 17.9 | TDD | 653 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3279145 | 1 | 121.4686785755 | 31.1502475193 | 176 | 2 | 9 | 29.0 | TDD | 696 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |

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
| 2024-09-20 22:21:31.558 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.578 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.691 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.691 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.374 | NREventA3 | measId:2;ServCellPCI:663;Se... |
| 2024-09-20 22:21:38.614 | NRHandoverAttempt | SourcePCI:663;SourceNR-ARFC... |
| 2024-09-20 22:21:38.660 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.674 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.804 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.804 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3279145 | 1 | 81.0769 | 92.0554 | -116.6274 | 16.7513 | 117.5196 | 0.0116 | 0.0197 |
| 2024_09_20 22:00 | 3217033 | 2 | 5.6979 | 13.8241 | -115.2850 | 5.8331 | 161.3923 | 0.0120 | 0.0118 |
| 2024_09_20 22:00 | 3237271 | 3 | 19.5398 | 18.8181 | -114.3136 | 6.0126 | 126.7081 | 0.0084 | 0.0052 |
| 2024_09_20 22:00 | 3230937 | 4 | 17.2539 | 13.4830 | -117.6995 | 15.2214 | 186.6292 | 0.0190 | 0.0178 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414781_88FC0BD6 | 504990 | 696 | -88.0 | 504990 | 653 | -92.1 | 504990 | 206 | -97.5 | 504990 | 961 |
| MR_1774414781_9AAD3E50 | 504990 | 696 | -89.9 | 504990 | 653 | -92.2 | 504990 | 206 | -96.4 | 504990 | 961 |
| MR_1774414781_99CFDF27 | 504990 | 696 | -87.7 | 504990 | 653 | -91.9 | 504990 | 206 | -96.8 | 504990 | 961 |
| MR_1774414781_7FE4EC67 | 504990 | 696 | -88.7 | 504990 | 653 | -91.7 | 504990 | 206 | -96.2 | 504990 | 961 |
| MR_1774414781_034B871D | 504990 | 696 | -89.6 | 504990 | 653 | -90.9 | 504990 | 206 | -97.6 | 504990 | 961 |
| MR_1774414781_1AE67421 | 504990 | 696 | -89.8 | 504990 | 653 | -92.9 | 504990 | 206 | -94.8 | 504990 | 961 |

> *... 2개 열 생략 (전체 14열)*

---
