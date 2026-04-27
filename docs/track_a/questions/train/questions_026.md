# Track A 문제 분석 — train[250]~train[259]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[250] ~ train[259] (10개)

## 목차

1. [문제 250: `1a4cadb0-76a...`](#250) — multiple-answer, 정답: C17|C22
2. [문제 251: `c4c17a89-e0f...`](#251) — single-answer, 정답: C17
3. [문제 252: `cdc45ff2-a66...`](#252) — single-answer, 정답: C21
4. [문제 253: `ef9fcc75-377...`](#253) — single-answer, 정답: C7
5. [문제 254: `a29f23ec-e0d...`](#254) — single-answer, 정답: C14
6. [문제 255: `0a9ef243-6ff...`](#255) — single-answer, 정답: C15
7. [문제 256: `6ed3d697-e63...`](#256) — single-answer, 정답: C13
8. [문제 257: `70ed6ff1-32a...`](#257) — single-answer, 정답: C6
9. [문제 258: `a5ab9176-12a...`](#258) — single-answer, 정답: C2
10. [문제 259: `6276ef6b-2c9...`](#259) — single-answer, 정답: C19

---

### 문제 250: `1a4cadb0-76a...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `1a4cadb0-76a8-4458-b4e0-885a9706a52f` |
| Tag | **multiple-answer** |
| 정답 | **C17|C22** |
| C17 의미 | Increase transmission power for 3270289_3 |
| C22 의미 | Adjust the azimuth of 3270289_3 by 45 degrees |
| 패턴 분류 | **P4 Coverage (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[250] topology](images/train_0250.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3270289_3
- `C2`: Add neighbor relationship between 3232399_4 and 3233895_1
- `C3`: Press down the tilt angle  of 3233895_1 by 5 degrees
- `C4`: Decrease transmission power for 3270289_3
- `C5`: Decrease transmission power for 3233895_1
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3270289_3
- `C7`: Increase A3 Offset threshold for 3233895_1
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3233895_1
- `C9`: Lift the tilt angle of 3270289_3 by 10 degrees
- `C10`: Increase transmission power for 3233895_1
- `C11`: Insufficient data; more data is needed for judgment.
- `C12`: Add neighbor relationship between 3270289_3 and 3233895_1
- `C13`: Decrease A3 Offset threshold for 3233895_1
- `C14`: Increase A3 Offset threshold for 3270289_3
- `C15`: Adjust the azimuth of 3233895_1 by 20 degrees
- `C16`: Press down the tilt angle of 3270289_3 by 10 degrees
- `C17`: Increase transmission power for 3270289_3 **← 정답**
- `C18`: Lift the tilt angle  of 3233895_1 by 5 degrees
- `C19`: Check test server and transmission issues
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3233895_1
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3270289_3
- `C22`: Adjust the azimuth of 3270289_3 by 45 degrees **← 정답**

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.383 | MS1 | 121.4656596105 | 31.1446355464 | 445 | 504990 | -92.73 | 16.84 | 477.20 | 0.11 | 2.26 | 1579 |
| 2024-09-20 22:21:32.669 | MS1 | 121.4656715763 | 31.1446219843 | 445 | 504990 | -94.20 | 17.02 | 582.87 | 0.17 | 2.08 | 1571 |
| 2024-09-20 22:21:33.889 | MS1 | 121.4656733806 | 31.1446210287 | 445 | 504990 | -93.25 | 14.12 | 439.72 | 0.00 | 2.33 | 1597 |
| 2024-09-20 22:21:34.571 | MS1 | 121.4656775708 | 31.1446285694 | 445 | 504990 | -106.78 | 1.14 | 50.50 | 0.17 | 1.09 | 1596 |
| 2024-09-20 22:21:35.309 | MS1 | 121.4656619067 | 31.1446347258 | 445 | 504990 | -105.77 | 1.24 | 49.53 | 0.06 | 1.17 | 1563 |
| 2024-09-20 22:21:36.660 | MS1 | 121.4656736357 | 31.1446356146 | 445 | 504990 | -106.81 | -1.42 | 37.12 | 0.19 | 1.05 | 1590 |
| 2024-09-20 22:21:37.592 | MS1 | 121.4656766796 | 31.1446205165 | 445 | 504990 | -109.66 | 0.80 | 41.96 | 0.03 | 1.44 | 1595 |
| 2024-09-20 22:21:38.359 | MS1 | 121.4656746815 | 31.1446323136 | 445 | 504990 | -107.39 | -0.10 | 66.33 | 0.03 | 1.12 | 1571 |
| 2024-09-20 22:21:39.760 | MS1 | 121.4656765799 | 31.1446376516 | 445 | 504990 | -107.76 | 1.75 | 31.91 | 0.11 | 1.27 | 1560 |
| 2024-09-20 22:21:40.673 | MS1 | 121.4656759688 | 31.1446339099 | 445 | 504990 | -90.81 | 12.25 | 375.97 | 0.18 | 2.68 | 1564 |
| 2024-09-20 22:21:41.513 | MS1 | 121.4656779257 | 31.1446269551 | 445 | 504990 | -93.07 | 12.80 | 597.84 | 0.02 | 2.46 | 1597 |
| 2024-09-20 22:21:42.681 | MS1 | 121.4656701119 | 31.1446190437 | 445 | 504990 | -94.51 | 15.04 | 550.51 | 0.11 | 2.72 | 1565 |

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
| 3232399 | 4 | 121.4722377397 | 31.1512674536 | 125 | 6 | 1 | 48.7 | TDD | 582 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3233895 | 1 | 121.4736672966 | 31.1557026627 | 192 | 4 | 9 | 19.9 | TDD | 334 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3241237 | 2 | 121.4745430637 | 31.1469815085 | 182 | 3 | 7 | 41.7 | TDD | 787 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3270289 | 3 | 121.4666461961 | 31.1470885479 | 154 | 11 | 10 | 30.3 | TDD | 445 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:31.659 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.675 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.796 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.796 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.964 | NREventA2 | measId:1;ServCellPCI:423;Se... |
| 2024-09-20 22:21:35.114 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3233895 | 1 | 6.7324 | 14.7227 | -117.6756 | 13.0425 | 83.3656 | 0.0143 | 0.0070 |
| 2024_09_20 22:00 | 3241237 | 2 | 13.1214 | 6.0712 | -114.5717 | 12.9141 | 135.5270 | 0.0007 | 0.0015 |
| 2024_09_20 22:00 | 3270289 | 3 | 18.2410 | 15.4615 | -116.0401 | 19.9000 | 157.5830 | 0.1758 | 0.0186 |
| 2024_09_20 22:00 | 3232399 | 4 | 16.2533 | 15.1414 | -114.6167 | 5.8161 | 127.1889 | 0.0095 | 0.0138 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417189_A71DD450 | 504990 | 445 | -105.8 | 504990 | 334 | -110.2 | 504990 | 582 | -118.0 | 504990 | 787 |
| MR_1774417189_0E537031 | 504990 | 445 | -107.0 | 504990 | 334 | -109.2 | 504990 | 582 | -117.8 | 504990 | 787 |
| MR_1774417189_3C65D8E2 | 504990 | 445 | -105.6 | 504990 | 334 | -109.2 | 504990 | 582 | -116.6 | 504990 | 787 |
| MR_1774417189_C17B5D81 | 504990 | 445 | -104.9 | 504990 | 334 | -110.6 | 504990 | 582 | -117.7 | 504990 | 787 |
| MR_1774417189_422F7448 | 504990 | 445 | -108.6 | 504990 | 334 | -108.0 | 504990 | 582 | -117.2 | 504990 | 787 |
| MR_1774417189_5CA5F614 | 504990 | 445 | -106.0 | 504990 | 334 | -110.4 | 504990 | 582 | -117.9 | 504990 | 787 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 251: `c4c17a89-e0f...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `c4c17a89-e0f9-417b-9b78-0391c086f70f` |
| Tag | **single-answer** |
| 정답 | **C17** |
| C17 의미 | Add neighbor relationship between 3270143_1 and 3242555_2 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[251] topology](images/train_0251.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3270143_1
- `C2`: Decrease A3 Offset threshold for 3242555_2
- `C3`: Lift the tilt angle of 3270143_1 by 10 degrees
- `C4`: Adjust the azimuth of 3242555_2 by 35 degrees
- `C5`: Increase transmission power for 3242555_2
- `C6`: Decrease transmission power for 3242555_2
- `C7`: Check test server and transmission issues
- `C8`: Increase A3 Offset threshold for 3242555_2
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3270143_1
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3242555_2
- `C11`: Lift the tilt angle  of 3242555_2 by 3 degrees
- `C12`: Press down the tilt angle of 3270143_1 by 10 degrees
- `C13`: Decrease transmission power for 3270143_1
- `C14`: Adjust the azimuth of 3270143_1 by 50 degrees
- `C15`: Press down the tilt angle  of 3242555_2 by 3 degrees
- `C16`: Add neighbor relationship between 3254194_4 and 3242555_2
- `C17`: Add neighbor relationship between 3270143_1 and 3242555_2 **← 정답**
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3270143_1
- `C19`: Increase A3 Offset threshold for 3270143_1
- `C20`: Insufficient data; more data is needed for judgment.
- `C21`: Increase transmission power for 3270143_1
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3242555_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.820 | MS1 | 121.4656593715 | 31.1446374163 | 1000 | 504990 | -77.98 | 14.00 | 320.21 | 0.19 | 2.37 | 1563 |
| 2024-09-20 22:21:32.448 | MS1 | 121.4656734400 | 31.1446311537 | 1000 | 504990 | -82.74 | 15.79 | 459.13 | 0.19 | 2.61 | 1569 |
| 2024-09-20 22:21:33.153 | MS1 | 121.4656677500 | 31.1446368620 | 1000 | 504990 | -83.94 | 16.56 | 375.16 | 0.14 | 2.43 | 1589 |
| 2024-09-20 22:21:34.435 | MS1 | 121.4656649512 | 31.1446282863 | 1000 | 504990 | -86.38 | -0.00 | 38.88 | 0.09 | 1.22 | 1587 |
| 2024-09-20 22:21:35.147 | MS1 | 121.4656629108 | 31.1446235281 | 1000 | 504990 | -86.14 | -3.51 | 39.55 | 0.04 | 1.16 | 1597 |
| 2024-09-20 22:21:36.417 | MS1 | 121.4656660202 | 31.1446311526 | 1000 | 504990 | -90.93 | -1.35 | 71.43 | 0.06 | 1.27 | 1589 |
| 2024-09-20 22:21:37.927 | MS1 | 121.4656705728 | 31.1446360323 | 1000 | 504990 | -94.73 | -1.99 | 51.66 | 0.20 | 1.31 | 1588 |
| 2024-09-20 22:21:38.972 | MS1 | 121.4656680920 | 31.1446206541 | 1000 | 504990 | -82.61 | 17.73 | 528.69 | 0.08 | 1.09 | 1590 |
| 2024-09-20 22:21:39.266 | MS1 | 121.4656754119 | 31.1446272073 | 1000 | 504990 | -83.45 | 12.71 | 538.19 | 0.01 | 1.04 | 1573 |
| 2024-09-20 22:21:40.499 | MS1 | 121.4656662675 | 31.1446253658 | 1000 | 504990 | -77.34 | 15.64 | 320.16 | 0.11 | 2.62 | 1588 |
| 2024-09-20 22:21:41.289 | MS1 | 121.4656589989 | 31.1446217227 | 1000 | 504990 | -79.26 | 17.98 | 544.96 | 0.13 | 2.03 | 1567 |
| 2024-09-20 22:21:42.630 | MS1 | 121.4656598269 | 31.1446287642 | 1000 | 504990 | -79.01 | 17.97 | 410.38 | 0.12 | 2.31 | 1599 |

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
| 3242555 | 2 | 121.4735422227 | 31.1546997756 | 249 | 2 | 11 | 30.2 | TDD | 697 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3254194 | 4 | 121.4671574093 | 31.1551510089 | 70 | 7 | 1 | 48.1 | TDD | 59 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3270143 | 1 | 121.4700144129 | 31.1458017282 | 146 | 9 | 1 | 21.7 | TDD | 1000 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3271403 | 3 | 121.4716719255 | 31.1546195379 | 357 | 11 | 2 | 33.6 | TDD | 346 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |

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
| 2024-09-20 22:21:31.586 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.607 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.725 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.725 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.443 | NREventA3 | measId:2;ServCellPCI:192;Se... |
| 2024-09-20 22:21:36.443 | NREventA3 | measId:2;ServCellPCI:192;Se... |
| 2024-09-20 22:21:37.443 | NREventA3 | measId:2;ServCellPCI:192;Se... |
| 2024-09-20 22:21:39.943 | NRRRCReestablishAttempt | PCI:192 |
| 2024-09-20 22:21:39.954 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.969 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:40.090 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:40.090 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3270143 | 1 | 10.1962 | 11.6171 | -115.8188 | 12.0169 | 92.8523 | 0.0121 | 0.1120 |
| 2024_09_20 22:00 | 3242555 | 2 | 10.3385 | 9.0961 | -114.0176 | 7.0979 | 99.2375 | 0.0065 | 0.0193 |
| 2024_09_20 22:00 | 3271403 | 3 | 9.0829 | 13.3082 | -116.3670 | 14.9060 | 112.6581 | 0.0072 | 0.0157 |
| 2024_09_20 22:00 | 3254194 | 4 | 13.5247 | 5.0172 | -117.3822 | 7.1131 | 91.0274 | 0.0194 | 0.0176 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412823_638C92BC | 504990 | 697 | -80.9 | 504990 | 1000 | -86.5 | 504990 | 59 | -83.2 | 504990 | 346 |
| MR_1774412823_34580D37 | 504990 | 697 | -81.4 | 504990 | 1000 | -87.2 | 504990 | 59 | -79.9 | 504990 | 346 |
| MR_1774412823_1190BE31 | 504990 | 697 | -79.1 | 504990 | 1000 | -86.2 | 504990 | 59 | -80.8 | 504990 | 346 |
| MR_1774412823_42472E92 | 504990 | 1000 | -88.2 | 504990 | 697 | -78.9 | 504990 | 59 | -82.2 | 504990 | 346 |
| MR_1774412823_91E5943D | 504990 | 697 | -81.7 | 504990 | 1000 | -87.8 | 504990 | 59 | -81.7 | 504990 | 346 |
| MR_1774412823_040C9ABF | 504990 | 1000 | -85.4 | 504990 | 697 | -82.3 | 504990 | 59 | -81.1 | 504990 | 346 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 252: `cdc45ff2-a66...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `cdc45ff2-a66d-41f5-942f-c70aba50f9b1` |
| Tag | **single-answer** |
| 정답 | **C21** |
| C21 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3226136_1 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[252] topology](images/train_0252.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3226136_1 and 3275515_2
- `C2`: Adjust the azimuth of 3275515_2 by 10 degrees
- `C3`: Increase A3 Offset threshold for 3275515_2
- `C4`: Lift the tilt angle  of 3275515_2 by 10 degrees
- `C5`: Check test server and transmission issues
- `C6`: Decrease A3 Offset threshold for 3275515_2
- `C7`: Adjust the azimuth of 3226136_1 by 30 degrees
- `C8`: Decrease transmission power for 3275515_2
- `C9`: Decrease transmission power for 3226136_1
- `C10`: Press down the tilt angle of 3226136_1 by 5 degrees
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3226136_1
- `C12`: Increase A3 Offset threshold for 3226136_1
- `C13`: Lift the tilt angle of 3226136_1 by 5 degrees
- `C14`: Press down the tilt angle  of 3275515_2 by 10 degrees
- `C15`: Increase transmission power for 3275515_2
- `C16`: Increase transmission power for 3226136_1
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3275515_2
- `C18`: Add neighbor relationship between 3228940_4 and 3275515_2
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3275515_2
- `C20`: Insufficient data; more data is needed for judgment.
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3226136_1 **← 정답**
- `C22`: Decrease A3 Offset threshold for 3226136_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.100 | MS1 | 121.4656759356 | 31.1446224729 | 337 | 504990 | -90.44 | 15.82 | 583.18 | 0.03 | 2.81 | 1588 |
| 2024-09-20 22:21:32.927 | MS1 | 121.4656600712 | 31.1446226395 | 337 | 504990 | -90.59 | 17.43 | 464.61 | 0.16 | 2.84 | 1572 |
| 2024-09-20 22:21:33.631 | MS1 | 121.4656688130 | 31.1446207515 | 337 | 504990 | -89.68 | 13.52 | 561.01 | 0.13 | 2.52 | 1583 |
| 2024-09-20 22:21:34.122 | MS1 | 121.4656701636 | 31.1446216623 | 337 | 504990 | -89.52 | 13.88 | 66.81 | 0.54 | 2.01 | 567 |
| 2024-09-20 22:21:35.715 | MS1 | 121.4656756595 | 31.1446340568 | 337 | 504990 | -91.64 | 14.11 | 58.78 | 0.62 | 2.35 | 643 |
| 2024-09-20 22:21:36.995 | MS1 | 121.4656658165 | 31.1446275029 | 337 | 504990 | -85.25 | 15.94 | 70.86 | 0.58 | 2.74 | 554 |
| 2024-09-20 22:21:37.545 | MS1 | 121.4656583815 | 31.1446223558 | 337 | 504990 | -91.00 | 8.71 | 57.79 | 0.68 | 2.59 | 553 |
| 2024-09-20 22:21:38.871 | MS1 | 121.4656748866 | 31.1446299651 | 337 | 504990 | -90.74 | 7.27 | 75.02 | 0.66 | 2.21 | 608 |
| 2024-09-20 22:21:39.708 | MS1 | 121.4656740327 | 31.1446306415 | 337 | 504990 | -91.05 | 7.29 | 49.41 | 0.55 | 2.85 | 539 |
| 2024-09-20 22:21:40.626 | MS1 | 121.4656650619 | 31.1446256860 | 337 | 504990 | -90.57 | 11.93 | 363.42 | 0.14 | 2.33 | 1586 |
| 2024-09-20 22:21:41.468 | MS1 | 121.4656617040 | 31.1446349144 | 337 | 504990 | -89.99 | 9.81 | 417.33 | 0.16 | 2.72 | 1600 |
| 2024-09-20 22:21:42.756 | MS1 | 121.4656713707 | 31.1446334493 | 337 | 504990 | -93.29 | 9.26 | 574.85 | 0.09 | 2.42 | 1583 |

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
| 3226136 | 1 | 121.4660584609 | 31.1524748441 | 152 | 2 | 0 | 38.5 | TDD | 337 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3227463 | 3 | 121.4744265824 | 31.1486912617 | 300 | 3 | 1 | 19.1 | TDD | 563 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3228940 | 4 | 121.4697170826 | 31.1477141867 | 160 | 6 | 8 | 45.2 | TDD | 900 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3275515 | 2 | 121.4680290344 | 31.1445261042 | 283 | 9 | 9 | 32.5 | TDD | 874 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |

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
| 2024-09-20 22:21:31.280 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.417 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.417 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.098 | NREventA3 | measId:2;ServCellPCI:741;Se... |
| 2024-09-20 22:21:38.338 | NRHandoverAttempt | SourcePCI:741;SourceNR-ARFC... |
| 2024-09-20 22:21:38.382 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.393 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.531 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.531 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3226136 | 1 | 10.3522 | 6.6341 | -114.9891 | 17.4093 | 172.1764 | 0.0194 | 0.0160 |
| 2024_09_20 22:00 | 3275515 | 2 | 14.3903 | 7.7852 | -115.6080 | 9.6584 | 132.4636 | 0.0139 | 0.0178 |
| 2024_09_20 22:00 | 3227463 | 3 | 15.3381 | 5.6662 | -114.1183 | 15.3772 | 106.2968 | 0.0103 | 0.0161 |
| 2024_09_20 22:00 | 3228940 | 4 | 5.9793 | 19.3763 | -117.2125 | 19.9465 | 161.6282 | 0.0116 | 0.0081 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412802_472C8403 | 504990 | 337 | -90.4 | 504990 | 874 | -92.1 | 504990 | 900 | -100.5 | 504990 | 563 |
| MR_1774412802_AE7C712E | 504990 | 337 | -89.4 | 504990 | 874 | -93.0 | 504990 | 900 | -100.8 | 504990 | 563 |
| MR_1774412802_519D3281 | 504990 | 337 | -89.7 | 504990 | 874 | -92.2 | 504990 | 900 | -100.5 | 504990 | 563 |
| MR_1774412802_D19B6CD7 | 504990 | 337 | -89.2 | 504990 | 874 | -91.4 | 504990 | 900 | -101.4 | 504990 | 563 |
| MR_1774412802_383E49AA | 504990 | 337 | -88.1 | 504990 | 874 | -89.8 | 504990 | 900 | -100.4 | 504990 | 563 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 253: `ef9fcc75-377...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `ef9fcc75-377f-471c-abcc-341969a9afec` |
| Tag | **single-answer** |
| 정답 | **C7** |
| C7 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[253] topology](images/train_0253.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle  of 3219137_1 by 10 degrees
- `C2`: Lift the tilt angle of 3236097_3 by 8 degrees
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3219137_1
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3236097_3
- `C5`: Increase transmission power for 3219137_1
- `C6`: Decrease A3 Offset threshold for 3219137_1
- `C7`: Check test server and transmission issues **← 정답**
- `C8`: Press down the tilt angle of 3236097_3 by 8 degrees
- `C9`: Adjust the azimuth of 3236097_3 by 50 degrees
- `C10`: Add neighbor relationship between 3266848_4 and 3219137_1
- `C11`: Increase transmission power for 3236097_3
- `C12`: Press down the tilt angle  of 3219137_1 by 10 degrees
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3236097_3
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Increase A3 Offset threshold for 3219137_1
- `C16`: Add neighbor relationship between 3236097_3 and 3219137_1
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3219137_1
- `C18`: Decrease A3 Offset threshold for 3236097_3
- `C19`: Decrease transmission power for 3219137_1
- `C20`: Decrease transmission power for 3236097_3
- `C21`: Adjust the azimuth of 3219137_1 by 50 degrees
- `C22`: Increase A3 Offset threshold for 3236097_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.467 | MS1 | 121.4656733998 | 31.1446339016 | 45 | 504990 | -89.58 | 15.48 | 327.86 | 0.10 | 2.13 | 1593 |
| 2024-09-20 22:21:32.494 | MS1 | 121.4656624046 | 31.1446363143 | 45 | 504990 | -89.81 | 13.53 | 317.69 | 0.14 | 2.62 | 1579 |
| 2024-09-20 22:21:33.907 | MS1 | 121.4656763667 | 31.1446212349 | 45 | 504990 | -91.50 | 16.39 | 438.81 | 0.08 | 2.54 | 1578 |
| 2024-09-20 22:21:34.612 | MS1 | 121.4656652390 | 31.1446221164 | 45 | 504990 | -85.11 | 17.81 | 77.00 | 0.18 | 2.80 | 439 |
| 2024-09-20 22:21:35.285 | MS1 | 121.4656625301 | 31.1446295190 | 45 | 504990 | -86.49 | 13.52 | 91.43 | 0.19 | 2.59 | 364 |
| 2024-09-20 22:21:36.579 | MS1 | 121.4656757017 | 31.1446181426 | 45 | 504990 | -91.45 | 16.63 | 87.66 | 0.09 | 2.32 | 473 |
| 2024-09-20 22:21:37.444 | MS1 | 121.4656674731 | 31.1446290244 | 45 | 504990 | -93.48 | 7.64 | 74.63 | 0.11 | 2.52 | 323 |
| 2024-09-20 22:21:38.823 | MS1 | 121.4656767124 | 31.1446351842 | 45 | 504990 | -89.12 | 9.86 | 97.92 | 0.12 | 2.33 | 380 |
| 2024-09-20 22:21:39.787 | MS1 | 121.4656711137 | 31.1446270720 | 45 | 504990 | -92.02 | 8.41 | 96.29 | 0.15 | 2.05 | 443 |
| 2024-09-20 22:21:40.135 | MS1 | 121.4656758089 | 31.1446237572 | 45 | 504990 | -92.06 | 10.23 | 584.76 | 0.01 | 2.11 | 1571 |
| 2024-09-20 22:21:41.614 | MS1 | 121.4656689776 | 31.1446329785 | 45 | 504990 | -93.78 | 9.34 | 350.29 | 0.11 | 2.17 | 1572 |
| 2024-09-20 22:21:42.428 | MS1 | 121.4656605196 | 31.1446257303 | 45 | 504990 | -92.63 | 8.34 | 353.83 | 0.02 | 2.30 | 1590 |

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
| 3219137 | 1 | 121.4707808150 | 31.1544341677 | 271 | 8 | 4 | 37.9 | TDD | 136 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3236097 | 3 | 121.4671618466 | 31.1550349228 | 112 | 6 | 10 | 36.1 | TDD | 45 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3256266 | 2 | 121.4724717553 | 31.1533831159 | 236 | 14 | 4 | 34.2 | TDD | 648 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3266848 | 4 | 121.4643751223 | 31.1494305428 | 160 | 10 | 6 | 38.3 | TDD | 453 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |

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
| 2024-09-20 22:21:31.664 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.808 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.808 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.486 | NREventA3 | measId:2;ServCellPCI:921;Se... |
| 2024-09-20 22:21:38.726 | NRHandoverAttempt | SourcePCI:921;SourceNR-ARFC... |
| 2024-09-20 22:21:38.760 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.773 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.875 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.875 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3219137 | 1 | 6.2565 | 18.5005 | -116.8576 | 11.8891 | 189.9291 | 0.0104 | 0.0018 |
| 2024_09_20 22:00 | 3256266 | 2 | 7.7571 | 12.9169 | -116.2162 | 16.4758 | 183.8162 | 0.0172 | 0.0091 |
| 2024_09_20 22:00 | 3236097 | 3 | 12.2406 | 15.1279 | -117.3825 | 19.4300 | 136.1702 | 0.0155 | 0.0024 |
| 2024_09_20 22:00 | 3266848 | 4 | 14.0912 | 8.7970 | -114.1147 | 12.2156 | 162.5207 | 0.0031 | 0.0043 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414493_8CDAE8EC | 504990 | 45 | -84.0 | 504990 | 136 | -88.8 | 504990 | 453 | -94.8 | 504990 | 648 |
| MR_1774414493_9E1FBB10 | 504990 | 45 | -86.0 | 504990 | 136 | -87.4 | 504990 | 453 | -95.4 | 504990 | 648 |
| MR_1774414493_322ED38A | 504990 | 45 | -84.5 | 504990 | 136 | -87.8 | 504990 | 453 | -94.3 | 504990 | 648 |
| MR_1774414493_5E192AA6 | 504990 | 45 | -83.5 | 504990 | 136 | -90.7 | 504990 | 453 | -95.4 | 504990 | 648 |
| MR_1774414493_50A80D8A | 504990 | 45 | -87.0 | 504990 | 136 | -86.9 | 504990 | 453 | -94.4 | 504990 | 648 |
| MR_1774414493_D7E85A74 | 504990 | 45 | -84.0 | 504990 | 136 | -89.0 | 504990 | 453 | -92.9 | 504990 | 648 |
| MR_1774414493_AD077A62 | 504990 | 45 | -85.1 | 504990 | 136 | -87.4 | 504990 | 453 | -93.7 | 504990 | 648 |
| MR_1774414493_F2BC2E38 | 504990 | 45 | -83.5 | 504990 | 136 | -90.0 | 504990 | 453 | -92.4 | 504990 | 648 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 254: `a29f23ec-e0d...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `a29f23ec-e0da-46f9-98be-0d18e1817c37` |
| Tag | **single-answer** |
| 정답 | **C14** |
| C14 의미 | Decrease A3 Offset threshold for 3235178_3 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[254] topology](images/train_0254.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3260063_2
- `C2`: Adjust the azimuth of 3260063_2 by 50 degrees
- `C3`: Press down the tilt angle of 3235178_3 by 10 degrees
- `C4`: Decrease transmission power for 3235178_3
- `C5`: Increase A3 Offset threshold for 3260063_2
- `C6`: Decrease transmission power for 3260063_2
- `C7`: Check test server and transmission issues
- `C8`: Adjust the azimuth of 3235178_3 by 50 degrees
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3260063_2
- `C10`: Insufficient data; more data is needed for judgment.
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3260063_2
- `C12`: Lift the tilt angle of 3235178_3 by 10 degrees
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3235178_3
- `C14`: Decrease A3 Offset threshold for 3235178_3 **← 정답**
- `C15`: Add neighbor relationship between 3235178_3 and 3260063_2
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3235178_3
- `C17`: Increase transmission power for 3235178_3
- `C18`: Increase A3 Offset threshold for 3235178_3
- `C19`: Add neighbor relationship between 3275276_4 and 3260063_2
- `C20`: Lift the tilt angle  of 3260063_2 by 10 degrees
- `C21`: Press down the tilt angle  of 3260063_2 by 10 degrees
- `C22`: Increase transmission power for 3260063_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.276 | MS1 | 121.4656658139 | 31.1446190851 | 590 | 504990 | -80.60 | 14.11 | 441.79 | 0.14 | 2.28 | 1593 |
| 2024-09-20 22:21:32.134 | MS1 | 121.4656633858 | 31.1446289443 | 590 | 504990 | -82.35 | 13.43 | 590.88 | 0.04 | 2.48 | 1572 |
| 2024-09-20 22:21:33.440 | MS1 | 121.4656650304 | 31.1446297407 | 590 | 504990 | -75.62 | 17.08 | 315.74 | 0.18 | 2.35 | 1578 |
| 2024-09-20 22:21:34.696 | MS1 | 121.4656709000 | 31.1446258588 | 590 | 504990 | -89.14 | -1.50 | 60.05 | 0.02 | 1.05 | 1566 |
| 2024-09-20 22:21:35.515 | MS1 | 121.4656612325 | 31.1446340022 | 590 | 504990 | -89.82 | -1.82 | 70.47 | 0.10 | 1.18 | 1574 |
| 2024-09-20 22:21:36.413 | MS1 | 121.4656594331 | 31.1446278675 | 590 | 504990 | -85.79 | -1.66 | 59.24 | 0.12 | 1.38 | 1582 |
| 2024-09-20 22:21:37.859 | MS1 | 121.4656607566 | 31.1446346372 | 590 | 504990 | -83.35 | -2.24 | 36.84 | 0.19 | 1.21 | 1595 |
| 2024-09-20 22:21:38.310 | MS1 | 121.4656694582 | 31.1446355510 | 590 | 504990 | -88.59 | -0.12 | 26.84 | 0.05 | 1.34 | 1586 |
| 2024-09-20 22:21:39.259 | MS1 | 121.4656711298 | 31.1446298077 | 186 | 504990 | -79.52 | 17.45 | 211.96 | 0.01 | 1.45 | 1589 |
| 2024-09-20 22:21:40.655 | MS1 | 121.4656732013 | 31.1446370556 | 186 | 504990 | -75.46 | 15.69 | 416.45 | 0.11 | 2.92 | 1592 |
| 2024-09-20 22:21:41.516 | MS1 | 121.4656662337 | 31.1446194603 | 186 | 504990 | -77.78 | 16.33 | 553.27 | 0.01 | 2.82 | 1581 |
| 2024-09-20 22:21:42.436 | MS1 | 121.4656778615 | 31.1446236694 | 186 | 504990 | -75.68 | 14.87 | 512.69 | 0.07 | 2.24 | 1580 |

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
| 3235178 | 3 | 121.4723939716 | 31.1513579840 | 107 | 8 | 9 | 41.8 | TDD | 590 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3260063 | 2 | 121.4678562005 | 31.1504173237 | 292 | 13 | 2 | 26.9 | TDD | 186 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3263951 | 1 | 121.4714144058 | 31.1488322904 | 111 | 0 | 8 | 43.7 | TDD | 344 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3275276 | 4 | 121.4706533966 | 31.1521461741 | 342 | 8 | 1 | 22.3 | TDD | 767 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |

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
| 2024-09-20 22:21:30.761 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.784 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:30.929 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.929 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.606 | NREventA3 | measId:2;ServCellPCI:607;Se... |
| 2024-09-20 22:21:37.846 | NRHandoverAttempt | SourcePCI:607;SourceNR-ARFC... |
| 2024-09-20 22:21:37.880 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.892 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.025 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.025 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3263951 | 1 | 16.3115 | 10.5145 | -116.3815 | 19.1636 | 100.7265 | 0.0008 | 0.0072 |
| 2024_09_20 22:00 | 3260063 | 2 | 12.3090 | 19.2750 | -117.5284 | 9.1862 | 175.5979 | 0.0180 | 0.0185 |
| 2024_09_20 22:00 | 3235178 | 3 | 8.3145 | 6.5492 | -114.7076 | 8.9681 | 97.2538 | 0.0192 | 0.1809 |
| 2024_09_20 22:00 | 3275276 | 4 | 5.5500 | 16.0997 | -115.8612 | 18.2477 | 167.1601 | 0.0135 | 0.0151 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416325_20A80592 | 504990 | 590 | -89.7 | 504990 | 186 | -83.9 | 504990 | 767 | -93.1 | 504990 | 344 |
| MR_1774416325_71669A44 | 504990 | 590 | -90.6 | 504990 | 186 | -84.0 | 504990 | 767 | -95.8 | 504990 | 344 |
| MR_1774416325_AE57D8A1 | 504990 | 590 | -91.1 | 504990 | 186 | -83.8 | 504990 | 767 | -95.3 | 504990 | 344 |
| MR_1774416325_763D2136 | 504990 | 186 | -84.6 | 504990 | 590 | -91.0 | 504990 | 767 | -92.5 | 504990 | 344 |
| MR_1774416325_DF108DAD | 504990 | 186 | -84.7 | 504990 | 590 | -89.1 | 504990 | 767 | -93.1 | 504990 | 344 |
| MR_1774416325_FF76323C | 504990 | 186 | -84.0 | 504990 | 590 | -89.0 | 504990 | 767 | -93.5 | 504990 | 344 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 255: `0a9ef243-6ff...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `0a9ef243-6ffe-4de3-bbae-673513f1980f` |
| Tag | **single-answer** |
| 정답 | **C15** |
| C15 의미 | Lift the tilt angle  of 3212717_1 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[255] topology](images/train_0255.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3262987_4 by 3 degrees
- `C2`: Decrease transmission power for 3274096_3
- `C3`: Adjust the azimuth of 3212717_1 by 50 degrees
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3262987_4
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3274096_3
- `C6`: Decrease A3 Offset threshold for 3274096_3
- `C7`: Increase A3 Offset threshold for 3262987_4
- `C8`: Decrease transmission power for 3262987_4
- `C9`: Increase transmission power for 3274096_3
- `C10`: Increase A3 Offset threshold for 3274096_3
- `C11`: Add neighbor relationship between 3212717_1 and 3274096_3
- `C12`: Insufficient data; more data is needed for judgment.
- `C13`: Lift the tilt angle of 3262987_4 by 3 degrees
- `C14`: Adjust the azimuth of 3262987_4 by 33 degrees
- `C15`: Lift the tilt angle  of 3212717_1 by 10 degrees **← 정답**
- `C16`: Add neighbor relationship between 3262987_4 and 3274096_3
- `C17`: Decrease A3 Offset threshold for 3262987_4
- `C18`: Increase transmission power for 3262987_4
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3262987_4
- `C20`: Check test server and transmission issues
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3274096_3
- `C22`: Press down the tilt angle  of 3212717_1 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.971 | MS1 | 121.4656755004 | 31.1446212901 | 191 | 504990 | -90.43 | 14.54 | 415.76 | 0.16 | 2.64 | 1560 |
| 2024-09-20 22:21:32.951 | MS1 | 121.4656666268 | 31.1446250364 | 191 | 504990 | -91.99 | 15.90 | 494.44 | 0.12 | 2.34 | 1598 |
| 2024-09-20 22:21:33.124 | MS1 | 121.4656678346 | 31.1446311779 | 191 | 504990 | -85.62 | 13.14 | 571.63 | 0.03 | 2.55 | 1593 |
| 2024-09-20 22:21:34.621 | MS1 | 121.4656747392 | 31.1446316831 | 191 | 504990 | -89.20 | 12.48 | 46.96 | 0.15 | 2.21 | 1572 |
| 2024-09-20 22:21:35.433 | MS1 | 121.4656646546 | 31.1446271505 | 191 | 504990 | -91.58 | 17.25 | 77.19 | 0.08 | 2.09 | 1565 |
| 2024-09-20 22:21:36.850 | MS1 | 121.4656591416 | 31.1446271791 | 191 | 504990 | -88.65 | 12.01 | 66.05 | 0.19 | 2.63 | 1578 |
| 2024-09-20 22:21:37.600 | MS1 | 121.4656672118 | 31.1446217861 | 191 | 504990 | -92.12 | 10.50 | 76.90 | 0.03 | 2.84 | 1589 |
| 2024-09-20 22:21:38.831 | MS1 | 121.4656649784 | 31.1446229003 | 191 | 504990 | -93.24 | 7.61 | 78.71 | 0.09 | 2.06 | 1582 |
| 2024-09-20 22:21:39.577 | MS1 | 121.4656718547 | 31.1446292538 | 191 | 504990 | -93.88 | 9.59 | 44.79 | 0.15 | 2.42 | 1584 |
| 2024-09-20 22:21:40.824 | MS1 | 121.4656646269 | 31.1446315867 | 191 | 504990 | -92.47 | 7.68 | 506.32 | 0.10 | 2.92 | 1591 |
| 2024-09-20 22:21:41.472 | MS1 | 121.4656621143 | 31.1446336954 | 191 | 504990 | -93.88 | 11.41 | 331.36 | 0.13 | 2.61 | 1590 |
| 2024-09-20 22:21:42.322 | MS1 | 121.4656598374 | 31.1446317881 | 191 | 504990 | -91.29 | 7.15 | 562.88 | 0.20 | 2.65 | 1581 |

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
| 3212717 | 1 | 121.4714836568 | 31.1490824434 | 42 | 9 | 10 | 49.7 | TDD | 291 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3251532 | 2 | 121.4648355629 | 31.1554381375 | 12 | 12 | 5 | 44.0 | TDD | 452 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3262987 | 4 | 121.4693139703 | 31.1545585445 | 164 | 1 | 8 | 48.0 | TDD | 191 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3274096 | 3 | 121.4700938476 | 31.1465208196 | 318 | 14 | 5 | 44.8 | TDD | 179 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |

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
| 2024-09-20 22:21:31.096 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.197 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.197 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.940 | NREventA3 | measId:2;ServCellPCI:434;Se... |
| 2024-09-20 22:21:38.180 | NRHandoverAttempt | SourcePCI:434;SourceNR-ARFC... |
| 2024-09-20 22:21:38.224 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.237 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.350 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.350 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3212717 | 1 | 13.3401 | 6.7879 | -117.3825 | 19.6741 | 142.3163 | 0.0195 | 0.0029 |
| 2024_09_20 22:00 | 3251532 | 2 | 15.3182 | 11.3213 | -116.3022 | 16.5579 | 197.5289 | 0.0178 | 0.0130 |
| 2024_09_20 22:00 | 3274096 | 3 | 12.1455 | 17.7196 | -114.1936 | 18.5125 | 119.1187 | 0.0108 | 0.0013 |
| 2024_09_20 22:00 | 3262987 | 4 | 84.3183 | 81.9271 | -114.5730 | 7.4451 | 95.4551 | 0.0072 | 0.0179 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412659_498837C7 | 504990 | 191 | -89.4 | 504990 | 179 | -90.6 | 504990 | 291 | -94.5 | 504990 | 452 |
| MR_1774412659_ABA9B64A | 504990 | 191 | -90.5 | 504990 | 179 | -89.5 | 504990 | 291 | -96.1 | 504990 | 452 |
| MR_1774412659_8269E076 | 504990 | 191 | -88.5 | 504990 | 179 | -92.1 | 504990 | 291 | -95.9 | 504990 | 452 |
| MR_1774412659_D74CE172 | 504990 | 191 | -87.5 | 504990 | 179 | -91.8 | 504990 | 291 | -95.2 | 504990 | 452 |
| MR_1774412659_B7C7C20C | 504990 | 191 | -87.9 | 504990 | 179 | -91.9 | 504990 | 291 | -96.2 | 504990 | 452 |
| MR_1774412659_F4220B4E | 504990 | 191 | -87.6 | 504990 | 179 | -89.9 | 504990 | 291 | -98.2 | 504990 | 452 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 256: `6ed3d697-e63...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `6ed3d697-e63e-4614-8047-9b6680b08ec7` |
| Tag | **single-answer** |
| 정답 | **C13** |
| C13 의미 | Lift the tilt angle  of 3218251_1 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[256] topology](images/train_0256.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3275162_2
- `C2`: Decrease A3 Offset threshold for 3275162_2
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3275162_2
- `C4`: Increase transmission power for 3275162_2
- `C5`: Add neighbor relationship between 3218251_1 and 3275162_2
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3250354_4
- `C7`: Insufficient data; more data is needed for judgment.
- `C8`: Lift the tilt angle of 3250354_4 by 4 degrees
- `C9`: Increase A3 Offset threshold for 3250354_4
- `C10`: Decrease transmission power for 3275162_2
- `C11`: Increase A3 Offset threshold for 3275162_2
- `C12`: Decrease A3 Offset threshold for 3250354_4
- `C13`: Lift the tilt angle  of 3218251_1 by 10 degrees **← 정답**
- `C14`: Increase transmission power for 3250354_4
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3250354_4
- `C16`: Adjust the azimuth of 3250354_4 by 20 degrees
- `C17`: Add neighbor relationship between 3250354_4 and 3275162_2
- `C18`: Press down the tilt angle of 3250354_4 by 4 degrees
- `C19`: Press down the tilt angle  of 3218251_1 by 10 degrees
- `C20`: Check test server and transmission issues
- `C21`: Decrease transmission power for 3250354_4
- `C22`: Adjust the azimuth of 3218251_1 by 50 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.352 | MS1 | 121.4656582913 | 31.1446377116 | 324 | 504990 | -87.80 | 12.53 | 586.48 | 0.03 | 2.40 | 1589 |
| 2024-09-20 22:21:32.830 | MS1 | 121.4656699737 | 31.1446246431 | 324 | 504990 | -87.83 | 16.30 | 478.98 | 0.08 | 2.09 | 1563 |
| 2024-09-20 22:21:33.502 | MS1 | 121.4656626219 | 31.1446228552 | 324 | 504990 | -87.08 | 14.33 | 427.13 | 0.07 | 2.27 | 1587 |
| 2024-09-20 22:21:34.784 | MS1 | 121.4656765416 | 31.1446271089 | 324 | 504990 | -91.21 | 15.11 | 78.68 | 0.10 | 2.99 | 1588 |
| 2024-09-20 22:21:35.842 | MS1 | 121.4656777838 | 31.1446327330 | 324 | 504990 | -88.60 | 13.61 | 72.04 | 0.19 | 2.21 | 1577 |
| 2024-09-20 22:21:36.205 | MS1 | 121.4656627389 | 31.1446248935 | 324 | 504990 | -85.02 | 13.12 | 50.69 | 0.13 | 2.04 | 1588 |
| 2024-09-20 22:21:37.722 | MS1 | 121.4656708859 | 31.1446353188 | 324 | 504990 | -92.80 | 8.22 | 57.33 | 0.18 | 2.44 | 1580 |
| 2024-09-20 22:21:38.729 | MS1 | 121.4656713170 | 31.1446276057 | 324 | 504990 | -90.98 | 10.72 | 86.31 | 0.11 | 2.95 | 1576 |
| 2024-09-20 22:21:39.688 | MS1 | 121.4656583535 | 31.1446275422 | 324 | 504990 | -93.05 | 7.61 | 86.04 | 0.10 | 2.52 | 1585 |
| 2024-09-20 22:21:40.487 | MS1 | 121.4656605335 | 31.1446379230 | 324 | 504990 | -89.84 | 11.60 | 396.50 | 0.01 | 2.36 | 1596 |
| 2024-09-20 22:21:41.704 | MS1 | 121.4656744037 | 31.1446311337 | 324 | 504990 | -92.01 | 12.92 | 307.92 | 0.03 | 2.30 | 1562 |
| 2024-09-20 22:21:42.209 | MS1 | 121.4656662030 | 31.1446210409 | 324 | 504990 | -93.20 | 9.55 | 428.07 | 0.09 | 2.68 | 1566 |

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
| 3218251 | 1 | 121.4653656784 | 31.1479894169 | 335 | 9 | 3 | 44.4 | TDD | 265 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3247236 | 3 | 121.4739846971 | 31.1486183017 | 300 | 2 | 3 | 23.6 | TDD | 932 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3250354 | 4 | 121.4734651989 | 31.1469440052 | 231 | 2 | 3 | 34.0 | TDD | 324 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3275162 | 2 | 121.4673779568 | 31.1455884474 | 334 | 11 | 1 | 16.4 | TDD | 418 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |

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
| 2024-09-20 22:21:31.384 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.399 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.535 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.535 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.208 | NREventA3 | measId:2;ServCellPCI:686;Se... |
| 2024-09-20 22:21:38.448 | NRHandoverAttempt | SourcePCI:686;SourceNR-ARFC... |
| 2024-09-20 22:21:38.495 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.507 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.647 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.647 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3218251 | 1 | 5.7093 | 18.0513 | -117.3488 | 18.6796 | 194.1136 | 0.0061 | 0.0007 |
| 2024_09_20 22:00 | 3275162 | 2 | 6.0219 | 5.2566 | -117.2792 | 10.3344 | 135.1676 | 0.0164 | 0.0153 |
| 2024_09_20 22:00 | 3247236 | 3 | 12.6688 | 13.2239 | -116.9611 | 12.2766 | 152.3009 | 0.0067 | 0.0166 |
| 2024_09_20 22:00 | 3250354 | 4 | 90.5408 | 92.7768 | -116.0061 | 17.5928 | 111.7227 | 0.0109 | 0.0030 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415663_241F0B35 | 504990 | 324 | -90.7 | 504990 | 418 | -91.8 | 504990 | 265 | -98.1 | 504990 | 932 |
| MR_1774415663_2AD38056 | 504990 | 324 | -91.0 | 504990 | 418 | -92.9 | 504990 | 265 | -100.2 | 504990 | 932 |
| MR_1774415663_C53D3C3D | 504990 | 324 | -90.5 | 504990 | 418 | -90.7 | 504990 | 265 | -101.1 | 504990 | 932 |
| MR_1774415663_84099E14 | 504990 | 324 | -91.4 | 504990 | 418 | -90.0 | 504990 | 265 | -98.0 | 504990 | 932 |
| MR_1774415663_F7AF6349 | 504990 | 324 | -92.6 | 504990 | 418 | -89.9 | 504990 | 265 | -99.3 | 504990 | 932 |
| MR_1774415663_37723DA6 | 504990 | 324 | -91.2 | 504990 | 418 | -93.2 | 504990 | 265 | -99.7 | 504990 | 932 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 257: `70ed6ff1-32a...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `70ed6ff1-32a0-423c-993c-e536ca85e711` |
| Tag | **single-answer** |
| 정답 | **C6** |
| C6 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[257] topology](images/train_0257.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3212029_1 by 4 degrees
- `C2`: Press down the tilt angle  of 3265960_2 by 10 degrees
- `C3`: Lift the tilt angle  of 3265960_2 by 10 degrees
- `C4`: Increase A3 Offset threshold for 3212029_1
- `C5`: Add neighbor relationship between 3254589_4 and 3265960_2
- `C6`: Insufficient data; more data is needed for judgment. **← 정답**
- `C7`: Adjust the azimuth of 3265960_2 by 50 degrees
- `C8`: Add neighbor relationship between 3212029_1 and 3265960_2
- `C9`: Check test server and transmission issues
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3265960_2
- `C11`: Decrease A3 Offset threshold for 3212029_1
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3212029_1
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3212029_1
- `C14`: Increase transmission power for 3212029_1
- `C15`: Decrease transmission power for 3265960_2
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3265960_2
- `C17`: Increase transmission power for 3265960_2
- `C18`: Lift the tilt angle of 3212029_1 by 4 degrees
- `C19`: Decrease A3 Offset threshold for 3265960_2
- `C20`: Adjust the azimuth of 3212029_1 by 50 degrees
- `C21`: Increase A3 Offset threshold for 3265960_2
- `C22`: Decrease transmission power for 3212029_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.512 | MS1 | 121.4656587415 | 31.1446200867 | 216 | 504990 | -86.54 | 13.12 | 366.86 | 0.05 | 2.22 | 1590 |
| 2024-09-20 22:21:32.536 | MS1 | 121.4656648310 | 31.1446338321 | 216 | 504990 | -86.71 | 16.35 | 453.50 | 0.16 | 2.74 | 1595 |
| 2024-09-20 22:21:33.448 | MS1 | 121.4656641379 | 31.1446283001 | 216 | 504990 | -87.07 | 17.54 | 363.08 | 0.19 | 2.65 | 1589 |
| 2024-09-20 22:21:34.390 | MS1 | 121.4656703257 | 31.1446296700 | 216 | 504990 | -86.77 | 12.52 | 103.08 | 0.17 | 2.90 | 1597 |
| 2024-09-20 22:21:35.907 | MS1 | 121.4656777666 | 31.1446196141 | 216 | 504990 | -85.75 | 17.10 | 63.16 | 0.07 | 2.27 | 1581 |
| 2024-09-20 22:21:36.681 | MS1 | 121.4656595719 | 31.1446268249 | 216 | 504990 | -85.36 | 15.53 | 86.15 | 0.20 | 2.62 | 1566 |
| 2024-09-20 22:21:37.423 | MS1 | 121.4656649061 | 31.1446337948 | 216 | 504990 | -89.07 | 8.91 | 93.71 | 0.11 | 2.17 | 1568 |
| 2024-09-20 22:21:38.985 | MS1 | 121.4656686129 | 31.1446373853 | 216 | 504990 | -92.25 | 11.33 | 57.49 | 0.14 | 2.82 | 1581 |
| 2024-09-20 22:21:39.862 | MS1 | 121.4656701242 | 31.1446226196 | 216 | 504990 | -92.12 | 11.58 | 49.90 | 0.12 | 2.08 | 1586 |
| 2024-09-20 22:21:40.275 | MS1 | 121.4656706620 | 31.1446270217 | 216 | 504990 | -93.05 | 9.93 | 380.58 | 0.03 | 2.57 | 1575 |
| 2024-09-20 22:21:41.421 | MS1 | 121.4656632329 | 31.1446358395 | 216 | 504990 | -93.67 | 12.39 | 402.39 | 0.11 | 2.56 | 1560 |
| 2024-09-20 22:21:42.612 | MS1 | 121.4656737927 | 31.1446333685 | 216 | 504990 | -90.72 | 9.73 | 486.04 | 0.13 | 2.26 | 1597 |

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
| 3212029 | 1 | 121.4734757668 | 31.1465497531 | 202 | 2 | 7 | 21.5 | TDD | 216 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3245110 | 3 | 121.4746707433 | 31.1544874737 | 308 | 8 | 11 | 48.2 | TDD | 616 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3254589 | 4 | 121.4651845663 | 31.1503050780 | 150 | 13 | 2 | 21.3 | TDD | 829 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3265960 | 2 | 121.4687492446 | 31.1528567595 | 336 | 15 | 4 | 46.1 | TDD | 749 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |

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
| 2024-09-20 22:21:30.812 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:30.933 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.933 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.644 | NREventA3 | measId:2;ServCellPCI:290;Se... |
| 2024-09-20 22:21:37.884 | NRHandoverAttempt | SourcePCI:290;SourceNR-ARFC... |
| 2024-09-20 22:21:37.930 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.942 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.066 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.066 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3212029 | 1 | 93.3342 | 94.6663 | -114.9384 | 7.9934 | 131.6520 | 0.0153 | 0.0124 |
| 2024_09_19 22:00 | 3265960 | 2 | 75.1059 | 79.7455 | -117.0661 | 5.9391 | 167.3338 | 0.0166 | 0.0077 |
| 2024_09_19 22:00 | 3245110 | 3 | 87.5645 | 79.3397 | -117.5361 | 9.4022 | 121.3881 | 0.0177 | 0.0005 |
| 2024_09_19 22:00 | 3254589 | 4 | 87.1935 | 85.7586 | -117.0806 | 15.3296 | 148.9970 | 0.0089 | 0.0049 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413367_E3DB5237 | 504990 | 216 | -86.6 | 504990 | 749 | -92.6 | 504990 | 829 | -92.2 | 504990 | 616 |
| MR_1774413367_0B72862A | 504990 | 216 | -85.1 | 504990 | 749 | -94.0 | 504990 | 829 | -95.8 | 504990 | 616 |
| MR_1774413367_884DDC86 | 504990 | 216 | -84.7 | 504990 | 749 | -93.4 | 504990 | 829 | -94.0 | 504990 | 616 |
| MR_1774413367_80828437 | 504990 | 216 | -85.4 | 504990 | 749 | -95.2 | 504990 | 829 | -93.6 | 504990 | 616 |
| MR_1774413367_510357DF | 504990 | 216 | -87.0 | 504990 | 749 | -94.8 | 504990 | 829 | -92.7 | 504990 | 616 |
| MR_1774413367_1375434C | 504990 | 216 | -87.2 | 504990 | 749 | -91.3 | 504990 | 829 | -91.9 | 504990 | 616 |
| MR_1774413367_9925E185 | 504990 | 216 | -84.5 | 504990 | 749 | -94.8 | 504990 | 829 | -93.3 | 504990 | 616 |
| MR_1774413367_4B1A69C6 | 504990 | 216 | -86.4 | 504990 | 749 | -93.8 | 504990 | 829 | -94.9 | 504990 | 616 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 258: `a5ab9176-12a...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `a5ab9176-12a3-4fdb-b9d5-39d1c1d85e9d` |
| Tag | **single-answer** |
| 정답 | **C2** |
| C2 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[258] topology](images/train_0258.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3258474_1
- `C2`: Check test server and transmission issues **← 정답**
- `C3`: Increase A3 Offset threshold for 3258474_1
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3258474_1
- `C5`: Increase transmission power for 3258474_1
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3243294_4
- `C7`: Lift the tilt angle  of 3243294_4 by 4 degrees
- `C8`: Press down the tilt angle  of 3243294_4 by 4 degrees
- `C9`: Increase A3 Offset threshold for 3243294_4
- `C10`: Adjust the azimuth of 3243294_4 by 50 degrees
- `C11`: Press down the tilt angle of 3258474_1 by 10 degrees
- `C12`: Decrease transmission power for 3243294_4
- `C13`: Lift the tilt angle of 3258474_1 by 10 degrees
- `C14`: Decrease A3 Offset threshold for 3243294_4
- `C15`: Insufficient data; more data is needed for judgment.
- `C16`: Add neighbor relationship between 3258474_1 and 3243294_4
- `C17`: Decrease A3 Offset threshold for 3258474_1
- `C18`: Add neighbor relationship between 3260675_2 and 3243294_4
- `C19`: Increase transmission power for 3243294_4
- `C20`: Adjust the azimuth of 3258474_1 by 50 degrees
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3243294_4
- `C22`: Decrease transmission power for 3258474_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.354 | MS1 | 121.4656596782 | 31.1446217938 | 552 | 504990 | -91.50 | 16.89 | 585.15 | 0.19 | 2.65 | 1571 |
| 2024-09-20 22:21:32.430 | MS1 | 121.4656589443 | 31.1446341597 | 552 | 504990 | -86.74 | 14.71 | 361.03 | 0.00 | 2.22 | 1577 |
| 2024-09-20 22:21:33.545 | MS1 | 121.4656681378 | 31.1446229974 | 552 | 504990 | -89.17 | 13.34 | 302.64 | 0.13 | 2.34 | 1565 |
| 2024-09-20 22:21:34.736 | MS1 | 121.4656740582 | 31.1446320903 | 552 | 504990 | -87.72 | 15.01 | 93.18 | 0.02 | 2.67 | 367 |
| 2024-09-20 22:21:35.281 | MS1 | 121.4656629823 | 31.1446362076 | 552 | 504990 | -86.95 | 12.27 | 82.71 | 0.17 | 2.86 | 435 |
| 2024-09-20 22:21:36.983 | MS1 | 121.4656666524 | 31.1446311885 | 552 | 504990 | -90.03 | 15.73 | 108.46 | 0.06 | 2.11 | 386 |
| 2024-09-20 22:21:37.915 | MS1 | 121.4656705537 | 31.1446325597 | 552 | 504990 | -91.04 | 8.95 | 93.52 | 0.15 | 2.71 | 369 |
| 2024-09-20 22:21:38.845 | MS1 | 121.4656626608 | 31.1446309691 | 552 | 504990 | -92.54 | 9.83 | 57.26 | 0.11 | 2.57 | 348 |
| 2024-09-20 22:21:39.607 | MS1 | 121.4656640676 | 31.1446377837 | 552 | 504990 | -92.02 | 7.68 | 84.95 | 0.17 | 2.82 | 379 |
| 2024-09-20 22:21:40.228 | MS1 | 121.4656627048 | 31.1446264826 | 552 | 504990 | -92.88 | 8.68 | 358.57 | 0.06 | 2.31 | 1574 |
| 2024-09-20 22:21:41.243 | MS1 | 121.4656656997 | 31.1446367987 | 552 | 504990 | -93.12 | 7.85 | 502.32 | 0.19 | 2.77 | 1570 |
| 2024-09-20 22:21:42.468 | MS1 | 121.4656596916 | 31.1446333040 | 552 | 504990 | -90.46 | 8.70 | 477.27 | 0.04 | 2.62 | 1595 |

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
| 3230657 | 3 | 121.4730214388 | 31.1515240879 | 157 | 11 | 10 | 25.1 | TDD | 590 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3243294 | 4 | 121.4708046898 | 31.1502124395 | 309 | 2 | 8 | 32.5 | TDD | 847 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3258474 | 1 | 121.4741868037 | 31.1440074543 | 24 | 13 | 8 | 44.7 | TDD | 552 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3260675 | 2 | 121.4681737269 | 31.1465427822 | 349 | 0 | 3 | 21.9 | TDD | 842 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |

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
| 2024-09-20 22:21:31.442 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.461 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.566 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.566 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.329 | NREventA3 | measId:2;ServCellPCI:579;Se... |
| 2024-09-20 22:21:38.569 | NRHandoverAttempt | SourcePCI:579;SourceNR-ARFC... |
| 2024-09-20 22:21:38.618 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.632 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.739 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.739 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3258474 | 1 | 16.7764 | 6.6781 | -116.7328 | 7.7475 | 142.1197 | 0.0194 | 0.0131 |
| 2024_09_20 22:00 | 3260675 | 2 | 8.5596 | 15.5347 | -115.4662 | 8.3756 | 180.5793 | 0.0086 | 0.0074 |
| 2024_09_20 22:00 | 3230657 | 3 | 7.9690 | 17.6038 | -117.2489 | 16.4138 | 177.1946 | 0.0138 | 0.0082 |
| 2024_09_20 22:00 | 3243294 | 4 | 6.0341 | 14.9898 | -114.3858 | 14.6970 | 131.5841 | 0.0094 | 0.0017 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414781_63F5C707 | 504990 | 552 | -86.5 | 504990 | 847 | -93.8 | 504990 | 842 | -101.1 | 504990 | 590 |
| MR_1774414781_E8767B55 | 504990 | 552 | -87.3 | 504990 | 847 | -92.5 | 504990 | 842 | -100.9 | 504990 | 590 |
| MR_1774414781_04844F9B | 504990 | 552 | -88.9 | 504990 | 847 | -93.9 | 504990 | 842 | -100.2 | 504990 | 590 |
| MR_1774414781_58388480 | 504990 | 552 | -87.6 | 504990 | 847 | -92.4 | 504990 | 842 | -103.6 | 504990 | 590 |
| MR_1774414781_B72AE96D | 504990 | 552 | -87.9 | 504990 | 847 | -93.7 | 504990 | 842 | -100.5 | 504990 | 590 |
| MR_1774414781_D5907A55 | 504990 | 552 | -87.1 | 504990 | 847 | -91.0 | 504990 | 842 | -101.2 | 504990 | 590 |
| MR_1774414781_76CF960E | 504990 | 552 | -87.7 | 504990 | 847 | -92.0 | 504990 | 842 | -102.3 | 504990 | 590 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 259: `6276ef6b-2c9...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `6276ef6b-2c9c-480f-b327-30238a85dbf4` |
| Tag | **single-answer** |
| 정답 | **C19** |
| C19 의미 | Add neighbor relationship between 3228021_1 and 3265603_3 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[259] topology](images/train_0259.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3228021_1
- `C2`: Decrease A3 Offset threshold for 3265603_3
- `C3`: Insufficient data; more data is needed for judgment.
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3265603_3
- `C5`: Adjust the azimuth of 3228021_1 by 50 degrees
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3228021_1
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3265603_3
- `C8`: Increase A3 Offset threshold for 3265603_3
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3228021_1
- `C10`: Press down the tilt angle  of 3265603_3 by 6 degrees
- `C11`: Increase transmission power for 3265603_3
- `C12`: Add neighbor relationship between 3252957_2 and 3265603_3
- `C13`: Decrease transmission power for 3265603_3
- `C14`: Increase transmission power for 3228021_1
- `C15`: Adjust the azimuth of 3265603_3 by 47 degrees
- `C16`: Press down the tilt angle of 3228021_1 by 10 degrees
- `C17`: Increase A3 Offset threshold for 3228021_1
- `C18`: Lift the tilt angle of 3228021_1 by 10 degrees
- `C19`: Add neighbor relationship between 3228021_1 and 3265603_3 **← 정답**
- `C20`: Lift the tilt angle  of 3265603_3 by 6 degrees
- `C21`: Check test server and transmission issues
- `C22`: Decrease transmission power for 3228021_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.785 | MS1 | 121.4656585910 | 31.1446180867 | 976 | 504990 | -81.14 | 12.54 | 568.49 | 0.02 | 2.04 | 1587 |
| 2024-09-20 22:21:32.369 | MS1 | 121.4656735785 | 31.1446276387 | 976 | 504990 | -81.85 | 16.73 | 329.08 | 0.15 | 2.43 | 1570 |
| 2024-09-20 22:21:33.249 | MS1 | 121.4656770843 | 31.1446343146 | 976 | 504990 | -79.77 | 16.82 | 320.90 | 0.15 | 2.87 | 1599 |
| 2024-09-20 22:21:34.755 | MS1 | 121.4656673612 | 31.1446353252 | 976 | 504990 | -93.92 | -0.96 | 42.37 | 0.05 | 1.33 | 1598 |
| 2024-09-20 22:21:35.179 | MS1 | 121.4656587657 | 31.1446244483 | 976 | 504990 | -86.94 | -0.28 | 46.22 | 0.07 | 1.18 | 1560 |
| 2024-09-20 22:21:36.630 | MS1 | 121.4656756063 | 31.1446372920 | 976 | 504990 | -87.57 | -3.98 | 55.52 | 0.11 | 1.13 | 1574 |
| 2024-09-20 22:21:37.340 | MS1 | 121.4656714152 | 31.1446327053 | 976 | 504990 | -92.65 | -2.97 | 35.58 | 0.07 | 1.24 | 1573 |
| 2024-09-20 22:21:38.991 | MS1 | 121.4656640864 | 31.1446270377 | 976 | 504990 | -80.36 | 12.68 | 316.10 | 0.03 | 1.47 | 1584 |
| 2024-09-20 22:21:39.893 | MS1 | 121.4656625105 | 31.1446365640 | 976 | 504990 | -80.47 | 16.48 | 431.66 | 0.01 | 1.45 | 1569 |
| 2024-09-20 22:21:40.739 | MS1 | 121.4656673959 | 31.1446294929 | 976 | 504990 | -83.93 | 16.57 | 504.72 | 0.00 | 2.74 | 1570 |
| 2024-09-20 22:21:41.381 | MS1 | 121.4656743496 | 31.1446346404 | 976 | 504990 | -76.65 | 15.93 | 499.56 | 0.10 | 2.22 | 1588 |
| 2024-09-20 22:21:42.169 | MS1 | 121.4656741460 | 31.1446331432 | 976 | 504990 | -81.41 | 14.58 | 328.58 | 0.08 | 2.25 | 1595 |

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
| 3228021 | 1 | 121.4707770171 | 31.1504703549 | 294 | 15 | 9 | 33.1 | TDD | 976 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3252957 | 2 | 121.4737636967 | 31.1447281158 | 9 | 15 | 8 | 33.8 | TDD | 730 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3261881 | 4 | 121.4725856012 | 31.1493899942 | 194 | 14 | 3 | 18.2 | TDD | 7 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3265603 | 3 | 121.4726859690 | 31.1530934460 | 168 | 5 | 0 | 16.0 | TDD | 436 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |

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
| 2024-09-20 22:21:31.263 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.283 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.428 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.428 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.153 | NREventA3 | measId:2;ServCellPCI:59;Ser... |
| 2024-09-20 22:21:36.153 | NREventA3 | measId:2;ServCellPCI:59;Ser... |
| 2024-09-20 22:21:37.153 | NREventA3 | measId:2;ServCellPCI:59;Ser... |
| 2024-09-20 22:21:39.653 | NRRRCReestablishAttempt | PCI:59 |
| 2024-09-20 22:21:39.668 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.682 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:39.810 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.810 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3228021 | 1 | 19.7036 | 12.7611 | -114.9756 | 12.8842 | 141.6601 | 0.0033 | 0.1177 |
| 2024_09_20 22:00 | 3252957 | 2 | 14.5964 | 13.0028 | -117.0734 | 10.0231 | 189.9560 | 0.0174 | 0.0044 |
| 2024_09_20 22:00 | 3265603 | 3 | 14.9355 | 18.5953 | -117.2853 | 14.3366 | 86.6138 | 0.0042 | 0.0080 |
| 2024_09_20 22:00 | 3261881 | 4 | 11.8197 | 18.4052 | -115.1160 | 19.3186 | 101.5267 | 0.0158 | 0.0064 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416563_679FCFC3 | 504990 | 436 | -88.8 | 504990 | 976 | -94.6 | 504990 | 730 | -92.8 | 504990 | 7 |
| MR_1774416563_539DB71F | 504990 | 976 | -94.1 | 504990 | 436 | -88.5 | 504990 | 730 | -93.2 | 504990 | 7 |
| MR_1774416563_725764D3 | 504990 | 976 | -94.7 | 504990 | 436 | -88.2 | 504990 | 730 | -93.8 | 504990 | 7 |
| MR_1774416563_A1A42E09 | 504990 | 436 | -89.8 | 504990 | 976 | -95.5 | 504990 | 730 | -93.5 | 504990 | 7 |
| MR_1774416563_A5083F75 | 504990 | 976 | -94.3 | 504990 | 436 | -88.8 | 504990 | 730 | -93.0 | 504990 | 7 |
| MR_1774416563_1405B776 | 504990 | 436 | -89.6 | 504990 | 976 | -92.2 | 504990 | 730 | -95.9 | 504990 | 7 |

> *... 2개 열 생략 (전체 14열)*

---
