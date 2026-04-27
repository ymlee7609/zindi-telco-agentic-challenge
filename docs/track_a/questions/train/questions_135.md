# Track A 문제 분석 — train[1340]~train[1349]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[1340] ~ train[1349] (10개)

## 목차

1. [문제 1340: `7fa5ac18-557...`](#1340) — multiple-answer, 정답: C7|C11|C14|C19
2. [문제 1341: `294e9e87-071...`](#1341) — single-answer, 정답: C10
3. [문제 1342: `90ede246-2fb...`](#1342) — single-answer, 정답: C13
4. [문제 1343: `4e20c8a9-742...`](#1343) — multiple-answer, 정답: C2|C18
5. [문제 1344: `d906fe9f-2bf...`](#1344) — single-answer, 정답: C1
6. [문제 1345: `c8a265e4-f0e...`](#1345) — single-answer, 정답: C10
7. [문제 1346: `367d402a-531...`](#1346) — single-answer, 정답: C8
8. [문제 1347: `aa0e0741-4b9...`](#1347) — single-answer, 정답: C17
9. [문제 1348: `1db8c85e-7d6...`](#1348) — single-answer, 정답: C6
10. [문제 1349: `bf44b7e6-9c1...`](#1349) — multiple-answer, 정답: C1|C20

---

### 문제 1340: `7fa5ac18-557...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `7fa5ac18-5570-49d4-a335-bc0250b3dffc` |
| Tag | **multiple-answer** |
| 정답 | **C7|C11|C14|C19** |
| C7 의미 | Decrease transmission power for 3231466_5 |
| C11 의미 | Increase A3 Offset threshold for 3231466_5 |
| C14 의미 | Increase A3 Offset threshold for 3242034_3 |
| C19 의미 | Press down the tilt angle  of 3231466_5 by 4 degrees |
| 패턴 분류 | **P3 Overshoot (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1340] topology](images/train_1340.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 5 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 5개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3242034_3 and 3231466_5
- `C2`: Press down the tilt angle of 3242034_3 by 3 degrees
- `C3`: Insufficient data; more data is needed for judgment.
- `C4`: Adjust the azimuth of 3231466_5 by 28 degrees
- `C5`: Lift the tilt angle  of 3231466_5 by 4 degrees
- `C6`: Decrease transmission power for 3242034_3
- `C7`: Decrease transmission power for 3231466_5 **← 정답**
- `C8`: Adjust the azimuth of 3242034_3 by 41 degrees
- `C9`: Lift the tilt angle of 3242034_3 by 3 degrees
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3242034_3
- `C11`: Increase A3 Offset threshold for 3231466_5 **← 정답**
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3231466_5
- `C13`: Increase transmission power for 3242034_3
- `C14`: Increase A3 Offset threshold for 3242034_3 **← 정답**
- `C15`: Increase transmission power for 3231466_5
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3231466_5
- `C17`: Check test server and transmission issues
- `C18`: Decrease A3 Offset threshold for 3231466_5
- `C19`: Press down the tilt angle  of 3231466_5 by 4 degrees **← 정답**
- `C20`: Decrease A3 Offset threshold for 3242034_3
- `C21`: Add neighbor relationship between 3218268_1 and 3231466_5
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3242034_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.260 | MS1 | 121.4656738388 | 31.1446295544 | 1004 | 504990 | -81.11 | 14.63 | 496.52 | 0.05 | 2.49 | 1583 |
| 2024-09-20 22:21:32.292 | MS1 | 121.4656646348 | 31.1446215398 | 1004 | 504990 | -76.37 | 12.10 | 341.97 | 0.02 | 2.40 | 1591 |
| 2024-09-20 22:21:33.587 | MS1 | 121.4656716390 | 31.1446324438 | 1004 | 504990 | -76.21 | 12.75 | 417.75 | 0.14 | 2.59 | 1566 |
| 2024-09-20 22:21:34.986 | MS1 | 121.4656691475 | 31.1446252954 | 860 | 504990 | -82.50 | 2.77 | 55.13 | 0.02 | 1.43 | 1573 |
| 2024-09-20 22:21:35.142 | MS1 | 121.4656718206 | 31.1446198880 | 860 | 504990 | -85.47 | 3.15 | 58.29 | 0.17 | 1.21 | 1588 |
| 2024-09-20 22:21:36.326 | MS1 | 121.4656710514 | 31.1446215592 | 1004 | 504990 | -82.39 | 2.54 | 34.99 | 0.10 | 1.14 | 1575 |
| 2024-09-20 22:21:37.657 | MS1 | 121.4656652467 | 31.1446291068 | 1004 | 504990 | -81.87 | 3.85 | 46.51 | 0.12 | 1.26 | 1569 |
| 2024-09-20 22:21:38.497 | MS1 | 121.4656653871 | 31.1446233857 | 860 | 504990 | -89.15 | 4.75 | 49.34 | 0.08 | 1.41 | 1572 |
| 2024-09-20 22:21:39.997 | MS1 | 121.4656674493 | 31.1446272276 | 860 | 504990 | -82.16 | 4.20 | 46.13 | 0.18 | 1.43 | 1596 |
| 2024-09-20 22:21:40.386 | MS1 | 121.4656685207 | 31.1446309566 | 860 | 504990 | -77.51 | 15.12 | 450.27 | 0.14 | 2.98 | 1562 |
| 2024-09-20 22:21:41.983 | MS1 | 121.4656609249 | 31.1446306368 | 860 | 504990 | -75.45 | 16.62 | 342.35 | 0.16 | 2.85 | 1570 |
| 2024-09-20 22:21:42.486 | MS1 | 121.4656762996 | 31.1446181989 | 860 | 504990 | -84.16 | 17.87 | 382.61 | 0.11 | 2.12 | 1594 |

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
| 3218268 | 1 | 121.4667211004 | 31.1526499022 | 121 | 10 | 2 | 16.1 | TDD | 804 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3222920 | 4 | 121.4665359160 | 31.1526075412 | 220 | 10 | 1 | 25.7 | TDD | 174 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3231466 | 5 | 121.4743991872 | 31.1475334105 | 221 | 1 | 10 | 43.3 | TDD | 92 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3242034 | 3 | 121.4741898028 | 31.1487948583 | 281 | 0 | 0 | 47.0 | TDD | 1004 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3257915 | 2 | 121.4644105939 | 31.1481770599 | 224 | 8 | 0 | 34.7 | TDD | 860 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:31.161 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.186 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.297 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.297 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.049 | NREventA3 | measId:2;ServCellPCI:361;Se... |
| 2024-09-20 22:21:34.289 | NRHandoverAttempt | SourcePCI:361;SourceNR-ARFC... |
| 2024-09-20 22:21:34.335 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:34.347 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:34.452 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:34.452 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:36.049 | NREventA3 | measId:2;ServCellPCI:175;Se... |
| 2024-09-20 22:21:36.289 | NRHandoverAttempt | SourcePCI:175;SourceNR-ARFC... |
| 2024-09-20 22:21:36.334 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:36.344 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:36.472 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.472 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.049 | NREventA3 | measId:2;ServCellPCI:361;Se... |
| 2024-09-20 22:21:38.289 | NRHandoverAttempt | SourcePCI:361;SourceNR-ARFC... |
| 2024-09-20 22:21:38.339 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.353 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.487 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.487 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3218268 | 1 | 14.8471 | 8.2989 | -114.0996 | 18.3172 | 167.8569 | 0.0071 | 0.0020 |
| 2024_09_20 22:00 | 3257915 | 2 | 7.0294 | 12.5811 | -116.0715 | 9.3580 | 184.4236 | 0.0147 | 0.0139 |
| 2024_09_20 22:00 | 3242034 | 3 | 12.7889 | 6.7264 | -115.2823 | 18.0422 | 153.8289 | 0.0076 | 0.0191 |
| 2024_09_20 22:00 | 3222920 | 4 | 9.9524 | 19.7077 | -117.3311 | 7.6651 | 183.7801 | 0.0159 | 0.0108 |
| 2024_09_20 22:00 | 3231466 | 5 | 5.6106 | 7.2198 | -117.6859 | 7.2018 | 181.7136 | 0.0129 | 0.0180 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416271_11A317D6 | 504990 | 860 | -83.0 | 504990 | 1004 | -84.9 | 504990 | 92 | -82.3 | 504990 | 804 |
| MR_1774416271_357D7458 | 504990 | 860 | -84.4 | 504990 | 1004 | -83.9 | 504990 | 92 | -85.6 | 504990 | 804 |
| MR_1774416271_CB5B8E9B | 504990 | 1004 | -81.3 | 504990 | 860 | -84.2 | 504990 | 92 | -84.5 | 504990 | 804 |
| MR_1774416271_8A0CE61B | 504990 | 860 | -81.6 | 504990 | 1004 | -83.7 | 504990 | 92 | -83.7 | 504990 | 804 |
| MR_1774416271_6A888EA7 | 504990 | 1004 | -83.6 | 504990 | 860 | -82.0 | 504990 | 92 | -82.3 | 504990 | 804 |
| MR_1774416271_627EBE06 | 504990 | 1004 | -83.4 | 504990 | 860 | -83.6 | 504990 | 92 | -83.9 | 504990 | 804 |
| MR_1774416271_041DD0A0 | 504990 | 860 | -82.2 | 504990 | 1004 | -82.9 | 504990 | 92 | -83.0 | 504990 | 804 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1341: `294e9e87-071...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `294e9e87-0718-4ab2-8458-2fc62c8e5a8c` |
| Tag | **single-answer** |
| 정답 | **C10** |
| C10 의미 | Decrease A3 Offset threshold for 3226668_2 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1341] topology](images/train_1341.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3226668_2 by 12 degrees
- `C2`: Press down the tilt angle of 3226668_2 by 10 degrees
- `C3`: Add neighbor relationship between 3226668_2 and 3215426_4
- `C4`: Decrease A3 Offset threshold for 3215426_4
- `C5`: Press down the tilt angle  of 3215426_4 by 6 degrees
- `C6`: Check test server and transmission issues
- `C7`: Adjust the azimuth of 3215426_4 by 50 degrees
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3215426_4
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3226668_2
- `C10`: Decrease A3 Offset threshold for 3226668_2 **← 정답**
- `C11`: Decrease transmission power for 3226668_2
- `C12`: Lift the tilt angle of 3226668_2 by 10 degrees
- `C13`: Insufficient data; more data is needed for judgment.
- `C14`: Lift the tilt angle  of 3215426_4 by 6 degrees
- `C15`: Increase transmission power for 3226668_2
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3215426_4
- `C17`: Add neighbor relationship between 3241674_3 and 3215426_4
- `C18`: Increase A3 Offset threshold for 3215426_4
- `C19`: Decrease transmission power for 3215426_4
- `C20`: Increase A3 Offset threshold for 3226668_2
- `C21`: Increase transmission power for 3215426_4
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3226668_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.554 | MS1 | 121.4656687754 | 31.1446236994 | 355 | 504990 | -75.95 | 16.49 | 389.72 | 0.12 | 2.96 | 1589 |
| 2024-09-20 22:21:32.261 | MS1 | 121.4656615070 | 31.1446199323 | 355 | 504990 | -82.49 | 14.20 | 420.91 | 0.16 | 2.41 | 1593 |
| 2024-09-20 22:21:33.156 | MS1 | 121.4656656497 | 31.1446350728 | 355 | 504990 | -76.13 | 15.55 | 364.06 | 0.10 | 2.83 | 1570 |
| 2024-09-20 22:21:34.333 | MS1 | 121.4656758596 | 31.1446369619 | 355 | 504990 | -83.42 | -2.31 | 54.80 | 0.13 | 1.22 | 1577 |
| 2024-09-20 22:21:35.943 | MS1 | 121.4656714284 | 31.1446297424 | 355 | 504990 | -89.57 | -3.17 | 45.76 | 0.17 | 1.28 | 1563 |
| 2024-09-20 22:21:36.531 | MS1 | 121.4656744553 | 31.1446316477 | 355 | 504990 | -85.09 | -0.59 | 36.25 | 0.19 | 1.11 | 1599 |
| 2024-09-20 22:21:37.732 | MS1 | 121.4656649953 | 31.1446334083 | 355 | 504990 | -84.80 | -3.23 | 82.28 | 0.14 | 1.47 | 1562 |
| 2024-09-20 22:21:38.288 | MS1 | 121.4656771827 | 31.1446266422 | 355 | 504990 | -83.03 | -2.00 | 37.92 | 0.15 | 1.06 | 1591 |
| 2024-09-20 22:21:39.240 | MS1 | 121.4656599540 | 31.1446343285 | 518 | 504990 | -76.77 | 15.97 | 301.17 | 0.03 | 1.47 | 1589 |
| 2024-09-20 22:21:40.325 | MS1 | 121.4656715921 | 31.1446209112 | 518 | 504990 | -80.22 | 16.66 | 417.28 | 0.17 | 2.40 | 1560 |
| 2024-09-20 22:21:41.432 | MS1 | 121.4656616996 | 31.1446335173 | 518 | 504990 | -77.89 | 12.85 | 537.44 | 0.03 | 2.99 | 1570 |
| 2024-09-20 22:21:42.651 | MS1 | 121.4656611247 | 31.1446222645 | 518 | 504990 | -81.51 | 15.24 | 512.84 | 0.10 | 2.45 | 1573 |

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
| 3215426 | 4 | 121.4660174197 | 31.1490219590 | 270 | 1 | 10 | 46.9 | TDD | 518 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3226668 | 2 | 121.4673740805 | 31.1535025500 | 177 | 10 | 10 | 35.8 | TDD | 355 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3241674 | 3 | 121.4640612605 | 31.1444420016 | 24 | 15 | 6 | 26.5 | TDD | 973 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3244366 | 1 | 121.4702502186 | 31.1548388343 | 247 | 7 | 3 | 42.5 | TDD | 274 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |

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
| 2024-09-20 22:21:31.217 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.239 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.382 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.382 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.110 | NREventA3 | measId:2;ServCellPCI:829;Se... |
| 2024-09-20 22:21:38.350 | NRHandoverAttempt | SourcePCI:829;SourceNR-ARFC... |
| 2024-09-20 22:21:38.387 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.399 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.500 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.500 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3244366 | 1 | 10.1073 | 15.5519 | -115.8924 | 18.5183 | 94.7652 | 0.0141 | 0.0119 |
| 2024_09_20 22:00 | 3226668 | 2 | 9.4232 | 18.2519 | -116.3511 | 19.5283 | 145.9871 | 0.0184 | 0.1528 |
| 2024_09_20 22:00 | 3241674 | 3 | 5.6836 | 8.8178 | -114.3323 | 12.1633 | 169.4632 | 0.0186 | 0.0150 |
| 2024_09_20 22:00 | 3215426 | 4 | 15.6200 | 10.6527 | -117.4287 | 6.5257 | 149.3153 | 0.0152 | 0.0150 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414037_A58D0694 | 504990 | 355 | -84.2 | 504990 | 518 | -77.7 | 504990 | 973 | -82.6 | 504990 | 274 |
| MR_1774414037_A1A74F6E | 504990 | 518 | -77.8 | 504990 | 355 | -82.8 | 504990 | 973 | -82.0 | 504990 | 274 |
| MR_1774414037_D05B3E86 | 504990 | 518 | -76.1 | 504990 | 355 | -84.2 | 504990 | 973 | -82.5 | 504990 | 274 |
| MR_1774414037_F520DE74 | 504990 | 518 | -79.9 | 504990 | 355 | -84.2 | 504990 | 973 | -81.4 | 504990 | 274 |
| MR_1774414037_06B682C7 | 504990 | 518 | -78.6 | 504990 | 355 | -81.5 | 504990 | 973 | -82.9 | 504990 | 274 |
| MR_1774414037_7AC43234 | 504990 | 355 | -83.7 | 504990 | 518 | -77.9 | 504990 | 973 | -82.9 | 504990 | 274 |
| MR_1774414037_8C03D2E7 | 504990 | 518 | -79.6 | 504990 | 355 | -84.9 | 504990 | 973 | -79.8 | 504990 | 274 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1342: `90ede246-2fb...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `90ede246-2fba-4195-8eef-42459df15b69` |
| Tag | **single-answer** |
| 정답 | **C13** |
| C13 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3234401_1 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1342] topology](images/train_1342.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3251895_3
- `C2`: Adjust the azimuth of 3234401_1 by 40 degrees
- `C3`: Increase A3 Offset threshold for 3251895_3
- `C4`: Press down the tilt angle  of 3251895_3 by 10 degrees
- `C5`: Increase transmission power for 3251895_3
- `C6`: Lift the tilt angle  of 3251895_3 by 10 degrees
- `C7`: Increase transmission power for 3234401_1
- `C8`: Decrease A3 Offset threshold for 3234401_1
- `C9`: Press down the tilt angle of 3234401_1 by 5 degrees
- `C10`: Decrease transmission power for 3251895_3
- `C11`: Decrease transmission power for 3234401_1
- `C12`: Add neighbor relationship between 3265799_4 and 3251895_3
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3234401_1 **← 정답**
- `C14`: Lift the tilt angle of 3234401_1 by 5 degrees
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3251895_3
- `C16`: Check test server and transmission issues
- `C17`: Increase A3 Offset threshold for 3234401_1
- `C18`: Adjust the azimuth of 3251895_3 by 50 degrees
- `C19`: Decrease A3 Offset threshold for 3251895_3
- `C20`: Add neighbor relationship between 3234401_1 and 3251895_3
- `C21`: Insufficient data; more data is needed for judgment.
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3234401_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.759 | MS1 | 121.4656776483 | 31.1446335573 | 131 | 504990 | -87.59 | 12.43 | 338.50 | 0.11 | 2.60 | 1568 |
| 2024-09-20 22:21:32.758 | MS1 | 121.4656597013 | 31.1446359628 | 131 | 504990 | -87.02 | 14.85 | 314.53 | 0.17 | 2.04 | 1571 |
| 2024-09-20 22:21:33.205 | MS1 | 121.4656593263 | 31.1446219097 | 131 | 504990 | -91.25 | 14.55 | 435.53 | 0.12 | 2.98 | 1567 |
| 2024-09-20 22:21:34.659 | MS1 | 121.4656659091 | 31.1446341036 | 131 | 504990 | -87.57 | 17.45 | 95.75 | 0.65 | 2.23 | 534 |
| 2024-09-20 22:21:35.821 | MS1 | 121.4656727676 | 31.1446218227 | 131 | 504990 | -87.21 | 17.93 | 64.72 | 0.56 | 2.69 | 664 |
| 2024-09-20 22:21:36.233 | MS1 | 121.4656749828 | 31.1446318096 | 131 | 504990 | -85.86 | 12.31 | 53.31 | 0.52 | 2.12 | 645 |
| 2024-09-20 22:21:37.284 | MS1 | 121.4656707342 | 31.1446366649 | 131 | 504990 | -91.18 | 12.25 | 102.61 | 0.62 | 2.55 | 659 |
| 2024-09-20 22:21:38.950 | MS1 | 121.4656745316 | 31.1446246705 | 131 | 504990 | -91.17 | 8.42 | 73.77 | 0.61 | 2.17 | 561 |
| 2024-09-20 22:21:39.175 | MS1 | 121.4656753714 | 31.1446215878 | 131 | 504990 | -91.74 | 8.67 | 82.97 | 0.56 | 2.82 | 613 |
| 2024-09-20 22:21:40.797 | MS1 | 121.4656595614 | 31.1446303606 | 131 | 504990 | -92.75 | 8.22 | 466.26 | 0.20 | 2.92 | 1566 |
| 2024-09-20 22:21:41.148 | MS1 | 121.4656697941 | 31.1446276957 | 131 | 504990 | -92.86 | 10.50 | 323.90 | 0.02 | 2.75 | 1569 |
| 2024-09-20 22:21:42.453 | MS1 | 121.4656704988 | 31.1446303149 | 131 | 504990 | -89.38 | 7.58 | 464.49 | 0.04 | 2.86 | 1597 |

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
| 3234401 | 1 | 121.4752213651 | 31.1550912727 | 178 | 4 | 7 | 21.6 | TDD | 131 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3251895 | 3 | 121.4719273485 | 31.1473390221 | 37 | 10 | 4 | 49.5 | TDD | 607 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3265799 | 4 | 121.4719921625 | 31.1467601439 | 287 | 15 | 3 | 37.0 | TDD | 311 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3277145 | 2 | 121.4674988048 | 31.1447516262 | 113 | 13 | 1 | 29.2 | TDD | 21 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:31.497 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.522 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.635 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.635 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.350 | NREventA3 | measId:2;ServCellPCI:467;Se... |
| 2024-09-20 22:21:38.590 | NRHandoverAttempt | SourcePCI:467;SourceNR-ARFC... |
| 2024-09-20 22:21:38.626 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.636 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.772 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.772 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3234401 | 1 | 16.6023 | 5.4814 | -117.8640 | 14.1403 | 96.9993 | 0.0127 | 0.0109 |
| 2024_09_20 22:00 | 3277145 | 2 | 13.2252 | 9.1775 | -115.4182 | 7.6825 | 129.7084 | 0.0103 | 0.0094 |
| 2024_09_20 22:00 | 3251895 | 3 | 12.7297 | 8.6405 | -115.6058 | 12.0475 | 87.8986 | 0.0033 | 0.0071 |
| 2024_09_20 22:00 | 3265799 | 4 | 5.9116 | 11.2215 | -115.9681 | 18.7603 | 197.6116 | 0.0012 | 0.0106 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417222_92550414 | 504990 | 131 | -89.3 | 504990 | 607 | -86.4 | 504990 | 311 | -96.2 | 504990 | 21 |
| MR_1774417222_D6858B6A | 504990 | 131 | -89.2 | 504990 | 607 | -86.4 | 504990 | 311 | -92.9 | 504990 | 21 |
| MR_1774417222_92A45951 | 504990 | 131 | -86.9 | 504990 | 607 | -89.0 | 504990 | 311 | -94.8 | 504990 | 21 |
| MR_1774417222_85D4BB2B | 504990 | 131 | -89.1 | 504990 | 607 | -87.3 | 504990 | 311 | -93.4 | 504990 | 21 |
| MR_1774417222_BEB50403 | 504990 | 131 | -86.0 | 504990 | 607 | -87.3 | 504990 | 311 | -96.6 | 504990 | 21 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1343: `4e20c8a9-742...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `4e20c8a9-7420-4b3a-8e1a-a27a0422278f` |
| Tag | **multiple-answer** |
| 정답 | **C2|C18** |
| C2 의미 | Decrease transmission power for 3237077_1 |
| C18 의미 | Press down the tilt angle  of 3237077_1 by 3 degrees |
| 패턴 분류 | **P3 Overshoot (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1343] topology](images/train_1343.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3237077_1 by 25 degrees
- `C2`: Decrease transmission power for 3237077_1 **← 정답**
- `C3`: Decrease A3 Offset threshold for 3255158_3
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3255158_3
- `C5`: Lift the tilt angle  of 3237077_1 by 3 degrees
- `C6`: Lift the tilt angle of 3255158_3 by 6 degrees
- `C7`: Decrease A3 Offset threshold for 3237077_1
- `C8`: Decrease transmission power for 3255158_3
- `C9`: Add neighbor relationship between 3255158_3 and 3237077_1
- `C10`: Increase A3 Offset threshold for 3237077_1
- `C11`: Increase transmission power for 3255158_3
- `C12`: Add neighbor relationship between 3224826_2 and 3237077_1
- `C13`: Increase transmission power for 3237077_1
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3255158_3
- `C16`: Press down the tilt angle of 3255158_3 by 6 degrees
- `C17`: Check test server and transmission issues
- `C18`: Press down the tilt angle  of 3237077_1 by 3 degrees **← 정답**
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3237077_1
- `C20`: Increase A3 Offset threshold for 3255158_3
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3237077_1
- `C22`: Adjust the azimuth of 3255158_3 by 44 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.336 | MS1 | 121.4656583329 | 31.1446186312 | 782 | 504990 | -75.48 | 16.65 | 481.90 | 0.20 | 2.57 | 1582 |
| 2024-09-20 22:21:32.658 | MS1 | 121.4656608500 | 31.1446333859 | 782 | 504990 | -80.66 | 12.26 | 420.48 | 0.11 | 2.82 | 1576 |
| 2024-09-20 22:21:33.996 | MS1 | 121.4656713201 | 31.1446199179 | 782 | 504990 | -76.05 | 17.27 | 550.47 | 0.04 | 2.07 | 1584 |
| 2024-09-20 22:21:34.181 | MS1 | 121.4656726555 | 31.1446291251 | 782 | 504990 | -89.18 | 0.59 | 77.23 | 0.02 | 1.43 | 1562 |
| 2024-09-20 22:21:35.866 | MS1 | 121.4656603782 | 31.1446295331 | 782 | 504990 | -88.79 | 3.90 | 56.28 | 0.19 | 1.38 | 1590 |
| 2024-09-20 22:21:36.695 | MS1 | 121.4656638683 | 31.1446331385 | 782 | 504990 | -90.29 | 3.64 | 92.00 | 0.19 | 1.44 | 1580 |
| 2024-09-20 22:21:37.991 | MS1 | 121.4656697903 | 31.1446186997 | 782 | 504990 | -95.00 | 2.31 | 74.82 | 0.12 | 1.45 | 1565 |
| 2024-09-20 22:21:38.839 | MS1 | 121.4656737136 | 31.1446325937 | 782 | 504990 | -88.23 | 0.58 | 63.85 | 0.06 | 1.32 | 1565 |
| 2024-09-20 22:21:39.690 | MS1 | 121.4656605518 | 31.1446329295 | 782 | 504990 | -87.64 | 1.99 | 48.84 | 0.12 | 1.31 | 1579 |
| 2024-09-20 22:21:40.970 | MS1 | 121.4656586815 | 31.1446357815 | 782 | 504990 | -80.34 | 13.96 | 556.11 | 0.01 | 2.83 | 1584 |
| 2024-09-20 22:21:41.765 | MS1 | 121.4656773317 | 31.1446233421 | 782 | 504990 | -75.30 | 15.08 | 516.75 | 0.01 | 2.75 | 1600 |
| 2024-09-20 22:21:42.821 | MS1 | 121.4656597510 | 31.1446247732 | 782 | 504990 | -82.41 | 17.89 | 481.86 | 0.17 | 2.12 | 1598 |

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
| 3224826 | 2 | 121.4649925723 | 31.1440731590 | 307 | 6 | 4 | 43.7 | TDD | 394 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3228743 | 4 | 121.4720046826 | 31.1485760194 | 218 | 2 | 7 | 45.1 | TDD | 351 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3237077 | 1 | 121.4677668334 | 31.1559647272 | 164 | 1 | 11 | 47.0 | TDD | 544 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3255158 | 3 | 121.4705653180 | 31.1486987851 | 182 | 3 | 11 | 29.8 | TDD | 782 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |

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
| 2024-09-20 22:21:31.239 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.264 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.407 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.407 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3237077 | 1 | 17.4556 | 17.2913 | -116.7061 | 8.0043 | 88.8601 | 0.0006 | 0.0065 |
| 2024_09_20 22:00 | 3224826 | 2 | 9.4050 | 9.4043 | -117.6746 | 19.0930 | 128.8643 | 0.0152 | 0.0170 |
| 2024_09_20 22:00 | 3255158 | 3 | 15.3046 | 18.3484 | -109.9744 | 10.0204 | 175.3607 | 0.0109 | 0.0093 |
| 2024_09_20 22:00 | 3228743 | 4 | 18.4388 | 19.5984 | -115.6799 | 12.7100 | 140.8348 | 0.0167 | 0.0198 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414077_85AA60C3 | 504990 | 782 | -90.5 | 504990 | 544 | -84.9 | 504990 | 394 | -91.3 | 504990 | 351 |
| MR_1774414077_F77F8701 | 504990 | 544 | -87.7 | 504990 | 782 | -83.6 | 504990 | 394 | -88.4 | 504990 | 351 |
| MR_1774414077_87F0F2E3 | 504990 | 544 | -90.2 | 504990 | 782 | -83.4 | 504990 | 394 | -91.3 | 504990 | 351 |
| MR_1774414077_02F39117 | 504990 | 782 | -88.9 | 504990 | 544 | -83.5 | 504990 | 394 | -90.2 | 504990 | 351 |
| MR_1774414077_41C5F372 | 504990 | 782 | -89.4 | 504990 | 544 | -85.9 | 504990 | 394 | -88.8 | 504990 | 351 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1344: `d906fe9f-2bf...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `d906fe9f-2bf4-42e2-9453-5d7c9c4ec6db` |
| Tag | **single-answer** |
| 정답 | **C1** |
| C1 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3259382_1 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1344] topology](images/train_1344.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3259382_1 **← 정답**
- `C2`: Press down the tilt angle  of 3226517_2 by 10 degrees
- `C3`: Increase transmission power for 3259382_1
- `C4`: Adjust the azimuth of 3259382_1 by 44 degrees
- `C5`: Adjust the azimuth of 3226517_2 by 50 degrees
- `C6`: Insufficient data; more data is needed for judgment.
- `C7`: Check test server and transmission issues
- `C8`: Increase A3 Offset threshold for 3226517_2
- `C9`: Decrease transmission power for 3226517_2
- `C10`: Increase A3 Offset threshold for 3259382_1
- `C11`: Add neighbor relationship between 3259382_1 and 3226517_2
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3226517_2
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3226517_2
- `C14`: Press down the tilt angle of 3259382_1 by 3 degrees
- `C15`: Decrease transmission power for 3259382_1
- `C16`: Lift the tilt angle of 3259382_1 by 3 degrees
- `C17`: Increase transmission power for 3226517_2
- `C18`: Add neighbor relationship between 3269929_3 and 3226517_2
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3259382_1
- `C20`: Decrease A3 Offset threshold for 3226517_2
- `C21`: Lift the tilt angle  of 3226517_2 by 10 degrees
- `C22`: Decrease A3 Offset threshold for 3259382_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.625 | MS1 | 121.4656587511 | 31.1446231094 | 666 | 504990 | -86.17 | 17.50 | 466.08 | 0.16 | 2.91 | 1585 |
| 2024-09-20 22:21:32.693 | MS1 | 121.4656646272 | 31.1446263324 | 666 | 504990 | -89.80 | 17.21 | 345.14 | 0.13 | 2.94 | 1572 |
| 2024-09-20 22:21:33.829 | MS1 | 121.4656649584 | 31.1446321958 | 666 | 504990 | -85.58 | 16.05 | 449.89 | 0.04 | 2.87 | 1568 |
| 2024-09-20 22:21:34.721 | MS1 | 121.4656601565 | 31.1446274746 | 666 | 504990 | -90.55 | 12.53 | 54.40 | 0.54 | 2.20 | 658 |
| 2024-09-20 22:21:35.817 | MS1 | 121.4656738718 | 31.1446261936 | 666 | 504990 | -88.61 | 13.86 | 60.88 | 0.55 | 2.25 | 507 |
| 2024-09-20 22:21:36.427 | MS1 | 121.4656711925 | 31.1446375636 | 666 | 504990 | -91.77 | 15.92 | 63.84 | 0.58 | 2.01 | 501 |
| 2024-09-20 22:21:37.877 | MS1 | 121.4656599173 | 31.1446216399 | 666 | 504990 | -93.30 | 11.51 | 85.32 | 0.55 | 2.20 | 506 |
| 2024-09-20 22:21:38.853 | MS1 | 121.4656753633 | 31.1446322510 | 666 | 504990 | -90.84 | 12.67 | 64.29 | 0.60 | 2.48 | 694 |
| 2024-09-20 22:21:39.427 | MS1 | 121.4656601708 | 31.1446217901 | 666 | 504990 | -91.08 | 8.90 | 67.44 | 0.53 | 2.76 | 647 |
| 2024-09-20 22:21:40.155 | MS1 | 121.4656651974 | 31.1446286050 | 666 | 504990 | -89.07 | 11.69 | 540.22 | 0.18 | 2.67 | 1576 |
| 2024-09-20 22:21:41.851 | MS1 | 121.4656738043 | 31.1446336217 | 666 | 504990 | -91.92 | 12.24 | 499.16 | 0.14 | 2.18 | 1582 |
| 2024-09-20 22:21:42.907 | MS1 | 121.4656711502 | 31.1446181090 | 666 | 504990 | -93.96 | 12.59 | 331.47 | 0.08 | 2.94 | 1593 |

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
| 3219048 | 4 | 121.4655822524 | 31.1483399406 | 179 | 7 | 11 | 28.7 | TDD | 370 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3226517 | 2 | 121.4674338690 | 31.1510385827 | 334 | 13 | 11 | 44.1 | TDD | 628 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3259382 | 1 | 121.4744705250 | 31.1511199976 | 185 | 2 | 2 | 21.5 | TDD | 666 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3269929 | 3 | 121.4656674495 | 31.1513031321 | 211 | 12 | 5 | 31.3 | TDD | 269 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:31.422 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.437 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.563 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.563 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.251 | NREventA3 | measId:2;ServCellPCI:853;Se... |
| 2024-09-20 22:21:38.491 | NRHandoverAttempt | SourcePCI:853;SourceNR-ARFC... |
| 2024-09-20 22:21:38.537 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.551 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.690 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.690 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3259382 | 1 | 9.9145 | 18.4288 | -116.4795 | 19.6096 | 164.9619 | 0.0142 | 0.0165 |
| 2024_09_20 22:00 | 3226517 | 2 | 10.4549 | 15.7892 | -114.7667 | 19.6720 | 175.4706 | 0.0068 | 0.0060 |
| 2024_09_20 22:00 | 3269929 | 3 | 6.8623 | 19.7852 | -117.8943 | 11.1564 | 80.8206 | 0.0077 | 0.0090 |
| 2024_09_20 22:00 | 3219048 | 4 | 19.5568 | 18.4220 | -114.3099 | 13.3469 | 124.5958 | 0.0193 | 0.0040 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412610_668459B7 | 504990 | 666 | -90.1 | 504990 | 628 | -96.0 | 504990 | 269 | -97.9 | 504990 | 370 |
| MR_1774412610_9F37D0BD | 504990 | 666 | -91.1 | 504990 | 628 | -95.2 | 504990 | 269 | -100.0 | 504990 | 370 |
| MR_1774412610_F0E89DD6 | 504990 | 666 | -91.6 | 504990 | 628 | -97.4 | 504990 | 269 | -100.0 | 504990 | 370 |
| MR_1774412610_37672D35 | 504990 | 666 | -91.5 | 504990 | 628 | -98.0 | 504990 | 269 | -99.5 | 504990 | 370 |
| MR_1774412610_1ECDBDD9 | 504990 | 666 | -90.1 | 504990 | 628 | -95.2 | 504990 | 269 | -99.6 | 504990 | 370 |
| MR_1774412610_703F1DCB | 504990 | 666 | -90.8 | 504990 | 628 | -95.2 | 504990 | 269 | -99.0 | 504990 | 370 |
| MR_1774412610_1F2D9C06 | 504990 | 666 | -91.2 | 504990 | 628 | -94.6 | 504990 | 269 | -96.6 | 504990 | 370 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1345: `c8a265e4-f0e...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `c8a265e4-f0e2-42e8-b4dc-a7211ea27a3f` |
| Tag | **single-answer** |
| 정답 | **C10** |
| C10 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1345] topology](images/train_1345.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3210985_4
- `C2`: Press down the tilt angle of 3210985_4 by 10 degrees
- `C3`: Lift the tilt angle  of 3212625_1 by 10 degrees
- `C4`: Decrease A3 Offset threshold for 3212625_1
- `C5`: Increase transmission power for 3212625_1
- `C6`: Adjust the azimuth of 3212625_1 by 50 degrees
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3210985_4
- `C8`: Decrease transmission power for 3212625_1
- `C9`: Increase A3 Offset threshold for 3210985_4
- `C10`: Insufficient data; more data is needed for judgment. **← 정답**
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3212625_1
- `C12`: Add neighbor relationship between 3210985_4 and 3212625_1
- `C13`: Check test server and transmission issues
- `C14`: Press down the tilt angle  of 3212625_1 by 10 degrees
- `C15`: Decrease A3 Offset threshold for 3210985_4
- `C16`: Add neighbor relationship between 3272850_2 and 3212625_1
- `C17`: Adjust the azimuth of 3210985_4 by 33 degrees
- `C18`: Decrease transmission power for 3210985_4
- `C19`: Increase transmission power for 3210985_4
- `C20`: Increase A3 Offset threshold for 3212625_1
- `C21`: Lift the tilt angle of 3210985_4 by 10 degrees
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3212625_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.936 | MS1 | 121.4656770744 | 31.1446239077 | 782 | 504990 | -87.73 | 17.82 | 316.59 | 0.03 | 2.70 | 1567 |
| 2024-09-20 22:21:32.687 | MS1 | 121.4656620889 | 31.1446304164 | 782 | 504990 | -88.45 | 15.45 | 382.73 | 0.02 | 2.97 | 1583 |
| 2024-09-20 22:21:33.735 | MS1 | 121.4656639901 | 31.1446307033 | 782 | 504990 | -90.39 | 16.14 | 484.17 | 0.18 | 2.70 | 1596 |
| 2024-09-20 22:21:34.210 | MS1 | 121.4656594919 | 31.1446194045 | 782 | 504990 | -89.98 | 12.13 | 54.46 | 0.02 | 2.01 | 1600 |
| 2024-09-20 22:21:35.616 | MS1 | 121.4656683454 | 31.1446211930 | 782 | 504990 | -91.04 | 12.21 | 91.79 | 0.14 | 2.13 | 1577 |
| 2024-09-20 22:21:36.515 | MS1 | 121.4656593864 | 31.1446315606 | 782 | 504990 | -91.22 | 13.19 | 76.80 | 0.02 | 2.19 | 1599 |
| 2024-09-20 22:21:37.527 | MS1 | 121.4656615784 | 31.1446372527 | 782 | 504990 | -89.87 | 11.47 | 100.43 | 0.18 | 2.60 | 1572 |
| 2024-09-20 22:21:38.472 | MS1 | 121.4656588784 | 31.1446250441 | 782 | 504990 | -90.26 | 12.86 | 93.24 | 0.09 | 2.71 | 1568 |
| 2024-09-20 22:21:39.772 | MS1 | 121.4656589035 | 31.1446314339 | 782 | 504990 | -89.40 | 12.81 | 88.69 | 0.19 | 2.16 | 1576 |
| 2024-09-20 22:21:40.455 | MS1 | 121.4656765729 | 31.1446222117 | 782 | 504990 | -90.41 | 10.18 | 455.89 | 0.14 | 2.10 | 1581 |
| 2024-09-20 22:21:41.699 | MS1 | 121.4656707420 | 31.1446372656 | 782 | 504990 | -89.45 | 7.91 | 387.44 | 0.16 | 2.69 | 1572 |
| 2024-09-20 22:21:42.322 | MS1 | 121.4656623636 | 31.1446273851 | 782 | 504990 | -93.34 | 10.28 | 577.92 | 0.09 | 2.46 | 1569 |

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
| 3210985 | 4 | 121.4752084167 | 31.1552983988 | 250 | 15 | 1 | 34.0 | TDD | 782 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3212625 | 1 | 121.4693483601 | 31.1461934956 | 320 | 13 | 3 | 24.1 | TDD | 633 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3264009 | 3 | 121.4735580858 | 31.1524451276 | 258 | 5 | 9 | 20.7 | TDD | 506 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3272850 | 2 | 121.4662612343 | 31.1513174471 | 69 | 14 | 3 | 23.4 | TDD | 210 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |

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
| 2024-09-20 22:21:31.128 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.143 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.272 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.272 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.935 | NREventA3 | measId:2;ServCellPCI:647;Se... |
| 2024-09-20 22:21:38.175 | NRHandoverAttempt | SourcePCI:647;SourceNR-ARFC... |
| 2024-09-20 22:21:38.218 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.233 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.372 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.372 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3212625 | 1 | 75.5354 | 76.4519 | -115.8491 | 15.4662 | 151.1506 | 0.0048 | 0.0108 |
| 2024_09_19 22:00 | 3272850 | 2 | 90.3792 | 76.2392 | -115.5973 | 17.6425 | 113.3350 | 0.0029 | 0.0023 |
| 2024_09_19 22:00 | 3264009 | 3 | 84.1054 | 82.3849 | -115.3255 | 18.0452 | 131.2444 | 0.0194 | 0.0175 |
| 2024_09_19 22:00 | 3210985 | 4 | 94.4754 | 76.8947 | -114.4256 | 11.1562 | 139.1105 | 0.0161 | 0.0105 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416767_97628C01 | 504990 | 782 | -91.7 | 504990 | 633 | -96.2 | 504990 | 210 | -96.8 | 504990 | 506 |
| MR_1774416767_8BD034E8 | 504990 | 782 | -90.9 | 504990 | 633 | -97.7 | 504990 | 210 | -96.1 | 504990 | 506 |
| MR_1774416767_3A3B6E16 | 504990 | 782 | -91.6 | 504990 | 633 | -98.1 | 504990 | 210 | -98.1 | 504990 | 506 |
| MR_1774416767_93ECF5E4 | 504990 | 782 | -90.6 | 504990 | 633 | -95.6 | 504990 | 210 | -98.1 | 504990 | 506 |
| MR_1774416767_6C45C550 | 504990 | 782 | -90.4 | 504990 | 633 | -97.8 | 504990 | 210 | -95.8 | 504990 | 506 |
| MR_1774416767_4B2A9550 | 504990 | 782 | -91.8 | 504990 | 633 | -97.8 | 504990 | 210 | -96.6 | 504990 | 506 |
| MR_1774416767_3868D84B | 504990 | 782 | -91.0 | 504990 | 633 | -98.9 | 504990 | 210 | -97.7 | 504990 | 506 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1346: `367d402a-531...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `367d402a-531e-42a0-b77a-42bebae63ade` |
| Tag | **single-answer** |
| 정답 | **C8** |
| C8 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3259841_2 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1346] topology](images/train_1346.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3259841_2
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3221723_3
- `C3`: Decrease A3 Offset threshold for 3259841_2
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3221723_3
- `C5`: Lift the tilt angle of 3259841_2 by 3 degrees
- `C6`: Insufficient data; more data is needed for judgment.
- `C7`: Adjust the azimuth of 3221723_3 by 50 degrees
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3259841_2 **← 정답**
- `C9`: Adjust the azimuth of 3259841_2 by 10 degrees
- `C10`: Press down the tilt angle  of 3221723_3 by 10 degrees
- `C11`: Check test server and transmission issues
- `C12`: Add neighbor relationship between 3273761_1 and 3221723_3
- `C13`: Decrease transmission power for 3221723_3
- `C14`: Increase A3 Offset threshold for 3259841_2
- `C15`: Increase transmission power for 3221723_3
- `C16`: Press down the tilt angle of 3259841_2 by 3 degrees
- `C17`: Add neighbor relationship between 3259841_2 and 3221723_3
- `C18`: Increase transmission power for 3259841_2
- `C19`: Increase A3 Offset threshold for 3221723_3
- `C20`: Lift the tilt angle  of 3221723_3 by 10 degrees
- `C21`: Decrease transmission power for 3259841_2
- `C22`: Decrease A3 Offset threshold for 3221723_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.340 | MS1 | 121.4656676738 | 31.1446214222 | 358 | 504990 | -86.77 | 13.91 | 513.27 | 0.12 | 2.85 | 1561 |
| 2024-09-20 22:21:32.171 | MS1 | 121.4656656850 | 31.1446212386 | 358 | 504990 | -89.82 | 13.97 | 491.88 | 0.10 | 2.84 | 1593 |
| 2024-09-20 22:21:33.303 | MS1 | 121.4656767281 | 31.1446284140 | 358 | 504990 | -86.07 | 16.89 | 522.92 | 0.04 | 2.47 | 1589 |
| 2024-09-20 22:21:34.487 | MS1 | 121.4656592441 | 31.1446282343 | 358 | 504990 | -90.33 | 14.10 | 50.66 | 0.55 | 2.82 | 686 |
| 2024-09-20 22:21:35.947 | MS1 | 121.4656717576 | 31.1446216477 | 358 | 504990 | -85.80 | 13.81 | 80.75 | 0.61 | 2.78 | 547 |
| 2024-09-20 22:21:36.940 | MS1 | 121.4656591127 | 31.1446256213 | 358 | 504990 | -89.48 | 15.76 | 84.63 | 0.50 | 2.05 | 585 |
| 2024-09-20 22:21:37.172 | MS1 | 121.4656734095 | 31.1446302175 | 358 | 504990 | -89.51 | 10.11 | 97.21 | 0.54 | 2.32 | 673 |
| 2024-09-20 22:21:38.863 | MS1 | 121.4656669883 | 31.1446349435 | 358 | 504990 | -91.90 | 10.61 | 69.46 | 0.61 | 2.71 | 659 |
| 2024-09-20 22:21:39.258 | MS1 | 121.4656726297 | 31.1446293887 | 358 | 504990 | -93.56 | 8.87 | 95.79 | 0.62 | 2.53 | 616 |
| 2024-09-20 22:21:40.385 | MS1 | 121.4656763173 | 31.1446292999 | 358 | 504990 | -93.17 | 8.07 | 339.54 | 0.01 | 2.81 | 1570 |
| 2024-09-20 22:21:41.250 | MS1 | 121.4656718951 | 31.1446297120 | 358 | 504990 | -93.71 | 8.29 | 300.82 | 0.00 | 2.77 | 1570 |
| 2024-09-20 22:21:42.153 | MS1 | 121.4656755491 | 31.1446182622 | 358 | 504990 | -91.42 | 9.66 | 376.73 | 0.10 | 2.34 | 1592 |

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
| 3221723 | 3 | 121.4743631737 | 31.1452755791 | 97 | 14 | 9 | 36.2 | TDD | 142 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3239071 | 4 | 121.4699058627 | 31.1472968835 | 122 | 3 | 2 | 26.2 | TDD | 755 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3259841 | 2 | 121.4654564217 | 31.1522649274 | 169 | 0 | 2 | 44.7 | TDD | 358 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3273761 | 1 | 121.4643816472 | 31.1466645613 | 267 | 13 | 5 | 43.9 | TDD | 362 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |

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
| 2024-09-20 22:21:31.281 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.303 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.423 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.423 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.176 | NREventA3 | measId:2;ServCellPCI:575;Se... |
| 2024-09-20 22:21:38.416 | NRHandoverAttempt | SourcePCI:575;SourceNR-ARFC... |
| 2024-09-20 22:21:38.456 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.469 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.587 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.587 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3273761 | 1 | 5.9430 | 9.7452 | -114.6087 | 14.8833 | 130.4290 | 0.0039 | 0.0088 |
| 2024_09_20 22:00 | 3259841 | 2 | 16.3208 | 10.9595 | -117.5843 | 7.4514 | 189.2566 | 0.0036 | 0.0015 |
| 2024_09_20 22:00 | 3221723 | 3 | 6.1026 | 13.8950 | -115.0814 | 10.2602 | 160.9368 | 0.0117 | 0.0107 |
| 2024_09_20 22:00 | 3239071 | 4 | 6.6486 | 19.6247 | -116.6287 | 19.4750 | 129.4991 | 0.0177 | 0.0053 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415654_3D576094 | 504990 | 358 | -91.1 | 504990 | 142 | -97.5 | 504990 | 362 | -100.4 | 504990 | 755 |
| MR_1774415654_AAB2C8DE | 504990 | 358 | -90.2 | 504990 | 142 | -96.6 | 504990 | 362 | -100.2 | 504990 | 755 |
| MR_1774415654_8AD27CED | 504990 | 358 | -91.9 | 504990 | 142 | -98.9 | 504990 | 362 | -100.1 | 504990 | 755 |
| MR_1774415654_6EC44733 | 504990 | 358 | -92.0 | 504990 | 142 | -100.4 | 504990 | 362 | -100.3 | 504990 | 755 |
| MR_1774415654_9F0A9073 | 504990 | 358 | -89.4 | 504990 | 142 | -99.3 | 504990 | 362 | -100.8 | 504990 | 755 |
| MR_1774415654_97AE32EB | 504990 | 358 | -91.3 | 504990 | 142 | -99.3 | 504990 | 362 | -100.8 | 504990 | 755 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1347: `aa0e0741-4b9...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `aa0e0741-4b90-4b4d-a99e-e8d69f96fcb0` |
| Tag | **single-answer** |
| 정답 | **C17** |
| C17 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1347] topology](images/train_1347.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3258025_4
- `C2`: Decrease transmission power for 3258025_4
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3258025_4
- `C4`: Decrease A3 Offset threshold for 3237984_1
- `C5`: Increase A3 Offset threshold for 3237984_1
- `C6`: Increase transmission power for 3237984_1
- `C7`: Insufficient data; more data is needed for judgment.
- `C8`: Increase A3 Offset threshold for 3258025_4
- `C9`: Lift the tilt angle  of 3237984_1 by 9 degrees
- `C10`: Press down the tilt angle of 3258025_4 by 10 degrees
- `C11`: Decrease transmission power for 3237984_1
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3237984_1
- `C13`: Increase transmission power for 3258025_4
- `C14`: Decrease A3 Offset threshold for 3258025_4
- `C15`: Press down the tilt angle  of 3237984_1 by 9 degrees
- `C16`: Adjust the azimuth of 3258025_4 by 50 degrees
- `C17`: Check test server and transmission issues **← 정답**
- `C18`: Add neighbor relationship between 3213513_2 and 3237984_1
- `C19`: Add neighbor relationship between 3258025_4 and 3237984_1
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3237984_1
- `C21`: Adjust the azimuth of 3237984_1 by 50 degrees
- `C22`: Lift the tilt angle of 3258025_4 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.947 | MS1 | 121.4656639004 | 31.1446274297 | 391 | 504990 | -91.06 | 13.41 | 581.15 | 0.07 | 2.93 | 1568 |
| 2024-09-20 22:21:32.574 | MS1 | 121.4656652858 | 31.1446205330 | 391 | 504990 | -88.88 | 14.36 | 568.85 | 0.19 | 2.12 | 1570 |
| 2024-09-20 22:21:33.944 | MS1 | 121.4656609476 | 31.1446194534 | 391 | 504990 | -91.70 | 17.92 | 329.51 | 0.12 | 2.26 | 1592 |
| 2024-09-20 22:21:34.248 | MS1 | 121.4656707262 | 31.1446339542 | 391 | 504990 | -89.95 | 16.72 | 104.56 | 0.10 | 2.51 | 357 |
| 2024-09-20 22:21:35.591 | MS1 | 121.4656676502 | 31.1446366420 | 391 | 504990 | -89.61 | 17.43 | 88.90 | 0.18 | 2.08 | 375 |
| 2024-09-20 22:21:36.519 | MS1 | 121.4656652014 | 31.1446276607 | 391 | 504990 | -85.81 | 16.88 | 78.31 | 0.20 | 2.16 | 333 |
| 2024-09-20 22:21:37.962 | MS1 | 121.4656600578 | 31.1446328472 | 391 | 504990 | -92.22 | 10.08 | 60.58 | 0.04 | 2.95 | 343 |
| 2024-09-20 22:21:38.271 | MS1 | 121.4656612801 | 31.1446214602 | 391 | 504990 | -89.91 | 9.56 | 83.96 | 0.03 | 2.93 | 450 |
| 2024-09-20 22:21:39.789 | MS1 | 121.4656621664 | 31.1446202796 | 391 | 504990 | -93.86 | 7.49 | 80.83 | 0.06 | 2.65 | 484 |
| 2024-09-20 22:21:40.878 | MS1 | 121.4656602333 | 31.1446355818 | 391 | 504990 | -91.01 | 12.07 | 460.35 | 0.20 | 2.29 | 1598 |
| 2024-09-20 22:21:41.116 | MS1 | 121.4656682370 | 31.1446261976 | 391 | 504990 | -89.06 | 12.57 | 501.12 | 0.04 | 2.98 | 1594 |
| 2024-09-20 22:21:42.336 | MS1 | 121.4656656533 | 31.1446356558 | 391 | 504990 | -90.54 | 12.60 | 521.97 | 0.18 | 2.92 | 1565 |

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
| 3213513 | 2 | 121.4648902539 | 31.1551707224 | 259 | 0 | 12 | 21.5 | TDD | 315 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3237984 | 1 | 121.4708192665 | 31.1469786286 | 330 | 7 | 7 | 22.8 | TDD | 138 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3258025 | 4 | 121.4720006965 | 31.1472695256 | 48 | 10 | 7 | 39.3 | TDD | 391 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3278825 | 3 | 121.4702549481 | 31.1463089209 | 344 | 4 | 3 | 35.0 | TDD | 237 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |

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
| 2024-09-20 22:21:31.250 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.265 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.415 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.415 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.127 | NREventA3 | measId:2;ServCellPCI:308;Se... |
| 2024-09-20 22:21:38.367 | NRHandoverAttempt | SourcePCI:308;SourceNR-ARFC... |
| 2024-09-20 22:21:38.402 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.417 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.546 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.546 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3237984 | 1 | 18.7662 | 18.6306 | -115.9729 | 10.9021 | 199.7445 | 0.0163 | 0.0024 |
| 2024_09_20 22:00 | 3213513 | 2 | 19.7874 | 8.5718 | -117.3728 | 6.2984 | 173.9639 | 0.0134 | 0.0092 |
| 2024_09_20 22:00 | 3278825 | 3 | 13.8242 | 6.3264 | -116.7165 | 8.1692 | 171.6266 | 0.0090 | 0.0189 |
| 2024_09_20 22:00 | 3258025 | 4 | 12.0060 | 7.0874 | -117.8355 | 6.6200 | 163.8637 | 0.0048 | 0.0006 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414235_5A66F192 | 504990 | 391 | -89.8 | 504990 | 138 | -98.2 | 504990 | 315 | -101.2 | 504990 | 237 |
| MR_1774414235_3CAA1097 | 504990 | 391 | -91.1 | 504990 | 138 | -97.5 | 504990 | 315 | -100.8 | 504990 | 237 |
| MR_1774414235_3A2269B5 | 504990 | 391 | -91.3 | 504990 | 138 | -98.8 | 504990 | 315 | -100.3 | 504990 | 237 |
| MR_1774414235_E553CA31 | 504990 | 391 | -90.2 | 504990 | 138 | -100.2 | 504990 | 315 | -98.7 | 504990 | 237 |
| MR_1774414235_A57A1EB2 | 504990 | 391 | -88.4 | 504990 | 138 | -99.9 | 504990 | 315 | -97.4 | 504990 | 237 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1348: `1db8c85e-7d6...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `1db8c85e-7d68-4067-90ad-0b152893c3a7` |
| Tag | **single-answer** |
| 정답 | **C6** |
| C6 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1348] topology](images/train_1348.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3266421_2
- `C2`: Decrease transmission power for 3260569_3
- `C3`: Add neighbor relationship between 3260569_3 and 3266421_2
- `C4`: Lift the tilt angle  of 3266421_2 by 2 degrees
- `C5`: Insufficient data; more data is needed for judgment.
- `C6`: Check test server and transmission issues **← 정답**
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3266421_2
- `C8`: Decrease transmission power for 3266421_2
- `C9`: Adjust the azimuth of 3260569_3 by 50 degrees
- `C10`: Increase transmission power for 3266421_2
- `C11`: Lift the tilt angle of 3260569_3 by 6 degrees
- `C12`: Increase A3 Offset threshold for 3260569_3
- `C13`: Add neighbor relationship between 3268347_1 and 3266421_2
- `C14`: Increase A3 Offset threshold for 3266421_2
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3260569_3
- `C16`: Decrease A3 Offset threshold for 3266421_2
- `C17`: Press down the tilt angle of 3260569_3 by 6 degrees
- `C18`: Decrease A3 Offset threshold for 3260569_3
- `C19`: Adjust the azimuth of 3266421_2 by 50 degrees
- `C20`: Press down the tilt angle  of 3266421_2 by 2 degrees
- `C21`: Increase transmission power for 3260569_3
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3260569_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.575 | MS1 | 121.4656644741 | 31.1446314304 | 508 | 504990 | -89.97 | 15.49 | 541.66 | 0.02 | 2.79 | 1572 |
| 2024-09-20 22:21:32.644 | MS1 | 121.4656742013 | 31.1446297352 | 508 | 504990 | -91.25 | 13.99 | 381.36 | 0.05 | 2.89 | 1577 |
| 2024-09-20 22:21:33.377 | MS1 | 121.4656692792 | 31.1446198382 | 508 | 504990 | -89.46 | 13.53 | 395.78 | 0.03 | 2.32 | 1582 |
| 2024-09-20 22:21:34.893 | MS1 | 121.4656723097 | 31.1446320142 | 508 | 504990 | -85.33 | 15.41 | 74.23 | 0.08 | 2.49 | 469 |
| 2024-09-20 22:21:35.421 | MS1 | 121.4656690428 | 31.1446273176 | 508 | 504990 | -87.55 | 17.12 | 78.86 | 0.01 | 2.38 | 346 |
| 2024-09-20 22:21:36.155 | MS1 | 121.4656765442 | 31.1446262263 | 508 | 504990 | -90.67 | 16.87 | 97.69 | 0.13 | 2.00 | 337 |
| 2024-09-20 22:21:37.857 | MS1 | 121.4656717273 | 31.1446303532 | 508 | 504990 | -91.67 | 7.07 | 90.07 | 0.04 | 2.72 | 469 |
| 2024-09-20 22:21:38.217 | MS1 | 121.4656676790 | 31.1446194189 | 508 | 504990 | -92.96 | 11.62 | 93.05 | 0.04 | 2.15 | 406 |
| 2024-09-20 22:21:39.839 | MS1 | 121.4656763046 | 31.1446212085 | 508 | 504990 | -93.92 | 8.56 | 68.75 | 0.19 | 2.62 | 437 |
| 2024-09-20 22:21:40.956 | MS1 | 121.4656669734 | 31.1446205700 | 508 | 504990 | -92.40 | 12.43 | 349.44 | 0.08 | 2.34 | 1562 |
| 2024-09-20 22:21:41.969 | MS1 | 121.4656584724 | 31.1446216133 | 508 | 504990 | -89.26 | 7.03 | 455.29 | 0.11 | 2.54 | 1565 |
| 2024-09-20 22:21:42.178 | MS1 | 121.4656730682 | 31.1446314216 | 508 | 504990 | -90.98 | 9.70 | 478.83 | 0.12 | 2.38 | 1573 |

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
| 3260569 | 3 | 121.4684114810 | 31.1541128214 | 73 | 4 | 1 | 39.9 | TDD | 508 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3266421 | 2 | 121.4757436570 | 31.1540468750 | 10 | 1 | 10 | 23.9 | TDD | 707 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3268347 | 1 | 121.4712387448 | 31.1482510242 | 258 | 0 | 9 | 25.5 | TDD | 417 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3270663 | 4 | 121.4729446790 | 31.1552911380 | 74 | 9 | 1 | 44.5 | TDD | 249 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:31.516 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.533 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.639 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.639 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.348 | NREventA3 | measId:2;ServCellPCI:886;Se... |
| 2024-09-20 22:21:38.588 | NRHandoverAttempt | SourcePCI:886;SourceNR-ARFC... |
| 2024-09-20 22:21:38.619 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.633 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.781 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.781 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3268347 | 1 | 7.9235 | 13.5115 | -115.5828 | 7.4282 | 184.0814 | 0.0112 | 0.0125 |
| 2024_09_20 22:00 | 3266421 | 2 | 8.7588 | 5.4892 | -116.3637 | 12.2078 | 117.3690 | 0.0049 | 0.0157 |
| 2024_09_20 22:00 | 3260569 | 3 | 9.9161 | 14.6448 | -114.8142 | 9.6179 | 110.0989 | 0.0172 | 0.0094 |
| 2024_09_20 22:00 | 3270663 | 4 | 12.7033 | 15.4910 | -117.5506 | 8.5693 | 191.5164 | 0.0189 | 0.0136 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415731_CDE5E50F | 504990 | 508 | -86.8 | 504990 | 707 | -88.3 | 504990 | 417 | -92.8 | 504990 | 249 |
| MR_1774415731_514529EA | 504990 | 508 | -83.4 | 504990 | 707 | -89.4 | 504990 | 417 | -90.8 | 504990 | 249 |
| MR_1774415731_4FE63AAA | 504990 | 508 | -84.3 | 504990 | 707 | -90.0 | 504990 | 417 | -93.6 | 504990 | 249 |
| MR_1774415731_E0F89EB8 | 504990 | 508 | -86.3 | 504990 | 707 | -89.4 | 504990 | 417 | -92.6 | 504990 | 249 |
| MR_1774415731_BD72B59C | 504990 | 508 | -86.5 | 504990 | 707 | -89.4 | 504990 | 417 | -94.2 | 504990 | 249 |
| MR_1774415731_E76A23DF | 504990 | 508 | -85.6 | 504990 | 707 | -88.7 | 504990 | 417 | -90.8 | 504990 | 249 |
| MR_1774415731_9913E2EE | 504990 | 508 | -86.7 | 504990 | 707 | -88.0 | 504990 | 417 | -93.2 | 504990 | 249 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1349: `bf44b7e6-9c1...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `bf44b7e6-9c18-495e-ae97-d49b13230b05` |
| Tag | **multiple-answer** |
| 정답 | **C1|C20** |
| C1 의미 | Decrease transmission power for 3263881_4 |
| C20 의미 | Press down the tilt angle  of 3263881_4 by 4 degrees |
| 패턴 분류 | **P3 Overshoot (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1349] topology](images/train_1349.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3263881_4 **← 정답**
- `C2`: Increase A3 Offset threshold for 3263881_4
- `C3`: Adjust the azimuth of 3263881_4 by 18 degrees
- `C4`: Check test server and transmission issues
- `C5`: Decrease A3 Offset threshold for 3259873_3
- `C6`: Add neighbor relationship between 3248516_2 and 3263881_4
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3263881_4
- `C8`: Insufficient data; more data is needed for judgment.
- `C9`: Increase transmission power for 3263881_4
- `C10`: Increase transmission power for 3259873_3
- `C11`: Lift the tilt angle  of 3263881_4 by 4 degrees
- `C12`: Decrease transmission power for 3259873_3
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3259873_3
- `C14`: Decrease A3 Offset threshold for 3263881_4
- `C15`: Adjust the azimuth of 3259873_3 by 8 degrees
- `C16`: Press down the tilt angle of 3259873_3 by 2 degrees
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3263881_4
- `C18`: Increase A3 Offset threshold for 3259873_3
- `C19`: Lift the tilt angle of 3259873_3 by 2 degrees
- `C20`: Press down the tilt angle  of 3263881_4 by 4 degrees **← 정답**
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3259873_3
- `C22`: Add neighbor relationship between 3259873_3 and 3263881_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.173 | MS1 | 121.4656664049 | 31.1446305197 | 797 | 504990 | -79.29 | 16.66 | 596.52 | 0.19 | 2.83 | 1573 |
| 2024-09-20 22:21:32.458 | MS1 | 121.4656775736 | 31.1446183754 | 797 | 504990 | -75.97 | 17.21 | 522.45 | 0.13 | 2.68 | 1591 |
| 2024-09-20 22:21:33.339 | MS1 | 121.4656664122 | 31.1446357796 | 797 | 504990 | -83.11 | 14.82 | 603.90 | 0.04 | 2.17 | 1597 |
| 2024-09-20 22:21:34.553 | MS1 | 121.4656590597 | 31.1446258070 | 797 | 504990 | -93.10 | 3.97 | 87.62 | 0.07 | 1.16 | 1599 |
| 2024-09-20 22:21:35.923 | MS1 | 121.4656690932 | 31.1446292744 | 797 | 504990 | -90.78 | 0.83 | 47.48 | 0.11 | 1.27 | 1566 |
| 2024-09-20 22:21:36.976 | MS1 | 121.4656714679 | 31.1446279431 | 797 | 504990 | -90.86 | 3.19 | 41.23 | 0.14 | 1.11 | 1593 |
| 2024-09-20 22:21:37.898 | MS1 | 121.4656674633 | 31.1446231018 | 797 | 504990 | -94.02 | 3.31 | 75.65 | 0.15 | 1.46 | 1569 |
| 2024-09-20 22:21:38.700 | MS1 | 121.4656584293 | 31.1446282753 | 797 | 504990 | -93.21 | 2.04 | 47.86 | 0.07 | 1.21 | 1600 |
| 2024-09-20 22:21:39.658 | MS1 | 121.4656640827 | 31.1446200227 | 797 | 504990 | -92.68 | 0.29 | 53.55 | 0.18 | 1.12 | 1596 |
| 2024-09-20 22:21:40.860 | MS1 | 121.4656661460 | 31.1446308648 | 797 | 504990 | -76.77 | 16.69 | 330.98 | 0.19 | 2.14 | 1595 |
| 2024-09-20 22:21:41.328 | MS1 | 121.4656666293 | 31.1446234585 | 797 | 504990 | -79.85 | 15.56 | 490.10 | 0.10 | 2.95 | 1588 |
| 2024-09-20 22:21:42.864 | MS1 | 121.4656701999 | 31.1446271864 | 797 | 504990 | -76.51 | 12.80 | 381.75 | 0.15 | 2.26 | 1591 |

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
| 3248516 | 2 | 121.4710660280 | 31.1452252721 | 180 | 2 | 11 | 15.5 | TDD | 508 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3259873 | 3 | 121.4690865944 | 31.1518671672 | 194 | 1 | 8 | 17.1 | TDD | 797 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3263881 | 4 | 121.4695549134 | 31.1509433998 | 190 | 3 | 1 | 16.2 | TDD | 702 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3270586 | 1 | 121.4696527463 | 31.1524803018 | 224 | 1 | 4 | 17.7 | TDD | 971 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:31.302 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.324 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.454 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.454 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3270586 | 1 | 12.0901 | 11.0950 | -115.4446 | 10.8299 | 127.1505 | 0.0161 | 0.0017 |
| 2024_09_20 22:00 | 3248516 | 2 | 13.5755 | 18.6256 | -114.9120 | 7.2487 | 164.7042 | 0.0189 | 0.0137 |
| 2024_09_20 22:00 | 3259873 | 3 | 14.5216 | 10.5522 | -109.4532 | 12.5472 | 181.8870 | 0.0013 | 0.0082 |
| 2024_09_20 22:00 | 3263881 | 4 | 16.1335 | 17.9381 | -116.6336 | 6.4894 | 86.2347 | 0.0073 | 0.0100 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415580_5D544342 | 504990 | 797 | -92.4 | 504990 | 702 | -90.9 | 504990 | 508 | -92.6 | 504990 | 971 |
| MR_1774415580_9F00FA64 | 504990 | 702 | -93.5 | 504990 | 797 | -91.7 | 504990 | 508 | -93.4 | 504990 | 971 |
| MR_1774415580_F9AA865D | 504990 | 797 | -94.1 | 504990 | 702 | -88.3 | 504990 | 508 | -93.0 | 504990 | 971 |
| MR_1774415580_25B2E763 | 504990 | 797 | -94.2 | 504990 | 702 | -88.5 | 504990 | 508 | -93.3 | 504990 | 971 |
| MR_1774415580_86D25C67 | 504990 | 702 | -94.1 | 504990 | 797 | -89.4 | 504990 | 508 | -95.5 | 504990 | 971 |

> *... 2개 열 생략 (전체 14열)*

---
