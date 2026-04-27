# Track A 문제 분석 — train[820]~train[829]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[820] ~ train[829] (10개)

## 목차

1. [문제 820: `d85c39a5-834...`](#820) — single-answer, 정답: C2
2. [문제 821: `ec1ba133-380...`](#821) — single-answer, 정답: C21
3. [문제 822: `a51cd4f1-eba...`](#822) — single-answer, 정답: C4
4. [문제 823: `220469e4-945...`](#823) — single-answer, 정답: C19
5. [문제 824: `265d96d1-323...`](#824) — multiple-answer, 정답: C1|C7
6. [문제 825: `02553df1-21c...`](#825) — single-answer, 정답: C9
7. [문제 826: `a5f1ebf9-8d0...`](#826) — single-answer, 정답: C17
8. [문제 827: `977da08b-86f...`](#827) — single-answer, 정답: C3
9. [문제 828: `ce3e0d77-9e9...`](#828) — single-answer, 정답: C3
10. [문제 829: `91206e7d-777...`](#829) — single-answer, 정답: C11

---

### 문제 820: `d85c39a5-834...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `d85c39a5-8341-4ece-80a3-c2e1a98bf74a` |
| Tag | **single-answer** |
| 정답 | **C2** |
| C2 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3251709_2 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[820] topology](images/train_0820.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3251709_2
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3251709_2 **← 정답**
- `C3`: Adjust the azimuth of 3251709_2 by 20 degrees
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3226398_4
- `C5`: Press down the tilt angle  of 3226398_4 by 7 degrees
- `C6`: Check test server and transmission issues
- `C7`: Decrease A3 Offset threshold for 3251709_2
- `C8`: Insufficient data; more data is needed for judgment.
- `C9`: Adjust the azimuth of 3226398_4 by 50 degrees
- `C10`: Lift the tilt angle of 3251709_2 by 6 degrees
- `C11`: Decrease A3 Offset threshold for 3226398_4
- `C12`: Add neighbor relationship between 3251709_2 and 3226398_4
- `C13`: Press down the tilt angle of 3251709_2 by 6 degrees
- `C14`: Increase transmission power for 3226398_4
- `C15`: Increase A3 Offset threshold for 3226398_4
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3226398_4
- `C17`: Decrease transmission power for 3226398_4
- `C18`: Lift the tilt angle  of 3226398_4 by 7 degrees
- `C19`: Increase A3 Offset threshold for 3251709_2
- `C20`: Add neighbor relationship between 3264107_3 and 3226398_4
- `C21`: Decrease transmission power for 3251709_2
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3251709_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.580 | MS1 | 121.4656585782 | 31.1446203855 | 914 | 504990 | -91.99 | 17.86 | 373.97 | 0.10 | 2.31 | 1586 |
| 2024-09-20 22:21:32.779 | MS1 | 121.4656737250 | 31.1446220383 | 914 | 504990 | -85.55 | 15.61 | 400.70 | 0.17 | 2.32 | 1576 |
| 2024-09-20 22:21:33.788 | MS1 | 121.4656747942 | 31.1446298183 | 914 | 504990 | -85.45 | 17.88 | 421.43 | 0.04 | 2.08 | 1579 |
| 2024-09-20 22:21:34.444 | MS1 | 121.4656670485 | 31.1446334557 | 914 | 504990 | -87.13 | 16.49 | 57.45 | 0.65 | 2.61 | 552 |
| 2024-09-20 22:21:35.441 | MS1 | 121.4656671320 | 31.1446287998 | 914 | 504990 | -89.65 | 12.34 | 47.60 | 0.62 | 2.53 | 517 |
| 2024-09-20 22:21:36.676 | MS1 | 121.4656735627 | 31.1446342416 | 914 | 504990 | -90.10 | 15.97 | 79.40 | 0.66 | 2.48 | 500 |
| 2024-09-20 22:21:37.602 | MS1 | 121.4656742235 | 31.1446284743 | 914 | 504990 | -89.04 | 11.60 | 73.68 | 0.54 | 2.03 | 543 |
| 2024-09-20 22:21:38.999 | MS1 | 121.4656594055 | 31.1446190736 | 914 | 504990 | -91.20 | 8.40 | 81.89 | 0.60 | 2.35 | 583 |
| 2024-09-20 22:21:39.720 | MS1 | 121.4656594149 | 31.1446349113 | 914 | 504990 | -89.96 | 12.73 | 98.66 | 0.65 | 2.10 | 664 |
| 2024-09-20 22:21:40.322 | MS1 | 121.4656621894 | 31.1446210599 | 914 | 504990 | -92.04 | 8.78 | 500.52 | 0.06 | 2.66 | 1567 |
| 2024-09-20 22:21:41.502 | MS1 | 121.4656595399 | 31.1446263346 | 914 | 504990 | -93.82 | 9.64 | 341.79 | 0.07 | 2.24 | 1599 |
| 2024-09-20 22:21:42.241 | MS1 | 121.4656707705 | 31.1446295582 | 914 | 504990 | -91.32 | 8.32 | 293.68 | 0.14 | 2.53 | 1595 |

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
| 3213441 | 1 | 121.4681811285 | 31.1521153175 | 305 | 10 | 6 | 18.0 | TDD | 113 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3226398 | 4 | 121.4652692924 | 31.1548040435 | 359 | 6 | 0 | 21.0 | TDD | 406 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3251709 | 2 | 121.4672655227 | 31.1556399064 | 207 | 5 | 8 | 15.8 | TDD | 914 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3264107 | 3 | 121.4673428289 | 31.1463864345 | 256 | 14 | 7 | 45.4 | TDD | 757 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |

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
| 2024-09-20 22:21:30.886 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.908 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.020 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.020 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.780 | NREventA3 | measId:2;ServCellPCI:67;Ser... |
| 2024-09-20 22:21:38.020 | NRHandoverAttempt | SourcePCI:67;SourceNR-ARFCN... |
| 2024-09-20 22:21:38.060 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.071 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.211 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.211 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3213441 | 1 | 16.8891 | 19.3546 | -114.5587 | 15.3823 | 159.9612 | 0.0001 | 0.0140 |
| 2024_09_20 22:00 | 3251709 | 2 | 16.2619 | 12.5596 | -114.2108 | 10.0445 | 157.1166 | 0.0185 | 0.0174 |
| 2024_09_20 22:00 | 3264107 | 3 | 15.8024 | 17.5016 | -116.0116 | 9.9292 | 114.1153 | 0.0016 | 0.0156 |
| 2024_09_20 22:00 | 3226398 | 4 | 18.3565 | 17.4431 | -115.4363 | 9.8443 | 96.9579 | 0.0191 | 0.0038 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413340_B25AC799 | 504990 | 914 | -85.3 | 504990 | 406 | -93.0 | 504990 | 757 | -100.2 | 504990 | 113 |
| MR_1774413340_7DEA24C6 | 504990 | 914 | -87.2 | 504990 | 406 | -89.9 | 504990 | 757 | -98.0 | 504990 | 113 |
| MR_1774413340_68B813C9 | 504990 | 914 | -87.5 | 504990 | 406 | -91.3 | 504990 | 757 | -100.7 | 504990 | 113 |
| MR_1774413340_890E973B | 504990 | 914 | -89.1 | 504990 | 406 | -92.2 | 504990 | 757 | -99.4 | 504990 | 113 |
| MR_1774413340_006AAEEE | 504990 | 914 | -85.8 | 504990 | 406 | -91.5 | 504990 | 757 | -98.6 | 504990 | 113 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 821: `ec1ba133-380...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `ec1ba133-380e-419f-92be-c08564ab0db1` |
| Tag | **single-answer** |
| 정답 | **C21** |
| C21 의미 | Lift the tilt angle  of 3216113_4 by 5 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[821] topology](images/train_0821.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment.
- `C2`: Decrease A3 Offset threshold for 3250776_2
- `C3`: Press down the tilt angle of 3221185_1 by 6 degrees
- `C4`: Decrease transmission power for 3221185_1
- `C5`: Decrease A3 Offset threshold for 3221185_1
- `C6`: Add neighbor relationship between 3216113_4 and 3250776_2
- `C7`: Increase A3 Offset threshold for 3250776_2
- `C8`: Adjust the azimuth of 3216113_4 by 50 degrees
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3221185_1
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3221185_1
- `C11`: Check test server and transmission issues
- `C12`: Press down the tilt angle  of 3216113_4 by 5 degrees
- `C13`: Decrease transmission power for 3250776_2
- `C14`: Lift the tilt angle of 3221185_1 by 6 degrees
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3250776_2
- `C16`: Add neighbor relationship between 3221185_1 and 3250776_2
- `C17`: Increase transmission power for 3250776_2
- `C18`: Increase transmission power for 3221185_1
- `C19`: Adjust the azimuth of 3221185_1 by 19 degrees
- `C20`: Increase A3 Offset threshold for 3221185_1
- `C21`: Lift the tilt angle  of 3216113_4 by 5 degrees **← 정답**
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3250776_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.729 | MS1 | 121.4656751451 | 31.1446379877 | 232 | 504990 | -85.88 | 14.34 | 466.51 | 0.07 | 2.19 | 1597 |
| 2024-09-20 22:21:32.344 | MS1 | 121.4656758130 | 31.1446225077 | 232 | 504990 | -88.16 | 14.84 | 418.28 | 0.02 | 2.09 | 1572 |
| 2024-09-20 22:21:33.638 | MS1 | 121.4656580364 | 31.1446356643 | 232 | 504990 | -87.34 | 12.61 | 462.93 | 0.04 | 2.38 | 1566 |
| 2024-09-20 22:21:34.868 | MS1 | 121.4656761992 | 31.1446258603 | 232 | 504990 | -85.61 | 15.82 | 78.48 | 0.04 | 2.79 | 1592 |
| 2024-09-20 22:21:35.331 | MS1 | 121.4656616231 | 31.1446344157 | 232 | 504990 | -89.20 | 12.23 | 66.65 | 0.16 | 2.22 | 1588 |
| 2024-09-20 22:21:36.324 | MS1 | 121.4656725506 | 31.1446278679 | 232 | 504990 | -91.58 | 16.99 | 79.90 | 0.07 | 2.37 | 1590 |
| 2024-09-20 22:21:37.221 | MS1 | 121.4656619217 | 31.1446307715 | 232 | 504990 | -91.30 | 9.27 | 45.44 | 0.19 | 2.72 | 1584 |
| 2024-09-20 22:21:38.991 | MS1 | 121.4656632700 | 31.1446290894 | 232 | 504990 | -91.59 | 7.85 | 84.83 | 0.04 | 2.81 | 1586 |
| 2024-09-20 22:21:39.288 | MS1 | 121.4656602405 | 31.1446351620 | 232 | 504990 | -92.78 | 8.14 | 62.06 | 0.12 | 2.25 | 1573 |
| 2024-09-20 22:21:40.756 | MS1 | 121.4656711098 | 31.1446368219 | 232 | 504990 | -92.13 | 12.75 | 426.08 | 0.10 | 2.58 | 1581 |
| 2024-09-20 22:21:41.191 | MS1 | 121.4656601519 | 31.1446318840 | 232 | 504990 | -93.39 | 8.04 | 408.35 | 0.03 | 2.72 | 1582 |
| 2024-09-20 22:21:42.955 | MS1 | 121.4656733339 | 31.1446321304 | 232 | 504990 | -89.88 | 9.80 | 518.53 | 0.05 | 2.10 | 1598 |

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
| 3213683 | 3 | 121.4741435100 | 31.1442947245 | 267 | 10 | 4 | 32.7 | TDD | 374 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3216113 | 4 | 121.4669142420 | 31.1479989665 | 69 | 7 | 0 | 22.9 | TDD | 191 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3221185 | 1 | 121.4668204436 | 31.1550446531 | 204 | 5 | 5 | 19.5 | TDD | 232 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3250776 | 2 | 121.4661551066 | 31.1500870106 | 100 | 1 | 4 | 43.7 | TDD | 801 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |

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
| 2024-09-20 22:21:31.638 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.662 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.765 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.765 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.463 | NREventA3 | measId:2;ServCellPCI:205;Se... |
| 2024-09-20 22:21:38.703 | NRHandoverAttempt | SourcePCI:205;SourceNR-ARFC... |
| 2024-09-20 22:21:38.740 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.753 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.878 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.878 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3221185 | 1 | 86.3269 | 77.0843 | -116.5562 | 14.5824 | 164.7977 | 0.0131 | 0.0110 |
| 2024_09_20 22:00 | 3250776 | 2 | 13.2698 | 7.2355 | -114.7402 | 10.3081 | 148.4470 | 0.0019 | 0.0109 |
| 2024_09_20 22:00 | 3213683 | 3 | 12.2773 | 7.2818 | -117.1311 | 11.3301 | 199.4563 | 0.0048 | 0.0140 |
| 2024_09_20 22:00 | 3216113 | 4 | 5.8866 | 13.0010 | -114.6728 | 5.3393 | 88.2027 | 0.0061 | 0.0045 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417113_8CDF2A66 | 504990 | 232 | -83.9 | 504990 | 801 | -93.3 | 504990 | 191 | -94.6 | 504990 | 374 |
| MR_1774417113_94A4CD58 | 504990 | 232 | -86.7 | 504990 | 801 | -90.9 | 504990 | 191 | -93.6 | 504990 | 374 |
| MR_1774417113_392F50AA | 504990 | 232 | -86.8 | 504990 | 801 | -92.8 | 504990 | 191 | -95.1 | 504990 | 374 |
| MR_1774417113_866FEBD2 | 504990 | 232 | -84.5 | 504990 | 801 | -90.3 | 504990 | 191 | -93.4 | 504990 | 374 |
| MR_1774417113_CAF2E1AD | 504990 | 232 | -85.4 | 504990 | 801 | -92.4 | 504990 | 191 | -95.3 | 504990 | 374 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 822: `a51cd4f1-eba...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `a51cd4f1-eba1-4e12-a85c-582927b11f12` |
| Tag | **single-answer** |
| 정답 | **C4** |
| C4 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[822] topology](images/train_0822.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3253870_3
- `C2`: Check test server and transmission issues
- `C3`: Increase A3 Offset threshold for 3219754_4
- `C4`: Insufficient data; more data is needed for judgment. **← 정답**
- `C5`: Increase transmission power for 3253870_3
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3253870_3
- `C7`: Lift the tilt angle  of 3253870_3 by 3 degrees
- `C8`: Increase A3 Offset threshold for 3253870_3
- `C9`: Decrease transmission power for 3219754_4
- `C10`: Increase transmission power for 3219754_4
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3253870_3
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3219754_4
- `C13`: Decrease A3 Offset threshold for 3219754_4
- `C14`: Add neighbor relationship between 3219754_4 and 3253870_3
- `C15`: Adjust the azimuth of 3253870_3 by 50 degrees
- `C16`: Adjust the azimuth of 3219754_4 by 50 degrees
- `C17`: Press down the tilt angle of 3219754_4 by 10 degrees
- `C18`: Lift the tilt angle of 3219754_4 by 10 degrees
- `C19`: Add neighbor relationship between 3225910_2 and 3253870_3
- `C20`: Press down the tilt angle  of 3253870_3 by 3 degrees
- `C21`: Decrease A3 Offset threshold for 3253870_3
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3219754_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.229 | MS1 | 121.4656767419 | 31.1446248439 | 106 | 504990 | -88.14 | 14.11 | 454.35 | 0.08 | 2.39 | 1589 |
| 2024-09-20 22:21:32.814 | MS1 | 121.4656581682 | 31.1446310491 | 106 | 504990 | -89.02 | 15.67 | 521.78 | 0.12 | 2.83 | 1571 |
| 2024-09-20 22:21:33.537 | MS1 | 121.4656745809 | 31.1446308447 | 106 | 504990 | -91.37 | 15.63 | 401.83 | 0.02 | 2.49 | 1584 |
| 2024-09-20 22:21:34.227 | MS1 | 121.4656734615 | 31.1446309747 | 106 | 504990 | -87.85 | 14.52 | 94.55 | 0.06 | 2.10 | 1593 |
| 2024-09-20 22:21:35.899 | MS1 | 121.4656583528 | 31.1446211759 | 106 | 504990 | -91.15 | 17.94 | 92.30 | 0.11 | 2.26 | 1562 |
| 2024-09-20 22:21:36.940 | MS1 | 121.4656660060 | 31.1446273469 | 106 | 504990 | -89.92 | 17.76 | 69.56 | 0.11 | 2.36 | 1573 |
| 2024-09-20 22:21:37.529 | MS1 | 121.4656593201 | 31.1446305702 | 106 | 504990 | -90.84 | 12.41 | 64.46 | 0.20 | 2.08 | 1579 |
| 2024-09-20 22:21:38.553 | MS1 | 121.4656622213 | 31.1446320232 | 106 | 504990 | -89.99 | 11.42 | 73.04 | 0.20 | 2.36 | 1584 |
| 2024-09-20 22:21:39.103 | MS1 | 121.4656644560 | 31.1446356160 | 106 | 504990 | -89.76 | 7.85 | 59.33 | 0.14 | 2.96 | 1598 |
| 2024-09-20 22:21:40.276 | MS1 | 121.4656745665 | 31.1446220909 | 106 | 504990 | -89.10 | 12.11 | 509.44 | 0.09 | 2.15 | 1593 |
| 2024-09-20 22:21:41.719 | MS1 | 121.4656648921 | 31.1446311908 | 106 | 504990 | -92.28 | 12.16 | 343.84 | 0.04 | 2.87 | 1583 |
| 2024-09-20 22:21:42.675 | MS1 | 121.4656740796 | 31.1446278581 | 106 | 504990 | -93.72 | 11.19 | 516.37 | 0.18 | 2.54 | 1584 |

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
| 3219754 | 4 | 121.4640921635 | 31.1553117667 | 40 | 12 | 7 | 41.0 | TDD | 106 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3225910 | 2 | 121.4752606347 | 31.1498781999 | 294 | 6 | 12 | 22.8 | TDD | 705 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3253870 | 3 | 121.4640772638 | 31.1530798428 | 273 | 0 | 3 | 43.3 | TDD | 162 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3260105 | 1 | 121.4730365262 | 31.1504395164 | 59 | 13 | 4 | 43.3 | TDD | 65 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |

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
| 2024-09-20 22:21:31.287 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.307 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.434 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.434 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.088 | NREventA3 | measId:2;ServCellPCI:895;Se... |
| 2024-09-20 22:21:38.328 | NRHandoverAttempt | SourcePCI:895;SourceNR-ARFC... |
| 2024-09-20 22:21:38.363 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.374 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.509 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.509 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3260105 | 1 | 81.9482 | 91.2318 | -117.1395 | 17.6779 | 82.1679 | 0.0134 | 0.0030 |
| 2024_09_19 22:00 | 3225910 | 2 | 84.9526 | 79.9776 | -117.3888 | 19.4587 | 160.8599 | 0.0018 | 0.0161 |
| 2024_09_19 22:00 | 3253870 | 3 | 92.7110 | 83.4674 | -114.9525 | 19.3197 | 194.5392 | 0.0155 | 0.0011 |
| 2024_09_19 22:00 | 3219754 | 4 | 87.1008 | 81.6426 | -115.1152 | 8.8667 | 107.9733 | 0.0030 | 0.0187 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412628_683ADC2E | 504990 | 106 | -89.7 | 504990 | 162 | -92.6 | 504990 | 705 | -103.1 | 504990 | 65 |
| MR_1774412628_7BD046BB | 504990 | 106 | -87.6 | 504990 | 162 | -93.1 | 504990 | 705 | -101.0 | 504990 | 65 |
| MR_1774412628_760BC99B | 504990 | 106 | -86.3 | 504990 | 162 | -93.0 | 504990 | 705 | -102.3 | 504990 | 65 |
| MR_1774412628_946E601E | 504990 | 106 | -85.9 | 504990 | 162 | -95.4 | 504990 | 705 | -99.2 | 504990 | 65 |
| MR_1774412628_02D87CC5 | 504990 | 106 | -85.9 | 504990 | 162 | -95.1 | 504990 | 705 | -101.9 | 504990 | 65 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 823: `220469e4-945...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `220469e4-945e-46ae-b4c7-53cecea2a2bc` |
| Tag | **single-answer** |
| 정답 | **C19** |
| C19 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3265744_4 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[823] topology](images/train_0823.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3265744_4
- `C2`: Decrease A3 Offset threshold for 3265744_4
- `C3`: Lift the tilt angle  of 3232773_6 by 2 degrees
- `C4`: Increase transmission power for 3265744_4
- `C5`: Press down the tilt angle  of 3232773_6 by 2 degrees
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3265744_4
- `C7`: Add neighbor relationship between 3265744_4 and 3232773_6
- `C8`: Add neighbor relationship between 3238631_11 and 3232773_6
- `C9`: Adjust the azimuth of 3232773_6 by 29 degrees
- `C10`: Increase A3 Offset threshold for 3265744_4
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3232773_6
- `C12`: Press down the tilt angle of 3265744_4 by 2 degrees
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3232773_6
- `C14`: Increase transmission power for 3232773_6
- `C15`: Check test server and transmission issues
- `C16`: Insufficient data; more data is needed for judgment.
- `C17`: Lift the tilt angle of 3265744_4 by 2 degrees
- `C18`: Decrease transmission power for 3232773_6
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3265744_4 **← 정답**
- `C20`: Adjust the azimuth of 3265744_4 by 9 degrees
- `C21`: Decrease A3 Offset threshold for 3232773_6
- `C22`: Increase A3 Offset threshold for 3232773_6

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.528 | MS1 | 121.4656710376 | 31.1446353745 | 690 | 504990 | -94.58 | 9.81 | 372.10 | 0.20 | 2.11 | 1566 |
| 2024-09-20 22:21:32.729 | MS1 | 121.4656769855 | 31.1446241372 | 145 | 504990 | -95.99 | 10.08 | 451.93 | 0.14 | 2.92 | 1600 |
| 2024-09-20 22:21:33.977 | MS1 | 121.4656690454 | 31.1446357087 | 779 | 504990 | -94.98 | 13.98 | 376.97 | 0.06 | 2.55 | 1565 |
| 2024-09-20 22:21:34.285 | MS1 | 121.4656776227 | 31.1446249070 | 762 | 152650 | -96.63 | 2.00 | 78.48 | 0.08 | 1.95 | 959 |
| 2024-09-20 22:21:35.484 | MS1 | 121.4656720178 | 31.1446211914 | 988 | 152650 | -88.26 | 2.97 | 89.72 | 0.06 | 1.66 | 946 |
| 2024-09-20 22:21:36.728 | MS1 | 121.4656720605 | 31.1446316953 | 335 | 152650 | -87.36 | 6.27 | 68.26 | 0.07 | 1.82 | 915 |
| 2024-09-20 22:21:37.294 | MS1 | 121.4656609235 | 31.1446276259 | 838 | 152650 | -95.89 | 7.64 | 59.94 | 0.02 | 1.96 | 943 |
| 2024-09-20 22:21:38.750 | MS1 | 121.4656707065 | 31.1446303999 | 762 | 152650 | -87.75 | 2.21 | 69.61 | 0.09 | 1.58 | 961 |
| 2024-09-20 22:21:39.701 | MS1 | 121.4656747896 | 31.1446286715 | 988 | 152650 | -88.31 | 7.18 | 59.31 | 0.05 | 1.67 | 930 |
| 2024-09-20 22:21:40.948 | MS1 | 121.4656641543 | 31.1446264582 | 335 | 152650 | -94.25 | 6.14 | 62.29 | 0.09 | 2.79 | 1584 |
| 2024-09-20 22:21:41.413 | MS1 | 121.4656650870 | 31.1446239659 | 838 | 152650 | -94.33 | 3.12 | 67.59 | 0.07 | 2.09 | 1598 |
| 2024-09-20 22:21:42.658 | MS1 | 121.4656716271 | 31.1446211943 | 762 | 152650 | -87.56 | 2.36 | 99.71 | 0.16 | 2.49 | 1572 |

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
| 3215286 | 7 | 121.4707650492 | 31.1528109140 | 296 | 4 | 8 | 28.9 | FDD | 838 | n1 | 152650 | 30M | 4T4R | 28 | 152650 |
| 3229966 | 3 | 121.4755429569 | 31.1455627424 | 69 | 15 | 2 | 10.9 | TDD | 145 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3232773 | 6 | 121.4724692868 | 31.1559771742 | 236 | 1 | 8 | 15.7 | TDD | 725 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3238631 | 11 | 121.4682150751 | 31.1543596569 | 298 | 2 | 3 | 16.0 | FDD | 335 | n1 | 152650 | 30M | 4T4R | 25 | 152650 |
| 3238899 | 9 | 121.4705327637 | 31.1452774270 | 352 | 9 | 1 | 9.3 | FDD | 139 | n1 | 152650 | 30M | 4T4R | 29 | 152650 |
| 3238910 | 12 | 121.4716513949 | 31.1510733507 | 179 | 15 | 11 | 5.9 | FDD | 762 | n1 | 152650 | 30M | 4T4R | 15 | 152650 |
| 3239396 | 5 | 121.4650315069 | 31.1523405493 | 32 | 4 | 12 | 26.4 | TDD | 307 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3250010 | 2 | 121.4656500040 | 31.1451315408 | 117 | 13 | 10 | 2.1 | TDD | 779 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3250150 | 10 | 121.4649964313 | 31.1448226869 | 278 | 11 | 9 | 3.5 | FDD | 77 | n1 | 152650 | 30M | 4T4R | 19 | 152650 |
| 3252224 | 1 | 121.4710420978 | 31.1492080007 | 6 | 4 | 0 | 0.1 | TDD | 706 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3265744 | 4 | 121.4674865083 | 31.1477202874 | 198 | 1 | 11 | 5.1 | TDD | 690 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3278957 | 13 | 121.4649439228 | 31.1477540237 | 56 | 15 | 3 | 15.4 | FDD | 988 | n1 | 152650 | 30M | 4T4R | 15 | 152650 |
| 3279918 | 8 | 121.4728237619 | 31.1450590337 | 344 | 8 | 9 | 18.4 | FDD | 936 | n1 | 152650 | 30M | 4T4R | 13 | 152650 |

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
| 2024-09-20 22:21:30.947 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.965 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.070 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.070 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.814 | NREventA2 | measId:1;ServCellPCI:279;Se... |
| 2024-09-20 22:21:34.916 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.170 | NREventA5 | measId:3;ServCellPCI:279;Se... |
| 2024-09-20 22:21:35.204 | NRHandoverAttempt | SourcePCI:279;SourceNR-ARFC... |
| 2024-09-20 22:21:35.250 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.265 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:35.405 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.405 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3252224 | 1 | 18.3772 | 13.1355 | -114.1383 | 8.9312 | 107.4911 | 0.0026 | 0.0192 |
| 2024_09_20 22:00 | 3250010 | 2 | 8.6244 | 7.5789 | -117.0320 | 14.6079 | 115.6784 | 0.0032 | 0.0010 |
| 2024_09_20 22:00 | 3229966 | 3 | 8.0792 | 15.5294 | -114.0218 | 11.3091 | 189.8652 | 0.0066 | 0.0182 |
| 2024_09_20 22:00 | 3265744 | 4 | 5.5771 | 5.8184 | -114.2615 | 15.7396 | 198.3720 | 0.0146 | 0.0096 |
| 2024_09_20 22:00 | 3239396 | 5 | 9.7876 | 6.8057 | -116.4602 | 8.8236 | 189.8240 | 0.0114 | 0.0134 |
| 2024_09_20 22:00 | 3232773 | 6 | 5.5087 | 6.6514 | -115.8034 | 17.9978 | 167.8987 | 0.0065 | 0.0083 |
| 2024_09_20 22:00 | 3215286 | 7 | 9.6867 | 13.1760 | -117.9447 | 3.5315 | 54.2281 | 0.0156 | 0.0000 |
| 2024_09_20 22:00 | 3279918 | 8 | 18.7144 | 8.1665 | -116.6879 | 3.3129 | 56.4503 | 0.0060 | 0.0166 |
| 2024_09_20 22:00 | 3238899 | 9 | 6.6318 | 9.2950 | -117.1334 | 4.0407 | 53.7328 | 0.0004 | 0.0056 |
| 2024_09_20 22:00 | 3250150 | 10 | 14.9019 | 19.0195 | -117.9113 | 3.9203 | 40.3041 | 0.0040 | 0.0099 |
| 2024_09_20 22:00 | 3238631 | 11 | 14.9715 | 18.3746 | -116.2753 | 4.9072 | 59.2907 | 0.0117 | 0.0005 |
| 2024_09_20 22:00 | 3238910 | 12 | 9.3011 | 8.6819 | -117.5371 | 3.1714 | 21.2615 | 0.0106 | 0.0009 |
| 2024_09_20 22:00 | 3278957 | 13 | 5.7625 | 6.2563 | -114.8402 | 4.8217 | 40.8509 | 0.0176 | 0.0183 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415041_AAEC09E0 | 504990 | 779 | -94.8 | 504990 | 725 | -94.3 | 504990 | 706 | -101.2 | 504990 | 307 |
| MR_1774415041_EF503736 | 152650 | 762 | -96.8 | 152650 | 77 | -101.6 | 152650 | 139 | -104.2 | 152650 | 936 |
| MR_1774415041_9BF6D0DC | 152650 | 762 | -96.4 | 152650 | 77 | -102.6 | 152650 | 139 | -106.6 | 152650 | 936 |
| MR_1774415041_A76402BB | 504990 | 779 | -95.0 | 504990 | 725 | -95.4 | 504990 | 706 | -101.2 | 504990 | 307 |
| MR_1774415041_A7F8F500 | 152650 | 762 | -96.6 | 152650 | 77 | -102.0 | 152650 | 139 | -105.6 | 152650 | 936 |
| MR_1774415041_8349748B | 504990 | 779 | -93.7 | 504990 | 725 | -94.2 | 504990 | 706 | -100.2 | 504990 | 307 |
| MR_1774415041_C7BF77BF | 152650 | 762 | -96.0 | 152650 | 77 | -100.7 | 152650 | 139 | -104.6 | 152650 | 936 |
| MR_1774415041_D3241F0B | 504990 | 779 | -95.2 | 504990 | 725 | -96.2 | 504990 | 706 | -101.3 | 504990 | 307 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 824: `265d96d1-323...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `265d96d1-3239-4cb8-bfa0-12b9f4437744` |
| Tag | **multiple-answer** |
| 정답 | **C1|C7** |
| C1 의미 | Increase transmission power for 3215121_4 |
| C7 의미 | Adjust the azimuth of 3215121_4 by 50 degrees |
| 패턴 분류 | **P4 Coverage (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[824] topology](images/train_0824.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3215121_4 **← 정답**
- `C2`: Decrease transmission power for 3253879_2
- `C3`: Decrease transmission power for 3215121_4
- `C4`: Insufficient data; more data is needed for judgment.
- `C5`: Add neighbor relationship between 3215121_4 and 3253879_2
- `C6`: Lift the tilt angle of 3215121_4 by 8 degrees
- `C7`: Adjust the azimuth of 3215121_4 by 50 degrees **← 정답**
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3215121_4
- `C9`: Lift the tilt angle  of 3253879_2 by 3 degrees
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3215121_4
- `C11`: Decrease A3 Offset threshold for 3215121_4
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3253879_2
- `C13`: Check test server and transmission issues
- `C14`: Increase A3 Offset threshold for 3253879_2
- `C15`: Add neighbor relationship between 3260350_1 and 3253879_2
- `C16`: Adjust the azimuth of 3253879_2 by 8 degrees
- `C17`: Press down the tilt angle  of 3253879_2 by 3 degrees
- `C18`: Decrease A3 Offset threshold for 3253879_2
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3253879_2
- `C20`: Increase A3 Offset threshold for 3215121_4
- `C21`: Press down the tilt angle of 3215121_4 by 8 degrees
- `C22`: Increase transmission power for 3253879_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.390 | MS1 | 121.4656733529 | 31.1446267749 | 733 | 504990 | -87.58 | 17.37 | 574.29 | 0.14 | 2.24 | 1593 |
| 2024-09-20 22:21:32.390 | MS1 | 121.4656691775 | 31.1446283617 | 733 | 504990 | -90.49 | 16.81 | 435.84 | 0.05 | 2.50 | 1563 |
| 2024-09-20 22:21:33.652 | MS1 | 121.4656661089 | 31.1446360665 | 733 | 504990 | -92.85 | 14.31 | 399.98 | 0.19 | 2.68 | 1593 |
| 2024-09-20 22:21:34.879 | MS1 | 121.4656726339 | 31.1446218201 | 733 | 504990 | -101.03 | -1.92 | 31.64 | 0.09 | 1.32 | 1584 |
| 2024-09-20 22:21:35.354 | MS1 | 121.4656722378 | 31.1446363012 | 733 | 504990 | -103.52 | -1.58 | 40.02 | 0.08 | 1.19 | 1578 |
| 2024-09-20 22:21:36.360 | MS1 | 121.4656593086 | 31.1446344384 | 733 | 504990 | -101.92 | -0.06 | 25.61 | 0.01 | 1.21 | 1573 |
| 2024-09-20 22:21:37.623 | MS1 | 121.4656641854 | 31.1446225627 | 733 | 504990 | -101.90 | 0.26 | 50.87 | 0.13 | 1.41 | 1579 |
| 2024-09-20 22:21:38.829 | MS1 | 121.4656618151 | 31.1446259115 | 733 | 504990 | -102.66 | -0.41 | 45.63 | 0.02 | 1.29 | 1590 |
| 2024-09-20 22:21:39.286 | MS1 | 121.4656643824 | 31.1446216699 | 733 | 504990 | -102.81 | -1.88 | 62.24 | 0.19 | 1.25 | 1591 |
| 2024-09-20 22:21:40.810 | MS1 | 121.4656591220 | 31.1446194391 | 733 | 504990 | -87.68 | 15.19 | 393.03 | 0.07 | 2.25 | 1590 |
| 2024-09-20 22:21:41.567 | MS1 | 121.4656728780 | 31.1446297563 | 733 | 504990 | -94.91 | 12.03 | 509.56 | 0.10 | 2.95 | 1573 |
| 2024-09-20 22:21:42.532 | MS1 | 121.4656770994 | 31.1446214882 | 733 | 504990 | -93.08 | 14.73 | 322.23 | 0.04 | 2.92 | 1561 |

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
| 3215121 | 4 | 121.4744060981 | 31.1463443623 | 329 | 5 | 10 | 45.4 | TDD | 733 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3216103 | 3 | 121.4711169561 | 31.1507855773 | 156 | 4 | 1 | 26.6 | TDD | 800 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3253879 | 2 | 121.4653977318 | 31.1496621521 | 169 | 0 | 3 | 31.1 | TDD | 866 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3260350 | 1 | 121.4706488463 | 31.1519136695 | 82 | 7 | 3 | 17.6 | TDD | 392 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:30.979 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.979 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.203 | NREventA2 | measId:1;ServCellPCI:361;Se... |
| 2024-09-20 22:21:34.336 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3260350 | 1 | 13.6597 | 16.1050 | -115.7164 | 15.0089 | 89.7577 | 0.0196 | 0.0010 |
| 2024_09_20 22:00 | 3253879 | 2 | 5.7766 | 10.8078 | -114.8339 | 13.7845 | 128.2888 | 0.0171 | 0.0088 |
| 2024_09_20 22:00 | 3216103 | 3 | 16.4852 | 15.1204 | -114.6392 | 16.3066 | 168.3426 | 0.0071 | 0.0017 |
| 2024_09_20 22:00 | 3215121 | 4 | 13.6049 | 12.0638 | -114.6291 | 12.8015 | 121.5703 | 0.1491 | 0.0144 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415054_1EF2EC43 | 504990 | 733 | -101.8 | 504990 | 866 | -106.7 | 504990 | 392 | -112.4 | 504990 | 800 |
| MR_1774415054_B64CBD36 | 504990 | 733 | -102.6 | 504990 | 866 | -106.0 | 504990 | 392 | -114.2 | 504990 | 800 |
| MR_1774415054_CCF2CAC7 | 504990 | 733 | -102.2 | 504990 | 866 | -108.7 | 504990 | 392 | -111.3 | 504990 | 800 |
| MR_1774415054_2848FC7A | 504990 | 733 | -101.9 | 504990 | 866 | -108.4 | 504990 | 392 | -112.5 | 504990 | 800 |
| MR_1774415054_8B24A047 | 504990 | 733 | -99.7 | 504990 | 866 | -109.4 | 504990 | 392 | -113.7 | 504990 | 800 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 825: `02553df1-21c...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `02553df1-21c8-4186-abf6-d3978dc93b63` |
| Tag | **single-answer** |
| 정답 | **C9** |
| C9 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3269642_1 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[825] topology](images/train_0825.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3237330_6 by 4 degrees
- `C2`: Decrease transmission power for 3237330_6
- `C3`: Press down the tilt angle of 3269642_1 by 2 degrees
- `C4`: Add neighbor relationship between 3240930_8 and 3237330_6
- `C5`: Decrease A3 Offset threshold for 3269642_1
- `C6`: Adjust the azimuth of 3237330_6 by 5 degrees
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3237330_6
- `C8`: Increase transmission power for 3237330_6
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3269642_1 **← 정답**
- `C10`: Increase A3 Offset threshold for 3237330_6
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3237330_6
- `C12`: Increase A3 Offset threshold for 3269642_1
- `C13`: Lift the tilt angle of 3269642_1 by 2 degrees
- `C14`: Check test server and transmission issues
- `C15`: Increase transmission power for 3269642_1
- `C16`: Adjust the azimuth of 3269642_1 by 31 degrees
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3269642_1
- `C18`: Decrease transmission power for 3269642_1
- `C19`: Lift the tilt angle  of 3237330_6 by 4 degrees
- `C20`: Insufficient data; more data is needed for judgment.
- `C21`: Add neighbor relationship between 3269642_1 and 3237330_6
- `C22`: Decrease A3 Offset threshold for 3237330_6

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.775 | MS1 | 121.4656689968 | 31.1446188552 | 162 | 504990 | -95.89 | 14.15 | 500.69 | 0.16 | 2.85 | 1593 |
| 2024-09-20 22:21:32.980 | MS1 | 121.4656758232 | 31.1446226068 | 39 | 504990 | -93.52 | 12.47 | 587.07 | 0.05 | 2.91 | 1572 |
| 2024-09-20 22:21:33.689 | MS1 | 121.4656601462 | 31.1446282722 | 207 | 504990 | -94.43 | 14.77 | 569.60 | 0.16 | 2.18 | 1565 |
| 2024-09-20 22:21:34.879 | MS1 | 121.4656587046 | 31.1446251844 | 109 | 152650 | -92.66 | 2.10 | 77.55 | 0.09 | 1.56 | 978 |
| 2024-09-20 22:21:35.285 | MS1 | 121.4656609427 | 31.1446351101 | 50 | 152650 | -91.88 | 2.14 | 53.05 | 0.05 | 1.67 | 952 |
| 2024-09-20 22:21:36.117 | MS1 | 121.4656716002 | 31.1446375795 | 516 | 152650 | -94.63 | 7.01 | 57.29 | 0.17 | 1.67 | 969 |
| 2024-09-20 22:21:37.613 | MS1 | 121.4656648965 | 31.1446281777 | 66 | 152650 | -87.47 | 4.66 | 63.65 | 0.10 | 1.56 | 920 |
| 2024-09-20 22:21:38.486 | MS1 | 121.4656722619 | 31.1446246911 | 109 | 152650 | -92.25 | 6.17 | 58.85 | 0.07 | 1.77 | 982 |
| 2024-09-20 22:21:39.571 | MS1 | 121.4656678500 | 31.1446316952 | 50 | 152650 | -87.16 | 5.47 | 91.02 | 0.04 | 1.91 | 976 |
| 2024-09-20 22:21:40.269 | MS1 | 121.4656694854 | 31.1446311520 | 516 | 152650 | -95.04 | 7.00 | 96.16 | 0.08 | 2.23 | 1560 |
| 2024-09-20 22:21:41.825 | MS1 | 121.4656686579 | 31.1446347405 | 66 | 152650 | -94.59 | 7.55 | 73.89 | 0.12 | 2.45 | 1577 |
| 2024-09-20 22:21:42.616 | MS1 | 121.4656598153 | 31.1446184569 | 109 | 152650 | -93.08 | 6.74 | 62.29 | 0.07 | 2.67 | 1574 |

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
| 3216969 | 5 | 121.4672675385 | 31.1537339288 | 57 | 5 | 9 | 7.2 | TDD | 475 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3220502 | 11 | 121.4731789775 | 31.1477929152 | 190 | 6 | 3 | 1.9 | FDD | 50 | n1 | 152650 | 30M | 4T4R | 19 | 152650 |
| 3220963 | 2 | 121.4651389347 | 31.1488281155 | 18 | 1 | 9 | 15.3 | TDD | 102 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3230344 | 13 | 121.4675505750 | 31.1529038689 | 315 | 10 | 4 | 5.9 | FDD | 319 | n1 | 152650 | 30M | 4T4R | 18 | 152650 |
| 3237330 | 6 | 121.4724656941 | 31.1557817464 | 203 | 3 | 7 | 26.8 | TDD | 223 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3240930 | 8 | 121.4673721523 | 31.1491783689 | 275 | 10 | 6 | 23.2 | FDD | 516 | n1 | 152650 | 30M | 4T4R | 24 | 152650 |
| 3244476 | 12 | 121.4670552660 | 31.1539122066 | 36 | 13 | 1 | 15.2 | FDD | 409 | n1 | 152650 | 30M | 4T4R | 27 | 152650 |
| 3260672 | 9 | 121.4661341609 | 31.1559014526 | 268 | 7 | 12 | 27.8 | FDD | 325 | n1 | 152650 | 30M | 4T4R | 14 | 152650 |
| 3263203 | 3 | 121.4673744805 | 31.1476301345 | 315 | 14 | 3 | 7.1 | TDD | 39 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3269174 | 10 | 121.4724287721 | 31.1446331992 | 239 | 14 | 1 | 8.9 | FDD | 109 | n1 | 152650 | 30M | 4T4R | 13 | 152650 |
| 3269642 | 1 | 121.4749678318 | 31.1529575600 | 193 | 2 | 7 | 1.7 | TDD | 162 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3270865 | 7 | 121.4693297169 | 31.1504515321 | 88 | 9 | 10 | 26.5 | FDD | 66 | n1 | 152650 | 30M | 4T4R | 13 | 152650 |
| 3272108 | 4 | 121.4666394830 | 31.1552113172 | 185 | 12 | 0 | 0.1 | TDD | 207 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:31.406 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.431 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.562 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.562 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.271 | NREventA2 | measId:1;ServCellPCI:680;Se... |
| 2024-09-20 22:21:35.393 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.632 | NREventA5 | measId:3;ServCellPCI:680;Se... |
| 2024-09-20 22:21:35.685 | NRHandoverAttempt | SourcePCI:680;SourceNR-ARFC... |
| 2024-09-20 22:21:35.724 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.737 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:35.849 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.849 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3269642 | 1 | 7.5078 | 9.1006 | -116.9265 | 15.0159 | 114.7639 | 0.0107 | 0.0026 |
| 2024_09_20 22:00 | 3220963 | 2 | 9.8247 | 14.3519 | -116.7783 | 19.5584 | 139.9650 | 0.0050 | 0.0193 |
| 2024_09_20 22:00 | 3263203 | 3 | 15.1468 | 8.2975 | -117.9293 | 9.5415 | 195.5332 | 0.0181 | 0.0032 |
| 2024_09_20 22:00 | 3272108 | 4 | 12.5455 | 15.2867 | -115.2097 | 13.7653 | 122.4442 | 0.0103 | 0.0051 |
| 2024_09_20 22:00 | 3216969 | 5 | 11.9700 | 9.3257 | -116.6156 | 7.4097 | 102.3080 | 0.0043 | 0.0185 |
| 2024_09_20 22:00 | 3237330 | 6 | 13.7533 | 14.4107 | -115.3166 | 8.8676 | 190.3855 | 0.0040 | 0.0118 |
| 2024_09_20 22:00 | 3270865 | 7 | 7.4321 | 16.7972 | -115.1969 | 4.9493 | 23.0764 | 0.0131 | 0.0069 |
| 2024_09_20 22:00 | 3240930 | 8 | 13.0198 | 7.6006 | -115.9507 | 4.8290 | 38.5172 | 0.0021 | 0.0039 |
| 2024_09_20 22:00 | 3260672 | 9 | 5.4085 | 9.4001 | -115.8040 | 3.9585 | 43.6209 | 0.0191 | 0.0153 |
| 2024_09_20 22:00 | 3269174 | 10 | 7.3318 | 17.9790 | -115.7355 | 4.3071 | 44.7780 | 0.0191 | 0.0156 |
| 2024_09_20 22:00 | 3220502 | 11 | 9.6436 | 18.7238 | -116.8026 | 4.9927 | 38.3963 | 0.0195 | 0.0187 |
| 2024_09_20 22:00 | 3244476 | 12 | 10.9397 | 16.5271 | -115.1557 | 3.5344 | 40.7621 | 0.0040 | 0.0054 |
| 2024_09_20 22:00 | 3230344 | 13 | 14.4280 | 9.6663 | -115.1118 | 4.0443 | 39.7464 | 0.0183 | 0.0191 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415276_0B9FE251 | 504990 | 207 | -96.3 | 504990 | 223 | -90.9 | 504990 | 102 | -97.4 | 504990 | 475 |
| MR_1774415276_E9F3B748 | 504990 | 207 | -93.1 | 504990 | 223 | -89.9 | 504990 | 102 | -96.3 | 504990 | 475 |
| MR_1774415276_37CB1B75 | 152650 | 109 | -91.2 | 152650 | 325 | -100.0 | 152650 | 409 | -103.8 | 152650 | 319 |
| MR_1774415276_05DDD5C7 | 504990 | 207 | -96.1 | 504990 | 223 | -89.3 | 504990 | 102 | -94.6 | 504990 | 475 |
| MR_1774415276_569130F0 | 504990 | 207 | -93.0 | 504990 | 223 | -91.1 | 504990 | 102 | -94.0 | 504990 | 475 |
| MR_1774415276_88A8CDEC | 504990 | 207 | -93.8 | 504990 | 223 | -91.4 | 504990 | 102 | -95.9 | 504990 | 475 |
| MR_1774415276_B81DD584 | 504990 | 207 | -93.8 | 504990 | 223 | -88.0 | 504990 | 102 | -96.9 | 504990 | 475 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 826: `a5f1ebf9-8d0...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `a5f1ebf9-8d01-41e5-a9d3-3b6f551879a6` |
| Tag | **single-answer** |
| 정답 | **C17** |
| C17 의미 | Lift the tilt angle  of 3254238_2 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[826] topology](images/train_0826.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment.
- `C2`: Decrease A3 Offset threshold for 3228921_3
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3228921_3
- `C4`: Decrease transmission power for 3253790_4
- `C5`: Add neighbor relationship between 3254238_2 and 3253790_4
- `C6`: Adjust the azimuth of 3254238_2 by 50 degrees
- `C7`: Press down the tilt angle  of 3254238_2 by 10 degrees
- `C8`: Increase A3 Offset threshold for 3253790_4
- `C9`: Increase transmission power for 3228921_3
- `C10`: Increase A3 Offset threshold for 3228921_3
- `C11`: Decrease transmission power for 3228921_3
- `C12`: Lift the tilt angle of 3228921_3 by 2 degrees
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3228921_3
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3253790_4
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3253790_4
- `C16`: Decrease A3 Offset threshold for 3253790_4
- `C17`: Lift the tilt angle  of 3254238_2 by 10 degrees **← 정답**
- `C18`: Increase transmission power for 3253790_4
- `C19`: Add neighbor relationship between 3228921_3 and 3253790_4
- `C20`: Adjust the azimuth of 3228921_3 by 28 degrees
- `C21`: Press down the tilt angle of 3228921_3 by 2 degrees
- `C22`: Check test server and transmission issues

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.889 | MS1 | 121.4656760469 | 31.1446314968 | 814 | 504990 | -85.16 | 14.77 | 320.77 | 0.04 | 2.36 | 1598 |
| 2024-09-20 22:21:32.202 | MS1 | 121.4656587924 | 31.1446314171 | 814 | 504990 | -91.25 | 12.44 | 565.32 | 0.11 | 2.39 | 1567 |
| 2024-09-20 22:21:33.200 | MS1 | 121.4656768257 | 31.1446364259 | 814 | 504990 | -85.72 | 14.59 | 499.44 | 0.06 | 2.45 | 1600 |
| 2024-09-20 22:21:34.360 | MS1 | 121.4656762923 | 31.1446344807 | 814 | 504990 | -88.87 | 14.36 | 90.50 | 0.05 | 2.03 | 1566 |
| 2024-09-20 22:21:35.307 | MS1 | 121.4656581270 | 31.1446338785 | 814 | 504990 | -87.42 | 17.09 | 63.93 | 0.04 | 2.04 | 1583 |
| 2024-09-20 22:21:36.930 | MS1 | 121.4656593164 | 31.1446195398 | 814 | 504990 | -89.90 | 14.32 | 82.10 | 0.11 | 2.10 | 1582 |
| 2024-09-20 22:21:37.844 | MS1 | 121.4656585866 | 31.1446243116 | 814 | 504990 | -90.12 | 12.77 | 95.35 | 0.13 | 2.91 | 1566 |
| 2024-09-20 22:21:38.539 | MS1 | 121.4656696564 | 31.1446345480 | 814 | 504990 | -92.34 | 12.94 | 77.15 | 0.01 | 2.83 | 1597 |
| 2024-09-20 22:21:39.268 | MS1 | 121.4656735367 | 31.1446377012 | 814 | 504990 | -91.28 | 8.63 | 100.05 | 0.14 | 2.78 | 1574 |
| 2024-09-20 22:21:40.739 | MS1 | 121.4656707581 | 31.1446286475 | 814 | 504990 | -93.21 | 7.73 | 302.43 | 0.14 | 2.01 | 1567 |
| 2024-09-20 22:21:41.674 | MS1 | 121.4656605180 | 31.1446180036 | 814 | 504990 | -89.11 | 12.13 | 469.96 | 0.04 | 2.62 | 1564 |
| 2024-09-20 22:21:42.985 | MS1 | 121.4656686257 | 31.1446235161 | 814 | 504990 | -93.61 | 7.06 | 446.65 | 0.01 | 2.53 | 1560 |

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
| 3210229 | 1 | 121.4642049281 | 31.1517147027 | 81 | 6 | 0 | 19.2 | TDD | 160 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3228921 | 3 | 121.4744582585 | 31.1538073227 | 191 | 0 | 0 | 48.8 | TDD | 814 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3253790 | 4 | 121.4705188950 | 31.1478000256 | 66 | 15 | 5 | 31.5 | TDD | 766 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3254238 | 2 | 121.4707290735 | 31.1459763527 | 344 | 6 | 12 | 21.7 | TDD | 627 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |

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
| 2024-09-20 22:21:31.557 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.582 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.708 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.708 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.417 | NREventA3 | measId:2;ServCellPCI:605;Se... |
| 2024-09-20 22:21:38.657 | NRHandoverAttempt | SourcePCI:605;SourceNR-ARFC... |
| 2024-09-20 22:21:38.696 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.710 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.821 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.821 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3210229 | 1 | 19.0999 | 6.8115 | -114.8273 | 16.9812 | 88.8663 | 0.0154 | 0.0031 |
| 2024_09_20 22:00 | 3254238 | 2 | 10.1850 | 12.7923 | -116.3956 | 8.5016 | 148.8076 | 0.0162 | 0.0200 |
| 2024_09_20 22:00 | 3228921 | 3 | 78.8802 | 85.9819 | -116.7095 | 18.4492 | 91.6803 | 0.0118 | 0.0136 |
| 2024_09_20 22:00 | 3253790 | 4 | 14.5803 | 16.3940 | -117.7722 | 15.7509 | 159.2063 | 0.0025 | 0.0057 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414907_0C15B842 | 504990 | 814 | -87.5 | 504990 | 766 | -96.8 | 504990 | 627 | -97.9 | 504990 | 160 |
| MR_1774414907_D30C1090 | 504990 | 814 | -88.7 | 504990 | 766 | -95.0 | 504990 | 627 | -97.5 | 504990 | 160 |
| MR_1774414907_136B8E0C | 504990 | 814 | -90.7 | 504990 | 766 | -94.5 | 504990 | 627 | -97.9 | 504990 | 160 |
| MR_1774414907_1B7AD5AF | 504990 | 814 | -89.2 | 504990 | 766 | -95.3 | 504990 | 627 | -99.0 | 504990 | 160 |
| MR_1774414907_C57BF356 | 504990 | 814 | -88.3 | 504990 | 766 | -94.2 | 504990 | 627 | -97.0 | 504990 | 160 |
| MR_1774414907_389A9C41 | 504990 | 814 | -87.3 | 504990 | 766 | -93.6 | 504990 | 627 | -96.0 | 504990 | 160 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 827: `977da08b-86f...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `977da08b-86f7-446e-b5b4-87db5ad5ed0a` |
| Tag | **single-answer** |
| 정답 | **C3** |
| C3 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3245984_3 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[827] topology](images/train_0827.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3245984_3 by 44 degrees
- `C2`: Add neighbor relationship between 3221187_1 and 3227917_2
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3245984_3 **← 정답**
- `C4`: Decrease A3 Offset threshold for 3227917_2
- `C5`: Decrease transmission power for 3245984_3
- `C6`: Decrease transmission power for 3227917_2
- `C7`: Decrease A3 Offset threshold for 3245984_3
- `C8`: Press down the tilt angle of 3245984_3 by 6 degrees
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3245984_3
- `C10`: Adjust the azimuth of 3227917_2 by 50 degrees
- `C11`: Check test server and transmission issues
- `C12`: Increase transmission power for 3227917_2
- `C13`: Press down the tilt angle  of 3227917_2 by 10 degrees
- `C14`: Lift the tilt angle of 3245984_3 by 6 degrees
- `C15`: Increase A3 Offset threshold for 3245984_3
- `C16`: Lift the tilt angle  of 3227917_2 by 10 degrees
- `C17`: Increase transmission power for 3245984_3
- `C18`: Add neighbor relationship between 3245984_3 and 3227917_2
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3227917_2
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3227917_2
- `C21`: Increase A3 Offset threshold for 3227917_2
- `C22`: Insufficient data; more data is needed for judgment.

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.301 | MS1 | 121.4656772358 | 31.1446180960 | 293 | 504990 | -88.94 | 13.14 | 340.66 | 0.14 | 2.66 | 1577 |
| 2024-09-20 22:21:32.183 | MS1 | 121.4656606560 | 31.1446254614 | 293 | 504990 | -88.43 | 17.62 | 511.05 | 0.18 | 2.90 | 1569 |
| 2024-09-20 22:21:33.717 | MS1 | 121.4656680811 | 31.1446266091 | 293 | 504990 | -86.33 | 14.34 | 318.54 | 0.09 | 2.76 | 1578 |
| 2024-09-20 22:21:34.930 | MS1 | 121.4656728996 | 31.1446213981 | 293 | 504990 | -86.41 | 13.71 | 94.45 | 0.51 | 2.46 | 579 |
| 2024-09-20 22:21:35.476 | MS1 | 121.4656686722 | 31.1446266998 | 293 | 504990 | -87.91 | 15.11 | 63.24 | 0.59 | 2.64 | 654 |
| 2024-09-20 22:21:36.487 | MS1 | 121.4656759432 | 31.1446233203 | 293 | 504990 | -87.00 | 15.12 | 68.51 | 0.65 | 2.44 | 577 |
| 2024-09-20 22:21:37.842 | MS1 | 121.4656754549 | 31.1446299454 | 293 | 504990 | -93.99 | 9.86 | 85.59 | 0.68 | 2.03 | 667 |
| 2024-09-20 22:21:38.612 | MS1 | 121.4656624393 | 31.1446283327 | 293 | 504990 | -93.35 | 9.94 | 93.63 | 0.51 | 2.65 | 587 |
| 2024-09-20 22:21:39.437 | MS1 | 121.4656720480 | 31.1446268513 | 293 | 504990 | -92.92 | 10.99 | 48.72 | 0.63 | 2.50 | 691 |
| 2024-09-20 22:21:40.690 | MS1 | 121.4656722759 | 31.1446308056 | 293 | 504990 | -90.46 | 8.49 | 551.54 | 0.04 | 2.49 | 1575 |
| 2024-09-20 22:21:41.946 | MS1 | 121.4656699178 | 31.1446301592 | 293 | 504990 | -93.05 | 11.66 | 479.79 | 0.17 | 2.54 | 1593 |
| 2024-09-20 22:21:42.386 | MS1 | 121.4656734264 | 31.1446235013 | 293 | 504990 | -90.53 | 9.57 | 356.11 | 0.08 | 2.87 | 1583 |

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
| 3215633 | 4 | 121.4702570507 | 31.1524854228 | 225 | 15 | 11 | 23.6 | TDD | 358 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3221187 | 1 | 121.4679382984 | 31.1556187910 | 283 | 15 | 12 | 35.5 | TDD | 576 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3227917 | 2 | 121.4708073597 | 31.1470891984 | 19 | 8 | 1 | 49.1 | TDD | 414 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3245984 | 3 | 121.4658909112 | 31.1547227757 | 137 | 4 | 9 | 33.8 | TDD | 293 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

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
| 2024-09-20 22:21:31.233 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.256 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.400 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.400 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.079 | NREventA3 | measId:2;ServCellPCI:13;Ser... |
| 2024-09-20 22:21:38.319 | NRHandoverAttempt | SourcePCI:13;SourceNR-ARFCN... |
| 2024-09-20 22:21:38.366 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.381 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.514 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.514 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3221187 | 1 | 18.2043 | 14.1709 | -116.4114 | 12.0573 | 183.6198 | 0.0023 | 0.0023 |
| 2024_09_20 22:00 | 3227917 | 2 | 19.6352 | 12.2593 | -117.2450 | 18.7516 | 112.2680 | 0.0181 | 0.0123 |
| 2024_09_20 22:00 | 3245984 | 3 | 6.5393 | 17.5852 | -114.1675 | 19.5960 | 115.8889 | 0.0067 | 0.0133 |
| 2024_09_20 22:00 | 3215633 | 4 | 7.7538 | 17.3887 | -116.5119 | 5.8575 | 177.2265 | 0.0099 | 0.0016 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416342_9B9D356E | 504990 | 293 | -85.1 | 504990 | 414 | -87.4 | 504990 | 576 | -96.9 | 504990 | 358 |
| MR_1774416342_CE07D0A5 | 504990 | 293 | -88.0 | 504990 | 414 | -89.0 | 504990 | 576 | -95.7 | 504990 | 358 |
| MR_1774416342_60FE12A7 | 504990 | 293 | -87.4 | 504990 | 414 | -88.5 | 504990 | 576 | -98.0 | 504990 | 358 |
| MR_1774416342_671EFA83 | 504990 | 293 | -85.1 | 504990 | 414 | -89.5 | 504990 | 576 | -98.4 | 504990 | 358 |
| MR_1774416342_FD3B662C | 504990 | 293 | -86.4 | 504990 | 414 | -87.3 | 504990 | 576 | -95.0 | 504990 | 358 |
| MR_1774416342_332B4FE5 | 504990 | 293 | -86.2 | 504990 | 414 | -89.6 | 504990 | 576 | -96.9 | 504990 | 358 |
| MR_1774416342_95151ABA | 504990 | 293 | -88.0 | 504990 | 414 | -90.2 | 504990 | 576 | -98.3 | 504990 | 358 |
| MR_1774416342_CE8AC913 | 504990 | 293 | -87.7 | 504990 | 414 | -88.8 | 504990 | 576 | -94.6 | 504990 | 358 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 828: `ce3e0d77-9e9...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `ce3e0d77-9e99-4ad3-a764-b588a35fadc6` |
| Tag | **single-answer** |
| 정답 | **C3** |
| C3 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3229923_1 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[828] topology](images/train_0828.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3254559_2 by 50 degrees
- `C2`: Increase transmission power for 3254559_2
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3229923_1 **← 정답**
- `C4`: Increase transmission power for 3229923_1
- `C5`: Decrease A3 Offset threshold for 3254559_2
- `C6`: Check test server and transmission issues
- `C7`: Add neighbor relationship between 3229923_1 and 3254559_2
- `C8`: Decrease transmission power for 3254559_2
- `C9`: Press down the tilt angle of 3229923_1 by 4 degrees
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3254559_2
- `C11`: Decrease A3 Offset threshold for 3229923_1
- `C12`: Add neighbor relationship between 3233978_4 and 3254559_2
- `C13`: Increase A3 Offset threshold for 3254559_2
- `C14`: Lift the tilt angle of 3229923_1 by 4 degrees
- `C15`: Insufficient data; more data is needed for judgment.
- `C16`: Adjust the azimuth of 3229923_1 by 44 degrees
- `C17`: Decrease transmission power for 3229923_1
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3229923_1
- `C19`: Increase A3 Offset threshold for 3229923_1
- `C20`: Lift the tilt angle  of 3254559_2 by 10 degrees
- `C21`: Press down the tilt angle  of 3254559_2 by 10 degrees
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3254559_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.824 | MS1 | 121.4656672445 | 31.1446309973 | 892 | 504990 | -87.14 | 14.20 | 567.95 | 0.05 | 2.68 | 1576 |
| 2024-09-20 22:21:32.782 | MS1 | 121.4656664606 | 31.1446182517 | 892 | 504990 | -87.61 | 16.69 | 453.96 | 0.12 | 2.72 | 1588 |
| 2024-09-20 22:21:33.818 | MS1 | 121.4656679250 | 31.1446288639 | 892 | 504990 | -90.12 | 15.97 | 568.04 | 0.03 | 2.59 | 1590 |
| 2024-09-20 22:21:34.107 | MS1 | 121.4656706612 | 31.1446337929 | 892 | 504990 | -85.36 | 12.06 | 74.90 | 0.57 | 2.20 | 603 |
| 2024-09-20 22:21:35.588 | MS1 | 121.4656773049 | 31.1446221853 | 892 | 504990 | -88.64 | 12.21 | 68.36 | 0.65 | 2.12 | 673 |
| 2024-09-20 22:21:36.104 | MS1 | 121.4656581299 | 31.1446185027 | 892 | 504990 | -87.25 | 13.38 | 94.16 | 0.67 | 2.82 | 634 |
| 2024-09-20 22:21:37.428 | MS1 | 121.4656760685 | 31.1446182745 | 892 | 504990 | -90.10 | 8.69 | 76.05 | 0.59 | 2.92 | 531 |
| 2024-09-20 22:21:38.527 | MS1 | 121.4656615059 | 31.1446318853 | 892 | 504990 | -90.45 | 12.15 | 64.14 | 0.65 | 2.63 | 682 |
| 2024-09-20 22:21:39.836 | MS1 | 121.4656749641 | 31.1446279519 | 892 | 504990 | -91.67 | 12.04 | 88.22 | 0.63 | 2.39 | 522 |
| 2024-09-20 22:21:40.589 | MS1 | 121.4656713717 | 31.1446223478 | 892 | 504990 | -90.67 | 10.24 | 496.71 | 0.01 | 2.43 | 1598 |
| 2024-09-20 22:21:41.379 | MS1 | 121.4656676046 | 31.1446344403 | 892 | 504990 | -90.84 | 12.52 | 540.41 | 0.05 | 2.19 | 1579 |
| 2024-09-20 22:21:42.218 | MS1 | 121.4656689044 | 31.1446345900 | 892 | 504990 | -91.53 | 12.46 | 415.00 | 0.18 | 2.58 | 1598 |

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
| 3229923 | 1 | 121.4740838154 | 31.1527089026 | 266 | 2 | 1 | 45.0 | TDD | 892 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3233978 | 4 | 121.4691021713 | 31.1483632965 | 197 | 4 | 12 | 26.1 | TDD | 924 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3239096 | 3 | 121.4734677655 | 31.1488542124 | 228 | 5 | 1 | 27.7 | TDD | 83 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3254559 | 2 | 121.4751951742 | 31.1471387421 | 128 | 8 | 8 | 32.8 | TDD | 66 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |

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
| 2024-09-20 22:21:30.865 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.886 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.025 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.025 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.720 | NREventA3 | measId:2;ServCellPCI:680;Se... |
| 2024-09-20 22:21:37.960 | NRHandoverAttempt | SourcePCI:680;SourceNR-ARFC... |
| 2024-09-20 22:21:37.990 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.005 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.112 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.112 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3229923 | 1 | 7.9844 | 5.1418 | -115.8081 | 8.2224 | 122.6890 | 0.0074 | 0.0176 |
| 2024_09_20 22:00 | 3254559 | 2 | 10.9802 | 10.8201 | -114.9294 | 5.9886 | 154.8438 | 0.0062 | 0.0106 |
| 2024_09_20 22:00 | 3239096 | 3 | 15.5349 | 8.3595 | -116.4775 | 11.8252 | 189.3787 | 0.0041 | 0.0084 |
| 2024_09_20 22:00 | 3233978 | 4 | 5.6843 | 16.4610 | -117.5082 | 12.8831 | 112.6679 | 0.0106 | 0.0086 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413646_335D6EE9 | 504990 | 892 | -84.2 | 504990 | 66 | -92.2 | 504990 | 924 | -93.8 | 504990 | 83 |
| MR_1774413646_C434A64F | 504990 | 892 | -86.7 | 504990 | 66 | -91.1 | 504990 | 924 | -96.5 | 504990 | 83 |
| MR_1774413646_33E7EBF8 | 504990 | 892 | -85.4 | 504990 | 66 | -90.2 | 504990 | 924 | -96.6 | 504990 | 83 |
| MR_1774413646_03B829AA | 504990 | 892 | -85.8 | 504990 | 66 | -89.7 | 504990 | 924 | -96.7 | 504990 | 83 |
| MR_1774413646_0F7BC424 | 504990 | 892 | -85.0 | 504990 | 66 | -91.6 | 504990 | 924 | -94.0 | 504990 | 83 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 829: `91206e7d-777...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `91206e7d-777e-40d3-b25a-851d35bbe5b4` |
| Tag | **single-answer** |
| 정답 | **C11** |
| C11 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3251147_4 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[829] topology](images/train_0829.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3214888_3
- `C2`: Increase transmission power for 3251147_4
- `C3`: Press down the tilt angle  of 3214888_3 by 1 degrees
- `C4`: Check test server and transmission issues
- `C5`: Lift the tilt angle  of 3214888_3 by 1 degrees
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3214888_3
- `C7`: Decrease A3 Offset threshold for 3251147_4
- `C8`: Lift the tilt angle of 3251147_4 by 5 degrees
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3251147_4
- `C10`: Press down the tilt angle of 3251147_4 by 5 degrees
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3251147_4 **← 정답**
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3214888_3
- `C13`: Decrease transmission power for 3214888_3
- `C14`: Increase A3 Offset threshold for 3251147_4
- `C15`: Adjust the azimuth of 3251147_4 by 13 degrees
- `C16`: Increase transmission power for 3214888_3
- `C17`: Decrease A3 Offset threshold for 3214888_3
- `C18`: Add neighbor relationship between 3264621_10 and 3214888_3
- `C19`: Adjust the azimuth of 3214888_3 by 28 degrees
- `C20`: Add neighbor relationship between 3251147_4 and 3214888_3
- `C21`: Insufficient data; more data is needed for judgment.
- `C22`: Decrease transmission power for 3251147_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.166 | MS1 | 121.4656670988 | 31.1446237798 | 169 | 504990 | -93.59 | 9.88 | 356.14 | 0.17 | 2.88 | 1595 |
| 2024-09-20 22:21:32.892 | MS1 | 121.4656613217 | 31.1446373280 | 441 | 504990 | -93.13 | 13.14 | 442.02 | 0.15 | 2.16 | 1570 |
| 2024-09-20 22:21:33.221 | MS1 | 121.4656708836 | 31.1446362767 | 238 | 504990 | -94.07 | 9.51 | 325.15 | 0.04 | 2.96 | 1599 |
| 2024-09-20 22:21:34.382 | MS1 | 121.4656722684 | 31.1446305535 | 452 | 152650 | -87.62 | 2.13 | 73.18 | 0.05 | 1.51 | 962 |
| 2024-09-20 22:21:35.801 | MS1 | 121.4656768809 | 31.1446338035 | 694 | 152650 | -92.23 | 2.08 | 62.93 | 0.11 | 1.78 | 927 |
| 2024-09-20 22:21:36.425 | MS1 | 121.4656750615 | 31.1446255838 | 137 | 152650 | -92.16 | 2.07 | 86.60 | 0.04 | 1.56 | 977 |
| 2024-09-20 22:21:37.306 | MS1 | 121.4656683601 | 31.1446253856 | 151 | 152650 | -90.04 | 5.85 | 103.05 | 0.08 | 1.81 | 996 |
| 2024-09-20 22:21:38.339 | MS1 | 121.4656723525 | 31.1446231254 | 452 | 152650 | -91.14 | 3.11 | 59.65 | 0.08 | 1.69 | 900 |
| 2024-09-20 22:21:39.931 | MS1 | 121.4656681165 | 31.1446359158 | 694 | 152650 | -90.16 | 7.97 | 83.95 | 0.06 | 1.51 | 981 |
| 2024-09-20 22:21:40.269 | MS1 | 121.4656624722 | 31.1446266646 | 137 | 152650 | -88.58 | 4.57 | 67.98 | 0.04 | 2.88 | 1596 |
| 2024-09-20 22:21:41.336 | MS1 | 121.4656638125 | 31.1446229907 | 151 | 152650 | -87.17 | 5.58 | 81.43 | 0.12 | 2.57 | 1564 |
| 2024-09-20 22:21:42.833 | MS1 | 121.4656629915 | 31.1446212440 | 452 | 152650 | -89.06 | 5.72 | 63.25 | 0.06 | 2.33 | 1598 |

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
| 3214888 | 3 | 121.4644498083 | 31.1545627144 | 146 | 1 | 8 | 2.1 | TDD | 902 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3218904 | 8 | 121.4756177097 | 31.1530822906 | 110 | 14 | 8 | 23.8 | FDD | 197 | n1 | 152650 | 30M | 4T4R | 25 | 152650 |
| 3225205 | 2 | 121.4645963939 | 31.1540378354 | 78 | 10 | 11 | 2.5 | TDD | 675 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3229215 | 7 | 121.4754262646 | 31.1512985378 | 118 | 5 | 2 | 25.4 | FDD | 452 | n1 | 152650 | 30M | 4T4R | 17 | 152650 |
| 3229668 | 9 | 121.4690192493 | 31.1477316735 | 276 | 13 | 1 | 23.4 | FDD | 631 | n1 | 152650 | 30M | 4T4R | 30 | 152650 |
| 3236339 | 6 | 121.4731681655 | 31.1465926346 | 27 | 1 | 10 | 18.1 | TDD | 441 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3242510 | 12 | 121.4731389009 | 31.1452815418 | 92 | 9 | 12 | 29.4 | FDD | 151 | n1 | 152650 | 30M | 4T4R | 24 | 152650 |
| 3243725 | 5 | 121.4665464646 | 31.1490519965 | 132 | 4 | 8 | 26.9 | TDD | 238 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3251147 | 4 | 121.4656722751 | 31.1495218888 | 193 | 4 | 11 | 13.9 | TDD | 169 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3258727 | 1 | 121.4738747949 | 31.1457700795 | 39 | 10 | 5 | 1.2 | TDD | 995 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3263964 | 11 | 121.4649121514 | 31.1522334803 | 355 | 3 | 6 | 27.3 | FDD | 694 | n1 | 152650 | 30M | 4T4R | 17 | 152650 |
| 3264621 | 10 | 121.4728402973 | 31.1498556364 | 348 | 6 | 5 | 24.0 | FDD | 137 | n1 | 152650 | 30M | 4T4R | 15 | 152650 |
| 3267314 | 13 | 121.4705888448 | 31.1523166669 | 156 | 2 | 0 | 27.5 | FDD | 729 | n1 | 152650 | 30M | 4T4R | 20 | 152650 |

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
| 2024-09-20 22:21:30.944 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.963 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.106 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.106 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.826 | NREventA2 | measId:1;ServCellPCI:920;Se... |
| 2024-09-20 22:21:34.935 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.225 | NREventA5 | measId:3;ServCellPCI:920;Se... |
| 2024-09-20 22:21:35.280 | NRHandoverAttempt | SourcePCI:920;SourceNR-ARFC... |
| 2024-09-20 22:21:35.313 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.323 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:35.465 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.465 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3258727 | 1 | 11.0513 | 6.2815 | -117.8724 | 5.3226 | 107.3322 | 0.0082 | 0.0146 |
| 2024_09_20 22:00 | 3225205 | 2 | 16.8411 | 11.0530 | -114.3939 | 6.1959 | 100.2448 | 0.0136 | 0.0007 |
| 2024_09_20 22:00 | 3214888 | 3 | 13.2582 | 19.5668 | -117.5020 | 5.4243 | 91.8589 | 0.0033 | 0.0016 |
| 2024_09_20 22:00 | 3251147 | 4 | 5.7027 | 12.9584 | -117.4077 | 15.3859 | 175.6265 | 0.0186 | 0.0097 |
| 2024_09_20 22:00 | 3243725 | 5 | 13.4297 | 16.2883 | -117.2899 | 7.0090 | 187.4816 | 0.0163 | 0.0111 |
| 2024_09_20 22:00 | 3236339 | 6 | 19.6329 | 7.7678 | -116.6843 | 16.7742 | 101.3561 | 0.0077 | 0.0183 |
| 2024_09_20 22:00 | 3229215 | 7 | 9.3768 | 19.0702 | -115.7818 | 3.4415 | 21.4669 | 0.0195 | 0.0093 |
| 2024_09_20 22:00 | 3218904 | 8 | 16.3817 | 18.8933 | -114.2821 | 4.3077 | 37.5194 | 0.0142 | 0.0010 |
| 2024_09_20 22:00 | 3229668 | 9 | 13.1009 | 8.5256 | -114.4331 | 3.4961 | 42.5485 | 0.0155 | 0.0057 |
| 2024_09_20 22:00 | 3264621 | 10 | 7.5798 | 8.3888 | -116.8485 | 4.7526 | 55.4776 | 0.0002 | 0.0072 |
| 2024_09_20 22:00 | 3263964 | 11 | 7.1838 | 16.8386 | -116.6269 | 3.7402 | 46.8819 | 0.0113 | 0.0171 |
| 2024_09_20 22:00 | 3242510 | 12 | 9.3762 | 18.5311 | -114.5311 | 3.1216 | 53.4045 | 0.0044 | 0.0134 |
| 2024_09_20 22:00 | 3267314 | 13 | 10.0458 | 12.1778 | -114.9837 | 4.9909 | 45.3658 | 0.0124 | 0.0111 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412903_08CA7983 | 152650 | 452 | -89.4 | 152650 | 729 | -94.3 | 152650 | 197 | -99.0 | 152650 | 631 |
| MR_1774412903_123E400C | 504990 | 238 | -92.1 | 504990 | 902 | -91.7 | 504990 | 995 | -97.2 | 504990 | 675 |
| MR_1774412903_9C66F5CB | 152650 | 452 | -85.6 | 152650 | 729 | -92.9 | 152650 | 197 | -99.5 | 152650 | 631 |
| MR_1774412903_2FE86B14 | 152650 | 452 | -88.3 | 152650 | 729 | -93.6 | 152650 | 197 | -96.3 | 152650 | 631 |
| MR_1774412903_B3229736 | 152650 | 452 | -89.6 | 152650 | 729 | -94.6 | 152650 | 197 | -97.3 | 152650 | 631 |
| MR_1774412903_3324F079 | 152650 | 452 | -88.2 | 152650 | 729 | -95.5 | 152650 | 197 | -99.9 | 152650 | 631 |

> *... 2개 열 생략 (전체 14열)*

---
