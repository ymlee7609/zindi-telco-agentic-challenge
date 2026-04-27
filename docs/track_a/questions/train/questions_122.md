# Track A 문제 분석 — train[1210]~train[1219]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[1210] ~ train[1219] (10개)

## 목차

1. [문제 1210: `cc9c1f77-805...`](#1210) — multiple-answer, 정답: C9|C18
2. [문제 1211: `b8162b0d-c04...`](#1211) — single-answer, 정답: C3
3. [문제 1212: `32550420-d6b...`](#1212) — single-answer, 정답: C14
4. [문제 1213: `10cf1f13-a5b...`](#1213) — multiple-answer, 정답: C2|C18|C21|C22
5. [문제 1214: `c82198d2-94d...`](#1214) — single-answer, 정답: C4
6. [문제 1215: `ddfd8396-907...`](#1215) — multiple-answer, 정답: C2|C9
7. [문제 1216: `54d29da2-fd4...`](#1216) — single-answer, 정답: C17
8. [문제 1217: `c299f829-515...`](#1217) — single-answer, 정답: C15
9. [문제 1218: `7b568252-061...`](#1218) — single-answer, 정답: C7
10. [문제 1219: `9239ae76-114...`](#1219) — single-answer, 정답: C18

---

### 문제 1210: `cc9c1f77-805...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `cc9c1f77-805b-4c92-9ee7-f01912938225` |
| Tag | **multiple-answer** |
| 정답 | **C9|C18** |
| C9 의미 | Increase transmission power for 3222596_3 |
| C18 의미 | Adjust the azimuth of 3222596_3 by 46 degrees |
| 패턴 분류 | **P4 Coverage (power)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1210] topology](images/train_1210.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3244280_2
- `C2`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3222596_3
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3244280_2
- `C4`: Adjust the azimuth of 3244280_2 by 41 degrees
- `C5`: Decrease A3 Offset threshold for 3222596_3
- `C6`: Lift the tilt angle  of 3244280_2 by 5 degrees
- `C7`: Decrease A3 Offset threshold for 3244280_2
- `C8`: Check test server and transmission issues
- `C9`: Increase transmission power for 3222596_3 **← 정답**
- `C10`: Lift the tilt angle of 3222596_3 by 10 degrees
- `C11`: Add neighbor relationship between 3222596_3 and 3244280_2
- `C12`: Insufficient data; more data is needed for judgment.
- `C13`: Press down the tilt angle  of 3244280_2 by 5 degrees
- `C14`: Add neighbor relationship between 3275958_4 and 3244280_2
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3222596_3
- `C16`: Press down the tilt angle of 3222596_3 by 10 degrees
- `C17`: Increase A3 Offset threshold for 3244280_2
- `C18`: Adjust the azimuth of 3222596_3 by 46 degrees **← 정답**
- `C19`: Decrease transmission power for 3244280_2
- `C20`: Increase transmission power for 3244280_2
- `C21`: Increase A3 Offset threshold for 3222596_3
- `C22`: Decrease transmission power for 3222596_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.886 | MS1 | 121.4656582470 | 31.1446351181 | 387 | 504990 | -86.45 | 16.41 | 445.10 | 0.16 | 2.41 | 1576 |
| 2024-09-20 22:21:32.371 | MS1 | 121.4656744386 | 31.1446299651 | 387 | 504990 | -93.77 | 12.74 | 418.01 | 0.01 | 2.49 | 1592 |
| 2024-09-20 22:21:33.980 | MS1 | 121.4656733762 | 31.1446232357 | 387 | 504990 | -93.61 | 14.11 | 484.48 | 0.16 | 2.41 | 1569 |
| 2024-09-20 22:21:34.167 | MS1 | 121.4656596662 | 31.1446374810 | 387 | 504990 | -103.21 | -0.37 | 26.36 | 0.17 | 1.10 | 1562 |
| 2024-09-20 22:21:35.706 | MS1 | 121.4656713114 | 31.1446283313 | 387 | 504990 | -101.33 | -1.24 | 72.84 | 0.11 | 1.25 | 1575 |
| 2024-09-20 22:21:36.689 | MS1 | 121.4656752097 | 31.1446238476 | 387 | 504990 | -103.09 | 0.06 | 48.12 | 0.19 | 1.25 | 1571 |
| 2024-09-20 22:21:37.550 | MS1 | 121.4656708157 | 31.1446319865 | 387 | 504990 | -103.01 | 1.38 | 47.65 | 0.01 | 1.40 | 1582 |
| 2024-09-20 22:21:38.419 | MS1 | 121.4656642825 | 31.1446204476 | 387 | 504990 | -106.54 | 0.25 | 50.76 | 0.09 | 1.05 | 1592 |
| 2024-09-20 22:21:39.373 | MS1 | 121.4656730040 | 31.1446221781 | 387 | 504990 | -101.16 | -1.57 | 43.91 | 0.20 | 1.35 | 1576 |
| 2024-09-20 22:21:40.524 | MS1 | 121.4656662597 | 31.1446300954 | 387 | 504990 | -85.64 | 15.33 | 332.92 | 0.19 | 2.39 | 1586 |
| 2024-09-20 22:21:41.143 | MS1 | 121.4656587276 | 31.1446368839 | 387 | 504990 | -88.66 | 15.57 | 349.09 | 0.13 | 2.76 | 1587 |
| 2024-09-20 22:21:42.264 | MS1 | 121.4656779271 | 31.1446295533 | 387 | 504990 | -91.85 | 12.43 | 517.15 | 0.08 | 2.00 | 1586 |

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
| 3222596 | 3 | 121.4645506695 | 31.1442148014 | 112 | 4 | 12 | 44.9 | TDD | 387 | n41 | 504990 | 100M | 64T64R | 23 | 504990 |
| 3244280 | 2 | 121.4697586218 | 31.1472363579 | 274 | 1 | 7 | 37.2 | TDD | 153 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3248801 | 1 | 121.4678728398 | 31.1462245531 | 225 | 14 | 0 | 46.4 | TDD | 96 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3275958 | 4 | 121.4705697326 | 31.1460554602 | 358 | 12 | 3 | 25.1 | TDD | 916 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |

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
| 2024-09-20 22:21:30.837 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:30.942 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.942 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.164 | NREventA2 | measId:1;ServCellPCI:16;Ser... |
| 2024-09-20 22:21:34.313 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3248801 | 1 | 14.0036 | 11.1248 | -116.2555 | 17.3307 | 167.6074 | 0.0053 | 0.0100 |
| 2024_09_20 22:00 | 3244280 | 2 | 5.1711 | 9.7656 | -116.6685 | 16.8925 | 98.8345 | 0.0077 | 0.0063 |
| 2024_09_20 22:00 | 3222596 | 3 | 5.9107 | 17.6774 | -117.1440 | 11.0016 | 89.2399 | 0.1287 | 0.0132 |
| 2024_09_20 22:00 | 3275958 | 4 | 18.0210 | 8.6808 | -116.8082 | 14.8326 | 155.8284 | 0.0135 | 0.0056 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414610_810AB74F | 504990 | 387 | -103.7 | 504990 | 153 | -108.8 | 504990 | 916 | -113.5 | 504990 | 96 |
| MR_1774414610_01A4E534 | 504990 | 387 | -103.3 | 504990 | 153 | -106.7 | 504990 | 916 | -114.2 | 504990 | 96 |
| MR_1774414610_268CD7A9 | 504990 | 387 | -101.3 | 504990 | 153 | -107.0 | 504990 | 916 | -112.7 | 504990 | 96 |
| MR_1774414610_C459D90D | 504990 | 387 | -104.6 | 504990 | 153 | -108.7 | 504990 | 916 | -114.5 | 504990 | 96 |
| MR_1774414610_178D5FCD | 504990 | 387 | -102.4 | 504990 | 153 | -106.8 | 504990 | 916 | -112.7 | 504990 | 96 |
| MR_1774414610_AC7C265E | 504990 | 387 | -103.9 | 504990 | 153 | -105.6 | 504990 | 916 | -113.8 | 504990 | 96 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1211: `b8162b0d-c04...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `b8162b0d-c04a-431c-8746-5e860fce5bf2` |
| Tag | **single-answer** |
| 정답 | **C3** |
| C3 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3277507_5 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1211] topology](images/train_1211.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3252084_3
- `C2`: Decrease transmission power for 3252084_3
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3277507_5 **← 정답**
- `C4`: Adjust the azimuth of 3277507_5 by 30 degrees
- `C5`: Check test server and transmission issues
- `C6`: Lift the tilt angle of 3277507_5 by 4 degrees
- `C7`: Increase A3 Offset threshold for 3277507_5
- `C8`: Lift the tilt angle  of 3252084_3 by 4 degrees
- `C9`: Add neighbor relationship between 3277507_5 and 3252084_3
- `C10`: Adjust the azimuth of 3252084_3 by 30 degrees
- `C11`: Add neighbor relationship between 3224393_10 and 3252084_3
- `C12`: Press down the tilt angle of 3277507_5 by 4 degrees
- `C13`: Decrease A3 Offset threshold for 3252084_3
- `C14`: Increase transmission power for 3252084_3
- `C15`: Insufficient data; more data is needed for judgment.
- `C16`: Modify PdcchOccupiedSymbolNum to 2SYM for 3252084_3
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3277507_5
- `C18`: Increase transmission power for 3277507_5
- `C19`: Decrease A3 Offset threshold for 3277507_5
- `C20`: Press down the tilt angle  of 3252084_3 by 4 degrees
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3252084_3
- `C22`: Decrease transmission power for 3277507_5

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.357 | MS1 | 121.4656730338 | 31.1446242851 | 339 | 504990 | -95.68 | 12.95 | 573.68 | 0.09 | 2.96 | 1590 |
| 2024-09-20 22:21:32.666 | MS1 | 121.4656656874 | 31.1446267602 | 386 | 504990 | -95.90 | 12.55 | 567.76 | 0.05 | 2.91 | 1600 |
| 2024-09-20 22:21:33.872 | MS1 | 121.4656608226 | 31.1446217243 | 789 | 504990 | -93.42 | 10.81 | 324.25 | 0.06 | 2.06 | 1593 |
| 2024-09-20 22:21:34.176 | MS1 | 121.4656777670 | 31.1446225445 | 534 | 152650 | -88.69 | 7.03 | 82.09 | 0.00 | 1.56 | 901 |
| 2024-09-20 22:21:35.618 | MS1 | 121.4656719538 | 31.1446360836 | 573 | 152650 | -93.96 | 5.40 | 89.52 | 0.18 | 1.88 | 963 |
| 2024-09-20 22:21:36.251 | MS1 | 121.4656700990 | 31.1446241848 | 533 | 152650 | -92.00 | 6.05 | 101.16 | 0.15 | 1.73 | 962 |
| 2024-09-20 22:21:37.317 | MS1 | 121.4656652529 | 31.1446356479 | 547 | 152650 | -91.75 | 2.93 | 53.85 | 0.02 | 1.96 | 935 |
| 2024-09-20 22:21:38.273 | MS1 | 121.4656693970 | 31.1446220978 | 534 | 152650 | -90.47 | 5.31 | 65.26 | 0.01 | 1.93 | 983 |
| 2024-09-20 22:21:39.148 | MS1 | 121.4656600427 | 31.1446240117 | 573 | 152650 | -87.11 | 2.60 | 52.23 | 0.00 | 1.73 | 952 |
| 2024-09-20 22:21:40.732 | MS1 | 121.4656646276 | 31.1446333135 | 533 | 152650 | -91.52 | 4.42 | 71.09 | 0.02 | 2.39 | 1580 |
| 2024-09-20 22:21:41.458 | MS1 | 121.4656640920 | 31.1446305989 | 547 | 152650 | -96.94 | 5.82 | 63.00 | 0.17 | 2.78 | 1579 |
| 2024-09-20 22:21:42.387 | MS1 | 121.4656645386 | 31.1446376776 | 534 | 152650 | -96.81 | 4.82 | 64.95 | 0.18 | 2.78 | 1576 |

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
| 3216701 | 4 | 121.4733979390 | 31.1465435688 | 232 | 6 | 1 | 18.3 | TDD | 683 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3224393 | 10 | 121.4664654704 | 31.1473902986 | 36 | 15 | 11 | 26.0 | FDD | 533 | n1 | 152650 | 30M | 4T4R | 22 | 152650 |
| 3229415 | 2 | 121.4640701269 | 31.1512993732 | 56 | 5 | 3 | 14.3 | TDD | 867 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3229665 | 12 | 121.4707839107 | 31.1547959201 | 238 | 1 | 6 | 0.2 | FDD | 573 | n1 | 152650 | 30M | 4T4R | 11 | 152650 |
| 3230036 | 11 | 121.4757533122 | 31.1480731215 | 56 | 6 | 3 | 13.5 | FDD | 534 | n1 | 152650 | 30M | 4T4R | 18 | 152650 |
| 3235834 | 13 | 121.4641469393 | 31.1463253688 | 125 | 1 | 10 | 6.6 | FDD | 830 | n1 | 152650 | 30M | 4T4R | 22 | 152650 |
| 3237616 | 9 | 121.4668197060 | 31.1447349908 | 63 | 15 | 5 | 20.2 | FDD | 176 | n1 | 152650 | 30M | 4T4R | 26 | 152650 |
| 3252084 | 3 | 121.4669022876 | 31.1520598366 | 218 | 3 | 4 | 18.4 | TDD | 170 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3256725 | 6 | 121.4757346635 | 31.1469590405 | 109 | 2 | 8 | 14.0 | TDD | 789 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3260666 | 8 | 121.4714219863 | 31.1445387861 | 166 | 12 | 4 | 8.4 | FDD | 931 | n1 | 152650 | 30M | 4T4R | 14 | 152650 |
| 3265150 | 7 | 121.4723652315 | 31.1479096129 | 10 | 10 | 7 | 6.1 | FDD | 547 | n1 | 152650 | 30M | 4T4R | 20 | 152650 |
| 3277507 | 5 | 121.4756119358 | 31.1501598289 | 207 | 3 | 5 | 19.2 | TDD | 339 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3278161 | 1 | 121.4758891661 | 31.1443402177 | 107 | 1 | 0 | 20.0 | TDD | 386 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |

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
| 2024-09-20 22:21:30.937 | NRRandomAccessSuc | Delay：21ms |
| 2024-09-20 22:21:31.085 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.085 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.765 | NREventA2 | measId:1;ServCellPCI:903;Se... |
| 2024-09-20 22:21:34.906 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.171 | NREventA5 | measId:3;ServCellPCI:903;Se... |
| 2024-09-20 22:21:35.243 | NRHandoverAttempt | SourcePCI:903;SourceNR-ARFC... |
| 2024-09-20 22:21:35.287 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.301 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:35.441 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:35.441 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3278161 | 1 | 15.7791 | 14.9283 | -114.8173 | 13.6983 | 151.5076 | 0.0030 | 0.0100 |
| 2024_09_20 22:00 | 3229415 | 2 | 5.0376 | 18.4844 | -117.0663 | 15.7699 | 85.0641 | 0.0026 | 0.0101 |
| 2024_09_20 22:00 | 3252084 | 3 | 18.7858 | 15.1939 | -115.6707 | 6.1028 | 189.0017 | 0.0014 | 0.0072 |
| 2024_09_20 22:00 | 3216701 | 4 | 12.8543 | 10.4459 | -115.5387 | 18.5307 | 137.6508 | 0.0129 | 0.0102 |
| 2024_09_20 22:00 | 3277507 | 5 | 12.7420 | 7.2852 | -115.3701 | 8.8657 | 186.6624 | 0.0021 | 0.0061 |
| 2024_09_20 22:00 | 3256725 | 6 | 9.8685 | 19.9691 | -114.2592 | 18.2614 | 117.1141 | 0.0021 | 0.0081 |
| 2024_09_20 22:00 | 3265150 | 7 | 14.8950 | 9.1389 | -115.5484 | 3.9166 | 38.8291 | 0.0173 | 0.0037 |
| 2024_09_20 22:00 | 3260666 | 8 | 10.4521 | 5.2412 | -116.1606 | 4.5529 | 31.4216 | 0.0043 | 0.0094 |
| 2024_09_20 22:00 | 3237616 | 9 | 9.4583 | 14.8707 | -115.5301 | 3.1097 | 54.9445 | 0.0190 | 0.0049 |
| 2024_09_20 22:00 | 3224393 | 10 | 8.0069 | 16.7320 | -115.4932 | 3.6944 | 37.3185 | 0.0124 | 0.0079 |
| 2024_09_20 22:00 | 3230036 | 11 | 9.9549 | 5.9072 | -115.1790 | 4.3685 | 57.5327 | 0.0129 | 0.0021 |
| 2024_09_20 22:00 | 3229665 | 12 | 5.8134 | 19.7785 | -114.7287 | 3.4341 | 29.8721 | 0.0141 | 0.0099 |
| 2024_09_20 22:00 | 3235834 | 13 | 19.9358 | 7.1998 | -115.1709 | 3.0945 | 31.4923 | 0.0167 | 0.0014 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416227_3FEF4C85 | 504990 | 789 | -92.4 | 504990 | 170 | -92.6 | 504990 | 683 | -90.7 | 504990 | 867 |
| MR_1774416227_9AB19030 | 504990 | 789 | -91.6 | 504990 | 170 | -89.0 | 504990 | 683 | -89.9 | 504990 | 867 |
| MR_1774416227_BA30CAAE | 504990 | 789 | -92.6 | 504990 | 170 | -91.2 | 504990 | 683 | -90.1 | 504990 | 867 |
| MR_1774416227_D83DA25B | 504990 | 789 | -91.9 | 504990 | 170 | -91.6 | 504990 | 683 | -89.8 | 504990 | 867 |
| MR_1774416227_A8D53D73 | 504990 | 789 | -92.1 | 504990 | 170 | -90.5 | 504990 | 683 | -92.9 | 504990 | 867 |
| MR_1774416227_67798946 | 504990 | 789 | -95.4 | 504990 | 170 | -90.2 | 504990 | 683 | -91.0 | 504990 | 867 |
| MR_1774416227_ED112577 | 152650 | 534 | -86.9 | 152650 | 830 | -94.0 | 152650 | 176 | -100.1 | 152650 | 931 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1212: `32550420-d6b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `32550420-d6b8-4976-9fba-53500dd589bf` |
| Tag | **single-answer** |
| 정답 | **C14** |
| C14 의미 | Modify PdcchOccupiedSymbolNum to 2SYM for 3240551_1 |
| 패턴 분류 | **P8 PDCCH Resource** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1212] topology](images/train_1212.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase transmission power for 3240551_1
- `C2`: Add neighbor relationship between 3240551_1 and 3278068_3
- `C3`: Decrease A3 Offset threshold for 3240551_1
- `C4`: Increase A3 Offset threshold for 3278068_3
- `C5`: Decrease transmission power for 3278068_3
- `C6`: Lift the tilt angle  of 3278068_3 by 7 degrees
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3278068_3
- `C8`: Adjust the azimuth of 3240551_1 by 2 degrees
- `C9`: Increase transmission power for 3278068_3
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3240551_1
- `C11`: Decrease A3 Offset threshold for 3278068_3
- `C12`: Add neighbor relationship between 3271015_4 and 3278068_3
- `C13`: Decrease transmission power for 3240551_1
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3240551_1 **← 정답**
- `C15`: Lift the tilt angle of 3240551_1 by 3 degrees
- `C16`: Check test server and transmission issues
- `C17`: Adjust the azimuth of 3278068_3 by 50 degrees
- `C18`: Press down the tilt angle  of 3278068_3 by 7 degrees
- `C19`: Press down the tilt angle of 3240551_1 by 3 degrees
- `C20`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3278068_3
- `C21`: Increase A3 Offset threshold for 3240551_1
- `C22`: Insufficient data; more data is needed for judgment.

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.352 | MS1 | 121.4656707732 | 31.1446242504 | 515 | 504990 | -88.60 | 13.72 | 328.01 | 0.20 | 2.53 | 1563 |
| 2024-09-20 22:21:32.879 | MS1 | 121.4656639560 | 31.1446306506 | 515 | 504990 | -91.65 | 12.51 | 389.47 | 0.12 | 2.04 | 1575 |
| 2024-09-20 22:21:33.734 | MS1 | 121.4656754339 | 31.1446375297 | 515 | 504990 | -90.77 | 13.57 | 313.82 | 0.12 | 2.99 | 1589 |
| 2024-09-20 22:21:34.670 | MS1 | 121.4656778893 | 31.1446279472 | 515 | 504990 | -91.87 | 15.58 | 45.01 | 0.52 | 2.89 | 621 |
| 2024-09-20 22:21:35.274 | MS1 | 121.4656637148 | 31.1446219799 | 515 | 504990 | -85.60 | 15.99 | 81.10 | 0.69 | 2.31 | 583 |
| 2024-09-20 22:21:36.420 | MS1 | 121.4656710834 | 31.1446250706 | 515 | 504990 | -91.28 | 14.43 | 69.96 | 0.68 | 2.14 | 550 |
| 2024-09-20 22:21:37.274 | MS1 | 121.4656591110 | 31.1446346266 | 515 | 504990 | -93.81 | 9.78 | 77.89 | 0.54 | 2.31 | 681 |
| 2024-09-20 22:21:38.152 | MS1 | 121.4656646718 | 31.1446254210 | 515 | 504990 | -93.39 | 12.28 | 67.93 | 0.52 | 2.13 | 601 |
| 2024-09-20 22:21:39.411 | MS1 | 121.4656764474 | 31.1446271777 | 515 | 504990 | -91.25 | 7.03 | 60.52 | 0.58 | 2.35 | 633 |
| 2024-09-20 22:21:40.221 | MS1 | 121.4656645880 | 31.1446373318 | 515 | 504990 | -93.52 | 12.56 | 518.10 | 0.06 | 2.82 | 1590 |
| 2024-09-20 22:21:41.872 | MS1 | 121.4656634110 | 31.1446340506 | 515 | 504990 | -89.92 | 11.89 | 427.05 | 0.06 | 2.14 | 1581 |
| 2024-09-20 22:21:42.386 | MS1 | 121.4656724181 | 31.1446198812 | 515 | 504990 | -89.78 | 11.71 | 509.52 | 0.05 | 2.64 | 1573 |

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
| 3215783 | 2 | 121.4711095651 | 31.1482997044 | 329 | 12 | 3 | 29.6 | TDD | 340 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3240551 | 1 | 121.4706087603 | 31.1528960326 | 205 | 1 | 2 | 35.7 | TDD | 515 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3271015 | 4 | 121.4673652175 | 31.1506849331 | 94 | 5 | 8 | 45.4 | TDD | 671 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3278068 | 3 | 121.4684060054 | 31.1481276815 | 15 | 4 | 7 | 27.1 | TDD | 574 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |

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
| 2024-09-20 22:21:31.175 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.194 | NRRandomAccessSuc | Delay：19ms |
| 2024-09-20 22:21:31.314 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.314 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.030 | NREventA3 | measId:2;ServCellPCI:255;Se... |
| 2024-09-20 22:21:38.270 | NRHandoverAttempt | SourcePCI:255;SourceNR-ARFC... |
| 2024-09-20 22:21:38.305 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.319 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.424 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.424 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3240551 | 1 | 6.8243 | 18.3791 | -117.4020 | 10.6067 | 121.6489 | 0.0070 | 0.0010 |
| 2024_09_20 22:00 | 3215783 | 2 | 8.1402 | 16.7133 | -117.3745 | 9.7783 | 178.7714 | 0.0109 | 0.0009 |
| 2024_09_20 22:00 | 3278068 | 3 | 10.6871 | 18.2971 | -115.8679 | 17.0023 | 129.2131 | 0.0095 | 0.0056 |
| 2024_09_20 22:00 | 3271015 | 4 | 14.4551 | 6.8429 | -115.9406 | 18.2719 | 124.7384 | 0.0075 | 0.0049 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413436_46EA08C2 | 504990 | 515 | -89.9 | 504990 | 574 | -91.3 | 504990 | 671 | -98.9 | 504990 | 340 |
| MR_1774413436_EA514969 | 504990 | 515 | -91.0 | 504990 | 574 | -92.5 | 504990 | 671 | -99.8 | 504990 | 340 |
| MR_1774413436_705177F6 | 504990 | 515 | -93.2 | 504990 | 574 | -94.3 | 504990 | 671 | -99.1 | 504990 | 340 |
| MR_1774413436_917CCD02 | 504990 | 515 | -93.1 | 504990 | 574 | -93.1 | 504990 | 671 | -98.2 | 504990 | 340 |
| MR_1774413436_8D5ACA8A | 504990 | 515 | -92.6 | 504990 | 574 | -90.9 | 504990 | 671 | -98.7 | 504990 | 340 |
| MR_1774413436_587A0101 | 504990 | 515 | -92.7 | 504990 | 574 | -93.4 | 504990 | 671 | -99.9 | 504990 | 340 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1213: `10cf1f13-a5b...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `10cf1f13-a5b8-4782-aac9-e1a900b5ff5f` |
| Tag | **multiple-answer** |
| 정답 | **C2|C18|C21|C22** |
| C2 의미 | Increase A3 Offset threshold for 3248124_3 |
| C18 의미 | Decrease transmission power for 3248124_3 |
| C21 의미 | Increase A3 Offset threshold for 3236099_2 |
| C22 의미 | Press down the tilt angle  of 3248124_3 by 4 degrees |
| 패턴 분류 | **P2 Ping-pong** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1213] topology](images/train_1213.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 5 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 5개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle  of 3248124_3 by 4 degrees
- `C2`: Increase A3 Offset threshold for 3248124_3 **← 정답**
- `C3`: Adjust the azimuth of 3236099_2 by 48 degrees
- `C4`: Press down the tilt angle of 3236099_2 by 4 degrees
- `C5`: Adjust the azimuth of 3248124_3 by 41 degrees
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3248124_3
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3248124_3
- `C8`: Check test server and transmission issues
- `C9`: Increase transmission power for 3236099_2
- `C10`: Modify PdcchOccupiedSymbolNum to 2SYM for 3236099_2
- `C11`: Decrease transmission power for 3236099_2
- `C12`: Add neighbor relationship between 3236099_2 and 3248124_3
- `C13`: Decrease A3 Offset threshold for 3236099_2
- `C14`: Add neighbor relationship between 3244986_5 and 3248124_3
- `C15`: Decrease A3 Offset threshold for 3248124_3
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3236099_2
- `C17`: Lift the tilt angle of 3236099_2 by 4 degrees
- `C18`: Decrease transmission power for 3248124_3 **← 정답**
- `C19`: Insufficient data; more data is needed for judgment.
- `C20`: Increase transmission power for 3248124_3
- `C21`: Increase A3 Offset threshold for 3236099_2 **← 정답**
- `C22`: Press down the tilt angle  of 3248124_3 by 4 degrees **← 정답**

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.823 | MS1 | 121.4656590093 | 31.1446289872 | 975 | 504990 | -77.92 | 14.81 | 458.41 | 0.01 | 2.88 | 1589 |
| 2024-09-20 22:21:32.297 | MS1 | 121.4656756017 | 31.1446188706 | 975 | 504990 | -77.61 | 12.00 | 494.52 | 0.10 | 2.05 | 1590 |
| 2024-09-20 22:21:33.464 | MS1 | 121.4656677686 | 31.1446214605 | 975 | 504990 | -76.87 | 13.34 | 420.12 | 0.02 | 2.16 | 1592 |
| 2024-09-20 22:21:34.806 | MS1 | 121.4656772658 | 31.1446280292 | 406 | 504990 | -88.93 | 1.77 | 53.71 | 0.14 | 1.11 | 1577 |
| 2024-09-20 22:21:35.715 | MS1 | 121.4656769986 | 31.1446362369 | 406 | 504990 | -86.08 | 2.49 | 64.34 | 0.05 | 1.01 | 1573 |
| 2024-09-20 22:21:36.574 | MS1 | 121.4656724601 | 31.1446360949 | 975 | 504990 | -89.25 | 1.78 | 74.02 | 0.16 | 1.04 | 1578 |
| 2024-09-20 22:21:37.815 | MS1 | 121.4656661199 | 31.1446303092 | 975 | 504990 | -84.80 | 1.00 | 31.21 | 0.15 | 1.42 | 1585 |
| 2024-09-20 22:21:38.574 | MS1 | 121.4656593508 | 31.1446217333 | 406 | 504990 | -82.76 | 1.24 | 63.39 | 0.12 | 1.40 | 1568 |
| 2024-09-20 22:21:39.393 | MS1 | 121.4656625065 | 31.1446285774 | 406 | 504990 | -87.08 | 3.26 | 32.42 | 0.08 | 1.28 | 1563 |
| 2024-09-20 22:21:40.510 | MS1 | 121.4656621535 | 31.1446276423 | 406 | 504990 | -75.13 | 14.42 | 555.47 | 0.03 | 2.30 | 1595 |
| 2024-09-20 22:21:41.848 | MS1 | 121.4656731768 | 31.1446328953 | 406 | 504990 | -80.26 | 13.85 | 448.45 | 0.09 | 2.65 | 1590 |
| 2024-09-20 22:21:42.253 | MS1 | 121.4656618894 | 31.1446190473 | 406 | 504990 | -76.59 | 12.83 | 435.31 | 0.06 | 2.86 | 1580 |

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
| 3215855 | 4 | 121.4748400371 | 31.1500807495 | 296 | 7 | 3 | 23.3 | TDD | 406 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3236099 | 2 | 121.4755467250 | 31.1523704917 | 276 | 3 | 8 | 17.7 | TDD | 975 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3244986 | 5 | 121.4641866770 | 31.1447880180 | 207 | 12 | 4 | 33.3 | TDD | 189 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3248124 | 3 | 121.4694975337 | 31.1546867047 | 239 | 2 | 1 | 32.1 | TDD | 628 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3265796 | 1 | 121.4697105980 | 31.1537953064 | 208 | 3 | 7 | 28.6 | TDD | 802 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |

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
| 2024-09-20 22:21:31.156 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.172 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.308 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.308 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.038 | NREventA3 | measId:2;ServCellPCI:730;Se... |
| 2024-09-20 22:21:34.278 | NRHandoverAttempt | SourcePCI:730;SourceNR-ARFC... |
| 2024-09-20 22:21:34.322 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:34.335 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:34.435 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:34.435 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:36.038 | NREventA3 | measId:2;ServCellPCI:294;Se... |
| 2024-09-20 22:21:36.278 | NRHandoverAttempt | SourcePCI:294;SourceNR-ARFC... |
| 2024-09-20 22:21:36.313 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:36.328 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:36.444 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.444 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.038 | NREventA3 | measId:2;ServCellPCI:730;Se... |
| 2024-09-20 22:21:38.278 | NRHandoverAttempt | SourcePCI:730;SourceNR-ARFC... |
| 2024-09-20 22:21:38.317 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.330 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.439 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.439 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3265796 | 1 | 6.2881 | 8.1657 | -114.2872 | 18.2912 | 94.9190 | 0.0009 | 0.0071 |
| 2024_09_20 22:00 | 3236099 | 2 | 14.7783 | 15.4398 | -115.3872 | 19.0627 | 80.2459 | 0.0182 | 0.0141 |
| 2024_09_20 22:00 | 3248124 | 3 | 11.8517 | 15.5362 | -114.2085 | 17.7190 | 176.0567 | 0.0182 | 0.0042 |
| 2024_09_20 22:00 | 3215855 | 4 | 12.3988 | 18.7765 | -117.7620 | 19.2914 | 146.0319 | 0.0132 | 0.0030 |
| 2024_09_20 22:00 | 3244986 | 5 | 8.2710 | 8.5075 | -114.2256 | 9.7701 | 107.4566 | 0.0075 | 0.0082 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414903_48037833 | 504990 | 406 | -90.5 | 504990 | 975 | -90.4 | 504990 | 628 | -89.6 | 504990 | 189 |
| MR_1774414903_99C813D5 | 504990 | 406 | -89.0 | 504990 | 975 | -88.4 | 504990 | 628 | -92.8 | 504990 | 189 |
| MR_1774414903_B4122718 | 504990 | 406 | -89.4 | 504990 | 975 | -90.0 | 504990 | 628 | -91.3 | 504990 | 189 |
| MR_1774414903_4BE87015 | 504990 | 406 | -88.0 | 504990 | 975 | -91.7 | 504990 | 628 | -90.8 | 504990 | 189 |
| MR_1774414903_7349EED5 | 504990 | 975 | -88.0 | 504990 | 406 | -89.5 | 504990 | 628 | -91.5 | 504990 | 189 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1214: `c82198d2-94d...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `c82198d2-94d3-4667-a53a-651e601d6b6e` |
| Tag | **single-answer** |
| 정답 | **C4** |
| C4 의미 | Lift the tilt angle  of 3275262_1 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1214] topology](images/train_1214.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3275262_1 by 10 degrees
- `C2`: Lift the tilt angle of 3222948_4 by 1 degrees
- `C3`: Check test server and transmission issues
- `C4`: Lift the tilt angle  of 3275262_1 by 10 degrees **← 정답**
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3243604_2
- `C6`: Decrease A3 Offset threshold for 3222948_4
- `C7`: Decrease transmission power for 3222948_4
- `C8`: Adjust the azimuth of 3275262_1 by 20 degrees
- `C9`: Modify PdcchOccupiedSymbolNum to 2SYM for 3222948_4
- `C10`: Increase transmission power for 3243604_2
- `C11`: Add neighbor relationship between 3222948_4 and 3243604_2
- `C12`: Add neighbor relationship between 3275262_1 and 3243604_2
- `C13`: Press down the tilt angle of 3222948_4 by 1 degrees
- `C14`: Adjust the azimuth of 3222948_4 by 43 degrees
- `C15`: Decrease A3 Offset threshold for 3243604_2
- `C16`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3222948_4
- `C17`: Insufficient data; more data is needed for judgment.
- `C18`: Increase A3 Offset threshold for 3243604_2
- `C19`: Decrease transmission power for 3243604_2
- `C20`: Increase transmission power for 3222948_4
- `C21`: Increase A3 Offset threshold for 3222948_4
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3243604_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.258 | MS1 | 121.4656641825 | 31.1446324718 | 133 | 504990 | -90.74 | 13.61 | 348.16 | 0.04 | 2.59 | 1582 |
| 2024-09-20 22:21:32.799 | MS1 | 121.4656603785 | 31.1446312025 | 133 | 504990 | -87.73 | 17.04 | 576.05 | 0.05 | 2.38 | 1571 |
| 2024-09-20 22:21:33.520 | MS1 | 121.4656662533 | 31.1446248698 | 133 | 504990 | -88.79 | 17.71 | 359.07 | 0.14 | 2.01 | 1599 |
| 2024-09-20 22:21:34.608 | MS1 | 121.4656591573 | 31.1446210923 | 133 | 504990 | -91.05 | 13.99 | 89.45 | 0.03 | 2.22 | 1588 |
| 2024-09-20 22:21:35.115 | MS1 | 121.4656589178 | 31.1446372507 | 133 | 504990 | -91.78 | 16.91 | 54.31 | 0.09 | 2.22 | 1595 |
| 2024-09-20 22:21:36.406 | MS1 | 121.4656668955 | 31.1446262099 | 133 | 504990 | -90.15 | 17.47 | 67.00 | 0.13 | 2.53 | 1566 |
| 2024-09-20 22:21:37.357 | MS1 | 121.4656645500 | 31.1446224518 | 133 | 504990 | -93.68 | 10.90 | 68.31 | 0.10 | 2.04 | 1562 |
| 2024-09-20 22:21:38.862 | MS1 | 121.4656632412 | 31.1446234974 | 133 | 504990 | -92.86 | 11.66 | 84.80 | 0.00 | 2.16 | 1563 |
| 2024-09-20 22:21:39.832 | MS1 | 121.4656626962 | 31.1446270028 | 133 | 504990 | -91.47 | 12.77 | 72.87 | 0.05 | 2.79 | 1570 |
| 2024-09-20 22:21:40.611 | MS1 | 121.4656680322 | 31.1446246339 | 133 | 504990 | -89.80 | 7.86 | 307.50 | 0.10 | 2.92 | 1571 |
| 2024-09-20 22:21:41.555 | MS1 | 121.4656772234 | 31.1446223215 | 133 | 504990 | -92.09 | 7.28 | 554.88 | 0.12 | 2.76 | 1592 |
| 2024-09-20 22:21:42.228 | MS1 | 121.4656658681 | 31.1446182030 | 133 | 504990 | -90.09 | 12.76 | 490.17 | 0.07 | 2.10 | 1595 |

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
| 3222948 | 4 | 121.4645072562 | 31.1552451023 | 218 | 0 | 4 | 29.1 | TDD | 133 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3224359 | 3 | 121.4717888277 | 31.1477001148 | 41 | 12 | 10 | 15.6 | TDD | 576 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3243604 | 2 | 121.4747906841 | 31.1444864871 | 251 | 10 | 11 | 16.2 | TDD | 401 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3275262 | 1 | 121.4733117234 | 31.1506914102 | 302 | 12 | 5 | 47.6 | TDD | 952 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |

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
| 2024-09-20 22:21:31.502 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.522 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.647 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.647 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.343 | NREventA3 | measId:2;ServCellPCI:979;Se... |
| 2024-09-20 22:21:38.583 | NRHandoverAttempt | SourcePCI:979;SourceNR-ARFC... |
| 2024-09-20 22:21:38.633 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.643 | NRRandomAccessSuc | Delay：10ms |
| 2024-09-20 22:21:38.774 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.774 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3275262 | 1 | 17.2274 | 12.6307 | -116.3960 | 13.9607 | 118.0918 | 0.0157 | 0.0104 |
| 2024_09_20 22:00 | 3243604 | 2 | 9.2577 | 17.9495 | -115.8193 | 12.6781 | 193.7493 | 0.0018 | 0.0179 |
| 2024_09_20 22:00 | 3224359 | 3 | 10.2616 | 6.9145 | -115.7735 | 13.1193 | 189.2724 | 0.0144 | 0.0149 |
| 2024_09_20 22:00 | 3222948 | 4 | 81.3082 | 87.9069 | -114.2973 | 12.8775 | 195.7421 | 0.0141 | 0.0184 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413537_6605D5FC | 504990 | 133 | -89.1 | 504990 | 401 | -97.3 | 504990 | 952 | -101.6 | 504990 | 576 |
| MR_1774413537_5474B63F | 504990 | 133 | -90.4 | 504990 | 401 | -98.3 | 504990 | 952 | -99.9 | 504990 | 576 |
| MR_1774413537_014530E1 | 504990 | 133 | -89.7 | 504990 | 401 | -97.1 | 504990 | 952 | -99.0 | 504990 | 576 |
| MR_1774413537_986172AC | 504990 | 133 | -92.0 | 504990 | 401 | -98.8 | 504990 | 952 | -100.9 | 504990 | 576 |
| MR_1774413537_0E815190 | 504990 | 133 | -90.4 | 504990 | 401 | -97.2 | 504990 | 952 | -100.4 | 504990 | 576 |
| MR_1774413537_36499D46 | 504990 | 133 | -92.3 | 504990 | 401 | -99.8 | 504990 | 952 | -98.8 | 504990 | 576 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1215: `ddfd8396-907...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `ddfd8396-9078-4797-a330-46e53d65d85d` |
| Tag | **multiple-answer** |
| 정답 | **C2|C9** |
| C2 의미 | Press down the tilt angle  of 3254817_1 by 3 degrees |
| C9 의미 | Decrease transmission power for 3254817_1 |
| 패턴 분류 | **P3 Overshoot (tilt)** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1215] topology](images/train_1215.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Insufficient data; more data is needed for judgment.
- `C2`: Press down the tilt angle  of 3254817_1 by 3 degrees **← 정답**
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3231673_4
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3254817_1
- `C5`: Modify PdcchOccupiedSymbolNum to 2SYM for 3231673_4
- `C6`: Add neighbor relationship between 3239545_3 and 3254817_1
- `C7`: Increase transmission power for 3231673_4
- `C8`: Increase A3 Offset threshold for 3254817_1
- `C9`: Decrease transmission power for 3254817_1 **← 정답**
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3254817_1
- `C11`: Lift the tilt angle of 3231673_4 by 1 degrees
- `C12`: Add neighbor relationship between 3231673_4 and 3254817_1
- `C13`: Decrease A3 Offset threshold for 3231673_4
- `C14`: Press down the tilt angle of 3231673_4 by 1 degrees
- `C15`: Decrease transmission power for 3231673_4
- `C16`: Adjust the azimuth of 3231673_4 by 11 degrees
- `C17`: Increase A3 Offset threshold for 3231673_4
- `C18`: Lift the tilt angle  of 3254817_1 by 3 degrees
- `C19`: Adjust the azimuth of 3254817_1 by 22 degrees
- `C20`: Increase transmission power for 3254817_1
- `C21`: Decrease A3 Offset threshold for 3254817_1
- `C22`: Check test server and transmission issues

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.777 | MS1 | 121.4656631017 | 31.1446278363 | 351 | 504990 | -77.64 | 17.33 | 501.44 | 0.15 | 2.92 | 1588 |
| 2024-09-20 22:21:32.664 | MS1 | 121.4656663779 | 31.1446224706 | 351 | 504990 | -83.71 | 12.73 | 592.98 | 0.05 | 2.94 | 1568 |
| 2024-09-20 22:21:33.479 | MS1 | 121.4656740195 | 31.1446223635 | 351 | 504990 | -83.61 | 15.51 | 381.62 | 0.11 | 2.91 | 1577 |
| 2024-09-20 22:21:34.946 | MS1 | 121.4656658548 | 31.1446250947 | 351 | 504990 | -94.41 | 3.95 | 77.83 | 0.02 | 1.40 | 1577 |
| 2024-09-20 22:21:35.622 | MS1 | 121.4656625122 | 31.1446297590 | 351 | 504990 | -87.35 | 2.25 | 83.03 | 0.07 | 1.18 | 1587 |
| 2024-09-20 22:21:36.152 | MS1 | 121.4656609328 | 31.1446254619 | 351 | 504990 | -93.49 | 1.03 | 59.19 | 0.06 | 1.37 | 1561 |
| 2024-09-20 22:21:37.339 | MS1 | 121.4656607324 | 31.1446248971 | 351 | 504990 | -94.46 | 3.40 | 88.50 | 0.12 | 1.41 | 1569 |
| 2024-09-20 22:21:38.144 | MS1 | 121.4656601860 | 31.1446323173 | 351 | 504990 | -85.66 | 0.75 | 81.12 | 0.05 | 1.39 | 1592 |
| 2024-09-20 22:21:39.888 | MS1 | 121.4656742922 | 31.1446256887 | 351 | 504990 | -85.04 | 3.22 | 46.49 | 0.10 | 1.27 | 1561 |
| 2024-09-20 22:21:40.189 | MS1 | 121.4656616340 | 31.1446202875 | 351 | 504990 | -82.10 | 16.96 | 462.58 | 0.02 | 2.29 | 1569 |
| 2024-09-20 22:21:41.641 | MS1 | 121.4656691644 | 31.1446370894 | 351 | 504990 | -80.37 | 15.00 | 549.50 | 0.10 | 2.28 | 1578 |
| 2024-09-20 22:21:42.692 | MS1 | 121.4656689153 | 31.1446316152 | 351 | 504990 | -77.68 | 13.62 | 318.43 | 0.06 | 2.92 | 1572 |

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
| 3223317 | 2 | 121.4647803230 | 31.1478777990 | 239 | 1 | 6 | 37.8 | TDD | 866 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3231673 | 4 | 121.4732360915 | 31.1545354488 | 224 | 0 | 5 | 26.0 | TDD | 351 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3239545 | 3 | 121.4751419906 | 31.1535743059 | 274 | 13 | 2 | 22.0 | TDD | 388 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3254817 | 1 | 121.4717671808 | 31.1481562857 | 258 | 1 | 6 | 20.5 | TDD | 769 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |

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
| 2024-09-20 22:21:31.151 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.167 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.287 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.287 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3254817 | 1 | 16.6985 | 16.7182 | -117.3367 | 12.1831 | 114.6476 | 0.0066 | 0.0143 |
| 2024_09_20 22:00 | 3223317 | 2 | 9.2855 | 9.1894 | -115.7944 | 19.7269 | 87.2215 | 0.0131 | 0.0050 |
| 2024_09_20 22:00 | 3239545 | 3 | 14.3967 | 18.2274 | -114.3605 | 18.4295 | 182.7158 | 0.0072 | 0.0035 |
| 2024_09_20 22:00 | 3231673 | 4 | 9.4562 | 6.9795 | -109.5116 | 15.3044 | 92.5038 | 0.0152 | 0.0039 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413163_C51008B8 | 504990 | 769 | -94.7 | 504990 | 351 | -97.7 | 504990 | 388 | -98.7 | 504990 | 866 |
| MR_1774413163_83C10AFB | 504990 | 351 | -94.5 | 504990 | 769 | -94.6 | 504990 | 388 | -97.0 | 504990 | 866 |
| MR_1774413163_C6F56620 | 504990 | 351 | -93.1 | 504990 | 769 | -94.1 | 504990 | 388 | -97.7 | 504990 | 866 |
| MR_1774413163_97580A11 | 504990 | 351 | -92.9 | 504990 | 769 | -94.2 | 504990 | 388 | -96.0 | 504990 | 866 |
| MR_1774413163_E25F3247 | 504990 | 351 | -96.3 | 504990 | 769 | -94.4 | 504990 | 388 | -96.0 | 504990 | 866 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1216: `54d29da2-fd4...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `54d29da2-fd46-4a15-9b4e-5795072fb69d` |
| Tag | **single-answer** |
| 정답 | **C17** |
| C17 의미 | Lift the tilt angle  of 3230658_1 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1216] topology](images/train_1216.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease transmission power for 3214632_3
- `C2`: Add neighbor relationship between 3247919_4 and 3214632_3
- `C3`: Lift the tilt angle of 3247919_4 by 6 degrees
- `C4`: Press down the tilt angle  of 3230658_1 by 10 degrees
- `C5`: Add neighbor relationship between 3230658_1 and 3214632_3
- `C6`: Decrease transmission power for 3247919_4
- `C7`: Press down the tilt angle of 3247919_4 by 6 degrees
- `C8`: Increase A3 Offset threshold for 3247919_4
- `C9`: Check test server and transmission issues
- `C10`: Increase A3 Offset threshold for 3214632_3
- `C11`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3214632_3
- `C12`: Adjust the azimuth of 3247919_4 by 45 degrees
- `C13`: Decrease A3 Offset threshold for 3214632_3
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3214632_3
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3247919_4
- `C16`: Decrease A3 Offset threshold for 3247919_4
- `C17`: Lift the tilt angle  of 3230658_1 by 10 degrees **← 정답**
- `C18`: Increase transmission power for 3214632_3
- `C19`: Increase transmission power for 3247919_4
- `C20`: Insufficient data; more data is needed for judgment.
- `C21`: Adjust the azimuth of 3230658_1 by 50 degrees
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3247919_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.317 | MS1 | 121.4656772684 | 31.1446331053 | 766 | 504990 | -85.90 | 15.20 | 523.79 | 0.09 | 2.04 | 1594 |
| 2024-09-20 22:21:32.101 | MS1 | 121.4656636478 | 31.1446245800 | 766 | 504990 | -86.47 | 17.20 | 433.76 | 0.06 | 2.13 | 1564 |
| 2024-09-20 22:21:33.889 | MS1 | 121.4656749824 | 31.1446239983 | 766 | 504990 | -88.74 | 15.46 | 349.42 | 0.03 | 2.34 | 1580 |
| 2024-09-20 22:21:34.227 | MS1 | 121.4656741133 | 31.1446372267 | 766 | 504990 | -85.80 | 17.31 | 51.68 | 0.15 | 2.66 | 1584 |
| 2024-09-20 22:21:35.504 | MS1 | 121.4656694381 | 31.1446225810 | 766 | 504990 | -90.93 | 17.21 | 64.22 | 0.11 | 2.59 | 1572 |
| 2024-09-20 22:21:36.405 | MS1 | 121.4656582531 | 31.1446259423 | 766 | 504990 | -91.41 | 12.35 | 67.33 | 0.04 | 2.91 | 1596 |
| 2024-09-20 22:21:37.840 | MS1 | 121.4656707813 | 31.1446187015 | 766 | 504990 | -91.00 | 11.96 | 63.82 | 0.10 | 2.23 | 1575 |
| 2024-09-20 22:21:38.687 | MS1 | 121.4656700765 | 31.1446289504 | 766 | 504990 | -92.06 | 9.91 | 48.56 | 0.01 | 2.13 | 1588 |
| 2024-09-20 22:21:39.938 | MS1 | 121.4656594079 | 31.1446291692 | 766 | 504990 | -90.85 | 11.23 | 104.66 | 0.11 | 2.75 | 1565 |
| 2024-09-20 22:21:40.674 | MS1 | 121.4656727240 | 31.1446372527 | 766 | 504990 | -91.80 | 10.98 | 301.34 | 0.12 | 2.86 | 1560 |
| 2024-09-20 22:21:41.731 | MS1 | 121.4656636176 | 31.1446370269 | 766 | 504990 | -89.76 | 11.94 | 330.56 | 0.01 | 2.35 | 1595 |
| 2024-09-20 22:21:42.727 | MS1 | 121.4656649725 | 31.1446192434 | 766 | 504990 | -89.06 | 9.49 | 323.06 | 0.05 | 2.23 | 1575 |

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
| 3214632 | 3 | 121.4702455703 | 31.1446428540 | 88 | 6 | 3 | 30.9 | TDD | 803 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |
| 3230658 | 1 | 121.4754896393 | 31.1557428733 | 355 | 6 | 8 | 36.9 | TDD | 393 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3247919 | 4 | 121.4680653585 | 31.1540906017 | 237 | 4 | 0 | 35.6 | TDD | 766 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3263950 | 2 | 121.4715463089 | 31.1459628670 | 69 | 10 | 1 | 46.1 | TDD | 994 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |

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
| 2024-09-20 22:21:31.456 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.476 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.580 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.580 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.319 | NREventA3 | measId:2;ServCellPCI:127;Se... |
| 2024-09-20 22:21:38.559 | NRHandoverAttempt | SourcePCI:127;SourceNR-ARFC... |
| 2024-09-20 22:21:38.595 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.607 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.752 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.752 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3230658 | 1 | 7.8314 | 7.8346 | -116.3262 | 17.8866 | 129.5099 | 0.0057 | 0.0086 |
| 2024_09_20 22:00 | 3263950 | 2 | 14.5947 | 7.0668 | -116.1292 | 11.4799 | 124.2400 | 0.0012 | 0.0074 |
| 2024_09_20 22:00 | 3214632 | 3 | 19.5150 | 11.1923 | -115.3227 | 10.6592 | 120.2135 | 0.0140 | 0.0190 |
| 2024_09_20 22:00 | 3247919 | 4 | 75.2577 | 80.0878 | -114.5182 | 9.0522 | 97.8662 | 0.0186 | 0.0051 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413107_E674C68E | 504990 | 766 | -83.8 | 504990 | 803 | -86.6 | 504990 | 393 | -96.6 | 504990 | 994 |
| MR_1774413107_20EA73A8 | 504990 | 766 | -87.2 | 504990 | 803 | -84.4 | 504990 | 393 | -97.2 | 504990 | 994 |
| MR_1774413107_89EF5CED | 504990 | 766 | -83.9 | 504990 | 803 | -84.4 | 504990 | 393 | -97.2 | 504990 | 994 |
| MR_1774413107_FDF8DE9F | 504990 | 766 | -84.7 | 504990 | 803 | -86.1 | 504990 | 393 | -99.9 | 504990 | 994 |
| MR_1774413107_0BA96E9D | 504990 | 766 | -85.2 | 504990 | 803 | -86.0 | 504990 | 393 | -98.6 | 504990 | 994 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1217: `c299f829-515...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `c299f829-5154-4a25-8635-39daa767898c` |
| Tag | **single-answer** |
| 정답 | **C15** |
| C15 의미 | Lift the tilt angle  of 3212776_4 by 10 degrees |
| 패턴 분류 | **P4 Coverage / P6 Tilt** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1217] topology](images/train_1217.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3212776_4 by 10 degrees
- `C2`: Increase A3 Offset threshold for 3240870_3
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3240870_3
- `C4`: Decrease transmission power for 3252135_1
- `C5`: Adjust the azimuth of 3252135_1 by 38 degrees
- `C6`: Adjust the azimuth of 3212776_4 by 8 degrees
- `C7`: Check test server and transmission issues
- `C8`: Decrease A3 Offset threshold for 3240870_3
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3252135_1
- `C10`: Insufficient data; more data is needed for judgment.
- `C11`: Increase transmission power for 3252135_1
- `C12`: Increase transmission power for 3240870_3
- `C13`: Increase A3 Offset threshold for 3252135_1
- `C14`: Lift the tilt angle of 3252135_1 by 6 degrees
- `C15`: Lift the tilt angle  of 3212776_4 by 10 degrees **← 정답**
- `C16`: Add neighbor relationship between 3212776_4 and 3240870_3
- `C17`: Decrease A3 Offset threshold for 3252135_1
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3240870_3
- `C19`: Decrease transmission power for 3240870_3
- `C20`: Add neighbor relationship between 3252135_1 and 3240870_3
- `C21`: Press down the tilt angle of 3252135_1 by 6 degrees
- `C22`: Modify PdcchOccupiedSymbolNum to 2SYM for 3252135_1

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.242 | MS1 | 121.4656678345 | 31.1446263276 | 670 | 504990 | -87.89 | 15.32 | 453.28 | 0.18 | 2.35 | 1565 |
| 2024-09-20 22:21:32.538 | MS1 | 121.4656589849 | 31.1446232852 | 670 | 504990 | -89.36 | 13.91 | 382.91 | 0.19 | 2.76 | 1565 |
| 2024-09-20 22:21:33.347 | MS1 | 121.4656581758 | 31.1446379402 | 670 | 504990 | -89.70 | 16.21 | 320.12 | 0.19 | 2.68 | 1574 |
| 2024-09-20 22:21:34.126 | MS1 | 121.4656696783 | 31.1446291530 | 670 | 504990 | -89.54 | 15.53 | 46.40 | 0.01 | 2.35 | 1581 |
| 2024-09-20 22:21:35.405 | MS1 | 121.4656667483 | 31.1446213580 | 670 | 504990 | -85.74 | 12.95 | 69.72 | 0.00 | 2.88 | 1584 |
| 2024-09-20 22:21:36.263 | MS1 | 121.4656634678 | 31.1446224710 | 670 | 504990 | -91.76 | 14.58 | 67.97 | 0.08 | 2.40 | 1588 |
| 2024-09-20 22:21:37.222 | MS1 | 121.4656603973 | 31.1446326231 | 670 | 504990 | -89.77 | 11.70 | 66.55 | 0.19 | 2.82 | 1589 |
| 2024-09-20 22:21:38.676 | MS1 | 121.4656652581 | 31.1446379065 | 670 | 504990 | -92.46 | 9.56 | 87.26 | 0.08 | 2.48 | 1591 |
| 2024-09-20 22:21:39.523 | MS1 | 121.4656655240 | 31.1446339729 | 670 | 504990 | -91.79 | 11.05 | 85.36 | 0.04 | 2.94 | 1598 |
| 2024-09-20 22:21:40.216 | MS1 | 121.4656670203 | 31.1446358142 | 670 | 504990 | -90.91 | 8.17 | 537.68 | 0.11 | 2.83 | 1562 |
| 2024-09-20 22:21:41.202 | MS1 | 121.4656606842 | 31.1446230288 | 670 | 504990 | -92.60 | 9.32 | 450.49 | 0.09 | 2.32 | 1589 |
| 2024-09-20 22:21:42.586 | MS1 | 121.4656769299 | 31.1446192369 | 670 | 504990 | -91.42 | 9.67 | 308.29 | 0.10 | 2.60 | 1560 |

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
| 3212776 | 4 | 121.4741241384 | 31.1465695202 | 47 | 10 | 5 | 24.5 | TDD | 414 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3240870 | 3 | 121.4660071084 | 31.1461500285 | 199 | 1 | 10 | 49.6 | TDD | 390 | n41 | 504990 | 100M | 64T64R | 28 | 504990 |
| 3251256 | 2 | 121.4726324258 | 31.1482348836 | 220 | 3 | 5 | 34.7 | TDD | 334 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3252135 | 1 | 121.4706604939 | 31.1523302243 | 171 | 4 | 9 | 27.1 | TDD | 670 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |

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
| 2024-09-20 22:21:30.950 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.974 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.108 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.108 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.756 | NREventA3 | measId:2;ServCellPCI:600;Se... |
| 2024-09-20 22:21:37.996 | NRHandoverAttempt | SourcePCI:600;SourceNR-ARFC... |
| 2024-09-20 22:21:38.027 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.038 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.167 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.167 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3252135 | 1 | 86.9598 | 76.1024 | -116.2307 | 9.9873 | 137.1717 | 0.0002 | 0.0160 |
| 2024_09_20 22:00 | 3251256 | 2 | 14.8169 | 17.7490 | -115.8339 | 18.5413 | 112.0910 | 0.0040 | 0.0099 |
| 2024_09_20 22:00 | 3240870 | 3 | 5.8344 | 16.7436 | -114.3084 | 5.1196 | 180.2858 | 0.0046 | 0.0129 |
| 2024_09_20 22:00 | 3212776 | 4 | 16.1213 | 5.0576 | -115.6843 | 10.2142 | 194.1963 | 0.0133 | 0.0134 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414726_9B1E0C70 | 504990 | 670 | -87.8 | 504990 | 390 | -97.5 | 504990 | 414 | -99.9 | 504990 | 334 |
| MR_1774414726_A6FD98E5 | 504990 | 670 | -88.8 | 504990 | 390 | -97.0 | 504990 | 414 | -101.2 | 504990 | 334 |
| MR_1774414726_2EF71E8D | 504990 | 670 | -89.9 | 504990 | 390 | -98.6 | 504990 | 414 | -100.5 | 504990 | 334 |
| MR_1774414726_F9D1909D | 504990 | 670 | -88.4 | 504990 | 390 | -100.2 | 504990 | 414 | -99.2 | 504990 | 334 |
| MR_1774414726_232D9481 | 504990 | 670 | -91.4 | 504990 | 390 | -99.4 | 504990 | 414 | -98.3 | 504990 | 334 |
| MR_1774414726_D872802D | 504990 | 670 | -88.9 | 504990 | 390 | -96.6 | 504990 | 414 | -100.8 | 504990 | 334 |
| MR_1774414726_8CA170BE | 504990 | 670 | -89.0 | 504990 | 390 | -99.0 | 504990 | 414 | -99.6 | 504990 | 334 |
| MR_1774414726_B3F6E9B0 | 504990 | 670 | -89.8 | 504990 | 390 | -98.5 | 504990 | 414 | -97.5 | 504990 | 334 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1218: `7b568252-061...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `7b568252-0612-4432-8236-66e2791e6ad5` |
| Tag | **single-answer** |
| 정답 | **C7** |
| C7 의미 | Add neighbor relationship between 3254453_3 and 3237070_2 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1218] topology](images/train_1218.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3256047_4 and 3237070_2
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3237070_2
- `C3`: Check test server and transmission issues
- `C4`: Increase A3 Offset threshold for 3237070_2
- `C5`: Press down the tilt angle of 3254453_3 by 10 degrees
- `C6`: Press down the tilt angle  of 3237070_2 by 4 degrees
- `C7`: Add neighbor relationship between 3254453_3 and 3237070_2 **← 정답**
- `C8`: Increase transmission power for 3254453_3
- `C9`: Lift the tilt angle  of 3237070_2 by 4 degrees
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3254453_3
- `C11`: Decrease transmission power for 3254453_3
- `C12`: Decrease transmission power for 3237070_2
- `C13`: Adjust the azimuth of 3254453_3 by 23 degrees
- `C14`: Insufficient data; more data is needed for judgment.
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3254453_3
- `C16`: Increase A3 Offset threshold for 3254453_3
- `C17`: Decrease A3 Offset threshold for 3254453_3
- `C18`: Decrease A3 Offset threshold for 3237070_2
- `C19`: Lift the tilt angle of 3254453_3 by 10 degrees
- `C20`: Increase transmission power for 3237070_2
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3237070_2
- `C22`: Adjust the azimuth of 3237070_2 by 32 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.178 | MS1 | 121.4656686783 | 31.1446186742 | 109 | 504990 | -81.55 | 18.00 | 380.40 | 0.09 | 2.87 | 1598 |
| 2024-09-20 22:21:32.516 | MS1 | 121.4656637710 | 31.1446237098 | 109 | 504990 | -80.14 | 12.16 | 502.87 | 0.20 | 2.48 | 1568 |
| 2024-09-20 22:21:33.386 | MS1 | 121.4656601074 | 31.1446200223 | 109 | 504990 | -78.31 | 13.22 | 337.24 | 0.02 | 2.19 | 1579 |
| 2024-09-20 22:21:34.128 | MS1 | 121.4656594528 | 31.1446310894 | 109 | 504990 | -92.33 | -3.38 | 56.01 | 0.05 | 1.18 | 1597 |
| 2024-09-20 22:21:35.712 | MS1 | 121.4656774049 | 31.1446184690 | 109 | 504990 | -90.22 | -3.77 | 58.15 | 0.07 | 1.39 | 1582 |
| 2024-09-20 22:21:36.398 | MS1 | 121.4656724196 | 31.1446356391 | 109 | 504990 | -87.81 | -1.57 | 71.28 | 0.09 | 1.40 | 1570 |
| 2024-09-20 22:21:37.331 | MS1 | 121.4656717363 | 31.1446235710 | 109 | 504990 | -89.54 | -1.94 | 28.64 | 0.13 | 1.27 | 1566 |
| 2024-09-20 22:21:38.527 | MS1 | 121.4656625362 | 31.1446191169 | 109 | 504990 | -76.56 | 13.60 | 386.64 | 0.15 | 1.07 | 1562 |
| 2024-09-20 22:21:39.912 | MS1 | 121.4656744066 | 31.1446277691 | 109 | 504990 | -78.12 | 15.76 | 344.81 | 0.17 | 1.35 | 1571 |
| 2024-09-20 22:21:40.118 | MS1 | 121.4656674423 | 31.1446223375 | 109 | 504990 | -77.67 | 15.95 | 541.19 | 0.20 | 2.55 | 1580 |
| 2024-09-20 22:21:41.376 | MS1 | 121.4656673243 | 31.1446355854 | 109 | 504990 | -77.81 | 12.34 | 313.33 | 0.19 | 2.10 | 1594 |
| 2024-09-20 22:21:42.152 | MS1 | 121.4656779648 | 31.1446288605 | 109 | 504990 | -83.89 | 15.63 | 455.45 | 0.18 | 2.84 | 1585 |

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
| 3237070 | 2 | 121.4711700002 | 31.1529502065 | 241 | 2 | 0 | 37.2 | TDD | 195 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3254453 | 3 | 121.4697665775 | 31.1491339847 | 241 | 10 | 5 | 45.5 | TDD | 109 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3256047 | 4 | 121.4715475597 | 31.1474536128 | 242 | 9 | 5 | 38.4 | TDD | 459 | n41 | 504990 | 100M | 64T64R | 25 | 504990 |
| 3271335 | 1 | 121.4741793050 | 31.1464128260 | 18 | 0 | 2 | 39.2 | TDD | 442 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |

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
| 2024-09-20 22:21:30.965 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.989 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.115 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.115 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.855 | NREventA3 | measId:2;ServCellPCI:418;Se... |
| 2024-09-20 22:21:35.855 | NREventA3 | measId:2;ServCellPCI:418;Se... |
| 2024-09-20 22:21:36.855 | NREventA3 | measId:2;ServCellPCI:418;Se... |
| 2024-09-20 22:21:39.355 | NRRRCReestablishAttempt | PCI:418 |
| 2024-09-20 22:21:39.368 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.379 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:39.522 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.522 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3271335 | 1 | 12.5104 | 12.5055 | -117.5114 | 8.0572 | 98.4306 | 0.0118 | 0.0116 |
| 2024_09_20 22:00 | 3237070 | 2 | 13.7705 | 6.1905 | -117.7744 | 8.8271 | 90.4369 | 0.0127 | 0.0034 |
| 2024_09_20 22:00 | 3254453 | 3 | 7.4142 | 11.9388 | -117.9962 | 8.5804 | 169.0191 | 0.0040 | 0.1184 |
| 2024_09_20 22:00 | 3256047 | 4 | 5.9303 | 19.2408 | -116.3102 | 10.6000 | 99.8264 | 0.0181 | 0.0194 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416381_55697E15 | 504990 | 195 | -87.0 | 504990 | 109 | -92.4 | 504990 | 459 | -96.2 | 504990 | 442 |
| MR_1774416381_1570E9E3 | 504990 | 195 | -84.8 | 504990 | 109 | -92.8 | 504990 | 459 | -95.1 | 504990 | 442 |
| MR_1774416381_8212BAFF | 504990 | 109 | -93.4 | 504990 | 195 | -86.1 | 504990 | 459 | -94.5 | 504990 | 442 |
| MR_1774416381_98992858 | 504990 | 109 | -91.9 | 504990 | 195 | -86.0 | 504990 | 459 | -92.9 | 504990 | 442 |
| MR_1774416381_0DB8F47B | 504990 | 195 | -87.4 | 504990 | 109 | -91.4 | 504990 | 459 | -94.4 | 504990 | 442 |
| MR_1774416381_BB638F69 | 504990 | 109 | -93.7 | 504990 | 195 | -85.2 | 504990 | 459 | -92.6 | 504990 | 442 |
| MR_1774416381_612FF5B8 | 504990 | 195 | -85.0 | 504990 | 109 | -92.1 | 504990 | 459 | -94.2 | 504990 | 442 |
| MR_1774416381_595EF82B | 504990 | 109 | -91.7 | 504990 | 195 | -85.9 | 504990 | 459 | -96.5 | 504990 | 442 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1219: `9239ae76-114...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `9239ae76-1145-4910-9578-47cb2bdf9430` |
| Tag | **single-answer** |
| 정답 | **C18** |
| C18 의미 | Decrease A3 Offset threshold for 3278916_2 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1219] topology](images/train_1219.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3260132_1 and 3258983_3
- `C2`: Increase A3 Offset threshold for 3278916_2
- `C3`: Decrease transmission power for 3258983_3
- `C4`: Modify PdcchOccupiedSymbolNum to 2SYM for 3258983_3
- `C5`: Press down the tilt angle  of 3258983_3 by 2 degrees
- `C6`: Lift the tilt angle  of 3258983_3 by 2 degrees
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3278916_2
- `C8`: Increase transmission power for 3258983_3
- `C9`: Increase A3 Offset threshold for 3258983_3
- `C10`: Press down the tilt angle of 3278916_2 by 9 degrees
- `C11`: Decrease A3 Offset threshold for 3258983_3
- `C12`: Lift the tilt angle of 3278916_2 by 9 degrees
- `C13`: Check test server and transmission issues
- `C14`: Decrease transmission power for 3278916_2
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3258983_3
- `C16`: Increase transmission power for 3278916_2
- `C17`: Adjust the azimuth of 3258983_3 by 50 degrees
- `C18`: Decrease A3 Offset threshold for 3278916_2 **← 정답**
- `C19`: Insufficient data; more data is needed for judgment.
- `C20`: Add neighbor relationship between 3278916_2 and 3258983_3
- `C21`: Adjust the azimuth of 3278916_2 by 50 degrees
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3278916_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.949 | MS1 | 121.4656719726 | 31.1446253461 | 53 | 504990 | -80.86 | 15.82 | 583.96 | 0.08 | 2.28 | 1583 |
| 2024-09-20 22:21:32.600 | MS1 | 121.4656657238 | 31.1446323669 | 53 | 504990 | -81.98 | 13.89 | 594.46 | 0.17 | 2.66 | 1569 |
| 2024-09-20 22:21:33.189 | MS1 | 121.4656584819 | 31.1446304221 | 53 | 504990 | -75.64 | 17.88 | 419.46 | 0.09 | 2.11 | 1568 |
| 2024-09-20 22:21:34.161 | MS1 | 121.4656695099 | 31.1446283467 | 53 | 504990 | -85.83 | -1.15 | 61.27 | 0.08 | 1.32 | 1561 |
| 2024-09-20 22:21:35.967 | MS1 | 121.4656663001 | 31.1446239086 | 53 | 504990 | -84.45 | -1.22 | 30.53 | 0.10 | 1.08 | 1565 |
| 2024-09-20 22:21:36.706 | MS1 | 121.4656735910 | 31.1446374422 | 53 | 504990 | -88.23 | -1.38 | 58.86 | 0.19 | 1.15 | 1600 |
| 2024-09-20 22:21:37.776 | MS1 | 121.4656705930 | 31.1446286287 | 53 | 504990 | -91.00 | -1.73 | 49.59 | 0.16 | 1.22 | 1563 |
| 2024-09-20 22:21:38.306 | MS1 | 121.4656724829 | 31.1446241120 | 53 | 504990 | -89.34 | -2.84 | 61.11 | 0.05 | 1.04 | 1563 |
| 2024-09-20 22:21:39.923 | MS1 | 121.4656721030 | 31.1446333705 | 508 | 504990 | -75.97 | 16.10 | 284.27 | 0.09 | 1.49 | 1587 |
| 2024-09-20 22:21:40.679 | MS1 | 121.4656618749 | 31.1446283129 | 508 | 504990 | -80.59 | 13.14 | 460.74 | 0.04 | 2.65 | 1574 |
| 2024-09-20 22:21:41.474 | MS1 | 121.4656663178 | 31.1446192557 | 508 | 504990 | -84.20 | 17.29 | 413.62 | 0.01 | 2.58 | 1589 |
| 2024-09-20 22:21:42.593 | MS1 | 121.4656745554 | 31.1446318467 | 508 | 504990 | -79.59 | 12.13 | 584.94 | 0.16 | 2.65 | 1567 |

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
| 3229036 | 4 | 121.4674440801 | 31.1482264975 | 261 | 7 | 11 | 46.4 | TDD | 993 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3258983 | 3 | 121.4747422043 | 31.1471027436 | 315 | 1 | 0 | 16.8 | TDD | 508 | n41 | 504990 | 100M | 64T64R | 11 | 504990 |
| 3260132 | 1 | 121.4712420657 | 31.1524011105 | 351 | 3 | 2 | 39.7 | TDD | 937 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3278916 | 2 | 121.4683260422 | 31.1553125328 | 106 | 8 | 2 | 29.8 | TDD | 53 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |

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
| 2024-09-20 22:21:31.049 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.071 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.199 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.199 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.860 | NREventA3 | measId:2;ServCellPCI:41;Ser... |
| 2024-09-20 22:21:38.100 | NRHandoverAttempt | SourcePCI:41;SourceNR-ARFCN... |
| 2024-09-20 22:21:38.147 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.158 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.286 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.286 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3260132 | 1 | 5.0180 | 5.8230 | -116.9607 | 17.0665 | 132.0223 | 0.0136 | 0.0060 |
| 2024_09_20 22:00 | 3278916 | 2 | 7.6482 | 10.5116 | -114.9192 | 17.5962 | 87.5278 | 0.0064 | 0.1116 |
| 2024_09_20 22:00 | 3258983 | 3 | 14.1909 | 16.1505 | -116.4986 | 8.8641 | 140.5213 | 0.0153 | 0.0055 |
| 2024_09_20 22:00 | 3229036 | 4 | 5.5442 | 16.2021 | -115.9612 | 9.2742 | 163.6933 | 0.0006 | 0.0170 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774415472_913E06E9 | 504990 | 508 | -80.3 | 504990 | 53 | -87.1 | 504990 | 937 | -83.6 | 504990 | 993 |
| MR_1774415472_E91300F1 | 504990 | 53 | -84.3 | 504990 | 508 | -79.3 | 504990 | 937 | -83.0 | 504990 | 993 |
| MR_1774415472_0F1A89D2 | 504990 | 508 | -81.9 | 504990 | 53 | -87.0 | 504990 | 937 | -84.2 | 504990 | 993 |
| MR_1774415472_2FEF98ED | 504990 | 508 | -82.9 | 504990 | 53 | -85.7 | 504990 | 937 | -86.5 | 504990 | 993 |
| MR_1774415472_BD753203 | 504990 | 53 | -86.9 | 504990 | 508 | -79.7 | 504990 | 937 | -83.4 | 504990 | 993 |
| MR_1774415472_83BFB574 | 504990 | 508 | -82.5 | 504990 | 53 | -86.2 | 504990 | 937 | -84.1 | 504990 | 993 |
| MR_1774415472_A6C27D1D | 504990 | 508 | -79.1 | 504990 | 53 | -84.1 | 504990 | 937 | -84.3 | 504990 | 993 |

> *... 2개 열 생략 (전체 14열)*

---
