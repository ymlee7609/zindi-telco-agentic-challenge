# Track A 문제 분석 — train[780]~train[789]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[780] ~ train[789] (10개)

## 목차

1. [문제 780: `fb3d4cf2-570...`](#780) — single-answer, 정답: C2
2. [문제 781: `449cd931-ec8...`](#781) — single-answer, 정답: C5
3. [문제 782: `5f56d4a9-0c4...`](#782) — single-answer, 정답: C13
4. [문제 783: `667a8718-a30...`](#783) — multiple-answer, 정답: C19|C21
5. [문제 784: `29db47c2-60f...`](#784) — single-answer, 정답: C19
6. [문제 785: `cb34c478-3a5...`](#785) — single-answer, 정답: C20
7. [문제 786: `aeba6002-d85...`](#786) — single-answer, 정답: C1
8. [문제 787: `28e70abd-209...`](#787) — single-answer, 정답: C12
9. [문제 788: `917c1807-585...`](#788) — multiple-answer, 정답: C19|C22
10. [문제 789: `64c90886-f6b...`](#789) — single-answer, 정답: C3

---

### 문제 780: `fb3d4cf2-570...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `fb3d4cf2-5708-4fb7-9fc1-87d915b6604d` |
| Tag | **single-answer** |
| 정답 | **C2** |
| C2 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[780] topology](images/train_0780.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3239471_3
- `C2`: Check test server and transmission issues **← 정답**
- `C3`: Increase A3 Offset threshold for 3241529_2
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3241529_2
- `C5`: Press down the tilt angle  of 3239471_3 by 10 degrees
- `C6`: Lift the tilt angle  of 3239471_3 by 10 degrees
- `C7`: Press down the tilt angle of 3241529_2 by 10 degrees
- `C8`: Add neighbor relationship between 3228501_1 and 3239471_3
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3239471_3
- `C10`: Decrease A3 Offset threshold for 3241529_2
- `C11`: Adjust the azimuth of 3241529_2 by 50 degrees
- `C12`: Increase transmission power for 3241529_2
- `C13`: Adjust the azimuth of 3239471_3 by 50 degrees
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Decrease transmission power for 3241529_2
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3241529_2
- `C17`: Lift the tilt angle of 3241529_2 by 10 degrees
- `C18`: Decrease transmission power for 3239471_3
- `C19`: Increase transmission power for 3239471_3
- `C20`: Increase A3 Offset threshold for 3239471_3
- `C21`: Add neighbor relationship between 3241529_2 and 3239471_3
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3239471_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.730 | MS1 | 121.4656709772 | 31.1446259547 | 211 | 504990 | -89.30 | 15.31 | 468.98 | 0.18 | 2.50 | 1582 |
| 2024-09-20 22:21:32.169 | MS1 | 121.4656707927 | 31.1446295813 | 211 | 504990 | -85.23 | 13.38 | 346.82 | 0.14 | 2.03 | 1570 |
| 2024-09-20 22:21:33.111 | MS1 | 121.4656761892 | 31.1446348382 | 211 | 504990 | -91.83 | 13.82 | 417.20 | 0.04 | 2.54 | 1598 |
| 2024-09-20 22:21:34.782 | MS1 | 121.4656736579 | 31.1446188490 | 211 | 504990 | -89.60 | 17.70 | 94.52 | 0.16 | 2.77 | 418 |
| 2024-09-20 22:21:35.801 | MS1 | 121.4656767778 | 31.1446277472 | 211 | 504990 | -90.15 | 17.36 | 67.54 | 0.02 | 2.67 | 473 |
| 2024-09-20 22:21:36.460 | MS1 | 121.4656746235 | 31.1446322514 | 211 | 504990 | -85.76 | 15.24 | 67.10 | 0.15 | 2.87 | 354 |
| 2024-09-20 22:21:37.303 | MS1 | 121.4656732863 | 31.1446290480 | 211 | 504990 | -91.79 | 11.88 | 63.62 | 0.14 | 2.70 | 424 |
| 2024-09-20 22:21:38.681 | MS1 | 121.4656650183 | 31.1446193959 | 211 | 504990 | -92.39 | 8.98 | 50.55 | 0.17 | 2.06 | 465 |
| 2024-09-20 22:21:39.940 | MS1 | 121.4656750369 | 31.1446304643 | 211 | 504990 | -90.41 | 7.14 | 78.32 | 0.00 | 2.36 | 348 |
| 2024-09-20 22:21:40.582 | MS1 | 121.4656747712 | 31.1446314048 | 211 | 504990 | -92.52 | 10.27 | 377.34 | 0.04 | 2.94 | 1577 |
| 2024-09-20 22:21:41.425 | MS1 | 121.4656628785 | 31.1446229739 | 211 | 504990 | -93.65 | 9.29 | 558.57 | 0.02 | 2.85 | 1560 |
| 2024-09-20 22:21:42.333 | MS1 | 121.4656746836 | 31.1446277687 | 211 | 504990 | -92.64 | 12.69 | 466.93 | 0.17 | 2.42 | 1562 |

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
| 3228501 | 1 | 121.4725296513 | 31.1528687083 | 37 | 13 | 5 | 30.8 | TDD | 345 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3239471 | 3 | 121.4648411797 | 31.1502005443 | 117 | 15 | 0 | 25.8 | TDD | 621 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3241529 | 2 | 121.4693453934 | 31.1443909063 | 33 | 6 | 10 | 44.8 | TDD | 211 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3273481 | 4 | 121.4728516891 | 31.1473324317 | 256 | 11 | 3 | 36.2 | TDD | 645 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |

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
| 2024-09-20 22:21:30.753 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.769 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:30.895 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.895 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.615 | NREventA3 | measId:2;ServCellPCI:422;Se... |
| 2024-09-20 22:21:37.855 | NRHandoverAttempt | SourcePCI:422;SourceNR-ARFC... |
| 2024-09-20 22:21:37.894 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.904 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.053 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.053 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3228501 | 1 | 5.9717 | 6.4496 | -115.8200 | 9.0226 | 199.3098 | 0.0004 | 0.0024 |
| 2024_09_20 22:00 | 3241529 | 2 | 10.7752 | 18.9865 | -114.7505 | 9.4447 | 170.0624 | 0.0004 | 0.0198 |
| 2024_09_20 22:00 | 3239471 | 3 | 18.1919 | 17.3659 | -117.6734 | 17.6872 | 173.0173 | 0.0073 | 0.0026 |
| 2024_09_20 22:00 | 3273481 | 4 | 17.6807 | 5.7111 | -117.9185 | 17.2097 | 86.0328 | 0.0158 | 0.0174 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415912_0DD32F15 | 504990 | 211 | -88.2 | 504990 | 621 | -87.5 | 504990 | 345 | -101.8 | 504990 | 645 |
| MR_1774415912_273FA643 | 504990 | 211 | -90.8 | 504990 | 621 | -89.6 | 504990 | 345 | -100.1 | 504990 | 645 |
| MR_1774415912_397AFABD | 504990 | 211 | -88.6 | 504990 | 621 | -89.6 | 504990 | 345 | -103.0 | 504990 | 645 |
| MR_1774415912_A24D51FE | 504990 | 211 | -89.8 | 504990 | 621 | -88.2 | 504990 | 345 | -103.3 | 504990 | 645 |
| MR_1774415912_D05D1015 | 504990 | 211 | -89.0 | 504990 | 621 | -87.5 | 504990 | 345 | -103.9 | 504990 | 645 |
| MR_1774415912_838BB086 | 504990 | 211 | -91.1 | 504990 | 621 | -89.6 | 504990 | 345 | -100.7 | 504990 | 645 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 781: `449cd931-ec8...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `449cd931-ec85-4bde-961f-772775c18a97` |
| Tag | **single-answer** |
| 정답 | **C5** |
| C5 의미 | Add neighbor relationship between 3236671_1 and 3240041_2 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[781] topology](images/train_0781.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3240041_2 by 5 degrees
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3240041_2
- `C3`: Decrease transmission power for 3236671_1
- `C4`: Decrease A3 Offset threshold for 3236671_1
- `C5`: Add neighbor relationship between 3236671_1 and 3240041_2 **← 정답**
- `C6`: Increase A3 Offset threshold for 3236671_1
- `C7`: Add neighbor relationship between 3237202_3 and 3240041_2
- `C8`: Decrease transmission power for 3240041_2
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3240041_2
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3236671_1
- `C11`: Increase A3 Offset threshold for 3240041_2
- `C12`: Increase transmission power for 3240041_2
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3236671_1
- `C14`: Adjust the azimuth of 3236671_1 by 50 degrees
- `C15`: Insufficient data; more data is needed for judgment.
- `C16`: Lift the tilt angle of 3236671_1 by 10 degrees
- `C17`: Press down the tilt angle of 3236671_1 by 10 degrees
- `C18`: Lift the tilt angle  of 3240041_2 by 5 degrees
- `C19`: Adjust the azimuth of 3240041_2 by 38 degrees
- `C20`: Decrease A3 Offset threshold for 3240041_2
- `C21`: Check test server and transmission issues
- `C22`: Increase transmission power for 3236671_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.604 | MS1 | 121.4656685529 | 31.1446336671 | 313 | 504990 | -75.05 | 16.94 | 539.91 | 0.13 | 2.23 | 1587 |
| 2024-09-20 22:21:32.302 | MS1 | 121.4656732752 | 31.1446363241 | 313 | 504990 | -82.66 | 16.84 | 487.85 | 0.11 | 2.54 | 1564 |
| 2024-09-20 22:21:33.225 | MS1 | 121.4656623995 | 31.1446358194 | 313 | 504990 | -84.87 | 13.63 | 500.88 | 0.10 | 2.46 | 1600 |
| 2024-09-20 22:21:34.703 | MS1 | 121.4656696158 | 31.1446314319 | 313 | 504990 | -89.63 | -3.20 | 45.92 | 0.12 | 1.34 | 1595 |
| 2024-09-20 22:21:35.854 | MS1 | 121.4656774027 | 31.1446242613 | 313 | 504990 | -91.94 | -1.67 | 59.78 | 0.15 | 1.36 | 1577 |
| 2024-09-20 22:21:36.119 | MS1 | 121.4656588552 | 31.1446377149 | 313 | 504990 | -92.65 | -1.25 | 49.73 | 0.17 | 1.17 | 1587 |
| 2024-09-20 22:21:37.748 | MS1 | 121.4656636483 | 31.1446290204 | 313 | 504990 | -86.77 | -2.28 | 35.67 | 0.19 | 1.37 | 1566 |
| 2024-09-20 22:21:38.288 | MS1 | 121.4656735729 | 31.1446223406 | 313 | 504990 | -81.50 | 13.37 | 547.64 | 0.11 | 1.04 | 1592 |
| 2024-09-20 22:21:39.904 | MS1 | 121.4656700677 | 31.1446254328 | 313 | 504990 | -78.34 | 16.03 | 448.98 | 0.20 | 1.36 | 1578 |
| 2024-09-20 22:21:40.248 | MS1 | 121.4656588807 | 31.1446324291 | 313 | 504990 | -77.22 | 16.90 | 482.89 | 0.13 | 2.85 | 1578 |
| 2024-09-20 22:21:41.535 | MS1 | 121.4656694701 | 31.1446345839 | 313 | 504990 | -84.21 | 12.29 | 431.75 | 0.15 | 2.27 | 1586 |
| 2024-09-20 22:21:42.428 | MS1 | 121.4656615034 | 31.1446378637 | 313 | 504990 | -83.89 | 17.06 | 540.78 | 0.04 | 2.60 | 1565 |

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
| 3224843 | 4 | 121.4662778690 | 31.1522106784 | 148 | 12 | 0 | 29.7 | TDD | 475 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3236671 | 1 | 121.4646888679 | 31.1457521780 | 248 | 11 | 6 | 19.2 | TDD | 313 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3237202 | 3 | 121.4746802364 | 31.1459644725 | 294 | 13 | 11 | 36.3 | TDD | 894 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3240041 | 2 | 121.4718931416 | 31.1551342608 | 245 | 3 | 7 | 40.5 | TDD | 673 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:30.903 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.925 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.066 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.066 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.755 | NREventA3 | measId:2;ServCellPCI:332;Se... |
| 2024-09-20 22:21:35.755 | NREventA3 | measId:2;ServCellPCI:332;Se... |
| 2024-09-20 22:21:36.755 | NREventA3 | measId:2;ServCellPCI:332;Se... |
| 2024-09-20 22:21:39.255 | NRRRCReestablishAttempt | PCI:332 |
| 2024-09-20 22:21:39.270 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.281 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:39.402 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.402 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3236671 | 1 | 8.3908 | 11.0591 | -115.4662 | 18.8753 | 103.1375 | 0.0040 | 0.1632 |
| 2024_09_20 22:00 | 3240041 | 2 | 5.1459 | 16.8910 | -117.4905 | 13.7154 | 192.5683 | 0.0105 | 0.0175 |
| 2024_09_20 22:00 | 3237202 | 3 | 18.2677 | 16.1374 | -117.8185 | 12.0862 | 172.0224 | 0.0092 | 0.0070 |
| 2024_09_20 22:00 | 3224843 | 4 | 10.4138 | 9.5091 | -117.0635 | 8.1537 | 178.9308 | 0.0047 | 0.0003 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412368_7172E3E0 | 504990 | 313 | -89.5 | 504990 | 673 | -85.1 | 504990 | 894 | -84.9 | 504990 | 475 |
| MR_1774412368_3E02F069 | 504990 | 313 | -90.3 | 504990 | 673 | -85.4 | 504990 | 894 | -85.1 | 504990 | 475 |
| MR_1774412368_7A796BAF | 504990 | 673 | -85.1 | 504990 | 313 | -89.8 | 504990 | 894 | -85.6 | 504990 | 475 |
| MR_1774412368_1EDE3D8B | 504990 | 313 | -90.9 | 504990 | 673 | -86.9 | 504990 | 894 | -85.2 | 504990 | 475 |
| MR_1774412368_56EFCF58 | 504990 | 673 | -84.7 | 504990 | 313 | -90.3 | 504990 | 894 | -87.3 | 504990 | 475 |
| MR_1774412368_EA402EED | 504990 | 673 | -86.4 | 504990 | 313 | -90.5 | 504990 | 894 | -87.9 | 504990 | 475 |
| MR_1774412368_6C31DB9C | 504990 | 673 | -85.7 | 504990 | 313 | -88.2 | 504990 | 894 | -84.6 | 504990 | 475 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 782: `5f56d4a9-0c4...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `5f56d4a9-0c4b-4637-9909-438d16570989` |
| Tag | **single-answer** |
| 정답 | **C13** |
| C13 의미 | Add neighbor relationship between 3214703_3 and 3262467_1 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[782] topology](images/train_0782.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3262467_1 by 2 degrees
- `C2`: Check test server and transmission issues
- `C3`: Increase transmission power for 3262467_1
- `C4`: Add neighbor relationship between 3264952_4 and 3262467_1
- `C5`: Decrease A3 Offset threshold for 3214703_3
- `C6`: Increase transmission power for 3214703_3
- `C7`: Lift the tilt angle  of 3262467_1 by 2 degrees
- `C8`: Decrease A3 Offset threshold for 3262467_1
- `C9`: Insufficient data; more data is needed for judgment.
- `C10`: Increase A3 Offset threshold for 3262467_1
- `C11`: Press down the tilt angle of 3214703_3 by 10 degrees
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3262467_1
- `C13`: Add neighbor relationship between 3214703_3 and 3262467_1 **← 정답**
- `C14`: Adjust the azimuth of 3262467_1 by 32 degrees
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3214703_3
- `C16`: Adjust the azimuth of 3214703_3 by 5 degrees
- `C17`: Decrease transmission power for 3262467_1
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3262467_1
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3214703_3
- `C20`: Increase A3 Offset threshold for 3214703_3
- `C21`: Lift the tilt angle of 3214703_3 by 10 degrees
- `C22`: Decrease transmission power for 3214703_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.994 | MS1 | 121.4656637793 | 31.1446351091 | 141 | 504990 | -77.07 | 17.95 | 336.75 | 0.19 | 2.41 | 1568 |
| 2024-09-20 22:21:32.997 | MS1 | 121.4656762456 | 31.1446339064 | 141 | 504990 | -84.92 | 14.44 | 510.51 | 0.05 | 2.83 | 1562 |
| 2024-09-20 22:21:33.738 | MS1 | 121.4656724014 | 31.1446317093 | 141 | 504990 | -84.32 | 16.38 | 293.76 | 0.08 | 2.59 | 1564 |
| 2024-09-20 22:21:34.251 | MS1 | 121.4656683670 | 31.1446366004 | 141 | 504990 | -88.28 | -3.06 | 35.58 | 0.09 | 1.09 | 1586 |
| 2024-09-20 22:21:35.783 | MS1 | 121.4656730135 | 31.1446355622 | 141 | 504990 | -88.96 | -2.15 | 60.84 | 0.18 | 1.45 | 1584 |
| 2024-09-20 22:21:36.789 | MS1 | 121.4656614507 | 31.1446352167 | 141 | 504990 | -93.92 | -1.53 | 63.55 | 0.12 | 1.40 | 1600 |
| 2024-09-20 22:21:37.782 | MS1 | 121.4656743886 | 31.1446289374 | 141 | 504990 | -85.17 | -1.17 | 53.21 | 0.06 | 1.49 | 1599 |
| 2024-09-20 22:21:38.295 | MS1 | 121.4656651741 | 31.1446335435 | 141 | 504990 | -81.11 | 17.60 | 515.27 | 0.12 | 1.00 | 1600 |
| 2024-09-20 22:21:39.746 | MS1 | 121.4656581341 | 31.1446248123 | 141 | 504990 | -76.25 | 12.75 | 458.21 | 0.11 | 1.32 | 1587 |
| 2024-09-20 22:21:40.826 | MS1 | 121.4656662760 | 31.1446268418 | 141 | 504990 | -76.65 | 14.72 | 307.53 | 0.08 | 2.43 | 1583 |
| 2024-09-20 22:21:41.465 | MS1 | 121.4656738205 | 31.1446243514 | 141 | 504990 | -82.49 | 14.45 | 306.00 | 0.13 | 2.89 | 1564 |
| 2024-09-20 22:21:42.933 | MS1 | 121.4656713755 | 31.1446337389 | 141 | 504990 | -84.85 | 16.44 | 546.90 | 0.20 | 2.02 | 1589 |

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
| 3214703 | 3 | 121.4686891687 | 31.1455549262 | 245 | 15 | 4 | 30.9 | TDD | 141 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3245974 | 2 | 121.4642203080 | 31.1528422770 | 105 | 11 | 4 | 15.9 | TDD | 604 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3262467 | 1 | 121.4744858799 | 31.1492616948 | 270 | 0 | 12 | 39.0 | TDD | 393 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3264952 | 4 | 121.4673091324 | 31.1451769607 | 126 | 12 | 10 | 18.2 | TDD | 622 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:30.825 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.849 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:30.995 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.995 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.687 | NREventA3 | measId:2;ServCellPCI:215;Se... |
| 2024-09-20 22:21:35.687 | NREventA3 | measId:2;ServCellPCI:215;Se... |
| 2024-09-20 22:21:36.687 | NREventA3 | measId:2;ServCellPCI:215;Se... |
| 2024-09-20 22:21:39.187 | NRRRCReestablishAttempt | PCI:215 |
| 2024-09-20 22:21:39.202 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.214 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:39.335 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.335 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3262467 | 1 | 15.5326 | 9.2019 | -115.7256 | 17.8176 | 104.3406 | 0.0102 | 0.0001 |
| 2024_09_20 22:00 | 3245974 | 2 | 16.6693 | 10.9337 | -117.1695 | 5.4784 | 88.3160 | 0.0153 | 0.0171 |
| 2024_09_20 22:00 | 3214703 | 3 | 15.3926 | 19.5385 | -117.0646 | 19.3139 | 90.2792 | 0.0039 | 0.1613 |
| 2024_09_20 22:00 | 3264952 | 4 | 16.1411 | 14.0139 | -115.1122 | 19.9257 | 166.3157 | 0.0129 | 0.0088 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413593_E8B7617A | 504990 | 393 | -81.8 | 504990 | 141 | -86.5 | 504990 | 622 | -86.2 | 504990 | 604 |
| MR_1774413593_F775A765 | 504990 | 393 | -80.4 | 504990 | 141 | -87.5 | 504990 | 622 | -85.2 | 504990 | 604 |
| MR_1774413593_F183A545 | 504990 | 393 | -82.7 | 504990 | 141 | -87.4 | 504990 | 622 | -83.9 | 504990 | 604 |
| MR_1774413593_87860561 | 504990 | 393 | -83.4 | 504990 | 141 | -86.5 | 504990 | 622 | -86.5 | 504990 | 604 |
| MR_1774413593_EB03681B | 504990 | 141 | -89.4 | 504990 | 393 | -84.3 | 504990 | 622 | -84.2 | 504990 | 604 |
| MR_1774413593_139C26BF | 504990 | 393 | -82.0 | 504990 | 141 | -88.2 | 504990 | 622 | -83.4 | 504990 | 604 |
| MR_1774413593_109C10F7 | 504990 | 141 | -87.5 | 504990 | 393 | -83.6 | 504990 | 622 | -86.4 | 504990 | 604 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 783: `667a8718-a30...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `667a8718-a306-4388-9929-429ed098a420` |
| Tag | **multiple-answer** |
| 정답 | **C19|C21** |
| C19 의미 | Decrease transmission power for 3256638_1 |
| C21 의미 | Press down the tilt angle  of 3256638_1 by 5 degrees |
| 패턴 분류 | **P3 Overshoot (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[783] topology](images/train_0783.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3256638_1
- `C2`: Add neighbor relationship between 3276821_4 and 3256638_1
- `C3`: Lift the tilt angle  of 3256638_1 by 5 degrees
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3276821_4
- `C5`: Insufficient data; more data is needed for judgment.
- `C6`: Check test server and transmission issues
- `C7`: Press down the tilt angle of 3276821_4 by 4 degrees
- `C8`: Adjust the azimuth of 3276821_4 by 31 degrees
- `C9`: Increase transmission power for 3276821_4
- `C10`: Decrease transmission power for 3276821_4
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3256638_1
- `C12`: Increase transmission power for 3256638_1
- `C13`: Increase A3 Offset threshold for 3256638_1
- `C14`: Add neighbor relationship between 3249787_3 and 3256638_1
- `C15`: Adjust the azimuth of 3256638_1 by 6 degrees
- `C16`: Increase A3 Offset threshold for 3276821_4
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3276821_4
- `C18`: Lift the tilt angle of 3276821_4 by 4 degrees
- `C19`: Decrease transmission power for 3256638_1 **← 정답**
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3256638_1
- `C21`: Press down the tilt angle  of 3256638_1 by 5 degrees **← 정답**
- `C22`: Decrease A3 Offset threshold for 3276821_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.224 | MS1 | 121.4656600860 | 31.1446315281 | 510 | 504990 | -78.41 | 14.08 | 426.64 | 0.04 | 2.02 | 1592 |
| 2024-09-20 22:21:32.315 | MS1 | 121.4656726277 | 31.1446238429 | 510 | 504990 | -75.50 | 12.49 | 517.09 | 0.19 | 2.25 | 1562 |
| 2024-09-20 22:21:33.745 | MS1 | 121.4656632210 | 31.1446277755 | 510 | 504990 | -83.46 | 15.61 | 462.75 | 0.01 | 2.82 | 1565 |
| 2024-09-20 22:21:34.204 | MS1 | 121.4656605400 | 31.1446289540 | 510 | 504990 | -91.87 | 3.52 | 84.21 | 0.10 | 1.14 | 1570 |
| 2024-09-20 22:21:35.485 | MS1 | 121.4656759088 | 31.1446267397 | 510 | 504990 | -92.92 | 1.56 | 40.91 | 0.17 | 1.17 | 1594 |
| 2024-09-20 22:21:36.629 | MS1 | 121.4656711515 | 31.1446361681 | 510 | 504990 | -89.59 | 1.88 | 79.67 | 0.09 | 1.33 | 1571 |
| 2024-09-20 22:21:37.625 | MS1 | 121.4656629750 | 31.1446296018 | 510 | 504990 | -92.00 | 3.24 | 85.02 | 0.13 | 1.23 | 1578 |
| 2024-09-20 22:21:38.725 | MS1 | 121.4656683577 | 31.1446305218 | 510 | 504990 | -88.56 | 1.20 | 87.26 | 0.12 | 1.40 | 1590 |
| 2024-09-20 22:21:39.130 | MS1 | 121.4656625886 | 31.1446201768 | 510 | 504990 | -89.22 | 3.71 | 53.70 | 0.08 | 1.13 | 1587 |
| 2024-09-20 22:21:40.473 | MS1 | 121.4656769324 | 31.1446194165 | 510 | 504990 | -78.78 | 17.97 | 422.32 | 0.01 | 2.78 | 1578 |
| 2024-09-20 22:21:41.912 | MS1 | 121.4656604223 | 31.1446227444 | 510 | 504990 | -80.82 | 13.24 | 418.66 | 0.03 | 2.49 | 1579 |
| 2024-09-20 22:21:42.113 | MS1 | 121.4656697448 | 31.1446259852 | 510 | 504990 | -79.66 | 16.15 | 504.10 | 0.19 | 2.63 | 1591 |

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
| 3248127 | 2 | 121.4676300505 | 31.1480083119 | 57 | 12 | 1 | 44.8 | TDD | 778 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3249787 | 3 | 121.4671531684 | 31.1466533178 | 58 | 8 | 12 | 34.4 | TDD | 116 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3256638 | 1 | 121.4665142338 | 31.1522621214 | 191 | 3 | 3 | 29.3 | TDD | 672 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3276821 | 4 | 121.4707956141 | 31.1504898726 | 248 | 2 | 11 | 23.7 | TDD | 510 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |

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
| 2024-09-20 22:21:30.752 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.772 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:30.921 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.921 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3256638 | 1 | 15.6183 | 10.0049 | -114.5149 | 14.6065 | 159.6899 | 0.0013 | 0.0189 |
| 2024_09_20 22:00 | 3248127 | 2 | 7.3488 | 11.5695 | -114.4975 | 6.9079 | 86.4362 | 0.0119 | 0.0101 |
| 2024_09_20 22:00 | 3249787 | 3 | 7.6915 | 11.7346 | -115.3963 | 15.4055 | 197.8951 | 0.0097 | 0.0055 |
| 2024_09_20 22:00 | 3276821 | 4 | 14.9579 | 9.2460 | -109.5091 | 18.0573 | 110.5216 | 0.0099 | 0.0100 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413977_1A048496 | 504990 | 510 | -93.8 | 504990 | 672 | -88.4 | 504990 | 116 | -95.1 | 504990 | 778 |
| MR_1774413977_ADB19BC7 | 504990 | 672 | -91.1 | 504990 | 510 | -89.7 | 504990 | 116 | -94.4 | 504990 | 778 |
| MR_1774413977_CAD4DD59 | 504990 | 672 | -93.0 | 504990 | 510 | -87.9 | 504990 | 116 | -93.7 | 504990 | 778 |
| MR_1774413977_8F6104B7 | 504990 | 510 | -91.3 | 504990 | 672 | -89.5 | 504990 | 116 | -95.9 | 504990 | 778 |
| MR_1774413977_E0CCE47B | 504990 | 510 | -92.5 | 504990 | 672 | -89.2 | 504990 | 116 | -95.4 | 504990 | 778 |
| MR_1774413977_CA422AD9 | 504990 | 672 | -92.8 | 504990 | 510 | -88.8 | 504990 | 116 | -95.2 | 504990 | 778 |
| MR_1774413977_D60BA76D | 504990 | 510 | -91.7 | 504990 | 672 | -89.8 | 504990 | 116 | -94.8 | 504990 | 778 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 784: `29db47c2-60f...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `29db47c2-60f7-42bc-a9ff-fd52ef7da218` |
| Tag | **single-answer** |
| 정답 | **C19** |
| C19 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[784] topology](images/train_0784.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3279969_1
- `C2`: Decrease transmission power for 3279969_1
- `C3`: Press down the tilt angle  of 3212715_2 by 2 degrees
- `C4`: Add neighbor relationship between 3262770_4 and 3212715_2
- `C5`: Lift the tilt angle of 3279969_1 by 2 degrees
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3279969_1
- `C7`: Adjust the azimuth of 3212715_2 by 50 degrees
- `C8`: Lift the tilt angle  of 3212715_2 by 2 degrees
- `C9`: Add neighbor relationship between 3279969_1 and 3212715_2
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3212715_2
- `C11`: Increase transmission power for 3212715_2
- `C12`: Check test server and transmission issues
- `C13`: Decrease A3 Offset threshold for 3212715_2
- `C14`: Adjust the azimuth of 3279969_1 by 50 degrees
- `C15`: Press down the tilt angle of 3279969_1 by 2 degrees
- `C16`: Increase A3 Offset threshold for 3212715_2
- `C17`: Decrease A3 Offset threshold for 3279969_1
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3212715_2
- `C19`: Insufficient data; more data is needed for judgment. **← 정답**
- `C20`: Decrease transmission power for 3212715_2
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3279969_1
- `C22`: Increase A3 Offset threshold for 3279969_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.156 | MS1 | 121.4656668679 | 31.1446228218 | 787 | 504990 | -85.59 | 14.02 | 444.79 | 0.10 | 2.39 | 1573 |
| 2024-09-20 22:21:32.261 | MS1 | 121.4656679263 | 31.1446211876 | 787 | 504990 | -89.98 | 12.23 | 358.65 | 0.18 | 2.30 | 1567 |
| 2024-09-20 22:21:33.116 | MS1 | 121.4656659259 | 31.1446379869 | 787 | 504990 | -91.08 | 12.11 | 393.84 | 0.05 | 2.24 | 1571 |
| 2024-09-20 22:21:34.217 | MS1 | 121.4656669277 | 31.1446274472 | 787 | 504990 | -87.25 | 12.70 | 72.03 | 0.20 | 2.61 | 1584 |
| 2024-09-20 22:21:35.948 | MS1 | 121.4656641955 | 31.1446243564 | 787 | 504990 | -85.51 | 13.16 | 77.40 | 0.18 | 2.69 | 1600 |
| 2024-09-20 22:21:36.819 | MS1 | 121.4656764891 | 31.1446308750 | 787 | 504990 | -88.68 | 17.35 | 58.36 | 0.13 | 2.67 | 1577 |
| 2024-09-20 22:21:37.957 | MS1 | 121.4656734494 | 31.1446244806 | 787 | 504990 | -93.90 | 12.84 | 60.65 | 0.05 | 2.49 | 1575 |
| 2024-09-20 22:21:38.162 | MS1 | 121.4656622284 | 31.1446180667 | 787 | 504990 | -93.60 | 10.64 | 54.90 | 0.10 | 2.12 | 1591 |
| 2024-09-20 22:21:39.112 | MS1 | 121.4656611717 | 31.1446267066 | 787 | 504990 | -92.48 | 8.18 | 65.87 | 0.08 | 2.25 | 1599 |
| 2024-09-20 22:21:40.972 | MS1 | 121.4656721878 | 31.1446285423 | 787 | 504990 | -89.83 | 12.63 | 419.19 | 0.09 | 2.53 | 1564 |
| 2024-09-20 22:21:41.435 | MS1 | 121.4656688719 | 31.1446346812 | 787 | 504990 | -89.43 | 10.76 | 323.33 | 0.10 | 2.16 | 1575 |
| 2024-09-20 22:21:42.194 | MS1 | 121.4656622593 | 31.1446242815 | 787 | 504990 | -90.75 | 9.78 | 362.77 | 0.03 | 2.21 | 1590 |

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
| 3212715 | 2 | 121.4759519754 | 31.1500575392 | 39 | 1 | 10 | 20.2 | TDD | 284 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3262770 | 4 | 121.4729287983 | 31.1449102159 | 68 | 0 | 9 | 19.4 | TDD | 703 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3279442 | 3 | 121.4738103820 | 31.1504166260 | 4 | 10 | 8 | 29.3 | TDD | 685 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3279969 | 1 | 121.4706352589 | 31.1515634794 | 110 | 0 | 3 | 26.2 | TDD | 787 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:30.794 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.818 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:30.954 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.954 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.658 | NREventA3 | measId:2;ServCellPCI:652;Se... |
| 2024-09-20 22:21:37.898 | NRHandoverAttempt | SourcePCI:652;SourceNR-ARFC... |
| 2024-09-20 22:21:37.946 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.958 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.084 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.084 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3279969 | 1 | 84.4116 | 86.3727 | -117.4435 | 7.3577 | 150.4377 | 0.0097 | 0.0060 |
| 2024_09_19 22:00 | 3212715 | 2 | 82.1028 | 78.2856 | -115.4682 | 13.3848 | 115.4101 | 0.0137 | 0.0142 |
| 2024_09_19 22:00 | 3279442 | 3 | 93.8353 | 91.4371 | -116.1461 | 9.7808 | 169.6530 | 0.0021 | 0.0015 |
| 2024_09_19 22:00 | 3262770 | 4 | 78.5865 | 88.3080 | -117.6093 | 15.4253 | 145.8740 | 0.0065 | 0.0197 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413297_2F5D4396 | 504990 | 787 | -87.2 | 504990 | 284 | -92.4 | 504990 | 703 | -95.6 | 504990 | 685 |
| MR_1774413297_E22E00DB | 504990 | 787 | -87.2 | 504990 | 284 | -91.2 | 504990 | 703 | -94.8 | 504990 | 685 |
| MR_1774413297_0E1BEF60 | 504990 | 787 | -87.6 | 504990 | 284 | -90.1 | 504990 | 703 | -93.3 | 504990 | 685 |
| MR_1774413297_421DE64C | 504990 | 787 | -89.1 | 504990 | 284 | -90.9 | 504990 | 703 | -95.7 | 504990 | 685 |
| MR_1774413297_1A0EC14C | 504990 | 787 | -86.6 | 504990 | 284 | -89.9 | 504990 | 703 | -93.9 | 504990 | 685 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 785: `cb34c478-3a5...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `cb34c478-3a5b-4e2b-85c1-6553e8bd2987` |
| Tag | **single-answer** |
| 정답 | **C20** |
| C20 의미 | Lift the tilt angle  of 3237419_4 by 5 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[785] topology](images/train_0785.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3223174_3
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3223174_3
- `C3`: Increase transmission power for 3223174_3
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3275496_2
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3275496_2
- `C6`: Press down the tilt angle of 3223174_3 by 6 degrees
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3223174_3
- `C8`: Add neighbor relationship between 3237419_4 and 3275496_2
- `C9`: Lift the tilt angle of 3223174_3 by 6 degrees
- `C10`: Decrease A3 Offset threshold for 3275496_2
- `C11`: Insufficient data; more data is needed for judgment.
- `C12`: Decrease transmission power for 3275496_2
- `C13`: Increase A3 Offset threshold for 3275496_2
- `C14`: Press down the tilt angle  of 3237419_4 by 5 degrees
- `C15`: Adjust the azimuth of 3223174_3 by 22 degrees
- `C16`: Check test server and transmission issues
- `C17`: Decrease A3 Offset threshold for 3223174_3
- `C18`: Increase transmission power for 3275496_2
- `C19`: Decrease transmission power for 3223174_3
- `C20`: Lift the tilt angle  of 3237419_4 by 5 degrees **← 정답**
- `C21`: Adjust the azimuth of 3237419_4 by 50 degrees
- `C22`: Add neighbor relationship between 3223174_3 and 3275496_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.480 | MS1 | 121.4656583049 | 31.1446332090 | 748 | 504990 | -86.33 | 15.01 | 312.00 | 0.03 | 2.60 | 1591 |
| 2024-09-20 22:21:32.943 | MS1 | 121.4656622480 | 31.1446281284 | 748 | 504990 | -86.47 | 14.26 | 421.00 | 0.05 | 2.32 | 1581 |
| 2024-09-20 22:21:33.232 | MS1 | 121.4656766520 | 31.1446244271 | 748 | 504990 | -88.55 | 14.36 | 455.88 | 0.11 | 2.13 | 1589 |
| 2024-09-20 22:21:34.313 | MS1 | 121.4656673549 | 31.1446295385 | 748 | 504990 | -89.16 | 16.07 | 51.81 | 0.15 | 2.72 | 1566 |
| 2024-09-20 22:21:35.806 | MS1 | 121.4656717367 | 31.1446277008 | 748 | 504990 | -89.97 | 14.54 | 59.71 | 0.17 | 2.02 | 1564 |
| 2024-09-20 22:21:36.837 | MS1 | 121.4656765810 | 31.1446223941 | 748 | 504990 | -90.40 | 17.82 | 83.37 | 0.02 | 2.88 | 1595 |
| 2024-09-20 22:21:37.117 | MS1 | 121.4656752542 | 31.1446221722 | 748 | 504990 | -93.82 | 8.31 | 90.39 | 0.18 | 2.61 | 1600 |
| 2024-09-20 22:21:38.507 | MS1 | 121.4656689189 | 31.1446315882 | 748 | 504990 | -91.97 | 11.92 | 80.83 | 0.18 | 2.57 | 1592 |
| 2024-09-20 22:21:39.249 | MS1 | 121.4656719427 | 31.1446191334 | 748 | 504990 | -92.87 | 12.95 | 85.06 | 0.16 | 2.31 | 1566 |
| 2024-09-20 22:21:40.514 | MS1 | 121.4656680091 | 31.1446224929 | 748 | 504990 | -90.50 | 10.13 | 385.26 | 0.02 | 2.16 | 1595 |
| 2024-09-20 22:21:41.977 | MS1 | 121.4656590421 | 31.1446235047 | 748 | 504990 | -92.13 | 11.56 | 431.62 | 0.05 | 2.72 | 1594 |
| 2024-09-20 22:21:42.603 | MS1 | 121.4656772349 | 31.1446370261 | 748 | 504990 | -89.46 | 9.42 | 535.50 | 0.20 | 2.48 | 1566 |

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
| 3223174 | 3 | 121.4736771760 | 31.1553307930 | 191 | 5 | 8 | 21.5 | TDD | 748 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3233674 | 1 | 121.4729440984 | 31.1497837559 | 81 | 4 | 5 | 39.8 | TDD | 664 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3237419 | 4 | 121.4732689379 | 31.1483713873 | 353 | 13 | 8 | 28.3 | TDD | 30 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3275496 | 2 | 121.4757416645 | 31.1524778990 | 119 | 4 | 11 | 27.6 | TDD | 145 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:31.135 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.153 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.264 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.264 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.986 | NREventA3 | measId:2;ServCellPCI:897;Se... |
| 2024-09-20 22:21:38.226 | NRHandoverAttempt | SourcePCI:897;SourceNR-ARFC... |
| 2024-09-20 22:21:38.256 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.268 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.413 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.413 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3233674 | 1 | 15.8002 | 6.7049 | -115.7963 | 11.2802 | 166.1881 | 0.0133 | 0.0055 |
| 2024_09_20 22:00 | 3275496 | 2 | 10.3832 | 10.1107 | -117.7466 | 12.9597 | 125.3741 | 0.0165 | 0.0112 |
| 2024_09_20 22:00 | 3223174 | 3 | 81.0095 | 80.2336 | -117.6725 | 14.1643 | 177.4892 | 0.0108 | 0.0120 |
| 2024_09_20 22:00 | 3237419 | 4 | 16.7363 | 8.9131 | -114.8678 | 17.7301 | 84.9709 | 0.0158 | 0.0076 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417010_828114B5 | 504990 | 748 | -89.5 | 504990 | 145 | -89.1 | 504990 | 30 | -102.8 | 504990 | 664 |
| MR_1774417010_B28F5EC8 | 504990 | 748 | -90.3 | 504990 | 145 | -87.4 | 504990 | 30 | -105.3 | 504990 | 664 |
| MR_1774417010_DDA8BB33 | 504990 | 748 | -90.2 | 504990 | 145 | -89.4 | 504990 | 30 | -104.5 | 504990 | 664 |
| MR_1774417010_6D1C6A73 | 504990 | 748 | -88.4 | 504990 | 145 | -90.4 | 504990 | 30 | -104.5 | 504990 | 664 |
| MR_1774417010_75AAE9CB | 504990 | 748 | -90.3 | 504990 | 145 | -89.6 | 504990 | 30 | -102.5 | 504990 | 664 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 786: `aeba6002-d85...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `aeba6002-d85b-4b2e-99e4-50f0dac238bd` |
| Tag | **single-answer** |
| 정답 | **C1** |
| C1 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3254083_6 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[786] topology](images/train_0786.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3254083_6 **← 정답**
- `C2`: Check test server and transmission issues
- `C3`: Increase transmission power for 3254835_5
- `C4`: Add neighbor relationship between 3254083_6 and 3254835_5
- `C5`: Decrease A3 Offset threshold for 3254835_5
- `C6`: Press down the tilt angle of 3254083_6 by 1 degrees
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3254835_5
- `C8`: Increase transmission power for 3254083_6
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3254835_5
- `C10`: Adjust the azimuth of 3254083_6 by 28 degrees
- `C11`: Lift the tilt angle of 3254083_6 by 1 degrees
- `C12`: Decrease A3 Offset threshold for 3254083_6
- `C13`: Add neighbor relationship between 3236849_13 and 3254835_5
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Lift the tilt angle  of 3254835_5 by 4 degrees
- `C16`: Decrease transmission power for 3254083_6
- `C17`: Decrease transmission power for 3254835_5
- `C18`: Adjust the azimuth of 3254835_5 by 25 degrees
- `C19`: Increase A3 Offset threshold for 3254835_5
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3254083_6
- `C21`: Increase A3 Offset threshold for 3254083_6
- `C22`: Press down the tilt angle  of 3254835_5 by 4 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.967 | MS1 | 121.4656652159 | 31.1446347827 | 415 | 504990 | -94.69 | 10.18 | 429.41 | 0.08 | 2.59 | 1600 |
| 2024-09-20 22:21:32.875 | MS1 | 121.4656658788 | 31.1446307162 | 101 | 504990 | -93.77 | 11.93 | 385.74 | 0.16 | 2.20 | 1583 |
| 2024-09-20 22:21:33.315 | MS1 | 121.4656691125 | 31.1446308787 | 33 | 504990 | -93.73 | 14.41 | 304.88 | 0.01 | 2.84 | 1568 |
| 2024-09-20 22:21:34.296 | MS1 | 121.4656678874 | 31.1446191051 | 138 | 152650 | -91.58 | 5.60 | 90.70 | 0.12 | 1.74 | 936 |
| 2024-09-20 22:21:35.838 | MS1 | 121.4656710680 | 31.1446203654 | 111 | 152650 | -95.80 | 3.12 | 42.38 | 0.17 | 1.86 | 934 |
| 2024-09-20 22:21:36.111 | MS1 | 121.4656584567 | 31.1446225037 | 318 | 152650 | -96.94 | 7.53 | 84.78 | 0.13 | 1.70 | 952 |
| 2024-09-20 22:21:37.809 | MS1 | 121.4656762298 | 31.1446245218 | 256 | 152650 | -94.52 | 3.28 | 92.04 | 0.02 | 1.70 | 952 |
| 2024-09-20 22:21:38.811 | MS1 | 121.4656698650 | 31.1446324194 | 138 | 152650 | -87.46 | 7.53 | 89.96 | 0.14 | 1.72 | 904 |
| 2024-09-20 22:21:39.805 | MS1 | 121.4656700573 | 31.1446183030 | 111 | 152650 | -91.70 | 7.67 | 65.63 | 0.10 | 1.70 | 935 |
| 2024-09-20 22:21:40.859 | MS1 | 121.4656606962 | 31.1446229830 | 318 | 152650 | -90.21 | 5.58 | 51.33 | 0.03 | 2.25 | 1584 |
| 2024-09-20 22:21:41.730 | MS1 | 121.4656701464 | 31.1446251234 | 256 | 152650 | -92.38 | 2.51 | 101.24 | 0.01 | 2.86 | 1578 |
| 2024-09-20 22:21:42.228 | MS1 | 121.4656591684 | 31.1446275659 | 138 | 152650 | -94.87 | 3.40 | 80.18 | 0.13 | 2.47 | 1569 |

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
| 3218318 | 7 | 121.4720204012 | 31.1517347319 | 8 | 5 | 0 | 8.5 | FDD | 256 | n1 | 152650 | 30M | 4T4R | 24 | 152650 |
| 3222071 | 10 | 121.4689023449 | 31.1540012414 | 245 | 14 | 12 | 6.6 | FDD | 111 | n1 | 152650 | 30M | 4T4R | 14 | 152650 |
| 3222425 | 12 | 121.4670309487 | 31.1540614155 | 35 | 11 | 5 | 16.6 | FDD | 668 | n1 | 152650 | 30M | 4T4R | 10 | 152650 |
| 3234759 | 2 | 121.4732295276 | 31.1474645816 | 351 | 10 | 4 | 17.2 | TDD | 257 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3235044 | 9 | 121.4703141369 | 31.1463844699 | 129 | 15 | 4 | 11.4 | FDD | 138 | n1 | 152650 | 30M | 4T4R | 21 | 152650 |
| 3236849 | 13 | 121.4644127210 | 31.1549213944 | 200 | 3 | 12 | 24.2 | FDD | 318 | n1 | 152650 | 30M | 4T4R | 22 | 152650 |
| 3237165 | 11 | 121.4703883945 | 31.1508009290 | 233 | 12 | 7 | 25.2 | FDD | 215 | n1 | 152650 | 30M | 4T4R | 28 | 152650 |
| 3244068 | 4 | 121.4735023688 | 31.1491158488 | 30 | 7 | 11 | 22.9 | TDD | 878 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3251208 | 3 | 121.4752447722 | 31.1525450987 | 310 | 15 | 4 | 28.8 | TDD | 101 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3254083 | 6 | 121.4678772713 | 31.1480767079 | 237 | 0 | 6 | 9.9 | TDD | 415 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3254835 | 5 | 121.4663041267 | 31.1447069769 | 236 | 1 | 12 | 3.3 | TDD | 277 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3264987 | 8 | 121.4685033574 | 31.1518679890 | 93 | 7 | 5 | 28.3 | FDD | 768 | n1 | 152650 | 30M | 4T4R | 28 | 152650 |
| 3265791 | 1 | 121.4744426461 | 31.1461598892 | 325 | 14 | 3 | 15.1 | TDD | 33 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |

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
| 2024-09-20 22:21:31.435 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.453 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.584 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.584 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.296 | NREventA2 | measId:1;ServCellPCI:868;Se... |
| 2024-09-20 22:21:35.435 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.698 | NREventA5 | measId:3;ServCellPCI:868;Se... |
| 2024-09-20 22:21:35.761 | NRHandoverAttempt | SourcePCI:868;SourceNR-ARFC... |
| 2024-09-20 22:21:35.788 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.802 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:35.915 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.915 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3265791 | 1 | 19.2086 | 5.3683 | -116.5626 | 10.3855 | 127.1495 | 0.0108 | 0.0086 |
| 2024_09_20 22:00 | 3234759 | 2 | 5.7665 | 19.2550 | -117.2379 | 6.5636 | 107.9623 | 0.0155 | 0.0091 |
| 2024_09_20 22:00 | 3251208 | 3 | 17.2176 | 16.0052 | -115.9524 | 12.5841 | 135.0959 | 0.0074 | 0.0110 |
| 2024_09_20 22:00 | 3244068 | 4 | 16.3124 | 13.3781 | -117.9368 | 10.1256 | 93.2148 | 0.0175 | 0.0163 |
| 2024_09_20 22:00 | 3254835 | 5 | 7.7117 | 5.0649 | -114.0323 | 9.6700 | 92.2225 | 0.0192 | 0.0075 |
| 2024_09_20 22:00 | 3254083 | 6 | 17.1978 | 13.5617 | -114.0805 | 14.9185 | 112.0219 | 0.0155 | 0.0128 |
| 2024_09_20 22:00 | 3218318 | 7 | 9.7436 | 18.8716 | -117.8464 | 4.7340 | 47.2296 | 0.0182 | 0.0077 |
| 2024_09_20 22:00 | 3264987 | 8 | 6.2059 | 17.1235 | -115.0119 | 3.0567 | 49.9912 | 0.0119 | 0.0052 |
| 2024_09_20 22:00 | 3235044 | 9 | 14.3811 | 16.3987 | -116.7435 | 3.4724 | 34.7172 | 0.0171 | 0.0146 |
| 2024_09_20 22:00 | 3222071 | 10 | 12.0992 | 9.8313 | -117.6861 | 3.5160 | 23.4801 | 0.0062 | 0.0059 |
| 2024_09_20 22:00 | 3237165 | 11 | 6.4808 | 12.6733 | -114.3435 | 4.7888 | 20.3570 | 0.0105 | 0.0040 |
| 2024_09_20 22:00 | 3222425 | 12 | 19.3833 | 10.7534 | -117.8244 | 3.5617 | 32.9268 | 0.0007 | 0.0136 |
| 2024_09_20 22:00 | 3236849 | 13 | 13.9515 | 5.8796 | -116.4218 | 4.3257 | 56.9076 | 0.0023 | 0.0165 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415577_FF93047C | 152650 | 138 | -89.6 | 152650 | 768 | -94.2 | 152650 | 668 | -101.0 | 152650 | 215 |
| MR_1774415577_8B8BEF90 | 152650 | 138 | -93.3 | 152650 | 768 | -93.5 | 152650 | 668 | -99.9 | 152650 | 215 |
| MR_1774415577_4445B62F | 152650 | 138 | -91.1 | 152650 | 768 | -94.5 | 152650 | 668 | -100.1 | 152650 | 215 |
| MR_1774415577_2C47C67F | 504990 | 33 | -95.6 | 504990 | 277 | -91.2 | 504990 | 257 | -96.1 | 504990 | 878 |
| MR_1774415577_64417006 | 504990 | 33 | -94.4 | 504990 | 277 | -91.8 | 504990 | 257 | -94.2 | 504990 | 878 |
| MR_1774415577_CD574014 | 504990 | 33 | -95.2 | 504990 | 277 | -91.2 | 504990 | 257 | -93.0 | 504990 | 878 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 787: `28e70abd-209...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `28e70abd-209d-49fa-8513-c8df6bbc6f63` |
| Tag | **single-answer** |
| 정답 | **C12** |
| C12 의미 | Add neighbor relationship between 3217078_1 and 3253649_4 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[787] topology](images/train_0787.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3253649_4
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3253649_4
- `C3`: Decrease transmission power for 3253649_4
- `C4`: Add neighbor relationship between 3259359_3 and 3253649_4
- `C5`: Increase transmission power for 3217078_1
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3217078_1
- `C7`: Increase A3 Offset threshold for 3253649_4
- `C8`: Decrease transmission power for 3217078_1
- `C9`: Insufficient data; more data is needed for judgment.
- `C10`: Adjust the azimuth of 3253649_4 by 1 degrees
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3253649_4
- `C12`: Add neighbor relationship between 3217078_1 and 3253649_4 **← 정답**
- `C13`: Increase A3 Offset threshold for 3217078_1
- `C14`: Lift the tilt angle  of 3253649_4 by 6 degrees
- `C15`: Adjust the azimuth of 3217078_1 by 9 degrees
- `C16`: Lift the tilt angle of 3217078_1 by 10 degrees
- `C17`: Press down the tilt angle of 3217078_1 by 10 degrees
- `C18`: Press down the tilt angle  of 3253649_4 by 6 degrees
- `C19`: Decrease A3 Offset threshold for 3217078_1
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3217078_1
- `C21`: Check test server and transmission issues
- `C22`: Decrease A3 Offset threshold for 3253649_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.417 | MS1 | 121.4656688778 | 31.1446271612 | 819 | 504990 | -76.77 | 16.71 | 426.03 | 0.14 | 2.25 | 1588 |
| 2024-09-20 22:21:32.257 | MS1 | 121.4656687785 | 31.1446190594 | 819 | 504990 | -81.95 | 14.12 | 369.10 | 0.01 | 2.38 | 1580 |
| 2024-09-20 22:21:33.253 | MS1 | 121.4656580978 | 31.1446305226 | 819 | 504990 | -81.09 | 13.55 | 334.46 | 0.17 | 2.41 | 1581 |
| 2024-09-20 22:21:34.766 | MS1 | 121.4656712869 | 31.1446254260 | 819 | 504990 | -94.42 | -2.37 | 48.10 | 0.12 | 1.48 | 1561 |
| 2024-09-20 22:21:35.943 | MS1 | 121.4656707388 | 31.1446253723 | 819 | 504990 | -85.19 | -0.61 | 35.99 | 0.12 | 1.33 | 1600 |
| 2024-09-20 22:21:36.128 | MS1 | 121.4656618664 | 31.1446365949 | 819 | 504990 | -88.56 | -1.91 | 37.61 | 0.01 | 1.27 | 1583 |
| 2024-09-20 22:21:37.446 | MS1 | 121.4656709258 | 31.1446344347 | 819 | 504990 | -85.67 | -0.12 | 39.20 | 0.02 | 1.12 | 1563 |
| 2024-09-20 22:21:38.370 | MS1 | 121.4656595726 | 31.1446326812 | 819 | 504990 | -83.80 | 14.01 | 560.77 | 0.02 | 1.03 | 1591 |
| 2024-09-20 22:21:39.331 | MS1 | 121.4656656295 | 31.1446343017 | 819 | 504990 | -80.12 | 14.94 | 545.38 | 0.03 | 1.32 | 1577 |
| 2024-09-20 22:21:40.197 | MS1 | 121.4656775939 | 31.1446363974 | 819 | 504990 | -77.72 | 16.50 | 324.53 | 0.06 | 2.47 | 1600 |
| 2024-09-20 22:21:41.374 | MS1 | 121.4656634435 | 31.1446278055 | 819 | 504990 | -75.92 | 17.55 | 305.75 | 0.01 | 2.45 | 1589 |
| 2024-09-20 22:21:42.779 | MS1 | 121.4656706085 | 31.1446231442 | 819 | 504990 | -83.63 | 17.33 | 543.82 | 0.13 | 2.35 | 1577 |

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
| 3217078 | 1 | 121.4709834107 | 31.1522598271 | 202 | 12 | 4 | 29.1 | TDD | 819 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3221234 | 2 | 121.4686793417 | 31.1441150754 | 150 | 0 | 7 | 30.5 | TDD | 794 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3253649 | 4 | 121.4715375811 | 31.1531127767 | 212 | 3 | 9 | 48.7 | TDD | 525 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3259359 | 3 | 121.4687749432 | 31.1442905693 | 107 | 12 | 5 | 15.7 | TDD | 523 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:31.549 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.564 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.677 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.677 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.389 | NREventA3 | measId:2;ServCellPCI:327;Se... |
| 2024-09-20 22:21:36.389 | NREventA3 | measId:2;ServCellPCI:327;Se... |
| 2024-09-20 22:21:37.389 | NREventA3 | measId:2;ServCellPCI:327;Se... |
| 2024-09-20 22:21:39.889 | NRRRCReestablishAttempt | PCI:327 |
| 2024-09-20 22:21:39.900 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.912 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:40.034 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:40.034 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3217078 | 1 | 15.7645 | 11.7400 | -114.1747 | 11.4365 | 166.8063 | 0.0198 | 0.1115 |
| 2024_09_20 22:00 | 3221234 | 2 | 16.1537 | 8.7005 | -117.2139 | 13.0325 | 126.4082 | 0.0007 | 0.0044 |
| 2024_09_20 22:00 | 3259359 | 3 | 13.7669 | 16.9905 | -115.3740 | 19.0295 | 121.2793 | 0.0137 | 0.0169 |
| 2024_09_20 22:00 | 3253649 | 4 | 19.6261 | 12.8645 | -117.6688 | 13.6380 | 131.4208 | 0.0185 | 0.0032 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416197_2B796532 | 504990 | 525 | -90.0 | 504990 | 819 | -93.4 | 504990 | 523 | -97.7 | 504990 | 794 |
| MR_1774416197_B97A03AA | 504990 | 525 | -91.7 | 504990 | 819 | -95.3 | 504990 | 523 | -97.3 | 504990 | 794 |
| MR_1774416197_7CC08DD4 | 504990 | 819 | -96.0 | 504990 | 525 | -88.0 | 504990 | 523 | -96.2 | 504990 | 794 |
| MR_1774416197_3EC02C83 | 504990 | 819 | -94.7 | 504990 | 525 | -89.4 | 504990 | 523 | -98.5 | 504990 | 794 |
| MR_1774416197_77D11088 | 504990 | 525 | -91.4 | 504990 | 819 | -95.7 | 504990 | 523 | -98.2 | 504990 | 794 |
| MR_1774416197_5888733E | 504990 | 819 | -96.1 | 504990 | 525 | -88.8 | 504990 | 523 | -96.7 | 504990 | 794 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 788: `917c1807-585...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `917c1807-5858-41b2-a237-038172179c1d` |
| Tag | **multiple-answer** |
| 정답 | **C19|C22** |
| C19 의미 | Adjust the azimuth of 3260928_1 by 50 degrees |
| C22 의미 | Increase transmission power for 3260928_1 |
| 패턴 분류 | **P4 Coverage (azimuth)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[788] topology](images/train_0788.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle of 3260928_1 by 10 degrees
- `C2`: Lift the tilt angle  of 3233038_2 by 6 degrees
- `C3`: Increase transmission power for 3233038_2
- `C4`: Check test server and transmission issues
- `C5`: Lift the tilt angle of 3260928_1 by 10 degrees
- `C6`: Add neighbor relationship between 3260928_1 and 3233038_2
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3233038_2
- `C8`: Decrease transmission power for 3260928_1
- `C9`: Decrease transmission power for 3233038_2
- `C10`: Decrease A3 Offset threshold for 3260928_1
- `C11`: Press down the tilt angle  of 3233038_2 by 6 degrees
- `C12`: Increase A3 Offset threshold for 3260928_1
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3260928_1
- `C14`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3260928_1
- `C15`: Adjust the azimuth of 3233038_2 by 3 degrees
- `C16`: Increase A3 Offset threshold for 3233038_2
- `C17`: Decrease A3 Offset threshold for 3233038_2
- `C18`: Add neighbor relationship between 3216673_3 and 3233038_2
- `C19`: Adjust the azimuth of 3260928_1 by 50 degrees **← 정답**
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3233038_2
- `C21`: Insufficient data; more data is needed for judgment.
- `C22`: Increase transmission power for 3260928_1 **← 정답**

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.334 | MS1 | 121.4656591658 | 31.1446303312 | 584 | 504990 | -94.09 | 17.57 | 548.76 | 0.20 | 2.43 | 1579 |
| 2024-09-20 22:21:32.346 | MS1 | 121.4656616935 | 31.1446233269 | 584 | 504990 | -87.07 | 15.17 | 505.84 | 0.01 | 2.75 | 1576 |
| 2024-09-20 22:21:33.269 | MS1 | 121.4656742019 | 31.1446217583 | 584 | 504990 | -86.88 | 16.88 | 583.90 | 0.09 | 2.17 | 1593 |
| 2024-09-20 22:21:34.254 | MS1 | 121.4656614035 | 31.1446309345 | 584 | 504990 | -101.74 | 0.61 | 37.69 | 0.01 | 1.42 | 1580 |
| 2024-09-20 22:21:35.363 | MS1 | 121.4656616679 | 31.1446260249 | 584 | 504990 | -101.25 | -0.25 | 63.85 | 0.13 | 1.03 | 1587 |
| 2024-09-20 22:21:36.108 | MS1 | 121.4656711985 | 31.1446294724 | 584 | 504990 | -104.66 | -0.85 | 53.60 | 0.04 | 1.08 | 1599 |
| 2024-09-20 22:21:37.142 | MS1 | 121.4656652951 | 31.1446216106 | 584 | 504990 | -101.92 | -1.45 | 40.82 | 0.13 | 1.13 | 1562 |
| 2024-09-20 22:21:38.756 | MS1 | 121.4656756167 | 31.1446207284 | 584 | 504990 | -105.84 | 0.67 | 61.37 | 0.17 | 1.28 | 1578 |
| 2024-09-20 22:21:39.623 | MS1 | 121.4656770112 | 31.1446197747 | 584 | 504990 | -108.53 | -1.96 | 79.98 | 0.02 | 1.45 | 1566 |
| 2024-09-20 22:21:40.568 | MS1 | 121.4656722414 | 31.1446197288 | 584 | 504990 | -86.62 | 14.16 | 449.28 | 0.07 | 2.81 | 1593 |
| 2024-09-20 22:21:41.483 | MS1 | 121.4656737178 | 31.1446371445 | 584 | 504990 | -85.76 | 12.66 | 555.48 | 0.13 | 2.77 | 1581 |
| 2024-09-20 22:21:42.376 | MS1 | 121.4656599758 | 31.1446358322 | 584 | 504990 | -91.82 | 12.12 | 499.43 | 0.13 | 2.11 | 1576 |

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
| 3216673 | 3 | 121.4728501090 | 31.1493140800 | 6 | 8 | 2 | 19.1 | TDD | 156 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3225130 | 4 | 121.4734452589 | 31.1454953341 | 273 | 4 | 10 | 32.5 | TDD | 912 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3233038 | 2 | 121.4753945316 | 31.1513935704 | 228 | 4 | 4 | 33.0 | TDD | 27 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3260928 | 1 | 121.4663246023 | 31.1507607896 | 135 | 6 | 3 | 43.7 | TDD | 584 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |

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
| 2024-09-20 22:21:31.545 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.561 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.683 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.683 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.945 | NREventA2 | measId:1;ServCellPCI:991;Se... |
| 2024-09-20 22:21:35.070 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3260928 | 1 | 9.1683 | 9.1161 | -114.1629 | 7.0544 | 194.2415 | 0.1847 | 0.0139 |
| 2024_09_20 22:00 | 3233038 | 2 | 8.1756 | 17.1875 | -116.5389 | 15.3267 | 171.6928 | 0.0147 | 0.0097 |
| 2024_09_20 22:00 | 3216673 | 3 | 6.0000 | 9.5750 | -116.3194 | 7.8263 | 96.4999 | 0.0110 | 0.0029 |
| 2024_09_20 22:00 | 3225130 | 4 | 17.7863 | 10.8221 | -114.1705 | 10.2518 | 139.7252 | 0.0092 | 0.0087 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412672_416F14AE | 504990 | 584 | -100.7 | 504990 | 27 | -109.6 | 504990 | 156 | -114.7 | 504990 | 912 |
| MR_1774412672_02E74A6B | 504990 | 584 | -100.4 | 504990 | 27 | -108.3 | 504990 | 156 | -113.0 | 504990 | 912 |
| MR_1774412672_907D1740 | 504990 | 584 | -101.0 | 504990 | 27 | -109.2 | 504990 | 156 | -112.5 | 504990 | 912 |
| MR_1774412672_710BD93C | 504990 | 584 | -101.7 | 504990 | 27 | -108.6 | 504990 | 156 | -112.5 | 504990 | 912 |
| MR_1774412672_3A046847 | 504990 | 584 | -101.3 | 504990 | 27 | -109.2 | 504990 | 156 | -115.6 | 504990 | 912 |
| MR_1774412672_05D73ABF | 504990 | 584 | -100.1 | 504990 | 27 | -108.5 | 504990 | 156 | -114.4 | 504990 | 912 |
| MR_1774412672_D3435754 | 504990 | 584 | -103.5 | 504990 | 27 | -108.8 | 504990 | 156 | -112.0 | 504990 | 912 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 789: `64c90886-f6b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `64c90886-f6b8-43f9-b84b-4ffd9060a5c1` |
| Tag | **single-answer** |
| 정답 | **C3** |
| C3 의미 | Lift the tilt angle  of 3269349_1 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[789] topology](images/train_0789.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3261234_3
- `C2`: Increase A3 Offset threshold for 3276707_2
- `C3`: Lift the tilt angle  of 3269349_1 by 10 degrees **← 정답**
- `C4`: Increase transmission power for 3276707_2
- `C5`: Decrease transmission power for 3276707_2
- `C6`: Add neighbor relationship between 3261234_3 and 3276707_2
- `C7`: Increase transmission power for 3261234_3
- `C8`: Adjust the azimuth of 3269349_1 by 50 degrees
- `C9`: Press down the tilt angle  of 3269349_1 by 10 degrees
- `C10`: Lift the tilt angle of 3261234_3 by 5 degrees
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3261234_3
- `C12`: Decrease A3 Offset threshold for 3261234_3
- `C13`: Press down the tilt angle of 3261234_3 by 5 degrees
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3276707_2
- `C16`: Decrease A3 Offset threshold for 3276707_2
- `C17`: Decrease transmission power for 3261234_3
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3276707_2
- `C19`: Increase A3 Offset threshold for 3261234_3
- `C20`: Adjust the azimuth of 3261234_3 by 7 degrees
- `C21`: Add neighbor relationship between 3269349_1 and 3276707_2
- `C22`: Check test server and transmission issues

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.819 | MS1 | 121.4656768422 | 31.1446270968 | 623 | 504990 | -90.24 | 15.86 | 487.59 | 0.03 | 2.77 | 1592 |
| 2024-09-20 22:21:32.800 | MS1 | 121.4656672446 | 31.1446306607 | 623 | 504990 | -88.25 | 14.46 | 555.14 | 0.02 | 2.37 | 1571 |
| 2024-09-20 22:21:33.217 | MS1 | 121.4656725811 | 31.1446378672 | 623 | 504990 | -91.15 | 12.84 | 403.46 | 0.14 | 2.16 | 1574 |
| 2024-09-20 22:21:34.574 | MS1 | 121.4656716174 | 31.1446209862 | 623 | 504990 | -90.05 | 13.46 | 96.16 | 0.05 | 2.81 | 1598 |
| 2024-09-20 22:21:35.579 | MS1 | 121.4656626440 | 31.1446347183 | 623 | 504990 | -85.64 | 13.82 | 57.78 | 0.12 | 2.71 | 1595 |
| 2024-09-20 22:21:36.493 | MS1 | 121.4656593105 | 31.1446329288 | 623 | 504990 | -86.82 | 17.72 | 48.60 | 0.17 | 2.92 | 1560 |
| 2024-09-20 22:21:37.665 | MS1 | 121.4656673259 | 31.1446215972 | 623 | 504990 | -89.22 | 8.47 | 78.55 | 0.11 | 2.20 | 1598 |
| 2024-09-20 22:21:38.186 | MS1 | 121.4656752378 | 31.1446260015 | 623 | 504990 | -89.30 | 10.94 | 60.03 | 0.10 | 2.31 | 1584 |
| 2024-09-20 22:21:39.652 | MS1 | 121.4656615489 | 31.1446182978 | 623 | 504990 | -92.66 | 10.78 | 94.98 | 0.04 | 2.89 | 1583 |
| 2024-09-20 22:21:40.334 | MS1 | 121.4656645625 | 31.1446278999 | 623 | 504990 | -89.47 | 10.90 | 373.79 | 0.07 | 2.85 | 1566 |
| 2024-09-20 22:21:41.410 | MS1 | 121.4656698021 | 31.1446361187 | 623 | 504990 | -92.29 | 10.91 | 384.92 | 0.13 | 2.62 | 1597 |
| 2024-09-20 22:21:42.110 | MS1 | 121.4656703379 | 31.1446212778 | 623 | 504990 | -89.32 | 10.48 | 584.06 | 0.14 | 2.38 | 1570 |

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
| 3243612 | 4 | 121.4754315096 | 31.1531901530 | 62 | 11 | 1 | 43.0 | TDD | 775 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3261234 | 3 | 121.4670969846 | 31.1553051937 | 194 | 3 | 12 | 48.2 | TDD | 623 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3269349 | 1 | 121.4656737961 | 31.1498646930 | 6 | 6 | 3 | 15.5 | TDD | 376 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3276707 | 2 | 121.4733932860 | 31.1523939103 | 294 | 13 | 12 | 39.8 | TDD | 865 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |

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
| 2024-09-20 22:21:30.907 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.927 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.032 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.032 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.720 | NREventA3 | measId:2;ServCellPCI:467;Se... |
| 2024-09-20 22:21:37.960 | NRHandoverAttempt | SourcePCI:467;SourceNR-ARFC... |
| 2024-09-20 22:21:37.995 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.009 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.136 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.136 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3269349 | 1 | 8.5446 | 9.4023 | -116.9231 | 11.8899 | 197.4949 | 0.0108 | 0.0015 |
| 2024_09_20 22:00 | 3276707 | 2 | 15.3889 | 7.9734 | -116.3403 | 6.6529 | 160.3162 | 0.0117 | 0.0170 |
| 2024_09_20 22:00 | 3261234 | 3 | 89.7548 | 90.7535 | -114.1036 | 16.2309 | 85.5949 | 0.0064 | 0.0011 |
| 2024_09_20 22:00 | 3243612 | 4 | 14.9686 | 7.5812 | -114.6692 | 6.3683 | 83.3850 | 0.0047 | 0.0022 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415219_B1A793DA | 504990 | 623 | -89.5 | 504990 | 865 | -94.5 | 504990 | 376 | -101.0 | 504990 | 775 |
| MR_1774415219_CA380EE4 | 504990 | 623 | -89.0 | 504990 | 865 | -95.4 | 504990 | 376 | -101.4 | 504990 | 775 |
| MR_1774415219_C13E0B01 | 504990 | 623 | -88.1 | 504990 | 865 | -94.9 | 504990 | 376 | -101.9 | 504990 | 775 |
| MR_1774415219_12A93E36 | 504990 | 623 | -89.8 | 504990 | 865 | -92.4 | 504990 | 376 | -100.8 | 504990 | 775 |
| MR_1774415219_7A99DBB5 | 504990 | 623 | -91.4 | 504990 | 865 | -92.8 | 504990 | 376 | -101.3 | 504990 | 775 |

> *... 2개 열 생략 (전체 14열)*

---
