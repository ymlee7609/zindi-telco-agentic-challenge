# Track A 문제 분석 — train[1780]~train[1789]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[1780] ~ train[1789] (10개)

## 목차

1. [문제 1780: `b224d0d6-17b...`](#1780) — multiple-answer, 정답: C14|C18
2. [문제 1781: `2aac6e10-b35...`](#1781) — multiple-answer, 정답: C15|C18
3. [문제 1782: `71b90755-e8d...`](#1782) — multiple-answer, 정답: C6|C8|C11|C21
4. [문제 1783: `47f0751d-e0f...`](#1783) — single-answer, 정답: C4
5. [문제 1784: `150e0446-106...`](#1784) — single-answer, 정답: C18
6. [문제 1785: `8e6ac801-952...`](#1785) — single-answer, 정답: C7
7. [문제 1786: `e0713f7f-4a6...`](#1786) — single-answer, 정답: C11
8. [문제 1787: `72ddbb86-e2c...`](#1787) — single-answer, 정답: C5
9. [문제 1788: `b7e65ce2-3fd...`](#1788) — multiple-answer, 정답: C8|C15
10. [문제 1789: `491bde9e-41b...`](#1789) — single-answer, 정답: C9

---

### 문제 1780: `b224d0d6-17b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `b224d0d6-17bc-4cdf-84ce-02dd8e27c685` |
| Tag | **multiple-answer** |
| 정답 | **C14|C18** |
| C14 의미 | Press down the tilt angle  of 3248079_2 by 4 degrees |
| C18 의미 | Decrease transmission power for 3248079_2 |
| 패턴 분류 | **P3 Overshoot (tilt)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1780] topology](images/train_1780.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3248079_2
- `C2`: Insufficient data; more data is needed for judgment.
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3248079_2
- `C4`: Increase transmission power for 3238237_3
- `C5`: Lift the tilt angle of 3238237_3 by 2 degrees
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3238237_3
- `C7`: Lift the tilt angle  of 3248079_2 by 4 degrees
- `C8`: Adjust the azimuth of 3238237_3 by 21 degrees
- `C9`: Press down the tilt angle of 3238237_3 by 2 degrees
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3238237_3
- `C11`: Increase A3 Offset threshold for 3238237_3
- `C12`: Decrease A3 Offset threshold for 3248079_2
- `C13`: Decrease A3 Offset threshold for 3238237_3
- `C14`: Press down the tilt angle  of 3248079_2 by 4 degrees **← 정답**
- `C15`: Decrease transmission power for 3238237_3
- `C16`: Increase A3 Offset threshold for 3248079_2
- `C17`: Add neighbor relationship between 3238237_3 and 3248079_2
- `C18`: Decrease transmission power for 3248079_2 **← 정답**
- `C19`: Add neighbor relationship between 3245546_1 and 3248079_2
- `C20`: Adjust the azimuth of 3248079_2 by 26 degrees
- `C21`: Check test server and transmission issues
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3248079_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.862 | MS1 | 121.4656614837 | 31.1446196791 | 822 | 504990 | -81.75 | 16.47 | 424.49 | 0.07 | 2.06 | 1561 |
| 2024-09-20 22:21:32.359 | MS1 | 121.4656710072 | 31.1446266864 | 822 | 504990 | -81.25 | 17.30 | 408.24 | 0.01 | 2.73 | 1561 |
| 2024-09-20 22:21:33.479 | MS1 | 121.4656766809 | 31.1446307345 | 822 | 504990 | -80.33 | 17.88 | 580.09 | 0.19 | 2.96 | 1567 |
| 2024-09-20 22:21:34.401 | MS1 | 121.4656636875 | 31.1446273490 | 822 | 504990 | -93.63 | 2.88 | 90.65 | 0.05 | 1.05 | 1575 |
| 2024-09-20 22:21:35.328 | MS1 | 121.4656698805 | 31.1446358513 | 822 | 504990 | -89.91 | 2.66 | 71.22 | 0.05 | 1.16 | 1586 |
| 2024-09-20 22:21:36.164 | MS1 | 121.4656584694 | 31.1446229553 | 822 | 504990 | -87.23 | 3.77 | 89.60 | 0.13 | 1.33 | 1579 |
| 2024-09-20 22:21:37.930 | MS1 | 121.4656754265 | 31.1446235905 | 822 | 504990 | -90.62 | 0.93 | 59.98 | 0.01 | 1.24 | 1561 |
| 2024-09-20 22:21:38.366 | MS1 | 121.4656676007 | 31.1446375548 | 822 | 504990 | -89.95 | 2.90 | 45.92 | 0.09 | 1.27 | 1564 |
| 2024-09-20 22:21:39.106 | MS1 | 121.4656740436 | 31.1446339794 | 822 | 504990 | -92.85 | 0.50 | 40.42 | 0.13 | 1.48 | 1560 |
| 2024-09-20 22:21:40.248 | MS1 | 121.4656648950 | 31.1446331298 | 822 | 504990 | -79.10 | 16.40 | 470.22 | 0.17 | 2.30 | 1570 |
| 2024-09-20 22:21:41.316 | MS1 | 121.4656675084 | 31.1446259539 | 822 | 504990 | -80.09 | 15.00 | 330.71 | 0.06 | 2.74 | 1571 |
| 2024-09-20 22:21:42.627 | MS1 | 121.4656675567 | 31.1446207612 | 822 | 504990 | -79.30 | 13.88 | 304.38 | 0.05 | 2.14 | 1587 |

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
| 3238237 | 3 | 121.4674753753 | 31.1542667461 | 168 | 0 | 7 | 35.6 | TDD | 822 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3245546 | 1 | 121.4727827923 | 31.1458278738 | 114 | 0 | 2 | 23.4 | TDD | 58 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3248079 | 2 | 121.4660347084 | 31.1550178156 | 156 | 3 | 12 | 26.0 | TDD | 459 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3271632 | 4 | 121.4732740457 | 31.1458198507 | 121 | 14 | 1 | 33.2 | TDD | 103 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:31.475 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.500 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.635 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.635 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3245546 | 1 | 13.5354 | 10.9639 | -114.3175 | 9.0205 | 143.3540 | 0.0094 | 0.0147 |
| 2024_09_20 22:00 | 3248079 | 2 | 11.6232 | 18.6469 | -117.1616 | 11.2687 | 88.4713 | 0.0166 | 0.0192 |
| 2024_09_20 22:00 | 3238237 | 3 | 16.7627 | 15.6860 | -108.9267 | 9.3231 | 100.2692 | 0.0114 | 0.0167 |
| 2024_09_20 22:00 | 3271632 | 4 | 13.1812 | 8.5557 | -117.0463 | 15.8115 | 133.6898 | 0.0131 | 0.0131 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415599_22D6F3E1 | 504990 | 459 | -91.8 | 504990 | 822 | -93.3 | 504990 | 58 | -97.1 | 504990 | 103 |
| MR_1774415599_148B87D2 | 504990 | 822 | -95.3 | 504990 | 459 | -94.5 | 504990 | 58 | -94.9 | 504990 | 103 |
| MR_1774415599_69C06251 | 504990 | 822 | -92.5 | 504990 | 459 | -93.4 | 504990 | 58 | -97.9 | 504990 | 103 |
| MR_1774415599_772007F1 | 504990 | 822 | -92.3 | 504990 | 459 | -95.1 | 504990 | 58 | -95.5 | 504990 | 103 |
| MR_1774415599_F3D91F0D | 504990 | 822 | -91.7 | 504990 | 459 | -96.4 | 504990 | 58 | -98.0 | 504990 | 103 |
| MR_1774415599_ED47A99A | 504990 | 459 | -94.8 | 504990 | 822 | -96.2 | 504990 | 58 | -94.8 | 504990 | 103 |
| MR_1774415599_C877FB1D | 504990 | 822 | -91.8 | 504990 | 459 | -93.4 | 504990 | 58 | -96.7 | 504990 | 103 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1781: `2aac6e10-b35...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `2aac6e10-b35e-4f28-ba79-50febb274bba` |
| Tag | **multiple-answer** |
| 정답 | **C15|C18** |
| C15 의미 | Decrease transmission power for 3279961_2 |
| C18 의미 | Press down the tilt angle  of 3279961_2 by 5 degrees |
| 패턴 분류 | **P3 Overshoot (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1781] topology](images/train_1781.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3214711_3 by 3 degrees
- `C2`: Decrease A3 Offset threshold for 3214711_3
- `C3`: Decrease transmission power for 3214711_3
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3214711_3
- `C5`: Insufficient data; more data is needed for judgment.
- `C6`: Adjust the azimuth of 3279961_2 by 4 degrees
- `C7`: Increase A3 Offset threshold for 3214711_3
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3279961_2
- `C9`: Decrease A3 Offset threshold for 3279961_2
- `C10`: Press down the tilt angle of 3214711_3 by 3 degrees
- `C11`: Add neighbor relationship between 3214711_3 and 3279961_2
- `C12`: Increase transmission power for 3214711_3
- `C13`: Increase A3 Offset threshold for 3279961_2
- `C14`: Check test server and transmission issues
- `C15`: Decrease transmission power for 3279961_2 **← 정답**
- `C16`: Adjust the azimuth of 3214711_3 by 39 degrees
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3279961_2
- `C18`: Press down the tilt angle  of 3279961_2 by 5 degrees **← 정답**
- `C19`: Lift the tilt angle  of 3279961_2 by 5 degrees
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3214711_3
- `C21`: Increase transmission power for 3279961_2
- `C22`: Add neighbor relationship between 3267011_1 and 3279961_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.803 | MS1 | 121.4656747251 | 31.1446277437 | 518 | 504990 | -83.12 | 15.60 | 476.68 | 0.07 | 2.58 | 1565 |
| 2024-09-20 22:21:32.873 | MS1 | 121.4656711315 | 31.1446277900 | 518 | 504990 | -80.94 | 13.86 | 383.80 | 0.08 | 2.64 | 1563 |
| 2024-09-20 22:21:33.356 | MS1 | 121.4656610741 | 31.1446223651 | 518 | 504990 | -80.83 | 14.64 | 516.14 | 0.09 | 2.40 | 1574 |
| 2024-09-20 22:21:34.805 | MS1 | 121.4656763783 | 31.1446353045 | 518 | 504990 | -87.72 | 3.71 | 53.07 | 0.04 | 1.41 | 1596 |
| 2024-09-20 22:21:35.185 | MS1 | 121.4656707123 | 31.1446337682 | 518 | 504990 | -87.91 | 2.90 | 95.92 | 0.10 | 1.49 | 1591 |
| 2024-09-20 22:21:36.144 | MS1 | 121.4656693479 | 31.1446329548 | 518 | 504990 | -94.95 | 0.47 | 66.70 | 0.02 | 1.24 | 1580 |
| 2024-09-20 22:21:37.284 | MS1 | 121.4656655812 | 31.1446232049 | 518 | 504990 | -86.41 | 3.72 | 64.10 | 0.10 | 1.12 | 1572 |
| 2024-09-20 22:21:38.182 | MS1 | 121.4656726840 | 31.1446318615 | 518 | 504990 | -88.86 | 0.26 | 41.15 | 0.04 | 1.16 | 1565 |
| 2024-09-20 22:21:39.796 | MS1 | 121.4656705962 | 31.1446254889 | 518 | 504990 | -87.49 | 1.72 | 70.26 | 0.18 | 1.32 | 1586 |
| 2024-09-20 22:21:40.128 | MS1 | 121.4656599381 | 31.1446323094 | 518 | 504990 | -77.18 | 16.08 | 595.22 | 0.16 | 2.27 | 1563 |
| 2024-09-20 22:21:41.950 | MS1 | 121.4656587604 | 31.1446205458 | 518 | 504990 | -81.73 | 15.31 | 315.05 | 0.06 | 2.38 | 1579 |
| 2024-09-20 22:21:42.468 | MS1 | 121.4656613844 | 31.1446332482 | 518 | 504990 | -83.03 | 14.37 | 435.47 | 0.05 | 2.90 | 1574 |

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
| 3214711 | 3 | 121.4757717680 | 31.1494152911 | 280 | 2 | 5 | 28.2 | TDD | 518 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3245509 | 4 | 121.4755907391 | 31.1549320109 | 138 | 3 | 8 | 21.9 | TDD | 486 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3267011 | 1 | 121.4649165663 | 31.1495853772 | 27 | 15 | 6 | 41.3 | TDD | 962 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3279961 | 2 | 121.4662875802 | 31.1542679692 | 179 | 4 | 5 | 15.3 | TDD | 901 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:30.828 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:30.933 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.933 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3267011 | 1 | 16.6561 | 19.6788 | -116.7413 | 7.4945 | 153.9922 | 0.0065 | 0.0003 |
| 2024_09_20 22:00 | 3279961 | 2 | 7.0151 | 16.9179 | -116.0917 | 8.9585 | 117.6160 | 0.0190 | 0.0189 |
| 2024_09_20 22:00 | 3214711 | 3 | 10.4091 | 19.1654 | -108.8754 | 8.9825 | 197.9888 | 0.0097 | 0.0115 |
| 2024_09_20 22:00 | 3245509 | 4 | 5.5991 | 18.9765 | -116.8108 | 9.8405 | 196.4062 | 0.0066 | 0.0124 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416479_FC367A0B | 504990 | 518 | -87.1 | 504990 | 901 | -84.8 | 504990 | 962 | -86.1 | 504990 | 486 |
| MR_1774416479_C2ABB042 | 504990 | 901 | -85.9 | 504990 | 518 | -86.3 | 504990 | 962 | -87.1 | 504990 | 486 |
| MR_1774416479_A4644646 | 504990 | 518 | -85.9 | 504990 | 901 | -85.2 | 504990 | 962 | -86.6 | 504990 | 486 |
| MR_1774416479_2CB10079 | 504990 | 901 | -86.1 | 504990 | 518 | -87.4 | 504990 | 962 | -85.5 | 504990 | 486 |
| MR_1774416479_489CB73E | 504990 | 901 | -89.2 | 504990 | 518 | -85.4 | 504990 | 962 | -85.5 | 504990 | 486 |
| MR_1774416479_371EAA55 | 504990 | 518 | -85.9 | 504990 | 901 | -87.9 | 504990 | 962 | -88.9 | 504990 | 486 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1782: `71b90755-e8d...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `71b90755-e8d8-45fd-8af4-d0f0d8b6d3d0` |
| Tag | **multiple-answer** |
| 정답 | **C6|C8|C11|C21** |
| C6 의미 | Increase A3 Offset threshold for 3255160_4 |
| C8 의미 | Press down the tilt angle  of 3266329_5 by 6 degrees |
| C11 의미 | Decrease transmission power for 3266329_5 |
| C21 의미 | Increase A3 Offset threshold for 3266329_5 |
| 패턴 분류 | **P2 Ping-pong** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1782] topology](images/train_1782.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 5 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 5개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Check test server and transmission issues
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3255160_4
- `C3`: Lift the tilt angle  of 3266329_5 by 6 degrees
- `C4`: Add neighbor relationship between 3250879_2 and 3266329_5
- `C5`: Increase transmission power for 3266329_5
- `C6`: Increase A3 Offset threshold for 3255160_4 **← 정답**
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3266329_5
- `C8`: Press down the tilt angle  of 3266329_5 by 6 degrees **← 정답**
- `C9`: Lift the tilt angle of 3255160_4 by 3 degrees
- `C10`: Insufficient data; more data is needed for judgment.
- `C11`: Decrease transmission power for 3266329_5 **← 정답**
- `C12`: Adjust the azimuth of 3266329_5 by 9 degrees
- `C13`: Adjust the azimuth of 3255160_4 by 50 degrees
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3255160_4
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3266329_5
- `C16`: Add neighbor relationship between 3255160_4 and 3266329_5
- `C17`: Press down the tilt angle of 3255160_4 by 3 degrees
- `C18`: Decrease A3 Offset threshold for 3255160_4
- `C19`: Decrease A3 Offset threshold for 3266329_5
- `C20`: Increase transmission power for 3255160_4
- `C21`: Increase A3 Offset threshold for 3266329_5 **← 정답**
- `C22`: Decrease transmission power for 3255160_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.704 | MS1 | 121.4656705858 | 31.1446300088 | 502 | 504990 | -79.61 | 17.92 | 468.29 | 0.05 | 2.10 | 1569 |
| 2024-09-20 22:21:32.627 | MS1 | 121.4656727357 | 31.1446359184 | 502 | 504990 | -78.14 | 14.24 | 360.55 | 0.16 | 2.10 | 1593 |
| 2024-09-20 22:21:33.609 | MS1 | 121.4656590552 | 31.1446345790 | 502 | 504990 | -82.41 | 16.07 | 495.22 | 0.04 | 2.15 | 1562 |
| 2024-09-20 22:21:34.674 | MS1 | 121.4656667309 | 31.1446297740 | 844 | 504990 | -80.40 | 3.73 | 53.83 | 0.15 | 1.06 | 1588 |
| 2024-09-20 22:21:35.842 | MS1 | 121.4656662852 | 31.1446249142 | 844 | 504990 | -87.76 | 1.01 | 27.73 | 0.09 | 1.10 | 1561 |
| 2024-09-20 22:21:36.886 | MS1 | 121.4656764999 | 31.1446365178 | 502 | 504990 | -85.50 | 4.94 | 51.95 | 0.03 | 1.36 | 1599 |
| 2024-09-20 22:21:37.531 | MS1 | 121.4656663485 | 31.1446286162 | 502 | 504990 | -80.62 | 4.95 | 39.85 | 0.03 | 1.40 | 1581 |
| 2024-09-20 22:21:38.111 | MS1 | 121.4656703607 | 31.1446234959 | 844 | 504990 | -86.05 | 1.27 | 59.44 | 0.19 | 1.27 | 1587 |
| 2024-09-20 22:21:39.690 | MS1 | 121.4656761189 | 31.1446221419 | 844 | 504990 | -88.65 | 2.26 | 31.28 | 0.15 | 1.44 | 1596 |
| 2024-09-20 22:21:40.125 | MS1 | 121.4656598057 | 31.1446209384 | 844 | 504990 | -77.81 | 16.75 | 521.40 | 0.07 | 2.97 | 1565 |
| 2024-09-20 22:21:41.243 | MS1 | 121.4656669636 | 31.1446225493 | 844 | 504990 | -84.27 | 13.23 | 512.18 | 0.15 | 2.36 | 1588 |
| 2024-09-20 22:21:42.203 | MS1 | 121.4656589186 | 31.1446212824 | 844 | 504990 | -76.70 | 17.31 | 512.28 | 0.18 | 2.86 | 1598 |

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
| 3236720 | 1 | 121.4671801077 | 31.1543456807 | 245 | 7 | 0 | 21.5 | TDD | 844 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3250879 | 2 | 121.4757209998 | 31.1458386243 | 38 | 6 | 1 | 45.8 | TDD | 236 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3255066 | 3 | 121.4732476635 | 31.1558444727 | 274 | 11 | 12 | 17.5 | TDD | 306 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3255160 | 4 | 121.4742160446 | 31.1461367153 | 308 | 1 | 11 | 29.0 | TDD | 502 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3266329 | 5 | 121.4715596892 | 31.1464951048 | 259 | 2 | 11 | 39.1 | TDD | 635 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |

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
| 2024-09-20 22:21:30.952 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.973 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.081 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.081 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:33.841 | NREventA3 | measId:2;ServCellPCI:258;Se... |
| 2024-09-20 22:21:34.081 | NRHandoverAttempt | SourcePCI:258;SourceNR-ARFC... |
| 2024-09-20 22:21:34.126 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:34.137 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:34.243 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:34.243 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.841 | NREventA3 | measId:2;ServCellPCI:301;Se... |
| 2024-09-20 22:21:36.081 | NRHandoverAttempt | SourcePCI:301;SourceNR-ARFC... |
| 2024-09-20 22:21:36.116 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:36.127 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:36.243 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.243 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.841 | NREventA3 | measId:2;ServCellPCI:258;Se... |
| 2024-09-20 22:21:38.081 | NRHandoverAttempt | SourcePCI:258;SourceNR-ARFC... |
| 2024-09-20 22:21:38.131 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.141 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.258 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.258 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3236720 | 1 | 5.0698 | 7.0760 | -116.2625 | 9.0814 | 198.4341 | 0.0153 | 0.0181 |
| 2024_09_20 22:00 | 3250879 | 2 | 6.0133 | 18.9817 | -116.6732 | 6.5868 | 85.4845 | 0.0152 | 0.0178 |
| 2024_09_20 22:00 | 3255066 | 3 | 8.1772 | 5.6688 | -117.6779 | 9.1698 | 132.5179 | 0.0152 | 0.0147 |
| 2024_09_20 22:00 | 3255160 | 4 | 15.0606 | 8.8038 | -116.6002 | 11.2570 | 110.0521 | 0.0002 | 0.0031 |
| 2024_09_20 22:00 | 3266329 | 5 | 6.0739 | 5.3288 | -116.1404 | 16.1284 | 145.1327 | 0.0066 | 0.0012 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413178_77AE7685 | 504990 | 502 | -82.1 | 504990 | 844 | -77.9 | 504990 | 635 | -85.9 | 504990 | 236 |
| MR_1774413178_F0040585 | 504990 | 844 | -82.0 | 504990 | 502 | -76.9 | 504990 | 635 | -87.4 | 504990 | 236 |
| MR_1774413178_2BF9223A | 504990 | 844 | -80.7 | 504990 | 502 | -80.4 | 504990 | 635 | -87.2 | 504990 | 236 |
| MR_1774413178_AB326721 | 504990 | 844 | -80.2 | 504990 | 502 | -80.0 | 504990 | 635 | -87.6 | 504990 | 236 |
| MR_1774413178_DFAE35AD | 504990 | 502 | -80.9 | 504990 | 844 | -78.0 | 504990 | 635 | -84.5 | 504990 | 236 |
| MR_1774413178_CB725618 | 504990 | 844 | -81.6 | 504990 | 502 | -79.5 | 504990 | 635 | -86.7 | 504990 | 236 |
| MR_1774413178_110D6D8D | 504990 | 502 | -79.5 | 504990 | 844 | -77.6 | 504990 | 635 | -88.0 | 504990 | 236 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1783: `47f0751d-e0f...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `47f0751d-e0fd-459a-9ddc-3ff596cff165` |
| Tag | **single-answer** |
| 정답 | **C4** |
| C4 의미 | Add neighbor relationship between 3223214_4 and 3276261_3 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1783] topology](images/train_1783.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle  of 3276261_3 by 5 degrees
- `C2`: Decrease transmission power for 3276261_3
- `C3`: Increase transmission power for 3223214_4
- `C4`: Add neighbor relationship between 3223214_4 and 3276261_3 **← 정답**
- `C5`: Increase A3 Offset threshold for 3276261_3
- `C6`: Decrease A3 Offset threshold for 3223214_4
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3276261_3
- `C8`: Decrease A3 Offset threshold for 3276261_3
- `C9`: Increase A3 Offset threshold for 3223214_4
- `C10`: Add neighbor relationship between 3228594_1 and 3276261_3
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3223214_4
- `C12`: Adjust the azimuth of 3223214_4 by 10 degrees
- `C13`: Increase transmission power for 3276261_3
- `C14`: Adjust the azimuth of 3276261_3 by 26 degrees
- `C15`: Decrease transmission power for 3223214_4
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3276261_3
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3223214_4
- `C18`: Press down the tilt angle  of 3276261_3 by 5 degrees
- `C19`: Press down the tilt angle of 3223214_4 by 9 degrees
- `C20`: Check test server and transmission issues
- `C21`: Insufficient data; more data is needed for judgment.
- `C22`: Lift the tilt angle of 3223214_4 by 9 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.572 | MS1 | 121.4656597336 | 31.1446196853 | 495 | 504990 | -80.93 | 12.37 | 598.04 | 0.01 | 2.20 | 1579 |
| 2024-09-20 22:21:32.473 | MS1 | 121.4656764622 | 31.1446220186 | 495 | 504990 | -76.66 | 16.92 | 507.82 | 0.15 | 2.99 | 1594 |
| 2024-09-20 22:21:33.657 | MS1 | 121.4656770593 | 31.1446237514 | 495 | 504990 | -83.09 | 13.35 | 601.49 | 0.15 | 2.20 | 1576 |
| 2024-09-20 22:21:34.210 | MS1 | 121.4656731826 | 31.1446302326 | 495 | 504990 | -90.46 | -1.79 | 51.43 | 0.15 | 1.33 | 1561 |
| 2024-09-20 22:21:35.114 | MS1 | 121.4656647777 | 31.1446269149 | 495 | 504990 | -87.97 | -3.91 | 48.65 | 0.06 | 1.22 | 1573 |
| 2024-09-20 22:21:36.693 | MS1 | 121.4656694499 | 31.1446358649 | 495 | 504990 | -85.89 | -0.25 | 77.06 | 0.08 | 1.24 | 1571 |
| 2024-09-20 22:21:37.594 | MS1 | 121.4656741718 | 31.1446336208 | 495 | 504990 | -91.36 | -2.23 | 38.65 | 0.05 | 1.25 | 1592 |
| 2024-09-20 22:21:38.694 | MS1 | 121.4656680166 | 31.1446264684 | 495 | 504990 | -78.85 | 13.65 | 325.47 | 0.16 | 1.20 | 1594 |
| 2024-09-20 22:21:39.255 | MS1 | 121.4656691762 | 31.1446296310 | 495 | 504990 | -78.27 | 13.50 | 587.07 | 0.09 | 1.43 | 1570 |
| 2024-09-20 22:21:40.748 | MS1 | 121.4656776822 | 31.1446207909 | 495 | 504990 | -83.55 | 13.60 | 563.00 | 0.09 | 2.86 | 1579 |
| 2024-09-20 22:21:41.276 | MS1 | 121.4656682646 | 31.1446308118 | 495 | 504990 | -79.34 | 12.89 | 479.73 | 0.11 | 2.69 | 1560 |
| 2024-09-20 22:21:42.515 | MS1 | 121.4656640335 | 31.1446210396 | 495 | 504990 | -80.20 | 13.85 | 528.00 | 0.13 | 2.51 | 1594 |

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
| 3223214 | 4 | 121.4730179757 | 31.1531991396 | 226 | 8 | 1 | 30.8 | TDD | 495 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3228594 | 1 | 121.4703582374 | 31.1445279916 | 100 | 5 | 7 | 29.6 | TDD | 834 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3258073 | 2 | 121.4653961130 | 31.1500469591 | 214 | 6 | 6 | 43.5 | TDD | 347 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3276261 | 3 | 121.4758779106 | 31.1496235956 | 266 | 4 | 12 | 24.5 | TDD | 244 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |

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
| 2024-09-20 22:21:30.950 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.975 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.120 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.120 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.773 | NREventA3 | measId:2;ServCellPCI:743;Se... |
| 2024-09-20 22:21:35.773 | NREventA3 | measId:2;ServCellPCI:743;Se... |
| 2024-09-20 22:21:36.773 | NREventA3 | measId:2;ServCellPCI:743;Se... |
| 2024-09-20 22:21:39.273 | NRRRCReestablishAttempt | PCI:743 |
| 2024-09-20 22:21:39.293 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.305 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:39.455 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.455 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3228594 | 1 | 9.4016 | 8.3313 | -116.2505 | 17.5515 | 106.6310 | 0.0029 | 0.0187 |
| 2024_09_20 22:00 | 3258073 | 2 | 8.8842 | 11.0749 | -116.1122 | 13.0893 | 114.8525 | 0.0109 | 0.0117 |
| 2024_09_20 22:00 | 3276261 | 3 | 8.6409 | 6.5459 | -116.5704 | 18.3457 | 140.8258 | 0.0139 | 0.0195 |
| 2024_09_20 22:00 | 3223214 | 4 | 13.7980 | 10.8834 | -114.8637 | 13.3165 | 162.2137 | 0.0010 | 0.1033 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413831_1ACAFA3C | 504990 | 495 | -88.7 | 504990 | 244 | -83.8 | 504990 | 834 | -91.9 | 504990 | 347 |
| MR_1774413831_1D38BB2D | 504990 | 495 | -88.5 | 504990 | 244 | -84.8 | 504990 | 834 | -91.7 | 504990 | 347 |
| MR_1774413831_A71AFBEE | 504990 | 495 | -92.0 | 504990 | 244 | -86.5 | 504990 | 834 | -95.1 | 504990 | 347 |
| MR_1774413831_C4E06A91 | 504990 | 495 | -92.3 | 504990 | 244 | -83.1 | 504990 | 834 | -94.2 | 504990 | 347 |
| MR_1774413831_E4284B08 | 504990 | 495 | -91.9 | 504990 | 244 | -86.8 | 504990 | 834 | -94.2 | 504990 | 347 |
| MR_1774413831_1BAB9843 | 504990 | 244 | -85.9 | 504990 | 495 | -91.3 | 504990 | 834 | -91.4 | 504990 | 347 |
| MR_1774413831_BC9B35F5 | 504990 | 495 | -91.2 | 504990 | 244 | -83.1 | 504990 | 834 | -92.9 | 504990 | 347 |
| MR_1774413831_6027D6E1 | 504990 | 495 | -89.7 | 504990 | 244 | -86.9 | 504990 | 834 | -93.4 | 504990 | 347 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1784: `150e0446-106...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `150e0446-1064-4b83-9020-a6c2e94e8b7b` |
| Tag | **single-answer** |
| 정답 | **C18** |
| C18 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3221086_3 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1784] topology](images/train_1784.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment.
- `C2`: Increase transmission power for 3221086_3
- `C3`: Add neighbor relationship between 3257303_2 and 3256366_1
- `C4`: Lift the tilt angle  of 3256366_1 by 8 degrees
- `C5`: Decrease A3 Offset threshold for 3221086_3
- `C6`: Increase A3 Offset threshold for 3221086_3
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3256366_1
- `C8`: Add neighbor relationship between 3221086_3 and 3256366_1
- `C9`: Adjust the azimuth of 3221086_3 by 33 degrees
- `C10`: Lift the tilt angle of 3221086_3 by 5 degrees
- `C11`: Decrease A3 Offset threshold for 3256366_1
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3221086_3
- `C13`: Decrease transmission power for 3256366_1
- `C14`: Adjust the azimuth of 3256366_1 by 25 degrees
- `C15`: Press down the tilt angle of 3221086_3 by 5 degrees
- `C16`: Decrease transmission power for 3221086_3
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3256366_1
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3221086_3 **← 정답**
- `C19`: Increase A3 Offset threshold for 3256366_1
- `C20`: Check test server and transmission issues
- `C21`: Increase transmission power for 3256366_1
- `C22`: Press down the tilt angle  of 3256366_1 by 8 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.699 | MS1 | 121.4656683513 | 31.1446210288 | 996 | 504990 | -87.97 | 15.43 | 541.17 | 0.18 | 2.37 | 1572 |
| 2024-09-20 22:21:32.744 | MS1 | 121.4656597737 | 31.1446328865 | 996 | 504990 | -85.80 | 14.21 | 413.24 | 0.04 | 2.36 | 1574 |
| 2024-09-20 22:21:33.729 | MS1 | 121.4656664801 | 31.1446257759 | 996 | 504990 | -89.51 | 12.37 | 409.01 | 0.19 | 2.32 | 1566 |
| 2024-09-20 22:21:34.593 | MS1 | 121.4656661480 | 31.1446327142 | 996 | 504990 | -91.55 | 12.41 | 83.50 | 0.57 | 2.01 | 694 |
| 2024-09-20 22:21:35.788 | MS1 | 121.4656755777 | 31.1446272261 | 996 | 504990 | -91.27 | 12.64 | 68.00 | 0.58 | 2.69 | 616 |
| 2024-09-20 22:21:36.661 | MS1 | 121.4656711796 | 31.1446281230 | 996 | 504990 | -86.17 | 14.07 | 94.46 | 0.63 | 2.03 | 642 |
| 2024-09-20 22:21:37.743 | MS1 | 121.4656604190 | 31.1446321435 | 996 | 504990 | -89.74 | 9.26 | 77.74 | 0.66 | 2.05 | 628 |
| 2024-09-20 22:21:38.599 | MS1 | 121.4656584808 | 31.1446321629 | 996 | 504990 | -92.43 | 7.61 | 47.41 | 0.54 | 2.80 | 523 |
| 2024-09-20 22:21:39.853 | MS1 | 121.4656725765 | 31.1446319545 | 996 | 504990 | -93.93 | 10.40 | 73.37 | 0.63 | 2.56 | 664 |
| 2024-09-20 22:21:40.271 | MS1 | 121.4656665982 | 31.1446320285 | 996 | 504990 | -89.90 | 7.71 | 508.93 | 0.04 | 2.85 | 1561 |
| 2024-09-20 22:21:41.824 | MS1 | 121.4656581454 | 31.1446248397 | 996 | 504990 | -89.64 | 12.24 | 511.49 | 0.11 | 2.55 | 1563 |
| 2024-09-20 22:21:42.411 | MS1 | 121.4656674468 | 31.1446374799 | 996 | 504990 | -90.19 | 8.92 | 476.31 | 0.16 | 2.11 | 1584 |

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
| 3221086 | 3 | 121.4753250640 | 31.1510234761 | 265 | 3 | 6 | 41.8 | TDD | 996 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3240868 | 4 | 121.4697029827 | 31.1503284670 | 251 | 11 | 1 | 47.0 | TDD | 774 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3256366 | 1 | 121.4644146945 | 31.1517125026 | 196 | 5 | 1 | 45.2 | TDD | 664 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3257303 | 2 | 121.4677569465 | 31.1518299695 | 281 | 0 | 0 | 31.6 | TDD | 458 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:31.430 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.445 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.545 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.545 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.266 | NREventA3 | measId:2;ServCellPCI:186;Se... |
| 2024-09-20 22:21:38.506 | NRHandoverAttempt | SourcePCI:186;SourceNR-ARFC... |
| 2024-09-20 22:21:38.556 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.571 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.678 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.678 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3256366 | 1 | 12.0671 | 5.9360 | -115.9341 | 9.4723 | 175.3588 | 0.0002 | 0.0036 |
| 2024_09_20 22:00 | 3257303 | 2 | 17.4881 | 6.5714 | -114.5488 | 8.8543 | 123.2619 | 0.0065 | 0.0102 |
| 2024_09_20 22:00 | 3221086 | 3 | 11.3238 | 19.3196 | -116.7776 | 9.6103 | 126.6227 | 0.0063 | 0.0128 |
| 2024_09_20 22:00 | 3240868 | 4 | 13.6003 | 15.1977 | -114.1571 | 16.4373 | 159.8256 | 0.0038 | 0.0178 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415037_2E17B0C7 | 504990 | 996 | -91.8 | 504990 | 664 | -100.9 | 504990 | 458 | -102.4 | 504990 | 774 |
| MR_1774415037_BA09CB68 | 504990 | 996 | -90.2 | 504990 | 664 | -99.4 | 504990 | 458 | -104.0 | 504990 | 774 |
| MR_1774415037_1F2C0AE0 | 504990 | 996 | -89.8 | 504990 | 664 | -99.1 | 504990 | 458 | -104.2 | 504990 | 774 |
| MR_1774415037_732DC245 | 504990 | 996 | -91.9 | 504990 | 664 | -101.1 | 504990 | 458 | -103.2 | 504990 | 774 |
| MR_1774415037_4A208FE8 | 504990 | 996 | -90.8 | 504990 | 664 | -97.3 | 504990 | 458 | -102.9 | 504990 | 774 |
| MR_1774415037_8A92E422 | 504990 | 996 | -89.8 | 504990 | 664 | -98.1 | 504990 | 458 | -104.8 | 504990 | 774 |
| MR_1774415037_BEB41FAC | 504990 | 996 | -92.4 | 504990 | 664 | -99.9 | 504990 | 458 | -104.4 | 504990 | 774 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1785: `8e6ac801-952...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `8e6ac801-952f-4a24-a83c-e7695380b28c` |
| Tag | **single-answer** |
| 정답 | **C7** |
| C7 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3265817_2 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1785] topology](images/train_1785.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle  of 3230745_3 by 7 degrees
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3230745_3
- `C3`: Adjust the azimuth of 3230745_3 by 50 degrees
- `C4`: Press down the tilt angle of 3265817_2 by 4 degrees
- `C5`: Decrease A3 Offset threshold for 3265817_2
- `C6`: Adjust the azimuth of 3265817_2 by 13 degrees
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3265817_2 **← 정답**
- `C8`: Check test server and transmission issues
- `C9`: Increase transmission power for 3230745_3
- `C10`: Increase A3 Offset threshold for 3265817_2
- `C11`: Decrease transmission power for 3230745_3
- `C12`: Insufficient data; more data is needed for judgment.
- `C13`: Lift the tilt angle of 3265817_2 by 4 degrees
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3265817_2
- `C15`: Add neighbor relationship between 3234023_1 and 3230745_3
- `C16`: Decrease A3 Offset threshold for 3230745_3
- `C17`: Decrease transmission power for 3265817_2
- `C18`: Increase transmission power for 3265817_2
- `C19`: Increase A3 Offset threshold for 3230745_3
- `C20`: Add neighbor relationship between 3265817_2 and 3230745_3
- `C21`: Press down the tilt angle  of 3230745_3 by 7 degrees
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3230745_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.398 | MS1 | 121.4656609544 | 31.1446244133 | 634 | 504990 | -89.22 | 13.66 | 520.78 | 0.11 | 2.89 | 1590 |
| 2024-09-20 22:21:32.978 | MS1 | 121.4656697468 | 31.1446262500 | 634 | 504990 | -85.54 | 16.25 | 570.53 | 0.20 | 2.06 | 1575 |
| 2024-09-20 22:21:33.313 | MS1 | 121.4656751661 | 31.1446260211 | 634 | 504990 | -90.28 | 13.22 | 408.88 | 0.13 | 2.30 | 1577 |
| 2024-09-20 22:21:34.277 | MS1 | 121.4656583818 | 31.1446191125 | 634 | 504990 | -91.70 | 12.80 | 58.12 | 0.67 | 2.20 | 673 |
| 2024-09-20 22:21:35.858 | MS1 | 121.4656605390 | 31.1446317692 | 634 | 504990 | -88.11 | 16.76 | 84.61 | 0.51 | 2.77 | 599 |
| 2024-09-20 22:21:36.141 | MS1 | 121.4656599914 | 31.1446370247 | 634 | 504990 | -87.99 | 16.93 | 55.11 | 0.52 | 2.07 | 554 |
| 2024-09-20 22:21:37.767 | MS1 | 121.4656617959 | 31.1446258495 | 634 | 504990 | -90.41 | 11.59 | 45.36 | 0.69 | 2.18 | 659 |
| 2024-09-20 22:21:38.721 | MS1 | 121.4656756613 | 31.1446340001 | 634 | 504990 | -93.89 | 8.18 | 83.28 | 0.56 | 2.17 | 589 |
| 2024-09-20 22:21:39.545 | MS1 | 121.4656768512 | 31.1446231621 | 634 | 504990 | -90.04 | 12.45 | 93.40 | 0.55 | 2.67 | 517 |
| 2024-09-20 22:21:40.488 | MS1 | 121.4656642229 | 31.1446364695 | 634 | 504990 | -90.97 | 12.56 | 596.31 | 0.10 | 2.35 | 1571 |
| 2024-09-20 22:21:41.286 | MS1 | 121.4656581217 | 31.1446323717 | 634 | 504990 | -94.00 | 11.49 | 335.37 | 0.17 | 2.11 | 1561 |
| 2024-09-20 22:21:42.109 | MS1 | 121.4656676120 | 31.1446250895 | 634 | 504990 | -90.91 | 9.87 | 454.66 | 0.03 | 2.74 | 1569 |

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
| 3230745 | 3 | 121.4700262959 | 31.1474095857 | 117 | 2 | 9 | 49.1 | TDD | 250 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3234023 | 1 | 121.4725875236 | 31.1533472498 | 94 | 4 | 9 | 41.8 | TDD | 57 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3264293 | 4 | 121.4647129145 | 31.1486163560 | 206 | 11 | 9 | 40.5 | TDD | 783 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3265817 | 2 | 121.4662316033 | 31.1555932903 | 196 | 2 | 11 | 43.6 | TDD | 634 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:31.589 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.611 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.732 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.732 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.452 | NREventA3 | measId:2;ServCellPCI:714;Se... |
| 2024-09-20 22:21:38.692 | NRHandoverAttempt | SourcePCI:714;SourceNR-ARFC... |
| 2024-09-20 22:21:38.740 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.755 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.878 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.878 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3234023 | 1 | 12.7069 | 13.3038 | -114.3495 | 17.2548 | 183.2808 | 0.0195 | 0.0130 |
| 2024_09_20 22:00 | 3265817 | 2 | 17.1884 | 19.3498 | -116.4163 | 11.3576 | 105.9153 | 0.0007 | 0.0003 |
| 2024_09_20 22:00 | 3230745 | 3 | 5.6909 | 9.8818 | -116.8767 | 8.3757 | 185.9841 | 0.0178 | 0.0131 |
| 2024_09_20 22:00 | 3264293 | 4 | 18.9283 | 14.8569 | -116.4333 | 17.8046 | 101.0164 | 0.0078 | 0.0080 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415011_733635FE | 504990 | 634 | -93.4 | 504990 | 250 | -96.6 | 504990 | 57 | -103.2 | 504990 | 783 |
| MR_1774415011_F2B09E8A | 504990 | 634 | -90.2 | 504990 | 250 | -95.2 | 504990 | 57 | -103.9 | 504990 | 783 |
| MR_1774415011_CDB356DA | 504990 | 634 | -91.9 | 504990 | 250 | -94.1 | 504990 | 57 | -103.1 | 504990 | 783 |
| MR_1774415011_3525EB5E | 504990 | 634 | -91.7 | 504990 | 250 | -93.4 | 504990 | 57 | -104.9 | 504990 | 783 |
| MR_1774415011_56136418 | 504990 | 634 | -91.3 | 504990 | 250 | -96.0 | 504990 | 57 | -104.3 | 504990 | 783 |
| MR_1774415011_87F388A0 | 504990 | 634 | -93.1 | 504990 | 250 | -92.8 | 504990 | 57 | -106.9 | 504990 | 783 |
| MR_1774415011_7B628EC1 | 504990 | 634 | -90.5 | 504990 | 250 | -95.9 | 504990 | 57 | -105.4 | 504990 | 783 |
| MR_1774415011_F982E3C2 | 504990 | 634 | -93.7 | 504990 | 250 | -95.7 | 504990 | 57 | -105.6 | 504990 | 783 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1786: `e0713f7f-4a6...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `e0713f7f-4a66-4ccc-94e5-e39c28c8c4c2` |
| Tag | **single-answer** |
| 정답 | **C11** |
| C11 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1786] topology](images/train_1786.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3249649_1
- `C2`: Adjust the azimuth of 3249649_1 by 50 degrees
- `C3`: Insufficient data; more data is needed for judgment.
- `C4`: Increase A3 Offset threshold for 3262825_3
- `C5`: Increase transmission power for 3262825_3
- `C6`: Lift the tilt angle of 3262825_3 by 3 degrees
- `C7`: Decrease transmission power for 3249649_1
- `C8`: Decrease A3 Offset threshold for 3262825_3
- `C9`: Press down the tilt angle of 3262825_3 by 3 degrees
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3249649_1
- `C11`: Check test server and transmission issues **← 정답**
- `C12`: Lift the tilt angle  of 3249649_1 by 10 degrees
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3262825_3
- `C14`: Decrease A3 Offset threshold for 3249649_1
- `C15`: Add neighbor relationship between 3225963_2 and 3249649_1
- `C16`: Increase transmission power for 3249649_1
- `C17`: Adjust the azimuth of 3262825_3 by 50 degrees
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3262825_3
- `C19`: Add neighbor relationship between 3262825_3 and 3249649_1
- `C20`: Press down the tilt angle  of 3249649_1 by 10 degrees
- `C21`: Increase A3 Offset threshold for 3249649_1
- `C22`: Decrease transmission power for 3262825_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.539 | MS1 | 121.4656722443 | 31.1446220644 | 846 | 504990 | -87.42 | 16.47 | 509.09 | 0.18 | 2.43 | 1568 |
| 2024-09-20 22:21:32.574 | MS1 | 121.4656597270 | 31.1446304542 | 846 | 504990 | -91.55 | 17.22 | 556.99 | 0.12 | 2.14 | 1588 |
| 2024-09-20 22:21:33.196 | MS1 | 121.4656770376 | 31.1446202435 | 846 | 504990 | -85.11 | 15.59 | 457.38 | 0.18 | 2.82 | 1575 |
| 2024-09-20 22:21:34.838 | MS1 | 121.4656717630 | 31.1446231762 | 846 | 504990 | -87.98 | 13.35 | 65.08 | 0.07 | 2.55 | 456 |
| 2024-09-20 22:21:35.151 | MS1 | 121.4656685632 | 31.1446200984 | 846 | 504990 | -87.22 | 12.24 | 80.08 | 0.19 | 2.48 | 371 |
| 2024-09-20 22:21:36.562 | MS1 | 121.4656728428 | 31.1446274412 | 846 | 504990 | -89.44 | 17.70 | 75.55 | 0.17 | 2.73 | 364 |
| 2024-09-20 22:21:37.532 | MS1 | 121.4656641424 | 31.1446300944 | 846 | 504990 | -92.97 | 7.75 | 81.53 | 0.18 | 2.06 | 328 |
| 2024-09-20 22:21:38.555 | MS1 | 121.4656626408 | 31.1446305729 | 846 | 504990 | -91.75 | 11.83 | 92.12 | 0.12 | 2.40 | 458 |
| 2024-09-20 22:21:39.973 | MS1 | 121.4656581768 | 31.1446355329 | 846 | 504990 | -90.31 | 10.82 | 90.08 | 0.02 | 2.99 | 488 |
| 2024-09-20 22:21:40.965 | MS1 | 121.4656732300 | 31.1446187342 | 846 | 504990 | -91.24 | 12.55 | 569.95 | 0.13 | 2.32 | 1592 |
| 2024-09-20 22:21:41.247 | MS1 | 121.4656701470 | 31.1446324016 | 846 | 504990 | -89.34 | 11.89 | 571.80 | 0.05 | 2.36 | 1583 |
| 2024-09-20 22:21:42.402 | MS1 | 121.4656775993 | 31.1446229024 | 846 | 504990 | -93.71 | 8.36 | 516.55 | 0.10 | 2.97 | 1594 |

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
| 3225963 | 2 | 121.4751576637 | 31.1465432192 | 28 | 12 | 8 | 22.4 | TDD | 612 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3249649 | 1 | 121.4735292692 | 31.1547014821 | 3 | 10 | 11 | 40.1 | TDD | 711 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3262693 | 4 | 121.4713329071 | 31.1446224998 | 202 | 8 | 9 | 46.8 | TDD | 623 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3262825 | 3 | 121.4684315195 | 31.1501894415 | 50 | 1 | 3 | 23.9 | TDD | 846 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |

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
| 2024-09-20 22:21:31.431 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.454 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.573 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.573 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.314 | NREventA3 | measId:2;ServCellPCI:304;Se... |
| 2024-09-20 22:21:38.554 | NRHandoverAttempt | SourcePCI:304;SourceNR-ARFC... |
| 2024-09-20 22:21:38.597 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.611 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.742 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.742 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3249649 | 1 | 6.5300 | 16.7983 | -114.1311 | 10.1149 | 176.1747 | 0.0103 | 0.0079 |
| 2024_09_20 22:00 | 3225963 | 2 | 6.6127 | 10.0711 | -116.8426 | 10.6693 | 121.9347 | 0.0184 | 0.0132 |
| 2024_09_20 22:00 | 3262825 | 3 | 5.0857 | 8.7212 | -117.1140 | 16.5098 | 161.5203 | 0.0012 | 0.0130 |
| 2024_09_20 22:00 | 3262693 | 4 | 14.3995 | 12.2646 | -117.3310 | 6.2076 | 138.3789 | 0.0071 | 0.0110 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415717_AB0262E3 | 504990 | 846 | -88.7 | 504990 | 711 | -89.4 | 504990 | 612 | -93.0 | 504990 | 623 |
| MR_1774415717_8E4E17BB | 504990 | 846 | -86.9 | 504990 | 711 | -86.6 | 504990 | 612 | -95.9 | 504990 | 623 |
| MR_1774415717_F4076DB0 | 504990 | 846 | -88.2 | 504990 | 711 | -86.8 | 504990 | 612 | -95.1 | 504990 | 623 |
| MR_1774415717_E913C35A | 504990 | 846 | -88.1 | 504990 | 711 | -87.7 | 504990 | 612 | -94.8 | 504990 | 623 |
| MR_1774415717_310D04F1 | 504990 | 846 | -88.1 | 504990 | 711 | -86.5 | 504990 | 612 | -94.3 | 504990 | 623 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1787: `72ddbb86-e2c...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `72ddbb86-e2c1-488d-9228-2e4ef6cc3ec3` |
| Tag | **single-answer** |
| 정답 | **C5** |
| C5 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3260959_1 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1787] topology](images/train_1787.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3260959_1
- `C2`: Increase transmission power for 3260959_1
- `C3`: Adjust the azimuth of 3221315_3 by 50 degrees
- `C4`: Increase transmission power for 3221315_3
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3260959_1 **← 정답**
- `C6`: Press down the tilt angle of 3260959_1 by 5 degrees
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3260959_1
- `C8`: Press down the tilt angle  of 3221315_3 by 8 degrees
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3221315_3
- `C10`: Adjust the azimuth of 3260959_1 by 42 degrees
- `C11`: Increase A3 Offset threshold for 3221315_3
- `C12`: Lift the tilt angle  of 3221315_3 by 8 degrees
- `C13`: Insufficient data; more data is needed for judgment.
- `C14`: Add neighbor relationship between 3222212_2 and 3221315_3
- `C15`: Check test server and transmission issues
- `C16`: Decrease transmission power for 3260959_1
- `C17`: Lift the tilt angle of 3260959_1 by 5 degrees
- `C18`: Decrease A3 Offset threshold for 3260959_1
- `C19`: Add neighbor relationship between 3260959_1 and 3221315_3
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3221315_3
- `C21`: Decrease transmission power for 3221315_3
- `C22`: Decrease A3 Offset threshold for 3221315_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.130 | MS1 | 121.4656734723 | 31.1446287019 | 704 | 504990 | -88.59 | 14.10 | 348.13 | 0.17 | 2.85 | 1569 |
| 2024-09-20 22:21:32.622 | MS1 | 121.4656719303 | 31.1446220448 | 704 | 504990 | -87.64 | 14.76 | 545.47 | 0.11 | 2.27 | 1593 |
| 2024-09-20 22:21:33.248 | MS1 | 121.4656708234 | 31.1446232750 | 704 | 504990 | -85.22 | 16.52 | 454.33 | 0.13 | 2.68 | 1594 |
| 2024-09-20 22:21:34.220 | MS1 | 121.4656623862 | 31.1446309797 | 704 | 504990 | -91.49 | 12.48 | 46.58 | 0.69 | 2.64 | 642 |
| 2024-09-20 22:21:35.337 | MS1 | 121.4656591527 | 31.1446350813 | 704 | 504990 | -85.55 | 15.34 | 89.34 | 0.66 | 2.23 | 609 |
| 2024-09-20 22:21:36.342 | MS1 | 121.4656707305 | 31.1446209339 | 704 | 504990 | -87.77 | 13.83 | 53.85 | 0.59 | 2.72 | 652 |
| 2024-09-20 22:21:37.228 | MS1 | 121.4656644134 | 31.1446296443 | 704 | 504990 | -89.82 | 7.32 | 63.29 | 0.68 | 2.58 | 670 |
| 2024-09-20 22:21:38.929 | MS1 | 121.4656748593 | 31.1446317145 | 704 | 504990 | -90.28 | 8.23 | 93.20 | 0.63 | 2.91 | 537 |
| 2024-09-20 22:21:39.240 | MS1 | 121.4656710903 | 31.1446376088 | 704 | 504990 | -89.18 | 8.55 | 99.82 | 0.54 | 2.83 | 545 |
| 2024-09-20 22:21:40.173 | MS1 | 121.4656673096 | 31.1446223066 | 704 | 504990 | -93.38 | 12.16 | 424.71 | 0.05 | 2.50 | 1567 |
| 2024-09-20 22:21:41.880 | MS1 | 121.4656733617 | 31.1446253242 | 704 | 504990 | -93.68 | 12.80 | 363.77 | 0.07 | 2.89 | 1591 |
| 2024-09-20 22:21:42.845 | MS1 | 121.4656742162 | 31.1446226661 | 704 | 504990 | -93.05 | 12.12 | 422.12 | 0.03 | 2.01 | 1562 |

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
| 3221315 | 3 | 121.4656260245 | 31.1558072318 | 359 | 7 | 9 | 28.8 | TDD | 906 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3222212 | 2 | 121.4658921145 | 31.1450517905 | 123 | 9 | 0 | 49.0 | TDD | 361 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3260959 | 1 | 121.4660517351 | 31.1525465828 | 140 | 3 | 10 | 31.8 | TDD | 704 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3269299 | 4 | 121.4686083778 | 31.1462166256 | 41 | 6 | 5 | 24.3 | TDD | 355 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:31.619 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.643 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.792 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.792 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.444 | NREventA3 | measId:2;ServCellPCI:18;Ser... |
| 2024-09-20 22:21:38.684 | NRHandoverAttempt | SourcePCI:18;SourceNR-ARFCN... |
| 2024-09-20 22:21:38.730 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.740 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.858 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.858 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3260959 | 1 | 14.5760 | 6.5900 | -116.4833 | 14.3681 | 184.3336 | 0.0010 | 0.0009 |
| 2024_09_20 22:00 | 3222212 | 2 | 7.4209 | 12.9150 | -117.2477 | 7.7046 | 94.2209 | 0.0020 | 0.0048 |
| 2024_09_20 22:00 | 3221315 | 3 | 6.0675 | 9.3559 | -115.9248 | 10.1665 | 98.2557 | 0.0123 | 0.0032 |
| 2024_09_20 22:00 | 3269299 | 4 | 7.2613 | 6.4282 | -117.2462 | 6.3831 | 167.1229 | 0.0136 | 0.0132 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413235_B96FB7AC | 504990 | 704 | -91.6 | 504990 | 906 | -92.9 | 504990 | 361 | -106.7 | 504990 | 355 |
| MR_1774413235_2A916F1A | 504990 | 704 | -93.2 | 504990 | 906 | -90.4 | 504990 | 361 | -106.0 | 504990 | 355 |
| MR_1774413235_32812351 | 504990 | 704 | -90.7 | 504990 | 906 | -92.4 | 504990 | 361 | -107.5 | 504990 | 355 |
| MR_1774413235_AF6D8E63 | 504990 | 704 | -93.2 | 504990 | 906 | -91.8 | 504990 | 361 | -107.6 | 504990 | 355 |
| MR_1774413235_A06759B4 | 504990 | 704 | -90.9 | 504990 | 906 | -93.2 | 504990 | 361 | -105.6 | 504990 | 355 |
| MR_1774413235_A5CF2A47 | 504990 | 704 | -93.3 | 504990 | 906 | -92.6 | 504990 | 361 | -104.4 | 504990 | 355 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1788: `b7e65ce2-3fd...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `b7e65ce2-3fdc-449b-99f1-1df59249713b` |
| Tag | **multiple-answer** |
| 정답 | **C8|C15** |
| C8 의미 | Increase transmission power for 3261467_1 |
| C15 의미 | Adjust the azimuth of 3261467_1 by 34 degrees |
| 패턴 분류 | **P4 Coverage (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1788] topology](images/train_1788.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle  of 3213629_2 by 4 degrees
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3261467_1
- `C3`: Insufficient data; more data is needed for judgment.
- `C4`: Increase transmission power for 3213629_2
- `C5`: Decrease A3 Offset threshold for 3261467_1
- `C6`: Press down the tilt angle of 3261467_1 by 10 degrees
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3213629_2
- `C8`: Increase transmission power for 3261467_1 **← 정답**
- `C9`: Decrease transmission power for 3261467_1
- `C10`: Increase A3 Offset threshold for 3261467_1
- `C11`: Add neighbor relationship between 3265503_3 and 3213629_2
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3213629_2
- `C13`: Adjust the azimuth of 3213629_2 by 5 degrees
- `C14`: Add neighbor relationship between 3261467_1 and 3213629_2
- `C15`: Adjust the azimuth of 3261467_1 by 34 degrees **← 정답**
- `C16`: Increase A3 Offset threshold for 3213629_2
- `C17`: Decrease A3 Offset threshold for 3213629_2
- `C18`: Lift the tilt angle of 3261467_1 by 10 degrees
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3261467_1
- `C20`: Check test server and transmission issues
- `C21`: Press down the tilt angle  of 3213629_2 by 4 degrees
- `C22`: Decrease transmission power for 3213629_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.762 | MS1 | 121.4656670366 | 31.1446184627 | 8 | 504990 | -87.95 | 15.16 | 329.06 | 0.18 | 2.94 | 1591 |
| 2024-09-20 22:21:32.551 | MS1 | 121.4656634531 | 31.1446338176 | 8 | 504990 | -85.20 | 15.47 | 446.35 | 0.01 | 2.48 | 1595 |
| 2024-09-20 22:21:33.487 | MS1 | 121.4656719360 | 31.1446348007 | 8 | 504990 | -94.10 | 14.59 | 577.10 | 0.17 | 2.08 | 1584 |
| 2024-09-20 22:21:34.245 | MS1 | 121.4656778692 | 31.1446254529 | 8 | 504990 | -102.04 | 1.14 | 30.11 | 0.06 | 1.39 | 1590 |
| 2024-09-20 22:21:35.525 | MS1 | 121.4656613740 | 31.1446211996 | 8 | 504990 | -100.37 | 0.53 | 71.67 | 0.07 | 1.10 | 1583 |
| 2024-09-20 22:21:36.802 | MS1 | 121.4656667643 | 31.1446274656 | 8 | 504990 | -102.20 | 1.25 | 60.36 | 0.10 | 1.38 | 1564 |
| 2024-09-20 22:21:37.310 | MS1 | 121.4656638241 | 31.1446227412 | 8 | 504990 | -102.89 | 0.71 | 51.33 | 0.00 | 1.16 | 1576 |
| 2024-09-20 22:21:38.708 | MS1 | 121.4656741092 | 31.1446320309 | 8 | 504990 | -101.68 | -1.24 | 73.63 | 0.16 | 1.13 | 1577 |
| 2024-09-20 22:21:39.708 | MS1 | 121.4656629048 | 31.1446283929 | 8 | 504990 | -108.61 | -0.77 | 48.18 | 0.20 | 1.30 | 1600 |
| 2024-09-20 22:21:40.574 | MS1 | 121.4656660681 | 31.1446379334 | 8 | 504990 | -87.53 | 15.77 | 559.62 | 0.06 | 2.25 | 1563 |
| 2024-09-20 22:21:41.136 | MS1 | 121.4656688234 | 31.1446333127 | 8 | 504990 | -86.94 | 16.57 | 508.83 | 0.18 | 2.70 | 1578 |
| 2024-09-20 22:21:42.301 | MS1 | 121.4656641788 | 31.1446291350 | 8 | 504990 | -87.18 | 15.41 | 504.39 | 0.05 | 2.93 | 1576 |

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
| 3213629 | 2 | 121.4742104669 | 31.1468644233 | 258 | 3 | 9 | 18.7 | TDD | 923 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3261467 | 1 | 121.4648483759 | 31.1527045719 | 209 | 8 | 4 | 34.8 | TDD | 8 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3265503 | 3 | 121.4667747898 | 31.1498552854 | 284 | 5 | 7 | 41.9 | TDD | 276 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3276134 | 4 | 121.4649959577 | 31.1533641178 | 241 | 8 | 8 | 40.2 | TDD | 197 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |

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
| 2024-09-20 22:21:31.351 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.373 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.490 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.490 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.735 | NREventA2 | measId:1;ServCellPCI:944;Se... |
| 2024-09-20 22:21:34.867 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3261467 | 1 | 9.5773 | 10.1838 | -115.5933 | 14.6543 | 146.9881 | 0.1233 | 0.0116 |
| 2024_09_20 22:00 | 3213629 | 2 | 17.3216 | 13.2535 | -117.4749 | 11.5635 | 82.0508 | 0.0168 | 0.0072 |
| 2024_09_20 22:00 | 3265503 | 3 | 17.9732 | 10.9576 | -116.8602 | 18.6622 | 155.3739 | 0.0054 | 0.0041 |
| 2024_09_20 22:00 | 3276134 | 4 | 19.4952 | 5.5477 | -116.7812 | 12.9521 | 106.9880 | 0.0188 | 0.0142 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412846_88704967 | 504990 | 8 | -103.7 | 504990 | 923 | -106.1 | 504990 | 276 | -117.2 | 504990 | 197 |
| MR_1774412846_13B89F04 | 504990 | 8 | -100.2 | 504990 | 923 | -109.7 | 504990 | 276 | -117.3 | 504990 | 197 |
| MR_1774412846_D7DE6255 | 504990 | 8 | -100.6 | 504990 | 923 | -109.0 | 504990 | 276 | -115.8 | 504990 | 197 |
| MR_1774412846_FEBC949E | 504990 | 8 | -100.0 | 504990 | 923 | -109.3 | 504990 | 276 | -114.2 | 504990 | 197 |
| MR_1774412846_882C1B37 | 504990 | 8 | -100.4 | 504990 | 923 | -105.9 | 504990 | 276 | -115.3 | 504990 | 197 |
| MR_1774412846_79D49E35 | 504990 | 8 | -103.9 | 504990 | 923 | -108.8 | 504990 | 276 | -117.3 | 504990 | 197 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1789: `491bde9e-41b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `491bde9e-41be-4cc9-800f-8e8ce710f5d3` |
| Tag | **single-answer** |
| 정답 | **C9** |
| C9 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3217777_3 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1789] topology](images/train_1789.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3251548_7 and 3217766_6
- `C2`: Insufficient data; more data is needed for judgment.
- `C3`: Press down the tilt angle  of 3217766_6 by 4 degrees
- `C4`: Decrease A3 Offset threshold for 3217777_3
- `C5`: Increase transmission power for 3217766_6
- `C6`: Decrease transmission power for 3217766_6
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3217766_6
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3217777_3
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3217777_3 **← 정답**
- `C10`: Adjust the azimuth of 3217766_6 by 22 degrees
- `C11`: Press down the tilt angle of 3217777_3 by 5 degrees
- `C12`: Decrease transmission power for 3217777_3
- `C13`: Adjust the azimuth of 3217777_3 by 6 degrees
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3217766_6
- `C15`: Increase A3 Offset threshold for 3217777_3
- `C16`: Increase transmission power for 3217777_3
- `C17`: Lift the tilt angle of 3217777_3 by 5 degrees
- `C18`: Lift the tilt angle  of 3217766_6 by 4 degrees
- `C19`: Increase A3 Offset threshold for 3217766_6
- `C20`: Add neighbor relationship between 3217777_3 and 3217766_6
- `C21`: Decrease A3 Offset threshold for 3217766_6
- `C22`: Check test server and transmission issues

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.773 | MS1 | 121.4656587266 | 31.1446215931 | 67 | 504990 | -93.17 | 14.00 | 509.06 | 0.01 | 2.19 | 1565 |
| 2024-09-20 22:21:32.915 | MS1 | 121.4656677881 | 31.1446258955 | 170 | 504990 | -93.72 | 13.78 | 306.70 | 0.17 | 2.50 | 1597 |
| 2024-09-20 22:21:33.737 | MS1 | 121.4656675125 | 31.1446281090 | 674 | 504990 | -94.34 | 14.33 | 498.11 | 0.10 | 2.15 | 1576 |
| 2024-09-20 22:21:34.788 | MS1 | 121.4656703250 | 31.1446186198 | 37 | 152650 | -87.65 | 3.17 | 62.17 | 0.16 | 1.64 | 919 |
| 2024-09-20 22:21:35.383 | MS1 | 121.4656743572 | 31.1446281499 | 758 | 152650 | -92.48 | 5.14 | 86.49 | 0.02 | 1.93 | 905 |
| 2024-09-20 22:21:36.921 | MS1 | 121.4656634605 | 31.1446379646 | 256 | 152650 | -90.22 | 2.93 | 57.75 | 0.01 | 1.54 | 937 |
| 2024-09-20 22:21:37.261 | MS1 | 121.4656626937 | 31.1446262445 | 603 | 152650 | -88.29 | 2.02 | 88.99 | 0.02 | 1.91 | 961 |
| 2024-09-20 22:21:38.379 | MS1 | 121.4656750988 | 31.1446326274 | 37 | 152650 | -93.28 | 4.61 | 96.45 | 0.08 | 1.60 | 998 |
| 2024-09-20 22:21:39.798 | MS1 | 121.4656757035 | 31.1446239643 | 758 | 152650 | -93.95 | 5.36 | 45.18 | 0.13 | 1.82 | 944 |
| 2024-09-20 22:21:40.452 | MS1 | 121.4656703339 | 31.1446289108 | 256 | 152650 | -94.27 | 5.36 | 80.95 | 0.12 | 2.65 | 1597 |
| 2024-09-20 22:21:41.792 | MS1 | 121.4656702375 | 31.1446189965 | 603 | 152650 | -93.33 | 2.85 | 69.82 | 0.07 | 2.39 | 1575 |
| 2024-09-20 22:21:42.804 | MS1 | 121.4656593269 | 31.1446300224 | 37 | 152650 | -94.28 | 6.13 | 73.82 | 0.14 | 2.43 | 1584 |

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
| 3217766 | 6 | 121.4733341670 | 31.1523962154 | 242 | 4 | 12 | 8.8 | TDD | 314 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3217777 | 3 | 121.4684062725 | 31.1480058225 | 221 | 1 | 1 | 28.2 | TDD | 67 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3223600 | 9 | 121.4684035723 | 31.1528349025 | 53 | 12 | 5 | 22.0 | FDD | 334 | n1 | 152650 | 30M | 4T4R | 24 | 152650 |
| 3239737 | 1 | 121.4724167058 | 31.1460787642 | 275 | 1 | 8 | 12.0 | TDD | 832 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3251548 | 7 | 121.4740058875 | 31.1501527646 | 42 | 1 | 3 | 26.6 | FDD | 256 | n1 | 152650 | 30M | 4T4R | 21 | 152650 |
| 3257903 | 2 | 121.4753965393 | 31.1461836575 | 96 | 0 | 5 | 7.9 | TDD | 674 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3262406 | 12 | 121.4740226845 | 31.1503539023 | 293 | 6 | 8 | 10.4 | FDD | 632 | n1 | 152650 | 30M | 4T4R | 22 | 152650 |
| 3264128 | 8 | 121.4695894799 | 31.1488670111 | 64 | 15 | 0 | 5.5 | FDD | 37 | n1 | 152650 | 30M | 4T4R | 23 | 152650 |
| 3266286 | 11 | 121.4647911008 | 31.1518477711 | 77 | 10 | 11 | 27.6 | FDD | 758 | n1 | 152650 | 30M | 4T4R | 19 | 152650 |
| 3269080 | 10 | 121.4739943513 | 31.1536686543 | 139 | 1 | 8 | 1.8 | FDD | 244 | n1 | 152650 | 30M | 4T4R | 18 | 152650 |
| 3274239 | 4 | 121.4650997832 | 31.1525700082 | 280 | 14 | 10 | 13.4 | TDD | 712 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3279004 | 5 | 121.4690664370 | 31.1483999388 | 246 | 10 | 9 | 7.7 | TDD | 170 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3279811 | 13 | 121.4746927269 | 31.1464064915 | 29 | 13 | 9 | 16.1 | FDD | 603 | n1 | 152650 | 30M | 4T4R | 29 | 152650 |

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
| 2024-09-20 22:21:31.554 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.572 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.680 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.680 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.418 | NREventA2 | measId:1;ServCellPCI:645;Se... |
| 2024-09-20 22:21:35.561 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.829 | NREventA5 | measId:3;ServCellPCI:645;Se... |
| 2024-09-20 22:21:35.861 | NRHandoverAttempt | SourcePCI:645;SourceNR-ARFC... |
| 2024-09-20 22:21:35.889 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.904 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:36.018 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.018 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3239737 | 1 | 6.0392 | 14.7771 | -116.5034 | 6.8112 | 98.8723 | 0.0136 | 0.0048 |
| 2024_09_20 22:00 | 3257903 | 2 | 6.3638 | 15.3239 | -116.4348 | 6.4944 | 183.3511 | 0.0139 | 0.0036 |
| 2024_09_20 22:00 | 3217777 | 3 | 12.9817 | 13.7735 | -117.7475 | 10.7476 | 149.9697 | 0.0099 | 0.0101 |
| 2024_09_20 22:00 | 3274239 | 4 | 7.5010 | 11.7094 | -114.5452 | 11.5507 | 118.3181 | 0.0098 | 0.0069 |
| 2024_09_20 22:00 | 3279004 | 5 | 7.7358 | 13.6528 | -114.9590 | 17.0490 | 156.5176 | 0.0010 | 0.0052 |
| 2024_09_20 22:00 | 3217766 | 6 | 12.5682 | 11.6858 | -115.2411 | 8.1523 | 122.7113 | 0.0034 | 0.0153 |
| 2024_09_20 22:00 | 3251548 | 7 | 10.6442 | 17.7578 | -117.4969 | 3.2451 | 34.2175 | 0.0184 | 0.0139 |
| 2024_09_20 22:00 | 3264128 | 8 | 5.6836 | 12.8344 | -114.2010 | 3.9838 | 55.6041 | 0.0192 | 0.0022 |
| 2024_09_20 22:00 | 3223600 | 9 | 10.4294 | 7.8633 | -117.9224 | 4.6363 | 38.5923 | 0.0053 | 0.0084 |
| 2024_09_20 22:00 | 3269080 | 10 | 19.9915 | 15.0398 | -115.2472 | 4.1552 | 59.1056 | 0.0178 | 0.0015 |
| 2024_09_20 22:00 | 3266286 | 11 | 6.1741 | 10.9710 | -115.3639 | 3.1837 | 58.2834 | 0.0082 | 0.0103 |
| 2024_09_20 22:00 | 3262406 | 12 | 16.5030 | 17.6734 | -116.9138 | 3.6757 | 47.3670 | 0.0113 | 0.0197 |
| 2024_09_20 22:00 | 3279811 | 13 | 9.3716 | 17.4929 | -117.0315 | 4.8472 | 36.2325 | 0.0094 | 0.0034 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774411972_31EE7EF0 | 504990 | 674 | -94.3 | 504990 | 314 | -93.9 | 504990 | 832 | -102.5 | 504990 | 712 |
| MR_1774411972_FDE69623 | 504990 | 674 | -93.1 | 504990 | 314 | -93.4 | 504990 | 832 | -100.7 | 504990 | 712 |
| MR_1774411972_73D895B1 | 504990 | 674 | -94.4 | 504990 | 314 | -93.8 | 504990 | 832 | -102.3 | 504990 | 712 |
| MR_1774411972_817BB824 | 504990 | 674 | -94.3 | 504990 | 314 | -93.7 | 504990 | 832 | -100.3 | 504990 | 712 |
| MR_1774411972_6C83F4E1 | 152650 | 37 | -86.5 | 152650 | 334 | -93.1 | 152650 | 244 | -97.0 | 152650 | 632 |
| MR_1774411972_A5C96397 | 152650 | 37 | -87.1 | 152650 | 334 | -94.8 | 152650 | 244 | -94.8 | 152650 | 632 |
| MR_1774411972_EAC7C9AD | 152650 | 37 | -89.1 | 152650 | 334 | -93.0 | 152650 | 244 | -95.8 | 152650 | 632 |
| MR_1774411972_60A0FED4 | 504990 | 674 | -96.3 | 504990 | 314 | -93.0 | 504990 | 832 | -100.5 | 504990 | 712 |

> *... 2개 열 생략 (전체 14열)*

---
