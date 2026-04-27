# Track A 문제 분석 — train[690]~train[699]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[690] ~ train[699] (10개)

## 목차

1. [문제 690: `585e6e32-463...`](#690) — single-answer, 정답: C22
2. [문제 691: `9a93ea7a-06a...`](#691) — single-answer, 정답: C4
3. [문제 692: `aa47177e-604...`](#692) — single-answer, 정답: C15
4. [문제 693: `4efb4f23-4f1...`](#693) — multiple-answer, 정답: C15|C20
5. [문제 694: `29f11787-3c9...`](#694) — single-answer, 정답: C10
6. [문제 695: `47054714-214...`](#695) — single-answer, 정답: C11
7. [문제 696: `7d9a4f6e-5b7...`](#696) — single-answer, 정답: C13
8. [문제 697: `322fb4fb-951...`](#697) — single-answer, 정답: C18
9. [문제 698: `fdc69ca8-162...`](#698) — single-answer, 정답: C15
10. [문제 699: `416a5366-8e5...`](#699) — multiple-answer, 정답: C5|C11|C13|C19

---

### 문제 690: `585e6e32-463...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `585e6e32-4635-4dda-9e50-96300b1b4a5d` |
| Tag | **single-answer** |
| 정답 | **C22** |
| C22 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[690] topology](images/train_0690.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3213018_3 by 44 degrees
- `C2`: Press down the tilt angle  of 3244058_4 by 10 degrees
- `C3`: Increase A3 Offset threshold for 3213018_3
- `C4`: Increase transmission power for 3213018_3
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3244058_4
- `C6`: Lift the tilt angle  of 3244058_4 by 10 degrees
- `C7`: Add neighbor relationship between 3213018_3 and 3244058_4
- `C8`: Lift the tilt angle of 3213018_3 by 10 degrees
- `C9`: Adjust the azimuth of 3244058_4 by 50 degrees
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3213018_3
- `C11`: Decrease A3 Offset threshold for 3244058_4
- `C12`: Decrease A3 Offset threshold for 3213018_3
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3244058_4
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3213018_3
- `C15`: Press down the tilt angle of 3213018_3 by 10 degrees
- `C16`: Increase A3 Offset threshold for 3244058_4
- `C17`: Decrease transmission power for 3213018_3
- `C18`: Decrease transmission power for 3244058_4
- `C19`: Check test server and transmission issues
- `C20`: Increase transmission power for 3244058_4
- `C21`: Add neighbor relationship between 3238840_1 and 3244058_4
- `C22`: Insufficient data; more data is needed for judgment. **← 정답**

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.639 | MS1 | 121.4656778233 | 31.1446297556 | 1005 | 504990 | -88.62 | 12.96 | 573.38 | 0.11 | 2.91 | 1561 |
| 2024-09-20 22:21:32.735 | MS1 | 121.4656751669 | 31.1446305964 | 1005 | 504990 | -87.22 | 16.84 | 437.81 | 0.11 | 2.77 | 1588 |
| 2024-09-20 22:21:33.790 | MS1 | 121.4656774895 | 31.1446195711 | 1005 | 504990 | -86.04 | 16.44 | 589.44 | 0.01 | 2.67 | 1593 |
| 2024-09-20 22:21:34.563 | MS1 | 121.4656680960 | 31.1446231250 | 1005 | 504990 | -87.88 | 14.61 | 98.47 | 0.00 | 2.07 | 1566 |
| 2024-09-20 22:21:35.100 | MS1 | 121.4656662116 | 31.1446191962 | 1005 | 504990 | -88.28 | 13.16 | 94.34 | 0.07 | 2.41 | 1573 |
| 2024-09-20 22:21:36.696 | MS1 | 121.4656596211 | 31.1446204057 | 1005 | 504990 | -90.09 | 14.82 | 82.20 | 0.09 | 2.59 | 1575 |
| 2024-09-20 22:21:37.501 | MS1 | 121.4656714567 | 31.1446246615 | 1005 | 504990 | -92.50 | 11.04 | 82.83 | 0.08 | 2.47 | 1587 |
| 2024-09-20 22:21:38.688 | MS1 | 121.4656775475 | 31.1446214602 | 1005 | 504990 | -91.08 | 10.09 | 54.32 | 0.17 | 2.98 | 1595 |
| 2024-09-20 22:21:39.343 | MS1 | 121.4656693734 | 31.1446223702 | 1005 | 504990 | -91.52 | 12.50 | 57.12 | 0.06 | 2.02 | 1588 |
| 2024-09-20 22:21:40.668 | MS1 | 121.4656686843 | 31.1446270805 | 1005 | 504990 | -90.03 | 12.65 | 475.88 | 0.17 | 2.47 | 1592 |
| 2024-09-20 22:21:41.613 | MS1 | 121.4656614350 | 31.1446273167 | 1005 | 504990 | -92.36 | 8.17 | 525.34 | 0.01 | 2.12 | 1596 |
| 2024-09-20 22:21:42.985 | MS1 | 121.4656673464 | 31.1446244388 | 1005 | 504990 | -92.38 | 10.03 | 354.41 | 0.05 | 2.80 | 1564 |

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
| 3213018 | 3 | 121.4741855887 | 31.1496924107 | 191 | 10 | 10 | 25.6 | TDD | 1005 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3233032 | 2 | 121.4748340727 | 31.1528150634 | 222 | 4 | 6 | 44.5 | TDD | 697 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3238840 | 1 | 121.4716091871 | 31.1534663211 | 270 | 5 | 10 | 20.9 | TDD | 592 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3244058 | 4 | 121.4657569344 | 31.1516155021 | 104 | 15 | 4 | 31.5 | TDD | 358 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |

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
| 2024-09-20 22:21:30.932 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.948 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.097 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.097 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.732 | NREventA3 | measId:2;ServCellPCI:894;Se... |
| 2024-09-20 22:21:37.972 | NRHandoverAttempt | SourcePCI:894;SourceNR-ARFC... |
| 2024-09-20 22:21:38.011 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.023 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.167 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.167 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3238840 | 1 | 76.2612 | 88.8886 | -116.0035 | 17.1406 | 148.1716 | 0.0097 | 0.0098 |
| 2024_09_19 22:00 | 3233032 | 2 | 77.2913 | 94.9818 | -116.8732 | 14.3755 | 93.9912 | 0.0020 | 0.0021 |
| 2024_09_19 22:00 | 3213018 | 3 | 88.8129 | 90.8383 | -116.2312 | 17.4614 | 150.1936 | 0.0180 | 0.0140 |
| 2024_09_19 22:00 | 3244058 | 4 | 81.8596 | 77.8365 | -117.6294 | 17.6280 | 197.1243 | 0.0048 | 0.0196 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413617_B6E2BA34 | 504990 | 1005 | -86.4 | 504990 | 358 | -90.6 | 504990 | 592 | -93.7 | 504990 | 697 |
| MR_1774413617_84F3B8FE | 504990 | 1005 | -88.3 | 504990 | 358 | -90.1 | 504990 | 592 | -93.1 | 504990 | 697 |
| MR_1774413617_A21535F9 | 504990 | 1005 | -87.9 | 504990 | 358 | -93.4 | 504990 | 592 | -95.8 | 504990 | 697 |
| MR_1774413617_8343D0FC | 504990 | 1005 | -86.0 | 504990 | 358 | -92.7 | 504990 | 592 | -93.7 | 504990 | 697 |
| MR_1774413617_9DF31B63 | 504990 | 1005 | -88.4 | 504990 | 358 | -92.2 | 504990 | 592 | -92.8 | 504990 | 697 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 691: `9a93ea7a-06a...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `9a93ea7a-06a5-4cd3-a978-52340f4f7694` |
| Tag | **single-answer** |
| 정답 | **C4** |
| C4 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3276642_1 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[691] topology](images/train_0691.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3212419_2
- `C2`: Press down the tilt angle of 3276642_1 by 4 degrees
- `C3`: Decrease transmission power for 3276642_1
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3276642_1 **← 정답**
- `C5`: Adjust the azimuth of 3276642_1 by 24 degrees
- `C6`: Add neighbor relationship between 3252470_3 and 3212419_2
- `C7`: Lift the tilt angle  of 3212419_2 by 1 degrees
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3276642_1
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3212419_2
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3212419_2
- `C11`: Increase A3 Offset threshold for 3276642_1
- `C12`: Add neighbor relationship between 3276642_1 and 3212419_2
- `C13`: Decrease A3 Offset threshold for 3212419_2
- `C14`: Check test server and transmission issues
- `C15`: Decrease transmission power for 3212419_2
- `C16`: Decrease A3 Offset threshold for 3276642_1
- `C17`: Increase transmission power for 3276642_1
- `C18`: Lift the tilt angle of 3276642_1 by 4 degrees
- `C19`: Increase A3 Offset threshold for 3212419_2
- `C20`: Adjust the azimuth of 3212419_2 by 50 degrees
- `C21`: Press down the tilt angle  of 3212419_2 by 1 degrees
- `C22`: Insufficient data; more data is needed for judgment.

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.327 | MS1 | 121.4656770996 | 31.1446266675 | 584 | 504990 | -86.48 | 15.63 | 534.75 | 0.15 | 2.22 | 1567 |
| 2024-09-20 22:21:32.102 | MS1 | 121.4656697366 | 31.1446205915 | 584 | 504990 | -85.23 | 12.58 | 583.92 | 0.19 | 2.72 | 1570 |
| 2024-09-20 22:21:33.374 | MS1 | 121.4656703125 | 31.1446250369 | 584 | 504990 | -90.43 | 17.68 | 383.15 | 0.14 | 2.46 | 1580 |
| 2024-09-20 22:21:34.998 | MS1 | 121.4656750178 | 31.1446250554 | 584 | 504990 | -89.40 | 13.17 | 78.37 | 0.55 | 2.99 | 581 |
| 2024-09-20 22:21:35.266 | MS1 | 121.4656658611 | 31.1446374355 | 584 | 504990 | -90.55 | 12.06 | 68.58 | 0.63 | 2.76 | 540 |
| 2024-09-20 22:21:36.661 | MS1 | 121.4656617619 | 31.1446228865 | 584 | 504990 | -89.88 | 12.14 | 95.93 | 0.51 | 2.91 | 599 |
| 2024-09-20 22:21:37.357 | MS1 | 121.4656635891 | 31.1446226324 | 584 | 504990 | -89.89 | 10.97 | 98.18 | 0.67 | 2.96 | 607 |
| 2024-09-20 22:21:38.566 | MS1 | 121.4656643135 | 31.1446336193 | 584 | 504990 | -92.18 | 11.03 | 85.80 | 0.70 | 2.28 | 675 |
| 2024-09-20 22:21:39.415 | MS1 | 121.4656674597 | 31.1446275936 | 584 | 504990 | -93.88 | 10.26 | 88.19 | 0.68 | 2.46 | 563 |
| 2024-09-20 22:21:40.520 | MS1 | 121.4656726710 | 31.1446334425 | 584 | 504990 | -89.68 | 7.54 | 353.34 | 0.18 | 2.46 | 1569 |
| 2024-09-20 22:21:41.393 | MS1 | 121.4656759507 | 31.1446319509 | 584 | 504990 | -90.17 | 10.32 | 491.67 | 0.12 | 2.50 | 1587 |
| 2024-09-20 22:21:42.944 | MS1 | 121.4656665301 | 31.1446199567 | 584 | 504990 | -91.19 | 12.63 | 364.77 | 0.04 | 2.88 | 1584 |

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
| 3212419 | 2 | 121.4657992224 | 31.1549297833 | 18 | 0 | 2 | 15.2 | TDD | 334 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3244188 | 4 | 121.4722436372 | 31.1484147109 | 134 | 4 | 2 | 42.7 | TDD | 814 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3252470 | 3 | 121.4736284988 | 31.1533342953 | 33 | 9 | 7 | 37.3 | TDD | 948 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3276642 | 1 | 121.4682408220 | 31.1503464751 | 225 | 2 | 12 | 21.1 | TDD | 584 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

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
| 2024-09-20 22:21:31.326 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.346 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.471 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.471 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.190 | NREventA3 | measId:2;ServCellPCI:679;Se... |
| 2024-09-20 22:21:38.430 | NRHandoverAttempt | SourcePCI:679;SourceNR-ARFC... |
| 2024-09-20 22:21:38.463 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.475 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.581 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.581 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3276642 | 1 | 5.4265 | 9.3557 | -115.4714 | 19.9743 | 199.1189 | 0.0138 | 0.0159 |
| 2024_09_20 22:00 | 3212419 | 2 | 5.5591 | 14.1486 | -116.5696 | 9.2777 | 143.9616 | 0.0048 | 0.0141 |
| 2024_09_20 22:00 | 3252470 | 3 | 12.2749 | 17.7047 | -116.5579 | 8.5629 | 154.5263 | 0.0196 | 0.0178 |
| 2024_09_20 22:00 | 3244188 | 4 | 6.8653 | 18.8665 | -114.2448 | 12.5378 | 185.4270 | 0.0003 | 0.0083 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417034_D19BFCC2 | 504990 | 584 | -87.5 | 504990 | 334 | -93.2 | 504990 | 948 | -94.8 | 504990 | 814 |
| MR_1774417034_58C2B9F1 | 504990 | 584 | -89.3 | 504990 | 334 | -91.1 | 504990 | 948 | -96.5 | 504990 | 814 |
| MR_1774417034_4013FFE2 | 504990 | 584 | -88.1 | 504990 | 334 | -94.2 | 504990 | 948 | -98.7 | 504990 | 814 |
| MR_1774417034_1AAA36AD | 504990 | 584 | -91.2 | 504990 | 334 | -93.8 | 504990 | 948 | -94.8 | 504990 | 814 |
| MR_1774417034_E17E009A | 504990 | 584 | -89.0 | 504990 | 334 | -92.3 | 504990 | 948 | -97.0 | 504990 | 814 |
| MR_1774417034_E1AC56A3 | 504990 | 584 | -88.9 | 504990 | 334 | -91.3 | 504990 | 948 | -95.4 | 504990 | 814 |
| MR_1774417034_34D7BB5C | 504990 | 584 | -91.1 | 504990 | 334 | -91.6 | 504990 | 948 | -97.6 | 504990 | 814 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 692: `aa47177e-604...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `aa47177e-6042-4ba2-8bea-a47e98e48bff` |
| Tag | **single-answer** |
| 정답 | **C15** |
| C15 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3273029_5 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[692] topology](images/train_0692.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3273029_5
- `C2`: Press down the tilt angle  of 3239351_6 by 1 degrees
- `C3`: Decrease A3 Offset threshold for 3239351_6
- `C4`: Increase transmission power for 3273029_5
- `C5`: Insufficient data; more data is needed for judgment.
- `C6`: Decrease transmission power for 3273029_5
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3239351_6
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3273029_5
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3239351_6
- `C10`: Adjust the azimuth of 3273029_5 by 48 degrees
- `C11`: Press down the tilt angle of 3273029_5 by 0 degrees
- `C12`: Lift the tilt angle of 3273029_5 by 0 degrees
- `C13`: Increase transmission power for 3239351_6
- `C14`: Increase A3 Offset threshold for 3239351_6
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3273029_5 **← 정답**
- `C16`: Decrease A3 Offset threshold for 3273029_5
- `C17`: Adjust the azimuth of 3239351_6 by 43 degrees
- `C18`: Add neighbor relationship between 3270082_13 and 3239351_6
- `C19`: Lift the tilt angle  of 3239351_6 by 1 degrees
- `C20`: Decrease transmission power for 3239351_6
- `C21`: Check test server and transmission issues
- `C22`: Add neighbor relationship between 3273029_5 and 3239351_6

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.840 | MS1 | 121.4656713323 | 31.1446284491 | 948 | 504990 | -93.93 | 13.17 | 436.01 | 0.20 | 2.15 | 1595 |
| 2024-09-20 22:21:32.509 | MS1 | 121.4656735711 | 31.1446375293 | 967 | 504990 | -95.56 | 12.57 | 487.27 | 0.05 | 2.74 | 1563 |
| 2024-09-20 22:21:33.241 | MS1 | 121.4656771572 | 31.1446329483 | 654 | 504990 | -95.38 | 11.66 | 481.59 | 0.01 | 2.87 | 1582 |
| 2024-09-20 22:21:34.623 | MS1 | 121.4656688876 | 31.1446204469 | 384 | 152650 | -93.62 | 6.60 | 78.77 | 0.01 | 1.73 | 944 |
| 2024-09-20 22:21:35.490 | MS1 | 121.4656763041 | 31.1446192931 | 47 | 152650 | -91.37 | 6.31 | 67.27 | 0.12 | 1.60 | 966 |
| 2024-09-20 22:21:36.486 | MS1 | 121.4656729017 | 31.1446337080 | 671 | 152650 | -92.52 | 6.86 | 75.17 | 0.13 | 1.94 | 941 |
| 2024-09-20 22:21:37.774 | MS1 | 121.4656761211 | 31.1446207795 | 740 | 152650 | -87.20 | 4.65 | 79.52 | 0.19 | 1.82 | 996 |
| 2024-09-20 22:21:38.412 | MS1 | 121.4656725378 | 31.1446357387 | 384 | 152650 | -91.65 | 6.14 | 66.58 | 0.18 | 1.84 | 991 |
| 2024-09-20 22:21:39.542 | MS1 | 121.4656585892 | 31.1446183835 | 47 | 152650 | -87.85 | 3.46 | 64.83 | 0.06 | 1.53 | 976 |
| 2024-09-20 22:21:40.963 | MS1 | 121.4656682871 | 31.1446323849 | 671 | 152650 | -89.61 | 7.28 | 97.25 | 0.13 | 2.47 | 1582 |
| 2024-09-20 22:21:41.730 | MS1 | 121.4656771368 | 31.1446219609 | 740 | 152650 | -87.26 | 3.71 | 80.28 | 0.06 | 2.39 | 1568 |
| 2024-09-20 22:21:42.919 | MS1 | 121.4656631119 | 31.1446229826 | 384 | 152650 | -96.58 | 2.31 | 68.60 | 0.08 | 2.45 | 1577 |

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
| 3211647 | 12 | 121.4735417804 | 31.1544135587 | 138 | 4 | 12 | 27.4 | FDD | 24 | n1 | 152650 | 30M | 4T4R | 19 | 152650 |
| 3211723 | 8 | 121.4645742637 | 31.1553941724 | 334 | 12 | 9 | 13.1 | FDD | 740 | n1 | 152650 | 30M | 4T4R | 17 | 152650 |
| 3223526 | 2 | 121.4672640338 | 31.1479830962 | 242 | 11 | 0 | 21.4 | TDD | 39 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3230817 | 1 | 121.4656600811 | 31.1479466989 | 186 | 6 | 9 | 16.8 | TDD | 70 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3231729 | 11 | 121.4711040512 | 31.1498243029 | 55 | 5 | 8 | 9.4 | FDD | 22 | n1 | 152650 | 30M | 4T4R | 21 | 152650 |
| 3239351 | 6 | 121.4712801882 | 31.1554091855 | 247 | 0 | 0 | 12.0 | TDD | 566 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3242331 | 9 | 121.4671557865 | 31.1507272187 | 195 | 0 | 8 | 23.2 | FDD | 652 | n1 | 152650 | 30M | 4T4R | 30 | 152650 |
| 3265049 | 7 | 121.4648781705 | 31.1495869834 | 324 | 14 | 9 | 25.8 | FDD | 384 | n1 | 152650 | 30M | 4T4R | 19 | 152650 |
| 3266533 | 3 | 121.4719792412 | 31.1453923945 | 71 | 10 | 7 | 18.3 | TDD | 967 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3267100 | 4 | 121.4711060477 | 31.1524353107 | 306 | 10 | 12 | 1.4 | TDD | 654 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3267516 | 10 | 121.4666113013 | 31.1533621075 | 163 | 1 | 2 | 18.9 | FDD | 47 | n1 | 152650 | 30M | 4T4R | 12 | 152650 |
| 3270082 | 13 | 121.4646747762 | 31.1482491899 | 295 | 4 | 10 | 9.5 | FDD | 671 | n1 | 152650 | 30M | 4T4R | 13 | 152650 |
| 3273029 | 5 | 121.4710446387 | 31.1541983649 | 158 | 0 | 7 | 4.2 | TDD | 948 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |

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
| 2024-09-20 22:21:31.311 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.335 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.452 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.452 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.171 | NREventA2 | measId:1;ServCellPCI:518;Se... |
| 2024-09-20 22:21:35.295 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.552 | NREventA5 | measId:3;ServCellPCI:518;Se... |
| 2024-09-20 22:21:35.595 | NRHandoverAttempt | SourcePCI:518;SourceNR-ARFC... |
| 2024-09-20 22:21:35.624 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.636 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:35.774 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.774 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3230817 | 1 | 11.1586 | 13.9329 | -116.1051 | 15.7226 | 195.2547 | 0.0033 | 0.0099 |
| 2024_09_20 22:00 | 3223526 | 2 | 14.0651 | 18.6417 | -114.0301 | 18.9696 | 115.8227 | 0.0037 | 0.0058 |
| 2024_09_20 22:00 | 3266533 | 3 | 9.5274 | 12.6713 | -115.2005 | 14.5349 | 133.7558 | 0.0053 | 0.0135 |
| 2024_09_20 22:00 | 3267100 | 4 | 5.0547 | 9.7943 | -116.7404 | 7.9582 | 120.6075 | 0.0176 | 0.0036 |
| 2024_09_20 22:00 | 3273029 | 5 | 9.3317 | 5.9686 | -114.6744 | 6.9662 | 141.5366 | 0.0185 | 0.0159 |
| 2024_09_20 22:00 | 3239351 | 6 | 10.7485 | 16.3942 | -114.1578 | 7.5549 | 102.6927 | 0.0106 | 0.0015 |
| 2024_09_20 22:00 | 3265049 | 7 | 9.2339 | 17.0110 | -116.9313 | 3.4388 | 26.0508 | 0.0000 | 0.0056 |
| 2024_09_20 22:00 | 3211723 | 8 | 9.5272 | 11.0807 | -115.7818 | 4.1532 | 20.0739 | 0.0039 | 0.0061 |
| 2024_09_20 22:00 | 3242331 | 9 | 12.5593 | 13.4990 | -114.6119 | 4.8193 | 52.7022 | 0.0176 | 0.0145 |
| 2024_09_20 22:00 | 3267516 | 10 | 11.7388 | 13.1479 | -116.5871 | 4.8337 | 35.8979 | 0.0118 | 0.0025 |
| 2024_09_20 22:00 | 3231729 | 11 | 14.5702 | 9.9791 | -116.8512 | 3.0249 | 51.6618 | 0.0153 | 0.0028 |
| 2024_09_20 22:00 | 3211647 | 12 | 17.6484 | 13.6717 | -117.9481 | 3.2238 | 51.3177 | 0.0171 | 0.0036 |
| 2024_09_20 22:00 | 3270082 | 13 | 8.3119 | 9.6797 | -116.5933 | 3.0888 | 28.0307 | 0.0019 | 0.0108 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416920_2B6110A3 | 504990 | 654 | -95.9 | 504990 | 566 | -91.3 | 504990 | 39 | -98.4 | 504990 | 70 |
| MR_1774416920_D1FB127E | 152650 | 384 | -93.5 | 152650 | 652 | -98.0 | 152650 | 22 | -103.0 | 152650 | 24 |
| MR_1774416920_EE357E57 | 504990 | 654 | -94.4 | 504990 | 566 | -91.0 | 504990 | 39 | -97.5 | 504990 | 70 |
| MR_1774416920_671B1F03 | 504990 | 654 | -96.9 | 504990 | 566 | -93.9 | 504990 | 39 | -96.3 | 504990 | 70 |
| MR_1774416920_E646312D | 504990 | 654 | -93.8 | 504990 | 566 | -91.1 | 504990 | 39 | -98.2 | 504990 | 70 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 693: `4efb4f23-4f1...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `4efb4f23-4f11-49e0-9f51-c3b2cd9768aa` |
| Tag | **multiple-answer** |
| 정답 | **C15|C20** |
| C15 의미 | Decrease transmission power for 3215700_4 |
| C20 의미 | Press down the tilt angle  of 3215700_4 by 4 degrees |
| 패턴 분류 | **P3 Overshoot (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[693] topology](images/train_0693.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3243046_2 and 3215700_4
- `C2`: Insufficient data; more data is needed for judgment.
- `C3`: Increase transmission power for 3215700_4
- `C4`: Decrease transmission power for 3234885_1
- `C5`: Lift the tilt angle  of 3215700_4 by 4 degrees
- `C6`: Modify PdcchOccupiedSymbolNum to 2SYM for 3215700_4
- `C7`: Decrease A3 Offset threshold for 3215700_4
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3234885_1
- `C9`: Check test server and transmission issues
- `C10`: Increase transmission power for 3234885_1
- `C11`: Increase A3 Offset threshold for 3234885_1
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3234885_1
- `C13`: Press down the tilt angle of 3234885_1 by 3 degrees
- `C14`: Decrease A3 Offset threshold for 3234885_1
- `C15`: Decrease transmission power for 3215700_4 **← 정답**
- `C16`: Add neighbor relationship between 3234885_1 and 3215700_4
- `C17`: Increase A3 Offset threshold for 3215700_4
- `C18`: Lift the tilt angle of 3234885_1 by 3 degrees
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3215700_4
- `C20`: Press down the tilt angle  of 3215700_4 by 4 degrees **← 정답**
- `C21`: Adjust the azimuth of 3234885_1 by 2 degrees
- `C22`: Adjust the azimuth of 3215700_4 by 2 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.689 | MS1 | 121.4656590419 | 31.1446257187 | 688 | 504990 | -81.87 | 15.14 | 549.79 | 0.05 | 2.23 | 1565 |
| 2024-09-20 22:21:32.690 | MS1 | 121.4656600294 | 31.1446355286 | 688 | 504990 | -80.32 | 14.73 | 385.88 | 0.06 | 2.44 | 1562 |
| 2024-09-20 22:21:33.728 | MS1 | 121.4656609925 | 31.1446222841 | 688 | 504990 | -84.98 | 14.65 | 372.32 | 0.01 | 2.07 | 1581 |
| 2024-09-20 22:21:34.394 | MS1 | 121.4656594298 | 31.1446315020 | 688 | 504990 | -86.12 | 0.77 | 69.51 | 0.03 | 1.26 | 1592 |
| 2024-09-20 22:21:35.834 | MS1 | 121.4656747872 | 31.1446193172 | 688 | 504990 | -90.90 | 1.64 | 56.76 | 0.19 | 1.22 | 1596 |
| 2024-09-20 22:21:36.177 | MS1 | 121.4656591472 | 31.1446300296 | 688 | 504990 | -92.54 | 3.85 | 49.59 | 0.13 | 1.47 | 1589 |
| 2024-09-20 22:21:37.898 | MS1 | 121.4656647612 | 31.1446363803 | 688 | 504990 | -90.22 | 3.08 | 46.66 | 0.01 | 1.00 | 1575 |
| 2024-09-20 22:21:38.161 | MS1 | 121.4656708668 | 31.1446322051 | 688 | 504990 | -89.36 | 1.61 | 67.15 | 0.02 | 1.07 | 1589 |
| 2024-09-20 22:21:39.413 | MS1 | 121.4656669227 | 31.1446234587 | 688 | 504990 | -89.17 | 2.60 | 46.45 | 0.03 | 1.15 | 1585 |
| 2024-09-20 22:21:40.655 | MS1 | 121.4656595249 | 31.1446280771 | 688 | 504990 | -82.24 | 17.36 | 368.90 | 0.09 | 2.36 | 1584 |
| 2024-09-20 22:21:41.648 | MS1 | 121.4656620232 | 31.1446283179 | 688 | 504990 | -83.68 | 15.78 | 369.04 | 0.13 | 2.14 | 1593 |
| 2024-09-20 22:21:42.688 | MS1 | 121.4656673989 | 31.1446288192 | 688 | 504990 | -81.54 | 12.23 | 493.37 | 0.20 | 2.67 | 1592 |

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
| 3215700 | 4 | 121.4708965306 | 31.1535328883 | 205 | 2 | 11 | 41.2 | TDD | 783 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3234885 | 1 | 121.4704103859 | 31.1520480986 | 207 | 2 | 7 | 24.2 | TDD | 688 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3243046 | 2 | 121.4729200297 | 31.1485674550 | 317 | 15 | 5 | 47.8 | TDD | 870 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3263071 | 3 | 121.4710561844 | 31.1484761598 | 58 | 15 | 7 | 23.5 | TDD | 680 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |

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
| 2024-09-20 22:21:31.608 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.624 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.731 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.731 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3234885 | 1 | 18.9823 | 5.2111 | -108.4416 | 7.6728 | 123.2052 | 0.0160 | 0.0122 |
| 2024_09_20 22:00 | 3243046 | 2 | 8.1839 | 8.5049 | -117.1449 | 14.5357 | 126.8403 | 0.0089 | 0.0001 |
| 2024_09_20 22:00 | 3263071 | 3 | 6.6261 | 7.4033 | -114.1019 | 17.3629 | 132.4773 | 0.0020 | 0.0134 |
| 2024_09_20 22:00 | 3215700 | 4 | 9.7251 | 16.4335 | -115.3729 | 8.2769 | 166.2029 | 0.0022 | 0.0194 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414470_F111BB8D | 504990 | 688 | -86.2 | 504990 | 783 | -83.2 | 504990 | 870 | -84.0 | 504990 | 680 |
| MR_1774414470_0FA5CC7C | 504990 | 688 | -85.2 | 504990 | 783 | -80.5 | 504990 | 870 | -86.4 | 504990 | 680 |
| MR_1774414470_129448A8 | 504990 | 783 | -85.2 | 504990 | 688 | -83.3 | 504990 | 870 | -86.3 | 504990 | 680 |
| MR_1774414470_DC032A97 | 504990 | 688 | -86.6 | 504990 | 783 | -82.1 | 504990 | 870 | -84.0 | 504990 | 680 |
| MR_1774414470_19A367A3 | 504990 | 688 | -87.4 | 504990 | 783 | -80.5 | 504990 | 870 | -85.7 | 504990 | 680 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 694: `29f11787-3c9...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `29f11787-3c9d-4483-8e9e-4b8675d1008c` |
| Tag | **single-answer** |
| 정답 | **C10** |
| C10 의미 | Lift the tilt angle  of 3276803_4 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[694] topology](images/train_0694.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3245376_2
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3234200_3
- `C3`: Decrease A3 Offset threshold for 3234200_3
- `C4`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3245376_2
- `C5`: Increase A3 Offset threshold for 3234200_3
- `C6`: Decrease A3 Offset threshold for 3245376_2
- `C7`: Adjust the azimuth of 3234200_3 by 39 degrees
- `C8`: Check test server and transmission issues
- `C9`: Press down the tilt angle of 3234200_3 by 5 degrees
- `C10`: Lift the tilt angle  of 3276803_4 by 10 degrees **← 정답**
- `C11`: Decrease transmission power for 3245376_2
- `C12`: Increase transmission power for 3245376_2
- `C13`: Add neighbor relationship between 3234200_3 and 3245376_2
- `C14`: Decrease transmission power for 3234200_3
- `C15`: Press down the tilt angle  of 3276803_4 by 10 degrees
- `C16`: Insufficient data; more data is needed for judgment.
- `C17`: Increase transmission power for 3234200_3
- `C18`: Add neighbor relationship between 3276803_4 and 3245376_2
- `C19`: Adjust the azimuth of 3276803_4 by 50 degrees
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3234200_3
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3245376_2
- `C22`: Lift the tilt angle of 3234200_3 by 5 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.603 | MS1 | 121.4656629351 | 31.1446297022 | 791 | 504990 | -85.75 | 14.31 | 342.19 | 0.06 | 2.69 | 1581 |
| 2024-09-20 22:21:32.491 | MS1 | 121.4656779396 | 31.1446183888 | 791 | 504990 | -91.12 | 13.55 | 337.92 | 0.07 | 2.83 | 1573 |
| 2024-09-20 22:21:33.968 | MS1 | 121.4656772326 | 31.1446365073 | 791 | 504990 | -91.67 | 14.93 | 513.07 | 0.07 | 2.25 | 1563 |
| 2024-09-20 22:21:34.997 | MS1 | 121.4656743712 | 31.1446299810 | 791 | 504990 | -87.55 | 14.98 | 80.48 | 0.19 | 2.37 | 1579 |
| 2024-09-20 22:21:35.878 | MS1 | 121.4656629783 | 31.1446226988 | 791 | 504990 | -91.49 | 15.02 | 64.27 | 0.15 | 2.45 | 1577 |
| 2024-09-20 22:21:36.428 | MS1 | 121.4656624769 | 31.1446221300 | 791 | 504990 | -85.30 | 15.16 | 101.86 | 0.10 | 2.40 | 1590 |
| 2024-09-20 22:21:37.235 | MS1 | 121.4656734474 | 31.1446247299 | 791 | 504990 | -93.51 | 10.89 | 76.55 | 0.18 | 2.47 | 1598 |
| 2024-09-20 22:21:38.641 | MS1 | 121.4656629291 | 31.1446375284 | 791 | 504990 | -93.31 | 12.39 | 87.85 | 0.05 | 2.09 | 1561 |
| 2024-09-20 22:21:39.406 | MS1 | 121.4656667993 | 31.1446292951 | 791 | 504990 | -91.51 | 11.90 | 50.34 | 0.06 | 3.00 | 1569 |
| 2024-09-20 22:21:40.321 | MS1 | 121.4656751093 | 31.1446374172 | 791 | 504990 | -92.60 | 7.08 | 427.95 | 0.07 | 2.76 | 1587 |
| 2024-09-20 22:21:41.841 | MS1 | 121.4656731399 | 31.1446370366 | 791 | 504990 | -90.88 | 10.34 | 310.19 | 0.11 | 2.76 | 1582 |
| 2024-09-20 22:21:42.613 | MS1 | 121.4656705194 | 31.1446238091 | 791 | 504990 | -93.06 | 8.74 | 413.32 | 0.12 | 2.37 | 1582 |

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
| 3234200 | 3 | 121.4684985614 | 31.1531377190 | 157 | 2 | 6 | 44.6 | TDD | 791 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3245376 | 2 | 121.4665601061 | 31.1549985020 | 48 | 15 | 3 | 18.6 | TDD | 403 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3274687 | 1 | 121.4722792733 | 31.1543756683 | 304 | 6 | 4 | 28.8 | TDD | 128 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3276803 | 4 | 121.4645981080 | 31.1443770343 | 1 | 5 | 8 | 18.4 | TDD | 975 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

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
| 2024-09-20 22:21:31.559 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.574 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.708 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.708 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.442 | NREventA3 | measId:2;ServCellPCI:101;Se... |
| 2024-09-20 22:21:38.682 | NRHandoverAttempt | SourcePCI:101;SourceNR-ARFC... |
| 2024-09-20 22:21:38.717 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.731 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.857 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.857 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3274687 | 1 | 5.8490 | 14.1652 | -115.3217 | 17.9440 | 112.5068 | 0.0128 | 0.0116 |
| 2024_09_20 22:00 | 3245376 | 2 | 13.3194 | 8.0153 | -115.1417 | 13.1271 | 98.4663 | 0.0177 | 0.0022 |
| 2024_09_20 22:00 | 3234200 | 3 | 77.3877 | 76.9244 | -116.9662 | 12.5826 | 175.4990 | 0.0138 | 0.0077 |
| 2024_09_20 22:00 | 3276803 | 4 | 6.4988 | 12.3436 | -117.4640 | 9.5732 | 81.4537 | 0.0006 | 0.0091 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415612_69D3861D | 504990 | 791 | -89.5 | 504990 | 403 | -95.6 | 504990 | 975 | -98.5 | 504990 | 128 |
| MR_1774415612_429DCECF | 504990 | 791 | -88.2 | 504990 | 403 | -95.6 | 504990 | 975 | -96.9 | 504990 | 128 |
| MR_1774415612_EF2D458D | 504990 | 791 | -87.6 | 504990 | 403 | -95.1 | 504990 | 975 | -98.3 | 504990 | 128 |
| MR_1774415612_87FA4287 | 504990 | 791 | -87.0 | 504990 | 403 | -95.8 | 504990 | 975 | -95.9 | 504990 | 128 |
| MR_1774415612_47804572 | 504990 | 791 | -85.8 | 504990 | 403 | -96.7 | 504990 | 975 | -95.3 | 504990 | 128 |
| MR_1774415612_DC941276 | 504990 | 791 | -88.1 | 504990 | 403 | -94.5 | 504990 | 975 | -97.8 | 504990 | 128 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 695: `47054714-214...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `47054714-214b-4daa-9e5c-27d40b31cff3` |
| Tag | **single-answer** |
| 정답 | **C11** |
| C11 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[695] topology](images/train_0695.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment.
- `C2`: Press down the tilt angle  of 3251846_2 by 10 degrees
- `C3`: Increase transmission power for 3248768_1
- `C4`: Add neighbor relationship between 3262050_3 and 3251846_2
- `C5`: Lift the tilt angle  of 3251846_2 by 10 degrees
- `C6`: Decrease A3 Offset threshold for 3248768_1
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3251846_2
- `C8`: Increase A3 Offset threshold for 3251846_2
- `C9`: Adjust the azimuth of 3248768_1 by 50 degrees
- `C10`: Adjust the azimuth of 3251846_2 by 48 degrees
- `C11`: Check test server and transmission issues **← 정답**
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3248768_1
- `C13`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3251846_2
- `C14`: Decrease transmission power for 3248768_1
- `C15`: Decrease transmission power for 3251846_2
- `C16`: Add neighbor relationship between 3248768_1 and 3251846_2
- `C17`: Increase transmission power for 3251846_2
- `C18`: Increase A3 Offset threshold for 3248768_1
- `C19`: Press down the tilt angle of 3248768_1 by 3 degrees
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3248768_1
- `C21`: Lift the tilt angle of 3248768_1 by 3 degrees
- `C22`: Decrease A3 Offset threshold for 3251846_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.972 | MS1 | 121.4656687470 | 31.1446260888 | 872 | 504990 | -89.36 | 12.88 | 417.70 | 0.09 | 2.13 | 1569 |
| 2024-09-20 22:21:32.455 | MS1 | 121.4656718477 | 31.1446262410 | 872 | 504990 | -88.26 | 15.35 | 487.51 | 0.06 | 2.23 | 1570 |
| 2024-09-20 22:21:33.330 | MS1 | 121.4656583305 | 31.1446369435 | 872 | 504990 | -85.36 | 16.56 | 492.22 | 0.08 | 2.78 | 1579 |
| 2024-09-20 22:21:34.602 | MS1 | 121.4656683676 | 31.1446290488 | 872 | 504990 | -85.42 | 17.79 | 83.49 | 0.01 | 2.72 | 384 |
| 2024-09-20 22:21:35.142 | MS1 | 121.4656776076 | 31.1446294894 | 872 | 504990 | -85.13 | 17.85 | 74.40 | 0.06 | 2.82 | 493 |
| 2024-09-20 22:21:36.267 | MS1 | 121.4656624482 | 31.1446326857 | 872 | 504990 | -85.28 | 14.88 | 94.98 | 0.18 | 2.51 | 453 |
| 2024-09-20 22:21:37.311 | MS1 | 121.4656662159 | 31.1446210187 | 872 | 504990 | -92.38 | 12.76 | 93.10 | 0.19 | 2.74 | 341 |
| 2024-09-20 22:21:38.743 | MS1 | 121.4656635083 | 31.1446376769 | 872 | 504990 | -90.06 | 9.06 | 91.60 | 0.07 | 2.06 | 477 |
| 2024-09-20 22:21:39.559 | MS1 | 121.4656706380 | 31.1446297194 | 872 | 504990 | -89.93 | 10.38 | 61.38 | 0.02 | 2.67 | 434 |
| 2024-09-20 22:21:40.909 | MS1 | 121.4656580723 | 31.1446333153 | 872 | 504990 | -93.53 | 10.81 | 347.54 | 0.01 | 2.75 | 1568 |
| 2024-09-20 22:21:41.896 | MS1 | 121.4656629589 | 31.1446347435 | 872 | 504990 | -90.01 | 11.11 | 358.69 | 0.13 | 2.09 | 1594 |
| 2024-09-20 22:21:42.535 | MS1 | 121.4656745774 | 31.1446340045 | 872 | 504990 | -90.27 | 12.31 | 384.79 | 0.18 | 2.64 | 1593 |

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
| 3248513 | 4 | 121.4707532882 | 31.1518459569 | 6 | 12 | 11 | 35.4 | TDD | 711 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3248768 | 1 | 121.4718002948 | 31.1510289942 | 59 | 2 | 9 | 15.9 | TDD | 872 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3251846 | 2 | 121.4727597115 | 31.1538838445 | 165 | 11 | 10 | 25.1 | TDD | 474 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3262050 | 3 | 121.4649993494 | 31.1484454952 | 155 | 15 | 5 | 38.4 | TDD | 301 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:31.019 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.037 | NRRandomAccessSuc | Delay：18ms |
| 2024-09-20 22:21:31.149 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.149 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.855 | NREventA3 | measId:2;ServCellPCI:523;Se... |
| 2024-09-20 22:21:38.095 | NRHandoverAttempt | SourcePCI:523;SourceNR-ARFC... |
| 2024-09-20 22:21:38.145 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.155 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.281 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.281 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3248768 | 1 | 18.2686 | 17.5802 | -115.0136 | 8.3894 | 144.6236 | 0.0057 | 0.0153 |
| 2024_09_20 22:00 | 3251846 | 2 | 5.5703 | 5.5209 | -117.7108 | 19.0912 | 162.5896 | 0.0032 | 0.0172 |
| 2024_09_20 22:00 | 3262050 | 3 | 7.2818 | 17.1180 | -115.6107 | 18.6749 | 194.2862 | 0.0146 | 0.0160 |
| 2024_09_20 22:00 | 3248513 | 4 | 15.4729 | 5.9925 | -114.1004 | 13.8451 | 158.4290 | 0.0040 | 0.0008 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774417160_ACD53931 | 504990 | 872 | -83.5 | 504990 | 474 | -85.1 | 504990 | 301 | -97.9 | 504990 | 711 |
| MR_1774417160_C3943170 | 504990 | 872 | -85.7 | 504990 | 474 | -84.4 | 504990 | 301 | -100.1 | 504990 | 711 |
| MR_1774417160_644AD9E6 | 504990 | 872 | -86.9 | 504990 | 474 | -86.9 | 504990 | 301 | -97.4 | 504990 | 711 |
| MR_1774417160_EDF7BAA6 | 504990 | 872 | -87.3 | 504990 | 474 | -84.5 | 504990 | 301 | -98.8 | 504990 | 711 |
| MR_1774417160_DB5E89A7 | 504990 | 872 | -86.2 | 504990 | 474 | -87.6 | 504990 | 301 | -99.1 | 504990 | 711 |
| MR_1774417160_BA1454EC | 504990 | 872 | -84.4 | 504990 | 474 | -86.4 | 504990 | 301 | -100.5 | 504990 | 711 |
| MR_1774417160_A3F03177 | 504990 | 872 | -85.0 | 504990 | 474 | -87.5 | 504990 | 301 | -98.7 | 504990 | 711 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 696: `7d9a4f6e-5b7...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `7d9a4f6e-5b78-4cf6-9fd4-85c646f048e8` |
| Tag | **single-answer** |
| 정답 | **C13** |
| C13 의미 | Decrease A3 Offset threshold for 3211860_4 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[696] topology](images/train_0696.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3241970_3
- `C2`: Adjust the azimuth of 3241970_3 by 25 degrees
- `C3`: Lift the tilt angle of 3211860_4 by 2 degrees
- `C4`: Check test server and transmission issues
- `C5`: Increase transmission power for 3211860_4
- `C6`: Decrease A3 Offset threshold for 3241970_3
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3241970_3
- `C8`: Insufficient data; more data is needed for judgment.
- `C9`: Decrease transmission power for 3211860_4
- `C10`: Increase A3 Offset threshold for 3211860_4
- `C11`: Lift the tilt angle  of 3241970_3 by 10 degrees
- `C12`: Modify PdcchOccupiedSymbolNum to 2SYM for 3211860_4
- `C13`: Decrease A3 Offset threshold for 3211860_4 **← 정답**
- `C14`: Add neighbor relationship between 3271545_2 and 3241970_3
- `C15`: Increase transmission power for 3241970_3
- `C16`: Press down the tilt angle  of 3241970_3 by 10 degrees
- `C17`: Press down the tilt angle of 3211860_4 by 2 degrees
- `C18`: Adjust the azimuth of 3211860_4 by 29 degrees
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3241970_3
- `C20`: Add neighbor relationship between 3211860_4 and 3241970_3
- `C21`: Decrease transmission power for 3241970_3
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3211860_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.639 | MS1 | 121.4656679259 | 31.1446249630 | 606 | 504990 | -82.39 | 15.30 | 316.92 | 0.10 | 2.80 | 1562 |
| 2024-09-20 22:21:32.287 | MS1 | 121.4656740238 | 31.1446327994 | 606 | 504990 | -79.26 | 12.71 | 582.34 | 0.06 | 2.35 | 1575 |
| 2024-09-20 22:21:33.534 | MS1 | 121.4656696830 | 31.1446206612 | 606 | 504990 | -79.76 | 16.32 | 540.62 | 0.12 | 2.47 | 1595 |
| 2024-09-20 22:21:34.554 | MS1 | 121.4656610139 | 31.1446346560 | 606 | 504990 | -86.07 | -3.52 | 53.04 | 0.07 | 1.11 | 1562 |
| 2024-09-20 22:21:35.759 | MS1 | 121.4656635643 | 31.1446322115 | 606 | 504990 | -85.25 | -2.50 | 73.67 | 0.10 | 1.21 | 1592 |
| 2024-09-20 22:21:36.583 | MS1 | 121.4656715634 | 31.1446194073 | 606 | 504990 | -89.53 | -1.32 | 74.71 | 0.20 | 1.38 | 1560 |
| 2024-09-20 22:21:37.905 | MS1 | 121.4656731832 | 31.1446304667 | 606 | 504990 | -83.94 | -0.59 | 46.89 | 0.09 | 1.37 | 1596 |
| 2024-09-20 22:21:38.523 | MS1 | 121.4656705556 | 31.1446192096 | 606 | 504990 | -89.60 | -0.00 | 68.19 | 0.06 | 1.06 | 1575 |
| 2024-09-20 22:21:39.997 | MS1 | 121.4656616760 | 31.1446218931 | 116 | 504990 | -75.91 | 14.42 | 264.46 | 0.11 | 1.50 | 1574 |
| 2024-09-20 22:21:40.324 | MS1 | 121.4656736166 | 31.1446330417 | 116 | 504990 | -84.01 | 12.02 | 335.67 | 0.01 | 2.53 | 1598 |
| 2024-09-20 22:21:41.318 | MS1 | 121.4656719568 | 31.1446222743 | 116 | 504990 | -79.54 | 12.27 | 310.38 | 0.01 | 2.27 | 1586 |
| 2024-09-20 22:21:42.329 | MS1 | 121.4656676668 | 31.1446221650 | 116 | 504990 | -81.40 | 17.57 | 545.22 | 0.09 | 2.03 | 1560 |

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
| 3210564 | 1 | 121.4715800147 | 31.1510777463 | 348 | 13 | 9 | 38.0 | TDD | 144 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3211860 | 4 | 121.4719200247 | 31.1491771740 | 259 | 0 | 8 | 30.2 | TDD | 606 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3241970 | 3 | 121.4713882206 | 31.1444235158 | 297 | 7 | 10 | 42.3 | TDD | 116 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3271545 | 2 | 121.4732523729 | 31.1518628267 | 299 | 6 | 3 | 30.2 | TDD | 163 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |

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
| 2024-09-20 22:21:31.535 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.559 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.690 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.690 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.338 | NREventA3 | measId:2;ServCellPCI:748;Se... |
| 2024-09-20 22:21:38.578 | NRHandoverAttempt | SourcePCI:748;SourceNR-ARFC... |
| 2024-09-20 22:21:38.613 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.625 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.745 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.745 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3210564 | 1 | 12.5265 | 19.0039 | -116.8325 | 9.2636 | 147.3107 | 0.0129 | 0.0156 |
| 2024_09_20 22:00 | 3271545 | 2 | 12.6999 | 16.3877 | -116.3815 | 7.2154 | 130.4024 | 0.0198 | 0.0150 |
| 2024_09_20 22:00 | 3241970 | 3 | 11.4994 | 15.1333 | -116.0923 | 19.2428 | 194.2263 | 0.0187 | 0.0080 |
| 2024_09_20 22:00 | 3211860 | 4 | 5.7680 | 17.7233 | -117.4168 | 16.3031 | 180.4454 | 0.0036 | 0.1643 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412434_F83508F4 | 504990 | 606 | -87.6 | 504990 | 116 | -79.2 | 504990 | 163 | -82.6 | 504990 | 144 |
| MR_1774412434_696D09EA | 504990 | 606 | -87.9 | 504990 | 116 | -81.3 | 504990 | 163 | -80.7 | 504990 | 144 |
| MR_1774412434_AE704C8D | 504990 | 116 | -82.2 | 504990 | 606 | -86.6 | 504990 | 163 | -83.5 | 504990 | 144 |
| MR_1774412434_5F9405D2 | 504990 | 116 | -80.8 | 504990 | 606 | -88.0 | 504990 | 163 | -83.3 | 504990 | 144 |
| MR_1774412434_9786398B | 504990 | 116 | -81.1 | 504990 | 606 | -87.9 | 504990 | 163 | -79.9 | 504990 | 144 |
| MR_1774412434_72C28DDB | 504990 | 606 | -87.1 | 504990 | 116 | -82.2 | 504990 | 163 | -81.4 | 504990 | 144 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 697: `322fb4fb-951...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `322fb4fb-951f-45ca-9bf4-7a798b67b307` |
| Tag | **single-answer** |
| 정답 | **C18** |
| C18 의미 | Lift the tilt angle  of 3278478_1 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[697] topology](images/train_0697.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3279462_3
- `C2`: Check test server and transmission issues
- `C3`: Lift the tilt angle of 3262509_2 by 4 degrees
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3262509_2
- `C5`: Decrease A3 Offset threshold for 3279462_3
- `C6`: Press down the tilt angle of 3262509_2 by 4 degrees
- `C7`: Adjust the azimuth of 3262509_2 by 8 degrees
- `C8`: Insufficient data; more data is needed for judgment.
- `C9`: Increase transmission power for 3262509_2
- `C10`: Decrease A3 Offset threshold for 3262509_2
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3262509_2
- `C12`: Increase A3 Offset threshold for 3262509_2
- `C13`: Adjust the azimuth of 3278478_1 by 50 degrees
- `C14`: Increase A3 Offset threshold for 3279462_3
- `C15`: Press down the tilt angle  of 3278478_1 by 10 degrees
- `C16`: Increase transmission power for 3279462_3
- `C17`: Decrease transmission power for 3262509_2
- `C18`: Lift the tilt angle  of 3278478_1 by 10 degrees **← 정답**
- `C19`: Modify PdcchOccupiedSymbolNum to 2SYM for 3279462_3
- `C20`: Add neighbor relationship between 3262509_2 and 3279462_3
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3279462_3
- `C22`: Add neighbor relationship between 3278478_1 and 3279462_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.244 | MS1 | 121.4656592787 | 31.1446353503 | 860 | 504990 | -86.08 | 14.10 | 330.50 | 0.06 | 2.90 | 1564 |
| 2024-09-20 22:21:32.866 | MS1 | 121.4656653171 | 31.1446237164 | 860 | 504990 | -88.56 | 16.53 | 579.23 | 0.06 | 2.70 | 1575 |
| 2024-09-20 22:21:33.386 | MS1 | 121.4656733334 | 31.1446193162 | 860 | 504990 | -86.38 | 14.01 | 400.56 | 0.06 | 2.57 | 1596 |
| 2024-09-20 22:21:34.935 | MS1 | 121.4656659635 | 31.1446365550 | 860 | 504990 | -90.17 | 16.59 | 60.93 | 0.09 | 2.02 | 1595 |
| 2024-09-20 22:21:35.958 | MS1 | 121.4656673443 | 31.1446292273 | 860 | 504990 | -85.15 | 16.45 | 80.45 | 0.07 | 2.05 | 1586 |
| 2024-09-20 22:21:36.785 | MS1 | 121.4656731532 | 31.1446303804 | 860 | 504990 | -88.05 | 13.94 | 50.61 | 0.15 | 2.48 | 1585 |
| 2024-09-20 22:21:37.689 | MS1 | 121.4656753592 | 31.1446233772 | 860 | 504990 | -91.58 | 12.75 | 60.75 | 0.12 | 2.14 | 1564 |
| 2024-09-20 22:21:38.968 | MS1 | 121.4656630191 | 31.1446249411 | 860 | 504990 | -92.65 | 7.38 | 65.89 | 0.00 | 2.01 | 1591 |
| 2024-09-20 22:21:39.739 | MS1 | 121.4656750029 | 31.1446208615 | 860 | 504990 | -91.01 | 10.96 | 74.95 | 0.02 | 2.44 | 1587 |
| 2024-09-20 22:21:40.348 | MS1 | 121.4656598155 | 31.1446227230 | 860 | 504990 | -92.60 | 11.57 | 493.21 | 0.13 | 2.21 | 1591 |
| 2024-09-20 22:21:41.762 | MS1 | 121.4656689358 | 31.1446295148 | 860 | 504990 | -91.78 | 8.66 | 327.01 | 0.19 | 2.82 | 1585 |
| 2024-09-20 22:21:42.414 | MS1 | 121.4656637785 | 31.1446233365 | 860 | 504990 | -89.67 | 7.09 | 410.24 | 0.05 | 2.20 | 1583 |

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
| 3262509 | 2 | 121.4700937158 | 31.1520137689 | 199 | 2 | 12 | 27.8 | TDD | 860 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3273221 | 4 | 121.4750205624 | 31.1459125201 | 93 | 11 | 1 | 48.8 | TDD | 415 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3278478 | 1 | 121.4653146470 | 31.1493568411 | 65 | 9 | 9 | 48.2 | TDD | 19 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3279462 | 3 | 121.4756958591 | 31.1485070895 | 24 | 12 | 10 | 42.0 | TDD | 55 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:30.919 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.934 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.055 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.055 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.801 | NREventA3 | measId:2;ServCellPCI:1006;S... |
| 2024-09-20 22:21:38.041 | NRHandoverAttempt | SourcePCI:1006;SourceNR-ARF... |
| 2024-09-20 22:21:38.072 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.084 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.210 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.210 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3278478 | 1 | 17.8099 | 17.8201 | -114.0434 | 9.3813 | 144.7657 | 0.0180 | 0.0003 |
| 2024_09_20 22:00 | 3262509 | 2 | 80.6569 | 91.5924 | -115.4274 | 13.6697 | 165.1411 | 0.0087 | 0.0190 |
| 2024_09_20 22:00 | 3279462 | 3 | 9.6570 | 19.2264 | -117.5159 | 10.1136 | 114.6738 | 0.0180 | 0.0040 |
| 2024_09_20 22:00 | 3273221 | 4 | 11.2396 | 5.0509 | -116.7462 | 14.8929 | 184.6611 | 0.0010 | 0.0153 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415908_437C0CFC | 504990 | 860 | -90.8 | 504990 | 55 | -95.3 | 504990 | 19 | -98.0 | 504990 | 415 |
| MR_1774415908_AE80E21E | 504990 | 860 | -91.5 | 504990 | 55 | -94.4 | 504990 | 19 | -95.6 | 504990 | 415 |
| MR_1774415908_FE730A42 | 504990 | 860 | -89.1 | 504990 | 55 | -97.7 | 504990 | 19 | -98.0 | 504990 | 415 |
| MR_1774415908_183FE180 | 504990 | 860 | -91.6 | 504990 | 55 | -95.5 | 504990 | 19 | -99.0 | 504990 | 415 |
| MR_1774415908_F0956870 | 504990 | 860 | -89.7 | 504990 | 55 | -98.0 | 504990 | 19 | -99.1 | 504990 | 415 |
| MR_1774415908_1B891CBD | 504990 | 860 | -90.6 | 504990 | 55 | -97.2 | 504990 | 19 | -99.3 | 504990 | 415 |
| MR_1774415908_8C49111D | 504990 | 860 | -88.9 | 504990 | 55 | -97.4 | 504990 | 19 | -98.2 | 504990 | 415 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 698: `fdc69ca8-162...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `fdc69ca8-1623-4005-afdf-061734ce465c` |
| Tag | **single-answer** |
| 정답 | **C15** |
| C15 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3234869_2 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[698] topology](images/train_0698.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3271331_1
- `C2`: Add neighbor relationship between 3214206_3 and 3271331_1
- `C3`: Insufficient data; more data is needed for judgment.
- `C4`: Increase A3 Offset threshold for 3271331_1
- `C5`: Adjust the azimuth of 3271331_1 by 50 degrees
- `C6`: Check test server and transmission issues
- `C7`: Lift the tilt angle of 3234869_2 by 4 degrees
- `C8`: Decrease transmission power for 3271331_1
- `C9`: Decrease A3 Offset threshold for 3234869_2
- `C10`: Adjust the azimuth of 3234869_2 by 23 degrees
- `C11`: Press down the tilt angle  of 3271331_1 by 7 degrees
- `C12`: Lift the tilt angle  of 3271331_1 by 7 degrees
- `C13`: Increase A3 Offset threshold for 3234869_2
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3271331_1
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3234869_2 **← 정답**
- `C16`: Press down the tilt angle of 3234869_2 by 4 degrees
- `C17`: Decrease transmission power for 3234869_2
- `C18`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3271331_1
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3234869_2
- `C20`: Add neighbor relationship between 3234869_2 and 3271331_1
- `C21`: Decrease A3 Offset threshold for 3271331_1
- `C22`: Increase transmission power for 3234869_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.521 | MS1 | 121.4656731596 | 31.1446292401 | 177 | 504990 | -90.15 | 15.51 | 431.27 | 0.04 | 2.28 | 1597 |
| 2024-09-20 22:21:32.235 | MS1 | 121.4656608075 | 31.1446274774 | 177 | 504990 | -90.65 | 16.31 | 357.61 | 0.06 | 2.24 | 1572 |
| 2024-09-20 22:21:33.900 | MS1 | 121.4656767719 | 31.1446338939 | 177 | 504990 | -86.88 | 16.33 | 484.80 | 0.20 | 2.57 | 1600 |
| 2024-09-20 22:21:34.332 | MS1 | 121.4656682401 | 31.1446296940 | 177 | 504990 | -90.56 | 12.46 | 99.31 | 0.56 | 2.13 | 672 |
| 2024-09-20 22:21:35.629 | MS1 | 121.4656620217 | 31.1446370821 | 177 | 504990 | -90.17 | 17.96 | 79.20 | 0.61 | 2.05 | 604 |
| 2024-09-20 22:21:36.706 | MS1 | 121.4656751106 | 31.1446241184 | 177 | 504990 | -89.55 | 16.41 | 92.07 | 0.56 | 2.20 | 512 |
| 2024-09-20 22:21:37.665 | MS1 | 121.4656626747 | 31.1446379211 | 177 | 504990 | -90.21 | 12.06 | 106.42 | 0.69 | 2.86 | 554 |
| 2024-09-20 22:21:38.820 | MS1 | 121.4656668413 | 31.1446180404 | 177 | 504990 | -92.74 | 12.21 | 86.85 | 0.67 | 2.40 | 660 |
| 2024-09-20 22:21:39.290 | MS1 | 121.4656583118 | 31.1446241857 | 177 | 504990 | -91.84 | 12.75 | 95.80 | 0.58 | 2.03 | 648 |
| 2024-09-20 22:21:40.880 | MS1 | 121.4656636553 | 31.1446336155 | 177 | 504990 | -92.56 | 9.89 | 586.38 | 0.19 | 2.77 | 1582 |
| 2024-09-20 22:21:41.444 | MS1 | 121.4656649034 | 31.1446206515 | 177 | 504990 | -89.22 | 10.00 | 546.62 | 0.15 | 2.12 | 1579 |
| 2024-09-20 22:21:42.883 | MS1 | 121.4656590895 | 31.1446252880 | 177 | 504990 | -91.00 | 7.85 | 474.59 | 0.06 | 2.79 | 1561 |

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
| 3214206 | 3 | 121.4713333788 | 31.1499955852 | 138 | 14 | 2 | 29.4 | TDD | 50 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3234869 | 2 | 121.4656629667 | 31.1496566050 | 157 | 1 | 2 | 32.7 | TDD | 177 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3271331 | 1 | 121.4641387900 | 31.1519309750 | 322 | 4 | 10 | 38.2 | TDD | 912 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3274448 | 4 | 121.4643076895 | 31.1498961970 | 265 | 6 | 11 | 35.4 | TDD | 302 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

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
| 2024-09-20 22:21:31.164 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.185 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.335 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.335 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.061 | NREventA3 | measId:2;ServCellPCI:639;Se... |
| 2024-09-20 22:21:38.301 | NRHandoverAttempt | SourcePCI:639;SourceNR-ARFC... |
| 2024-09-20 22:21:38.342 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.356 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.497 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.497 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3271331 | 1 | 6.7898 | 19.5192 | -116.7881 | 15.7379 | 152.4190 | 0.0015 | 0.0197 |
| 2024_09_20 22:00 | 3234869 | 2 | 19.3851 | 11.0920 | -114.8303 | 7.4716 | 144.9045 | 0.0087 | 0.0187 |
| 2024_09_20 22:00 | 3214206 | 3 | 8.4278 | 5.6287 | -116.5119 | 11.7488 | 162.4846 | 0.0096 | 0.0092 |
| 2024_09_20 22:00 | 3274448 | 4 | 7.8772 | 8.0966 | -114.3126 | 6.7430 | 164.3599 | 0.0179 | 0.0169 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415601_2F8F32A7 | 504990 | 177 | -92.4 | 504990 | 912 | -92.6 | 504990 | 50 | -101.7 | 504990 | 302 |
| MR_1774415601_F6F84324 | 504990 | 177 | -90.3 | 504990 | 912 | -90.4 | 504990 | 50 | -102.0 | 504990 | 302 |
| MR_1774415601_09536F1F | 504990 | 177 | -90.7 | 504990 | 912 | -91.3 | 504990 | 50 | -102.8 | 504990 | 302 |
| MR_1774415601_E7C9D53E | 504990 | 177 | -90.5 | 504990 | 912 | -93.9 | 504990 | 50 | -102.6 | 504990 | 302 |
| MR_1774415601_E252D40F | 504990 | 177 | -90.9 | 504990 | 912 | -90.3 | 504990 | 50 | -102.9 | 504990 | 302 |
| MR_1774415601_2544E06B | 504990 | 177 | -88.9 | 504990 | 912 | -93.5 | 504990 | 50 | -102.0 | 504990 | 302 |
| MR_1774415601_448162F9 | 504990 | 177 | -91.3 | 504990 | 912 | -91.3 | 504990 | 50 | -103.9 | 504990 | 302 |
| MR_1774415601_19E9E21A | 504990 | 177 | -89.6 | 504990 | 912 | -93.2 | 504990 | 50 | -103.6 | 504990 | 302 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 699: `416a5366-8e5...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `416a5366-8e5e-4de0-ad5e-788028ace4f4` |
| Tag | **multiple-answer** |
| 정답 | **C5|C11|C13|C19** |
| C5 의미 | Increase A3 Offset threshold for 3213992_5 |
| C11 의미 | Decrease transmission power for 3252165_3 |
| C13 의미 | Press down the tilt angle  of 3252165_3 by 4 degrees |
| C19 의미 | Increase A3 Offset threshold for 3252165_3 |
| 패턴 분류 | **P2 Ping-pong** |

**시각화 (기지국 배치 + UE 시계열)**

![train[699] topology](images/train_0699.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 5 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 5개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3213992_5
- `C2`: Lift the tilt angle  of 3252165_3 by 4 degrees
- `C3`: Add neighbor relationship between 3213992_5 and 3252165_3
- `C4`: Check test server and transmission issues
- `C5`: Increase A3 Offset threshold for 3213992_5 **← 정답**
- `C6`: Decrease transmission power for 3213992_5
- `C7`: Adjust the azimuth of 3213992_5 by 44 degrees
- `C8`: Modify PdcchOccupiedSymbolNum to 2SYM for 3252165_3
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3252165_3
- `C10`: Add neighbor relationship between 3236645_4 and 3252165_3
- `C11`: Decrease transmission power for 3252165_3 **← 정답**
- `C12`: Adjust the azimuth of 3252165_3 by 9 degrees
- `C13`: Press down the tilt angle  of 3252165_3 by 4 degrees **← 정답**
- `C14`: Decrease A3 Offset threshold for 3213992_5
- `C15`: Decrease A3 Offset threshold for 3252165_3
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3213992_5
- `C17`: Lift the tilt angle of 3213992_5 by 4 degrees
- `C18`: Increase transmission power for 3252165_3
- `C19`: Increase A3 Offset threshold for 3252165_3 **← 정답**
- `C20`: Insufficient data; more data is needed for judgment.
- `C21`: Increase transmission power for 3213992_5
- `C22`: Press down the tilt angle of 3213992_5 by 4 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.501 | MS1 | 121.4656760787 | 31.1446190670 | 248 | 504990 | -75.26 | 16.67 | 408.74 | 0.19 | 2.97 | 1589 |
| 2024-09-20 22:21:32.659 | MS1 | 121.4656666050 | 31.1446321616 | 248 | 504990 | -76.63 | 16.07 | 412.96 | 0.07 | 2.76 | 1584 |
| 2024-09-20 22:21:33.568 | MS1 | 121.4656606664 | 31.1446222875 | 248 | 504990 | -83.16 | 13.25 | 485.50 | 0.10 | 2.43 | 1588 |
| 2024-09-20 22:21:34.112 | MS1 | 121.4656591898 | 31.1446201082 | 74 | 504990 | -89.14 | 4.14 | 41.44 | 0.03 | 1.43 | 1561 |
| 2024-09-20 22:21:35.354 | MS1 | 121.4656618104 | 31.1446311684 | 74 | 504990 | -87.95 | 3.91 | 46.34 | 0.16 | 1.11 | 1594 |
| 2024-09-20 22:21:36.399 | MS1 | 121.4656665923 | 31.1446274963 | 248 | 504990 | -87.60 | 2.66 | 57.56 | 0.19 | 1.21 | 1582 |
| 2024-09-20 22:21:37.464 | MS1 | 121.4656692563 | 31.1446202869 | 248 | 504990 | -85.10 | 3.15 | 39.20 | 0.08 | 1.46 | 1586 |
| 2024-09-20 22:21:38.469 | MS1 | 121.4656609934 | 31.1446258809 | 74 | 504990 | -86.11 | 4.50 | 52.24 | 0.07 | 1.04 | 1578 |
| 2024-09-20 22:21:39.719 | MS1 | 121.4656754980 | 31.1446297786 | 74 | 504990 | -88.72 | 3.20 | 45.57 | 0.16 | 1.09 | 1579 |
| 2024-09-20 22:21:40.564 | MS1 | 121.4656606751 | 31.1446214173 | 74 | 504990 | -78.13 | 17.05 | 597.25 | 0.06 | 2.34 | 1580 |
| 2024-09-20 22:21:41.683 | MS1 | 121.4656776604 | 31.1446313797 | 74 | 504990 | -78.33 | 12.33 | 393.43 | 0.09 | 2.48 | 1597 |
| 2024-09-20 22:21:42.775 | MS1 | 121.4656772585 | 31.1446260045 | 74 | 504990 | -82.60 | 17.00 | 436.19 | 0.10 | 2.02 | 1585 |

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
| 3213992 | 5 | 121.4727959516 | 31.1551905569 | 254 | 3 | 3 | 17.1 | TDD | 248 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3218055 | 1 | 121.4743581549 | 31.1491989858 | 273 | 0 | 8 | 21.7 | TDD | 40 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3236645 | 4 | 121.4753492537 | 31.1523546330 | 180 | 11 | 0 | 34.1 | TDD | 952 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3252165 | 3 | 121.4744911146 | 31.1462092115 | 249 | 1 | 6 | 39.5 | TDD | 627 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3269218 | 2 | 121.4733050158 | 31.1531804263 | 276 | 3 | 3 | 45.9 | TDD | 74 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:31.625 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.650 | NRRandomAccessSuc | Delay：25ms |
| 2024-09-20 22:21:31.780 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.780 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.453 | NREventA3 | measId:2;ServCellPCI:249;Se... |
| 2024-09-20 22:21:34.693 | NRHandoverAttempt | SourcePCI:249;SourceNR-ARFC... |
| 2024-09-20 22:21:34.741 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:34.751 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:34.897 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:34.897 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:36.453 | NREventA3 | measId:2;ServCellPCI:537;Se... |
| 2024-09-20 22:21:36.693 | NRHandoverAttempt | SourcePCI:537;SourceNR-ARFC... |
| 2024-09-20 22:21:36.726 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:36.738 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:36.864 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.864 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.453 | NREventA3 | measId:2;ServCellPCI:249;Se... |
| 2024-09-20 22:21:38.693 | NRHandoverAttempt | SourcePCI:249;SourceNR-ARFC... |
| 2024-09-20 22:21:38.743 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.756 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.887 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.887 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3218055 | 1 | 17.5649 | 17.1947 | -114.1162 | 7.7130 | 177.7577 | 0.0079 | 0.0051 |
| 2024_09_20 22:00 | 3269218 | 2 | 18.8371 | 14.3436 | -117.9027 | 14.7215 | 183.2564 | 0.0027 | 0.0130 |
| 2024_09_20 22:00 | 3252165 | 3 | 18.3318 | 10.5093 | -114.8716 | 12.9048 | 194.5119 | 0.0064 | 0.0067 |
| 2024_09_20 22:00 | 3236645 | 4 | 12.1852 | 17.7296 | -117.1724 | 13.9032 | 140.5792 | 0.0128 | 0.0008 |
| 2024_09_20 22:00 | 3213992 | 5 | 10.3220 | 16.9959 | -115.9900 | 12.1613 | 106.9846 | 0.0189 | 0.0153 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412447_7C8E7118 | 504990 | 74 | -88.4 | 504990 | 248 | -87.6 | 504990 | 627 | -95.9 | 504990 | 952 |
| MR_1774412447_F3541917 | 504990 | 74 | -88.8 | 504990 | 248 | -87.8 | 504990 | 627 | -96.5 | 504990 | 952 |
| MR_1774412447_F98108D9 | 504990 | 74 | -88.9 | 504990 | 248 | -89.1 | 504990 | 627 | -96.1 | 504990 | 952 |
| MR_1774412447_4446D4E5 | 504990 | 74 | -88.0 | 504990 | 248 | -87.2 | 504990 | 627 | -93.6 | 504990 | 952 |
| MR_1774412447_23C92760 | 504990 | 248 | -90.2 | 504990 | 74 | -89.6 | 504990 | 627 | -96.3 | 504990 | 952 |
| MR_1774412447_19C20787 | 504990 | 248 | -90.7 | 504990 | 74 | -87.6 | 504990 | 627 | -96.5 | 504990 | 952 |
| MR_1774412447_8672C4DB | 504990 | 248 | -91.0 | 504990 | 74 | -86.9 | 504990 | 627 | -96.7 | 504990 | 952 |
| MR_1774412447_55C9E720 | 504990 | 74 | -90.6 | 504990 | 248 | -90.1 | 504990 | 627 | -97.3 | 504990 | 952 |

> *... 2개 열 생략 (전체 14열)*

---
