# Track A 문제 분석 — train[730]~train[739]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[730] ~ train[739] (10개)

## 목차

1. [문제 730: `dbff130b-0fb...`](#730) — single-answer, 정답: C7
2. [문제 731: `79546e8a-647...`](#731) — single-answer, 정답: C18
3. [문제 732: `d228ab47-afe...`](#732) — single-answer, 정답: C14
4. [문제 733: `3b45fe80-0c4...`](#733) — single-answer, 정답: C18
5. [문제 734: `55bd5295-8fb...`](#734) — single-answer, 정답: C15
6. [문제 735: `608ba3b9-c7e...`](#735) — single-answer, 정답: C21
7. [문제 736: `00844953-d89...`](#736) — single-answer, 정답: C2
8. [문제 737: `80b1e309-2a9...`](#737) — single-answer, 정답: C20
9. [문제 738: `7ffb1348-277...`](#738) — single-answer, 정답: C21
10. [문제 739: `e5604caf-9cf...`](#739) — single-answer, 정답: C15

---

### 문제 730: `dbff130b-0fb...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `dbff130b-0fb9-4535-a385-e45f7ad25a27` |
| Tag | **single-answer** |
| 정답 | **C7** |
| C7 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[730] topology](images/train_0730.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3211694_3
- `C2`: Decrease transmission power for 3211694_3
- `C3`: Decrease A3 Offset threshold for 3211694_3
- `C4`: Increase transmission power for 3211389_4
- `C5`: Press down the tilt angle of 3211389_4 by 10 degrees
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3211389_4
- `C7`: Check test server and transmission issues **← 정답**
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3211389_4
- `C9`: Add neighbor relationship between 3211389_4 and 3211694_3
- `C10`: Lift the tilt angle of 3211389_4 by 10 degrees
- `C11`: Add neighbor relationship between 3219973_1 and 3211694_3
- `C12`: Increase A3 Offset threshold for 3211694_3
- `C13`: Insufficient data; more data is needed for judgment.
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3211694_3
- `C15`: Adjust the azimuth of 3211389_4 by 50 degrees
- `C16`: Decrease A3 Offset threshold for 3211389_4
- `C17`: Increase A3 Offset threshold for 3211389_4
- `C18`: Lift the tilt angle  of 3211694_3 by 3 degrees
- `C19`: Decrease transmission power for 3211389_4
- `C20`: Adjust the azimuth of 3211694_3 by 15 degrees
- `C21`: Press down the tilt angle  of 3211694_3 by 3 degrees
- `C22`: Increase transmission power for 3211694_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.506 | MS1 | 121.4656691742 | 31.1446366064 | 45 | 504990 | -85.34 | 16.97 | 413.24 | 0.01 | 2.49 | 1585 |
| 2024-09-20 22:21:32.692 | MS1 | 121.4656618584 | 31.1446220123 | 45 | 504990 | -88.97 | 17.62 | 361.72 | 0.03 | 2.08 | 1596 |
| 2024-09-20 22:21:33.866 | MS1 | 121.4656701782 | 31.1446180265 | 45 | 504990 | -87.44 | 16.47 | 420.16 | 0.05 | 2.22 | 1594 |
| 2024-09-20 22:21:34.136 | MS1 | 121.4656650540 | 31.1446332220 | 45 | 504990 | -86.60 | 13.59 | 54.96 | 0.13 | 2.04 | 396 |
| 2024-09-20 22:21:35.927 | MS1 | 121.4656752126 | 31.1446303369 | 45 | 504990 | -86.09 | 16.93 | 77.24 | 0.12 | 2.48 | 440 |
| 2024-09-20 22:21:36.210 | MS1 | 121.4656699537 | 31.1446317421 | 45 | 504990 | -89.85 | 16.42 | 83.93 | 0.20 | 2.77 | 332 |
| 2024-09-20 22:21:37.285 | MS1 | 121.4656705860 | 31.1446330989 | 45 | 504990 | -91.91 | 11.05 | 55.46 | 0.04 | 2.63 | 453 |
| 2024-09-20 22:21:38.524 | MS1 | 121.4656651192 | 31.1446359971 | 45 | 504990 | -93.92 | 12.40 | 94.21 | 0.15 | 2.88 | 367 |
| 2024-09-20 22:21:39.356 | MS1 | 121.4656617750 | 31.1446300778 | 45 | 504990 | -90.34 | 7.13 | 77.60 | 0.09 | 2.76 | 354 |
| 2024-09-20 22:21:40.797 | MS1 | 121.4656693917 | 31.1446357707 | 45 | 504990 | -90.82 | 12.68 | 520.45 | 0.12 | 2.99 | 1564 |
| 2024-09-20 22:21:41.639 | MS1 | 121.4656615941 | 31.1446369308 | 45 | 504990 | -93.06 | 12.72 | 450.75 | 0.06 | 2.96 | 1589 |
| 2024-09-20 22:21:42.574 | MS1 | 121.4656636682 | 31.1446372422 | 45 | 504990 | -89.89 | 8.62 | 294.62 | 0.18 | 2.33 | 1575 |

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
| 3211389 | 4 | 121.4659287800 | 31.1541085459 | 79 | 12 | 8 | 49.0 | TDD | 45 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3211694 | 3 | 121.4709227656 | 31.1534575009 | 192 | 2 | 7 | 18.0 | TDD | 443 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3219973 | 1 | 121.4644538726 | 31.1454767355 | 29 | 9 | 6 | 37.4 | TDD | 848 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3240555 | 2 | 121.4755702713 | 31.1441236392 | 297 | 14 | 4 | 41.5 | TDD | 106 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:31.227 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.349 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.349 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.047 | NREventA3 | measId:2;ServCellPCI:105;Se... |
| 2024-09-20 22:21:38.287 | NRHandoverAttempt | SourcePCI:105;SourceNR-ARFC... |
| 2024-09-20 22:21:38.324 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.339 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.478 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.478 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3219973 | 1 | 19.0085 | 15.7145 | -116.2833 | 19.7395 | 113.0533 | 0.0161 | 0.0014 |
| 2024_09_20 22:00 | 3240555 | 2 | 7.0091 | 9.4709 | -114.3243 | 16.7113 | 194.6219 | 0.0103 | 0.0109 |
| 2024_09_20 22:00 | 3211694 | 3 | 10.6441 | 17.8190 | -117.9814 | 14.7528 | 156.5632 | 0.0029 | 0.0003 |
| 2024_09_20 22:00 | 3211389 | 4 | 16.9868 | 18.1187 | -117.1154 | 11.9146 | 164.2876 | 0.0162 | 0.0125 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416691_477BFAA9 | 504990 | 45 | -88.5 | 504990 | 443 | -91.5 | 504990 | 848 | -98.8 | 504990 | 106 |
| MR_1774416691_AD16DB03 | 504990 | 45 | -86.9 | 504990 | 443 | -91.9 | 504990 | 848 | -101.7 | 504990 | 106 |
| MR_1774416691_5F27BBE0 | 504990 | 45 | -88.3 | 504990 | 443 | -90.0 | 504990 | 848 | -99.4 | 504990 | 106 |
| MR_1774416691_7E8F507D | 504990 | 45 | -86.5 | 504990 | 443 | -88.8 | 504990 | 848 | -99.2 | 504990 | 106 |
| MR_1774416691_ACA97A94 | 504990 | 45 | -86.9 | 504990 | 443 | -88.5 | 504990 | 848 | -100.8 | 504990 | 106 |
| MR_1774416691_E12269AD | 504990 | 45 | -87.8 | 504990 | 443 | -89.8 | 504990 | 848 | -98.1 | 504990 | 106 |
| MR_1774416691_F5E2090E | 504990 | 45 | -85.5 | 504990 | 443 | -90.3 | 504990 | 848 | -99.9 | 504990 | 106 |
| MR_1774416691_E5B52764 | 504990 | 45 | -85.9 | 504990 | 443 | -91.6 | 504990 | 848 | -101.1 | 504990 | 106 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 731: `79546e8a-647...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `79546e8a-6479-4a8f-b1a6-3a08287f06cf` |
| Tag | **single-answer** |
| 정답 | **C18** |
| C18 의미 | Add neighbor relationship between 3239018_4 and 3272619_1 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[731] topology](images/train_0731.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Check test server and transmission issues
- `C2`: Adjust the azimuth of 3239018_4 by 50 degrees
- `C3`: Insufficient data; more data is needed for judgment.
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3239018_4
- `C5`: Increase transmission power for 3239018_4
- `C6`: Increase A3 Offset threshold for 3272619_1
- `C7`: Adjust the azimuth of 3272619_1 by 12 degrees
- `C8`: Lift the tilt angle of 3239018_4 by 9 degrees
- `C9`: Decrease A3 Offset threshold for 3239018_4
- `C10`: Press down the tilt angle of 3239018_4 by 9 degrees
- `C11`: Decrease transmission power for 3239018_4
- `C12`: Decrease transmission power for 3272619_1
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3272619_1
- `C14`: Increase A3 Offset threshold for 3239018_4
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3239018_4
- `C16`: Lift the tilt angle  of 3272619_1 by 2 degrees
- `C17`: Decrease A3 Offset threshold for 3272619_1
- `C18`: Add neighbor relationship between 3239018_4 and 3272619_1 **← 정답**
- `C19`: Add neighbor relationship between 3251234_2 and 3272619_1
- `C20`: Press down the tilt angle  of 3272619_1 by 2 degrees
- `C21`: Increase transmission power for 3272619_1
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3272619_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.447 | MS1 | 121.4656666607 | 31.1446315109 | 159 | 504990 | -79.19 | 13.27 | 320.38 | 0.08 | 2.70 | 1593 |
| 2024-09-20 22:21:32.845 | MS1 | 121.4656704608 | 31.1446212854 | 159 | 504990 | -84.51 | 13.29 | 392.51 | 0.13 | 2.89 | 1595 |
| 2024-09-20 22:21:33.624 | MS1 | 121.4656686152 | 31.1446289761 | 159 | 504990 | -77.80 | 16.18 | 516.01 | 0.02 | 2.68 | 1586 |
| 2024-09-20 22:21:34.335 | MS1 | 121.4656778755 | 31.1446333747 | 159 | 504990 | -88.87 | -1.26 | 51.43 | 0.04 | 1.04 | 1567 |
| 2024-09-20 22:21:35.665 | MS1 | 121.4656603720 | 31.1446345345 | 159 | 504990 | -88.36 | -1.46 | 42.18 | 0.05 | 1.16 | 1578 |
| 2024-09-20 22:21:36.544 | MS1 | 121.4656665453 | 31.1446370188 | 159 | 504990 | -86.91 | -1.04 | 56.45 | 0.13 | 1.45 | 1580 |
| 2024-09-20 22:21:37.119 | MS1 | 121.4656768884 | 31.1446208009 | 159 | 504990 | -86.87 | -2.59 | 39.01 | 0.03 | 1.07 | 1593 |
| 2024-09-20 22:21:38.833 | MS1 | 121.4656668243 | 31.1446369766 | 159 | 504990 | -77.04 | 16.60 | 471.08 | 0.03 | 1.29 | 1567 |
| 2024-09-20 22:21:39.291 | MS1 | 121.4656594248 | 31.1446272460 | 159 | 504990 | -83.22 | 17.01 | 603.73 | 0.15 | 1.10 | 1581 |
| 2024-09-20 22:21:40.976 | MS1 | 121.4656769918 | 31.1446357380 | 159 | 504990 | -82.14 | 14.38 | 366.45 | 0.12 | 2.37 | 1586 |
| 2024-09-20 22:21:41.447 | MS1 | 121.4656744601 | 31.1446213469 | 159 | 504990 | -82.71 | 15.37 | 458.94 | 0.07 | 2.11 | 1588 |
| 2024-09-20 22:21:42.912 | MS1 | 121.4656645367 | 31.1446333800 | 159 | 504990 | -84.69 | 16.95 | 359.56 | 0.18 | 2.84 | 1580 |

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
| 3231859 | 3 | 121.4753907926 | 31.1477512817 | 352 | 12 | 10 | 34.2 | TDD | 741 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3239018 | 4 | 121.4650479171 | 31.1471733301 | 322 | 3 | 10 | 32.6 | TDD | 159 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3251234 | 2 | 121.4722881038 | 31.1531796402 | 111 | 6 | 12 | 46.0 | TDD | 555 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3272619 | 1 | 121.4648800804 | 31.1548510456 | 188 | 1 | 5 | 19.2 | TDD | 466 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |

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
| 2024-09-20 22:21:31.364 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.380 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.509 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.509 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.170 | NREventA3 | measId:2;ServCellPCI:278;Se... |
| 2024-09-20 22:21:36.170 | NREventA3 | measId:2;ServCellPCI:278;Se... |
| 2024-09-20 22:21:37.170 | NREventA3 | measId:2;ServCellPCI:278;Se... |
| 2024-09-20 22:21:39.670 | NRRRCReestablishAttempt | PCI:278 |
| 2024-09-20 22:21:39.683 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.698 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:39.843 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.843 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3272619 | 1 | 5.6465 | 5.0003 | -115.0632 | 6.1200 | 163.8589 | 0.0105 | 0.0041 |
| 2024_09_20 22:00 | 3251234 | 2 | 17.4601 | 17.6378 | -116.6966 | 5.5016 | 172.1795 | 0.0102 | 0.0189 |
| 2024_09_20 22:00 | 3231859 | 3 | 11.4428 | 19.3307 | -117.2404 | 14.3954 | 147.2092 | 0.0170 | 0.0183 |
| 2024_09_20 22:00 | 3239018 | 4 | 6.6965 | 7.9654 | -115.7428 | 10.9905 | 121.9465 | 0.0027 | 0.1464 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414712_214218D1 | 504990 | 466 | -81.9 | 504990 | 159 | -87.5 | 504990 | 555 | -91.4 | 504990 | 741 |
| MR_1774414712_CB31BB7E | 504990 | 466 | -85.3 | 504990 | 159 | -89.5 | 504990 | 555 | -92.6 | 504990 | 741 |
| MR_1774414712_343DC476 | 504990 | 159 | -88.6 | 504990 | 466 | -81.9 | 504990 | 555 | -90.4 | 504990 | 741 |
| MR_1774414712_3BBEAD04 | 504990 | 466 | -83.1 | 504990 | 159 | -89.6 | 504990 | 555 | -91.2 | 504990 | 741 |
| MR_1774414712_353178A8 | 504990 | 159 | -89.2 | 504990 | 466 | -84.9 | 504990 | 555 | -92.6 | 504990 | 741 |
| MR_1774414712_BF9F2A3D | 504990 | 466 | -84.2 | 504990 | 159 | -90.2 | 504990 | 555 | -93.1 | 504990 | 741 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 732: `d228ab47-afe...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `d228ab47-afea-4732-b090-a0f441dbd431` |
| Tag | **single-answer** |
| 정답 | **C14** |
| C14 의미 | Add neighbor relationship between 3253073_2 and 3214469_4 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[732] topology](images/train_0732.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3253073_2 by 4 degrees
- `C2`: Increase A3 Offset threshold for 3253073_2
- `C3`: Adjust the azimuth of 3253073_2 by 50 degrees
- `C4`: Lift the tilt angle  of 3214469_4 by 1 degrees
- `C5`: Add neighbor relationship between 3259951_3 and 3214469_4
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3253073_2
- `C7`: Press down the tilt angle of 3253073_2 by 4 degrees
- `C8`: Decrease A3 Offset threshold for 3253073_2
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3253073_2
- `C10`: Check test server and transmission issues
- `C11`: Decrease A3 Offset threshold for 3214469_4
- `C12`: Adjust the azimuth of 3214469_4 by 7 degrees
- `C13`: Increase A3 Offset threshold for 3214469_4
- `C14`: Add neighbor relationship between 3253073_2 and 3214469_4 **← 정답**
- `C15`: Increase transmission power for 3214469_4
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3214469_4
- `C17`: Insufficient data; more data is needed for judgment.
- `C18`: Decrease transmission power for 3214469_4
- `C19`: Press down the tilt angle  of 3214469_4 by 1 degrees
- `C20`: Increase transmission power for 3253073_2
- `C21`: Decrease transmission power for 3253073_2
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3214469_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.269 | MS1 | 121.4656663490 | 31.1446183652 | 27 | 504990 | -82.92 | 17.15 | 415.68 | 0.17 | 2.63 | 1572 |
| 2024-09-20 22:21:32.421 | MS1 | 121.4656614304 | 31.1446226867 | 27 | 504990 | -77.47 | 14.39 | 317.90 | 0.07 | 2.88 | 1585 |
| 2024-09-20 22:21:33.469 | MS1 | 121.4656599755 | 31.1446354552 | 27 | 504990 | -82.58 | 16.65 | 480.37 | 0.02 | 2.82 | 1576 |
| 2024-09-20 22:21:34.529 | MS1 | 121.4656723849 | 31.1446187591 | 27 | 504990 | -86.51 | -1.01 | 59.64 | 0.04 | 1.11 | 1596 |
| 2024-09-20 22:21:35.781 | MS1 | 121.4656673280 | 31.1446323458 | 27 | 504990 | -88.92 | -1.77 | 61.45 | 0.06 | 1.27 | 1566 |
| 2024-09-20 22:21:36.514 | MS1 | 121.4656677557 | 31.1446265318 | 27 | 504990 | -87.72 | -3.74 | 39.61 | 0.06 | 1.20 | 1578 |
| 2024-09-20 22:21:37.265 | MS1 | 121.4656688672 | 31.1446238311 | 27 | 504990 | -90.82 | -2.86 | 54.33 | 0.15 | 1.49 | 1593 |
| 2024-09-20 22:21:38.538 | MS1 | 121.4656631214 | 31.1446307568 | 27 | 504990 | -77.38 | 16.07 | 593.71 | 0.04 | 1.20 | 1588 |
| 2024-09-20 22:21:39.786 | MS1 | 121.4656659158 | 31.1446248775 | 27 | 504990 | -80.10 | 16.52 | 409.63 | 0.02 | 1.35 | 1600 |
| 2024-09-20 22:21:40.550 | MS1 | 121.4656736043 | 31.1446297169 | 27 | 504990 | -80.22 | 16.62 | 604.46 | 0.11 | 2.88 | 1565 |
| 2024-09-20 22:21:41.861 | MS1 | 121.4656640981 | 31.1446298785 | 27 | 504990 | -78.74 | 13.81 | 413.04 | 0.13 | 2.82 | 1576 |
| 2024-09-20 22:21:42.883 | MS1 | 121.4656748015 | 31.1446346487 | 27 | 504990 | -84.84 | 15.65 | 422.17 | 0.17 | 2.33 | 1567 |

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
| 3214469 | 4 | 121.4733427612 | 31.1441502733 | 281 | 0 | 8 | 15.3 | TDD | 606 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3253073 | 2 | 121.4720449638 | 31.1481406687 | 354 | 2 | 8 | 25.7 | TDD | 27 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3259951 | 3 | 121.4732962812 | 31.1515571036 | 251 | 6 | 11 | 45.3 | TDD | 163 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3266261 | 1 | 121.4685072382 | 31.1528470719 | 354 | 0 | 5 | 24.4 | TDD | 97 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |

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
| 2024-09-20 22:21:31.339 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.358 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.490 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.490 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.225 | NREventA3 | measId:2;ServCellPCI:185;Se... |
| 2024-09-20 22:21:36.225 | NREventA3 | measId:2;ServCellPCI:185;Se... |
| 2024-09-20 22:21:37.225 | NREventA3 | measId:2;ServCellPCI:185;Se... |
| 2024-09-20 22:21:39.725 | NRRRCReestablishAttempt | PCI:185 |
| 2024-09-20 22:21:39.738 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.752 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:39.873 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.873 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3266261 | 1 | 5.0140 | 10.9180 | -115.8686 | 13.5582 | 115.6382 | 0.0159 | 0.0006 |
| 2024_09_20 22:00 | 3253073 | 2 | 18.1659 | 5.8712 | -115.8199 | 19.8274 | 174.0358 | 0.0194 | 0.1287 |
| 2024_09_20 22:00 | 3259951 | 3 | 15.5861 | 19.3970 | -116.6146 | 16.9395 | 142.6848 | 0.0092 | 0.0049 |
| 2024_09_20 22:00 | 3214469 | 4 | 8.7266 | 12.8167 | -117.6022 | 7.8455 | 120.6076 | 0.0056 | 0.0132 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414804_9B685CD1 | 504990 | 27 | -86.0 | 504990 | 606 | -81.5 | 504990 | 163 | -82.5 | 504990 | 97 |
| MR_1774414804_B96F1DEF | 504990 | 27 | -86.4 | 504990 | 606 | -81.5 | 504990 | 163 | -85.9 | 504990 | 97 |
| MR_1774414804_0B1BF6C6 | 504990 | 27 | -85.8 | 504990 | 606 | -81.4 | 504990 | 163 | -82.5 | 504990 | 97 |
| MR_1774414804_24A70875 | 504990 | 606 | -79.2 | 504990 | 27 | -87.2 | 504990 | 163 | -82.4 | 504990 | 97 |
| MR_1774414804_01827F10 | 504990 | 606 | -81.4 | 504990 | 27 | -85.1 | 504990 | 163 | -83.5 | 504990 | 97 |
| MR_1774414804_7E21DC62 | 504990 | 27 | -87.1 | 504990 | 606 | -79.8 | 504990 | 163 | -85.8 | 504990 | 97 |
| MR_1774414804_D5B4B0F3 | 504990 | 27 | -87.2 | 504990 | 606 | -81.8 | 504990 | 163 | -85.2 | 504990 | 97 |
| MR_1774414804_C23197F4 | 504990 | 27 | -86.8 | 504990 | 606 | -82.2 | 504990 | 163 | -84.8 | 504990 | 97 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 733: `3b45fe80-0c4...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `3b45fe80-0c4e-4f99-a895-20bd2acb983c` |
| Tag | **single-answer** |
| 정답 | **C18** |
| C18 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[733] topology](images/train_0733.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3227216_2
- `C2`: Add neighbor relationship between 3234791_1 and 3227216_2
- `C3`: Press down the tilt angle  of 3227216_2 by 4 degrees
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3252695_3
- `C5`: Increase transmission power for 3252695_3
- `C6`: Adjust the azimuth of 3227216_2 by 36 degrees
- `C7`: Lift the tilt angle of 3252695_3 by 7 degrees
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3252695_3
- `C9`: Lift the tilt angle  of 3227216_2 by 4 degrees
- `C10`: Increase A3 Offset threshold for 3227216_2
- `C11`: Increase transmission power for 3227216_2
- `C12`: Adjust the azimuth of 3252695_3 by 50 degrees
- `C13`: Decrease transmission power for 3252695_3
- `C14`: Decrease A3 Offset threshold for 3252695_3
- `C15`: Add neighbor relationship between 3252695_3 and 3227216_2
- `C16`: Decrease A3 Offset threshold for 3227216_2
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3227216_2
- `C18`: Insufficient data; more data is needed for judgment. **← 정답**
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3227216_2
- `C20`: Press down the tilt angle of 3252695_3 by 7 degrees
- `C21`: Check test server and transmission issues
- `C22`: Increase A3 Offset threshold for 3252695_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.797 | MS1 | 121.4656624706 | 31.1446346541 | 212 | 504990 | -89.36 | 17.26 | 387.28 | 0.17 | 2.72 | 1593 |
| 2024-09-20 22:21:32.861 | MS1 | 121.4656752977 | 31.1446254414 | 212 | 504990 | -85.70 | 16.28 | 376.53 | 0.19 | 2.36 | 1589 |
| 2024-09-20 22:21:33.728 | MS1 | 121.4656716646 | 31.1446232511 | 212 | 504990 | -91.16 | 17.44 | 354.21 | 0.14 | 2.04 | 1579 |
| 2024-09-20 22:21:34.752 | MS1 | 121.4656757053 | 31.1446284985 | 212 | 504990 | -91.68 | 14.87 | 88.02 | 0.17 | 2.56 | 1560 |
| 2024-09-20 22:21:35.263 | MS1 | 121.4656668948 | 31.1446234041 | 212 | 504990 | -90.29 | 13.93 | 62.11 | 0.10 | 2.75 | 1591 |
| 2024-09-20 22:21:36.737 | MS1 | 121.4656624350 | 31.1446305236 | 212 | 504990 | -90.19 | 13.04 | 72.34 | 0.10 | 2.30 | 1564 |
| 2024-09-20 22:21:37.568 | MS1 | 121.4656743660 | 31.1446338477 | 212 | 504990 | -91.88 | 9.16 | 49.54 | 0.19 | 2.20 | 1589 |
| 2024-09-20 22:21:38.762 | MS1 | 121.4656607409 | 31.1446333733 | 212 | 504990 | -93.25 | 7.97 | 90.76 | 0.07 | 2.55 | 1596 |
| 2024-09-20 22:21:39.773 | MS1 | 121.4656602477 | 31.1446244111 | 212 | 504990 | -90.58 | 11.09 | 71.09 | 0.05 | 2.05 | 1578 |
| 2024-09-20 22:21:40.151 | MS1 | 121.4656596031 | 31.1446209468 | 212 | 504990 | -90.55 | 7.62 | 529.39 | 0.13 | 2.46 | 1578 |
| 2024-09-20 22:21:41.410 | MS1 | 121.4656675470 | 31.1446283163 | 212 | 504990 | -91.04 | 10.40 | 481.09 | 0.16 | 2.81 | 1597 |
| 2024-09-20 22:21:42.968 | MS1 | 121.4656667074 | 31.1446286210 | 212 | 504990 | -90.66 | 12.11 | 588.35 | 0.10 | 2.85 | 1592 |

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
| 3227216 | 2 | 121.4759190281 | 31.1540295378 | 259 | 2 | 0 | 43.1 | TDD | 738 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3234791 | 1 | 121.4718760743 | 31.1475274062 | 341 | 11 | 12 | 43.3 | TDD | 264 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3246514 | 4 | 121.4729129038 | 31.1544192787 | 249 | 1 | 5 | 26.5 | TDD | 725 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3252695 | 3 | 121.4687452606 | 31.1469719604 | 29 | 5 | 0 | 16.7 | TDD | 212 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |

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
| 2024-09-20 22:21:30.844 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.860 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:30.973 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.973 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.708 | NREventA3 | measId:2;ServCellPCI:670;Se... |
| 2024-09-20 22:21:37.948 | NRHandoverAttempt | SourcePCI:670;SourceNR-ARFC... |
| 2024-09-20 22:21:37.990 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.000 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.116 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.116 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3234791 | 1 | 77.0437 | 78.4066 | -115.6007 | 8.6265 | 191.0057 | 0.0021 | 0.0093 |
| 2024_09_19 22:00 | 3227216 | 2 | 82.9431 | 88.4314 | -114.6931 | 6.0257 | 88.2801 | 0.0007 | 0.0144 |
| 2024_09_19 22:00 | 3252695 | 3 | 83.4350 | 77.5785 | -115.1385 | 9.3342 | 151.1440 | 0.0101 | 0.0136 |
| 2024_09_19 22:00 | 3246514 | 4 | 92.7649 | 80.0333 | -114.7048 | 9.6685 | 123.7949 | 0.0195 | 0.0095 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414344_CFC522FB | 504990 | 212 | -90.7 | 504990 | 738 | -97.8 | 504990 | 264 | -105.4 | 504990 | 725 |
| MR_1774414344_5708142D | 504990 | 212 | -90.6 | 504990 | 738 | -99.5 | 504990 | 264 | -103.5 | 504990 | 725 |
| MR_1774414344_7D373745 | 504990 | 212 | -91.3 | 504990 | 738 | -99.0 | 504990 | 264 | -105.5 | 504990 | 725 |
| MR_1774414344_E4572E6F | 504990 | 212 | -90.9 | 504990 | 738 | -98.9 | 504990 | 264 | -105.0 | 504990 | 725 |
| MR_1774414344_F200AA2E | 504990 | 212 | -90.0 | 504990 | 738 | -101.0 | 504990 | 264 | -104.4 | 504990 | 725 |
| MR_1774414344_168507F1 | 504990 | 212 | -93.5 | 504990 | 738 | -98.2 | 504990 | 264 | -105.1 | 504990 | 725 |
| MR_1774414344_A4A840DF | 504990 | 212 | -90.3 | 504990 | 738 | -101.3 | 504990 | 264 | -106.2 | 504990 | 725 |
| MR_1774414344_77DB4FC3 | 504990 | 212 | -91.4 | 504990 | 738 | -98.8 | 504990 | 264 | -105.3 | 504990 | 725 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 734: `55bd5295-8fb...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `55bd5295-8fb1-476b-9f81-4f8e7289cbc9` |
| Tag | **single-answer** |
| 정답 | **C15** |
| C15 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3259298_3 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[734] topology](images/train_0734.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3279614_2
- `C2`: Lift the tilt angle  of 3279614_2 by 3 degrees
- `C3`: Decrease transmission power for 3259298_3
- `C4`: Increase A3 Offset threshold for 3259298_3
- `C5`: Press down the tilt angle of 3259298_3 by 4 degrees
- `C6`: Adjust the azimuth of 3279614_2 by 27 degrees
- `C7`: Increase transmission power for 3259298_3
- `C8`: Decrease transmission power for 3279614_2
- `C9`: Decrease A3 Offset threshold for 3259298_3
- `C10`: Check test server and transmission issues
- `C11`: Insufficient data; more data is needed for judgment.
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3259298_3
- `C13`: Increase A3 Offset threshold for 3279614_2
- `C14`: Add neighbor relationship between 3275213_7 and 3279614_2
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3259298_3 **← 정답**
- `C16`: Lift the tilt angle of 3259298_3 by 4 degrees
- `C17`: Add neighbor relationship between 3259298_3 and 3279614_2
- `C18`: Increase transmission power for 3279614_2
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3279614_2
- `C20`: Adjust the azimuth of 3259298_3 by 40 degrees
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3279614_2
- `C22`: Press down the tilt angle  of 3279614_2 by 3 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.966 | MS1 | 121.4656740954 | 31.1446220294 | 308 | 504990 | -94.51 | 9.48 | 553.58 | 0.00 | 2.81 | 1595 |
| 2024-09-20 22:21:32.837 | MS1 | 121.4656609769 | 31.1446360858 | 917 | 504990 | -94.54 | 9.10 | 383.43 | 0.19 | 2.47 | 1589 |
| 2024-09-20 22:21:33.774 | MS1 | 121.4656619039 | 31.1446237010 | 90 | 504990 | -93.95 | 9.05 | 591.03 | 0.04 | 2.23 | 1581 |
| 2024-09-20 22:21:34.723 | MS1 | 121.4656669599 | 31.1446196844 | 244 | 152650 | -92.37 | 6.79 | 70.71 | 0.02 | 1.73 | 961 |
| 2024-09-20 22:21:35.477 | MS1 | 121.4656695937 | 31.1446230547 | 406 | 152650 | -87.72 | 7.65 | 73.18 | 0.19 | 1.99 | 964 |
| 2024-09-20 22:21:36.948 | MS1 | 121.4656731657 | 31.1446367074 | 770 | 152650 | -91.02 | 6.57 | 64.05 | 0.19 | 1.96 | 969 |
| 2024-09-20 22:21:37.775 | MS1 | 121.4656705938 | 31.1446191963 | 948 | 152650 | -94.85 | 7.09 | 77.36 | 0.12 | 1.78 | 988 |
| 2024-09-20 22:21:38.976 | MS1 | 121.4656727332 | 31.1446286325 | 244 | 152650 | -90.13 | 2.51 | 66.12 | 0.01 | 1.79 | 988 |
| 2024-09-20 22:21:39.700 | MS1 | 121.4656666206 | 31.1446223150 | 406 | 152650 | -96.17 | 4.41 | 62.52 | 0.01 | 1.94 | 991 |
| 2024-09-20 22:21:40.969 | MS1 | 121.4656651024 | 31.1446191604 | 770 | 152650 | -95.30 | 3.13 | 84.41 | 0.00 | 2.26 | 1573 |
| 2024-09-20 22:21:41.892 | MS1 | 121.4656697333 | 31.1446268774 | 948 | 152650 | -87.47 | 5.54 | 75.48 | 0.10 | 2.59 | 1599 |
| 2024-09-20 22:21:42.336 | MS1 | 121.4656721556 | 31.1446253140 | 244 | 152650 | -87.48 | 3.90 | 94.51 | 0.03 | 2.40 | 1560 |

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
| 3216315 | 9 | 121.4671734763 | 31.1495415217 | 324 | 3 | 9 | 9.4 | FDD | 330 | n1 | 152650 | 30M | 4T4R | 23 | 152650 |
| 3226911 | 12 | 121.4717510059 | 31.1485800917 | 238 | 10 | 12 | 3.4 | FDD | 406 | n1 | 152650 | 30M | 4T4R | 11 | 152650 |
| 3238282 | 10 | 121.4699825607 | 31.1460492426 | 145 | 3 | 4 | 11.6 | FDD | 948 | n1 | 152650 | 30M | 4T4R | 21 | 152650 |
| 3238362 | 6 | 121.4658637876 | 31.1531972936 | 289 | 6 | 3 | 17.8 | TDD | 156 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3251533 | 5 | 121.4655416248 | 31.1521018840 | 8 | 9 | 2 | 2.8 | TDD | 90 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3251874 | 4 | 121.4667660312 | 31.1444414867 | 279 | 2 | 6 | 25.5 | TDD | 917 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3254237 | 11 | 121.4693592944 | 31.1455035391 | 193 | 4 | 2 | 27.4 | FDD | 244 | n1 | 152650 | 30M | 4T4R | 23 | 152650 |
| 3259221 | 1 | 121.4703812880 | 31.1539937035 | 324 | 8 | 5 | 25.5 | TDD | 872 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3259298 | 3 | 121.4717741950 | 31.1450001258 | 226 | 1 | 8 | 27.3 | TDD | 308 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3273718 | 13 | 121.4688694308 | 31.1442417257 | 132 | 4 | 10 | 0.0 | FDD | 153 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |
| 3275213 | 7 | 121.4708681142 | 31.1472509147 | 44 | 0 | 8 | 16.7 | FDD | 770 | n1 | 152650 | 30M | 4T4R | 22 | 152650 |
| 3277779 | 8 | 121.4702154633 | 31.1550256694 | 262 | 1 | 7 | 3.4 | FDD | 739 | n1 | 152650 | 30M | 4T4R | 12 | 152650 |
| 3279614 | 2 | 121.4693815235 | 31.1444874709 | 245 | 3 | 6 | 0.7 | TDD | 592 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |

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
| 2024-09-20 22:21:31.519 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.542 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.647 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.647 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.320 | NREventA2 | measId:1;ServCellPCI:225;Se... |
| 2024-09-20 22:21:35.443 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.723 | NREventA5 | measId:3;ServCellPCI:225;Se... |
| 2024-09-20 22:21:35.781 | NRHandoverAttempt | SourcePCI:225;SourceNR-ARFC... |
| 2024-09-20 22:21:35.802 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.817 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:35.934 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.934 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3259221 | 1 | 7.8628 | 17.9110 | -117.8594 | 12.0660 | 117.5966 | 0.0148 | 0.0131 |
| 2024_09_20 22:00 | 3279614 | 2 | 14.1960 | 19.7890 | -114.6826 | 16.8678 | 92.3684 | 0.0053 | 0.0152 |
| 2024_09_20 22:00 | 3259298 | 3 | 13.6684 | 14.4819 | -115.6391 | 13.0375 | 97.5392 | 0.0140 | 0.0112 |
| 2024_09_20 22:00 | 3251874 | 4 | 7.0090 | 5.9095 | -117.2291 | 11.7630 | 99.9996 | 0.0148 | 0.0006 |
| 2024_09_20 22:00 | 3251533 | 5 | 9.4919 | 17.9019 | -116.8939 | 17.9052 | 149.9549 | 0.0057 | 0.0175 |
| 2024_09_20 22:00 | 3238362 | 6 | 9.7136 | 5.5190 | -117.3958 | 14.4231 | 94.5382 | 0.0064 | 0.0028 |
| 2024_09_20 22:00 | 3275213 | 7 | 19.9996 | 18.4124 | -117.1200 | 4.0136 | 36.7789 | 0.0176 | 0.0139 |
| 2024_09_20 22:00 | 3277779 | 8 | 14.7458 | 10.8735 | -117.4046 | 3.9898 | 48.2590 | 0.0035 | 0.0037 |
| 2024_09_20 22:00 | 3216315 | 9 | 15.9868 | 13.9668 | -116.2104 | 3.8783 | 24.7116 | 0.0108 | 0.0091 |
| 2024_09_20 22:00 | 3238282 | 10 | 17.9634 | 13.2767 | -114.0999 | 4.5298 | 51.2168 | 0.0125 | 0.0031 |
| 2024_09_20 22:00 | 3254237 | 11 | 6.1860 | 19.1263 | -117.0684 | 4.8857 | 44.4779 | 0.0160 | 0.0064 |
| 2024_09_20 22:00 | 3226911 | 12 | 15.0258 | 11.9387 | -116.9031 | 3.5974 | 21.1595 | 0.0063 | 0.0044 |
| 2024_09_20 22:00 | 3273718 | 13 | 13.0293 | 9.8244 | -116.1135 | 4.6521 | 31.9272 | 0.0010 | 0.0016 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412265_470B7419 | 504990 | 90 | -95.7 | 504990 | 592 | -93.0 | 504990 | 872 | -95.9 | 504990 | 156 |
| MR_1774412265_EA8EAF63 | 504990 | 90 | -94.1 | 504990 | 592 | -92.1 | 504990 | 872 | -95.4 | 504990 | 156 |
| MR_1774412265_025A8DE8 | 152650 | 244 | -93.7 | 152650 | 153 | -95.5 | 152650 | 739 | -98.7 | 152650 | 330 |
| MR_1774412265_05C645D9 | 504990 | 90 | -94.5 | 504990 | 592 | -91.8 | 504990 | 872 | -98.9 | 504990 | 156 |
| MR_1774412265_48571D28 | 152650 | 244 | -93.4 | 152650 | 153 | -96.2 | 152650 | 739 | -99.0 | 152650 | 330 |
| MR_1774412265_61888F09 | 504990 | 90 | -92.4 | 504990 | 592 | -92.0 | 504990 | 872 | -95.9 | 504990 | 156 |
| MR_1774412265_A4606AE4 | 504990 | 90 | -92.7 | 504990 | 592 | -94.4 | 504990 | 872 | -98.5 | 504990 | 156 |
| MR_1774412265_A7DC2F27 | 152650 | 244 | -91.0 | 152650 | 153 | -98.8 | 152650 | 739 | -98.5 | 152650 | 330 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 735: `608ba3b9-c7e...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `608ba3b9-c7e1-4e5e-992e-435e4ab77804` |
| Tag | **single-answer** |
| 정답 | **C21** |
| C21 의미 | Lift the tilt angle  of 3276987_2 by 7 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[735] topology](images/train_0735.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3276987_2 by 50 degrees
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3223426_4
- `C3`: Check test server and transmission issues
- `C4`: Press down the tilt angle of 3239384_3 by 6 degrees
- `C5`: Decrease A3 Offset threshold for 3223426_4
- `C6`: Insufficient data; more data is needed for judgment.
- `C7`: Decrease A3 Offset threshold for 3239384_3
- `C8`: Adjust the azimuth of 3239384_3 by 37 degrees
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3223426_4
- `C10`: Increase transmission power for 3223426_4
- `C11`: Press down the tilt angle  of 3276987_2 by 7 degrees
- `C12`: Decrease transmission power for 3239384_3
- `C13`: Increase A3 Offset threshold for 3223426_4
- `C14`: Lift the tilt angle of 3239384_3 by 6 degrees
- `C15`: Increase A3 Offset threshold for 3239384_3
- `C16`: Add neighbor relationship between 3239384_3 and 3223426_4
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3239384_3
- `C18`: Increase transmission power for 3239384_3
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3239384_3
- `C20`: Add neighbor relationship between 3276987_2 and 3223426_4
- `C21`: Lift the tilt angle  of 3276987_2 by 7 degrees **← 정답**
- `C22`: Decrease transmission power for 3223426_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.409 | MS1 | 121.4656704148 | 31.1446193295 | 30 | 504990 | -89.62 | 17.72 | 551.92 | 0.04 | 2.78 | 1585 |
| 2024-09-20 22:21:32.415 | MS1 | 121.4656591977 | 31.1446316399 | 30 | 504990 | -89.36 | 17.44 | 395.17 | 0.12 | 2.34 | 1599 |
| 2024-09-20 22:21:33.167 | MS1 | 121.4656706790 | 31.1446188514 | 30 | 504990 | -88.07 | 13.99 | 466.98 | 0.19 | 2.91 | 1586 |
| 2024-09-20 22:21:34.838 | MS1 | 121.4656624534 | 31.1446215073 | 30 | 504990 | -89.66 | 14.72 | 80.59 | 0.03 | 2.83 | 1581 |
| 2024-09-20 22:21:35.535 | MS1 | 121.4656621370 | 31.1446227673 | 30 | 504990 | -89.30 | 14.29 | 56.17 | 0.06 | 2.48 | 1562 |
| 2024-09-20 22:21:36.447 | MS1 | 121.4656653440 | 31.1446276651 | 30 | 504990 | -85.68 | 16.96 | 79.35 | 0.10 | 2.58 | 1569 |
| 2024-09-20 22:21:37.364 | MS1 | 121.4656596649 | 31.1446283195 | 30 | 504990 | -93.59 | 11.40 | 91.31 | 0.17 | 2.02 | 1594 |
| 2024-09-20 22:21:38.396 | MS1 | 121.4656698037 | 31.1446321320 | 30 | 504990 | -89.64 | 8.48 | 71.59 | 0.07 | 2.52 | 1597 |
| 2024-09-20 22:21:39.745 | MS1 | 121.4656695704 | 31.1446308948 | 30 | 504990 | -92.99 | 12.65 | 56.81 | 0.14 | 2.88 | 1584 |
| 2024-09-20 22:21:40.387 | MS1 | 121.4656679404 | 31.1446347050 | 30 | 504990 | -90.47 | 11.46 | 320.34 | 0.01 | 2.41 | 1586 |
| 2024-09-20 22:21:41.618 | MS1 | 121.4656716698 | 31.1446261495 | 30 | 504990 | -89.82 | 10.70 | 426.76 | 0.18 | 2.92 | 1563 |
| 2024-09-20 22:21:42.725 | MS1 | 121.4656627842 | 31.1446232859 | 30 | 504990 | -89.61 | 9.26 | 549.01 | 0.09 | 2.52 | 1597 |

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
| 3223426 | 4 | 121.4653304348 | 31.1486142894 | 238 | 2 | 7 | 41.5 | TDD | 919 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3223772 | 1 | 121.4694728763 | 31.1509610635 | 171 | 7 | 5 | 38.9 | TDD | 840 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3239384 | 3 | 121.4685608022 | 31.1542146578 | 158 | 5 | 8 | 16.7 | TDD | 30 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3276987 | 2 | 121.4645362577 | 31.1447909016 | 11 | 11 | 7 | 48.5 | TDD | 739 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |

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
| 2024-09-20 22:21:31.674 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.690 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.824 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.824 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.493 | NREventA3 | measId:2;ServCellPCI:463;Se... |
| 2024-09-20 22:21:38.733 | NRHandoverAttempt | SourcePCI:463;SourceNR-ARFC... |
| 2024-09-20 22:21:38.768 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.781 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.892 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.892 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3223772 | 1 | 11.6682 | 14.2251 | -114.4117 | 6.6945 | 150.9631 | 0.0061 | 0.0031 |
| 2024_09_20 22:00 | 3276987 | 2 | 19.4875 | 14.6136 | -115.0364 | 16.5793 | 116.3201 | 0.0111 | 0.0105 |
| 2024_09_20 22:00 | 3239384 | 3 | 90.4146 | 87.4681 | -116.6092 | 9.6145 | 120.3251 | 0.0064 | 0.0057 |
| 2024_09_20 22:00 | 3223426 | 4 | 9.9438 | 11.2465 | -117.0372 | 19.2847 | 165.7171 | 0.0028 | 0.0188 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413722_9B21F7B0 | 504990 | 30 | -91.2 | 504990 | 919 | -94.6 | 504990 | 739 | -101.7 | 504990 | 840 |
| MR_1774413722_6B4CABF7 | 504990 | 30 | -88.3 | 504990 | 919 | -96.1 | 504990 | 739 | -100.1 | 504990 | 840 |
| MR_1774413722_14D0E633 | 504990 | 30 | -90.0 | 504990 | 919 | -94.6 | 504990 | 739 | -101.6 | 504990 | 840 |
| MR_1774413722_7EF47261 | 504990 | 30 | -91.4 | 504990 | 919 | -96.3 | 504990 | 739 | -102.8 | 504990 | 840 |
| MR_1774413722_DCF3A908 | 504990 | 30 | -90.0 | 504990 | 919 | -94.4 | 504990 | 739 | -100.9 | 504990 | 840 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 736: `00844953-d89...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `00844953-d89c-4eb4-8f48-f535ecf95e33` |
| Tag | **single-answer** |
| 정답 | **C2** |
| C2 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3236170_4 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[736] topology](images/train_0736.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Check test server and transmission issues
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3236170_4 **← 정답**
- `C3`: Insufficient data; more data is needed for judgment.
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3236170_4
- `C5`: Increase transmission power for 3218309_5
- `C6`: Adjust the azimuth of 3236170_4 by 29 degrees
- `C7`: Increase A3 Offset threshold for 3236170_4
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3218309_5
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3218309_5
- `C10`: Lift the tilt angle of 3236170_4 by 2 degrees
- `C11`: Adjust the azimuth of 3218309_5 by 4 degrees
- `C12`: Add neighbor relationship between 3236170_4 and 3218309_5
- `C13`: Lift the tilt angle  of 3218309_5 by 2 degrees
- `C14`: Decrease A3 Offset threshold for 3218309_5
- `C15`: Decrease A3 Offset threshold for 3236170_4
- `C16`: Press down the tilt angle  of 3218309_5 by 2 degrees
- `C17`: Decrease transmission power for 3236170_4
- `C18`: Increase A3 Offset threshold for 3218309_5
- `C19`: Decrease transmission power for 3218309_5
- `C20`: Add neighbor relationship between 3272366_7 and 3218309_5
- `C21`: Increase transmission power for 3236170_4
- `C22`: Press down the tilt angle of 3236170_4 by 2 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.179 | MS1 | 121.4656725376 | 31.1446330309 | 977 | 504990 | -94.61 | 12.49 | 570.78 | 0.15 | 2.85 | 1582 |
| 2024-09-20 22:21:32.614 | MS1 | 121.4656604704 | 31.1446303320 | 259 | 504990 | -94.28 | 10.09 | 556.39 | 0.10 | 2.89 | 1570 |
| 2024-09-20 22:21:33.512 | MS1 | 121.4656727895 | 31.1446201098 | 776 | 504990 | -93.71 | 14.25 | 525.74 | 0.02 | 2.85 | 1580 |
| 2024-09-20 22:21:34.658 | MS1 | 121.4656697520 | 31.1446281438 | 877 | 152650 | -96.64 | 7.38 | 71.85 | 0.19 | 1.55 | 996 |
| 2024-09-20 22:21:35.490 | MS1 | 121.4656667810 | 31.1446200922 | 792 | 152650 | -92.70 | 2.85 | 51.61 | 0.19 | 1.55 | 980 |
| 2024-09-20 22:21:36.879 | MS1 | 121.4656631947 | 31.1446357653 | 160 | 152650 | -88.74 | 4.65 | 80.09 | 0.11 | 1.55 | 939 |
| 2024-09-20 22:21:37.611 | MS1 | 121.4656651711 | 31.1446361710 | 948 | 152650 | -92.41 | 5.60 | 61.36 | 0.05 | 1.93 | 950 |
| 2024-09-20 22:21:38.686 | MS1 | 121.4656693679 | 31.1446268627 | 877 | 152650 | -93.70 | 4.79 | 94.27 | 0.11 | 1.94 | 966 |
| 2024-09-20 22:21:39.581 | MS1 | 121.4656651286 | 31.1446300718 | 792 | 152650 | -96.08 | 6.40 | 81.53 | 0.08 | 1.68 | 990 |
| 2024-09-20 22:21:40.533 | MS1 | 121.4656661757 | 31.1446185402 | 160 | 152650 | -90.71 | 6.20 | 59.73 | 0.15 | 2.75 | 1565 |
| 2024-09-20 22:21:41.796 | MS1 | 121.4656675772 | 31.1446350062 | 948 | 152650 | -89.38 | 5.33 | 79.45 | 0.16 | 2.47 | 1593 |
| 2024-09-20 22:21:42.778 | MS1 | 121.4656655130 | 31.1446208263 | 877 | 152650 | -87.24 | 7.97 | 59.02 | 0.11 | 2.03 | 1568 |

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
| 3218309 | 5 | 121.4687990120 | 31.1540653044 | 200 | 1 | 4 | 12.1 | TDD | 253 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3221730 | 2 | 121.4722085647 | 31.1441482430 | 108 | 15 | 8 | 13.5 | TDD | 776 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3235085 | 6 | 121.4663192783 | 31.1531276385 | 44 | 1 | 9 | 22.4 | TDD | 159 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3236170 | 4 | 121.4681377575 | 31.1493950028 | 233 | 1 | 7 | 7.2 | TDD | 977 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3247367 | 13 | 121.4700541855 | 31.1505893467 | 208 | 10 | 10 | 16.0 | FDD | 95 | n1 | 152650 | 30M | 4T4R | 15 | 152650 |
| 3253180 | 1 | 121.4673763071 | 31.1467139064 | 16 | 11 | 5 | 13.4 | TDD | 259 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3268317 | 8 | 121.4708561076 | 31.1463745096 | 274 | 13 | 4 | 3.8 | FDD | 712 | n1 | 152650 | 30M | 4T4R | 26 | 152650 |
| 3272340 | 12 | 121.4715645208 | 31.1450572718 | 202 | 15 | 11 | 12.1 | FDD | 792 | n1 | 152650 | 30M | 4T4R | 18 | 152650 |
| 3272366 | 7 | 121.4697964127 | 31.1504823813 | 156 | 13 | 8 | 14.6 | FDD | 160 | n1 | 152650 | 30M | 4T4R | 10 | 152650 |
| 3275465 | 3 | 121.4711880311 | 31.1537474692 | 249 | 11 | 2 | 20.8 | TDD | 749 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3275610 | 11 | 121.4640150432 | 31.1530590215 | 169 | 7 | 5 | 26.2 | FDD | 948 | n1 | 152650 | 30M | 4T4R | 20 | 152650 |
| 3276480 | 10 | 121.4721433766 | 31.1442346134 | 188 | 8 | 10 | 2.8 | FDD | 877 | n1 | 152650 | 30M | 4T4R | 12 | 152650 |
| 3278695 | 9 | 121.4683824849 | 31.1503810892 | 293 | 5 | 3 | 16.7 | FDD | 393 | n1 | 152650 | 30M | 4T4R | 11 | 152650 |

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
| 2024-09-20 22:21:31.132 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.262 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.262 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.962 | NREventA2 | measId:1;ServCellPCI:442;Se... |
| 2024-09-20 22:21:35.093 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.336 | NREventA5 | measId:3;ServCellPCI:442;Se... |
| 2024-09-20 22:21:35.376 | NRHandoverAttempt | SourcePCI:442;SourceNR-ARFC... |
| 2024-09-20 22:21:35.405 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.420 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:35.557 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.557 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3253180 | 1 | 12.0940 | 11.9902 | -117.4670 | 12.1825 | 139.8141 | 0.0095 | 0.0082 |
| 2024_09_20 22:00 | 3221730 | 2 | 8.8548 | 10.7425 | -115.0601 | 6.2420 | 103.6950 | 0.0077 | 0.0149 |
| 2024_09_20 22:00 | 3275465 | 3 | 17.4196 | 11.0067 | -115.9124 | 5.4241 | 198.4409 | 0.0031 | 0.0119 |
| 2024_09_20 22:00 | 3236170 | 4 | 12.1860 | 14.8693 | -115.8894 | 12.5765 | 189.7247 | 0.0128 | 0.0023 |
| 2024_09_20 22:00 | 3218309 | 5 | 16.3526 | 10.8284 | -116.5112 | 10.1682 | 177.1976 | 0.0092 | 0.0041 |
| 2024_09_20 22:00 | 3235085 | 6 | 10.6689 | 17.5815 | -114.2281 | 15.8049 | 160.3158 | 0.0051 | 0.0004 |
| 2024_09_20 22:00 | 3272366 | 7 | 16.7489 | 10.7577 | -114.8963 | 4.8921 | 56.5186 | 0.0050 | 0.0021 |
| 2024_09_20 22:00 | 3268317 | 8 | 8.3089 | 7.0557 | -116.1716 | 3.6860 | 42.9951 | 0.0183 | 0.0132 |
| 2024_09_20 22:00 | 3278695 | 9 | 13.2495 | 11.6112 | -117.7937 | 3.8421 | 58.0831 | 0.0038 | 0.0049 |
| 2024_09_20 22:00 | 3276480 | 10 | 18.6758 | 9.1138 | -116.1090 | 3.2941 | 28.5266 | 0.0176 | 0.0165 |
| 2024_09_20 22:00 | 3275610 | 11 | 8.8471 | 12.6509 | -115.8568 | 3.5048 | 59.1820 | 0.0109 | 0.0177 |
| 2024_09_20 22:00 | 3272340 | 12 | 14.5884 | 13.2174 | -117.7169 | 4.4910 | 29.6867 | 0.0111 | 0.0093 |
| 2024_09_20 22:00 | 3247367 | 13 | 9.7605 | 8.8427 | -115.6567 | 3.6027 | 36.7820 | 0.0064 | 0.0073 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417070_89AC5006 | 152650 | 877 | -98.0 | 152650 | 95 | -100.1 | 152650 | 712 | -104.5 | 152650 | 393 |
| MR_1774417070_8B6A07A6 | 504990 | 776 | -94.9 | 504990 | 253 | -94.5 | 504990 | 159 | -101.7 | 504990 | 749 |
| MR_1774417070_32E715C9 | 504990 | 776 | -91.9 | 504990 | 253 | -96.9 | 504990 | 159 | -101.6 | 504990 | 749 |
| MR_1774417070_2D40E0D4 | 504990 | 776 | -93.7 | 504990 | 253 | -97.9 | 504990 | 159 | -98.7 | 504990 | 749 |
| MR_1774417070_43F03D92 | 504990 | 776 | -95.3 | 504990 | 253 | -94.6 | 504990 | 159 | -100.4 | 504990 | 749 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 737: `80b1e309-2a9...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `80b1e309-2a95-4a4a-96ae-ca7a0ff1c43d` |
| Tag | **single-answer** |
| 정답 | **C20** |
| C20 의미 | Decrease A3 Offset threshold for 3239188_4 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[737] topology](images/train_0737.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3226753_1
- `C2`: Decrease transmission power for 3226753_1
- `C3`: Decrease A3 Offset threshold for 3226753_1
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3239188_4
- `C5`: Increase transmission power for 3239188_4
- `C6`: Adjust the azimuth of 3226753_1 by 50 degrees
- `C7`: Lift the tilt angle  of 3226753_1 by 6 degrees
- `C8`: Increase A3 Offset threshold for 3239188_4
- `C9`: Add neighbor relationship between 3239188_4 and 3226753_1
- `C10`: Add neighbor relationship between 3265726_3 and 3226753_1
- `C11`: Press down the tilt angle  of 3226753_1 by 6 degrees
- `C12`: Decrease transmission power for 3239188_4
- `C13`: Lift the tilt angle of 3239188_4 by 10 degrees
- `C14`: Press down the tilt angle of 3239188_4 by 10 degrees
- `C15`: Adjust the azimuth of 3239188_4 by 50 degrees
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3226753_1
- `C17`: Check test server and transmission issues
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3239188_4
- `C19`: Insufficient data; more data is needed for judgment.
- `C20`: Decrease A3 Offset threshold for 3239188_4 **← 정답**
- `C21`: Increase A3 Offset threshold for 3226753_1
- `C22`: Increase transmission power for 3226753_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.414 | MS1 | 121.4656646160 | 31.1446201529 | 181 | 504990 | -75.48 | 15.86 | 496.70 | 0.14 | 2.02 | 1593 |
| 2024-09-20 22:21:32.110 | MS1 | 121.4656750584 | 31.1446239941 | 181 | 504990 | -81.90 | 14.60 | 533.12 | 0.18 | 2.80 | 1560 |
| 2024-09-20 22:21:33.553 | MS1 | 121.4656619601 | 31.1446205339 | 181 | 504990 | -79.54 | 17.91 | 421.64 | 0.07 | 2.17 | 1576 |
| 2024-09-20 22:21:34.397 | MS1 | 121.4656711201 | 31.1446338693 | 181 | 504990 | -89.36 | -1.21 | 38.51 | 0.15 | 1.07 | 1586 |
| 2024-09-20 22:21:35.119 | MS1 | 121.4656763895 | 31.1446251931 | 181 | 504990 | -88.86 | -1.89 | 43.38 | 0.17 | 1.30 | 1574 |
| 2024-09-20 22:21:36.531 | MS1 | 121.4656770995 | 31.1446214131 | 181 | 504990 | -88.61 | -3.18 | 42.51 | 0.18 | 1.03 | 1594 |
| 2024-09-20 22:21:37.791 | MS1 | 121.4656669759 | 31.1446318032 | 181 | 504990 | -86.31 | -1.67 | 39.35 | 0.12 | 1.07 | 1560 |
| 2024-09-20 22:21:38.156 | MS1 | 121.4656728771 | 31.1446180385 | 181 | 504990 | -87.14 | -2.49 | 29.10 | 0.10 | 1.07 | 1568 |
| 2024-09-20 22:21:39.548 | MS1 | 121.4656708110 | 31.1446272687 | 443 | 504990 | -79.30 | 16.29 | 220.74 | 0.06 | 1.31 | 1564 |
| 2024-09-20 22:21:40.293 | MS1 | 121.4656629709 | 31.1446373768 | 443 | 504990 | -80.52 | 12.33 | 557.92 | 0.06 | 2.98 | 1598 |
| 2024-09-20 22:21:41.458 | MS1 | 121.4656705954 | 31.1446253027 | 443 | 504990 | -80.51 | 14.48 | 431.90 | 0.09 | 2.82 | 1583 |
| 2024-09-20 22:21:42.646 | MS1 | 121.4656633567 | 31.1446276355 | 443 | 504990 | -75.01 | 17.62 | 476.62 | 0.18 | 2.34 | 1596 |

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
| 3219275 | 2 | 121.4644456521 | 31.1522265013 | 221 | 7 | 0 | 41.2 | TDD | 324 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3226753 | 1 | 121.4684063197 | 31.1493355455 | 311 | 4 | 9 | 18.5 | TDD | 443 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3239188 | 4 | 121.4673513646 | 31.1519594600 | 257 | 11 | 12 | 28.2 | TDD | 181 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3265726 | 3 | 121.4695698786 | 31.1461981327 | 112 | 2 | 4 | 20.5 | TDD | 293 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |

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
| 2024-09-20 22:21:31.396 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.416 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.565 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.565 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.260 | NREventA3 | measId:2;ServCellPCI:161;Se... |
| 2024-09-20 22:21:38.500 | NRHandoverAttempt | SourcePCI:161;SourceNR-ARFC... |
| 2024-09-20 22:21:38.545 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.559 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.665 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.665 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3226753 | 1 | 9.2327 | 15.1793 | -114.7912 | 16.0643 | 125.2949 | 0.0188 | 0.0060 |
| 2024_09_20 22:00 | 3219275 | 2 | 18.1609 | 5.8011 | -116.3547 | 16.6617 | 170.4361 | 0.0147 | 0.0026 |
| 2024_09_20 22:00 | 3265726 | 3 | 12.3040 | 17.6891 | -117.6336 | 7.0807 | 178.9438 | 0.0134 | 0.0050 |
| 2024_09_20 22:00 | 3239188 | 4 | 6.8387 | 10.3214 | -117.2135 | 9.3994 | 143.5444 | 0.0081 | 0.1339 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414464_7B7E65FD | 504990 | 443 | -83.4 | 504990 | 181 | -90.5 | 504990 | 293 | -81.9 | 504990 | 324 |
| MR_1774414464_112ABA82 | 504990 | 443 | -83.8 | 504990 | 181 | -88.7 | 504990 | 293 | -83.9 | 504990 | 324 |
| MR_1774414464_0D91A8C3 | 504990 | 181 | -88.7 | 504990 | 443 | -83.4 | 504990 | 293 | -82.7 | 504990 | 324 |
| MR_1774414464_F0E3DC0B | 504990 | 443 | -80.4 | 504990 | 181 | -89.4 | 504990 | 293 | -84.6 | 504990 | 324 |
| MR_1774414464_D50032EB | 504990 | 181 | -89.2 | 504990 | 443 | -82.3 | 504990 | 293 | -82.8 | 504990 | 324 |
| MR_1774414464_05E7550B | 504990 | 443 | -82.3 | 504990 | 181 | -91.1 | 504990 | 293 | -82.8 | 504990 | 324 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 738: `7ffb1348-277...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `7ffb1348-277d-4f86-b467-ca1c38d29a85` |
| Tag | **single-answer** |
| 정답 | **C21** |
| C21 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3254252_6 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[738] topology](images/train_0738.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3273666_3 by 41 degrees
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3273666_3
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3273666_3
- `C4`: Decrease A3 Offset threshold for 3254252_6
- `C5`: Lift the tilt angle  of 3273666_3 by 6 degrees
- `C6`: Check test server and transmission issues
- `C7`: Decrease A3 Offset threshold for 3273666_3
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3254252_6
- `C9`: Add neighbor relationship between 3254252_6 and 3273666_3
- `C10`: Increase A3 Offset threshold for 3254252_6
- `C11`: Increase transmission power for 3273666_3
- `C12`: Decrease transmission power for 3273666_3
- `C13`: Press down the tilt angle  of 3273666_3 by 6 degrees
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Adjust the azimuth of 3254252_6 by 25 degrees
- `C16`: Increase transmission power for 3254252_6
- `C17`: Decrease transmission power for 3254252_6
- `C18`: Increase A3 Offset threshold for 3273666_3
- `C19`: Press down the tilt angle of 3254252_6 by 6 degrees
- `C20`: Lift the tilt angle of 3254252_6 by 6 degrees
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3254252_6 **← 정답**
- `C22`: Add neighbor relationship between 3276150_11 and 3273666_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.335 | MS1 | 121.4656722098 | 31.1446180388 | 189 | 504990 | -95.15 | 11.45 | 411.91 | 0.00 | 2.10 | 1568 |
| 2024-09-20 22:21:32.603 | MS1 | 121.4656641200 | 31.1446273260 | 298 | 504990 | -94.34 | 9.18 | 544.33 | 0.09 | 2.90 | 1596 |
| 2024-09-20 22:21:33.827 | MS1 | 121.4656752174 | 31.1446280531 | 948 | 504990 | -94.98 | 9.98 | 548.40 | 0.20 | 2.48 | 1597 |
| 2024-09-20 22:21:34.346 | MS1 | 121.4656697767 | 31.1446305577 | 177 | 152650 | -95.28 | 2.59 | 91.26 | 0.03 | 1.59 | 954 |
| 2024-09-20 22:21:35.395 | MS1 | 121.4656720384 | 31.1446257764 | 631 | 152650 | -96.69 | 5.12 | 58.45 | 0.08 | 1.85 | 970 |
| 2024-09-20 22:21:36.518 | MS1 | 121.4656601721 | 31.1446188814 | 756 | 152650 | -94.42 | 4.61 | 70.33 | 0.01 | 1.80 | 952 |
| 2024-09-20 22:21:37.170 | MS1 | 121.4656634123 | 31.1446370352 | 66 | 152650 | -89.03 | 2.63 | 50.28 | 0.18 | 1.63 | 976 |
| 2024-09-20 22:21:38.977 | MS1 | 121.4656626016 | 31.1446329835 | 177 | 152650 | -88.07 | 5.05 | 85.10 | 0.03 | 1.94 | 978 |
| 2024-09-20 22:21:39.774 | MS1 | 121.4656676138 | 31.1446287477 | 631 | 152650 | -96.67 | 3.74 | 63.71 | 0.01 | 1.96 | 999 |
| 2024-09-20 22:21:40.707 | MS1 | 121.4656686181 | 31.1446332259 | 756 | 152650 | -89.15 | 3.44 | 82.89 | 0.20 | 2.02 | 1589 |
| 2024-09-20 22:21:41.369 | MS1 | 121.4656643958 | 31.1446323662 | 66 | 152650 | -91.06 | 4.55 | 69.66 | 0.01 | 2.21 | 1572 |
| 2024-09-20 22:21:42.921 | MS1 | 121.4656686529 | 31.1446310504 | 177 | 152650 | -94.77 | 5.98 | 77.52 | 0.10 | 2.65 | 1576 |

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
| 3213138 | 10 | 121.4724956839 | 31.1461676809 | 275 | 10 | 6 | 28.0 | FDD | 49 | n1 | 152650 | 30M | 4T4R | 20 | 152650 |
| 3225547 | 8 | 121.4690893198 | 31.1551253296 | 338 | 12 | 12 | 29.1 | FDD | 777 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |
| 3230398 | 7 | 121.4682592494 | 31.1487898457 | 230 | 1 | 5 | 12.1 | FDD | 66 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |
| 3231155 | 12 | 121.4725024737 | 31.1448643259 | 56 | 12 | 11 | 6.1 | FDD | 631 | n1 | 152650 | 30M | 4T4R | 20 | 152650 |
| 3231804 | 9 | 121.4712891604 | 31.1523790645 | 103 | 13 | 4 | 9.1 | FDD | 177 | n1 | 152650 | 30M | 4T4R | 14 | 152650 |
| 3240705 | 1 | 121.4658310614 | 31.1557689342 | 220 | 9 | 5 | 20.1 | TDD | 298 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3250356 | 5 | 121.4730915683 | 31.1555088628 | 82 | 13 | 0 | 20.6 | TDD | 697 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3254252 | 6 | 121.4757079196 | 31.1454856346 | 289 | 5 | 12 | 12.2 | TDD | 189 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3266638 | 2 | 121.4662240641 | 31.1501857062 | 206 | 14 | 0 | 17.9 | TDD | 748 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3269563 | 13 | 121.4710499061 | 31.1535565350 | 243 | 5 | 7 | 12.1 | FDD | 539 | n1 | 152650 | 30M | 4T4R | 26 | 152650 |
| 3273666 | 3 | 121.4710537034 | 31.1516309894 | 254 | 4 | 12 | 26.3 | TDD | 656 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3276150 | 11 | 121.4759558913 | 31.1498888321 | 42 | 7 | 0 | 0.5 | FDD | 756 | n1 | 152650 | 30M | 4T4R | 17 | 152650 |
| 3278752 | 4 | 121.4730789325 | 31.1465425049 | 112 | 2 | 2 | 21.4 | TDD | 948 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |

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
| 2024-09-20 22:21:31.495 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.519 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.659 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.659 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.338 | NREventA2 | measId:1;ServCellPCI:719;Se... |
| 2024-09-20 22:21:35.440 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.643 | NREventA5 | measId:3;ServCellPCI:719;Se... |
| 2024-09-20 22:21:35.695 | NRHandoverAttempt | SourcePCI:719;SourceNR-ARFC... |
| 2024-09-20 22:21:35.715 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.726 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:35.836 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.836 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3240705 | 1 | 11.1105 | 13.0452 | -115.9119 | 9.4653 | 142.6576 | 0.0082 | 0.0173 |
| 2024_09_20 22:00 | 3266638 | 2 | 17.3902 | 15.9654 | -114.3380 | 17.9842 | 122.8167 | 0.0050 | 0.0021 |
| 2024_09_20 22:00 | 3273666 | 3 | 10.3069 | 16.8406 | -115.9062 | 13.0345 | 184.7352 | 0.0017 | 0.0125 |
| 2024_09_20 22:00 | 3278752 | 4 | 8.4380 | 19.9136 | -115.1543 | 15.7862 | 157.3391 | 0.0180 | 0.0129 |
| 2024_09_20 22:00 | 3250356 | 5 | 7.2581 | 15.3261 | -114.9711 | 15.0422 | 173.7693 | 0.0042 | 0.0114 |
| 2024_09_20 22:00 | 3254252 | 6 | 14.6785 | 12.4859 | -115.4435 | 16.7794 | 185.2702 | 0.0093 | 0.0099 |
| 2024_09_20 22:00 | 3230398 | 7 | 8.4557 | 7.1502 | -115.1730 | 4.2877 | 58.4743 | 0.0034 | 0.0010 |
| 2024_09_20 22:00 | 3225547 | 8 | 13.5705 | 6.1467 | -114.6471 | 3.9210 | 50.0114 | 0.0193 | 0.0007 |
| 2024_09_20 22:00 | 3231804 | 9 | 5.0300 | 18.8787 | -116.4754 | 4.0956 | 35.2547 | 0.0023 | 0.0072 |
| 2024_09_20 22:00 | 3213138 | 10 | 12.9683 | 12.3937 | -114.2190 | 4.0103 | 52.0677 | 0.0159 | 0.0187 |
| 2024_09_20 22:00 | 3276150 | 11 | 16.7481 | 12.3041 | -114.5896 | 3.8110 | 24.0852 | 0.0084 | 0.0059 |
| 2024_09_20 22:00 | 3231155 | 12 | 7.6359 | 11.9555 | -117.5826 | 3.9622 | 22.5649 | 0.0189 | 0.0096 |
| 2024_09_20 22:00 | 3269563 | 13 | 18.9823 | 12.3125 | -116.7096 | 3.1123 | 21.7533 | 0.0167 | 0.0087 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415779_F44818C2 | 152650 | 177 | -95.6 | 152650 | 539 | -97.5 | 152650 | 49 | -105.6 | 152650 | 777 |
| MR_1774415779_B6C1B157 | 152650 | 177 | -94.5 | 152650 | 539 | -96.4 | 152650 | 49 | -103.5 | 152650 | 777 |
| MR_1774415779_4E4A000C | 152650 | 177 | -93.4 | 152650 | 539 | -96.9 | 152650 | 49 | -105.7 | 152650 | 777 |
| MR_1774415779_35E11B2D | 504990 | 948 | -93.5 | 504990 | 656 | -97.7 | 504990 | 697 | -104.2 | 504990 | 748 |
| MR_1774415779_D4F8FE0B | 504990 | 948 | -93.2 | 504990 | 656 | -99.4 | 504990 | 697 | -100.7 | 504990 | 748 |
| MR_1774415779_CB5A5E7E | 504990 | 948 | -93.1 | 504990 | 656 | -99.3 | 504990 | 697 | -104.5 | 504990 | 748 |
| MR_1774415779_DD09BF92 | 152650 | 177 | -93.5 | 152650 | 539 | -99.2 | 152650 | 49 | -104.3 | 152650 | 777 |
| MR_1774415779_59CA89FF | 504990 | 948 | -95.4 | 504990 | 656 | -100.1 | 504990 | 697 | -101.8 | 504990 | 748 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 739: `e5604caf-9cf...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `e5604caf-9cf2-4a01-a4eb-b4218d978b99` |
| Tag | **single-answer** |
| 정답 | **C15** |
| C15 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[739] topology](images/train_0739.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3246077_3
- `C2`: Press down the tilt angle  of 3246077_3 by 9 degrees
- `C3`: Increase transmission power for 3246077_3
- `C4`: Lift the tilt angle of 3245185_2 by 10 degrees
- `C5`: Insufficient data; more data is needed for judgment.
- `C6`: Press down the tilt angle of 3245185_2 by 10 degrees
- `C7`: Increase A3 Offset threshold for 3246077_3
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3246077_3
- `C9`: Adjust the azimuth of 3245185_2 by 50 degrees
- `C10`: Decrease transmission power for 3246077_3
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3246077_3
- `C12`: Adjust the azimuth of 3246077_3 by 50 degrees
- `C13`: Decrease transmission power for 3245185_2
- `C14`: Increase transmission power for 3245185_2
- `C15`: Check test server and transmission issues **← 정답**
- `C16`: Add neighbor relationship between 3250852_1 and 3246077_3
- `C17`: Add neighbor relationship between 3245185_2 and 3246077_3
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3245185_2
- `C19`: Lift the tilt angle  of 3246077_3 by 9 degrees
- `C20`: Increase A3 Offset threshold for 3245185_2
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3245185_2
- `C22`: Decrease A3 Offset threshold for 3245185_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.139 | MS1 | 121.4656739402 | 31.1446261908 | 628 | 504990 | -91.38 | 12.39 | 461.44 | 0.02 | 2.86 | 1570 |
| 2024-09-20 22:21:32.469 | MS1 | 121.4656585282 | 31.1446200667 | 628 | 504990 | -89.14 | 15.60 | 378.57 | 0.17 | 2.88 | 1568 |
| 2024-09-20 22:21:33.797 | MS1 | 121.4656646707 | 31.1446282115 | 628 | 504990 | -87.24 | 13.87 | 425.96 | 0.20 | 2.95 | 1599 |
| 2024-09-20 22:21:34.753 | MS1 | 121.4656709225 | 31.1446225275 | 628 | 504990 | -87.17 | 12.60 | 57.57 | 0.06 | 2.12 | 473 |
| 2024-09-20 22:21:35.292 | MS1 | 121.4656766591 | 31.1446363858 | 628 | 504990 | -87.27 | 17.17 | 68.90 | 0.09 | 2.42 | 490 |
| 2024-09-20 22:21:36.111 | MS1 | 121.4656609325 | 31.1446198672 | 628 | 504990 | -85.72 | 15.43 | 96.78 | 0.05 | 2.87 | 302 |
| 2024-09-20 22:21:37.563 | MS1 | 121.4656695433 | 31.1446320809 | 628 | 504990 | -90.65 | 7.87 | 67.59 | 0.05 | 2.75 | 493 |
| 2024-09-20 22:21:38.322 | MS1 | 121.4656677517 | 31.1446290595 | 628 | 504990 | -89.70 | 12.21 | 90.29 | 0.05 | 2.90 | 385 |
| 2024-09-20 22:21:39.677 | MS1 | 121.4656765219 | 31.1446315550 | 628 | 504990 | -93.52 | 7.42 | 101.20 | 0.20 | 2.17 | 343 |
| 2024-09-20 22:21:40.445 | MS1 | 121.4656764295 | 31.1446239880 | 628 | 504990 | -93.24 | 11.17 | 348.70 | 0.19 | 2.89 | 1586 |
| 2024-09-20 22:21:41.507 | MS1 | 121.4656679494 | 31.1446302384 | 628 | 504990 | -93.50 | 7.80 | 565.92 | 0.15 | 2.60 | 1561 |
| 2024-09-20 22:21:42.828 | MS1 | 121.4656699132 | 31.1446300995 | 628 | 504990 | -91.01 | 12.77 | 400.56 | 0.08 | 2.37 | 1597 |

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
| 3245185 | 2 | 121.4659634136 | 31.1527163858 | 98 | 12 | 11 | 41.8 | TDD | 628 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3246077 | 3 | 121.4661657102 | 31.1477688108 | 66 | 2 | 12 | 45.8 | TDD | 702 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3250852 | 1 | 121.4647998798 | 31.1474202403 | 70 | 13 | 6 | 15.3 | TDD | 337 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3254193 | 4 | 121.4650681115 | 31.1456833056 | 32 | 4 | 5 | 27.3 | TDD | 958 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |

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
| 2024-09-20 22:21:30.836 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:30.969 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.969 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.710 | NREventA3 | measId:2;ServCellPCI:232;Se... |
| 2024-09-20 22:21:37.950 | NRHandoverAttempt | SourcePCI:232;SourceNR-ARFC... |
| 2024-09-20 22:21:37.982 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.995 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.108 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.108 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3250852 | 1 | 9.9246 | 9.4257 | -115.2013 | 13.0296 | 148.7227 | 0.0103 | 0.0171 |
| 2024_09_20 22:00 | 3245185 | 2 | 15.1546 | 7.7998 | -114.6478 | 12.3501 | 125.4145 | 0.0066 | 0.0018 |
| 2024_09_20 22:00 | 3246077 | 3 | 13.2050 | 19.0350 | -117.7775 | 7.2490 | 90.8386 | 0.0021 | 0.0100 |
| 2024_09_20 22:00 | 3254193 | 4 | 13.9371 | 14.9267 | -116.2304 | 13.4619 | 93.8576 | 0.0119 | 0.0083 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412367_D41195FD | 504990 | 628 | -88.0 | 504990 | 702 | -88.0 | 504990 | 337 | -100.2 | 504990 | 958 |
| MR_1774412367_556FA6C4 | 504990 | 628 | -88.9 | 504990 | 702 | -85.2 | 504990 | 337 | -102.2 | 504990 | 958 |
| MR_1774412367_63DC7845 | 504990 | 628 | -85.3 | 504990 | 702 | -85.5 | 504990 | 337 | -102.3 | 504990 | 958 |
| MR_1774412367_A63F83EE | 504990 | 628 | -88.4 | 504990 | 702 | -86.4 | 504990 | 337 | -100.0 | 504990 | 958 |
| MR_1774412367_9E4FA000 | 504990 | 628 | -85.9 | 504990 | 702 | -85.9 | 504990 | 337 | -99.8 | 504990 | 958 |
| MR_1774412367_D45B6450 | 504990 | 628 | -88.1 | 504990 | 702 | -87.5 | 504990 | 337 | -102.8 | 504990 | 958 |
| MR_1774412367_D0AE1D09 | 504990 | 628 | -85.4 | 504990 | 702 | -86.6 | 504990 | 337 | -102.6 | 504990 | 958 |
| MR_1774412367_175EC075 | 504990 | 628 | -86.0 | 504990 | 702 | -87.5 | 504990 | 337 | -102.0 | 504990 | 958 |

> *... 2개 열 생략 (전체 14열)*

---
