# Track A 문제 분석 — train[1460]~train[1469]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[1460] ~ train[1469] (10개)

## 목차

1. [문제 1460: `f82ce400-927...`](#1460) — single-answer, 정답: C13
2. [문제 1461: `30167031-159...`](#1461) — single-answer, 정답: C15
3. [문제 1462: `2909f32a-842...`](#1462) — multiple-answer, 정답: C4|C19
4. [문제 1463: `d10fbc5b-c91...`](#1463) — multiple-answer, 정답: C2|C14
5. [문제 1464: `1598dd9b-12b...`](#1464) — single-answer, 정답: C8
6. [문제 1465: `781f9e9c-2af...`](#1465) — single-answer, 정답: C14
7. [문제 1466: `bd9518bd-eab...`](#1466) — single-answer, 정답: C1
8. [문제 1467: `8d7a5ca6-1cd...`](#1467) — single-answer, 정답: C15
9. [문제 1468: `b5af089a-16f...`](#1468) — multiple-answer, 정답: C11|C13
10. [문제 1469: `b4497b07-ff5...`](#1469) — single-answer, 정답: C5

---

### 문제 1460: `f82ce400-927...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `f82ce400-9278-4db4-845a-79cd32177bf4` |
| Tag | **single-answer** |
| 정답 | **C13** |
| C13 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3220478_4 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1460] topology](images/train_1460.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3220478_4
- `C2`: Decrease transmission power for 3242654_5
- `C3`: Add neighbor relationship between 3221049_8 and 3242654_5
- `C4`: Lift the tilt angle  of 3242654_5 by 2 degrees
- `C5`: Increase A3 Offset threshold for 3220478_4
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3242654_5
- `C7`: Add neighbor relationship between 3220478_4 and 3242654_5
- `C8`: Decrease A3 Offset threshold for 3242654_5
- `C9`: Adjust the azimuth of 3242654_5 by 23 degrees
- `C10`: Press down the tilt angle  of 3242654_5 by 2 degrees
- `C11`: Check test server and transmission issues
- `C12`: Decrease transmission power for 3220478_4
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3220478_4 **← 정답**
- `C14`: Press down the tilt angle of 3220478_4 by 4 degrees
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3242654_5
- `C16`: Lift the tilt angle of 3220478_4 by 4 degrees
- `C17`: Insufficient data; more data is needed for judgment.
- `C18`: Increase A3 Offset threshold for 3242654_5
- `C19`: Adjust the azimuth of 3220478_4 by 10 degrees
- `C20`: Decrease A3 Offset threshold for 3220478_4
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3220478_4
- `C22`: Increase transmission power for 3242654_5

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.953 | MS1 | 121.4656739774 | 31.1446328331 | 783 | 504990 | -94.88 | 13.08 | 455.56 | 0.01 | 2.41 | 1567 |
| 2024-09-20 22:21:32.979 | MS1 | 121.4656663196 | 31.1446261589 | 388 | 504990 | -93.34 | 14.46 | 445.25 | 0.11 | 2.47 | 1573 |
| 2024-09-20 22:21:33.705 | MS1 | 121.4656726721 | 31.1446341921 | 671 | 504990 | -95.64 | 11.55 | 551.04 | 0.00 | 2.53 | 1590 |
| 2024-09-20 22:21:34.324 | MS1 | 121.4656774097 | 31.1446296196 | 531 | 152650 | -90.11 | 6.50 | 77.85 | 0.08 | 1.51 | 923 |
| 2024-09-20 22:21:35.692 | MS1 | 121.4656714022 | 31.1446330303 | 52 | 152650 | -94.84 | 7.36 | 78.41 | 0.00 | 1.92 | 905 |
| 2024-09-20 22:21:36.731 | MS1 | 121.4656752852 | 31.1446303762 | 530 | 152650 | -93.11 | 6.99 | 54.02 | 0.20 | 1.98 | 987 |
| 2024-09-20 22:21:37.398 | MS1 | 121.4656722829 | 31.1446259026 | 499 | 152650 | -93.44 | 7.74 | 72.15 | 0.05 | 1.60 | 907 |
| 2024-09-20 22:21:38.679 | MS1 | 121.4656628919 | 31.1446353602 | 531 | 152650 | -96.74 | 2.34 | 56.49 | 0.12 | 1.67 | 957 |
| 2024-09-20 22:21:39.440 | MS1 | 121.4656770797 | 31.1446338050 | 52 | 152650 | -88.65 | 4.25 | 56.71 | 0.19 | 1.51 | 945 |
| 2024-09-20 22:21:40.818 | MS1 | 121.4656662790 | 31.1446294581 | 530 | 152650 | -91.42 | 2.27 | 64.62 | 0.12 | 2.54 | 1560 |
| 2024-09-20 22:21:41.341 | MS1 | 121.4656772465 | 31.1446378347 | 499 | 152650 | -89.85 | 3.11 | 70.38 | 0.13 | 2.84 | 1577 |
| 2024-09-20 22:21:42.971 | MS1 | 121.4656696762 | 31.1446361852 | 531 | 152650 | -92.90 | 4.17 | 69.71 | 0.01 | 2.82 | 1570 |

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
| 3218348 | 11 | 121.4725769095 | 31.1544223030 | 230 | 3 | 1 | 25.8 | FDD | 499 | n1 | 152650 | 30M | 4T4R | 11 | 152650 |
| 3220478 | 4 | 121.4674880414 | 31.1483174213 | 213 | 2 | 3 | 13.0 | TDD | 783 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3220755 | 1 | 121.4709365013 | 31.1554333627 | 15 | 7 | 12 | 23.7 | TDD | 640 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3221049 | 8 | 121.4724559064 | 31.1529446101 | 113 | 4 | 4 | 17.9 | FDD | 530 | n1 | 152650 | 30M | 4T4R | 27 | 152650 |
| 3226153 | 6 | 121.4671185205 | 31.1537085937 | 130 | 10 | 9 | 28.5 | TDD | 671 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3229909 | 7 | 121.4737903713 | 31.1514394479 | 319 | 14 | 1 | 5.8 | FDD | 486 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |
| 3230054 | 2 | 121.4688605757 | 31.1487363554 | 277 | 3 | 10 | 20.0 | TDD | 738 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3236344 | 3 | 121.4701540127 | 31.1460251518 | 288 | 8 | 2 | 17.9 | TDD | 388 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3242654 | 5 | 121.4669074361 | 31.1474866754 | 223 | 1 | 4 | 3.0 | TDD | 245 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3244433 | 10 | 121.4695885140 | 31.1491484646 | 248 | 2 | 10 | 7.2 | FDD | 52 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |
| 3250872 | 12 | 121.4672948966 | 31.1483505220 | 102 | 6 | 9 | 5.4 | FDD | 596 | n1 | 152650 | 30M | 4T4R | 10 | 152650 |
| 3253252 | 13 | 121.4735037995 | 31.1467032392 | 238 | 7 | 4 | 0.8 | FDD | 664 | n1 | 152650 | 30M | 4T4R | 18 | 152650 |
| 3272785 | 9 | 121.4665984097 | 31.1559830006 | 340 | 1 | 1 | 2.9 | FDD | 531 | n1 | 152650 | 30M | 4T4R | 24 | 152650 |

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
| 2024-09-20 22:21:31.104 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.122 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.259 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.259 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.942 | NREventA2 | measId:1;ServCellPCI:355;Se... |
| 2024-09-20 22:21:35.081 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.359 | NREventA5 | measId:3;ServCellPCI:355;Se... |
| 2024-09-20 22:21:35.398 | NRHandoverAttempt | SourcePCI:355;SourceNR-ARFC... |
| 2024-09-20 22:21:35.426 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.437 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:35.566 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.566 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3220755 | 1 | 17.4340 | 18.3313 | -115.7805 | 5.5198 | 111.6796 | 0.0020 | 0.0092 |
| 2024_09_20 22:00 | 3230054 | 2 | 6.4847 | 11.8709 | -115.4311 | 12.2418 | 117.5080 | 0.0113 | 0.0034 |
| 2024_09_20 22:00 | 3236344 | 3 | 16.7245 | 12.7726 | -114.6696 | 11.9361 | 103.1048 | 0.0055 | 0.0105 |
| 2024_09_20 22:00 | 3220478 | 4 | 8.8258 | 5.2222 | -117.5372 | 5.0510 | 164.9694 | 0.0093 | 0.0072 |
| 2024_09_20 22:00 | 3242654 | 5 | 10.0413 | 12.0345 | -115.4167 | 15.3586 | 111.0476 | 0.0090 | 0.0181 |
| 2024_09_20 22:00 | 3226153 | 6 | 8.3854 | 16.6147 | -116.6442 | 12.0653 | 148.0191 | 0.0032 | 0.0052 |
| 2024_09_20 22:00 | 3229909 | 7 | 10.0195 | 6.4268 | -116.8977 | 4.6021 | 48.7963 | 0.0042 | 0.0051 |
| 2024_09_20 22:00 | 3221049 | 8 | 15.1008 | 6.4353 | -116.6575 | 3.0466 | 53.4092 | 0.0104 | 0.0063 |
| 2024_09_20 22:00 | 3272785 | 9 | 7.7800 | 8.5450 | -117.7263 | 3.0751 | 35.5050 | 0.0014 | 0.0015 |
| 2024_09_20 22:00 | 3244433 | 10 | 16.6293 | 14.2679 | -117.4680 | 4.2623 | 56.9045 | 0.0001 | 0.0162 |
| 2024_09_20 22:00 | 3218348 | 11 | 9.6426 | 10.6346 | -114.8918 | 3.6184 | 40.4971 | 0.0080 | 0.0052 |
| 2024_09_20 22:00 | 3250872 | 12 | 19.3447 | 16.6206 | -114.6414 | 4.4760 | 25.6964 | 0.0151 | 0.0080 |
| 2024_09_20 22:00 | 3253252 | 13 | 12.3801 | 6.3401 | -117.5948 | 3.8369 | 45.3620 | 0.0035 | 0.0101 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774411998_D8C78CAE | 152650 | 531 | -90.9 | 152650 | 664 | -97.0 | 152650 | 486 | -102.9 | 152650 | 596 |
| MR_1774411998_EA7FA0F0 | 504990 | 671 | -96.6 | 504990 | 245 | -91.6 | 504990 | 738 | -101.4 | 504990 | 640 |
| MR_1774411998_55287892 | 504990 | 671 | -95.9 | 504990 | 245 | -95.3 | 504990 | 738 | -99.9 | 504990 | 640 |
| MR_1774411998_72FC14ED | 504990 | 671 | -96.0 | 504990 | 245 | -93.0 | 504990 | 738 | -100.0 | 504990 | 640 |
| MR_1774411998_1DA239C1 | 504990 | 671 | -97.5 | 504990 | 245 | -92.0 | 504990 | 738 | -101.8 | 504990 | 640 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1461: `30167031-159...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `30167031-159f-4ae3-8d92-4b346a62f67e` |
| Tag | **single-answer** |
| 정답 | **C15** |
| C15 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3236602_1 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1461] topology](images/train_1461.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Check test server and transmission issues
- `C2`: Increase A3 Offset threshold for 3212831_2
- `C3`: Increase A3 Offset threshold for 3236602_1
- `C4`: Add neighbor relationship between 3277130_7 and 3212831_2
- `C5`: Add neighbor relationship between 3236602_1 and 3212831_2
- `C6`: Press down the tilt angle of 3236602_1 by 1 degrees
- `C7`: Lift the tilt angle  of 3212831_2 by 3 degrees
- `C8`: Decrease transmission power for 3236602_1
- `C9`: Insufficient data; more data is needed for judgment.
- `C10`: Adjust the azimuth of 3212831_2 by 16 degrees
- `C11`: Decrease transmission power for 3212831_2
- `C12`: Lift the tilt angle of 3236602_1 by 1 degrees
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3212831_2
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3212831_2
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3236602_1 **← 정답**
- `C16`: Adjust the azimuth of 3236602_1 by 31 degrees
- `C17`: Press down the tilt angle  of 3212831_2 by 3 degrees
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3236602_1
- `C19`: Decrease A3 Offset threshold for 3212831_2
- `C20`: Decrease A3 Offset threshold for 3236602_1
- `C21`: Increase transmission power for 3236602_1
- `C22`: Increase transmission power for 3212831_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.863 | MS1 | 121.4656627104 | 31.1446269568 | 386 | 504990 | -94.80 | 9.60 | 342.59 | 0.15 | 2.54 | 1567 |
| 2024-09-20 22:21:32.402 | MS1 | 121.4656711499 | 31.1446247284 | 637 | 504990 | -95.73 | 12.76 | 565.16 | 0.18 | 2.83 | 1581 |
| 2024-09-20 22:21:33.228 | MS1 | 121.4656596917 | 31.1446345488 | 469 | 504990 | -94.74 | 9.45 | 457.13 | 0.09 | 2.15 | 1592 |
| 2024-09-20 22:21:34.513 | MS1 | 121.4656640911 | 31.1446191415 | 846 | 152650 | -92.91 | 5.91 | 74.05 | 0.17 | 1.75 | 936 |
| 2024-09-20 22:21:35.396 | MS1 | 121.4656747599 | 31.1446262215 | 90 | 152650 | -89.23 | 5.20 | 72.08 | 0.16 | 1.57 | 907 |
| 2024-09-20 22:21:36.809 | MS1 | 121.4656723042 | 31.1446235415 | 554 | 152650 | -89.25 | 2.08 | 85.05 | 0.04 | 1.51 | 989 |
| 2024-09-20 22:21:37.646 | MS1 | 121.4656665860 | 31.1446331529 | 249 | 152650 | -88.55 | 6.07 | 66.00 | 0.12 | 1.74 | 927 |
| 2024-09-20 22:21:38.250 | MS1 | 121.4656732977 | 31.1446236661 | 846 | 152650 | -90.09 | 3.05 | 92.62 | 0.02 | 1.59 | 922 |
| 2024-09-20 22:21:39.227 | MS1 | 121.4656698906 | 31.1446316263 | 90 | 152650 | -92.02 | 2.06 | 89.87 | 0.16 | 1.76 | 989 |
| 2024-09-20 22:21:40.236 | MS1 | 121.4656718120 | 31.1446183458 | 554 | 152650 | -95.59 | 7.96 | 50.99 | 0.12 | 2.83 | 1576 |
| 2024-09-20 22:21:41.529 | MS1 | 121.4656755676 | 31.1446303345 | 249 | 152650 | -89.48 | 7.84 | 82.07 | 0.18 | 2.44 | 1590 |
| 2024-09-20 22:21:42.497 | MS1 | 121.4656640700 | 31.1446285846 | 846 | 152650 | -88.60 | 5.66 | 61.93 | 0.17 | 2.57 | 1571 |

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
| 3212831 | 2 | 121.4736778011 | 31.1459011795 | 275 | 3 | 4 | 5.6 | TDD | 12 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3222394 | 13 | 121.4737735497 | 31.1549013188 | 165 | 11 | 12 | 10.7 | FDD | 90 | n1 | 152650 | 30M | 4T4R | 18 | 152650 |
| 3230208 | 4 | 121.4749681050 | 31.1446823428 | 19 | 5 | 8 | 24.2 | TDD | 469 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3233083 | 5 | 121.4688810304 | 31.1510745699 | 51 | 11 | 10 | 20.9 | TDD | 792 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3236602 | 1 | 121.4709749440 | 31.1480463609 | 202 | 0 | 9 | 14.3 | TDD | 386 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3246333 | 8 | 121.4730395428 | 31.1559338837 | 131 | 7 | 6 | 4.8 | FDD | 939 | n1 | 152650 | 30M | 4T4R | 17 | 152650 |
| 3248493 | 12 | 121.4725736648 | 31.1467726393 | 161 | 1 | 12 | 11.8 | FDD | 249 | n1 | 152650 | 30M | 4T4R | 13 | 152650 |
| 3256074 | 3 | 121.4655506552 | 31.1503506442 | 202 | 13 | 10 | 10.4 | TDD | 52 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3269987 | 11 | 121.4655359237 | 31.1505659656 | 257 | 10 | 2 | 25.7 | FDD | 276 | n1 | 152650 | 30M | 4T4R | 28 | 152650 |
| 3270379 | 10 | 121.4658983828 | 31.1540498390 | 321 | 12 | 5 | 7.2 | FDD | 302 | n1 | 152650 | 30M | 4T4R | 22 | 152650 |
| 3273673 | 9 | 121.4692027035 | 31.1472407191 | 254 | 12 | 0 | 5.9 | FDD | 846 | n1 | 152650 | 30M | 4T4R | 17 | 152650 |
| 3277130 | 7 | 121.4738829817 | 31.1463188751 | 243 | 3 | 0 | 2.2 | FDD | 554 | n1 | 152650 | 30M | 4T4R | 25 | 152650 |
| 3278193 | 6 | 121.4725401199 | 31.1465153098 | 112 | 5 | 9 | 1.6 | TDD | 637 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |

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
| 2024-09-20 22:21:31.147 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.172 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.299 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.299 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.045 | NREventA2 | measId:1;ServCellPCI:316;Se... |
| 2024-09-20 22:21:35.147 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.385 | NREventA5 | measId:3;ServCellPCI:316;Se... |
| 2024-09-20 22:21:35.437 | NRHandoverAttempt | SourcePCI:316;SourceNR-ARFC... |
| 2024-09-20 22:21:35.459 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.470 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:35.615 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.615 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3236602 | 1 | 17.8790 | 7.3273 | -115.9262 | 12.0423 | 159.7374 | 0.0026 | 0.0198 |
| 2024_09_20 22:00 | 3212831 | 2 | 18.4085 | 15.2668 | -116.0810 | 19.7861 | 169.1606 | 0.0184 | 0.0175 |
| 2024_09_20 22:00 | 3256074 | 3 | 7.1951 | 7.3506 | -115.8835 | 10.1148 | 164.2037 | 0.0171 | 0.0180 |
| 2024_09_20 22:00 | 3230208 | 4 | 5.2944 | 15.1981 | -115.9830 | 13.6406 | 168.7792 | 0.0181 | 0.0166 |
| 2024_09_20 22:00 | 3233083 | 5 | 5.4257 | 5.7542 | -116.7087 | 16.5099 | 92.1574 | 0.0114 | 0.0010 |
| 2024_09_20 22:00 | 3278193 | 6 | 18.8705 | 12.1219 | -115.0070 | 9.5976 | 174.7855 | 0.0035 | 0.0116 |
| 2024_09_20 22:00 | 3277130 | 7 | 5.1960 | 9.9989 | -116.4549 | 4.7904 | 42.0943 | 0.0133 | 0.0179 |
| 2024_09_20 22:00 | 3246333 | 8 | 6.2693 | 10.6239 | -116.5883 | 4.1882 | 38.6553 | 0.0125 | 0.0149 |
| 2024_09_20 22:00 | 3273673 | 9 | 15.2011 | 8.5962 | -116.6085 | 3.2357 | 31.3885 | 0.0198 | 0.0113 |
| 2024_09_20 22:00 | 3270379 | 10 | 19.9697 | 19.9779 | -116.9269 | 4.2484 | 48.8996 | 0.0022 | 0.0183 |
| 2024_09_20 22:00 | 3269987 | 11 | 12.4856 | 11.5382 | -117.7832 | 3.0692 | 38.8846 | 0.0117 | 0.0037 |
| 2024_09_20 22:00 | 3248493 | 12 | 5.2361 | 13.4256 | -116.6871 | 3.3753 | 33.5685 | 0.0092 | 0.0032 |
| 2024_09_20 22:00 | 3222394 | 13 | 11.3949 | 12.2230 | -115.1188 | 3.3692 | 48.3410 | 0.0089 | 0.0008 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412008_CF497D38 | 152650 | 846 | -92.0 | 152650 | 276 | -96.0 | 152650 | 939 | -103.1 | 152650 | 302 |
| MR_1774412008_CCF252AE | 504990 | 469 | -94.7 | 504990 | 12 | -92.6 | 504990 | 52 | -101.2 | 504990 | 792 |
| MR_1774412008_F49DEB4D | 504990 | 469 | -95.6 | 504990 | 12 | -91.8 | 504990 | 52 | -101.3 | 504990 | 792 |
| MR_1774412008_5764E9C9 | 152650 | 846 | -92.9 | 152650 | 276 | -94.3 | 152650 | 939 | -102.6 | 152650 | 302 |
| MR_1774412008_A2E21818 | 152650 | 846 | -94.6 | 152650 | 276 | -94.4 | 152650 | 939 | -102.5 | 152650 | 302 |
| MR_1774412008_3197FF59 | 504990 | 469 | -95.9 | 504990 | 12 | -94.1 | 504990 | 52 | -100.8 | 504990 | 792 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1462: `2909f32a-842...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `2909f32a-8426-42c5-9d99-7f9386a2f0de` |
| Tag | **multiple-answer** |
| 정답 | **C4|C19** |
| C4 의미 | Decrease transmission power for 3279766_1 |
| C19 의미 | Press down the tilt angle  of 3279766_1 by 4 degrees |
| 패턴 분류 | **P3 Overshoot (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1462] topology](images/train_1462.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3279766_1
- `C2`: Adjust the azimuth of 3255383_4 by 44 degrees
- `C3`: Decrease A3 Offset threshold for 3279766_1
- `C4`: Decrease transmission power for 3279766_1 **← 정답**
- `C5`: Adjust the azimuth of 3279766_1 by 21 degrees
- `C6`: Decrease A3 Offset threshold for 3255383_4
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3279766_1
- `C8`: Increase transmission power for 3279766_1
- `C9`: Add neighbor relationship between 3255383_4 and 3279766_1
- `C10`: Increase A3 Offset threshold for 3255383_4
- `C11`: Decrease transmission power for 3255383_4
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3255383_4
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3255383_4
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3279766_1
- `C15`: Add neighbor relationship between 3219171_3 and 3279766_1
- `C16`: Lift the tilt angle of 3255383_4 by 6 degrees
- `C17`: Check test server and transmission issues
- `C18`: Press down the tilt angle of 3255383_4 by 6 degrees
- `C19`: Press down the tilt angle  of 3279766_1 by 4 degrees **← 정답**
- `C20`: Increase transmission power for 3255383_4
- `C21`: Insufficient data; more data is needed for judgment.
- `C22`: Lift the tilt angle  of 3279766_1 by 4 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.990 | MS1 | 121.4656761275 | 31.1446267910 | 703 | 504990 | -76.18 | 15.54 | 356.27 | 0.15 | 2.64 | 1564 |
| 2024-09-20 22:21:32.245 | MS1 | 121.4656648644 | 31.1446360959 | 703 | 504990 | -77.74 | 15.84 | 372.79 | 0.14 | 2.85 | 1586 |
| 2024-09-20 22:21:33.625 | MS1 | 121.4656639997 | 31.1446338930 | 703 | 504990 | -81.51 | 15.26 | 358.46 | 0.10 | 2.10 | 1580 |
| 2024-09-20 22:21:34.365 | MS1 | 121.4656711644 | 31.1446219595 | 703 | 504990 | -88.74 | 0.25 | 62.48 | 0.19 | 1.45 | 1570 |
| 2024-09-20 22:21:35.767 | MS1 | 121.4656639485 | 31.1446342375 | 703 | 504990 | -85.35 | 2.04 | 55.64 | 0.15 | 1.17 | 1598 |
| 2024-09-20 22:21:36.240 | MS1 | 121.4656656905 | 31.1446361185 | 703 | 504990 | -91.50 | 1.53 | 64.35 | 0.14 | 1.22 | 1566 |
| 2024-09-20 22:21:37.321 | MS1 | 121.4656726816 | 31.1446302561 | 703 | 504990 | -90.86 | 0.18 | 90.05 | 0.17 | 1.13 | 1598 |
| 2024-09-20 22:21:38.378 | MS1 | 121.4656696814 | 31.1446329595 | 703 | 504990 | -85.55 | 0.40 | 63.90 | 0.04 | 1.47 | 1569 |
| 2024-09-20 22:21:39.847 | MS1 | 121.4656755705 | 31.1446254131 | 703 | 504990 | -87.64 | 3.58 | 44.12 | 0.07 | 1.37 | 1573 |
| 2024-09-20 22:21:40.127 | MS1 | 121.4656646347 | 31.1446271576 | 703 | 504990 | -78.29 | 12.20 | 468.84 | 0.01 | 2.90 | 1566 |
| 2024-09-20 22:21:41.451 | MS1 | 121.4656624514 | 31.1446183435 | 703 | 504990 | -76.57 | 17.61 | 354.04 | 0.01 | 2.34 | 1597 |
| 2024-09-20 22:21:42.764 | MS1 | 121.4656744335 | 31.1446376986 | 703 | 504990 | -83.91 | 12.75 | 355.46 | 0.13 | 2.49 | 1578 |

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
| 3219171 | 3 | 121.4713058485 | 31.1456552384 | 225 | 15 | 12 | 46.6 | TDD | 309 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3235845 | 2 | 121.4737449767 | 31.1526554789 | 198 | 10 | 2 | 20.3 | TDD | 451 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3255383 | 4 | 121.4666011017 | 31.1534122478 | 229 | 3 | 0 | 45.8 | TDD | 703 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3279766 | 1 | 121.4681805649 | 31.1544233438 | 171 | 2 | 4 | 46.0 | TDD | 361 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |

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
| 2024-09-20 22:21:31.070 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.093 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.217 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.217 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3279766 | 1 | 15.4467 | 7.0607 | -116.8886 | 19.9296 | 114.2674 | 0.0108 | 0.0052 |
| 2024_09_20 22:00 | 3235845 | 2 | 19.8813 | 12.6293 | -114.5787 | 7.0786 | 173.9140 | 0.0173 | 0.0173 |
| 2024_09_20 22:00 | 3219171 | 3 | 12.6659 | 6.5103 | -115.7075 | 19.8986 | 137.7835 | 0.0046 | 0.0104 |
| 2024_09_20 22:00 | 3255383 | 4 | 8.4761 | 9.1811 | -108.6621 | 12.1697 | 116.7078 | 0.0073 | 0.0032 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414236_13A0CB0F | 504990 | 703 | -90.7 | 504990 | 361 | -91.7 | 504990 | 309 | -89.5 | 504990 | 451 |
| MR_1774414236_AF3FC337 | 504990 | 361 | -87.3 | 504990 | 703 | -89.8 | 504990 | 309 | -92.5 | 504990 | 451 |
| MR_1774414236_803A4B82 | 504990 | 703 | -89.9 | 504990 | 361 | -91.9 | 504990 | 309 | -91.9 | 504990 | 451 |
| MR_1774414236_65EE81C1 | 504990 | 703 | -89.0 | 504990 | 361 | -92.0 | 504990 | 309 | -92.2 | 504990 | 451 |
| MR_1774414236_B51E8901 | 504990 | 361 | -87.8 | 504990 | 703 | -92.0 | 504990 | 309 | -92.2 | 504990 | 451 |
| MR_1774414236_74C5C671 | 504990 | 703 | -90.6 | 504990 | 361 | -88.7 | 504990 | 309 | -92.0 | 504990 | 451 |
| MR_1774414236_ACFE8575 | 504990 | 361 | -89.1 | 504990 | 703 | -90.0 | 504990 | 309 | -91.5 | 504990 | 451 |
| MR_1774414236_6444716F | 504990 | 703 | -90.3 | 504990 | 361 | -88.7 | 504990 | 309 | -92.0 | 504990 | 451 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1463: `d10fbc5b-c91...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `d10fbc5b-c91c-48f0-95fa-cee4f71cf5f8` |
| Tag | **multiple-answer** |
| 정답 | **C2|C14** |
| C2 의미 | Adjust the azimuth of 3235685_2 by 50 degrees |
| C14 의미 | Increase transmission power for 3235685_2 |
| 패턴 분류 | **P4 Coverage (azimuth)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1463] topology](images/train_1463.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3235685_2
- `C2`: Adjust the azimuth of 3235685_2 by 50 degrees **← 정답**
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3234454_4
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3235685_2
- `C5`: Increase A3 Offset threshold for 3235685_2
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3234454_4
- `C7`: Decrease A3 Offset threshold for 3235685_2
- `C8`: Adjust the azimuth of 3234454_4 by 21 degrees
- `C9`: Decrease A3 Offset threshold for 3234454_4
- `C10`: Add neighbor relationship between 3235685_2 and 3234454_4
- `C11`: Increase A3 Offset threshold for 3234454_4
- `C12`: Insufficient data; more data is needed for judgment.
- `C13`: Add neighbor relationship between 3261223_1 and 3234454_4
- `C14`: Increase transmission power for 3235685_2 **← 정답**
- `C15`: Decrease transmission power for 3234454_4
- `C16`: Press down the tilt angle of 3235685_2 by 10 degrees
- `C17`: Decrease transmission power for 3235685_2
- `C18`: Check test server and transmission issues
- `C19`: Press down the tilt angle  of 3234454_4 by 4 degrees
- `C20`: Lift the tilt angle  of 3234454_4 by 4 degrees
- `C21`: Increase transmission power for 3234454_4
- `C22`: Lift the tilt angle of 3235685_2 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.763 | MS1 | 121.4656738070 | 31.1446343891 | 986 | 504990 | -88.59 | 14.44 | 423.27 | 0.17 | 2.21 | 1600 |
| 2024-09-20 22:21:32.762 | MS1 | 121.4656689470 | 31.1446316889 | 986 | 504990 | -87.07 | 16.97 | 464.96 | 0.09 | 2.52 | 1589 |
| 2024-09-20 22:21:33.939 | MS1 | 121.4656601904 | 31.1446354516 | 986 | 504990 | -86.00 | 17.99 | 368.89 | 0.05 | 2.56 | 1572 |
| 2024-09-20 22:21:34.835 | MS1 | 121.4656589253 | 31.1446337111 | 986 | 504990 | -104.89 | 0.72 | 66.39 | 0.14 | 1.42 | 1571 |
| 2024-09-20 22:21:35.663 | MS1 | 121.4656607609 | 31.1446315672 | 986 | 504990 | -109.21 | -1.67 | 86.07 | 0.20 | 1.39 | 1595 |
| 2024-09-20 22:21:36.608 | MS1 | 121.4656756316 | 31.1446220842 | 986 | 504990 | -109.45 | 1.63 | 75.72 | 0.17 | 1.18 | 1598 |
| 2024-09-20 22:21:37.226 | MS1 | 121.4656768291 | 31.1446257858 | 986 | 504990 | -105.49 | -0.26 | 33.63 | 0.00 | 1.17 | 1569 |
| 2024-09-20 22:21:38.252 | MS1 | 121.4656683019 | 31.1446297803 | 986 | 504990 | -107.32 | 1.26 | 11.62 | 0.17 | 1.49 | 1571 |
| 2024-09-20 22:21:39.437 | MS1 | 121.4656763773 | 31.1446367687 | 986 | 504990 | -103.98 | 0.94 | 51.63 | 0.09 | 1.21 | 1579 |
| 2024-09-20 22:21:40.832 | MS1 | 121.4656608000 | 31.1446302068 | 986 | 504990 | -91.03 | 17.32 | 332.18 | 0.15 | 2.98 | 1592 |
| 2024-09-20 22:21:41.379 | MS1 | 121.4656709301 | 31.1446343443 | 986 | 504990 | -94.04 | 13.29 | 535.06 | 0.08 | 2.73 | 1570 |
| 2024-09-20 22:21:42.431 | MS1 | 121.4656745572 | 31.1446334848 | 986 | 504990 | -94.17 | 17.60 | 333.77 | 0.09 | 2.15 | 1573 |

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
| 3234454 | 4 | 121.4668281835 | 31.1503401110 | 169 | 1 | 7 | 39.4 | TDD | 541 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3235685 | 2 | 121.4746225498 | 31.1490370661 | 293 | 12 | 4 | 43.3 | TDD | 986 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3261223 | 1 | 121.4712720653 | 31.1523270932 | 195 | 1 | 6 | 46.4 | TDD | 896 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3263463 | 3 | 121.4677501116 | 31.1558325587 | 239 | 14 | 1 | 39.3 | TDD | 58 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |

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
| 2024-09-20 22:21:31.295 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.317 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.446 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.446 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.664 | NREventA2 | measId:1;ServCellPCI:7;Serv... |
| 2024-09-20 22:21:34.802 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3261223 | 1 | 19.3344 | 6.6226 | -115.3371 | 16.1247 | 162.5010 | 0.0078 | 0.0163 |
| 2024_09_20 22:00 | 3235685 | 2 | 8.1809 | 19.2538 | -116.7712 | 14.7965 | 106.4019 | 0.1441 | 0.0142 |
| 2024_09_20 22:00 | 3263463 | 3 | 9.8331 | 7.4671 | -117.1228 | 13.9039 | 149.6433 | 0.0015 | 0.0136 |
| 2024_09_20 22:00 | 3234454 | 4 | 14.8198 | 7.0858 | -117.1515 | 16.5469 | 112.7340 | 0.0163 | 0.0125 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412782_05C67732 | 504990 | 986 | -106.1 | 504990 | 541 | -110.6 | 504990 | 896 | -117.9 | 504990 | 58 |
| MR_1774412782_DD5A3F9F | 504990 | 986 | -106.5 | 504990 | 541 | -112.6 | 504990 | 896 | -119.0 | 504990 | 58 |
| MR_1774412782_D347DBDE | 504990 | 986 | -104.9 | 504990 | 541 | -113.9 | 504990 | 896 | -119.0 | 504990 | 58 |
| MR_1774412782_6C80A4DC | 504990 | 986 | -104.2 | 504990 | 541 | -112.0 | 504990 | 896 | -118.9 | 504990 | 58 |
| MR_1774412782_EB8884D0 | 504990 | 986 | -105.6 | 504990 | 541 | -113.3 | 504990 | 896 | -119.7 | 504990 | 58 |
| MR_1774412782_5E542F70 | 504990 | 986 | -105.7 | 504990 | 541 | -112.6 | 504990 | 896 | -117.0 | 504990 | 58 |
| MR_1774412782_0235C07D | 504990 | 986 | -104.9 | 504990 | 541 | -112.7 | 504990 | 896 | -120.1 | 504990 | 58 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1464: `1598dd9b-12b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `1598dd9b-12b7-49fa-92ab-612b9d887c40` |
| Tag | **single-answer** |
| 정답 | **C8** |
| C8 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3242527_6 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1464] topology](images/train_1464.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3242527_6
- `C2`: Increase A3 Offset threshold for 3242527_6
- `C3`: Insufficient data; more data is needed for judgment.
- `C4`: Decrease A3 Offset threshold for 3242527_6
- `C5`: Check test server and transmission issues
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3238163_1
- `C7`: Decrease transmission power for 3238163_1
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3242527_6 **← 정답**
- `C9`: Increase transmission power for 3238163_1
- `C10`: Press down the tilt angle  of 3238163_1 by 2 degrees
- `C11`: Lift the tilt angle of 3242527_6 by 4 degrees
- `C12`: Adjust the azimuth of 3238163_1 by 47 degrees
- `C13`: Add neighbor relationship between 3242527_6 and 3238163_1
- `C14`: Lift the tilt angle  of 3238163_1 by 2 degrees
- `C15`: Increase A3 Offset threshold for 3238163_1
- `C16`: Decrease A3 Offset threshold for 3238163_1
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3238163_1
- `C18`: Press down the tilt angle of 3242527_6 by 4 degrees
- `C19`: Adjust the azimuth of 3242527_6 by 25 degrees
- `C20`: Increase transmission power for 3242527_6
- `C21`: Add neighbor relationship between 3222279_11 and 3238163_1
- `C22`: Decrease transmission power for 3242527_6

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.813 | MS1 | 121.4656770628 | 31.1446293272 | 951 | 504990 | -93.54 | 11.57 | 577.20 | 0.01 | 2.62 | 1582 |
| 2024-09-20 22:21:32.543 | MS1 | 121.4656612717 | 31.1446228417 | 835 | 504990 | -93.41 | 11.46 | 330.60 | 0.05 | 2.75 | 1587 |
| 2024-09-20 22:21:33.780 | MS1 | 121.4656755957 | 31.1446379982 | 404 | 504990 | -94.98 | 13.59 | 373.51 | 0.19 | 2.24 | 1596 |
| 2024-09-20 22:21:34.809 | MS1 | 121.4656612094 | 31.1446202552 | 4 | 152650 | -91.63 | 2.83 | 64.79 | 0.05 | 1.97 | 957 |
| 2024-09-20 22:21:35.223 | MS1 | 121.4656672469 | 31.1446360247 | 668 | 152650 | -90.15 | 5.85 | 97.03 | 0.13 | 1.52 | 983 |
| 2024-09-20 22:21:36.674 | MS1 | 121.4656592672 | 31.1446191895 | 817 | 152650 | -87.08 | 3.76 | 61.35 | 0.14 | 1.65 | 904 |
| 2024-09-20 22:21:37.101 | MS1 | 121.4656695430 | 31.1446279049 | 502 | 152650 | -88.43 | 2.40 | 53.49 | 0.11 | 1.61 | 944 |
| 2024-09-20 22:21:38.190 | MS1 | 121.4656580931 | 31.1446294828 | 4 | 152650 | -96.54 | 7.18 | 81.69 | 0.09 | 1.68 | 991 |
| 2024-09-20 22:21:39.238 | MS1 | 121.4656644871 | 31.1446325913 | 668 | 152650 | -89.96 | 7.73 | 63.47 | 0.04 | 1.83 | 905 |
| 2024-09-20 22:21:40.222 | MS1 | 121.4656616238 | 31.1446238482 | 817 | 152650 | -92.42 | 5.29 | 73.40 | 0.03 | 2.98 | 1574 |
| 2024-09-20 22:21:41.517 | MS1 | 121.4656757838 | 31.1446251752 | 502 | 152650 | -87.85 | 4.98 | 73.71 | 0.00 | 2.28 | 1570 |
| 2024-09-20 22:21:42.395 | MS1 | 121.4656636300 | 31.1446308084 | 4 | 152650 | -95.37 | 3.99 | 51.96 | 0.08 | 2.00 | 1581 |

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
| 3219932 | 2 | 121.4738380653 | 31.1454596418 | 217 | 10 | 10 | 3.7 | TDD | 835 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3222279 | 11 | 121.4711429934 | 31.1508603928 | 322 | 10 | 6 | 5.6 | FDD | 817 | n1 | 152650 | 30M | 4T4R | 27 | 152650 |
| 3222451 | 12 | 121.4651471715 | 31.1488732781 | 249 | 4 | 3 | 11.9 | FDD | 502 | n1 | 152650 | 30M | 4T4R | 22 | 152650 |
| 3232117 | 7 | 121.4753238148 | 31.1539215036 | 99 | 8 | 8 | 4.0 | FDD | 193 | n1 | 152650 | 30M | 4T4R | 24 | 152650 |
| 3232855 | 10 | 121.4734365800 | 31.1468768461 | 206 | 1 | 7 | 1.2 | FDD | 165 | n1 | 152650 | 30M | 4T4R | 26 | 152650 |
| 3233193 | 5 | 121.4644147971 | 31.1493370013 | 124 | 14 | 10 | 23.6 | TDD | 501 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3238163 | 1 | 121.4665891227 | 31.1483582100 | 145 | 0 | 8 | 16.4 | TDD | 736 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3242144 | 8 | 121.4745979725 | 31.1469983623 | 274 | 5 | 3 | 25.9 | FDD | 33 | n1 | 152650 | 30M | 4T4R | 17 | 152650 |
| 3242485 | 9 | 121.4640212665 | 31.1554983339 | 226 | 4 | 4 | 18.0 | FDD | 4 | n1 | 152650 | 30M | 4T4R | 24 | 152650 |
| 3242527 | 6 | 121.4737425957 | 31.1461980117 | 282 | 3 | 9 | 11.7 | TDD | 951 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3277320 | 3 | 121.4703647429 | 31.1448135458 | 9 | 7 | 11 | 17.3 | TDD | 114 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3278702 | 13 | 121.4744241400 | 31.1487191824 | 274 | 15 | 1 | 24.2 | FDD | 668 | n1 | 152650 | 30M | 4T4R | 14 | 152650 |
| 3279179 | 4 | 121.4725439092 | 31.1443675214 | 159 | 9 | 7 | 19.0 | TDD | 404 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |

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
| 2024-09-20 22:21:31.174 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.192 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.318 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.318 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.984 | NREventA2 | measId:1;ServCellPCI:848;Se... |
| 2024-09-20 22:21:35.107 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.401 | NREventA5 | measId:3;ServCellPCI:848;Se... |
| 2024-09-20 22:21:35.481 | NRHandoverAttempt | SourcePCI:848;SourceNR-ARFC... |
| 2024-09-20 22:21:35.507 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.521 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:35.650 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.650 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3238163 | 1 | 8.6216 | 19.1682 | -116.6195 | 6.6828 | 194.1744 | 0.0186 | 0.0121 |
| 2024_09_20 22:00 | 3219932 | 2 | 11.2106 | 18.9361 | -115.6725 | 15.1034 | 195.2269 | 0.0138 | 0.0130 |
| 2024_09_20 22:00 | 3277320 | 3 | 5.9280 | 5.4670 | -116.4251 | 12.6446 | 94.4945 | 0.0016 | 0.0090 |
| 2024_09_20 22:00 | 3279179 | 4 | 16.6067 | 18.5042 | -114.6717 | 12.2861 | 103.8563 | 0.0188 | 0.0167 |
| 2024_09_20 22:00 | 3233193 | 5 | 11.7235 | 15.3641 | -116.8180 | 19.9817 | 147.8733 | 0.0053 | 0.0053 |
| 2024_09_20 22:00 | 3242527 | 6 | 19.1403 | 6.5711 | -114.2516 | 13.9910 | 94.1056 | 0.0172 | 0.0177 |
| 2024_09_20 22:00 | 3232117 | 7 | 14.4270 | 17.4197 | -114.3359 | 4.7081 | 59.6672 | 0.0098 | 0.0034 |
| 2024_09_20 22:00 | 3242144 | 8 | 18.6892 | 9.7247 | -114.2375 | 4.6091 | 43.0466 | 0.0084 | 0.0153 |
| 2024_09_20 22:00 | 3242485 | 9 | 6.5821 | 17.4395 | -117.6352 | 3.5244 | 20.3823 | 0.0095 | 0.0017 |
| 2024_09_20 22:00 | 3232855 | 10 | 19.8025 | 17.6958 | -115.9555 | 4.7727 | 47.8075 | 0.0186 | 0.0086 |
| 2024_09_20 22:00 | 3222279 | 11 | 10.7166 | 12.0888 | -115.0926 | 3.8910 | 26.6666 | 0.0009 | 0.0081 |
| 2024_09_20 22:00 | 3222451 | 12 | 15.3312 | 15.5195 | -116.9141 | 4.9879 | 55.4706 | 0.0155 | 0.0181 |
| 2024_09_20 22:00 | 3278702 | 13 | 9.9249 | 15.7394 | -114.2406 | 4.3342 | 29.6757 | 0.0137 | 0.0087 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412099_EF684481 | 504990 | 404 | -94.4 | 504990 | 736 | -95.4 | 504990 | 501 | -99.5 | 504990 | 114 |
| MR_1774412099_7C4C016A | 152650 | 4 | -93.4 | 152650 | 193 | -93.0 | 152650 | 33 | -98.9 | 152650 | 165 |
| MR_1774412099_CF421210 | 152650 | 4 | -91.8 | 152650 | 193 | -95.2 | 152650 | 33 | -99.5 | 152650 | 165 |
| MR_1774412099_DCCCA1C8 | 152650 | 4 | -90.0 | 152650 | 193 | -95.9 | 152650 | 33 | -101.5 | 152650 | 165 |
| MR_1774412099_CD09825B | 152650 | 4 | -90.2 | 152650 | 193 | -94.6 | 152650 | 33 | -99.2 | 152650 | 165 |
| MR_1774412099_689BB5B8 | 152650 | 4 | -91.6 | 152650 | 193 | -95.8 | 152650 | 33 | -98.7 | 152650 | 165 |
| MR_1774412099_C99BB9CA | 504990 | 404 | -94.2 | 504990 | 736 | -95.3 | 504990 | 501 | -101.8 | 504990 | 114 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1465: `781f9e9c-2af...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `781f9e9c-2afe-4e0d-9bde-38423c7abede` |
| Tag | **single-answer** |
| 정답 | **C14** |
| C14 의미 | Decrease A3 Offset threshold for 3248187_1 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1465] topology](images/train_1465.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3243647_3
- `C2`: Increase transmission power for 3248187_1
- `C3`: Adjust the azimuth of 3243647_3 by 31 degrees
- `C4`: Add neighbor relationship between 3257340_2 and 3243647_3
- `C5`: Press down the tilt angle of 3248187_1 by 2 degrees
- `C6`: Decrease transmission power for 3248187_1
- `C7`: Decrease A3 Offset threshold for 3243647_3
- `C8`: Insufficient data; more data is needed for judgment.
- `C9`: Press down the tilt angle  of 3243647_3 by 8 degrees
- `C10`: Lift the tilt angle  of 3243647_3 by 8 degrees
- `C11`: Adjust the azimuth of 3248187_1 by 50 degrees
- `C12`: Increase transmission power for 3243647_3
- `C13`: Check test server and transmission issues
- `C14`: Decrease A3 Offset threshold for 3248187_1 **← 정답**
- `C15`: Lift the tilt angle of 3248187_1 by 2 degrees
- `C16`: Add neighbor relationship between 3248187_1 and 3243647_3
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3248187_1
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3248187_1
- `C19`: Decrease transmission power for 3243647_3
- `C20`: Increase A3 Offset threshold for 3248187_1
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3243647_3
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3243647_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.125 | MS1 | 121.4656728681 | 31.1446320551 | 792 | 504990 | -84.00 | 15.18 | 573.60 | 0.15 | 2.19 | 1598 |
| 2024-09-20 22:21:32.409 | MS1 | 121.4656602658 | 31.1446375460 | 792 | 504990 | -75.56 | 14.40 | 315.15 | 0.20 | 2.89 | 1575 |
| 2024-09-20 22:21:33.272 | MS1 | 121.4656696444 | 31.1446373771 | 792 | 504990 | -83.91 | 13.75 | 314.64 | 0.13 | 2.34 | 1587 |
| 2024-09-20 22:21:34.435 | MS1 | 121.4656679527 | 31.1446321227 | 792 | 504990 | -85.58 | -2.42 | 68.35 | 0.03 | 1.27 | 1580 |
| 2024-09-20 22:21:35.181 | MS1 | 121.4656646692 | 31.1446183527 | 792 | 504990 | -88.99 | -3.60 | 43.39 | 0.06 | 1.14 | 1568 |
| 2024-09-20 22:21:36.492 | MS1 | 121.4656594769 | 31.1446310392 | 792 | 504990 | -92.47 | -0.49 | 58.96 | 0.00 | 1.13 | 1579 |
| 2024-09-20 22:21:37.781 | MS1 | 121.4656704652 | 31.1446336449 | 792 | 504990 | -87.08 | -1.23 | 37.65 | 0.02 | 1.43 | 1575 |
| 2024-09-20 22:21:38.413 | MS1 | 121.4656716326 | 31.1446236548 | 792 | 504990 | -92.75 | -2.63 | 60.60 | 0.11 | 1.28 | 1589 |
| 2024-09-20 22:21:39.642 | MS1 | 121.4656698455 | 31.1446247418 | 373 | 504990 | -78.33 | 12.95 | 151.22 | 0.17 | 1.42 | 1569 |
| 2024-09-20 22:21:40.581 | MS1 | 121.4656700341 | 31.1446301694 | 373 | 504990 | -81.14 | 14.99 | 486.97 | 0.14 | 2.22 | 1583 |
| 2024-09-20 22:21:41.129 | MS1 | 121.4656748257 | 31.1446221890 | 373 | 504990 | -77.63 | 13.68 | 479.16 | 0.14 | 2.06 | 1574 |
| 2024-09-20 22:21:42.575 | MS1 | 121.4656652839 | 31.1446311513 | 373 | 504990 | -80.24 | 14.63 | 401.91 | 0.10 | 2.22 | 1579 |

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
| 3243647 | 3 | 121.4734560231 | 31.1537948345 | 247 | 6 | 7 | 33.8 | TDD | 373 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3245733 | 4 | 121.4715363461 | 31.1483445835 | 85 | 4 | 2 | 48.0 | TDD | 727 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3248187 | 1 | 121.4686764894 | 31.1533742995 | 350 | 0 | 6 | 27.8 | TDD | 792 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3257340 | 2 | 121.4646619446 | 31.1460351485 | 202 | 2 | 0 | 18.4 | TDD | 971 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |

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
| 2024-09-20 22:21:31.603 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.624 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.754 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.754 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.469 | NREventA3 | measId:2;ServCellPCI:510;Se... |
| 2024-09-20 22:21:38.709 | NRHandoverAttempt | SourcePCI:510;SourceNR-ARFC... |
| 2024-09-20 22:21:38.749 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.761 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.902 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.902 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3248187 | 1 | 8.1211 | 13.6464 | -115.4756 | 14.9330 | 151.5707 | 0.0134 | 0.1034 |
| 2024_09_20 22:00 | 3257340 | 2 | 14.4918 | 16.9626 | -115.9616 | 8.6653 | 116.2472 | 0.0084 | 0.0008 |
| 2024_09_20 22:00 | 3243647 | 3 | 7.6164 | 14.2994 | -117.7037 | 16.3116 | 81.6528 | 0.0124 | 0.0127 |
| 2024_09_20 22:00 | 3245733 | 4 | 17.4779 | 6.7007 | -114.8197 | 15.9330 | 157.9180 | 0.0052 | 0.0019 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414579_F99E1776 | 504990 | 373 | -80.4 | 504990 | 792 | -84.1 | 504990 | 971 | -87.4 | 504990 | 727 |
| MR_1774414579_22E0C842 | 504990 | 792 | -86.8 | 504990 | 373 | -78.3 | 504990 | 971 | -87.8 | 504990 | 727 |
| MR_1774414579_BFE75CA7 | 504990 | 792 | -86.7 | 504990 | 373 | -78.6 | 504990 | 971 | -86.3 | 504990 | 727 |
| MR_1774414579_B3AB6D2A | 504990 | 792 | -83.8 | 504990 | 373 | -81.2 | 504990 | 971 | -88.5 | 504990 | 727 |
| MR_1774414579_6D272F10 | 504990 | 792 | -85.0 | 504990 | 373 | -79.8 | 504990 | 971 | -87.6 | 504990 | 727 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1466: `bd9518bd-eab...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `bd9518bd-eabf-4da0-9279-5970f42e8678` |
| Tag | **single-answer** |
| 정답 | **C1** |
| C1 의미 | Add neighbor relationship between 3254456_1 and 3221038_4 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1466] topology](images/train_1466.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3254456_1 and 3221038_4 **← 정답**
- `C2`: Increase A3 Offset threshold for 3221038_4
- `C3`: Decrease A3 Offset threshold for 3221038_4
- `C4`: Add neighbor relationship between 3210105_2 and 3221038_4
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3221038_4
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3254456_1
- `C7`: Lift the tilt angle of 3254456_1 by 10 degrees
- `C8`: Decrease A3 Offset threshold for 3254456_1
- `C9`: Press down the tilt angle  of 3221038_4 by 2 degrees
- `C10`: Adjust the azimuth of 3254456_1 by 50 degrees
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3254456_1
- `C12`: Insufficient data; more data is needed for judgment.
- `C13`: Decrease transmission power for 3254456_1
- `C14`: Decrease transmission power for 3221038_4
- `C15`: Increase transmission power for 3221038_4
- `C16`: Adjust the azimuth of 3221038_4 by 13 degrees
- `C17`: Increase transmission power for 3254456_1
- `C18`: Press down the tilt angle of 3254456_1 by 10 degrees
- `C19`: Lift the tilt angle  of 3221038_4 by 2 degrees
- `C20`: Check test server and transmission issues
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3221038_4
- `C22`: Increase A3 Offset threshold for 3254456_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.293 | MS1 | 121.4656636346 | 31.1446256526 | 96 | 504990 | -83.93 | 16.48 | 334.79 | 0.10 | 2.20 | 1596 |
| 2024-09-20 22:21:32.349 | MS1 | 121.4656698160 | 31.1446334699 | 96 | 504990 | -84.90 | 13.58 | 498.15 | 0.17 | 2.63 | 1576 |
| 2024-09-20 22:21:33.485 | MS1 | 121.4656766843 | 31.1446320605 | 96 | 504990 | -76.24 | 15.78 | 496.99 | 0.08 | 2.89 | 1590 |
| 2024-09-20 22:21:34.298 | MS1 | 121.4656734773 | 31.1446266047 | 96 | 504990 | -92.90 | -3.57 | 21.97 | 0.06 | 1.16 | 1568 |
| 2024-09-20 22:21:35.807 | MS1 | 121.4656674074 | 31.1446232639 | 96 | 504990 | -94.58 | -2.54 | 30.02 | 0.18 | 1.03 | 1560 |
| 2024-09-20 22:21:36.674 | MS1 | 121.4656586291 | 31.1446223521 | 96 | 504990 | -90.49 | -0.46 | 58.09 | 0.10 | 1.05 | 1587 |
| 2024-09-20 22:21:37.816 | MS1 | 121.4656596461 | 31.1446248492 | 96 | 504990 | -93.73 | -3.81 | 76.81 | 0.10 | 1.18 | 1572 |
| 2024-09-20 22:21:38.412 | MS1 | 121.4656705214 | 31.1446182045 | 96 | 504990 | -79.24 | 12.65 | 574.53 | 0.08 | 1.46 | 1568 |
| 2024-09-20 22:21:39.542 | MS1 | 121.4656738724 | 31.1446311669 | 96 | 504990 | -83.02 | 17.95 | 393.05 | 0.06 | 1.44 | 1596 |
| 2024-09-20 22:21:40.161 | MS1 | 121.4656615987 | 31.1446331144 | 96 | 504990 | -84.29 | 16.62 | 505.36 | 0.18 | 2.64 | 1599 |
| 2024-09-20 22:21:41.133 | MS1 | 121.4656712042 | 31.1446216383 | 96 | 504990 | -77.27 | 13.80 | 317.09 | 0.02 | 2.44 | 1569 |
| 2024-09-20 22:21:42.667 | MS1 | 121.4656772572 | 31.1446256474 | 96 | 504990 | -81.34 | 17.70 | 431.72 | 0.18 | 2.97 | 1577 |

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
| 3210105 | 2 | 121.4640894160 | 31.1544368611 | 30 | 15 | 6 | 25.4 | TDD | 169 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3221038 | 4 | 121.4711196808 | 31.1529866056 | 222 | 1 | 5 | 23.3 | TDD | 262 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3238764 | 3 | 121.4759756573 | 31.1536623036 | 317 | 4 | 2 | 33.2 | TDD | 76 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3254456 | 1 | 121.4751020528 | 31.1555680345 | 283 | 15 | 5 | 35.3 | TDD | 96 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |

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
| 2024-09-20 22:21:31.218 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.233 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.376 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.376 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.056 | NREventA3 | measId:2;ServCellPCI:881;Se... |
| 2024-09-20 22:21:36.056 | NREventA3 | measId:2;ServCellPCI:881;Se... |
| 2024-09-20 22:21:37.056 | NREventA3 | measId:2;ServCellPCI:881;Se... |
| 2024-09-20 22:21:39.556 | NRRRCReestablishAttempt | PCI:881 |
| 2024-09-20 22:21:39.576 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.589 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:39.724 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.724 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3254456 | 1 | 10.6982 | 18.5576 | -114.1876 | 10.1841 | 137.4584 | 0.0160 | 0.1214 |
| 2024_09_20 22:00 | 3210105 | 2 | 6.0308 | 19.9049 | -116.8206 | 6.3816 | 179.1672 | 0.0179 | 0.0197 |
| 2024_09_20 22:00 | 3238764 | 3 | 12.9113 | 10.1317 | -114.6675 | 9.5472 | 135.7224 | 0.0123 | 0.0155 |
| 2024_09_20 22:00 | 3221038 | 4 | 7.6914 | 17.4432 | -115.2609 | 12.9647 | 171.2255 | 0.0053 | 0.0044 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416759_79B0D8A5 | 504990 | 96 | -91.7 | 504990 | 262 | -87.6 | 504990 | 169 | -98.1 | 504990 | 76 |
| MR_1774416759_D84D5CF1 | 504990 | 96 | -94.0 | 504990 | 262 | -86.9 | 504990 | 169 | -95.4 | 504990 | 76 |
| MR_1774416759_05F823D9 | 504990 | 96 | -92.0 | 504990 | 262 | -87.8 | 504990 | 169 | -97.0 | 504990 | 76 |
| MR_1774416759_6F8C6591 | 504990 | 96 | -94.0 | 504990 | 262 | -90.3 | 504990 | 169 | -98.0 | 504990 | 76 |
| MR_1774416759_DDBF17D0 | 504990 | 96 | -94.7 | 504990 | 262 | -90.0 | 504990 | 169 | -96.3 | 504990 | 76 |
| MR_1774416759_4DBA4021 | 504990 | 262 | -88.6 | 504990 | 96 | -91.5 | 504990 | 169 | -95.1 | 504990 | 76 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1467: `8d7a5ca6-1cd...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `8d7a5ca6-1cd3-46cc-909d-6652f70e7d4d` |
| Tag | **single-answer** |
| 정답 | **C15** |
| C15 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1467] topology](images/train_1467.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3248236_2
- `C2`: Decrease A3 Offset threshold for 3263589_1
- `C3`: Lift the tilt angle  of 3248236_2 by 10 degrees
- `C4`: Add neighbor relationship between 3263589_1 and 3248236_2
- `C5`: Increase A3 Offset threshold for 3263589_1
- `C6`: Adjust the azimuth of 3263589_1 by 50 degrees
- `C7`: Decrease transmission power for 3263589_1
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3248236_2
- `C9`: Add neighbor relationship between 3258306_3 and 3248236_2
- `C10`: Insufficient data; more data is needed for judgment.
- `C11`: Decrease A3 Offset threshold for 3248236_2
- `C12`: Press down the tilt angle of 3263589_1 by 10 degrees
- `C13`: Increase transmission power for 3248236_2
- `C14`: Increase A3 Offset threshold for 3248236_2
- `C15`: Check test server and transmission issues **← 정답**
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3248236_2
- `C17`: Press down the tilt angle  of 3248236_2 by 10 degrees
- `C18`: Lift the tilt angle of 3263589_1 by 10 degrees
- `C19`: Increase transmission power for 3263589_1
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3263589_1
- `C21`: Adjust the azimuth of 3248236_2 by 50 degrees
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3263589_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.305 | MS1 | 121.4656582979 | 31.1446229534 | 18 | 504990 | -90.72 | 17.94 | 521.52 | 0.01 | 2.10 | 1579 |
| 2024-09-20 22:21:32.635 | MS1 | 121.4656597493 | 31.1446364200 | 18 | 504990 | -91.50 | 14.19 | 472.12 | 0.02 | 2.72 | 1564 |
| 2024-09-20 22:21:33.741 | MS1 | 121.4656758140 | 31.1446319863 | 18 | 504990 | -89.03 | 12.61 | 498.50 | 0.00 | 2.09 | 1592 |
| 2024-09-20 22:21:34.164 | MS1 | 121.4656643487 | 31.1446349682 | 18 | 504990 | -91.87 | 15.25 | 66.51 | 0.16 | 2.41 | 453 |
| 2024-09-20 22:21:35.569 | MS1 | 121.4656621409 | 31.1446287097 | 18 | 504990 | -90.66 | 15.73 | 65.19 | 0.17 | 2.83 | 317 |
| 2024-09-20 22:21:36.508 | MS1 | 121.4656623568 | 31.1446230214 | 18 | 504990 | -86.13 | 15.46 | 55.80 | 0.04 | 2.85 | 474 |
| 2024-09-20 22:21:37.637 | MS1 | 121.4656778416 | 31.1446375716 | 18 | 504990 | -93.94 | 10.83 | 89.55 | 0.06 | 2.91 | 434 |
| 2024-09-20 22:21:38.576 | MS1 | 121.4656775862 | 31.1446278168 | 18 | 504990 | -93.70 | 12.58 | 67.73 | 0.10 | 2.09 | 500 |
| 2024-09-20 22:21:39.151 | MS1 | 121.4656639279 | 31.1446225073 | 18 | 504990 | -92.01 | 8.41 | 70.90 | 0.19 | 2.03 | 415 |
| 2024-09-20 22:21:40.246 | MS1 | 121.4656638372 | 31.1446185804 | 18 | 504990 | -89.95 | 9.02 | 477.22 | 0.11 | 2.07 | 1575 |
| 2024-09-20 22:21:41.684 | MS1 | 121.4656755093 | 31.1446193580 | 18 | 504990 | -93.87 | 8.51 | 383.43 | 0.06 | 2.44 | 1582 |
| 2024-09-20 22:21:42.600 | MS1 | 121.4656593396 | 31.1446375727 | 18 | 504990 | -91.26 | 12.61 | 604.20 | 0.01 | 2.84 | 1594 |

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
| 3248236 | 2 | 121.4743164716 | 31.1501640850 | 340 | 12 | 10 | 37.1 | TDD | 762 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3250950 | 4 | 121.4713848584 | 31.1449050162 | 112 | 0 | 9 | 17.7 | TDD | 439 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3258306 | 3 | 121.4741197659 | 31.1487446983 | 322 | 11 | 6 | 46.4 | TDD | 826 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3263589 | 1 | 121.4751235506 | 31.1446268823 | 168 | 14 | 7 | 38.9 | TDD | 18 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:30.906 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.930 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.068 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.068 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.804 | NREventA3 | measId:2;ServCellPCI:572;Se... |
| 2024-09-20 22:21:38.044 | NRHandoverAttempt | SourcePCI:572;SourceNR-ARFC... |
| 2024-09-20 22:21:38.088 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.100 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.222 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.222 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3263589 | 1 | 5.7409 | 8.0146 | -115.6465 | 11.6840 | 140.8852 | 0.0131 | 0.0165 |
| 2024_09_20 22:00 | 3248236 | 2 | 6.0711 | 7.1547 | -117.3664 | 7.2218 | 126.1945 | 0.0178 | 0.0055 |
| 2024_09_20 22:00 | 3258306 | 3 | 11.3788 | 5.4980 | -115.5429 | 18.4786 | 156.7434 | 0.0009 | 0.0190 |
| 2024_09_20 22:00 | 3250950 | 4 | 5.9017 | 14.4913 | -116.9763 | 8.1542 | 116.6966 | 0.0103 | 0.0063 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416707_88207797 | 504990 | 18 | -92.6 | 504990 | 762 | -99.6 | 504990 | 826 | -100.4 | 504990 | 439 |
| MR_1774416707_A11EB3A4 | 504990 | 18 | -90.0 | 504990 | 762 | -97.8 | 504990 | 826 | -102.0 | 504990 | 439 |
| MR_1774416707_FC291637 | 504990 | 18 | -90.1 | 504990 | 762 | -101.1 | 504990 | 826 | -102.9 | 504990 | 439 |
| MR_1774416707_3D687BE1 | 504990 | 18 | -91.7 | 504990 | 762 | -101.4 | 504990 | 826 | -100.8 | 504990 | 439 |
| MR_1774416707_BF606DDF | 504990 | 18 | -93.5 | 504990 | 762 | -100.2 | 504990 | 826 | -100.0 | 504990 | 439 |
| MR_1774416707_00AF2FDC | 504990 | 18 | -91.2 | 504990 | 762 | -100.7 | 504990 | 826 | -101.8 | 504990 | 439 |
| MR_1774416707_CDB9CCDE | 504990 | 18 | -90.2 | 504990 | 762 | -100.1 | 504990 | 826 | -102.0 | 504990 | 439 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1468: `b5af089a-16f...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `b5af089a-16f7-44b0-970e-e0be961ddeb8` |
| Tag | **multiple-answer** |
| 정답 | **C11|C13** |
| C11 의미 | Decrease transmission power for 3211738_2 |
| C13 의미 | Press down the tilt angle  of 3211738_2 by 5 degrees |
| 패턴 분류 | **P3 Overshoot (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1468] topology](images/train_1468.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3279895_3 and 3211738_2
- `C2`: Adjust the azimuth of 3211738_2 by 18 degrees
- `C3`: Lift the tilt angle of 3279895_3 by 2 degrees
- `C4`: Check test server and transmission issues
- `C5`: Increase A3 Offset threshold for 3279895_3
- `C6`: Decrease A3 Offset threshold for 3279895_3
- `C7`: Increase transmission power for 3211738_2
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3279895_3
- `C9`: Adjust the azimuth of 3279895_3 by 10 degrees
- `C10`: Decrease transmission power for 3279895_3
- `C11`: Decrease transmission power for 3211738_2 **← 정답**
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3279895_3
- `C13`: Press down the tilt angle  of 3211738_2 by 5 degrees **← 정답**
- `C14`: Lift the tilt angle  of 3211738_2 by 5 degrees
- `C15`: Increase A3 Offset threshold for 3211738_2
- `C16`: Press down the tilt angle of 3279895_3 by 2 degrees
- `C17`: Decrease A3 Offset threshold for 3211738_2
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3211738_2
- `C19`: Add neighbor relationship between 3231529_1 and 3211738_2
- `C20`: Increase transmission power for 3279895_3
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3211738_2
- `C22`: Insufficient data; more data is needed for judgment.

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.162 | MS1 | 121.4656689602 | 31.1446292111 | 74 | 504990 | -76.73 | 17.41 | 307.96 | 0.17 | 2.56 | 1579 |
| 2024-09-20 22:21:32.858 | MS1 | 121.4656761957 | 31.1446307279 | 74 | 504990 | -77.64 | 16.70 | 588.50 | 0.03 | 2.54 | 1592 |
| 2024-09-20 22:21:33.390 | MS1 | 121.4656766494 | 31.1446339639 | 74 | 504990 | -80.95 | 16.91 | 538.72 | 0.10 | 2.99 | 1566 |
| 2024-09-20 22:21:34.216 | MS1 | 121.4656680226 | 31.1446272595 | 74 | 504990 | -93.31 | 0.11 | 35.51 | 0.14 | 1.37 | 1580 |
| 2024-09-20 22:21:35.830 | MS1 | 121.4656641626 | 31.1446228212 | 74 | 504990 | -86.13 | 3.44 | 75.46 | 0.11 | 1.40 | 1585 |
| 2024-09-20 22:21:36.991 | MS1 | 121.4656696229 | 31.1446344222 | 74 | 504990 | -90.94 | 3.66 | 46.86 | 0.15 | 1.33 | 1566 |
| 2024-09-20 22:21:37.456 | MS1 | 121.4656584445 | 31.1446298286 | 74 | 504990 | -90.13 | 1.28 | 68.15 | 0.01 | 1.41 | 1598 |
| 2024-09-20 22:21:38.330 | MS1 | 121.4656752776 | 31.1446307774 | 74 | 504990 | -94.61 | 3.64 | 56.09 | 0.06 | 1.06 | 1583 |
| 2024-09-20 22:21:39.202 | MS1 | 121.4656741476 | 31.1446293719 | 74 | 504990 | -94.01 | 2.48 | 61.92 | 0.02 | 1.25 | 1598 |
| 2024-09-20 22:21:40.284 | MS1 | 121.4656653667 | 31.1446312265 | 74 | 504990 | -77.14 | 12.74 | 598.91 | 0.16 | 2.79 | 1579 |
| 2024-09-20 22:21:41.228 | MS1 | 121.4656767716 | 31.1446218256 | 74 | 504990 | -79.42 | 17.49 | 459.84 | 0.10 | 2.79 | 1568 |
| 2024-09-20 22:21:42.325 | MS1 | 121.4656599522 | 31.1446278081 | 74 | 504990 | -83.67 | 12.59 | 541.36 | 0.09 | 2.04 | 1571 |

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
| 3211738 | 2 | 121.4746302745 | 31.1554166047 | 233 | 4 | 12 | 36.5 | TDD | 938 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3231529 | 1 | 121.4678030491 | 31.1500882064 | 50 | 3 | 8 | 48.1 | TDD | 96 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3248695 | 4 | 121.4711334543 | 31.1487229412 | 97 | 8 | 4 | 36.7 | TDD | 383 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3279895 | 3 | 121.4735899540 | 31.1457325688 | 251 | 1 | 8 | 16.9 | TDD | 74 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:30.798 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.820 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:30.952 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.952 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3231529 | 1 | 13.1287 | 7.5731 | -117.1819 | 5.5281 | 92.6005 | 0.0069 | 0.0027 |
| 2024_09_20 22:00 | 3211738 | 2 | 18.4505 | 5.4084 | -114.0352 | 10.6175 | 128.0788 | 0.0187 | 0.0039 |
| 2024_09_20 22:00 | 3279895 | 3 | 8.7700 | 15.2098 | -108.8619 | 10.0680 | 87.0454 | 0.0117 | 0.0070 |
| 2024_09_20 22:00 | 3248695 | 4 | 14.0872 | 12.6800 | -117.4144 | 7.0376 | 168.0465 | 0.0189 | 0.0164 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416249_34F974CC | 504990 | 74 | -93.4 | 504990 | 938 | -87.9 | 504990 | 96 | -89.1 | 504990 | 383 |
| MR_1774416249_2B5484D2 | 504990 | 74 | -95.1 | 504990 | 938 | -89.5 | 504990 | 96 | -91.4 | 504990 | 383 |
| MR_1774416249_BA61467D | 504990 | 938 | -91.5 | 504990 | 74 | -87.7 | 504990 | 96 | -92.6 | 504990 | 383 |
| MR_1774416249_43C3F01B | 504990 | 74 | -92.5 | 504990 | 938 | -90.8 | 504990 | 96 | -91.8 | 504990 | 383 |
| MR_1774416249_0D86638C | 504990 | 938 | -93.9 | 504990 | 74 | -87.6 | 504990 | 96 | -92.0 | 504990 | 383 |
| MR_1774416249_F5CDD63F | 504990 | 74 | -93.5 | 504990 | 938 | -89.0 | 504990 | 96 | -91.7 | 504990 | 383 |
| MR_1774416249_3EA7C593 | 504990 | 74 | -91.5 | 504990 | 938 | -89.7 | 504990 | 96 | -92.2 | 504990 | 383 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1469: `b4497b07-ff5...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `b4497b07-ff5f-4886-be65-23a36ee5a123` |
| Tag | **single-answer** |
| 정답 | **C5** |
| C5 의미 | Add neighbor relationship between 3270377_4 and 3251483_1 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1469] topology](images/train_1469.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3251483_1
- `C2`: Lift the tilt angle of 3270377_4 by 4 degrees
- `C3`: Lift the tilt angle  of 3251483_1 by 5 degrees
- `C4`: Adjust the azimuth of 3251483_1 by 19 degrees
- `C5`: Add neighbor relationship between 3270377_4 and 3251483_1 **← 정답**
- `C6`: Add neighbor relationship between 3229396_2 and 3251483_1
- `C7`: Increase A3 Offset threshold for 3270377_4
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3270377_4
- `C9`: Decrease A3 Offset threshold for 3251483_1
- `C10`: Check test server and transmission issues
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3251483_1
- `C12`: Decrease A3 Offset threshold for 3270377_4
- `C13`: Decrease transmission power for 3270377_4
- `C14`: Press down the tilt angle  of 3251483_1 by 5 degrees
- `C15`: Increase transmission power for 3270377_4
- `C16`: Decrease transmission power for 3251483_1
- `C17`: Insufficient data; more data is needed for judgment.
- `C18`: Press down the tilt angle of 3270377_4 by 4 degrees
- `C19`: Adjust the azimuth of 3270377_4 by 50 degrees
- `C20`: Increase A3 Offset threshold for 3251483_1
- `C21`: Increase transmission power for 3251483_1
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3270377_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.725 | MS1 | 121.4656641843 | 31.1446261107 | 852 | 504990 | -75.13 | 12.40 | 543.16 | 0.09 | 2.15 | 1580 |
| 2024-09-20 22:21:32.174 | MS1 | 121.4656688722 | 31.1446300311 | 852 | 504990 | -81.59 | 16.46 | 508.52 | 0.16 | 2.12 | 1561 |
| 2024-09-20 22:21:33.258 | MS1 | 121.4656749567 | 31.1446237183 | 852 | 504990 | -84.86 | 16.95 | 419.10 | 0.17 | 2.95 | 1560 |
| 2024-09-20 22:21:34.784 | MS1 | 121.4656673904 | 31.1446240807 | 852 | 504990 | -87.80 | -2.21 | 40.65 | 0.15 | 1.33 | 1561 |
| 2024-09-20 22:21:35.773 | MS1 | 121.4656600415 | 31.1446287435 | 852 | 504990 | -89.30 | -0.60 | 46.51 | 0.17 | 1.15 | 1570 |
| 2024-09-20 22:21:36.283 | MS1 | 121.4656744462 | 31.1446270242 | 852 | 504990 | -85.22 | -1.90 | 28.35 | 0.15 | 1.49 | 1595 |
| 2024-09-20 22:21:37.569 | MS1 | 121.4656738810 | 31.1446181632 | 852 | 504990 | -86.50 | -1.96 | 44.20 | 0.16 | 1.21 | 1586 |
| 2024-09-20 22:21:38.552 | MS1 | 121.4656633589 | 31.1446299450 | 852 | 504990 | -80.16 | 12.16 | 546.95 | 0.12 | 1.31 | 1585 |
| 2024-09-20 22:21:39.368 | MS1 | 121.4656627620 | 31.1446234954 | 852 | 504990 | -79.25 | 14.56 | 577.09 | 0.13 | 1.12 | 1583 |
| 2024-09-20 22:21:40.697 | MS1 | 121.4656611299 | 31.1446275597 | 852 | 504990 | -82.23 | 13.94 | 454.04 | 0.16 | 2.65 | 1564 |
| 2024-09-20 22:21:41.500 | MS1 | 121.4656662747 | 31.1446188368 | 852 | 504990 | -79.82 | 17.33 | 424.90 | 0.16 | 2.98 | 1582 |
| 2024-09-20 22:21:42.992 | MS1 | 121.4656666854 | 31.1446336487 | 852 | 504990 | -84.20 | 17.38 | 492.57 | 0.08 | 2.29 | 1598 |

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
| 3229396 | 2 | 121.4730128824 | 31.1447781724 | 3 | 6 | 3 | 49.7 | TDD | 716 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3249025 | 3 | 121.4739652330 | 31.1446703800 | 113 | 8 | 8 | 21.8 | TDD | 263 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3251483 | 1 | 121.4745554333 | 31.1484680607 | 224 | 2 | 10 | 46.1 | TDD | 832 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3270377 | 4 | 121.4675063773 | 31.1526327781 | 304 | 2 | 5 | 31.0 | TDD | 852 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:31.361 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.378 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.498 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.498 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.162 | NREventA3 | measId:2;ServCellPCI:289;Se... |
| 2024-09-20 22:21:36.162 | NREventA3 | measId:2;ServCellPCI:289;Se... |
| 2024-09-20 22:21:37.162 | NREventA3 | measId:2;ServCellPCI:289;Se... |
| 2024-09-20 22:21:39.662 | NRRRCReestablishAttempt | PCI:289 |
| 2024-09-20 22:21:39.681 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.693 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:39.814 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.814 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3251483 | 1 | 18.6686 | 10.3163 | -116.8911 | 11.8769 | 130.8707 | 0.0098 | 0.0043 |
| 2024_09_20 22:00 | 3229396 | 2 | 19.7717 | 9.4939 | -116.4850 | 13.1833 | 182.9130 | 0.0040 | 0.0166 |
| 2024_09_20 22:00 | 3249025 | 3 | 17.7926 | 15.1915 | -117.4972 | 15.1303 | 91.9354 | 0.0171 | 0.0067 |
| 2024_09_20 22:00 | 3270377 | 4 | 17.0846 | 16.8757 | -115.3455 | 14.0234 | 121.6164 | 0.0155 | 0.1912 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414094_F0975090 | 504990 | 832 | -81.8 | 504990 | 852 | -87.0 | 504990 | 716 | -81.7 | 504990 | 263 |
| MR_1774414094_325511EB | 504990 | 832 | -82.1 | 504990 | 852 | -87.6 | 504990 | 716 | -85.6 | 504990 | 263 |
| MR_1774414094_96DE76FE | 504990 | 832 | -85.2 | 504990 | 852 | -89.4 | 504990 | 716 | -84.6 | 504990 | 263 |
| MR_1774414094_75ED5C7B | 504990 | 852 | -87.9 | 504990 | 832 | -84.7 | 504990 | 716 | -82.7 | 504990 | 263 |
| MR_1774414094_9C0A7E18 | 504990 | 832 | -82.1 | 504990 | 852 | -89.1 | 504990 | 716 | -84.9 | 504990 | 263 |
| MR_1774414094_A1705CAD | 504990 | 832 | -83.1 | 504990 | 852 | -89.6 | 504990 | 716 | -82.8 | 504990 | 263 |
| MR_1774414094_99F578DE | 504990 | 852 | -87.2 | 504990 | 832 | -83.6 | 504990 | 716 | -85.0 | 504990 | 263 |

> *... 2개 열 생략 (전체 14열)*

---
