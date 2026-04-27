# Track A 문제 분석 — train[1430]~train[1439]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[1430] ~ train[1439] (10개)

## 목차

1. [문제 1430: `e369203f-a40...`](#1430) — single-answer, 정답: C22
2. [문제 1431: `75f92daf-999...`](#1431) — multiple-answer, 정답: C9|C13|C18|C22
3. [문제 1432: `0aed7aa1-073...`](#1432) — multiple-answer, 정답: C3|C9|C13|C18
4. [문제 1433: `02675c12-d31...`](#1433) — single-answer, 정답: C4
5. [문제 1434: `50dc8d47-143...`](#1434) — single-answer, 정답: C7
6. [문제 1435: `643e7382-296...`](#1435) — multiple-answer, 정답: C2|C6|C20|C21
7. [문제 1436: `381f29f6-0e8...`](#1436) — single-answer, 정답: C1
8. [문제 1437: `716fdee2-00e...`](#1437) — multiple-answer, 정답: C3|C7|C11|C15
9. [문제 1438: `d9d2cbda-293...`](#1438) — single-answer, 정답: C4
10. [문제 1439: `e72857c2-04b...`](#1439) — single-answer, 정답: C1

---

### 문제 1430: `e369203f-a40...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `e369203f-a407-45d8-a0e3-9e24b2a81a6b` |
| Tag | **single-answer** |
| 정답 | **C22** |
| C22 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3264757_3 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1430] topology](images/train_1430.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3248150_5
- `C2`: Press down the tilt angle  of 3248150_5 by 2 degrees
- `C3`: Increase transmission power for 3264757_3
- `C4`: Decrease transmission power for 3248150_5
- `C5`: Lift the tilt angle of 3264757_3 by 3 degrees
- `C6`: Lift the tilt angle  of 3248150_5 by 2 degrees
- `C7`: Insufficient data; more data is needed for judgment.
- `C8`: Check test server and transmission issues
- `C9`: Increase transmission power for 3248150_5
- `C10`: Adjust the azimuth of 3264757_3 by 24 degrees
- `C11`: Decrease A3 Offset threshold for 3248150_5
- `C12`: Adjust the azimuth of 3248150_5 by 16 degrees
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3248150_5
- `C14`: Increase A3 Offset threshold for 3248150_5
- `C15`: Add neighbor relationship between 3264757_3 and 3248150_5
- `C16`: Decrease transmission power for 3264757_3
- `C17`: Increase A3 Offset threshold for 3264757_3
- `C18`: Press down the tilt angle of 3264757_3 by 3 degrees
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3264757_3
- `C20`: Add neighbor relationship between 3221519_13 and 3248150_5
- `C21`: Decrease A3 Offset threshold for 3264757_3
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3264757_3 **← 정답**

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.430 | MS1 | 121.4656624922 | 31.1446366621 | 330 | 504990 | -93.53 | 11.64 | 486.38 | 0.08 | 2.80 | 1572 |
| 2024-09-20 22:21:32.341 | MS1 | 121.4656584536 | 31.1446274585 | 813 | 504990 | -94.30 | 10.17 | 438.75 | 0.19 | 2.89 | 1586 |
| 2024-09-20 22:21:33.440 | MS1 | 121.4656637352 | 31.1446220655 | 416 | 504990 | -95.99 | 9.09 | 589.81 | 0.13 | 2.26 | 1597 |
| 2024-09-20 22:21:34.474 | MS1 | 121.4656730024 | 31.1446313951 | 179 | 152650 | -95.37 | 5.83 | 84.94 | 0.12 | 1.73 | 931 |
| 2024-09-20 22:21:35.385 | MS1 | 121.4656703738 | 31.1446308840 | 937 | 152650 | -93.35 | 2.81 | 66.37 | 0.04 | 1.75 | 919 |
| 2024-09-20 22:21:36.126 | MS1 | 121.4656661164 | 31.1446241425 | 986 | 152650 | -87.76 | 3.64 | 72.64 | 0.20 | 1.97 | 942 |
| 2024-09-20 22:21:37.126 | MS1 | 121.4656584940 | 31.1446356765 | 971 | 152650 | -95.44 | 5.03 | 83.03 | 0.01 | 1.84 | 913 |
| 2024-09-20 22:21:38.384 | MS1 | 121.4656601560 | 31.1446379969 | 179 | 152650 | -93.21 | 7.05 | 84.02 | 0.20 | 1.68 | 950 |
| 2024-09-20 22:21:39.794 | MS1 | 121.4656661088 | 31.1446299752 | 937 | 152650 | -90.95 | 3.89 | 83.12 | 0.19 | 1.53 | 946 |
| 2024-09-20 22:21:40.749 | MS1 | 121.4656735103 | 31.1446364694 | 986 | 152650 | -89.89 | 2.10 | 54.35 | 0.12 | 2.89 | 1570 |
| 2024-09-20 22:21:41.842 | MS1 | 121.4656635126 | 31.1446293953 | 971 | 152650 | -94.53 | 2.08 | 95.97 | 0.15 | 2.47 | 1562 |
| 2024-09-20 22:21:42.237 | MS1 | 121.4656694660 | 31.1446312869 | 179 | 152650 | -88.24 | 3.77 | 75.99 | 0.10 | 2.79 | 1576 |

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
| 3218018 | 4 | 121.4738361923 | 31.1558858016 | 10 | 2 | 4 | 28.3 | TDD | 813 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3221519 | 13 | 121.4685915648 | 31.1558366862 | 57 | 5 | 3 | 23.4 | FDD | 986 | n1 | 152650 | 30M | 4T4R | 24 | 152650 |
| 3229592 | 2 | 121.4681944904 | 31.1531412414 | 173 | 0 | 9 | 15.5 | TDD | 520 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3241883 | 9 | 121.4713377621 | 31.1525418267 | 150 | 7 | 5 | 0.2 | FDD | 971 | n1 | 152650 | 30M | 4T4R | 19 | 152650 |
| 3248150 | 5 | 121.4657658878 | 31.1485194833 | 197 | 2 | 4 | 0.7 | TDD | 436 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3252050 | 8 | 121.4717103912 | 31.1537243392 | 356 | 12 | 0 | 22.0 | FDD | 969 | n1 | 152650 | 30M | 4T4R | 12 | 152650 |
| 3256119 | 10 | 121.4671426410 | 31.1490964311 | 280 | 2 | 3 | 2.3 | FDD | 179 | n1 | 152650 | 30M | 4T4R | 28 | 152650 |
| 3264757 | 3 | 121.4748399843 | 31.1543408227 | 243 | 3 | 5 | 8.5 | TDD | 330 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3265555 | 6 | 121.4730954440 | 31.1484785996 | 312 | 5 | 9 | 20.5 | TDD | 855 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3267247 | 12 | 121.4734462262 | 31.1523125791 | 323 | 0 | 10 | 2.5 | FDD | 729 | n1 | 152650 | 30M | 4T4R | 24 | 152650 |
| 3270617 | 11 | 121.4677843480 | 31.1473926400 | 233 | 14 | 12 | 17.9 | FDD | 887 | n1 | 152650 | 30M | 4T4R | 18 | 152650 |
| 3272893 | 1 | 121.4759676452 | 31.1480015804 | 337 | 7 | 2 | 18.2 | TDD | 416 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3275326 | 7 | 121.4746839323 | 31.1519575049 | 155 | 12 | 1 | 0.9 | FDD | 937 | n1 | 152650 | 30M | 4T4R | 26 | 152650 |

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
| 2024-09-20 22:21:31.463 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.478 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.597 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.597 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.265 | NREventA2 | measId:1;ServCellPCI:444;Se... |
| 2024-09-20 22:21:35.388 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.685 | NREventA5 | measId:3;ServCellPCI:444;Se... |
| 2024-09-20 22:21:35.737 | NRHandoverAttempt | SourcePCI:444;SourceNR-ARFC... |
| 2024-09-20 22:21:35.767 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.782 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:35.919 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.919 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3272893 | 1 | 8.4898 | 9.1468 | -114.1759 | 11.7111 | 155.6566 | 0.0069 | 0.0151 |
| 2024_09_20 22:00 | 3229592 | 2 | 15.6427 | 10.2664 | -117.8927 | 11.0743 | 98.4930 | 0.0168 | 0.0091 |
| 2024_09_20 22:00 | 3264757 | 3 | 11.4662 | 12.6103 | -114.0924 | 10.1208 | 162.3322 | 0.0094 | 0.0092 |
| 2024_09_20 22:00 | 3218018 | 4 | 19.4600 | 7.7003 | -115.6653 | 6.0068 | 112.3082 | 0.0162 | 0.0178 |
| 2024_09_20 22:00 | 3248150 | 5 | 15.9294 | 18.0120 | -114.7671 | 18.8553 | 179.2676 | 0.0027 | 0.0104 |
| 2024_09_20 22:00 | 3265555 | 6 | 5.6598 | 18.8122 | -117.8815 | 10.4378 | 81.0679 | 0.0141 | 0.0173 |
| 2024_09_20 22:00 | 3275326 | 7 | 11.4436 | 14.6883 | -114.0505 | 3.4555 | 43.7888 | 0.0046 | 0.0100 |
| 2024_09_20 22:00 | 3252050 | 8 | 19.3845 | 17.9078 | -117.5902 | 4.4999 | 27.3443 | 0.0078 | 0.0191 |
| 2024_09_20 22:00 | 3241883 | 9 | 17.5509 | 8.2262 | -115.8052 | 4.4870 | 53.6973 | 0.0129 | 0.0153 |
| 2024_09_20 22:00 | 3256119 | 10 | 15.1655 | 7.1575 | -117.0396 | 3.2838 | 58.5022 | 0.0149 | 0.0096 |
| 2024_09_20 22:00 | 3270617 | 11 | 18.0928 | 13.5034 | -115.9920 | 3.9822 | 58.2691 | 0.0032 | 0.0085 |
| 2024_09_20 22:00 | 3267247 | 12 | 14.5163 | 15.9449 | -114.2253 | 3.1078 | 37.8497 | 0.0141 | 0.0014 |
| 2024_09_20 22:00 | 3221519 | 13 | 6.8039 | 6.7447 | -117.9985 | 3.3796 | 37.2026 | 0.0174 | 0.0005 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415870_C645AACA | 504990 | 416 | -96.0 | 504990 | 436 | -93.6 | 504990 | 855 | -98.4 | 504990 | 520 |
| MR_1774415870_B0F28B4B | 504990 | 416 | -94.4 | 504990 | 436 | -95.0 | 504990 | 855 | -99.4 | 504990 | 520 |
| MR_1774415870_111A25CC | 504990 | 416 | -96.2 | 504990 | 436 | -92.9 | 504990 | 855 | -96.6 | 504990 | 520 |
| MR_1774415870_9E73867A | 504990 | 416 | -96.5 | 504990 | 436 | -92.2 | 504990 | 855 | -95.6 | 504990 | 520 |
| MR_1774415870_E7F2FDDE | 504990 | 416 | -96.5 | 504990 | 436 | -95.4 | 504990 | 855 | -98.0 | 504990 | 520 |
| MR_1774415870_6C6D7734 | 152650 | 179 | -94.9 | 152650 | 887 | -99.1 | 152650 | 969 | -101.7 | 152650 | 729 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1431: `75f92daf-999...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `75f92daf-9997-4299-8bd8-2ea604c6c602` |
| Tag | **multiple-answer** |
| 정답 | **C9|C13|C18|C22** |
| C9 의미 | Increase A3 Offset threshold for 3225423_5 |
| C13 의미 | Press down the tilt angle  of 3225423_5 by 4 degrees |
| C18 의미 | Decrease transmission power for 3225423_5 |
| C22 의미 | Increase A3 Offset threshold for 3247029_3 |
| 패턴 분류 | **P2 Ping-pong** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1431] topology](images/train_1431.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 5 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 5개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3247029_3 by 3 degrees
- `C2`: Increase transmission power for 3247029_3
- `C3`: Decrease transmission power for 3247029_3
- `C4`: Add neighbor relationship between 3273530_2 and 3225423_5
- `C5`: Adjust the azimuth of 3225423_5 by 40 degrees
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3247029_3
- `C7`: Add neighbor relationship between 3247029_3 and 3225423_5
- `C8`: Check test server and transmission issues
- `C9`: Increase A3 Offset threshold for 3225423_5 **← 정답**
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3225423_5
- `C11`: Adjust the azimuth of 3247029_3 by 2 degrees
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3225423_5
- `C13`: Press down the tilt angle  of 3225423_5 by 4 degrees **← 정답**
- `C14`: Decrease A3 Offset threshold for 3247029_3
- `C15`: Increase transmission power for 3225423_5
- `C16`: Lift the tilt angle  of 3225423_5 by 4 degrees
- `C17`: Insufficient data; more data is needed for judgment.
- `C18`: Decrease transmission power for 3225423_5 **← 정답**
- `C19`: Press down the tilt angle of 3247029_3 by 3 degrees
- `C20`: Decrease A3 Offset threshold for 3225423_5
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3247029_3
- `C22`: Increase A3 Offset threshold for 3247029_3 **← 정답**

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.897 | MS1 | 121.4656776937 | 31.1446276799 | 625 | 504990 | -78.07 | 14.67 | 545.43 | 0.10 | 2.46 | 1575 |
| 2024-09-20 22:21:32.703 | MS1 | 121.4656671063 | 31.1446322372 | 625 | 504990 | -84.49 | 14.22 | 402.76 | 0.16 | 2.96 | 1575 |
| 2024-09-20 22:21:33.878 | MS1 | 121.4656587702 | 31.1446265894 | 625 | 504990 | -78.43 | 14.05 | 462.42 | 0.12 | 2.90 | 1587 |
| 2024-09-20 22:21:34.942 | MS1 | 121.4656713411 | 31.1446320279 | 387 | 504990 | -84.27 | 2.16 | 52.99 | 0.09 | 1.46 | 1570 |
| 2024-09-20 22:21:35.953 | MS1 | 121.4656700111 | 31.1446359535 | 387 | 504990 | -87.76 | 4.34 | 59.81 | 0.19 | 1.29 | 1570 |
| 2024-09-20 22:21:36.577 | MS1 | 121.4656612033 | 31.1446321984 | 625 | 504990 | -81.70 | 2.09 | 59.71 | 0.17 | 1.10 | 1581 |
| 2024-09-20 22:21:37.536 | MS1 | 121.4656711593 | 31.1446372827 | 625 | 504990 | -82.47 | 2.63 | 46.67 | 0.18 | 1.33 | 1576 |
| 2024-09-20 22:21:38.329 | MS1 | 121.4656645493 | 31.1446285518 | 387 | 504990 | -89.71 | 3.70 | 62.91 | 0.17 | 1.22 | 1589 |
| 2024-09-20 22:21:39.745 | MS1 | 121.4656666601 | 31.1446324223 | 387 | 504990 | -88.82 | 3.83 | 58.73 | 0.04 | 1.26 | 1569 |
| 2024-09-20 22:21:40.921 | MS1 | 121.4656653087 | 31.1446357483 | 387 | 504990 | -83.55 | 14.86 | 499.48 | 0.09 | 2.84 | 1596 |
| 2024-09-20 22:21:41.997 | MS1 | 121.4656774057 | 31.1446209150 | 387 | 504990 | -82.84 | 12.63 | 586.04 | 0.17 | 2.16 | 1589 |
| 2024-09-20 22:21:42.319 | MS1 | 121.4656664268 | 31.1446258955 | 387 | 504990 | -83.69 | 13.54 | 316.82 | 0.02 | 2.10 | 1563 |

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
| 3217448 | 1 | 121.4715943785 | 31.1479294435 | 264 | 10 | 3 | 44.5 | TDD | 387 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3225423 | 5 | 121.4727782408 | 31.1454974405 | 222 | 0 | 3 | 42.5 | TDD | 275 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3233622 | 4 | 121.4677131700 | 31.1555701376 | 17 | 10 | 6 | 38.5 | TDD | 786 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3247029 | 3 | 121.4716675191 | 31.1475902173 | 242 | 0 | 10 | 38.9 | TDD | 625 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3273530 | 2 | 121.4716551050 | 31.1470434927 | 50 | 11 | 6 | 19.5 | TDD | 143 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |

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
| 2024-09-20 22:21:30.845 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.866 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:30.997 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.997 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:33.649 | NREventA3 | measId:2;ServCellPCI:361;Se... |
| 2024-09-20 22:21:33.889 | NRHandoverAttempt | SourcePCI:361;SourceNR-ARFC... |
| 2024-09-20 22:21:33.930 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:33.944 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:34.074 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:34.074 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.649 | NREventA3 | measId:2;ServCellPCI:694;Se... |
| 2024-09-20 22:21:35.889 | NRHandoverAttempt | SourcePCI:694;SourceNR-ARFC... |
| 2024-09-20 22:21:35.933 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.943 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:36.075 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.075 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.649 | NREventA3 | measId:2;ServCellPCI:361;Se... |
| 2024-09-20 22:21:37.889 | NRHandoverAttempt | SourcePCI:361;SourceNR-ARFC... |
| 2024-09-20 22:21:37.925 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.937 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.040 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.040 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3217448 | 1 | 13.2484 | 16.6268 | -115.5940 | 14.8640 | 195.8867 | 0.0109 | 0.0123 |
| 2024_09_20 22:00 | 3273530 | 2 | 7.1961 | 9.9203 | -116.2114 | 12.9801 | 132.8221 | 0.0016 | 0.0140 |
| 2024_09_20 22:00 | 3247029 | 3 | 10.3382 | 7.5404 | -117.9540 | 11.2187 | 155.3271 | 0.0041 | 0.0068 |
| 2024_09_20 22:00 | 3233622 | 4 | 19.1615 | 16.3334 | -114.4088 | 6.0147 | 131.4954 | 0.0169 | 0.0038 |
| 2024_09_20 22:00 | 3225423 | 5 | 10.8162 | 6.8916 | -117.3761 | 18.7894 | 138.0270 | 0.0058 | 0.0152 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413331_4762D9DC | 504990 | 387 | -82.8 | 504990 | 625 | -83.3 | 504990 | 275 | -83.8 | 504990 | 143 |
| MR_1774413331_4B05C26B | 504990 | 387 | -85.5 | 504990 | 625 | -83.6 | 504990 | 275 | -87.7 | 504990 | 143 |
| MR_1774413331_45D13A8A | 504990 | 387 | -85.0 | 504990 | 625 | -81.0 | 504990 | 275 | -85.9 | 504990 | 143 |
| MR_1774413331_E0FF5674 | 504990 | 387 | -85.7 | 504990 | 625 | -84.2 | 504990 | 275 | -84.9 | 504990 | 143 |
| MR_1774413331_3C9A305A | 504990 | 625 | -83.1 | 504990 | 387 | -83.1 | 504990 | 275 | -84.5 | 504990 | 143 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1432: `0aed7aa1-073...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `0aed7aa1-073c-4850-9415-2ca739039de3` |
| Tag | **multiple-answer** |
| 정답 | **C3|C9|C13|C18** |
| C3 의미 | Increase A3 Offset threshold for 3212292_2 |
| C9 의미 | Decrease transmission power for 3212292_2 |
| C13 의미 | Press down the tilt angle  of 3212292_2 by 4 degrees |
| C18 의미 | Increase A3 Offset threshold for 3237793_1 |
| 패턴 분류 | **P2 Ping-pong** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1432] topology](images/train_1432.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 5 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 5개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment.
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3237793_1
- `C3`: Increase A3 Offset threshold for 3212292_2 **← 정답**
- `C4`: Adjust the azimuth of 3212292_2 by 24 degrees
- `C5`: Decrease transmission power for 3237793_1
- `C6`: Lift the tilt angle  of 3212292_2 by 4 degrees
- `C7`: Add neighbor relationship between 3237793_1 and 3212292_2
- `C8`: Increase transmission power for 3237793_1
- `C9`: Decrease transmission power for 3212292_2 **← 정답**
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3212292_2
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3212292_2
- `C12`: Decrease A3 Offset threshold for 3212292_2
- `C13`: Press down the tilt angle  of 3212292_2 by 4 degrees **← 정답**
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3237793_1
- `C15`: Decrease A3 Offset threshold for 3237793_1
- `C16`: Lift the tilt angle of 3237793_1 by 3 degrees
- `C17`: Increase transmission power for 3212292_2
- `C18`: Increase A3 Offset threshold for 3237793_1 **← 정답**
- `C19`: Add neighbor relationship between 3251304_3 and 3212292_2
- `C20`: Check test server and transmission issues
- `C21`: Press down the tilt angle of 3237793_1 by 3 degrees
- `C22`: Adjust the azimuth of 3237793_1 by 15 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.126 | MS1 | 121.4656692764 | 31.1446191506 | 932 | 504990 | -78.90 | 15.71 | 464.48 | 0.04 | 2.31 | 1576 |
| 2024-09-20 22:21:32.608 | MS1 | 121.4656712451 | 31.1446202961 | 932 | 504990 | -78.87 | 13.91 | 577.40 | 0.11 | 2.24 | 1568 |
| 2024-09-20 22:21:33.734 | MS1 | 121.4656736848 | 31.1446270750 | 932 | 504990 | -84.61 | 17.48 | 492.06 | 0.01 | 2.62 | 1571 |
| 2024-09-20 22:21:34.262 | MS1 | 121.4656710750 | 31.1446264905 | 24 | 504990 | -87.49 | 1.08 | 43.51 | 0.01 | 1.01 | 1577 |
| 2024-09-20 22:21:35.451 | MS1 | 121.4656773923 | 31.1446204472 | 24 | 504990 | -87.73 | 2.99 | 34.07 | 0.16 | 1.02 | 1595 |
| 2024-09-20 22:21:36.345 | MS1 | 121.4656663572 | 31.1446335907 | 932 | 504990 | -89.40 | 3.74 | 55.30 | 0.03 | 1.23 | 1571 |
| 2024-09-20 22:21:37.524 | MS1 | 121.4656717008 | 31.1446379165 | 932 | 504990 | -85.00 | 4.37 | 52.24 | 0.13 | 1.14 | 1589 |
| 2024-09-20 22:21:38.943 | MS1 | 121.4656765593 | 31.1446219565 | 24 | 504990 | -85.61 | 1.28 | 63.53 | 0.18 | 1.03 | 1590 |
| 2024-09-20 22:21:39.498 | MS1 | 121.4656688433 | 31.1446204606 | 24 | 504990 | -89.85 | 2.66 | 32.23 | 0.07 | 1.17 | 1566 |
| 2024-09-20 22:21:40.239 | MS1 | 121.4656733288 | 31.1446254451 | 24 | 504990 | -78.89 | 16.47 | 321.13 | 0.01 | 2.36 | 1594 |
| 2024-09-20 22:21:41.257 | MS1 | 121.4656668260 | 31.1446353346 | 24 | 504990 | -79.85 | 17.11 | 466.33 | 0.14 | 2.94 | 1572 |
| 2024-09-20 22:21:42.232 | MS1 | 121.4656587145 | 31.1446188131 | 24 | 504990 | -84.42 | 15.80 | 429.07 | 0.04 | 2.70 | 1593 |

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
| 3212292 | 2 | 121.4694946658 | 31.1457314326 | 227 | 1 | 3 | 18.4 | TDD | 75 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3230655 | 4 | 121.4754992534 | 31.1485739942 | 258 | 10 | 4 | 33.5 | TDD | 375 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3230740 | 5 | 121.4654619455 | 31.1490495188 | 49 | 15 | 11 | 28.3 | TDD | 24 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3237793 | 1 | 121.4744144678 | 31.1501722101 | 218 | 2 | 5 | 25.8 | TDD | 932 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3251304 | 3 | 121.4722511320 | 31.1449839936 | 244 | 14 | 5 | 40.7 | TDD | 942 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |

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
| 2024-09-20 22:21:31.231 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.254 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.390 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.390 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.078 | NREventA3 | measId:2;ServCellPCI:170;Se... |
| 2024-09-20 22:21:34.318 | NRHandoverAttempt | SourcePCI:170;SourceNR-ARFC... |
| 2024-09-20 22:21:34.359 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:34.369 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:34.481 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:34.481 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:36.078 | NREventA3 | measId:2;ServCellPCI:576;Se... |
| 2024-09-20 22:21:36.318 | NRHandoverAttempt | SourcePCI:576;SourceNR-ARFC... |
| 2024-09-20 22:21:36.357 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:36.372 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:36.507 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.507 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.078 | NREventA3 | measId:2;ServCellPCI:170;Se... |
| 2024-09-20 22:21:38.318 | NRHandoverAttempt | SourcePCI:170;SourceNR-ARFC... |
| 2024-09-20 22:21:38.365 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.378 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.497 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.497 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3237793 | 1 | 13.3067 | 8.6614 | -115.5369 | 12.0444 | 101.1199 | 0.0060 | 0.0012 |
| 2024_09_20 22:00 | 3212292 | 2 | 18.4423 | 5.3361 | -114.8861 | 13.6518 | 174.5257 | 0.0124 | 0.0108 |
| 2024_09_20 22:00 | 3251304 | 3 | 8.5684 | 12.7677 | -114.8400 | 15.8886 | 87.1447 | 0.0198 | 0.0039 |
| 2024_09_20 22:00 | 3230655 | 4 | 17.6276 | 17.5707 | -114.5885 | 9.6592 | 119.1847 | 0.0117 | 0.0011 |
| 2024_09_20 22:00 | 3230740 | 5 | 12.6052 | 13.7408 | -115.4240 | 13.4228 | 133.4829 | 0.0021 | 0.0044 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414120_EEDD2A44 | 504990 | 24 | -89.1 | 504990 | 932 | -87.8 | 504990 | 75 | -86.8 | 504990 | 942 |
| MR_1774414120_A353F232 | 504990 | 24 | -88.7 | 504990 | 932 | -87.8 | 504990 | 75 | -89.8 | 504990 | 942 |
| MR_1774414120_CF356881 | 504990 | 24 | -87.2 | 504990 | 932 | -88.5 | 504990 | 75 | -87.9 | 504990 | 942 |
| MR_1774414120_20BD8392 | 504990 | 932 | -89.0 | 504990 | 24 | -86.5 | 504990 | 75 | -87.4 | 504990 | 942 |
| MR_1774414120_71196636 | 504990 | 932 | -87.4 | 504990 | 24 | -89.8 | 504990 | 75 | -88.7 | 504990 | 942 |
| MR_1774414120_C27905CE | 504990 | 932 | -86.9 | 504990 | 24 | -89.7 | 504990 | 75 | -89.0 | 504990 | 942 |
| MR_1774414120_F8EDCBB3 | 504990 | 24 | -85.7 | 504990 | 932 | -88.6 | 504990 | 75 | -86.6 | 504990 | 942 |
| MR_1774414120_33016EA4 | 504990 | 24 | -88.6 | 504990 | 932 | -86.5 | 504990 | 75 | -87.0 | 504990 | 942 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1433: `02675c12-d31...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `02675c12-d315-4fb3-a1c7-5706ba523d5d` |
| Tag | **single-answer** |
| 정답 | **C4** |
| C4 의미 | Lift the tilt angle  of 3264875_2 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1433] topology](images/train_1433.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3261800_1 and 3258138_3
- `C2`: Increase transmission power for 3261800_1
- `C3`: Increase A3 Offset threshold for 3258138_3
- `C4`: Lift the tilt angle  of 3264875_2 by 10 degrees **← 정답**
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3258138_3
- `C6`: Check test server and transmission issues
- `C7`: Adjust the azimuth of 3264875_2 by 18 degrees
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3261800_1
- `C9`: Add neighbor relationship between 3264875_2 and 3258138_3
- `C10`: Increase A3 Offset threshold for 3261800_1
- `C11`: Adjust the azimuth of 3261800_1 by 26 degrees
- `C12`: Decrease A3 Offset threshold for 3258138_3
- `C13`: Decrease transmission power for 3258138_3
- `C14`: Press down the tilt angle of 3261800_1 by 5 degrees
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3258138_3
- `C16`: Decrease A3 Offset threshold for 3261800_1
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3261800_1
- `C18`: Increase transmission power for 3258138_3
- `C19`: Press down the tilt angle  of 3264875_2 by 10 degrees
- `C20`: Insufficient data; more data is needed for judgment.
- `C21`: Decrease transmission power for 3261800_1
- `C22`: Lift the tilt angle of 3261800_1 by 5 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.744 | MS1 | 121.4656621306 | 31.1446319879 | 738 | 504990 | -88.18 | 15.73 | 580.72 | 0.04 | 2.65 | 1562 |
| 2024-09-20 22:21:32.603 | MS1 | 121.4656619576 | 31.1446292166 | 738 | 504990 | -85.33 | 16.62 | 470.60 | 0.17 | 2.93 | 1588 |
| 2024-09-20 22:21:33.863 | MS1 | 121.4656778391 | 31.1446348240 | 738 | 504990 | -89.61 | 16.48 | 308.27 | 0.10 | 2.11 | 1583 |
| 2024-09-20 22:21:34.198 | MS1 | 121.4656712807 | 31.1446309093 | 738 | 504990 | -86.62 | 14.39 | 73.30 | 0.11 | 2.06 | 1569 |
| 2024-09-20 22:21:35.636 | MS1 | 121.4656622261 | 31.1446343531 | 738 | 504990 | -88.95 | 13.29 | 50.51 | 0.16 | 2.32 | 1574 |
| 2024-09-20 22:21:36.320 | MS1 | 121.4656721948 | 31.1446228505 | 738 | 504990 | -88.56 | 16.28 | 49.55 | 0.07 | 2.36 | 1588 |
| 2024-09-20 22:21:37.383 | MS1 | 121.4656752680 | 31.1446255597 | 738 | 504990 | -90.46 | 12.21 | 78.76 | 0.20 | 2.72 | 1577 |
| 2024-09-20 22:21:38.235 | MS1 | 121.4656596814 | 31.1446209554 | 738 | 504990 | -94.00 | 12.81 | 85.08 | 0.12 | 2.94 | 1576 |
| 2024-09-20 22:21:39.477 | MS1 | 121.4656779679 | 31.1446339961 | 738 | 504990 | -93.59 | 11.36 | 89.58 | 0.16 | 2.75 | 1576 |
| 2024-09-20 22:21:40.875 | MS1 | 121.4656774868 | 31.1446184563 | 738 | 504990 | -92.47 | 9.16 | 553.64 | 0.08 | 2.87 | 1597 |
| 2024-09-20 22:21:41.920 | MS1 | 121.4656640307 | 31.1446228393 | 738 | 504990 | -90.79 | 12.26 | 441.64 | 0.19 | 2.15 | 1569 |
| 2024-09-20 22:21:42.403 | MS1 | 121.4656738662 | 31.1446240971 | 738 | 504990 | -93.32 | 10.65 | 486.57 | 0.09 | 2.58 | 1560 |

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
| 3243384 | 4 | 121.4698926538 | 31.1460176791 | 86 | 8 | 2 | 28.0 | TDD | 63 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3258138 | 3 | 121.4711012711 | 31.1508445650 | 199 | 7 | 5 | 43.9 | TDD | 77 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3261800 | 1 | 121.4676327343 | 31.1503060671 | 222 | 2 | 8 | 35.6 | TDD | 738 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3264875 | 2 | 121.4757408195 | 31.1528933946 | 328 | 5 | 1 | 48.2 | TDD | 684 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |

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
| 2024-09-20 22:21:30.947 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.967 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.071 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.071 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.768 | NREventA3 | measId:2;ServCellPCI:337;Se... |
| 2024-09-20 22:21:38.008 | NRHandoverAttempt | SourcePCI:337;SourceNR-ARFC... |
| 2024-09-20 22:21:38.057 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.068 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.172 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.172 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3261800 | 1 | 78.8303 | 84.7367 | -115.7329 | 7.5861 | 108.6332 | 0.0123 | 0.0067 |
| 2024_09_20 22:00 | 3264875 | 2 | 18.6281 | 17.3854 | -116.5286 | 13.1938 | 163.8553 | 0.0151 | 0.0024 |
| 2024_09_20 22:00 | 3258138 | 3 | 19.0430 | 7.2394 | -115.8878 | 10.3695 | 187.6146 | 0.0193 | 0.0088 |
| 2024_09_20 22:00 | 3243384 | 4 | 17.1223 | 18.5168 | -116.8453 | 14.6679 | 169.7116 | 0.0126 | 0.0039 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413869_9275811B | 504990 | 738 | -87.8 | 504990 | 77 | -95.4 | 504990 | 684 | -91.9 | 504990 | 63 |
| MR_1774413869_A3750FC7 | 504990 | 738 | -86.2 | 504990 | 77 | -92.0 | 504990 | 684 | -93.2 | 504990 | 63 |
| MR_1774413869_485B9FF5 | 504990 | 738 | -85.6 | 504990 | 77 | -94.4 | 504990 | 684 | -95.0 | 504990 | 63 |
| MR_1774413869_02722C8D | 504990 | 738 | -87.5 | 504990 | 77 | -94.2 | 504990 | 684 | -95.7 | 504990 | 63 |
| MR_1774413869_2165EEF1 | 504990 | 738 | -87.2 | 504990 | 77 | -95.2 | 504990 | 684 | -95.2 | 504990 | 63 |
| MR_1774413869_4DEC027F | 504990 | 738 | -86.0 | 504990 | 77 | -94.2 | 504990 | 684 | -93.5 | 504990 | 63 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1434: `50dc8d47-143...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `50dc8d47-143c-4c33-a2d1-978e1d718812` |
| Tag | **single-answer** |
| 정답 | **C7** |
| C7 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1434] topology](images/train_1434.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3235961_1 by 10 degrees
- `C2`: Decrease transmission power for 3235961_1
- `C3`: Press down the tilt angle  of 3248505_4 by 4 degrees
- `C4`: Add neighbor relationship between 3229834_2 and 3248505_4
- `C5`: Decrease transmission power for 3248505_4
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3235961_1
- `C7`: Insufficient data; more data is needed for judgment. **← 정답**
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3248505_4
- `C9`: Decrease A3 Offset threshold for 3235961_1
- `C10`: Increase transmission power for 3235961_1
- `C11`: Increase transmission power for 3248505_4
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3248505_4
- `C13`: Add neighbor relationship between 3235961_1 and 3248505_4
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3235961_1
- `C15`: Adjust the azimuth of 3235961_1 by 40 degrees
- `C16`: Decrease A3 Offset threshold for 3248505_4
- `C17`: Lift the tilt angle of 3235961_1 by 10 degrees
- `C18`: Increase A3 Offset threshold for 3248505_4
- `C19`: Adjust the azimuth of 3248505_4 by 50 degrees
- `C20`: Increase A3 Offset threshold for 3235961_1
- `C21`: Check test server and transmission issues
- `C22`: Lift the tilt angle  of 3248505_4 by 4 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.788 | MS1 | 121.4656747412 | 31.1446228969 | 3 | 504990 | -87.30 | 13.82 | 373.68 | 0.08 | 2.34 | 1567 |
| 2024-09-20 22:21:32.580 | MS1 | 121.4656757667 | 31.1446251744 | 3 | 504990 | -91.35 | 15.64 | 475.65 | 0.13 | 2.14 | 1577 |
| 2024-09-20 22:21:33.763 | MS1 | 121.4656696614 | 31.1446305023 | 3 | 504990 | -85.70 | 13.21 | 592.98 | 0.15 | 2.78 | 1592 |
| 2024-09-20 22:21:34.623 | MS1 | 121.4656722815 | 31.1446346048 | 3 | 504990 | -90.86 | 12.97 | 59.97 | 0.18 | 2.50 | 1590 |
| 2024-09-20 22:21:35.148 | MS1 | 121.4656669435 | 31.1446294343 | 3 | 504990 | -90.18 | 16.32 | 94.88 | 0.05 | 2.30 | 1591 |
| 2024-09-20 22:21:36.495 | MS1 | 121.4656709968 | 31.1446280992 | 3 | 504990 | -88.78 | 12.65 | 85.42 | 0.20 | 2.08 | 1571 |
| 2024-09-20 22:21:37.271 | MS1 | 121.4656774775 | 31.1446277339 | 3 | 504990 | -92.51 | 7.12 | 81.41 | 0.05 | 3.00 | 1582 |
| 2024-09-20 22:21:38.555 | MS1 | 121.4656679300 | 31.1446350369 | 3 | 504990 | -90.85 | 12.30 | 91.01 | 0.06 | 2.37 | 1565 |
| 2024-09-20 22:21:39.137 | MS1 | 121.4656762538 | 31.1446223567 | 3 | 504990 | -90.54 | 10.46 | 61.39 | 0.14 | 2.72 | 1583 |
| 2024-09-20 22:21:40.964 | MS1 | 121.4656693715 | 31.1446239344 | 3 | 504990 | -93.29 | 7.80 | 457.37 | 0.08 | 2.63 | 1561 |
| 2024-09-20 22:21:41.304 | MS1 | 121.4656618223 | 31.1446329988 | 3 | 504990 | -92.29 | 11.52 | 429.98 | 0.16 | 2.47 | 1562 |
| 2024-09-20 22:21:42.416 | MS1 | 121.4656582706 | 31.1446198693 | 3 | 504990 | -93.05 | 8.35 | 302.77 | 0.00 | 2.80 | 1585 |

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
| 3216406 | 3 | 121.4668827028 | 31.1441961810 | 341 | 15 | 8 | 40.9 | TDD | 939 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3229834 | 2 | 121.4645007402 | 31.1446900889 | 244 | 3 | 3 | 22.2 | TDD | 587 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3235961 | 1 | 121.4708111740 | 31.1519865015 | 251 | 11 | 6 | 43.2 | TDD | 3 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3248505 | 4 | 121.4665697475 | 31.1522566856 | 32 | 3 | 10 | 21.0 | TDD | 166 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |

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
| 2024-09-20 22:21:30.825 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.840 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:30.961 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.961 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.642 | NREventA3 | measId:2;ServCellPCI:552;Se... |
| 2024-09-20 22:21:37.882 | NRHandoverAttempt | SourcePCI:552;SourceNR-ARFC... |
| 2024-09-20 22:21:37.931 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.942 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.042 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.042 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3235961 | 1 | 79.2194 | 85.8466 | -117.8082 | 11.7814 | 169.9754 | 0.0161 | 0.0156 |
| 2024_09_19 22:00 | 3229834 | 2 | 75.5020 | 83.6630 | -114.6067 | 14.8915 | 196.9301 | 0.0147 | 0.0078 |
| 2024_09_19 22:00 | 3216406 | 3 | 76.7983 | 78.7412 | -116.8253 | 5.8532 | 80.8227 | 0.0117 | 0.0158 |
| 2024_09_19 22:00 | 3248505 | 4 | 88.5863 | 92.1078 | -116.3999 | 15.7457 | 121.4357 | 0.0025 | 0.0086 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412675_E4FE5D18 | 504990 | 3 | -89.2 | 504990 | 166 | -97.5 | 504990 | 587 | -103.7 | 504990 | 939 |
| MR_1774412675_F6BE4096 | 504990 | 3 | -90.5 | 504990 | 166 | -96.9 | 504990 | 587 | -103.5 | 504990 | 939 |
| MR_1774412675_1D1A61C0 | 504990 | 3 | -90.2 | 504990 | 166 | -95.7 | 504990 | 587 | -103.7 | 504990 | 939 |
| MR_1774412675_59C99693 | 504990 | 3 | -89.7 | 504990 | 166 | -94.0 | 504990 | 587 | -103.8 | 504990 | 939 |
| MR_1774412675_8365BE3C | 504990 | 3 | -91.4 | 504990 | 166 | -95.9 | 504990 | 587 | -105.7 | 504990 | 939 |
| MR_1774412675_CBA06422 | 504990 | 3 | -89.3 | 504990 | 166 | -94.2 | 504990 | 587 | -104.8 | 504990 | 939 |
| MR_1774412675_7F4F7612 | 504990 | 3 | -90.8 | 504990 | 166 | -94.4 | 504990 | 587 | -105.2 | 504990 | 939 |
| MR_1774412675_F9189BC9 | 504990 | 3 | -89.0 | 504990 | 166 | -94.3 | 504990 | 587 | -105.6 | 504990 | 939 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1435: `643e7382-296...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `643e7382-2961-479c-be28-11500e272244` |
| Tag | **multiple-answer** |
| 정답 | **C2|C6|C20|C21** |
| C2 의미 | Decrease transmission power for 3239398_5 |
| C6 의미 | Increase A3 Offset threshold for 3223899_1 |
| C20 의미 | Press down the tilt angle  of 3239398_5 by 1 degrees |
| C21 의미 | Increase A3 Offset threshold for 3239398_5 |
| 패턴 분류 | **P3 Overshoot (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1435] topology](images/train_1435.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 5 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 5개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3239398_5
- `C2`: Decrease transmission power for 3239398_5 **← 정답**
- `C3`: Increase transmission power for 3239398_5
- `C4`: Lift the tilt angle of 3223899_1 by 5 degrees
- `C5`: Decrease A3 Offset threshold for 3239398_5
- `C6`: Increase A3 Offset threshold for 3223899_1 **← 정답**
- `C7`: Decrease transmission power for 3223899_1
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3223899_1
- `C9`: Press down the tilt angle of 3223899_1 by 5 degrees
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3223899_1
- `C11`: Insufficient data; more data is needed for judgment.
- `C12`: Decrease A3 Offset threshold for 3223899_1
- `C13`: Check test server and transmission issues
- `C14`: Add neighbor relationship between 3223899_1 and 3239398_5
- `C15`: Lift the tilt angle  of 3239398_5 by 1 degrees
- `C16`: Add neighbor relationship between 3248102_4 and 3239398_5
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3239398_5
- `C18`: Increase transmission power for 3223899_1
- `C19`: Adjust the azimuth of 3239398_5 by 15 degrees
- `C20`: Press down the tilt angle  of 3239398_5 by 1 degrees **← 정답**
- `C21`: Increase A3 Offset threshold for 3239398_5 **← 정답**
- `C22`: Adjust the azimuth of 3223899_1 by 42 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.149 | MS1 | 121.4656695602 | 31.1446182255 | 353 | 504990 | -75.01 | 13.85 | 492.61 | 0.15 | 2.00 | 1580 |
| 2024-09-20 22:21:32.679 | MS1 | 121.4656773826 | 31.1446317488 | 353 | 504990 | -79.00 | 16.50 | 426.83 | 0.05 | 2.56 | 1599 |
| 2024-09-20 22:21:33.676 | MS1 | 121.4656728343 | 31.1446275549 | 353 | 504990 | -84.73 | 13.78 | 451.79 | 0.02 | 2.25 | 1587 |
| 2024-09-20 22:21:34.909 | MS1 | 121.4656653962 | 31.1446212049 | 428 | 504990 | -81.33 | 4.37 | 56.01 | 0.20 | 1.22 | 1599 |
| 2024-09-20 22:21:35.949 | MS1 | 121.4656689736 | 31.1446206356 | 428 | 504990 | -86.39 | 3.08 | 59.19 | 0.01 | 1.30 | 1562 |
| 2024-09-20 22:21:36.893 | MS1 | 121.4656650106 | 31.1446299815 | 353 | 504990 | -87.62 | 3.19 | 29.37 | 0.12 | 1.00 | 1577 |
| 2024-09-20 22:21:37.650 | MS1 | 121.4656669091 | 31.1446205053 | 353 | 504990 | -81.60 | 2.01 | 64.93 | 0.18 | 1.04 | 1565 |
| 2024-09-20 22:21:38.991 | MS1 | 121.4656773583 | 31.1446188699 | 428 | 504990 | -89.09 | 2.76 | 65.10 | 0.15 | 1.41 | 1599 |
| 2024-09-20 22:21:39.717 | MS1 | 121.4656700504 | 31.1446262754 | 428 | 504990 | -83.17 | 3.34 | 65.74 | 0.08 | 1.01 | 1590 |
| 2024-09-20 22:21:40.772 | MS1 | 121.4656633031 | 31.1446208331 | 428 | 504990 | -80.67 | 16.00 | 456.49 | 0.13 | 2.57 | 1571 |
| 2024-09-20 22:21:41.805 | MS1 | 121.4656604052 | 31.1446237652 | 428 | 504990 | -80.42 | 16.22 | 556.29 | 0.06 | 2.97 | 1571 |
| 2024-09-20 22:21:42.859 | MS1 | 121.4656731860 | 31.1446332850 | 428 | 504990 | -76.05 | 15.31 | 378.35 | 0.12 | 2.43 | 1584 |

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
| 3215150 | 2 | 121.4709198763 | 31.1464982271 | 145 | 7 | 1 | 36.5 | TDD | 581 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3223899 | 1 | 121.4728543361 | 31.1542897814 | 254 | 3 | 0 | 37.9 | TDD | 353 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3239398 | 5 | 121.4681559405 | 31.1526176665 | 180 | 0 | 12 | 17.8 | TDD | 726 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3248102 | 4 | 121.4737013941 | 31.1449499122 | 214 | 7 | 0 | 28.3 | TDD | 978 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3260423 | 3 | 121.4656835919 | 31.1505977930 | 7 | 5 | 8 | 27.2 | TDD | 428 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |

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
| 2024-09-20 22:21:30.860 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.876 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.013 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.013 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:33.670 | NREventA3 | measId:2;ServCellPCI:97;Ser... |
| 2024-09-20 22:21:33.910 | NRHandoverAttempt | SourcePCI:97;SourceNR-ARFCN... |
| 2024-09-20 22:21:33.955 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:33.965 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:34.106 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:34.106 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.670 | NREventA3 | measId:2;ServCellPCI:1;Serv... |
| 2024-09-20 22:21:35.910 | NRHandoverAttempt | SourcePCI:1;SourceNR-ARFCN:... |
| 2024-09-20 22:21:35.943 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.953 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:36.073 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.073 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.670 | NREventA3 | measId:2;ServCellPCI:97;Ser... |
| 2024-09-20 22:21:37.910 | NRHandoverAttempt | SourcePCI:97;SourceNR-ARFCN... |
| 2024-09-20 22:21:37.958 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.970 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.082 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.082 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3223899 | 1 | 5.9860 | 15.9961 | -116.7334 | 14.2874 | 131.2298 | 0.0070 | 0.0098 |
| 2024_09_20 22:00 | 3215150 | 2 | 12.6151 | 14.2794 | -117.8589 | 11.2711 | 133.6466 | 0.0100 | 0.0131 |
| 2024_09_20 22:00 | 3260423 | 3 | 11.5811 | 15.4040 | -117.5295 | 13.1656 | 110.2929 | 0.0153 | 0.0125 |
| 2024_09_20 22:00 | 3248102 | 4 | 17.9202 | 8.5941 | -114.6682 | 19.4292 | 192.1136 | 0.0086 | 0.0009 |
| 2024_09_20 22:00 | 3239398 | 5 | 18.5608 | 11.8610 | -116.4472 | 12.2552 | 101.3764 | 0.0061 | 0.0160 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413544_3E10782B | 504990 | 428 | -80.8 | 504990 | 353 | -80.9 | 504990 | 726 | -82.0 | 504990 | 978 |
| MR_1774413544_388B0624 | 504990 | 353 | -80.8 | 504990 | 428 | -79.3 | 504990 | 726 | -79.1 | 504990 | 978 |
| MR_1774413544_AB74003F | 504990 | 353 | -80.9 | 504990 | 428 | -77.9 | 504990 | 726 | -79.1 | 504990 | 978 |
| MR_1774413544_DEC97457 | 504990 | 428 | -83.2 | 504990 | 353 | -80.0 | 504990 | 726 | -81.3 | 504990 | 978 |
| MR_1774413544_4CE0470B | 504990 | 353 | -80.3 | 504990 | 428 | -79.6 | 504990 | 726 | -81.2 | 504990 | 978 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1436: `381f29f6-0e8...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `381f29f6-0e88-4ab9-8098-6b2045c67167` |
| Tag | **single-answer** |
| 정답 | **C1** |
| C1 의미 | Decrease A3 Offset threshold for 3232122_4 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1436] topology](images/train_1436.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3232122_4 **← 정답**
- `C2`: Lift the tilt angle of 3232122_4 by 10 degrees
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3232122_4
- `C4`: Adjust the azimuth of 3232122_4 by 50 degrees
- `C5`: Decrease transmission power for 3232122_4
- `C6`: Decrease transmission power for 3234119_1
- `C7`: Check test server and transmission issues
- `C8`: Increase A3 Offset threshold for 3232122_4
- `C9`: Increase transmission power for 3232122_4
- `C10`: Decrease A3 Offset threshold for 3234119_1
- `C11`: Increase A3 Offset threshold for 3234119_1
- `C12`: Press down the tilt angle  of 3234119_1 by 10 degrees
- `C13`: Adjust the azimuth of 3234119_1 by 50 degrees
- `C14`: Add neighbor relationship between 3220589_3 and 3234119_1
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3234119_1
- `C16`: Lift the tilt angle  of 3234119_1 by 10 degrees
- `C17`: Add neighbor relationship between 3232122_4 and 3234119_1
- `C18`: Press down the tilt angle of 3232122_4 by 10 degrees
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3232122_4
- `C20`: Increase transmission power for 3234119_1
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3234119_1
- `C22`: Insufficient data; more data is needed for judgment.

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.583 | MS1 | 121.4656693416 | 31.1446185183 | 319 | 504990 | -79.06 | 15.99 | 334.39 | 0.01 | 2.49 | 1600 |
| 2024-09-20 22:21:32.696 | MS1 | 121.4656637148 | 31.1446295686 | 319 | 504990 | -80.28 | 17.09 | 438.38 | 0.10 | 2.78 | 1596 |
| 2024-09-20 22:21:33.653 | MS1 | 121.4656601164 | 31.1446248895 | 319 | 504990 | -82.37 | 17.69 | 362.43 | 0.08 | 2.27 | 1578 |
| 2024-09-20 22:21:34.329 | MS1 | 121.4656600692 | 31.1446297066 | 319 | 504990 | -92.48 | -1.53 | 32.60 | 0.04 | 1.06 | 1580 |
| 2024-09-20 22:21:35.696 | MS1 | 121.4656659903 | 31.1446248253 | 319 | 504990 | -87.38 | -2.20 | 69.18 | 0.11 | 1.36 | 1579 |
| 2024-09-20 22:21:36.637 | MS1 | 121.4656771954 | 31.1446258724 | 319 | 504990 | -92.20 | -0.57 | 60.42 | 0.16 | 1.43 | 1586 |
| 2024-09-20 22:21:37.663 | MS1 | 121.4656770657 | 31.1446323790 | 319 | 504990 | -85.03 | -3.79 | 43.25 | 0.16 | 1.43 | 1595 |
| 2024-09-20 22:21:38.321 | MS1 | 121.4656591087 | 31.1446285262 | 319 | 504990 | -86.50 | -2.79 | 45.12 | 0.19 | 1.40 | 1583 |
| 2024-09-20 22:21:39.501 | MS1 | 121.4656695571 | 31.1446327419 | 506 | 504990 | -82.10 | 17.33 | 303.22 | 0.12 | 1.23 | 1564 |
| 2024-09-20 22:21:40.591 | MS1 | 121.4656752543 | 31.1446358272 | 506 | 504990 | -84.34 | 17.80 | 450.64 | 0.19 | 2.99 | 1579 |
| 2024-09-20 22:21:41.908 | MS1 | 121.4656631987 | 31.1446295974 | 506 | 504990 | -82.57 | 15.54 | 555.62 | 0.09 | 2.45 | 1593 |
| 2024-09-20 22:21:42.973 | MS1 | 121.4656743709 | 31.1446273680 | 506 | 504990 | -79.45 | 12.95 | 515.50 | 0.11 | 2.83 | 1561 |

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
| 3220589 | 3 | 121.4753737116 | 31.1478230148 | 261 | 11 | 4 | 35.1 | TDD | 572 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3232122 | 4 | 121.4670581173 | 31.1462934716 | 294 | 15 | 7 | 34.0 | TDD | 319 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3234119 | 1 | 121.4732104031 | 31.1496672399 | 137 | 9 | 1 | 40.9 | TDD | 506 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3265333 | 2 | 121.4694060040 | 31.1456279248 | 284 | 10 | 2 | 32.1 | TDD | 59 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:30.948 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.969 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.085 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.085 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.801 | NREventA3 | measId:2;ServCellPCI:127;Se... |
| 2024-09-20 22:21:38.041 | NRHandoverAttempt | SourcePCI:127;SourceNR-ARFC... |
| 2024-09-20 22:21:38.073 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.087 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.199 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.199 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3234119 | 1 | 16.3159 | 13.1635 | -117.4916 | 8.0419 | 86.0003 | 0.0063 | 0.0017 |
| 2024_09_20 22:00 | 3265333 | 2 | 18.9604 | 13.9887 | -116.7275 | 14.7440 | 137.5857 | 0.0084 | 0.0044 |
| 2024_09_20 22:00 | 3220589 | 3 | 10.4715 | 17.5060 | -114.5483 | 18.3721 | 187.5319 | 0.0154 | 0.0135 |
| 2024_09_20 22:00 | 3232122 | 4 | 6.6212 | 16.2081 | -114.1351 | 12.5358 | 85.0328 | 0.0182 | 0.1074 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416811_D40FE7B6 | 504990 | 319 | -94.3 | 504990 | 506 | -87.5 | 504990 | 572 | -90.9 | 504990 | 59 |
| MR_1774416811_87FCEFF9 | 504990 | 506 | -87.5 | 504990 | 319 | -91.3 | 504990 | 572 | -90.8 | 504990 | 59 |
| MR_1774416811_C9171D97 | 504990 | 319 | -91.9 | 504990 | 506 | -85.5 | 504990 | 572 | -91.4 | 504990 | 59 |
| MR_1774416811_A4C07E31 | 504990 | 506 | -87.5 | 504990 | 319 | -92.7 | 504990 | 572 | -93.9 | 504990 | 59 |
| MR_1774416811_9F032962 | 504990 | 506 | -87.3 | 504990 | 319 | -90.9 | 504990 | 572 | -93.9 | 504990 | 59 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1437: `716fdee2-00e...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `716fdee2-00e6-4391-aa1a-a69d49b01715` |
| Tag | **multiple-answer** |
| 정답 | **C3|C7|C11|C15** |
| C3 의미 | Increase A3 Offset threshold for 3279157_4 |
| C7 의미 | Press down the tilt angle  of 3279157_4 by 1 degrees |
| C11 의미 | Increase A3 Offset threshold for 3265811_2 |
| C15 의미 | Decrease transmission power for 3279157_4 |
| 패턴 분류 | **P2 Ping-pong** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1437] topology](images/train_1437.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 5 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 5개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3279157_4
- `C2`: Lift the tilt angle  of 3279157_4 by 1 degrees
- `C3`: Increase A3 Offset threshold for 3279157_4 **← 정답**
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3279157_4
- `C5`: Insufficient data; more data is needed for judgment.
- `C6`: Adjust the azimuth of 3265811_2 by 44 degrees
- `C7`: Press down the tilt angle  of 3279157_4 by 1 degrees **← 정답**
- `C8`: Add neighbor relationship between 3265811_2 and 3279157_4
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3265811_2
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3265811_2
- `C11`: Increase A3 Offset threshold for 3265811_2 **← 정답**
- `C12`: Increase transmission power for 3265811_2
- `C13`: Add neighbor relationship between 3248885_1 and 3279157_4
- `C14`: Press down the tilt angle of 3265811_2 by 4 degrees
- `C15`: Decrease transmission power for 3279157_4 **← 정답**
- `C16`: Adjust the azimuth of 3279157_4 by 14 degrees
- `C17`: Check test server and transmission issues
- `C18`: Decrease A3 Offset threshold for 3265811_2
- `C19`: Lift the tilt angle of 3265811_2 by 4 degrees
- `C20`: Decrease transmission power for 3265811_2
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3279157_4
- `C22`: Increase transmission power for 3279157_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.359 | MS1 | 121.4656773369 | 31.1446339551 | 403 | 504990 | -75.86 | 14.08 | 451.44 | 0.16 | 2.45 | 1563 |
| 2024-09-20 22:21:32.932 | MS1 | 121.4656616885 | 31.1446190061 | 403 | 504990 | -80.24 | 12.39 | 355.36 | 0.17 | 2.78 | 1573 |
| 2024-09-20 22:21:33.557 | MS1 | 121.4656634283 | 31.1446307816 | 403 | 504990 | -80.59 | 15.65 | 571.03 | 0.05 | 2.91 | 1562 |
| 2024-09-20 22:21:34.790 | MS1 | 121.4656739210 | 31.1446248107 | 87 | 504990 | -80.39 | 2.90 | 42.85 | 0.17 | 1.46 | 1564 |
| 2024-09-20 22:21:35.128 | MS1 | 121.4656659853 | 31.1446363395 | 87 | 504990 | -83.54 | 4.51 | 71.20 | 0.01 | 1.31 | 1588 |
| 2024-09-20 22:21:36.809 | MS1 | 121.4656686859 | 31.1446240955 | 403 | 504990 | -80.72 | 2.24 | 71.39 | 0.14 | 1.00 | 1560 |
| 2024-09-20 22:21:37.535 | MS1 | 121.4656752224 | 31.1446223007 | 403 | 504990 | -86.69 | 4.91 | 42.62 | 0.19 | 1.24 | 1589 |
| 2024-09-20 22:21:38.703 | MS1 | 121.4656591435 | 31.1446257864 | 87 | 504990 | -80.57 | 3.09 | 77.35 | 0.01 | 1.38 | 1584 |
| 2024-09-20 22:21:39.715 | MS1 | 121.4656662679 | 31.1446213781 | 87 | 504990 | -84.62 | 2.74 | 57.05 | 0.19 | 1.43 | 1579 |
| 2024-09-20 22:21:40.793 | MS1 | 121.4656626257 | 31.1446248602 | 87 | 504990 | -77.21 | 14.36 | 339.45 | 0.19 | 2.44 | 1560 |
| 2024-09-20 22:21:41.968 | MS1 | 121.4656683629 | 31.1446302760 | 87 | 504990 | -79.51 | 16.85 | 485.57 | 0.00 | 2.59 | 1584 |
| 2024-09-20 22:21:42.586 | MS1 | 121.4656666772 | 31.1446294956 | 87 | 504990 | -80.96 | 14.69 | 457.44 | 0.08 | 2.44 | 1568 |

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
| 3211588 | 5 | 121.4660302037 | 31.1535169312 | 227 | 5 | 9 | 23.5 | TDD | 988 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3220507 | 3 | 121.4698976028 | 31.1542253281 | 53 | 15 | 12 | 28.5 | TDD | 87 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3248885 | 1 | 121.4647418016 | 31.1501949019 | 302 | 8 | 6 | 37.0 | TDD | 338 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3265811 | 2 | 121.4755650707 | 31.1477431550 | 294 | 2 | 8 | 38.5 | TDD | 403 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3279157 | 4 | 121.4744867284 | 31.1537722511 | 233 | 0 | 11 | 34.1 | TDD | 763 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |

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
| 2024-09-20 22:21:30.924 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.941 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.073 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.073 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:33.726 | NREventA3 | measId:2;ServCellPCI:659;Se... |
| 2024-09-20 22:21:33.966 | NRHandoverAttempt | SourcePCI:659;SourceNR-ARFC... |
| 2024-09-20 22:21:33.996 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:34.010 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:34.134 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:34.134 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.726 | NREventA3 | measId:2;ServCellPCI:308;Se... |
| 2024-09-20 22:21:35.966 | NRHandoverAttempt | SourcePCI:308;SourceNR-ARFC... |
| 2024-09-20 22:21:36.004 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:36.015 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:36.118 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.118 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.726 | NREventA3 | measId:2;ServCellPCI:659;Se... |
| 2024-09-20 22:21:37.966 | NRHandoverAttempt | SourcePCI:659;SourceNR-ARFC... |
| 2024-09-20 22:21:38.004 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.015 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.156 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.156 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3248885 | 1 | 14.9308 | 8.3165 | -115.8164 | 8.2496 | 160.3346 | 0.0020 | 0.0195 |
| 2024_09_20 22:00 | 3265811 | 2 | 8.6492 | 12.1722 | -117.3098 | 12.1397 | 116.8567 | 0.0129 | 0.0131 |
| 2024_09_20 22:00 | 3220507 | 3 | 13.0370 | 14.9719 | -117.0715 | 6.6236 | 117.2957 | 0.0054 | 0.0108 |
| 2024_09_20 22:00 | 3279157 | 4 | 11.4221 | 17.7592 | -117.1226 | 16.7050 | 166.7992 | 0.0131 | 0.0002 |
| 2024_09_20 22:00 | 3211588 | 5 | 8.0758 | 14.2384 | -115.6278 | 5.8894 | 188.5219 | 0.0085 | 0.0151 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415789_41E5F634 | 504990 | 403 | -81.3 | 504990 | 87 | -79.7 | 504990 | 763 | -81.0 | 504990 | 338 |
| MR_1774415789_F72B6E05 | 504990 | 87 | -79.8 | 504990 | 403 | -77.5 | 504990 | 763 | -82.6 | 504990 | 338 |
| MR_1774415789_6198D343 | 504990 | 403 | -82.2 | 504990 | 87 | -77.2 | 504990 | 763 | -81.1 | 504990 | 338 |
| MR_1774415789_62D89F1D | 504990 | 403 | -78.5 | 504990 | 87 | -80.2 | 504990 | 763 | -82.5 | 504990 | 338 |
| MR_1774415789_F0125CC8 | 504990 | 87 | -82.0 | 504990 | 403 | -80.1 | 504990 | 763 | -79.2 | 504990 | 338 |
| MR_1774415789_9557B106 | 504990 | 403 | -81.7 | 504990 | 87 | -79.2 | 504990 | 763 | -80.0 | 504990 | 338 |
| MR_1774415789_6197D251 | 504990 | 403 | -80.2 | 504990 | 87 | -77.2 | 504990 | 763 | -82.3 | 504990 | 338 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1438: `d9d2cbda-293...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `d9d2cbda-2934-47eb-b029-ca0e18e08b7f` |
| Tag | **single-answer** |
| 정답 | **C4** |
| C4 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1438] topology](images/train_1438.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3255165_1 by 10 degrees
- `C2`: Press down the tilt angle of 3255165_1 by 10 degrees
- `C3`: Lift the tilt angle  of 3264666_4 by 5 degrees
- `C4`: Check test server and transmission issues **← 정답**
- `C5`: Decrease A3 Offset threshold for 3255165_1
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3255165_1
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3255165_1
- `C8`: Increase A3 Offset threshold for 3264666_4
- `C9`: Adjust the azimuth of 3255165_1 by 50 degrees
- `C10`: Decrease transmission power for 3264666_4
- `C11`: Increase transmission power for 3255165_1
- `C12`: Increase transmission power for 3264666_4
- `C13`: Decrease transmission power for 3255165_1
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3264666_4
- `C15`: Decrease A3 Offset threshold for 3264666_4
- `C16`: Press down the tilt angle  of 3264666_4 by 5 degrees
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3264666_4
- `C18`: Add neighbor relationship between 3255165_1 and 3264666_4
- `C19`: Insufficient data; more data is needed for judgment.
- `C20`: Add neighbor relationship between 3246066_2 and 3264666_4
- `C21`: Adjust the azimuth of 3264666_4 by 20 degrees
- `C22`: Increase A3 Offset threshold for 3255165_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.179 | MS1 | 121.4656736426 | 31.1446308399 | 224 | 504990 | -91.47 | 13.40 | 324.37 | 0.19 | 2.18 | 1569 |
| 2024-09-20 22:21:32.301 | MS1 | 121.4656732577 | 31.1446216285 | 224 | 504990 | -90.31 | 15.31 | 595.36 | 0.06 | 2.24 | 1571 |
| 2024-09-20 22:21:33.755 | MS1 | 121.4656649533 | 31.1446216260 | 224 | 504990 | -85.23 | 12.87 | 320.74 | 0.00 | 2.76 | 1572 |
| 2024-09-20 22:21:34.545 | MS1 | 121.4656585974 | 31.1446236568 | 224 | 504990 | -88.56 | 17.22 | 77.02 | 0.14 | 3.00 | 494 |
| 2024-09-20 22:21:35.485 | MS1 | 121.4656727898 | 31.1446276718 | 224 | 504990 | -89.11 | 17.83 | 58.64 | 0.08 | 2.28 | 324 |
| 2024-09-20 22:21:36.379 | MS1 | 121.4656695268 | 31.1446268966 | 224 | 504990 | -88.06 | 14.11 | 62.38 | 0.03 | 2.45 | 385 |
| 2024-09-20 22:21:37.954 | MS1 | 121.4656641166 | 31.1446262100 | 224 | 504990 | -92.05 | 8.81 | 90.61 | 0.18 | 2.10 | 303 |
| 2024-09-20 22:21:38.862 | MS1 | 121.4656717999 | 31.1446222784 | 224 | 504990 | -90.30 | 12.63 | 76.51 | 0.11 | 2.93 | 480 |
| 2024-09-20 22:21:39.903 | MS1 | 121.4656593473 | 31.1446343149 | 224 | 504990 | -89.92 | 12.87 | 77.03 | 0.08 | 2.83 | 440 |
| 2024-09-20 22:21:40.321 | MS1 | 121.4656630278 | 31.1446321480 | 224 | 504990 | -89.59 | 8.41 | 594.60 | 0.11 | 2.07 | 1589 |
| 2024-09-20 22:21:41.580 | MS1 | 121.4656708263 | 31.1446347189 | 224 | 504990 | -92.63 | 12.89 | 427.78 | 0.17 | 2.61 | 1567 |
| 2024-09-20 22:21:42.203 | MS1 | 121.4656700236 | 31.1446337010 | 224 | 504990 | -90.17 | 12.51 | 334.35 | 0.06 | 2.49 | 1597 |

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
| 3246066 | 2 | 121.4743385201 | 31.1488126676 | 304 | 3 | 9 | 46.3 | TDD | 537 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3249583 | 3 | 121.4693280756 | 31.1474644546 | 55 | 9 | 5 | 20.7 | TDD | 710 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3255165 | 1 | 121.4680175477 | 31.1448562618 | 79 | 3 | 2 | 33.4 | TDD | 224 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3264666 | 4 | 121.4739532483 | 31.1529182297 | 201 | 3 | 6 | 41.2 | TDD | 255 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |

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
| 2024-09-20 22:21:31.634 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.651 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.754 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.754 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.467 | NREventA3 | measId:2;ServCellPCI:41;Ser... |
| 2024-09-20 22:21:38.707 | NRHandoverAttempt | SourcePCI:41;SourceNR-ARFCN... |
| 2024-09-20 22:21:38.752 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.762 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.903 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.903 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3255165 | 1 | 13.8476 | 6.5913 | -115.7336 | 10.1837 | 172.4355 | 0.0085 | 0.0083 |
| 2024_09_20 22:00 | 3246066 | 2 | 13.4053 | 5.2405 | -117.5433 | 10.1663 | 125.2612 | 0.0167 | 0.0034 |
| 2024_09_20 22:00 | 3249583 | 3 | 16.7521 | 7.7742 | -117.8698 | 15.4706 | 132.2200 | 0.0171 | 0.0028 |
| 2024_09_20 22:00 | 3264666 | 4 | 17.5342 | 19.1734 | -114.0515 | 17.9971 | 89.5501 | 0.0200 | 0.0038 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412023_4E75D913 | 504990 | 224 | -87.0 | 504990 | 255 | -97.8 | 504990 | 537 | -98.1 | 504990 | 710 |
| MR_1774412023_963790BB | 504990 | 224 | -87.4 | 504990 | 255 | -96.0 | 504990 | 537 | -98.3 | 504990 | 710 |
| MR_1774412023_E467F333 | 504990 | 224 | -90.5 | 504990 | 255 | -95.7 | 504990 | 537 | -98.4 | 504990 | 710 |
| MR_1774412023_FFC2EFF5 | 504990 | 224 | -89.7 | 504990 | 255 | -97.5 | 504990 | 537 | -96.6 | 504990 | 710 |
| MR_1774412023_96EFA5AF | 504990 | 224 | -90.2 | 504990 | 255 | -96.0 | 504990 | 537 | -96.8 | 504990 | 710 |
| MR_1774412023_A0A2DE84 | 504990 | 224 | -89.9 | 504990 | 255 | -98.4 | 504990 | 537 | -95.7 | 504990 | 710 |
| MR_1774412023_F3329C91 | 504990 | 224 | -89.4 | 504990 | 255 | -98.8 | 504990 | 537 | -98.7 | 504990 | 710 |
| MR_1774412023_345F582D | 504990 | 224 | -89.2 | 504990 | 255 | -97.6 | 504990 | 537 | -97.6 | 504990 | 710 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1439: `e72857c2-04b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `e72857c2-04b2-47c2-a191-261d7582fdbd` |
| Tag | **single-answer** |
| 정답 | **C1** |
| C1 의미 | Add neighbor relationship between 3223455_4 and 3270173_1 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1439] topology](images/train_1439.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3223455_4 and 3270173_1 **← 정답**
- `C2`: Lift the tilt angle  of 3270173_1 by 4 degrees
- `C3`: Lift the tilt angle of 3223455_4 by 4 degrees
- `C4`: Press down the tilt angle of 3223455_4 by 4 degrees
- `C5`: Decrease A3 Offset threshold for 3270173_1
- `C6`: Press down the tilt angle  of 3270173_1 by 4 degrees
- `C7`: Increase transmission power for 3223455_4
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3223455_4
- `C9`: Increase transmission power for 3270173_1
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3223455_4
- `C11`: Check test server and transmission issues
- `C12`: Adjust the azimuth of 3270173_1 by 35 degrees
- `C13`: Decrease transmission power for 3223455_4
- `C14`: Add neighbor relationship between 3252942_2 and 3270173_1
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3270173_1
- `C16`: Decrease A3 Offset threshold for 3223455_4
- `C17`: Decrease transmission power for 3270173_1
- `C18`: Increase A3 Offset threshold for 3223455_4
- `C19`: Insufficient data; more data is needed for judgment.
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3270173_1
- `C21`: Increase A3 Offset threshold for 3270173_1
- `C22`: Adjust the azimuth of 3223455_4 by 50 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.639 | MS1 | 121.4656716302 | 31.1446289793 | 319 | 504990 | -80.68 | 17.98 | 318.98 | 0.04 | 2.32 | 1569 |
| 2024-09-20 22:21:32.988 | MS1 | 121.4656734358 | 31.1446252183 | 319 | 504990 | -79.01 | 15.39 | 580.01 | 0.11 | 2.58 | 1564 |
| 2024-09-20 22:21:33.948 | MS1 | 121.4656738816 | 31.1446377090 | 319 | 504990 | -76.21 | 17.27 | 377.45 | 0.16 | 2.88 | 1569 |
| 2024-09-20 22:21:34.453 | MS1 | 121.4656705503 | 31.1446334196 | 319 | 504990 | -94.55 | -3.64 | 36.19 | 0.07 | 1.36 | 1582 |
| 2024-09-20 22:21:35.562 | MS1 | 121.4656639226 | 31.1446362147 | 319 | 504990 | -88.69 | -3.75 | 68.73 | 0.13 | 1.11 | 1568 |
| 2024-09-20 22:21:36.631 | MS1 | 121.4656617509 | 31.1446341574 | 319 | 504990 | -89.15 | -1.96 | 29.08 | 0.02 | 1.18 | 1581 |
| 2024-09-20 22:21:37.631 | MS1 | 121.4656675034 | 31.1446206480 | 319 | 504990 | -90.29 | -0.77 | 68.39 | 0.10 | 1.38 | 1592 |
| 2024-09-20 22:21:38.591 | MS1 | 121.4656599751 | 31.1446267764 | 319 | 504990 | -76.47 | 16.74 | 366.95 | 0.10 | 1.40 | 1566 |
| 2024-09-20 22:21:39.181 | MS1 | 121.4656622676 | 31.1446307188 | 319 | 504990 | -81.85 | 12.26 | 352.28 | 0.02 | 1.06 | 1565 |
| 2024-09-20 22:21:40.199 | MS1 | 121.4656739627 | 31.1446188248 | 319 | 504990 | -78.86 | 13.92 | 559.26 | 0.18 | 2.83 | 1591 |
| 2024-09-20 22:21:41.725 | MS1 | 121.4656673145 | 31.1446237650 | 319 | 504990 | -80.12 | 13.89 | 314.08 | 0.20 | 2.52 | 1591 |
| 2024-09-20 22:21:42.853 | MS1 | 121.4656735809 | 31.1446321070 | 319 | 504990 | -77.68 | 15.45 | 298.44 | 0.03 | 2.24 | 1581 |

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
| 3223455 | 4 | 121.4721936903 | 31.1443736046 | 323 | 2 | 11 | 16.7 | TDD | 319 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3226022 | 3 | 121.4714403493 | 31.1511703758 | 83 | 11 | 6 | 15.2 | TDD | 373 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3252942 | 2 | 121.4718562360 | 31.1525644396 | 225 | 9 | 1 | 15.7 | TDD | 233 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3270173 | 1 | 121.4752066615 | 31.1506780830 | 269 | 2 | 4 | 40.6 | TDD | 425 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |

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
| 2024-09-20 22:21:31.033 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.050 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.175 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.175 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.846 | NREventA3 | measId:2;ServCellPCI:180;Se... |
| 2024-09-20 22:21:35.846 | NREventA3 | measId:2;ServCellPCI:180;Se... |
| 2024-09-20 22:21:36.846 | NREventA3 | measId:2;ServCellPCI:180;Se... |
| 2024-09-20 22:21:39.346 | NRRRCReestablishAttempt | PCI:180 |
| 2024-09-20 22:21:39.363 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.374 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:39.520 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.520 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3270173 | 1 | 7.1615 | 15.5250 | -117.4877 | 13.3652 | 159.7006 | 0.0197 | 0.0070 |
| 2024_09_20 22:00 | 3252942 | 2 | 8.9448 | 11.8741 | -117.8033 | 13.3829 | 115.1741 | 0.0066 | 0.0087 |
| 2024_09_20 22:00 | 3226022 | 3 | 5.4024 | 10.9678 | -114.2594 | 15.7079 | 165.0830 | 0.0185 | 0.0032 |
| 2024_09_20 22:00 | 3223455 | 4 | 14.7784 | 15.7982 | -117.4655 | 11.3202 | 104.2438 | 0.0061 | 0.1963 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416431_0E225526 | 504990 | 319 | -94.1 | 504990 | 425 | -90.4 | 504990 | 233 | -99.8 | 504990 | 373 |
| MR_1774416431_C2BC7332 | 504990 | 425 | -87.4 | 504990 | 319 | -96.4 | 504990 | 233 | -100.3 | 504990 | 373 |
| MR_1774416431_D935B4E2 | 504990 | 319 | -96.2 | 504990 | 425 | -88.0 | 504990 | 233 | -99.7 | 504990 | 373 |
| MR_1774416431_F7EE70AB | 504990 | 319 | -96.3 | 504990 | 425 | -88.8 | 504990 | 233 | -97.2 | 504990 | 373 |
| MR_1774416431_8E4131FE | 504990 | 319 | -95.9 | 504990 | 425 | -89.2 | 504990 | 233 | -98.7 | 504990 | 373 |
| MR_1774416431_FBAF6C7D | 504990 | 425 | -90.1 | 504990 | 319 | -93.3 | 504990 | 233 | -99.2 | 504990 | 373 |
| MR_1774416431_D92370A1 | 504990 | 319 | -93.0 | 504990 | 425 | -88.5 | 504990 | 233 | -100.0 | 504990 | 373 |
| MR_1774416431_F99BEE37 | 504990 | 425 | -87.1 | 504990 | 319 | -95.4 | 504990 | 233 | -99.2 | 504990 | 373 |

> *... 2개 열 생략 (전체 14열)*

---
