# Track A 문제 분석 — train[1510]~train[1519]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[1510] ~ train[1519] (10개)

## 목차

1. [문제 1510: `8d3540ec-69f...`](#1510) — single-answer, 정답: C18
2. [문제 1511: `016845ee-b1e...`](#1511) — single-answer, 정답: C13
3. [문제 1512: `587fbf35-b72...`](#1512) — multiple-answer, 정답: C1|C21
4. [문제 1513: `b023a3ab-419...`](#1513) — single-answer, 정답: C8
5. [문제 1514: `1a77b465-896...`](#1514) — single-answer, 정답: C4
6. [문제 1515: `96cb92fa-f90...`](#1515) — single-answer, 정답: C2
7. [문제 1516: `57b14bd6-02c...`](#1516) — single-answer, 정답: C8
8. [문제 1517: `f547fc96-33d...`](#1517) — single-answer, 정답: C7
9. [문제 1518: `cba1a897-db2...`](#1518) — multiple-answer, 정답: C14|C17
10. [문제 1519: `af4a70be-beb...`](#1519) — single-answer, 정답: C17

---

### 문제 1510: `8d3540ec-69f...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `8d3540ec-69f8-4f9d-993d-93dec5c5ac5e` |
| Tag | **single-answer** |
| 정답 | **C18** |
| C18 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1510] topology](images/train_1510.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3259118_2
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3213592_1
- `C3`: Increase A3 Offset threshold for 3213592_1
- `C4`: Lift the tilt angle of 3213592_1 by 10 degrees
- `C5`: Add neighbor relationship between 3267317_3 and 3259118_2
- `C6`: Press down the tilt angle of 3213592_1 by 10 degrees
- `C7`: Add neighbor relationship between 3213592_1 and 3259118_2
- `C8`: Press down the tilt angle  of 3259118_2 by 10 degrees
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3259118_2
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3259118_2
- `C11`: Lift the tilt angle  of 3259118_2 by 10 degrees
- `C12`: Decrease A3 Offset threshold for 3259118_2
- `C13`: Increase transmission power for 3259118_2
- `C14`: Increase transmission power for 3213592_1
- `C15`: Adjust the azimuth of 3213592_1 by 17 degrees
- `C16`: Decrease transmission power for 3213592_1
- `C17`: Check test server and transmission issues
- `C18`: Insufficient data; more data is needed for judgment. **← 정답**
- `C19`: Decrease A3 Offset threshold for 3213592_1
- `C20`: Decrease transmission power for 3259118_2
- `C21`: Adjust the azimuth of 3259118_2 by 50 degrees
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3213592_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.586 | MS1 | 121.4656763397 | 31.1446215090 | 552 | 504990 | -87.20 | 16.68 | 359.90 | 0.08 | 2.79 | 1580 |
| 2024-09-20 22:21:32.202 | MS1 | 121.4656706343 | 31.1446254655 | 552 | 504990 | -85.29 | 17.92 | 468.28 | 0.13 | 2.29 | 1586 |
| 2024-09-20 22:21:33.752 | MS1 | 121.4656599023 | 31.1446183824 | 552 | 504990 | -87.42 | 13.29 | 349.54 | 0.05 | 2.99 | 1593 |
| 2024-09-20 22:21:34.234 | MS1 | 121.4656703207 | 31.1446369549 | 552 | 504990 | -91.94 | 17.62 | 53.74 | 0.01 | 2.68 | 1569 |
| 2024-09-20 22:21:35.920 | MS1 | 121.4656636092 | 31.1446252001 | 552 | 504990 | -89.83 | 14.88 | 89.27 | 0.02 | 2.31 | 1567 |
| 2024-09-20 22:21:36.472 | MS1 | 121.4656777476 | 31.1446212964 | 552 | 504990 | -86.05 | 14.74 | 77.70 | 0.07 | 2.55 | 1598 |
| 2024-09-20 22:21:37.234 | MS1 | 121.4656684044 | 31.1446356849 | 552 | 504990 | -92.97 | 7.10 | 78.36 | 0.15 | 2.96 | 1564 |
| 2024-09-20 22:21:38.170 | MS1 | 121.4656696298 | 31.1446379228 | 552 | 504990 | -90.72 | 7.18 | 64.76 | 0.01 | 2.72 | 1568 |
| 2024-09-20 22:21:39.332 | MS1 | 121.4656640909 | 31.1446248870 | 552 | 504990 | -90.06 | 7.41 | 75.55 | 0.01 | 2.15 | 1561 |
| 2024-09-20 22:21:40.507 | MS1 | 121.4656703646 | 31.1446338434 | 552 | 504990 | -92.27 | 7.53 | 405.22 | 0.13 | 2.05 | 1588 |
| 2024-09-20 22:21:41.294 | MS1 | 121.4656654301 | 31.1446334614 | 552 | 504990 | -89.40 | 9.97 | 351.69 | 0.11 | 2.41 | 1588 |
| 2024-09-20 22:21:42.638 | MS1 | 121.4656730308 | 31.1446378056 | 552 | 504990 | -89.82 | 7.79 | 426.20 | 0.04 | 2.53 | 1585 |

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
| 3213592 | 1 | 121.4678147702 | 31.1471056512 | 234 | 12 | 12 | 45.7 | TDD | 552 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3223408 | 4 | 121.4661424407 | 31.1544637314 | 273 | 7 | 3 | 37.4 | TDD | 882 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3259118 | 2 | 121.4645235282 | 31.1505538946 | 95 | 15 | 9 | 29.6 | TDD | 434 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3267317 | 3 | 121.4727936182 | 31.1534796143 | 91 | 4 | 9 | 48.2 | TDD | 996 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |

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
| 2024-09-20 22:21:31.196 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.218 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.367 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.367 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.051 | NREventA3 | measId:2;ServCellPCI:322;Se... |
| 2024-09-20 22:21:38.291 | NRHandoverAttempt | SourcePCI:322;SourceNR-ARFC... |
| 2024-09-20 22:21:38.326 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.339 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.461 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.461 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3213592 | 1 | 85.8381 | 90.6713 | -115.1040 | 19.2674 | 132.1066 | 0.0021 | 0.0168 |
| 2024_09_19 22:00 | 3259118 | 2 | 94.9353 | 94.6078 | -114.5109 | 18.4575 | 154.0984 | 0.0011 | 0.0170 |
| 2024_09_19 22:00 | 3267317 | 3 | 86.7661 | 76.1239 | -116.8960 | 16.3537 | 174.1820 | 0.0096 | 0.0168 |
| 2024_09_19 22:00 | 3223408 | 4 | 94.8535 | 82.3952 | -116.7895 | 15.1789 | 132.5047 | 0.0121 | 0.0090 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413570_FCB8AD7C | 504990 | 552 | -93.9 | 504990 | 434 | -101.9 | 504990 | 996 | -100.7 | 504990 | 882 |
| MR_1774413570_96686314 | 504990 | 552 | -90.5 | 504990 | 434 | -100.4 | 504990 | 996 | -100.4 | 504990 | 882 |
| MR_1774413570_9A28DF34 | 504990 | 552 | -90.8 | 504990 | 434 | -102.1 | 504990 | 996 | -101.7 | 504990 | 882 |
| MR_1774413570_5CDAF712 | 504990 | 552 | -93.5 | 504990 | 434 | -99.8 | 504990 | 996 | -101.9 | 504990 | 882 |
| MR_1774413570_4BDC7EE9 | 504990 | 552 | -90.1 | 504990 | 434 | -102.2 | 504990 | 996 | -100.5 | 504990 | 882 |
| MR_1774413570_A6BA765E | 504990 | 552 | -93.9 | 504990 | 434 | -102.9 | 504990 | 996 | -100.1 | 504990 | 882 |
| MR_1774413570_761F0139 | 504990 | 552 | -92.6 | 504990 | 434 | -103.1 | 504990 | 996 | -103.9 | 504990 | 882 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1511: `016845ee-b1e...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `016845ee-b1e6-48dd-bc19-99b70ef70f84` |
| Tag | **single-answer** |
| 정답 | **C13** |
| C13 의미 | Add neighbor relationship between 3269636_1 and 3234495_4 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1511] topology](images/train_1511.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3240013_2 and 3234495_4
- `C2`: Increase transmission power for 3234495_4
- `C3`: Lift the tilt angle  of 3234495_4 by 5 degrees
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3269636_1
- `C5`: Decrease A3 Offset threshold for 3269636_1
- `C6`: Decrease transmission power for 3234495_4
- `C7`: Press down the tilt angle of 3269636_1 by 10 degrees
- `C8`: Insufficient data; more data is needed for judgment.
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3269636_1
- `C10`: Adjust the azimuth of 3269636_1 by 50 degrees
- `C11`: Adjust the azimuth of 3234495_4 by 40 degrees
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3234495_4
- `C13`: Add neighbor relationship between 3269636_1 and 3234495_4 **← 정답**
- `C14`: Increase A3 Offset threshold for 3269636_1
- `C15`: Increase A3 Offset threshold for 3234495_4
- `C16`: Decrease transmission power for 3269636_1
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3234495_4
- `C18`: Check test server and transmission issues
- `C19`: Press down the tilt angle  of 3234495_4 by 5 degrees
- `C20`: Lift the tilt angle of 3269636_1 by 10 degrees
- `C21`: Decrease A3 Offset threshold for 3234495_4
- `C22`: Increase transmission power for 3269636_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.904 | MS1 | 121.4656606123 | 31.1446353966 | 633 | 504990 | -77.53 | 13.62 | 399.41 | 0.15 | 2.22 | 1599 |
| 2024-09-20 22:21:32.786 | MS1 | 121.4656760989 | 31.1446375425 | 633 | 504990 | -80.84 | 17.33 | 400.68 | 0.08 | 2.77 | 1585 |
| 2024-09-20 22:21:33.493 | MS1 | 121.4656680796 | 31.1446189612 | 633 | 504990 | -78.89 | 12.20 | 399.02 | 0.15 | 2.74 | 1566 |
| 2024-09-20 22:21:34.524 | MS1 | 121.4656588730 | 31.1446233144 | 633 | 504990 | -85.32 | -2.82 | 42.41 | 0.18 | 1.38 | 1560 |
| 2024-09-20 22:21:35.576 | MS1 | 121.4656630283 | 31.1446289826 | 633 | 504990 | -90.89 | -2.54 | 37.27 | 0.10 | 1.48 | 1561 |
| 2024-09-20 22:21:36.192 | MS1 | 121.4656599074 | 31.1446267199 | 633 | 504990 | -92.56 | -1.79 | 46.85 | 0.11 | 1.16 | 1571 |
| 2024-09-20 22:21:37.560 | MS1 | 121.4656735785 | 31.1446376682 | 633 | 504990 | -88.83 | -1.52 | 40.77 | 0.14 | 1.23 | 1579 |
| 2024-09-20 22:21:38.172 | MS1 | 121.4656663188 | 31.1446341110 | 633 | 504990 | -80.29 | 16.13 | 531.31 | 0.16 | 1.18 | 1586 |
| 2024-09-20 22:21:39.835 | MS1 | 121.4656709996 | 31.1446369264 | 633 | 504990 | -82.15 | 17.43 | 378.35 | 0.15 | 1.40 | 1595 |
| 2024-09-20 22:21:40.860 | MS1 | 121.4656633131 | 31.1446348421 | 633 | 504990 | -79.14 | 13.40 | 519.92 | 0.13 | 2.26 | 1599 |
| 2024-09-20 22:21:41.882 | MS1 | 121.4656665302 | 31.1446349838 | 633 | 504990 | -79.46 | 17.04 | 313.07 | 0.04 | 2.13 | 1581 |
| 2024-09-20 22:21:42.256 | MS1 | 121.4656594460 | 31.1446192956 | 633 | 504990 | -83.97 | 16.17 | 555.90 | 0.03 | 2.88 | 1579 |

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
| 3234495 | 4 | 121.4706972875 | 31.1492936476 | 263 | 2 | 1 | 32.8 | TDD | 374 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3240013 | 2 | 121.4656813486 | 31.1482569946 | 347 | 9 | 11 | 20.4 | TDD | 531 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3250767 | 3 | 121.4755679047 | 31.1488293001 | 292 | 1 | 8 | 47.3 | TDD | 341 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3269636 | 1 | 121.4759443428 | 31.1532426922 | 285 | 13 | 4 | 35.7 | TDD | 633 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |

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
| 2024-09-20 22:21:31.173 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.189 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.323 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.323 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.989 | NREventA3 | measId:2;ServCellPCI:23;Ser... |
| 2024-09-20 22:21:35.989 | NREventA3 | measId:2;ServCellPCI:23;Ser... |
| 2024-09-20 22:21:36.989 | NREventA3 | measId:2;ServCellPCI:23;Ser... |
| 2024-09-20 22:21:39.489 | NRRRCReestablishAttempt | PCI:23 |
| 2024-09-20 22:21:39.502 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.517 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:39.643 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.643 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3269636 | 1 | 15.1704 | 16.1744 | -115.4608 | 16.1236 | 171.1645 | 0.0027 | 0.1850 |
| 2024_09_20 22:00 | 3240013 | 2 | 17.7915 | 16.5113 | -114.8980 | 12.9682 | 124.7405 | 0.0018 | 0.0119 |
| 2024_09_20 22:00 | 3250767 | 3 | 9.7583 | 18.4043 | -114.7626 | 19.0728 | 134.8502 | 0.0092 | 0.0100 |
| 2024_09_20 22:00 | 3234495 | 4 | 5.6504 | 6.9036 | -114.8163 | 8.7581 | 158.7647 | 0.0030 | 0.0018 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414984_9FC602E9 | 504990 | 633 | -85.6 | 504990 | 374 | -80.2 | 504990 | 531 | -86.6 | 504990 | 341 |
| MR_1774414984_8FD27A01 | 504990 | 374 | -80.6 | 504990 | 633 | -86.5 | 504990 | 531 | -86.2 | 504990 | 341 |
| MR_1774414984_25E197D8 | 504990 | 633 | -84.1 | 504990 | 374 | -80.9 | 504990 | 531 | -86.7 | 504990 | 341 |
| MR_1774414984_62BD2895 | 504990 | 374 | -81.0 | 504990 | 633 | -86.4 | 504990 | 531 | -83.7 | 504990 | 341 |
| MR_1774414984_33DF134B | 504990 | 374 | -79.1 | 504990 | 633 | -86.6 | 504990 | 531 | -86.8 | 504990 | 341 |
| MR_1774414984_17B61C06 | 504990 | 374 | -82.2 | 504990 | 633 | -85.7 | 504990 | 531 | -85.9 | 504990 | 341 |
| MR_1774414984_4342A602 | 504990 | 374 | -80.9 | 504990 | 633 | -84.6 | 504990 | 531 | -84.5 | 504990 | 341 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1512: `587fbf35-b72...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `587fbf35-b728-4d48-98aa-1d71ab944cad` |
| Tag | **multiple-answer** |
| 정답 | **C1|C21** |
| C1 의미 | Adjust the azimuth of 3244011_2 by 50 degrees |
| C21 의미 | Increase transmission power for 3244011_2 |
| 패턴 분류 | **P4 Coverage (azimuth)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1512] topology](images/train_1512.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3244011_2 by 50 degrees **← 정답**
- `C2`: Lift the tilt angle of 3244011_2 by 10 degrees
- `C3`: Press down the tilt angle  of 3248253_1 by 4 degrees
- `C4`: Check test server and transmission issues
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3248253_1
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3248253_1
- `C7`: Adjust the azimuth of 3248253_1 by 32 degrees
- `C8`: Decrease A3 Offset threshold for 3244011_2
- `C9`: Lift the tilt angle  of 3248253_1 by 4 degrees
- `C10`: Increase A3 Offset threshold for 3248253_1
- `C11`: Add neighbor relationship between 3267061_3 and 3248253_1
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3244011_2
- `C13`: Increase transmission power for 3248253_1
- `C14`: Press down the tilt angle of 3244011_2 by 10 degrees
- `C15`: Decrease transmission power for 3248253_1
- `C16`: Decrease A3 Offset threshold for 3248253_1
- `C17`: Add neighbor relationship between 3244011_2 and 3248253_1
- `C18`: Insufficient data; more data is needed for judgment.
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3244011_2
- `C20`: Increase A3 Offset threshold for 3244011_2
- `C21`: Increase transmission power for 3244011_2 **← 정답**
- `C22`: Decrease transmission power for 3244011_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.155 | MS1 | 121.4656605594 | 31.1446183791 | 975 | 504990 | -91.71 | 15.29 | 353.91 | 0.16 | 2.62 | 1600 |
| 2024-09-20 22:21:32.481 | MS1 | 121.4656587516 | 31.1446374149 | 975 | 504990 | -91.47 | 14.39 | 544.28 | 0.08 | 2.93 | 1565 |
| 2024-09-20 22:21:33.290 | MS1 | 121.4656769100 | 31.1446236169 | 975 | 504990 | -88.98 | 14.65 | 489.19 | 0.11 | 2.05 | 1564 |
| 2024-09-20 22:21:34.240 | MS1 | 121.4656590147 | 31.1446272953 | 975 | 504990 | -101.87 | 0.77 | 25.04 | 0.15 | 1.38 | 1599 |
| 2024-09-20 22:21:35.991 | MS1 | 121.4656705760 | 31.1446363103 | 975 | 504990 | -108.70 | -1.27 | 76.35 | 0.10 | 1.29 | 1593 |
| 2024-09-20 22:21:36.906 | MS1 | 121.4656593825 | 31.1446326609 | 975 | 504990 | -108.98 | -1.59 | 73.76 | 0.01 | 1.19 | 1569 |
| 2024-09-20 22:21:37.617 | MS1 | 121.4656639618 | 31.1446180850 | 975 | 504990 | -102.26 | -1.83 | 39.27 | 0.10 | 1.26 | 1579 |
| 2024-09-20 22:21:38.517 | MS1 | 121.4656749365 | 31.1446315861 | 975 | 504990 | -108.61 | 0.56 | 71.86 | 0.10 | 1.18 | 1589 |
| 2024-09-20 22:21:39.322 | MS1 | 121.4656603399 | 31.1446241425 | 975 | 504990 | -108.89 | 1.73 | 20.21 | 0.00 | 1.19 | 1581 |
| 2024-09-20 22:21:40.344 | MS1 | 121.4656646297 | 31.1446330364 | 975 | 504990 | -88.78 | 15.76 | 450.80 | 0.16 | 2.19 | 1566 |
| 2024-09-20 22:21:41.631 | MS1 | 121.4656609674 | 31.1446272018 | 975 | 504990 | -92.96 | 17.36 | 398.06 | 0.03 | 2.88 | 1570 |
| 2024-09-20 22:21:42.352 | MS1 | 121.4656770266 | 31.1446239566 | 975 | 504990 | -94.91 | 17.68 | 406.11 | 0.01 | 2.82 | 1598 |

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
| 3244011 | 2 | 121.4647581972 | 31.1465694180 | 90 | 6 | 5 | 18.3 | TDD | 975 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3248253 | 1 | 121.4696268187 | 31.1542246057 | 231 | 3 | 12 | 15.5 | TDD | 994 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3267061 | 3 | 121.4655561303 | 31.1542076462 | 247 | 13 | 9 | 38.4 | TDD | 850 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3267154 | 4 | 121.4685967981 | 31.1533144539 | 96 | 3 | 11 | 28.4 | TDD | 855 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |

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
| 2024-09-20 22:21:31.373 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.391 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.513 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.513 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.674 | NREventA2 | measId:1;ServCellPCI:607;Se... |
| 2024-09-20 22:21:34.779 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3248253 | 1 | 14.5071 | 8.7472 | -117.9627 | 8.1497 | 130.8490 | 0.0104 | 0.0046 |
| 2024_09_20 22:00 | 3244011 | 2 | 5.6665 | 9.7750 | -117.5226 | 13.5353 | 180.4558 | 0.1780 | 0.0065 |
| 2024_09_20 22:00 | 3267061 | 3 | 7.8712 | 19.6634 | -116.6798 | 15.1891 | 140.1223 | 0.0170 | 0.0172 |
| 2024_09_20 22:00 | 3267154 | 4 | 9.2240 | 12.4934 | -117.0209 | 9.0744 | 129.4829 | 0.0165 | 0.0146 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412045_C5030B47 | 504990 | 975 | -101.5 | 504990 | 994 | -105.8 | 504990 | 850 | -111.9 | 504990 | 855 |
| MR_1774412045_327F3A29 | 504990 | 975 | -100.9 | 504990 | 994 | -106.6 | 504990 | 850 | -111.8 | 504990 | 855 |
| MR_1774412045_0659A180 | 504990 | 975 | -103.8 | 504990 | 994 | -108.7 | 504990 | 850 | -110.6 | 504990 | 855 |
| MR_1774412045_84D6C436 | 504990 | 975 | -101.5 | 504990 | 994 | -108.6 | 504990 | 850 | -111.4 | 504990 | 855 |
| MR_1774412045_A36BD3CF | 504990 | 975 | -100.2 | 504990 | 994 | -105.8 | 504990 | 850 | -111.8 | 504990 | 855 |
| MR_1774412045_890D9889 | 504990 | 975 | -102.7 | 504990 | 994 | -108.3 | 504990 | 850 | -110.5 | 504990 | 855 |
| MR_1774412045_D8F9FD3F | 504990 | 975 | -100.5 | 504990 | 994 | -105.9 | 504990 | 850 | -109.6 | 504990 | 855 |
| MR_1774412045_F10F107A | 504990 | 975 | -103.6 | 504990 | 994 | -107.5 | 504990 | 850 | -111.0 | 504990 | 855 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1513: `b023a3ab-419...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `b023a3ab-4193-463f-a53f-da5bc0ea868d` |
| Tag | **single-answer** |
| 정답 | **C8** |
| C8 의미 | Decrease A3 Offset threshold for 3240590_3 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1513] topology](images/train_1513.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3240590_3
- `C2`: Press down the tilt angle  of 3272927_2 by 10 degrees
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3272927_2
- `C4`: Insufficient data; more data is needed for judgment.
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3272927_2
- `C6`: Add neighbor relationship between 3227481_1 and 3272927_2
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3240590_3
- `C8`: Decrease A3 Offset threshold for 3240590_3 **← 정답**
- `C9`: Press down the tilt angle of 3240590_3 by 10 degrees
- `C10`: Adjust the azimuth of 3272927_2 by 50 degrees
- `C11`: Increase transmission power for 3272927_2
- `C12`: Check test server and transmission issues
- `C13`: Lift the tilt angle of 3240590_3 by 10 degrees
- `C14`: Add neighbor relationship between 3240590_3 and 3272927_2
- `C15`: Decrease transmission power for 3272927_2
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3240590_3
- `C17`: Adjust the azimuth of 3240590_3 by 50 degrees
- `C18`: Lift the tilt angle  of 3272927_2 by 10 degrees
- `C19`: Increase A3 Offset threshold for 3272927_2
- `C20`: Increase A3 Offset threshold for 3240590_3
- `C21`: Decrease A3 Offset threshold for 3272927_2
- `C22`: Increase transmission power for 3240590_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.984 | MS1 | 121.4656581692 | 31.1446205280 | 111 | 504990 | -81.38 | 14.01 | 476.57 | 0.19 | 2.43 | 1582 |
| 2024-09-20 22:21:32.700 | MS1 | 121.4656625357 | 31.1446313064 | 111 | 504990 | -81.63 | 16.76 | 482.65 | 0.14 | 2.87 | 1588 |
| 2024-09-20 22:21:33.593 | MS1 | 121.4656650674 | 31.1446239013 | 111 | 504990 | -75.74 | 15.89 | 299.97 | 0.01 | 2.97 | 1572 |
| 2024-09-20 22:21:34.719 | MS1 | 121.4656664100 | 31.1446233149 | 111 | 504990 | -86.02 | -0.20 | 65.99 | 0.05 | 1.40 | 1598 |
| 2024-09-20 22:21:35.769 | MS1 | 121.4656730000 | 31.1446251808 | 111 | 504990 | -89.50 | -3.37 | 60.51 | 0.20 | 1.21 | 1577 |
| 2024-09-20 22:21:36.906 | MS1 | 121.4656586848 | 31.1446236632 | 111 | 504990 | -83.88 | -3.82 | 51.74 | 0.17 | 1.34 | 1598 |
| 2024-09-20 22:21:37.893 | MS1 | 121.4656650290 | 31.1446359532 | 111 | 504990 | -86.77 | -0.26 | 50.72 | 0.14 | 1.23 | 1600 |
| 2024-09-20 22:21:38.757 | MS1 | 121.4656746293 | 31.1446256941 | 111 | 504990 | -91.84 | -1.25 | 49.77 | 0.13 | 1.09 | 1592 |
| 2024-09-20 22:21:39.909 | MS1 | 121.4656739201 | 31.1446322193 | 12 | 504990 | -75.80 | 17.28 | 180.43 | 0.16 | 1.49 | 1582 |
| 2024-09-20 22:21:40.658 | MS1 | 121.4656746432 | 31.1446301227 | 12 | 504990 | -80.56 | 16.81 | 310.56 | 0.17 | 2.52 | 1587 |
| 2024-09-20 22:21:41.202 | MS1 | 121.4656581942 | 31.1446329491 | 12 | 504990 | -82.07 | 17.44 | 500.71 | 0.04 | 2.08 | 1570 |
| 2024-09-20 22:21:42.761 | MS1 | 121.4656759067 | 31.1446379968 | 12 | 504990 | -80.48 | 16.76 | 451.52 | 0.01 | 2.11 | 1587 |

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
| 3227481 | 1 | 121.4753849153 | 31.1444569171 | 282 | 11 | 6 | 28.1 | TDD | 128 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3240590 | 3 | 121.4729203701 | 31.1441144968 | 79 | 15 | 9 | 47.9 | TDD | 111 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3240975 | 4 | 121.4708435892 | 31.1532565244 | 47 | 8 | 2 | 17.5 | TDD | 324 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3272927 | 2 | 121.4646654561 | 31.1446422731 | 354 | 13 | 5 | 24.1 | TDD | 12 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |

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
| 2024-09-20 22:21:31.152 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.167 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.275 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.275 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.976 | NREventA3 | measId:2;ServCellPCI:530;Se... |
| 2024-09-20 22:21:38.216 | NRHandoverAttempt | SourcePCI:530;SourceNR-ARFC... |
| 2024-09-20 22:21:38.259 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.273 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.411 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.411 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3227481 | 1 | 17.7461 | 10.7880 | -116.9111 | 12.8406 | 147.9648 | 0.0066 | 0.0053 |
| 2024_09_20 22:00 | 3272927 | 2 | 15.3758 | 19.1291 | -114.6454 | 8.0190 | 157.3086 | 0.0016 | 0.0082 |
| 2024_09_20 22:00 | 3240590 | 3 | 17.0675 | 7.1548 | -114.8200 | 8.6493 | 81.2717 | 0.0183 | 0.1644 |
| 2024_09_20 22:00 | 3240975 | 4 | 14.7014 | 18.8464 | -117.8477 | 12.2176 | 81.9023 | 0.0079 | 0.0082 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415761_34A3C731 | 504990 | 111 | -84.3 | 504990 | 12 | -80.0 | 504990 | 128 | -86.5 | 504990 | 324 |
| MR_1774415761_37E8FF24 | 504990 | 12 | -81.7 | 504990 | 111 | -86.9 | 504990 | 128 | -88.3 | 504990 | 324 |
| MR_1774415761_8D4708CE | 504990 | 12 | -79.6 | 504990 | 111 | -87.3 | 504990 | 128 | -87.0 | 504990 | 324 |
| MR_1774415761_55E4E8E5 | 504990 | 111 | -84.7 | 504990 | 12 | -80.9 | 504990 | 128 | -90.1 | 504990 | 324 |
| MR_1774415761_E29395E1 | 504990 | 111 | -85.7 | 504990 | 12 | -81.0 | 504990 | 128 | -88.7 | 504990 | 324 |
| MR_1774415761_F47946F1 | 504990 | 111 | -85.2 | 504990 | 12 | -79.6 | 504990 | 128 | -87.4 | 504990 | 324 |
| MR_1774415761_B75AF125 | 504990 | 111 | -87.2 | 504990 | 12 | -80.3 | 504990 | 128 | -90.1 | 504990 | 324 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1514: `1a77b465-896...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `1a77b465-896e-4046-9517-409b8dbd0554` |
| Tag | **single-answer** |
| 정답 | **C4** |
| C4 의미 | Decrease A3 Offset threshold for 3239830_3 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1514] topology](images/train_1514.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3239830_3 by 10 degrees
- `C2`: Press down the tilt angle  of 3226196_1 by 10 degrees
- `C3`: Add neighbor relationship between 3239830_3 and 3226196_1
- `C4`: Decrease A3 Offset threshold for 3239830_3 **← 정답**
- `C5`: Increase transmission power for 3226196_1
- `C6`: Decrease transmission power for 3239830_3
- `C7`: Insufficient data; more data is needed for judgment.
- `C8`: Add neighbor relationship between 3237292_2 and 3226196_1
- `C9`: Decrease A3 Offset threshold for 3226196_1
- `C10`: Increase A3 Offset threshold for 3226196_1
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3239830_3
- `C12`: Lift the tilt angle of 3239830_3 by 10 degrees
- `C13`: Lift the tilt angle  of 3226196_1 by 10 degrees
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3226196_1
- `C15`: Increase transmission power for 3239830_3
- `C16`: Check test server and transmission issues
- `C17`: Adjust the azimuth of 3226196_1 by 50 degrees
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3226196_1
- `C19`: Adjust the azimuth of 3239830_3 by 50 degrees
- `C20`: Decrease transmission power for 3226196_1
- `C21`: Increase A3 Offset threshold for 3239830_3
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3239830_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.371 | MS1 | 121.4656581638 | 31.1446353791 | 86 | 504990 | -80.00 | 16.82 | 408.72 | 0.18 | 2.33 | 1585 |
| 2024-09-20 22:21:32.702 | MS1 | 121.4656672622 | 31.1446298251 | 86 | 504990 | -79.98 | 17.35 | 549.45 | 0.01 | 2.14 | 1568 |
| 2024-09-20 22:21:33.709 | MS1 | 121.4656721980 | 31.1446315550 | 86 | 504990 | -84.52 | 15.36 | 480.25 | 0.12 | 2.86 | 1599 |
| 2024-09-20 22:21:34.331 | MS1 | 121.4656631012 | 31.1446291126 | 86 | 504990 | -88.57 | -3.80 | 47.80 | 0.17 | 1.27 | 1586 |
| 2024-09-20 22:21:35.479 | MS1 | 121.4656680830 | 31.1446232785 | 86 | 504990 | -87.63 | -0.80 | 52.71 | 0.05 | 1.29 | 1568 |
| 2024-09-20 22:21:36.222 | MS1 | 121.4656628462 | 31.1446251552 | 86 | 504990 | -84.08 | -3.88 | 46.66 | 0.07 | 1.26 | 1574 |
| 2024-09-20 22:21:37.270 | MS1 | 121.4656759399 | 31.1446195195 | 86 | 504990 | -83.19 | -0.33 | 28.72 | 0.09 | 1.15 | 1565 |
| 2024-09-20 22:21:38.779 | MS1 | 121.4656706379 | 31.1446287084 | 86 | 504990 | -89.52 | -1.08 | 33.05 | 0.09 | 1.21 | 1574 |
| 2024-09-20 22:21:39.741 | MS1 | 121.4656597185 | 31.1446334833 | 635 | 504990 | -75.70 | 17.75 | 223.59 | 0.03 | 1.14 | 1570 |
| 2024-09-20 22:21:40.332 | MS1 | 121.4656777927 | 31.1446365242 | 635 | 504990 | -83.07 | 15.29 | 469.82 | 0.01 | 2.50 | 1581 |
| 2024-09-20 22:21:41.299 | MS1 | 121.4656708868 | 31.1446275782 | 635 | 504990 | -84.88 | 14.77 | 490.63 | 0.10 | 2.10 | 1571 |
| 2024-09-20 22:21:42.259 | MS1 | 121.4656676299 | 31.1446227003 | 635 | 504990 | -82.27 | 13.67 | 585.61 | 0.18 | 2.63 | 1566 |

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
| 3218071 | 4 | 121.4717746885 | 31.1443571518 | 346 | 15 | 11 | 21.5 | TDD | 758 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3226196 | 1 | 121.4726616518 | 31.1449706014 | 62 | 7 | 11 | 37.3 | TDD | 635 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3237292 | 2 | 121.4739682101 | 31.1522928545 | 256 | 13 | 11 | 37.3 | TDD | 964 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3239830 | 3 | 121.4678517236 | 31.1468292987 | 98 | 10 | 6 | 16.1 | TDD | 86 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |

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
| 2024-09-20 22:21:31.277 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.293 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.419 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.419 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.175 | NREventA3 | measId:2;ServCellPCI:509;Se... |
| 2024-09-20 22:21:38.415 | NRHandoverAttempt | SourcePCI:509;SourceNR-ARFC... |
| 2024-09-20 22:21:38.465 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.475 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.594 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.594 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3226196 | 1 | 8.2312 | 5.1713 | -114.9013 | 18.0538 | 167.0267 | 0.0074 | 0.0164 |
| 2024_09_20 22:00 | 3237292 | 2 | 17.3202 | 19.6363 | -117.5712 | 18.7246 | 103.0168 | 0.0065 | 0.0183 |
| 2024_09_20 22:00 | 3239830 | 3 | 9.6554 | 19.1724 | -115.3540 | 12.9502 | 120.0268 | 0.0081 | 0.1404 |
| 2024_09_20 22:00 | 3218071 | 4 | 17.4209 | 17.7142 | -117.5343 | 12.9015 | 94.1774 | 0.0110 | 0.0155 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413119_F92CD824 | 504990 | 635 | -84.0 | 504990 | 86 | -87.3 | 504990 | 964 | -87.3 | 504990 | 758 |
| MR_1774413119_329BDB73 | 504990 | 635 | -85.2 | 504990 | 86 | -88.0 | 504990 | 964 | -87.8 | 504990 | 758 |
| MR_1774413119_903A15D0 | 504990 | 635 | -83.4 | 504990 | 86 | -89.5 | 504990 | 964 | -87.8 | 504990 | 758 |
| MR_1774413119_D16824F7 | 504990 | 635 | -84.4 | 504990 | 86 | -90.1 | 504990 | 964 | -87.5 | 504990 | 758 |
| MR_1774413119_A0AA253F | 504990 | 86 | -86.7 | 504990 | 635 | -81.5 | 504990 | 964 | -90.0 | 504990 | 758 |
| MR_1774413119_181E88E7 | 504990 | 635 | -82.2 | 504990 | 86 | -87.9 | 504990 | 964 | -87.7 | 504990 | 758 |
| MR_1774413119_06846901 | 504990 | 86 | -89.2 | 504990 | 635 | -83.0 | 504990 | 964 | -89.1 | 504990 | 758 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1515: `96cb92fa-f90...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `96cb92fa-f90c-4572-999b-ecc9852c1323` |
| Tag | **single-answer** |
| 정답 | **C2** |
| C2 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1515] topology](images/train_1515.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3246716_1
- `C2`: Check test server and transmission issues **← 정답**
- `C3`: Decrease A3 Offset threshold for 3264954_4
- `C4`: Increase A3 Offset threshold for 3264954_4
- `C5`: Insufficient data; more data is needed for judgment.
- `C6`: Add neighbor relationship between 3246716_1 and 3264954_4
- `C7`: Decrease transmission power for 3246716_1
- `C8`: Decrease A3 Offset threshold for 3246716_1
- `C9`: Increase A3 Offset threshold for 3246716_1
- `C10`: Lift the tilt angle  of 3264954_4 by 6 degrees
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3246716_1
- `C12`: Press down the tilt angle  of 3264954_4 by 6 degrees
- `C13`: Add neighbor relationship between 3252275_2 and 3264954_4
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3264954_4
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3246716_1
- `C16`: Decrease transmission power for 3264954_4
- `C17`: Adjust the azimuth of 3264954_4 by 50 degrees
- `C18`: Increase transmission power for 3264954_4
- `C19`: Adjust the azimuth of 3246716_1 by 14 degrees
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3264954_4
- `C21`: Lift the tilt angle of 3246716_1 by 4 degrees
- `C22`: Press down the tilt angle of 3246716_1 by 4 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.794 | MS1 | 121.4656659590 | 31.1446366257 | 481 | 504990 | -87.86 | 14.71 | 439.96 | 0.09 | 2.44 | 1587 |
| 2024-09-20 22:21:32.859 | MS1 | 121.4656757561 | 31.1446228608 | 481 | 504990 | -85.05 | 16.56 | 554.94 | 0.10 | 2.25 | 1567 |
| 2024-09-20 22:21:33.976 | MS1 | 121.4656772426 | 31.1446258883 | 481 | 504990 | -87.89 | 14.12 | 568.68 | 0.16 | 2.69 | 1598 |
| 2024-09-20 22:21:34.245 | MS1 | 121.4656581495 | 31.1446325624 | 481 | 504990 | -91.79 | 15.93 | 98.77 | 0.12 | 2.79 | 480 |
| 2024-09-20 22:21:35.777 | MS1 | 121.4656607585 | 31.1446208716 | 481 | 504990 | -91.24 | 17.38 | 62.79 | 0.15 | 2.70 | 426 |
| 2024-09-20 22:21:36.189 | MS1 | 121.4656653201 | 31.1446347724 | 481 | 504990 | -87.31 | 14.19 | 91.15 | 0.03 | 2.07 | 488 |
| 2024-09-20 22:21:37.973 | MS1 | 121.4656671268 | 31.1446205988 | 481 | 504990 | -92.58 | 10.94 | 50.30 | 0.13 | 2.22 | 458 |
| 2024-09-20 22:21:38.127 | MS1 | 121.4656752695 | 31.1446273496 | 481 | 504990 | -89.63 | 9.72 | 59.47 | 0.12 | 2.44 | 374 |
| 2024-09-20 22:21:39.238 | MS1 | 121.4656670322 | 31.1446209183 | 481 | 504990 | -92.75 | 11.21 | 44.93 | 0.04 | 2.88 | 420 |
| 2024-09-20 22:21:40.254 | MS1 | 121.4656590074 | 31.1446230319 | 481 | 504990 | -91.50 | 10.52 | 498.55 | 0.20 | 2.89 | 1596 |
| 2024-09-20 22:21:41.298 | MS1 | 121.4656619695 | 31.1446284016 | 481 | 504990 | -90.63 | 8.67 | 470.16 | 0.08 | 2.22 | 1579 |
| 2024-09-20 22:21:42.777 | MS1 | 121.4656677830 | 31.1446332608 | 481 | 504990 | -89.21 | 7.14 | 538.44 | 0.13 | 2.47 | 1585 |

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
| 3246716 | 1 | 121.4717698706 | 31.1448486342 | 282 | 1 | 4 | 31.4 | TDD | 481 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3252275 | 2 | 121.4652017680 | 31.1480823695 | 124 | 15 | 12 | 35.5 | TDD | 266 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3255599 | 3 | 121.4698463449 | 31.1452668686 | 173 | 11 | 2 | 26.7 | TDD | 371 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3264954 | 4 | 121.4662951277 | 31.1517719439 | 9 | 3 | 2 | 40.4 | TDD | 663 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |

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
| 2024-09-20 22:21:31.277 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.410 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.410 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.119 | NREventA3 | measId:2;ServCellPCI:665;Se... |
| 2024-09-20 22:21:38.359 | NRHandoverAttempt | SourcePCI:665;SourceNR-ARFC... |
| 2024-09-20 22:21:38.390 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.404 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.524 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.524 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3246716 | 1 | 19.1112 | 18.5115 | -116.4837 | 18.5283 | 191.5365 | 0.0104 | 0.0144 |
| 2024_09_20 22:00 | 3252275 | 2 | 15.2417 | 11.1084 | -117.0605 | 13.2808 | 182.5204 | 0.0146 | 0.0125 |
| 2024_09_20 22:00 | 3255599 | 3 | 17.4046 | 15.6782 | -114.5402 | 19.9923 | 86.0636 | 0.0113 | 0.0176 |
| 2024_09_20 22:00 | 3264954 | 4 | 8.3499 | 15.8393 | -116.4053 | 5.7580 | 176.0935 | 0.0122 | 0.0183 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415363_74C998EC | 504990 | 481 | -93.3 | 504990 | 663 | -96.7 | 504990 | 266 | -98.2 | 504990 | 371 |
| MR_1774415363_C6F6B92D | 504990 | 481 | -91.5 | 504990 | 663 | -99.8 | 504990 | 266 | -97.0 | 504990 | 371 |
| MR_1774415363_5DA8B5B9 | 504990 | 481 | -93.3 | 504990 | 663 | -99.5 | 504990 | 266 | -98.4 | 504990 | 371 |
| MR_1774415363_917A9BD5 | 504990 | 481 | -90.1 | 504990 | 663 | -97.2 | 504990 | 266 | -98.5 | 504990 | 371 |
| MR_1774415363_4A9953E4 | 504990 | 481 | -92.8 | 504990 | 663 | -98.5 | 504990 | 266 | -99.3 | 504990 | 371 |
| MR_1774415363_A25553BD | 504990 | 481 | -91.5 | 504990 | 663 | -99.1 | 504990 | 266 | -100.0 | 504990 | 371 |
| MR_1774415363_2AA74BAE | 504990 | 481 | -90.9 | 504990 | 663 | -97.8 | 504990 | 266 | -98.6 | 504990 | 371 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1516: `57b14bd6-02c...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `57b14bd6-02cd-4e5b-b5ad-53ef2e5c3bb9` |
| Tag | **single-answer** |
| 정답 | **C8** |
| C8 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1516] topology](images/train_1516.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment.
- `C2`: Lift the tilt angle of 3247681_2 by 10 degrees
- `C3`: Increase transmission power for 3247681_2
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3247681_2
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3247681_2
- `C6`: Increase A3 Offset threshold for 3247681_2
- `C7`: Decrease A3 Offset threshold for 3247681_2
- `C8`: Check test server and transmission issues **← 정답**
- `C9`: Lift the tilt angle  of 3229023_1 by 10 degrees
- `C10`: Press down the tilt angle of 3247681_2 by 10 degrees
- `C11`: Increase transmission power for 3229023_1
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3229023_1
- `C13`: Adjust the azimuth of 3247681_2 by 50 degrees
- `C14`: Press down the tilt angle  of 3229023_1 by 10 degrees
- `C15`: Decrease transmission power for 3247681_2
- `C16`: Add neighbor relationship between 3267924_3 and 3229023_1
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3229023_1
- `C18`: Decrease A3 Offset threshold for 3229023_1
- `C19`: Adjust the azimuth of 3229023_1 by 50 degrees
- `C20`: Decrease transmission power for 3229023_1
- `C21`: Add neighbor relationship between 3247681_2 and 3229023_1
- `C22`: Increase A3 Offset threshold for 3229023_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.847 | MS1 | 121.4656641313 | 31.1446312193 | 596 | 504990 | -87.00 | 12.20 | 394.56 | 0.11 | 2.80 | 1575 |
| 2024-09-20 22:21:32.677 | MS1 | 121.4656755070 | 31.1446189970 | 596 | 504990 | -85.26 | 12.23 | 587.50 | 0.17 | 2.50 | 1594 |
| 2024-09-20 22:21:33.466 | MS1 | 121.4656644400 | 31.1446313907 | 596 | 504990 | -85.80 | 14.32 | 436.09 | 0.09 | 2.81 | 1562 |
| 2024-09-20 22:21:34.802 | MS1 | 121.4656742842 | 31.1446278638 | 596 | 504990 | -87.83 | 16.84 | 61.23 | 0.01 | 2.30 | 338 |
| 2024-09-20 22:21:35.121 | MS1 | 121.4656599596 | 31.1446244003 | 596 | 504990 | -87.62 | 13.31 | 74.16 | 0.17 | 2.86 | 462 |
| 2024-09-20 22:21:36.930 | MS1 | 121.4656743914 | 31.1446342218 | 596 | 504990 | -89.73 | 13.39 | 68.07 | 0.14 | 2.92 | 376 |
| 2024-09-20 22:21:37.762 | MS1 | 121.4656740861 | 31.1446257724 | 596 | 504990 | -90.23 | 8.91 | 65.79 | 0.19 | 2.75 | 437 |
| 2024-09-20 22:21:38.313 | MS1 | 121.4656621594 | 31.1446287179 | 596 | 504990 | -89.52 | 7.91 | 93.64 | 0.16 | 2.82 | 454 |
| 2024-09-20 22:21:39.817 | MS1 | 121.4656631655 | 31.1446200235 | 596 | 504990 | -92.65 | 12.45 | 90.54 | 0.04 | 2.80 | 487 |
| 2024-09-20 22:21:40.456 | MS1 | 121.4656657794 | 31.1446217443 | 596 | 504990 | -89.02 | 8.43 | 334.53 | 0.15 | 2.38 | 1567 |
| 2024-09-20 22:21:41.978 | MS1 | 121.4656694696 | 31.1446360609 | 596 | 504990 | -91.76 | 11.89 | 388.55 | 0.16 | 2.60 | 1582 |
| 2024-09-20 22:21:42.870 | MS1 | 121.4656640777 | 31.1446338630 | 596 | 504990 | -91.58 | 9.32 | 362.66 | 0.04 | 2.34 | 1576 |

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
| 3229023 | 1 | 121.4724272819 | 31.1492680232 | 79 | 12 | 11 | 24.9 | TDD | 129 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3247681 | 2 | 121.4752372625 | 31.1541632179 | 167 | 11 | 0 | 17.4 | TDD | 596 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3267924 | 3 | 121.4697083496 | 31.1454884950 | 24 | 0 | 12 | 19.9 | TDD | 293 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3273432 | 4 | 121.4744088306 | 31.1470539154 | 85 | 13 | 4 | 40.6 | TDD | 303 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:31.464 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.487 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.596 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.596 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.341 | NREventA3 | measId:2;ServCellPCI:447;Se... |
| 2024-09-20 22:21:38.581 | NRHandoverAttempt | SourcePCI:447;SourceNR-ARFC... |
| 2024-09-20 22:21:38.624 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.636 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.758 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.758 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3229023 | 1 | 7.6078 | 10.7617 | -114.7608 | 17.0287 | 105.2181 | 0.0050 | 0.0091 |
| 2024_09_20 22:00 | 3247681 | 2 | 16.4061 | 5.1641 | -115.6124 | 14.7370 | 153.1061 | 0.0063 | 0.0124 |
| 2024_09_20 22:00 | 3267924 | 3 | 17.2736 | 16.9166 | -114.7921 | 10.6721 | 132.4603 | 0.0066 | 0.0145 |
| 2024_09_20 22:00 | 3273432 | 4 | 13.5243 | 11.9823 | -115.8006 | 19.1979 | 183.4118 | 0.0060 | 0.0052 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415753_423D4D06 | 504990 | 596 | -89.0 | 504990 | 129 | -96.1 | 504990 | 293 | -94.1 | 504990 | 303 |
| MR_1774415753_0390EB4F | 504990 | 596 | -88.9 | 504990 | 129 | -94.6 | 504990 | 293 | -93.9 | 504990 | 303 |
| MR_1774415753_7DC7493F | 504990 | 596 | -88.0 | 504990 | 129 | -94.4 | 504990 | 293 | -95.7 | 504990 | 303 |
| MR_1774415753_5976E6F1 | 504990 | 596 | -86.6 | 504990 | 129 | -93.8 | 504990 | 293 | -97.0 | 504990 | 303 |
| MR_1774415753_100E9120 | 504990 | 596 | -88.9 | 504990 | 129 | -93.4 | 504990 | 293 | -94.0 | 504990 | 303 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1517: `f547fc96-33d...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `f547fc96-33d9-4015-9c05-84e3102176f6` |
| Tag | **single-answer** |
| 정답 | **C7** |
| C7 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3266846_1 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1517] topology](images/train_1517.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3243359_3
- `C2`: Decrease transmission power for 3266846_1
- `C3`: Increase transmission power for 3266846_1
- `C4`: Decrease transmission power for 3243359_3
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3243359_3
- `C6`: Decrease A3 Offset threshold for 3266846_1
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3266846_1 **← 정답**
- `C8`: Check test server and transmission issues
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3266846_1
- `C10`: Add neighbor relationship between 3264830_2 and 3243359_3
- `C11`: Adjust the azimuth of 3266846_1 by 47 degrees
- `C12`: Increase A3 Offset threshold for 3266846_1
- `C13`: Lift the tilt angle of 3266846_1 by 1 degrees
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3243359_3
- `C15`: Adjust the azimuth of 3243359_3 by 50 degrees
- `C16`: Increase transmission power for 3243359_3
- `C17`: Insufficient data; more data is needed for judgment.
- `C18`: Increase A3 Offset threshold for 3243359_3
- `C19`: Press down the tilt angle of 3266846_1 by 1 degrees
- `C20`: Add neighbor relationship between 3266846_1 and 3243359_3
- `C21`: Lift the tilt angle  of 3243359_3 by 3 degrees
- `C22`: Press down the tilt angle  of 3243359_3 by 3 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.867 | MS1 | 121.4656755514 | 31.1446269959 | 665 | 504990 | -85.91 | 12.20 | 407.26 | 0.10 | 2.43 | 1595 |
| 2024-09-20 22:21:32.247 | MS1 | 121.4656725895 | 31.1446336496 | 665 | 504990 | -90.45 | 14.54 | 449.27 | 0.17 | 2.07 | 1578 |
| 2024-09-20 22:21:33.573 | MS1 | 121.4656640327 | 31.1446321544 | 665 | 504990 | -91.28 | 16.55 | 450.12 | 0.15 | 2.95 | 1562 |
| 2024-09-20 22:21:34.103 | MS1 | 121.4656769401 | 31.1446256186 | 665 | 504990 | -87.26 | 16.96 | 78.46 | 0.60 | 2.04 | 527 |
| 2024-09-20 22:21:35.624 | MS1 | 121.4656762176 | 31.1446245058 | 665 | 504990 | -87.33 | 14.39 | 83.27 | 0.67 | 2.95 | 644 |
| 2024-09-20 22:21:36.625 | MS1 | 121.4656758978 | 31.1446269544 | 665 | 504990 | -90.85 | 17.76 | 92.03 | 0.54 | 2.15 | 686 |
| 2024-09-20 22:21:37.588 | MS1 | 121.4656616001 | 31.1446351943 | 665 | 504990 | -93.76 | 7.53 | 64.22 | 0.57 | 2.69 | 576 |
| 2024-09-20 22:21:38.110 | MS1 | 121.4656601256 | 31.1446362392 | 665 | 504990 | -93.49 | 12.70 | 79.33 | 0.68 | 2.70 | 545 |
| 2024-09-20 22:21:39.568 | MS1 | 121.4656649143 | 31.1446305669 | 665 | 504990 | -91.75 | 12.52 | 60.60 | 0.60 | 2.91 | 570 |
| 2024-09-20 22:21:40.662 | MS1 | 121.4656722049 | 31.1446239317 | 665 | 504990 | -92.40 | 10.34 | 451.08 | 0.13 | 2.49 | 1570 |
| 2024-09-20 22:21:41.765 | MS1 | 121.4656613897 | 31.1446211775 | 665 | 504990 | -92.16 | 8.94 | 453.46 | 0.01 | 2.84 | 1595 |
| 2024-09-20 22:21:42.809 | MS1 | 121.4656628744 | 31.1446274950 | 665 | 504990 | -92.89 | 7.13 | 418.36 | 0.06 | 2.57 | 1567 |

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
| 3243359 | 3 | 121.4739045930 | 31.1471749157 | 0 | 0 | 4 | 46.5 | TDD | 892 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3261966 | 4 | 121.4737995570 | 31.1555871595 | 31 | 0 | 12 | 20.7 | TDD | 591 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3264830 | 2 | 121.4751026101 | 31.1450159075 | 299 | 1 | 4 | 27.0 | TDD | 323 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3266846 | 1 | 121.4691344661 | 31.1523050488 | 154 | 0 | 12 | 19.2 | TDD | 665 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:31.171 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.190 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.301 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.301 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.977 | NREventA3 | measId:2;ServCellPCI:315;Se... |
| 2024-09-20 22:21:38.217 | NRHandoverAttempt | SourcePCI:315;SourceNR-ARFC... |
| 2024-09-20 22:21:38.247 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.262 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.387 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.387 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3266846 | 1 | 15.9050 | 7.2209 | -114.8107 | 11.5997 | 155.3643 | 0.0134 | 0.0017 |
| 2024_09_20 22:00 | 3264830 | 2 | 19.7778 | 5.2846 | -114.3628 | 8.0039 | 110.0912 | 0.0010 | 0.0085 |
| 2024_09_20 22:00 | 3243359 | 3 | 13.4365 | 16.5703 | -116.7277 | 14.5185 | 150.0132 | 0.0056 | 0.0024 |
| 2024_09_20 22:00 | 3261966 | 4 | 10.8547 | 13.9417 | -117.3137 | 16.6083 | 193.4948 | 0.0062 | 0.0070 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412123_8CAFDEB8 | 504990 | 665 | -85.7 | 504990 | 892 | -90.9 | 504990 | 323 | -98.2 | 504990 | 591 |
| MR_1774412123_5E7E070C | 504990 | 665 | -88.0 | 504990 | 892 | -93.2 | 504990 | 323 | -100.3 | 504990 | 591 |
| MR_1774412123_D084FE22 | 504990 | 665 | -85.4 | 504990 | 892 | -91.6 | 504990 | 323 | -100.1 | 504990 | 591 |
| MR_1774412123_C504AA19 | 504990 | 665 | -85.7 | 504990 | 892 | -91.8 | 504990 | 323 | -98.2 | 504990 | 591 |
| MR_1774412123_DB1241F0 | 504990 | 665 | -86.1 | 504990 | 892 | -90.3 | 504990 | 323 | -98.1 | 504990 | 591 |
| MR_1774412123_89C3DEB8 | 504990 | 665 | -86.9 | 504990 | 892 | -92.0 | 504990 | 323 | -99.0 | 504990 | 591 |
| MR_1774412123_12D9306F | 504990 | 665 | -85.5 | 504990 | 892 | -93.2 | 504990 | 323 | -96.8 | 504990 | 591 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1518: `cba1a897-db2...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `cba1a897-db2a-4e9e-997f-0a9307776f7d` |
| Tag | **multiple-answer** |
| 정답 | **C14|C17** |
| C14 의미 | Adjust the azimuth of 3214156_2 by 50 degrees |
| C17 의미 | Increase transmission power for 3214156_2 |
| 패턴 분류 | **P4 Coverage (azimuth)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1518] topology](images/train_1518.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3214156_2
- `C2`: Press down the tilt angle of 3214156_2 by 4 degrees
- `C3`: Lift the tilt angle of 3214156_2 by 4 degrees
- `C4`: Add neighbor relationship between 3214156_2 and 3237270_3
- `C5`: Check test server and transmission issues
- `C6`: Increase transmission power for 3237270_3
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3237270_3
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3237270_3
- `C9`: Insufficient data; more data is needed for judgment.
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3214156_2
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3214156_2
- `C12`: Decrease A3 Offset threshold for 3237270_3
- `C13`: Increase A3 Offset threshold for 3237270_3
- `C14`: Adjust the azimuth of 3214156_2 by 50 degrees **← 정답**
- `C15`: Lift the tilt angle  of 3237270_3 by 4 degrees
- `C16`: Increase A3 Offset threshold for 3214156_2
- `C17`: Increase transmission power for 3214156_2 **← 정답**
- `C18`: Press down the tilt angle  of 3237270_3 by 4 degrees
- `C19`: Add neighbor relationship between 3233362_4 and 3237270_3
- `C20`: Decrease A3 Offset threshold for 3214156_2
- `C21`: Decrease transmission power for 3237270_3
- `C22`: Adjust the azimuth of 3237270_3 by 40 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.234 | MS1 | 121.4656585855 | 31.1446227161 | 967 | 504990 | -90.88 | 16.08 | 471.62 | 0.12 | 2.83 | 1580 |
| 2024-09-20 22:21:32.660 | MS1 | 121.4656597364 | 31.1446247915 | 967 | 504990 | -86.42 | 12.00 | 460.93 | 0.15 | 2.72 | 1572 |
| 2024-09-20 22:21:33.168 | MS1 | 121.4656640301 | 31.1446313098 | 967 | 504990 | -92.78 | 14.34 | 501.84 | 0.06 | 2.65 | 1562 |
| 2024-09-20 22:21:34.391 | MS1 | 121.4656606207 | 31.1446328678 | 967 | 504990 | -103.50 | 1.93 | 58.95 | 0.04 | 1.28 | 1566 |
| 2024-09-20 22:21:35.861 | MS1 | 121.4656630716 | 31.1446263295 | 967 | 504990 | -108.74 | -0.87 | 21.65 | 0.18 | 1.25 | 1600 |
| 2024-09-20 22:21:36.141 | MS1 | 121.4656597698 | 31.1446225438 | 967 | 504990 | -109.79 | 1.68 | 40.03 | 0.11 | 1.04 | 1572 |
| 2024-09-20 22:21:37.353 | MS1 | 121.4656762805 | 31.1446229156 | 967 | 504990 | -104.81 | -0.72 | 60.59 | 0.19 | 1.22 | 1579 |
| 2024-09-20 22:21:38.191 | MS1 | 121.4656628743 | 31.1446248748 | 967 | 504990 | -106.88 | 0.99 | 26.79 | 0.01 | 1.20 | 1577 |
| 2024-09-20 22:21:39.278 | MS1 | 121.4656611923 | 31.1446287090 | 967 | 504990 | -105.45 | 0.59 | 38.22 | 0.04 | 1.05 | 1568 |
| 2024-09-20 22:21:40.664 | MS1 | 121.4656749937 | 31.1446284283 | 967 | 504990 | -85.41 | 13.26 | 426.65 | 0.08 | 2.51 | 1577 |
| 2024-09-20 22:21:41.498 | MS1 | 121.4656764675 | 31.1446334096 | 967 | 504990 | -92.81 | 17.26 | 387.99 | 0.01 | 2.13 | 1596 |
| 2024-09-20 22:21:42.410 | MS1 | 121.4656717043 | 31.1446372318 | 967 | 504990 | -88.90 | 13.96 | 450.74 | 0.05 | 2.65 | 1565 |

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
| 3214156 | 2 | 121.4678943744 | 31.1540127237 | 115 | 3 | 8 | 24.2 | TDD | 967 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3233362 | 4 | 121.4755753367 | 31.1527725274 | 83 | 13 | 4 | 23.7 | TDD | 511 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3237270 | 3 | 121.4722511811 | 31.1520400589 | 257 | 1 | 9 | 46.0 | TDD | 759 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3254122 | 1 | 121.4727484994 | 31.1442675449 | 6 | 13 | 8 | 19.0 | TDD | 601 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:30.935 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.955 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.076 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.076 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.297 | NREventA2 | measId:1;ServCellPCI:619;Se... |
| 2024-09-20 22:21:34.415 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3254122 | 1 | 5.4394 | 13.7963 | -116.0124 | 19.8879 | 149.3236 | 0.0021 | 0.0036 |
| 2024_09_20 22:00 | 3214156 | 2 | 7.8732 | 15.3968 | -117.1020 | 18.7596 | 189.3441 | 0.1720 | 0.0016 |
| 2024_09_20 22:00 | 3237270 | 3 | 9.5625 | 12.5292 | -115.5547 | 10.7980 | 166.5022 | 0.0135 | 0.0062 |
| 2024_09_20 22:00 | 3233362 | 4 | 8.3157 | 5.3773 | -115.0459 | 15.3741 | 123.4993 | 0.0023 | 0.0142 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416534_C9477459 | 504990 | 967 | -104.3 | 504990 | 759 | -110.3 | 504990 | 511 | -117.2 | 504990 | 601 |
| MR_1774416534_C3E498ED | 504990 | 967 | -102.9 | 504990 | 759 | -111.1 | 504990 | 511 | -117.2 | 504990 | 601 |
| MR_1774416534_810FE6D2 | 504990 | 967 | -102.8 | 504990 | 759 | -111.2 | 504990 | 511 | -116.4 | 504990 | 601 |
| MR_1774416534_B68DD7A9 | 504990 | 967 | -102.1 | 504990 | 759 | -111.6 | 504990 | 511 | -114.3 | 504990 | 601 |
| MR_1774416534_7F506370 | 504990 | 967 | -103.1 | 504990 | 759 | -109.7 | 504990 | 511 | -116.8 | 504990 | 601 |
| MR_1774416534_1EA9C30B | 504990 | 967 | -105.4 | 504990 | 759 | -110.4 | 504990 | 511 | -116.7 | 504990 | 601 |
| MR_1774416534_905ABD6E | 504990 | 967 | -105.4 | 504990 | 759 | -108.7 | 504990 | 511 | -114.4 | 504990 | 601 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1519: `af4a70be-beb...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `af4a70be-beb4-4b95-94c0-63a4e831ba43` |
| Tag | **single-answer** |
| 정답 | **C17** |
| C17 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1519] topology](images/train_1519.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3269902_4 by 10 degrees
- `C2`: Add neighbor relationship between 3272220_1 and 3269902_4
- `C3`: Increase A3 Offset threshold for 3272220_1
- `C4`: Adjust the azimuth of 3272220_1 by 50 degrees
- `C5`: Decrease transmission power for 3269902_4
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3272220_1
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3269902_4
- `C8`: Decrease A3 Offset threshold for 3272220_1
- `C9`: Check test server and transmission issues
- `C10`: Decrease transmission power for 3272220_1
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3269902_4
- `C12`: Press down the tilt angle of 3272220_1 by 10 degrees
- `C13`: Decrease A3 Offset threshold for 3269902_4
- `C14`: Add neighbor relationship between 3215636_2 and 3269902_4
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3272220_1
- `C16`: Increase transmission power for 3272220_1
- `C17`: Insufficient data; more data is needed for judgment. **← 정답**
- `C18`: Increase transmission power for 3269902_4
- `C19`: Increase A3 Offset threshold for 3269902_4
- `C20`: Lift the tilt angle of 3272220_1 by 10 degrees
- `C21`: Lift the tilt angle  of 3269902_4 by 10 degrees
- `C22`: Adjust the azimuth of 3269902_4 by 50 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.213 | MS1 | 121.4656742112 | 31.1446243266 | 736 | 504990 | -87.93 | 17.37 | 510.86 | 0.15 | 2.13 | 1591 |
| 2024-09-20 22:21:32.274 | MS1 | 121.4656670288 | 31.1446361312 | 736 | 504990 | -91.24 | 17.77 | 387.68 | 0.05 | 2.66 | 1597 |
| 2024-09-20 22:21:33.101 | MS1 | 121.4656592356 | 31.1446205012 | 736 | 504990 | -87.75 | 16.94 | 397.86 | 0.09 | 2.29 | 1590 |
| 2024-09-20 22:21:34.982 | MS1 | 121.4656666571 | 31.1446242386 | 736 | 504990 | -85.56 | 13.64 | 65.34 | 0.06 | 2.67 | 1571 |
| 2024-09-20 22:21:35.459 | MS1 | 121.4656720750 | 31.1446324246 | 736 | 504990 | -86.84 | 13.63 | 57.07 | 0.16 | 2.62 | 1588 |
| 2024-09-20 22:21:36.541 | MS1 | 121.4656769154 | 31.1446231681 | 736 | 504990 | -86.33 | 12.63 | 98.18 | 0.20 | 2.53 | 1571 |
| 2024-09-20 22:21:37.709 | MS1 | 121.4656746327 | 31.1446325521 | 736 | 504990 | -93.70 | 11.69 | 93.25 | 0.07 | 2.93 | 1585 |
| 2024-09-20 22:21:38.278 | MS1 | 121.4656608304 | 31.1446279300 | 736 | 504990 | -93.92 | 7.06 | 68.69 | 0.07 | 2.78 | 1592 |
| 2024-09-20 22:21:39.404 | MS1 | 121.4656679670 | 31.1446312208 | 736 | 504990 | -93.26 | 7.34 | 99.75 | 0.16 | 2.46 | 1575 |
| 2024-09-20 22:21:40.782 | MS1 | 121.4656631550 | 31.1446354541 | 736 | 504990 | -90.31 | 8.84 | 542.79 | 0.11 | 2.52 | 1566 |
| 2024-09-20 22:21:41.987 | MS1 | 121.4656597887 | 31.1446372508 | 736 | 504990 | -92.81 | 10.24 | 485.50 | 0.05 | 2.12 | 1565 |
| 2024-09-20 22:21:42.304 | MS1 | 121.4656659377 | 31.1446219894 | 736 | 504990 | -91.01 | 8.46 | 576.94 | 0.01 | 2.33 | 1570 |

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
| 3215636 | 2 | 121.4658673475 | 31.1527011038 | 177 | 13 | 2 | 26.1 | TDD | 384 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3217273 | 3 | 121.4644654340 | 31.1471753522 | 282 | 6 | 2 | 36.9 | TDD | 381 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3269902 | 4 | 121.4743651282 | 31.1520811709 | 26 | 10 | 2 | 25.5 | TDD | 639 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3272220 | 1 | 121.4740766427 | 31.1470277260 | 102 | 8 | 11 | 24.2 | TDD | 736 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |

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
| 2024-09-20 22:21:31.253 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.270 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.391 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.391 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.085 | NREventA3 | measId:2;ServCellPCI:621;Se... |
| 2024-09-20 22:21:38.325 | NRHandoverAttempt | SourcePCI:621;SourceNR-ARFC... |
| 2024-09-20 22:21:38.363 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.376 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.507 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.507 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3272220 | 1 | 78.9015 | 91.3114 | -115.9528 | 7.8383 | 128.2000 | 0.0117 | 0.0087 |
| 2024_09_19 22:00 | 3215636 | 2 | 84.1897 | 90.6112 | -117.5765 | 11.1335 | 146.1255 | 0.0101 | 0.0053 |
| 2024_09_19 22:00 | 3217273 | 3 | 76.1931 | 86.3324 | -116.5759 | 5.8366 | 182.3073 | 0.0037 | 0.0021 |
| 2024_09_19 22:00 | 3269902 | 4 | 81.0451 | 82.4897 | -116.5597 | 16.2347 | 118.0981 | 0.0140 | 0.0169 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415830_49965B27 | 504990 | 736 | -84.8 | 504990 | 639 | -92.5 | 504990 | 384 | -96.5 | 504990 | 381 |
| MR_1774415830_08A929E8 | 504990 | 736 | -85.2 | 504990 | 639 | -90.8 | 504990 | 384 | -96.6 | 504990 | 381 |
| MR_1774415830_C8300DC1 | 504990 | 736 | -86.1 | 504990 | 639 | -92.6 | 504990 | 384 | -95.5 | 504990 | 381 |
| MR_1774415830_BBA613C4 | 504990 | 736 | -83.8 | 504990 | 639 | -90.3 | 504990 | 384 | -95.3 | 504990 | 381 |
| MR_1774415830_FB68DDDA | 504990 | 736 | -86.5 | 504990 | 639 | -92.7 | 504990 | 384 | -95.9 | 504990 | 381 |

> *... 2개 열 생략 (전체 14열)*

---
