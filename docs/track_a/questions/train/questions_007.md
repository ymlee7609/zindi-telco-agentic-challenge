# Track A 문제 분석 — train[60]~train[69]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[60] ~ train[69] (10개)

## 목차

1. [문제 60: `92e7fc49-428...`](#60) — single-answer, 정답: C4
2. [문제 61: `11841358-d52...`](#61) — single-answer, 정답: C9
3. [문제 62: `2edc834d-76b...`](#62) — single-answer, 정답: C16
4. [문제 63: `b8d29b3b-5de...`](#63) — multiple-answer, 정답: C2|C10
5. [문제 64: `92491e9d-9e2...`](#64) — single-answer, 정답: C14
6. [문제 65: `b1c10be0-f68...`](#65) — single-answer, 정답: C19
7. [문제 66: `734ed6c7-16d...`](#66) — single-answer, 정답: C11
8. [문제 67: `624cfce0-2b9...`](#67) — single-answer, 정답: C5
9. [문제 68: `3412afd3-6fb...`](#68) — single-answer, 정답: C20
10. [문제 69: `ac638334-b1e...`](#69) — single-answer, 정답: C10

---

### 문제 60: `92e7fc49-428...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `92e7fc49-4289-4bb2-838b-700bc6233f4a` |
| Tag | **single-answer** |
| 정답 | **C4** |
| C4 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[60] topology](images/train_0060.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3239916_2
- `C2`: Decrease transmission power for 3239916_2
- `C3`: Press down the tilt angle of 3268249_3 by 9 degrees
- `C4`: Check test server and transmission issues **← 정답**
- `C5`: Increase transmission power for 3239916_2
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3239916_2
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3239916_2
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3268249_3
- `C9`: Increase A3 Offset threshold for 3268249_3
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3268249_3
- `C11`: Decrease A3 Offset threshold for 3239916_2
- `C12`: Decrease transmission power for 3268249_3
- `C13`: Increase transmission power for 3268249_3
- `C14`: Lift the tilt angle of 3268249_3 by 9 degrees
- `C15`: Add neighbor relationship between 3268249_3 and 3239916_2
- `C16`: Press down the tilt angle  of 3239916_2 by 10 degrees
- `C17`: Decrease A3 Offset threshold for 3268249_3
- `C18`: Insufficient data; more data is needed for judgment.
- `C19`: Adjust the azimuth of 3268249_3 by 50 degrees
- `C20`: Add neighbor relationship between 3234415_4 and 3239916_2
- `C21`: Lift the tilt angle  of 3239916_2 by 10 degrees
- `C22`: Adjust the azimuth of 3239916_2 by 50 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.581 | MS1 | 121.4656727098 | 31.1446307398 | 359 | 504990 | -90.05 | 14.24 | 487.20 | 0.09 | 2.60 | 1580 |
| 2024-09-20 22:21:32.671 | MS1 | 121.4656758678 | 31.1446241576 | 359 | 504990 | -90.68 | 17.72 | 577.63 | 0.04 | 2.15 | 1596 |
| 2024-09-20 22:21:33.312 | MS1 | 121.4656581521 | 31.1446356663 | 359 | 504990 | -91.27 | 16.51 | 473.27 | 0.05 | 2.66 | 1577 |
| 2024-09-20 22:21:34.515 | MS1 | 121.4656692719 | 31.1446257426 | 359 | 504990 | -89.85 | 13.49 | 67.26 | 0.06 | 2.72 | 393 |
| 2024-09-20 22:21:35.237 | MS1 | 121.4656769080 | 31.1446363891 | 359 | 504990 | -88.40 | 16.91 | 52.73 | 0.09 | 2.96 | 468 |
| 2024-09-20 22:21:36.612 | MS1 | 121.4656698054 | 31.1446286020 | 359 | 504990 | -90.23 | 17.25 | 102.64 | 0.09 | 2.46 | 402 |
| 2024-09-20 22:21:37.833 | MS1 | 121.4656705399 | 31.1446368123 | 359 | 504990 | -92.26 | 12.17 | 79.39 | 0.11 | 2.06 | 421 |
| 2024-09-20 22:21:38.952 | MS1 | 121.4656685956 | 31.1446222360 | 359 | 504990 | -90.83 | 9.79 | 68.36 | 0.07 | 2.15 | 454 |
| 2024-09-20 22:21:39.117 | MS1 | 121.4656649827 | 31.1446355746 | 359 | 504990 | -91.28 | 8.70 | 92.23 | 0.15 | 2.85 | 399 |
| 2024-09-20 22:21:40.819 | MS1 | 121.4656678676 | 31.1446259716 | 359 | 504990 | -90.85 | 10.78 | 523.43 | 0.00 | 2.79 | 1568 |
| 2024-09-20 22:21:41.344 | MS1 | 121.4656587534 | 31.1446208442 | 359 | 504990 | -91.89 | 7.15 | 410.79 | 0.12 | 2.68 | 1596 |
| 2024-09-20 22:21:42.918 | MS1 | 121.4656588515 | 31.1446258655 | 359 | 504990 | -92.00 | 8.15 | 508.81 | 0.12 | 2.74 | 1562 |

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
| 3234415 | 4 | 121.4708439069 | 31.1518783897 | 28 | 6 | 6 | 16.0 | TDD | 815 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3239916 | 2 | 121.4720412793 | 31.1450971830 | 2 | 9 | 6 | 35.1 | TDD | 34 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3267223 | 1 | 121.4650636107 | 31.1520882908 | 130 | 1 | 2 | 35.8 | TDD | 792 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3268249 | 3 | 121.4730293090 | 31.1502798433 | 111 | 8 | 7 | 17.9 | TDD | 359 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:30.957 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.975 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.119 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.119 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.836 | NREventA3 | measId:2;ServCellPCI:761;Se... |
| 2024-09-20 22:21:38.076 | NRHandoverAttempt | SourcePCI:761;SourceNR-ARFC... |
| 2024-09-20 22:21:38.119 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.130 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.252 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.252 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3267223 | 1 | 13.7140 | 5.9749 | -117.3188 | 17.9806 | 81.7031 | 0.0003 | 0.0012 |
| 2024_09_20 22:00 | 3239916 | 2 | 14.6631 | 14.7591 | -115.7522 | 17.7364 | 134.5312 | 0.0105 | 0.0146 |
| 2024_09_20 22:00 | 3268249 | 3 | 11.5528 | 10.5748 | -115.7796 | 8.2678 | 159.8301 | 0.0044 | 0.0040 |
| 2024_09_20 22:00 | 3234415 | 4 | 14.8189 | 8.1423 | -117.9291 | 17.2908 | 195.6249 | 0.0104 | 0.0028 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416782_939B991C | 504990 | 359 | -90.0 | 504990 | 34 | -95.5 | 504990 | 815 | -95.8 | 504990 | 792 |
| MR_1774416782_09206DF2 | 504990 | 359 | -88.8 | 504990 | 34 | -94.7 | 504990 | 815 | -98.4 | 504990 | 792 |
| MR_1774416782_35407E31 | 504990 | 359 | -91.8 | 504990 | 34 | -98.7 | 504990 | 815 | -96.3 | 504990 | 792 |
| MR_1774416782_D6A562B9 | 504990 | 359 | -89.5 | 504990 | 34 | -95.3 | 504990 | 815 | -96.8 | 504990 | 792 |
| MR_1774416782_33547DA5 | 504990 | 359 | -91.5 | 504990 | 34 | -96.9 | 504990 | 815 | -98.5 | 504990 | 792 |
| MR_1774416782_6C98BAC7 | 504990 | 359 | -90.3 | 504990 | 34 | -95.5 | 504990 | 815 | -98.1 | 504990 | 792 |
| MR_1774416782_2F746300 | 504990 | 359 | -90.5 | 504990 | 34 | -95.8 | 504990 | 815 | -98.7 | 504990 | 792 |
| MR_1774416782_C8C474F4 | 504990 | 359 | -90.9 | 504990 | 34 | -94.7 | 504990 | 815 | -96.7 | 504990 | 792 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 61: `11841358-d52...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `11841358-d522-49cb-b47d-377f3b78b4ba` |
| Tag | **single-answer** |
| 정답 | **C9** |
| C9 의미 | Decrease A3 Offset threshold for 3222676_2 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[61] topology](images/train_0061.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3222676_2
- `C2`: Insufficient data; more data is needed for judgment.
- `C3`: Increase A3 Offset threshold for 3220574_4
- `C4`: Decrease transmission power for 3220574_4
- `C5`: Adjust the azimuth of 3222676_2 by 25 degrees
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3220574_4
- `C7`: Add neighbor relationship between 3225218_3 and 3220574_4
- `C8`: Lift the tilt angle of 3222676_2 by 9 degrees
- `C9`: Decrease A3 Offset threshold for 3222676_2 **← 정답**
- `C10`: Press down the tilt angle  of 3220574_4 by 10 degrees
- `C11`: Decrease transmission power for 3222676_2
- `C12`: Increase transmission power for 3222676_2
- `C13`: Press down the tilt angle of 3222676_2 by 9 degrees
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3220574_4
- `C15`: Increase transmission power for 3220574_4
- `C16`: Lift the tilt angle  of 3220574_4 by 10 degrees
- `C17`: Check test server and transmission issues
- `C18`: Add neighbor relationship between 3222676_2 and 3220574_4
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3222676_2
- `C20`: Increase A3 Offset threshold for 3222676_2
- `C21`: Adjust the azimuth of 3220574_4 by 50 degrees
- `C22`: Decrease A3 Offset threshold for 3220574_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.896 | MS1 | 121.4656713099 | 31.1446236176 | 382 | 504990 | -79.40 | 13.15 | 368.11 | 0.12 | 2.37 | 1583 |
| 2024-09-20 22:21:32.763 | MS1 | 121.4656690920 | 31.1446349643 | 382 | 504990 | -82.14 | 14.54 | 415.34 | 0.13 | 2.60 | 1560 |
| 2024-09-20 22:21:33.491 | MS1 | 121.4656636112 | 31.1446333928 | 382 | 504990 | -84.70 | 12.50 | 504.18 | 0.15 | 2.42 | 1569 |
| 2024-09-20 22:21:34.460 | MS1 | 121.4656668166 | 31.1446341356 | 382 | 504990 | -91.91 | -0.04 | 69.64 | 0.02 | 1.39 | 1581 |
| 2024-09-20 22:21:35.724 | MS1 | 121.4656620124 | 31.1446185853 | 382 | 504990 | -90.61 | -3.03 | 49.16 | 0.16 | 1.05 | 1583 |
| 2024-09-20 22:21:36.725 | MS1 | 121.4656733537 | 31.1446266782 | 382 | 504990 | -86.56 | -1.09 | 49.70 | 0.01 | 1.03 | 1575 |
| 2024-09-20 22:21:37.216 | MS1 | 121.4656619715 | 31.1446327416 | 382 | 504990 | -84.52 | -0.23 | 54.13 | 0.19 | 1.06 | 1567 |
| 2024-09-20 22:21:38.738 | MS1 | 121.4656607044 | 31.1446188001 | 382 | 504990 | -86.38 | -3.61 | 39.56 | 0.04 | 1.43 | 1594 |
| 2024-09-20 22:21:39.135 | MS1 | 121.4656591569 | 31.1446368355 | 734 | 504990 | -84.01 | 15.97 | 157.85 | 0.14 | 1.11 | 1581 |
| 2024-09-20 22:21:40.136 | MS1 | 121.4656775632 | 31.1446211316 | 734 | 504990 | -79.50 | 15.53 | 320.71 | 0.01 | 2.60 | 1585 |
| 2024-09-20 22:21:41.430 | MS1 | 121.4656676735 | 31.1446188823 | 734 | 504990 | -77.54 | 14.11 | 298.11 | 0.10 | 2.41 | 1582 |
| 2024-09-20 22:21:42.879 | MS1 | 121.4656707033 | 31.1446232357 | 734 | 504990 | -77.28 | 16.41 | 489.39 | 0.19 | 2.02 | 1599 |

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
| 3220574 | 4 | 121.4664686870 | 31.1484135842 | 36 | 13 | 5 | 15.0 | TDD | 734 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3222676 | 2 | 121.4748834458 | 31.1538164008 | 246 | 7 | 9 | 43.8 | TDD | 382 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3225218 | 3 | 121.4693612038 | 31.1477811078 | 19 | 5 | 7 | 49.2 | TDD | 325 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3276471 | 1 | 121.4643176706 | 31.1495319256 | 87 | 8 | 2 | 49.2 | TDD | 592 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:31.255 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.255 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.957 | NREventA3 | measId:2;ServCellPCI:390;Se... |
| 2024-09-20 22:21:38.197 | NRHandoverAttempt | SourcePCI:390;SourceNR-ARFC... |
| 2024-09-20 22:21:38.244 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.256 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.395 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.395 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3276471 | 1 | 16.1731 | 19.1586 | -117.9671 | 17.6689 | 157.8517 | 0.0175 | 0.0126 |
| 2024_09_20 22:00 | 3222676 | 2 | 15.6396 | 10.3613 | -114.4338 | 9.5657 | 184.1625 | 0.0049 | 0.1161 |
| 2024_09_20 22:00 | 3225218 | 3 | 7.6161 | 15.7046 | -117.7927 | 11.0902 | 163.9505 | 0.0156 | 0.0160 |
| 2024_09_20 22:00 | 3220574 | 4 | 7.1135 | 17.1035 | -115.6852 | 16.6865 | 199.5085 | 0.0126 | 0.0144 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414348_C136E837 | 504990 | 734 | -87.2 | 504990 | 382 | -93.2 | 504990 | 325 | -93.1 | 504990 | 592 |
| MR_1774414348_466741BA | 504990 | 734 | -89.8 | 504990 | 382 | -92.2 | 504990 | 325 | -89.7 | 504990 | 592 |
| MR_1774414348_23F541D3 | 504990 | 382 | -90.2 | 504990 | 734 | -88.9 | 504990 | 325 | -90.7 | 504990 | 592 |
| MR_1774414348_545FFC9A | 504990 | 382 | -91.4 | 504990 | 734 | -86.8 | 504990 | 325 | -91.5 | 504990 | 592 |
| MR_1774414348_966D6DE8 | 504990 | 734 | -89.2 | 504990 | 382 | -91.1 | 504990 | 325 | -89.4 | 504990 | 592 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 62: `2edc834d-76b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `2edc834d-76b6-440d-95d1-dfbc40b25415` |
| Tag | **single-answer** |
| 정답 | **C16** |
| C16 의미 | Decrease A3 Offset threshold for 3262149_3 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[62] topology](images/train_0062.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3275126_1
- `C2`: Increase A3 Offset threshold for 3275126_1
- `C3`: Decrease transmission power for 3262149_3
- `C4`: Increase A3 Offset threshold for 3262149_3
- `C5`: Increase transmission power for 3275126_1
- `C6`: Press down the tilt angle  of 3275126_1 by 10 degrees
- `C7`: Decrease transmission power for 3275126_1
- `C8`: Lift the tilt angle  of 3275126_1 by 10 degrees
- `C9`: Add neighbor relationship between 3262149_3 and 3275126_1
- `C10`: Lift the tilt angle of 3262149_3 by 10 degrees
- `C11`: Adjust the azimuth of 3275126_1 by 50 degrees
- `C12`: Increase transmission power for 3262149_3
- `C13`: Press down the tilt angle of 3262149_3 by 10 degrees
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3262149_3
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3275126_1
- `C16`: Decrease A3 Offset threshold for 3262149_3 **← 정답**
- `C17`: Adjust the azimuth of 3262149_3 by 50 degrees
- `C18`: Decrease A3 Offset threshold for 3275126_1
- `C19`: Check test server and transmission issues
- `C20`: Insufficient data; more data is needed for judgment.
- `C21`: Add neighbor relationship between 3259979_4 and 3275126_1
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3262149_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.294 | MS1 | 121.4656612680 | 31.1446341967 | 667 | 504990 | -83.52 | 13.72 | 580.95 | 0.06 | 2.31 | 1575 |
| 2024-09-20 22:21:32.367 | MS1 | 121.4656700079 | 31.1446376083 | 667 | 504990 | -76.35 | 17.35 | 440.67 | 0.15 | 2.08 | 1592 |
| 2024-09-20 22:21:33.453 | MS1 | 121.4656621201 | 31.1446357921 | 667 | 504990 | -84.82 | 15.95 | 441.13 | 0.19 | 2.50 | 1577 |
| 2024-09-20 22:21:34.633 | MS1 | 121.4656640782 | 31.1446208530 | 667 | 504990 | -85.04 | -0.09 | 23.17 | 0.09 | 1.05 | 1566 |
| 2024-09-20 22:21:35.950 | MS1 | 121.4656691800 | 31.1446313626 | 667 | 504990 | -92.77 | -2.75 | 55.33 | 0.07 | 1.12 | 1585 |
| 2024-09-20 22:21:36.148 | MS1 | 121.4656594734 | 31.1446301570 | 667 | 504990 | -86.43 | -3.80 | 66.71 | 0.09 | 1.39 | 1589 |
| 2024-09-20 22:21:37.920 | MS1 | 121.4656586039 | 31.1446352018 | 667 | 504990 | -87.45 | -0.99 | 55.63 | 0.20 | 1.06 | 1598 |
| 2024-09-20 22:21:38.679 | MS1 | 121.4656620578 | 31.1446343412 | 667 | 504990 | -86.29 | -3.67 | 61.14 | 0.06 | 1.17 | 1582 |
| 2024-09-20 22:21:39.970 | MS1 | 121.4656735225 | 31.1446215210 | 440 | 504990 | -80.60 | 14.62 | 184.53 | 0.15 | 1.41 | 1565 |
| 2024-09-20 22:21:40.802 | MS1 | 121.4656662323 | 31.1446226998 | 440 | 504990 | -75.21 | 14.28 | 436.73 | 0.19 | 2.71 | 1577 |
| 2024-09-20 22:21:41.607 | MS1 | 121.4656708458 | 31.1446332158 | 440 | 504990 | -77.01 | 13.44 | 560.17 | 0.13 | 2.49 | 1564 |
| 2024-09-20 22:21:42.369 | MS1 | 121.4656689776 | 31.1446204840 | 440 | 504990 | -80.38 | 15.32 | 338.25 | 0.06 | 2.90 | 1560 |

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
| 3259979 | 4 | 121.4698232989 | 31.1466356687 | 163 | 3 | 11 | 18.6 | TDD | 965 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3262149 | 3 | 121.4645640259 | 31.1476266011 | 42 | 6 | 1 | 48.1 | TDD | 667 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3264265 | 2 | 121.4716073509 | 31.1545895466 | 47 | 3 | 10 | 46.8 | TDD | 523 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3275126 | 1 | 121.4721678678 | 31.1490330540 | 94 | 9 | 12 | 34.9 | TDD | 440 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

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
| 2024-09-20 22:21:31.108 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.129 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.257 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.257 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.924 | NREventA3 | measId:2;ServCellPCI:335;Se... |
| 2024-09-20 22:21:38.164 | NRHandoverAttempt | SourcePCI:335;SourceNR-ARFC... |
| 2024-09-20 22:21:38.210 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.225 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.336 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.336 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3275126 | 1 | 11.4452 | 13.1295 | -117.1636 | 7.7588 | 180.5365 | 0.0127 | 0.0155 |
| 2024_09_20 22:00 | 3264265 | 2 | 16.0158 | 16.9230 | -117.1558 | 13.1536 | 109.7714 | 0.0077 | 0.0074 |
| 2024_09_20 22:00 | 3262149 | 3 | 6.5516 | 12.7978 | -115.7264 | 13.0313 | 183.6988 | 0.0181 | 0.1898 |
| 2024_09_20 22:00 | 3259979 | 4 | 18.7364 | 18.2899 | -114.8593 | 16.0981 | 158.0480 | 0.0118 | 0.0127 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416993_FAC71A9B | 504990 | 440 | -79.9 | 504990 | 667 | -86.6 | 504990 | 965 | -81.7 | 504990 | 523 |
| MR_1774416993_45B8CD96 | 504990 | 667 | -85.1 | 504990 | 440 | -80.2 | 504990 | 965 | -82.1 | 504990 | 523 |
| MR_1774416993_1373464E | 504990 | 667 | -83.7 | 504990 | 440 | -78.3 | 504990 | 965 | -80.7 | 504990 | 523 |
| MR_1774416993_BC97C75E | 504990 | 667 | -85.1 | 504990 | 440 | -81.3 | 504990 | 965 | -81.5 | 504990 | 523 |
| MR_1774416993_0A00A0D9 | 504990 | 440 | -80.3 | 504990 | 667 | -83.0 | 504990 | 965 | -79.4 | 504990 | 523 |
| MR_1774416993_FD91BC69 | 504990 | 667 | -86.6 | 504990 | 440 | -81.5 | 504990 | 965 | -80.1 | 504990 | 523 |
| MR_1774416993_186E8878 | 504990 | 440 | -81.0 | 504990 | 667 | -83.9 | 504990 | 965 | -80.2 | 504990 | 523 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 63: `b8d29b3b-5de...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `b8d29b3b-5de8-47f5-9786-e25f4bf3e170` |
| Tag | **multiple-answer** |
| 정답 | **C2|C10** |
| C2 의미 | Decrease transmission power for 3220131_2 |
| C10 의미 | Press down the tilt angle  of 3220131_2 by 5 degrees |
| 패턴 분류 | **P3 Overshoot (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[63] topology](images/train_0063.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3259153_1
- `C2`: Decrease transmission power for 3220131_2 **← 정답**
- `C3`: Adjust the azimuth of 3259153_1 by 24 degrees
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3220131_2
- `C5`: Decrease A3 Offset threshold for 3220131_2
- `C6`: Increase transmission power for 3220131_2
- `C7`: Increase A3 Offset threshold for 3259153_1
- `C8`: Insufficient data; more data is needed for judgment.
- `C9`: Decrease A3 Offset threshold for 3259153_1
- `C10`: Press down the tilt angle  of 3220131_2 by 5 degrees **← 정답**
- `C11`: Adjust the azimuth of 3220131_2 by 20 degrees
- `C12`: Increase A3 Offset threshold for 3220131_2
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3220131_2
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3259153_1
- `C15`: Check test server and transmission issues
- `C16`: Increase transmission power for 3259153_1
- `C17`: Lift the tilt angle of 3259153_1 by 5 degrees
- `C18`: Add neighbor relationship between 3224293_3 and 3220131_2
- `C19`: Decrease transmission power for 3259153_1
- `C20`: Press down the tilt angle of 3259153_1 by 5 degrees
- `C21`: Lift the tilt angle  of 3220131_2 by 5 degrees
- `C22`: Add neighbor relationship between 3259153_1 and 3220131_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.416 | MS1 | 121.4656666992 | 31.1446276586 | 394 | 504990 | -84.67 | 16.10 | 466.53 | 0.17 | 2.98 | 1597 |
| 2024-09-20 22:21:32.115 | MS1 | 121.4656770845 | 31.1446326694 | 394 | 504990 | -77.14 | 16.43 | 339.90 | 0.08 | 2.13 | 1569 |
| 2024-09-20 22:21:33.634 | MS1 | 121.4656776503 | 31.1446211132 | 394 | 504990 | -76.65 | 16.57 | 370.15 | 0.01 | 2.40 | 1560 |
| 2024-09-20 22:21:34.447 | MS1 | 121.4656662244 | 31.1446322826 | 394 | 504990 | -90.64 | 2.45 | 46.47 | 0.20 | 1.32 | 1598 |
| 2024-09-20 22:21:35.655 | MS1 | 121.4656763243 | 31.1446263472 | 394 | 504990 | -86.01 | 3.66 | 63.90 | 0.03 | 1.22 | 1592 |
| 2024-09-20 22:21:36.489 | MS1 | 121.4656747863 | 31.1446252757 | 394 | 504990 | -88.00 | 3.80 | 80.82 | 0.04 | 1.13 | 1566 |
| 2024-09-20 22:21:37.765 | MS1 | 121.4656641693 | 31.1446190446 | 394 | 504990 | -94.06 | 3.27 | 74.42 | 0.18 | 1.29 | 1576 |
| 2024-09-20 22:21:38.735 | MS1 | 121.4656695244 | 31.1446354884 | 394 | 504990 | -89.65 | 3.45 | 66.14 | 0.12 | 1.28 | 1593 |
| 2024-09-20 22:21:39.138 | MS1 | 121.4656707270 | 31.1446330030 | 394 | 504990 | -90.21 | 2.65 | 81.10 | 0.17 | 1.30 | 1565 |
| 2024-09-20 22:21:40.495 | MS1 | 121.4656761148 | 31.1446245142 | 394 | 504990 | -81.45 | 15.04 | 608.86 | 0.12 | 2.93 | 1583 |
| 2024-09-20 22:21:41.963 | MS1 | 121.4656628559 | 31.1446308933 | 394 | 504990 | -80.68 | 14.70 | 513.48 | 0.18 | 2.37 | 1591 |
| 2024-09-20 22:21:42.582 | MS1 | 121.4656654899 | 31.1446280109 | 394 | 504990 | -82.91 | 14.83 | 332.13 | 0.17 | 2.36 | 1573 |

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
| 3220131 | 2 | 121.4748307744 | 31.1551504391 | 237 | 4 | 12 | 35.8 | TDD | 363 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3220978 | 4 | 121.4712918963 | 31.1495632866 | 236 | 3 | 11 | 25.0 | TDD | 855 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3224293 | 3 | 121.4669867054 | 31.1496734308 | 346 | 1 | 1 | 36.0 | TDD | 580 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3259153 | 1 | 121.4660144386 | 31.1549184277 | 158 | 3 | 4 | 49.6 | TDD | 394 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |

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
| 2024-09-20 22:21:30.783 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.802 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:30.948 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.948 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3259153 | 1 | 18.9146 | 10.5415 | -109.8139 | 15.0913 | 160.2504 | 0.0096 | 0.0078 |
| 2024_09_20 22:00 | 3220131 | 2 | 12.1049 | 17.5819 | -114.9065 | 8.3264 | 98.0156 | 0.0150 | 0.0007 |
| 2024_09_20 22:00 | 3224293 | 3 | 11.4348 | 9.1039 | -115.4660 | 19.6901 | 86.6388 | 0.0066 | 0.0155 |
| 2024_09_20 22:00 | 3220978 | 4 | 15.6972 | 8.2687 | -116.3158 | 12.3329 | 98.8914 | 0.0090 | 0.0051 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414974_5576E192 | 504990 | 363 | -89.7 | 504990 | 394 | -93.3 | 504990 | 580 | -92.9 | 504990 | 855 |
| MR_1774414974_775D7F39 | 504990 | 394 | -91.2 | 504990 | 363 | -92.8 | 504990 | 580 | -90.9 | 504990 | 855 |
| MR_1774414974_D9B7C232 | 504990 | 394 | -90.2 | 504990 | 363 | -91.5 | 504990 | 580 | -91.8 | 504990 | 855 |
| MR_1774414974_2D135495 | 504990 | 363 | -90.1 | 504990 | 394 | -90.4 | 504990 | 580 | -92.5 | 504990 | 855 |
| MR_1774414974_6ED67346 | 504990 | 363 | -91.9 | 504990 | 394 | -91.1 | 504990 | 580 | -94.0 | 504990 | 855 |
| MR_1774414974_D9D841CA | 504990 | 363 | -91.2 | 504990 | 394 | -92.4 | 504990 | 580 | -93.8 | 504990 | 855 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 64: `92491e9d-9e2...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `92491e9d-9e22-4b96-8a77-409385989781` |
| Tag | **single-answer** |
| 정답 | **C14** |
| C14 의미 | Decrease A3 Offset threshold for 3243772_2 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[64] topology](images/train_0064.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle  of 3237579_1 by 10 degrees
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3243772_2
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3237579_1
- `C4`: Adjust the azimuth of 3237579_1 by 50 degrees
- `C5`: Press down the tilt angle  of 3237579_1 by 10 degrees
- `C6`: Insufficient data; more data is needed for judgment.
- `C7`: Add neighbor relationship between 3243772_2 and 3237579_1
- `C8`: Increase A3 Offset threshold for 3237579_1
- `C9`: Add neighbor relationship between 3236314_4 and 3237579_1
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3237579_1
- `C11`: Lift the tilt angle of 3243772_2 by 10 degrees
- `C12`: Check test server and transmission issues
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3243772_2
- `C14`: Decrease A3 Offset threshold for 3243772_2 **← 정답**
- `C15`: Increase transmission power for 3237579_1
- `C16`: Decrease A3 Offset threshold for 3237579_1
- `C17`: Press down the tilt angle of 3243772_2 by 10 degrees
- `C18`: Decrease transmission power for 3243772_2
- `C19`: Increase A3 Offset threshold for 3243772_2
- `C20`: Decrease transmission power for 3237579_1
- `C21`: Adjust the azimuth of 3243772_2 by 50 degrees
- `C22`: Increase transmission power for 3243772_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.889 | MS1 | 121.4656675407 | 31.1446258826 | 522 | 504990 | -82.24 | 16.16 | 576.29 | 0.17 | 2.47 | 1597 |
| 2024-09-20 22:21:32.284 | MS1 | 121.4656715202 | 31.1446257079 | 522 | 504990 | -80.56 | 15.15 | 352.46 | 0.17 | 2.74 | 1580 |
| 2024-09-20 22:21:33.613 | MS1 | 121.4656740450 | 31.1446290236 | 522 | 504990 | -81.36 | 17.23 | 507.72 | 0.06 | 2.99 | 1595 |
| 2024-09-20 22:21:34.321 | MS1 | 121.4656774939 | 31.1446342613 | 522 | 504990 | -88.76 | -2.01 | 45.56 | 0.04 | 1.02 | 1575 |
| 2024-09-20 22:21:35.315 | MS1 | 121.4656587033 | 31.1446236260 | 522 | 504990 | -87.89 | -0.31 | 63.20 | 0.13 | 1.24 | 1587 |
| 2024-09-20 22:21:36.306 | MS1 | 121.4656613766 | 31.1446324148 | 522 | 504990 | -87.83 | -1.90 | 66.93 | 0.04 | 1.32 | 1587 |
| 2024-09-20 22:21:37.148 | MS1 | 121.4656584675 | 31.1446243486 | 522 | 504990 | -83.50 | -0.90 | 49.25 | 0.15 | 1.08 | 1573 |
| 2024-09-20 22:21:38.312 | MS1 | 121.4656720963 | 31.1446188686 | 522 | 504990 | -90.90 | -0.02 | 76.58 | 0.19 | 1.25 | 1569 |
| 2024-09-20 22:21:39.143 | MS1 | 121.4656640322 | 31.1446248345 | 368 | 504990 | -75.24 | 16.57 | 203.77 | 0.06 | 1.29 | 1572 |
| 2024-09-20 22:21:40.391 | MS1 | 121.4656684824 | 31.1446215619 | 368 | 504990 | -83.99 | 14.45 | 415.91 | 0.13 | 2.77 | 1596 |
| 2024-09-20 22:21:41.193 | MS1 | 121.4656582901 | 31.1446352436 | 368 | 504990 | -77.36 | 14.08 | 301.37 | 0.18 | 2.18 | 1591 |
| 2024-09-20 22:21:42.804 | MS1 | 121.4656761309 | 31.1446375987 | 368 | 504990 | -84.50 | 14.21 | 363.69 | 0.01 | 2.24 | 1578 |

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
| 3230007 | 3 | 121.4718351310 | 31.1551134514 | 40 | 1 | 5 | 43.0 | TDD | 514 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3236314 | 4 | 121.4712837839 | 31.1509534669 | 103 | 10 | 1 | 16.0 | TDD | 412 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3237579 | 1 | 121.4756750522 | 31.1554652990 | 51 | 14 | 10 | 27.2 | TDD | 368 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3243772 | 2 | 121.4680155246 | 31.1503627360 | 353 | 15 | 10 | 30.7 | TDD | 522 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |

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
| 2024-09-20 22:21:31.001 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.021 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.124 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.124 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.876 | NREventA3 | measId:2;ServCellPCI:2;Serv... |
| 2024-09-20 22:21:38.116 | NRHandoverAttempt | SourcePCI:2;SourceNR-ARFCN:... |
| 2024-09-20 22:21:38.157 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.172 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.303 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.303 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3237579 | 1 | 15.6963 | 15.6512 | -116.7588 | 11.5605 | 139.6899 | 0.0002 | 0.0027 |
| 2024_09_20 22:00 | 3243772 | 2 | 19.0142 | 10.3865 | -117.3477 | 14.3165 | 196.4734 | 0.0131 | 0.1812 |
| 2024_09_20 22:00 | 3230007 | 3 | 7.6060 | 13.9903 | -114.4150 | 8.7936 | 115.8356 | 0.0097 | 0.0104 |
| 2024_09_20 22:00 | 3236314 | 4 | 8.1086 | 16.1811 | -117.9439 | 11.3742 | 161.9996 | 0.0104 | 0.0158 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412301_2F73C907 | 504990 | 522 | -89.6 | 504990 | 368 | -83.2 | 504990 | 412 | -85.2 | 504990 | 514 |
| MR_1774412301_FFAE4DC3 | 504990 | 522 | -89.8 | 504990 | 368 | -84.1 | 504990 | 412 | -81.8 | 504990 | 514 |
| MR_1774412301_D919BB25 | 504990 | 522 | -88.0 | 504990 | 368 | -82.8 | 504990 | 412 | -81.6 | 504990 | 514 |
| MR_1774412301_4DD3D0B2 | 504990 | 368 | -85.1 | 504990 | 522 | -90.4 | 504990 | 412 | -85.5 | 504990 | 514 |
| MR_1774412301_00903E44 | 504990 | 522 | -87.4 | 504990 | 368 | -81.7 | 504990 | 412 | -82.3 | 504990 | 514 |
| MR_1774412301_41CE56D7 | 504990 | 522 | -89.0 | 504990 | 368 | -84.5 | 504990 | 412 | -85.1 | 504990 | 514 |
| MR_1774412301_16FDB886 | 504990 | 522 | -87.9 | 504990 | 368 | -84.5 | 504990 | 412 | -85.4 | 504990 | 514 |
| MR_1774412301_8D410A26 | 504990 | 368 | -85.3 | 504990 | 522 | -89.5 | 504990 | 412 | -84.5 | 504990 | 514 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 65: `b1c10be0-f68...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `b1c10be0-f68a-4ed3-819d-98e7b20bbb9e` |
| Tag | **single-answer** |
| 정답 | **C19** |
| C19 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[65] topology](images/train_0065.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3239875_3 by 26 degrees
- `C2`: Increase A3 Offset threshold for 3270407_1
- `C3`: Add neighbor relationship between 3260074_4 and 3239875_3
- `C4`: Press down the tilt angle  of 3239875_3 by 2 degrees
- `C5`: Increase A3 Offset threshold for 3239875_3
- `C6`: Decrease transmission power for 3270407_1
- `C7`: Decrease A3 Offset threshold for 3239875_3
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3239875_3
- `C9`: Decrease transmission power for 3239875_3
- `C10`: Press down the tilt angle of 3270407_1 by 10 degrees
- `C11`: Lift the tilt angle  of 3239875_3 by 2 degrees
- `C12`: Increase transmission power for 3239875_3
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3270407_1
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3239875_3
- `C15`: Add neighbor relationship between 3270407_1 and 3239875_3
- `C16`: Insufficient data; more data is needed for judgment.
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3270407_1
- `C18`: Lift the tilt angle of 3270407_1 by 10 degrees
- `C19`: Check test server and transmission issues **← 정답**
- `C20`: Increase transmission power for 3270407_1
- `C21`: Decrease A3 Offset threshold for 3270407_1
- `C22`: Adjust the azimuth of 3270407_1 by 50 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.768 | MS1 | 121.4656707641 | 31.1446366091 | 921 | 504990 | -85.30 | 17.73 | 495.57 | 0.03 | 2.88 | 1575 |
| 2024-09-20 22:21:32.157 | MS1 | 121.4656588829 | 31.1446283003 | 921 | 504990 | -85.51 | 14.88 | 512.67 | 0.10 | 2.52 | 1563 |
| 2024-09-20 22:21:33.561 | MS1 | 121.4656740542 | 31.1446331582 | 921 | 504990 | -87.31 | 14.86 | 373.13 | 0.08 | 2.05 | 1600 |
| 2024-09-20 22:21:34.234 | MS1 | 121.4656672728 | 31.1446341576 | 921 | 504990 | -85.89 | 16.74 | 81.23 | 0.01 | 2.32 | 440 |
| 2024-09-20 22:21:35.363 | MS1 | 121.4656722050 | 31.1446315278 | 921 | 504990 | -91.20 | 16.46 | 62.11 | 0.08 | 2.31 | 325 |
| 2024-09-20 22:21:36.483 | MS1 | 121.4656765417 | 31.1446196319 | 921 | 504990 | -87.97 | 17.90 | 94.27 | 0.05 | 2.83 | 379 |
| 2024-09-20 22:21:37.332 | MS1 | 121.4656657837 | 31.1446299058 | 921 | 504990 | -92.17 | 10.51 | 81.27 | 0.12 | 2.13 | 453 |
| 2024-09-20 22:21:38.925 | MS1 | 121.4656718564 | 31.1446261610 | 921 | 504990 | -93.83 | 10.86 | 77.39 | 0.16 | 2.57 | 485 |
| 2024-09-20 22:21:39.340 | MS1 | 121.4656614163 | 31.1446238042 | 921 | 504990 | -93.81 | 9.07 | 75.25 | 0.08 | 2.28 | 481 |
| 2024-09-20 22:21:40.760 | MS1 | 121.4656665235 | 31.1446312453 | 921 | 504990 | -92.76 | 12.68 | 555.53 | 0.07 | 2.16 | 1569 |
| 2024-09-20 22:21:41.436 | MS1 | 121.4656640039 | 31.1446348970 | 921 | 504990 | -93.65 | 7.08 | 416.52 | 0.01 | 2.12 | 1596 |
| 2024-09-20 22:21:42.437 | MS1 | 121.4656628075 | 31.1446262975 | 921 | 504990 | -92.52 | 10.66 | 535.12 | 0.18 | 2.30 | 1574 |

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
| 3239875 | 3 | 121.4708481620 | 31.1550155323 | 177 | 0 | 2 | 34.4 | TDD | 590 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3260074 | 4 | 121.4736589870 | 31.1522683484 | 248 | 6 | 8 | 17.4 | TDD | 774 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3270407 | 1 | 121.4710735211 | 31.1550651441 | 80 | 12 | 9 | 45.0 | TDD | 921 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3275800 | 2 | 121.4659465173 | 31.1549611309 | 15 | 4 | 8 | 42.2 | TDD | 541 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

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
| 2024-09-20 22:21:31.162 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.185 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.329 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.329 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.973 | NREventA3 | measId:2;ServCellPCI:580;Se... |
| 2024-09-20 22:21:38.213 | NRHandoverAttempt | SourcePCI:580;SourceNR-ARFC... |
| 2024-09-20 22:21:38.246 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.258 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.398 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.398 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3270407 | 1 | 16.4243 | 10.1725 | -117.0289 | 16.0797 | 110.7779 | 0.0110 | 0.0164 |
| 2024_09_20 22:00 | 3275800 | 2 | 6.4272 | 13.4340 | -115.9878 | 9.0563 | 112.5798 | 0.0175 | 0.0009 |
| 2024_09_20 22:00 | 3239875 | 3 | 19.3266 | 10.8564 | -116.1714 | 8.3071 | 187.0269 | 0.0117 | 0.0109 |
| 2024_09_20 22:00 | 3260074 | 4 | 5.9915 | 18.6891 | -114.7659 | 5.3607 | 85.9403 | 0.0196 | 0.0024 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414133_F5648A50 | 504990 | 921 | -86.6 | 504990 | 590 | -94.7 | 504990 | 774 | -99.5 | 504990 | 541 |
| MR_1774414133_4A727620 | 504990 | 921 | -86.8 | 504990 | 590 | -95.3 | 504990 | 774 | -98.4 | 504990 | 541 |
| MR_1774414133_83702A76 | 504990 | 921 | -86.5 | 504990 | 590 | -96.8 | 504990 | 774 | -97.7 | 504990 | 541 |
| MR_1774414133_E0B695B3 | 504990 | 921 | -87.1 | 504990 | 590 | -96.3 | 504990 | 774 | -99.9 | 504990 | 541 |
| MR_1774414133_19D36FA8 | 504990 | 921 | -84.1 | 504990 | 590 | -97.2 | 504990 | 774 | -101.2 | 504990 | 541 |
| MR_1774414133_103C0DD5 | 504990 | 921 | -84.4 | 504990 | 590 | -95.1 | 504990 | 774 | -98.5 | 504990 | 541 |
| MR_1774414133_8059257F | 504990 | 921 | -84.5 | 504990 | 590 | -96.8 | 504990 | 774 | -99.5 | 504990 | 541 |
| MR_1774414133_C60D9160 | 504990 | 921 | -87.7 | 504990 | 590 | -94.6 | 504990 | 774 | -97.7 | 504990 | 541 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 66: `734ed6c7-16d...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `734ed6c7-16df-4a38-9b24-31edf5219123` |
| Tag | **single-answer** |
| 정답 | **C11** |
| C11 의미 | Add neighbor relationship between 3212630_1 and 3222469_3 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[66] topology](images/train_0066.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3222469_3 by 1 degrees
- `C2`: Decrease A3 Offset threshold for 3222469_3
- `C3`: Increase transmission power for 3222469_3
- `C4`: Decrease transmission power for 3222469_3
- `C5`: Insufficient data; more data is needed for judgment.
- `C6`: Increase transmission power for 3212630_1
- `C7`: Press down the tilt angle of 3212630_1 by 10 degrees
- `C8`: Lift the tilt angle of 3212630_1 by 10 degrees
- `C9`: Adjust the azimuth of 3212630_1 by 50 degrees
- `C10`: Decrease transmission power for 3212630_1
- `C11`: Add neighbor relationship between 3212630_1 and 3222469_3 **← 정답**
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3212630_1
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3222469_3
- `C14`: Increase A3 Offset threshold for 3222469_3
- `C15`: Check test server and transmission issues
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3222469_3
- `C17`: Increase A3 Offset threshold for 3212630_1
- `C18`: Lift the tilt angle  of 3222469_3 by 2 degrees
- `C19`: Add neighbor relationship between 3237841_2 and 3222469_3
- `C20`: Press down the tilt angle  of 3222469_3 by 2 degrees
- `C21`: Decrease A3 Offset threshold for 3212630_1
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3212630_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.832 | MS1 | 121.4656627334 | 31.1446273970 | 349 | 504990 | -79.18 | 13.27 | 536.98 | 0.19 | 2.95 | 1589 |
| 2024-09-20 22:21:32.717 | MS1 | 121.4656719077 | 31.1446236709 | 349 | 504990 | -75.96 | 13.76 | 365.72 | 0.02 | 2.98 | 1583 |
| 2024-09-20 22:21:33.722 | MS1 | 121.4656642183 | 31.1446270422 | 349 | 504990 | -78.63 | 15.12 | 565.16 | 0.16 | 2.76 | 1586 |
| 2024-09-20 22:21:34.841 | MS1 | 121.4656723989 | 31.1446290622 | 349 | 504990 | -89.39 | -0.32 | 49.45 | 0.17 | 1.43 | 1580 |
| 2024-09-20 22:21:35.156 | MS1 | 121.4656605689 | 31.1446323015 | 349 | 504990 | -93.87 | -0.25 | 47.26 | 0.06 | 1.35 | 1588 |
| 2024-09-20 22:21:36.726 | MS1 | 121.4656768256 | 31.1446206292 | 349 | 504990 | -91.79 | -1.20 | 43.82 | 0.05 | 1.35 | 1588 |
| 2024-09-20 22:21:37.144 | MS1 | 121.4656729881 | 31.1446327089 | 349 | 504990 | -86.29 | -1.22 | 69.66 | 0.05 | 1.34 | 1581 |
| 2024-09-20 22:21:38.232 | MS1 | 121.4656753791 | 31.1446284489 | 349 | 504990 | -82.03 | 14.70 | 557.70 | 0.00 | 1.48 | 1560 |
| 2024-09-20 22:21:39.562 | MS1 | 121.4656682750 | 31.1446339120 | 349 | 504990 | -81.96 | 14.03 | 548.00 | 0.19 | 1.00 | 1566 |
| 2024-09-20 22:21:40.320 | MS1 | 121.4656766509 | 31.1446338358 | 349 | 504990 | -76.63 | 16.95 | 458.58 | 0.14 | 2.76 | 1570 |
| 2024-09-20 22:21:41.566 | MS1 | 121.4656636461 | 31.1446311439 | 349 | 504990 | -75.86 | 13.19 | 340.09 | 0.00 | 2.94 | 1585 |
| 2024-09-20 22:21:42.646 | MS1 | 121.4656629499 | 31.1446311366 | 349 | 504990 | -78.43 | 12.58 | 369.69 | 0.00 | 2.15 | 1596 |

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
| 3212630 | 1 | 121.4748179019 | 31.1453054464 | 330 | 9 | 3 | 40.7 | TDD | 349 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3222469 | 3 | 121.4686596004 | 31.1512185734 | 202 | 0 | 2 | 32.5 | TDD | 413 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3237841 | 2 | 121.4715420165 | 31.1463603421 | 261 | 12 | 2 | 20.0 | TDD | 549 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3243140 | 4 | 121.4687927536 | 31.1523705898 | 59 | 4 | 10 | 19.7 | TDD | 55 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |

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
| 2024-09-20 22:21:30.847 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.870 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.005 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.005 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.680 | NREventA3 | measId:2;ServCellPCI:707;Se... |
| 2024-09-20 22:21:35.680 | NREventA3 | measId:2;ServCellPCI:707;Se... |
| 2024-09-20 22:21:36.680 | NREventA3 | measId:2;ServCellPCI:707;Se... |
| 2024-09-20 22:21:39.180 | NRRRCReestablishAttempt | PCI:707 |
| 2024-09-20 22:21:39.190 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.205 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:39.355 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.355 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3212630 | 1 | 17.9873 | 5.3216 | -116.5137 | 12.4229 | 102.5810 | 0.0133 | 0.1961 |
| 2024_09_20 22:00 | 3237841 | 2 | 10.9744 | 19.2310 | -117.4458 | 19.4101 | 100.3501 | 0.0052 | 0.0195 |
| 2024_09_20 22:00 | 3222469 | 3 | 15.8826 | 6.6630 | -114.4183 | 11.0139 | 133.1714 | 0.0131 | 0.0160 |
| 2024_09_20 22:00 | 3243140 | 4 | 16.3889 | 6.7945 | -117.4578 | 19.0508 | 170.4200 | 0.0041 | 0.0100 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413758_58C80405 | 504990 | 413 | -84.5 | 504990 | 349 | -88.8 | 504990 | 549 | -89.1 | 504990 | 55 |
| MR_1774413758_F4D298F9 | 504990 | 349 | -90.6 | 504990 | 413 | -85.8 | 504990 | 549 | -90.2 | 504990 | 55 |
| MR_1774413758_549CEC0A | 504990 | 413 | -84.5 | 504990 | 349 | -88.8 | 504990 | 549 | -90.0 | 504990 | 55 |
| MR_1774413758_2E60480D | 504990 | 349 | -88.6 | 504990 | 413 | -83.6 | 504990 | 549 | -90.6 | 504990 | 55 |
| MR_1774413758_AD28708F | 504990 | 349 | -87.8 | 504990 | 413 | -84.8 | 504990 | 549 | -90.1 | 504990 | 55 |
| MR_1774413758_73065E45 | 504990 | 413 | -82.9 | 504990 | 349 | -89.6 | 504990 | 549 | -91.2 | 504990 | 55 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 67: `624cfce0-2b9...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `624cfce0-2b95-4177-b725-c4afff5ba91c` |
| Tag | **single-answer** |
| 정답 | **C5** |
| C5 의미 | Lift the tilt angle  of 3234135_4 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[67] topology](images/train_0067.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3220188_2
- `C2`: Add neighbor relationship between 3253407_1 and 3220188_2
- `C3`: Insufficient data; more data is needed for judgment.
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3253407_1
- `C5`: Lift the tilt angle  of 3234135_4 by 10 degrees **← 정답**
- `C6`: Increase transmission power for 3253407_1
- `C7`: Decrease A3 Offset threshold for 3253407_1
- `C8`: Decrease transmission power for 3220188_2
- `C9`: Lift the tilt angle of 3253407_1 by 2 degrees
- `C10`: Increase A3 Offset threshold for 3253407_1
- `C11`: Press down the tilt angle  of 3234135_4 by 10 degrees
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3220188_2
- `C13`: Increase transmission power for 3220188_2
- `C14`: Adjust the azimuth of 3253407_1 by 33 degrees
- `C15`: Check test server and transmission issues
- `C16`: Add neighbor relationship between 3234135_4 and 3220188_2
- `C17`: Adjust the azimuth of 3234135_4 by 50 degrees
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3220188_2
- `C19`: Decrease A3 Offset threshold for 3220188_2
- `C20`: Press down the tilt angle of 3253407_1 by 2 degrees
- `C21`: Decrease transmission power for 3253407_1
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3253407_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.937 | MS1 | 121.4656638366 | 31.1446284652 | 135 | 504990 | -90.11 | 16.05 | 561.81 | 0.12 | 2.64 | 1575 |
| 2024-09-20 22:21:32.512 | MS1 | 121.4656681859 | 31.1446296684 | 135 | 504990 | -85.97 | 16.70 | 442.63 | 0.13 | 2.36 | 1571 |
| 2024-09-20 22:21:33.955 | MS1 | 121.4656683492 | 31.1446263264 | 135 | 504990 | -89.34 | 16.92 | 598.21 | 0.04 | 2.33 | 1576 |
| 2024-09-20 22:21:34.298 | MS1 | 121.4656706741 | 31.1446253317 | 135 | 504990 | -87.73 | 17.92 | 84.20 | 0.10 | 2.77 | 1581 |
| 2024-09-20 22:21:35.704 | MS1 | 121.4656618954 | 31.1446181020 | 135 | 504990 | -86.64 | 15.02 | 75.55 | 0.02 | 2.78 | 1563 |
| 2024-09-20 22:21:36.761 | MS1 | 121.4656625734 | 31.1446362861 | 135 | 504990 | -88.90 | 14.12 | 75.28 | 0.03 | 2.42 | 1560 |
| 2024-09-20 22:21:37.900 | MS1 | 121.4656771881 | 31.1446224545 | 135 | 504990 | -90.11 | 7.08 | 66.97 | 0.05 | 2.01 | 1574 |
| 2024-09-20 22:21:38.251 | MS1 | 121.4656643856 | 31.1446209352 | 135 | 504990 | -92.42 | 11.21 | 64.23 | 0.02 | 2.33 | 1600 |
| 2024-09-20 22:21:39.386 | MS1 | 121.4656684123 | 31.1446232533 | 135 | 504990 | -92.41 | 9.30 | 67.71 | 0.16 | 2.06 | 1580 |
| 2024-09-20 22:21:40.437 | MS1 | 121.4656586197 | 31.1446213272 | 135 | 504990 | -90.95 | 11.62 | 392.12 | 0.13 | 2.58 | 1580 |
| 2024-09-20 22:21:41.862 | MS1 | 121.4656622354 | 31.1446204685 | 135 | 504990 | -92.27 | 10.36 | 405.45 | 0.07 | 2.99 | 1581 |
| 2024-09-20 22:21:42.393 | MS1 | 121.4656648694 | 31.1446185022 | 135 | 504990 | -93.11 | 12.21 | 592.48 | 0.14 | 2.49 | 1584 |

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
| 3220188 | 2 | 121.4675306622 | 31.1445468594 | 42 | 6 | 11 | 26.2 | TDD | 689 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3234135 | 4 | 121.4700249519 | 31.1476441600 | 14 | 3 | 12 | 30.0 | TDD | 871 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3253407 | 1 | 121.4668910693 | 31.1508534026 | 223 | 0 | 1 | 19.7 | TDD | 135 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3267179 | 3 | 121.4745818783 | 31.1512897268 | 258 | 15 | 0 | 47.1 | TDD | 567 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

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
| 2024-09-20 22:21:30.812 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.829 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:30.943 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.943 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.640 | NREventA3 | measId:2;ServCellPCI:447;Se... |
| 2024-09-20 22:21:37.880 | NRHandoverAttempt | SourcePCI:447;SourceNR-ARFC... |
| 2024-09-20 22:21:37.913 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.927 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.055 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.055 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3253407 | 1 | 85.5351 | 79.4508 | -115.7825 | 8.1367 | 184.0297 | 0.0200 | 0.0006 |
| 2024_09_20 22:00 | 3220188 | 2 | 5.6406 | 13.5036 | -117.0259 | 16.7098 | 189.0063 | 0.0031 | 0.0060 |
| 2024_09_20 22:00 | 3267179 | 3 | 10.1317 | 11.5473 | -116.7407 | 16.5040 | 128.0410 | 0.0146 | 0.0071 |
| 2024_09_20 22:00 | 3234135 | 4 | 12.8725 | 13.0306 | -117.0408 | 16.6494 | 178.8459 | 0.0166 | 0.0176 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414229_E025793D | 504990 | 135 | -88.9 | 504990 | 689 | -89.5 | 504990 | 871 | -99.0 | 504990 | 567 |
| MR_1774414229_2980D373 | 504990 | 135 | -87.9 | 504990 | 689 | -88.5 | 504990 | 871 | -100.4 | 504990 | 567 |
| MR_1774414229_C7E0C58D | 504990 | 135 | -89.3 | 504990 | 689 | -91.7 | 504990 | 871 | -100.0 | 504990 | 567 |
| MR_1774414229_346FA8AD | 504990 | 135 | -88.9 | 504990 | 689 | -92.2 | 504990 | 871 | -98.7 | 504990 | 567 |
| MR_1774414229_BAAD0867 | 504990 | 135 | -86.7 | 504990 | 689 | -92.3 | 504990 | 871 | -100.9 | 504990 | 567 |
| MR_1774414229_59BCC61C | 504990 | 135 | -88.9 | 504990 | 689 | -91.2 | 504990 | 871 | -99.4 | 504990 | 567 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 68: `3412afd3-6fb...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `3412afd3-6fb7-41d9-9e07-2ebcccebc858` |
| Tag | **single-answer** |
| 정답 | **C20** |
| C20 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[68] topology](images/train_0068.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3243225_4
- `C2`: Adjust the azimuth of 3268787_3 by 50 degrees
- `C3`: Press down the tilt angle  of 3268787_3 by 10 degrees
- `C4`: Press down the tilt angle of 3243225_4 by 8 degrees
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3243225_4
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3268787_3
- `C7`: Lift the tilt angle of 3243225_4 by 8 degrees
- `C8`: Increase A3 Offset threshold for 3268787_3
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3268787_3
- `C10`: Increase transmission power for 3243225_4
- `C11`: Lift the tilt angle  of 3268787_3 by 10 degrees
- `C12`: Check test server and transmission issues
- `C13`: Increase transmission power for 3268787_3
- `C14`: Decrease A3 Offset threshold for 3243225_4
- `C15`: Decrease transmission power for 3268787_3
- `C16`: Decrease A3 Offset threshold for 3268787_3
- `C17`: Adjust the azimuth of 3243225_4 by 50 degrees
- `C18`: Add neighbor relationship between 3259016_2 and 3268787_3
- `C19`: Add neighbor relationship between 3243225_4 and 3268787_3
- `C20`: Insufficient data; more data is needed for judgment. **← 정답**
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3243225_4
- `C22`: Increase A3 Offset threshold for 3243225_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.432 | MS1 | 121.4656639438 | 31.1446185040 | 292 | 504990 | -85.61 | 13.10 | 515.11 | 0.10 | 2.61 | 1589 |
| 2024-09-20 22:21:32.545 | MS1 | 121.4656601670 | 31.1446319608 | 292 | 504990 | -90.58 | 17.78 | 380.86 | 0.04 | 2.50 | 1561 |
| 2024-09-20 22:21:33.937 | MS1 | 121.4656608747 | 31.1446337383 | 292 | 504990 | -90.80 | 12.50 | 550.62 | 0.09 | 2.15 | 1570 |
| 2024-09-20 22:21:34.694 | MS1 | 121.4656761594 | 31.1446361624 | 292 | 504990 | -86.23 | 12.64 | 75.21 | 0.02 | 3.00 | 1564 |
| 2024-09-20 22:21:35.776 | MS1 | 121.4656684988 | 31.1446210602 | 292 | 504990 | -91.46 | 16.58 | 48.37 | 0.03 | 2.32 | 1585 |
| 2024-09-20 22:21:36.803 | MS1 | 121.4656763707 | 31.1446273267 | 292 | 504990 | -91.53 | 12.78 | 61.76 | 0.17 | 2.85 | 1567 |
| 2024-09-20 22:21:37.833 | MS1 | 121.4656680312 | 31.1446303048 | 292 | 504990 | -89.91 | 9.55 | 86.66 | 0.06 | 2.24 | 1583 |
| 2024-09-20 22:21:38.601 | MS1 | 121.4656676911 | 31.1446267121 | 292 | 504990 | -93.94 | 7.67 | 75.59 | 0.20 | 2.64 | 1594 |
| 2024-09-20 22:21:39.480 | MS1 | 121.4656594440 | 31.1446372649 | 292 | 504990 | -90.38 | 12.44 | 78.53 | 0.07 | 2.54 | 1586 |
| 2024-09-20 22:21:40.159 | MS1 | 121.4656730710 | 31.1446347127 | 292 | 504990 | -89.78 | 8.96 | 313.96 | 0.07 | 2.03 | 1584 |
| 2024-09-20 22:21:41.943 | MS1 | 121.4656759137 | 31.1446339662 | 292 | 504990 | -89.57 | 7.12 | 377.16 | 0.01 | 2.15 | 1596 |
| 2024-09-20 22:21:42.679 | MS1 | 121.4656774655 | 31.1446311455 | 292 | 504990 | -90.36 | 12.64 | 452.51 | 0.10 | 2.79 | 1578 |

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
| 3243225 | 4 | 121.4717013147 | 31.1461067902 | 328 | 5 | 8 | 32.1 | TDD | 292 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3259016 | 2 | 121.4699698738 | 31.1559163287 | 140 | 7 | 5 | 46.1 | TDD | 900 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3268787 | 3 | 121.4684296173 | 31.1446969646 | 142 | 1 | 0 | 39.6 | TDD | 780 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3268874 | 1 | 121.4735876937 | 31.1493603880 | 338 | 4 | 6 | 49.3 | TDD | 454 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |

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
| 2024-09-20 22:21:31.048 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.068 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.190 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.190 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.911 | NREventA3 | measId:2;ServCellPCI:354;Se... |
| 2024-09-20 22:21:38.151 | NRHandoverAttempt | SourcePCI:354;SourceNR-ARFC... |
| 2024-09-20 22:21:38.189 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.200 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.344 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.344 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3268874 | 1 | 88.4270 | 81.3068 | -115.2686 | 19.7134 | 169.0463 | 0.0016 | 0.0181 |
| 2024_09_19 22:00 | 3259016 | 2 | 81.9678 | 89.3000 | -114.5992 | 10.0280 | 158.9329 | 0.0139 | 0.0097 |
| 2024_09_19 22:00 | 3268787 | 3 | 75.7644 | 77.0129 | -115.2597 | 13.0376 | 104.3903 | 0.0173 | 0.0014 |
| 2024_09_19 22:00 | 3243225 | 4 | 80.2182 | 93.0514 | -117.1244 | 12.2042 | 196.9558 | 0.0088 | 0.0111 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412379_1CF60FC1 | 504990 | 292 | -88.2 | 504990 | 780 | -92.3 | 504990 | 900 | -91.6 | 504990 | 454 |
| MR_1774412379_A85CEF98 | 504990 | 292 | -87.5 | 504990 | 780 | -90.8 | 504990 | 900 | -94.3 | 504990 | 454 |
| MR_1774412379_D5786CEA | 504990 | 292 | -88.1 | 504990 | 780 | -92.5 | 504990 | 900 | -93.6 | 504990 | 454 |
| MR_1774412379_C67DC04C | 504990 | 292 | -85.6 | 504990 | 780 | -92.6 | 504990 | 900 | -93.0 | 504990 | 454 |
| MR_1774412379_1FC9DD8A | 504990 | 292 | -85.9 | 504990 | 780 | -92.1 | 504990 | 900 | -91.5 | 504990 | 454 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 69: `ac638334-b1e...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `ac638334-b1e6-4342-826c-071a78f5d24d` |
| Tag | **single-answer** |
| 정답 | **C10** |
| C10 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3268585_4 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[69] topology](images/train_0069.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Check test server and transmission issues
- `C2`: Decrease A3 Offset threshold for 3238846_5
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3238846_5
- `C4`: Increase A3 Offset threshold for 3238846_5
- `C5`: Adjust the azimuth of 3268585_4 by 20 degrees
- `C6`: Lift the tilt angle of 3268585_4 by 2 degrees
- `C7`: Press down the tilt angle of 3268585_4 by 2 degrees
- `C8`: Press down the tilt angle  of 3238846_5 by 3 degrees
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3238846_5
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3268585_4 **← 정답**
- `C11`: Decrease transmission power for 3238846_5
- `C12`: Insufficient data; more data is needed for judgment.
- `C13`: Increase A3 Offset threshold for 3268585_4
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3268585_4
- `C15`: Increase transmission power for 3238846_5
- `C16`: Add neighbor relationship between 3268585_4 and 3238846_5
- `C17`: Increase transmission power for 3268585_4
- `C18`: Adjust the azimuth of 3238846_5 by 41 degrees
- `C19`: Add neighbor relationship between 3274570_11 and 3238846_5
- `C20`: Decrease transmission power for 3268585_4
- `C21`: Decrease A3 Offset threshold for 3268585_4
- `C22`: Lift the tilt angle  of 3238846_5 by 3 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.293 | MS1 | 121.4656763878 | 31.1446279136 | 305 | 504990 | -94.21 | 12.92 | 537.67 | 0.04 | 2.69 | 1591 |
| 2024-09-20 22:21:32.907 | MS1 | 121.4656610623 | 31.1446346298 | 249 | 504990 | -95.51 | 13.11 | 548.48 | 0.07 | 2.85 | 1595 |
| 2024-09-20 22:21:33.220 | MS1 | 121.4656703397 | 31.1446315090 | 673 | 504990 | -93.75 | 13.90 | 426.59 | 0.14 | 2.81 | 1569 |
| 2024-09-20 22:21:34.829 | MS1 | 121.4656741047 | 31.1446184986 | 55 | 152650 | -93.86 | 6.49 | 79.60 | 0.09 | 1.79 | 913 |
| 2024-09-20 22:21:35.252 | MS1 | 121.4656757086 | 31.1446219115 | 493 | 152650 | -94.37 | 5.16 | 79.94 | 0.09 | 1.59 | 982 |
| 2024-09-20 22:21:36.457 | MS1 | 121.4656677805 | 31.1446363737 | 463 | 152650 | -88.38 | 5.06 | 99.08 | 0.01 | 1.71 | 967 |
| 2024-09-20 22:21:37.458 | MS1 | 121.4656717534 | 31.1446366437 | 900 | 152650 | -93.01 | 5.89 | 63.12 | 0.08 | 1.54 | 969 |
| 2024-09-20 22:21:38.296 | MS1 | 121.4656668936 | 31.1446184042 | 55 | 152650 | -91.50 | 8.00 | 72.44 | 0.11 | 1.62 | 982 |
| 2024-09-20 22:21:39.788 | MS1 | 121.4656631581 | 31.1446263310 | 493 | 152650 | -96.51 | 4.37 | 66.40 | 0.03 | 1.63 | 902 |
| 2024-09-20 22:21:40.241 | MS1 | 121.4656721086 | 31.1446194906 | 463 | 152650 | -90.32 | 3.35 | 81.40 | 0.13 | 2.64 | 1561 |
| 2024-09-20 22:21:41.985 | MS1 | 121.4656676754 | 31.1446293133 | 900 | 152650 | -95.10 | 6.95 | 76.15 | 0.06 | 2.84 | 1599 |
| 2024-09-20 22:21:42.780 | MS1 | 121.4656777993 | 31.1446261360 | 55 | 152650 | -90.99 | 3.48 | 86.70 | 0.03 | 2.84 | 1593 |

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
| 3220551 | 10 | 121.4728169789 | 31.1449492836 | 240 | 10 | 6 | 24.9 | FDD | 654 | n1 | 152650 | 30M | 4T4R | 12 | 152650 |
| 3227242 | 1 | 121.4732008174 | 31.1459949647 | 348 | 13 | 12 | 15.6 | TDD | 673 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3238405 | 2 | 121.4665731459 | 31.1478818997 | 321 | 4 | 4 | 3.5 | TDD | 677 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3238846 | 5 | 121.4748608778 | 31.1453297438 | 306 | 3 | 4 | 1.1 | TDD | 117 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3240909 | 6 | 121.4697412093 | 31.1453361212 | 337 | 1 | 8 | 24.7 | TDD | 249 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3253956 | 12 | 121.4759769807 | 31.1507440734 | 35 | 14 | 1 | 24.6 | FDD | 948 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |
| 3256759 | 9 | 121.4749106174 | 31.1488769947 | 352 | 0 | 6 | 1.0 | FDD | 493 | n1 | 152650 | 30M | 4T4R | 27 | 152650 |
| 3258243 | 13 | 121.4702301916 | 31.1450223838 | 242 | 6 | 8 | 29.7 | FDD | 55 | n1 | 152650 | 30M | 4T4R | 21 | 152650 |
| 3261418 | 7 | 121.4758272611 | 31.1532951540 | 315 | 7 | 1 | 24.1 | FDD | 900 | n1 | 152650 | 30M | 4T4R | 20 | 152650 |
| 3264216 | 3 | 121.4650713413 | 31.1480746533 | 116 | 10 | 0 | 14.4 | TDD | 335 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3268585 | 4 | 121.4651349877 | 31.1528517380 | 197 | 1 | 7 | 13.9 | TDD | 305 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3274570 | 11 | 121.4655321483 | 31.1449330604 | 252 | 5 | 10 | 11.9 | FDD | 463 | n1 | 152650 | 30M | 4T4R | 11 | 152650 |
| 3276500 | 8 | 121.4724266357 | 31.1511372319 | 164 | 15 | 3 | 4.9 | FDD | 300 | n1 | 152650 | 30M | 4T4R | 17 | 152650 |

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
| 2024-09-20 22:21:30.937 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.960 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.073 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.073 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.815 | NREventA2 | measId:1;ServCellPCI:663;Se... |
| 2024-09-20 22:21:34.918 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.216 | NREventA5 | measId:3;ServCellPCI:663;Se... |
| 2024-09-20 22:21:35.247 | NRHandoverAttempt | SourcePCI:663;SourceNR-ARFC... |
| 2024-09-20 22:21:35.274 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.287 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:35.405 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.405 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3227242 | 1 | 7.9434 | 9.4543 | -115.9029 | 12.3777 | 190.7562 | 0.0108 | 0.0113 |
| 2024_09_20 22:00 | 3238405 | 2 | 8.2727 | 14.7199 | -117.3146 | 8.7523 | 174.4410 | 0.0187 | 0.0103 |
| 2024_09_20 22:00 | 3264216 | 3 | 11.7731 | 10.2094 | -115.7079 | 14.2374 | 153.3766 | 0.0091 | 0.0190 |
| 2024_09_20 22:00 | 3268585 | 4 | 6.7630 | 8.0254 | -115.4531 | 10.0702 | 122.7153 | 0.0189 | 0.0192 |
| 2024_09_20 22:00 | 3238846 | 5 | 9.9245 | 7.0212 | -115.2275 | 7.4664 | 197.4686 | 0.0173 | 0.0148 |
| 2024_09_20 22:00 | 3240909 | 6 | 6.2079 | 11.4585 | -117.7214 | 8.3007 | 114.9055 | 0.0007 | 0.0101 |
| 2024_09_20 22:00 | 3261418 | 7 | 12.6446 | 8.6000 | -115.8463 | 3.8132 | 24.7849 | 0.0174 | 0.0115 |
| 2024_09_20 22:00 | 3276500 | 8 | 10.1065 | 15.4418 | -117.3189 | 3.8579 | 33.4581 | 0.0174 | 0.0048 |
| 2024_09_20 22:00 | 3256759 | 9 | 8.8109 | 13.1861 | -115.1218 | 3.4451 | 35.9149 | 0.0021 | 0.0165 |
| 2024_09_20 22:00 | 3220551 | 10 | 15.3106 | 13.7851 | -116.2439 | 3.9691 | 47.8516 | 0.0039 | 0.0155 |
| 2024_09_20 22:00 | 3274570 | 11 | 19.4125 | 9.4056 | -115.2337 | 4.7138 | 56.9150 | 0.0176 | 0.0190 |
| 2024_09_20 22:00 | 3253956 | 12 | 17.2206 | 16.9797 | -115.8932 | 4.5542 | 44.5721 | 0.0075 | 0.0136 |
| 2024_09_20 22:00 | 3258243 | 13 | 14.0115 | 15.6759 | -117.7956 | 3.7483 | 39.8730 | 0.0041 | 0.0078 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413540_56BFDDEE | 152650 | 55 | -93.5 | 152650 | 654 | -101.6 | 152650 | 948 | -103.2 | 152650 | 300 |
| MR_1774413540_603266A1 | 152650 | 55 | -93.2 | 152650 | 654 | -99.1 | 152650 | 948 | -100.2 | 152650 | 300 |
| MR_1774413540_C4EB05AC | 504990 | 673 | -95.4 | 504990 | 117 | -90.3 | 504990 | 335 | -98.7 | 504990 | 677 |
| MR_1774413540_305DD210 | 504990 | 673 | -92.5 | 504990 | 117 | -91.2 | 504990 | 335 | -97.5 | 504990 | 677 |
| MR_1774413540_2DB720EE | 152650 | 55 | -95.1 | 152650 | 654 | -99.7 | 152650 | 948 | -103.7 | 152650 | 300 |
| MR_1774413540_7257F5A4 | 504990 | 673 | -93.6 | 504990 | 117 | -93.5 | 504990 | 335 | -98.6 | 504990 | 677 |

> *... 2개 열 생략 (전체 14열)*

---
