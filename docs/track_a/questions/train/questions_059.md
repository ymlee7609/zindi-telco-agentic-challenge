# Track A 문제 분석 — train[580]~train[589]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[580] ~ train[589] (10개)

## 목차

1. [문제 580: `66c4e5f0-54f...`](#580) — single-answer, 정답: C3
2. [문제 581: `a0083fc1-776...`](#581) — single-answer, 정답: C14
3. [문제 582: `ece2d7aa-3c2...`](#582) — multiple-answer, 정답: C5|C12
4. [문제 583: `0c87b3c3-7e5...`](#583) — multiple-answer, 정답: C18|C19
5. [문제 584: `f28c1f2f-5e4...`](#584) — single-answer, 정답: C1
6. [문제 585: `6faf3c03-07e...`](#585) — single-answer, 정답: C5
7. [문제 586: `c709b75c-a87...`](#586) — multiple-answer, 정답: C4|C11
8. [문제 587: `0a0f387d-0f9...`](#587) — single-answer, 정답: C6
9. [문제 588: `a4b5f79c-0f9...`](#588) — single-answer, 정답: C12
10. [문제 589: `eb290709-b15...`](#589) — single-answer, 정답: C5

---

### 문제 580: `66c4e5f0-54f...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `66c4e5f0-54fc-4571-ad6d-75b9375fb7a1` |
| Tag | **single-answer** |
| 정답 | **C3** |
| C3 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[580] topology](images/train_0580.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3265668_3
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3240048_1
- `C3`: Insufficient data; more data is needed for judgment. **← 정답**
- `C4`: Increase A3 Offset threshold for 3265668_3
- `C5`: Lift the tilt angle  of 3265668_3 by 10 degrees
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3240048_1
- `C7`: Lift the tilt angle of 3240048_1 by 10 degrees
- `C8`: Check test server and transmission issues
- `C9`: Increase A3 Offset threshold for 3240048_1
- `C10`: Add neighbor relationship between 3240048_1 and 3265668_3
- `C11`: Add neighbor relationship between 3241344_2 and 3265668_3
- `C12`: Press down the tilt angle  of 3265668_3 by 10 degrees
- `C13`: Decrease A3 Offset threshold for 3265668_3
- `C14`: Adjust the azimuth of 3240048_1 by 50 degrees
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3265668_3
- `C16`: Decrease A3 Offset threshold for 3240048_1
- `C17`: Press down the tilt angle of 3240048_1 by 10 degrees
- `C18`: Decrease transmission power for 3240048_1
- `C19`: Increase transmission power for 3240048_1
- `C20`: Increase transmission power for 3265668_3
- `C21`: Decrease transmission power for 3265668_3
- `C22`: Adjust the azimuth of 3265668_3 by 50 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.776 | MS1 | 121.4656583895 | 31.1446202199 | 516 | 504990 | -86.56 | 16.85 | 401.38 | 0.13 | 2.31 | 1579 |
| 2024-09-20 22:21:32.931 | MS1 | 121.4656738617 | 31.1446251208 | 516 | 504990 | -90.30 | 12.11 | 350.28 | 0.03 | 2.12 | 1593 |
| 2024-09-20 22:21:33.470 | MS1 | 121.4656622414 | 31.1446245087 | 516 | 504990 | -85.40 | 14.29 | 318.60 | 0.07 | 2.77 | 1568 |
| 2024-09-20 22:21:34.484 | MS1 | 121.4656636068 | 31.1446374433 | 516 | 504990 | -90.00 | 12.02 | 67.18 | 0.15 | 2.31 | 1584 |
| 2024-09-20 22:21:35.416 | MS1 | 121.4656669058 | 31.1446306148 | 516 | 504990 | -86.38 | 16.23 | 88.29 | 0.18 | 2.25 | 1574 |
| 2024-09-20 22:21:36.695 | MS1 | 121.4656678995 | 31.1446204086 | 516 | 504990 | -86.70 | 15.43 | 84.59 | 0.00 | 2.39 | 1588 |
| 2024-09-20 22:21:37.642 | MS1 | 121.4656743034 | 31.1446193336 | 516 | 504990 | -90.13 | 10.35 | 64.49 | 0.03 | 2.24 | 1579 |
| 2024-09-20 22:21:38.825 | MS1 | 121.4656640190 | 31.1446205288 | 516 | 504990 | -92.54 | 11.39 | 63.19 | 0.13 | 2.59 | 1586 |
| 2024-09-20 22:21:39.890 | MS1 | 121.4656618747 | 31.1446369921 | 516 | 504990 | -92.73 | 7.37 | 59.91 | 0.14 | 2.59 | 1572 |
| 2024-09-20 22:21:40.892 | MS1 | 121.4656730138 | 31.1446267346 | 516 | 504990 | -91.81 | 11.71 | 386.09 | 0.08 | 3.00 | 1577 |
| 2024-09-20 22:21:41.290 | MS1 | 121.4656763247 | 31.1446207048 | 516 | 504990 | -93.55 | 11.76 | 580.53 | 0.04 | 2.96 | 1565 |
| 2024-09-20 22:21:42.452 | MS1 | 121.4656609876 | 31.1446249994 | 516 | 504990 | -91.73 | 8.75 | 399.36 | 0.05 | 2.91 | 1594 |

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
| 3240048 | 1 | 121.4690529738 | 31.1543651790 | 250 | 13 | 12 | 16.1 | TDD | 516 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3241344 | 2 | 121.4702840872 | 31.1522561170 | 89 | 5 | 7 | 39.2 | TDD | 639 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3265668 | 3 | 121.4684708642 | 31.1440235812 | 141 | 14 | 3 | 43.2 | TDD | 36 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3271160 | 4 | 121.4750910734 | 31.1487539794 | 304 | 14 | 8 | 26.9 | TDD | 655 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |

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
| 2024-09-20 22:21:31.411 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.429 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.565 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.565 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.304 | NREventA3 | measId:2;ServCellPCI:15;Ser... |
| 2024-09-20 22:21:38.544 | NRHandoverAttempt | SourcePCI:15;SourceNR-ARFCN... |
| 2024-09-20 22:21:38.591 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.604 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.724 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.724 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3240048 | 1 | 86.0245 | 89.2651 | -117.0775 | 10.8418 | 181.6039 | 0.0006 | 0.0182 |
| 2024_09_19 22:00 | 3241344 | 2 | 78.5833 | 81.4287 | -115.5001 | 17.8179 | 129.5416 | 0.0183 | 0.0044 |
| 2024_09_19 22:00 | 3265668 | 3 | 92.9949 | 92.6629 | -114.5931 | 6.7438 | 106.9279 | 0.0107 | 0.0061 |
| 2024_09_19 22:00 | 3271160 | 4 | 79.8081 | 83.3213 | -114.4504 | 9.4130 | 162.5405 | 0.0019 | 0.0128 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414863_B4BE9A65 | 504990 | 516 | -90.1 | 504990 | 36 | -93.7 | 504990 | 639 | -102.5 | 504990 | 655 |
| MR_1774414863_54C9BFA3 | 504990 | 516 | -88.7 | 504990 | 36 | -95.8 | 504990 | 639 | -100.1 | 504990 | 655 |
| MR_1774414863_E5786416 | 504990 | 516 | -91.2 | 504990 | 36 | -95.2 | 504990 | 639 | -103.2 | 504990 | 655 |
| MR_1774414863_5B297C5B | 504990 | 516 | -89.7 | 504990 | 36 | -95.2 | 504990 | 639 | -101.4 | 504990 | 655 |
| MR_1774414863_7B2E3D42 | 504990 | 516 | -89.6 | 504990 | 36 | -95.2 | 504990 | 639 | -101.9 | 504990 | 655 |
| MR_1774414863_834F3E28 | 504990 | 516 | -88.1 | 504990 | 36 | -94.3 | 504990 | 639 | -101.3 | 504990 | 655 |
| MR_1774414863_BDA94F50 | 504990 | 516 | -89.0 | 504990 | 36 | -96.6 | 504990 | 639 | -103.4 | 504990 | 655 |
| MR_1774414863_F16E94D1 | 504990 | 516 | -89.4 | 504990 | 36 | -92.9 | 504990 | 639 | -99.7 | 504990 | 655 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 581: `a0083fc1-776...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `a0083fc1-776b-4309-9a12-e49839adbfa8` |
| Tag | **single-answer** |
| 정답 | **C14** |
| C14 의미 | Decrease A3 Offset threshold for 3272562_2 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[581] topology](images/train_0581.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3229124_4
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3229124_4
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3272562_2
- `C4`: Adjust the azimuth of 3272562_2 by 5 degrees
- `C5`: Adjust the azimuth of 3229124_4 by 28 degrees
- `C6`: Increase transmission power for 3229124_4
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3272562_2
- `C8`: Add neighbor relationship between 3272562_2 and 3229124_4
- `C9`: Increase transmission power for 3272562_2
- `C10`: Add neighbor relationship between 3211349_3 and 3229124_4
- `C11`: Lift the tilt angle  of 3229124_4 by 10 degrees
- `C12`: Check test server and transmission issues
- `C13`: Insufficient data; more data is needed for judgment.
- `C14`: Decrease A3 Offset threshold for 3272562_2 **← 정답**
- `C15`: Decrease transmission power for 3229124_4
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3229124_4
- `C17`: Press down the tilt angle  of 3229124_4 by 10 degrees
- `C18`: Lift the tilt angle of 3272562_2 by 5 degrees
- `C19`: Press down the tilt angle of 3272562_2 by 5 degrees
- `C20`: Increase A3 Offset threshold for 3272562_2
- `C21`: Decrease transmission power for 3272562_2
- `C22`: Decrease A3 Offset threshold for 3229124_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.988 | MS1 | 121.4656677561 | 31.1446275939 | 852 | 504990 | -83.72 | 14.25 | 466.21 | 0.10 | 2.99 | 1569 |
| 2024-09-20 22:21:32.713 | MS1 | 121.4656688856 | 31.1446217191 | 852 | 504990 | -75.10 | 13.53 | 479.52 | 0.03 | 2.50 | 1581 |
| 2024-09-20 22:21:33.889 | MS1 | 121.4656595264 | 31.1446221363 | 852 | 504990 | -83.55 | 17.22 | 556.36 | 0.07 | 2.23 | 1583 |
| 2024-09-20 22:21:34.210 | MS1 | 121.4656769233 | 31.1446274906 | 852 | 504990 | -86.64 | -0.74 | 50.23 | 0.16 | 1.32 | 1563 |
| 2024-09-20 22:21:35.612 | MS1 | 121.4656773616 | 31.1446370480 | 852 | 504990 | -90.43 | -0.19 | 39.77 | 0.14 | 1.29 | 1596 |
| 2024-09-20 22:21:36.395 | MS1 | 121.4656768267 | 31.1446207559 | 852 | 504990 | -89.54 | -2.78 | 79.76 | 0.04 | 1.11 | 1560 |
| 2024-09-20 22:21:37.608 | MS1 | 121.4656700483 | 31.1446215385 | 852 | 504990 | -92.61 | -1.98 | 40.26 | 0.09 | 1.19 | 1583 |
| 2024-09-20 22:21:38.128 | MS1 | 121.4656727429 | 31.1446252437 | 852 | 504990 | -89.05 | -2.77 | 74.88 | 0.18 | 1.04 | 1598 |
| 2024-09-20 22:21:39.712 | MS1 | 121.4656605026 | 31.1446349961 | 588 | 504990 | -79.57 | 17.94 | 209.32 | 0.15 | 1.45 | 1575 |
| 2024-09-20 22:21:40.804 | MS1 | 121.4656733946 | 31.1446239159 | 588 | 504990 | -76.14 | 13.71 | 494.74 | 0.08 | 2.82 | 1570 |
| 2024-09-20 22:21:41.970 | MS1 | 121.4656610684 | 31.1446232673 | 588 | 504990 | -77.43 | 12.62 | 537.46 | 0.02 | 2.76 | 1591 |
| 2024-09-20 22:21:42.364 | MS1 | 121.4656714691 | 31.1446233483 | 588 | 504990 | -78.46 | 15.80 | 345.39 | 0.20 | 2.47 | 1571 |

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
| 3211349 | 3 | 121.4673329429 | 31.1552537876 | 259 | 2 | 10 | 21.1 | TDD | 998 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3229124 | 4 | 121.4648365833 | 31.1542017524 | 148 | 12 | 12 | 42.6 | TDD | 588 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3230683 | 1 | 121.4725821009 | 31.1450591945 | 164 | 2 | 9 | 21.8 | TDD | 713 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3272562 | 2 | 121.4670619383 | 31.1486036298 | 202 | 3 | 9 | 16.9 | TDD | 852 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:31.329 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.349 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.450 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.450 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.199 | NREventA3 | measId:2;ServCellPCI:438;Se... |
| 2024-09-20 22:21:38.439 | NRHandoverAttempt | SourcePCI:438;SourceNR-ARFC... |
| 2024-09-20 22:21:38.488 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.503 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.610 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.610 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3230683 | 1 | 11.9311 | 6.9622 | -115.8780 | 5.8807 | 117.0326 | 0.0178 | 0.0111 |
| 2024_09_20 22:00 | 3272562 | 2 | 11.7619 | 13.1620 | -114.3577 | 18.6429 | 172.8101 | 0.0191 | 0.1815 |
| 2024_09_20 22:00 | 3211349 | 3 | 6.6617 | 15.5763 | -114.0008 | 14.9164 | 138.5930 | 0.0093 | 0.0086 |
| 2024_09_20 22:00 | 3229124 | 4 | 19.7227 | 5.4129 | -115.3851 | 8.1821 | 164.7639 | 0.0187 | 0.0109 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417097_127C2B45 | 504990 | 852 | -87.9 | 504990 | 588 | -79.4 | 504990 | 998 | -92.5 | 504990 | 713 |
| MR_1774417097_DC764945 | 504990 | 852 | -87.3 | 504990 | 588 | -82.6 | 504990 | 998 | -90.7 | 504990 | 713 |
| MR_1774417097_74D580A6 | 504990 | 852 | -85.3 | 504990 | 588 | -81.1 | 504990 | 998 | -90.7 | 504990 | 713 |
| MR_1774417097_7F771C24 | 504990 | 852 | -88.5 | 504990 | 588 | -81.8 | 504990 | 998 | -90.9 | 504990 | 713 |
| MR_1774417097_BE7858C6 | 504990 | 588 | -82.2 | 504990 | 852 | -87.4 | 504990 | 998 | -92.2 | 504990 | 713 |
| MR_1774417097_A4A9BB30 | 504990 | 588 | -79.2 | 504990 | 852 | -85.2 | 504990 | 998 | -89.9 | 504990 | 713 |
| MR_1774417097_B018E02D | 504990 | 852 | -85.1 | 504990 | 588 | -82.7 | 504990 | 998 | -89.0 | 504990 | 713 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 582: `ece2d7aa-3c2...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `ece2d7aa-3c2b-444d-bc32-24e1b746be3e` |
| Tag | **multiple-answer** |
| 정답 | **C5|C12** |
| C5 의미 | Increase transmission power for 3211072_1 |
| C12 의미 | Adjust the azimuth of 3211072_1 by 50 degrees |
| 패턴 분류 | **P4 Coverage (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[582] topology](images/train_0582.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3233400_4
- `C2`: Decrease A3 Offset threshold for 3233400_4
- `C3`: Increase A3 Offset threshold for 3211072_1
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3211072_1
- `C5`: Increase transmission power for 3211072_1 **← 정답**
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3233400_4
- `C7`: Increase A3 Offset threshold for 3233400_4
- `C8`: Decrease A3 Offset threshold for 3211072_1
- `C9`: Press down the tilt angle  of 3233400_4 by 6 degrees
- `C10`: Insufficient data; more data is needed for judgment.
- `C11`: Lift the tilt angle of 3211072_1 by 10 degrees
- `C12`: Adjust the azimuth of 3211072_1 by 50 degrees **← 정답**
- `C13`: Check test server and transmission issues
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3233400_4
- `C15`: Decrease transmission power for 3211072_1
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3211072_1
- `C17`: Add neighbor relationship between 3211072_1 and 3233400_4
- `C18`: Press down the tilt angle of 3211072_1 by 10 degrees
- `C19`: Decrease transmission power for 3233400_4
- `C20`: Adjust the azimuth of 3233400_4 by 22 degrees
- `C21`: Add neighbor relationship between 3229164_3 and 3233400_4
- `C22`: Lift the tilt angle  of 3233400_4 by 6 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.627 | MS1 | 121.4656688152 | 31.1446261810 | 659 | 504990 | -90.48 | 15.69 | 430.28 | 0.03 | 2.49 | 1561 |
| 2024-09-20 22:21:32.344 | MS1 | 121.4656681531 | 31.1446302039 | 659 | 504990 | -93.88 | 13.95 | 588.33 | 0.19 | 2.01 | 1581 |
| 2024-09-20 22:21:33.644 | MS1 | 121.4656766115 | 31.1446269106 | 659 | 504990 | -86.38 | 12.94 | 543.32 | 0.16 | 2.61 | 1572 |
| 2024-09-20 22:21:34.449 | MS1 | 121.4656717211 | 31.1446207403 | 659 | 504990 | -109.40 | -0.41 | 41.25 | 0.06 | 1.28 | 1580 |
| 2024-09-20 22:21:35.317 | MS1 | 121.4656695806 | 31.1446343716 | 659 | 504990 | -101.21 | -1.27 | 43.85 | 0.17 | 1.26 | 1575 |
| 2024-09-20 22:21:36.878 | MS1 | 121.4656616207 | 31.1446227781 | 659 | 504990 | -101.75 | -1.96 | 37.45 | 0.11 | 1.16 | 1570 |
| 2024-09-20 22:21:37.481 | MS1 | 121.4656751681 | 31.1446193887 | 659 | 504990 | -106.28 | 0.02 | 57.26 | 0.05 | 1.22 | 1571 |
| 2024-09-20 22:21:38.380 | MS1 | 121.4656601494 | 31.1446192580 | 659 | 504990 | -103.36 | 1.97 | 41.80 | 0.04 | 1.28 | 1597 |
| 2024-09-20 22:21:39.742 | MS1 | 121.4656677902 | 31.1446347862 | 659 | 504990 | -108.06 | 0.67 | 69.32 | 0.17 | 1.35 | 1581 |
| 2024-09-20 22:21:40.680 | MS1 | 121.4656706948 | 31.1446355821 | 659 | 504990 | -88.99 | 14.61 | 571.30 | 0.10 | 2.11 | 1600 |
| 2024-09-20 22:21:41.379 | MS1 | 121.4656752926 | 31.1446199547 | 659 | 504990 | -93.12 | 16.70 | 544.50 | 0.01 | 3.00 | 1567 |
| 2024-09-20 22:21:42.908 | MS1 | 121.4656654075 | 31.1446311483 | 659 | 504990 | -93.64 | 16.37 | 424.95 | 0.20 | 2.42 | 1574 |

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
| 3211072 | 1 | 121.4688645573 | 31.1463092782 | 296 | 6 | 6 | 25.3 | TDD | 659 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3216438 | 2 | 121.4661226201 | 31.1513844763 | 151 | 7 | 1 | 28.5 | TDD | 716 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3229164 | 3 | 121.4703872803 | 31.1553468657 | 278 | 1 | 7 | 39.2 | TDD | 292 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3233400 | 4 | 121.4697992869 | 31.1549076195 | 177 | 5 | 3 | 16.5 | TDD | 807 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |

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
| 2024-09-20 22:21:30.785 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.806 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:30.913 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.913 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.163 | NREventA2 | measId:1;ServCellPCI:194;Se... |
| 2024-09-20 22:21:34.280 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3211072 | 1 | 19.0420 | 18.5594 | -114.0944 | 16.4950 | 120.6574 | 0.1166 | 0.0104 |
| 2024_09_20 22:00 | 3216438 | 2 | 18.8146 | 17.3452 | -114.7197 | 17.1511 | 130.0687 | 0.0170 | 0.0115 |
| 2024_09_20 22:00 | 3229164 | 3 | 11.8075 | 11.5960 | -115.6065 | 19.4286 | 171.5173 | 0.0050 | 0.0143 |
| 2024_09_20 22:00 | 3233400 | 4 | 15.5383 | 7.4699 | -117.4561 | 12.8941 | 81.2092 | 0.0042 | 0.0103 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416554_9779005C | 504990 | 659 | -109.9 | 504990 | 807 | -116.1 | 504990 | 292 | -120.2 | 504990 | 716 |
| MR_1774416554_8184B977 | 504990 | 659 | -107.8 | 504990 | 807 | -116.2 | 504990 | 292 | -117.7 | 504990 | 716 |
| MR_1774416554_1864E623 | 504990 | 659 | -109.4 | 504990 | 807 | -115.6 | 504990 | 292 | -120.0 | 504990 | 716 |
| MR_1774416554_00632154 | 504990 | 659 | -111.0 | 504990 | 807 | -114.9 | 504990 | 292 | -117.6 | 504990 | 716 |
| MR_1774416554_9FB201E1 | 504990 | 659 | -107.9 | 504990 | 807 | -116.9 | 504990 | 292 | -119.9 | 504990 | 716 |
| MR_1774416554_7954B55A | 504990 | 659 | -108.2 | 504990 | 807 | -116.1 | 504990 | 292 | -120.0 | 504990 | 716 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 583: `0c87b3c3-7e5...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `0c87b3c3-7e5d-4d87-ba04-4f2ed4829a27` |
| Tag | **multiple-answer** |
| 정답 | **C18|C19** |
| C18 의미 | Increase transmission power for 3243952_1 |
| C19 의미 | Adjust the azimuth of 3243952_1 by 50 degrees |
| 패턴 분류 | **P4 Coverage (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[583] topology](images/train_0583.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3243320_3
- `C2`: Decrease transmission power for 3243952_1
- `C3`: Add neighbor relationship between 3211434_2 and 3243320_3
- `C4`: Decrease transmission power for 3243320_3
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3243320_3
- `C6`: Add neighbor relationship between 3243952_1 and 3243320_3
- `C7`: Press down the tilt angle of 3243952_1 by 4 degrees
- `C8`: Lift the tilt angle of 3243952_1 by 4 degrees
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3243952_1
- `C10`: Lift the tilt angle  of 3243320_3 by 2 degrees
- `C11`: Adjust the azimuth of 3243320_3 by 24 degrees
- `C12`: Press down the tilt angle  of 3243320_3 by 2 degrees
- `C13`: Increase A3 Offset threshold for 3243952_1
- `C14`: Decrease A3 Offset threshold for 3243320_3
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3243320_3
- `C16`: Increase transmission power for 3243320_3
- `C17`: Check test server and transmission issues
- `C18`: Increase transmission power for 3243952_1 **← 정답**
- `C19`: Adjust the azimuth of 3243952_1 by 50 degrees **← 정답**
- `C20`: Decrease A3 Offset threshold for 3243952_1
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3243952_1
- `C22`: Insufficient data; more data is needed for judgment.

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.492 | MS1 | 121.4656658098 | 31.1446261035 | 394 | 504990 | -85.09 | 12.76 | 474.76 | 0.06 | 2.68 | 1571 |
| 2024-09-20 22:21:32.273 | MS1 | 121.4656739140 | 31.1446198283 | 394 | 504990 | -93.81 | 14.16 | 381.43 | 0.07 | 2.00 | 1566 |
| 2024-09-20 22:21:33.777 | MS1 | 121.4656720021 | 31.1446374105 | 394 | 504990 | -94.42 | 12.52 | 468.21 | 0.16 | 2.66 | 1573 |
| 2024-09-20 22:21:34.184 | MS1 | 121.4656646798 | 31.1446206223 | 394 | 504990 | -101.06 | -1.88 | 70.98 | 0.03 | 1.01 | 1579 |
| 2024-09-20 22:21:35.251 | MS1 | 121.4656581890 | 31.1446336592 | 394 | 504990 | -104.20 | -0.08 | 45.78 | 0.07 | 1.34 | 1577 |
| 2024-09-20 22:21:36.108 | MS1 | 121.4656708559 | 31.1446348615 | 394 | 504990 | -107.72 | -1.93 | 62.50 | 0.03 | 1.26 | 1600 |
| 2024-09-20 22:21:37.364 | MS1 | 121.4656733049 | 31.1446254873 | 394 | 504990 | -104.31 | -0.16 | 39.18 | 0.10 | 1.14 | 1560 |
| 2024-09-20 22:21:38.710 | MS1 | 121.4656692855 | 31.1446352049 | 394 | 504990 | -101.72 | 0.52 | 57.32 | 0.17 | 1.38 | 1589 |
| 2024-09-20 22:21:39.589 | MS1 | 121.4656758450 | 31.1446359411 | 394 | 504990 | -106.85 | -0.39 | 50.88 | 0.18 | 1.27 | 1560 |
| 2024-09-20 22:21:40.539 | MS1 | 121.4656756622 | 31.1446356977 | 394 | 504990 | -93.19 | 15.63 | 535.51 | 0.16 | 2.39 | 1564 |
| 2024-09-20 22:21:41.209 | MS1 | 121.4656669511 | 31.1446228294 | 394 | 504990 | -87.71 | 13.19 | 436.34 | 0.06 | 2.75 | 1583 |
| 2024-09-20 22:21:42.647 | MS1 | 121.4656728307 | 31.1446237121 | 394 | 504990 | -91.82 | 13.74 | 339.64 | 0.03 | 2.24 | 1565 |

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
| 3211434 | 2 | 121.4751545094 | 31.1475553717 | 182 | 7 | 8 | 36.3 | TDD | 755 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3229479 | 4 | 121.4733631118 | 31.1473682975 | 219 | 12 | 10 | 42.6 | TDD | 540 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3243320 | 3 | 121.4667251186 | 31.1499590766 | 166 | 0 | 12 | 19.3 | TDD | 764 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3243952 | 1 | 121.4738561771 | 31.1501724347 | 290 | 3 | 11 | 20.0 | TDD | 394 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

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
| 2024-09-20 22:21:30.964 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.986 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.116 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.116 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.283 | NREventA2 | measId:1;ServCellPCI:37;Ser... |
| 2024-09-20 22:21:34.420 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3243952 | 1 | 19.1223 | 19.8597 | -117.3179 | 9.3634 | 159.7043 | 0.1526 | 0.0021 |
| 2024_09_20 22:00 | 3211434 | 2 | 19.8920 | 10.9976 | -114.8972 | 5.3789 | 94.0108 | 0.0058 | 0.0146 |
| 2024_09_20 22:00 | 3243320 | 3 | 16.2843 | 18.6930 | -117.7494 | 12.0517 | 98.9416 | 0.0113 | 0.0125 |
| 2024_09_20 22:00 | 3229479 | 4 | 7.8399 | 16.3032 | -116.1740 | 12.9475 | 169.4147 | 0.0006 | 0.0185 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415978_A6F58030 | 504990 | 394 | -100.4 | 504990 | 764 | -103.4 | 504990 | 755 | -110.1 | 504990 | 540 |
| MR_1774415978_0514F643 | 504990 | 394 | -101.0 | 504990 | 764 | -103.9 | 504990 | 755 | -111.0 | 504990 | 540 |
| MR_1774415978_45BFFD5E | 504990 | 394 | -100.1 | 504990 | 764 | -103.6 | 504990 | 755 | -110.2 | 504990 | 540 |
| MR_1774415978_2CA7A586 | 504990 | 394 | -102.6 | 504990 | 764 | -103.3 | 504990 | 755 | -110.3 | 504990 | 540 |
| MR_1774415978_C8D1BE52 | 504990 | 394 | -101.5 | 504990 | 764 | -103.5 | 504990 | 755 | -110.5 | 504990 | 540 |
| MR_1774415978_FC68AB51 | 504990 | 394 | -99.3 | 504990 | 764 | -104.2 | 504990 | 755 | -111.2 | 504990 | 540 |
| MR_1774415978_C73E8871 | 504990 | 394 | -102.6 | 504990 | 764 | -103.5 | 504990 | 755 | -109.5 | 504990 | 540 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 584: `f28c1f2f-5e4...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `f28c1f2f-5e4d-4c35-b9ed-3735e09e8747` |
| Tag | **single-answer** |
| 정답 | **C1** |
| C1 의미 | Decrease A3 Offset threshold for 3264227_4 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[584] topology](images/train_0584.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3264227_4 **← 정답**
- `C2`: Lift the tilt angle of 3264227_4 by 10 degrees
- `C3`: Add neighbor relationship between 3215266_1 and 3255250_2
- `C4`: Decrease transmission power for 3255250_2
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3264227_4
- `C6`: Decrease A3 Offset threshold for 3255250_2
- `C7`: Increase A3 Offset threshold for 3255250_2
- `C8`: Increase transmission power for 3255250_2
- `C9`: Adjust the azimuth of 3264227_4 by 50 degrees
- `C10`: Adjust the azimuth of 3255250_2 by 50 degrees
- `C11`: Insufficient data; more data is needed for judgment.
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3255250_2
- `C13`: Increase transmission power for 3264227_4
- `C14`: Press down the tilt angle  of 3255250_2 by 10 degrees
- `C15`: Check test server and transmission issues
- `C16`: Add neighbor relationship between 3264227_4 and 3255250_2
- `C17`: Press down the tilt angle of 3264227_4 by 10 degrees
- `C18`: Increase A3 Offset threshold for 3264227_4
- `C19`: Lift the tilt angle  of 3255250_2 by 10 degrees
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3264227_4
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3255250_2
- `C22`: Decrease transmission power for 3264227_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.545 | MS1 | 121.4656621120 | 31.1446351188 | 626 | 504990 | -80.65 | 12.86 | 303.68 | 0.14 | 2.86 | 1564 |
| 2024-09-20 22:21:32.943 | MS1 | 121.4656618996 | 31.1446258528 | 626 | 504990 | -76.31 | 16.05 | 333.85 | 0.01 | 2.67 | 1595 |
| 2024-09-20 22:21:33.315 | MS1 | 121.4656699493 | 31.1446295918 | 626 | 504990 | -78.63 | 15.90 | 434.89 | 0.03 | 2.03 | 1568 |
| 2024-09-20 22:21:34.320 | MS1 | 121.4656594918 | 31.1446193162 | 626 | 504990 | -88.03 | -0.55 | 31.88 | 0.13 | 1.48 | 1585 |
| 2024-09-20 22:21:35.352 | MS1 | 121.4656750457 | 31.1446298459 | 626 | 504990 | -91.35 | -0.53 | 43.73 | 0.10 | 1.30 | 1595 |
| 2024-09-20 22:21:36.640 | MS1 | 121.4656665773 | 31.1446306083 | 626 | 504990 | -83.10 | -1.77 | 60.89 | 0.06 | 1.06 | 1570 |
| 2024-09-20 22:21:37.168 | MS1 | 121.4656644069 | 31.1446214700 | 626 | 504990 | -91.08 | -2.61 | 46.16 | 0.15 | 1.18 | 1563 |
| 2024-09-20 22:21:38.179 | MS1 | 121.4656603263 | 31.1446295416 | 626 | 504990 | -90.60 | -1.03 | 74.04 | 0.03 | 1.47 | 1570 |
| 2024-09-20 22:21:39.366 | MS1 | 121.4656692575 | 31.1446192723 | 338 | 504990 | -80.97 | 14.90 | 237.62 | 0.20 | 1.46 | 1591 |
| 2024-09-20 22:21:40.658 | MS1 | 121.4656750585 | 31.1446292580 | 338 | 504990 | -78.04 | 16.88 | 430.38 | 0.19 | 2.35 | 1584 |
| 2024-09-20 22:21:41.674 | MS1 | 121.4656639903 | 31.1446181043 | 338 | 504990 | -82.57 | 13.67 | 308.79 | 0.01 | 2.89 | 1581 |
| 2024-09-20 22:21:42.913 | MS1 | 121.4656737918 | 31.1446359038 | 338 | 504990 | -78.74 | 12.30 | 393.84 | 0.11 | 2.15 | 1573 |

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
| 3215266 | 1 | 121.4702030493 | 31.1443427850 | 336 | 3 | 3 | 32.9 | TDD | 194 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3232030 | 3 | 121.4699025724 | 31.1445893174 | 290 | 6 | 7 | 22.5 | TDD | 965 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3255250 | 2 | 121.4735893083 | 31.1525857604 | 63 | 13 | 3 | 27.2 | TDD | 338 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3264227 | 4 | 121.4656248547 | 31.1488067150 | 258 | 9 | 12 | 29.0 | TDD | 626 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |

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
| 2024-09-20 22:21:30.753 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.777 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:30.902 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.902 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.645 | NREventA3 | measId:2;ServCellPCI:139;Se... |
| 2024-09-20 22:21:37.885 | NRHandoverAttempt | SourcePCI:139;SourceNR-ARFC... |
| 2024-09-20 22:21:37.918 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.930 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.071 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.071 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3215266 | 1 | 6.8048 | 17.6718 | -116.2315 | 9.9473 | 138.0888 | 0.0121 | 0.0085 |
| 2024_09_20 22:00 | 3255250 | 2 | 7.7676 | 7.4290 | -117.0799 | 7.3589 | 188.6785 | 0.0083 | 0.0036 |
| 2024_09_20 22:00 | 3232030 | 3 | 17.7795 | 9.2607 | -116.4969 | 8.5380 | 96.9439 | 0.0121 | 0.0136 |
| 2024_09_20 22:00 | 3264227 | 4 | 8.9984 | 8.8354 | -117.1044 | 18.5783 | 104.3451 | 0.0134 | 0.1409 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416701_060332C5 | 504990 | 626 | -86.4 | 504990 | 338 | -82.2 | 504990 | 194 | -85.2 | 504990 | 965 |
| MR_1774416701_31C90AEF | 504990 | 338 | -82.5 | 504990 | 626 | -87.4 | 504990 | 194 | -87.0 | 504990 | 965 |
| MR_1774416701_982E3201 | 504990 | 626 | -88.5 | 504990 | 338 | -81.9 | 504990 | 194 | -85.7 | 504990 | 965 |
| MR_1774416701_5B8FB8AB | 504990 | 338 | -82.6 | 504990 | 626 | -89.2 | 504990 | 194 | -86.4 | 504990 | 965 |
| MR_1774416701_BE7E40B4 | 504990 | 626 | -88.9 | 504990 | 338 | -84.1 | 504990 | 194 | -86.6 | 504990 | 965 |
| MR_1774416701_4C4F5F10 | 504990 | 626 | -89.0 | 504990 | 338 | -84.3 | 504990 | 194 | -85.0 | 504990 | 965 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 585: `6faf3c03-07e...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `6faf3c03-07ea-4d8a-a75a-00259df40935` |
| Tag | **single-answer** |
| 정답 | **C5** |
| C5 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3254622_3 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[585] topology](images/train_0585.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Check test server and transmission issues
- `C2`: Decrease A3 Offset threshold for 3254622_3
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3274250_1
- `C4`: Lift the tilt angle of 3254622_3 by 0 degrees
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3254622_3 **← 정답**
- `C6`: Increase A3 Offset threshold for 3274250_1
- `C7`: Add neighbor relationship between 3261479_9 and 3274250_1
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3254622_3
- `C9`: Add neighbor relationship between 3254622_3 and 3274250_1
- `C10`: Increase A3 Offset threshold for 3254622_3
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3274250_1
- `C12`: Increase transmission power for 3274250_1
- `C13`: Decrease transmission power for 3254622_3
- `C14`: Adjust the azimuth of 3274250_1 by 1 degrees
- `C15`: Insufficient data; more data is needed for judgment.
- `C16`: Decrease A3 Offset threshold for 3274250_1
- `C17`: Lift the tilt angle  of 3274250_1 by 5 degrees
- `C18`: Adjust the azimuth of 3254622_3 by 36 degrees
- `C19`: Increase transmission power for 3254622_3
- `C20`: Press down the tilt angle of 3254622_3 by 0 degrees
- `C21`: Decrease transmission power for 3274250_1
- `C22`: Press down the tilt angle  of 3274250_1 by 5 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.783 | MS1 | 121.4656748099 | 31.1446248867 | 682 | 504990 | -93.22 | 14.91 | 358.65 | 0.19 | 2.71 | 1571 |
| 2024-09-20 22:21:32.830 | MS1 | 121.4656639499 | 31.1446215390 | 666 | 504990 | -95.85 | 9.91 | 490.42 | 0.12 | 2.69 | 1590 |
| 2024-09-20 22:21:33.592 | MS1 | 121.4656738132 | 31.1446247754 | 44 | 504990 | -93.44 | 9.85 | 462.73 | 0.06 | 2.30 | 1596 |
| 2024-09-20 22:21:34.846 | MS1 | 121.4656721664 | 31.1446259040 | 586 | 152650 | -92.80 | 2.54 | 78.11 | 0.15 | 1.68 | 991 |
| 2024-09-20 22:21:35.988 | MS1 | 121.4656675540 | 31.1446275794 | 264 | 152650 | -94.08 | 3.27 | 103.51 | 0.01 | 1.83 | 980 |
| 2024-09-20 22:21:36.702 | MS1 | 121.4656629782 | 31.1446214391 | 360 | 152650 | -90.41 | 3.46 | 74.51 | 0.10 | 1.77 | 924 |
| 2024-09-20 22:21:37.899 | MS1 | 121.4656634876 | 31.1446275489 | 714 | 152650 | -95.36 | 7.77 | 91.09 | 0.03 | 1.62 | 903 |
| 2024-09-20 22:21:38.841 | MS1 | 121.4656765659 | 31.1446321570 | 586 | 152650 | -88.51 | 6.65 | 102.64 | 0.07 | 1.94 | 990 |
| 2024-09-20 22:21:39.971 | MS1 | 121.4656771316 | 31.1446323278 | 264 | 152650 | -91.54 | 3.65 | 82.48 | 0.04 | 1.61 | 943 |
| 2024-09-20 22:21:40.671 | MS1 | 121.4656753790 | 31.1446276641 | 360 | 152650 | -92.97 | 3.81 | 82.11 | 0.06 | 2.79 | 1593 |
| 2024-09-20 22:21:41.562 | MS1 | 121.4656741994 | 31.1446294298 | 714 | 152650 | -96.08 | 4.68 | 83.91 | 0.11 | 2.45 | 1568 |
| 2024-09-20 22:21:42.488 | MS1 | 121.4656636443 | 31.1446217352 | 586 | 152650 | -91.08 | 7.33 | 72.58 | 0.10 | 2.08 | 1573 |

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
| 3210019 | 8 | 121.4699548733 | 31.1516500246 | 41 | 6 | 9 | 5.2 | FDD | 264 | n1 | 152650 | 30M | 4T4R | 12 | 152650 |
| 3218153 | 11 | 121.4688270475 | 31.1456081599 | 239 | 15 | 1 | 25.3 | FDD | 586 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |
| 3226192 | 10 | 121.4644265701 | 31.1534784677 | 259 | 13 | 0 | 22.4 | FDD | 714 | n1 | 152650 | 30M | 4T4R | 25 | 152650 |
| 3228762 | 4 | 121.4691446132 | 31.1453282894 | 24 | 10 | 10 | 5.6 | TDD | 44 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3231481 | 7 | 121.4684448334 | 31.1466121379 | 117 | 0 | 2 | 19.1 | FDD | 390 | n1 | 152650 | 30M | 4T4R | 30 | 152650 |
| 3240281 | 6 | 121.4688866690 | 31.1482786635 | 341 | 1 | 0 | 29.1 | TDD | 666 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3246621 | 12 | 121.4717641458 | 31.1559036316 | 71 | 11 | 5 | 9.3 | FDD | 303 | n1 | 152650 | 30M | 4T4R | 14 | 152650 |
| 3253542 | 5 | 121.4723993557 | 31.1545246748 | 251 | 7 | 6 | 27.2 | TDD | 915 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3254622 | 3 | 121.4759245772 | 31.1454754340 | 300 | 0 | 10 | 7.4 | TDD | 682 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3255658 | 13 | 121.4691576515 | 31.1454843966 | 136 | 3 | 2 | 10.4 | FDD | 783 | n1 | 152650 | 30M | 4T4R | 29 | 152650 |
| 3261479 | 9 | 121.4658172672 | 31.1475169548 | 238 | 8 | 0 | 10.4 | FDD | 360 | n1 | 152650 | 30M | 4T4R | 14 | 152650 |
| 3267869 | 2 | 121.4731987341 | 31.1513647973 | 215 | 10 | 4 | 1.3 | TDD | 234 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3274250 | 1 | 121.4676960669 | 31.1471943962 | 213 | 0 | 4 | 27.2 | TDD | 867 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |

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
| 2024-09-20 22:21:30.832 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.857 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:30.999 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.999 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.642 | NREventA2 | measId:1;ServCellPCI:887;Se... |
| 2024-09-20 22:21:34.780 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.047 | NREventA5 | measId:3;ServCellPCI:887;Se... |
| 2024-09-20 22:21:35.102 | NRHandoverAttempt | SourcePCI:887;SourceNR-ARFC... |
| 2024-09-20 22:21:35.125 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.138 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:35.240 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.240 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3274250 | 1 | 14.0487 | 14.9888 | -117.0577 | 8.2785 | 150.3141 | 0.0029 | 0.0093 |
| 2024_09_20 22:00 | 3267869 | 2 | 6.6451 | 14.6649 | -116.3293 | 15.3595 | 171.6044 | 0.0160 | 0.0161 |
| 2024_09_20 22:00 | 3254622 | 3 | 9.1447 | 19.0020 | -114.9670 | 15.3491 | 172.9701 | 0.0189 | 0.0027 |
| 2024_09_20 22:00 | 3228762 | 4 | 12.4882 | 7.5808 | -116.4744 | 14.5192 | 164.7221 | 0.0122 | 0.0184 |
| 2024_09_20 22:00 | 3253542 | 5 | 17.9051 | 5.9713 | -116.2605 | 11.8460 | 125.5540 | 0.0100 | 0.0091 |
| 2024_09_20 22:00 | 3240281 | 6 | 16.7769 | 13.3511 | -117.0808 | 12.6170 | 192.3909 | 0.0096 | 0.0016 |
| 2024_09_20 22:00 | 3231481 | 7 | 6.6775 | 18.9796 | -117.7177 | 4.5147 | 37.6760 | 0.0001 | 0.0116 |
| 2024_09_20 22:00 | 3210019 | 8 | 17.7739 | 15.9233 | -114.9866 | 4.6568 | 59.4777 | 0.0081 | 0.0063 |
| 2024_09_20 22:00 | 3261479 | 9 | 19.9442 | 12.2516 | -116.3693 | 3.8665 | 46.0684 | 0.0056 | 0.0176 |
| 2024_09_20 22:00 | 3226192 | 10 | 17.0108 | 16.1109 | -114.7955 | 3.2237 | 28.7770 | 0.0102 | 0.0029 |
| 2024_09_20 22:00 | 3218153 | 11 | 17.2474 | 5.4397 | -114.2967 | 4.5056 | 40.4477 | 0.0021 | 0.0130 |
| 2024_09_20 22:00 | 3246621 | 12 | 7.9375 | 8.9220 | -115.1354 | 4.6071 | 55.2910 | 0.0084 | 0.0047 |
| 2024_09_20 22:00 | 3255658 | 13 | 9.7620 | 7.6135 | -117.9390 | 4.5835 | 29.9497 | 0.0113 | 0.0192 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415853_87AAD86E | 504990 | 44 | -93.3 | 504990 | 867 | -94.6 | 504990 | 234 | -99.2 | 504990 | 915 |
| MR_1774415853_B4E18DD6 | 152650 | 586 | -94.5 | 152650 | 303 | -93.4 | 152650 | 390 | -101.5 | 152650 | 783 |
| MR_1774415853_E3FDB6C6 | 504990 | 44 | -92.8 | 504990 | 867 | -93.2 | 504990 | 234 | -101.4 | 504990 | 915 |
| MR_1774415853_56002F4F | 152650 | 586 | -94.1 | 152650 | 303 | -96.3 | 152650 | 390 | -101.7 | 152650 | 783 |
| MR_1774415853_03EAE9EA | 504990 | 44 | -92.8 | 504990 | 867 | -94.5 | 504990 | 234 | -100.8 | 504990 | 915 |
| MR_1774415853_0680DC45 | 152650 | 586 | -91.7 | 152650 | 303 | -97.0 | 152650 | 390 | -101.9 | 152650 | 783 |
| MR_1774415853_5C7C195F | 504990 | 44 | -93.4 | 504990 | 867 | -92.3 | 504990 | 234 | -98.8 | 504990 | 915 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 586: `c709b75c-a87...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `c709b75c-a871-4bb0-a58d-b55b02e37efc` |
| Tag | **multiple-answer** |
| 정답 | **C4|C11** |
| C4 의미 | Adjust the azimuth of 3250350_3 by 50 degrees |
| C11 의미 | Increase transmission power for 3250350_3 |
| 패턴 분류 | **P4 Coverage (azimuth)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[586] topology](images/train_0586.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3250350_3 by 10 degrees
- `C2`: Add neighbor relationship between 3250350_3 and 3233164_2
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3250350_3
- `C4`: Adjust the azimuth of 3250350_3 by 50 degrees **← 정답**
- `C5`: Press down the tilt angle of 3250350_3 by 10 degrees
- `C6`: Add neighbor relationship between 3264573_4 and 3233164_2
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3233164_2
- `C8`: Decrease transmission power for 3250350_3
- `C9`: Decrease transmission power for 3233164_2
- `C10`: Insufficient data; more data is needed for judgment.
- `C11`: Increase transmission power for 3250350_3 **← 정답**
- `C12`: Check test server and transmission issues
- `C13`: Press down the tilt angle  of 3233164_2 by 4 degrees
- `C14`: Lift the tilt angle  of 3233164_2 by 4 degrees
- `C15`: Adjust the azimuth of 3233164_2 by 8 degrees
- `C16`: Increase A3 Offset threshold for 3233164_2
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3233164_2
- `C18`: Decrease A3 Offset threshold for 3233164_2
- `C19`: Increase transmission power for 3233164_2
- `C20`: Increase A3 Offset threshold for 3250350_3
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3250350_3
- `C22`: Decrease A3 Offset threshold for 3250350_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.707 | MS1 | 121.4656621517 | 31.1446303038 | 598 | 504990 | -87.08 | 13.78 | 503.42 | 0.04 | 2.90 | 1581 |
| 2024-09-20 22:21:32.420 | MS1 | 121.4656656141 | 31.1446313658 | 598 | 504990 | -89.01 | 13.00 | 485.35 | 0.07 | 2.77 | 1593 |
| 2024-09-20 22:21:33.221 | MS1 | 121.4656758801 | 31.1446317004 | 598 | 504990 | -94.71 | 13.95 | 431.24 | 0.08 | 2.09 | 1587 |
| 2024-09-20 22:21:34.509 | MS1 | 121.4656596464 | 31.1446349804 | 598 | 504990 | -108.48 | -0.95 | 65.43 | 0.03 | 1.46 | 1592 |
| 2024-09-20 22:21:35.720 | MS1 | 121.4656767568 | 31.1446260726 | 598 | 504990 | -104.24 | 0.04 | 63.10 | 0.04 | 1.13 | 1571 |
| 2024-09-20 22:21:36.224 | MS1 | 121.4656742365 | 31.1446200007 | 598 | 504990 | -105.48 | 0.78 | 61.31 | 0.15 | 1.36 | 1583 |
| 2024-09-20 22:21:37.650 | MS1 | 121.4656695004 | 31.1446212963 | 598 | 504990 | -101.67 | 1.97 | 75.79 | 0.01 | 1.23 | 1561 |
| 2024-09-20 22:21:38.134 | MS1 | 121.4656693771 | 31.1446218430 | 598 | 504990 | -102.85 | 1.79 | 27.75 | 0.02 | 1.22 | 1598 |
| 2024-09-20 22:21:39.525 | MS1 | 121.4656778325 | 31.1446244242 | 598 | 504990 | -107.82 | 0.16 | 51.53 | 0.18 | 1.39 | 1576 |
| 2024-09-20 22:21:40.108 | MS1 | 121.4656776239 | 31.1446364699 | 598 | 504990 | -85.24 | 15.72 | 550.44 | 0.00 | 2.47 | 1577 |
| 2024-09-20 22:21:41.829 | MS1 | 121.4656598673 | 31.1446373558 | 598 | 504990 | -86.35 | 13.64 | 381.67 | 0.19 | 2.03 | 1590 |
| 2024-09-20 22:21:42.848 | MS1 | 121.4656598345 | 31.1446282845 | 598 | 504990 | -94.35 | 17.95 | 322.67 | 0.08 | 2.39 | 1560 |

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
| 3219842 | 1 | 121.4736632309 | 31.1480035787 | 71 | 14 | 2 | 37.4 | TDD | 264 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3233164 | 2 | 121.4647099966 | 31.1516099929 | 165 | 1 | 9 | 47.3 | TDD | 45 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3250350 | 3 | 121.4716241505 | 31.1443317557 | 348 | 14 | 2 | 46.2 | TDD | 598 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3264573 | 4 | 121.4682807481 | 31.1477444686 | 311 | 15 | 5 | 19.0 | TDD | 742 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |

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
| 2024-09-20 22:21:31.208 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.224 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.354 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.354 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.580 | NREventA2 | measId:1;ServCellPCI:302;Se... |
| 2024-09-20 22:21:34.707 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3219842 | 1 | 15.4026 | 6.9011 | -115.4101 | 13.6679 | 177.9831 | 0.0145 | 0.0183 |
| 2024_09_20 22:00 | 3233164 | 2 | 18.7109 | 12.8632 | -116.0916 | 9.4511 | 149.0189 | 0.0182 | 0.0110 |
| 2024_09_20 22:00 | 3250350 | 3 | 7.9295 | 12.9417 | -116.1851 | 6.8254 | 121.0168 | 0.1528 | 0.0157 |
| 2024_09_20 22:00 | 3264573 | 4 | 9.2411 | 15.5882 | -116.3450 | 10.4426 | 93.3485 | 0.0039 | 0.0111 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412459_98682B9F | 504990 | 598 | -108.8 | 504990 | 45 | -115.1 | 504990 | 742 | -123.7 | 504990 | 264 |
| MR_1774412459_A1DB6E12 | 504990 | 598 | -106.7 | 504990 | 45 | -114.6 | 504990 | 742 | -121.0 | 504990 | 264 |
| MR_1774412459_0319858E | 504990 | 598 | -108.3 | 504990 | 45 | -115.5 | 504990 | 742 | -121.4 | 504990 | 264 |
| MR_1774412459_EE61AEAC | 504990 | 598 | -107.4 | 504990 | 45 | -114.7 | 504990 | 742 | -122.5 | 504990 | 264 |
| MR_1774412459_B19B408D | 504990 | 598 | -107.0 | 504990 | 45 | -117.1 | 504990 | 742 | -124.2 | 504990 | 264 |
| MR_1774412459_394BCA14 | 504990 | 598 | -110.3 | 504990 | 45 | -118.0 | 504990 | 742 | -124.2 | 504990 | 264 |
| MR_1774412459_DE90E62E | 504990 | 598 | -106.5 | 504990 | 45 | -116.6 | 504990 | 742 | -120.9 | 504990 | 264 |
| MR_1774412459_C68BCF3B | 504990 | 598 | -109.1 | 504990 | 45 | -114.5 | 504990 | 742 | -123.9 | 504990 | 264 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 587: `0a0f387d-0f9...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `0a0f387d-0f96-48a5-8fb4-9701bbfba516` |
| Tag | **single-answer** |
| 정답 | **C6** |
| C6 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3259562_3 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[587] topology](images/train_0587.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3259562_3 by 2 degrees
- `C2`: Adjust the azimuth of 3242627_5 by 8 degrees
- `C3`: Add neighbor relationship between 3237025_11 and 3242627_5
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3242627_5
- `C5`: Adjust the azimuth of 3259562_3 by 31 degrees
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3259562_3 **← 정답**
- `C7`: Press down the tilt angle of 3259562_3 by 2 degrees
- `C8`: Decrease A3 Offset threshold for 3242627_5
- `C9`: Lift the tilt angle  of 3242627_5 by 1 degrees
- `C10`: Increase A3 Offset threshold for 3259562_3
- `C11`: Increase transmission power for 3259562_3
- `C12`: Decrease A3 Offset threshold for 3259562_3
- `C13`: Press down the tilt angle  of 3242627_5 by 1 degrees
- `C14`: Increase A3 Offset threshold for 3242627_5
- `C15`: Check test server and transmission issues
- `C16`: Increase transmission power for 3242627_5
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3259562_3
- `C18`: Decrease transmission power for 3242627_5
- `C19`: Insufficient data; more data is needed for judgment.
- `C20`: Decrease transmission power for 3259562_3
- `C21`: Add neighbor relationship between 3259562_3 and 3242627_5
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3242627_5

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.453 | MS1 | 121.4656711607 | 31.1446190597 | 402 | 504990 | -95.68 | 11.42 | 598.56 | 0.03 | 2.32 | 1569 |
| 2024-09-20 22:21:32.288 | MS1 | 121.4656747087 | 31.1446287772 | 183 | 504990 | -95.15 | 14.06 | 347.89 | 0.04 | 2.74 | 1590 |
| 2024-09-20 22:21:33.677 | MS1 | 121.4656687073 | 31.1446234577 | 90 | 504990 | -95.64 | 11.23 | 369.14 | 0.12 | 2.59 | 1589 |
| 2024-09-20 22:21:34.847 | MS1 | 121.4656638998 | 31.1446347461 | 180 | 152650 | -94.04 | 2.81 | 83.63 | 0.15 | 1.54 | 919 |
| 2024-09-20 22:21:35.520 | MS1 | 121.4656752466 | 31.1446245366 | 618 | 152650 | -92.72 | 4.99 | 86.44 | 0.10 | 1.66 | 936 |
| 2024-09-20 22:21:36.461 | MS1 | 121.4656666210 | 31.1446200189 | 626 | 152650 | -96.09 | 7.73 | 75.55 | 0.19 | 1.92 | 936 |
| 2024-09-20 22:21:37.836 | MS1 | 121.4656724254 | 31.1446345147 | 363 | 152650 | -93.31 | 2.38 | 70.84 | 0.07 | 2.00 | 994 |
| 2024-09-20 22:21:38.469 | MS1 | 121.4656771992 | 31.1446245361 | 180 | 152650 | -88.58 | 6.48 | 62.79 | 0.00 | 1.78 | 924 |
| 2024-09-20 22:21:39.839 | MS1 | 121.4656737978 | 31.1446350544 | 618 | 152650 | -93.47 | 7.28 | 93.32 | 0.10 | 1.55 | 979 |
| 2024-09-20 22:21:40.917 | MS1 | 121.4656622201 | 31.1446301572 | 626 | 152650 | -94.28 | 3.49 | 56.24 | 0.20 | 2.64 | 1590 |
| 2024-09-20 22:21:41.625 | MS1 | 121.4656776537 | 31.1446307352 | 363 | 152650 | -90.62 | 4.10 | 65.53 | 0.15 | 2.98 | 1573 |
| 2024-09-20 22:21:42.486 | MS1 | 121.4656652010 | 31.1446186412 | 180 | 152650 | -93.16 | 2.78 | 75.44 | 0.10 | 2.95 | 1579 |

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
| 3225523 | 1 | 121.4696229872 | 31.1482388671 | 146 | 5 | 12 | 7.5 | TDD | 261 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3229564 | 13 | 121.4703044925 | 31.1499036328 | 289 | 1 | 5 | 23.5 | FDD | 948 | n1 | 152650 | 30M | 4T4R | 15 | 152650 |
| 3235191 | 7 | 121.4694970312 | 31.1476766665 | 332 | 0 | 10 | 20.4 | FDD | 262 | n1 | 152650 | 30M | 4T4R | 22 | 152650 |
| 3237025 | 11 | 121.4685960800 | 31.1484279385 | 1 | 0 | 3 | 1.5 | FDD | 626 | n1 | 152650 | 30M | 4T4R | 23 | 152650 |
| 3237319 | 4 | 121.4720477706 | 31.1508972017 | 281 | 13 | 10 | 21.0 | TDD | 183 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3242627 | 5 | 121.4738267867 | 31.1537363641 | 210 | 1 | 9 | 7.2 | TDD | 794 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3245681 | 12 | 121.4685104794 | 31.1507858725 | 71 | 8 | 1 | 17.5 | FDD | 180 | n1 | 152650 | 30M | 4T4R | 26 | 152650 |
| 3257885 | 10 | 121.4743443880 | 31.1440636879 | 55 | 0 | 7 | 7.9 | FDD | 332 | n1 | 152650 | 30M | 4T4R | 26 | 152650 |
| 3259562 | 3 | 121.4699513998 | 31.1552196155 | 168 | 2 | 0 | 8.9 | TDD | 402 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3263889 | 9 | 121.4745644300 | 31.1461138025 | 192 | 14 | 3 | 8.9 | FDD | 363 | n1 | 152650 | 30M | 4T4R | 26 | 152650 |
| 3267043 | 8 | 121.4686368123 | 31.1475588040 | 201 | 2 | 1 | 20.3 | FDD | 618 | n1 | 152650 | 30M | 4T4R | 11 | 152650 |
| 3267094 | 6 | 121.4736464195 | 31.1548899429 | 322 | 5 | 8 | 6.9 | TDD | 220 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3278231 | 2 | 121.4710571822 | 31.1519539663 | 59 | 1 | 7 | 1.6 | TDD | 90 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |

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
| 2024-09-20 22:21:30.786 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.804 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:30.913 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.913 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.670 | NREventA2 | measId:1;ServCellPCI:379;Se... |
| 2024-09-20 22:21:34.795 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.058 | NREventA5 | measId:3;ServCellPCI:379;Se... |
| 2024-09-20 22:21:35.125 | NRHandoverAttempt | SourcePCI:379;SourceNR-ARFC... |
| 2024-09-20 22:21:35.155 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.169 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:35.278 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.278 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3225523 | 1 | 7.8993 | 8.1144 | -115.4314 | 17.8511 | 145.6959 | 0.0068 | 0.0123 |
| 2024_09_20 22:00 | 3278231 | 2 | 16.0214 | 6.3978 | -116.9366 | 6.4059 | 82.8433 | 0.0146 | 0.0016 |
| 2024_09_20 22:00 | 3259562 | 3 | 10.0058 | 11.0329 | -116.7829 | 10.0771 | 199.8943 | 0.0022 | 0.0098 |
| 2024_09_20 22:00 | 3237319 | 4 | 5.6787 | 11.1517 | -115.1243 | 17.5193 | 187.4846 | 0.0005 | 0.0019 |
| 2024_09_20 22:00 | 3242627 | 5 | 6.9534 | 9.6977 | -117.5247 | 8.7078 | 171.6868 | 0.0190 | 0.0007 |
| 2024_09_20 22:00 | 3267094 | 6 | 7.7680 | 13.2524 | -115.3450 | 15.1996 | 112.0973 | 0.0168 | 0.0073 |
| 2024_09_20 22:00 | 3235191 | 7 | 18.1168 | 11.6142 | -117.4686 | 3.6266 | 45.9852 | 0.0094 | 0.0197 |
| 2024_09_20 22:00 | 3267043 | 8 | 7.4902 | 10.7552 | -114.9614 | 4.9100 | 47.0238 | 0.0103 | 0.0162 |
| 2024_09_20 22:00 | 3263889 | 9 | 19.3466 | 9.9328 | -116.4718 | 3.5935 | 52.8230 | 0.0048 | 0.0140 |
| 2024_09_20 22:00 | 3257885 | 10 | 13.1326 | 12.0383 | -114.8947 | 3.3246 | 22.3035 | 0.0007 | 0.0155 |
| 2024_09_20 22:00 | 3237025 | 11 | 10.4488 | 6.2658 | -114.1550 | 4.4340 | 33.2448 | 0.0030 | 0.0039 |
| 2024_09_20 22:00 | 3245681 | 12 | 10.0908 | 7.0791 | -115.3412 | 4.6851 | 51.2346 | 0.0148 | 0.0135 |
| 2024_09_20 22:00 | 3229564 | 13 | 17.4742 | 13.4201 | -114.3574 | 4.2486 | 26.2471 | 0.0011 | 0.0129 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412702_73DE82CF | 152650 | 180 | -94.9 | 152650 | 262 | -96.8 | 152650 | 332 | -102.8 | 152650 | 948 |
| MR_1774412702_623F983D | 504990 | 90 | -94.0 | 504990 | 794 | -97.1 | 504990 | 261 | -99.6 | 504990 | 220 |
| MR_1774412702_638AC4AA | 152650 | 180 | -94.5 | 152650 | 262 | -96.0 | 152650 | 332 | -101.9 | 152650 | 948 |
| MR_1774412702_92DE0391 | 152650 | 180 | -94.8 | 152650 | 262 | -98.3 | 152650 | 332 | -103.6 | 152650 | 948 |
| MR_1774412702_949FA5C3 | 504990 | 90 | -93.7 | 504990 | 794 | -94.5 | 504990 | 261 | -101.0 | 504990 | 220 |
| MR_1774412702_7AE81879 | 152650 | 180 | -96.0 | 152650 | 262 | -97.4 | 152650 | 332 | -104.5 | 152650 | 948 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 588: `a4b5f79c-0f9...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `a4b5f79c-0f9a-431c-89b6-1b41c2e74908` |
| Tag | **single-answer** |
| 정답 | **C12** |
| C12 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[588] topology](images/train_0588.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Check test server and transmission issues
- `C2`: Adjust the azimuth of 3218680_2 by 50 degrees
- `C3`: Adjust the azimuth of 3234179_1 by 50 degrees
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3218680_2
- `C5`: Decrease transmission power for 3234179_1
- `C6`: Add neighbor relationship between 3218680_2 and 3234179_1
- `C7`: Add neighbor relationship between 3267612_4 and 3234179_1
- `C8`: Press down the tilt angle  of 3234179_1 by 3 degrees
- `C9`: Increase transmission power for 3218680_2
- `C10`: Increase transmission power for 3234179_1
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3218680_2
- `C12`: Insufficient data; more data is needed for judgment. **← 정답**
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3234179_1
- `C14`: Lift the tilt angle  of 3234179_1 by 3 degrees
- `C15`: Press down the tilt angle of 3218680_2 by 10 degrees
- `C16`: Decrease transmission power for 3218680_2
- `C17`: Increase A3 Offset threshold for 3234179_1
- `C18`: Increase A3 Offset threshold for 3218680_2
- `C19`: Lift the tilt angle of 3218680_2 by 10 degrees
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3234179_1
- `C21`: Decrease A3 Offset threshold for 3234179_1
- `C22`: Decrease A3 Offset threshold for 3218680_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.572 | MS1 | 121.4656632380 | 31.1446378659 | 788 | 504990 | -87.98 | 12.01 | 514.37 | 0.14 | 2.36 | 1598 |
| 2024-09-20 22:21:32.151 | MS1 | 121.4656615874 | 31.1446246521 | 788 | 504990 | -89.01 | 12.33 | 375.18 | 0.07 | 2.46 | 1591 |
| 2024-09-20 22:21:33.768 | MS1 | 121.4656772243 | 31.1446318270 | 788 | 504990 | -88.12 | 14.25 | 383.96 | 0.09 | 2.63 | 1595 |
| 2024-09-20 22:21:34.576 | MS1 | 121.4656682651 | 31.1446189943 | 788 | 504990 | -89.11 | 15.78 | 69.74 | 0.03 | 2.90 | 1569 |
| 2024-09-20 22:21:35.680 | MS1 | 121.4656624485 | 31.1446185018 | 788 | 504990 | -90.50 | 14.25 | 59.18 | 0.15 | 2.86 | 1575 |
| 2024-09-20 22:21:36.532 | MS1 | 121.4656676152 | 31.1446287548 | 788 | 504990 | -90.74 | 16.79 | 58.90 | 0.14 | 2.88 | 1590 |
| 2024-09-20 22:21:37.609 | MS1 | 121.4656738630 | 31.1446309184 | 788 | 504990 | -89.40 | 9.54 | 41.30 | 0.02 | 2.19 | 1569 |
| 2024-09-20 22:21:38.997 | MS1 | 121.4656655554 | 31.1446318879 | 788 | 504990 | -92.36 | 8.27 | 98.52 | 0.10 | 2.88 | 1589 |
| 2024-09-20 22:21:39.452 | MS1 | 121.4656657516 | 31.1446344220 | 788 | 504990 | -93.29 | 7.14 | 74.62 | 0.11 | 2.36 | 1576 |
| 2024-09-20 22:21:40.579 | MS1 | 121.4656700616 | 31.1446317429 | 788 | 504990 | -90.65 | 9.81 | 365.16 | 0.16 | 2.79 | 1579 |
| 2024-09-20 22:21:41.433 | MS1 | 121.4656648618 | 31.1446228498 | 788 | 504990 | -89.27 | 9.18 | 586.85 | 0.14 | 2.96 | 1588 |
| 2024-09-20 22:21:42.716 | MS1 | 121.4656672213 | 31.1446311671 | 788 | 504990 | -89.57 | 8.54 | 386.16 | 0.05 | 2.60 | 1566 |

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
| 3218680 | 2 | 121.4648313606 | 31.1546790222 | 359 | 9 | 3 | 38.3 | TDD | 788 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3234179 | 1 | 121.4743285172 | 31.1493907555 | 88 | 1 | 8 | 39.5 | TDD | 729 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3267612 | 4 | 121.4707225776 | 31.1469209600 | 211 | 9 | 8 | 18.1 | TDD | 567 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3269937 | 3 | 121.4758201531 | 31.1537095143 | 39 | 14 | 1 | 23.4 | TDD | 281 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:31.447 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.463 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.601 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.601 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.307 | NREventA3 | measId:2;ServCellPCI:127;Se... |
| 2024-09-20 22:21:38.547 | NRHandoverAttempt | SourcePCI:127;SourceNR-ARFC... |
| 2024-09-20 22:21:38.589 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.602 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.718 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.718 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3234179 | 1 | 92.6785 | 88.4576 | -114.6748 | 5.7947 | 99.6588 | 0.0022 | 0.0057 |
| 2024_09_19 22:00 | 3218680 | 2 | 89.0960 | 85.3233 | -117.3663 | 10.6619 | 109.1425 | 0.0130 | 0.0133 |
| 2024_09_19 22:00 | 3269937 | 3 | 76.3069 | 90.1982 | -114.2465 | 18.5761 | 197.8884 | 0.0071 | 0.0088 |
| 2024_09_19 22:00 | 3267612 | 4 | 91.7289 | 90.8659 | -114.4962 | 7.0970 | 126.7598 | 0.0091 | 0.0054 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414524_47A9E4CC | 504990 | 788 | -90.4 | 504990 | 729 | -96.7 | 504990 | 567 | -103.9 | 504990 | 281 |
| MR_1774414524_9D46E211 | 504990 | 788 | -89.9 | 504990 | 729 | -95.5 | 504990 | 567 | -100.5 | 504990 | 281 |
| MR_1774414524_654C4D1C | 504990 | 788 | -89.7 | 504990 | 729 | -94.0 | 504990 | 567 | -101.1 | 504990 | 281 |
| MR_1774414524_EC2CD43C | 504990 | 788 | -89.3 | 504990 | 729 | -97.5 | 504990 | 567 | -103.0 | 504990 | 281 |
| MR_1774414524_C9E2CAE2 | 504990 | 788 | -89.3 | 504990 | 729 | -96.0 | 504990 | 567 | -103.2 | 504990 | 281 |
| MR_1774414524_3D0EAAB3 | 504990 | 788 | -90.3 | 504990 | 729 | -94.6 | 504990 | 567 | -102.3 | 504990 | 281 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 589: `eb290709-b15...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `eb290709-b158-46e2-8495-2755ee44398f` |
| Tag | **single-answer** |
| 정답 | **C5** |
| C5 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[589] topology](images/train_0589.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3250721_1 by 10 degrees
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3278590_3
- `C3`: Increase A3 Offset threshold for 3278590_3
- `C4`: Add neighbor relationship between 3250721_1 and 3278590_3
- `C5`: Check test server and transmission issues **← 정답**
- `C6`: Increase A3 Offset threshold for 3250721_1
- `C7`: Press down the tilt angle of 3250721_1 by 10 degrees
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3250721_1
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3250721_1
- `C10`: Lift the tilt angle  of 3278590_3 by 10 degrees
- `C11`: Decrease transmission power for 3278590_3
- `C12`: Decrease A3 Offset threshold for 3250721_1
- `C13`: Insufficient data; more data is needed for judgment.
- `C14`: Increase transmission power for 3250721_1
- `C15`: Add neighbor relationship between 3265445_2 and 3278590_3
- `C16`: Adjust the azimuth of 3250721_1 by 50 degrees
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3278590_3
- `C18`: Press down the tilt angle  of 3278590_3 by 10 degrees
- `C19`: Decrease A3 Offset threshold for 3278590_3
- `C20`: Increase transmission power for 3278590_3
- `C21`: Decrease transmission power for 3250721_1
- `C22`: Adjust the azimuth of 3278590_3 by 50 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.174 | MS1 | 121.4656640846 | 31.1446186060 | 528 | 504990 | -89.74 | 12.50 | 360.00 | 0.08 | 2.09 | 1589 |
| 2024-09-20 22:21:32.389 | MS1 | 121.4656697965 | 31.1446302672 | 528 | 504990 | -91.34 | 13.92 | 550.14 | 0.07 | 2.96 | 1572 |
| 2024-09-20 22:21:33.329 | MS1 | 121.4656670501 | 31.1446350520 | 528 | 504990 | -85.38 | 14.66 | 558.84 | 0.03 | 2.79 | 1592 |
| 2024-09-20 22:21:34.831 | MS1 | 121.4656764436 | 31.1446211246 | 528 | 504990 | -89.37 | 17.58 | 71.35 | 0.13 | 2.12 | 320 |
| 2024-09-20 22:21:35.706 | MS1 | 121.4656691420 | 31.1446329579 | 528 | 504990 | -85.31 | 12.27 | 88.97 | 0.09 | 2.76 | 474 |
| 2024-09-20 22:21:36.596 | MS1 | 121.4656758481 | 31.1446235991 | 528 | 504990 | -89.49 | 17.83 | 77.26 | 0.19 | 2.62 | 363 |
| 2024-09-20 22:21:37.866 | MS1 | 121.4656677397 | 31.1446230006 | 528 | 504990 | -91.28 | 9.80 | 86.15 | 0.09 | 2.55 | 366 |
| 2024-09-20 22:21:38.252 | MS1 | 121.4656714763 | 31.1446355006 | 528 | 504990 | -93.50 | 12.29 | 99.03 | 0.08 | 2.71 | 345 |
| 2024-09-20 22:21:39.852 | MS1 | 121.4656672391 | 31.1446243509 | 528 | 504990 | -91.74 | 10.92 | 77.37 | 0.16 | 2.17 | 455 |
| 2024-09-20 22:21:40.802 | MS1 | 121.4656654306 | 31.1446265524 | 528 | 504990 | -89.27 | 10.03 | 571.25 | 0.05 | 2.69 | 1579 |
| 2024-09-20 22:21:41.443 | MS1 | 121.4656603509 | 31.1446234333 | 528 | 504990 | -91.13 | 10.26 | 421.49 | 0.11 | 2.48 | 1566 |
| 2024-09-20 22:21:42.143 | MS1 | 121.4656754155 | 31.1446301553 | 528 | 504990 | -91.32 | 11.89 | 392.28 | 0.15 | 2.33 | 1560 |

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
| 3250721 | 1 | 121.4667989966 | 31.1457379798 | 161 | 6 | 9 | 41.9 | TDD | 528 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3265445 | 2 | 121.4654353975 | 31.1524264023 | 322 | 0 | 12 | 17.7 | TDD | 536 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3278590 | 3 | 121.4737778345 | 31.1481348973 | 188 | 8 | 3 | 23.7 | TDD | 156 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3279165 | 4 | 121.4678606542 | 31.1477094318 | 307 | 1 | 8 | 19.3 | TDD | 21 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:30.824 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.848 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:30.951 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.951 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.664 | NREventA3 | measId:2;ServCellPCI:731;Se... |
| 2024-09-20 22:21:37.904 | NRHandoverAttempt | SourcePCI:731;SourceNR-ARFC... |
| 2024-09-20 22:21:37.940 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.955 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.066 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.066 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3250721 | 1 | 12.2206 | 5.3867 | -114.5945 | 8.3099 | 94.7129 | 0.0072 | 0.0132 |
| 2024_09_20 22:00 | 3265445 | 2 | 15.7328 | 13.8581 | -117.2334 | 12.8303 | 158.4175 | 0.0041 | 0.0082 |
| 2024_09_20 22:00 | 3278590 | 3 | 5.0415 | 19.4282 | -115.0289 | 12.8945 | 192.5509 | 0.0048 | 0.0136 |
| 2024_09_20 22:00 | 3279165 | 4 | 7.1070 | 18.8388 | -114.6160 | 13.6563 | 145.9119 | 0.0114 | 0.0041 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412551_40D309E9 | 504990 | 528 | -90.0 | 504990 | 156 | -94.4 | 504990 | 536 | -103.2 | 504990 | 21 |
| MR_1774412551_209DF9AA | 504990 | 528 | -87.4 | 504990 | 156 | -92.7 | 504990 | 536 | -103.3 | 504990 | 21 |
| MR_1774412551_9E26B6A8 | 504990 | 528 | -91.1 | 504990 | 156 | -96.0 | 504990 | 536 | -104.3 | 504990 | 21 |
| MR_1774412551_0FB6DA4A | 504990 | 528 | -89.9 | 504990 | 156 | -95.8 | 504990 | 536 | -102.0 | 504990 | 21 |
| MR_1774412551_730BB4DF | 504990 | 528 | -91.1 | 504990 | 156 | -96.1 | 504990 | 536 | -102.8 | 504990 | 21 |

> *... 2개 열 생략 (전체 14열)*

---
