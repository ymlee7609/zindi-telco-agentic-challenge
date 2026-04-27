# Track A 문제 분석 — train[30]~train[39]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[30] ~ train[39] (10개)

## 목차

1. [문제 30: `0e6973b6-094...`](#30) — single-answer, 정답: C19
2. [문제 31: `6fc2c635-2c2...`](#31) — multiple-answer, 정답: C4|C11|C12|C20
3. [문제 32: `e39f26f7-37c...`](#32) — single-answer, 정답: C2
4. [문제 33: `6f044631-678...`](#33) — multiple-answer, 정답: C2|C3
5. [문제 34: `4d61d1a4-bae...`](#34) — single-answer, 정답: C5
6. [문제 35: `c3760904-0d8...`](#35) — single-answer, 정답: C17
7. [문제 36: `4fb7da43-d26...`](#36) — single-answer, 정답: C17
8. [문제 37: `1caef10f-900...`](#37) — multiple-answer, 정답: C5|C15
9. [문제 38: `7b6d8a8a-201...`](#38) — single-answer, 정답: C13
10. [문제 39: `cd460e77-232...`](#39) — single-answer, 정답: C22

---

### 문제 30: `0e6973b6-094...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `0e6973b6-0948-4d0b-85ef-cb8ff7675c44` |
| Tag | **single-answer** |
| 정답 | **C19** |
| C19 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[30] topology](images/train_0030.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3219251_4 by 10 degrees
- `C2`: Increase transmission power for 3219251_4
- `C3`: Add neighbor relationship between 3255098_1 and 3219251_4
- `C4`: Check test server and transmission issues
- `C5`: Increase A3 Offset threshold for 3235267_3
- `C6`: Lift the tilt angle  of 3219251_4 by 10 degrees
- `C7`: Lift the tilt angle of 3235267_3 by 10 degrees
- `C8`: Decrease transmission power for 3219251_4
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3235267_3
- `C10`: Increase A3 Offset threshold for 3219251_4
- `C11`: Adjust the azimuth of 3235267_3 by 50 degrees
- `C12`: Press down the tilt angle of 3235267_3 by 10 degrees
- `C13`: Decrease A3 Offset threshold for 3235267_3
- `C14`: Increase transmission power for 3235267_3
- `C15`: Adjust the azimuth of 3219251_4 by 50 degrees
- `C16`: Decrease A3 Offset threshold for 3219251_4
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3235267_3
- `C18`: Add neighbor relationship between 3235267_3 and 3219251_4
- `C19`: Insufficient data; more data is needed for judgment. **← 정답**
- `C20`: Decrease transmission power for 3235267_3
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3219251_4
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3219251_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.487 | MS1 | 121.4656691287 | 31.1446307199 | 836 | 504990 | -89.49 | 15.27 | 503.93 | 0.09 | 2.26 | 1594 |
| 2024-09-20 22:21:32.140 | MS1 | 121.4656626562 | 31.1446279924 | 836 | 504990 | -91.79 | 15.57 | 476.46 | 0.12 | 2.39 | 1600 |
| 2024-09-20 22:21:33.386 | MS1 | 121.4656616182 | 31.1446304607 | 836 | 504990 | -86.50 | 13.82 | 431.45 | 0.17 | 2.11 | 1593 |
| 2024-09-20 22:21:34.229 | MS1 | 121.4656761209 | 31.1446258176 | 836 | 504990 | -90.60 | 13.03 | 84.68 | 0.04 | 2.96 | 1584 |
| 2024-09-20 22:21:35.572 | MS1 | 121.4656724400 | 31.1446186667 | 836 | 504990 | -91.79 | 14.13 | 70.91 | 0.11 | 2.32 | 1574 |
| 2024-09-20 22:21:36.260 | MS1 | 121.4656717223 | 31.1446217912 | 836 | 504990 | -86.60 | 17.33 | 52.65 | 0.05 | 2.94 | 1584 |
| 2024-09-20 22:21:37.546 | MS1 | 121.4656737604 | 31.1446226789 | 836 | 504990 | -93.12 | 10.92 | 61.03 | 0.03 | 2.35 | 1569 |
| 2024-09-20 22:21:38.640 | MS1 | 121.4656779668 | 31.1446248846 | 836 | 504990 | -91.06 | 12.38 | 85.28 | 0.18 | 2.81 | 1584 |
| 2024-09-20 22:21:39.978 | MS1 | 121.4656649653 | 31.1446309230 | 836 | 504990 | -90.54 | 8.62 | 58.95 | 0.18 | 3.00 | 1599 |
| 2024-09-20 22:21:40.828 | MS1 | 121.4656675682 | 31.1446233598 | 836 | 504990 | -92.45 | 11.84 | 576.11 | 0.11 | 2.37 | 1567 |
| 2024-09-20 22:21:41.725 | MS1 | 121.4656585742 | 31.1446362046 | 836 | 504990 | -90.44 | 11.07 | 403.01 | 0.14 | 2.14 | 1594 |
| 2024-09-20 22:21:42.932 | MS1 | 121.4656697055 | 31.1446348372 | 836 | 504990 | -90.73 | 8.47 | 445.58 | 0.02 | 2.66 | 1597 |

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
| 3219251 | 4 | 121.4663093883 | 31.1555205477 | 118 | 11 | 7 | 40.5 | TDD | 1006 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3229245 | 2 | 121.4656627512 | 31.1487851383 | 142 | 2 | 1 | 20.2 | TDD | 738 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3235267 | 3 | 121.4653369675 | 31.1477946866 | 324 | 10 | 0 | 24.5 | TDD | 836 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3255098 | 1 | 121.4749133743 | 31.1449075670 | 246 | 2 | 7 | 21.1 | TDD | 449 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

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
| 2024-09-20 22:21:31.255 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.280 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.430 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.430 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.105 | NREventA3 | measId:2;ServCellPCI:995;Se... |
| 2024-09-20 22:21:38.345 | NRHandoverAttempt | SourcePCI:995;SourceNR-ARFC... |
| 2024-09-20 22:21:38.386 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.399 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.549 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.549 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3255098 | 1 | 91.6977 | 75.4406 | -115.8220 | 10.3365 | 175.6754 | 0.0056 | 0.0041 |
| 2024_09_19 22:00 | 3229245 | 2 | 80.7651 | 94.3692 | -117.8100 | 5.4159 | 127.8271 | 0.0186 | 0.0034 |
| 2024_09_19 22:00 | 3235267 | 3 | 80.3664 | 87.4454 | -115.7331 | 19.2810 | 188.6353 | 0.0064 | 0.0079 |
| 2024_09_19 22:00 | 3219251 | 4 | 80.2752 | 80.4917 | -114.4807 | 6.2598 | 187.0443 | 0.0064 | 0.0069 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416597_D0C2D018 | 504990 | 836 | -90.5 | 504990 | 1006 | -97.9 | 504990 | 449 | -100.3 | 504990 | 738 |
| MR_1774416597_82F270A6 | 504990 | 836 | -91.2 | 504990 | 1006 | -98.8 | 504990 | 449 | -101.2 | 504990 | 738 |
| MR_1774416597_1CE6B9EE | 504990 | 836 | -89.7 | 504990 | 1006 | -97.1 | 504990 | 449 | -99.3 | 504990 | 738 |
| MR_1774416597_2169D803 | 504990 | 836 | -90.9 | 504990 | 1006 | -99.1 | 504990 | 449 | -100.3 | 504990 | 738 |
| MR_1774416597_E8CCF6F3 | 504990 | 836 | -89.1 | 504990 | 1006 | -97.0 | 504990 | 449 | -100.1 | 504990 | 738 |
| MR_1774416597_76E38155 | 504990 | 836 | -89.5 | 504990 | 1006 | -98.2 | 504990 | 449 | -102.3 | 504990 | 738 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 31: `6fc2c635-2c2...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `6fc2c635-2c2a-4f1c-9ce0-db0d4c53b46a` |
| Tag | **multiple-answer** |
| 정답 | **C4|C11|C12|C20** |
| C4 의미 | Decrease transmission power for 3214884_2 |
| C11 의미 | Increase A3 Offset threshold for 3215272_1 |
| C12 의미 | Press down the tilt angle  of 3214884_2 by 6 degrees |
| C20 의미 | Increase A3 Offset threshold for 3214884_2 |
| 패턴 분류 | **P3 Overshoot (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[31] topology](images/train_0031.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 5 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 5개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3215272_1 by 2 degrees
- `C2`: Insufficient data; more data is needed for judgment.
- `C3`: Adjust the azimuth of 3214884_2 by 4 degrees
- `C4`: Decrease transmission power for 3214884_2 **← 정답**
- `C5`: Decrease A3 Offset threshold for 3214884_2
- `C6`: Check test server and transmission issues
- `C7`: Increase transmission power for 3215272_1
- `C8`: Add neighbor relationship between 3215272_1 and 3214884_2
- `C9`: Press down the tilt angle of 3215272_1 by 2 degrees
- `C10`: Increase transmission power for 3214884_2
- `C11`: Increase A3 Offset threshold for 3215272_1 **← 정답**
- `C12`: Press down the tilt angle  of 3214884_2 by 6 degrees **← 정답**
- `C13`: Decrease A3 Offset threshold for 3215272_1
- `C14`: Lift the tilt angle  of 3214884_2 by 6 degrees
- `C15`: Add neighbor relationship between 3258849_5 and 3214884_2
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3214884_2
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3214884_2
- `C18`: Adjust the azimuth of 3215272_1 by 25 degrees
- `C19`: Decrease transmission power for 3215272_1
- `C20`: Increase A3 Offset threshold for 3214884_2 **← 정답**
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3215272_1
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3215272_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.916 | MS1 | 121.4656636351 | 31.1446323737 | 417 | 504990 | -84.09 | 15.28 | 604.41 | 0.04 | 2.27 | 1582 |
| 2024-09-20 22:21:32.242 | MS1 | 121.4656644142 | 31.1446228953 | 417 | 504990 | -79.71 | 14.36 | 434.85 | 0.05 | 2.98 | 1599 |
| 2024-09-20 22:21:33.220 | MS1 | 121.4656602910 | 31.1446226654 | 417 | 504990 | -77.93 | 13.86 | 439.77 | 0.11 | 2.74 | 1561 |
| 2024-09-20 22:21:34.766 | MS1 | 121.4656661243 | 31.1446261800 | 921 | 504990 | -87.37 | 3.67 | 44.20 | 0.11 | 1.16 | 1596 |
| 2024-09-20 22:21:35.717 | MS1 | 121.4656638821 | 31.1446375017 | 921 | 504990 | -89.54 | 2.58 | 51.09 | 0.19 | 1.44 | 1600 |
| 2024-09-20 22:21:36.217 | MS1 | 121.4656765499 | 31.1446244251 | 417 | 504990 | -85.04 | 2.37 | 25.41 | 0.18 | 1.47 | 1600 |
| 2024-09-20 22:21:37.690 | MS1 | 121.4656739358 | 31.1446316031 | 417 | 504990 | -87.62 | 3.69 | 72.06 | 0.11 | 1.16 | 1569 |
| 2024-09-20 22:21:38.582 | MS1 | 121.4656614629 | 31.1446365852 | 921 | 504990 | -88.55 | 1.77 | 36.56 | 0.01 | 1.36 | 1561 |
| 2024-09-20 22:21:39.838 | MS1 | 121.4656743407 | 31.1446239988 | 921 | 504990 | -88.17 | 3.89 | 44.80 | 0.19 | 1.34 | 1588 |
| 2024-09-20 22:21:40.188 | MS1 | 121.4656680141 | 31.1446282863 | 921 | 504990 | -77.41 | 15.37 | 520.19 | 0.07 | 2.83 | 1585 |
| 2024-09-20 22:21:41.347 | MS1 | 121.4656644419 | 31.1446329767 | 921 | 504990 | -84.09 | 12.99 | 354.25 | 0.19 | 2.70 | 1573 |
| 2024-09-20 22:21:42.585 | MS1 | 121.4656587647 | 31.1446377563 | 921 | 504990 | -82.90 | 15.61 | 377.69 | 0.01 | 2.54 | 1571 |

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
| 3214884 | 2 | 121.4705522096 | 31.1481967507 | 233 | 1 | 3 | 49.4 | TDD | 282 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3214990 | 3 | 121.4663806571 | 31.1517024531 | 163 | 7 | 2 | 42.5 | TDD | 599 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3215272 | 1 | 121.4694774648 | 31.1505330132 | 234 | 0 | 11 | 25.7 | TDD | 417 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3229523 | 4 | 121.4722019471 | 31.1455327319 | 106 | 2 | 3 | 34.2 | TDD | 921 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3258849 | 5 | 121.4646901199 | 31.1474925924 | 350 | 9 | 6 | 34.9 | TDD | 186 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:31.310 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.326 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.436 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.436 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.179 | NREventA3 | measId:2;ServCellPCI:630;Se... |
| 2024-09-20 22:21:34.419 | NRHandoverAttempt | SourcePCI:630;SourceNR-ARFC... |
| 2024-09-20 22:21:34.455 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:34.466 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:34.598 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:34.598 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:36.179 | NREventA3 | measId:2;ServCellPCI:994;Se... |
| 2024-09-20 22:21:36.419 | NRHandoverAttempt | SourcePCI:994;SourceNR-ARFC... |
| 2024-09-20 22:21:36.467 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:36.479 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:36.587 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.587 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.179 | NREventA3 | measId:2;ServCellPCI:630;Se... |
| 2024-09-20 22:21:38.419 | NRHandoverAttempt | SourcePCI:630;SourceNR-ARFC... |
| 2024-09-20 22:21:38.453 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.465 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.614 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.614 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3215272 | 1 | 6.4942 | 11.5331 | -115.9200 | 8.2706 | 105.8407 | 0.0181 | 0.0163 |
| 2024_09_20 22:00 | 3214884 | 2 | 5.6925 | 17.1183 | -116.9873 | 6.7498 | 132.6529 | 0.0102 | 0.0196 |
| 2024_09_20 22:00 | 3214990 | 3 | 6.3413 | 16.1644 | -114.3149 | 19.9586 | 99.8857 | 0.0100 | 0.0158 |
| 2024_09_20 22:00 | 3229523 | 4 | 6.3423 | 5.6054 | -116.4583 | 13.5699 | 90.5833 | 0.0039 | 0.0062 |
| 2024_09_20 22:00 | 3258849 | 5 | 18.3307 | 10.7101 | -116.3787 | 8.5701 | 187.8144 | 0.0158 | 0.0073 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412933_2D85FEC8 | 504990 | 417 | -86.1 | 504990 | 921 | -81.9 | 504990 | 282 | -87.8 | 504990 | 186 |
| MR_1774412933_535D77F0 | 504990 | 417 | -87.6 | 504990 | 921 | -85.4 | 504990 | 282 | -89.2 | 504990 | 186 |
| MR_1774412933_C400CE19 | 504990 | 921 | -87.1 | 504990 | 417 | -82.8 | 504990 | 282 | -88.3 | 504990 | 186 |
| MR_1774412933_DC60030E | 504990 | 921 | -89.3 | 504990 | 417 | -85.4 | 504990 | 282 | -85.5 | 504990 | 186 |
| MR_1774412933_C0B90353 | 504990 | 417 | -85.6 | 504990 | 921 | -82.7 | 504990 | 282 | -85.5 | 504990 | 186 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 32: `e39f26f7-37c...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `e39f26f7-37ca-4ddf-8d2b-1bc453479f07` |
| Tag | **single-answer** |
| 정답 | **C2** |
| C2 의미 | Add neighbor relationship between 3249994_2 and 3223536_1 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[32] topology](images/train_0032.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3249994_2
- `C2`: Add neighbor relationship between 3249994_2 and 3223536_1 **← 정답**
- `C3`: Lift the tilt angle of 3249994_2 by 10 degrees
- `C4`: Check test server and transmission issues
- `C5`: Increase transmission power for 3223536_1
- `C6`: Adjust the azimuth of 3223536_1 by 29 degrees
- `C7`: Decrease transmission power for 3223536_1
- `C8`: Decrease A3 Offset threshold for 3223536_1
- `C9`: Increase A3 Offset threshold for 3249994_2
- `C10`: Decrease A3 Offset threshold for 3249994_2
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3223536_1
- `C12`: Adjust the azimuth of 3249994_2 by 50 degrees
- `C13`: Press down the tilt angle  of 3223536_1 by 6 degrees
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3223536_1
- `C15`: Decrease transmission power for 3249994_2
- `C16`: Add neighbor relationship between 3224780_4 and 3223536_1
- `C17`: Increase A3 Offset threshold for 3223536_1
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3249994_2
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3249994_2
- `C20`: Press down the tilt angle of 3249994_2 by 10 degrees
- `C21`: Lift the tilt angle  of 3223536_1 by 6 degrees
- `C22`: Insufficient data; more data is needed for judgment.

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.799 | MS1 | 121.4656674875 | 31.1446299406 | 479 | 504990 | -79.82 | 17.11 | 309.71 | 0.11 | 2.05 | 1595 |
| 2024-09-20 22:21:32.640 | MS1 | 121.4656747308 | 31.1446347061 | 479 | 504990 | -79.19 | 13.01 | 409.77 | 0.04 | 2.88 | 1597 |
| 2024-09-20 22:21:33.786 | MS1 | 121.4656678546 | 31.1446234342 | 479 | 504990 | -81.50 | 15.76 | 348.97 | 0.02 | 2.18 | 1564 |
| 2024-09-20 22:21:34.170 | MS1 | 121.4656655198 | 31.1446308847 | 479 | 504990 | -90.90 | -0.45 | 59.13 | 0.20 | 1.42 | 1565 |
| 2024-09-20 22:21:35.636 | MS1 | 121.4656759729 | 31.1446340921 | 479 | 504990 | -88.97 | -2.77 | 53.54 | 0.03 | 1.23 | 1598 |
| 2024-09-20 22:21:36.910 | MS1 | 121.4656701386 | 31.1446378900 | 479 | 504990 | -91.25 | -0.12 | 45.62 | 0.06 | 1.03 | 1577 |
| 2024-09-20 22:21:37.246 | MS1 | 121.4656632890 | 31.1446304752 | 479 | 504990 | -85.95 | -2.62 | 43.73 | 0.18 | 1.09 | 1564 |
| 2024-09-20 22:21:38.274 | MS1 | 121.4656638692 | 31.1446344704 | 479 | 504990 | -77.17 | 16.19 | 333.52 | 0.17 | 1.45 | 1583 |
| 2024-09-20 22:21:39.369 | MS1 | 121.4656628309 | 31.1446332113 | 479 | 504990 | -84.66 | 12.23 | 319.74 | 0.19 | 1.19 | 1597 |
| 2024-09-20 22:21:40.463 | MS1 | 121.4656664870 | 31.1446251659 | 479 | 504990 | -79.41 | 13.62 | 549.59 | 0.19 | 2.88 | 1575 |
| 2024-09-20 22:21:41.305 | MS1 | 121.4656617894 | 31.1446189536 | 479 | 504990 | -82.94 | 13.38 | 298.83 | 0.05 | 2.81 | 1596 |
| 2024-09-20 22:21:42.833 | MS1 | 121.4656765377 | 31.1446308627 | 479 | 504990 | -82.70 | 12.71 | 314.01 | 0.14 | 2.40 | 1561 |

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
| 3223536 | 1 | 121.4692951662 | 31.1475997406 | 255 | 3 | 7 | 24.4 | TDD | 49 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3224780 | 4 | 121.4679826706 | 31.1440754308 | 134 | 5 | 8 | 47.9 | TDD | 817 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3227224 | 3 | 121.4743117431 | 31.1493713521 | 224 | 14 | 10 | 41.6 | TDD | 559 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3249994 | 2 | 121.4685132114 | 31.1516195220 | 120 | 15 | 9 | 44.0 | TDD | 479 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |

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
| 2024-09-20 22:21:31.496 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.517 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.634 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.634 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.307 | NREventA3 | measId:2;ServCellPCI:348;Se... |
| 2024-09-20 22:21:36.307 | NREventA3 | measId:2;ServCellPCI:348;Se... |
| 2024-09-20 22:21:37.307 | NREventA3 | measId:2;ServCellPCI:348;Se... |
| 2024-09-20 22:21:39.807 | NRRRCReestablishAttempt | PCI:348 |
| 2024-09-20 22:21:39.821 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.831 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:39.957 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.957 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3223536 | 1 | 6.4286 | 13.2027 | -116.6693 | 6.1052 | 106.7413 | 0.0113 | 0.0103 |
| 2024_09_20 22:00 | 3249994 | 2 | 9.3848 | 6.8557 | -115.6311 | 7.9455 | 136.4605 | 0.0114 | 0.1176 |
| 2024_09_20 22:00 | 3227224 | 3 | 17.4110 | 11.4507 | -116.6447 | 9.3169 | 140.7581 | 0.0169 | 0.0069 |
| 2024_09_20 22:00 | 3224780 | 4 | 8.1346 | 15.1147 | -117.0649 | 12.1748 | 116.1162 | 0.0050 | 0.0022 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416878_4D76BF09 | 504990 | 479 | -92.2 | 504990 | 49 | -85.9 | 504990 | 817 | -93.2 | 504990 | 559 |
| MR_1774416878_8F87AAD9 | 504990 | 479 | -90.0 | 504990 | 49 | -84.4 | 504990 | 817 | -90.4 | 504990 | 559 |
| MR_1774416878_C04C1869 | 504990 | 479 | -90.8 | 504990 | 49 | -86.8 | 504990 | 817 | -92.6 | 504990 | 559 |
| MR_1774416878_F1F85201 | 504990 | 49 | -87.4 | 504990 | 479 | -90.6 | 504990 | 817 | -93.3 | 504990 | 559 |
| MR_1774416878_91108AE1 | 504990 | 479 | -90.5 | 504990 | 49 | -87.3 | 504990 | 817 | -92.7 | 504990 | 559 |
| MR_1774416878_51FC6D71 | 504990 | 479 | -91.4 | 504990 | 49 | -87.3 | 504990 | 817 | -93.1 | 504990 | 559 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 33: `6f044631-678...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `6f044631-678d-4fb1-836a-27211bda5e0e` |
| Tag | **multiple-answer** |
| 정답 | **C2|C3** |
| C2 의미 | Increase transmission power for 3242895_1 |
| C3 의미 | Adjust the azimuth of 3242895_1 by 50 degrees |
| 패턴 분류 | **P4 Coverage (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[33] topology](images/train_0033.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3242895_1
- `C2`: Increase transmission power for 3242895_1 **← 정답**
- `C3`: Adjust the azimuth of 3242895_1 by 50 degrees **← 정답**
- `C4`: Adjust the azimuth of 3270873_2 by 47 degrees
- `C5`: Check test server and transmission issues
- `C6`: Lift the tilt angle of 3242895_1 by 3 degrees
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3270873_2
- `C8`: Increase A3 Offset threshold for 3242895_1
- `C9`: Press down the tilt angle  of 3270873_2 by 5 degrees
- `C10`: Decrease A3 Offset threshold for 3270873_2
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3242895_1
- `C12`: Increase transmission power for 3270873_2
- `C13`: Add neighbor relationship between 3242895_1 and 3270873_2
- `C14`: Add neighbor relationship between 3252781_4 and 3270873_2
- `C15`: Insufficient data; more data is needed for judgment.
- `C16`: Lift the tilt angle  of 3270873_2 by 5 degrees
- `C17`: Decrease transmission power for 3270873_2
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3270873_2
- `C19`: Press down the tilt angle of 3242895_1 by 3 degrees
- `C20`: Increase A3 Offset threshold for 3270873_2
- `C21`: Decrease transmission power for 3242895_1
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3242895_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.764 | MS1 | 121.4656749022 | 31.1446351613 | 64 | 504990 | -88.51 | 16.57 | 363.84 | 0.00 | 2.73 | 1589 |
| 2024-09-20 22:21:32.892 | MS1 | 121.4656667915 | 31.1446311344 | 64 | 504990 | -92.84 | 14.60 | 558.91 | 0.12 | 2.00 | 1569 |
| 2024-09-20 22:21:33.348 | MS1 | 121.4656599932 | 31.1446328410 | 64 | 504990 | -94.07 | 14.05 | 531.18 | 0.20 | 2.52 | 1582 |
| 2024-09-20 22:21:34.879 | MS1 | 121.4656585588 | 31.1446256718 | 64 | 504990 | -107.67 | -0.34 | 72.09 | 0.11 | 1.40 | 1582 |
| 2024-09-20 22:21:35.271 | MS1 | 121.4656712146 | 31.1446336012 | 64 | 504990 | -100.88 | 1.87 | 57.07 | 0.12 | 1.22 | 1579 |
| 2024-09-20 22:21:36.839 | MS1 | 121.4656651979 | 31.1446215318 | 64 | 504990 | -103.69 | -1.24 | 49.22 | 0.09 | 1.02 | 1593 |
| 2024-09-20 22:21:37.274 | MS1 | 121.4656600048 | 31.1446236297 | 64 | 504990 | -109.64 | 0.37 | 39.35 | 0.10 | 1.31 | 1575 |
| 2024-09-20 22:21:38.162 | MS1 | 121.4656766088 | 31.1446363502 | 64 | 504990 | -102.86 | 1.86 | 76.09 | 0.05 | 1.49 | 1580 |
| 2024-09-20 22:21:39.341 | MS1 | 121.4656610375 | 31.1446335285 | 64 | 504990 | -104.89 | -1.96 | 24.84 | 0.01 | 1.36 | 1581 |
| 2024-09-20 22:21:40.447 | MS1 | 121.4656652487 | 31.1446253686 | 64 | 504990 | -87.04 | 16.06 | 382.87 | 0.15 | 2.96 | 1582 |
| 2024-09-20 22:21:41.514 | MS1 | 121.4656620468 | 31.1446291641 | 64 | 504990 | -94.29 | 14.04 | 400.16 | 0.16 | 2.71 | 1583 |
| 2024-09-20 22:21:42.330 | MS1 | 121.4656769100 | 31.1446185905 | 64 | 504990 | -93.10 | 17.87 | 342.86 | 0.15 | 2.07 | 1599 |

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
| 3223288 | 3 | 121.4656235695 | 31.1499000667 | 98 | 10 | 1 | 40.2 | TDD | 749 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3242895 | 1 | 121.4688039446 | 31.1495942068 | 147 | 2 | 7 | 15.9 | TDD | 64 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3252781 | 4 | 121.4682843291 | 31.1531570633 | 275 | 4 | 0 | 36.4 | TDD | 630 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3270873 | 2 | 121.4744149479 | 31.1480902933 | 292 | 3 | 1 | 29.0 | TDD | 784 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

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
| 2024-09-20 22:21:30.840 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:30.987 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.987 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.190 | NREventA2 | measId:1;ServCellPCI:385;Se... |
| 2024-09-20 22:21:34.340 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3242895 | 1 | 18.3515 | 19.1575 | -117.4693 | 14.3208 | 161.8804 | 0.1878 | 0.0142 |
| 2024_09_20 22:00 | 3270873 | 2 | 12.7403 | 5.5139 | -116.9159 | 19.3945 | 125.8481 | 0.0041 | 0.0023 |
| 2024_09_20 22:00 | 3223288 | 3 | 6.4976 | 16.3760 | -114.5057 | 8.9601 | 128.4853 | 0.0130 | 0.0026 |
| 2024_09_20 22:00 | 3252781 | 4 | 12.5551 | 13.1450 | -116.8066 | 10.8543 | 160.1584 | 0.0197 | 0.0086 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415223_5CE7E75A | 504990 | 64 | -109.2 | 504990 | 784 | -111.8 | 504990 | 630 | -117.6 | 504990 | 749 |
| MR_1774415223_BEF241C3 | 504990 | 64 | -109.4 | 504990 | 784 | -113.3 | 504990 | 630 | -119.3 | 504990 | 749 |
| MR_1774415223_BB3E7FDE | 504990 | 64 | -109.6 | 504990 | 784 | -113.6 | 504990 | 630 | -119.5 | 504990 | 749 |
| MR_1774415223_9728824E | 504990 | 64 | -109.7 | 504990 | 784 | -114.0 | 504990 | 630 | -117.3 | 504990 | 749 |
| MR_1774415223_72B630A7 | 504990 | 64 | -109.4 | 504990 | 784 | -113.6 | 504990 | 630 | -118.7 | 504990 | 749 |
| MR_1774415223_29C82D60 | 504990 | 64 | -105.7 | 504990 | 784 | -113.2 | 504990 | 630 | -119.7 | 504990 | 749 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 34: `4d61d1a4-bae...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `4d61d1a4-bae5-4d86-9b3b-4b6f0107ee9a` |
| Tag | **single-answer** |
| 정답 | **C5** |
| C5 의미 | Lift the tilt angle  of 3240072_2 by 7 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[34] topology](images/train_0034.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Check test server and transmission issues
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3221963_1
- `C3`: Decrease A3 Offset threshold for 3221963_1
- `C4`: Increase transmission power for 3221963_1
- `C5`: Lift the tilt angle  of 3240072_2 by 7 degrees **← 정답**
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3276322_4
- `C7`: Add neighbor relationship between 3240072_2 and 3276322_4
- `C8`: Decrease transmission power for 3221963_1
- `C9`: Press down the tilt angle of 3221963_1 by 3 degrees
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3276322_4
- `C11`: Adjust the azimuth of 3221963_1 by 30 degrees
- `C12`: Increase A3 Offset threshold for 3221963_1
- `C13`: Decrease A3 Offset threshold for 3276322_4
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3221963_1
- `C15`: Adjust the azimuth of 3240072_2 by 50 degrees
- `C16`: Increase A3 Offset threshold for 3276322_4
- `C17`: Insufficient data; more data is needed for judgment.
- `C18`: Add neighbor relationship between 3221963_1 and 3276322_4
- `C19`: Increase transmission power for 3276322_4
- `C20`: Decrease transmission power for 3276322_4
- `C21`: Press down the tilt angle  of 3240072_2 by 7 degrees
- `C22`: Lift the tilt angle of 3221963_1 by 3 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.969 | MS1 | 121.4656689105 | 31.1446370794 | 816 | 504990 | -87.50 | 16.72 | 322.77 | 0.12 | 2.11 | 1567 |
| 2024-09-20 22:21:32.847 | MS1 | 121.4656596292 | 31.1446330793 | 816 | 504990 | -88.57 | 12.03 | 313.53 | 0.09 | 2.13 | 1595 |
| 2024-09-20 22:21:33.389 | MS1 | 121.4656612066 | 31.1446296960 | 816 | 504990 | -89.69 | 17.57 | 300.22 | 0.14 | 2.92 | 1580 |
| 2024-09-20 22:21:34.560 | MS1 | 121.4656686894 | 31.1446241722 | 816 | 504990 | -91.78 | 15.88 | 59.18 | 0.01 | 2.88 | 1574 |
| 2024-09-20 22:21:35.516 | MS1 | 121.4656595993 | 31.1446303178 | 816 | 504990 | -87.46 | 17.21 | 66.18 | 0.03 | 2.94 | 1594 |
| 2024-09-20 22:21:36.937 | MS1 | 121.4656591530 | 31.1446365714 | 816 | 504990 | -87.97 | 12.40 | 68.73 | 0.08 | 2.29 | 1577 |
| 2024-09-20 22:21:37.268 | MS1 | 121.4656721227 | 31.1446195462 | 816 | 504990 | -90.50 | 8.65 | 91.20 | 0.15 | 2.18 | 1588 |
| 2024-09-20 22:21:38.422 | MS1 | 121.4656698769 | 31.1446329077 | 816 | 504990 | -91.80 | 9.51 | 79.73 | 0.18 | 2.93 | 1563 |
| 2024-09-20 22:21:39.588 | MS1 | 121.4656711823 | 31.1446256501 | 816 | 504990 | -93.98 | 11.33 | 86.37 | 0.13 | 3.00 | 1568 |
| 2024-09-20 22:21:40.855 | MS1 | 121.4656762277 | 31.1446252151 | 816 | 504990 | -92.20 | 12.62 | 502.07 | 0.16 | 2.07 | 1562 |
| 2024-09-20 22:21:41.994 | MS1 | 121.4656745776 | 31.1446358616 | 816 | 504990 | -91.79 | 7.67 | 567.76 | 0.08 | 2.55 | 1597 |
| 2024-09-20 22:21:42.763 | MS1 | 121.4656703430 | 31.1446354077 | 816 | 504990 | -90.93 | 7.36 | 435.10 | 0.13 | 2.25 | 1569 |

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
| 3221963 | 1 | 121.4669981398 | 31.1547096120 | 156 | 1 | 6 | 44.2 | TDD | 816 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3240072 | 2 | 121.4650175588 | 31.1500026034 | 24 | 1 | 4 | 32.1 | TDD | 105 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3256654 | 3 | 121.4704998322 | 31.1504413642 | 187 | 6 | 1 | 17.4 | TDD | 425 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3276322 | 4 | 121.4701560064 | 31.1533210872 | 294 | 5 | 4 | 37.9 | TDD | 15 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |

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
| 2024-09-20 22:21:31.456 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.475 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.598 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.598 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.350 | NREventA3 | measId:2;ServCellPCI:709;Se... |
| 2024-09-20 22:21:38.590 | NRHandoverAttempt | SourcePCI:709;SourceNR-ARFC... |
| 2024-09-20 22:21:38.627 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.637 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.742 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.742 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3221963 | 1 | 84.1181 | 88.1442 | -114.2708 | 6.6718 | 134.1640 | 0.0181 | 0.0146 |
| 2024_09_20 22:00 | 3240072 | 2 | 8.0974 | 14.2364 | -116.4130 | 7.8801 | 126.8854 | 0.0197 | 0.0044 |
| 2024_09_20 22:00 | 3256654 | 3 | 6.1655 | 8.9837 | -115.1378 | 19.2548 | 86.7070 | 0.0166 | 0.0104 |
| 2024_09_20 22:00 | 3276322 | 4 | 7.8321 | 12.9418 | -114.6256 | 13.8086 | 197.0376 | 0.0098 | 0.0149 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412866_83F9CD1A | 504990 | 816 | -91.8 | 504990 | 15 | -92.4 | 504990 | 105 | -108.1 | 504990 | 425 |
| MR_1774412866_EDB71017 | 504990 | 816 | -93.6 | 504990 | 15 | -93.9 | 504990 | 105 | -106.5 | 504990 | 425 |
| MR_1774412866_6F0CBC95 | 504990 | 816 | -93.2 | 504990 | 15 | -91.7 | 504990 | 105 | -105.2 | 504990 | 425 |
| MR_1774412866_17654E76 | 504990 | 816 | -91.5 | 504990 | 15 | -93.0 | 504990 | 105 | -106.8 | 504990 | 425 |
| MR_1774412866_3D8A30B3 | 504990 | 816 | -90.0 | 504990 | 15 | -92.2 | 504990 | 105 | -105.8 | 504990 | 425 |
| MR_1774412866_55EA05B6 | 504990 | 816 | -92.7 | 504990 | 15 | -92.9 | 504990 | 105 | -105.3 | 504990 | 425 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 35: `c3760904-0d8...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `c3760904-0d87-42dc-863b-58103e8785ba` |
| Tag | **single-answer** |
| 정답 | **C17** |
| C17 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3264355_4 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[35] topology](images/train_0035.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3273510_2
- `C2`: Press down the tilt angle of 3264355_4 by 4 degrees
- `C3`: Increase A3 Offset threshold for 3273510_2
- `C4`: Adjust the azimuth of 3273510_2 by 18 degrees
- `C5`: Increase transmission power for 3273510_2
- `C6`: Check test server and transmission issues
- `C7`: Lift the tilt angle of 3264355_4 by 4 degrees
- `C8`: Decrease transmission power for 3273510_2
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3273510_2
- `C10`: Decrease transmission power for 3264355_4
- `C11`: Increase A3 Offset threshold for 3264355_4
- `C12`: Add neighbor relationship between 3256267_8 and 3273510_2
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3273510_2
- `C14`: Press down the tilt angle  of 3273510_2 by 3 degrees
- `C15`: Lift the tilt angle  of 3273510_2 by 3 degrees
- `C16`: Increase transmission power for 3264355_4
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3264355_4 **← 정답**
- `C18`: Add neighbor relationship between 3264355_4 and 3273510_2
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3264355_4
- `C20`: Insufficient data; more data is needed for judgment.
- `C21`: Adjust the azimuth of 3264355_4 by 32 degrees
- `C22`: Decrease A3 Offset threshold for 3264355_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.318 | MS1 | 121.4656643787 | 31.1446235098 | 213 | 504990 | -93.44 | 13.40 | 409.84 | 0.11 | 2.54 | 1591 |
| 2024-09-20 22:21:32.660 | MS1 | 121.4656759186 | 31.1446266356 | 628 | 504990 | -95.11 | 12.46 | 464.94 | 0.19 | 2.40 | 1568 |
| 2024-09-20 22:21:33.774 | MS1 | 121.4656700565 | 31.1446376830 | 937 | 504990 | -95.62 | 13.49 | 426.57 | 0.00 | 2.42 | 1600 |
| 2024-09-20 22:21:34.401 | MS1 | 121.4656587908 | 31.1446308453 | 42 | 152650 | -90.42 | 5.23 | 53.07 | 0.11 | 1.53 | 972 |
| 2024-09-20 22:21:35.547 | MS1 | 121.4656684665 | 31.1446306973 | 672 | 152650 | -96.49 | 3.46 | 92.85 | 0.20 | 1.58 | 960 |
| 2024-09-20 22:21:36.267 | MS1 | 121.4656601845 | 31.1446310258 | 200 | 152650 | -90.48 | 6.17 | 68.57 | 0.05 | 1.69 | 950 |
| 2024-09-20 22:21:37.765 | MS1 | 121.4656692999 | 31.1446270299 | 810 | 152650 | -87.04 | 4.85 | 108.21 | 0.08 | 1.88 | 923 |
| 2024-09-20 22:21:38.716 | MS1 | 121.4656729014 | 31.1446209341 | 42 | 152650 | -94.85 | 4.55 | 70.56 | 0.13 | 1.64 | 984 |
| 2024-09-20 22:21:39.439 | MS1 | 121.4656735804 | 31.1446217199 | 672 | 152650 | -87.69 | 2.37 | 64.16 | 0.18 | 1.91 | 931 |
| 2024-09-20 22:21:40.186 | MS1 | 121.4656610632 | 31.1446256238 | 200 | 152650 | -89.24 | 6.29 | 62.92 | 0.01 | 2.26 | 1600 |
| 2024-09-20 22:21:41.335 | MS1 | 121.4656689975 | 31.1446293647 | 810 | 152650 | -91.28 | 6.77 | 74.46 | 0.19 | 2.24 | 1576 |
| 2024-09-20 22:21:42.521 | MS1 | 121.4656624725 | 31.1446238333 | 42 | 152650 | -94.95 | 3.55 | 78.49 | 0.16 | 2.90 | 1590 |

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
| 3211838 | 1 | 121.4737768240 | 31.1542546186 | 319 | 14 | 0 | 22.1 | TDD | 937 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3231329 | 13 | 121.4662010380 | 31.1521809443 | 276 | 5 | 3 | 27.3 | FDD | 219 | n1 | 152650 | 30M | 4T4R | 11 | 152650 |
| 3242085 | 12 | 121.4667208739 | 31.1543005583 | 106 | 7 | 3 | 14.2 | FDD | 730 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |
| 3242502 | 3 | 121.4648003877 | 31.1513043229 | 140 | 7 | 4 | 25.0 | TDD | 628 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3244131 | 11 | 121.4716113492 | 31.1534752327 | 315 | 5 | 12 | 18.0 | FDD | 728 | n1 | 152650 | 30M | 4T4R | 18 | 152650 |
| 3252894 | 7 | 121.4663883559 | 31.1547817797 | 18 | 1 | 3 | 2.9 | FDD | 672 | n1 | 152650 | 30M | 4T4R | 22 | 152650 |
| 3256267 | 8 | 121.4715954171 | 31.1486113480 | 43 | 14 | 10 | 11.3 | FDD | 200 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |
| 3264355 | 4 | 121.4730342308 | 31.1557499294 | 242 | 3 | 4 | 27.0 | TDD | 213 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3270195 | 6 | 121.4743870771 | 31.1499206863 | 236 | 11 | 4 | 25.6 | TDD | 856 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3271223 | 9 | 121.4745615215 | 31.1539525019 | 324 | 6 | 8 | 6.3 | FDD | 42 | n1 | 152650 | 30M | 4T4R | 28 | 152650 |
| 3273510 | 2 | 121.4752150537 | 31.1554585715 | 199 | 3 | 8 | 5.4 | TDD | 106 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3274422 | 5 | 121.4732555455 | 31.1494233670 | 318 | 13 | 6 | 19.9 | TDD | 983 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3275163 | 10 | 121.4690931289 | 31.1486519823 | 289 | 13 | 11 | 24.1 | FDD | 810 | n1 | 152650 | 30M | 4T4R | 13 | 152650 |

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
| 2024-09-20 22:21:31.508 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.524 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.672 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.672 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.356 | NREventA2 | measId:1;ServCellPCI:181;Se... |
| 2024-09-20 22:21:35.502 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.703 | NREventA5 | measId:3;ServCellPCI:181;Se... |
| 2024-09-20 22:21:35.761 | NRHandoverAttempt | SourcePCI:181;SourceNR-ARFC... |
| 2024-09-20 22:21:35.789 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.802 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:35.921 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.921 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3211838 | 1 | 10.8759 | 7.7946 | -117.5492 | 10.8511 | 137.2379 | 0.0178 | 0.0194 |
| 2024_09_20 22:00 | 3273510 | 2 | 11.9406 | 18.1077 | -116.4283 | 12.3092 | 91.7551 | 0.0139 | 0.0135 |
| 2024_09_20 22:00 | 3242502 | 3 | 10.5866 | 17.9180 | -115.1512 | 11.7107 | 137.2032 | 0.0045 | 0.0123 |
| 2024_09_20 22:00 | 3264355 | 4 | 9.2647 | 7.5532 | -117.7083 | 6.0003 | 91.6868 | 0.0149 | 0.0095 |
| 2024_09_20 22:00 | 3274422 | 5 | 11.4243 | 15.9557 | -117.0214 | 14.9937 | 190.5688 | 0.0083 | 0.0118 |
| 2024_09_20 22:00 | 3270195 | 6 | 6.4271 | 19.8388 | -114.9996 | 11.5702 | 162.5610 | 0.0096 | 0.0026 |
| 2024_09_20 22:00 | 3252894 | 7 | 12.2053 | 7.1643 | -114.8025 | 4.5929 | 53.7581 | 0.0104 | 0.0086 |
| 2024_09_20 22:00 | 3256267 | 8 | 18.4444 | 16.5418 | -115.3994 | 4.1065 | 42.5715 | 0.0059 | 0.0035 |
| 2024_09_20 22:00 | 3271223 | 9 | 7.9125 | 7.9473 | -117.4869 | 3.7370 | 35.4402 | 0.0195 | 0.0162 |
| 2024_09_20 22:00 | 3275163 | 10 | 11.3956 | 5.7438 | -117.5265 | 4.8829 | 29.5699 | 0.0110 | 0.0152 |
| 2024_09_20 22:00 | 3244131 | 11 | 17.9201 | 10.2563 | -114.6917 | 3.5808 | 42.5766 | 0.0111 | 0.0095 |
| 2024_09_20 22:00 | 3242085 | 12 | 14.4910 | 6.5246 | -116.8894 | 3.8284 | 53.0156 | 0.0117 | 0.0165 |
| 2024_09_20 22:00 | 3231329 | 13 | 18.6339 | 5.7992 | -116.0442 | 3.8438 | 37.4790 | 0.0124 | 0.0177 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416716_10145B14 | 504990 | 937 | -94.4 | 504990 | 106 | -94.8 | 504990 | 856 | -93.4 | 504990 | 983 |
| MR_1774416716_30CF9A95 | 504990 | 937 | -96.9 | 504990 | 106 | -93.9 | 504990 | 856 | -94.6 | 504990 | 983 |
| MR_1774416716_67F7E9FC | 152650 | 42 | -89.3 | 152650 | 730 | -99.5 | 152650 | 219 | -98.9 | 152650 | 728 |
| MR_1774416716_E2879583 | 504990 | 937 | -94.5 | 504990 | 106 | -93.6 | 504990 | 856 | -95.4 | 504990 | 983 |
| MR_1774416716_6933E622 | 504990 | 937 | -97.1 | 504990 | 106 | -93.2 | 504990 | 856 | -95.0 | 504990 | 983 |
| MR_1774416716_6E4ED738 | 152650 | 42 | -90.3 | 152650 | 730 | -96.2 | 152650 | 219 | -100.3 | 152650 | 728 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 36: `4fb7da43-d26...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `4fb7da43-d261-4d61-a459-c47b9b8823a7` |
| Tag | **single-answer** |
| 정답 | **C17** |
| C17 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3236777_1 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[36] topology](images/train_0036.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment.
- `C2`: Decrease A3 Offset threshold for 3242974_3
- `C3`: Decrease transmission power for 3236777_1
- `C4`: Lift the tilt angle of 3236777_1 by 3 degrees
- `C5`: Add neighbor relationship between 3236777_1 and 3242974_3
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3236777_1
- `C7`: Increase transmission power for 3242974_3
- `C8`: Press down the tilt angle of 3236777_1 by 3 degrees
- `C9`: Check test server and transmission issues
- `C10`: Adjust the azimuth of 3236777_1 by 14 degrees
- `C11`: Press down the tilt angle  of 3242974_3 by 8 degrees
- `C12`: Lift the tilt angle  of 3242974_3 by 8 degrees
- `C13`: Increase transmission power for 3236777_1
- `C14`: Decrease A3 Offset threshold for 3236777_1
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3242974_3
- `C16`: Increase A3 Offset threshold for 3242974_3
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3236777_1 **← 정답**
- `C18`: Increase A3 Offset threshold for 3236777_1
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3242974_3
- `C20`: Decrease transmission power for 3242974_3
- `C21`: Add neighbor relationship between 3245970_4 and 3242974_3
- `C22`: Adjust the azimuth of 3242974_3 by 50 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.490 | MS1 | 121.4656737550 | 31.1446377189 | 680 | 504990 | -88.15 | 15.50 | 373.27 | 0.12 | 2.62 | 1574 |
| 2024-09-20 22:21:32.836 | MS1 | 121.4656640236 | 31.1446259674 | 680 | 504990 | -88.56 | 13.58 | 391.86 | 0.15 | 2.78 | 1572 |
| 2024-09-20 22:21:33.698 | MS1 | 121.4656723271 | 31.1446378185 | 680 | 504990 | -91.77 | 16.04 | 423.94 | 0.15 | 2.80 | 1575 |
| 2024-09-20 22:21:34.561 | MS1 | 121.4656738880 | 31.1446299647 | 680 | 504990 | -88.88 | 15.48 | 94.24 | 0.64 | 2.50 | 695 |
| 2024-09-20 22:21:35.314 | MS1 | 121.4656779579 | 31.1446191727 | 680 | 504990 | -88.91 | 13.64 | 66.96 | 0.54 | 2.88 | 530 |
| 2024-09-20 22:21:36.595 | MS1 | 121.4656622451 | 31.1446337723 | 680 | 504990 | -90.91 | 13.39 | 75.00 | 0.52 | 2.27 | 600 |
| 2024-09-20 22:21:37.612 | MS1 | 121.4656633518 | 31.1446215676 | 680 | 504990 | -92.75 | 12.06 | 83.87 | 0.65 | 2.51 | 577 |
| 2024-09-20 22:21:38.572 | MS1 | 121.4656604420 | 31.1446257642 | 680 | 504990 | -92.02 | 8.98 | 80.41 | 0.54 | 2.62 | 606 |
| 2024-09-20 22:21:39.479 | MS1 | 121.4656763937 | 31.1446219999 | 680 | 504990 | -91.96 | 12.09 | 74.35 | 0.52 | 2.87 | 500 |
| 2024-09-20 22:21:40.976 | MS1 | 121.4656765775 | 31.1446195241 | 680 | 504990 | -89.84 | 9.65 | 342.51 | 0.08 | 2.68 | 1589 |
| 2024-09-20 22:21:41.698 | MS1 | 121.4656734670 | 31.1446187282 | 680 | 504990 | -89.83 | 11.69 | 513.88 | 0.14 | 2.67 | 1571 |
| 2024-09-20 22:21:42.150 | MS1 | 121.4656618754 | 31.1446185008 | 680 | 504990 | -89.08 | 7.43 | 453.06 | 0.13 | 2.27 | 1562 |

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
| 3236777 | 1 | 121.4696394200 | 31.1508177409 | 195 | 0 | 6 | 45.0 | TDD | 680 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3242974 | 3 | 121.4660620832 | 31.1527211392 | 336 | 6 | 5 | 30.4 | TDD | 60 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3245652 | 2 | 121.4712900301 | 31.1545681553 | 76 | 3 | 12 | 29.8 | TDD | 675 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3245970 | 4 | 121.4739421858 | 31.1460354151 | 18 | 3 | 5 | 27.4 | TDD | 844 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |

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
| 2024-09-20 22:21:31.581 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.597 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.736 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.736 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.462 | NREventA3 | measId:2;ServCellPCI:58;Ser... |
| 2024-09-20 22:21:38.702 | NRHandoverAttempt | SourcePCI:58;SourceNR-ARFCN... |
| 2024-09-20 22:21:38.748 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.759 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.881 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.881 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3236777 | 1 | 11.3594 | 12.7364 | -116.3887 | 19.0935 | 185.4307 | 0.0043 | 0.0070 |
| 2024_09_20 22:00 | 3245652 | 2 | 11.8685 | 17.2874 | -114.4239 | 19.3025 | 109.4468 | 0.0175 | 0.0016 |
| 2024_09_20 22:00 | 3242974 | 3 | 15.2435 | 12.1210 | -115.6252 | 14.8005 | 132.0578 | 0.0163 | 0.0008 |
| 2024_09_20 22:00 | 3245970 | 4 | 18.7408 | 10.1929 | -114.8210 | 10.5471 | 145.5237 | 0.0111 | 0.0197 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414815_13DAA011 | 504990 | 680 | -90.5 | 504990 | 60 | -88.5 | 504990 | 844 | -101.2 | 504990 | 675 |
| MR_1774414815_373B1E84 | 504990 | 680 | -88.4 | 504990 | 60 | -90.0 | 504990 | 844 | -102.8 | 504990 | 675 |
| MR_1774414815_48DFF32F | 504990 | 680 | -89.0 | 504990 | 60 | -91.1 | 504990 | 844 | -100.4 | 504990 | 675 |
| MR_1774414815_89D1806B | 504990 | 680 | -87.0 | 504990 | 60 | -88.5 | 504990 | 844 | -101.6 | 504990 | 675 |
| MR_1774414815_0B9DA659 | 504990 | 680 | -89.4 | 504990 | 60 | -91.7 | 504990 | 844 | -101.2 | 504990 | 675 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 37: `1caef10f-900...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `1caef10f-900e-4b2d-8495-f20808d8f47f` |
| Tag | **multiple-answer** |
| 정답 | **C5|C15** |
| C5 의미 | Press down the tilt angle  of 3250590_3 by 4 degrees |
| C15 의미 | Decrease transmission power for 3250590_3 |
| 패턴 분류 | **P3 Overshoot (tilt)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[37] topology](images/train_0037.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3276950_1
- `C2`: Add neighbor relationship between 3276950_1 and 3250590_3
- `C3`: Insufficient data; more data is needed for judgment.
- `C4`: Check test server and transmission issues
- `C5`: Press down the tilt angle  of 3250590_3 by 4 degrees **← 정답**
- `C6`: Decrease A3 Offset threshold for 3250590_3
- `C7`: Add neighbor relationship between 3261370_2 and 3250590_3
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3276950_1
- `C9`: Adjust the azimuth of 3250590_3 by 27 degrees
- `C10`: Adjust the azimuth of 3276950_1 by 9 degrees
- `C11`: Increase transmission power for 3250590_3
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3276950_1
- `C13`: Increase A3 Offset threshold for 3276950_1
- `C14`: Press down the tilt angle of 3276950_1 by 4 degrees
- `C15`: Decrease transmission power for 3250590_3 **← 정답**
- `C16`: Lift the tilt angle of 3276950_1 by 4 degrees
- `C17`: Increase A3 Offset threshold for 3250590_3
- `C18`: Increase transmission power for 3276950_1
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3250590_3
- `C20`: Decrease transmission power for 3276950_1
- `C21`: Lift the tilt angle  of 3250590_3 by 4 degrees
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3250590_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.393 | MS1 | 121.4656608305 | 31.1446221043 | 344 | 504990 | -80.46 | 17.48 | 387.05 | 0.10 | 2.84 | 1560 |
| 2024-09-20 22:21:32.383 | MS1 | 121.4656697653 | 31.1446366296 | 344 | 504990 | -83.41 | 15.59 | 529.83 | 0.09 | 2.62 | 1585 |
| 2024-09-20 22:21:33.561 | MS1 | 121.4656725039 | 31.1446182773 | 344 | 504990 | -82.08 | 14.57 | 516.24 | 0.09 | 2.08 | 1588 |
| 2024-09-20 22:21:34.945 | MS1 | 121.4656590216 | 31.1446328084 | 344 | 504990 | -89.52 | 0.30 | 82.68 | 0.09 | 1.06 | 1566 |
| 2024-09-20 22:21:35.811 | MS1 | 121.4656662612 | 31.1446335192 | 344 | 504990 | -91.92 | 0.38 | 54.22 | 0.17 | 1.10 | 1588 |
| 2024-09-20 22:21:36.565 | MS1 | 121.4656647260 | 31.1446223268 | 344 | 504990 | -91.62 | 3.75 | 65.70 | 0.19 | 1.44 | 1598 |
| 2024-09-20 22:21:37.448 | MS1 | 121.4656647560 | 31.1446222232 | 344 | 504990 | -91.02 | 1.98 | 61.89 | 0.19 | 1.47 | 1563 |
| 2024-09-20 22:21:38.440 | MS1 | 121.4656608697 | 31.1446283249 | 344 | 504990 | -85.67 | 3.81 | 53.73 | 0.12 | 1.17 | 1596 |
| 2024-09-20 22:21:39.533 | MS1 | 121.4656593700 | 31.1446364342 | 344 | 504990 | -92.25 | 0.51 | 81.94 | 0.09 | 1.07 | 1574 |
| 2024-09-20 22:21:40.878 | MS1 | 121.4656696770 | 31.1446197850 | 344 | 504990 | -75.19 | 12.66 | 391.93 | 0.09 | 2.22 | 1589 |
| 2024-09-20 22:21:41.734 | MS1 | 121.4656654809 | 31.1446351248 | 344 | 504990 | -76.43 | 15.82 | 403.61 | 0.01 | 2.50 | 1575 |
| 2024-09-20 22:21:42.696 | MS1 | 121.4656591291 | 31.1446198870 | 344 | 504990 | -83.03 | 14.27 | 463.83 | 0.20 | 2.17 | 1570 |

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
| 3249475 | 4 | 121.4669027400 | 31.1457355154 | 288 | 13 | 8 | 44.7 | TDD | 493 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3250590 | 3 | 121.4664063979 | 31.1528250391 | 157 | 3 | 3 | 20.7 | TDD | 312 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3261370 | 2 | 121.4739693664 | 31.1476980754 | 227 | 8 | 2 | 31.9 | TDD | 873 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3276950 | 1 | 121.4656889082 | 31.1492582386 | 189 | 0 | 7 | 39.2 | TDD | 344 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |

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
| 2024-09-20 22:21:31.471 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.488 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.635 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.635 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3276950 | 1 | 17.9673 | 12.2821 | -108.6164 | 8.0876 | 142.7404 | 0.0066 | 0.0133 |
| 2024_09_20 22:00 | 3261370 | 2 | 15.4984 | 13.6732 | -116.2583 | 11.7014 | 180.9513 | 0.0049 | 0.0165 |
| 2024_09_20 22:00 | 3250590 | 3 | 15.1237 | 9.8619 | -114.6269 | 16.0166 | 107.5832 | 0.0034 | 0.0090 |
| 2024_09_20 22:00 | 3249475 | 4 | 17.4152 | 12.7912 | -115.3602 | 10.3172 | 171.6344 | 0.0105 | 0.0037 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415041_52CE8077 | 504990 | 312 | -89.8 | 504990 | 344 | -87.8 | 504990 | 873 | -88.9 | 504990 | 493 |
| MR_1774415041_FB12747A | 504990 | 344 | -90.1 | 504990 | 312 | -89.9 | 504990 | 873 | -89.3 | 504990 | 493 |
| MR_1774415041_431D6D43 | 504990 | 344 | -89.3 | 504990 | 312 | -90.1 | 504990 | 873 | -88.2 | 504990 | 493 |
| MR_1774415041_CFE4CC3F | 504990 | 344 | -89.1 | 504990 | 312 | -90.8 | 504990 | 873 | -90.7 | 504990 | 493 |
| MR_1774415041_BEC44C2B | 504990 | 344 | -89.6 | 504990 | 312 | -89.4 | 504990 | 873 | -91.0 | 504990 | 493 |
| MR_1774415041_93A9265D | 504990 | 344 | -90.7 | 504990 | 312 | -89.3 | 504990 | 873 | -89.0 | 504990 | 493 |
| MR_1774415041_E9E7DE65 | 504990 | 344 | -91.2 | 504990 | 312 | -90.7 | 504990 | 873 | -89.8 | 504990 | 493 |
| MR_1774415041_F6332DCC | 504990 | 344 | -87.6 | 504990 | 312 | -87.3 | 504990 | 873 | -88.2 | 504990 | 493 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 38: `7b6d8a8a-201...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `7b6d8a8a-2016-402d-91cd-04d74d04487f` |
| Tag | **single-answer** |
| 정답 | **C13** |
| C13 의미 | Decrease A3 Offset threshold for 3217332_4 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[38] topology](images/train_0038.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Check test server and transmission issues
- `C2`: Decrease transmission power for 3218044_1
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3218044_1
- `C4`: Add neighbor relationship between 3217332_4 and 3218044_1
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3217332_4
- `C6`: Decrease transmission power for 3217332_4
- `C7`: Lift the tilt angle  of 3218044_1 by 10 degrees
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3218044_1
- `C9`: Increase transmission power for 3218044_1
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3217332_4
- `C11`: Press down the tilt angle of 3217332_4 by 10 degrees
- `C12`: Press down the tilt angle  of 3218044_1 by 10 degrees
- `C13`: Decrease A3 Offset threshold for 3217332_4 **← 정답**
- `C14`: Decrease A3 Offset threshold for 3218044_1
- `C15`: Increase A3 Offset threshold for 3217332_4
- `C16`: Add neighbor relationship between 3245147_2 and 3218044_1
- `C17`: Lift the tilt angle of 3217332_4 by 10 degrees
- `C18`: Adjust the azimuth of 3218044_1 by 50 degrees
- `C19`: Increase A3 Offset threshold for 3218044_1
- `C20`: Insufficient data; more data is needed for judgment.
- `C21`: Adjust the azimuth of 3217332_4 by 50 degrees
- `C22`: Increase transmission power for 3217332_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.171 | MS1 | 121.4656743760 | 31.1446248511 | 990 | 504990 | -75.69 | 12.46 | 558.35 | 0.08 | 2.97 | 1570 |
| 2024-09-20 22:21:32.551 | MS1 | 121.4656710432 | 31.1446266084 | 990 | 504990 | -84.07 | 16.20 | 537.57 | 0.10 | 2.39 | 1582 |
| 2024-09-20 22:21:33.356 | MS1 | 121.4656773855 | 31.1446337484 | 990 | 504990 | -80.24 | 13.60 | 346.17 | 0.10 | 2.13 | 1571 |
| 2024-09-20 22:21:34.187 | MS1 | 121.4656638295 | 31.1446335372 | 990 | 504990 | -92.41 | -1.40 | 28.34 | 0.15 | 1.07 | 1568 |
| 2024-09-20 22:21:35.519 | MS1 | 121.4656744229 | 31.1446279100 | 990 | 504990 | -92.59 | -2.06 | 52.20 | 0.18 | 1.50 | 1566 |
| 2024-09-20 22:21:36.711 | MS1 | 121.4656760366 | 31.1446224539 | 990 | 504990 | -89.44 | -1.72 | 52.04 | 0.10 | 1.03 | 1598 |
| 2024-09-20 22:21:37.243 | MS1 | 121.4656769637 | 31.1446371115 | 990 | 504990 | -89.93 | -1.32 | 71.20 | 0.05 | 1.05 | 1567 |
| 2024-09-20 22:21:38.756 | MS1 | 121.4656763757 | 31.1446339304 | 990 | 504990 | -86.74 | -1.05 | 63.49 | 0.14 | 1.45 | 1598 |
| 2024-09-20 22:21:39.232 | MS1 | 121.4656740259 | 31.1446223237 | 797 | 504990 | -76.25 | 14.65 | 265.60 | 0.02 | 1.35 | 1596 |
| 2024-09-20 22:21:40.579 | MS1 | 121.4656709556 | 31.1446368959 | 797 | 504990 | -80.12 | 16.58 | 317.39 | 0.16 | 2.03 | 1597 |
| 2024-09-20 22:21:41.582 | MS1 | 121.4656598873 | 31.1446370912 | 797 | 504990 | -79.83 | 13.72 | 353.59 | 0.10 | 2.26 | 1566 |
| 2024-09-20 22:21:42.342 | MS1 | 121.4656600576 | 31.1446180184 | 797 | 504990 | -75.88 | 17.48 | 413.52 | 0.03 | 2.74 | 1563 |

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
| 3212596 | 3 | 121.4665138046 | 31.1484288535 | 137 | 8 | 0 | 27.1 | TDD | 789 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3217332 | 4 | 121.4688551550 | 31.1483332812 | 122 | 15 | 10 | 15.4 | TDD | 990 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3218044 | 1 | 121.4705554065 | 31.1519128324 | 132 | 10 | 6 | 16.6 | TDD | 797 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3245147 | 2 | 121.4697766832 | 31.1520333955 | 316 | 4 | 4 | 18.9 | TDD | 435 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |

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
| 2024-09-20 22:21:30.911 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.936 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.078 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.078 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.794 | NREventA3 | measId:2;ServCellPCI:129;Se... |
| 2024-09-20 22:21:38.034 | NRHandoverAttempt | SourcePCI:129;SourceNR-ARFC... |
| 2024-09-20 22:21:38.071 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.085 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.201 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.201 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3218044 | 1 | 14.7901 | 19.0487 | -115.3760 | 5.4706 | 193.3816 | 0.0159 | 0.0198 |
| 2024_09_20 22:00 | 3245147 | 2 | 10.0431 | 15.4608 | -114.5241 | 19.5203 | 174.1206 | 0.0104 | 0.0122 |
| 2024_09_20 22:00 | 3212596 | 3 | 7.5113 | 6.3513 | -116.6880 | 5.3100 | 119.6347 | 0.0067 | 0.0106 |
| 2024_09_20 22:00 | 3217332 | 4 | 10.4153 | 5.8312 | -115.5365 | 5.5508 | 170.4204 | 0.0082 | 0.1956 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416671_EC5EA3F0 | 504990 | 990 | -91.6 | 504990 | 797 | -86.2 | 504990 | 435 | -95.3 | 504990 | 789 |
| MR_1774416671_18A893B4 | 504990 | 990 | -94.1 | 504990 | 797 | -87.3 | 504990 | 435 | -93.6 | 504990 | 789 |
| MR_1774416671_F4A0C632 | 504990 | 990 | -93.7 | 504990 | 797 | -86.7 | 504990 | 435 | -95.2 | 504990 | 789 |
| MR_1774416671_5BCEBB8C | 504990 | 990 | -93.2 | 504990 | 797 | -85.2 | 504990 | 435 | -94.4 | 504990 | 789 |
| MR_1774416671_8260A599 | 504990 | 797 | -86.8 | 504990 | 990 | -92.5 | 504990 | 435 | -96.8 | 504990 | 789 |
| MR_1774416671_F26C7CE0 | 504990 | 990 | -93.7 | 504990 | 797 | -88.7 | 504990 | 435 | -93.9 | 504990 | 789 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 39: `cd460e77-232...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `cd460e77-2324-40d0-9f0d-f6145a03b7b9` |
| Tag | **single-answer** |
| 정답 | **C22** |
| C22 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3229603_3 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[39] topology](images/train_0039.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3229603_3
- `C2`: Decrease transmission power for 3244897_4
- `C3`: Decrease A3 Offset threshold for 3229603_3
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3244897_4
- `C5`: Increase A3 Offset threshold for 3244897_4
- `C6`: Lift the tilt angle of 3229603_3 by 4 degrees
- `C7`: Lift the tilt angle  of 3244897_4 by 4 degrees
- `C8`: Check test server and transmission issues
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3229603_3
- `C10`: Increase transmission power for 3229603_3
- `C11`: Insufficient data; more data is needed for judgment.
- `C12`: Increase A3 Offset threshold for 3229603_3
- `C13`: Adjust the azimuth of 3244897_4 by 49 degrees
- `C14`: Adjust the azimuth of 3229603_3 by 17 degrees
- `C15`: Add neighbor relationship between 3229603_3 and 3244897_4
- `C16`: Press down the tilt angle  of 3244897_4 by 4 degrees
- `C17`: Increase transmission power for 3244897_4
- `C18`: Add neighbor relationship between 3236242_7 and 3244897_4
- `C19`: Decrease A3 Offset threshold for 3244897_4
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3244897_4
- `C21`: Press down the tilt angle of 3229603_3 by 4 degrees
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3229603_3 **← 정답**

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.800 | MS1 | 121.4656715896 | 31.1446327237 | 86 | 504990 | -95.12 | 12.88 | 360.73 | 0.07 | 2.88 | 1593 |
| 2024-09-20 22:21:32.732 | MS1 | 121.4656679124 | 31.1446295697 | 284 | 504990 | -94.35 | 13.23 | 387.60 | 0.09 | 2.07 | 1571 |
| 2024-09-20 22:21:33.467 | MS1 | 121.4656714090 | 31.1446205543 | 443 | 504990 | -93.34 | 13.10 | 359.15 | 0.14 | 2.20 | 1573 |
| 2024-09-20 22:21:34.255 | MS1 | 121.4656586523 | 31.1446194103 | 716 | 152650 | -96.21 | 5.57 | 59.33 | 0.16 | 1.94 | 996 |
| 2024-09-20 22:21:35.603 | MS1 | 121.4656637243 | 31.1446187189 | 41 | 152650 | -90.79 | 2.67 | 78.68 | 0.13 | 1.96 | 992 |
| 2024-09-20 22:21:36.499 | MS1 | 121.4656667915 | 31.1446241441 | 673 | 152650 | -87.64 | 6.31 | 74.91 | 0.07 | 1.60 | 941 |
| 2024-09-20 22:21:37.887 | MS1 | 121.4656700803 | 31.1446227632 | 516 | 152650 | -87.78 | 6.81 | 96.02 | 0.00 | 1.72 | 998 |
| 2024-09-20 22:21:38.636 | MS1 | 121.4656749853 | 31.1446367945 | 716 | 152650 | -91.49 | 7.02 | 89.66 | 0.19 | 1.86 | 932 |
| 2024-09-20 22:21:39.599 | MS1 | 121.4656685706 | 31.1446210353 | 41 | 152650 | -91.51 | 5.10 | 86.36 | 0.13 | 1.87 | 989 |
| 2024-09-20 22:21:40.726 | MS1 | 121.4656711811 | 31.1446185052 | 673 | 152650 | -90.25 | 7.31 | 56.46 | 0.02 | 2.14 | 1566 |
| 2024-09-20 22:21:41.599 | MS1 | 121.4656651167 | 31.1446221009 | 516 | 152650 | -87.26 | 6.63 | 45.30 | 0.05 | 2.24 | 1561 |
| 2024-09-20 22:21:42.557 | MS1 | 121.4656639796 | 31.1446230904 | 716 | 152650 | -90.66 | 5.43 | 98.43 | 0.11 | 2.47 | 1582 |

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
| 3213852 | 11 | 121.4714900935 | 31.1513064034 | 343 | 5 | 0 | 25.4 | FDD | 716 | n1 | 152650 | 30M | 4T4R | 27 | 152650 |
| 3221507 | 5 | 121.4716981674 | 31.1504048004 | 219 | 0 | 9 | 15.0 | TDD | 443 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3222252 | 6 | 121.4755649081 | 31.1554911582 | 144 | 1 | 7 | 13.8 | TDD | 284 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3229603 | 3 | 121.4685458392 | 31.1502614220 | 187 | 2 | 5 | 27.4 | TDD | 86 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3236242 | 7 | 121.4699306705 | 31.1459855604 | 91 | 3 | 2 | 24.9 | FDD | 673 | n1 | 152650 | 30M | 4T4R | 17 | 152650 |
| 3244897 | 4 | 121.4676435293 | 31.1558811002 | 238 | 3 | 11 | 25.5 | TDD | 246 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3251614 | 10 | 121.4718230858 | 31.1447875692 | 267 | 7 | 3 | 6.0 | FDD | 460 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |
| 3266025 | 2 | 121.4735382386 | 31.1475903051 | 247 | 12 | 12 | 19.0 | TDD | 301 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3271967 | 13 | 121.4647640239 | 31.1504932257 | 119 | 5 | 4 | 21.4 | FDD | 540 | n1 | 152650 | 30M | 4T4R | 19 | 152650 |
| 3276543 | 12 | 121.4729435355 | 31.1541876872 | 239 | 14 | 3 | 27.9 | FDD | 371 | n1 | 152650 | 30M | 4T4R | 19 | 152650 |
| 3277139 | 8 | 121.4723524488 | 31.1504349411 | 325 | 0 | 4 | 27.8 | FDD | 516 | n1 | 152650 | 30M | 4T4R | 28 | 152650 |
| 3277770 | 1 | 121.4663500675 | 31.1440253380 | 357 | 8 | 2 | 20.9 | TDD | 924 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3279711 | 9 | 121.4703138318 | 31.1550916211 | 202 | 10 | 3 | 22.2 | FDD | 41 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |

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
| 2024-09-20 22:21:30.882 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.904 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.005 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.005 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.760 | NREventA2 | measId:1;ServCellPCI:193;Se... |
| 2024-09-20 22:21:34.863 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.091 | NREventA5 | measId:3;ServCellPCI:193;Se... |
| 2024-09-20 22:21:35.166 | NRHandoverAttempt | SourcePCI:193;SourceNR-ARFC... |
| 2024-09-20 22:21:35.196 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.211 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:35.334 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.334 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3277770 | 1 | 6.1740 | 19.2417 | -117.4056 | 16.5732 | 179.2543 | 0.0037 | 0.0178 |
| 2024_09_20 22:00 | 3266025 | 2 | 6.7318 | 17.9022 | -117.6031 | 17.7143 | 87.1429 | 0.0158 | 0.0168 |
| 2024_09_20 22:00 | 3229603 | 3 | 7.8577 | 15.9108 | -114.7806 | 14.9122 | 150.9775 | 0.0075 | 0.0140 |
| 2024_09_20 22:00 | 3244897 | 4 | 16.6723 | 16.3666 | -117.6045 | 10.3194 | 152.1119 | 0.0164 | 0.0133 |
| 2024_09_20 22:00 | 3221507 | 5 | 6.6762 | 7.7338 | -114.4280 | 7.0153 | 121.6688 | 0.0147 | 0.0075 |
| 2024_09_20 22:00 | 3222252 | 6 | 17.6507 | 13.3327 | -116.1068 | 11.2973 | 163.8864 | 0.0136 | 0.0180 |
| 2024_09_20 22:00 | 3236242 | 7 | 7.3535 | 6.1144 | -115.4336 | 3.7499 | 48.0564 | 0.0128 | 0.0063 |
| 2024_09_20 22:00 | 3277139 | 8 | 8.9443 | 12.0578 | -114.7673 | 4.7247 | 32.4539 | 0.0171 | 0.0041 |
| 2024_09_20 22:00 | 3279711 | 9 | 17.7217 | 6.0192 | -114.3069 | 4.8945 | 48.9395 | 0.0002 | 0.0171 |
| 2024_09_20 22:00 | 3251614 | 10 | 8.8445 | 6.0163 | -117.4568 | 4.9235 | 49.1850 | 0.0177 | 0.0154 |
| 2024_09_20 22:00 | 3213852 | 11 | 8.7607 | 9.5073 | -115.6508 | 4.3098 | 27.9483 | 0.0159 | 0.0134 |
| 2024_09_20 22:00 | 3276543 | 12 | 13.1752 | 9.5987 | -115.0509 | 4.6714 | 27.1739 | 0.0059 | 0.0173 |
| 2024_09_20 22:00 | 3271967 | 13 | 18.3867 | 8.5175 | -117.8353 | 4.5682 | 46.9054 | 0.0038 | 0.0001 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415684_CBDBDA83 | 152650 | 716 | -94.7 | 152650 | 460 | -100.9 | 152650 | 371 | -103.2 | 152650 | 540 |
| MR_1774415684_F368D94B | 152650 | 716 | -98.0 | 152650 | 460 | -103.1 | 152650 | 371 | -104.5 | 152650 | 540 |
| MR_1774415684_1F0F4515 | 152650 | 716 | -96.6 | 152650 | 460 | -104.1 | 152650 | 371 | -104.1 | 152650 | 540 |
| MR_1774415684_1FD43884 | 152650 | 716 | -97.3 | 152650 | 460 | -102.6 | 152650 | 371 | -102.2 | 152650 | 540 |
| MR_1774415684_4CAA7ACC | 152650 | 716 | -94.5 | 152650 | 460 | -100.6 | 152650 | 371 | -102.2 | 152650 | 540 |

> *... 2개 열 생략 (전체 14열)*

---
