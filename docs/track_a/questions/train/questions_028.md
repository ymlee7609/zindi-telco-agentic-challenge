# Track A 문제 분석 — train[270]~train[279]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[270] ~ train[279] (10개)

## 목차

1. [문제 270: `c1530ef8-148...`](#270) — single-answer, 정답: C4
2. [문제 271: `0f7de029-0e8...`](#271) — single-answer, 정답: C13
3. [문제 272: `356762a5-d71...`](#272) — single-answer, 정답: C19
4. [문제 273: `83776488-ee4...`](#273) — single-answer, 정답: C20
5. [문제 274: `a21308d3-6c7...`](#274) — multiple-answer, 정답: C2|C4|C6|C8
6. [문제 275: `184d6c23-3fb...`](#275) — single-answer, 정답: C20
7. [문제 276: `f28eadd3-6c6...`](#276) — multiple-answer, 정답: C6|C8
8. [문제 277: `d03aa61f-e96...`](#277) — single-answer, 정답: C22
9. [문제 278: `34a8842c-632...`](#278) — multiple-answer, 정답: C12|C21
10. [문제 279: `9d6034a1-491...`](#279) — single-answer, 정답: C12

---

### 문제 270: `c1530ef8-148...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `c1530ef8-148b-426c-beb5-fd78ca16f808` |
| Tag | **single-answer** |
| 정답 | **C4** |
| C4 의미 | Add neighbor relationship between 3213254_2 and 3217709_1 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[270] topology](images/train_0270.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3217709_1
- `C2`: Lift the tilt angle of 3213254_2 by 1 degrees
- `C3`: Increase transmission power for 3213254_2
- `C4`: Add neighbor relationship between 3213254_2 and 3217709_1 **← 정답**
- `C5`: Adjust the azimuth of 3217709_1 by 2 degrees
- `C6`: Insufficient data; more data is needed for judgment.
- `C7`: Press down the tilt angle  of 3217709_1 by 2 degrees
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3217709_1
- `C9`: Increase transmission power for 3217709_1
- `C10`: Increase A3 Offset threshold for 3217709_1
- `C11`: Press down the tilt angle of 3213254_2 by 1 degrees
- `C12`: Decrease transmission power for 3217709_1
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3213254_2
- `C14`: Increase A3 Offset threshold for 3213254_2
- `C15`: Decrease A3 Offset threshold for 3213254_2
- `C16`: Lift the tilt angle  of 3217709_1 by 2 degrees
- `C17`: Decrease transmission power for 3213254_2
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3213254_2
- `C19`: Check test server and transmission issues
- `C20`: Adjust the azimuth of 3213254_2 by 50 degrees
- `C21`: Decrease A3 Offset threshold for 3217709_1
- `C22`: Add neighbor relationship between 3256633_3 and 3217709_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.461 | MS1 | 121.4656608251 | 31.1446367968 | 741 | 504990 | -84.50 | 17.10 | 426.36 | 0.04 | 2.35 | 1595 |
| 2024-09-20 22:21:32.449 | MS1 | 121.4656626205 | 31.1446259817 | 741 | 504990 | -80.03 | 13.85 | 583.64 | 0.05 | 2.21 | 1597 |
| 2024-09-20 22:21:33.170 | MS1 | 121.4656664767 | 31.1446187788 | 741 | 504990 | -77.79 | 14.52 | 437.52 | 0.05 | 2.59 | 1598 |
| 2024-09-20 22:21:34.709 | MS1 | 121.4656709000 | 31.1446303217 | 741 | 504990 | -94.03 | -0.16 | 72.27 | 0.10 | 1.29 | 1598 |
| 2024-09-20 22:21:35.596 | MS1 | 121.4656745703 | 31.1446354964 | 741 | 504990 | -90.31 | -3.01 | 30.82 | 0.01 | 1.49 | 1589 |
| 2024-09-20 22:21:36.583 | MS1 | 121.4656693767 | 31.1446344775 | 741 | 504990 | -91.71 | -2.56 | 41.63 | 0.18 | 1.37 | 1592 |
| 2024-09-20 22:21:37.744 | MS1 | 121.4656751079 | 31.1446318576 | 741 | 504990 | -88.99 | -2.30 | 71.90 | 0.08 | 1.38 | 1580 |
| 2024-09-20 22:21:38.650 | MS1 | 121.4656758323 | 31.1446182106 | 741 | 504990 | -81.26 | 17.66 | 303.49 | 0.17 | 1.24 | 1570 |
| 2024-09-20 22:21:39.461 | MS1 | 121.4656767977 | 31.1446196885 | 741 | 504990 | -82.64 | 16.28 | 537.91 | 0.02 | 1.44 | 1588 |
| 2024-09-20 22:21:40.759 | MS1 | 121.4656661876 | 31.1446342240 | 741 | 504990 | -76.96 | 12.29 | 504.91 | 0.10 | 2.08 | 1589 |
| 2024-09-20 22:21:41.502 | MS1 | 121.4656692209 | 31.1446318565 | 741 | 504990 | -78.65 | 14.52 | 405.20 | 0.12 | 2.51 | 1571 |
| 2024-09-20 22:21:42.230 | MS1 | 121.4656770807 | 31.1446216214 | 741 | 504990 | -75.04 | 13.40 | 477.01 | 0.06 | 2.25 | 1592 |

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
| 3210738 | 4 | 121.4655889004 | 31.1553024985 | 225 | 8 | 2 | 21.9 | TDD | 311 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3213254 | 2 | 121.4652194965 | 31.1518491647 | 240 | 0 | 2 | 16.3 | TDD | 741 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3217709 | 1 | 121.4650628768 | 31.1541491312 | 175 | 0 | 12 | 38.0 | TDD | 120 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3256633 | 3 | 121.4677973048 | 31.1528166088 | 321 | 0 | 7 | 18.8 | TDD | 893 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |

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
| 2024-09-20 22:21:31.392 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.411 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.512 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.512 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.265 | NREventA3 | measId:2;ServCellPCI:983;Se... |
| 2024-09-20 22:21:36.265 | NREventA3 | measId:2;ServCellPCI:983;Se... |
| 2024-09-20 22:21:37.265 | NREventA3 | measId:2;ServCellPCI:983;Se... |
| 2024-09-20 22:21:39.765 | NRRRCReestablishAttempt | PCI:983 |
| 2024-09-20 22:21:39.776 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.790 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:39.922 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.922 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3217709 | 1 | 9.1301 | 10.8360 | -115.2286 | 10.3744 | 84.6620 | 0.0022 | 0.0008 |
| 2024_09_20 22:00 | 3213254 | 2 | 6.5473 | 13.7947 | -115.0068 | 17.6782 | 103.4603 | 0.0020 | 0.1814 |
| 2024_09_20 22:00 | 3256633 | 3 | 11.5353 | 17.6693 | -116.2333 | 7.4264 | 136.7215 | 0.0025 | 0.0005 |
| 2024_09_20 22:00 | 3210738 | 4 | 14.8961 | 12.8803 | -114.3892 | 9.5925 | 108.3053 | 0.0187 | 0.0004 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412198_68428D23 | 504990 | 120 | -90.9 | 504990 | 741 | -94.0 | 504990 | 893 | -95.7 | 504990 | 311 |
| MR_1774412198_FBEC1A5F | 504990 | 120 | -88.4 | 504990 | 741 | -95.1 | 504990 | 893 | -94.4 | 504990 | 311 |
| MR_1774412198_3491F527 | 504990 | 120 | -91.5 | 504990 | 741 | -93.2 | 504990 | 893 | -98.1 | 504990 | 311 |
| MR_1774412198_0984C027 | 504990 | 120 | -90.3 | 504990 | 741 | -95.5 | 504990 | 893 | -98.1 | 504990 | 311 |
| MR_1774412198_4A2B4B91 | 504990 | 741 | -95.9 | 504990 | 120 | -91.9 | 504990 | 893 | -95.8 | 504990 | 311 |
| MR_1774412198_A25E0A8F | 504990 | 120 | -89.7 | 504990 | 741 | -92.9 | 504990 | 893 | -96.1 | 504990 | 311 |
| MR_1774412198_B1DE0404 | 504990 | 741 | -92.2 | 504990 | 120 | -88.1 | 504990 | 893 | -97.2 | 504990 | 311 |
| MR_1774412198_BD3768BB | 504990 | 120 | -90.5 | 504990 | 741 | -93.7 | 504990 | 893 | -97.7 | 504990 | 311 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 271: `0f7de029-0e8...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `0f7de029-0e83-4f6e-8aac-e8130c545672` |
| Tag | **single-answer** |
| 정답 | **C13** |
| C13 의미 | Add neighbor relationship between 3223623_2 and 3214475_1 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[271] topology](images/train_0271.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3223623_2
- `C2`: Adjust the azimuth of 3223623_2 by 50 degrees
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3223623_2
- `C4`: Lift the tilt angle  of 3214475_1 by 5 degrees
- `C5`: Increase A3 Offset threshold for 3223623_2
- `C6`: Decrease transmission power for 3223623_2
- `C7`: Adjust the azimuth of 3214475_1 by 13 degrees
- `C8`: Increase transmission power for 3214475_1
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3214475_1
- `C10`: Press down the tilt angle of 3223623_2 by 10 degrees
- `C11`: Add neighbor relationship between 3258897_3 and 3214475_1
- `C12`: Decrease A3 Offset threshold for 3223623_2
- `C13`: Add neighbor relationship between 3223623_2 and 3214475_1 **← 정답**
- `C14`: Decrease transmission power for 3214475_1
- `C15`: Increase A3 Offset threshold for 3214475_1
- `C16`: Increase transmission power for 3223623_2
- `C17`: Lift the tilt angle of 3223623_2 by 10 degrees
- `C18`: Press down the tilt angle  of 3214475_1 by 5 degrees
- `C19`: Decrease A3 Offset threshold for 3214475_1
- `C20`: Insufficient data; more data is needed for judgment.
- `C21`: Check test server and transmission issues
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3214475_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.524 | MS1 | 121.4656685454 | 31.1446248364 | 617 | 504990 | -79.62 | 13.40 | 398.74 | 0.17 | 2.57 | 1562 |
| 2024-09-20 22:21:32.311 | MS1 | 121.4656754459 | 31.1446371789 | 617 | 504990 | -75.15 | 17.43 | 559.77 | 0.07 | 2.50 | 1596 |
| 2024-09-20 22:21:33.269 | MS1 | 121.4656683266 | 31.1446359047 | 617 | 504990 | -76.64 | 16.73 | 419.32 | 0.16 | 2.33 | 1592 |
| 2024-09-20 22:21:34.121 | MS1 | 121.4656581817 | 31.1446202159 | 617 | 504990 | -90.04 | -3.54 | 68.58 | 0.06 | 1.04 | 1561 |
| 2024-09-20 22:21:35.320 | MS1 | 121.4656648597 | 31.1446339904 | 617 | 504990 | -93.05 | -2.33 | 35.57 | 0.10 | 1.24 | 1595 |
| 2024-09-20 22:21:36.953 | MS1 | 121.4656725215 | 31.1446273376 | 617 | 504990 | -91.66 | -0.91 | 56.08 | 0.19 | 1.17 | 1561 |
| 2024-09-20 22:21:37.652 | MS1 | 121.4656727350 | 31.1446337930 | 617 | 504990 | -85.25 | -0.43 | 32.09 | 0.19 | 1.17 | 1566 |
| 2024-09-20 22:21:38.985 | MS1 | 121.4656733560 | 31.1446354643 | 617 | 504990 | -84.46 | 13.06 | 513.31 | 0.07 | 1.36 | 1597 |
| 2024-09-20 22:21:39.470 | MS1 | 121.4656778277 | 31.1446224350 | 617 | 504990 | -75.40 | 13.87 | 588.37 | 0.17 | 1.02 | 1600 |
| 2024-09-20 22:21:40.224 | MS1 | 121.4656716241 | 31.1446296402 | 617 | 504990 | -75.22 | 16.50 | 352.23 | 0.10 | 2.14 | 1583 |
| 2024-09-20 22:21:41.690 | MS1 | 121.4656756181 | 31.1446261179 | 617 | 504990 | -78.83 | 15.93 | 508.10 | 0.17 | 2.52 | 1564 |
| 2024-09-20 22:21:42.577 | MS1 | 121.4656749864 | 31.1446280002 | 617 | 504990 | -79.53 | 13.60 | 472.91 | 0.13 | 2.13 | 1584 |

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
| 3214475 | 1 | 121.4696284479 | 31.1440549814 | 293 | 0 | 11 | 35.1 | TDD | 504 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3223623 | 2 | 121.4642612641 | 31.1442747812 | 352 | 11 | 9 | 23.2 | TDD | 617 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3258897 | 3 | 121.4719359235 | 31.1502802554 | 188 | 9 | 2 | 28.2 | TDD | 130 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3275814 | 4 | 121.4742722506 | 31.1511682288 | 341 | 15 | 10 | 40.4 | TDD | 373 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |

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
| 2024-09-20 22:21:31.318 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.339 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.482 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.482 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.173 | NREventA3 | measId:2;ServCellPCI:546;Se... |
| 2024-09-20 22:21:36.173 | NREventA3 | measId:2;ServCellPCI:546;Se... |
| 2024-09-20 22:21:37.173 | NREventA3 | measId:2;ServCellPCI:546;Se... |
| 2024-09-20 22:21:39.673 | NRRRCReestablishAttempt | PCI:546 |
| 2024-09-20 22:21:39.687 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.700 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:39.840 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.840 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3214475 | 1 | 6.7726 | 6.6320 | -114.5296 | 17.3119 | 167.0903 | 0.0157 | 0.0006 |
| 2024_09_20 22:00 | 3223623 | 2 | 7.9839 | 13.7979 | -116.3820 | 7.8072 | 158.3907 | 0.0121 | 0.1374 |
| 2024_09_20 22:00 | 3258897 | 3 | 9.8185 | 11.8543 | -114.6521 | 7.4054 | 86.8197 | 0.0180 | 0.0175 |
| 2024_09_20 22:00 | 3275814 | 4 | 9.9783 | 6.1574 | -114.8111 | 7.0345 | 187.4506 | 0.0083 | 0.0050 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412965_25245240 | 504990 | 504 | -87.0 | 504990 | 617 | -91.6 | 504990 | 130 | -94.1 | 504990 | 373 |
| MR_1774412965_49B8BCEB | 504990 | 504 | -84.4 | 504990 | 617 | -89.1 | 504990 | 130 | -94.8 | 504990 | 373 |
| MR_1774412965_DC7A7CBF | 504990 | 617 | -89.0 | 504990 | 504 | -86.5 | 504990 | 130 | -91.3 | 504990 | 373 |
| MR_1774412965_65B89D1E | 504990 | 617 | -89.6 | 504990 | 504 | -84.8 | 504990 | 130 | -92.4 | 504990 | 373 |
| MR_1774412965_4BD85AB7 | 504990 | 504 | -84.5 | 504990 | 617 | -91.8 | 504990 | 130 | -94.7 | 504990 | 373 |
| MR_1774412965_63074A25 | 504990 | 504 | -85.1 | 504990 | 617 | -88.1 | 504990 | 130 | -91.1 | 504990 | 373 |
| MR_1774412965_A9DB09CD | 504990 | 504 | -84.7 | 504990 | 617 | -88.3 | 504990 | 130 | -93.1 | 504990 | 373 |
| MR_1774412965_19CE3887 | 504990 | 504 | -87.6 | 504990 | 617 | -91.4 | 504990 | 130 | -92.9 | 504990 | 373 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 272: `356762a5-d71...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `356762a5-d71a-4a25-a247-96a556612b43` |
| Tag | **single-answer** |
| 정답 | **C19** |
| C19 의미 | Add neighbor relationship between 3227658_1 and 3239292_2 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[272] topology](images/train_0272.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Check test server and transmission issues
- `C2`: Press down the tilt angle  of 3239292_2 by 6 degrees
- `C3`: Decrease A3 Offset threshold for 3227658_1
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3239292_2
- `C5`: Press down the tilt angle of 3227658_1 by 2 degrees
- `C6`: Increase A3 Offset threshold for 3227658_1
- `C7`: Increase transmission power for 3239292_2
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3239292_2
- `C9`: Adjust the azimuth of 3239292_2 by 10 degrees
- `C10`: Lift the tilt angle of 3227658_1 by 2 degrees
- `C11`: Increase transmission power for 3227658_1
- `C12`: Lift the tilt angle  of 3239292_2 by 6 degrees
- `C13`: Adjust the azimuth of 3227658_1 by 50 degrees
- `C14`: Increase A3 Offset threshold for 3239292_2
- `C15`: Decrease transmission power for 3227658_1
- `C16`: Add neighbor relationship between 3262912_3 and 3239292_2
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3227658_1
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3227658_1
- `C19`: Add neighbor relationship between 3227658_1 and 3239292_2 **← 정답**
- `C20`: Decrease transmission power for 3239292_2
- `C21`: Decrease A3 Offset threshold for 3239292_2
- `C22`: Insufficient data; more data is needed for judgment.

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.190 | MS1 | 121.4656674680 | 31.1446208056 | 448 | 504990 | -77.16 | 12.20 | 355.54 | 0.07 | 2.00 | 1587 |
| 2024-09-20 22:21:32.876 | MS1 | 121.4656751009 | 31.1446310391 | 448 | 504990 | -81.89 | 14.52 | 512.37 | 0.05 | 2.54 | 1596 |
| 2024-09-20 22:21:33.131 | MS1 | 121.4656623468 | 31.1446302195 | 448 | 504990 | -81.28 | 16.85 | 486.65 | 0.08 | 2.77 | 1571 |
| 2024-09-20 22:21:34.799 | MS1 | 121.4656759177 | 31.1446370586 | 448 | 504990 | -93.11 | -1.19 | 58.23 | 0.11 | 1.43 | 1562 |
| 2024-09-20 22:21:35.600 | MS1 | 121.4656670969 | 31.1446284360 | 448 | 504990 | -94.93 | -3.96 | 42.17 | 0.06 | 1.24 | 1565 |
| 2024-09-20 22:21:36.502 | MS1 | 121.4656713685 | 31.1446228021 | 448 | 504990 | -87.61 | -0.31 | 29.89 | 0.19 | 1.38 | 1564 |
| 2024-09-20 22:21:37.752 | MS1 | 121.4656689765 | 31.1446286540 | 448 | 504990 | -90.25 | -2.98 | 54.19 | 0.14 | 1.46 | 1563 |
| 2024-09-20 22:21:38.910 | MS1 | 121.4656686026 | 31.1446371133 | 448 | 504990 | -79.49 | 14.70 | 532.31 | 0.16 | 1.12 | 1589 |
| 2024-09-20 22:21:39.896 | MS1 | 121.4656744418 | 31.1446271712 | 448 | 504990 | -75.77 | 15.46 | 512.85 | 0.10 | 1.25 | 1560 |
| 2024-09-20 22:21:40.106 | MS1 | 121.4656613376 | 31.1446271764 | 448 | 504990 | -84.18 | 13.83 | 496.14 | 0.12 | 2.95 | 1570 |
| 2024-09-20 22:21:41.879 | MS1 | 121.4656603922 | 31.1446246693 | 448 | 504990 | -81.64 | 15.57 | 373.98 | 0.04 | 2.59 | 1582 |
| 2024-09-20 22:21:42.686 | MS1 | 121.4656679645 | 31.1446219966 | 448 | 504990 | -81.53 | 17.64 | 299.66 | 0.07 | 2.30 | 1591 |

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
| 3227658 | 1 | 121.4664952692 | 31.1509369535 | 8 | 1 | 11 | 16.6 | TDD | 448 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3239292 | 2 | 121.4725098766 | 31.1455931658 | 251 | 4 | 2 | 17.8 | TDD | 91 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3262912 | 3 | 121.4642838821 | 31.1528111674 | 61 | 13 | 6 | 43.5 | TDD | 142 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3278639 | 4 | 121.4690193098 | 31.1469937673 | 14 | 0 | 3 | 43.7 | TDD | 447 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:31.375 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.397 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.540 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.540 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.259 | NREventA3 | measId:2;ServCellPCI:197;Se... |
| 2024-09-20 22:21:36.259 | NREventA3 | measId:2;ServCellPCI:197;Se... |
| 2024-09-20 22:21:37.259 | NREventA3 | measId:2;ServCellPCI:197;Se... |
| 2024-09-20 22:21:39.759 | NRRRCReestablishAttempt | PCI:197 |
| 2024-09-20 22:21:39.769 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.779 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:39.901 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.901 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3227658 | 1 | 10.8830 | 6.6702 | -114.0022 | 6.7773 | 107.6282 | 0.0090 | 0.1108 |
| 2024_09_20 22:00 | 3239292 | 2 | 12.3946 | 5.5241 | -115.7456 | 11.5058 | 124.2852 | 0.0015 | 0.0033 |
| 2024_09_20 22:00 | 3262912 | 3 | 7.3908 | 16.6870 | -114.0491 | 7.3162 | 187.8120 | 0.0121 | 0.0101 |
| 2024_09_20 22:00 | 3278639 | 4 | 17.0825 | 19.5726 | -114.7767 | 5.2228 | 194.8153 | 0.0042 | 0.0100 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415066_0798C7E6 | 504990 | 448 | -91.8 | 504990 | 91 | -88.6 | 504990 | 142 | -90.8 | 504990 | 447 |
| MR_1774415066_28FF8E74 | 504990 | 91 | -88.7 | 504990 | 448 | -91.2 | 504990 | 142 | -90.0 | 504990 | 447 |
| MR_1774415066_022D01F1 | 504990 | 91 | -89.0 | 504990 | 448 | -92.7 | 504990 | 142 | -92.3 | 504990 | 447 |
| MR_1774415066_77B06D05 | 504990 | 91 | -87.7 | 504990 | 448 | -92.0 | 504990 | 142 | -89.2 | 504990 | 447 |
| MR_1774415066_6DED7DCE | 504990 | 448 | -93.8 | 504990 | 91 | -88.5 | 504990 | 142 | -89.9 | 504990 | 447 |
| MR_1774415066_A21C29C3 | 504990 | 448 | -93.8 | 504990 | 91 | -90.2 | 504990 | 142 | -90.2 | 504990 | 447 |
| MR_1774415066_48854234 | 504990 | 448 | -93.4 | 504990 | 91 | -89.8 | 504990 | 142 | -88.9 | 504990 | 447 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 273: `83776488-ee4...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `83776488-ee45-44f0-844e-f20ecfe3e221` |
| Tag | **single-answer** |
| 정답 | **C20** |
| C20 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[273] topology](images/train_0273.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3214321_3 by 10 degrees
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3214321_3
- `C3`: Add neighbor relationship between 3244504_4 and 3260608_1
- `C4`: Lift the tilt angle of 3214321_3 by 10 degrees
- `C5`: Increase transmission power for 3260608_1
- `C6`: Increase A3 Offset threshold for 3260608_1
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3260608_1
- `C8`: Decrease transmission power for 3260608_1
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3214321_3
- `C10`: Press down the tilt angle  of 3260608_1 by 6 degrees
- `C11`: Increase transmission power for 3214321_3
- `C12`: Lift the tilt angle  of 3260608_1 by 6 degrees
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3260608_1
- `C14`: Check test server and transmission issues
- `C15`: Add neighbor relationship between 3214321_3 and 3260608_1
- `C16`: Increase A3 Offset threshold for 3214321_3
- `C17`: Decrease A3 Offset threshold for 3214321_3
- `C18`: Decrease transmission power for 3214321_3
- `C19`: Adjust the azimuth of 3214321_3 by 50 degrees
- `C20`: Insufficient data; more data is needed for judgment. **← 정답**
- `C21`: Adjust the azimuth of 3260608_1 by 50 degrees
- `C22`: Decrease A3 Offset threshold for 3260608_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.222 | MS1 | 121.4656695064 | 31.1446314161 | 974 | 504990 | -87.20 | 12.03 | 573.17 | 0.06 | 2.10 | 1576 |
| 2024-09-20 22:21:32.425 | MS1 | 121.4656647057 | 31.1446284910 | 974 | 504990 | -89.09 | 13.19 | 303.21 | 0.16 | 2.31 | 1578 |
| 2024-09-20 22:21:33.777 | MS1 | 121.4656774944 | 31.1446330068 | 974 | 504990 | -89.21 | 14.69 | 316.07 | 0.07 | 2.59 | 1573 |
| 2024-09-20 22:21:34.518 | MS1 | 121.4656685571 | 31.1446190236 | 974 | 504990 | -89.31 | 15.78 | 74.08 | 0.13 | 2.38 | 1578 |
| 2024-09-20 22:21:35.817 | MS1 | 121.4656658380 | 31.1446283866 | 974 | 504990 | -89.13 | 17.87 | 89.29 | 0.01 | 2.61 | 1561 |
| 2024-09-20 22:21:36.166 | MS1 | 121.4656690319 | 31.1446274034 | 974 | 504990 | -88.51 | 17.75 | 97.17 | 0.11 | 2.44 | 1567 |
| 2024-09-20 22:21:37.524 | MS1 | 121.4656722816 | 31.1446233810 | 974 | 504990 | -91.24 | 12.15 | 83.64 | 0.18 | 2.58 | 1595 |
| 2024-09-20 22:21:38.546 | MS1 | 121.4656624389 | 31.1446252026 | 974 | 504990 | -91.23 | 8.32 | 92.09 | 0.03 | 2.98 | 1588 |
| 2024-09-20 22:21:39.447 | MS1 | 121.4656739418 | 31.1446215330 | 974 | 504990 | -90.33 | 7.42 | 65.84 | 0.10 | 2.88 | 1581 |
| 2024-09-20 22:21:40.803 | MS1 | 121.4656766417 | 31.1446275441 | 974 | 504990 | -93.14 | 9.34 | 388.95 | 0.14 | 2.73 | 1560 |
| 2024-09-20 22:21:41.599 | MS1 | 121.4656589318 | 31.1446309618 | 974 | 504990 | -92.48 | 12.05 | 555.54 | 0.10 | 2.44 | 1597 |
| 2024-09-20 22:21:42.584 | MS1 | 121.4656599940 | 31.1446186368 | 974 | 504990 | -92.02 | 7.75 | 328.01 | 0.16 | 2.99 | 1586 |

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
| 3214321 | 3 | 121.4667146081 | 31.1523437306 | 71 | 15 | 10 | 49.6 | TDD | 974 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3244504 | 4 | 121.4705007506 | 31.1551813734 | 58 | 7 | 4 | 27.6 | TDD | 860 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3259830 | 2 | 121.4754048383 | 31.1558185411 | 232 | 10 | 5 | 26.5 | TDD | 724 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3260608 | 1 | 121.4742110780 | 31.1497108115 | 138 | 5 | 8 | 24.9 | TDD | 232 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |

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
| 2024-09-20 22:21:31.532 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.557 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.687 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.687 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.367 | NREventA3 | measId:2;ServCellPCI:208;Se... |
| 2024-09-20 22:21:38.607 | NRHandoverAttempt | SourcePCI:208;SourceNR-ARFC... |
| 2024-09-20 22:21:38.644 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.654 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.794 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.794 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3260608 | 1 | 84.9594 | 87.1994 | -116.1610 | 12.7575 | 122.8466 | 0.0068 | 0.0077 |
| 2024_09_19 22:00 | 3259830 | 2 | 83.0761 | 85.7436 | -114.2621 | 13.8800 | 150.3016 | 0.0149 | 0.0062 |
| 2024_09_19 22:00 | 3214321 | 3 | 81.4978 | 81.5060 | -117.6057 | 5.4803 | 189.4205 | 0.0192 | 0.0157 |
| 2024_09_19 22:00 | 3244504 | 4 | 84.4288 | 94.1211 | -116.7637 | 14.9453 | 130.6961 | 0.0117 | 0.0185 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414640_AFDEAD45 | 504990 | 974 | -91.0 | 504990 | 232 | -98.0 | 504990 | 860 | -103.4 | 504990 | 724 |
| MR_1774414640_2F792F76 | 504990 | 974 | -90.2 | 504990 | 232 | -96.0 | 504990 | 860 | -101.4 | 504990 | 724 |
| MR_1774414640_8A98F544 | 504990 | 974 | -88.1 | 504990 | 232 | -97.5 | 504990 | 860 | -103.8 | 504990 | 724 |
| MR_1774414640_7A91786B | 504990 | 974 | -90.7 | 504990 | 232 | -97.8 | 504990 | 860 | -101.2 | 504990 | 724 |
| MR_1774414640_F0E26E6B | 504990 | 974 | -87.9 | 504990 | 232 | -96.0 | 504990 | 860 | -103.7 | 504990 | 724 |
| MR_1774414640_9D2A9E46 | 504990 | 974 | -90.5 | 504990 | 232 | -96.8 | 504990 | 860 | -102.1 | 504990 | 724 |
| MR_1774414640_96A1CF7A | 504990 | 974 | -90.7 | 504990 | 232 | -97.8 | 504990 | 860 | -103.2 | 504990 | 724 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 274: `a21308d3-6c7...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `a21308d3-6c7d-43ba-907f-e0eec2a8d108` |
| Tag | **multiple-answer** |
| 정답 | **C2|C4|C6|C8** |
| C2 의미 | Increase A3 Offset threshold for 3221213_3 |
| C4 의미 | Press down the tilt angle  of 3221213_3 by 3 degrees |
| C6 의미 | Decrease transmission power for 3221213_3 |
| C8 의미 | Increase A3 Offset threshold for 3258987_2 |
| 패턴 분류 | **P2 Ping-pong** |

**시각화 (기지국 배치 + UE 시계열)**

![train[274] topology](images/train_0274.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 5 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 5개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment.
- `C2`: Increase A3 Offset threshold for 3221213_3 **← 정답**
- `C3`: Increase transmission power for 3258987_2
- `C4`: Press down the tilt angle  of 3221213_3 by 3 degrees **← 정답**
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3221213_3
- `C6`: Decrease transmission power for 3221213_3 **← 정답**
- `C7`: Decrease A3 Offset threshold for 3221213_3
- `C8`: Increase A3 Offset threshold for 3258987_2 **← 정답**
- `C9`: Press down the tilt angle of 3258987_2 by 2 degrees
- `C10`: Lift the tilt angle  of 3221213_3 by 3 degrees
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3221213_3
- `C12`: Adjust the azimuth of 3221213_3 by 21 degrees
- `C13`: Decrease transmission power for 3258987_2
- `C14`: Add neighbor relationship between 3258987_2 and 3221213_3
- `C15`: Add neighbor relationship between 3213327_5 and 3221213_3
- `C16`: Adjust the azimuth of 3258987_2 by 24 degrees
- `C17`: Increase transmission power for 3221213_3
- `C18`: Lift the tilt angle of 3258987_2 by 2 degrees
- `C19`: Decrease A3 Offset threshold for 3258987_2
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3258987_2
- `C21`: Check test server and transmission issues
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3258987_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.823 | MS1 | 121.4656666257 | 31.1446180478 | 232 | 504990 | -78.13 | 13.61 | 564.22 | 0.02 | 2.34 | 1589 |
| 2024-09-20 22:21:32.282 | MS1 | 121.4656745689 | 31.1446266806 | 232 | 504990 | -78.71 | 13.16 | 575.35 | 0.01 | 2.32 | 1592 |
| 2024-09-20 22:21:33.840 | MS1 | 121.4656619503 | 31.1446362327 | 232 | 504990 | -82.06 | 12.40 | 591.23 | 0.02 | 2.16 | 1567 |
| 2024-09-20 22:21:34.430 | MS1 | 121.4656588432 | 31.1446277131 | 953 | 504990 | -87.94 | 4.33 | 66.77 | 0.14 | 1.05 | 1583 |
| 2024-09-20 22:21:35.978 | MS1 | 121.4656770487 | 31.1446224109 | 953 | 504990 | -89.54 | 3.33 | 46.05 | 0.14 | 1.23 | 1578 |
| 2024-09-20 22:21:36.545 | MS1 | 121.4656624443 | 31.1446180738 | 232 | 504990 | -80.95 | 3.07 | 82.72 | 0.12 | 1.48 | 1560 |
| 2024-09-20 22:21:37.686 | MS1 | 121.4656769629 | 31.1446218775 | 232 | 504990 | -82.18 | 2.69 | 69.70 | 0.13 | 1.30 | 1572 |
| 2024-09-20 22:21:38.875 | MS1 | 121.4656752815 | 31.1446205667 | 953 | 504990 | -88.07 | 4.37 | 37.17 | 0.06 | 1.08 | 1580 |
| 2024-09-20 22:21:39.302 | MS1 | 121.4656631315 | 31.1446275267 | 953 | 504990 | -81.81 | 2.59 | 44.47 | 0.17 | 1.22 | 1578 |
| 2024-09-20 22:21:40.718 | MS1 | 121.4656696382 | 31.1446372145 | 953 | 504990 | -80.65 | 16.07 | 528.61 | 0.09 | 2.63 | 1560 |
| 2024-09-20 22:21:41.417 | MS1 | 121.4656760281 | 31.1446356106 | 953 | 504990 | -77.45 | 15.06 | 565.12 | 0.15 | 2.64 | 1583 |
| 2024-09-20 22:21:42.692 | MS1 | 121.4656701547 | 31.1446216114 | 953 | 504990 | -78.04 | 16.56 | 339.29 | 0.01 | 2.36 | 1570 |

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
| 3213327 | 5 | 121.4758538672 | 31.1482726438 | 147 | 5 | 5 | 37.8 | TDD | 924 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3221213 | 3 | 121.4669960343 | 31.1555807044 | 207 | 1 | 9 | 48.7 | TDD | 111 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3258987 | 2 | 121.4723217555 | 31.1448500928 | 292 | 0 | 4 | 21.2 | TDD | 232 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3260113 | 4 | 121.4672616141 | 31.1531441028 | 116 | 2 | 5 | 45.1 | TDD | 953 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3277445 | 1 | 121.4677474038 | 31.1510976095 | 146 | 5 | 7 | 16.4 | TDD | 68 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |

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
| 2024-09-20 22:21:30.925 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.941 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.067 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.067 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:33.730 | NREventA3 | measId:2;ServCellPCI:460;Se... |
| 2024-09-20 22:21:33.970 | NRHandoverAttempt | SourcePCI:460;SourceNR-ARFC... |
| 2024-09-20 22:21:34.013 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:34.027 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:34.165 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:34.165 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.730 | NREventA3 | measId:2;ServCellPCI:1006;S... |
| 2024-09-20 22:21:35.970 | NRHandoverAttempt | SourcePCI:1006;SourceNR-ARF... |
| 2024-09-20 22:21:36.007 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:36.021 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:36.168 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.168 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.730 | NREventA3 | measId:2;ServCellPCI:460;Se... |
| 2024-09-20 22:21:37.970 | NRHandoverAttempt | SourcePCI:460;SourceNR-ARFC... |
| 2024-09-20 22:21:38.002 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.013 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.137 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.137 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3277445 | 1 | 14.0445 | 19.7739 | -115.4726 | 14.7151 | 196.9293 | 0.0117 | 0.0005 |
| 2024_09_20 22:00 | 3258987 | 2 | 13.9027 | 6.0280 | -114.5791 | 13.7487 | 107.1284 | 0.0033 | 0.0120 |
| 2024_09_20 22:00 | 3221213 | 3 | 16.1601 | 6.3867 | -115.6013 | 13.1686 | 107.4390 | 0.0101 | 0.0181 |
| 2024_09_20 22:00 | 3260113 | 4 | 9.4983 | 11.1702 | -115.9823 | 10.9562 | 116.4523 | 0.0107 | 0.0044 |
| 2024_09_20 22:00 | 3213327 | 5 | 16.8815 | 13.6230 | -116.2245 | 15.3863 | 152.8767 | 0.0160 | 0.0073 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415788_C01D0A8E | 504990 | 232 | -89.8 | 504990 | 953 | -86.4 | 504990 | 111 | -87.6 | 504990 | 924 |
| MR_1774415788_57AB02A8 | 504990 | 953 | -87.8 | 504990 | 232 | -86.0 | 504990 | 111 | -85.7 | 504990 | 924 |
| MR_1774415788_B6F33477 | 504990 | 232 | -89.8 | 504990 | 953 | -86.5 | 504990 | 111 | -88.3 | 504990 | 924 |
| MR_1774415788_93D803A2 | 504990 | 232 | -86.5 | 504990 | 953 | -87.3 | 504990 | 111 | -88.2 | 504990 | 924 |
| MR_1774415788_E63B7987 | 504990 | 232 | -88.2 | 504990 | 953 | -86.1 | 504990 | 111 | -85.9 | 504990 | 924 |
| MR_1774415788_5B79F208 | 504990 | 953 | -87.2 | 504990 | 232 | -86.0 | 504990 | 111 | -88.6 | 504990 | 924 |
| MR_1774415788_D73C9B01 | 504990 | 232 | -89.0 | 504990 | 953 | -85.1 | 504990 | 111 | -86.8 | 504990 | 924 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 275: `184d6c23-3fb...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `184d6c23-3fb0-4d74-b19f-50d0c44ba782` |
| Tag | **single-answer** |
| 정답 | **C20** |
| C20 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3220782_3 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[275] topology](images/train_0275.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3212147_4 by 50 degrees
- `C2`: Increase A3 Offset threshold for 3212147_4
- `C3`: Add neighbor relationship between 3236042_2 and 3212147_4
- `C4`: Decrease transmission power for 3220782_3
- `C5`: Adjust the azimuth of 3220782_3 by 22 degrees
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3220782_3
- `C7`: Decrease transmission power for 3212147_4
- `C8`: Check test server and transmission issues
- `C9`: Insufficient data; more data is needed for judgment.
- `C10`: Lift the tilt angle  of 3212147_4 by 10 degrees
- `C11`: Press down the tilt angle of 3220782_3 by 5 degrees
- `C12`: Decrease A3 Offset threshold for 3212147_4
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3212147_4
- `C14`: Press down the tilt angle  of 3212147_4 by 10 degrees
- `C15`: Decrease A3 Offset threshold for 3220782_3
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3212147_4
- `C17`: Increase transmission power for 3212147_4
- `C18`: Add neighbor relationship between 3220782_3 and 3212147_4
- `C19`: Lift the tilt angle of 3220782_3 by 5 degrees
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3220782_3 **← 정답**
- `C21`: Increase A3 Offset threshold for 3220782_3
- `C22`: Increase transmission power for 3220782_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.914 | MS1 | 121.4656679192 | 31.1446292287 | 124 | 504990 | -89.57 | 13.77 | 481.57 | 0.01 | 2.69 | 1582 |
| 2024-09-20 22:21:32.668 | MS1 | 121.4656616231 | 31.1446249674 | 124 | 504990 | -86.32 | 16.01 | 410.93 | 0.12 | 2.31 | 1589 |
| 2024-09-20 22:21:33.344 | MS1 | 121.4656777381 | 31.1446346558 | 124 | 504990 | -87.12 | 15.00 | 436.05 | 0.17 | 2.29 | 1560 |
| 2024-09-20 22:21:34.111 | MS1 | 121.4656623969 | 31.1446182956 | 124 | 504990 | -86.00 | 13.45 | 67.27 | 0.53 | 2.27 | 654 |
| 2024-09-20 22:21:35.706 | MS1 | 121.4656763962 | 31.1446252971 | 124 | 504990 | -88.24 | 17.67 | 90.35 | 0.58 | 2.98 | 576 |
| 2024-09-20 22:21:36.978 | MS1 | 121.4656609994 | 31.1446284545 | 124 | 504990 | -86.83 | 15.89 | 54.19 | 0.63 | 2.49 | 679 |
| 2024-09-20 22:21:37.648 | MS1 | 121.4656632848 | 31.1446325326 | 124 | 504990 | -93.03 | 11.79 | 66.06 | 0.66 | 2.63 | 641 |
| 2024-09-20 22:21:38.913 | MS1 | 121.4656671135 | 31.1446288751 | 124 | 504990 | -91.82 | 12.58 | 49.86 | 0.62 | 2.62 | 506 |
| 2024-09-20 22:21:39.318 | MS1 | 121.4656722745 | 31.1446378212 | 124 | 504990 | -92.42 | 12.74 | 54.72 | 0.69 | 2.20 | 624 |
| 2024-09-20 22:21:40.809 | MS1 | 121.4656634316 | 31.1446373759 | 124 | 504990 | -91.55 | 9.95 | 393.04 | 0.14 | 2.29 | 1597 |
| 2024-09-20 22:21:41.980 | MS1 | 121.4656742849 | 31.1446240970 | 124 | 504990 | -93.94 | 11.01 | 315.49 | 0.17 | 2.73 | 1562 |
| 2024-09-20 22:21:42.536 | MS1 | 121.4656765567 | 31.1446378543 | 124 | 504990 | -92.92 | 7.50 | 566.60 | 0.00 | 2.46 | 1580 |

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
| 3212147 | 4 | 121.4654862219 | 31.1467684150 | 84 | 5 | 0 | 41.0 | TDD | 415 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3220782 | 3 | 121.4671834765 | 31.1489191816 | 219 | 2 | 6 | 30.1 | TDD | 124 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3236042 | 2 | 121.4730657104 | 31.1498906521 | 298 | 1 | 9 | 28.7 | TDD | 635 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3263162 | 1 | 121.4650929623 | 31.1544447631 | 307 | 6 | 9 | 16.4 | TDD | 402 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |

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
| 2024-09-20 22:21:30.947 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.947 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.632 | NREventA3 | measId:2;ServCellPCI:258;Se... |
| 2024-09-20 22:21:37.872 | NRHandoverAttempt | SourcePCI:258;SourceNR-ARFC... |
| 2024-09-20 22:21:37.922 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.936 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.059 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.059 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3263162 | 1 | 10.1238 | 7.7830 | -116.3548 | 16.9856 | 184.9032 | 0.0085 | 0.0080 |
| 2024_09_20 22:00 | 3236042 | 2 | 7.6737 | 12.2640 | -114.0282 | 8.5762 | 160.2651 | 0.0119 | 0.0071 |
| 2024_09_20 22:00 | 3220782 | 3 | 13.8177 | 12.8284 | -115.8128 | 5.3183 | 135.9358 | 0.0178 | 0.0077 |
| 2024_09_20 22:00 | 3212147 | 4 | 6.5595 | 7.3537 | -115.2978 | 16.0844 | 162.9160 | 0.0078 | 0.0063 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415182_B6C6647D | 504990 | 124 | -86.9 | 504990 | 415 | -88.4 | 504990 | 635 | -100.0 | 504990 | 402 |
| MR_1774415182_D572109C | 504990 | 124 | -84.6 | 504990 | 415 | -91.4 | 504990 | 635 | -98.3 | 504990 | 402 |
| MR_1774415182_BD5E4958 | 504990 | 124 | -87.6 | 504990 | 415 | -91.1 | 504990 | 635 | -97.6 | 504990 | 402 |
| MR_1774415182_C842648F | 504990 | 124 | -87.5 | 504990 | 415 | -90.2 | 504990 | 635 | -98.5 | 504990 | 402 |
| MR_1774415182_31831F36 | 504990 | 124 | -84.9 | 504990 | 415 | -91.1 | 504990 | 635 | -100.3 | 504990 | 402 |
| MR_1774415182_A46DA407 | 504990 | 124 | -85.8 | 504990 | 415 | -88.6 | 504990 | 635 | -100.4 | 504990 | 402 |
| MR_1774415182_72B7BFF9 | 504990 | 124 | -84.4 | 504990 | 415 | -88.4 | 504990 | 635 | -100.0 | 504990 | 402 |
| MR_1774415182_FC0E5A43 | 504990 | 124 | -87.8 | 504990 | 415 | -91.5 | 504990 | 635 | -97.7 | 504990 | 402 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 276: `f28eadd3-6c6...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `f28eadd3-6c69-4429-947c-2b990dd3f2cd` |
| Tag | **multiple-answer** |
| 정답 | **C6|C8** |
| C6 의미 | Adjust the azimuth of 3242518_4 by 50 degrees |
| C8 의미 | Increase transmission power for 3242518_4 |
| 패턴 분류 | **P4 Coverage (azimuth)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[276] topology](images/train_0276.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3265860_2 by 4 degrees
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3265860_2
- `C3`: Lift the tilt angle of 3242518_4 by 10 degrees
- `C4`: Decrease A3 Offset threshold for 3265860_2
- `C5`: Decrease transmission power for 3265860_2
- `C6`: Adjust the azimuth of 3242518_4 by 50 degrees **← 정답**
- `C7`: Lift the tilt angle  of 3265860_2 by 4 degrees
- `C8`: Increase transmission power for 3242518_4 **← 정답**
- `C9`: Add neighbor relationship between 3242775_1 and 3265860_2
- `C10`: Check test server and transmission issues
- `C11`: Adjust the azimuth of 3265860_2 by 35 degrees
- `C12`: Decrease A3 Offset threshold for 3242518_4
- `C13`: Add neighbor relationship between 3242518_4 and 3265860_2
- `C14`: Increase transmission power for 3265860_2
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3242518_4
- `C16`: Decrease transmission power for 3242518_4
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3265860_2
- `C18`: Insufficient data; more data is needed for judgment.
- `C19`: Press down the tilt angle of 3242518_4 by 10 degrees
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3242518_4
- `C21`: Increase A3 Offset threshold for 3265860_2
- `C22`: Increase A3 Offset threshold for 3242518_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.786 | MS1 | 121.4656600058 | 31.1446324647 | 237 | 504990 | -85.81 | 14.36 | 498.78 | 0.02 | 2.80 | 1584 |
| 2024-09-20 22:21:32.370 | MS1 | 121.4656611505 | 31.1446201488 | 237 | 504990 | -91.59 | 17.72 | 359.62 | 0.16 | 2.64 | 1567 |
| 2024-09-20 22:21:33.199 | MS1 | 121.4656777312 | 31.1446255794 | 237 | 504990 | -88.51 | 13.32 | 382.08 | 0.08 | 2.91 | 1597 |
| 2024-09-20 22:21:34.859 | MS1 | 121.4656629533 | 31.1446229691 | 237 | 504990 | -107.86 | 1.07 | 36.48 | 0.02 | 1.26 | 1572 |
| 2024-09-20 22:21:35.206 | MS1 | 121.4656615597 | 31.1446288943 | 237 | 504990 | -108.99 | -1.94 | 15.79 | 0.19 | 1.39 | 1573 |
| 2024-09-20 22:21:36.729 | MS1 | 121.4656744703 | 31.1446273663 | 237 | 504990 | -100.21 | -0.48 | 55.50 | 0.15 | 1.46 | 1569 |
| 2024-09-20 22:21:37.576 | MS1 | 121.4656715016 | 31.1446223564 | 237 | 504990 | -107.07 | 0.54 | 19.92 | 0.03 | 1.32 | 1598 |
| 2024-09-20 22:21:38.232 | MS1 | 121.4656695009 | 31.1446281456 | 237 | 504990 | -107.36 | -0.25 | 38.19 | 0.02 | 1.26 | 1580 |
| 2024-09-20 22:21:39.163 | MS1 | 121.4656778345 | 31.1446368524 | 237 | 504990 | -104.73 | -1.65 | 63.52 | 0.00 | 1.38 | 1600 |
| 2024-09-20 22:21:40.502 | MS1 | 121.4656691361 | 31.1446180469 | 237 | 504990 | -88.61 | 12.24 | 405.19 | 0.01 | 2.77 | 1569 |
| 2024-09-20 22:21:41.582 | MS1 | 121.4656620615 | 31.1446263424 | 237 | 504990 | -91.78 | 13.14 | 387.87 | 0.07 | 2.19 | 1572 |
| 2024-09-20 22:21:42.618 | MS1 | 121.4656706716 | 31.1446303770 | 237 | 504990 | -85.88 | 12.88 | 526.29 | 0.03 | 2.51 | 1574 |

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
| 3239579 | 3 | 121.4696632251 | 31.1523149120 | 40 | 15 | 12 | 45.4 | TDD | 156 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3242518 | 4 | 121.4688690953 | 31.1444157270 | 346 | 2 | 7 | 46.2 | TDD | 237 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3242775 | 1 | 121.4743879401 | 31.1502454057 | 213 | 2 | 9 | 45.7 | TDD | 488 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3265860 | 2 | 121.4640850753 | 31.1486973480 | 197 | 2 | 2 | 16.7 | TDD | 434 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |

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
| 2024-09-20 22:21:30.945 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.964 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.083 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.083 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.283 | NREventA2 | measId:1;ServCellPCI:467;Se... |
| 2024-09-20 22:21:34.384 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3242775 | 1 | 5.8471 | 5.9282 | -115.9867 | 11.9041 | 134.6907 | 0.0162 | 0.0118 |
| 2024_09_20 22:00 | 3265860 | 2 | 15.1724 | 10.8848 | -117.2937 | 8.2235 | 136.3299 | 0.0032 | 0.0175 |
| 2024_09_20 22:00 | 3239579 | 3 | 14.7077 | 9.5936 | -117.3900 | 17.7873 | 191.2573 | 0.0188 | 0.0117 |
| 2024_09_20 22:00 | 3242518 | 4 | 11.4873 | 9.0444 | -115.8489 | 10.0769 | 164.4471 | 0.1686 | 0.0129 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415930_8C78F784 | 504990 | 237 | -108.6 | 504990 | 434 | -112.6 | 504990 | 488 | -116.0 | 504990 | 156 |
| MR_1774415930_3E5BEA2A | 504990 | 237 | -109.2 | 504990 | 434 | -112.9 | 504990 | 488 | -117.2 | 504990 | 156 |
| MR_1774415930_B082B8C9 | 504990 | 237 | -106.5 | 504990 | 434 | -109.3 | 504990 | 488 | -115.4 | 504990 | 156 |
| MR_1774415930_581DCA27 | 504990 | 237 | -109.5 | 504990 | 434 | -111.6 | 504990 | 488 | -116.0 | 504990 | 156 |
| MR_1774415930_B7364847 | 504990 | 237 | -109.6 | 504990 | 434 | -109.5 | 504990 | 488 | -118.2 | 504990 | 156 |
| MR_1774415930_84F1AE63 | 504990 | 237 | -107.2 | 504990 | 434 | -110.2 | 504990 | 488 | -115.7 | 504990 | 156 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 277: `d03aa61f-e96...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `d03aa61f-e96b-47c5-a2d0-d1c89aed634f` |
| Tag | **single-answer** |
| 정답 | **C22** |
| C22 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3213735_2 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[277] topology](images/train_0277.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3223147_4 by 50 degrees
- `C2`: Increase A3 Offset threshold for 3213735_2
- `C3`: Decrease transmission power for 3223147_4
- `C4`: Add neighbor relationship between 3213735_2 and 3223147_4
- `C5`: Decrease A3 Offset threshold for 3213735_2
- `C6`: Insufficient data; more data is needed for judgment.
- `C7`: Adjust the azimuth of 3213735_2 by 34 degrees
- `C8`: Press down the tilt angle  of 3223147_4 by 7 degrees
- `C9`: Increase transmission power for 3213735_2
- `C10`: Add neighbor relationship between 3259608_1 and 3223147_4
- `C11`: Press down the tilt angle of 3213735_2 by 4 degrees
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3223147_4
- `C13`: Increase A3 Offset threshold for 3223147_4
- `C14`: Decrease transmission power for 3213735_2
- `C15`: Lift the tilt angle of 3213735_2 by 4 degrees
- `C16`: Decrease A3 Offset threshold for 3223147_4
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3213735_2
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3223147_4
- `C19`: Check test server and transmission issues
- `C20`: Lift the tilt angle  of 3223147_4 by 7 degrees
- `C21`: Increase transmission power for 3223147_4
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3213735_2 **← 정답**

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.502 | MS1 | 121.4656658762 | 31.1446300688 | 492 | 504990 | -86.81 | 14.15 | 602.07 | 0.02 | 2.98 | 1591 |
| 2024-09-20 22:21:32.362 | MS1 | 121.4656634741 | 31.1446330719 | 492 | 504990 | -88.74 | 15.40 | 499.26 | 0.09 | 2.17 | 1573 |
| 2024-09-20 22:21:33.838 | MS1 | 121.4656774303 | 31.1446240423 | 492 | 504990 | -89.96 | 14.08 | 337.83 | 0.12 | 2.28 | 1580 |
| 2024-09-20 22:21:34.986 | MS1 | 121.4656651999 | 31.1446259777 | 492 | 504990 | -86.86 | 15.82 | 73.63 | 0.54 | 2.97 | 700 |
| 2024-09-20 22:21:35.687 | MS1 | 121.4656708263 | 31.1446283157 | 492 | 504990 | -91.05 | 12.50 | 70.13 | 0.61 | 2.74 | 620 |
| 2024-09-20 22:21:36.649 | MS1 | 121.4656704947 | 31.1446315242 | 492 | 504990 | -86.39 | 15.15 | 81.86 | 0.65 | 2.22 | 657 |
| 2024-09-20 22:21:37.302 | MS1 | 121.4656585375 | 31.1446214647 | 492 | 504990 | -93.05 | 10.01 | 63.96 | 0.51 | 2.75 | 531 |
| 2024-09-20 22:21:38.848 | MS1 | 121.4656667319 | 31.1446346569 | 492 | 504990 | -91.21 | 9.03 | 43.33 | 0.59 | 2.86 | 563 |
| 2024-09-20 22:21:39.295 | MS1 | 121.4656732808 | 31.1446313567 | 492 | 504990 | -92.56 | 9.10 | 55.24 | 0.54 | 2.70 | 572 |
| 2024-09-20 22:21:40.312 | MS1 | 121.4656731195 | 31.1446317422 | 492 | 504990 | -92.24 | 10.96 | 547.19 | 0.01 | 2.54 | 1569 |
| 2024-09-20 22:21:41.372 | MS1 | 121.4656599040 | 31.1446348012 | 492 | 504990 | -91.89 | 12.02 | 400.45 | 0.02 | 2.22 | 1585 |
| 2024-09-20 22:21:42.337 | MS1 | 121.4656701847 | 31.1446367969 | 492 | 504990 | -92.42 | 10.28 | 327.12 | 0.15 | 2.79 | 1578 |

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
| 3213735 | 2 | 121.4691519619 | 31.1442847025 | 311 | 1 | 5 | 20.4 | TDD | 492 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3223147 | 4 | 121.4672552432 | 31.1473816912 | 107 | 2 | 1 | 28.3 | TDD | 146 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3240356 | 3 | 121.4715215758 | 31.1532309954 | 286 | 11 | 10 | 25.6 | TDD | 906 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3259608 | 1 | 121.4748555089 | 31.1521017297 | 19 | 8 | 11 | 17.8 | TDD | 194 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:30.808 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.826 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:30.964 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.964 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.639 | NREventA3 | measId:2;ServCellPCI:984;Se... |
| 2024-09-20 22:21:37.879 | NRHandoverAttempt | SourcePCI:984;SourceNR-ARFC... |
| 2024-09-20 22:21:37.910 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.922 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.069 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.069 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3259608 | 1 | 6.9588 | 16.5192 | -117.6768 | 11.4360 | 167.0156 | 0.0094 | 0.0063 |
| 2024_09_20 22:00 | 3213735 | 2 | 12.1318 | 13.3659 | -114.8633 | 7.9117 | 173.5880 | 0.0197 | 0.0115 |
| 2024_09_20 22:00 | 3240356 | 3 | 15.9961 | 10.2081 | -117.1421 | 15.9006 | 86.9817 | 0.0015 | 0.0094 |
| 2024_09_20 22:00 | 3223147 | 4 | 14.0333 | 13.9213 | -114.7085 | 18.8832 | 114.9719 | 0.0183 | 0.0163 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415452_4472D217 | 504990 | 492 | -86.8 | 504990 | 146 | -93.0 | 504990 | 194 | -95.7 | 504990 | 906 |
| MR_1774415452_5C5D3E75 | 504990 | 492 | -88.1 | 504990 | 146 | -90.7 | 504990 | 194 | -98.0 | 504990 | 906 |
| MR_1774415452_6B20F7D1 | 504990 | 492 | -86.1 | 504990 | 146 | -92.0 | 504990 | 194 | -98.8 | 504990 | 906 |
| MR_1774415452_4E7466F6 | 504990 | 492 | -86.8 | 504990 | 146 | -92.3 | 504990 | 194 | -97.8 | 504990 | 906 |
| MR_1774415452_EDB486F1 | 504990 | 492 | -85.7 | 504990 | 146 | -91.7 | 504990 | 194 | -96.9 | 504990 | 906 |
| MR_1774415452_8F5890DB | 504990 | 492 | -88.1 | 504990 | 146 | -90.1 | 504990 | 194 | -94.8 | 504990 | 906 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 278: `34a8842c-632...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `34a8842c-6327-4e14-b02e-a77907ca666f` |
| Tag | **multiple-answer** |
| 정답 | **C12|C21** |
| C12 의미 | Decrease transmission power for 3242220_4 |
| C21 의미 | Press down the tilt angle  of 3242220_4 by 3 degrees |
| 패턴 분류 | **P3 Overshoot (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[278] topology](images/train_0278.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3218367_2 by 28 degrees
- `C2`: Lift the tilt angle  of 3242220_4 by 3 degrees
- `C3`: Decrease A3 Offset threshold for 3242220_4
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3218367_2
- `C5`: Decrease A3 Offset threshold for 3218367_2
- `C6`: Decrease transmission power for 3218367_2
- `C7`: Lift the tilt angle of 3218367_2 by 4 degrees
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3218367_2
- `C9`: Add neighbor relationship between 3218367_2 and 3242220_4
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3242220_4
- `C11`: Add neighbor relationship between 3276129_3 and 3242220_4
- `C12`: Decrease transmission power for 3242220_4 **← 정답**
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3242220_4
- `C14`: Press down the tilt angle of 3218367_2 by 4 degrees
- `C15`: Increase A3 Offset threshold for 3218367_2
- `C16`: Adjust the azimuth of 3242220_4 by 16 degrees
- `C17`: Increase transmission power for 3242220_4
- `C18`: Insufficient data; more data is needed for judgment.
- `C19`: Check test server and transmission issues
- `C20`: Increase A3 Offset threshold for 3242220_4
- `C21`: Press down the tilt angle  of 3242220_4 by 3 degrees **← 정답**
- `C22`: Increase transmission power for 3218367_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.495 | MS1 | 121.4656622419 | 31.1446258312 | 121 | 504990 | -80.00 | 12.70 | 387.16 | 0.17 | 2.63 | 1585 |
| 2024-09-20 22:21:32.362 | MS1 | 121.4656779326 | 31.1446293607 | 121 | 504990 | -83.82 | 14.37 | 435.29 | 0.14 | 2.30 | 1566 |
| 2024-09-20 22:21:33.862 | MS1 | 121.4656691028 | 31.1446180134 | 121 | 504990 | -84.26 | 17.99 | 534.21 | 0.14 | 2.46 | 1579 |
| 2024-09-20 22:21:34.189 | MS1 | 121.4656674818 | 31.1446265281 | 121 | 504990 | -90.60 | 3.52 | 80.43 | 0.16 | 1.13 | 1597 |
| 2024-09-20 22:21:35.707 | MS1 | 121.4656583756 | 31.1446308589 | 121 | 504990 | -91.48 | 0.61 | 48.94 | 0.08 | 1.30 | 1578 |
| 2024-09-20 22:21:36.892 | MS1 | 121.4656674577 | 31.1446187342 | 121 | 504990 | -85.69 | 0.98 | 84.86 | 0.08 | 1.21 | 1590 |
| 2024-09-20 22:21:37.951 | MS1 | 121.4656775541 | 31.1446190983 | 121 | 504990 | -89.20 | 0.93 | 45.94 | 0.13 | 1.02 | 1593 |
| 2024-09-20 22:21:38.611 | MS1 | 121.4656659152 | 31.1446245648 | 121 | 504990 | -94.93 | 1.99 | 57.82 | 0.11 | 1.35 | 1575 |
| 2024-09-20 22:21:39.565 | MS1 | 121.4656771314 | 31.1446323042 | 121 | 504990 | -89.80 | 0.19 | 87.93 | 0.02 | 1.22 | 1595 |
| 2024-09-20 22:21:40.264 | MS1 | 121.4656754209 | 31.1446225403 | 121 | 504990 | -77.73 | 16.15 | 513.68 | 0.17 | 2.57 | 1593 |
| 2024-09-20 22:21:41.711 | MS1 | 121.4656640736 | 31.1446354617 | 121 | 504990 | -78.02 | 16.08 | 314.44 | 0.02 | 2.91 | 1580 |
| 2024-09-20 22:21:42.239 | MS1 | 121.4656633398 | 31.1446287030 | 121 | 504990 | -81.76 | 12.94 | 409.29 | 0.09 | 2.37 | 1562 |

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
| 3218367 | 2 | 121.4708114839 | 31.1509206811 | 187 | 1 | 1 | 44.0 | TDD | 121 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3242220 | 4 | 121.4665689596 | 31.1507936286 | 203 | 1 | 3 | 19.4 | TDD | 955 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3252553 | 1 | 121.4696657233 | 31.1553581734 | 120 | 12 | 8 | 34.5 | TDD | 96 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3276129 | 3 | 121.4705749614 | 31.1537730232 | 315 | 11 | 8 | 36.7 | TDD | 386 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:30.815 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.839 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:30.985 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.985 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3252553 | 1 | 12.8727 | 13.4715 | -114.2319 | 19.3696 | 174.9736 | 0.0168 | 0.0173 |
| 2024_09_20 22:00 | 3218367 | 2 | 11.3784 | 17.8840 | -108.3652 | 17.4648 | 147.2307 | 0.0178 | 0.0077 |
| 2024_09_20 22:00 | 3276129 | 3 | 8.2339 | 7.0746 | -114.0707 | 7.1509 | 98.4265 | 0.0113 | 0.0009 |
| 2024_09_20 22:00 | 3242220 | 4 | 7.0778 | 17.1826 | -114.2558 | 12.2235 | 94.2785 | 0.0078 | 0.0101 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414963_7141535E | 504990 | 121 | -91.5 | 504990 | 955 | -85.1 | 504990 | 386 | -95.3 | 504990 | 96 |
| MR_1774414963_50B86B61 | 504990 | 955 | -92.5 | 504990 | 121 | -86.7 | 504990 | 386 | -93.4 | 504990 | 96 |
| MR_1774414963_4FC6A926 | 504990 | 121 | -89.5 | 504990 | 955 | -87.6 | 504990 | 386 | -92.6 | 504990 | 96 |
| MR_1774414963_72E6368B | 504990 | 121 | -91.7 | 504990 | 955 | -88.9 | 504990 | 386 | -91.7 | 504990 | 96 |
| MR_1774414963_77B6F55B | 504990 | 121 | -89.3 | 504990 | 955 | -87.2 | 504990 | 386 | -92.3 | 504990 | 96 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 279: `9d6034a1-491...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `9d6034a1-4910-4857-ae66-a69e9ff30feb` |
| Tag | **single-answer** |
| 정답 | **C12** |
| C12 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3221568_5 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[279] topology](images/train_0279.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3221568_5
- `C2`: Decrease A3 Offset threshold for 3221568_5
- `C3`: Insufficient data; more data is needed for judgment.
- `C4`: Add neighbor relationship between 3230533_10 and 3258270_4
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3258270_4
- `C6`: Check test server and transmission issues
- `C7`: Increase A3 Offset threshold for 3258270_4
- `C8`: Adjust the azimuth of 3221568_5 by 10 degrees
- `C9`: Decrease A3 Offset threshold for 3258270_4
- `C10`: Decrease transmission power for 3221568_5
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3221568_5
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3221568_5 **← 정답**
- `C13`: Adjust the azimuth of 3258270_4 by 14 degrees
- `C14`: Lift the tilt angle  of 3258270_4 by 6 degrees
- `C15`: Increase A3 Offset threshold for 3221568_5
- `C16`: Press down the tilt angle of 3221568_5 by 6 degrees
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3258270_4
- `C18`: Add neighbor relationship between 3221568_5 and 3258270_4
- `C19`: Decrease transmission power for 3258270_4
- `C20`: Lift the tilt angle of 3221568_5 by 6 degrees
- `C21`: Increase transmission power for 3258270_4
- `C22`: Press down the tilt angle  of 3258270_4 by 6 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.797 | MS1 | 121.4656650009 | 31.1446234152 | 373 | 504990 | -95.52 | 10.12 | 346.61 | 0.04 | 2.05 | 1598 |
| 2024-09-20 22:21:32.526 | MS1 | 121.4656597766 | 31.1446212248 | 802 | 504990 | -94.89 | 9.98 | 370.44 | 0.02 | 2.11 | 1587 |
| 2024-09-20 22:21:33.947 | MS1 | 121.4656659850 | 31.1446279446 | 284 | 504990 | -93.42 | 10.40 | 459.71 | 0.11 | 2.81 | 1583 |
| 2024-09-20 22:21:34.525 | MS1 | 121.4656701479 | 31.1446239612 | 327 | 152650 | -94.03 | 5.68 | 63.77 | 0.14 | 1.53 | 940 |
| 2024-09-20 22:21:35.628 | MS1 | 121.4656601169 | 31.1446364043 | 838 | 152650 | -95.23 | 5.67 | 102.62 | 0.04 | 1.67 | 979 |
| 2024-09-20 22:21:36.391 | MS1 | 121.4656618113 | 31.1446349639 | 491 | 152650 | -87.16 | 3.27 | 88.99 | 0.06 | 1.64 | 930 |
| 2024-09-20 22:21:37.979 | MS1 | 121.4656748031 | 31.1446287215 | 785 | 152650 | -91.76 | 2.13 | 48.32 | 0.01 | 1.60 | 935 |
| 2024-09-20 22:21:38.213 | MS1 | 121.4656691799 | 31.1446325713 | 327 | 152650 | -94.15 | 4.91 | 78.93 | 0.13 | 1.55 | 944 |
| 2024-09-20 22:21:39.377 | MS1 | 121.4656731549 | 31.1446194162 | 838 | 152650 | -90.47 | 4.35 | 69.11 | 0.14 | 1.69 | 998 |
| 2024-09-20 22:21:40.305 | MS1 | 121.4656756036 | 31.1446375652 | 491 | 152650 | -92.80 | 6.34 | 62.41 | 0.13 | 2.90 | 1581 |
| 2024-09-20 22:21:41.233 | MS1 | 121.4656652992 | 31.1446201651 | 785 | 152650 | -90.33 | 7.12 | 81.83 | 0.11 | 2.36 | 1585 |
| 2024-09-20 22:21:42.603 | MS1 | 121.4656739646 | 31.1446324250 | 327 | 152650 | -96.15 | 5.89 | 87.18 | 0.02 | 2.17 | 1594 |

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
| 3221568 | 5 | 121.4687766006 | 31.1528752290 | 208 | 5 | 10 | 11.5 | TDD | 373 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3225503 | 8 | 121.4702593095 | 31.1487790827 | 65 | 13 | 6 | 9.5 | FDD | 327 | n1 | 152650 | 30M | 4T4R | 19 | 152650 |
| 3230533 | 10 | 121.4648143414 | 31.1539807038 | 222 | 5 | 5 | 1.2 | FDD | 491 | n1 | 152650 | 30M | 4T4R | 24 | 152650 |
| 3231598 | 9 | 121.4702670109 | 31.1518104133 | 275 | 3 | 12 | 25.6 | FDD | 362 | n1 | 152650 | 30M | 4T4R | 28 | 152650 |
| 3236572 | 13 | 121.4685955693 | 31.1535940720 | 57 | 11 | 1 | 2.2 | FDD | 92 | n1 | 152650 | 30M | 4T4R | 27 | 152650 |
| 3237037 | 3 | 121.4651992210 | 31.1544646705 | 69 | 7 | 8 | 8.3 | TDD | 938 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3240676 | 11 | 121.4744648064 | 31.1482309552 | 334 | 3 | 4 | 10.5 | FDD | 970 | n1 | 152650 | 30M | 4T4R | 13 | 152650 |
| 3243165 | 1 | 121.4697693738 | 31.1525280190 | 62 | 9 | 0 | 5.4 | TDD | 802 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3247869 | 12 | 121.4697553246 | 31.1513782043 | 106 | 7 | 4 | 6.4 | FDD | 785 | n1 | 152650 | 30M | 4T4R | 11 | 152650 |
| 3250788 | 6 | 121.4661203073 | 31.1486800663 | 190 | 6 | 10 | 4.0 | TDD | 284 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3253287 | 7 | 121.4751702705 | 31.1445830868 | 105 | 2 | 4 | 28.3 | FDD | 838 | n1 | 152650 | 30M | 4T4R | 12 | 152650 |
| 3258270 | 4 | 121.4746833334 | 31.1495241601 | 224 | 5 | 11 | 15.3 | TDD | 755 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3275137 | 2 | 121.4730415282 | 31.1494470135 | 217 | 2 | 9 | 22.3 | TDD | 233 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |

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
| 2024-09-20 22:21:30.747 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.765 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:30.893 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.893 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.604 | NREventA2 | measId:1;ServCellPCI:780;Se... |
| 2024-09-20 22:21:34.744 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:34.957 | NREventA5 | measId:3;ServCellPCI:780;Se... |
| 2024-09-20 22:21:35.027 | NRHandoverAttempt | SourcePCI:780;SourceNR-ARFC... |
| 2024-09-20 22:21:35.057 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.072 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:35.202 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.202 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3243165 | 1 | 12.5731 | 17.5757 | -114.2228 | 9.5083 | 157.9072 | 0.0188 | 0.0153 |
| 2024_09_20 22:00 | 3275137 | 2 | 15.2800 | 6.7993 | -117.8637 | 17.9889 | 106.9597 | 0.0032 | 0.0082 |
| 2024_09_20 22:00 | 3237037 | 3 | 15.5538 | 9.1729 | -117.2698 | 10.4014 | 149.9920 | 0.0154 | 0.0069 |
| 2024_09_20 22:00 | 3258270 | 4 | 9.9725 | 8.8946 | -117.0660 | 6.7881 | 115.6711 | 0.0013 | 0.0104 |
| 2024_09_20 22:00 | 3221568 | 5 | 12.3981 | 11.5350 | -116.4771 | 7.2989 | 107.5552 | 0.0173 | 0.0112 |
| 2024_09_20 22:00 | 3250788 | 6 | 10.0845 | 17.2441 | -116.7146 | 15.9223 | 129.4235 | 0.0145 | 0.0018 |
| 2024_09_20 22:00 | 3253287 | 7 | 6.7768 | 11.6636 | -117.5689 | 4.9210 | 55.3989 | 0.0070 | 0.0013 |
| 2024_09_20 22:00 | 3225503 | 8 | 13.6391 | 10.1636 | -114.3519 | 4.8651 | 28.7279 | 0.0042 | 0.0191 |
| 2024_09_20 22:00 | 3231598 | 9 | 17.5684 | 18.2725 | -116.0392 | 4.7720 | 45.9950 | 0.0138 | 0.0180 |
| 2024_09_20 22:00 | 3230533 | 10 | 9.0432 | 7.1369 | -115.9323 | 3.0763 | 44.4284 | 0.0041 | 0.0050 |
| 2024_09_20 22:00 | 3240676 | 11 | 16.8525 | 8.5159 | -115.6162 | 3.1602 | 23.8703 | 0.0030 | 0.0169 |
| 2024_09_20 22:00 | 3247869 | 12 | 15.1712 | 9.7134 | -115.5038 | 4.0439 | 48.1376 | 0.0002 | 0.0067 |
| 2024_09_20 22:00 | 3236572 | 13 | 11.6818 | 17.9070 | -115.7590 | 4.0619 | 49.9276 | 0.0176 | 0.0047 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415773_9FCD5E4F | 152650 | 327 | -95.5 | 152650 | 92 | -94.7 | 152650 | 362 | -104.4 | 152650 | 970 |
| MR_1774415773_6AB0FEA8 | 504990 | 284 | -93.0 | 504990 | 755 | -94.3 | 504990 | 938 | -98.2 | 504990 | 233 |
| MR_1774415773_BE205C35 | 504990 | 284 | -91.8 | 504990 | 755 | -98.0 | 504990 | 938 | -99.1 | 504990 | 233 |
| MR_1774415773_3661F4BC | 504990 | 284 | -92.2 | 504990 | 755 | -97.6 | 504990 | 938 | -98.2 | 504990 | 233 |
| MR_1774415773_84D3EDD7 | 504990 | 284 | -94.5 | 504990 | 755 | -96.5 | 504990 | 938 | -99.7 | 504990 | 233 |
| MR_1774415773_7CDE8DAD | 152650 | 327 | -92.6 | 152650 | 92 | -96.3 | 152650 | 362 | -101.3 | 152650 | 970 |
| MR_1774415773_07BB5E7B | 504990 | 284 | -92.6 | 504990 | 755 | -97.1 | 504990 | 938 | -99.9 | 504990 | 233 |
| MR_1774415773_716E5B0B | 152650 | 327 | -93.4 | 152650 | 92 | -96.6 | 152650 | 362 | -104.8 | 152650 | 970 |

> *... 2개 열 생략 (전체 14열)*

---
