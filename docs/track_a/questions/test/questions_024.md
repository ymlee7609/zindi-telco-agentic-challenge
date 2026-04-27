# Track A 문제 분석 — test[230]~test[239]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/test.json`
> 범위: test[230] ~ test[239] (10개)

## 목차

1. [문제 230: `8d971287-932...`](#230) — single-answer
2. [문제 231: `e0ea374e-8d3...`](#231) — single-answer
3. [문제 232: `d7f93cd4-05f...`](#232) — single-answer
4. [문제 233: `96a1171c-84d...`](#233) — single-answer
5. [문제 234: `181effab-f64...`](#234) — multiple-answer
6. [문제 235: `9c4b3b5e-f34...`](#235) — single-answer
7. [문제 236: `b6db3a8a-712...`](#236) — multiple-answer
8. [문제 237: `61573815-1f6...`](#237) — single-answer
9. [문제 238: `63c3f8c0-7a9...`](#238) — single-answer
10. [문제 239: `b8885d83-91d...`](#239) — single-answer

---

### 문제 230: `8d971287-932...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `8d971287-9324-46d1-8718-297903024f9c` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[230] topology](images/test_0230.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3232175_2 and 3269380_3
- `C2`: Increase transmission power for 3270070_4
- `C3`: Increase A3 Offset threshold for 3270070_4
- `C4`: Adjust the azimuth of 3270070_4 by 16 degrees
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3270070_4
- `C6`: Increase transmission power for 3269380_3
- `C7`: Insufficient data; more data is needed for judgment.
- `C8`: Lift the tilt angle of 3270070_4 by 3 degrees
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3269380_3
- `C10`: Decrease A3 Offset threshold for 3269380_3
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3269380_3
- `C12`: Adjust the azimuth of 3269380_3 by 4 degrees
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3270070_4
- `C14`: Increase A3 Offset threshold for 3269380_3
- `C15`: Lift the tilt angle  of 3269380_3 by 10 degrees
- `C16`: Decrease A3 Offset threshold for 3270070_4
- `C17`: Check test server and transmission issues
- `C18`: Add neighbor relationship between 3270070_4 and 3269380_3
- `C19`: Press down the tilt angle  of 3269380_3 by 10 degrees
- `C20`: Decrease transmission power for 3269380_3
- `C21`: Decrease transmission power for 3270070_4
- `C22`: Press down the tilt angle of 3270070_4 by 3 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.134 | MS1 | 121.4656609348 | 31.1446205424 | 606 | 504990 | -90.50 | 13.31 | 414.33 | 0.07 | 2.46 | 1582 |
| 2024-09-20 22:21:32.827 | MS1 | 121.4656716852 | 31.1446256764 | 606 | 504990 | -91.21 | 13.29 | 448.13 | 0.20 | 2.16 | 1589 |
| 2024-09-20 22:21:33.685 | MS1 | 121.4656713052 | 31.1446307589 | 606 | 504990 | -87.02 | 15.94 | 333.34 | 0.07 | 2.23 | 1590 |
| 2024-09-20 22:21:34.988 | MS1 | 121.4656723716 | 31.1446219301 | 606 | 504990 | -89.20 | 17.16 | 89.76 | 0.61 | 2.78 | 682 |
| 2024-09-20 22:21:35.863 | MS1 | 121.4656762800 | 31.1446350048 | 606 | 504990 | -91.18 | 13.81 | 47.83 | 0.68 | 2.78 | 530 |
| 2024-09-20 22:21:36.276 | MS1 | 121.4656600493 | 31.1446352867 | 606 | 504990 | -86.03 | 13.46 | 52.25 | 0.58 | 2.21 | 693 |
| 2024-09-20 22:21:37.456 | MS1 | 121.4656685568 | 31.1446309701 | 606 | 504990 | -93.54 | 8.72 | 61.12 | 0.50 | 2.14 | 615 |
| 2024-09-20 22:21:38.963 | MS1 | 121.4656769181 | 31.1446243822 | 606 | 504990 | -89.83 | 11.65 | 58.03 | 0.55 | 2.33 | 506 |
| 2024-09-20 22:21:39.410 | MS1 | 121.4656708726 | 31.1446214333 | 606 | 504990 | -89.26 | 8.52 | 67.43 | 0.62 | 2.66 | 508 |
| 2024-09-20 22:21:40.377 | MS1 | 121.4656666602 | 31.1446300126 | 606 | 504990 | -92.02 | 8.48 | 521.82 | 0.08 | 2.06 | 1589 |
| 2024-09-20 22:21:41.108 | MS1 | 121.4656634916 | 31.1446311734 | 606 | 504990 | -90.16 | 11.91 | 492.53 | 0.14 | 2.53 | 1588 |
| 2024-09-20 22:21:42.367 | MS1 | 121.4656616905 | 31.1446315995 | 606 | 504990 | -91.19 | 7.56 | 579.45 | 0.08 | 2.74 | 1560 |

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
| 3232175 | 2 | 121.4653866469 | 31.1556293664 | 1 | 3 | 6 | 17.1 | TDD | 244 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3236244 | 1 | 121.4669039399 | 31.1525069508 | 302 | 15 | 0 | 37.4 | TDD | 146 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3269380 | 3 | 121.4644355307 | 31.1470819113 | 153 | 8 | 8 | 23.9 | TDD | 325 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3270070 | 4 | 121.4744465406 | 31.1485982302 | 258 | 0 | 2 | 47.2 | TDD | 606 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |

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
| 2024-09-20 22:21:31.205 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.222 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.357 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.357 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.061 | NREventA3 | measId:2;ServCellPCI:115;Se... |
| 2024-09-20 22:21:38.301 | NRHandoverAttempt | SourcePCI:115;SourceNR-ARFC... |
| 2024-09-20 22:21:38.344 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.354 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.471 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.471 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3236244 | 1 | 19.5590 | 8.6586 | -114.1664 | 19.1398 | 147.7462 | 0.0062 | 0.0001 |
| 2024_09_20 22:00 | 3232175 | 2 | 10.5250 | 10.1605 | -117.5925 | 16.2223 | 130.5515 | 0.0113 | 0.0107 |
| 2024_09_20 22:00 | 3269380 | 3 | 6.0489 | 15.3808 | -115.9878 | 5.2252 | 107.7491 | 0.0072 | 0.0199 |
| 2024_09_20 22:00 | 3270070 | 4 | 9.8476 | 7.1789 | -116.8595 | 5.7885 | 156.7412 | 0.0126 | 0.0104 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416087_CB58B1B6 | 504990 | 606 | -90.6 | 504990 | 325 | -97.1 | 504990 | 244 | -98.5 | 504990 | 146 |
| MR_1774416087_5E8ABA8A | 504990 | 606 | -88.2 | 504990 | 325 | -99.8 | 504990 | 244 | -100.8 | 504990 | 146 |
| MR_1774416087_D750D508 | 504990 | 606 | -90.2 | 504990 | 325 | -98.2 | 504990 | 244 | -100.8 | 504990 | 146 |
| MR_1774416087_AC6969BE | 504990 | 606 | -88.8 | 504990 | 325 | -98.6 | 504990 | 244 | -99.2 | 504990 | 146 |
| MR_1774416087_095E4C67 | 504990 | 606 | -89.4 | 504990 | 325 | -98.1 | 504990 | 244 | -100.4 | 504990 | 146 |
| MR_1774416087_35E2D0A3 | 504990 | 606 | -88.8 | 504990 | 325 | -97.7 | 504990 | 244 | -99.3 | 504990 | 146 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 231: `e0ea374e-8d3...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `e0ea374e-8d31-4043-bf83-238b97fbf639` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[231] topology](images/test_0231.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3259183_4
- `C2`: Increase transmission power for 3259183_4
- `C3`: Insufficient data; more data is needed for judgment.
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3259183_4
- `C5`: Decrease A3 Offset threshold for 3259183_4
- `C6`: Adjust the azimuth of 3259183_4 by 50 degrees
- `C7`: Decrease transmission power for 3262395_2
- `C8`: Add neighbor relationship between 3274075_3 and 3262395_2
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3262395_2
- `C10`: Press down the tilt angle of 3259183_4 by 10 degrees
- `C11`: Increase transmission power for 3262395_2
- `C12`: Increase A3 Offset threshold for 3259183_4
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3262395_2
- `C14`: Increase A3 Offset threshold for 3262395_2
- `C15`: Lift the tilt angle  of 3262395_2 by 3 degrees
- `C16`: Decrease A3 Offset threshold for 3262395_2
- `C17`: Press down the tilt angle  of 3262395_2 by 3 degrees
- `C18`: Lift the tilt angle of 3259183_4 by 10 degrees
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3259183_4
- `C20`: Check test server and transmission issues
- `C21`: Adjust the azimuth of 3262395_2 by 15 degrees
- `C22`: Add neighbor relationship between 3259183_4 and 3262395_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.398 | MS1 | 121.4656684382 | 31.1446204732 | 614 | 504990 | -89.63 | 12.67 | 349.44 | 0.01 | 2.33 | 1598 |
| 2024-09-20 22:21:32.978 | MS1 | 121.4656603635 | 31.1446247370 | 614 | 504990 | -86.96 | 15.25 | 394.41 | 0.15 | 2.63 | 1574 |
| 2024-09-20 22:21:33.446 | MS1 | 121.4656597831 | 31.1446260312 | 614 | 504990 | -88.67 | 17.82 | 301.87 | 0.12 | 2.16 | 1576 |
| 2024-09-20 22:21:34.632 | MS1 | 121.4656745913 | 31.1446289714 | 614 | 504990 | -90.94 | 15.14 | 79.17 | 0.15 | 2.57 | 1572 |
| 2024-09-20 22:21:35.861 | MS1 | 121.4656600027 | 31.1446192548 | 614 | 504990 | -86.86 | 13.85 | 92.03 | 0.17 | 2.81 | 1576 |
| 2024-09-20 22:21:36.381 | MS1 | 121.4656674758 | 31.1446191908 | 614 | 504990 | -89.68 | 15.09 | 97.12 | 0.09 | 2.80 | 1569 |
| 2024-09-20 22:21:37.331 | MS1 | 121.4656655562 | 31.1446210539 | 614 | 504990 | -89.54 | 10.57 | 85.90 | 0.11 | 2.82 | 1581 |
| 2024-09-20 22:21:38.395 | MS1 | 121.4656619855 | 31.1446214562 | 614 | 504990 | -90.67 | 12.92 | 95.78 | 0.17 | 2.42 | 1576 |
| 2024-09-20 22:21:39.997 | MS1 | 121.4656742735 | 31.1446191702 | 614 | 504990 | -91.22 | 11.63 | 76.03 | 0.18 | 2.48 | 1589 |
| 2024-09-20 22:21:40.439 | MS1 | 121.4656673914 | 31.1446228299 | 614 | 504990 | -93.16 | 8.42 | 424.00 | 0.13 | 2.36 | 1591 |
| 2024-09-20 22:21:41.982 | MS1 | 121.4656725867 | 31.1446307599 | 614 | 504990 | -89.22 | 9.67 | 587.52 | 0.11 | 2.62 | 1594 |
| 2024-09-20 22:21:42.563 | MS1 | 121.4656612391 | 31.1446329207 | 614 | 504990 | -93.87 | 11.51 | 488.27 | 0.06 | 2.51 | 1585 |

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
| 3259183 | 4 | 121.4731841184 | 31.1508745449 | 165 | 13 | 5 | 23.4 | TDD | 614 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3262395 | 2 | 121.4732856942 | 31.1520256946 | 236 | 1 | 5 | 43.1 | TDD | 922 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3267133 | 1 | 121.4756397160 | 31.1485475199 | 85 | 5 | 4 | 33.2 | TDD | 16 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3274075 | 3 | 121.4707658212 | 31.1454925539 | 356 | 4 | 4 | 44.1 | TDD | 916 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:31.503 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.526 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.664 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.664 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.347 | NREventA3 | measId:2;ServCellPCI:953;Se... |
| 2024-09-20 22:21:38.587 | NRHandoverAttempt | SourcePCI:953;SourceNR-ARFC... |
| 2024-09-20 22:21:38.637 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.652 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.771 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.771 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3267133 | 1 | 83.5752 | 84.8990 | -114.3253 | 6.1742 | 92.5710 | 0.0016 | 0.0081 |
| 2024_09_19 22:00 | 3262395 | 2 | 76.7349 | 75.3538 | -114.9610 | 12.3285 | 183.9857 | 0.0153 | 0.0040 |
| 2024_09_19 22:00 | 3274075 | 3 | 93.9436 | 79.5540 | -116.2727 | 18.8888 | 137.3612 | 0.0199 | 0.0054 |
| 2024_09_19 22:00 | 3259183 | 4 | 76.2612 | 85.3603 | -115.5596 | 6.4651 | 98.1006 | 0.0097 | 0.0059 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415399_690622FE | 504990 | 614 | -90.0 | 504990 | 922 | -94.0 | 504990 | 916 | -104.2 | 504990 | 16 |
| MR_1774415399_EC684735 | 504990 | 614 | -90.3 | 504990 | 922 | -95.3 | 504990 | 916 | -107.5 | 504990 | 16 |
| MR_1774415399_CDB9929A | 504990 | 614 | -89.5 | 504990 | 922 | -95.3 | 504990 | 916 | -107.0 | 504990 | 16 |
| MR_1774415399_E84A9D41 | 504990 | 614 | -91.5 | 504990 | 922 | -92.2 | 504990 | 916 | -104.0 | 504990 | 16 |
| MR_1774415399_BD5D40C2 | 504990 | 614 | -89.5 | 504990 | 922 | -93.3 | 504990 | 916 | -107.0 | 504990 | 16 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 232: `d7f93cd4-05f...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `d7f93cd4-05f6-41f0-b44e-0dc3d459aa62` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[232] topology](images/test_0232.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3213499_4 and 3254312_1
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3213499_4
- `C3`: Increase A3 Offset threshold for 3213499_4
- `C4`: Lift the tilt angle  of 3254312_1 by 5 degrees
- `C5`: Check test server and transmission issues
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3254312_1
- `C7`: Decrease A3 Offset threshold for 3254312_1
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3254312_1
- `C9`: Decrease transmission power for 3213499_4
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3213499_4
- `C11`: Increase transmission power for 3213499_4
- `C12`: Add neighbor relationship between 3264842_11 and 3254312_1
- `C13`: Decrease transmission power for 3254312_1
- `C14`: Decrease A3 Offset threshold for 3213499_4
- `C15`: Increase A3 Offset threshold for 3254312_1
- `C16`: Press down the tilt angle of 3213499_4 by 4 degrees
- `C17`: Increase transmission power for 3254312_1
- `C18`: Adjust the azimuth of 3213499_4 by 24 degrees
- `C19`: Insufficient data; more data is needed for judgment.
- `C20`: Adjust the azimuth of 3254312_1 by 32 degrees
- `C21`: Lift the tilt angle of 3213499_4 by 4 degrees
- `C22`: Press down the tilt angle  of 3254312_1 by 5 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.878 | MS1 | 121.4656721234 | 31.1446367176 | 816 | 504990 | -94.48 | 14.48 | 424.60 | 0.12 | 2.28 | 1584 |
| 2024-09-20 22:21:32.352 | MS1 | 121.4656665282 | 31.1446335034 | 333 | 504990 | -94.18 | 13.20 | 417.31 | 0.19 | 2.69 | 1591 |
| 2024-09-20 22:21:33.730 | MS1 | 121.4656638180 | 31.1446190981 | 720 | 504990 | -94.12 | 9.90 | 382.51 | 0.16 | 2.62 | 1595 |
| 2024-09-20 22:21:34.829 | MS1 | 121.4656678705 | 31.1446303917 | 626 | 152650 | -90.45 | 7.19 | 44.92 | 0.01 | 1.70 | 964 |
| 2024-09-20 22:21:35.957 | MS1 | 121.4656663146 | 31.1446232482 | 869 | 152650 | -95.21 | 2.97 | 55.93 | 0.13 | 1.94 | 952 |
| 2024-09-20 22:21:36.299 | MS1 | 121.4656665158 | 31.1446366392 | 209 | 152650 | -91.83 | 4.16 | 58.93 | 0.06 | 1.78 | 915 |
| 2024-09-20 22:21:37.447 | MS1 | 121.4656590375 | 31.1446238215 | 548 | 152650 | -91.79 | 7.40 | 84.36 | 0.02 | 1.64 | 909 |
| 2024-09-20 22:21:38.562 | MS1 | 121.4656700437 | 31.1446333160 | 626 | 152650 | -89.69 | 6.71 | 66.88 | 0.06 | 1.52 | 988 |
| 2024-09-20 22:21:39.350 | MS1 | 121.4656644701 | 31.1446286546 | 869 | 152650 | -89.75 | 5.39 | 68.90 | 0.04 | 1.75 | 936 |
| 2024-09-20 22:21:40.807 | MS1 | 121.4656729030 | 31.1446208617 | 209 | 152650 | -88.12 | 2.86 | 68.09 | 0.18 | 2.80 | 1583 |
| 2024-09-20 22:21:41.671 | MS1 | 121.4656608802 | 31.1446216962 | 548 | 152650 | -88.30 | 6.31 | 73.17 | 0.14 | 2.44 | 1589 |
| 2024-09-20 22:21:42.266 | MS1 | 121.4656647226 | 31.1446259544 | 626 | 152650 | -90.20 | 7.85 | 74.42 | 0.12 | 2.31 | 1600 |

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
| 3213499 | 4 | 121.4726517438 | 31.1557892019 | 232 | 3 | 7 | 17.3 | TDD | 816 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3218348 | 6 | 121.4686410142 | 31.1442516607 | 340 | 1 | 6 | 3.1 | TDD | 311 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3230420 | 10 | 121.4694021472 | 31.1551009177 | 223 | 1 | 1 | 7.6 | FDD | 336 | n1 | 152650 | 30M | 4T4R | 27 | 152650 |
| 3237007 | 3 | 121.4707951624 | 31.1533949996 | 141 | 0 | 4 | 1.3 | TDD | 333 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3246017 | 5 | 121.4731158171 | 31.1502723096 | 179 | 2 | 8 | 15.9 | TDD | 720 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3254312 | 1 | 121.4658399133 | 31.1532028306 | 149 | 5 | 4 | 3.7 | TDD | 775 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3256816 | 13 | 121.4657721843 | 31.1465067926 | 105 | 12 | 3 | 27.7 | FDD | 54 | n1 | 152650 | 30M | 4T4R | 21 | 152650 |
| 3264842 | 11 | 121.4744261986 | 31.1503650960 | 327 | 11 | 2 | 15.1 | FDD | 209 | n1 | 152650 | 30M | 4T4R | 13 | 152650 |
| 3267412 | 7 | 121.4670636860 | 31.1553784930 | 224 | 14 | 4 | 20.1 | FDD | 548 | n1 | 152650 | 30M | 4T4R | 13 | 152650 |
| 3269240 | 8 | 121.4720565092 | 31.1528797184 | 59 | 6 | 5 | 12.5 | FDD | 869 | n1 | 152650 | 30M | 4T4R | 18 | 152650 |
| 3269642 | 9 | 121.4701092167 | 31.1476556627 | 80 | 1 | 4 | 24.5 | FDD | 585 | n1 | 152650 | 30M | 4T4R | 18 | 152650 |
| 3273862 | 2 | 121.4656444424 | 31.1480446405 | 242 | 9 | 6 | 2.4 | TDD | 363 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3278891 | 12 | 121.4678757720 | 31.1554068777 | 318 | 15 | 3 | 25.6 | FDD | 626 | n1 | 152650 | 30M | 4T4R | 13 | 152650 |

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
| 2024-09-20 22:21:30.813 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.836 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:30.938 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.938 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.653 | NREventA2 | measId:1;ServCellPCI:985;Se... |
| 2024-09-20 22:21:34.777 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.045 | NREventA5 | measId:3;ServCellPCI:985;Se... |
| 2024-09-20 22:21:35.111 | NRHandoverAttempt | SourcePCI:985;SourceNR-ARFC... |
| 2024-09-20 22:21:35.135 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.145 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:35.262 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.262 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3254312 | 1 | 9.0283 | 16.0535 | -117.6772 | 16.7937 | 125.6869 | 0.0170 | 0.0113 |
| 2024_09_20 22:00 | 3273862 | 2 | 8.2899 | 5.4924 | -116.4342 | 9.0783 | 138.7244 | 0.0176 | 0.0141 |
| 2024_09_20 22:00 | 3237007 | 3 | 9.6923 | 6.7817 | -116.9274 | 5.4587 | 152.3339 | 0.0104 | 0.0160 |
| 2024_09_20 22:00 | 3213499 | 4 | 10.0358 | 7.7325 | -114.0962 | 12.8037 | 88.1386 | 0.0199 | 0.0190 |
| 2024_09_20 22:00 | 3246017 | 5 | 12.1147 | 9.2242 | -116.4790 | 17.2569 | 141.5293 | 0.0020 | 0.0121 |
| 2024_09_20 22:00 | 3218348 | 6 | 12.8522 | 16.7087 | -116.5623 | 6.1760 | 119.4826 | 0.0039 | 0.0102 |
| 2024_09_20 22:00 | 3267412 | 7 | 17.2704 | 7.5270 | -116.7078 | 3.4759 | 24.2925 | 0.0020 | 0.0115 |
| 2024_09_20 22:00 | 3269240 | 8 | 17.2168 | 13.8115 | -115.4178 | 3.9704 | 35.4690 | 0.0166 | 0.0048 |
| 2024_09_20 22:00 | 3269642 | 9 | 10.0931 | 7.0833 | -114.1385 | 4.1086 | 34.8045 | 0.0194 | 0.0001 |
| 2024_09_20 22:00 | 3230420 | 10 | 5.0820 | 5.2031 | -115.9824 | 4.6937 | 39.3791 | 0.0173 | 0.0043 |
| 2024_09_20 22:00 | 3264842 | 11 | 11.7038 | 6.9860 | -115.0380 | 4.8340 | 25.9046 | 0.0055 | 0.0120 |
| 2024_09_20 22:00 | 3278891 | 12 | 16.2564 | 14.0880 | -114.4594 | 4.1029 | 31.6955 | 0.0049 | 0.0150 |
| 2024_09_20 22:00 | 3256816 | 13 | 9.3674 | 15.8453 | -117.1868 | 3.3102 | 32.2420 | 0.0151 | 0.0093 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413893_7CA5036C | 504990 | 720 | -93.5 | 504990 | 775 | -96.3 | 504990 | 311 | -97.5 | 504990 | 363 |
| MR_1774413893_782862E1 | 504990 | 720 | -95.0 | 504990 | 775 | -95.3 | 504990 | 311 | -98.2 | 504990 | 363 |
| MR_1774413893_29F55DCB | 504990 | 720 | -92.5 | 504990 | 775 | -97.6 | 504990 | 311 | -97.6 | 504990 | 363 |
| MR_1774413893_77E5584A | 152650 | 626 | -89.2 | 152650 | 585 | -96.7 | 152650 | 336 | -99.5 | 152650 | 54 |
| MR_1774413893_EF9629C3 | 152650 | 626 | -91.4 | 152650 | 585 | -93.6 | 152650 | 336 | -98.5 | 152650 | 54 |
| MR_1774413893_B7934545 | 504990 | 720 | -93.9 | 504990 | 775 | -97.7 | 504990 | 311 | -97.1 | 504990 | 363 |
| MR_1774413893_791B88AD | 152650 | 626 | -90.0 | 152650 | 585 | -94.1 | 152650 | 336 | -98.2 | 152650 | 54 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 233: `96a1171c-84d...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `96a1171c-84da-4f8f-a9da-35b22f265b8e` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[233] topology](images/test_0233.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3266763_1
- `C2`: Lift the tilt angle  of 3250200_5 by 1 degrees
- `C3`: Adjust the azimuth of 3266763_1 by 5 degrees
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3250200_5
- `C5`: Insufficient data; more data is needed for judgment.
- `C6`: Press down the tilt angle of 3266763_1 by 5 degrees
- `C7`: Lift the tilt angle of 3266763_1 by 5 degrees
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3266763_1
- `C9`: Increase A3 Offset threshold for 3266763_1
- `C10`: Decrease transmission power for 3266763_1
- `C11`: Decrease A3 Offset threshold for 3250200_5
- `C12`: Increase transmission power for 3266763_1
- `C13`: Increase transmission power for 3250200_5
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3266763_1
- `C15`: Add neighbor relationship between 3211212_13 and 3250200_5
- `C16`: Add neighbor relationship between 3266763_1 and 3250200_5
- `C17`: Check test server and transmission issues
- `C18`: Decrease transmission power for 3250200_5
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3250200_5
- `C20`: Increase A3 Offset threshold for 3250200_5
- `C21`: Press down the tilt angle  of 3250200_5 by 1 degrees
- `C22`: Adjust the azimuth of 3250200_5 by 39 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.468 | MS1 | 121.4656604702 | 31.1446283371 | 386 | 504990 | -93.86 | 9.35 | 449.55 | 0.19 | 2.31 | 1578 |
| 2024-09-20 22:21:32.489 | MS1 | 121.4656616944 | 31.1446285655 | 178 | 504990 | -94.09 | 14.52 | 342.85 | 0.01 | 2.67 | 1569 |
| 2024-09-20 22:21:33.829 | MS1 | 121.4656760620 | 31.1446279634 | 202 | 504990 | -95.66 | 9.64 | 320.81 | 0.00 | 2.03 | 1586 |
| 2024-09-20 22:21:34.368 | MS1 | 121.4656749304 | 31.1446193538 | 167 | 152650 | -87.72 | 2.28 | 105.42 | 0.06 | 1.95 | 905 |
| 2024-09-20 22:21:35.583 | MS1 | 121.4656602285 | 31.1446349681 | 897 | 152650 | -89.67 | 4.43 | 103.95 | 0.17 | 1.92 | 987 |
| 2024-09-20 22:21:36.780 | MS1 | 121.4656616727 | 31.1446260270 | 92 | 152650 | -91.46 | 7.09 | 86.75 | 0.06 | 1.96 | 901 |
| 2024-09-20 22:21:37.830 | MS1 | 121.4656591020 | 31.1446358962 | 459 | 152650 | -96.86 | 7.12 | 61.58 | 0.01 | 1.98 | 906 |
| 2024-09-20 22:21:38.789 | MS1 | 121.4656580058 | 31.1446186859 | 167 | 152650 | -88.01 | 5.74 | 76.46 | 0.18 | 1.90 | 919 |
| 2024-09-20 22:21:39.772 | MS1 | 121.4656588357 | 31.1446228046 | 897 | 152650 | -89.48 | 6.89 | 93.14 | 0.18 | 1.91 | 905 |
| 2024-09-20 22:21:40.815 | MS1 | 121.4656618628 | 31.1446269797 | 92 | 152650 | -90.41 | 5.48 | 82.42 | 0.13 | 2.41 | 1586 |
| 2024-09-20 22:21:41.183 | MS1 | 121.4656644618 | 31.1446227603 | 459 | 152650 | -94.08 | 6.40 | 80.85 | 0.04 | 2.13 | 1563 |
| 2024-09-20 22:21:42.961 | MS1 | 121.4656592569 | 31.1446371474 | 167 | 152650 | -93.17 | 5.92 | 80.45 | 0.11 | 2.86 | 1585 |

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
| 3211212 | 13 | 121.4666937067 | 31.1477807712 | 136 | 13 | 7 | 0.4 | FDD | 92 | n1 | 152650 | 30M | 4T4R | 15 | 152650 |
| 3215008 | 9 | 121.4643751778 | 31.1527020416 | 130 | 4 | 6 | 5.7 | FDD | 962 | n1 | 152650 | 30M | 4T4R | 20 | 152650 |
| 3216865 | 2 | 121.4646514516 | 31.1484423494 | 111 | 8 | 6 | 26.0 | TDD | 647 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3243628 | 3 | 121.4644473675 | 31.1499625394 | 7 | 5 | 4 | 21.5 | TDD | 202 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3245462 | 8 | 121.4756541884 | 31.1468047941 | 263 | 11 | 6 | 4.7 | FDD | 897 | n1 | 152650 | 30M | 4T4R | 17 | 152650 |
| 3250200 | 5 | 121.4698668142 | 31.1540081582 | 240 | 0 | 12 | 25.0 | TDD | 18 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3258729 | 10 | 121.4728926115 | 31.1486912936 | 223 | 7 | 5 | 1.7 | FDD | 167 | n1 | 152650 | 30M | 4T4R | 10 | 152650 |
| 3260248 | 6 | 121.4667857594 | 31.1558122914 | 51 | 13 | 2 | 18.8 | TDD | 439 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3262848 | 11 | 121.4642871368 | 31.1447440187 | 78 | 3 | 12 | 19.9 | FDD | 459 | n1 | 152650 | 30M | 4T4R | 29 | 152650 |
| 3266005 | 7 | 121.4730919468 | 31.1489902607 | 10 | 11 | 12 | 23.4 | FDD | 32 | n1 | 152650 | 30M | 4T4R | 27 | 152650 |
| 3266763 | 1 | 121.4719517563 | 31.1448694588 | 263 | 3 | 0 | 16.2 | TDD | 386 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3268787 | 12 | 121.4676062941 | 31.1530584158 | 99 | 13 | 1 | 13.3 | FDD | 402 | n1 | 152650 | 30M | 4T4R | 24 | 152650 |
| 3271245 | 4 | 121.4741233446 | 31.1538312532 | 255 | 10 | 3 | 1.8 | TDD | 178 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |

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
| 2024-09-20 22:21:31.515 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.534 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.670 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.670 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.359 | NREventA2 | measId:1;ServCellPCI:457;Se... |
| 2024-09-20 22:21:35.473 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.718 | NREventA5 | measId:3;ServCellPCI:457;Se... |
| 2024-09-20 22:21:35.755 | NRHandoverAttempt | SourcePCI:457;SourceNR-ARFC... |
| 2024-09-20 22:21:35.777 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.789 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:35.925 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.925 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3266763 | 1 | 18.9056 | 5.4139 | -117.2384 | 16.2109 | 108.6848 | 0.0159 | 0.0166 |
| 2024_09_20 22:00 | 3216865 | 2 | 16.7457 | 6.1051 | -114.2510 | 10.7416 | 163.7991 | 0.0153 | 0.0018 |
| 2024_09_20 22:00 | 3243628 | 3 | 11.6803 | 19.6992 | -116.6964 | 16.6588 | 91.6357 | 0.0189 | 0.0168 |
| 2024_09_20 22:00 | 3271245 | 4 | 14.1427 | 6.0040 | -114.2241 | 5.9452 | 131.1238 | 0.0197 | 0.0091 |
| 2024_09_20 22:00 | 3250200 | 5 | 19.7778 | 15.4841 | -115.2892 | 14.6784 | 137.1498 | 0.0124 | 0.0169 |
| 2024_09_20 22:00 | 3260248 | 6 | 7.6564 | 9.1360 | -115.2795 | 6.9451 | 177.8730 | 0.0008 | 0.0053 |
| 2024_09_20 22:00 | 3266005 | 7 | 11.5320 | 14.9868 | -114.7769 | 4.4219 | 23.4520 | 0.0156 | 0.0007 |
| 2024_09_20 22:00 | 3245462 | 8 | 9.6982 | 15.8110 | -115.7722 | 3.0454 | 46.2558 | 0.0064 | 0.0156 |
| 2024_09_20 22:00 | 3215008 | 9 | 13.7946 | 11.0430 | -114.8585 | 3.6126 | 46.1978 | 0.0032 | 0.0158 |
| 2024_09_20 22:00 | 3258729 | 10 | 17.4599 | 6.7871 | -115.2744 | 3.7848 | 42.1678 | 0.0118 | 0.0088 |
| 2024_09_20 22:00 | 3262848 | 11 | 11.9175 | 12.6881 | -115.5384 | 4.2742 | 50.5603 | 0.0060 | 0.0172 |
| 2024_09_20 22:00 | 3268787 | 12 | 13.2772 | 19.4495 | -114.9349 | 4.5451 | 20.0407 | 0.0098 | 0.0139 |
| 2024_09_20 22:00 | 3211212 | 13 | 10.5854 | 15.9346 | -115.9289 | 3.4776 | 51.8380 | 0.0183 | 0.0171 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412768_D8131194 | 504990 | 202 | -97.3 | 504990 | 18 | -100.7 | 504990 | 647 | -101.1 | 504990 | 439 |
| MR_1774412768_C5242C50 | 152650 | 92 | -93.1 | 152650 | 32 | -99.1 | 152650 | 402 | -99.2 | 152650 | 962 |
| MR_1774412768_0FCFAA62 | 152650 | 92 | -90.9 | 152650 | 32 | -99.1 | 152650 | 402 | -100.7 | 152650 | 962 |
| MR_1774412768_E5213CC3 | 152650 | 92 | -91.6 | 152650 | 32 | -100.7 | 152650 | 402 | -100.7 | 152650 | 962 |
| MR_1774412768_2854C68C | 152650 | 92 | -90.9 | 152650 | 32 | -97.9 | 152650 | 402 | -99.0 | 152650 | 962 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 234: `181effab-f64...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `181effab-f64c-4091-b44d-443386468716` |
| Tag | **multiple-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[234] topology](images/test_0234.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 5 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 5개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3255513_1 by 31 degrees
- `C2`: Increase A3 Offset threshold for 3255513_1
- `C3`: Increase transmission power for 3246729_2
- `C4`: Decrease transmission power for 3246729_2
- `C5`: Decrease A3 Offset threshold for 3246729_2
- `C6`: Insufficient data; more data is needed for judgment.
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3246729_2
- `C8`: Decrease A3 Offset threshold for 3255513_1
- `C9`: Press down the tilt angle of 3255513_1 by 4 degrees
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3255513_1
- `C11`: Decrease transmission power for 3255513_1
- `C12`: Lift the tilt angle  of 3246729_2 by 3 degrees
- `C13`: Check test server and transmission issues
- `C14`: Adjust the azimuth of 3246729_2 by 21 degrees
- `C15`: Increase A3 Offset threshold for 3246729_2
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3255513_1
- `C17`: Add neighbor relationship between 3255513_1 and 3246729_2
- `C18`: Press down the tilt angle  of 3246729_2 by 3 degrees
- `C19`: Lift the tilt angle of 3255513_1 by 4 degrees
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3246729_2
- `C21`: Add neighbor relationship between 3216895_5 and 3246729_2
- `C22`: Increase transmission power for 3255513_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.290 | MS1 | 121.4656634346 | 31.1446227577 | 79 | 504990 | -76.75 | 17.52 | 494.18 | 0.05 | 2.94 | 1560 |
| 2024-09-20 22:21:32.302 | MS1 | 121.4656664678 | 31.1446308339 | 79 | 504990 | -82.34 | 17.86 | 508.19 | 0.02 | 2.01 | 1584 |
| 2024-09-20 22:21:33.691 | MS1 | 121.4656773667 | 31.1446266173 | 79 | 504990 | -81.13 | 17.39 | 386.47 | 0.05 | 2.42 | 1581 |
| 2024-09-20 22:21:34.411 | MS1 | 121.4656728815 | 31.1446203498 | 821 | 504990 | -84.83 | 3.10 | 56.39 | 0.03 | 1.03 | 1582 |
| 2024-09-20 22:21:35.758 | MS1 | 121.4656626622 | 31.1446318197 | 821 | 504990 | -88.31 | 2.04 | 68.53 | 0.07 | 1.26 | 1578 |
| 2024-09-20 22:21:36.555 | MS1 | 121.4656697874 | 31.1446222094 | 79 | 504990 | -87.29 | 4.17 | 71.80 | 0.08 | 1.47 | 1566 |
| 2024-09-20 22:21:37.471 | MS1 | 121.4656596351 | 31.1446376213 | 79 | 504990 | -81.77 | 3.78 | 45.15 | 0.12 | 1.47 | 1588 |
| 2024-09-20 22:21:38.707 | MS1 | 121.4656590576 | 31.1446328030 | 821 | 504990 | -83.18 | 3.25 | 36.08 | 0.01 | 1.20 | 1571 |
| 2024-09-20 22:21:39.818 | MS1 | 121.4656640587 | 31.1446319238 | 821 | 504990 | -80.43 | 2.67 | 43.50 | 0.03 | 1.38 | 1576 |
| 2024-09-20 22:21:40.198 | MS1 | 121.4656691649 | 31.1446214490 | 821 | 504990 | -75.55 | 12.24 | 364.03 | 0.20 | 2.19 | 1577 |
| 2024-09-20 22:21:41.408 | MS1 | 121.4656645123 | 31.1446215241 | 821 | 504990 | -77.01 | 14.04 | 363.30 | 0.06 | 2.28 | 1566 |
| 2024-09-20 22:21:42.914 | MS1 | 121.4656670749 | 31.1446291465 | 821 | 504990 | -80.69 | 15.11 | 557.34 | 0.09 | 2.01 | 1571 |

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
| 3216895 | 5 | 121.4726187619 | 31.1528025162 | 176 | 1 | 11 | 37.9 | TDD | 987 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3246729 | 2 | 121.4744689104 | 31.1492544922 | 217 | 1 | 10 | 41.3 | TDD | 946 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3255513 | 1 | 121.4726240907 | 31.1461870845 | 286 | 1 | 12 | 37.8 | TDD | 79 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3261529 | 3 | 121.4745129514 | 31.1543096097 | 124 | 15 | 7 | 47.8 | TDD | 596 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3277862 | 4 | 121.4650333019 | 31.1494973670 | 327 | 8 | 0 | 17.3 | TDD | 821 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |

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
| 2024-09-20 22:21:30.966 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.985 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.088 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.088 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:33.844 | NREventA3 | measId:2;ServCellPCI:693;Se... |
| 2024-09-20 22:21:34.084 | NRHandoverAttempt | SourcePCI:693;SourceNR-ARFC... |
| 2024-09-20 22:21:34.117 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:34.132 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:34.282 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:34.282 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.844 | NREventA3 | measId:2;ServCellPCI:356;Se... |
| 2024-09-20 22:21:36.084 | NRHandoverAttempt | SourcePCI:356;SourceNR-ARFC... |
| 2024-09-20 22:21:36.119 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:36.132 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:36.239 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.239 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.844 | NREventA3 | measId:2;ServCellPCI:693;Se... |
| 2024-09-20 22:21:38.084 | NRHandoverAttempt | SourcePCI:693;SourceNR-ARFC... |
| 2024-09-20 22:21:38.118 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.128 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.232 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.232 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3255513 | 1 | 15.2702 | 17.8852 | -114.8122 | 18.7816 | 149.1552 | 0.0082 | 0.0097 |
| 2024_09_20 22:00 | 3246729 | 2 | 5.7785 | 6.7125 | -117.8443 | 12.0920 | 172.7311 | 0.0010 | 0.0110 |
| 2024_09_20 22:00 | 3261529 | 3 | 10.6826 | 9.5359 | -114.8277 | 7.5667 | 120.7654 | 0.0147 | 0.0177 |
| 2024_09_20 22:00 | 3277862 | 4 | 17.4608 | 9.1520 | -116.1387 | 11.6253 | 146.6286 | 0.0169 | 0.0041 |
| 2024_09_20 22:00 | 3216895 | 5 | 15.9382 | 5.8879 | -114.7599 | 11.5692 | 157.1433 | 0.0194 | 0.0025 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414441_E0F772C8 | 504990 | 821 | -85.5 | 504990 | 79 | -83.7 | 504990 | 946 | -82.5 | 504990 | 987 |
| MR_1774414441_FE66BD3D | 504990 | 821 | -85.6 | 504990 | 79 | -83.6 | 504990 | 946 | -85.0 | 504990 | 987 |
| MR_1774414441_108AD882 | 504990 | 79 | -84.0 | 504990 | 821 | -82.9 | 504990 | 946 | -85.1 | 504990 | 987 |
| MR_1774414441_1FDF3515 | 504990 | 79 | -84.5 | 504990 | 821 | -81.6 | 504990 | 946 | -83.2 | 504990 | 987 |
| MR_1774414441_DF5EB008 | 504990 | 821 | -83.8 | 504990 | 79 | -83.9 | 504990 | 946 | -83.1 | 504990 | 987 |
| MR_1774414441_D5AB90A4 | 504990 | 821 | -86.3 | 504990 | 79 | -82.4 | 504990 | 946 | -85.4 | 504990 | 987 |
| MR_1774414441_F8740420 | 504990 | 821 | -83.8 | 504990 | 79 | -83.0 | 504990 | 946 | -82.1 | 504990 | 987 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 235: `9c4b3b5e-f34...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `9c4b3b5e-f343-4d56-974b-4f373705bbcf` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[235] topology](images/test_0235.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3237860_1
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3237860_1
- `C3`: Adjust the azimuth of 3237860_1 by 30 degrees
- `C4`: Decrease A3 Offset threshold for 3211968_2
- `C5`: Increase A3 Offset threshold for 3211968_2
- `C6`: Insufficient data; more data is needed for judgment.
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3211968_2
- `C8`: Decrease A3 Offset threshold for 3237860_1
- `C9`: Press down the tilt angle  of 3211968_2 by 10 degrees
- `C10`: Increase transmission power for 3211968_2
- `C11`: Adjust the azimuth of 3211968_2 by 50 degrees
- `C12`: Check test server and transmission issues
- `C13`: Decrease transmission power for 3211968_2
- `C14`: Decrease transmission power for 3237860_1
- `C15`: Increase A3 Offset threshold for 3237860_1
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3237860_1
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3211968_2
- `C18`: Press down the tilt angle of 3237860_1 by 8 degrees
- `C19`: Lift the tilt angle  of 3211968_2 by 10 degrees
- `C20`: Lift the tilt angle of 3237860_1 by 8 degrees
- `C21`: Add neighbor relationship between 3237860_1 and 3211968_2
- `C22`: Add neighbor relationship between 3214884_3 and 3211968_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.213 | MS1 | 121.4656677324 | 31.1446209302 | 231 | 504990 | -84.17 | 17.86 | 357.20 | 0.20 | 2.15 | 1582 |
| 2024-09-20 22:21:32.308 | MS1 | 121.4656776114 | 31.1446341770 | 231 | 504990 | -78.33 | 14.90 | 456.83 | 0.07 | 2.95 | 1562 |
| 2024-09-20 22:21:33.318 | MS1 | 121.4656776451 | 31.1446276206 | 231 | 504990 | -75.04 | 16.50 | 570.55 | 0.16 | 2.28 | 1573 |
| 2024-09-20 22:21:34.537 | MS1 | 121.4656714646 | 31.1446288429 | 231 | 504990 | -84.20 | -3.30 | 66.59 | 0.03 | 1.12 | 1560 |
| 2024-09-20 22:21:35.763 | MS1 | 121.4656581544 | 31.1446313877 | 231 | 504990 | -90.80 | -2.41 | 25.17 | 0.08 | 1.43 | 1564 |
| 2024-09-20 22:21:36.793 | MS1 | 121.4656764655 | 31.1446269774 | 231 | 504990 | -88.86 | -0.48 | 44.38 | 0.01 | 1.24 | 1600 |
| 2024-09-20 22:21:37.344 | MS1 | 121.4656734986 | 31.1446337366 | 231 | 504990 | -85.83 | -2.78 | 42.43 | 0.17 | 1.23 | 1570 |
| 2024-09-20 22:21:38.958 | MS1 | 121.4656636991 | 31.1446279672 | 231 | 504990 | -89.62 | -3.99 | 57.82 | 0.00 | 1.25 | 1575 |
| 2024-09-20 22:21:39.869 | MS1 | 121.4656752050 | 31.1446213255 | 756 | 504990 | -76.96 | 17.38 | 241.93 | 0.18 | 1.05 | 1594 |
| 2024-09-20 22:21:40.976 | MS1 | 121.4656691531 | 31.1446250688 | 756 | 504990 | -81.03 | 16.92 | 417.67 | 0.12 | 2.96 | 1569 |
| 2024-09-20 22:21:41.675 | MS1 | 121.4656714853 | 31.1446333572 | 756 | 504990 | -82.35 | 15.58 | 586.38 | 0.03 | 2.24 | 1563 |
| 2024-09-20 22:21:42.946 | MS1 | 121.4656666796 | 31.1446247237 | 756 | 504990 | -80.30 | 14.25 | 342.60 | 0.06 | 2.17 | 1563 |

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
| 3211968 | 2 | 121.4726955395 | 31.1442659237 | 213 | 11 | 9 | 33.6 | TDD | 756 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3214884 | 3 | 121.4698149929 | 31.1452703246 | 184 | 9 | 1 | 26.6 | TDD | 573 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3226511 | 4 | 121.4685837018 | 31.1528576375 | 349 | 15 | 8 | 48.8 | TDD | 255 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3237860 | 1 | 121.4698153803 | 31.1556314488 | 228 | 7 | 4 | 18.6 | TDD | 231 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:31.040 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.065 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.178 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.178 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.869 | NREventA3 | measId:2;ServCellPCI:371;Se... |
| 2024-09-20 22:21:38.109 | NRHandoverAttempt | SourcePCI:371;SourceNR-ARFC... |
| 2024-09-20 22:21:38.150 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.160 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.260 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.260 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3237860 | 1 | 6.3696 | 11.3153 | -117.2052 | 13.1381 | 122.4808 | 0.0132 | 0.1121 |
| 2024_09_20 22:00 | 3211968 | 2 | 16.1299 | 7.9478 | -115.9594 | 10.5948 | 140.4398 | 0.0115 | 0.0181 |
| 2024_09_20 22:00 | 3214884 | 3 | 18.4515 | 11.8599 | -115.6620 | 9.5772 | 110.7433 | 0.0117 | 0.0173 |
| 2024_09_20 22:00 | 3226511 | 4 | 5.3068 | 11.2672 | -115.5511 | 18.7254 | 147.5491 | 0.0065 | 0.0160 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416090_C3498888 | 504990 | 756 | -81.1 | 504990 | 231 | -83.5 | 504990 | 573 | -85.2 | 504990 | 255 |
| MR_1774416090_3B2674C4 | 504990 | 231 | -83.9 | 504990 | 756 | -79.5 | 504990 | 573 | -84.3 | 504990 | 255 |
| MR_1774416090_65D7D9C9 | 504990 | 756 | -79.5 | 504990 | 231 | -85.7 | 504990 | 573 | -86.5 | 504990 | 255 |
| MR_1774416090_05611D06 | 504990 | 756 | -78.6 | 504990 | 231 | -85.6 | 504990 | 573 | -84.6 | 504990 | 255 |
| MR_1774416090_4C0E9A9E | 504990 | 231 | -84.4 | 504990 | 756 | -78.6 | 504990 | 573 | -83.9 | 504990 | 255 |
| MR_1774416090_275E40E7 | 504990 | 231 | -83.4 | 504990 | 756 | -79.0 | 504990 | 573 | -85.4 | 504990 | 255 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 236: `b6db3a8a-712...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `b6db3a8a-7126-4a0a-8d0d-f171fac37711` |
| Tag | **multiple-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[236] topology](images/test_0236.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle  of 3244242_2 by 5 degrees
- `C2`: Press down the tilt angle of 3246207_3 by 6 degrees
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3244242_2
- `C4`: Increase A3 Offset threshold for 3244242_2
- `C5`: Press down the tilt angle  of 3244242_2 by 5 degrees
- `C6`: Decrease A3 Offset threshold for 3246207_3
- `C7`: Insufficient data; more data is needed for judgment.
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3246207_3
- `C9`: Adjust the azimuth of 3246207_3 by 34 degrees
- `C10`: Increase A3 Offset threshold for 3246207_3
- `C11`: Add neighbor relationship between 3215052_1 and 3244242_2
- `C12`: Adjust the azimuth of 3244242_2 by 17 degrees
- `C13`: Increase transmission power for 3246207_3
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3246207_3
- `C15`: Decrease A3 Offset threshold for 3244242_2
- `C16`: Increase transmission power for 3244242_2
- `C17`: Lift the tilt angle of 3246207_3 by 6 degrees
- `C18`: Decrease transmission power for 3246207_3
- `C19`: Check test server and transmission issues
- `C20`: Add neighbor relationship between 3246207_3 and 3244242_2
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3244242_2
- `C22`: Decrease transmission power for 3244242_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.424 | MS1 | 121.4656672389 | 31.1446239618 | 267 | 504990 | -80.50 | 13.69 | 466.19 | 0.19 | 2.71 | 1596 |
| 2024-09-20 22:21:32.745 | MS1 | 121.4656753300 | 31.1446210828 | 267 | 504990 | -82.52 | 17.82 | 483.34 | 0.02 | 2.43 | 1593 |
| 2024-09-20 22:21:33.565 | MS1 | 121.4656643457 | 31.1446213174 | 267 | 504990 | -77.07 | 15.54 | 360.11 | 0.01 | 2.59 | 1576 |
| 2024-09-20 22:21:34.440 | MS1 | 121.4656685781 | 31.1446213183 | 267 | 504990 | -94.84 | 0.34 | 82.34 | 0.10 | 1.47 | 1568 |
| 2024-09-20 22:21:35.866 | MS1 | 121.4656627363 | 31.1446231642 | 267 | 504990 | -91.67 | 1.83 | 34.71 | 0.15 | 1.06 | 1583 |
| 2024-09-20 22:21:36.686 | MS1 | 121.4656610609 | 31.1446294757 | 267 | 504990 | -94.82 | 1.36 | 40.60 | 0.02 | 1.44 | 1593 |
| 2024-09-20 22:21:37.744 | MS1 | 121.4656626656 | 31.1446230931 | 267 | 504990 | -87.79 | 1.72 | 55.82 | 0.03 | 1.21 | 1590 |
| 2024-09-20 22:21:38.790 | MS1 | 121.4656653013 | 31.1446208958 | 267 | 504990 | -85.17 | 3.64 | 96.56 | 0.16 | 1.35 | 1583 |
| 2024-09-20 22:21:39.865 | MS1 | 121.4656624300 | 31.1446197498 | 267 | 504990 | -91.31 | 2.49 | 43.39 | 0.01 | 1.02 | 1586 |
| 2024-09-20 22:21:40.432 | MS1 | 121.4656725716 | 31.1446207834 | 267 | 504990 | -78.97 | 15.27 | 585.87 | 0.06 | 3.00 | 1574 |
| 2024-09-20 22:21:41.159 | MS1 | 121.4656586906 | 31.1446263249 | 267 | 504990 | -83.63 | 17.34 | 562.11 | 0.20 | 2.18 | 1575 |
| 2024-09-20 22:21:42.501 | MS1 | 121.4656586018 | 31.1446263442 | 267 | 504990 | -75.65 | 16.10 | 492.53 | 0.09 | 2.46 | 1590 |

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
| 3215052 | 1 | 121.4686557007 | 31.1525956431 | 248 | 11 | 6 | 35.9 | TDD | 497 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3220591 | 4 | 121.4676203500 | 31.1468804094 | 148 | 11 | 4 | 39.2 | TDD | 666 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3244242 | 2 | 121.4732323545 | 31.1469507018 | 233 | 3 | 1 | 29.6 | TDD | 914 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3246207 | 3 | 121.4729570640 | 31.1556648781 | 175 | 4 | 9 | 42.3 | TDD | 267 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |

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
| 2024-09-20 22:21:31.468 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.491 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.629 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.629 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3215052 | 1 | 11.3394 | 15.3318 | -117.3743 | 19.7931 | 143.4706 | 0.0071 | 0.0030 |
| 2024_09_20 22:00 | 3244242 | 2 | 6.2675 | 12.1454 | -117.8147 | 18.6482 | 80.3687 | 0.0003 | 0.0145 |
| 2024_09_20 22:00 | 3246207 | 3 | 6.7908 | 18.3890 | -108.7831 | 11.5989 | 137.8787 | 0.0109 | 0.0095 |
| 2024_09_20 22:00 | 3220591 | 4 | 6.2373 | 14.3492 | -115.6846 | 14.9923 | 124.8334 | 0.0122 | 0.0082 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412366_AC23BA26 | 504990 | 267 | -92.9 | 504990 | 914 | -92.8 | 504990 | 497 | -93.8 | 504990 | 666 |
| MR_1774412366_25DCF6CE | 504990 | 914 | -94.4 | 504990 | 267 | -91.0 | 504990 | 497 | -93.0 | 504990 | 666 |
| MR_1774412366_7A68A13D | 504990 | 914 | -96.5 | 504990 | 267 | -90.6 | 504990 | 497 | -94.5 | 504990 | 666 |
| MR_1774412366_126C95F3 | 504990 | 267 | -95.8 | 504990 | 914 | -91.9 | 504990 | 497 | -91.3 | 504990 | 666 |
| MR_1774412366_D52069A4 | 504990 | 267 | -93.0 | 504990 | 914 | -89.7 | 504990 | 497 | -91.7 | 504990 | 666 |
| MR_1774412366_B5220207 | 504990 | 267 | -93.7 | 504990 | 914 | -92.8 | 504990 | 497 | -92.4 | 504990 | 666 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 237: `61573815-1f6...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `61573815-1f67-43fc-853f-b652931b3154` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[237] topology](images/test_0237.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3216177_1
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3216177_1
- `C3`: Insufficient data; more data is needed for judgment.
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3237111_3
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3237111_3
- `C6`: Lift the tilt angle of 3216177_1 by 1 degrees
- `C7`: Adjust the azimuth of 3216177_1 by 35 degrees
- `C8`: Increase A3 Offset threshold for 3237111_3
- `C9`: Adjust the azimuth of 3237111_3 by 50 degrees
- `C10`: Decrease A3 Offset threshold for 3216177_1
- `C11`: Decrease transmission power for 3237111_3
- `C12`: Check test server and transmission issues
- `C13`: Press down the tilt angle of 3216177_1 by 1 degrees
- `C14`: Press down the tilt angle  of 3237111_3 by 10 degrees
- `C15`: Decrease transmission power for 3216177_1
- `C16`: Add neighbor relationship between 3217056_4 and 3237111_3
- `C17`: Add neighbor relationship between 3216177_1 and 3237111_3
- `C18`: Increase transmission power for 3216177_1
- `C19`: Lift the tilt angle  of 3237111_3 by 10 degrees
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3216177_1
- `C21`: Decrease A3 Offset threshold for 3237111_3
- `C22`: Increase transmission power for 3237111_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.562 | MS1 | 121.4656666965 | 31.1446271361 | 49 | 504990 | -88.34 | 12.07 | 386.63 | 0.10 | 2.11 | 1571 |
| 2024-09-20 22:21:32.147 | MS1 | 121.4656724912 | 31.1446219152 | 49 | 504990 | -89.90 | 13.15 | 322.23 | 0.10 | 2.28 | 1578 |
| 2024-09-20 22:21:33.182 | MS1 | 121.4656657921 | 31.1446345410 | 49 | 504990 | -89.40 | 16.62 | 602.72 | 0.06 | 2.51 | 1586 |
| 2024-09-20 22:21:34.344 | MS1 | 121.4656616952 | 31.1446259380 | 49 | 504990 | -89.20 | 17.26 | 89.70 | 0.60 | 2.94 | 547 |
| 2024-09-20 22:21:35.857 | MS1 | 121.4656741002 | 31.1446231236 | 49 | 504990 | -87.66 | 13.55 | 60.52 | 0.53 | 2.42 | 559 |
| 2024-09-20 22:21:36.325 | MS1 | 121.4656681738 | 31.1446287365 | 49 | 504990 | -85.89 | 13.99 | 44.61 | 0.70 | 2.45 | 697 |
| 2024-09-20 22:21:37.395 | MS1 | 121.4656581646 | 31.1446213169 | 49 | 504990 | -92.65 | 9.04 | 58.14 | 0.59 | 2.36 | 603 |
| 2024-09-20 22:21:38.589 | MS1 | 121.4656666734 | 31.1446238147 | 49 | 504990 | -91.82 | 10.55 | 63.78 | 0.62 | 2.73 | 531 |
| 2024-09-20 22:21:39.337 | MS1 | 121.4656658296 | 31.1446289415 | 49 | 504990 | -92.94 | 12.70 | 86.10 | 0.59 | 2.14 | 658 |
| 2024-09-20 22:21:40.636 | MS1 | 121.4656709131 | 31.1446225455 | 49 | 504990 | -93.07 | 8.71 | 432.00 | 0.10 | 2.19 | 1582 |
| 2024-09-20 22:21:41.330 | MS1 | 121.4656739214 | 31.1446247999 | 49 | 504990 | -91.72 | 10.77 | 437.07 | 0.09 | 2.65 | 1562 |
| 2024-09-20 22:21:42.976 | MS1 | 121.4656771190 | 31.1446245799 | 49 | 504990 | -91.55 | 9.25 | 299.17 | 0.10 | 2.25 | 1562 |

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
| 3211341 | 2 | 121.4647777504 | 31.1460262450 | 21 | 1 | 2 | 22.9 | TDD | 172 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3216177 | 1 | 121.4739966070 | 31.1491739450 | 202 | 0 | 7 | 24.3 | TDD | 49 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3217056 | 4 | 121.4715977876 | 31.1521276475 | 231 | 15 | 10 | 48.1 | TDD | 463 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3237111 | 3 | 121.4690348533 | 31.1529575599 | 24 | 8 | 0 | 41.6 | TDD | 553 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |

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
| 2024-09-20 22:21:31.063 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.084 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.190 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.190 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.920 | NREventA3 | measId:2;ServCellPCI:411;Se... |
| 2024-09-20 22:21:38.160 | NRHandoverAttempt | SourcePCI:411;SourceNR-ARFC... |
| 2024-09-20 22:21:38.192 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.205 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.345 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.345 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3216177 | 1 | 6.2645 | 17.6619 | -117.9177 | 11.2583 | 122.7657 | 0.0056 | 0.0041 |
| 2024_09_20 22:00 | 3211341 | 2 | 9.3257 | 18.7206 | -116.1348 | 15.6714 | 164.0095 | 0.0063 | 0.0142 |
| 2024_09_20 22:00 | 3237111 | 3 | 5.1030 | 5.6075 | -117.7284 | 13.0945 | 154.7074 | 0.0103 | 0.0097 |
| 2024_09_20 22:00 | 3217056 | 4 | 10.9351 | 15.8959 | -115.2052 | 17.5451 | 125.0712 | 0.0130 | 0.0035 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412745_74E688D2 | 504990 | 49 | -89.0 | 504990 | 553 | -95.4 | 504990 | 463 | -100.5 | 504990 | 172 |
| MR_1774412745_D4DF4258 | 504990 | 49 | -90.0 | 504990 | 553 | -93.2 | 504990 | 463 | -100.9 | 504990 | 172 |
| MR_1774412745_9E1CC8E6 | 504990 | 49 | -90.0 | 504990 | 553 | -96.1 | 504990 | 463 | -100.7 | 504990 | 172 |
| MR_1774412745_CCE58ABA | 504990 | 49 | -89.9 | 504990 | 553 | -95.7 | 504990 | 463 | -101.9 | 504990 | 172 |
| MR_1774412745_24BC0894 | 504990 | 49 | -88.7 | 504990 | 553 | -94.7 | 504990 | 463 | -100.1 | 504990 | 172 |
| MR_1774412745_F8F954BF | 504990 | 49 | -89.3 | 504990 | 553 | -95.8 | 504990 | 463 | -98.4 | 504990 | 172 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 238: `63c3f8c0-7a9...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `63c3f8c0-7a9d-4d35-afd2-6b9a9cfaaa0c` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[238] topology](images/test_0238.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3226461_9 and 3236784_3
- `C2`: Check test server and transmission issues
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3249875_1
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3236784_3
- `C5`: Decrease transmission power for 3236784_3
- `C6`: Add neighbor relationship between 3249875_1 and 3236784_3
- `C7`: Increase transmission power for 3236784_3
- `C8`: Lift the tilt angle of 3249875_1 by 3 degrees
- `C9`: Insufficient data; more data is needed for judgment.
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3236784_3
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3249875_1
- `C12`: Adjust the azimuth of 3236784_3 by 35 degrees
- `C13`: Increase A3 Offset threshold for 3249875_1
- `C14`: Decrease A3 Offset threshold for 3236784_3
- `C15`: Press down the tilt angle of 3249875_1 by 3 degrees
- `C16`: Decrease transmission power for 3249875_1
- `C17`: Press down the tilt angle  of 3236784_3 by 5 degrees
- `C18`: Adjust the azimuth of 3249875_1 by 49 degrees
- `C19`: Decrease A3 Offset threshold for 3249875_1
- `C20`: Increase A3 Offset threshold for 3236784_3
- `C21`: Increase transmission power for 3249875_1
- `C22`: Lift the tilt angle  of 3236784_3 by 5 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.228 | MS1 | 121.4656588714 | 31.1446206505 | 175 | 504990 | -94.44 | 9.55 | 309.05 | 0.17 | 2.35 | 1563 |
| 2024-09-20 22:21:32.130 | MS1 | 121.4656601527 | 31.1446251783 | 254 | 504990 | -93.20 | 13.57 | 481.84 | 0.06 | 2.63 | 1600 |
| 2024-09-20 22:21:33.684 | MS1 | 121.4656677653 | 31.1446276960 | 251 | 504990 | -94.92 | 14.85 | 525.53 | 0.16 | 2.14 | 1564 |
| 2024-09-20 22:21:34.657 | MS1 | 121.4656724541 | 31.1446257906 | 648 | 152650 | -95.53 | 5.23 | 79.81 | 0.17 | 1.65 | 916 |
| 2024-09-20 22:21:35.169 | MS1 | 121.4656709326 | 31.1446217282 | 22 | 152650 | -95.16 | 4.26 | 97.33 | 0.08 | 1.69 | 962 |
| 2024-09-20 22:21:36.204 | MS1 | 121.4656664516 | 31.1446240441 | 743 | 152650 | -96.22 | 6.14 | 87.71 | 0.20 | 1.66 | 921 |
| 2024-09-20 22:21:37.535 | MS1 | 121.4656667685 | 31.1446282779 | 290 | 152650 | -94.02 | 6.47 | 96.17 | 0.06 | 1.97 | 949 |
| 2024-09-20 22:21:38.476 | MS1 | 121.4656617722 | 31.1446290607 | 648 | 152650 | -90.17 | 2.65 | 69.61 | 0.12 | 1.89 | 910 |
| 2024-09-20 22:21:39.835 | MS1 | 121.4656644982 | 31.1446285091 | 22 | 152650 | -89.99 | 6.75 | 92.77 | 0.01 | 1.54 | 915 |
| 2024-09-20 22:21:40.517 | MS1 | 121.4656655639 | 31.1446363167 | 743 | 152650 | -87.71 | 7.82 | 50.93 | 0.05 | 2.84 | 1585 |
| 2024-09-20 22:21:41.174 | MS1 | 121.4656665976 | 31.1446308494 | 290 | 152650 | -92.89 | 6.15 | 56.99 | 0.14 | 2.66 | 1569 |
| 2024-09-20 22:21:42.851 | MS1 | 121.4656735572 | 31.1446276456 | 648 | 152650 | -95.73 | 5.96 | 83.54 | 0.02 | 2.44 | 1566 |

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
| 3215762 | 7 | 121.4724661896 | 31.1444412183 | 335 | 2 | 4 | 23.6 | FDD | 64 | n1 | 152650 | 30M | 4T4R | 10 | 152650 |
| 3226461 | 9 | 121.4704966917 | 31.1559827784 | 43 | 2 | 0 | 16.9 | FDD | 743 | n1 | 152650 | 30M | 4T4R | 10 | 152650 |
| 3230689 | 10 | 121.4697991873 | 31.1447876521 | 55 | 13 | 10 | 11.9 | FDD | 648 | n1 | 152650 | 30M | 4T4R | 14 | 152650 |
| 3232580 | 6 | 121.4743695345 | 31.1486135537 | 177 | 6 | 5 | 25.9 | TDD | 543 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3236784 | 3 | 121.4668864277 | 31.1471515061 | 238 | 1 | 9 | 22.6 | TDD | 119 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3236978 | 2 | 121.4693611618 | 31.1482366622 | 55 | 0 | 12 | 26.4 | TDD | 722 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3238181 | 12 | 121.4654996870 | 31.1486671126 | 303 | 4 | 4 | 1.2 | FDD | 753 | n1 | 152650 | 30M | 4T4R | 10 | 152650 |
| 3241596 | 11 | 121.4740521047 | 31.1542242996 | 69 | 11 | 11 | 23.2 | FDD | 777 | n1 | 152650 | 30M | 4T4R | 11 | 152650 |
| 3244990 | 13 | 121.4727218297 | 31.1532751473 | 113 | 1 | 1 | 15.9 | FDD | 22 | n1 | 152650 | 30M | 4T4R | 24 | 152650 |
| 3248800 | 8 | 121.4755466130 | 31.1517831654 | 327 | 2 | 3 | 21.3 | FDD | 290 | n1 | 152650 | 30M | 4T4R | 29 | 152650 |
| 3249875 | 1 | 121.4651448127 | 31.1476427499 | 221 | 2 | 7 | 3.9 | TDD | 175 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3250253 | 4 | 121.4673328318 | 31.1554020726 | 242 | 3 | 11 | 24.9 | TDD | 251 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3259487 | 5 | 121.4750693525 | 31.1465063831 | 108 | 5 | 9 | 28.5 | TDD | 254 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |

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
| 2024-09-20 22:21:31.403 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.426 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.569 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.569 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.218 | NREventA2 | measId:1;ServCellPCI:493;Se... |
| 2024-09-20 22:21:35.366 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.612 | NREventA5 | measId:3;ServCellPCI:493;Se... |
| 2024-09-20 22:21:35.653 | NRHandoverAttempt | SourcePCI:493;SourceNR-ARFC... |
| 2024-09-20 22:21:35.689 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.703 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:35.847 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.847 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3249875 | 1 | 5.6253 | 11.3306 | -114.8638 | 8.5302 | 188.4140 | 0.0070 | 0.0191 |
| 2024_09_20 22:00 | 3236978 | 2 | 18.0060 | 14.8369 | -117.2765 | 18.9432 | 90.5965 | 0.0041 | 0.0167 |
| 2024_09_20 22:00 | 3236784 | 3 | 12.2026 | 13.3413 | -117.9417 | 17.5442 | 143.9516 | 0.0150 | 0.0184 |
| 2024_09_20 22:00 | 3250253 | 4 | 6.7402 | 13.9224 | -115.0786 | 17.0509 | 126.4724 | 0.0131 | 0.0031 |
| 2024_09_20 22:00 | 3259487 | 5 | 18.4167 | 18.3838 | -116.0971 | 19.7794 | 145.8838 | 0.0122 | 0.0046 |
| 2024_09_20 22:00 | 3232580 | 6 | 14.5747 | 13.1794 | -116.0639 | 6.8565 | 90.4908 | 0.0083 | 0.0152 |
| 2024_09_20 22:00 | 3215762 | 7 | 19.7489 | 11.9962 | -114.1589 | 3.2387 | 48.1059 | 0.0099 | 0.0153 |
| 2024_09_20 22:00 | 3248800 | 8 | 16.2497 | 13.5409 | -114.4832 | 4.5141 | 40.0627 | 0.0129 | 0.0154 |
| 2024_09_20 22:00 | 3226461 | 9 | 17.2613 | 10.8649 | -116.0396 | 3.1842 | 21.7409 | 0.0023 | 0.0032 |
| 2024_09_20 22:00 | 3230689 | 10 | 7.0900 | 9.2422 | -115.2389 | 4.6143 | 35.8164 | 0.0157 | 0.0136 |
| 2024_09_20 22:00 | 3241596 | 11 | 14.6693 | 8.6906 | -116.1207 | 4.3664 | 33.5734 | 0.0165 | 0.0092 |
| 2024_09_20 22:00 | 3238181 | 12 | 11.4806 | 14.0472 | -115.8267 | 3.1154 | 50.7850 | 0.0093 | 0.0013 |
| 2024_09_20 22:00 | 3244990 | 13 | 6.8753 | 12.2036 | -115.4214 | 3.3912 | 57.8546 | 0.0090 | 0.0062 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416336_B69B5564 | 152650 | 648 | -97.1 | 152650 | 777 | -101.3 | 152650 | 753 | -104.7 | 152650 | 64 |
| MR_1774416336_E2309FC8 | 504990 | 251 | -96.0 | 504990 | 119 | -96.4 | 504990 | 543 | -99.6 | 504990 | 722 |
| MR_1774416336_F6F6CED5 | 504990 | 251 | -94.4 | 504990 | 119 | -96.2 | 504990 | 543 | -100.1 | 504990 | 722 |
| MR_1774416336_13D203D5 | 152650 | 648 | -93.8 | 152650 | 777 | -100.3 | 152650 | 753 | -106.9 | 152650 | 64 |
| MR_1774416336_5CD02D21 | 504990 | 251 | -95.2 | 504990 | 119 | -96.2 | 504990 | 543 | -101.1 | 504990 | 722 |
| MR_1774416336_F6F1D802 | 152650 | 648 | -95.8 | 152650 | 777 | -99.7 | 152650 | 753 | -106.6 | 152650 | 64 |
| MR_1774416336_5479EC7B | 504990 | 251 | -96.5 | 504990 | 119 | -95.5 | 504990 | 543 | -99.9 | 504990 | 722 |
| MR_1774416336_4C30848C | 504990 | 251 | -93.0 | 504990 | 119 | -94.0 | 504990 | 543 | -101.6 | 504990 | 722 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 239: `b8885d83-91d...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `b8885d83-91d3-4927-816a-88c9e850a6fc` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[239] topology](images/test_0239.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Check test server and transmission issues
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3216716_2
- `C3`: Lift the tilt angle of 3240956_1 by 2 degrees
- `C4`: Decrease A3 Offset threshold for 3240956_1
- `C5`: Press down the tilt angle of 3240956_1 by 2 degrees
- `C6`: Increase transmission power for 3240956_1
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3216716_2
- `C8`: Adjust the azimuth of 3216716_2 by 20 degrees
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3240956_1
- `C10`: Decrease A3 Offset threshold for 3216716_2
- `C11`: Add neighbor relationship between 3236324_11 and 3216716_2
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3240956_1
- `C13`: Add neighbor relationship between 3240956_1 and 3216716_2
- `C14`: Increase transmission power for 3216716_2
- `C15`: Adjust the azimuth of 3240956_1 by 4 degrees
- `C16`: Increase A3 Offset threshold for 3216716_2
- `C17`: Insufficient data; more data is needed for judgment.
- `C18`: Decrease transmission power for 3240956_1
- `C19`: Increase A3 Offset threshold for 3240956_1
- `C20`: Lift the tilt angle  of 3216716_2 by 2 degrees
- `C21`: Decrease transmission power for 3216716_2
- `C22`: Press down the tilt angle  of 3216716_2 by 2 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.605 | MS1 | 121.4656685178 | 31.1446363377 | 524 | 504990 | -95.83 | 12.58 | 505.00 | 0.01 | 2.70 | 1563 |
| 2024-09-20 22:21:32.624 | MS1 | 121.4656727953 | 31.1446210006 | 572 | 504990 | -93.85 | 14.04 | 519.81 | 0.03 | 2.30 | 1573 |
| 2024-09-20 22:21:33.556 | MS1 | 121.4656625073 | 31.1446360204 | 440 | 504990 | -94.57 | 10.54 | 454.93 | 0.04 | 2.59 | 1592 |
| 2024-09-20 22:21:34.744 | MS1 | 121.4656662589 | 31.1446375499 | 26 | 152650 | -94.42 | 6.99 | 65.22 | 0.05 | 1.82 | 970 |
| 2024-09-20 22:21:35.823 | MS1 | 121.4656704272 | 31.1446309759 | 805 | 152650 | -96.56 | 4.36 | 51.34 | 0.08 | 1.62 | 943 |
| 2024-09-20 22:21:36.711 | MS1 | 121.4656642457 | 31.1446214991 | 849 | 152650 | -88.58 | 7.52 | 49.91 | 0.14 | 1.50 | 984 |
| 2024-09-20 22:21:37.123 | MS1 | 121.4656619633 | 31.1446338049 | 377 | 152650 | -94.68 | 7.26 | 96.68 | 0.19 | 1.84 | 922 |
| 2024-09-20 22:21:38.107 | MS1 | 121.4656756207 | 31.1446262461 | 26 | 152650 | -94.24 | 4.02 | 108.61 | 0.01 | 1.68 | 932 |
| 2024-09-20 22:21:39.925 | MS1 | 121.4656585785 | 31.1446308296 | 805 | 152650 | -90.88 | 2.01 | 64.72 | 0.18 | 1.52 | 926 |
| 2024-09-20 22:21:40.732 | MS1 | 121.4656764321 | 31.1446291248 | 849 | 152650 | -87.28 | 3.87 | 89.96 | 0.16 | 2.99 | 1577 |
| 2024-09-20 22:21:41.909 | MS1 | 121.4656761513 | 31.1446344103 | 377 | 152650 | -92.31 | 6.37 | 77.38 | 0.02 | 2.24 | 1584 |
| 2024-09-20 22:21:42.880 | MS1 | 121.4656743465 | 31.1446335844 | 26 | 152650 | -94.97 | 4.87 | 82.33 | 0.15 | 2.56 | 1560 |

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
| 3216716 | 2 | 121.4753105913 | 31.1500255288 | 257 | 0 | 7 | 29.6 | TDD | 178 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3217495 | 5 | 121.4741436717 | 31.1441971236 | 254 | 5 | 3 | 13.5 | TDD | 440 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3223585 | 3 | 121.4664353136 | 31.1547972054 | 48 | 2 | 4 | 26.0 | TDD | 469 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3226362 | 4 | 121.4658968497 | 31.1496436957 | 46 | 11 | 11 | 9.4 | TDD | 149 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3230250 | 10 | 121.4640691102 | 31.1475950371 | 66 | 1 | 0 | 7.0 | FDD | 783 | n1 | 152650 | 30M | 4T4R | 10 | 152650 |
| 3236324 | 11 | 121.4712290018 | 31.1459402731 | 58 | 10 | 11 | 14.0 | FDD | 849 | n1 | 152650 | 30M | 4T4R | 30 | 152650 |
| 3240956 | 1 | 121.4669706590 | 31.1534303016 | 191 | 0 | 9 | 28.2 | TDD | 524 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3247108 | 9 | 121.4727172243 | 31.1510188532 | 322 | 12 | 11 | 24.4 | FDD | 397 | n1 | 152650 | 30M | 4T4R | 30 | 152650 |
| 3251382 | 13 | 121.4675504070 | 31.1532477402 | 85 | 4 | 2 | 16.1 | FDD | 26 | n1 | 152650 | 30M | 4T4R | 13 | 152650 |
| 3255274 | 12 | 121.4742385038 | 31.1493738637 | 268 | 8 | 10 | 11.0 | FDD | 377 | n1 | 152650 | 30M | 4T4R | 14 | 152650 |
| 3258438 | 8 | 121.4660997759 | 31.1530749396 | 194 | 15 | 4 | 25.5 | FDD | 709 | n1 | 152650 | 30M | 4T4R | 26 | 152650 |
| 3263868 | 7 | 121.4758663032 | 31.1464244864 | 290 | 9 | 5 | 24.5 | FDD | 805 | n1 | 152650 | 30M | 4T4R | 14 | 152650 |
| 3271421 | 6 | 121.4735301646 | 31.1548771685 | 126 | 1 | 2 | 15.3 | TDD | 572 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |

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
| 2024-09-20 22:21:31.417 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.440 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.566 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.566 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.239 | NREventA2 | measId:1;ServCellPCI:854;Se... |
| 2024-09-20 22:21:35.342 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.583 | NREventA5 | measId:3;ServCellPCI:854;Se... |
| 2024-09-20 22:21:35.629 | NRHandoverAttempt | SourcePCI:854;SourceNR-ARFC... |
| 2024-09-20 22:21:35.661 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.672 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:35.782 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.782 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3240956 | 1 | 18.5042 | 10.3577 | -116.8009 | 10.3640 | 184.0020 | 0.0086 | 0.0187 |
| 2024_09_20 22:00 | 3216716 | 2 | 17.2354 | 17.1829 | -115.1173 | 6.3395 | 194.8242 | 0.0146 | 0.0082 |
| 2024_09_20 22:00 | 3223585 | 3 | 12.4757 | 7.4894 | -114.9759 | 18.6404 | 152.4753 | 0.0071 | 0.0158 |
| 2024_09_20 22:00 | 3226362 | 4 | 8.6369 | 8.3939 | -114.4036 | 16.6437 | 178.7040 | 0.0163 | 0.0103 |
| 2024_09_20 22:00 | 3217495 | 5 | 5.6560 | 12.4562 | -116.9006 | 17.8743 | 157.2353 | 0.0164 | 0.0170 |
| 2024_09_20 22:00 | 3271421 | 6 | 10.9297 | 6.3931 | -114.5824 | 12.1609 | 169.6493 | 0.0030 | 0.0177 |
| 2024_09_20 22:00 | 3263868 | 7 | 11.5976 | 17.5332 | -115.8750 | 3.2715 | 27.6570 | 0.0012 | 0.0111 |
| 2024_09_20 22:00 | 3258438 | 8 | 18.1985 | 14.6223 | -115.8915 | 4.0078 | 43.7138 | 0.0161 | 0.0148 |
| 2024_09_20 22:00 | 3247108 | 9 | 19.6308 | 7.0592 | -115.1774 | 3.1284 | 24.8819 | 0.0117 | 0.0010 |
| 2024_09_20 22:00 | 3230250 | 10 | 12.6087 | 5.2456 | -115.8061 | 3.9085 | 49.1971 | 0.0139 | 0.0053 |
| 2024_09_20 22:00 | 3236324 | 11 | 9.7995 | 18.3479 | -117.3144 | 4.5398 | 47.7920 | 0.0095 | 0.0063 |
| 2024_09_20 22:00 | 3255274 | 12 | 8.2498 | 5.1314 | -117.4330 | 3.9179 | 32.1254 | 0.0168 | 0.0135 |
| 2024_09_20 22:00 | 3251382 | 13 | 18.1007 | 14.9237 | -116.6941 | 4.1364 | 28.4277 | 0.0057 | 0.0115 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416535_924CD972 | 504990 | 440 | -93.6 | 504990 | 178 | -94.4 | 504990 | 469 | -97.4 | 504990 | 149 |
| MR_1774416535_05B4AFC2 | 152650 | 26 | -95.5 | 152650 | 397 | -99.4 | 152650 | 709 | -102.6 | 152650 | 783 |
| MR_1774416535_425B3106 | 152650 | 26 | -92.7 | 152650 | 397 | -96.8 | 152650 | 709 | -101.2 | 152650 | 783 |
| MR_1774416535_E631B31E | 504990 | 440 | -92.9 | 504990 | 178 | -91.3 | 504990 | 469 | -100.5 | 504990 | 149 |
| MR_1774416535_03835BA1 | 152650 | 26 | -95.4 | 152650 | 397 | -97.0 | 152650 | 709 | -102.0 | 152650 | 783 |
| MR_1774416535_869FCCAF | 152650 | 26 | -96.4 | 152650 | 397 | -97.8 | 152650 | 709 | -102.1 | 152650 | 783 |
| MR_1774416535_D971CBA7 | 504990 | 440 | -93.1 | 504990 | 178 | -93.2 | 504990 | 469 | -100.4 | 504990 | 149 |
| MR_1774416535_CD3960A0 | 504990 | 440 | -94.3 | 504990 | 178 | -91.9 | 504990 | 469 | -99.3 | 504990 | 149 |

> *... 2개 열 생략 (전체 14열)*

---
