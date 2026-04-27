# Track A 문제 분석 — train[1550]~train[1559]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[1550] ~ train[1559] (10개)

## 목차

1. [문제 1550: `661dd4a7-8f1...`](#1550) — single-answer, 정답: C1
2. [문제 1551: `e14838ab-a62...`](#1551) — multiple-answer, 정답: C5|C8
3. [문제 1552: `cb0ed28c-14a...`](#1552) — multiple-answer, 정답: C2|C4
4. [문제 1553: `6f365dbc-c85...`](#1553) — single-answer, 정답: C19
5. [문제 1554: `fe4614f9-a96...`](#1554) — single-answer, 정답: C6
6. [문제 1555: `cb1ef7ac-185...`](#1555) — single-answer, 정답: C3
7. [문제 1556: `cd1d619b-ff4...`](#1556) — multiple-answer, 정답: C2|C6|C16|C20
8. [문제 1557: `fca01f8d-50b...`](#1557) — multiple-answer, 정답: C9|C14
9. [문제 1558: `02e256dc-59d...`](#1558) — single-answer, 정답: C12
10. [문제 1559: `51fc4268-828...`](#1559) — multiple-answer, 정답: C5|C7|C12|C17

---

### 문제 1550: `661dd4a7-8f1...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `661dd4a7-8f19-4e1a-acb8-2f6d51eb083c` |
| Tag | **single-answer** |
| 정답 | **C1** |
| C1 의미 | Lift the tilt angle  of 3275706_2 by 9 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1550] topology](images/train_1550.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle  of 3275706_2 by 9 degrees **← 정답**
- `C2`: Increase transmission power for 3221224_3
- `C3`: Lift the tilt angle of 3224157_4 by 6 degrees
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3221224_3
- `C5`: Decrease transmission power for 3221224_3
- `C6`: Press down the tilt angle of 3224157_4 by 6 degrees
- `C7`: Insufficient data; more data is needed for judgment.
- `C8`: Decrease A3 Offset threshold for 3224157_4
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3224157_4
- `C10`: Press down the tilt angle  of 3275706_2 by 9 degrees
- `C11`: Add neighbor relationship between 3224157_4 and 3221224_3
- `C12`: Check test server and transmission issues
- `C13`: Increase A3 Offset threshold for 3221224_3
- `C14`: Add neighbor relationship between 3275706_2 and 3221224_3
- `C15`: Decrease transmission power for 3224157_4
- `C16`: Adjust the azimuth of 3224157_4 by 14 degrees
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3221224_3
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3224157_4
- `C19`: Adjust the azimuth of 3275706_2 by 50 degrees
- `C20`: Decrease A3 Offset threshold for 3221224_3
- `C21`: Increase transmission power for 3224157_4
- `C22`: Increase A3 Offset threshold for 3224157_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.134 | MS1 | 121.4656652549 | 31.1446295308 | 7 | 504990 | -89.07 | 17.22 | 543.00 | 0.20 | 2.01 | 1561 |
| 2024-09-20 22:21:32.759 | MS1 | 121.4656713461 | 31.1446202394 | 7 | 504990 | -91.09 | 13.13 | 429.10 | 0.10 | 2.99 | 1586 |
| 2024-09-20 22:21:33.151 | MS1 | 121.4656729327 | 31.1446305616 | 7 | 504990 | -89.98 | 15.69 | 320.27 | 0.20 | 2.97 | 1595 |
| 2024-09-20 22:21:34.153 | MS1 | 121.4656660749 | 31.1446280746 | 7 | 504990 | -89.33 | 14.99 | 55.22 | 0.13 | 2.80 | 1577 |
| 2024-09-20 22:21:35.423 | MS1 | 121.4656673327 | 31.1446199899 | 7 | 504990 | -87.08 | 15.08 | 64.02 | 0.16 | 2.67 | 1571 |
| 2024-09-20 22:21:36.557 | MS1 | 121.4656679364 | 31.1446309620 | 7 | 504990 | -90.41 | 12.35 | 47.96 | 0.10 | 2.04 | 1572 |
| 2024-09-20 22:21:37.728 | MS1 | 121.4656738188 | 31.1446275983 | 7 | 504990 | -93.27 | 12.89 | 93.89 | 0.02 | 2.21 | 1600 |
| 2024-09-20 22:21:38.638 | MS1 | 121.4656640137 | 31.1446203274 | 7 | 504990 | -93.50 | 10.94 | 86.86 | 0.17 | 2.84 | 1596 |
| 2024-09-20 22:21:39.711 | MS1 | 121.4656589931 | 31.1446181449 | 7 | 504990 | -89.25 | 8.93 | 68.86 | 0.13 | 2.43 | 1575 |
| 2024-09-20 22:21:40.196 | MS1 | 121.4656676687 | 31.1446369256 | 7 | 504990 | -93.64 | 11.05 | 382.04 | 0.01 | 2.87 | 1565 |
| 2024-09-20 22:21:41.698 | MS1 | 121.4656708324 | 31.1446214196 | 7 | 504990 | -92.67 | 12.79 | 476.07 | 0.00 | 2.45 | 1588 |
| 2024-09-20 22:21:42.944 | MS1 | 121.4656644929 | 31.1446337491 | 7 | 504990 | -89.67 | 10.08 | 555.20 | 0.01 | 2.40 | 1572 |

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
| 3221224 | 3 | 121.4758620941 | 31.1472657413 | 324 | 8 | 1 | 21.9 | TDD | 157 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3224157 | 4 | 121.4660372841 | 31.1479570829 | 171 | 0 | 4 | 38.9 | TDD | 7 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3273783 | 1 | 121.4735106226 | 31.1526915504 | 173 | 6 | 4 | 44.9 | TDD | 268 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3275706 | 2 | 121.4739961819 | 31.1478786992 | 343 | 12 | 4 | 44.0 | TDD | 317 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:30.814 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.829 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:30.976 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.976 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.633 | NREventA3 | measId:2;ServCellPCI:534;Se... |
| 2024-09-20 22:21:37.873 | NRHandoverAttempt | SourcePCI:534;SourceNR-ARFC... |
| 2024-09-20 22:21:37.919 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.930 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.040 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.040 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3273783 | 1 | 16.1590 | 19.1749 | -115.4768 | 11.2649 | 148.6611 | 0.0053 | 0.0180 |
| 2024_09_20 22:00 | 3275706 | 2 | 5.4209 | 5.1440 | -114.9768 | 5.1726 | 161.8333 | 0.0066 | 0.0104 |
| 2024_09_20 22:00 | 3221224 | 3 | 13.4696 | 7.3716 | -117.8239 | 13.0821 | 126.4842 | 0.0036 | 0.0176 |
| 2024_09_20 22:00 | 3224157 | 4 | 83.1384 | 87.0435 | -115.2815 | 16.6113 | 134.5172 | 0.0185 | 0.0169 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412863_AF0B8D67 | 504990 | 7 | -90.6 | 504990 | 157 | -96.9 | 504990 | 317 | -94.6 | 504990 | 268 |
| MR_1774412863_A26685E8 | 504990 | 7 | -88.1 | 504990 | 157 | -96.6 | 504990 | 317 | -97.3 | 504990 | 268 |
| MR_1774412863_3986AFF4 | 504990 | 7 | -89.6 | 504990 | 157 | -94.5 | 504990 | 317 | -96.5 | 504990 | 268 |
| MR_1774412863_04EAA991 | 504990 | 7 | -91.2 | 504990 | 157 | -95.4 | 504990 | 317 | -94.7 | 504990 | 268 |
| MR_1774412863_D1518A66 | 504990 | 7 | -88.2 | 504990 | 157 | -94.9 | 504990 | 317 | -96.7 | 504990 | 268 |
| MR_1774412863_396820D4 | 504990 | 7 | -91.1 | 504990 | 157 | -95.6 | 504990 | 317 | -95.8 | 504990 | 268 |
| MR_1774412863_DB30E52B | 504990 | 7 | -89.9 | 504990 | 157 | -94.3 | 504990 | 317 | -96.5 | 504990 | 268 |
| MR_1774412863_2C6E3E10 | 504990 | 7 | -90.6 | 504990 | 157 | -94.7 | 504990 | 317 | -96.2 | 504990 | 268 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1551: `e14838ab-a62...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `e14838ab-a629-4afb-a84d-fab6ebbe539d` |
| Tag | **multiple-answer** |
| 정답 | **C5|C8** |
| C5 의미 | Press down the tilt angle  of 3263003_4 by 2 degrees |
| C8 의미 | Decrease transmission power for 3263003_4 |
| 패턴 분류 | **P3 Overshoot (tilt)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1551] topology](images/train_1551.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3224035_2
- `C2`: Insufficient data; more data is needed for judgment.
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3263003_4
- `C4`: Increase transmission power for 3224035_2
- `C5`: Press down the tilt angle  of 3263003_4 by 2 degrees **← 정답**
- `C6`: Increase transmission power for 3263003_4
- `C7`: Add neighbor relationship between 3212375_1 and 3263003_4
- `C8`: Decrease transmission power for 3263003_4 **← 정답**
- `C9`: Increase A3 Offset threshold for 3263003_4
- `C10`: Lift the tilt angle  of 3263003_4 by 2 degrees
- `C11`: Increase A3 Offset threshold for 3224035_2
- `C12`: Adjust the azimuth of 3263003_4 by 0 degrees
- `C13`: Adjust the azimuth of 3224035_2 by 20 degrees
- `C14`: Check test server and transmission issues
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3224035_2
- `C16`: Press down the tilt angle of 3224035_2 by 2 degrees
- `C17`: Lift the tilt angle of 3224035_2 by 2 degrees
- `C18`: Decrease A3 Offset threshold for 3224035_2
- `C19`: Decrease transmission power for 3224035_2
- `C20`: Decrease A3 Offset threshold for 3263003_4
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3263003_4
- `C22`: Add neighbor relationship between 3224035_2 and 3263003_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.329 | MS1 | 121.4656643979 | 31.1446241404 | 68 | 504990 | -81.03 | 17.82 | 460.33 | 0.05 | 2.18 | 1595 |
| 2024-09-20 22:21:32.132 | MS1 | 121.4656603663 | 31.1446366005 | 68 | 504990 | -75.86 | 12.48 | 408.22 | 0.16 | 2.45 | 1567 |
| 2024-09-20 22:21:33.402 | MS1 | 121.4656637025 | 31.1446317321 | 68 | 504990 | -78.40 | 13.78 | 348.26 | 0.04 | 2.43 | 1592 |
| 2024-09-20 22:21:34.258 | MS1 | 121.4656763303 | 31.1446215129 | 68 | 504990 | -87.64 | 2.11 | 66.05 | 0.07 | 1.12 | 1589 |
| 2024-09-20 22:21:35.904 | MS1 | 121.4656711875 | 31.1446368228 | 68 | 504990 | -90.76 | 3.66 | 72.27 | 0.08 | 1.40 | 1576 |
| 2024-09-20 22:21:36.788 | MS1 | 121.4656595594 | 31.1446350533 | 68 | 504990 | -94.00 | 1.10 | 45.95 | 0.14 | 1.15 | 1568 |
| 2024-09-20 22:21:37.512 | MS1 | 121.4656650243 | 31.1446315844 | 68 | 504990 | -87.04 | 0.03 | 51.50 | 0.12 | 1.01 | 1590 |
| 2024-09-20 22:21:38.680 | MS1 | 121.4656730698 | 31.1446327833 | 68 | 504990 | -94.18 | 1.15 | 48.10 | 0.15 | 1.48 | 1600 |
| 2024-09-20 22:21:39.591 | MS1 | 121.4656749808 | 31.1446326930 | 68 | 504990 | -85.16 | 1.95 | 72.92 | 0.01 | 1.49 | 1587 |
| 2024-09-20 22:21:40.221 | MS1 | 121.4656638837 | 31.1446353958 | 68 | 504990 | -75.20 | 17.98 | 586.36 | 0.16 | 2.17 | 1600 |
| 2024-09-20 22:21:41.153 | MS1 | 121.4656773316 | 31.1446190698 | 68 | 504990 | -78.90 | 14.03 | 560.86 | 0.19 | 2.33 | 1594 |
| 2024-09-20 22:21:42.477 | MS1 | 121.4656688773 | 31.1446246325 | 68 | 504990 | -81.24 | 15.02 | 508.61 | 0.13 | 2.96 | 1561 |

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
| 3211426 | 3 | 121.4742601492 | 31.1546611423 | 159 | 1 | 3 | 42.4 | TDD | 589 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3212375 | 1 | 121.4755277547 | 31.1443674639 | 82 | 3 | 5 | 49.1 | TDD | 813 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3224035 | 2 | 121.4754928341 | 31.1559693838 | 237 | 1 | 10 | 16.9 | TDD | 68 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3263003 | 4 | 121.4759079098 | 31.1481078717 | 248 | 0 | 5 | 39.2 | TDD | 615 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |

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
| 2024-09-20 22:21:31.059 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.084 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.198 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.198 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3212375 | 1 | 7.9035 | 14.2886 | -114.2065 | 18.4563 | 116.2349 | 0.0145 | 0.0138 |
| 2024_09_20 22:00 | 3224035 | 2 | 8.3983 | 18.1764 | -109.9845 | 10.1421 | 178.1552 | 0.0034 | 0.0155 |
| 2024_09_20 22:00 | 3211426 | 3 | 8.2565 | 15.9731 | -117.7890 | 11.4836 | 86.1115 | 0.0181 | 0.0149 |
| 2024_09_20 22:00 | 3263003 | 4 | 5.0059 | 14.9138 | -117.4450 | 11.5615 | 164.3863 | 0.0141 | 0.0110 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413651_8904788E | 504990 | 68 | -88.6 | 504990 | 615 | -82.8 | 504990 | 813 | -86.7 | 504990 | 589 |
| MR_1774413651_74E5F258 | 504990 | 68 | -89.5 | 504990 | 615 | -85.4 | 504990 | 813 | -86.2 | 504990 | 589 |
| MR_1774413651_BDA57C23 | 504990 | 615 | -89.5 | 504990 | 68 | -85.6 | 504990 | 813 | -88.1 | 504990 | 589 |
| MR_1774413651_03C2CBF6 | 504990 | 68 | -89.0 | 504990 | 615 | -82.2 | 504990 | 813 | -87.5 | 504990 | 589 |
| MR_1774413651_CC21F5D7 | 504990 | 615 | -86.3 | 504990 | 68 | -84.8 | 504990 | 813 | -89.9 | 504990 | 589 |
| MR_1774413651_10870352 | 504990 | 68 | -88.3 | 504990 | 615 | -81.9 | 504990 | 813 | -87.2 | 504990 | 589 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1552: `cb0ed28c-14a...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `cb0ed28c-14ab-46a1-a9e8-f73b974f48e6` |
| Tag | **multiple-answer** |
| 정답 | **C2|C4** |
| C2 의미 | Increase transmission power for 3229155_1 |
| C4 의미 | Adjust the azimuth of 3229155_1 by 37 degrees |
| 패턴 분류 | **P4 Coverage (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1552] topology](images/train_1552.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3235422_3
- `C2`: Increase transmission power for 3229155_1 **← 정답**
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3235422_3
- `C4`: Adjust the azimuth of 3229155_1 by 37 degrees **← 정답**
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3229155_1
- `C6`: Add neighbor relationship between 3252005_2 and 3235422_3
- `C7`: Increase transmission power for 3235422_3
- `C8`: Add neighbor relationship between 3229155_1 and 3235422_3
- `C9`: Press down the tilt angle  of 3235422_3 by 3 degrees
- `C10`: Lift the tilt angle of 3229155_1 by 10 degrees
- `C11`: Check test server and transmission issues
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3229155_1
- `C13`: Increase A3 Offset threshold for 3229155_1
- `C14`: Adjust the azimuth of 3235422_3 by 37 degrees
- `C15`: Insufficient data; more data is needed for judgment.
- `C16`: Decrease A3 Offset threshold for 3229155_1
- `C17`: Decrease transmission power for 3229155_1
- `C18`: Lift the tilt angle  of 3235422_3 by 3 degrees
- `C19`: Press down the tilt angle of 3229155_1 by 10 degrees
- `C20`: Increase A3 Offset threshold for 3235422_3
- `C21`: Decrease A3 Offset threshold for 3235422_3
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3235422_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.284 | MS1 | 121.4656769911 | 31.1446361918 | 824 | 504990 | -88.01 | 13.14 | 368.57 | 0.15 | 2.34 | 1564 |
| 2024-09-20 22:21:32.568 | MS1 | 121.4656631863 | 31.1446360494 | 824 | 504990 | -90.89 | 16.34 | 607.06 | 0.10 | 2.41 | 1567 |
| 2024-09-20 22:21:33.842 | MS1 | 121.4656618290 | 31.1446289420 | 824 | 504990 | -88.34 | 12.45 | 366.53 | 0.10 | 2.84 | 1587 |
| 2024-09-20 22:21:34.368 | MS1 | 121.4656675367 | 31.1446366703 | 824 | 504990 | -108.98 | -1.91 | 76.35 | 0.08 | 1.46 | 1597 |
| 2024-09-20 22:21:35.616 | MS1 | 121.4656617461 | 31.1446181276 | 824 | 504990 | -106.70 | 0.44 | 59.50 | 0.07 | 1.25 | 1583 |
| 2024-09-20 22:21:36.933 | MS1 | 121.4656645711 | 31.1446291262 | 824 | 504990 | -101.60 | 1.46 | 40.23 | 0.04 | 1.12 | 1568 |
| 2024-09-20 22:21:37.946 | MS1 | 121.4656728526 | 31.1446223667 | 824 | 504990 | -101.11 | 0.70 | 80.26 | 0.08 | 1.28 | 1563 |
| 2024-09-20 22:21:38.200 | MS1 | 121.4656714154 | 31.1446294529 | 824 | 504990 | -109.89 | 1.26 | 73.32 | 0.03 | 1.15 | 1572 |
| 2024-09-20 22:21:39.905 | MS1 | 121.4656620560 | 31.1446379577 | 824 | 504990 | -107.36 | -1.00 | 78.39 | 0.12 | 1.23 | 1568 |
| 2024-09-20 22:21:40.977 | MS1 | 121.4656659296 | 31.1446199538 | 824 | 504990 | -92.56 | 15.50 | 588.55 | 0.06 | 2.37 | 1591 |
| 2024-09-20 22:21:41.367 | MS1 | 121.4656764901 | 31.1446204949 | 824 | 504990 | -93.31 | 14.36 | 470.69 | 0.03 | 2.83 | 1599 |
| 2024-09-20 22:21:42.463 | MS1 | 121.4656666973 | 31.1446358839 | 824 | 504990 | -93.13 | 12.81 | 548.60 | 0.10 | 2.65 | 1582 |

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
| 3214420 | 4 | 121.4657471853 | 31.1492246680 | 283 | 13 | 5 | 46.4 | TDD | 252 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3229155 | 1 | 121.4705334829 | 31.1453034259 | 298 | 9 | 7 | 29.1 | TDD | 824 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3235422 | 3 | 121.4730123640 | 31.1514279929 | 186 | 1 | 3 | 39.2 | TDD | 1003 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3252005 | 2 | 121.4754670053 | 31.1481674134 | 208 | 13 | 2 | 18.5 | TDD | 554 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:30.977 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.997 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.147 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.147 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.359 | NREventA2 | measId:1;ServCellPCI:75;Ser... |
| 2024-09-20 22:21:34.466 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3229155 | 1 | 7.1532 | 5.2335 | -116.9977 | 13.8310 | 193.6429 | 0.1836 | 0.0007 |
| 2024_09_20 22:00 | 3252005 | 2 | 14.8028 | 17.8587 | -115.2922 | 5.2512 | 190.4553 | 0.0139 | 0.0098 |
| 2024_09_20 22:00 | 3235422 | 3 | 19.7525 | 8.3668 | -115.1480 | 19.2290 | 176.2722 | 0.0194 | 0.0061 |
| 2024_09_20 22:00 | 3214420 | 4 | 9.2474 | 19.4563 | -117.3579 | 9.6465 | 132.2576 | 0.0187 | 0.0054 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415935_C8CF5C21 | 504990 | 824 | -109.1 | 504990 | 1003 | -113.3 | 504990 | 554 | -116.2 | 504990 | 252 |
| MR_1774415935_7E7B92F7 | 504990 | 824 | -110.4 | 504990 | 1003 | -112.0 | 504990 | 554 | -115.7 | 504990 | 252 |
| MR_1774415935_E35B1407 | 504990 | 824 | -110.4 | 504990 | 1003 | -112.6 | 504990 | 554 | -118.2 | 504990 | 252 |
| MR_1774415935_CCAE8D56 | 504990 | 824 | -109.8 | 504990 | 1003 | -113.9 | 504990 | 554 | -114.4 | 504990 | 252 |
| MR_1774415935_B297DE16 | 504990 | 824 | -108.5 | 504990 | 1003 | -111.4 | 504990 | 554 | -117.9 | 504990 | 252 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1553: `6f365dbc-c85...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `6f365dbc-c85c-4473-bf14-be3d32c08fbb` |
| Tag | **single-answer** |
| 정답 | **C19** |
| C19 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1553] topology](images/train_1553.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3212327_4 and 3278722_2
- `C2`: Increase A3 Offset threshold for 3278722_2
- `C3`: Press down the tilt angle of 3245492_3 by 10 degrees
- `C4`: Increase transmission power for 3245492_3
- `C5`: Decrease A3 Offset threshold for 3245492_3
- `C6`: Increase transmission power for 3278722_2
- `C7`: Increase A3 Offset threshold for 3245492_3
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3245492_3
- `C9`: Decrease transmission power for 3245492_3
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3278722_2
- `C11`: Decrease A3 Offset threshold for 3278722_2
- `C12`: Lift the tilt angle  of 3278722_2 by 10 degrees
- `C13`: Check test server and transmission issues
- `C14`: Press down the tilt angle  of 3278722_2 by 10 degrees
- `C15`: Lift the tilt angle of 3245492_3 by 10 degrees
- `C16`: Adjust the azimuth of 3278722_2 by 31 degrees
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3245492_3
- `C18`: Add neighbor relationship between 3245492_3 and 3278722_2
- `C19`: Insufficient data; more data is needed for judgment. **← 정답**
- `C20`: Adjust the azimuth of 3245492_3 by 41 degrees
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3278722_2
- `C22`: Decrease transmission power for 3278722_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.966 | MS1 | 121.4656724493 | 31.1446194948 | 53 | 504990 | -90.84 | 17.47 | 308.12 | 0.18 | 2.12 | 1578 |
| 2024-09-20 22:21:32.415 | MS1 | 121.4656679974 | 31.1446305980 | 53 | 504990 | -86.92 | 14.44 | 451.32 | 0.10 | 2.33 | 1597 |
| 2024-09-20 22:21:33.231 | MS1 | 121.4656746836 | 31.1446194790 | 53 | 504990 | -90.15 | 13.61 | 492.82 | 0.07 | 2.31 | 1566 |
| 2024-09-20 22:21:34.206 | MS1 | 121.4656663801 | 31.1446319910 | 53 | 504990 | -87.88 | 12.15 | 67.86 | 0.07 | 2.45 | 1597 |
| 2024-09-20 22:21:35.457 | MS1 | 121.4656768713 | 31.1446296580 | 53 | 504990 | -91.85 | 14.83 | 52.71 | 0.01 | 2.54 | 1583 |
| 2024-09-20 22:21:36.723 | MS1 | 121.4656693846 | 31.1446192560 | 53 | 504990 | -88.70 | 15.87 | 79.35 | 0.06 | 2.38 | 1569 |
| 2024-09-20 22:21:37.232 | MS1 | 121.4656767049 | 31.1446209494 | 53 | 504990 | -90.04 | 7.40 | 91.00 | 0.05 | 2.63 | 1564 |
| 2024-09-20 22:21:38.955 | MS1 | 121.4656656222 | 31.1446251295 | 53 | 504990 | -92.43 | 7.26 | 100.68 | 0.19 | 2.07 | 1584 |
| 2024-09-20 22:21:39.900 | MS1 | 121.4656580758 | 31.1446217975 | 53 | 504990 | -91.25 | 10.35 | 88.95 | 0.15 | 2.77 | 1567 |
| 2024-09-20 22:21:40.872 | MS1 | 121.4656586273 | 31.1446256655 | 53 | 504990 | -91.83 | 9.91 | 587.80 | 0.05 | 2.75 | 1591 |
| 2024-09-20 22:21:41.443 | MS1 | 121.4656720565 | 31.1446280760 | 53 | 504990 | -93.35 | 8.02 | 473.09 | 0.14 | 2.49 | 1597 |
| 2024-09-20 22:21:42.744 | MS1 | 121.4656691948 | 31.1446352542 | 53 | 504990 | -89.76 | 12.76 | 457.45 | 0.19 | 2.65 | 1564 |

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
| 3212327 | 4 | 121.4741301644 | 31.1499424581 | 136 | 3 | 0 | 38.1 | TDD | 470 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3236413 | 1 | 121.4664822695 | 31.1558389835 | 91 | 9 | 7 | 23.3 | TDD | 424 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3245492 | 3 | 121.4700313132 | 31.1549735669 | 241 | 8 | 10 | 39.3 | TDD | 53 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3278722 | 2 | 121.4698793678 | 31.1555936424 | 167 | 11 | 4 | 32.3 | TDD | 377 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:31.129 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.246 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.246 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.968 | NREventA3 | measId:2;ServCellPCI:570;Se... |
| 2024-09-20 22:21:38.208 | NRHandoverAttempt | SourcePCI:570;SourceNR-ARFC... |
| 2024-09-20 22:21:38.251 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.262 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.374 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.374 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3236413 | 1 | 87.1611 | 82.7624 | -117.0216 | 12.0552 | 163.3151 | 0.0075 | 0.0004 |
| 2024_09_19 22:00 | 3278722 | 2 | 83.3516 | 88.2220 | -115.4010 | 19.3979 | 125.6410 | 0.0158 | 0.0073 |
| 2024_09_19 22:00 | 3245492 | 3 | 86.5868 | 93.0440 | -116.6099 | 11.1390 | 164.4866 | 0.0111 | 0.0091 |
| 2024_09_19 22:00 | 3212327 | 4 | 79.8275 | 91.0773 | -117.7067 | 15.7534 | 193.0701 | 0.0035 | 0.0146 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412961_646E44C4 | 504990 | 53 | -89.6 | 504990 | 377 | -93.9 | 504990 | 470 | -100.1 | 504990 | 424 |
| MR_1774412961_13BA3384 | 504990 | 53 | -89.2 | 504990 | 377 | -91.3 | 504990 | 470 | -96.9 | 504990 | 424 |
| MR_1774412961_15CCD4D7 | 504990 | 53 | -88.1 | 504990 | 377 | -92.4 | 504990 | 470 | -99.9 | 504990 | 424 |
| MR_1774412961_33C69B9E | 504990 | 53 | -87.5 | 504990 | 377 | -92.5 | 504990 | 470 | -98.5 | 504990 | 424 |
| MR_1774412961_6DD4C1E8 | 504990 | 53 | -87.2 | 504990 | 377 | -92.3 | 504990 | 470 | -96.6 | 504990 | 424 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1554: `fe4614f9-a96...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `fe4614f9-a964-43d4-b809-6f265c44ea85` |
| Tag | **single-answer** |
| 정답 | **C6** |
| C6 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3254300_4 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1554] topology](images/train_1554.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment.
- `C2`: Decrease A3 Offset threshold for 3254300_4
- `C3`: Decrease A3 Offset threshold for 3228525_6
- `C4`: Check test server and transmission issues
- `C5`: Adjust the azimuth of 3254300_4 by 18 degrees
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3254300_4 **← 정답**
- `C7`: Increase transmission power for 3228525_6
- `C8`: Lift the tilt angle of 3254300_4 by 5 degrees
- `C9`: Add neighbor relationship between 3261534_9 and 3228525_6
- `C10`: Add neighbor relationship between 3254300_4 and 3228525_6
- `C11`: Decrease transmission power for 3228525_6
- `C12`: Press down the tilt angle of 3254300_4 by 5 degrees
- `C13`: Increase A3 Offset threshold for 3254300_4
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3228525_6
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3228525_6
- `C16`: Increase A3 Offset threshold for 3228525_6
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3254300_4
- `C18`: Press down the tilt angle  of 3228525_6 by 2 degrees
- `C19`: Decrease transmission power for 3254300_4
- `C20`: Adjust the azimuth of 3228525_6 by 7 degrees
- `C21`: Lift the tilt angle  of 3228525_6 by 2 degrees
- `C22`: Increase transmission power for 3254300_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.843 | MS1 | 121.4656640878 | 31.1446366281 | 11 | 504990 | -95.58 | 14.24 | 481.61 | 0.06 | 2.76 | 1583 |
| 2024-09-20 22:21:32.775 | MS1 | 121.4656687050 | 31.1446323240 | 133 | 504990 | -94.39 | 11.84 | 571.26 | 0.18 | 2.77 | 1576 |
| 2024-09-20 22:21:33.141 | MS1 | 121.4656624940 | 31.1446230147 | 973 | 504990 | -93.17 | 10.02 | 482.03 | 0.02 | 2.12 | 1589 |
| 2024-09-20 22:21:34.197 | MS1 | 121.4656778050 | 31.1446288876 | 788 | 152650 | -88.65 | 5.82 | 74.14 | 0.05 | 1.61 | 980 |
| 2024-09-20 22:21:35.687 | MS1 | 121.4656634344 | 31.1446196002 | 111 | 152650 | -87.72 | 5.32 | 79.95 | 0.17 | 1.92 | 976 |
| 2024-09-20 22:21:36.300 | MS1 | 121.4656663454 | 31.1446334308 | 562 | 152650 | -87.26 | 6.40 | 80.23 | 0.00 | 1.92 | 941 |
| 2024-09-20 22:21:37.887 | MS1 | 121.4656627822 | 31.1446264310 | 478 | 152650 | -90.58 | 4.88 | 46.16 | 0.10 | 1.70 | 970 |
| 2024-09-20 22:21:38.993 | MS1 | 121.4656688875 | 31.1446288224 | 788 | 152650 | -94.28 | 6.91 | 86.40 | 0.02 | 1.80 | 942 |
| 2024-09-20 22:21:39.480 | MS1 | 121.4656631769 | 31.1446368031 | 111 | 152650 | -87.09 | 6.95 | 48.66 | 0.00 | 1.60 | 988 |
| 2024-09-20 22:21:40.919 | MS1 | 121.4656663699 | 31.1446241900 | 562 | 152650 | -91.57 | 5.04 | 102.49 | 0.09 | 2.39 | 1575 |
| 2024-09-20 22:21:41.114 | MS1 | 121.4656665888 | 31.1446288729 | 478 | 152650 | -91.80 | 3.92 | 79.16 | 0.06 | 2.97 | 1580 |
| 2024-09-20 22:21:42.813 | MS1 | 121.4656666800 | 31.1446337937 | 788 | 152650 | -89.88 | 4.44 | 59.35 | 0.05 | 2.96 | 1600 |

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
| 3212601 | 11 | 121.4702325836 | 31.1492033488 | 71 | 5 | 9 | 1.3 | FDD | 788 | n1 | 152650 | 30M | 4T4R | 18 | 152650 |
| 3215959 | 13 | 121.4707243865 | 31.1510065109 | 4 | 0 | 2 | 17.9 | FDD | 478 | n1 | 152650 | 30M | 4T4R | 13 | 152650 |
| 3218645 | 3 | 121.4656587733 | 31.1507954774 | 86 | 1 | 4 | 3.2 | TDD | 549 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3224393 | 5 | 121.4678702850 | 31.1539091841 | 302 | 0 | 11 | 4.7 | TDD | 973 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3228525 | 6 | 121.4682973684 | 31.1530739529 | 202 | 1 | 0 | 21.5 | TDD | 309 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3240887 | 1 | 121.4661614941 | 31.1506181616 | 65 | 4 | 10 | 14.6 | TDD | 352 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3243616 | 10 | 121.4706483214 | 31.1505608004 | 54 | 4 | 8 | 22.7 | FDD | 851 | n1 | 152650 | 30M | 4T4R | 12 | 152650 |
| 3251861 | 12 | 121.4758976208 | 31.1450194731 | 105 | 6 | 3 | 1.5 | FDD | 157 | n1 | 152650 | 30M | 4T4R | 11 | 152650 |
| 3252849 | 8 | 121.4659591157 | 31.1527354272 | 84 | 9 | 0 | 9.7 | FDD | 111 | n1 | 152650 | 30M | 4T4R | 28 | 152650 |
| 3252985 | 7 | 121.4756905181 | 31.1557711395 | 3 | 1 | 2 | 28.5 | FDD | 271 | n1 | 152650 | 30M | 4T4R | 25 | 152650 |
| 3254300 | 4 | 121.4756828617 | 31.1485230512 | 228 | 3 | 6 | 29.9 | TDD | 11 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3259536 | 2 | 121.4737446828 | 31.1490776075 | 52 | 6 | 5 | 21.0 | TDD | 133 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3261534 | 9 | 121.4650659459 | 31.1440691811 | 45 | 3 | 7 | 13.3 | FDD | 562 | n1 | 152650 | 30M | 4T4R | 15 | 152650 |

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
| 2024-09-20 22:21:30.999 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.015 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.157 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.157 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.887 | NREventA2 | measId:1;ServCellPCI:1000;S... |
| 2024-09-20 22:21:35.006 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.273 | NREventA5 | measId:3;ServCellPCI:1000;S... |
| 2024-09-20 22:21:35.323 | NRHandoverAttempt | SourcePCI:1000;SourceNR-ARF... |
| 2024-09-20 22:21:35.357 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.370 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:35.502 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.502 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3240887 | 1 | 14.8134 | 8.8412 | -114.8739 | 8.6082 | 154.8138 | 0.0146 | 0.0006 |
| 2024_09_20 22:00 | 3259536 | 2 | 19.2240 | 5.8787 | -114.7505 | 19.8811 | 102.3569 | 0.0053 | 0.0096 |
| 2024_09_20 22:00 | 3218645 | 3 | 17.8081 | 7.6095 | -115.3736 | 12.0138 | 149.5277 | 0.0070 | 0.0181 |
| 2024_09_20 22:00 | 3254300 | 4 | 9.8479 | 11.6442 | -114.5608 | 10.0612 | 153.0679 | 0.0111 | 0.0142 |
| 2024_09_20 22:00 | 3224393 | 5 | 17.4585 | 8.2580 | -114.5514 | 6.3619 | 106.1647 | 0.0195 | 0.0029 |
| 2024_09_20 22:00 | 3228525 | 6 | 13.7043 | 6.1785 | -116.0504 | 6.7833 | 152.7134 | 0.0093 | 0.0091 |
| 2024_09_20 22:00 | 3252985 | 7 | 15.8862 | 6.5184 | -117.0751 | 4.2056 | 22.3783 | 0.0110 | 0.0132 |
| 2024_09_20 22:00 | 3252849 | 8 | 6.2073 | 8.6933 | -114.8309 | 4.6666 | 54.2148 | 0.0014 | 0.0069 |
| 2024_09_20 22:00 | 3261534 | 9 | 19.5715 | 15.1377 | -117.6838 | 4.9570 | 57.2969 | 0.0122 | 0.0176 |
| 2024_09_20 22:00 | 3243616 | 10 | 7.1098 | 6.4251 | -116.4538 | 4.5850 | 30.0697 | 0.0125 | 0.0042 |
| 2024_09_20 22:00 | 3212601 | 11 | 7.6633 | 12.4129 | -114.1032 | 3.9162 | 53.7871 | 0.0150 | 0.0183 |
| 2024_09_20 22:00 | 3251861 | 12 | 10.5240 | 6.8571 | -114.1649 | 3.1378 | 59.0292 | 0.0000 | 0.0152 |
| 2024_09_20 22:00 | 3215959 | 13 | 19.4816 | 6.0677 | -114.8354 | 3.9773 | 27.1243 | 0.0044 | 0.0106 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412818_383A99ED | 504990 | 973 | -95.0 | 504990 | 309 | -90.1 | 504990 | 549 | -101.8 | 504990 | 352 |
| MR_1774412818_A4A37579 | 152650 | 788 | -88.4 | 152650 | 271 | -89.3 | 152650 | 157 | -97.3 | 152650 | 851 |
| MR_1774412818_B86AA8FC | 504990 | 973 | -94.2 | 504990 | 309 | -89.0 | 504990 | 549 | -101.3 | 504990 | 352 |
| MR_1774412818_9AF00193 | 152650 | 788 | -87.8 | 152650 | 271 | -92.2 | 152650 | 157 | -100.5 | 152650 | 851 |
| MR_1774412818_EBBE2D8C | 152650 | 788 | -89.4 | 152650 | 271 | -91.1 | 152650 | 157 | -98.7 | 152650 | 851 |
| MR_1774412818_7D09DAD1 | 504990 | 973 | -94.8 | 504990 | 309 | -91.8 | 504990 | 549 | -99.3 | 504990 | 352 |
| MR_1774412818_63FE2429 | 504990 | 973 | -94.9 | 504990 | 309 | -89.6 | 504990 | 549 | -98.8 | 504990 | 352 |
| MR_1774412818_8AE09B47 | 152650 | 788 | -89.6 | 152650 | 271 | -92.1 | 152650 | 157 | -100.2 | 152650 | 851 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1555: `cb1ef7ac-185...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `cb1ef7ac-185d-41e7-97c8-f39029b9b5bb` |
| Tag | **single-answer** |
| 정답 | **C3** |
| C3 의미 | Lift the tilt angle  of 3229668_2 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1555] topology](images/train_1555.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3252016_1
- `C2`: Add neighbor relationship between 3229668_2 and 3252016_1
- `C3`: Lift the tilt angle  of 3229668_2 by 10 degrees **← 정답**
- `C4`: Decrease transmission power for 3252016_1
- `C5`: Increase transmission power for 3231973_4
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3252016_1
- `C7`: Decrease transmission power for 3231973_4
- `C8`: Increase A3 Offset threshold for 3252016_1
- `C9`: Increase A3 Offset threshold for 3231973_4
- `C10`: Insufficient data; more data is needed for judgment.
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3231973_4
- `C12`: Add neighbor relationship between 3231973_4 and 3252016_1
- `C13`: Decrease A3 Offset threshold for 3252016_1
- `C14`: Press down the tilt angle of 3231973_4 by 2 degrees
- `C15`: Adjust the azimuth of 3231973_4 by 19 degrees
- `C16`: Decrease A3 Offset threshold for 3231973_4
- `C17`: Press down the tilt angle  of 3229668_2 by 10 degrees
- `C18`: Increase transmission power for 3252016_1
- `C19`: Check test server and transmission issues
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3231973_4
- `C21`: Adjust the azimuth of 3229668_2 by 50 degrees
- `C22`: Lift the tilt angle of 3231973_4 by 2 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.428 | MS1 | 121.4656715442 | 31.1446288404 | 527 | 504990 | -87.61 | 13.22 | 488.49 | 0.01 | 2.28 | 1583 |
| 2024-09-20 22:21:32.702 | MS1 | 121.4656767037 | 31.1446351136 | 527 | 504990 | -87.93 | 16.10 | 507.82 | 0.11 | 2.69 | 1574 |
| 2024-09-20 22:21:33.165 | MS1 | 121.4656581042 | 31.1446368187 | 527 | 504990 | -90.98 | 17.17 | 391.07 | 0.02 | 2.82 | 1568 |
| 2024-09-20 22:21:34.449 | MS1 | 121.4656611414 | 31.1446294010 | 527 | 504990 | -91.13 | 15.72 | 103.76 | 0.13 | 2.13 | 1569 |
| 2024-09-20 22:21:35.672 | MS1 | 121.4656753365 | 31.1446189677 | 527 | 504990 | -88.68 | 13.61 | 54.57 | 0.06 | 2.14 | 1599 |
| 2024-09-20 22:21:36.491 | MS1 | 121.4656752843 | 31.1446282678 | 527 | 504990 | -91.68 | 16.44 | 92.57 | 0.10 | 2.07 | 1567 |
| 2024-09-20 22:21:37.549 | MS1 | 121.4656760945 | 31.1446264938 | 527 | 504990 | -90.04 | 10.06 | 60.77 | 0.17 | 2.43 | 1586 |
| 2024-09-20 22:21:38.179 | MS1 | 121.4656632505 | 31.1446195517 | 527 | 504990 | -93.21 | 9.69 | 56.47 | 0.10 | 2.70 | 1582 |
| 2024-09-20 22:21:39.479 | MS1 | 121.4656701535 | 31.1446326125 | 527 | 504990 | -91.14 | 7.63 | 53.86 | 0.12 | 2.45 | 1597 |
| 2024-09-20 22:21:40.443 | MS1 | 121.4656582932 | 31.1446370789 | 527 | 504990 | -90.94 | 12.40 | 461.71 | 0.18 | 2.08 | 1590 |
| 2024-09-20 22:21:41.864 | MS1 | 121.4656779815 | 31.1446193126 | 527 | 504990 | -92.14 | 9.81 | 402.39 | 0.09 | 2.23 | 1577 |
| 2024-09-20 22:21:42.428 | MS1 | 121.4656601895 | 31.1446330318 | 527 | 504990 | -92.62 | 12.62 | 401.18 | 0.16 | 2.91 | 1587 |

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
| 3229668 | 2 | 121.4751185926 | 31.1448704804 | 354 | 3 | 7 | 43.6 | TDD | 874 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3231973 | 4 | 121.4721958772 | 31.1550579066 | 189 | 1 | 9 | 26.9 | TDD | 527 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3247812 | 3 | 121.4682017193 | 31.1488771993 | 55 | 8 | 7 | 42.4 | TDD | 148 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3252016 | 1 | 121.4687319752 | 31.1451785384 | 91 | 14 | 5 | 28.9 | TDD | 905 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:31.379 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.402 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.502 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.502 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.228 | NREventA3 | measId:2;ServCellPCI:558;Se... |
| 2024-09-20 22:21:38.468 | NRHandoverAttempt | SourcePCI:558;SourceNR-ARFC... |
| 2024-09-20 22:21:38.511 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.521 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.668 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.668 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3252016 | 1 | 12.8573 | 18.6000 | -115.7454 | 5.5746 | 135.0558 | 0.0143 | 0.0188 |
| 2024_09_20 22:00 | 3229668 | 2 | 11.5439 | 15.9493 | -114.1881 | 17.0740 | 172.5761 | 0.0095 | 0.0101 |
| 2024_09_20 22:00 | 3247812 | 3 | 9.3467 | 12.2357 | -116.0007 | 6.5003 | 85.5244 | 0.0108 | 0.0010 |
| 2024_09_20 22:00 | 3231973 | 4 | 76.9044 | 75.1413 | -115.4623 | 13.8612 | 151.9971 | 0.0043 | 0.0035 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416386_366CA821 | 504990 | 527 | -87.8 | 504990 | 905 | -90.6 | 504990 | 874 | -96.8 | 504990 | 148 |
| MR_1774416386_40784D6D | 504990 | 527 | -89.5 | 504990 | 905 | -89.4 | 504990 | 874 | -98.3 | 504990 | 148 |
| MR_1774416386_84DB4A8D | 504990 | 527 | -89.7 | 504990 | 905 | -88.4 | 504990 | 874 | -95.1 | 504990 | 148 |
| MR_1774416386_C9A60969 | 504990 | 527 | -87.4 | 504990 | 905 | -90.0 | 504990 | 874 | -95.7 | 504990 | 148 |
| MR_1774416386_1B6CBCEA | 504990 | 527 | -88.2 | 504990 | 905 | -91.5 | 504990 | 874 | -96.0 | 504990 | 148 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1556: `cd1d619b-ff4...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `cd1d619b-ff4b-4477-9020-1ab8e4b277cc` |
| Tag | **multiple-answer** |
| 정답 | **C2|C6|C16|C20** |
| C2 의미 | Press down the tilt angle  of 3278507_2 by 2 degrees |
| C6 의미 | Increase A3 Offset threshold for 3278507_2 |
| C16 의미 | Decrease transmission power for 3278507_2 |
| C20 의미 | Increase A3 Offset threshold for 3238910_1 |
| 패턴 분류 | **P3 Overshoot (tilt)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1556] topology](images/train_1556.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 5 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 5개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3238910_1
- `C2`: Press down the tilt angle  of 3278507_2 by 2 degrees **← 정답**
- `C3`: Add neighbor relationship between 3238910_1 and 3278507_2
- `C4`: Decrease A3 Offset threshold for 3278507_2
- `C5`: Lift the tilt angle  of 3278507_2 by 2 degrees
- `C6`: Increase A3 Offset threshold for 3278507_2 **← 정답**
- `C7`: Decrease transmission power for 3238910_1
- `C8`: Insufficient data; more data is needed for judgment.
- `C9`: Press down the tilt angle of 3238910_1 by 4 degrees
- `C10`: Adjust the azimuth of 3278507_2 by 30 degrees
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3278507_2
- `C12`: Add neighbor relationship between 3261670_3 and 3278507_2
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3278507_2
- `C14`: Adjust the azimuth of 3238910_1 by 39 degrees
- `C15`: Increase transmission power for 3238910_1
- `C16`: Decrease transmission power for 3278507_2 **← 정답**
- `C17`: Lift the tilt angle of 3238910_1 by 4 degrees
- `C18`: Decrease A3 Offset threshold for 3238910_1
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3238910_1
- `C20`: Increase A3 Offset threshold for 3238910_1 **← 정답**
- `C21`: Increase transmission power for 3278507_2
- `C22`: Check test server and transmission issues

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.112 | MS1 | 121.4656587728 | 31.1446228550 | 198 | 504990 | -75.05 | 17.08 | 395.07 | 0.12 | 2.76 | 1600 |
| 2024-09-20 22:21:32.171 | MS1 | 121.4656594390 | 31.1446284548 | 198 | 504990 | -80.37 | 13.28 | 331.95 | 0.09 | 2.20 | 1580 |
| 2024-09-20 22:21:33.189 | MS1 | 121.4656748644 | 31.1446188937 | 198 | 504990 | -83.33 | 17.04 | 482.84 | 0.06 | 3.00 | 1585 |
| 2024-09-20 22:21:34.152 | MS1 | 121.4656753161 | 31.1446195210 | 312 | 504990 | -85.22 | 3.66 | 50.72 | 0.07 | 1.03 | 1578 |
| 2024-09-20 22:21:35.854 | MS1 | 121.4656742747 | 31.1446335697 | 312 | 504990 | -83.22 | 3.94 | 29.28 | 0.15 | 1.32 | 1589 |
| 2024-09-20 22:21:36.163 | MS1 | 121.4656678990 | 31.1446264690 | 198 | 504990 | -85.80 | 1.87 | 34.37 | 0.01 | 1.08 | 1592 |
| 2024-09-20 22:21:37.582 | MS1 | 121.4656592540 | 31.1446233311 | 198 | 504990 | -81.81 | 3.77 | 61.22 | 0.07 | 1.15 | 1574 |
| 2024-09-20 22:21:38.628 | MS1 | 121.4656618384 | 31.1446336110 | 312 | 504990 | -81.28 | 1.29 | 59.41 | 0.14 | 1.26 | 1571 |
| 2024-09-20 22:21:39.737 | MS1 | 121.4656733733 | 31.1446298731 | 312 | 504990 | -84.49 | 2.97 | 84.78 | 0.13 | 1.36 | 1586 |
| 2024-09-20 22:21:40.866 | MS1 | 121.4656663261 | 31.1446339769 | 312 | 504990 | -75.76 | 12.91 | 491.82 | 0.18 | 2.50 | 1581 |
| 2024-09-20 22:21:41.935 | MS1 | 121.4656766538 | 31.1446325013 | 312 | 504990 | -83.54 | 16.06 | 315.05 | 0.12 | 2.77 | 1573 |
| 2024-09-20 22:21:42.319 | MS1 | 121.4656653075 | 31.1446353262 | 312 | 504990 | -82.74 | 17.21 | 483.93 | 0.15 | 2.86 | 1592 |

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
| 3214912 | 4 | 121.4665534472 | 31.1510447283 | 313 | 11 | 7 | 15.7 | TDD | 312 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3238910 | 1 | 121.4724191994 | 31.1465190449 | 213 | 3 | 0 | 16.9 | TDD | 198 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3259444 | 5 | 121.4706462870 | 31.1537240101 | 216 | 7 | 0 | 19.7 | TDD | 441 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3261670 | 3 | 121.4730458780 | 31.1441547441 | 153 | 0 | 10 | 43.0 | TDD | 527 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3278507 | 2 | 121.4658549491 | 31.1526640977 | 151 | 1 | 4 | 22.2 | TDD | 111 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |

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
| 2024-09-20 22:21:31.545 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.560 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.705 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.705 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.365 | NREventA3 | measId:2;ServCellPCI:519;Se... |
| 2024-09-20 22:21:34.605 | NRHandoverAttempt | SourcePCI:519;SourceNR-ARFC... |
| 2024-09-20 22:21:34.642 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:34.657 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:34.765 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:34.765 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:36.365 | NREventA3 | measId:2;ServCellPCI:141;Se... |
| 2024-09-20 22:21:36.605 | NRHandoverAttempt | SourcePCI:141;SourceNR-ARFC... |
| 2024-09-20 22:21:36.650 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:36.661 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:36.801 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.801 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.365 | NREventA3 | measId:2;ServCellPCI:519;Se... |
| 2024-09-20 22:21:38.605 | NRHandoverAttempt | SourcePCI:519;SourceNR-ARFC... |
| 2024-09-20 22:21:38.642 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.655 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.770 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.770 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3238910 | 1 | 12.3410 | 11.8222 | -117.2261 | 10.9717 | 190.4232 | 0.0098 | 0.0013 |
| 2024_09_20 22:00 | 3278507 | 2 | 7.9279 | 17.5829 | -117.1628 | 15.6572 | 131.2576 | 0.0102 | 0.0018 |
| 2024_09_20 22:00 | 3261670 | 3 | 12.7851 | 5.1470 | -115.3740 | 15.9743 | 125.6999 | 0.0034 | 0.0104 |
| 2024_09_20 22:00 | 3214912 | 4 | 19.1593 | 14.2263 | -115.8188 | 10.6652 | 141.0631 | 0.0173 | 0.0018 |
| 2024_09_20 22:00 | 3259444 | 5 | 13.4370 | 12.7853 | -116.6101 | 8.8837 | 116.0601 | 0.0187 | 0.0086 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412695_ACE51DAC | 504990 | 312 | -86.6 | 504990 | 198 | -83.1 | 504990 | 111 | -86.3 | 504990 | 527 |
| MR_1774412695_CF30A2DF | 504990 | 198 | -84.8 | 504990 | 312 | -85.9 | 504990 | 111 | -85.3 | 504990 | 527 |
| MR_1774412695_88DB4A29 | 504990 | 198 | -84.5 | 504990 | 312 | -83.6 | 504990 | 111 | -85.3 | 504990 | 527 |
| MR_1774412695_B53841A0 | 504990 | 312 | -86.7 | 504990 | 198 | -83.2 | 504990 | 111 | -85.2 | 504990 | 527 |
| MR_1774412695_C8740802 | 504990 | 312 | -85.3 | 504990 | 198 | -82.5 | 504990 | 111 | -84.7 | 504990 | 527 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1557: `fca01f8d-50b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `fca01f8d-50b2-4e99-886d-e186f18f5dbd` |
| Tag | **multiple-answer** |
| 정답 | **C9|C14** |
| C9 의미 | Decrease transmission power for 3250963_3 |
| C14 의미 | Press down the tilt angle  of 3250963_3 by 4 degrees |
| 패턴 분류 | **P3 Overshoot (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1557] topology](images/train_1557.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3272437_2
- `C2`: Add neighbor relationship between 3272437_2 and 3250963_3
- `C3`: Adjust the azimuth of 3250963_3 by 10 degrees
- `C4`: Lift the tilt angle  of 3250963_3 by 4 degrees
- `C5`: Lift the tilt angle of 3272437_2 by 5 degrees
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3250963_3
- `C7`: Increase transmission power for 3250963_3
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3272437_2
- `C9`: Decrease transmission power for 3250963_3 **← 정답**
- `C10`: Adjust the azimuth of 3272437_2 by 15 degrees
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3250963_3
- `C12`: Add neighbor relationship between 3264014_4 and 3250963_3
- `C13`: Press down the tilt angle of 3272437_2 by 5 degrees
- `C14`: Press down the tilt angle  of 3250963_3 by 4 degrees **← 정답**
- `C15`: Increase A3 Offset threshold for 3272437_2
- `C16`: Insufficient data; more data is needed for judgment.
- `C17`: Decrease A3 Offset threshold for 3250963_3
- `C18`: Increase A3 Offset threshold for 3250963_3
- `C19`: Check test server and transmission issues
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3272437_2
- `C21`: Decrease transmission power for 3272437_2
- `C22`: Decrease A3 Offset threshold for 3272437_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.533 | MS1 | 121.4656610730 | 31.1446379168 | 63 | 504990 | -84.20 | 16.25 | 341.14 | 0.18 | 2.22 | 1580 |
| 2024-09-20 22:21:32.500 | MS1 | 121.4656660468 | 31.1446261809 | 63 | 504990 | -75.95 | 12.35 | 452.27 | 0.19 | 2.47 | 1568 |
| 2024-09-20 22:21:33.868 | MS1 | 121.4656638074 | 31.1446368237 | 63 | 504990 | -77.12 | 12.07 | 573.67 | 0.10 | 2.52 | 1596 |
| 2024-09-20 22:21:34.790 | MS1 | 121.4656751218 | 31.1446259544 | 63 | 504990 | -88.41 | 0.51 | 93.52 | 0.15 | 1.44 | 1565 |
| 2024-09-20 22:21:35.844 | MS1 | 121.4656723724 | 31.1446358642 | 63 | 504990 | -85.91 | 1.61 | 61.21 | 0.02 | 1.08 | 1595 |
| 2024-09-20 22:21:36.812 | MS1 | 121.4656693093 | 31.1446338467 | 63 | 504990 | -89.55 | 2.89 | 74.60 | 0.15 | 1.04 | 1584 |
| 2024-09-20 22:21:37.752 | MS1 | 121.4656696456 | 31.1446292687 | 63 | 504990 | -85.27 | 2.60 | 79.94 | 0.07 | 1.40 | 1577 |
| 2024-09-20 22:21:38.760 | MS1 | 121.4656732068 | 31.1446375784 | 63 | 504990 | -87.78 | 0.34 | 79.04 | 0.05 | 1.37 | 1569 |
| 2024-09-20 22:21:39.909 | MS1 | 121.4656737074 | 31.1446272953 | 63 | 504990 | -89.19 | 2.44 | 63.45 | 0.06 | 1.07 | 1582 |
| 2024-09-20 22:21:40.277 | MS1 | 121.4656740295 | 31.1446251127 | 63 | 504990 | -84.72 | 17.92 | 489.10 | 0.19 | 2.49 | 1582 |
| 2024-09-20 22:21:41.393 | MS1 | 121.4656722907 | 31.1446349951 | 63 | 504990 | -83.72 | 14.82 | 521.78 | 0.05 | 2.98 | 1584 |
| 2024-09-20 22:21:42.443 | MS1 | 121.4656761645 | 31.1446210387 | 63 | 504990 | -80.26 | 13.88 | 567.41 | 0.20 | 2.32 | 1580 |

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
| 3218205 | 1 | 121.4735176483 | 31.1445598103 | 264 | 12 | 5 | 42.3 | TDD | 377 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3250963 | 3 | 121.4658766190 | 31.1546342683 | 191 | 3 | 11 | 28.5 | TDD | 351 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3264014 | 4 | 121.4640562969 | 31.1526732801 | 290 | 10 | 5 | 32.3 | TDD | 407 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3272437 | 2 | 121.4718873493 | 31.1509836779 | 235 | 2 | 0 | 46.8 | TDD | 63 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |

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
| 2024-09-20 22:21:31.559 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.584 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.690 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.690 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3218205 | 1 | 18.4833 | 6.2848 | -117.5924 | 7.7576 | 90.3463 | 0.0193 | 0.0182 |
| 2024_09_20 22:00 | 3272437 | 2 | 18.4911 | 17.6973 | -108.1517 | 5.4255 | 146.2045 | 0.0084 | 0.0076 |
| 2024_09_20 22:00 | 3250963 | 3 | 10.3619 | 8.4998 | -115.3035 | 11.4211 | 103.4145 | 0.0089 | 0.0027 |
| 2024_09_20 22:00 | 3264014 | 4 | 15.9760 | 10.0017 | -114.6309 | 13.8282 | 134.4043 | 0.0111 | 0.0065 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417020_065FEF97 | 504990 | 63 | -87.5 | 504990 | 351 | -90.6 | 504990 | 407 | -91.1 | 504990 | 377 |
| MR_1774417020_367A20F0 | 504990 | 63 | -87.6 | 504990 | 351 | -89.5 | 504990 | 407 | -89.5 | 504990 | 377 |
| MR_1774417020_B40A6419 | 504990 | 63 | -88.8 | 504990 | 351 | -87.8 | 504990 | 407 | -90.7 | 504990 | 377 |
| MR_1774417020_4D831BB5 | 504990 | 63 | -88.3 | 504990 | 351 | -90.6 | 504990 | 407 | -88.9 | 504990 | 377 |
| MR_1774417020_E2550709 | 504990 | 63 | -87.2 | 504990 | 351 | -89.2 | 504990 | 407 | -88.5 | 504990 | 377 |
| MR_1774417020_36F087D1 | 504990 | 351 | -89.1 | 504990 | 63 | -88.5 | 504990 | 407 | -89.3 | 504990 | 377 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1558: `02e256dc-59d...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `02e256dc-59d0-4563-82de-5cc69dfd3442` |
| Tag | **single-answer** |
| 정답 | **C12** |
| C12 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1558] topology](images/train_1558.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3245620_1 by 10 degrees
- `C2`: Decrease transmission power for 3245620_1
- `C3`: Increase transmission power for 3245620_1
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3245620_1
- `C5`: Lift the tilt angle of 3278262_2 by 10 degrees
- `C6`: Adjust the azimuth of 3278262_2 by 50 degrees
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3278262_2
- `C8`: Decrease transmission power for 3278262_2
- `C9`: Decrease A3 Offset threshold for 3245620_1
- `C10`: Increase transmission power for 3278262_2
- `C11`: Add neighbor relationship between 3210426_4 and 3245620_1
- `C12`: Check test server and transmission issues **← 정답**
- `C13`: Press down the tilt angle of 3278262_2 by 10 degrees
- `C14`: Decrease A3 Offset threshold for 3278262_2
- `C15`: Increase A3 Offset threshold for 3245620_1
- `C16`: Lift the tilt angle  of 3245620_1 by 8 degrees
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3245620_1
- `C18`: Increase A3 Offset threshold for 3278262_2
- `C19`: Add neighbor relationship between 3278262_2 and 3245620_1
- `C20`: Press down the tilt angle  of 3245620_1 by 8 degrees
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3278262_2
- `C22`: Insufficient data; more data is needed for judgment.

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.661 | MS1 | 121.4656597196 | 31.1446246509 | 708 | 504990 | -87.82 | 15.79 | 340.23 | 0.10 | 2.25 | 1581 |
| 2024-09-20 22:21:32.232 | MS1 | 121.4656634644 | 31.1446231404 | 708 | 504990 | -89.65 | 16.42 | 580.59 | 0.14 | 2.43 | 1589 |
| 2024-09-20 22:21:33.557 | MS1 | 121.4656584895 | 31.1446265526 | 708 | 504990 | -89.34 | 12.79 | 579.12 | 0.19 | 2.55 | 1598 |
| 2024-09-20 22:21:34.525 | MS1 | 121.4656726193 | 31.1446275694 | 708 | 504990 | -91.88 | 12.90 | 108.25 | 0.04 | 2.88 | 319 |
| 2024-09-20 22:21:35.716 | MS1 | 121.4656754132 | 31.1446374753 | 708 | 504990 | -87.34 | 14.96 | 93.51 | 0.09 | 2.37 | 342 |
| 2024-09-20 22:21:36.413 | MS1 | 121.4656719554 | 31.1446379905 | 708 | 504990 | -91.89 | 13.59 | 102.95 | 0.00 | 2.78 | 454 |
| 2024-09-20 22:21:37.867 | MS1 | 121.4656580547 | 31.1446221031 | 708 | 504990 | -92.38 | 8.22 | 89.05 | 0.14 | 2.98 | 483 |
| 2024-09-20 22:21:38.236 | MS1 | 121.4656680030 | 31.1446325824 | 708 | 504990 | -91.67 | 7.03 | 93.25 | 0.14 | 2.26 | 440 |
| 2024-09-20 22:21:39.398 | MS1 | 121.4656684568 | 31.1446286364 | 708 | 504990 | -89.61 | 11.77 | 96.72 | 0.12 | 2.92 | 351 |
| 2024-09-20 22:21:40.317 | MS1 | 121.4656743577 | 31.1446325485 | 708 | 504990 | -93.68 | 8.56 | 457.35 | 0.12 | 2.57 | 1588 |
| 2024-09-20 22:21:41.450 | MS1 | 121.4656746174 | 31.1446331202 | 708 | 504990 | -93.88 | 12.97 | 341.18 | 0.03 | 2.76 | 1600 |
| 2024-09-20 22:21:42.999 | MS1 | 121.4656716672 | 31.1446246001 | 708 | 504990 | -92.93 | 11.93 | 561.59 | 0.07 | 2.58 | 1583 |

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
| 3210426 | 4 | 121.4708350707 | 31.1480293990 | 287 | 4 | 3 | 32.5 | TDD | 607 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3245620 | 1 | 121.4640616634 | 31.1531408798 | 161 | 7 | 9 | 23.8 | TDD | 610 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3278262 | 2 | 121.4735301067 | 31.1506215351 | 99 | 14 | 5 | 19.1 | TDD | 708 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3279375 | 3 | 121.4705942423 | 31.1468617058 | 13 | 13 | 10 | 44.5 | TDD | 652 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |

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
| 2024-09-20 22:21:31.328 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.351 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.483 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.483 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.198 | NREventA3 | measId:2;ServCellPCI:881;Se... |
| 2024-09-20 22:21:38.438 | NRHandoverAttempt | SourcePCI:881;SourceNR-ARFC... |
| 2024-09-20 22:21:38.478 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.491 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.595 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.595 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3245620 | 1 | 14.5939 | 14.4224 | -114.1545 | 19.4945 | 145.5839 | 0.0049 | 0.0013 |
| 2024_09_20 22:00 | 3278262 | 2 | 9.5475 | 18.0889 | -115.5409 | 15.8629 | 158.7881 | 0.0187 | 0.0126 |
| 2024_09_20 22:00 | 3279375 | 3 | 14.7650 | 9.0917 | -115.0808 | 5.2286 | 110.2889 | 0.0140 | 0.0023 |
| 2024_09_20 22:00 | 3210426 | 4 | 9.6051 | 17.9694 | -116.5841 | 19.1057 | 132.2803 | 0.0126 | 0.0078 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412612_DED57B72 | 504990 | 708 | -88.2 | 504990 | 610 | -88.1 | 504990 | 607 | -98.2 | 504990 | 652 |
| MR_1774412612_D4FA772C | 504990 | 708 | -87.0 | 504990 | 610 | -89.0 | 504990 | 607 | -101.5 | 504990 | 652 |
| MR_1774412612_51E1C626 | 504990 | 708 | -86.9 | 504990 | 610 | -91.1 | 504990 | 607 | -98.8 | 504990 | 652 |
| MR_1774412612_407631AC | 504990 | 708 | -85.6 | 504990 | 610 | -91.6 | 504990 | 607 | -99.8 | 504990 | 652 |
| MR_1774412612_7A43C05A | 504990 | 708 | -88.0 | 504990 | 610 | -88.0 | 504990 | 607 | -100.9 | 504990 | 652 |
| MR_1774412612_08F7C86D | 504990 | 708 | -88.1 | 504990 | 610 | -91.6 | 504990 | 607 | -101.0 | 504990 | 652 |
| MR_1774412612_DE697E00 | 504990 | 708 | -86.0 | 504990 | 610 | -89.5 | 504990 | 607 | -99.1 | 504990 | 652 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1559: `51fc4268-828...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `51fc4268-8281-40cf-ac7d-01738e5b53b1` |
| Tag | **multiple-answer** |
| 정답 | **C5|C7|C12|C17** |
| C5 의미 | Increase A3 Offset threshold for 3248053_1 |
| C7 의미 | Decrease transmission power for 3248053_1 |
| C12 의미 | Increase A3 Offset threshold for 3216953_3 |
| C17 의미 | Press down the tilt angle  of 3248053_1 by 5 degrees |
| 패턴 분류 | **P2 Ping-pong** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1559] topology](images/train_1559.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 5 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 5개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3216953_3
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3216953_3
- `C3`: Lift the tilt angle of 3216953_3 by 6 degrees
- `C4`: Add neighbor relationship between 3239722_5 and 3248053_1
- `C5`: Increase A3 Offset threshold for 3248053_1 **← 정답**
- `C6`: Decrease transmission power for 3216953_3
- `C7`: Decrease transmission power for 3248053_1 **← 정답**
- `C8`: Check test server and transmission issues
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3248053_1
- `C10`: Adjust the azimuth of 3216953_3 by 29 degrees
- `C11`: Decrease A3 Offset threshold for 3216953_3
- `C12`: Increase A3 Offset threshold for 3216953_3 **← 정답**
- `C13`: Add neighbor relationship between 3216953_3 and 3248053_1
- `C14`: Adjust the azimuth of 3248053_1 by 18 degrees
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3248053_1
- `C16`: Increase transmission power for 3248053_1
- `C17`: Press down the tilt angle  of 3248053_1 by 5 degrees **← 정답**
- `C18`: Decrease A3 Offset threshold for 3248053_1
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3216953_3
- `C20`: Press down the tilt angle of 3216953_3 by 6 degrees
- `C21`: Insufficient data; more data is needed for judgment.
- `C22`: Lift the tilt angle  of 3248053_1 by 5 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.233 | MS1 | 121.4656722912 | 31.1446288039 | 809 | 504990 | -77.06 | 17.80 | 338.77 | 0.19 | 2.17 | 1580 |
| 2024-09-20 22:21:32.953 | MS1 | 121.4656627766 | 31.1446285055 | 809 | 504990 | -75.33 | 15.69 | 485.10 | 0.13 | 2.52 | 1567 |
| 2024-09-20 22:21:33.617 | MS1 | 121.4656623731 | 31.1446231854 | 809 | 504990 | -84.35 | 16.68 | 353.61 | 0.12 | 2.11 | 1592 |
| 2024-09-20 22:21:34.314 | MS1 | 121.4656778249 | 31.1446183241 | 44 | 504990 | -87.72 | 3.39 | 57.40 | 0.05 | 1.37 | 1570 |
| 2024-09-20 22:21:35.930 | MS1 | 121.4656643563 | 31.1446293553 | 44 | 504990 | -88.39 | 3.67 | 50.72 | 0.05 | 1.43 | 1585 |
| 2024-09-20 22:21:36.130 | MS1 | 121.4656609495 | 31.1446246045 | 809 | 504990 | -80.29 | 3.91 | 70.53 | 0.04 | 1.40 | 1592 |
| 2024-09-20 22:21:37.658 | MS1 | 121.4656644071 | 31.1446254782 | 809 | 504990 | -86.29 | 4.96 | 24.98 | 0.01 | 1.39 | 1562 |
| 2024-09-20 22:21:38.950 | MS1 | 121.4656743550 | 31.1446261546 | 44 | 504990 | -87.48 | 2.98 | 24.09 | 0.18 | 1.21 | 1563 |
| 2024-09-20 22:21:39.392 | MS1 | 121.4656754331 | 31.1446316281 | 44 | 504990 | -84.69 | 2.64 | 86.22 | 0.04 | 1.14 | 1579 |
| 2024-09-20 22:21:40.383 | MS1 | 121.4656778909 | 31.1446246429 | 44 | 504990 | -84.45 | 12.07 | 397.85 | 0.06 | 2.86 | 1590 |
| 2024-09-20 22:21:41.358 | MS1 | 121.4656601678 | 31.1446327737 | 44 | 504990 | -82.30 | 13.90 | 441.77 | 0.06 | 2.49 | 1575 |
| 2024-09-20 22:21:42.246 | MS1 | 121.4656757460 | 31.1446214259 | 44 | 504990 | -82.37 | 13.39 | 509.85 | 0.10 | 2.42 | 1587 |

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
| 3216953 | 3 | 121.4647633789 | 31.1519093240 | 203 | 3 | 9 | 35.7 | TDD | 809 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3239722 | 5 | 121.4758814424 | 31.1555435881 | 323 | 4 | 3 | 32.8 | TDD | 914 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3248053 | 1 | 121.4733787439 | 31.1503079961 | 247 | 4 | 3 | 23.9 | TDD | 640 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3266992 | 2 | 121.4752759505 | 31.1484592217 | 196 | 3 | 10 | 34.6 | TDD | 420 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3271980 | 4 | 121.4686895195 | 31.1452782626 | 289 | 1 | 4 | 48.8 | TDD | 44 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:31.341 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.362 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.480 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.480 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.208 | NREventA3 | measId:2;ServCellPCI:941;Se... |
| 2024-09-20 22:21:34.448 | NRHandoverAttempt | SourcePCI:941;SourceNR-ARFC... |
| 2024-09-20 22:21:34.483 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:34.498 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:34.604 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:34.604 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:36.208 | NREventA3 | measId:2;ServCellPCI:72;Ser... |
| 2024-09-20 22:21:36.448 | NRHandoverAttempt | SourcePCI:72;SourceNR-ARFCN... |
| 2024-09-20 22:21:36.491 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:36.506 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:36.626 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.626 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.208 | NREventA3 | measId:2;ServCellPCI:941;Se... |
| 2024-09-20 22:21:38.448 | NRHandoverAttempt | SourcePCI:941;SourceNR-ARFC... |
| 2024-09-20 22:21:38.495 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.507 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.625 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.625 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3248053 | 1 | 9.0851 | 6.7769 | -116.3555 | 9.2716 | 117.4522 | 0.0098 | 0.0156 |
| 2024_09_20 22:00 | 3266992 | 2 | 8.5719 | 11.0845 | -115.2635 | 8.9075 | 155.4792 | 0.0111 | 0.0091 |
| 2024_09_20 22:00 | 3216953 | 3 | 17.8664 | 12.6743 | -115.3369 | 7.9671 | 140.8747 | 0.0006 | 0.0142 |
| 2024_09_20 22:00 | 3271980 | 4 | 10.7776 | 7.3771 | -117.1837 | 5.1049 | 120.0307 | 0.0159 | 0.0082 |
| 2024_09_20 22:00 | 3239722 | 5 | 14.6375 | 14.6056 | -117.1602 | 7.6694 | 141.4541 | 0.0149 | 0.0006 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416582_37F10BE3 | 504990 | 44 | -89.2 | 504990 | 809 | -87.6 | 504990 | 640 | -88.0 | 504990 | 914 |
| MR_1774416582_5E5BC15C | 504990 | 809 | -86.0 | 504990 | 44 | -87.8 | 504990 | 640 | -89.9 | 504990 | 914 |
| MR_1774416582_619CCD42 | 504990 | 44 | -86.9 | 504990 | 809 | -85.1 | 504990 | 640 | -86.4 | 504990 | 914 |
| MR_1774416582_1FAEE1B4 | 504990 | 809 | -87.7 | 504990 | 44 | -86.5 | 504990 | 640 | -86.4 | 504990 | 914 |
| MR_1774416582_888CA6EE | 504990 | 44 | -89.0 | 504990 | 809 | -87.2 | 504990 | 640 | -88.3 | 504990 | 914 |

> *... 2개 열 생략 (전체 14열)*

---
