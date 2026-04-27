# Track A 문제 분석 — train[610]~train[619]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[610] ~ train[619] (10개)

## 목차

1. [문제 610: `dd080c4f-7bd...`](#610) — single-answer, 정답: C14
2. [문제 611: `6bf7d884-28f...`](#611) — single-answer, 정답: C11
3. [문제 612: `f9fd5881-811...`](#612) — single-answer, 정답: C6
4. [문제 613: `f1a1ac88-53b...`](#613) — single-answer, 정답: C22
5. [문제 614: `957ca21b-ee4...`](#614) — single-answer, 정답: C9
6. [문제 615: `d2f48ebf-f9f...`](#615) — single-answer, 정답: C8
7. [문제 616: `765b22db-dc4...`](#616) — single-answer, 정답: C7
8. [문제 617: `1f1e827f-68a...`](#617) — single-answer, 정답: C15
9. [문제 618: `12c457c6-be3...`](#618) — single-answer, 정답: C21
10. [문제 619: `cb605c80-a0c...`](#619) — single-answer, 정답: C19

---

### 문제 610: `dd080c4f-7bd...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `dd080c4f-7bdb-4200-b4b3-d427876b6a14` |
| Tag | **single-answer** |
| 정답 | **C14** |
| C14 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[610] topology](images/train_0610.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3212273_2
- `C2`: Increase transmission power for 3258068_4
- `C3`: Increase transmission power for 3212273_2
- `C4`: Check test server and transmission issues
- `C5`: Add neighbor relationship between 3212273_2 and 3258068_4
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3258068_4
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3212273_2
- `C8`: Lift the tilt angle  of 3258068_4 by 10 degrees
- `C9`: Lift the tilt angle of 3212273_2 by 8 degrees
- `C10`: Decrease A3 Offset threshold for 3258068_4
- `C11`: Decrease transmission power for 3258068_4
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3258068_4
- `C13`: Adjust the azimuth of 3212273_2 by 50 degrees
- `C14`: Insufficient data; more data is needed for judgment. **← 정답**
- `C15`: Increase A3 Offset threshold for 3212273_2
- `C16`: Press down the tilt angle  of 3258068_4 by 10 degrees
- `C17`: Decrease transmission power for 3212273_2
- `C18`: Decrease A3 Offset threshold for 3212273_2
- `C19`: Adjust the azimuth of 3258068_4 by 50 degrees
- `C20`: Press down the tilt angle of 3212273_2 by 8 degrees
- `C21`: Increase A3 Offset threshold for 3258068_4
- `C22`: Add neighbor relationship between 3262573_3 and 3258068_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.753 | MS1 | 121.4656677116 | 31.1446326695 | 781 | 504990 | -90.94 | 12.60 | 372.12 | 0.03 | 2.32 | 1569 |
| 2024-09-20 22:21:32.608 | MS1 | 121.4656727580 | 31.1446238892 | 781 | 504990 | -87.13 | 13.50 | 517.78 | 0.00 | 2.93 | 1589 |
| 2024-09-20 22:21:33.777 | MS1 | 121.4656597750 | 31.1446260634 | 781 | 504990 | -89.70 | 17.07 | 307.62 | 0.18 | 2.57 | 1595 |
| 2024-09-20 22:21:34.871 | MS1 | 121.4656684619 | 31.1446294284 | 781 | 504990 | -89.80 | 17.67 | 62.18 | 0.15 | 2.72 | 1562 |
| 2024-09-20 22:21:35.312 | MS1 | 121.4656764637 | 31.1446241759 | 781 | 504990 | -85.59 | 13.45 | 98.56 | 0.04 | 2.95 | 1600 |
| 2024-09-20 22:21:36.413 | MS1 | 121.4656632330 | 31.1446266202 | 781 | 504990 | -88.66 | 13.72 | 85.41 | 0.06 | 2.66 | 1600 |
| 2024-09-20 22:21:37.155 | MS1 | 121.4656616636 | 31.1446193729 | 781 | 504990 | -90.53 | 7.06 | 73.66 | 0.06 | 2.89 | 1591 |
| 2024-09-20 22:21:38.960 | MS1 | 121.4656626898 | 31.1446310463 | 781 | 504990 | -93.52 | 8.43 | 51.98 | 0.10 | 2.21 | 1600 |
| 2024-09-20 22:21:39.783 | MS1 | 121.4656669124 | 31.1446198271 | 781 | 504990 | -90.75 | 8.04 | 82.97 | 0.03 | 2.24 | 1593 |
| 2024-09-20 22:21:40.832 | MS1 | 121.4656737977 | 31.1446322003 | 781 | 504990 | -93.88 | 11.52 | 504.49 | 0.11 | 2.66 | 1600 |
| 2024-09-20 22:21:41.944 | MS1 | 121.4656582068 | 31.1446350413 | 781 | 504990 | -93.94 | 11.78 | 551.10 | 0.10 | 2.94 | 1586 |
| 2024-09-20 22:21:42.181 | MS1 | 121.4656753921 | 31.1446326686 | 781 | 504990 | -92.51 | 8.69 | 479.33 | 0.16 | 2.32 | 1569 |

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
| 3212273 | 2 | 121.4758982449 | 31.1545259131 | 166 | 6 | 8 | 39.4 | TDD | 781 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3235840 | 1 | 121.4650997254 | 31.1509889788 | 1 | 0 | 3 | 20.0 | TDD | 314 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3258068 | 4 | 121.4707661157 | 31.1528285370 | 156 | 10 | 10 | 33.4 | TDD | 189 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3262573 | 3 | 121.4748494978 | 31.1496023890 | 281 | 13 | 8 | 23.8 | TDD | 581 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |

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
| 2024-09-20 22:21:31.072 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.091 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.241 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.241 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.894 | NREventA3 | measId:2;ServCellPCI:72;Ser... |
| 2024-09-20 22:21:38.134 | NRHandoverAttempt | SourcePCI:72;SourceNR-ARFCN... |
| 2024-09-20 22:21:38.170 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.185 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.332 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.332 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3235840 | 1 | 92.0479 | 91.3432 | -117.2720 | 10.4729 | 145.1834 | 0.0084 | 0.0194 |
| 2024_09_19 22:00 | 3212273 | 2 | 88.6076 | 81.8897 | -117.1943 | 16.7420 | 173.1959 | 0.0035 | 0.0086 |
| 2024_09_19 22:00 | 3262573 | 3 | 83.2537 | 89.2249 | -115.9244 | 6.9063 | 124.7057 | 0.0116 | 0.0066 |
| 2024_09_19 22:00 | 3258068 | 4 | 81.3542 | 90.6135 | -117.2889 | 13.7942 | 115.2868 | 0.0069 | 0.0106 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416128_416BD3DA | 504990 | 781 | -88.0 | 504990 | 189 | -95.9 | 504990 | 581 | -101.3 | 504990 | 314 |
| MR_1774416128_F38DBF8C | 504990 | 781 | -90.1 | 504990 | 189 | -95.6 | 504990 | 581 | -101.1 | 504990 | 314 |
| MR_1774416128_40A357E6 | 504990 | 781 | -89.3 | 504990 | 189 | -98.8 | 504990 | 581 | -99.9 | 504990 | 314 |
| MR_1774416128_90310289 | 504990 | 781 | -90.9 | 504990 | 189 | -97.2 | 504990 | 581 | -98.9 | 504990 | 314 |
| MR_1774416128_F7A49EFE | 504990 | 781 | -89.2 | 504990 | 189 | -95.7 | 504990 | 581 | -98.7 | 504990 | 314 |
| MR_1774416128_2DF21C05 | 504990 | 781 | -88.4 | 504990 | 189 | -97.2 | 504990 | 581 | -98.9 | 504990 | 314 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 611: `6bf7d884-28f...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `6bf7d884-28f7-4a11-a522-d81edfcb399d` |
| Tag | **single-answer** |
| 정답 | **C11** |
| C11 의미 | Add neighbor relationship between 3226933_3 and 3229498_1 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[611] topology](images/train_0611.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3229498_1 by 27 degrees
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3226933_3
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3229498_1
- `C4`: Press down the tilt angle of 3226933_3 by 5 degrees
- `C5`: Press down the tilt angle  of 3229498_1 by 5 degrees
- `C6`: Adjust the azimuth of 3226933_3 by 50 degrees
- `C7`: Lift the tilt angle  of 3229498_1 by 5 degrees
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3229498_1
- `C9`: Increase A3 Offset threshold for 3229498_1
- `C10`: Add neighbor relationship between 3255033_2 and 3229498_1
- `C11`: Add neighbor relationship between 3226933_3 and 3229498_1 **← 정답**
- `C12`: Insufficient data; more data is needed for judgment.
- `C13`: Decrease A3 Offset threshold for 3226933_3
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3226933_3
- `C15`: Decrease transmission power for 3226933_3
- `C16`: Check test server and transmission issues
- `C17`: Decrease A3 Offset threshold for 3229498_1
- `C18`: Lift the tilt angle of 3226933_3 by 5 degrees
- `C19`: Increase A3 Offset threshold for 3226933_3
- `C20`: Decrease transmission power for 3229498_1
- `C21`: Increase transmission power for 3226933_3
- `C22`: Increase transmission power for 3229498_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.704 | MS1 | 121.4656674028 | 31.1446279250 | 322 | 504990 | -78.74 | 15.26 | 565.25 | 0.16 | 2.25 | 1596 |
| 2024-09-20 22:21:32.886 | MS1 | 121.4656677459 | 31.1446242256 | 322 | 504990 | -79.46 | 13.73 | 409.93 | 0.03 | 2.08 | 1600 |
| 2024-09-20 22:21:33.477 | MS1 | 121.4656717388 | 31.1446181967 | 322 | 504990 | -80.42 | 14.97 | 405.27 | 0.10 | 2.43 | 1585 |
| 2024-09-20 22:21:34.587 | MS1 | 121.4656594944 | 31.1446197633 | 322 | 504990 | -88.69 | -0.34 | 48.47 | 0.06 | 1.14 | 1590 |
| 2024-09-20 22:21:35.746 | MS1 | 121.4656658758 | 31.1446186739 | 322 | 504990 | -93.69 | -0.58 | 37.75 | 0.11 | 1.12 | 1582 |
| 2024-09-20 22:21:36.759 | MS1 | 121.4656719547 | 31.1446302103 | 322 | 504990 | -85.15 | -1.21 | 47.87 | 0.04 | 1.28 | 1586 |
| 2024-09-20 22:21:37.970 | MS1 | 121.4656743943 | 31.1446280465 | 322 | 504990 | -90.61 | -1.62 | 58.07 | 0.16 | 1.24 | 1578 |
| 2024-09-20 22:21:38.623 | MS1 | 121.4656606355 | 31.1446319374 | 322 | 504990 | -83.93 | 16.43 | 397.15 | 0.09 | 1.12 | 1589 |
| 2024-09-20 22:21:39.492 | MS1 | 121.4656660225 | 31.1446356166 | 322 | 504990 | -77.24 | 17.20 | 475.11 | 0.08 | 1.45 | 1581 |
| 2024-09-20 22:21:40.348 | MS1 | 121.4656670396 | 31.1446213080 | 322 | 504990 | -79.23 | 12.17 | 429.78 | 0.00 | 2.60 | 1587 |
| 2024-09-20 22:21:41.956 | MS1 | 121.4656708591 | 31.1446291553 | 322 | 504990 | -78.24 | 13.98 | 345.01 | 0.13 | 2.44 | 1583 |
| 2024-09-20 22:21:42.295 | MS1 | 121.4656772494 | 31.1446338838 | 322 | 504990 | -77.78 | 13.95 | 432.56 | 0.17 | 2.27 | 1572 |

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
| 3224271 | 4 | 121.4674817262 | 31.1454765332 | 217 | 11 | 12 | 39.1 | TDD | 655 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3226933 | 3 | 121.4650170830 | 31.1482597321 | 303 | 1 | 2 | 30.3 | TDD | 322 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3229498 | 1 | 121.4737115029 | 31.1442140321 | 246 | 3 | 2 | 22.1 | TDD | 416 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3255033 | 2 | 121.4711145134 | 31.1440045117 | 213 | 3 | 5 | 49.0 | TDD | 593 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |

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
| 2024-09-20 22:21:30.822 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.838 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:30.972 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.972 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.688 | NREventA3 | measId:2;ServCellPCI:981;Se... |
| 2024-09-20 22:21:35.688 | NREventA3 | measId:2;ServCellPCI:981;Se... |
| 2024-09-20 22:21:36.688 | NREventA3 | measId:2;ServCellPCI:981;Se... |
| 2024-09-20 22:21:39.188 | NRRRCReestablishAttempt | PCI:981 |
| 2024-09-20 22:21:39.201 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.216 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:39.354 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.354 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3229498 | 1 | 13.9688 | 17.9456 | -115.3952 | 17.9299 | 86.7039 | 0.0008 | 0.0052 |
| 2024_09_20 22:00 | 3255033 | 2 | 19.1513 | 18.7501 | -116.1880 | 15.8337 | 164.9208 | 0.0120 | 0.0163 |
| 2024_09_20 22:00 | 3226933 | 3 | 5.4870 | 19.4436 | -115.3278 | 17.6333 | 141.6236 | 0.0065 | 0.1905 |
| 2024_09_20 22:00 | 3224271 | 4 | 19.6665 | 7.7535 | -114.6398 | 9.7622 | 134.8048 | 0.0096 | 0.0157 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415898_5065386B | 504990 | 322 | -86.8 | 504990 | 416 | -86.5 | 504990 | 593 | -87.3 | 504990 | 655 |
| MR_1774415898_1208170D | 504990 | 416 | -86.3 | 504990 | 322 | -88.5 | 504990 | 593 | -85.5 | 504990 | 655 |
| MR_1774415898_EEB1BFFE | 504990 | 322 | -87.9 | 504990 | 416 | -84.9 | 504990 | 593 | -85.6 | 504990 | 655 |
| MR_1774415898_F231F570 | 504990 | 322 | -89.4 | 504990 | 416 | -86.4 | 504990 | 593 | -84.8 | 504990 | 655 |
| MR_1774415898_3CA3FAB7 | 504990 | 322 | -86.9 | 504990 | 416 | -85.6 | 504990 | 593 | -86.7 | 504990 | 655 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 612: `f9fd5881-811...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `f9fd5881-8114-4d8a-ae46-1d2f9353c1df` |
| Tag | **single-answer** |
| 정답 | **C6** |
| C6 의미 | Decrease A3 Offset threshold for 3212633_3 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[612] topology](images/train_0612.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3212633_3 and 3253083_4
- `C2`: Increase A3 Offset threshold for 3212633_3
- `C3`: Decrease A3 Offset threshold for 3253083_4
- `C4`: Insufficient data; more data is needed for judgment.
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3253083_4
- `C6`: Decrease A3 Offset threshold for 3212633_3 **← 정답**
- `C7`: Decrease transmission power for 3253083_4
- `C8`: Increase transmission power for 3253083_4
- `C9`: Adjust the azimuth of 3253083_4 by 11 degrees
- `C10`: Adjust the azimuth of 3212633_3 by 50 degrees
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3212633_3
- `C12`: Increase A3 Offset threshold for 3253083_4
- `C13`: Lift the tilt angle of 3212633_3 by 10 degrees
- `C14`: Press down the tilt angle  of 3253083_4 by 6 degrees
- `C15`: Lift the tilt angle  of 3253083_4 by 6 degrees
- `C16`: Press down the tilt angle of 3212633_3 by 10 degrees
- `C17`: Check test server and transmission issues
- `C18`: Decrease transmission power for 3212633_3
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3253083_4
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3212633_3
- `C21`: Increase transmission power for 3212633_3
- `C22`: Add neighbor relationship between 3262351_2 and 3253083_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.487 | MS1 | 121.4656743074 | 31.1446350112 | 148 | 504990 | -79.67 | 13.95 | 583.08 | 0.11 | 2.45 | 1570 |
| 2024-09-20 22:21:32.459 | MS1 | 121.4656639272 | 31.1446308630 | 148 | 504990 | -82.99 | 16.23 | 429.98 | 0.08 | 2.05 | 1580 |
| 2024-09-20 22:21:33.418 | MS1 | 121.4656661720 | 31.1446286870 | 148 | 504990 | -82.75 | 15.85 | 491.68 | 0.02 | 2.36 | 1597 |
| 2024-09-20 22:21:34.455 | MS1 | 121.4656632362 | 31.1446186838 | 148 | 504990 | -90.82 | -3.27 | 44.91 | 0.18 | 1.40 | 1589 |
| 2024-09-20 22:21:35.161 | MS1 | 121.4656754806 | 31.1446237210 | 148 | 504990 | -83.65 | -1.40 | 32.96 | 0.15 | 1.41 | 1582 |
| 2024-09-20 22:21:36.181 | MS1 | 121.4656673221 | 31.1446212526 | 148 | 504990 | -89.42 | -3.71 | 66.16 | 0.15 | 1.29 | 1586 |
| 2024-09-20 22:21:37.331 | MS1 | 121.4656672291 | 31.1446264864 | 148 | 504990 | -89.45 | -2.64 | 42.72 | 0.03 | 1.23 | 1576 |
| 2024-09-20 22:21:38.217 | MS1 | 121.4656747913 | 31.1446327441 | 148 | 504990 | -89.21 | -1.57 | 71.37 | 0.13 | 1.35 | 1582 |
| 2024-09-20 22:21:39.346 | MS1 | 121.4656682021 | 31.1446208225 | 46 | 504990 | -80.73 | 12.90 | 174.03 | 0.12 | 1.15 | 1592 |
| 2024-09-20 22:21:40.793 | MS1 | 121.4656769175 | 31.1446195418 | 46 | 504990 | -82.31 | 14.67 | 543.58 | 0.04 | 2.02 | 1576 |
| 2024-09-20 22:21:41.923 | MS1 | 121.4656778577 | 31.1446289450 | 46 | 504990 | -81.09 | 16.58 | 529.51 | 0.13 | 2.22 | 1567 |
| 2024-09-20 22:21:42.635 | MS1 | 121.4656758444 | 31.1446260725 | 46 | 504990 | -83.39 | 13.28 | 348.65 | 0.11 | 2.36 | 1592 |

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
| 3212633 | 3 | 121.4650905801 | 31.1491364569 | 40 | 15 | 5 | 33.4 | TDD | 148 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3253083 | 4 | 121.4693469799 | 31.1468518855 | 246 | 1 | 2 | 36.8 | TDD | 46 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3262351 | 2 | 121.4651466496 | 31.1519999360 | 56 | 12 | 5 | 43.9 | TDD | 651 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3275833 | 1 | 121.4734181692 | 31.1508212870 | 174 | 12 | 3 | 48.8 | TDD | 936 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:31.206 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.221 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.363 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.363 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.007 | NREventA3 | measId:2;ServCellPCI:280;Se... |
| 2024-09-20 22:21:38.247 | NRHandoverAttempt | SourcePCI:280;SourceNR-ARFC... |
| 2024-09-20 22:21:38.292 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.306 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.432 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.432 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3275833 | 1 | 7.7675 | 6.6297 | -114.0283 | 5.7474 | 98.5786 | 0.0117 | 0.0048 |
| 2024_09_20 22:00 | 3262351 | 2 | 13.9744 | 11.5124 | -116.6240 | 10.9884 | 80.7386 | 0.0189 | 0.0071 |
| 2024_09_20 22:00 | 3212633 | 3 | 14.7646 | 15.8346 | -114.2094 | 15.3792 | 109.1559 | 0.0094 | 0.1696 |
| 2024_09_20 22:00 | 3253083 | 4 | 17.3136 | 16.6550 | -117.4156 | 13.0387 | 107.2219 | 0.0161 | 0.0098 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415840_BE198062 | 504990 | 148 | -88.8 | 504990 | 46 | -84.8 | 504990 | 651 | -87.0 | 504990 | 936 |
| MR_1774415840_29A4E743 | 504990 | 148 | -91.0 | 504990 | 46 | -84.6 | 504990 | 651 | -89.7 | 504990 | 936 |
| MR_1774415840_D6EA4A91 | 504990 | 148 | -92.1 | 504990 | 46 | -83.9 | 504990 | 651 | -87.3 | 504990 | 936 |
| MR_1774415840_FBCE537C | 504990 | 148 | -91.6 | 504990 | 46 | -87.8 | 504990 | 651 | -88.5 | 504990 | 936 |
| MR_1774415840_376142C9 | 504990 | 148 | -91.7 | 504990 | 46 | -86.4 | 504990 | 651 | -86.3 | 504990 | 936 |
| MR_1774415840_19D5BFD8 | 504990 | 46 | -86.1 | 504990 | 148 | -89.1 | 504990 | 651 | -86.5 | 504990 | 936 |
| MR_1774415840_447007A3 | 504990 | 148 | -91.2 | 504990 | 46 | -84.5 | 504990 | 651 | -89.8 | 504990 | 936 |
| MR_1774415840_C05BC573 | 504990 | 148 | -90.3 | 504990 | 46 | -86.2 | 504990 | 651 | -87.3 | 504990 | 936 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 613: `f1a1ac88-53b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `f1a1ac88-53bf-4c0e-9723-761411acb488` |
| Tag | **single-answer** |
| 정답 | **C22** |
| C22 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3277679_6 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[613] topology](images/train_0613.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment.
- `C2`: Decrease transmission power for 3277679_6
- `C3`: Adjust the azimuth of 3277679_6 by 11 degrees
- `C4`: Add neighbor relationship between 3236468_10 and 3224949_2
- `C5`: Increase A3 Offset threshold for 3277679_6
- `C6`: Press down the tilt angle  of 3224949_2 by 6 degrees
- `C7`: Increase A3 Offset threshold for 3224949_2
- `C8`: Add neighbor relationship between 3277679_6 and 3224949_2
- `C9`: Press down the tilt angle of 3277679_6 by 6 degrees
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3224949_2
- `C11`: Decrease A3 Offset threshold for 3224949_2
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3224949_2
- `C13`: Increase transmission power for 3277679_6
- `C14`: Increase transmission power for 3224949_2
- `C15`: Decrease A3 Offset threshold for 3277679_6
- `C16`: Decrease transmission power for 3224949_2
- `C17`: Lift the tilt angle of 3277679_6 by 6 degrees
- `C18`: Check test server and transmission issues
- `C19`: Lift the tilt angle  of 3224949_2 by 6 degrees
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3277679_6
- `C21`: Adjust the azimuth of 3224949_2 by 1 degrees
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3277679_6 **← 정답**

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.756 | MS1 | 121.4656656152 | 31.1446308069 | 248 | 504990 | -95.92 | 9.38 | 492.20 | 0.09 | 2.45 | 1571 |
| 2024-09-20 22:21:32.964 | MS1 | 121.4656663134 | 31.1446234767 | 300 | 504990 | -95.40 | 10.06 | 540.66 | 0.02 | 2.46 | 1594 |
| 2024-09-20 22:21:33.965 | MS1 | 121.4656605844 | 31.1446198433 | 617 | 504990 | -94.72 | 11.28 | 313.85 | 0.03 | 2.11 | 1600 |
| 2024-09-20 22:21:34.667 | MS1 | 121.4656624719 | 31.1446262937 | 205 | 152650 | -88.97 | 3.87 | 67.55 | 0.04 | 1.73 | 931 |
| 2024-09-20 22:21:35.577 | MS1 | 121.4656704253 | 31.1446191137 | 186 | 152650 | -96.00 | 6.36 | 76.78 | 0.16 | 1.65 | 968 |
| 2024-09-20 22:21:36.998 | MS1 | 121.4656612423 | 31.1446376277 | 570 | 152650 | -88.60 | 3.68 | 63.10 | 0.04 | 1.95 | 935 |
| 2024-09-20 22:21:37.545 | MS1 | 121.4656695219 | 31.1446376615 | 69 | 152650 | -89.50 | 2.49 | 77.56 | 0.11 | 1.83 | 937 |
| 2024-09-20 22:21:38.781 | MS1 | 121.4656738946 | 31.1446223697 | 205 | 152650 | -92.66 | 3.91 | 72.59 | 0.13 | 1.80 | 974 |
| 2024-09-20 22:21:39.490 | MS1 | 121.4656587192 | 31.1446338110 | 186 | 152650 | -92.38 | 2.22 | 74.73 | 0.11 | 1.80 | 987 |
| 2024-09-20 22:21:40.115 | MS1 | 121.4656702822 | 31.1446343681 | 570 | 152650 | -89.16 | 5.44 | 83.07 | 0.15 | 2.77 | 1562 |
| 2024-09-20 22:21:41.860 | MS1 | 121.4656749535 | 31.1446269131 | 69 | 152650 | -90.05 | 6.67 | 88.47 | 0.09 | 2.12 | 1561 |
| 2024-09-20 22:21:42.221 | MS1 | 121.4656754617 | 31.1446362289 | 205 | 152650 | -92.30 | 5.63 | 58.64 | 0.15 | 2.88 | 1568 |

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
| 3210246 | 7 | 121.4640376088 | 31.1527017773 | 150 | 2 | 4 | 7.8 | FDD | 69 | n1 | 152650 | 30M | 4T4R | 12 | 152650 |
| 3213384 | 13 | 121.4654680647 | 31.1484086319 | 17 | 8 | 2 | 24.4 | FDD | 605 | n1 | 152650 | 30M | 4T4R | 26 | 152650 |
| 3217960 | 11 | 121.4664659468 | 31.1538958123 | 15 | 3 | 11 | 18.8 | FDD | 375 | n1 | 152650 | 30M | 4T4R | 23 | 152650 |
| 3221315 | 8 | 121.4712727879 | 31.1480231010 | 1 | 11 | 4 | 3.5 | FDD | 265 | n1 | 152650 | 30M | 4T4R | 22 | 152650 |
| 3223671 | 1 | 121.4710347593 | 31.1543736390 | 56 | 1 | 6 | 29.3 | TDD | 512 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3224949 | 2 | 121.4687502487 | 31.1444803811 | 272 | 1 | 12 | 25.4 | TDD | 932 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3233239 | 3 | 121.4656424675 | 31.1536393291 | 299 | 11 | 12 | 8.2 | TDD | 617 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3236468 | 10 | 121.4725991048 | 31.1535762257 | 275 | 10 | 9 | 10.4 | FDD | 570 | n1 | 152650 | 30M | 4T4R | 30 | 152650 |
| 3242817 | 12 | 121.4713276109 | 31.1469106518 | 257 | 4 | 5 | 13.5 | FDD | 186 | n1 | 152650 | 30M | 4T4R | 22 | 152650 |
| 3251110 | 9 | 121.4678604803 | 31.1478057546 | 192 | 15 | 10 | 6.2 | FDD | 205 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |
| 3257187 | 4 | 121.4697876881 | 31.1477705190 | 123 | 10 | 4 | 25.8 | TDD | 300 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3259720 | 5 | 121.4682657785 | 31.1520835185 | 165 | 15 | 4 | 4.6 | TDD | 45 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3277679 | 6 | 121.4650116203 | 31.1479284895 | 159 | 5 | 2 | 5.8 | TDD | 248 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:31.337 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.358 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.463 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.463 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.211 | NREventA2 | measId:1;ServCellPCI:168;Se... |
| 2024-09-20 22:21:35.316 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.556 | NREventA5 | measId:3;ServCellPCI:168;Se... |
| 2024-09-20 22:21:35.614 | NRHandoverAttempt | SourcePCI:168;SourceNR-ARFC... |
| 2024-09-20 22:21:35.635 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.647 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:35.753 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.753 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3223671 | 1 | 7.0698 | 7.6876 | -117.4731 | 13.7596 | 116.3385 | 0.0053 | 0.0187 |
| 2024_09_20 22:00 | 3224949 | 2 | 12.5531 | 17.8279 | -114.4000 | 10.9145 | 132.1415 | 0.0178 | 0.0165 |
| 2024_09_20 22:00 | 3233239 | 3 | 8.8365 | 16.2691 | -114.6376 | 15.0218 | 143.2568 | 0.0170 | 0.0197 |
| 2024_09_20 22:00 | 3257187 | 4 | 14.8637 | 5.2295 | -114.1472 | 6.3153 | 195.2237 | 0.0019 | 0.0178 |
| 2024_09_20 22:00 | 3259720 | 5 | 6.0104 | 11.7384 | -117.8449 | 9.3609 | 129.9591 | 0.0118 | 0.0136 |
| 2024_09_20 22:00 | 3277679 | 6 | 16.2433 | 13.4737 | -114.2192 | 12.1699 | 111.1685 | 0.0081 | 0.0094 |
| 2024_09_20 22:00 | 3210246 | 7 | 9.0733 | 8.7772 | -114.8665 | 3.8672 | 21.5128 | 0.0173 | 0.0181 |
| 2024_09_20 22:00 | 3221315 | 8 | 8.1804 | 15.7644 | -114.2062 | 4.0752 | 39.3213 | 0.0010 | 0.0193 |
| 2024_09_20 22:00 | 3251110 | 9 | 12.5559 | 13.3646 | -114.2485 | 4.6792 | 52.9334 | 0.0150 | 0.0030 |
| 2024_09_20 22:00 | 3236468 | 10 | 6.3219 | 5.9438 | -117.1113 | 3.5172 | 45.5201 | 0.0124 | 0.0109 |
| 2024_09_20 22:00 | 3217960 | 11 | 10.7156 | 5.2565 | -116.8238 | 3.7456 | 26.9821 | 0.0043 | 0.0118 |
| 2024_09_20 22:00 | 3242817 | 12 | 5.9860 | 16.0836 | -116.6493 | 3.3399 | 38.2148 | 0.0123 | 0.0168 |
| 2024_09_20 22:00 | 3213384 | 13 | 17.9446 | 19.9218 | -117.1806 | 4.5638 | 57.9898 | 0.0014 | 0.0064 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412954_FDB8F284 | 152650 | 205 | -89.8 | 152650 | 605 | -94.7 | 152650 | 265 | -98.4 | 152650 | 375 |
| MR_1774412954_1BD6C6A0 | 152650 | 205 | -90.7 | 152650 | 605 | -96.5 | 152650 | 265 | -99.0 | 152650 | 375 |
| MR_1774412954_08B24B31 | 152650 | 205 | -87.2 | 152650 | 605 | -94.2 | 152650 | 265 | -99.3 | 152650 | 375 |
| MR_1774412954_10957BC6 | 504990 | 617 | -95.0 | 504990 | 932 | -95.1 | 504990 | 512 | -96.2 | 504990 | 45 |
| MR_1774412954_0111FFD6 | 504990 | 617 | -95.8 | 504990 | 932 | -93.2 | 504990 | 512 | -97.2 | 504990 | 45 |
| MR_1774412954_85F23CDB | 152650 | 205 | -87.9 | 152650 | 605 | -96.1 | 152650 | 265 | -98.5 | 152650 | 375 |
| MR_1774412954_2C6744FF | 152650 | 205 | -89.3 | 152650 | 605 | -95.8 | 152650 | 265 | -98.7 | 152650 | 375 |
| MR_1774412954_E8AD77A3 | 504990 | 617 | -96.5 | 504990 | 932 | -95.5 | 504990 | 512 | -94.6 | 504990 | 45 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 614: `957ca21b-ee4...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `957ca21b-ee48-4cef-bc9f-bb69d36b65da` |
| Tag | **single-answer** |
| 정답 | **C9** |
| C9 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3254568_1 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[614] topology](images/train_0614.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3254568_1
- `C2`: Lift the tilt angle of 3254568_1 by 2 degrees
- `C3`: Decrease transmission power for 3254568_1
- `C4`: Increase A3 Offset threshold for 3254568_1
- `C5`: Add neighbor relationship between 3260082_10 and 3248922_2
- `C6`: Press down the tilt angle  of 3248922_2 by 5 degrees
- `C7`: Add neighbor relationship between 3254568_1 and 3248922_2
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3248922_2
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3254568_1 **← 정답**
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3248922_2
- `C11`: Insufficient data; more data is needed for judgment.
- `C12`: Increase transmission power for 3254568_1
- `C13`: Increase transmission power for 3248922_2
- `C14`: Lift the tilt angle  of 3248922_2 by 5 degrees
- `C15`: Decrease transmission power for 3248922_2
- `C16`: Increase A3 Offset threshold for 3248922_2
- `C17`: Adjust the azimuth of 3248922_2 by 10 degrees
- `C18`: Decrease A3 Offset threshold for 3248922_2
- `C19`: Adjust the azimuth of 3254568_1 by 4 degrees
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3254568_1
- `C21`: Check test server and transmission issues
- `C22`: Press down the tilt angle of 3254568_1 by 2 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.355 | MS1 | 121.4656761527 | 31.1446186182 | 40 | 504990 | -93.08 | 12.86 | 538.56 | 0.11 | 2.66 | 1560 |
| 2024-09-20 22:21:32.730 | MS1 | 121.4656723529 | 31.1446240552 | 735 | 504990 | -94.25 | 9.11 | 315.45 | 0.10 | 3.00 | 1577 |
| 2024-09-20 22:21:33.606 | MS1 | 121.4656707802 | 31.1446209366 | 478 | 504990 | -93.96 | 14.77 | 440.90 | 0.19 | 2.46 | 1586 |
| 2024-09-20 22:21:34.461 | MS1 | 121.4656747217 | 31.1446265737 | 965 | 152650 | -91.76 | 7.50 | 67.67 | 0.09 | 1.51 | 984 |
| 2024-09-20 22:21:35.416 | MS1 | 121.4656710034 | 31.1446238488 | 793 | 152650 | -87.25 | 5.23 | 90.40 | 0.01 | 1.92 | 930 |
| 2024-09-20 22:21:36.491 | MS1 | 121.4656772629 | 31.1446364661 | 234 | 152650 | -95.04 | 7.06 | 92.41 | 0.13 | 1.54 | 947 |
| 2024-09-20 22:21:37.731 | MS1 | 121.4656774842 | 31.1446292264 | 742 | 152650 | -89.09 | 3.85 | 47.34 | 0.15 | 1.56 | 970 |
| 2024-09-20 22:21:38.371 | MS1 | 121.4656586665 | 31.1446250754 | 965 | 152650 | -90.22 | 2.39 | 89.06 | 0.18 | 1.66 | 984 |
| 2024-09-20 22:21:39.849 | MS1 | 121.4656618101 | 31.1446355311 | 793 | 152650 | -91.82 | 3.43 | 89.38 | 0.18 | 1.69 | 966 |
| 2024-09-20 22:21:40.483 | MS1 | 121.4656623129 | 31.1446203126 | 234 | 152650 | -94.06 | 3.19 | 51.02 | 0.15 | 2.98 | 1582 |
| 2024-09-20 22:21:41.741 | MS1 | 121.4656632159 | 31.1446292392 | 742 | 152650 | -89.30 | 5.24 | 77.16 | 0.09 | 2.55 | 1564 |
| 2024-09-20 22:21:42.392 | MS1 | 121.4656732610 | 31.1446269105 | 965 | 152650 | -89.08 | 6.34 | 91.21 | 0.17 | 2.79 | 1591 |

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
| 3216465 | 5 | 121.4640702090 | 31.1524029878 | 352 | 11 | 6 | 14.3 | TDD | 478 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3227950 | 9 | 121.4692972201 | 31.1504061896 | 228 | 6 | 5 | 7.2 | FDD | 901 | n1 | 152650 | 30M | 4T4R | 12 | 152650 |
| 3232348 | 12 | 121.4715370121 | 31.1479930760 | 290 | 3 | 9 | 4.5 | FDD | 793 | n1 | 152650 | 30M | 4T4R | 17 | 152650 |
| 3232708 | 4 | 121.4666831421 | 31.1441614542 | 168 | 0 | 9 | 26.4 | TDD | 254 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3239324 | 8 | 121.4726304797 | 31.1443288760 | 210 | 0 | 2 | 0.9 | FDD | 742 | n1 | 152650 | 30M | 4T4R | 19 | 152650 |
| 3243703 | 7 | 121.4753994283 | 31.1462030932 | 118 | 3 | 3 | 25.0 | FDD | 965 | n1 | 152650 | 30M | 4T4R | 15 | 152650 |
| 3248922 | 2 | 121.4754776573 | 31.1505330661 | 225 | 4 | 1 | 12.7 | TDD | 105 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3249886 | 3 | 121.4683874485 | 31.1543197690 | 160 | 13 | 10 | 2.7 | TDD | 108 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3254568 | 1 | 121.4700090963 | 31.1557312181 | 194 | 2 | 5 | 4.0 | TDD | 40 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3260082 | 10 | 121.4668456668 | 31.1526603480 | 107 | 13 | 10 | 27.0 | FDD | 234 | n1 | 152650 | 30M | 4T4R | 11 | 152650 |
| 3261541 | 6 | 121.4712522702 | 31.1452426096 | 267 | 14 | 9 | 10.7 | TDD | 735 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3267416 | 13 | 121.4753230706 | 31.1529617495 | 70 | 9 | 11 | 7.8 | FDD | 730 | n1 | 152650 | 30M | 4T4R | 13 | 152650 |
| 3269216 | 11 | 121.4702129219 | 31.1493921131 | 96 | 13 | 11 | 2.4 | FDD | 468 | n1 | 152650 | 30M | 4T4R | 18 | 152650 |

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
| 2024-09-20 22:21:31.355 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.371 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.511 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.511 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.206 | NREventA2 | measId:1;ServCellPCI:648;Se... |
| 2024-09-20 22:21:35.315 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.614 | NREventA5 | measId:3;ServCellPCI:648;Se... |
| 2024-09-20 22:21:35.654 | NRHandoverAttempt | SourcePCI:648;SourceNR-ARFC... |
| 2024-09-20 22:21:35.696 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.711 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:35.826 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.826 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3254568 | 1 | 14.9109 | 16.4418 | -115.0834 | 18.2933 | 80.0471 | 0.0190 | 0.0118 |
| 2024_09_20 22:00 | 3248922 | 2 | 13.4220 | 14.8698 | -116.8345 | 9.8484 | 104.0517 | 0.0192 | 0.0077 |
| 2024_09_20 22:00 | 3249886 | 3 | 9.1502 | 7.7320 | -116.2663 | 14.6607 | 89.9637 | 0.0188 | 0.0138 |
| 2024_09_20 22:00 | 3232708 | 4 | 19.6311 | 10.9794 | -115.1328 | 6.2477 | 154.1860 | 0.0113 | 0.0097 |
| 2024_09_20 22:00 | 3216465 | 5 | 15.5893 | 16.2388 | -116.8166 | 19.9593 | 146.0445 | 0.0160 | 0.0190 |
| 2024_09_20 22:00 | 3261541 | 6 | 11.7487 | 19.7561 | -116.7810 | 14.5932 | 105.1325 | 0.0135 | 0.0151 |
| 2024_09_20 22:00 | 3243703 | 7 | 16.8047 | 8.2273 | -114.2493 | 4.2219 | 48.0888 | 0.0070 | 0.0105 |
| 2024_09_20 22:00 | 3239324 | 8 | 18.7297 | 16.3339 | -114.3818 | 3.9791 | 49.7591 | 0.0120 | 0.0027 |
| 2024_09_20 22:00 | 3227950 | 9 | 9.8831 | 11.8973 | -116.3791 | 4.5037 | 44.2389 | 0.0191 | 0.0083 |
| 2024_09_20 22:00 | 3260082 | 10 | 9.2449 | 18.1930 | -116.3834 | 4.2401 | 59.3323 | 0.0109 | 0.0036 |
| 2024_09_20 22:00 | 3269216 | 11 | 15.7033 | 10.9415 | -116.6755 | 3.6015 | 26.0402 | 0.0022 | 0.0148 |
| 2024_09_20 22:00 | 3232348 | 12 | 17.9154 | 19.8901 | -115.2576 | 4.7160 | 52.4348 | 0.0047 | 0.0102 |
| 2024_09_20 22:00 | 3267416 | 13 | 17.0821 | 9.5466 | -117.3362 | 3.1583 | 58.4466 | 0.0110 | 0.0008 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415987_E861B0B2 | 152650 | 965 | -93.5 | 152650 | 901 | -95.9 | 152650 | 730 | -103.6 | 152650 | 468 |
| MR_1774415987_06B47283 | 504990 | 478 | -94.3 | 504990 | 105 | -94.5 | 504990 | 108 | -100.6 | 504990 | 254 |
| MR_1774415987_35BEDD03 | 504990 | 478 | -95.6 | 504990 | 105 | -94.2 | 504990 | 108 | -99.1 | 504990 | 254 |
| MR_1774415987_375B2F48 | 504990 | 478 | -92.3 | 504990 | 105 | -92.8 | 504990 | 108 | -99.9 | 504990 | 254 |
| MR_1774415987_F860585F | 504990 | 478 | -93.1 | 504990 | 105 | -93.3 | 504990 | 108 | -101.9 | 504990 | 254 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 615: `d2f48ebf-f9f...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `d2f48ebf-f9f4-4b8d-90fd-97a0375124ac` |
| Tag | **single-answer** |
| 정답 | **C8** |
| C8 의미 | Decrease A3 Offset threshold for 3245099_2 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[615] topology](images/train_0615.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3224671_3
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3245099_2
- `C3`: Check test server and transmission issues
- `C4`: Press down the tilt angle of 3245099_2 by 10 degrees
- `C5`: Add neighbor relationship between 3245099_2 and 3224671_3
- `C6`: Increase transmission power for 3224671_3
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3224671_3
- `C8`: Decrease A3 Offset threshold for 3245099_2 **← 정답**
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3224671_3
- `C10`: Insufficient data; more data is needed for judgment.
- `C11`: Adjust the azimuth of 3245099_2 by 50 degrees
- `C12`: Increase A3 Offset threshold for 3224671_3
- `C13`: Increase transmission power for 3245099_2
- `C14`: Adjust the azimuth of 3224671_3 by 26 degrees
- `C15`: Add neighbor relationship between 3232094_4 and 3224671_3
- `C16`: Press down the tilt angle  of 3224671_3 by 10 degrees
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3245099_2
- `C18`: Decrease transmission power for 3224671_3
- `C19`: Decrease transmission power for 3245099_2
- `C20`: Increase A3 Offset threshold for 3245099_2
- `C21`: Lift the tilt angle of 3245099_2 by 10 degrees
- `C22`: Lift the tilt angle  of 3224671_3 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.871 | MS1 | 121.4656703709 | 31.1446278500 | 17 | 504990 | -81.57 | 12.39 | 527.66 | 0.01 | 2.13 | 1568 |
| 2024-09-20 22:21:32.648 | MS1 | 121.4656674177 | 31.1446227464 | 17 | 504990 | -75.93 | 12.51 | 441.18 | 0.19 | 2.79 | 1577 |
| 2024-09-20 22:21:33.469 | MS1 | 121.4656776117 | 31.1446265090 | 17 | 504990 | -76.68 | 17.06 | 399.65 | 0.01 | 2.67 | 1571 |
| 2024-09-20 22:21:34.744 | MS1 | 121.4656714638 | 31.1446305585 | 17 | 504990 | -92.10 | -3.39 | 56.42 | 0.11 | 1.31 | 1573 |
| 2024-09-20 22:21:35.538 | MS1 | 121.4656761438 | 31.1446355463 | 17 | 504990 | -85.51 | -2.75 | 74.06 | 0.13 | 1.27 | 1589 |
| 2024-09-20 22:21:36.756 | MS1 | 121.4656618985 | 31.1446185929 | 17 | 504990 | -88.15 | -3.31 | 55.21 | 0.17 | 1.06 | 1582 |
| 2024-09-20 22:21:37.995 | MS1 | 121.4656772298 | 31.1446279556 | 17 | 504990 | -92.31 | -0.60 | 49.15 | 0.18 | 1.32 | 1576 |
| 2024-09-20 22:21:38.632 | MS1 | 121.4656647675 | 31.1446358123 | 17 | 504990 | -89.76 | -3.11 | 70.10 | 0.05 | 1.40 | 1566 |
| 2024-09-20 22:21:39.158 | MS1 | 121.4656729053 | 31.1446357641 | 610 | 504990 | -77.80 | 17.11 | 170.55 | 0.02 | 1.37 | 1580 |
| 2024-09-20 22:21:40.925 | MS1 | 121.4656587335 | 31.1446232564 | 610 | 504990 | -80.96 | 15.92 | 600.36 | 0.08 | 2.11 | 1598 |
| 2024-09-20 22:21:41.422 | MS1 | 121.4656584800 | 31.1446378613 | 610 | 504990 | -84.42 | 13.17 | 461.27 | 0.16 | 2.12 | 1581 |
| 2024-09-20 22:21:42.797 | MS1 | 121.4656664995 | 31.1446294269 | 610 | 504990 | -81.69 | 15.57 | 569.00 | 0.12 | 2.59 | 1580 |

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
| 3224671 | 3 | 121.4705709910 | 31.1461969774 | 275 | 15 | 0 | 49.6 | TDD | 610 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3232094 | 4 | 121.4683440193 | 31.1444854883 | 208 | 10 | 3 | 23.4 | TDD | 831 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3232663 | 1 | 121.4658039002 | 31.1483465740 | 291 | 11 | 1 | 44.8 | TDD | 712 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3245099 | 2 | 121.4702306592 | 31.1494608033 | 93 | 9 | 3 | 19.6 | TDD | 17 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |

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
| 2024-09-20 22:21:31.113 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.131 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.275 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.275 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.943 | NREventA3 | measId:2;ServCellPCI:526;Se... |
| 2024-09-20 22:21:38.183 | NRHandoverAttempt | SourcePCI:526;SourceNR-ARFC... |
| 2024-09-20 22:21:38.232 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.243 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.367 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.367 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3232663 | 1 | 12.2117 | 17.1847 | -116.9790 | 19.6482 | 167.7525 | 0.0072 | 0.0097 |
| 2024_09_20 22:00 | 3245099 | 2 | 7.4251 | 14.9100 | -117.9792 | 13.2417 | 157.4779 | 0.0040 | 0.1566 |
| 2024_09_20 22:00 | 3224671 | 3 | 14.8394 | 19.3622 | -117.3929 | 18.1523 | 196.9771 | 0.0106 | 0.0036 |
| 2024_09_20 22:00 | 3232094 | 4 | 7.9916 | 16.2169 | -116.3660 | 10.7797 | 174.2720 | 0.0104 | 0.0031 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413413_774274A7 | 504990 | 610 | -86.3 | 504990 | 17 | -91.4 | 504990 | 831 | -86.9 | 504990 | 712 |
| MR_1774413413_B41C6A98 | 504990 | 17 | -91.4 | 504990 | 610 | -87.1 | 504990 | 831 | -86.9 | 504990 | 712 |
| MR_1774413413_41F176FC | 504990 | 17 | -93.2 | 504990 | 610 | -87.4 | 504990 | 831 | -87.9 | 504990 | 712 |
| MR_1774413413_03290F77 | 504990 | 17 | -90.4 | 504990 | 610 | -86.8 | 504990 | 831 | -89.4 | 504990 | 712 |
| MR_1774413413_99E1353E | 504990 | 17 | -91.3 | 504990 | 610 | -88.2 | 504990 | 831 | -87.7 | 504990 | 712 |
| MR_1774413413_CBF2D902 | 504990 | 17 | -91.2 | 504990 | 610 | -87.6 | 504990 | 831 | -85.7 | 504990 | 712 |
| MR_1774413413_78B48C72 | 504990 | 17 | -92.9 | 504990 | 610 | -85.6 | 504990 | 831 | -86.4 | 504990 | 712 |
| MR_1774413413_C44CCE44 | 504990 | 17 | -93.7 | 504990 | 610 | -86.3 | 504990 | 831 | -86.7 | 504990 | 712 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 616: `765b22db-dc4...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `765b22db-dc42-47fb-be2b-8eac79cbfba5` |
| Tag | **single-answer** |
| 정답 | **C7** |
| C7 의미 | Decrease A3 Offset threshold for 3222933_1 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[616] topology](images/train_0616.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Check test server and transmission issues
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3222933_1
- `C3`: Increase A3 Offset threshold for 3242012_2
- `C4`: Increase transmission power for 3222933_1
- `C5`: Insufficient data; more data is needed for judgment.
- `C6`: Adjust the azimuth of 3242012_2 by 50 degrees
- `C7`: Decrease A3 Offset threshold for 3222933_1 **← 정답**
- `C8`: Press down the tilt angle  of 3242012_2 by 2 degrees
- `C9`: Increase transmission power for 3242012_2
- `C10`: Decrease transmission power for 3242012_2
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3242012_2
- `C12`: Add neighbor relationship between 3259791_3 and 3242012_2
- `C13`: Lift the tilt angle of 3222933_1 by 2 degrees
- `C14`: Add neighbor relationship between 3222933_1 and 3242012_2
- `C15`: Decrease A3 Offset threshold for 3242012_2
- `C16`: Increase A3 Offset threshold for 3222933_1
- `C17`: Adjust the azimuth of 3222933_1 by 50 degrees
- `C18`: Lift the tilt angle  of 3242012_2 by 2 degrees
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3242012_2
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3222933_1
- `C21`: Press down the tilt angle of 3222933_1 by 2 degrees
- `C22`: Decrease transmission power for 3222933_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.776 | MS1 | 121.4656634377 | 31.1446319942 | 649 | 504990 | -81.55 | 14.33 | 527.47 | 0.01 | 2.14 | 1584 |
| 2024-09-20 22:21:32.259 | MS1 | 121.4656711499 | 31.1446318001 | 649 | 504990 | -75.91 | 17.97 | 415.07 | 0.04 | 2.79 | 1581 |
| 2024-09-20 22:21:33.313 | MS1 | 121.4656725687 | 31.1446347553 | 649 | 504990 | -82.33 | 15.56 | 381.66 | 0.15 | 2.83 | 1593 |
| 2024-09-20 22:21:34.474 | MS1 | 121.4656619672 | 31.1446288935 | 649 | 504990 | -88.20 | -3.48 | 71.55 | 0.17 | 1.43 | 1594 |
| 2024-09-20 22:21:35.652 | MS1 | 121.4656742481 | 31.1446222844 | 649 | 504990 | -92.42 | -0.17 | 24.88 | 0.03 | 1.48 | 1563 |
| 2024-09-20 22:21:36.955 | MS1 | 121.4656717121 | 31.1446184171 | 649 | 504990 | -89.77 | -2.05 | 74.50 | 0.07 | 1.12 | 1578 |
| 2024-09-20 22:21:37.452 | MS1 | 121.4656715223 | 31.1446238223 | 649 | 504990 | -83.81 | -3.97 | 55.67 | 0.01 | 1.06 | 1576 |
| 2024-09-20 22:21:38.878 | MS1 | 121.4656768840 | 31.1446226857 | 649 | 504990 | -85.89 | -1.35 | 55.07 | 0.12 | 1.06 | 1591 |
| 2024-09-20 22:21:39.878 | MS1 | 121.4656753718 | 31.1446314988 | 915 | 504990 | -77.51 | 15.95 | 203.63 | 0.04 | 1.46 | 1567 |
| 2024-09-20 22:21:40.576 | MS1 | 121.4656624651 | 31.1446275442 | 915 | 504990 | -84.91 | 13.09 | 490.66 | 0.08 | 2.33 | 1596 |
| 2024-09-20 22:21:41.514 | MS1 | 121.4656746842 | 31.1446239797 | 915 | 504990 | -75.23 | 12.71 | 368.30 | 0.07 | 2.95 | 1562 |
| 2024-09-20 22:21:42.443 | MS1 | 121.4656614231 | 31.1446282002 | 915 | 504990 | -78.68 | 15.51 | 461.58 | 0.08 | 2.88 | 1590 |

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
| 3222933 | 1 | 121.4671554108 | 31.1522887629 | 27 | 0 | 1 | 26.7 | TDD | 649 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3234546 | 4 | 121.4662292222 | 31.1554329518 | 132 | 3 | 10 | 15.7 | TDD | 308 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3242012 | 2 | 121.4701319276 | 31.1558003156 | 60 | 1 | 8 | 22.8 | TDD | 915 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3259791 | 3 | 121.4755845616 | 31.1533591338 | 253 | 13 | 4 | 27.0 | TDD | 524 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |

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
| 2024-09-20 22:21:31.490 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.636 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.636 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.360 | NREventA3 | measId:2;ServCellPCI:253;Se... |
| 2024-09-20 22:21:38.600 | NRHandoverAttempt | SourcePCI:253;SourceNR-ARFC... |
| 2024-09-20 22:21:38.642 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.655 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.804 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.804 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3222933 | 1 | 12.0768 | 10.2785 | -115.8242 | 19.0588 | 94.0157 | 0.0192 | 0.1810 |
| 2024_09_20 22:00 | 3242012 | 2 | 17.9023 | 11.5109 | -115.4476 | 19.1431 | 108.4842 | 0.0191 | 0.0185 |
| 2024_09_20 22:00 | 3259791 | 3 | 7.4653 | 18.2041 | -114.5936 | 5.8429 | 179.1542 | 0.0165 | 0.0124 |
| 2024_09_20 22:00 | 3234546 | 4 | 6.1102 | 6.6747 | -115.4481 | 14.2411 | 184.1823 | 0.0167 | 0.0082 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413304_171F7DFB | 504990 | 915 | -83.2 | 504990 | 649 | -88.1 | 504990 | 524 | -83.3 | 504990 | 308 |
| MR_1774413304_21D1CBE0 | 504990 | 915 | -83.2 | 504990 | 649 | -89.0 | 504990 | 524 | -83.4 | 504990 | 308 |
| MR_1774413304_A025ECFD | 504990 | 915 | -79.6 | 504990 | 649 | -88.4 | 504990 | 524 | -82.1 | 504990 | 308 |
| MR_1774413304_2366BB27 | 504990 | 649 | -89.6 | 504990 | 915 | -82.8 | 504990 | 524 | -82.6 | 504990 | 308 |
| MR_1774413304_AAFB98A2 | 504990 | 649 | -88.9 | 504990 | 915 | -80.7 | 504990 | 524 | -81.2 | 504990 | 308 |
| MR_1774413304_101FA02E | 504990 | 649 | -88.5 | 504990 | 915 | -79.7 | 504990 | 524 | -81.3 | 504990 | 308 |
| MR_1774413304_AB3D7924 | 504990 | 649 | -87.6 | 504990 | 915 | -82.8 | 504990 | 524 | -83.4 | 504990 | 308 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 617: `1f1e827f-68a...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `1f1e827f-68ad-40d7-8137-808eaa1274e7` |
| Tag | **single-answer** |
| 정답 | **C15** |
| C15 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3263567_3 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[617] topology](images/train_0617.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3225561_4
- `C2`: Lift the tilt angle  of 3225561_4 by 2 degrees
- `C3`: Decrease A3 Offset threshold for 3263567_3
- `C4`: Adjust the azimuth of 3225561_4 by 50 degrees
- `C5`: Press down the tilt angle  of 3225561_4 by 2 degrees
- `C6`: Add neighbor relationship between 3234363_1 and 3225561_4
- `C7`: Lift the tilt angle of 3263567_3 by 4 degrees
- `C8`: Insufficient data; more data is needed for judgment.
- `C9`: Increase transmission power for 3263567_3
- `C10`: Decrease A3 Offset threshold for 3225561_4
- `C11`: Decrease transmission power for 3263567_3
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3225561_4
- `C13`: Increase transmission power for 3225561_4
- `C14`: Increase A3 Offset threshold for 3263567_3
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3263567_3 **← 정답**
- `C16`: Add neighbor relationship between 3263567_3 and 3225561_4
- `C17`: Check test server and transmission issues
- `C18`: Adjust the azimuth of 3263567_3 by 1 degrees
- `C19`: Increase A3 Offset threshold for 3225561_4
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3225561_4
- `C21`: Press down the tilt angle of 3263567_3 by 4 degrees
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3263567_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.968 | MS1 | 121.4656710151 | 31.1446348121 | 597 | 504990 | -89.86 | 12.65 | 442.42 | 0.15 | 2.23 | 1568 |
| 2024-09-20 22:21:32.642 | MS1 | 121.4656723384 | 31.1446374195 | 597 | 504990 | -88.29 | 15.03 | 376.01 | 0.20 | 2.55 | 1586 |
| 2024-09-20 22:21:33.451 | MS1 | 121.4656661435 | 31.1446235025 | 597 | 504990 | -86.44 | 17.82 | 394.48 | 0.01 | 2.15 | 1568 |
| 2024-09-20 22:21:34.126 | MS1 | 121.4656658210 | 31.1446350165 | 597 | 504990 | -88.85 | 12.53 | 88.58 | 0.60 | 2.48 | 662 |
| 2024-09-20 22:21:35.248 | MS1 | 121.4656750393 | 31.1446336969 | 597 | 504990 | -87.15 | 13.89 | 66.43 | 0.57 | 2.45 | 699 |
| 2024-09-20 22:21:36.221 | MS1 | 121.4656613307 | 31.1446366458 | 597 | 504990 | -85.58 | 13.89 | 73.30 | 0.69 | 2.99 | 575 |
| 2024-09-20 22:21:37.194 | MS1 | 121.4656745932 | 31.1446193496 | 597 | 504990 | -93.25 | 11.81 | 104.80 | 0.65 | 2.39 | 672 |
| 2024-09-20 22:21:38.643 | MS1 | 121.4656616038 | 31.1446259288 | 597 | 504990 | -91.94 | 11.43 | 72.91 | 0.61 | 2.26 | 611 |
| 2024-09-20 22:21:39.578 | MS1 | 121.4656751022 | 31.1446265523 | 597 | 504990 | -93.81 | 10.17 | 55.29 | 0.57 | 2.69 | 565 |
| 2024-09-20 22:21:40.401 | MS1 | 121.4656774635 | 31.1446256543 | 597 | 504990 | -92.10 | 12.59 | 383.50 | 0.00 | 2.62 | 1591 |
| 2024-09-20 22:21:41.876 | MS1 | 121.4656725943 | 31.1446186721 | 597 | 504990 | -89.95 | 8.98 | 338.10 | 0.06 | 2.31 | 1564 |
| 2024-09-20 22:21:42.195 | MS1 | 121.4656633564 | 31.1446315448 | 597 | 504990 | -93.07 | 11.70 | 519.31 | 0.09 | 2.08 | 1581 |

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
| 3225561 | 4 | 121.4757410304 | 31.1548798751 | 102 | 1 | 11 | 33.3 | TDD | 446 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3234363 | 1 | 121.4695625269 | 31.1496475007 | 203 | 8 | 7 | 29.5 | TDD | 641 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3241412 | 2 | 121.4736320125 | 31.1481162572 | 146 | 8 | 9 | 46.4 | TDD | 212 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3263567 | 3 | 121.4676815946 | 31.1486409656 | 202 | 0 | 2 | 32.4 | TDD | 597 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:30.787 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.806 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:30.919 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.919 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.666 | NREventA3 | measId:2;ServCellPCI:778;Se... |
| 2024-09-20 22:21:37.906 | NRHandoverAttempt | SourcePCI:778;SourceNR-ARFC... |
| 2024-09-20 22:21:37.944 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.955 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.064 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.064 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3234363 | 1 | 10.6797 | 14.5366 | -115.1527 | 8.1767 | 108.6168 | 0.0070 | 0.0113 |
| 2024_09_20 22:00 | 3241412 | 2 | 12.7986 | 15.8868 | -114.5566 | 7.9299 | 134.5725 | 0.0105 | 0.0033 |
| 2024_09_20 22:00 | 3263567 | 3 | 10.5484 | 16.0814 | -117.5500 | 19.1555 | 185.2245 | 0.0118 | 0.0079 |
| 2024_09_20 22:00 | 3225561 | 4 | 10.8745 | 6.7774 | -117.8849 | 19.4617 | 158.1110 | 0.0096 | 0.0181 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412264_93DD4648 | 504990 | 597 | -89.4 | 504990 | 446 | -94.2 | 504990 | 641 | -100.1 | 504990 | 212 |
| MR_1774412264_A0E2C523 | 504990 | 597 | -89.9 | 504990 | 446 | -91.2 | 504990 | 641 | -101.0 | 504990 | 212 |
| MR_1774412264_147D2326 | 504990 | 597 | -87.4 | 504990 | 446 | -94.8 | 504990 | 641 | -97.5 | 504990 | 212 |
| MR_1774412264_314372EF | 504990 | 597 | -88.6 | 504990 | 446 | -92.3 | 504990 | 641 | -99.2 | 504990 | 212 |
| MR_1774412264_54D57526 | 504990 | 597 | -88.0 | 504990 | 446 | -94.7 | 504990 | 641 | -100.8 | 504990 | 212 |
| MR_1774412264_D3F6483A | 504990 | 597 | -86.9 | 504990 | 446 | -94.8 | 504990 | 641 | -101.0 | 504990 | 212 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 618: `12c457c6-be3...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `12c457c6-be3c-4710-8dab-01c0b80b8ceb` |
| Tag | **single-answer** |
| 정답 | **C21** |
| C21 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3257440_2 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[618] topology](images/train_0618.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment.
- `C2`: Increase transmission power for 3257440_2
- `C3`: Lift the tilt angle of 3257440_2 by 5 degrees
- `C4`: Press down the tilt angle  of 3272463_1 by 10 degrees
- `C5`: Decrease transmission power for 3257440_2
- `C6`: Adjust the azimuth of 3257440_2 by 37 degrees
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3272463_1
- `C8`: Decrease transmission power for 3272463_1
- `C9`: Check test server and transmission issues
- `C10`: Adjust the azimuth of 3272463_1 by 50 degrees
- `C11`: Decrease A3 Offset threshold for 3272463_1
- `C12`: Lift the tilt angle  of 3272463_1 by 10 degrees
- `C13`: Increase transmission power for 3272463_1
- `C14`: Add neighbor relationship between 3251060_3 and 3272463_1
- `C15`: Decrease A3 Offset threshold for 3257440_2
- `C16`: Increase A3 Offset threshold for 3272463_1
- `C17`: Press down the tilt angle of 3257440_2 by 5 degrees
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3257440_2
- `C19`: Increase A3 Offset threshold for 3257440_2
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3272463_1
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3257440_2 **← 정답**
- `C22`: Add neighbor relationship between 3257440_2 and 3272463_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.560 | MS1 | 121.4656607534 | 31.1446336090 | 814 | 504990 | -88.87 | 17.43 | 494.69 | 0.09 | 2.00 | 1593 |
| 2024-09-20 22:21:32.258 | MS1 | 121.4656759573 | 31.1446240525 | 814 | 504990 | -87.72 | 16.66 | 359.02 | 0.14 | 2.59 | 1565 |
| 2024-09-20 22:21:33.532 | MS1 | 121.4656650716 | 31.1446365338 | 814 | 504990 | -89.36 | 17.33 | 428.15 | 0.03 | 2.33 | 1571 |
| 2024-09-20 22:21:34.616 | MS1 | 121.4656716914 | 31.1446378051 | 814 | 504990 | -88.64 | 12.59 | 89.46 | 0.57 | 2.90 | 689 |
| 2024-09-20 22:21:35.223 | MS1 | 121.4656677772 | 31.1446339344 | 814 | 504990 | -85.74 | 15.50 | 74.00 | 0.68 | 2.66 | 692 |
| 2024-09-20 22:21:36.203 | MS1 | 121.4656642400 | 31.1446184039 | 814 | 504990 | -87.61 | 13.79 | 69.10 | 0.68 | 2.04 | 603 |
| 2024-09-20 22:21:37.453 | MS1 | 121.4656676497 | 31.1446259311 | 814 | 504990 | -90.56 | 8.09 | 63.06 | 0.58 | 2.18 | 522 |
| 2024-09-20 22:21:38.211 | MS1 | 121.4656695282 | 31.1446300575 | 814 | 504990 | -90.43 | 10.67 | 90.13 | 0.57 | 2.49 | 600 |
| 2024-09-20 22:21:39.280 | MS1 | 121.4656708972 | 31.1446245416 | 814 | 504990 | -92.30 | 7.03 | 99.10 | 0.58 | 2.15 | 556 |
| 2024-09-20 22:21:40.795 | MS1 | 121.4656657067 | 31.1446302173 | 814 | 504990 | -90.01 | 9.05 | 584.99 | 0.09 | 2.33 | 1586 |
| 2024-09-20 22:21:41.524 | MS1 | 121.4656673845 | 31.1446180889 | 814 | 504990 | -91.92 | 11.21 | 492.62 | 0.10 | 2.59 | 1561 |
| 2024-09-20 22:21:42.489 | MS1 | 121.4656606747 | 31.1446235039 | 814 | 504990 | -92.68 | 8.68 | 412.48 | 0.04 | 2.96 | 1566 |

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
| 3243340 | 4 | 121.4710627590 | 31.1546822803 | 37 | 9 | 5 | 23.1 | TDD | 670 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3251060 | 3 | 121.4718661698 | 31.1454014151 | 143 | 5 | 3 | 47.8 | TDD | 724 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3257440 | 2 | 121.4739921379 | 31.1529855528 | 257 | 3 | 9 | 32.8 | TDD | 814 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3272463 | 1 | 121.4667050631 | 31.1465333067 | 110 | 5 | 6 | 39.3 | TDD | 356 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |

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
| 2024-09-20 22:21:31.356 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.374 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.510 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.510 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.173 | NREventA3 | measId:2;ServCellPCI:281;Se... |
| 2024-09-20 22:21:38.413 | NRHandoverAttempt | SourcePCI:281;SourceNR-ARFC... |
| 2024-09-20 22:21:38.461 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.475 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.621 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.621 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3272463 | 1 | 6.4393 | 14.0606 | -116.1433 | 6.0435 | 170.1643 | 0.0042 | 0.0184 |
| 2024_09_20 22:00 | 3257440 | 2 | 7.1635 | 11.6574 | -114.1820 | 19.5949 | 88.6885 | 0.0006 | 0.0169 |
| 2024_09_20 22:00 | 3251060 | 3 | 8.3130 | 5.6955 | -117.7364 | 16.6580 | 123.5866 | 0.0110 | 0.0186 |
| 2024_09_20 22:00 | 3243340 | 4 | 6.4001 | 15.6141 | -115.4958 | 12.8307 | 148.0025 | 0.0067 | 0.0047 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416759_415A87DB | 504990 | 814 | -87.6 | 504990 | 356 | -96.2 | 504990 | 724 | -99.8 | 504990 | 670 |
| MR_1774416759_349ECEA7 | 504990 | 814 | -90.4 | 504990 | 356 | -98.5 | 504990 | 724 | -98.6 | 504990 | 670 |
| MR_1774416759_68460ECE | 504990 | 814 | -89.8 | 504990 | 356 | -96.6 | 504990 | 724 | -98.9 | 504990 | 670 |
| MR_1774416759_AA4A2E85 | 504990 | 814 | -89.5 | 504990 | 356 | -96.8 | 504990 | 724 | -96.2 | 504990 | 670 |
| MR_1774416759_E0C178C4 | 504990 | 814 | -90.2 | 504990 | 356 | -99.2 | 504990 | 724 | -96.8 | 504990 | 670 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 619: `cb605c80-a0c...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `cb605c80-a0c6-4d0a-9305-852f8114ead3` |
| Tag | **single-answer** |
| 정답 | **C19** |
| C19 의미 | Decrease A3 Offset threshold for 3264659_1 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[619] topology](images/train_0619.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3234061_3
- `C2`: Increase A3 Offset threshold for 3234061_3
- `C3`: Adjust the azimuth of 3264659_1 by 50 degrees
- `C4`: Lift the tilt angle of 3264659_1 by 6 degrees
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3264659_1
- `C6`: Decrease A3 Offset threshold for 3234061_3
- `C7`: Press down the tilt angle of 3264659_1 by 6 degrees
- `C8`: Press down the tilt angle  of 3234061_3 by 2 degrees
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3234061_3
- `C10`: Check test server and transmission issues
- `C11`: Add neighbor relationship between 3264659_1 and 3234061_3
- `C12`: Decrease transmission power for 3234061_3
- `C13`: Adjust the azimuth of 3234061_3 by 50 degrees
- `C14`: Decrease transmission power for 3264659_1
- `C15`: Lift the tilt angle  of 3234061_3 by 2 degrees
- `C16`: Insufficient data; more data is needed for judgment.
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3234061_3
- `C18`: Increase A3 Offset threshold for 3264659_1
- `C19`: Decrease A3 Offset threshold for 3264659_1 **← 정답**
- `C20`: Add neighbor relationship between 3272869_2 and 3234061_3
- `C21`: Increase transmission power for 3264659_1
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3264659_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.796 | MS1 | 121.4656625821 | 31.1446371326 | 64 | 504990 | -79.53 | 16.66 | 492.19 | 0.13 | 2.34 | 1592 |
| 2024-09-20 22:21:32.692 | MS1 | 121.4656583644 | 31.1446293287 | 64 | 504990 | -81.15 | 16.18 | 458.86 | 0.01 | 2.26 | 1593 |
| 2024-09-20 22:21:33.576 | MS1 | 121.4656584761 | 31.1446273422 | 64 | 504990 | -77.10 | 12.78 | 428.99 | 0.01 | 2.56 | 1592 |
| 2024-09-20 22:21:34.629 | MS1 | 121.4656763361 | 31.1446315818 | 64 | 504990 | -87.39 | -3.20 | 72.94 | 0.00 | 1.11 | 1599 |
| 2024-09-20 22:21:35.672 | MS1 | 121.4656729203 | 31.1446274842 | 64 | 504990 | -89.34 | -1.06 | 42.43 | 0.13 | 1.37 | 1591 |
| 2024-09-20 22:21:36.756 | MS1 | 121.4656738073 | 31.1446235568 | 64 | 504990 | -90.55 | -2.69 | 49.80 | 0.01 | 1.42 | 1569 |
| 2024-09-20 22:21:37.976 | MS1 | 121.4656744742 | 31.1446363222 | 64 | 504990 | -91.16 | -4.00 | 39.81 | 0.06 | 1.20 | 1578 |
| 2024-09-20 22:21:38.848 | MS1 | 121.4656667714 | 31.1446353377 | 64 | 504990 | -84.15 | -2.53 | 82.63 | 0.09 | 1.12 | 1564 |
| 2024-09-20 22:21:39.833 | MS1 | 121.4656698283 | 31.1446203234 | 90 | 504990 | -82.59 | 14.77 | 145.94 | 0.04 | 1.19 | 1594 |
| 2024-09-20 22:21:40.661 | MS1 | 121.4656673964 | 31.1446266904 | 90 | 504990 | -83.29 | 13.24 | 474.79 | 0.12 | 2.09 | 1593 |
| 2024-09-20 22:21:41.252 | MS1 | 121.4656631681 | 31.1446323922 | 90 | 504990 | -78.87 | 14.88 | 387.26 | 0.19 | 2.17 | 1562 |
| 2024-09-20 22:21:42.763 | MS1 | 121.4656652728 | 31.1446351405 | 90 | 504990 | -78.27 | 12.11 | 402.79 | 0.04 | 2.94 | 1600 |

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
| 3234061 | 3 | 121.4651768505 | 31.1551086473 | 341 | 1 | 9 | 20.4 | TDD | 90 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3262697 | 4 | 121.4709773330 | 31.1501687327 | 35 | 10 | 7 | 41.1 | TDD | 35 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3264659 | 1 | 121.4686339403 | 31.1518003500 | 124 | 3 | 9 | 49.8 | TDD | 64 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3272869 | 2 | 121.4695520631 | 31.1546162920 | 87 | 14 | 1 | 25.0 | TDD | 568 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

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
| 2024-09-20 22:21:30.878 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.899 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.014 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.014 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.682 | NREventA3 | measId:2;ServCellPCI:135;Se... |
| 2024-09-20 22:21:37.922 | NRHandoverAttempt | SourcePCI:135;SourceNR-ARFC... |
| 2024-09-20 22:21:37.956 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.971 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.091 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.091 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3264659 | 1 | 6.3201 | 11.4779 | -117.6654 | 12.7490 | 100.9846 | 0.0111 | 0.1230 |
| 2024_09_20 22:00 | 3272869 | 2 | 5.3376 | 13.8425 | -114.1237 | 12.3768 | 141.0072 | 0.0175 | 0.0122 |
| 2024_09_20 22:00 | 3234061 | 3 | 19.7296 | 5.6585 | -115.4855 | 12.8082 | 102.0126 | 0.0051 | 0.0029 |
| 2024_09_20 22:00 | 3262697 | 4 | 15.5763 | 15.8712 | -116.0682 | 11.1361 | 199.2247 | 0.0072 | 0.0179 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415887_0097A01B | 504990 | 64 | -85.7 | 504990 | 90 | -82.1 | 504990 | 568 | -83.3 | 504990 | 35 |
| MR_1774415887_1C5BDDD8 | 504990 | 64 | -86.9 | 504990 | 90 | -81.0 | 504990 | 568 | -85.3 | 504990 | 35 |
| MR_1774415887_20D2FD4C | 504990 | 64 | -88.1 | 504990 | 90 | -82.8 | 504990 | 568 | -84.8 | 504990 | 35 |
| MR_1774415887_B8A72A90 | 504990 | 64 | -85.4 | 504990 | 90 | -84.6 | 504990 | 568 | -85.7 | 504990 | 35 |
| MR_1774415887_2A46AEEA | 504990 | 90 | -82.4 | 504990 | 64 | -85.9 | 504990 | 568 | -83.4 | 504990 | 35 |

> *... 2개 열 생략 (전체 14열)*

---
