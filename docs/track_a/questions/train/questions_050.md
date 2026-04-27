# Track A 문제 분석 — train[490]~train[499]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[490] ~ train[499] (10개)

## 목차

1. [문제 490: `dcb9fe1c-a25...`](#490) — single-answer, 정답: C6
2. [문제 491: `47fe8e2a-800...`](#491) — single-answer, 정답: C12
3. [문제 492: `249bbb13-5db...`](#492) — single-answer, 정답: C16
4. [문제 493: `7295455d-8d0...`](#493) — single-answer, 정답: C8
5. [문제 494: `6d45a063-95e...`](#494) — multiple-answer, 정답: C3|C11
6. [문제 495: `06740329-998...`](#495) — single-answer, 정답: C20
7. [문제 496: `fc315a50-900...`](#496) — single-answer, 정답: C12
8. [문제 497: `f1faae2a-ca5...`](#497) — single-answer, 정답: C10
9. [문제 498: `e05914bb-e6c...`](#498) — multiple-answer, 정답: C2|C4|C5|C15
10. [문제 499: `5ab417b9-70e...`](#499) — single-answer, 정답: C12

---

### 문제 490: `dcb9fe1c-a25...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `dcb9fe1c-a259-4cca-983d-ee60403c53d5` |
| Tag | **single-answer** |
| 정답 | **C6** |
| C6 의미 | Decrease A3 Offset threshold for 3227812_1 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[490] topology](images/train_0490.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3217146_4
- `C2`: Press down the tilt angle of 3227812_1 by 5 degrees
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3227812_1
- `C4`: Increase transmission power for 3227812_1
- `C5`: Decrease A3 Offset threshold for 3217146_4
- `C6`: Decrease A3 Offset threshold for 3227812_1 **← 정답**
- `C7`: Press down the tilt angle  of 3217146_4 by 5 degrees
- `C8`: Increase transmission power for 3217146_4
- `C9`: Adjust the azimuth of 3227812_1 by 2 degrees
- `C10`: Decrease transmission power for 3227812_1
- `C11`: Lift the tilt angle  of 3217146_4 by 5 degrees
- `C12`: Insufficient data; more data is needed for judgment.
- `C13`: Add neighbor relationship between 3227812_1 and 3217146_4
- `C14`: Increase A3 Offset threshold for 3227812_1
- `C15`: Decrease transmission power for 3217146_4
- `C16`: Lift the tilt angle of 3227812_1 by 5 degrees
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3217146_4
- `C18`: Adjust the azimuth of 3217146_4 by 19 degrees
- `C19`: Check test server and transmission issues
- `C20`: Increase A3 Offset threshold for 3217146_4
- `C21`: Add neighbor relationship between 3215934_3 and 3217146_4
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3227812_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.379 | MS1 | 121.4656667062 | 31.1446189407 | 793 | 504990 | -78.30 | 12.31 | 528.46 | 0.10 | 2.85 | 1582 |
| 2024-09-20 22:21:32.277 | MS1 | 121.4656592216 | 31.1446212382 | 793 | 504990 | -75.42 | 14.92 | 402.67 | 0.02 | 2.21 | 1595 |
| 2024-09-20 22:21:33.984 | MS1 | 121.4656629375 | 31.1446262785 | 793 | 504990 | -79.36 | 17.08 | 321.79 | 0.06 | 2.64 | 1568 |
| 2024-09-20 22:21:34.234 | MS1 | 121.4656749868 | 31.1446364952 | 793 | 504990 | -91.13 | -3.06 | 39.84 | 0.03 | 1.25 | 1560 |
| 2024-09-20 22:21:35.850 | MS1 | 121.4656610421 | 31.1446363466 | 793 | 504990 | -89.11 | -1.45 | 40.26 | 0.07 | 1.39 | 1561 |
| 2024-09-20 22:21:36.228 | MS1 | 121.4656728288 | 31.1446228545 | 793 | 504990 | -91.35 | -0.82 | 35.37 | 0.01 | 1.07 | 1596 |
| 2024-09-20 22:21:37.787 | MS1 | 121.4656680091 | 31.1446273138 | 793 | 504990 | -83.06 | -2.42 | 30.51 | 0.03 | 1.30 | 1576 |
| 2024-09-20 22:21:38.531 | MS1 | 121.4656659706 | 31.1446301376 | 793 | 504990 | -92.02 | -2.10 | 26.03 | 0.19 | 1.17 | 1571 |
| 2024-09-20 22:21:39.725 | MS1 | 121.4656664309 | 31.1446276150 | 467 | 504990 | -84.36 | 15.02 | 273.74 | 0.17 | 1.49 | 1599 |
| 2024-09-20 22:21:40.824 | MS1 | 121.4656697998 | 31.1446256921 | 467 | 504990 | -83.88 | 17.45 | 391.02 | 0.09 | 2.45 | 1565 |
| 2024-09-20 22:21:41.825 | MS1 | 121.4656665230 | 31.1446211650 | 467 | 504990 | -75.66 | 12.96 | 400.29 | 0.02 | 2.17 | 1575 |
| 2024-09-20 22:21:42.711 | MS1 | 121.4656673306 | 31.1446309079 | 467 | 504990 | -76.89 | 16.91 | 419.76 | 0.11 | 2.41 | 1572 |

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
| 3215934 | 3 | 121.4715582032 | 31.1499180881 | 150 | 11 | 11 | 18.9 | TDD | 371 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3217146 | 4 | 121.4693304541 | 31.1536714009 | 180 | 2 | 2 | 46.8 | TDD | 467 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3227812 | 1 | 121.4695064087 | 31.1489315811 | 219 | 2 | 7 | 27.0 | TDD | 793 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3232598 | 2 | 121.4667217312 | 31.1486681358 | 292 | 11 | 12 | 15.9 | TDD | 266 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |

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
| 2024-09-20 22:21:31.574 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.592 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.706 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.706 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.378 | NREventA3 | measId:2;ServCellPCI:384;Se... |
| 2024-09-20 22:21:38.618 | NRHandoverAttempt | SourcePCI:384;SourceNR-ARFC... |
| 2024-09-20 22:21:38.667 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.677 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.786 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.786 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3227812 | 1 | 19.7510 | 14.6898 | -114.3830 | 8.7461 | 97.9682 | 0.0040 | 0.1171 |
| 2024_09_20 22:00 | 3232598 | 2 | 16.2019 | 15.5253 | -114.3730 | 5.0368 | 103.8015 | 0.0155 | 0.0007 |
| 2024_09_20 22:00 | 3215934 | 3 | 5.8128 | 7.6763 | -117.6571 | 12.3277 | 144.8151 | 0.0180 | 0.0044 |
| 2024_09_20 22:00 | 3217146 | 4 | 13.9522 | 10.3569 | -117.4338 | 5.8884 | 192.3442 | 0.0093 | 0.0125 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413276_E0CD8658 | 504990 | 793 | -89.6 | 504990 | 467 | -86.4 | 504990 | 371 | -91.0 | 504990 | 266 |
| MR_1774413276_93722DFA | 504990 | 467 | -85.2 | 504990 | 793 | -90.4 | 504990 | 371 | -91.1 | 504990 | 266 |
| MR_1774413276_3B8FB903 | 504990 | 467 | -88.1 | 504990 | 793 | -90.6 | 504990 | 371 | -89.4 | 504990 | 266 |
| MR_1774413276_21D85829 | 504990 | 793 | -90.7 | 504990 | 467 | -86.4 | 504990 | 371 | -89.2 | 504990 | 266 |
| MR_1774413276_62FAE72D | 504990 | 467 | -86.4 | 504990 | 793 | -92.6 | 504990 | 371 | -91.1 | 504990 | 266 |
| MR_1774413276_33A092A3 | 504990 | 467 | -86.7 | 504990 | 793 | -91.7 | 504990 | 371 | -89.8 | 504990 | 266 |
| MR_1774413276_A75F60CB | 504990 | 467 | -85.4 | 504990 | 793 | -89.8 | 504990 | 371 | -89.9 | 504990 | 266 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 491: `47fe8e2a-800...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `47fe8e2a-800b-4285-8704-4427d5a6f600` |
| Tag | **single-answer** |
| 정답 | **C12** |
| C12 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3256263_3 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[491] topology](images/train_0491.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3256263_3
- `C2`: Increase A3 Offset threshold for 3242903_2
- `C3`: Decrease transmission power for 3256263_3
- `C4`: Lift the tilt angle  of 3242903_2 by 10 degrees
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3242903_2
- `C6`: Decrease transmission power for 3242903_2
- `C7`: Press down the tilt angle  of 3242903_2 by 10 degrees
- `C8`: Decrease A3 Offset threshold for 3242903_2
- `C9`: Add neighbor relationship between 3242219_1 and 3242903_2
- `C10`: Decrease A3 Offset threshold for 3256263_3
- `C11`: Adjust the azimuth of 3256263_3 by 2 degrees
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3256263_3 **← 정답**
- `C13`: Adjust the azimuth of 3242903_2 by 50 degrees
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Check test server and transmission issues
- `C16`: Lift the tilt angle of 3256263_3 by 4 degrees
- `C17`: Press down the tilt angle of 3256263_3 by 4 degrees
- `C18`: Increase transmission power for 3256263_3
- `C19`: Add neighbor relationship between 3256263_3 and 3242903_2
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3242903_2
- `C21`: Increase A3 Offset threshold for 3256263_3
- `C22`: Increase transmission power for 3242903_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.720 | MS1 | 121.4656646731 | 31.1446369697 | 878 | 504990 | -89.28 | 16.68 | 491.77 | 0.18 | 2.74 | 1584 |
| 2024-09-20 22:21:32.499 | MS1 | 121.4656700188 | 31.1446330946 | 878 | 504990 | -85.01 | 15.15 | 425.02 | 0.12 | 2.36 | 1562 |
| 2024-09-20 22:21:33.388 | MS1 | 121.4656586380 | 31.1446250197 | 878 | 504990 | -88.68 | 15.79 | 505.29 | 0.17 | 2.64 | 1568 |
| 2024-09-20 22:21:34.157 | MS1 | 121.4656685012 | 31.1446257636 | 878 | 504990 | -87.43 | 17.60 | 98.53 | 0.64 | 2.28 | 679 |
| 2024-09-20 22:21:35.750 | MS1 | 121.4656652103 | 31.1446257871 | 878 | 504990 | -86.70 | 16.29 | 73.55 | 0.64 | 2.63 | 631 |
| 2024-09-20 22:21:36.817 | MS1 | 121.4656703578 | 31.1446285433 | 878 | 504990 | -89.93 | 15.65 | 56.15 | 0.57 | 2.55 | 694 |
| 2024-09-20 22:21:37.147 | MS1 | 121.4656582785 | 31.1446204738 | 878 | 504990 | -92.45 | 7.10 | 83.93 | 0.62 | 2.21 | 537 |
| 2024-09-20 22:21:38.946 | MS1 | 121.4656758949 | 31.1446320557 | 878 | 504990 | -91.98 | 8.83 | 87.04 | 0.68 | 2.30 | 697 |
| 2024-09-20 22:21:39.139 | MS1 | 121.4656646126 | 31.1446335796 | 878 | 504990 | -92.08 | 9.36 | 52.09 | 0.61 | 2.61 | 567 |
| 2024-09-20 22:21:40.185 | MS1 | 121.4656676643 | 31.1446351803 | 878 | 504990 | -89.50 | 12.09 | 426.77 | 0.17 | 2.71 | 1575 |
| 2024-09-20 22:21:41.365 | MS1 | 121.4656733497 | 31.1446199756 | 878 | 504990 | -91.11 | 8.38 | 542.28 | 0.18 | 2.56 | 1583 |
| 2024-09-20 22:21:42.872 | MS1 | 121.4656738694 | 31.1446216690 | 878 | 504990 | -90.36 | 11.68 | 587.97 | 0.14 | 2.21 | 1567 |

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
| 3242219 | 1 | 121.4713685850 | 31.1482508675 | 37 | 10 | 12 | 25.5 | TDD | 56 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3242903 | 2 | 121.4664535955 | 31.1453424845 | 53 | 0 | 4 | 26.0 | TDD | 841 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3250013 | 4 | 121.4719469158 | 31.1522846214 | 135 | 4 | 4 | 32.0 | TDD | 390 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3256263 | 3 | 121.4665482427 | 31.1540234725 | 187 | 2 | 9 | 44.2 | TDD | 878 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |

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
| 2024-09-20 22:21:31.114 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.132 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.249 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.249 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.012 | NREventA3 | measId:2;ServCellPCI:211;Se... |
| 2024-09-20 22:21:38.252 | NRHandoverAttempt | SourcePCI:211;SourceNR-ARFC... |
| 2024-09-20 22:21:38.301 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.315 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.424 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.424 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3242219 | 1 | 8.9033 | 8.9971 | -117.7965 | 5.1081 | 131.8684 | 0.0113 | 0.0127 |
| 2024_09_20 22:00 | 3242903 | 2 | 12.3380 | 8.6066 | -116.1170 | 13.8136 | 176.5131 | 0.0146 | 0.0174 |
| 2024_09_20 22:00 | 3256263 | 3 | 6.3214 | 14.9273 | -116.0758 | 6.8708 | 134.0364 | 0.0134 | 0.0044 |
| 2024_09_20 22:00 | 3250013 | 4 | 6.5703 | 5.2561 | -116.7623 | 6.3625 | 100.1724 | 0.0033 | 0.0163 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414110_BD1DE501 | 504990 | 878 | -85.6 | 504990 | 841 | -88.1 | 504990 | 56 | -100.0 | 504990 | 390 |
| MR_1774414110_871EDD29 | 504990 | 878 | -87.5 | 504990 | 841 | -88.3 | 504990 | 56 | -96.8 | 504990 | 390 |
| MR_1774414110_BC880582 | 504990 | 878 | -88.2 | 504990 | 841 | -88.6 | 504990 | 56 | -98.4 | 504990 | 390 |
| MR_1774414110_1A86BE4C | 504990 | 878 | -89.1 | 504990 | 841 | -87.2 | 504990 | 56 | -99.7 | 504990 | 390 |
| MR_1774414110_374E67DA | 504990 | 878 | -86.2 | 504990 | 841 | -88.6 | 504990 | 56 | -97.1 | 504990 | 390 |
| MR_1774414110_910FD0E0 | 504990 | 878 | -87.2 | 504990 | 841 | -87.6 | 504990 | 56 | -96.3 | 504990 | 390 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 492: `249bbb13-5db...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `249bbb13-5db4-4d39-8171-0632dd539697` |
| Tag | **single-answer** |
| 정답 | **C16** |
| C16 의미 | Add neighbor relationship between 3236069_1 and 3239916_3 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[492] topology](images/train_0492.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3236069_1
- `C2`: Increase transmission power for 3239916_3
- `C3`: Decrease A3 Offset threshold for 3239916_3
- `C4`: Increase A3 Offset threshold for 3239916_3
- `C5`: Increase transmission power for 3236069_1
- `C6`: Check test server and transmission issues
- `C7`: Decrease A3 Offset threshold for 3236069_1
- `C8`: Lift the tilt angle of 3236069_1 by 4 degrees
- `C9`: Add neighbor relationship between 3220887_4 and 3239916_3
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3239916_3
- `C11`: Adjust the azimuth of 3236069_1 by 50 degrees
- `C12`: Press down the tilt angle of 3236069_1 by 4 degrees
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3239916_3
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3236069_1
- `C15`: Press down the tilt angle  of 3239916_3 by 3 degrees
- `C16`: Add neighbor relationship between 3236069_1 and 3239916_3 **← 정답**
- `C17`: Adjust the azimuth of 3239916_3 by 22 degrees
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3236069_1
- `C19`: Insufficient data; more data is needed for judgment.
- `C20`: Decrease transmission power for 3239916_3
- `C21`: Decrease transmission power for 3236069_1
- `C22`: Lift the tilt angle  of 3239916_3 by 3 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.209 | MS1 | 121.4656756681 | 31.1446362854 | 304 | 504990 | -77.64 | 15.76 | 453.47 | 0.19 | 2.16 | 1581 |
| 2024-09-20 22:21:32.991 | MS1 | 121.4656720631 | 31.1446292516 | 304 | 504990 | -77.58 | 17.02 | 455.73 | 0.13 | 2.50 | 1594 |
| 2024-09-20 22:21:33.912 | MS1 | 121.4656755169 | 31.1446188945 | 304 | 504990 | -79.63 | 13.14 | 533.95 | 0.02 | 2.31 | 1585 |
| 2024-09-20 22:21:34.187 | MS1 | 121.4656757469 | 31.1446296239 | 304 | 504990 | -94.34 | -3.23 | 38.38 | 0.11 | 1.10 | 1595 |
| 2024-09-20 22:21:35.973 | MS1 | 121.4656662186 | 31.1446359869 | 304 | 504990 | -86.74 | -3.18 | 66.18 | 0.17 | 1.06 | 1563 |
| 2024-09-20 22:21:36.335 | MS1 | 121.4656670192 | 31.1446213769 | 304 | 504990 | -91.78 | -2.10 | 50.03 | 0.08 | 1.18 | 1570 |
| 2024-09-20 22:21:37.551 | MS1 | 121.4656699515 | 31.1446307243 | 304 | 504990 | -91.76 | -1.47 | 57.00 | 0.12 | 1.01 | 1587 |
| 2024-09-20 22:21:38.367 | MS1 | 121.4656648202 | 31.1446191405 | 304 | 504990 | -82.96 | 12.29 | 337.88 | 0.16 | 1.43 | 1589 |
| 2024-09-20 22:21:39.727 | MS1 | 121.4656582818 | 31.1446273817 | 304 | 504990 | -75.40 | 12.63 | 538.79 | 0.08 | 1.11 | 1565 |
| 2024-09-20 22:21:40.852 | MS1 | 121.4656667310 | 31.1446261985 | 304 | 504990 | -79.30 | 16.23 | 358.52 | 0.20 | 2.83 | 1590 |
| 2024-09-20 22:21:41.108 | MS1 | 121.4656627170 | 31.1446353530 | 304 | 504990 | -84.02 | 15.11 | 599.42 | 0.13 | 2.39 | 1587 |
| 2024-09-20 22:21:42.380 | MS1 | 121.4656659541 | 31.1446226689 | 304 | 504990 | -81.52 | 17.82 | 358.58 | 0.11 | 2.01 | 1583 |

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
| 3220887 | 4 | 121.4709022579 | 31.1534296031 | 75 | 14 | 2 | 37.7 | TDD | 111 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3236069 | 1 | 121.4683868280 | 31.1534128058 | 121 | 2 | 9 | 41.0 | TDD | 304 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3239916 | 3 | 121.4653339544 | 31.1514357609 | 200 | 0 | 12 | 43.9 | TDD | 84 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3256438 | 2 | 121.4752139345 | 31.1552475207 | 212 | 1 | 4 | 37.3 | TDD | 800 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |

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
| 2024-09-20 22:21:30.983 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.998 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.107 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.107 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.873 | NREventA3 | measId:2;ServCellPCI:37;Ser... |
| 2024-09-20 22:21:35.873 | NREventA3 | measId:2;ServCellPCI:37;Ser... |
| 2024-09-20 22:21:36.873 | NREventA3 | measId:2;ServCellPCI:37;Ser... |
| 2024-09-20 22:21:39.373 | NRRRCReestablishAttempt | PCI:37 |
| 2024-09-20 22:21:39.390 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.403 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:39.534 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.534 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3236069 | 1 | 12.7812 | 14.0444 | -117.8517 | 9.4648 | 155.8350 | 0.0115 | 0.1395 |
| 2024_09_20 22:00 | 3256438 | 2 | 7.5733 | 5.5183 | -117.3128 | 18.7169 | 190.6327 | 0.0151 | 0.0151 |
| 2024_09_20 22:00 | 3239916 | 3 | 11.6579 | 11.6821 | -116.7281 | 15.2581 | 191.3229 | 0.0041 | 0.0056 |
| 2024_09_20 22:00 | 3220887 | 4 | 15.6534 | 14.3013 | -117.8793 | 15.3834 | 152.1055 | 0.0162 | 0.0075 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417051_489ACF3F | 504990 | 304 | -94.7 | 504990 | 84 | -88.9 | 504990 | 111 | -94.0 | 504990 | 800 |
| MR_1774417051_5D94E02A | 504990 | 304 | -93.7 | 504990 | 84 | -87.8 | 504990 | 111 | -94.6 | 504990 | 800 |
| MR_1774417051_8D2AC7F6 | 504990 | 84 | -88.9 | 504990 | 304 | -95.5 | 504990 | 111 | -95.2 | 504990 | 800 |
| MR_1774417051_0C93B240 | 504990 | 304 | -95.6 | 504990 | 84 | -90.9 | 504990 | 111 | -95.2 | 504990 | 800 |
| MR_1774417051_84D73357 | 504990 | 304 | -93.5 | 504990 | 84 | -87.0 | 504990 | 111 | -94.6 | 504990 | 800 |
| MR_1774417051_1042BE44 | 504990 | 304 | -93.3 | 504990 | 84 | -87.5 | 504990 | 111 | -92.7 | 504990 | 800 |
| MR_1774417051_0BBF21D6 | 504990 | 304 | -93.0 | 504990 | 84 | -86.9 | 504990 | 111 | -93.3 | 504990 | 800 |
| MR_1774417051_6BEF175B | 504990 | 304 | -93.4 | 504990 | 84 | -88.4 | 504990 | 111 | -93.4 | 504990 | 800 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 493: `7295455d-8d0...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `7295455d-8d04-46af-ba3d-f4cd371bf2e8` |
| Tag | **single-answer** |
| 정답 | **C8** |
| C8 의미 | Add neighbor relationship between 3242721_3 and 3245781_1 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[493] topology](images/train_0493.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3242721_3
- `C2`: Press down the tilt angle  of 3245781_1 by 5 degrees
- `C3`: Adjust the azimuth of 3242721_3 by 50 degrees
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3245781_1
- `C5`: Lift the tilt angle of 3242721_3 by 10 degrees
- `C6`: Adjust the azimuth of 3245781_1 by 39 degrees
- `C7`: Increase A3 Offset threshold for 3242721_3
- `C8`: Add neighbor relationship between 3242721_3 and 3245781_1 **← 정답**
- `C9`: Decrease A3 Offset threshold for 3242721_3
- `C10`: Increase A3 Offset threshold for 3245781_1
- `C11`: Check test server and transmission issues
- `C12`: Insufficient data; more data is needed for judgment.
- `C13`: Add neighbor relationship between 3235314_2 and 3245781_1
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3245781_1
- `C15`: Decrease transmission power for 3242721_3
- `C16`: Increase transmission power for 3245781_1
- `C17`: Decrease A3 Offset threshold for 3245781_1
- `C18`: Decrease transmission power for 3245781_1
- `C19`: Press down the tilt angle of 3242721_3 by 10 degrees
- `C20`: Lift the tilt angle  of 3245781_1 by 5 degrees
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3242721_3
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3242721_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.689 | MS1 | 121.4656778255 | 31.1446208513 | 866 | 504990 | -84.58 | 17.04 | 591.32 | 0.04 | 2.89 | 1564 |
| 2024-09-20 22:21:32.356 | MS1 | 121.4656603168 | 31.1446322760 | 866 | 504990 | -82.41 | 12.74 | 476.87 | 0.09 | 2.45 | 1576 |
| 2024-09-20 22:21:33.989 | MS1 | 121.4656705710 | 31.1446361050 | 866 | 504990 | -82.17 | 12.23 | 457.80 | 0.10 | 2.10 | 1564 |
| 2024-09-20 22:21:34.498 | MS1 | 121.4656622028 | 31.1446201101 | 866 | 504990 | -86.58 | -1.59 | 47.86 | 0.09 | 1.20 | 1578 |
| 2024-09-20 22:21:35.745 | MS1 | 121.4656677677 | 31.1446358299 | 866 | 504990 | -93.05 | -2.95 | 45.37 | 0.17 | 1.14 | 1579 |
| 2024-09-20 22:21:36.795 | MS1 | 121.4656767578 | 31.1446228107 | 866 | 504990 | -86.81 | -1.46 | 32.66 | 0.13 | 1.45 | 1567 |
| 2024-09-20 22:21:37.971 | MS1 | 121.4656753936 | 31.1446319573 | 866 | 504990 | -88.33 | -3.76 | 48.11 | 0.19 | 1.15 | 1571 |
| 2024-09-20 22:21:38.703 | MS1 | 121.4656735704 | 31.1446235469 | 866 | 504990 | -77.43 | 14.20 | 387.66 | 0.04 | 1.31 | 1578 |
| 2024-09-20 22:21:39.130 | MS1 | 121.4656696319 | 31.1446231879 | 866 | 504990 | -78.93 | 12.62 | 483.36 | 0.14 | 1.38 | 1598 |
| 2024-09-20 22:21:40.454 | MS1 | 121.4656630785 | 31.1446344902 | 866 | 504990 | -77.41 | 16.81 | 316.85 | 0.02 | 2.22 | 1570 |
| 2024-09-20 22:21:41.531 | MS1 | 121.4656586219 | 31.1446290268 | 866 | 504990 | -81.47 | 13.34 | 414.56 | 0.14 | 2.30 | 1598 |
| 2024-09-20 22:21:42.975 | MS1 | 121.4656582918 | 31.1446199945 | 866 | 504990 | -83.33 | 16.17 | 548.64 | 0.10 | 2.89 | 1560 |

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
| 3235314 | 2 | 121.4650911759 | 31.1516521884 | 82 | 13 | 1 | 40.3 | TDD | 193 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3242721 | 3 | 121.4680685378 | 31.1481607608 | 356 | 10 | 2 | 44.9 | TDD | 866 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3245781 | 1 | 121.4656397670 | 31.1545534870 | 141 | 4 | 1 | 27.9 | TDD | 152 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3247681 | 4 | 121.4707301847 | 31.1496217761 | 206 | 10 | 5 | 15.8 | TDD | 727 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

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
| 2024-09-20 22:21:31.639 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.661 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.769 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.769 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.456 | NREventA3 | measId:2;ServCellPCI:866;Se... |
| 2024-09-20 22:21:36.456 | NREventA3 | measId:2;ServCellPCI:866;Se... |
| 2024-09-20 22:21:37.456 | NREventA3 | measId:2;ServCellPCI:866;Se... |
| 2024-09-20 22:21:39.956 | NRRRCReestablishAttempt | PCI:866 |
| 2024-09-20 22:21:39.966 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.980 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:40.112 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:40.112 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3245781 | 1 | 12.8430 | 11.8603 | -117.8471 | 19.0078 | 116.0340 | 0.0191 | 0.0125 |
| 2024_09_20 22:00 | 3235314 | 2 | 7.0954 | 19.8591 | -114.8283 | 14.3566 | 125.8046 | 0.0105 | 0.0167 |
| 2024_09_20 22:00 | 3242721 | 3 | 12.8198 | 11.6712 | -116.9063 | 17.9466 | 108.6569 | 0.0109 | 0.1019 |
| 2024_09_20 22:00 | 3247681 | 4 | 5.0347 | 7.5663 | -115.4735 | 12.7344 | 151.2104 | 0.0071 | 0.0002 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414236_3E1396C4 | 504990 | 866 | -87.4 | 504990 | 152 | -80.1 | 504990 | 193 | -90.4 | 504990 | 727 |
| MR_1774414236_3E614D43 | 504990 | 152 | -80.3 | 504990 | 866 | -84.6 | 504990 | 193 | -88.1 | 504990 | 727 |
| MR_1774414236_94B172BA | 504990 | 866 | -88.1 | 504990 | 152 | -82.2 | 504990 | 193 | -86.9 | 504990 | 727 |
| MR_1774414236_39FC99E0 | 504990 | 866 | -85.0 | 504990 | 152 | -82.0 | 504990 | 193 | -89.5 | 504990 | 727 |
| MR_1774414236_B0005E78 | 504990 | 866 | -87.7 | 504990 | 152 | -79.6 | 504990 | 193 | -88.5 | 504990 | 727 |
| MR_1774414236_286CA2D5 | 504990 | 866 | -86.2 | 504990 | 152 | -81.9 | 504990 | 193 | -88.5 | 504990 | 727 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 494: `6d45a063-95e...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `6d45a063-95ea-4dda-a22c-d2bbcb9b0b25` |
| Tag | **multiple-answer** |
| 정답 | **C3|C11** |
| C3 의미 | Adjust the azimuth of 3267899_4 by 50 degrees |
| C11 의미 | Increase transmission power for 3267899_4 |
| 패턴 분류 | **P4 Coverage (azimuth)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[494] topology](images/train_0494.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle  of 3258120_3 by 1 degrees
- `C2`: Add neighbor relationship between 3267899_4 and 3258120_3
- `C3`: Adjust the azimuth of 3267899_4 by 50 degrees **← 정답**
- `C4`: Decrease A3 Offset threshold for 3258120_3
- `C5`: Decrease A3 Offset threshold for 3267899_4
- `C6`: Increase transmission power for 3258120_3
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3267899_4
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3258120_3
- `C9`: Press down the tilt angle  of 3258120_3 by 1 degrees
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3258120_3
- `C11`: Increase transmission power for 3267899_4 **← 정답**
- `C12`: Decrease transmission power for 3258120_3
- `C13`: Lift the tilt angle of 3267899_4 by 5 degrees
- `C14`: Increase A3 Offset threshold for 3258120_3
- `C15`: Increase A3 Offset threshold for 3267899_4
- `C16`: Check test server and transmission issues
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3267899_4
- `C18`: Adjust the azimuth of 3258120_3 by 6 degrees
- `C19`: Insufficient data; more data is needed for judgment.
- `C20`: Add neighbor relationship between 3276543_1 and 3258120_3
- `C21`: Decrease transmission power for 3267899_4
- `C22`: Press down the tilt angle of 3267899_4 by 5 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.873 | MS1 | 121.4656615468 | 31.1446363457 | 823 | 504990 | -92.18 | 16.62 | 607.27 | 0.03 | 2.04 | 1597 |
| 2024-09-20 22:21:32.428 | MS1 | 121.4656621298 | 31.1446286951 | 823 | 504990 | -90.55 | 16.11 | 349.18 | 0.06 | 2.83 | 1561 |
| 2024-09-20 22:21:33.935 | MS1 | 121.4656757967 | 31.1446191067 | 823 | 504990 | -92.29 | 17.79 | 517.70 | 0.07 | 2.99 | 1592 |
| 2024-09-20 22:21:34.745 | MS1 | 121.4656591948 | 31.1446286912 | 823 | 504990 | -100.80 | 0.44 | 58.03 | 0.15 | 1.00 | 1581 |
| 2024-09-20 22:21:35.601 | MS1 | 121.4656705545 | 31.1446313947 | 823 | 504990 | -101.81 | 1.47 | 43.10 | 0.07 | 1.18 | 1565 |
| 2024-09-20 22:21:36.960 | MS1 | 121.4656637636 | 31.1446333096 | 823 | 504990 | -108.12 | -0.42 | 72.54 | 0.03 | 1.10 | 1594 |
| 2024-09-20 22:21:37.125 | MS1 | 121.4656718938 | 31.1446288297 | 823 | 504990 | -105.23 | 1.76 | 61.20 | 0.02 | 1.08 | 1566 |
| 2024-09-20 22:21:38.333 | MS1 | 121.4656768695 | 31.1446262095 | 823 | 504990 | -105.99 | 0.44 | 79.67 | 0.09 | 1.29 | 1586 |
| 2024-09-20 22:21:39.584 | MS1 | 121.4656635042 | 31.1446361401 | 823 | 504990 | -107.72 | -0.72 | 30.90 | 0.02 | 1.08 | 1596 |
| 2024-09-20 22:21:40.159 | MS1 | 121.4656725734 | 31.1446246755 | 823 | 504990 | -89.94 | 17.13 | 350.48 | 0.17 | 2.22 | 1575 |
| 2024-09-20 22:21:41.978 | MS1 | 121.4656768512 | 31.1446331147 | 823 | 504990 | -90.56 | 17.82 | 585.78 | 0.09 | 2.94 | 1565 |
| 2024-09-20 22:21:42.473 | MS1 | 121.4656648997 | 31.1446213122 | 823 | 504990 | -90.55 | 17.14 | 346.83 | 0.20 | 2.29 | 1580 |

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
| 3258120 | 3 | 121.4664192413 | 31.1513703315 | 191 | 0 | 9 | 18.0 | TDD | 229 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3267899 | 4 | 121.4752116588 | 31.1545162533 | 297 | 3 | 10 | 46.4 | TDD | 823 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3267993 | 2 | 121.4756460814 | 31.1442079114 | 140 | 5 | 10 | 24.0 | TDD | 668 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3276543 | 1 | 121.4694241830 | 31.1510063632 | 33 | 15 | 3 | 39.7 | TDD | 865 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |

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
| 2024-09-20 22:21:31.573 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.598 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.718 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.718 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.955 | NREventA2 | measId:1;ServCellPCI:377;Se... |
| 2024-09-20 22:21:35.056 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3276543 | 1 | 9.5665 | 15.2684 | -116.7900 | 9.5920 | 142.4065 | 0.0013 | 0.0139 |
| 2024_09_20 22:00 | 3267993 | 2 | 6.6488 | 7.6713 | -114.3464 | 13.6702 | 185.9445 | 0.0152 | 0.0030 |
| 2024_09_20 22:00 | 3258120 | 3 | 13.9238 | 16.6062 | -114.1958 | 5.7849 | 146.1212 | 0.0169 | 0.0041 |
| 2024_09_20 22:00 | 3267899 | 4 | 14.4742 | 7.9501 | -117.2842 | 13.0808 | 96.1391 | 0.1008 | 0.0020 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416094_2AA65D1A | 504990 | 823 | -101.2 | 504990 | 229 | -105.1 | 504990 | 865 | -108.6 | 504990 | 668 |
| MR_1774416094_5143714E | 504990 | 823 | -100.8 | 504990 | 229 | -104.8 | 504990 | 865 | -110.3 | 504990 | 668 |
| MR_1774416094_95CA47F7 | 504990 | 823 | -102.1 | 504990 | 229 | -103.9 | 504990 | 865 | -111.7 | 504990 | 668 |
| MR_1774416094_886A2BE4 | 504990 | 823 | -99.9 | 504990 | 229 | -104.4 | 504990 | 865 | -111.1 | 504990 | 668 |
| MR_1774416094_B1F20CDB | 504990 | 823 | -100.0 | 504990 | 229 | -104.5 | 504990 | 865 | -111.7 | 504990 | 668 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 495: `06740329-998...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `06740329-9988-4399-8cbb-5c2eadfc9fff` |
| Tag | **single-answer** |
| 정답 | **C20** |
| C20 의미 | Lift the tilt angle  of 3228940_1 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[495] topology](images/train_0495.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3248184_3
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3238153_4
- `C3`: Increase A3 Offset threshold for 3248184_3
- `C4`: Increase A3 Offset threshold for 3238153_4
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3238153_4
- `C6`: Decrease A3 Offset threshold for 3248184_3
- `C7`: Adjust the azimuth of 3228940_1 by 50 degrees
- `C8`: Check test server and transmission issues
- `C9`: Press down the tilt angle of 3238153_4 by 3 degrees
- `C10`: Increase transmission power for 3238153_4
- `C11`: Decrease transmission power for 3248184_3
- `C12`: Adjust the azimuth of 3238153_4 by 10 degrees
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3248184_3
- `C14`: Decrease transmission power for 3238153_4
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3248184_3
- `C16`: Add neighbor relationship between 3228940_1 and 3248184_3
- `C17`: Add neighbor relationship between 3238153_4 and 3248184_3
- `C18`: Lift the tilt angle of 3238153_4 by 3 degrees
- `C19`: Press down the tilt angle  of 3228940_1 by 10 degrees
- `C20`: Lift the tilt angle  of 3228940_1 by 10 degrees **← 정답**
- `C21`: Decrease A3 Offset threshold for 3238153_4
- `C22`: Insufficient data; more data is needed for judgment.

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.689 | MS1 | 121.4656735773 | 31.1446367465 | 645 | 504990 | -88.15 | 14.84 | 329.26 | 0.18 | 2.19 | 1600 |
| 2024-09-20 22:21:32.457 | MS1 | 121.4656740731 | 31.1446320013 | 645 | 504990 | -90.58 | 17.56 | 419.36 | 0.16 | 2.95 | 1579 |
| 2024-09-20 22:21:33.809 | MS1 | 121.4656767165 | 31.1446194010 | 645 | 504990 | -88.89 | 16.97 | 398.47 | 0.09 | 2.83 | 1592 |
| 2024-09-20 22:21:34.751 | MS1 | 121.4656761108 | 31.1446234671 | 645 | 504990 | -87.75 | 17.99 | 106.08 | 0.14 | 2.98 | 1566 |
| 2024-09-20 22:21:35.458 | MS1 | 121.4656739628 | 31.1446287295 | 645 | 504990 | -86.53 | 15.29 | 80.55 | 0.12 | 2.30 | 1600 |
| 2024-09-20 22:21:36.310 | MS1 | 121.4656708938 | 31.1446285047 | 645 | 504990 | -87.72 | 16.49 | 95.63 | 0.02 | 2.26 | 1582 |
| 2024-09-20 22:21:37.717 | MS1 | 121.4656660282 | 31.1446336155 | 645 | 504990 | -93.39 | 10.22 | 62.46 | 0.12 | 2.87 | 1594 |
| 2024-09-20 22:21:38.144 | MS1 | 121.4656685127 | 31.1446288360 | 645 | 504990 | -92.31 | 11.49 | 84.42 | 0.04 | 2.86 | 1577 |
| 2024-09-20 22:21:39.742 | MS1 | 121.4656616165 | 31.1446278326 | 645 | 504990 | -92.58 | 9.83 | 93.80 | 0.10 | 2.93 | 1600 |
| 2024-09-20 22:21:40.153 | MS1 | 121.4656615173 | 31.1446318255 | 645 | 504990 | -92.11 | 7.58 | 493.34 | 0.00 | 2.59 | 1567 |
| 2024-09-20 22:21:41.948 | MS1 | 121.4656762163 | 31.1446228633 | 645 | 504990 | -92.80 | 8.74 | 497.49 | 0.07 | 2.50 | 1597 |
| 2024-09-20 22:21:42.299 | MS1 | 121.4656629335 | 31.1446182522 | 645 | 504990 | -90.57 | 10.37 | 526.67 | 0.03 | 2.09 | 1579 |

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
| 3228940 | 1 | 121.4675711322 | 31.1458571170 | 310 | 11 | 6 | 30.0 | TDD | 16 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3238153 | 4 | 121.4704898168 | 31.1544277093 | 213 | 1 | 3 | 33.4 | TDD | 645 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3248184 | 3 | 121.4753810592 | 31.1467241570 | 116 | 9 | 9 | 23.8 | TDD | 716 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3252370 | 2 | 121.4704512500 | 31.1503934689 | 348 | 5 | 0 | 38.2 | TDD | 113 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |

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
| 2024-09-20 22:21:31.038 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.060 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.183 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.183 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.871 | NREventA3 | measId:2;ServCellPCI:768;Se... |
| 2024-09-20 22:21:38.111 | NRHandoverAttempt | SourcePCI:768;SourceNR-ARFC... |
| 2024-09-20 22:21:38.157 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.170 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.272 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.272 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3228940 | 1 | 10.6562 | 14.5835 | -117.2664 | 5.4047 | 123.2944 | 0.0170 | 0.0192 |
| 2024_09_20 22:00 | 3252370 | 2 | 12.4517 | 15.6822 | -115.3245 | 5.5117 | 98.6548 | 0.0190 | 0.0092 |
| 2024_09_20 22:00 | 3248184 | 3 | 14.6199 | 11.7287 | -115.1960 | 11.8983 | 100.6238 | 0.0175 | 0.0149 |
| 2024_09_20 22:00 | 3238153 | 4 | 87.7298 | 86.0399 | -117.3481 | 13.7403 | 114.9528 | 0.0046 | 0.0017 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412100_9C00D99D | 504990 | 645 | -85.0 | 504990 | 716 | -88.3 | 504990 | 16 | -94.7 | 504990 | 113 |
| MR_1774412100_4EC4119E | 504990 | 645 | -85.8 | 504990 | 716 | -89.4 | 504990 | 16 | -93.5 | 504990 | 113 |
| MR_1774412100_EC30A8FC | 504990 | 645 | -86.9 | 504990 | 716 | -91.6 | 504990 | 16 | -97.0 | 504990 | 113 |
| MR_1774412100_BDEDB4AC | 504990 | 645 | -87.7 | 504990 | 716 | -88.4 | 504990 | 16 | -95.3 | 504990 | 113 |
| MR_1774412100_532DBA7D | 504990 | 645 | -87.0 | 504990 | 716 | -90.7 | 504990 | 16 | -94.4 | 504990 | 113 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 496: `fc315a50-900...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `fc315a50-900a-453f-a204-4685d6fe6a31` |
| Tag | **single-answer** |
| 정답 | **C12** |
| C12 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3257860_6 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[496] topology](images/train_0496.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3260256_2
- `C2`: Check test server and transmission issues
- `C3`: Increase A3 Offset threshold for 3257860_6
- `C4`: Decrease A3 Offset threshold for 3257860_6
- `C5`: Lift the tilt angle of 3257860_6 by 2 degrees
- `C6`: Adjust the azimuth of 3257860_6 by 43 degrees
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3260256_2
- `C8`: Press down the tilt angle of 3257860_6 by 2 degrees
- `C9`: Press down the tilt angle  of 3260256_2 by 5 degrees
- `C10`: Add neighbor relationship between 3257860_6 and 3260256_2
- `C11`: Adjust the azimuth of 3260256_2 by 13 degrees
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3257860_6 **← 정답**
- `C13`: Decrease transmission power for 3257860_6
- `C14`: Decrease A3 Offset threshold for 3260256_2
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3260256_2
- `C16`: Decrease transmission power for 3260256_2
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3257860_6
- `C18`: Add neighbor relationship between 3241100_9 and 3260256_2
- `C19`: Insufficient data; more data is needed for judgment.
- `C20`: Increase A3 Offset threshold for 3260256_2
- `C21`: Increase transmission power for 3257860_6
- `C22`: Lift the tilt angle  of 3260256_2 by 5 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.231 | MS1 | 121.4656602742 | 31.1446312391 | 278 | 504990 | -94.06 | 12.49 | 544.42 | 0.19 | 2.78 | 1563 |
| 2024-09-20 22:21:32.274 | MS1 | 121.4656716345 | 31.1446331428 | 374 | 504990 | -95.00 | 10.55 | 457.65 | 0.06 | 2.35 | 1578 |
| 2024-09-20 22:21:33.120 | MS1 | 121.4656750115 | 31.1446355860 | 814 | 504990 | -94.27 | 13.03 | 405.41 | 0.17 | 2.35 | 1570 |
| 2024-09-20 22:21:34.230 | MS1 | 121.4656698493 | 31.1446330241 | 989 | 152650 | -95.34 | 6.86 | 59.01 | 0.10 | 1.91 | 917 |
| 2024-09-20 22:21:35.179 | MS1 | 121.4656749278 | 31.1446313187 | 237 | 152650 | -94.67 | 3.68 | 98.79 | 0.17 | 1.87 | 985 |
| 2024-09-20 22:21:36.654 | MS1 | 121.4656657551 | 31.1446353762 | 908 | 152650 | -91.20 | 3.20 | 56.83 | 0.07 | 1.89 | 942 |
| 2024-09-20 22:21:37.736 | MS1 | 121.4656622469 | 31.1446240804 | 457 | 152650 | -88.25 | 5.39 | 88.60 | 0.12 | 1.89 | 973 |
| 2024-09-20 22:21:38.877 | MS1 | 121.4656681603 | 31.1446306208 | 989 | 152650 | -90.59 | 3.88 | 85.33 | 0.13 | 1.97 | 911 |
| 2024-09-20 22:21:39.302 | MS1 | 121.4656662264 | 31.1446224352 | 237 | 152650 | -89.80 | 2.61 | 51.32 | 0.11 | 1.99 | 902 |
| 2024-09-20 22:21:40.394 | MS1 | 121.4656656307 | 31.1446288827 | 908 | 152650 | -96.83 | 3.11 | 57.66 | 0.05 | 2.60 | 1568 |
| 2024-09-20 22:21:41.502 | MS1 | 121.4656660778 | 31.1446315437 | 457 | 152650 | -96.47 | 6.04 | 79.22 | 0.17 | 2.44 | 1581 |
| 2024-09-20 22:21:42.666 | MS1 | 121.4656770058 | 31.1446360593 | 989 | 152650 | -91.21 | 7.33 | 81.91 | 0.01 | 2.69 | 1595 |

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
| 3213813 | 1 | 121.4727588021 | 31.1502052459 | 206 | 1 | 10 | 8.6 | TDD | 994 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3221398 | 7 | 121.4730622343 | 31.1475149296 | 342 | 8 | 5 | 0.3 | FDD | 457 | n1 | 152650 | 30M | 4T4R | 14 | 152650 |
| 3227050 | 8 | 121.4672594253 | 31.1559084388 | 146 | 1 | 5 | 6.8 | FDD | 170 | n1 | 152650 | 30M | 4T4R | 11 | 152650 |
| 3228630 | 13 | 121.4684538205 | 31.1501491945 | 293 | 3 | 0 | 18.4 | FDD | 989 | n1 | 152650 | 30M | 4T4R | 10 | 152650 |
| 3234264 | 3 | 121.4680885642 | 31.1456761846 | 70 | 8 | 2 | 11.3 | TDD | 814 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3241100 | 9 | 121.4706075392 | 31.1459720968 | 323 | 0 | 4 | 1.2 | FDD | 908 | n1 | 152650 | 30M | 4T4R | 14 | 152650 |
| 3247490 | 5 | 121.4719245432 | 31.1538821009 | 13 | 1 | 4 | 5.7 | TDD | 374 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3252939 | 4 | 121.4740278914 | 31.1520822736 | 99 | 10 | 11 | 14.4 | TDD | 693 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3255420 | 11 | 121.4642352062 | 31.1543947867 | 11 | 12 | 6 | 20.6 | FDD | 852 | n1 | 152650 | 30M | 4T4R | 19 | 152650 |
| 3257860 | 6 | 121.4664050733 | 31.1551831405 | 140 | 1 | 0 | 14.3 | TDD | 278 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3259646 | 10 | 121.4684977749 | 31.1548504425 | 223 | 15 | 5 | 16.8 | FDD | 237 | n1 | 152650 | 30M | 4T4R | 12 | 152650 |
| 3260256 | 2 | 121.4691220985 | 31.1507816156 | 193 | 5 | 3 | 3.8 | TDD | 66 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3276739 | 12 | 121.4722070708 | 31.1555366406 | 191 | 14 | 6 | 16.5 | FDD | 726 | n1 | 152650 | 30M | 4T4R | 11 | 152650 |

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
| 2024-09-20 22:21:31.438 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.458 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.575 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.575 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.277 | NREventA2 | measId:1;ServCellPCI:389;Se... |
| 2024-09-20 22:21:35.382 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.662 | NREventA5 | measId:3;ServCellPCI:389;Se... |
| 2024-09-20 22:21:35.721 | NRHandoverAttempt | SourcePCI:389;SourceNR-ARFC... |
| 2024-09-20 22:21:35.755 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.770 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:35.873 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.873 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3213813 | 1 | 6.1567 | 18.7589 | -115.7321 | 12.8184 | 144.8456 | 0.0021 | 0.0077 |
| 2024_09_20 22:00 | 3260256 | 2 | 19.5895 | 17.3336 | -116.6623 | 16.7322 | 86.3489 | 0.0180 | 0.0035 |
| 2024_09_20 22:00 | 3234264 | 3 | 6.5458 | 10.4805 | -116.1528 | 9.3104 | 151.5155 | 0.0049 | 0.0104 |
| 2024_09_20 22:00 | 3252939 | 4 | 7.8204 | 16.6001 | -117.9757 | 19.1712 | 120.2302 | 0.0164 | 0.0159 |
| 2024_09_20 22:00 | 3247490 | 5 | 10.6897 | 19.3461 | -116.9440 | 13.3024 | 154.2467 | 0.0047 | 0.0037 |
| 2024_09_20 22:00 | 3257860 | 6 | 17.2920 | 18.7141 | -114.3865 | 19.5127 | 189.7685 | 0.0198 | 0.0188 |
| 2024_09_20 22:00 | 3221398 | 7 | 10.6581 | 19.4358 | -114.5905 | 4.7091 | 45.0861 | 0.0021 | 0.0138 |
| 2024_09_20 22:00 | 3227050 | 8 | 13.3454 | 18.2179 | -114.4291 | 3.7656 | 35.1088 | 0.0186 | 0.0170 |
| 2024_09_20 22:00 | 3241100 | 9 | 8.3336 | 14.9829 | -115.8450 | 3.2004 | 42.9348 | 0.0187 | 0.0118 |
| 2024_09_20 22:00 | 3259646 | 10 | 11.5026 | 17.9422 | -117.1148 | 4.1675 | 35.7786 | 0.0045 | 0.0177 |
| 2024_09_20 22:00 | 3255420 | 11 | 19.2518 | 6.5494 | -117.3178 | 3.0482 | 45.7135 | 0.0158 | 0.0099 |
| 2024_09_20 22:00 | 3276739 | 12 | 13.7275 | 7.6620 | -116.0690 | 4.0203 | 32.0500 | 0.0036 | 0.0194 |
| 2024_09_20 22:00 | 3228630 | 13 | 11.0683 | 6.7750 | -115.5049 | 4.6515 | 38.7464 | 0.0179 | 0.0171 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414958_CEFEBF89 | 152650 | 989 | -94.4 | 152650 | 170 | -104.7 | 152650 | 852 | -107.6 | 152650 | 726 |
| MR_1774414958_D17F0E8B | 152650 | 989 | -94.5 | 152650 | 170 | -102.5 | 152650 | 852 | -105.7 | 152650 | 726 |
| MR_1774414958_86F123B7 | 152650 | 989 | -94.4 | 152650 | 170 | -103.2 | 152650 | 852 | -108.0 | 152650 | 726 |
| MR_1774414958_B7285C28 | 152650 | 989 | -97.2 | 152650 | 170 | -103.4 | 152650 | 852 | -109.0 | 152650 | 726 |
| MR_1774414958_8DDBAF3A | 504990 | 814 | -93.3 | 504990 | 66 | -94.3 | 504990 | 994 | -97.4 | 504990 | 693 |
| MR_1774414958_AF7B10C5 | 504990 | 814 | -93.6 | 504990 | 66 | -96.3 | 504990 | 994 | -99.3 | 504990 | 693 |
| MR_1774414958_9FDCD734 | 504990 | 814 | -95.1 | 504990 | 66 | -96.4 | 504990 | 994 | -96.1 | 504990 | 693 |
| MR_1774414958_FD3261DC | 504990 | 814 | -96.2 | 504990 | 66 | -95.3 | 504990 | 994 | -96.6 | 504990 | 693 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 497: `f1faae2a-ca5...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `f1faae2a-ca5f-400a-a438-59826bf80886` |
| Tag | **single-answer** |
| 정답 | **C10** |
| C10 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[497] topology](images/train_0497.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Check test server and transmission issues
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3260976_1
- `C3`: Increase A3 Offset threshold for 3267741_3
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3267741_3
- `C5`: Increase transmission power for 3267741_3
- `C6`: Add neighbor relationship between 3223839_2 and 3260976_1
- `C7`: Press down the tilt angle  of 3260976_1 by 10 degrees
- `C8`: Increase transmission power for 3260976_1
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3267741_3
- `C10`: Insufficient data; more data is needed for judgment. **← 정답**
- `C11`: Decrease transmission power for 3267741_3
- `C12`: Lift the tilt angle  of 3260976_1 by 10 degrees
- `C13`: Adjust the azimuth of 3260976_1 by 36 degrees
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3260976_1
- `C15`: Press down the tilt angle of 3267741_3 by 3 degrees
- `C16`: Add neighbor relationship between 3267741_3 and 3260976_1
- `C17`: Increase A3 Offset threshold for 3260976_1
- `C18`: Decrease A3 Offset threshold for 3260976_1
- `C19`: Adjust the azimuth of 3267741_3 by 16 degrees
- `C20`: Lift the tilt angle of 3267741_3 by 3 degrees
- `C21`: Decrease A3 Offset threshold for 3267741_3
- `C22`: Decrease transmission power for 3260976_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.606 | MS1 | 121.4656718657 | 31.1446347967 | 954 | 504990 | -90.68 | 14.47 | 352.29 | 0.14 | 2.16 | 1577 |
| 2024-09-20 22:21:32.197 | MS1 | 121.4656605183 | 31.1446329475 | 954 | 504990 | -85.40 | 16.66 | 391.77 | 0.01 | 2.65 | 1574 |
| 2024-09-20 22:21:33.456 | MS1 | 121.4656727076 | 31.1446284270 | 954 | 504990 | -91.54 | 15.38 | 464.45 | 0.16 | 2.46 | 1571 |
| 2024-09-20 22:21:34.632 | MS1 | 121.4656747523 | 31.1446283567 | 954 | 504990 | -90.18 | 16.01 | 61.60 | 0.10 | 3.00 | 1560 |
| 2024-09-20 22:21:35.707 | MS1 | 121.4656630983 | 31.1446358009 | 954 | 504990 | -86.19 | 17.86 | 105.02 | 0.17 | 2.65 | 1577 |
| 2024-09-20 22:21:36.260 | MS1 | 121.4656736453 | 31.1446263102 | 954 | 504990 | -87.16 | 16.23 | 78.32 | 0.18 | 2.73 | 1596 |
| 2024-09-20 22:21:37.807 | MS1 | 121.4656594159 | 31.1446322717 | 954 | 504990 | -90.28 | 11.25 | 68.12 | 0.04 | 2.51 | 1590 |
| 2024-09-20 22:21:38.514 | MS1 | 121.4656690883 | 31.1446200182 | 954 | 504990 | -89.66 | 9.56 | 64.74 | 0.05 | 2.92 | 1580 |
| 2024-09-20 22:21:39.669 | MS1 | 121.4656598874 | 31.1446372493 | 954 | 504990 | -90.40 | 10.38 | 53.40 | 0.07 | 2.76 | 1590 |
| 2024-09-20 22:21:40.698 | MS1 | 121.4656697655 | 31.1446266263 | 954 | 504990 | -90.22 | 8.97 | 479.26 | 0.15 | 2.94 | 1562 |
| 2024-09-20 22:21:41.389 | MS1 | 121.4656619693 | 31.1446363786 | 954 | 504990 | -93.36 | 11.94 | 495.65 | 0.01 | 2.73 | 1560 |
| 2024-09-20 22:21:42.233 | MS1 | 121.4656726813 | 31.1446348682 | 954 | 504990 | -93.87 | 11.73 | 471.85 | 0.05 | 2.89 | 1573 |

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
| 3223839 | 2 | 121.4731163342 | 31.1555915682 | 208 | 5 | 5 | 22.5 | TDD | 825 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3260976 | 1 | 121.4654861186 | 31.1462243441 | 139 | 4 | 7 | 49.9 | TDD | 24 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3267741 | 3 | 121.4678593353 | 31.1524388682 | 210 | 0 | 11 | 48.3 | TDD | 954 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3270893 | 4 | 121.4746544080 | 31.1512031843 | 85 | 13 | 6 | 31.4 | TDD | 313 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |

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
| 2024-09-20 22:21:30.984 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.105 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.105 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.794 | NREventA3 | measId:2;ServCellPCI:168;Se... |
| 2024-09-20 22:21:38.034 | NRHandoverAttempt | SourcePCI:168;SourceNR-ARFC... |
| 2024-09-20 22:21:38.073 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.087 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.212 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.212 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3260976 | 1 | 78.2499 | 85.9338 | -114.2321 | 19.3713 | 180.8907 | 0.0197 | 0.0173 |
| 2024_09_19 22:00 | 3223839 | 2 | 89.5106 | 92.5071 | -114.3191 | 19.9825 | 168.3944 | 0.0065 | 0.0186 |
| 2024_09_19 22:00 | 3267741 | 3 | 84.2130 | 87.5013 | -114.5700 | 9.7195 | 108.6021 | 0.0155 | 0.0013 |
| 2024_09_19 22:00 | 3270893 | 4 | 81.4644 | 78.1348 | -117.5959 | 16.5844 | 194.0916 | 0.0045 | 0.0060 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774411987_F2A7A147 | 504990 | 954 | -88.6 | 504990 | 24 | -91.0 | 504990 | 825 | -104.0 | 504990 | 313 |
| MR_1774411987_725DC5F3 | 504990 | 954 | -88.3 | 504990 | 24 | -90.2 | 504990 | 825 | -104.2 | 504990 | 313 |
| MR_1774411987_A2CCF845 | 504990 | 954 | -91.8 | 504990 | 24 | -92.1 | 504990 | 825 | -105.2 | 504990 | 313 |
| MR_1774411987_5AA28B50 | 504990 | 954 | -91.0 | 504990 | 24 | -92.0 | 504990 | 825 | -103.7 | 504990 | 313 |
| MR_1774411987_404CACF7 | 504990 | 954 | -88.3 | 504990 | 24 | -90.7 | 504990 | 825 | -107.0 | 504990 | 313 |
| MR_1774411987_1B0AB286 | 504990 | 954 | -90.8 | 504990 | 24 | -88.9 | 504990 | 825 | -106.0 | 504990 | 313 |
| MR_1774411987_A6B8B1E7 | 504990 | 954 | -89.9 | 504990 | 24 | -92.4 | 504990 | 825 | -106.4 | 504990 | 313 |
| MR_1774411987_C8F3A2D4 | 504990 | 954 | -91.1 | 504990 | 24 | -91.1 | 504990 | 825 | -106.5 | 504990 | 313 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 498: `e05914bb-e6c...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `e05914bb-e6c9-4db4-8294-4d6b6d7f2167` |
| Tag | **multiple-answer** |
| 정답 | **C2|C4|C5|C15** |
| C2 의미 | Decrease transmission power for 3269605_2 |
| C4 의미 | Press down the tilt angle  of 3269605_2 by 3 degrees |
| C5 의미 | Increase A3 Offset threshold for 3268562_4 |
| C15 의미 | Increase A3 Offset threshold for 3269605_2 |
| 패턴 분류 | **P3 Overshoot (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[498] topology](images/train_0498.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 5 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 5개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3268562_4 by 5 degrees
- `C2`: Decrease transmission power for 3269605_2 **← 정답**
- `C3`: Insufficient data; more data is needed for judgment.
- `C4`: Press down the tilt angle  of 3269605_2 by 3 degrees **← 정답**
- `C5`: Increase A3 Offset threshold for 3268562_4 **← 정답**
- `C6`: Increase transmission power for 3268562_4
- `C7`: Add neighbor relationship between 3268562_4 and 3269605_2
- `C8`: Increase transmission power for 3269605_2
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3268562_4
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3269605_2
- `C11`: Adjust the azimuth of 3268562_4 by 3 degrees
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3268562_4
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3269605_2
- `C14`: Decrease transmission power for 3268562_4
- `C15`: Increase A3 Offset threshold for 3269605_2 **← 정답**
- `C16`: Decrease A3 Offset threshold for 3268562_4
- `C17`: Lift the tilt angle of 3268562_4 by 5 degrees
- `C18`: Add neighbor relationship between 3238608_3 and 3269605_2
- `C19`: Lift the tilt angle  of 3269605_2 by 3 degrees
- `C20`: Check test server and transmission issues
- `C21`: Decrease A3 Offset threshold for 3269605_2
- `C22`: Adjust the azimuth of 3269605_2 by 40 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.784 | MS1 | 121.4656603488 | 31.1446192739 | 562 | 504990 | -82.53 | 12.53 | 448.35 | 0.04 | 2.69 | 1581 |
| 2024-09-20 22:21:32.496 | MS1 | 121.4656718194 | 31.1446291696 | 562 | 504990 | -82.33 | 17.09 | 385.01 | 0.01 | 2.89 | 1570 |
| 2024-09-20 22:21:33.592 | MS1 | 121.4656659502 | 31.1446355140 | 562 | 504990 | -77.56 | 17.93 | 553.44 | 0.04 | 2.70 | 1598 |
| 2024-09-20 22:21:34.689 | MS1 | 121.4656763051 | 31.1446231040 | 230 | 504990 | -80.58 | 3.67 | 46.49 | 0.14 | 1.40 | 1594 |
| 2024-09-20 22:21:35.499 | MS1 | 121.4656601384 | 31.1446331116 | 230 | 504990 | -80.03 | 4.61 | 41.40 | 0.13 | 1.37 | 1563 |
| 2024-09-20 22:21:36.809 | MS1 | 121.4656712628 | 31.1446379679 | 562 | 504990 | -85.05 | 3.25 | 46.75 | 0.01 | 1.49 | 1561 |
| 2024-09-20 22:21:37.713 | MS1 | 121.4656635743 | 31.1446299251 | 562 | 504990 | -82.48 | 2.75 | 50.33 | 0.13 | 1.10 | 1587 |
| 2024-09-20 22:21:38.316 | MS1 | 121.4656761943 | 31.1446346268 | 230 | 504990 | -82.75 | 4.05 | 26.68 | 0.08 | 1.43 | 1580 |
| 2024-09-20 22:21:39.459 | MS1 | 121.4656642043 | 31.1446368650 | 230 | 504990 | -83.18 | 1.34 | 61.91 | 0.18 | 1.30 | 1580 |
| 2024-09-20 22:21:40.424 | MS1 | 121.4656612869 | 31.1446181030 | 230 | 504990 | -77.36 | 16.00 | 447.44 | 0.00 | 2.76 | 1583 |
| 2024-09-20 22:21:41.244 | MS1 | 121.4656664611 | 31.1446257396 | 230 | 504990 | -83.42 | 15.56 | 378.21 | 0.10 | 2.31 | 1575 |
| 2024-09-20 22:21:42.382 | MS1 | 121.4656581359 | 31.1446327830 | 230 | 504990 | -77.93 | 13.58 | 601.82 | 0.07 | 2.50 | 1568 |

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
| 3235470 | 5 | 121.4720206765 | 31.1487510959 | 344 | 3 | 4 | 26.3 | TDD | 981 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3238608 | 3 | 121.4696062194 | 31.1443889027 | 215 | 9 | 5 | 29.8 | TDD | 649 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3265764 | 1 | 121.4723514511 | 31.1532693562 | 326 | 1 | 2 | 34.3 | TDD | 230 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3268562 | 4 | 121.4680123118 | 31.1538569749 | 189 | 3 | 6 | 40.9 | TDD | 562 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3269605 | 2 | 121.4667969786 | 31.1505679082 | 149 | 0 | 4 | 37.0 | TDD | 8 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |

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
| 2024-09-20 22:21:31.184 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.205 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.317 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.317 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.011 | NREventA3 | measId:2;ServCellPCI:932;Se... |
| 2024-09-20 22:21:34.251 | NRHandoverAttempt | SourcePCI:932;SourceNR-ARFC... |
| 2024-09-20 22:21:34.294 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:34.305 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:34.448 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:34.448 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:36.011 | NREventA3 | measId:2;ServCellPCI:993;Se... |
| 2024-09-20 22:21:36.251 | NRHandoverAttempt | SourcePCI:993;SourceNR-ARFC... |
| 2024-09-20 22:21:36.287 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:36.300 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:36.430 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.430 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.011 | NREventA3 | measId:2;ServCellPCI:932;Se... |
| 2024-09-20 22:21:38.251 | NRHandoverAttempt | SourcePCI:932;SourceNR-ARFC... |
| 2024-09-20 22:21:38.300 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.310 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.425 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.425 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3265764 | 1 | 17.9924 | 8.7788 | -116.6871 | 15.1776 | 136.3350 | 0.0151 | 0.0049 |
| 2024_09_20 22:00 | 3269605 | 2 | 16.3403 | 19.7823 | -115.6805 | 6.6953 | 177.0250 | 0.0023 | 0.0114 |
| 2024_09_20 22:00 | 3238608 | 3 | 12.7717 | 8.4850 | -114.6107 | 18.0617 | 172.1760 | 0.0095 | 0.0171 |
| 2024_09_20 22:00 | 3268562 | 4 | 19.0008 | 12.4979 | -116.0261 | 9.7287 | 163.6774 | 0.0020 | 0.0100 |
| 2024_09_20 22:00 | 3235470 | 5 | 11.9525 | 16.9659 | -117.2256 | 6.4825 | 178.8596 | 0.0040 | 0.0033 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413444_4EE0F49D | 504990 | 230 | -81.0 | 504990 | 562 | -79.1 | 504990 | 8 | -80.4 | 504990 | 649 |
| MR_1774413444_F5E6452E | 504990 | 230 | -80.9 | 504990 | 562 | -79.4 | 504990 | 8 | -83.3 | 504990 | 649 |
| MR_1774413444_4BE92FA3 | 504990 | 230 | -79.7 | 504990 | 562 | -82.4 | 504990 | 8 | -80.9 | 504990 | 649 |
| MR_1774413444_CBF2F28C | 504990 | 230 | -81.0 | 504990 | 562 | -81.5 | 504990 | 8 | -83.0 | 504990 | 649 |
| MR_1774413444_94B1067C | 504990 | 562 | -79.6 | 504990 | 230 | -80.1 | 504990 | 8 | -80.9 | 504990 | 649 |
| MR_1774413444_F358E472 | 504990 | 562 | -80.0 | 504990 | 230 | -80.1 | 504990 | 8 | -83.3 | 504990 | 649 |
| MR_1774413444_6DFF4314 | 504990 | 230 | -79.7 | 504990 | 562 | -80.0 | 504990 | 8 | -80.4 | 504990 | 649 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 499: `5ab417b9-70e...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `5ab417b9-70ed-44c7-8d6f-3109dcfe4903` |
| Tag | **single-answer** |
| 정답 | **C12** |
| C12 의미 | Add neighbor relationship between 3275532_2 and 3213246_4 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[499] topology](images/train_0499.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3275532_2
- `C2`: Insufficient data; more data is needed for judgment.
- `C3`: Check test server and transmission issues
- `C4`: Lift the tilt angle  of 3213246_4 by 3 degrees
- `C5`: Decrease transmission power for 3213246_4
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3213246_4
- `C7`: Decrease A3 Offset threshold for 3213246_4
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3275532_2
- `C9`: Press down the tilt angle  of 3213246_4 by 3 degrees
- `C10`: Increase transmission power for 3275532_2
- `C11`: Add neighbor relationship between 3227684_3 and 3213246_4
- `C12`: Add neighbor relationship between 3275532_2 and 3213246_4 **← 정답**
- `C13`: Decrease A3 Offset threshold for 3275532_2
- `C14`: Increase transmission power for 3213246_4
- `C15`: Lift the tilt angle of 3275532_2 by 10 degrees
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3275532_2
- `C17`: Press down the tilt angle of 3275532_2 by 10 degrees
- `C18`: Adjust the azimuth of 3275532_2 by 50 degrees
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3213246_4
- `C20`: Adjust the azimuth of 3213246_4 by 49 degrees
- `C21`: Decrease transmission power for 3275532_2
- `C22`: Increase A3 Offset threshold for 3213246_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.806 | MS1 | 121.4656637234 | 31.1446308366 | 362 | 504990 | -78.51 | 16.15 | 369.13 | 0.17 | 2.05 | 1600 |
| 2024-09-20 22:21:32.767 | MS1 | 121.4656581376 | 31.1446197016 | 362 | 504990 | -77.97 | 12.38 | 338.77 | 0.16 | 2.74 | 1572 |
| 2024-09-20 22:21:33.261 | MS1 | 121.4656592154 | 31.1446203503 | 362 | 504990 | -80.19 | 16.98 | 526.25 | 0.03 | 2.30 | 1591 |
| 2024-09-20 22:21:34.995 | MS1 | 121.4656636060 | 31.1446214371 | 362 | 504990 | -91.20 | -2.90 | 35.71 | 0.01 | 1.05 | 1600 |
| 2024-09-20 22:21:35.560 | MS1 | 121.4656648412 | 31.1446288011 | 362 | 504990 | -86.82 | -2.65 | 68.55 | 0.02 | 1.05 | 1562 |
| 2024-09-20 22:21:36.410 | MS1 | 121.4656690045 | 31.1446342459 | 362 | 504990 | -89.53 | -2.67 | 65.86 | 0.13 | 1.45 | 1569 |
| 2024-09-20 22:21:37.837 | MS1 | 121.4656694313 | 31.1446225869 | 362 | 504990 | -93.10 | -1.69 | 38.84 | 0.03 | 1.39 | 1581 |
| 2024-09-20 22:21:38.821 | MS1 | 121.4656717664 | 31.1446195233 | 362 | 504990 | -78.24 | 14.20 | 458.34 | 0.03 | 1.47 | 1596 |
| 2024-09-20 22:21:39.133 | MS1 | 121.4656612485 | 31.1446283847 | 362 | 504990 | -76.99 | 15.20 | 464.91 | 0.01 | 1.31 | 1582 |
| 2024-09-20 22:21:40.448 | MS1 | 121.4656699654 | 31.1446306499 | 362 | 504990 | -75.98 | 13.08 | 311.78 | 0.15 | 2.74 | 1582 |
| 2024-09-20 22:21:41.681 | MS1 | 121.4656645955 | 31.1446332316 | 362 | 504990 | -76.75 | 12.50 | 557.44 | 0.01 | 2.44 | 1600 |
| 2024-09-20 22:21:42.776 | MS1 | 121.4656681026 | 31.1446358765 | 362 | 504990 | -79.89 | 12.12 | 406.75 | 0.20 | 2.40 | 1560 |

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
| 3213246 | 4 | 121.4709431474 | 31.1508807789 | 167 | 0 | 7 | 46.3 | TDD | 757 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3220326 | 1 | 121.4749162424 | 31.1520925297 | 111 | 7 | 8 | 45.5 | TDD | 816 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3227684 | 3 | 121.4718265394 | 31.1553818750 | 245 | 11 | 1 | 28.0 | TDD | 988 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3275532 | 2 | 121.4734146362 | 31.1534981998 | 328 | 11 | 10 | 46.1 | TDD | 362 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:31.090 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.114 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.259 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.259 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.895 | NREventA3 | measId:2;ServCellPCI:88;Ser... |
| 2024-09-20 22:21:35.895 | NREventA3 | measId:2;ServCellPCI:88;Ser... |
| 2024-09-20 22:21:36.895 | NREventA3 | measId:2;ServCellPCI:88;Ser... |
| 2024-09-20 22:21:39.395 | NRRRCReestablishAttempt | PCI:88 |
| 2024-09-20 22:21:39.412 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.424 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:39.565 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.565 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3220326 | 1 | 7.9097 | 17.9683 | -114.6070 | 12.1591 | 145.5489 | 0.0010 | 0.0051 |
| 2024_09_20 22:00 | 3275532 | 2 | 17.4661 | 15.9450 | -116.1033 | 16.5175 | 196.6654 | 0.0006 | 0.1035 |
| 2024_09_20 22:00 | 3227684 | 3 | 11.8162 | 19.1886 | -115.8874 | 14.7956 | 136.7415 | 0.0184 | 0.0087 |
| 2024_09_20 22:00 | 3213246 | 4 | 15.5022 | 7.8306 | -114.8606 | 7.4017 | 109.3042 | 0.0143 | 0.0040 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416084_BA3CE674 | 504990 | 362 | -92.2 | 504990 | 757 | -88.0 | 504990 | 988 | -90.2 | 504990 | 816 |
| MR_1774416084_D8AEA4DC | 504990 | 362 | -93.0 | 504990 | 757 | -87.0 | 504990 | 988 | -91.0 | 504990 | 816 |
| MR_1774416084_B9E3FE18 | 504990 | 362 | -91.8 | 504990 | 757 | -84.6 | 504990 | 988 | -91.4 | 504990 | 816 |
| MR_1774416084_56925DAC | 504990 | 362 | -90.9 | 504990 | 757 | -87.4 | 504990 | 988 | -91.3 | 504990 | 816 |
| MR_1774416084_14DCF0A6 | 504990 | 362 | -90.3 | 504990 | 757 | -88.2 | 504990 | 988 | -91.6 | 504990 | 816 |
| MR_1774416084_EA6EF7BA | 504990 | 757 | -87.0 | 504990 | 362 | -91.3 | 504990 | 988 | -89.9 | 504990 | 816 |
| MR_1774416084_D7E56BCD | 504990 | 362 | -90.7 | 504990 | 757 | -87.8 | 504990 | 988 | -91.5 | 504990 | 816 |
| MR_1774416084_AAAEF2DB | 504990 | 757 | -88.2 | 504990 | 362 | -91.1 | 504990 | 988 | -91.9 | 504990 | 816 |

> *... 2개 열 생략 (전체 14열)*

---
