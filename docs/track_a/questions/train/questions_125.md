# Track A 문제 분석 — train[1240]~train[1249]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[1240] ~ train[1249] (10개)

## 목차

1. [문제 1240: `6d5b3a87-5d9...`](#1240) — single-answer, 정답: C16
2. [문제 1241: `d93beeb0-918...`](#1241) — single-answer, 정답: C21
3. [문제 1242: `6a536744-535...`](#1242) — single-answer, 정답: C13
4. [문제 1243: `499ab3dd-c0d...`](#1243) — single-answer, 정답: C11
5. [문제 1244: `a81a6c5a-2d8...`](#1244) — single-answer, 정답: C20
6. [문제 1245: `4a8f63a6-d9a...`](#1245) — multiple-answer, 정답: C6|C8
7. [문제 1246: `a45c4f4e-bc5...`](#1246) — single-answer, 정답: C22
8. [문제 1247: `3c4551c6-d53...`](#1247) — single-answer, 정답: C12
9. [문제 1248: `ced309eb-7f0...`](#1248) — single-answer, 정답: C11
10. [문제 1249: `aa8811f0-b7f...`](#1249) — single-answer, 정답: C12

---

### 문제 1240: `6d5b3a87-5d9...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `6d5b3a87-5d93-4f60-ae3f-60b94428e959` |
| Tag | **single-answer** |
| 정답 | **C16** |
| C16 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3213711_1 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1240] topology](images/train_1240.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3213711_1 by 5 degrees
- `C2`: Decrease A3 Offset threshold for 3213711_1
- `C3`: Adjust the azimuth of 3250231_5 by 26 degrees
- `C4`: Lift the tilt angle of 3213711_1 by 5 degrees
- `C5`: Lift the tilt angle  of 3250231_5 by 4 degrees
- `C6`: Add neighbor relationship between 3262384_11 and 3250231_5
- `C7`: Decrease A3 Offset threshold for 3250231_5
- `C8`: Decrease transmission power for 3213711_1
- `C9`: Increase transmission power for 3213711_1
- `C10`: Press down the tilt angle  of 3250231_5 by 4 degrees
- `C11`: Check test server and transmission issues
- `C12`: Increase A3 Offset threshold for 3250231_5
- `C13`: Decrease transmission power for 3250231_5
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3213711_1
- `C15`: Increase A3 Offset threshold for 3213711_1
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3213711_1 **← 정답**
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3250231_5
- `C18`: Increase transmission power for 3250231_5
- `C19`: Add neighbor relationship between 3213711_1 and 3250231_5
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3250231_5
- `C21`: Insufficient data; more data is needed for judgment.
- `C22`: Adjust the azimuth of 3213711_1 by 35 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.394 | MS1 | 121.4656717237 | 31.1446350322 | 358 | 504990 | -93.19 | 14.17 | 564.81 | 0.15 | 2.02 | 1572 |
| 2024-09-20 22:21:32.909 | MS1 | 121.4656705475 | 31.1446356260 | 59 | 504990 | -93.20 | 12.21 | 325.13 | 0.16 | 2.36 | 1576 |
| 2024-09-20 22:21:33.894 | MS1 | 121.4656775148 | 31.1446334300 | 15 | 504990 | -93.16 | 11.17 | 352.97 | 0.07 | 2.20 | 1574 |
| 2024-09-20 22:21:34.765 | MS1 | 121.4656640670 | 31.1446377861 | 893 | 152650 | -89.13 | 7.86 | 97.78 | 0.11 | 1.93 | 973 |
| 2024-09-20 22:21:35.952 | MS1 | 121.4656678041 | 31.1446293484 | 829 | 152650 | -88.87 | 5.82 | 95.76 | 0.05 | 1.62 | 961 |
| 2024-09-20 22:21:36.381 | MS1 | 121.4656584221 | 31.1446252929 | 150 | 152650 | -94.35 | 6.12 | 70.03 | 0.04 | 1.90 | 964 |
| 2024-09-20 22:21:37.753 | MS1 | 121.4656759357 | 31.1446286436 | 530 | 152650 | -88.86 | 2.34 | 62.57 | 0.06 | 1.52 | 968 |
| 2024-09-20 22:21:38.894 | MS1 | 121.4656595551 | 31.1446378977 | 893 | 152650 | -90.97 | 4.02 | 86.28 | 0.00 | 1.73 | 959 |
| 2024-09-20 22:21:39.671 | MS1 | 121.4656632047 | 31.1446255621 | 829 | 152650 | -90.29 | 7.08 | 101.61 | 0.10 | 1.57 | 915 |
| 2024-09-20 22:21:40.443 | MS1 | 121.4656649024 | 31.1446279236 | 150 | 152650 | -90.98 | 5.08 | 90.50 | 0.01 | 2.08 | 1565 |
| 2024-09-20 22:21:41.439 | MS1 | 121.4656696356 | 31.1446291090 | 530 | 152650 | -94.34 | 4.32 | 78.99 | 0.17 | 2.28 | 1587 |
| 2024-09-20 22:21:42.893 | MS1 | 121.4656596315 | 31.1446355536 | 893 | 152650 | -96.62 | 4.39 | 79.92 | 0.06 | 2.40 | 1568 |

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
| 3210967 | 4 | 121.4738157685 | 31.1491092554 | 353 | 13 | 5 | 28.3 | TDD | 884 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3213711 | 1 | 121.4694697237 | 31.1554101422 | 162 | 4 | 8 | 22.9 | TDD | 358 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3216677 | 13 | 121.4713016577 | 31.1472253318 | 257 | 10 | 12 | 17.8 | FDD | 829 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |
| 3217131 | 10 | 121.4645080410 | 31.1493974112 | 355 | 14 | 8 | 29.2 | FDD | 530 | n1 | 152650 | 30M | 4T4R | 18 | 152650 |
| 3218735 | 7 | 121.4675079815 | 31.1530725490 | 63 | 1 | 6 | 5.9 | FDD | 964 | n1 | 152650 | 30M | 4T4R | 28 | 152650 |
| 3237229 | 9 | 121.4657277496 | 31.1461092816 | 126 | 13 | 8 | 16.8 | FDD | 849 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |
| 3250231 | 5 | 121.4721008873 | 31.1511732172 | 194 | 3 | 3 | 9.6 | TDD | 790 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3255121 | 12 | 121.4695081084 | 31.1445723901 | 8 | 11 | 6 | 21.7 | FDD | 728 | n1 | 152650 | 30M | 4T4R | 15 | 152650 |
| 3262384 | 11 | 121.4652897839 | 31.1451949232 | 318 | 14 | 9 | 9.5 | FDD | 150 | n1 | 152650 | 30M | 4T4R | 25 | 152650 |
| 3263124 | 8 | 121.4747071673 | 31.1491777642 | 85 | 9 | 11 | 5.2 | FDD | 893 | n1 | 152650 | 30M | 4T4R | 27 | 152650 |
| 3271016 | 6 | 121.4675756782 | 31.1527830279 | 335 | 1 | 0 | 23.2 | TDD | 59 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3276134 | 2 | 121.4754739727 | 31.1515062915 | 351 | 7 | 3 | 6.5 | TDD | 778 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3277059 | 3 | 121.4745829012 | 31.1454311382 | 128 | 5 | 12 | 9.2 | TDD | 15 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |

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
| 2024-09-20 22:21:31.580 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.600 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.747 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.747 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.480 | NREventA2 | measId:1;ServCellPCI:72;Ser... |
| 2024-09-20 22:21:35.609 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.837 | NREventA5 | measId:3;ServCellPCI:72;Ser... |
| 2024-09-20 22:21:35.874 | NRHandoverAttempt | SourcePCI:72;SourceNR-ARFCN... |
| 2024-09-20 22:21:35.915 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.929 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:36.062 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.062 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3213711 | 1 | 12.2917 | 17.6780 | -115.6537 | 7.3857 | 98.4346 | 0.0034 | 0.0088 |
| 2024_09_20 22:00 | 3276134 | 2 | 8.8380 | 16.2474 | -116.8595 | 13.2459 | 105.6929 | 0.0106 | 0.0042 |
| 2024_09_20 22:00 | 3277059 | 3 | 14.3994 | 7.4156 | -114.2834 | 16.0230 | 187.6031 | 0.0056 | 0.0197 |
| 2024_09_20 22:00 | 3210967 | 4 | 14.3213 | 13.7991 | -115.8885 | 15.0209 | 186.5642 | 0.0200 | 0.0177 |
| 2024_09_20 22:00 | 3250231 | 5 | 14.5460 | 13.0444 | -116.6602 | 13.5713 | 165.1731 | 0.0052 | 0.0090 |
| 2024_09_20 22:00 | 3271016 | 6 | 10.6886 | 15.1874 | -114.8017 | 19.9607 | 184.4604 | 0.0073 | 0.0014 |
| 2024_09_20 22:00 | 3218735 | 7 | 6.0794 | 10.9341 | -116.1158 | 4.4490 | 23.3661 | 0.0182 | 0.0073 |
| 2024_09_20 22:00 | 3263124 | 8 | 12.9268 | 8.1401 | -117.0089 | 4.9830 | 59.9228 | 0.0187 | 0.0021 |
| 2024_09_20 22:00 | 3237229 | 9 | 10.9442 | 15.0843 | -117.3197 | 3.1767 | 48.2226 | 0.0057 | 0.0032 |
| 2024_09_20 22:00 | 3217131 | 10 | 19.1272 | 11.9332 | -117.3986 | 4.0474 | 30.3441 | 0.0125 | 0.0047 |
| 2024_09_20 22:00 | 3262384 | 11 | 13.8419 | 6.9861 | -114.9145 | 3.3091 | 35.1815 | 0.0118 | 0.0184 |
| 2024_09_20 22:00 | 3255121 | 12 | 8.5753 | 13.5802 | -117.8495 | 4.2688 | 25.9830 | 0.0034 | 0.0080 |
| 2024_09_20 22:00 | 3216677 | 13 | 15.9985 | 5.6651 | -115.4581 | 3.4994 | 44.1354 | 0.0035 | 0.0093 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414573_EE0D3FB4 | 152650 | 893 | -87.2 | 152650 | 964 | -92.2 | 152650 | 849 | -102.4 | 152650 | 728 |
| MR_1774414573_1577D78F | 504990 | 15 | -93.8 | 504990 | 790 | -96.0 | 504990 | 884 | -96.1 | 504990 | 778 |
| MR_1774414573_121FD1F9 | 504990 | 15 | -92.2 | 504990 | 790 | -93.8 | 504990 | 884 | -98.0 | 504990 | 778 |
| MR_1774414573_31E90F48 | 152650 | 893 | -90.8 | 152650 | 964 | -94.0 | 152650 | 849 | -99.8 | 152650 | 728 |
| MR_1774414573_9CBC5A21 | 152650 | 893 | -91.1 | 152650 | 964 | -92.5 | 152650 | 849 | -100.1 | 152650 | 728 |
| MR_1774414573_47981AA8 | 152650 | 893 | -90.2 | 152650 | 964 | -90.9 | 152650 | 849 | -99.6 | 152650 | 728 |
| MR_1774414573_47F3A0EB | 152650 | 893 | -87.6 | 152650 | 964 | -93.7 | 152650 | 849 | -98.7 | 152650 | 728 |
| MR_1774414573_EC6B83BA | 152650 | 893 | -91.1 | 152650 | 964 | -93.2 | 152650 | 849 | -101.8 | 152650 | 728 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1241: `d93beeb0-918...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `d93beeb0-9182-49f1-be0e-8d14e8c0e0ba` |
| Tag | **single-answer** |
| 정답 | **C21** |
| C21 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3275041_2 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1241] topology](images/train_1241.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3275041_2 by 5 degrees
- `C2`: Add neighbor relationship between 3275041_2 and 3255010_4
- `C3`: Check test server and transmission issues
- `C4`: Lift the tilt angle  of 3255010_4 by 10 degrees
- `C5`: Decrease A3 Offset threshold for 3255010_4
- `C6`: Insufficient data; more data is needed for judgment.
- `C7`: Decrease transmission power for 3275041_2
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3275041_2
- `C9`: Adjust the azimuth of 3255010_4 by 50 degrees
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3255010_4
- `C11`: Increase transmission power for 3255010_4
- `C12`: Add neighbor relationship between 3222473_3 and 3255010_4
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3255010_4
- `C14`: Increase A3 Offset threshold for 3275041_2
- `C15`: Increase A3 Offset threshold for 3255010_4
- `C16`: Decrease transmission power for 3255010_4
- `C17`: Press down the tilt angle of 3275041_2 by 5 degrees
- `C18`: Press down the tilt angle  of 3255010_4 by 10 degrees
- `C19`: Adjust the azimuth of 3275041_2 by 28 degrees
- `C20`: Increase transmission power for 3275041_2
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3275041_2 **← 정답**
- `C22`: Decrease A3 Offset threshold for 3275041_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.245 | MS1 | 121.4656642885 | 31.1446339213 | 51 | 504990 | -87.19 | 12.32 | 490.79 | 0.02 | 2.96 | 1589 |
| 2024-09-20 22:21:32.810 | MS1 | 121.4656581038 | 31.1446337065 | 51 | 504990 | -91.39 | 17.33 | 491.65 | 0.16 | 2.61 | 1564 |
| 2024-09-20 22:21:33.658 | MS1 | 121.4656642695 | 31.1446312149 | 51 | 504990 | -89.78 | 15.47 | 552.72 | 0.10 | 2.54 | 1594 |
| 2024-09-20 22:21:34.586 | MS1 | 121.4656773167 | 31.1446284248 | 51 | 504990 | -88.38 | 12.92 | 70.37 | 0.61 | 2.44 | 501 |
| 2024-09-20 22:21:35.966 | MS1 | 121.4656588762 | 31.1446291954 | 51 | 504990 | -88.72 | 12.08 | 86.11 | 0.56 | 2.25 | 580 |
| 2024-09-20 22:21:36.877 | MS1 | 121.4656672641 | 31.1446354243 | 51 | 504990 | -86.74 | 13.80 | 61.49 | 0.57 | 2.21 | 606 |
| 2024-09-20 22:21:37.336 | MS1 | 121.4656678663 | 31.1446314545 | 51 | 504990 | -89.16 | 9.71 | 51.72 | 0.51 | 2.25 | 533 |
| 2024-09-20 22:21:38.561 | MS1 | 121.4656723845 | 31.1446366197 | 51 | 504990 | -93.70 | 12.84 | 67.69 | 0.60 | 2.03 | 650 |
| 2024-09-20 22:21:39.555 | MS1 | 121.4656690877 | 31.1446185681 | 51 | 504990 | -91.80 | 12.37 | 93.77 | 0.64 | 2.31 | 515 |
| 2024-09-20 22:21:40.502 | MS1 | 121.4656701629 | 31.1446182381 | 51 | 504990 | -93.41 | 10.82 | 517.31 | 0.04 | 2.28 | 1576 |
| 2024-09-20 22:21:41.429 | MS1 | 121.4656630885 | 31.1446253234 | 51 | 504990 | -92.87 | 10.74 | 357.56 | 0.12 | 2.91 | 1597 |
| 2024-09-20 22:21:42.912 | MS1 | 121.4656606591 | 31.1446224622 | 51 | 504990 | -91.04 | 7.46 | 472.89 | 0.06 | 2.02 | 1570 |

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
| 3222473 | 3 | 121.4709027682 | 31.1462001251 | 31 | 11 | 10 | 43.0 | TDD | 716 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3255010 | 4 | 121.4755134279 | 31.1553404791 | 48 | 10 | 9 | 24.0 | TDD | 869 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3257362 | 1 | 121.4703403542 | 31.1520590050 | 323 | 10 | 10 | 42.8 | TDD | 72 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3275041 | 2 | 121.4654548230 | 31.1536276213 | 151 | 4 | 7 | 20.5 | TDD | 51 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |

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
| 2024-09-20 22:21:30.778 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.799 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:30.901 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.901 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.600 | NREventA3 | measId:2;ServCellPCI:694;Se... |
| 2024-09-20 22:21:37.840 | NRHandoverAttempt | SourcePCI:694;SourceNR-ARFC... |
| 2024-09-20 22:21:37.874 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.887 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.037 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.037 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3257362 | 1 | 18.2576 | 11.7487 | -117.3765 | 9.5720 | 137.3159 | 0.0198 | 0.0179 |
| 2024_09_20 22:00 | 3275041 | 2 | 6.4823 | 9.3856 | -117.1240 | 13.0343 | 169.8386 | 0.0029 | 0.0174 |
| 2024_09_20 22:00 | 3222473 | 3 | 15.3682 | 12.9919 | -116.4719 | 17.4030 | 170.8717 | 0.0005 | 0.0044 |
| 2024_09_20 22:00 | 3255010 | 4 | 10.6204 | 6.9846 | -114.4159 | 7.1099 | 84.3274 | 0.0106 | 0.0076 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414007_DC4ACE5E | 504990 | 51 | -87.6 | 504990 | 869 | -93.8 | 504990 | 716 | -99.2 | 504990 | 72 |
| MR_1774414007_0B101A1E | 504990 | 51 | -86.8 | 504990 | 869 | -91.8 | 504990 | 716 | -99.5 | 504990 | 72 |
| MR_1774414007_8389B497 | 504990 | 51 | -90.0 | 504990 | 869 | -94.8 | 504990 | 716 | -98.6 | 504990 | 72 |
| MR_1774414007_3E3D653B | 504990 | 51 | -89.9 | 504990 | 869 | -93.6 | 504990 | 716 | -98.9 | 504990 | 72 |
| MR_1774414007_8616B649 | 504990 | 51 | -89.9 | 504990 | 869 | -94.7 | 504990 | 716 | -99.9 | 504990 | 72 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1242: `6a536744-535...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `6a536744-5354-4c30-b1f0-3b963103c405` |
| Tag | **single-answer** |
| 정답 | **C13** |
| C13 의미 | Lift the tilt angle  of 3256704_2 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1242] topology](images/train_1242.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3234682_4
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3234682_4
- `C3`: Insufficient data; more data is needed for judgment.
- `C4`: Check test server and transmission issues
- `C5`: Increase A3 Offset threshold for 3234682_4
- `C6`: Adjust the azimuth of 3256704_2 by 50 degrees
- `C7`: Increase transmission power for 3210089_3
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3234682_4
- `C9`: Add neighbor relationship between 3256704_2 and 3234682_4
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3210089_3
- `C11`: Decrease transmission power for 3210089_3
- `C12`: Adjust the azimuth of 3210089_3 by 16 degrees
- `C13`: Lift the tilt angle  of 3256704_2 by 10 degrees **← 정답**
- `C14`: Press down the tilt angle  of 3256704_2 by 10 degrees
- `C15`: Lift the tilt angle of 3210089_3 by 3 degrees
- `C16`: Increase transmission power for 3234682_4
- `C17`: Decrease transmission power for 3234682_4
- `C18`: Increase A3 Offset threshold for 3210089_3
- `C19`: Add neighbor relationship between 3210089_3 and 3234682_4
- `C20`: Press down the tilt angle of 3210089_3 by 3 degrees
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3210089_3
- `C22`: Decrease A3 Offset threshold for 3210089_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.909 | MS1 | 121.4656746085 | 31.1446308896 | 206 | 504990 | -90.15 | 17.41 | 592.51 | 0.12 | 2.14 | 1588 |
| 2024-09-20 22:21:32.299 | MS1 | 121.4656744597 | 31.1446378345 | 206 | 504990 | -87.03 | 13.67 | 528.19 | 0.07 | 2.03 | 1574 |
| 2024-09-20 22:21:33.391 | MS1 | 121.4656591189 | 31.1446183781 | 206 | 504990 | -90.84 | 15.21 | 485.18 | 0.15 | 2.59 | 1597 |
| 2024-09-20 22:21:34.469 | MS1 | 121.4656733058 | 31.1446270913 | 206 | 504990 | -85.29 | 16.88 | 69.83 | 0.11 | 2.99 | 1587 |
| 2024-09-20 22:21:35.920 | MS1 | 121.4656762218 | 31.1446353752 | 206 | 504990 | -85.72 | 14.48 | 50.82 | 0.17 | 2.76 | 1597 |
| 2024-09-20 22:21:36.171 | MS1 | 121.4656691193 | 31.1446336034 | 206 | 504990 | -88.25 | 12.51 | 93.13 | 0.01 | 2.01 | 1593 |
| 2024-09-20 22:21:37.159 | MS1 | 121.4656684796 | 31.1446211066 | 206 | 504990 | -92.63 | 12.83 | 104.80 | 0.08 | 2.73 | 1571 |
| 2024-09-20 22:21:38.580 | MS1 | 121.4656603213 | 31.1446285458 | 206 | 504990 | -89.34 | 7.38 | 76.30 | 0.15 | 2.71 | 1581 |
| 2024-09-20 22:21:39.140 | MS1 | 121.4656760517 | 31.1446219693 | 206 | 504990 | -89.95 | 10.77 | 43.46 | 0.05 | 2.80 | 1570 |
| 2024-09-20 22:21:40.725 | MS1 | 121.4656650378 | 31.1446307137 | 206 | 504990 | -89.32 | 7.44 | 311.75 | 0.09 | 2.94 | 1599 |
| 2024-09-20 22:21:41.164 | MS1 | 121.4656591035 | 31.1446312092 | 206 | 504990 | -90.86 | 12.04 | 425.42 | 0.12 | 2.78 | 1587 |
| 2024-09-20 22:21:42.829 | MS1 | 121.4656637243 | 31.1446268253 | 206 | 504990 | -91.79 | 9.26 | 552.68 | 0.07 | 2.60 | 1597 |

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
| 3210089 | 3 | 121.4640286875 | 31.1513743609 | 184 | 0 | 2 | 41.4 | TDD | 206 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3216733 | 1 | 121.4647589749 | 31.1554824142 | 275 | 0 | 12 | 48.0 | TDD | 744 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3234682 | 4 | 121.4671438963 | 31.1506566672 | 272 | 6 | 9 | 45.1 | TDD | 671 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3256704 | 2 | 121.4699921986 | 31.1557560546 | 293 | 8 | 4 | 26.0 | TDD | 173 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |

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
| 2024-09-20 22:21:31.335 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.356 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.480 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.480 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.194 | NREventA3 | measId:2;ServCellPCI:260;Se... |
| 2024-09-20 22:21:38.434 | NRHandoverAttempt | SourcePCI:260;SourceNR-ARFC... |
| 2024-09-20 22:21:38.477 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.491 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.614 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.614 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3216733 | 1 | 17.8544 | 10.6294 | -117.8612 | 6.1432 | 167.6300 | 0.0025 | 0.0069 |
| 2024_09_20 22:00 | 3256704 | 2 | 9.3534 | 13.7992 | -116.0851 | 5.0463 | 146.7434 | 0.0187 | 0.0050 |
| 2024_09_20 22:00 | 3210089 | 3 | 91.5553 | 91.5747 | -116.9790 | 14.4843 | 170.5209 | 0.0123 | 0.0169 |
| 2024_09_20 22:00 | 3234682 | 4 | 12.0457 | 6.3873 | -116.6198 | 19.7384 | 140.4902 | 0.0036 | 0.0040 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412693_FDE5541E | 504990 | 206 | -86.1 | 504990 | 671 | -89.1 | 504990 | 173 | -96.4 | 504990 | 744 |
| MR_1774412693_880939EA | 504990 | 206 | -86.1 | 504990 | 671 | -90.4 | 504990 | 173 | -99.3 | 504990 | 744 |
| MR_1774412693_3F3B2159 | 504990 | 206 | -83.9 | 504990 | 671 | -90.4 | 504990 | 173 | -98.2 | 504990 | 744 |
| MR_1774412693_E0F2B22F | 504990 | 206 | -84.8 | 504990 | 671 | -90.0 | 504990 | 173 | -96.5 | 504990 | 744 |
| MR_1774412693_3AADABF7 | 504990 | 206 | -85.1 | 504990 | 671 | -89.8 | 504990 | 173 | -96.9 | 504990 | 744 |
| MR_1774412693_26105D63 | 504990 | 206 | -84.0 | 504990 | 671 | -90.2 | 504990 | 173 | -98.9 | 504990 | 744 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1243: `499ab3dd-c0d...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `499ab3dd-c0d8-435c-bec3-52b519e06540` |
| Tag | **single-answer** |
| 정답 | **C11** |
| C11 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3236364_2 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1243] topology](images/train_1243.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3236364_2 by 13 degrees
- `C2`: Press down the tilt angle of 3236364_2 by 6 degrees
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3269700_1
- `C4`: Check test server and transmission issues
- `C5`: Increase A3 Offset threshold for 3236364_2
- `C6`: Press down the tilt angle  of 3269700_1 by 9 degrees
- `C7`: Adjust the azimuth of 3269700_1 by 50 degrees
- `C8`: Increase transmission power for 3236364_2
- `C9`: Decrease transmission power for 3236364_2
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3269700_1
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3236364_2 **← 정답**
- `C12`: Increase A3 Offset threshold for 3269700_1
- `C13`: Add neighbor relationship between 3236364_2 and 3269700_1
- `C14`: Decrease A3 Offset threshold for 3236364_2
- `C15`: Add neighbor relationship between 3251752_3 and 3269700_1
- `C16`: Decrease A3 Offset threshold for 3269700_1
- `C17`: Decrease transmission power for 3269700_1
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3236364_2
- `C19`: Insufficient data; more data is needed for judgment.
- `C20`: Lift the tilt angle of 3236364_2 by 6 degrees
- `C21`: Lift the tilt angle  of 3269700_1 by 9 degrees
- `C22`: Increase transmission power for 3269700_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.745 | MS1 | 121.4656648526 | 31.1446207340 | 716 | 504990 | -85.21 | 15.03 | 431.41 | 0.02 | 2.09 | 1575 |
| 2024-09-20 22:21:32.965 | MS1 | 121.4656690834 | 31.1446299036 | 716 | 504990 | -89.53 | 12.70 | 589.99 | 0.07 | 2.29 | 1575 |
| 2024-09-20 22:21:33.462 | MS1 | 121.4656621364 | 31.1446293539 | 716 | 504990 | -90.64 | 16.24 | 411.14 | 0.15 | 2.67 | 1600 |
| 2024-09-20 22:21:34.445 | MS1 | 121.4656688224 | 31.1446251470 | 716 | 504990 | -89.20 | 14.98 | 72.43 | 0.54 | 2.80 | 534 |
| 2024-09-20 22:21:35.162 | MS1 | 121.4656670660 | 31.1446231435 | 716 | 504990 | -88.67 | 16.34 | 60.10 | 0.60 | 2.76 | 661 |
| 2024-09-20 22:21:36.302 | MS1 | 121.4656617201 | 31.1446265267 | 716 | 504990 | -85.80 | 16.95 | 52.90 | 0.61 | 2.68 | 662 |
| 2024-09-20 22:21:37.275 | MS1 | 121.4656666333 | 31.1446239012 | 716 | 504990 | -93.85 | 8.81 | 93.59 | 0.52 | 2.33 | 674 |
| 2024-09-20 22:21:38.184 | MS1 | 121.4656622364 | 31.1446312804 | 716 | 504990 | -91.70 | 11.19 | 55.11 | 0.58 | 2.80 | 645 |
| 2024-09-20 22:21:39.123 | MS1 | 121.4656732266 | 31.1446365714 | 716 | 504990 | -89.34 | 8.42 | 98.04 | 0.51 | 2.34 | 693 |
| 2024-09-20 22:21:40.292 | MS1 | 121.4656668218 | 31.1446319885 | 716 | 504990 | -90.82 | 10.60 | 394.33 | 0.07 | 2.61 | 1565 |
| 2024-09-20 22:21:41.933 | MS1 | 121.4656585843 | 31.1446241151 | 716 | 504990 | -89.12 | 11.79 | 540.20 | 0.20 | 2.50 | 1579 |
| 2024-09-20 22:21:42.668 | MS1 | 121.4656674084 | 31.1446354653 | 716 | 504990 | -93.35 | 11.69 | 420.42 | 0.10 | 2.80 | 1566 |

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
| 3236364 | 2 | 121.4730768122 | 31.1458418325 | 272 | 3 | 7 | 33.6 | TDD | 716 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3251752 | 3 | 121.4737652746 | 31.1440559710 | 261 | 14 | 6 | 37.5 | TDD | 829 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3268524 | 4 | 121.4722313588 | 31.1517344403 | 109 | 7 | 7 | 41.9 | TDD | 382 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3269700 | 1 | 121.4710644366 | 31.1445356132 | 60 | 6 | 3 | 25.9 | TDD | 120 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |

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
| 2024-09-20 22:21:31.453 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.473 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.586 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.586 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.349 | NREventA3 | measId:2;ServCellPCI:865;Se... |
| 2024-09-20 22:21:38.589 | NRHandoverAttempt | SourcePCI:865;SourceNR-ARFC... |
| 2024-09-20 22:21:38.639 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.652 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.763 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.763 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3269700 | 1 | 15.6352 | 5.1993 | -117.4145 | 8.8801 | 190.6662 | 0.0104 | 0.0136 |
| 2024_09_20 22:00 | 3236364 | 2 | 11.9115 | 12.1549 | -117.3215 | 13.8138 | 160.1139 | 0.0198 | 0.0015 |
| 2024_09_20 22:00 | 3251752 | 3 | 5.5720 | 8.0239 | -115.3008 | 13.5242 | 108.6030 | 0.0061 | 0.0092 |
| 2024_09_20 22:00 | 3268524 | 4 | 6.1494 | 18.2640 | -114.1062 | 5.6409 | 86.6626 | 0.0092 | 0.0027 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412060_61BA5320 | 504990 | 716 | -89.7 | 504990 | 120 | -93.9 | 504990 | 829 | -100.1 | 504990 | 382 |
| MR_1774412060_6A960A58 | 504990 | 716 | -88.8 | 504990 | 120 | -93.8 | 504990 | 829 | -98.8 | 504990 | 382 |
| MR_1774412060_C17C737B | 504990 | 716 | -88.3 | 504990 | 120 | -96.0 | 504990 | 829 | -98.5 | 504990 | 382 |
| MR_1774412060_2AC3C2B7 | 504990 | 716 | -89.7 | 504990 | 120 | -95.2 | 504990 | 829 | -99.3 | 504990 | 382 |
| MR_1774412060_1968D942 | 504990 | 716 | -89.9 | 504990 | 120 | -95.6 | 504990 | 829 | -101.1 | 504990 | 382 |
| MR_1774412060_FB10BCB8 | 504990 | 716 | -90.8 | 504990 | 120 | -94.2 | 504990 | 829 | -98.5 | 504990 | 382 |
| MR_1774412060_C6675D5C | 504990 | 716 | -88.6 | 504990 | 120 | -95.1 | 504990 | 829 | -101.6 | 504990 | 382 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1244: `a81a6c5a-2d8...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `a81a6c5a-2d84-4b14-a2ad-140bab07bb26` |
| Tag | **single-answer** |
| 정답 | **C20** |
| C20 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1244] topology](images/train_1244.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3258894_3
- `C2`: Press down the tilt angle of 3260202_4 by 10 degrees
- `C3`: Decrease transmission power for 3258894_3
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3260202_4
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3260202_4
- `C6`: Adjust the azimuth of 3258894_3 by 44 degrees
- `C7`: Check test server and transmission issues
- `C8`: Lift the tilt angle  of 3258894_3 by 8 degrees
- `C9`: Decrease transmission power for 3260202_4
- `C10`: Press down the tilt angle  of 3258894_3 by 8 degrees
- `C11`: Lift the tilt angle of 3260202_4 by 10 degrees
- `C12`: Add neighbor relationship between 3260202_4 and 3258894_3
- `C13`: Add neighbor relationship between 3270825_2 and 3258894_3
- `C14`: Decrease A3 Offset threshold for 3260202_4
- `C15`: Increase A3 Offset threshold for 3260202_4
- `C16`: Increase A3 Offset threshold for 3258894_3
- `C17`: Increase transmission power for 3258894_3
- `C18`: Increase transmission power for 3260202_4
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3258894_3
- `C20`: Insufficient data; more data is needed for judgment. **← 정답**
- `C21`: Adjust the azimuth of 3260202_4 by 50 degrees
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3258894_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.516 | MS1 | 121.4656608077 | 31.1446262522 | 831 | 504990 | -88.38 | 13.63 | 469.83 | 0.16 | 2.41 | 1573 |
| 2024-09-20 22:21:32.756 | MS1 | 121.4656677826 | 31.1446212582 | 831 | 504990 | -85.67 | 16.45 | 333.94 | 0.19 | 2.56 | 1560 |
| 2024-09-20 22:21:33.788 | MS1 | 121.4656589839 | 31.1446248746 | 831 | 504990 | -87.25 | 12.92 | 389.23 | 0.03 | 2.29 | 1589 |
| 2024-09-20 22:21:34.800 | MS1 | 121.4656593822 | 31.1446360915 | 831 | 504990 | -86.71 | 16.01 | 92.31 | 0.04 | 2.78 | 1585 |
| 2024-09-20 22:21:35.681 | MS1 | 121.4656661071 | 31.1446338886 | 831 | 504990 | -89.21 | 14.01 | 56.90 | 0.01 | 2.65 | 1570 |
| 2024-09-20 22:21:36.959 | MS1 | 121.4656615503 | 31.1446236049 | 831 | 504990 | -86.87 | 13.38 | 89.46 | 0.01 | 2.08 | 1579 |
| 2024-09-20 22:21:37.212 | MS1 | 121.4656661726 | 31.1446209743 | 831 | 504990 | -93.33 | 8.41 | 74.77 | 0.15 | 2.80 | 1560 |
| 2024-09-20 22:21:38.565 | MS1 | 121.4656629671 | 31.1446350883 | 831 | 504990 | -89.83 | 9.79 | 78.68 | 0.04 | 2.51 | 1579 |
| 2024-09-20 22:21:39.492 | MS1 | 121.4656658430 | 31.1446366066 | 831 | 504990 | -89.16 | 9.56 | 107.92 | 0.11 | 2.89 | 1588 |
| 2024-09-20 22:21:40.962 | MS1 | 121.4656733704 | 31.1446194336 | 831 | 504990 | -89.76 | 11.03 | 360.15 | 0.15 | 2.57 | 1573 |
| 2024-09-20 22:21:41.345 | MS1 | 121.4656587281 | 31.1446248305 | 831 | 504990 | -93.43 | 11.93 | 357.56 | 0.17 | 2.81 | 1595 |
| 2024-09-20 22:21:42.210 | MS1 | 121.4656612397 | 31.1446244431 | 831 | 504990 | -92.23 | 12.83 | 456.05 | 0.10 | 2.09 | 1575 |

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
| 3232956 | 1 | 121.4759718174 | 31.1517019795 | 239 | 10 | 3 | 24.5 | TDD | 731 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3258894 | 3 | 121.4702643133 | 31.1440674012 | 234 | 6 | 7 | 16.5 | TDD | 686 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3260202 | 4 | 121.4731189171 | 31.1514798059 | 68 | 13 | 10 | 44.3 | TDD | 831 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3270825 | 2 | 121.4746967269 | 31.1555062604 | 16 | 14 | 3 | 22.0 | TDD | 741 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |

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
| 2024-09-20 22:21:30.803 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.822 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:30.935 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.935 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.687 | NREventA3 | measId:2;ServCellPCI:206;Se... |
| 2024-09-20 22:21:37.927 | NRHandoverAttempt | SourcePCI:206;SourceNR-ARFC... |
| 2024-09-20 22:21:37.975 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.986 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.117 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.117 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3232956 | 1 | 78.9155 | 81.5859 | -116.9943 | 5.6149 | 175.5209 | 0.0087 | 0.0007 |
| 2024_09_19 22:00 | 3270825 | 2 | 82.1036 | 88.3117 | -117.7337 | 7.0943 | 173.1235 | 0.0158 | 0.0054 |
| 2024_09_19 22:00 | 3258894 | 3 | 77.1686 | 93.8712 | -115.8561 | 9.5555 | 138.6281 | 0.0018 | 0.0047 |
| 2024_09_19 22:00 | 3260202 | 4 | 93.6510 | 91.2344 | -116.4118 | 12.6883 | 137.6754 | 0.0066 | 0.0121 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414592_DD2272CB | 504990 | 831 | -85.7 | 504990 | 686 | -88.2 | 504990 | 741 | -98.0 | 504990 | 731 |
| MR_1774414592_C58F7B4C | 504990 | 831 | -87.5 | 504990 | 686 | -88.4 | 504990 | 741 | -97.9 | 504990 | 731 |
| MR_1774414592_E2D3C870 | 504990 | 831 | -86.7 | 504990 | 686 | -85.6 | 504990 | 741 | -97.3 | 504990 | 731 |
| MR_1774414592_9F182198 | 504990 | 831 | -87.8 | 504990 | 686 | -85.9 | 504990 | 741 | -98.4 | 504990 | 731 |
| MR_1774414592_18DE85B6 | 504990 | 831 | -85.2 | 504990 | 686 | -87.7 | 504990 | 741 | -99.4 | 504990 | 731 |
| MR_1774414592_84604F85 | 504990 | 831 | -87.3 | 504990 | 686 | -86.8 | 504990 | 741 | -97.1 | 504990 | 731 |
| MR_1774414592_4B9EB572 | 504990 | 831 | -85.2 | 504990 | 686 | -86.1 | 504990 | 741 | -98.0 | 504990 | 731 |
| MR_1774414592_C154C8DB | 504990 | 831 | -86.6 | 504990 | 686 | -88.2 | 504990 | 741 | -99.4 | 504990 | 731 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1245: `4a8f63a6-d9a...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `4a8f63a6-d9a0-4ff7-a03e-c8248a939246` |
| Tag | **multiple-answer** |
| 정답 | **C6|C8** |
| C6 의미 | Decrease transmission power for 3220223_4 |
| C8 의미 | Press down the tilt angle  of 3220223_4 by 4 degrees |
| 패턴 분류 | **P3 Overshoot (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1245] topology](images/train_1245.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3212727_3 and 3220223_4
- `C2`: Lift the tilt angle  of 3220223_4 by 4 degrees
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3241671_1
- `C4`: Increase transmission power for 3241671_1
- `C5`: Increase A3 Offset threshold for 3220223_4
- `C6`: Decrease transmission power for 3220223_4 **← 정답**
- `C7`: Adjust the azimuth of 3241671_1 by 15 degrees
- `C8`: Press down the tilt angle  of 3220223_4 by 4 degrees **← 정답**
- `C9`: Decrease A3 Offset threshold for 3241671_1
- `C10`: Decrease A3 Offset threshold for 3220223_4
- `C11`: Insufficient data; more data is needed for judgment.
- `C12`: Adjust the azimuth of 3220223_4 by 0 degrees
- `C13`: Press down the tilt angle of 3241671_1 by 4 degrees
- `C14`: Decrease transmission power for 3241671_1
- `C15`: Increase A3 Offset threshold for 3241671_1
- `C16`: Check test server and transmission issues
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3241671_1
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3220223_4
- `C19`: Lift the tilt angle of 3241671_1 by 4 degrees
- `C20`: Increase transmission power for 3220223_4
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3220223_4
- `C22`: Add neighbor relationship between 3241671_1 and 3220223_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.667 | MS1 | 121.4656592446 | 31.1446332550 | 603 | 504990 | -82.45 | 12.07 | 469.15 | 0.02 | 2.79 | 1570 |
| 2024-09-20 22:21:32.725 | MS1 | 121.4656684668 | 31.1446292926 | 603 | 504990 | -76.25 | 15.58 | 317.24 | 0.09 | 2.51 | 1580 |
| 2024-09-20 22:21:33.622 | MS1 | 121.4656634523 | 31.1446220713 | 603 | 504990 | -76.15 | 13.08 | 549.95 | 0.13 | 2.87 | 1580 |
| 2024-09-20 22:21:34.333 | MS1 | 121.4656710766 | 31.1446196354 | 603 | 504990 | -93.51 | 1.94 | 78.38 | 0.01 | 1.05 | 1573 |
| 2024-09-20 22:21:35.922 | MS1 | 121.4656660590 | 31.1446283591 | 603 | 504990 | -87.83 | 3.09 | 43.96 | 0.13 | 1.04 | 1600 |
| 2024-09-20 22:21:36.230 | MS1 | 121.4656725804 | 31.1446326857 | 603 | 504990 | -94.17 | 0.64 | 55.34 | 0.00 | 1.08 | 1597 |
| 2024-09-20 22:21:37.333 | MS1 | 121.4656634709 | 31.1446356270 | 603 | 504990 | -87.70 | 0.59 | 64.90 | 0.08 | 1.25 | 1591 |
| 2024-09-20 22:21:38.621 | MS1 | 121.4656602356 | 31.1446239970 | 603 | 504990 | -92.63 | 0.36 | 76.49 | 0.18 | 1.36 | 1579 |
| 2024-09-20 22:21:39.206 | MS1 | 121.4656751427 | 31.1446182597 | 603 | 504990 | -87.79 | 2.07 | 85.88 | 0.15 | 1.28 | 1591 |
| 2024-09-20 22:21:40.761 | MS1 | 121.4656774920 | 31.1446195915 | 603 | 504990 | -79.50 | 12.99 | 524.91 | 0.18 | 2.67 | 1571 |
| 2024-09-20 22:21:41.885 | MS1 | 121.4656597296 | 31.1446361689 | 603 | 504990 | -77.46 | 16.91 | 585.58 | 0.13 | 2.71 | 1573 |
| 2024-09-20 22:21:42.113 | MS1 | 121.4656653060 | 31.1446264166 | 603 | 504990 | -82.21 | 12.17 | 488.28 | 0.10 | 2.80 | 1582 |

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
| 3212727 | 3 | 121.4671766468 | 31.1498198426 | 233 | 2 | 8 | 40.7 | TDD | 109 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3220223 | 4 | 121.4726356288 | 31.1509563556 | 223 | 2 | 4 | 31.5 | TDD | 661 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3241671 | 1 | 121.4705536987 | 31.1503262212 | 201 | 2 | 5 | 31.6 | TDD | 603 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3278854 | 2 | 121.4724202309 | 31.1559274335 | 13 | 2 | 2 | 39.5 | TDD | 182 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |

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
| 2024-09-20 22:21:30.918 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.939 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.040 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.040 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3241671 | 1 | 7.6907 | 14.3201 | -109.2441 | 9.0954 | 93.7655 | 0.0170 | 0.0093 |
| 2024_09_20 22:00 | 3278854 | 2 | 19.4597 | 13.6640 | -115.1156 | 12.5406 | 120.9639 | 0.0057 | 0.0032 |
| 2024_09_20 22:00 | 3212727 | 3 | 17.9465 | 10.2862 | -116.1336 | 16.7805 | 178.8679 | 0.0073 | 0.0112 |
| 2024_09_20 22:00 | 3220223 | 4 | 11.3680 | 8.8806 | -114.4598 | 7.1595 | 168.5766 | 0.0187 | 0.0164 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413742_8BDBDEA3 | 504990 | 661 | -93.7 | 504990 | 603 | -92.3 | 504990 | 109 | -92.1 | 504990 | 182 |
| MR_1774413742_FB81BC39 | 504990 | 603 | -94.9 | 504990 | 661 | -89.5 | 504990 | 109 | -89.8 | 504990 | 182 |
| MR_1774413742_E8E184D2 | 504990 | 661 | -91.9 | 504990 | 603 | -91.3 | 504990 | 109 | -89.3 | 504990 | 182 |
| MR_1774413742_24071D3D | 504990 | 603 | -94.4 | 504990 | 661 | -90.4 | 504990 | 109 | -89.3 | 504990 | 182 |
| MR_1774413742_19D9CEDE | 504990 | 661 | -94.3 | 504990 | 603 | -92.3 | 504990 | 109 | -89.5 | 504990 | 182 |
| MR_1774413742_77D5F2CF | 504990 | 661 | -94.1 | 504990 | 603 | -89.8 | 504990 | 109 | -88.8 | 504990 | 182 |
| MR_1774413742_E1306171 | 504990 | 603 | -93.5 | 504990 | 661 | -89.4 | 504990 | 109 | -91.5 | 504990 | 182 |
| MR_1774413742_D8AA264D | 504990 | 603 | -94.7 | 504990 | 661 | -90.6 | 504990 | 109 | -89.0 | 504990 | 182 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1246: `a45c4f4e-bc5...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `a45c4f4e-bc5c-44be-b09b-cc97b9803f09` |
| Tag | **single-answer** |
| 정답 | **C22** |
| C22 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3231803_4 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1246] topology](images/train_1246.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3231803_4 by 2 degrees
- `C2`: Check test server and transmission issues
- `C3`: Adjust the azimuth of 3231803_4 by 39 degrees
- `C4`: Decrease transmission power for 3245589_5
- `C5`: Lift the tilt angle  of 3245589_5 by 5 degrees
- `C6`: Increase A3 Offset threshold for 3231803_4
- `C7`: Increase transmission power for 3245589_5
- `C8`: Add neighbor relationship between 3261433_8 and 3245589_5
- `C9`: Press down the tilt angle  of 3245589_5 by 5 degrees
- `C10`: Decrease A3 Offset threshold for 3231803_4
- `C11`: Adjust the azimuth of 3245589_5 by 3 degrees
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3245589_5
- `C13`: Increase transmission power for 3231803_4
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3245589_5
- `C15`: Lift the tilt angle of 3231803_4 by 2 degrees
- `C16`: Increase A3 Offset threshold for 3245589_5
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3231803_4
- `C18`: Decrease A3 Offset threshold for 3245589_5
- `C19`: Add neighbor relationship between 3231803_4 and 3245589_5
- `C20`: Decrease transmission power for 3231803_4
- `C21`: Insufficient data; more data is needed for judgment.
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3231803_4 **← 정답**

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.163 | MS1 | 121.4656606376 | 31.1446293215 | 649 | 504990 | -94.19 | 13.94 | 405.95 | 0.11 | 2.99 | 1591 |
| 2024-09-20 22:21:32.472 | MS1 | 121.4656737641 | 31.1446286037 | 867 | 504990 | -94.37 | 10.05 | 307.07 | 0.13 | 2.24 | 1580 |
| 2024-09-20 22:21:33.901 | MS1 | 121.4656658459 | 31.1446217719 | 711 | 504990 | -95.70 | 13.59 | 500.86 | 0.15 | 2.18 | 1581 |
| 2024-09-20 22:21:34.485 | MS1 | 121.4656717813 | 31.1446328477 | 58 | 152650 | -89.28 | 7.16 | 69.94 | 0.14 | 1.67 | 960 |
| 2024-09-20 22:21:35.996 | MS1 | 121.4656723171 | 31.1446277520 | 187 | 152650 | -93.38 | 5.53 | 85.93 | 0.02 | 1.65 | 924 |
| 2024-09-20 22:21:36.987 | MS1 | 121.4656591643 | 31.1446349609 | 525 | 152650 | -91.23 | 4.92 | 107.00 | 0.14 | 1.73 | 933 |
| 2024-09-20 22:21:37.827 | MS1 | 121.4656626770 | 31.1446211296 | 567 | 152650 | -87.04 | 3.09 | 47.51 | 0.11 | 2.00 | 990 |
| 2024-09-20 22:21:38.423 | MS1 | 121.4656706731 | 31.1446220864 | 58 | 152650 | -93.85 | 5.51 | 52.36 | 0.10 | 1.86 | 999 |
| 2024-09-20 22:21:39.174 | MS1 | 121.4656690410 | 31.1446362414 | 187 | 152650 | -94.07 | 5.53 | 58.22 | 0.10 | 1.96 | 979 |
| 2024-09-20 22:21:40.703 | MS1 | 121.4656721984 | 31.1446184607 | 525 | 152650 | -90.01 | 2.09 | 60.97 | 0.02 | 2.82 | 1570 |
| 2024-09-20 22:21:41.206 | MS1 | 121.4656708686 | 31.1446271203 | 567 | 152650 | -96.41 | 7.51 | 55.77 | 0.06 | 2.93 | 1596 |
| 2024-09-20 22:21:42.244 | MS1 | 121.4656712750 | 31.1446310977 | 58 | 152650 | -91.60 | 7.90 | 99.95 | 0.16 | 2.67 | 1593 |

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
| 3224566 | 7 | 121.4724282454 | 31.1454252996 | 154 | 6 | 10 | 5.5 | FDD | 204 | n1 | 152650 | 30M | 4T4R | 10 | 152650 |
| 3231803 | 4 | 121.4750046495 | 31.1485987161 | 205 | 1 | 1 | 10.8 | TDD | 649 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3234602 | 3 | 121.4717358750 | 31.1461257974 | 119 | 7 | 6 | 3.8 | TDD | 711 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3245589 | 5 | 121.4661895197 | 31.1531931701 | 186 | 4 | 6 | 19.2 | TDD | 335 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3252701 | 11 | 121.4758727829 | 31.1551657586 | 118 | 10 | 11 | 25.2 | FDD | 58 | n1 | 152650 | 30M | 4T4R | 11 | 152650 |
| 3258446 | 6 | 121.4652348119 | 31.1552151768 | 108 | 13 | 7 | 4.7 | TDD | 671 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3259696 | 10 | 121.4699212627 | 31.1497309644 | 306 | 5 | 9 | 20.6 | FDD | 567 | n1 | 152650 | 30M | 4T4R | 26 | 152650 |
| 3261433 | 8 | 121.4733174909 | 31.1449897117 | 296 | 15 | 11 | 22.1 | FDD | 525 | n1 | 152650 | 30M | 4T4R | 10 | 152650 |
| 3268501 | 13 | 121.4662704429 | 31.1542342729 | 70 | 3 | 11 | 19.8 | FDD | 895 | n1 | 152650 | 30M | 4T4R | 27 | 152650 |
| 3272970 | 2 | 121.4646895992 | 31.1445704954 | 358 | 14 | 1 | 18.5 | TDD | 867 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3273694 | 9 | 121.4644952066 | 31.1545397764 | 21 | 4 | 2 | 17.2 | FDD | 243 | n1 | 152650 | 30M | 4T4R | 15 | 152650 |
| 3274477 | 12 | 121.4696698290 | 31.1519548956 | 311 | 8 | 0 | 14.4 | FDD | 187 | n1 | 152650 | 30M | 4T4R | 29 | 152650 |
| 3276172 | 1 | 121.4705210933 | 31.1473932049 | 298 | 8 | 6 | 29.8 | TDD | 864 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |

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
| 2024-09-20 22:21:31.065 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.085 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.235 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.235 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.928 | NREventA2 | measId:1;ServCellPCI:644;Se... |
| 2024-09-20 22:21:35.038 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.293 | NREventA5 | measId:3;ServCellPCI:644;Se... |
| 2024-09-20 22:21:35.362 | NRHandoverAttempt | SourcePCI:644;SourceNR-ARFC... |
| 2024-09-20 22:21:35.389 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.404 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:35.512 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.512 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3276172 | 1 | 16.4172 | 9.3626 | -117.1820 | 10.6109 | 181.2593 | 0.0031 | 0.0145 |
| 2024_09_20 22:00 | 3272970 | 2 | 10.0344 | 5.4436 | -117.5014 | 15.2420 | 185.4910 | 0.0094 | 0.0141 |
| 2024_09_20 22:00 | 3234602 | 3 | 18.2528 | 11.1594 | -116.3168 | 16.7542 | 87.7239 | 0.0034 | 0.0115 |
| 2024_09_20 22:00 | 3231803 | 4 | 6.4992 | 18.2755 | -115.5421 | 12.2201 | 86.6153 | 0.0151 | 0.0071 |
| 2024_09_20 22:00 | 3245589 | 5 | 10.1101 | 9.4344 | -115.6862 | 6.7807 | 195.0543 | 0.0173 | 0.0166 |
| 2024_09_20 22:00 | 3258446 | 6 | 9.2933 | 14.1202 | -117.5543 | 5.8347 | 85.4766 | 0.0150 | 0.0049 |
| 2024_09_20 22:00 | 3224566 | 7 | 9.1319 | 19.5339 | -115.9539 | 4.4217 | 22.3270 | 0.0149 | 0.0106 |
| 2024_09_20 22:00 | 3261433 | 8 | 11.8334 | 9.7680 | -116.7978 | 3.5908 | 21.1986 | 0.0114 | 0.0029 |
| 2024_09_20 22:00 | 3273694 | 9 | 14.1979 | 18.1107 | -117.2185 | 4.8439 | 44.7760 | 0.0004 | 0.0009 |
| 2024_09_20 22:00 | 3259696 | 10 | 5.3613 | 13.2494 | -114.0341 | 3.2478 | 47.7553 | 0.0144 | 0.0192 |
| 2024_09_20 22:00 | 3252701 | 11 | 13.9592 | 11.2559 | -116.6516 | 3.2651 | 27.0112 | 0.0165 | 0.0199 |
| 2024_09_20 22:00 | 3274477 | 12 | 12.0747 | 19.8121 | -115.0679 | 4.9396 | 56.1051 | 0.0180 | 0.0081 |
| 2024_09_20 22:00 | 3268501 | 13 | 18.0370 | 6.4018 | -114.4726 | 3.2310 | 58.2262 | 0.0123 | 0.0092 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415556_CB449260 | 152650 | 58 | -88.3 | 152650 | 895 | -94.2 | 152650 | 243 | -96.8 | 152650 | 204 |
| MR_1774415556_37C3C1E7 | 504990 | 711 | -97.6 | 504990 | 335 | -92.5 | 504990 | 864 | -95.2 | 504990 | 671 |
| MR_1774415556_1E26DADA | 152650 | 58 | -89.0 | 152650 | 895 | -95.9 | 152650 | 243 | -96.2 | 152650 | 204 |
| MR_1774415556_F463146E | 504990 | 711 | -95.8 | 504990 | 335 | -95.4 | 504990 | 864 | -96.4 | 504990 | 671 |
| MR_1774415556_E5A316DF | 152650 | 58 | -89.6 | 152650 | 895 | -95.1 | 152650 | 243 | -99.5 | 152650 | 204 |
| MR_1774415556_7C412C66 | 504990 | 711 | -96.2 | 504990 | 335 | -92.2 | 504990 | 864 | -98.2 | 504990 | 671 |
| MR_1774415556_DBC31A97 | 504990 | 711 | -94.5 | 504990 | 335 | -93.0 | 504990 | 864 | -97.5 | 504990 | 671 |
| MR_1774415556_F1F16BF0 | 152650 | 58 | -88.8 | 152650 | 895 | -94.0 | 152650 | 243 | -95.7 | 152650 | 204 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1247: `3c4551c6-d53...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `3c4551c6-d539-4bc5-ac47-44c8d59589b9` |
| Tag | **single-answer** |
| 정답 | **C12** |
| C12 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3226602_6 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1247] topology](images/train_1247.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3232126_3
- `C2`: Increase transmission power for 3232126_3
- `C3`: Decrease A3 Offset threshold for 3226602_6
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3226602_6
- `C5`: Increase A3 Offset threshold for 3226602_6
- `C6`: Add neighbor relationship between 3265278_7 and 3232126_3
- `C7`: Press down the tilt angle  of 3232126_3 by 4 degrees
- `C8`: Check test server and transmission issues
- `C9`: Lift the tilt angle of 3226602_6 by 1 degrees
- `C10`: Adjust the azimuth of 3226602_6 by 38 degrees
- `C11`: Increase transmission power for 3226602_6
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3226602_6 **← 정답**
- `C13`: Lift the tilt angle  of 3232126_3 by 4 degrees
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Decrease A3 Offset threshold for 3232126_3
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3232126_3
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3232126_3
- `C18`: Press down the tilt angle of 3226602_6 by 1 degrees
- `C19`: Decrease transmission power for 3226602_6
- `C20`: Increase A3 Offset threshold for 3232126_3
- `C21`: Adjust the azimuth of 3232126_3 by 4 degrees
- `C22`: Add neighbor relationship between 3226602_6 and 3232126_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.127 | MS1 | 121.4656698966 | 31.1446272232 | 511 | 504990 | -95.94 | 9.45 | 432.78 | 0.13 | 2.14 | 1571 |
| 2024-09-20 22:21:32.692 | MS1 | 121.4656638124 | 31.1446197773 | 67 | 504990 | -95.26 | 10.74 | 416.56 | 0.11 | 2.89 | 1598 |
| 2024-09-20 22:21:33.712 | MS1 | 121.4656586955 | 31.1446193705 | 861 | 504990 | -95.95 | 13.08 | 417.49 | 0.14 | 2.66 | 1564 |
| 2024-09-20 22:21:34.262 | MS1 | 121.4656650020 | 31.1446353611 | 189 | 152650 | -87.96 | 3.11 | 74.83 | 0.13 | 2.00 | 928 |
| 2024-09-20 22:21:35.120 | MS1 | 121.4656733561 | 31.1446251518 | 669 | 152650 | -92.48 | 3.49 | 103.61 | 0.20 | 1.77 | 987 |
| 2024-09-20 22:21:36.475 | MS1 | 121.4656719750 | 31.1446238486 | 481 | 152650 | -96.57 | 4.56 | 70.36 | 0.06 | 1.50 | 950 |
| 2024-09-20 22:21:37.469 | MS1 | 121.4656632613 | 31.1446323735 | 37 | 152650 | -91.49 | 5.73 | 64.41 | 0.19 | 1.63 | 973 |
| 2024-09-20 22:21:38.138 | MS1 | 121.4656626361 | 31.1446332593 | 189 | 152650 | -87.37 | 4.74 | 57.04 | 0.18 | 1.69 | 937 |
| 2024-09-20 22:21:39.639 | MS1 | 121.4656621373 | 31.1446370448 | 669 | 152650 | -92.86 | 6.47 | 66.64 | 0.06 | 1.86 | 1000 |
| 2024-09-20 22:21:40.263 | MS1 | 121.4656705084 | 31.1446225461 | 481 | 152650 | -89.83 | 4.34 | 44.81 | 0.07 | 2.99 | 1569 |
| 2024-09-20 22:21:41.712 | MS1 | 121.4656617903 | 31.1446230413 | 37 | 152650 | -89.92 | 7.03 | 96.40 | 0.07 | 2.11 | 1593 |
| 2024-09-20 22:21:42.685 | MS1 | 121.4656735338 | 31.1446253517 | 189 | 152650 | -90.49 | 2.59 | 85.73 | 0.17 | 2.86 | 1579 |

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
| 3210915 | 8 | 121.4655074089 | 31.1557356889 | 21 | 3 | 2 | 26.8 | FDD | 37 | n1 | 152650 | 30M | 4T4R | 14 | 152650 |
| 3222548 | 2 | 121.4749970009 | 31.1524500365 | 225 | 14 | 4 | 23.7 | TDD | 742 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3224737 | 13 | 121.4731543716 | 31.1511501589 | 219 | 7 | 10 | 22.0 | FDD | 189 | n1 | 152650 | 30M | 4T4R | 27 | 152650 |
| 3226602 | 6 | 121.4714331815 | 31.1444170611 | 310 | 0 | 4 | 11.9 | TDD | 511 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3227153 | 4 | 121.4752808146 | 31.1485026891 | 36 | 3 | 0 | 25.9 | TDD | 80 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3232126 | 3 | 121.4723089267 | 31.1544025580 | 214 | 4 | 10 | 9.1 | TDD | 809 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3234918 | 12 | 121.4747992352 | 31.1460378470 | 232 | 0 | 12 | 26.7 | FDD | 210 | n1 | 152650 | 30M | 4T4R | 11 | 152650 |
| 3245558 | 10 | 121.4700957114 | 31.1477151387 | 309 | 12 | 9 | 12.3 | FDD | 582 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |
| 3253334 | 11 | 121.4699102947 | 31.1477567063 | 140 | 11 | 11 | 8.9 | FDD | 870 | n1 | 152650 | 30M | 4T4R | 30 | 152650 |
| 3265278 | 7 | 121.4722378176 | 31.1454910167 | 262 | 7 | 2 | 5.9 | FDD | 481 | n1 | 152650 | 30M | 4T4R | 22 | 152650 |
| 3265892 | 1 | 121.4662929121 | 31.1547102542 | 29 | 6 | 2 | 13.5 | TDD | 67 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3266217 | 5 | 121.4694038977 | 31.1512110249 | 323 | 12 | 3 | 27.1 | TDD | 861 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3275326 | 9 | 121.4688962210 | 31.1539032259 | 102 | 0 | 12 | 15.0 | FDD | 669 | n1 | 152650 | 30M | 4T4R | 26 | 152650 |

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
| 2024-09-20 22:21:31.337 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.439 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.439 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.164 | NREventA2 | measId:1;ServCellPCI:229;Se... |
| 2024-09-20 22:21:35.284 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.528 | NREventA5 | measId:3;ServCellPCI:229;Se... |
| 2024-09-20 22:21:35.606 | NRHandoverAttempt | SourcePCI:229;SourceNR-ARFC... |
| 2024-09-20 22:21:35.654 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.667 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:35.794 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.794 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3265892 | 1 | 17.4252 | 19.1648 | -115.1596 | 14.3758 | 172.4256 | 0.0049 | 0.0048 |
| 2024_09_20 22:00 | 3222548 | 2 | 12.1243 | 14.0026 | -115.8550 | 14.7301 | 106.5335 | 0.0186 | 0.0096 |
| 2024_09_20 22:00 | 3232126 | 3 | 15.3516 | 15.3885 | -116.5058 | 11.1909 | 146.9471 | 0.0120 | 0.0137 |
| 2024_09_20 22:00 | 3227153 | 4 | 5.5254 | 17.5230 | -114.9718 | 5.6321 | 193.0316 | 0.0093 | 0.0190 |
| 2024_09_20 22:00 | 3266217 | 5 | 19.4093 | 13.7740 | -117.5833 | 13.6158 | 173.4982 | 0.0126 | 0.0151 |
| 2024_09_20 22:00 | 3226602 | 6 | 18.5388 | 7.1667 | -117.5283 | 12.7473 | 131.2769 | 0.0069 | 0.0182 |
| 2024_09_20 22:00 | 3265278 | 7 | 13.1142 | 15.7315 | -117.9448 | 4.7011 | 34.5739 | 0.0065 | 0.0093 |
| 2024_09_20 22:00 | 3210915 | 8 | 8.2410 | 9.1338 | -116.0432 | 4.9591 | 57.9468 | 0.0007 | 0.0055 |
| 2024_09_20 22:00 | 3275326 | 9 | 11.9801 | 11.0110 | -114.1734 | 4.5210 | 43.6476 | 0.0039 | 0.0161 |
| 2024_09_20 22:00 | 3245558 | 10 | 5.6055 | 5.1190 | -116.4334 | 3.8478 | 37.8283 | 0.0172 | 0.0121 |
| 2024_09_20 22:00 | 3253334 | 11 | 19.7663 | 17.8328 | -115.0766 | 3.7413 | 27.6720 | 0.0037 | 0.0170 |
| 2024_09_20 22:00 | 3234918 | 12 | 14.5119 | 7.6220 | -116.9890 | 4.0168 | 59.9256 | 0.0029 | 0.0160 |
| 2024_09_20 22:00 | 3224737 | 13 | 12.4894 | 19.4388 | -117.9902 | 3.3885 | 20.6735 | 0.0120 | 0.0079 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417068_7FF79A85 | 504990 | 861 | -97.4 | 504990 | 809 | -92.7 | 504990 | 80 | -97.7 | 504990 | 742 |
| MR_1774417068_EAB147E3 | 504990 | 861 | -96.3 | 504990 | 809 | -95.5 | 504990 | 80 | -94.4 | 504990 | 742 |
| MR_1774417068_8818AAAA | 504990 | 861 | -97.3 | 504990 | 809 | -92.9 | 504990 | 80 | -96.9 | 504990 | 742 |
| MR_1774417068_C131C66E | 504990 | 861 | -94.3 | 504990 | 809 | -95.3 | 504990 | 80 | -97.2 | 504990 | 742 |
| MR_1774417068_4F9D140E | 152650 | 189 | -89.1 | 152650 | 582 | -90.5 | 152650 | 870 | -97.7 | 152650 | 210 |
| MR_1774417068_D21887EC | 152650 | 189 | -88.1 | 152650 | 582 | -88.3 | 152650 | 870 | -98.0 | 152650 | 210 |
| MR_1774417068_759E8A2D | 152650 | 189 | -86.7 | 152650 | 582 | -90.9 | 152650 | 870 | -99.6 | 152650 | 210 |
| MR_1774417068_0827BD96 | 152650 | 189 | -87.8 | 152650 | 582 | -90.6 | 152650 | 870 | -99.1 | 152650 | 210 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1248: `ced309eb-7f0...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `ced309eb-7f0b-45ea-ab72-1963b3c74f02` |
| Tag | **single-answer** |
| 정답 | **C11** |
| C11 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1248] topology](images/train_1248.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3240825_3 and 3270105_1
- `C2`: Decrease transmission power for 3270105_1
- `C3`: Increase A3 Offset threshold for 3240825_3
- `C4`: Adjust the azimuth of 3240825_3 by 50 degrees
- `C5`: Increase transmission power for 3240825_3
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3240825_3
- `C7`: Decrease transmission power for 3240825_3
- `C8`: Lift the tilt angle  of 3270105_1 by 10 degrees
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3270105_1
- `C10`: Decrease A3 Offset threshold for 3240825_3
- `C11`: Check test server and transmission issues **← 정답**
- `C12`: Insufficient data; more data is needed for judgment.
- `C13`: Press down the tilt angle  of 3270105_1 by 10 degrees
- `C14`: Decrease A3 Offset threshold for 3270105_1
- `C15`: Increase A3 Offset threshold for 3270105_1
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3270105_1
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3240825_3
- `C18`: Lift the tilt angle of 3240825_3 by 6 degrees
- `C19`: Adjust the azimuth of 3270105_1 by 50 degrees
- `C20`: Add neighbor relationship between 3247499_2 and 3270105_1
- `C21`: Press down the tilt angle of 3240825_3 by 6 degrees
- `C22`: Increase transmission power for 3270105_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.514 | MS1 | 121.4656766491 | 31.1446205514 | 404 | 504990 | -89.05 | 14.64 | 441.34 | 0.10 | 2.58 | 1560 |
| 2024-09-20 22:21:32.326 | MS1 | 121.4656754754 | 31.1446214300 | 404 | 504990 | -86.81 | 12.43 | 428.90 | 0.16 | 2.97 | 1579 |
| 2024-09-20 22:21:33.921 | MS1 | 121.4656635720 | 31.1446361533 | 404 | 504990 | -86.87 | 14.39 | 464.41 | 0.18 | 2.70 | 1581 |
| 2024-09-20 22:21:34.512 | MS1 | 121.4656778339 | 31.1446331257 | 404 | 504990 | -87.59 | 12.36 | 80.27 | 0.02 | 2.05 | 387 |
| 2024-09-20 22:21:35.526 | MS1 | 121.4656583357 | 31.1446376264 | 404 | 504990 | -89.94 | 13.50 | 92.43 | 0.19 | 2.65 | 332 |
| 2024-09-20 22:21:36.687 | MS1 | 121.4656582215 | 31.1446283465 | 404 | 504990 | -86.17 | 15.79 | 74.76 | 0.17 | 2.08 | 448 |
| 2024-09-20 22:21:37.914 | MS1 | 121.4656747514 | 31.1446340281 | 404 | 504990 | -89.81 | 7.55 | 69.58 | 0.15 | 2.66 | 450 |
| 2024-09-20 22:21:38.230 | MS1 | 121.4656709514 | 31.1446335652 | 404 | 504990 | -92.97 | 10.67 | 78.74 | 0.07 | 2.72 | 421 |
| 2024-09-20 22:21:39.376 | MS1 | 121.4656584875 | 31.1446264921 | 404 | 504990 | -91.57 | 12.16 | 65.44 | 0.02 | 2.92 | 304 |
| 2024-09-20 22:21:40.102 | MS1 | 121.4656674112 | 31.1446335065 | 404 | 504990 | -92.08 | 12.25 | 438.48 | 0.07 | 2.42 | 1596 |
| 2024-09-20 22:21:41.409 | MS1 | 121.4656766378 | 31.1446232070 | 404 | 504990 | -90.80 | 12.62 | 454.17 | 0.17 | 2.28 | 1572 |
| 2024-09-20 22:21:42.491 | MS1 | 121.4656675682 | 31.1446377509 | 404 | 504990 | -92.22 | 11.60 | 561.74 | 0.05 | 2.12 | 1590 |

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
| 3215260 | 4 | 121.4646087198 | 31.1508510361 | 141 | 10 | 11 | 29.0 | TDD | 622 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3240825 | 3 | 121.4750948350 | 31.1472152078 | 33 | 4 | 7 | 34.3 | TDD | 404 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3247499 | 2 | 121.4664507351 | 31.1508699646 | 321 | 11 | 10 | 47.7 | TDD | 155 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3270105 | 1 | 121.4709307402 | 31.1485026142 | 86 | 10 | 0 | 49.3 | TDD | 298 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:31.138 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.156 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.303 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.303 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.007 | NREventA3 | measId:2;ServCellPCI:332;Se... |
| 2024-09-20 22:21:38.247 | NRHandoverAttempt | SourcePCI:332;SourceNR-ARFC... |
| 2024-09-20 22:21:38.293 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.306 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.448 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.448 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3270105 | 1 | 18.6251 | 6.1644 | -114.4230 | 12.3103 | 191.4334 | 0.0165 | 0.0057 |
| 2024_09_20 22:00 | 3247499 | 2 | 5.7687 | 10.1780 | -116.2284 | 17.1531 | 92.4915 | 0.0108 | 0.0041 |
| 2024_09_20 22:00 | 3240825 | 3 | 19.4162 | 19.3026 | -115.8719 | 10.8709 | 156.4854 | 0.0029 | 0.0004 |
| 2024_09_20 22:00 | 3215260 | 4 | 8.3007 | 13.6599 | -115.1182 | 11.3028 | 163.6518 | 0.0021 | 0.0083 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414495_2E3087D2 | 504990 | 404 | -89.1 | 504990 | 298 | -93.9 | 504990 | 155 | -103.8 | 504990 | 622 |
| MR_1774414495_6C02FACE | 504990 | 404 | -88.0 | 504990 | 298 | -91.1 | 504990 | 155 | -102.6 | 504990 | 622 |
| MR_1774414495_74714CE4 | 504990 | 404 | -87.4 | 504990 | 298 | -94.8 | 504990 | 155 | -103.2 | 504990 | 622 |
| MR_1774414495_4742C7DD | 504990 | 404 | -87.5 | 504990 | 298 | -91.3 | 504990 | 155 | -103.6 | 504990 | 622 |
| MR_1774414495_F68640C6 | 504990 | 404 | -89.1 | 504990 | 298 | -91.5 | 504990 | 155 | -101.0 | 504990 | 622 |
| MR_1774414495_9288B562 | 504990 | 404 | -89.1 | 504990 | 298 | -91.9 | 504990 | 155 | -101.9 | 504990 | 622 |
| MR_1774414495_785CA18A | 504990 | 404 | -87.3 | 504990 | 298 | -94.4 | 504990 | 155 | -102.2 | 504990 | 622 |
| MR_1774414495_567FBC37 | 504990 | 404 | -88.9 | 504990 | 298 | -92.7 | 504990 | 155 | -102.0 | 504990 | 622 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1249: `aa8811f0-b7f...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `aa8811f0-b7f8-4682-b142-4d953229e4b4` |
| Tag | **single-answer** |
| 정답 | **C12** |
| C12 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3222844_6 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1249] topology](images/train_1249.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3269218_5 by 1 degrees
- `C2`: Adjust the azimuth of 3222844_6 by 15 degrees
- `C3`: Increase transmission power for 3269218_5
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3222844_6
- `C5`: Press down the tilt angle of 3222844_6 by 5 degrees
- `C6`: Adjust the azimuth of 3269218_5 by 41 degrees
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3269218_5
- `C8`: Lift the tilt angle of 3222844_6 by 5 degrees
- `C9`: Decrease transmission power for 3222844_6
- `C10`: Increase A3 Offset threshold for 3222844_6
- `C11`: Add neighbor relationship between 3255770_13 and 3269218_5
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3222844_6 **← 정답**
- `C13`: Decrease A3 Offset threshold for 3269218_5
- `C14`: Increase A3 Offset threshold for 3269218_5
- `C15`: Add neighbor relationship between 3222844_6 and 3269218_5
- `C16`: Insufficient data; more data is needed for judgment.
- `C17`: Decrease transmission power for 3269218_5
- `C18`: Check test server and transmission issues
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3269218_5
- `C20`: Lift the tilt angle  of 3269218_5 by 1 degrees
- `C21`: Decrease A3 Offset threshold for 3222844_6
- `C22`: Increase transmission power for 3222844_6

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.254 | MS1 | 121.4656675364 | 31.1446322194 | 799 | 504990 | -93.86 | 10.83 | 607.30 | 0.01 | 2.88 | 1562 |
| 2024-09-20 22:21:32.566 | MS1 | 121.4656624192 | 31.1446193804 | 306 | 504990 | -94.27 | 14.70 | 339.35 | 0.14 | 2.27 | 1570 |
| 2024-09-20 22:21:33.387 | MS1 | 121.4656599770 | 31.1446290913 | 325 | 504990 | -95.77 | 13.36 | 340.29 | 0.11 | 2.02 | 1578 |
| 2024-09-20 22:21:34.243 | MS1 | 121.4656621420 | 31.1446228778 | 821 | 152650 | -88.59 | 3.63 | 85.73 | 0.02 | 1.57 | 956 |
| 2024-09-20 22:21:35.845 | MS1 | 121.4656735139 | 31.1446350888 | 790 | 152650 | -95.39 | 6.61 | 53.74 | 0.04 | 1.89 | 919 |
| 2024-09-20 22:21:36.386 | MS1 | 121.4656748375 | 31.1446352257 | 92 | 152650 | -95.90 | 2.11 | 77.75 | 0.18 | 1.97 | 982 |
| 2024-09-20 22:21:37.835 | MS1 | 121.4656699491 | 31.1446181257 | 88 | 152650 | -91.74 | 5.24 | 74.40 | 0.05 | 1.75 | 958 |
| 2024-09-20 22:21:38.107 | MS1 | 121.4656768144 | 31.1446277253 | 821 | 152650 | -94.20 | 3.23 | 57.34 | 0.03 | 1.70 | 930 |
| 2024-09-20 22:21:39.609 | MS1 | 121.4656763199 | 31.1446361131 | 790 | 152650 | -90.96 | 6.05 | 74.15 | 0.03 | 1.82 | 900 |
| 2024-09-20 22:21:40.792 | MS1 | 121.4656722190 | 31.1446277416 | 92 | 152650 | -95.76 | 5.01 | 72.29 | 0.13 | 2.65 | 1600 |
| 2024-09-20 22:21:41.203 | MS1 | 121.4656582295 | 31.1446217823 | 88 | 152650 | -92.00 | 2.91 | 54.45 | 0.13 | 2.49 | 1585 |
| 2024-09-20 22:21:42.105 | MS1 | 121.4656614154 | 31.1446379205 | 821 | 152650 | -89.49 | 6.34 | 83.72 | 0.14 | 2.29 | 1579 |

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
| 3213241 | 4 | 121.4698654009 | 31.1553789030 | 70 | 6 | 2 | 7.0 | TDD | 248 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3215073 | 7 | 121.4656274061 | 31.1548663178 | 167 | 1 | 5 | 21.7 | FDD | 237 | n1 | 152650 | 30M | 4T4R | 24 | 152650 |
| 3215981 | 3 | 121.4721717442 | 31.1461613290 | 81 | 9 | 9 | 19.4 | TDD | 309 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3216561 | 10 | 121.4742487134 | 31.1539050690 | 14 | 1 | 11 | 6.0 | FDD | 790 | n1 | 152650 | 30M | 4T4R | 27 | 152650 |
| 3218817 | 2 | 121.4660583856 | 31.1520308014 | 77 | 13 | 11 | 13.0 | TDD | 306 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3220195 | 9 | 121.4671713881 | 31.1500707724 | 256 | 2 | 7 | 20.5 | FDD | 821 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |
| 3222844 | 6 | 121.4741980144 | 31.1537241042 | 234 | 4 | 12 | 27.3 | TDD | 799 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3229381 | 11 | 121.4672006223 | 31.1524584933 | 22 | 5 | 8 | 28.8 | FDD | 88 | n1 | 152650 | 30M | 4T4R | 21 | 152650 |
| 3231927 | 8 | 121.4694410440 | 31.1527122292 | 295 | 5 | 0 | 15.3 | FDD | 242 | n1 | 152650 | 30M | 4T4R | 12 | 152650 |
| 3240810 | 1 | 121.4673521363 | 31.1557493886 | 78 | 7 | 8 | 12.9 | TDD | 325 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3255770 | 13 | 121.4675069293 | 31.1497858769 | 204 | 5 | 8 | 2.8 | FDD | 92 | n1 | 152650 | 30M | 4T4R | 27 | 152650 |
| 3263180 | 12 | 121.4670906065 | 31.1449938608 | 155 | 9 | 1 | 20.3 | FDD | 953 | n1 | 152650 | 30M | 4T4R | 25 | 152650 |
| 3269218 | 5 | 121.4699558355 | 31.1469505822 | 279 | 0 | 6 | 7.3 | TDD | 666 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |

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
| 2024-09-20 22:21:30.960 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.984 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.128 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.128 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.819 | NREventA2 | measId:1;ServCellPCI:739;Se... |
| 2024-09-20 22:21:34.965 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.189 | NREventA5 | measId:3;ServCellPCI:739;Se... |
| 2024-09-20 22:21:35.260 | NRHandoverAttempt | SourcePCI:739;SourceNR-ARFC... |
| 2024-09-20 22:21:35.303 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.316 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:35.429 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.429 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3240810 | 1 | 18.0303 | 9.6356 | -117.1892 | 16.9815 | 191.3989 | 0.0048 | 0.0185 |
| 2024_09_20 22:00 | 3218817 | 2 | 7.8818 | 9.2332 | -116.9853 | 17.6370 | 164.8361 | 0.0148 | 0.0057 |
| 2024_09_20 22:00 | 3215981 | 3 | 12.4780 | 19.3049 | -116.8136 | 12.2463 | 111.0214 | 0.0068 | 0.0198 |
| 2024_09_20 22:00 | 3213241 | 4 | 15.6466 | 10.1265 | -116.0310 | 6.2315 | 133.7734 | 0.0104 | 0.0049 |
| 2024_09_20 22:00 | 3269218 | 5 | 6.6053 | 13.9297 | -114.9564 | 11.5334 | 196.1747 | 0.0114 | 0.0165 |
| 2024_09_20 22:00 | 3222844 | 6 | 6.2347 | 18.5040 | -116.6681 | 5.5085 | 108.0776 | 0.0094 | 0.0099 |
| 2024_09_20 22:00 | 3215073 | 7 | 11.1869 | 15.5662 | -116.2718 | 3.7526 | 31.2512 | 0.0184 | 0.0055 |
| 2024_09_20 22:00 | 3231927 | 8 | 15.1401 | 13.7967 | -114.7224 | 4.8937 | 48.3869 | 0.0092 | 0.0107 |
| 2024_09_20 22:00 | 3220195 | 9 | 18.5994 | 14.2187 | -114.5318 | 3.6986 | 34.3471 | 0.0070 | 0.0050 |
| 2024_09_20 22:00 | 3216561 | 10 | 17.8660 | 12.9676 | -115.2009 | 4.5991 | 25.0090 | 0.0083 | 0.0169 |
| 2024_09_20 22:00 | 3229381 | 11 | 10.0638 | 14.9455 | -116.3841 | 3.5255 | 33.6538 | 0.0047 | 0.0182 |
| 2024_09_20 22:00 | 3263180 | 12 | 13.6790 | 6.3130 | -117.3455 | 3.0362 | 48.9947 | 0.0010 | 0.0017 |
| 2024_09_20 22:00 | 3255770 | 13 | 13.5779 | 14.0938 | -114.2224 | 4.9700 | 30.4124 | 0.0184 | 0.0013 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416818_E455D23E | 152650 | 821 | -88.6 | 152650 | 242 | -92.6 | 152650 | 237 | -98.9 | 152650 | 953 |
| MR_1774416818_41DF813C | 152650 | 821 | -90.2 | 152650 | 242 | -91.7 | 152650 | 237 | -101.2 | 152650 | 953 |
| MR_1774416818_7AE79E35 | 152650 | 821 | -90.3 | 152650 | 242 | -89.7 | 152650 | 237 | -99.7 | 152650 | 953 |
| MR_1774416818_7051135D | 152650 | 821 | -88.1 | 152650 | 242 | -91.2 | 152650 | 237 | -99.0 | 152650 | 953 |
| MR_1774416818_830FC107 | 504990 | 325 | -94.2 | 504990 | 666 | -89.3 | 504990 | 309 | -103.0 | 504990 | 248 |

> *... 2개 열 생략 (전체 14열)*

---
