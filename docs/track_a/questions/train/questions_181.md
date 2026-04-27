# Track A 문제 분석 — train[1800]~train[1809]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[1800] ~ train[1809] (10개)

## 목차

1. [문제 1800: `678109ab-0e2...`](#1800) — single-answer, 정답: C12
2. [문제 1801: `22875fc7-189...`](#1801) — single-answer, 정답: C17
3. [문제 1802: `53965022-b7f...`](#1802) — single-answer, 정답: C2
4. [문제 1803: `a0b72b49-bf9...`](#1803) — single-answer, 정답: C6
5. [문제 1804: `55668d73-58a...`](#1804) — single-answer, 정답: C22
6. [문제 1805: `889c404a-4d1...`](#1805) — single-answer, 정답: C21
7. [문제 1806: `826a3375-4fa...`](#1806) — single-answer, 정답: C4
8. [문제 1807: `8063d95f-bf8...`](#1807) — single-answer, 정답: C11
9. [문제 1808: `8b429021-ae2...`](#1808) — multiple-answer, 정답: C5|C10
10. [문제 1809: `0017e56b-064...`](#1809) — single-answer, 정답: C9

---

### 문제 1800: `678109ab-0e2...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `678109ab-0e27-466a-bf7b-6db8f0bf2339` |
| Tag | **single-answer** |
| 정답 | **C12** |
| C12 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1800] topology](images/train_1800.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3264058_3 by 50 degrees
- `C2`: Adjust the azimuth of 3242226_4 by 50 degrees
- `C3`: Lift the tilt angle  of 3264058_3 by 4 degrees
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3242226_4
- `C5`: Add neighbor relationship between 3212950_2 and 3264058_3
- `C6`: Add neighbor relationship between 3242226_4 and 3264058_3
- `C7`: Increase A3 Offset threshold for 3242226_4
- `C8`: Increase transmission power for 3264058_3
- `C9`: Press down the tilt angle  of 3264058_3 by 4 degrees
- `C10`: Increase A3 Offset threshold for 3264058_3
- `C11`: Decrease A3 Offset threshold for 3264058_3
- `C12`: Insufficient data; more data is needed for judgment. **← 정답**
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3264058_3
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3242226_4
- `C15`: Decrease A3 Offset threshold for 3242226_4
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3264058_3
- `C17`: Decrease transmission power for 3264058_3
- `C18`: Check test server and transmission issues
- `C19`: Lift the tilt angle of 3242226_4 by 10 degrees
- `C20`: Increase transmission power for 3242226_4
- `C21`: Decrease transmission power for 3242226_4
- `C22`: Press down the tilt angle of 3242226_4 by 10 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.731 | MS1 | 121.4656713789 | 31.1446238935 | 52 | 504990 | -90.12 | 15.91 | 386.14 | 0.06 | 2.06 | 1564 |
| 2024-09-20 22:21:32.995 | MS1 | 121.4656591786 | 31.1446372777 | 52 | 504990 | -91.03 | 13.01 | 395.54 | 0.19 | 2.68 | 1579 |
| 2024-09-20 22:21:33.942 | MS1 | 121.4656720612 | 31.1446346619 | 52 | 504990 | -91.68 | 15.63 | 322.44 | 0.12 | 2.34 | 1597 |
| 2024-09-20 22:21:34.151 | MS1 | 121.4656709196 | 31.1446379848 | 52 | 504990 | -86.68 | 15.48 | 65.22 | 0.04 | 2.57 | 1594 |
| 2024-09-20 22:21:35.524 | MS1 | 121.4656615442 | 31.1446238027 | 52 | 504990 | -91.01 | 15.48 | 89.19 | 0.13 | 2.94 | 1571 |
| 2024-09-20 22:21:36.870 | MS1 | 121.4656651296 | 31.1446326760 | 52 | 504990 | -86.09 | 12.02 | 55.88 | 0.11 | 2.51 | 1560 |
| 2024-09-20 22:21:37.589 | MS1 | 121.4656736920 | 31.1446320805 | 52 | 504990 | -93.59 | 7.59 | 80.80 | 0.01 | 2.97 | 1578 |
| 2024-09-20 22:21:38.694 | MS1 | 121.4656601250 | 31.1446377727 | 52 | 504990 | -91.65 | 8.53 | 73.10 | 0.13 | 2.47 | 1565 |
| 2024-09-20 22:21:39.332 | MS1 | 121.4656617710 | 31.1446338411 | 52 | 504990 | -91.58 | 12.06 | 61.11 | 0.04 | 2.89 | 1588 |
| 2024-09-20 22:21:40.514 | MS1 | 121.4656703393 | 31.1446367911 | 52 | 504990 | -90.33 | 10.30 | 514.76 | 0.17 | 2.98 | 1566 |
| 2024-09-20 22:21:41.512 | MS1 | 121.4656622670 | 31.1446345418 | 52 | 504990 | -91.57 | 8.99 | 361.30 | 0.01 | 2.72 | 1584 |
| 2024-09-20 22:21:42.950 | MS1 | 121.4656758725 | 31.1446372792 | 52 | 504990 | -91.06 | 7.14 | 372.77 | 0.10 | 2.55 | 1562 |

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
| 3212950 | 2 | 121.4724370841 | 31.1506544497 | 79 | 5 | 7 | 32.4 | TDD | 380 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3242226 | 4 | 121.4682860802 | 31.1523314579 | 272 | 13 | 8 | 27.5 | TDD | 52 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3264058 | 3 | 121.4672459647 | 31.1552642884 | 55 | 2 | 3 | 44.4 | TDD | 470 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3272520 | 1 | 121.4713642210 | 31.1525095011 | 204 | 4 | 7 | 19.1 | TDD | 436 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |

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
| 2024-09-20 22:21:30.927 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.952 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.084 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.084 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.735 | NREventA3 | measId:2;ServCellPCI:848;Se... |
| 2024-09-20 22:21:37.975 | NRHandoverAttempt | SourcePCI:848;SourceNR-ARFC... |
| 2024-09-20 22:21:38.016 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.031 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.139 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.139 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3272520 | 1 | 89.3059 | 86.9527 | -116.9121 | 5.5754 | 121.9066 | 0.0194 | 0.0038 |
| 2024_09_19 22:00 | 3212950 | 2 | 92.4186 | 88.3420 | -116.3739 | 13.3834 | 89.1915 | 0.0115 | 0.0174 |
| 2024_09_19 22:00 | 3264058 | 3 | 81.1595 | 82.9755 | -117.9546 | 13.9301 | 82.8768 | 0.0192 | 0.0166 |
| 2024_09_19 22:00 | 3242226 | 4 | 77.8688 | 81.8906 | -116.9897 | 12.3850 | 133.2045 | 0.0075 | 0.0040 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414800_38A54FF4 | 504990 | 52 | -85.2 | 504990 | 470 | -86.5 | 504990 | 380 | -98.7 | 504990 | 436 |
| MR_1774414800_5150A824 | 504990 | 52 | -84.8 | 504990 | 470 | -87.4 | 504990 | 380 | -95.8 | 504990 | 436 |
| MR_1774414800_D3F1364D | 504990 | 52 | -86.6 | 504990 | 470 | -87.1 | 504990 | 380 | -97.2 | 504990 | 436 |
| MR_1774414800_1D25061A | 504990 | 52 | -87.9 | 504990 | 470 | -87.4 | 504990 | 380 | -95.8 | 504990 | 436 |
| MR_1774414800_08DD1714 | 504990 | 52 | -87.0 | 504990 | 470 | -86.8 | 504990 | 380 | -96.8 | 504990 | 436 |
| MR_1774414800_0D199788 | 504990 | 52 | -88.2 | 504990 | 470 | -88.2 | 504990 | 380 | -95.2 | 504990 | 436 |
| MR_1774414800_01639EB1 | 504990 | 52 | -87.9 | 504990 | 470 | -86.9 | 504990 | 380 | -97.2 | 504990 | 436 |
| MR_1774414800_F0532755 | 504990 | 52 | -86.7 | 504990 | 470 | -88.2 | 504990 | 380 | -98.8 | 504990 | 436 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1801: `22875fc7-189...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `22875fc7-1894-404f-a531-8dba69fc5d13` |
| Tag | **single-answer** |
| 정답 | **C17** |
| C17 의미 | Add neighbor relationship between 3265409_3 and 3254961_1 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1801] topology](images/train_1801.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3265409_3 by 9 degrees
- `C2`: Adjust the azimuth of 3254961_1 by 31 degrees
- `C3`: Increase A3 Offset threshold for 3265409_3
- `C4`: Decrease transmission power for 3265409_3
- `C5`: Add neighbor relationship between 3232679_4 and 3254961_1
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3254961_1
- `C7`: Press down the tilt angle of 3265409_3 by 9 degrees
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3265409_3
- `C9`: Increase transmission power for 3254961_1
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3265409_3
- `C11`: Decrease A3 Offset threshold for 3254961_1
- `C12`: Increase transmission power for 3265409_3
- `C13`: Insufficient data; more data is needed for judgment.
- `C14`: Press down the tilt angle  of 3254961_1 by 4 degrees
- `C15`: Check test server and transmission issues
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3254961_1
- `C17`: Add neighbor relationship between 3265409_3 and 3254961_1 **← 정답**
- `C18`: Adjust the azimuth of 3265409_3 by 21 degrees
- `C19`: Decrease A3 Offset threshold for 3265409_3
- `C20`: Lift the tilt angle  of 3254961_1 by 4 degrees
- `C21`: Increase A3 Offset threshold for 3254961_1
- `C22`: Decrease transmission power for 3254961_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.934 | MS1 | 121.4656666089 | 31.1446283907 | 190 | 504990 | -82.24 | 14.23 | 442.67 | 0.08 | 2.40 | 1577 |
| 2024-09-20 22:21:32.184 | MS1 | 121.4656761427 | 31.1446188071 | 190 | 504990 | -80.04 | 12.98 | 414.07 | 0.19 | 2.19 | 1584 |
| 2024-09-20 22:21:33.137 | MS1 | 121.4656583198 | 31.1446355248 | 190 | 504990 | -77.22 | 14.10 | 411.93 | 0.09 | 2.77 | 1587 |
| 2024-09-20 22:21:34.572 | MS1 | 121.4656706747 | 31.1446294428 | 190 | 504990 | -87.66 | -1.71 | 60.19 | 0.11 | 1.17 | 1569 |
| 2024-09-20 22:21:35.879 | MS1 | 121.4656672938 | 31.1446254373 | 190 | 504990 | -85.70 | -1.23 | 28.71 | 0.04 | 1.06 | 1580 |
| 2024-09-20 22:21:36.272 | MS1 | 121.4656617585 | 31.1446333906 | 190 | 504990 | -87.20 | -2.91 | 75.80 | 0.02 | 1.44 | 1583 |
| 2024-09-20 22:21:37.472 | MS1 | 121.4656602313 | 31.1446339153 | 190 | 504990 | -86.24 | -3.15 | 43.33 | 0.04 | 1.20 | 1572 |
| 2024-09-20 22:21:38.127 | MS1 | 121.4656755569 | 31.1446260538 | 190 | 504990 | -82.66 | 13.05 | 479.89 | 0.02 | 1.22 | 1578 |
| 2024-09-20 22:21:39.973 | MS1 | 121.4656758978 | 31.1446285761 | 190 | 504990 | -77.50 | 15.19 | 512.92 | 0.13 | 1.23 | 1570 |
| 2024-09-20 22:21:40.569 | MS1 | 121.4656711484 | 31.1446252757 | 190 | 504990 | -79.86 | 13.08 | 416.00 | 0.04 | 2.79 | 1579 |
| 2024-09-20 22:21:41.853 | MS1 | 121.4656619636 | 31.1446298326 | 190 | 504990 | -84.42 | 13.52 | 449.03 | 0.13 | 2.67 | 1571 |
| 2024-09-20 22:21:42.811 | MS1 | 121.4656693595 | 31.1446216882 | 190 | 504990 | -81.47 | 14.82 | 331.52 | 0.19 | 2.03 | 1590 |

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
| 3232679 | 4 | 121.4736924203 | 31.1476115299 | 9 | 14 | 4 | 48.5 | TDD | 535 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3241663 | 2 | 121.4721436102 | 31.1445859139 | 60 | 10 | 12 | 29.7 | TDD | 266 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3254961 | 1 | 121.4641697169 | 31.1482722835 | 192 | 1 | 4 | 23.5 | TDD | 698 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3265409 | 3 | 121.4695741329 | 31.1519345682 | 226 | 6 | 9 | 43.5 | TDD | 190 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:31.319 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.336 | NRRandomAccessSuc | Delay：17ms |
| 2024-09-20 22:21:31.474 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.474 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.142 | NREventA3 | measId:2;ServCellPCI:209;Se... |
| 2024-09-20 22:21:36.142 | NREventA3 | measId:2;ServCellPCI:209;Se... |
| 2024-09-20 22:21:37.142 | NREventA3 | measId:2;ServCellPCI:209;Se... |
| 2024-09-20 22:21:39.642 | NRRRCReestablishAttempt | PCI:209 |
| 2024-09-20 22:21:39.652 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.664 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:39.808 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.808 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3254961 | 1 | 18.3639 | 11.2013 | -116.1157 | 10.2385 | 189.9290 | 0.0038 | 0.0012 |
| 2024_09_20 22:00 | 3241663 | 2 | 17.7707 | 12.5500 | -115.9159 | 8.1256 | 150.7242 | 0.0180 | 0.0020 |
| 2024_09_20 22:00 | 3265409 | 3 | 19.2237 | 19.5533 | -114.2801 | 5.6442 | 157.4597 | 0.0094 | 0.1965 |
| 2024_09_20 22:00 | 3232679 | 4 | 8.2454 | 15.7483 | -114.5154 | 19.3427 | 138.1663 | 0.0118 | 0.0108 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416876_70D66B09 | 504990 | 190 | -89.5 | 504990 | 698 | -82.4 | 504990 | 535 | -85.3 | 504990 | 266 |
| MR_1774416876_0F816F88 | 504990 | 190 | -87.6 | 504990 | 698 | -83.5 | 504990 | 535 | -85.0 | 504990 | 266 |
| MR_1774416876_A3F190C7 | 504990 | 190 | -89.6 | 504990 | 698 | -81.9 | 504990 | 535 | -83.7 | 504990 | 266 |
| MR_1774416876_4351E577 | 504990 | 190 | -86.2 | 504990 | 698 | -83.3 | 504990 | 535 | -83.1 | 504990 | 266 |
| MR_1774416876_424AEBE3 | 504990 | 698 | -83.8 | 504990 | 190 | -86.8 | 504990 | 535 | -82.4 | 504990 | 266 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1802: `53965022-b7f...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `53965022-b7f0-475e-9d21-079990037a38` |
| Tag | **single-answer** |
| 정답 | **C2** |
| C2 의미 | Add neighbor relationship between 3229130_3 and 3226693_2 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1802] topology](images/train_1802.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3229130_3
- `C2`: Add neighbor relationship between 3229130_3 and 3226693_2 **← 정답**
- `C3`: Decrease A3 Offset threshold for 3226693_2
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3226693_2
- `C5`: Press down the tilt angle  of 3226693_2 by 3 degrees
- `C6`: Lift the tilt angle of 3229130_3 by 10 degrees
- `C7`: Decrease A3 Offset threshold for 3229130_3
- `C8`: Press down the tilt angle of 3229130_3 by 10 degrees
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3226693_2
- `C10`: Increase A3 Offset threshold for 3229130_3
- `C11`: Lift the tilt angle  of 3226693_2 by 3 degrees
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3229130_3
- `C13`: Insufficient data; more data is needed for judgment.
- `C14`: Adjust the azimuth of 3229130_3 by 50 degrees
- `C15`: Decrease transmission power for 3229130_3
- `C16`: Adjust the azimuth of 3226693_2 by 30 degrees
- `C17`: Check test server and transmission issues
- `C18`: Increase transmission power for 3226693_2
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3229130_3
- `C20`: Add neighbor relationship between 3275428_1 and 3226693_2
- `C21`: Increase A3 Offset threshold for 3226693_2
- `C22`: Decrease transmission power for 3226693_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.706 | MS1 | 121.4656725056 | 31.1446232216 | 67 | 504990 | -80.21 | 16.05 | 367.70 | 0.16 | 2.60 | 1560 |
| 2024-09-20 22:21:32.646 | MS1 | 121.4656763957 | 31.1446236717 | 67 | 504990 | -75.34 | 13.14 | 378.71 | 0.05 | 2.49 | 1584 |
| 2024-09-20 22:21:33.499 | MS1 | 121.4656663107 | 31.1446370974 | 67 | 504990 | -79.59 | 14.94 | 429.04 | 0.13 | 2.87 | 1600 |
| 2024-09-20 22:21:34.766 | MS1 | 121.4656766338 | 31.1446332291 | 67 | 504990 | -89.25 | -1.52 | 69.68 | 0.11 | 1.07 | 1591 |
| 2024-09-20 22:21:35.604 | MS1 | 121.4656664692 | 31.1446300849 | 67 | 504990 | -90.03 | -1.05 | 67.91 | 0.08 | 1.07 | 1570 |
| 2024-09-20 22:21:36.213 | MS1 | 121.4656652008 | 31.1446262314 | 67 | 504990 | -87.48 | -0.42 | 59.44 | 0.08 | 1.03 | 1587 |
| 2024-09-20 22:21:37.107 | MS1 | 121.4656619508 | 31.1446290135 | 67 | 504990 | -90.53 | -0.71 | 49.90 | 0.13 | 1.23 | 1596 |
| 2024-09-20 22:21:38.239 | MS1 | 121.4656581360 | 31.1446222067 | 67 | 504990 | -80.79 | 13.41 | 571.73 | 0.11 | 1.07 | 1588 |
| 2024-09-20 22:21:39.436 | MS1 | 121.4656685996 | 31.1446252442 | 67 | 504990 | -76.45 | 12.24 | 309.19 | 0.12 | 1.44 | 1570 |
| 2024-09-20 22:21:40.964 | MS1 | 121.4656692607 | 31.1446297864 | 67 | 504990 | -81.81 | 16.82 | 403.53 | 0.02 | 2.99 | 1578 |
| 2024-09-20 22:21:41.630 | MS1 | 121.4656714671 | 31.1446192933 | 67 | 504990 | -80.73 | 14.62 | 468.78 | 0.04 | 2.26 | 1561 |
| 2024-09-20 22:21:42.808 | MS1 | 121.4656626186 | 31.1446301771 | 67 | 504990 | -81.88 | 13.66 | 345.20 | 0.10 | 2.55 | 1597 |

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
| 3226693 | 2 | 121.4678486063 | 31.1557507247 | 160 | 2 | 12 | 17.8 | TDD | 905 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3229130 | 3 | 121.4642373273 | 31.1449447420 | 250 | 2 | 7 | 49.1 | TDD | 67 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3271117 | 4 | 121.4737907406 | 31.1486778834 | 237 | 2 | 6 | 21.8 | TDD | 766 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3275428 | 1 | 121.4644688886 | 31.1443998498 | 65 | 11 | 11 | 38.5 | TDD | 896 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |

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
| 2024-09-20 22:21:31.512 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.536 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.648 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.648 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.313 | NREventA3 | measId:2;ServCellPCI:695;Se... |
| 2024-09-20 22:21:36.313 | NREventA3 | measId:2;ServCellPCI:695;Se... |
| 2024-09-20 22:21:37.313 | NREventA3 | measId:2;ServCellPCI:695;Se... |
| 2024-09-20 22:21:39.813 | NRRRCReestablishAttempt | PCI:695 |
| 2024-09-20 22:21:39.825 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.838 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:39.974 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.974 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3275428 | 1 | 14.2980 | 8.1009 | -116.0763 | 18.7844 | 164.5545 | 0.0089 | 0.0090 |
| 2024_09_20 22:00 | 3226693 | 2 | 6.3201 | 14.4305 | -114.6289 | 8.2373 | 153.4900 | 0.0066 | 0.0154 |
| 2024_09_20 22:00 | 3229130 | 3 | 7.4635 | 11.5268 | -115.0224 | 7.5196 | 183.8491 | 0.0112 | 0.1422 |
| 2024_09_20 22:00 | 3271117 | 4 | 18.4324 | 7.1703 | -117.7129 | 10.2283 | 175.0381 | 0.0176 | 0.0039 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412445_8D080E9A | 504990 | 905 | -83.5 | 504990 | 67 | -90.2 | 504990 | 896 | -88.0 | 504990 | 766 |
| MR_1774412445_7065741A | 504990 | 67 | -89.3 | 504990 | 905 | -82.1 | 504990 | 896 | -88.0 | 504990 | 766 |
| MR_1774412445_D1E499F4 | 504990 | 67 | -91.1 | 504990 | 905 | -83.3 | 504990 | 896 | -88.7 | 504990 | 766 |
| MR_1774412445_AB6C595F | 504990 | 905 | -85.4 | 504990 | 67 | -90.0 | 504990 | 896 | -88.5 | 504990 | 766 |
| MR_1774412445_FACFC1BB | 504990 | 67 | -88.4 | 504990 | 905 | -84.4 | 504990 | 896 | -87.2 | 504990 | 766 |
| MR_1774412445_C94C9252 | 504990 | 67 | -88.4 | 504990 | 905 | -83.5 | 504990 | 896 | -86.2 | 504990 | 766 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1803: `a0b72b49-bf9...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `a0b72b49-bf99-4119-9d63-fc172fbd25fa` |
| Tag | **single-answer** |
| 정답 | **C6** |
| C6 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3265669_3 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1803] topology](images/train_1803.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment.
- `C2`: Increase transmission power for 3265669_3
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3277497_1
- `C4`: Press down the tilt angle  of 3277497_1 by 10 degrees
- `C5`: Decrease A3 Offset threshold for 3265669_3
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3265669_3 **← 정답**
- `C7`: Decrease transmission power for 3265669_3
- `C8`: Add neighbor relationship between 3230266_4 and 3277497_1
- `C9`: Adjust the azimuth of 3265669_3 by 5 degrees
- `C10`: Decrease transmission power for 3277497_1
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3265669_3
- `C12`: Decrease A3 Offset threshold for 3277497_1
- `C13`: Lift the tilt angle of 3265669_3 by 5 degrees
- `C14`: Increase A3 Offset threshold for 3265669_3
- `C15`: Lift the tilt angle  of 3277497_1 by 10 degrees
- `C16`: Check test server and transmission issues
- `C17`: Press down the tilt angle of 3265669_3 by 5 degrees
- `C18`: Increase A3 Offset threshold for 3277497_1
- `C19`: Adjust the azimuth of 3277497_1 by 50 degrees
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3277497_1
- `C21`: Increase transmission power for 3277497_1
- `C22`: Add neighbor relationship between 3265669_3 and 3277497_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.900 | MS1 | 121.4656772962 | 31.1446283677 | 244 | 504990 | -88.69 | 13.62 | 313.56 | 0.18 | 2.32 | 1593 |
| 2024-09-20 22:21:32.518 | MS1 | 121.4656674820 | 31.1446301888 | 244 | 504990 | -87.78 | 12.19 | 544.14 | 0.09 | 2.36 | 1583 |
| 2024-09-20 22:21:33.424 | MS1 | 121.4656771662 | 31.1446326097 | 244 | 504990 | -88.67 | 17.46 | 547.61 | 0.07 | 2.59 | 1590 |
| 2024-09-20 22:21:34.132 | MS1 | 121.4656656844 | 31.1446262183 | 244 | 504990 | -86.78 | 12.57 | 93.31 | 0.69 | 2.04 | 667 |
| 2024-09-20 22:21:35.835 | MS1 | 121.4656631424 | 31.1446219161 | 244 | 504990 | -89.44 | 12.68 | 78.21 | 0.58 | 2.73 | 524 |
| 2024-09-20 22:21:36.354 | MS1 | 121.4656614087 | 31.1446287967 | 244 | 504990 | -86.36 | 12.43 | 89.86 | 0.63 | 2.30 | 656 |
| 2024-09-20 22:21:37.280 | MS1 | 121.4656753559 | 31.1446266991 | 244 | 504990 | -90.74 | 13.00 | 77.96 | 0.54 | 2.25 | 580 |
| 2024-09-20 22:21:38.748 | MS1 | 121.4656745779 | 31.1446364286 | 244 | 504990 | -89.03 | 9.58 | 68.59 | 0.62 | 2.82 | 606 |
| 2024-09-20 22:21:39.129 | MS1 | 121.4656708528 | 31.1446278173 | 244 | 504990 | -89.59 | 7.58 | 63.27 | 0.63 | 2.86 | 628 |
| 2024-09-20 22:21:40.929 | MS1 | 121.4656642604 | 31.1446325851 | 244 | 504990 | -89.81 | 7.34 | 453.19 | 0.01 | 2.66 | 1570 |
| 2024-09-20 22:21:41.146 | MS1 | 121.4656590936 | 31.1446317684 | 244 | 504990 | -92.69 | 7.80 | 428.49 | 0.02 | 2.25 | 1582 |
| 2024-09-20 22:21:42.492 | MS1 | 121.4656605510 | 31.1446374129 | 244 | 504990 | -89.71 | 9.05 | 374.28 | 0.17 | 2.27 | 1589 |

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
| 3230235 | 2 | 121.4711488955 | 31.1526766126 | 62 | 8 | 6 | 29.8 | TDD | 579 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3230266 | 4 | 121.4650047358 | 31.1477237873 | 41 | 2 | 8 | 41.1 | TDD | 718 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3265669 | 3 | 121.4731713655 | 31.1513171731 | 229 | 3 | 6 | 37.8 | TDD | 244 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3277497 | 1 | 121.4661807985 | 31.1449139883 | 59 | 0 | 1 | 17.3 | TDD | 880 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |

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
| 2024-09-20 22:21:30.934 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.956 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.058 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.058 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.773 | NREventA3 | measId:2;ServCellPCI:729;Se... |
| 2024-09-20 22:21:38.013 | NRHandoverAttempt | SourcePCI:729;SourceNR-ARFC... |
| 2024-09-20 22:21:38.049 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.060 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.195 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.195 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3277497 | 1 | 14.6109 | 17.7505 | -116.2497 | 13.4143 | 147.0674 | 0.0044 | 0.0000 |
| 2024_09_20 22:00 | 3230235 | 2 | 9.8583 | 11.4887 | -114.6583 | 11.0195 | 195.2774 | 0.0130 | 0.0050 |
| 2024_09_20 22:00 | 3265669 | 3 | 13.0296 | 18.7029 | -116.4263 | 6.2368 | 81.0098 | 0.0011 | 0.0122 |
| 2024_09_20 22:00 | 3230266 | 4 | 10.0524 | 12.3814 | -116.9979 | 9.6746 | 134.0366 | 0.0190 | 0.0155 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417128_1D13B49B | 504990 | 244 | -86.9 | 504990 | 880 | -92.6 | 504990 | 718 | -94.1 | 504990 | 579 |
| MR_1774417128_FAF11DCC | 504990 | 244 | -87.3 | 504990 | 880 | -92.0 | 504990 | 718 | -95.1 | 504990 | 579 |
| MR_1774417128_29F69EAD | 504990 | 244 | -88.2 | 504990 | 880 | -93.2 | 504990 | 718 | -96.5 | 504990 | 579 |
| MR_1774417128_0663338B | 504990 | 244 | -86.1 | 504990 | 880 | -90.7 | 504990 | 718 | -96.5 | 504990 | 579 |
| MR_1774417128_B4BF54FE | 504990 | 244 | -87.6 | 504990 | 880 | -91.6 | 504990 | 718 | -97.4 | 504990 | 579 |
| MR_1774417128_E789BB6E | 504990 | 244 | -86.8 | 504990 | 880 | -92.9 | 504990 | 718 | -96.8 | 504990 | 579 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1804: `55668d73-58a...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `55668d73-58a7-4869-8d3c-2f86cf644284` |
| Tag | **single-answer** |
| 정답 | **C22** |
| C22 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3278611_4 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1804] topology](images/train_1804.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3265699_1
- `C2`: Press down the tilt angle of 3278611_4 by 2 degrees
- `C3`: Add neighbor relationship between 3214064_13 and 3265699_1
- `C4`: Increase A3 Offset threshold for 3265699_1
- `C5`: Decrease transmission power for 3278611_4
- `C6`: Check test server and transmission issues
- `C7`: Add neighbor relationship between 3278611_4 and 3265699_1
- `C8`: Increase transmission power for 3265699_1
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3278611_4
- `C10`: Adjust the azimuth of 3265699_1 by 37 degrees
- `C11`: Decrease transmission power for 3265699_1
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3265699_1
- `C13`: Press down the tilt angle  of 3265699_1 by 2 degrees
- `C14`: Decrease A3 Offset threshold for 3278611_4
- `C15`: Increase transmission power for 3278611_4
- `C16`: Lift the tilt angle of 3278611_4 by 2 degrees
- `C17`: Lift the tilt angle  of 3265699_1 by 2 degrees
- `C18`: Decrease A3 Offset threshold for 3265699_1
- `C19`: Insufficient data; more data is needed for judgment.
- `C20`: Increase A3 Offset threshold for 3278611_4
- `C21`: Adjust the azimuth of 3278611_4 by 17 degrees
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3278611_4 **← 정답**

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.247 | MS1 | 121.4656623501 | 31.1446356135 | 533 | 504990 | -95.42 | 14.34 | 478.45 | 0.13 | 2.51 | 1570 |
| 2024-09-20 22:21:32.542 | MS1 | 121.4656651731 | 31.1446222733 | 734 | 504990 | -95.42 | 11.52 | 598.61 | 0.01 | 2.66 | 1578 |
| 2024-09-20 22:21:33.153 | MS1 | 121.4656628054 | 31.1446354961 | 164 | 504990 | -93.76 | 14.38 | 335.17 | 0.16 | 2.63 | 1563 |
| 2024-09-20 22:21:34.625 | MS1 | 121.4656711544 | 31.1446268901 | 688 | 152650 | -88.95 | 6.97 | 66.58 | 0.04 | 1.64 | 988 |
| 2024-09-20 22:21:35.684 | MS1 | 121.4656677837 | 31.1446202490 | 714 | 152650 | -96.05 | 4.10 | 46.14 | 0.07 | 1.80 | 982 |
| 2024-09-20 22:21:36.149 | MS1 | 121.4656594570 | 31.1446246728 | 700 | 152650 | -88.94 | 7.97 | 78.49 | 0.04 | 1.68 | 966 |
| 2024-09-20 22:21:37.310 | MS1 | 121.4656592042 | 31.1446270771 | 1 | 152650 | -87.46 | 2.59 | 68.47 | 0.20 | 1.93 | 925 |
| 2024-09-20 22:21:38.782 | MS1 | 121.4656623949 | 31.1446286796 | 688 | 152650 | -94.41 | 5.99 | 86.05 | 0.13 | 1.55 | 942 |
| 2024-09-20 22:21:39.400 | MS1 | 121.4656618750 | 31.1446327445 | 714 | 152650 | -92.17 | 5.36 | 95.53 | 0.19 | 1.84 | 938 |
| 2024-09-20 22:21:40.377 | MS1 | 121.4656690409 | 31.1446308942 | 700 | 152650 | -91.93 | 2.02 | 57.12 | 0.17 | 2.94 | 1574 |
| 2024-09-20 22:21:41.655 | MS1 | 121.4656642014 | 31.1446319502 | 1 | 152650 | -90.18 | 7.03 | 61.29 | 0.01 | 2.18 | 1582 |
| 2024-09-20 22:21:42.986 | MS1 | 121.4656699872 | 31.1446349842 | 688 | 152650 | -92.43 | 3.81 | 58.65 | 0.04 | 2.05 | 1568 |

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
| 3214064 | 13 | 121.4681403346 | 31.1535100189 | 212 | 2 | 0 | 8.4 | FDD | 700 | n1 | 152650 | 30M | 4T4R | 29 | 152650 |
| 3220832 | 9 | 121.4734921533 | 31.1508037139 | 258 | 6 | 5 | 4.3 | FDD | 714 | n1 | 152650 | 30M | 4T4R | 17 | 152650 |
| 3230129 | 3 | 121.4749898316 | 31.1557458128 | 91 | 2 | 5 | 0.5 | TDD | 525 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3233434 | 6 | 121.4736465744 | 31.1473682496 | 79 | 7 | 1 | 26.1 | TDD | 734 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3234222 | 5 | 121.4688162979 | 31.1500483085 | 18 | 9 | 5 | 17.9 | TDD | 507 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3243449 | 7 | 121.4687195311 | 31.1552852547 | 110 | 7 | 5 | 23.1 | FDD | 1 | n1 | 152650 | 30M | 4T4R | 20 | 152650 |
| 3249353 | 2 | 121.4699466622 | 31.1525497306 | 66 | 10 | 5 | 17.7 | TDD | 164 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3257239 | 10 | 121.4670921942 | 31.1484879476 | 286 | 15 | 9 | 28.0 | FDD | 298 | n1 | 152650 | 30M | 4T4R | 23 | 152650 |
| 3260790 | 11 | 121.4723975406 | 31.1544684668 | 203 | 4 | 0 | 1.2 | FDD | 590 | n1 | 152650 | 30M | 4T4R | 11 | 152650 |
| 3263912 | 8 | 121.4673895372 | 31.1539252659 | 298 | 1 | 10 | 22.8 | FDD | 930 | n1 | 152650 | 30M | 4T4R | 20 | 152650 |
| 3265699 | 1 | 121.4717569656 | 31.1531178634 | 175 | 1 | 0 | 15.7 | TDD | 129 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3270244 | 12 | 121.4651210506 | 31.1454759263 | 341 | 15 | 8 | 15.9 | FDD | 688 | n1 | 152650 | 30M | 4T4R | 10 | 152650 |
| 3278611 | 4 | 121.4749899412 | 31.1543736594 | 202 | 1 | 11 | 21.1 | TDD | 533 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |

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
| 2024-09-20 22:21:31.300 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.318 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.432 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.432 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.111 | NREventA2 | measId:1;ServCellPCI:489;Se... |
| 2024-09-20 22:21:35.240 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.471 | NREventA5 | measId:3;ServCellPCI:489;Se... |
| 2024-09-20 22:21:35.501 | NRHandoverAttempt | SourcePCI:489;SourceNR-ARFC... |
| 2024-09-20 22:21:35.528 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.541 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:35.689 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.689 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3265699 | 1 | 18.3470 | 8.1256 | -117.2438 | 17.2912 | 161.5655 | 0.0055 | 0.0100 |
| 2024_09_20 22:00 | 3249353 | 2 | 8.9354 | 8.7901 | -115.9514 | 12.5305 | 90.5065 | 0.0173 | 0.0152 |
| 2024_09_20 22:00 | 3230129 | 3 | 19.0097 | 9.1220 | -115.2018 | 17.1542 | 132.2731 | 0.0007 | 0.0111 |
| 2024_09_20 22:00 | 3278611 | 4 | 12.7138 | 5.4223 | -114.1561 | 10.9633 | 115.2973 | 0.0012 | 0.0176 |
| 2024_09_20 22:00 | 3234222 | 5 | 13.9737 | 14.8752 | -114.4414 | 12.5111 | 126.6543 | 0.0197 | 0.0142 |
| 2024_09_20 22:00 | 3233434 | 6 | 7.6285 | 9.1196 | -115.8955 | 9.2256 | 94.4888 | 0.0150 | 0.0179 |
| 2024_09_20 22:00 | 3243449 | 7 | 19.2340 | 5.0482 | -117.5463 | 4.7767 | 47.0638 | 0.0199 | 0.0160 |
| 2024_09_20 22:00 | 3263912 | 8 | 9.1167 | 9.4841 | -114.1693 | 3.5036 | 21.5943 | 0.0073 | 0.0083 |
| 2024_09_20 22:00 | 3220832 | 9 | 12.8640 | 19.9758 | -114.5687 | 4.2453 | 23.0064 | 0.0055 | 0.0187 |
| 2024_09_20 22:00 | 3257239 | 10 | 10.6008 | 18.7715 | -114.4840 | 3.0318 | 39.7785 | 0.0100 | 0.0120 |
| 2024_09_20 22:00 | 3260790 | 11 | 14.2229 | 11.0395 | -115.1420 | 4.2035 | 45.7342 | 0.0191 | 0.0078 |
| 2024_09_20 22:00 | 3270244 | 12 | 11.5205 | 15.9182 | -115.8279 | 3.6261 | 35.8705 | 0.0172 | 0.0091 |
| 2024_09_20 22:00 | 3214064 | 13 | 12.9232 | 12.3583 | -115.2918 | 4.7001 | 31.7522 | 0.0109 | 0.0158 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413448_FCFD453A | 152650 | 688 | -88.8 | 152650 | 930 | -97.1 | 152650 | 590 | -98.4 | 152650 | 298 |
| MR_1774413448_27FE533E | 152650 | 688 | -89.5 | 152650 | 930 | -96.6 | 152650 | 590 | -99.1 | 152650 | 298 |
| MR_1774413448_26DEB7C9 | 504990 | 164 | -94.0 | 504990 | 129 | -91.6 | 504990 | 507 | -97.3 | 504990 | 525 |
| MR_1774413448_C86D34C7 | 504990 | 164 | -94.8 | 504990 | 129 | -91.5 | 504990 | 507 | -97.6 | 504990 | 525 |
| MR_1774413448_B9A3B9A7 | 152650 | 688 | -90.7 | 152650 | 930 | -94.2 | 152650 | 590 | -98.7 | 152650 | 298 |
| MR_1774413448_55DA25B2 | 152650 | 688 | -89.1 | 152650 | 930 | -94.2 | 152650 | 590 | -101.5 | 152650 | 298 |
| MR_1774413448_68AD9A6B | 504990 | 164 | -95.3 | 504990 | 129 | -92.6 | 504990 | 507 | -100.0 | 504990 | 525 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1805: `889c404a-4d1...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `889c404a-4d10-40bb-849f-384c8792f400` |
| Tag | **single-answer** |
| 정답 | **C21** |
| C21 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1805] topology](images/train_1805.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3262639_4 by 10 degrees
- `C2`: Adjust the azimuth of 3262639_4 by 50 degrees
- `C3`: Press down the tilt angle  of 3248138_1 by 3 degrees
- `C4`: Decrease transmission power for 3248138_1
- `C5`: Decrease A3 Offset threshold for 3262639_4
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3248138_1
- `C7`: Press down the tilt angle of 3262639_4 by 10 degrees
- `C8`: Add neighbor relationship between 3262639_4 and 3248138_1
- `C9`: Insufficient data; more data is needed for judgment.
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3262639_4
- `C11`: Decrease A3 Offset threshold for 3248138_1
- `C12`: Increase transmission power for 3248138_1
- `C13`: Add neighbor relationship between 3210083_3 and 3248138_1
- `C14`: Adjust the azimuth of 3248138_1 by 11 degrees
- `C15`: Increase transmission power for 3262639_4
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3248138_1
- `C17`: Lift the tilt angle  of 3248138_1 by 3 degrees
- `C18`: Decrease transmission power for 3262639_4
- `C19`: Increase A3 Offset threshold for 3262639_4
- `C20`: Increase A3 Offset threshold for 3248138_1
- `C21`: Check test server and transmission issues **← 정답**
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3262639_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.981 | MS1 | 121.4656688447 | 31.1446192826 | 413 | 504990 | -91.96 | 17.52 | 486.84 | 0.05 | 2.20 | 1569 |
| 2024-09-20 22:21:32.543 | MS1 | 121.4656706144 | 31.1446280191 | 413 | 504990 | -90.14 | 15.41 | 552.67 | 0.04 | 2.98 | 1575 |
| 2024-09-20 22:21:33.778 | MS1 | 121.4656766405 | 31.1446349314 | 413 | 504990 | -89.28 | 15.34 | 430.21 | 0.03 | 2.97 | 1578 |
| 2024-09-20 22:21:34.423 | MS1 | 121.4656663075 | 31.1446278826 | 413 | 504990 | -86.57 | 14.49 | 90.83 | 0.05 | 2.22 | 442 |
| 2024-09-20 22:21:35.185 | MS1 | 121.4656627216 | 31.1446206632 | 413 | 504990 | -86.31 | 17.22 | 85.84 | 0.11 | 2.49 | 462 |
| 2024-09-20 22:21:36.647 | MS1 | 121.4656667950 | 31.1446242995 | 413 | 504990 | -89.35 | 12.44 | 100.68 | 0.03 | 2.68 | 401 |
| 2024-09-20 22:21:37.440 | MS1 | 121.4656774214 | 31.1446378221 | 413 | 504990 | -92.27 | 10.10 | 93.54 | 0.04 | 2.14 | 493 |
| 2024-09-20 22:21:38.104 | MS1 | 121.4656671033 | 31.1446281261 | 413 | 504990 | -89.30 | 9.36 | 100.22 | 0.04 | 2.98 | 491 |
| 2024-09-20 22:21:39.231 | MS1 | 121.4656580432 | 31.1446365888 | 413 | 504990 | -92.78 | 9.50 | 52.45 | 0.11 | 2.87 | 415 |
| 2024-09-20 22:21:40.793 | MS1 | 121.4656706350 | 31.1446328289 | 413 | 504990 | -91.88 | 9.94 | 541.65 | 0.16 | 2.21 | 1580 |
| 2024-09-20 22:21:41.998 | MS1 | 121.4656634379 | 31.1446371303 | 413 | 504990 | -92.84 | 11.88 | 449.82 | 0.04 | 2.71 | 1587 |
| 2024-09-20 22:21:42.887 | MS1 | 121.4656605212 | 31.1446326827 | 413 | 504990 | -89.55 | 8.13 | 538.57 | 0.13 | 2.36 | 1582 |

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
| 3210083 | 3 | 121.4716070386 | 31.1472618091 | 29 | 9 | 5 | 48.5 | TDD | 435 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3217442 | 2 | 121.4650207456 | 31.1491499098 | 201 | 0 | 3 | 46.1 | TDD | 1 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3248138 | 1 | 121.4725228052 | 31.1539436551 | 201 | 1 | 6 | 41.4 | TDD | 176 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3262639 | 4 | 121.4747413744 | 31.1440752705 | 59 | 14 | 5 | 48.2 | TDD | 413 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |

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
| 2024-09-20 22:21:31.040 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.060 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.184 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.184 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.855 | NREventA3 | measId:2;ServCellPCI:415;Se... |
| 2024-09-20 22:21:38.095 | NRHandoverAttempt | SourcePCI:415;SourceNR-ARFC... |
| 2024-09-20 22:21:38.132 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.145 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.245 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.245 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3248138 | 1 | 7.1310 | 13.9155 | -115.6951 | 17.8515 | 134.6008 | 0.0126 | 0.0051 |
| 2024_09_20 22:00 | 3217442 | 2 | 8.3103 | 15.9002 | -116.1589 | 10.8512 | 187.6981 | 0.0076 | 0.0135 |
| 2024_09_20 22:00 | 3210083 | 3 | 9.0993 | 16.2242 | -116.8602 | 9.2217 | 173.7127 | 0.0062 | 0.0091 |
| 2024_09_20 22:00 | 3262639 | 4 | 13.6054 | 6.4664 | -116.0074 | 10.9301 | 199.3146 | 0.0135 | 0.0110 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414531_B1BF7773 | 504990 | 413 | -85.7 | 504990 | 176 | -94.3 | 504990 | 435 | -93.0 | 504990 | 1 |
| MR_1774414531_6FF4C92A | 504990 | 413 | -87.2 | 504990 | 176 | -92.4 | 504990 | 435 | -93.0 | 504990 | 1 |
| MR_1774414531_FD69B498 | 504990 | 413 | -86.7 | 504990 | 176 | -93.0 | 504990 | 435 | -93.4 | 504990 | 1 |
| MR_1774414531_7C0A9936 | 504990 | 413 | -88.5 | 504990 | 176 | -90.8 | 504990 | 435 | -94.6 | 504990 | 1 |
| MR_1774414531_415CA1A9 | 504990 | 413 | -85.6 | 504990 | 176 | -91.7 | 504990 | 435 | -94.6 | 504990 | 1 |
| MR_1774414531_554D42CD | 504990 | 413 | -88.2 | 504990 | 176 | -93.2 | 504990 | 435 | -91.3 | 504990 | 1 |
| MR_1774414531_65124CFA | 504990 | 413 | -88.5 | 504990 | 176 | -90.8 | 504990 | 435 | -93.2 | 504990 | 1 |
| MR_1774414531_3FAEE360 | 504990 | 413 | -88.1 | 504990 | 176 | -91.4 | 504990 | 435 | -91.6 | 504990 | 1 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1806: `826a3375-4fa...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `826a3375-4fa6-4534-b5ee-98f09b208d9d` |
| Tag | **single-answer** |
| 정답 | **C4** |
| C4 의미 | Lift the tilt angle  of 3248416_4 by 5 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1806] topology](images/train_1806.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Check test server and transmission issues
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3278387_2
- `C3`: Press down the tilt angle  of 3248416_4 by 5 degrees
- `C4`: Lift the tilt angle  of 3248416_4 by 5 degrees **← 정답**
- `C5`: Insufficient data; more data is needed for judgment.
- `C6`: Adjust the azimuth of 3278387_2 by 28 degrees
- `C7`: Decrease transmission power for 3278387_2
- `C8`: Add neighbor relationship between 3248416_4 and 3270967_1
- `C9`: Increase transmission power for 3270967_1
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3270967_1
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3278387_2
- `C12`: Decrease transmission power for 3270967_1
- `C13`: Press down the tilt angle of 3278387_2 by 5 degrees
- `C14`: Decrease A3 Offset threshold for 3278387_2
- `C15`: Adjust the azimuth of 3248416_4 by 50 degrees
- `C16`: Increase A3 Offset threshold for 3270967_1
- `C17`: Add neighbor relationship between 3278387_2 and 3270967_1
- `C18`: Decrease A3 Offset threshold for 3270967_1
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3270967_1
- `C20`: Increase A3 Offset threshold for 3278387_2
- `C21`: Lift the tilt angle of 3278387_2 by 5 degrees
- `C22`: Increase transmission power for 3278387_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.580 | MS1 | 121.4656761901 | 31.1446270586 | 75 | 504990 | -88.07 | 17.22 | 390.52 | 0.10 | 2.62 | 1571 |
| 2024-09-20 22:21:32.914 | MS1 | 121.4656634875 | 31.1446238006 | 75 | 504990 | -85.89 | 14.14 | 313.88 | 0.13 | 2.89 | 1569 |
| 2024-09-20 22:21:33.187 | MS1 | 121.4656600729 | 31.1446375248 | 75 | 504990 | -87.35 | 16.25 | 389.38 | 0.07 | 2.51 | 1594 |
| 2024-09-20 22:21:34.380 | MS1 | 121.4656675741 | 31.1446328023 | 75 | 504990 | -88.04 | 13.09 | 58.04 | 0.05 | 2.38 | 1562 |
| 2024-09-20 22:21:35.514 | MS1 | 121.4656606025 | 31.1446239528 | 75 | 504990 | -85.49 | 17.60 | 81.27 | 0.04 | 2.91 | 1580 |
| 2024-09-20 22:21:36.367 | MS1 | 121.4656657623 | 31.1446316214 | 75 | 504990 | -88.25 | 15.76 | 60.75 | 0.14 | 2.77 | 1590 |
| 2024-09-20 22:21:37.207 | MS1 | 121.4656592604 | 31.1446309689 | 75 | 504990 | -89.78 | 8.41 | 53.49 | 0.06 | 2.04 | 1561 |
| 2024-09-20 22:21:38.124 | MS1 | 121.4656694864 | 31.1446323033 | 75 | 504990 | -89.16 | 11.82 | 89.33 | 0.12 | 2.64 | 1568 |
| 2024-09-20 22:21:39.457 | MS1 | 121.4656603201 | 31.1446248688 | 75 | 504990 | -91.92 | 12.32 | 60.94 | 0.14 | 2.98 | 1581 |
| 2024-09-20 22:21:40.887 | MS1 | 121.4656704359 | 31.1446356524 | 75 | 504990 | -92.18 | 11.21 | 519.34 | 0.06 | 2.59 | 1582 |
| 2024-09-20 22:21:41.774 | MS1 | 121.4656770196 | 31.1446266360 | 75 | 504990 | -89.55 | 9.51 | 531.36 | 0.08 | 2.88 | 1585 |
| 2024-09-20 22:21:42.314 | MS1 | 121.4656608886 | 31.1446268922 | 75 | 504990 | -91.05 | 7.12 | 466.44 | 0.12 | 2.50 | 1590 |

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
| 3240365 | 3 | 121.4646025020 | 31.1501608002 | 11 | 2 | 5 | 39.5 | TDD | 467 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3248416 | 4 | 121.4727097811 | 31.1459416504 | 65 | 6 | 7 | 23.1 | TDD | 119 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3270967 | 1 | 121.4709485061 | 31.1543391921 | 309 | 3 | 0 | 39.6 | TDD | 921 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3278387 | 2 | 121.4722597678 | 31.1513417051 | 192 | 3 | 2 | 37.9 | TDD | 75 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:30.953 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.086 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.086 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.736 | NREventA3 | measId:2;ServCellPCI:824;Se... |
| 2024-09-20 22:21:37.976 | NRHandoverAttempt | SourcePCI:824;SourceNR-ARFC... |
| 2024-09-20 22:21:38.012 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.025 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.140 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.140 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3270967 | 1 | 14.9554 | 16.2326 | -116.1760 | 10.8318 | 112.7711 | 0.0144 | 0.0199 |
| 2024_09_20 22:00 | 3278387 | 2 | 82.1583 | 90.2021 | -114.2178 | 16.3709 | 145.7774 | 0.0188 | 0.0043 |
| 2024_09_20 22:00 | 3240365 | 3 | 14.0903 | 13.3381 | -116.7913 | 13.4515 | 131.3780 | 0.0148 | 0.0145 |
| 2024_09_20 22:00 | 3248416 | 4 | 18.3401 | 15.7545 | -117.2345 | 13.4228 | 122.0214 | 0.0089 | 0.0193 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412382_1AB185DB | 504990 | 75 | -89.1 | 504990 | 921 | -95.0 | 504990 | 119 | -94.0 | 504990 | 467 |
| MR_1774412382_1B501DA7 | 504990 | 75 | -87.7 | 504990 | 921 | -94.6 | 504990 | 119 | -93.9 | 504990 | 467 |
| MR_1774412382_FB66E35A | 504990 | 75 | -87.1 | 504990 | 921 | -95.4 | 504990 | 119 | -93.3 | 504990 | 467 |
| MR_1774412382_57E98D56 | 504990 | 75 | -88.9 | 504990 | 921 | -95.9 | 504990 | 119 | -94.6 | 504990 | 467 |
| MR_1774412382_8B40E436 | 504990 | 75 | -88.3 | 504990 | 921 | -93.0 | 504990 | 119 | -93.2 | 504990 | 467 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1807: `8063d95f-bf8...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `8063d95f-bf8d-463f-a0d3-360ada65290a` |
| Tag | **single-answer** |
| 정답 | **C11** |
| C11 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3218509_2 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1807] topology](images/train_1807.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3218509_2 and 3213579_1
- `C2`: Decrease transmission power for 3218509_2
- `C3`: Adjust the azimuth of 3218509_2 by 49 degrees
- `C4`: Increase transmission power for 3218509_2
- `C5`: Press down the tilt angle of 3218509_2 by 1 degrees
- `C6`: Insufficient data; more data is needed for judgment.
- `C7`: Adjust the azimuth of 3213579_1 by 50 degrees
- `C8`: Decrease A3 Offset threshold for 3218509_2
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3218509_2
- `C10`: Increase transmission power for 3213579_1
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3218509_2 **← 정답**
- `C12`: Lift the tilt angle of 3218509_2 by 1 degrees
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3213579_1
- `C14`: Add neighbor relationship between 3250018_4 and 3213579_1
- `C15`: Press down the tilt angle  of 3213579_1 by 8 degrees
- `C16`: Increase A3 Offset threshold for 3218509_2
- `C17`: Lift the tilt angle  of 3213579_1 by 8 degrees
- `C18`: Decrease A3 Offset threshold for 3213579_1
- `C19`: Decrease transmission power for 3213579_1
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3213579_1
- `C21`: Check test server and transmission issues
- `C22`: Increase A3 Offset threshold for 3213579_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.824 | MS1 | 121.4656602310 | 31.1446351526 | 935 | 504990 | -85.10 | 12.49 | 368.91 | 0.15 | 2.94 | 1576 |
| 2024-09-20 22:21:32.942 | MS1 | 121.4656656611 | 31.1446352533 | 935 | 504990 | -87.63 | 16.66 | 407.56 | 0.07 | 2.95 | 1587 |
| 2024-09-20 22:21:33.352 | MS1 | 121.4656667092 | 31.1446227592 | 935 | 504990 | -91.44 | 13.25 | 532.37 | 0.09 | 2.15 | 1599 |
| 2024-09-20 22:21:34.924 | MS1 | 121.4656723534 | 31.1446365384 | 935 | 504990 | -86.93 | 15.61 | 65.84 | 0.58 | 2.62 | 658 |
| 2024-09-20 22:21:35.972 | MS1 | 121.4656759312 | 31.1446259012 | 935 | 504990 | -85.42 | 12.90 | 71.26 | 0.55 | 2.47 | 630 |
| 2024-09-20 22:21:36.527 | MS1 | 121.4656617674 | 31.1446266711 | 935 | 504990 | -89.45 | 14.38 | 72.23 | 0.59 | 2.02 | 513 |
| 2024-09-20 22:21:37.603 | MS1 | 121.4656710285 | 31.1446330320 | 935 | 504990 | -89.89 | 12.95 | 76.78 | 0.66 | 2.34 | 580 |
| 2024-09-20 22:21:38.444 | MS1 | 121.4656693689 | 31.1446354225 | 935 | 504990 | -89.68 | 7.77 | 103.59 | 0.63 | 2.10 | 528 |
| 2024-09-20 22:21:39.152 | MS1 | 121.4656655232 | 31.1446227023 | 935 | 504990 | -90.40 | 8.63 | 63.14 | 0.52 | 2.30 | 674 |
| 2024-09-20 22:21:40.485 | MS1 | 121.4656641321 | 31.1446346831 | 935 | 504990 | -89.83 | 11.91 | 440.24 | 0.10 | 2.16 | 1574 |
| 2024-09-20 22:21:41.959 | MS1 | 121.4656776566 | 31.1446197959 | 935 | 504990 | -89.50 | 12.73 | 372.08 | 0.19 | 2.19 | 1568 |
| 2024-09-20 22:21:42.427 | MS1 | 121.4656674065 | 31.1446373579 | 935 | 504990 | -91.95 | 12.06 | 445.38 | 0.18 | 2.87 | 1591 |

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
| 3213579 | 1 | 121.4672806111 | 31.1541073856 | 301 | 6 | 1 | 43.2 | TDD | 640 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3218509 | 2 | 121.4753242521 | 31.1450641207 | 218 | 0 | 11 | 18.7 | TDD | 935 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3219200 | 3 | 121.4750427967 | 31.1515663429 | 317 | 13 | 11 | 28.9 | TDD | 922 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3250018 | 4 | 121.4742558367 | 31.1499054971 | 358 | 4 | 5 | 35.7 | TDD | 959 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |

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
| 2024-09-20 22:21:31.041 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.064 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.193 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.193 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.852 | NREventA3 | measId:2;ServCellPCI:939;Se... |
| 2024-09-20 22:21:38.092 | NRHandoverAttempt | SourcePCI:939;SourceNR-ARFC... |
| 2024-09-20 22:21:38.140 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.152 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.294 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.294 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3213579 | 1 | 13.7249 | 7.2495 | -114.7325 | 19.1800 | 174.6966 | 0.0093 | 0.0061 |
| 2024_09_20 22:00 | 3218509 | 2 | 18.8288 | 7.6251 | -115.2701 | 7.5414 | 84.4115 | 0.0041 | 0.0050 |
| 2024_09_20 22:00 | 3219200 | 3 | 5.6117 | 19.4903 | -117.1080 | 15.2962 | 169.9873 | 0.0041 | 0.0137 |
| 2024_09_20 22:00 | 3250018 | 4 | 11.7641 | 8.3084 | -114.8151 | 12.7562 | 104.1909 | 0.0004 | 0.0096 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414273_EE2C5769 | 504990 | 935 | -88.0 | 504990 | 640 | -92.7 | 504990 | 959 | -97.8 | 504990 | 922 |
| MR_1774414273_D43BF69D | 504990 | 935 | -87.9 | 504990 | 640 | -94.4 | 504990 | 959 | -94.8 | 504990 | 922 |
| MR_1774414273_FA19B056 | 504990 | 935 | -88.2 | 504990 | 640 | -93.3 | 504990 | 959 | -96.7 | 504990 | 922 |
| MR_1774414273_C1F3A3D0 | 504990 | 935 | -86.2 | 504990 | 640 | -91.3 | 504990 | 959 | -96.9 | 504990 | 922 |
| MR_1774414273_FCC3B7A3 | 504990 | 935 | -86.6 | 504990 | 640 | -91.3 | 504990 | 959 | -96.5 | 504990 | 922 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1808: `8b429021-ae2...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `8b429021-ae22-428f-9b2c-80697a137b4d` |
| Tag | **multiple-answer** |
| 정답 | **C5|C10** |
| C5 의미 | Decrease transmission power for 3255244_2 |
| C10 의미 | Press down the tilt angle  of 3255244_2 by 4 degrees |
| 패턴 분류 | **P3 Overshoot (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1808] topology](images/train_1808.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3255244_2
- `C2`: Increase transmission power for 3244723_1
- `C3`: Press down the tilt angle of 3244723_1 by 5 degrees
- `C4`: Adjust the azimuth of 3255244_2 by 18 degrees
- `C5`: Decrease transmission power for 3255244_2 **← 정답**
- `C6`: Increase A3 Offset threshold for 3255244_2
- `C7`: Lift the tilt angle of 3244723_1 by 5 degrees
- `C8`: Adjust the azimuth of 3244723_1 by 43 degrees
- `C9`: Check test server and transmission issues
- `C10`: Press down the tilt angle  of 3255244_2 by 4 degrees **← 정답**
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3255244_2
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3244723_1
- `C13`: Add neighbor relationship between 3233704_4 and 3255244_2
- `C14`: Increase A3 Offset threshold for 3244723_1
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3244723_1
- `C16`: Decrease transmission power for 3244723_1
- `C17`: Insufficient data; more data is needed for judgment.
- `C18`: Add neighbor relationship between 3244723_1 and 3255244_2
- `C19`: Decrease A3 Offset threshold for 3255244_2
- `C20`: Increase transmission power for 3255244_2
- `C21`: Lift the tilt angle  of 3255244_2 by 4 degrees
- `C22`: Decrease A3 Offset threshold for 3244723_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.349 | MS1 | 121.4656680039 | 31.1446197281 | 218 | 504990 | -76.27 | 17.95 | 336.03 | 0.06 | 2.06 | 1590 |
| 2024-09-20 22:21:32.556 | MS1 | 121.4656641745 | 31.1446325070 | 218 | 504990 | -77.17 | 17.96 | 465.59 | 0.06 | 2.39 | 1581 |
| 2024-09-20 22:21:33.308 | MS1 | 121.4656598596 | 31.1446203706 | 218 | 504990 | -84.44 | 16.53 | 356.22 | 0.04 | 2.83 | 1583 |
| 2024-09-20 22:21:34.468 | MS1 | 121.4656614581 | 31.1446266732 | 218 | 504990 | -92.75 | 2.43 | 61.04 | 0.03 | 1.12 | 1585 |
| 2024-09-20 22:21:35.745 | MS1 | 121.4656634020 | 31.1446228417 | 218 | 504990 | -92.67 | 2.48 | 64.14 | 0.03 | 1.28 | 1575 |
| 2024-09-20 22:21:36.871 | MS1 | 121.4656613308 | 31.1446309009 | 218 | 504990 | -93.17 | 1.04 | 70.47 | 0.06 | 1.37 | 1588 |
| 2024-09-20 22:21:37.633 | MS1 | 121.4656769673 | 31.1446313141 | 218 | 504990 | -89.29 | 0.76 | 60.87 | 0.18 | 1.41 | 1579 |
| 2024-09-20 22:21:38.910 | MS1 | 121.4656708695 | 31.1446224646 | 218 | 504990 | -94.09 | 2.76 | 75.98 | 0.15 | 1.43 | 1575 |
| 2024-09-20 22:21:39.909 | MS1 | 121.4656623733 | 31.1446372787 | 218 | 504990 | -87.26 | 3.79 | 55.38 | 0.03 | 1.17 | 1591 |
| 2024-09-20 22:21:40.532 | MS1 | 121.4656729720 | 31.1446306927 | 218 | 504990 | -80.47 | 14.29 | 447.80 | 0.13 | 2.07 | 1576 |
| 2024-09-20 22:21:41.801 | MS1 | 121.4656643443 | 31.1446243922 | 218 | 504990 | -84.86 | 13.99 | 332.92 | 0.18 | 2.06 | 1593 |
| 2024-09-20 22:21:42.591 | MS1 | 121.4656776136 | 31.1446196508 | 218 | 504990 | -81.13 | 16.76 | 406.29 | 0.17 | 2.57 | 1579 |

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
| 3233704 | 4 | 121.4643001870 | 31.1501291974 | 347 | 3 | 3 | 44.8 | TDD | 844 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3244723 | 1 | 121.4716160909 | 31.1485019166 | 190 | 2 | 3 | 32.0 | TDD | 218 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3251711 | 3 | 121.4723138877 | 31.1499194618 | 127 | 12 | 10 | 19.2 | TDD | 932 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3255244 | 2 | 121.4690059238 | 31.1526360788 | 182 | 1 | 0 | 45.7 | TDD | 139 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |

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
| 2024-09-20 22:21:31.496 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.629 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.629 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3244723 | 1 | 18.0236 | 13.1251 | -108.7705 | 15.7341 | 135.3131 | 0.0086 | 0.0006 |
| 2024_09_20 22:00 | 3255244 | 2 | 5.1646 | 12.6326 | -117.7718 | 18.5612 | 161.7789 | 0.0054 | 0.0018 |
| 2024_09_20 22:00 | 3251711 | 3 | 18.8678 | 11.9991 | -114.4112 | 6.6529 | 174.5919 | 0.0110 | 0.0002 |
| 2024_09_20 22:00 | 3233704 | 4 | 13.5010 | 6.6974 | -116.8812 | 9.7876 | 125.4751 | 0.0191 | 0.0003 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415431_9708EEDD | 504990 | 139 | -92.0 | 504990 | 218 | -88.0 | 504990 | 844 | -93.0 | 504990 | 932 |
| MR_1774415431_D68F2EB5 | 504990 | 218 | -93.0 | 504990 | 139 | -89.6 | 504990 | 844 | -94.8 | 504990 | 932 |
| MR_1774415431_8286F8BD | 504990 | 139 | -93.7 | 504990 | 218 | -88.0 | 504990 | 844 | -91.5 | 504990 | 932 |
| MR_1774415431_5DCF40BF | 504990 | 218 | -93.6 | 504990 | 139 | -88.3 | 504990 | 844 | -94.7 | 504990 | 932 |
| MR_1774415431_CADB0212 | 504990 | 139 | -92.9 | 504990 | 218 | -89.5 | 504990 | 844 | -94.6 | 504990 | 932 |
| MR_1774415431_738684CC | 504990 | 139 | -94.5 | 504990 | 218 | -91.2 | 504990 | 844 | -91.6 | 504990 | 932 |
| MR_1774415431_90B153D7 | 504990 | 139 | -91.8 | 504990 | 218 | -88.9 | 504990 | 844 | -93.9 | 504990 | 932 |
| MR_1774415431_E72B4607 | 504990 | 218 | -92.5 | 504990 | 139 | -87.4 | 504990 | 844 | -92.5 | 504990 | 932 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1809: `0017e56b-064...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `0017e56b-0648-4d4d-8b1b-7d4d267e1a92` |
| Tag | **single-answer** |
| 정답 | **C9** |
| C9 의미 | Lift the tilt angle  of 3218344_4 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1809] topology](images/train_1809.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease A3 Offset threshold for 3276647_2
- `C2`: Press down the tilt angle  of 3218344_4 by 10 degrees
- `C3`: Decrease A3 Offset threshold for 3210730_1
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3276647_2
- `C5`: Adjust the azimuth of 3218344_4 by 50 degrees
- `C6`: Add neighbor relationship between 3210730_1 and 3276647_2
- `C7`: Press down the tilt angle of 3210730_1 by 4 degrees
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3210730_1
- `C9`: Lift the tilt angle  of 3218344_4 by 10 degrees **← 정답**
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3210730_1
- `C11`: Decrease transmission power for 3210730_1
- `C12`: Increase A3 Offset threshold for 3210730_1
- `C13`: Increase transmission power for 3210730_1
- `C14`: Increase A3 Offset threshold for 3276647_2
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3276647_2
- `C16`: Increase transmission power for 3276647_2
- `C17`: Add neighbor relationship between 3218344_4 and 3276647_2
- `C18`: Insufficient data; more data is needed for judgment.
- `C19`: Decrease transmission power for 3276647_2
- `C20`: Check test server and transmission issues
- `C21`: Lift the tilt angle of 3210730_1 by 4 degrees
- `C22`: Adjust the azimuth of 3210730_1 by 41 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.372 | MS1 | 121.4656627486 | 31.1446253893 | 72 | 504990 | -89.87 | 13.20 | 449.24 | 0.05 | 2.65 | 1578 |
| 2024-09-20 22:21:32.756 | MS1 | 121.4656612249 | 31.1446214712 | 72 | 504990 | -90.32 | 16.91 | 457.48 | 0.05 | 2.59 | 1589 |
| 2024-09-20 22:21:33.786 | MS1 | 121.4656703156 | 31.1446228228 | 72 | 504990 | -90.64 | 17.97 | 557.75 | 0.12 | 2.95 | 1569 |
| 2024-09-20 22:21:34.590 | MS1 | 121.4656582182 | 31.1446214907 | 72 | 504990 | -91.98 | 14.98 | 83.38 | 0.02 | 2.95 | 1580 |
| 2024-09-20 22:21:35.195 | MS1 | 121.4656665725 | 31.1446301717 | 72 | 504990 | -85.44 | 13.72 | 67.17 | 0.07 | 2.83 | 1585 |
| 2024-09-20 22:21:36.966 | MS1 | 121.4656609991 | 31.1446307661 | 72 | 504990 | -85.06 | 15.87 | 53.19 | 0.12 | 2.91 | 1590 |
| 2024-09-20 22:21:37.444 | MS1 | 121.4656649420 | 31.1446330183 | 72 | 504990 | -89.83 | 11.39 | 63.67 | 0.17 | 2.16 | 1566 |
| 2024-09-20 22:21:38.412 | MS1 | 121.4656715257 | 31.1446358184 | 72 | 504990 | -89.88 | 7.86 | 103.76 | 0.00 | 2.80 | 1572 |
| 2024-09-20 22:21:39.900 | MS1 | 121.4656766582 | 31.1446193750 | 72 | 504990 | -89.15 | 10.91 | 84.63 | 0.18 | 2.37 | 1584 |
| 2024-09-20 22:21:40.487 | MS1 | 121.4656616913 | 31.1446291815 | 72 | 504990 | -89.42 | 9.68 | 554.10 | 0.10 | 2.88 | 1578 |
| 2024-09-20 22:21:41.234 | MS1 | 121.4656649878 | 31.1446344290 | 72 | 504990 | -91.00 | 7.51 | 560.55 | 0.17 | 2.91 | 1561 |
| 2024-09-20 22:21:42.159 | MS1 | 121.4656598543 | 31.1446366614 | 72 | 504990 | -89.57 | 9.43 | 503.12 | 0.07 | 2.86 | 1596 |

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
| 3210730 | 1 | 121.4744774483 | 31.1503055510 | 274 | 3 | 4 | 16.8 | TDD | 72 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3218344 | 4 | 121.4728063327 | 31.1496515746 | 73 | 3 | 0 | 26.9 | TDD | 295 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3269967 | 3 | 121.4684278244 | 31.1503642696 | 77 | 10 | 11 | 38.5 | TDD | 520 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3276647 | 2 | 121.4682296420 | 31.1463836718 | 139 | 11 | 3 | 24.6 | TDD | 441 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |

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
| 2024-09-20 22:21:30.890 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.908 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.057 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.057 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.754 | NREventA3 | measId:2;ServCellPCI:395;Se... |
| 2024-09-20 22:21:37.994 | NRHandoverAttempt | SourcePCI:395;SourceNR-ARFC... |
| 2024-09-20 22:21:38.029 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.041 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.181 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.181 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3210730 | 1 | 83.5890 | 75.2529 | -117.0166 | 16.2337 | 149.6285 | 0.0116 | 0.0118 |
| 2024_09_20 22:00 | 3276647 | 2 | 17.4650 | 13.2667 | -115.1766 | 14.9984 | 84.4668 | 0.0118 | 0.0066 |
| 2024_09_20 22:00 | 3269967 | 3 | 10.0584 | 8.5992 | -115.7675 | 16.9890 | 191.0756 | 0.0163 | 0.0001 |
| 2024_09_20 22:00 | 3218344 | 4 | 13.7671 | 18.9066 | -114.7078 | 15.3828 | 193.9163 | 0.0081 | 0.0102 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414624_191076A4 | 504990 | 72 | -90.7 | 504990 | 441 | -90.2 | 504990 | 295 | -103.0 | 504990 | 520 |
| MR_1774414624_D13E1196 | 504990 | 72 | -92.1 | 504990 | 441 | -91.0 | 504990 | 295 | -103.2 | 504990 | 520 |
| MR_1774414624_26A1BAC0 | 504990 | 72 | -91.5 | 504990 | 441 | -91.0 | 504990 | 295 | -100.9 | 504990 | 520 |
| MR_1774414624_848CFC62 | 504990 | 72 | -92.7 | 504990 | 441 | -92.9 | 504990 | 295 | -103.6 | 504990 | 520 |
| MR_1774414624_40D541CB | 504990 | 72 | -90.5 | 504990 | 441 | -93.2 | 504990 | 295 | -100.8 | 504990 | 520 |
| MR_1774414624_470CE129 | 504990 | 72 | -93.1 | 504990 | 441 | -91.3 | 504990 | 295 | -101.5 | 504990 | 520 |

> *... 2개 열 생략 (전체 14열)*

---
