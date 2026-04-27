# Track A 문제 분석 — train[1230]~train[1239]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[1230] ~ train[1239] (10개)

## 목차

1. [문제 1230: `8c2daca2-ad1...`](#1230) — single-answer, 정답: C22
2. [문제 1231: `f6cc87b0-0d4...`](#1231) — single-answer, 정답: C21
3. [문제 1232: `cdecdc75-b2f...`](#1232) — single-answer, 정답: C18
4. [문제 1233: `ebfda965-3b9...`](#1233) — multiple-answer, 정답: C7|C11
5. [문제 1234: `67c7d130-d64...`](#1234) — single-answer, 정답: C13
6. [문제 1235: `23954f46-f25...`](#1235) — multiple-answer, 정답: C17|C19
7. [문제 1236: `3866ca85-530...`](#1236) — single-answer, 정답: C17
8. [문제 1237: `71ac5469-ca1...`](#1237) — single-answer, 정답: C17
9. [문제 1238: `31be4e6f-a02...`](#1238) — single-answer, 정답: C9
10. [문제 1239: `fc175865-7db...`](#1239) — multiple-answer, 정답: C3|C20

---

### 문제 1230: `8c2daca2-ad1...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `8c2daca2-ad19-4f2b-b95c-31b94b8a1840` |
| Tag | **single-answer** |
| 정답 | **C22** |
| C22 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1230] topology](images/train_1230.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3255873_3 by 10 degrees
- `C2`: Add neighbor relationship between 3255873_3 and 3227267_2
- `C3`: Add neighbor relationship between 3241477_4 and 3227267_2
- `C4`: Check test server and transmission issues
- `C5`: Adjust the azimuth of 3227267_2 by 50 degrees
- `C6`: Increase transmission power for 3255873_3
- `C7`: Adjust the azimuth of 3255873_3 by 2 degrees
- `C8`: Increase A3 Offset threshold for 3227267_2
- `C9`: Lift the tilt angle  of 3227267_2 by 10 degrees
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3255873_3
- `C11`: Decrease transmission power for 3227267_2
- `C12`: Increase transmission power for 3227267_2
- `C13`: Decrease A3 Offset threshold for 3227267_2
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3227267_2
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3227267_2
- `C16`: Decrease A3 Offset threshold for 3255873_3
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3255873_3
- `C18`: Press down the tilt angle  of 3227267_2 by 10 degrees
- `C19`: Lift the tilt angle of 3255873_3 by 10 degrees
- `C20`: Increase A3 Offset threshold for 3255873_3
- `C21`: Decrease transmission power for 3255873_3
- `C22`: Insufficient data; more data is needed for judgment. **← 정답**

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.887 | MS1 | 121.4656685493 | 31.1446367029 | 788 | 504990 | -89.12 | 17.35 | 451.98 | 0.01 | 2.59 | 1598 |
| 2024-09-20 22:21:32.756 | MS1 | 121.4656751751 | 31.1446371884 | 788 | 504990 | -86.95 | 13.10 | 380.02 | 0.11 | 2.53 | 1589 |
| 2024-09-20 22:21:33.277 | MS1 | 121.4656724530 | 31.1446225382 | 788 | 504990 | -89.80 | 17.35 | 530.63 | 0.01 | 2.91 | 1594 |
| 2024-09-20 22:21:34.297 | MS1 | 121.4656706594 | 31.1446332262 | 788 | 504990 | -87.87 | 16.10 | 49.44 | 0.08 | 2.59 | 1586 |
| 2024-09-20 22:21:35.770 | MS1 | 121.4656738620 | 31.1446224269 | 788 | 504990 | -91.28 | 15.50 | 71.86 | 0.01 | 2.67 | 1561 |
| 2024-09-20 22:21:36.263 | MS1 | 121.4656717801 | 31.1446332651 | 788 | 504990 | -87.35 | 17.06 | 86.38 | 0.05 | 2.59 | 1574 |
| 2024-09-20 22:21:37.938 | MS1 | 121.4656660371 | 31.1446339101 | 788 | 504990 | -91.69 | 12.39 | 84.28 | 0.09 | 2.25 | 1569 |
| 2024-09-20 22:21:38.169 | MS1 | 121.4656777236 | 31.1446369053 | 788 | 504990 | -93.33 | 7.79 | 57.97 | 0.11 | 2.22 | 1588 |
| 2024-09-20 22:21:39.429 | MS1 | 121.4656630615 | 31.1446217361 | 788 | 504990 | -90.23 | 8.43 | 81.54 | 0.12 | 2.53 | 1576 |
| 2024-09-20 22:21:40.696 | MS1 | 121.4656743766 | 31.1446303115 | 788 | 504990 | -89.18 | 10.94 | 362.76 | 0.07 | 2.33 | 1562 |
| 2024-09-20 22:21:41.487 | MS1 | 121.4656627717 | 31.1446207762 | 788 | 504990 | -90.67 | 12.07 | 566.48 | 0.02 | 2.33 | 1587 |
| 2024-09-20 22:21:42.771 | MS1 | 121.4656606483 | 31.1446270553 | 788 | 504990 | -93.43 | 8.55 | 482.10 | 0.10 | 2.67 | 1561 |

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
| 3227267 | 2 | 121.4732088085 | 31.1468109220 | 47 | 9 | 4 | 28.2 | TDD | 713 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3241477 | 4 | 121.4657550015 | 31.1501200537 | 153 | 1 | 5 | 17.4 | TDD | 869 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3255873 | 3 | 121.4722975410 | 31.1548166412 | 211 | 11 | 6 | 45.7 | TDD | 788 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3258786 | 1 | 121.4645744280 | 31.1461599628 | 176 | 0 | 3 | 29.4 | TDD | 488 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |

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
| 2024-09-20 22:21:31.488 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.506 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.607 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.607 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.329 | NREventA3 | measId:2;ServCellPCI:305;Se... |
| 2024-09-20 22:21:38.569 | NRHandoverAttempt | SourcePCI:305;SourceNR-ARFC... |
| 2024-09-20 22:21:38.601 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.615 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.741 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.741 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3258786 | 1 | 89.6973 | 93.1866 | -117.8345 | 15.7181 | 179.5068 | 0.0017 | 0.0200 |
| 2024_09_19 22:00 | 3227267 | 2 | 88.9529 | 76.2837 | -114.9078 | 13.9174 | 170.2290 | 0.0140 | 0.0165 |
| 2024_09_19 22:00 | 3255873 | 3 | 79.1835 | 81.2919 | -117.7521 | 6.7844 | 121.3734 | 0.0087 | 0.0054 |
| 2024_09_19 22:00 | 3241477 | 4 | 89.0473 | 93.3454 | -114.4153 | 8.6261 | 164.6275 | 0.0052 | 0.0074 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416847_743C38EA | 504990 | 788 | -87.4 | 504990 | 713 | -89.5 | 504990 | 869 | -97.0 | 504990 | 488 |
| MR_1774416847_E73B33E2 | 504990 | 788 | -86.5 | 504990 | 713 | -87.0 | 504990 | 869 | -95.6 | 504990 | 488 |
| MR_1774416847_F6C5F236 | 504990 | 788 | -86.3 | 504990 | 713 | -89.0 | 504990 | 869 | -95.0 | 504990 | 488 |
| MR_1774416847_48C48FBA | 504990 | 788 | -86.0 | 504990 | 713 | -88.4 | 504990 | 869 | -96.8 | 504990 | 488 |
| MR_1774416847_E309CA06 | 504990 | 788 | -86.2 | 504990 | 713 | -87.6 | 504990 | 869 | -98.6 | 504990 | 488 |
| MR_1774416847_19268277 | 504990 | 788 | -87.1 | 504990 | 713 | -86.8 | 504990 | 869 | -96.0 | 504990 | 488 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1231: `f6cc87b0-0d4...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `f6cc87b0-0d4d-4f39-a8ec-44b47c4608e1` |
| Tag | **single-answer** |
| 정답 | **C21** |
| C21 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3241186_3 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1231] topology](images/train_1231.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3210650_5
- `C2`: Press down the tilt angle of 3241186_3 by 5 degrees
- `C3`: Add neighbor relationship between 3236109_9 and 3210650_5
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3210650_5
- `C5`: Decrease A3 Offset threshold for 3241186_3
- `C6`: Decrease transmission power for 3210650_5
- `C7`: Decrease A3 Offset threshold for 3210650_5
- `C8`: Decrease transmission power for 3241186_3
- `C9`: Insufficient data; more data is needed for judgment.
- `C10`: Increase transmission power for 3241186_3
- `C11`: Adjust the azimuth of 3210650_5 by 2 degrees
- `C12`: Check test server and transmission issues
- `C13`: Add neighbor relationship between 3241186_3 and 3210650_5
- `C14`: Lift the tilt angle  of 3210650_5 by 3 degrees
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3241186_3
- `C16`: Increase transmission power for 3210650_5
- `C17`: Lift the tilt angle of 3241186_3 by 5 degrees
- `C18`: Increase A3 Offset threshold for 3241186_3
- `C19`: Press down the tilt angle  of 3210650_5 by 3 degrees
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3210650_5
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3241186_3 **← 정답**
- `C22`: Adjust the azimuth of 3241186_3 by 15 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.499 | MS1 | 121.4656622455 | 31.1446315929 | 213 | 504990 | -94.03 | 12.91 | 523.16 | 0.07 | 2.97 | 1562 |
| 2024-09-20 22:21:32.352 | MS1 | 121.4656741974 | 31.1446343728 | 739 | 504990 | -94.96 | 11.06 | 429.37 | 0.06 | 2.99 | 1563 |
| 2024-09-20 22:21:33.787 | MS1 | 121.4656585229 | 31.1446213252 | 639 | 504990 | -93.74 | 9.21 | 407.88 | 0.13 | 2.01 | 1595 |
| 2024-09-20 22:21:34.920 | MS1 | 121.4656584031 | 31.1446348273 | 928 | 152650 | -96.42 | 3.54 | 90.17 | 0.08 | 1.74 | 977 |
| 2024-09-20 22:21:35.122 | MS1 | 121.4656758551 | 31.1446365584 | 457 | 152650 | -90.45 | 2.08 | 92.99 | 0.12 | 1.69 | 954 |
| 2024-09-20 22:21:36.350 | MS1 | 121.4656687234 | 31.1446242164 | 103 | 152650 | -88.63 | 7.25 | 75.36 | 0.02 | 1.78 | 961 |
| 2024-09-20 22:21:37.290 | MS1 | 121.4656657402 | 31.1446242771 | 263 | 152650 | -93.02 | 5.61 | 85.21 | 0.08 | 1.77 | 926 |
| 2024-09-20 22:21:38.955 | MS1 | 121.4656668480 | 31.1446256404 | 928 | 152650 | -91.09 | 3.60 | 98.19 | 0.14 | 1.70 | 935 |
| 2024-09-20 22:21:39.647 | MS1 | 121.4656771563 | 31.1446355125 | 457 | 152650 | -88.56 | 2.08 | 83.42 | 0.07 | 1.89 | 948 |
| 2024-09-20 22:21:40.957 | MS1 | 121.4656639770 | 31.1446354351 | 103 | 152650 | -90.03 | 3.42 | 78.34 | 0.18 | 2.92 | 1576 |
| 2024-09-20 22:21:41.389 | MS1 | 121.4656747762 | 31.1446180367 | 263 | 152650 | -93.39 | 7.93 | 63.63 | 0.16 | 2.52 | 1595 |
| 2024-09-20 22:21:42.399 | MS1 | 121.4656661792 | 31.1446193260 | 928 | 152650 | -93.33 | 4.79 | 79.69 | 0.18 | 2.67 | 1575 |

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
| 3210650 | 5 | 121.4674505878 | 31.1532130892 | 192 | 3 | 8 | 8.1 | TDD | 603 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3213197 | 11 | 121.4738526414 | 31.1504681357 | 353 | 11 | 3 | 11.9 | FDD | 235 | n1 | 152650 | 30M | 4T4R | 12 | 152650 |
| 3223751 | 4 | 121.4737476105 | 31.1479352107 | 35 | 9 | 1 | 29.7 | TDD | 26 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3224296 | 8 | 121.4661082942 | 31.1488907168 | 120 | 12 | 4 | 11.7 | FDD | 263 | n1 | 152650 | 30M | 4T4R | 27 | 152650 |
| 3229314 | 13 | 121.4676981180 | 31.1559099613 | 78 | 9 | 8 | 15.6 | FDD | 764 | n1 | 152650 | 30M | 4T4R | 15 | 152650 |
| 3236109 | 9 | 121.4730072132 | 31.1495414108 | 61 | 4 | 5 | 28.0 | FDD | 103 | n1 | 152650 | 30M | 4T4R | 20 | 152650 |
| 3241186 | 3 | 121.4640179086 | 31.1480541955 | 173 | 5 | 6 | 0.5 | TDD | 213 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3241816 | 6 | 121.4694811931 | 31.1524893996 | 155 | 9 | 8 | 4.5 | TDD | 639 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3256292 | 7 | 121.4645153065 | 31.1526814186 | 317 | 12 | 10 | 25.7 | FDD | 928 | n1 | 152650 | 30M | 4T4R | 12 | 152650 |
| 3260115 | 12 | 121.4681670043 | 31.1523476764 | 139 | 9 | 1 | 4.2 | FDD | 691 | n1 | 152650 | 30M | 4T4R | 11 | 152650 |
| 3261494 | 10 | 121.4672664215 | 31.1525934630 | 237 | 15 | 12 | 25.8 | FDD | 457 | n1 | 152650 | 30M | 4T4R | 10 | 152650 |
| 3261984 | 1 | 121.4702482074 | 31.1531665516 | 60 | 13 | 5 | 28.4 | TDD | 320 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3272604 | 2 | 121.4723831512 | 31.1535166147 | 81 | 15 | 8 | 8.1 | TDD | 739 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |

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
| 2024-09-20 22:21:31.467 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.490 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.617 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.617 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.366 | NREventA2 | measId:1;ServCellPCI:77;Ser... |
| 2024-09-20 22:21:35.508 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.726 | NREventA5 | measId:3;ServCellPCI:77;Ser... |
| 2024-09-20 22:21:35.766 | NRHandoverAttempt | SourcePCI:77;SourceNR-ARFCN... |
| 2024-09-20 22:21:35.793 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.804 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:35.953 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.953 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3261984 | 1 | 19.2962 | 10.4694 | -116.8505 | 12.8082 | 109.2750 | 0.0017 | 0.0103 |
| 2024_09_20 22:00 | 3272604 | 2 | 19.1639 | 14.7829 | -115.0229 | 15.7779 | 126.6490 | 0.0191 | 0.0061 |
| 2024_09_20 22:00 | 3241186 | 3 | 15.2256 | 14.7596 | -117.3184 | 6.0466 | 112.7305 | 0.0100 | 0.0152 |
| 2024_09_20 22:00 | 3223751 | 4 | 18.3078 | 16.5703 | -115.3396 | 16.5986 | 136.1566 | 0.0132 | 0.0023 |
| 2024_09_20 22:00 | 3210650 | 5 | 18.3586 | 6.5550 | -114.5652 | 11.4086 | 113.0241 | 0.0148 | 0.0059 |
| 2024_09_20 22:00 | 3241816 | 6 | 5.2875 | 16.7966 | -114.9674 | 18.4762 | 187.4862 | 0.0147 | 0.0192 |
| 2024_09_20 22:00 | 3256292 | 7 | 14.4052 | 5.0074 | -114.9053 | 4.5213 | 34.7327 | 0.0030 | 0.0023 |
| 2024_09_20 22:00 | 3224296 | 8 | 16.4277 | 5.9477 | -114.6349 | 4.5930 | 55.3876 | 0.0094 | 0.0124 |
| 2024_09_20 22:00 | 3236109 | 9 | 12.4467 | 6.7542 | -117.7167 | 3.6124 | 34.2087 | 0.0200 | 0.0119 |
| 2024_09_20 22:00 | 3261494 | 10 | 13.5853 | 9.5315 | -115.8800 | 3.2367 | 55.4372 | 0.0082 | 0.0089 |
| 2024_09_20 22:00 | 3213197 | 11 | 10.1407 | 19.2623 | -115.7757 | 4.5145 | 48.9678 | 0.0141 | 0.0150 |
| 2024_09_20 22:00 | 3260115 | 12 | 19.9209 | 17.6183 | -115.4312 | 4.4504 | 33.0736 | 0.0044 | 0.0133 |
| 2024_09_20 22:00 | 3229314 | 13 | 16.6029 | 12.3842 | -114.8725 | 4.2626 | 23.0285 | 0.0075 | 0.0143 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412736_C661A2BB | 152650 | 928 | -95.3 | 152650 | 691 | -102.5 | 152650 | 235 | -106.0 | 152650 | 764 |
| MR_1774412736_33F32E35 | 152650 | 928 | -98.3 | 152650 | 691 | -101.3 | 152650 | 235 | -103.7 | 152650 | 764 |
| MR_1774412736_3B687428 | 152650 | 928 | -97.0 | 152650 | 691 | -101.1 | 152650 | 235 | -106.3 | 152650 | 764 |
| MR_1774412736_A090D9B7 | 152650 | 928 | -95.5 | 152650 | 691 | -102.7 | 152650 | 235 | -104.2 | 152650 | 764 |
| MR_1774412736_3AEA9174 | 152650 | 928 | -97.0 | 152650 | 691 | -102.6 | 152650 | 235 | -102.5 | 152650 | 764 |
| MR_1774412736_69D6D941 | 504990 | 639 | -93.3 | 504990 | 603 | -89.3 | 504990 | 26 | -96.9 | 504990 | 320 |
| MR_1774412736_5FACFA5C | 152650 | 928 | -95.0 | 152650 | 691 | -103.9 | 152650 | 235 | -103.2 | 152650 | 764 |
| MR_1774412736_E14E0773 | 504990 | 639 | -93.7 | 504990 | 603 | -90.5 | 504990 | 26 | -96.6 | 504990 | 320 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1232: `cdecdc75-b2f...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `cdecdc75-b2fb-4143-b0a9-a940ebc66ace` |
| Tag | **single-answer** |
| 정답 | **C18** |
| C18 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1232] topology](images/train_1232.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3271552_4 by 10 degrees
- `C2`: Increase transmission power for 3258918_2
- `C3`: Increase A3 Offset threshold for 3271552_4
- `C4`: Add neighbor relationship between 3217781_3 and 3258918_2
- `C5`: Lift the tilt angle  of 3258918_2 by 5 degrees
- `C6`: Decrease A3 Offset threshold for 3258918_2
- `C7`: Increase transmission power for 3271552_4
- `C8`: Insufficient data; more data is needed for judgment.
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3258918_2
- `C10`: Add neighbor relationship between 3271552_4 and 3258918_2
- `C11`: Adjust the azimuth of 3271552_4 by 50 degrees
- `C12`: Adjust the azimuth of 3258918_2 by 50 degrees
- `C13`: Press down the tilt angle  of 3258918_2 by 5 degrees
- `C14`: Decrease A3 Offset threshold for 3271552_4
- `C15`: Decrease transmission power for 3271552_4
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3271552_4
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3258918_2
- `C18`: Check test server and transmission issues **← 정답**
- `C19`: Lift the tilt angle of 3271552_4 by 10 degrees
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3271552_4
- `C21`: Decrease transmission power for 3258918_2
- `C22`: Increase A3 Offset threshold for 3258918_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.153 | MS1 | 121.4656716232 | 31.1446290244 | 165 | 504990 | -85.24 | 12.59 | 413.96 | 0.09 | 2.38 | 1567 |
| 2024-09-20 22:21:32.515 | MS1 | 121.4656584199 | 31.1446371720 | 165 | 504990 | -90.22 | 12.72 | 511.14 | 0.20 | 2.20 | 1586 |
| 2024-09-20 22:21:33.637 | MS1 | 121.4656679248 | 31.1446234627 | 165 | 504990 | -88.56 | 17.36 | 528.72 | 0.14 | 2.26 | 1590 |
| 2024-09-20 22:21:34.398 | MS1 | 121.4656588618 | 31.1446376878 | 165 | 504990 | -86.75 | 15.76 | 81.74 | 0.14 | 2.20 | 363 |
| 2024-09-20 22:21:35.448 | MS1 | 121.4656628991 | 31.1446260989 | 165 | 504990 | -88.53 | 13.93 | 76.05 | 0.07 | 2.99 | 342 |
| 2024-09-20 22:21:36.858 | MS1 | 121.4656776144 | 31.1446246881 | 165 | 504990 | -85.28 | 17.67 | 72.81 | 0.20 | 2.50 | 325 |
| 2024-09-20 22:21:37.424 | MS1 | 121.4656631194 | 31.1446243801 | 165 | 504990 | -93.91 | 12.81 | 59.19 | 0.05 | 2.17 | 450 |
| 2024-09-20 22:21:38.303 | MS1 | 121.4656711557 | 31.1446348153 | 165 | 504990 | -93.47 | 7.24 | 48.98 | 0.15 | 2.04 | 409 |
| 2024-09-20 22:21:39.610 | MS1 | 121.4656671554 | 31.1446230115 | 165 | 504990 | -90.51 | 11.92 | 82.67 | 0.19 | 2.25 | 393 |
| 2024-09-20 22:21:40.368 | MS1 | 121.4656766791 | 31.1446200717 | 165 | 504990 | -90.73 | 8.93 | 412.31 | 0.03 | 2.07 | 1580 |
| 2024-09-20 22:21:41.535 | MS1 | 121.4656590080 | 31.1446286643 | 165 | 504990 | -92.25 | 12.51 | 516.27 | 0.09 | 2.44 | 1582 |
| 2024-09-20 22:21:42.686 | MS1 | 121.4656659787 | 31.1446184707 | 165 | 504990 | -92.63 | 7.69 | 421.73 | 0.01 | 2.10 | 1561 |

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
| 3217781 | 3 | 121.4709934782 | 31.1552284138 | 87 | 11 | 6 | 44.7 | TDD | 757 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3217949 | 1 | 121.4683353715 | 31.1519734007 | 148 | 7 | 2 | 32.5 | TDD | 835 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3258918 | 2 | 121.4658346477 | 31.1513789528 | 92 | 3 | 2 | 22.8 | TDD | 108 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3271552 | 4 | 121.4694247957 | 31.1481989494 | 5 | 11 | 11 | 48.7 | TDD | 165 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |

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
| 2024-09-20 22:21:30.996 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.016 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.148 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.148 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.841 | NREventA3 | measId:2;ServCellPCI:364;Se... |
| 2024-09-20 22:21:38.081 | NRHandoverAttempt | SourcePCI:364;SourceNR-ARFC... |
| 2024-09-20 22:21:38.119 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.133 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.280 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.280 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3217949 | 1 | 18.9705 | 19.1346 | -117.8258 | 19.7766 | 85.1596 | 0.0002 | 0.0079 |
| 2024_09_20 22:00 | 3258918 | 2 | 7.8361 | 9.8478 | -114.8433 | 17.6330 | 147.8855 | 0.0173 | 0.0011 |
| 2024_09_20 22:00 | 3217781 | 3 | 5.4973 | 6.1928 | -115.0618 | 17.9788 | 191.2346 | 0.0189 | 0.0078 |
| 2024_09_20 22:00 | 3271552 | 4 | 16.9089 | 17.1484 | -115.0052 | 10.4241 | 80.3580 | 0.0127 | 0.0025 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415251_6C806489 | 504990 | 165 | -86.1 | 504990 | 108 | -96.6 | 504990 | 757 | -96.8 | 504990 | 835 |
| MR_1774415251_5D32B3F7 | 504990 | 165 | -88.7 | 504990 | 108 | -92.8 | 504990 | 757 | -94.6 | 504990 | 835 |
| MR_1774415251_60D6694C | 504990 | 165 | -85.6 | 504990 | 108 | -94.4 | 504990 | 757 | -96.0 | 504990 | 835 |
| MR_1774415251_84A26263 | 504990 | 165 | -87.2 | 504990 | 108 | -93.1 | 504990 | 757 | -96.9 | 504990 | 835 |
| MR_1774415251_A70EDBC1 | 504990 | 165 | -85.6 | 504990 | 108 | -93.5 | 504990 | 757 | -96.2 | 504990 | 835 |
| MR_1774415251_7D6E5766 | 504990 | 165 | -85.4 | 504990 | 108 | -93.4 | 504990 | 757 | -93.7 | 504990 | 835 |
| MR_1774415251_937FD207 | 504990 | 165 | -85.7 | 504990 | 108 | -94.6 | 504990 | 757 | -93.1 | 504990 | 835 |
| MR_1774415251_1F7EEC9B | 504990 | 165 | -84.9 | 504990 | 108 | -94.2 | 504990 | 757 | -96.5 | 504990 | 835 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1233: `ebfda965-3b9...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `ebfda965-3b91-4b92-9a79-59fa91d67377` |
| Tag | **multiple-answer** |
| 정답 | **C7|C11** |
| C7 의미 | Adjust the azimuth of 3257451_2 by 50 degrees |
| C11 의미 | Increase transmission power for 3257451_2 |
| 패턴 분류 | **P4 Coverage (azimuth)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1233] topology](images/train_1233.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3257451_2 and 3263848_1
- `C2`: Decrease A3 Offset threshold for 3263848_1
- `C3`: Insufficient data; more data is needed for judgment.
- `C4`: Check test server and transmission issues
- `C5`: Increase A3 Offset threshold for 3257451_2
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3263848_1
- `C7`: Adjust the azimuth of 3257451_2 by 50 degrees **← 정답**
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3257451_2
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3257451_2
- `C10`: Decrease A3 Offset threshold for 3257451_2
- `C11`: Increase transmission power for 3257451_2 **← 정답**
- `C12`: Press down the tilt angle of 3257451_2 by 3 degrees
- `C13`: Press down the tilt angle  of 3263848_1 by 2 degrees
- `C14`: Adjust the azimuth of 3263848_1 by 14 degrees
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3263848_1
- `C16`: Decrease transmission power for 3257451_2
- `C17`: Lift the tilt angle of 3257451_2 by 3 degrees
- `C18`: Increase A3 Offset threshold for 3263848_1
- `C19`: Decrease transmission power for 3263848_1
- `C20`: Increase transmission power for 3263848_1
- `C21`: Lift the tilt angle  of 3263848_1 by 2 degrees
- `C22`: Add neighbor relationship between 3222450_4 and 3263848_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.393 | MS1 | 121.4656717254 | 31.1446353802 | 787 | 504990 | -88.33 | 15.44 | 447.84 | 0.02 | 2.68 | 1598 |
| 2024-09-20 22:21:32.758 | MS1 | 121.4656602361 | 31.1446230266 | 787 | 504990 | -85.01 | 14.48 | 323.03 | 0.10 | 2.22 | 1594 |
| 2024-09-20 22:21:33.812 | MS1 | 121.4656757888 | 31.1446355378 | 787 | 504990 | -87.50 | 17.70 | 450.02 | 0.18 | 2.84 | 1574 |
| 2024-09-20 22:21:34.429 | MS1 | 121.4656688622 | 31.1446267245 | 787 | 504990 | -101.49 | 0.60 | 69.19 | 0.05 | 1.25 | 1588 |
| 2024-09-20 22:21:35.808 | MS1 | 121.4656775205 | 31.1446364944 | 787 | 504990 | -106.52 | 0.73 | 62.16 | 0.14 | 1.38 | 1568 |
| 2024-09-20 22:21:36.963 | MS1 | 121.4656770068 | 31.1446313778 | 787 | 504990 | -107.31 | 0.60 | 71.63 | 0.04 | 1.05 | 1598 |
| 2024-09-20 22:21:37.244 | MS1 | 121.4656623516 | 31.1446332283 | 787 | 504990 | -107.21 | 0.38 | 66.05 | 0.07 | 1.29 | 1600 |
| 2024-09-20 22:21:38.879 | MS1 | 121.4656734169 | 31.1446236355 | 787 | 504990 | -104.02 | 0.30 | 53.20 | 0.00 | 1.09 | 1563 |
| 2024-09-20 22:21:39.338 | MS1 | 121.4656645884 | 31.1446222747 | 787 | 504990 | -107.16 | 0.79 | 32.60 | 0.06 | 1.37 | 1588 |
| 2024-09-20 22:21:40.775 | MS1 | 121.4656721554 | 31.1446272400 | 787 | 504990 | -86.38 | 16.69 | 410.41 | 0.09 | 2.16 | 1600 |
| 2024-09-20 22:21:41.777 | MS1 | 121.4656779295 | 31.1446251286 | 787 | 504990 | -86.27 | 14.98 | 400.59 | 0.12 | 2.04 | 1595 |
| 2024-09-20 22:21:42.830 | MS1 | 121.4656583119 | 31.1446316117 | 787 | 504990 | -88.74 | 13.44 | 409.44 | 0.00 | 2.58 | 1598 |

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
| 3215513 | 3 | 121.4741174091 | 31.1462820193 | 244 | 13 | 3 | 37.6 | TDD | 196 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3222450 | 4 | 121.4649479833 | 31.1516616504 | 284 | 11 | 12 | 40.7 | TDD | 301 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3257451 | 2 | 121.4686665462 | 31.1553423840 | 119 | 2 | 7 | 18.7 | TDD | 787 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3263848 | 1 | 121.4750965478 | 31.1481678879 | 232 | 0 | 0 | 34.6 | TDD | 18 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |

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
| 2024-09-20 22:21:31.058 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.079 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.193 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.193 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.373 | NREventA2 | measId:1;ServCellPCI:16;Ser... |
| 2024-09-20 22:21:34.484 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3263848 | 1 | 17.5303 | 16.5777 | -114.5516 | 19.2959 | 158.3299 | 0.0128 | 0.0138 |
| 2024_09_20 22:00 | 3257451 | 2 | 7.6227 | 11.1767 | -116.7690 | 9.1372 | 90.7089 | 0.1928 | 0.0038 |
| 2024_09_20 22:00 | 3215513 | 3 | 12.2147 | 7.2164 | -114.7255 | 16.4464 | 199.4085 | 0.0198 | 0.0086 |
| 2024_09_20 22:00 | 3222450 | 4 | 12.4132 | 6.7611 | -116.2972 | 5.7370 | 152.7083 | 0.0156 | 0.0050 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412787_1AA9B4C7 | 504990 | 787 | -102.6 | 504990 | 18 | -109.2 | 504990 | 301 | -117.0 | 504990 | 196 |
| MR_1774412787_492838E1 | 504990 | 787 | -100.2 | 504990 | 18 | -108.3 | 504990 | 301 | -116.7 | 504990 | 196 |
| MR_1774412787_52D4B3DE | 504990 | 787 | -99.6 | 504990 | 18 | -108.2 | 504990 | 301 | -113.3 | 504990 | 196 |
| MR_1774412787_660E65A7 | 504990 | 787 | -100.7 | 504990 | 18 | -109.0 | 504990 | 301 | -113.1 | 504990 | 196 |
| MR_1774412787_5E0FC89C | 504990 | 787 | -101.2 | 504990 | 18 | -108.3 | 504990 | 301 | -116.5 | 504990 | 196 |
| MR_1774412787_834C5069 | 504990 | 787 | -103.2 | 504990 | 18 | -110.1 | 504990 | 301 | -115.0 | 504990 | 196 |
| MR_1774412787_F5DBEA6B | 504990 | 787 | -102.2 | 504990 | 18 | -109.8 | 504990 | 301 | -114.0 | 504990 | 196 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1234: `67c7d130-d64...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `67c7d130-d64a-4ca6-88ad-f1521c5788a7` |
| Tag | **single-answer** |
| 정답 | **C13** |
| C13 의미 | Lift the tilt angle  of 3214079_4 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1234] topology](images/train_1234.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3230219_1
- `C2`: Increase transmission power for 3230219_1
- `C3`: Increase transmission power for 3262530_2
- `C4`: Press down the tilt angle  of 3214079_4 by 10 degrees
- `C5`: Lift the tilt angle of 3230219_1 by 4 degrees
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3262530_2
- `C7`: Decrease A3 Offset threshold for 3230219_1
- `C8`: Increase A3 Offset threshold for 3262530_2
- `C9`: Adjust the azimuth of 3214079_4 by 39 degrees
- `C10`: Add neighbor relationship between 3214079_4 and 3262530_2
- `C11`: Increase A3 Offset threshold for 3230219_1
- `C12`: Check test server and transmission issues
- `C13`: Lift the tilt angle  of 3214079_4 by 10 degrees **← 정답**
- `C14`: Adjust the azimuth of 3230219_1 by 34 degrees
- `C15`: Press down the tilt angle of 3230219_1 by 4 degrees
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3230219_1
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3262530_2
- `C18`: Add neighbor relationship between 3230219_1 and 3262530_2
- `C19`: Decrease transmission power for 3230219_1
- `C20`: Decrease A3 Offset threshold for 3262530_2
- `C21`: Insufficient data; more data is needed for judgment.
- `C22`: Decrease transmission power for 3262530_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.126 | MS1 | 121.4656622006 | 31.1446340728 | 170 | 504990 | -86.05 | 13.27 | 361.70 | 0.19 | 2.72 | 1580 |
| 2024-09-20 22:21:32.402 | MS1 | 121.4656654869 | 31.1446310114 | 170 | 504990 | -86.80 | 16.75 | 363.35 | 0.02 | 2.67 | 1573 |
| 2024-09-20 22:21:33.289 | MS1 | 121.4656671617 | 31.1446300404 | 170 | 504990 | -91.31 | 14.93 | 462.90 | 0.02 | 2.24 | 1585 |
| 2024-09-20 22:21:34.840 | MS1 | 121.4656629270 | 31.1446180540 | 170 | 504990 | -89.78 | 16.29 | 83.54 | 0.10 | 2.33 | 1589 |
| 2024-09-20 22:21:35.375 | MS1 | 121.4656604558 | 31.1446327707 | 170 | 504990 | -90.69 | 17.29 | 51.75 | 0.16 | 2.74 | 1595 |
| 2024-09-20 22:21:36.911 | MS1 | 121.4656673059 | 31.1446312230 | 170 | 504990 | -87.88 | 16.09 | 65.46 | 0.04 | 2.98 | 1600 |
| 2024-09-20 22:21:37.333 | MS1 | 121.4656750456 | 31.1446343656 | 170 | 504990 | -91.59 | 12.27 | 80.68 | 0.05 | 2.75 | 1586 |
| 2024-09-20 22:21:38.396 | MS1 | 121.4656592638 | 31.1446294250 | 170 | 504990 | -92.51 | 12.22 | 63.75 | 0.04 | 2.40 | 1574 |
| 2024-09-20 22:21:39.737 | MS1 | 121.4656771162 | 31.1446318627 | 170 | 504990 | -92.92 | 10.87 | 90.08 | 0.16 | 2.92 | 1587 |
| 2024-09-20 22:21:40.665 | MS1 | 121.4656660112 | 31.1446333648 | 170 | 504990 | -91.02 | 7.22 | 384.87 | 0.19 | 2.39 | 1573 |
| 2024-09-20 22:21:41.395 | MS1 | 121.4656625403 | 31.1446277708 | 170 | 504990 | -90.38 | 8.69 | 408.30 | 0.02 | 2.96 | 1579 |
| 2024-09-20 22:21:42.278 | MS1 | 121.4656777802 | 31.1446329948 | 170 | 504990 | -93.57 | 12.33 | 446.62 | 0.06 | 2.93 | 1574 |

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
| 3214079 | 4 | 121.4727444005 | 31.1537171846 | 340 | 11 | 7 | 23.4 | TDD | 775 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3230219 | 1 | 121.4643526400 | 31.1533377641 | 139 | 3 | 8 | 16.6 | TDD | 170 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3262530 | 2 | 121.4647190682 | 31.1452789679 | 168 | 13 | 7 | 23.0 | TDD | 82 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3276192 | 3 | 121.4735782953 | 31.1457791450 | 268 | 7 | 12 | 26.6 | TDD | 877 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |

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
| 2024-09-20 22:21:30.930 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.945 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.060 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.060 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.806 | NREventA3 | measId:2;ServCellPCI:179;Se... |
| 2024-09-20 22:21:38.046 | NRHandoverAttempt | SourcePCI:179;SourceNR-ARFC... |
| 2024-09-20 22:21:38.095 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.105 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.253 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.253 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3230219 | 1 | 84.5914 | 94.6820 | -115.4546 | 11.2863 | 122.5408 | 0.0116 | 0.0081 |
| 2024_09_20 22:00 | 3262530 | 2 | 14.4179 | 17.1742 | -115.6842 | 6.9561 | 188.5717 | 0.0048 | 0.0199 |
| 2024_09_20 22:00 | 3276192 | 3 | 5.7475 | 16.6782 | -114.7937 | 16.1552 | 183.9396 | 0.0148 | 0.0036 |
| 2024_09_20 22:00 | 3214079 | 4 | 14.2647 | 17.4900 | -115.7195 | 7.4603 | 196.8346 | 0.0132 | 0.0145 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412012_6B63500F | 504990 | 170 | -90.8 | 504990 | 82 | -95.9 | 504990 | 775 | -95.7 | 504990 | 877 |
| MR_1774412012_421D5EE6 | 504990 | 170 | -87.8 | 504990 | 82 | -95.9 | 504990 | 775 | -97.8 | 504990 | 877 |
| MR_1774412012_F52D44C5 | 504990 | 170 | -88.2 | 504990 | 82 | -98.8 | 504990 | 775 | -98.1 | 504990 | 877 |
| MR_1774412012_393FD192 | 504990 | 170 | -90.5 | 504990 | 82 | -95.8 | 504990 | 775 | -97.4 | 504990 | 877 |
| MR_1774412012_7020113F | 504990 | 170 | -89.5 | 504990 | 82 | -98.6 | 504990 | 775 | -97.9 | 504990 | 877 |
| MR_1774412012_63D95400 | 504990 | 170 | -88.5 | 504990 | 82 | -96.2 | 504990 | 775 | -97.3 | 504990 | 877 |
| MR_1774412012_8BA042FB | 504990 | 170 | -89.1 | 504990 | 82 | -98.8 | 504990 | 775 | -97.0 | 504990 | 877 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1235: `23954f46-f25...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `23954f46-f25e-4b95-86b3-3f39e14ea077` |
| Tag | **multiple-answer** |
| 정답 | **C17|C19** |
| C17 의미 | Increase transmission power for 3229417_3 |
| C19 의미 | Adjust the azimuth of 3229417_3 by 50 degrees |
| 패턴 분류 | **P4 Coverage (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1235] topology](images/train_1235.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3249072_2
- `C2`: Lift the tilt angle of 3229417_3 by 10 degrees
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3229417_3
- `C4`: Decrease A3 Offset threshold for 3249072_2
- `C5`: Increase A3 Offset threshold for 3229417_3
- `C6`: Press down the tilt angle of 3229417_3 by 10 degrees
- `C7`: Add neighbor relationship between 3267322_1 and 3249072_2
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3249072_2
- `C9`: Insufficient data; more data is needed for judgment.
- `C10`: Adjust the azimuth of 3249072_2 by 19 degrees
- `C11`: Increase transmission power for 3249072_2
- `C12`: Check test server and transmission issues
- `C13`: Decrease A3 Offset threshold for 3229417_3
- `C14`: Press down the tilt angle  of 3249072_2 by 4 degrees
- `C15`: Add neighbor relationship between 3229417_3 and 3249072_2
- `C16`: Decrease transmission power for 3229417_3
- `C17`: Increase transmission power for 3229417_3 **← 정답**
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3249072_2
- `C19`: Adjust the azimuth of 3229417_3 by 50 degrees **← 정답**
- `C20`: Lift the tilt angle  of 3249072_2 by 4 degrees
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3229417_3
- `C22`: Decrease transmission power for 3249072_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.528 | MS1 | 121.4656673983 | 31.1446320789 | 531 | 504990 | -85.08 | 12.99 | 325.07 | 0.10 | 2.10 | 1573 |
| 2024-09-20 22:21:32.506 | MS1 | 121.4656669257 | 31.1446228700 | 531 | 504990 | -91.96 | 17.19 | 418.84 | 0.10 | 2.35 | 1591 |
| 2024-09-20 22:21:33.270 | MS1 | 121.4656684363 | 31.1446229577 | 531 | 504990 | -87.24 | 12.62 | 402.39 | 0.04 | 2.81 | 1561 |
| 2024-09-20 22:21:34.244 | MS1 | 121.4656676544 | 31.1446202523 | 531 | 504990 | -105.69 | 1.29 | 24.76 | 0.04 | 1.23 | 1592 |
| 2024-09-20 22:21:35.652 | MS1 | 121.4656721535 | 31.1446210712 | 531 | 504990 | -100.49 | 0.24 | 37.76 | 0.13 | 1.50 | 1573 |
| 2024-09-20 22:21:36.282 | MS1 | 121.4656612330 | 31.1446229725 | 531 | 504990 | -107.13 | 1.88 | 38.29 | 0.01 | 1.31 | 1589 |
| 2024-09-20 22:21:37.287 | MS1 | 121.4656581213 | 31.1446308706 | 531 | 504990 | -101.52 | 1.29 | 31.58 | 0.08 | 1.26 | 1595 |
| 2024-09-20 22:21:38.662 | MS1 | 121.4656779050 | 31.1446379859 | 531 | 504990 | -103.22 | 1.61 | 22.83 | 0.16 | 1.20 | 1574 |
| 2024-09-20 22:21:39.191 | MS1 | 121.4656741219 | 31.1446361374 | 531 | 504990 | -103.58 | 0.44 | 41.79 | 0.11 | 1.15 | 1571 |
| 2024-09-20 22:21:40.799 | MS1 | 121.4656731750 | 31.1446188541 | 531 | 504990 | -93.11 | 12.77 | 449.68 | 0.03 | 2.38 | 1599 |
| 2024-09-20 22:21:41.441 | MS1 | 121.4656778034 | 31.1446377771 | 531 | 504990 | -87.11 | 17.56 | 376.13 | 0.02 | 2.85 | 1572 |
| 2024-09-20 22:21:42.433 | MS1 | 121.4656733364 | 31.1446336541 | 531 | 504990 | -86.76 | 16.49 | 400.65 | 0.16 | 2.91 | 1589 |

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
| 3229417 | 3 | 121.4640708202 | 31.1455304057 | 62 | 13 | 3 | 37.7 | TDD | 531 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3249072 | 2 | 121.4703290059 | 31.1458595542 | 272 | 2 | 10 | 16.8 | TDD | 231 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3266283 | 4 | 121.4738995865 | 31.1501561629 | 233 | 1 | 5 | 26.2 | TDD | 895 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3267322 | 1 | 121.4759440814 | 31.1535859950 | 46 | 11 | 4 | 32.2 | TDD | 904 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |

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
| 2024-09-20 22:21:30.959 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.978 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.082 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.082 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.320 | NREventA2 | measId:1;ServCellPCI:628;Se... |
| 2024-09-20 22:21:34.431 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3267322 | 1 | 19.5776 | 12.0933 | -115.7993 | 17.0034 | 153.0155 | 0.0033 | 0.0072 |
| 2024_09_20 22:00 | 3249072 | 2 | 17.5094 | 5.7191 | -116.0694 | 13.5671 | 129.8418 | 0.0188 | 0.0048 |
| 2024_09_20 22:00 | 3229417 | 3 | 16.5121 | 6.5043 | -114.1837 | 17.5657 | 183.7681 | 0.1148 | 0.0071 |
| 2024_09_20 22:00 | 3266283 | 4 | 5.8017 | 13.9960 | -115.6260 | 17.2346 | 159.3143 | 0.0011 | 0.0195 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414001_49BC7A1C | 504990 | 531 | -103.9 | 504990 | 231 | -110.0 | 504990 | 904 | -115.1 | 504990 | 895 |
| MR_1774414001_E1E3BF67 | 504990 | 531 | -105.1 | 504990 | 231 | -109.8 | 504990 | 904 | -116.1 | 504990 | 895 |
| MR_1774414001_9A39BC3C | 504990 | 531 | -104.8 | 504990 | 231 | -110.9 | 504990 | 904 | -114.2 | 504990 | 895 |
| MR_1774414001_340844F0 | 504990 | 531 | -106.1 | 504990 | 231 | -110.3 | 504990 | 904 | -113.8 | 504990 | 895 |
| MR_1774414001_AF1A648F | 504990 | 531 | -106.9 | 504990 | 231 | -111.0 | 504990 | 904 | -114.5 | 504990 | 895 |
| MR_1774414001_805FB225 | 504990 | 531 | -107.7 | 504990 | 231 | -113.7 | 504990 | 904 | -116.3 | 504990 | 895 |
| MR_1774414001_EF91D024 | 504990 | 531 | -107.4 | 504990 | 231 | -110.1 | 504990 | 904 | -116.8 | 504990 | 895 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1236: `3866ca85-530...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `3866ca85-530e-49cf-8cc8-c31363b62ad4` |
| Tag | **single-answer** |
| 정답 | **C17** |
| C17 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1236] topology](images/train_1236.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle  of 3213942_4 by 10 degrees
- `C2`: Increase transmission power for 3213087_2
- `C3`: Decrease transmission power for 3213087_2
- `C4`: Lift the tilt angle of 3213087_2 by 10 degrees
- `C5`: Increase transmission power for 3213942_4
- `C6`: Press down the tilt angle  of 3213942_4 by 10 degrees
- `C7`: Decrease A3 Offset threshold for 3213942_4
- `C8`: Decrease transmission power for 3213942_4
- `C9`: Add neighbor relationship between 3218688_3 and 3213942_4
- `C10`: Decrease A3 Offset threshold for 3213087_2
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3213942_4
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3213087_2
- `C13`: Check test server and transmission issues
- `C14`: Adjust the azimuth of 3213942_4 by 50 degrees
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3213087_2
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3213942_4
- `C17`: Insufficient data; more data is needed for judgment. **← 정답**
- `C18`: Press down the tilt angle of 3213087_2 by 10 degrees
- `C19`: Adjust the azimuth of 3213087_2 by 50 degrees
- `C20`: Add neighbor relationship between 3213087_2 and 3213942_4
- `C21`: Increase A3 Offset threshold for 3213942_4
- `C22`: Increase A3 Offset threshold for 3213087_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.448 | MS1 | 121.4656664791 | 31.1446207562 | 68 | 504990 | -91.77 | 12.71 | 347.03 | 0.19 | 2.63 | 1593 |
| 2024-09-20 22:21:32.786 | MS1 | 121.4656632925 | 31.1446255392 | 68 | 504990 | -86.06 | 14.63 | 538.17 | 0.01 | 2.58 | 1591 |
| 2024-09-20 22:21:33.677 | MS1 | 121.4656656041 | 31.1446337946 | 68 | 504990 | -86.87 | 15.29 | 489.85 | 0.11 | 2.63 | 1564 |
| 2024-09-20 22:21:34.676 | MS1 | 121.4656698272 | 31.1446241442 | 68 | 504990 | -85.76 | 13.11 | 84.75 | 0.01 | 2.09 | 1569 |
| 2024-09-20 22:21:35.257 | MS1 | 121.4656687089 | 31.1446212698 | 68 | 504990 | -88.57 | 12.14 | 69.42 | 0.07 | 2.06 | 1586 |
| 2024-09-20 22:21:36.414 | MS1 | 121.4656761724 | 31.1446231778 | 68 | 504990 | -86.24 | 14.08 | 74.30 | 0.14 | 2.36 | 1562 |
| 2024-09-20 22:21:37.108 | MS1 | 121.4656679564 | 31.1446285244 | 68 | 504990 | -92.64 | 8.33 | 96.35 | 0.11 | 2.48 | 1586 |
| 2024-09-20 22:21:38.691 | MS1 | 121.4656774338 | 31.1446341377 | 68 | 504990 | -90.51 | 9.45 | 88.17 | 0.07 | 2.03 | 1594 |
| 2024-09-20 22:21:39.168 | MS1 | 121.4656621339 | 31.1446263517 | 68 | 504990 | -90.93 | 10.87 | 89.49 | 0.01 | 2.27 | 1594 |
| 2024-09-20 22:21:40.938 | MS1 | 121.4656630130 | 31.1446275065 | 68 | 504990 | -90.54 | 9.91 | 426.29 | 0.17 | 2.90 | 1593 |
| 2024-09-20 22:21:41.416 | MS1 | 121.4656770408 | 31.1446374069 | 68 | 504990 | -90.16 | 9.98 | 311.32 | 0.08 | 2.97 | 1574 |
| 2024-09-20 22:21:42.556 | MS1 | 121.4656735041 | 31.1446217230 | 68 | 504990 | -89.83 | 8.65 | 356.53 | 0.13 | 2.23 | 1588 |

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
| 3213087 | 2 | 121.4682164667 | 31.1447833189 | 141 | 9 | 5 | 43.9 | TDD | 68 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3213942 | 4 | 121.4739668047 | 31.1503444045 | 14 | 10 | 1 | 48.3 | TDD | 295 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3218688 | 3 | 121.4702673977 | 31.1477694624 | 169 | 13 | 10 | 40.4 | TDD | 366 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3234862 | 1 | 121.4648516600 | 31.1501945445 | 45 | 12 | 5 | 37.5 | TDD | 816 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |

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
| 2024-09-20 22:21:31.276 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.298 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.424 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.424 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.135 | NREventA3 | measId:2;ServCellPCI:149;Se... |
| 2024-09-20 22:21:38.375 | NRHandoverAttempt | SourcePCI:149;SourceNR-ARFC... |
| 2024-09-20 22:21:38.425 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.438 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.563 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.563 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3234862 | 1 | 80.5643 | 94.2553 | -116.3080 | 14.0609 | 113.3572 | 0.0189 | 0.0117 |
| 2024_09_19 22:00 | 3213087 | 2 | 84.2740 | 79.4045 | -115.0850 | 9.0044 | 140.8805 | 0.0075 | 0.0022 |
| 2024_09_19 22:00 | 3218688 | 3 | 78.9993 | 89.9651 | -116.9006 | 8.7415 | 87.3053 | 0.0061 | 0.0021 |
| 2024_09_19 22:00 | 3213942 | 4 | 85.3887 | 76.0003 | -117.7118 | 10.7154 | 183.2749 | 0.0005 | 0.0155 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414594_95EC10BD | 504990 | 68 | -86.2 | 504990 | 295 | -89.9 | 504990 | 366 | -98.7 | 504990 | 816 |
| MR_1774414594_AC4397DC | 504990 | 68 | -85.6 | 504990 | 295 | -93.0 | 504990 | 366 | -100.0 | 504990 | 816 |
| MR_1774414594_3600910C | 504990 | 68 | -87.0 | 504990 | 295 | -92.6 | 504990 | 366 | -98.8 | 504990 | 816 |
| MR_1774414594_8C7304DE | 504990 | 68 | -85.8 | 504990 | 295 | -89.2 | 504990 | 366 | -99.3 | 504990 | 816 |
| MR_1774414594_A1B1F09C | 504990 | 68 | -87.2 | 504990 | 295 | -91.4 | 504990 | 366 | -99.4 | 504990 | 816 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1237: `71ac5469-ca1...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `71ac5469-ca1a-401b-a7d5-0596820695ab` |
| Tag | **single-answer** |
| 정답 | **C17** |
| C17 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3278854_2 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1237] topology](images/train_1237.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle  of 3233094_1 by 2 degrees
- `C2`: Increase transmission power for 3278854_2
- `C3`: Add neighbor relationship between 3254093_12 and 3233094_1
- `C4`: Adjust the azimuth of 3233094_1 by 31 degrees
- `C5`: Add neighbor relationship between 3278854_2 and 3233094_1
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3233094_1
- `C7`: Increase A3 Offset threshold for 3233094_1
- `C8`: Insufficient data; more data is needed for judgment.
- `C9`: Increase transmission power for 3233094_1
- `C10`: Decrease transmission power for 3233094_1
- `C11`: Decrease transmission power for 3278854_2
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3278854_2
- `C13`: Decrease A3 Offset threshold for 3278854_2
- `C14`: Press down the tilt angle  of 3233094_1 by 2 degrees
- `C15`: Lift the tilt angle of 3278854_2 by 2 degrees
- `C16`: Decrease A3 Offset threshold for 3233094_1
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3278854_2 **← 정답**
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3233094_1
- `C19`: Adjust the azimuth of 3278854_2 by 41 degrees
- `C20`: Press down the tilt angle of 3278854_2 by 2 degrees
- `C21`: Increase A3 Offset threshold for 3278854_2
- `C22`: Check test server and transmission issues

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.583 | MS1 | 121.4656634327 | 31.1446344935 | 385 | 504990 | -95.62 | 13.92 | 420.19 | 0.15 | 2.44 | 1579 |
| 2024-09-20 22:21:32.178 | MS1 | 121.4656623424 | 31.1446367887 | 193 | 504990 | -95.90 | 11.69 | 416.60 | 0.01 | 2.04 | 1583 |
| 2024-09-20 22:21:33.888 | MS1 | 121.4656691752 | 31.1446365390 | 373 | 504990 | -93.27 | 13.73 | 574.83 | 0.04 | 2.90 | 1570 |
| 2024-09-20 22:21:34.407 | MS1 | 121.4656757126 | 31.1446346824 | 297 | 152650 | -91.85 | 7.71 | 91.89 | 0.12 | 1.96 | 923 |
| 2024-09-20 22:21:35.719 | MS1 | 121.4656624364 | 31.1446267577 | 641 | 152650 | -87.02 | 3.82 | 69.00 | 0.00 | 1.71 | 927 |
| 2024-09-20 22:21:36.398 | MS1 | 121.4656777102 | 31.1446337737 | 848 | 152650 | -91.17 | 4.60 | 62.71 | 0.19 | 1.99 | 990 |
| 2024-09-20 22:21:37.538 | MS1 | 121.4656687890 | 31.1446303679 | 705 | 152650 | -95.36 | 3.33 | 88.70 | 0.04 | 1.78 | 979 |
| 2024-09-20 22:21:38.331 | MS1 | 121.4656679647 | 31.1446228077 | 297 | 152650 | -96.69 | 5.01 | 48.92 | 0.06 | 1.99 | 920 |
| 2024-09-20 22:21:39.368 | MS1 | 121.4656703714 | 31.1446275017 | 641 | 152650 | -93.68 | 4.66 | 66.56 | 0.18 | 1.81 | 956 |
| 2024-09-20 22:21:40.156 | MS1 | 121.4656689807 | 31.1446198378 | 848 | 152650 | -90.24 | 5.43 | 82.88 | 0.06 | 2.36 | 1595 |
| 2024-09-20 22:21:41.837 | MS1 | 121.4656700829 | 31.1446308626 | 705 | 152650 | -94.55 | 3.24 | 61.72 | 0.02 | 2.76 | 1582 |
| 2024-09-20 22:21:42.822 | MS1 | 121.4656673125 | 31.1446315830 | 297 | 152650 | -90.32 | 6.61 | 84.16 | 0.08 | 2.13 | 1579 |

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
| 3210267 | 7 | 121.4736478479 | 31.1536490518 | 168 | 0 | 4 | 14.9 | FDD | 641 | n1 | 152650 | 30M | 4T4R | 26 | 152650 |
| 3224118 | 3 | 121.4641036670 | 31.1489355951 | 194 | 0 | 3 | 4.9 | TDD | 193 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3228065 | 11 | 121.4723205194 | 31.1535674257 | 354 | 1 | 7 | 22.5 | FDD | 14 | n1 | 152650 | 30M | 4T4R | 10 | 152650 |
| 3233094 | 1 | 121.4662652247 | 31.1469605336 | 161 | 0 | 3 | 10.3 | TDD | 896 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3235286 | 10 | 121.4734320658 | 31.1558511302 | 54 | 9 | 12 | 24.9 | FDD | 779 | n1 | 152650 | 30M | 4T4R | 28 | 152650 |
| 3252482 | 13 | 121.4675639882 | 31.1528055290 | 313 | 0 | 2 | 29.5 | FDD | 817 | n1 | 152650 | 30M | 4T4R | 13 | 152650 |
| 3254037 | 9 | 121.4697058468 | 31.1466123078 | 236 | 14 | 12 | 0.2 | FDD | 297 | n1 | 152650 | 30M | 4T4R | 21 | 152650 |
| 3254093 | 12 | 121.4696011307 | 31.1516371466 | 268 | 15 | 10 | 19.2 | FDD | 848 | n1 | 152650 | 30M | 4T4R | 24 | 152650 |
| 3255701 | 8 | 121.4705409331 | 31.1526548493 | 4 | 3 | 6 | 5.8 | FDD | 705 | n1 | 152650 | 30M | 4T4R | 19 | 152650 |
| 3258807 | 4 | 121.4642437502 | 31.1492006134 | 4 | 15 | 12 | 0.7 | TDD | 237 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3261757 | 5 | 121.4755205818 | 31.1448418548 | 15 | 11 | 7 | 25.3 | TDD | 979 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3264949 | 6 | 121.4749279437 | 31.1481772337 | 76 | 2 | 2 | 18.4 | TDD | 373 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3278854 | 2 | 121.4722126219 | 31.1496947687 | 187 | 0 | 2 | 22.8 | TDD | 385 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |

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
| 2024-09-20 22:21:30.837 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.854 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:30.964 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.964 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.686 | NREventA2 | measId:1;ServCellPCI:858;Se... |
| 2024-09-20 22:21:34.832 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.123 | NREventA5 | measId:3;ServCellPCI:858;Se... |
| 2024-09-20 22:21:35.199 | NRHandoverAttempt | SourcePCI:858;SourceNR-ARFC... |
| 2024-09-20 22:21:35.223 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.235 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:35.340 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.340 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3233094 | 1 | 6.4407 | 16.6130 | -114.3051 | 14.3722 | 97.5520 | 0.0192 | 0.0134 |
| 2024_09_20 22:00 | 3278854 | 2 | 14.7452 | 11.9003 | -115.9924 | 7.8901 | 133.5903 | 0.0163 | 0.0173 |
| 2024_09_20 22:00 | 3224118 | 3 | 6.8693 | 14.2064 | -114.5600 | 10.9529 | 176.7875 | 0.0028 | 0.0173 |
| 2024_09_20 22:00 | 3258807 | 4 | 16.5398 | 5.6202 | -115.7836 | 8.8650 | 81.0249 | 0.0100 | 0.0043 |
| 2024_09_20 22:00 | 3261757 | 5 | 5.3378 | 10.9593 | -115.5961 | 5.5192 | 113.1408 | 0.0034 | 0.0168 |
| 2024_09_20 22:00 | 3264949 | 6 | 5.0596 | 17.6675 | -115.3875 | 6.1556 | 177.3171 | 0.0104 | 0.0005 |
| 2024_09_20 22:00 | 3210267 | 7 | 7.3051 | 8.8995 | -116.1766 | 3.0535 | 35.2871 | 0.0061 | 0.0055 |
| 2024_09_20 22:00 | 3255701 | 8 | 13.3529 | 17.6489 | -115.5973 | 4.9332 | 41.8098 | 0.0019 | 0.0021 |
| 2024_09_20 22:00 | 3254037 | 9 | 14.7750 | 13.2712 | -114.2395 | 4.9847 | 45.3778 | 0.0040 | 0.0168 |
| 2024_09_20 22:00 | 3235286 | 10 | 17.9038 | 19.2448 | -114.6566 | 3.7523 | 40.1056 | 0.0003 | 0.0170 |
| 2024_09_20 22:00 | 3228065 | 11 | 11.5991 | 14.8772 | -115.6987 | 4.7839 | 43.4740 | 0.0009 | 0.0002 |
| 2024_09_20 22:00 | 3254093 | 12 | 9.8998 | 7.4592 | -115.6210 | 3.1888 | 48.3305 | 0.0013 | 0.0050 |
| 2024_09_20 22:00 | 3252482 | 13 | 16.5758 | 13.5485 | -115.0209 | 4.8694 | 40.1714 | 0.0111 | 0.0105 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412816_CCB563A2 | 504990 | 373 | -92.3 | 504990 | 896 | -90.7 | 504990 | 979 | -98.5 | 504990 | 237 |
| MR_1774412816_EAEF1E16 | 152650 | 297 | -93.7 | 152650 | 779 | -98.8 | 152650 | 817 | -103.2 | 152650 | 14 |
| MR_1774412816_FEB3B768 | 152650 | 297 | -92.8 | 152650 | 779 | -95.5 | 152650 | 817 | -103.6 | 152650 | 14 |
| MR_1774412816_16CC22B0 | 504990 | 373 | -94.9 | 504990 | 896 | -88.7 | 504990 | 979 | -98.9 | 504990 | 237 |
| MR_1774412816_63C88D17 | 152650 | 297 | -90.1 | 152650 | 779 | -96.4 | 152650 | 817 | -103.4 | 152650 | 14 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1238: `31be4e6f-a02...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `31be4e6f-a025-41b0-9223-db5d6823143a` |
| Tag | **single-answer** |
| 정답 | **C9** |
| C9 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3279894_1 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1238] topology](images/train_1238.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3210761_3
- `C2`: Press down the tilt angle of 3279894_1 by 3 degrees
- `C3`: Add neighbor relationship between 3279894_1 and 3210761_3
- `C4`: Lift the tilt angle  of 3210761_3 by 3 degrees
- `C5`: Check test server and transmission issues
- `C6`: Lift the tilt angle of 3279894_1 by 3 degrees
- `C7`: Adjust the azimuth of 3279894_1 by 20 degrees
- `C8`: Increase transmission power for 3279894_1
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3279894_1 **← 정답**
- `C10`: Decrease transmission power for 3210761_3
- `C11`: Adjust the azimuth of 3210761_3 by 50 degrees
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3210761_3
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3210761_3
- `C14`: Increase A3 Offset threshold for 3210761_3
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3279894_1
- `C16`: Decrease A3 Offset threshold for 3279894_1
- `C17`: Increase transmission power for 3210761_3
- `C18`: Press down the tilt angle  of 3210761_3 by 3 degrees
- `C19`: Decrease transmission power for 3279894_1
- `C20`: Add neighbor relationship between 3238291_2 and 3210761_3
- `C21`: Increase A3 Offset threshold for 3279894_1
- `C22`: Insufficient data; more data is needed for judgment.

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.405 | MS1 | 121.4656604771 | 31.1446200286 | 32 | 504990 | -88.95 | 14.49 | 481.46 | 0.13 | 2.87 | 1577 |
| 2024-09-20 22:21:32.749 | MS1 | 121.4656765686 | 31.1446356706 | 32 | 504990 | -91.71 | 13.57 | 339.15 | 0.18 | 2.60 | 1577 |
| 2024-09-20 22:21:33.653 | MS1 | 121.4656590560 | 31.1446310988 | 32 | 504990 | -87.98 | 12.32 | 476.73 | 0.18 | 2.74 | 1570 |
| 2024-09-20 22:21:34.922 | MS1 | 121.4656583999 | 31.1446183966 | 32 | 504990 | -89.46 | 16.85 | 60.46 | 0.56 | 2.35 | 516 |
| 2024-09-20 22:21:35.872 | MS1 | 121.4656728382 | 31.1446256636 | 32 | 504990 | -86.38 | 14.76 | 80.27 | 0.70 | 2.60 | 597 |
| 2024-09-20 22:21:36.572 | MS1 | 121.4656597285 | 31.1446316724 | 32 | 504990 | -86.10 | 17.95 | 99.23 | 0.59 | 2.21 | 518 |
| 2024-09-20 22:21:37.926 | MS1 | 121.4656723626 | 31.1446366393 | 32 | 504990 | -91.57 | 11.84 | 80.10 | 0.63 | 2.46 | 573 |
| 2024-09-20 22:21:38.939 | MS1 | 121.4656751944 | 31.1446274539 | 32 | 504990 | -91.50 | 7.80 | 63.70 | 0.68 | 2.66 | 501 |
| 2024-09-20 22:21:39.203 | MS1 | 121.4656736719 | 31.1446376216 | 32 | 504990 | -91.75 | 12.69 | 85.07 | 0.53 | 2.12 | 591 |
| 2024-09-20 22:21:40.436 | MS1 | 121.4656709748 | 31.1446324526 | 32 | 504990 | -89.38 | 12.51 | 475.90 | 0.11 | 2.82 | 1573 |
| 2024-09-20 22:21:41.846 | MS1 | 121.4656592555 | 31.1446353327 | 32 | 504990 | -92.23 | 8.59 | 420.63 | 0.09 | 2.73 | 1570 |
| 2024-09-20 22:21:42.648 | MS1 | 121.4656634220 | 31.1446274382 | 32 | 504990 | -91.02 | 12.23 | 309.13 | 0.08 | 2.30 | 1592 |

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
| 3210761 | 3 | 121.4748125193 | 31.1557671101 | 69 | 2 | 4 | 34.6 | TDD | 677 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3238291 | 2 | 121.4731332723 | 31.1440892384 | 248 | 9 | 5 | 28.0 | TDD | 12 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3279894 | 1 | 121.4699199260 | 31.1505172801 | 232 | 2 | 3 | 16.5 | TDD | 32 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3279960 | 4 | 121.4704266748 | 31.1461008987 | 322 | 7 | 4 | 28.5 | TDD | 382 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |

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
| 2024-09-20 22:21:31.480 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.505 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.625 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.625 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.361 | NREventA3 | measId:2;ServCellPCI:951;Se... |
| 2024-09-20 22:21:38.601 | NRHandoverAttempt | SourcePCI:951;SourceNR-ARFC... |
| 2024-09-20 22:21:38.649 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.663 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.766 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.766 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3279894 | 1 | 6.5242 | 11.7473 | -117.3041 | 6.7369 | 151.8654 | 0.0042 | 0.0083 |
| 2024_09_20 22:00 | 3238291 | 2 | 11.8442 | 17.8868 | -117.4243 | 7.1687 | 84.0261 | 0.0181 | 0.0056 |
| 2024_09_20 22:00 | 3210761 | 3 | 12.4144 | 5.2819 | -117.6582 | 12.6373 | 183.3083 | 0.0062 | 0.0096 |
| 2024_09_20 22:00 | 3279960 | 4 | 15.9330 | 15.4303 | -114.5412 | 14.5415 | 96.1783 | 0.0159 | 0.0107 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415472_26E21AC3 | 504990 | 32 | -88.6 | 504990 | 677 | -92.6 | 504990 | 12 | -98.7 | 504990 | 382 |
| MR_1774415472_C1C6F897 | 504990 | 32 | -87.5 | 504990 | 677 | -93.3 | 504990 | 12 | -98.7 | 504990 | 382 |
| MR_1774415472_ADC12D31 | 504990 | 32 | -88.1 | 504990 | 677 | -95.0 | 504990 | 12 | -95.6 | 504990 | 382 |
| MR_1774415472_C5F86746 | 504990 | 32 | -87.5 | 504990 | 677 | -95.5 | 504990 | 12 | -97.7 | 504990 | 382 |
| MR_1774415472_894425F0 | 504990 | 32 | -90.0 | 504990 | 677 | -94.0 | 504990 | 12 | -96.0 | 504990 | 382 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1239: `fc175865-7db...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `fc175865-7dbc-4eed-a8aa-af18e911a31e` |
| Tag | **multiple-answer** |
| 정답 | **C3|C20** |
| C3 의미 | Increase transmission power for 3223126_2 |
| C20 의미 | Adjust the azimuth of 3223126_2 by 50 degrees |
| 패턴 분류 | **P4 Coverage (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1239] topology](images/train_1239.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3223126_2
- `C2`: Adjust the azimuth of 3267467_1 by 4 degrees
- `C3`: Increase transmission power for 3223126_2 **← 정답**
- `C4`: Decrease A3 Offset threshold for 3267467_1
- `C5`: Decrease A3 Offset threshold for 3223126_2
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3267467_1
- `C7`: Increase transmission power for 3267467_1
- `C8`: Add neighbor relationship between 3218745_4 and 3267467_1
- `C9`: Lift the tilt angle of 3223126_2 by 10 degrees
- `C10`: Decrease transmission power for 3267467_1
- `C11`: Lift the tilt angle  of 3267467_1 by 1 degrees
- `C12`: Check test server and transmission issues
- `C13`: Decrease transmission power for 3223126_2
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3267467_1
- `C15`: Press down the tilt angle  of 3267467_1 by 1 degrees
- `C16`: Insufficient data; more data is needed for judgment.
- `C17`: Increase A3 Offset threshold for 3223126_2
- `C18`: Increase A3 Offset threshold for 3267467_1
- `C19`: Add neighbor relationship between 3223126_2 and 3267467_1
- `C20`: Adjust the azimuth of 3223126_2 by 50 degrees **← 정답**
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3223126_2
- `C22`: Press down the tilt angle of 3223126_2 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.214 | MS1 | 121.4656746553 | 31.1446251406 | 306 | 504990 | -94.82 | 15.90 | 350.57 | 0.04 | 2.36 | 1576 |
| 2024-09-20 22:21:32.509 | MS1 | 121.4656732106 | 31.1446227059 | 306 | 504990 | -86.36 | 14.31 | 496.91 | 0.06 | 2.06 | 1600 |
| 2024-09-20 22:21:33.189 | MS1 | 121.4656687566 | 31.1446358639 | 306 | 504990 | -87.81 | 16.22 | 457.13 | 0.11 | 2.55 | 1560 |
| 2024-09-20 22:21:34.319 | MS1 | 121.4656691974 | 31.1446198500 | 306 | 504990 | -102.09 | -1.33 | 34.43 | 0.12 | 1.13 | 1562 |
| 2024-09-20 22:21:35.604 | MS1 | 121.4656761678 | 31.1446366721 | 306 | 504990 | -108.65 | 1.51 | 47.53 | 0.13 | 1.04 | 1583 |
| 2024-09-20 22:21:36.719 | MS1 | 121.4656671842 | 31.1446280758 | 306 | 504990 | -104.43 | 1.83 | 61.07 | 0.18 | 1.50 | 1562 |
| 2024-09-20 22:21:37.379 | MS1 | 121.4656643440 | 31.1446217002 | 306 | 504990 | -102.50 | -1.07 | 64.08 | 0.10 | 1.37 | 1570 |
| 2024-09-20 22:21:38.737 | MS1 | 121.4656770253 | 31.1446306535 | 306 | 504990 | -109.92 | -1.83 | 82.49 | 0.01 | 1.43 | 1568 |
| 2024-09-20 22:21:39.968 | MS1 | 121.4656767267 | 31.1446263392 | 306 | 504990 | -103.43 | -1.69 | 67.48 | 0.04 | 1.18 | 1581 |
| 2024-09-20 22:21:40.210 | MS1 | 121.4656654473 | 31.1446296826 | 306 | 504990 | -89.54 | 16.10 | 367.42 | 0.08 | 2.06 | 1579 |
| 2024-09-20 22:21:41.110 | MS1 | 121.4656772574 | 31.1446223943 | 306 | 504990 | -89.15 | 17.90 | 323.37 | 0.01 | 2.72 | 1583 |
| 2024-09-20 22:21:42.463 | MS1 | 121.4656675596 | 31.1446346839 | 306 | 504990 | -89.52 | 16.45 | 487.48 | 0.10 | 2.78 | 1568 |

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
| 3218745 | 4 | 121.4689231311 | 31.1474717963 | 83 | 11 | 12 | 45.1 | TDD | 126 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3223126 | 2 | 121.4663692007 | 31.1480443778 | 249 | 10 | 8 | 31.1 | TDD | 306 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3267467 | 1 | 121.4758572658 | 31.1552528226 | 223 | 0 | 1 | 32.5 | TDD | 968 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3272538 | 3 | 121.4682957224 | 31.1526097992 | 2 | 7 | 12 | 43.1 | TDD | 933 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:30.784 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.799 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:30.929 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.929 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.165 | NREventA2 | measId:1;ServCellPCI:564;Se... |
| 2024-09-20 22:21:34.315 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3267467 | 1 | 13.8996 | 12.5507 | -116.8962 | 14.1612 | 96.4852 | 0.0199 | 0.0075 |
| 2024_09_20 22:00 | 3223126 | 2 | 6.1488 | 8.7390 | -116.6028 | 10.5515 | 117.7867 | 0.1041 | 0.0036 |
| 2024_09_20 22:00 | 3272538 | 3 | 8.2450 | 7.9544 | -115.3676 | 17.8114 | 116.6322 | 0.0052 | 0.0150 |
| 2024_09_20 22:00 | 3218745 | 4 | 12.2893 | 18.8876 | -114.4891 | 18.0001 | 102.4509 | 0.0053 | 0.0180 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413540_9C8B78FE | 504990 | 306 | -101.2 | 504990 | 968 | -107.1 | 504990 | 126 | -111.9 | 504990 | 933 |
| MR_1774413540_E02DD328 | 504990 | 306 | -100.3 | 504990 | 968 | -103.8 | 504990 | 126 | -110.1 | 504990 | 933 |
| MR_1774413540_7F9BF287 | 504990 | 306 | -103.5 | 504990 | 968 | -106.6 | 504990 | 126 | -111.6 | 504990 | 933 |
| MR_1774413540_36F513F5 | 504990 | 306 | -101.5 | 504990 | 968 | -104.4 | 504990 | 126 | -112.3 | 504990 | 933 |
| MR_1774413540_2606E2C2 | 504990 | 306 | -101.8 | 504990 | 968 | -103.3 | 504990 | 126 | -109.0 | 504990 | 933 |

> *... 2개 열 생략 (전체 14열)*

---
