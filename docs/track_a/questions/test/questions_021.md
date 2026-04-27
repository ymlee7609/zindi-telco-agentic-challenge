# Track A 문제 분석 — test[200]~test[209]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/test.json`
> 범위: test[200] ~ test[209] (10개)

## 목차

1. [문제 200: `25c5bb95-a47...`](#200) — single-answer
2. [문제 201: `dd382472-1c6...`](#201) — single-answer
3. [문제 202: `709f4a68-1ea...`](#202) — single-answer
4. [문제 203: `ec2a5048-42a...`](#203) — single-answer
5. [문제 204: `943d9f90-009...`](#204) — single-answer
6. [문제 205: `c1b8381c-685...`](#205) — single-answer
7. [문제 206: `09630a87-1ba...`](#206) — single-answer
8. [문제 207: `c5304405-33e...`](#207) — single-answer
9. [문제 208: `1055a805-991...`](#208) — single-answer
10. [문제 209: `5062639c-c70...`](#209) — single-answer

---

### 문제 200: `25c5bb95-a47...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `25c5bb95-a476-40d1-9b9e-705f9f046ad4` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[200] topology](images/test_0200.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3229077_2 by 4 degrees
- `C2`: Adjust the azimuth of 3229077_2 by 50 degrees
- `C3`: Decrease transmission power for 3251847_1
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3251847_1
- `C5`: Insufficient data; more data is needed for judgment.
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3251847_1
- `C7`: Press down the tilt angle  of 3251847_1 by 7 degrees
- `C8`: Check test server and transmission issues
- `C9`: Press down the tilt angle of 3229077_2 by 4 degrees
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3229077_2
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3229077_2
- `C12`: Adjust the azimuth of 3251847_1 by 50 degrees
- `C13`: Decrease A3 Offset threshold for 3251847_1
- `C14`: Decrease A3 Offset threshold for 3229077_2
- `C15`: Increase transmission power for 3251847_1
- `C16`: Add neighbor relationship between 3268501_4 and 3251847_1
- `C17`: Lift the tilt angle  of 3251847_1 by 7 degrees
- `C18`: Increase A3 Offset threshold for 3251847_1
- `C19`: Increase A3 Offset threshold for 3229077_2
- `C20`: Add neighbor relationship between 3229077_2 and 3251847_1
- `C21`: Decrease transmission power for 3229077_2
- `C22`: Increase transmission power for 3229077_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.290 | MS1 | 121.4656609241 | 31.1446203779 | 846 | 504990 | -90.01 | 17.47 | 542.32 | 0.07 | 2.51 | 1572 |
| 2024-09-20 22:21:32.427 | MS1 | 121.4656614687 | 31.1446250475 | 846 | 504990 | -91.98 | 17.39 | 345.01 | 0.18 | 2.14 | 1564 |
| 2024-09-20 22:21:33.390 | MS1 | 121.4656729314 | 31.1446313325 | 846 | 504990 | -86.55 | 12.41 | 352.05 | 0.14 | 2.20 | 1579 |
| 2024-09-20 22:21:34.260 | MS1 | 121.4656701213 | 31.1446344172 | 846 | 504990 | -85.95 | 15.81 | 86.47 | 0.01 | 2.14 | 1587 |
| 2024-09-20 22:21:35.678 | MS1 | 121.4656585159 | 31.1446188166 | 846 | 504990 | -87.65 | 15.29 | 80.71 | 0.07 | 2.81 | 1574 |
| 2024-09-20 22:21:36.438 | MS1 | 121.4656727650 | 31.1446228868 | 846 | 504990 | -86.65 | 13.73 | 76.32 | 0.08 | 2.52 | 1578 |
| 2024-09-20 22:21:37.322 | MS1 | 121.4656706146 | 31.1446227041 | 846 | 504990 | -89.90 | 8.47 | 75.11 | 0.02 | 2.49 | 1594 |
| 2024-09-20 22:21:38.734 | MS1 | 121.4656627768 | 31.1446354572 | 846 | 504990 | -93.34 | 12.09 | 59.63 | 0.00 | 2.76 | 1592 |
| 2024-09-20 22:21:39.511 | MS1 | 121.4656697078 | 31.1446373707 | 846 | 504990 | -91.22 | 11.09 | 79.94 | 0.04 | 2.74 | 1597 |
| 2024-09-20 22:21:40.247 | MS1 | 121.4656654997 | 31.1446321669 | 846 | 504990 | -92.47 | 10.79 | 602.24 | 0.03 | 2.34 | 1571 |
| 2024-09-20 22:21:41.781 | MS1 | 121.4656695059 | 31.1446319558 | 846 | 504990 | -92.98 | 11.88 | 497.21 | 0.07 | 2.35 | 1564 |
| 2024-09-20 22:21:42.277 | MS1 | 121.4656712973 | 31.1446255485 | 846 | 504990 | -93.52 | 10.27 | 352.79 | 0.17 | 2.88 | 1586 |

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
| 3229077 | 2 | 121.4724424781 | 31.1523318234 | 114 | 3 | 0 | 24.1 | TDD | 846 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3251847 | 1 | 121.4660383775 | 31.1545539151 | 342 | 5 | 0 | 47.1 | TDD | 240 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3268501 | 4 | 121.4659004366 | 31.1515721464 | 15 | 9 | 0 | 44.2 | TDD | 238 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3278157 | 3 | 121.4667222523 | 31.1553675505 | 198 | 2 | 6 | 26.4 | TDD | 142 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |

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
| 2024-09-20 22:21:30.757 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.772 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:30.874 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.874 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.611 | NREventA3 | measId:2;ServCellPCI:481;Se... |
| 2024-09-20 22:21:37.851 | NRHandoverAttempt | SourcePCI:481;SourceNR-ARFC... |
| 2024-09-20 22:21:37.889 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.900 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.049 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.049 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3251847 | 1 | 89.8772 | 87.5616 | -117.8988 | 14.8486 | 154.8502 | 0.0057 | 0.0007 |
| 2024_09_19 22:00 | 3229077 | 2 | 92.7793 | 93.9903 | -115.6816 | 8.5598 | 156.3179 | 0.0150 | 0.0062 |
| 2024_09_19 22:00 | 3278157 | 3 | 87.8854 | 75.9198 | -115.7543 | 19.0599 | 179.5304 | 0.0150 | 0.0020 |
| 2024_09_19 22:00 | 3268501 | 4 | 75.8632 | 92.1320 | -114.1279 | 15.5455 | 92.5356 | 0.0007 | 0.0174 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416839_A2DA7EE7 | 504990 | 846 | -84.7 | 504990 | 240 | -92.4 | 504990 | 238 | -95.0 | 504990 | 142 |
| MR_1774416839_D5400509 | 504990 | 846 | -87.0 | 504990 | 240 | -93.7 | 504990 | 238 | -96.0 | 504990 | 142 |
| MR_1774416839_182AC22A | 504990 | 846 | -84.7 | 504990 | 240 | -90.8 | 504990 | 238 | -95.6 | 504990 | 142 |
| MR_1774416839_C370521C | 504990 | 846 | -84.7 | 504990 | 240 | -92.7 | 504990 | 238 | -96.9 | 504990 | 142 |
| MR_1774416839_AA370EF7 | 504990 | 846 | -87.4 | 504990 | 240 | -94.7 | 504990 | 238 | -96.6 | 504990 | 142 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 201: `dd382472-1c6...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `dd382472-1c6c-4044-aa03-2fddddbb38c5` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[201] topology](images/test_0201.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3252884_1
- `C2`: Decrease transmission power for 3258851_3
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3258851_3
- `C4`: Increase transmission power for 3258851_3
- `C5`: Adjust the azimuth of 3258851_3 by 50 degrees
- `C6`: Add neighbor relationship between 3216062_4 and 3258851_3
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3252884_1
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3258851_3
- `C9`: Increase A3 Offset threshold for 3258851_3
- `C10`: Decrease A3 Offset threshold for 3258851_3
- `C11`: Press down the tilt angle  of 3258851_3 by 1 degrees
- `C12`: Insufficient data; more data is needed for judgment.
- `C13`: Increase transmission power for 3252884_1
- `C14`: Decrease A3 Offset threshold for 3252884_1
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3252884_1
- `C16`: Lift the tilt angle of 3252884_1 by 2 degrees
- `C17`: Add neighbor relationship between 3252884_1 and 3258851_3
- `C18`: Lift the tilt angle  of 3258851_3 by 1 degrees
- `C19`: Press down the tilt angle of 3252884_1 by 2 degrees
- `C20`: Adjust the azimuth of 3252884_1 by 17 degrees
- `C21`: Increase A3 Offset threshold for 3252884_1
- `C22`: Check test server and transmission issues

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.331 | MS1 | 121.4656733834 | 31.1446235300 | 49 | 504990 | -85.54 | 17.73 | 300.37 | 0.14 | 2.99 | 1575 |
| 2024-09-20 22:21:32.926 | MS1 | 121.4656777671 | 31.1446281413 | 49 | 504990 | -90.26 | 13.92 | 524.49 | 0.10 | 2.44 | 1572 |
| 2024-09-20 22:21:33.444 | MS1 | 121.4656699945 | 31.1446196128 | 49 | 504990 | -90.02 | 13.44 | 416.28 | 0.02 | 2.28 | 1588 |
| 2024-09-20 22:21:34.453 | MS1 | 121.4656753371 | 31.1446334592 | 49 | 504990 | -86.77 | 14.38 | 82.22 | 0.61 | 2.43 | 576 |
| 2024-09-20 22:21:35.762 | MS1 | 121.4656696662 | 31.1446320324 | 49 | 504990 | -85.39 | 17.52 | 77.14 | 0.55 | 2.73 | 506 |
| 2024-09-20 22:21:36.915 | MS1 | 121.4656747359 | 31.1446243534 | 49 | 504990 | -91.97 | 16.08 | 69.41 | 0.57 | 2.27 | 673 |
| 2024-09-20 22:21:37.619 | MS1 | 121.4656641906 | 31.1446196454 | 49 | 504990 | -90.73 | 9.20 | 52.84 | 0.57 | 2.37 | 531 |
| 2024-09-20 22:21:38.603 | MS1 | 121.4656747699 | 31.1446271041 | 49 | 504990 | -91.48 | 9.86 | 73.73 | 0.58 | 2.50 | 632 |
| 2024-09-20 22:21:39.952 | MS1 | 121.4656642030 | 31.1446334920 | 49 | 504990 | -89.00 | 8.32 | 63.64 | 0.54 | 2.47 | 580 |
| 2024-09-20 22:21:40.568 | MS1 | 121.4656630614 | 31.1446374359 | 49 | 504990 | -89.79 | 7.08 | 576.33 | 0.04 | 2.87 | 1598 |
| 2024-09-20 22:21:41.701 | MS1 | 121.4656595566 | 31.1446254982 | 49 | 504990 | -90.17 | 12.36 | 487.03 | 0.09 | 2.07 | 1581 |
| 2024-09-20 22:21:42.511 | MS1 | 121.4656668592 | 31.1446309618 | 49 | 504990 | -90.81 | 10.15 | 451.63 | 0.09 | 2.58 | 1580 |

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
| 3216062 | 4 | 121.4742052197 | 31.1522733706 | 180 | 12 | 5 | 34.9 | TDD | 263 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3252884 | 1 | 121.4716907847 | 31.1544160052 | 191 | 1 | 0 | 18.0 | TDD | 49 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3258851 | 3 | 121.4663930904 | 31.1547548314 | 1 | 0 | 2 | 24.1 | TDD | 419 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3271434 | 2 | 121.4717198021 | 31.1498359716 | 248 | 4 | 10 | 36.2 | TDD | 891 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |

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
| 2024-09-20 22:21:31.542 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.559 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.693 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.693 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.388 | NREventA3 | measId:2;ServCellPCI:187;Se... |
| 2024-09-20 22:21:38.628 | NRHandoverAttempt | SourcePCI:187;SourceNR-ARFC... |
| 2024-09-20 22:21:38.675 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.685 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.832 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.832 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3252884 | 1 | 18.9351 | 15.1664 | -116.3260 | 11.3263 | 143.2213 | 0.0111 | 0.0003 |
| 2024_09_20 22:00 | 3271434 | 2 | 7.6192 | 5.3458 | -117.4296 | 7.2839 | 182.9538 | 0.0165 | 0.0113 |
| 2024_09_20 22:00 | 3258851 | 3 | 10.9411 | 8.7396 | -117.8173 | 10.8978 | 171.5113 | 0.0197 | 0.0013 |
| 2024_09_20 22:00 | 3216062 | 4 | 5.9649 | 16.8971 | -115.7653 | 6.4581 | 109.8169 | 0.0035 | 0.0108 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414464_390F211D | 504990 | 49 | -88.5 | 504990 | 419 | -87.5 | 504990 | 263 | -98.0 | 504990 | 891 |
| MR_1774414464_BEAE3CB6 | 504990 | 49 | -86.2 | 504990 | 419 | -88.6 | 504990 | 263 | -97.2 | 504990 | 891 |
| MR_1774414464_6A8057FC | 504990 | 49 | -87.7 | 504990 | 419 | -88.1 | 504990 | 263 | -98.5 | 504990 | 891 |
| MR_1774414464_71090BAE | 504990 | 49 | -86.7 | 504990 | 419 | -87.7 | 504990 | 263 | -96.8 | 504990 | 891 |
| MR_1774414464_E9A7C06D | 504990 | 49 | -88.1 | 504990 | 419 | -88.7 | 504990 | 263 | -95.7 | 504990 | 891 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 202: `709f4a68-1ea...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `709f4a68-1ea9-4816-8b49-3fe58ba7e4c8` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[202] topology](images/test_0202.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment.
- `C2`: Decrease transmission power for 3226327_2
- `C3`: Adjust the azimuth of 3264712_1 by 50 degrees
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3264712_1
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3226327_2
- `C6`: Adjust the azimuth of 3226327_2 by 50 degrees
- `C7`: Add neighbor relationship between 3241120_4 and 3226327_2
- `C8`: Lift the tilt angle of 3264712_1 by 6 degrees
- `C9`: Add neighbor relationship between 3264712_1 and 3226327_2
- `C10`: Press down the tilt angle  of 3226327_2 by 8 degrees
- `C11`: Increase A3 Offset threshold for 3226327_2
- `C12`: Decrease transmission power for 3264712_1
- `C13`: Increase transmission power for 3264712_1
- `C14`: Check test server and transmission issues
- `C15`: Decrease A3 Offset threshold for 3226327_2
- `C16`: Lift the tilt angle  of 3226327_2 by 8 degrees
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3264712_1
- `C18`: Decrease A3 Offset threshold for 3264712_1
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3226327_2
- `C20`: Press down the tilt angle of 3264712_1 by 6 degrees
- `C21`: Increase transmission power for 3226327_2
- `C22`: Increase A3 Offset threshold for 3264712_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.749 | MS1 | 121.4656710392 | 31.1446316086 | 625 | 504990 | -85.16 | 16.42 | 478.41 | 0.12 | 2.82 | 1593 |
| 2024-09-20 22:21:32.853 | MS1 | 121.4656725654 | 31.1446256706 | 625 | 504990 | -88.13 | 16.59 | 567.59 | 0.10 | 2.69 | 1583 |
| 2024-09-20 22:21:33.891 | MS1 | 121.4656635353 | 31.1446367237 | 625 | 504990 | -91.33 | 15.79 | 528.13 | 0.13 | 2.70 | 1586 |
| 2024-09-20 22:21:34.136 | MS1 | 121.4656586139 | 31.1446254321 | 625 | 504990 | -87.55 | 12.67 | 84.20 | 0.14 | 2.24 | 423 |
| 2024-09-20 22:21:35.410 | MS1 | 121.4656640515 | 31.1446323032 | 625 | 504990 | -91.94 | 13.07 | 80.99 | 0.17 | 2.75 | 303 |
| 2024-09-20 22:21:36.671 | MS1 | 121.4656625016 | 31.1446198649 | 625 | 504990 | -91.72 | 12.82 | 58.36 | 0.18 | 2.66 | 412 |
| 2024-09-20 22:21:37.608 | MS1 | 121.4656618428 | 31.1446207431 | 625 | 504990 | -90.90 | 12.02 | 64.34 | 0.04 | 2.21 | 419 |
| 2024-09-20 22:21:38.138 | MS1 | 121.4656652968 | 31.1446223413 | 625 | 504990 | -93.96 | 11.93 | 82.93 | 0.13 | 2.01 | 304 |
| 2024-09-20 22:21:39.493 | MS1 | 121.4656757464 | 31.1446262913 | 625 | 504990 | -92.19 | 12.95 | 84.72 | 0.06 | 2.71 | 328 |
| 2024-09-20 22:21:40.556 | MS1 | 121.4656691450 | 31.1446350046 | 625 | 504990 | -92.91 | 12.62 | 381.40 | 0.09 | 2.15 | 1567 |
| 2024-09-20 22:21:41.109 | MS1 | 121.4656604000 | 31.1446223946 | 625 | 504990 | -90.37 | 8.88 | 462.88 | 0.19 | 2.71 | 1594 |
| 2024-09-20 22:21:42.555 | MS1 | 121.4656700912 | 31.1446323288 | 625 | 504990 | -89.47 | 7.27 | 435.78 | 0.19 | 2.21 | 1572 |

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
| 3226327 | 2 | 121.4713727289 | 31.1483244321 | 335 | 4 | 8 | 46.3 | TDD | 699 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3227047 | 3 | 121.4738926225 | 31.1458340955 | 260 | 2 | 9 | 22.6 | TDD | 468 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3241120 | 4 | 121.4728723078 | 31.1532139115 | 195 | 1 | 0 | 41.3 | TDD | 817 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3264712 | 1 | 121.4697486757 | 31.1476698802 | 41 | 3 | 12 | 25.1 | TDD | 625 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:31.450 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.469 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.595 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.595 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.306 | NREventA3 | measId:2;ServCellPCI:435;Se... |
| 2024-09-20 22:21:38.546 | NRHandoverAttempt | SourcePCI:435;SourceNR-ARFC... |
| 2024-09-20 22:21:38.579 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.590 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.733 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.733 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3264712 | 1 | 15.3322 | 15.8826 | -114.5745 | 14.6954 | 144.4398 | 0.0062 | 0.0101 |
| 2024_09_20 22:00 | 3226327 | 2 | 14.2405 | 11.5874 | -114.4246 | 15.7098 | 191.2564 | 0.0048 | 0.0188 |
| 2024_09_20 22:00 | 3227047 | 3 | 7.0405 | 13.3602 | -114.0911 | 8.5001 | 149.1328 | 0.0051 | 0.0161 |
| 2024_09_20 22:00 | 3241120 | 4 | 18.9024 | 9.9691 | -114.5964 | 11.3620 | 173.7811 | 0.0156 | 0.0060 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414584_9D420F87 | 504990 | 625 | -89.2 | 504990 | 699 | -94.2 | 504990 | 817 | -103.6 | 504990 | 468 |
| MR_1774414584_27F043E5 | 504990 | 625 | -89.5 | 504990 | 699 | -93.0 | 504990 | 817 | -100.7 | 504990 | 468 |
| MR_1774414584_32AAE8EA | 504990 | 625 | -85.9 | 504990 | 699 | -94.2 | 504990 | 817 | -103.5 | 504990 | 468 |
| MR_1774414584_65554209 | 504990 | 625 | -88.3 | 504990 | 699 | -94.8 | 504990 | 817 | -102.0 | 504990 | 468 |
| MR_1774414584_A812A8F4 | 504990 | 625 | -87.4 | 504990 | 699 | -93.3 | 504990 | 817 | -101.5 | 504990 | 468 |
| MR_1774414584_71407E0F | 504990 | 625 | -86.7 | 504990 | 699 | -93.5 | 504990 | 817 | -102.9 | 504990 | 468 |
| MR_1774414584_B5221994 | 504990 | 625 | -87.2 | 504990 | 699 | -95.2 | 504990 | 817 | -100.8 | 504990 | 468 |
| MR_1774414584_1080E323 | 504990 | 625 | -86.1 | 504990 | 699 | -93.5 | 504990 | 817 | -102.7 | 504990 | 468 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 203: `ec2a5048-42a...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `ec2a5048-42a0-4ae9-999b-67263bdc2f90` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[203] topology](images/test_0203.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3262023_2
- `C2`: Press down the tilt angle  of 3232392_1 by 5 degrees
- `C3`: Adjust the azimuth of 3232392_1 by 20 degrees
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3262023_2
- `C5`: Insufficient data; more data is needed for judgment.
- `C6`: Decrease A3 Offset threshold for 3262023_2
- `C7`: Increase transmission power for 3232392_1
- `C8`: Increase A3 Offset threshold for 3262023_2
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3232392_1
- `C10`: Press down the tilt angle of 3262023_2 by 10 degrees
- `C11`: Lift the tilt angle  of 3232392_1 by 5 degrees
- `C12`: Add neighbor relationship between 3258253_4 and 3232392_1
- `C13`: Decrease transmission power for 3262023_2
- `C14`: Lift the tilt angle of 3262023_2 by 10 degrees
- `C15`: Adjust the azimuth of 3262023_2 by 50 degrees
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3262023_2
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3232392_1
- `C18`: Decrease A3 Offset threshold for 3232392_1
- `C19`: Check test server and transmission issues
- `C20`: Decrease transmission power for 3232392_1
- `C21`: Increase A3 Offset threshold for 3232392_1
- `C22`: Add neighbor relationship between 3262023_2 and 3232392_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.988 | MS1 | 121.4656773237 | 31.1446334814 | 41 | 504990 | -83.41 | 12.85 | 445.13 | 0.16 | 2.52 | 1564 |
| 2024-09-20 22:21:32.203 | MS1 | 121.4656621467 | 31.1446302028 | 41 | 504990 | -76.72 | 15.36 | 303.55 | 0.07 | 2.39 | 1588 |
| 2024-09-20 22:21:33.703 | MS1 | 121.4656769814 | 31.1446294927 | 41 | 504990 | -79.78 | 15.21 | 593.41 | 0.10 | 2.92 | 1572 |
| 2024-09-20 22:21:34.765 | MS1 | 121.4656658801 | 31.1446317270 | 41 | 504990 | -91.09 | -3.82 | 50.82 | 0.02 | 1.30 | 1597 |
| 2024-09-20 22:21:35.547 | MS1 | 121.4656737904 | 31.1446338229 | 41 | 504990 | -93.81 | -1.23 | 69.31 | 0.14 | 1.18 | 1586 |
| 2024-09-20 22:21:36.282 | MS1 | 121.4656698645 | 31.1446245756 | 41 | 504990 | -94.69 | -0.88 | 54.74 | 0.09 | 1.28 | 1594 |
| 2024-09-20 22:21:37.421 | MS1 | 121.4656652995 | 31.1446314595 | 41 | 504990 | -87.84 | -1.74 | 47.93 | 0.14 | 1.30 | 1585 |
| 2024-09-20 22:21:38.969 | MS1 | 121.4656707498 | 31.1446366798 | 41 | 504990 | -84.08 | 12.55 | 582.61 | 0.08 | 1.16 | 1589 |
| 2024-09-20 22:21:39.189 | MS1 | 121.4656643061 | 31.1446302564 | 41 | 504990 | -83.92 | 16.01 | 513.65 | 0.11 | 1.47 | 1579 |
| 2024-09-20 22:21:40.481 | MS1 | 121.4656581444 | 31.1446284640 | 41 | 504990 | -76.52 | 16.77 | 547.43 | 0.15 | 2.04 | 1595 |
| 2024-09-20 22:21:41.437 | MS1 | 121.4656721175 | 31.1446281347 | 41 | 504990 | -76.71 | 16.01 | 460.31 | 0.15 | 2.66 | 1589 |
| 2024-09-20 22:21:42.361 | MS1 | 121.4656752879 | 31.1446336501 | 41 | 504990 | -82.57 | 15.11 | 531.85 | 0.06 | 2.91 | 1592 |

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
| 3227708 | 3 | 121.4675493117 | 31.1559792608 | 336 | 5 | 4 | 37.2 | TDD | 586 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3232392 | 1 | 121.4753510182 | 31.1471616372 | 233 | 4 | 11 | 23.7 | TDD | 824 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3258253 | 4 | 121.4670408493 | 31.1443832401 | 170 | 0 | 3 | 46.7 | TDD | 566 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3262023 | 2 | 121.4664367438 | 31.1471864128 | 250 | 6 | 3 | 21.5 | TDD | 41 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |

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
| 2024-09-20 22:21:30.968 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.989 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.104 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.104 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.810 | NREventA3 | measId:2;ServCellPCI:336;Se... |
| 2024-09-20 22:21:35.810 | NREventA3 | measId:2;ServCellPCI:336;Se... |
| 2024-09-20 22:21:36.810 | NREventA3 | measId:2;ServCellPCI:336;Se... |
| 2024-09-20 22:21:39.310 | NRRRCReestablishAttempt | PCI:336 |
| 2024-09-20 22:21:39.329 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.341 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:39.488 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.488 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3232392 | 1 | 14.6487 | 18.7558 | -117.6298 | 17.4344 | 170.0690 | 0.0175 | 0.0046 |
| 2024_09_20 22:00 | 3262023 | 2 | 9.4664 | 6.3373 | -117.3437 | 18.6368 | 180.5139 | 0.0128 | 0.1594 |
| 2024_09_20 22:00 | 3227708 | 3 | 12.4473 | 19.5927 | -117.6924 | 9.3441 | 153.8069 | 0.0140 | 0.0096 |
| 2024_09_20 22:00 | 3258253 | 4 | 18.9227 | 13.3237 | -116.3868 | 11.2423 | 170.4686 | 0.0167 | 0.0154 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417060_DA8D267E | 504990 | 824 | -84.8 | 504990 | 41 | -92.4 | 504990 | 566 | -95.1 | 504990 | 586 |
| MR_1774417060_DBD00AB6 | 504990 | 41 | -89.3 | 504990 | 824 | -86.4 | 504990 | 566 | -96.0 | 504990 | 586 |
| MR_1774417060_0BDA5655 | 504990 | 41 | -92.9 | 504990 | 824 | -86.1 | 504990 | 566 | -94.1 | 504990 | 586 |
| MR_1774417060_2217DED8 | 504990 | 41 | -92.7 | 504990 | 824 | -87.5 | 504990 | 566 | -95.0 | 504990 | 586 |
| MR_1774417060_B86E882D | 504990 | 824 | -85.0 | 504990 | 41 | -91.3 | 504990 | 566 | -95.4 | 504990 | 586 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 204: `943d9f90-009...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `943d9f90-009b-416e-afde-497247b7f552` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[204] topology](images/test_0204.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment.
- `C2`: Decrease A3 Offset threshold for 3214274_2
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3214274_2
- `C4`: Lift the tilt angle  of 3214274_2 by 8 degrees
- `C5`: Increase transmission power for 3235893_1
- `C6`: Decrease transmission power for 3214274_2
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3235893_1
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3235893_1
- `C9`: Press down the tilt angle of 3235893_1 by 10 degrees
- `C10`: Press down the tilt angle  of 3214274_2 by 8 degrees
- `C11`: Decrease transmission power for 3235893_1
- `C12`: Adjust the azimuth of 3235893_1 by 14 degrees
- `C13`: Check test server and transmission issues
- `C14`: Add neighbor relationship between 3235893_1 and 3214274_2
- `C15`: Decrease A3 Offset threshold for 3235893_1
- `C16`: Increase transmission power for 3214274_2
- `C17`: Increase A3 Offset threshold for 3235893_1
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3214274_2
- `C19`: Lift the tilt angle of 3235893_1 by 10 degrees
- `C20`: Increase A3 Offset threshold for 3214274_2
- `C21`: Adjust the azimuth of 3214274_2 by 50 degrees
- `C22`: Add neighbor relationship between 3260177_3 and 3214274_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.273 | MS1 | 121.4656596855 | 31.1446296410 | 64 | 504990 | -75.52 | 16.04 | 383.11 | 0.11 | 2.64 | 1598 |
| 2024-09-20 22:21:32.695 | MS1 | 121.4656629387 | 31.1446275399 | 64 | 504990 | -79.45 | 16.83 | 493.44 | 0.20 | 2.83 | 1590 |
| 2024-09-20 22:21:33.597 | MS1 | 121.4656726583 | 31.1446373047 | 64 | 504990 | -83.10 | 17.46 | 534.14 | 0.04 | 2.69 | 1561 |
| 2024-09-20 22:21:34.749 | MS1 | 121.4656732763 | 31.1446379010 | 64 | 504990 | -87.09 | -1.00 | 67.88 | 0.10 | 1.07 | 1595 |
| 2024-09-20 22:21:35.350 | MS1 | 121.4656594444 | 31.1446271688 | 64 | 504990 | -88.86 | -3.72 | 52.81 | 0.05 | 1.34 | 1594 |
| 2024-09-20 22:21:36.385 | MS1 | 121.4656630976 | 31.1446334944 | 64 | 504990 | -90.29 | -2.25 | 79.51 | 0.06 | 1.37 | 1578 |
| 2024-09-20 22:21:37.502 | MS1 | 121.4656750414 | 31.1446182368 | 64 | 504990 | -84.43 | -2.14 | 44.79 | 0.14 | 1.19 | 1590 |
| 2024-09-20 22:21:38.583 | MS1 | 121.4656634586 | 31.1446303515 | 64 | 504990 | -86.54 | -0.87 | 68.31 | 0.16 | 1.46 | 1592 |
| 2024-09-20 22:21:39.696 | MS1 | 121.4656655207 | 31.1446365068 | 745 | 504990 | -79.55 | 15.68 | 195.70 | 0.10 | 1.26 | 1588 |
| 2024-09-20 22:21:40.538 | MS1 | 121.4656671847 | 31.1446295269 | 745 | 504990 | -77.35 | 17.57 | 317.04 | 0.17 | 2.06 | 1590 |
| 2024-09-20 22:21:41.327 | MS1 | 121.4656594853 | 31.1446210340 | 745 | 504990 | -81.70 | 17.63 | 329.16 | 0.20 | 2.47 | 1592 |
| 2024-09-20 22:21:42.840 | MS1 | 121.4656730992 | 31.1446354695 | 745 | 504990 | -78.13 | 13.54 | 411.39 | 0.13 | 2.54 | 1576 |

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
| 3214274 | 2 | 121.4657459164 | 31.1540696680 | 6 | 6 | 6 | 29.3 | TDD | 745 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3230068 | 4 | 121.4714133297 | 31.1530812660 | 295 | 1 | 3 | 37.0 | TDD | 756 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3235893 | 1 | 121.4662499060 | 31.1558551980 | 169 | 12 | 0 | 38.6 | TDD | 64 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3260177 | 3 | 121.4642317313 | 31.1482780525 | 241 | 12 | 5 | 36.6 | TDD | 883 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |

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
| 2024-09-20 22:21:31.446 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.461 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.591 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.591 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.275 | NREventA3 | measId:2;ServCellPCI:727;Se... |
| 2024-09-20 22:21:38.515 | NRHandoverAttempt | SourcePCI:727;SourceNR-ARFC... |
| 2024-09-20 22:21:38.549 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.561 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.679 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.679 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3235893 | 1 | 16.8744 | 15.4875 | -114.0265 | 7.6462 | 185.3048 | 0.0191 | 0.1663 |
| 2024_09_20 22:00 | 3214274 | 2 | 12.5600 | 10.6838 | -117.8549 | 12.3002 | 140.1263 | 0.0126 | 0.0064 |
| 2024_09_20 22:00 | 3260177 | 3 | 18.1554 | 5.5855 | -116.0435 | 19.4803 | 193.8209 | 0.0147 | 0.0057 |
| 2024_09_20 22:00 | 3230068 | 4 | 9.4431 | 16.7106 | -116.7867 | 13.2044 | 170.8187 | 0.0032 | 0.0132 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774411979_5AFC8CBF | 504990 | 64 | -85.8 | 504990 | 745 | -83.0 | 504990 | 883 | -80.7 | 504990 | 756 |
| MR_1774411979_309C39D6 | 504990 | 64 | -88.9 | 504990 | 745 | -82.1 | 504990 | 883 | -81.7 | 504990 | 756 |
| MR_1774411979_BC2415F6 | 504990 | 745 | -80.2 | 504990 | 64 | -85.2 | 504990 | 883 | -81.3 | 504990 | 756 |
| MR_1774411979_A4FC1F27 | 504990 | 64 | -85.7 | 504990 | 745 | -82.7 | 504990 | 883 | -83.3 | 504990 | 756 |
| MR_1774411979_2D65780E | 504990 | 745 | -81.9 | 504990 | 64 | -89.1 | 504990 | 883 | -84.0 | 504990 | 756 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 205: `c1b8381c-685...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `c1b8381c-6850-423c-921d-f2f3938a87aa` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[205] topology](images/test_0205.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3260411_1
- `C2`: Press down the tilt angle  of 3260411_1 by 3 degrees
- `C3`: Increase transmission power for 3226472_4
- `C4`: Lift the tilt angle  of 3260411_1 by 3 degrees
- `C5`: Lift the tilt angle of 3226472_4 by 5 degrees
- `C6`: Adjust the azimuth of 3260411_1 by 6 degrees
- `C7`: Increase A3 Offset threshold for 3260411_1
- `C8`: Decrease transmission power for 3260411_1
- `C9`: Check test server and transmission issues
- `C10`: Add neighbor relationship between 3253416_3 and 3260411_1
- `C11`: Press down the tilt angle of 3226472_4 by 5 degrees
- `C12`: Increase A3 Offset threshold for 3226472_4
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3226472_4
- `C14`: Increase transmission power for 3260411_1
- `C15`: Insufficient data; more data is needed for judgment.
- `C16`: Decrease A3 Offset threshold for 3260411_1
- `C17`: Add neighbor relationship between 3226472_4 and 3260411_1
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3260411_1
- `C19`: Adjust the azimuth of 3226472_4 by 50 degrees
- `C20`: Decrease A3 Offset threshold for 3226472_4
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3226472_4
- `C22`: Decrease transmission power for 3226472_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.943 | MS1 | 121.4656707989 | 31.1446346301 | 943 | 504990 | -84.38 | 12.33 | 307.84 | 0.18 | 2.82 | 1593 |
| 2024-09-20 22:21:32.843 | MS1 | 121.4656749651 | 31.1446318914 | 943 | 504990 | -84.38 | 13.11 | 444.56 | 0.15 | 2.44 | 1568 |
| 2024-09-20 22:21:33.268 | MS1 | 121.4656593427 | 31.1446269283 | 943 | 504990 | -79.45 | 15.48 | 513.81 | 0.09 | 2.50 | 1599 |
| 2024-09-20 22:21:34.176 | MS1 | 121.4656774670 | 31.1446335854 | 943 | 504990 | -94.57 | -0.84 | 58.54 | 0.15 | 1.41 | 1591 |
| 2024-09-20 22:21:35.122 | MS1 | 121.4656645431 | 31.1446279907 | 943 | 504990 | -88.96 | -1.51 | 41.05 | 0.12 | 1.34 | 1565 |
| 2024-09-20 22:21:36.703 | MS1 | 121.4656687067 | 31.1446192293 | 943 | 504990 | -88.20 | -2.80 | 35.28 | 0.19 | 1.19 | 1593 |
| 2024-09-20 22:21:37.980 | MS1 | 121.4656641123 | 31.1446346744 | 943 | 504990 | -91.67 | -0.73 | 47.27 | 0.08 | 1.03 | 1590 |
| 2024-09-20 22:21:38.303 | MS1 | 121.4656739217 | 31.1446359644 | 943 | 504990 | -80.65 | 13.14 | 546.28 | 0.09 | 1.20 | 1570 |
| 2024-09-20 22:21:39.622 | MS1 | 121.4656766946 | 31.1446182107 | 943 | 504990 | -82.53 | 13.51 | 520.95 | 0.13 | 1.31 | 1586 |
| 2024-09-20 22:21:40.890 | MS1 | 121.4656766362 | 31.1446284809 | 943 | 504990 | -81.07 | 17.07 | 519.22 | 0.19 | 2.10 | 1571 |
| 2024-09-20 22:21:41.950 | MS1 | 121.4656742157 | 31.1446324305 | 943 | 504990 | -80.93 | 14.50 | 474.27 | 0.01 | 2.25 | 1578 |
| 2024-09-20 22:21:42.910 | MS1 | 121.4656689326 | 31.1446362493 | 943 | 504990 | -75.10 | 17.05 | 438.07 | 0.04 | 2.40 | 1563 |

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
| 3226472 | 4 | 121.4730757027 | 31.1495516359 | 93 | 3 | 10 | 29.2 | TDD | 943 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3253416 | 3 | 121.4751611055 | 31.1499025083 | 76 | 15 | 12 | 48.7 | TDD | 938 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3260411 | 1 | 121.4700290475 | 31.1498516117 | 221 | 0 | 9 | 34.2 | TDD | 178 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3273409 | 2 | 121.4739128504 | 31.1558927702 | 192 | 11 | 3 | 34.4 | TDD | 561 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |

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
| 2024-09-20 22:21:30.739 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.757 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:30.880 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.880 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.632 | NREventA3 | measId:2;ServCellPCI:757;Se... |
| 2024-09-20 22:21:35.632 | NREventA3 | measId:2;ServCellPCI:757;Se... |
| 2024-09-20 22:21:36.632 | NREventA3 | measId:2;ServCellPCI:757;Se... |
| 2024-09-20 22:21:39.132 | NRRRCReestablishAttempt | PCI:757 |
| 2024-09-20 22:21:39.147 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.158 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:39.283 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.283 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3260411 | 1 | 10.1130 | 15.5904 | -115.6834 | 14.8822 | 123.3106 | 0.0171 | 0.0167 |
| 2024_09_20 22:00 | 3273409 | 2 | 7.2810 | 15.1605 | -116.6811 | 18.6880 | 146.6977 | 0.0131 | 0.0155 |
| 2024_09_20 22:00 | 3253416 | 3 | 12.0286 | 13.8628 | -114.5576 | 5.8682 | 177.3918 | 0.0040 | 0.0150 |
| 2024_09_20 22:00 | 3226472 | 4 | 18.4267 | 5.2322 | -115.3734 | 19.9841 | 147.5955 | 0.0141 | 0.1852 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774411988_CE044323 | 504990 | 943 | -93.8 | 504990 | 178 | -91.4 | 504990 | 938 | -98.9 | 504990 | 561 |
| MR_1774411988_44D23BCE | 504990 | 178 | -89.9 | 504990 | 943 | -94.5 | 504990 | 938 | -99.9 | 504990 | 561 |
| MR_1774411988_EC0FB572 | 504990 | 178 | -90.8 | 504990 | 943 | -92.8 | 504990 | 938 | -96.8 | 504990 | 561 |
| MR_1774411988_00A1ECA3 | 504990 | 943 | -96.1 | 504990 | 178 | -88.6 | 504990 | 938 | -97.1 | 504990 | 561 |
| MR_1774411988_DA339DEA | 504990 | 178 | -91.6 | 504990 | 943 | -94.6 | 504990 | 938 | -96.7 | 504990 | 561 |
| MR_1774411988_53888826 | 504990 | 943 | -96.0 | 504990 | 178 | -89.3 | 504990 | 938 | -99.7 | 504990 | 561 |
| MR_1774411988_47210759 | 504990 | 943 | -95.2 | 504990 | 178 | -89.1 | 504990 | 938 | -96.8 | 504990 | 561 |
| MR_1774411988_3BF6E0A3 | 504990 | 178 | -91.6 | 504990 | 943 | -92.7 | 504990 | 938 | -97.1 | 504990 | 561 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 206: `09630a87-1ba...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `09630a87-1ba8-43d4-b4b5-559de74d9a2d` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[206] topology](images/test_0206.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3237087_2
- `C2`: Increase transmission power for 3237087_2
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3239911_3
- `C4`: Adjust the azimuth of 3239911_3 by 31 degrees
- `C5`: Increase transmission power for 3239911_3
- `C6`: Decrease A3 Offset threshold for 3237087_2
- `C7`: Increase A3 Offset threshold for 3239911_3
- `C8`: Decrease transmission power for 3239911_3
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3239911_3
- `C10`: Adjust the azimuth of 3237087_2 by 50 degrees
- `C11`: Lift the tilt angle  of 3239911_3 by 6 degrees
- `C12`: Decrease A3 Offset threshold for 3239911_3
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3237087_2
- `C14`: Press down the tilt angle of 3237087_2 by 10 degrees
- `C15`: Lift the tilt angle of 3237087_2 by 10 degrees
- `C16`: Add neighbor relationship between 3278084_1 and 3239911_3
- `C17`: Check test server and transmission issues
- `C18`: Press down the tilt angle  of 3239911_3 by 6 degrees
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3237087_2
- `C20`: Insufficient data; more data is needed for judgment.
- `C21`: Decrease transmission power for 3237087_2
- `C22`: Add neighbor relationship between 3237087_2 and 3239911_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.913 | MS1 | 121.4656600051 | 31.1446258070 | 759 | 504990 | -79.41 | 17.28 | 532.12 | 0.05 | 2.09 | 1565 |
| 2024-09-20 22:21:32.487 | MS1 | 121.4656693675 | 31.1446256692 | 759 | 504990 | -82.27 | 14.14 | 516.76 | 0.16 | 2.99 | 1584 |
| 2024-09-20 22:21:33.830 | MS1 | 121.4656743480 | 31.1446368556 | 759 | 504990 | -81.27 | 13.39 | 403.11 | 0.07 | 2.90 | 1581 |
| 2024-09-20 22:21:34.581 | MS1 | 121.4656641713 | 31.1446283500 | 759 | 504990 | -85.37 | -1.03 | 47.73 | 0.02 | 1.20 | 1594 |
| 2024-09-20 22:21:35.978 | MS1 | 121.4656729941 | 31.1446211449 | 759 | 504990 | -91.13 | -0.54 | 37.02 | 0.05 | 1.26 | 1581 |
| 2024-09-20 22:21:36.596 | MS1 | 121.4656713883 | 31.1446294064 | 759 | 504990 | -91.78 | -0.23 | 43.36 | 0.19 | 1.48 | 1562 |
| 2024-09-20 22:21:37.574 | MS1 | 121.4656700942 | 31.1446201141 | 759 | 504990 | -91.77 | -3.54 | 53.31 | 0.05 | 1.05 | 1568 |
| 2024-09-20 22:21:38.578 | MS1 | 121.4656686065 | 31.1446238508 | 759 | 504990 | -80.46 | 16.75 | 565.84 | 0.13 | 1.45 | 1570 |
| 2024-09-20 22:21:39.624 | MS1 | 121.4656723947 | 31.1446256730 | 759 | 504990 | -82.23 | 16.55 | 516.86 | 0.04 | 1.30 | 1586 |
| 2024-09-20 22:21:40.714 | MS1 | 121.4656612021 | 31.1446186320 | 759 | 504990 | -79.74 | 14.23 | 330.69 | 0.19 | 2.84 | 1588 |
| 2024-09-20 22:21:41.794 | MS1 | 121.4656712279 | 31.1446182402 | 759 | 504990 | -80.80 | 14.65 | 590.85 | 0.05 | 2.51 | 1567 |
| 2024-09-20 22:21:42.245 | MS1 | 121.4656635163 | 31.1446229699 | 759 | 504990 | -84.15 | 15.03 | 394.21 | 0.10 | 2.65 | 1595 |

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
| 3237087 | 2 | 121.4667381261 | 31.1512905473 | 110 | 11 | 4 | 27.5 | TDD | 759 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3239911 | 3 | 121.4755478715 | 31.1551173928 | 250 | 5 | 5 | 19.1 | TDD | 214 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3255456 | 4 | 121.4663366015 | 31.1495362910 | 117 | 2 | 4 | 26.2 | TDD | 815 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3278084 | 1 | 121.4703640764 | 31.1479078734 | 108 | 1 | 12 | 41.5 | TDD | 129 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:31.068 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.092 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.195 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.195 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.956 | NREventA3 | measId:2;ServCellPCI:204;Se... |
| 2024-09-20 22:21:35.956 | NREventA3 | measId:2;ServCellPCI:204;Se... |
| 2024-09-20 22:21:36.956 | NREventA3 | measId:2;ServCellPCI:204;Se... |
| 2024-09-20 22:21:39.456 | NRRRCReestablishAttempt | PCI:204 |
| 2024-09-20 22:21:39.468 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.479 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:39.622 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.622 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3278084 | 1 | 8.6496 | 16.2963 | -114.8206 | 9.1081 | 87.0017 | 0.0142 | 0.0093 |
| 2024_09_20 22:00 | 3237087 | 2 | 18.4333 | 10.9474 | -115.5971 | 19.3371 | 160.2537 | 0.0101 | 0.1633 |
| 2024_09_20 22:00 | 3239911 | 3 | 8.9400 | 6.7660 | -115.7748 | 10.0504 | 136.5565 | 0.0156 | 0.0136 |
| 2024_09_20 22:00 | 3255456 | 4 | 19.1465 | 16.8996 | -115.7911 | 12.1628 | 85.4836 | 0.0077 | 0.0052 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413774_9A440E10 | 504990 | 759 | -83.6 | 504990 | 214 | -78.4 | 504990 | 129 | -84.6 | 504990 | 815 |
| MR_1774413774_C5853800 | 504990 | 759 | -85.7 | 504990 | 214 | -81.3 | 504990 | 129 | -86.8 | 504990 | 815 |
| MR_1774413774_A8F523AC | 504990 | 214 | -79.9 | 504990 | 759 | -85.6 | 504990 | 129 | -85.5 | 504990 | 815 |
| MR_1774413774_DDA76B6C | 504990 | 214 | -78.7 | 504990 | 759 | -86.1 | 504990 | 129 | -87.7 | 504990 | 815 |
| MR_1774413774_47C983C9 | 504990 | 214 | -81.5 | 504990 | 759 | -83.4 | 504990 | 129 | -87.6 | 504990 | 815 |
| MR_1774413774_C2F7794A | 504990 | 759 | -84.7 | 504990 | 214 | -79.0 | 504990 | 129 | -84.9 | 504990 | 815 |
| MR_1774413774_E736A120 | 504990 | 214 | -80.6 | 504990 | 759 | -85.5 | 504990 | 129 | -86.0 | 504990 | 815 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 207: `c5304405-33e...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `c5304405-33e4-4bf4-9f23-32d8328d0c12` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[207] topology](images/test_0207.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3279394_1
- `C2`: Add neighbor relationship between 3276561_3 and 3279394_1
- `C3`: Decrease transmission power for 3279394_1
- `C4`: Adjust the azimuth of 3276561_3 by 50 degrees
- `C5`: Press down the tilt angle  of 3276561_3 by 5 degrees
- `C6`: Insufficient data; more data is needed for judgment.
- `C7`: Add neighbor relationship between 3255718_2 and 3279394_1
- `C8`: Press down the tilt angle of 3255718_2 by 3 degrees
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3279394_1
- `C10`: Increase transmission power for 3279394_1
- `C11`: Adjust the azimuth of 3255718_2 by 16 degrees
- `C12`: Increase A3 Offset threshold for 3255718_2
- `C13`: Decrease A3 Offset threshold for 3255718_2
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3279394_1
- `C15`: Increase A3 Offset threshold for 3279394_1
- `C16`: Lift the tilt angle of 3255718_2 by 3 degrees
- `C17`: Check test server and transmission issues
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3255718_2
- `C19`: Lift the tilt angle  of 3276561_3 by 5 degrees
- `C20`: Increase transmission power for 3255718_2
- `C21`: Decrease transmission power for 3255718_2
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3255718_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.849 | MS1 | 121.4656635575 | 31.1446196904 | 866 | 504990 | -89.47 | 16.97 | 382.73 | 0.15 | 2.31 | 1566 |
| 2024-09-20 22:21:32.165 | MS1 | 121.4656580805 | 31.1446373597 | 866 | 504990 | -87.81 | 14.19 | 536.82 | 0.09 | 2.45 | 1594 |
| 2024-09-20 22:21:33.642 | MS1 | 121.4656774671 | 31.1446223969 | 866 | 504990 | -91.99 | 17.07 | 562.00 | 0.03 | 2.02 | 1575 |
| 2024-09-20 22:21:34.816 | MS1 | 121.4656708837 | 31.1446366842 | 866 | 504990 | -87.37 | 13.83 | 84.81 | 0.12 | 2.70 | 1598 |
| 2024-09-20 22:21:35.607 | MS1 | 121.4656713524 | 31.1446371237 | 866 | 504990 | -90.88 | 12.22 | 68.19 | 0.17 | 2.67 | 1569 |
| 2024-09-20 22:21:36.144 | MS1 | 121.4656757111 | 31.1446243625 | 866 | 504990 | -87.90 | 12.30 | 84.12 | 0.04 | 2.43 | 1586 |
| 2024-09-20 22:21:37.881 | MS1 | 121.4656723961 | 31.1446341536 | 866 | 504990 | -89.94 | 11.50 | 65.99 | 0.14 | 2.55 | 1570 |
| 2024-09-20 22:21:38.550 | MS1 | 121.4656623143 | 31.1446324131 | 866 | 504990 | -91.52 | 11.58 | 93.33 | 0.19 | 2.10 | 1591 |
| 2024-09-20 22:21:39.487 | MS1 | 121.4656627444 | 31.1446272986 | 866 | 504990 | -90.79 | 7.50 | 68.89 | 0.19 | 2.84 | 1597 |
| 2024-09-20 22:21:40.245 | MS1 | 121.4656778916 | 31.1446258113 | 866 | 504990 | -90.89 | 12.37 | 457.83 | 0.11 | 2.56 | 1572 |
| 2024-09-20 22:21:41.299 | MS1 | 121.4656676265 | 31.1446346253 | 866 | 504990 | -93.52 | 12.18 | 446.91 | 0.07 | 2.99 | 1566 |
| 2024-09-20 22:21:42.369 | MS1 | 121.4656722696 | 31.1446354513 | 866 | 504990 | -92.94 | 12.34 | 375.21 | 0.17 | 2.28 | 1580 |

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
| 3255718 | 2 | 121.4756646858 | 31.1479825877 | 233 | 2 | 3 | 21.3 | TDD | 866 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3276561 | 3 | 121.4738928585 | 31.1468069523 | 11 | 2 | 6 | 18.9 | TDD | 112 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3277748 | 4 | 121.4739049639 | 31.1497353208 | 42 | 7 | 4 | 43.4 | TDD | 192 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3279394 | 1 | 121.4687065734 | 31.1519441559 | 126 | 3 | 9 | 36.2 | TDD | 512 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |

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
| 2024-09-20 22:21:31.242 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.263 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.370 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.370 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.072 | NREventA3 | measId:2;ServCellPCI:297;Se... |
| 2024-09-20 22:21:38.312 | NRHandoverAttempt | SourcePCI:297;SourceNR-ARFC... |
| 2024-09-20 22:21:38.348 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.361 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.494 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.494 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3279394 | 1 | 9.0397 | 18.2787 | -116.0008 | 13.1427 | 190.8734 | 0.0113 | 0.0178 |
| 2024_09_20 22:00 | 3255718 | 2 | 84.9940 | 88.0432 | -117.1890 | 15.9018 | 142.3386 | 0.0060 | 0.0081 |
| 2024_09_20 22:00 | 3276561 | 3 | 16.7559 | 19.4317 | -114.0521 | 5.3910 | 173.6720 | 0.0051 | 0.0189 |
| 2024_09_20 22:00 | 3277748 | 4 | 18.0010 | 14.8639 | -115.0358 | 9.2369 | 100.7038 | 0.0011 | 0.0181 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415644_0B6037DD | 504990 | 866 | -86.4 | 504990 | 512 | -89.6 | 504990 | 112 | -95.5 | 504990 | 192 |
| MR_1774415644_D568F7F6 | 504990 | 866 | -88.5 | 504990 | 512 | -88.5 | 504990 | 112 | -96.0 | 504990 | 192 |
| MR_1774415644_50628EA3 | 504990 | 866 | -87.1 | 504990 | 512 | -88.6 | 504990 | 112 | -98.3 | 504990 | 192 |
| MR_1774415644_44555E65 | 504990 | 866 | -88.8 | 504990 | 512 | -89.7 | 504990 | 112 | -95.4 | 504990 | 192 |
| MR_1774415644_A3612D3B | 504990 | 866 | -88.8 | 504990 | 512 | -89.8 | 504990 | 112 | -98.4 | 504990 | 192 |
| MR_1774415644_5A7D7167 | 504990 | 866 | -89.1 | 504990 | 512 | -91.3 | 504990 | 112 | -94.6 | 504990 | 192 |
| MR_1774415644_AF91A040 | 504990 | 866 | -88.4 | 504990 | 512 | -89.0 | 504990 | 112 | -96.9 | 504990 | 192 |
| MR_1774415644_7D81B306 | 504990 | 866 | -87.7 | 504990 | 512 | -89.9 | 504990 | 112 | -96.5 | 504990 | 192 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 208: `1055a805-991...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `1055a805-991a-4582-ad61-d47de9369dce` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[208] topology](images/test_0208.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3266882_1 and 3211777_6
- `C2`: Press down the tilt angle  of 3211777_6 by 4 degrees
- `C3`: Decrease A3 Offset threshold for 3266882_1
- `C4`: Lift the tilt angle  of 3211777_6 by 4 degrees
- `C5`: Decrease transmission power for 3211777_6
- `C6`: Add neighbor relationship between 3273031_9 and 3211777_6
- `C7`: Increase transmission power for 3211777_6
- `C8`: Adjust the azimuth of 3266882_1 by 31 degrees
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3266882_1
- `C10`: Decrease A3 Offset threshold for 3211777_6
- `C11`: Adjust the azimuth of 3211777_6 by 11 degrees
- `C12`: Increase A3 Offset threshold for 3211777_6
- `C13`: Increase A3 Offset threshold for 3266882_1
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3266882_1
- `C15`: Insufficient data; more data is needed for judgment.
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3211777_6
- `C17`: Lift the tilt angle of 3266882_1 by 2 degrees
- `C18`: Press down the tilt angle of 3266882_1 by 2 degrees
- `C19`: Decrease transmission power for 3266882_1
- `C20`: Increase transmission power for 3266882_1
- `C21`: Check test server and transmission issues
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3211777_6

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.150 | MS1 | 121.4656663282 | 31.1446277654 | 776 | 504990 | -93.61 | 11.41 | 499.64 | 0.06 | 2.84 | 1592 |
| 2024-09-20 22:21:32.155 | MS1 | 121.4656628389 | 31.1446275101 | 170 | 504990 | -94.17 | 13.38 | 456.55 | 0.06 | 2.15 | 1584 |
| 2024-09-20 22:21:33.915 | MS1 | 121.4656600567 | 31.1446218508 | 554 | 504990 | -95.22 | 12.29 | 420.13 | 0.08 | 2.18 | 1575 |
| 2024-09-20 22:21:34.278 | MS1 | 121.4656686760 | 31.1446217184 | 58 | 152650 | -94.66 | 6.06 | 57.43 | 0.12 | 1.97 | 957 |
| 2024-09-20 22:21:35.754 | MS1 | 121.4656669519 | 31.1446190102 | 832 | 152650 | -90.44 | 5.87 | 82.34 | 0.18 | 1.76 | 975 |
| 2024-09-20 22:21:36.871 | MS1 | 121.4656693511 | 31.1446290433 | 325 | 152650 | -89.33 | 5.06 | 72.12 | 0.19 | 1.61 | 944 |
| 2024-09-20 22:21:37.812 | MS1 | 121.4656749331 | 31.1446297964 | 417 | 152650 | -94.81 | 5.18 | 78.36 | 0.02 | 1.63 | 921 |
| 2024-09-20 22:21:38.824 | MS1 | 121.4656680584 | 31.1446180227 | 58 | 152650 | -92.99 | 2.72 | 105.65 | 0.02 | 1.77 | 926 |
| 2024-09-20 22:21:39.322 | MS1 | 121.4656707794 | 31.1446214638 | 832 | 152650 | -93.17 | 6.96 | 57.02 | 0.03 | 1.58 | 944 |
| 2024-09-20 22:21:40.835 | MS1 | 121.4656695785 | 31.1446357806 | 325 | 152650 | -87.56 | 3.86 | 77.60 | 0.10 | 2.85 | 1592 |
| 2024-09-20 22:21:41.851 | MS1 | 121.4656685652 | 31.1446192458 | 417 | 152650 | -92.66 | 4.75 | 60.67 | 0.04 | 2.65 | 1561 |
| 2024-09-20 22:21:42.451 | MS1 | 121.4656747731 | 31.1446303824 | 58 | 152650 | -94.88 | 6.04 | 74.50 | 0.08 | 2.57 | 1563 |

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
| 3211205 | 13 | 121.4710724288 | 31.1543323543 | 89 | 9 | 9 | 28.7 | FDD | 317 | n1 | 152650 | 30M | 4T4R | 22 | 152650 |
| 3211777 | 6 | 121.4695986090 | 31.1543742104 | 188 | 3 | 4 | 19.4 | TDD | 187 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3233486 | 5 | 121.4722361749 | 31.1518118775 | 312 | 12 | 8 | 10.6 | TDD | 751 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3233990 | 7 | 121.4704736375 | 31.1443817052 | 152 | 3 | 12 | 26.6 | FDD | 832 | n1 | 152650 | 30M | 4T4R | 17 | 152650 |
| 3236995 | 2 | 121.4669807663 | 31.1551975456 | 182 | 5 | 1 | 12.0 | TDD | 170 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3237960 | 10 | 121.4658602389 | 31.1552281845 | 142 | 3 | 3 | 20.4 | FDD | 105 | n1 | 152650 | 30M | 4T4R | 14 | 152650 |
| 3239258 | 8 | 121.4718491850 | 31.1516515839 | 77 | 6 | 12 | 4.2 | FDD | 417 | n1 | 152650 | 30M | 4T4R | 26 | 152650 |
| 3246512 | 4 | 121.4680380414 | 31.1555009232 | 266 | 12 | 12 | 1.4 | TDD | 683 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3266531 | 3 | 121.4689293345 | 31.1514603196 | 330 | 11 | 9 | 24.9 | TDD | 554 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3266882 | 1 | 121.4685790041 | 31.1459546023 | 211 | 2 | 4 | 2.4 | TDD | 776 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3270136 | 11 | 121.4754355972 | 31.1483262605 | 30 | 5 | 10 | 3.4 | FDD | 75 | n1 | 152650 | 30M | 4T4R | 20 | 152650 |
| 3273031 | 9 | 121.4694291389 | 31.1497967825 | 344 | 15 | 9 | 11.1 | FDD | 325 | n1 | 152650 | 30M | 4T4R | 28 | 152650 |
| 3277895 | 12 | 121.4675987005 | 31.1473921425 | 220 | 7 | 2 | 11.2 | FDD | 58 | n1 | 152650 | 30M | 4T4R | 23 | 152650 |

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
| 2024-09-20 22:21:30.760 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.780 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:30.928 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.928 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.617 | NREventA2 | measId:1;ServCellPCI:1003;S... |
| 2024-09-20 22:21:34.728 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:34.992 | NREventA5 | measId:3;ServCellPCI:1003;S... |
| 2024-09-20 22:21:35.063 | NRHandoverAttempt | SourcePCI:1003;SourceNR-ARF... |
| 2024-09-20 22:21:35.110 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.123 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:35.250 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.250 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3266882 | 1 | 16.6152 | 12.9136 | -116.1215 | 10.4538 | 173.9815 | 0.0065 | 0.0074 |
| 2024_09_20 22:00 | 3236995 | 2 | 6.8422 | 11.4475 | -115.0178 | 6.6552 | 167.8331 | 0.0035 | 0.0177 |
| 2024_09_20 22:00 | 3266531 | 3 | 14.9670 | 14.5085 | -114.3226 | 16.8126 | 187.0170 | 0.0188 | 0.0049 |
| 2024_09_20 22:00 | 3246512 | 4 | 15.5215 | 12.3692 | -115.8517 | 5.3286 | 179.7635 | 0.0129 | 0.0060 |
| 2024_09_20 22:00 | 3233486 | 5 | 15.2031 | 11.0973 | -114.9157 | 14.4458 | 123.6102 | 0.0135 | 0.0191 |
| 2024_09_20 22:00 | 3211777 | 6 | 11.6822 | 11.9081 | -115.4800 | 17.6058 | 194.1363 | 0.0186 | 0.0064 |
| 2024_09_20 22:00 | 3233990 | 7 | 16.7280 | 11.1898 | -114.5090 | 3.5410 | 31.7901 | 0.0082 | 0.0107 |
| 2024_09_20 22:00 | 3239258 | 8 | 19.9777 | 15.0681 | -114.2221 | 4.2954 | 58.2087 | 0.0156 | 0.0169 |
| 2024_09_20 22:00 | 3273031 | 9 | 19.7846 | 6.3793 | -117.1936 | 4.9072 | 22.7000 | 0.0097 | 0.0199 |
| 2024_09_20 22:00 | 3237960 | 10 | 16.3890 | 12.0630 | -115.7345 | 4.0240 | 28.7870 | 0.0168 | 0.0124 |
| 2024_09_20 22:00 | 3270136 | 11 | 18.6787 | 16.8852 | -117.1346 | 3.9646 | 22.2293 | 0.0200 | 0.0046 |
| 2024_09_20 22:00 | 3277895 | 12 | 9.3261 | 19.3048 | -117.4157 | 4.5060 | 29.7742 | 0.0068 | 0.0168 |
| 2024_09_20 22:00 | 3211205 | 13 | 7.1339 | 8.6309 | -117.4286 | 3.6220 | 29.3342 | 0.0115 | 0.0165 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412340_2FE3A7C1 | 504990 | 554 | -94.1 | 504990 | 187 | -91.4 | 504990 | 683 | -97.9 | 504990 | 751 |
| MR_1774412340_DF05A192 | 152650 | 58 | -93.7 | 152650 | 75 | -98.9 | 152650 | 317 | -99.1 | 152650 | 105 |
| MR_1774412340_AEC77617 | 152650 | 58 | -96.3 | 152650 | 75 | -102.1 | 152650 | 317 | -99.5 | 152650 | 105 |
| MR_1774412340_7A11A3A4 | 504990 | 554 | -94.6 | 504990 | 187 | -94.4 | 504990 | 683 | -100.2 | 504990 | 751 |
| MR_1774412340_58CF266A | 152650 | 58 | -96.1 | 152650 | 75 | -98.6 | 152650 | 317 | -102.0 | 152650 | 105 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 209: `5062639c-c70...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `5062639c-c700-478a-8ea9-6da1f2c189ad` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[209] topology](images/test_0209.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3256860_1
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3217294_3
- `C3`: Adjust the azimuth of 3217294_3 by 50 degrees
- `C4`: Add neighbor relationship between 3248435_2 and 3217294_3
- `C5`: Lift the tilt angle  of 3217294_3 by 5 degrees
- `C6`: Insufficient data; more data is needed for judgment.
- `C7`: Adjust the azimuth of 3256860_1 by 50 degrees
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3217294_3
- `C9`: Decrease A3 Offset threshold for 3217294_3
- `C10`: Decrease transmission power for 3217294_3
- `C11`: Increase transmission power for 3217294_3
- `C12`: Decrease transmission power for 3256860_1
- `C13`: Increase transmission power for 3256860_1
- `C14`: Lift the tilt angle of 3256860_1 by 10 degrees
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3256860_1
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3256860_1
- `C17`: Add neighbor relationship between 3256860_1 and 3217294_3
- `C18`: Press down the tilt angle of 3256860_1 by 10 degrees
- `C19`: Increase A3 Offset threshold for 3256860_1
- `C20`: Press down the tilt angle  of 3217294_3 by 5 degrees
- `C21`: Increase A3 Offset threshold for 3217294_3
- `C22`: Check test server and transmission issues

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.675 | MS1 | 121.4656711776 | 31.1446214097 | 255 | 504990 | -86.82 | 17.90 | 478.22 | 0.03 | 2.94 | 1587 |
| 2024-09-20 22:21:32.587 | MS1 | 121.4656612237 | 31.1446230579 | 255 | 504990 | -91.39 | 14.33 | 550.26 | 0.02 | 2.11 | 1574 |
| 2024-09-20 22:21:33.267 | MS1 | 121.4656668151 | 31.1446283688 | 255 | 504990 | -90.33 | 16.86 | 554.78 | 0.11 | 2.06 | 1575 |
| 2024-09-20 22:21:34.487 | MS1 | 121.4656713986 | 31.1446300102 | 255 | 504990 | -86.70 | 14.71 | 51.41 | 0.18 | 2.82 | 1593 |
| 2024-09-20 22:21:35.516 | MS1 | 121.4656729193 | 31.1446252813 | 255 | 504990 | -87.57 | 12.58 | 88.73 | 0.08 | 2.09 | 1571 |
| 2024-09-20 22:21:36.275 | MS1 | 121.4656736487 | 31.1446319259 | 255 | 504990 | -85.11 | 14.28 | 50.99 | 0.17 | 2.33 | 1599 |
| 2024-09-20 22:21:37.815 | MS1 | 121.4656644309 | 31.1446208418 | 255 | 504990 | -89.44 | 7.32 | 57.39 | 0.16 | 2.44 | 1584 |
| 2024-09-20 22:21:38.922 | MS1 | 121.4656775232 | 31.1446248303 | 255 | 504990 | -91.21 | 10.11 | 77.75 | 0.06 | 2.02 | 1581 |
| 2024-09-20 22:21:39.668 | MS1 | 121.4656773558 | 31.1446183048 | 255 | 504990 | -89.10 | 10.87 | 86.17 | 0.13 | 2.73 | 1597 |
| 2024-09-20 22:21:40.737 | MS1 | 121.4656745519 | 31.1446378476 | 255 | 504990 | -91.53 | 12.07 | 528.70 | 0.20 | 2.88 | 1567 |
| 2024-09-20 22:21:41.256 | MS1 | 121.4656691214 | 31.1446262901 | 255 | 504990 | -93.71 | 8.64 | 472.78 | 0.06 | 2.42 | 1583 |
| 2024-09-20 22:21:42.127 | MS1 | 121.4656634381 | 31.1446354381 | 255 | 504990 | -90.05 | 10.11 | 581.45 | 0.06 | 2.41 | 1577 |

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
| 3217294 | 3 | 121.4736113875 | 31.1445074459 | 134 | 2 | 3 | 41.6 | TDD | 46 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3219772 | 4 | 121.4686746654 | 31.1554526870 | 81 | 3 | 6 | 33.9 | TDD | 243 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3248435 | 2 | 121.4673972415 | 31.1449068109 | 45 | 4 | 7 | 25.8 | TDD | 899 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3256860 | 1 | 121.4759946414 | 31.1515251722 | 333 | 11 | 3 | 29.8 | TDD | 255 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |

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
| 2024-09-20 22:21:31.080 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.104 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.234 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.234 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.966 | NREventA3 | measId:2;ServCellPCI:783;Se... |
| 2024-09-20 22:21:38.206 | NRHandoverAttempt | SourcePCI:783;SourceNR-ARFC... |
| 2024-09-20 22:21:38.244 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.254 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.380 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.380 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3256860 | 1 | 80.5143 | 92.8737 | -117.8937 | 12.8591 | 185.2103 | 0.0179 | 0.0146 |
| 2024_09_19 22:00 | 3248435 | 2 | 87.0053 | 87.2420 | -114.0048 | 7.6143 | 155.7238 | 0.0060 | 0.0197 |
| 2024_09_19 22:00 | 3217294 | 3 | 88.1395 | 90.1755 | -116.7484 | 14.4789 | 179.4025 | 0.0180 | 0.0080 |
| 2024_09_19 22:00 | 3219772 | 4 | 92.6868 | 86.0703 | -117.6182 | 19.0913 | 118.5560 | 0.0015 | 0.0091 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416914_7C35EFEC | 504990 | 255 | -87.0 | 504990 | 46 | -87.3 | 504990 | 899 | -100.7 | 504990 | 243 |
| MR_1774416914_6CC9ED6E | 504990 | 255 | -84.7 | 504990 | 46 | -85.7 | 504990 | 899 | -100.2 | 504990 | 243 |
| MR_1774416914_39097443 | 504990 | 255 | -86.1 | 504990 | 46 | -86.3 | 504990 | 899 | -100.5 | 504990 | 243 |
| MR_1774416914_D5960BCA | 504990 | 255 | -88.7 | 504990 | 46 | -89.1 | 504990 | 899 | -97.9 | 504990 | 243 |
| MR_1774416914_A734C0AD | 504990 | 255 | -86.4 | 504990 | 46 | -88.8 | 504990 | 899 | -99.5 | 504990 | 243 |
| MR_1774416914_7F879ACC | 504990 | 255 | -87.1 | 504990 | 46 | -86.2 | 504990 | 899 | -99.4 | 504990 | 243 |
| MR_1774416914_0EADD65E | 504990 | 255 | -87.0 | 504990 | 46 | -87.5 | 504990 | 899 | -100.1 | 504990 | 243 |

> *... 2개 열 생략 (전체 14열)*

---
