# Track A 문제 분석 — test[490]~test[499]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/test.json`
> 범위: test[490] ~ test[499] (10개)

## 목차

1. [문제 490: `d665ee22-b32...`](#490) — single-answer
2. [문제 491: `c29d8867-ce8...`](#491) — single-answer
3. [문제 492: `d177a511-d4d...`](#492) — single-answer
4. [문제 493: `c4968703-ff2...`](#493) — multiple-answer
5. [문제 494: `20246447-016...`](#494) — multiple-answer
6. [문제 495: `0d0eb9a9-641...`](#495) — single-answer
7. [문제 496: `a43ccc33-002...`](#496) — single-answer
8. [문제 497: `4797741d-169...`](#497) — single-answer
9. [문제 498: `2c1973e2-300...`](#498) — single-answer
10. [문제 499: `f95c5233-bd9...`](#499) — multiple-answer

---

### 문제 490: `d665ee22-b32...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `d665ee22-b321-4006-b16d-2536082a5501` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[490] topology](images/test_0490.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Check test server and transmission issues
- `C2`: Add neighbor relationship between 3225456_5 and 3274972_1
- `C3`: Press down the tilt angle  of 3274972_1 by 2 degrees
- `C4`: Decrease transmission power for 3274972_1
- `C5`: Insufficient data; more data is needed for judgment.
- `C6`: Increase A3 Offset threshold for 3225456_5
- `C7`: Lift the tilt angle  of 3274972_1 by 2 degrees
- `C8`: Add neighbor relationship between 3223262_11 and 3274972_1
- `C9`: Increase transmission power for 3225456_5
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3274972_1
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3225456_5
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3225456_5
- `C13`: Increase transmission power for 3274972_1
- `C14`: Press down the tilt angle of 3225456_5 by 2 degrees
- `C15`: Adjust the azimuth of 3225456_5 by 49 degrees
- `C16`: Adjust the azimuth of 3274972_1 by 19 degrees
- `C17`: Increase A3 Offset threshold for 3274972_1
- `C18`: Decrease transmission power for 3225456_5
- `C19`: Lift the tilt angle of 3225456_5 by 2 degrees
- `C20`: Decrease A3 Offset threshold for 3225456_5
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3274972_1
- `C22`: Decrease A3 Offset threshold for 3274972_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.958 | MS1 | 121.4656699734 | 31.1446196283 | 499 | 504990 | -93.95 | 10.70 | 309.42 | 0.13 | 2.25 | 1600 |
| 2024-09-20 22:21:32.813 | MS1 | 121.4656769777 | 31.1446315582 | 144 | 504990 | -93.01 | 13.06 | 506.32 | 0.07 | 2.31 | 1579 |
| 2024-09-20 22:21:33.271 | MS1 | 121.4656655024 | 31.1446357384 | 653 | 504990 | -94.95 | 13.59 | 513.78 | 0.16 | 2.22 | 1565 |
| 2024-09-20 22:21:34.696 | MS1 | 121.4656669642 | 31.1446281054 | 134 | 152650 | -90.74 | 3.61 | 81.03 | 0.15 | 1.72 | 921 |
| 2024-09-20 22:21:35.442 | MS1 | 121.4656648632 | 31.1446297947 | 81 | 152650 | -93.41 | 3.31 | 101.29 | 0.14 | 1.82 | 914 |
| 2024-09-20 22:21:36.778 | MS1 | 121.4656730220 | 31.1446324586 | 376 | 152650 | -92.96 | 3.05 | 89.19 | 0.14 | 1.92 | 944 |
| 2024-09-20 22:21:37.340 | MS1 | 121.4656590202 | 31.1446304889 | 937 | 152650 | -95.31 | 6.78 | 63.19 | 0.04 | 1.84 | 935 |
| 2024-09-20 22:21:38.713 | MS1 | 121.4656694850 | 31.1446222909 | 134 | 152650 | -95.28 | 6.57 | 93.10 | 0.12 | 1.56 | 983 |
| 2024-09-20 22:21:39.613 | MS1 | 121.4656660787 | 31.1446227510 | 81 | 152650 | -95.22 | 5.92 | 90.89 | 0.16 | 1.62 | 992 |
| 2024-09-20 22:21:40.331 | MS1 | 121.4656718196 | 31.1446359307 | 376 | 152650 | -92.67 | 6.32 | 58.18 | 0.10 | 2.06 | 1587 |
| 2024-09-20 22:21:41.266 | MS1 | 121.4656740612 | 31.1446269749 | 937 | 152650 | -88.41 | 7.60 | 77.01 | 0.09 | 2.28 | 1563 |
| 2024-09-20 22:21:42.143 | MS1 | 121.4656687846 | 31.1446228971 | 134 | 152650 | -95.68 | 4.36 | 84.75 | 0.18 | 2.75 | 1589 |

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
| 3219068 | 6 | 121.4663582409 | 31.1521325366 | 147 | 3 | 9 | 14.1 | TDD | 884 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3220419 | 10 | 121.4713712820 | 31.1517010067 | 78 | 12 | 9 | 6.0 | FDD | 81 | n1 | 152650 | 30M | 4T4R | 21 | 152650 |
| 3223262 | 11 | 121.4722975420 | 31.1537494058 | 303 | 11 | 5 | 3.3 | FDD | 376 | n1 | 152650 | 30M | 4T4R | 10 | 152650 |
| 3225456 | 5 | 121.4736335647 | 31.1516030510 | 175 | 1 | 4 | 14.7 | TDD | 499 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3248373 | 13 | 121.4746800695 | 31.1548629390 | 199 | 7 | 3 | 5.7 | FDD | 703 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |
| 3251112 | 9 | 121.4670482188 | 31.1471397843 | 171 | 9 | 8 | 14.3 | FDD | 461 | n1 | 152650 | 30M | 4T4R | 18 | 152650 |
| 3262493 | 2 | 121.4673338579 | 31.1543112471 | 71 | 2 | 0 | 14.7 | TDD | 589 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3264484 | 4 | 121.4742620413 | 31.1440836604 | 58 | 10 | 3 | 1.2 | TDD | 144 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3267929 | 12 | 121.4645813996 | 31.1534586421 | 77 | 15 | 3 | 4.1 | FDD | 92 | n1 | 152650 | 30M | 4T4R | 13 | 152650 |
| 3270457 | 7 | 121.4654769940 | 31.1544509680 | 324 | 14 | 1 | 20.7 | FDD | 134 | n1 | 152650 | 30M | 4T4R | 11 | 152650 |
| 3271259 | 8 | 121.4732380216 | 31.1528467775 | 88 | 8 | 11 | 19.8 | FDD | 937 | n1 | 152650 | 30M | 4T4R | 25 | 152650 |
| 3274972 | 1 | 121.4703288716 | 31.1491260351 | 241 | 1 | 6 | 6.7 | TDD | 739 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3275356 | 3 | 121.4725784596 | 31.1445131058 | 124 | 8 | 2 | 1.2 | TDD | 653 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |

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
| 2024-09-20 22:21:31.192 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.216 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.357 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.357 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.015 | NREventA2 | measId:1;ServCellPCI:806;Se... |
| 2024-09-20 22:21:35.126 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.345 | NREventA5 | measId:3;ServCellPCI:806;Se... |
| 2024-09-20 22:21:35.383 | NRHandoverAttempt | SourcePCI:806;SourceNR-ARFC... |
| 2024-09-20 22:21:35.426 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.437 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:35.542 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.542 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3274972 | 1 | 6.9664 | 19.7218 | -117.8495 | 15.2003 | 125.5095 | 0.0129 | 0.0031 |
| 2024_09_20 22:00 | 3262493 | 2 | 10.8119 | 5.3257 | -116.2164 | 15.3386 | 138.2235 | 0.0153 | 0.0199 |
| 2024_09_20 22:00 | 3275356 | 3 | 6.3312 | 6.8721 | -117.2823 | 16.7617 | 159.7354 | 0.0110 | 0.0024 |
| 2024_09_20 22:00 | 3264484 | 4 | 15.6342 | 12.6963 | -114.9200 | 10.2705 | 186.1486 | 0.0175 | 0.0103 |
| 2024_09_20 22:00 | 3225456 | 5 | 19.7162 | 13.1975 | -114.1004 | 8.0912 | 135.1054 | 0.0095 | 0.0116 |
| 2024_09_20 22:00 | 3219068 | 6 | 14.1947 | 16.4625 | -117.3518 | 16.6303 | 119.8410 | 0.0143 | 0.0123 |
| 2024_09_20 22:00 | 3270457 | 7 | 18.8551 | 13.5541 | -115.2661 | 4.5657 | 40.6894 | 0.0196 | 0.0036 |
| 2024_09_20 22:00 | 3271259 | 8 | 18.6597 | 5.5011 | -116.1707 | 3.1317 | 29.8813 | 0.0072 | 0.0136 |
| 2024_09_20 22:00 | 3251112 | 9 | 12.5965 | 11.4624 | -114.1583 | 3.0379 | 50.6080 | 0.0146 | 0.0114 |
| 2024_09_20 22:00 | 3220419 | 10 | 6.4558 | 9.3810 | -115.0038 | 4.9138 | 57.7187 | 0.0045 | 0.0083 |
| 2024_09_20 22:00 | 3223262 | 11 | 12.2600 | 12.1715 | -116.7863 | 3.1468 | 48.8436 | 0.0185 | 0.0132 |
| 2024_09_20 22:00 | 3267929 | 12 | 13.5431 | 11.0478 | -117.2062 | 3.4730 | 30.5607 | 0.0160 | 0.0074 |
| 2024_09_20 22:00 | 3248373 | 13 | 8.8199 | 16.4248 | -117.0563 | 4.0268 | 44.2075 | 0.0147 | 0.0088 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414262_B1851349 | 504990 | 653 | -95.5 | 504990 | 739 | -89.1 | 504990 | 589 | -98.9 | 504990 | 884 |
| MR_1774414262_F736BF9B | 504990 | 653 | -94.4 | 504990 | 739 | -91.2 | 504990 | 589 | -98.9 | 504990 | 884 |
| MR_1774414262_73DD9208 | 152650 | 134 | -91.4 | 152650 | 92 | -95.1 | 152650 | 703 | -101.2 | 152650 | 461 |
| MR_1774414262_8D929D49 | 152650 | 134 | -89.7 | 152650 | 92 | -92.5 | 152650 | 703 | -101.7 | 152650 | 461 |
| MR_1774414262_B4813874 | 504990 | 653 | -95.7 | 504990 | 739 | -91.2 | 504990 | 589 | -98.6 | 504990 | 884 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 491: `c29d8867-ce8...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `c29d8867-ce87-4096-886c-0e3e48f88463` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[491] topology](images/test_0491.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3264292_3 by 8 degrees
- `C2`: Add neighbor relationship between 3226789_1 and 3264292_3
- `C3`: Insufficient data; more data is needed for judgment.
- `C4`: Increase transmission power for 3226789_1
- `C5`: Lift the tilt angle of 3226789_1 by 7 degrees
- `C6`: Add neighbor relationship between 3268006_2 and 3264292_3
- `C7`: Decrease A3 Offset threshold for 3226789_1
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3226789_1
- `C9`: Decrease transmission power for 3264292_3
- `C10`: Increase A3 Offset threshold for 3226789_1
- `C11`: Check test server and transmission issues
- `C12`: Adjust the azimuth of 3226789_1 by 50 degrees
- `C13`: Increase A3 Offset threshold for 3264292_3
- `C14`: Press down the tilt angle of 3226789_1 by 7 degrees
- `C15`: Increase transmission power for 3264292_3
- `C16`: Decrease A3 Offset threshold for 3264292_3
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3264292_3
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3226789_1
- `C19`: Adjust the azimuth of 3264292_3 by 50 degrees
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3264292_3
- `C21`: Lift the tilt angle  of 3264292_3 by 8 degrees
- `C22`: Decrease transmission power for 3226789_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.710 | MS1 | 121.4656662461 | 31.1446330193 | 898 | 504990 | -87.32 | 16.58 | 435.08 | 0.10 | 2.92 | 1598 |
| 2024-09-20 22:21:32.381 | MS1 | 121.4656713296 | 31.1446266593 | 898 | 504990 | -90.52 | 15.64 | 539.13 | 0.11 | 2.49 | 1580 |
| 2024-09-20 22:21:33.182 | MS1 | 121.4656779082 | 31.1446246042 | 898 | 504990 | -90.69 | 14.40 | 335.07 | 0.12 | 2.33 | 1591 |
| 2024-09-20 22:21:34.682 | MS1 | 121.4656638253 | 31.1446333436 | 898 | 504990 | -89.77 | 15.75 | 64.15 | 0.16 | 2.96 | 311 |
| 2024-09-20 22:21:35.118 | MS1 | 121.4656748058 | 31.1446237605 | 898 | 504990 | -86.34 | 13.05 | 42.50 | 0.17 | 2.22 | 415 |
| 2024-09-20 22:21:36.703 | MS1 | 121.4656703960 | 31.1446212185 | 898 | 504990 | -85.07 | 14.90 | 87.72 | 0.16 | 2.80 | 468 |
| 2024-09-20 22:21:37.769 | MS1 | 121.4656631814 | 31.1446295168 | 898 | 504990 | -89.40 | 11.66 | 56.31 | 0.17 | 2.89 | 485 |
| 2024-09-20 22:21:38.102 | MS1 | 121.4656634342 | 31.1446237871 | 898 | 504990 | -93.77 | 10.77 | 85.90 | 0.11 | 2.31 | 425 |
| 2024-09-20 22:21:39.857 | MS1 | 121.4656679831 | 31.1446289253 | 898 | 504990 | -90.69 | 9.50 | 101.60 | 0.12 | 2.04 | 356 |
| 2024-09-20 22:21:40.720 | MS1 | 121.4656588901 | 31.1446354857 | 898 | 504990 | -93.76 | 11.92 | 583.50 | 0.16 | 2.76 | 1578 |
| 2024-09-20 22:21:41.105 | MS1 | 121.4656610028 | 31.1446277156 | 898 | 504990 | -90.71 | 12.03 | 389.46 | 0.01 | 2.24 | 1598 |
| 2024-09-20 22:21:42.395 | MS1 | 121.4656734410 | 31.1446283289 | 898 | 504990 | -92.54 | 9.79 | 354.79 | 0.18 | 2.94 | 1586 |

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
| 3213665 | 4 | 121.4740216805 | 31.1548361172 | 292 | 5 | 6 | 31.9 | TDD | 975 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3226789 | 1 | 121.4690516290 | 31.1544148247 | 100 | 5 | 10 | 49.5 | TDD | 898 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3264292 | 3 | 121.4645733602 | 31.1500828209 | 344 | 4 | 1 | 41.0 | TDD | 319 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3268006 | 2 | 121.4740834311 | 31.1481371597 | 65 | 5 | 10 | 49.0 | TDD | 1004 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

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
| 2024-09-20 22:21:31.172 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.193 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.307 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.307 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.991 | NREventA3 | measId:2;ServCellPCI:365;Se... |
| 2024-09-20 22:21:38.231 | NRHandoverAttempt | SourcePCI:365;SourceNR-ARFC... |
| 2024-09-20 22:21:38.265 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.279 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.395 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.395 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3226789 | 1 | 8.1814 | 5.0147 | -117.9552 | 16.9134 | 185.5025 | 0.0110 | 0.0156 |
| 2024_09_20 22:00 | 3268006 | 2 | 16.6745 | 12.2495 | -116.5546 | 13.0035 | 160.7120 | 0.0078 | 0.0018 |
| 2024_09_20 22:00 | 3264292 | 3 | 19.7430 | 5.8881 | -116.7012 | 6.9408 | 146.9074 | 0.0109 | 0.0066 |
| 2024_09_20 22:00 | 3213665 | 4 | 9.4591 | 16.1962 | -117.3106 | 18.7042 | 122.1190 | 0.0123 | 0.0126 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417018_7CB94543 | 504990 | 898 | -91.7 | 504990 | 319 | -92.6 | 504990 | 1004 | -102.4 | 504990 | 975 |
| MR_1774417018_7FD75E28 | 504990 | 898 | -89.9 | 504990 | 319 | -89.9 | 504990 | 1004 | -103.4 | 504990 | 975 |
| MR_1774417018_1373E0A8 | 504990 | 898 | -89.5 | 504990 | 319 | -90.5 | 504990 | 1004 | -101.1 | 504990 | 975 |
| MR_1774417018_8826E351 | 504990 | 898 | -89.8 | 504990 | 319 | -89.9 | 504990 | 1004 | -100.8 | 504990 | 975 |
| MR_1774417018_7DB4ED7D | 504990 | 898 | -90.5 | 504990 | 319 | -91.3 | 504990 | 1004 | -104.0 | 504990 | 975 |
| MR_1774417018_91CE58B3 | 504990 | 898 | -88.0 | 504990 | 319 | -92.1 | 504990 | 1004 | -104.1 | 504990 | 975 |
| MR_1774417018_BAF24810 | 504990 | 898 | -89.8 | 504990 | 319 | -92.5 | 504990 | 1004 | -101.2 | 504990 | 975 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 492: `d177a511-d4d...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `d177a511-d4d0-4381-affc-8cfca79ff936` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[492] topology](images/test_0492.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3248125_2 by 5 degrees
- `C2`: Adjust the azimuth of 3248125_2 by 2 degrees
- `C3`: Press down the tilt angle  of 3247946_6 by 4 degrees
- `C4`: Check test server and transmission issues
- `C5`: Increase A3 Offset threshold for 3248125_2
- `C6`: Decrease A3 Offset threshold for 3247946_6
- `C7`: Increase A3 Offset threshold for 3247946_6
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3247946_6
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3248125_2
- `C10`: Lift the tilt angle of 3248125_2 by 5 degrees
- `C11`: Decrease transmission power for 3248125_2
- `C12`: Increase transmission power for 3247946_6
- `C13`: Increase transmission power for 3248125_2
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Decrease transmission power for 3247946_6
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3248125_2
- `C17`: Add neighbor relationship between 3248125_2 and 3247946_6
- `C18`: Lift the tilt angle  of 3247946_6 by 4 degrees
- `C19`: Add neighbor relationship between 3213134_7 and 3247946_6
- `C20`: Decrease A3 Offset threshold for 3248125_2
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3247946_6
- `C22`: Adjust the azimuth of 3247946_6 by 18 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.368 | MS1 | 121.4656659031 | 31.1446193971 | 740 | 504990 | -95.01 | 12.16 | 400.48 | 0.17 | 2.40 | 1575 |
| 2024-09-20 22:21:32.133 | MS1 | 121.4656672456 | 31.1446195311 | 371 | 504990 | -94.83 | 10.59 | 438.77 | 0.09 | 2.36 | 1575 |
| 2024-09-20 22:21:33.440 | MS1 | 121.4656665056 | 31.1446305544 | 979 | 504990 | -94.37 | 13.76 | 576.00 | 0.12 | 2.30 | 1576 |
| 2024-09-20 22:21:34.193 | MS1 | 121.4656636044 | 31.1446290789 | 118 | 152650 | -87.47 | 5.65 | 68.97 | 0.07 | 1.87 | 917 |
| 2024-09-20 22:21:35.430 | MS1 | 121.4656717342 | 31.1446316806 | 478 | 152650 | -87.74 | 6.90 | 61.02 | 0.19 | 1.69 | 962 |
| 2024-09-20 22:21:36.201 | MS1 | 121.4656597824 | 31.1446184892 | 931 | 152650 | -92.31 | 2.02 | 96.80 | 0.05 | 1.74 | 932 |
| 2024-09-20 22:21:37.124 | MS1 | 121.4656702368 | 31.1446255023 | 7 | 152650 | -91.71 | 4.32 | 61.36 | 0.14 | 1.99 | 934 |
| 2024-09-20 22:21:38.126 | MS1 | 121.4656676877 | 31.1446358709 | 118 | 152650 | -95.46 | 2.20 | 63.39 | 0.18 | 1.92 | 909 |
| 2024-09-20 22:21:39.410 | MS1 | 121.4656747566 | 31.1446235302 | 478 | 152650 | -87.40 | 3.08 | 72.51 | 0.06 | 1.91 | 958 |
| 2024-09-20 22:21:40.775 | MS1 | 121.4656598368 | 31.1446273908 | 931 | 152650 | -95.79 | 5.36 | 88.34 | 0.11 | 2.15 | 1589 |
| 2024-09-20 22:21:41.443 | MS1 | 121.4656692912 | 31.1446357343 | 7 | 152650 | -90.35 | 2.38 | 63.43 | 0.10 | 2.19 | 1594 |
| 2024-09-20 22:21:42.955 | MS1 | 121.4656680690 | 31.1446227996 | 118 | 152650 | -91.37 | 5.30 | 54.67 | 0.04 | 2.51 | 1594 |

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
| 3213134 | 7 | 121.4741897834 | 31.1499609845 | 179 | 14 | 10 | 25.2 | FDD | 931 | n1 | 152650 | 30M | 4T4R | 26 | 152650 |
| 3214362 | 4 | 121.4740027654 | 31.1521097002 | 45 | 2 | 3 | 4.9 | TDD | 371 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3227474 | 12 | 121.4734861985 | 31.1485161724 | 242 | 6 | 4 | 28.6 | FDD | 478 | n1 | 152650 | 30M | 4T4R | 20 | 152650 |
| 3234452 | 5 | 121.4643451669 | 31.1497464501 | 200 | 12 | 5 | 8.4 | TDD | 979 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3235107 | 1 | 121.4719167837 | 31.1477065056 | 287 | 11 | 5 | 29.6 | TDD | 641 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3241576 | 9 | 121.4645864663 | 31.1507779306 | 134 | 8 | 0 | 5.4 | FDD | 109 | n1 | 152650 | 30M | 4T4R | 28 | 152650 |
| 3247692 | 13 | 121.4688217340 | 31.1468506775 | 7 | 3 | 8 | 15.5 | FDD | 287 | n1 | 152650 | 30M | 4T4R | 13 | 152650 |
| 3247945 | 10 | 121.4686229580 | 31.1544217165 | 222 | 7 | 5 | 3.8 | FDD | 118 | n1 | 152650 | 30M | 4T4R | 12 | 152650 |
| 3247946 | 6 | 121.4740119218 | 31.1518499031 | 207 | 3 | 6 | 27.4 | TDD | 502 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3248125 | 2 | 121.4684817791 | 31.1533082528 | 193 | 4 | 1 | 9.4 | TDD | 740 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3250404 | 8 | 121.4725067655 | 31.1528114704 | 239 | 3 | 1 | 5.7 | FDD | 7 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |
| 3259676 | 3 | 121.4689842324 | 31.1502321222 | 251 | 13 | 10 | 9.2 | TDD | 809 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3272369 | 11 | 121.4647873221 | 31.1520521495 | 355 | 3 | 0 | 28.1 | FDD | 694 | n1 | 152650 | 30M | 4T4R | 15 | 152650 |

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
| 2024-09-20 22:21:31.521 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.544 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.682 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.682 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.338 | NREventA2 | measId:1;ServCellPCI:594;Se... |
| 2024-09-20 22:21:35.481 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.699 | NREventA5 | measId:3;ServCellPCI:594;Se... |
| 2024-09-20 22:21:35.740 | NRHandoverAttempt | SourcePCI:594;SourceNR-ARFC... |
| 2024-09-20 22:21:35.787 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.797 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:35.903 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.903 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3235107 | 1 | 17.4037 | 17.0826 | -115.9893 | 5.4071 | 101.1779 | 0.0188 | 0.0005 |
| 2024_09_20 22:00 | 3248125 | 2 | 7.7701 | 13.1549 | -114.1087 | 11.7005 | 154.5792 | 0.0057 | 0.0046 |
| 2024_09_20 22:00 | 3259676 | 3 | 15.4182 | 9.6414 | -115.7162 | 12.4640 | 83.1115 | 0.0154 | 0.0163 |
| 2024_09_20 22:00 | 3214362 | 4 | 6.3664 | 18.1107 | -115.9402 | 18.2063 | 103.0570 | 0.0174 | 0.0021 |
| 2024_09_20 22:00 | 3234452 | 5 | 15.8840 | 7.3811 | -117.6077 | 12.5190 | 141.7112 | 0.0018 | 0.0105 |
| 2024_09_20 22:00 | 3247946 | 6 | 13.3151 | 15.2898 | -115.8020 | 9.7795 | 111.5186 | 0.0096 | 0.0044 |
| 2024_09_20 22:00 | 3213134 | 7 | 5.0435 | 9.4351 | -117.0639 | 3.2252 | 24.4131 | 0.0116 | 0.0120 |
| 2024_09_20 22:00 | 3250404 | 8 | 7.1708 | 16.8220 | -115.3185 | 3.9781 | 22.3513 | 0.0040 | 0.0043 |
| 2024_09_20 22:00 | 3241576 | 9 | 11.6043 | 7.1762 | -115.4508 | 3.9976 | 51.1674 | 0.0163 | 0.0058 |
| 2024_09_20 22:00 | 3247945 | 10 | 19.2561 | 13.6190 | -116.4664 | 4.2304 | 55.7314 | 0.0186 | 0.0124 |
| 2024_09_20 22:00 | 3272369 | 11 | 5.6494 | 17.1725 | -117.2201 | 3.7981 | 35.3788 | 0.0146 | 0.0019 |
| 2024_09_20 22:00 | 3227474 | 12 | 7.6023 | 12.1834 | -114.5001 | 3.1703 | 54.4338 | 0.0048 | 0.0099 |
| 2024_09_20 22:00 | 3247692 | 13 | 7.5533 | 13.7240 | -114.7440 | 3.7517 | 34.4320 | 0.0115 | 0.0039 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414312_D0363C15 | 504990 | 979 | -94.6 | 504990 | 502 | -91.9 | 504990 | 641 | -92.6 | 504990 | 809 |
| MR_1774414312_73B46FF4 | 152650 | 118 | -87.8 | 152650 | 287 | -93.7 | 152650 | 109 | -100.1 | 152650 | 694 |
| MR_1774414312_DBE4B7B0 | 504990 | 979 | -94.0 | 504990 | 502 | -92.3 | 504990 | 641 | -92.0 | 504990 | 809 |
| MR_1774414312_EA57C96E | 152650 | 118 | -87.3 | 152650 | 287 | -91.9 | 152650 | 109 | -99.5 | 152650 | 694 |
| MR_1774414312_4D25ED2B | 152650 | 118 | -86.4 | 152650 | 287 | -92.1 | 152650 | 109 | -97.7 | 152650 | 694 |
| MR_1774414312_6AECB731 | 504990 | 979 | -94.2 | 504990 | 502 | -89.2 | 504990 | 641 | -94.0 | 504990 | 809 |
| MR_1774414312_436A4994 | 504990 | 979 | -94.9 | 504990 | 502 | -92.6 | 504990 | 641 | -95.0 | 504990 | 809 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 493: `c4968703-ff2...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `c4968703-ff24-401d-80f7-2f4ce2486e25` |
| Tag | **multiple-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[493] topology](images/test_0493.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3237221_3
- `C2`: Lift the tilt angle  of 3229947_1 by 3 degrees
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3229947_1
- `C4`: Insufficient data; more data is needed for judgment.
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3237221_3
- `C6`: Add neighbor relationship between 3228526_4 and 3229947_1
- `C7`: Increase A3 Offset threshold for 3229947_1
- `C8`: Press down the tilt angle of 3237221_3 by 10 degrees
- `C9`: Press down the tilt angle  of 3229947_1 by 3 degrees
- `C10`: Decrease transmission power for 3237221_3
- `C11`: Increase transmission power for 3229947_1
- `C12`: Lift the tilt angle of 3237221_3 by 10 degrees
- `C13`: Decrease transmission power for 3229947_1
- `C14`: Add neighbor relationship between 3237221_3 and 3229947_1
- `C15`: Adjust the azimuth of 3229947_1 by 26 degrees
- `C16`: Decrease A3 Offset threshold for 3229947_1
- `C17`: Increase A3 Offset threshold for 3237221_3
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3229947_1
- `C19`: Check test server and transmission issues
- `C20`: Decrease A3 Offset threshold for 3237221_3
- `C21`: Adjust the azimuth of 3237221_3 by 30 degrees
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3237221_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.727 | MS1 | 121.4656697527 | 31.1446202993 | 694 | 504990 | -86.67 | 12.81 | 405.14 | 0.03 | 2.21 | 1590 |
| 2024-09-20 22:21:32.539 | MS1 | 121.4656624622 | 31.1446371382 | 694 | 504990 | -92.34 | 14.77 | 590.61 | 0.03 | 2.05 | 1584 |
| 2024-09-20 22:21:33.854 | MS1 | 121.4656764898 | 31.1446379146 | 694 | 504990 | -91.96 | 12.55 | 482.18 | 0.09 | 2.26 | 1598 |
| 2024-09-20 22:21:34.162 | MS1 | 121.4656768465 | 31.1446364622 | 694 | 504990 | -100.25 | 0.01 | 69.63 | 0.00 | 1.48 | 1573 |
| 2024-09-20 22:21:35.435 | MS1 | 121.4656686822 | 31.1446310375 | 694 | 504990 | -104.38 | 1.73 | 80.49 | 0.19 | 1.29 | 1592 |
| 2024-09-20 22:21:36.709 | MS1 | 121.4656638687 | 31.1446376830 | 694 | 504990 | -108.86 | -0.16 | 16.87 | 0.06 | 1.18 | 1566 |
| 2024-09-20 22:21:37.337 | MS1 | 121.4656629061 | 31.1446197813 | 694 | 504990 | -109.51 | 1.40 | 27.58 | 0.15 | 1.17 | 1583 |
| 2024-09-20 22:21:38.319 | MS1 | 121.4656734104 | 31.1446180356 | 694 | 504990 | -109.40 | 0.02 | 23.48 | 0.15 | 1.38 | 1576 |
| 2024-09-20 22:21:39.741 | MS1 | 121.4656775504 | 31.1446292678 | 694 | 504990 | -109.33 | 1.77 | 37.70 | 0.08 | 1.14 | 1572 |
| 2024-09-20 22:21:40.728 | MS1 | 121.4656778840 | 31.1446252656 | 694 | 504990 | -86.39 | 15.18 | 562.48 | 0.07 | 2.66 | 1577 |
| 2024-09-20 22:21:41.523 | MS1 | 121.4656763677 | 31.1446371456 | 694 | 504990 | -91.29 | 13.53 | 453.40 | 0.10 | 2.82 | 1590 |
| 2024-09-20 22:21:42.122 | MS1 | 121.4656760731 | 31.1446182524 | 694 | 504990 | -87.98 | 13.72 | 422.74 | 0.13 | 2.93 | 1570 |

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
| 3228526 | 4 | 121.4695475608 | 31.1471959734 | 17 | 15 | 9 | 38.8 | TDD | 399 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3229947 | 1 | 121.4652052975 | 31.1553471666 | 152 | 1 | 10 | 36.1 | TDD | 840 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3237221 | 3 | 121.4743376455 | 31.1470836465 | 282 | 8 | 10 | 30.3 | TDD | 694 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3261804 | 2 | 121.4719941036 | 31.1462689318 | 316 | 8 | 6 | 39.9 | TDD | 370 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:31.472 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.493 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.627 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.627 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.796 | NREventA2 | measId:1;ServCellPCI:860;Se... |
| 2024-09-20 22:21:34.945 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3229947 | 1 | 12.2611 | 11.3836 | -117.5454 | 8.3962 | 92.2087 | 0.0124 | 0.0093 |
| 2024_09_20 22:00 | 3261804 | 2 | 5.2636 | 10.0888 | -115.6379 | 19.7946 | 165.5638 | 0.0079 | 0.0038 |
| 2024_09_20 22:00 | 3237221 | 3 | 5.9493 | 9.1067 | -116.8598 | 18.9553 | 190.4458 | 0.1942 | 0.0134 |
| 2024_09_20 22:00 | 3228526 | 4 | 10.0159 | 13.3733 | -114.2527 | 7.5868 | 198.4383 | 0.0142 | 0.0003 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413277_B23C26DD | 504990 | 694 | -100.5 | 504990 | 840 | -103.0 | 504990 | 399 | -112.6 | 504990 | 370 |
| MR_1774413277_3DFB2371 | 504990 | 694 | -100.8 | 504990 | 840 | -104.0 | 504990 | 399 | -110.1 | 504990 | 370 |
| MR_1774413277_864DF1DA | 504990 | 694 | -99.1 | 504990 | 840 | -102.3 | 504990 | 399 | -110.6 | 504990 | 370 |
| MR_1774413277_9D0448C9 | 504990 | 694 | -98.6 | 504990 | 840 | -102.2 | 504990 | 399 | -113.5 | 504990 | 370 |
| MR_1774413277_FED943DF | 504990 | 694 | -100.7 | 504990 | 840 | -104.5 | 504990 | 399 | -111.0 | 504990 | 370 |
| MR_1774413277_02F241DB | 504990 | 694 | -99.1 | 504990 | 840 | -104.4 | 504990 | 399 | -110.2 | 504990 | 370 |
| MR_1774413277_9BE11E6B | 504990 | 694 | -101.2 | 504990 | 840 | -104.6 | 504990 | 399 | -111.6 | 504990 | 370 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 494: `20246447-016...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `20246447-016a-4262-80f5-9ec14f2a852a` |
| Tag | **multiple-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[494] topology](images/test_0494.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Check test server and transmission issues
- `C2`: Add neighbor relationship between 3248701_2 and 3248382_1
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3248382_1
- `C4`: Adjust the azimuth of 3248382_1 by 11 degrees
- `C5`: Add neighbor relationship between 3253216_3 and 3248382_1
- `C6`: Press down the tilt angle  of 3248382_1 by 4 degrees
- `C7`: Adjust the azimuth of 3248701_2 by 50 degrees
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3248701_2
- `C9`: Increase A3 Offset threshold for 3248382_1
- `C10`: Press down the tilt angle of 3248701_2 by 10 degrees
- `C11`: Increase transmission power for 3248701_2
- `C12`: Decrease transmission power for 3248701_2
- `C13`: Increase transmission power for 3248382_1
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3248701_2
- `C15`: Decrease transmission power for 3248382_1
- `C16`: Lift the tilt angle of 3248701_2 by 10 degrees
- `C17`: Decrease A3 Offset threshold for 3248382_1
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3248382_1
- `C19`: Decrease A3 Offset threshold for 3248701_2
- `C20`: Increase A3 Offset threshold for 3248701_2
- `C21`: Lift the tilt angle  of 3248382_1 by 4 degrees
- `C22`: Insufficient data; more data is needed for judgment.

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.264 | MS1 | 121.4656712460 | 31.1446377010 | 897 | 504990 | -87.63 | 17.33 | 532.95 | 0.03 | 2.48 | 1578 |
| 2024-09-20 22:21:32.227 | MS1 | 121.4656582467 | 31.1446258960 | 897 | 504990 | -89.37 | 16.77 | 444.01 | 0.06 | 2.16 | 1569 |
| 2024-09-20 22:21:33.311 | MS1 | 121.4656624266 | 31.1446337083 | 897 | 504990 | -92.44 | 17.88 | 568.50 | 0.01 | 2.44 | 1597 |
| 2024-09-20 22:21:34.977 | MS1 | 121.4656595376 | 31.1446243996 | 897 | 504990 | -108.84 | -1.73 | 37.18 | 0.03 | 1.26 | 1570 |
| 2024-09-20 22:21:35.398 | MS1 | 121.4656682658 | 31.1446337044 | 897 | 504990 | -101.67 | -0.12 | 61.04 | 0.04 | 1.29 | 1571 |
| 2024-09-20 22:21:36.813 | MS1 | 121.4656705834 | 31.1446379677 | 897 | 504990 | -108.95 | -0.12 | 69.75 | 0.08 | 1.50 | 1596 |
| 2024-09-20 22:21:37.968 | MS1 | 121.4656696683 | 31.1446328271 | 897 | 504990 | -103.42 | -1.94 | 40.89 | 0.03 | 1.38 | 1561 |
| 2024-09-20 22:21:38.702 | MS1 | 121.4656583909 | 31.1446356628 | 897 | 504990 | -107.88 | -0.47 | 47.40 | 0.14 | 1.31 | 1597 |
| 2024-09-20 22:21:39.391 | MS1 | 121.4656764996 | 31.1446218062 | 897 | 504990 | -108.49 | 0.93 | 58.23 | 0.05 | 1.36 | 1576 |
| 2024-09-20 22:21:40.602 | MS1 | 121.4656587532 | 31.1446319127 | 897 | 504990 | -94.50 | 17.69 | 337.14 | 0.11 | 2.72 | 1596 |
| 2024-09-20 22:21:41.228 | MS1 | 121.4656709619 | 31.1446327847 | 897 | 504990 | -90.10 | 13.56 | 412.39 | 0.06 | 2.40 | 1600 |
| 2024-09-20 22:21:42.546 | MS1 | 121.4656700153 | 31.1446202253 | 897 | 504990 | -91.99 | 17.48 | 495.27 | 0.08 | 2.21 | 1567 |

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
| 3248382 | 1 | 121.4756887284 | 31.1526037018 | 238 | 3 | 5 | 24.9 | TDD | 232 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3248701 | 2 | 121.4695310225 | 31.1447705843 | 341 | 13 | 3 | 48.5 | TDD | 897 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3253216 | 3 | 121.4753333696 | 31.1559958116 | 268 | 12 | 9 | 29.0 | TDD | 588 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3259571 | 4 | 121.4709151932 | 31.1519590454 | 180 | 13 | 4 | 44.6 | TDD | 909 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |

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
| 2024-09-20 22:21:31.593 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.617 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.751 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.751 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.932 | NREventA2 | measId:1;ServCellPCI:669;Se... |
| 2024-09-20 22:21:35.081 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3248382 | 1 | 18.3381 | 9.6507 | -115.6087 | 6.7634 | 122.1429 | 0.0188 | 0.0164 |
| 2024_09_20 22:00 | 3248701 | 2 | 6.2489 | 10.8959 | -115.8962 | 16.7468 | 114.5201 | 0.1199 | 0.0162 |
| 2024_09_20 22:00 | 3253216 | 3 | 16.1127 | 7.7568 | -115.8493 | 11.9715 | 129.2789 | 0.0082 | 0.0121 |
| 2024_09_20 22:00 | 3259571 | 4 | 9.4183 | 18.2779 | -116.8541 | 10.3737 | 187.3527 | 0.0090 | 0.0162 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415593_E5FA23A8 | 504990 | 897 | -108.5 | 504990 | 232 | -116.1 | 504990 | 588 | -122.6 | 504990 | 909 |
| MR_1774415593_498CF78F | 504990 | 897 | -108.4 | 504990 | 232 | -114.7 | 504990 | 588 | -121.1 | 504990 | 909 |
| MR_1774415593_FD629478 | 504990 | 897 | -107.0 | 504990 | 232 | -113.5 | 504990 | 588 | -123.0 | 504990 | 909 |
| MR_1774415593_B87CCC07 | 504990 | 897 | -108.0 | 504990 | 232 | -115.8 | 504990 | 588 | -119.6 | 504990 | 909 |
| MR_1774415593_EF652B40 | 504990 | 897 | -107.2 | 504990 | 232 | -112.4 | 504990 | 588 | -121.0 | 504990 | 909 |
| MR_1774415593_93D9EF9F | 504990 | 897 | -109.5 | 504990 | 232 | -115.0 | 504990 | 588 | -122.1 | 504990 | 909 |
| MR_1774415593_250D38D4 | 504990 | 897 | -110.5 | 504990 | 232 | -115.5 | 504990 | 588 | -122.5 | 504990 | 909 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 495: `0d0eb9a9-641...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `0d0eb9a9-641e-4c9d-8ac4-a009996d42ec` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[495] topology](images/test_0495.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3266726_3 and 3228560_2
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3228560_2
- `C3`: Press down the tilt angle  of 3263237_1 by 10 degrees
- `C4`: Lift the tilt angle of 3266726_3 by 3 degrees
- `C5`: Increase transmission power for 3266726_3
- `C6`: Decrease A3 Offset threshold for 3228560_2
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3266726_3
- `C8`: Increase A3 Offset threshold for 3266726_3
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3266726_3
- `C10`: Decrease A3 Offset threshold for 3266726_3
- `C11`: Decrease transmission power for 3266726_3
- `C12`: Decrease transmission power for 3228560_2
- `C13`: Lift the tilt angle  of 3263237_1 by 10 degrees
- `C14`: Adjust the azimuth of 3263237_1 by 2 degrees
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3228560_2
- `C16`: Add neighbor relationship between 3263237_1 and 3228560_2
- `C17`: Check test server and transmission issues
- `C18`: Insufficient data; more data is needed for judgment.
- `C19`: Adjust the azimuth of 3266726_3 by 26 degrees
- `C20`: Increase transmission power for 3228560_2
- `C21`: Increase A3 Offset threshold for 3228560_2
- `C22`: Press down the tilt angle of 3266726_3 by 3 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.470 | MS1 | 121.4656590601 | 31.1446267405 | 901 | 504990 | -87.55 | 13.52 | 407.37 | 0.13 | 2.84 | 1597 |
| 2024-09-20 22:21:32.588 | MS1 | 121.4656581948 | 31.1446223403 | 901 | 504990 | -85.30 | 14.92 | 521.63 | 0.02 | 2.10 | 1583 |
| 2024-09-20 22:21:33.260 | MS1 | 121.4656730057 | 31.1446274076 | 901 | 504990 | -90.84 | 16.12 | 382.50 | 0.01 | 2.98 | 1582 |
| 2024-09-20 22:21:34.396 | MS1 | 121.4656703185 | 31.1446207603 | 901 | 504990 | -91.36 | 12.90 | 79.23 | 0.02 | 2.54 | 1561 |
| 2024-09-20 22:21:35.135 | MS1 | 121.4656667962 | 31.1446187280 | 901 | 504990 | -87.28 | 17.16 | 73.74 | 0.14 | 2.09 | 1583 |
| 2024-09-20 22:21:36.835 | MS1 | 121.4656777742 | 31.1446326257 | 901 | 504990 | -90.86 | 17.69 | 108.54 | 0.15 | 2.57 | 1571 |
| 2024-09-20 22:21:37.100 | MS1 | 121.4656745877 | 31.1446275723 | 901 | 504990 | -93.25 | 12.85 | 61.09 | 0.13 | 2.88 | 1586 |
| 2024-09-20 22:21:38.872 | MS1 | 121.4656618943 | 31.1446341965 | 901 | 504990 | -92.01 | 7.83 | 93.55 | 0.13 | 2.96 | 1568 |
| 2024-09-20 22:21:39.542 | MS1 | 121.4656585130 | 31.1446358802 | 901 | 504990 | -91.26 | 8.80 | 67.53 | 0.03 | 2.60 | 1588 |
| 2024-09-20 22:21:40.949 | MS1 | 121.4656734028 | 31.1446254645 | 901 | 504990 | -92.99 | 11.11 | 409.87 | 0.13 | 2.08 | 1588 |
| 2024-09-20 22:21:41.525 | MS1 | 121.4656648076 | 31.1446260688 | 901 | 504990 | -91.89 | 12.95 | 599.70 | 0.01 | 2.72 | 1570 |
| 2024-09-20 22:21:42.705 | MS1 | 121.4656737555 | 31.1446364768 | 901 | 504990 | -92.35 | 12.45 | 317.32 | 0.14 | 2.59 | 1578 |

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
| 3221139 | 4 | 121.4733138119 | 31.1448078188 | 168 | 14 | 11 | 32.8 | TDD | 542 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3228560 | 2 | 121.4751841213 | 31.1452371421 | 268 | 9 | 3 | 37.8 | TDD | 980 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3263237 | 1 | 121.4745295083 | 31.1464468717 | 58 | 1 | 11 | 15.1 | TDD | 65 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3266726 | 3 | 121.4645673378 | 31.1551370671 | 201 | 2 | 5 | 16.8 | TDD | 901 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:31.678 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.702 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.818 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.818 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.494 | NREventA3 | measId:2;ServCellPCI:291;Se... |
| 2024-09-20 22:21:38.734 | NRHandoverAttempt | SourcePCI:291;SourceNR-ARFC... |
| 2024-09-20 22:21:38.784 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.796 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.901 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.901 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3263237 | 1 | 17.7025 | 6.0884 | -117.6919 | 6.6008 | 95.6844 | 0.0169 | 0.0111 |
| 2024_09_20 22:00 | 3228560 | 2 | 18.4293 | 12.2196 | -115.5128 | 18.4209 | 92.6050 | 0.0083 | 0.0166 |
| 2024_09_20 22:00 | 3266726 | 3 | 88.1723 | 80.3555 | -114.8564 | 15.8462 | 193.2288 | 0.0138 | 0.0036 |
| 2024_09_20 22:00 | 3221139 | 4 | 8.5282 | 17.4146 | -114.2581 | 8.5802 | 154.6575 | 0.0169 | 0.0200 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413594_E5EFB949 | 504990 | 901 | -90.5 | 504990 | 980 | -97.2 | 504990 | 65 | -103.2 | 504990 | 542 |
| MR_1774413594_A77B237C | 504990 | 901 | -92.7 | 504990 | 980 | -96.2 | 504990 | 65 | -102.4 | 504990 | 542 |
| MR_1774413594_6063FA15 | 504990 | 901 | -89.5 | 504990 | 980 | -97.5 | 504990 | 65 | -102.4 | 504990 | 542 |
| MR_1774413594_D252C533 | 504990 | 901 | -91.8 | 504990 | 980 | -96.0 | 504990 | 65 | -104.7 | 504990 | 542 |
| MR_1774413594_F1312D3A | 504990 | 901 | -90.1 | 504990 | 980 | -98.0 | 504990 | 65 | -101.4 | 504990 | 542 |
| MR_1774413594_FE1E0108 | 504990 | 901 | -91.4 | 504990 | 980 | -98.3 | 504990 | 65 | -103.6 | 504990 | 542 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 496: `a43ccc33-002...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `a43ccc33-0022-4a2e-b6ad-8d333cc37e67` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[496] topology](images/test_0496.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3210895_2
- `C2`: Lift the tilt angle  of 3268573_1 by 10 degrees
- `C3`: Decrease transmission power for 3242447_3
- `C4`: Add neighbor relationship between 3268573_1 and 3210895_2
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3242447_3
- `C6`: Add neighbor relationship between 3242447_3 and 3210895_2
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3210895_2
- `C8`: Increase transmission power for 3242447_3
- `C9`: Adjust the azimuth of 3242447_3 by 35 degrees
- `C10`: Press down the tilt angle of 3242447_3 by 4 degrees
- `C11`: Press down the tilt angle  of 3268573_1 by 10 degrees
- `C12`: Increase transmission power for 3210895_2
- `C13`: Increase A3 Offset threshold for 3242447_3
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3210895_2
- `C15`: Decrease A3 Offset threshold for 3242447_3
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3242447_3
- `C17`: Insufficient data; more data is needed for judgment.
- `C18`: Check test server and transmission issues
- `C19`: Lift the tilt angle of 3242447_3 by 4 degrees
- `C20`: Decrease A3 Offset threshold for 3210895_2
- `C21`: Decrease transmission power for 3210895_2
- `C22`: Adjust the azimuth of 3268573_1 by 50 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.592 | MS1 | 121.4656635917 | 31.1446255577 | 44 | 504990 | -85.15 | 15.01 | 402.09 | 0.09 | 2.19 | 1592 |
| 2024-09-20 22:21:32.489 | MS1 | 121.4656690521 | 31.1446254750 | 44 | 504990 | -85.82 | 13.41 | 436.83 | 0.02 | 2.09 | 1595 |
| 2024-09-20 22:21:33.183 | MS1 | 121.4656725770 | 31.1446190050 | 44 | 504990 | -87.51 | 14.98 | 409.47 | 0.17 | 2.60 | 1572 |
| 2024-09-20 22:21:34.573 | MS1 | 121.4656655433 | 31.1446359222 | 44 | 504990 | -88.01 | 14.21 | 55.87 | 0.05 | 2.97 | 1563 |
| 2024-09-20 22:21:35.246 | MS1 | 121.4656640786 | 31.1446370187 | 44 | 504990 | -90.72 | 14.44 | 85.68 | 0.08 | 2.87 | 1588 |
| 2024-09-20 22:21:36.576 | MS1 | 121.4656684592 | 31.1446335224 | 44 | 504990 | -88.58 | 15.16 | 74.15 | 0.06 | 2.20 | 1565 |
| 2024-09-20 22:21:37.984 | MS1 | 121.4656768582 | 31.1446309582 | 44 | 504990 | -91.52 | 10.69 | 70.47 | 0.03 | 2.33 | 1578 |
| 2024-09-20 22:21:38.199 | MS1 | 121.4656664473 | 31.1446319038 | 44 | 504990 | -93.78 | 7.77 | 81.42 | 0.13 | 2.52 | 1572 |
| 2024-09-20 22:21:39.477 | MS1 | 121.4656671076 | 31.1446370870 | 44 | 504990 | -92.66 | 12.93 | 71.66 | 0.18 | 2.96 | 1574 |
| 2024-09-20 22:21:40.699 | MS1 | 121.4656757641 | 31.1446357186 | 44 | 504990 | -91.97 | 11.15 | 501.53 | 0.11 | 2.34 | 1568 |
| 2024-09-20 22:21:41.421 | MS1 | 121.4656667540 | 31.1446322503 | 44 | 504990 | -93.54 | 12.41 | 390.19 | 0.02 | 2.43 | 1585 |
| 2024-09-20 22:21:42.985 | MS1 | 121.4656631387 | 31.1446329718 | 44 | 504990 | -92.57 | 8.12 | 451.63 | 0.11 | 2.16 | 1597 |

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
| 3210895 | 2 | 121.4717230389 | 31.1545507863 | 305 | 15 | 4 | 21.1 | TDD | 51 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3242447 | 3 | 121.4658919444 | 31.1526145487 | 216 | 2 | 11 | 27.2 | TDD | 44 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3248467 | 4 | 121.4684407200 | 31.1519606113 | 134 | 12 | 10 | 26.8 | TDD | 144 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3268573 | 1 | 121.4671022673 | 31.1557634548 | 50 | 9 | 11 | 20.0 | TDD | 8 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |

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
| 2024-09-20 22:21:31.319 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.344 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.451 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.451 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.144 | NREventA3 | measId:2;ServCellPCI:483;Se... |
| 2024-09-20 22:21:38.384 | NRHandoverAttempt | SourcePCI:483;SourceNR-ARFC... |
| 2024-09-20 22:21:38.430 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.443 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.544 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.544 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3268573 | 1 | 11.0793 | 6.7503 | -117.7532 | 9.2607 | 166.8234 | 0.0154 | 0.0095 |
| 2024_09_20 22:00 | 3210895 | 2 | 5.0957 | 16.8622 | -115.0830 | 12.0977 | 184.0268 | 0.0007 | 0.0026 |
| 2024_09_20 22:00 | 3242447 | 3 | 75.2675 | 89.4893 | -114.3892 | 8.9382 | 147.0423 | 0.0026 | 0.0180 |
| 2024_09_20 22:00 | 3248467 | 4 | 15.2428 | 13.4719 | -117.7754 | 8.9313 | 137.3412 | 0.0083 | 0.0050 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774411981_96609B0C | 504990 | 44 | -86.8 | 504990 | 51 | -87.4 | 504990 | 8 | -97.5 | 504990 | 144 |
| MR_1774411981_CD752199 | 504990 | 44 | -88.4 | 504990 | 51 | -86.5 | 504990 | 8 | -95.8 | 504990 | 144 |
| MR_1774411981_36C55928 | 504990 | 44 | -88.2 | 504990 | 51 | -87.2 | 504990 | 8 | -95.9 | 504990 | 144 |
| MR_1774411981_4A6B9ED6 | 504990 | 44 | -88.3 | 504990 | 51 | -87.0 | 504990 | 8 | -94.7 | 504990 | 144 |
| MR_1774411981_EE1FBA0C | 504990 | 44 | -87.8 | 504990 | 51 | -88.7 | 504990 | 8 | -97.4 | 504990 | 144 |
| MR_1774411981_09999325 | 504990 | 44 | -88.7 | 504990 | 51 | -88.1 | 504990 | 8 | -95.9 | 504990 | 144 |
| MR_1774411981_ED26D760 | 504990 | 44 | -87.7 | 504990 | 51 | -88.3 | 504990 | 8 | -96.6 | 504990 | 144 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 497: `4797741d-169...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `4797741d-1691-49cb-ad1e-b57c1502b03c` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[497] topology](images/test_0497.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3210756_2
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3268217_4
- `C3`: Decrease A3 Offset threshold for 3210756_2
- `C4`: Insufficient data; more data is needed for judgment.
- `C5`: Press down the tilt angle of 3268217_4 by 6 degrees
- `C6`: Increase transmission power for 3268217_4
- `C7`: Increase transmission power for 3210756_2
- `C8`: Lift the tilt angle of 3268217_4 by 6 degrees
- `C9`: Adjust the azimuth of 3268217_4 by 50 degrees
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3268217_4
- `C11`: Decrease transmission power for 3210756_2
- `C12`: Decrease A3 Offset threshold for 3268217_4
- `C13`: Lift the tilt angle  of 3210756_2 by 6 degrees
- `C14`: Increase A3 Offset threshold for 3268217_4
- `C15`: Increase A3 Offset threshold for 3210756_2
- `C16`: Add neighbor relationship between 3268217_4 and 3210756_2
- `C17`: Decrease transmission power for 3268217_4
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3210756_2
- `C19`: Adjust the azimuth of 3210756_2 by 2 degrees
- `C20`: Add neighbor relationship between 3243017_3 and 3210756_2
- `C21`: Press down the tilt angle  of 3210756_2 by 6 degrees
- `C22`: Check test server and transmission issues

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.507 | MS1 | 121.4656585660 | 31.1446228546 | 524 | 504990 | -84.17 | 14.68 | 351.58 | 0.18 | 2.09 | 1598 |
| 2024-09-20 22:21:32.770 | MS1 | 121.4656739641 | 31.1446316534 | 524 | 504990 | -79.15 | 13.38 | 414.81 | 0.03 | 2.86 | 1566 |
| 2024-09-20 22:21:33.667 | MS1 | 121.4656704099 | 31.1446327071 | 524 | 504990 | -76.46 | 16.92 | 464.04 | 0.16 | 2.80 | 1588 |
| 2024-09-20 22:21:34.108 | MS1 | 121.4656764145 | 31.1446334222 | 524 | 504990 | -93.99 | -1.33 | 41.95 | 0.01 | 1.11 | 1583 |
| 2024-09-20 22:21:35.939 | MS1 | 121.4656737331 | 31.1446377109 | 524 | 504990 | -92.20 | -3.52 | 57.99 | 0.02 | 1.41 | 1587 |
| 2024-09-20 22:21:36.397 | MS1 | 121.4656654153 | 31.1446375643 | 524 | 504990 | -87.44 | -0.55 | 42.47 | 0.02 | 1.47 | 1563 |
| 2024-09-20 22:21:37.338 | MS1 | 121.4656588769 | 31.1446354303 | 524 | 504990 | -94.60 | -1.11 | 22.65 | 0.11 | 1.18 | 1580 |
| 2024-09-20 22:21:38.488 | MS1 | 121.4656749487 | 31.1446273700 | 524 | 504990 | -76.40 | 17.34 | 354.70 | 0.04 | 1.35 | 1594 |
| 2024-09-20 22:21:39.342 | MS1 | 121.4656588763 | 31.1446378129 | 524 | 504990 | -84.66 | 14.52 | 313.55 | 0.10 | 1.08 | 1568 |
| 2024-09-20 22:21:40.150 | MS1 | 121.4656704401 | 31.1446347454 | 524 | 504990 | -76.08 | 13.44 | 536.72 | 0.14 | 2.15 | 1581 |
| 2024-09-20 22:21:41.968 | MS1 | 121.4656607767 | 31.1446239583 | 524 | 504990 | -75.46 | 15.60 | 397.78 | 0.14 | 2.09 | 1566 |
| 2024-09-20 22:21:42.262 | MS1 | 121.4656666184 | 31.1446209224 | 524 | 504990 | -80.76 | 17.40 | 305.42 | 0.13 | 2.43 | 1565 |

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
| 3210756 | 2 | 121.4672599389 | 31.1504299316 | 191 | 3 | 8 | 34.6 | TDD | 489 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3215777 | 1 | 121.4715779296 | 31.1451330231 | 161 | 13 | 7 | 27.3 | TDD | 628 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3243017 | 3 | 121.4697990568 | 31.1531009204 | 299 | 15 | 2 | 16.2 | TDD | 892 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3268217 | 4 | 121.4749201019 | 31.1473521996 | 304 | 3 | 0 | 49.8 | TDD | 524 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |

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
| 2024-09-20 22:21:30.804 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.822 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:30.969 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.969 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.621 | NREventA3 | measId:2;ServCellPCI:949;Se... |
| 2024-09-20 22:21:35.621 | NREventA3 | measId:2;ServCellPCI:949;Se... |
| 2024-09-20 22:21:36.621 | NREventA3 | measId:2;ServCellPCI:949;Se... |
| 2024-09-20 22:21:39.121 | NRRRCReestablishAttempt | PCI:949 |
| 2024-09-20 22:21:39.133 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.147 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:39.294 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.294 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3215777 | 1 | 19.9326 | 16.8305 | -115.5926 | 10.6987 | 111.8896 | 0.0177 | 0.0108 |
| 2024_09_20 22:00 | 3210756 | 2 | 9.9446 | 7.5520 | -115.0001 | 12.8307 | 168.6562 | 0.0196 | 0.0111 |
| 2024_09_20 22:00 | 3243017 | 3 | 10.1943 | 6.8831 | -116.7765 | 18.5600 | 173.3198 | 0.0142 | 0.0118 |
| 2024_09_20 22:00 | 3268217 | 4 | 17.6148 | 10.4784 | -117.9275 | 5.2489 | 111.2792 | 0.0067 | 0.1018 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414588_3EEA22A8 | 504990 | 489 | -86.8 | 504990 | 524 | -95.9 | 504990 | 892 | -99.2 | 504990 | 628 |
| MR_1774414588_13BC4A90 | 504990 | 524 | -92.2 | 504990 | 489 | -86.1 | 504990 | 892 | -99.5 | 504990 | 628 |
| MR_1774414588_E5AC9E8B | 504990 | 524 | -95.2 | 504990 | 489 | -86.6 | 504990 | 892 | -99.6 | 504990 | 628 |
| MR_1774414588_787B29C8 | 504990 | 489 | -87.8 | 504990 | 524 | -92.1 | 504990 | 892 | -98.1 | 504990 | 628 |
| MR_1774414588_B11484BC | 504990 | 524 | -92.6 | 504990 | 489 | -86.2 | 504990 | 892 | -100.1 | 504990 | 628 |
| MR_1774414588_27337F54 | 504990 | 524 | -93.3 | 504990 | 489 | -87.6 | 504990 | 892 | -99.9 | 504990 | 628 |
| MR_1774414588_6441D771 | 504990 | 524 | -95.1 | 504990 | 489 | -88.7 | 504990 | 892 | -98.4 | 504990 | 628 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 498: `2c1973e2-300...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `2c1973e2-3000-448b-a016-857b591c6069` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[498] topology](images/test_0498.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3241272_3
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3248374_1
- `C3`: Check test server and transmission issues
- `C4`: Lift the tilt angle of 3241272_3 by 9 degrees
- `C5`: Adjust the azimuth of 3241272_3 by 18 degrees
- `C6`: Decrease transmission power for 3241272_3
- `C7`: Lift the tilt angle  of 3248374_1 by 3 degrees
- `C8`: Add neighbor relationship between 3210669_4 and 3248374_1
- `C9`: Adjust the azimuth of 3248374_1 by 20 degrees
- `C10`: Increase transmission power for 3241272_3
- `C11`: Press down the tilt angle  of 3248374_1 by 3 degrees
- `C12`: Insufficient data; more data is needed for judgment.
- `C13`: Increase A3 Offset threshold for 3241272_3
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3241272_3
- `C15`: Decrease transmission power for 3248374_1
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3248374_1
- `C17`: Increase A3 Offset threshold for 3248374_1
- `C18`: Add neighbor relationship between 3241272_3 and 3248374_1
- `C19`: Increase transmission power for 3248374_1
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3241272_3
- `C21`: Press down the tilt angle of 3241272_3 by 9 degrees
- `C22`: Decrease A3 Offset threshold for 3248374_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.963 | MS1 | 121.4656609576 | 31.1446298278 | 570 | 504990 | -78.97 | 15.21 | 536.91 | 0.16 | 2.74 | 1579 |
| 2024-09-20 22:21:32.130 | MS1 | 121.4656727065 | 31.1446307556 | 570 | 504990 | -76.38 | 14.49 | 375.22 | 0.06 | 2.66 | 1589 |
| 2024-09-20 22:21:33.574 | MS1 | 121.4656721306 | 31.1446283730 | 570 | 504990 | -76.23 | 14.32 | 353.77 | 0.10 | 2.59 | 1600 |
| 2024-09-20 22:21:34.305 | MS1 | 121.4656666528 | 31.1446203562 | 570 | 504990 | -86.55 | -0.33 | 47.72 | 0.16 | 1.41 | 1570 |
| 2024-09-20 22:21:35.834 | MS1 | 121.4656714869 | 31.1446279760 | 570 | 504990 | -86.75 | -3.76 | 48.63 | 0.17 | 1.32 | 1589 |
| 2024-09-20 22:21:36.466 | MS1 | 121.4656658925 | 31.1446317683 | 570 | 504990 | -94.25 | -3.74 | 45.41 | 0.07 | 1.38 | 1589 |
| 2024-09-20 22:21:37.679 | MS1 | 121.4656588961 | 31.1446223372 | 570 | 504990 | -91.28 | -0.44 | 56.90 | 0.13 | 1.43 | 1594 |
| 2024-09-20 22:21:38.574 | MS1 | 121.4656625677 | 31.1446372799 | 570 | 504990 | -81.51 | 15.69 | 377.14 | 0.11 | 1.01 | 1563 |
| 2024-09-20 22:21:39.915 | MS1 | 121.4656681157 | 31.1446225451 | 570 | 504990 | -81.54 | 15.80 | 561.55 | 0.05 | 1.31 | 1597 |
| 2024-09-20 22:21:40.531 | MS1 | 121.4656743686 | 31.1446348290 | 570 | 504990 | -78.89 | 15.60 | 421.29 | 0.19 | 2.80 | 1581 |
| 2024-09-20 22:21:41.997 | MS1 | 121.4656670399 | 31.1446274615 | 570 | 504990 | -82.98 | 16.14 | 430.36 | 0.03 | 2.43 | 1583 |
| 2024-09-20 22:21:42.574 | MS1 | 121.4656754456 | 31.1446335479 | 570 | 504990 | -79.08 | 17.29 | 364.93 | 0.14 | 2.82 | 1591 |

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
| 3210669 | 4 | 121.4738547848 | 31.1538454440 | 287 | 2 | 4 | 46.9 | TDD | 853 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3241272 | 3 | 121.4714389297 | 31.1551804444 | 187 | 7 | 12 | 47.4 | TDD | 570 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3248374 | 1 | 121.4684410951 | 31.1479310376 | 196 | 0 | 6 | 23.8 | TDD | 418 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3275802 | 2 | 121.4757537916 | 31.1484072578 | 347 | 10 | 6 | 45.4 | TDD | 27 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |

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
| 2024-09-20 22:21:31.339 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.362 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.472 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.472 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.154 | NREventA3 | measId:2;ServCellPCI:667;Se... |
| 2024-09-20 22:21:36.154 | NREventA3 | measId:2;ServCellPCI:667;Se... |
| 2024-09-20 22:21:37.154 | NREventA3 | measId:2;ServCellPCI:667;Se... |
| 2024-09-20 22:21:39.654 | NRRRCReestablishAttempt | PCI:667 |
| 2024-09-20 22:21:39.674 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.689 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:39.837 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.837 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3248374 | 1 | 12.2039 | 8.6408 | -115.1198 | 10.2804 | 169.1256 | 0.0080 | 0.0189 |
| 2024_09_20 22:00 | 3275802 | 2 | 11.6693 | 11.7006 | -114.3929 | 15.1480 | 154.5328 | 0.0198 | 0.0073 |
| 2024_09_20 22:00 | 3241272 | 3 | 8.9067 | 9.4804 | -115.3016 | 5.6313 | 107.9168 | 0.0029 | 0.1500 |
| 2024_09_20 22:00 | 3210669 | 4 | 12.7359 | 9.3377 | -114.7723 | 8.1263 | 170.9293 | 0.0154 | 0.0066 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413704_88AFE33B | 504990 | 418 | -82.0 | 504990 | 570 | -87.3 | 504990 | 853 | -90.2 | 504990 | 27 |
| MR_1774413704_1EB79640 | 504990 | 570 | -88.2 | 504990 | 418 | -82.5 | 504990 | 853 | -90.0 | 504990 | 27 |
| MR_1774413704_0DA3C9A5 | 504990 | 570 | -84.6 | 504990 | 418 | -81.4 | 504990 | 853 | -90.4 | 504990 | 27 |
| MR_1774413704_95E4B014 | 504990 | 418 | -84.1 | 504990 | 570 | -85.9 | 504990 | 853 | -87.8 | 504990 | 27 |
| MR_1774413704_62E9AB1F | 504990 | 570 | -84.7 | 504990 | 418 | -81.2 | 504990 | 853 | -90.4 | 504990 | 27 |
| MR_1774413704_A4A23324 | 504990 | 418 | -82.2 | 504990 | 570 | -85.7 | 504990 | 853 | -87.1 | 504990 | 27 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 499: `f95c5233-bd9...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `f95c5233-bd9c-4305-8bd4-5385158c436e` |
| Tag | **multiple-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[499] topology](images/test_0499.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 5 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 5개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3224046_2 and 3219221_3
- `C2`: Increase A3 Offset threshold for 3219221_3
- `C3`: Press down the tilt angle of 3214189_5 by 4 degrees
- `C4`: Decrease transmission power for 3214189_5
- `C5`: Insufficient data; more data is needed for judgment.
- `C6`: Lift the tilt angle of 3214189_5 by 4 degrees
- `C7`: Increase A3 Offset threshold for 3214189_5
- `C8`: Press down the tilt angle  of 3219221_3 by 2 degrees
- `C9`: Adjust the azimuth of 3219221_3 by 46 degrees
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3214189_5
- `C11`: Lift the tilt angle  of 3219221_3 by 2 degrees
- `C12`: Increase transmission power for 3214189_5
- `C13`: Decrease transmission power for 3219221_3
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3219221_3
- `C15`: Adjust the azimuth of 3214189_5 by 9 degrees
- `C16`: Increase transmission power for 3219221_3
- `C17`: Decrease A3 Offset threshold for 3214189_5
- `C18`: Decrease A3 Offset threshold for 3219221_3
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3219221_3
- `C20`: Add neighbor relationship between 3214189_5 and 3219221_3
- `C21`: Check test server and transmission issues
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3214189_5

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.186 | MS1 | 121.4656640213 | 31.1446320634 | 510 | 504990 | -84.29 | 12.12 | 571.77 | 0.01 | 2.61 | 1593 |
| 2024-09-20 22:21:32.392 | MS1 | 121.4656679393 | 31.1446206700 | 510 | 504990 | -75.36 | 14.52 | 506.38 | 0.18 | 2.68 | 1584 |
| 2024-09-20 22:21:33.178 | MS1 | 121.4656760266 | 31.1446347988 | 510 | 504990 | -82.36 | 12.48 | 571.86 | 0.01 | 2.03 | 1579 |
| 2024-09-20 22:21:34.326 | MS1 | 121.4656684829 | 31.1446269674 | 88 | 504990 | -87.92 | 3.90 | 35.88 | 0.08 | 1.06 | 1588 |
| 2024-09-20 22:21:35.861 | MS1 | 121.4656615475 | 31.1446269261 | 88 | 504990 | -86.63 | 3.54 | 74.09 | 0.07 | 1.42 | 1570 |
| 2024-09-20 22:21:36.973 | MS1 | 121.4656757343 | 31.1446206765 | 510 | 504990 | -87.79 | 1.49 | 61.79 | 0.20 | 1.36 | 1589 |
| 2024-09-20 22:21:37.573 | MS1 | 121.4656605396 | 31.1446268959 | 510 | 504990 | -81.90 | 4.12 | 67.51 | 0.04 | 1.32 | 1600 |
| 2024-09-20 22:21:38.393 | MS1 | 121.4656614876 | 31.1446268957 | 88 | 504990 | -84.93 | 1.40 | 36.91 | 0.03 | 1.32 | 1597 |
| 2024-09-20 22:21:39.759 | MS1 | 121.4656741116 | 31.1446242130 | 88 | 504990 | -83.46 | 1.64 | 70.95 | 0.01 | 1.20 | 1580 |
| 2024-09-20 22:21:40.526 | MS1 | 121.4656706240 | 31.1446245081 | 88 | 504990 | -75.66 | 17.47 | 347.54 | 0.02 | 2.22 | 1560 |
| 2024-09-20 22:21:41.361 | MS1 | 121.4656741192 | 31.1446229514 | 88 | 504990 | -81.88 | 13.34 | 443.34 | 0.11 | 2.72 | 1583 |
| 2024-09-20 22:21:42.362 | MS1 | 121.4656754494 | 31.1446375403 | 88 | 504990 | -83.56 | 15.56 | 394.03 | 0.06 | 2.35 | 1575 |

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
| 3214189 | 5 | 121.4679758520 | 31.1476702210 | 204 | 1 | 3 | 20.8 | TDD | 510 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3219221 | 3 | 121.4648701673 | 31.1548120625 | 130 | 1 | 1 | 20.1 | TDD | 310 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3224046 | 2 | 121.4715160882 | 31.1445699805 | 188 | 15 | 11 | 44.9 | TDD | 6 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3249153 | 4 | 121.4655355184 | 31.1446846041 | 167 | 4 | 1 | 44.2 | TDD | 88 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3274129 | 1 | 121.4706327807 | 31.1499518204 | 293 | 4 | 6 | 25.6 | TDD | 548 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |

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
| 2024-09-20 22:21:31.264 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.289 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.414 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.414 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.069 | NREventA3 | measId:2;ServCellPCI:777;Se... |
| 2024-09-20 22:21:34.309 | NRHandoverAttempt | SourcePCI:777;SourceNR-ARFC... |
| 2024-09-20 22:21:34.352 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:34.365 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:34.481 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:34.481 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:36.069 | NREventA3 | measId:2;ServCellPCI:558;Se... |
| 2024-09-20 22:21:36.309 | NRHandoverAttempt | SourcePCI:558;SourceNR-ARFC... |
| 2024-09-20 22:21:36.351 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:36.365 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:36.487 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.487 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.069 | NREventA3 | measId:2;ServCellPCI:777;Se... |
| 2024-09-20 22:21:38.309 | NRHandoverAttempt | SourcePCI:777;SourceNR-ARFC... |
| 2024-09-20 22:21:38.355 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.366 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.505 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.505 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3274129 | 1 | 15.0918 | 19.4215 | -115.8944 | 6.1579 | 126.7010 | 0.0120 | 0.0125 |
| 2024_09_20 22:00 | 3224046 | 2 | 10.7124 | 13.1638 | -114.0807 | 12.3296 | 147.6427 | 0.0083 | 0.0188 |
| 2024_09_20 22:00 | 3219221 | 3 | 7.7705 | 6.1064 | -116.9248 | 12.7770 | 128.6996 | 0.0150 | 0.0071 |
| 2024_09_20 22:00 | 3249153 | 4 | 16.2694 | 11.4363 | -115.3451 | 5.0441 | 190.1727 | 0.0011 | 0.0072 |
| 2024_09_20 22:00 | 3214189 | 5 | 6.4792 | 15.9625 | -115.2420 | 7.9955 | 143.2297 | 0.0060 | 0.0038 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415594_92F67E0F | 504990 | 510 | -88.1 | 504990 | 88 | -83.7 | 504990 | 310 | -86.8 | 504990 | 6 |
| MR_1774415594_290CD140 | 504990 | 88 | -86.6 | 504990 | 510 | -83.8 | 504990 | 310 | -87.6 | 504990 | 6 |
| MR_1774415594_BCB75100 | 504990 | 510 | -86.1 | 504990 | 88 | -85.2 | 504990 | 310 | -86.6 | 504990 | 6 |
| MR_1774415594_C03C3DC2 | 504990 | 88 | -86.7 | 504990 | 510 | -82.6 | 504990 | 310 | -88.0 | 504990 | 6 |
| MR_1774415594_3A912AE8 | 504990 | 510 | -86.6 | 504990 | 88 | -82.7 | 504990 | 310 | -87.3 | 504990 | 6 |
| MR_1774415594_B1F3134B | 504990 | 510 | -87.4 | 504990 | 88 | -84.2 | 504990 | 310 | -87.9 | 504990 | 6 |
| MR_1774415594_2FA04FE8 | 504990 | 510 | -89.1 | 504990 | 88 | -84.2 | 504990 | 310 | -87.1 | 504990 | 6 |

> *... 2개 열 생략 (전체 14열)*

---
