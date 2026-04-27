# Track A 문제 분석 — test[440]~test[449]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/test.json`
> 범위: test[440] ~ test[449] (10개)

## 목차

1. [문제 440: `c077ae18-f4b...`](#440) — single-answer
2. [문제 441: `f8b790f0-b34...`](#441) — single-answer
3. [문제 442: `043f6132-917...`](#442) — single-answer
4. [문제 443: `80ee0db6-6fa...`](#443) — multiple-answer
5. [문제 444: `b144d49f-593...`](#444) — single-answer
6. [문제 445: `db674175-94d...`](#445) — single-answer
7. [문제 446: `98d94e6f-74d...`](#446) — single-answer
8. [문제 447: `4108db9f-92e...`](#447) — single-answer
9. [문제 448: `0398bf0e-df2...`](#448) — single-answer
10. [문제 449: `b33a9a1e-d85...`](#449) — single-answer

---

### 문제 440: `c077ae18-f4b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `c077ae18-f4b2-4c94-bdda-8f6c323ae216` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[440] topology](images/test_0440.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3252450_1
- `C2`: Decrease transmission power for 3239258_2
- `C3`: Add neighbor relationship between 3252450_1 and 3239258_2
- `C4`: Insufficient data; more data is needed for judgment.
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3239258_2
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3252450_1
- `C7`: Lift the tilt angle of 3252450_1 by 3 degrees
- `C8`: Decrease A3 Offset threshold for 3252450_1
- `C9`: Check test server and transmission issues
- `C10`: Increase transmission power for 3239258_2
- `C11`: Press down the tilt angle  of 3239258_2 by 4 degrees
- `C12`: Decrease transmission power for 3252450_1
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3252450_1
- `C14`: Adjust the azimuth of 3239258_2 by 50 degrees
- `C15`: Add neighbor relationship between 3278612_3 and 3239258_2
- `C16`: Adjust the azimuth of 3252450_1 by 50 degrees
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3239258_2
- `C18`: Decrease A3 Offset threshold for 3239258_2
- `C19`: Lift the tilt angle  of 3239258_2 by 4 degrees
- `C20`: Increase A3 Offset threshold for 3239258_2
- `C21`: Press down the tilt angle of 3252450_1 by 3 degrees
- `C22`: Increase A3 Offset threshold for 3252450_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.967 | MS1 | 121.4656732906 | 31.1446339592 | 99 | 504990 | -85.56 | 12.82 | 491.06 | 0.01 | 2.88 | 1569 |
| 2024-09-20 22:21:32.542 | MS1 | 121.4656647822 | 31.1446234351 | 99 | 504990 | -87.59 | 14.39 | 558.83 | 0.03 | 2.77 | 1600 |
| 2024-09-20 22:21:33.314 | MS1 | 121.4656651401 | 31.1446189326 | 99 | 504990 | -85.33 | 12.34 | 425.71 | 0.09 | 2.67 | 1588 |
| 2024-09-20 22:21:34.376 | MS1 | 121.4656601783 | 31.1446212063 | 99 | 504990 | -89.62 | 16.75 | 78.38 | 0.09 | 2.51 | 1560 |
| 2024-09-20 22:21:35.796 | MS1 | 121.4656643440 | 31.1446360341 | 99 | 504990 | -85.14 | 13.53 | 66.25 | 0.10 | 2.15 | 1590 |
| 2024-09-20 22:21:36.756 | MS1 | 121.4656712534 | 31.1446294834 | 99 | 504990 | -85.95 | 12.04 | 78.81 | 0.10 | 2.34 | 1596 |
| 2024-09-20 22:21:37.235 | MS1 | 121.4656616071 | 31.1446321828 | 99 | 504990 | -92.92 | 12.26 | 80.69 | 0.10 | 2.33 | 1596 |
| 2024-09-20 22:21:38.846 | MS1 | 121.4656639353 | 31.1446214142 | 99 | 504990 | -90.24 | 11.43 | 74.36 | 0.03 | 2.53 | 1575 |
| 2024-09-20 22:21:39.195 | MS1 | 121.4656615788 | 31.1446351522 | 99 | 504990 | -90.69 | 11.93 | 94.32 | 0.09 | 2.39 | 1593 |
| 2024-09-20 22:21:40.126 | MS1 | 121.4656664551 | 31.1446318253 | 99 | 504990 | -92.03 | 10.95 | 465.70 | 0.20 | 2.03 | 1599 |
| 2024-09-20 22:21:41.652 | MS1 | 121.4656660453 | 31.1446204527 | 99 | 504990 | -90.64 | 8.04 | 323.75 | 0.04 | 2.99 | 1564 |
| 2024-09-20 22:21:42.509 | MS1 | 121.4656684397 | 31.1446317914 | 99 | 504990 | -90.70 | 11.32 | 344.28 | 0.00 | 2.71 | 1584 |

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
| 3239258 | 2 | 121.4729798777 | 31.1546067607 | 68 | 3 | 6 | 27.1 | TDD | 563 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3252450 | 1 | 121.4733310835 | 31.1526806136 | 81 | 2 | 10 | 26.8 | TDD | 99 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3275844 | 4 | 121.4663354014 | 31.1499789454 | 304 | 15 | 3 | 29.7 | TDD | 430 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3278612 | 3 | 121.4733684807 | 31.1526047692 | 310 | 15 | 5 | 47.0 | TDD | 875 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |

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
| 2024-09-20 22:21:31.333 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.349 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.465 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.465 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.191 | NREventA3 | measId:2;ServCellPCI:378;Se... |
| 2024-09-20 22:21:38.431 | NRHandoverAttempt | SourcePCI:378;SourceNR-ARFC... |
| 2024-09-20 22:21:38.479 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.493 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.610 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.610 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3252450 | 1 | 89.9628 | 82.9641 | -116.3475 | 16.8758 | 129.6146 | 0.0162 | 0.0088 |
| 2024_09_19 22:00 | 3239258 | 2 | 85.2643 | 85.8581 | -116.9762 | 19.3809 | 95.7076 | 0.0004 | 0.0140 |
| 2024_09_19 22:00 | 3278612 | 3 | 92.1933 | 82.1719 | -114.6489 | 14.7444 | 106.5945 | 0.0076 | 0.0043 |
| 2024_09_19 22:00 | 3275844 | 4 | 84.5305 | 76.3757 | -114.2968 | 12.4560 | 183.6744 | 0.0104 | 0.0188 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415105_A0446A92 | 504990 | 99 | -91.2 | 504990 | 563 | -97.4 | 504990 | 875 | -99.0 | 504990 | 430 |
| MR_1774415105_C8F1393B | 504990 | 99 | -91.4 | 504990 | 563 | -97.9 | 504990 | 875 | -98.6 | 504990 | 430 |
| MR_1774415105_B47E912B | 504990 | 99 | -89.8 | 504990 | 563 | -96.5 | 504990 | 875 | -95.8 | 504990 | 430 |
| MR_1774415105_6A1402B1 | 504990 | 99 | -91.5 | 504990 | 563 | -96.4 | 504990 | 875 | -95.9 | 504990 | 430 |
| MR_1774415105_D34AB794 | 504990 | 99 | -91.3 | 504990 | 563 | -97.2 | 504990 | 875 | -97.7 | 504990 | 430 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 441: `f8b790f0-b34...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `f8b790f0-b34a-4003-897f-2759c4ffc007` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[441] topology](images/test_0441.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3213078_2
- `C2`: Insufficient data; more data is needed for judgment.
- `C3`: Add neighbor relationship between 3213078_2 and 3210437_1
- `C4`: Add neighbor relationship between 3262192_3 and 3210437_1
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3213078_2
- `C6`: Increase A3 Offset threshold for 3210437_1
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3210437_1
- `C8`: Increase transmission power for 3210437_1
- `C9`: Press down the tilt angle of 3213078_2 by 10 degrees
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3210437_1
- `C11`: Check test server and transmission issues
- `C12`: Increase A3 Offset threshold for 3213078_2
- `C13`: Decrease transmission power for 3213078_2
- `C14`: Press down the tilt angle  of 3210437_1 by 4 degrees
- `C15`: Lift the tilt angle  of 3210437_1 by 4 degrees
- `C16`: Decrease transmission power for 3210437_1
- `C17`: Increase transmission power for 3213078_2
- `C18`: Adjust the azimuth of 3210437_1 by 21 degrees
- `C19`: Lift the tilt angle of 3213078_2 by 10 degrees
- `C20`: Decrease A3 Offset threshold for 3213078_2
- `C21`: Decrease A3 Offset threshold for 3210437_1
- `C22`: Adjust the azimuth of 3213078_2 by 6 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.229 | MS1 | 121.4656584126 | 31.1446377911 | 412 | 504990 | -75.92 | 15.44 | 476.82 | 0.06 | 2.32 | 1560 |
| 2024-09-20 22:21:32.603 | MS1 | 121.4656656066 | 31.1446280249 | 412 | 504990 | -78.24 | 16.96 | 319.64 | 0.15 | 2.79 | 1577 |
| 2024-09-20 22:21:33.807 | MS1 | 121.4656726028 | 31.1446246409 | 412 | 504990 | -77.12 | 17.88 | 544.48 | 0.03 | 2.73 | 1585 |
| 2024-09-20 22:21:34.584 | MS1 | 121.4656592150 | 31.1446302579 | 412 | 504990 | -88.98 | -3.76 | 63.48 | 0.19 | 1.34 | 1586 |
| 2024-09-20 22:21:35.774 | MS1 | 121.4656666403 | 31.1446301409 | 412 | 504990 | -90.43 | -0.56 | 59.97 | 0.16 | 1.48 | 1578 |
| 2024-09-20 22:21:36.965 | MS1 | 121.4656619874 | 31.1446188663 | 412 | 504990 | -85.40 | -0.07 | 42.87 | 0.04 | 1.13 | 1588 |
| 2024-09-20 22:21:37.281 | MS1 | 121.4656631688 | 31.1446344996 | 412 | 504990 | -90.64 | -2.94 | 58.17 | 0.17 | 1.27 | 1587 |
| 2024-09-20 22:21:38.405 | MS1 | 121.4656688298 | 31.1446228265 | 412 | 504990 | -82.62 | 12.27 | 442.01 | 0.18 | 1.18 | 1598 |
| 2024-09-20 22:21:39.242 | MS1 | 121.4656629583 | 31.1446367397 | 412 | 504990 | -84.92 | 12.35 | 486.17 | 0.10 | 1.20 | 1575 |
| 2024-09-20 22:21:40.669 | MS1 | 121.4656751334 | 31.1446294537 | 412 | 504990 | -75.57 | 16.69 | 314.44 | 0.13 | 2.05 | 1574 |
| 2024-09-20 22:21:41.106 | MS1 | 121.4656585608 | 31.1446282086 | 412 | 504990 | -75.66 | 14.91 | 597.55 | 0.08 | 2.69 | 1565 |
| 2024-09-20 22:21:42.717 | MS1 | 121.4656624768 | 31.1446346227 | 412 | 504990 | -76.85 | 13.74 | 576.09 | 0.01 | 2.56 | 1569 |

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
| 3210437 | 1 | 121.4755478833 | 31.1490057148 | 222 | 2 | 4 | 36.7 | TDD | 779 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3213078 | 2 | 121.4677055754 | 31.1515636139 | 200 | 10 | 1 | 17.2 | TDD | 412 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3251785 | 4 | 121.4666831374 | 31.1530670174 | 65 | 9 | 3 | 44.2 | TDD | 974 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3262192 | 3 | 121.4711498226 | 31.1473754777 | 207 | 11 | 9 | 45.2 | TDD | 966 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |

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
| 2024-09-20 22:21:30.857 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.874 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.007 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.007 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.727 | NREventA3 | measId:2;ServCellPCI:172;Se... |
| 2024-09-20 22:21:35.727 | NREventA3 | measId:2;ServCellPCI:172;Se... |
| 2024-09-20 22:21:36.727 | NREventA3 | measId:2;ServCellPCI:172;Se... |
| 2024-09-20 22:21:39.227 | NRRRCReestablishAttempt | PCI:172 |
| 2024-09-20 22:21:39.244 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.259 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:39.405 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.405 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3210437 | 1 | 7.5754 | 16.9042 | -117.9905 | 7.6809 | 191.0931 | 0.0136 | 0.0034 |
| 2024_09_20 22:00 | 3213078 | 2 | 5.0261 | 16.5263 | -114.9796 | 14.7516 | 165.4219 | 0.0167 | 0.1021 |
| 2024_09_20 22:00 | 3262192 | 3 | 18.6186 | 8.8399 | -114.7946 | 12.7243 | 190.2525 | 0.0136 | 0.0054 |
| 2024_09_20 22:00 | 3251785 | 4 | 5.8164 | 12.4219 | -114.9930 | 17.0314 | 135.1166 | 0.0164 | 0.0012 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415994_0825BB51 | 504990 | 779 | -84.3 | 504990 | 412 | -89.8 | 504990 | 966 | -91.7 | 504990 | 974 |
| MR_1774415994_7593F28F | 504990 | 412 | -89.1 | 504990 | 779 | -85.8 | 504990 | 966 | -90.0 | 504990 | 974 |
| MR_1774415994_BED32E4C | 504990 | 412 | -90.3 | 504990 | 779 | -82.8 | 504990 | 966 | -90.6 | 504990 | 974 |
| MR_1774415994_03583B35 | 504990 | 412 | -89.8 | 504990 | 779 | -84.2 | 504990 | 966 | -91.0 | 504990 | 974 |
| MR_1774415994_FAE4FE20 | 504990 | 412 | -90.5 | 504990 | 779 | -84.6 | 504990 | 966 | -88.7 | 504990 | 974 |
| MR_1774415994_0E22047D | 504990 | 412 | -88.9 | 504990 | 779 | -85.7 | 504990 | 966 | -90.7 | 504990 | 974 |
| MR_1774415994_24287910 | 504990 | 412 | -90.8 | 504990 | 779 | -86.4 | 504990 | 966 | -91.1 | 504990 | 974 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 442: `043f6132-917...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `043f6132-917a-432b-91ea-64db57ed0cda` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[442] topology](images/test_0442.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3250102_4
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3250102_4
- `C3`: Adjust the azimuth of 3225387_1 by 50 degrees
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3225387_1
- `C5`: Check test server and transmission issues
- `C6`: Increase transmission power for 3225387_1
- `C7`: Decrease transmission power for 3250102_4
- `C8`: Increase A3 Offset threshold for 3225387_1
- `C9`: Decrease A3 Offset threshold for 3250102_4
- `C10`: Press down the tilt angle  of 3225387_1 by 10 degrees
- `C11`: Decrease A3 Offset threshold for 3225387_1
- `C12`: Decrease transmission power for 3225387_1
- `C13`: Add neighbor relationship between 3277852_2 and 3225387_1
- `C14`: Add neighbor relationship between 3250102_4 and 3225387_1
- `C15`: Lift the tilt angle  of 3225387_1 by 10 degrees
- `C16`: Insufficient data; more data is needed for judgment.
- `C17`: Press down the tilt angle of 3250102_4 by 8 degrees
- `C18`: Lift the tilt angle of 3250102_4 by 8 degrees
- `C19`: Adjust the azimuth of 3250102_4 by 50 degrees
- `C20`: Increase transmission power for 3250102_4
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3225387_1
- `C22`: Increase A3 Offset threshold for 3250102_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.368 | MS1 | 121.4656754256 | 31.1446216466 | 774 | 504990 | -78.61 | 15.97 | 323.99 | 0.15 | 2.59 | 1579 |
| 2024-09-20 22:21:32.507 | MS1 | 121.4656750357 | 31.1446196716 | 774 | 504990 | -76.11 | 17.01 | 363.30 | 0.01 | 2.90 | 1600 |
| 2024-09-20 22:21:33.935 | MS1 | 121.4656611067 | 31.1446218001 | 774 | 504990 | -83.59 | 12.84 | 545.06 | 0.06 | 2.65 | 1568 |
| 2024-09-20 22:21:34.269 | MS1 | 121.4656584887 | 31.1446305772 | 774 | 504990 | -83.76 | -3.79 | 66.69 | 0.17 | 1.16 | 1586 |
| 2024-09-20 22:21:35.823 | MS1 | 121.4656672324 | 31.1446356171 | 774 | 504990 | -83.10 | -2.72 | 28.86 | 0.18 | 1.42 | 1575 |
| 2024-09-20 22:21:36.971 | MS1 | 121.4656767404 | 31.1446376090 | 774 | 504990 | -88.51 | -0.26 | 39.16 | 0.08 | 1.09 | 1568 |
| 2024-09-20 22:21:37.727 | MS1 | 121.4656692429 | 31.1446260259 | 774 | 504990 | -92.15 | -0.21 | 62.27 | 0.01 | 1.22 | 1566 |
| 2024-09-20 22:21:38.767 | MS1 | 121.4656646562 | 31.1446287873 | 774 | 504990 | -84.82 | -1.03 | 31.79 | 0.01 | 1.44 | 1598 |
| 2024-09-20 22:21:39.221 | MS1 | 121.4656731190 | 31.1446260704 | 688 | 504990 | -77.93 | 14.64 | 234.84 | 0.13 | 1.41 | 1584 |
| 2024-09-20 22:21:40.839 | MS1 | 121.4656628196 | 31.1446255025 | 688 | 504990 | -83.89 | 12.71 | 408.62 | 0.13 | 2.08 | 1584 |
| 2024-09-20 22:21:41.264 | MS1 | 121.4656631740 | 31.1446236182 | 688 | 504990 | -80.65 | 16.18 | 583.79 | 0.18 | 2.53 | 1561 |
| 2024-09-20 22:21:42.323 | MS1 | 121.4656678210 | 31.1446340448 | 688 | 504990 | -78.89 | 13.80 | 409.45 | 0.19 | 2.24 | 1577 |

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
| 3225387 | 1 | 121.4713775839 | 31.1446282787 | 60 | 11 | 1 | 16.7 | TDD | 688 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3236272 | 3 | 121.4649088408 | 31.1505357446 | 135 | 5 | 5 | 36.9 | TDD | 732 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3250102 | 4 | 121.4722676115 | 31.1520331104 | 285 | 6 | 9 | 37.8 | TDD | 774 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3277852 | 2 | 121.4666524813 | 31.1513220115 | 296 | 6 | 2 | 21.4 | TDD | 716 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:30.916 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.938 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.054 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.054 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.741 | NREventA3 | measId:2;ServCellPCI:956;Se... |
| 2024-09-20 22:21:37.981 | NRHandoverAttempt | SourcePCI:956;SourceNR-ARFC... |
| 2024-09-20 22:21:38.015 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.026 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.158 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.158 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3225387 | 1 | 5.4369 | 15.9000 | -116.0997 | 17.9970 | 97.5597 | 0.0041 | 0.0022 |
| 2024_09_20 22:00 | 3277852 | 2 | 13.6821 | 8.0440 | -117.5875 | 13.9962 | 88.4652 | 0.0187 | 0.0059 |
| 2024_09_20 22:00 | 3236272 | 3 | 10.4414 | 12.1482 | -116.2209 | 7.6928 | 141.3033 | 0.0011 | 0.0043 |
| 2024_09_20 22:00 | 3250102 | 4 | 19.3190 | 9.4775 | -117.5386 | 17.4088 | 128.2144 | 0.0183 | 0.1898 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417024_F4DB8832 | 504990 | 774 | -85.0 | 504990 | 688 | -76.3 | 504990 | 716 | -87.8 | 504990 | 732 |
| MR_1774417024_5551B67E | 504990 | 688 | -78.5 | 504990 | 774 | -84.2 | 504990 | 716 | -89.2 | 504990 | 732 |
| MR_1774417024_49BC4A4C | 504990 | 774 | -84.1 | 504990 | 688 | -79.9 | 504990 | 716 | -86.7 | 504990 | 732 |
| MR_1774417024_F34AB719 | 504990 | 774 | -85.7 | 504990 | 688 | -76.2 | 504990 | 716 | -86.2 | 504990 | 732 |
| MR_1774417024_AAECC70A | 504990 | 688 | -78.7 | 504990 | 774 | -81.8 | 504990 | 716 | -89.7 | 504990 | 732 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 443: `80ee0db6-6fa...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `80ee0db6-6fa8-4797-a5da-7a623e754423` |
| Tag | **multiple-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[443] topology](images/test_0443.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3238501_1
- `C2`: Adjust the azimuth of 3238501_1 by 50 degrees
- `C3`: Check test server and transmission issues
- `C4`: Press down the tilt angle  of 3272018_4 by 6 degrees
- `C5`: Increase A3 Offset threshold for 3238501_1
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3272018_4
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3238501_1
- `C8`: Add neighbor relationship between 3238501_1 and 3272018_4
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3238501_1
- `C10`: Lift the tilt angle of 3238501_1 by 10 degrees
- `C11`: Insufficient data; more data is needed for judgment.
- `C12`: Increase transmission power for 3238501_1
- `C13`: Decrease transmission power for 3272018_4
- `C14`: Increase A3 Offset threshold for 3272018_4
- `C15`: Add neighbor relationship between 3227345_2 and 3272018_4
- `C16`: Adjust the azimuth of 3272018_4 by 8 degrees
- `C17`: Lift the tilt angle  of 3272018_4 by 6 degrees
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3272018_4
- `C19`: Decrease A3 Offset threshold for 3238501_1
- `C20`: Decrease A3 Offset threshold for 3272018_4
- `C21`: Increase transmission power for 3272018_4
- `C22`: Press down the tilt angle of 3238501_1 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.220 | MS1 | 121.4656607319 | 31.1446246433 | 1007 | 504990 | -91.73 | 17.24 | 437.03 | 0.08 | 2.48 | 1575 |
| 2024-09-20 22:21:32.731 | MS1 | 121.4656735854 | 31.1446320074 | 1007 | 504990 | -91.65 | 15.03 | 466.80 | 0.19 | 2.65 | 1569 |
| 2024-09-20 22:21:33.943 | MS1 | 121.4656711022 | 31.1446304599 | 1007 | 504990 | -93.58 | 12.14 | 292.78 | 0.01 | 2.28 | 1564 |
| 2024-09-20 22:21:34.263 | MS1 | 121.4656617379 | 31.1446342132 | 1007 | 504990 | -103.41 | -0.96 | 23.60 | 0.14 | 1.05 | 1572 |
| 2024-09-20 22:21:35.357 | MS1 | 121.4656612437 | 31.1446313614 | 1007 | 504990 | -107.88 | -1.31 | 66.87 | 0.18 | 1.43 | 1587 |
| 2024-09-20 22:21:36.827 | MS1 | 121.4656696212 | 31.1446338784 | 1007 | 504990 | -104.22 | 0.34 | 26.27 | 0.09 | 1.34 | 1564 |
| 2024-09-20 22:21:37.363 | MS1 | 121.4656652038 | 31.1446286508 | 1007 | 504990 | -100.47 | 0.35 | 69.85 | 0.00 | 1.35 | 1590 |
| 2024-09-20 22:21:38.167 | MS1 | 121.4656743708 | 31.1446355218 | 1007 | 504990 | -107.66 | 1.61 | 51.79 | 0.09 | 1.40 | 1579 |
| 2024-09-20 22:21:39.602 | MS1 | 121.4656652060 | 31.1446331368 | 1007 | 504990 | -105.76 | 1.07 | 62.02 | 0.03 | 1.47 | 1585 |
| 2024-09-20 22:21:40.951 | MS1 | 121.4656648518 | 31.1446371706 | 1007 | 504990 | -92.38 | 15.82 | 350.03 | 0.02 | 2.53 | 1587 |
| 2024-09-20 22:21:41.257 | MS1 | 121.4656685523 | 31.1446236677 | 1007 | 504990 | -92.14 | 16.43 | 500.71 | 0.03 | 2.43 | 1594 |
| 2024-09-20 22:21:42.874 | MS1 | 121.4656664327 | 31.1446228406 | 1007 | 504990 | -92.02 | 13.51 | 348.98 | 0.00 | 2.15 | 1561 |

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
| 3227345 | 2 | 121.4716322231 | 31.1486515318 | 35 | 4 | 0 | 19.4 | TDD | 717 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3238501 | 1 | 121.4720350664 | 31.1451738065 | 339 | 11 | 5 | 47.7 | TDD | 1007 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3272018 | 4 | 121.4697931476 | 31.1524848858 | 212 | 4 | 4 | 32.2 | TDD | 975 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3272153 | 3 | 121.4661451954 | 31.1504907501 | 247 | 12 | 8 | 41.8 | TDD | 270 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:30.862 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.886 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:30.986 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.986 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.249 | NREventA2 | measId:1;ServCellPCI:335;Se... |
| 2024-09-20 22:21:34.383 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3238501 | 1 | 10.3490 | 18.2261 | -114.6022 | 9.2730 | 132.3870 | 0.1502 | 0.0170 |
| 2024_09_20 22:00 | 3227345 | 2 | 17.4861 | 18.0063 | -115.5759 | 6.9724 | 134.3242 | 0.0082 | 0.0006 |
| 2024_09_20 22:00 | 3272153 | 3 | 13.1600 | 10.1009 | -116.8321 | 14.7447 | 108.4673 | 0.0009 | 0.0064 |
| 2024_09_20 22:00 | 3272018 | 4 | 17.6442 | 17.5223 | -114.2302 | 18.8226 | 128.5031 | 0.0013 | 0.0131 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417071_A9CF3105 | 504990 | 1007 | -102.0 | 504990 | 975 | -107.3 | 504990 | 717 | -111.4 | 504990 | 270 |
| MR_1774417071_7B121E31 | 504990 | 1007 | -104.6 | 504990 | 975 | -106.3 | 504990 | 717 | -113.1 | 504990 | 270 |
| MR_1774417071_EA3114D4 | 504990 | 1007 | -104.8 | 504990 | 975 | -107.9 | 504990 | 717 | -110.4 | 504990 | 270 |
| MR_1774417071_2FA0E57B | 504990 | 1007 | -104.7 | 504990 | 975 | -106.1 | 504990 | 717 | -111.5 | 504990 | 270 |
| MR_1774417071_76380EA6 | 504990 | 1007 | -103.1 | 504990 | 975 | -106.4 | 504990 | 717 | -110.4 | 504990 | 270 |
| MR_1774417071_D7D0E344 | 504990 | 1007 | -102.7 | 504990 | 975 | -106.7 | 504990 | 717 | -110.8 | 504990 | 270 |
| MR_1774417071_30F883F8 | 504990 | 1007 | -103.8 | 504990 | 975 | -105.5 | 504990 | 717 | -111.1 | 504990 | 270 |
| MR_1774417071_386657D1 | 504990 | 1007 | -101.9 | 504990 | 975 | -106.5 | 504990 | 717 | -113.8 | 504990 | 270 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 444: `b144d49f-593...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `b144d49f-5938-4f43-b662-9f9aa35ca48e` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[444] topology](images/test_0444.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3237769_1
- `C2`: Decrease transmission power for 3227764_2
- `C3`: Decrease transmission power for 3237769_1
- `C4`: Lift the tilt angle  of 3237769_1 by 4 degrees
- `C5`: Press down the tilt angle  of 3237769_1 by 4 degrees
- `C6`: Add neighbor relationship between 3227764_2 and 3237769_1
- `C7`: Increase A3 Offset threshold for 3227764_2
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3227764_2
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3237769_1
- `C10`: Add neighbor relationship between 3262293_7 and 3237769_1
- `C11`: Decrease A3 Offset threshold for 3227764_2
- `C12`: Decrease A3 Offset threshold for 3237769_1
- `C13`: Check test server and transmission issues
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Press down the tilt angle of 3227764_2 by 5 degrees
- `C16`: Adjust the azimuth of 3237769_1 by 2 degrees
- `C17`: Increase transmission power for 3237769_1
- `C18`: Increase A3 Offset threshold for 3237769_1
- `C19`: Adjust the azimuth of 3227764_2 by 5 degrees
- `C20`: Increase transmission power for 3227764_2
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3227764_2
- `C22`: Lift the tilt angle of 3227764_2 by 5 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.261 | MS1 | 121.4656646138 | 31.1446362589 | 933 | 504990 | -94.52 | 11.59 | 565.40 | 0.12 | 2.45 | 1587 |
| 2024-09-20 22:21:32.966 | MS1 | 121.4656697537 | 31.1446202433 | 142 | 504990 | -95.00 | 11.20 | 571.72 | 0.14 | 2.18 | 1577 |
| 2024-09-20 22:21:33.294 | MS1 | 121.4656681206 | 31.1446286795 | 145 | 504990 | -94.47 | 10.53 | 396.88 | 0.19 | 2.88 | 1578 |
| 2024-09-20 22:21:34.912 | MS1 | 121.4656655061 | 31.1446334057 | 916 | 152650 | -96.36 | 4.98 | 83.01 | 0.14 | 1.83 | 910 |
| 2024-09-20 22:21:35.595 | MS1 | 121.4656673607 | 31.1446270287 | 991 | 152650 | -91.14 | 2.11 | 100.54 | 0.07 | 1.78 | 977 |
| 2024-09-20 22:21:36.485 | MS1 | 121.4656693701 | 31.1446267471 | 386 | 152650 | -93.77 | 3.24 | 99.07 | 0.14 | 1.88 | 966 |
| 2024-09-20 22:21:37.334 | MS1 | 121.4656591429 | 31.1446239680 | 554 | 152650 | -89.64 | 6.85 | 98.43 | 0.03 | 1.87 | 900 |
| 2024-09-20 22:21:38.535 | MS1 | 121.4656742470 | 31.1446221240 | 916 | 152650 | -93.34 | 4.45 | 52.06 | 0.09 | 1.96 | 966 |
| 2024-09-20 22:21:39.753 | MS1 | 121.4656696251 | 31.1446236588 | 991 | 152650 | -89.05 | 5.93 | 46.02 | 0.07 | 1.96 | 965 |
| 2024-09-20 22:21:40.522 | MS1 | 121.4656605352 | 31.1446324821 | 386 | 152650 | -92.03 | 6.30 | 90.44 | 0.08 | 2.78 | 1578 |
| 2024-09-20 22:21:41.836 | MS1 | 121.4656649497 | 31.1446318263 | 554 | 152650 | -93.61 | 7.52 | 61.99 | 0.03 | 2.31 | 1588 |
| 2024-09-20 22:21:42.109 | MS1 | 121.4656670187 | 31.1446374201 | 916 | 152650 | -91.43 | 4.36 | 46.59 | 0.17 | 2.02 | 1572 |

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
| 3212393 | 4 | 121.4758054565 | 31.1471591159 | 248 | 4 | 10 | 26.3 | TDD | 11 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3216770 | 12 | 121.4752755537 | 31.1519975448 | 257 | 0 | 11 | 28.3 | FDD | 344 | n1 | 152650 | 30M | 4T4R | 19 | 152650 |
| 3221967 | 13 | 121.4755898949 | 31.1490433702 | 133 | 14 | 11 | 4.4 | FDD | 991 | n1 | 152650 | 30M | 4T4R | 22 | 152650 |
| 3227764 | 2 | 121.4676463004 | 31.1495924790 | 204 | 4 | 4 | 8.5 | TDD | 933 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3233211 | 6 | 121.4682698114 | 31.1555193699 | 276 | 8 | 4 | 15.8 | TDD | 145 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3234261 | 5 | 121.4716473619 | 31.1545013651 | 204 | 2 | 11 | 15.8 | TDD | 142 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3237769 | 1 | 121.4687620259 | 31.1465175930 | 232 | 1 | 9 | 20.6 | TDD | 419 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3242940 | 10 | 121.4737918319 | 31.1468935074 | 305 | 3 | 5 | 16.4 | FDD | 273 | n1 | 152650 | 30M | 4T4R | 15 | 152650 |
| 3252802 | 9 | 121.4648691952 | 31.1471227589 | 326 | 12 | 3 | 18.2 | FDD | 369 | n1 | 152650 | 30M | 4T4R | 29 | 152650 |
| 3260613 | 8 | 121.4724583610 | 31.1551292721 | 272 | 14 | 2 | 9.3 | FDD | 554 | n1 | 152650 | 30M | 4T4R | 12 | 152650 |
| 3262239 | 11 | 121.4695704003 | 31.1447651020 | 354 | 10 | 2 | 17.4 | FDD | 916 | n1 | 152650 | 30M | 4T4R | 15 | 152650 |
| 3262293 | 7 | 121.4755697035 | 31.1551728451 | 221 | 12 | 10 | 3.6 | FDD | 386 | n1 | 152650 | 30M | 4T4R | 22 | 152650 |
| 3269902 | 3 | 121.4730053502 | 31.1528406548 | 124 | 12 | 3 | 25.3 | TDD | 200 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:31.492 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.515 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.623 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.623 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.383 | NREventA2 | measId:1;ServCellPCI:602;Se... |
| 2024-09-20 22:21:35.511 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.714 | NREventA5 | measId:3;ServCellPCI:602;Se... |
| 2024-09-20 22:21:35.756 | NRHandoverAttempt | SourcePCI:602;SourceNR-ARFC... |
| 2024-09-20 22:21:35.784 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.798 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:35.911 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.911 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3237769 | 1 | 11.8027 | 8.6835 | -117.2839 | 14.2257 | 170.5146 | 0.0150 | 0.0042 |
| 2024_09_20 22:00 | 3227764 | 2 | 9.9283 | 13.7344 | -114.8110 | 8.2486 | 106.0546 | 0.0130 | 0.0038 |
| 2024_09_20 22:00 | 3269902 | 3 | 15.5939 | 14.8608 | -117.0282 | 9.8835 | 163.8909 | 0.0002 | 0.0105 |
| 2024_09_20 22:00 | 3212393 | 4 | 9.5092 | 5.9722 | -115.7956 | 16.7714 | 149.2704 | 0.0099 | 0.0048 |
| 2024_09_20 22:00 | 3234261 | 5 | 6.4926 | 7.8302 | -116.3418 | 14.6689 | 162.4751 | 0.0102 | 0.0024 |
| 2024_09_20 22:00 | 3233211 | 6 | 15.7729 | 7.0412 | -117.9495 | 19.7856 | 185.0037 | 0.0135 | 0.0055 |
| 2024_09_20 22:00 | 3262293 | 7 | 6.2747 | 15.9290 | -116.8205 | 3.2968 | 43.3403 | 0.0040 | 0.0046 |
| 2024_09_20 22:00 | 3260613 | 8 | 7.2591 | 12.1590 | -114.4137 | 3.9500 | 29.7909 | 0.0193 | 0.0095 |
| 2024_09_20 22:00 | 3252802 | 9 | 17.5853 | 14.5649 | -116.8101 | 4.6850 | 49.7121 | 0.0171 | 0.0090 |
| 2024_09_20 22:00 | 3242940 | 10 | 16.7337 | 14.9303 | -114.6841 | 4.4482 | 49.0120 | 0.0148 | 0.0167 |
| 2024_09_20 22:00 | 3262239 | 11 | 14.3430 | 6.1671 | -115.6507 | 3.4093 | 38.6815 | 0.0010 | 0.0196 |
| 2024_09_20 22:00 | 3216770 | 12 | 17.2866 | 5.3337 | -114.4819 | 3.4366 | 28.6370 | 0.0000 | 0.0191 |
| 2024_09_20 22:00 | 3221967 | 13 | 11.5757 | 19.3167 | -114.5596 | 4.1014 | 20.4953 | 0.0045 | 0.0195 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413750_FA5E4287 | 504990 | 145 | -94.1 | 504990 | 419 | -90.3 | 504990 | 11 | -94.4 | 504990 | 200 |
| MR_1774413750_EA5D58F9 | 152650 | 916 | -95.4 | 152650 | 369 | -100.7 | 152650 | 344 | -104.5 | 152650 | 273 |
| MR_1774413750_69582529 | 152650 | 916 | -94.5 | 152650 | 369 | -100.9 | 152650 | 344 | -107.5 | 152650 | 273 |
| MR_1774413750_D3905AAE | 152650 | 916 | -94.5 | 152650 | 369 | -103.2 | 152650 | 344 | -104.9 | 152650 | 273 |
| MR_1774413750_769B43DD | 504990 | 145 | -96.1 | 504990 | 419 | -91.5 | 504990 | 11 | -95.9 | 504990 | 200 |
| MR_1774413750_41C953EA | 152650 | 916 | -95.2 | 152650 | 369 | -103.8 | 152650 | 344 | -106.3 | 152650 | 273 |
| MR_1774413750_39AD410B | 152650 | 916 | -98.1 | 152650 | 369 | -101.3 | 152650 | 344 | -104.2 | 152650 | 273 |
| MR_1774413750_CFB4BD1D | 152650 | 916 | -96.4 | 152650 | 369 | -104.2 | 152650 | 344 | -108.0 | 152650 | 273 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 445: `db674175-94d...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `db674175-94d6-4040-b142-be728f37d16a` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[445] topology](images/test_0445.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3250889_3 by 6 degrees
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3249829_2
- `C3`: Increase transmission power for 3250889_3
- `C4`: Add neighbor relationship between 3250889_3 and 3249829_2
- `C5`: Press down the tilt angle of 3250889_3 by 6 degrees
- `C6`: Insufficient data; more data is needed for judgment.
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3250889_3
- `C8`: Adjust the azimuth of 3250889_3 by 35 degrees
- `C9`: Increase A3 Offset threshold for 3250889_3
- `C10`: Increase A3 Offset threshold for 3249829_2
- `C11`: Decrease A3 Offset threshold for 3250889_3
- `C12`: Lift the tilt angle  of 3249829_2 by 10 degrees
- `C13`: Decrease A3 Offset threshold for 3249829_2
- `C14`: Adjust the azimuth of 3249829_2 by 50 degrees
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3250889_3
- `C16`: Increase transmission power for 3249829_2
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3249829_2
- `C18`: Press down the tilt angle  of 3249829_2 by 10 degrees
- `C19`: Decrease transmission power for 3250889_3
- `C20`: Decrease transmission power for 3249829_2
- `C21`: Check test server and transmission issues
- `C22`: Add neighbor relationship between 3274619_1 and 3249829_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.326 | MS1 | 121.4656670356 | 31.1446180461 | 467 | 504990 | -91.57 | 14.16 | 367.42 | 0.02 | 2.39 | 1589 |
| 2024-09-20 22:21:32.257 | MS1 | 121.4656594443 | 31.1446357297 | 467 | 504990 | -85.91 | 16.74 | 584.75 | 0.08 | 2.06 | 1569 |
| 2024-09-20 22:21:33.698 | MS1 | 121.4656691939 | 31.1446333085 | 467 | 504990 | -89.04 | 12.91 | 381.12 | 0.09 | 2.90 | 1594 |
| 2024-09-20 22:21:34.826 | MS1 | 121.4656772115 | 31.1446324983 | 467 | 504990 | -86.87 | 13.59 | 85.00 | 0.11 | 2.45 | 352 |
| 2024-09-20 22:21:35.234 | MS1 | 121.4656614202 | 31.1446364543 | 467 | 504990 | -85.91 | 17.50 | 69.30 | 0.11 | 2.54 | 496 |
| 2024-09-20 22:21:36.680 | MS1 | 121.4656659460 | 31.1446352437 | 467 | 504990 | -85.68 | 17.28 | 98.11 | 0.11 | 2.98 | 498 |
| 2024-09-20 22:21:37.456 | MS1 | 121.4656658070 | 31.1446315389 | 467 | 504990 | -93.76 | 12.21 | 58.15 | 0.19 | 2.66 | 480 |
| 2024-09-20 22:21:38.299 | MS1 | 121.4656694986 | 31.1446230817 | 467 | 504990 | -90.93 | 11.24 | 49.12 | 0.03 | 2.95 | 337 |
| 2024-09-20 22:21:39.654 | MS1 | 121.4656687430 | 31.1446346644 | 467 | 504990 | -89.99 | 9.77 | 84.14 | 0.09 | 2.40 | 491 |
| 2024-09-20 22:21:40.591 | MS1 | 121.4656647282 | 31.1446357434 | 467 | 504990 | -90.66 | 7.77 | 482.46 | 0.13 | 2.84 | 1573 |
| 2024-09-20 22:21:41.399 | MS1 | 121.4656631872 | 31.1446257978 | 467 | 504990 | -92.38 | 8.04 | 315.58 | 0.12 | 2.70 | 1584 |
| 2024-09-20 22:21:42.310 | MS1 | 121.4656701063 | 31.1446318355 | 467 | 504990 | -89.31 | 8.28 | 369.70 | 0.11 | 2.27 | 1577 |

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
| 3248453 | 4 | 121.4752964972 | 31.1552595233 | 132 | 9 | 12 | 28.0 | TDD | 807 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3249829 | 2 | 121.4733972812 | 31.1495613190 | 65 | 12 | 9 | 22.4 | TDD | 355 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3250889 | 3 | 121.4645496860 | 31.1498027617 | 205 | 3 | 8 | 33.1 | TDD | 467 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3274619 | 1 | 121.4690087986 | 31.1543212881 | 124 | 4 | 1 | 37.9 | TDD | 654 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |

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
| 2024-09-20 22:21:31.362 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.380 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.528 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.528 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.204 | NREventA3 | measId:2;ServCellPCI:517;Se... |
| 2024-09-20 22:21:38.444 | NRHandoverAttempt | SourcePCI:517;SourceNR-ARFC... |
| 2024-09-20 22:21:38.488 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.500 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.648 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.648 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3274619 | 1 | 9.1017 | 8.2505 | -115.6680 | 8.7583 | 189.0380 | 0.0191 | 0.0145 |
| 2024_09_20 22:00 | 3249829 | 2 | 7.9925 | 17.2764 | -117.6035 | 6.9504 | 89.9212 | 0.0060 | 0.0049 |
| 2024_09_20 22:00 | 3250889 | 3 | 7.3501 | 5.5634 | -115.6186 | 8.6728 | 194.2247 | 0.0054 | 0.0096 |
| 2024_09_20 22:00 | 3248453 | 4 | 13.3978 | 13.5848 | -115.1858 | 19.4742 | 134.2679 | 0.0027 | 0.0062 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415732_65B81F47 | 504990 | 467 | -87.6 | 504990 | 355 | -93.0 | 504990 | 654 | -95.9 | 504990 | 807 |
| MR_1774415732_1AA593FE | 504990 | 467 | -87.4 | 504990 | 355 | -92.5 | 504990 | 654 | -95.2 | 504990 | 807 |
| MR_1774415732_1B750073 | 504990 | 467 | -85.1 | 504990 | 355 | -91.6 | 504990 | 654 | -95.7 | 504990 | 807 |
| MR_1774415732_8624288B | 504990 | 467 | -87.0 | 504990 | 355 | -93.2 | 504990 | 654 | -96.2 | 504990 | 807 |
| MR_1774415732_C9A4F507 | 504990 | 467 | -85.3 | 504990 | 355 | -92.0 | 504990 | 654 | -93.4 | 504990 | 807 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 446: `98d94e6f-74d...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `98d94e6f-74db-4933-ac1e-c1b48c452d7d` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[446] topology](images/test_0446.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3240982_1
- `C2`: Increase transmission power for 3236509_2
- `C3`: Lift the tilt angle  of 3236509_2 by 10 degrees
- `C4`: Decrease transmission power for 3236509_2
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3236509_2
- `C6`: Insufficient data; more data is needed for judgment.
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3240982_1
- `C8`: Increase A3 Offset threshold for 3240982_1
- `C9`: Adjust the azimuth of 3236509_2 by 0 degrees
- `C10`: Press down the tilt angle  of 3236509_2 by 10 degrees
- `C11`: Press down the tilt angle of 3240982_1 by 6 degrees
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3240982_1
- `C13`: Decrease A3 Offset threshold for 3236509_2
- `C14`: Decrease transmission power for 3240982_1
- `C15`: Check test server and transmission issues
- `C16`: Lift the tilt angle of 3240982_1 by 6 degrees
- `C17`: Increase A3 Offset threshold for 3236509_2
- `C18`: Adjust the azimuth of 3240982_1 by 50 degrees
- `C19`: Add neighbor relationship between 3240982_1 and 3236509_2
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3236509_2
- `C21`: Decrease A3 Offset threshold for 3240982_1
- `C22`: Add neighbor relationship between 3240826_4 and 3236509_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.592 | MS1 | 121.4656660470 | 31.1446318114 | 1 | 504990 | -81.57 | 12.69 | 341.05 | 0.09 | 2.09 | 1598 |
| 2024-09-20 22:21:32.401 | MS1 | 121.4656645994 | 31.1446237152 | 1 | 504990 | -77.38 | 16.14 | 464.91 | 0.04 | 2.71 | 1577 |
| 2024-09-20 22:21:33.806 | MS1 | 121.4656735340 | 31.1446184105 | 1 | 504990 | -79.38 | 12.27 | 408.34 | 0.04 | 2.07 | 1561 |
| 2024-09-20 22:21:34.783 | MS1 | 121.4656609607 | 31.1446270902 | 1 | 504990 | -86.67 | -3.41 | 57.01 | 0.04 | 1.45 | 1576 |
| 2024-09-20 22:21:35.771 | MS1 | 121.4656619159 | 31.1446285243 | 1 | 504990 | -90.77 | -1.09 | 33.66 | 0.14 | 1.33 | 1581 |
| 2024-09-20 22:21:36.546 | MS1 | 121.4656679032 | 31.1446302328 | 1 | 504990 | -91.97 | -3.05 | 62.53 | 0.00 | 1.16 | 1573 |
| 2024-09-20 22:21:37.499 | MS1 | 121.4656746459 | 31.1446260137 | 1 | 504990 | -84.26 | -3.23 | 58.63 | 0.03 | 1.39 | 1585 |
| 2024-09-20 22:21:38.680 | MS1 | 121.4656712206 | 31.1446313507 | 1 | 504990 | -85.76 | -0.17 | 41.00 | 0.02 | 1.12 | 1592 |
| 2024-09-20 22:21:39.246 | MS1 | 121.4656768882 | 31.1446260530 | 753 | 504990 | -83.07 | 14.53 | 276.44 | 0.19 | 1.12 | 1577 |
| 2024-09-20 22:21:40.232 | MS1 | 121.4656600658 | 31.1446239737 | 753 | 504990 | -83.20 | 13.52 | 436.08 | 0.16 | 2.14 | 1592 |
| 2024-09-20 22:21:41.467 | MS1 | 121.4656746490 | 31.1446224987 | 753 | 504990 | -76.39 | 13.63 | 334.84 | 0.01 | 2.04 | 1576 |
| 2024-09-20 22:21:42.523 | MS1 | 121.4656604437 | 31.1446370458 | 753 | 504990 | -83.79 | 15.85 | 464.79 | 0.19 | 2.84 | 1570 |

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
| 3220309 | 3 | 121.4749966053 | 31.1491047353 | 19 | 3 | 1 | 41.6 | TDD | 390 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3236509 | 2 | 121.4700640085 | 31.1525286472 | 205 | 13 | 6 | 36.5 | TDD | 753 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3240826 | 4 | 121.4726493367 | 31.1491456422 | 250 | 8 | 2 | 27.6 | TDD | 159 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3240982 | 1 | 121.4738715527 | 31.1453155846 | 354 | 3 | 0 | 41.4 | TDD | 1 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |

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
| 2024-09-20 22:21:31.449 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.469 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.600 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.600 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.269 | NREventA3 | measId:2;ServCellPCI:606;Se... |
| 2024-09-20 22:21:38.509 | NRHandoverAttempt | SourcePCI:606;SourceNR-ARFC... |
| 2024-09-20 22:21:38.541 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.553 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.681 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.681 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3240982 | 1 | 5.2365 | 16.9565 | -114.8340 | 10.5964 | 190.0295 | 0.0053 | 0.1967 |
| 2024_09_20 22:00 | 3236509 | 2 | 18.0642 | 12.5269 | -117.9419 | 15.0836 | 83.0495 | 0.0194 | 0.0178 |
| 2024_09_20 22:00 | 3220309 | 3 | 17.0754 | 13.6187 | -117.2355 | 6.0879 | 108.6993 | 0.0098 | 0.0019 |
| 2024_09_20 22:00 | 3240826 | 4 | 17.4897 | 16.0894 | -114.1714 | 16.1372 | 176.3625 | 0.0076 | 0.0019 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412679_C3DFBE06 | 504990 | 1 | -87.0 | 504990 | 753 | -81.2 | 504990 | 159 | -82.8 | 504990 | 390 |
| MR_1774412679_8E2D1A37 | 504990 | 753 | -81.4 | 504990 | 1 | -87.6 | 504990 | 159 | -81.3 | 504990 | 390 |
| MR_1774412679_01704886 | 504990 | 1 | -85.0 | 504990 | 753 | -81.7 | 504990 | 159 | -79.6 | 504990 | 390 |
| MR_1774412679_0906750E | 504990 | 1 | -85.9 | 504990 | 753 | -78.4 | 504990 | 159 | -82.5 | 504990 | 390 |
| MR_1774412679_1F6F2815 | 504990 | 1 | -86.1 | 504990 | 753 | -78.6 | 504990 | 159 | -80.8 | 504990 | 390 |
| MR_1774412679_7A4F2623 | 504990 | 1 | -87.5 | 504990 | 753 | -78.5 | 504990 | 159 | -81.2 | 504990 | 390 |
| MR_1774412679_5AF40036 | 504990 | 1 | -85.9 | 504990 | 753 | -79.3 | 504990 | 159 | -80.2 | 504990 | 390 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 447: `4108db9f-92e...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `4108db9f-92e9-4d1a-8e71-02bb23e8e909` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[447] topology](images/test_0447.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3218552_4
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3269013_1
- `C3`: Lift the tilt angle of 3218552_4 by 3 degrees
- `C4`: Decrease A3 Offset threshold for 3269013_1
- `C5`: Press down the tilt angle of 3218552_4 by 3 degrees
- `C6`: Adjust the azimuth of 3240379_2 by 41 degrees
- `C7`: Increase A3 Offset threshold for 3218552_4
- `C8`: Adjust the azimuth of 3218552_4 by 7 degrees
- `C9`: Decrease A3 Offset threshold for 3218552_4
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3269013_1
- `C11`: Add neighbor relationship between 3240379_2 and 3269013_1
- `C12`: Check test server and transmission issues
- `C13`: Add neighbor relationship between 3218552_4 and 3269013_1
- `C14`: Increase transmission power for 3269013_1
- `C15`: Increase A3 Offset threshold for 3269013_1
- `C16`: Press down the tilt angle  of 3240379_2 by 9 degrees
- `C17`: Insufficient data; more data is needed for judgment.
- `C18`: Increase transmission power for 3218552_4
- `C19`: Decrease transmission power for 3269013_1
- `C20`: Lift the tilt angle  of 3240379_2 by 9 degrees
- `C21`: Decrease transmission power for 3218552_4
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3218552_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.493 | MS1 | 121.4656582209 | 31.1446359715 | 535 | 504990 | -87.22 | 14.26 | 471.45 | 0.11 | 2.49 | 1566 |
| 2024-09-20 22:21:32.380 | MS1 | 121.4656736353 | 31.1446251777 | 535 | 504990 | -88.20 | 16.01 | 578.02 | 0.14 | 2.01 | 1599 |
| 2024-09-20 22:21:33.651 | MS1 | 121.4656737640 | 31.1446352344 | 535 | 504990 | -89.57 | 14.30 | 435.88 | 0.12 | 2.92 | 1594 |
| 2024-09-20 22:21:34.280 | MS1 | 121.4656696386 | 31.1446346541 | 535 | 504990 | -85.78 | 16.29 | 68.71 | 0.06 | 2.30 | 1580 |
| 2024-09-20 22:21:35.249 | MS1 | 121.4656662385 | 31.1446227393 | 535 | 504990 | -89.92 | 15.79 | 92.26 | 0.07 | 2.71 | 1572 |
| 2024-09-20 22:21:36.592 | MS1 | 121.4656616300 | 31.1446188416 | 535 | 504990 | -85.37 | 13.71 | 75.96 | 0.17 | 2.22 | 1594 |
| 2024-09-20 22:21:37.931 | MS1 | 121.4656685815 | 31.1446274034 | 535 | 504990 | -89.78 | 11.29 | 72.19 | 0.05 | 2.08 | 1578 |
| 2024-09-20 22:21:38.355 | MS1 | 121.4656665696 | 31.1446351107 | 535 | 504990 | -92.08 | 8.93 | 60.78 | 0.04 | 2.79 | 1565 |
| 2024-09-20 22:21:39.853 | MS1 | 121.4656630890 | 31.1446235872 | 535 | 504990 | -90.57 | 7.27 | 62.31 | 0.19 | 2.27 | 1579 |
| 2024-09-20 22:21:40.954 | MS1 | 121.4656742615 | 31.1446327506 | 535 | 504990 | -93.16 | 11.79 | 422.61 | 0.08 | 2.95 | 1590 |
| 2024-09-20 22:21:41.633 | MS1 | 121.4656695874 | 31.1446195135 | 535 | 504990 | -91.20 | 9.22 | 341.09 | 0.03 | 2.13 | 1596 |
| 2024-09-20 22:21:42.674 | MS1 | 121.4656721942 | 31.1446305132 | 535 | 504990 | -92.52 | 8.81 | 484.13 | 0.07 | 2.71 | 1590 |

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
| 3218552 | 4 | 121.4738868530 | 31.1529501988 | 227 | 2 | 6 | 15.1 | TDD | 535 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3240379 | 2 | 121.4666849051 | 31.1467514112 | 90 | 10 | 5 | 34.0 | TDD | 178 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3262459 | 3 | 121.4712089970 | 31.1519125138 | 248 | 10 | 2 | 20.2 | TDD | 363 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3269013 | 1 | 121.4686526170 | 31.1450718729 | 301 | 3 | 6 | 32.8 | TDD | 240 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |

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
| 2024-09-20 22:21:31.279 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.304 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.406 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.406 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.134 | NREventA3 | measId:2;ServCellPCI:629;Se... |
| 2024-09-20 22:21:38.374 | NRHandoverAttempt | SourcePCI:629;SourceNR-ARFC... |
| 2024-09-20 22:21:38.415 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.429 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.546 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.546 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3269013 | 1 | 14.9442 | 12.3240 | -115.0536 | 19.2957 | 198.1623 | 0.0119 | 0.0061 |
| 2024_09_20 22:00 | 3240379 | 2 | 15.7123 | 14.9085 | -115.8600 | 18.0486 | 145.1216 | 0.0132 | 0.0167 |
| 2024_09_20 22:00 | 3262459 | 3 | 9.6235 | 6.8292 | -115.7227 | 7.9887 | 126.4527 | 0.0144 | 0.0058 |
| 2024_09_20 22:00 | 3218552 | 4 | 85.7312 | 89.5357 | -116.4134 | 15.4674 | 113.1162 | 0.0051 | 0.0076 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413518_652737CA | 504990 | 535 | -85.2 | 504990 | 240 | -87.3 | 504990 | 178 | -100.4 | 504990 | 363 |
| MR_1774413518_6BD6418E | 504990 | 535 | -87.2 | 504990 | 240 | -86.3 | 504990 | 178 | -99.4 | 504990 | 363 |
| MR_1774413518_B91CAD2F | 504990 | 535 | -84.7 | 504990 | 240 | -86.1 | 504990 | 178 | -99.4 | 504990 | 363 |
| MR_1774413518_FEBF2487 | 504990 | 535 | -86.4 | 504990 | 240 | -87.4 | 504990 | 178 | -101.2 | 504990 | 363 |
| MR_1774413518_E4DD7CB5 | 504990 | 535 | -86.3 | 504990 | 240 | -85.6 | 504990 | 178 | -99.4 | 504990 | 363 |
| MR_1774413518_37D2EF77 | 504990 | 535 | -84.4 | 504990 | 240 | -87.6 | 504990 | 178 | -100.9 | 504990 | 363 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 448: `0398bf0e-df2...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `0398bf0e-df2c-4049-a2d9-792a45ae49d4` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[448] topology](images/test_0448.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3233455_1
- `C2`: Insufficient data; more data is needed for judgment.
- `C3`: Add neighbor relationship between 3226573_2 and 3233455_1
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3247392_4
- `C5`: Adjust the azimuth of 3233455_1 by 50 degrees
- `C6`: Lift the tilt angle of 3247392_4 by 8 degrees
- `C7`: Decrease A3 Offset threshold for 3233455_1
- `C8`: Increase transmission power for 3247392_4
- `C9`: Press down the tilt angle of 3247392_4 by 8 degrees
- `C10`: Increase A3 Offset threshold for 3247392_4
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3247392_4
- `C12`: Adjust the azimuth of 3247392_4 by 50 degrees
- `C13`: Increase A3 Offset threshold for 3233455_1
- `C14`: Decrease A3 Offset threshold for 3247392_4
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3233455_1
- `C16`: Add neighbor relationship between 3247392_4 and 3233455_1
- `C17`: Decrease transmission power for 3247392_4
- `C18`: Press down the tilt angle  of 3233455_1 by 10 degrees
- `C19`: Lift the tilt angle  of 3233455_1 by 10 degrees
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3233455_1
- `C21`: Increase transmission power for 3233455_1
- `C22`: Check test server and transmission issues

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.926 | MS1 | 121.4656774457 | 31.1446371627 | 907 | 504990 | -79.98 | 17.43 | 427.25 | 0.08 | 2.48 | 1598 |
| 2024-09-20 22:21:32.888 | MS1 | 121.4656748411 | 31.1446277910 | 907 | 504990 | -80.92 | 15.67 | 421.35 | 0.01 | 2.66 | 1579 |
| 2024-09-20 22:21:33.814 | MS1 | 121.4656757548 | 31.1446188869 | 907 | 504990 | -78.27 | 12.72 | 480.94 | 0.16 | 2.49 | 1574 |
| 2024-09-20 22:21:34.739 | MS1 | 121.4656636178 | 31.1446320767 | 907 | 504990 | -84.63 | -0.36 | 63.19 | 0.06 | 1.44 | 1582 |
| 2024-09-20 22:21:35.366 | MS1 | 121.4656621317 | 31.1446298227 | 907 | 504990 | -86.37 | -1.95 | 33.93 | 0.17 | 1.46 | 1569 |
| 2024-09-20 22:21:36.762 | MS1 | 121.4656624982 | 31.1446273186 | 907 | 504990 | -88.10 | -0.85 | 64.07 | 0.15 | 1.29 | 1588 |
| 2024-09-20 22:21:37.168 | MS1 | 121.4656673630 | 31.1446280218 | 907 | 504990 | -84.67 | -1.43 | 64.30 | 0.04 | 1.37 | 1594 |
| 2024-09-20 22:21:38.822 | MS1 | 121.4656656025 | 31.1446287165 | 907 | 504990 | -85.44 | -2.28 | 74.18 | 0.14 | 1.14 | 1566 |
| 2024-09-20 22:21:39.992 | MS1 | 121.4656641092 | 31.1446194061 | 571 | 504990 | -78.59 | 15.57 | 210.61 | 0.19 | 1.13 | 1563 |
| 2024-09-20 22:21:40.993 | MS1 | 121.4656605753 | 31.1446326557 | 571 | 504990 | -79.31 | 16.63 | 582.34 | 0.13 | 2.05 | 1574 |
| 2024-09-20 22:21:41.675 | MS1 | 121.4656642202 | 31.1446268121 | 571 | 504990 | -82.14 | 13.52 | 424.49 | 0.14 | 2.36 | 1568 |
| 2024-09-20 22:21:42.382 | MS1 | 121.4656645392 | 31.1446290685 | 571 | 504990 | -79.90 | 17.05 | 509.75 | 0.18 | 2.47 | 1585 |

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
| 3226573 | 2 | 121.4664155647 | 31.1454113398 | 121 | 14 | 9 | 16.2 | TDD | 843 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3233455 | 1 | 121.4729251071 | 31.1524078910 | 304 | 8 | 11 | 43.1 | TDD | 571 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3247392 | 4 | 121.4759463734 | 31.1474560287 | 190 | 5 | 7 | 47.2 | TDD | 907 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3278534 | 3 | 121.4722408024 | 31.1483798986 | 233 | 0 | 7 | 33.2 | TDD | 123 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:31.078 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.101 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.221 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.221 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.971 | NREventA3 | measId:2;ServCellPCI:927;Se... |
| 2024-09-20 22:21:38.211 | NRHandoverAttempt | SourcePCI:927;SourceNR-ARFC... |
| 2024-09-20 22:21:38.253 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.263 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.371 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.371 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3233455 | 1 | 10.2718 | 5.0187 | -115.4464 | 19.5110 | 172.1144 | 0.0093 | 0.0171 |
| 2024_09_20 22:00 | 3226573 | 2 | 13.1347 | 19.6090 | -114.7485 | 16.4950 | 197.8558 | 0.0158 | 0.0051 |
| 2024_09_20 22:00 | 3278534 | 3 | 10.6062 | 7.6406 | -114.2900 | 17.0216 | 163.0556 | 0.0023 | 0.0118 |
| 2024_09_20 22:00 | 3247392 | 4 | 13.4250 | 16.2031 | -115.5907 | 9.2892 | 111.2427 | 0.0056 | 0.1793 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415367_68B545DE | 504990 | 571 | -80.5 | 504990 | 907 | -83.6 | 504990 | 843 | -83.6 | 504990 | 123 |
| MR_1774415367_3F8F3DEF | 504990 | 907 | -82.9 | 504990 | 571 | -79.6 | 504990 | 843 | -84.8 | 504990 | 123 |
| MR_1774415367_FDF2270F | 504990 | 571 | -81.1 | 504990 | 907 | -85.8 | 504990 | 843 | -83.0 | 504990 | 123 |
| MR_1774415367_2A92DEA0 | 504990 | 907 | -85.2 | 504990 | 571 | -82.2 | 504990 | 843 | -82.4 | 504990 | 123 |
| MR_1774415367_46B45913 | 504990 | 571 | -80.7 | 504990 | 907 | -85.0 | 504990 | 843 | -81.9 | 504990 | 123 |
| MR_1774415367_430660A8 | 504990 | 907 | -85.3 | 504990 | 571 | -81.2 | 504990 | 843 | -84.2 | 504990 | 123 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 449: `b33a9a1e-d85...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `b33a9a1e-d851-4b55-8e6e-0d5b3658834d` |
| Tag | **single-answer** |
| 정답 | *(비공개)* |

**시각화 (기지국 배치 + UE 시계열)**

![test[449] topology](images/test_0449.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3263083_2
- `C2`: Adjust the azimuth of 3263083_2 by 50 degrees
- `C3`: Lift the tilt angle of 3212092_4 by 7 degrees
- `C4`: Decrease A3 Offset threshold for 3212092_4
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3263083_2
- `C6`: Decrease transmission power for 3212092_4
- `C7`: Add neighbor relationship between 3212092_4 and 3263083_2
- `C8`: Check test server and transmission issues
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3263083_2
- `C10`: Increase transmission power for 3212092_4
- `C11`: Add neighbor relationship between 3271207_3 and 3263083_2
- `C12`: Decrease A3 Offset threshold for 3263083_2
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3212092_4
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3212092_4
- `C15`: Adjust the azimuth of 3212092_4 by 50 degrees
- `C16`: Increase transmission power for 3263083_2
- `C17`: Decrease transmission power for 3263083_2
- `C18`: Lift the tilt angle  of 3263083_2 by 10 degrees
- `C19`: Press down the tilt angle of 3212092_4 by 7 degrees
- `C20`: Increase A3 Offset threshold for 3212092_4
- `C21`: Press down the tilt angle  of 3263083_2 by 10 degrees
- `C22`: Insufficient data; more data is needed for judgment.

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.929 | MS1 | 121.4656604034 | 31.1446371852 | 313 | 504990 | -81.48 | 16.62 | 345.68 | 0.13 | 2.57 | 1562 |
| 2024-09-20 22:21:32.876 | MS1 | 121.4656603197 | 31.1446243337 | 313 | 504990 | -75.30 | 12.81 | 492.88 | 0.07 | 2.06 | 1581 |
| 2024-09-20 22:21:33.490 | MS1 | 121.4656778709 | 31.1446377746 | 313 | 504990 | -76.45 | 15.59 | 324.42 | 0.01 | 2.46 | 1579 |
| 2024-09-20 22:21:34.413 | MS1 | 121.4656735782 | 31.1446290739 | 313 | 504990 | -92.64 | -0.63 | 58.81 | 0.06 | 1.17 | 1571 |
| 2024-09-20 22:21:35.512 | MS1 | 121.4656584859 | 31.1446222534 | 313 | 504990 | -83.04 | -0.95 | 64.18 | 0.20 | 1.25 | 1569 |
| 2024-09-20 22:21:36.717 | MS1 | 121.4656666408 | 31.1446228738 | 313 | 504990 | -85.27 | -3.44 | 24.40 | 0.02 | 1.29 | 1583 |
| 2024-09-20 22:21:37.574 | MS1 | 121.4656715460 | 31.1446359054 | 313 | 504990 | -90.03 | -3.19 | 41.11 | 0.18 | 1.13 | 1575 |
| 2024-09-20 22:21:38.364 | MS1 | 121.4656718835 | 31.1446262495 | 313 | 504990 | -91.30 | -1.44 | 59.81 | 0.13 | 1.43 | 1590 |
| 2024-09-20 22:21:39.202 | MS1 | 121.4656621197 | 31.1446339995 | 937 | 504990 | -80.73 | 17.18 | 232.80 | 0.09 | 1.36 | 1600 |
| 2024-09-20 22:21:40.927 | MS1 | 121.4656673601 | 31.1446329412 | 937 | 504990 | -81.97 | 13.27 | 504.31 | 0.06 | 2.82 | 1588 |
| 2024-09-20 22:21:41.183 | MS1 | 121.4656655151 | 31.1446273375 | 937 | 504990 | -77.97 | 14.22 | 438.73 | 0.14 | 2.64 | 1563 |
| 2024-09-20 22:21:42.197 | MS1 | 121.4656755207 | 31.1446222565 | 937 | 504990 | -84.20 | 15.75 | 388.79 | 0.18 | 2.87 | 1564 |

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
| 3212092 | 4 | 121.4719368095 | 31.1476966196 | 73 | 3 | 2 | 49.5 | TDD | 313 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3263083 | 2 | 121.4707800252 | 31.1463832487 | 308 | 10 | 9 | 18.0 | TDD | 937 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3269241 | 1 | 121.4758577138 | 31.1455814495 | 80 | 8 | 11 | 26.0 | TDD | 577 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3271207 | 3 | 121.4659030653 | 31.1540176472 | 235 | 11 | 4 | 24.6 | TDD | 918 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |

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
| 2024-09-20 22:21:30.801 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.819 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:30.954 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.954 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.634 | NREventA3 | measId:2;ServCellPCI:318;Se... |
| 2024-09-20 22:21:37.874 | NRHandoverAttempt | SourcePCI:318;SourceNR-ARFC... |
| 2024-09-20 22:21:37.920 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.930 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.051 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.051 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3269241 | 1 | 8.4409 | 19.9487 | -117.3852 | 18.7003 | 148.6999 | 0.0122 | 0.0016 |
| 2024_09_20 22:00 | 3263083 | 2 | 15.7610 | 16.1249 | -115.3845 | 10.5155 | 88.8115 | 0.0110 | 0.0046 |
| 2024_09_20 22:00 | 3271207 | 3 | 14.6714 | 12.7161 | -116.3055 | 18.8284 | 133.5314 | 0.0070 | 0.0148 |
| 2024_09_20 22:00 | 3212092 | 4 | 17.9247 | 14.1526 | -115.8167 | 5.2010 | 114.6042 | 0.0013 | 0.1422 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413285_43929FB2 | 504990 | 313 | -94.2 | 504990 | 937 | -85.5 | 504990 | 918 | -89.8 | 504990 | 577 |
| MR_1774413285_A89A239F | 504990 | 313 | -91.6 | 504990 | 937 | -88.5 | 504990 | 918 | -92.7 | 504990 | 577 |
| MR_1774413285_2D640C54 | 504990 | 313 | -91.1 | 504990 | 937 | -89.0 | 504990 | 918 | -93.1 | 504990 | 577 |
| MR_1774413285_BFC9B38B | 504990 | 937 | -85.7 | 504990 | 313 | -93.6 | 504990 | 918 | -90.4 | 504990 | 577 |
| MR_1774413285_59881933 | 504990 | 313 | -90.7 | 504990 | 937 | -87.1 | 504990 | 918 | -93.6 | 504990 | 577 |
| MR_1774413285_C0654D4D | 504990 | 313 | -91.6 | 504990 | 937 | -87.7 | 504990 | 918 | -91.1 | 504990 | 577 |
| MR_1774413285_2C7882B9 | 504990 | 313 | -93.3 | 504990 | 937 | -85.8 | 504990 | 918 | -90.9 | 504990 | 577 |

> *... 2개 열 생략 (전체 14열)*

---
