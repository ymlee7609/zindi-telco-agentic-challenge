# Track A 문제 분석 — test[190]~test[199]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/test.json`
> 범위: test[190] ~ test[199] (10개)

## 목차

1. [문제 190: `d41178af-2f1...`](#190) — single-answer
2. [문제 191: `ae4fb431-f18...`](#191) — single-answer
3. [문제 192: `55b007b6-72a...`](#192) — single-answer
4. [문제 193: `c83b850c-7c2...`](#193) — single-answer
5. [문제 194: `9baf6d46-290...`](#194) — multiple-answer
6. [문제 195: `af52175e-56f...`](#195) — single-answer
7. [문제 196: `9c32f53f-622...`](#196) — multiple-answer
8. [문제 197: `b6462848-e14...`](#197) — single-answer
9. [문제 198: `4a7d1ec9-3ce...`](#198) — single-answer
10. [문제 199: `256b3278-305...`](#199) — single-answer

---

### 문제 190: `d41178af-2f1...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `d41178af-2f18-4d8e-910e-e3507144de55` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[190] topology](images/test_0190.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3218108_1
- `C2`: Increase A3 Offset threshold for 3248835_2
- `C3`: Lift the tilt angle  of 3248835_2 by 4 degrees
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3248835_2
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3218108_1
- `C6`: Adjust the azimuth of 3218108_1 by 50 degrees
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3248835_2
- `C8`: Press down the tilt angle of 3218108_1 by 3 degrees
- `C9`: Check test server and transmission issues
- `C10`: Decrease transmission power for 3248835_2
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3218108_1
- `C12`: Decrease A3 Offset threshold for 3218108_1
- `C13`: Increase transmission power for 3218108_1
- `C14`: Increase transmission power for 3248835_2
- `C15`: Add neighbor relationship between 3225146_4 and 3248835_2
- `C16`: Decrease transmission power for 3218108_1
- `C17`: Press down the tilt angle  of 3248835_2 by 4 degrees
- `C18`: Insufficient data; more data is needed for judgment.
- `C19`: Decrease A3 Offset threshold for 3248835_2
- `C20`: Lift the tilt angle of 3218108_1 by 3 degrees
- `C21`: Add neighbor relationship between 3218108_1 and 3248835_2
- `C22`: Adjust the azimuth of 3248835_2 by 37 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.450 | MS1 | 121.4656667037 | 31.1446334447 | 224 | 504990 | -79.34 | 14.68 | 549.26 | 0.19 | 2.57 | 1561 |
| 2024-09-20 22:21:32.153 | MS1 | 121.4656684354 | 31.1446319003 | 224 | 504990 | -82.05 | 15.26 | 327.41 | 0.00 | 2.07 | 1587 |
| 2024-09-20 22:21:33.618 | MS1 | 121.4656668254 | 31.1446338759 | 224 | 504990 | -77.73 | 14.63 | 547.97 | 0.18 | 2.69 | 1585 |
| 2024-09-20 22:21:34.886 | MS1 | 121.4656644897 | 31.1446253017 | 224 | 504990 | -85.49 | -2.41 | 53.69 | 0.16 | 1.38 | 1588 |
| 2024-09-20 22:21:35.917 | MS1 | 121.4656776163 | 31.1446266005 | 224 | 504990 | -88.48 | -2.55 | 67.82 | 0.04 | 1.30 | 1597 |
| 2024-09-20 22:21:36.394 | MS1 | 121.4656621573 | 31.1446314405 | 224 | 504990 | -89.07 | -3.62 | 29.91 | 0.19 | 1.08 | 1561 |
| 2024-09-20 22:21:37.449 | MS1 | 121.4656664797 | 31.1446258155 | 224 | 504990 | -90.64 | -2.56 | 45.20 | 0.07 | 1.45 | 1562 |
| 2024-09-20 22:21:38.103 | MS1 | 121.4656620499 | 31.1446238473 | 224 | 504990 | -77.87 | 16.79 | 306.58 | 0.07 | 1.36 | 1580 |
| 2024-09-20 22:21:39.678 | MS1 | 121.4656768973 | 31.1446259257 | 224 | 504990 | -83.60 | 15.26 | 533.58 | 0.00 | 1.21 | 1594 |
| 2024-09-20 22:21:40.323 | MS1 | 121.4656588879 | 31.1446275337 | 224 | 504990 | -79.10 | 15.93 | 440.96 | 0.08 | 2.80 | 1593 |
| 2024-09-20 22:21:41.472 | MS1 | 121.4656617858 | 31.1446343589 | 224 | 504990 | -82.17 | 13.90 | 584.14 | 0.14 | 2.51 | 1589 |
| 2024-09-20 22:21:42.361 | MS1 | 121.4656589537 | 31.1446251996 | 224 | 504990 | -76.70 | 12.96 | 354.62 | 0.03 | 2.61 | 1572 |

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
| 3211263 | 3 | 121.4735859992 | 31.1511265709 | 180 | 1 | 1 | 39.1 | TDD | 4 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3218108 | 1 | 121.4723645853 | 31.1505633250 | 291 | 2 | 3 | 17.7 | TDD | 224 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3225146 | 4 | 121.4736063574 | 31.1534759109 | 38 | 15 | 4 | 33.7 | TDD | 358 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3248835 | 2 | 121.4649824242 | 31.1547527299 | 140 | 2 | 5 | 45.5 | TDD | 859 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:31.552 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.576 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.720 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.720 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.388 | NREventA3 | measId:2;ServCellPCI:672;Se... |
| 2024-09-20 22:21:36.388 | NREventA3 | measId:2;ServCellPCI:672;Se... |
| 2024-09-20 22:21:37.388 | NREventA3 | measId:2;ServCellPCI:672;Se... |
| 2024-09-20 22:21:39.888 | NRRRCReestablishAttempt | PCI:672 |
| 2024-09-20 22:21:39.902 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.913 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:40.053 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:40.053 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3218108 | 1 | 6.6502 | 8.3865 | -117.0327 | 15.6267 | 84.9805 | 0.0053 | 0.1342 |
| 2024_09_20 22:00 | 3248835 | 2 | 6.4449 | 19.1204 | -115.4102 | 13.4118 | 196.0045 | 0.0062 | 0.0148 |
| 2024_09_20 22:00 | 3211263 | 3 | 17.7954 | 8.9583 | -117.6385 | 8.0881 | 139.1671 | 0.0146 | 0.0135 |
| 2024_09_20 22:00 | 3225146 | 4 | 19.5418 | 13.6170 | -117.3939 | 9.0458 | 152.3644 | 0.0107 | 0.0057 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416254_935EA2EA | 504990 | 859 | -81.6 | 504990 | 224 | -85.9 | 504990 | 358 | -88.2 | 504990 | 4 |
| MR_1774416254_C3FE3D66 | 504990 | 859 | -81.7 | 504990 | 224 | -85.2 | 504990 | 358 | -87.0 | 504990 | 4 |
| MR_1774416254_6FB8E2E4 | 504990 | 224 | -84.5 | 504990 | 859 | -81.8 | 504990 | 358 | -88.8 | 504990 | 4 |
| MR_1774416254_A41ACB0E | 504990 | 224 | -86.7 | 504990 | 859 | -79.1 | 504990 | 358 | -87.4 | 504990 | 4 |
| MR_1774416254_AE2302EE | 504990 | 859 | -79.1 | 504990 | 224 | -85.3 | 504990 | 358 | -86.3 | 504990 | 4 |
| MR_1774416254_A5BF648A | 504990 | 224 | -85.1 | 504990 | 859 | -80.8 | 504990 | 358 | -88.6 | 504990 | 4 |
| MR_1774416254_49382ECE | 504990 | 859 | -79.5 | 504990 | 224 | -84.6 | 504990 | 358 | -86.6 | 504990 | 4 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 191: `ae4fb431-f18...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `ae4fb431-f189-4383-b6be-bbe654ef6f94` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[191] topology](images/test_0191.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3219648_2
- `C2`: Decrease A3 Offset threshold for 3255688_3
- `C3`: Adjust the azimuth of 3228959_1 by 50 degrees
- `C4`: Decrease transmission power for 3219648_2
- `C5`: Press down the tilt angle  of 3228959_1 by 10 degrees
- `C6`: Increase transmission power for 3219648_2
- `C7`: Increase A3 Offset threshold for 3255688_3
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3219648_2
- `C9`: Decrease A3 Offset threshold for 3219648_2
- `C10`: Decrease transmission power for 3255688_3
- `C11`: Increase A3 Offset threshold for 3219648_2
- `C12`: Add neighbor relationship between 3219648_2 and 3255688_3
- `C13`: Insufficient data; more data is needed for judgment.
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3255688_3
- `C15`: Add neighbor relationship between 3228959_1 and 3255688_3
- `C16`: Adjust the azimuth of 3219648_2 by 14 degrees
- `C17`: Press down the tilt angle of 3219648_2 by 4 degrees
- `C18`: Lift the tilt angle  of 3228959_1 by 10 degrees
- `C19`: Check test server and transmission issues
- `C20`: Lift the tilt angle of 3219648_2 by 4 degrees
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3255688_3
- `C22`: Increase transmission power for 3255688_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.683 | MS1 | 121.4656643535 | 31.1446185369 | 281 | 504990 | -91.01 | 12.08 | 350.76 | 0.14 | 2.88 | 1574 |
| 2024-09-20 22:21:32.768 | MS1 | 121.4656617366 | 31.1446286807 | 281 | 504990 | -87.20 | 14.46 | 565.74 | 0.10 | 2.78 | 1571 |
| 2024-09-20 22:21:33.936 | MS1 | 121.4656775828 | 31.1446225567 | 281 | 504990 | -89.87 | 13.71 | 457.92 | 0.12 | 2.70 | 1561 |
| 2024-09-20 22:21:34.249 | MS1 | 121.4656731384 | 31.1446318399 | 281 | 504990 | -91.35 | 16.68 | 64.14 | 0.18 | 2.22 | 1589 |
| 2024-09-20 22:21:35.118 | MS1 | 121.4656675492 | 31.1446223087 | 281 | 504990 | -88.82 | 17.59 | 69.13 | 0.15 | 2.30 | 1592 |
| 2024-09-20 22:21:36.563 | MS1 | 121.4656687108 | 31.1446197686 | 281 | 504990 | -90.49 | 15.15 | 52.30 | 0.17 | 2.08 | 1568 |
| 2024-09-20 22:21:37.680 | MS1 | 121.4656645182 | 31.1446357353 | 281 | 504990 | -93.51 | 8.88 | 61.36 | 0.13 | 2.73 | 1600 |
| 2024-09-20 22:21:38.358 | MS1 | 121.4656660827 | 31.1446254014 | 281 | 504990 | -93.01 | 10.66 | 85.30 | 0.07 | 2.88 | 1579 |
| 2024-09-20 22:21:39.839 | MS1 | 121.4656653257 | 31.1446287950 | 281 | 504990 | -92.86 | 8.51 | 85.55 | 0.09 | 2.20 | 1598 |
| 2024-09-20 22:21:40.697 | MS1 | 121.4656666249 | 31.1446316846 | 281 | 504990 | -90.35 | 8.39 | 546.85 | 0.05 | 2.75 | 1583 |
| 2024-09-20 22:21:41.637 | MS1 | 121.4656717085 | 31.1446180070 | 281 | 504990 | -89.03 | 8.41 | 545.55 | 0.18 | 2.36 | 1575 |
| 2024-09-20 22:21:42.794 | MS1 | 121.4656641250 | 31.1446197589 | 281 | 504990 | -93.46 | 9.58 | 572.28 | 0.09 | 2.58 | 1571 |

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
| 3219648 | 2 | 121.4755040548 | 31.1546331489 | 234 | 3 | 12 | 24.5 | TDD | 281 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3228959 | 1 | 121.4652633701 | 31.1476835488 | 256 | 15 | 1 | 33.9 | TDD | 656 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3231396 | 4 | 121.4670762037 | 31.1538508981 | 300 | 6 | 11 | 30.1 | TDD | 411 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3255688 | 3 | 121.4687768523 | 31.1507181340 | 136 | 13 | 11 | 45.6 | TDD | 74 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |

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
| 2024-09-20 22:21:30.905 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.920 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.041 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.041 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.760 | NREventA3 | measId:2;ServCellPCI:301;Se... |
| 2024-09-20 22:21:38.000 | NRHandoverAttempt | SourcePCI:301;SourceNR-ARFC... |
| 2024-09-20 22:21:38.040 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.052 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.166 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.166 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3228959 | 1 | 19.9112 | 17.2964 | -115.5847 | 19.7022 | 175.5461 | 0.0029 | 0.0009 |
| 2024_09_20 22:00 | 3219648 | 2 | 87.5333 | 87.4315 | -115.4723 | 18.7500 | 82.4734 | 0.0102 | 0.0168 |
| 2024_09_20 22:00 | 3255688 | 3 | 18.7725 | 5.9065 | -117.7111 | 18.4146 | 197.4762 | 0.0024 | 0.0088 |
| 2024_09_20 22:00 | 3231396 | 4 | 12.3326 | 14.9954 | -115.6138 | 17.2981 | 87.4281 | 0.0126 | 0.0157 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414699_E45FEFEC | 504990 | 281 | -92.3 | 504990 | 74 | -96.8 | 504990 | 656 | -102.9 | 504990 | 411 |
| MR_1774414699_4D13A767 | 504990 | 281 | -92.4 | 504990 | 74 | -96.3 | 504990 | 656 | -102.9 | 504990 | 411 |
| MR_1774414699_57E56193 | 504990 | 281 | -89.7 | 504990 | 74 | -96.0 | 504990 | 656 | -103.2 | 504990 | 411 |
| MR_1774414699_106BE2BA | 504990 | 281 | -93.1 | 504990 | 74 | -96.4 | 504990 | 656 | -100.6 | 504990 | 411 |
| MR_1774414699_04563748 | 504990 | 281 | -93.3 | 504990 | 74 | -96.6 | 504990 | 656 | -100.8 | 504990 | 411 |
| MR_1774414699_FFF8951F | 504990 | 281 | -92.8 | 504990 | 74 | -97.4 | 504990 | 656 | -100.8 | 504990 | 411 |
| MR_1774414699_A96F05F4 | 504990 | 281 | -89.9 | 504990 | 74 | -99.7 | 504990 | 656 | -103.0 | 504990 | 411 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 192: `55b007b6-72a...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `55b007b6-72a8-4e63-a44a-172fd77d470f` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[192] topology](images/test_0192.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3269504_2
- `C2`: Check test server and transmission issues
- `C3`: Adjust the azimuth of 3211857_1 by 5 degrees
- `C4`: Increase A3 Offset threshold for 3269504_2
- `C5`: Add neighbor relationship between 3214647_3 and 3269504_2
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3269504_2
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3269504_2
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3211857_1
- `C9`: Add neighbor relationship between 3211857_1 and 3269504_2
- `C10`: Insufficient data; more data is needed for judgment.
- `C11`: Press down the tilt angle of 3211857_1 by 2 degrees
- `C12`: Lift the tilt angle of 3211857_1 by 2 degrees
- `C13`: Decrease transmission power for 3211857_1
- `C14`: Lift the tilt angle  of 3269504_2 by 1 degrees
- `C15`: Increase transmission power for 3211857_1
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3211857_1
- `C17`: Increase A3 Offset threshold for 3211857_1
- `C18`: Adjust the azimuth of 3269504_2 by 50 degrees
- `C19`: Decrease A3 Offset threshold for 3269504_2
- `C20`: Decrease A3 Offset threshold for 3211857_1
- `C21`: Press down the tilt angle  of 3269504_2 by 1 degrees
- `C22`: Increase transmission power for 3269504_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.781 | MS1 | 121.4656648354 | 31.1446207833 | 91 | 504990 | -86.58 | 13.21 | 382.17 | 0.02 | 2.77 | 1568 |
| 2024-09-20 22:21:32.397 | MS1 | 121.4656737551 | 31.1446345930 | 91 | 504990 | -90.43 | 16.28 | 358.36 | 0.07 | 2.22 | 1590 |
| 2024-09-20 22:21:33.618 | MS1 | 121.4656729513 | 31.1446321874 | 91 | 504990 | -90.16 | 14.67 | 550.12 | 0.12 | 2.58 | 1570 |
| 2024-09-20 22:21:34.535 | MS1 | 121.4656626289 | 31.1446253065 | 91 | 504990 | -85.23 | 15.15 | 77.63 | 0.66 | 2.08 | 607 |
| 2024-09-20 22:21:35.746 | MS1 | 121.4656663070 | 31.1446302428 | 91 | 504990 | -89.71 | 13.10 | 68.36 | 0.64 | 2.85 | 675 |
| 2024-09-20 22:21:36.724 | MS1 | 121.4656654125 | 31.1446190931 | 91 | 504990 | -88.10 | 17.44 | 83.53 | 0.51 | 2.84 | 555 |
| 2024-09-20 22:21:37.133 | MS1 | 121.4656732906 | 31.1446263822 | 91 | 504990 | -91.18 | 10.07 | 83.49 | 0.57 | 2.98 | 653 |
| 2024-09-20 22:21:38.292 | MS1 | 121.4656611940 | 31.1446251170 | 91 | 504990 | -93.68 | 9.26 | 52.21 | 0.50 | 2.61 | 640 |
| 2024-09-20 22:21:39.819 | MS1 | 121.4656586341 | 31.1446189384 | 91 | 504990 | -90.89 | 7.19 | 54.19 | 0.52 | 2.78 | 579 |
| 2024-09-20 22:21:40.375 | MS1 | 121.4656776047 | 31.1446300028 | 91 | 504990 | -90.46 | 7.59 | 481.76 | 0.13 | 2.88 | 1562 |
| 2024-09-20 22:21:41.734 | MS1 | 121.4656705848 | 31.1446255145 | 91 | 504990 | -92.15 | 11.18 | 428.61 | 0.10 | 2.68 | 1564 |
| 2024-09-20 22:21:42.130 | MS1 | 121.4656648539 | 31.1446269717 | 91 | 504990 | -93.94 | 9.02 | 454.48 | 0.04 | 2.33 | 1577 |

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
| 3211857 | 1 | 121.4652213046 | 31.1532944614 | 173 | 1 | 11 | 17.0 | TDD | 91 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3214647 | 3 | 121.4758600509 | 31.1488665638 | 74 | 6 | 1 | 36.7 | TDD | 590 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3223689 | 4 | 121.4730958080 | 31.1555587119 | 353 | 8 | 10 | 30.1 | TDD | 967 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3269504 | 2 | 121.4759297537 | 31.1559225897 | 286 | 0 | 6 | 29.9 | TDD | 124 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |

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
| 2024-09-20 22:21:31.476 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.496 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.642 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.642 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.279 | NREventA3 | measId:2;ServCellPCI:595;Se... |
| 2024-09-20 22:21:38.519 | NRHandoverAttempt | SourcePCI:595;SourceNR-ARFC... |
| 2024-09-20 22:21:38.556 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.570 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.683 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.683 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3211857 | 1 | 9.6272 | 12.5094 | -114.4568 | 9.3900 | 92.4619 | 0.0142 | 0.0140 |
| 2024_09_20 22:00 | 3269504 | 2 | 13.0199 | 16.5874 | -115.3885 | 19.0233 | 188.7890 | 0.0133 | 0.0135 |
| 2024_09_20 22:00 | 3214647 | 3 | 17.8048 | 18.6008 | -116.7915 | 9.1838 | 99.5263 | 0.0105 | 0.0160 |
| 2024_09_20 22:00 | 3223689 | 4 | 8.6365 | 19.1467 | -114.3549 | 15.9431 | 117.3035 | 0.0069 | 0.0095 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415101_7DDAD583 | 504990 | 91 | -83.4 | 504990 | 124 | -89.7 | 504990 | 590 | -98.0 | 504990 | 967 |
| MR_1774415101_DD047218 | 504990 | 91 | -83.3 | 504990 | 124 | -90.8 | 504990 | 590 | -98.2 | 504990 | 967 |
| MR_1774415101_C605063A | 504990 | 91 | -85.0 | 504990 | 124 | -90.8 | 504990 | 590 | -98.7 | 504990 | 967 |
| MR_1774415101_BE751ACD | 504990 | 91 | -85.1 | 504990 | 124 | -91.3 | 504990 | 590 | -96.9 | 504990 | 967 |
| MR_1774415101_A2848738 | 504990 | 91 | -84.1 | 504990 | 124 | -90.6 | 504990 | 590 | -99.7 | 504990 | 967 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 193: `c83b850c-7c2...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `c83b850c-7c2a-4f65-8c32-b35e6a00b61e` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[193] topology](images/test_0193.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3240705_4
- `C2`: Add neighbor relationship between 3240705_4 and 3211792_2
- `C3`: Lift the tilt angle of 3240705_4 by 6 degrees
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3240705_4
- `C5`: Increase A3 Offset threshold for 3211792_2
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3211792_2
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3240705_4
- `C8`: Adjust the azimuth of 3217364_3 by 50 degrees
- `C9`: Add neighbor relationship between 3217364_3 and 3211792_2
- `C10`: Decrease A3 Offset threshold for 3240705_4
- `C11`: Increase transmission power for 3211792_2
- `C12`: Press down the tilt angle of 3240705_4 by 6 degrees
- `C13`: Increase A3 Offset threshold for 3240705_4
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Press down the tilt angle  of 3217364_3 by 10 degrees
- `C16`: Adjust the azimuth of 3240705_4 by 24 degrees
- `C17`: Decrease A3 Offset threshold for 3211792_2
- `C18`: Decrease transmission power for 3240705_4
- `C19`: Lift the tilt angle  of 3217364_3 by 10 degrees
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3211792_2
- `C21`: Check test server and transmission issues
- `C22`: Decrease transmission power for 3211792_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.965 | MS1 | 121.4656753379 | 31.1446303444 | 143 | 504990 | -89.26 | 14.10 | 455.40 | 0.15 | 2.98 | 1580 |
| 2024-09-20 22:21:32.402 | MS1 | 121.4656769538 | 31.1446224082 | 143 | 504990 | -85.43 | 13.31 | 497.80 | 0.20 | 2.96 | 1592 |
| 2024-09-20 22:21:33.275 | MS1 | 121.4656645351 | 31.1446278544 | 143 | 504990 | -91.79 | 14.18 | 516.64 | 0.19 | 2.04 | 1577 |
| 2024-09-20 22:21:34.198 | MS1 | 121.4656614356 | 31.1446318041 | 143 | 504990 | -89.98 | 15.29 | 103.65 | 0.04 | 2.10 | 1584 |
| 2024-09-20 22:21:35.791 | MS1 | 121.4656657161 | 31.1446272894 | 143 | 504990 | -87.89 | 17.65 | 91.87 | 0.04 | 2.73 | 1600 |
| 2024-09-20 22:21:36.912 | MS1 | 121.4656768341 | 31.1446299370 | 143 | 504990 | -89.82 | 12.26 | 70.59 | 0.06 | 2.59 | 1560 |
| 2024-09-20 22:21:37.289 | MS1 | 121.4656664073 | 31.1446332419 | 143 | 504990 | -91.32 | 10.00 | 93.52 | 0.17 | 2.59 | 1600 |
| 2024-09-20 22:21:38.471 | MS1 | 121.4656673488 | 31.1446204240 | 143 | 504990 | -93.39 | 7.34 | 56.99 | 0.09 | 2.15 | 1584 |
| 2024-09-20 22:21:39.317 | MS1 | 121.4656757560 | 31.1446237622 | 143 | 504990 | -89.74 | 12.12 | 106.02 | 0.16 | 2.33 | 1583 |
| 2024-09-20 22:21:40.901 | MS1 | 121.4656636174 | 31.1446272626 | 143 | 504990 | -92.85 | 12.31 | 306.16 | 0.11 | 2.15 | 1592 |
| 2024-09-20 22:21:41.144 | MS1 | 121.4656602465 | 31.1446288133 | 143 | 504990 | -92.81 | 9.00 | 327.75 | 0.06 | 2.96 | 1580 |
| 2024-09-20 22:21:42.104 | MS1 | 121.4656616624 | 31.1446317019 | 143 | 504990 | -91.10 | 12.22 | 550.18 | 0.12 | 2.94 | 1599 |

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
| 3211792 | 2 | 121.4655536677 | 31.1498046628 | 62 | 9 | 9 | 48.3 | TDD | 483 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3217364 | 3 | 121.4691627207 | 31.1487993905 | 322 | 7 | 7 | 16.6 | TDD | 237 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3220685 | 1 | 121.4681103699 | 31.1452048346 | 319 | 0 | 8 | 28.5 | TDD | 848 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3240705 | 4 | 121.4681881794 | 31.1556022929 | 215 | 4 | 2 | 42.9 | TDD | 143 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:31.198 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.218 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.330 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.330 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.033 | NREventA3 | measId:2;ServCellPCI:983;Se... |
| 2024-09-20 22:21:38.273 | NRHandoverAttempt | SourcePCI:983;SourceNR-ARFC... |
| 2024-09-20 22:21:38.317 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.327 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.461 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.461 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3220685 | 1 | 10.0003 | 11.6912 | -115.8583 | 7.1555 | 132.7942 | 0.0053 | 0.0053 |
| 2024_09_20 22:00 | 3211792 | 2 | 18.0910 | 10.1583 | -116.1473 | 12.0097 | 120.8790 | 0.0062 | 0.0035 |
| 2024_09_20 22:00 | 3217364 | 3 | 12.7069 | 17.0030 | -114.1401 | 9.6706 | 192.4363 | 0.0144 | 0.0187 |
| 2024_09_20 22:00 | 3240705 | 4 | 80.3165 | 84.0113 | -115.1071 | 19.1449 | 114.2567 | 0.0022 | 0.0002 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412399_98B19FB0 | 504990 | 143 | -88.8 | 504990 | 483 | -95.8 | 504990 | 237 | -95.8 | 504990 | 848 |
| MR_1774412399_E2858639 | 504990 | 143 | -87.0 | 504990 | 483 | -95.8 | 504990 | 237 | -95.7 | 504990 | 848 |
| MR_1774412399_D955F71A | 504990 | 143 | -87.2 | 504990 | 483 | -95.7 | 504990 | 237 | -96.0 | 504990 | 848 |
| MR_1774412399_80D80EA0 | 504990 | 143 | -88.7 | 504990 | 483 | -98.5 | 504990 | 237 | -98.6 | 504990 | 848 |
| MR_1774412399_4A026B3C | 504990 | 143 | -89.6 | 504990 | 483 | -96.7 | 504990 | 237 | -96.3 | 504990 | 848 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 194: `9baf6d46-290...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `9baf6d46-2902-43fb-bc48-8740c8877b1e` |
| Tag | **multiple-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[194] topology](images/test_0194.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 5 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 5개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3239110_1
- `C2`: Increase A3 Offset threshold for 3239110_1
- `C3`: Adjust the azimuth of 3239110_1 by 30 degrees
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3239110_1
- `C5`: Increase transmission power for 3239110_1
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3260376_3
- `C7`: Insufficient data; more data is needed for judgment.
- `C8`: Press down the tilt angle  of 3260376_3 by 5 degrees
- `C9`: Lift the tilt angle  of 3260376_3 by 5 degrees
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3239110_1
- `C11`: Add neighbor relationship between 3273332_2 and 3260376_3
- `C12`: Check test server and transmission issues
- `C13`: Decrease A3 Offset threshold for 3260376_3
- `C14`: Decrease transmission power for 3260376_3
- `C15`: Increase A3 Offset threshold for 3260376_3
- `C16`: Press down the tilt angle of 3239110_1 by 5 degrees
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3260376_3
- `C18`: Decrease A3 Offset threshold for 3239110_1
- `C19`: Lift the tilt angle of 3239110_1 by 5 degrees
- `C20`: Increase transmission power for 3260376_3
- `C21`: Adjust the azimuth of 3260376_3 by 24 degrees
- `C22`: Add neighbor relationship between 3239110_1 and 3260376_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.868 | MS1 | 121.4656595488 | 31.1446215557 | 5 | 504990 | -76.08 | 16.63 | 368.88 | 0.07 | 2.18 | 1565 |
| 2024-09-20 22:21:32.471 | MS1 | 121.4656597150 | 31.1446230526 | 5 | 504990 | -80.40 | 14.08 | 510.80 | 0.11 | 2.24 | 1591 |
| 2024-09-20 22:21:33.606 | MS1 | 121.4656591574 | 31.1446351860 | 5 | 504990 | -78.89 | 14.45 | 511.26 | 0.12 | 2.70 | 1572 |
| 2024-09-20 22:21:34.486 | MS1 | 121.4656734673 | 31.1446280108 | 952 | 504990 | -80.78 | 4.05 | 42.16 | 0.10 | 1.23 | 1599 |
| 2024-09-20 22:21:35.119 | MS1 | 121.4656620953 | 31.1446184460 | 952 | 504990 | -89.23 | 1.32 | 36.92 | 0.15 | 1.09 | 1596 |
| 2024-09-20 22:21:36.947 | MS1 | 121.4656674005 | 31.1446188637 | 5 | 504990 | -88.72 | 3.62 | 56.78 | 0.14 | 1.16 | 1582 |
| 2024-09-20 22:21:37.772 | MS1 | 121.4656708789 | 31.1446310505 | 5 | 504990 | -87.85 | 4.08 | 78.24 | 0.04 | 1.35 | 1563 |
| 2024-09-20 22:21:38.242 | MS1 | 121.4656695345 | 31.1446363851 | 952 | 504990 | -86.52 | 1.95 | 38.05 | 0.08 | 1.35 | 1575 |
| 2024-09-20 22:21:39.374 | MS1 | 121.4656622731 | 31.1446262819 | 952 | 504990 | -88.76 | 3.91 | 36.84 | 0.16 | 1.43 | 1582 |
| 2024-09-20 22:21:40.604 | MS1 | 121.4656779458 | 31.1446190104 | 952 | 504990 | -78.82 | 15.03 | 534.21 | 0.15 | 2.80 | 1565 |
| 2024-09-20 22:21:41.880 | MS1 | 121.4656629755 | 31.1446205239 | 952 | 504990 | -77.86 | 17.73 | 577.27 | 0.13 | 2.66 | 1597 |
| 2024-09-20 22:21:42.716 | MS1 | 121.4656669308 | 31.1446208787 | 952 | 504990 | -75.75 | 17.16 | 374.67 | 0.03 | 2.68 | 1573 |

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
| 3239110 | 1 | 121.4718768163 | 31.1526659428 | 243 | 4 | 2 | 24.9 | TDD | 5 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3254400 | 4 | 121.4677261057 | 31.1446605740 | 220 | 3 | 10 | 25.9 | TDD | 952 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3260376 | 3 | 121.4726104909 | 31.1529710011 | 191 | 3 | 8 | 49.3 | TDD | 719 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3263332 | 5 | 121.4714461644 | 31.1529664117 | 117 | 2 | 12 | 27.9 | TDD | 348 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3273332 | 2 | 121.4739211976 | 31.1478947765 | 166 | 7 | 0 | 22.9 | TDD | 967 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:31.601 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.617 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.742 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.742 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.460 | NREventA3 | measId:2;ServCellPCI:543;Se... |
| 2024-09-20 22:21:34.700 | NRHandoverAttempt | SourcePCI:543;SourceNR-ARFC... |
| 2024-09-20 22:21:34.730 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:34.740 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:34.855 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:34.855 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:36.460 | NREventA3 | measId:2;ServCellPCI:594;Se... |
| 2024-09-20 22:21:36.700 | NRHandoverAttempt | SourcePCI:594;SourceNR-ARFC... |
| 2024-09-20 22:21:36.738 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:36.753 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:36.902 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.902 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.460 | NREventA3 | measId:2;ServCellPCI:543;Se... |
| 2024-09-20 22:21:38.700 | NRHandoverAttempt | SourcePCI:543;SourceNR-ARFC... |
| 2024-09-20 22:21:38.739 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.752 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.893 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.893 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3239110 | 1 | 15.4413 | 16.9235 | -116.1343 | 15.8394 | 190.7090 | 0.0027 | 0.0001 |
| 2024_09_20 22:00 | 3273332 | 2 | 11.2570 | 17.1738 | -114.4247 | 14.5360 | 192.6682 | 0.0187 | 0.0178 |
| 2024_09_20 22:00 | 3260376 | 3 | 13.6817 | 6.4752 | -115.7124 | 12.4862 | 138.7669 | 0.0191 | 0.0109 |
| 2024_09_20 22:00 | 3254400 | 4 | 19.8301 | 12.2686 | -114.0740 | 18.3309 | 85.0203 | 0.0079 | 0.0147 |
| 2024_09_20 22:00 | 3263332 | 5 | 17.9978 | 18.4956 | -114.0401 | 15.2103 | 199.3165 | 0.0012 | 0.0071 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417022_23B4FFBE | 504990 | 5 | -82.5 | 504990 | 952 | -80.8 | 504990 | 719 | -85.1 | 504990 | 967 |
| MR_1774417022_B85E78FA | 504990 | 5 | -78.9 | 504990 | 952 | -77.4 | 504990 | 719 | -85.2 | 504990 | 967 |
| MR_1774417022_9D90C490 | 504990 | 952 | -80.0 | 504990 | 5 | -81.3 | 504990 | 719 | -85.9 | 504990 | 967 |
| MR_1774417022_19D96576 | 504990 | 5 | -81.7 | 504990 | 952 | -78.0 | 504990 | 719 | -86.1 | 504990 | 967 |
| MR_1774417022_4F1DAFC8 | 504990 | 5 | -80.2 | 504990 | 952 | -79.2 | 504990 | 719 | -85.0 | 504990 | 967 |
| MR_1774417022_A033AABB | 504990 | 952 | -81.1 | 504990 | 5 | -79.1 | 504990 | 719 | -83.4 | 504990 | 967 |
| MR_1774417022_FE636F63 | 504990 | 5 | -80.7 | 504990 | 952 | -78.7 | 504990 | 719 | -85.2 | 504990 | 967 |
| MR_1774417022_6499ADDC | 504990 | 952 | -82.5 | 504990 | 5 | -79.7 | 504990 | 719 | -83.1 | 504990 | 967 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 195: `af52175e-56f...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `af52175e-56f4-49be-a86b-7764d2982e1a` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[195] topology](images/test_0195.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3214928_2 by 9 degrees
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3214928_2
- `C3`: Adjust the azimuth of 3214928_2 by 50 degrees
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3214928_2
- `C5`: Decrease transmission power for 3238102_4
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3238102_4
- `C7`: Decrease A3 Offset threshold for 3238102_4
- `C8`: Press down the tilt angle of 3214928_2 by 9 degrees
- `C9`: Check test server and transmission issues
- `C10`: Decrease transmission power for 3214928_2
- `C11`: Lift the tilt angle  of 3238102_4 by 4 degrees
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3238102_4
- `C13`: Decrease A3 Offset threshold for 3214928_2
- `C14`: Add neighbor relationship between 3245489_1 and 3238102_4
- `C15`: Press down the tilt angle  of 3238102_4 by 4 degrees
- `C16`: Increase A3 Offset threshold for 3214928_2
- `C17`: Add neighbor relationship between 3214928_2 and 3238102_4
- `C18`: Increase transmission power for 3214928_2
- `C19`: Increase A3 Offset threshold for 3238102_4
- `C20`: Insufficient data; more data is needed for judgment.
- `C21`: Adjust the azimuth of 3238102_4 by 50 degrees
- `C22`: Increase transmission power for 3238102_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.801 | MS1 | 121.4656607383 | 31.1446242966 | 147 | 504990 | -89.69 | 15.45 | 476.84 | 0.07 | 2.63 | 1567 |
| 2024-09-20 22:21:32.893 | MS1 | 121.4656675517 | 31.1446355837 | 147 | 504990 | -91.31 | 13.59 | 585.74 | 0.17 | 2.18 | 1581 |
| 2024-09-20 22:21:33.636 | MS1 | 121.4656717789 | 31.1446372840 | 147 | 504990 | -87.09 | 16.06 | 365.12 | 0.10 | 2.81 | 1599 |
| 2024-09-20 22:21:34.487 | MS1 | 121.4656774549 | 31.1446260424 | 147 | 504990 | -87.25 | 13.77 | 76.62 | 0.05 | 2.10 | 1578 |
| 2024-09-20 22:21:35.689 | MS1 | 121.4656604625 | 31.1446323565 | 147 | 504990 | -85.02 | 14.20 | 67.21 | 0.02 | 2.49 | 1582 |
| 2024-09-20 22:21:36.966 | MS1 | 121.4656607040 | 31.1446339325 | 147 | 504990 | -88.36 | 14.00 | 53.94 | 0.07 | 2.54 | 1563 |
| 2024-09-20 22:21:37.223 | MS1 | 121.4656741817 | 31.1446361166 | 147 | 504990 | -91.46 | 10.04 | 90.25 | 0.20 | 2.19 | 1564 |
| 2024-09-20 22:21:38.177 | MS1 | 121.4656689632 | 31.1446341231 | 147 | 504990 | -90.52 | 12.54 | 48.23 | 0.14 | 2.83 | 1588 |
| 2024-09-20 22:21:39.839 | MS1 | 121.4656642501 | 31.1446338243 | 147 | 504990 | -90.80 | 7.98 | 94.50 | 0.15 | 2.93 | 1560 |
| 2024-09-20 22:21:40.846 | MS1 | 121.4656623468 | 31.1446283551 | 147 | 504990 | -93.75 | 12.29 | 384.38 | 0.11 | 2.06 | 1579 |
| 2024-09-20 22:21:41.169 | MS1 | 121.4656745274 | 31.1446300787 | 147 | 504990 | -89.98 | 8.63 | 345.52 | 0.09 | 2.53 | 1582 |
| 2024-09-20 22:21:42.426 | MS1 | 121.4656742551 | 31.1446256960 | 147 | 504990 | -90.61 | 9.49 | 449.90 | 0.13 | 2.21 | 1576 |

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
| 3214928 | 2 | 121.4647617594 | 31.1548037625 | 303 | 7 | 8 | 45.1 | TDD | 147 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3238102 | 4 | 121.4742697814 | 31.1544617271 | 35 | 3 | 5 | 24.4 | TDD | 957 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3245489 | 1 | 121.4743425935 | 31.1475310397 | 125 | 2 | 11 | 38.7 | TDD | 777 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3274376 | 3 | 121.4677733292 | 31.1466291475 | 186 | 4 | 11 | 44.6 | TDD | 541 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:30.990 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.015 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.146 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.146 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.836 | NREventA3 | measId:2;ServCellPCI:844;Se... |
| 2024-09-20 22:21:38.076 | NRHandoverAttempt | SourcePCI:844;SourceNR-ARFC... |
| 2024-09-20 22:21:38.107 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.117 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.223 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.223 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3245489 | 1 | 89.1131 | 76.5579 | -114.8160 | 18.5081 | 185.9157 | 0.0007 | 0.0028 |
| 2024_09_19 22:00 | 3214928 | 2 | 84.2563 | 87.7422 | -116.4073 | 11.8803 | 149.9678 | 0.0179 | 0.0046 |
| 2024_09_19 22:00 | 3274376 | 3 | 92.4290 | 77.2866 | -116.6345 | 11.2723 | 145.3385 | 0.0031 | 0.0144 |
| 2024_09_19 22:00 | 3238102 | 4 | 88.4710 | 75.6152 | -116.1547 | 7.6835 | 123.4085 | 0.0053 | 0.0003 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416401_8542A9D7 | 504990 | 147 | -85.9 | 504990 | 957 | -88.7 | 504990 | 777 | -101.0 | 504990 | 541 |
| MR_1774416401_A601FDF5 | 504990 | 147 | -85.5 | 504990 | 957 | -89.5 | 504990 | 777 | -100.0 | 504990 | 541 |
| MR_1774416401_F7704CCE | 504990 | 147 | -88.5 | 504990 | 957 | -89.5 | 504990 | 777 | -100.4 | 504990 | 541 |
| MR_1774416401_6DD4E8E3 | 504990 | 147 | -87.4 | 504990 | 957 | -87.7 | 504990 | 777 | -97.5 | 504990 | 541 |
| MR_1774416401_21A5539A | 504990 | 147 | -88.6 | 504990 | 957 | -87.9 | 504990 | 777 | -99.8 | 504990 | 541 |
| MR_1774416401_1473AE81 | 504990 | 147 | -85.7 | 504990 | 957 | -90.6 | 504990 | 777 | -99.6 | 504990 | 541 |
| MR_1774416401_EC5A9F7B | 504990 | 147 | -85.8 | 504990 | 957 | -90.6 | 504990 | 777 | -97.3 | 504990 | 541 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 196: `9c32f53f-622...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `9c32f53f-622a-4877-a9c8-d030850278c0` |
| Tag | **multiple-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[196] topology](images/test_0196.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3239206_1 and 3210458_4
- `C2`: Add neighbor relationship between 3239754_2 and 3210458_4
- `C3`: Press down the tilt angle of 3239206_1 by 6 degrees
- `C4`: Increase A3 Offset threshold for 3210458_4
- `C5`: Decrease transmission power for 3210458_4
- `C6`: Adjust the azimuth of 3239206_1 by 24 degrees
- `C7`: Check test server and transmission issues
- `C8`: Insufficient data; more data is needed for judgment.
- `C9`: Adjust the azimuth of 3210458_4 by 12 degrees
- `C10`: Decrease A3 Offset threshold for 3210458_4
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3239206_1
- `C12`: Increase A3 Offset threshold for 3239206_1
- `C13`: Lift the tilt angle  of 3210458_4 by 5 degrees
- `C14`: Decrease A3 Offset threshold for 3239206_1
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3210458_4
- `C16`: Increase transmission power for 3210458_4
- `C17`: Increase transmission power for 3239206_1
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3210458_4
- `C19`: Press down the tilt angle  of 3210458_4 by 5 degrees
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3239206_1
- `C21`: Lift the tilt angle of 3239206_1 by 6 degrees
- `C22`: Decrease transmission power for 3239206_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.181 | MS1 | 121.4656686987 | 31.1446225505 | 667 | 504990 | -84.07 | 17.01 | 571.89 | 0.08 | 2.18 | 1592 |
| 2024-09-20 22:21:32.502 | MS1 | 121.4656687363 | 31.1446207314 | 667 | 504990 | -80.73 | 12.92 | 312.75 | 0.10 | 2.80 | 1565 |
| 2024-09-20 22:21:33.537 | MS1 | 121.4656626557 | 31.1446370890 | 667 | 504990 | -84.46 | 15.66 | 313.89 | 0.09 | 2.71 | 1569 |
| 2024-09-20 22:21:34.135 | MS1 | 121.4656773085 | 31.1446197875 | 667 | 504990 | -88.20 | 3.21 | 87.64 | 0.02 | 1.23 | 1582 |
| 2024-09-20 22:21:35.484 | MS1 | 121.4656661499 | 31.1446288993 | 667 | 504990 | -87.93 | 3.57 | 85.72 | 0.10 | 1.34 | 1583 |
| 2024-09-20 22:21:36.450 | MS1 | 121.4656663309 | 31.1446295325 | 667 | 504990 | -86.82 | 1.62 | 58.90 | 0.12 | 1.41 | 1570 |
| 2024-09-20 22:21:37.896 | MS1 | 121.4656628601 | 31.1446355613 | 667 | 504990 | -93.01 | 0.62 | 66.74 | 0.01 | 1.05 | 1585 |
| 2024-09-20 22:21:38.769 | MS1 | 121.4656640200 | 31.1446184895 | 667 | 504990 | -94.16 | 2.61 | 62.30 | 0.06 | 1.49 | 1568 |
| 2024-09-20 22:21:39.282 | MS1 | 121.4656693160 | 31.1446247573 | 667 | 504990 | -85.52 | 2.31 | 52.90 | 0.02 | 1.49 | 1560 |
| 2024-09-20 22:21:40.309 | MS1 | 121.4656739971 | 31.1446319101 | 667 | 504990 | -81.33 | 13.02 | 386.89 | 0.15 | 2.01 | 1587 |
| 2024-09-20 22:21:41.165 | MS1 | 121.4656582777 | 31.1446277976 | 667 | 504990 | -78.61 | 12.64 | 527.16 | 0.08 | 2.66 | 1580 |
| 2024-09-20 22:21:42.421 | MS1 | 121.4656708379 | 31.1446313588 | 667 | 504990 | -75.16 | 12.79 | 511.97 | 0.11 | 2.62 | 1581 |

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
| 3210458 | 4 | 121.4749571580 | 31.1525919388 | 213 | 3 | 12 | 36.7 | TDD | 84 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3239206 | 1 | 121.4734242156 | 31.1535828967 | 241 | 4 | 11 | 38.4 | TDD | 667 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3239754 | 2 | 121.4657066043 | 31.1475042146 | 202 | 4 | 12 | 24.5 | TDD | 676 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3268078 | 3 | 121.4676976849 | 31.1447854856 | 311 | 0 | 6 | 42.9 | TDD | 229 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:31.571 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.590 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.724 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.724 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3239206 | 1 | 11.8611 | 18.5644 | -109.4953 | 18.6313 | 171.0871 | 0.0130 | 0.0085 |
| 2024_09_20 22:00 | 3239754 | 2 | 15.8305 | 14.1646 | -114.2833 | 17.6752 | 149.0896 | 0.0152 | 0.0076 |
| 2024_09_20 22:00 | 3268078 | 3 | 11.5796 | 7.1383 | -116.5957 | 8.0789 | 83.3501 | 0.0086 | 0.0049 |
| 2024_09_20 22:00 | 3210458 | 4 | 16.4950 | 10.9800 | -114.4243 | 14.8919 | 108.3708 | 0.0092 | 0.0066 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413397_6A8CF1DC | 504990 | 667 | -88.4 | 504990 | 84 | -89.8 | 504990 | 676 | -89.6 | 504990 | 229 |
| MR_1774413397_FF2AC97C | 504990 | 84 | -89.5 | 504990 | 667 | -90.6 | 504990 | 676 | -91.2 | 504990 | 229 |
| MR_1774413397_44D19450 | 504990 | 667 | -86.3 | 504990 | 84 | -91.2 | 504990 | 676 | -90.1 | 504990 | 229 |
| MR_1774413397_EDA6B89E | 504990 | 667 | -90.2 | 504990 | 84 | -89.3 | 504990 | 676 | -92.1 | 504990 | 229 |
| MR_1774413397_9CC8BAC8 | 504990 | 84 | -86.7 | 504990 | 667 | -88.6 | 504990 | 676 | -89.9 | 504990 | 229 |
| MR_1774413397_4B026747 | 504990 | 667 | -88.5 | 504990 | 84 | -88.1 | 504990 | 676 | -91.7 | 504990 | 229 |
| MR_1774413397_85B1BA81 | 504990 | 667 | -87.0 | 504990 | 84 | -89.7 | 504990 | 676 | -89.3 | 504990 | 229 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 197: `b6462848-e14...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `b6462848-e146-4d07-8940-6c0b215d2ca0` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[197] topology](images/test_0197.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3253536_2 and 3242181_1
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3242181_1
- `C3`: Press down the tilt angle of 3253536_2 by 2 degrees
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3253536_2
- `C5`: Decrease A3 Offset threshold for 3242181_1
- `C6`: Press down the tilt angle  of 3242181_1 by 10 degrees
- `C7`: Adjust the azimuth of 3253536_2 by 4 degrees
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3253536_2
- `C9`: Decrease transmission power for 3253536_2
- `C10`: Increase transmission power for 3242181_1
- `C11`: Increase A3 Offset threshold for 3242181_1
- `C12`: Lift the tilt angle of 3253536_2 by 2 degrees
- `C13`: Decrease transmission power for 3242181_1
- `C14`: Adjust the azimuth of 3242181_1 by 50 degrees
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3242181_1
- `C16`: Increase transmission power for 3253536_2
- `C17`: Insufficient data; more data is needed for judgment.
- `C18`: Lift the tilt angle  of 3242181_1 by 10 degrees
- `C19`: Add neighbor relationship between 3254811_4 and 3242181_1
- `C20`: Increase A3 Offset threshold for 3253536_2
- `C21`: Check test server and transmission issues
- `C22`: Decrease A3 Offset threshold for 3253536_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.790 | MS1 | 121.4656611214 | 31.1446323535 | 938 | 504990 | -86.39 | 13.77 | 398.58 | 0.14 | 2.61 | 1573 |
| 2024-09-20 22:21:32.664 | MS1 | 121.4656687622 | 31.1446304853 | 938 | 504990 | -85.53 | 16.43 | 449.44 | 0.19 | 2.70 | 1566 |
| 2024-09-20 22:21:33.953 | MS1 | 121.4656685410 | 31.1446217743 | 938 | 504990 | -89.54 | 14.64 | 417.94 | 0.03 | 2.10 | 1585 |
| 2024-09-20 22:21:34.726 | MS1 | 121.4656632822 | 31.1446209950 | 938 | 504990 | -90.29 | 14.63 | 48.50 | 0.53 | 2.06 | 520 |
| 2024-09-20 22:21:35.959 | MS1 | 121.4656704842 | 31.1446362262 | 938 | 504990 | -85.57 | 16.04 | 64.55 | 0.64 | 2.25 | 590 |
| 2024-09-20 22:21:36.828 | MS1 | 121.4656761170 | 31.1446358098 | 938 | 504990 | -89.80 | 15.82 | 82.91 | 0.61 | 2.74 | 521 |
| 2024-09-20 22:21:37.949 | MS1 | 121.4656611756 | 31.1446365019 | 938 | 504990 | -92.60 | 10.40 | 71.49 | 0.60 | 2.83 | 678 |
| 2024-09-20 22:21:38.166 | MS1 | 121.4656694264 | 31.1446256341 | 938 | 504990 | -92.10 | 7.85 | 57.24 | 0.51 | 2.67 | 610 |
| 2024-09-20 22:21:39.878 | MS1 | 121.4656700256 | 31.1446330443 | 938 | 504990 | -90.65 | 7.55 | 57.17 | 0.62 | 2.06 | 619 |
| 2024-09-20 22:21:40.973 | MS1 | 121.4656645916 | 31.1446274860 | 938 | 504990 | -89.47 | 9.36 | 462.35 | 0.08 | 2.05 | 1600 |
| 2024-09-20 22:21:41.861 | MS1 | 121.4656704969 | 31.1446264962 | 938 | 504990 | -93.73 | 12.22 | 294.31 | 0.04 | 2.86 | 1574 |
| 2024-09-20 22:21:42.836 | MS1 | 121.4656597580 | 31.1446354186 | 938 | 504990 | -90.57 | 12.93 | 607.00 | 0.15 | 2.76 | 1575 |

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
| 3216024 | 3 | 121.4707161077 | 31.1554374792 | 141 | 4 | 3 | 32.0 | TDD | 765 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3242181 | 1 | 121.4641981160 | 31.1556204230 | 57 | 12 | 2 | 20.3 | TDD | 769 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3253536 | 2 | 121.4742810155 | 31.1502121431 | 229 | 1 | 8 | 18.9 | TDD | 938 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3254811 | 4 | 121.4746023718 | 31.1470249772 | 142 | 1 | 6 | 22.4 | TDD | 410 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:31.055 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.075 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.192 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.192 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.867 | NREventA3 | measId:2;ServCellPCI:905;Se... |
| 2024-09-20 22:21:38.107 | NRHandoverAttempt | SourcePCI:905;SourceNR-ARFC... |
| 2024-09-20 22:21:38.141 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.152 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.257 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.257 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3242181 | 1 | 19.7858 | 13.2958 | -116.0528 | 11.2632 | 127.5509 | 0.0196 | 0.0066 |
| 2024_09_20 22:00 | 3253536 | 2 | 5.5590 | 8.2486 | -115.6000 | 10.6005 | 139.2250 | 0.0140 | 0.0141 |
| 2024_09_20 22:00 | 3216024 | 3 | 15.7500 | 7.7841 | -114.2712 | 19.7704 | 98.6785 | 0.0015 | 0.0054 |
| 2024_09_20 22:00 | 3254811 | 4 | 9.0390 | 13.5838 | -115.3713 | 11.8851 | 141.4778 | 0.0054 | 0.0087 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774411997_6BD1FF2D | 504990 | 938 | -90.2 | 504990 | 769 | -99.4 | 504990 | 410 | -104.0 | 504990 | 765 |
| MR_1774411997_8B062511 | 504990 | 938 | -91.8 | 504990 | 769 | -100.1 | 504990 | 410 | -103.5 | 504990 | 765 |
| MR_1774411997_F33ED323 | 504990 | 938 | -90.5 | 504990 | 769 | -97.9 | 504990 | 410 | -102.0 | 504990 | 765 |
| MR_1774411997_B5BB4B44 | 504990 | 938 | -91.6 | 504990 | 769 | -99.4 | 504990 | 410 | -101.1 | 504990 | 765 |
| MR_1774411997_7FC97379 | 504990 | 938 | -92.2 | 504990 | 769 | -99.1 | 504990 | 410 | -103.9 | 504990 | 765 |
| MR_1774411997_B53F3DA7 | 504990 | 938 | -90.4 | 504990 | 769 | -100.3 | 504990 | 410 | -102.7 | 504990 | 765 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 198: `4a7d1ec9-3ce...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `4a7d1ec9-3ce0-45e3-a499-fa32a4e36e0e` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[198] topology](images/test_0198.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3262308_3
- `C2`: Adjust the azimuth of 3262636_2 by 50 degrees
- `C3`: Press down the tilt angle of 3262308_3 by 10 degrees
- `C4`: Increase A3 Offset threshold for 3262308_3
- `C5`: Lift the tilt angle of 3262308_3 by 10 degrees
- `C6`: Check test server and transmission issues
- `C7`: Increase transmission power for 3262308_3
- `C8`: Decrease A3 Offset threshold for 3262636_2
- `C9`: Insufficient data; more data is needed for judgment.
- `C10`: Decrease transmission power for 3262308_3
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3262636_2
- `C12`: Lift the tilt angle  of 3262636_2 by 9 degrees
- `C13`: Decrease A3 Offset threshold for 3262308_3
- `C14`: Press down the tilt angle  of 3262636_2 by 9 degrees
- `C15`: Increase A3 Offset threshold for 3262636_2
- `C16`: Adjust the azimuth of 3262308_3 by 50 degrees
- `C17`: Add neighbor relationship between 3247682_1 and 3262636_2
- `C18`: Increase transmission power for 3262636_2
- `C19`: Add neighbor relationship between 3262308_3 and 3262636_2
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3262308_3
- `C21`: Decrease transmission power for 3262636_2
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3262636_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.297 | MS1 | 121.4656692952 | 31.1446324375 | 87 | 504990 | -90.72 | 15.27 | 369.52 | 0.04 | 2.87 | 1585 |
| 2024-09-20 22:21:32.535 | MS1 | 121.4656658089 | 31.1446215222 | 87 | 504990 | -86.28 | 17.17 | 577.61 | 0.03 | 2.60 | 1574 |
| 2024-09-20 22:21:33.208 | MS1 | 121.4656596502 | 31.1446286066 | 87 | 504990 | -87.35 | 14.57 | 330.83 | 0.02 | 2.66 | 1562 |
| 2024-09-20 22:21:34.966 | MS1 | 121.4656603969 | 31.1446213897 | 87 | 504990 | -87.99 | 12.32 | 48.89 | 0.01 | 2.10 | 1574 |
| 2024-09-20 22:21:35.723 | MS1 | 121.4656661456 | 31.1446295225 | 87 | 504990 | -87.53 | 12.63 | 80.96 | 0.08 | 2.20 | 1580 |
| 2024-09-20 22:21:36.961 | MS1 | 121.4656725272 | 31.1446342408 | 87 | 504990 | -86.26 | 13.85 | 77.09 | 0.11 | 2.57 | 1570 |
| 2024-09-20 22:21:37.504 | MS1 | 121.4656750199 | 31.1446235261 | 87 | 504990 | -92.79 | 8.49 | 103.50 | 0.04 | 2.37 | 1562 |
| 2024-09-20 22:21:38.997 | MS1 | 121.4656778620 | 31.1446198847 | 87 | 504990 | -92.69 | 8.61 | 52.36 | 0.07 | 2.18 | 1566 |
| 2024-09-20 22:21:39.881 | MS1 | 121.4656696564 | 31.1446373502 | 87 | 504990 | -93.13 | 9.83 | 84.08 | 0.05 | 2.29 | 1586 |
| 2024-09-20 22:21:40.264 | MS1 | 121.4656697044 | 31.1446249877 | 87 | 504990 | -93.87 | 8.85 | 555.76 | 0.18 | 2.43 | 1582 |
| 2024-09-20 22:21:41.658 | MS1 | 121.4656582031 | 31.1446270412 | 87 | 504990 | -89.52 | 10.77 | 340.08 | 0.10 | 2.61 | 1564 |
| 2024-09-20 22:21:42.329 | MS1 | 121.4656657652 | 31.1446226106 | 87 | 504990 | -91.37 | 12.79 | 522.36 | 0.09 | 2.06 | 1596 |

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
| 3223195 | 4 | 121.4722424448 | 31.1500649726 | 282 | 7 | 11 | 29.8 | TDD | 511 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3247682 | 1 | 121.4680649997 | 31.1502316994 | 91 | 4 | 12 | 19.7 | TDD | 281 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3262308 | 3 | 121.4691197750 | 31.1507769928 | 290 | 7 | 0 | 35.0 | TDD | 87 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3262636 | 2 | 121.4725289821 | 31.1481513480 | 53 | 7 | 6 | 28.7 | TDD | 418 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |

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
| 2024-09-20 22:21:30.919 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.938 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.066 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.066 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.795 | NREventA3 | measId:2;ServCellPCI:489;Se... |
| 2024-09-20 22:21:38.035 | NRHandoverAttempt | SourcePCI:489;SourceNR-ARFC... |
| 2024-09-20 22:21:38.072 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.083 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.219 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.219 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3247682 | 1 | 90.9219 | 76.9799 | -117.0741 | 15.0650 | 133.2069 | 0.0079 | 0.0104 |
| 2024_09_19 22:00 | 3262636 | 2 | 81.0110 | 92.5931 | -115.5927 | 19.9017 | 121.3571 | 0.0028 | 0.0137 |
| 2024_09_19 22:00 | 3262308 | 3 | 90.9132 | 77.6715 | -116.7887 | 10.8875 | 87.5274 | 0.0040 | 0.0042 |
| 2024_09_19 22:00 | 3223195 | 4 | 89.5851 | 82.2173 | -116.8476 | 9.5513 | 148.1843 | 0.0096 | 0.0002 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412741_A53C5096 | 504990 | 87 | -88.7 | 504990 | 418 | -91.0 | 504990 | 281 | -101.8 | 504990 | 511 |
| MR_1774412741_075788C8 | 504990 | 87 | -89.5 | 504990 | 418 | -92.9 | 504990 | 281 | -101.0 | 504990 | 511 |
| MR_1774412741_33AD42DD | 504990 | 87 | -87.3 | 504990 | 418 | -92.8 | 504990 | 281 | -101.3 | 504990 | 511 |
| MR_1774412741_06720B1F | 504990 | 87 | -86.7 | 504990 | 418 | -92.7 | 504990 | 281 | -101.2 | 504990 | 511 |
| MR_1774412741_E3F3045C | 504990 | 87 | -88.5 | 504990 | 418 | -94.5 | 504990 | 281 | -100.5 | 504990 | 511 |
| MR_1774412741_AB1D74FA | 504990 | 87 | -89.9 | 504990 | 418 | -93.0 | 504990 | 281 | -102.1 | 504990 | 511 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 199: `256b3278-305...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `256b3278-3058-4017-8fe9-524e795a347f` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[199] topology](images/test_0199.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3279915_3
- `C2`: Press down the tilt angle  of 3279915_3 by 2 degrees
- `C3`: Decrease transmission power for 3261393_2
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3261393_2
- `C5`: Press down the tilt angle of 3261393_2 by 8 degrees
- `C6`: Add neighbor relationship between 3261393_2 and 3279915_3
- `C7`: Lift the tilt angle  of 3279915_3 by 2 degrees
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3279915_3
- `C9`: Lift the tilt angle of 3261393_2 by 8 degrees
- `C10`: Decrease transmission power for 3279915_3
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3261393_2
- `C12`: Adjust the azimuth of 3279915_3 by 46 degrees
- `C13`: Add neighbor relationship between 3249792_4 and 3279915_3
- `C14`: Decrease A3 Offset threshold for 3261393_2
- `C15`: Increase transmission power for 3261393_2
- `C16`: Insufficient data; more data is needed for judgment.
- `C17`: Adjust the azimuth of 3261393_2 by 50 degrees
- `C18`: Check test server and transmission issues
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3279915_3
- `C20`: Increase A3 Offset threshold for 3261393_2
- `C21`: Increase A3 Offset threshold for 3279915_3
- `C22`: Decrease A3 Offset threshold for 3279915_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.788 | MS1 | 121.4656778487 | 31.1446261995 | 201 | 504990 | -80.38 | 13.32 | 530.12 | 0.01 | 2.86 | 1580 |
| 2024-09-20 22:21:32.363 | MS1 | 121.4656592939 | 31.1446208036 | 201 | 504990 | -78.88 | 13.98 | 372.97 | 0.11 | 2.98 | 1587 |
| 2024-09-20 22:21:33.441 | MS1 | 121.4656609786 | 31.1446367736 | 201 | 504990 | -76.14 | 15.26 | 408.03 | 0.01 | 2.31 | 1596 |
| 2024-09-20 22:21:34.709 | MS1 | 121.4656778195 | 31.1446300840 | 201 | 504990 | -92.36 | -3.42 | 55.78 | 0.02 | 1.26 | 1595 |
| 2024-09-20 22:21:35.648 | MS1 | 121.4656639491 | 31.1446193927 | 201 | 504990 | -91.96 | -0.58 | 72.54 | 0.13 | 1.33 | 1594 |
| 2024-09-20 22:21:36.622 | MS1 | 121.4656698414 | 31.1446245607 | 201 | 504990 | -85.35 | -0.54 | 42.50 | 0.15 | 1.44 | 1577 |
| 2024-09-20 22:21:37.751 | MS1 | 121.4656756274 | 31.1446327176 | 201 | 504990 | -93.00 | -2.27 | 32.60 | 0.18 | 1.43 | 1570 |
| 2024-09-20 22:21:38.248 | MS1 | 121.4656739449 | 31.1446336330 | 201 | 504990 | -82.09 | 12.52 | 494.54 | 0.04 | 1.38 | 1578 |
| 2024-09-20 22:21:39.254 | MS1 | 121.4656763422 | 31.1446377125 | 201 | 504990 | -83.80 | 12.95 | 324.98 | 0.11 | 1.41 | 1577 |
| 2024-09-20 22:21:40.949 | MS1 | 121.4656765052 | 31.1446264491 | 201 | 504990 | -78.59 | 12.72 | 351.31 | 0.19 | 2.94 | 1575 |
| 2024-09-20 22:21:41.557 | MS1 | 121.4656713171 | 31.1446355446 | 201 | 504990 | -82.67 | 16.90 | 553.86 | 0.06 | 2.83 | 1584 |
| 2024-09-20 22:21:42.742 | MS1 | 121.4656704714 | 31.1446202325 | 201 | 504990 | -83.36 | 16.42 | 526.81 | 0.16 | 2.27 | 1562 |

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
| 3249792 | 4 | 121.4736901705 | 31.1454141795 | 112 | 14 | 9 | 24.3 | TDD | 57 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3260958 | 1 | 121.4706587311 | 31.1527655487 | 255 | 9 | 1 | 21.7 | TDD | 256 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3261393 | 2 | 121.4646809971 | 31.1491238202 | 343 | 6 | 5 | 16.7 | TDD | 201 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3279915 | 3 | 121.4711995431 | 31.1554666053 | 250 | 0 | 2 | 40.6 | TDD | 524 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |

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
| 2024-09-20 22:21:31.211 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.233 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.354 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.354 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.026 | NREventA3 | measId:2;ServCellPCI:598;Se... |
| 2024-09-20 22:21:36.026 | NREventA3 | measId:2;ServCellPCI:598;Se... |
| 2024-09-20 22:21:37.026 | NREventA3 | measId:2;ServCellPCI:598;Se... |
| 2024-09-20 22:21:39.526 | NRRRCReestablishAttempt | PCI:598 |
| 2024-09-20 22:21:39.538 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.552 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:39.699 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.699 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3260958 | 1 | 10.0410 | 7.7887 | -115.2488 | 19.3111 | 131.1105 | 0.0106 | 0.0138 |
| 2024_09_20 22:00 | 3261393 | 2 | 13.1521 | 13.6780 | -114.6134 | 11.9682 | 117.0886 | 0.0092 | 0.1680 |
| 2024_09_20 22:00 | 3279915 | 3 | 12.4146 | 11.6940 | -116.2957 | 5.3952 | 117.8677 | 0.0119 | 0.0027 |
| 2024_09_20 22:00 | 3249792 | 4 | 13.2544 | 6.2991 | -117.5383 | 12.7095 | 178.6086 | 0.0147 | 0.0174 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413408_18B7FCD0 | 504990 | 524 | -87.3 | 504990 | 201 | -91.6 | 504990 | 57 | -88.0 | 504990 | 256 |
| MR_1774413408_D3506EF2 | 504990 | 524 | -87.3 | 504990 | 201 | -91.2 | 504990 | 57 | -86.4 | 504990 | 256 |
| MR_1774413408_F1534263 | 504990 | 201 | -90.5 | 504990 | 524 | -86.7 | 504990 | 57 | -89.1 | 504990 | 256 |
| MR_1774413408_A1088B8C | 504990 | 524 | -85.8 | 504990 | 201 | -90.5 | 504990 | 57 | -88.4 | 504990 | 256 |
| MR_1774413408_6DF689DD | 504990 | 201 | -92.7 | 504990 | 524 | -88.5 | 504990 | 57 | -89.8 | 504990 | 256 |

> *... 2개 열 생략 (전체 14열)*

---
