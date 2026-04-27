# Track A 문제 분석 — train[1310]~train[1319]

> 자동 생성: `generate_question_docs.py`
> 원본: `data/Track A/data/Phase_1/train.json`
> 범위: train[1310] ~ train[1319] (10개)

## 목차

1. [문제 1310: `e4caacef-6af...`](#1310) — single-answer, 정답: C15
2. [문제 1311: `be5120fd-ee0...`](#1311) — single-answer, 정답: C7
3. [문제 1312: `e252d1f2-641...`](#1312) — single-answer, 정답: C14
4. [문제 1313: `ca073467-d65...`](#1313) — single-answer, 정답: C18
5. [문제 1314: `f71f1590-0e3...`](#1314) — single-answer, 정답: C5
6. [문제 1315: `80bd2a05-8be...`](#1315) — single-answer, 정답: C16
7. [문제 1316: `e547cbd6-73a...`](#1316) — single-answer, 정답: C9
8. [문제 1317: `33863515-9cc...`](#1317) — single-answer, 정답: C6
9. [문제 1318: `fe57cb75-6e8...`](#1318) — single-answer, 정답: C22
10. [문제 1319: `0b10534d-ef8...`](#1319) — single-answer, 정답: C2

---

### 문제 1310: `e4caacef-6af...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `e4caacef-6afc-462b-841b-211408b13b98` |
| Tag | **single-answer** |
| 정답 | **C15** |
| C15 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1310] topology](images/train_1310.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3248993_3
- `C2`: Add neighbor relationship between 3223808_4 and 3258718_2
- `C3`: Decrease A3 Offset threshold for 3248993_3
- `C4`: Adjust the azimuth of 3258718_2 by 50 degrees
- `C5`: Press down the tilt angle of 3248993_3 by 5 degrees
- `C6`: Decrease A3 Offset threshold for 3258718_2
- `C7`: Adjust the azimuth of 3248993_3 by 18 degrees
- `C8`: Increase transmission power for 3258718_2
- `C9`: Increase A3 Offset threshold for 3258718_2
- `C10`: Add neighbor relationship between 3248993_3 and 3258718_2
- `C11`: Increase transmission power for 3248993_3
- `C12`: Press down the tilt angle  of 3258718_2 by 10 degrees
- `C13`: Decrease transmission power for 3258718_2
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3248993_3
- `C15`: Insufficient data; more data is needed for judgment. **← 정답**
- `C16`: Lift the tilt angle of 3248993_3 by 5 degrees
- `C17`: Decrease transmission power for 3248993_3
- `C18`: Lift the tilt angle  of 3258718_2 by 10 degrees
- `C19`: Increase A3 Offset threshold for 3248993_3
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3258718_2
- `C21`: Check test server and transmission issues
- `C22`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3258718_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.910 | MS1 | 121.4656675394 | 31.1446364384 | 486 | 504990 | -91.21 | 15.05 | 606.53 | 0.07 | 2.49 | 1577 |
| 2024-09-20 22:21:32.275 | MS1 | 121.4656614448 | 31.1446338437 | 486 | 504990 | -89.60 | 16.78 | 347.96 | 0.11 | 2.49 | 1594 |
| 2024-09-20 22:21:33.654 | MS1 | 121.4656754411 | 31.1446369381 | 486 | 504990 | -86.92 | 15.85 | 364.22 | 0.12 | 2.91 | 1577 |
| 2024-09-20 22:21:34.941 | MS1 | 121.4656632882 | 31.1446197710 | 486 | 504990 | -90.61 | 12.86 | 52.17 | 0.10 | 2.28 | 1593 |
| 2024-09-20 22:21:35.768 | MS1 | 121.4656776488 | 31.1446189079 | 486 | 504990 | -89.92 | 15.46 | 101.68 | 0.14 | 2.64 | 1569 |
| 2024-09-20 22:21:36.859 | MS1 | 121.4656728312 | 31.1446313968 | 486 | 504990 | -88.00 | 12.84 | 71.95 | 0.11 | 2.68 | 1566 |
| 2024-09-20 22:21:37.675 | MS1 | 121.4656684783 | 31.1446234577 | 486 | 504990 | -92.06 | 7.97 | 61.47 | 0.11 | 2.52 | 1600 |
| 2024-09-20 22:21:38.488 | MS1 | 121.4656614228 | 31.1446183926 | 486 | 504990 | -91.85 | 11.28 | 55.89 | 0.08 | 2.23 | 1582 |
| 2024-09-20 22:21:39.342 | MS1 | 121.4656591607 | 31.1446254184 | 486 | 504990 | -92.94 | 7.04 | 96.76 | 0.02 | 2.63 | 1584 |
| 2024-09-20 22:21:40.306 | MS1 | 121.4656655165 | 31.1446304682 | 486 | 504990 | -89.62 | 9.66 | 523.39 | 0.11 | 2.65 | 1575 |
| 2024-09-20 22:21:41.143 | MS1 | 121.4656617158 | 31.1446265979 | 486 | 504990 | -90.23 | 9.57 | 338.30 | 0.09 | 2.66 | 1575 |
| 2024-09-20 22:21:42.295 | MS1 | 121.4656597755 | 31.1446191940 | 486 | 504990 | -93.76 | 7.13 | 513.38 | 0.20 | 2.08 | 1582 |

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
| 3223808 | 4 | 121.4742624872 | 31.1454831212 | 31 | 5 | 5 | 45.8 | TDD | 247 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3248993 | 3 | 121.4739188650 | 31.1517253925 | 207 | 4 | 8 | 23.7 | TDD | 486 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3258718 | 2 | 121.4725266420 | 31.1479200612 | 26 | 12 | 0 | 29.2 | TDD | 615 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3278996 | 1 | 121.4663024680 | 31.1494755398 | 294 | 3 | 12 | 20.6 | TDD | 448 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:30.979 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.995 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.106 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.106 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.835 | NREventA3 | measId:2;ServCellPCI:499;Se... |
| 2024-09-20 22:21:38.075 | NRHandoverAttempt | SourcePCI:499;SourceNR-ARFC... |
| 2024-09-20 22:21:38.106 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.120 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.226 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.226 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3278996 | 1 | 93.8783 | 75.0214 | -117.7666 | 11.8574 | 136.0466 | 0.0061 | 0.0156 |
| 2024_09_19 22:00 | 3258718 | 2 | 86.3169 | 80.2977 | -116.6055 | 8.1027 | 113.3313 | 0.0028 | 0.0120 |
| 2024_09_19 22:00 | 3248993 | 3 | 78.4407 | 79.6100 | -114.2346 | 11.5829 | 137.1350 | 0.0183 | 0.0082 |
| 2024_09_19 22:00 | 3223808 | 4 | 87.5254 | 85.1313 | -117.1695 | 10.9929 | 80.4542 | 0.0145 | 0.0032 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413787_68CE9D6F | 504990 | 486 | -91.5 | 504990 | 615 | -99.0 | 504990 | 247 | -102.1 | 504990 | 448 |
| MR_1774413787_153BE3E2 | 504990 | 486 | -90.4 | 504990 | 615 | -100.6 | 504990 | 247 | -101.6 | 504990 | 448 |
| MR_1774413787_11DA694B | 504990 | 486 | -92.1 | 504990 | 615 | -98.2 | 504990 | 247 | -99.6 | 504990 | 448 |
| MR_1774413787_AF6DE1EB | 504990 | 486 | -91.1 | 504990 | 615 | -98.9 | 504990 | 247 | -102.2 | 504990 | 448 |
| MR_1774413787_916D3E90 | 504990 | 486 | -91.7 | 504990 | 615 | -100.4 | 504990 | 247 | -101.1 | 504990 | 448 |
| MR_1774413787_186B772D | 504990 | 486 | -91.5 | 504990 | 615 | -99.2 | 504990 | 247 | -102.6 | 504990 | 448 |
| MR_1774413787_6F89BC3A | 504990 | 486 | -92.2 | 504990 | 615 | -101.3 | 504990 | 247 | -101.6 | 504990 | 448 |
| MR_1774413787_76DC82F1 | 504990 | 486 | -91.1 | 504990 | 615 | -99.6 | 504990 | 247 | -100.2 | 504990 | 448 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1311: `be5120fd-ee0...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `be5120fd-ee0c-4e7d-a11f-c043e4e8a8b2` |
| Tag | **single-answer** |
| 정답 | **C7** |
| C7 의미 | Add neighbor relationship between 3246151_1 and 3250562_2 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1311] topology](images/train_1311.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Increase A3 Offset threshold for 3246151_1
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3246151_1
- `C3`: Check test server and transmission issues
- `C4`: Increase transmission power for 3250562_2
- `C5`: Increase transmission power for 3246151_1
- `C6`: Lift the tilt angle  of 3250562_2 by 2 degrees
- `C7`: Add neighbor relationship between 3246151_1 and 3250562_2 **← 정답**
- `C8`: Adjust the azimuth of 3250562_2 by 2 degrees
- `C9`: Increase A3 Offset threshold for 3250562_2
- `C10`: Decrease transmission power for 3250562_2
- `C11`: Decrease A3 Offset threshold for 3246151_1
- `C12`: Lift the tilt angle of 3246151_1 by 10 degrees
- `C13`: Insufficient data; more data is needed for judgment.
- `C14`: Press down the tilt angle  of 3250562_2 by 2 degrees
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3250562_2
- `C16`: Decrease A3 Offset threshold for 3250562_2
- `C17`: Modify PdcchOccupiedSymbolNum to 2SYM for 3250562_2
- `C18`: Adjust the azimuth of 3246151_1 by 50 degrees
- `C19`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3246151_1
- `C20`: Press down the tilt angle of 3246151_1 by 10 degrees
- `C21`: Decrease transmission power for 3246151_1
- `C22`: Add neighbor relationship between 3253497_4 and 3250562_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.609 | MS1 | 121.4656588550 | 31.1446320665 | 872 | 504990 | -79.68 | 15.92 | 435.11 | 0.20 | 2.54 | 1591 |
| 2024-09-20 22:21:32.907 | MS1 | 121.4656734686 | 31.1446330127 | 872 | 504990 | -83.31 | 12.00 | 326.27 | 0.15 | 2.92 | 1582 |
| 2024-09-20 22:21:33.166 | MS1 | 121.4656768697 | 31.1446216933 | 872 | 504990 | -82.97 | 13.48 | 483.61 | 0.10 | 2.03 | 1569 |
| 2024-09-20 22:21:34.391 | MS1 | 121.4656648260 | 31.1446234620 | 872 | 504990 | -85.76 | -1.32 | 70.77 | 0.19 | 1.47 | 1571 |
| 2024-09-20 22:21:35.560 | MS1 | 121.4656581808 | 31.1446362945 | 872 | 504990 | -93.79 | -0.07 | 59.34 | 0.03 | 1.16 | 1588 |
| 2024-09-20 22:21:36.389 | MS1 | 121.4656642448 | 31.1446222861 | 872 | 504990 | -85.79 | -0.05 | 49.63 | 0.13 | 1.30 | 1587 |
| 2024-09-20 22:21:37.987 | MS1 | 121.4656581666 | 31.1446348494 | 872 | 504990 | -89.82 | -3.58 | 48.73 | 0.15 | 1.40 | 1598 |
| 2024-09-20 22:21:38.854 | MS1 | 121.4656772684 | 31.1446361237 | 872 | 504990 | -84.37 | 14.88 | 353.91 | 0.15 | 1.24 | 1578 |
| 2024-09-20 22:21:39.625 | MS1 | 121.4656727832 | 31.1446281726 | 872 | 504990 | -83.17 | 16.19 | 354.32 | 0.15 | 1.45 | 1593 |
| 2024-09-20 22:21:40.713 | MS1 | 121.4656770058 | 31.1446209321 | 872 | 504990 | -83.06 | 16.66 | 359.50 | 0.16 | 2.44 | 1599 |
| 2024-09-20 22:21:41.132 | MS1 | 121.4656686254 | 31.1446287872 | 872 | 504990 | -78.62 | 16.18 | 470.98 | 0.09 | 2.71 | 1570 |
| 2024-09-20 22:21:42.279 | MS1 | 121.4656775755 | 31.1446360758 | 872 | 504990 | -75.69 | 14.73 | 411.36 | 0.03 | 2.63 | 1582 |

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
| 3210000 | 3 | 121.4660513814 | 31.1513510540 | 219 | 15 | 5 | 42.1 | TDD | 165 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3246151 | 1 | 121.4696529564 | 31.1471164789 | 25 | 7 | 2 | 43.5 | TDD | 872 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3250562 | 2 | 121.4718716040 | 31.1508262776 | 219 | 0 | 8 | 35.3 | TDD | 434 | n41 | 504990 | 100M | 64T64R | 19 | 504990 |
| 3253497 | 4 | 121.4732048922 | 31.1502663191 | 303 | 5 | 4 | 47.9 | TDD | 751 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |

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
| 2024-09-20 22:21:31.099 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.123 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.257 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.257 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.922 | NREventA3 | measId:2;ServCellPCI:53;Ser... |
| 2024-09-20 22:21:35.922 | NREventA3 | measId:2;ServCellPCI:53;Ser... |
| 2024-09-20 22:21:36.922 | NREventA3 | measId:2;ServCellPCI:53;Ser... |
| 2024-09-20 22:21:39.422 | NRRRCReestablishAttempt | PCI:53 |
| 2024-09-20 22:21:39.432 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.444 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:39.568 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.568 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3246151 | 1 | 5.7138 | 11.6249 | -114.3745 | 17.2485 | 153.6439 | 0.0195 | 0.1263 |
| 2024_09_20 22:00 | 3250562 | 2 | 14.7914 | 10.6221 | -114.0699 | 11.9379 | 143.0513 | 0.0078 | 0.0142 |
| 2024_09_20 22:00 | 3210000 | 3 | 19.5916 | 12.2128 | -115.4842 | 12.7474 | 115.0121 | 0.0104 | 0.0032 |
| 2024_09_20 22:00 | 3253497 | 4 | 17.5851 | 15.9220 | -117.5520 | 17.9909 | 143.4766 | 0.0137 | 0.0078 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412040_CD7D596E | 504990 | 434 | -79.7 | 504990 | 872 | -87.7 | 504990 | 751 | -83.0 | 504990 | 165 |
| MR_1774412040_E02344E9 | 504990 | 872 | -85.2 | 504990 | 434 | -82.3 | 504990 | 751 | -85.5 | 504990 | 165 |
| MR_1774412040_2B7BFA74 | 504990 | 872 | -83.9 | 504990 | 434 | -78.9 | 504990 | 751 | -85.0 | 504990 | 165 |
| MR_1774412040_E95DF15F | 504990 | 434 | -82.6 | 504990 | 872 | -86.7 | 504990 | 751 | -83.7 | 504990 | 165 |
| MR_1774412040_11CFB4C1 | 504990 | 872 | -87.4 | 504990 | 434 | -82.2 | 504990 | 751 | -84.1 | 504990 | 165 |
| MR_1774412040_DE6CE1DC | 504990 | 872 | -84.0 | 504990 | 434 | -81.2 | 504990 | 751 | -83.4 | 504990 | 165 |
| MR_1774412040_FB624DCF | 504990 | 434 | -80.6 | 504990 | 872 | -84.2 | 504990 | 751 | -83.1 | 504990 | 165 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1312: `e252d1f2-641...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `e252d1f2-641d-44b5-bef9-4a0ef4373299` |
| Tag | **single-answer** |
| 정답 | **C14** |
| C14 의미 | Decrease A3 Offset threshold for 3271592_3 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1312] topology](images/train_1312.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Press down the tilt angle  of 3266187_1 by 10 degrees
- `C2`: Insufficient data; more data is needed for judgment.
- `C3`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3266187_1
- `C4`: Lift the tilt angle  of 3266187_1 by 10 degrees
- `C5`: Check test server and transmission issues
- `C6`: Decrease transmission power for 3266187_1
- `C7`: Lift the tilt angle of 3271592_3 by 10 degrees
- `C8`: Increase A3 Offset threshold for 3271592_3
- `C9`: Add neighbor relationship between 3214938_4 and 3266187_1
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3271592_3
- `C11`: Decrease A3 Offset threshold for 3266187_1
- `C12`: Increase transmission power for 3266187_1
- `C13`: Increase A3 Offset threshold for 3266187_1
- `C14`: Decrease A3 Offset threshold for 3271592_3 **← 정답**
- `C15`: Adjust the azimuth of 3266187_1 by 50 degrees
- `C16`: Add neighbor relationship between 3271592_3 and 3266187_1
- `C17`: Press down the tilt angle of 3271592_3 by 10 degrees
- `C18`: Modify PdcchOccupiedSymbolNum to 2SYM for 3271592_3
- `C19`: Adjust the azimuth of 3271592_3 by 50 degrees
- `C20`: Decrease transmission power for 3271592_3
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3266187_1
- `C22`: Increase transmission power for 3271592_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.104 | MS1 | 121.4656654622 | 31.1446213554 | 430 | 504990 | -76.05 | 12.16 | 489.69 | 0.04 | 2.19 | 1562 |
| 2024-09-20 22:21:32.130 | MS1 | 121.4656721283 | 31.1446242700 | 430 | 504990 | -75.28 | 12.43 | 404.99 | 0.06 | 2.68 | 1576 |
| 2024-09-20 22:21:33.139 | MS1 | 121.4656762556 | 31.1446214851 | 430 | 504990 | -84.78 | 17.75 | 434.54 | 0.11 | 2.62 | 1593 |
| 2024-09-20 22:21:34.934 | MS1 | 121.4656622801 | 31.1446339548 | 430 | 504990 | -89.10 | -1.58 | 63.65 | 0.14 | 1.29 | 1591 |
| 2024-09-20 22:21:35.362 | MS1 | 121.4656733351 | 31.1446355692 | 430 | 504990 | -85.16 | -0.45 | 46.74 | 0.12 | 1.13 | 1582 |
| 2024-09-20 22:21:36.690 | MS1 | 121.4656628972 | 31.1446298319 | 430 | 504990 | -86.62 | -2.49 | 62.38 | 0.08 | 1.15 | 1564 |
| 2024-09-20 22:21:37.824 | MS1 | 121.4656758348 | 31.1446332803 | 430 | 504990 | -85.36 | -3.71 | 52.86 | 0.06 | 1.29 | 1573 |
| 2024-09-20 22:21:38.821 | MS1 | 121.4656629408 | 31.1446303192 | 430 | 504990 | -89.22 | -3.85 | 70.48 | 0.19 | 1.46 | 1595 |
| 2024-09-20 22:21:39.218 | MS1 | 121.4656600659 | 31.1446349931 | 634 | 504990 | -77.02 | 14.22 | 228.75 | 0.04 | 1.45 | 1569 |
| 2024-09-20 22:21:40.983 | MS1 | 121.4656713655 | 31.1446356356 | 634 | 504990 | -78.58 | 13.67 | 495.94 | 0.18 | 2.41 | 1590 |
| 2024-09-20 22:21:41.143 | MS1 | 121.4656748847 | 31.1446266598 | 634 | 504990 | -84.07 | 17.88 | 484.35 | 0.19 | 2.22 | 1598 |
| 2024-09-20 22:21:42.402 | MS1 | 121.4656625395 | 31.1446289537 | 634 | 504990 | -79.21 | 14.54 | 317.15 | 0.01 | 2.05 | 1598 |

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
| 3214938 | 4 | 121.4718855227 | 31.1558642421 | 223 | 9 | 2 | 32.6 | TDD | 98 | n41 | 504990 | 100M | 64T64R | 14 | 504990 |
| 3225490 | 2 | 121.4702031357 | 31.1511060400 | 334 | 6 | 5 | 27.8 | TDD | 269 | n41 | 504990 | 100M | 64T64R | 17 | 504990 |
| 3266187 | 1 | 121.4724726034 | 31.1447814328 | 215 | 12 | 11 | 48.4 | TDD | 634 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3271592 | 3 | 121.4755146588 | 31.1505339287 | 123 | 14 | 6 | 46.1 | TDD | 430 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |

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
| 2024-09-20 22:21:31.518 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.540 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.674 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.674 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.416 | NREventA3 | measId:2;ServCellPCI:6;Serv... |
| 2024-09-20 22:21:38.656 | NRHandoverAttempt | SourcePCI:6;SourceNR-ARFCN:... |
| 2024-09-20 22:21:38.700 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.713 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:38.823 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.823 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3266187 | 1 | 17.9686 | 19.3934 | -116.7483 | 11.6981 | 109.9416 | 0.0135 | 0.0049 |
| 2024_09_20 22:00 | 3225490 | 2 | 8.0476 | 19.7407 | -117.8475 | 6.9043 | 108.7454 | 0.0016 | 0.0072 |
| 2024_09_20 22:00 | 3271592 | 3 | 8.2263 | 18.5250 | -114.4983 | 6.2104 | 193.6914 | 0.0047 | 0.1997 |
| 2024_09_20 22:00 | 3214938 | 4 | 6.0492 | 5.4531 | -116.4617 | 17.4985 | 179.4967 | 0.0128 | 0.0059 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414520_F4079831 | 504990 | 430 | -90.5 | 504990 | 634 | -83.1 | 504990 | 98 | -88.3 | 504990 | 269 |
| MR_1774414520_80EB8C24 | 504990 | 634 | -84.6 | 504990 | 430 | -90.5 | 504990 | 98 | -88.6 | 504990 | 269 |
| MR_1774414520_361244FB | 504990 | 430 | -90.0 | 504990 | 634 | -86.0 | 504990 | 98 | -91.3 | 504990 | 269 |
| MR_1774414520_41DA0B72 | 504990 | 430 | -87.3 | 504990 | 634 | -83.6 | 504990 | 98 | -90.5 | 504990 | 269 |
| MR_1774414520_A4E4CB63 | 504990 | 430 | -88.6 | 504990 | 634 | -85.0 | 504990 | 98 | -91.0 | 504990 | 269 |
| MR_1774414520_4D80ABF9 | 504990 | 634 | -83.7 | 504990 | 430 | -87.2 | 504990 | 98 | -91.1 | 504990 | 269 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1313: `ca073467-d65...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `ca073467-d656-404a-b793-66506def6f1f` |
| Tag | **single-answer** |
| 정답 | **C18** |
| C18 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1313] topology](images/train_1313.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Add neighbor relationship between 3273720_1 and 3221373_4
- `C2`: Increase A3 Offset threshold for 3273720_1
- `C3`: Press down the tilt angle of 3273720_1 by 9 degrees
- `C4`: Lift the tilt angle  of 3221373_4 by 5 degrees
- `C5`: Increase A3 Offset threshold for 3221373_4
- `C6`: Increase transmission power for 3273720_1
- `C7`: Decrease A3 Offset threshold for 3221373_4
- `C8`: Lift the tilt angle of 3273720_1 by 9 degrees
- `C9`: Decrease transmission power for 3273720_1
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3221373_4
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3221373_4
- `C12`: Adjust the azimuth of 3221373_4 by 41 degrees
- `C13`: Adjust the azimuth of 3273720_1 by 50 degrees
- `C14`: Decrease transmission power for 3221373_4
- `C15`: Insufficient data; more data is needed for judgment.
- `C16`: Press down the tilt angle  of 3221373_4 by 5 degrees
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3273720_1
- `C18`: Check test server and transmission issues **← 정답**
- `C19`: Increase transmission power for 3221373_4
- `C20`: Decrease A3 Offset threshold for 3273720_1
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3273720_1
- `C22`: Add neighbor relationship between 3257075_2 and 3221373_4

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.666 | MS1 | 121.4656600998 | 31.1446239636 | 573 | 504990 | -87.30 | 14.61 | 404.65 | 0.06 | 2.23 | 1562 |
| 2024-09-20 22:21:32.488 | MS1 | 121.4656656398 | 31.1446345966 | 573 | 504990 | -88.98 | 17.26 | 323.19 | 0.18 | 2.26 | 1561 |
| 2024-09-20 22:21:33.872 | MS1 | 121.4656693033 | 31.1446351971 | 573 | 504990 | -87.15 | 14.15 | 525.79 | 0.19 | 2.81 | 1561 |
| 2024-09-20 22:21:34.710 | MS1 | 121.4656731422 | 31.1446278449 | 573 | 504990 | -89.94 | 15.70 | 64.03 | 0.08 | 2.54 | 361 |
| 2024-09-20 22:21:35.555 | MS1 | 121.4656596745 | 31.1446317810 | 573 | 504990 | -91.84 | 14.16 | 79.23 | 0.01 | 2.29 | 385 |
| 2024-09-20 22:21:36.333 | MS1 | 121.4656693507 | 31.1446231134 | 573 | 504990 | -88.62 | 16.15 | 105.30 | 0.05 | 2.31 | 365 |
| 2024-09-20 22:21:37.287 | MS1 | 121.4656730170 | 31.1446294442 | 573 | 504990 | -89.40 | 9.90 | 59.37 | 0.01 | 2.40 | 366 |
| 2024-09-20 22:21:38.586 | MS1 | 121.4656672443 | 31.1446358632 | 573 | 504990 | -90.88 | 8.24 | 68.78 | 0.09 | 2.39 | 457 |
| 2024-09-20 22:21:39.751 | MS1 | 121.4656612245 | 31.1446246751 | 573 | 504990 | -92.16 | 9.53 | 78.67 | 0.11 | 2.42 | 465 |
| 2024-09-20 22:21:40.457 | MS1 | 121.4656653443 | 31.1446309554 | 573 | 504990 | -90.87 | 9.80 | 588.34 | 0.18 | 2.84 | 1562 |
| 2024-09-20 22:21:41.976 | MS1 | 121.4656765057 | 31.1446253413 | 573 | 504990 | -91.31 | 12.97 | 456.89 | 0.04 | 2.01 | 1594 |
| 2024-09-20 22:21:42.631 | MS1 | 121.4656656963 | 31.1446264794 | 573 | 504990 | -92.25 | 8.66 | 492.06 | 0.13 | 2.63 | 1591 |

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
| 3221373 | 4 | 121.4728768566 | 31.1478498986 | 283 | 3 | 1 | 29.0 | TDD | 524 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3247501 | 3 | 121.4745737367 | 31.1524414499 | 35 | 1 | 10 | 35.7 | TDD | 988 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3257075 | 2 | 121.4747232877 | 31.1497901681 | 349 | 3 | 10 | 45.9 | TDD | 995 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |
| 3273720 | 1 | 121.4757740505 | 31.1550883516 | 295 | 8 | 7 | 16.2 | TDD | 573 | n41 | 504990 | 100M | 64T64R | 26 | 504990 |

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
| 2024-09-20 22:21:30.788 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.804 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:30.942 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:30.942 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.614 | NREventA3 | measId:2;ServCellPCI:42;Ser... |
| 2024-09-20 22:21:37.854 | NRHandoverAttempt | SourcePCI:42;SourceNR-ARFCN... |
| 2024-09-20 22:21:37.892 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:37.907 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.052 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.052 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3273720 | 1 | 17.4133 | 18.4578 | -114.5103 | 8.8734 | 197.3373 | 0.0028 | 0.0048 |
| 2024_09_20 22:00 | 3257075 | 2 | 11.9158 | 5.2261 | -117.0372 | 8.0964 | 189.2411 | 0.0087 | 0.0025 |
| 2024_09_20 22:00 | 3247501 | 3 | 9.0598 | 17.7781 | -116.9571 | 7.9110 | 135.8162 | 0.0079 | 0.0057 |
| 2024_09_20 22:00 | 3221373 | 4 | 9.8275 | 15.2105 | -116.3560 | 13.3963 | 102.9864 | 0.0175 | 0.0084 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412492_33C38A62 | 504990 | 573 | -90.8 | 504990 | 524 | -99.2 | 504990 | 995 | -102.3 | 504990 | 988 |
| MR_1774412492_8B50F23F | 504990 | 573 | -89.5 | 504990 | 524 | -100.0 | 504990 | 995 | -104.0 | 504990 | 988 |
| MR_1774412492_E72EB028 | 504990 | 573 | -91.6 | 504990 | 524 | -96.3 | 504990 | 995 | -104.4 | 504990 | 988 |
| MR_1774412492_4647F100 | 504990 | 573 | -89.4 | 504990 | 524 | -97.5 | 504990 | 995 | -104.1 | 504990 | 988 |
| MR_1774412492_5EDB385D | 504990 | 573 | -89.9 | 504990 | 524 | -97.3 | 504990 | 995 | -102.7 | 504990 | 988 |
| MR_1774412492_9EE19601 | 504990 | 573 | -88.3 | 504990 | 524 | -97.2 | 504990 | 995 | -104.3 | 504990 | 988 |
| MR_1774412492_06FC79CF | 504990 | 573 | -88.0 | 504990 | 524 | -96.5 | 504990 | 995 | -103.4 | 504990 | 988 |
| MR_1774412492_DA7F1F41 | 504990 | 573 | -89.8 | 504990 | 524 | -97.1 | 504990 | 995 | -103.7 | 504990 | 988 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1314: `f71f1590-0e3...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `f71f1590-0e3d-47d4-9ff0-1b96c70379f3` |
| Tag | **single-answer** |
| 정답 | **C5** |
| C5 의미 | Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3217708_2 |
| 패턴 분류 | **P10 Coverage Threshold** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1314] topology](images/train_1314.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 13 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 13개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3217708_2
- `C2`: Modify PdcchOccupiedSymbolNum to 2SYM for 3214587_6
- `C3`: Lift the tilt angle  of 3214587_6 by 5 degrees
- `C4`: Press down the tilt angle  of 3214587_6 by 5 degrees
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3217708_2 **← 정답**
- `C6`: Increase transmission power for 3214587_6
- `C7`: Press down the tilt angle of 3217708_2 by 1 degrees
- `C8`: Insufficient data; more data is needed for judgment.
- `C9`: Decrease transmission power for 3214587_6
- `C10`: Add neighbor relationship between 3219082_12 and 3214587_6
- `C11`: Lift the tilt angle of 3217708_2 by 1 degrees
- `C12`: Adjust the azimuth of 3217708_2 by 1 degrees
- `C13`: Decrease A3 Offset threshold for 3217708_2
- `C14`: Increase transmission power for 3217708_2
- `C15`: Add neighbor relationship between 3217708_2 and 3214587_6
- `C16`: Adjust the azimuth of 3214587_6 by 44 degrees
- `C17`: Decrease A3 Offset threshold for 3214587_6
- `C18`: Increase A3 Offset threshold for 3217708_2
- `C19`: Decrease transmission power for 3217708_2
- `C20`: Increase A3 Offset threshold for 3214587_6
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3214587_6
- `C22`: Check test server and transmission issues

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.878 | MS1 | 121.4656685336 | 31.1446302334 | 260 | 504990 | -94.10 | 12.89 | 379.06 | 0.05 | 2.24 | 1576 |
| 2024-09-20 22:21:32.739 | MS1 | 121.4656680449 | 31.1446185445 | 961 | 504990 | -95.61 | 14.36 | 341.07 | 0.18 | 2.17 | 1599 |
| 2024-09-20 22:21:33.493 | MS1 | 121.4656714427 | 31.1446316146 | 509 | 504990 | -93.27 | 10.54 | 488.52 | 0.08 | 2.18 | 1578 |
| 2024-09-20 22:21:34.906 | MS1 | 121.4656716007 | 31.1446313649 | 526 | 152650 | -87.36 | 6.12 | 78.26 | 0.01 | 1.66 | 922 |
| 2024-09-20 22:21:35.199 | MS1 | 121.4656676658 | 31.1446376998 | 177 | 152650 | -95.79 | 3.75 | 92.81 | 0.20 | 1.64 | 926 |
| 2024-09-20 22:21:36.337 | MS1 | 121.4656639346 | 31.1446191181 | 346 | 152650 | -94.32 | 3.84 | 94.91 | 0.17 | 1.71 | 930 |
| 2024-09-20 22:21:37.633 | MS1 | 121.4656738561 | 31.1446298868 | 636 | 152650 | -90.17 | 5.11 | 94.03 | 0.08 | 1.57 | 953 |
| 2024-09-20 22:21:38.118 | MS1 | 121.4656745582 | 31.1446189282 | 526 | 152650 | -89.73 | 4.03 | 84.28 | 0.13 | 1.53 | 983 |
| 2024-09-20 22:21:39.836 | MS1 | 121.4656677361 | 31.1446338845 | 177 | 152650 | -90.66 | 6.30 | 83.87 | 0.14 | 1.81 | 952 |
| 2024-09-20 22:21:40.546 | MS1 | 121.4656720797 | 31.1446215923 | 346 | 152650 | -96.16 | 2.45 | 95.41 | 0.07 | 2.93 | 1593 |
| 2024-09-20 22:21:41.592 | MS1 | 121.4656590163 | 31.1446351213 | 636 | 152650 | -91.92 | 6.91 | 101.34 | 0.08 | 2.53 | 1599 |
| 2024-09-20 22:21:42.832 | MS1 | 121.4656746647 | 31.1446253716 | 526 | 152650 | -90.08 | 3.94 | 84.66 | 0.15 | 2.96 | 1573 |

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
| 3213413 | 13 | 121.4731286070 | 31.1463203662 | 226 | 12 | 12 | 13.9 | FDD | 636 | n1 | 152650 | 30M | 4T4R | 17 | 152650 |
| 3214587 | 6 | 121.4735871042 | 31.1503838139 | 186 | 5 | 5 | 4.9 | TDD | 862 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |
| 3217708 | 2 | 121.4682055094 | 31.1516419870 | 196 | 1 | 2 | 6.0 | TDD | 260 | n41 | 504990 | 100M | 64T64R | 18 | 504990 |
| 3219082 | 12 | 121.4729967131 | 31.1490163333 | 315 | 15 | 11 | 0.0 | FDD | 346 | n1 | 152650 | 30M | 4T4R | 16 | 152650 |
| 3220072 | 4 | 121.4704651314 | 31.1542028488 | 304 | 0 | 4 | 17.0 | TDD | 25 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3221099 | 7 | 121.4668723334 | 31.1545219537 | 284 | 13 | 3 | 10.5 | FDD | 323 | n1 | 152650 | 30M | 4T4R | 12 | 152650 |
| 3225309 | 1 | 121.4656623472 | 31.1489858462 | 111 | 7 | 10 | 19.9 | TDD | 961 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3229009 | 5 | 121.4750357701 | 31.1506881457 | 195 | 1 | 2 | 8.3 | TDD | 509 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3248745 | 10 | 121.4704433302 | 31.1507403058 | 157 | 3 | 0 | 15.6 | FDD | 559 | n1 | 152650 | 30M | 4T4R | 24 | 152650 |
| 3253937 | 8 | 121.4750308219 | 31.1532508265 | 108 | 15 | 6 | 22.4 | FDD | 263 | n1 | 152650 | 30M | 4T4R | 18 | 152650 |
| 3260208 | 9 | 121.4755187075 | 31.1524119412 | 332 | 7 | 11 | 2.9 | FDD | 526 | n1 | 152650 | 30M | 4T4R | 11 | 152650 |
| 3273668 | 11 | 121.4728740681 | 31.1534562077 | 293 | 13 | 9 | 16.7 | FDD | 177 | n1 | 152650 | 30M | 4T4R | 20 | 152650 |
| 3277035 | 3 | 121.4685396894 | 31.1554167780 | 308 | 12 | 2 | 20.4 | TDD | 940 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:31.508 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.530 | NRRandomAccessSuc | Delay：22ms |
| 2024-09-20 22:21:31.665 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.665 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:35.343 | NREventA2 | measId:1;ServCellPCI:382;Se... |
| 2024-09-20 22:21:35.493 | NREventA5MeasConfig | measId:3;NR-ARFCN:152650;a5... |
| 2024-09-20 22:21:35.767 | NREventA5 | measId:3;ServCellPCI:382;Se... |
| 2024-09-20 22:21:35.838 | NRHandoverAttempt | SourcePCI:382;SourceNR-ARFC... |
| 2024-09-20 22:21:35.860 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:35.874 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:36.015 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:36.015 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3225309 | 1 | 14.0913 | 11.1862 | -114.9277 | 9.5599 | 110.5384 | 0.0134 | 0.0187 |
| 2024_09_20 22:00 | 3217708 | 2 | 8.0861 | 9.7261 | -115.4179 | 8.9882 | 174.8373 | 0.0051 | 0.0092 |
| 2024_09_20 22:00 | 3277035 | 3 | 10.7443 | 17.6583 | -117.1325 | 10.7679 | 131.7668 | 0.0025 | 0.0142 |
| 2024_09_20 22:00 | 3220072 | 4 | 16.9031 | 16.5522 | -116.3418 | 17.3285 | 93.4262 | 0.0199 | 0.0111 |
| 2024_09_20 22:00 | 3229009 | 5 | 18.2779 | 13.6538 | -117.7838 | 14.4778 | 110.7804 | 0.0067 | 0.0103 |
| 2024_09_20 22:00 | 3214587 | 6 | 8.0484 | 16.6409 | -115.7374 | 6.3268 | 109.0378 | 0.0029 | 0.0000 |
| 2024_09_20 22:00 | 3221099 | 7 | 18.4328 | 14.1735 | -116.8691 | 4.3062 | 29.4590 | 0.0008 | 0.0132 |
| 2024_09_20 22:00 | 3253937 | 8 | 16.6908 | 16.7881 | -116.0171 | 4.8641 | 42.2611 | 0.0101 | 0.0040 |
| 2024_09_20 22:00 | 3260208 | 9 | 7.4888 | 12.9307 | -116.0353 | 4.2508 | 44.6836 | 0.0029 | 0.0171 |
| 2024_09_20 22:00 | 3248745 | 10 | 11.1568 | 17.8713 | -116.8778 | 3.7080 | 20.3777 | 0.0109 | 0.0096 |
| 2024_09_20 22:00 | 3273668 | 11 | 11.4968 | 7.6764 | -117.6671 | 4.2469 | 23.2150 | 0.0113 | 0.0193 |
| 2024_09_20 22:00 | 3219082 | 12 | 14.4145 | 8.8041 | -116.2785 | 3.8987 | 52.5518 | 0.0189 | 0.0133 |
| 2024_09_20 22:00 | 3213413 | 13 | 9.6087 | 9.3691 | -116.8919 | 4.4925 | 55.6736 | 0.0135 | 0.0049 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414790_52C9C9D4 | 152650 | 526 | -88.7 | 152650 | 323 | -94.4 | 152650 | 263 | -98.0 | 152650 | 559 |
| MR_1774414790_C683F687 | 504990 | 509 | -93.5 | 504990 | 862 | -92.2 | 504990 | 25 | -99.8 | 504990 | 940 |
| MR_1774414790_FC7776BB | 504990 | 509 | -92.4 | 504990 | 862 | -93.4 | 504990 | 25 | -100.7 | 504990 | 940 |
| MR_1774414790_632D425A | 504990 | 509 | -91.8 | 504990 | 862 | -94.6 | 504990 | 25 | -99.6 | 504990 | 940 |
| MR_1774414790_9C5050DB | 152650 | 526 | -86.7 | 152650 | 323 | -93.3 | 152650 | 263 | -96.3 | 152650 | 559 |
| MR_1774414790_79253857 | 152650 | 526 | -85.4 | 152650 | 323 | -92.0 | 152650 | 263 | -98.5 | 152650 | 559 |
| MR_1774414790_4A9326C8 | 504990 | 509 | -95.2 | 504990 | 862 | -93.3 | 504990 | 25 | -100.6 | 504990 | 940 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1315: `80bd2a05-8be...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `80bd2a05-8be6-47fd-8a07-dcaae0d703b2` |
| Tag | **single-answer** |
| 정답 | **C16** |
| C16 의미 | Insufficient data; more data is needed for judgment. |
| 패턴 분류 | **P7 Insufficient Data** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1315] topology](images/train_1315.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3216297_4
- `C2`: Adjust the azimuth of 3216297_4 by 50 degrees
- `C3`: Press down the tilt angle  of 3273435_3 by 6 degrees
- `C4`: Decrease transmission power for 3273435_3
- `C5`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3273435_3
- `C6`: Decrease A3 Offset threshold for 3273435_3
- `C7`: Decrease transmission power for 3216297_4
- `C8`: Increase A3 Offset threshold for 3216297_4
- `C9`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3216297_4
- `C10`: Check test server and transmission issues
- `C11`: Increase transmission power for 3273435_3
- `C12`: Press down the tilt angle of 3216297_4 by 8 degrees
- `C13`: Lift the tilt angle of 3216297_4 by 8 degrees
- `C14`: Add neighbor relationship between 3216297_4 and 3273435_3
- `C15`: Modify PdcchOccupiedSymbolNum to 2SYM for 3273435_3
- `C16`: Insufficient data; more data is needed for judgment. **← 정답**
- `C17`: Lift the tilt angle  of 3273435_3 by 6 degrees
- `C18`: Add neighbor relationship between 3266592_1 and 3273435_3
- `C19`: Increase transmission power for 3216297_4
- `C20`: Decrease A3 Offset threshold for 3216297_4
- `C21`: Adjust the azimuth of 3273435_3 by 50 degrees
- `C22`: Increase A3 Offset threshold for 3273435_3

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.314 | MS1 | 121.4656657653 | 31.1446190221 | 998 | 504990 | -91.22 | 15.87 | 500.96 | 0.18 | 2.57 | 1595 |
| 2024-09-20 22:21:32.195 | MS1 | 121.4656642981 | 31.1446312652 | 998 | 504990 | -87.56 | 15.14 | 430.76 | 0.18 | 2.85 | 1563 |
| 2024-09-20 22:21:33.231 | MS1 | 121.4656722685 | 31.1446273259 | 998 | 504990 | -89.36 | 12.64 | 537.10 | 0.01 | 2.25 | 1578 |
| 2024-09-20 22:21:34.933 | MS1 | 121.4656615180 | 31.1446231216 | 998 | 504990 | -91.11 | 14.07 | 98.93 | 0.14 | 2.11 | 1586 |
| 2024-09-20 22:21:35.988 | MS1 | 121.4656666243 | 31.1446258319 | 998 | 504990 | -89.08 | 16.55 | 57.02 | 0.00 | 2.51 | 1564 |
| 2024-09-20 22:21:36.686 | MS1 | 121.4656649804 | 31.1446256248 | 998 | 504990 | -89.03 | 17.11 | 59.15 | 0.01 | 2.20 | 1582 |
| 2024-09-20 22:21:37.566 | MS1 | 121.4656697555 | 31.1446285457 | 998 | 504990 | -92.56 | 11.64 | 98.01 | 0.15 | 2.16 | 1581 |
| 2024-09-20 22:21:38.890 | MS1 | 121.4656711127 | 31.1446267499 | 998 | 504990 | -93.67 | 10.36 | 78.87 | 0.01 | 2.36 | 1560 |
| 2024-09-20 22:21:39.683 | MS1 | 121.4656764785 | 31.1446328604 | 998 | 504990 | -91.54 | 8.28 | 58.94 | 0.03 | 2.63 | 1576 |
| 2024-09-20 22:21:40.760 | MS1 | 121.4656698289 | 31.1446275378 | 998 | 504990 | -93.35 | 10.39 | 398.70 | 0.04 | 2.20 | 1591 |
| 2024-09-20 22:21:41.242 | MS1 | 121.4656645156 | 31.1446211032 | 998 | 504990 | -93.66 | 11.57 | 362.98 | 0.09 | 2.98 | 1579 |
| 2024-09-20 22:21:42.794 | MS1 | 121.4656735579 | 31.1446358614 | 998 | 504990 | -89.75 | 11.34 | 505.77 | 0.20 | 2.69 | 1572 |

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
| 3216297 | 4 | 121.4653927176 | 31.1510009312 | 250 | 5 | 10 | 39.9 | TDD | 998 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3256856 | 2 | 121.4755517124 | 31.1512208340 | 12 | 11 | 7 | 35.1 | TDD | 826 | n41 | 504990 | 100M | 64T64R | 21 | 504990 |
| 3266592 | 1 | 121.4713841570 | 31.1446325209 | 151 | 0 | 10 | 30.2 | TDD | 424 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3273435 | 3 | 121.4682274770 | 31.1540886185 | 44 | 5 | 10 | 28.2 | TDD | 694 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:31.265 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.280 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:31.402 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.402 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.084 | NREventA3 | measId:2;ServCellPCI:20;Ser... |
| 2024-09-20 22:21:38.324 | NRHandoverAttempt | SourcePCI:20;SourceNR-ARFCN... |
| 2024-09-20 22:21:38.367 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.381 | NRRandomAccessSuc | Delay：14ms |
| 2024-09-20 22:21:38.529 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.529 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_19 22:00 | 3266592 | 1 | 81.0321 | 89.9758 | -114.7605 | 9.5589 | 140.9976 | 0.0157 | 0.0052 |
| 2024_09_19 22:00 | 3256856 | 2 | 83.5040 | 84.0233 | -115.7501 | 6.9530 | 173.4713 | 0.0012 | 0.0057 |
| 2024_09_19 22:00 | 3273435 | 3 | 83.9903 | 89.8976 | -116.0295 | 9.4290 | 96.4917 | 0.0132 | 0.0048 |
| 2024_09_19 22:00 | 3216297 | 4 | 90.1498 | 88.7398 | -115.7178 | 13.6891 | 169.0144 | 0.0197 | 0.0183 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774413254_72CA0B94 | 504990 | 998 | -89.2 | 504990 | 694 | -98.5 | 504990 | 424 | -99.9 | 504990 | 826 |
| MR_1774413254_411321EA | 504990 | 998 | -90.4 | 504990 | 694 | -99.3 | 504990 | 424 | -101.2 | 504990 | 826 |
| MR_1774413254_52D5B74D | 504990 | 998 | -91.3 | 504990 | 694 | -99.3 | 504990 | 424 | -103.3 | 504990 | 826 |
| MR_1774413254_26443E76 | 504990 | 998 | -90.4 | 504990 | 694 | -100.3 | 504990 | 424 | -100.9 | 504990 | 826 |
| MR_1774413254_C0491C01 | 504990 | 998 | -90.8 | 504990 | 694 | -101.0 | 504990 | 424 | -103.4 | 504990 | 826 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1316: `e547cbd6-73a...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `e547cbd6-73ab-4014-bdcd-0f4ff58a93c4` |
| Tag | **single-answer** |
| 정답 | **C9** |
| C9 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1316] topology](images/train_1316.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Adjust the azimuth of 3234395_1 by 48 degrees
- `C2`: Decrease A3 Offset threshold for 3234395_1
- `C3`: Increase transmission power for 3234395_1
- `C4`: Adjust the azimuth of 3244455_2 by 26 degrees
- `C5`: Increase transmission power for 3244455_2
- `C6`: Add neighbor relationship between 3255171_4 and 3244455_2
- `C7`: Lift the tilt angle of 3234395_1 by 8 degrees
- `C8`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3234395_1
- `C9`: Check test server and transmission issues **← 정답**
- `C10`: Decrease transmission power for 3234395_1
- `C11`: Modify PdcchOccupiedSymbolNum to 2SYM for 3234395_1
- `C12`: Press down the tilt angle  of 3244455_2 by 10 degrees
- `C13`: Modify PdcchOccupiedSymbolNum to 2SYM for 3244455_2
- `C14`: Lift the tilt angle  of 3244455_2 by 10 degrees
- `C15`: Increase A3 Offset threshold for 3234395_1
- `C16`: Add neighbor relationship between 3234395_1 and 3244455_2
- `C17`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3244455_2
- `C18`: Press down the tilt angle of 3234395_1 by 8 degrees
- `C19`: Decrease transmission power for 3244455_2
- `C20`: Decrease A3 Offset threshold for 3244455_2
- `C21`: Insufficient data; more data is needed for judgment.
- `C22`: Increase A3 Offset threshold for 3244455_2

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.100 | MS1 | 121.4656607982 | 31.1446213694 | 562 | 504990 | -90.50 | 15.43 | 565.51 | 0.19 | 2.89 | 1560 |
| 2024-09-20 22:21:32.125 | MS1 | 121.4656734843 | 31.1446283489 | 562 | 504990 | -90.51 | 17.97 | 392.95 | 0.16 | 2.39 | 1585 |
| 2024-09-20 22:21:33.905 | MS1 | 121.4656748995 | 31.1446261760 | 562 | 504990 | -86.20 | 16.18 | 512.80 | 0.16 | 2.04 | 1564 |
| 2024-09-20 22:21:34.566 | MS1 | 121.4656729171 | 31.1446237251 | 562 | 504990 | -85.68 | 14.74 | 88.05 | 0.19 | 2.16 | 489 |
| 2024-09-20 22:21:35.875 | MS1 | 121.4656618985 | 31.1446356311 | 562 | 504990 | -91.09 | 17.63 | 54.55 | 0.13 | 2.48 | 369 |
| 2024-09-20 22:21:36.169 | MS1 | 121.4656758828 | 31.1446349238 | 562 | 504990 | -86.02 | 16.20 | 65.34 | 0.01 | 2.82 | 429 |
| 2024-09-20 22:21:37.406 | MS1 | 121.4656771938 | 31.1446250121 | 562 | 504990 | -91.71 | 11.53 | 66.40 | 0.20 | 2.03 | 403 |
| 2024-09-20 22:21:38.323 | MS1 | 121.4656750790 | 31.1446378841 | 562 | 504990 | -90.57 | 10.32 | 56.80 | 0.17 | 2.48 | 404 |
| 2024-09-20 22:21:39.210 | MS1 | 121.4656718001 | 31.1446246312 | 562 | 504990 | -93.04 | 9.62 | 57.76 | 0.03 | 2.35 | 335 |
| 2024-09-20 22:21:40.872 | MS1 | 121.4656722081 | 31.1446297894 | 562 | 504990 | -93.29 | 8.41 | 515.77 | 0.09 | 2.63 | 1600 |
| 2024-09-20 22:21:41.968 | MS1 | 121.4656606618 | 31.1446356156 | 562 | 504990 | -93.77 | 10.94 | 498.82 | 0.17 | 2.11 | 1565 |
| 2024-09-20 22:21:42.618 | MS1 | 121.4656750458 | 31.1446343632 | 562 | 504990 | -90.49 | 7.71 | 436.06 | 0.02 | 2.09 | 1580 |

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
| 3234395 | 1 | 121.4721031469 | 31.1536649205 | 259 | 6 | 0 | 41.0 | TDD | 562 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3244455 | 2 | 121.4693803568 | 31.1451607964 | 235 | 15 | 12 | 28.9 | TDD | 397 | n41 | 504990 | 100M | 64T64R | 24 | 504990 |
| 3255171 | 4 | 121.4731413598 | 31.1547902886 | 282 | 9 | 5 | 33.9 | TDD | 783 | n41 | 504990 | 100M | 64T64R | 16 | 504990 |
| 3257828 | 3 | 121.4707407546 | 31.1559452515 | 84 | 12 | 11 | 28.2 | TDD | 917 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:30.859 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.883 | NRRandomAccessSuc | Delay：24ms |
| 2024-09-20 22:21:31.014 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.014 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:37.735 | NREventA3 | measId:2;ServCellPCI:465;Se... |
| 2024-09-20 22:21:37.975 | NRHandoverAttempt | SourcePCI:465;SourceNR-ARFC... |
| 2024-09-20 22:21:38.018 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.029 | NRRandomAccessSuc | Delay：11ms |
| 2024-09-20 22:21:38.157 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.157 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3234395 | 1 | 6.0919 | 19.9156 | -116.4126 | 17.6029 | 160.5124 | 0.0065 | 0.0129 |
| 2024_09_20 22:00 | 3244455 | 2 | 12.1106 | 10.2264 | -115.6217 | 16.3550 | 176.4150 | 0.0122 | 0.0173 |
| 2024_09_20 22:00 | 3257828 | 3 | 7.6830 | 9.7612 | -115.8326 | 8.5765 | 92.5839 | 0.0187 | 0.0046 |
| 2024_09_20 22:00 | 3255171 | 4 | 5.0276 | 13.1462 | -115.6504 | 12.6140 | 132.6927 | 0.0109 | 0.0070 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774414053_40166B52 | 504990 | 562 | -84.8 | 504990 | 397 | -88.9 | 504990 | 783 | -98.1 | 504990 | 917 |
| MR_1774414053_0EDEFED7 | 504990 | 562 | -86.7 | 504990 | 397 | -88.9 | 504990 | 783 | -100.0 | 504990 | 917 |
| MR_1774414053_6F3F0BBB | 504990 | 562 | -87.3 | 504990 | 397 | -90.8 | 504990 | 783 | -96.5 | 504990 | 917 |
| MR_1774414053_E3EDCDF2 | 504990 | 562 | -84.6 | 504990 | 397 | -91.3 | 504990 | 783 | -96.9 | 504990 | 917 |
| MR_1774414053_DE3C68CA | 504990 | 562 | -84.4 | 504990 | 397 | -90.5 | 504990 | 783 | -99.5 | 504990 | 917 |
| MR_1774414053_774DEB2E | 504990 | 562 | -84.0 | 504990 | 397 | -88.5 | 504990 | 783 | -96.4 | 504990 | 917 |
| MR_1774414053_24ECD988 | 504990 | 562 | -84.9 | 504990 | 397 | -87.7 | 504990 | 783 | -96.6 | 504990 | 917 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1317: `33863515-9cc...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `33863515-9cc6-4e26-a027-a5d6b14d1288` |
| Tag | **single-answer** |
| 정답 | **C6** |
| C6 의미 | Add neighbor relationship between 3231690_1 and 3228846_4 |
| 패턴 분류 | **P9 Missing Neighbor** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1317] topology](images/train_1317.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3231690_1 by 10 degrees
- `C2`: Increase transmission power for 3228846_4
- `C3`: Modify PdcchOccupiedSymbolNum to 2SYM for 3231690_1
- `C4`: Increase A3 Offset threshold for 3231690_1
- `C5`: Decrease transmission power for 3231690_1
- `C6`: Add neighbor relationship between 3231690_1 and 3228846_4 **← 정답**
- `C7`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3231690_1
- `C8`: Adjust the azimuth of 3231690_1 by 50 degrees
- `C9`: Add neighbor relationship between 3269865_2 and 3228846_4
- `C10`: Press down the tilt angle of 3231690_1 by 10 degrees
- `C11`: Adjust the azimuth of 3228846_4 by 22 degrees
- `C12`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3228846_4
- `C13`: Insufficient data; more data is needed for judgment.
- `C14`: Check test server and transmission issues
- `C15`: Lift the tilt angle  of 3228846_4 by 5 degrees
- `C16`: Decrease transmission power for 3228846_4
- `C17`: Decrease A3 Offset threshold for 3231690_1
- `C18`: Increase A3 Offset threshold for 3228846_4
- `C19`: Increase transmission power for 3231690_1
- `C20`: Decrease A3 Offset threshold for 3228846_4
- `C21`: Modify PdcchOccupiedSymbolNum to 2SYM for 3228846_4
- `C22`: Press down the tilt angle  of 3228846_4 by 5 degrees

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.472 | MS1 | 121.4656711139 | 31.1446340749 | 603 | 504990 | -81.84 | 16.26 | 356.81 | 0.20 | 2.59 | 1583 |
| 2024-09-20 22:21:32.656 | MS1 | 121.4656768057 | 31.1446287665 | 603 | 504990 | -78.34 | 17.88 | 411.17 | 0.08 | 2.32 | 1569 |
| 2024-09-20 22:21:33.601 | MS1 | 121.4656760715 | 31.1446257507 | 603 | 504990 | -84.25 | 13.55 | 397.42 | 0.18 | 2.78 | 1576 |
| 2024-09-20 22:21:34.124 | MS1 | 121.4656698981 | 31.1446290794 | 603 | 504990 | -86.01 | -3.89 | 45.59 | 0.19 | 1.07 | 1596 |
| 2024-09-20 22:21:35.330 | MS1 | 121.4656661712 | 31.1446271881 | 603 | 504990 | -93.57 | -0.42 | 28.51 | 0.19 | 1.29 | 1567 |
| 2024-09-20 22:21:36.106 | MS1 | 121.4656727343 | 31.1446191657 | 603 | 504990 | -90.94 | -2.91 | 52.91 | 0.02 | 1.29 | 1582 |
| 2024-09-20 22:21:37.783 | MS1 | 121.4656594972 | 31.1446275979 | 603 | 504990 | -85.99 | -2.14 | 60.22 | 0.02 | 1.01 | 1594 |
| 2024-09-20 22:21:38.710 | MS1 | 121.4656657852 | 31.1446310295 | 603 | 504990 | -75.75 | 16.68 | 549.53 | 0.07 | 1.22 | 1573 |
| 2024-09-20 22:21:39.690 | MS1 | 121.4656768554 | 31.1446268225 | 603 | 504990 | -77.86 | 13.88 | 450.28 | 0.11 | 1.47 | 1574 |
| 2024-09-20 22:21:40.565 | MS1 | 121.4656722228 | 31.1446180277 | 603 | 504990 | -83.53 | 17.78 | 555.82 | 0.07 | 2.33 | 1574 |
| 2024-09-20 22:21:41.764 | MS1 | 121.4656707635 | 31.1446269425 | 603 | 504990 | -83.50 | 16.73 | 469.86 | 0.17 | 2.90 | 1564 |
| 2024-09-20 22:21:42.218 | MS1 | 121.4656660206 | 31.1446195876 | 603 | 504990 | -79.83 | 13.71 | 500.10 | 0.05 | 2.08 | 1582 |

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
| 3228846 | 4 | 121.4688589101 | 31.1449907744 | 240 | 1 | 11 | 19.7 | TDD | 543 | n41 | 504990 | 100M | 64T64R | 22 | 504990 |
| 3231690 | 1 | 121.4690029336 | 31.1525712191 | 126 | 15 | 1 | 49.9 | TDD | 603 | n41 | 504990 | 100M | 64T64R | 29 | 504990 |
| 3260602 | 3 | 121.4692611712 | 31.1555523707 | 61 | 13 | 1 | 28.0 | TDD | 694 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3269865 | 2 | 121.4684875360 | 31.1448216303 | 209 | 11 | 10 | 35.6 | TDD | 222 | n41 | 504990 | 100M | 64T64R | 13 | 504990 |

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
| 2024-09-20 22:21:30.891 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:30.914 | NRRandomAccessSuc | Delay：23ms |
| 2024-09-20 22:21:31.032 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.032 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:34.709 | NREventA3 | measId:2;ServCellPCI:58;Ser... |
| 2024-09-20 22:21:35.709 | NREventA3 | measId:2;ServCellPCI:58;Ser... |
| 2024-09-20 22:21:36.709 | NREventA3 | measId:2;ServCellPCI:58;Ser... |
| 2024-09-20 22:21:39.209 | NRRRCReestablishAttempt | PCI:58 |
| 2024-09-20 22:21:39.222 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:39.235 | NRRandomAccessSuc | Delay：13ms |
| 2024-09-20 22:21:39.365 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:39.365 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3231690 | 1 | 12.8593 | 13.4043 | -116.5774 | 5.0747 | 104.7351 | 0.0131 | 0.1156 |
| 2024_09_20 22:00 | 3269865 | 2 | 7.5908 | 10.8113 | -114.4835 | 10.2397 | 154.5010 | 0.0027 | 0.0091 |
| 2024_09_20 22:00 | 3260602 | 3 | 7.1546 | 10.8502 | -116.2092 | 17.6611 | 144.4804 | 0.0011 | 0.0025 |
| 2024_09_20 22:00 | 3228846 | 4 | 11.4618 | 16.2067 | -117.2285 | 13.2077 | 87.3729 | 0.0040 | 0.0130 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774416629_E58493AD | 504990 | 543 | -81.8 | 504990 | 603 | -85.6 | 504990 | 222 | -84.7 | 504990 | 694 |
| MR_1774416629_D9B34600 | 504990 | 543 | -83.3 | 504990 | 603 | -88.0 | 504990 | 222 | -84.7 | 504990 | 694 |
| MR_1774416629_4B91A6C9 | 504990 | 603 | -87.2 | 504990 | 543 | -80.3 | 504990 | 222 | -83.8 | 504990 | 694 |
| MR_1774416629_E3CD598A | 504990 | 543 | -79.8 | 504990 | 603 | -87.5 | 504990 | 222 | -86.2 | 504990 | 694 |
| MR_1774416629_C5560DF4 | 504990 | 603 | -85.0 | 504990 | 543 | -79.9 | 504990 | 222 | -86.0 | 504990 | 694 |
| MR_1774416629_521103B1 | 504990 | 543 | -81.7 | 504990 | 603 | -87.1 | 504990 | 222 | -83.4 | 504990 | 694 |
| MR_1774416629_D4C87016 | 504990 | 543 | -81.1 | 504990 | 603 | -87.8 | 504990 | 222 | -85.7 | 504990 | 694 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1318: `fe57cb75-6e8...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `fe57cb75-6e86-4f9f-bdc2-3855218a20f5` |
| Tag | **single-answer** |
| 정답 | **C22** |
| C22 의미 | Check test server and transmission issues |
| 패턴 분류 | **P5 Server Issue** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1318] topology](images/train_1318.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Modify PdcchOccupiedSymbolNum to 2SYM for 3274622_4
- `C2`: Increase transmission power for 3274622_4
- `C3`: Insufficient data; more data is needed for judgment.
- `C4`: Increase A3 Offset threshold for 3226826_2
- `C5`: Press down the tilt angle of 3274622_4 by 6 degrees
- `C6`: Decrease transmission power for 3226826_2
- `C7`: Modify PdcchOccupiedSymbolNum to 2SYM for 3226826_2
- `C8`: Add neighbor relationship between 3216376_1 and 3226826_2
- `C9`: Increase A3 Offset threshold for 3274622_4
- `C10`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3274622_4
- `C11`: Adjust the azimuth of 3226826_2 by 50 degrees
- `C12`: Decrease A3 Offset threshold for 3274622_4
- `C13`: Decrease transmission power for 3274622_4
- `C14`: Decrease A3 Offset threshold for 3226826_2
- `C15`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3226826_2
- `C16`: Increase transmission power for 3226826_2
- `C17`: Press down the tilt angle  of 3226826_2 by 10 degrees
- `C18`: Lift the tilt angle of 3274622_4 by 6 degrees
- `C19`: Add neighbor relationship between 3274622_4 and 3226826_2
- `C20`: Adjust the azimuth of 3274622_4 by 50 degrees
- `C21`: Lift the tilt angle  of 3226826_2 by 10 degrees
- `C22`: Check test server and transmission issues **← 정답**

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.491 | MS1 | 121.4656745888 | 31.1446366118 | 991 | 504990 | -90.08 | 14.74 | 314.05 | 0.04 | 2.32 | 1577 |
| 2024-09-20 22:21:32.545 | MS1 | 121.4656584803 | 31.1446298920 | 991 | 504990 | -85.04 | 15.22 | 495.25 | 0.07 | 2.21 | 1600 |
| 2024-09-20 22:21:33.886 | MS1 | 121.4656693634 | 31.1446293102 | 991 | 504990 | -88.68 | 16.72 | 425.79 | 0.05 | 2.02 | 1564 |
| 2024-09-20 22:21:34.241 | MS1 | 121.4656655139 | 31.1446304091 | 991 | 504990 | -90.36 | 15.39 | 74.93 | 0.10 | 2.40 | 359 |
| 2024-09-20 22:21:35.640 | MS1 | 121.4656716015 | 31.1446222510 | 991 | 504990 | -89.45 | 15.30 | 96.49 | 0.19 | 2.77 | 380 |
| 2024-09-20 22:21:36.266 | MS1 | 121.4656590731 | 31.1446234757 | 991 | 504990 | -91.96 | 17.44 | 69.25 | 0.18 | 2.08 | 396 |
| 2024-09-20 22:21:37.127 | MS1 | 121.4656714208 | 31.1446356312 | 991 | 504990 | -90.03 | 10.34 | 84.16 | 0.16 | 2.77 | 377 |
| 2024-09-20 22:21:38.788 | MS1 | 121.4656677057 | 31.1446350193 | 991 | 504990 | -90.55 | 10.58 | 55.18 | 0.16 | 2.91 | 494 |
| 2024-09-20 22:21:39.877 | MS1 | 121.4656736066 | 31.1446377013 | 991 | 504990 | -90.81 | 11.64 | 92.24 | 0.06 | 2.85 | 498 |
| 2024-09-20 22:21:40.732 | MS1 | 121.4656777539 | 31.1446349044 | 991 | 504990 | -90.83 | 11.02 | 543.08 | 0.16 | 2.05 | 1572 |
| 2024-09-20 22:21:41.818 | MS1 | 121.4656590338 | 31.1446271386 | 991 | 504990 | -89.75 | 11.90 | 578.97 | 0.07 | 2.27 | 1581 |
| 2024-09-20 22:21:42.691 | MS1 | 121.4656711352 | 31.1446269066 | 991 | 504990 | -90.43 | 9.30 | 394.15 | 0.08 | 2.19 | 1587 |

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
| 3212231 | 3 | 121.4752039864 | 31.1462050672 | 320 | 3 | 2 | 33.6 | TDD | 614 | n41 | 504990 | 100M | 64T64R | 15 | 504990 |
| 3216376 | 1 | 121.4665620940 | 31.1526824053 | 174 | 8 | 7 | 16.5 | TDD | 594 | n41 | 504990 | 100M | 64T64R | 20 | 504990 |
| 3226826 | 2 | 121.4707941161 | 31.1525066386 | 285 | 13 | 10 | 29.0 | TDD | 133 | n41 | 504990 | 100M | 64T64R | 30 | 504990 |
| 3274622 | 4 | 121.4645305036 | 31.1494100876 | 116 | 3 | 4 | 27.3 | TDD | 991 | n41 | 504990 | 100M | 64T64R | 12 | 504990 |

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
| 2024-09-20 22:21:31.317 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.333 | NRRandomAccessSuc | Delay：16ms |
| 2024-09-20 22:21:31.462 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.462 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.180 | NREventA3 | measId:2;ServCellPCI:607;Se... |
| 2024-09-20 22:21:38.420 | NRHandoverAttempt | SourcePCI:607;SourceNR-ARFC... |
| 2024-09-20 22:21:38.466 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.481 | NRRandomAccessSuc | Delay：15ms |
| 2024-09-20 22:21:38.607 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.607 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3216376 | 1 | 6.2788 | 12.9674 | -114.8027 | 5.9371 | 157.6118 | 0.0158 | 0.0052 |
| 2024_09_20 22:00 | 3226826 | 2 | 16.2842 | 7.1644 | -114.6625 | 16.3216 | 195.9219 | 0.0171 | 0.0103 |
| 2024_09_20 22:00 | 3212231 | 3 | 15.4787 | 9.2211 | -114.7310 | 6.0224 | 82.5555 | 0.0127 | 0.0128 |
| 2024_09_20 22:00 | 3274622 | 4 | 7.4060 | 18.2255 | -114.4649 | 15.4588 | 137.1703 | 0.0091 | 0.0047 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412368_1D0C25B0 | 504990 | 991 | -91.8 | 504990 | 133 | -100.3 | 504990 | 594 | -99.7 | 504990 | 614 |
| MR_1774412368_8C276D06 | 504990 | 991 | -89.6 | 504990 | 133 | -100.4 | 504990 | 594 | -98.3 | 504990 | 614 |
| MR_1774412368_B1561ADC | 504990 | 991 | -90.5 | 504990 | 133 | -99.2 | 504990 | 594 | -99.3 | 504990 | 614 |
| MR_1774412368_E340B686 | 504990 | 991 | -90.6 | 504990 | 133 | -100.9 | 504990 | 594 | -97.2 | 504990 | 614 |
| MR_1774412368_557C2F55 | 504990 | 991 | -91.7 | 504990 | 133 | -97.0 | 504990 | 594 | -97.5 | 504990 | 614 |
| MR_1774412368_4E88FA87 | 504990 | 991 | -91.6 | 504990 | 133 | -99.9 | 504990 | 594 | -100.4 | 504990 | 614 |
| MR_1774412368_55D951F1 | 504990 | 991 | -89.5 | 504990 | 133 | -98.5 | 504990 | 594 | -98.6 | 504990 | 614 |
| MR_1774412368_F636A348 | 504990 | 991 | -91.3 | 504990 | 133 | -99.4 | 504990 | 594 | -97.3 | 504990 | 614 |

> *... 2개 열 생략 (전체 14열)*

---

### 문제 1319: `0b10534d-ef8...`

| 항목 | 값 |
| --- | --- |
| Scenario ID | `0b10534d-ef87-4304-a41b-b309a3ae1129` |
| Tag | **single-answer** |
| 정답 | **C2** |
| C2 의미 | Decrease A3 Offset threshold for 3261077_4 |
| 패턴 분류 | **P1 Late Handover** |

**시각화 (기지국 배치 + UE 시계열)**

![train[1319] topology](images/train_1319.png)

> **배경**: A network engineer conducted drive testing with a user equipment (UE) mounted on a moving vehicle across a region covered by 4 base stations (BSs), simulating a realistic 5G wireless network.
> 네트워크: 5G, 기지국 4개, 시나리오: vehicle-based drive test

**선택지 (22개)**

- `C1`: Lift the tilt angle of 3261077_4 by 10 degrees
- `C2`: Decrease A3 Offset threshold for 3261077_4 **← 정답**
- `C3`: Add neighbor relationship between 3238550_2 and 3220132_1
- `C4`: Decrease transmission power for 3261077_4
- `C5`: Press down the tilt angle of 3261077_4 by 10 degrees
- `C6`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3261077_4
- `C7`: Adjust the azimuth of 3261077_4 by 50 degrees
- `C8`: Increase transmission power for 3261077_4
- `C9`: Check test server and transmission issues
- `C10`: Add neighbor relationship between 3261077_4 and 3220132_1
- `C11`: Lift the tilt angle  of 3220132_1 by 5 degrees
- `C12`: Increase transmission power for 3220132_1
- `C13`: Decrease transmission power for 3220132_1
- `C14`: Modify PdcchOccupiedSymbolNum to 2SYM for 3220132_1
- `C15`: Increase A3 Offset threshold for 3220132_1
- `C16`: Increase A3 Offset threshold for 3261077_4
- `C17`: Adjust the azimuth of 3220132_1 by 46 degrees
- `C18`: Press down the tilt angle  of 3220132_1 by 5 degrees
- `C19`: Decrease A3 Offset threshold for 3220132_1
- `C20`: Modify PdcchOccupiedSymbolNum to 2SYM for 3261077_4
- `C21`: Decrease CovInterFreqA2RsrpThld and CovInterFreqA5RsrpThld1 thresholds for 3220132_1
- `C22`: Insufficient data; more data is needed for judgment.

**UE 측정 데이터 (User Plane)**

| Timestamp | UE | Longitude | Latitude | PCI | ARFCN | SS-RSRP (dBm) | SS-SINR (dB) | DL Throughput (Mbps) | CCE Fail Rate | Avg Rank | Grant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024-09-20 22:21:31.944 | MS1 | 121.4656584658 | 31.1446244823 | 221 | 504990 | -79.21 | 16.64 | 546.33 | 0.11 | 2.27 | 1588 |
| 2024-09-20 22:21:32.589 | MS1 | 121.4656762731 | 31.1446231658 | 221 | 504990 | -78.81 | 15.36 | 502.11 | 0.07 | 2.18 | 1597 |
| 2024-09-20 22:21:33.816 | MS1 | 121.4656775840 | 31.1446260120 | 221 | 504990 | -75.31 | 12.54 | 410.61 | 0.12 | 2.30 | 1589 |
| 2024-09-20 22:21:34.831 | MS1 | 121.4656735817 | 31.1446378455 | 221 | 504990 | -84.94 | -2.57 | 54.86 | 0.15 | 1.10 | 1586 |
| 2024-09-20 22:21:35.767 | MS1 | 121.4656723887 | 31.1446215432 | 221 | 504990 | -85.22 | -2.91 | 78.51 | 0.15 | 1.20 | 1575 |
| 2024-09-20 22:21:36.974 | MS1 | 121.4656596653 | 31.1446281316 | 221 | 504990 | -86.22 | -1.87 | 71.30 | 0.07 | 1.17 | 1574 |
| 2024-09-20 22:21:37.263 | MS1 | 121.4656615109 | 31.1446315210 | 221 | 504990 | -92.02 | -2.09 | 26.87 | 0.08 | 1.35 | 1572 |
| 2024-09-20 22:21:38.727 | MS1 | 121.4656689934 | 31.1446308993 | 221 | 504990 | -91.74 | -2.97 | 66.81 | 0.02 | 1.47 | 1568 |
| 2024-09-20 22:21:39.837 | MS1 | 121.4656628039 | 31.1446228751 | 704 | 504990 | -80.76 | 14.44 | 179.10 | 0.01 | 1.32 | 1560 |
| 2024-09-20 22:21:40.145 | MS1 | 121.4656608063 | 31.1446257600 | 704 | 504990 | -82.13 | 16.59 | 340.53 | 0.05 | 2.62 | 1590 |
| 2024-09-20 22:21:41.647 | MS1 | 121.4656756068 | 31.1446264138 | 704 | 504990 | -83.51 | 12.58 | 526.53 | 0.12 | 2.76 | 1598 |
| 2024-09-20 22:21:42.949 | MS1 | 121.4656752778 | 31.1446223748 | 704 | 504990 | -84.68 | 12.45 | 340.01 | 0.15 | 2.48 | 1580 |

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
| 3220132 | 1 | 121.4747543832 | 31.1550984585 | 263 | 4 | 12 | 20.2 | TDD | 704 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |
| 3238550 | 2 | 121.4742504262 | 31.1520472996 | 154 | 9 | 7 | 28.4 | TDD | 137 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3261077 | 4 | 121.4666744978 | 31.1470478710 | 112 | 0 | 4 | 49.7 | TDD | 221 | n41 | 504990 | 100M | 64T64R | 10 | 504990 |
| 3279217 | 3 | 121.4686951368 | 31.1477198009 | 157 | 10 | 6 | 17.4 | TDD | 517 | n41 | 504990 | 100M | 64T64R | 27 | 504990 |

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
| 2024-09-20 22:21:31.611 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:31.631 | NRRandomAccessSuc | Delay：20ms |
| 2024-09-20 22:21:31.762 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:31.762 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |
| 2024-09-20 22:21:38.467 | NREventA3 | measId:2;ServCellPCI:429;Se... |
| 2024-09-20 22:21:38.707 | NRHandoverAttempt | SourcePCI:429;SourceNR-ARFC... |
| 2024-09-20 22:21:38.750 | NRRandomAccessAttempt |  |
| 2024-09-20 22:21:38.762 | NRRandomAccessSuc | Delay：12ms |
| 2024-09-20 22:21:38.874 | NREventA2MeasConfig | measId:1;NR-ARFCN:504990;a2... |
| 2024-09-20 22:21:38.874 | NREventA3MeasConfig | measId:2;NR-ARFCN:504990;a3... |

**트래픽 통계 (Traffic Data)**

| Day\Hour | gNodeB_ID | Cell_ID | Uplink PRB utilization(%) | Downlink PRB utilizati... | Uplink PRB Interferenc... | User Uplink Throughput... | User Downlink Throughp... | Downlink Weak Coversge... | TA>1KM Ratio |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2024_09_20 22:00 | 3220132 | 1 | 16.0819 | 13.3495 | -114.1132 | 12.5054 | 173.5983 | 0.0146 | 0.0033 |
| 2024_09_20 22:00 | 3238550 | 2 | 18.3752 | 16.3937 | -114.4485 | 15.2676 | 186.9587 | 0.0096 | 0.0036 |
| 2024_09_20 22:00 | 3279217 | 3 | 12.9036 | 11.8778 | -116.9686 | 19.0243 | 115.1027 | 0.0176 | 0.0164 |
| 2024_09_20 22:00 | 3261077 | 4 | 5.2024 | 7.7145 | -116.2698 | 6.6526 | 120.4052 | 0.0023 | 0.1892 |

> *... 4개 열 생략 (전체 14열)*

**MR (Measurement Report)**

| Call_ID | Serving ARFCN | Serving PCI | Serving RSRP(dBm) | Neighbor 1 ARFCN | Neighbor 1 PCI | Neighbor 1 RSRP(dBm) | Neighbor 2 ARFCN | Neighbor 2 PCI | Neighbor 2 RSRP(dBm) | Neighbor 3 ARFCN | Neighbor 3 PCI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| MR_1774412825_179D2F8A | 504990 | 704 | -80.5 | 504990 | 221 | -84.0 | 504990 | 137 | -82.9 | 504990 | 517 |
| MR_1774412825_0D5BBBBD | 504990 | 704 | -81.7 | 504990 | 221 | -84.2 | 504990 | 137 | -85.0 | 504990 | 517 |
| MR_1774412825_935583C6 | 504990 | 221 | -83.3 | 504990 | 704 | -80.2 | 504990 | 137 | -81.2 | 504990 | 517 |
| MR_1774412825_26D46768 | 504990 | 704 | -80.4 | 504990 | 221 | -86.2 | 504990 | 137 | -84.3 | 504990 | 517 |
| MR_1774412825_CFC218A5 | 504990 | 704 | -79.2 | 504990 | 221 | -86.6 | 504990 | 137 | -85.0 | 504990 | 517 |
| MR_1774412825_509E17D7 | 504990 | 221 | -86.5 | 504990 | 704 | -81.4 | 504990 | 137 | -84.7 | 504990 | 517 |

> *... 2개 열 생략 (전체 14열)*

---
